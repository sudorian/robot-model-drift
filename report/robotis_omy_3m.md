# robotis_omy_3m

Status: **partial history**. Provenance: **unknown**, confidence **incomplete**.

Unresolved historical compilation prevents selecting or rejecting a matching source. Pairwise M/H differences are reported with unknown provenance.

M: `https://github.com/google-deepmind/mujoco_menagerie`, `robotis_omy_3m/omy_3m.xml`, commit `370c43965323c0944b433b202aac5058b5f907a9`.
H: `https://github.com/ROBOTIS-GIT/open_manipulator`, `open_manipulator_description/urdf/omy_3m/omy_3m.urdf`, commit `cb946894a8b5d242d2d4e012f93f01eecac5a3ce`.
S: unavailable. A machine-readable H can still be compared to M; no-match differences are never counted as STALE.

Limit semantics: MJCF effort values are supported actuator torque/force envelopes. URDF effort and velocity values are manufacturer declarations retained from XML; MuJoCo does not enforce those tags. Such declaration comparisons are explicitly distinct from compiled inertial/range quantities.


## Source evidence

```json
[
  {
    "url": "https://github.com/ROBOTIS-GIT/open_manipulator/tree/main/open_manipulator_description/meshes/omy_3m",
    "document": "robotis_omy_3m/README.md",
    "commit": "370c43965323c0944b433b202aac5058b5f907a9",
    "current": true
  },
  {
    "url": "https://github.com/ROBOTIS-GIT/open_manipulator/tree/main/open_manipulator_description/urdf/omy_3m",
    "document": "robotis_omy_3m/README.md",
    "commit": "370c43965323c0944b433b202aac5058b5f907a9",
    "current": true
  }
]
```


## README derivation evidence

Documentation labels are conservative: an automated documented label requires an explicit affected entity and quantity. Broader conversion notes are retained here for review.

> The OMY-3M is a 6-DOF fixed-base robotic manipulator designed for research and industrial manipulation tasks.
>    limits.
> 6. Added `fullinertia` values directly from the URDF for accurate dynamics simulation.
> - The compiled mass, center of mass, principal inertia and inertial orientation of all six moving links match the
> The position actuators use the documented maximum torque as their force limit. See the

## Kinematics consistency

A proper Kabsch rigid transform aligns all matched zero-pose body origins. The maximum per-origin residual and signed hinge/slide axis angles determine whether CoM can be compared; RMS is also recorded. Fewer than three non-collinear origins give insufficient kinematic coverage. CoM records that fail either required M/H or M/S check are excluded from counts and largest discrepancies. Masses, principal moments and raw joint ranges remain unchanged; a flagged range still requires convention review.

| Pair | Status | Origins / rank | RMS / maximum mm | Disagreeing / checked axes |
|---|---|---:|---:|---:|
| M/H | consistent | 7 / 2 | 2.15607267e-14 / 3.92523115e-14 | 0 / 6 |

Exact fitted transforms, per-origin residuals, thresholds and axis vectors:

```json
{
  "M/H": {
    "status": "consistent",
    "matched_body_origins": 7,
    "position_threshold_m": 0.005,
    "axis_threshold_rad": 0.005,
    "residual_definition": "maximum Euclidean residual over matched body origins; Kabsch minimizes RMS, which is also recorded",
    "coordinate_frames": "each snapshot registered to its matched report anchor",
    "anchor_m": "base_unit",
    "anchor_other": "link0",
    "rotation_other_to_m": [
      [
        1.0,
        0.0,
        0.0
      ],
      [
        0.0,
        0.9999999999999997,
        -1.8310946422906377e-17
      ],
      [
        0.0,
        1.5265566588595902e-16,
        1.0
      ]
    ],
    "translation_other_to_m": [
      0.0,
      -1.3877787807814457e-17,
      0.0
    ],
    "rms_residual_m": 2.1560726693993167e-17,
    "max_residual_m": 3.925231146709438e-17,
    "fit_rank": 2,
    "axis_checks": [
      {
        "joint_m": "joint1",
        "joint_other": "joint1",
        "axis_m": [
          0.0,
          0.0,
          1.0
        ],
        "axis_other_aligned": [
          0.0,
          -1.8310946422906377e-17,
          1.0
        ],
        "angle_rad": 1.8310946422906377e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "joint2",
        "joint_other": "joint2",
        "axis_m": [
          0.0,
          1.0,
          0.0
        ],
        "axis_other_aligned": [
          0.0,
          1.0,
          1.5265566588595907e-16
        ],
        "angle_rad": 1.5265566588595907e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "joint3",
        "joint_other": "joint3",
        "axis_m": [
          0.0,
          1.0,
          0.0
        ],
        "axis_other_aligned": [
          0.0,
          1.0,
          1.5265566588595907e-16
        ],
        "angle_rad": 1.5265566588595907e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "joint4",
        "joint_other": "joint4",
        "axis_m": [
          0.0,
          1.0,
          0.0
        ],
        "axis_other_aligned": [
          0.0,
          1.0,
          1.5265566588595907e-16
        ],
        "angle_rad": 1.5265566588595907e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "joint5",
        "joint_other": "joint5",
        "axis_m": [
          0.0,
          0.0,
          1.0
        ],
        "axis_other_aligned": [
          0.0,
          -1.8310946422906377e-17,
          1.0
        ],
        "angle_rad": 1.8310946422906377e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "joint6",
        "joint_other": "joint6",
        "axis_m": [
          0.0,
          1.0,
          0.0
        ],
        "axis_other_aligned": [
          0.0,
          1.0,
          1.5265566588595907e-16
        ],
        "angle_rad": 1.5265566588595907e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      }
    ],
    "axis_disagreements": [],
    "com_eligible": true,
    "covariance_singular_values": [
      0.506644963502365,
      0.01999996506906358,
      0.0
    ],
    "origin_residuals_m": {
      "link1": 1.70181151193429e-17,
      "link2": 3.925231146709438e-17,
      "link3": 1.3877787807814457e-17,
      "link4": 2.5560171625628726e-17,
      "link5": 1.3877787807814457e-17,
      "link6": 1.3877787807814457e-17,
      "base_unit": 1.3877787807814457e-17
    },
    "reason": "Unique proper rigid fit and matched signed axes meet the configured thresholds"
  }
}
```


## Every reported quantity difference

Counts are quantity records, including correlated total/subtree/body mass records; they are not independent robot defects.

