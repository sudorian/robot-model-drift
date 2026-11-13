# trs_so_arm100

Status: **complete**. Provenance: **pinned**, confidence **high**.

Source selected using the ordered amended provenance rules.

M: `https://github.com/google-deepmind/mujoco_menagerie`, `trs_so_arm100/so_arm100.xml`, commit `370c43965323c0944b433b202aac5058b5f907a9`.
H: `https://github.com/TheRobotStudio/SO-ARM100`, `Simulation/SO100/so100.urdf`, commit `a758567c3978dfeefe282ede0500085a48fe8f78`.
S: `4e9c5588d8a8415b6a6c2142a0ce8c32207cf3e9` (2024-10-28T09:41:11+01:00). Menagerie release/change: 2025-06-09T19:00:21-07:00.

Limit semantics: MJCF effort values are supported actuator torque/force envelopes. URDF effort and velocity values are manufacturer declarations retained from XML; MuJoCo does not enforce those tags. Such declaration comparisons are explicitly distinct from compiled inertial/range quantities.


## Source evidence

```json
[
  {
    "url": "https://github.com/TheRobotStudio/SO-ARM100/blob/4e9c5588d8a8415b6a6c2142a0ce8c32207cf3e9/URDF/SO_5DOF_ARM100_8j_URDF.SLDASM/urdf/SO_5DOF_ARM100_8j_URDF.SLDASM.urdf",
    "document": "trs_so_arm100/README.md",
    "commit": "370c43965323c0944b433b202aac5058b5f907a9",
    "current": true
  },
  {
    "url": "https://github.com/TheRobotStudio/SO-ARM100/tree/main",
    "document": "trs_so_arm100/README.md",
    "commit": "370c43965323c0944b433b202aac5058b5f907a9",
    "current": true
  }
]
```


## README derivation evidence

Documentation labels are conservative: an automated documented label requires an explicit affected entity and quantity. Broader conversion notes are retained here for review.

> 7. Added approximate joint limits.

## Kinematics consistency

A proper Kabsch rigid transform aligns all matched zero-pose body origins. The maximum per-origin residual and signed hinge/slide axis angles determine whether CoM can be compared; RMS is also recorded. Fewer than three non-collinear origins give insufficient kinematic coverage. CoM records that fail either required M/H or M/S check are excluded from counts and largest discrepancies. Masses, principal moments and raw joint ranges remain unchanged; a flagged range still requires convention review.

| Pair | Status | Origins / rank | RMS / maximum mm | Disagreeing / checked axes |
|---|---|---:|---:|---:|
| M/H | kinematic convention differs | 7 / 3 | 102.758033 / 144.551971 | 2 / 6 |
| M/S | kinematic convention differs | 7 / 3 | 72.3833215 / 117.67773 | 6 / 6 |

Exact fitted transforms, per-origin residuals, thresholds and axis vectors:

```json
{
  "M/H": {
    "status": "kinematic convention differs",
    "matched_body_origins": 7,
    "position_threshold_m": 0.005,
    "axis_threshold_rad": 0.005,
    "residual_definition": "maximum Euclidean residual over matched body origins; Kabsch minimizes RMS, which is also recorded",
    "coordinate_frames": "each snapshot registered to its matched report anchor",
    "anchor_m": "Base",
    "anchor_other": "base",
    "rotation_other_to_m": [
      [
        0.9999999999997178,
        4.0045135099774355e-07,
        6.359276739843944e-07
      ],
      [
        -3.5719555641459836e-08,
        0.870572223822533,
        -0.49204065188629237
      ],
      [
        -7.506593130668376e-07,
        0.492040651886131,
        0.8705722238223015
      ]
    ],
    "translation_other_to_m": [
      -3.4979242993544874e-08,
      -0.09305799907142534,
      0.02462255620401626
    ],
    "rms_residual_m": 0.10275803295226063,
    "max_residual_m": 0.14455197092272762,
    "fit_rank": 3,
    "axis_checks": [
      {
        "joint_m": "Rotation",
        "joint_other": "shoulder_pan",
        "axis_m": [
          0.0,
          -4.242642374308048e-06,
          0.9999999999910001
        ],
        "axis_other_aligned": [
          6.359302075452309e-07,
          -0.49203514394454206,
          0.8705753368451633
        ],
        "angle_rad": 0.5144216701086731,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "Pitch",
        "joint_other": "shoulder_lift",
        "axis_m": [
          1.0,
          0.0,
          0.0
        ],
        "axis_other_aligned": [
          0.9999999999997178,
          -3.5719555641459836e-08,
          -7.506593130668376e-07
        ],
        "angle_rad": 7.515086765628898e-07,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "Elbow",
        "joint_other": "elbow_flex",
        "axis_m": [
          1.0,
          0.0,
          0.0
        ],
        "axis_other_aligned": [
          0.9999999999997178,
          -3.5719555641459836e-08,
          -7.506593130668376e-07
        ],
        "angle_rad": 7.515086765628898e-07,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "Wrist_Pitch",
        "joint_other": "wrist_flex",
        "axis_m": [
          1.0,
          0.0,
          0.0
        ],
        "axis_other_aligned": [
          0.9999999999997178,
          -3.5719555641459836e-08,
          -7.506593130668376e-07
        ],
        "angle_rad": 7.515086765628898e-07,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "Wrist_Roll",
        "joint_other": "wrist_roll",
        "axis_m": [
          3.677781903179613e-22,
          0.9999999999441436,
          1.0569437270557011e-05
        ],
        "axis_other_aligned": [
          5.903365599430179e-07,
          0.6554543671578654,
          0.7552347797693997
        ],
        "angle_rad": 0.8560016701082024,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "Jaw",
        "joint_other": "gripper",
        "axis_m": [
          -0.9999999999530006,
          -7.346353128060081e-06,
          -6.3269265135890135e-06
        ],
        "axis_other_aligned": [
          -0.9999999998284168,
          1.4370366206305326e-05,
          -1.1690116722076745e-05
        ],
        "angle_rad": 2.236916869032922e-05,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      }
    ],
    "axis_disagreements": [
      {
        "joint_m": "Rotation",
        "joint_other": "shoulder_pan",
        "axis_m": [
          0.0,
          -4.242642374308048e-06,
          0.9999999999910001
        ],
        "axis_other_aligned": [
          6.359302075452309e-07,
          -0.49203514394454206,
          0.8705753368451633
        ],
        "angle_rad": 0.5144216701086731,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "Wrist_Roll",
        "joint_other": "wrist_roll",
        "axis_m": [
          3.677781903179613e-22,
          0.9999999999441436,
          1.0569437270557011e-05
        ],
        "axis_other_aligned": [
          5.903365599430179e-07,
          0.6554543671578654,
          0.7552347797693997
        ],
        "angle_rad": 0.8560016701082024,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      }
    ],
    "com_eligible": false,
    "covariance_singular_values": [
      0.08097823991156458,
      0.004577155793452258,
      7.566928951600672e-15
    ],
    "origin_residuals_m": {
      "Base": 0.0962603836746902,
      "Rotation_Pitch": 0.09532685372345409,
      "Upper_Arm": 0.14455197092272762,
      "Lower_Arm": 0.09190893534174863,
      "Wrist_Pitch_Roll": 0.07760373239002326,
      "Fixed_Jaw": 0.09884508514957877,
      "Moving_Jaw": 0.10210782543529734
    },
    "reason": "Origin residual exceeds threshold and/or matched signed joint axes disagree"
  },
  "M/S": {
    "status": "kinematic convention differs",
    "matched_body_origins": 7,
    "position_threshold_m": 0.005,
    "axis_threshold_rad": 0.005,
    "residual_definition": "maximum Euclidean residual over matched body origins; Kabsch minimizes RMS, which is also recorded",
    "coordinate_frames": "each snapshot registered to its matched report anchor",
    "anchor_m": "Base",
    "anchor_other": "Base",
    "rotation_other_to_m": [
      [
        0.9989949322930093,
        -0.04444310610617281,
        -0.005825424664393431
      ],
      [
        0.03917270503527555,
        0.9288215799687548,
        -0.3684507725118312
      ],
      [
        0.02178587691841549,
        0.3678522568966805,
        0.9296290080795211
      ]
    ],
    "translation_other_to_m": [
      -0.002314751361328093,
      -0.029339674908504337,
      0.0021019106423395967
    ],
    "rms_residual_m": 0.07238332154448461,
    "max_residual_m": 0.11767772964865476,
    "fit_rank": 3,
    "axis_checks": [
      {
        "joint_m": "Rotation",
        "joint_other": "Rotation",
        "axis_m": [
          0.0,
          -4.242642374308048e-06,
          0.9999999999910001
        ],
        "axis_other_aligned": [
          -0.00582526141570998,
          -0.3684541842615131,
          0.9296276568764624
        ],
        "angle_rad": 0.37739095995310534,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "Pitch",
        "joint_other": "Pitch",
        "axis_m": [
          1.0,
          0.0,
          0.0
        ],
        "axis_other_aligned": [
          0.9989949322930097,
          0.03917270503527557,
          0.0217858769184155
        ],
        "angle_rad": 0.04483828971562366,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "Elbow",
        "joint_other": "Elbow",
        "axis_m": [
          1.0,
          0.0,
          0.0
        ],
        "axis_other_aligned": [
          0.9989949322930097,
          0.03917270503527557,
          0.0217858769184155
        ],
        "angle_rad": 0.04483828971562366,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "Wrist_Pitch",
        "joint_other": "Wrist_Pitch",
        "axis_m": [
          1.0,
          0.0,
          0.0
        ],
        "axis_other_aligned": [
          0.9989949322930097,
          0.03917270503527557,
          0.0217858769184155
        ],
        "angle_rad": 0.04483828971562366,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "Wrist_Roll",
        "joint_other": "Wrist_Roll",
        "axis_m": [
          3.677781903179613e-22,
          0.9999999999441436,
          1.0569437270557011e-05
        ],
        "axis_other_aligned": [
          -0.00582526141570998,
          -0.3684541842615131,
          0.9296276568764624
        ],
        "angle_rad": 1.94813142865105,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "Jaw",
        "joint_other": "Jaw",
        "axis_m": [
          -0.9999999999530006,
          -7.346353128060081e-06,
          -6.3269265135890135e-06
        ],
        "axis_other_aligned": [
          -0.04444308465397789,
          0.9288229333598607,
          0.3678488421773586
        ],
        "angle_rad": 1.5263477584133234,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      }
    ],
    "axis_disagreements": [
      {
        "joint_m": "Rotation",
        "joint_other": "Rotation",
        "axis_m": [
          0.0,
          -4.242642374308048e-06,
          0.9999999999910001
        ],
        "axis_other_aligned": [
          -0.00582526141570998,
          -0.3684541842615131,
          0.9296276568764624
        ],
        "angle_rad": 0.37739095995310534,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "Pitch",
        "joint_other": "Pitch",
        "axis_m": [
          1.0,
          0.0,
          0.0
        ],
        "axis_other_aligned": [
          0.9989949322930097,
          0.03917270503527557,
          0.0217858769184155
        ],
        "angle_rad": 0.04483828971562366,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "Elbow",
        "joint_other": "Elbow",
        "axis_m": [
          1.0,
          0.0,
          0.0
        ],
        "axis_other_aligned": [
          0.9989949322930097,
          0.03917270503527557,
          0.0217858769184155
        ],
        "angle_rad": 0.04483828971562366,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "Wrist_Pitch",
        "joint_other": "Wrist_Pitch",
        "axis_m": [
          1.0,
          0.0,
          0.0
        ],
        "axis_other_aligned": [
          0.9989949322930097,
          0.03917270503527557,
          0.0217858769184155
        ],
        "angle_rad": 0.04483828971562366,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "Wrist_Roll",
        "joint_other": "Wrist_Roll",
        "axis_m": [
          3.677781903179613e-22,
          0.9999999999441436,
          1.0569437270557011e-05
        ],
        "axis_other_aligned": [
          -0.00582526141570998,
          -0.3684541842615131,
          0.9296276568764624
        ],
        "angle_rad": 1.94813142865105,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "Jaw",
        "joint_other": "Jaw",
        "axis_m": [
          -0.9999999999530006,
          -7.346353128060081e-06,
          -6.3269265135890135e-06
        ],
        "axis_other_aligned": [
          -0.04444308465397789,
          0.9288229333598607,
          0.3678488421773586
        ],
        "angle_rad": 1.5263477584133234,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      }
    ],
    "com_eligible": false,
    "covariance_singular_values": [
      0.12726088383518708,
      0.005833323391806642,
      1.632382321742157e-09
    ],
    "origin_residuals_m": {
      "Base": 0.029505806648012008,
      "Rotation_Pitch": 0.03582143795909027,
      "Upper_Arm": 0.07590914199823334,
      "Lower_Arm": 0.09107285157222063,
      "Wrist_Pitch_Roll": 0.04162728408415516,
      "Fixed_Jaw": 0.06988782192478464,
      "Moving_Jaw": 0.11767772964865476
    },
    "reason": "Origin residual exceeds threshold and/or matched signed joint axes disagree"
  }
}
```


