"""Independent XML physical-quantity extraction. Never imports MuJoCo."""
import json
import math
from pathlib import PurePosixPath
import random
import xml.etree.ElementTree as ET
import numpy as np
from .sources import GitSource
from .network import ROOT,log
from .publication import public_data,public_text


def direct_root(source,commit,path,arguments=None,main_path=None):
    text=source.read(commit,path)
    if 'xacro:' in text or path.endswith('.xacro'):
        # Share only the prescribed third-party input preprocessor; all physical
        # extraction, tree transforms and arithmetic below are independent.
        from .loader import expand_xacro
        return ET.fromstring(expand_xacro(source,commit,path,dict(arguments or {})))
    root=ET.fromstring(text)
    main_path=main_path or path
    for parent in list(root.iter()):
        for child in list(parent):
            if child.tag=='include':
                import posixpath
                target=posixpath.normpath(str(PurePosixPath(path).parent/child.get('file')))
                known=source.git('ls-tree','-r','--name-only',commit).splitlines()
                if target not in known:
                    root_relative=posixpath.normpath(str(PurePosixPath(main_path).parent/child.get('file')))
                    if root_relative in known:target=root_relative
                included=direct_root(source,commit,target,arguments,main_path)
                i=list(parent).index(child);parent.remove(child)
                for n,node in enumerate(list(included)):
                    parent.insert(i+n,node)
    return root


def vector(value,default):
    return np.array([float(v) for v in value.split()]) if value else np.array(default,dtype=float)


def axis_rotation(axis,angle):
    axis=np.array(axis,dtype=float);axis/=np.linalg.norm(axis)
    x,y,z=axis;c,s=math.cos(angle),math.sin(angle)
    return c*np.eye(3)+(1-c)*np.outer(axis,axis)+s*np.array([[0,-z,y],[z,0,-x],[-y,x,0]])


def quaternion(value):
    q=vector(value,[1,0,0,0]);q/=np.linalg.norm(q);w,x,y,z=q
    return np.array([[1-2*(y*y+z*z),2*(x*y-z*w),2*(x*z+y*w)],
                     [2*(x*y+z*w),1-2*(x*x+z*z),2*(y*z-x*w)],
                     [2*(x*z-y*w),2*(y*z+x*w),1-2*(x*x+y*y)]])


def rotation(attrs,angle_scale=1,euler_sequence='xyz',urdf=False):
    if 'quat' in attrs:
        return quaternion(attrs['quat'])
    if 'axisangle' in attrs:
        a=vector(attrs['axisangle'],[0,0,1,0]);return axis_rotation(a[:3],a[3]*angle_scale)
    if 'euler' in attrs or 'rpy' in attrs:
        values=vector(attrs.get('euler',attrs.get('rpy')),[0,0,0])*angle_scale
        rotations=[axis_rotation(np.eye(3)[i],values[i]) for i in range(3)]
        if urdf:
            return rotations[2]@rotations[1]@rotations[0]
        result=np.eye(3)
        for letter,angle in zip(euler_sequence,values):
            r=axis_rotation(np.eye(3)['xyz'.index(letter.lower())],angle)
            result=result@r if letter.islower() else r@result
        return result
    if 'xyaxes' in attrs:
        a=vector(attrs['xyaxes'],[1,0,0,0,1,0]);x=a[:3]/np.linalg.norm(a[:3]);y=a[3:]-x*np.dot(x,a[3:]);y/=np.linalg.norm(y)
        return np.column_stack((x,y,np.cross(x,y)))
    if 'zaxis' in attrs:
        z=vector(attrs['zaxis'],[0,0,1]);z/=np.linalg.norm(z);axis=np.cross([0,0,1],z)
        return axis_rotation(axis,math.acos(np.clip(z[2],-1,1))) if np.linalg.norm(axis)>1e-12 else (np.eye(3) if z[2]>0 else np.diag([1,-1,-1]))
    return np.eye(3)


