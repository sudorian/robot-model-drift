"""Offline H1 acceptance diagnostic. Reads cloned Git objects; never uses network.

Source files and meshes remain in ignored Git object stores or process memory.
No source XML is copied into the project.
"""
from __future__ import annotations
import json
import os
from pathlib import Path, PurePosixPath
import subprocess
import xml.etree.ElementTree as ET
import numpy as np
import mujoco
import hashlib
from collections import OrderedDict
from .compare import Tolerances, classify
from .publication import public_data


from .sources import GitSource

_compiled_inputs=OrderedDict()


def explicit_mass_sum(text):
    """Independent direct XML diagnostic, not a replacement for compilation."""
    root = ET.fromstring(text)
    if root.tag == "robot":
        try:
            return sum(float(i.attrib["value"]) for i in root.findall("link/inertial/mass"))
        except ValueError:
            return None # unexpanded expressions have no literal XML sum
    try:
        return sum(float(i.attrib["mass"]) for i in root.findall("worldbody//inertial"))
    except ValueError:
        return None


def _compile_model(xml,assets):
    from collections import Counter
    warnings=[]
    mujoco.set_mju_user_warning(warnings.append)
    try:
        model=mujoco.MjModel.from_xml_string(xml,assets)
    finally:
        mujoco.set_mju_user_warning(None)
        if warnings:
            from .network import log
            log('MuJoCo compiler warnings: '+json.dumps(dict(Counter(warnings))))
    return model,warnings


def compile_snapshot(source, commit, path, strip_geometry=None, arguments=None):
    from .loader import prepare
    text = source.read(commit, path)
    root, assets, metadata = prepare(source, commit, path, strip_geometry, arguments)
    serialized=ET.tostring(root,encoding='unicode')
    digest=hashlib.sha256(serialized.encode())
    for name,blob in sorted(assets.items()):
        digest.update(name.encode());digest.update(hashlib.sha256(blob).digest())
    fingerprint=digest.hexdigest()
    if fingerprint in _compiled_inputs:
        _compiled_inputs.move_to_end(fingerprint)
        result={**_compiled_inputs[fingerprint],**metadata,'compilation_cache_hit':True,
                'direct_xml_explicit_mass':explicit_mass_sum(text)}
        return result
    model,compiler_warnings = _compile_model(serialized, assets)
    if model.nbody<2 or float(model.body_mass.sum())<=0:
        raise ValueError('XML has no robot bodies; it is an include/extension fragment, not a standalone source')
    data = mujoco.MjData(model)
    # Zero scalar joints, retaining valid free/ball quaternions from qpos0.
    for j in range(model.njnt):
        if model.jnt_type[j] in (mujoco.mjtJoint.mjJNT_HINGE, mujoco.mjtJoint.mjJNT_SLIDE):
            data.qpos[model.jnt_qposadr[j]] = 0
    mujoco.mj_forward(model, data)
    body_names = [mujoco.mj_id2name(model, mujoco.mjtObj.mjOBJ_BODY, i) or f"body_{i}" for i in range(model.nbody)]
    bodies = {}
    root_pos = data.xpos[1].copy() if model.nbody > 1 else np.zeros(3)
    root_rot = data.xmat[1].reshape(3,3).copy() if model.nbody > 1 else np.eye(3)
    for i in range(1, model.nbody):
        bodies[body_names[i]] = {
            "mass": float(model.body_mass[i]), "subtree_mass": float(model.body_subtreemass[i]),
            "com_world": data.xipos[i].tolist(), "com_registered": (root_rot.T @ (data.xipos[i]-root_pos)).tolist(), "position_registered": (root_rot.T @ (data.xpos[i]-root_pos)).tolist(), "principal_moments": sorted(model.body_inertia[i].tolist()),
            "parent": body_names[model.body_parentid[i]],
            "rotation_registered": (root_rot.T @ data.xmat[i].reshape(3,3)).tolist(),
        }
    joints = {}
    joint_axes_registered = {}
    for j in range(model.njnt):
        name = mujoco.mj_id2name(model, mujoco.mjtObj.mjOBJ_JOINT, j)
        if model.jnt_type[j] == mujoco.mjtJoint.mjJNT_FREE:
            continue
        joints[name] = {"range": model.jnt_range[j].tolist() if model.jnt_limited[j] else None,
                        "body": body_names[model.jnt_bodyid[j]],
                        "type": int(model.jnt_type[j]), "axis": model.jnt_axis[j].tolist(),
                        "effort": None, "force": None, "velocity": None}
        if model.jnt_type[j] in (mujoco.mjtJoint.mjJNT_HINGE,mujoco.mjtJoint.mjJNT_SLIDE):
            joint_axes_registered[name]=(root_rot.T @ data.xaxis[j]).tolist()
        if root.tag == "robot":
            limit = root.find(f"joint[@name='{name}']/limit")
            if limit is not None:
                for quantity, attr in (("effort", "effort"), ("velocity", "velocity")):
                    if attr in limit.attrib:
                        joints[name][quantity] = float(limit.get(attr))
        elif model.jnt_type[j] != mujoco.mjtJoint.mjJNT_BALL:
            limits = []
            for actuator in range(model.nu):
                if model.actuator_trnid[actuator, 0] != j or model.actuator_trntype[actuator] != 0:
                    continue
                force_range = None
                if model.actuator_forcelimited[actuator]:
                    force_range = model.actuator_forcerange[actuator]
                elif model.actuator_ctrllimited[actuator] and model.actuator_gaintype[actuator] == 0 and model.actuator_biastype[actuator] == 0:
                    force_range = model.actuator_ctrlrange[actuator] * model.actuator_gainprm[actuator, 0]
                if force_range is not None:
                    limits.append(float(max(abs(force_range)) * abs(model.actuator_gear[actuator, 0])))
            if len(limits) == 1:
                joints[name]["effort"] = limits[0]
                joints[name]["force"] = limits[0]
            if model.jnt_actfrclimited[j]:
                joints[name]["force"] = float(max(abs(model.jnt_actfrcrange[j])))
    result = {
        "total_mass": float(model.body_mass.sum()), "bodies": bodies, "joints": joints,
        "joint_axes_registered":joint_axes_registered,
        "total_com_registered": (root_rot.T @ (data.subtree_com[0]-root_pos)).tolist(),
        "total_com_world": data.subtree_com[0].tolist(),
        "compiler_warnings": compiler_warnings,
        "limit_semantics": "URDF effort/velocity declarations are retained metadata, not enforced by MuJoCo" if root.tag=='robot' else "Effort from supported scalar actuator envelopes; force from joint caps or supported envelopes; velocity unavailable unless explicitly represented",
        **metadata, "registration": {"translation": root_pos.tolist(), "rotation": root_rot.tolist()},
        "fusestatic": False, "xacro_arguments": {}, "direct_xml_explicit_mass": explicit_mass_sum(text),
    }
    result.update(metadata)
    result['compiled_input_sha256']=fingerprint
    result['compilation_cache_hit']=False
    _compiled_inputs[fingerprint]=result
    if len(_compiled_inputs)>128:_compiled_inputs.popitem(last=False)
    return result


