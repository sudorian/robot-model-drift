# kuka_iiwa_14

Status: **complete**. Provenance: **none**, confidence **none**.

No public revision matches all comparable quantities. Class: NO MATCHING SOURCE; never counted as STALE.

M: `https://github.com/google-deepmind/mujoco_menagerie`, `kuka_iiwa_14/iiwa14.xml`, commit `370c43965323c0944b433b202aac5058b5f907a9`.
H: `https://github.com/RobotLocomotion/drake`, `multibody/benchmarks/kuka_iiwa_robot/kuka_iiwa_robot.urdf`, commit `9977d90894fe487195e9ac95a93ca4330a6ae81b`.
S: unavailable. A machine-readable H can still be compared to M; no-match differences are never counted as STALE.

Limit semantics: MJCF effort values are supported actuator torque/force envelopes. URDF effort and velocity values are manufacturer declarations retained from XML; MuJoCo does not enforce those tags. Such declaration comparisons are explicitly distinct from compiled inertial/range quantities.


## Source evidence

```json
[
  {
    "url": "https://github.com/RobotLocomotion/drake",
    "document": "kuka_iiwa_14/README.md",
    "commit": "370c43965323c0944b433b202aac5058b5f907a9",
    "current": true
  },
  {
    "url": "https://github.com/RobotLocomotion/drake/blob/master/manipulation/models/iiwa_description/urdf/iiwa14_spheres_dense_collision.urdf",
    "document": "kuka_iiwa_14/README.md",
    "commit": "370c43965323c0944b433b202aac5058b5f907a9",
    "current": true
  }
]
```


## README derivation evidence

Documentation labels are conservative: an automated documented label requires an explicit affected entity and quantity. Broader conversion notes are retained here for review.

