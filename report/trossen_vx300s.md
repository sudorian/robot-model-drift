# trossen_vx300s

Status: **complete**. Provenance: **none**, confidence **none**.

No public revision matches all comparable quantities. Class: NO MATCHING SOURCE; never counted as STALE.

M: `https://github.com/google-deepmind/mujoco_menagerie`, `trossen_vx300s/vx300s.xml`, commit `370c43965323c0944b433b202aac5058b5f907a9`.
H: `https://github.com/Interbotix/interbotix_ros_manipulators`, `interbotix_ros_xsarms/interbotix_xsarm_descriptions/urdf/vx300s.urdf.xacro`, commit `0bb2b0e6d0e619bff02cf74dbd5af5681dcf80c9`.
S: unavailable. A machine-readable H can still be compared to M; no-match differences are never counted as STALE.

Limit semantics: MJCF effort values are supported actuator torque/force envelopes. URDF effort and velocity values are manufacturer declarations retained from XML; MuJoCo does not enforce those tags. Such declaration comparisons are explicitly distinct from compiled inertial/range quantities.


## Source evidence

```json
[
  {
    "url": "https://github.com/Interbotix/interbotix_ros_manipulators/blob/main/interbotix_ros_xsarms/interbotix_xsarm_descriptions/meshes/interbotix_black.png",
    "document": "trossen_vx300s/README.md",
    "commit": "370c43965323c0944b433b202aac5058b5f907a9",
    "current": true
  },
  {
    "url": "https://github.com/Interbotix/interbotix_ros_manipulators/blob/main/interbotix_ros_xsarms/interbotix_xsarm_descriptions/urdf/vx300s.urdf.xacro",
    "document": "trossen_vx300s/README.md",
    "commit": "370c43965323c0944b433b202aac5058b5f907a9",
    "current": true
  }
]
```


## README derivation evidence

Documentation labels are conservative: an automated documented label requires an explicit affected entity and quantity. Broader conversion notes are retained here for review.

> 1. Added `<mujoco> <compiler discardvisual="false" strippath="false" fusestatic="false"/> </mujoco>` to the URDF's

## Kinematics consistency

A proper Kabsch rigid transform aligns all matched zero-pose body origins. The maximum per-origin residual and signed hinge/slide axis angles determine whether CoM can be compared; RMS is also recorded. Fewer than three non-collinear origins give insufficient kinematic coverage. CoM records that fail either required M/H or M/S check are excluded from counts and largest discrepancies. Masses, principal moments and raw joint ranges remain unchanged; a flagged range still requires convention review.

| Pair | Status | Origins / rank | RMS / maximum mm | Disagreeing / checked axes |
|---|---|---:|---:|---:|
| M/H | insufficient kinematic coverage | 1 / 0 | 0 / 0 | 0 / 0 |

Exact fitted transforms, per-origin residuals, thresholds and axis vectors:

```json
{
  "M/H": {
    "status": "insufficient kinematic coverage",
    "matched_body_origins": 1,
    "position_threshold_m": 0.005,
    "axis_threshold_rad": 0.005,
    "residual_definition": "maximum Euclidean residual over matched body origins; Kabsch minimizes RMS, which is also recorded",
    "coordinate_frames": "each snapshot registered to its matched report anchor",
    "anchor_m": "gripper_prop_link",
    "anchor_other": "vx300s/ee_gripper_link",
    "rotation_other_to_m": [
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
    ],
    "translation_other_to_m": [
      0.0,
      0.0,
      0.0
    ],
    "rms_residual_m": 0.0,
    "max_residual_m": 0.0,
    "fit_rank": 0,
    "axis_checks": [],
    "axis_disagreements": [],
    "com_eligible": false,
    "covariance_singular_values": [
      0.0,
      0.0,
      0.0
    ],
    "origin_residuals_m": {
      "gripper_prop_link": 0.0
    },
    "reason": "Fewer than three non-collinear matched origins; fitted rotation is underdetermined"
  }
}
```


## Every reported quantity difference

Counts are quantity records, including correlated total/subtree/body mass records; they are not independent robot defects.

