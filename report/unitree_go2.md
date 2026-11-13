# unitree_go2

Status: **complete**. Provenance: **none**, confidence **none**.

No public revision matches all comparable quantities. Class: NO MATCHING SOURCE; never counted as STALE.

M: `https://github.com/google-deepmind/mujoco_menagerie`, `unitree_go2/go2.xml`, commit `370c43965323c0944b433b202aac5058b5f907a9`.
H: `https://github.com/unitreerobotics/unitree_ros`, `robots/go2_description/urdf/go2_description.urdf`, commit `157ff950351e5f535e03c5d85a16b7d594b3dbcc`.
S: unavailable. A machine-readable H can still be compared to M; no-match differences are never counted as STALE.

Limit semantics: MJCF effort values are supported actuator torque/force envelopes. URDF effort and velocity values are manufacturer declarations retained from XML; MuJoCo does not enforce those tags. Such declaration comparisons are explicitly distinct from compiled inertial/range quantities.


## Source evidence

```json
[
  {
    "url": "https://github.com/google-deepmind/mujoco_menagerie/pull/57",
    "document": "git commit message",
    "commit": "ca7031c3b93adb5543c2dad8746286c6f2ff5ddd",
    "current": false
  },
  {
    "url": "https://github.com/kevinzakka/obj2mjcf",
    "document": "unitree_go2/README.md",
    "commit": "370c43965323c0944b433b202aac5058b5f907a9",
    "current": true
  },
  {
    "url": "https://github.com/lonelyfluency",
    "document": "unitree_go2/README.md",
    "commit": "370c43965323c0944b433b202aac5058b5f907a9",
    "current": true
  },
  {
    "url": "https://github.com/unitreerobotics/unitree_ros/tree/master/robots/go2_description",
    "document": "unitree_go2/README.md",
    "commit": "370c43965323c0944b433b202aac5058b5f907a9",
    "current": true
  },
  {
    "url": "https://github.com/unitreerobotics/unitree_ros/tree/master/robots/go2_description/meshes",
    "document": "unitree_go2/README.md",
    "commit": "370c43965323c0944b433b202aac5058b5f907a9",
    "current": true
  },
  {
    "url": "https://github.com/unitreerobotics/unitree_mujoco/tree/main/data/a1/meshes",
    "document": "unitree_go2/README.md",
    "commit": "a5836a9410b36a7f69ad575e1436403214116039",
    "current": false
  }
]
```


## README derivation evidence

Documentation labels are conservative: an automated documented label requires an explicit affected entity and quantity. Broader conversion notes are retained here for review.

> 3. Added `<mujoco> <compiler discardvisual="false" strippath="false" fusestatic="false"/> </mujoco>` to the URDF's

## Kinematics consistency

A proper Kabsch rigid transform aligns all matched zero-pose body origins. The maximum per-origin residual and signed hinge/slide axis angles determine whether CoM can be compared; RMS is also recorded. Fewer than three non-collinear origins give insufficient kinematic coverage. CoM records that fail either required M/H or M/S check are excluded from counts and largest discrepancies. Masses, principal moments and raw joint ranges remain unchanged; a flagged range still requires convention review.

| Pair | Status | Origins / rank | RMS / maximum mm | Disagreeing / checked axes |
|---|---|---:|---:|---:|
| M/H | consistent | 13 / 3 | 4.90640377e-14 / 6.20633538e-14 | 0 / 12 |

Exact fitted transforms, per-origin residuals, thresholds and axis vectors:

