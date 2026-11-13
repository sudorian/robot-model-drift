"""Name-first matching, conservative tree fallback and quantity-level comparisons."""
from collections import Counter
import numpy as np
from .compare import Tolerances
from .provenance import class_with_provenance
from .kinematics import check as check_kinematics, align, COM_QUANTITIES


def body_mapping(a, b):
    mapping = {name: name for name in a["bodies"] if name in b["bodies"]}
    methods = {name: "name" for name in mapping}
    child_maps={}
    for snapshot in (a,b):
        child_maps[id(snapshot)]={}
        for n,body in snapshot['bodies'].items():
            child_maps[id(snapshot)].setdefault(body['parent'],[]).append(n)
    signatures={}
    def important(snapshot,name):
        return snapshot['bodies'][name]['mass']>1e-12 or any(j['body']==name for j in snapshot['joints'].values())
    def physical_parent(snapshot,name):
        parent=snapshot['bodies'][name]['parent']
        while parent in snapshot['bodies'] and not important(snapshot,parent):
            parent=snapshot['bodies'][parent]['parent']
        return parent
    def children(snapshot, name):
        found=[]
        for child in child_maps[id(snapshot)].get(name,[]):
            if important(snapshot,child):found.append(child)
            else:found.extend(children(snapshot,child))
        return found
    def signature(snapshot, name, depth=0):
        key=id(snapshot),name
        if key in signatures:
            return signatures[key]
        own = sorted(j.get("type", -1) for j in snapshot["joints"].values() if j["body"] == name)
        if depth > 25:
            return (tuple(own), ())
        signatures[key]=(tuple(own), tuple(sorted(signature(snapshot, child, depth+1) for child in children(snapshot, name))))
        return signatures[key]
    # Only unique subtrees with compatible already-matched parents are accepted.
    changed = True
    while changed:
        changed = False
        for name, body in a["bodies"].items():
            if name in mapping:
                continue
            parent = physical_parent(a,name)
            candidates = []
            for other, obody in b["bodies"].items():
                if important(a,name)!=important(b,other):
                    continue
                if other in mapping.values() or signature(a, name) != signature(b, other):
                    continue
                other_parent=physical_parent(b,other)
                if parent in mapping and other_parent != mapping[parent]:
                    continue
                if parent not in a["bodies"] and other_parent in b["bodies"]:
                    continue
                candidates.append(other)
            reverse = [n for n in a["bodies"] if n not in mapping and signature(a,n) == signature(a,name)]
            if len(candidates) == 1 and len(reverse) == 1:
                mapping[name] = candidates[0]
                methods[name] = "unique kinematic subtree"
                changed = True
    return mapping, methods


def match(a, b):
    bodies, methods = body_mapping(a, b)
    joints = {name: name for name in a["joints"] if name in b["joints"]}
    jmethods = {name: "name" for name in joints}
    for name, joint in a["joints"].items():
        if name in joints:
            continue
        candidates = [n for n,j in b["joints"].items() if n not in joints.values() and
                      j["body"] == bodies.get(joint["body"]) and j.get("type") == joint.get("type") and
                      np.allclose(j.get("axis", [0,0,1]), joint.get("axis", [0,0,1]), atol=1e-6)]
        if len(candidates) == 1:
            joints[name] = candidates[0]
            jmethods[name] = "unique joint on matched body with same type and axis"
    return {"bodies": bodies, "joints": joints, "body_methods": methods, "joint_methods": jmethods,
            "unmatched_m_bodies": sorted(set(a["bodies"])-set(bodies)),
            "unmatched_upstream_bodies": sorted(set(b["bodies"])-set(bodies.values())),
            "unmatched_m_joints": sorted(set(a["joints"])-set(joints)),
            "unmatched_upstream_joints": sorted(set(b["joints"])-set(joints.values()))}


def quantity_rows(m, other, mapping,anchor=None):
    yield {"entity": "robot", "quantity": "total_mass", "tolerance": "mass", "m": m["total_mass"], "other": other["total_mass"], "other_entity": "robot"}
    # Use the first matched physical frame as common world origin/orientation.
    # This also removes a URDF's massless root scaffold placement.
    anchor=anchor if anchor in mapping['bodies'] else next(iter(mapping['bodies']),None)
    def register(snapshot,point,name):
        if name is None:
            return point
        body=snapshot['bodies'][name]
        rotation=np.asarray(body.get('rotation_registered',np.eye(3)))
        return (rotation.T @ (np.asarray(point)-np.asarray(body.get('position_registered',[0,0,0])))).tolist()
    if 'total_com_registered' in m and 'total_com_registered' in other:
        yield {"entity":"robot","quantity":"total_com_registered","tolerance":"com",
               "m":register(m,m['total_com_registered'],anchor),
               "other":register(other,other['total_com_registered'],mapping['bodies'].get(anchor)),"other_entity":"robot"}
    for name, b in m["bodies"].items():
        target = mapping["bodies"].get(name)
        if target is None:
            continue
        ob = other["bodies"][target]
        for field, tolerance in (("mass","mass"), ("subtree_mass","mass"), ("com_registered","com"), ("principal_moments","inertia")):
            av,bv=b[field],ob[field]
            if field=='com_registered':
                av=register(m,av,anchor);bv=register(other,bv,mapping['bodies'].get(anchor))
            yield {"entity": name, "other_entity": target, "quantity": field, "tolerance": tolerance, "m": av, "other": bv}
    for name, j in m["joints"].items():
        target = mapping["joints"].get(name)
        if target is None:
            continue
        oj = other["joints"][target]
        for field, tolerance in (("range","range"), ("effort","limit"), ("force","limit"), ("velocity","limit")):
            if field=='range' and j.get('type')==2:
                tolerance='slide_range'
            yield {"entity": name, "other_entity": target, "quantity": field, "tolerance": tolerance, "m": j.get(field), "other": oj.get(field)}


