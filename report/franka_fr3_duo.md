# franka_fr3_duo

Status: **partial history**. Provenance: **pinned**, confidence **high**.

Source selected using the ordered amended provenance rules.

M: `https://github.com/google-deepmind/mujoco_menagerie`, `franka_fr3_duo/fr3_duo.xml`, commit `370c43965323c0944b433b202aac5058b5f907a9`.
H: `https://github.com/frankarobotics/franka_description`, `robots/fr3_duo/fr3_duo.urdf.xacro`, commit `7aeeddc449edf8d62b594f9e36a81da53e7796f9`.
S: `7aeeddc449edf8d62b594f9e36a81da53e7796f9` (2026-08-17T10:29:44+02:00). Menagerie release/change: 2026-11-10T14:14:23-06:00.

Limit semantics: MJCF effort values are supported actuator torque/force envelopes. URDF effort and velocity values are manufacturer declarations retained from XML; MuJoCo does not enforce those tags. Such declaration comparisons are explicitly distinct from compiled inertial/range quantities.


## Source evidence

```json
[
  {
    "url": "https://github.com/frankarobotics/franka_description",
    "document": "franka_fr3_duo/README.md",
    "commit": "370c43965323c0944b433b202aac5058b5f907a9",
    "current": true
  },
  {
    "url": "https://github.com/frankarobotics/franka_description/blob/main/robots/fr3_duo/fr3_duo.urdf.xacro",
    "document": "franka_fr3_duo/README.md",
    "commit": "370c43965323c0944b433b202aac5058b5f907a9",
    "current": true
  },
  {
    "url": "https://github.com/google-deepmind/mujoco_menagerie/blob/main/franka_fr3_v2/fr3v2.xml",
    "document": "franka_fr3_duo/README.md",
    "commit": "370c43965323c0944b433b202aac5058b5f907a9",
    "current": true
  },
  {
    "url": "https://github.com/google-deepmind/mujoco_menagerie/tree/main/franka_fr3_v2",
    "document": "franka_fr3_duo/README.md",
    "commit": "370c43965323c0944b433b202aac5058b5f907a9",
    "current": true
  },
  {
    "url": "https://github.com/kevinzakka/obj2mjcf",
    "document": "franka_fr3_duo/README.md",
    "commit": "370c43965323c0944b433b202aac5058b5f907a9",
    "current": true
  }
]
```


## README derivation evidence

Documentation labels are conservative: an automated documented label requires an explicit affected entity and quantity. Broader conversion notes are retained here for review.

>    transforms, joint limits, and inertials come directly from MuJoCo's URDF
>      <compiler balanceinertia="true" discardvisual="true" fusestatic="false"
>    collapsed fixed mounting-frame and empty accelerometer bodies while
>      the column's `0.1` + `[0, 0.85]` m vertical slide range) so the arms have

## Kinematics consistency

A proper Kabsch rigid transform aligns all matched zero-pose body origins. The maximum per-origin residual and signed hinge/slide axis angles determine whether CoM can be compared; RMS is also recorded. Fewer than three non-collinear origins give insufficient kinematic coverage. CoM records that fail either required M/H or M/S check are excluded from counts and largest discrepancies. Masses, principal moments and raw joint ranges remain unchanged; a flagged range still requires convention review.

| Pair | Status | Origins / rank | RMS / maximum mm | Disagreeing / checked axes |
|---|---|---:|---:|---:|
| M/H | consistent | 20 / 3 | 0.000365574262 / 0.000518179983 | 0 / 14 |
| M/S | consistent | 20 / 3 | 0.000365574262 / 0.000518179983 | 0 / 14 |

Exact fitted transforms, per-origin residuals, thresholds and axis vectors:

```json
{
  "M/H": {
    "status": "consistent",
    "matched_body_origins": 20,
    "position_threshold_m": 0.005,
    "axis_threshold_rad": 0.005,
    "residual_definition": "maximum Euclidean residual over matched body origins; Kabsch minimizes RMS, which is also recorded",
    "coordinate_frames": "each snapshot registered to its matched report anchor",
    "anchor_m": "base",
    "anchor_other": "base",
    "rotation_other_to_m": [
      [
        0.9999999999997051,
        -2.9402837820954658e-16,
        -7.677379804551219e-07
      ],
      [
        9.740871557439799e-17,
        0.9999999999999999,
        4.284139370612888e-16
      ],
      [
        7.677379803561202e-07,
        -3.945950881151018e-16,
        0.9999999999997051
      ]
    ],
    "translation_other_to_m": [
      1.5871186828664285e-07,
      -1.5884745375023836e-16,
      2.2888082190641867e-07
    ],
    "rms_residual_m": 3.655742619181393e-07,
    "max_residual_m": 5.181799827628616e-07,
    "fit_rank": 3,
    "axis_checks": [
      {
        "joint_m": "left_fr3v2_joint1",
        "joint_other": "left_fr3v2_joint1",
        "axis_m": [
          0.2508633842481772,
          0.7456746696692493,
          0.6172818233653146
        ],
        "axis_other_aligned": [
          0.25086319748076535,
          0.7456751171306403,
          0.6172813587351657
        ],
        "angle_rad": 6.715541212954825e-07,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "left_fr3v2_joint2",
        "joint_other": "left_fr3v2_joint2",
        "axis_m": [
          0.4012022843492421,
          0.5002366388995451,
          -0.7673330646697274
        ],
        "axis_other_aligned": [
          0.40120290213695914,
          0.5002358900030518,
          -0.7673332298745679
        ],
        "angle_rad": 9.847843724847255e-07,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "left_fr3v2_joint3",
        "joint_other": "left_fr3v2_joint3",
        "axis_m": [
          0.2508633842481771,
          0.7456746696692491,
          0.6172818233653147
        ],
        "axis_other_aligned": [
          0.25086319748076535,
          0.7456751171306403,
          0.6172813587351657
        ],
        "angle_rad": 6.715541214397091e-07,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "left_fr3v2_joint4",
        "joint_other": "left_fr3v2_joint4",
        "axis_m": [
          -0.40120228434924166,
          -0.5002366388995445,
          0.7673330646697281
        ],
        "axis_other_aligned": [
          -0.40120290213695925,
          -0.5002358900030524,
          0.7673332298745674
        ],
        "angle_rad": 9.84784371786098e-07,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "left_fr3v2_joint5",
        "joint_other": "left_fr3v2_joint5",
        "axis_m": [
          0.25086338424817706,
          0.7456746696692489,
          0.617281823365315
        ],
        "axis_other_aligned": [
          0.2508631974807653,
          0.7456751171306402,
          0.6172813587351658
        ],
        "angle_rad": 6.715541216971143e-07,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "left_fr3v2_joint6",
        "joint_other": "left_fr3v2_joint6",
        "axis_m": [
          -0.40120228434924154,
          -0.5002366388995445,
          0.7673330646697281
        ],
        "axis_other_aligned": [
          -0.4012029021369592,
          -0.5002358900030524,
          0.7673332298745674
        ],
        "angle_rad": 9.847843718262618e-07,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "left_fr3v2_joint7",
        "joint_other": "left_fr3v2_joint7",
        "axis_m": [
          -0.2508633842481774,
          -0.7456746696692501,
          -0.6172818233653135
        ],
        "axis_other_aligned": [
          -0.25086319748076497,
          -0.7456751171306398,
          -0.6172813587351663
        ],
        "angle_rad": 6.715541193692639e-07,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "right_fr3v2_joint1",
        "joint_other": "right_fr3v2_joint1",
        "axis_m": [
          0.2508633842481772,
          -0.7456746696692493,
          0.6172818233653146
        ],
        "axis_other_aligned": [
          0.2508631974807658,
          -0.7456751171306398,
          0.6172813587351662
        ],
        "angle_rad": 6.715541204603013e-07,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "right_fr3v2_joint2",
        "joint_other": "right_fr3v2_joint2",
        "axis_m": [
          -0.4012022843492418,
          0.5002366388995447,
          0.7673330646697278
        ],
        "axis_other_aligned": [
          -0.4012029021369595,
          0.5002358900030528,
          0.7673332298745669
        ],
        "angle_rad": 9.847843716385557e-07,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "right_fr3v2_joint3",
        "joint_other": "right_fr3v2_joint3",
        "axis_m": [
          0.2508633842481771,
          -0.7456746696692491,
          0.6172818233653147
        ],
        "axis_other_aligned": [
          0.2508631974807658,
          -0.7456751171306397,
          0.6172813587351663
        ],
        "angle_rad": 6.715541204910862e-07,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "right_fr3v2_joint4",
        "joint_other": "right_fr3v2_joint4",
        "axis_m": [
          0.4012022843492423,
          -0.5002366388995453,
          -0.7673330646697272
        ],
        "axis_other_aligned": [
          0.40120290213695936,
          -0.5002358900030524,
          -0.7673332298745673
        ],
        "angle_rad": 9.847843721713824e-07,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "right_fr3v2_joint5",
        "joint_other": "right_fr3v2_joint5",
        "axis_m": [
          0.2508633842481771,
          -0.7456746696692489,
          0.617281823365315
        ],
        "axis_other_aligned": [
          0.2508631974807658,
          -0.7456751171306397,
          0.6172813587351663
        ],
        "angle_rad": 6.715541209237991e-07,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "right_fr3v2_joint6",
        "joint_other": "right_fr3v2_joint6",
        "axis_m": [
          0.4012022843492424,
          -0.5002366388995454,
          -0.7673330646697272
        ],
        "axis_other_aligned": [
          0.4012029021369593,
          -0.5002358900030525,
          -0.7673332298745673
        ],
        "angle_rad": 9.84784372091055e-07,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "right_fr3v2_joint7",
        "joint_other": "right_fr3v2_joint7",
        "axis_m": [
          -0.25086338424817756,
          0.7456746696692501,
          -0.6172818233653133
        ],
        "axis_other_aligned": [
          -0.2508631974807662,
          0.7456751171306402,
          -0.6172813587351655
        ],
        "angle_rad": 6.71554119780072e-07,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      }
    ],
    "axis_disagreements": [],
    "com_eligible": true,
    "covariance_singular_values": [
      6.327903155452061,
      1.4583708639675683,
      0.018037601553561575
    ],
    "origin_residuals_m": {
      "base": 2.7852448325343754e-07,
      "head_link": 2.3090395244742432e-07,
      "left_fr3v2_link0": 2.8403301536672573e-07,
      "left_fr3v2_link1": 1.9000336765778159e-07,
      "left_fr3v2_link2": 1.9000336765778159e-07,
      "left_fr3v2_link3": 2.937569119997285e-07,
      "left_fr3v2_link4": 2.851850646883395e-07,
      "left_fr3v2_link5": 5.181799827628616e-07,
      "left_fr3v2_link6": 5.181799827628616e-07,
      "left_fr3v2_link7": 4.8454790313296e-07,
      "left_fr3v2_link8": 4.22718029448474e-07,
      "right_fr3v2_link0": 2.840330154161968e-07,
      "right_fr3v2_link1": 1.900033678721268e-07,
      "right_fr3v2_link2": 1.900033678721268e-07,
      "right_fr3v2_link3": 2.937569114513996e-07,
      "right_fr3v2_link4": 2.85185064533244e-07,
      "right_fr3v2_link5": 5.181799820296383e-07,
      "right_fr3v2_link6": 5.181799820296383e-07,
      "right_fr3v2_link7": 4.845479024870128e-07,
      "right_fr3v2_link8": 4.2271802894098315e-07
    },
    "reason": "Unique proper rigid fit and matched signed axes meet the configured thresholds"
  },
  "M/S": {
    "status": "consistent",
    "matched_body_origins": 20,
    "position_threshold_m": 0.005,
    "axis_threshold_rad": 0.005,
    "residual_definition": "maximum Euclidean residual over matched body origins; Kabsch minimizes RMS, which is also recorded",
    "coordinate_frames": "each snapshot registered to its matched report anchor",
    "anchor_m": "base",
    "anchor_other": "base",
    "rotation_other_to_m": [
      [
        0.9999999999997051,
        -2.9402837820954658e-16,
        -7.677379804551219e-07
      ],
      [
        9.740871557439799e-17,
        0.9999999999999999,
        4.284139370612888e-16
      ],
      [
        7.677379803561202e-07,
        -3.945950881151018e-16,
        0.9999999999997051
      ]
    ],
    "translation_other_to_m": [
      1.5871186828664285e-07,
      -1.5884745375023836e-16,
      2.2888082190641867e-07
    ],
    "rms_residual_m": 3.655742619181393e-07,
    "max_residual_m": 5.181799827628616e-07,
    "fit_rank": 3,
    "axis_checks": [
      {
        "joint_m": "left_fr3v2_joint1",
        "joint_other": "left_fr3v2_joint1",
        "axis_m": [
          0.2508633842481772,
          0.7456746696692493,
          0.6172818233653146
        ],
        "axis_other_aligned": [
          0.25086319748076535,
          0.7456751171306403,
          0.6172813587351657
        ],
        "angle_rad": 6.715541212954825e-07,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "left_fr3v2_joint2",
        "joint_other": "left_fr3v2_joint2",
        "axis_m": [
          0.4012022843492421,
          0.5002366388995451,
          -0.7673330646697274
        ],
        "axis_other_aligned": [
          0.40120290213695914,
          0.5002358900030518,
          -0.7673332298745679
        ],
        "angle_rad": 9.847843724847255e-07,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "left_fr3v2_joint3",
        "joint_other": "left_fr3v2_joint3",
        "axis_m": [
          0.2508633842481771,
          0.7456746696692491,
          0.6172818233653147
        ],
        "axis_other_aligned": [
          0.25086319748076535,
          0.7456751171306403,
          0.6172813587351657
        ],
        "angle_rad": 6.715541214397091e-07,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "left_fr3v2_joint4",
        "joint_other": "left_fr3v2_joint4",
        "axis_m": [
          -0.40120228434924166,
          -0.5002366388995445,
          0.7673330646697281
        ],
        "axis_other_aligned": [
          -0.40120290213695925,
          -0.5002358900030524,
          0.7673332298745674
        ],
        "angle_rad": 9.84784371786098e-07,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "left_fr3v2_joint5",
        "joint_other": "left_fr3v2_joint5",
        "axis_m": [
          0.25086338424817706,
          0.7456746696692489,
          0.617281823365315
        ],
        "axis_other_aligned": [
          0.2508631974807653,
          0.7456751171306402,
          0.6172813587351658
        ],
        "angle_rad": 6.715541216971143e-07,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "left_fr3v2_joint6",
        "joint_other": "left_fr3v2_joint6",
        "axis_m": [
          -0.40120228434924154,
          -0.5002366388995445,
          0.7673330646697281
        ],
        "axis_other_aligned": [
          -0.4012029021369592,
          -0.5002358900030524,
          0.7673332298745674
        ],
        "angle_rad": 9.847843718262618e-07,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "left_fr3v2_joint7",
        "joint_other": "left_fr3v2_joint7",
        "axis_m": [
          -0.2508633842481774,
          -0.7456746696692501,
          -0.6172818233653135
        ],
        "axis_other_aligned": [
          -0.25086319748076497,
          -0.7456751171306398,
          -0.6172813587351663
        ],
        "angle_rad": 6.715541193692639e-07,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "right_fr3v2_joint1",
        "joint_other": "right_fr3v2_joint1",
        "axis_m": [
          0.2508633842481772,
          -0.7456746696692493,
          0.6172818233653146
        ],
        "axis_other_aligned": [
          0.2508631974807658,
          -0.7456751171306398,
          0.6172813587351662
        ],
        "angle_rad": 6.715541204603013e-07,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "right_fr3v2_joint2",
        "joint_other": "right_fr3v2_joint2",
        "axis_m": [
          -0.4012022843492418,
          0.5002366388995447,
          0.7673330646697278
        ],
        "axis_other_aligned": [
          -0.4012029021369595,
          0.5002358900030528,
          0.7673332298745669
        ],
        "angle_rad": 9.847843716385557e-07,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "right_fr3v2_joint3",
        "joint_other": "right_fr3v2_joint3",
        "axis_m": [
          0.2508633842481771,
          -0.7456746696692491,
          0.6172818233653147
        ],
        "axis_other_aligned": [
          0.2508631974807658,
          -0.7456751171306397,
          0.6172813587351663
        ],
        "angle_rad": 6.715541204910862e-07,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "right_fr3v2_joint4",
        "joint_other": "right_fr3v2_joint4",
        "axis_m": [
          0.4012022843492423,
          -0.5002366388995453,
          -0.7673330646697272
        ],
        "axis_other_aligned": [
          0.40120290213695936,
          -0.5002358900030524,
          -0.7673332298745673
        ],
        "angle_rad": 9.847843721713824e-07,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "right_fr3v2_joint5",
        "joint_other": "right_fr3v2_joint5",
        "axis_m": [
          0.2508633842481771,
          -0.7456746696692489,
          0.617281823365315
        ],
        "axis_other_aligned": [
          0.2508631974807658,
          -0.7456751171306397,
          0.6172813587351663
        ],
        "angle_rad": 6.715541209237991e-07,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "right_fr3v2_joint6",
        "joint_other": "right_fr3v2_joint6",
        "axis_m": [
          0.4012022843492424,
          -0.5002366388995454,
          -0.7673330646697272
        ],
        "axis_other_aligned": [
          0.4012029021369593,
          -0.5002358900030525,
          -0.7673332298745673
        ],
        "angle_rad": 9.84784372091055e-07,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "right_fr3v2_joint7",
        "joint_other": "right_fr3v2_joint7",
        "axis_m": [
          -0.25086338424817756,
          0.7456746696692501,
          -0.6172818233653133
        ],
        "axis_other_aligned": [
          -0.2508631974807662,
          0.7456751171306402,
          -0.6172813587351655
        ],
        "angle_rad": 6.71554119780072e-07,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      }
    ],
    "axis_disagreements": [],
    "com_eligible": true,
    "covariance_singular_values": [
      6.327903155452061,
      1.4583708639675683,
      0.018037601553561575
    ],
    "origin_residuals_m": {
      "base": 2.7852448325343754e-07,
      "head_link": 2.3090395244742432e-07,
      "left_fr3v2_link0": 2.8403301536672573e-07,
      "left_fr3v2_link1": 1.9000336765778159e-07,
      "left_fr3v2_link2": 1.9000336765778159e-07,
      "left_fr3v2_link3": 2.937569119997285e-07,
      "left_fr3v2_link4": 2.851850646883395e-07,
      "left_fr3v2_link5": 5.181799827628616e-07,
      "left_fr3v2_link6": 5.181799827628616e-07,
      "left_fr3v2_link7": 4.8454790313296e-07,
      "left_fr3v2_link8": 4.22718029448474e-07,
      "right_fr3v2_link0": 2.840330154161968e-07,
      "right_fr3v2_link1": 1.900033678721268e-07,
      "right_fr3v2_link2": 1.900033678721268e-07,
      "right_fr3v2_link3": 2.937569114513996e-07,
      "right_fr3v2_link4": 2.85185064533244e-07,
      "right_fr3v2_link5": 5.181799820296383e-07,
      "right_fr3v2_link6": 5.181799820296383e-07,
      "right_fr3v2_link7": 4.845479024870128e-07,
      "right_fr3v2_link8": 4.2271802894098315e-07
    },
    "reason": "Unique proper rigid fit and matched signed axes meet the configured thresholds"
  }
}
```