```json
{
  "M/H": {
    "status": "consistent",
    "matched_body_origins": 13,
    "position_threshold_m": 0.005,
    "axis_threshold_rad": 0.005,
    "residual_definition": "maximum Euclidean residual over matched body origins; Kabsch minimizes RMS, which is also recorded",
    "coordinate_frames": "each snapshot registered to its matched report anchor",
    "anchor_m": "base",
    "anchor_other": "base",
    "rotation_other_to_m": [
      [
        1.0,
        -1.810559851952202e-17,
        1.2711673304503802e-17
      ],
      [
        1.810559851952201e-17,
        0.9999999999999996,
        5.4482936637544203e-17
      ],
      [
        -1.2711673304503798e-17,
        6.00156998413033e-17,
        0.9999999999999999
      ]
    ],
    "translation_other_to_m": [
      8.331035119567105e-19,
      3.570727847322127e-18,
      -1.3877787807814457e-17
    ],
    "rms_residual_m": 4.906403771626902e-17,
    "max_residual_m": 6.206335383118183e-17,
    "fit_rank": 3,
    "axis_checks": [
      {
        "joint_m": "FL_hip_joint",
        "joint_other": "FL_hip_joint",
        "axis_m": [
          1.0,
          0.0,
          0.0
        ],
        "axis_other_aligned": [
          1.0,
          1.810559851952201e-17,
          -1.2711673304503798e-17
        ],
        "angle_rad": 2.2122371842787386e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "FL_thigh_joint",
        "joint_other": "FL_thigh_joint",
        "axis_m": [
          0.0,
          1.0,
          0.0
        ],
        "axis_other_aligned": [
          -1.810559851952203e-17,
          1.0,
          6.001569984130332e-17
        ],
        "angle_rad": 6.268729476689462e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "FL_calf_joint",
        "joint_other": "FL_calf_joint",
        "axis_m": [
          0.0,
          1.0,
          0.0
        ],
        "axis_other_aligned": [
          -1.810559851952203e-17,
          1.0,
          6.001569984130332e-17
        ],
        "angle_rad": 6.268729476689462e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "FR_hip_joint",
        "joint_other": "FR_hip_joint",
        "axis_m": [
          1.0,
          0.0,
          0.0
        ],
        "axis_other_aligned": [
          1.0,
          1.810559851952201e-17,
          -1.2711673304503798e-17
        ],
        "angle_rad": 2.2122371842787386e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "FR_thigh_joint",
        "joint_other": "FR_thigh_joint",
        "axis_m": [
          0.0,
          1.0,
          0.0
        ],
        "axis_other_aligned": [
          -1.810559851952203e-17,
          1.0,
          6.001569984130332e-17
        ],
        "angle_rad": 6.268729476689462e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "FR_calf_joint",
        "joint_other": "FR_calf_joint",
        "axis_m": [
          0.0,
          1.0,
          0.0
        ],
        "axis_other_aligned": [
          -1.810559851952203e-17,
          1.0,
          6.001569984130332e-17
        ],
        "angle_rad": 6.268729476689462e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "RL_hip_joint",
        "joint_other": "RL_hip_joint",
        "axis_m": [
          1.0,
          0.0,
          0.0
        ],
        "axis_other_aligned": [
          1.0,
          1.810559851952201e-17,
          -1.2711673304503798e-17
        ],
        "angle_rad": 2.2122371842787386e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "RL_thigh_joint",
        "joint_other": "RL_thigh_joint",
        "axis_m": [
          0.0,
          1.0,
          0.0
        ],
        "axis_other_aligned": [
          -1.810559851952203e-17,
          1.0,
          6.001569984130332e-17
        ],
        "angle_rad": 6.268729476689462e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "RL_calf_joint",
        "joint_other": "RL_calf_joint",
        "axis_m": [
          0.0,
          1.0,
          0.0
        ],
        "axis_other_aligned": [
          -1.810559851952203e-17,
          1.0,
          6.001569984130332e-17
        ],
        "angle_rad": 6.268729476689462e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "RR_hip_joint",
        "joint_other": "RR_hip_joint",
        "axis_m": [
          1.0,
          0.0,
          0.0
        ],
        "axis_other_aligned": [
          1.0,
          1.810559851952201e-17,
          -1.2711673304503798e-17
        ],
        "angle_rad": 2.2122371842787386e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "RR_thigh_joint",
        "joint_other": "RR_thigh_joint",
        "axis_m": [
          0.0,
          1.0,
          0.0
        ],
        "axis_other_aligned": [
          -1.810559851952203e-17,
          1.0,
          6.001569984130332e-17
        ],
        "angle_rad": 6.268729476689462e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "RR_calf_joint",
        "joint_other": "RR_calf_joint",
        "axis_m": [
          0.0,
          1.0,
          0.0
        ],
        "axis_other_aligned": [
          -1.810559851952203e-17,
          1.0,
          6.001569984130332e-17
        ],
        "angle_rad": 6.268729476689462e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      }
    ],
    "axis_disagreements": [],
    "com_eligible": true,
    "covariance_singular_values": [
      0.44884272,
      0.16996100000000006,
      0.12563723076923072
    ],
    "origin_residuals_m": {
      "base": 1.4353994331195756e-17,
      "FL_hip": 1.5219352606506696e-17,
      "FL_thigh": 5.605841993179073e-17,
      "FL_calf": 6.206335383118183e-17,
      "FR_hip": 3.3707749898378274e-17,
      "FR_thigh": 6.082294539218795e-17,
      "FR_calf": 6.206335383118183e-17,
      "RL_hip": 1.6341544605665936e-17,
      "RL_thigh": 5.558670002820992e-17,
      "RL_calf": 6.206335383118183e-17,
      "RR_hip": 2.52043769557036e-17,
      "RR_thigh": 5.898435815276767e-17,
      "RR_calf": 6.206335383118183e-17
    },
    "reason": "Unique proper rigid fit and matched signed axes meet the configured thresholds"
  }
}
```


## Every reported quantity difference

Counts are quantity records, including correlated total/subtree/body mass records; they are not independent robot defects.