def physical_xml(view):
    source=GitSource(view['cache'],view['repo'])
    root=direct_root(source,view['commit'],view['file'],view.get('snapshot',{}).get('xacro_arguments'))
    compiler=root.find('mujoco/compiler') if root.tag=='robot' else root.find('compiler')
    compiler_attrs=compiler.attrib if compiler is not None else {}
    bodies,joints={},{}
    if root.tag=='robot':
        links={l.get('name'):l for l in root.findall('link')}
        edges={j.find('child').get('link'):j for j in root.findall('joint') if j.find('child') is not None}
        def visit(name):
            if name in bodies:return
            item=links[name];edge=edges.get(name)
            if edge is None:p=np.zeros(3);r=np.eye(3);parent=None
            else:
                parent=edge.find('parent').get('link');visit(parent)
                origin=edge.find('origin');attrs=origin.attrib if origin is not None else {}
                p=bodies[parent]['p']+bodies[parent]['r']@vector(attrs.get('xyz'),[0,0,0])
                r=bodies[parent]['r']@rotation(attrs,urdf=True)
                if edge.get('type') not in ('fixed','floating'):
                    limit=edge.find('limit')
                    ranges=[float(limit.get('lower')),float(limit.get('upper'))] if limit is not None and edge.get('type')!='continuous' and 'lower' in limit.attrib and 'upper' in limit.attrib else None
                    joints[edge.get('name')]={'range':ranges,'body':name,'effort':float(limit.get('effort')) if limit is not None and 'effort' in limit.attrib else None,
                        'velocity':float(limit.get('velocity')) if limit is not None and 'velocity' in limit.attrib else None,'force':None}
            inertial=item.find('inertial');mass=None;moments=None;com=p.copy()
            if inertial is not None:
                mass_item=inertial.find('mass');mass=float(mass_item.get('value')) if mass_item is not None else None
                origin=inertial.find('origin');com=p+r@vector(origin.get('xyz') if origin is not None else None,[0,0,0])
                tensor=inertial.find('inertia')
                if tensor is not None:
                    a=tensor.attrib
                    matrix=np.array([[float(a['ixx']),float(a['ixy']),float(a['ixz'])],[float(a['ixy']),float(a['iyy']),float(a['iyz'])],[float(a['ixz']),float(a['iyz']),float(a['izz'])]])
                    moments=np.linalg.eigvalsh(matrix).tolist()
            elif item.find('visual') is None and item.find('collision') is None:
                mass=0.;moments=[0.,0.,0.]
            bodies[name]={'p':p,'r':r,'parent':parent,'mass':mass,'com':com,'principal_moments':moments,'com_inferred':mass is None}
        for name in links:visit(name)
    else:
        compiler=root.find('compiler');attrs=compiler.attrib if compiler is not None else {}
        scale=1 if attrs.get('angle','degree')=='radian' else math.pi/180
        sequence=attrs.get('eulerseq','xyz')
        defaults={}
        def read_defaults(node,inherited=None):
            values={tag:dict(a) for tag,a in (inherited or {}).items()}
            for child in node:
                if child.tag!='default':values.setdefault(child.tag,{}).update(child.attrib)
            defaults[node.get('class','main')]=values
            for child in node.findall('default'):read_defaults(child,values)
        for node in root.findall('default'):read_defaults(node)
        def attributes(node,childclass='main'):
            group=defaults.get(node.get('class',childclass),{})
            d=dict(group.get('general',{})) if node.tag in ('motor','position','velocity','general','muscle','cylinder','damper','intvelocity','adhesion') else {}
            d.update(group.get(node.tag,{}));d.update(node.attrib);return d
        def visit(item,parent=None,childclass='main'):
            a=attributes(item,childclass);name=a.get('name')
            if name is None:raise ValueError('Unnamed body is not eligible for independent matching')
            parent_r=bodies[parent]['r'] if parent else np.eye(3);parent_p=bodies[parent]['p'] if parent else np.zeros(3)
            p=parent_p+parent_r@vector(a.get('pos'),[0,0,0]);r=parent_r@rotation(a,scale,sequence)
            ownclass=a.get('childclass',childclass)
            for joint in item.findall('joint'):
                j=attributes(joint,ownclass);kind=j.get('type','hinge');axis=vector(j.get('axis'),[0,0,1]);ref=float(j.get('ref',0))
                if kind=='hinge' and ref:
                    local=vector(j.get('pos'),[0,0,0]);old=r;r=r@axis_rotation(axis,-ref*scale);p=p+old@local-r@local
                elif kind=='slide' and ref:p=p+r@axis*(-ref)
                if j.get('name') and kind in ('hinge','slide'):
                    ranges=vector(j['range'],[0,0]).tolist() if 'range' in j and j.get('limited')!='false' else None
                    if ranges and kind=='hinge':ranges=[x*scale for x in ranges]
                    joints[j['name']]={'range':ranges,'body':name,'effort':None,'force':None,'velocity':None,'attrs':j}
            inertial=item.find('inertial');mass=None;moments=None;com=p.copy()
            if inertial is not None:
                ia=inertial.attrib;mass=float(ia['mass']);com=p+r@vector(ia.get('pos'),[0,0,0])
                if 'diaginertia' in ia:moments=sorted(vector(ia['diaginertia'],[0,0,0]).tolist())
                elif 'fullinertia' in ia:
                    xx,yy,zz,xy,xz,yz=vector(ia['fullinertia'],[0]*6);moments=np.linalg.eigvalsh([[xx,xy,xz],[xy,yy,yz],[xz,yz,zz]]).tolist()
            elif not item.findall('geom'):
                mass=0.;moments=[0.,0.,0.]
            bodies[name]={'p':p,'r':r,'parent':parent,'mass':mass,'com':com,'principal_moments':moments,'com_inferred':mass is None}
            for child in item.findall('body'):visit(child,name,ownclass)
        world=root.find('worldbody')
        if world is None:raise ValueError('No standalone worldbody')
        for item in world.findall('body'):visit(item)
        actuators=root.find('actuator')
        if actuators is not None:
            limits={}
            for actuator in actuators:
                a=attributes(actuator);name=a.get('joint')
                if name not in joints:continue
                envelope=None
                if 'forcerange' in a and a.get('forcelimited')!='false':envelope=vector(a['forcerange'],[0,0])
                elif actuator.tag=='motor' and 'ctrlrange' in a and a.get('ctrllimited')!='false':envelope=vector(a['ctrlrange'],[0,0])
                elif actuator.tag=='general' and 'ctrlrange' in a and a.get('gaintype','fixed')=='fixed' and a.get('biastype','none')=='none':envelope=vector(a['ctrlrange'],[0,0])*vector(a.get('gainprm'),[1])[0]
                if envelope is not None:limits.setdefault(name,[]).append(float(max(abs(envelope))*abs(vector(a.get('gear'),[1])[0])))
            for name,values in limits.items():
                if len(values)==1:joints[name]['effort']=values[0];joints[name]['force']=values[0]
        for joint in joints.values():
            a=joint.get('attrs',{})
            if 'actuatorfrcrange' in a and a.get('actuatorfrclimited')!='false':joint['force']=float(max(abs(vector(a['actuatorfrcrange'],[0,0]))))
    force_geometry=compiler_attrs.get('inertiafromgeom')=='true'
    for body in bodies.values():
        if force_geometry:
            body['mass']=None;body['principal_moments']=None;body['com_inferred']=True
            continue
        if body['mass'] is not None:
            body['mass']=max(body['mass'],float(compiler_attrs.get('boundmass',0)))
        if body['principal_moments'] is not None:
            moments=np.maximum(body['principal_moments'],float(compiler_attrs.get('boundinertia',0)))
            if compiler_attrs.get('balanceinertia')=='true' and moments.max()>moments.sum()-moments.max():
                moments[:]=moments.mean()
            body['principal_moments']=sorted(moments.tolist())
    desired=float(compiler_attrs.get('settotalmass',0))
    if desired>0:
        if any(b['mass'] is None for b in bodies.values()):
            raise ValueError('settotalmass requires geometry-derived contributions')
        factor=desired/sum(b['mass'] for b in bodies.values())
        for body in bodies.values():
            body['mass']*=factor
            if body['principal_moments'] is not None:body['principal_moments']=[v*factor for v in body['principal_moments']]
    return bodies,joints