| Entity / quantity | M | S | H | H − M | Class | M source | S source | H source |
|---|---|---|---|---|---|---|---|---|
| gripper_prop_link / mass | 0.008009 | unavailable | 0.001 | -0.007009 | NO MATCHING SOURCE | [input L119](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/trossen_vx300s/vx300s.xml#L119) | unavailable | [input L523](https://github.com/Interbotix/interbotix_ros_manipulators/blob/0bb2b0e6d0e619bff02cf74dbd5af5681dcf80c9/interbotix_ros_xsarms/interbotix_xsarm_descriptions/urdf/vx300s.urdf.xacro#L523) |
| gripper_prop_link / subtree_mass | 0.008009 | unavailable | 0.001 | -0.007009 | NO MATCHING SOURCE | [subtree root L117](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/trossen_vx300s/vx300s.xml#L117) | unavailable | [subtree root L521](https://github.com/Interbotix/interbotix_ros_manipulators/blob/0bb2b0e6d0e619bff02cf74dbd5af5681dcf80c9/interbotix_ros_xsarms/interbotix_xsarm_descriptions/urdf/vx300s.urdf.xacro#L521) |
| gripper_prop_link / principal_moments | [1.5314e-06, 2.8868e-06, 4.2979e-06] | unavailable | [0.0001, 0.0001, 0.0001] | [9.84686e-05, 9.71132e-05, 9.57021e-05] | NO MATCHING SOURCE | [inertia input L119](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/trossen_vx300s/vx300s.xml#L119) | unavailable | [inertia input L524](https://github.com/Interbotix/interbotix_ros_manipulators/blob/0bb2b0e6d0e619bff02cf74dbd5af5681dcf80c9/interbotix_ros_xsarms/interbotix_xsarm_descriptions/urdf/vx300s.urdf.xacro#L524) |
| waist / effort | 35 | unavailable | 10 | -25 | NO MATCHING SOURCE | [inherited actuator input L25](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/trossen_vx300s/vx300s.xml#L25) | unavailable | [input L55](https://github.com/Interbotix/interbotix_ros_manipulators/blob/0bb2b0e6d0e619bff02cf74dbd5af5681dcf80c9/interbotix_ros_xsarms/interbotix_xsarm_descriptions/urdf/vx300s.urdf.xacro#L55) |
| shoulder / effort | 57 | unavailable | 20 | -37 | NO MATCHING SOURCE | [inherited actuator input L32](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/trossen_vx300s/vx300s.xml#L32) | unavailable | [input L95](https://github.com/Interbotix/interbotix_ros_manipulators/blob/0bb2b0e6d0e619bff02cf74dbd5af5681dcf80c9/interbotix_ros_xsarms/interbotix_xsarm_descriptions/urdf/vx300s.urdf.xacro#L95) |
| elbow / effort | 25 | unavailable | 15 | -10 | NO MATCHING SOURCE | [inherited actuator input L36](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/trossen_vx300s/vx300s.xml#L36) | unavailable | [input L135](https://github.com/Interbotix/interbotix_ros_manipulators/blob/0bb2b0e6d0e619bff02cf74dbd5af5681dcf80c9/interbotix_ros_xsarms/interbotix_xsarm_descriptions/urdf/vx300s.urdf.xacro#L135) |
| forearm_roll / effort | 10 | unavailable | 2 | -8 | NO MATCHING SOURCE | [inherited actuator input L40](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/trossen_vx300s/vx300s.xml#L40) | unavailable | [input L175](https://github.com/Interbotix/interbotix_ros_manipulators/blob/0bb2b0e6d0e619bff02cf74dbd5af5681dcf80c9/interbotix_ros_xsarms/interbotix_xsarm_descriptions/urdf/vx300s.urdf.xacro#L175) |
| wrist_angle / effort | 35 | unavailable | 5 | -30 | NO MATCHING SOURCE | [inherited actuator input L25](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/trossen_vx300s/vx300s.xml#L25) | unavailable | [input L215](https://github.com/Interbotix/interbotix_ros_manipulators/blob/0bb2b0e6d0e619bff02cf74dbd5af5681dcf80c9/interbotix_ros_xsarms/interbotix_xsarm_descriptions/urdf/vx300s.urdf.xacro#L215) |
| wrist_rotate / effort | 35 | unavailable | 1 | -34 | NO MATCHING SOURCE | [inherited actuator input L25](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/trossen_vx300s/vx300s.xml#L25) | unavailable | [input L255](https://github.com/Interbotix/interbotix_ros_manipulators/blob/0bb2b0e6d0e619bff02cf74dbd5af5681dcf80c9/interbotix_ros_xsarms/interbotix_xsarm_descriptions/urdf/vx300s.urdf.xacro#L255) |
| left_finger / effort | 35 | unavailable | 5 | -30 | NO MATCHING SOURCE | [inherited actuator input L25](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/trossen_vx300s/vx300s.xml#L25) | unavailable | [input L433](https://github.com/Interbotix/interbotix_ros_manipulators/blob/0bb2b0e6d0e619bff02cf74dbd5af5681dcf80c9/interbotix_ros_xsarms/interbotix_xsarm_descriptions/urdf/vx300s.urdf.xacro#L433) |

## Raw CoM records and reporting decisions

Raw values retain the previous root-anchor registration before Kabsch; original world coordinates also remain in the snapshots. Eligible findings above use the fitted transform into M. Excluded raw records below are diagnostic numbers, not findings. No CoM suppression applies to mass or principal inertia moments.

| Entity / quantity | Raw M | Raw S | Raw H | Raw H − M | Decision | M source | S source | H source |
|---|---|---|---|---|---|---|---|---|
| robot / total_com_registered | [-0.383833566, 0.000607687776, -0.192042587] | unavailable | [-0.442533565, 0.000607687776, -0.192042587] | [-0.0586999996, -1.16058422e-14, -2.77791845e-10] | M/H: insufficient kinematic coverage | [aggregate inputs](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/trossen_vx300s/vx300s.xml#L1) | unavailable | [aggregate inputs](https://github.com/Interbotix/interbotix_ros_manipulators/blob/0bb2b0e6d0e619bff02cf74dbd5af5681dcf80c9/interbotix_ros_xsarms/interbotix_xsarm_descriptions/urdf/vx300s.urdf.xacro#L1) |
| gripper_prop_link / com_registered | [0.002378, 2.85e-08, 0] | unavailable | [0, 0, 0] | [-0.002378, -2.85e-08, 0] | M/H: insufficient kinematic coverage | [CoM/kinematic input L119](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/trossen_vx300s/vx300s.xml#L119) | unavailable | [geometry/inference input L521](https://github.com/Interbotix/interbotix_ros_manipulators/blob/0bb2b0e6d0e619bff02cf74dbd5af5681dcf80c9/interbotix_ros_xsarms/interbotix_xsarm_descriptions/urdf/vx300s.urdf.xacro#L521) |

## Mass accounting

Every contributing compiled body mass is listed here so total/subtree sums can be checked. Links point to explicit inertials or to geometry inputs when the compiler inferred a mass. CoM links identify inertial inputs; world coordinates additionally use the ancestor transforms and the registration recorded below.

| M body | M kg / source | S kg / source | H kg / source |
|---|---|---|---|
| base_link | 0.969034 / [input L75](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/trossen_vx300s/vx300s.xml#L75) | unavailable | unmatched |
| shoulder_link | 0.798614 / [input L80](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/trossen_vx300s/vx300s.xml#L80) | unavailable | unmatched |
| upper_arm_link | 0.792592 / [input L86](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/trossen_vx300s/vx300s.xml#L86) | unavailable | unmatched |
| upper_forearm_link | 0.322228 / [input L92](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/trossen_vx300s/vx300s.xml#L92) | unavailable | unmatched |
| lower_forearm_link | 0.414823 / [input L98](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/trossen_vx300s/vx300s.xml#L98) | unavailable | unmatched |
| wrist_link | 0.115395 / [input L104](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/trossen_vx300s/vx300s.xml#L104) | unavailable | unmatched |
| gripper_link | 0.251652 / [input L110](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/trossen_vx300s/vx300s.xml#L110) | unavailable | unmatched |
| gripper_prop_link | 0.008009 / [input L119](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/trossen_vx300s/vx300s.xml#L119) | unavailable | 0.001 / [input L523](https://github.com/Interbotix/interbotix_ros_manipulators/blob/0bb2b0e6d0e619bff02cf74dbd5af5681dcf80c9/interbotix_ros_xsarms/interbotix_xsarm_descriptions/urdf/vx300s.urdf.xacro#L523) |
| left_finger_link | 0.034796 / [input L125](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/trossen_vx300s/vx300s.xml#L125) | unavailable | unmatched |
| right_finger_link | 0.034796 / [input L149](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/trossen_vx300s/vx300s.xml#L149) | unavailable | unmatched |
| upstream-only vx300s/base_link | unavailable | unavailable | 0.969034 / [input L48](https://github.com/Interbotix/interbotix_ros_manipulators/blob/0bb2b0e6d0e619bff02cf74dbd5af5681dcf80c9/interbotix_ros_xsarms/interbotix_xsarm_descriptions/urdf/vx300s.urdf.xacro#L48) |
| upstream-only vx300s/ee_arm_link | unavailable | unavailable | 0.001 / [input L302](https://github.com/Interbotix/interbotix_ros_manipulators/blob/0bb2b0e6d0e619bff02cf74dbd5af5681dcf80c9/interbotix_ros_xsarms/interbotix_xsarm_descriptions/urdf/vx300s.urdf.xacro#L302) |
| upstream-only vx300s/fingers_link | unavailable | unavailable | 0.001 / [input L422](https://github.com/Interbotix/interbotix_ros_manipulators/blob/0bb2b0e6d0e619bff02cf74dbd5af5681dcf80c9/interbotix_ros_xsarms/interbotix_xsarm_descriptions/urdf/vx300s.urdf.xacro#L422) |
| upstream-only vx300s/gripper_bar_link | unavailable | unavailable | 0.150986 / [input L408](https://github.com/Interbotix/interbotix_ros_manipulators/blob/0bb2b0e6d0e619bff02cf74dbd5af5681dcf80c9/interbotix_ros_xsarms/interbotix_xsarm_descriptions/urdf/vx300s.urdf.xacro#L408) |
| upstream-only vx300s/gripper_link | unavailable | unavailable | 0.097666 / [input L288](https://github.com/Interbotix/interbotix_ros_manipulators/blob/0bb2b0e6d0e619bff02cf74dbd5af5681dcf80c9/interbotix_ros_xsarms/interbotix_xsarm_descriptions/urdf/vx300s.urdf.xacro#L288) |
| upstream-only vx300s/gripper_prop_link | unavailable | unavailable | 0.008009 / [input L342](https://github.com/Interbotix/interbotix_ros_manipulators/blob/0bb2b0e6d0e619bff02cf74dbd5af5681dcf80c9/interbotix_ros_xsarms/interbotix_xsarm_descriptions/urdf/vx300s.urdf.xacro#L342) |
| upstream-only vx300s/left_finger_link | unavailable | unavailable | 0.034796 / [input L466](https://github.com/Interbotix/interbotix_ros_manipulators/blob/0bb2b0e6d0e619bff02cf74dbd5af5681dcf80c9/interbotix_ros_xsarms/interbotix_xsarm_descriptions/urdf/vx300s.urdf.xacro#L466) |
| upstream-only vx300s/lower_forearm_link | unavailable | unavailable | 0.414823 / [input L208](https://github.com/Interbotix/interbotix_ros_manipulators/blob/0bb2b0e6d0e619bff02cf74dbd5af5681dcf80c9/interbotix_ros_xsarms/interbotix_xsarm_descriptions/urdf/vx300s.urdf.xacro#L208) |
| upstream-only vx300s/right_finger_link | unavailable | unavailable | 0.034796 / [input L509](https://github.com/Interbotix/interbotix_ros_manipulators/blob/0bb2b0e6d0e619bff02cf74dbd5af5681dcf80c9/interbotix_ros_xsarms/interbotix_xsarm_descriptions/urdf/vx300s.urdf.xacro#L509) |
| upstream-only vx300s/shoulder_link | unavailable | unavailable | 0.798614 / [input L88](https://github.com/Interbotix/interbotix_ros_manipulators/blob/0bb2b0e6d0e619bff02cf74dbd5af5681dcf80c9/interbotix_ros_xsarms/interbotix_xsarm_descriptions/urdf/vx300s.urdf.xacro#L88) |
| upstream-only vx300s/upper_arm_link | unavailable | unavailable | 0.792592 / [input L128](https://github.com/Interbotix/interbotix_ros_manipulators/blob/0bb2b0e6d0e619bff02cf74dbd5af5681dcf80c9/interbotix_ros_xsarms/interbotix_xsarm_descriptions/urdf/vx300s.urdf.xacro#L128) |
| upstream-only vx300s/upper_forearm_link | unavailable | unavailable | 0.322228 / [input L168](https://github.com/Interbotix/interbotix_ros_manipulators/blob/0bb2b0e6d0e619bff02cf74dbd5af5681dcf80c9/interbotix_ros_xsarms/interbotix_xsarm_descriptions/urdf/vx300s.urdf.xacro#L168) |
| upstream-only vx300s/wrist_link | unavailable | unavailable | 0.115395 / [input L248](https://github.com/Interbotix/interbotix_ros_manipulators/blob/0bb2b0e6d0e619bff02cf74dbd5af5681dcf80c9/interbotix_ros_xsarms/interbotix_xsarm_descriptions/urdf/vx300s.urdf.xacro#L248) |

## Coverage and unmatched elements

```json
{
  "mapping_h": {
    "bodies": {
      "gripper_prop_link": "vx300s/ee_gripper_link"
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
      "gripper_prop_link": "unique kinematic subtree"
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
    "unmatched_m_bodies": [
      "base_link",
      "gripper_link",
      "left_finger_link",
      "lower_forearm_link",
      "right_finger_link",
      "shoulder_link",
      "upper_arm_link",
      "upper_forearm_link",
      "wrist_link"
    ],
    "unmatched_upstream_bodies": [
      "vx300s/base_link",
      "vx300s/ee_arm_link",
      "vx300s/fingers_link",
      "vx300s/gripper_bar_link",
      "vx300s/gripper_link",
      "vx300s/gripper_prop_link",
      "vx300s/left_finger_link",
      "vx300s/lower_forearm_link",
      "vx300s/right_finger_link",
      "vx300s/shoulder_link",
      "vx300s/upper_arm_link",
      "vx300s/upper_forearm_link",
      "vx300s/wrist_link"
    ],
    "unmatched_m_joints": [],
    "unmatched_upstream_joints": [
      "gripper"
    ],
    "registration_anchor": {
      "M": "gripper_prop_link",
      "H": "vx300s/ee_gripper_link",
      "root_unmatched": true
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
      "m": 57.0,
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
      "m": 25.0,
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
      "m": 10.0,
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
| shoulder / force | 57 | unavailable | unavailable |
| shoulder / velocity | unavailable | unavailable | 3.14159265 |
| elbow / force | 25 | unavailable | unavailable |
| elbow / velocity | unavailable | unavailable | 3.14159265 |
| forearm_roll / force | 10 | unavailable | unavailable |
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
  "interbotix_ros_xsarms/interbotix_xsarm_descriptions/urdf/vx300s.urdf.xacro"
]
```

## Self comparisons

```json
[
  {
    "file": "trossen_vx300s/vx300s.xml",
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
      "NO MATCHING SOURCE": 10
    },
    "classifications_changed": 0,
    "finding_membership_changes": 0
  },
  "2": {
    "provenance_method": "none",
    "counts": {
      "NO MATCHING SOURCE": 10
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
      "trossen_vx300s/vx300s.xml"
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
      "robot_name": "vx300s",
      "base_link_frame": "base_link",
      "show_ar_tag": "false",
      "show_gripper_bar": "true",
      "show_gripper_fingers": "true",
      "use_world_frame": "false",
      "external_urdf_loc": "",
      "load_gazebo_configs": "false"
    },
    "source_dependencies": [
      "interbotix_ros_xsarms/interbotix_xsarm_descriptions/urdf/vx300s.urdf.xacro"
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
  "historical_snapshots_reused": 8,
  "primary_physics_unchanged": true,
  "source_matching": "original raw-value provenance criteria retained; kinematic guard applies to reported CoM"
}
```
