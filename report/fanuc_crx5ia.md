# fanuc_crx5ia

Status: **complete**. Provenance: **pinned**, confidence **high**.

Source selected using the ordered amended provenance rules.

M: `https://github.com/google-deepmind/mujoco_menagerie`, `fanuc_crx5ia/crx5ia.xml`, commit `370c43965323c0944b433b202aac5058b5f907a9`.
H: `https://github.com/FANUC-CORPORATION/fanuc_description`, `fanuc_crx_description/robot/crx5ia.urdf.xacro`, commit `fb40c9803a826ba68c7c8e28ba904a25efa7fcd2`.
S: `fb40c9803a826ba68c7c8e28ba904a25efa7fcd2` (2026-08-05T15:17:46+09:00). Menagerie release/change: 2026-10-30T17:08:38-07:00.

Limit semantics: MJCF effort values are supported actuator torque/force envelopes. URDF effort and velocity values are manufacturer declarations retained from XML; MuJoCo does not enforce those tags. Such declaration comparisons are explicitly distinct from compiled inertial/range quantities.


## Source evidence

```json
[
  {
    "url": "https://github.com/FANUC-CORPORATION/fanuc_description",
    "document": "fanuc_crx5ia/README.md",
    "commit": "370c43965323c0944b433b202aac5058b5f907a9",
    "current": true
  }
]
```


## README derivation evidence

Documentation labels are conservative: an automated documented label requires an explicit affected entity and quantity. Broader conversion notes are retained here for review.

> 3. Added `<mujoco> <compiler meshdir="assets" discardvisual="false" fusestatic="false" balanceinertia="true"/> </mujoco>`
> 6. Added position-controlled actuators using the URDF effort limits as
>    `forcerange` (160 N·m for J1–J3, 40 N·m for J4–J6) and tuned joint
> The URDF, meshes, and inertial parameters are © 2025–2026 FANUC CORPORATION

## Kinematics consistency

A proper Kabsch rigid transform aligns all matched zero-pose body origins. The maximum per-origin residual and signed hinge/slide axis angles determine whether CoM can be compared; RMS is also recorded. Fewer than three non-collinear origins give insufficient kinematic coverage. CoM records that fail either required M/H or M/S check are excluded from counts and largest discrepancies. Masses, principal moments and raw joint ranges remain unchanged; a flagged range still requires convention review.