> 3. Created base body and added its corresponding inertial properties.
> 8.  Added forcelimits to match the torque limits in the [spec sheet](https://www.reeco.co.uk/wp-content/uploads/2020/05/KUKA-LBR-iiwa-technical-data.pdf).

## Kinematics consistency

A proper Kabsch rigid transform aligns all matched zero-pose body origins. The maximum per-origin residual and signed hinge/slide axis angles determine whether CoM can be compared; RMS is also recorded. Fewer than three non-collinear origins give insufficient kinematic coverage. CoM records that fail either required M/H or M/S check are excluded from counts and largest discrepancies. Masses, principal moments and raw joint ranges remain unchanged; a flagged range still requires convention review.

| Pair | Status | Origins / rank | RMS / maximum mm | Disagreeing / checked axes |
|---|---|---:|---:|---:|
| M/H | insufficient kinematic coverage | 7 / 1 | 2.46464543e-13 / 3.41405704e-13 | 0 / 0 |

Exact fitted transforms, per-origin residuals, thresholds and axis vectors:

```json
{
  "M/H": {
    "status": "insufficient kinematic coverage",
    "matched_body_origins": 7,
    "position_threshold_m": 0.005,
    "axis_threshold_rad": 0.005,
    "residual_definition": "maximum Euclidean residual over matched body origins; Kabsch minimizes RMS, which is also recorded",
    "coordinate_frames": "each snapshot registered to its matched report anchor",
    "anchor_m": "base",
    "anchor_other": "base",
    "rotation_other_to_m": [
      [
        0.9791998324943134,
        -0.2028982208968531,
        2.7755575615628914e-17
      ],
      [
        0.2028982208968531,
        0.9791998324943134,
        1.1102230246251568e-16
      ],
      [
        -9.678644695308528e-17,
        -3.307576248994596e-16,
        1.0
      ]
    ],
    "translation_other_to_m": [
      6.5741312494755185e-18,
      -7.470656607296218e-17,
      -3.3306690738754696e-16
    ],
    "rms_residual_m": 2.464645431492673e-16,
    "max_residual_m": 3.414057044233502e-16,
    "fit_rank": 1,
    "axis_checks": [],
    "axis_disagreements": [],
    "com_eligible": false,
    "covariance_singular_values": [
      1.2391414999999992,
      5.035111827043696e-32,
      0.0
    ],
    "origin_residuals_m": {
      "base": 3.414057044233502e-16,
      "link2": 3.3528311574906857e-16,
      "link3": 2.350124780370338e-16,
      "link4": 1.5677464898718746e-16,
      "link5": 7.773418758717098e-17,
      "link6": 2.32528025789304e-16,
      "link7": 2.3731778777361013e-16
    },
    "reason": "Fewer than three non-collinear matched origins; fitted rotation is underdetermined"
  }
}
```


## Every reported quantity difference

Counts are quantity records, including correlated total/subtree/body mass records; they are not independent robot defects.

| Entity / quantity | M | S | H | H − M | Class | M source | S source | H source |
|---|---|---|---|---|---|---|---|---|
| base / mass | 5 | unavailable | 0 | -5 | NO MATCHING SOURCE | [input L56](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/kuka_iiwa_14/iiwa14.xml#L56) | unavailable | [geometry/inference input L4](https://github.com/RobotLocomotion/drake/blob/9977d90894fe487195e9ac95a93ca4330a6ae81b/multibody/benchmarks/kuka_iiwa_robot/kuka_iiwa_robot.urdf#L4) |
| base / principal_moments | [0.03, 0.05, 0.06] | unavailable | [0, 0, 0] | [-0.03, -0.05, -0.06] | NO MATCHING SOURCE | [inertia input L56](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/kuka_iiwa_14/iiwa14.xml#L56) | unavailable | [geometry/inference input L4](https://github.com/RobotLocomotion/drake/blob/9977d90894fe487195e9ac95a93ca4330a6ae81b/multibody/benchmarks/kuka_iiwa_robot/kuka_iiwa_robot.urdf#L4) |

## Raw CoM records and reporting decisions

Raw values retain the previous root-anchor registration before Kabsch; original world coordinates also remain in the snapshots. Eligible findings above use the fitted transform into M. Excluded raw records below are diagnostic numbers, not findings. No CoM suppression applies to mass or principal inertia moments.

| Entity / quantity | Raw M | Raw S | Raw H | Raw H − M | Decision | M source | S source | H source |
|---|---|---|---|---|---|---|---|---|
| robot / total_com_registered | [-0.0164081999, 0.000232603724, 0.565446913] | unavailable | [-0.0164081999, 0.000232603724, 0.565446913] | [-1.73472348e-17, 1.26851654e-17, 0] | M/H: insufficient kinematic coverage | [aggregate inputs](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/kuka_iiwa_14/iiwa14.xml#L1) | unavailable | [aggregate inputs](https://github.com/RobotLocomotion/drake/blob/9977d90894fe487195e9ac95a93ca4330a6ae81b/multibody/benchmarks/kuka_iiwa_robot/kuka_iiwa_robot.urdf#L1) |
| base / com_registered | [-0.1, 0, 0.07] | unavailable | [0, 0, 0] | [0.1, 0, -0.07] | M/H: insufficient kinematic coverage | [CoM/kinematic input L56](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/kuka_iiwa_14/iiwa14.xml#L56) | unavailable | [geometry/inference input L4](https://github.com/RobotLocomotion/drake/blob/9977d90894fe487195e9ac95a93ca4330a6ae81b/multibody/benchmarks/kuka_iiwa_robot/kuka_iiwa_robot.urdf#L4) |
| link2 / com_registered | [-0.0003, 0.042, 0.419] | unavailable | [-0.0003, 0.042, 0.419] | [5.09575021e-18, 3.46944695e-17, 0] | M/H: insufficient kinematic coverage | [CoM/kinematic input L72](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/kuka_iiwa_14/iiwa14.xml#L72) | unavailable | [CoM/kinematic input L41](https://github.com/RobotLocomotion/drake/blob/9977d90894fe487195e9ac95a93ca4330a6ae81b/multibody/benchmarks/kuka_iiwa_robot/kuka_iiwa_robot.urdf#L41) |
| link3 / com_registered | [0, 0.03, 0.6945] | unavailable | [-1.2246468e-17, 0.03, 0.6945] | [-1.2246468e-17, 1.14491749e-16, 1.11022302e-16] | M/H: insufficient kinematic coverage | [CoM/kinematic input L86](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/kuka_iiwa_14/iiwa14.xml#L86) | unavailable | [CoM/kinematic input L57](https://github.com/RobotLocomotion/drake/blob/9977d90894fe487195e9ac95a93ca4330a6ae81b/multibody/benchmarks/kuka_iiwa_robot/kuka_iiwa_robot.urdf#L57) |
| link4 / com_registered | [0, -0.034, 0.847] | unavailable | [-3.87600712e-17, -0.034, 0.847] | [-3.87600712e-17, 6.24500451e-17, 2.22044605e-16] | M/H: insufficient kinematic coverage | [CoM/kinematic input L101](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/kuka_iiwa_14/iiwa14.xml#L101) | unavailable | [CoM/kinematic input L73](https://github.com/RobotLocomotion/drake/blob/9977d90894fe487195e9ac95a93ca4330a6ae81b/multibody/benchmarks/kuka_iiwa_robot/kuka_iiwa_robot.urdf#L73) |
| link5 / com_registered | [-0.0001, -0.021, 1.0405] | unavailable | [-0.0001, -0.021, 1.0405] | [-6.35477998e-17, -2.08166817e-17, 4.4408921e-16] | M/H: insufficient kinematic coverage | [CoM/kinematic input L112](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/kuka_iiwa_14/iiwa14.xml#L112) | unavailable | [CoM/kinematic input L89](https://github.com/RobotLocomotion/drake/blob/9977d90894fe487195e9ac95a93ca4330a6ae81b/multibody/benchmarks/kuka_iiwa_robot/kuka_iiwa_robot.urdf#L89) |
| link6 / com_registered | [0, 0.0004, 1.1806] | unavailable | [-7.53525176e-17, 0.0004, 1.1806] | [-7.53525176e-17, -1.13624388e-16, 4.4408921e-16] | M/H: insufficient kinematic coverage | [CoM/kinematic input L127](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/kuka_iiwa_14/iiwa14.xml#L127) | unavailable | [CoM/kinematic input L105](https://github.com/RobotLocomotion/drake/blob/9977d90894fe487195e9ac95a93ca4330a6ae81b/multibody/benchmarks/kuka_iiwa_robot/kuka_iiwa_robot.urdf#L105) |
| link7 / com_registered | [0, -9.14565708e-17, 1.281] | unavailable | [-8.77459432e-17, -2.23891283e-16, 1.281] | [-8.77459432e-17, -1.32434712e-16, 4.4408921e-16] | M/H: insufficient kinematic coverage | [CoM/kinematic input L135](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/kuka_iiwa_14/iiwa14.xml#L135) | unavailable | [CoM/kinematic input L121](https://github.com/RobotLocomotion/drake/blob/9977d90894fe487195e9ac95a93ca4330a6ae81b/multibody/benchmarks/kuka_iiwa_robot/kuka_iiwa_robot.urdf#L121) |

## Mass accounting

Every contributing compiled body mass is listed here so total/subtree sums can be checked. Links point to explicit inertials or to geometry inputs when the compiler inferred a mass. CoM links identify inertial inputs; world coordinates additionally use the ancestor transforms and the registration recorded below.

| M body | M kg / source | S kg / source | H kg / source |
|---|---|---|---|
| base | 5 / [input L56](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/kuka_iiwa_14/iiwa14.xml#L56) | unavailable | 0 / [geometry/inference input L4](https://github.com/RobotLocomotion/drake/blob/9977d90894fe487195e9ac95a93ca4330a6ae81b/multibody/benchmarks/kuka_iiwa_robot/kuka_iiwa_robot.urdf#L4) |
| link1 | 5.76 / [input L63](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/kuka_iiwa_14/iiwa14.xml#L63) | unavailable | unmatched |
| link2 | 6.35 / [input L72](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/kuka_iiwa_14/iiwa14.xml#L72) | unavailable | 6.35 / [input L42](https://github.com/RobotLocomotion/drake/blob/9977d90894fe487195e9ac95a93ca4330a6ae81b/multibody/benchmarks/kuka_iiwa_robot/kuka_iiwa_robot.urdf#L42) |
| link3 | 3.5 / [input L86](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/kuka_iiwa_14/iiwa14.xml#L86) | unavailable | 3.5 / [input L58](https://github.com/RobotLocomotion/drake/blob/9977d90894fe487195e9ac95a93ca4330a6ae81b/multibody/benchmarks/kuka_iiwa_robot/kuka_iiwa_robot.urdf#L58) |
| link4 | 3.5 / [input L101](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/kuka_iiwa_14/iiwa14.xml#L101) | unavailable | 3.5 / [input L74](https://github.com/RobotLocomotion/drake/blob/9977d90894fe487195e9ac95a93ca4330a6ae81b/multibody/benchmarks/kuka_iiwa_robot/kuka_iiwa_robot.urdf#L74) |
| link5 | 3.5 / [input L112](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/kuka_iiwa_14/iiwa14.xml#L112) | unavailable | 3.5 / [input L90](https://github.com/RobotLocomotion/drake/blob/9977d90894fe487195e9ac95a93ca4330a6ae81b/multibody/benchmarks/kuka_iiwa_robot/kuka_iiwa_robot.urdf#L90) |
| link6 | 1.8 / [input L127](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/kuka_iiwa_14/iiwa14.xml#L127) | unavailable | 1.8 / [input L106](https://github.com/RobotLocomotion/drake/blob/9977d90894fe487195e9ac95a93ca4330a6ae81b/multibody/benchmarks/kuka_iiwa_robot/kuka_iiwa_robot.urdf#L106) |
| link7 | 1.2 / [input L135](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/kuka_iiwa_14/iiwa14.xml#L135) | unavailable | 1.2 / [input L122](https://github.com/RobotLocomotion/drake/blob/9977d90894fe487195e9ac95a93ca4330a6ae81b/multibody/benchmarks/kuka_iiwa_robot/kuka_iiwa_robot.urdf#L122) |
| upstream-only iiwa_link_0 | unavailable | unavailable | 5 / [input L14](https://github.com/RobotLocomotion/drake/blob/9977d90894fe487195e9ac95a93ca4330a6ae81b/multibody/benchmarks/kuka_iiwa_robot/kuka_iiwa_robot.urdf#L14) |
| upstream-only iiwa_link_1 | unavailable | unavailable | 5.76 / [input L28](https://github.com/RobotLocomotion/drake/blob/9977d90894fe487195e9ac95a93ca4330a6ae81b/multibody/benchmarks/kuka_iiwa_robot/kuka_iiwa_robot.urdf#L28) |

## Coverage and unmatched elements

```json
{
  "mapping_h": {
    "bodies": {
      "base": "base",
      "link2": "iiwa_link_2",
      "link3": "iiwa_link_3",
      "link4": "iiwa_link_4",
      "link5": "iiwa_link_5",
      "link6": "iiwa_link_6",
      "link7": "iiwa_link_7"
    },
    "joints": {
      "joint2": "iiwa_joint_2",
      "joint3": "iiwa_joint_3",
      "joint4": "iiwa_joint_4",
      "joint5": "iiwa_joint_5",
      "joint6": "iiwa_joint_6",
      "joint7": "iiwa_joint_7"
    },
    "body_methods": {
      "base": "name",
      "link2": "unique kinematic subtree",
      "link3": "unique kinematic subtree",
      "link4": "unique kinematic subtree",
      "link5": "unique kinematic subtree",
      "link6": "unique kinematic subtree",
      "link7": "unique kinematic subtree"
    },
    "joint_methods": {
      "joint2": "unique joint on matched body with same type and axis",
      "joint3": "unique joint on matched body with same type and axis",
      "joint4": "unique joint on matched body with same type and axis",
      "joint5": "unique joint on matched body with same type and axis",
      "joint6": "unique joint on matched body with same type and axis",
      "joint7": "unique joint on matched body with same type and axis"
    },
    "unmatched_m_bodies": [
      "link1"
    ],
    "unmatched_upstream_bodies": [
      "iiwa_link_0",
      "iiwa_link_1"
    ],
    "unmatched_m_joints": [
      "joint1"
    ],
    "unmatched_upstream_joints": [
      "iiwa_joint_1"
    ],
    "registration_anchor": {
      "M": "base",
      "H": "base",
      "root_unmatched": false
    }
  },
  "mapping_s": null,
  "unavailable": [
    {
      "entity": "joint2",
      "other_entity": "iiwa_joint_2",
      "quantity": "range",
      "tolerance": "range",
      "m": [
        -2.0944,
        2.0944
      ],
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "joint2",
      "other_entity": "iiwa_joint_2",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "joint2",
      "other_entity": "iiwa_joint_2",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "joint2",
      "other_entity": "iiwa_joint_2",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "joint3",
      "other_entity": "iiwa_joint_3",
      "quantity": "range",
      "tolerance": "range",
      "m": [
        -2.96706,
        2.96706
      ],
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "joint3",
      "other_entity": "iiwa_joint_3",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "joint3",
      "other_entity": "iiwa_joint_3",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "joint3",
      "other_entity": "iiwa_joint_3",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "joint4",
      "other_entity": "iiwa_joint_4",
      "quantity": "range",
      "tolerance": "range",
      "m": [
        -2.0944,
        2.0944
      ],
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "joint4",
      "other_entity": "iiwa_joint_4",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "joint4",
      "other_entity": "iiwa_joint_4",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "joint4",
      "other_entity": "iiwa_joint_4",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "joint5",
      "other_entity": "iiwa_joint_5",
      "quantity": "range",
      "tolerance": "range",
      "m": [
        -2.96706,
        2.96706
      ],
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "joint5",
      "other_entity": "iiwa_joint_5",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "joint5",
      "other_entity": "iiwa_joint_5",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "joint5",
      "other_entity": "iiwa_joint_5",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "joint6",
      "other_entity": "iiwa_joint_6",
      "quantity": "range",
      "tolerance": "range",
      "m": [
        -2.0944,
        2.0944
      ],
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "joint6",
      "other_entity": "iiwa_joint_6",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "joint6",
      "other_entity": "iiwa_joint_6",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "joint6",
      "other_entity": "iiwa_joint_6",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "joint7",
      "other_entity": "iiwa_joint_7",
      "quantity": "range",
      "tolerance": "range",
      "m": [
        -3.05433,
        3.05433
      ],
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "joint7",
      "other_entity": "iiwa_joint_7",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "joint7",
      "other_entity": "iiwa_joint_7",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "joint7",
      "other_entity": "iiwa_joint_7",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    }
  ]
}
```

## Limits unavailable for a like-for-like simulator comparison

URDF effort and velocity tags are manufacturer declarations; MuJoCo ignores them. Missing enforced quantities are not interpreted as zero. The available values are shown for review and excluded from STALE counts.

| Joint / quantity | M | S | H / declared upstream |
|---|---|---|---|
| joint2 / effort | unavailable | unavailable | unavailable |
| joint2 / force | unavailable | unavailable | unavailable |
| joint2 / velocity | unavailable | unavailable | unavailable |
| joint3 / effort | unavailable | unavailable | unavailable |
| joint3 / force | unavailable | unavailable | unavailable |
| joint3 / velocity | unavailable | unavailable | unavailable |
| joint4 / effort | unavailable | unavailable | unavailable |
| joint4 / force | unavailable | unavailable | unavailable |
| joint4 / velocity | unavailable | unavailable | unavailable |
| joint5 / effort | unavailable | unavailable | unavailable |
| joint5 / force | unavailable | unavailable | unavailable |
| joint5 / velocity | unavailable | unavailable | unavailable |
| joint6 / effort | unavailable | unavailable | unavailable |
| joint6 / force | unavailable | unavailable | unavailable |
| joint6 / velocity | unavailable | unavailable | unavailable |
| joint7 / effort | unavailable | unavailable | unavailable |
| joint7 / force | unavailable | unavailable | unavailable |
| joint7 / velocity | unavailable | unavailable | unavailable |
## Tolerances

```json
{
  "mass_relative": 0.005,
  "mass_absolute": 0.001,
  "com_absolute": 0.0005,
  "inertia_relative": 0.01,
  "range_absolute": 0.005,
  "slide_range_absolute": 0.0005,
  "limit_relative": 0.01,
  "kinematic_residual": 0.005,
  "kinematic_axis_angle": 0.005,
  "scale": 1.0
}
```

## Candidate errors

```json
[]
```

## Self comparisons

```json
[
  {
    "file": "kuka_iiwa_14/iiwa14.xml",
    "status": "passed",
    "findings": 0
  }
]
```

## Sensitivity

```json
{
  "0.5": {
    "provenance_method": "none",
    "counts": {
      "NO MATCHING SOURCE": 2
    },
    "classifications_changed": 0,
    "finding_membership_changes": 0
  },
  "2": {
    "provenance_method": "none",
    "counts": {
      "NO MATCHING SOURCE": 2
    },
    "classifications_changed": 0,
    "finding_membership_changes": 0
  }
}
```

## Compilation

```json
{
  "M": {
    "geometry_stripped": true,
    "missing_explicit_inertials": [],
    "assets_loaded": 0,
    "mesh_conversions": [],
    "xacro_arguments": {},
    "registration": {
      "translation": [
        0.0,
        0.0,
        0.0
      ],
      "rotation": [
        [
          1.0,
          0.0,
          0.0
        ],
        [
          0.0,
          1.0,
          0.0
        ],
        [
          0.0,
          0.0,
          1.0
        ]
      ]
    }
  },
  "H": {
    "geometry_stripped": false,
    "missing_explicit_inertials": [
      "base"
    ],
    "assets_loaded": 0,
    "mesh_conversions": [],
    "xacro_arguments": {},
    "registration": {
      "translation": [
        0.0,
        0.0,
        0.0
      ],
      "rotation": [
        [
          1.0,
          0.0,
          0.0
        ],
        [
          0.0,
          1.0,
          0.0
        ],
        [
          0.0,
          0.0,
          1.0
        ]
      ]
    }
  }
}
```

## Rerun

```json
{
  "mode": "frozen revisions",
  "primary_views_recompiled": [
    "H",
    "M"
  ],
  "self_variants_recompiled": 1,
  "historical_snapshots_reused": 3,
  "primary_physics_unchanged": true,
  "source_matching": "original raw-value provenance criteria retained; kinematic guard applies to reported CoM"
}
```
