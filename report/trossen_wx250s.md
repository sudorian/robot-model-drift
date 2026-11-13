# trossen_wx250s

Status: **complete**. Provenance: **none**, confidence **none**.

No public revision matches all comparable quantities. Class: NO MATCHING SOURCE; never counted as STALE.

M: `https://github.com/google-deepmind/mujoco_menagerie`, `trossen_wx250s/wx250s.xml`, commit `370c43965323c0944b433b202aac5058b5f907a9`.
H: `https://github.com/Interbotix/interbotix_ros_manipulators`, `interbotix_ros_xsarms/interbotix_xsarm_descriptions/urdf/wx250s.urdf.xacro`, commit `0bb2b0e6d0e619bff02cf74dbd5af5681dcf80c9`.
S: unavailable. A machine-readable H can still be compared to M; no-match differences are never counted as STALE.

Limit semantics: MJCF effort values are supported actuator torque/force envelopes. URDF effort and velocity values are manufacturer declarations retained from XML; MuJoCo does not enforce those tags. Such declaration comparisons are explicitly distinct from compiled inertial/range quantities.


## Source evidence

```json
[
  {
    "url": "https://github.com/Interbotix/interbotix_ros_manipulators/blob/main/interbotix_ros_xsarms/interbotix_xsarm_descriptions/meshes/interbotix_black.png",
    "document": "trossen_wx250s/README.md",
    "commit": "370c43965323c0944b433b202aac5058b5f907a9",
    "current": true
  },
  {
    "url": "https://github.com/Interbotix/interbotix_ros_manipulators/blob/main/interbotix_ros_xsarms/interbotix_xsarm_descriptions/urdf/wx250s.urdf.xacro",
    "document": "trossen_wx250s/README.md",
    "commit": "370c43965323c0944b433b202aac5058b5f907a9",
    "current": true
  }
]
```


## README derivation evidence

Documentation labels are conservative: an automated documented label requires an explicit affected entity and quantity. Broader conversion notes are retained here for review.

> 1. Added `<mujoco> <compiler discardvisual="false" strippath="false" fusestatic="false"/> </mujoco>` to the URDF's
>     * Removed all `actuatorfrcrange` as they were extremely low and affecting the actuation.

## Kinematics consistency

A proper Kabsch rigid transform aligns all matched zero-pose body origins. The maximum per-origin residual and signed hinge/slide axis angles determine whether CoM can be compared; RMS is also recorded. Fewer than three non-collinear origins give insufficient kinematic coverage. CoM records that fail either required M/H or M/S check are excluded from counts and largest discrepancies. Masses, principal moments and raw joint ranges remain unchanged; a flagged range still requires convention review.

| Pair | Status | Origins / rank | RMS / maximum mm | Disagreeing / checked axes |
|---|---|---:|---:|---:|
| M/H | consistent | 9 / 2 | 6.21512013e-14 / 7.85046229e-14 | 0 / 8 |

Exact fitted transforms, per-origin residuals, thresholds and axis vectors:

```json
{
  "M/H": {
    "status": "consistent",
    "matched_body_origins": 9,
    "position_threshold_m": 0.005,
    "axis_threshold_rad": 0.005,
    "residual_definition": "maximum Euclidean residual over matched body origins; Kabsch minimizes RMS, which is also recorded",
    "coordinate_frames": "each snapshot registered to its matched report anchor",
    "anchor_m": "wx250s/base_link",
    "anchor_other": "wx250s/base_link",
    "rotation_other_to_m": [
      [
        0.9999999999999998,
        0.0,
        1.9694837139087456e-16
      ],
      [
        0.0,
        1.0,
        0.0
      ],
      [
        -1.1102230246251565e-16,
        0.0,
        0.9999999999999998
      ]
    ],
    "translation_other_to_m": [
      0.0,
      0.0,
      5.551115123125783e-17
    ],
    "rms_residual_m": 6.215120129258017e-17,
    "max_residual_m": 7.850462293418876e-17,
    "fit_rank": 2,
    "axis_checks": [
      {
        "joint_m": "waist",
        "joint_other": "waist",
        "axis_m": [
          0.0,
          0.0,
          1.0
        ],
        "axis_other_aligned": [
          1.969483713908746e-16,
          0.0,
          1.0
        ],
        "angle_rad": 1.969483713908746e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "shoulder",
        "joint_other": "shoulder",
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
        "joint_m": "elbow",
        "joint_other": "elbow",
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
        "joint_m": "forearm_roll",
        "joint_other": "forearm_roll",
        "axis_m": [
          1.0,
          0.0,
          0.0
        ],
        "axis_other_aligned": [
          1.0,
          0.0,
          -1.1102230246251568e-16
        ],
        "angle_rad": 1.1102230246251568e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "wrist_angle",
        "joint_other": "wrist_angle",
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
        "joint_m": "wrist_rotate",
        "joint_other": "wrist_rotate",
        "axis_m": [
          1.0,
          0.0,
          0.0
        ],
        "axis_other_aligned": [
          1.0,
          0.0,
          -1.1102230246251568e-16
        ],
        "angle_rad": 1.1102230246251568e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "left_finger",
        "joint_other": "left_finger",
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
        "joint_m": "right_finger",
        "joint_other": "right_finger",
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
      }
    ],
    "axis_disagreements": [],
    "com_eligible": true,
    "covariance_singular_values": [
      0.4232279079746056,
      0.04957062980317221,
      0.0
    ],
    "origin_residuals_m": {
      "wx250s/base_link": 5.551115123125783e-17,
      "wx250s/shoulder_link": 4.3982011874616524e-17,
      "wx250s/upper_arm_link": 3.5288495894665206e-17,
      "wx250s/upper_forearm_link": 7.850462293418876e-17,
      "wx250s/lower_forearm_link": 6.206335383118183e-17,
      "wx250s/wrist_link": 5.551115123125783e-17,
      "wx250s/gripper_link": 5.551115123125783e-17,
      "wx250s/left_finger_link": 7.850462293418876e-17,
      "wx250s/right_finger_link": 7.850462293418876e-17
    },
    "reason": "Unique proper rigid fit and matched signed axes meet the configured thresholds"
  }
}
```


## Every reported quantity difference

Counts are quantity records, including correlated total/subtree/body mass records; they are not independent robot defects.