def source_match(m, other, tolerances=Tolerances()):
    mapping = match(m, other)
    comparable = [r for r in quantity_rows(m, other, mapping) if r["m"] is not None and r["other"] is not None]
    mismatch = [r for r in comparable if not tolerances.close(r["m"],r["other"],r["tolerance"])]
    # Additional zero-mass sensor frames do not invalidate a physical match; disclose
    # them. Unmatched physical bodies or movable joints do invalidate one.
    unphysical = any(other["bodies"][n]["mass"] > tolerances.mass_absolute for n in mapping["unmatched_upstream_bodies"])
    complete = not mapping["unmatched_m_bodies"] and not mapping["unmatched_m_joints"] and not mapping["unmatched_upstream_joints"] and not unphysical
    return {"matches": complete and not mismatch, "mismatch_count": len(mismatch), "mapping": mapping,
            "comparable_quantities": len(comparable), "mismatches": mismatch}


def compare(m, s, h, method, tolerances=Tolerances(), documented_keys=()):
    hm = match(m,h)
    sm = match(m,s) if s else None
    common=[name for name in m['bodies'] if name in hm['bodies'] and (sm is None or name in sm['bodies'])]
    anchor=common[0] if common else None
    hm['registration_anchor']={'M':anchor,'H':hm['bodies'].get(anchor),'root_unmatched':anchor!=next(iter(m['bodies']),None)}
    if sm:sm['registration_anchor']={'M':anchor,'S':sm['bodies'].get(anchor)}
    kinematics={'M/H':check_kinematics(m,h,hm,tolerances,anchor)}
    if sm:kinematics['M/S']=check_kinematics(m,s,sm,tolerances,anchor)
    com_eligible=all(k['com_eligible'] for k in kinematics.values())
    srows = {(r["entity"],r["quantity"]):r for r in quantity_rows(m,s,sm,anchor)} if s else {}
    rows, unavailable = [], []
    for row in quantity_rows(m,h,hm,anchor):
        key = row["entity"],row["quantity"]
        sv = srows.get(key,{}).get("other")
        if row["m"] is None or row["other"] is None:
            unavailable.append({**row,"s":sv,"reason":"quantity absent or not enforced/declared on one side"})
            continue
        raw_values=None
        raw_class=None
        if row['quantity'] in COM_QUANTITIES:
            raw_values={'m':row['m'],'s':sv,'h':row['other']}
            raw_class=class_with_provenance(row['m'],sv,row['other'],row['tolerance'],method,tolerances,key in documented_keys)
            if com_eligible:
                row['other']=align(row['other'],kinematics['M/H'])
                if sv is not None:sv=align(sv,kinematics['M/S'])
        value = class_with_provenance(row["m"],sv,row["other"],row["tolerance"],method,tolerances,key in documented_keys)
        hv=row.pop('other')
        difference = np.asarray(hv)-np.asarray(row["m"])
        changed = not tolerances.close(row["m"],hv,row["tolerance"])
        record={**row,"h":hv,"s":sv,"source_entity":srows.get(key,{}).get("other_entity"),
                     "class":value,"h_minus_m":difference.tolist(),"absolute_difference":float(np.max(np.abs(difference))),
                     "m_h_changed":changed,"tolerance_multiple":tolerances.ratio(row['m'],hv,row['tolerance'])}
        if raw_values is not None:
            record.update(raw_values=raw_values,raw_class=raw_class,com_aligned=com_eligible,
                          excluded_from_findings=not com_eligible)
            if not com_eligible:
                record['exclusion_reason']='; '.join(label+': '+k['status'] for label,k in kinematics.items() if not k['com_eligible'])
        rows.append(record)
    candidates = [r for r in rows if r["class"].removesuffix(" (inferred)") != "unchanged" and (r['class'].removesuffix(' (inferred)') not in ('NO MATCHING SOURCE','unknown') or r["m_h_changed"])]
    findings=[r for r in candidates if not r.get('excluded_from_findings')]
    return {"rows":rows,"findings":findings,"counts":dict(Counter(r["class"] for r in findings)),"mapping_h":hm,
            "mapping_s":sm,"unavailable":unavailable,"kinematics":kinematics,
            "excluded_findings":[r for r in candidates if r.get('excluded_from_findings')]}
