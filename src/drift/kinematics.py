"""Zero-pose rigid registration and signed joint-axis consistency checks."""
import numpy as np

COM_QUANTITIES = frozenset(('com_registered', 'total_com_registered'))


def frame(snapshot, anchor):
    body = snapshot['bodies'].get(anchor, {})
    return (np.asarray(body.get('position_registered', [0, 0, 0]), dtype=float),
            np.asarray(body.get('rotation_registered', np.eye(3)), dtype=float))


def check(m, other, mapping, tolerances, anchor=None):
    """Fit other to M with proper Kabsch (no reflection), in the report frames.

    The maximum origin residual is the quality threshold; RMS is also recorded.
    Fewer than three
    non-collinear matched origins cannot determine a unique 3-D rotation;
    those cases are unverified, rather than evidence of an axis disagreement.
    """
    names = list(mapping['bodies'])
    anchor = anchor if anchor in mapping['bodies'] else next(iter(names), None)
    mp, mr = frame(m, anchor)
    op, ort = frame(other, mapping['bodies'].get(anchor))
    output = {'status': 'insufficient kinematic coverage', 'matched_body_origins': len(names),
              'position_threshold_m': tolerances.kinematic_residual,
              'axis_threshold_rad': tolerances.kinematic_axis_angle,
              'residual_definition': 'maximum Euclidean residual over matched body origins; Kabsch minimizes RMS, which is also recorded',
              'coordinate_frames': 'each snapshot registered to its matched report anchor',
              'anchor_m': anchor, 'anchor_other': mapping['bodies'].get(anchor),
              'rotation_other_to_m': None, 'translation_other_to_m': None,
              'rms_residual_m': None, 'max_residual_m': None, 'fit_rank': 0,
              'axis_checks': [], 'axis_disagreements': [], 'com_eligible': False}
    if not names or any('position_registered' not in s['bodies'][n] for s, ns in
                        ((m, names), (other, list(mapping['bodies'].values()))) for n in ns):
        output['reason'] = 'No matched origins, or zero-pose body-origin data unavailable'
        return output
    a = np.array([mr.T @ (np.asarray(m['bodies'][n]['position_registered']) - mp) for n in names])
    b = np.array([ort.T @ (np.asarray(other['bodies'][mapping['bodies'][n]]['position_registered']) - op) for n in names])
    ac, bc = a.mean(axis=0), b.mean(axis=0)
    u, singular_values, vt = np.linalg.svd((b - bc).T @ (a - ac))
    correction = np.eye(3)
    correction[2, 2] = 1 if np.linalg.det(vt.T @ u.T) >= 0 else -1
    rotation = vt.T @ correction @ u.T
    translation = ac - rotation @ bc
    residuals = np.linalg.norm(a - (b @ rotation.T + translation), axis=1)
    rank = min(int(np.linalg.matrix_rank(a - ac, tol=1e-9)),
               int(np.linalg.matrix_rank(b - bc, tol=1e-9)))
    output.update(rotation_other_to_m=rotation.tolist(), translation_other_to_m=translation.tolist(),
                  rms_residual_m=float(np.sqrt(np.mean(residuals ** 2))),
                  max_residual_m=float(residuals.max()), fit_rank=rank,
                  covariance_singular_values=singular_values.tolist(),
                  origin_residuals_m={n: float(value) for n, value in zip(names, residuals)})
    if rank < 2:
        if output['max_residual_m'] > tolerances.kinematic_residual:
            output['status'] = 'kinematic convention differs'
            output['reason'] = 'Origin residual exceeds threshold; fitted rotation is also underdetermined'
        else:
            output['reason'] = 'Fewer than three non-collinear matched origins; fitted rotation is underdetermined'
        return output
    for name, target in mapping['joints'].items():
        j, k = m['joints'][name], other['joints'][target]
        # Ball joints have no single signed hinge/slide axis to compare.
        if j['type'] not in (2, 3) or k['type'] not in (2, 3):
            continue
        ma=m.get('joint_axes_registered',{}).get(name)
        oa=other.get('joint_axes_registered',{}).get(target)
        axis_m = mr.T @ (np.asarray(ma) if ma is not None else np.asarray(m['bodies'][j['body']]['rotation_registered']) @ np.asarray(j['axis']))
        axis_other = rotation @ ort.T @ (np.asarray(oa) if oa is not None else np.asarray(other['bodies'][k['body']]['rotation_registered']) @ np.asarray(k['axis']))
        axis_m /= np.linalg.norm(axis_m)
        axis_other /= np.linalg.norm(axis_other)
        angle = float(np.arctan2(np.linalg.norm(np.cross(axis_m, axis_other)), np.dot(axis_m, axis_other)))
        record = {'joint_m': name, 'joint_other': target, 'axis_m': axis_m.tolist(),
                  'axis_other_aligned': axis_other.tolist(), 'angle_rad': angle,
                  'axis_source_m':'MuJoCo xaxis at zero pose' if ma is not None else 'legacy body-frame reconstruction',
                  'axis_source_other':'MuJoCo xaxis at zero pose' if oa is not None else 'legacy body-frame reconstruction',
                  'type_agrees': j['type'] == k['type']}
        output['axis_checks'].append(record)
        if angle > tolerances.kinematic_axis_angle or not record['type_agrees']:
            output['axis_disagreements'].append(record)
    differs = output['max_residual_m'] > tolerances.kinematic_residual or bool(output['axis_disagreements'])
    output['status'] = 'kinematic convention differs' if differs else 'consistent'
    output['com_eligible'] = not differs
    output['reason'] = ('Origin residual exceeds threshold and/or matched signed joint axes disagree' if differs
                        else 'Unique proper rigid fit and matched signed axes meet the configured thresholds')
    return output


def align(value, diagnostic):
    return (np.asarray(diagnostic['rotation_other_to_m']) @ np.asarray(value) +
            np.asarray(diagnostic['translation_other_to_m'])).tolist()