| Entity / quantity | M | S | H | H − M | Class | M source | S source | H source |
|---|---|---|---|---|---|---|---|---|
| robot / total_com_registered | [0.0792535516, 0.000717696912, 0.19994266] | unavailable | [0.0799333005, 0.000716236537, 0.200268989] | [0.000679748895, -1.46037415e-06, 0.000326329211] | NO MATCHING SOURCE | [aggregate inputs](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/trossen_wx250s/wx250s.xml#L1) | unavailable | [aggregate inputs](https://github.com/Interbotix/interbotix_ros_manipulators/blob/0bb2b0e6d0e619bff02cf74dbd5af5681dcf80c9/interbotix_ros_xsarms/interbotix_xsarm_descriptions/urdf/wx250s.urdf.xacro#L1) |
| wx250s/upper_forearm_link / subtree_mass | 0.683113 | unavailable | 0.687453 | 0.00434 | NO MATCHING SOURCE | [subtree root L57](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/trossen_wx250s/wx250s.xml#L57) | unavailable | [subtree root L152](https://github.com/Interbotix/interbotix_ros_manipulators/blob/0bb2b0e6d0e619bff02cf74dbd5af5681dcf80c9/interbotix_ros_xsarms/interbotix_xsarm_descriptions/urdf/wx250s.urdf.xacro#L152) |
| wx250s/lower_forearm_link / subtree_mass | 0.448524 | unavailable | 0.452864 | 0.00434 | NO MATCHING SOURCE | [subtree root L63](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/trossen_wx250s/wx250s.xml#L63) | unavailable | [subtree root L192](https://github.com/Interbotix/interbotix_ros_manipulators/blob/0bb2b0e6d0e619bff02cf74dbd5af5681dcf80c9/interbotix_ros_xsarms/interbotix_xsarm_descriptions/urdf/wx250s.urdf.xacro#L192) |
| wx250s/wrist_link / subtree_mass | 0.227533 | unavailable | 0.231873 | 0.00434 | NO MATCHING SOURCE | [subtree root L69](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/trossen_wx250s/wx250s.xml#L69) | unavailable | [subtree root L232](https://github.com/Interbotix/interbotix_ros_manipulators/blob/0bb2b0e6d0e619bff02cf74dbd5af5681dcf80c9/interbotix_ros_xsarms/interbotix_xsarm_descriptions/urdf/wx250s.urdf.xacro#L232) |
| wx250s/gripper_link / mass | 0.110084 | unavailable | 0.072885 | -0.037199 | NO MATCHING SOURCE | [input L77](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/trossen_wx250s/wx250s.xml#L77) | unavailable | [input L288](https://github.com/Interbotix/interbotix_ros_manipulators/blob/0bb2b0e6d0e619bff02cf74dbd5af5681dcf80c9/interbotix_ros_xsarms/interbotix_xsarm_descriptions/urdf/wx250s.urdf.xacro#L288) |
| wx250s/gripper_link / subtree_mass | 0.142576 | unavailable | 0.146916 | 0.00434 | NO MATCHING SOURCE | [subtree root L75](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/trossen_wx250s/wx250s.xml#L75) | unavailable | [subtree root L272](https://github.com/Interbotix/interbotix_ros_manipulators/blob/0bb2b0e6d0e619bff02cf74dbd5af5681dcf80c9/interbotix_ros_xsarms/interbotix_xsarm_descriptions/urdf/wx250s.urdf.xacro#L272) |
| wx250s/gripper_link / com_registered | [0.3972796, 4.2061e-07, 0.3697459] | unavailable | [0.386381, 2.516e-07, 0.37206] | [-0.0108986, -1.6901e-07, 0.0023141] | NO MATCHING SOURCE | [CoM/kinematic input L77](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/trossen_wx250s/wx250s.xml#L77) | unavailable | [CoM/kinematic input L287](https://github.com/Interbotix/interbotix_ros_manipulators/blob/0bb2b0e6d0e619bff02cf74dbd5af5681dcf80c9/interbotix_ros_xsarms/interbotix_xsarm_descriptions/urdf/wx250s.urdf.xacro#L287) |
| wx250s/gripper_link / principal_moments | [0.0030332, 0.00307326, 0.00307592] | unavailable | [1.66310571e-05, 1.84689429e-05, 2.537e-05] | [-0.00301656894, -0.00305479106, -0.00305055] | NO MATCHING SOURCE | [inertia input L77](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/trossen_wx250s/wx250s.xml#L77) | unavailable | [inertia input L289](https://github.com/Interbotix/interbotix_ros_manipulators/blob/0bb2b0e6d0e619bff02cf74dbd5af5681dcf80c9/interbotix_ros_xsarms/interbotix_xsarm_descriptions/urdf/wx250s.urdf.xacro#L289) |
| waist / effort | 35 | unavailable | 10 | -25 | NO MATCHING SOURCE | [inherited actuator input L26](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/trossen_wx250s/wx250s.xml#L26) | unavailable | [input L55](https://github.com/Interbotix/interbotix_ros_manipulators/blob/0bb2b0e6d0e619bff02cf74dbd5af5681dcf80c9/interbotix_ros_xsarms/interbotix_xsarm_descriptions/urdf/wx250s.urdf.xacro#L55) |
| shoulder / effort | 35 | unavailable | 20 | -15 | NO MATCHING SOURCE | [inherited actuator input L26](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/trossen_wx250s/wx250s.xml#L26) | unavailable | [input L95](https://github.com/Interbotix/interbotix_ros_manipulators/blob/0bb2b0e6d0e619bff02cf74dbd5af5681dcf80c9/interbotix_ros_xsarms/interbotix_xsarm_descriptions/urdf/wx250s.urdf.xacro#L95) |
| elbow / effort | 35 | unavailable | 15 | -20 | NO MATCHING SOURCE | [inherited actuator input L26](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/trossen_wx250s/wx250s.xml#L26) | unavailable | [input L135](https://github.com/Interbotix/interbotix_ros_manipulators/blob/0bb2b0e6d0e619bff02cf74dbd5af5681dcf80c9/interbotix_ros_xsarms/interbotix_xsarm_descriptions/urdf/wx250s.urdf.xacro#L135) |
| forearm_roll / effort | 35 | unavailable | 2 | -33 | NO MATCHING SOURCE | [inherited actuator input L26](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/trossen_wx250s/wx250s.xml#L26) | unavailable | [input L175](https://github.com/Interbotix/interbotix_ros_manipulators/blob/0bb2b0e6d0e619bff02cf74dbd5af5681dcf80c9/interbotix_ros_xsarms/interbotix_xsarm_descriptions/urdf/wx250s.urdf.xacro#L175) |
| wrist_angle / effort | 35 | unavailable | 5 | -30 | NO MATCHING SOURCE | [inherited actuator input L26](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/trossen_wx250s/wx250s.xml#L26) | unavailable | [input L215](https://github.com/Interbotix/interbotix_ros_manipulators/blob/0bb2b0e6d0e619bff02cf74dbd5af5681dcf80c9/interbotix_ros_xsarms/interbotix_xsarm_descriptions/urdf/wx250s.urdf.xacro#L215) |
| wrist_rotate / effort | 35 | unavailable | 1 | -34 | NO MATCHING SOURCE | [inherited actuator input L26](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/trossen_wx250s/wx250s.xml#L26) | unavailable | [input L255](https://github.com/Interbotix/interbotix_ros_manipulators/blob/0bb2b0e6d0e619bff02cf74dbd5af5681dcf80c9/interbotix_ros_xsarms/interbotix_xsarm_descriptions/urdf/wx250s.urdf.xacro#L255) |
| left_finger / effort | 35 | unavailable | 5 | -30 | NO MATCHING SOURCE | [inherited actuator input L26](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/trossen_wx250s/wx250s.xml#L26) | unavailable | [input L433](https://github.com/Interbotix/interbotix_ros_manipulators/blob/0bb2b0e6d0e619bff02cf74dbd5af5681dcf80c9/interbotix_ros_xsarms/interbotix_xsarm_descriptions/urdf/wx250s.urdf.xacro#L433) |

## Raw CoM records and reporting decisions

Raw values retain the previous root-anchor registration before Kabsch; original world coordinates also remain in the snapshots. Eligible findings above use the fitted transform into M. Excluded raw records below are diagnostic numbers, not findings. No CoM suppression applies to mass or principal inertia moments.

| Entity / quantity | Raw M | Raw S | Raw H | Raw H − M | Decision | M source | S source | H source |
|---|---|---|---|---|---|---|---|---|
| robot / total_com_registered | [0.0792535516, 0.000717696912, 0.19994266] | unavailable | [0.0799333005, 0.000716236537, 0.200268989] | [0.000679748895, -1.46037415e-06, 0.000326329211] | eligible; compared after Kabsch alignment | [aggregate inputs](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/trossen_wx250s/wx250s.xml#L1) | unavailable | [aggregate inputs](https://github.com/Interbotix/interbotix_ros_manipulators/blob/0bb2b0e6d0e619bff02cf74dbd5af5681dcf80c9/interbotix_ros_xsarms/interbotix_xsarm_descriptions/urdf/wx250s.urdf.xacro#L1) |
| wx250s/base_link / com_registered | [-0.0380446, 0.000613892, 0.0193354] | unavailable | [-0.0380446, 0.000613892, 0.0193354] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L42](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/trossen_wx250s/wx250s.xml#L42) | unavailable | [CoM/kinematic input L47](https://github.com/Interbotix/interbotix_ros_manipulators/blob/0bb2b0e6d0e619bff02cf74dbd5af5681dcf80c9/interbotix_ros_xsarms/interbotix_xsarm_descriptions/urdf/wx250s.urdf.xacro#L47) |
| wx250s/shoulder_link / com_registered | [2.23482e-05, 4.14609e-05, 0.0786287] | unavailable | [2.23482e-05, 4.14609e-05, 0.0786287] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L47](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/trossen_wx250s/wx250s.xml#L47) | unavailable | [CoM/kinematic input L87](https://github.com/Interbotix/interbotix_ros_manipulators/blob/0bb2b0e6d0e619bff02cf74dbd5af5681dcf80c9/interbotix_ros_xsarms/interbotix_xsarm_descriptions/urdf/wx250s.urdf.xacro#L87) |
| wx250s/upper_arm_link / com_registered | [0.0171605, 2.725e-07, 0.301973] | unavailable | [0.0171605, 2.725e-07, 0.301973] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L53](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/trossen_wx250s/wx250s.xml#L53) | unavailable | [CoM/kinematic input L127](https://github.com/Interbotix/interbotix_ros_manipulators/blob/0bb2b0e6d0e619bff02cf74dbd5af5681dcf80c9/interbotix_ros_xsarms/interbotix_xsarm_descriptions/urdf/wx250s.urdf.xacro#L127) |
| wx250s/upper_forearm_link / com_registered | [0.157713, 0.000115876, 0.36065] | unavailable | [0.157713, 0.000115876, 0.36065] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L59](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/trossen_wx250s/wx250s.xml#L59) | unavailable | [CoM/kinematic input L167](https://github.com/Interbotix/interbotix_ros_manipulators/blob/0bb2b0e6d0e619bff02cf74dbd5af5681dcf80c9/interbotix_ros_xsarms/interbotix_xsarm_descriptions/urdf/wx250s.urdf.xacro#L167) |
| wx250s/lower_forearm_link / com_registered | [0.2621895, 0.00522252, 0.36065] | unavailable | [0.2621895, 0.00522252, 0.36065] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L65](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/trossen_wx250s/wx250s.xml#L65) | unavailable | [CoM/kinematic input L207](https://github.com/Interbotix/interbotix_ros_manipulators/blob/0bb2b0e6d0e619bff02cf74dbd5af5681dcf80c9/interbotix_ros_xsarms/interbotix_xsarm_descriptions/urdf/wx250s.urdf.xacro#L207) |
| wx250s/wrist_link / com_registered | [0.34211, -1.0663e-05, 0.371227] | unavailable | [0.34211, -1.0663e-05, 0.371227] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L71](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/trossen_wx250s/wx250s.xml#L71) | unavailable | [CoM/kinematic input L247](https://github.com/Interbotix/interbotix_ros_manipulators/blob/0bb2b0e6d0e619bff02cf74dbd5af5681dcf80c9/interbotix_ros_xsarms/interbotix_xsarm_descriptions/urdf/wx250s.urdf.xacro#L247) |
| wx250s/gripper_link / com_registered | [0.3972796, 4.2061e-07, 0.3697459] | unavailable | [0.386381, 2.516e-07, 0.37206] | [-0.0108986, -1.6901e-07, 0.0023141] | eligible; compared after Kabsch alignment | [CoM/kinematic input L77](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/trossen_wx250s/wx250s.xml#L77) | unavailable | [CoM/kinematic input L287](https://github.com/Interbotix/interbotix_ros_manipulators/blob/0bb2b0e6d0e619bff02cf74dbd5af5681dcf80c9/interbotix_ros_xsarms/interbotix_xsarm_descriptions/urdf/wx250s.urdf.xacro#L287) |
| wx250s/left_finger_link / com_registered | [0.444566, 0, 0.36065] | unavailable | [0.444566, 0, 0.36065] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L85](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/trossen_wx250s/wx250s.xml#L85) | unavailable | [CoM/kinematic input L465](https://github.com/Interbotix/interbotix_ros_manipulators/blob/0bb2b0e6d0e619bff02cf74dbd5af5681dcf80c9/interbotix_ros_xsarms/interbotix_xsarm_descriptions/urdf/wx250s.urdf.xacro#L465) |
| wx250s/right_finger_link / com_registered | [0.444566, 0, 0.36065] | unavailable | [0.444566, 0, 0.36065] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L94](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/trossen_wx250s/wx250s.xml#L94) | unavailable | [CoM/kinematic input L508](https://github.com/Interbotix/interbotix_ros_manipulators/blob/0bb2b0e6d0e619bff02cf74dbd5af5681dcf80c9/interbotix_ros_xsarms/interbotix_xsarm_descriptions/urdf/wx250s.urdf.xacro#L508) |

## Mass accounting

Every contributing compiled body mass is listed here so total/subtree sums can be checked. Links point to explicit inertials or to geometry inputs when the compiler inferred a mass. CoM links identify inertial inputs; world coordinates additionally use the ancestor transforms and the registration recorded below.

| M body | M kg / source | S kg / source | H kg / source |
|---|---|---|---|
| wx250s/base_link | 0.538736 / [input L42](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/trossen_wx250s/wx250s.xml#L42) | unavailable | 0.538736 / [input L48](https://github.com/Interbotix/interbotix_ros_manipulators/blob/0bb2b0e6d0e619bff02cf74dbd5af5681dcf80c9/interbotix_ros_xsarms/interbotix_xsarm_descriptions/urdf/wx250s.urdf.xacro#L48) |
| wx250s/shoulder_link | 0.480879 / [input L47](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/trossen_wx250s/wx250s.xml#L47) | unavailable | 0.480879 / [input L88](https://github.com/Interbotix/interbotix_ros_manipulators/blob/0bb2b0e6d0e619bff02cf74dbd5af5681dcf80c9/interbotix_ros_xsarms/interbotix_xsarm_descriptions/urdf/wx250s.urdf.xacro#L88) |
| wx250s/upper_arm_link | 0.430811 / [input L53](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/trossen_wx250s/wx250s.xml#L53) | unavailable | 0.430811 / [input L128](https://github.com/Interbotix/interbotix_ros_manipulators/blob/0bb2b0e6d0e619bff02cf74dbd5af5681dcf80c9/interbotix_ros_xsarms/interbotix_xsarm_descriptions/urdf/wx250s.urdf.xacro#L128) |
| wx250s/upper_forearm_link | 0.234589 / [input L59](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/trossen_wx250s/wx250s.xml#L59) | unavailable | 0.234589 / [input L168](https://github.com/Interbotix/interbotix_ros_manipulators/blob/0bb2b0e6d0e619bff02cf74dbd5af5681dcf80c9/interbotix_ros_xsarms/interbotix_xsarm_descriptions/urdf/wx250s.urdf.xacro#L168) |
| wx250s/lower_forearm_link | 0.220991 / [input L65](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/trossen_wx250s/wx250s.xml#L65) | unavailable | 0.220991 / [input L208](https://github.com/Interbotix/interbotix_ros_manipulators/blob/0bb2b0e6d0e619bff02cf74dbd5af5681dcf80c9/interbotix_ros_xsarms/interbotix_xsarm_descriptions/urdf/wx250s.urdf.xacro#L208) |
| wx250s/wrist_link | 0.084957 / [input L71](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/trossen_wx250s/wx250s.xml#L71) | unavailable | 0.084957 / [input L248](https://github.com/Interbotix/interbotix_ros_manipulators/blob/0bb2b0e6d0e619bff02cf74dbd5af5681dcf80c9/interbotix_ros_xsarms/interbotix_xsarm_descriptions/urdf/wx250s.urdf.xacro#L248) |
| wx250s/gripper_link | 0.110084 / [input L77](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/trossen_wx250s/wx250s.xml#L77) | unavailable | 0.072885 / [input L288](https://github.com/Interbotix/interbotix_ros_manipulators/blob/0bb2b0e6d0e619bff02cf74dbd5af5681dcf80c9/interbotix_ros_xsarms/interbotix_xsarm_descriptions/urdf/wx250s.urdf.xacro#L288) |
| wx250s/left_finger_link | 0.016246 / [input L85](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/trossen_wx250s/wx250s.xml#L85) | unavailable | 0.016246 / [input L466](https://github.com/Interbotix/interbotix_ros_manipulators/blob/0bb2b0e6d0e619bff02cf74dbd5af5681dcf80c9/interbotix_ros_xsarms/interbotix_xsarm_descriptions/urdf/wx250s.urdf.xacro#L466) |
| wx250s/right_finger_link | 0.016246 / [input L94](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/trossen_wx250s/wx250s.xml#L94) | unavailable | 0.016246 / [input L509](https://github.com/Interbotix/interbotix_ros_manipulators/blob/0bb2b0e6d0e619bff02cf74dbd5af5681dcf80c9/interbotix_ros_xsarms/interbotix_xsarm_descriptions/urdf/wx250s.urdf.xacro#L509) |
| upstream-only wx250s/ee_arm_link | unavailable | unavailable | 0.001 / [input L302](https://github.com/Interbotix/interbotix_ros_manipulators/blob/0bb2b0e6d0e619bff02cf74dbd5af5681dcf80c9/interbotix_ros_xsarms/interbotix_xsarm_descriptions/urdf/wx250s.urdf.xacro#L302) |
| upstream-only wx250s/ee_gripper_link | unavailable | unavailable | 0.001 / [input L523](https://github.com/Interbotix/interbotix_ros_manipulators/blob/0bb2b0e6d0e619bff02cf74dbd5af5681dcf80c9/interbotix_ros_xsarms/interbotix_xsarm_descriptions/urdf/wx250s.urdf.xacro#L523) |
| upstream-only wx250s/fingers_link | unavailable | unavailable | 0.001 / [input L422](https://github.com/Interbotix/interbotix_ros_manipulators/blob/0bb2b0e6d0e619bff02cf74dbd5af5681dcf80c9/interbotix_ros_xsarms/interbotix_xsarm_descriptions/urdf/wx250s.urdf.xacro#L422) |
| upstream-only wx250s/gripper_bar_link | unavailable | unavailable | 0.034199 / [input L408](https://github.com/Interbotix/interbotix_ros_manipulators/blob/0bb2b0e6d0e619bff02cf74dbd5af5681dcf80c9/interbotix_ros_xsarms/interbotix_xsarm_descriptions/urdf/wx250s.urdf.xacro#L408) |
| upstream-only wx250s/gripper_prop_link | unavailable | unavailable | 0.00434 / [input L342](https://github.com/Interbotix/interbotix_ros_manipulators/blob/0bb2b0e6d0e619bff02cf74dbd5af5681dcf80c9/interbotix_ros_xsarms/interbotix_xsarm_descriptions/urdf/wx250s.urdf.xacro#L342) |

## Coverage and unmatched elements

```json
{
  "mapping_h": {
    "bodies": {
      "wx250s/base_link": "wx250s/base_link",
      "wx250s/shoulder_link": "wx250s/shoulder_link",
      "wx250s/upper_arm_link": "wx250s/upper_arm_link",
      "wx250s/upper_forearm_link": "wx250s/upper_forearm_link",
      "wx250s/lower_forearm_link": "wx250s/lower_forearm_link",
      "wx250s/wrist_link": "wx250s/wrist_link",
      "wx250s/gripper_link": "wx250s/gripper_link",
      "wx250s/left_finger_link": "wx250s/left_finger_link",
      "wx250s/right_finger_link": "wx250s/right_finger_link"
    },
    "joints": {
      "waist": "waist",
      "shoulder": "shoulder",
      "elbow": "elbow",
      "forearm_roll": "forearm_roll",
      "wrist_angle": "wrist_angle",
      "wrist_rotate": "wrist_rotate",
      "left_finger": "left_finger",
      "right_finger": "right_finger"
    },
    "body_methods": {
      "wx250s/base_link": "name",
      "wx250s/shoulder_link": "name",
      "wx250s/upper_arm_link": "name",
      "wx250s/upper_forearm_link": "name",
      "wx250s/lower_forearm_link": "name",
      "wx250s/wrist_link": "name",
      "wx250s/gripper_link": "name",
      "wx250s/left_finger_link": "name",
      "wx250s/right_finger_link": "name"
    },
    "joint_methods": {
      "waist": "name",
      "shoulder": "name",
      "elbow": "name",
      "forearm_roll": "name",
      "wrist_angle": "name",
      "wrist_rotate": "name",
      "left_finger": "name",
      "right_finger": "name"
    },
    "unmatched_m_bodies": [],
    "unmatched_upstream_bodies": [
      "wx250s/ee_arm_link",
      "wx250s/ee_gripper_link",
      "wx250s/fingers_link",
      "wx250s/gripper_bar_link",
      "wx250s/gripper_prop_link"
    ],
    "unmatched_m_joints": [],
    "unmatched_upstream_joints": [
      "gripper"
    ],
    "registration_anchor": {
      "M": "wx250s/base_link",
      "H": "wx250s/base_link",
      "root_unmatched": false
    }
  },
  "mapping_s": null,
  "unavailable": [
    {
      "entity": "waist",
      "other_entity": "waist",
      "quantity": "force",
      "tolerance": "limit",
      "m": 35.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "waist",
      "other_entity": "waist",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 3.141592653589793,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "shoulder",
      "other_entity": "shoulder",
      "quantity": "force",
      "tolerance": "limit",
      "m": 35.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "shoulder",
      "other_entity": "shoulder",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 3.141592653589793,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "elbow",
      "other_entity": "elbow",
      "quantity": "force",
      "tolerance": "limit",
      "m": 35.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "elbow",
      "other_entity": "elbow",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 3.141592653589793,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "forearm_roll",
      "other_entity": "forearm_roll",
      "quantity": "force",
      "tolerance": "limit",
      "m": 35.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "forearm_roll",
      "other_entity": "forearm_roll",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 3.141592653589793,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "wrist_angle",
      "other_entity": "wrist_angle",
      "quantity": "force",
      "tolerance": "limit",
      "m": 35.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "wrist_angle",
      "other_entity": "wrist_angle",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 3.141592653589793,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "wrist_rotate",
      "other_entity": "wrist_rotate",
      "quantity": "force",
      "tolerance": "limit",
      "m": 35.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "wrist_rotate",
      "other_entity": "wrist_rotate",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 3.141592653589793,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_finger",
      "other_entity": "left_finger",
      "quantity": "force",
      "tolerance": "limit",
      "m": 35.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_finger",
      "other_entity": "left_finger",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 1.0,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "right_finger",
      "other_entity": "right_finger",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": 5.0,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "right_finger",
      "other_entity": "right_finger",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "right_finger",
      "other_entity": "right_finger",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 1.0,
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
| waist / force | 35 | unavailable | unavailable |
| waist / velocity | unavailable | unavailable | 3.14159265 |
| shoulder / force | 35 | unavailable | unavailable |
| shoulder / velocity | unavailable | unavailable | 3.14159265 |
| elbow / force | 35 | unavailable | unavailable |
| elbow / velocity | unavailable | unavailable | 3.14159265 |
| forearm_roll / force | 35 | unavailable | unavailable |
| forearm_roll / velocity | unavailable | unavailable | 3.14159265 |
| wrist_angle / force | 35 | unavailable | unavailable |
| wrist_angle / velocity | unavailable | unavailable | 3.14159265 |
| wrist_rotate / force | 35 | unavailable | unavailable |
| wrist_rotate / velocity | unavailable | unavailable | 3.14159265 |
| left_finger / force | 35 | unavailable | unavailable |
| left_finger / velocity | unavailable | unavailable | 1 |
| right_finger / effort | unavailable | unavailable | 5 |
| right_finger / force | unavailable | unavailable | unavailable |
| right_finger / velocity | unavailable | unavailable | 1 |
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
  "interbotix_ros_xsarms/interbotix_xsarm_descriptions/urdf/control.urdf.xacro",
  "interbotix_ros_xsarms/interbotix_xsarm_descriptions/urdf/gazebo_configs.urdf.xacro",
  "interbotix_ros_xsarms/interbotix_xsarm_descriptions/urdf/wx250s.urdf.xacro"
]
```

## Self comparisons

```json
[
  {
    "file": "trossen_wx250s/wx250s.xml",
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
      "NO MATCHING SOURCE": 17
    },
    "classifications_changed": 0,
    "finding_membership_changes": 2
  },
  "2": {
    "provenance_method": "none",
    "counts": {
      "NO MATCHING SOURCE": 12
    },
    "classifications_changed": 0,
    "finding_membership_changes": 3
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
      "trossen_wx250s/wx250s.xml"
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
    "geometry_stripped": true,
    "missing_explicit_inertials": [],
    "assets_loaded": 0,
    "mesh_conversions": [],
    "nonphysical_normalizations": [],
    "xacro_arguments": {
      "robot_name": "wx250s",
      "base_link_frame": "base_link",
      "show_ar_tag": "false",
      "show_gripper_bar": "true",
      "show_gripper_fingers": "true",
      "use_world_frame": "false",
      "external_urdf_loc": "",
      "load_gazebo_configs": "false"
    },
    "source_dependencies": [
      "interbotix_ros_xsarms/interbotix_xsarm_descriptions/urdf/wx250s.urdf.xacro"
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
  "historical_snapshots_reused": 7,
  "primary_physics_unchanged": true,
  "source_matching": "original raw-value provenance criteria retained; kinematic guard applies to reported CoM"
}
```
