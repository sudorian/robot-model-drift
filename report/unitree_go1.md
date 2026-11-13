# unitree_go1

Status: **complete**. Provenance: **none**, confidence **none**.

No public revision matches all comparable quantities. Class: NO MATCHING SOURCE; never counted as STALE.

M: `https://github.com/google-deepmind/mujoco_menagerie`, `unitree_go1/go1.xml`, commit `370c43965323c0944b433b202aac5058b5f907a9`.
H: `https://github.com/unitreerobotics/unitree_ros`, `robots/go1_description/urdf/go1.urdf`, commit `157ff950351e5f535e03c5d85a16b7d594b3dbcc`.
S: unavailable. A machine-readable H can still be compared to M; no-match differences are never counted as STALE.

Limit semantics: MJCF effort values are supported actuator torque/force envelopes. URDF effort and velocity values are manufacturer declarations retained from XML; MuJoCo does not enforce those tags. Such declaration comparisons are explicitly distinct from compiled inertial/range quantities.


## Source evidence

```json
[
  {
    "url": "https://github.com/unitreerobotics/unitree_ros/tree/master/robots/go1_description",
    "document": "unitree_go1/README.md",
    "commit": "370c43965323c0944b433b202aac5058b5f907a9",
    "current": true
  }
]
```


## Kinematics consistency

A proper Kabsch rigid transform aligns all matched zero-pose body origins. The maximum per-origin residual and signed hinge/slide axis angles determine whether CoM can be compared; RMS is also recorded. Fewer than three non-collinear origins give insufficient kinematic coverage. CoM records that fail either required M/H or M/S check are excluded from counts and largest discrepancies. Masses, principal moments and raw joint ranges remain unchanged; a flagged range still requires convention review.

