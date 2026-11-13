# unitree_h1

Status: **complete**. Provenance: **none**, confidence **none**.

No public revision matches all comparable quantities. Class: NO MATCHING SOURCE; never counted as STALE.

M: `https://github.com/google-deepmind/mujoco_menagerie`, `unitree_h1/h1.xml`, commit `370c43965323c0944b433b202aac5058b5f907a9`.
H: `https://github.com/unitreerobotics/unitree_ros`, `robots/h1_description/urdf/h1.urdf`, commit `157ff950351e5f535e03c5d85a16b7d594b3dbcc`.
S: unavailable. A machine-readable H can still be compared to M; no-match differences are never counted as STALE.

Limit semantics: MJCF effort values are supported actuator torque/force envelopes. URDF effort and velocity values are manufacturer declarations retained from XML; MuJoCo does not enforce those tags. Such declaration comparisons are explicitly distinct from compiled inertial/range quantities.


## README derivation evidence

Documentation labels are conservative: an automated documented label requires an explicit affected entity and quantity. Broader conversion notes are retained here for review.

> 1. Added `<mujoco> <compiler discardvisual="false" strippath="false" fusestatic="false"/> </mujoco>` to the URDF's

## Kinematics consistency

A proper Kabsch rigid transform aligns all matched zero-pose body origins. The maximum per-origin residual and signed hinge/slide axis angles determine whether CoM can be compared; RMS is also recorded. Fewer than three non-collinear origins give insufficient kinematic coverage. CoM records that fail either required M/H or M/S check are excluded from counts and largest discrepancies. Masses, principal moments and raw joint ranges remain unchanged; a flagged range still requires convention review.

