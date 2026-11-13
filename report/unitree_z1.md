# unitree_z1

Status: **partial history**. Provenance: **dated match**, confidence **medium**.

Source selected using the ordered amended provenance rules.

M: `https://github.com/google-deepmind/mujoco_menagerie`, `unitree_z1/z1.xml`, commit `370c43965323c0944b433b202aac5058b5f907a9`.
H: `https://github.com/unitreerobotics/unitree_ros`, `robots/z1_description/xacro/z1.urdf`, commit `157ff950351e5f535e03c5d85a16b7d594b3dbcc`.
S: `f10d1c6add85785542fed20fc5e3b4e66a13f64b` (2023-07-20T15:36:48+08:00). Menagerie release/change: 2023-12-14T15:23:47+03:00.

Limit semantics: MJCF effort values are supported actuator torque/force envelopes. URDF effort and velocity values are manufacturer declarations retained from XML; MuJoCo does not enforce those tags. Such declaration comparisons are explicitly distinct from compiled inertial/range quantities.


## Source evidence

```json
[
  {
    "url": "https://github.com/unitreerobotics/unitree_ros/blob/master/robots/z1_description/",
    "document": "unitree_z1/README.md",
    "commit": "370c43965323c0944b433b202aac5058b5f907a9",
    "current": true
  },
  {
    "url": "https://github.com/unitreerobotics/unitree_ros/blob/master/robots/z1_description/xacro/z1.urdf",
    "document": "unitree_z1/README.md",
    "commit": "7bc6c99d5367e9dcd568fa2dbb54b6160cced324",
    "current": false
  }
]
```


## README derivation evidence

Documentation labels are conservative: an automated documented label requires an explicit affected entity and quantity. Broader conversion notes are retained here for review.

> 1. Added `<mujoco><compiler discardvisual="false" fusestatic="false"/></mujoco>` to the URDF's `<robot>` clause in order to preserve visual geometries.

## Kinematics consistency

A proper Kabsch rigid transform aligns all matched zero-pose body origins. The maximum per-origin residual and signed hinge/slide axis angles determine whether CoM can be compared; RMS is also recorded. Fewer than three non-collinear origins give insufficient kinematic coverage. CoM records that fail either required M/H or M/S check are excluded from counts and largest discrepancies. Masses, principal moments and raw joint ranges remain unchanged; a flagged range still requires convention review.