def extract(view,entity,quantity,anchor=None):
    bodies,joints=physical_xml(view)
    anchor=anchor or next(iter(bodies))
    def registered(point):return (bodies[anchor]['r'].T@(point-bodies[anchor]['p'])).tolist()
    def subtree(name):
        values=[body['mass'] for n,body in bodies.items() if n==name or descendant(n,name)]
        if any(v is None for v in values):raise ValueError('Subtree includes geometry-inferred mass')
        return sum(values)
    def descendant(name,ancestor):
        parent=bodies[name]['parent']
        return parent is not None and (parent==ancestor or descendant(parent,ancestor))
    if entity=='robot':
        masses=[body['mass'] for body in bodies.values()]
        if any(m is None for m in masses):raise ValueError('Aggregate includes geometry-inferred masses')
        if quantity=='total_mass':return sum(masses)
        if quantity=='total_com_registered':return registered(sum(body['com']*body['mass'] for body in bodies.values())/sum(masses))
    if quantity in ('range','effort','force','velocity') and entity in joints and joints[entity].get(quantity) is not None:
        return joints[entity][quantity]
    if entity in bodies:
        body=bodies[entity]
        if quantity=='com_registered':
            if body.get('com_inferred'):raise ValueError('CoM is geometry-derived')
            return registered(body['com'])
        if quantity=='subtree_mass':return subtree(entity)
        if quantity in ('mass','principal_moments') and body[quantity] is not None:return body[quantity]
        raise ValueError('Quantity requires geometry-derived inertia/mass')
    if entity in joints and joints[entity].get(quantity) is not None:return joints[entity][quantity]
    raise ValueError('No directly extractable XML value')