| Pair | Status | Origins / rank | RMS / maximum mm | Disagreeing / checked axes |
|---|---|---:|---:|---:|
| M/H | consistent | 20 / 3 | 2.26370402e-05 / 3.4825342e-05 | 0 / 19 |

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
    "anchor_m": "pelvis",
    "anchor_other": "pelvis",
    "rotation_other_to_m": [
      [
        0.9999999999999997,
        5.0570735438144876e-18,
        -9.778026019757526e-10
      ],
      [
        -5.0570735391514276e-18,
        1.0,
        4.768918265913707e-18
      ],
      [
        9.778028109419523e-10,
        -4.768918260968887e-18,
        0.9999999999999997
      ]
    ],
    "translation_other_to_m": [
      -7.733135312659734e-11,
      4.691328953858494e-19,
      -1.4596718778125961e-08
    ],
    "rms_residual_m": 2.2637040170197347e-08,
    "max_residual_m": 3.482534197742629e-08,
    "fit_rank": 3,
    "axis_checks": [
      {
        "joint_m": "left_hip_yaw",
        "joint_other": "left_hip_yaw_joint",
        "axis_m": [
          0.0,
          0.0,
          1.0
        ],
        "axis_other_aligned": [
          -9.77802601975753e-10,
          4.768918265913709e-18,
          1.0
        ],
        "angle_rad": 9.77802601975753e-10,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "left_hip_roll",
        "joint_other": "left_hip_roll_joint",
        "axis_m": [
          1.0,
          0.0,
          0.0
        ],
        "axis_other_aligned": [
          1.0,
          -5.057073539151429e-18,
          9.778028109419527e-10
        ],
        "angle_rad": 9.778028109419527e-10,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "left_hip_pitch",
        "joint_other": "left_hip_pitch_joint",
        "axis_m": [
          0.0,
          1.0,
          0.0
        ],
        "axis_other_aligned": [
          5.0570735438144876e-18,
          1.0,
          -4.768918260968887e-18
        ],
        "angle_rad": 6.951012459156647e-18,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "left_knee",
        "joint_other": "left_knee_joint",
        "axis_m": [
          0.0,
          1.0,
          0.0
        ],
        "axis_other_aligned": [
          5.0570735438144876e-18,
          1.0,
          -4.768918260968887e-18
        ],
        "angle_rad": 6.951012459156647e-18,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "left_ankle",
        "joint_other": "left_ankle_joint",
        "axis_m": [
          0.0,
          1.0,
          0.0
        ],
        "axis_other_aligned": [
          5.0570735438144876e-18,
          1.0,
          -4.768918260968887e-18
        ],
        "angle_rad": 6.951012459156647e-18,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "right_hip_yaw",
        "joint_other": "right_hip_yaw_joint",
        "axis_m": [
          0.0,
          0.0,
          1.0
        ],
        "axis_other_aligned": [
          -9.77802601975753e-10,
          4.768918265913709e-18,
          1.0
        ],
        "angle_rad": 9.77802601975753e-10,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "right_hip_roll",
        "joint_other": "right_hip_roll_joint",
        "axis_m": [
          1.0,
          0.0,
          0.0
        ],
        "axis_other_aligned": [
          1.0,
          -5.057073539151429e-18,
          9.778028109419527e-10
        ],
        "angle_rad": 9.778028109419527e-10,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "right_hip_pitch",
        "joint_other": "right_hip_pitch_joint",
        "axis_m": [
          0.0,
          1.0,
          0.0
        ],
        "axis_other_aligned": [
          5.0570735438144876e-18,
          1.0,
          -4.768918260968887e-18
        ],
        "angle_rad": 6.951012459156647e-18,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "right_knee",
        "joint_other": "right_knee_joint",
        "axis_m": [
          0.0,
          1.0,
          0.0
        ],
        "axis_other_aligned": [
          5.0570735438144876e-18,
          1.0,
          -4.768918260968887e-18
        ],
        "angle_rad": 6.951012459156647e-18,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "right_ankle",
        "joint_other": "right_ankle_joint",
        "axis_m": [
          0.0,
          1.0,
          0.0
        ],
        "axis_other_aligned": [
          5.0570735438144876e-18,
          1.0,
          -4.768918260968887e-18
        ],
        "angle_rad": 6.951012459156647e-18,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "torso",
        "joint_other": "torso_joint",
        "axis_m": [
          0.0,
          0.0,
          1.0
        ],
        "axis_other_aligned": [
          -9.77802601975753e-10,
          4.768918265913709e-18,
          1.0
        ],
        "angle_rad": 9.77802601975753e-10,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "left_shoulder_pitch",
        "joint_other": "left_shoulder_pitch_joint",
        "axis_m": [
          0.0,
          0.9063091175534986,
          0.4226154084263831
        ],
        "axis_other_aligned": [
          -4.132351816316765e-10,
          0.906308764549666,
          0.4226161654509422
        ],
        "angle_rad": 8.352832212239623e-07,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "left_shoulder_roll",
        "joint_other": "left_shoulder_roll_joint",
        "axis_m": [
          1.0,
          0.0,
          0.0
        ],
        "axis_other_aligned": [
          1.0,
          -5.057073539151429e-18,
          9.778028109419527e-10
        ],
        "angle_rad": 9.778028109419527e-10,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "left_shoulder_yaw",
        "joint_other": "left_shoulder_yaw_joint",
        "axis_m": [
          0.0,
          1.3494461133010112e-17,
          1.0
        ],
        "axis_other_aligned": [
          -9.77802601975753e-10,
          -2.1318256664803615e-17,
          1.0
        ],
        "angle_rad": 9.778026019757536e-10,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "left_elbow",
        "joint_other": "left_elbow_joint",
        "axis_m": [
          0.0,
          1.0,
          -1.3494461133010112e-17
        ],
        "axis_other_aligned": [
          5.05707351830638e-18,
          1.0,
          2.131825666974842e-17
        ],
        "angle_rad": 3.5178108439540303e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "right_shoulder_pitch",
        "joint_other": "right_shoulder_pitch_joint",
        "axis_m": [
          0.0,
          0.9063091175534986,
          -0.4226154084263831
        ],
        "axis_other_aligned": [
          4.132351907982167e-10,
          0.906308764549666,
          -0.4226161654509422
        ],
        "angle_rad": 8.352832212239669e-07,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "right_shoulder_roll",
        "joint_other": "right_shoulder_roll_joint",
        "axis_m": [
          1.0,
          0.0,
          0.0
        ],
        "axis_other_aligned": [
          1.0,
          -5.057073539151429e-18,
          9.778028109419527e-10
        ],
        "angle_rad": 9.778028109419527e-10,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "right_shoulder_yaw",
        "joint_other": "right_shoulder_yaw_joint",
        "axis_m": [
          0.0,
          -1.3494461133010112e-17,
          1.0
        ],
        "axis_other_aligned": [
          -9.77802601975753e-10,
          3.0856093196631034e-17,
          1.0
        ],
        "angle_rad": 9.77802601975754e-10,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "right_elbow",
        "joint_other": "right_elbow_joint",
        "axis_m": [
          0.0,
          1.0,
          1.3494461133010112e-17
        ],
        "axis_other_aligned": [
          5.0570735693225954e-18,
          1.0,
          -3.0856093191686195e-17
        ],
        "angle_rad": 4.463793971492613e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      }
    ],
    "axis_disagreements": [],
    "com_eligible": true,
    "covariance_singular_values": [
      3.5814336721940387,
      0.5993747031678194,
      0.0030645263229153543
    ],
    "origin_residuals_m": {
      "pelvis": 1.4596923621978414e-08,
      "left_hip_yaw_link": 1.4597014968921709e-08,
      "left_hip_roll_link": 1.4558423818974894e-08,
      "left_hip_pitch_link": 1.4558423818974894e-08,
      "left_knee_link": 1.4566174106385365e-08,
      "left_ankle_link": 1.4584412975620216e-08,
      "right_hip_yaw_link": 1.4597014968916071e-08,
      "right_hip_roll_link": 1.4558423818974894e-08,
      "right_hip_pitch_link": 1.4558423818974894e-08,
      "right_knee_link": 1.4566174106385365e-08,
      "right_ankle_link": 1.4584412975620216e-08,
      "torso_link": 1.4596923621978414e-08,
      "left_shoulder_pitch_link": 1.4599829374554987e-08,
      "left_shoulder_roll_link": 3.48108835163216e-08,
      "left_shoulder_yaw_link": 3.480922062493389e-08,
      "left_elbow_link": 3.482534197742629e-08,
      "right_shoulder_pitch_link": 1.4599829374614132e-08,
      "right_shoulder_roll_link": 3.4810883516353024e-08,
      "right_shoulder_yaw_link": 3.480922062495716e-08,
      "right_elbow_link": 3.482534197742629e-08
    },
    "reason": "Unique proper rigid fit and matched signed axes meet the configured thresholds"
  }
}
```


## Every reported quantity difference

Counts are quantity records, including correlated total/subtree/body mass records; they are not independent robot defects.

| Entity / quantity | M | S | H | H − M | Class | M source | S source | H source |
|---|---|---|---|---|---|---|---|---|
| robot / total_mass | 51.437 | unavailable | 59.3380126 | 7.90101257 | NO MATCHING SOURCE | [aggregate inputs](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_h1/h1.xml#L1) | unavailable | [aggregate inputs](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/h1_description/urdf/h1.urdf#L1) |
| robot / total_com_registered | [0.0162599623, 0.000971507533, -0.0350662197] | unavailable | [0.0164705078, 0.000842249534, -0.0787576569] | [0.000210545516, -0.000129257999, -0.0436914372] | NO MATCHING SOURCE | [aggregate inputs](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_h1/h1.xml#L1) | unavailable | [aggregate inputs](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/h1_description/urdf/h1.urdf#L1) |
| pelvis / mass | 5.39 | unavailable | 5.983 | 0.593 | NO MATCHING SOURCE | [input L61](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_h1/h1.xml#L61) | unavailable | [input L19](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/h1_description/urdf/h1.urdf#L19) |
| pelvis / subtree_mass | 51.437 | unavailable | 59.3380126 | 7.90101257 | NO MATCHING SOURCE | [subtree root L59](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_h1/h1.xml#L59) | unavailable | [subtree root L16](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/h1_description/urdf/h1.urdf#L16) |
| pelvis / com_registered | [-0.0002, 4e-05, -0.04522] | unavailable | [-0.000400000032, 3.7e-05, -0.0468640146] | [-0.000200000032, -3e-06, -0.0016440146] | NO MATCHING SOURCE | [CoM/kinematic input L61](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_h1/h1.xml#L61) | unavailable | [CoM/kinematic input L18](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/h1_description/urdf/h1.urdf#L18) |
| pelvis / principal_moments | [0.00824619, 0.0445821, 0.0490211] | unavailable | [0.0090258339, 0.0491678319, 0.0531564802] | [0.000779643903, 0.00458573194, 0.00413538015] | NO MATCHING SOURCE | [inertia input L61](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_h1/h1.xml#L61) | unavailable | [inertia input L20](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/h1_description/urdf/h1.urdf#L20) |
| left_hip_yaw_link / mass | 2.244 | unavailable | 2.965 | 0.721 | NO MATCHING SOURCE | [input L66](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_h1/h1.xml#L66) | unavailable | [input L41](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/h1_description/urdf/h1.urdf#L41) |
| left_hip_yaw_link / subtree_mass | 10.795 | unavailable | 14.182 | 3.387 | NO MATCHING SOURCE | [subtree root L64](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_h1/h1.xml#L64) | unavailable | [subtree root L38](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/h1_description/urdf/h1.urdf#L38) |
| left_hip_yaw_link / com_registered | [-0.04923, 0.0876, -0.167] | unavailable | [-0.0614329999, 0.087517, -0.166573015] | [-0.0122029999, -8.3e-05, 0.000426985343] | NO MATCHING SOURCE | [CoM/kinematic input L66](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_h1/h1.xml#L66) | unavailable | [CoM/kinematic input L40](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/h1_description/urdf/h1.urdf#L40) |
| left_hip_yaw_link / principal_moments | [0.00189201, 0.00296885, 0.00304494] | unavailable | [0.00364268483, 0.00501769221, 0.00577917496] | [0.00175067483, 0.00204884221, 0.00273423496] | NO MATCHING SOURCE | [inertia input L66](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_h1/h1.xml#L66) | unavailable | [inertia input L42](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/h1_description/urdf/h1.urdf#L42) |
| left_hip_roll_link / mass | 2.232 | unavailable | 2.715 | 0.483 | NO MATCHING SOURCE | [input L72](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_h1/h1.xml#L72) | unavailable | [input L70](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/h1_description/urdf/h1.urdf#L70) |
| left_hip_roll_link / subtree_mass | 8.551 | unavailable | 11.217 | 2.666 | NO MATCHING SOURCE | [subtree root L70](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_h1/h1.xml#L70) | unavailable | [subtree root L67](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/h1_description/urdf/h1.urdf#L67) |
| left_hip_roll_link / com_registered | [0.033668, 0.08431, -0.17429] | unavailable | [0.0341920001, 0.073927, -0.174196015] | [0.000524000093, -0.010383, 9.39854367e-05] | NO MATCHING SOURCE | [CoM/kinematic input L72](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_h1/h1.xml#L72) | unavailable | [CoM/kinematic input L69](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/h1_description/urdf/h1.urdf#L69) |
| left_hip_roll_link / principal_moments | [0.00205492, 0.00225325, 0.00243264] | unavailable | [0.00305823052, 0.00347559669, 0.00438902979] | [0.00100331052, 0.00122234669, 0.00195638979] | NO MATCHING SOURCE | [inertia input L72](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_h1/h1.xml#L72) | unavailable | [inertia input L71](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/h1_description/urdf/h1.urdf#L71) |
| left_hip_pitch_link / mass | 4.152 | unavailable | 4.953 | 0.801 | NO MATCHING SOURCE | [input L78](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_h1/h1.xml#L78) | unavailable | [input L99](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/h1_description/urdf/h1.urdf#L99) |
| left_hip_pitch_link / subtree_mass | 6.319 | unavailable | 8.502 | 2.183 | NO MATCHING SOURCE | [subtree root L76](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_h1/h1.xml#L76) | unavailable | [subtree root L96](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/h1_description/urdf/h1.urdf#L96) |
| left_hip_pitch_link / com_registered | [0.046928, 0.1794, -0.25613] | unavailable | [0.0471040002, 0.173562, -0.256870015] | [0.000176000174, -0.005838, -0.000740014551] | NO MATCHING SOURCE | [CoM/kinematic input L78](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_h1/h1.xml#L78) | unavailable | [CoM/kinematic input L98](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/h1_description/urdf/h1.urdf#L98) |
| left_hip_pitch_link / principal_moments | [0.00510909, 0.0821457, 0.0829503] | unavailable | [0.00678241149, 0.0962457546, 0.0968615819] | [0.00167332149, 0.0141000546, 0.0139112819] | NO MATCHING SOURCE | [inertia input L78](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_h1/h1.xml#L78) | unavailable | [inertia input L100](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/h1_description/urdf/h1.urdf#L100) |
| left_knee_link / mass | 1.721 | unavailable | 2.824 | 1.103 | NO MATCHING SOURCE | [input L86](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_h1/h1.xml#L86) | unavailable | [input L128](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/h1_description/urdf/h1.urdf#L128) |
| left_knee_link / subtree_mass | 2.167 | unavailable | 3.549 | 1.382 | NO MATCHING SOURCE | [subtree root L84](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_h1/h1.xml#L84) | unavailable | [subtree root L125](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/h1_description/urdf/h1.urdf#L125) |
| left_knee_link / com_registered | [0.038108, 0.19774, -0.7126] | unavailable | [0.0428740006, 0.197581, -0.717902015] | [0.00476600062, -0.000159, -0.00530201455] | NO MATCHING SOURCE | [CoM/kinematic input L86](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_h1/h1.xml#L86) | unavailable | [CoM/kinematic input L127](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/h1_description/urdf/h1.urdf#L127) |
| left_knee_link / principal_moments | [0.0019428, 0.0123104, 0.0125237] | unavailable | [0.00314179105, 0.023832889, 0.0245583159] | [0.00119899105, 0.011522489, 0.0120346159] | NO MATCHING SOURCE | [inertia input L86](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_h1/h1.xml#L86) | unavailable | [inertia input L129](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/h1_description/urdf/h1.urdf#L129) |
| left_ankle_link / mass | 0.446 | unavailable | 0.725 | 0.279 | NO MATCHING SOURCE | [input L93](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_h1/h1.xml#L93) | unavailable | [input L157](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/h1_description/urdf/h1.urdf#L157) |
| left_ankle_link / subtree_mass | 0.446 | unavailable | 0.725 | 0.279 | NO MATCHING SOURCE | [subtree root L91](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_h1/h1.xml#L91) | unavailable | [subtree root L154](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/h1_description/urdf/h1.urdf#L154) |
| left_ankle_link / com_registered | [0.106688, 0.20301, -1.01917] | unavailable | [0.0820050009, 0.20286, -1.01587401] | [-0.0246829991, -0.00015, 0.00329598548] | NO MATCHING SOURCE | [CoM/kinematic input L93](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_h1/h1.xml#L93) | unavailable | [CoM/kinematic input L156](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/h1_description/urdf/h1.urdf#L156) |
| left_ankle_link / principal_moments | [0.000214202, 0.00218961, 0.00220848] | unavailable | [0.000223391, 0.003158865, 0.003296133] | [9.18899999e-06, 0.000969255, 0.001087653] | NO MATCHING SOURCE | [inertia input L93](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_h1/h1.xml#L93) | unavailable | [inertia input L158](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/h1_description/urdf/h1.urdf#L158) |
| right_hip_yaw_link / mass | 2.244 | unavailable | 2.965 | 0.721 | NO MATCHING SOURCE | [input L106](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_h1/h1.xml#L106) | unavailable | [input L186](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/h1_description/urdf/h1.urdf#L186) |
| right_hip_yaw_link / subtree_mass | 10.795 | unavailable | 14.182 | 3.387 | NO MATCHING SOURCE | [subtree root L104](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_h1/h1.xml#L104) | unavailable | [subtree root L183](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/h1_description/urdf/h1.urdf#L183) |
| right_hip_yaw_link / com_registered | [-0.04923, -0.0876, -0.167] | unavailable | [-0.0614329999, -0.087517, -0.166573015] | [-0.0122029999, 8.3e-05, 0.000426985343] | NO MATCHING SOURCE | [CoM/kinematic input L106](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_h1/h1.xml#L106) | unavailable | [CoM/kinematic input L185](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/h1_description/urdf/h1.urdf#L185) |
| right_hip_yaw_link / principal_moments | [0.00189201, 0.00296885, 0.00304494] | unavailable | [0.00364268483, 0.00501769221, 0.00577917496] | [0.00175067483, 0.00204884221, 0.00273423496] | NO MATCHING SOURCE | [inertia input L106](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_h1/h1.xml#L106) | unavailable | [inertia input L187](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/h1_description/urdf/h1.urdf#L187) |
| right_hip_roll_link / mass | 2.232 | unavailable | 2.715 | 0.483 | NO MATCHING SOURCE | [input L112](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_h1/h1.xml#L112) | unavailable | [input L215](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/h1_description/urdf/h1.urdf#L215) |
| right_hip_roll_link / subtree_mass | 8.551 | unavailable | 11.217 | 2.666 | NO MATCHING SOURCE | [subtree root L110](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_h1/h1.xml#L110) | unavailable | [subtree root L212](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/h1_description/urdf/h1.urdf#L212) |
| right_hip_roll_link / com_registered | [0.033668, -0.08431, -0.17429] | unavailable | [0.0341920001, -0.073927, -0.174196015] | [0.000524000093, 0.010383, 9.39854367e-05] | NO MATCHING SOURCE | [CoM/kinematic input L112](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_h1/h1.xml#L112) | unavailable | [CoM/kinematic input L214](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/h1_description/urdf/h1.urdf#L214) |
| right_hip_roll_link / principal_moments | [0.00205492, 0.00225325, 0.00243264] | unavailable | [0.00305823052, 0.00347559669, 0.00438902979] | [0.00100331052, 0.00122234669, 0.00195638979] | NO MATCHING SOURCE | [inertia input L112](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_h1/h1.xml#L112) | unavailable | [inertia input L216](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/h1_description/urdf/h1.urdf#L216) |
| right_hip_pitch_link / mass | 4.152 | unavailable | 4.953 | 0.801 | NO MATCHING SOURCE | [input L118](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_h1/h1.xml#L118) | unavailable | [input L244](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/h1_description/urdf/h1.urdf#L244) |
| right_hip_pitch_link / subtree_mass | 6.319 | unavailable | 8.502 | 2.183 | NO MATCHING SOURCE | [subtree root L116](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_h1/h1.xml#L116) | unavailable | [subtree root L241](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/h1_description/urdf/h1.urdf#L241) |
| right_hip_pitch_link / com_registered | [0.046928, -0.1794, -0.25613] | unavailable | [0.0471040002, -0.173562, -0.256870015] | [0.000176000174, 0.005838, -0.000740014551] | NO MATCHING SOURCE | [CoM/kinematic input L118](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_h1/h1.xml#L118) | unavailable | [CoM/kinematic input L243](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/h1_description/urdf/h1.urdf#L243) |
| right_hip_pitch_link / principal_moments | [0.00510909, 0.0821457, 0.0829503] | unavailable | [0.00678241149, 0.0962457546, 0.0968615819] | [0.00167332149, 0.0141000546, 0.0139112819] | NO MATCHING SOURCE | [inertia input L118](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_h1/h1.xml#L118) | unavailable | [inertia input L245](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/h1_description/urdf/h1.urdf#L245) |
| right_knee_link / mass | 1.721 | unavailable | 2.824 | 1.103 | NO MATCHING SOURCE | [input L126](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_h1/h1.xml#L126) | unavailable | [input L273](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/h1_description/urdf/h1.urdf#L273) |
| right_knee_link / subtree_mass | 2.167 | unavailable | 3.549 | 1.382 | NO MATCHING SOURCE | [subtree root L124](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_h1/h1.xml#L124) | unavailable | [subtree root L270](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/h1_description/urdf/h1.urdf#L270) |
| right_knee_link / com_registered | [0.038108, -0.19774, -0.7126] | unavailable | [0.0428740006, -0.197581, -0.717902015] | [0.00476600062, 0.000159, -0.00530201455] | NO MATCHING SOURCE | [CoM/kinematic input L126](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_h1/h1.xml#L126) | unavailable | [CoM/kinematic input L272](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/h1_description/urdf/h1.urdf#L272) |
| right_knee_link / principal_moments | [0.0019428, 0.0123104, 0.0125237] | unavailable | [0.00314179105, 0.023832889, 0.0245583159] | [0.00119899105, 0.011522489, 0.0120346159] | NO MATCHING SOURCE | [inertia input L126](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_h1/h1.xml#L126) | unavailable | [inertia input L274](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/h1_description/urdf/h1.urdf#L274) |
| right_ankle_link / mass | 0.446 | unavailable | 0.725 | 0.279 | NO MATCHING SOURCE | [input L133](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_h1/h1.xml#L133) | unavailable | [input L302](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/h1_description/urdf/h1.urdf#L302) |
| right_ankle_link / subtree_mass | 0.446 | unavailable | 0.725 | 0.279 | NO MATCHING SOURCE | [subtree root L131](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_h1/h1.xml#L131) | unavailable | [subtree root L299](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/h1_description/urdf/h1.urdf#L299) |
| right_ankle_link / com_registered | [0.106688, -0.20301, -1.01917] | unavailable | [0.0820050009, -0.20286, -1.01587401] | [-0.0246829991, 0.00015, 0.00329598548] | NO MATCHING SOURCE | [CoM/kinematic input L133](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_h1/h1.xml#L133) | unavailable | [CoM/kinematic input L301](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/h1_description/urdf/h1.urdf#L301) |
| right_ankle_link / principal_moments | [0.000214202, 0.00218961, 0.00220848] | unavailable | [0.000223391, 0.003158865, 0.003296133] | [9.18899999e-06, 0.000969255, 0.001087653] | NO MATCHING SOURCE | [inertia input L133](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_h1/h1.xml#L133) | unavailable | [inertia input L303](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/h1_description/urdf/h1.urdf#L303) |
| torso_link / subtree_mass | 24.457 | unavailable | 24.9910126 | 0.534012566 | NO MATCHING SOURCE | [subtree root L144](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_h1/h1.xml#L144) | unavailable | [subtree root L328](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/h1_description/urdf/h1.urdf#L328) |
| left_shoulder_pitch_link / mass | 1.033 | unavailable | 1.142 | 0.109 | NO MATCHING SOURCE | [input L157](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_h1/h1.xml#L157) | unavailable | [input L360](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/h1_description/urdf/h1.urdf#L360) |
| left_shoulder_pitch_link / subtree_mass | 3.334 | unavailable | 3.601 | 0.267 | NO MATCHING SOURCE | [subtree root L155](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_h1/h1.xml#L155) | unavailable | [subtree root L357](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/h1_description/urdf/h1.urdf#L357) |
| left_shoulder_roll_link / mass | 0.793 | unavailable | 0.852 | 0.059 | NO MATCHING SOURCE | [input L162](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_h1/h1.xml#L162) | unavailable | [input L389](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/h1_description/urdf/h1.urdf#L389) |
| left_shoulder_roll_link / subtree_mass | 2.301 | unavailable | 2.459 | 0.158 | NO MATCHING SOURCE | [subtree root L160](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_h1/h1.xml#L160) | unavailable | [subtree root L386](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/h1_description/urdf/h1.urdf#L386) |
| left_shoulder_yaw_link / mass | 0.839 | unavailable | 0.862 | 0.023 | NO MATCHING SOURCE | [input L169](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_h1/h1.xml#L169) | unavailable | [input L418](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/h1_description/urdf/h1.urdf#L418) |
| left_shoulder_yaw_link / subtree_mass | 1.508 | unavailable | 1.607 | 0.099 | NO MATCHING SOURCE | [subtree root L167](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_h1/h1.xml#L167) | unavailable | [subtree root L415](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/h1_description/urdf/h1.urdf#L415) |
| left_elbow_link / mass | 0.669 | unavailable | 0.745 | 0.076 | NO MATCHING SOURCE | [input L175](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_h1/h1.xml#L175) | unavailable | [input L447](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/h1_description/urdf/h1.urdf#L447) |
| left_elbow_link / subtree_mass | 0.669 | unavailable | 0.745 | 0.076 | NO MATCHING SOURCE | [subtree root L173](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_h1/h1.xml#L173) | unavailable | [subtree root L444](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/h1_description/urdf/h1.urdf#L444) |
| left_elbow_link / com_registered | [0.17758, 0.213385619, 0.0908376701] | unavailable | [0.183362, 0.213647612, 0.0908797043] | [0.00578199983, 0.000261992546, 4.2034179e-05] | NO MATCHING SOURCE | [CoM/kinematic input L175](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_h1/h1.xml#L175) | unavailable | [CoM/kinematic input L446](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/h1_description/urdf/h1.urdf#L446) |
| right_shoulder_pitch_link / mass | 1.033 | unavailable | 1.142 | 0.109 | NO MATCHING SOURCE | [input L186](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_h1/h1.xml#L186) | unavailable | [input L476](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/h1_description/urdf/h1.urdf#L476) |
| right_shoulder_pitch_link / subtree_mass | 3.334 | unavailable | 3.601 | 0.267 | NO MATCHING SOURCE | [subtree root L184](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_h1/h1.xml#L184) | unavailable | [subtree root L473](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/h1_description/urdf/h1.urdf#L473) |
| right_shoulder_roll_link / mass | 0.793 | unavailable | 0.852 | 0.059 | NO MATCHING SOURCE | [input L191](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_h1/h1.xml#L191) | unavailable | [input L505](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/h1_description/urdf/h1.urdf#L505) |
| right_shoulder_roll_link / subtree_mass | 2.301 | unavailable | 2.459 | 0.158 | NO MATCHING SOURCE | [subtree root L189](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_h1/h1.xml#L189) | unavailable | [subtree root L502](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/h1_description/urdf/h1.urdf#L502) |
| right_shoulder_yaw_link / mass | 0.839 | unavailable | 0.862 | 0.023 | NO MATCHING SOURCE | [input L198](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_h1/h1.xml#L198) | unavailable | [input L534](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/h1_description/urdf/h1.urdf#L534) |
| right_shoulder_yaw_link / subtree_mass | 1.508 | unavailable | 1.607 | 0.099 | NO MATCHING SOURCE | [subtree root L196](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_h1/h1.xml#L196) | unavailable | [subtree root L531](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/h1_description/urdf/h1.urdf#L531) |
| right_elbow_link / mass | 0.669 | unavailable | 0.745 | 0.076 | NO MATCHING SOURCE | [input L204](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_h1/h1.xml#L204) | unavailable | [input L563](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/h1_description/urdf/h1.urdf#L563) |
| right_elbow_link / subtree_mass | 0.669 | unavailable | 0.745 | 0.076 | NO MATCHING SOURCE | [subtree root L202](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_h1/h1.xml#L202) | unavailable | [subtree root L560](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/h1_description/urdf/h1.urdf#L560) |
| right_elbow_link / com_registered | [0.17758, -0.213385619, 0.0908376701] | unavailable | [0.183362, -0.213647612, 0.0908797043] | [0.00578199983, -0.000261992546, 4.2034179e-05] | NO MATCHING SOURCE | [CoM/kinematic input L204](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_h1/h1.xml#L204) | unavailable | [CoM/kinematic input L562](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/h1_description/urdf/h1.urdf#L562) |
| left_hip_pitch / range | [-1.57, 1.57] | unavailable | [-3.14, 2.53] | [-1.57, 0.96] | NO MATCHING SOURCE | [input L79](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_h1/h1.xml#L79) | unavailable | [input L123](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/h1_description/urdf/h1.urdf#L123) |
| right_hip_pitch / range | [-1.57, 1.57] | unavailable | [-3.14, 2.53] | [-1.57, 0.96] | NO MATCHING SOURCE | [input L119](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_h1/h1.xml#L119) | unavailable | [input L268](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/h1_description/urdf/h1.urdf#L268) |

## Raw CoM records and reporting decisions

Raw values retain the previous root-anchor registration before Kabsch; original world coordinates also remain in the snapshots. Eligible findings above use the fitted transform into M. Excluded raw records below are diagnostic numbers, not findings. No CoM suppression applies to mass or principal inertia moments.

| Entity / quantity | Raw M | Raw S | Raw H | Raw H − M | Decision | M source | S source | H source |
|---|---|---|---|---|---|---|---|---|
| robot / total_com_registered | [0.0162599623, 0.000971507533, -0.0350662197] | unavailable | [0.0164705078, 0.000842249534, -0.0787576423] | [0.000210545516, -0.000129257999, -0.0436914227] | eligible; compared after Kabsch alignment | [aggregate inputs](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_h1/h1.xml#L1) | unavailable | [aggregate inputs](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/h1_description/urdf/h1.urdf#L1) |
| pelvis / com_registered | [-0.0002, 4e-05, -0.04522] | unavailable | [-0.0004, 3.7e-05, -0.046864] | [-0.0002, -3e-06, -0.001644] | eligible; compared after Kabsch alignment | [CoM/kinematic input L61](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_h1/h1.xml#L61) | unavailable | [CoM/kinematic input L18](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/h1_description/urdf/h1.urdf#L18) |
| left_hip_yaw_link / com_registered | [-0.04923, 0.0876, -0.167] | unavailable | [-0.061433, 0.087517, -0.166573] | [-0.012203, -8.3e-05, 0.000427] | eligible; compared after Kabsch alignment | [CoM/kinematic input L66](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_h1/h1.xml#L66) | unavailable | [CoM/kinematic input L40](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/h1_description/urdf/h1.urdf#L40) |
| left_hip_roll_link / com_registered | [0.033668, 0.08431, -0.17429] | unavailable | [0.034192, 0.073927, -0.174196] | [0.000524, -0.010383, 9.4e-05] | eligible; compared after Kabsch alignment | [CoM/kinematic input L72](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_h1/h1.xml#L72) | unavailable | [CoM/kinematic input L69](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/h1_description/urdf/h1.urdf#L69) |
| left_hip_pitch_link / com_registered | [0.046928, 0.1794, -0.25613] | unavailable | [0.047104, 0.173562, -0.25687] | [0.000176, -0.005838, -0.00074] | eligible; compared after Kabsch alignment | [CoM/kinematic input L78](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_h1/h1.xml#L78) | unavailable | [CoM/kinematic input L98](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/h1_description/urdf/h1.urdf#L98) |
| left_knee_link / com_registered | [0.038108, 0.19774, -0.7126] | unavailable | [0.042874, 0.197581, -0.717902] | [0.004766, -0.000159, -0.005302] | eligible; compared after Kabsch alignment | [CoM/kinematic input L86](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_h1/h1.xml#L86) | unavailable | [CoM/kinematic input L127](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/h1_description/urdf/h1.urdf#L127) |
| left_ankle_link / com_registered | [0.106688, 0.20301, -1.01917] | unavailable | [0.082005, 0.20286, -1.015874] | [-0.024683, -0.00015, 0.003296] | eligible; compared after Kabsch alignment | [CoM/kinematic input L93](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_h1/h1.xml#L93) | unavailable | [CoM/kinematic input L156](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/h1_description/urdf/h1.urdf#L156) |
| right_hip_yaw_link / com_registered | [-0.04923, -0.0876, -0.167] | unavailable | [-0.061433, -0.087517, -0.166573] | [-0.012203, 8.3e-05, 0.000427] | eligible; compared after Kabsch alignment | [CoM/kinematic input L106](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_h1/h1.xml#L106) | unavailable | [CoM/kinematic input L185](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/h1_description/urdf/h1.urdf#L185) |
| right_hip_roll_link / com_registered | [0.033668, -0.08431, -0.17429] | unavailable | [0.034192, -0.073927, -0.174196] | [0.000524, 0.010383, 9.4e-05] | eligible; compared after Kabsch alignment | [CoM/kinematic input L112](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_h1/h1.xml#L112) | unavailable | [CoM/kinematic input L214](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/h1_description/urdf/h1.urdf#L214) |
| right_hip_pitch_link / com_registered | [0.046928, -0.1794, -0.25613] | unavailable | [0.047104, -0.173562, -0.25687] | [0.000176, 0.005838, -0.00074] | eligible; compared after Kabsch alignment | [CoM/kinematic input L118](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_h1/h1.xml#L118) | unavailable | [CoM/kinematic input L243](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/h1_description/urdf/h1.urdf#L243) |
| right_knee_link / com_registered | [0.038108, -0.19774, -0.7126] | unavailable | [0.042874, -0.197581, -0.717902] | [0.004766, 0.000159, -0.005302] | eligible; compared after Kabsch alignment | [CoM/kinematic input L126](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_h1/h1.xml#L126) | unavailable | [CoM/kinematic input L272](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/h1_description/urdf/h1.urdf#L272) |
| right_ankle_link / com_registered | [0.106688, -0.20301, -1.01917] | unavailable | [0.082005, -0.20286, -1.015874] | [-0.024683, 0.00015, 0.003296] | eligible; compared after Kabsch alignment | [CoM/kinematic input L133](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_h1/h1.xml#L133) | unavailable | [CoM/kinematic input L301](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/h1_description/urdf/h1.urdf#L301) |
| torso_link / com_registered | [0.000489, 0.002797, 0.20484] | unavailable | [0.000489, 0.002797, 0.20484] | [0, 0, 8.32667268e-17] | eligible; compared after Kabsch alignment | [CoM/kinematic input L146](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_h1/h1.xml#L146) | unavailable | [CoM/kinematic input L330](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/h1_description/urdf/h1.urdf#L330) |
| left_shoulder_pitch_link / com_registered | [0.010545, 0.210621229, 0.438423627] | unavailable | [0.010545, 0.210621222, 0.438423673] | [0, -7.04448569e-09, 4.6167122e-08] | eligible; compared after Kabsch alignment | [CoM/kinematic input L157](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_h1/h1.xml#L157) | unavailable | [CoM/kinematic input L359](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/h1_description/urdf/h1.urdf#L359) |
| left_shoulder_roll_link / com_registered | [0.000679, 0.214679619, 0.34483767] | unavailable | [0.000679, 0.214679612, 0.344837719] | [0, -7.45381135e-09, 4.85964508e-08] | eligible; compared after Kabsch alignment | [CoM/kinematic input L162](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_h1/h1.xml#L162) | unavailable | [CoM/kinematic input L388](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/h1_description/urdf/h1.urdf#L388) |
| left_shoulder_yaw_link / com_registered | [0.01365, 0.216296619, 0.14195367] | unavailable | [0.01365, 0.216296612, 0.141953719] | [0, -7.45381135e-09, 4.85964509e-08] | eligible; compared after Kabsch alignment | [CoM/kinematic input L169](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_h1/h1.xml#L169) | unavailable | [CoM/kinematic input L417](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/h1_description/urdf/h1.urdf#L417) |
| left_elbow_link / com_registered | [0.17758, 0.213385619, 0.0908376701] | unavailable | [0.183362, 0.213647612, 0.0908797187] | [0.005782, 0.000261992546, 4.20485965e-05] | eligible; compared after Kabsch alignment | [CoM/kinematic input L175](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_h1/h1.xml#L175) | unavailable | [CoM/kinematic input L446](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/h1_description/urdf/h1.urdf#L446) |
| right_shoulder_pitch_link / com_registered | [0.010545, -0.210621229, 0.438423627] | unavailable | [0.010545, -0.210621222, 0.438423673] | [0, 7.04448569e-09, 4.6167122e-08] | eligible; compared after Kabsch alignment | [CoM/kinematic input L186](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_h1/h1.xml#L186) | unavailable | [CoM/kinematic input L475](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/h1_description/urdf/h1.urdf#L475) |
| right_shoulder_roll_link / com_registered | [0.000679, -0.214679619, 0.34483767] | unavailable | [0.000679, -0.214679612, 0.344837719] | [0, 7.45381135e-09, 4.85964508e-08] | eligible; compared after Kabsch alignment | [CoM/kinematic input L191](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_h1/h1.xml#L191) | unavailable | [CoM/kinematic input L504](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/h1_description/urdf/h1.urdf#L504) |
| right_shoulder_yaw_link / com_registered | [0.01365, -0.216296619, 0.14195367] | unavailable | [0.01365, -0.216296612, 0.141953719] | [0, 7.45381135e-09, 4.85964509e-08] | eligible; compared after Kabsch alignment | [CoM/kinematic input L198](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_h1/h1.xml#L198) | unavailable | [CoM/kinematic input L533](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/h1_description/urdf/h1.urdf#L533) |
| right_elbow_link / com_registered | [0.17758, -0.213385619, 0.0908376701] | unavailable | [0.183362, -0.213647612, 0.0908797187] | [0.005782, -0.000261992546, 4.20485965e-05] | eligible; compared after Kabsch alignment | [CoM/kinematic input L204](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_h1/h1.xml#L204) | unavailable | [CoM/kinematic input L562](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/h1_description/urdf/h1.urdf#L562) |

## Mass accounting

Every contributing compiled body mass is listed here so total/subtree sums can be checked. Links point to explicit inertials or to geometry inputs when the compiler inferred a mass. CoM links identify inertial inputs; world coordinates additionally use the ancestor transforms and the registration recorded below.

| M body | M kg / source | S kg / source | H kg / source |
|---|---|---|---|
| pelvis | 5.39 / [input L61](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_h1/h1.xml#L61) | unavailable | 5.983 / [input L19](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/h1_description/urdf/h1.urdf#L19) |
| left_hip_yaw_link | 2.244 / [input L66](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_h1/h1.xml#L66) | unavailable | 2.965 / [input L41](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/h1_description/urdf/h1.urdf#L41) |
| left_hip_roll_link | 2.232 / [input L72](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_h1/h1.xml#L72) | unavailable | 2.715 / [input L70](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/h1_description/urdf/h1.urdf#L70) |
| left_hip_pitch_link | 4.152 / [input L78](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_h1/h1.xml#L78) | unavailable | 4.953 / [input L99](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/h1_description/urdf/h1.urdf#L99) |
| left_knee_link | 1.721 / [input L86](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_h1/h1.xml#L86) | unavailable | 2.824 / [input L128](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/h1_description/urdf/h1.urdf#L128) |
| left_ankle_link | 0.446 / [input L93](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_h1/h1.xml#L93) | unavailable | 0.725 / [input L157](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/h1_description/urdf/h1.urdf#L157) |
| right_hip_yaw_link | 2.244 / [input L106](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_h1/h1.xml#L106) | unavailable | 2.965 / [input L186](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/h1_description/urdf/h1.urdf#L186) |
| right_hip_roll_link | 2.232 / [input L112](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_h1/h1.xml#L112) | unavailable | 2.715 / [input L215](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/h1_description/urdf/h1.urdf#L215) |
| right_hip_pitch_link | 4.152 / [input L118](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_h1/h1.xml#L118) | unavailable | 4.953 / [input L244](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/h1_description/urdf/h1.urdf#L244) |
| right_knee_link | 1.721 / [input L126](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_h1/h1.xml#L126) | unavailable | 2.824 / [input L273](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/h1_description/urdf/h1.urdf#L273) |
| right_ankle_link | 0.446 / [input L133](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_h1/h1.xml#L133) | unavailable | 0.725 / [input L302](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/h1_description/urdf/h1.urdf#L302) |
| torso_link | 17.789 / [input L146](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_h1/h1.xml#L146) | unavailable | 17.789 / [input L331](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/h1_description/urdf/h1.urdf#L331) |
| left_shoulder_pitch_link | 1.033 / [input L157](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_h1/h1.xml#L157) | unavailable | 1.142 / [input L360](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/h1_description/urdf/h1.urdf#L360) |
| left_shoulder_roll_link | 0.793 / [input L162](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_h1/h1.xml#L162) | unavailable | 0.852 / [input L389](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/h1_description/urdf/h1.urdf#L389) |
| left_shoulder_yaw_link | 0.839 / [input L169](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_h1/h1.xml#L169) | unavailable | 0.862 / [input L418](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/h1_description/urdf/h1.urdf#L418) |
| left_elbow_link | 0.669 / [input L175](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_h1/h1.xml#L175) | unavailable | 0.745 / [input L447](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/h1_description/urdf/h1.urdf#L447) |
| right_shoulder_pitch_link | 1.033 / [input L186](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_h1/h1.xml#L186) | unavailable | 1.142 / [input L476](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/h1_description/urdf/h1.urdf#L476) |
| right_shoulder_roll_link | 0.793 / [input L191](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_h1/h1.xml#L191) | unavailable | 0.852 / [input L505](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/h1_description/urdf/h1.urdf#L505) |
| right_shoulder_yaw_link | 0.839 / [input L198](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_h1/h1.xml#L198) | unavailable | 0.862 / [input L534](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/h1_description/urdf/h1.urdf#L534) |
| right_elbow_link | 0.669 / [input L204](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_h1/h1.xml#L204) | unavailable | 0.745 / [input L563](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/h1_description/urdf/h1.urdf#L563) |
| upstream-only d435_left_imager_link | unavailable | unavailable | 4.1887902e-06 / [geometry/inference input L615](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/h1_description/urdf/h1.urdf#L615) |
| upstream-only d435_rgb_module_link | unavailable | unavailable | 4.1887902e-06 / [geometry/inference input L638](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/h1_description/urdf/h1.urdf#L638) |
| upstream-only imu_link | unavailable | unavailable | 0 / [geometry/inference input L589](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/h1_description/urdf/h1.urdf#L589) |
| upstream-only logo_link | unavailable | unavailable | 0 / [geometry/inference input L595](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/h1_description/urdf/h1.urdf#L595) |
| upstream-only mid360_link | unavailable | unavailable | 4.1887902e-06 / [geometry/inference input L661](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/h1_description/urdf/h1.urdf#L661) |

## Coverage and unmatched elements

```json
{
  "mapping_h": {
    "bodies": {
      "pelvis": "pelvis",
      "left_hip_yaw_link": "left_hip_yaw_link",
      "left_hip_roll_link": "left_hip_roll_link",
      "left_hip_pitch_link": "left_hip_pitch_link",
      "left_knee_link": "left_knee_link",
      "left_ankle_link": "left_ankle_link",
      "right_hip_yaw_link": "right_hip_yaw_link",
      "right_hip_roll_link": "right_hip_roll_link",
      "right_hip_pitch_link": "right_hip_pitch_link",
      "right_knee_link": "right_knee_link",
      "right_ankle_link": "right_ankle_link",
      "torso_link": "torso_link",
      "left_shoulder_pitch_link": "left_shoulder_pitch_link",
      "left_shoulder_roll_link": "left_shoulder_roll_link",
      "left_shoulder_yaw_link": "left_shoulder_yaw_link",
      "left_elbow_link": "left_elbow_link",
      "right_shoulder_pitch_link": "right_shoulder_pitch_link",
      "right_shoulder_roll_link": "right_shoulder_roll_link",
      "right_shoulder_yaw_link": "right_shoulder_yaw_link",
      "right_elbow_link": "right_elbow_link"
    },
    "joints": {
      "left_hip_yaw": "left_hip_yaw_joint",
      "left_hip_roll": "left_hip_roll_joint",
      "left_hip_pitch": "left_hip_pitch_joint",
      "left_knee": "left_knee_joint",
      "left_ankle": "left_ankle_joint",
      "right_hip_yaw": "right_hip_yaw_joint",
      "right_hip_roll": "right_hip_roll_joint",
      "right_hip_pitch": "right_hip_pitch_joint",
      "right_knee": "right_knee_joint",
      "right_ankle": "right_ankle_joint",
      "torso": "torso_joint",
      "left_shoulder_pitch": "left_shoulder_pitch_joint",
      "left_shoulder_roll": "left_shoulder_roll_joint",
      "left_shoulder_yaw": "left_shoulder_yaw_joint",
      "left_elbow": "left_elbow_joint",
      "right_shoulder_pitch": "right_shoulder_pitch_joint",
      "right_shoulder_roll": "right_shoulder_roll_joint",
      "right_shoulder_yaw": "right_shoulder_yaw_joint",
      "right_elbow": "right_elbow_joint"
    },
    "body_methods": {
      "pelvis": "name",
      "left_hip_yaw_link": "name",
      "left_hip_roll_link": "name",
      "left_hip_pitch_link": "name",
      "left_knee_link": "name",
      "left_ankle_link": "name",
      "right_hip_yaw_link": "name",
      "right_hip_roll_link": "name",
      "right_hip_pitch_link": "name",
      "right_knee_link": "name",
      "right_ankle_link": "name",
      "torso_link": "name",
      "left_shoulder_pitch_link": "name",
      "left_shoulder_roll_link": "name",
      "left_shoulder_yaw_link": "name",
      "left_elbow_link": "name",
      "right_shoulder_pitch_link": "name",
      "right_shoulder_roll_link": "name",
      "right_shoulder_yaw_link": "name",
      "right_elbow_link": "name"
    },
    "joint_methods": {
      "left_hip_yaw": "unique joint on matched body with same type and axis",
      "left_hip_roll": "unique joint on matched body with same type and axis",
      "left_hip_pitch": "unique joint on matched body with same type and axis",
      "left_knee": "unique joint on matched body with same type and axis",
      "left_ankle": "unique joint on matched body with same type and axis",
      "right_hip_yaw": "unique joint on matched body with same type and axis",
      "right_hip_roll": "unique joint on matched body with same type and axis",
      "right_hip_pitch": "unique joint on matched body with same type and axis",
      "right_knee": "unique joint on matched body with same type and axis",
      "right_ankle": "unique joint on matched body with same type and axis",
      "torso": "unique joint on matched body with same type and axis",
      "left_shoulder_pitch": "unique joint on matched body with same type and axis",
      "left_shoulder_roll": "unique joint on matched body with same type and axis",
      "left_shoulder_yaw": "unique joint on matched body with same type and axis",
      "left_elbow": "unique joint on matched body with same type and axis",
      "right_shoulder_pitch": "unique joint on matched body with same type and axis",
      "right_shoulder_roll": "unique joint on matched body with same type and axis",
      "right_shoulder_yaw": "unique joint on matched body with same type and axis",
      "right_elbow": "unique joint on matched body with same type and axis"
    },
    "unmatched_m_bodies": [],
    "unmatched_upstream_bodies": [
      "d435_left_imager_link",
      "d435_rgb_module_link",
      "imu_link",
      "logo_link",
      "mid360_link"
    ],
    "unmatched_m_joints": [],
    "unmatched_upstream_joints": [],
    "registration_anchor": {
      "M": "pelvis",
      "H": "pelvis",
      "root_unmatched": false
    }
  },
  "mapping_s": null,
  "unavailable": [
    {
      "entity": "left_hip_yaw",
      "other_entity": "left_hip_yaw_joint",
      "quantity": "force",
      "tolerance": "limit",
      "m": 200.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_hip_yaw",
      "other_entity": "left_hip_yaw_joint",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 23.0,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_hip_roll",
      "other_entity": "left_hip_roll_joint",
      "quantity": "force",
      "tolerance": "limit",
      "m": 200.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_hip_roll",
      "other_entity": "left_hip_roll_joint",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 23.0,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_hip_pitch",
      "other_entity": "left_hip_pitch_joint",
      "quantity": "force",
      "tolerance": "limit",
      "m": 200.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_hip_pitch",
      "other_entity": "left_hip_pitch_joint",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 23.0,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_knee",
      "other_entity": "left_knee_joint",
      "quantity": "force",
      "tolerance": "limit",
      "m": 300.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_knee",
      "other_entity": "left_knee_joint",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 14.0,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_ankle",
      "other_entity": "left_ankle_joint",
      "quantity": "force",
      "tolerance": "limit",
      "m": 40.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_ankle",
      "other_entity": "left_ankle_joint",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 9.0,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "right_hip_yaw",
      "other_entity": "right_hip_yaw_joint",
      "quantity": "force",
      "tolerance": "limit",
      "m": 200.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "right_hip_yaw",
      "other_entity": "right_hip_yaw_joint",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 23.0,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "right_hip_roll",
      "other_entity": "right_hip_roll_joint",
      "quantity": "force",
      "tolerance": "limit",
      "m": 200.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "right_hip_roll",
      "other_entity": "right_hip_roll_joint",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 23.0,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "right_hip_pitch",
      "other_entity": "right_hip_pitch_joint",
      "quantity": "force",
      "tolerance": "limit",
      "m": 200.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "right_hip_pitch",
      "other_entity": "right_hip_pitch_joint",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 23.0,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "right_knee",
      "other_entity": "right_knee_joint",
      "quantity": "force",
      "tolerance": "limit",
      "m": 300.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "right_knee",
      "other_entity": "right_knee_joint",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 14.0,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "right_ankle",
      "other_entity": "right_ankle_joint",
      "quantity": "force",
      "tolerance": "limit",
      "m": 40.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "right_ankle",
      "other_entity": "right_ankle_joint",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 9.0,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "torso",
      "other_entity": "torso_joint",
      "quantity": "force",
      "tolerance": "limit",
      "m": 200.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "torso",
      "other_entity": "torso_joint",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 23.0,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_shoulder_pitch",
      "other_entity": "left_shoulder_pitch_joint",
      "quantity": "force",
      "tolerance": "limit",
      "m": 40.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_shoulder_pitch",
      "other_entity": "left_shoulder_pitch_joint",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 9.0,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_shoulder_roll",
      "other_entity": "left_shoulder_roll_joint",
      "quantity": "force",
      "tolerance": "limit",
      "m": 40.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_shoulder_roll",
      "other_entity": "left_shoulder_roll_joint",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 9.0,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_shoulder_yaw",
      "other_entity": "left_shoulder_yaw_joint",
      "quantity": "force",
      "tolerance": "limit",
      "m": 18.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_shoulder_yaw",
      "other_entity": "left_shoulder_yaw_joint",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 20.0,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_elbow",
      "other_entity": "left_elbow_joint",
      "quantity": "force",
      "tolerance": "limit",
      "m": 18.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_elbow",
      "other_entity": "left_elbow_joint",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 20.0,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "right_shoulder_pitch",
      "other_entity": "right_shoulder_pitch_joint",
      "quantity": "force",
      "tolerance": "limit",
      "m": 40.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "right_shoulder_pitch",
      "other_entity": "right_shoulder_pitch_joint",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 9.0,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "right_shoulder_roll",
      "other_entity": "right_shoulder_roll_joint",
      "quantity": "force",
      "tolerance": "limit",
      "m": 40.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "right_shoulder_roll",
      "other_entity": "right_shoulder_roll_joint",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 9.0,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "right_shoulder_yaw",
      "other_entity": "right_shoulder_yaw_joint",
      "quantity": "force",
      "tolerance": "limit",
      "m": 18.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "right_shoulder_yaw",
      "other_entity": "right_shoulder_yaw_joint",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 20.0,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "right_elbow",
      "other_entity": "right_elbow_joint",
      "quantity": "force",
      "tolerance": "limit",
      "m": 18.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "right_elbow",
      "other_entity": "right_elbow_joint",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 20.0,
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
| left_hip_yaw / force | 200 | unavailable | unavailable |
| left_hip_yaw / velocity | unavailable | unavailable | 23 |
| left_hip_roll / force | 200 | unavailable | unavailable |
| left_hip_roll / velocity | unavailable | unavailable | 23 |
| left_hip_pitch / force | 200 | unavailable | unavailable |
| left_hip_pitch / velocity | unavailable | unavailable | 23 |
| left_knee / force | 300 | unavailable | unavailable |
| left_knee / velocity | unavailable | unavailable | 14 |
| left_ankle / force | 40 | unavailable | unavailable |
| left_ankle / velocity | unavailable | unavailable | 9 |
| right_hip_yaw / force | 200 | unavailable | unavailable |
| right_hip_yaw / velocity | unavailable | unavailable | 23 |
| right_hip_roll / force | 200 | unavailable | unavailable |
| right_hip_roll / velocity | unavailable | unavailable | 23 |
| right_hip_pitch / force | 200 | unavailable | unavailable |
| right_hip_pitch / velocity | unavailable | unavailable | 23 |
| right_knee / force | 300 | unavailable | unavailable |
| right_knee / velocity | unavailable | unavailable | 14 |
| right_ankle / force | 40 | unavailable | unavailable |
| right_ankle / velocity | unavailable | unavailable | 9 |
| torso / force | 200 | unavailable | unavailable |
| torso / velocity | unavailable | unavailable | 23 |
| left_shoulder_pitch / force | 40 | unavailable | unavailable |
| left_shoulder_pitch / velocity | unavailable | unavailable | 9 |
| left_shoulder_roll / force | 40 | unavailable | unavailable |
| left_shoulder_roll / velocity | unavailable | unavailable | 9 |
| left_shoulder_yaw / force | 18 | unavailable | unavailable |
| left_shoulder_yaw / velocity | unavailable | unavailable | 20 |
| left_elbow / force | 18 | unavailable | unavailable |
| left_elbow / velocity | unavailable | unavailable | 20 |
| right_shoulder_pitch / force | 40 | unavailable | unavailable |
| right_shoulder_pitch / velocity | unavailable | unavailable | 9 |
| right_shoulder_roll / force | 40 | unavailable | unavailable |
| right_shoulder_roll / velocity | unavailable | unavailable | 9 |
| right_shoulder_yaw / force | 18 | unavailable | unavailable |
| right_shoulder_yaw / velocity | unavailable | unavailable | 20 |
| right_elbow / force | 18 | unavailable | unavailable |
| right_elbow / velocity | unavailable | unavailable | 20 |
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
  "robots/h1_description/meshes/left_ankle_link.STL",
  "robots/h1_description/meshes/left_ankle_link.dae",
  "robots/h1_description/meshes/left_elbow_link.STL",
  "robots/h1_description/meshes/left_elbow_link.dae",
  "robots/h1_description/meshes/left_hip_pitch_link.STL",
  "robots/h1_description/meshes/left_hip_pitch_link.dae",
  "robots/h1_description/meshes/left_hip_roll_link.STL",
  "robots/h1_description/meshes/left_hip_roll_link.dae",
  "robots/h1_description/meshes/left_hip_yaw_link.STL",
  "robots/h1_description/meshes/left_hip_yaw_link.dae",
  "robots/h1_description/meshes/left_knee_link.STL",
  "robots/h1_description/meshes/left_knee_link.dae",
  "robots/h1_description/meshes/left_shoulder_pitch_link.STL",
  "robots/h1_description/meshes/left_shoulder_pitch_link.dae",
  "robots/h1_description/meshes/left_shoulder_roll_link.STL",
  "robots/h1_description/meshes/left_shoulder_roll_link.dae",
  "robots/h1_description/meshes/left_shoulder_yaw_link.STL",
  "robots/h1_description/meshes/left_shoulder_yaw_link.dae",
  "robots/h1_description/meshes/logo_link.STL",
  "robots/h1_description/meshes/logo_link.dae",
  "robots/h1_description/meshes/pelvis.STL",
  "robots/h1_description/meshes/pelvis.dae",
  "robots/h1_description/meshes/right_ankle_link.STL",
  "robots/h1_description/meshes/right_ankle_link.dae",
  "robots/h1_description/meshes/right_elbow_link.STL",
  "robots/h1_description/meshes/right_elbow_link.dae",
  "robots/h1_description/meshes/right_hip_pitch_link.STL",
  "robots/h1_description/meshes/right_hip_pitch_link.dae",
  "robots/h1_description/meshes/right_hip_roll_link.STL",
  "robots/h1_description/meshes/right_hip_roll_link.dae",
  "robots/h1_description/meshes/right_hip_yaw_link.STL",
  "robots/h1_description/meshes/right_hip_yaw_link.dae",
  "robots/h1_description/meshes/right_knee_link.STL",
  "robots/h1_description/meshes/right_knee_link.dae",
  "robots/h1_description/meshes/right_shoulder_pitch_link.STL",
  "robots/h1_description/meshes/right_shoulder_pitch_link.dae",
  "robots/h1_description/meshes/right_shoulder_roll_link.STL",
  "robots/h1_description/meshes/right_shoulder_roll_link.dae",
  "robots/h1_description/meshes/right_shoulder_yaw_link.STL",
  "robots/h1_description/meshes/right_shoulder_yaw_link.dae",
  "robots/h1_description/meshes/torso_link.STL",
  "robots/h1_description/meshes/torso_link.dae",
  "robots/h1_description/urdf/h1.urdf"
]
```

## Self comparisons

```json
[
  {
    "file": "unitree_h1/h1.xml",
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
      "NO MATCHING SOURCE": 67
    },
    "classifications_changed": 0,
    "finding_membership_changes": 0
  },
  "2": {
    "provenance_method": "none",
    "counts": {
      "NO MATCHING SOURCE": 67
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
      "unitree_h1/h1.xml"
    ],
    "registration": {
      "translation": [
        0.0,
        0.0,
        1.06
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
      "imu_link",
      "logo_link",
      "d435_left_imager_link",
      "d435_rgb_module_link",
      "mid360_link"
    ],
    "assets_loaded": 21,
    "mesh_conversions": [],
    "nonphysical_normalizations": [],
    "xacro_arguments": {},
    "source_dependencies": [
      "robots/h1_description/urdf/h1.urdf",
      "robots/h1_description/meshes/pelvis.STL",
      "robots/h1_description/meshes/left_hip_yaw_link.STL",
      "robots/h1_description/meshes/left_hip_roll_link.STL",
      "robots/h1_description/meshes/left_hip_pitch_link.STL",
      "robots/h1_description/meshes/left_knee_link.STL",
      "robots/h1_description/meshes/left_ankle_link.STL",
      "robots/h1_description/meshes/right_hip_yaw_link.STL",
      "robots/h1_description/meshes/right_hip_roll_link.STL",
      "robots/h1_description/meshes/right_hip_pitch_link.STL",
      "robots/h1_description/meshes/right_knee_link.STL",
      "robots/h1_description/meshes/right_ankle_link.STL",
      "robots/h1_description/meshes/torso_link.STL",
      "robots/h1_description/meshes/left_shoulder_pitch_link.STL",
      "robots/h1_description/meshes/left_shoulder_roll_link.STL",
      "robots/h1_description/meshes/left_shoulder_yaw_link.STL",
      "robots/h1_description/meshes/left_elbow_link.STL",
      "robots/h1_description/meshes/right_shoulder_pitch_link.STL",
      "robots/h1_description/meshes/right_shoulder_roll_link.STL",
      "robots/h1_description/meshes/right_shoulder_yaw_link.STL",
      "robots/h1_description/meshes/right_elbow_link.STL",
      "robots/h1_description/meshes/logo_link.STL"
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
  "historical_snapshots_reused": 11,
  "primary_physics_unchanged": true,
  "source_matching": "original raw-value provenance criteria retained; kinematic guard applies to reported CoM"
}
```

## H1 nine-revision acceptance

The Menagerie README states:

> The original URDF and assets were provided directly by [Unitree Robotics](https://www.unitree.com/) under a BSD-3-Clause License.

[README, exact revision and lines](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_h1/README.md#L13). The quote joins wrapped source lines; the linked README preserves the original Markdown.

Menagerie release: **2023-11-06**. Earliest public H1 revision: **2023-12-07**. Every compiled candidate fails the match criteria; no proxy is selected. In particular, Menagerie ankle masses are 0.446 kg, while the earliest source has 0.552448 kg and the closest later source has 0.474 kg. A total mass within tolerance does not establish a body-level match.

All differences below are **upstream revision minus Menagerie**. Masses are compiled with MuJoCo, including inferred sensor mass. Both leg subtrees are rooted at their hip-yaw body. Joint ranges show lower/upper endpoint differences in radians.

| Revision/date | Total kg (Δ) | Left leg kg (Δ) | Right leg kg (Δ) | Left hip-pitch range (Δ rad) | Right hip-pitch range (Δ rad) | Match? |
|---|---:|---:|---:|---|---|---|
| [e197ae1](https://github.com/unitreerobotics/unitree_ros/blob/e197ae10d301c41f17f61fe3a741925a033db1e8/robots/h1_description/urdf/h1.urdf#L1) / 2023-12-07 | 51.649896000 (+0.212896000) | 10.901448000 (+0.106448000) | 10.901448000 (+0.106448000) | [-1.57, 1.57] ([0, 0]) | [-1.57, 1.57] ([0, 0]) | no (17 quantities differ) |
| [1a3e648](https://github.com/unitreerobotics/unitree_ros/blob/1a3e6489c06f551090b3ad0e617d791b9b84a38a/robots/h1_description/urdf/h1.urdf#L1) / 2024-01-19 | 51.493000000 (+0.056000000) | 10.823000000 (+0.028000000) | 10.823000000 (+0.028000000) | [-1.57, 1.57] ([0, 0]) | [-1.57, 1.57] ([0, 0]) | no (11 quantities differ) |
| [39c9da3](https://github.com/unitreerobotics/unitree_ros/blob/39c9da3e6bd097747cd6a5881cb655e3438b5708/robots/h1_description/urdf/h1.urdf#L1) / 2024-01-22 | 51.493000000 (+0.056000000) | 10.823000000 (+0.028000000) | 10.823000000 (+0.028000000) | [-3.14, 2.53] ([-1.57, 0.96]) | [-3.14, 2.53] ([-1.57, 0.96]) | no (13 quantities differ) |
| [67ac212](https://github.com/unitreerobotics/unitree_ros/blob/67ac2124494e93af87d34d6e53ef9060dbf9c923/robots/h1_description/urdf/h1.urdf#L1) / 2024-02-01 | 51.601000000 (+0.164000000) | 10.823000000 (+0.028000000) | 10.823000000 (+0.028000000) | [-3.14, 2.53] ([-1.57, 0.96]) | [-3.14, 2.53] ([-1.57, 0.96]) | no (25 quantities differ) |
| [73be4a2](https://github.com/unitreerobotics/unitree_ros/blob/73be4a2b90dcc5639cc4e4997ba7732fa11b7672/robots/h1_description/urdf/h1.urdf#L1) / 2024-04-08 | 51.601012566 (+0.164012566) | 10.823000000 (+0.028000000) | 10.823000000 (+0.028000000) | [-3.14, 2.53] ([-1.57, 0.96]) | [-3.14, 2.53] ([-1.57, 0.96]) | no (25 quantities differ) |
| [fa16256](https://github.com/unitreerobotics/unitree_ros/blob/fa16256a76eae9565d8e17e9f4e5be2fb61a8807/robots/h1_description/urdf/h1.urdf#L1) / 2024-07-17 | 51.601012566 (+0.164012566) | 10.823000000 (+0.028000000) | 10.823000000 (+0.028000000) | [-3.14, 2.53] ([-1.57, 0.96]) | [-3.14, 2.53] ([-1.57, 0.96]) | no (25 quantities differ) |
| [a3b70ca](https://github.com/unitreerobotics/unitree_ros/blob/a3b70cae6fd4a82c0e1ece633d5c6f97e88c9d76/robots/h1_description/urdf/h1.urdf#L1) / 2025-06-19 | 51.601012566 (+0.164012566) | 10.823000000 (+0.028000000) | 10.823000000 (+0.028000000) | [-3.14, 2.53] ([-1.57, 0.96]) | [-3.14, 2.53] ([-1.57, 0.96]) | no (25 quantities differ) |
| [c4519eb](https://github.com/unitreerobotics/unitree_ros/blob/c4519eba87c5c2a959c53629c74d03f1ee9bc866/robots/h1_description/urdf/h1.urdf#L1) / 2025-12-09 | 55.001012566 (+3.564012566) | 10.823000000 (+0.028000000) | 10.823000000 (+0.028000000) | [-3.14, 2.53] ([-1.57, 0.96]) | [-3.14, 2.53] ([-1.57, 0.96]) | no (30 quantities differ) |
| [34e7506](https://github.com/unitreerobotics/unitree_ros/blob/34e7506c5333666f7c6dad6bfeeca2176cace70b/robots/h1_description/urdf/h1.urdf#L1) / 2025-12-31 | 59.338012566 (+7.901012566) | 14.182000000 (+3.387000000) | 14.182000000 (+3.387000000) | [-3.14, 2.53] ([-1.57, 0.96]) | [-3.14, 2.53] ([-1.57, 0.96]) | no (67 quantities differ) |

Acceptance: **passed**; model class **NO MATCHING SOURCE**. No candidate has been silently treated as the source. These discrepancies are excluded from STALE totals.