## Every reported quantity difference

Counts are quantity records, including correlated total/subtree/body mass records; they are not independent robot defects.

| Entity / quantity | M | S | H | H − M | Class | M source | S source | H source |
|---|---|---|---|---|---|---|---|---|
| robot / total_mass | 1.17143099 | 0.802149861 | 1.6089654 | 0.437534409 | needs a human look | [aggregate inputs](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/trs_so_arm100/so_arm100.xml#L1) | [aggregate inputs](https://github.com/TheRobotStudio/SO-ARM100/blob/4e9c5588d8a8415b6a6c2142a0ce8c32207cf3e9/URDF/SO_5DOF_ARM100_8j_URDF.SLDASM/urdf/SO_5DOF_ARM100_8j_URDF.SLDASM.urdf#L1) | [aggregate inputs](https://github.com/TheRobotStudio/SO-ARM100/blob/a758567c3978dfeefe282ede0500085a48fe8f78/Simulation/SO100/so100.urdf#L1) |
| Base / mass | 0.562465591 | 0.193184128 | 1 | 0.437534409 | needs a human look | [geometry/inference input L68](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/trs_so_arm100/so_arm100.xml#L68) | [input L14](https://github.com/TheRobotStudio/SO-ARM100/blob/4e9c5588d8a8415b6a6c2142a0ce8c32207cf3e9/URDF/SO_5DOF_ARM100_8j_URDF.SLDASM/urdf/SO_5DOF_ARM100_8j_URDF.SLDASM.urdf#L14) | [input L16](https://github.com/TheRobotStudio/SO-ARM100/blob/a758567c3978dfeefe282ede0500085a48fe8f78/Simulation/SO100/so100.urdf#L16) |
| Base / subtree_mass | 1.17143099 | 0.802149861 | 1.6089654 | 0.437534409 | needs a human look | [subtree root L68](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/trs_so_arm100/so_arm100.xml#L68) | [subtree root L8](https://github.com/TheRobotStudio/SO-ARM100/blob/4e9c5588d8a8415b6a6c2142a0ce8c32207cf3e9/URDF/SO_5DOF_ARM100_8j_URDF.SLDASM/urdf/SO_5DOF_ARM100_8j_URDF.SLDASM.urdf#L8) | [subtree root L13](https://github.com/TheRobotStudio/SO-ARM100/blob/a758567c3978dfeefe282ede0500085a48fe8f78/Simulation/SO100/so100.urdf#L13) |
| Base / principal_moments | [0.000365031476, 0.000481383489, 0.000614986306] | [0.000131461789, 0.00013703071, 0.000182725483] | [0.01, 0.01, 0.01] | [0.00963496852, 0.00951861651, 0.00938501369] | needs a human look | [geometry/inference input L68](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/trs_so_arm100/so_arm100.xml#L68) | [inertia input L21](https://github.com/TheRobotStudio/SO-ARM100/blob/4e9c5588d8a8415b6a6c2142a0ce8c32207cf3e9/URDF/SO_5DOF_ARM100_8j_URDF.SLDASM/urdf/SO_5DOF_ARM100_8j_URDF.SLDASM.urdf#L21) | [inertia input L18](https://github.com/TheRobotStudio/SO-ARM100/blob/a758567c3978dfeefe282ede0500085a48fe8f78/Simulation/SO100/so100.urdf#L18) |
| Rotation / range | [-1.92, 1.92] | unavailable | [-2, 2] | [-0.08, 0.08] | unknown | [inherited default L35](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/trs_so_arm100/so_arm100.xml#L35) | [geometry/inference input L89](https://github.com/TheRobotStudio/SO-ARM100/blob/4e9c5588d8a8415b6a6c2142a0ce8c32207cf3e9/URDF/SO_5DOF_ARM100_8j_URDF.SLDASM/urdf/SO_5DOF_ARM100_8j_URDF.SLDASM.urdf#L89) | [input L186](https://github.com/TheRobotStudio/SO-ARM100/blob/a758567c3978dfeefe282ede0500085a48fe8f78/Simulation/SO100/so100.urdf#L186) |
| Rotation / effort | 3.5 | unavailable | 35 | 31.5 | unknown | [inherited actuator input L33](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/trs_so_arm100/so_arm100.xml#L33) | [geometry/inference input L89](https://github.com/TheRobotStudio/SO-ARM100/blob/4e9c5588d8a8415b6a6c2142a0ce8c32207cf3e9/URDF/SO_5DOF_ARM100_8j_URDF.SLDASM/urdf/SO_5DOF_ARM100_8j_URDF.SLDASM.urdf#L89) | [input L186](https://github.com/TheRobotStudio/SO-ARM100/blob/a758567c3978dfeefe282ede0500085a48fe8f78/Simulation/SO100/so100.urdf#L186) |
| Pitch / range | [-3.32, 0.174] | unavailable | [0, 3.5] | [3.32, 3.326] | unknown | [inherited default L38](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/trs_so_arm100/so_arm100.xml#L38) | [geometry/inference input L142](https://github.com/TheRobotStudio/SO-ARM100/blob/4e9c5588d8a8415b6a6c2142a0ce8c32207cf3e9/URDF/SO_5DOF_ARM100_8j_URDF.SLDASM/urdf/SO_5DOF_ARM100_8j_URDF.SLDASM.urdf#L142) | [input L206](https://github.com/TheRobotStudio/SO-ARM100/blob/a758567c3978dfeefe282ede0500085a48fe8f78/Simulation/SO100/so100.urdf#L206) |
| Pitch / effort | 3.5 | unavailable | 35 | 31.5 | unknown | [inherited actuator input L33](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/trs_so_arm100/so_arm100.xml#L33) | [geometry/inference input L142](https://github.com/TheRobotStudio/SO-ARM100/blob/4e9c5588d8a8415b6a6c2142a0ce8c32207cf3e9/URDF/SO_5DOF_ARM100_8j_URDF.SLDASM/urdf/SO_5DOF_ARM100_8j_URDF.SLDASM.urdf#L142) | [input L206](https://github.com/TheRobotStudio/SO-ARM100/blob/a758567c3978dfeefe282ede0500085a48fe8f78/Simulation/SO100/so100.urdf#L206) |
| Elbow / range | [-0.174, 3.14] | unavailable | [-3.14158, 0] | [-2.96758, -3.14] | unknown | [inherited default L41](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/trs_so_arm100/so_arm100.xml#L41) | [geometry/inference input L195](https://github.com/TheRobotStudio/SO-ARM100/blob/4e9c5588d8a8415b6a6c2142a0ce8c32207cf3e9/URDF/SO_5DOF_ARM100_8j_URDF.SLDASM/urdf/SO_5DOF_ARM100_8j_URDF.SLDASM.urdf#L195) | [input L226](https://github.com/TheRobotStudio/SO-ARM100/blob/a758567c3978dfeefe282ede0500085a48fe8f78/Simulation/SO100/so100.urdf#L226) |
| Elbow / effort | 3.5 | unavailable | 35 | 31.5 | unknown | [inherited actuator input L33](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/trs_so_arm100/so_arm100.xml#L33) | [geometry/inference input L195](https://github.com/TheRobotStudio/SO-ARM100/blob/4e9c5588d8a8415b6a6c2142a0ce8c32207cf3e9/URDF/SO_5DOF_ARM100_8j_URDF.SLDASM/urdf/SO_5DOF_ARM100_8j_URDF.SLDASM.urdf#L195) | [input L226](https://github.com/TheRobotStudio/SO-ARM100/blob/a758567c3978dfeefe282ede0500085a48fe8f78/Simulation/SO100/so100.urdf#L226) |
| Wrist_Pitch / range | [-1.66, 1.66] | unavailable | [-2.5, 1.2] | [-0.84, -0.46] | unknown | [inherited default L44](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/trs_so_arm100/so_arm100.xml#L44) | [geometry/inference input L248](https://github.com/TheRobotStudio/SO-ARM100/blob/4e9c5588d8a8415b6a6c2142a0ce8c32207cf3e9/URDF/SO_5DOF_ARM100_8j_URDF.SLDASM/urdf/SO_5DOF_ARM100_8j_URDF.SLDASM.urdf#L248) | [input L246](https://github.com/TheRobotStudio/SO-ARM100/blob/a758567c3978dfeefe282ede0500085a48fe8f78/Simulation/SO100/so100.urdf#L246) |
| Wrist_Pitch / effort | 3.5 | unavailable | 35 | 31.5 | unknown | [inherited actuator input L33](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/trs_so_arm100/so_arm100.xml#L33) | [geometry/inference input L248](https://github.com/TheRobotStudio/SO-ARM100/blob/4e9c5588d8a8415b6a6c2142a0ce8c32207cf3e9/URDF/SO_5DOF_ARM100_8j_URDF.SLDASM/urdf/SO_5DOF_ARM100_8j_URDF.SLDASM.urdf#L248) | [input L246](https://github.com/TheRobotStudio/SO-ARM100/blob/a758567c3978dfeefe282ede0500085a48fe8f78/Simulation/SO100/so100.urdf#L246) |
| Wrist_Roll / range | [-2.79, 2.79] | unavailable | [-3.14158, 3.14158] | [-0.35158, 0.35158] | unknown | [inherited default L47](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/trs_so_arm100/so_arm100.xml#L47) | [geometry/inference input L301](https://github.com/TheRobotStudio/SO-ARM100/blob/4e9c5588d8a8415b6a6c2142a0ce8c32207cf3e9/URDF/SO_5DOF_ARM100_8j_URDF.SLDASM/urdf/SO_5DOF_ARM100_8j_URDF.SLDASM.urdf#L301) | [input L266](https://github.com/TheRobotStudio/SO-ARM100/blob/a758567c3978dfeefe282ede0500085a48fe8f78/Simulation/SO100/so100.urdf#L266) |
| Wrist_Roll / effort | 3.5 | unavailable | 35 | 31.5 | unknown | [inherited actuator input L33](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/trs_so_arm100/so_arm100.xml#L33) | [geometry/inference input L301](https://github.com/TheRobotStudio/SO-ARM100/blob/4e9c5588d8a8415b6a6c2142a0ce8c32207cf3e9/URDF/SO_5DOF_ARM100_8j_URDF.SLDASM/urdf/SO_5DOF_ARM100_8j_URDF.SLDASM.urdf#L301) | [input L266](https://github.com/TheRobotStudio/SO-ARM100/blob/a758567c3978dfeefe282ede0500085a48fe8f78/Simulation/SO100/so100.urdf#L266) |
| Jaw / range | [-0.174, 1.75] | unavailable | [-0.2, 2] | [-0.026, 0.25] | unknown | [inherited default L50](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/trs_so_arm100/so_arm100.xml#L50) | [geometry/inference input L354](https://github.com/TheRobotStudio/SO-ARM100/blob/4e9c5588d8a8415b6a6c2142a0ce8c32207cf3e9/URDF/SO_5DOF_ARM100_8j_URDF.SLDASM/urdf/SO_5DOF_ARM100_8j_URDF.SLDASM.urdf#L354) | [input L286](https://github.com/TheRobotStudio/SO-ARM100/blob/a758567c3978dfeefe282ede0500085a48fe8f78/Simulation/SO100/so100.urdf#L286) |
| Jaw / effort | 3.5 | unavailable | 35 | 31.5 | unknown | [inherited actuator input L33](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/trs_so_arm100/so_arm100.xml#L33) | [geometry/inference input L354](https://github.com/TheRobotStudio/SO-ARM100/blob/4e9c5588d8a8415b6a6c2142a0ce8c32207cf3e9/URDF/SO_5DOF_ARM100_8j_URDF.SLDASM/urdf/SO_5DOF_ARM100_8j_URDF.SLDASM.urdf#L354) | [input L286](https://github.com/TheRobotStudio/SO-ARM100/blob/a758567c3978dfeefe282ede0500085a48fe8f78/Simulation/SO100/so100.urdf#L286) |

## Raw CoM records and reporting decisions

Raw values retain the previous root-anchor registration before Kabsch; original world coordinates also remain in the snapshots. Eligible findings above use the fitted transform into M. Excluded raw records below are diagnostic numbers, not findings. No CoM suppression applies to mass or principal inertia moments.

| Entity / quantity | Raw M | Raw S | Raw H | Raw H − M | Decision | M source | S source | H source |
|---|---|---|---|---|---|---|---|---|
| robot / total_com_registered | [-0.000889152645, -0.129363, 0.0636979999] | [-0.00117509517, -0.10654626, 0.133666803] | [-0.000648948915, -0.0270161197, 0.0438163273] | [0.000240203729, 0.102346881, -0.0198816727] | M/H: kinematic convention differs; M/S: kinematic convention differs | [aggregate inputs](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/trs_so_arm100/so_arm100.xml#L1) | [aggregate inputs](https://github.com/TheRobotStudio/SO-ARM100/blob/4e9c5588d8a8415b6a6c2142a0ce8c32207cf3e9/URDF/SO_5DOF_ARM100_8j_URDF.SLDASM/urdf/SO_5DOF_ARM100_8j_URDF.SLDASM.urdf#L1) | [aggregate inputs](https://github.com/TheRobotStudio/SO-ARM100/blob/a758567c3978dfeefe282ede0500085a48fe8f78/Simulation/SO100/so100.urdf#L1) |
| Base / com_registered | [4.53590122e-06, -0.0154104524, 0.0284425542] | [-2.45960667e-07, 0.031141817, 0.0175746661] | [0, 0, 0] | [-4.53590122e-06, 0.0154104524, -0.0284425542] | M/H: kinematic convention differs; M/S: kinematic convention differs | [geometry/inference input L68](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/trs_so_arm100/so_arm100.xml#L68) | [CoM/kinematic input L12](https://github.com/TheRobotStudio/SO-ARM100/blob/4e9c5588d8a8415b6a6c2142a0ce8c32207cf3e9/URDF/SO_5DOF_ARM100_8j_URDF.SLDASM/urdf/SO_5DOF_ARM100_8j_URDF.SLDASM.urdf#L12) | [CoM/kinematic input L17](https://github.com/TheRobotStudio/SO-ARM100/blob/a758567c3978dfeefe282ede0500085a48fe8f78/Simulation/SO100/so100.urdf#L17) |
| Rotation_Pitch / com_registered | [-9.07886e-05, -0.0762892507, 0.0755970681] | [-9.07886225e-05, -0.076289234, 0.0755970679] | [-9.07886e-05, -0.0762886261, 0.0755973967] | [0, 6.24624491e-07, 3.28592584e-07] | M/H: kinematic convention differs; M/S: kinematic convention differs | [CoM/kinematic input L74](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/trs_so_arm100/so_arm100.xml#L74) | [CoM/kinematic input L52](https://github.com/TheRobotStudio/SO-ARM100/blob/4e9c5588d8a8415b6a6c2142a0ce8c32207cf3e9/URDF/SO_5DOF_ARM100_8j_URDF.SLDASM/urdf/SO_5DOF_ARM100_8j_URDF.SLDASM.urdf#L52) | [CoM/kinematic input L43](https://github.com/TheRobotStudio/SO-ARM100/blob/a758567c3978dfeefe282ede0500085a48fe8f78/Simulation/SO100/so100.urdf#L43) |
| Upper_Arm / com_registered | [-1.72052e-05, -0.145980641, 0.115894566] | [-1.72051702e-05, -0.0789060855, 0.189180092] | [-1.72052e-05, -0.006749047, 0.106078903] | [3.38813179e-21, 0.139231594, -0.00981566303] | M/H: kinematic convention differs; M/S: kinematic convention differs | [CoM/kinematic input L81](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/trs_so_arm100/so_arm100.xml#L81) | [CoM/kinematic input L105](https://github.com/TheRobotStudio/SO-ARM100/blob/4e9c5588d8a8415b6a6c2142a0ce8c32207cf3e9/URDF/SO_5DOF_ARM100_8j_URDF.SLDASM/urdf/SO_5DOF_ARM100_8j_URDF.SLDASM.urdf#L105) | [CoM/kinematic input L69](https://github.com/TheRobotStudio/SO-ARM100/blob/a758567c3978dfeefe282ede0500085a48fe8f78/Simulation/SO100/so100.urdf#L69) |
| Lower_Arm / com_registered | [-0.00339604, -0.265171199, 0.0923777389] | [-0.0033960371, -0.18060147, 0.232947466] | [-0.00339604, -0.0342905209, 0.139483199] | [0, 0.230880678, 0.0471054601] | M/H: kinematic convention differs; M/S: kinematic convention differs | [CoM/kinematic input L88](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/trs_so_arm100/so_arm100.xml#L88) | [CoM/kinematic input L158](https://github.com/TheRobotStudio/SO-ARM100/blob/4e9c5588d8a8415b6a6c2142a0ce8c32207cf3e9/URDF/SO_5DOF_ARM100_8j_URDF.SLDASM/urdf/SO_5DOF_ARM100_8j_URDF.SLDASM.urdf#L158) | [CoM/kinematic input L95](https://github.com/TheRobotStudio/SO-ARM100/blob/a758567c3978dfeefe282ede0500085a48fe8f78/Simulation/SO100/so100.urdf#L95) |
| Wrist_Pitch_Roll / com_registered | [-0.00852653, -0.358498415, 0.0961756979] | [-0.00852653127, -0.238677217, 0.20154139] | [-0.00852653, -0.123186601, 0.144583656] | [0, 0.235311814, 0.0484079576] | M/H: kinematic convention differs; M/S: kinematic convention differs | [CoM/kinematic input L95](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/trs_so_arm100/so_arm100.xml#L95) | [CoM/kinematic input L211](https://github.com/TheRobotStudio/SO-ARM100/blob/4e9c5588d8a8415b6a6c2142a0ce8c32207cf3e9/URDF/SO_5DOF_ARM100_8j_URDF.SLDASM/urdf/SO_5DOF_ARM100_8j_URDF.SLDASM.urdf#L211) | [CoM/kinematic input L121](https://github.com/TheRobotStudio/SO-ARM100/blob/a758567c3978dfeefe282ede0500085a48fe8f78/Simulation/SO100/so100.urdf#L121) |
| Fixed_Jaw / com_registered | [0.000483617948, -0.411387157, 0.0906748342] | [0.00552376906, -0.239184068, 0.148652572] | [0.000483617948, -0.171177363, 0.121684631] | [8.67361738e-19, 0.240209794, 0.0310097973] | M/H: kinematic convention differs; M/S: kinematic convention differs | [CoM/kinematic input L102](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/trs_so_arm100/so_arm100.xml#L102) | [CoM/kinematic input L264](https://github.com/TheRobotStudio/SO-ARM100/blob/4e9c5588d8a8415b6a6c2142a0ce8c32207cf3e9/URDF/SO_5DOF_ARM100_8j_URDF.SLDASM/urdf/SO_5DOF_ARM100_8j_URDF.SLDASM.urdf#L264) | [CoM/kinematic input L147](https://github.com/TheRobotStudio/SO-ARM100/blob/a758567c3978dfeefe282ede0500085a48fe8f78/Simulation/SO100/so100.urdf#L147) |
| Moving_Jaw / com_registered | [-0.000449540623, -0.438118003, 0.114780643] | [-0.018582331, -0.238250964, 0.121922041] | [-0.000449743101, -0.204438685, 0.13544412] | [-2.02478814e-07, 0.233679318, 0.0206634776] | M/H: kinematic convention differs; M/S: kinematic convention differs | [CoM/kinematic input L114](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/trs_so_arm100/so_arm100.xml#L114) | [CoM/kinematic input L317](https://github.com/TheRobotStudio/SO-ARM100/blob/4e9c5588d8a8415b6a6c2142a0ce8c32207cf3e9/URDF/SO_5DOF_ARM100_8j_URDF.SLDASM/urdf/SO_5DOF_ARM100_8j_URDF.SLDASM.urdf#L317) | [CoM/kinematic input L168](https://github.com/TheRobotStudio/SO-ARM100/blob/a758567c3978dfeefe282ede0500085a48fe8f78/Simulation/SO100/so100.urdf#L168) |

## Mass accounting

Every contributing compiled body mass is listed here so total/subtree sums can be checked. Links point to explicit inertials or to geometry inputs when the compiler inferred a mass. CoM links identify inertial inputs; world coordinates additionally use the ancestor transforms and the registration recorded below.

| M body | M kg / source | S kg / source | H kg / source |
|---|---|---|---|
| Base | 0.562465591 / [geometry/inference input L68](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/trs_so_arm100/so_arm100.xml#L68) | 0.193184128 / [input L14](https://github.com/TheRobotStudio/SO-ARM100/blob/4e9c5588d8a8415b6a6c2142a0ce8c32207cf3e9/URDF/SO_5DOF_ARM100_8j_URDF.SLDASM/urdf/SO_5DOF_ARM100_8j_URDF.SLDASM.urdf#L14) | 1 / [input L16](https://github.com/TheRobotStudio/SO-ARM100/blob/a758567c3978dfeefe282ede0500085a48fe8f78/Simulation/SO100/so100.urdf#L16) |
| Rotation_Pitch | 0.119226 / [input L74](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/trs_so_arm100/so_arm100.xml#L74) | 0.119226314 / [input L54](https://github.com/TheRobotStudio/SO-ARM100/blob/4e9c5588d8a8415b6a6c2142a0ce8c32207cf3e9/URDF/SO_5DOF_ARM100_8j_URDF.SLDASM/urdf/SO_5DOF_ARM100_8j_URDF.SLDASM.urdf#L54) | 0.119226 / [input L42](https://github.com/TheRobotStudio/SO-ARM100/blob/a758567c3978dfeefe282ede0500085a48fe8f78/Simulation/SO100/so100.urdf#L42) |
| Upper_Arm | 0.162409 / [input L81](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/trs_so_arm100/so_arm100.xml#L81) | 0.162409285 / [input L107](https://github.com/TheRobotStudio/SO-ARM100/blob/4e9c5588d8a8415b6a6c2142a0ce8c32207cf3e9/URDF/SO_5DOF_ARM100_8j_URDF.SLDASM/urdf/SO_5DOF_ARM100_8j_URDF.SLDASM.urdf#L107) | 0.162409 / [input L68](https://github.com/TheRobotStudio/SO-ARM100/blob/a758567c3978dfeefe282ede0500085a48fe8f78/Simulation/SO100/so100.urdf#L68) |
| Lower_Arm | 0.147968 / [input L88](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/trs_so_arm100/so_arm100.xml#L88) | 0.147967775 / [input L160](https://github.com/TheRobotStudio/SO-ARM100/blob/4e9c5588d8a8415b6a6c2142a0ce8c32207cf3e9/URDF/SO_5DOF_ARM100_8j_URDF.SLDASM/urdf/SO_5DOF_ARM100_8j_URDF.SLDASM.urdf#L160) | 0.147968 / [input L94](https://github.com/TheRobotStudio/SO-ARM100/blob/a758567c3978dfeefe282ede0500085a48fe8f78/Simulation/SO100/so100.urdf#L94) |
| Wrist_Pitch_Roll | 0.0661321 / [input L95](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/trs_so_arm100/so_arm100.xml#L95) | 0.0661320671 / [input L213](https://github.com/TheRobotStudio/SO-ARM100/blob/4e9c5588d8a8415b6a6c2142a0ce8c32207cf3e9/URDF/SO_5DOF_ARM100_8j_URDF.SLDASM/urdf/SO_5DOF_ARM100_8j_URDF.SLDASM.urdf#L213) | 0.0661321 / [input L120](https://github.com/TheRobotStudio/SO-ARM100/blob/a758567c3978dfeefe282ede0500085a48fe8f78/Simulation/SO100/so100.urdf#L120) |
| Fixed_Jaw | 0.0929859 / [input L102](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/trs_so_arm100/so_arm100.xml#L102) | 0.0929859131 / [input L266](https://github.com/TheRobotStudio/SO-ARM100/blob/4e9c5588d8a8415b6a6c2142a0ce8c32207cf3e9/URDF/SO_5DOF_ARM100_8j_URDF.SLDASM/urdf/SO_5DOF_ARM100_8j_URDF.SLDASM.urdf#L266) | 0.0929859 / [input L146](https://github.com/TheRobotStudio/SO-ARM100/blob/a758567c3978dfeefe282ede0500085a48fe8f78/Simulation/SO100/so100.urdf#L146) |
| Moving_Jaw | 0.0202444 / [input L114](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/trs_so_arm100/so_arm100.xml#L114) | 0.0202443795 / [input L319](https://github.com/TheRobotStudio/SO-ARM100/blob/4e9c5588d8a8415b6a6c2142a0ce8c32207cf3e9/URDF/SO_5DOF_ARM100_8j_URDF.SLDASM/urdf/SO_5DOF_ARM100_8j_URDF.SLDASM.urdf#L319) | 0.0202444 / [input L167](https://github.com/TheRobotStudio/SO-ARM100/blob/a758567c3978dfeefe282ede0500085a48fe8f78/Simulation/SO100/so100.urdf#L167) |

## Coverage and unmatched elements

```json
{
  "mapping_h": {
    "bodies": {
      "Base": "base",
      "Rotation_Pitch": "shoulder",
      "Upper_Arm": "upper_arm",
      "Lower_Arm": "lower_arm",
      "Wrist_Pitch_Roll": "wrist",
      "Fixed_Jaw": "gripper",
      "Moving_Jaw": "jaw"
    },
    "joints": {
      "Rotation": "shoulder_pan",
      "Pitch": "shoulder_lift",
      "Elbow": "elbow_flex",
      "Wrist_Pitch": "wrist_flex",
      "Wrist_Roll": "wrist_roll",
      "Jaw": "gripper"
    },
    "body_methods": {
      "Base": "unique kinematic subtree",
      "Rotation_Pitch": "unique kinematic subtree",
      "Upper_Arm": "unique kinematic subtree",
      "Lower_Arm": "unique kinematic subtree",
      "Wrist_Pitch_Roll": "unique kinematic subtree",
      "Fixed_Jaw": "unique kinematic subtree",
      "Moving_Jaw": "unique kinematic subtree"
    },
    "joint_methods": {
      "Rotation": "unique joint on matched body with same type and axis",
      "Pitch": "unique joint on matched body with same type and axis",
      "Elbow": "unique joint on matched body with same type and axis",
      "Wrist_Pitch": "unique joint on matched body with same type and axis",
      "Wrist_Roll": "unique joint on matched body with same type and axis",
      "Jaw": "unique joint on matched body with same type and axis"
    },
    "unmatched_m_bodies": [],
    "unmatched_upstream_bodies": [],
    "unmatched_m_joints": [],
    "unmatched_upstream_joints": [],
    "registration_anchor": {
      "M": "Base",
      "H": "base",
      "root_unmatched": false
    }
  },
  "mapping_s": {
    "bodies": {
      "Base": "Base",
      "Rotation_Pitch": "Rotation_Pitch",
      "Upper_Arm": "Upper_Arm",
      "Lower_Arm": "Lower_Arm",
      "Wrist_Pitch_Roll": "Wrist_Pitch_Roll",
      "Fixed_Jaw": "Fixed_Jaw",
      "Moving_Jaw": "Moving Jaw"
    },
    "joints": {
      "Rotation": "Rotation",
      "Pitch": "Pitch",
      "Elbow": "Elbow",
      "Wrist_Pitch": "Wrist_Pitch",
      "Wrist_Roll": "Wrist_Roll",
      "Jaw": "Jaw"
    },
    "body_methods": {
      "Base": "name",
      "Rotation_Pitch": "name",
      "Upper_Arm": "name",
      "Lower_Arm": "name",
      "Wrist_Pitch_Roll": "name",
      "Fixed_Jaw": "name",
      "Moving_Jaw": "unique kinematic subtree"
    },
    "joint_methods": {
      "Rotation": "name",
      "Pitch": "name",
      "Elbow": "name",
      "Wrist_Pitch": "name",
      "Wrist_Roll": "name",
      "Jaw": "name"
    },
    "unmatched_m_bodies": [],
    "unmatched_upstream_bodies": [],
    "unmatched_m_joints": [],
    "unmatched_upstream_joints": [],
    "registration_anchor": {
      "M": "Base",
      "S": "Base"
    }
  },
  "unavailable": [
    {
      "entity": "Rotation",
      "other_entity": "shoulder_pan",
      "quantity": "force",
      "tolerance": "limit",
      "m": 3.5,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "Rotation",
      "other_entity": "shoulder_pan",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 1.0,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "Pitch",
      "other_entity": "shoulder_lift",
      "quantity": "force",
      "tolerance": "limit",
      "m": 3.5,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "Pitch",
      "other_entity": "shoulder_lift",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 1.0,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "Elbow",
      "other_entity": "elbow_flex",
      "quantity": "force",
      "tolerance": "limit",
      "m": 3.5,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "Elbow",
      "other_entity": "elbow_flex",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 1.0,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "Wrist_Pitch",
      "other_entity": "wrist_flex",
      "quantity": "force",
      "tolerance": "limit",
      "m": 3.5,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "Wrist_Pitch",
      "other_entity": "wrist_flex",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 1.0,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "Wrist_Roll",
      "other_entity": "wrist_roll",
      "quantity": "force",
      "tolerance": "limit",
      "m": 3.5,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "Wrist_Roll",
      "other_entity": "wrist_roll",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 1.0,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "Jaw",
      "other_entity": "gripper",
      "quantity": "force",
      "tolerance": "limit",
      "m": 3.5,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "Jaw",
      "other_entity": "gripper",
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
| Rotation / force | 3.5 | unavailable | unavailable |
| Rotation / velocity | unavailable | unavailable | 1 |
| Pitch / force | 3.5 | unavailable | unavailable |
| Pitch / velocity | unavailable | unavailable | 1 |
| Elbow / force | 3.5 | unavailable | unavailable |
| Elbow / velocity | unavailable | unavailable | 1 |
| Wrist_Pitch / force | 3.5 | unavailable | unavailable |
| Wrist_Pitch / velocity | unavailable | unavailable | 1 |
| Wrist_Roll / force | 3.5 | unavailable | unavailable |
| Wrist_Roll / velocity | unavailable | unavailable | 1 |
| Jaw / force | 3.5 | unavailable | unavailable |
| Jaw / velocity | unavailable | unavailable | 1 |
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
  "https://github.com/TheRobotStudio/SO-ARM100 URDF/SO_5DOF_ARM100_8j_URDF.SLDASM/urdf/SO_5DOF_ARM100_8j_URDF.SLDASM.urdf at a758567c3978dfeefe282ede0500085a48fe8f78: CalledProcessError: Command '['git', '-C', '.cache/TheRobotStudio__SO-ARM100', 'show', 'a758567c3978dfeefe282ede0500085a48fe8f78:URDF/SO_5DOF_ARM100_8j_URDF.SLDASM/urdf/SO_5DOF_ARM100_8j_URDF.SLDASM.urdf']' returned non-zero exit status 128."
]
```

## Self comparisons

```json
[
  {
    "file": "trs_so_arm100/so_arm100.xml",
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
      "needs a human look": 4,
      "unknown": 12
    },
    "classifications_changed": 0,
    "finding_membership_changes": 0
  },
  "2": {
    "provenance_method": "pinned",
    "counts": {
      "needs a human look": 4,
      "unknown": 12
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
      "Base"
    ],
    "assets_loaded": 18,
    "mesh_conversions": [],
    "xacro_arguments": {},
    "source_dependencies": [
      "trs_so_arm100/so_arm100.xml"
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
    "xacro_arguments": {},
    "source_dependencies": [
      "Simulation/SO100/so100.urdf"
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
    "geometry_stripped": true,
    "missing_explicit_inertials": [],
    "assets_loaded": 0,
    "mesh_conversions": [],
    "xacro_arguments": {},
    "source_dependencies": [
      "URDF/SO_5DOF_ARM100_8j_URDF.SLDASM/urdf/SO_5DOF_ARM100_8j_URDF.SLDASM.urdf"
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
  "self_variants_recompiled": 1,
  "historical_snapshots_reused": 2,
  "primary_physics_unchanged": true,
  "source_matching": "original raw-value provenance criteria retained; kinematic guard applies to reported CoM"
}
```