def direct_values(result,row):
    """Recompute values and any CoM fit entirely from XML FK, not cached R/t."""
    comparison=result['comparison']
    mapping=comparison['mapping_h']['bodies']
    anchor=comparison['mapping_h'].get('registration_anchor',{}).get('M') or next(iter(mapping),None)
    values={'m':extract(result['menagerie'],row['entity'],row['quantity'],anchor),
            'h':extract(result['upstream'],row['other_entity'],row['quantity'],mapping.get(anchor)),'s':None}
    if row['s'] is not None and result.get('source_view'):
        sm=comparison['mapping_s']['bodies']
        values['s']=extract(result['source_view'],row['source_entity'],row['quantity'],sm.get(anchor))
    if row.get('com_aligned'):
        mb,_=physical_xml(result['menagerie'])
        for label,key,mapping_key in (('h','upstream','mapping_h'),('s','source_view','mapping_s')):
            if values[label] is None:continue
            ob,_=physical_xml(result[key]);matched=comparison[mapping_key]['bodies']
            other_anchor=matched[anchor]
            a=np.array([mb[anchor]['r'].T@(mb[n]['p']-mb[anchor]['p']) for n in matched])
            b=np.array([ob[other_anchor]['r'].T@(ob[n]['p']-ob[other_anchor]['p']) for n in matched.values()])
            ac,bc=a.mean(0),b.mean(0)
            u,_,vt=np.linalg.svd((b-bc).T@(a-ac))
            sign=np.eye(3);sign[2,2]=1 if np.linalg.det(vt.T@u.T)>=0 else -1
            rotation=vt.T@sign@u.T
            values[label]=(rotation@(np.asarray(values[label])-bc)+ac).tolist()
    return values