| Entity / quantity | M | S | H | H − M | Class | M source | S source | H source |
|---|---|---|---|---|---|---|---|---|
| joint1 / effort | 61.4 | unavailable | 1000 | 938.6 | unknown | [inherited actuator input L12](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/robotis_omy_3m/omy_3m.xml#L12) | unavailable | [input L56](https://github.com/ROBOTIS-GIT/open_manipulator/blob/cb946894a8b5d242d2d4e012f93f01eecac5a3ce/open_manipulator_description/urdf/omy_3m/omy_3m.urdf#L56) |
| joint2 / effort | 61.4 | unavailable | 1000 | 938.6 | unknown | [inherited actuator input L12](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/robotis_omy_3m/omy_3m.xml#L12) | unavailable | [input L86](https://github.com/ROBOTIS-GIT/open_manipulator/blob/cb946894a8b5d242d2d4e012f93f01eecac5a3ce/open_manipulator_description/urdf/omy_3m/omy_3m.urdf#L86) |
| joint3 / range | [-2.617994, 2.617994] | unavailable | [-6.28318531, 6.28318531] | [-3.66519131, 3.66519131] | unknown | [inherited default L24](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/robotis_omy_3m/omy_3m.xml#L24) | unavailable | [input L116](https://github.com/ROBOTIS-GIT/open_manipulator/blob/cb946894a8b5d242d2d4e012f93f01eecac5a3ce/open_manipulator_description/urdf/omy_3m/omy_3m.urdf#L116) |
| joint3 / effort | 31.7 | unavailable | 1000 | 968.3 | unknown | [inherited actuator input L22](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/robotis_omy_3m/omy_3m.xml#L22) | unavailable | [input L116](https://github.com/ROBOTIS-GIT/open_manipulator/blob/cb946894a8b5d242d2d4e012f93f01eecac5a3ce/open_manipulator_description/urdf/omy_3m/omy_3m.urdf#L116) |
| joint4 / effort | 31.7 | unavailable | 1000 | 968.3 | unknown | [inherited actuator input L22](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/robotis_omy_3m/omy_3m.xml#L22) | unavailable | [input L146](https://github.com/ROBOTIS-GIT/open_manipulator/blob/cb946894a8b5d242d2d4e012f93f01eecac5a3ce/open_manipulator_description/urdf/omy_3m/omy_3m.urdf#L146) |
| joint5 / effort | 31.7 | unavailable | 1000 | 968.3 | unknown | [inherited actuator input L22](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/robotis_omy_3m/omy_3m.xml#L22) | unavailable | [input L176](https://github.com/ROBOTIS-GIT/open_manipulator/blob/cb946894a8b5d242d2d4e012f93f01eecac5a3ce/open_manipulator_description/urdf/omy_3m/omy_3m.urdf#L176) |
| joint6 / effort | 31.7 | unavailable | 1000 | 968.3 | unknown | [inherited actuator input L22](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/robotis_omy_3m/omy_3m.xml#L22) | unavailable | [input L206](https://github.com/ROBOTIS-GIT/open_manipulator/blob/cb946894a8b5d242d2d4e012f93f01eecac5a3ce/open_manipulator_description/urdf/omy_3m/omy_3m.urdf#L206) |

## Raw CoM records and reporting decisions

Raw values retain the previous root-anchor registration before Kabsch; original world coordinates also remain in the snapshots. Eligible findings above use the fitted transform into M. Excluded raw records below are diagnostic numbers, not findings. No CoM suppression applies to mass or principal inertia moments.

| Entity / quantity | Raw M | Raw S | Raw H | Raw H − M | Decision | M source | S source | H source |
|---|---|---|---|---|---|---|---|---|
| robot / total_com_registered | [-0.000480604828, -0.0648604437, 0.388618306] | unavailable | [-0.000480604828, -0.0648604437, 0.388618306] | [0, 0, 0] | eligible; compared after Kabsch alignment | [aggregate inputs](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/robotis_omy_3m/omy_3m.xml#L1) | unavailable | [aggregate inputs](https://github.com/ROBOTIS-GIT/open_manipulator/blob/cb946894a8b5d242d2d4e012f93f01eecac5a3ce/open_manipulator_description/urdf/omy_3m/omy_3m.urdf#L1) |
| base_unit / com_registered | [-0.0040215824, 0.0013083991, 0.05507347] | unavailable | [-0.0040215824, 0.0013083991, 0.05507347] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L60](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/robotis_omy_3m/omy_3m.xml#L60) | unavailable | [CoM/kinematic input L46](https://github.com/ROBOTIS-GIT/open_manipulator/blob/cb946894a8b5d242d2d4e012f93f01eecac5a3ce/open_manipulator_description/urdf/omy_3m/omy_3m.urdf#L46) |
| link1 / com_registered | [-0.00011063615, -0.005471127, 0.155602267] | unavailable | [-0.00011063615, -0.005471127, 0.155602267] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L65](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/robotis_omy_3m/omy_3m.xml#L65) | unavailable | [CoM/kinematic input L76](https://github.com/ROBOTIS-GIT/open_manipulator/blob/cb946894a8b5d242d2d4e012f93f01eecac5a3ce/open_manipulator_description/urdf/omy_3m/omy_3m.urdf#L76) |
| link2 / com_registered | [1.1405379e-05, -0.105315756, 0.27510634] | unavailable | [1.1405379e-05, -0.105315756, 0.27510634] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L71](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/robotis_omy_3m/omy_3m.xml#L71) | unavailable | [CoM/kinematic input L106](https://github.com/ROBOTIS-GIT/open_manipulator/blob/cb946894a8b5d242d2d4e012f93f01eecac5a3ce/open_manipulator_description/urdf/omy_3m/omy_3m.urdf#L106) |
| link3 / com_registered | [7.8148689e-05, -0.01431519, 0.55967267] | unavailable | [7.8148689e-05, -0.01431519, 0.55967267] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L77](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/robotis_omy_3m/omy_3m.xml#L77) | unavailable | [CoM/kinematic input L136](https://github.com/ROBOTIS-GIT/open_manipulator/blob/cb946894a8b5d242d2d4e012f93f01eecac5a3ce/open_manipulator_description/urdf/omy_3m/omy_3m.urdf#L136) |
| link4 / com_registered | [-0.00013318256, -0.10746667, 0.657090688] | unavailable | [-0.00013318256, -0.10746667, 0.657090688] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L83](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/robotis_omy_3m/omy_3m.xml#L83) | unavailable | [CoM/kinematic input L166](https://github.com/ROBOTIS-GIT/open_manipulator/blob/cb946894a8b5d242d2d4e012f93f01eecac5a3ce/open_manipulator_description/urdf/omy_3m/omy_3m.urdf#L166) |
| link5 / com_registered | [0.00013318256, -0.132090688, 0.74796667] | unavailable | [0.00013318256, -0.132090688, 0.74796667] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L89](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/robotis_omy_3m/omy_3m.xml#L89) | unavailable | [CoM/kinematic input L196](https://github.com/ROBOTIS-GIT/open_manipulator/blob/cb946894a8b5d242d2d4e012f93f01eecac5a3ce/open_manipulator_description/urdf/omy_3m/omy_3m.urdf#L196) |
| link6 / com_registered | [1.1080146e-05, -0.193594056, 0.762802934] | unavailable | [1.1080146e-05, -0.193594056, 0.762802934] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L95](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/robotis_omy_3m/omy_3m.xml#L95) | unavailable | [CoM/kinematic input L226](https://github.com/ROBOTIS-GIT/open_manipulator/blob/cb946894a8b5d242d2d4e012f93f01eecac5a3ce/open_manipulator_description/urdf/omy_3m/omy_3m.urdf#L226) |

## Mass accounting

Every contributing compiled body mass is listed here so total/subtree sums can be checked. Links point to explicit inertials or to geometry inputs when the compiler inferred a mass. CoM links identify inertial inputs; world coordinates additionally use the ancestor transforms and the registration recorded below.

| M body | M kg / source | S kg / source | H kg / source |
|---|---|---|---|
| base_unit | 1.5287486 / [input L60](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/robotis_omy_3m/omy_3m.xml#L60) | unavailable | 1.5287486 / [input L47](https://github.com/ROBOTIS-GIT/open_manipulator/blob/cb946894a8b5d242d2d4e012f93f01eecac5a3ce/open_manipulator_description/urdf/omy_3m/omy_3m.urdf#L47) |
| link1 | 2.0648832 / [input L65](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/robotis_omy_3m/omy_3m.xml#L65) | unavailable | 2.0648832 / [input L77](https://github.com/ROBOTIS-GIT/open_manipulator/blob/cb946894a8b5d242d2d4e012f93f01eecac5a3ce/open_manipulator_description/urdf/omy_3m/omy_3m.urdf#L77) |
| link2 | 3.6795395 / [input L71](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/robotis_omy_3m/omy_3m.xml#L71) | unavailable | 3.6795395 / [input L107](https://github.com/ROBOTIS-GIT/open_manipulator/blob/cb946894a8b5d242d2d4e012f93f01eecac5a3ce/open_manipulator_description/urdf/omy_3m/omy_3m.urdf#L107) |
| link3 | 2.3865916 / [input L77](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/robotis_omy_3m/omy_3m.xml#L77) | unavailable | 2.3865916 / [input L137](https://github.com/ROBOTIS-GIT/open_manipulator/blob/cb946894a8b5d242d2d4e012f93f01eecac5a3ce/open_manipulator_description/urdf/omy_3m/omy_3m.urdf#L137) |
| link4 | 1.4002347 / [input L83](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/robotis_omy_3m/omy_3m.xml#L83) | unavailable | 1.4002347 / [input L167](https://github.com/ROBOTIS-GIT/open_manipulator/blob/cb946894a8b5d242d2d4e012f93f01eecac5a3ce/open_manipulator_description/urdf/omy_3m/omy_3m.urdf#L167) |
| link5 | 1.4002347 / [input L89](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/robotis_omy_3m/omy_3m.xml#L89) | unavailable | 1.4002347 / [input L197](https://github.com/ROBOTIS-GIT/open_manipulator/blob/cb946894a8b5d242d2d4e012f93f01eecac5a3ce/open_manipulator_description/urdf/omy_3m/omy_3m.urdf#L197) |
| link6 | 0.32442692 / [input L95](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/robotis_omy_3m/omy_3m.xml#L95) | unavailable | 0.32442692 / [input L227](https://github.com/ROBOTIS-GIT/open_manipulator/blob/cb946894a8b5d242d2d4e012f93f01eecac5a3ce/open_manipulator_description/urdf/omy_3m/omy_3m.urdf#L227) |
| upstream-only end_effector_link | unavailable | unavailable | 0 / [geometry/inference input L18](https://github.com/ROBOTIS-GIT/open_manipulator/blob/cb946894a8b5d242d2d4e012f93f01eecac5a3ce/open_manipulator_description/urdf/omy_3m/omy_3m.urdf#L18) |

## Coverage and unmatched elements

```json
{
  "mapping_h": {
    "bodies": {
      "link1": "link1",
      "link2": "link2",
      "link3": "link3",
      "link4": "link4",
      "link5": "link5",
      "link6": "link6",
      "base_unit": "link0"
    },
    "joints": {
      "joint1": "joint1",
      "joint2": "joint2",
      "joint3": "joint3",
      "joint4": "joint4",
      "joint5": "joint5",
      "joint6": "joint6"
    },
    "body_methods": {
      "link1": "name",
      "link2": "name",
      "link3": "name",
      "link4": "name",
      "link5": "name",
      "link6": "name",
      "base_unit": "unique kinematic subtree"
    },
    "joint_methods": {
      "joint1": "name",
      "joint2": "name",
      "joint3": "name",
      "joint4": "name",
      "joint5": "name",
      "joint6": "name"
    },
    "unmatched_m_bodies": [],
    "unmatched_upstream_bodies": [
      "end_effector_link"
    ],
    "unmatched_m_joints": [],
    "unmatched_upstream_joints": [],
    "registration_anchor": {
      "M": "base_unit",
      "H": "link0",
      "root_unmatched": false
    }
  },
  "mapping_s": null,
  "unavailable": [
    {
      "entity": "joint1",
      "other_entity": "joint1",
      "quantity": "force",
      "tolerance": "limit",
      "m": 61.4,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "joint1",
      "other_entity": "joint1",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 4.8,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "joint2",
      "other_entity": "joint2",
      "quantity": "force",
      "tolerance": "limit",
      "m": 61.4,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "joint2",
      "other_entity": "joint2",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 4.8,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "joint3",
      "other_entity": "joint3",
      "quantity": "force",
      "tolerance": "limit",
      "m": 31.7,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "joint3",
      "other_entity": "joint3",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 4.8,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "joint4",
      "other_entity": "joint4",
      "quantity": "force",
      "tolerance": "limit",
      "m": 31.7,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "joint4",
      "other_entity": "joint4",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 4.8,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "joint5",
      "other_entity": "joint5",
      "quantity": "force",
      "tolerance": "limit",
      "m": 31.7,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "joint5",
      "other_entity": "joint5",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 4.8,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "joint6",
      "other_entity": "joint6",
      "quantity": "force",
      "tolerance": "limit",
      "m": 31.7,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "joint6",
      "other_entity": "joint6",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 4.8,
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
| joint1 / force | 61.4 | unavailable | unavailable |
| joint1 / velocity | unavailable | unavailable | 4.8 |
| joint2 / force | 61.4 | unavailable | unavailable |
| joint2 / velocity | unavailable | unavailable | 4.8 |
| joint3 / force | 31.7 | unavailable | unavailable |
| joint3 / velocity | unavailable | unavailable | 4.8 |
| joint4 / force | 31.7 | unavailable | unavailable |
| joint4 / velocity | unavailable | unavailable | 4.8 |
| joint5 / force | 31.7 | unavailable | unavailable |
| joint5 / velocity | unavailable | unavailable | 4.8 |
| joint6 / force | 31.7 | unavailable | unavailable |
| joint6 / velocity | unavailable | unavailable | 4.8 |
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

## History inputs

```json
[
  "open_manipulator_description/meshes/omy_3m/base_unit.stl",
  "open_manipulator_description/meshes/omy_3m/link1.stl",
  "open_manipulator_description/meshes/omy_3m/link2.stl",
  "open_manipulator_description/meshes/omy_3m/link3.stl",
  "open_manipulator_description/meshes/omy_3m/link4.stl",
  "open_manipulator_description/meshes/omy_3m/link5.stl",
  "open_manipulator_description/meshes/omy_3m/link6.stl",
  "open_manipulator_description/urdf/omy_3m/omy_3m.urdf"
]
```

## Self comparisons

```json
[
  {
    "file": "robotis_omy_3m/omy_3m.xml",
    "status": "passed",
    "findings": 0
  }
]
```

## Sensitivity

```json
{
  "0.5": {
    "provenance_method": "unknown",
    "counts": {
      "unknown": 7
    },
    "classifications_changed": 0,
    "finding_membership_changes": 0
  },
  "2": {
    "provenance_method": "unknown",
    "counts": {
      "unknown": 7
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
    "nonphysical_normalizations": [],
    "xacro_arguments": {},
    "source_dependencies": [
      "robotis_omy_3m/omy_3m.xml"
    ],
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
    },
    "compiler_warnings": [],
    "limit_semantics": "Effort from supported scalar actuator envelopes; force from joint caps or supported envelopes; velocity unavailable unless explicitly represented"
  },
  "H": {
    "geometry_stripped": false,
    "missing_explicit_inertials": [
      "world",
      "end_effector_link"
    ],
    "assets_loaded": 7,
    "mesh_conversions": [],
    "nonphysical_normalizations": [],
    "xacro_arguments": {},
    "source_dependencies": [
      "open_manipulator_description/urdf/omy_3m/omy_3m.urdf",
      "open_manipulator_description/meshes/omy_3m/base_unit.stl",
      "open_manipulator_description/meshes/omy_3m/link1.stl",
      "open_manipulator_description/meshes/omy_3m/link2.stl",
      "open_manipulator_description/meshes/omy_3m/link3.stl",
      "open_manipulator_description/meshes/omy_3m/link4.stl",
      "open_manipulator_description/meshes/omy_3m/link5.stl",
      "open_manipulator_description/meshes/omy_3m/link6.stl"
    ],
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
    },
    "compiler_warnings": [],
    "limit_semantics": "URDF effort/velocity declarations are retained metadata, not enforced by MuJoCo"
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
  "historical_snapshots_reused": 2,
  "primary_physics_unchanged": true,
  "source_matching": "original raw-value provenance criteria retained; kinematic guard applies to reported CoM"
}
```