def run(root,menagerie_ref='370c439',upstream_ref='34e7506'):
    from .provenance import select_source, class_with_provenance
    m = GitSource(root / ".cache/menagerie", "https://github.com/google-deepmind/mujoco_menagerie")
    u = GitSource(root / ".cache/unitree_ros", "https://github.com/unitreerobotics/unitree_ros")
    msha = m.git("rev-parse", menagerie_ref+'^{commit}').strip()
    hsha = u.git("rev-parse", upstream_ref+'^{commit}').strip()
    mp, up = "unitree_h1/h1.xml", "robots/h1_description/urdf/h1.urdf"
    mhistory = m.history(mp)
    # Strict bound: original introduction, not a later light/format/collider edit.
    # Later unrelated edits cannot make a future URDF the original conversion source.
    origin = min(mhistory, key=lambda row: int(row["timestamp"]))
    reachable=set(u.git('log','--format=%H',hsha).splitlines())
    history = [row for row in u.history(up) if row['commit'] in reachable]
    ms = compile_snapshot(m, msha, mp, strip_geometry=True)
    for row in history:
        row["eligible"] = int(row["timestamp"]) <= int(origin["timestamp"])
        row["explicit_mass"] = explicit_mass_sum(u.read(row["commit"], up))
        try:
            row["snapshot"] = compile_snapshot(u, row["commit"], up)
            from .engine import source_match
            row.update(source_match(ms, row["snapshot"]))
        except (ValueError, subprocess.CalledProcessError) as exc:
            row["error"] = str(exc)
            row["matches"] = False
    hs = compile_snapshot(u, hsha, up)
    provenance = select_source(history, origin["timestamp"])
    baseline = provenance["candidate"]["snapshot"]["total_mass"] if provenance["candidate"] else None
    return {
        "status": "passed" if all(not r.get("error") for r in history) else "incomplete",
        "reason": "Reproduced compiled quantities; applied amended provenance rules",
        "menagerie": {"repo": m.url, "commit": msha, "file": mp, "origin": origin, "snapshot": ms},
        "upstream": {"repo": u.url, "commit": hsha, "file": up, "snapshot": hs},
        "source_candidates": history, "source": provenance,
        "three_way_total_mass_class": class_with_provenance(ms["total_mass"], baseline, hs["total_mass"], "mass", provenance["method"], Tolerances()),
        "tolerances": Tolerances().__dict__,
        "mujoco_version": mujoco.__version__,
        "fixture_refs": {'menagerie':menagerie_ref,'upstream':upstream_ref,'purpose':'Fixed acceptance fixture; full survey independently uses current upstream HEAD'},
    }


def main():
    import argparse
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path.cwd())
    parser.add_argument("--output", type=Path, default=Path("report/acceptance.json"))
    args = parser.parse_args()
    result = run(args.root)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(public_data(result, args.root), indent=2) + "\n")
    print(json.dumps({"status": result["status"], "reason": result["reason"], "M": result["menagerie"]["snapshot"]["total_mass"], "H": result["upstream"]["snapshot"]["total_mass"], "class": result["three_way_total_mass_class"]}, indent=2))
    raise SystemExit(2 if result["status"] != "passed" else 0)


if __name__ == "__main__":
    main()