| Pair | Status | Origins / rank | RMS / maximum mm | Disagreeing / checked axes |
|---|---|---:|---:|---:|
| M/H | consistent | 7 / 2 | 5.24537054e-15 / 1.38777878e-14 | 0 / 6 |
| M/S | consistent | 7 / 2 | 5.24537054e-15 / 1.38777878e-14 | 0 / 6 |

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
    "anchor_m": "link00",
    "anchor_other": "link00",
    "rotation_other_to_m": [
      [
        1.0,
        0.0,
        -5.573215285101207e-19
      ],
      [
        0.0,
        1.0,
        0.0
      ],
      [
        2.7755575615628914e-17,
        0.0,
        1.0
      ]
    ],
    "translation_other_to_m": [
      0.0,
      0.0,
      0.0
    ],
    "rms_residual_m": 5.245370540055972e-18,
    "max_residual_m": 1.3877787807814457e-17,
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
          -5.573215285101207e-19,
          0.0,
          1.0
        ],
        "angle_rad": 5.573215285101207e-19,
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
          0.0
        ],
        "angle_rad": 0.0,
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
          0.0
        ],
        "angle_rad": 0.0,
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
          0.0
        ],
        "angle_rad": 0.0,
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
          -5.573215285101207e-19,
          0.0,
          1.0
        ],
        "angle_rad": 5.573215285101207e-19,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "joint6",
        "joint_other": "joint6",
        "axis_m": [
          1.0,
          0.0,
          0.0
        ],
        "axis_other_aligned": [
          1.0,
          0.0,
          2.7755575615628914e-17
        ],
        "angle_rad": 2.7755575615628914e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      }
    ],
    "axis_disagreements": [],
    "com_eligible": true,
    "covariance_singular_values": [
      0.1009156633005266,
      0.021138642413759078,
      0.0
    ],
    "origin_residuals_m": {
      "link00": 0.0,
      "link01": 3.2603309417842065e-20,
      "link02": 5.768277820079749e-20,
      "link03": 1.3877787807814457e-17,
      "link04": 0.0,
      "link05": 0.0,
      "link06": 0.0
    },
    "reason": "Unique proper rigid fit and matched signed axes meet the configured thresholds"
  },
  "M/S": {
    "status": "consistent",
    "matched_body_origins": 7,
    "position_threshold_m": 0.005,
    "axis_threshold_rad": 0.005,
    "residual_definition": "maximum Euclidean residual over matched body origins; Kabsch minimizes RMS, which is also recorded",
    "coordinate_frames": "each snapshot registered to its matched report anchor",
    "anchor_m": "link00",
    "anchor_other": "link00",
    "rotation_other_to_m": [
      [
        1.0,
        0.0,
        -5.573215285101207e-19
      ],
      [
        0.0,
        1.0,
        0.0
      ],
      [
        2.7755575615628914e-17,
        0.0,
        1.0
      ]
    ],
    "translation_other_to_m": [
      0.0,
      0.0,
      0.0
    ],
    "rms_residual_m": 5.245370540055972e-18,
    "max_residual_m": 1.3877787807814457e-17,
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
          -5.573215285101207e-19,
          0.0,
          1.0
        ],
        "angle_rad": 5.573215285101207e-19,
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
          0.0
        ],
        "angle_rad": 0.0,
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
          0.0
        ],
        "angle_rad": 0.0,
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
          0.0
        ],
        "angle_rad": 0.0,
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
          -5.573215285101207e-19,
          0.0,
          1.0
        ],
        "angle_rad": 5.573215285101207e-19,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "joint6",
        "joint_other": "joint6",
        "axis_m": [
          1.0,
          0.0,
          0.0
        ],
        "axis_other_aligned": [
          1.0,
          0.0,
          2.7755575615628914e-17
        ],
        "angle_rad": 2.7755575615628914e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      }
    ],
    "axis_disagreements": [],
    "com_eligible": true,
    "covariance_singular_values": [
      0.1009156633005266,
      0.021138642413759078,
      0.0
    ],
    "origin_residuals_m": {
      "link00": 0.0,
      "link01": 3.2603309417842065e-20,
      "link02": 5.768277820079749e-20,
      "link03": 1.3877787807814457e-17,
      "link04": 0.0,
      "link05": 0.0,
      "link06": 0.0
    },
    "reason": "Unique proper rigid fit and matched signed axes meet the configured thresholds"
  }
}
```


## Every reported quantity difference

Counts are quantity records, including correlated total/subtree/body mass records; they are not independent robot defects.

| Entity / quantity | M | S | H | H − M | Class | M source | S source | H source |
|---|---|---|---|---|---|---|---|---|
No differences exceeded the configured tolerances among the compared quantities.

## Raw CoM records and reporting decisions

Raw values retain the previous root-anchor registration before Kabsch; original world coordinates also remain in the snapshots. Eligible findings above use the fitted transform into M. Excluded raw records below are diagnostic numbers, not findings. No CoM suppression applies to mass or principal inertia moments.

| Entity / quantity | Raw M | Raw S | Raw H | Raw H − M | Decision | M source | S source | H source |
|---|---|---|---|---|---|---|---|---|
| robot / total_com_registered | [-0.0896292844, 1.91579508e-05, 0.115088429] | [-0.0896292841, 1.91593913e-05, 0.115088433] | [-0.0896292841, 1.91593913e-05, 0.115088433] | [3.08161177e-10, 1.44045955e-09, 3.85569114e-09] | eligible; compared after Kabsch alignment | [aggregate inputs](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_z1/z1.xml#L1) | [aggregate inputs](https://github.com/unitreerobotics/unitree_ros/blob/f10d1c6add85785542fed20fc5e3b4e66a13f64b/robots/z1_description/xacro/z1.urdf#L1) | [aggregate inputs](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/z1_description/xacro/z1.urdf#L1) |
| link00 / com_registered | [-0.00334984, -0.00013615, 0.0249584] | [-0.00334984, -0.00013615, 0.02495843] | [-0.00334984, -0.00013615, 0.02495843] | [0, 0, 3e-08] | eligible; compared after Kabsch alignment | [CoM/kinematic input L32](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_z1/z1.xml#L32) | [CoM/kinematic input L42](https://github.com/unitreerobotics/unitree_ros/blob/f10d1c6add85785542fed20fc5e3b4e66a13f64b/robots/z1_description/xacro/z1.urdf#L42) | [CoM/kinematic input L42](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/z1_description/xacro/z1.urdf#L42) |
| link01 / com_registered | [2.47e-06, -0.00025198, 0.0816717] | [2.47e-06, -0.00025198, 0.08167169] | [2.47e-06, -0.00025198, 0.08167169] | [0, 0, -9.99999999e-09] | eligible; compared after Kabsch alignment | [CoM/kinematic input L37](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_z1/z1.xml#L37) | [CoM/kinematic input L63](https://github.com/unitreerobotics/unitree_ros/blob/f10d1c6add85785542fed20fc5e3b4e66a13f64b/robots/z1_description/xacro/z1.urdf#L63) | [CoM/kinematic input L63](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/z1_description/xacro/z1.urdf#L63) |
| link02 / com_registered | [-0.110126, 0.00240029, 0.10508266] | [-0.11012601, 0.00240029, 0.10508266] | [-0.11012601, 0.00240029, 0.10508266] | [-9.99999999e-09, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L42](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_z1/z1.xml#L42) | [CoM/kinematic input L102](https://github.com/unitreerobotics/unitree_ros/blob/f10d1c6add85785542fed20fc5e3b4e66a13f64b/robots/z1_description/xacro/z1.urdf#L102) | [CoM/kinematic input L102](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/z1_description/xacro/z1.urdf#L102) |
| link03 / com_registered | [-0.243908, -0.00541815, 0.1382638] | [-0.24390792, -0.00541815, 0.13826383] | [-0.24390792, -0.00541815, 0.13826383] | [8e-08, 0, 3e-08] | eligible; compared after Kabsch alignment | [CoM/kinematic input L50](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_z1/z1.xml#L50) | [CoM/kinematic input L135](https://github.com/unitreerobotics/unitree_ros/blob/f10d1c6add85785542fed20fc5e3b4e66a13f64b/robots/z1_description/xacro/z1.urdf#L135) | [CoM/kinematic input L135](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/z1_description/xacro/z1.urdf#L135) |
| link04 / com_registered | [-0.0883332, 0.00364738, 0.15879808] | [-0.08833319, 0.00364738, 0.15879808] | [-0.08833319, 0.00364738, 0.15879808] | [9.99999999e-09, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L57](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_z1/z1.xml#L57) | [CoM/kinematic input L162](https://github.com/unitreerobotics/unitree_ros/blob/f10d1c6add85785542fed20fc5e3b4e66a13f64b/robots/z1_description/xacro/z1.urdf#L162) | [CoM/kinematic input L162](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/z1_description/xacro/z1.urdf#L162) |
| link05 / com_registered | [-0.0307847, 0, 0.16696316] | [-0.03078467, 0, 0.16696316] | [-0.03078467, 0, 0.16696316] | [3e-08, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L63](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_z1/z1.xml#L63) | [CoM/kinematic input L183](https://github.com/unitreerobotics/unitree_ros/blob/f10d1c6add85785542fed20fc5e3b4e66a13f64b/robots/z1_description/xacro/z1.urdf#L183) | [CoM/kinematic input L183](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/z1_description/xacro/z1.urdf#L183) |
| link06 / com_registered | [0.0113569, -0.00017355, 0.15906124] | [0.0113569, -0.00017355, 0.15906124] | [0.0113569, -0.00017355, 0.15906124] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L68](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_z1/z1.xml#L68) | [CoM/kinematic input L210](https://github.com/unitreerobotics/unitree_ros/blob/f10d1c6add85785542fed20fc5e3b4e66a13f64b/robots/z1_description/xacro/z1.urdf#L210) | [CoM/kinematic input L210](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/z1_description/xacro/z1.urdf#L210) |

## Mass accounting

Every contributing compiled body mass is listed here so total/subtree sums can be checked. Links point to explicit inertials or to geometry inputs when the compiler inferred a mass. CoM links identify inertial inputs; world coordinates additionally use the ancestor transforms and the registration recorded below.

| M body | M kg / source | S kg / source | H kg / source |
|---|---|---|---|
| link00 | 0.472475 / [input L32](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_z1/z1.xml#L32) | 0.47247481 / [input L43](https://github.com/unitreerobotics/unitree_ros/blob/f10d1c6add85785542fed20fc5e3b4e66a13f64b/robots/z1_description/xacro/z1.urdf#L43) | 0.47247481 / [input L43](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/z1_description/xacro/z1.urdf#L43) |
| link01 | 0.673326 / [input L37](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_z1/z1.xml#L37) | 0.67332551 / [input L64](https://github.com/unitreerobotics/unitree_ros/blob/f10d1c6add85785542fed20fc5e3b4e66a13f64b/robots/z1_description/xacro/z1.urdf#L64) | 0.67332551 / [input L64](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/z1_description/xacro/z1.urdf#L64) |
| link02 | 1.19132 / [input L42](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_z1/z1.xml#L42) | 1.19132258 / [input L103](https://github.com/unitreerobotics/unitree_ros/blob/f10d1c6add85785542fed20fc5e3b4e66a13f64b/robots/z1_description/xacro/z1.urdf#L103) | 1.19132258 / [input L103](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/z1_description/xacro/z1.urdf#L103) |
| link03 | 0.839409 / [input L50](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_z1/z1.xml#L50) | 0.83940874 / [input L136](https://github.com/unitreerobotics/unitree_ros/blob/f10d1c6add85785542fed20fc5e3b4e66a13f64b/robots/z1_description/xacro/z1.urdf#L136) | 0.83940874 / [input L136](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/z1_description/xacro/z1.urdf#L136) |
| link04 | 0.564046 / [input L57](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_z1/z1.xml#L57) | 0.56404563 / [input L163](https://github.com/unitreerobotics/unitree_ros/blob/f10d1c6add85785542fed20fc5e3b4e66a13f64b/robots/z1_description/xacro/z1.urdf#L163) | 0.56404563 / [input L163](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/z1_description/xacro/z1.urdf#L163) |
| link05 | 0.389385 / [input L63](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_z1/z1.xml#L63) | 0.38938492 / [input L184](https://github.com/unitreerobotics/unitree_ros/blob/f10d1c6add85785542fed20fc5e3b4e66a13f64b/robots/z1_description/xacro/z1.urdf#L184) | 0.38938492 / [input L184](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/z1_description/xacro/z1.urdf#L184) |
| link06 | 0.288758 / [input L68](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_z1/z1.xml#L68) | 0.28875807 / [input L211](https://github.com/unitreerobotics/unitree_ros/blob/f10d1c6add85785542fed20fc5e3b4e66a13f64b/robots/z1_description/xacro/z1.urdf#L211) | 0.28875807 / [input L211](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/z1_description/xacro/z1.urdf#L211) |

## Coverage and unmatched elements

```json
{
  "mapping_h": {
    "bodies": {
      "link00": "link00",
      "link01": "link01",
      "link02": "link02",
      "link03": "link03",
      "link04": "link04",
      "link05": "link05",
      "link06": "link06"
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
      "link00": "name",
      "link01": "name",
      "link02": "name",
      "link03": "name",
      "link04": "name",
      "link05": "name",
      "link06": "name"
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
    "unmatched_upstream_bodies": [],
    "unmatched_m_joints": [],
    "unmatched_upstream_joints": [],
    "registration_anchor": {
      "M": "link00",
      "H": "link00",
      "root_unmatched": false
    }
  },
  "mapping_s": {
    "bodies": {
      "link00": "link00",
      "link01": "link01",
      "link02": "link02",
      "link03": "link03",
      "link04": "link04",
      "link05": "link05",
      "link06": "link06"
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
      "link00": "name",
      "link01": "name",
      "link02": "name",
      "link03": "name",
      "link04": "name",
      "link05": "name",
      "link06": "name"
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
    "unmatched_upstream_bodies": [],
    "unmatched_m_joints": [],
    "unmatched_upstream_joints": [],
    "registration_anchor": {
      "M": "link00",
      "S": "link00"
    }
  },
  "unavailable": [
    {
      "entity": "joint1",
      "other_entity": "joint1",
      "quantity": "force",
      "tolerance": "limit",
      "m": 30.0,
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
      "other": 3.1415,
      "s": 3.1415,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "joint2",
      "other_entity": "joint2",
      "quantity": "force",
      "tolerance": "limit",
      "m": 60.0,
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
      "other": 3.1415,
      "s": 3.1415,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "joint3",
      "other_entity": "joint3",
      "quantity": "force",
      "tolerance": "limit",
      "m": 30.0,
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
      "other": 3.1415,
      "s": 3.1415,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "joint4",
      "other_entity": "joint4",
      "quantity": "force",
      "tolerance": "limit",
      "m": 30.0,
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
      "other": 3.1415,
      "s": 3.1415,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "joint5",
      "other_entity": "joint5",
      "quantity": "force",
      "tolerance": "limit",
      "m": 30.0,
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
      "other": 3.1415,
      "s": 3.1415,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "joint6",
      "other_entity": "joint6",
      "quantity": "force",
      "tolerance": "limit",
      "m": 30.0,
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
      "other": 3.1415,
      "s": 3.1415,
      "reason": "quantity absent or not enforced/declared on one side"
    }
  ]
}
```

## Limits unavailable for a like-for-like simulator comparison

URDF effort and velocity tags are manufacturer declarations; MuJoCo ignores them. Missing enforced quantities are not interpreted as zero. The available values are shown for review and excluded from STALE counts.

| Joint / quantity | M | S | H / declared upstream |
|---|---|---|---|
| joint1 / force | 30 | unavailable | unavailable |
| joint1 / velocity | unavailable | 3.1415 | 3.1415 |
| joint2 / force | 60 | unavailable | unavailable |
| joint2 / velocity | unavailable | 3.1415 | 3.1415 |
| joint3 / force | 30 | unavailable | unavailable |
| joint3 / velocity | unavailable | 3.1415 | 3.1415 |
| joint4 / force | 30 | unavailable | unavailable |
| joint4 / velocity | unavailable | 3.1415 | 3.1415 |
| joint5 / force | 30 | unavailable | unavailable |
| joint5 / velocity | unavailable | 3.1415 | 3.1415 |
| joint6 / force | 30 | unavailable | unavailable |
| joint6 / velocity | unavailable | 3.1415 | 3.1415 |
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
[
  "https://github.com/unitreerobotics/unitree_ros robots/z1_description/xacro/const.xacro at 157ff950351e5f535e03c5d85a16b7d594b3dbcc: ValueError: XML has no robot bodies; it is an include/extension fragment, not a standalone source",
  "https://github.com/unitreerobotics/unitree_ros robots/z1_description/xacro/gazebo.xacro at 157ff950351e5f535e03c5d85a16b7d594b3dbcc: ValueError: XML has no robot bodies; it is an include/extension fragment, not a standalone source",
  "https://github.com/unitreerobotics/unitree_ros robots/z1_description/xacro/transmission.xacro at 157ff950351e5f535e03c5d85a16b7d594b3dbcc: ValueError: XML has no robot bodies; it is an include/extension fragment, not a standalone source"
]
```

## History inputs

```json
[
  "robots/z1_description/meshes/visual/z1_Link00.dae",
  "robots/z1_description/meshes/visual/z1_Link01.dae",
  "robots/z1_description/meshes/visual/z1_Link02.dae",
  "robots/z1_description/meshes/visual/z1_Link03.dae",
  "robots/z1_description/meshes/visual/z1_Link04.dae",
  "robots/z1_description/meshes/visual/z1_Link05.dae",
  "robots/z1_description/meshes/visual/z1_Link06.dae",
  "robots/z1_description/meshes/z1_Link00.dae",
  "robots/z1_description/meshes/z1_Link01.dae",
  "robots/z1_description/meshes/z1_Link02.dae",
  "robots/z1_description/meshes/z1_Link03.dae",
  "robots/z1_description/meshes/z1_Link04.dae",
  "robots/z1_description/meshes/z1_Link05.dae",
  "robots/z1_description/meshes/z1_Link06.dae",
  "robots/z1_description/xacro/z1.urdf"
]
```

## Self comparisons

```json
[
  {
    "file": "unitree_z1/z1.xml",
    "status": "passed",
    "findings": 0
  },
  {
    "file": "unitree_z1/z1_gripper.xml",
    "status": "passed",
    "findings": 0
  }
]
```

## Sensitivity

```json
{
  "0.5": {
    "provenance_method": "dated match",
    "counts": {},
    "classifications_changed": 0,
    "finding_membership_changes": 0
  },
  "2": {
    "provenance_method": "dated match",
    "counts": {},
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
      "unitree_z1/z1.xml"
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
      "world"
    ],
    "assets_loaded": 7,
    "mesh_conversions": [
      {
        "file": "robots/z1_description/meshes/visual/z1_Link00.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "robots/z1_description/meshes/visual/z1_Link01.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "robots/z1_description/meshes/visual/z1_Link02.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "robots/z1_description/meshes/visual/z1_Link03.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "robots/z1_description/meshes/visual/z1_Link04.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "robots/z1_description/meshes/visual/z1_Link05.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "robots/z1_description/meshes/visual/z1_Link06.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      }
    ],
    "nonphysical_normalizations": [],
    "xacro_arguments": {},
    "source_dependencies": [
      "robots/z1_description/xacro/z1.urdf",
      "robots/z1_description/meshes/visual/z1_Link00.dae",
      "robots/z1_description/meshes/visual/z1_Link01.dae",
      "robots/z1_description/meshes/visual/z1_Link02.dae",
      "robots/z1_description/meshes/visual/z1_Link03.dae",
      "robots/z1_description/meshes/visual/z1_Link04.dae",
      "robots/z1_description/meshes/visual/z1_Link05.dae",
      "robots/z1_description/meshes/visual/z1_Link06.dae"
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
  },
  "S": {
    "geometry_stripped": false,
    "missing_explicit_inertials": [
      "world"
    ],
    "assets_loaded": 7,
    "mesh_conversions": [
      {
        "file": "robots/z1_description/meshes/visual/z1_Link00.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "robots/z1_description/meshes/visual/z1_Link01.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "robots/z1_description/meshes/visual/z1_Link02.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "robots/z1_description/meshes/visual/z1_Link03.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "robots/z1_description/meshes/visual/z1_Link04.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "robots/z1_description/meshes/visual/z1_Link05.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "robots/z1_description/meshes/visual/z1_Link06.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      }
    ],
    "nonphysical_normalizations": [],
    "xacro_arguments": {},
    "source_dependencies": [
      "robots/z1_description/xacro/z1.urdf",
      "robots/z1_description/meshes/visual/z1_Link00.dae",
      "robots/z1_description/meshes/visual/z1_Link01.dae",
      "robots/z1_description/meshes/visual/z1_Link02.dae",
      "robots/z1_description/meshes/visual/z1_Link03.dae",
      "robots/z1_description/meshes/visual/z1_Link04.dae",
      "robots/z1_description/meshes/visual/z1_Link05.dae",
      "robots/z1_description/meshes/visual/z1_Link06.dae"
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
    "M",
    "S"
  ],
  "self_variants_recompiled": 2,
  "historical_snapshots_reused": 3,
  "primary_physics_unchanged": true,
  "source_matching": "original raw-value provenance criteria retained; kinematic guard applies to reported CoM"
}
```