def cross_check(results,seed=20261113):
    # Randomize all reported differences first, then disclose any non-verifiable
    # draws. This supports all quantity families, including independent FK/eigenvalues.
    candidates=[(result,row) for result in results for row in result.get('comparison',{}).get('findings',[])]
    random.Random(seed).shuffle(candidates)
    checks,excluded=[],[]
    for result,row in candidates:
        if len(checks)==3:break
        try:
            values=direct_values(result,row)
            mv,sv,hv=(values[k] for k in ('m','s','h'))
            agree=bool(np.allclose(mv,row['m'],rtol=1e-9,atol=1e-9) and np.allclose(hv,row['h'],rtol=1e-9,atol=1e-9) and (sv is None or np.allclose(sv,row['s'],rtol=1e-9,atol=1e-9)))
            checks.append({'model':result['model'],'entity':row['entity'],'quantity':row['quantity'],'compiled':{k:row[k] for k in ('m','s','h')},'direct_xml':{'m':mv,'s':sv,'h':hv},'agree':agree})
        except Exception as exc:
            excluded.append({'model':result['model'],'entity':row['entity'],'quantity':row['quantity'],'reason':str(exc)})
    output={'seed':seed,'all_reported_findings':len(candidates),'selection':'shuffle every finding without replacement; inspect in this order until three are independently extractable; every skipped draw recorded','checks':checks,'skipped_draws':excluded}
    (ROOT/'report/cross_checks.json').write_text(json.dumps(public_data(output, ROOT),indent=2)+'\n')
    lines=['# Three independent XML cross-checks','',f"Random seed: {seed}. Reported differences shuffled: {len(candidates)}. Physical values are computed directly from XML without importing MuJoCo. The independent parser handles masses, subtrees, FK/world CoM, inertia eigenvalues, ranges and supported limits. Eligible CoM rigid fits are independently recomputed from XML body origins, without reusing cached transforms. Excluded convention/coverage CoM records are outside the finding population. Xacro uses the prescribed input-expansion package. Every skipped non-extractable draw is recorded in JSON.",'','| Model / entity / quantity | Compiled M / S / H | Direct XML M / S / H | Agree? |','|---|---|---|---|']
    for c in checks:lines.append(f"| {c['model']} / {c['entity']} / {c['quantity']} | {json.dumps(c['compiled'])} | {json.dumps(c['direct_xml'])} | {'yes' if c['agree'] else 'NO'} |")
    lines+=['','Full sample and skipped draws: `report/cross_checks.json`.']
    (ROOT/'report/cross_checks.md').write_text(public_text('\n'.join(lines)+'\n', ROOT))
    log(f"Direct XML random cross-checks: {len(checks)} selected, seed {seed}; agreements {[c['agree'] for c in checks]}; skipped draws {len(excluded)}.")
    return output


if __name__=='__main__':
    result=cross_check(json.loads((ROOT/'report/results.json').read_text()))
    print(json.dumps(result,indent=2))


def audit_stale(results):
    """Extra independent audit of the full counted STALE set."""
    from .compare import Tolerances
    from .provenance import class_with_provenance
    checks=[]
    for result in results:
        for row in result.get('comparison',{}).get('findings',[]):
            if row['class'].removesuffix(' (inferred)')!='STALE':continue
            c={'model':result['model'],'entity':row['entity'],'quantity':row['quantity'],
               'compiled':{k:row[k] for k in ('m','s','h')}}
            try:
                values=direct_values(result,row)
                c['direct_xml']=values
                c['direct_class']=class_with_provenance(values['m'],values['s'],values['h'],row['tolerance'],result['source']['method'],Tolerances(**result['tolerances']))
                c['agree']=all(np.allclose(values[k],row[k],rtol=1e-9,atol=1e-9) for k in values) and c['direct_class']==row['class']
            except Exception as exc:c.update(error=f'{type(exc).__name__}: {exc}',agree=False)
            checks.append(c)
    output={'scope':'Every counted STALE record, separate from the seeded random sample',
            'implementation':'Direct XML quantities and FK; CoM Kabsch independently recomputed from XML origins, not cached transforms; no MuJoCo import',
            'checks':checks}
    (ROOT/'report/stale_cross_checks.json').write_text(json.dumps(public_data(output, ROOT),indent=2)+'\n')
    lines=['# Direct XML checks of every STALE record','',f"Agreements: {sum(c['agree'] for c in checks)}/{len(checks)}. Eligible CoM alignment is independently fitted from XML origins. Excluded convention/coverage records are not counted STALE.",'','| Model / entity / quantity | Direct class | Agree? |','|---|---|---|']
    for c in checks:lines.append(f"| {c['model']} / {c['entity']} / {c['quantity']} | {c.get('direct_class',c.get('error'))} | {c['agree']} |")
    lines+=['','Exact compiled and independent values: `report/stale_cross_checks.json`.']
    (ROOT/'report/stale_cross_checks.md').write_text(public_text('\n'.join(lines)+'\n', ROOT))
    log(f"Every-STALE independent XML audit: {sum(c['agree'] for c in checks)}/{len(checks)} agree; CoM fits independently recomputed from XML origins.")
    return output