| Pair | Status | Origins / rank | RMS / maximum mm | Disagreeing / checked axes |
|---|---|---:|---:|---:|
| M/H | consistent | 13 / 3 | 6.30332132e-15 / 8.4464767e-15 | 0 / 12 |

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
    "anchor_m": "trunk",
    "anchor_other": "trunk",
    "rotation_other_to_m": [
      [
        1.0,
        1.6974740518819113e-18,
        1.284339456091695e-18
      ],
      [
        -1.6974740518819115e-18,
        1.0,
        -6.389003759127213e-17
      ],
      [
        -1.284339456091695e-18,
        -6.473287929516485e-17,
        1.0
      ]
    ],
    "translation_other_to_m": [
      8.417363204539443e-20,
      -4.1872547713664496e-18,
      0.0
    ],
    "rms_residual_m": 6.3033213200824585e-18,
    "max_residual_m": 8.446476702352993e-18,
    "fit_rank": 3,
    "axis_checks": [
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
          -1.6974740518819115e-18,
          -1.284339456091695e-18
        ],
        "angle_rad": 2.1286018874571884e-18,
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
          1.6974740518819113e-18,
          1.0,
          -6.473287929516485e-17
        ],
        "angle_rad": 6.475513168853256e-17,
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
          1.6974740518819113e-18,
          1.0,
          -6.473287929516485e-17
        ],
        "angle_rad": 6.475513168853256e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
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
          -1.6974740518819115e-18,
          -1.284339456091695e-18
        ],
        "angle_rad": 2.1286018874571884e-18,
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
          1.6974740518819113e-18,
          1.0,
          -6.473287929516485e-17
        ],
        "angle_rad": 6.475513168853256e-17,
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
          1.6974740518819113e-18,
          1.0,
          -6.473287929516485e-17
        ],
        "angle_rad": 6.475513168853256e-17,
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
          -1.6974740518819115e-18,
          -1.284339456091695e-18
        ],
        "angle_rad": 2.1286018874571884e-18,
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
          1.6974740518819113e-18,
          1.0,
          -6.473287929516485e-17
        ],
        "angle_rad": 6.475513168853256e-17,
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
          1.6974740518819113e-18,
          1.0,
          -6.473287929516485e-17
        ],
        "angle_rad": 6.475513168853256e-17,
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
          -1.6974740518819115e-18,
          -1.284339456091695e-18
        ],
        "angle_rad": 2.1286018874571884e-18,
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
          1.6974740518819113e-18,
          1.0,
          -6.473287929516485e-17
        ],
        "angle_rad": 6.475513168853256e-17,
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
          1.6974740518819113e-18,
          1.0,
          -6.473287929516485e-17
        ],
        "angle_rad": 6.475513168853256e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      }
    ],
    "axis_disagreements": [],
    "com_eligible": true,
    "covariance_singular_values": [
      0.42457932000000004,
      0.13726675000000002,
      0.12563723076923078
    ],
    "origin_residuals_m": {
      "trunk": 4.188100729526788e-18,
      "FR_hip": 7.476809437708222e-18,
      "FR_thigh": 7.963308198971297e-18,
      "FR_calf": 0.0,
      "FL_hip": 7.669880601026975e-18,
      "FL_thigh": 8.446476702352993e-18,
      "FL_calf": 0.0,
      "RR_hip": 7.669880601026975e-18,
      "RR_thigh": 8.446476702352993e-18,
      "RR_calf": 0.0,
      "RL_hip": 7.476809437708222e-18,
      "RL_thigh": 7.963308198971297e-18,
      "RL_calf": 0.0
    },
    "reason": "Unique proper rigid fit and matched signed axes meet the configured thresholds"
  }
}
```


## Every reported quantity difference

Counts are quantity records, including correlated total/subtree/body mass records; they are not independent robot defects.

| Entity / quantity | M | S | H | H − M | Class | M source | S source | H source |
|---|---|---|---|---|---|---|---|---|
| robot / total_mass | 12.743448 | unavailable | 13.100528 | 0.35708 | NO MATCHING SOURCE | [aggregate inputs](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_go1/go1.xml#L1) | unavailable | [aggregate inputs](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/go1_description/urdf/go1.urdf#L1) |
| robot / total_com_registered | [0.00840575999, 0.000876778001, -0.0319658317] | unavailable | [0.0081758198, 0.000847825354, -0.0310950855] | [-0.000229940186, -2.8952647e-05, 0.000870746169] | NO MATCHING SOURCE | [aggregate inputs](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_go1/go1.xml#L1) | unavailable | [aggregate inputs](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/go1_description/urdf/go1.urdf#L1) |
| trunk / subtree_mass | 12.743448 | unavailable | 13.100528 | 0.35708 | NO MATCHING SOURCE | [subtree root L79](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_go1/go1.xml#L79) | unavailable | [subtree root L420](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/go1_description/urdf/go1.urdf#L420) |
| FR_hip / mass | 0.68 | unavailable | 0.591 | -0.089 | NO MATCHING SOURCE | [input L97](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_go1/go1.xml#L97) | unavailable | [input L494](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/go1_description/urdf/go1.urdf#L494) |
| FR_hip / com_registered | [0.1831834, -0.03912385, -8.865e-05] | unavailable | [0.182443, -0.037998, -0.000102] | [-0.0007404, 0.00112585, -1.335e-05] | NO MATCHING SOURCE | [CoM/kinematic input L97](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_go1/go1.xml#L97) | unavailable | [CoM/kinematic input L493](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/go1_description/urdf/go1.urdf#L493) |
| FR_hip / principal_moments | [0.000398719, 0.000468438, 0.000734064] | unavailable | [0.000333570603, 0.000400591834, 0.000619523321] | [-6.51483974e-05, -6.78461658e-05, -0.000114540679] | NO MATCHING SOURCE | [inertia input L97](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_go1/go1.xml#L97) | unavailable | [inertia input L495](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/go1_description/urdf/go1.urdf#L495) |
| FR_thigh / mass | 1.009 | unavailable | 0.92 | -0.089 | NO MATCHING SOURCE | [input L104](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_go1/go1.xml#L104) | unavailable | [input L547](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/go1_description/urdf/go1.urdf#L547) |
| FR_thigh / com_registered | [0.18505278, -0.107435, -0.0305004] | unavailable | [0.184758, -0.108696, -0.033451] | [-0.00029478, -0.001261, -0.0029506] | NO MATCHING SOURCE | [CoM/kinematic input L104](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_go1/go1.xml#L104) | unavailable | [CoM/kinematic input L546](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/go1_description/urdf/go1.urdf#L546) |
| FR_thigh / principal_moments | [0.000709268, 0.00460903, 0.00478717] | unavailable | [0.000641595245, 0.00444044645, 0.00457569999] | [-6.76727553e-05, -0.000168583551, -0.000211470007] | NO MATCHING SOURCE | [inertia input L104](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_go1/go1.xml#L104) | unavailable | [inertia input L548](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/go1_description/urdf/go1.urdf#L548) |
| FR_calf / mass | 0.195862 | unavailable | 0.135862 | -0.06 | NO MATCHING SOURCE | [input L112](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_go1/go1.xml#L112) | unavailable | [input L600](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/go1_description/urdf/go1.urdf#L600) |
| FR_calf / com_registered | [0.19239862, -0.125773324, -0.359197] | unavailable | [0.194297, -0.125342, -0.329695] | [0.00189838, 0.000431324, 0.029502] | NO MATCHING SOURCE | [CoM/kinematic input L112](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_go1/go1.xml#L112) | unavailable | [CoM/kinematic input L599](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/go1_description/urdf/go1.urdf#L599) |
| FR_calf / principal_moments | [3.58427e-05, 0.00148468, 0.00149767] | unavailable | [2.47358147e-05, 0.00108883563, 0.00110043781] | [-1.11068853e-05, -0.000395844368, -0.000397232194] | NO MATCHING SOURCE | [inertia input L112](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_go1/go1.xml#L112) | unavailable | [inertia input L601](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/go1_description/urdf/go1.urdf#L601) |
| FL_hip / mass | 0.68 | unavailable | 0.591 | -0.089 | NO MATCHING SOURCE | [input L124](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_go1/go1.xml#L124) | unavailable | [input L707](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/go1_description/urdf/go1.urdf#L707) |
| FL_hip / com_registered | [0.1831834, 0.03912385, -8.865e-05] | unavailable | [0.182443, 0.037998, -0.000102] | [-0.0007404, -0.00112585, -1.335e-05] | NO MATCHING SOURCE | [CoM/kinematic input L124](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_go1/go1.xml#L124) | unavailable | [CoM/kinematic input L706](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/go1_description/urdf/go1.urdf#L706) |
| FL_hip / principal_moments | [0.000398719, 0.000468438, 0.000734064] | unavailable | [0.000333570603, 0.000400591834, 0.000619523321] | [-6.51483974e-05, -6.78461658e-05, -0.000114540679] | NO MATCHING SOURCE | [inertia input L124](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_go1/go1.xml#L124) | unavailable | [inertia input L708](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/go1_description/urdf/go1.urdf#L708) |
| FL_thigh / mass | 1.009 | unavailable | 0.92 | -0.089 | NO MATCHING SOURCE | [input L131](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_go1/go1.xml#L131) | unavailable | [input L760](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/go1_description/urdf/go1.urdf#L760) |
| FL_thigh / com_registered | [0.18505278, 0.107435, -0.0305004] | unavailable | [0.184758, 0.108696, -0.033451] | [-0.00029478, 0.001261, -0.0029506] | NO MATCHING SOURCE | [CoM/kinematic input L131](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_go1/go1.xml#L131) | unavailable | [CoM/kinematic input L759](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/go1_description/urdf/go1.urdf#L759) |
| FL_thigh / principal_moments | [0.000709268, 0.00460903, 0.00478717] | unavailable | [0.000641595245, 0.00444044645, 0.00457569999] | [-6.76727553e-05, -0.000168583551, -0.000211470007] | NO MATCHING SOURCE | [inertia input L131](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_go1/go1.xml#L131) | unavailable | [inertia input L761](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/go1_description/urdf/go1.urdf#L761) |
| FL_calf / mass | 0.195862 | unavailable | 0.135862 | -0.06 | NO MATCHING SOURCE | [input L139](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_go1/go1.xml#L139) | unavailable | [input L813](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/go1_description/urdf/go1.urdf#L813) |
| FL_calf / com_registered | [0.19239862, 0.127726676, -0.359197] | unavailable | [0.194297, 0.128158, -0.329695] | [0.00189838, 0.000431324, 0.029502] | NO MATCHING SOURCE | [CoM/kinematic input L139](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_go1/go1.xml#L139) | unavailable | [CoM/kinematic input L812](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/go1_description/urdf/go1.urdf#L812) |
| FL_calf / principal_moments | [3.58427e-05, 0.00148468, 0.00149767] | unavailable | [2.47358147e-05, 0.00108883563, 0.00110043781] | [-1.11068853e-05, -0.000395844368, -0.000397232194] | NO MATCHING SOURCE | [inertia input L139](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_go1/go1.xml#L139) | unavailable | [inertia input L814](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/go1_description/urdf/go1.urdf#L814) |
| RR_hip / mass | 0.68 | unavailable | 0.591 | -0.089 | NO MATCHING SOURCE | [input L151](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_go1/go1.xml#L151) | unavailable | [input L920](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/go1_description/urdf/go1.urdf#L920) |
| RR_hip / com_registered | [-0.1831834, -0.03912385, -8.865e-05] | unavailable | [-0.182443, -0.037998, -0.000102] | [0.0007404, 0.00112585, -1.335e-05] | NO MATCHING SOURCE | [CoM/kinematic input L151](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_go1/go1.xml#L151) | unavailable | [CoM/kinematic input L919](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/go1_description/urdf/go1.urdf#L919) |
| RR_hip / principal_moments | [0.000398719, 0.000468438, 0.000734064] | unavailable | [0.000333570603, 0.000400591834, 0.000619523321] | [-6.51483974e-05, -6.78461658e-05, -0.000114540679] | NO MATCHING SOURCE | [inertia input L151](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_go1/go1.xml#L151) | unavailable | [inertia input L921](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/go1_description/urdf/go1.urdf#L921) |
| RR_thigh / mass | 1.009 | unavailable | 0.92 | -0.089 | NO MATCHING SOURCE | [input L159](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_go1/go1.xml#L159) | unavailable | [input L973](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/go1_description/urdf/go1.urdf#L973) |
| RR_thigh / com_registered | [-0.19114722, -0.107435, -0.0305004] | unavailable | [-0.191442, -0.108696, -0.033451] | [-0.00029478, -0.001261, -0.0029506] | NO MATCHING SOURCE | [CoM/kinematic input L159](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_go1/go1.xml#L159) | unavailable | [CoM/kinematic input L972](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/go1_description/urdf/go1.urdf#L972) |
| RR_thigh / principal_moments | [0.000709268, 0.00460903, 0.00478717] | unavailable | [0.000641595245, 0.00444044645, 0.00457569999] | [-6.76727553e-05, -0.000168583551, -0.000211470007] | NO MATCHING SOURCE | [inertia input L159](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_go1/go1.xml#L159) | unavailable | [inertia input L974](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/go1_description/urdf/go1.urdf#L974) |
| RR_calf / mass | 0.195862 | unavailable | 0.135862 | -0.06 | NO MATCHING SOURCE | [input L167](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_go1/go1.xml#L167) | unavailable | [input L1026](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/go1_description/urdf/go1.urdf#L1026) |
| RR_calf / com_registered | [-0.18380138, -0.125773324, -0.359197] | unavailable | [-0.181903, -0.125342, -0.329695] | [0.00189838, 0.000431324, 0.029502] | NO MATCHING SOURCE | [CoM/kinematic input L167](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_go1/go1.xml#L167) | unavailable | [CoM/kinematic input L1025](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/go1_description/urdf/go1.urdf#L1025) |
| RR_calf / principal_moments | [3.58427e-05, 0.00148468, 0.00149767] | unavailable | [2.47358147e-05, 0.00108883563, 0.00110043781] | [-1.11068853e-05, -0.000395844368, -0.000397232194] | NO MATCHING SOURCE | [inertia input L167](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_go1/go1.xml#L167) | unavailable | [inertia input L1027](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/go1_description/urdf/go1.urdf#L1027) |
| RL_hip / mass | 0.68 | unavailable | 0.591 | -0.089 | NO MATCHING SOURCE | [input L179](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_go1/go1.xml#L179) | unavailable | [input L1133](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/go1_description/urdf/go1.urdf#L1133) |
| RL_hip / com_registered | [-0.1831834, 0.03912385, -8.865e-05] | unavailable | [-0.182443, 0.037998, -0.000102] | [0.0007404, -0.00112585, -1.335e-05] | NO MATCHING SOURCE | [CoM/kinematic input L179](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_go1/go1.xml#L179) | unavailable | [CoM/kinematic input L1132](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/go1_description/urdf/go1.urdf#L1132) |
| RL_hip / principal_moments | [0.000398719, 0.000468438, 0.000734064] | unavailable | [0.000333570603, 0.000400591834, 0.000619523321] | [-6.51483974e-05, -6.78461658e-05, -0.000114540679] | NO MATCHING SOURCE | [inertia input L179](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_go1/go1.xml#L179) | unavailable | [inertia input L1134](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/go1_description/urdf/go1.urdf#L1134) |
| RL_thigh / mass | 1.009 | unavailable | 0.92 | -0.089 | NO MATCHING SOURCE | [input L187](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_go1/go1.xml#L187) | unavailable | [input L1186](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/go1_description/urdf/go1.urdf#L1186) |
| RL_thigh / com_registered | [-0.19114722, 0.107435, -0.0305004] | unavailable | [-0.191442, 0.108696, -0.033451] | [-0.00029478, 0.001261, -0.0029506] | NO MATCHING SOURCE | [CoM/kinematic input L187](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_go1/go1.xml#L187) | unavailable | [CoM/kinematic input L1185](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/go1_description/urdf/go1.urdf#L1185) |
| RL_thigh / principal_moments | [0.000709268, 0.00460903, 0.00478717] | unavailable | [0.000641595245, 0.00444044645, 0.00457569999] | [-6.76727553e-05, -0.000168583551, -0.000211470007] | NO MATCHING SOURCE | [inertia input L187](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_go1/go1.xml#L187) | unavailable | [inertia input L1187](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/go1_description/urdf/go1.urdf#L1187) |
| RL_calf / mass | 0.195862 | unavailable | 0.135862 | -0.06 | NO MATCHING SOURCE | [input L195](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_go1/go1.xml#L195) | unavailable | [input L1239](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/go1_description/urdf/go1.urdf#L1239) |
| RL_calf / com_registered | [-0.18380138, 0.127726676, -0.359197] | unavailable | [-0.181903, 0.128158, -0.329695] | [0.00189838, 0.000431324, 0.029502] | NO MATCHING SOURCE | [CoM/kinematic input L195](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_go1/go1.xml#L195) | unavailable | [CoM/kinematic input L1238](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/go1_description/urdf/go1.urdf#L1238) |
| RL_calf / principal_moments | [3.58427e-05, 0.00148468, 0.00149767] | unavailable | [2.47358147e-05, 0.00108883563, 0.00110043781] | [-1.11068853e-05, -0.000395844368, -0.000397232194] | NO MATCHING SOURCE | [inertia input L195](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_go1/go1.xml#L195) | unavailable | [inertia input L1240](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/go1_description/urdf/go1.urdf#L1240) |

## Raw CoM records and reporting decisions

Raw values retain the previous root-anchor registration before Kabsch; original world coordinates also remain in the snapshots. Eligible findings above use the fitted transform into M. Excluded raw records below are diagnostic numbers, not findings. No CoM suppression applies to mass or principal inertia moments.

| Entity / quantity | Raw M | Raw S | Raw H | Raw H − M | Decision | M source | S source | H source |
|---|---|---|---|---|---|---|---|---|
| robot / total_com_registered | [0.00840575999, 0.000876778001, -0.0319658317] | unavailable | [0.0081758198, 0.000847825354, -0.0310950855] | [-0.000229940186, -2.8952647e-05, 0.000870746169] | eligible; compared after Kabsch alignment | [aggregate inputs](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_go1/go1.xml#L1) | unavailable | [aggregate inputs](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/go1_description/urdf/go1.urdf#L1) |
| trunk / com_registered | [0.0223, 0.002, -0.0005] | unavailable | [0.0223, 0.002, -0.0005] | [0, 0, 4.33680869e-19] | eligible; compared after Kabsch alignment | [CoM/kinematic input L83](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_go1/go1.xml#L83) | unavailable | [CoM/kinematic input L435](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/go1_description/urdf/go1.urdf#L435) |
| FR_hip / com_registered | [0.1831834, -0.03912385, -8.865e-05] | unavailable | [0.182443, -0.037998, -0.000102] | [-0.0007404, 0.00112585, -1.335e-05] | eligible; compared after Kabsch alignment | [CoM/kinematic input L97](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_go1/go1.xml#L97) | unavailable | [CoM/kinematic input L493](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/go1_description/urdf/go1.urdf#L493) |
| FR_thigh / com_registered | [0.18505278, -0.107435, -0.0305004] | unavailable | [0.184758, -0.108696, -0.033451] | [-0.00029478, -0.001261, -0.0029506] | eligible; compared after Kabsch alignment | [CoM/kinematic input L104](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_go1/go1.xml#L104) | unavailable | [CoM/kinematic input L546](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/go1_description/urdf/go1.urdf#L546) |
| FR_calf / com_registered | [0.19239862, -0.125773324, -0.359197] | unavailable | [0.194297, -0.125342, -0.329695] | [0.00189838, 0.000431324, 0.029502] | eligible; compared after Kabsch alignment | [CoM/kinematic input L112](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_go1/go1.xml#L112) | unavailable | [CoM/kinematic input L599](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/go1_description/urdf/go1.urdf#L599) |
| FL_hip / com_registered | [0.1831834, 0.03912385, -8.865e-05] | unavailable | [0.182443, 0.037998, -0.000102] | [-0.0007404, -0.00112585, -1.335e-05] | eligible; compared after Kabsch alignment | [CoM/kinematic input L124](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_go1/go1.xml#L124) | unavailable | [CoM/kinematic input L706](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/go1_description/urdf/go1.urdf#L706) |
| FL_thigh / com_registered | [0.18505278, 0.107435, -0.0305004] | unavailable | [0.184758, 0.108696, -0.033451] | [-0.00029478, 0.001261, -0.0029506] | eligible; compared after Kabsch alignment | [CoM/kinematic input L131](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_go1/go1.xml#L131) | unavailable | [CoM/kinematic input L759](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/go1_description/urdf/go1.urdf#L759) |
| FL_calf / com_registered | [0.19239862, 0.127726676, -0.359197] | unavailable | [0.194297, 0.128158, -0.329695] | [0.00189838, 0.000431324, 0.029502] | eligible; compared after Kabsch alignment | [CoM/kinematic input L139](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_go1/go1.xml#L139) | unavailable | [CoM/kinematic input L812](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/go1_description/urdf/go1.urdf#L812) |
| RR_hip / com_registered | [-0.1831834, -0.03912385, -8.865e-05] | unavailable | [-0.182443, -0.037998, -0.000102] | [0.0007404, 0.00112585, -1.335e-05] | eligible; compared after Kabsch alignment | [CoM/kinematic input L151](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_go1/go1.xml#L151) | unavailable | [CoM/kinematic input L919](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/go1_description/urdf/go1.urdf#L919) |
| RR_thigh / com_registered | [-0.19114722, -0.107435, -0.0305004] | unavailable | [-0.191442, -0.108696, -0.033451] | [-0.00029478, -0.001261, -0.0029506] | eligible; compared after Kabsch alignment | [CoM/kinematic input L159](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_go1/go1.xml#L159) | unavailable | [CoM/kinematic input L972](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/go1_description/urdf/go1.urdf#L972) |
| RR_calf / com_registered | [-0.18380138, -0.125773324, -0.359197] | unavailable | [-0.181903, -0.125342, -0.329695] | [0.00189838, 0.000431324, 0.029502] | eligible; compared after Kabsch alignment | [CoM/kinematic input L167](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_go1/go1.xml#L167) | unavailable | [CoM/kinematic input L1025](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/go1_description/urdf/go1.urdf#L1025) |
| RL_hip / com_registered | [-0.1831834, 0.03912385, -8.865e-05] | unavailable | [-0.182443, 0.037998, -0.000102] | [0.0007404, -0.00112585, -1.335e-05] | eligible; compared after Kabsch alignment | [CoM/kinematic input L179](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_go1/go1.xml#L179) | unavailable | [CoM/kinematic input L1132](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/go1_description/urdf/go1.urdf#L1132) |
| RL_thigh / com_registered | [-0.19114722, 0.107435, -0.0305004] | unavailable | [-0.191442, 0.108696, -0.033451] | [-0.00029478, 0.001261, -0.0029506] | eligible; compared after Kabsch alignment | [CoM/kinematic input L187](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_go1/go1.xml#L187) | unavailable | [CoM/kinematic input L1185](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/go1_description/urdf/go1.urdf#L1185) |
| RL_calf / com_registered | [-0.18380138, 0.127726676, -0.359197] | unavailable | [-0.181903, 0.128158, -0.329695] | [0.00189838, 0.000431324, 0.029502] | eligible; compared after Kabsch alignment | [CoM/kinematic input L195](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_go1/go1.xml#L195) | unavailable | [CoM/kinematic input L1238](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/go1_description/urdf/go1.urdf#L1238) |

## Mass accounting

Every contributing compiled body mass is listed here so total/subtree sums can be checked. Links point to explicit inertials or to geometry inputs when the compiler inferred a mass. CoM links identify inertial inputs; world coordinates additionally use the ancestor transforms and the registration recorded below.

| M body | M kg / source | S kg / source | H kg / source |
|---|---|---|---|
| trunk | 5.204 / [input L83](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_go1/go1.xml#L83) | unavailable | 5.204 / [input L436](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/go1_description/urdf/go1.urdf#L436) |
| FR_hip | 0.68 / [input L97](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_go1/go1.xml#L97) | unavailable | 0.591 / [input L494](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/go1_description/urdf/go1.urdf#L494) |
| FR_thigh | 1.009 / [input L104](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_go1/go1.xml#L104) | unavailable | 0.92 / [input L547](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/go1_description/urdf/go1.urdf#L547) |
| FR_calf | 0.195862 / [input L112](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_go1/go1.xml#L112) | unavailable | 0.135862 / [input L600](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/go1_description/urdf/go1.urdf#L600) |
| FL_hip | 0.68 / [input L124](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_go1/go1.xml#L124) | unavailable | 0.591 / [input L707](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/go1_description/urdf/go1.urdf#L707) |
| FL_thigh | 1.009 / [input L131](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_go1/go1.xml#L131) | unavailable | 0.92 / [input L760](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/go1_description/urdf/go1.urdf#L760) |
| FL_calf | 0.195862 / [input L139](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_go1/go1.xml#L139) | unavailable | 0.135862 / [input L813](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/go1_description/urdf/go1.urdf#L813) |
| RR_hip | 0.68 / [input L151](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_go1/go1.xml#L151) | unavailable | 0.591 / [input L920](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/go1_description/urdf/go1.urdf#L920) |
| RR_thigh | 1.009 / [input L159](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_go1/go1.xml#L159) | unavailable | 0.92 / [input L973](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/go1_description/urdf/go1.urdf#L973) |
| RR_calf | 0.195862 / [input L167](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_go1/go1.xml#L167) | unavailable | 0.135862 / [input L1026](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/go1_description/urdf/go1.urdf#L1026) |
| RL_hip | 0.68 / [input L179](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_go1/go1.xml#L179) | unavailable | 0.591 / [input L1133](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/go1_description/urdf/go1.urdf#L1133) |
| RL_thigh | 1.009 / [input L187](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_go1/go1.xml#L187) | unavailable | 0.92 / [input L1186](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/go1_description/urdf/go1.urdf#L1186) |
| RL_calf | 0.195862 / [input L195](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_go1/go1.xml#L195) | unavailable | 0.135862 / [input L1239](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/go1_description/urdf/go1.urdf#L1239) |
| upstream-only FL_calf_rotor | unavailable | unavailable | 0.089 / [input L833](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/go1_description/urdf/go1.urdf#L833) |
| upstream-only FL_foot | unavailable | unavailable | 0.06 / [input L857](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/go1_description/urdf/go1.urdf#L857) |
| upstream-only FL_hip_rotor | unavailable | unavailable | 0.089 / [input L727](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/go1_description/urdf/go1.urdf#L727) |
| upstream-only FL_thigh_rotor | unavailable | unavailable | 0.089 / [input L780](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/go1_description/urdf/go1.urdf#L780) |
| upstream-only FR_calf_rotor | unavailable | unavailable | 0.089 / [input L620](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/go1_description/urdf/go1.urdf#L620) |
| upstream-only FR_foot | unavailable | unavailable | 0.06 / [input L644](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/go1_description/urdf/go1.urdf#L644) |
| upstream-only FR_hip_rotor | unavailable | unavailable | 0.089 / [input L514](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/go1_description/urdf/go1.urdf#L514) |
| upstream-only FR_thigh_rotor | unavailable | unavailable | 0.089 / [input L567](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/go1_description/urdf/go1.urdf#L567) |
| upstream-only RL_calf_rotor | unavailable | unavailable | 0.089 / [input L1259](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/go1_description/urdf/go1.urdf#L1259) |
| upstream-only RL_foot | unavailable | unavailable | 0.06 / [input L1283](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/go1_description/urdf/go1.urdf#L1283) |
| upstream-only RL_hip_rotor | unavailable | unavailable | 0.089 / [input L1153](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/go1_description/urdf/go1.urdf#L1153) |
| upstream-only RL_thigh_rotor | unavailable | unavailable | 0.089 / [input L1206](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/go1_description/urdf/go1.urdf#L1206) |
| upstream-only RR_calf_rotor | unavailable | unavailable | 0.089 / [input L1046](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/go1_description/urdf/go1.urdf#L1046) |
| upstream-only RR_foot | unavailable | unavailable | 0.06 / [input L1070](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/go1_description/urdf/go1.urdf#L1070) |
| upstream-only RR_hip_rotor | unavailable | unavailable | 0.089 / [input L940](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/go1_description/urdf/go1.urdf#L940) |
| upstream-only RR_thigh_rotor | unavailable | unavailable | 0.089 / [input L993](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/go1_description/urdf/go1.urdf#L993) |
| upstream-only base | unavailable | unavailable | 0 / [geometry/inference input L407](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/go1_description/urdf/go1.urdf#L407) |
| upstream-only camera_chin | unavailable | unavailable | 1e-05 / [input L1410](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/go1_description/urdf/go1.urdf#L1410) |
| upstream-only camera_face | unavailable | unavailable | 1e-05 / [input L1336](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/go1_description/urdf/go1.urdf#L1336) |
| upstream-only camera_laserscan_link_left | unavailable | unavailable | 0 / [geometry/inference input L1692](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/go1_description/urdf/go1.urdf#L1692) |
| upstream-only camera_laserscan_link_right | unavailable | unavailable | 0 / [geometry/inference input L1699](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/go1_description/urdf/go1.urdf#L1699) |
| upstream-only camera_left | unavailable | unavailable | 1e-05 / [input L1484](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/go1_description/urdf/go1.urdf#L1484) |
| upstream-only camera_optical_chin | unavailable | unavailable | 0 / [geometry/inference input L1420](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/go1_description/urdf/go1.urdf#L1420) |
| upstream-only camera_optical_face | unavailable | unavailable | 0 / [geometry/inference input L1346](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/go1_description/urdf/go1.urdf#L1346) |
| upstream-only camera_optical_left | unavailable | unavailable | 0 / [geometry/inference input L1494](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/go1_description/urdf/go1.urdf#L1494) |
| upstream-only camera_optical_rearDown | unavailable | unavailable | 0 / [geometry/inference input L1642](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/go1_description/urdf/go1.urdf#L1642) |
| upstream-only camera_optical_right | unavailable | unavailable | 0 / [geometry/inference input L1568](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/go1_description/urdf/go1.urdf#L1568) |
| upstream-only camera_rearDown | unavailable | unavailable | 1e-05 / [input L1632](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/go1_description/urdf/go1.urdf#L1632) |
| upstream-only camera_right | unavailable | unavailable | 1e-05 / [input L1558](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/go1_description/urdf/go1.urdf#L1558) |
| upstream-only imu_link | unavailable | unavailable | 0.001 / [input L447](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/go1_description/urdf/go1.urdf#L447) |
| upstream-only ultraSound_face | unavailable | unavailable | 1e-05 / [input L1771](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/go1_description/urdf/go1.urdf#L1771) |
| upstream-only ultraSound_left | unavailable | unavailable | 1e-05 / [input L1721](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/go1_description/urdf/go1.urdf#L1721) |
| upstream-only ultraSound_right | unavailable | unavailable | 1e-05 / [input L1746](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/go1_description/urdf/go1.urdf#L1746) |

## Coverage and unmatched elements

```json
{
  "mapping_h": {
    "bodies": {
      "trunk": "trunk",
      "FR_hip": "FR_hip",
      "FR_thigh": "FR_thigh",
      "FR_calf": "FR_calf",
      "FL_hip": "FL_hip",
      "FL_thigh": "FL_thigh",
      "FL_calf": "FL_calf",
      "RR_hip": "RR_hip",
      "RR_thigh": "RR_thigh",
      "RR_calf": "RR_calf",
      "RL_hip": "RL_hip",
      "RL_thigh": "RL_thigh",
      "RL_calf": "RL_calf"
    },
    "joints": {
      "FR_hip_joint": "FR_hip_joint",
      "FR_thigh_joint": "FR_thigh_joint",
      "FR_calf_joint": "FR_calf_joint",
      "FL_hip_joint": "FL_hip_joint",
      "FL_thigh_joint": "FL_thigh_joint",
      "FL_calf_joint": "FL_calf_joint",
      "RR_hip_joint": "RR_hip_joint",
      "RR_thigh_joint": "RR_thigh_joint",
      "RR_calf_joint": "RR_calf_joint",
      "RL_hip_joint": "RL_hip_joint",
      "RL_thigh_joint": "RL_thigh_joint",
      "RL_calf_joint": "RL_calf_joint"
    },
    "body_methods": {
      "trunk": "name",
      "FR_hip": "name",
      "FR_thigh": "name",
      "FR_calf": "name",
      "FL_hip": "name",
      "FL_thigh": "name",
      "FL_calf": "name",
      "RR_hip": "name",
      "RR_thigh": "name",
      "RR_calf": "name",
      "RL_hip": "name",
      "RL_thigh": "name",
      "RL_calf": "name"
    },
    "joint_methods": {
      "FR_hip_joint": "name",
      "FR_thigh_joint": "name",
      "FR_calf_joint": "name",
      "FL_hip_joint": "name",
      "FL_thigh_joint": "name",
      "FL_calf_joint": "name",
      "RR_hip_joint": "name",
      "RR_thigh_joint": "name",
      "RR_calf_joint": "name",
      "RL_hip_joint": "name",
      "RL_thigh_joint": "name",
      "RL_calf_joint": "name"
    },
    "unmatched_m_bodies": [],
    "unmatched_upstream_bodies": [
      "FL_calf_rotor",
      "FL_foot",
      "FL_hip_rotor",
      "FL_thigh_rotor",
      "FR_calf_rotor",
      "FR_foot",
      "FR_hip_rotor",
      "FR_thigh_rotor",
      "RL_calf_rotor",
      "RL_foot",
      "RL_hip_rotor",
      "RL_thigh_rotor",
      "RR_calf_rotor",
      "RR_foot",
      "RR_hip_rotor",
      "RR_thigh_rotor",
      "base",
      "camera_chin",
      "camera_face",
      "camera_laserscan_link_left",
      "camera_laserscan_link_right",
      "camera_left",
      "camera_optical_chin",
      "camera_optical_face",
      "camera_optical_left",
      "camera_optical_rearDown",
      "camera_optical_right",
      "camera_rearDown",
      "camera_right",
      "imu_link",
      "ultraSound_face",
      "ultraSound_left",
      "ultraSound_right"
    ],
    "unmatched_m_joints": [],
    "unmatched_upstream_joints": [],
    "registration_anchor": {
      "M": "trunk",
      "H": "trunk",
      "root_unmatched": false
    }
  },
  "mapping_s": null,
  "unavailable": [
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
      "m": 35.55,
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
      "other": 20.06,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
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
      "m": 35.55,
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
      "other": 20.06,
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
      "m": 35.55,
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
      "other": 20.06,
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
      "m": 35.55,
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
      "other": 20.06,
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
| FR_hip_joint / force | 23.7 | unavailable | unavailable |
| FR_hip_joint / velocity | unavailable | unavailable | 30.1 |
| FR_thigh_joint / force | 23.7 | unavailable | unavailable |
| FR_thigh_joint / velocity | unavailable | unavailable | 30.1 |
| FR_calf_joint / force | 35.55 | unavailable | unavailable |
| FR_calf_joint / velocity | unavailable | unavailable | 20.06 |
| FL_hip_joint / force | 23.7 | unavailable | unavailable |
| FL_hip_joint / velocity | unavailable | unavailable | 30.1 |
| FL_thigh_joint / force | 23.7 | unavailable | unavailable |
| FL_thigh_joint / velocity | unavailable | unavailable | 30.1 |
| FL_calf_joint / force | 35.55 | unavailable | unavailable |
| FL_calf_joint / velocity | unavailable | unavailable | 20.06 |
| RR_hip_joint / force | 23.7 | unavailable | unavailable |
| RR_hip_joint / velocity | unavailable | unavailable | 30.1 |
| RR_thigh_joint / force | 23.7 | unavailable | unavailable |
| RR_thigh_joint / velocity | unavailable | unavailable | 30.1 |
| RR_calf_joint / force | 35.55 | unavailable | unavailable |
| RR_calf_joint / velocity | unavailable | unavailable | 20.06 |
| RL_hip_joint / force | 23.7 | unavailable | unavailable |
| RL_hip_joint / velocity | unavailable | unavailable | 30.1 |
| RL_thigh_joint / force | 23.7 | unavailable | unavailable |
| RL_thigh_joint / velocity | unavailable | unavailable | 30.1 |
| RL_calf_joint / force | 35.55 | unavailable | unavailable |
| RL_calf_joint / velocity | unavailable | unavailable | 20.06 |
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
  "https://github.com/unitreerobotics/unitree_ros robots/go1_description/xacro/leg.xacro at 157ff950351e5f535e03c5d85a16b7d594b3dbcc: ValueError: Macro leg requires unsupported explicit arguments: ['mirror', 'mirror_dae', 'front_hind', 'front_hind_dae']",
  "https://github.com/unitreerobotics/unitree_ros robots/go1_description/xacro/const.xacro at 157ff950351e5f535e03c5d85a16b7d594b3dbcc: ValueError: XML has no robot bodies; it is an include/extension fragment, not a standalone source",
  "https://github.com/unitreerobotics/unitree_ros robots/go1_description/xacro/gazebo.xacro at 157ff950351e5f535e03c5d85a16b7d594b3dbcc: ValueError: XML has no robot bodies; it is an include/extension fragment, not a standalone source",
  "https://github.com/unitreerobotics/unitree_ros robots/go1_description/xacro/materials.xacro at 157ff950351e5f535e03c5d85a16b7d594b3dbcc: ValueError: XML has no robot bodies; it is an include/extension fragment, not a standalone source",
  "https://github.com/unitreerobotics/unitree_ros robots/go1_description/xacro/ultraSound.xacro at 157ff950351e5f535e03c5d85a16b7d594b3dbcc: ValueError: XML Error: URDF joint parent or child missing\nElement 'joint', line 1\n",
  "https://github.com/unitreerobotics/unitree_ros robots/go1_description/xacro/depthCamera.xacro at 157ff950351e5f535e03c5d85a16b7d594b3dbcc: ValueError: Macro depthCamera requires unsupported explicit arguments: ['camID']",
  "https://github.com/unitreerobotics/unitree_ros robots/go1_description/xacro/transmission.xacro at 157ff950351e5f535e03c5d85a16b7d594b3dbcc: ValueError: XML has no robot bodies; it is an include/extension fragment, not a standalone source"
]
```

## History inputs

```json
[
  "robots/go1_description/meshes/calf.dae",
  "robots/go1_description/meshes/depthCamera.dae",
  "robots/go1_description/meshes/hip.dae",
  "robots/go1_description/meshes/thigh.dae",
  "robots/go1_description/meshes/thigh_mirror.dae",
  "robots/go1_description/meshes/trunk.dae",
  "robots/go1_description/meshes/ultraSound.dae",
  "robots/go1_description/urdf/go1.urdf"
]
```

## Self comparisons

```json
[
  {
    "file": "unitree_go1/go1.xml",
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
      "NO MATCHING SOURCE": 39
    },
    "classifications_changed": 0,
    "finding_membership_changes": 0
  },
  "2": {
    "provenance_method": "none",
    "counts": {
      "NO MATCHING SOURCE": 38
    },
    "classifications_changed": 0,
    "finding_membership_changes": 1
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
      "unitree_go1/go1.xml"
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
      "base",
      "camera_optical_face",
      "camera_optical_chin",
      "camera_optical_left",
      "camera_optical_right",
      "camera_optical_rearDown",
      "camera_laserscan_link_left",
      "camera_laserscan_link_right"
    ],
    "assets_loaded": 21,
    "mesh_conversions": [
      {
        "file": "robots/go1_description/meshes/trunk.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "robots/go1_description/meshes/hip.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "robots/go1_description/meshes/thigh_mirror.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "robots/go1_description/meshes/calf.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "robots/go1_description/meshes/hip.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "robots/go1_description/meshes/thigh.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "robots/go1_description/meshes/calf.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "robots/go1_description/meshes/hip.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "robots/go1_description/meshes/thigh_mirror.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "robots/go1_description/meshes/calf.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "robots/go1_description/meshes/hip.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "robots/go1_description/meshes/thigh.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "robots/go1_description/meshes/calf.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "robots/go1_description/meshes/depthCamera.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "robots/go1_description/meshes/depthCamera.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "robots/go1_description/meshes/depthCamera.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "robots/go1_description/meshes/depthCamera.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "robots/go1_description/meshes/depthCamera.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "robots/go1_description/meshes/ultraSound.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "robots/go1_description/meshes/ultraSound.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "robots/go1_description/meshes/ultraSound.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      }
    ],
    "nonphysical_normalizations": [],
    "xacro_arguments": {},
    "source_dependencies": [
      "robots/go1_description/urdf/go1.urdf",
      "robots/go1_description/meshes/trunk.dae",
      "robots/go1_description/meshes/hip.dae",
      "robots/go1_description/meshes/thigh_mirror.dae",
      "robots/go1_description/meshes/calf.dae",
      "robots/go1_description/meshes/hip.dae",
      "robots/go1_description/meshes/thigh.dae",
      "robots/go1_description/meshes/calf.dae",
      "robots/go1_description/meshes/hip.dae",
      "robots/go1_description/meshes/thigh_mirror.dae",
      "robots/go1_description/meshes/calf.dae",
      "robots/go1_description/meshes/hip.dae",
      "robots/go1_description/meshes/thigh.dae",
      "robots/go1_description/meshes/calf.dae",
      "robots/go1_description/meshes/depthCamera.dae",
      "robots/go1_description/meshes/depthCamera.dae",
      "robots/go1_description/meshes/depthCamera.dae",
      "robots/go1_description/meshes/depthCamera.dae",
      "robots/go1_description/meshes/depthCamera.dae",
      "robots/go1_description/meshes/ultraSound.dae",
      "robots/go1_description/meshes/ultraSound.dae",
      "robots/go1_description/meshes/ultraSound.dae"
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
  "historical_snapshots_reused": 4,
  "primary_physics_unchanged": true,
  "source_matching": "original raw-value provenance criteria retained; kinematic guard applies to reported CoM"
}
```