| Pair | Status | Origins / rank | RMS / maximum mm | Disagreeing / checked axes |
|---|---|---:|---:|---:|
| M/H | consistent | 7 / 3 | 1.30943237e-13 / 1.73297134e-13 | 0 / 6 |
| M/S | consistent | 7 / 3 | 1.30943237e-13 / 1.73297134e-13 | 0 / 6 |

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
    "anchor_m": "base_link",
    "anchor_other": "base_link",
    "rotation_other_to_m": [
      [
        1.0,
        -5.565137488822728e-16,
        3.5188908768336515e-17
      ],
      [
        6.2666615017445e-16,
        1.0000000000000004,
        -3.9541343897811237e-16
      ],
      [
        -1.9916793908558716e-16,
        1.7564075194265172e-16,
        1.0000000000000002
      ]
    ],
    "translation_other_to_m": [
      -2.7755575615628914e-17,
      8.673617379884035e-17,
      -1.1102230246251565e-16
    ],
    "rms_residual_m": 1.3094323654036084e-16,
    "max_residual_m": 1.7329713442131156e-16,
    "fit_rank": 3,
    "axis_checks": [
      {
        "joint_m": "J1",
        "joint_other": "J1",
        "axis_m": [
          0.0,
          0.0,
          1.0
        ],
        "axis_other_aligned": [
          3.518890876833651e-17,
          -3.9541343897811227e-16,
          1.0
        ],
        "angle_rad": 3.9697612903649964e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "J2",
        "joint_other": "J2",
        "axis_m": [
          0.0,
          1.0,
          0.0
        ],
        "axis_other_aligned": [
          -5.565137488822725e-16,
          1.0,
          1.7564075194265164e-16
        ],
        "angle_rad": 5.835728115993591e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "J3",
        "joint_other": "J3",
        "axis_m": [
          0.0,
          -1.0,
          0.0
        ],
        "axis_other_aligned": [
          5.565137488822725e-16,
          -1.0,
          -1.7564075194265164e-16
        ],
        "angle_rad": 5.835728115993591e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "J4",
        "joint_other": "J4",
        "axis_m": [
          -1.0,
          0.0,
          0.0
        ],
        "axis_other_aligned": [
          -1.0,
          -6.2666615017445e-16,
          1.9916793908558716e-16
        ],
        "angle_rad": 6.575548127221536e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "J5",
        "joint_other": "J5",
        "axis_m": [
          0.0,
          -1.0,
          0.0
        ],
        "axis_other_aligned": [
          5.565137488822725e-16,
          -1.0,
          -1.7564075194265164e-16
        ],
        "angle_rad": 5.835728115993591e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "J6",
        "joint_other": "J6",
        "axis_m": [
          -1.0,
          0.0,
          0.0
        ],
        "axis_other_aligned": [
          -1.0,
          -6.2666615017445e-16,
          1.9916793908558716e-16
        ],
        "angle_rad": 6.575548127221536e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      }
    ],
    "axis_disagreements": [],
    "com_eligible": true,
    "covariance_singular_values": [
      0.525401297062902,
      0.1491673756315727,
      0.00825275587695394
    ],
    "origin_residuals_m": {
      "base_link": 1.4359487270475865e-16,
      "J1_link": 3.7500565358504275e-17,
      "J2_link": 3.7500565358504275e-17,
      "J3_link": 1.4869122695137974e-16,
      "J4_link": 1.4869122695137974e-16,
      "J5_link": 1.7329713442131156e-16,
      "J6_link": 1.4946834900704541e-16
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
    "anchor_m": "base_link",
    "anchor_other": "base_link",
    "rotation_other_to_m": [
      [
        1.0,
        -5.565137488822728e-16,
        3.5188908768336515e-17
      ],
      [
        6.2666615017445e-16,
        1.0000000000000004,
        -3.9541343897811237e-16
      ],
      [
        -1.9916793908558716e-16,
        1.7564075194265172e-16,
        1.0000000000000002
      ]
    ],
    "translation_other_to_m": [
      -2.7755575615628914e-17,
      8.673617379884035e-17,
      -1.1102230246251565e-16
    ],
    "rms_residual_m": 1.3094323654036084e-16,
    "max_residual_m": 1.7329713442131156e-16,
    "fit_rank": 3,
    "axis_checks": [
      {
        "joint_m": "J1",
        "joint_other": "J1",
        "axis_m": [
          0.0,
          0.0,
          1.0
        ],
        "axis_other_aligned": [
          3.518890876833651e-17,
          -3.9541343897811227e-16,
          1.0
        ],
        "angle_rad": 3.9697612903649964e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "J2",
        "joint_other": "J2",
        "axis_m": [
          0.0,
          1.0,
          0.0
        ],
        "axis_other_aligned": [
          -5.565137488822725e-16,
          1.0,
          1.7564075194265164e-16
        ],
        "angle_rad": 5.835728115993591e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "J3",
        "joint_other": "J3",
        "axis_m": [
          0.0,
          -1.0,
          0.0
        ],
        "axis_other_aligned": [
          5.565137488822725e-16,
          -1.0,
          -1.7564075194265164e-16
        ],
        "angle_rad": 5.835728115993591e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "J4",
        "joint_other": "J4",
        "axis_m": [
          -1.0,
          0.0,
          0.0
        ],
        "axis_other_aligned": [
          -1.0,
          -6.2666615017445e-16,
          1.9916793908558716e-16
        ],
        "angle_rad": 6.575548127221536e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "J5",
        "joint_other": "J5",
        "axis_m": [
          0.0,
          -1.0,
          0.0
        ],
        "axis_other_aligned": [
          5.565137488822725e-16,
          -1.0,
          -1.7564075194265164e-16
        ],
        "angle_rad": 5.835728115993591e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "J6",
        "joint_other": "J6",
        "axis_m": [
          -1.0,
          0.0,
          0.0
        ],
        "axis_other_aligned": [
          -1.0,
          -6.2666615017445e-16,
          1.9916793908558716e-16
        ],
        "angle_rad": 6.575548127221536e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      }
    ],
    "axis_disagreements": [],
    "com_eligible": true,
    "covariance_singular_values": [
      0.525401297062902,
      0.1491673756315727,
      0.00825275587695394
    ],
    "origin_residuals_m": {
      "base_link": 1.4359487270475865e-16,
      "J1_link": 3.7500565358504275e-17,
      "J2_link": 3.7500565358504275e-17,
      "J3_link": 1.4869122695137974e-16,
      "J4_link": 1.4869122695137974e-16,
      "J5_link": 1.7329713442131156e-16,
      "J6_link": 1.4946834900704541e-16
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
| robot / total_com_registered | [0.11923982, -0.0588660618, 0.385149122] | [0.11923982, -0.0588660618, 0.385149122] | [0.11923982, -0.0588660618, 0.385149122] | [0, 0, 5.55111512e-17] | eligible; compared after Kabsch alignment | [aggregate inputs](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/fanuc_crx5ia/crx5ia.xml#L1) | [aggregate inputs](https://github.com/FANUC-CORPORATION/fanuc_description/blob/fb40c9803a826ba68c7c8e28ba904a25efa7fcd2/fanuc_crx_description/robot/crx5ia.urdf.xacro#L1) | [aggregate inputs](https://github.com/FANUC-CORPORATION/fanuc_description/blob/fb40c9803a826ba68c7c8e28ba904a25efa7fcd2/fanuc_crx_description/robot/crx5ia.urdf.xacro#L1) |
| base_link / com_registered | [-0.02329, -0.00113, 0.04668] | [-0.02329, -0.00113, 0.04668] | [-0.02329, -0.00113, 0.04668] | [0, 0, 5.55111512e-17] | eligible; compared after Kabsch alignment | [CoM/kinematic input L66](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/fanuc_crx5ia/crx5ia.xml#L66) | [CoM/kinematic input L79](https://github.com/FANUC-CORPORATION/fanuc_description/blob/fb40c9803a826ba68c7c8e28ba904a25efa7fcd2/fanuc_crx_description/urdf/crx5ia_urdf_macro.xacro#L79) | [CoM/kinematic input L79](https://github.com/FANUC-CORPORATION/fanuc_description/blob/fb40c9803a826ba68c7c8e28ba904a25efa7fcd2/fanuc_crx_description/urdf/crx5ia_urdf_macro.xacro#L79) |
| J1_link / com_registered | [-0.00223, -0.04084, 0.155] | [-0.00223, -0.04084, 0.155] | [-0.00223, -0.04084, 0.155] | [0, 0, 2.77555756e-17] | eligible; compared after Kabsch alignment | [CoM/kinematic input L75](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/fanuc_crx5ia/crx5ia.xml#L75) | [CoM/kinematic input L111](https://github.com/FANUC-CORPORATION/fanuc_description/blob/fb40c9803a826ba68c7c8e28ba904a25efa7fcd2/fanuc_crx_description/urdf/crx5ia_urdf_macro.xacro#L111) | [CoM/kinematic input L111](https://github.com/FANUC-CORPORATION/fanuc_description/blob/fb40c9803a826ba68c7c8e28ba904a25efa7fcd2/fanuc_crx_description/urdf/crx5ia_urdf_macro.xacro#L111) |
| J2_link / com_registered | [0.00013, -0.14378, 0.37066] | [0.00013, -0.14378, 0.37066] | [0.00013, -0.14378, 0.37066] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L82](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/fanuc_crx5ia/crx5ia.xml#L82) | [CoM/kinematic input L143](https://github.com/FANUC-CORPORATION/fanuc_description/blob/fb40c9803a826ba68c7c8e28ba904a25efa7fcd2/fanuc_crx_description/urdf/crx5ia_urdf_macro.xacro#L143) | [CoM/kinematic input L143](https://github.com/FANUC-CORPORATION/fanuc_description/blob/fb40c9803a826ba68c7c8e28ba904a25efa7fcd2/fanuc_crx_description/urdf/crx5ia_urdf_macro.xacro#L143) |
| J3_link / com_registered | [0.0303, -0.01286, 0.5948] | [0.0303, -0.01286, 0.5948] | [0.0303, -0.01286, 0.5948] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L88](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/fanuc_crx5ia/crx5ia.xml#L88) | [CoM/kinematic input L175](https://github.com/FANUC-CORPORATION/fanuc_description/blob/fb40c9803a826ba68c7c8e28ba904a25efa7fcd2/fanuc_crx_description/urdf/crx5ia_urdf_macro.xacro#L175) | [CoM/kinematic input L175](https://github.com/FANUC-CORPORATION/fanuc_description/blob/fb40c9803a826ba68c7c8e28ba904a25efa7fcd2/fanuc_crx_description/urdf/crx5ia_urdf_macro.xacro#L175) |
| J4_link / com_registered | [0.28287, 0.00109, 0.59519] | [0.28287, 0.00109, 0.59519] | [0.28287, 0.00109, 0.59519] | [0, 0, -1.11022302e-16] | eligible; compared after Kabsch alignment | [CoM/kinematic input L95](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/fanuc_crx5ia/crx5ia.xml#L95) | [CoM/kinematic input L207](https://github.com/FANUC-CORPORATION/fanuc_description/blob/fb40c9803a826ba68c7c8e28ba904a25efa7fcd2/fanuc_crx_description/urdf/crx5ia_urdf_macro.xacro#L207) | [CoM/kinematic input L207](https://github.com/FANUC-CORPORATION/fanuc_description/blob/fb40c9803a826ba68c7c8e28ba904a25efa7fcd2/fanuc_crx_description/urdf/crx5ia_urdf_macro.xacro#L207) |
| J5_link / com_registered | [0.44442, -0.09491, 0.59664] | [0.44442, -0.09491, 0.59664] | [0.44442, -0.09491, 0.59664] | [0, 0, 1.11022302e-16] | eligible; compared after Kabsch alignment | [CoM/kinematic input L103](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/fanuc_crx5ia/crx5ia.xml#L103) | [CoM/kinematic input L242](https://github.com/FANUC-CORPORATION/fanuc_description/blob/fb40c9803a826ba68c7c8e28ba904a25efa7fcd2/fanuc_crx_description/urdf/crx5ia_urdf_macro.xacro#L242) | [CoM/kinematic input L242](https://github.com/FANUC-CORPORATION/fanuc_description/blob/fb40c9803a826ba68c7c8e28ba904a25efa7fcd2/fanuc_crx_description/urdf/crx5ia_urdf_macro.xacro#L242) |
| J6_link / com_registered | [0.53028, -0.12948, 0.59502] | [0.53028, -0.12948, 0.59502] | [0.53028, -0.12948, 0.59502] | [0, 0, -1.11022302e-16] | eligible; compared after Kabsch alignment | [CoM/kinematic input L110](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/fanuc_crx5ia/crx5ia.xml#L110) | [CoM/kinematic input L274](https://github.com/FANUC-CORPORATION/fanuc_description/blob/fb40c9803a826ba68c7c8e28ba904a25efa7fcd2/fanuc_crx_description/urdf/crx5ia_urdf_macro.xacro#L274) | [CoM/kinematic input L274](https://github.com/FANUC-CORPORATION/fanuc_description/blob/fb40c9803a826ba68c7c8e28ba904a25efa7fcd2/fanuc_crx_description/urdf/crx5ia_urdf_macro.xacro#L274) |

## Mass accounting

Every contributing compiled body mass is listed here so total/subtree sums can be checked. Links point to explicit inertials or to geometry inputs when the compiler inferred a mass. CoM links identify inertial inputs; world coordinates additionally use the ancestor transforms and the registration recorded below.

| M body | M kg / source | S kg / source | H kg / source |
|---|---|---|---|
| base_link | 2.695 / [input L66](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/fanuc_crx5ia/crx5ia.xml#L66) | 2.695 / [input L78](https://github.com/FANUC-CORPORATION/fanuc_description/blob/fb40c9803a826ba68c7c8e28ba904a25efa7fcd2/fanuc_crx_description/urdf/crx5ia_urdf_macro.xacro#L78) | 2.695 / [input L78](https://github.com/FANUC-CORPORATION/fanuc_description/blob/fb40c9803a826ba68c7c8e28ba904a25efa7fcd2/fanuc_crx_description/urdf/crx5ia_urdf_macro.xacro#L78) |
| J1_link | 5.173 / [input L75](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/fanuc_crx5ia/crx5ia.xml#L75) | 5.173 / [input L110](https://github.com/FANUC-CORPORATION/fanuc_description/blob/fb40c9803a826ba68c7c8e28ba904a25efa7fcd2/fanuc_crx_description/urdf/crx5ia_urdf_macro.xacro#L110) | 5.173 / [input L110](https://github.com/FANUC-CORPORATION/fanuc_description/blob/fb40c9803a826ba68c7c8e28ba904a25efa7fcd2/fanuc_crx_description/urdf/crx5ia_urdf_macro.xacro#L110) |
| J2_link | 5.014 / [input L82](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/fanuc_crx5ia/crx5ia.xml#L82) | 5.014 / [input L142](https://github.com/FANUC-CORPORATION/fanuc_description/blob/fb40c9803a826ba68c7c8e28ba904a25efa7fcd2/fanuc_crx_description/urdf/crx5ia_urdf_macro.xacro#L142) | 5.014 / [input L142](https://github.com/FANUC-CORPORATION/fanuc_description/blob/fb40c9803a826ba68c7c8e28ba904a25efa7fcd2/fanuc_crx_description/urdf/crx5ia_urdf_macro.xacro#L142) |
| J3_link | 3.133 / [input L88](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/fanuc_crx5ia/crx5ia.xml#L88) | 3.133 / [input L174](https://github.com/FANUC-CORPORATION/fanuc_description/blob/fb40c9803a826ba68c7c8e28ba904a25efa7fcd2/fanuc_crx_description/urdf/crx5ia_urdf_macro.xacro#L174) | 3.133 / [input L174](https://github.com/FANUC-CORPORATION/fanuc_description/blob/fb40c9803a826ba68c7c8e28ba904a25efa7fcd2/fanuc_crx_description/urdf/crx5ia_urdf_macro.xacro#L174) |
| J4_link | 3.508 / [input L95](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/fanuc_crx5ia/crx5ia.xml#L95) | 3.508 / [input L206](https://github.com/FANUC-CORPORATION/fanuc_description/blob/fb40c9803a826ba68c7c8e28ba904a25efa7fcd2/fanuc_crx_description/urdf/crx5ia_urdf_macro.xacro#L206) | 3.508 / [input L206](https://github.com/FANUC-CORPORATION/fanuc_description/blob/fb40c9803a826ba68c7c8e28ba904a25efa7fcd2/fanuc_crx_description/urdf/crx5ia_urdf_macro.xacro#L206) |
| J5_link | 2.434 / [input L103](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/fanuc_crx5ia/crx5ia.xml#L103) | 2.434 / [input L241](https://github.com/FANUC-CORPORATION/fanuc_description/blob/fb40c9803a826ba68c7c8e28ba904a25efa7fcd2/fanuc_crx_description/urdf/crx5ia_urdf_macro.xacro#L241) | 2.434 / [input L241](https://github.com/FANUC-CORPORATION/fanuc_description/blob/fb40c9803a826ba68c7c8e28ba904a25efa7fcd2/fanuc_crx_description/urdf/crx5ia_urdf_macro.xacro#L241) |
| J6_link | 1.272 / [input L110](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/fanuc_crx5ia/crx5ia.xml#L110) | 1.272 / [input L273](https://github.com/FANUC-CORPORATION/fanuc_description/blob/fb40c9803a826ba68c7c8e28ba904a25efa7fcd2/fanuc_crx_description/urdf/crx5ia_urdf_macro.xacro#L273) | 1.272 / [input L273](https://github.com/FANUC-CORPORATION/fanuc_description/blob/fb40c9803a826ba68c7c8e28ba904a25efa7fcd2/fanuc_crx_description/urdf/crx5ia_urdf_macro.xacro#L273) |
| upstream-only ee_link | unavailable | unavailable | 0 / [geometry/inference input L8](https://github.com/FANUC-CORPORATION/fanuc_description/blob/fb40c9803a826ba68c7c8e28ba904a25efa7fcd2/fanuc_crx_description/robot/crx5ia.urdf.xacro#L8) |
| upstream-only fanuc_flange | unavailable | unavailable | 0 / [geometry/inference input L374](https://github.com/FANUC-CORPORATION/fanuc_description/blob/fb40c9803a826ba68c7c8e28ba904a25efa7fcd2/fanuc_crx_description/urdf/crx5ia_urdf_macro.xacro#L374) |
| upstream-only flange | unavailable | unavailable | 0 / [geometry/inference input L374](https://github.com/FANUC-CORPORATION/fanuc_description/blob/fb40c9803a826ba68c7c8e28ba904a25efa7fcd2/fanuc_crx_description/urdf/crx5ia_urdf_macro.xacro#L374) |
| upstream-only wbase | unavailable | unavailable | 0 / [geometry/inference input L366](https://github.com/FANUC-CORPORATION/fanuc_description/blob/fb40c9803a826ba68c7c8e28ba904a25efa7fcd2/fanuc_crx_description/urdf/crx5ia_urdf_macro.xacro#L366) |

## Coverage and unmatched elements

```json
{
  "mapping_h": {
    "bodies": {
      "base_link": "base_link",
      "J1_link": "J1_link",
      "J2_link": "J2_link",
      "J3_link": "J3_link",
      "J4_link": "J4_link",
      "J5_link": "J5_link",
      "J6_link": "J6_link"
    },
    "joints": {
      "J1": "J1",
      "J2": "J2",
      "J3": "J3",
      "J4": "J4",
      "J5": "J5",
      "J6": "J6"
    },
    "body_methods": {
      "base_link": "name",
      "J1_link": "name",
      "J2_link": "name",
      "J3_link": "name",
      "J4_link": "name",
      "J5_link": "name",
      "J6_link": "name"
    },
    "joint_methods": {
      "J1": "name",
      "J2": "name",
      "J3": "name",
      "J4": "name",
      "J5": "name",
      "J6": "name"
    },
    "unmatched_m_bodies": [],
    "unmatched_upstream_bodies": [
      "ee_link",
      "fanuc_flange",
      "flange",
      "wbase"
    ],
    "unmatched_m_joints": [],
    "unmatched_upstream_joints": [],
    "registration_anchor": {
      "M": "base_link",
      "H": "base_link",
      "root_unmatched": false
    }
  },
  "mapping_s": {
    "bodies": {
      "base_link": "base_link",
      "J1_link": "J1_link",
      "J2_link": "J2_link",
      "J3_link": "J3_link",
      "J4_link": "J4_link",
      "J5_link": "J5_link",
      "J6_link": "J6_link"
    },
    "joints": {
      "J1": "J1",
      "J2": "J2",
      "J3": "J3",
      "J4": "J4",
      "J5": "J5",
      "J6": "J6"
    },
    "body_methods": {
      "base_link": "name",
      "J1_link": "name",
      "J2_link": "name",
      "J3_link": "name",
      "J4_link": "name",
      "J5_link": "name",
      "J6_link": "name"
    },
    "joint_methods": {
      "J1": "name",
      "J2": "name",
      "J3": "name",
      "J4": "name",
      "J5": "name",
      "J6": "name"
    },
    "unmatched_m_bodies": [],
    "unmatched_upstream_bodies": [
      "ee_link",
      "fanuc_flange",
      "flange",
      "wbase"
    ],
    "unmatched_m_joints": [],
    "unmatched_upstream_joints": [],
    "registration_anchor": {
      "M": "base_link",
      "S": "base_link"
    }
  },
  "unavailable": [
    {
      "entity": "J1",
      "other_entity": "J1",
      "quantity": "force",
      "tolerance": "limit",
      "m": 160.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "J1",
      "other_entity": "J1",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 2.6179938779914944,
      "s": 2.6179938779914944,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "J2",
      "other_entity": "J2",
      "quantity": "force",
      "tolerance": "limit",
      "m": 160.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "J2",
      "other_entity": "J2",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 2.6179938779914944,
      "s": 2.6179938779914944,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "J3",
      "other_entity": "J3",
      "quantity": "force",
      "tolerance": "limit",
      "m": 160.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "J3",
      "other_entity": "J3",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 3.141592653589793,
      "s": 3.141592653589793,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "J4",
      "other_entity": "J4",
      "quantity": "force",
      "tolerance": "limit",
      "m": 40.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "J4",
      "other_entity": "J4",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 3.9269908169872414,
      "s": 3.9269908169872414,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "J5",
      "other_entity": "J5",
      "quantity": "force",
      "tolerance": "limit",
      "m": 40.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "J5",
      "other_entity": "J5",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 3.9269908169872414,
      "s": 3.9269908169872414,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "J6",
      "other_entity": "J6",
      "quantity": "force",
      "tolerance": "limit",
      "m": 40.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "J6",
      "other_entity": "J6",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 3.9269908169872414,
      "s": 3.9269908169872414,
      "reason": "quantity absent or not enforced/declared on one side"
    }
  ]
}
```

## Limits unavailable for a like-for-like simulator comparison

URDF effort and velocity tags are manufacturer declarations; MuJoCo ignores them. Missing enforced quantities are not interpreted as zero. The available values are shown for review and excluded from STALE counts.

| Joint / quantity | M | S | H / declared upstream |
|---|---|---|---|
| J1 / force | 160 | unavailable | unavailable |
| J1 / velocity | unavailable | 2.61799388 | 2.61799388 |
| J2 / force | 160 | unavailable | unavailable |
| J2 / velocity | unavailable | 2.61799388 | 2.61799388 |
| J3 / force | 160 | unavailable | unavailable |
| J3 / velocity | unavailable | 3.14159265 | 3.14159265 |
| J4 / force | 40 | unavailable | unavailable |
| J4 / velocity | unavailable | 3.92699082 | 3.92699082 |
| J5 / force | 40 | unavailable | unavailable |
| J5 / velocity | unavailable | 3.92699082 | 3.92699082 |
| J6 / force | 40 | unavailable | unavailable |
| J6 / velocity | unavailable | 3.92699082 | 3.92699082 |
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
  "fanuc_crx_description/meshes/crx5ia/collision/base.stl",
  "fanuc_crx_description/meshes/crx5ia/collision/j1.stl",
  "fanuc_crx_description/meshes/crx5ia/collision/j2.stl",
  "fanuc_crx_description/meshes/crx5ia/collision/j3.stl",
  "fanuc_crx_description/meshes/crx5ia/collision/j4.stl",
  "fanuc_crx_description/meshes/crx5ia/collision/j5.stl",
  "fanuc_crx_description/meshes/crx5ia/collision/j6.stl",
  "fanuc_crx_description/meshes/crx5ia/visual/base.dae",
  "fanuc_crx_description/meshes/crx5ia/visual/j1.dae",
  "fanuc_crx_description/meshes/crx5ia/visual/j2.dae",
  "fanuc_crx_description/meshes/crx5ia/visual/j3.dae",
  "fanuc_crx_description/meshes/crx5ia/visual/j4.dae",
  "fanuc_crx_description/meshes/crx5ia/visual/j5.dae",
  "fanuc_crx_description/meshes/crx5ia/visual/j6.dae",
  "fanuc_crx_description/robot/crx5ia.urdf.xacro",
  "fanuc_crx_description/urdf/crx5ia_urdf_macro.xacro",
  "fanuc_crx_description/urdf/fanuc_common_urdf_macro.xacro"
]
```

## Self comparisons

```json
[
  {
    "file": "fanuc_crx5ia/crx5ia.xml",
    "status": "passed",
    "findings": 0
  }
]
```

## Sensitivity

```json
{
  "0.5": {
    "provenance_method": "pinned",
    "counts": {},
    "classifications_changed": 0,
    "finding_membership_changes": 0
  },
  "2": {
    "provenance_method": "pinned",
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
      "fanuc_crx5ia/crx5ia.xml"
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
      "ee_link",
      "wbase",
      "flange",
      "fanuc_flange"
    ],
    "assets_loaded": 14,
    "mesh_conversions": [
      {
        "file": "fanuc_crx_description/meshes/crx5ia/visual/base.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "fanuc_crx_description/meshes/crx5ia/visual/j1.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "fanuc_crx_description/meshes/crx5ia/visual/j2.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "fanuc_crx_description/meshes/crx5ia/visual/j3.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "fanuc_crx_description/meshes/crx5ia/visual/j4.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "fanuc_crx_description/meshes/crx5ia/visual/j5.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "fanuc_crx_description/meshes/crx5ia/visual/j6.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      }
    ],
    "nonphysical_normalizations": [],
    "xacro_arguments": {},
    "source_dependencies": [
      "fanuc_crx_description/robot/crx5ia.urdf.xacro",
      "fanuc_crx_description/urdf/crx5ia_urdf_macro.xacro",
      "fanuc_crx_description/meshes/crx5ia/visual/base.dae",
      "fanuc_crx_description/meshes/crx5ia/collision/base.stl",
      "fanuc_crx_description/meshes/crx5ia/visual/j1.dae",
      "fanuc_crx_description/meshes/crx5ia/collision/j1.stl",
      "fanuc_crx_description/meshes/crx5ia/visual/j2.dae",
      "fanuc_crx_description/meshes/crx5ia/collision/j2.stl",
      "fanuc_crx_description/meshes/crx5ia/visual/j3.dae",
      "fanuc_crx_description/meshes/crx5ia/collision/j3.stl",
      "fanuc_crx_description/meshes/crx5ia/visual/j4.dae",
      "fanuc_crx_description/meshes/crx5ia/collision/j4.stl",
      "fanuc_crx_description/meshes/crx5ia/visual/j5.dae",
      "fanuc_crx_description/meshes/crx5ia/collision/j5.stl",
      "fanuc_crx_description/meshes/crx5ia/visual/j6.dae",
      "fanuc_crx_description/meshes/crx5ia/collision/j6.stl"
    ],
    "registration": {
      "translation": [
        0.0,
        0.0,
        0.75
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
      "world",
      "ee_link",
      "wbase",
      "flange",
      "fanuc_flange"
    ],
    "assets_loaded": 14,
    "mesh_conversions": [
      {
        "file": "fanuc_crx_description/meshes/crx5ia/visual/base.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "fanuc_crx_description/meshes/crx5ia/visual/j1.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "fanuc_crx_description/meshes/crx5ia/visual/j2.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "fanuc_crx_description/meshes/crx5ia/visual/j3.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "fanuc_crx_description/meshes/crx5ia/visual/j4.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "fanuc_crx_description/meshes/crx5ia/visual/j5.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "fanuc_crx_description/meshes/crx5ia/visual/j6.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      }
    ],
    "nonphysical_normalizations": [],
    "xacro_arguments": {},
    "source_dependencies": [
      "fanuc_crx_description/robot/crx5ia.urdf.xacro",
      "fanuc_crx_description/urdf/crx5ia_urdf_macro.xacro",
      "fanuc_crx_description/meshes/crx5ia/visual/base.dae",
      "fanuc_crx_description/meshes/crx5ia/collision/base.stl",
      "fanuc_crx_description/meshes/crx5ia/visual/j1.dae",
      "fanuc_crx_description/meshes/crx5ia/collision/j1.stl",
      "fanuc_crx_description/meshes/crx5ia/visual/j2.dae",
      "fanuc_crx_description/meshes/crx5ia/collision/j2.stl",
      "fanuc_crx_description/meshes/crx5ia/visual/j3.dae",
      "fanuc_crx_description/meshes/crx5ia/collision/j3.stl",
      "fanuc_crx_description/meshes/crx5ia/visual/j4.dae",
      "fanuc_crx_description/meshes/crx5ia/collision/j4.stl",
      "fanuc_crx_description/meshes/crx5ia/visual/j5.dae",
      "fanuc_crx_description/meshes/crx5ia/collision/j5.stl",
      "fanuc_crx_description/meshes/crx5ia/visual/j6.dae",
      "fanuc_crx_description/meshes/crx5ia/collision/j6.stl"
    ],
    "registration": {
      "translation": [
        0.0,
        0.0,
        0.75
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
  "self_variants_recompiled": 1,
  "historical_snapshots_reused": 3,
  "primary_physics_unchanged": true,
  "source_matching": "original raw-value provenance criteria retained; kinematic guard applies to reported CoM"
}
```
