# iit_softfoot

Status: **complete**. Provenance: **dated match**, confidence **medium**.

Source selected using the ordered amended provenance rules.

M: `https://github.com/google-deepmind/mujoco_menagerie`, `iit_softfoot/softfoot.xml`, commit `370c43965323c0944b433b202aac5058b5f907a9`.
H: `https://github.com/NMMI/SoftFoot_MuJoCo`, `softfoot.xml`, commit `3b87622feb1e36e9a758aa76854204412d4ca8e8`.
S: `43834f4490adf19a2443e8daa81d3a69fe716ea5` (2024-12-11T12:41:12+01:00). Menagerie release/change: 2024-12-11T12:59:49Z.

Limit semantics: MJCF effort values are supported actuator torque/force envelopes. URDF effort and velocity values are manufacturer declarations retained from XML; MuJoCo does not enforce those tags. Such declaration comparisons are explicitly distinct from compiled inertial/range quantities.


## Source evidence

```json
[
  {
    "url": "https://github.com/NMMI/SoftFoot_MuJoCo",
    "document": "iit_softfoot/README.md",
    "commit": "370c43965323c0944b433b202aac5058b5f907a9",
    "current": true
  },
  {
    "url": "https://github.com/google-deepmind/dm_control/tree/main/dm_control/mjcf",
    "document": "iit_softfoot/README.md",
    "commit": "370c43965323c0944b433b202aac5058b5f907a9",
    "current": true
  }
]
```


## Kinematics consistency

A proper Kabsch rigid transform aligns all matched zero-pose body origins. The maximum per-origin residual and signed hinge/slide axis angles determine whether CoM can be compared; RMS is also recorded. Fewer than three non-collinear origins give insufficient kinematic coverage. CoM records that fail either required M/H or M/S check are excluded from counts and largest discrepancies. Masses, principal moments and raw joint ranges remain unchanged; a flagged range still requires convention review.

| Pair | Status | Origins / rank | RMS / maximum mm | Disagreeing / checked axes |
|---|---|---:|---:|---:|
| M/H | consistent | 49 / 3 | 1.61475609e-14 / 2.77569084e-14 | 0 / 92 |
| M/S | consistent | 49 / 3 | 1.61475609e-14 / 2.77569084e-14 | 0 / 92 |

Exact fitted transforms, per-origin residuals, thresholds and axis vectors:

```json
{
  "M/H": {
    "status": "consistent",
    "matched_body_origins": 49,
    "position_threshold_m": 0.005,
    "axis_threshold_rad": 0.005,
    "residual_definition": "maximum Euclidean residual over matched body origins; Kabsch minimizes RMS, which is also recorded",
    "coordinate_frames": "each snapshot registered to its matched report anchor",
    "anchor_m": "attachment_cube",
    "anchor_other": "attachment_cube",
    "rotation_other_to_m": [
      [
        1.0000000000000002,
        3.9204323500495214e-17,
        7.443474041670852e-18
      ],
      [
        1.1222604088474022e-17,
        1.0,
        2.8680063501349526e-17
      ],
      [
        1.1899118843028411e-17,
        -1.5157146371347352e-16,
        1.0000000000000004
      ]
    ],
    "translation_other_to_m": [
      -1.3877787807814457e-17,
      0.0,
      1.1384122811097797e-17
    ],
    "rms_residual_m": 1.6147560902450608e-17,
    "max_residual_m": 2.7756908414657696e-17,
    "fit_rank": 3,
    "axis_checks": [
      {
        "joint_m": "posterior_arch_to_heel",
        "joint_other": "posterior_arch_to_heel",
        "axis_m": [
          1.827910301094998e-17,
          4.440892098500624e-16,
          1.0
        ],
        "axis_other_aligned": [
          2.5722577052620843e-17,
          4.727692733514118e-16,
          1.0
        ],
        "angle_rad": 2.963024381017577e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "heel_phalanx_1_to_virtual_1_1",
        "joint_other": "heel_phalanx_1_to_virtual_1_1",
        "axis_m": [
          4.734643501393354e-33,
          6.661338147750934e-16,
          1.0
        ],
        "axis_other_aligned": [
          7.443474041670879e-18,
          6.948138782764426e-16,
          1.0
        ],
        "angle_rad": 2.9630243810175585e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "virtual_1_1_to_phalanx_1_1",
        "joint_other": "virtual_1_1_to_phalanx_1_1",
        "axis_m": [
          4.537561723341792e-33,
          6.661338147750935e-16,
          1.0
        ],
        "axis_other_aligned": [
          7.443474041670879e-18,
          6.948138782764427e-16,
          1.0
        ],
        "angle_rad": 2.9630243810175585e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "phalanx_1_1_to_virtual_2_1",
        "joint_other": "phalanx_1_1_to_virtual_2_1",
        "axis_m": [
          4.537561723341792e-33,
          6.661338147750935e-16,
          1.0
        ],
        "axis_other_aligned": [
          7.443474041670879e-18,
          6.948138782764427e-16,
          1.0
        ],
        "angle_rad": 2.9630243810175585e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "virtual_2_1_to_phalanx_2_1",
        "joint_other": "virtual_2_1_to_phalanx_2_1",
        "axis_m": [
          4.537561723341792e-33,
          6.661338147750935e-16,
          1.0
        ],
        "axis_other_aligned": [
          7.443474041670879e-18,
          6.948138782764427e-16,
          1.0
        ],
        "angle_rad": 2.9630243810175585e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "phalanx_2_1_to_virtual_3_1",
        "joint_other": "phalanx_2_1_to_virtual_3_1",
        "axis_m": [
          4.537561723341792e-33,
          6.661338147750935e-16,
          1.0
        ],
        "axis_other_aligned": [
          7.443474041670879e-18,
          6.948138782764427e-16,
          1.0
        ],
        "angle_rad": 2.9630243810175585e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "virtual_3_1_to_phalanx_3_1",
        "joint_other": "virtual_3_1_to_phalanx_3_1",
        "axis_m": [
          4.537561723341792e-33,
          6.661338147750935e-16,
          1.0
        ],
        "axis_other_aligned": [
          7.443474041670879e-18,
          6.948138782764427e-16,
          1.0
        ],
        "angle_rad": 2.9630243810175585e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "phalanx_3_1_to_virtual_4_1",
        "joint_other": "phalanx_3_1_to_virtual_4_1",
        "axis_m": [
          4.537561723341792e-33,
          6.661338147750935e-16,
          1.0
        ],
        "axis_other_aligned": [
          7.443474041670879e-18,
          6.948138782764427e-16,
          1.0
        ],
        "angle_rad": 2.9630243810175585e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "virtual_4_1_to_phalanx_4_1",
        "joint_other": "virtual_4_1_to_phalanx_4_1",
        "axis_m": [
          4.537561723341792e-33,
          6.661338147750935e-16,
          1.0
        ],
        "axis_other_aligned": [
          7.443474041670879e-18,
          6.948138782764427e-16,
          1.0
        ],
        "angle_rad": 2.9630243810175585e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "phalanx_4_1_to_virtual_5_1",
        "joint_other": "phalanx_4_1_to_virtual_5_1",
        "axis_m": [
          4.537561723341792e-33,
          6.661338147750935e-16,
          1.0
        ],
        "axis_other_aligned": [
          7.443474041670879e-18,
          6.948138782764427e-16,
          1.0
        ],
        "angle_rad": 2.9630243810175585e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "virtual_5_1_to_phalanx_5_1",
        "joint_other": "virtual_5_1_to_phalanx_5_1",
        "axis_m": [
          4.537561723341792e-33,
          6.661338147750935e-16,
          1.0
        ],
        "axis_other_aligned": [
          7.443474041670879e-18,
          6.948138782764427e-16,
          1.0
        ],
        "angle_rad": 2.9630243810175585e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "phalanx_5_1_to_virtual_6_1",
        "joint_other": "phalanx_5_1_to_virtual_6_1",
        "axis_m": [
          4.537561723341792e-33,
          6.661338147750935e-16,
          1.0
        ],
        "axis_other_aligned": [
          7.443474041670879e-18,
          6.948138782764427e-16,
          1.0
        ],
        "angle_rad": 2.9630243810175585e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "virtual_6_1_to_reverse_phalanx_1",
        "joint_other": "virtual_6_1_to_reverse_phalanx_1",
        "axis_m": [
          4.537561723341792e-33,
          6.661338147750935e-16,
          1.0
        ],
        "axis_other_aligned": [
          7.443474041670879e-18,
          6.948138782764427e-16,
          1.0
        ],
        "angle_rad": 2.9630243810175585e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "reverse_phalanx_1_to_virtual_7_1",
        "joint_other": "reverse_phalanx_1_to_virtual_7_1",
        "axis_m": [
          4.537561723341792e-33,
          6.661338147750935e-16,
          1.0
        ],
        "axis_other_aligned": [
          7.443474041670879e-18,
          6.948138782764427e-16,
          1.0
        ],
        "angle_rad": 2.9630243810175585e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "virtual_7_1_to_rollover_phalanx_1",
        "joint_other": "virtual_7_1_to_rollover_phalanx_1",
        "axis_m": [
          4.537561723341792e-33,
          6.661338147750935e-16,
          1.0
        ],
        "axis_other_aligned": [
          7.443474041670879e-18,
          6.948138782764427e-16,
          1.0
        ],
        "angle_rad": 2.9630243810175585e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "rollover_phalanx_1_to_virtual_8_1",
        "joint_other": "rollover_phalanx_1_to_virtual_8_1",
        "axis_m": [
          4.537561723341792e-33,
          6.661338147750935e-16,
          1.0
        ],
        "axis_other_aligned": [
          7.443474041670879e-18,
          6.948138782764427e-16,
          1.0
        ],
        "angle_rad": 2.9630243810175585e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "virtual_8_1_to_phalanx_6_1",
        "joint_other": "virtual_8_1_to_phalanx_6_1",
        "axis_m": [
          4.537561723341792e-33,
          6.661338147750935e-16,
          1.0
        ],
        "axis_other_aligned": [
          7.443474041670879e-18,
          6.948138782764427e-16,
          1.0
        ],
        "angle_rad": 2.9630243810175585e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "phalanx_6_1_to_virtual_9_1",
        "joint_other": "phalanx_6_1_to_virtual_9_1",
        "axis_m": [
          4.537561723341792e-33,
          6.661338147750935e-16,
          1.0
        ],
        "axis_other_aligned": [
          7.443474041670879e-18,
          6.948138782764427e-16,
          1.0
        ],
        "angle_rad": 2.9630243810175585e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "virtual_9_1_to_distal_phalanx_1",
        "joint_other": "virtual_9_1_to_distal_phalanx_1",
        "axis_m": [
          4.537561723341792e-33,
          6.661338147750935e-16,
          1.0
        ],
        "axis_other_aligned": [
          7.443474041670879e-18,
          6.948138782764427e-16,
          1.0
        ],
        "angle_rad": 2.9630243810175585e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "heel_phalanx_2_to_virtual_1_2",
        "joint_other": "heel_phalanx_2_to_virtual_1_2",
        "axis_m": [
          4.734643501393354e-33,
          6.661338147750934e-16,
          1.0
        ],
        "axis_other_aligned": [
          7.443474041670879e-18,
          6.948138782764426e-16,
          1.0
        ],
        "angle_rad": 2.9630243810175585e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "virtual_1_2_to_phalanx_1_2",
        "joint_other": "virtual_1_2_to_phalanx_1_2",
        "axis_m": [
          4.537561723341792e-33,
          6.661338147750935e-16,
          1.0
        ],
        "axis_other_aligned": [
          7.443474041670879e-18,
          6.948138782764427e-16,
          1.0
        ],
        "angle_rad": 2.9630243810175585e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "phalanx_1_2_to_virtual_2_2",
        "joint_other": "phalanx_1_2_to_virtual_2_2",
        "axis_m": [
          4.537561723341792e-33,
          6.661338147750935e-16,
          1.0
        ],
        "axis_other_aligned": [
          7.443474041670879e-18,
          6.948138782764427e-16,
          1.0
        ],
        "angle_rad": 2.9630243810175585e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "virtual_2_2_to_phalanx_2_2",
        "joint_other": "virtual_2_2_to_phalanx_2_2",
        "axis_m": [
          4.537561723341792e-33,
          6.661338147750935e-16,
          1.0
        ],
        "axis_other_aligned": [
          7.443474041670879e-18,
          6.948138782764427e-16,
          1.0
        ],
        "angle_rad": 2.9630243810175585e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "phalanx_2_2_to_virtual_3_2",
        "joint_other": "phalanx_2_2_to_virtual_3_2",
        "axis_m": [
          4.537561723341792e-33,
          6.661338147750935e-16,
          1.0
        ],
        "axis_other_aligned": [
          7.443474041670879e-18,
          6.948138782764427e-16,
          1.0
        ],
        "angle_rad": 2.9630243810175585e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "virtual_3_2_to_phalanx_3_2",
        "joint_other": "virtual_3_2_to_phalanx_3_2",
        "axis_m": [
          4.537561723341792e-33,
          6.661338147750935e-16,
          1.0
        ],
        "axis_other_aligned": [
          7.443474041670879e-18,
          6.948138782764427e-16,
          1.0
        ],
        "angle_rad": 2.9630243810175585e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "phalanx_3_2_to_virtual_4_2",
        "joint_other": "phalanx_3_2_to_virtual_4_2",
        "axis_m": [
          4.537561723341792e-33,
          6.661338147750935e-16,
          1.0
        ],
        "axis_other_aligned": [
          7.443474041670879e-18,
          6.948138782764427e-16,
          1.0
        ],
        "angle_rad": 2.9630243810175585e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "virtual_4_2_to_phalanx_4_2",
        "joint_other": "virtual_4_2_to_phalanx_4_2",
        "axis_m": [
          4.537561723341792e-33,
          6.661338147750935e-16,
          1.0
        ],
        "axis_other_aligned": [
          7.443474041670879e-18,
          6.948138782764427e-16,
          1.0
        ],
        "angle_rad": 2.9630243810175585e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "phalanx_4_2_to_virtual_5_2",
        "joint_other": "phalanx_4_2_to_virtual_5_2",
        "axis_m": [
          4.537561723341792e-33,
          6.661338147750935e-16,
          1.0
        ],
        "axis_other_aligned": [
          7.443474041670879e-18,
          6.948138782764427e-16,
          1.0
        ],
        "angle_rad": 2.9630243810175585e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "virtual_5_2_to_phalanx_5_2",
        "joint_other": "virtual_5_2_to_phalanx_5_2",
        "axis_m": [
          4.537561723341792e-33,
          6.661338147750935e-16,
          1.0
        ],
        "axis_other_aligned": [
          7.443474041670879e-18,
          6.948138782764427e-16,
          1.0
        ],
        "angle_rad": 2.9630243810175585e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "phalanx_5_2_to_virtual_6_2",
        "joint_other": "phalanx_5_2_to_virtual_6_2",
        "axis_m": [
          4.537561723341792e-33,
          6.661338147750935e-16,
          1.0
        ],
        "axis_other_aligned": [
          7.443474041670879e-18,
          6.948138782764427e-16,
          1.0
        ],
        "angle_rad": 2.9630243810175585e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "virtual_6_2_to_reverse_phalanx_2",
        "joint_other": "virtual_6_2_to_reverse_phalanx_2",
        "axis_m": [
          4.537561723341792e-33,
          6.661338147750935e-16,
          1.0
        ],
        "axis_other_aligned": [
          7.443474041670879e-18,
          6.948138782764427e-16,
          1.0
        ],
        "angle_rad": 2.9630243810175585e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "reverse_phalanx_2_to_virtual_7_2",
        "joint_other": "reverse_phalanx_2_to_virtual_7_2",
        "axis_m": [
          4.537561723341792e-33,
          6.661338147750935e-16,
          1.0
        ],
        "axis_other_aligned": [
          7.443474041670879e-18,
          6.948138782764427e-16,
          1.0
        ],
        "angle_rad": 2.9630243810175585e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "virtual_7_2_to_rollover_phalanx_2",
        "joint_other": "virtual_7_2_to_rollover_phalanx_2",
        "axis_m": [
          4.537561723341792e-33,
          6.661338147750935e-16,
          1.0
        ],
        "axis_other_aligned": [
          7.443474041670879e-18,
          6.948138782764427e-16,
          1.0
        ],
        "angle_rad": 2.9630243810175585e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "rollover_phalanx_2_to_virtual_8_2",
        "joint_other": "rollover_phalanx_2_to_virtual_8_2",
        "axis_m": [
          4.537561723341792e-33,
          6.661338147750935e-16,
          1.0
        ],
        "axis_other_aligned": [
          7.443474041670879e-18,
          6.948138782764427e-16,
          1.0
        ],
        "angle_rad": 2.9630243810175585e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "virtual_8_2_to_phalanx_6_2",
        "joint_other": "virtual_8_2_to_phalanx_6_2",
        "axis_m": [
          4.537561723341792e-33,
          6.661338147750935e-16,
          1.0
        ],
        "axis_other_aligned": [
          7.443474041670879e-18,
          6.948138782764427e-16,
          1.0
        ],
        "angle_rad": 2.9630243810175585e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "phalanx_6_2_to_virtual_9_2",
        "joint_other": "phalanx_6_2_to_virtual_9_2",
        "axis_m": [
          4.537561723341792e-33,
          6.661338147750935e-16,
          1.0
        ],
        "axis_other_aligned": [
          7.443474041670879e-18,
          6.948138782764427e-16,
          1.0
        ],
        "angle_rad": 2.9630243810175585e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "virtual_9_2_to_distal_phalanx_2",
        "joint_other": "virtual_9_2_to_distal_phalanx_2",
        "axis_m": [
          4.537561723341792e-33,
          6.661338147750935e-16,
          1.0
        ],
        "axis_other_aligned": [
          7.443474041670879e-18,
          6.948138782764427e-16,
          1.0
        ],
        "angle_rad": 2.9630243810175585e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "heel_phalanx_3_to_virtual_1_3",
        "joint_other": "heel_phalanx_3_to_virtual_1_3",
        "axis_m": [
          4.734643501393354e-33,
          6.661338147750934e-16,
          1.0
        ],
        "axis_other_aligned": [
          7.443474041670879e-18,
          6.948138782764426e-16,
          1.0
        ],
        "angle_rad": 2.9630243810175585e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "virtual_1_3_to_phalanx_1_3",
        "joint_other": "virtual_1_3_to_phalanx_1_3",
        "axis_m": [
          4.537561723341792e-33,
          6.661338147750935e-16,
          1.0
        ],
        "axis_other_aligned": [
          7.443474041670879e-18,
          6.948138782764427e-16,
          1.0
        ],
        "angle_rad": 2.9630243810175585e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "phalanx_1_3_to_virtual_2_3",
        "joint_other": "phalanx_1_3_to_virtual_2_3",
        "axis_m": [
          4.537561723341792e-33,
          6.661338147750935e-16,
          1.0
        ],
        "axis_other_aligned": [
          7.443474041670879e-18,
          6.948138782764427e-16,
          1.0
        ],
        "angle_rad": 2.9630243810175585e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "virtual_2_3_to_phalanx_2_3",
        "joint_other": "virtual_2_3_to_phalanx_2_3",
        "axis_m": [
          4.537561723341792e-33,
          6.661338147750935e-16,
          1.0
        ],
        "axis_other_aligned": [
          7.443474041670879e-18,
          6.948138782764427e-16,
          1.0
        ],
        "angle_rad": 2.9630243810175585e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "phalanx_2_3_to_virtual_3_3",
        "joint_other": "phalanx_2_3_to_virtual_3_3",
        "axis_m": [
          4.537561723341792e-33,
          6.661338147750935e-16,
          1.0
        ],
        "axis_other_aligned": [
          7.443474041670879e-18,
          6.948138782764427e-16,
          1.0
        ],
        "angle_rad": 2.9630243810175585e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "virtual_3_3_to_phalanx_3_3",
        "joint_other": "virtual_3_3_to_phalanx_3_3",
        "axis_m": [
          4.537561723341792e-33,
          6.661338147750935e-16,
          1.0
        ],
        "axis_other_aligned": [
          7.443474041670879e-18,
          6.948138782764427e-16,
          1.0
        ],
        "angle_rad": 2.9630243810175585e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "phalanx_3_3_to_virtual_4_3",
        "joint_other": "phalanx_3_3_to_virtual_4_3",
        "axis_m": [
          4.537561723341792e-33,
          6.661338147750935e-16,
          1.0
        ],
        "axis_other_aligned": [
          7.443474041670879e-18,
          6.948138782764427e-16,
          1.0
        ],
        "angle_rad": 2.9630243810175585e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "virtual_4_3_to_phalanx_4_3",
        "joint_other": "virtual_4_3_to_phalanx_4_3",
        "axis_m": [
          4.537561723341792e-33,
          6.661338147750935e-16,
          1.0
        ],
        "axis_other_aligned": [
          7.443474041670879e-18,
          6.948138782764427e-16,
          1.0
        ],
        "angle_rad": 2.9630243810175585e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "phalanx_4_3_to_virtual_5_3",
        "joint_other": "phalanx_4_3_to_virtual_5_3",
        "axis_m": [
          4.537561723341792e-33,
          6.661338147750935e-16,
          1.0
        ],
        "axis_other_aligned": [
          7.443474041670879e-18,
          6.948138782764427e-16,
          1.0
        ],
        "angle_rad": 2.9630243810175585e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "virtual_5_3_to_phalanx_5_3",
        "joint_other": "virtual_5_3_to_phalanx_5_3",
        "axis_m": [
          4.537561723341792e-33,
          6.661338147750935e-16,
          1.0
        ],
        "axis_other_aligned": [
          7.443474041670879e-18,
          6.948138782764427e-16,
          1.0
        ],
        "angle_rad": 2.9630243810175585e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "phalanx_5_3_to_virtual_6_3",
        "joint_other": "phalanx_5_3_to_virtual_6_3",
        "axis_m": [
          4.537561723341792e-33,
          6.661338147750935e-16,
          1.0
        ],
        "axis_other_aligned": [
          7.443474041670879e-18,
          6.948138782764427e-16,
          1.0
        ],
        "angle_rad": 2.9630243810175585e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "virtual_6_3_to_reverse_phalanx_3",
        "joint_other": "virtual_6_3_to_reverse_phalanx_3",
        "axis_m": [
          4.537561723341792e-33,
          6.661338147750935e-16,
          1.0
        ],
        "axis_other_aligned": [
          7.443474041670879e-18,
          6.948138782764427e-16,
          1.0
        ],
        "angle_rad": 2.9630243810175585e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "reverse_phalanx_3_to_virtual_7_3",
        "joint_other": "reverse_phalanx_3_to_virtual_7_3",
        "axis_m": [
          4.537561723341792e-33,
          6.661338147750935e-16,
          1.0
        ],
        "axis_other_aligned": [
          7.443474041670879e-18,
          6.948138782764427e-16,
          1.0
        ],
        "angle_rad": 2.9630243810175585e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "virtual_7_3_to_rollover_phalanx_3",
        "joint_other": "virtual_7_3_to_rollover_phalanx_3",
        "axis_m": [
          4.537561723341792e-33,
          6.661338147750935e-16,
          1.0
        ],
        "axis_other_aligned": [
          7.443474041670879e-18,
          6.948138782764427e-16,
          1.0
        ],
        "angle_rad": 2.9630243810175585e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "rollover_phalanx_3_to_virtual_8_3",
        "joint_other": "rollover_phalanx_3_to_virtual_8_3",
        "axis_m": [
          4.537561723341792e-33,
          6.661338147750935e-16,
          1.0
        ],
        "axis_other_aligned": [
          7.443474041670879e-18,
          6.948138782764427e-16,
          1.0
        ],
        "angle_rad": 2.9630243810175585e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "virtual_8_3_to_phalanx_6_3",
        "joint_other": "virtual_8_3_to_phalanx_6_3",
        "axis_m": [
          4.537561723341792e-33,
          6.661338147750935e-16,
          1.0
        ],
        "axis_other_aligned": [
          7.443474041670879e-18,
          6.948138782764427e-16,
          1.0
        ],
        "angle_rad": 2.9630243810175585e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "phalanx_6_3_to_virtual_9_3",
        "joint_other": "phalanx_6_3_to_virtual_9_3",
        "axis_m": [
          4.537561723341792e-33,
          6.661338147750935e-16,
          1.0
        ],
        "axis_other_aligned": [
          7.443474041670879e-18,
          6.948138782764427e-16,
          1.0
        ],
        "angle_rad": 2.9630243810175585e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "virtual_9_3_to_distal_phalanx_3",
        "joint_other": "virtual_9_3_to_distal_phalanx_3",
        "axis_m": [
          4.537561723341792e-33,
          6.661338147750935e-16,
          1.0
        ],
        "axis_other_aligned": [
          7.443474041670879e-18,
          6.948138782764427e-16,
          1.0
        ],
        "angle_rad": 2.9630243810175585e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "heel_phalanx_4_to_virtual_1_4",
        "joint_other": "heel_phalanx_4_to_virtual_1_4",
        "axis_m": [
          4.734643501393354e-33,
          6.661338147750934e-16,
          1.0
        ],
        "axis_other_aligned": [
          7.443474041670879e-18,
          6.948138782764426e-16,
          1.0
        ],
        "angle_rad": 2.9630243810175585e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "virtual_1_4_to_phalanx_1_4",
        "joint_other": "virtual_1_4_to_phalanx_1_4",
        "axis_m": [
          4.537561723341792e-33,
          6.661338147750935e-16,
          1.0
        ],
        "axis_other_aligned": [
          7.443474041670879e-18,
          6.948138782764427e-16,
          1.0
        ],
        "angle_rad": 2.9630243810175585e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "phalanx_1_4_to_virtual_2_4",
        "joint_other": "phalanx_1_4_to_virtual_2_4",
        "axis_m": [
          4.537561723341792e-33,
          6.661338147750935e-16,
          1.0
        ],
        "axis_other_aligned": [
          7.443474041670879e-18,
          6.948138782764427e-16,
          1.0
        ],
        "angle_rad": 2.9630243810175585e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "virtual_2_4_to_phalanx_2_4",
        "joint_other": "virtual_2_4_to_phalanx_2_4",
        "axis_m": [
          4.537561723341792e-33,
          6.661338147750935e-16,
          1.0
        ],
        "axis_other_aligned": [
          7.443474041670879e-18,
          6.948138782764427e-16,
          1.0
        ],
        "angle_rad": 2.9630243810175585e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "phalanx_2_4_to_virtual_3_4",
        "joint_other": "phalanx_2_4_to_virtual_3_4",
        "axis_m": [
          4.537561723341792e-33,
          6.661338147750935e-16,
          1.0
        ],
        "axis_other_aligned": [
          7.443474041670879e-18,
          6.948138782764427e-16,
          1.0
        ],
        "angle_rad": 2.9630243810175585e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "virtual_3_4_to_phalanx_3_4",
        "joint_other": "virtual_3_4_to_phalanx_3_4",
        "axis_m": [
          4.537561723341792e-33,
          6.661338147750935e-16,
          1.0
        ],
        "axis_other_aligned": [
          7.443474041670879e-18,
          6.948138782764427e-16,
          1.0
        ],
        "angle_rad": 2.9630243810175585e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "phalanx_3_4_to_virtual_4_4",
        "joint_other": "phalanx_3_4_to_virtual_4_4",
        "axis_m": [
          4.537561723341792e-33,
          6.661338147750935e-16,
          1.0
        ],
        "axis_other_aligned": [
          7.443474041670879e-18,
          6.948138782764427e-16,
          1.0
        ],
        "angle_rad": 2.9630243810175585e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "virtual_4_4_to_phalanx_4_4",
        "joint_other": "virtual_4_4_to_phalanx_4_4",
        "axis_m": [
          4.537561723341792e-33,
          6.661338147750935e-16,
          1.0
        ],
        "axis_other_aligned": [
          7.443474041670879e-18,
          6.948138782764427e-16,
          1.0
        ],
        "angle_rad": 2.9630243810175585e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "phalanx_4_4_to_virtual_5_4",
        "joint_other": "phalanx_4_4_to_virtual_5_4",
        "axis_m": [
          4.537561723341792e-33,
          6.661338147750935e-16,
          1.0
        ],
        "axis_other_aligned": [
          7.443474041670879e-18,
          6.948138782764427e-16,
          1.0
        ],
        "angle_rad": 2.9630243810175585e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "virtual_5_4_to_phalanx_5_4",
        "joint_other": "virtual_5_4_to_phalanx_5_4",
        "axis_m": [
          4.537561723341792e-33,
          6.661338147750935e-16,
          1.0
        ],
        "axis_other_aligned": [
          7.443474041670879e-18,
          6.948138782764427e-16,
          1.0
        ],
        "angle_rad": 2.9630243810175585e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "phalanx_5_4_to_virtual_6_4",
        "joint_other": "phalanx_5_4_to_virtual_6_4",
        "axis_m": [
          4.537561723341792e-33,
          6.661338147750935e-16,
          1.0
        ],
        "axis_other_aligned": [
          7.443474041670879e-18,
          6.948138782764427e-16,
          1.0
        ],
        "angle_rad": 2.9630243810175585e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "virtual_6_4_to_reverse_phalanx_4",
        "joint_other": "virtual_6_4_to_reverse_phalanx_4",
        "axis_m": [
          4.537561723341792e-33,
          6.661338147750935e-16,
          1.0
        ],
        "axis_other_aligned": [
          7.443474041670879e-18,
          6.948138782764427e-16,
          1.0
        ],
        "angle_rad": 2.9630243810175585e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "reverse_phalanx_4_to_virtual_7_4",
        "joint_other": "reverse_phalanx_4_to_virtual_7_4",
        "axis_m": [
          4.537561723341792e-33,
          6.661338147750935e-16,
          1.0
        ],
        "axis_other_aligned": [
          7.443474041670879e-18,
          6.948138782764427e-16,
          1.0
        ],
        "angle_rad": 2.9630243810175585e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "virtual_7_4_to_rollover_phalanx_4",
        "joint_other": "virtual_7_4_to_rollover_phalanx_4",
        "axis_m": [
          4.537561723341792e-33,
          6.661338147750935e-16,
          1.0
        ],
        "axis_other_aligned": [
          7.443474041670879e-18,
          6.948138782764427e-16,
          1.0
        ],
        "angle_rad": 2.9630243810175585e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "rollover_phalanx_4_to_virtual_8_4",
        "joint_other": "rollover_phalanx_4_to_virtual_8_4",
        "axis_m": [
          4.537561723341792e-33,
          6.661338147750935e-16,
          1.0
        ],
        "axis_other_aligned": [
          7.443474041670879e-18,
          6.948138782764427e-16,
          1.0
        ],
        "angle_rad": 2.9630243810175585e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "virtual_8_4_to_phalanx_6_4",
        "joint_other": "virtual_8_4_to_phalanx_6_4",
        "axis_m": [
          4.537561723341792e-33,
          6.661338147750935e-16,
          1.0
        ],
        "axis_other_aligned": [
          7.443474041670879e-18,
          6.948138782764427e-16,
          1.0
        ],
        "angle_rad": 2.9630243810175585e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "phalanx_6_4_to_virtual_9_4",
        "joint_other": "phalanx_6_4_to_virtual_9_4",
        "axis_m": [
          4.537561723341792e-33,
          6.661338147750935e-16,
          1.0
        ],
        "axis_other_aligned": [
          7.443474041670879e-18,
          6.948138782764427e-16,
          1.0
        ],
        "angle_rad": 2.9630243810175585e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "virtual_9_4_to_distal_phalanx_4",
        "joint_other": "virtual_9_4_to_distal_phalanx_4",
        "axis_m": [
          4.537561723341792e-33,
          6.661338147750935e-16,
          1.0
        ],
        "axis_other_aligned": [
          7.443474041670879e-18,
          6.948138782764427e-16,
          1.0
        ],
        "angle_rad": 2.9630243810175585e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "heel_phalanx_5_to_virtual_1_5",
        "joint_other": "heel_phalanx_5_to_virtual_1_5",
        "axis_m": [
          4.734643501393354e-33,
          6.661338147750934e-16,
          1.0
        ],
        "axis_other_aligned": [
          7.443474041670879e-18,
          6.948138782764426e-16,
          1.0
        ],
        "angle_rad": 2.9630243810175585e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "virtual_1_5_to_phalanx_1_5",
        "joint_other": "virtual_1_5_to_phalanx_1_5",
        "axis_m": [
          4.537561723341792e-33,
          6.661338147750935e-16,
          1.0
        ],
        "axis_other_aligned": [
          7.443474041670879e-18,
          6.948138782764427e-16,
          1.0
        ],
        "angle_rad": 2.9630243810175585e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "phalanx_1_5_to_virtual_2_5",
        "joint_other": "phalanx_1_5_to_virtual_2_5",
        "axis_m": [
          4.537561723341792e-33,
          6.661338147750935e-16,
          1.0
        ],
        "axis_other_aligned": [
          7.443474041670879e-18,
          6.948138782764427e-16,
          1.0
        ],
        "angle_rad": 2.9630243810175585e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "virtual_2_5_to_phalanx_2_5",
        "joint_other": "virtual_2_5_to_phalanx_2_5",
        "axis_m": [
          4.537561723341792e-33,
          6.661338147750935e-16,
          1.0
        ],
        "axis_other_aligned": [
          7.443474041670879e-18,
          6.948138782764427e-16,
          1.0
        ],
        "angle_rad": 2.9630243810175585e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "phalanx_2_5_to_virtual_3_5",
        "joint_other": "phalanx_2_5_to_virtual_3_5",
        "axis_m": [
          4.537561723341792e-33,
          6.661338147750935e-16,
          1.0
        ],
        "axis_other_aligned": [
          7.443474041670879e-18,
          6.948138782764427e-16,
          1.0
        ],
        "angle_rad": 2.9630243810175585e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "virtual_3_5_to_phalanx_3_5",
        "joint_other": "virtual_3_5_to_phalanx_3_5",
        "axis_m": [
          4.537561723341792e-33,
          6.661338147750935e-16,
          1.0
        ],
        "axis_other_aligned": [
          7.443474041670879e-18,
          6.948138782764427e-16,
          1.0
        ],
        "angle_rad": 2.9630243810175585e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "phalanx_3_5_to_virtual_4_5",
        "joint_other": "phalanx_3_5_to_virtual_4_5",
        "axis_m": [
          4.537561723341792e-33,
          6.661338147750935e-16,
          1.0
        ],
        "axis_other_aligned": [
          7.443474041670879e-18,
          6.948138782764427e-16,
          1.0
        ],
        "angle_rad": 2.9630243810175585e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "virtual_4_5_to_phalanx_4_5",
        "joint_other": "virtual_4_5_to_phalanx_4_5",
        "axis_m": [
          4.537561723341792e-33,
          6.661338147750935e-16,
          1.0
        ],
        "axis_other_aligned": [
          7.443474041670879e-18,
          6.948138782764427e-16,
          1.0
        ],
        "angle_rad": 2.9630243810175585e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "phalanx_4_5_to_virtual_5_5",
        "joint_other": "phalanx_4_5_to_virtual_5_5",
        "axis_m": [
          4.537561723341792e-33,
          6.661338147750935e-16,
          1.0
        ],
        "axis_other_aligned": [
          7.443474041670879e-18,
          6.948138782764427e-16,
          1.0
        ],
        "angle_rad": 2.9630243810175585e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "virtual_5_5_to_phalanx_5_5",
        "joint_other": "virtual_5_5_to_phalanx_5_5",
        "axis_m": [
          4.537561723341792e-33,
          6.661338147750935e-16,
          1.0
        ],
        "axis_other_aligned": [
          7.443474041670879e-18,
          6.948138782764427e-16,
          1.0
        ],
        "angle_rad": 2.9630243810175585e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "phalanx_5_5_to_virtual_6_5",
        "joint_other": "phalanx_5_5_to_virtual_6_5",
        "axis_m": [
          4.537561723341792e-33,
          6.661338147750935e-16,
          1.0
        ],
        "axis_other_aligned": [
          7.443474041670879e-18,
          6.948138782764427e-16,
          1.0
        ],
        "angle_rad": 2.9630243810175585e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "virtual_6_5_to_reverse_phalanx_5",
        "joint_other": "virtual_6_5_to_reverse_phalanx_5",
        "axis_m": [
          4.537561723341792e-33,
          6.661338147750935e-16,
          1.0
        ],
        "axis_other_aligned": [
          7.443474041670879e-18,
          6.948138782764427e-16,
          1.0
        ],
        "angle_rad": 2.9630243810175585e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "reverse_phalanx_5_to_virtual_7_5",
        "joint_other": "reverse_phalanx_5_to_virtual_7_5",
        "axis_m": [
          4.537561723341792e-33,
          6.661338147750935e-16,
          1.0
        ],
        "axis_other_aligned": [
          7.443474041670879e-18,
          6.948138782764427e-16,
          1.0
        ],
        "angle_rad": 2.9630243810175585e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "virtual_7_5_to_rollover_phalanx_5",
        "joint_other": "virtual_7_5_to_rollover_phalanx_5",
        "axis_m": [
          4.537561723341792e-33,
          6.661338147750935e-16,
          1.0
        ],
        "axis_other_aligned": [
          7.443474041670879e-18,
          6.948138782764427e-16,
          1.0
        ],
        "angle_rad": 2.9630243810175585e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "rollover_phalanx_5_to_virtual_8_5",
        "joint_other": "rollover_phalanx_5_to_virtual_8_5",
        "axis_m": [
          4.537561723341792e-33,
          6.661338147750935e-16,
          1.0
        ],
        "axis_other_aligned": [
          7.443474041670879e-18,
          6.948138782764427e-16,
          1.0
        ],
        "angle_rad": 2.9630243810175585e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "virtual_8_5_to_phalanx_6_5",
        "joint_other": "virtual_8_5_to_phalanx_6_5",
        "axis_m": [
          4.537561723341792e-33,
          6.661338147750935e-16,
          1.0
        ],
        "axis_other_aligned": [
          7.443474041670879e-18,
          6.948138782764427e-16,
          1.0
        ],
        "angle_rad": 2.9630243810175585e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "phalanx_6_5_to_virtual_9_5",
        "joint_other": "phalanx_6_5_to_virtual_9_5",
        "axis_m": [
          4.537561723341792e-33,
          6.661338147750935e-16,
          1.0
        ],
        "axis_other_aligned": [
          7.443474041670879e-18,
          6.948138782764427e-16,
          1.0
        ],
        "angle_rad": 2.9630243810175585e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "virtual_9_5_to_distal_phalanx_5",
        "joint_other": "virtual_9_5_to_distal_phalanx_5",
        "axis_m": [
          4.537561723341792e-33,
          6.661338147750935e-16,
          1.0
        ],
        "axis_other_aligned": [
          7.443474041670879e-18,
          6.948138782764427e-16,
          1.0
        ],
        "angle_rad": 2.9630243810175585e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "cube_to_frontal_arch",
        "joint_other": "cube_to_frontal_arch",
        "axis_m": [
          1.0336302097132477e-17,
          4.440892098500624e-16,
          1.0
        ],
        "axis_other_aligned": [
          1.777977613880334e-17,
          4.727692733514118e-16,
          1.0
        ],
        "angle_rad": 2.963024381017577e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      }
    ],
    "axis_disagreements": [],
    "com_eligible": true,
    "covariance_singular_values": [
      0.18460232913673458,
      0.030637874809684325,
      0.019076466542020994
    ],
    "origin_residuals_m": {
      "attachment_cube": 1.794968653255206e-17,
      "posterior_arch": 1.794968653255206e-17,
      "heel": 2.7756908414657696e-17,
      "phalanx_1_1": 2.5018537765542006e-17,
      "phalanx_2_1": 1.962615573354719e-17,
      "phalanx_3_1": 2.2551405187698492e-17,
      "phalanx_4_1": 2.110382192020081e-17,
      "phalanx_5_1": 2.0816681711721685e-17,
      "reverse_phalanx_1": 2.0816681711721685e-17,
      "rollover_phalanx_1": 2.5018537765542006e-17,
      "phalanx_6_1": 2.0816681711721685e-17,
      "distal_phalanx_1": 2.0816681711721685e-17,
      "phalanx_1_2": 2.1942709178604383e-17,
      "phalanx_2_2": 1.5515838457795457e-17,
      "phalanx_3_2": 1.1107649934270853e-17,
      "phalanx_4_2": 7.757919228897728e-18,
      "phalanx_5_2": 6.938893903907228e-18,
      "reverse_phalanx_2": 6.938893903907228e-18,
      "rollover_phalanx_2": 1.5515838457795457e-17,
      "phalanx_6_2": 6.938893903907228e-18,
      "distal_phalanx_2": 6.938893903907228e-18,
      "phalanx_1_3": 2.0901639266105137e-17,
      "phalanx_2_3": 1.3972120070117818e-17,
      "phalanx_3_3": 8.779447576003984e-18,
      "phalanx_4_3": 3.6388319680924014e-18,
      "phalanx_5_3": 8.355051001106803e-19,
      "reverse_phalanx_3": 5.737244855640548e-19,
      "rollover_phalanx_3": 1.3880954285428108e-17,
      "phalanx_6_3": 8.429678645541644e-20,
      "distal_phalanx_3": 3.460774010020419e-19,
      "phalanx_1_4": 2.3273757686693185e-17,
      "phalanx_2_4": 1.734723475976807e-17,
      "phalanx_3_4": 1.3548623466035522e-17,
      "phalanx_4_4": 1.0971354589302191e-17,
      "phalanx_5_4": 1.0408340855860843e-17,
      "reverse_phalanx_4": 1.0408340855860843e-17,
      "rollover_phalanx_4": 1.734723475976807e-17,
      "phalanx_6_4": 1.0408340855860843e-17,
      "distal_phalanx_4": 6.938893903907228e-18,
      "phalanx_1_5": 2.5018537765542006e-17,
      "phalanx_2_5": 1.962615573354719e-17,
      "phalanx_3_5": 1.6365348541700844e-17,
      "phalanx_4_5": 1.4304896245381992e-17,
      "phalanx_5_5": 1.3877787807814457e-17,
      "reverse_phalanx_5": 1.3877787807814457e-17,
      "rollover_phalanx_5": 1.962615573354719e-17,
      "phalanx_6_5": 1.3877787807814457e-17,
      "distal_phalanx_5": 1.3877787807814457e-17,
      "frontal_arch": 1.794968653255206e-17
    },
    "reason": "Unique proper rigid fit and matched signed axes meet the configured thresholds"
  },
  "M/S": {
    "status": "consistent",
    "matched_body_origins": 49,
    "position_threshold_m": 0.005,
    "axis_threshold_rad": 0.005,
    "residual_definition": "maximum Euclidean residual over matched body origins; Kabsch minimizes RMS, which is also recorded",
    "coordinate_frames": "each snapshot registered to its matched report anchor",
    "anchor_m": "attachment_cube",
    "anchor_other": "attachment_cube",
    "rotation_other_to_m": [
      [
        1.0000000000000002,
        3.9204323500495214e-17,
        7.443474041670852e-18
      ],
      [
        1.1222604088474022e-17,
        1.0,
        2.8680063501349526e-17
      ],
      [
        1.1899118843028411e-17,
        -1.5157146371347352e-16,
        1.0000000000000004
      ]
    ],
    "translation_other_to_m": [
      -1.3877787807814457e-17,
      0.0,
      1.1384122811097797e-17
    ],
    "rms_residual_m": 1.6147560902450608e-17,
    "max_residual_m": 2.7756908414657696e-17,
    "fit_rank": 3,
    "axis_checks": [
      {
        "joint_m": "posterior_arch_to_heel",
        "joint_other": "posterior_arch_to_heel",
        "axis_m": [
          1.827910301094998e-17,
          4.440892098500624e-16,
          1.0
        ],
        "axis_other_aligned": [
          2.5722577052620843e-17,
          4.727692733514118e-16,
          1.0
        ],
        "angle_rad": 2.963024381017577e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "heel_phalanx_1_to_virtual_1_1",
        "joint_other": "heel_phalanx_1_to_virtual_1_1",
        "axis_m": [
          4.734643501393354e-33,
          6.661338147750934e-16,
          1.0
        ],
        "axis_other_aligned": [
          7.443474041670879e-18,
          6.948138782764426e-16,
          1.0
        ],
        "angle_rad": 2.9630243810175585e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "virtual_1_1_to_phalanx_1_1",
        "joint_other": "virtual_1_1_to_phalanx_1_1",
        "axis_m": [
          4.537561723341792e-33,
          6.661338147750935e-16,
          1.0
        ],
        "axis_other_aligned": [
          7.443474041670879e-18,
          6.948138782764427e-16,
          1.0
        ],
        "angle_rad": 2.9630243810175585e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "phalanx_1_1_to_virtual_2_1",
        "joint_other": "phalanx_1_1_to_virtual_2_1",
        "axis_m": [
          4.537561723341792e-33,
          6.661338147750935e-16,
          1.0
        ],
        "axis_other_aligned": [
          7.443474041670879e-18,
          6.948138782764427e-16,
          1.0
        ],
        "angle_rad": 2.9630243810175585e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "virtual_2_1_to_phalanx_2_1",
        "joint_other": "virtual_2_1_to_phalanx_2_1",
        "axis_m": [
          4.537561723341792e-33,
          6.661338147750935e-16,
          1.0
        ],
        "axis_other_aligned": [
          7.443474041670879e-18,
          6.948138782764427e-16,
          1.0
        ],
        "angle_rad": 2.9630243810175585e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "phalanx_2_1_to_virtual_3_1",
        "joint_other": "phalanx_2_1_to_virtual_3_1",
        "axis_m": [
          4.537561723341792e-33,
          6.661338147750935e-16,
          1.0
        ],
        "axis_other_aligned": [
          7.443474041670879e-18,
          6.948138782764427e-16,
          1.0
        ],
        "angle_rad": 2.9630243810175585e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "virtual_3_1_to_phalanx_3_1",
        "joint_other": "virtual_3_1_to_phalanx_3_1",
        "axis_m": [
          4.537561723341792e-33,
          6.661338147750935e-16,
          1.0
        ],
        "axis_other_aligned": [
          7.443474041670879e-18,
          6.948138782764427e-16,
          1.0
        ],
        "angle_rad": 2.9630243810175585e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "phalanx_3_1_to_virtual_4_1",
        "joint_other": "phalanx_3_1_to_virtual_4_1",
        "axis_m": [
          4.537561723341792e-33,
          6.661338147750935e-16,
          1.0
        ],
        "axis_other_aligned": [
          7.443474041670879e-18,
          6.948138782764427e-16,
          1.0
        ],
        "angle_rad": 2.9630243810175585e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "virtual_4_1_to_phalanx_4_1",
        "joint_other": "virtual_4_1_to_phalanx_4_1",
        "axis_m": [
          4.537561723341792e-33,
          6.661338147750935e-16,
          1.0
        ],
        "axis_other_aligned": [
          7.443474041670879e-18,
          6.948138782764427e-16,
          1.0
        ],
        "angle_rad": 2.9630243810175585e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "phalanx_4_1_to_virtual_5_1",
        "joint_other": "phalanx_4_1_to_virtual_5_1",
        "axis_m": [
          4.537561723341792e-33,
          6.661338147750935e-16,
          1.0
        ],
        "axis_other_aligned": [
          7.443474041670879e-18,
          6.948138782764427e-16,
          1.0
        ],
        "angle_rad": 2.9630243810175585e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "virtual_5_1_to_phalanx_5_1",
        "joint_other": "virtual_5_1_to_phalanx_5_1",
        "axis_m": [
          4.537561723341792e-33,
          6.661338147750935e-16,
          1.0
        ],
        "axis_other_aligned": [
          7.443474041670879e-18,
          6.948138782764427e-16,
          1.0
        ],
        "angle_rad": 2.9630243810175585e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "phalanx_5_1_to_virtual_6_1",
        "joint_other": "phalanx_5_1_to_virtual_6_1",
        "axis_m": [
          4.537561723341792e-33,
          6.661338147750935e-16,
          1.0
        ],
        "axis_other_aligned": [
          7.443474041670879e-18,
          6.948138782764427e-16,
          1.0
        ],
        "angle_rad": 2.9630243810175585e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "virtual_6_1_to_reverse_phalanx_1",
        "joint_other": "virtual_6_1_to_reverse_phalanx_1",
        "axis_m": [
          4.537561723341792e-33,
          6.661338147750935e-16,
          1.0
        ],
        "axis_other_aligned": [
          7.443474041670879e-18,
          6.948138782764427e-16,
          1.0
        ],
        "angle_rad": 2.9630243810175585e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "reverse_phalanx_1_to_virtual_7_1",
        "joint_other": "reverse_phalanx_1_to_virtual_7_1",
        "axis_m": [
          4.537561723341792e-33,
          6.661338147750935e-16,
          1.0
        ],
        "axis_other_aligned": [
          7.443474041670879e-18,
          6.948138782764427e-16,
          1.0
        ],
        "angle_rad": 2.9630243810175585e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "virtual_7_1_to_rollover_phalanx_1",
        "joint_other": "virtual_7_1_to_rollover_phalanx_1",
        "axis_m": [
          4.537561723341792e-33,
          6.661338147750935e-16,
          1.0
        ],
        "axis_other_aligned": [
          7.443474041670879e-18,
          6.948138782764427e-16,
          1.0
        ],
        "angle_rad": 2.9630243810175585e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "rollover_phalanx_1_to_virtual_8_1",
        "joint_other": "rollover_phalanx_1_to_virtual_8_1",
        "axis_m": [
          4.537561723341792e-33,
          6.661338147750935e-16,
          1.0
        ],
        "axis_other_aligned": [
          7.443474041670879e-18,
          6.948138782764427e-16,
          1.0
        ],
        "angle_rad": 2.9630243810175585e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "virtual_8_1_to_phalanx_6_1",
        "joint_other": "virtual_8_1_to_phalanx_6_1",
        "axis_m": [
          4.537561723341792e-33,
          6.661338147750935e-16,
          1.0
        ],
        "axis_other_aligned": [
          7.443474041670879e-18,
          6.948138782764427e-16,
          1.0
        ],
        "angle_rad": 2.9630243810175585e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "phalanx_6_1_to_virtual_9_1",
        "joint_other": "phalanx_6_1_to_virtual_9_1",
        "axis_m": [
          4.537561723341792e-33,
          6.661338147750935e-16,
          1.0
        ],
        "axis_other_aligned": [
          7.443474041670879e-18,
          6.948138782764427e-16,
          1.0
        ],
        "angle_rad": 2.9630243810175585e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "virtual_9_1_to_distal_phalanx_1",
        "joint_other": "virtual_9_1_to_distal_phalanx_1",
        "axis_m": [
          4.537561723341792e-33,
          6.661338147750935e-16,
          1.0
        ],
        "axis_other_aligned": [
          7.443474041670879e-18,
          6.948138782764427e-16,
          1.0
        ],
        "angle_rad": 2.9630243810175585e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "heel_phalanx_2_to_virtual_1_2",
        "joint_other": "heel_phalanx_2_to_virtual_1_2",
        "axis_m": [
          4.734643501393354e-33,
          6.661338147750934e-16,
          1.0
        ],
        "axis_other_aligned": [
          7.443474041670879e-18,
          6.948138782764426e-16,
          1.0
        ],
        "angle_rad": 2.9630243810175585e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "virtual_1_2_to_phalanx_1_2",
        "joint_other": "virtual_1_2_to_phalanx_1_2",
        "axis_m": [
          4.537561723341792e-33,
          6.661338147750935e-16,
          1.0
        ],
        "axis_other_aligned": [
          7.443474041670879e-18,
          6.948138782764427e-16,
          1.0
        ],
        "angle_rad": 2.9630243810175585e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "phalanx_1_2_to_virtual_2_2",
        "joint_other": "phalanx_1_2_to_virtual_2_2",
        "axis_m": [
          4.537561723341792e-33,
          6.661338147750935e-16,
          1.0
        ],
        "axis_other_aligned": [
          7.443474041670879e-18,
          6.948138782764427e-16,
          1.0
        ],
        "angle_rad": 2.9630243810175585e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "virtual_2_2_to_phalanx_2_2",
        "joint_other": "virtual_2_2_to_phalanx_2_2",
        "axis_m": [
          4.537561723341792e-33,
          6.661338147750935e-16,
          1.0
        ],
        "axis_other_aligned": [
          7.443474041670879e-18,
          6.948138782764427e-16,
          1.0
        ],
        "angle_rad": 2.9630243810175585e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "phalanx_2_2_to_virtual_3_2",
        "joint_other": "phalanx_2_2_to_virtual_3_2",
        "axis_m": [
          4.537561723341792e-33,
          6.661338147750935e-16,
          1.0
        ],
        "axis_other_aligned": [
          7.443474041670879e-18,
          6.948138782764427e-16,
          1.0
        ],
        "angle_rad": 2.9630243810175585e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "virtual_3_2_to_phalanx_3_2",
        "joint_other": "virtual_3_2_to_phalanx_3_2",
        "axis_m": [
          4.537561723341792e-33,
          6.661338147750935e-16,
          1.0
        ],
        "axis_other_aligned": [
          7.443474041670879e-18,
          6.948138782764427e-16,
          1.0
        ],
        "angle_rad": 2.9630243810175585e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "phalanx_3_2_to_virtual_4_2",
        "joint_other": "phalanx_3_2_to_virtual_4_2",
        "axis_m": [
          4.537561723341792e-33,
          6.661338147750935e-16,
          1.0
        ],
        "axis_other_aligned": [
          7.443474041670879e-18,
          6.948138782764427e-16,
          1.0
        ],
        "angle_rad": 2.9630243810175585e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "virtual_4_2_to_phalanx_4_2",
        "joint_other": "virtual_4_2_to_phalanx_4_2",
        "axis_m": [
          4.537561723341792e-33,
          6.661338147750935e-16,
          1.0
        ],
        "axis_other_aligned": [
          7.443474041670879e-18,
          6.948138782764427e-16,
          1.0
        ],
        "angle_rad": 2.9630243810175585e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "phalanx_4_2_to_virtual_5_2",
        "joint_other": "phalanx_4_2_to_virtual_5_2",
        "axis_m": [
          4.537561723341792e-33,
          6.661338147750935e-16,
          1.0
        ],
        "axis_other_aligned": [
          7.443474041670879e-18,
          6.948138782764427e-16,
          1.0
        ],
        "angle_rad": 2.9630243810175585e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "virtual_5_2_to_phalanx_5_2",
        "joint_other": "virtual_5_2_to_phalanx_5_2",
        "axis_m": [
          4.537561723341792e-33,
          6.661338147750935e-16,
          1.0
        ],
        "axis_other_aligned": [
          7.443474041670879e-18,
          6.948138782764427e-16,
          1.0
        ],
        "angle_rad": 2.9630243810175585e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "phalanx_5_2_to_virtual_6_2",
        "joint_other": "phalanx_5_2_to_virtual_6_2",
        "axis_m": [
          4.537561723341792e-33,
          6.661338147750935e-16,
          1.0
        ],
        "axis_other_aligned": [
          7.443474041670879e-18,
          6.948138782764427e-16,
          1.0
        ],
        "angle_rad": 2.9630243810175585e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "virtual_6_2_to_reverse_phalanx_2",
        "joint_other": "virtual_6_2_to_reverse_phalanx_2",
        "axis_m": [
          4.537561723341792e-33,
          6.661338147750935e-16,
          1.0
        ],
        "axis_other_aligned": [
          7.443474041670879e-18,
          6.948138782764427e-16,
          1.0
        ],
        "angle_rad": 2.9630243810175585e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "reverse_phalanx_2_to_virtual_7_2",
        "joint_other": "reverse_phalanx_2_to_virtual_7_2",
        "axis_m": [
          4.537561723341792e-33,
          6.661338147750935e-16,
          1.0
        ],
        "axis_other_aligned": [
          7.443474041670879e-18,
          6.948138782764427e-16,
          1.0
        ],
        "angle_rad": 2.9630243810175585e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "virtual_7_2_to_rollover_phalanx_2",
        "joint_other": "virtual_7_2_to_rollover_phalanx_2",
        "axis_m": [
          4.537561723341792e-33,
          6.661338147750935e-16,
          1.0
        ],
        "axis_other_aligned": [
          7.443474041670879e-18,
          6.948138782764427e-16,
          1.0
        ],
        "angle_rad": 2.9630243810175585e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "rollover_phalanx_2_to_virtual_8_2",
        "joint_other": "rollover_phalanx_2_to_virtual_8_2",
        "axis_m": [
          4.537561723341792e-33,
          6.661338147750935e-16,
          1.0
        ],
        "axis_other_aligned": [
          7.443474041670879e-18,
          6.948138782764427e-16,
          1.0
        ],
        "angle_rad": 2.9630243810175585e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "virtual_8_2_to_phalanx_6_2",
        "joint_other": "virtual_8_2_to_phalanx_6_2",
        "axis_m": [
          4.537561723341792e-33,
          6.661338147750935e-16,
          1.0
        ],
        "axis_other_aligned": [
          7.443474041670879e-18,
          6.948138782764427e-16,
          1.0
        ],
        "angle_rad": 2.9630243810175585e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "phalanx_6_2_to_virtual_9_2",
        "joint_other": "phalanx_6_2_to_virtual_9_2",
        "axis_m": [
          4.537561723341792e-33,
          6.661338147750935e-16,
          1.0
        ],
        "axis_other_aligned": [
          7.443474041670879e-18,
          6.948138782764427e-16,
          1.0
        ],
        "angle_rad": 2.9630243810175585e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "virtual_9_2_to_distal_phalanx_2",
        "joint_other": "virtual_9_2_to_distal_phalanx_2",
        "axis_m": [
          4.537561723341792e-33,
          6.661338147750935e-16,
          1.0
        ],
        "axis_other_aligned": [
          7.443474041670879e-18,
          6.948138782764427e-16,
          1.0
        ],
        "angle_rad": 2.9630243810175585e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "heel_phalanx_3_to_virtual_1_3",
        "joint_other": "heel_phalanx_3_to_virtual_1_3",
        "axis_m": [
          4.734643501393354e-33,
          6.661338147750934e-16,
          1.0
        ],
        "axis_other_aligned": [
          7.443474041670879e-18,
          6.948138782764426e-16,
          1.0
        ],
        "angle_rad": 2.9630243810175585e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "virtual_1_3_to_phalanx_1_3",
        "joint_other": "virtual_1_3_to_phalanx_1_3",
        "axis_m": [
          4.537561723341792e-33,
          6.661338147750935e-16,
          1.0
        ],
        "axis_other_aligned": [
          7.443474041670879e-18,
          6.948138782764427e-16,
          1.0
        ],
        "angle_rad": 2.9630243810175585e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "phalanx_1_3_to_virtual_2_3",
        "joint_other": "phalanx_1_3_to_virtual_2_3",
        "axis_m": [
          4.537561723341792e-33,
          6.661338147750935e-16,
          1.0
        ],
        "axis_other_aligned": [
          7.443474041670879e-18,
          6.948138782764427e-16,
          1.0
        ],
        "angle_rad": 2.9630243810175585e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "virtual_2_3_to_phalanx_2_3",
        "joint_other": "virtual_2_3_to_phalanx_2_3",
        "axis_m": [
          4.537561723341792e-33,
          6.661338147750935e-16,
          1.0
        ],
        "axis_other_aligned": [
          7.443474041670879e-18,
          6.948138782764427e-16,
          1.0
        ],
        "angle_rad": 2.9630243810175585e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "phalanx_2_3_to_virtual_3_3",
        "joint_other": "phalanx_2_3_to_virtual_3_3",
        "axis_m": [
          4.537561723341792e-33,
          6.661338147750935e-16,
          1.0
        ],
        "axis_other_aligned": [
          7.443474041670879e-18,
          6.948138782764427e-16,
          1.0
        ],
        "angle_rad": 2.9630243810175585e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "virtual_3_3_to_phalanx_3_3",
        "joint_other": "virtual_3_3_to_phalanx_3_3",
        "axis_m": [
          4.537561723341792e-33,
          6.661338147750935e-16,
          1.0
        ],
        "axis_other_aligned": [
          7.443474041670879e-18,
          6.948138782764427e-16,
          1.0
        ],
        "angle_rad": 2.9630243810175585e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "phalanx_3_3_to_virtual_4_3",
        "joint_other": "phalanx_3_3_to_virtual_4_3",
        "axis_m": [
          4.537561723341792e-33,
          6.661338147750935e-16,
          1.0
        ],
        "axis_other_aligned": [
          7.443474041670879e-18,
          6.948138782764427e-16,
          1.0
        ],
        "angle_rad": 2.9630243810175585e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "virtual_4_3_to_phalanx_4_3",
        "joint_other": "virtual_4_3_to_phalanx_4_3",
        "axis_m": [
          4.537561723341792e-33,
          6.661338147750935e-16,
          1.0
        ],
        "axis_other_aligned": [
          7.443474041670879e-18,
          6.948138782764427e-16,
          1.0
        ],
        "angle_rad": 2.9630243810175585e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "phalanx_4_3_to_virtual_5_3",
        "joint_other": "phalanx_4_3_to_virtual_5_3",
        "axis_m": [
          4.537561723341792e-33,
          6.661338147750935e-16,
          1.0
        ],
        "axis_other_aligned": [
          7.443474041670879e-18,
          6.948138782764427e-16,
          1.0
        ],
        "angle_rad": 2.9630243810175585e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "virtual_5_3_to_phalanx_5_3",
        "joint_other": "virtual_5_3_to_phalanx_5_3",
        "axis_m": [
          4.537561723341792e-33,
          6.661338147750935e-16,
          1.0
        ],
        "axis_other_aligned": [
          7.443474041670879e-18,
          6.948138782764427e-16,
          1.0
        ],
        "angle_rad": 2.9630243810175585e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "phalanx_5_3_to_virtual_6_3",
        "joint_other": "phalanx_5_3_to_virtual_6_3",
        "axis_m": [
          4.537561723341792e-33,
          6.661338147750935e-16,
          1.0
        ],
        "axis_other_aligned": [
          7.443474041670879e-18,
          6.948138782764427e-16,
          1.0
        ],
        "angle_rad": 2.9630243810175585e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "virtual_6_3_to_reverse_phalanx_3",
        "joint_other": "virtual_6_3_to_reverse_phalanx_3",
        "axis_m": [
          4.537561723341792e-33,
          6.661338147750935e-16,
          1.0
        ],
        "axis_other_aligned": [
          7.443474041670879e-18,
          6.948138782764427e-16,
          1.0
        ],
        "angle_rad": 2.9630243810175585e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "reverse_phalanx_3_to_virtual_7_3",
        "joint_other": "reverse_phalanx_3_to_virtual_7_3",
        "axis_m": [
          4.537561723341792e-33,
          6.661338147750935e-16,
          1.0
        ],
        "axis_other_aligned": [
          7.443474041670879e-18,
          6.948138782764427e-16,
          1.0
        ],
        "angle_rad": 2.9630243810175585e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "virtual_7_3_to_rollover_phalanx_3",
        "joint_other": "virtual_7_3_to_rollover_phalanx_3",
        "axis_m": [
          4.537561723341792e-33,
          6.661338147750935e-16,
          1.0
        ],
        "axis_other_aligned": [
          7.443474041670879e-18,
          6.948138782764427e-16,
          1.0
        ],
        "angle_rad": 2.9630243810175585e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "rollover_phalanx_3_to_virtual_8_3",
        "joint_other": "rollover_phalanx_3_to_virtual_8_3",
        "axis_m": [
          4.537561723341792e-33,
          6.661338147750935e-16,
          1.0
        ],
        "axis_other_aligned": [
          7.443474041670879e-18,
          6.948138782764427e-16,
          1.0
        ],
        "angle_rad": 2.9630243810175585e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "virtual_8_3_to_phalanx_6_3",
        "joint_other": "virtual_8_3_to_phalanx_6_3",
        "axis_m": [
          4.537561723341792e-33,
          6.661338147750935e-16,
          1.0
        ],
        "axis_other_aligned": [
          7.443474041670879e-18,
          6.948138782764427e-16,
          1.0
        ],
        "angle_rad": 2.9630243810175585e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "phalanx_6_3_to_virtual_9_3",
        "joint_other": "phalanx_6_3_to_virtual_9_3",
        "axis_m": [
          4.537561723341792e-33,
          6.661338147750935e-16,
          1.0
        ],
        "axis_other_aligned": [
          7.443474041670879e-18,
          6.948138782764427e-16,
          1.0
        ],
        "angle_rad": 2.9630243810175585e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "virtual_9_3_to_distal_phalanx_3",
        "joint_other": "virtual_9_3_to_distal_phalanx_3",
        "axis_m": [
          4.537561723341792e-33,
          6.661338147750935e-16,
          1.0
        ],
        "axis_other_aligned": [
          7.443474041670879e-18,
          6.948138782764427e-16,
          1.0
        ],
        "angle_rad": 2.9630243810175585e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "heel_phalanx_4_to_virtual_1_4",
        "joint_other": "heel_phalanx_4_to_virtual_1_4",
        "axis_m": [
          4.734643501393354e-33,
          6.661338147750934e-16,
          1.0
        ],
        "axis_other_aligned": [
          7.443474041670879e-18,
          6.948138782764426e-16,
          1.0
        ],
        "angle_rad": 2.9630243810175585e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "virtual_1_4_to_phalanx_1_4",
        "joint_other": "virtual_1_4_to_phalanx_1_4",
        "axis_m": [
          4.537561723341792e-33,
          6.661338147750935e-16,
          1.0
        ],
        "axis_other_aligned": [
          7.443474041670879e-18,
          6.948138782764427e-16,
          1.0
        ],
        "angle_rad": 2.9630243810175585e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "phalanx_1_4_to_virtual_2_4",
        "joint_other": "phalanx_1_4_to_virtual_2_4",
        "axis_m": [
          4.537561723341792e-33,
          6.661338147750935e-16,
          1.0
        ],
        "axis_other_aligned": [
          7.443474041670879e-18,
          6.948138782764427e-16,
          1.0
        ],
        "angle_rad": 2.9630243810175585e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "virtual_2_4_to_phalanx_2_4",
        "joint_other": "virtual_2_4_to_phalanx_2_4",
        "axis_m": [
          4.537561723341792e-33,
          6.661338147750935e-16,
          1.0
        ],
        "axis_other_aligned": [
          7.443474041670879e-18,
          6.948138782764427e-16,
          1.0
        ],
        "angle_rad": 2.9630243810175585e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "phalanx_2_4_to_virtual_3_4",
        "joint_other": "phalanx_2_4_to_virtual_3_4",
        "axis_m": [
          4.537561723341792e-33,
          6.661338147750935e-16,
          1.0
        ],
        "axis_other_aligned": [
          7.443474041670879e-18,
          6.948138782764427e-16,
          1.0
        ],
        "angle_rad": 2.9630243810175585e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "virtual_3_4_to_phalanx_3_4",
        "joint_other": "virtual_3_4_to_phalanx_3_4",
        "axis_m": [
          4.537561723341792e-33,
          6.661338147750935e-16,
          1.0
        ],
        "axis_other_aligned": [
          7.443474041670879e-18,
          6.948138782764427e-16,
          1.0
        ],
        "angle_rad": 2.9630243810175585e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "phalanx_3_4_to_virtual_4_4",
        "joint_other": "phalanx_3_4_to_virtual_4_4",
        "axis_m": [
          4.537561723341792e-33,
          6.661338147750935e-16,
          1.0
        ],
        "axis_other_aligned": [
          7.443474041670879e-18,
          6.948138782764427e-16,
          1.0
        ],
        "angle_rad": 2.9630243810175585e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "virtual_4_4_to_phalanx_4_4",
        "joint_other": "virtual_4_4_to_phalanx_4_4",
        "axis_m": [
          4.537561723341792e-33,
          6.661338147750935e-16,
          1.0
        ],
        "axis_other_aligned": [
          7.443474041670879e-18,
          6.948138782764427e-16,
          1.0
        ],
        "angle_rad": 2.9630243810175585e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "phalanx_4_4_to_virtual_5_4",
        "joint_other": "phalanx_4_4_to_virtual_5_4",
        "axis_m": [
          4.537561723341792e-33,
          6.661338147750935e-16,
          1.0
        ],
        "axis_other_aligned": [
          7.443474041670879e-18,
          6.948138782764427e-16,
          1.0
        ],
        "angle_rad": 2.9630243810175585e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "virtual_5_4_to_phalanx_5_4",
        "joint_other": "virtual_5_4_to_phalanx_5_4",
        "axis_m": [
          4.537561723341792e-33,
          6.661338147750935e-16,
          1.0
        ],
        "axis_other_aligned": [
          7.443474041670879e-18,
          6.948138782764427e-16,
          1.0
        ],
        "angle_rad": 2.9630243810175585e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "phalanx_5_4_to_virtual_6_4",
        "joint_other": "phalanx_5_4_to_virtual_6_4",
        "axis_m": [
          4.537561723341792e-33,
          6.661338147750935e-16,
          1.0
        ],
        "axis_other_aligned": [
          7.443474041670879e-18,
          6.948138782764427e-16,
          1.0
        ],
        "angle_rad": 2.9630243810175585e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "virtual_6_4_to_reverse_phalanx_4",
        "joint_other": "virtual_6_4_to_reverse_phalanx_4",
        "axis_m": [
          4.537561723341792e-33,
          6.661338147750935e-16,
          1.0
        ],
        "axis_other_aligned": [
          7.443474041670879e-18,
          6.948138782764427e-16,
          1.0
        ],
        "angle_rad": 2.9630243810175585e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "reverse_phalanx_4_to_virtual_7_4",
        "joint_other": "reverse_phalanx_4_to_virtual_7_4",
        "axis_m": [
          4.537561723341792e-33,
          6.661338147750935e-16,
          1.0
        ],
        "axis_other_aligned": [
          7.443474041670879e-18,
          6.948138782764427e-16,
          1.0
        ],
        "angle_rad": 2.9630243810175585e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "virtual_7_4_to_rollover_phalanx_4",
        "joint_other": "virtual_7_4_to_rollover_phalanx_4",
        "axis_m": [
          4.537561723341792e-33,
          6.661338147750935e-16,
          1.0
        ],
        "axis_other_aligned": [
          7.443474041670879e-18,
          6.948138782764427e-16,
          1.0
        ],
        "angle_rad": 2.9630243810175585e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "rollover_phalanx_4_to_virtual_8_4",
        "joint_other": "rollover_phalanx_4_to_virtual_8_4",
        "axis_m": [
          4.537561723341792e-33,
          6.661338147750935e-16,
          1.0
        ],
        "axis_other_aligned": [
          7.443474041670879e-18,
          6.948138782764427e-16,
          1.0
        ],
        "angle_rad": 2.9630243810175585e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "virtual_8_4_to_phalanx_6_4",
        "joint_other": "virtual_8_4_to_phalanx_6_4",
        "axis_m": [
          4.537561723341792e-33,
          6.661338147750935e-16,
          1.0
        ],
        "axis_other_aligned": [
          7.443474041670879e-18,
          6.948138782764427e-16,
          1.0
        ],
        "angle_rad": 2.9630243810175585e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "phalanx_6_4_to_virtual_9_4",
        "joint_other": "phalanx_6_4_to_virtual_9_4",
        "axis_m": [
          4.537561723341792e-33,
          6.661338147750935e-16,
          1.0
        ],
        "axis_other_aligned": [
          7.443474041670879e-18,
          6.948138782764427e-16,
          1.0
        ],
        "angle_rad": 2.9630243810175585e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "virtual_9_4_to_distal_phalanx_4",
        "joint_other": "virtual_9_4_to_distal_phalanx_4",
        "axis_m": [
          4.537561723341792e-33,
          6.661338147750935e-16,
          1.0
        ],
        "axis_other_aligned": [
          7.443474041670879e-18,
          6.948138782764427e-16,
          1.0
        ],
        "angle_rad": 2.9630243810175585e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "heel_phalanx_5_to_virtual_1_5",
        "joint_other": "heel_phalanx_5_to_virtual_1_5",
        "axis_m": [
          4.734643501393354e-33,
          6.661338147750934e-16,
          1.0
        ],
        "axis_other_aligned": [
          7.443474041670879e-18,
          6.948138782764426e-16,
          1.0
        ],
        "angle_rad": 2.9630243810175585e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "virtual_1_5_to_phalanx_1_5",
        "joint_other": "virtual_1_5_to_phalanx_1_5",
        "axis_m": [
          4.537561723341792e-33,
          6.661338147750935e-16,
          1.0
        ],
        "axis_other_aligned": [
          7.443474041670879e-18,
          6.948138782764427e-16,
          1.0
        ],
        "angle_rad": 2.9630243810175585e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "phalanx_1_5_to_virtual_2_5",
        "joint_other": "phalanx_1_5_to_virtual_2_5",
        "axis_m": [
          4.537561723341792e-33,
          6.661338147750935e-16,
          1.0
        ],
        "axis_other_aligned": [
          7.443474041670879e-18,
          6.948138782764427e-16,
          1.0
        ],
        "angle_rad": 2.9630243810175585e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "virtual_2_5_to_phalanx_2_5",
        "joint_other": "virtual_2_5_to_phalanx_2_5",
        "axis_m": [
          4.537561723341792e-33,
          6.661338147750935e-16,
          1.0
        ],
        "axis_other_aligned": [
          7.443474041670879e-18,
          6.948138782764427e-16,
          1.0
        ],
        "angle_rad": 2.9630243810175585e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "phalanx_2_5_to_virtual_3_5",
        "joint_other": "phalanx_2_5_to_virtual_3_5",
        "axis_m": [
          4.537561723341792e-33,
          6.661338147750935e-16,
          1.0
        ],
        "axis_other_aligned": [
          7.443474041670879e-18,
          6.948138782764427e-16,
          1.0
        ],
        "angle_rad": 2.9630243810175585e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "virtual_3_5_to_phalanx_3_5",
        "joint_other": "virtual_3_5_to_phalanx_3_5",
        "axis_m": [
          4.537561723341792e-33,
          6.661338147750935e-16,
          1.0
        ],
        "axis_other_aligned": [
          7.443474041670879e-18,
          6.948138782764427e-16,
          1.0
        ],
        "angle_rad": 2.9630243810175585e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "phalanx_3_5_to_virtual_4_5",
        "joint_other": "phalanx_3_5_to_virtual_4_5",
        "axis_m": [
          4.537561723341792e-33,
          6.661338147750935e-16,
          1.0
        ],
        "axis_other_aligned": [
          7.443474041670879e-18,
          6.948138782764427e-16,
          1.0
        ],
        "angle_rad": 2.9630243810175585e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "virtual_4_5_to_phalanx_4_5",
        "joint_other": "virtual_4_5_to_phalanx_4_5",
        "axis_m": [
          4.537561723341792e-33,
          6.661338147750935e-16,
          1.0
        ],
        "axis_other_aligned": [
          7.443474041670879e-18,
          6.948138782764427e-16,
          1.0
        ],
        "angle_rad": 2.9630243810175585e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "phalanx_4_5_to_virtual_5_5",
        "joint_other": "phalanx_4_5_to_virtual_5_5",
        "axis_m": [
          4.537561723341792e-33,
          6.661338147750935e-16,
          1.0
        ],
        "axis_other_aligned": [
          7.443474041670879e-18,
          6.948138782764427e-16,
          1.0
        ],
        "angle_rad": 2.9630243810175585e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "virtual_5_5_to_phalanx_5_5",
        "joint_other": "virtual_5_5_to_phalanx_5_5",
        "axis_m": [
          4.537561723341792e-33,
          6.661338147750935e-16,
          1.0
        ],
        "axis_other_aligned": [
          7.443474041670879e-18,
          6.948138782764427e-16,
          1.0
        ],
        "angle_rad": 2.9630243810175585e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "phalanx_5_5_to_virtual_6_5",
        "joint_other": "phalanx_5_5_to_virtual_6_5",
        "axis_m": [
          4.537561723341792e-33,
          6.661338147750935e-16,
          1.0
        ],
        "axis_other_aligned": [
          7.443474041670879e-18,
          6.948138782764427e-16,
          1.0
        ],
        "angle_rad": 2.9630243810175585e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "virtual_6_5_to_reverse_phalanx_5",
        "joint_other": "virtual_6_5_to_reverse_phalanx_5",
        "axis_m": [
          4.537561723341792e-33,
          6.661338147750935e-16,
          1.0
        ],
        "axis_other_aligned": [
          7.443474041670879e-18,
          6.948138782764427e-16,
          1.0
        ],
        "angle_rad": 2.9630243810175585e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "reverse_phalanx_5_to_virtual_7_5",
        "joint_other": "reverse_phalanx_5_to_virtual_7_5",
        "axis_m": [
          4.537561723341792e-33,
          6.661338147750935e-16,
          1.0
        ],
        "axis_other_aligned": [
          7.443474041670879e-18,
          6.948138782764427e-16,
          1.0
        ],
        "angle_rad": 2.9630243810175585e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "virtual_7_5_to_rollover_phalanx_5",
        "joint_other": "virtual_7_5_to_rollover_phalanx_5",
        "axis_m": [
          4.537561723341792e-33,
          6.661338147750935e-16,
          1.0
        ],
        "axis_other_aligned": [
          7.443474041670879e-18,
          6.948138782764427e-16,
          1.0
        ],
        "angle_rad": 2.9630243810175585e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "rollover_phalanx_5_to_virtual_8_5",
        "joint_other": "rollover_phalanx_5_to_virtual_8_5",
        "axis_m": [
          4.537561723341792e-33,
          6.661338147750935e-16,
          1.0
        ],
        "axis_other_aligned": [
          7.443474041670879e-18,
          6.948138782764427e-16,
          1.0
        ],
        "angle_rad": 2.9630243810175585e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "virtual_8_5_to_phalanx_6_5",
        "joint_other": "virtual_8_5_to_phalanx_6_5",
        "axis_m": [
          4.537561723341792e-33,
          6.661338147750935e-16,
          1.0
        ],
        "axis_other_aligned": [
          7.443474041670879e-18,
          6.948138782764427e-16,
          1.0
        ],
        "angle_rad": 2.9630243810175585e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "phalanx_6_5_to_virtual_9_5",
        "joint_other": "phalanx_6_5_to_virtual_9_5",
        "axis_m": [
          4.537561723341792e-33,
          6.661338147750935e-16,
          1.0
        ],
        "axis_other_aligned": [
          7.443474041670879e-18,
          6.948138782764427e-16,
          1.0
        ],
        "angle_rad": 2.9630243810175585e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "virtual_9_5_to_distal_phalanx_5",
        "joint_other": "virtual_9_5_to_distal_phalanx_5",
        "axis_m": [
          4.537561723341792e-33,
          6.661338147750935e-16,
          1.0
        ],
        "axis_other_aligned": [
          7.443474041670879e-18,
          6.948138782764427e-16,
          1.0
        ],
        "angle_rad": 2.9630243810175585e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "cube_to_frontal_arch",
        "joint_other": "cube_to_frontal_arch",
        "axis_m": [
          1.0336302097132477e-17,
          4.440892098500624e-16,
          1.0
        ],
        "axis_other_aligned": [
          1.777977613880334e-17,
          4.727692733514118e-16,
          1.0
        ],
        "angle_rad": 2.963024381017577e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      }
    ],
    "axis_disagreements": [],
    "com_eligible": true,
    "covariance_singular_values": [
      0.18460232913673458,
      0.030637874809684325,
      0.019076466542020994
    ],
    "origin_residuals_m": {
      "attachment_cube": 1.794968653255206e-17,
      "posterior_arch": 1.794968653255206e-17,
      "heel": 2.7756908414657696e-17,
      "phalanx_1_1": 2.5018537765542006e-17,
      "phalanx_2_1": 1.962615573354719e-17,
      "phalanx_3_1": 2.2551405187698492e-17,
      "phalanx_4_1": 2.110382192020081e-17,
      "phalanx_5_1": 2.0816681711721685e-17,
      "reverse_phalanx_1": 2.0816681711721685e-17,
      "rollover_phalanx_1": 2.5018537765542006e-17,
      "phalanx_6_1": 2.0816681711721685e-17,
      "distal_phalanx_1": 2.0816681711721685e-17,
      "phalanx_1_2": 2.1942709178604383e-17,
      "phalanx_2_2": 1.5515838457795457e-17,
      "phalanx_3_2": 1.1107649934270853e-17,
      "phalanx_4_2": 7.757919228897728e-18,
      "phalanx_5_2": 6.938893903907228e-18,
      "reverse_phalanx_2": 6.938893903907228e-18,
      "rollover_phalanx_2": 1.5515838457795457e-17,
      "phalanx_6_2": 6.938893903907228e-18,
      "distal_phalanx_2": 6.938893903907228e-18,
      "phalanx_1_3": 2.0901639266105137e-17,
      "phalanx_2_3": 1.3972120070117818e-17,
      "phalanx_3_3": 8.779447576003984e-18,
      "phalanx_4_3": 3.6388319680924014e-18,
      "phalanx_5_3": 8.355051001106803e-19,
      "reverse_phalanx_3": 5.737244855640548e-19,
      "rollover_phalanx_3": 1.3880954285428108e-17,
      "phalanx_6_3": 8.429678645541644e-20,
      "distal_phalanx_3": 3.460774010020419e-19,
      "phalanx_1_4": 2.3273757686693185e-17,
      "phalanx_2_4": 1.734723475976807e-17,
      "phalanx_3_4": 1.3548623466035522e-17,
      "phalanx_4_4": 1.0971354589302191e-17,
      "phalanx_5_4": 1.0408340855860843e-17,
      "reverse_phalanx_4": 1.0408340855860843e-17,
      "rollover_phalanx_4": 1.734723475976807e-17,
      "phalanx_6_4": 1.0408340855860843e-17,
      "distal_phalanx_4": 6.938893903907228e-18,
      "phalanx_1_5": 2.5018537765542006e-17,
      "phalanx_2_5": 1.962615573354719e-17,
      "phalanx_3_5": 1.6365348541700844e-17,
      "phalanx_4_5": 1.4304896245381992e-17,
      "phalanx_5_5": 1.3877787807814457e-17,
      "reverse_phalanx_5": 1.3877787807814457e-17,
      "rollover_phalanx_5": 1.962615573354719e-17,
      "phalanx_6_5": 1.3877787807814457e-17,
      "distal_phalanx_5": 1.3877787807814457e-17,
      "frontal_arch": 1.794968653255206e-17
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
| robot / total_com_registered | [0.0168048625, 0.037031595, 0.000706205305] | [0.0168048625, 0.037031595, 0.000706205305] | [0.0168048625, 0.037031595, 0.000706205305] | [0, 0, 0] | eligible; compared after Kabsch alignment | [aggregate inputs](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/iit_softfoot/softfoot.xml#L1) | [aggregate inputs](https://github.com/NMMI/SoftFoot_MuJoCo/blob/43834f4490adf19a2443e8daa81d3a69fe716ea5/softfoot.xml#L1) | [aggregate inputs](https://github.com/NMMI/SoftFoot_MuJoCo/blob/3b87622feb1e36e9a758aa76854204412d4ca8e8/softfoot.xml#L1) |
| attachment_cube / com_registered | [-9.5664949e-05, -1.6749134e-05, 0.0013880927] | [-9.5664949e-05, -1.6749134e-05, 0.0013880927] | [-9.5664949e-05, -1.6749134e-05, 0.0013880927] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L54](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/iit_softfoot/softfoot.xml#L54) | [CoM/kinematic input L51](https://github.com/NMMI/SoftFoot_MuJoCo/blob/43834f4490adf19a2443e8daa81d3a69fe716ea5/softfoot.xml#L51) | [CoM/kinematic input L51](https://github.com/NMMI/SoftFoot_MuJoCo/blob/3b87622feb1e36e9a758aa76854204412d4ca8e8/softfoot.xml#L51) |
| posterior_arch / com_registered | [-0.03061955, 0.04238064, 0] | [-0.03061955, 0.04238064, 0] | [-0.03061955, 0.04238064, 0] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L61](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/iit_softfoot/softfoot.xml#L61) | [CoM/kinematic input L56](https://github.com/NMMI/SoftFoot_MuJoCo/blob/43834f4490adf19a2443e8daa81d3a69fe716ea5/softfoot.xml#L56) | [CoM/kinematic input L56](https://github.com/NMMI/SoftFoot_MuJoCo/blob/3b87622feb1e36e9a758aa76854204412d4ca8e8/softfoot.xml#L56) |
| heel / com_registered | [-0.0650750596, 0.083711226, 6.61892e-05] | [-0.0650750596, 0.083711226, 6.61892e-05] | [-0.0650750596, 0.083711226, 6.61892e-05] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L70](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/iit_softfoot/softfoot.xml#L70) | [CoM/kinematic input L61](https://github.com/NMMI/SoftFoot_MuJoCo/blob/43834f4490adf19a2443e8daa81d3a69fe716ea5/softfoot.xml#L61) | [CoM/kinematic input L61](https://github.com/NMMI/SoftFoot_MuJoCo/blob/3b87622feb1e36e9a758aa76854204412d4ca8e8/softfoot.xml#L61) |
| phalanx_1_1 / com_registered | [-0.0312710799, 0.085199705, 0.036999833] | [-0.0312710799, 0.085199705, 0.036999833] | [-0.0312710799, 0.085199705, 0.036999833] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L149](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/iit_softfoot/softfoot.xml#L149) | [CoM/kinematic input L105](https://github.com/NMMI/SoftFoot_MuJoCo/blob/43834f4490adf19a2443e8daa81d3a69fe716ea5/softfoot.xml#L105) | [CoM/kinematic input L105](https://github.com/NMMI/SoftFoot_MuJoCo/blob/3b87622feb1e36e9a758aa76854204412d4ca8e8/softfoot.xml#L105) |
| phalanx_2_1 / com_registered | [-0.00927107994, 0.085199705, 0.036999833] | [-0.00927107994, 0.085199705, 0.036999833] | [-0.00927107994, 0.085199705, 0.036999833] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L163](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/iit_softfoot/softfoot.xml#L163) | [CoM/kinematic input L115](https://github.com/NMMI/SoftFoot_MuJoCo/blob/43834f4490adf19a2443e8daa81d3a69fe716ea5/softfoot.xml#L115) | [CoM/kinematic input L115](https://github.com/NMMI/SoftFoot_MuJoCo/blob/3b87622feb1e36e9a758aa76854204412d4ca8e8/softfoot.xml#L115) |
| phalanx_3_1 / com_registered | [0.0127289201, 0.085199705, 0.036999833] | [0.0127289201, 0.085199705, 0.036999833] | [0.0127289201, 0.085199705, 0.036999833] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L177](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/iit_softfoot/softfoot.xml#L177) | [CoM/kinematic input L125](https://github.com/NMMI/SoftFoot_MuJoCo/blob/43834f4490adf19a2443e8daa81d3a69fe716ea5/softfoot.xml#L125) | [CoM/kinematic input L125](https://github.com/NMMI/SoftFoot_MuJoCo/blob/3b87622feb1e36e9a758aa76854204412d4ca8e8/softfoot.xml#L125) |
| phalanx_4_1 / com_registered | [0.0347289201, 0.085199705, 0.036999833] | [0.0347289201, 0.085199705, 0.036999833] | [0.0347289201, 0.085199705, 0.036999833] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L192](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/iit_softfoot/softfoot.xml#L192) | [CoM/kinematic input L135](https://github.com/NMMI/SoftFoot_MuJoCo/blob/43834f4490adf19a2443e8daa81d3a69fe716ea5/softfoot.xml#L135) | [CoM/kinematic input L135](https://github.com/NMMI/SoftFoot_MuJoCo/blob/3b87622feb1e36e9a758aa76854204412d4ca8e8/softfoot.xml#L135) |
| phalanx_5_1 / com_registered | [0.0567289201, 0.085199705, 0.036999833] | [0.0567289201, 0.085199705, 0.036999833] | [0.0567289201, 0.085199705, 0.036999833] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L207](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/iit_softfoot/softfoot.xml#L207) | [CoM/kinematic input L145](https://github.com/NMMI/SoftFoot_MuJoCo/blob/43834f4490adf19a2443e8daa81d3a69fe716ea5/softfoot.xml#L145) | [CoM/kinematic input L145](https://github.com/NMMI/SoftFoot_MuJoCo/blob/3b87622feb1e36e9a758aa76854204412d4ca8e8/softfoot.xml#L145) |
| reverse_phalanx_1 / com_registered | [0.0796469401, 0.086339144, 0.0369890249] | [0.0796469401, 0.086339144, 0.0369890249] | [0.0796469401, 0.086339144, 0.0369890249] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L222](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/iit_softfoot/softfoot.xml#L222) | [CoM/kinematic input L155](https://github.com/NMMI/SoftFoot_MuJoCo/blob/43834f4490adf19a2443e8daa81d3a69fe716ea5/softfoot.xml#L155) | [CoM/kinematic input L155](https://github.com/NMMI/SoftFoot_MuJoCo/blob/3b87622feb1e36e9a758aa76854204412d4ca8e8/softfoot.xml#L155) |
| rollover_phalanx_1 / com_registered | [0.10762416, 0.082813934, 0.0370001248] | [0.10762416, 0.082813934, 0.0370001248] | [0.10762416, 0.082813934, 0.0370001248] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L238](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/iit_softfoot/softfoot.xml#L238) | [CoM/kinematic input L165](https://github.com/NMMI/SoftFoot_MuJoCo/blob/43834f4490adf19a2443e8daa81d3a69fe716ea5/softfoot.xml#L165) | [CoM/kinematic input L165](https://github.com/NMMI/SoftFoot_MuJoCo/blob/3b87622feb1e36e9a758aa76854204412d4ca8e8/softfoot.xml#L165) |
| phalanx_6_1 / com_registered | [0.13457108, 0.085199705, 0.037000167] | [0.13457108, 0.085199705, 0.037000167] | [0.13457108, 0.085199705, 0.037000167] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L255](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/iit_softfoot/softfoot.xml#L255) | [CoM/kinematic input L175](https://github.com/NMMI/SoftFoot_MuJoCo/blob/43834f4490adf19a2443e8daa81d3a69fe716ea5/softfoot.xml#L175) | [CoM/kinematic input L175](https://github.com/NMMI/SoftFoot_MuJoCo/blob/3b87622feb1e36e9a758aa76854204412d4ca8e8/softfoot.xml#L175) |
| distal_phalanx_1 / com_registered | [0.1627173, 0.086778004, 0.0370001059] | [0.1627173, 0.086778004, 0.0370001059] | [0.1627173, 0.086778004, 0.0370001059] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L273](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/iit_softfoot/softfoot.xml#L273) | [CoM/kinematic input L185](https://github.com/NMMI/SoftFoot_MuJoCo/blob/43834f4490adf19a2443e8daa81d3a69fe716ea5/softfoot.xml#L185) | [CoM/kinematic input L185](https://github.com/NMMI/SoftFoot_MuJoCo/blob/3b87622feb1e36e9a758aa76854204412d4ca8e8/softfoot.xml#L185) |
| phalanx_1_2 / com_registered | [-0.0312710799, 0.085199705, 0.018499833] | [-0.0312710799, 0.085199705, 0.018499833] | [-0.0312710799, 0.085199705, 0.018499833] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L300](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/iit_softfoot/softfoot.xml#L300) | [CoM/kinematic input L205](https://github.com/NMMI/SoftFoot_MuJoCo/blob/43834f4490adf19a2443e8daa81d3a69fe716ea5/softfoot.xml#L205) | [CoM/kinematic input L205](https://github.com/NMMI/SoftFoot_MuJoCo/blob/3b87622feb1e36e9a758aa76854204412d4ca8e8/softfoot.xml#L205) |
| phalanx_2_2 / com_registered | [-0.00927107994, 0.085199705, 0.018499833] | [-0.00927107994, 0.085199705, 0.018499833] | [-0.00927107994, 0.085199705, 0.018499833] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L314](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/iit_softfoot/softfoot.xml#L314) | [CoM/kinematic input L215](https://github.com/NMMI/SoftFoot_MuJoCo/blob/43834f4490adf19a2443e8daa81d3a69fe716ea5/softfoot.xml#L215) | [CoM/kinematic input L215](https://github.com/NMMI/SoftFoot_MuJoCo/blob/3b87622feb1e36e9a758aa76854204412d4ca8e8/softfoot.xml#L215) |
| phalanx_3_2 / com_registered | [0.0127289201, 0.085199705, 0.018499833] | [0.0127289201, 0.085199705, 0.018499833] | [0.0127289201, 0.085199705, 0.018499833] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L328](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/iit_softfoot/softfoot.xml#L328) | [CoM/kinematic input L225](https://github.com/NMMI/SoftFoot_MuJoCo/blob/43834f4490adf19a2443e8daa81d3a69fe716ea5/softfoot.xml#L225) | [CoM/kinematic input L225](https://github.com/NMMI/SoftFoot_MuJoCo/blob/3b87622feb1e36e9a758aa76854204412d4ca8e8/softfoot.xml#L225) |
| phalanx_4_2 / com_registered | [0.0347289201, 0.085199705, 0.018499833] | [0.0347289201, 0.085199705, 0.018499833] | [0.0347289201, 0.085199705, 0.018499833] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L343](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/iit_softfoot/softfoot.xml#L343) | [CoM/kinematic input L235](https://github.com/NMMI/SoftFoot_MuJoCo/blob/43834f4490adf19a2443e8daa81d3a69fe716ea5/softfoot.xml#L235) | [CoM/kinematic input L235](https://github.com/NMMI/SoftFoot_MuJoCo/blob/3b87622feb1e36e9a758aa76854204412d4ca8e8/softfoot.xml#L235) |
| phalanx_5_2 / com_registered | [0.0567289201, 0.085199705, 0.018499833] | [0.0567289201, 0.085199705, 0.018499833] | [0.0567289201, 0.085199705, 0.018499833] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L358](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/iit_softfoot/softfoot.xml#L358) | [CoM/kinematic input L245](https://github.com/NMMI/SoftFoot_MuJoCo/blob/43834f4490adf19a2443e8daa81d3a69fe716ea5/softfoot.xml#L245) | [CoM/kinematic input L245](https://github.com/NMMI/SoftFoot_MuJoCo/blob/3b87622feb1e36e9a758aa76854204412d4ca8e8/softfoot.xml#L245) |
| reverse_phalanx_2 / com_registered | [0.0796469401, 0.086339144, 0.0184890249] | [0.0796469401, 0.086339144, 0.0184890249] | [0.0796469401, 0.086339144, 0.0184890249] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L373](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/iit_softfoot/softfoot.xml#L373) | [CoM/kinematic input L255](https://github.com/NMMI/SoftFoot_MuJoCo/blob/43834f4490adf19a2443e8daa81d3a69fe716ea5/softfoot.xml#L255) | [CoM/kinematic input L255](https://github.com/NMMI/SoftFoot_MuJoCo/blob/3b87622feb1e36e9a758aa76854204412d4ca8e8/softfoot.xml#L255) |
| rollover_phalanx_2 / com_registered | [0.10762416, 0.082813934, 0.0185001248] | [0.10762416, 0.082813934, 0.0185001248] | [0.10762416, 0.082813934, 0.0185001248] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L389](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/iit_softfoot/softfoot.xml#L389) | [CoM/kinematic input L265](https://github.com/NMMI/SoftFoot_MuJoCo/blob/43834f4490adf19a2443e8daa81d3a69fe716ea5/softfoot.xml#L265) | [CoM/kinematic input L265](https://github.com/NMMI/SoftFoot_MuJoCo/blob/3b87622feb1e36e9a758aa76854204412d4ca8e8/softfoot.xml#L265) |
| phalanx_6_2 / com_registered | [0.13457108, 0.085199705, 0.018500167] | [0.13457108, 0.085199705, 0.018500167] | [0.13457108, 0.085199705, 0.018500167] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L406](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/iit_softfoot/softfoot.xml#L406) | [CoM/kinematic input L275](https://github.com/NMMI/SoftFoot_MuJoCo/blob/43834f4490adf19a2443e8daa81d3a69fe716ea5/softfoot.xml#L275) | [CoM/kinematic input L275](https://github.com/NMMI/SoftFoot_MuJoCo/blob/3b87622feb1e36e9a758aa76854204412d4ca8e8/softfoot.xml#L275) |
| distal_phalanx_2 / com_registered | [0.1627173, 0.086778004, 0.0185001059] | [0.1627173, 0.086778004, 0.0185001059] | [0.1627173, 0.086778004, 0.0185001059] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L424](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/iit_softfoot/softfoot.xml#L424) | [CoM/kinematic input L285](https://github.com/NMMI/SoftFoot_MuJoCo/blob/43834f4490adf19a2443e8daa81d3a69fe716ea5/softfoot.xml#L285) | [CoM/kinematic input L285](https://github.com/NMMI/SoftFoot_MuJoCo/blob/3b87622feb1e36e9a758aa76854204412d4ca8e8/softfoot.xml#L285) |
| phalanx_1_3 / com_registered | [-0.0312710799, 0.085199705, -1.66954e-07] | [-0.0312710799, 0.085199705, -1.66954e-07] | [-0.0312710799, 0.085199705, -1.66954e-07] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L451](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/iit_softfoot/softfoot.xml#L451) | [CoM/kinematic input L305](https://github.com/NMMI/SoftFoot_MuJoCo/blob/43834f4490adf19a2443e8daa81d3a69fe716ea5/softfoot.xml#L305) | [CoM/kinematic input L305](https://github.com/NMMI/SoftFoot_MuJoCo/blob/3b87622feb1e36e9a758aa76854204412d4ca8e8/softfoot.xml#L305) |
| phalanx_2_3 / com_registered | [-0.00927107994, 0.085199705, -1.66954e-07] | [-0.00927107994, 0.085199705, -1.66954e-07] | [-0.00927107994, 0.085199705, -1.66954e-07] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L465](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/iit_softfoot/softfoot.xml#L465) | [CoM/kinematic input L315](https://github.com/NMMI/SoftFoot_MuJoCo/blob/43834f4490adf19a2443e8daa81d3a69fe716ea5/softfoot.xml#L315) | [CoM/kinematic input L315](https://github.com/NMMI/SoftFoot_MuJoCo/blob/3b87622feb1e36e9a758aa76854204412d4ca8e8/softfoot.xml#L315) |
| phalanx_3_3 / com_registered | [0.0127289201, 0.085199705, -1.66954e-07] | [0.0127289201, 0.085199705, -1.66954e-07] | [0.0127289201, 0.085199705, -1.66954e-07] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L479](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/iit_softfoot/softfoot.xml#L479) | [CoM/kinematic input L325](https://github.com/NMMI/SoftFoot_MuJoCo/blob/43834f4490adf19a2443e8daa81d3a69fe716ea5/softfoot.xml#L325) | [CoM/kinematic input L325](https://github.com/NMMI/SoftFoot_MuJoCo/blob/3b87622feb1e36e9a758aa76854204412d4ca8e8/softfoot.xml#L325) |
| phalanx_4_3 / com_registered | [0.0347289201, 0.085199705, -1.66954e-07] | [0.0347289201, 0.085199705, -1.66954e-07] | [0.0347289201, 0.085199705, -1.66954e-07] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L494](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/iit_softfoot/softfoot.xml#L494) | [CoM/kinematic input L335](https://github.com/NMMI/SoftFoot_MuJoCo/blob/43834f4490adf19a2443e8daa81d3a69fe716ea5/softfoot.xml#L335) | [CoM/kinematic input L335](https://github.com/NMMI/SoftFoot_MuJoCo/blob/3b87622feb1e36e9a758aa76854204412d4ca8e8/softfoot.xml#L335) |
| phalanx_5_3 / com_registered | [0.0567289201, 0.085199705, -1.66954e-07] | [0.0567289201, 0.085199705, -1.66954e-07] | [0.0567289201, 0.085199705, -1.66954e-07] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L509](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/iit_softfoot/softfoot.xml#L509) | [CoM/kinematic input L345](https://github.com/NMMI/SoftFoot_MuJoCo/blob/43834f4490adf19a2443e8daa81d3a69fe716ea5/softfoot.xml#L345) | [CoM/kinematic input L345](https://github.com/NMMI/SoftFoot_MuJoCo/blob/3b87622feb1e36e9a758aa76854204412d4ca8e8/softfoot.xml#L345) |
| reverse_phalanx_3 / com_registered | [0.0796469401, 0.086339144, -1.09751e-05] | [0.0796469401, 0.086339144, -1.09751e-05] | [0.0796469401, 0.086339144, -1.09751e-05] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L524](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/iit_softfoot/softfoot.xml#L524) | [CoM/kinematic input L355](https://github.com/NMMI/SoftFoot_MuJoCo/blob/43834f4490adf19a2443e8daa81d3a69fe716ea5/softfoot.xml#L355) | [CoM/kinematic input L355](https://github.com/NMMI/SoftFoot_MuJoCo/blob/3b87622feb1e36e9a758aa76854204412d4ca8e8/softfoot.xml#L355) |
| rollover_phalanx_3 / com_registered | [0.10762416, 0.082813934, 1.24761e-07] | [0.10762416, 0.082813934, 1.24761e-07] | [0.10762416, 0.082813934, 1.24761e-07] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L540](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/iit_softfoot/softfoot.xml#L540) | [CoM/kinematic input L365](https://github.com/NMMI/SoftFoot_MuJoCo/blob/43834f4490adf19a2443e8daa81d3a69fe716ea5/softfoot.xml#L365) | [CoM/kinematic input L365](https://github.com/NMMI/SoftFoot_MuJoCo/blob/3b87622feb1e36e9a758aa76854204412d4ca8e8/softfoot.xml#L365) |
| phalanx_6_3 / com_registered | [0.13457108, 0.085199705, 1.66954e-07] | [0.13457108, 0.085199705, 1.66954e-07] | [0.13457108, 0.085199705, 1.66954e-07] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L557](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/iit_softfoot/softfoot.xml#L557) | [CoM/kinematic input L375](https://github.com/NMMI/SoftFoot_MuJoCo/blob/43834f4490adf19a2443e8daa81d3a69fe716ea5/softfoot.xml#L375) | [CoM/kinematic input L375](https://github.com/NMMI/SoftFoot_MuJoCo/blob/3b87622feb1e36e9a758aa76854204412d4ca8e8/softfoot.xml#L375) |
| distal_phalanx_3 / com_registered | [0.1627173, 0.086778004, 1.0587e-07] | [0.1627173, 0.086778004, 1.0587e-07] | [0.1627173, 0.086778004, 1.0587e-07] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L575](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/iit_softfoot/softfoot.xml#L575) | [CoM/kinematic input L385](https://github.com/NMMI/SoftFoot_MuJoCo/blob/43834f4490adf19a2443e8daa81d3a69fe716ea5/softfoot.xml#L385) | [CoM/kinematic input L385](https://github.com/NMMI/SoftFoot_MuJoCo/blob/3b87622feb1e36e9a758aa76854204412d4ca8e8/softfoot.xml#L385) |
| phalanx_1_4 / com_registered | [-0.0312710799, 0.085199705, -0.018000167] | [-0.0312710799, 0.085199705, -0.018000167] | [-0.0312710799, 0.085199705, -0.018000167] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L602](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/iit_softfoot/softfoot.xml#L602) | [CoM/kinematic input L405](https://github.com/NMMI/SoftFoot_MuJoCo/blob/43834f4490adf19a2443e8daa81d3a69fe716ea5/softfoot.xml#L405) | [CoM/kinematic input L405](https://github.com/NMMI/SoftFoot_MuJoCo/blob/3b87622feb1e36e9a758aa76854204412d4ca8e8/softfoot.xml#L405) |
| phalanx_2_4 / com_registered | [-0.00927107994, 0.085199705, -0.018000167] | [-0.00927107994, 0.085199705, -0.018000167] | [-0.00927107994, 0.085199705, -0.018000167] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L616](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/iit_softfoot/softfoot.xml#L616) | [CoM/kinematic input L415](https://github.com/NMMI/SoftFoot_MuJoCo/blob/43834f4490adf19a2443e8daa81d3a69fe716ea5/softfoot.xml#L415) | [CoM/kinematic input L415](https://github.com/NMMI/SoftFoot_MuJoCo/blob/3b87622feb1e36e9a758aa76854204412d4ca8e8/softfoot.xml#L415) |
| phalanx_3_4 / com_registered | [0.0127289201, 0.085199705, -0.018000167] | [0.0127289201, 0.085199705, -0.018000167] | [0.0127289201, 0.085199705, -0.018000167] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L630](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/iit_softfoot/softfoot.xml#L630) | [CoM/kinematic input L425](https://github.com/NMMI/SoftFoot_MuJoCo/blob/43834f4490adf19a2443e8daa81d3a69fe716ea5/softfoot.xml#L425) | [CoM/kinematic input L425](https://github.com/NMMI/SoftFoot_MuJoCo/blob/3b87622feb1e36e9a758aa76854204412d4ca8e8/softfoot.xml#L425) |
| phalanx_4_4 / com_registered | [0.0347289201, 0.085199705, -0.018000167] | [0.0347289201, 0.085199705, -0.018000167] | [0.0347289201, 0.085199705, -0.018000167] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L645](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/iit_softfoot/softfoot.xml#L645) | [CoM/kinematic input L435](https://github.com/NMMI/SoftFoot_MuJoCo/blob/43834f4490adf19a2443e8daa81d3a69fe716ea5/softfoot.xml#L435) | [CoM/kinematic input L435](https://github.com/NMMI/SoftFoot_MuJoCo/blob/3b87622feb1e36e9a758aa76854204412d4ca8e8/softfoot.xml#L435) |
| phalanx_5_4 / com_registered | [0.0567289201, 0.085199705, -0.018000167] | [0.0567289201, 0.085199705, -0.018000167] | [0.0567289201, 0.085199705, -0.018000167] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L660](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/iit_softfoot/softfoot.xml#L660) | [CoM/kinematic input L445](https://github.com/NMMI/SoftFoot_MuJoCo/blob/43834f4490adf19a2443e8daa81d3a69fe716ea5/softfoot.xml#L445) | [CoM/kinematic input L445](https://github.com/NMMI/SoftFoot_MuJoCo/blob/3b87622feb1e36e9a758aa76854204412d4ca8e8/softfoot.xml#L445) |
| reverse_phalanx_4 / com_registered | [0.0796469401, 0.086339144, -0.0180109751] | [0.0796469401, 0.086339144, -0.0180109751] | [0.0796469401, 0.086339144, -0.0180109751] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L675](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/iit_softfoot/softfoot.xml#L675) | [CoM/kinematic input L455](https://github.com/NMMI/SoftFoot_MuJoCo/blob/43834f4490adf19a2443e8daa81d3a69fe716ea5/softfoot.xml#L455) | [CoM/kinematic input L455](https://github.com/NMMI/SoftFoot_MuJoCo/blob/3b87622feb1e36e9a758aa76854204412d4ca8e8/softfoot.xml#L455) |
| rollover_phalanx_4 / com_registered | [0.10762416, 0.082813934, -0.0179998752] | [0.10762416, 0.082813934, -0.0179998752] | [0.10762416, 0.082813934, -0.0179998752] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L691](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/iit_softfoot/softfoot.xml#L691) | [CoM/kinematic input L465](https://github.com/NMMI/SoftFoot_MuJoCo/blob/43834f4490adf19a2443e8daa81d3a69fe716ea5/softfoot.xml#L465) | [CoM/kinematic input L465](https://github.com/NMMI/SoftFoot_MuJoCo/blob/3b87622feb1e36e9a758aa76854204412d4ca8e8/softfoot.xml#L465) |
| phalanx_6_4 / com_registered | [0.13457108, 0.085199705, -0.017999833] | [0.13457108, 0.085199705, -0.017999833] | [0.13457108, 0.085199705, -0.017999833] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L708](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/iit_softfoot/softfoot.xml#L708) | [CoM/kinematic input L475](https://github.com/NMMI/SoftFoot_MuJoCo/blob/43834f4490adf19a2443e8daa81d3a69fe716ea5/softfoot.xml#L475) | [CoM/kinematic input L475](https://github.com/NMMI/SoftFoot_MuJoCo/blob/3b87622feb1e36e9a758aa76854204412d4ca8e8/softfoot.xml#L475) |
| distal_phalanx_4 / com_registered | [0.1627173, 0.086778004, -0.0179998941] | [0.1627173, 0.086778004, -0.0179998941] | [0.1627173, 0.086778004, -0.0179998941] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L726](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/iit_softfoot/softfoot.xml#L726) | [CoM/kinematic input L485](https://github.com/NMMI/SoftFoot_MuJoCo/blob/43834f4490adf19a2443e8daa81d3a69fe716ea5/softfoot.xml#L485) | [CoM/kinematic input L485](https://github.com/NMMI/SoftFoot_MuJoCo/blob/3b87622feb1e36e9a758aa76854204412d4ca8e8/softfoot.xml#L485) |
| phalanx_1_5 / com_registered | [-0.0312710799, 0.085199705, -0.037000167] | [-0.0312710799, 0.085199705, -0.037000167] | [-0.0312710799, 0.085199705, -0.037000167] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L753](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/iit_softfoot/softfoot.xml#L753) | [CoM/kinematic input L505](https://github.com/NMMI/SoftFoot_MuJoCo/blob/43834f4490adf19a2443e8daa81d3a69fe716ea5/softfoot.xml#L505) | [CoM/kinematic input L505](https://github.com/NMMI/SoftFoot_MuJoCo/blob/3b87622feb1e36e9a758aa76854204412d4ca8e8/softfoot.xml#L505) |
| phalanx_2_5 / com_registered | [-0.00927107994, 0.085199705, -0.037000167] | [-0.00927107994, 0.085199705, -0.037000167] | [-0.00927107994, 0.085199705, -0.037000167] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L767](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/iit_softfoot/softfoot.xml#L767) | [CoM/kinematic input L515](https://github.com/NMMI/SoftFoot_MuJoCo/blob/43834f4490adf19a2443e8daa81d3a69fe716ea5/softfoot.xml#L515) | [CoM/kinematic input L515](https://github.com/NMMI/SoftFoot_MuJoCo/blob/3b87622feb1e36e9a758aa76854204412d4ca8e8/softfoot.xml#L515) |
| phalanx_3_5 / com_registered | [0.0127289201, 0.085199705, -0.037000167] | [0.0127289201, 0.085199705, -0.037000167] | [0.0127289201, 0.085199705, -0.037000167] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L781](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/iit_softfoot/softfoot.xml#L781) | [CoM/kinematic input L525](https://github.com/NMMI/SoftFoot_MuJoCo/blob/43834f4490adf19a2443e8daa81d3a69fe716ea5/softfoot.xml#L525) | [CoM/kinematic input L525](https://github.com/NMMI/SoftFoot_MuJoCo/blob/3b87622feb1e36e9a758aa76854204412d4ca8e8/softfoot.xml#L525) |
| phalanx_4_5 / com_registered | [0.0347289201, 0.085199705, -0.037000167] | [0.0347289201, 0.085199705, -0.037000167] | [0.0347289201, 0.085199705, -0.037000167] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L796](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/iit_softfoot/softfoot.xml#L796) | [CoM/kinematic input L535](https://github.com/NMMI/SoftFoot_MuJoCo/blob/43834f4490adf19a2443e8daa81d3a69fe716ea5/softfoot.xml#L535) | [CoM/kinematic input L535](https://github.com/NMMI/SoftFoot_MuJoCo/blob/3b87622feb1e36e9a758aa76854204412d4ca8e8/softfoot.xml#L535) |
| phalanx_5_5 / com_registered | [0.0567289201, 0.085199705, -0.037000167] | [0.0567289201, 0.085199705, -0.037000167] | [0.0567289201, 0.085199705, -0.037000167] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L811](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/iit_softfoot/softfoot.xml#L811) | [CoM/kinematic input L545](https://github.com/NMMI/SoftFoot_MuJoCo/blob/43834f4490adf19a2443e8daa81d3a69fe716ea5/softfoot.xml#L545) | [CoM/kinematic input L545](https://github.com/NMMI/SoftFoot_MuJoCo/blob/3b87622feb1e36e9a758aa76854204412d4ca8e8/softfoot.xml#L545) |
| reverse_phalanx_5 / com_registered | [0.0796469401, 0.086339144, -0.0370109751] | [0.0796469401, 0.086339144, -0.0370109751] | [0.0796469401, 0.086339144, -0.0370109751] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L826](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/iit_softfoot/softfoot.xml#L826) | [CoM/kinematic input L555](https://github.com/NMMI/SoftFoot_MuJoCo/blob/43834f4490adf19a2443e8daa81d3a69fe716ea5/softfoot.xml#L555) | [CoM/kinematic input L555](https://github.com/NMMI/SoftFoot_MuJoCo/blob/3b87622feb1e36e9a758aa76854204412d4ca8e8/softfoot.xml#L555) |
| rollover_phalanx_5 / com_registered | [0.10762416, 0.082813934, -0.0369998752] | [0.10762416, 0.082813934, -0.0369998752] | [0.10762416, 0.082813934, -0.0369998752] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L842](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/iit_softfoot/softfoot.xml#L842) | [CoM/kinematic input L565](https://github.com/NMMI/SoftFoot_MuJoCo/blob/43834f4490adf19a2443e8daa81d3a69fe716ea5/softfoot.xml#L565) | [CoM/kinematic input L565](https://github.com/NMMI/SoftFoot_MuJoCo/blob/3b87622feb1e36e9a758aa76854204412d4ca8e8/softfoot.xml#L565) |
| phalanx_6_5 / com_registered | [0.13457108, 0.085199705, -0.036999833] | [0.13457108, 0.085199705, -0.036999833] | [0.13457108, 0.085199705, -0.036999833] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L859](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/iit_softfoot/softfoot.xml#L859) | [CoM/kinematic input L575](https://github.com/NMMI/SoftFoot_MuJoCo/blob/43834f4490adf19a2443e8daa81d3a69fe716ea5/softfoot.xml#L575) | [CoM/kinematic input L575](https://github.com/NMMI/SoftFoot_MuJoCo/blob/3b87622feb1e36e9a758aa76854204412d4ca8e8/softfoot.xml#L575) |
| distal_phalanx_5 / com_registered | [0.1627173, 0.086778004, -0.0369998941] | [0.1627173, 0.086778004, -0.0369998941] | [0.1627173, 0.086778004, -0.0369998941] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L877](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/iit_softfoot/softfoot.xml#L877) | [CoM/kinematic input L585](https://github.com/NMMI/SoftFoot_MuJoCo/blob/43834f4490adf19a2443e8daa81d3a69fe716ea5/softfoot.xml#L585) | [CoM/kinematic input L585](https://github.com/NMMI/SoftFoot_MuJoCo/blob/3b87622feb1e36e9a758aa76854204412d4ca8e8/softfoot.xml#L585) |
| frontal_arch / com_registered | [0.0613925737, 0.0374110872, 0] | [0.0613925737, 0.0374110872, 0] | [0.0613925737, 0.0374110872, 0] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L903](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/iit_softfoot/softfoot.xml#L903) | [CoM/kinematic input L606](https://github.com/NMMI/SoftFoot_MuJoCo/blob/43834f4490adf19a2443e8daa81d3a69fe716ea5/softfoot.xml#L606) | [CoM/kinematic input L606](https://github.com/NMMI/SoftFoot_MuJoCo/blob/3b87622feb1e36e9a758aa76854204412d4ca8e8/softfoot.xml#L606) |

## Mass accounting

Every contributing compiled body mass is listed here so total/subtree sums can be checked. Links point to explicit inertials or to geometry inputs when the compiler inferred a mass. CoM links identify inertial inputs; world coordinates additionally use the ancestor transforms and the registration recorded below.

| M body | M kg / source | S kg / source | H kg / source |
|---|---|---|---|
| attachment_cube | 0.45418805 / [input L54](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/iit_softfoot/softfoot.xml#L54) | 0.45418805 / [input L51](https://github.com/NMMI/SoftFoot_MuJoCo/blob/43834f4490adf19a2443e8daa81d3a69fe716ea5/softfoot.xml#L51) | 0.45418805 / [input L51](https://github.com/NMMI/SoftFoot_MuJoCo/blob/3b87622feb1e36e9a758aa76854204412d4ca8e8/softfoot.xml#L51) |
| posterior_arch | 0.067640931 / [input L61](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/iit_softfoot/softfoot.xml#L61) | 0.067640931 / [input L56](https://github.com/NMMI/SoftFoot_MuJoCo/blob/43834f4490adf19a2443e8daa81d3a69fe716ea5/softfoot.xml#L56) | 0.067640931 / [input L56](https://github.com/NMMI/SoftFoot_MuJoCo/blob/3b87622feb1e36e9a758aa76854204412d4ca8e8/softfoot.xml#L56) |
| heel | 0.0795653 / [input L70](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/iit_softfoot/softfoot.xml#L70) | 0.0795653 / [input L61](https://github.com/NMMI/SoftFoot_MuJoCo/blob/43834f4490adf19a2443e8daa81d3a69fe716ea5/softfoot.xml#L61) | 0.0795653 / [input L61](https://github.com/NMMI/SoftFoot_MuJoCo/blob/3b87622feb1e36e9a758aa76854204412d4ca8e8/softfoot.xml#L61) |
| phalanx_1_1 | 0.00523906 / [input L149](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/iit_softfoot/softfoot.xml#L149) | 0.00523906 / [input L105](https://github.com/NMMI/SoftFoot_MuJoCo/blob/43834f4490adf19a2443e8daa81d3a69fe716ea5/softfoot.xml#L105) | 0.00523906 / [input L105](https://github.com/NMMI/SoftFoot_MuJoCo/blob/3b87622feb1e36e9a758aa76854204412d4ca8e8/softfoot.xml#L105) |
| phalanx_2_1 | 0.00523906 / [input L163](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/iit_softfoot/softfoot.xml#L163) | 0.00523906 / [input L115](https://github.com/NMMI/SoftFoot_MuJoCo/blob/43834f4490adf19a2443e8daa81d3a69fe716ea5/softfoot.xml#L115) | 0.00523906 / [input L115](https://github.com/NMMI/SoftFoot_MuJoCo/blob/3b87622feb1e36e9a758aa76854204412d4ca8e8/softfoot.xml#L115) |
| phalanx_3_1 | 0.00523906 / [input L177](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/iit_softfoot/softfoot.xml#L177) | 0.00523906 / [input L125](https://github.com/NMMI/SoftFoot_MuJoCo/blob/43834f4490adf19a2443e8daa81d3a69fe716ea5/softfoot.xml#L125) | 0.00523906 / [input L125](https://github.com/NMMI/SoftFoot_MuJoCo/blob/3b87622feb1e36e9a758aa76854204412d4ca8e8/softfoot.xml#L125) |
| phalanx_4_1 | 0.00523906 / [input L192](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/iit_softfoot/softfoot.xml#L192) | 0.00523906 / [input L135](https://github.com/NMMI/SoftFoot_MuJoCo/blob/43834f4490adf19a2443e8daa81d3a69fe716ea5/softfoot.xml#L135) | 0.00523906 / [input L135](https://github.com/NMMI/SoftFoot_MuJoCo/blob/3b87622feb1e36e9a758aa76854204412d4ca8e8/softfoot.xml#L135) |
| phalanx_5_1 | 0.00523906 / [input L207](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/iit_softfoot/softfoot.xml#L207) | 0.00523906 / [input L145](https://github.com/NMMI/SoftFoot_MuJoCo/blob/43834f4490adf19a2443e8daa81d3a69fe716ea5/softfoot.xml#L145) | 0.00523906 / [input L145](https://github.com/NMMI/SoftFoot_MuJoCo/blob/3b87622feb1e36e9a758aa76854204412d4ca8e8/softfoot.xml#L145) |
| reverse_phalanx_1 | 0.00482342 / [input L222](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/iit_softfoot/softfoot.xml#L222) | 0.00482342 / [input L155](https://github.com/NMMI/SoftFoot_MuJoCo/blob/43834f4490adf19a2443e8daa81d3a69fe716ea5/softfoot.xml#L155) | 0.00482342 / [input L155](https://github.com/NMMI/SoftFoot_MuJoCo/blob/3b87622feb1e36e9a758aa76854204412d4ca8e8/softfoot.xml#L155) |
| rollover_phalanx_1 | 0.00692955 / [input L238](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/iit_softfoot/softfoot.xml#L238) | 0.00692955 / [input L165](https://github.com/NMMI/SoftFoot_MuJoCo/blob/43834f4490adf19a2443e8daa81d3a69fe716ea5/softfoot.xml#L165) | 0.00692955 / [input L165](https://github.com/NMMI/SoftFoot_MuJoCo/blob/3b87622feb1e36e9a758aa76854204412d4ca8e8/softfoot.xml#L165) |
| phalanx_6_1 | 0.00523906 / [input L255](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/iit_softfoot/softfoot.xml#L255) | 0.00523906 / [input L175](https://github.com/NMMI/SoftFoot_MuJoCo/blob/43834f4490adf19a2443e8daa81d3a69fe716ea5/softfoot.xml#L175) | 0.00523906 / [input L175](https://github.com/NMMI/SoftFoot_MuJoCo/blob/3b87622feb1e36e9a758aa76854204412d4ca8e8/softfoot.xml#L175) |
| distal_phalanx_1 | 0.00955892 / [input L273](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/iit_softfoot/softfoot.xml#L273) | 0.00955892 / [input L185](https://github.com/NMMI/SoftFoot_MuJoCo/blob/43834f4490adf19a2443e8daa81d3a69fe716ea5/softfoot.xml#L185) | 0.00955892 / [input L185](https://github.com/NMMI/SoftFoot_MuJoCo/blob/3b87622feb1e36e9a758aa76854204412d4ca8e8/softfoot.xml#L185) |
| phalanx_1_2 | 0.00523906 / [input L300](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/iit_softfoot/softfoot.xml#L300) | 0.00523906 / [input L205](https://github.com/NMMI/SoftFoot_MuJoCo/blob/43834f4490adf19a2443e8daa81d3a69fe716ea5/softfoot.xml#L205) | 0.00523906 / [input L205](https://github.com/NMMI/SoftFoot_MuJoCo/blob/3b87622feb1e36e9a758aa76854204412d4ca8e8/softfoot.xml#L205) |
| phalanx_2_2 | 0.00523906 / [input L314](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/iit_softfoot/softfoot.xml#L314) | 0.00523906 / [input L215](https://github.com/NMMI/SoftFoot_MuJoCo/blob/43834f4490adf19a2443e8daa81d3a69fe716ea5/softfoot.xml#L215) | 0.00523906 / [input L215](https://github.com/NMMI/SoftFoot_MuJoCo/blob/3b87622feb1e36e9a758aa76854204412d4ca8e8/softfoot.xml#L215) |
| phalanx_3_2 | 0.00523906 / [input L328](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/iit_softfoot/softfoot.xml#L328) | 0.00523906 / [input L225](https://github.com/NMMI/SoftFoot_MuJoCo/blob/43834f4490adf19a2443e8daa81d3a69fe716ea5/softfoot.xml#L225) | 0.00523906 / [input L225](https://github.com/NMMI/SoftFoot_MuJoCo/blob/3b87622feb1e36e9a758aa76854204412d4ca8e8/softfoot.xml#L225) |
| phalanx_4_2 | 0.00523906 / [input L343](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/iit_softfoot/softfoot.xml#L343) | 0.00523906 / [input L235](https://github.com/NMMI/SoftFoot_MuJoCo/blob/43834f4490adf19a2443e8daa81d3a69fe716ea5/softfoot.xml#L235) | 0.00523906 / [input L235](https://github.com/NMMI/SoftFoot_MuJoCo/blob/3b87622feb1e36e9a758aa76854204412d4ca8e8/softfoot.xml#L235) |
| phalanx_5_2 | 0.00523906 / [input L358](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/iit_softfoot/softfoot.xml#L358) | 0.00523906 / [input L245](https://github.com/NMMI/SoftFoot_MuJoCo/blob/43834f4490adf19a2443e8daa81d3a69fe716ea5/softfoot.xml#L245) | 0.00523906 / [input L245](https://github.com/NMMI/SoftFoot_MuJoCo/blob/3b87622feb1e36e9a758aa76854204412d4ca8e8/softfoot.xml#L245) |
| reverse_phalanx_2 | 0.00482342 / [input L373](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/iit_softfoot/softfoot.xml#L373) | 0.00482342 / [input L255](https://github.com/NMMI/SoftFoot_MuJoCo/blob/43834f4490adf19a2443e8daa81d3a69fe716ea5/softfoot.xml#L255) | 0.00482342 / [input L255](https://github.com/NMMI/SoftFoot_MuJoCo/blob/3b87622feb1e36e9a758aa76854204412d4ca8e8/softfoot.xml#L255) |
| rollover_phalanx_2 | 0.00692955 / [input L389](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/iit_softfoot/softfoot.xml#L389) | 0.00692955 / [input L265](https://github.com/NMMI/SoftFoot_MuJoCo/blob/43834f4490adf19a2443e8daa81d3a69fe716ea5/softfoot.xml#L265) | 0.00692955 / [input L265](https://github.com/NMMI/SoftFoot_MuJoCo/blob/3b87622feb1e36e9a758aa76854204412d4ca8e8/softfoot.xml#L265) |
| phalanx_6_2 | 0.00523906 / [input L406](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/iit_softfoot/softfoot.xml#L406) | 0.00523906 / [input L275](https://github.com/NMMI/SoftFoot_MuJoCo/blob/43834f4490adf19a2443e8daa81d3a69fe716ea5/softfoot.xml#L275) | 0.00523906 / [input L275](https://github.com/NMMI/SoftFoot_MuJoCo/blob/3b87622feb1e36e9a758aa76854204412d4ca8e8/softfoot.xml#L275) |
| distal_phalanx_2 | 0.00955892 / [input L424](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/iit_softfoot/softfoot.xml#L424) | 0.00955892 / [input L285](https://github.com/NMMI/SoftFoot_MuJoCo/blob/43834f4490adf19a2443e8daa81d3a69fe716ea5/softfoot.xml#L285) | 0.00955892 / [input L285](https://github.com/NMMI/SoftFoot_MuJoCo/blob/3b87622feb1e36e9a758aa76854204412d4ca8e8/softfoot.xml#L285) |
| phalanx_1_3 | 0.00523906 / [input L451](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/iit_softfoot/softfoot.xml#L451) | 0.00523906 / [input L305](https://github.com/NMMI/SoftFoot_MuJoCo/blob/43834f4490adf19a2443e8daa81d3a69fe716ea5/softfoot.xml#L305) | 0.00523906 / [input L305](https://github.com/NMMI/SoftFoot_MuJoCo/blob/3b87622feb1e36e9a758aa76854204412d4ca8e8/softfoot.xml#L305) |
| phalanx_2_3 | 0.00523906 / [input L465](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/iit_softfoot/softfoot.xml#L465) | 0.00523906 / [input L315](https://github.com/NMMI/SoftFoot_MuJoCo/blob/43834f4490adf19a2443e8daa81d3a69fe716ea5/softfoot.xml#L315) | 0.00523906 / [input L315](https://github.com/NMMI/SoftFoot_MuJoCo/blob/3b87622feb1e36e9a758aa76854204412d4ca8e8/softfoot.xml#L315) |
| phalanx_3_3 | 0.00523906 / [input L479](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/iit_softfoot/softfoot.xml#L479) | 0.00523906 / [input L325](https://github.com/NMMI/SoftFoot_MuJoCo/blob/43834f4490adf19a2443e8daa81d3a69fe716ea5/softfoot.xml#L325) | 0.00523906 / [input L325](https://github.com/NMMI/SoftFoot_MuJoCo/blob/3b87622feb1e36e9a758aa76854204412d4ca8e8/softfoot.xml#L325) |
| phalanx_4_3 | 0.00523906 / [input L494](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/iit_softfoot/softfoot.xml#L494) | 0.00523906 / [input L335](https://github.com/NMMI/SoftFoot_MuJoCo/blob/43834f4490adf19a2443e8daa81d3a69fe716ea5/softfoot.xml#L335) | 0.00523906 / [input L335](https://github.com/NMMI/SoftFoot_MuJoCo/blob/3b87622feb1e36e9a758aa76854204412d4ca8e8/softfoot.xml#L335) |
| phalanx_5_3 | 0.00523906 / [input L509](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/iit_softfoot/softfoot.xml#L509) | 0.00523906 / [input L345](https://github.com/NMMI/SoftFoot_MuJoCo/blob/43834f4490adf19a2443e8daa81d3a69fe716ea5/softfoot.xml#L345) | 0.00523906 / [input L345](https://github.com/NMMI/SoftFoot_MuJoCo/blob/3b87622feb1e36e9a758aa76854204412d4ca8e8/softfoot.xml#L345) |
| reverse_phalanx_3 | 0.00482342 / [input L524](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/iit_softfoot/softfoot.xml#L524) | 0.00482342 / [input L355](https://github.com/NMMI/SoftFoot_MuJoCo/blob/43834f4490adf19a2443e8daa81d3a69fe716ea5/softfoot.xml#L355) | 0.00482342 / [input L355](https://github.com/NMMI/SoftFoot_MuJoCo/blob/3b87622feb1e36e9a758aa76854204412d4ca8e8/softfoot.xml#L355) |
| rollover_phalanx_3 | 0.00692955 / [input L540](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/iit_softfoot/softfoot.xml#L540) | 0.00692955 / [input L365](https://github.com/NMMI/SoftFoot_MuJoCo/blob/43834f4490adf19a2443e8daa81d3a69fe716ea5/softfoot.xml#L365) | 0.00692955 / [input L365](https://github.com/NMMI/SoftFoot_MuJoCo/blob/3b87622feb1e36e9a758aa76854204412d4ca8e8/softfoot.xml#L365) |
| phalanx_6_3 | 0.00523906 / [input L557](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/iit_softfoot/softfoot.xml#L557) | 0.00523906 / [input L375](https://github.com/NMMI/SoftFoot_MuJoCo/blob/43834f4490adf19a2443e8daa81d3a69fe716ea5/softfoot.xml#L375) | 0.00523906 / [input L375](https://github.com/NMMI/SoftFoot_MuJoCo/blob/3b87622feb1e36e9a758aa76854204412d4ca8e8/softfoot.xml#L375) |
| distal_phalanx_3 | 0.00955892 / [input L575](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/iit_softfoot/softfoot.xml#L575) | 0.00955892 / [input L385](https://github.com/NMMI/SoftFoot_MuJoCo/blob/43834f4490adf19a2443e8daa81d3a69fe716ea5/softfoot.xml#L385) | 0.00955892 / [input L385](https://github.com/NMMI/SoftFoot_MuJoCo/blob/3b87622feb1e36e9a758aa76854204412d4ca8e8/softfoot.xml#L385) |
| phalanx_1_4 | 0.00523906 / [input L602](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/iit_softfoot/softfoot.xml#L602) | 0.00523906 / [input L405](https://github.com/NMMI/SoftFoot_MuJoCo/blob/43834f4490adf19a2443e8daa81d3a69fe716ea5/softfoot.xml#L405) | 0.00523906 / [input L405](https://github.com/NMMI/SoftFoot_MuJoCo/blob/3b87622feb1e36e9a758aa76854204412d4ca8e8/softfoot.xml#L405) |
| phalanx_2_4 | 0.00523906 / [input L616](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/iit_softfoot/softfoot.xml#L616) | 0.00523906 / [input L415](https://github.com/NMMI/SoftFoot_MuJoCo/blob/43834f4490adf19a2443e8daa81d3a69fe716ea5/softfoot.xml#L415) | 0.00523906 / [input L415](https://github.com/NMMI/SoftFoot_MuJoCo/blob/3b87622feb1e36e9a758aa76854204412d4ca8e8/softfoot.xml#L415) |
| phalanx_3_4 | 0.00523906 / [input L630](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/iit_softfoot/softfoot.xml#L630) | 0.00523906 / [input L425](https://github.com/NMMI/SoftFoot_MuJoCo/blob/43834f4490adf19a2443e8daa81d3a69fe716ea5/softfoot.xml#L425) | 0.00523906 / [input L425](https://github.com/NMMI/SoftFoot_MuJoCo/blob/3b87622feb1e36e9a758aa76854204412d4ca8e8/softfoot.xml#L425) |
| phalanx_4_4 | 0.00523906 / [input L645](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/iit_softfoot/softfoot.xml#L645) | 0.00523906 / [input L435](https://github.com/NMMI/SoftFoot_MuJoCo/blob/43834f4490adf19a2443e8daa81d3a69fe716ea5/softfoot.xml#L435) | 0.00523906 / [input L435](https://github.com/NMMI/SoftFoot_MuJoCo/blob/3b87622feb1e36e9a758aa76854204412d4ca8e8/softfoot.xml#L435) |
| phalanx_5_4 | 0.00523906 / [input L660](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/iit_softfoot/softfoot.xml#L660) | 0.00523906 / [input L445](https://github.com/NMMI/SoftFoot_MuJoCo/blob/43834f4490adf19a2443e8daa81d3a69fe716ea5/softfoot.xml#L445) | 0.00523906 / [input L445](https://github.com/NMMI/SoftFoot_MuJoCo/blob/3b87622feb1e36e9a758aa76854204412d4ca8e8/softfoot.xml#L445) |
| reverse_phalanx_4 | 0.00482342 / [input L675](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/iit_softfoot/softfoot.xml#L675) | 0.00482342 / [input L455](https://github.com/NMMI/SoftFoot_MuJoCo/blob/43834f4490adf19a2443e8daa81d3a69fe716ea5/softfoot.xml#L455) | 0.00482342 / [input L455](https://github.com/NMMI/SoftFoot_MuJoCo/blob/3b87622feb1e36e9a758aa76854204412d4ca8e8/softfoot.xml#L455) |
| rollover_phalanx_4 | 0.00692955 / [input L691](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/iit_softfoot/softfoot.xml#L691) | 0.00692955 / [input L465](https://github.com/NMMI/SoftFoot_MuJoCo/blob/43834f4490adf19a2443e8daa81d3a69fe716ea5/softfoot.xml#L465) | 0.00692955 / [input L465](https://github.com/NMMI/SoftFoot_MuJoCo/blob/3b87622feb1e36e9a758aa76854204412d4ca8e8/softfoot.xml#L465) |
| phalanx_6_4 | 0.00523906 / [input L708](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/iit_softfoot/softfoot.xml#L708) | 0.00523906 / [input L475](https://github.com/NMMI/SoftFoot_MuJoCo/blob/43834f4490adf19a2443e8daa81d3a69fe716ea5/softfoot.xml#L475) | 0.00523906 / [input L475](https://github.com/NMMI/SoftFoot_MuJoCo/blob/3b87622feb1e36e9a758aa76854204412d4ca8e8/softfoot.xml#L475) |
| distal_phalanx_4 | 0.00955892 / [input L726](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/iit_softfoot/softfoot.xml#L726) | 0.00955892 / [input L485](https://github.com/NMMI/SoftFoot_MuJoCo/blob/43834f4490adf19a2443e8daa81d3a69fe716ea5/softfoot.xml#L485) | 0.00955892 / [input L485](https://github.com/NMMI/SoftFoot_MuJoCo/blob/3b87622feb1e36e9a758aa76854204412d4ca8e8/softfoot.xml#L485) |
| phalanx_1_5 | 0.00523906 / [input L753](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/iit_softfoot/softfoot.xml#L753) | 0.00523906 / [input L505](https://github.com/NMMI/SoftFoot_MuJoCo/blob/43834f4490adf19a2443e8daa81d3a69fe716ea5/softfoot.xml#L505) | 0.00523906 / [input L505](https://github.com/NMMI/SoftFoot_MuJoCo/blob/3b87622feb1e36e9a758aa76854204412d4ca8e8/softfoot.xml#L505) |
| phalanx_2_5 | 0.00523906 / [input L767](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/iit_softfoot/softfoot.xml#L767) | 0.00523906 / [input L515](https://github.com/NMMI/SoftFoot_MuJoCo/blob/43834f4490adf19a2443e8daa81d3a69fe716ea5/softfoot.xml#L515) | 0.00523906 / [input L515](https://github.com/NMMI/SoftFoot_MuJoCo/blob/3b87622feb1e36e9a758aa76854204412d4ca8e8/softfoot.xml#L515) |
| phalanx_3_5 | 0.00523906 / [input L781](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/iit_softfoot/softfoot.xml#L781) | 0.00523906 / [input L525](https://github.com/NMMI/SoftFoot_MuJoCo/blob/43834f4490adf19a2443e8daa81d3a69fe716ea5/softfoot.xml#L525) | 0.00523906 / [input L525](https://github.com/NMMI/SoftFoot_MuJoCo/blob/3b87622feb1e36e9a758aa76854204412d4ca8e8/softfoot.xml#L525) |
| phalanx_4_5 | 0.00523906 / [input L796](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/iit_softfoot/softfoot.xml#L796) | 0.00523906 / [input L535](https://github.com/NMMI/SoftFoot_MuJoCo/blob/43834f4490adf19a2443e8daa81d3a69fe716ea5/softfoot.xml#L535) | 0.00523906 / [input L535](https://github.com/NMMI/SoftFoot_MuJoCo/blob/3b87622feb1e36e9a758aa76854204412d4ca8e8/softfoot.xml#L535) |
| phalanx_5_5 | 0.00523906 / [input L811](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/iit_softfoot/softfoot.xml#L811) | 0.00523906 / [input L545](https://github.com/NMMI/SoftFoot_MuJoCo/blob/43834f4490adf19a2443e8daa81d3a69fe716ea5/softfoot.xml#L545) | 0.00523906 / [input L545](https://github.com/NMMI/SoftFoot_MuJoCo/blob/3b87622feb1e36e9a758aa76854204412d4ca8e8/softfoot.xml#L545) |
| reverse_phalanx_5 | 0.00482342 / [input L826](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/iit_softfoot/softfoot.xml#L826) | 0.00482342 / [input L555](https://github.com/NMMI/SoftFoot_MuJoCo/blob/43834f4490adf19a2443e8daa81d3a69fe716ea5/softfoot.xml#L555) | 0.00482342 / [input L555](https://github.com/NMMI/SoftFoot_MuJoCo/blob/3b87622feb1e36e9a758aa76854204412d4ca8e8/softfoot.xml#L555) |
| rollover_phalanx_5 | 0.00692955 / [input L842](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/iit_softfoot/softfoot.xml#L842) | 0.00692955 / [input L565](https://github.com/NMMI/SoftFoot_MuJoCo/blob/43834f4490adf19a2443e8daa81d3a69fe716ea5/softfoot.xml#L565) | 0.00692955 / [input L565](https://github.com/NMMI/SoftFoot_MuJoCo/blob/3b87622feb1e36e9a758aa76854204412d4ca8e8/softfoot.xml#L565) |
| phalanx_6_5 | 0.00523906 / [input L859](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/iit_softfoot/softfoot.xml#L859) | 0.00523906 / [input L575](https://github.com/NMMI/SoftFoot_MuJoCo/blob/43834f4490adf19a2443e8daa81d3a69fe716ea5/softfoot.xml#L575) | 0.00523906 / [input L575](https://github.com/NMMI/SoftFoot_MuJoCo/blob/3b87622feb1e36e9a758aa76854204412d4ca8e8/softfoot.xml#L575) |
| distal_phalanx_5 | 0.00955892 / [input L877](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/iit_softfoot/softfoot.xml#L877) | 0.00955892 / [input L585](https://github.com/NMMI/SoftFoot_MuJoCo/blob/43834f4490adf19a2443e8daa81d3a69fe716ea5/softfoot.xml#L585) | 0.00955892 / [input L585](https://github.com/NMMI/SoftFoot_MuJoCo/blob/3b87622feb1e36e9a758aa76854204412d4ca8e8/softfoot.xml#L585) |
| frontal_arch | 0.0720266 / [input L903](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/iit_softfoot/softfoot.xml#L903) | 0.0720266 / [input L606](https://github.com/NMMI/SoftFoot_MuJoCo/blob/43834f4490adf19a2443e8daa81d3a69fe716ea5/softfoot.xml#L606) | 0.0720266 / [input L606](https://github.com/NMMI/SoftFoot_MuJoCo/blob/3b87622feb1e36e9a758aa76854204412d4ca8e8/softfoot.xml#L606) |

## Coverage and unmatched elements

```json
{
  "mapping_h": {
    "bodies": {
      "attachment_cube": "attachment_cube",
      "posterior_arch": "posterior_arch",
      "heel": "heel",
      "phalanx_1_1": "phalanx_1_1",
      "phalanx_2_1": "phalanx_2_1",
      "phalanx_3_1": "phalanx_3_1",
      "phalanx_4_1": "phalanx_4_1",
      "phalanx_5_1": "phalanx_5_1",
      "reverse_phalanx_1": "reverse_phalanx_1",
      "rollover_phalanx_1": "rollover_phalanx_1",
      "phalanx_6_1": "phalanx_6_1",
      "distal_phalanx_1": "distal_phalanx_1",
      "phalanx_1_2": "phalanx_1_2",
      "phalanx_2_2": "phalanx_2_2",
      "phalanx_3_2": "phalanx_3_2",
      "phalanx_4_2": "phalanx_4_2",
      "phalanx_5_2": "phalanx_5_2",
      "reverse_phalanx_2": "reverse_phalanx_2",
      "rollover_phalanx_2": "rollover_phalanx_2",
      "phalanx_6_2": "phalanx_6_2",
      "distal_phalanx_2": "distal_phalanx_2",
      "phalanx_1_3": "phalanx_1_3",
      "phalanx_2_3": "phalanx_2_3",
      "phalanx_3_3": "phalanx_3_3",
      "phalanx_4_3": "phalanx_4_3",
      "phalanx_5_3": "phalanx_5_3",
      "reverse_phalanx_3": "reverse_phalanx_3",
      "rollover_phalanx_3": "rollover_phalanx_3",
      "phalanx_6_3": "phalanx_6_3",
      "distal_phalanx_3": "distal_phalanx_3",
      "phalanx_1_4": "phalanx_1_4",
      "phalanx_2_4": "phalanx_2_4",
      "phalanx_3_4": "phalanx_3_4",
      "phalanx_4_4": "phalanx_4_4",
      "phalanx_5_4": "phalanx_5_4",
      "reverse_phalanx_4": "reverse_phalanx_4",
      "rollover_phalanx_4": "rollover_phalanx_4",
      "phalanx_6_4": "phalanx_6_4",
      "distal_phalanx_4": "distal_phalanx_4",
      "phalanx_1_5": "phalanx_1_5",
      "phalanx_2_5": "phalanx_2_5",
      "phalanx_3_5": "phalanx_3_5",
      "phalanx_4_5": "phalanx_4_5",
      "phalanx_5_5": "phalanx_5_5",
      "reverse_phalanx_5": "reverse_phalanx_5",
      "rollover_phalanx_5": "rollover_phalanx_5",
      "phalanx_6_5": "phalanx_6_5",
      "distal_phalanx_5": "distal_phalanx_5",
      "frontal_arch": "frontal_arch"
    },
    "joints": {
      "posterior_arch_to_heel": "posterior_arch_to_heel",
      "heel_phalanx_1_to_virtual_1_1": "heel_phalanx_1_to_virtual_1_1",
      "virtual_1_1_to_phalanx_1_1": "virtual_1_1_to_phalanx_1_1",
      "phalanx_1_1_to_virtual_2_1": "phalanx_1_1_to_virtual_2_1",
      "virtual_2_1_to_phalanx_2_1": "virtual_2_1_to_phalanx_2_1",
      "phalanx_2_1_to_virtual_3_1": "phalanx_2_1_to_virtual_3_1",
      "virtual_3_1_to_phalanx_3_1": "virtual_3_1_to_phalanx_3_1",
      "phalanx_3_1_to_virtual_4_1": "phalanx_3_1_to_virtual_4_1",
      "virtual_4_1_to_phalanx_4_1": "virtual_4_1_to_phalanx_4_1",
      "phalanx_4_1_to_virtual_5_1": "phalanx_4_1_to_virtual_5_1",
      "virtual_5_1_to_phalanx_5_1": "virtual_5_1_to_phalanx_5_1",
      "phalanx_5_1_to_virtual_6_1": "phalanx_5_1_to_virtual_6_1",
      "virtual_6_1_to_reverse_phalanx_1": "virtual_6_1_to_reverse_phalanx_1",
      "reverse_phalanx_1_to_virtual_7_1": "reverse_phalanx_1_to_virtual_7_1",
      "virtual_7_1_to_rollover_phalanx_1": "virtual_7_1_to_rollover_phalanx_1",
      "rollover_phalanx_1_to_virtual_8_1": "rollover_phalanx_1_to_virtual_8_1",
      "virtual_8_1_to_phalanx_6_1": "virtual_8_1_to_phalanx_6_1",
      "phalanx_6_1_to_virtual_9_1": "phalanx_6_1_to_virtual_9_1",
      "virtual_9_1_to_distal_phalanx_1": "virtual_9_1_to_distal_phalanx_1",
      "heel_phalanx_2_to_virtual_1_2": "heel_phalanx_2_to_virtual_1_2",
      "virtual_1_2_to_phalanx_1_2": "virtual_1_2_to_phalanx_1_2",
      "phalanx_1_2_to_virtual_2_2": "phalanx_1_2_to_virtual_2_2",
      "virtual_2_2_to_phalanx_2_2": "virtual_2_2_to_phalanx_2_2",
      "phalanx_2_2_to_virtual_3_2": "phalanx_2_2_to_virtual_3_2",
      "virtual_3_2_to_phalanx_3_2": "virtual_3_2_to_phalanx_3_2",
      "phalanx_3_2_to_virtual_4_2": "phalanx_3_2_to_virtual_4_2",
      "virtual_4_2_to_phalanx_4_2": "virtual_4_2_to_phalanx_4_2",
      "phalanx_4_2_to_virtual_5_2": "phalanx_4_2_to_virtual_5_2",
      "virtual_5_2_to_phalanx_5_2": "virtual_5_2_to_phalanx_5_2",
      "phalanx_5_2_to_virtual_6_2": "phalanx_5_2_to_virtual_6_2",
      "virtual_6_2_to_reverse_phalanx_2": "virtual_6_2_to_reverse_phalanx_2",
      "reverse_phalanx_2_to_virtual_7_2": "reverse_phalanx_2_to_virtual_7_2",
      "virtual_7_2_to_rollover_phalanx_2": "virtual_7_2_to_rollover_phalanx_2",
      "rollover_phalanx_2_to_virtual_8_2": "rollover_phalanx_2_to_virtual_8_2",
      "virtual_8_2_to_phalanx_6_2": "virtual_8_2_to_phalanx_6_2",
      "phalanx_6_2_to_virtual_9_2": "phalanx_6_2_to_virtual_9_2",
      "virtual_9_2_to_distal_phalanx_2": "virtual_9_2_to_distal_phalanx_2",
      "heel_phalanx_3_to_virtual_1_3": "heel_phalanx_3_to_virtual_1_3",
      "virtual_1_3_to_phalanx_1_3": "virtual_1_3_to_phalanx_1_3",
      "phalanx_1_3_to_virtual_2_3": "phalanx_1_3_to_virtual_2_3",
      "virtual_2_3_to_phalanx_2_3": "virtual_2_3_to_phalanx_2_3",
      "phalanx_2_3_to_virtual_3_3": "phalanx_2_3_to_virtual_3_3",
      "virtual_3_3_to_phalanx_3_3": "virtual_3_3_to_phalanx_3_3",
      "phalanx_3_3_to_virtual_4_3": "phalanx_3_3_to_virtual_4_3",
      "virtual_4_3_to_phalanx_4_3": "virtual_4_3_to_phalanx_4_3",
      "phalanx_4_3_to_virtual_5_3": "phalanx_4_3_to_virtual_5_3",
      "virtual_5_3_to_phalanx_5_3": "virtual_5_3_to_phalanx_5_3",
      "phalanx_5_3_to_virtual_6_3": "phalanx_5_3_to_virtual_6_3",
      "virtual_6_3_to_reverse_phalanx_3": "virtual_6_3_to_reverse_phalanx_3",
      "reverse_phalanx_3_to_virtual_7_3": "reverse_phalanx_3_to_virtual_7_3",
      "virtual_7_3_to_rollover_phalanx_3": "virtual_7_3_to_rollover_phalanx_3",
      "rollover_phalanx_3_to_virtual_8_3": "rollover_phalanx_3_to_virtual_8_3",
      "virtual_8_3_to_phalanx_6_3": "virtual_8_3_to_phalanx_6_3",
      "phalanx_6_3_to_virtual_9_3": "phalanx_6_3_to_virtual_9_3",
      "virtual_9_3_to_distal_phalanx_3": "virtual_9_3_to_distal_phalanx_3",
      "heel_phalanx_4_to_virtual_1_4": "heel_phalanx_4_to_virtual_1_4",
      "virtual_1_4_to_phalanx_1_4": "virtual_1_4_to_phalanx_1_4",
      "phalanx_1_4_to_virtual_2_4": "phalanx_1_4_to_virtual_2_4",
      "virtual_2_4_to_phalanx_2_4": "virtual_2_4_to_phalanx_2_4",
      "phalanx_2_4_to_virtual_3_4": "phalanx_2_4_to_virtual_3_4",
      "virtual_3_4_to_phalanx_3_4": "virtual_3_4_to_phalanx_3_4",
      "phalanx_3_4_to_virtual_4_4": "phalanx_3_4_to_virtual_4_4",
      "virtual_4_4_to_phalanx_4_4": "virtual_4_4_to_phalanx_4_4",
      "phalanx_4_4_to_virtual_5_4": "phalanx_4_4_to_virtual_5_4",
      "virtual_5_4_to_phalanx_5_4": "virtual_5_4_to_phalanx_5_4",
      "phalanx_5_4_to_virtual_6_4": "phalanx_5_4_to_virtual_6_4",
      "virtual_6_4_to_reverse_phalanx_4": "virtual_6_4_to_reverse_phalanx_4",
      "reverse_phalanx_4_to_virtual_7_4": "reverse_phalanx_4_to_virtual_7_4",
      "virtual_7_4_to_rollover_phalanx_4": "virtual_7_4_to_rollover_phalanx_4",
      "rollover_phalanx_4_to_virtual_8_4": "rollover_phalanx_4_to_virtual_8_4",
      "virtual_8_4_to_phalanx_6_4": "virtual_8_4_to_phalanx_6_4",
      "phalanx_6_4_to_virtual_9_4": "phalanx_6_4_to_virtual_9_4",
      "virtual_9_4_to_distal_phalanx_4": "virtual_9_4_to_distal_phalanx_4",
      "heel_phalanx_5_to_virtual_1_5": "heel_phalanx_5_to_virtual_1_5",
      "virtual_1_5_to_phalanx_1_5": "virtual_1_5_to_phalanx_1_5",
      "phalanx_1_5_to_virtual_2_5": "phalanx_1_5_to_virtual_2_5",
      "virtual_2_5_to_phalanx_2_5": "virtual_2_5_to_phalanx_2_5",
      "phalanx_2_5_to_virtual_3_5": "phalanx_2_5_to_virtual_3_5",
      "virtual_3_5_to_phalanx_3_5": "virtual_3_5_to_phalanx_3_5",
      "phalanx_3_5_to_virtual_4_5": "phalanx_3_5_to_virtual_4_5",
      "virtual_4_5_to_phalanx_4_5": "virtual_4_5_to_phalanx_4_5",
      "phalanx_4_5_to_virtual_5_5": "phalanx_4_5_to_virtual_5_5",
      "virtual_5_5_to_phalanx_5_5": "virtual_5_5_to_phalanx_5_5",
      "phalanx_5_5_to_virtual_6_5": "phalanx_5_5_to_virtual_6_5",
      "virtual_6_5_to_reverse_phalanx_5": "virtual_6_5_to_reverse_phalanx_5",
      "reverse_phalanx_5_to_virtual_7_5": "reverse_phalanx_5_to_virtual_7_5",
      "virtual_7_5_to_rollover_phalanx_5": "virtual_7_5_to_rollover_phalanx_5",
      "rollover_phalanx_5_to_virtual_8_5": "rollover_phalanx_5_to_virtual_8_5",
      "virtual_8_5_to_phalanx_6_5": "virtual_8_5_to_phalanx_6_5",
      "phalanx_6_5_to_virtual_9_5": "phalanx_6_5_to_virtual_9_5",
      "virtual_9_5_to_distal_phalanx_5": "virtual_9_5_to_distal_phalanx_5",
      "cube_to_frontal_arch": "cube_to_frontal_arch"
    },
    "body_methods": {
      "attachment_cube": "name",
      "posterior_arch": "name",
      "heel": "name",
      "phalanx_1_1": "name",
      "phalanx_2_1": "name",
      "phalanx_3_1": "name",
      "phalanx_4_1": "name",
      "phalanx_5_1": "name",
      "reverse_phalanx_1": "name",
      "rollover_phalanx_1": "name",
      "phalanx_6_1": "name",
      "distal_phalanx_1": "name",
      "phalanx_1_2": "name",
      "phalanx_2_2": "name",
      "phalanx_3_2": "name",
      "phalanx_4_2": "name",
      "phalanx_5_2": "name",
      "reverse_phalanx_2": "name",
      "rollover_phalanx_2": "name",
      "phalanx_6_2": "name",
      "distal_phalanx_2": "name",
      "phalanx_1_3": "name",
      "phalanx_2_3": "name",
      "phalanx_3_3": "name",
      "phalanx_4_3": "name",
      "phalanx_5_3": "name",
      "reverse_phalanx_3": "name",
      "rollover_phalanx_3": "name",
      "phalanx_6_3": "name",
      "distal_phalanx_3": "name",
      "phalanx_1_4": "name",
      "phalanx_2_4": "name",
      "phalanx_3_4": "name",
      "phalanx_4_4": "name",
      "phalanx_5_4": "name",
      "reverse_phalanx_4": "name",
      "rollover_phalanx_4": "name",
      "phalanx_6_4": "name",
      "distal_phalanx_4": "name",
      "phalanx_1_5": "name",
      "phalanx_2_5": "name",
      "phalanx_3_5": "name",
      "phalanx_4_5": "name",
      "phalanx_5_5": "name",
      "reverse_phalanx_5": "name",
      "rollover_phalanx_5": "name",
      "phalanx_6_5": "name",
      "distal_phalanx_5": "name",
      "frontal_arch": "name"
    },
    "joint_methods": {
      "posterior_arch_to_heel": "name",
      "heel_phalanx_1_to_virtual_1_1": "name",
      "virtual_1_1_to_phalanx_1_1": "name",
      "phalanx_1_1_to_virtual_2_1": "name",
      "virtual_2_1_to_phalanx_2_1": "name",
      "phalanx_2_1_to_virtual_3_1": "name",
      "virtual_3_1_to_phalanx_3_1": "name",
      "phalanx_3_1_to_virtual_4_1": "name",
      "virtual_4_1_to_phalanx_4_1": "name",
      "phalanx_4_1_to_virtual_5_1": "name",
      "virtual_5_1_to_phalanx_5_1": "name",
      "phalanx_5_1_to_virtual_6_1": "name",
      "virtual_6_1_to_reverse_phalanx_1": "name",
      "reverse_phalanx_1_to_virtual_7_1": "name",
      "virtual_7_1_to_rollover_phalanx_1": "name",
      "rollover_phalanx_1_to_virtual_8_1": "name",
      "virtual_8_1_to_phalanx_6_1": "name",
      "phalanx_6_1_to_virtual_9_1": "name",
      "virtual_9_1_to_distal_phalanx_1": "name",
      "heel_phalanx_2_to_virtual_1_2": "name",
      "virtual_1_2_to_phalanx_1_2": "name",
      "phalanx_1_2_to_virtual_2_2": "name",
      "virtual_2_2_to_phalanx_2_2": "name",
      "phalanx_2_2_to_virtual_3_2": "name",
      "virtual_3_2_to_phalanx_3_2": "name",
      "phalanx_3_2_to_virtual_4_2": "name",
      "virtual_4_2_to_phalanx_4_2": "name",
      "phalanx_4_2_to_virtual_5_2": "name",
      "virtual_5_2_to_phalanx_5_2": "name",
      "phalanx_5_2_to_virtual_6_2": "name",
      "virtual_6_2_to_reverse_phalanx_2": "name",
      "reverse_phalanx_2_to_virtual_7_2": "name",
      "virtual_7_2_to_rollover_phalanx_2": "name",
      "rollover_phalanx_2_to_virtual_8_2": "name",
      "virtual_8_2_to_phalanx_6_2": "name",
      "phalanx_6_2_to_virtual_9_2": "name",
      "virtual_9_2_to_distal_phalanx_2": "name",
      "heel_phalanx_3_to_virtual_1_3": "name",
      "virtual_1_3_to_phalanx_1_3": "name",
      "phalanx_1_3_to_virtual_2_3": "name",
      "virtual_2_3_to_phalanx_2_3": "name",
      "phalanx_2_3_to_virtual_3_3": "name",
      "virtual_3_3_to_phalanx_3_3": "name",
      "phalanx_3_3_to_virtual_4_3": "name",
      "virtual_4_3_to_phalanx_4_3": "name",
      "phalanx_4_3_to_virtual_5_3": "name",
      "virtual_5_3_to_phalanx_5_3": "name",
      "phalanx_5_3_to_virtual_6_3": "name",
      "virtual_6_3_to_reverse_phalanx_3": "name",
      "reverse_phalanx_3_to_virtual_7_3": "name",
      "virtual_7_3_to_rollover_phalanx_3": "name",
      "rollover_phalanx_3_to_virtual_8_3": "name",
      "virtual_8_3_to_phalanx_6_3": "name",
      "phalanx_6_3_to_virtual_9_3": "name",
      "virtual_9_3_to_distal_phalanx_3": "name",
      "heel_phalanx_4_to_virtual_1_4": "name",
      "virtual_1_4_to_phalanx_1_4": "name",
      "phalanx_1_4_to_virtual_2_4": "name",
      "virtual_2_4_to_phalanx_2_4": "name",
      "phalanx_2_4_to_virtual_3_4": "name",
      "virtual_3_4_to_phalanx_3_4": "name",
      "phalanx_3_4_to_virtual_4_4": "name",
      "virtual_4_4_to_phalanx_4_4": "name",
      "phalanx_4_4_to_virtual_5_4": "name",
      "virtual_5_4_to_phalanx_5_4": "name",
      "phalanx_5_4_to_virtual_6_4": "name",
      "virtual_6_4_to_reverse_phalanx_4": "name",
      "reverse_phalanx_4_to_virtual_7_4": "name",
      "virtual_7_4_to_rollover_phalanx_4": "name",
      "rollover_phalanx_4_to_virtual_8_4": "name",
      "virtual_8_4_to_phalanx_6_4": "name",
      "phalanx_6_4_to_virtual_9_4": "name",
      "virtual_9_4_to_distal_phalanx_4": "name",
      "heel_phalanx_5_to_virtual_1_5": "name",
      "virtual_1_5_to_phalanx_1_5": "name",
      "phalanx_1_5_to_virtual_2_5": "name",
      "virtual_2_5_to_phalanx_2_5": "name",
      "phalanx_2_5_to_virtual_3_5": "name",
      "virtual_3_5_to_phalanx_3_5": "name",
      "phalanx_3_5_to_virtual_4_5": "name",
      "virtual_4_5_to_phalanx_4_5": "name",
      "phalanx_4_5_to_virtual_5_5": "name",
      "virtual_5_5_to_phalanx_5_5": "name",
      "phalanx_5_5_to_virtual_6_5": "name",
      "virtual_6_5_to_reverse_phalanx_5": "name",
      "reverse_phalanx_5_to_virtual_7_5": "name",
      "virtual_7_5_to_rollover_phalanx_5": "name",
      "rollover_phalanx_5_to_virtual_8_5": "name",
      "virtual_8_5_to_phalanx_6_5": "name",
      "phalanx_6_5_to_virtual_9_5": "name",
      "virtual_9_5_to_distal_phalanx_5": "name",
      "cube_to_frontal_arch": "name"
    },
    "unmatched_m_bodies": [],
    "unmatched_upstream_bodies": [],
    "unmatched_m_joints": [],
    "unmatched_upstream_joints": [],
    "registration_anchor": {
      "M": "attachment_cube",
      "H": "attachment_cube",
      "root_unmatched": false
    }
  },
  "mapping_s": {
    "bodies": {
      "attachment_cube": "attachment_cube",
      "posterior_arch": "posterior_arch",
      "heel": "heel",
      "phalanx_1_1": "phalanx_1_1",
      "phalanx_2_1": "phalanx_2_1",
      "phalanx_3_1": "phalanx_3_1",
      "phalanx_4_1": "phalanx_4_1",
      "phalanx_5_1": "phalanx_5_1",
      "reverse_phalanx_1": "reverse_phalanx_1",
      "rollover_phalanx_1": "rollover_phalanx_1",
      "phalanx_6_1": "phalanx_6_1",
      "distal_phalanx_1": "distal_phalanx_1",
      "phalanx_1_2": "phalanx_1_2",
      "phalanx_2_2": "phalanx_2_2",
      "phalanx_3_2": "phalanx_3_2",
      "phalanx_4_2": "phalanx_4_2",
      "phalanx_5_2": "phalanx_5_2",
      "reverse_phalanx_2": "reverse_phalanx_2",
      "rollover_phalanx_2": "rollover_phalanx_2",
      "phalanx_6_2": "phalanx_6_2",
      "distal_phalanx_2": "distal_phalanx_2",
      "phalanx_1_3": "phalanx_1_3",
      "phalanx_2_3": "phalanx_2_3",
      "phalanx_3_3": "phalanx_3_3",
      "phalanx_4_3": "phalanx_4_3",
      "phalanx_5_3": "phalanx_5_3",
      "reverse_phalanx_3": "reverse_phalanx_3",
      "rollover_phalanx_3": "rollover_phalanx_3",
      "phalanx_6_3": "phalanx_6_3",
      "distal_phalanx_3": "distal_phalanx_3",
      "phalanx_1_4": "phalanx_1_4",
      "phalanx_2_4": "phalanx_2_4",
      "phalanx_3_4": "phalanx_3_4",
      "phalanx_4_4": "phalanx_4_4",
      "phalanx_5_4": "phalanx_5_4",
      "reverse_phalanx_4": "reverse_phalanx_4",
      "rollover_phalanx_4": "rollover_phalanx_4",
      "phalanx_6_4": "phalanx_6_4",
      "distal_phalanx_4": "distal_phalanx_4",
      "phalanx_1_5": "phalanx_1_5",
      "phalanx_2_5": "phalanx_2_5",
      "phalanx_3_5": "phalanx_3_5",
      "phalanx_4_5": "phalanx_4_5",
      "phalanx_5_5": "phalanx_5_5",
      "reverse_phalanx_5": "reverse_phalanx_5",
      "rollover_phalanx_5": "rollover_phalanx_5",
      "phalanx_6_5": "phalanx_6_5",
      "distal_phalanx_5": "distal_phalanx_5",
      "frontal_arch": "frontal_arch"
    },
    "joints": {
      "posterior_arch_to_heel": "posterior_arch_to_heel",
      "heel_phalanx_1_to_virtual_1_1": "heel_phalanx_1_to_virtual_1_1",
      "virtual_1_1_to_phalanx_1_1": "virtual_1_1_to_phalanx_1_1",
      "phalanx_1_1_to_virtual_2_1": "phalanx_1_1_to_virtual_2_1",
      "virtual_2_1_to_phalanx_2_1": "virtual_2_1_to_phalanx_2_1",
      "phalanx_2_1_to_virtual_3_1": "phalanx_2_1_to_virtual_3_1",
      "virtual_3_1_to_phalanx_3_1": "virtual_3_1_to_phalanx_3_1",
      "phalanx_3_1_to_virtual_4_1": "phalanx_3_1_to_virtual_4_1",
      "virtual_4_1_to_phalanx_4_1": "virtual_4_1_to_phalanx_4_1",
      "phalanx_4_1_to_virtual_5_1": "phalanx_4_1_to_virtual_5_1",
      "virtual_5_1_to_phalanx_5_1": "virtual_5_1_to_phalanx_5_1",
      "phalanx_5_1_to_virtual_6_1": "phalanx_5_1_to_virtual_6_1",
      "virtual_6_1_to_reverse_phalanx_1": "virtual_6_1_to_reverse_phalanx_1",
      "reverse_phalanx_1_to_virtual_7_1": "reverse_phalanx_1_to_virtual_7_1",
      "virtual_7_1_to_rollover_phalanx_1": "virtual_7_1_to_rollover_phalanx_1",
      "rollover_phalanx_1_to_virtual_8_1": "rollover_phalanx_1_to_virtual_8_1",
      "virtual_8_1_to_phalanx_6_1": "virtual_8_1_to_phalanx_6_1",
      "phalanx_6_1_to_virtual_9_1": "phalanx_6_1_to_virtual_9_1",
      "virtual_9_1_to_distal_phalanx_1": "virtual_9_1_to_distal_phalanx_1",
      "heel_phalanx_2_to_virtual_1_2": "heel_phalanx_2_to_virtual_1_2",
      "virtual_1_2_to_phalanx_1_2": "virtual_1_2_to_phalanx_1_2",
      "phalanx_1_2_to_virtual_2_2": "phalanx_1_2_to_virtual_2_2",
      "virtual_2_2_to_phalanx_2_2": "virtual_2_2_to_phalanx_2_2",
      "phalanx_2_2_to_virtual_3_2": "phalanx_2_2_to_virtual_3_2",
      "virtual_3_2_to_phalanx_3_2": "virtual_3_2_to_phalanx_3_2",
      "phalanx_3_2_to_virtual_4_2": "phalanx_3_2_to_virtual_4_2",
      "virtual_4_2_to_phalanx_4_2": "virtual_4_2_to_phalanx_4_2",
      "phalanx_4_2_to_virtual_5_2": "phalanx_4_2_to_virtual_5_2",
      "virtual_5_2_to_phalanx_5_2": "virtual_5_2_to_phalanx_5_2",
      "phalanx_5_2_to_virtual_6_2": "phalanx_5_2_to_virtual_6_2",
      "virtual_6_2_to_reverse_phalanx_2": "virtual_6_2_to_reverse_phalanx_2",
      "reverse_phalanx_2_to_virtual_7_2": "reverse_phalanx_2_to_virtual_7_2",
      "virtual_7_2_to_rollover_phalanx_2": "virtual_7_2_to_rollover_phalanx_2",
      "rollover_phalanx_2_to_virtual_8_2": "rollover_phalanx_2_to_virtual_8_2",
      "virtual_8_2_to_phalanx_6_2": "virtual_8_2_to_phalanx_6_2",
      "phalanx_6_2_to_virtual_9_2": "phalanx_6_2_to_virtual_9_2",
      "virtual_9_2_to_distal_phalanx_2": "virtual_9_2_to_distal_phalanx_2",
      "heel_phalanx_3_to_virtual_1_3": "heel_phalanx_3_to_virtual_1_3",
      "virtual_1_3_to_phalanx_1_3": "virtual_1_3_to_phalanx_1_3",
      "phalanx_1_3_to_virtual_2_3": "phalanx_1_3_to_virtual_2_3",
      "virtual_2_3_to_phalanx_2_3": "virtual_2_3_to_phalanx_2_3",
      "phalanx_2_3_to_virtual_3_3": "phalanx_2_3_to_virtual_3_3",
      "virtual_3_3_to_phalanx_3_3": "virtual_3_3_to_phalanx_3_3",
      "phalanx_3_3_to_virtual_4_3": "phalanx_3_3_to_virtual_4_3",
      "virtual_4_3_to_phalanx_4_3": "virtual_4_3_to_phalanx_4_3",
      "phalanx_4_3_to_virtual_5_3": "phalanx_4_3_to_virtual_5_3",
      "virtual_5_3_to_phalanx_5_3": "virtual_5_3_to_phalanx_5_3",
      "phalanx_5_3_to_virtual_6_3": "phalanx_5_3_to_virtual_6_3",
      "virtual_6_3_to_reverse_phalanx_3": "virtual_6_3_to_reverse_phalanx_3",
      "reverse_phalanx_3_to_virtual_7_3": "reverse_phalanx_3_to_virtual_7_3",
      "virtual_7_3_to_rollover_phalanx_3": "virtual_7_3_to_rollover_phalanx_3",
      "rollover_phalanx_3_to_virtual_8_3": "rollover_phalanx_3_to_virtual_8_3",
      "virtual_8_3_to_phalanx_6_3": "virtual_8_3_to_phalanx_6_3",
      "phalanx_6_3_to_virtual_9_3": "phalanx_6_3_to_virtual_9_3",
      "virtual_9_3_to_distal_phalanx_3": "virtual_9_3_to_distal_phalanx_3",
      "heel_phalanx_4_to_virtual_1_4": "heel_phalanx_4_to_virtual_1_4",
      "virtual_1_4_to_phalanx_1_4": "virtual_1_4_to_phalanx_1_4",
      "phalanx_1_4_to_virtual_2_4": "phalanx_1_4_to_virtual_2_4",
      "virtual_2_4_to_phalanx_2_4": "virtual_2_4_to_phalanx_2_4",
      "phalanx_2_4_to_virtual_3_4": "phalanx_2_4_to_virtual_3_4",
      "virtual_3_4_to_phalanx_3_4": "virtual_3_4_to_phalanx_3_4",
      "phalanx_3_4_to_virtual_4_4": "phalanx_3_4_to_virtual_4_4",
      "virtual_4_4_to_phalanx_4_4": "virtual_4_4_to_phalanx_4_4",
      "phalanx_4_4_to_virtual_5_4": "phalanx_4_4_to_virtual_5_4",
      "virtual_5_4_to_phalanx_5_4": "virtual_5_4_to_phalanx_5_4",
      "phalanx_5_4_to_virtual_6_4": "phalanx_5_4_to_virtual_6_4",
      "virtual_6_4_to_reverse_phalanx_4": "virtual_6_4_to_reverse_phalanx_4",
      "reverse_phalanx_4_to_virtual_7_4": "reverse_phalanx_4_to_virtual_7_4",
      "virtual_7_4_to_rollover_phalanx_4": "virtual_7_4_to_rollover_phalanx_4",
      "rollover_phalanx_4_to_virtual_8_4": "rollover_phalanx_4_to_virtual_8_4",
      "virtual_8_4_to_phalanx_6_4": "virtual_8_4_to_phalanx_6_4",
      "phalanx_6_4_to_virtual_9_4": "phalanx_6_4_to_virtual_9_4",
      "virtual_9_4_to_distal_phalanx_4": "virtual_9_4_to_distal_phalanx_4",
      "heel_phalanx_5_to_virtual_1_5": "heel_phalanx_5_to_virtual_1_5",
      "virtual_1_5_to_phalanx_1_5": "virtual_1_5_to_phalanx_1_5",
      "phalanx_1_5_to_virtual_2_5": "phalanx_1_5_to_virtual_2_5",
      "virtual_2_5_to_phalanx_2_5": "virtual_2_5_to_phalanx_2_5",
      "phalanx_2_5_to_virtual_3_5": "phalanx_2_5_to_virtual_3_5",
      "virtual_3_5_to_phalanx_3_5": "virtual_3_5_to_phalanx_3_5",
      "phalanx_3_5_to_virtual_4_5": "phalanx_3_5_to_virtual_4_5",
      "virtual_4_5_to_phalanx_4_5": "virtual_4_5_to_phalanx_4_5",
      "phalanx_4_5_to_virtual_5_5": "phalanx_4_5_to_virtual_5_5",
      "virtual_5_5_to_phalanx_5_5": "virtual_5_5_to_phalanx_5_5",
      "phalanx_5_5_to_virtual_6_5": "phalanx_5_5_to_virtual_6_5",
      "virtual_6_5_to_reverse_phalanx_5": "virtual_6_5_to_reverse_phalanx_5",
      "reverse_phalanx_5_to_virtual_7_5": "reverse_phalanx_5_to_virtual_7_5",
      "virtual_7_5_to_rollover_phalanx_5": "virtual_7_5_to_rollover_phalanx_5",
      "rollover_phalanx_5_to_virtual_8_5": "rollover_phalanx_5_to_virtual_8_5",
      "virtual_8_5_to_phalanx_6_5": "virtual_8_5_to_phalanx_6_5",
      "phalanx_6_5_to_virtual_9_5": "phalanx_6_5_to_virtual_9_5",
      "virtual_9_5_to_distal_phalanx_5": "virtual_9_5_to_distal_phalanx_5",
      "cube_to_frontal_arch": "cube_to_frontal_arch"
    },
    "body_methods": {
      "attachment_cube": "name",
      "posterior_arch": "name",
      "heel": "name",
      "phalanx_1_1": "name",
      "phalanx_2_1": "name",
      "phalanx_3_1": "name",
      "phalanx_4_1": "name",
      "phalanx_5_1": "name",
      "reverse_phalanx_1": "name",
      "rollover_phalanx_1": "name",
      "phalanx_6_1": "name",
      "distal_phalanx_1": "name",
      "phalanx_1_2": "name",
      "phalanx_2_2": "name",
      "phalanx_3_2": "name",
      "phalanx_4_2": "name",
      "phalanx_5_2": "name",
      "reverse_phalanx_2": "name",
      "rollover_phalanx_2": "name",
      "phalanx_6_2": "name",
      "distal_phalanx_2": "name",
      "phalanx_1_3": "name",
      "phalanx_2_3": "name",
      "phalanx_3_3": "name",
      "phalanx_4_3": "name",
      "phalanx_5_3": "name",
      "reverse_phalanx_3": "name",
      "rollover_phalanx_3": "name",
      "phalanx_6_3": "name",
      "distal_phalanx_3": "name",
      "phalanx_1_4": "name",
      "phalanx_2_4": "name",
      "phalanx_3_4": "name",
      "phalanx_4_4": "name",
      "phalanx_5_4": "name",
      "reverse_phalanx_4": "name",
      "rollover_phalanx_4": "name",
      "phalanx_6_4": "name",
      "distal_phalanx_4": "name",
      "phalanx_1_5": "name",
      "phalanx_2_5": "name",
      "phalanx_3_5": "name",
      "phalanx_4_5": "name",
      "phalanx_5_5": "name",
      "reverse_phalanx_5": "name",
      "rollover_phalanx_5": "name",
      "phalanx_6_5": "name",
      "distal_phalanx_5": "name",
      "frontal_arch": "name"
    },
    "joint_methods": {
      "posterior_arch_to_heel": "name",
      "heel_phalanx_1_to_virtual_1_1": "name",
      "virtual_1_1_to_phalanx_1_1": "name",
      "phalanx_1_1_to_virtual_2_1": "name",
      "virtual_2_1_to_phalanx_2_1": "name",
      "phalanx_2_1_to_virtual_3_1": "name",
      "virtual_3_1_to_phalanx_3_1": "name",
      "phalanx_3_1_to_virtual_4_1": "name",
      "virtual_4_1_to_phalanx_4_1": "name",
      "phalanx_4_1_to_virtual_5_1": "name",
      "virtual_5_1_to_phalanx_5_1": "name",
      "phalanx_5_1_to_virtual_6_1": "name",
      "virtual_6_1_to_reverse_phalanx_1": "name",
      "reverse_phalanx_1_to_virtual_7_1": "name",
      "virtual_7_1_to_rollover_phalanx_1": "name",
      "rollover_phalanx_1_to_virtual_8_1": "name",
      "virtual_8_1_to_phalanx_6_1": "name",
      "phalanx_6_1_to_virtual_9_1": "name",
      "virtual_9_1_to_distal_phalanx_1": "name",
      "heel_phalanx_2_to_virtual_1_2": "name",
      "virtual_1_2_to_phalanx_1_2": "name",
      "phalanx_1_2_to_virtual_2_2": "name",
      "virtual_2_2_to_phalanx_2_2": "name",
      "phalanx_2_2_to_virtual_3_2": "name",
      "virtual_3_2_to_phalanx_3_2": "name",
      "phalanx_3_2_to_virtual_4_2": "name",
      "virtual_4_2_to_phalanx_4_2": "name",
      "phalanx_4_2_to_virtual_5_2": "name",
      "virtual_5_2_to_phalanx_5_2": "name",
      "phalanx_5_2_to_virtual_6_2": "name",
      "virtual_6_2_to_reverse_phalanx_2": "name",
      "reverse_phalanx_2_to_virtual_7_2": "name",
      "virtual_7_2_to_rollover_phalanx_2": "name",
      "rollover_phalanx_2_to_virtual_8_2": "name",
      "virtual_8_2_to_phalanx_6_2": "name",
      "phalanx_6_2_to_virtual_9_2": "name",
      "virtual_9_2_to_distal_phalanx_2": "name",
      "heel_phalanx_3_to_virtual_1_3": "name",
      "virtual_1_3_to_phalanx_1_3": "name",
      "phalanx_1_3_to_virtual_2_3": "name",
      "virtual_2_3_to_phalanx_2_3": "name",
      "phalanx_2_3_to_virtual_3_3": "name",
      "virtual_3_3_to_phalanx_3_3": "name",
      "phalanx_3_3_to_virtual_4_3": "name",
      "virtual_4_3_to_phalanx_4_3": "name",
      "phalanx_4_3_to_virtual_5_3": "name",
      "virtual_5_3_to_phalanx_5_3": "name",
      "phalanx_5_3_to_virtual_6_3": "name",
      "virtual_6_3_to_reverse_phalanx_3": "name",
      "reverse_phalanx_3_to_virtual_7_3": "name",
      "virtual_7_3_to_rollover_phalanx_3": "name",
      "rollover_phalanx_3_to_virtual_8_3": "name",
      "virtual_8_3_to_phalanx_6_3": "name",
      "phalanx_6_3_to_virtual_9_3": "name",
      "virtual_9_3_to_distal_phalanx_3": "name",
      "heel_phalanx_4_to_virtual_1_4": "name",
      "virtual_1_4_to_phalanx_1_4": "name",
      "phalanx_1_4_to_virtual_2_4": "name",
      "virtual_2_4_to_phalanx_2_4": "name",
      "phalanx_2_4_to_virtual_3_4": "name",
      "virtual_3_4_to_phalanx_3_4": "name",
      "phalanx_3_4_to_virtual_4_4": "name",
      "virtual_4_4_to_phalanx_4_4": "name",
      "phalanx_4_4_to_virtual_5_4": "name",
      "virtual_5_4_to_phalanx_5_4": "name",
      "phalanx_5_4_to_virtual_6_4": "name",
      "virtual_6_4_to_reverse_phalanx_4": "name",
      "reverse_phalanx_4_to_virtual_7_4": "name",
      "virtual_7_4_to_rollover_phalanx_4": "name",
      "rollover_phalanx_4_to_virtual_8_4": "name",
      "virtual_8_4_to_phalanx_6_4": "name",
      "phalanx_6_4_to_virtual_9_4": "name",
      "virtual_9_4_to_distal_phalanx_4": "name",
      "heel_phalanx_5_to_virtual_1_5": "name",
      "virtual_1_5_to_phalanx_1_5": "name",
      "phalanx_1_5_to_virtual_2_5": "name",
      "virtual_2_5_to_phalanx_2_5": "name",
      "phalanx_2_5_to_virtual_3_5": "name",
      "virtual_3_5_to_phalanx_3_5": "name",
      "phalanx_3_5_to_virtual_4_5": "name",
      "virtual_4_5_to_phalanx_4_5": "name",
      "phalanx_4_5_to_virtual_5_5": "name",
      "virtual_5_5_to_phalanx_5_5": "name",
      "phalanx_5_5_to_virtual_6_5": "name",
      "virtual_6_5_to_reverse_phalanx_5": "name",
      "reverse_phalanx_5_to_virtual_7_5": "name",
      "virtual_7_5_to_rollover_phalanx_5": "name",
      "rollover_phalanx_5_to_virtual_8_5": "name",
      "virtual_8_5_to_phalanx_6_5": "name",
      "phalanx_6_5_to_virtual_9_5": "name",
      "virtual_9_5_to_distal_phalanx_5": "name",
      "cube_to_frontal_arch": "name"
    },
    "unmatched_m_bodies": [],
    "unmatched_upstream_bodies": [],
    "unmatched_m_joints": [],
    "unmatched_upstream_joints": [],
    "registration_anchor": {
      "M": "attachment_cube",
      "S": "attachment_cube"
    }
  },
  "unavailable": [
    {
      "entity": "posterior_arch_to_heel",
      "other_entity": "posterior_arch_to_heel",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "posterior_arch_to_heel",
      "other_entity": "posterior_arch_to_heel",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "posterior_arch_to_heel",
      "other_entity": "posterior_arch_to_heel",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "heel_phalanx_1_to_virtual_1_1",
      "other_entity": "heel_phalanx_1_to_virtual_1_1",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "heel_phalanx_1_to_virtual_1_1",
      "other_entity": "heel_phalanx_1_to_virtual_1_1",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "heel_phalanx_1_to_virtual_1_1",
      "other_entity": "heel_phalanx_1_to_virtual_1_1",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "virtual_1_1_to_phalanx_1_1",
      "other_entity": "virtual_1_1_to_phalanx_1_1",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "virtual_1_1_to_phalanx_1_1",
      "other_entity": "virtual_1_1_to_phalanx_1_1",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "virtual_1_1_to_phalanx_1_1",
      "other_entity": "virtual_1_1_to_phalanx_1_1",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "phalanx_1_1_to_virtual_2_1",
      "other_entity": "phalanx_1_1_to_virtual_2_1",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "phalanx_1_1_to_virtual_2_1",
      "other_entity": "phalanx_1_1_to_virtual_2_1",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "phalanx_1_1_to_virtual_2_1",
      "other_entity": "phalanx_1_1_to_virtual_2_1",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "virtual_2_1_to_phalanx_2_1",
      "other_entity": "virtual_2_1_to_phalanx_2_1",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "virtual_2_1_to_phalanx_2_1",
      "other_entity": "virtual_2_1_to_phalanx_2_1",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "virtual_2_1_to_phalanx_2_1",
      "other_entity": "virtual_2_1_to_phalanx_2_1",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "phalanx_2_1_to_virtual_3_1",
      "other_entity": "phalanx_2_1_to_virtual_3_1",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "phalanx_2_1_to_virtual_3_1",
      "other_entity": "phalanx_2_1_to_virtual_3_1",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "phalanx_2_1_to_virtual_3_1",
      "other_entity": "phalanx_2_1_to_virtual_3_1",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "virtual_3_1_to_phalanx_3_1",
      "other_entity": "virtual_3_1_to_phalanx_3_1",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "virtual_3_1_to_phalanx_3_1",
      "other_entity": "virtual_3_1_to_phalanx_3_1",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "virtual_3_1_to_phalanx_3_1",
      "other_entity": "virtual_3_1_to_phalanx_3_1",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "phalanx_3_1_to_virtual_4_1",
      "other_entity": "phalanx_3_1_to_virtual_4_1",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "phalanx_3_1_to_virtual_4_1",
      "other_entity": "phalanx_3_1_to_virtual_4_1",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "phalanx_3_1_to_virtual_4_1",
      "other_entity": "phalanx_3_1_to_virtual_4_1",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "virtual_4_1_to_phalanx_4_1",
      "other_entity": "virtual_4_1_to_phalanx_4_1",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "virtual_4_1_to_phalanx_4_1",
      "other_entity": "virtual_4_1_to_phalanx_4_1",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "virtual_4_1_to_phalanx_4_1",
      "other_entity": "virtual_4_1_to_phalanx_4_1",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "phalanx_4_1_to_virtual_5_1",
      "other_entity": "phalanx_4_1_to_virtual_5_1",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "phalanx_4_1_to_virtual_5_1",
      "other_entity": "phalanx_4_1_to_virtual_5_1",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "phalanx_4_1_to_virtual_5_1",
      "other_entity": "phalanx_4_1_to_virtual_5_1",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "virtual_5_1_to_phalanx_5_1",
      "other_entity": "virtual_5_1_to_phalanx_5_1",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "virtual_5_1_to_phalanx_5_1",
      "other_entity": "virtual_5_1_to_phalanx_5_1",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "virtual_5_1_to_phalanx_5_1",
      "other_entity": "virtual_5_1_to_phalanx_5_1",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "phalanx_5_1_to_virtual_6_1",
      "other_entity": "phalanx_5_1_to_virtual_6_1",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "phalanx_5_1_to_virtual_6_1",
      "other_entity": "phalanx_5_1_to_virtual_6_1",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "phalanx_5_1_to_virtual_6_1",
      "other_entity": "phalanx_5_1_to_virtual_6_1",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "virtual_6_1_to_reverse_phalanx_1",
      "other_entity": "virtual_6_1_to_reverse_phalanx_1",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "virtual_6_1_to_reverse_phalanx_1",
      "other_entity": "virtual_6_1_to_reverse_phalanx_1",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "virtual_6_1_to_reverse_phalanx_1",
      "other_entity": "virtual_6_1_to_reverse_phalanx_1",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "reverse_phalanx_1_to_virtual_7_1",
      "other_entity": "reverse_phalanx_1_to_virtual_7_1",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "reverse_phalanx_1_to_virtual_7_1",
      "other_entity": "reverse_phalanx_1_to_virtual_7_1",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "reverse_phalanx_1_to_virtual_7_1",
      "other_entity": "reverse_phalanx_1_to_virtual_7_1",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "virtual_7_1_to_rollover_phalanx_1",
      "other_entity": "virtual_7_1_to_rollover_phalanx_1",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "virtual_7_1_to_rollover_phalanx_1",
      "other_entity": "virtual_7_1_to_rollover_phalanx_1",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "virtual_7_1_to_rollover_phalanx_1",
      "other_entity": "virtual_7_1_to_rollover_phalanx_1",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "rollover_phalanx_1_to_virtual_8_1",
      "other_entity": "rollover_phalanx_1_to_virtual_8_1",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "rollover_phalanx_1_to_virtual_8_1",
      "other_entity": "rollover_phalanx_1_to_virtual_8_1",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "rollover_phalanx_1_to_virtual_8_1",
      "other_entity": "rollover_phalanx_1_to_virtual_8_1",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "virtual_8_1_to_phalanx_6_1",
      "other_entity": "virtual_8_1_to_phalanx_6_1",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "virtual_8_1_to_phalanx_6_1",
      "other_entity": "virtual_8_1_to_phalanx_6_1",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "virtual_8_1_to_phalanx_6_1",
      "other_entity": "virtual_8_1_to_phalanx_6_1",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "phalanx_6_1_to_virtual_9_1",
      "other_entity": "phalanx_6_1_to_virtual_9_1",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "phalanx_6_1_to_virtual_9_1",
      "other_entity": "phalanx_6_1_to_virtual_9_1",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "phalanx_6_1_to_virtual_9_1",
      "other_entity": "phalanx_6_1_to_virtual_9_1",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "virtual_9_1_to_distal_phalanx_1",
      "other_entity": "virtual_9_1_to_distal_phalanx_1",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "virtual_9_1_to_distal_phalanx_1",
      "other_entity": "virtual_9_1_to_distal_phalanx_1",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "virtual_9_1_to_distal_phalanx_1",
      "other_entity": "virtual_9_1_to_distal_phalanx_1",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "heel_phalanx_2_to_virtual_1_2",
      "other_entity": "heel_phalanx_2_to_virtual_1_2",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "heel_phalanx_2_to_virtual_1_2",
      "other_entity": "heel_phalanx_2_to_virtual_1_2",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "heel_phalanx_2_to_virtual_1_2",
      "other_entity": "heel_phalanx_2_to_virtual_1_2",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "virtual_1_2_to_phalanx_1_2",
      "other_entity": "virtual_1_2_to_phalanx_1_2",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "virtual_1_2_to_phalanx_1_2",
      "other_entity": "virtual_1_2_to_phalanx_1_2",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "virtual_1_2_to_phalanx_1_2",
      "other_entity": "virtual_1_2_to_phalanx_1_2",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "phalanx_1_2_to_virtual_2_2",
      "other_entity": "phalanx_1_2_to_virtual_2_2",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "phalanx_1_2_to_virtual_2_2",
      "other_entity": "phalanx_1_2_to_virtual_2_2",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "phalanx_1_2_to_virtual_2_2",
      "other_entity": "phalanx_1_2_to_virtual_2_2",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "virtual_2_2_to_phalanx_2_2",
      "other_entity": "virtual_2_2_to_phalanx_2_2",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "virtual_2_2_to_phalanx_2_2",
      "other_entity": "virtual_2_2_to_phalanx_2_2",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "virtual_2_2_to_phalanx_2_2",
      "other_entity": "virtual_2_2_to_phalanx_2_2",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "phalanx_2_2_to_virtual_3_2",
      "other_entity": "phalanx_2_2_to_virtual_3_2",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "phalanx_2_2_to_virtual_3_2",
      "other_entity": "phalanx_2_2_to_virtual_3_2",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "phalanx_2_2_to_virtual_3_2",
      "other_entity": "phalanx_2_2_to_virtual_3_2",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "virtual_3_2_to_phalanx_3_2",
      "other_entity": "virtual_3_2_to_phalanx_3_2",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "virtual_3_2_to_phalanx_3_2",
      "other_entity": "virtual_3_2_to_phalanx_3_2",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "virtual_3_2_to_phalanx_3_2",
      "other_entity": "virtual_3_2_to_phalanx_3_2",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "phalanx_3_2_to_virtual_4_2",
      "other_entity": "phalanx_3_2_to_virtual_4_2",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "phalanx_3_2_to_virtual_4_2",
      "other_entity": "phalanx_3_2_to_virtual_4_2",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "phalanx_3_2_to_virtual_4_2",
      "other_entity": "phalanx_3_2_to_virtual_4_2",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "virtual_4_2_to_phalanx_4_2",
      "other_entity": "virtual_4_2_to_phalanx_4_2",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "virtual_4_2_to_phalanx_4_2",
      "other_entity": "virtual_4_2_to_phalanx_4_2",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "virtual_4_2_to_phalanx_4_2",
      "other_entity": "virtual_4_2_to_phalanx_4_2",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "phalanx_4_2_to_virtual_5_2",
      "other_entity": "phalanx_4_2_to_virtual_5_2",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "phalanx_4_2_to_virtual_5_2",
      "other_entity": "phalanx_4_2_to_virtual_5_2",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "phalanx_4_2_to_virtual_5_2",
      "other_entity": "phalanx_4_2_to_virtual_5_2",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "virtual_5_2_to_phalanx_5_2",
      "other_entity": "virtual_5_2_to_phalanx_5_2",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "virtual_5_2_to_phalanx_5_2",
      "other_entity": "virtual_5_2_to_phalanx_5_2",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "virtual_5_2_to_phalanx_5_2",
      "other_entity": "virtual_5_2_to_phalanx_5_2",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "phalanx_5_2_to_virtual_6_2",
      "other_entity": "phalanx_5_2_to_virtual_6_2",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "phalanx_5_2_to_virtual_6_2",
      "other_entity": "phalanx_5_2_to_virtual_6_2",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "phalanx_5_2_to_virtual_6_2",
      "other_entity": "phalanx_5_2_to_virtual_6_2",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "virtual_6_2_to_reverse_phalanx_2",
      "other_entity": "virtual_6_2_to_reverse_phalanx_2",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "virtual_6_2_to_reverse_phalanx_2",
      "other_entity": "virtual_6_2_to_reverse_phalanx_2",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "virtual_6_2_to_reverse_phalanx_2",
      "other_entity": "virtual_6_2_to_reverse_phalanx_2",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "reverse_phalanx_2_to_virtual_7_2",
      "other_entity": "reverse_phalanx_2_to_virtual_7_2",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "reverse_phalanx_2_to_virtual_7_2",
      "other_entity": "reverse_phalanx_2_to_virtual_7_2",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "reverse_phalanx_2_to_virtual_7_2",
      "other_entity": "reverse_phalanx_2_to_virtual_7_2",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "virtual_7_2_to_rollover_phalanx_2",
      "other_entity": "virtual_7_2_to_rollover_phalanx_2",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "virtual_7_2_to_rollover_phalanx_2",
      "other_entity": "virtual_7_2_to_rollover_phalanx_2",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "virtual_7_2_to_rollover_phalanx_2",
      "other_entity": "virtual_7_2_to_rollover_phalanx_2",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "rollover_phalanx_2_to_virtual_8_2",
      "other_entity": "rollover_phalanx_2_to_virtual_8_2",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "rollover_phalanx_2_to_virtual_8_2",
      "other_entity": "rollover_phalanx_2_to_virtual_8_2",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "rollover_phalanx_2_to_virtual_8_2",
      "other_entity": "rollover_phalanx_2_to_virtual_8_2",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "virtual_8_2_to_phalanx_6_2",
      "other_entity": "virtual_8_2_to_phalanx_6_2",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "virtual_8_2_to_phalanx_6_2",
      "other_entity": "virtual_8_2_to_phalanx_6_2",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "virtual_8_2_to_phalanx_6_2",
      "other_entity": "virtual_8_2_to_phalanx_6_2",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "phalanx_6_2_to_virtual_9_2",
      "other_entity": "phalanx_6_2_to_virtual_9_2",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "phalanx_6_2_to_virtual_9_2",
      "other_entity": "phalanx_6_2_to_virtual_9_2",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "phalanx_6_2_to_virtual_9_2",
      "other_entity": "phalanx_6_2_to_virtual_9_2",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "virtual_9_2_to_distal_phalanx_2",
      "other_entity": "virtual_9_2_to_distal_phalanx_2",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "virtual_9_2_to_distal_phalanx_2",
      "other_entity": "virtual_9_2_to_distal_phalanx_2",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "virtual_9_2_to_distal_phalanx_2",
      "other_entity": "virtual_9_2_to_distal_phalanx_2",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "heel_phalanx_3_to_virtual_1_3",
      "other_entity": "heel_phalanx_3_to_virtual_1_3",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "heel_phalanx_3_to_virtual_1_3",
      "other_entity": "heel_phalanx_3_to_virtual_1_3",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "heel_phalanx_3_to_virtual_1_3",
      "other_entity": "heel_phalanx_3_to_virtual_1_3",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "virtual_1_3_to_phalanx_1_3",
      "other_entity": "virtual_1_3_to_phalanx_1_3",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "virtual_1_3_to_phalanx_1_3",
      "other_entity": "virtual_1_3_to_phalanx_1_3",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "virtual_1_3_to_phalanx_1_3",
      "other_entity": "virtual_1_3_to_phalanx_1_3",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "phalanx_1_3_to_virtual_2_3",
      "other_entity": "phalanx_1_3_to_virtual_2_3",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "phalanx_1_3_to_virtual_2_3",
      "other_entity": "phalanx_1_3_to_virtual_2_3",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "phalanx_1_3_to_virtual_2_3",
      "other_entity": "phalanx_1_3_to_virtual_2_3",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "virtual_2_3_to_phalanx_2_3",
      "other_entity": "virtual_2_3_to_phalanx_2_3",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "virtual_2_3_to_phalanx_2_3",
      "other_entity": "virtual_2_3_to_phalanx_2_3",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "virtual_2_3_to_phalanx_2_3",
      "other_entity": "virtual_2_3_to_phalanx_2_3",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "phalanx_2_3_to_virtual_3_3",
      "other_entity": "phalanx_2_3_to_virtual_3_3",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "phalanx_2_3_to_virtual_3_3",
      "other_entity": "phalanx_2_3_to_virtual_3_3",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "phalanx_2_3_to_virtual_3_3",
      "other_entity": "phalanx_2_3_to_virtual_3_3",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "virtual_3_3_to_phalanx_3_3",
      "other_entity": "virtual_3_3_to_phalanx_3_3",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "virtual_3_3_to_phalanx_3_3",
      "other_entity": "virtual_3_3_to_phalanx_3_3",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "virtual_3_3_to_phalanx_3_3",
      "other_entity": "virtual_3_3_to_phalanx_3_3",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "phalanx_3_3_to_virtual_4_3",
      "other_entity": "phalanx_3_3_to_virtual_4_3",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "phalanx_3_3_to_virtual_4_3",
      "other_entity": "phalanx_3_3_to_virtual_4_3",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "phalanx_3_3_to_virtual_4_3",
      "other_entity": "phalanx_3_3_to_virtual_4_3",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "virtual_4_3_to_phalanx_4_3",
      "other_entity": "virtual_4_3_to_phalanx_4_3",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "virtual_4_3_to_phalanx_4_3",
      "other_entity": "virtual_4_3_to_phalanx_4_3",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "virtual_4_3_to_phalanx_4_3",
      "other_entity": "virtual_4_3_to_phalanx_4_3",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "phalanx_4_3_to_virtual_5_3",
      "other_entity": "phalanx_4_3_to_virtual_5_3",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "phalanx_4_3_to_virtual_5_3",
      "other_entity": "phalanx_4_3_to_virtual_5_3",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "phalanx_4_3_to_virtual_5_3",
      "other_entity": "phalanx_4_3_to_virtual_5_3",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "virtual_5_3_to_phalanx_5_3",
      "other_entity": "virtual_5_3_to_phalanx_5_3",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "virtual_5_3_to_phalanx_5_3",
      "other_entity": "virtual_5_3_to_phalanx_5_3",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "virtual_5_3_to_phalanx_5_3",
      "other_entity": "virtual_5_3_to_phalanx_5_3",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "phalanx_5_3_to_virtual_6_3",
      "other_entity": "phalanx_5_3_to_virtual_6_3",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "phalanx_5_3_to_virtual_6_3",
      "other_entity": "phalanx_5_3_to_virtual_6_3",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "phalanx_5_3_to_virtual_6_3",
      "other_entity": "phalanx_5_3_to_virtual_6_3",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "virtual_6_3_to_reverse_phalanx_3",
      "other_entity": "virtual_6_3_to_reverse_phalanx_3",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "virtual_6_3_to_reverse_phalanx_3",
      "other_entity": "virtual_6_3_to_reverse_phalanx_3",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "virtual_6_3_to_reverse_phalanx_3",
      "other_entity": "virtual_6_3_to_reverse_phalanx_3",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "reverse_phalanx_3_to_virtual_7_3",
      "other_entity": "reverse_phalanx_3_to_virtual_7_3",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "reverse_phalanx_3_to_virtual_7_3",
      "other_entity": "reverse_phalanx_3_to_virtual_7_3",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "reverse_phalanx_3_to_virtual_7_3",
      "other_entity": "reverse_phalanx_3_to_virtual_7_3",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "virtual_7_3_to_rollover_phalanx_3",
      "other_entity": "virtual_7_3_to_rollover_phalanx_3",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "virtual_7_3_to_rollover_phalanx_3",
      "other_entity": "virtual_7_3_to_rollover_phalanx_3",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "virtual_7_3_to_rollover_phalanx_3",
      "other_entity": "virtual_7_3_to_rollover_phalanx_3",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "rollover_phalanx_3_to_virtual_8_3",
      "other_entity": "rollover_phalanx_3_to_virtual_8_3",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "rollover_phalanx_3_to_virtual_8_3",
      "other_entity": "rollover_phalanx_3_to_virtual_8_3",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "rollover_phalanx_3_to_virtual_8_3",
      "other_entity": "rollover_phalanx_3_to_virtual_8_3",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "virtual_8_3_to_phalanx_6_3",
      "other_entity": "virtual_8_3_to_phalanx_6_3",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "virtual_8_3_to_phalanx_6_3",
      "other_entity": "virtual_8_3_to_phalanx_6_3",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "virtual_8_3_to_phalanx_6_3",
      "other_entity": "virtual_8_3_to_phalanx_6_3",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "phalanx_6_3_to_virtual_9_3",
      "other_entity": "phalanx_6_3_to_virtual_9_3",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "phalanx_6_3_to_virtual_9_3",
      "other_entity": "phalanx_6_3_to_virtual_9_3",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "phalanx_6_3_to_virtual_9_3",
      "other_entity": "phalanx_6_3_to_virtual_9_3",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "virtual_9_3_to_distal_phalanx_3",
      "other_entity": "virtual_9_3_to_distal_phalanx_3",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "virtual_9_3_to_distal_phalanx_3",
      "other_entity": "virtual_9_3_to_distal_phalanx_3",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "virtual_9_3_to_distal_phalanx_3",
      "other_entity": "virtual_9_3_to_distal_phalanx_3",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "heel_phalanx_4_to_virtual_1_4",
      "other_entity": "heel_phalanx_4_to_virtual_1_4",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "heel_phalanx_4_to_virtual_1_4",
      "other_entity": "heel_phalanx_4_to_virtual_1_4",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "heel_phalanx_4_to_virtual_1_4",
      "other_entity": "heel_phalanx_4_to_virtual_1_4",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "virtual_1_4_to_phalanx_1_4",
      "other_entity": "virtual_1_4_to_phalanx_1_4",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "virtual_1_4_to_phalanx_1_4",
      "other_entity": "virtual_1_4_to_phalanx_1_4",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "virtual_1_4_to_phalanx_1_4",
      "other_entity": "virtual_1_4_to_phalanx_1_4",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "phalanx_1_4_to_virtual_2_4",
      "other_entity": "phalanx_1_4_to_virtual_2_4",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "phalanx_1_4_to_virtual_2_4",
      "other_entity": "phalanx_1_4_to_virtual_2_4",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "phalanx_1_4_to_virtual_2_4",
      "other_entity": "phalanx_1_4_to_virtual_2_4",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "virtual_2_4_to_phalanx_2_4",
      "other_entity": "virtual_2_4_to_phalanx_2_4",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "virtual_2_4_to_phalanx_2_4",
      "other_entity": "virtual_2_4_to_phalanx_2_4",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "virtual_2_4_to_phalanx_2_4",
      "other_entity": "virtual_2_4_to_phalanx_2_4",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "phalanx_2_4_to_virtual_3_4",
      "other_entity": "phalanx_2_4_to_virtual_3_4",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "phalanx_2_4_to_virtual_3_4",
      "other_entity": "phalanx_2_4_to_virtual_3_4",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "phalanx_2_4_to_virtual_3_4",
      "other_entity": "phalanx_2_4_to_virtual_3_4",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "virtual_3_4_to_phalanx_3_4",
      "other_entity": "virtual_3_4_to_phalanx_3_4",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "virtual_3_4_to_phalanx_3_4",
      "other_entity": "virtual_3_4_to_phalanx_3_4",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "virtual_3_4_to_phalanx_3_4",
      "other_entity": "virtual_3_4_to_phalanx_3_4",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "phalanx_3_4_to_virtual_4_4",
      "other_entity": "phalanx_3_4_to_virtual_4_4",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "phalanx_3_4_to_virtual_4_4",
      "other_entity": "phalanx_3_4_to_virtual_4_4",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "phalanx_3_4_to_virtual_4_4",
      "other_entity": "phalanx_3_4_to_virtual_4_4",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "virtual_4_4_to_phalanx_4_4",
      "other_entity": "virtual_4_4_to_phalanx_4_4",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "virtual_4_4_to_phalanx_4_4",
      "other_entity": "virtual_4_4_to_phalanx_4_4",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "virtual_4_4_to_phalanx_4_4",
      "other_entity": "virtual_4_4_to_phalanx_4_4",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "phalanx_4_4_to_virtual_5_4",
      "other_entity": "phalanx_4_4_to_virtual_5_4",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "phalanx_4_4_to_virtual_5_4",
      "other_entity": "phalanx_4_4_to_virtual_5_4",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "phalanx_4_4_to_virtual_5_4",
      "other_entity": "phalanx_4_4_to_virtual_5_4",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "virtual_5_4_to_phalanx_5_4",
      "other_entity": "virtual_5_4_to_phalanx_5_4",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "virtual_5_4_to_phalanx_5_4",
      "other_entity": "virtual_5_4_to_phalanx_5_4",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "virtual_5_4_to_phalanx_5_4",
      "other_entity": "virtual_5_4_to_phalanx_5_4",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "phalanx_5_4_to_virtual_6_4",
      "other_entity": "phalanx_5_4_to_virtual_6_4",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "phalanx_5_4_to_virtual_6_4",
      "other_entity": "phalanx_5_4_to_virtual_6_4",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "phalanx_5_4_to_virtual_6_4",
      "other_entity": "phalanx_5_4_to_virtual_6_4",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "virtual_6_4_to_reverse_phalanx_4",
      "other_entity": "virtual_6_4_to_reverse_phalanx_4",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "virtual_6_4_to_reverse_phalanx_4",
      "other_entity": "virtual_6_4_to_reverse_phalanx_4",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "virtual_6_4_to_reverse_phalanx_4",
      "other_entity": "virtual_6_4_to_reverse_phalanx_4",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "reverse_phalanx_4_to_virtual_7_4",
      "other_entity": "reverse_phalanx_4_to_virtual_7_4",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "reverse_phalanx_4_to_virtual_7_4",
      "other_entity": "reverse_phalanx_4_to_virtual_7_4",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "reverse_phalanx_4_to_virtual_7_4",
      "other_entity": "reverse_phalanx_4_to_virtual_7_4",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "virtual_7_4_to_rollover_phalanx_4",
      "other_entity": "virtual_7_4_to_rollover_phalanx_4",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "virtual_7_4_to_rollover_phalanx_4",
      "other_entity": "virtual_7_4_to_rollover_phalanx_4",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "virtual_7_4_to_rollover_phalanx_4",
      "other_entity": "virtual_7_4_to_rollover_phalanx_4",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "rollover_phalanx_4_to_virtual_8_4",
      "other_entity": "rollover_phalanx_4_to_virtual_8_4",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "rollover_phalanx_4_to_virtual_8_4",
      "other_entity": "rollover_phalanx_4_to_virtual_8_4",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "rollover_phalanx_4_to_virtual_8_4",
      "other_entity": "rollover_phalanx_4_to_virtual_8_4",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "virtual_8_4_to_phalanx_6_4",
      "other_entity": "virtual_8_4_to_phalanx_6_4",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "virtual_8_4_to_phalanx_6_4",
      "other_entity": "virtual_8_4_to_phalanx_6_4",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "virtual_8_4_to_phalanx_6_4",
      "other_entity": "virtual_8_4_to_phalanx_6_4",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "phalanx_6_4_to_virtual_9_4",
      "other_entity": "phalanx_6_4_to_virtual_9_4",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "phalanx_6_4_to_virtual_9_4",
      "other_entity": "phalanx_6_4_to_virtual_9_4",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "phalanx_6_4_to_virtual_9_4",
      "other_entity": "phalanx_6_4_to_virtual_9_4",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "virtual_9_4_to_distal_phalanx_4",
      "other_entity": "virtual_9_4_to_distal_phalanx_4",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "virtual_9_4_to_distal_phalanx_4",
      "other_entity": "virtual_9_4_to_distal_phalanx_4",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "virtual_9_4_to_distal_phalanx_4",
      "other_entity": "virtual_9_4_to_distal_phalanx_4",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "heel_phalanx_5_to_virtual_1_5",
      "other_entity": "heel_phalanx_5_to_virtual_1_5",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "heel_phalanx_5_to_virtual_1_5",
      "other_entity": "heel_phalanx_5_to_virtual_1_5",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "heel_phalanx_5_to_virtual_1_5",
      "other_entity": "heel_phalanx_5_to_virtual_1_5",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "virtual_1_5_to_phalanx_1_5",
      "other_entity": "virtual_1_5_to_phalanx_1_5",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "virtual_1_5_to_phalanx_1_5",
      "other_entity": "virtual_1_5_to_phalanx_1_5",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "virtual_1_5_to_phalanx_1_5",
      "other_entity": "virtual_1_5_to_phalanx_1_5",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "phalanx_1_5_to_virtual_2_5",
      "other_entity": "phalanx_1_5_to_virtual_2_5",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "phalanx_1_5_to_virtual_2_5",
      "other_entity": "phalanx_1_5_to_virtual_2_5",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "phalanx_1_5_to_virtual_2_5",
      "other_entity": "phalanx_1_5_to_virtual_2_5",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "virtual_2_5_to_phalanx_2_5",
      "other_entity": "virtual_2_5_to_phalanx_2_5",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "virtual_2_5_to_phalanx_2_5",
      "other_entity": "virtual_2_5_to_phalanx_2_5",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "virtual_2_5_to_phalanx_2_5",
      "other_entity": "virtual_2_5_to_phalanx_2_5",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "phalanx_2_5_to_virtual_3_5",
      "other_entity": "phalanx_2_5_to_virtual_3_5",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "phalanx_2_5_to_virtual_3_5",
      "other_entity": "phalanx_2_5_to_virtual_3_5",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "phalanx_2_5_to_virtual_3_5",
      "other_entity": "phalanx_2_5_to_virtual_3_5",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "virtual_3_5_to_phalanx_3_5",
      "other_entity": "virtual_3_5_to_phalanx_3_5",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "virtual_3_5_to_phalanx_3_5",
      "other_entity": "virtual_3_5_to_phalanx_3_5",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "virtual_3_5_to_phalanx_3_5",
      "other_entity": "virtual_3_5_to_phalanx_3_5",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "phalanx_3_5_to_virtual_4_5",
      "other_entity": "phalanx_3_5_to_virtual_4_5",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "phalanx_3_5_to_virtual_4_5",
      "other_entity": "phalanx_3_5_to_virtual_4_5",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "phalanx_3_5_to_virtual_4_5",
      "other_entity": "phalanx_3_5_to_virtual_4_5",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "virtual_4_5_to_phalanx_4_5",
      "other_entity": "virtual_4_5_to_phalanx_4_5",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "virtual_4_5_to_phalanx_4_5",
      "other_entity": "virtual_4_5_to_phalanx_4_5",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "virtual_4_5_to_phalanx_4_5",
      "other_entity": "virtual_4_5_to_phalanx_4_5",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "phalanx_4_5_to_virtual_5_5",
      "other_entity": "phalanx_4_5_to_virtual_5_5",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "phalanx_4_5_to_virtual_5_5",
      "other_entity": "phalanx_4_5_to_virtual_5_5",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "phalanx_4_5_to_virtual_5_5",
      "other_entity": "phalanx_4_5_to_virtual_5_5",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "virtual_5_5_to_phalanx_5_5",
      "other_entity": "virtual_5_5_to_phalanx_5_5",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "virtual_5_5_to_phalanx_5_5",
      "other_entity": "virtual_5_5_to_phalanx_5_5",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "virtual_5_5_to_phalanx_5_5",
      "other_entity": "virtual_5_5_to_phalanx_5_5",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "phalanx_5_5_to_virtual_6_5",
      "other_entity": "phalanx_5_5_to_virtual_6_5",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "phalanx_5_5_to_virtual_6_5",
      "other_entity": "phalanx_5_5_to_virtual_6_5",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "phalanx_5_5_to_virtual_6_5",
      "other_entity": "phalanx_5_5_to_virtual_6_5",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "virtual_6_5_to_reverse_phalanx_5",
      "other_entity": "virtual_6_5_to_reverse_phalanx_5",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "virtual_6_5_to_reverse_phalanx_5",
      "other_entity": "virtual_6_5_to_reverse_phalanx_5",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "virtual_6_5_to_reverse_phalanx_5",
      "other_entity": "virtual_6_5_to_reverse_phalanx_5",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "reverse_phalanx_5_to_virtual_7_5",
      "other_entity": "reverse_phalanx_5_to_virtual_7_5",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "reverse_phalanx_5_to_virtual_7_5",
      "other_entity": "reverse_phalanx_5_to_virtual_7_5",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "reverse_phalanx_5_to_virtual_7_5",
      "other_entity": "reverse_phalanx_5_to_virtual_7_5",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "virtual_7_5_to_rollover_phalanx_5",
      "other_entity": "virtual_7_5_to_rollover_phalanx_5",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "virtual_7_5_to_rollover_phalanx_5",
      "other_entity": "virtual_7_5_to_rollover_phalanx_5",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "virtual_7_5_to_rollover_phalanx_5",
      "other_entity": "virtual_7_5_to_rollover_phalanx_5",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "rollover_phalanx_5_to_virtual_8_5",
      "other_entity": "rollover_phalanx_5_to_virtual_8_5",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "rollover_phalanx_5_to_virtual_8_5",
      "other_entity": "rollover_phalanx_5_to_virtual_8_5",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "rollover_phalanx_5_to_virtual_8_5",
      "other_entity": "rollover_phalanx_5_to_virtual_8_5",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "virtual_8_5_to_phalanx_6_5",
      "other_entity": "virtual_8_5_to_phalanx_6_5",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "virtual_8_5_to_phalanx_6_5",
      "other_entity": "virtual_8_5_to_phalanx_6_5",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "virtual_8_5_to_phalanx_6_5",
      "other_entity": "virtual_8_5_to_phalanx_6_5",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "phalanx_6_5_to_virtual_9_5",
      "other_entity": "phalanx_6_5_to_virtual_9_5",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "phalanx_6_5_to_virtual_9_5",
      "other_entity": "phalanx_6_5_to_virtual_9_5",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "phalanx_6_5_to_virtual_9_5",
      "other_entity": "phalanx_6_5_to_virtual_9_5",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "virtual_9_5_to_distal_phalanx_5",
      "other_entity": "virtual_9_5_to_distal_phalanx_5",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "virtual_9_5_to_distal_phalanx_5",
      "other_entity": "virtual_9_5_to_distal_phalanx_5",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "virtual_9_5_to_distal_phalanx_5",
      "other_entity": "virtual_9_5_to_distal_phalanx_5",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "cube_to_frontal_arch",
      "other_entity": "cube_to_frontal_arch",
      "quantity": "range",
      "tolerance": "range",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "cube_to_frontal_arch",
      "other_entity": "cube_to_frontal_arch",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "cube_to_frontal_arch",
      "other_entity": "cube_to_frontal_arch",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "cube_to_frontal_arch",
      "other_entity": "cube_to_frontal_arch",
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
| posterior_arch_to_heel / effort | unavailable | unavailable | unavailable |
| posterior_arch_to_heel / force | unavailable | unavailable | unavailable |
| posterior_arch_to_heel / velocity | unavailable | unavailable | unavailable |
| heel_phalanx_1_to_virtual_1_1 / effort | unavailable | unavailable | unavailable |
| heel_phalanx_1_to_virtual_1_1 / force | unavailable | unavailable | unavailable |
| heel_phalanx_1_to_virtual_1_1 / velocity | unavailable | unavailable | unavailable |
| virtual_1_1_to_phalanx_1_1 / effort | unavailable | unavailable | unavailable |
| virtual_1_1_to_phalanx_1_1 / force | unavailable | unavailable | unavailable |
| virtual_1_1_to_phalanx_1_1 / velocity | unavailable | unavailable | unavailable |
| phalanx_1_1_to_virtual_2_1 / effort | unavailable | unavailable | unavailable |
| phalanx_1_1_to_virtual_2_1 / force | unavailable | unavailable | unavailable |
| phalanx_1_1_to_virtual_2_1 / velocity | unavailable | unavailable | unavailable |
| virtual_2_1_to_phalanx_2_1 / effort | unavailable | unavailable | unavailable |
| virtual_2_1_to_phalanx_2_1 / force | unavailable | unavailable | unavailable |
| virtual_2_1_to_phalanx_2_1 / velocity | unavailable | unavailable | unavailable |
| phalanx_2_1_to_virtual_3_1 / effort | unavailable | unavailable | unavailable |
| phalanx_2_1_to_virtual_3_1 / force | unavailable | unavailable | unavailable |
| phalanx_2_1_to_virtual_3_1 / velocity | unavailable | unavailable | unavailable |
| virtual_3_1_to_phalanx_3_1 / effort | unavailable | unavailable | unavailable |
| virtual_3_1_to_phalanx_3_1 / force | unavailable | unavailable | unavailable |
| virtual_3_1_to_phalanx_3_1 / velocity | unavailable | unavailable | unavailable |
| phalanx_3_1_to_virtual_4_1 / effort | unavailable | unavailable | unavailable |
| phalanx_3_1_to_virtual_4_1 / force | unavailable | unavailable | unavailable |
| phalanx_3_1_to_virtual_4_1 / velocity | unavailable | unavailable | unavailable |
| virtual_4_1_to_phalanx_4_1 / effort | unavailable | unavailable | unavailable |
| virtual_4_1_to_phalanx_4_1 / force | unavailable | unavailable | unavailable |
| virtual_4_1_to_phalanx_4_1 / velocity | unavailable | unavailable | unavailable |
| phalanx_4_1_to_virtual_5_1 / effort | unavailable | unavailable | unavailable |
| phalanx_4_1_to_virtual_5_1 / force | unavailable | unavailable | unavailable |
| phalanx_4_1_to_virtual_5_1 / velocity | unavailable | unavailable | unavailable |
| virtual_5_1_to_phalanx_5_1 / effort | unavailable | unavailable | unavailable |
| virtual_5_1_to_phalanx_5_1 / force | unavailable | unavailable | unavailable |
| virtual_5_1_to_phalanx_5_1 / velocity | unavailable | unavailable | unavailable |
| phalanx_5_1_to_virtual_6_1 / effort | unavailable | unavailable | unavailable |
| phalanx_5_1_to_virtual_6_1 / force | unavailable | unavailable | unavailable |
| phalanx_5_1_to_virtual_6_1 / velocity | unavailable | unavailable | unavailable |
| virtual_6_1_to_reverse_phalanx_1 / effort | unavailable | unavailable | unavailable |
| virtual_6_1_to_reverse_phalanx_1 / force | unavailable | unavailable | unavailable |
| virtual_6_1_to_reverse_phalanx_1 / velocity | unavailable | unavailable | unavailable |
| reverse_phalanx_1_to_virtual_7_1 / effort | unavailable | unavailable | unavailable |
| reverse_phalanx_1_to_virtual_7_1 / force | unavailable | unavailable | unavailable |
| reverse_phalanx_1_to_virtual_7_1 / velocity | unavailable | unavailable | unavailable |
| virtual_7_1_to_rollover_phalanx_1 / effort | unavailable | unavailable | unavailable |
| virtual_7_1_to_rollover_phalanx_1 / force | unavailable | unavailable | unavailable |
| virtual_7_1_to_rollover_phalanx_1 / velocity | unavailable | unavailable | unavailable |
| rollover_phalanx_1_to_virtual_8_1 / effort | unavailable | unavailable | unavailable |
| rollover_phalanx_1_to_virtual_8_1 / force | unavailable | unavailable | unavailable |
| rollover_phalanx_1_to_virtual_8_1 / velocity | unavailable | unavailable | unavailable |
| virtual_8_1_to_phalanx_6_1 / effort | unavailable | unavailable | unavailable |
| virtual_8_1_to_phalanx_6_1 / force | unavailable | unavailable | unavailable |
| virtual_8_1_to_phalanx_6_1 / velocity | unavailable | unavailable | unavailable |
| phalanx_6_1_to_virtual_9_1 / effort | unavailable | unavailable | unavailable |
| phalanx_6_1_to_virtual_9_1 / force | unavailable | unavailable | unavailable |
| phalanx_6_1_to_virtual_9_1 / velocity | unavailable | unavailable | unavailable |
| virtual_9_1_to_distal_phalanx_1 / effort | unavailable | unavailable | unavailable |
| virtual_9_1_to_distal_phalanx_1 / force | unavailable | unavailable | unavailable |
| virtual_9_1_to_distal_phalanx_1 / velocity | unavailable | unavailable | unavailable |
| heel_phalanx_2_to_virtual_1_2 / effort | unavailable | unavailable | unavailable |
| heel_phalanx_2_to_virtual_1_2 / force | unavailable | unavailable | unavailable |
| heel_phalanx_2_to_virtual_1_2 / velocity | unavailable | unavailable | unavailable |
| virtual_1_2_to_phalanx_1_2 / effort | unavailable | unavailable | unavailable |
| virtual_1_2_to_phalanx_1_2 / force | unavailable | unavailable | unavailable |
| virtual_1_2_to_phalanx_1_2 / velocity | unavailable | unavailable | unavailable |
| phalanx_1_2_to_virtual_2_2 / effort | unavailable | unavailable | unavailable |
| phalanx_1_2_to_virtual_2_2 / force | unavailable | unavailable | unavailable |
| phalanx_1_2_to_virtual_2_2 / velocity | unavailable | unavailable | unavailable |
| virtual_2_2_to_phalanx_2_2 / effort | unavailable | unavailable | unavailable |
| virtual_2_2_to_phalanx_2_2 / force | unavailable | unavailable | unavailable |
| virtual_2_2_to_phalanx_2_2 / velocity | unavailable | unavailable | unavailable |
| phalanx_2_2_to_virtual_3_2 / effort | unavailable | unavailable | unavailable |
| phalanx_2_2_to_virtual_3_2 / force | unavailable | unavailable | unavailable |
| phalanx_2_2_to_virtual_3_2 / velocity | unavailable | unavailable | unavailable |
| virtual_3_2_to_phalanx_3_2 / effort | unavailable | unavailable | unavailable |
| virtual_3_2_to_phalanx_3_2 / force | unavailable | unavailable | unavailable |
| virtual_3_2_to_phalanx_3_2 / velocity | unavailable | unavailable | unavailable |
| phalanx_3_2_to_virtual_4_2 / effort | unavailable | unavailable | unavailable |
| phalanx_3_2_to_virtual_4_2 / force | unavailable | unavailable | unavailable |
| phalanx_3_2_to_virtual_4_2 / velocity | unavailable | unavailable | unavailable |
| virtual_4_2_to_phalanx_4_2 / effort | unavailable | unavailable | unavailable |
| virtual_4_2_to_phalanx_4_2 / force | unavailable | unavailable | unavailable |
| virtual_4_2_to_phalanx_4_2 / velocity | unavailable | unavailable | unavailable |
| phalanx_4_2_to_virtual_5_2 / effort | unavailable | unavailable | unavailable |
| phalanx_4_2_to_virtual_5_2 / force | unavailable | unavailable | unavailable |
| phalanx_4_2_to_virtual_5_2 / velocity | unavailable | unavailable | unavailable |
| virtual_5_2_to_phalanx_5_2 / effort | unavailable | unavailable | unavailable |
| virtual_5_2_to_phalanx_5_2 / force | unavailable | unavailable | unavailable |
| virtual_5_2_to_phalanx_5_2 / velocity | unavailable | unavailable | unavailable |
| phalanx_5_2_to_virtual_6_2 / effort | unavailable | unavailable | unavailable |
| phalanx_5_2_to_virtual_6_2 / force | unavailable | unavailable | unavailable |
| phalanx_5_2_to_virtual_6_2 / velocity | unavailable | unavailable | unavailable |
| virtual_6_2_to_reverse_phalanx_2 / effort | unavailable | unavailable | unavailable |
| virtual_6_2_to_reverse_phalanx_2 / force | unavailable | unavailable | unavailable |
| virtual_6_2_to_reverse_phalanx_2 / velocity | unavailable | unavailable | unavailable |
| reverse_phalanx_2_to_virtual_7_2 / effort | unavailable | unavailable | unavailable |
| reverse_phalanx_2_to_virtual_7_2 / force | unavailable | unavailable | unavailable |
| reverse_phalanx_2_to_virtual_7_2 / velocity | unavailable | unavailable | unavailable |
| virtual_7_2_to_rollover_phalanx_2 / effort | unavailable | unavailable | unavailable |
| virtual_7_2_to_rollover_phalanx_2 / force | unavailable | unavailable | unavailable |
| virtual_7_2_to_rollover_phalanx_2 / velocity | unavailable | unavailable | unavailable |
| rollover_phalanx_2_to_virtual_8_2 / effort | unavailable | unavailable | unavailable |
| rollover_phalanx_2_to_virtual_8_2 / force | unavailable | unavailable | unavailable |
| rollover_phalanx_2_to_virtual_8_2 / velocity | unavailable | unavailable | unavailable |
| virtual_8_2_to_phalanx_6_2 / effort | unavailable | unavailable | unavailable |
| virtual_8_2_to_phalanx_6_2 / force | unavailable | unavailable | unavailable |
| virtual_8_2_to_phalanx_6_2 / velocity | unavailable | unavailable | unavailable |
| phalanx_6_2_to_virtual_9_2 / effort | unavailable | unavailable | unavailable |
| phalanx_6_2_to_virtual_9_2 / force | unavailable | unavailable | unavailable |
| phalanx_6_2_to_virtual_9_2 / velocity | unavailable | unavailable | unavailable |
| virtual_9_2_to_distal_phalanx_2 / effort | unavailable | unavailable | unavailable |
| virtual_9_2_to_distal_phalanx_2 / force | unavailable | unavailable | unavailable |
| virtual_9_2_to_distal_phalanx_2 / velocity | unavailable | unavailable | unavailable |
| heel_phalanx_3_to_virtual_1_3 / effort | unavailable | unavailable | unavailable |
| heel_phalanx_3_to_virtual_1_3 / force | unavailable | unavailable | unavailable |
| heel_phalanx_3_to_virtual_1_3 / velocity | unavailable | unavailable | unavailable |
| virtual_1_3_to_phalanx_1_3 / effort | unavailable | unavailable | unavailable |
| virtual_1_3_to_phalanx_1_3 / force | unavailable | unavailable | unavailable |
| virtual_1_3_to_phalanx_1_3 / velocity | unavailable | unavailable | unavailable |
| phalanx_1_3_to_virtual_2_3 / effort | unavailable | unavailable | unavailable |
| phalanx_1_3_to_virtual_2_3 / force | unavailable | unavailable | unavailable |
| phalanx_1_3_to_virtual_2_3 / velocity | unavailable | unavailable | unavailable |
| virtual_2_3_to_phalanx_2_3 / effort | unavailable | unavailable | unavailable |
| virtual_2_3_to_phalanx_2_3 / force | unavailable | unavailable | unavailable |
| virtual_2_3_to_phalanx_2_3 / velocity | unavailable | unavailable | unavailable |
| phalanx_2_3_to_virtual_3_3 / effort | unavailable | unavailable | unavailable |
| phalanx_2_3_to_virtual_3_3 / force | unavailable | unavailable | unavailable |
| phalanx_2_3_to_virtual_3_3 / velocity | unavailable | unavailable | unavailable |
| virtual_3_3_to_phalanx_3_3 / effort | unavailable | unavailable | unavailable |
| virtual_3_3_to_phalanx_3_3 / force | unavailable | unavailable | unavailable |
| virtual_3_3_to_phalanx_3_3 / velocity | unavailable | unavailable | unavailable |
| phalanx_3_3_to_virtual_4_3 / effort | unavailable | unavailable | unavailable |
| phalanx_3_3_to_virtual_4_3 / force | unavailable | unavailable | unavailable |
| phalanx_3_3_to_virtual_4_3 / velocity | unavailable | unavailable | unavailable |
| virtual_4_3_to_phalanx_4_3 / effort | unavailable | unavailable | unavailable |
| virtual_4_3_to_phalanx_4_3 / force | unavailable | unavailable | unavailable |
| virtual_4_3_to_phalanx_4_3 / velocity | unavailable | unavailable | unavailable |
| phalanx_4_3_to_virtual_5_3 / effort | unavailable | unavailable | unavailable |
| phalanx_4_3_to_virtual_5_3 / force | unavailable | unavailable | unavailable |
| phalanx_4_3_to_virtual_5_3 / velocity | unavailable | unavailable | unavailable |
| virtual_5_3_to_phalanx_5_3 / effort | unavailable | unavailable | unavailable |
| virtual_5_3_to_phalanx_5_3 / force | unavailable | unavailable | unavailable |
| virtual_5_3_to_phalanx_5_3 / velocity | unavailable | unavailable | unavailable |
| phalanx_5_3_to_virtual_6_3 / effort | unavailable | unavailable | unavailable |
| phalanx_5_3_to_virtual_6_3 / force | unavailable | unavailable | unavailable |
| phalanx_5_3_to_virtual_6_3 / velocity | unavailable | unavailable | unavailable |
| virtual_6_3_to_reverse_phalanx_3 / effort | unavailable | unavailable | unavailable |
| virtual_6_3_to_reverse_phalanx_3 / force | unavailable | unavailable | unavailable |
| virtual_6_3_to_reverse_phalanx_3 / velocity | unavailable | unavailable | unavailable |
| reverse_phalanx_3_to_virtual_7_3 / effort | unavailable | unavailable | unavailable |
| reverse_phalanx_3_to_virtual_7_3 / force | unavailable | unavailable | unavailable |
| reverse_phalanx_3_to_virtual_7_3 / velocity | unavailable | unavailable | unavailable |
| virtual_7_3_to_rollover_phalanx_3 / effort | unavailable | unavailable | unavailable |
| virtual_7_3_to_rollover_phalanx_3 / force | unavailable | unavailable | unavailable |
| virtual_7_3_to_rollover_phalanx_3 / velocity | unavailable | unavailable | unavailable |
| rollover_phalanx_3_to_virtual_8_3 / effort | unavailable | unavailable | unavailable |
| rollover_phalanx_3_to_virtual_8_3 / force | unavailable | unavailable | unavailable |
| rollover_phalanx_3_to_virtual_8_3 / velocity | unavailable | unavailable | unavailable |
| virtual_8_3_to_phalanx_6_3 / effort | unavailable | unavailable | unavailable |
| virtual_8_3_to_phalanx_6_3 / force | unavailable | unavailable | unavailable |
| virtual_8_3_to_phalanx_6_3 / velocity | unavailable | unavailable | unavailable |
| phalanx_6_3_to_virtual_9_3 / effort | unavailable | unavailable | unavailable |
| phalanx_6_3_to_virtual_9_3 / force | unavailable | unavailable | unavailable |
| phalanx_6_3_to_virtual_9_3 / velocity | unavailable | unavailable | unavailable |
| virtual_9_3_to_distal_phalanx_3 / effort | unavailable | unavailable | unavailable |
| virtual_9_3_to_distal_phalanx_3 / force | unavailable | unavailable | unavailable |
| virtual_9_3_to_distal_phalanx_3 / velocity | unavailable | unavailable | unavailable |
| heel_phalanx_4_to_virtual_1_4 / effort | unavailable | unavailable | unavailable |
| heel_phalanx_4_to_virtual_1_4 / force | unavailable | unavailable | unavailable |
| heel_phalanx_4_to_virtual_1_4 / velocity | unavailable | unavailable | unavailable |
| virtual_1_4_to_phalanx_1_4 / effort | unavailable | unavailable | unavailable |
| virtual_1_4_to_phalanx_1_4 / force | unavailable | unavailable | unavailable |
| virtual_1_4_to_phalanx_1_4 / velocity | unavailable | unavailable | unavailable |
| phalanx_1_4_to_virtual_2_4 / effort | unavailable | unavailable | unavailable |
| phalanx_1_4_to_virtual_2_4 / force | unavailable | unavailable | unavailable |
| phalanx_1_4_to_virtual_2_4 / velocity | unavailable | unavailable | unavailable |
| virtual_2_4_to_phalanx_2_4 / effort | unavailable | unavailable | unavailable |
| virtual_2_4_to_phalanx_2_4 / force | unavailable | unavailable | unavailable |
| virtual_2_4_to_phalanx_2_4 / velocity | unavailable | unavailable | unavailable |
| phalanx_2_4_to_virtual_3_4 / effort | unavailable | unavailable | unavailable |
| phalanx_2_4_to_virtual_3_4 / force | unavailable | unavailable | unavailable |
| phalanx_2_4_to_virtual_3_4 / velocity | unavailable | unavailable | unavailable |
| virtual_3_4_to_phalanx_3_4 / effort | unavailable | unavailable | unavailable |
| virtual_3_4_to_phalanx_3_4 / force | unavailable | unavailable | unavailable |
| virtual_3_4_to_phalanx_3_4 / velocity | unavailable | unavailable | unavailable |
| phalanx_3_4_to_virtual_4_4 / effort | unavailable | unavailable | unavailable |
| phalanx_3_4_to_virtual_4_4 / force | unavailable | unavailable | unavailable |
| phalanx_3_4_to_virtual_4_4 / velocity | unavailable | unavailable | unavailable |
| virtual_4_4_to_phalanx_4_4 / effort | unavailable | unavailable | unavailable |
| virtual_4_4_to_phalanx_4_4 / force | unavailable | unavailable | unavailable |
| virtual_4_4_to_phalanx_4_4 / velocity | unavailable | unavailable | unavailable |
| phalanx_4_4_to_virtual_5_4 / effort | unavailable | unavailable | unavailable |
| phalanx_4_4_to_virtual_5_4 / force | unavailable | unavailable | unavailable |
| phalanx_4_4_to_virtual_5_4 / velocity | unavailable | unavailable | unavailable |
| virtual_5_4_to_phalanx_5_4 / effort | unavailable | unavailable | unavailable |
| virtual_5_4_to_phalanx_5_4 / force | unavailable | unavailable | unavailable |
| virtual_5_4_to_phalanx_5_4 / velocity | unavailable | unavailable | unavailable |
| phalanx_5_4_to_virtual_6_4 / effort | unavailable | unavailable | unavailable |
| phalanx_5_4_to_virtual_6_4 / force | unavailable | unavailable | unavailable |
| phalanx_5_4_to_virtual_6_4 / velocity | unavailable | unavailable | unavailable |
| virtual_6_4_to_reverse_phalanx_4 / effort | unavailable | unavailable | unavailable |
| virtual_6_4_to_reverse_phalanx_4 / force | unavailable | unavailable | unavailable |
| virtual_6_4_to_reverse_phalanx_4 / velocity | unavailable | unavailable | unavailable |
| reverse_phalanx_4_to_virtual_7_4 / effort | unavailable | unavailable | unavailable |
| reverse_phalanx_4_to_virtual_7_4 / force | unavailable | unavailable | unavailable |
| reverse_phalanx_4_to_virtual_7_4 / velocity | unavailable | unavailable | unavailable |
| virtual_7_4_to_rollover_phalanx_4 / effort | unavailable | unavailable | unavailable |
| virtual_7_4_to_rollover_phalanx_4 / force | unavailable | unavailable | unavailable |
| virtual_7_4_to_rollover_phalanx_4 / velocity | unavailable | unavailable | unavailable |
| rollover_phalanx_4_to_virtual_8_4 / effort | unavailable | unavailable | unavailable |
| rollover_phalanx_4_to_virtual_8_4 / force | unavailable | unavailable | unavailable |
| rollover_phalanx_4_to_virtual_8_4 / velocity | unavailable | unavailable | unavailable |
| virtual_8_4_to_phalanx_6_4 / effort | unavailable | unavailable | unavailable |
| virtual_8_4_to_phalanx_6_4 / force | unavailable | unavailable | unavailable |
| virtual_8_4_to_phalanx_6_4 / velocity | unavailable | unavailable | unavailable |
| phalanx_6_4_to_virtual_9_4 / effort | unavailable | unavailable | unavailable |
| phalanx_6_4_to_virtual_9_4 / force | unavailable | unavailable | unavailable |
| phalanx_6_4_to_virtual_9_4 / velocity | unavailable | unavailable | unavailable |
| virtual_9_4_to_distal_phalanx_4 / effort | unavailable | unavailable | unavailable |
| virtual_9_4_to_distal_phalanx_4 / force | unavailable | unavailable | unavailable |
| virtual_9_4_to_distal_phalanx_4 / velocity | unavailable | unavailable | unavailable |
| heel_phalanx_5_to_virtual_1_5 / effort | unavailable | unavailable | unavailable |
| heel_phalanx_5_to_virtual_1_5 / force | unavailable | unavailable | unavailable |
| heel_phalanx_5_to_virtual_1_5 / velocity | unavailable | unavailable | unavailable |
| virtual_1_5_to_phalanx_1_5 / effort | unavailable | unavailable | unavailable |
| virtual_1_5_to_phalanx_1_5 / force | unavailable | unavailable | unavailable |
| virtual_1_5_to_phalanx_1_5 / velocity | unavailable | unavailable | unavailable |
| phalanx_1_5_to_virtual_2_5 / effort | unavailable | unavailable | unavailable |
| phalanx_1_5_to_virtual_2_5 / force | unavailable | unavailable | unavailable |
| phalanx_1_5_to_virtual_2_5 / velocity | unavailable | unavailable | unavailable |
| virtual_2_5_to_phalanx_2_5 / effort | unavailable | unavailable | unavailable |
| virtual_2_5_to_phalanx_2_5 / force | unavailable | unavailable | unavailable |
| virtual_2_5_to_phalanx_2_5 / velocity | unavailable | unavailable | unavailable |
| phalanx_2_5_to_virtual_3_5 / effort | unavailable | unavailable | unavailable |
| phalanx_2_5_to_virtual_3_5 / force | unavailable | unavailable | unavailable |
| phalanx_2_5_to_virtual_3_5 / velocity | unavailable | unavailable | unavailable |
| virtual_3_5_to_phalanx_3_5 / effort | unavailable | unavailable | unavailable |
| virtual_3_5_to_phalanx_3_5 / force | unavailable | unavailable | unavailable |
| virtual_3_5_to_phalanx_3_5 / velocity | unavailable | unavailable | unavailable |
| phalanx_3_5_to_virtual_4_5 / effort | unavailable | unavailable | unavailable |
| phalanx_3_5_to_virtual_4_5 / force | unavailable | unavailable | unavailable |
| phalanx_3_5_to_virtual_4_5 / velocity | unavailable | unavailable | unavailable |
| virtual_4_5_to_phalanx_4_5 / effort | unavailable | unavailable | unavailable |
| virtual_4_5_to_phalanx_4_5 / force | unavailable | unavailable | unavailable |
| virtual_4_5_to_phalanx_4_5 / velocity | unavailable | unavailable | unavailable |
| phalanx_4_5_to_virtual_5_5 / effort | unavailable | unavailable | unavailable |
| phalanx_4_5_to_virtual_5_5 / force | unavailable | unavailable | unavailable |
| phalanx_4_5_to_virtual_5_5 / velocity | unavailable | unavailable | unavailable |
| virtual_5_5_to_phalanx_5_5 / effort | unavailable | unavailable | unavailable |
| virtual_5_5_to_phalanx_5_5 / force | unavailable | unavailable | unavailable |
| virtual_5_5_to_phalanx_5_5 / velocity | unavailable | unavailable | unavailable |
| phalanx_5_5_to_virtual_6_5 / effort | unavailable | unavailable | unavailable |
| phalanx_5_5_to_virtual_6_5 / force | unavailable | unavailable | unavailable |
| phalanx_5_5_to_virtual_6_5 / velocity | unavailable | unavailable | unavailable |
| virtual_6_5_to_reverse_phalanx_5 / effort | unavailable | unavailable | unavailable |
| virtual_6_5_to_reverse_phalanx_5 / force | unavailable | unavailable | unavailable |
| virtual_6_5_to_reverse_phalanx_5 / velocity | unavailable | unavailable | unavailable |
| reverse_phalanx_5_to_virtual_7_5 / effort | unavailable | unavailable | unavailable |
| reverse_phalanx_5_to_virtual_7_5 / force | unavailable | unavailable | unavailable |
| reverse_phalanx_5_to_virtual_7_5 / velocity | unavailable | unavailable | unavailable |
| virtual_7_5_to_rollover_phalanx_5 / effort | unavailable | unavailable | unavailable |
| virtual_7_5_to_rollover_phalanx_5 / force | unavailable | unavailable | unavailable |
| virtual_7_5_to_rollover_phalanx_5 / velocity | unavailable | unavailable | unavailable |
| rollover_phalanx_5_to_virtual_8_5 / effort | unavailable | unavailable | unavailable |
| rollover_phalanx_5_to_virtual_8_5 / force | unavailable | unavailable | unavailable |
| rollover_phalanx_5_to_virtual_8_5 / velocity | unavailable | unavailable | unavailable |
| virtual_8_5_to_phalanx_6_5 / effort | unavailable | unavailable | unavailable |
| virtual_8_5_to_phalanx_6_5 / force | unavailable | unavailable | unavailable |
| virtual_8_5_to_phalanx_6_5 / velocity | unavailable | unavailable | unavailable |
| phalanx_6_5_to_virtual_9_5 / effort | unavailable | unavailable | unavailable |
| phalanx_6_5_to_virtual_9_5 / force | unavailable | unavailable | unavailable |
| phalanx_6_5_to_virtual_9_5 / velocity | unavailable | unavailable | unavailable |
| virtual_9_5_to_distal_phalanx_5 / effort | unavailable | unavailable | unavailable |
| virtual_9_5_to_distal_phalanx_5 / force | unavailable | unavailable | unavailable |
| virtual_9_5_to_distal_phalanx_5 / velocity | unavailable | unavailable | unavailable |
| cube_to_frontal_arch / effort | unavailable | unavailable | unavailable |
| cube_to_frontal_arch / force | unavailable | unavailable | unavailable |
| cube_to_frontal_arch / velocity | unavailable | unavailable | unavailable |
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
    "file": "iit_softfoot/softfoot.xml",
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
    "xacro_arguments": {},
    "registration": {
      "translation": [
        0.0,
        0.0,
        0.0
      ],
      "rotation": [
        [
          1.0000000000000002,
          0.0,
          0.0
        ],
        [
          0.0,
          0.0,
          1.0000000000000002
        ],
        [
          0.0,
          -1.0000000000000002,
          0.0
        ]
      ]
    }
  },
  "H": {
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
          1.0000000000000002,
          0.0,
          0.0
        ],
        [
          0.0,
          0.0,
          1.0000000000000002
        ],
        [
          0.0,
          -1.0000000000000002,
          0.0
        ]
      ]
    }
  },
  "S": {
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
          1.0000000000000002,
          0.0,
          0.0
        ],
        [
          0.0,
          0.0,
          1.0000000000000002
        ],
        [
          0.0,
          -1.0000000000000002,
          0.0
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
    "M",
    "S"
  ],
  "self_variants_recompiled": 1,
  "historical_snapshots_reused": 1,
  "primary_physics_unchanged": true,
  "source_matching": "original raw-value provenance criteria retained; kinematic guard applies to reported CoM"
}
```