## Every reported quantity difference

Counts are quantity records, including correlated total/subtree/body mass records; they are not independent robot defects.

| Entity / quantity | M | S | H | H − M | Class | M source | S source | H source |
|---|---|---|---|---|---|---|---|---|
| robot / total_mass | 36.260357 | 37.686555 | 37.686555 | 1.426198 | undocumented derivation difference | [aggregate inputs](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/franka_fr3_duo/fr3_duo.xml#L1) | [aggregate inputs](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/fr3_duo/fr3_duo.urdf.xacro#L1) | [aggregate inputs](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/fr3_duo/fr3_duo.urdf.xacro#L1) |
| robot / total_com_registered | [0.178469097, 0.00352932441, 0.378716385] | [0.184846346, 0.00324858419, 0.387933155] | [0.184846346, 0.00324858419, 0.387933155] | [0.00637724842, -0.000280740224, 0.00921677012] | undocumented derivation difference | [aggregate inputs](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/franka_fr3_duo/fr3_duo.xml#L1) | [aggregate inputs](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/fr3_duo/fr3_duo.urdf.xacro#L1) | [aggregate inputs](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/fr3_duo/fr3_duo.urdf.xacro#L1) |
| base / mass | 4.09385 | 0 | 0 | -4.09385 | undocumented derivation difference | [input L98](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/franka_fr3_duo/fr3_duo.xml#L98) | [macro declaration L62](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/fr3_duo/fr3_duo.urdf.xacro#L62) | [macro declaration L62](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/fr3_duo/fr3_duo.urdf.xacro#L62) |
| base / subtree_mass | 36.260357 | 37.686555 | 37.686555 | 1.426198 | undocumented derivation difference | [subtree root L92](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/franka_fr3_duo/fr3_duo.xml#L92) | [macro declaration L62](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/fr3_duo/fr3_duo.urdf.xacro#L62) | [macro declaration L62](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/fr3_duo/fr3_duo.urdf.xacro#L62) |
| base / com_registered | [-0.011817, -5e-05, 0.044431] | [1.58711868e-07, -1.58847454e-16, 2.28880822e-07] | [1.58711868e-07, -1.58847454e-16, 2.28880822e-07] | [0.0118171587, 5e-05, -0.0444307711] | undocumented derivation difference | [CoM/kinematic input L98](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/franka_fr3_duo/fr3_duo.xml#L98) | [macro declaration L62](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/fr3_duo/fr3_duo.urdf.xacro#L62) | [macro declaration L62](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/fr3_duo/fr3_duo.urdf.xacro#L62) |
| base / principal_moments | [0.0164193, 0.0204768, 0.0236957] | [0, 0, 0] | [0, 0, 0] | [-0.0164193, -0.0204768, -0.0236957] | undocumented derivation difference | [inertia input L98](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/franka_fr3_duo/fr3_duo.xml#L98) | [macro declaration L62](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/fr3_duo/fr3_duo.urdf.xacro#L62) | [macro declaration L62](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/fr3_duo/fr3_duo.urdf.xacro#L62) |
| left_fr3v2_link0 / subtree_mass | 15.907821 | 16.620422 | 16.620422 | 0.712601 | undocumented derivation difference | [subtree root L109](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/franka_fr3_duo/fr3_duo.xml#L109) | [macro declaration L41](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L41) | [macro declaration L41](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L41) |
| left_fr3v2_link1 / subtree_mass | 13.511221 | 14.223822 | 14.223822 | 0.712601 | undocumented derivation difference | [subtree root L119](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/franka_fr3_duo/fr3_duo.xml#L119) | [macro declaration L41](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L41) | [macro declaration L41](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L41) |
| left_fr3v2_link2 / subtree_mass | 11.073521 | 11.786122 | 11.786122 | 0.712601 | undocumented derivation difference | [subtree root L129](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/franka_fr3_duo/fr3_duo.xml#L129) | [macro declaration L41](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L41) | [macro declaration L41](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L41) |
| left_fr3v2_link3 / subtree_mass | 8.836021 | 9.548622 | 9.548622 | 0.712601 | undocumented derivation difference | [subtree root L139](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/franka_fr3_duo/fr3_duo.xml#L139) | [macro declaration L41](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L41) | [macro declaration L41](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L41) |
| left_fr3v2_link4 / subtree_mass | 6.642941 | 7.35554 | 7.35554 | 0.712599 | undocumented derivation difference | [subtree root L149](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/franka_fr3_duo/fr3_duo.xml#L149) | [macro declaration L41](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L41) | [macro declaration L41](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L41) |
| left_fr3v2_link5 / subtree_mass | 4.461401 | 5.174003 | 5.174003 | 0.712602 | undocumented derivation difference | [subtree root L159](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/franka_fr3_duo/fr3_duo.xml#L159) | [macro declaration L41](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L41) | [macro declaration L41](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L41) |
| left_fr3v2_link6 / subtree_mass | 2.274521 | 2.987122 | 2.987122 | 0.712601 | undocumented derivation difference | [subtree root L170](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/franka_fr3_duo/fr3_duo.xml#L170) | [macro declaration L41](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L41) | [macro declaration L41](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L41) |
| left_fr3v2_link7 / subtree_mass | 0.694841 | 1.407441 | 1.407441 | 0.7126 | undocumented derivation difference | [subtree root L186](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/franka_fr3_duo/fr3_duo.xml#L186) | [macro declaration L41](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L41) | [macro declaration L41](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L41) |
| left_fr3v2_link8 / subtree_mass | 0 | 0.7126 | 0.7126 | 0.7126 | undocumented derivation difference | [subtree root L199](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/franka_fr3_duo/fr3_duo.xml#L199) | [subtree root L148](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/franka_arm.xacro#L148) | [subtree root L148](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/franka_arm.xacro#L148) |
| right_fr3v2_link0 / subtree_mass | 15.907821 | 16.620422 | 16.620422 | 0.712601 | undocumented derivation difference | [subtree root L212](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/franka_fr3_duo/fr3_duo.xml#L212) | [macro declaration L41](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L41) | [macro declaration L41](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L41) |
| right_fr3v2_link1 / subtree_mass | 13.511221 | 14.223822 | 14.223822 | 0.712601 | undocumented derivation difference | [subtree root L222](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/franka_fr3_duo/fr3_duo.xml#L222) | [macro declaration L41](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L41) | [macro declaration L41](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L41) |
| right_fr3v2_link2 / subtree_mass | 11.073521 | 11.786122 | 11.786122 | 0.712601 | undocumented derivation difference | [subtree root L232](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/franka_fr3_duo/fr3_duo.xml#L232) | [macro declaration L41](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L41) | [macro declaration L41](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L41) |
| right_fr3v2_link3 / subtree_mass | 8.836021 | 9.548622 | 9.548622 | 0.712601 | undocumented derivation difference | [subtree root L242](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/franka_fr3_duo/fr3_duo.xml#L242) | [macro declaration L41](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L41) | [macro declaration L41](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L41) |
| right_fr3v2_link4 / subtree_mass | 6.642941 | 7.35554 | 7.35554 | 0.712599 | undocumented derivation difference | [subtree root L252](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/franka_fr3_duo/fr3_duo.xml#L252) | [macro declaration L41](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L41) | [macro declaration L41](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L41) |
| right_fr3v2_link5 / subtree_mass | 4.461401 | 5.174003 | 5.174003 | 0.712602 | undocumented derivation difference | [subtree root L262](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/franka_fr3_duo/fr3_duo.xml#L262) | [macro declaration L41](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L41) | [macro declaration L41](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L41) |
| right_fr3v2_link6 / subtree_mass | 2.274521 | 2.987122 | 2.987122 | 0.712601 | undocumented derivation difference | [subtree root L273](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/franka_fr3_duo/fr3_duo.xml#L273) | [macro declaration L41](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L41) | [macro declaration L41](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L41) |
| right_fr3v2_link7 / subtree_mass | 0.694841 | 1.407441 | 1.407441 | 0.7126 | undocumented derivation difference | [subtree root L289](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/franka_fr3_duo/fr3_duo.xml#L289) | [macro declaration L41](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L41) | [macro declaration L41](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L41) |
| right_fr3v2_link8 / subtree_mass | 0 | 0.7126 | 0.7126 | 0.7126 | undocumented derivation difference | [subtree root L302](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/franka_fr3_duo/fr3_duo.xml#L302) | [subtree root L148](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/franka_arm.xacro#L148) | [subtree root L148](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/franka_arm.xacro#L148) |

## Raw CoM records and reporting decisions

Raw values retain the previous root-anchor registration before Kabsch; original world coordinates also remain in the snapshots. Eligible findings above use the fitted transform into M. Excluded raw records below are diagnostic numbers, not findings. No CoM suppression applies to mass or principal inertia moments.

| Entity / quantity | Raw M | Raw S | Raw H | Raw H − M | Decision | M source | S source | H source |
|---|---|---|---|---|---|---|---|---|
| robot / total_com_registered | [0.178469097, 0.00352932441, 0.378716385] | [0.184846485, 0.00324858419, 0.387932784] | [0.184846485, 0.00324858419, 0.387932784] | [0.00637738754, -0.000280740224, 0.00921639932] | eligible; compared after Kabsch alignment | [aggregate inputs](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/franka_fr3_duo/fr3_duo.xml#L1) | [aggregate inputs](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/fr3_duo/fr3_duo.urdf.xacro#L1) | [aggregate inputs](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/fr3_duo/fr3_duo.urdf.xacro#L1) |
| base / com_registered | [-0.011817, -5e-05, 0.044431] | [0, 0, 0] | [0, 0, 0] | [0.011817, 5e-05, -0.044431] | eligible; compared after Kabsch alignment | [CoM/kinematic input L98](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/franka_fr3_duo/fr3_duo.xml#L98) | [macro declaration L62](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/fr3_duo/fr3_duo.urdf.xacro#L62) | [macro declaration L62](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/fr3_duo/fr3_duo.urdf.xacro#L62) |
| head_link / com_registered | [0, 0, 0.167] | [0, 0, 0.167] | [0, 0, 0.167] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L104](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/franka_fr3_duo/fr3_duo.xml#L104) | [geometry/inference input L12](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/accessories/franka_head_v0_2/franka_head.xacro#L12) | [geometry/inference input L12](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/accessories/franka_head_v0_2/franka_head.xacro#L12) |
| left_fr3v2_link0 / com_registered | [0.0406971566, 0.113503449, 0.092693347] | [0.0406971797, 0.113503483, 0.0926932937] | [0.0406971797, 0.113503483, 0.0926932937] | [2.30346246e-08, 3.46371047e-08, -5.33691075e-08] | eligible; compared after Kabsch alignment | [CoM/kinematic input L118](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/franka_fr3_duo/fr3_duo.xml#L118) | [macro declaration L16](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L16); [YAML numeric inputs L3](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/fr3v2/inertials.yaml#L3) | [macro declaration L16](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L16); [YAML numeric inputs L3](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/fr3v2/inertials.yaml#L3) |
| left_fr3v2_link1 / com_registered | [0.111838198, 0.267937253, 0.195881127] | [0.111838277, 0.267937355, 0.195880935] | [0.111838277, 0.267937355, 0.195880935] | [7.90821779e-08, 1.01545598e-07, -1.92147439e-07] | eligible; compared after Kabsch alignment | [CoM/kinematic input L121](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/franka_fr3_duo/fr3_duo.xml#L121) | [macro declaration L16](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L16); [YAML numeric inputs L15](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/fr3v2/inertials.yaml#L15) | [macro declaration L16](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L16); [YAML numeric inputs L15](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/fr3v2/inertials.yaml#L15) |
| left_fr3v2_link2 / com_registered | [0.165662539, 0.425985663, 0.37592166] | [0.165662686, 0.4259859, 0.375921328] | [0.165662686, 0.4259859, 0.375921328] | [1.46771593e-07, 2.37281949e-07, -3.31539793e-07] | eligible; compared after Kabsch alignment | [CoM/kinematic input L131](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/franka_fr3_duo/fr3_duo.xml#L131) | [macro declaration L16](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L16); [YAML numeric inputs L27](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/fr3v2/inertials.yaml#L27) | [macro declaration L16](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L16); [YAML numeric inputs L27](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/fr3v2/inertials.yaml#L27) |
| left_fr3v2_link3 / com_registered | [0.290724197, 0.538676811, 0.476251318] | [0.290724388, 0.538677098, 0.476250875] | [0.290724388, 0.538677098, 0.476250875] | [1.91143721e-07, 2.8723553e-07, -4.42958361e-07] | eligible; compared after Kabsch alignment | [CoM/kinematic input L141](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/franka_fr3_duo/fr3_duo.xml#L141) | [macro declaration L16](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L16); [YAML numeric inputs L39](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/fr3v2/inertials.yaml#L39) | [macro declaration L16](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L16); [YAML numeric inputs L39](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/fr3v2/inertials.yaml#L39) |
| left_fr3v2_link4 / com_registered | [0.215483182, 0.603110313, 0.516973051] | [0.215483397, 0.603110655, 0.516972564] | [0.215483397, 0.603110655, 0.516972564] | [2.14204674e-07, 3.41555885e-07, -4.86299442e-07] | eligible; compared after Kabsch alignment | [CoM/kinematic input L151](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/franka_fr3_duo/fr3_duo.xml#L151) | [macro declaration L16](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L16); [YAML numeric inputs L51](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/fr3v2/inertials.yaml#L51) | [macro declaration L16](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L16); [YAML numeric inputs L51](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/fr3v2/inertials.yaml#L51) |
| left_fr3v2_link5 / com_registered | [0.29424903, 0.782146199, 0.648417077] | [0.294249311, 0.782146629, 0.64841643] | [0.294249311, 0.782146629, 0.64841643] | [2.80820909e-07, 4.29989621e-07, -6.46671244e-07] | eligible; compared after Kabsch alignment | [CoM/kinematic input L161](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/franka_fr3_duo/fr3_duo.xml#L161) | [macro declaration L16](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L16); [YAML numeric inputs L63](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/fr3v2/inertials.yaml#L63) | [macro declaration L16](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L16); [YAML numeric inputs L63](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/fr3v2/inertials.yaml#L63) |
| left_fr3v2_link6 / com_registered | [0.368173813, 0.795014103, 0.663079275] | [0.3681741, 0.795014525, 0.663078607] | [0.3681741, 0.795014525, 0.663078607] | [2.86332529e-07, 4.22253791e-07, -6.67670933e-07] | eligible; compared after Kabsch alignment | [CoM/kinematic input L172](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/franka_fr3_duo/fr3_duo.xml#L172) | [macro declaration L16](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L16); [YAML numeric inputs L75](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/fr3v2/inertials.yaml#L75) | [macro declaration L16](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L16); [YAML numeric inputs L75](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/fr3v2/inertials.yaml#L75) |
| left_fr3v2_link7 / com_registered | [0.342068393, 0.728229187, 0.675191594] | [0.342068663, 0.728229626, 0.675190986] | [0.342068663, 0.728229626, 0.675190986] | [2.69968251e-07, 4.39417597e-07, -6.08302871e-07] | eligible; compared after Kabsch alignment | [CoM/kinematic input L188](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/franka_fr3_duo/fr3_duo.xml#L188) | [macro declaration L16](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L16); [YAML numeric inputs L87](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/fr3v2/inertials.yaml#L87) | [macro declaration L16](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L16); [YAML numeric inputs L87](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/fr3v2/inertials.yaml#L87) |
| left_fr3v2_link8 / com_registered | [0.319982279, 0.622154298, 0.570837242] | [0.319982506, 0.622154656, 0.570836725] | [0.319982506, 0.622154656, 0.570836725] | [2.26825294e-07, 3.58280792e-07, -5.16697242e-07] | eligible; compared after Kabsch alignment | [geometry/inference input L199](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/franka_fr3_duo/fr3_duo.xml#L199) | [geometry/inference input L148](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/franka_arm.xacro#L148) | [geometry/inference input L148](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/franka_arm.xacro#L148) |
| right_fr3v2_link0 / com_registered | [0.0403761948, -0.113103259, 0.0933072135] | [0.0403762178, -0.113103295, 0.0933071605] | [0.0403762178, -0.113103295, 0.0933071605] | [2.30116832e-08, -3.52362219e-08, -5.29905288e-08] | eligible; compared after Kabsch alignment | [CoM/kinematic input L221](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/franka_fr3_duo/fr3_duo.xml#L221) | [macro declaration L16](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L16); [YAML numeric inputs L3](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/fr3v2/inertials.yaml#L3) | [macro declaration L16](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L16); [YAML numeric inputs L3](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/fr3v2/inertials.yaml#L3) |
| right_fr3v2_link1 / com_registered | [0.0901604363, -0.240908467, 0.237341668] | [0.0901605138, -0.240908609, 0.237341501] | [0.0901605138, -0.240908609, 0.237341501] | [7.75327166e-08, -1.42009974e-07, -1.66578236e-07] | eligible; compared after Kabsch alignment | [CoM/kinematic input L224](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/franka_fr3_duo/fr3_duo.xml#L224) | [macro declaration L16](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L16); [YAML numeric inputs L15](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/fr3v2/inertials.yaml#L15) | [macro declaration L16](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L16); [YAML numeric inputs L15](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/fr3v2/inertials.yaml#L15) |
| right_fr3v2_link2 / com_registered | [0.174070936, -0.436469622, 0.359839894] | [0.174071084, -0.436469844, 0.359839552] | [0.174071084, -0.436469844, 0.359839552] | [1.473726e-07, -2.21586576e-07, -3.41457607e-07] | eligible; compared after Kabsch alignment | [CoM/kinematic input L234](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/franka_fr3_duo/fr3_duo.xml#L234) | [macro declaration L16](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L16); [YAML numeric inputs L27](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/fr3v2/inertials.yaml#L27) | [macro declaration L16](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L16); [YAML numeric inputs L27](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/fr3v2/inertials.yaml#L27) |
| right_fr3v2_link3 / com_registered | [0.275412713, -0.51958578, 0.505535817] | [0.275412903, -0.519586096, 0.505535392] | [0.275412903, -0.519586096, 0.505535392] | [1.90049302e-07, -3.15816416e-07, -4.24898266e-07] | eligible; compared after Kabsch alignment | [CoM/kinematic input L244](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/franka_fr3_duo/fr3_duo.xml#L244) | [macro declaration L16](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L16); [YAML numeric inputs L39](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/fr3v2/inertials.yaml#L39) | [macro declaration L16](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L16); [YAML numeric inputs L39](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/fr3v2/inertials.yaml#L39) |
| right_fr3v2_link4 / com_registered | [0.223603517, -0.613235103, 0.501442229] | [0.223603731, -0.613235429, 0.501441733] | [0.223603731, -0.613235429, 0.501441733] | [2.14785091e-07, -3.2639822e-07, -4.95877482e-07] | eligible; compared after Kabsch alignment | [CoM/kinematic input L254](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/franka_fr3_duo/fr3_duo.xml#L254) | [macro declaration L16](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L16); [YAML numeric inputs L51](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/fr3v2/inertials.yaml#L51) | [macro declaration L16](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L16); [YAML numeric inputs L51](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/fr3v2/inertials.yaml#L51) |
| right_fr3v2_link5 / com_registered | [0.286080552, -0.771961381, 0.664039978] | [0.286080832, -0.771961826, 0.664039341] | [0.286080832, -0.771961826, 0.664039341] | [2.80237051e-07, -4.45237153e-07, -6.37036417e-07] | eligible; compared after Kabsch alignment | [CoM/kinematic input L264](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/franka_fr3_duo/fr3_duo.xml#L264) | [macro declaration L16](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L16); [YAML numeric inputs L63](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/fr3v2/inertials.yaml#L63) | [macro declaration L16](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L16); [YAML numeric inputs L63](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/fr3v2/inertials.yaml#L63) |
| right_fr3v2_link6 / com_registered | [0.340069593, -0.759972527, 0.716830956] | [0.340069878, -0.759973001, 0.716830321] | [0.340069878, -0.759973001, 0.716830321] | [2.84323723e-07, -4.7471399e-07, -6.3452164e-07] | eligible; compared after Kabsch alignment | [CoM/kinematic input L275](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/franka_fr3_duo/fr3_duo.xml#L275) | [macro declaration L16](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L16); [YAML numeric inputs L75](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/fr3v2/inertials.yaml#L75) | [macro declaration L16](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L16); [YAML numeric inputs L75](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/fr3v2/inertials.yaml#L75) |
| right_fr3v2_link7 / com_registered | [0.356632838, -0.746388777, 0.647335869] | [0.356633109, -0.746389189, 0.647335244] | [0.356633109, -0.746389189, 0.647335244] | [2.71009274e-07, -4.12231156e-07, -6.25481824e-07] | eligible; compared after Kabsch alignment | [CoM/kinematic input L291](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/franka_fr3_duo/fr3_duo.xml#L291) | [macro declaration L16](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L16); [YAML numeric inputs L87](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/fr3v2/inertials.yaml#L87) | [macro declaration L16](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L16); [YAML numeric inputs L87](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/fr3v2/inertials.yaml#L87) |
| right_fr3v2_link8 / com_registered | [0.319982279, -0.622154298, 0.570837242] | [0.319982506, -0.622154656, 0.570836725] | [0.319982506, -0.622154656, 0.570836725] | [2.26825294e-07, -3.58280792e-07, -5.16697241e-07] | eligible; compared after Kabsch alignment | [geometry/inference input L302](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/franka_fr3_duo/fr3_duo.xml#L302) | [geometry/inference input L148](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/franka_arm.xacro#L148) | [geometry/inference input L148](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/franka_arm.xacro#L148) |

## Mass accounting

Every contributing compiled body mass is listed here so total/subtree sums can be checked. Links point to explicit inertials or to geometry inputs when the compiler inferred a mass. CoM links identify inertial inputs; world coordinates additionally use the ancestor transforms and the registration recorded below.

| M body | M kg / source | S kg / source | H kg / source |
|---|---|---|---|
| base | 4.09385 / [input L98](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/franka_fr3_duo/fr3_duo.xml#L98) | 0 / [macro declaration L62](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/fr3_duo/fr3_duo.urdf.xacro#L62) | 0 / [macro declaration L62](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/fr3_duo/fr3_duo.urdf.xacro#L62) |
| head_link | 0.350865 / [input L104](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/franka_fr3_duo/fr3_duo.xml#L104) | 0.350865 / [geometry/inference input L12](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/accessories/franka_head_v0_2/franka_head.xacro#L12) | 0.350865 / [geometry/inference input L12](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/accessories/franka_head_v0_2/franka_head.xacro#L12) |
| left_fr3v2_link0 | 2.3966 / [input L118](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/franka_fr3_duo/fr3_duo.xml#L118) | 2.3966 / [macro declaration L17](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L17); [YAML numeric inputs L5](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/fr3v2/inertials.yaml#L5) | 2.3966 / [macro declaration L17](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L17); [YAML numeric inputs L5](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/fr3v2/inertials.yaml#L5) |
| left_fr3v2_link1 | 2.4377 / [input L121](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/franka_fr3_duo/fr3_duo.xml#L121) | 2.4377 / [macro declaration L17](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L17); [YAML numeric inputs L17](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/fr3v2/inertials.yaml#L17) | 2.4377 / [macro declaration L17](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L17); [YAML numeric inputs L17](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/fr3v2/inertials.yaml#L17) |
| left_fr3v2_link2 | 2.2375 / [input L131](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/franka_fr3_duo/fr3_duo.xml#L131) | 2.2375 / [macro declaration L17](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L17); [YAML numeric inputs L29](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/fr3v2/inertials.yaml#L29) | 2.2375 / [macro declaration L17](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L17); [YAML numeric inputs L29](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/fr3v2/inertials.yaml#L29) |
| left_fr3v2_link3 | 2.19308 / [input L141](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/franka_fr3_duo/fr3_duo.xml#L141) | 2.193082 / [macro declaration L17](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L17); [YAML numeric inputs L41](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/fr3v2/inertials.yaml#L41) | 2.193082 / [macro declaration L17](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L17); [YAML numeric inputs L41](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/fr3v2/inertials.yaml#L41) |
| left_fr3v2_link4 | 2.18154 / [input L151](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/franka_fr3_duo/fr3_duo.xml#L151) | 2.181537 / [macro declaration L17](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L17); [YAML numeric inputs L53](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/fr3v2/inertials.yaml#L53) | 2.181537 / [macro declaration L17](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L17); [YAML numeric inputs L53](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/fr3v2/inertials.yaml#L53) |
| left_fr3v2_link5 | 2.18688 / [input L161](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/franka_fr3_duo/fr3_duo.xml#L161) | 2.186881 / [macro declaration L17](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L17); [YAML numeric inputs L65](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/fr3v2/inertials.yaml#L65) | 2.186881 / [macro declaration L17](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L17); [YAML numeric inputs L65](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/fr3v2/inertials.yaml#L65) |
| left_fr3v2_link6 | 1.57968 / [input L172](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/franka_fr3_duo/fr3_duo.xml#L172) | 1.579681 / [macro declaration L17](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L17); [YAML numeric inputs L77](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/fr3v2/inertials.yaml#L77) | 1.579681 / [macro declaration L17](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L17); [YAML numeric inputs L77](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/fr3v2/inertials.yaml#L77) |
| left_fr3v2_link7 | 0.694841 / [input L188](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/franka_fr3_duo/fr3_duo.xml#L188) | 0.694841 / [macro declaration L17](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L17); [YAML numeric inputs L89](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/fr3v2/inertials.yaml#L89) | 0.694841 / [macro declaration L17](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L17); [YAML numeric inputs L89](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/fr3v2/inertials.yaml#L89) |
| left_fr3v2_link8 | 0 / [geometry/inference input L199](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/franka_fr3_duo/fr3_duo.xml#L199) | 0 / [geometry/inference input L148](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/franka_arm.xacro#L148) | 0 / [geometry/inference input L148](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/franka_arm.xacro#L148) |
| right_fr3v2_link0 | 2.3966 / [input L221](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/franka_fr3_duo/fr3_duo.xml#L221) | 2.3966 / [macro declaration L17](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L17); [YAML numeric inputs L5](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/fr3v2/inertials.yaml#L5) | 2.3966 / [macro declaration L17](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L17); [YAML numeric inputs L5](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/fr3v2/inertials.yaml#L5) |
| right_fr3v2_link1 | 2.4377 / [input L224](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/franka_fr3_duo/fr3_duo.xml#L224) | 2.4377 / [macro declaration L17](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L17); [YAML numeric inputs L17](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/fr3v2/inertials.yaml#L17) | 2.4377 / [macro declaration L17](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L17); [YAML numeric inputs L17](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/fr3v2/inertials.yaml#L17) |
| right_fr3v2_link2 | 2.2375 / [input L234](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/franka_fr3_duo/fr3_duo.xml#L234) | 2.2375 / [macro declaration L17](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L17); [YAML numeric inputs L29](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/fr3v2/inertials.yaml#L29) | 2.2375 / [macro declaration L17](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L17); [YAML numeric inputs L29](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/fr3v2/inertials.yaml#L29) |
| right_fr3v2_link3 | 2.19308 / [input L244](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/franka_fr3_duo/fr3_duo.xml#L244) | 2.193082 / [macro declaration L17](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L17); [YAML numeric inputs L41](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/fr3v2/inertials.yaml#L41) | 2.193082 / [macro declaration L17](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L17); [YAML numeric inputs L41](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/fr3v2/inertials.yaml#L41) |
| right_fr3v2_link4 | 2.18154 / [input L254](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/franka_fr3_duo/fr3_duo.xml#L254) | 2.181537 / [macro declaration L17](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L17); [YAML numeric inputs L53](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/fr3v2/inertials.yaml#L53) | 2.181537 / [macro declaration L17](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L17); [YAML numeric inputs L53](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/fr3v2/inertials.yaml#L53) |
| right_fr3v2_link5 | 2.18688 / [input L264](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/franka_fr3_duo/fr3_duo.xml#L264) | 2.186881 / [macro declaration L17](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L17); [YAML numeric inputs L65](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/fr3v2/inertials.yaml#L65) | 2.186881 / [macro declaration L17](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L17); [YAML numeric inputs L65](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/fr3v2/inertials.yaml#L65) |
| right_fr3v2_link6 | 1.57968 / [input L275](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/franka_fr3_duo/fr3_duo.xml#L275) | 1.579681 / [macro declaration L17](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L17); [YAML numeric inputs L77](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/fr3v2/inertials.yaml#L77) | 1.579681 / [macro declaration L17](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L17); [YAML numeric inputs L77](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/fr3v2/inertials.yaml#L77) |
| right_fr3v2_link7 | 0.694841 / [input L291](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/franka_fr3_duo/fr3_duo.xml#L291) | 0.694841 / [macro declaration L17](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L17); [YAML numeric inputs L89](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/fr3v2/inertials.yaml#L89) | 0.694841 / [macro declaration L17](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L17); [YAML numeric inputs L89](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/fr3v2/inertials.yaml#L89) |
| right_fr3v2_link8 | 0 / [geometry/inference input L302](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/franka_fr3_duo/fr3_duo.xml#L302) | 0 / [geometry/inference input L148](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/franka_arm.xacro#L148) | 0 / [geometry/inference input L148](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/franka_arm.xacro#L148) |
| upstream-only fr3_duo_mount_left | unavailable | unavailable | 0 / [geometry/inference input L53](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/accessories/fr3_duo_mount_v0_3/fr3_duo_mount.xacro#L53) |
| upstream-only fr3_duo_mount_mounting_point | unavailable | unavailable | 4.093846 / [geometry/inference input L12](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/accessories/fr3_duo_mount_v0_3/fr3_duo_mount.xacro#L12) |
| upstream-only fr3_duo_mount_origin | unavailable | unavailable | 0 / [geometry/inference input L42](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/accessories/fr3_duo_mount_v0_3/fr3_duo_mount.xacro#L42) |
| upstream-only fr3_duo_mount_right | unavailable | unavailable | 0 / [geometry/inference input L53](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/accessories/fr3_duo_mount_v0_3/fr3_duo_mount.xacro#L53) |
| upstream-only head_camera_mounting_point | unavailable | unavailable | 0.001 / [geometry/inference input L34](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/accessories/franka_head_v0_2/franka_head.xacro#L34) |
| upstream-only left_base | unavailable | unavailable | 0 / [macro declaration L26](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/franka_arm.xacro#L26) |
| upstream-only left_fr3v2_hand | unavailable | unavailable | 0.6544 / [geometry/inference input L6](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/end_effectors/franka_hand/franka_hand.srdf.xacro#L6) |
| upstream-only left_fr3v2_hand_tcp | unavailable | unavailable | 0 / [geometry/inference input L37](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/end_effectors/common/franka_hand.xacro#L37) |
| upstream-only left_fr3v2_leftfinger | unavailable | unavailable | 0.0291 / [geometry/inference input L43](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/end_effectors/common/franka_hand.xacro#L43) |
| upstream-only left_fr3v2_link0_accelerometer_bottom | unavailable | unavailable | 0 / [geometry/inference input L204](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L204) |
| upstream-only left_fr3v2_link0_accelerometer_top | unavailable | unavailable | 0 / [geometry/inference input L195](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L195) |
| upstream-only left_fr3v2_link1_accelerometer_bottom | unavailable | unavailable | 0 / [geometry/inference input L204](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L204) |
| upstream-only left_fr3v2_link1_accelerometer_top | unavailable | unavailable | 0 / [geometry/inference input L195](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L195) |
| upstream-only left_fr3v2_link2_accelerometer_bottom | unavailable | unavailable | 0 / [geometry/inference input L204](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L204) |
| upstream-only left_fr3v2_link2_accelerometer_top | unavailable | unavailable | 0 / [geometry/inference input L195](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L195) |
| upstream-only left_fr3v2_link3_accelerometer_bottom | unavailable | unavailable | 0 / [geometry/inference input L204](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L204) |
| upstream-only left_fr3v2_link3_accelerometer_top | unavailable | unavailable | 0 / [geometry/inference input L195](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L195) |
| upstream-only left_fr3v2_link4_accelerometer_bottom | unavailable | unavailable | 0 / [geometry/inference input L204](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L204) |
| upstream-only left_fr3v2_link4_accelerometer_top | unavailable | unavailable | 0 / [geometry/inference input L195](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L195) |
| upstream-only left_fr3v2_link5_accelerometer_bottom | unavailable | unavailable | 0 / [geometry/inference input L204](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L204) |
| upstream-only left_fr3v2_link5_accelerometer_top | unavailable | unavailable | 0 / [geometry/inference input L195](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L195) |
| upstream-only left_fr3v2_rightfinger | unavailable | unavailable | 0.0291 / [geometry/inference input L79](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/end_effectors/common/franka_hand.xacro#L79) |
| upstream-only right_base | unavailable | unavailable | 0 / [macro declaration L26](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/franka_arm.xacro#L26) |
| upstream-only right_fr3v2_hand | unavailable | unavailable | 0.6544 / [geometry/inference input L6](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/end_effectors/franka_hand/franka_hand.srdf.xacro#L6) |
| upstream-only right_fr3v2_hand_tcp | unavailable | unavailable | 0 / [geometry/inference input L37](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/end_effectors/common/franka_hand.xacro#L37) |
| upstream-only right_fr3v2_leftfinger | unavailable | unavailable | 0.0291 / [geometry/inference input L43](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/end_effectors/common/franka_hand.xacro#L43) |
| upstream-only right_fr3v2_link0_accelerometer_bottom | unavailable | unavailable | 0 / [geometry/inference input L204](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L204) |
| upstream-only right_fr3v2_link0_accelerometer_top | unavailable | unavailable | 0 / [geometry/inference input L195](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L195) |
| upstream-only right_fr3v2_link1_accelerometer_bottom | unavailable | unavailable | 0 / [geometry/inference input L204](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L204) |
| upstream-only right_fr3v2_link1_accelerometer_top | unavailable | unavailable | 0 / [geometry/inference input L195](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L195) |
| upstream-only right_fr3v2_link2_accelerometer_bottom | unavailable | unavailable | 0 / [geometry/inference input L204](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L204) |
| upstream-only right_fr3v2_link2_accelerometer_top | unavailable | unavailable | 0 / [geometry/inference input L195](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L195) |
| upstream-only right_fr3v2_link3_accelerometer_bottom | unavailable | unavailable | 0 / [geometry/inference input L204](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L204) |
| upstream-only right_fr3v2_link3_accelerometer_top | unavailable | unavailable | 0 / [geometry/inference input L195](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L195) |
| upstream-only right_fr3v2_link4_accelerometer_bottom | unavailable | unavailable | 0 / [geometry/inference input L204](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L204) |
| upstream-only right_fr3v2_link4_accelerometer_top | unavailable | unavailable | 0 / [geometry/inference input L195](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L195) |
| upstream-only right_fr3v2_link5_accelerometer_bottom | unavailable | unavailable | 0 / [geometry/inference input L204](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L204) |
| upstream-only right_fr3v2_link5_accelerometer_top | unavailable | unavailable | 0 / [geometry/inference input L195](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L195) |
| upstream-only right_fr3v2_rightfinger | unavailable | unavailable | 0.0291 / [geometry/inference input L79](https://github.com/frankarobotics/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/end_effectors/common/franka_hand.xacro#L79) |

## Coverage and unmatched elements

```json
{
  "mapping_h": {
    "bodies": {
      "base": "base",
      "head_link": "head_link",
      "left_fr3v2_link0": "left_fr3v2_link0",
      "left_fr3v2_link1": "left_fr3v2_link1",
      "left_fr3v2_link2": "left_fr3v2_link2",
      "left_fr3v2_link3": "left_fr3v2_link3",
      "left_fr3v2_link4": "left_fr3v2_link4",
      "left_fr3v2_link5": "left_fr3v2_link5",
      "left_fr3v2_link6": "left_fr3v2_link6",
      "left_fr3v2_link7": "left_fr3v2_link7",
      "left_fr3v2_link8": "left_fr3v2_link8",
      "right_fr3v2_link0": "right_fr3v2_link0",
      "right_fr3v2_link1": "right_fr3v2_link1",
      "right_fr3v2_link2": "right_fr3v2_link2",
      "right_fr3v2_link3": "right_fr3v2_link3",
      "right_fr3v2_link4": "right_fr3v2_link4",
      "right_fr3v2_link5": "right_fr3v2_link5",
      "right_fr3v2_link6": "right_fr3v2_link6",
      "right_fr3v2_link7": "right_fr3v2_link7",
      "right_fr3v2_link8": "right_fr3v2_link8"
    },
    "joints": {
      "left_fr3v2_joint1": "left_fr3v2_joint1",
      "left_fr3v2_joint2": "left_fr3v2_joint2",
      "left_fr3v2_joint3": "left_fr3v2_joint3",
      "left_fr3v2_joint4": "left_fr3v2_joint4",
      "left_fr3v2_joint5": "left_fr3v2_joint5",
      "left_fr3v2_joint6": "left_fr3v2_joint6",
      "left_fr3v2_joint7": "left_fr3v2_joint7",
      "right_fr3v2_joint1": "right_fr3v2_joint1",
      "right_fr3v2_joint2": "right_fr3v2_joint2",
      "right_fr3v2_joint3": "right_fr3v2_joint3",
      "right_fr3v2_joint4": "right_fr3v2_joint4",
      "right_fr3v2_joint5": "right_fr3v2_joint5",
      "right_fr3v2_joint6": "right_fr3v2_joint6",
      "right_fr3v2_joint7": "right_fr3v2_joint7"
    },
    "body_methods": {
      "base": "name",
      "head_link": "name",
      "left_fr3v2_link0": "name",
      "left_fr3v2_link1": "name",
      "left_fr3v2_link2": "name",
      "left_fr3v2_link3": "name",
      "left_fr3v2_link4": "name",
      "left_fr3v2_link5": "name",
      "left_fr3v2_link6": "name",
      "left_fr3v2_link7": "name",
      "left_fr3v2_link8": "name",
      "right_fr3v2_link0": "name",
      "right_fr3v2_link1": "name",
      "right_fr3v2_link2": "name",
      "right_fr3v2_link3": "name",
      "right_fr3v2_link4": "name",
      "right_fr3v2_link5": "name",
      "right_fr3v2_link6": "name",
      "right_fr3v2_link7": "name",
      "right_fr3v2_link8": "name"
    },
    "joint_methods": {
      "left_fr3v2_joint1": "name",
      "left_fr3v2_joint2": "name",
      "left_fr3v2_joint3": "name",
      "left_fr3v2_joint4": "name",
      "left_fr3v2_joint5": "name",
      "left_fr3v2_joint6": "name",
      "left_fr3v2_joint7": "name",
      "right_fr3v2_joint1": "name",
      "right_fr3v2_joint2": "name",
      "right_fr3v2_joint3": "name",
      "right_fr3v2_joint4": "name",
      "right_fr3v2_joint5": "name",
      "right_fr3v2_joint6": "name",
      "right_fr3v2_joint7": "name"
    },
    "unmatched_m_bodies": [],
    "unmatched_upstream_bodies": [
      "fr3_duo_mount_left",
      "fr3_duo_mount_mounting_point",
      "fr3_duo_mount_origin",
      "fr3_duo_mount_right",
      "head_camera_mounting_point",
      "left_base",
      "left_fr3v2_hand",
      "left_fr3v2_hand_tcp",
      "left_fr3v2_leftfinger",
      "left_fr3v2_link0_accelerometer_bottom",
      "left_fr3v2_link0_accelerometer_top",
      "left_fr3v2_link1_accelerometer_bottom",
      "left_fr3v2_link1_accelerometer_top",
      "left_fr3v2_link2_accelerometer_bottom",
      "left_fr3v2_link2_accelerometer_top",
      "left_fr3v2_link3_accelerometer_bottom",
      "left_fr3v2_link3_accelerometer_top",
      "left_fr3v2_link4_accelerometer_bottom",
      "left_fr3v2_link4_accelerometer_top",
      "left_fr3v2_link5_accelerometer_bottom",
      "left_fr3v2_link5_accelerometer_top",
      "left_fr3v2_rightfinger",
      "right_base",
      "right_fr3v2_hand",
      "right_fr3v2_hand_tcp",
      "right_fr3v2_leftfinger",
      "right_fr3v2_link0_accelerometer_bottom",
      "right_fr3v2_link0_accelerometer_top",
      "right_fr3v2_link1_accelerometer_bottom",
      "right_fr3v2_link1_accelerometer_top",
      "right_fr3v2_link2_accelerometer_bottom",
      "right_fr3v2_link2_accelerometer_top",
      "right_fr3v2_link3_accelerometer_bottom",
      "right_fr3v2_link3_accelerometer_top",
      "right_fr3v2_link4_accelerometer_bottom",
      "right_fr3v2_link4_accelerometer_top",
      "right_fr3v2_link5_accelerometer_bottom",
      "right_fr3v2_link5_accelerometer_top",
      "right_fr3v2_rightfinger"
    ],
    "unmatched_m_joints": [],
    "unmatched_upstream_joints": [
      "left_fr3v2_finger_joint1",
      "left_fr3v2_finger_joint2",
      "right_fr3v2_finger_joint1",
      "right_fr3v2_finger_joint2"
    ],
    "registration_anchor": {
      "M": "base",
      "H": "base",
      "root_unmatched": false
    }
  },
  "mapping_s": {
    "bodies": {
      "base": "base",
      "head_link": "head_link",
      "left_fr3v2_link0": "left_fr3v2_link0",
      "left_fr3v2_link1": "left_fr3v2_link1",
      "left_fr3v2_link2": "left_fr3v2_link2",
      "left_fr3v2_link3": "left_fr3v2_link3",
      "left_fr3v2_link4": "left_fr3v2_link4",
      "left_fr3v2_link5": "left_fr3v2_link5",
      "left_fr3v2_link6": "left_fr3v2_link6",
      "left_fr3v2_link7": "left_fr3v2_link7",
      "left_fr3v2_link8": "left_fr3v2_link8",
      "right_fr3v2_link0": "right_fr3v2_link0",
      "right_fr3v2_link1": "right_fr3v2_link1",
      "right_fr3v2_link2": "right_fr3v2_link2",
      "right_fr3v2_link3": "right_fr3v2_link3",
      "right_fr3v2_link4": "right_fr3v2_link4",
      "right_fr3v2_link5": "right_fr3v2_link5",
      "right_fr3v2_link6": "right_fr3v2_link6",
      "right_fr3v2_link7": "right_fr3v2_link7",
      "right_fr3v2_link8": "right_fr3v2_link8"
    },
    "joints": {
      "left_fr3v2_joint1": "left_fr3v2_joint1",
      "left_fr3v2_joint2": "left_fr3v2_joint2",
      "left_fr3v2_joint3": "left_fr3v2_joint3",
      "left_fr3v2_joint4": "left_fr3v2_joint4",
      "left_fr3v2_joint5": "left_fr3v2_joint5",
      "left_fr3v2_joint6": "left_fr3v2_joint6",
      "left_fr3v2_joint7": "left_fr3v2_joint7",
      "right_fr3v2_joint1": "right_fr3v2_joint1",
      "right_fr3v2_joint2": "right_fr3v2_joint2",
      "right_fr3v2_joint3": "right_fr3v2_joint3",
      "right_fr3v2_joint4": "right_fr3v2_joint4",
      "right_fr3v2_joint5": "right_fr3v2_joint5",
      "right_fr3v2_joint6": "right_fr3v2_joint6",
      "right_fr3v2_joint7": "right_fr3v2_joint7"
    },
    "body_methods": {
      "base": "name",
      "head_link": "name",
      "left_fr3v2_link0": "name",
      "left_fr3v2_link1": "name",
      "left_fr3v2_link2": "name",
      "left_fr3v2_link3": "name",
      "left_fr3v2_link4": "name",
      "left_fr3v2_link5": "name",
      "left_fr3v2_link6": "name",
      "left_fr3v2_link7": "name",
      "left_fr3v2_link8": "name",
      "right_fr3v2_link0": "name",
      "right_fr3v2_link1": "name",
      "right_fr3v2_link2": "name",
      "right_fr3v2_link3": "name",
      "right_fr3v2_link4": "name",
      "right_fr3v2_link5": "name",
      "right_fr3v2_link6": "name",
      "right_fr3v2_link7": "name",
      "right_fr3v2_link8": "name"
    },
    "joint_methods": {
      "left_fr3v2_joint1": "name",
      "left_fr3v2_joint2": "name",
      "left_fr3v2_joint3": "name",
      "left_fr3v2_joint4": "name",
      "left_fr3v2_joint5": "name",
      "left_fr3v2_joint6": "name",
      "left_fr3v2_joint7": "name",
      "right_fr3v2_joint1": "name",
      "right_fr3v2_joint2": "name",
      "right_fr3v2_joint3": "name",
      "right_fr3v2_joint4": "name",
      "right_fr3v2_joint5": "name",
      "right_fr3v2_joint6": "name",
      "right_fr3v2_joint7": "name"
    },
    "unmatched_m_bodies": [],
    "unmatched_upstream_bodies": [
      "fr3_duo_mount_left",
      "fr3_duo_mount_mounting_point",
      "fr3_duo_mount_origin",
      "fr3_duo_mount_right",
      "head_camera_mounting_point",
      "left_base",
      "left_fr3v2_hand",
      "left_fr3v2_hand_tcp",
      "left_fr3v2_leftfinger",
      "left_fr3v2_link0_accelerometer_bottom",
      "left_fr3v2_link0_accelerometer_top",
      "left_fr3v2_link1_accelerometer_bottom",
      "left_fr3v2_link1_accelerometer_top",
      "left_fr3v2_link2_accelerometer_bottom",
      "left_fr3v2_link2_accelerometer_top",
      "left_fr3v2_link3_accelerometer_bottom",
      "left_fr3v2_link3_accelerometer_top",
      "left_fr3v2_link4_accelerometer_bottom",
      "left_fr3v2_link4_accelerometer_top",
      "left_fr3v2_link5_accelerometer_bottom",
      "left_fr3v2_link5_accelerometer_top",
      "left_fr3v2_rightfinger",
      "right_base",
      "right_fr3v2_hand",
      "right_fr3v2_hand_tcp",
      "right_fr3v2_leftfinger",
      "right_fr3v2_link0_accelerometer_bottom",
      "right_fr3v2_link0_accelerometer_top",
      "right_fr3v2_link1_accelerometer_bottom",
      "right_fr3v2_link1_accelerometer_top",
      "right_fr3v2_link2_accelerometer_bottom",
      "right_fr3v2_link2_accelerometer_top",
      "right_fr3v2_link3_accelerometer_bottom",
      "right_fr3v2_link3_accelerometer_top",
      "right_fr3v2_link4_accelerometer_bottom",
      "right_fr3v2_link4_accelerometer_top",
      "right_fr3v2_link5_accelerometer_bottom",
      "right_fr3v2_link5_accelerometer_top",
      "right_fr3v2_rightfinger"
    ],
    "unmatched_m_joints": [],
    "unmatched_upstream_joints": [
      "left_fr3v2_finger_joint1",
      "left_fr3v2_finger_joint2",
      "right_fr3v2_finger_joint1",
      "right_fr3v2_finger_joint2"
    ],
    "registration_anchor": {
      "M": "base",
      "S": "base"
    }
  },
  "unavailable": [
    {
      "entity": "left_fr3v2_joint1",
      "other_entity": "left_fr3v2_joint1",
      "quantity": "force",
      "tolerance": "limit",
      "m": 87.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_fr3v2_joint1",
      "other_entity": "left_fr3v2_joint1",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 2.62,
      "s": 2.62,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_fr3v2_joint2",
      "other_entity": "left_fr3v2_joint2",
      "quantity": "force",
      "tolerance": "limit",
      "m": 87.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_fr3v2_joint2",
      "other_entity": "left_fr3v2_joint2",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 2.62,
      "s": 2.62,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_fr3v2_joint3",
      "other_entity": "left_fr3v2_joint3",
      "quantity": "force",
      "tolerance": "limit",
      "m": 87.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_fr3v2_joint3",
      "other_entity": "left_fr3v2_joint3",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 2.62,
      "s": 2.62,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_fr3v2_joint4",
      "other_entity": "left_fr3v2_joint4",
      "quantity": "force",
      "tolerance": "limit",
      "m": 87.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_fr3v2_joint4",
      "other_entity": "left_fr3v2_joint4",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 2.62,
      "s": 2.62,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_fr3v2_joint5",
      "other_entity": "left_fr3v2_joint5",
      "quantity": "force",
      "tolerance": "limit",
      "m": 12.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_fr3v2_joint5",
      "other_entity": "left_fr3v2_joint5",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 5.26,
      "s": 5.26,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_fr3v2_joint6",
      "other_entity": "left_fr3v2_joint6",
      "quantity": "force",
      "tolerance": "limit",
      "m": 12.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_fr3v2_joint6",
      "other_entity": "left_fr3v2_joint6",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 4.18,
      "s": 4.18,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_fr3v2_joint7",
      "other_entity": "left_fr3v2_joint7",
      "quantity": "force",
      "tolerance": "limit",
      "m": 12.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_fr3v2_joint7",
      "other_entity": "left_fr3v2_joint7",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 5.26,
      "s": 5.26,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "right_fr3v2_joint1",
      "other_entity": "right_fr3v2_joint1",
      "quantity": "force",
      "tolerance": "limit",
      "m": 87.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "right_fr3v2_joint1",
      "other_entity": "right_fr3v2_joint1",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 2.62,
      "s": 2.62,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "right_fr3v2_joint2",
      "other_entity": "right_fr3v2_joint2",
      "quantity": "force",
      "tolerance": "limit",
      "m": 87.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "right_fr3v2_joint2",
      "other_entity": "right_fr3v2_joint2",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 2.62,
      "s": 2.62,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "right_fr3v2_joint3",
      "other_entity": "right_fr3v2_joint3",
      "quantity": "force",
      "tolerance": "limit",
      "m": 87.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "right_fr3v2_joint3",
      "other_entity": "right_fr3v2_joint3",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 2.62,
      "s": 2.62,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "right_fr3v2_joint4",
      "other_entity": "right_fr3v2_joint4",
      "quantity": "force",
      "tolerance": "limit",
      "m": 87.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "right_fr3v2_joint4",
      "other_entity": "right_fr3v2_joint4",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 2.62,
      "s": 2.62,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "right_fr3v2_joint5",
      "other_entity": "right_fr3v2_joint5",
      "quantity": "force",
      "tolerance": "limit",
      "m": 12.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "right_fr3v2_joint5",
      "other_entity": "right_fr3v2_joint5",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 5.26,
      "s": 5.26,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "right_fr3v2_joint6",
      "other_entity": "right_fr3v2_joint6",
      "quantity": "force",
      "tolerance": "limit",
      "m": 12.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "right_fr3v2_joint6",
      "other_entity": "right_fr3v2_joint6",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 4.18,
      "s": 4.18,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "right_fr3v2_joint7",
      "other_entity": "right_fr3v2_joint7",
      "quantity": "force",
      "tolerance": "limit",
      "m": 12.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "right_fr3v2_joint7",
      "other_entity": "right_fr3v2_joint7",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 5.26,
      "s": 5.26,
      "reason": "quantity absent or not enforced/declared on one side"
    }
  ]
}
```

## Limits unavailable for a like-for-like simulator comparison

URDF effort and velocity tags are manufacturer declarations; MuJoCo ignores them. Missing enforced quantities are not interpreted as zero. The available values are shown for review and excluded from STALE counts.

| Joint / quantity | M | S | H / declared upstream |
|---|---|---|---|
| left_fr3v2_joint1 / force | 87 | unavailable | unavailable |
| left_fr3v2_joint1 / velocity | unavailable | 2.62 | 2.62 |
| left_fr3v2_joint2 / force | 87 | unavailable | unavailable |
| left_fr3v2_joint2 / velocity | unavailable | 2.62 | 2.62 |
| left_fr3v2_joint3 / force | 87 | unavailable | unavailable |
| left_fr3v2_joint3 / velocity | unavailable | 2.62 | 2.62 |
| left_fr3v2_joint4 / force | 87 | unavailable | unavailable |
| left_fr3v2_joint4 / velocity | unavailable | 2.62 | 2.62 |
| left_fr3v2_joint5 / force | 12 | unavailable | unavailable |
| left_fr3v2_joint5 / velocity | unavailable | 5.26 | 5.26 |
| left_fr3v2_joint6 / force | 12 | unavailable | unavailable |
| left_fr3v2_joint6 / velocity | unavailable | 4.18 | 4.18 |
| left_fr3v2_joint7 / force | 12 | unavailable | unavailable |
| left_fr3v2_joint7 / velocity | unavailable | 5.26 | 5.26 |
| right_fr3v2_joint1 / force | 87 | unavailable | unavailable |
| right_fr3v2_joint1 / velocity | unavailable | 2.62 | 2.62 |
| right_fr3v2_joint2 / force | 87 | unavailable | unavailable |
| right_fr3v2_joint2 / velocity | unavailable | 2.62 | 2.62 |
| right_fr3v2_joint3 / force | 87 | unavailable | unavailable |
| right_fr3v2_joint3 / velocity | unavailable | 2.62 | 2.62 |
| right_fr3v2_joint4 / force | 87 | unavailable | unavailable |
| right_fr3v2_joint4 / velocity | unavailable | 2.62 | 2.62 |
| right_fr3v2_joint5 / force | 12 | unavailable | unavailable |
| right_fr3v2_joint5 / velocity | unavailable | 5.26 | 5.26 |
| right_fr3v2_joint6 / force | 12 | unavailable | unavailable |
| right_fr3v2_joint6 / velocity | unavailable | 4.18 | 4.18 |
| right_fr3v2_joint7 / force | 12 | unavailable | unavailable |
| right_fr3v2_joint7 / velocity | unavailable | 5.26 | 5.26 |
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
  "https://github.com/frankarobotics/franka_description robots/fr3_duo/fr3_duo.xacro at 7aeeddc449edf8d62b594f9e36a81da53e7796f9: ValueError: Macro fr3_duo requires unsupported explicit arguments: ['robot_types', 'hand', 'ee_id', 'special_connection', 'xyz_ee', 'rpy_ee', 'tcp_xyz', 'tcp_rpy', 'safety_distance', 'with_sc', 'include_self_collision_geometry', 'description_pkg', 'base_mount', 'connected_to', 'arm_prefixes', '**arm0_extras', '**arm1_extras']"
]
```

## History inputs

```json
[
  "accessories/fr3_duo_mount_v0_3/fr3_duo_mount.xacro",
  "accessories/fr3_duo_mount_v0_3/inertials.yaml",
  "accessories/fr3_duo_mount_v0_3/kinematics.yaml",
  "accessories/franka_head_v0_2/franka_head.xacro",
  "accessories/franka_head_v0_2/inertials.yaml",
  "accessories/franka_head_v0_2/kinematics.yaml",
  "end_effectors/common/franka_hand.xacro",
  "end_effectors/common/utils.xacro",
  "end_effectors/franka_hand/franka_hand_arguments.xacro",
  "end_effectors/franka_hand/inertials.yaml",
  "meshes/accessories/fr3_duo_mount/collision/fr3_duo_cover.stl",
  "meshes/accessories/fr3_duo_mount/collision/fr3_duo_mount.stl",
  "meshes/accessories/fr3_duo_mount/visual/fr3_duo_cover.dae",
  "meshes/accessories/fr3_duo_mount/visual/fr3_duo_mount.dae",
  "meshes/accessories/fr3_duo_mount_v0_3/collision/fr3_duo_cover.stl",
  "meshes/accessories/fr3_duo_mount_v0_3/collision/fr3_duo_mount.stl",
  "meshes/accessories/fr3_duo_mount_v0_3/visual/fr3_duo_cover.dae",
  "meshes/accessories/fr3_duo_mount_v0_3/visual/fr3_duo_mount.dae",
  "meshes/accessories/franka_head_v0_2/collision/franka_head.stl",
  "meshes/accessories/franka_head_v0_2/visual/franka_head.dae",
  "meshes/robot_arms/fr3/collision/link0.stl",
  "meshes/robot_arms/fr3/collision/link1.stl",
  "meshes/robot_arms/fr3/collision/link2.stl",
  "meshes/robot_arms/fr3/collision/link3.stl",
  "meshes/robot_arms/fr3/collision/link4.stl",
  "meshes/robot_arms/fr3/collision/link5.stl",
  "meshes/robot_arms/fr3/collision/link6.stl",
  "meshes/robot_arms/fr3/collision/link7.stl",
  "meshes/robot_arms/fr3/visual/link0.dae",
  "meshes/robot_arms/fr3/visual/link1.dae",
  "meshes/robot_arms/fr3/visual/link2.dae",
  "meshes/robot_arms/fr3/visual/link3.dae",
  "meshes/robot_arms/fr3/visual/link4.dae",
  "meshes/robot_arms/fr3/visual/link5.dae",
  "meshes/robot_arms/fr3/visual/link6.dae",
  "meshes/robot_arms/fr3/visual/link7.dae",
  "meshes/robot_arms/fr3_duo/cover/collision/fr3_duo_cover.stl",
  "meshes/robot_arms/fr3_duo/cover/visual/fr3_duo_cover.dae",
  "meshes/robot_arms/fr3_duo/mount/collision/fr3_duo_mount.stl",
  "meshes/robot_arms/fr3_duo/mount/visual/fr3_duo_mount.dae",
  "meshes/robot_arms/fr3_duo/mount/visual/fr3_duo_mount.stl",
  "meshes/robot_arms/fr3v2/collision/link0.stl",
  "meshes/robot_arms/fr3v2/collision/link1.stl",
  "meshes/robot_arms/fr3v2/collision/link2.stl",
  "meshes/robot_arms/fr3v2/collision/link3.stl",
  "meshes/robot_arms/fr3v2/collision/link4.stl",
  "meshes/robot_arms/fr3v2/collision/link5.stl",
  "meshes/robot_arms/fr3v2/collision/link6.stl",
  "meshes/robot_arms/fr3v2/collision/link7.stl",
  "meshes/robot_arms/fr3v2/visual/link0.dae",
  "meshes/robot_arms/fr3v2/visual/link1.dae",
  "meshes/robot_arms/fr3v2/visual/link2.dae",
  "meshes/robot_arms/fr3v2/visual/link3.dae",
  "meshes/robot_arms/fr3v2/visual/link4.dae",
  "meshes/robot_arms/fr3v2/visual/link5.dae",
  "meshes/robot_arms/fr3v2/visual/link6.dae",
  "meshes/robot_arms/fr3v2/visual/link7.dae",
  "meshes/robot_ee/franka_hand_white/collision/hand.stl",
  "meshes/robot_ee/franka_hand_white/visual/finger.dae",
  "meshes/robot_ee/franka_hand_white/visual/hand.dae",
  "meshes/robots/fr3/collision/link0.stl",
  "meshes/robots/fr3/collision/link1.stl",
  "meshes/robots/fr3/collision/link2.stl",
  "meshes/robots/fr3/collision/link3.stl",
  "meshes/robots/fr3/collision/link4.stl",
  "meshes/robots/fr3/collision/link5.stl",
  "meshes/robots/fr3/collision/link6.stl",
  "meshes/robots/fr3/collision/link7.stl",
  "meshes/robots/fr3/visual/link0.dae",
  "meshes/robots/fr3/visual/link1.dae",
  "meshes/robots/fr3/visual/link2.dae",
  "meshes/robots/fr3/visual/link3.dae",
  "meshes/robots/fr3/visual/link4.dae",
  "meshes/robots/fr3/visual/link5.dae",
  "meshes/robots/fr3/visual/link6.dae",
  "meshes/robots/fr3/visual/link7.dae",
  "meshes/robots/fr3v2/collision/link0.stl",
  "meshes/robots/fr3v2/collision/link1.stl",
  "meshes/robots/fr3v2/collision/link2.stl",
  "meshes/robots/fr3v2/collision/link3.stl",
  "meshes/robots/fr3v2/collision/link4.stl",
  "meshes/robots/fr3v2/collision/link5.stl",
  "meshes/robots/fr3v2/collision/link6.stl",
  "meshes/robots/fr3v2/collision/link7.stl",
  "meshes/robots/fr3v2/visual/link0.dae",
  "meshes/robots/fr3v2/visual/link1.dae",
  "meshes/robots/fr3v2/visual/link2.dae",
  "meshes/robots/fr3v2/visual/link3.dae",
  "meshes/robots/fr3v2/visual/link4.dae",
  "meshes/robots/fr3v2/visual/link5.dae",
  "meshes/robots/fr3v2/visual/link6.dae",
  "meshes/robots/fr3v2/visual/link7.dae",
  "robots/common/franka_arm.xacro",
  "robots/common/franka_robot.xacro",
  "robots/common/utils.xacro",
  "robots/fr3/accelerometers.yaml",
  "robots/fr3/dynamics.yaml",
  "robots/fr3/inertials.yaml",
  "robots/fr3/joint_limits.yaml",
  "robots/fr3/kinematics.yaml",
  "robots/fr3_duo/fr3_duo.ros2_control.xacro",
  "robots/fr3_duo/fr3_duo.urdf.xacro",
  "robots/fr3_duo/fr3_duo.xacro",
  "robots/fr3_duo/fr3_duo_cover/fr3_duo_cover.xacro",
  "robots/fr3_duo/fr3_duo_cover/inertials.yaml",
  "robots/fr3_duo/fr3_duo_mount/fr3_duo_mount.xacro",
  "robots/fr3_duo/fr3_duo_mount/inertials.yaml",
  "robots/fr3_duo/fr3_duo_mount/kinematics.yaml",
  "robots/fr3v2/accelerometers.yaml",
  "robots/fr3v2/dynamics.yaml",
  "robots/fr3v2/inertials.yaml",
  "robots/fr3v2/joint_limits.yaml",
  "robots/fr3v2/kinematics.yaml"
]
```

## Self comparisons

```json
[
  {
    "file": "franka_fr3_duo/fr3_duo.xml",
    "status": "passed",
    "findings": 0
  },
  {
    "file": "franka_fr3_duo/fr3_duo_with_spine.xml",
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
    "counts": {
      "undocumented derivation difference": 25
    },
    "classifications_changed": 1,
    "finding_membership_changes": 1
  },
  "2": {
    "provenance_method": "pinned",
    "counts": {
      "undocumented derivation difference": 24
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
    "geometry_stripped": false,
    "missing_explicit_inertials": [
      "left_fr3v2_link8",
      "right_fr3v2_link8"
    ],
    "assets_loaded": 58,
    "mesh_conversions": [],
    "nonphysical_normalizations": [],
    "xacro_arguments": {},
    "source_dependencies": [
      "franka_fr3_duo/fr3_duo.xml",
      "franka_fr3_duo/assets/fr3_duo_mount.obj",
      "franka_fr3_duo/assets/fr3_duo_cover.obj",
      "franka_fr3_duo/assets/franka_head.obj",
      "franka_fr3_duo/assets/fr3_duo_mount.stl",
      "franka_fr3_duo/assets/fr3_duo_cover.stl",
      "franka_fr3_duo/assets/franka_head.stl",
      "franka_fr3_duo/assets/link0_0.obj",
      "franka_fr3_duo/assets/link0_1.obj",
      "franka_fr3_duo/assets/link0_2.obj",
      "franka_fr3_duo/assets/link0_3.obj",
      "franka_fr3_duo/assets/link0_4.obj",
      "franka_fr3_duo/assets/link0_5.obj",
      "franka_fr3_duo/assets/link1_0.obj",
      "franka_fr3_duo/assets/link1_1.obj",
      "franka_fr3_duo/assets/link1_2.obj",
      "franka_fr3_duo/assets/link1_3.obj",
      "franka_fr3_duo/assets/link2_0.obj",
      "franka_fr3_duo/assets/link2_1.obj",
      "franka_fr3_duo/assets/link2_2.obj",
      "franka_fr3_duo/assets/link2_3.obj",
      "franka_fr3_duo/assets/link3_0.obj",
      "franka_fr3_duo/assets/link3_1.obj",
      "franka_fr3_duo/assets/link3_2.obj",
      "franka_fr3_duo/assets/link3_3.obj",
      "franka_fr3_duo/assets/link4_0.obj",
      "franka_fr3_duo/assets/link4_1.obj",
      "franka_fr3_duo/assets/link4_2.obj",
      "franka_fr3_duo/assets/link4_3.obj",
      "franka_fr3_duo/assets/link5_0.obj",
      "franka_fr3_duo/assets/link5_1.obj",
      "franka_fr3_duo/assets/link5_2.obj",
      "franka_fr3_duo/assets/link5_3.obj",
      "franka_fr3_duo/assets/link5_4.obj",
      "franka_fr3_duo/assets/link6_0.obj",
      "franka_fr3_duo/assets/link6_1.obj",
      "franka_fr3_duo/assets/link6_2.obj",
      "franka_fr3_duo/assets/link6_3.obj",
      "franka_fr3_duo/assets/link6_4.obj",
      "franka_fr3_duo/assets/link6_5.obj",
      "franka_fr3_duo/assets/link6_6.obj",
      "franka_fr3_duo/assets/link6_7.obj",
      "franka_fr3_duo/assets/link6_8.obj",
      "franka_fr3_duo/assets/link6_9.obj",
      "franka_fr3_duo/assets/link7_0.obj",
      "franka_fr3_duo/assets/link7_1.obj",
      "franka_fr3_duo/assets/link7_2.obj",
      "franka_fr3_duo/assets/link7_3.obj",
      "franka_fr3_duo/assets/link7_4.obj",
      "franka_fr3_duo/assets/link7_5.obj",
      "franka_fr3_duo/assets/link7_6.obj",
      "franka_fr3_duo/assets/link0.stl",
      "franka_fr3_duo/assets/link1.stl",
      "franka_fr3_duo/assets/link2.stl",
      "franka_fr3_duo/assets/link3.stl",
      "franka_fr3_duo/assets/link4.stl",
      "franka_fr3_duo/assets/link5.stl",
      "franka_fr3_duo/assets/link6.stl",
      "franka_fr3_duo/assets/link7.stl"
    ],
    "registration": {
      "translation": [
        0.0,
        0.0,
        0.030814
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
      "fr3_duo_mount_origin",
      "fr3_duo_mount_left",
      "fr3_duo_mount_right",
      "left_base",
      "left_fr3v2_link0_accelerometer_top",
      "left_fr3v2_link0_accelerometer_bottom",
      "left_fr3v2_link1_accelerometer_top",
      "left_fr3v2_link1_accelerometer_bottom",
      "left_fr3v2_link2_accelerometer_top",
      "left_fr3v2_link2_accelerometer_bottom",
      "left_fr3v2_link3_accelerometer_top",
      "left_fr3v2_link3_accelerometer_bottom",
      "left_fr3v2_link4_accelerometer_top",
      "left_fr3v2_link4_accelerometer_bottom",
      "left_fr3v2_link5_accelerometer_top",
      "left_fr3v2_link5_accelerometer_bottom",
      "left_fr3v2_link8",
      "left_fr3v2_hand_tcp",
      "right_base",
      "right_fr3v2_link0_accelerometer_top",
      "right_fr3v2_link0_accelerometer_bottom",
      "right_fr3v2_link1_accelerometer_top",
      "right_fr3v2_link1_accelerometer_bottom",
      "right_fr3v2_link2_accelerometer_top",
      "right_fr3v2_link2_accelerometer_bottom",
      "right_fr3v2_link3_accelerometer_top",
      "right_fr3v2_link3_accelerometer_bottom",
      "right_fr3v2_link4_accelerometer_top",
      "right_fr3v2_link4_accelerometer_bottom",
      "right_fr3v2_link5_accelerometer_top",
      "right_fr3v2_link5_accelerometer_bottom",
      "right_fr3v2_link8",
      "right_fr3v2_hand_tcp"
    ],
    "assets_loaded": 46,
    "mesh_conversions": [
      {
        "file": "meshes/accessories/fr3_duo_mount_v0_3/visual/fr3_duo_mount.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "meshes/accessories/fr3_duo_mount_v0_3/visual/fr3_duo_cover.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "meshes/accessories/franka_head_v0_2/visual/franka_head.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "meshes/robots/fr3v2/visual/link0.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "meshes/robots/fr3v2/visual/link1.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "meshes/robots/fr3v2/visual/link2.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "meshes/robots/fr3v2/visual/link3.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "meshes/robots/fr3v2/visual/link4.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "meshes/robots/fr3v2/visual/link5.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "meshes/robots/fr3v2/visual/link6.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "meshes/robots/fr3v2/visual/link7.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "meshes/robot_ee/franka_hand_white/visual/hand.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "meshes/robot_ee/franka_hand_white/visual/finger.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "meshes/robot_ee/franka_hand_white/visual/finger.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "meshes/robots/fr3v2/visual/link0.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "meshes/robots/fr3v2/visual/link1.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "meshes/robots/fr3v2/visual/link2.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "meshes/robots/fr3v2/visual/link3.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "meshes/robots/fr3v2/visual/link4.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "meshes/robots/fr3v2/visual/link5.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "meshes/robots/fr3v2/visual/link6.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "meshes/robots/fr3v2/visual/link7.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "meshes/robot_ee/franka_hand_white/visual/hand.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "meshes/robot_ee/franka_hand_white/visual/finger.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "meshes/robot_ee/franka_hand_white/visual/finger.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      }
    ],
    "nonphysical_normalizations": [],
    "xacro_arguments": {
      "robot_types": "['fr3v2','fr3v2']",
      "no_prefix": "false",
      "hand": "true",
      "ee_id": "franka_hand",
      "special_connection": "",
      "xyz_ee": "0 0 0",
      "rpy_ee": "0 0 -0.7853981633974483",
      "tcp_xyz": "",
      "tcp_rpy": "0 0 0",
      "safety_distance": "0.03",
      "with_sc": "false",
      "include_self_collision_geometry": "true",
      "description_pkg": "franka_description",
      "arm_prefixes": "['left','right']",
      "xyz": "0 0 0",
      "rpy": "0 0 0",
      "base_mount": "base"
    },
    "source_dependencies": [
      "accessories/fr3_duo_mount_v0_3/fr3_duo_mount.xacro",
      "accessories/fr3_duo_mount_v0_3/inertials.yaml",
      "accessories/fr3_duo_mount_v0_3/kinematics.yaml",
      "accessories/franka_head_v0_2/franka_head.xacro",
      "accessories/franka_head_v0_2/inertials.yaml",
      "accessories/franka_head_v0_2/kinematics.yaml",
      "end_effectors/common/franka_hand.xacro",
      "end_effectors/common/utils.xacro",
      "end_effectors/franka_hand/inertials.yaml",
      "robots/common/franka_arm.xacro",
      "robots/common/franka_robot.xacro",
      "robots/common/utils.xacro",
      "robots/fr3_duo/fr3_duo.urdf.xacro",
      "robots/fr3_duo/fr3_duo.xacro",
      "robots/fr3v2/accelerometers.yaml",
      "robots/fr3v2/dynamics.yaml",
      "robots/fr3v2/inertials.yaml",
      "robots/fr3v2/joint_limits.yaml",
      "robots/fr3v2/kinematics.yaml",
      "meshes/accessories/fr3_duo_mount_v0_3/visual/fr3_duo_mount.dae",
      "meshes/accessories/fr3_duo_mount_v0_3/visual/fr3_duo_cover.dae",
      "meshes/accessories/fr3_duo_mount_v0_3/collision/fr3_duo_mount.stl",
      "meshes/accessories/fr3_duo_mount_v0_3/collision/fr3_duo_cover.stl",
      "meshes/accessories/franka_head_v0_2/visual/franka_head.dae",
      "meshes/accessories/franka_head_v0_2/collision/franka_head.stl",
      "meshes/robots/fr3v2/visual/link0.dae",
      "meshes/robots/fr3v2/collision/link0.stl",
      "meshes/robots/fr3v2/visual/link1.dae",
      "meshes/robots/fr3v2/collision/link1.stl",
      "meshes/robots/fr3v2/visual/link2.dae",
      "meshes/robots/fr3v2/collision/link2.stl",
      "meshes/robots/fr3v2/visual/link3.dae",
      "meshes/robots/fr3v2/collision/link3.stl",
      "meshes/robots/fr3v2/visual/link4.dae",
      "meshes/robots/fr3v2/collision/link4.stl",
      "meshes/robots/fr3v2/visual/link5.dae",
      "meshes/robots/fr3v2/collision/link5.stl",
      "meshes/robots/fr3v2/visual/link6.dae",
      "meshes/robots/fr3v2/collision/link6.stl",
      "meshes/robots/fr3v2/visual/link7.dae",
      "meshes/robots/fr3v2/collision/link7.stl",
      "meshes/robot_ee/franka_hand_white/visual/hand.dae",
      "meshes/robot_ee/franka_hand_white/collision/hand.stl",
      "meshes/robot_ee/franka_hand_white/visual/finger.dae",
      "meshes/robot_ee/franka_hand_white/visual/finger.dae",
      "meshes/robots/fr3v2/visual/link0.dae",
      "meshes/robots/fr3v2/collision/link0.stl",
      "meshes/robots/fr3v2/visual/link1.dae",
      "meshes/robots/fr3v2/collision/link1.stl",
      "meshes/robots/fr3v2/visual/link2.dae",
      "meshes/robots/fr3v2/collision/link2.stl",
      "meshes/robots/fr3v2/visual/link3.dae",
      "meshes/robots/fr3v2/collision/link3.stl",
      "meshes/robots/fr3v2/visual/link4.dae",
      "meshes/robots/fr3v2/collision/link4.stl",
      "meshes/robots/fr3v2/visual/link5.dae",
      "meshes/robots/fr3v2/collision/link5.stl",
      "meshes/robots/fr3v2/visual/link6.dae",
      "meshes/robots/fr3v2/collision/link6.stl",
      "meshes/robots/fr3v2/visual/link7.dae",
      "meshes/robots/fr3v2/collision/link7.stl",
      "meshes/robot_ee/franka_hand_white/visual/hand.dae",
      "meshes/robot_ee/franka_hand_white/collision/hand.stl",
      "meshes/robot_ee/franka_hand_white/visual/finger.dae",
      "meshes/robot_ee/franka_hand_white/visual/finger.dae"
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
      "base",
      "fr3_duo_mount_origin",
      "fr3_duo_mount_left",
      "fr3_duo_mount_right",
      "left_base",
      "left_fr3v2_link0_accelerometer_top",
      "left_fr3v2_link0_accelerometer_bottom",
      "left_fr3v2_link1_accelerometer_top",
      "left_fr3v2_link1_accelerometer_bottom",
      "left_fr3v2_link2_accelerometer_top",
      "left_fr3v2_link2_accelerometer_bottom",
      "left_fr3v2_link3_accelerometer_top",
      "left_fr3v2_link3_accelerometer_bottom",
      "left_fr3v2_link4_accelerometer_top",
      "left_fr3v2_link4_accelerometer_bottom",
      "left_fr3v2_link5_accelerometer_top",
      "left_fr3v2_link5_accelerometer_bottom",
      "left_fr3v2_link8",
      "left_fr3v2_hand_tcp",
      "right_base",
      "right_fr3v2_link0_accelerometer_top",
      "right_fr3v2_link0_accelerometer_bottom",
      "right_fr3v2_link1_accelerometer_top",
      "right_fr3v2_link1_accelerometer_bottom",
      "right_fr3v2_link2_accelerometer_top",
      "right_fr3v2_link2_accelerometer_bottom",
      "right_fr3v2_link3_accelerometer_top",
      "right_fr3v2_link3_accelerometer_bottom",
      "right_fr3v2_link4_accelerometer_top",
      "right_fr3v2_link4_accelerometer_bottom",
      "right_fr3v2_link5_accelerometer_top",
      "right_fr3v2_link5_accelerometer_bottom",
      "right_fr3v2_link8",
      "right_fr3v2_hand_tcp"
    ],
    "assets_loaded": 46,
    "mesh_conversions": [
      {
        "file": "meshes/accessories/fr3_duo_mount_v0_3/visual/fr3_duo_mount.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "meshes/accessories/fr3_duo_mount_v0_3/visual/fr3_duo_cover.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "meshes/accessories/franka_head_v0_2/visual/franka_head.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "meshes/robots/fr3v2/visual/link0.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "meshes/robots/fr3v2/visual/link1.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "meshes/robots/fr3v2/visual/link2.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "meshes/robots/fr3v2/visual/link3.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "meshes/robots/fr3v2/visual/link4.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "meshes/robots/fr3v2/visual/link5.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "meshes/robots/fr3v2/visual/link6.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "meshes/robots/fr3v2/visual/link7.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "meshes/robot_ee/franka_hand_white/visual/hand.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "meshes/robot_ee/franka_hand_white/visual/finger.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "meshes/robot_ee/franka_hand_white/visual/finger.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "meshes/robots/fr3v2/visual/link0.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "meshes/robots/fr3v2/visual/link1.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "meshes/robots/fr3v2/visual/link2.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "meshes/robots/fr3v2/visual/link3.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "meshes/robots/fr3v2/visual/link4.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "meshes/robots/fr3v2/visual/link5.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "meshes/robots/fr3v2/visual/link6.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "meshes/robots/fr3v2/visual/link7.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "meshes/robot_ee/franka_hand_white/visual/hand.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "meshes/robot_ee/franka_hand_white/visual/finger.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "meshes/robot_ee/franka_hand_white/visual/finger.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      }
    ],
    "nonphysical_normalizations": [],
    "xacro_arguments": {
      "robot_types": "['fr3v2','fr3v2']",
      "no_prefix": "false",
      "hand": "true",
      "ee_id": "franka_hand",
      "special_connection": "",
      "xyz_ee": "0 0 0",
      "rpy_ee": "0 0 -0.7853981633974483",
      "tcp_xyz": "",
      "tcp_rpy": "0 0 0",
      "safety_distance": "0.03",
      "with_sc": "false",
      "include_self_collision_geometry": "true",
      "description_pkg": "franka_description",
      "arm_prefixes": "['left','right']",
      "xyz": "0 0 0",
      "rpy": "0 0 0",
      "base_mount": "base"
    },
    "source_dependencies": [
      "accessories/fr3_duo_mount_v0_3/fr3_duo_mount.xacro",
      "accessories/fr3_duo_mount_v0_3/inertials.yaml",
      "accessories/fr3_duo_mount_v0_3/kinematics.yaml",
      "accessories/franka_head_v0_2/franka_head.xacro",
      "accessories/franka_head_v0_2/inertials.yaml",
      "accessories/franka_head_v0_2/kinematics.yaml",
      "end_effectors/common/franka_hand.xacro",
      "end_effectors/common/utils.xacro",
      "end_effectors/franka_hand/inertials.yaml",
      "robots/common/franka_arm.xacro",
      "robots/common/franka_robot.xacro",
      "robots/common/utils.xacro",
      "robots/fr3_duo/fr3_duo.urdf.xacro",
      "robots/fr3_duo/fr3_duo.xacro",
      "robots/fr3v2/accelerometers.yaml",
      "robots/fr3v2/dynamics.yaml",
      "robots/fr3v2/inertials.yaml",
      "robots/fr3v2/joint_limits.yaml",
      "robots/fr3v2/kinematics.yaml",
      "meshes/accessories/fr3_duo_mount_v0_3/visual/fr3_duo_mount.dae",
      "meshes/accessories/fr3_duo_mount_v0_3/visual/fr3_duo_cover.dae",
      "meshes/accessories/fr3_duo_mount_v0_3/collision/fr3_duo_mount.stl",
      "meshes/accessories/fr3_duo_mount_v0_3/collision/fr3_duo_cover.stl",
      "meshes/accessories/franka_head_v0_2/visual/franka_head.dae",
      "meshes/accessories/franka_head_v0_2/collision/franka_head.stl",
      "meshes/robots/fr3v2/visual/link0.dae",
      "meshes/robots/fr3v2/collision/link0.stl",
      "meshes/robots/fr3v2/visual/link1.dae",
      "meshes/robots/fr3v2/collision/link1.stl",
      "meshes/robots/fr3v2/visual/link2.dae",
      "meshes/robots/fr3v2/collision/link2.stl",
      "meshes/robots/fr3v2/visual/link3.dae",
      "meshes/robots/fr3v2/collision/link3.stl",
      "meshes/robots/fr3v2/visual/link4.dae",
      "meshes/robots/fr3v2/collision/link4.stl",
      "meshes/robots/fr3v2/visual/link5.dae",
      "meshes/robots/fr3v2/collision/link5.stl",
      "meshes/robots/fr3v2/visual/link6.dae",
      "meshes/robots/fr3v2/collision/link6.stl",
      "meshes/robots/fr3v2/visual/link7.dae",
      "meshes/robots/fr3v2/collision/link7.stl",
      "meshes/robot_ee/franka_hand_white/visual/hand.dae",
      "meshes/robot_ee/franka_hand_white/collision/hand.stl",
      "meshes/robot_ee/franka_hand_white/visual/finger.dae",
      "meshes/robot_ee/franka_hand_white/visual/finger.dae",
      "meshes/robots/fr3v2/visual/link0.dae",
      "meshes/robots/fr3v2/collision/link0.stl",
      "meshes/robots/fr3v2/visual/link1.dae",
      "meshes/robots/fr3v2/collision/link1.stl",
      "meshes/robots/fr3v2/visual/link2.dae",
      "meshes/robots/fr3v2/collision/link2.stl",
      "meshes/robots/fr3v2/visual/link3.dae",
      "meshes/robots/fr3v2/collision/link3.stl",
      "meshes/robots/fr3v2/visual/link4.dae",
      "meshes/robots/fr3v2/collision/link4.stl",
      "meshes/robots/fr3v2/visual/link5.dae",
      "meshes/robots/fr3v2/collision/link5.stl",
      "meshes/robots/fr3v2/visual/link6.dae",
      "meshes/robots/fr3v2/collision/link6.stl",
      "meshes/robots/fr3v2/visual/link7.dae",
      "meshes/robots/fr3v2/collision/link7.stl",
      "meshes/robot_ee/franka_hand_white/visual/hand.dae",
      "meshes/robot_ee/franka_hand_white/collision/hand.stl",
      "meshes/robot_ee/franka_hand_white/visual/finger.dae",
      "meshes/robot_ee/franka_hand_white/visual/finger.dae"
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
  "historical_snapshots_reused": 54,
  "primary_physics_unchanged": true,
  "source_matching": "original raw-value provenance criteria retained; kinematic guard applies to reported CoM"
}
```