| Entity / quantity | M | S | H | H − M | Class | M source | S source | H source |
|---|---|---|---|---|---|---|---|---|
| robot / total_mass | 15.206408 | unavailable | 16.2764066 | 1.06999862 | NO MATCHING SOURCE | [aggregate inputs](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_go2/go2.xml#L1) | unavailable | [aggregate inputs](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/go2_description/urdf/go2_description.urdf#L1) |
| robot / total_com_registered | [0.00887523158, 0, -0.0348709211] | unavailable | [0.00832729174, 1.94635735e-18, -0.0325815973] | [-0.00054793984, 1.94635735e-18, 0.00228932377] | NO MATCHING SOURCE | [aggregate inputs](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_go2/go2.xml#L1) | unavailable | [aggregate inputs](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/go2_description/urdf/go2_description.urdf#L1) |
| base / subtree_mass | 15.206408 | unavailable | 16.2764066 | 1.06999862 | NO MATCHING SOURCE | [subtree root L64](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_go2/go2.xml#L64) | unavailable | [subtree root L3](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/go2_description/urdf/go2_description.urdf#L3) |
| FL_hip / subtree_mass | 2.071352 | unavailable | 2.24935166 | 0.177999655 | NO MATCHING SOURCE | [subtree root L77](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_go2/go2.xml#L77) | unavailable | [subtree root L60](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/go2_description/urdf/go2_description.urdf#L60) |
| FL_thigh / subtree_mass | 1.393352 | unavailable | 1.48235166 | 0.0889996553 | NO MATCHING SOURCE | [subtree root L84](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_go2/go2.xml#L84) | unavailable | [subtree root L98](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/go2_description/urdf/go2_description.urdf#L98) |
| FL_calf / mass | 0.241352 | unavailable | 0.154 | -0.087352 | NO MATCHING SOURCE | [input L94](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_go2/go2.xml#L94) | unavailable | [input L139](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/go2_description/urdf/go2_description.urdf#L139) |
| FL_calf / com_registered | [0.19969595, 0.141377879, -0.354417] | unavailable | [0.19888, 0.141025, -0.328] | [-0.00081595, -0.000352879, 0.026417] | NO MATCHING SOURCE | [CoM/kinematic input L94](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_go2/go2.xml#L94) | unavailable | [CoM/kinematic input L138](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/go2_description/urdf/go2_description.urdf#L138) |
| FL_calf / principal_moments | [5.31397e-05, 0.00146356, 0.0014901] | unavailable | [3.25534208e-05, 0.00108027101, 0.00110007556] | [-2.05862792e-05, -0.000383288986, -0.000390024435] | NO MATCHING SOURCE | [inertia input L94](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_go2/go2.xml#L94) | unavailable | [inertia input L140](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/go2_description/urdf/go2_description.urdf#L140) |
| FR_hip / subtree_mass | 2.071352 | unavailable | 2.24935166 | 0.177999655 | NO MATCHING SOURCE | [subtree root L107](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_go2/go2.xml#L107) | unavailable | [subtree root L227](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/go2_description/urdf/go2_description.urdf#L227) |
| FR_thigh / subtree_mass | 1.393352 | unavailable | 1.48235166 | 0.0889996553 | NO MATCHING SOURCE | [subtree root L114](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_go2/go2.xml#L114) | unavailable | [subtree root L265](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/go2_description/urdf/go2_description.urdf#L265) |
| FR_calf / mass | 0.241352 | unavailable | 0.154 | -0.087352 | NO MATCHING SOURCE | [input L124](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_go2/go2.xml#L124) | unavailable | [input L306](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/go2_description/urdf/go2_description.urdf#L306) |
| FR_calf / com_registered | [0.19969595, -0.141377879, -0.354417] | unavailable | [0.19888, -0.141025, -0.328] | [-0.00081595, 0.000352879, 0.026417] | NO MATCHING SOURCE | [CoM/kinematic input L124](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_go2/go2.xml#L124) | unavailable | [CoM/kinematic input L305](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/go2_description/urdf/go2_description.urdf#L305) |
| FR_calf / principal_moments | [5.31397e-05, 0.00146356, 0.0014901] | unavailable | [3.25534208e-05, 0.00108027101, 0.00110007556] | [-2.05862792e-05, -0.000383288986, -0.000390024435] | NO MATCHING SOURCE | [inertia input L124](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_go2/go2.xml#L124) | unavailable | [inertia input L307](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/go2_description/urdf/go2_description.urdf#L307) |
| RL_hip / subtree_mass | 2.071352 | unavailable | 2.24935166 | 0.177999655 | NO MATCHING SOURCE | [subtree root L137](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_go2/go2.xml#L137) | unavailable | [subtree root L394](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/go2_description/urdf/go2_description.urdf#L394) |
| RL_thigh / subtree_mass | 1.393352 | unavailable | 1.48235166 | 0.0889996553 | NO MATCHING SOURCE | [subtree root L144](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_go2/go2.xml#L144) | unavailable | [subtree root L432](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/go2_description/urdf/go2_description.urdf#L432) |
| RL_calf / mass | 0.241352 | unavailable | 0.154 | -0.087352 | NO MATCHING SOURCE | [input L154](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_go2/go2.xml#L154) | unavailable | [input L473](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/go2_description/urdf/go2_description.urdf#L473) |
| RL_calf / com_registered | [-0.18710405, 0.141377879, -0.354417] | unavailable | [-0.18792, 0.141025, -0.328] | [-0.00081595, -0.000352879, 0.026417] | NO MATCHING SOURCE | [CoM/kinematic input L154](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_go2/go2.xml#L154) | unavailable | [CoM/kinematic input L472](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/go2_description/urdf/go2_description.urdf#L472) |
| RL_calf / principal_moments | [5.31397e-05, 0.00146356, 0.0014901] | unavailable | [3.25534208e-05, 0.00108027101, 0.00110007556] | [-2.05862792e-05, -0.000383288986, -0.000390024435] | NO MATCHING SOURCE | [inertia input L154](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_go2/go2.xml#L154) | unavailable | [inertia input L474](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/go2_description/urdf/go2_description.urdf#L474) |
| RR_hip / subtree_mass | 2.071352 | unavailable | 2.24935166 | 0.177999655 | NO MATCHING SOURCE | [subtree root L167](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_go2/go2.xml#L167) | unavailable | [subtree root L561](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/go2_description/urdf/go2_description.urdf#L561) |
| RR_thigh / subtree_mass | 1.393352 | unavailable | 1.48235166 | 0.0889996553 | NO MATCHING SOURCE | [subtree root L174](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_go2/go2.xml#L174) | unavailable | [subtree root L599](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/go2_description/urdf/go2_description.urdf#L599) |
| RR_calf / mass | 0.241352 | unavailable | 0.154 | -0.087352 | NO MATCHING SOURCE | [input L184](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_go2/go2.xml#L184) | unavailable | [input L640](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/go2_description/urdf/go2_description.urdf#L640) |
| RR_calf / com_registered | [-0.18710405, -0.141377879, -0.354417] | unavailable | [-0.18792, -0.141025, -0.328] | [-0.00081595, 0.000352879, 0.026417] | NO MATCHING SOURCE | [CoM/kinematic input L184](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_go2/go2.xml#L184) | unavailable | [CoM/kinematic input L639](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/go2_description/urdf/go2_description.urdf#L639) |
| RR_calf / principal_moments | [5.31397e-05, 0.00146356, 0.0014901] | unavailable | [3.25534208e-05, 0.00108027101, 0.00110007556] | [-2.05862792e-05, -0.000383288986, -0.000390024435] | NO MATCHING SOURCE | [inertia input L184](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_go2/go2.xml#L184) | unavailable | [inertia input L641](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/go2_description/urdf/go2_description.urdf#L641) |

## Raw CoM records and reporting decisions

Raw values retain the previous root-anchor registration before Kabsch; original world coordinates also remain in the snapshots. Eligible findings above use the fitted transform into M. Excluded raw records below are diagnostic numbers, not findings. No CoM suppression applies to mass or principal inertia moments.

| Entity / quantity | Raw M | Raw S | Raw H | Raw H − M | Decision | M source | S source | H source |
|---|---|---|---|---|---|---|---|---|
| robot / total_com_registered | [0.00887523158, 0, -0.0348709211] | unavailable | [0.00832729174, 0, -0.0325815973] | [-0.00054793984, 0, 0.00228932377] | eligible; compared after Kabsch alignment | [aggregate inputs](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_go2/go2.xml#L1) | unavailable | [aggregate inputs](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/go2_description/urdf/go2_description.urdf#L1) |
| base / com_registered | [0.021112, 0, -0.005366] | unavailable | [0.021112, 0, -0.005366] | [0, 0, -1.82145965e-17] | eligible; compared after Kabsch alignment | [CoM/kinematic input L66](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_go2/go2.xml#L66) | unavailable | [CoM/kinematic input L5](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/go2_description/urdf/go2_description.urdf#L5) |
| FL_hip / com_registered | [0.188, 0.04844, -0.000105] | unavailable | [0.188, 0.04844, -0.000105] | [0, 0, 2.17382536e-17] | eligible; compared after Kabsch alignment | [CoM/kinematic input L79](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_go2/go2.xml#L79) | unavailable | [CoM/kinematic input L62](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/go2_description/urdf/go2_description.urdf#L62) |
| FL_thigh / com_registered | [0.18966, 0.1197, -0.0327] | unavailable | [0.18966, 0.1197, -0.0327] | [0, 0, 6.9388939e-18] | eligible; compared after Kabsch alignment | [CoM/kinematic input L86](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_go2/go2.xml#L86) | unavailable | [CoM/kinematic input L100](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/go2_description/urdf/go2_description.urdf#L100) |
| FL_calf / com_registered | [0.19969595, 0.141377879, -0.354417] | unavailable | [0.19888, 0.141025, -0.328] | [-0.00081595, -0.000352879, 0.026417] | eligible; compared after Kabsch alignment | [CoM/kinematic input L94](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_go2/go2.xml#L94) | unavailable | [CoM/kinematic input L138](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/go2_description/urdf/go2_description.urdf#L138) |
| FR_hip / com_registered | [0.188, -0.04844, -0.000105] | unavailable | [0.188, -0.04844, -0.000105] | [0, 0, 2.17382536e-17] | eligible; compared after Kabsch alignment | [CoM/kinematic input L109](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_go2/go2.xml#L109) | unavailable | [CoM/kinematic input L229](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/go2_description/urdf/go2_description.urdf#L229) |
| FR_thigh / com_registered | [0.18966, -0.1197, -0.0327] | unavailable | [0.18966, -0.1197, -0.0327] | [0, 0, 6.9388939e-18] | eligible; compared after Kabsch alignment | [CoM/kinematic input L116](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_go2/go2.xml#L116) | unavailable | [CoM/kinematic input L267](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/go2_description/urdf/go2_description.urdf#L267) |
| FR_calf / com_registered | [0.19969595, -0.141377879, -0.354417] | unavailable | [0.19888, -0.141025, -0.328] | [-0.00081595, 0.000352879, 0.026417] | eligible; compared after Kabsch alignment | [CoM/kinematic input L124](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_go2/go2.xml#L124) | unavailable | [CoM/kinematic input L305](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/go2_description/urdf/go2_description.urdf#L305) |
| RL_hip / com_registered | [-0.188, 0.04844, -0.000105] | unavailable | [-0.188, 0.04844, -0.000105] | [0, 0, 2.17382536e-17] | eligible; compared after Kabsch alignment | [CoM/kinematic input L139](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_go2/go2.xml#L139) | unavailable | [CoM/kinematic input L396](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/go2_description/urdf/go2_description.urdf#L396) |
| RL_thigh / com_registered | [-0.19714, 0.1197, -0.0327] | unavailable | [-0.19714, 0.1197, -0.0327] | [0, 0, 6.9388939e-18] | eligible; compared after Kabsch alignment | [CoM/kinematic input L146](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_go2/go2.xml#L146) | unavailable | [CoM/kinematic input L434](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/go2_description/urdf/go2_description.urdf#L434) |
| RL_calf / com_registered | [-0.18710405, 0.141377879, -0.354417] | unavailable | [-0.18792, 0.141025, -0.328] | [-0.00081595, -0.000352879, 0.026417] | eligible; compared after Kabsch alignment | [CoM/kinematic input L154](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_go2/go2.xml#L154) | unavailable | [CoM/kinematic input L472](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/go2_description/urdf/go2_description.urdf#L472) |
| RR_hip / com_registered | [-0.188, -0.04844, -0.000105] | unavailable | [-0.188, -0.04844, -0.000105] | [0, 0, 2.17382536e-17] | eligible; compared after Kabsch alignment | [CoM/kinematic input L169](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_go2/go2.xml#L169) | unavailable | [CoM/kinematic input L563](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/go2_description/urdf/go2_description.urdf#L563) |
| RR_thigh / com_registered | [-0.19714, -0.1197, -0.0327] | unavailable | [-0.19714, -0.1197, -0.0327] | [0, 0, 6.9388939e-18] | eligible; compared after Kabsch alignment | [CoM/kinematic input L176](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_go2/go2.xml#L176) | unavailable | [CoM/kinematic input L601](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/go2_description/urdf/go2_description.urdf#L601) |
| RR_calf / com_registered | [-0.18710405, -0.141377879, -0.354417] | unavailable | [-0.18792, -0.141025, -0.328] | [-0.00081595, 0.000352879, 0.026417] | eligible; compared after Kabsch alignment | [CoM/kinematic input L184](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_go2/go2.xml#L184) | unavailable | [CoM/kinematic input L639](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/go2_description/urdf/go2_description.urdf#L639) |

## Mass accounting

Every contributing compiled body mass is listed here so total/subtree sums can be checked. Links point to explicit inertials or to geometry inputs when the compiler inferred a mass. CoM links identify inertial inputs; world coordinates additionally use the ancestor transforms and the registration recorded below.

| M body | M kg / source | S kg / source | H kg / source |
|---|---|---|---|
| base | 6.921 / [input L66](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_go2/go2.xml#L66) | unavailable | 6.921 / [input L6](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/go2_description/urdf/go2_description.urdf#L6) |
| FL_hip | 0.678 / [input L79](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_go2/go2.xml#L79) | unavailable | 0.678 / [input L63](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/go2_description/urdf/go2_description.urdf#L63) |
| FL_thigh | 1.152 / [input L86](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_go2/go2.xml#L86) | unavailable | 1.152 / [input L101](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/go2_description/urdf/go2_description.urdf#L101) |
| FL_calf | 0.241352 / [input L94](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_go2/go2.xml#L94) | unavailable | 0.154 / [input L139](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/go2_description/urdf/go2_description.urdf#L139) |
| FR_hip | 0.678 / [input L109](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_go2/go2.xml#L109) | unavailable | 0.678 / [input L230](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/go2_description/urdf/go2_description.urdf#L230) |
| FR_thigh | 1.152 / [input L116](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_go2/go2.xml#L116) | unavailable | 1.152 / [input L268](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/go2_description/urdf/go2_description.urdf#L268) |
| FR_calf | 0.241352 / [input L124](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_go2/go2.xml#L124) | unavailable | 0.154 / [input L306](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/go2_description/urdf/go2_description.urdf#L306) |
| RL_hip | 0.678 / [input L139](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_go2/go2.xml#L139) | unavailable | 0.678 / [input L397](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/go2_description/urdf/go2_description.urdf#L397) |
| RL_thigh | 1.152 / [input L146](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_go2/go2.xml#L146) | unavailable | 1.152 / [input L435](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/go2_description/urdf/go2_description.urdf#L435) |
| RL_calf | 0.241352 / [input L154](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_go2/go2.xml#L154) | unavailable | 0.154 / [input L473](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/go2_description/urdf/go2_description.urdf#L473) |
| RR_hip | 0.678 / [input L169](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_go2/go2.xml#L169) | unavailable | 0.678 / [input L564](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/go2_description/urdf/go2_description.urdf#L564) |
| RR_thigh | 1.152 / [input L176](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_go2/go2.xml#L176) | unavailable | 1.152 / [input L602](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/go2_description/urdf/go2_description.urdf#L602) |
| RR_calf | 0.241352 / [input L184](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_go2/go2.xml#L184) | unavailable | 0.154 / [input L640](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/go2_description/urdf/go2_description.urdf#L640) |
| upstream-only FL_calf_rotor | unavailable | unavailable | 0.089 / [input L193](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/go2_description/urdf/go2_description.urdf#L193) |
| upstream-only FL_calflower | unavailable | unavailable | 0.0247086262 / [geometry/inference input L162](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/go2_description/urdf/go2_description.urdf#L162) |
| upstream-only FL_calflower1 | unavailable | unavailable | 0.0226430291 / [geometry/inference input L176](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/go2_description/urdf/go2_description.urdf#L176) |
| upstream-only FL_foot | unavailable | unavailable | 0.04 / [input L205](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/go2_description/urdf/go2_description.urdf#L205) |
| upstream-only FL_hip_rotor | unavailable | unavailable | 0.089 / [input L89](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/go2_description/urdf/go2_description.urdf#L89) |
| upstream-only FL_thigh_rotor | unavailable | unavailable | 0.089 / [input L127](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/go2_description/urdf/go2_description.urdf#L127) |
| upstream-only FR_calf_rotor | unavailable | unavailable | 0.089 / [input L360](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/go2_description/urdf/go2_description.urdf#L360) |
| upstream-only FR_calflower | unavailable | unavailable | 0.0247086262 / [geometry/inference input L329](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/go2_description/urdf/go2_description.urdf#L329) |
| upstream-only FR_calflower1 | unavailable | unavailable | 0.0226430291 / [geometry/inference input L343](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/go2_description/urdf/go2_description.urdf#L343) |
| upstream-only FR_foot | unavailable | unavailable | 0.04 / [input L372](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/go2_description/urdf/go2_description.urdf#L372) |
| upstream-only FR_hip_rotor | unavailable | unavailable | 0.089 / [input L256](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/go2_description/urdf/go2_description.urdf#L256) |
| upstream-only FR_thigh_rotor | unavailable | unavailable | 0.089 / [input L294](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/go2_description/urdf/go2_description.urdf#L294) |
| upstream-only Head_lower | unavailable | unavailable | 0.001 / [input L44](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/go2_description/urdf/go2_description.urdf#L44) |
| upstream-only Head_upper | unavailable | unavailable | 0.001 / [input L25](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/go2_description/urdf/go2_description.urdf#L25) |
| upstream-only RL_calf_rotor | unavailable | unavailable | 0.089 / [input L527](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/go2_description/urdf/go2_description.urdf#L527) |
| upstream-only RL_calflower | unavailable | unavailable | 0.0247086262 / [geometry/inference input L496](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/go2_description/urdf/go2_description.urdf#L496) |
| upstream-only RL_calflower1 | unavailable | unavailable | 0.0226430291 / [geometry/inference input L510](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/go2_description/urdf/go2_description.urdf#L510) |
| upstream-only RL_foot | unavailable | unavailable | 0.04 / [input L539](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/go2_description/urdf/go2_description.urdf#L539) |
| upstream-only RL_hip_rotor | unavailable | unavailable | 0.089 / [input L423](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/go2_description/urdf/go2_description.urdf#L423) |
| upstream-only RL_thigh_rotor | unavailable | unavailable | 0.089 / [input L461](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/go2_description/urdf/go2_description.urdf#L461) |
| upstream-only RR_calf_rotor | unavailable | unavailable | 0.089 / [input L694](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/go2_description/urdf/go2_description.urdf#L694) |
| upstream-only RR_calflower | unavailable | unavailable | 0.0247086262 / [geometry/inference input L663](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/go2_description/urdf/go2_description.urdf#L663) |
| upstream-only RR_calflower1 | unavailable | unavailable | 0.0226430291 / [geometry/inference input L677](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/go2_description/urdf/go2_description.urdf#L677) |
| upstream-only RR_foot | unavailable | unavailable | 0.04 / [input L706](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/go2_description/urdf/go2_description.urdf#L706) |
| upstream-only RR_hip_rotor | unavailable | unavailable | 0.089 / [input L590](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/go2_description/urdf/go2_description.urdf#L590) |
| upstream-only RR_thigh_rotor | unavailable | unavailable | 0.089 / [input L628](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/go2_description/urdf/go2_description.urdf#L628) |
| upstream-only front_camera | unavailable | unavailable | 0 / [geometry/inference input L759](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/go2_description/urdf/go2_description.urdf#L759) |
| upstream-only imu | unavailable | unavailable | 0 / [input L731](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/go2_description/urdf/go2_description.urdf#L731) |
| upstream-only radar | unavailable | unavailable | 0 / [input L744](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/go2_description/urdf/go2_description.urdf#L744) |

## Coverage and unmatched elements

```json
{
  "mapping_h": {
    "bodies": {
      "base": "base",
      "FL_hip": "FL_hip",
      "FL_thigh": "FL_thigh",
      "FL_calf": "FL_calf",
      "FR_hip": "FR_hip",
      "FR_thigh": "FR_thigh",
      "FR_calf": "FR_calf",
      "RL_hip": "RL_hip",
      "RL_thigh": "RL_thigh",
      "RL_calf": "RL_calf",
      "RR_hip": "RR_hip",
      "RR_thigh": "RR_thigh",
      "RR_calf": "RR_calf"
    },
    "joints": {
      "FL_hip_joint": "FL_hip_joint",
      "FL_thigh_joint": "FL_thigh_joint",
      "FL_calf_joint": "FL_calf_joint",
      "FR_hip_joint": "FR_hip_joint",
      "FR_thigh_joint": "FR_thigh_joint",
      "FR_calf_joint": "FR_calf_joint",
      "RL_hip_joint": "RL_hip_joint",
      "RL_thigh_joint": "RL_thigh_joint",
      "RL_calf_joint": "RL_calf_joint",
      "RR_hip_joint": "RR_hip_joint",
      "RR_thigh_joint": "RR_thigh_joint",
      "RR_calf_joint": "RR_calf_joint"
    },
    "body_methods": {
      "base": "name",
      "FL_hip": "name",
      "FL_thigh": "name",
      "FL_calf": "name",
      "FR_hip": "name",
      "FR_thigh": "name",
      "FR_calf": "name",
      "RL_hip": "name",
      "RL_thigh": "name",
      "RL_calf": "name",
      "RR_hip": "name",
      "RR_thigh": "name",
      "RR_calf": "name"
    },
    "joint_methods": {
      "FL_hip_joint": "name",
      "FL_thigh_joint": "name",
      "FL_calf_joint": "name",
      "FR_hip_joint": "name",
      "FR_thigh_joint": "name",
      "FR_calf_joint": "name",
      "RL_hip_joint": "name",
      "RL_thigh_joint": "name",
      "RL_calf_joint": "name",
      "RR_hip_joint": "name",
      "RR_thigh_joint": "name",
      "RR_calf_joint": "name"
    },
    "unmatched_m_bodies": [],
    "unmatched_upstream_bodies": [
      "FL_calf_rotor",
      "FL_calflower",
      "FL_calflower1",
      "FL_foot",
      "FL_hip_rotor",
      "FL_thigh_rotor",
      "FR_calf_rotor",
      "FR_calflower",
      "FR_calflower1",
      "FR_foot",
      "FR_hip_rotor",
      "FR_thigh_rotor",
      "Head_lower",
      "Head_upper",
      "RL_calf_rotor",
      "RL_calflower",
      "RL_calflower1",
      "RL_foot",
      "RL_hip_rotor",
      "RL_thigh_rotor",
      "RR_calf_rotor",
      "RR_calflower",
      "RR_calflower1",
      "RR_foot",
      "RR_hip_rotor",
      "RR_thigh_rotor",
      "front_camera",
      "imu",
      "radar"
    ],
    "unmatched_m_joints": [],
    "unmatched_upstream_joints": [],
    "registration_anchor": {
      "M": "base",
      "H": "base",
      "root_unmatched": false
    }
  },
  "mapping_s": null,
  "unavailable": [
    {
      "entity": "FL_hip_joint",
      "other_entity": "FL_hip_joint",
      "quantity": "force",
      "tolerance": "limit",
      "m": 23.7,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "FL_hip_joint",
      "other_entity": "FL_hip_joint",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 30.1,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "FL_thigh_joint",
      "other_entity": "FL_thigh_joint",
      "quantity": "force",
      "tolerance": "limit",
      "m": 23.7,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "FL_thigh_joint",
      "other_entity": "FL_thigh_joint",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 30.1,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "FL_calf_joint",
      "other_entity": "FL_calf_joint",
      "quantity": "force",
      "tolerance": "limit",
      "m": 45.43,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "FL_calf_joint",
      "other_entity": "FL_calf_joint",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 15.7,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "FR_hip_joint",
      "other_entity": "FR_hip_joint",
      "quantity": "force",
      "tolerance": "limit",
      "m": 23.7,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "FR_hip_joint",
      "other_entity": "FR_hip_joint",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 30.1,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "FR_thigh_joint",
      "other_entity": "FR_thigh_joint",
      "quantity": "force",
      "tolerance": "limit",
      "m": 23.7,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "FR_thigh_joint",
      "other_entity": "FR_thigh_joint",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 30.1,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "FR_calf_joint",
      "other_entity": "FR_calf_joint",
      "quantity": "force",
      "tolerance": "limit",
      "m": 45.43,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "FR_calf_joint",
      "other_entity": "FR_calf_joint",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 15.7,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "RL_hip_joint",
      "other_entity": "RL_hip_joint",
      "quantity": "force",
      "tolerance": "limit",
      "m": 23.7,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "RL_hip_joint",
      "other_entity": "RL_hip_joint",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 30.1,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "RL_thigh_joint",
      "other_entity": "RL_thigh_joint",
      "quantity": "force",
      "tolerance": "limit",
      "m": 23.7,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "RL_thigh_joint",
      "other_entity": "RL_thigh_joint",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 30.1,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "RL_calf_joint",
      "other_entity": "RL_calf_joint",
      "quantity": "force",
      "tolerance": "limit",
      "m": 45.43,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "RL_calf_joint",
      "other_entity": "RL_calf_joint",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 15.7,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "RR_hip_joint",
      "other_entity": "RR_hip_joint",
      "quantity": "force",
      "tolerance": "limit",
      "m": 23.7,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "RR_hip_joint",
      "other_entity": "RR_hip_joint",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 30.1,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "RR_thigh_joint",
      "other_entity": "RR_thigh_joint",
      "quantity": "force",
      "tolerance": "limit",
      "m": 23.7,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "RR_thigh_joint",
      "other_entity": "RR_thigh_joint",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 30.1,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "RR_calf_joint",
      "other_entity": "RR_calf_joint",
      "quantity": "force",
      "tolerance": "limit",
      "m": 45.43,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "RR_calf_joint",
      "other_entity": "RR_calf_joint",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 15.7,
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
| FL_hip_joint / force | 23.7 | unavailable | unavailable |
| FL_hip_joint / velocity | unavailable | unavailable | 30.1 |
| FL_thigh_joint / force | 23.7 | unavailable | unavailable |
| FL_thigh_joint / velocity | unavailable | unavailable | 30.1 |
| FL_calf_joint / force | 45.43 | unavailable | unavailable |
| FL_calf_joint / velocity | unavailable | unavailable | 15.7 |
| FR_hip_joint / force | 23.7 | unavailable | unavailable |
| FR_hip_joint / velocity | unavailable | unavailable | 30.1 |
| FR_thigh_joint / force | 23.7 | unavailable | unavailable |
| FR_thigh_joint / velocity | unavailable | unavailable | 30.1 |
| FR_calf_joint / force | 45.43 | unavailable | unavailable |
| FR_calf_joint / velocity | unavailable | unavailable | 15.7 |
| RL_hip_joint / force | 23.7 | unavailable | unavailable |
| RL_hip_joint / velocity | unavailable | unavailable | 30.1 |
| RL_thigh_joint / force | 23.7 | unavailable | unavailable |
| RL_thigh_joint / velocity | unavailable | unavailable | 30.1 |
| RL_calf_joint / force | 45.43 | unavailable | unavailable |
| RL_calf_joint / velocity | unavailable | unavailable | 15.7 |
| RR_hip_joint / force | 23.7 | unavailable | unavailable |
| RR_hip_joint / velocity | unavailable | unavailable | 30.1 |
| RR_thigh_joint / force | 23.7 | unavailable | unavailable |
| RR_thigh_joint / velocity | unavailable | unavailable | 30.1 |
| RR_calf_joint / force | 45.43 | unavailable | unavailable |
| RR_calf_joint / velocity | unavailable | unavailable | 15.7 |
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
  "https://github.com/unitreerobotics/unitree_ros robots/go2_description/xacro/leg.xacro at 157ff950351e5f535e03c5d85a16b7d594b3dbcc: ValueError: Macro leg requires unsupported explicit arguments: ['mirror', 'mirror_dae', 'front_hind', 'front_hind_dae']",
  "https://github.com/unitreerobotics/unitree_ros robots/go2_description/xacro/const.xacro at 157ff950351e5f535e03c5d85a16b7d594b3dbcc: ValueError: XML has no robot bodies; it is an include/extension fragment, not a standalone source",
  "https://github.com/unitreerobotics/unitree_ros robots/go2_description/xacro/robot.xacro at 157ff950351e5f535e03c5d85a16b7d594b3dbcc: ValueError: Resource missing at 157ff950351e5f535e03c5d85a16b7d594b3dbcc: robots/go2_description/xacro/robots/go2_description/meshes/trunk.dae",
  "https://github.com/unitreerobotics/unitree_ros robots/go2_description/xacro/gazebo.xacro at 157ff950351e5f535e03c5d85a16b7d594b3dbcc: ValueError: XML has no robot bodies; it is an include/extension fragment, not a standalone source",
  "https://github.com/unitreerobotics/unitree_ros robots/go2_description/xacro/materials.xacro at 157ff950351e5f535e03c5d85a16b7d594b3dbcc: ValueError: XML has no robot bodies; it is an include/extension fragment, not a standalone source",
  "https://github.com/unitreerobotics/unitree_ros robots/go2_description/xacro/transmission.xacro at 157ff950351e5f535e03c5d85a16b7d594b3dbcc: ValueError: XML has no robot bodies; it is an include/extension fragment, not a standalone source"
]
```

## History inputs

```json
[
  "robots/go2_description/dae/base.dae",
  "robots/go2_description/dae/calf.dae",
  "robots/go2_description/dae/calf_mirror.dae",
  "robots/go2_description/dae/foot.dae",
  "robots/go2_description/dae/hip.dae",
  "robots/go2_description/dae/thigh.dae",
  "robots/go2_description/dae/thigh_mirror.dae",
  "robots/go2_description/urdf/go2_description.urdf"
]
```

## Self comparisons

```json
[
  {
    "file": "unitree_go2/go2.xml",
    "status": "passed",
    "findings": 0
  },
  {
    "file": "unitree_go2/go2_mjx.xml",
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
      "NO MATCHING SOURCE": 23
    },
    "classifications_changed": 0,
    "finding_membership_changes": 0
  },
  "2": {
    "provenance_method": "none",
    "counts": {
      "NO MATCHING SOURCE": 23
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
      "unitree_go2/go2.xml"
    ],
    "registration": {
      "translation": [
        0.0,
        0.0,
        0.445
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
      "FL_calflower",
      "FL_calflower1",
      "FR_calflower",
      "FR_calflower1",
      "RL_calflower",
      "RL_calflower1",
      "RR_calflower",
      "RR_calflower1",
      "front_camera"
    ],
    "assets_loaded": 17,
    "mesh_conversions": [
      {
        "file": "robots/go2_description/dae/base.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "robots/go2_description/dae/hip.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "robots/go2_description/dae/thigh.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "robots/go2_description/dae/calf.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "robots/go2_description/dae/foot.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "robots/go2_description/dae/hip.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "robots/go2_description/dae/thigh_mirror.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "robots/go2_description/dae/calf_mirror.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "robots/go2_description/dae/foot.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "robots/go2_description/dae/hip.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "robots/go2_description/dae/thigh.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "robots/go2_description/dae/calf.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "robots/go2_description/dae/foot.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "robots/go2_description/dae/hip.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "robots/go2_description/dae/thigh_mirror.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "robots/go2_description/dae/calf_mirror.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "robots/go2_description/dae/foot.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      }
    ],
    "nonphysical_normalizations": [
      "Retained first of duplicate visual material tags; geometry, inertials and joints unchanged",
      "Retained first of duplicate visual material tags; geometry, inertials and joints unchanged",
      "Retained first of duplicate visual material tags; geometry, inertials and joints unchanged",
      "Retained first of duplicate visual material tags; geometry, inertials and joints unchanged",
      "Retained first of duplicate visual material tags; geometry, inertials and joints unchanged",
      "Retained first of duplicate visual material tags; geometry, inertials and joints unchanged",
      "Retained first of duplicate visual material tags; geometry, inertials and joints unchanged",
      "Retained first of duplicate visual material tags; geometry, inertials and joints unchanged",
      "Retained first of duplicate visual material tags; geometry, inertials and joints unchanged",
      "Retained first of duplicate visual material tags; geometry, inertials and joints unchanged",
      "Retained first of duplicate visual material tags; geometry, inertials and joints unchanged",
      "Retained first of duplicate visual material tags; geometry, inertials and joints unchanged",
      "Retained first of duplicate visual material tags; geometry, inertials and joints unchanged"
    ],
    "xacro_arguments": {},
    "source_dependencies": [
      "robots/go2_description/urdf/go2_description.urdf",
      "robots/go2_description/dae/base.dae",
      "robots/go2_description/dae/hip.dae",
      "robots/go2_description/dae/thigh.dae",
      "robots/go2_description/dae/calf.dae",
      "robots/go2_description/dae/foot.dae",
      "robots/go2_description/dae/hip.dae",
      "robots/go2_description/dae/thigh_mirror.dae",
      "robots/go2_description/dae/calf_mirror.dae",
      "robots/go2_description/dae/foot.dae",
      "robots/go2_description/dae/hip.dae",
      "robots/go2_description/dae/thigh.dae",
      "robots/go2_description/dae/calf.dae",
      "robots/go2_description/dae/foot.dae",
      "robots/go2_description/dae/hip.dae",
      "robots/go2_description/dae/thigh_mirror.dae",
      "robots/go2_description/dae/calf_mirror.dae",
      "robots/go2_description/dae/foot.dae"
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
  "self_variants_recompiled": 2,
  "historical_snapshots_reused": 5,
  "primary_physics_unchanged": true,
  "source_matching": "original raw-value provenance criteria retained; kinematic guard applies to reported CoM"
}
```
