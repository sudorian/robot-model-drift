# unitree_g1

Status: **complete**. Provenance: **dated match**, confidence **medium**.

Source selected using the ordered amended provenance rules.

M: `https://github.com/google-deepmind/mujoco_menagerie`, `unitree_g1/g1_with_hands.xml`, commit `370c43965323c0944b433b202aac5058b5f907a9`.
H: `https://github.com/unitreerobotics/unitree_ros`, `robots/g1_description/g1_29dof_with_hand_rev_1_0.xml`, commit `157ff950351e5f535e03c5d85a16b7d594b3dbcc`.
S: `adb48c7910ef8404ca34a07df95fc3acbb09f318` (2024-10-22T17:24:55+08:00). Menagerie release/change: 2024-12-10T14:34:36-08:00.

Limit semantics: MJCF effort values are supported actuator torque/force envelopes. URDF effort and velocity values are manufacturer declarations retained from XML; MuJoCo does not enforce those tags. Such declaration comparisons are explicitly distinct from compiled inertial/range quantities.


## Source evidence

```json
[
  {
    "url": "https://github.com/unitreerobotics/unitree_ros/blob/master/robots/g1_description/g1_29dof_rev_1_0.xml",
    "document": "unitree_g1/README.md",
    "commit": "370c43965323c0944b433b202aac5058b5f907a9",
    "current": true
  },
  {
    "url": "https://github.com/unitreerobotics/unitree_ros/blob/master/robots/g1_description",
    "document": "unitree_g1/README.md",
    "commit": "b5ff2e8666c2fa36fddd0961e5bd992726c1efc1",
    "current": false
  },
  {
    "url": "https://github.com/unitreerobotics/unitree_ros/blob/master/robots/g1_description/g1_29dof_with_hand_rev_1_0.xml",
    "document": "unitree_g1/README.md",
    "commit": "b5ff2e8666c2fa36fddd0961e5bd992726c1efc1",
    "current": false
  },
  {
    "url": "https://github.com/unitreerobotics/unitree_ros/tree/master/robots/g1_description",
    "document": "unitree_g1/README.md",
    "commit": "3d9225cc00d68a053fc74129ee609f4f9f760065",
    "current": false
  },
  {
    "url": "https://github.com/unitreerobotics/unitree_ros/blob/master/robots/g1_description",
    "document": "unitree_g1/CHANGELOG.md",
    "commit": "370c43965323c0944b433b202aac5058b5f907a9",
    "current": true
  },
  {
    "url": "https://github.com/unitreerobotics/unitree_ros/blob/master/robots/g1_description/g1_29dof_rev_1_0.xml",
    "document": "unitree_g1/CHANGELOG.md",
    "commit": "370c43965323c0944b433b202aac5058b5f907a9",
    "current": true
  },
  {
    "url": "https://github.com/unitreerobotics/unitree_ros/blob/master/robots/g1_description/g1_29dof_with_hand_rev_1_0.xml",
    "document": "unitree_g1/CHANGELOG.md",
    "commit": "370c43965323c0944b433b202aac5058b5f907a9",
    "current": true
  }
]
```


## Kinematics consistency

A proper Kabsch rigid transform aligns all matched zero-pose body origins. The maximum per-origin residual and signed hinge/slide axis angles determine whether CoM can be compared; RMS is also recorded. Fewer than three non-collinear origins give insufficient kinematic coverage. CoM records that fail either required M/H or M/S check are excluded from counts and largest discrepancies. Masses, principal moments and raw joint ranges remain unchanged; a flagged range still requires convention review.

| Pair | Status | Origins / rank | RMS / maximum mm | Disagreeing / checked axes |
|---|---|---:|---:|---:|
| M/H | consistent | 44 / 3 | 1.5173376e-13 / 3.57540738e-13 | 0 / 43 |
| M/S | consistent | 44 / 3 | 1.5173376e-13 / 3.57540738e-13 | 0 / 43 |

Exact fitted transforms, per-origin residuals, thresholds and axis vectors:

```json
{
  "M/H": {
    "status": "consistent",
    "matched_body_origins": 44,
    "position_threshold_m": 0.005,
    "axis_threshold_rad": 0.005,
    "residual_definition": "maximum Euclidean residual over matched body origins; Kabsch minimizes RMS, which is also recorded",
    "coordinate_frames": "each snapshot registered to its matched report anchor",
    "anchor_m": "pelvis",
    "anchor_other": "pelvis",
    "rotation_other_to_m": [
      [
        1.0000000000000004,
        9.425688003565556e-17,
        -4.1392684775774333e-17
      ],
      [
        -2.0373607146713636e-16,
        1.0000000000000002,
        1.6094913686332389e-16
      ],
      [
        -5.390435620009602e-17,
        -6.396792817664476e-18,
        1.0000000000000004
      ]
    ],
    "translation_other_to_m": [
      -5.551115123125783e-17,
      2.896725624667619e-17,
      1.734723475976807e-17
    ],
    "rms_residual_m": 1.5173376042280695e-16,
    "max_residual_m": 3.5754073794616016e-16,
    "fit_rank": 3,
    "axis_checks": [
      {
        "joint_m": "left_hip_pitch_joint",
        "joint_other": "left_hip_pitch_joint",
        "axis_m": [
          0.0,
          1.0,
          0.0
        ],
        "axis_other_aligned": [
          9.425688003565554e-17,
          1.0,
          -6.396792817664475e-18
        ],
        "angle_rad": 9.44736915358349e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "left_hip_roll_joint",
        "joint_other": "left_hip_roll_joint",
        "axis_m": [
          0.9847439475280368,
          0.0,
          0.17400964860288382
        ],
        "axis_other_aligned": [
          0.9847439475280368,
          -1.7262116052187758e-16,
          0.17400964860288376
        ],
        "angle_rad": 1.813271986518829e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "left_hip_yaw_joint",
        "joint_other": "left_hip_yaw_joint",
        "axis_m": [
          -0.17400964860288382,
          0.0,
          0.9847439475280368
        ],
        "axis_other_aligned": [
          -0.17400964860288384,
          1.9394573058974818e-16,
          0.9847439475280368
        ],
        "angle_rad": 1.959217149571381e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "left_knee_joint",
        "joint_other": "left_knee_joint",
        "axis_m": [
          0.0,
          1.0,
          0.0
        ],
        "axis_other_aligned": [
          9.425688003565554e-17,
          1.0,
          -6.396792817664475e-18
        ],
        "angle_rad": 9.44736915358349e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "left_ankle_pitch_joint",
        "joint_other": "left_ankle_pitch_joint",
        "axis_m": [
          0.0,
          1.0,
          0.0
        ],
        "axis_other_aligned": [
          9.425688003565554e-17,
          1.0,
          -6.396792817664475e-18
        ],
        "angle_rad": 9.44736915358349e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "left_ankle_roll_joint",
        "joint_other": "left_ankle_roll_joint",
        "axis_m": [
          1.0,
          0.0,
          -1.2005303483887466e-17
        ],
        "axis_other_aligned": [
          1.0,
          -2.0373607146713626e-16,
          -6.590965968398346e-17
        ],
        "angle_rad": 2.1074645058507838e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "right_hip_pitch_joint",
        "joint_other": "right_hip_pitch_joint",
        "axis_m": [
          0.0,
          1.0,
          0.0
        ],
        "axis_other_aligned": [
          9.425688003565554e-17,
          1.0,
          -6.396792817664475e-18
        ],
        "angle_rad": 9.44736915358349e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "right_hip_roll_joint",
        "joint_other": "right_hip_roll_joint",
        "axis_m": [
          0.9847439475280368,
          0.0,
          0.17400964860288382
        ],
        "axis_other_aligned": [
          0.9847439475280368,
          -1.7262116052187758e-16,
          0.17400964860288376
        ],
        "angle_rad": 1.813271986518829e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "right_hip_yaw_joint",
        "joint_other": "right_hip_yaw_joint",
        "axis_m": [
          -0.17400964860288382,
          0.0,
          0.9847439475280368
        ],
        "axis_other_aligned": [
          -0.17400964860288384,
          1.9394573058974818e-16,
          0.9847439475280368
        ],
        "angle_rad": 1.959217149571381e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "right_knee_joint",
        "joint_other": "right_knee_joint",
        "axis_m": [
          0.0,
          1.0,
          0.0
        ],
        "axis_other_aligned": [
          9.425688003565554e-17,
          1.0,
          -6.396792817664475e-18
        ],
        "angle_rad": 9.44736915358349e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "right_ankle_pitch_joint",
        "joint_other": "right_ankle_pitch_joint",
        "axis_m": [
          0.0,
          1.0,
          0.0
        ],
        "axis_other_aligned": [
          9.425688003565554e-17,
          1.0,
          -6.396792817664475e-18
        ],
        "angle_rad": 9.44736915358349e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "right_ankle_roll_joint",
        "joint_other": "right_ankle_roll_joint",
        "axis_m": [
          1.0,
          0.0,
          -1.2005303483887466e-17
        ],
        "axis_other_aligned": [
          1.0,
          -2.0373607146713626e-16,
          -6.590965968398346e-17
        ],
        "angle_rad": 2.1074645058507838e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "waist_yaw_joint",
        "joint_other": "waist_yaw_joint",
        "axis_m": [
          0.0,
          0.0,
          1.0
        ],
        "axis_other_aligned": [
          -4.1392684775774315e-17,
          1.6094913686332381e-16,
          1.0
        ],
        "angle_rad": 1.6618657891055932e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "waist_roll_joint",
        "joint_other": "waist_roll_joint",
        "axis_m": [
          1.0,
          0.0,
          0.0
        ],
        "axis_other_aligned": [
          1.0,
          -2.0373607146713626e-16,
          -5.3904356200095996e-17
        ],
        "angle_rad": 2.1074645058507838e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "waist_pitch_joint",
        "joint_other": "waist_pitch_joint",
        "axis_m": [
          0.0,
          1.0,
          0.0
        ],
        "axis_other_aligned": [
          9.425688003565554e-17,
          1.0,
          -6.396792817664475e-18
        ],
        "angle_rad": 9.44736915358349e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "left_shoulder_pitch_joint",
        "joint_other": "left_shoulder_pitch_joint",
        "axis_m": [
          0.00019931407505568427,
          0.9612461327923458,
          0.27569155312714855
        ],
        "axis_other_aligned": [
          0.0001993140750557635,
          0.9612461327923458,
          0.2756915531271486
        ],
        "angle_rad": 9.674353303540759e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "left_shoulder_roll_joint",
        "joint_other": "left_shoulder_roll_joint",
        "axis_m": [
          0.9999999801369496,
          -0.0001915899764289088,
          -5.494889850922211e-05
        ],
        "axis_other_aligned": [
          0.9999999801369496,
          -0.00019158997642911252,
          -5.494889850927602e-05
        ],
        "angle_rad": 2.1073265903852135e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "left_shoulder_yaw_joint",
        "joint_other": "left_shoulder_yaw_joint",
        "axis_m": [
          5.493768102472281e-05,
          -5.8554204231390726e-05,
          0.9999999967766282
        ],
        "axis_other_aligned": [
          5.493768102468141e-05,
          -5.8554204231229776e-05,
          0.9999999967766282
        ],
        "angle_rad": 1.6618810751928158e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "left_elbow_joint",
        "joint_other": "left_elbow_joint",
        "axis_m": [
          0.00019159319330036868,
          0.9999999799323429,
          5.854367755931303e-05
        ],
        "axis_other_aligned": [
          0.00019159319330046292,
          0.9999999799323428,
          5.8543677559306626e-05
        ],
        "angle_rad": 9.448815736960099e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "left_wrist_roll_joint",
        "joint_other": "left_wrist_roll_joint",
        "axis_m": [
          0.9999999801369496,
          -0.0001915899764289088,
          -5.494889850922211e-05
        ],
        "axis_other_aligned": [
          0.9999999801369496,
          -0.00019158997642911252,
          -5.494889850927602e-05
        ],
        "angle_rad": 2.1073265903852135e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "left_wrist_pitch_joint",
        "joint_other": "left_wrist_pitch_joint",
        "axis_m": [
          0.00019159319330036868,
          0.9999999799323429,
          5.854367755931303e-05
        ],
        "axis_other_aligned": [
          0.00019159319330046292,
          0.9999999799323428,
          5.8543677559306626e-05
        ],
        "angle_rad": 9.448815736960099e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "left_wrist_yaw_joint",
        "joint_other": "left_wrist_yaw_joint",
        "axis_m": [
          5.493768102472281e-05,
          -5.8554204231390726e-05,
          0.9999999967766282
        ],
        "axis_other_aligned": [
          5.493768102468141e-05,
          -5.8554204231229776e-05,
          0.9999999967766282
        ],
        "angle_rad": 1.6618810751928158e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "left_hand_thumb_0_joint",
        "joint_other": "left_hand_thumb_0_joint",
        "axis_m": [
          0.00019159319330036868,
          0.9999999799323429,
          5.854367755931303e-05
        ],
        "axis_other_aligned": [
          0.00019159319330046292,
          0.9999999799323428,
          5.8543677559306626e-05
        ],
        "angle_rad": 9.448815736960099e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "left_hand_thumb_1_joint",
        "joint_other": "left_hand_thumb_1_joint",
        "axis_m": [
          5.493768102472281e-05,
          -5.8554204231390726e-05,
          0.9999999967766282
        ],
        "axis_other_aligned": [
          5.493768102468141e-05,
          -5.8554204231229776e-05,
          0.9999999967766282
        ],
        "angle_rad": 1.6618810751928158e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "left_hand_thumb_2_joint",
        "joint_other": "left_hand_thumb_2_joint",
        "axis_m": [
          5.493768102472281e-05,
          -5.8554204231390726e-05,
          0.9999999967766282
        ],
        "axis_other_aligned": [
          5.493768102468141e-05,
          -5.8554204231229776e-05,
          0.9999999967766282
        ],
        "angle_rad": 1.6618810751928158e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "left_hand_middle_0_joint",
        "joint_other": "left_hand_middle_0_joint",
        "axis_m": [
          5.493768102472281e-05,
          -5.8554204231390726e-05,
          0.9999999967766282
        ],
        "axis_other_aligned": [
          5.493768102468141e-05,
          -5.8554204231229776e-05,
          0.9999999967766282
        ],
        "angle_rad": 1.6618810751928158e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "left_hand_middle_1_joint",
        "joint_other": "left_hand_middle_1_joint",
        "axis_m": [
          5.493768102472281e-05,
          -5.8554204231390726e-05,
          0.9999999967766282
        ],
        "axis_other_aligned": [
          5.493768102468141e-05,
          -5.8554204231229776e-05,
          0.9999999967766282
        ],
        "angle_rad": 1.6618810751928158e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "left_hand_index_0_joint",
        "joint_other": "left_hand_index_0_joint",
        "axis_m": [
          5.493768102472281e-05,
          -5.8554204231390726e-05,
          0.9999999967766282
        ],
        "axis_other_aligned": [
          5.493768102468141e-05,
          -5.8554204231229776e-05,
          0.9999999967766282
        ],
        "angle_rad": 1.6618810751928158e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "left_hand_index_1_joint",
        "joint_other": "left_hand_index_1_joint",
        "axis_m": [
          5.493768102472281e-05,
          -5.8554204231390726e-05,
          0.9999999967766282
        ],
        "axis_other_aligned": [
          5.493768102468141e-05,
          -5.8554204231229776e-05,
          0.9999999967766282
        ],
        "angle_rad": 1.6618810751928158e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "right_shoulder_pitch_joint",
        "joint_other": "right_shoulder_pitch_joint",
        "axis_m": [
          -0.00019931407505568427,
          0.9612461327923458,
          -0.27569155312714855
        ],
        "axis_other_aligned": [
          -0.00019931407505558227,
          0.9612461327923458,
          -0.2756915531271486
        ],
        "angle_rad": 1.161220451667229e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "right_shoulder_roll_joint",
        "joint_other": "right_shoulder_roll_joint",
        "axis_m": [
          0.9999999801369496,
          0.0001915899764289088,
          -5.494889850922211e-05
        ],
        "axis_other_aligned": [
          0.9999999801369496,
          0.00019158997642870502,
          -5.494889850927602e-05
        ],
        "angle_rad": 2.1078506713143388e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "right_shoulder_yaw_joint",
        "joint_other": "right_shoulder_yaw_joint",
        "axis_m": [
          5.493768102472281e-05,
          5.8554204231390726e-05,
          0.9999999967766282
        ],
        "axis_other_aligned": [
          5.4937681024681424e-05,
          5.855420423155165e-05,
          0.9999999967766282
        ],
        "angle_rad": 1.6615848137232817e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "right_elbow_joint",
        "joint_other": "right_elbow_joint",
        "axis_m": [
          -0.00019159319330036868,
          0.9999999799323429,
          -5.854367755931303e-05
        ],
        "axis_other_aligned": [
          -0.00019159319330027443,
          0.9999999799323428,
          -5.854367755931942e-05
        ],
        "angle_rad": 9.443407170303172e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "right_wrist_roll_joint",
        "joint_other": "right_wrist_roll_joint",
        "axis_m": [
          0.9999999801369496,
          0.0001915899764289088,
          -5.494889850922211e-05
        ],
        "axis_other_aligned": [
          0.9999999801369496,
          0.00019158997642870502,
          -5.494889850927602e-05
        ],
        "angle_rad": 2.1078506713143388e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "right_wrist_pitch_joint",
        "joint_other": "right_wrist_pitch_joint",
        "axis_m": [
          -0.00019159319330036868,
          0.9999999799323429,
          -5.854367755931303e-05
        ],
        "axis_other_aligned": [
          -0.00019159319330027443,
          0.9999999799323428,
          -5.854367755931942e-05
        ],
        "angle_rad": 9.443407170303172e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "right_wrist_yaw_joint",
        "joint_other": "right_wrist_yaw_joint",
        "axis_m": [
          5.493768102472281e-05,
          5.8554204231390726e-05,
          0.9999999967766282
        ],
        "axis_other_aligned": [
          5.4937681024681424e-05,
          5.855420423155165e-05,
          0.9999999967766282
        ],
        "angle_rad": 1.6615848137232817e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "right_hand_thumb_0_joint",
        "joint_other": "right_hand_thumb_0_joint",
        "axis_m": [
          -0.00019159319330036868,
          0.9999999799323429,
          -5.854367755931303e-05
        ],
        "axis_other_aligned": [
          -0.00019159319330027443,
          0.9999999799323428,
          -5.854367755931942e-05
        ],
        "angle_rad": 9.443407170303172e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "right_hand_thumb_1_joint",
        "joint_other": "right_hand_thumb_1_joint",
        "axis_m": [
          5.493768102472281e-05,
          5.8554204231390726e-05,
          0.9999999967766282
        ],
        "axis_other_aligned": [
          5.4937681024681424e-05,
          5.855420423155165e-05,
          0.9999999967766282
        ],
        "angle_rad": 1.6615848137232817e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "right_hand_thumb_2_joint",
        "joint_other": "right_hand_thumb_2_joint",
        "axis_m": [
          5.493768102472281e-05,
          5.8554204231390726e-05,
          0.9999999967766282
        ],
        "axis_other_aligned": [
          5.4937681024681424e-05,
          5.855420423155165e-05,
          0.9999999967766282
        ],
        "angle_rad": 1.6615848137232817e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "right_hand_middle_0_joint",
        "joint_other": "right_hand_middle_0_joint",
        "axis_m": [
          5.493768102472281e-05,
          5.8554204231390726e-05,
          0.9999999967766282
        ],
        "axis_other_aligned": [
          5.4937681024681424e-05,
          5.855420423155165e-05,
          0.9999999967766282
        ],
        "angle_rad": 1.6615848137232817e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "right_hand_middle_1_joint",
        "joint_other": "right_hand_middle_1_joint",
        "axis_m": [
          5.493768102472281e-05,
          5.8554204231390726e-05,
          0.9999999967766282
        ],
        "axis_other_aligned": [
          5.4937681024681424e-05,
          5.855420423155165e-05,
          0.9999999967766282
        ],
        "angle_rad": 1.6615848137232817e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "right_hand_index_0_joint",
        "joint_other": "right_hand_index_0_joint",
        "axis_m": [
          5.493768102472281e-05,
          5.8554204231390726e-05,
          0.9999999967766282
        ],
        "axis_other_aligned": [
          5.4937681024681424e-05,
          5.855420423155165e-05,
          0.9999999967766282
        ],
        "angle_rad": 1.6615848137232817e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "right_hand_index_1_joint",
        "joint_other": "right_hand_index_1_joint",
        "axis_m": [
          5.493768102472281e-05,
          5.8554204231390726e-05,
          0.9999999967766282
        ],
        "axis_other_aligned": [
          5.4937681024681424e-05,
          5.855420423155165e-05,
          0.9999999967766282
        ],
        "angle_rad": 1.6615848137232817e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      }
    ],
    "axis_disagreements": [],
    "com_eligible": true,
    "covariance_singular_values": [
      3.5415313610133516,
      0.7198400847771237,
      0.709103202902268
    ],
    "origin_residuals_m": {
      "pelvis": 6.497319754553167e-17,
      "left_hip_pitch_link": 5.985344798713177e-17,
      "left_hip_roll_link": 5.534902401705332e-17,
      "left_hip_yaw_link": 1.1188630228279524e-16,
      "left_knee_link": 2.2400932806813643e-16,
      "left_ankle_pitch_link": 3.404954766261228e-16,
      "left_ankle_roll_link": 3.404669249313444e-16,
      "right_hip_pitch_link": 6.370002625926186e-17,
      "right_hip_roll_link": 7.251727474114698e-17,
      "right_hip_yaw_link": 1.3092278833360675e-16,
      "right_knee_link": 2.3763754973844197e-16,
      "right_ankle_pitch_link": 3.5754073794616016e-16,
      "right_ankle_roll_link": 3.574681308336489e-16,
      "waist_yaw_link": 6.497319754553167e-17,
      "waist_roll_link": 8.105832119307043e-17,
      "torso_link": 8.105832119307043e-17,
      "left_shoulder_pitch_link": 1.5856858822415465e-16,
      "left_shoulder_roll_link": 1.661085354955402e-16,
      "left_shoulder_yaw_link": 1.4729633594786414e-16,
      "left_elbow_link": 1.0710424936134174e-16,
      "left_wrist_roll_link": 7.97218214573518e-17,
      "left_wrist_pitch_link": 7.473417450352271e-17,
      "left_wrist_yaw_link": 8.886119947416683e-17,
      "left_hand_thumb_0_link": 7.473417450352271e-17,
      "left_hand_thumb_1_link": 7.473417450352271e-17,
      "left_hand_thumb_2_link": 7.076311083754595e-17,
      "left_hand_middle_0_link": 1.1443916996305594e-16,
      "left_hand_middle_1_link": 1.1443916996305594e-16,
      "left_hand_index_0_link": 1.2719202621569003e-16,
      "left_hand_index_1_link": 1.2177709378935645e-16,
      "right_shoulder_pitch_link": 1.4140045113229895e-16,
      "right_shoulder_roll_link": 1.480645733181173e-16,
      "right_shoulder_yaw_link": 1.379538079060927e-16,
      "right_elbow_link": 9.053860682492399e-17,
      "right_wrist_roll_link": 5.721958498152797e-17,
      "right_wrist_pitch_link": 6.206335383118183e-17,
      "right_wrist_yaw_link": 5.003707553108401e-17,
      "right_hand_thumb_0_link": 7.473417450352271e-17,
      "right_hand_thumb_1_link": 7.473417450352271e-17,
      "right_hand_thumb_2_link": 7.473417450352271e-17,
      "right_hand_middle_0_link": 1.415262216750919e-16,
      "right_hand_middle_1_link": 1.415262216750919e-16,
      "right_hand_index_0_link": 1.3597399555105182e-16,
      "right_hand_index_1_link": 1.3597399555105182e-16
    },
    "reason": "Unique proper rigid fit and matched signed axes meet the configured thresholds"
  },
  "M/S": {
    "status": "consistent",
    "matched_body_origins": 44,
    "position_threshold_m": 0.005,
    "axis_threshold_rad": 0.005,
    "residual_definition": "maximum Euclidean residual over matched body origins; Kabsch minimizes RMS, which is also recorded",
    "coordinate_frames": "each snapshot registered to its matched report anchor",
    "anchor_m": "pelvis",
    "anchor_other": "pelvis",
    "rotation_other_to_m": [
      [
        1.0000000000000004,
        9.425688003565556e-17,
        -4.1392684775774333e-17
      ],
      [
        -2.0373607146713636e-16,
        1.0000000000000002,
        1.6094913686332389e-16
      ],
      [
        -5.390435620009602e-17,
        -6.396792817664476e-18,
        1.0000000000000004
      ]
    ],
    "translation_other_to_m": [
      -5.551115123125783e-17,
      2.896725624667619e-17,
      1.734723475976807e-17
    ],
    "rms_residual_m": 1.5173376042280695e-16,
    "max_residual_m": 3.5754073794616016e-16,
    "fit_rank": 3,
    "axis_checks": [
      {
        "joint_m": "left_hip_pitch_joint",
        "joint_other": "left_hip_pitch_joint",
        "axis_m": [
          0.0,
          1.0,
          0.0
        ],
        "axis_other_aligned": [
          9.425688003565554e-17,
          1.0,
          -6.396792817664475e-18
        ],
        "angle_rad": 9.44736915358349e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "left_hip_roll_joint",
        "joint_other": "left_hip_roll_joint",
        "axis_m": [
          0.9847439475280368,
          0.0,
          0.17400964860288382
        ],
        "axis_other_aligned": [
          0.9847439475280368,
          -1.7262116052187758e-16,
          0.17400964860288376
        ],
        "angle_rad": 1.813271986518829e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "left_hip_yaw_joint",
        "joint_other": "left_hip_yaw_joint",
        "axis_m": [
          -0.17400964860288382,
          0.0,
          0.9847439475280368
        ],
        "axis_other_aligned": [
          -0.17400964860288384,
          1.9394573058974818e-16,
          0.9847439475280368
        ],
        "angle_rad": 1.959217149571381e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "left_knee_joint",
        "joint_other": "left_knee_joint",
        "axis_m": [
          0.0,
          1.0,
          0.0
        ],
        "axis_other_aligned": [
          9.425688003565554e-17,
          1.0,
          -6.396792817664475e-18
        ],
        "angle_rad": 9.44736915358349e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "left_ankle_pitch_joint",
        "joint_other": "left_ankle_pitch_joint",
        "axis_m": [
          0.0,
          1.0,
          0.0
        ],
        "axis_other_aligned": [
          9.425688003565554e-17,
          1.0,
          -6.396792817664475e-18
        ],
        "angle_rad": 9.44736915358349e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "left_ankle_roll_joint",
        "joint_other": "left_ankle_roll_joint",
        "axis_m": [
          1.0,
          0.0,
          -1.2005303483887466e-17
        ],
        "axis_other_aligned": [
          1.0,
          -2.0373607146713626e-16,
          -6.590965968398346e-17
        ],
        "angle_rad": 2.1074645058507838e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "right_hip_pitch_joint",
        "joint_other": "right_hip_pitch_joint",
        "axis_m": [
          0.0,
          1.0,
          0.0
        ],
        "axis_other_aligned": [
          9.425688003565554e-17,
          1.0,
          -6.396792817664475e-18
        ],
        "angle_rad": 9.44736915358349e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "right_hip_roll_joint",
        "joint_other": "right_hip_roll_joint",
        "axis_m": [
          0.9847439475280368,
          0.0,
          0.17400964860288382
        ],
        "axis_other_aligned": [
          0.9847439475280368,
          -1.7262116052187758e-16,
          0.17400964860288376
        ],
        "angle_rad": 1.813271986518829e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "right_hip_yaw_joint",
        "joint_other": "right_hip_yaw_joint",
        "axis_m": [
          -0.17400964860288382,
          0.0,
          0.9847439475280368
        ],
        "axis_other_aligned": [
          -0.17400964860288384,
          1.9394573058974818e-16,
          0.9847439475280368
        ],
        "angle_rad": 1.959217149571381e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "right_knee_joint",
        "joint_other": "right_knee_joint",
        "axis_m": [
          0.0,
          1.0,
          0.0
        ],
        "axis_other_aligned": [
          9.425688003565554e-17,
          1.0,
          -6.396792817664475e-18
        ],
        "angle_rad": 9.44736915358349e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "right_ankle_pitch_joint",
        "joint_other": "right_ankle_pitch_joint",
        "axis_m": [
          0.0,
          1.0,
          0.0
        ],
        "axis_other_aligned": [
          9.425688003565554e-17,
          1.0,
          -6.396792817664475e-18
        ],
        "angle_rad": 9.44736915358349e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "right_ankle_roll_joint",
        "joint_other": "right_ankle_roll_joint",
        "axis_m": [
          1.0,
          0.0,
          -1.2005303483887466e-17
        ],
        "axis_other_aligned": [
          1.0,
          -2.0373607146713626e-16,
          -6.590965968398346e-17
        ],
        "angle_rad": 2.1074645058507838e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "waist_yaw_joint",
        "joint_other": "waist_yaw_joint",
        "axis_m": [
          0.0,
          0.0,
          1.0
        ],
        "axis_other_aligned": [
          -4.1392684775774315e-17,
          1.6094913686332381e-16,
          1.0
        ],
        "angle_rad": 1.6618657891055932e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "waist_roll_joint",
        "joint_other": "waist_roll_joint",
        "axis_m": [
          1.0,
          0.0,
          0.0
        ],
        "axis_other_aligned": [
          1.0,
          -2.0373607146713626e-16,
          -5.3904356200095996e-17
        ],
        "angle_rad": 2.1074645058507838e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "waist_pitch_joint",
        "joint_other": "waist_pitch_joint",
        "axis_m": [
          0.0,
          1.0,
          0.0
        ],
        "axis_other_aligned": [
          9.425688003565554e-17,
          1.0,
          -6.396792817664475e-18
        ],
        "angle_rad": 9.44736915358349e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "left_shoulder_pitch_joint",
        "joint_other": "left_shoulder_pitch_joint",
        "axis_m": [
          0.00019931407505568427,
          0.9612461327923458,
          0.27569155312714855
        ],
        "axis_other_aligned": [
          0.0001993140750557635,
          0.9612461327923458,
          0.2756915531271486
        ],
        "angle_rad": 9.674353303540759e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "left_shoulder_roll_joint",
        "joint_other": "left_shoulder_roll_joint",
        "axis_m": [
          0.9999999801369496,
          -0.0001915899764289088,
          -5.494889850922211e-05
        ],
        "axis_other_aligned": [
          0.9999999801369496,
          -0.00019158997642911252,
          -5.494889850927602e-05
        ],
        "angle_rad": 2.1073265903852135e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "left_shoulder_yaw_joint",
        "joint_other": "left_shoulder_yaw_joint",
        "axis_m": [
          5.493768102472281e-05,
          -5.8554204231390726e-05,
          0.9999999967766282
        ],
        "axis_other_aligned": [
          5.493768102468141e-05,
          -5.8554204231229776e-05,
          0.9999999967766282
        ],
        "angle_rad": 1.6618810751928158e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "left_elbow_joint",
        "joint_other": "left_elbow_joint",
        "axis_m": [
          0.00019159319330036868,
          0.9999999799323429,
          5.854367755931303e-05
        ],
        "axis_other_aligned": [
          0.00019159319330046292,
          0.9999999799323428,
          5.8543677559306626e-05
        ],
        "angle_rad": 9.448815736960099e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "left_wrist_roll_joint",
        "joint_other": "left_wrist_roll_joint",
        "axis_m": [
          0.9999999801369496,
          -0.0001915899764289088,
          -5.494889850922211e-05
        ],
        "axis_other_aligned": [
          0.9999999801369496,
          -0.00019158997642911252,
          -5.494889850927602e-05
        ],
        "angle_rad": 2.1073265903852135e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "left_wrist_pitch_joint",
        "joint_other": "left_wrist_pitch_joint",
        "axis_m": [
          0.00019159319330036868,
          0.9999999799323429,
          5.854367755931303e-05
        ],
        "axis_other_aligned": [
          0.00019159319330046292,
          0.9999999799323428,
          5.8543677559306626e-05
        ],
        "angle_rad": 9.448815736960099e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "left_wrist_yaw_joint",
        "joint_other": "left_wrist_yaw_joint",
        "axis_m": [
          5.493768102472281e-05,
          -5.8554204231390726e-05,
          0.9999999967766282
        ],
        "axis_other_aligned": [
          5.493768102468141e-05,
          -5.8554204231229776e-05,
          0.9999999967766282
        ],
        "angle_rad": 1.6618810751928158e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "left_hand_thumb_0_joint",
        "joint_other": "left_hand_thumb_0_joint",
        "axis_m": [
          0.00019159319330036868,
          0.9999999799323429,
          5.854367755931303e-05
        ],
        "axis_other_aligned": [
          0.00019159319330046292,
          0.9999999799323428,
          5.8543677559306626e-05
        ],
        "angle_rad": 9.448815736960099e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "left_hand_thumb_1_joint",
        "joint_other": "left_hand_thumb_1_joint",
        "axis_m": [
          5.493768102472281e-05,
          -5.8554204231390726e-05,
          0.9999999967766282
        ],
        "axis_other_aligned": [
          5.493768102468141e-05,
          -5.8554204231229776e-05,
          0.9999999967766282
        ],
        "angle_rad": 1.6618810751928158e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "left_hand_thumb_2_joint",
        "joint_other": "left_hand_thumb_2_joint",
        "axis_m": [
          5.493768102472281e-05,
          -5.8554204231390726e-05,
          0.9999999967766282
        ],
        "axis_other_aligned": [
          5.493768102468141e-05,
          -5.8554204231229776e-05,
          0.9999999967766282
        ],
        "angle_rad": 1.6618810751928158e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "left_hand_middle_0_joint",
        "joint_other": "left_hand_middle_0_joint",
        "axis_m": [
          5.493768102472281e-05,
          -5.8554204231390726e-05,
          0.9999999967766282
        ],
        "axis_other_aligned": [
          5.493768102468141e-05,
          -5.8554204231229776e-05,
          0.9999999967766282
        ],
        "angle_rad": 1.6618810751928158e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "left_hand_middle_1_joint",
        "joint_other": "left_hand_middle_1_joint",
        "axis_m": [
          5.493768102472281e-05,
          -5.8554204231390726e-05,
          0.9999999967766282
        ],
        "axis_other_aligned": [
          5.493768102468141e-05,
          -5.8554204231229776e-05,
          0.9999999967766282
        ],
        "angle_rad": 1.6618810751928158e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "left_hand_index_0_joint",
        "joint_other": "left_hand_index_0_joint",
        "axis_m": [
          5.493768102472281e-05,
          -5.8554204231390726e-05,
          0.9999999967766282
        ],
        "axis_other_aligned": [
          5.493768102468141e-05,
          -5.8554204231229776e-05,
          0.9999999967766282
        ],
        "angle_rad": 1.6618810751928158e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "left_hand_index_1_joint",
        "joint_other": "left_hand_index_1_joint",
        "axis_m": [
          5.493768102472281e-05,
          -5.8554204231390726e-05,
          0.9999999967766282
        ],
        "axis_other_aligned": [
          5.493768102468141e-05,
          -5.8554204231229776e-05,
          0.9999999967766282
        ],
        "angle_rad": 1.6618810751928158e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "right_shoulder_pitch_joint",
        "joint_other": "right_shoulder_pitch_joint",
        "axis_m": [
          -0.00019931407505568427,
          0.9612461327923458,
          -0.27569155312714855
        ],
        "axis_other_aligned": [
          -0.00019931407505558227,
          0.9612461327923458,
          -0.2756915531271486
        ],
        "angle_rad": 1.161220451667229e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "right_shoulder_roll_joint",
        "joint_other": "right_shoulder_roll_joint",
        "axis_m": [
          0.9999999801369496,
          0.0001915899764289088,
          -5.494889850922211e-05
        ],
        "axis_other_aligned": [
          0.9999999801369496,
          0.00019158997642870502,
          -5.494889850927602e-05
        ],
        "angle_rad": 2.1078506713143388e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "right_shoulder_yaw_joint",
        "joint_other": "right_shoulder_yaw_joint",
        "axis_m": [
          5.493768102472281e-05,
          5.8554204231390726e-05,
          0.9999999967766282
        ],
        "axis_other_aligned": [
          5.4937681024681424e-05,
          5.855420423155165e-05,
          0.9999999967766282
        ],
        "angle_rad": 1.6615848137232817e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "right_elbow_joint",
        "joint_other": "right_elbow_joint",
        "axis_m": [
          -0.00019159319330036868,
          0.9999999799323429,
          -5.854367755931303e-05
        ],
        "axis_other_aligned": [
          -0.00019159319330027443,
          0.9999999799323428,
          -5.854367755931942e-05
        ],
        "angle_rad": 9.443407170303172e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "right_wrist_roll_joint",
        "joint_other": "right_wrist_roll_joint",
        "axis_m": [
          0.9999999801369496,
          0.0001915899764289088,
          -5.494889850922211e-05
        ],
        "axis_other_aligned": [
          0.9999999801369496,
          0.00019158997642870502,
          -5.494889850927602e-05
        ],
        "angle_rad": 2.1078506713143388e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "right_wrist_pitch_joint",
        "joint_other": "right_wrist_pitch_joint",
        "axis_m": [
          -0.00019159319330036868,
          0.9999999799323429,
          -5.854367755931303e-05
        ],
        "axis_other_aligned": [
          -0.00019159319330027443,
          0.9999999799323428,
          -5.854367755931942e-05
        ],
        "angle_rad": 9.443407170303172e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "right_wrist_yaw_joint",
        "joint_other": "right_wrist_yaw_joint",
        "axis_m": [
          5.493768102472281e-05,
          5.8554204231390726e-05,
          0.9999999967766282
        ],
        "axis_other_aligned": [
          5.4937681024681424e-05,
          5.855420423155165e-05,
          0.9999999967766282
        ],
        "angle_rad": 1.6615848137232817e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "right_hand_thumb_0_joint",
        "joint_other": "right_hand_thumb_0_joint",
        "axis_m": [
          -0.00019159319330036868,
          0.9999999799323429,
          -5.854367755931303e-05
        ],
        "axis_other_aligned": [
          -0.00019159319330027443,
          0.9999999799323428,
          -5.854367755931942e-05
        ],
        "angle_rad": 9.443407170303172e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "right_hand_thumb_1_joint",
        "joint_other": "right_hand_thumb_1_joint",
        "axis_m": [
          5.493768102472281e-05,
          5.8554204231390726e-05,
          0.9999999967766282
        ],
        "axis_other_aligned": [
          5.4937681024681424e-05,
          5.855420423155165e-05,
          0.9999999967766282
        ],
        "angle_rad": 1.6615848137232817e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "right_hand_thumb_2_joint",
        "joint_other": "right_hand_thumb_2_joint",
        "axis_m": [
          5.493768102472281e-05,
          5.8554204231390726e-05,
          0.9999999967766282
        ],
        "axis_other_aligned": [
          5.4937681024681424e-05,
          5.855420423155165e-05,
          0.9999999967766282
        ],
        "angle_rad": 1.6615848137232817e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "right_hand_middle_0_joint",
        "joint_other": "right_hand_middle_0_joint",
        "axis_m": [
          5.493768102472281e-05,
          5.8554204231390726e-05,
          0.9999999967766282
        ],
        "axis_other_aligned": [
          5.4937681024681424e-05,
          5.855420423155165e-05,
          0.9999999967766282
        ],
        "angle_rad": 1.6615848137232817e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "right_hand_middle_1_joint",
        "joint_other": "right_hand_middle_1_joint",
        "axis_m": [
          5.493768102472281e-05,
          5.8554204231390726e-05,
          0.9999999967766282
        ],
        "axis_other_aligned": [
          5.4937681024681424e-05,
          5.855420423155165e-05,
          0.9999999967766282
        ],
        "angle_rad": 1.6615848137232817e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "right_hand_index_0_joint",
        "joint_other": "right_hand_index_0_joint",
        "axis_m": [
          5.493768102472281e-05,
          5.8554204231390726e-05,
          0.9999999967766282
        ],
        "axis_other_aligned": [
          5.4937681024681424e-05,
          5.855420423155165e-05,
          0.9999999967766282
        ],
        "angle_rad": 1.6615848137232817e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "right_hand_index_1_joint",
        "joint_other": "right_hand_index_1_joint",
        "axis_m": [
          5.493768102472281e-05,
          5.8554204231390726e-05,
          0.9999999967766282
        ],
        "axis_other_aligned": [
          5.4937681024681424e-05,
          5.855420423155165e-05,
          0.9999999967766282
        ],
        "angle_rad": 1.6615848137232817e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      }
    ],
    "axis_disagreements": [],
    "com_eligible": true,
    "covariance_singular_values": [
      3.5415313610133516,
      0.7198400847771237,
      0.709103202902268
    ],
    "origin_residuals_m": {
      "pelvis": 6.497319754553167e-17,
      "left_hip_pitch_link": 5.985344798713177e-17,
      "left_hip_roll_link": 5.534902401705332e-17,
      "left_hip_yaw_link": 1.1188630228279524e-16,
      "left_knee_link": 2.2400932806813643e-16,
      "left_ankle_pitch_link": 3.404954766261228e-16,
      "left_ankle_roll_link": 3.404669249313444e-16,
      "right_hip_pitch_link": 6.370002625926186e-17,
      "right_hip_roll_link": 7.251727474114698e-17,
      "right_hip_yaw_link": 1.3092278833360675e-16,
      "right_knee_link": 2.3763754973844197e-16,
      "right_ankle_pitch_link": 3.5754073794616016e-16,
      "right_ankle_roll_link": 3.574681308336489e-16,
      "waist_yaw_link": 6.497319754553167e-17,
      "waist_roll_link": 8.105832119307043e-17,
      "torso_link": 8.105832119307043e-17,
      "left_shoulder_pitch_link": 1.5856858822415465e-16,
      "left_shoulder_roll_link": 1.661085354955402e-16,
      "left_shoulder_yaw_link": 1.4729633594786414e-16,
      "left_elbow_link": 1.0710424936134174e-16,
      "left_wrist_roll_link": 7.97218214573518e-17,
      "left_wrist_pitch_link": 7.473417450352271e-17,
      "left_wrist_yaw_link": 8.886119947416683e-17,
      "left_hand_thumb_0_link": 7.473417450352271e-17,
      "left_hand_thumb_1_link": 7.473417450352271e-17,
      "left_hand_thumb_2_link": 7.076311083754595e-17,
      "left_hand_middle_0_link": 1.1443916996305594e-16,
      "left_hand_middle_1_link": 1.1443916996305594e-16,
      "left_hand_index_0_link": 1.2719202621569003e-16,
      "left_hand_index_1_link": 1.2177709378935645e-16,
      "right_shoulder_pitch_link": 1.4140045113229895e-16,
      "right_shoulder_roll_link": 1.480645733181173e-16,
      "right_shoulder_yaw_link": 1.379538079060927e-16,
      "right_elbow_link": 9.053860682492399e-17,
      "right_wrist_roll_link": 5.721958498152797e-17,
      "right_wrist_pitch_link": 6.206335383118183e-17,
      "right_wrist_yaw_link": 5.003707553108401e-17,
      "right_hand_thumb_0_link": 7.473417450352271e-17,
      "right_hand_thumb_1_link": 7.473417450352271e-17,
      "right_hand_thumb_2_link": 7.473417450352271e-17,
      "right_hand_middle_0_link": 1.415262216750919e-16,
      "right_hand_middle_1_link": 1.415262216750919e-16,
      "right_hand_index_0_link": 1.3597399555105182e-16,
      "right_hand_index_1_link": 1.3597399555105182e-16
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
| robot / total_com_registered | [0.0292670433, 7.98953038e-05, -0.0830634557] | [0.0292670433, 7.98953038e-05, -0.0830634557] | [0.0292670433, 7.98953038e-05, -0.0830634557] | [0, 0, 0] | eligible; compared after Kabsch alignment | [aggregate inputs](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_g1/g1_with_hands.xml#L1) | [aggregate inputs](https://github.com/unitreerobotics/unitree_ros/blob/adb48c7910ef8404ca34a07df95fc3acbb09f318/robots/g1_description/g1_29dof_with_hand_rev_1_0.xml#L1) | [aggregate inputs](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/g1_description/g1_29dof_with_hand_rev_1_0.xml#L1) |
| pelvis / com_registered | [0, 0, -0.07605] | [0, 0, -0.07605] | [0, 0, -0.07605] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L80](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_g1/g1_with_hands.xml#L80) | [CoM/kinematic input L58](https://github.com/unitreerobotics/unitree_ros/blob/adb48c7910ef8404ca34a07df95fc3acbb09f318/robots/g1_description/g1_29dof_with_hand_rev_1_0.xml#L58) | [CoM/kinematic input L58](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/g1_description/g1_29dof_with_hand_rev_1_0.xml#L58) |
| left_hip_pitch_link / com_registered | [0.002741, 0.112243, -0.12876] | [0.002741, 0.112243, -0.12876] | [0.002741, 0.112243, -0.12876] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L88](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_g1/g1_with_hands.xml#L88) | [CoM/kinematic input L65](https://github.com/unitreerobotics/unitree_ros/blob/adb48c7910ef8404ca34a07df95fc3acbb09f318/robots/g1_description/g1_29dof_with_hand_rev_1_0.xml#L65) | [CoM/kinematic input L65](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/g1_description/g1_29dof_with_hand_rev_1_0.xml#L65) |
| left_hip_roll_link / com_registered | [0.044658551, 0.115407, -0.214569899] | [0.044658551, 0.115407, -0.214569899] | [0.044658551, 0.115407, -0.214569899] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L94](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_g1/g1_with_hands.xml#L94) | [CoM/kinematic input L70](https://github.com/unitreerobotics/unitree_ros/blob/adb48c7910ef8404ca34a07df95fc3acbb09f318/robots/g1_description/g1_29dof_with_hand_rev_1_0.xml#L70) | [CoM/kinematic input L70](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/g1_description/g1_29dof_with_hand_rev_1_0.xml#L70) |
| left_hip_yaw_link / com_registered | [0.0156262474, 0.105471, -0.409562619] | [0.0156262474, 0.105471, -0.409562619] | [0.0156262474, 0.105471, -0.409562619] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L100](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_g1/g1_with_hands.xml#L100) | [CoM/kinematic input L75](https://github.com/unitreerobotics/unitree_ros/blob/adb48c7910ef8404ca34a07df95fc3acbb09f318/robots/g1_description/g1_29dof_with_hand_rev_1_0.xml#L75) | [CoM/kinematic input L75](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/g1_description/g1_29dof_with_hand_rev_1_0.xml#L75) |
| left_knee_link / com_registered | [0.0054546691, 0.1225649, -0.560035752] | [0.0054546691, 0.1225649, -0.560035752] | [0.0054546691, 0.1225649, -0.560035752] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L106](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_g1/g1_with_hands.xml#L106) | [CoM/kinematic input L80](https://github.com/unitreerobotics/unitree_ros/blob/adb48c7910ef8404ca34a07df95fc3acbb09f318/robots/g1_description/g1_29dof_with_hand_rev_1_0.xml#L80) | [CoM/kinematic input L80](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/g1_description/g1_29dof_with_hand_rev_1_0.xml#L80) |
| left_ankle_pitch_link / com_registered | [-0.0072713309, 0.118506455, -0.728168752] | [-0.0072713309, 0.118506455, -0.728168752] | [-0.0072713309, 0.118506455, -0.728168752] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L112](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_g1/g1_with_hands.xml#L112) | [CoM/kinematic input L85](https://github.com/unitreerobotics/unitree_ros/blob/adb48c7910ef8404ca34a07df95fc3acbb09f318/robots/g1_description/g1_29dof_with_hand_rev_1_0.xml#L85) | [CoM/kinematic input L85](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/g1_description/g1_29dof_with_hand_rev_1_0.xml#L85) |
| left_ankle_roll_link / com_registered | [0.0265026691, 0.118506455, -0.773288752] | [0.0265026691, 0.118506455, -0.773288752] | [0.0265026691, 0.118506455, -0.773288752] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L118](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_g1/g1_with_hands.xml#L118) | [CoM/kinematic input L90](https://github.com/unitreerobotics/unitree_ros/blob/adb48c7910ef8404ca34a07df95fc3acbb09f318/robots/g1_description/g1_29dof_with_hand_rev_1_0.xml#L90) | [CoM/kinematic input L90](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/g1_description/g1_29dof_with_hand_rev_1_0.xml#L90) |
| right_hip_pitch_link / com_registered | [0.002741, -0.112243, -0.12876] | [0.002741, -0.112243, -0.12876] | [0.002741, -0.112243, -0.12876] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L134](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_g1/g1_with_hands.xml#L134) | [CoM/kinematic input L104](https://github.com/unitreerobotics/unitree_ros/blob/adb48c7910ef8404ca34a07df95fc3acbb09f318/robots/g1_description/g1_29dof_with_hand_rev_1_0.xml#L104) | [CoM/kinematic input L104](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/g1_description/g1_29dof_with_hand_rev_1_0.xml#L104) |
| right_hip_roll_link / com_registered | [0.044658551, -0.115407, -0.214569899] | [0.044658551, -0.115407, -0.214569899] | [0.044658551, -0.115407, -0.214569899] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L140](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_g1/g1_with_hands.xml#L140) | [CoM/kinematic input L109](https://github.com/unitreerobotics/unitree_ros/blob/adb48c7910ef8404ca34a07df95fc3acbb09f318/robots/g1_description/g1_29dof_with_hand_rev_1_0.xml#L109) | [CoM/kinematic input L109](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/g1_description/g1_29dof_with_hand_rev_1_0.xml#L109) |
| right_hip_yaw_link / com_registered | [0.0156262474, -0.105471, -0.409562619] | [0.0156262474, -0.105471, -0.409562619] | [0.0156262474, -0.105471, -0.409562619] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L146](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_g1/g1_with_hands.xml#L146) | [CoM/kinematic input L114](https://github.com/unitreerobotics/unitree_ros/blob/adb48c7910ef8404ca34a07df95fc3acbb09f318/robots/g1_description/g1_29dof_with_hand_rev_1_0.xml#L114) | [CoM/kinematic input L114](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/g1_description/g1_29dof_with_hand_rev_1_0.xml#L114) |
| right_knee_link / com_registered | [0.0054546691, -0.1225649, -0.560035752] | [0.0054546691, -0.1225649, -0.560035752] | [0.0054546691, -0.1225649, -0.560035752] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L152](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_g1/g1_with_hands.xml#L152) | [CoM/kinematic input L119](https://github.com/unitreerobotics/unitree_ros/blob/adb48c7910ef8404ca34a07df95fc3acbb09f318/robots/g1_description/g1_29dof_with_hand_rev_1_0.xml#L119) | [CoM/kinematic input L119](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/g1_description/g1_29dof_with_hand_rev_1_0.xml#L119) |
| right_ankle_pitch_link / com_registered | [-0.0072713309, -0.118506455, -0.728168752] | [-0.0072713309, -0.118506455, -0.728168752] | [-0.0072713309, -0.118506455, -0.728168752] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L158](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_g1/g1_with_hands.xml#L158) | [CoM/kinematic input L124](https://github.com/unitreerobotics/unitree_ros/blob/adb48c7910ef8404ca34a07df95fc3acbb09f318/robots/g1_description/g1_29dof_with_hand_rev_1_0.xml#L124) | [CoM/kinematic input L124](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/g1_description/g1_29dof_with_hand_rev_1_0.xml#L124) |
| right_ankle_roll_link / com_registered | [0.0265026691, -0.118506455, -0.773288752] | [0.0265026691, -0.118506455, -0.773288752] | [0.0265026691, -0.118506455, -0.773288752] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L164](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_g1/g1_with_hands.xml#L164) | [CoM/kinematic input L129](https://github.com/unitreerobotics/unitree_ros/blob/adb48c7910ef8404ca34a07df95fc3acbb09f318/robots/g1_description/g1_29dof_with_hand_rev_1_0.xml#L129) | [CoM/kinematic input L129](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/g1_description/g1_29dof_with_hand_rev_1_0.xml#L129) |
| waist_yaw_link / com_registered | [0.003494, 0.000233, 0.018034] | [0.003494, 0.000233, 0.018034] | [0.003494, 0.000233, 0.018034] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L180](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_g1/g1_with_hands.xml#L180) | [CoM/kinematic input L143](https://github.com/unitreerobotics/unitree_ros/blob/adb48c7910ef8404ca34a07df95fc3acbb09f318/robots/g1_description/g1_29dof_with_hand_rev_1_0.xml#L143) | [CoM/kinematic input L143](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/g1_description/g1_29dof_with_hand_rev_1_0.xml#L143) |
| waist_roll_link / com_registered | [-0.0039635, 2.3e-05, 0.044] | [-0.0039635, 2.3e-05, 0.044] | [-0.0039635, 2.3e-05, 0.044] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L184](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_g1/g1_with_hands.xml#L184) | [CoM/kinematic input L147](https://github.com/unitreerobotics/unitree_ros/blob/adb48c7910ef8404ca34a07df95fc3acbb09f318/robots/g1_description/g1_29dof_with_hand_rev_1_0.xml#L147) | [CoM/kinematic input L147](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/g1_description/g1_29dof_with_hand_rev_1_0.xml#L147) |
| torso_link / com_registered | [-0.00193192, 0.000339683, 0.228568] | [-0.00193192, 0.000339683, 0.228568] | [-0.00193192, 0.000339683, 0.228568] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L189](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_g1/g1_with_hands.xml#L189) | [CoM/kinematic input L151](https://github.com/unitreerobotics/unitree_ros/blob/adb48c7910ef8404ca34a07df95fc3acbb09f318/robots/g1_description/g1_29dof_with_hand_rev_1_0.xml#L151) | [CoM/kinematic input L151](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/g1_description/g1_29dof_with_hand_rev_1_0.xml#L151) |
| left_shoulder_pitch_link / com_registered | [-4.62154742e-08, 0.137926788, 0.290497751] | [-4.62154742e-08, 0.137926788, 0.290497751] | [-4.62154742e-08, 0.137926788, 0.290497751] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L200](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_g1/g1_with_hands.xml#L200) | [CoM/kinematic input L161](https://github.com/unitreerobotics/unitree_ros/blob/adb48c7910ef8404ca34a07df95fc3acbb09f318/robots/g1_description/g1_29dof_with_hand_rev_1_0.xml#L161) | [CoM/kinematic input L161](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/g1_description/g1_29dof_with_hand_rev_1_0.xml#L161) |
| left_shoulder_roll_link / com_registered | [-0.000228707597, 0.147834189, 0.225718722] | [-0.000228707597, 0.147834189, 0.225718722] | [-0.000228707597, 0.147834189, 0.225718722] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L207](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_g1/g1_with_hands.xml#L207) | [CoM/kinematic input L166](https://github.com/unitreerobotics/unitree_ros/blob/adb48c7910ef8404ca34a07df95fc3acbb09f318/robots/g1_description/g1_29dof_with_hand_rev_1_0.xml#L166) | [CoM/kinematic input L166](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/g1_description/g1_29dof_with_hand_rev_1_0.xml#L166) |
| left_shoulder_yaw_link / com_registered | [0.0107643787, 0.143859638, 0.113751885] | [0.0107643787, 0.143859638, 0.113751885] | [0.0107643787, 0.143859638, 0.113751885] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L213](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_g1/g1_with_hands.xml#L213) | [CoM/kinematic input L171](https://github.com/unitreerobotics/unitree_ros/blob/adb48c7910ef8404ca34a07df95fc3acbb09f318/robots/g1_description/g1_29dof_with_hand_rev_1_0.xml#L171) | [CoM/kinematic input L171](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/g1_description/g1_29dof_with_hand_rev_1_0.xml#L171) |
| left_elbow_link / com_registered | [0.0807307754, 0.151250321, 0.0951774737] | [0.0807307754, 0.151250321, 0.0951774737] | [0.0807307754, 0.151250321, 0.0951774737] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L219](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_g1/g1_with_hands.xml#L219) | [CoM/kinematic input L176](https://github.com/unitreerobotics/unitree_ros/blob/adb48c7910ef8404ca34a07df95fc3acbb09f318/robots/g1_description/g1_29dof_with_hand_rev_1_0.xml#L176) | [CoM/kinematic input L176](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/g1_description/g1_29dof_with_hand_rev_1_0.xml#L176) |
| left_wrist_roll_link / com_registered | [0.132913789, 0.14921182, 0.0952369761] | [0.132913789, 0.14921182, 0.0952369761] | [0.132913789, 0.14921182, 0.0952369761] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L225](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_g1/g1_with_hands.xml#L225) | [CoM/kinematic input L181](https://github.com/unitreerobotics/unitree_ros/blob/adb48c7910ef8404ca34a07df95fc3acbb09f318/robots/g1_description/g1_29dof_with_hand_rev_1_0.xml#L181) | [CoM/kinematic input L181](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/g1_description/g1_29dof_with_hand_rev_1_0.xml#L181) |
| left_wrist_pitch_link / com_registered | [0.17677391, 0.147549041, 0.0941174005] | [0.17677391, 0.147549041, 0.0941174005] | [0.17677391, 0.147549041, 0.0941174005] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L231](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_g1/g1_with_hands.xml#L231) | [CoM/kinematic input L186](https://github.com/unitreerobotics/unitree_ros/blob/adb48c7910ef8404ca34a07df95fc3acbb09f318/robots/g1_description/g1_29dof_with_hand_rev_1_0.xml#L186) | [CoM/kinematic input L186](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/g1_description/g1_29dof_with_hand_rev_1_0.xml#L186) |
| left_wrist_yaw_link / com_registered | [0.288325269, 0.150766636, 0.0948534786] | [0.288325269, 0.150766636, 0.0948534786] | [0.288325269, 0.150766636, 0.0948534786] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L237](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_g1/g1_with_hands.xml#L237) | [CoM/kinematic input L191](https://github.com/unitreerobotics/unitree_ros/blob/adb48c7910ef8404ca34a07df95fc3acbb09f318/robots/g1_description/g1_29dof_with_hand_rev_1_0.xml#L191) | [CoM/kinematic input L191](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/g1_description/g1_29dof_with_hand_rev_1_0.xml#L191) |
| left_hand_thumb_0_link / com_registered | [0.26588901, 0.143014627, 0.0961731123] | [0.26588901, 0.143014627, 0.0961731123] | [0.26588901, 0.143014627, 0.0961731123] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L246](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_g1/g1_with_hands.xml#L246) | [CoM/kinematic input L198](https://github.com/unitreerobotics/unitree_ros/blob/adb48c7910ef8404ca34a07df95fc3acbb09f318/robots/g1_description/g1_29dof_with_hand_rev_1_0.xml#L198) | [CoM/kinematic input L198](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/g1_description/g1_29dof_with_hand_rev_1_0.xml#L198) |
| left_hand_thumb_1_link / com_registered | [0.263436455, 0.0968748438, 0.0948453523] | [0.263436455, 0.0968748438, 0.0948453523] | [0.263436455, 0.0968748438, 0.0948453523] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L253](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_g1/g1_with_hands.xml#L253) | [CoM/kinematic input L203](https://github.com/unitreerobotics/unitree_ros/blob/adb48c7910ef8404ca34a07df95fc3acbb09f318/robots/g1_description/g1_29dof_with_hand_rev_1_0.xml#L203) | [CoM/kinematic input L203](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/g1_description/g1_29dof_with_hand_rev_1_0.xml#L203) |
| left_hand_thumb_2_link / com_registered | [0.262540006, 0.0602674863, 0.0953319471] | [0.262540006, 0.0602674863, 0.0953319471] | [0.262540006, 0.0602674863, 0.0953319471] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L260](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_g1/g1_with_hands.xml#L260) | [CoM/kinematic input L208](https://github.com/unitreerobotics/unitree_ros/blob/adb48c7910ef8404ca34a07df95fc3acbb09f318/robots/g1_description/g1_29dof_with_hand_rev_1_0.xml#L208) | [CoM/kinematic input L208](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/g1_description/g1_29dof_with_hand_rev_1_0.xml#L208) |
| left_hand_middle_0_link / com_registered | [0.354448177, 0.15406132, 0.0671055008] | [0.354448177, 0.15406132, 0.0671055008] | [0.354448177, 0.15406132, 0.0671055008] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L269](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_g1/g1_with_hands.xml#L269) | [CoM/kinematic input L216](https://github.com/unitreerobotics/unitree_ros/blob/adb48c7910ef8404ca34a07df95fc3acbb09f318/robots/g1_description/g1_29dof_with_hand_rev_1_0.xml#L216) | [CoM/kinematic input L216](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/g1_description/g1_29dof_with_hand_rev_1_0.xml#L216) |
| left_hand_middle_1_link / com_registered | [0.39105582, 0.154943797, 0.0666148523] | [0.39105582, 0.154943797, 0.0666148523] | [0.39105582, 0.154943797, 0.0666148523] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L276](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_g1/g1_with_hands.xml#L276) | [CoM/kinematic input L221](https://github.com/unitreerobotics/unitree_ros/blob/adb48c7910ef8404ca34a07df95fc3acbb09f318/robots/g1_description/g1_29dof_with_hand_rev_1_0.xml#L221) | [CoM/kinematic input L221](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/g1_description/g1_29dof_with_hand_rev_1_0.xml#L221) |
| left_hand_index_0_link / com_registered | [0.354451308, 0.154057982, 0.124105501] | [0.354451308, 0.154057982, 0.124105501] | [0.354451308, 0.154057982, 0.124105501] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L284](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_g1/g1_with_hands.xml#L284) | [CoM/kinematic input L228](https://github.com/unitreerobotics/unitree_ros/blob/adb48c7910ef8404ca34a07df95fc3acbb09f318/robots/g1_description/g1_29dof_with_hand_rev_1_0.xml#L228) | [CoM/kinematic input L228](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/g1_description/g1_29dof_with_hand_rev_1_0.xml#L228) |
| left_hand_index_1_link / com_registered | [0.391058951, 0.154940459, 0.123614852] | [0.391058951, 0.154940459, 0.123614852] | [0.391058951, 0.154940459, 0.123614852] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L291](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_g1/g1_with_hands.xml#L291) | [CoM/kinematic input L233](https://github.com/unitreerobotics/unitree_ros/blob/adb48c7910ef8404ca34a07df95fc3acbb09f318/robots/g1_description/g1_29dof_with_hand_rev_1_0.xml#L233) | [CoM/kinematic input L233](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/g1_description/g1_29dof_with_hand_rev_1_0.xml#L233) |
| right_shoulder_pitch_link / com_registered | [-4.62154742e-08, -0.137916788, 0.290497751] | [-4.62154742e-08, -0.137916788, 0.290497751] | [-4.62154742e-08, -0.137916788, 0.290497751] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L307](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_g1/g1_with_hands.xml#L307) | [CoM/kinematic input L247](https://github.com/unitreerobotics/unitree_ros/blob/adb48c7910ef8404ca34a07df95fc3acbb09f318/robots/g1_description/g1_29dof_with_hand_rev_1_0.xml#L247) | [CoM/kinematic input L247](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/g1_description/g1_29dof_with_hand_rev_1_0.xml#L247) |
| right_shoulder_roll_link / com_registered | [-0.000228707597, -0.147824189, 0.225718722] | [-0.000228707597, -0.147824189, 0.225718722] | [-0.000228707597, -0.147824189, 0.225718722] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L314](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_g1/g1_with_hands.xml#L314) | [CoM/kinematic input L252](https://github.com/unitreerobotics/unitree_ros/blob/adb48c7910ef8404ca34a07df95fc3acbb09f318/robots/g1_description/g1_29dof_with_hand_rev_1_0.xml#L252) | [CoM/kinematic input L252](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/g1_description/g1_29dof_with_hand_rev_1_0.xml#L252) |
| right_shoulder_yaw_link / com_registered | [0.0107643787, -0.143849638, 0.113751885] | [0.0107643787, -0.143849638, 0.113751885] | [0.0107643787, -0.143849638, 0.113751885] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L320](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_g1/g1_with_hands.xml#L320) | [CoM/kinematic input L257](https://github.com/unitreerobotics/unitree_ros/blob/adb48c7910ef8404ca34a07df95fc3acbb09f318/robots/g1_description/g1_29dof_with_hand_rev_1_0.xml#L257) | [CoM/kinematic input L257](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/g1_description/g1_29dof_with_hand_rev_1_0.xml#L257) |
| right_elbow_link / com_registered | [0.0807307754, -0.151240321, 0.0951774737] | [0.0807307754, -0.151240321, 0.0951774737] | [0.0807307754, -0.151240321, 0.0951774737] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L326](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_g1/g1_with_hands.xml#L326) | [CoM/kinematic input L262](https://github.com/unitreerobotics/unitree_ros/blob/adb48c7910ef8404ca34a07df95fc3acbb09f318/robots/g1_description/g1_29dof_with_hand_rev_1_0.xml#L262) | [CoM/kinematic input L262](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/g1_description/g1_29dof_with_hand_rev_1_0.xml#L262) |
| right_wrist_roll_link / com_registered | [0.132913789, -0.14920182, 0.0952369761] | [0.132913789, -0.14920182, 0.0952369761] | [0.132913789, -0.14920182, 0.0952369761] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L332](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_g1/g1_with_hands.xml#L332) | [CoM/kinematic input L267](https://github.com/unitreerobotics/unitree_ros/blob/adb48c7910ef8404ca34a07df95fc3acbb09f318/robots/g1_description/g1_29dof_with_hand_rev_1_0.xml#L267) | [CoM/kinematic input L267](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/g1_description/g1_29dof_with_hand_rev_1_0.xml#L267) |
| right_wrist_pitch_link / com_registered | [0.17677391, -0.147539041, 0.0941174005] | [0.17677391, -0.147539041, 0.0941174005] | [0.17677391, -0.147539041, 0.0941174005] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L338](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_g1/g1_with_hands.xml#L338) | [CoM/kinematic input L272](https://github.com/unitreerobotics/unitree_ros/blob/adb48c7910ef8404ca34a07df95fc3acbb09f318/robots/g1_description/g1_29dof_with_hand_rev_1_0.xml#L272) | [CoM/kinematic input L272](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/g1_description/g1_29dof_with_hand_rev_1_0.xml#L272) |
| right_wrist_yaw_link / com_registered | [0.288325269, -0.150756636, 0.0948534786] | [0.288325269, -0.150756636, 0.0948534786] | [0.288325269, -0.150756636, 0.0948534786] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L344](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_g1/g1_with_hands.xml#L344) | [CoM/kinematic input L277](https://github.com/unitreerobotics/unitree_ros/blob/adb48c7910ef8404ca34a07df95fc3acbb09f318/robots/g1_description/g1_29dof_with_hand_rev_1_0.xml#L277) | [CoM/kinematic input L277](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/g1_description/g1_29dof_with_hand_rev_1_0.xml#L277) |
| right_hand_thumb_0_link / com_registered | [0.26588901, -0.143004627, 0.0961731123] | [0.26588901, -0.143004627, 0.0961731123] | [0.26588901, -0.143004627, 0.0961731123] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L353](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_g1/g1_with_hands.xml#L353) | [CoM/kinematic input L284](https://github.com/unitreerobotics/unitree_ros/blob/adb48c7910ef8404ca34a07df95fc3acbb09f318/robots/g1_description/g1_29dof_with_hand_rev_1_0.xml#L284) | [CoM/kinematic input L284](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/g1_description/g1_29dof_with_hand_rev_1_0.xml#L284) |
| right_hand_thumb_1_link / com_registered | [0.263436455, -0.0968648438, 0.0948453523] | [0.263436455, -0.0968648438, 0.0948453523] | [0.263436455, -0.0968648438, 0.0948453523] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L360](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_g1/g1_with_hands.xml#L360) | [CoM/kinematic input L289](https://github.com/unitreerobotics/unitree_ros/blob/adb48c7910ef8404ca34a07df95fc3acbb09f318/robots/g1_description/g1_29dof_with_hand_rev_1_0.xml#L289) | [CoM/kinematic input L289](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/g1_description/g1_29dof_with_hand_rev_1_0.xml#L289) |
| right_hand_thumb_2_link / com_registered | [0.262540006, -0.0602574863, 0.0953319471] | [0.262540006, -0.0602574863, 0.0953319471] | [0.262540006, -0.0602574863, 0.0953319471] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L367](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_g1/g1_with_hands.xml#L367) | [CoM/kinematic input L294](https://github.com/unitreerobotics/unitree_ros/blob/adb48c7910ef8404ca34a07df95fc3acbb09f318/robots/g1_description/g1_29dof_with_hand_rev_1_0.xml#L294) | [CoM/kinematic input L294](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/g1_description/g1_29dof_with_hand_rev_1_0.xml#L294) |
| right_hand_middle_0_link / com_registered | [0.354448177, -0.15405132, 0.0671055008] | [0.354448177, -0.15405132, 0.0671055008] | [0.354448177, -0.15405132, 0.0671055008] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L376](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_g1/g1_with_hands.xml#L376) | [CoM/kinematic input L302](https://github.com/unitreerobotics/unitree_ros/blob/adb48c7910ef8404ca34a07df95fc3acbb09f318/robots/g1_description/g1_29dof_with_hand_rev_1_0.xml#L302) | [CoM/kinematic input L302](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/g1_description/g1_29dof_with_hand_rev_1_0.xml#L302) |
| right_hand_middle_1_link / com_registered | [0.39105582, -0.154933797, 0.0666148523] | [0.39105582, -0.154933797, 0.0666148523] | [0.39105582, -0.154933797, 0.0666148523] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L383](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_g1/g1_with_hands.xml#L383) | [CoM/kinematic input L307](https://github.com/unitreerobotics/unitree_ros/blob/adb48c7910ef8404ca34a07df95fc3acbb09f318/robots/g1_description/g1_29dof_with_hand_rev_1_0.xml#L307) | [CoM/kinematic input L307](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/g1_description/g1_29dof_with_hand_rev_1_0.xml#L307) |
| right_hand_index_0_link / com_registered | [0.354451308, -0.154047982, 0.124105501] | [0.354451308, -0.154047982, 0.124105501] | [0.354451308, -0.154047982, 0.124105501] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L391](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_g1/g1_with_hands.xml#L391) | [CoM/kinematic input L314](https://github.com/unitreerobotics/unitree_ros/blob/adb48c7910ef8404ca34a07df95fc3acbb09f318/robots/g1_description/g1_29dof_with_hand_rev_1_0.xml#L314) | [CoM/kinematic input L314](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/g1_description/g1_29dof_with_hand_rev_1_0.xml#L314) |
| right_hand_index_1_link / com_registered | [0.391058951, -0.154930459, 0.123614852] | [0.391058951, -0.154930459, 0.123614852] | [0.391058951, -0.154930459, 0.123614852] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L398](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_g1/g1_with_hands.xml#L398) | [CoM/kinematic input L319](https://github.com/unitreerobotics/unitree_ros/blob/adb48c7910ef8404ca34a07df95fc3acbb09f318/robots/g1_description/g1_29dof_with_hand_rev_1_0.xml#L319) | [CoM/kinematic input L319](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/g1_description/g1_29dof_with_hand_rev_1_0.xml#L319) |

## Mass accounting

Every contributing compiled body mass is listed here so total/subtree sums can be checked. Links point to explicit inertials or to geometry inputs when the compiler inferred a mass. CoM links identify inertial inputs; world coordinates additionally use the ancestor transforms and the registration recorded below.

| M body | M kg / source | S kg / source | H kg / source |
|---|---|---|---|
| pelvis | 3.813 / [input L80](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_g1/g1_with_hands.xml#L80) | 3.813 / [input L58](https://github.com/unitreerobotics/unitree_ros/blob/adb48c7910ef8404ca34a07df95fc3acbb09f318/robots/g1_description/g1_29dof_with_hand_rev_1_0.xml#L58) | 3.813 / [input L58](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/g1_description/g1_29dof_with_hand_rev_1_0.xml#L58) |
| left_hip_pitch_link | 1.35 / [input L88](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_g1/g1_with_hands.xml#L88) | 1.35 / [input L65](https://github.com/unitreerobotics/unitree_ros/blob/adb48c7910ef8404ca34a07df95fc3acbb09f318/robots/g1_description/g1_29dof_with_hand_rev_1_0.xml#L65) | 1.35 / [input L65](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/g1_description/g1_29dof_with_hand_rev_1_0.xml#L65) |
| left_hip_roll_link | 1.52 / [input L94](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_g1/g1_with_hands.xml#L94) | 1.52 / [input L70](https://github.com/unitreerobotics/unitree_ros/blob/adb48c7910ef8404ca34a07df95fc3acbb09f318/robots/g1_description/g1_29dof_with_hand_rev_1_0.xml#L70) | 1.52 / [input L70](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/g1_description/g1_29dof_with_hand_rev_1_0.xml#L70) |
| left_hip_yaw_link | 1.702 / [input L100](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_g1/g1_with_hands.xml#L100) | 1.702 / [input L75](https://github.com/unitreerobotics/unitree_ros/blob/adb48c7910ef8404ca34a07df95fc3acbb09f318/robots/g1_description/g1_29dof_with_hand_rev_1_0.xml#L75) | 1.702 / [input L75](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/g1_description/g1_29dof_with_hand_rev_1_0.xml#L75) |
| left_knee_link | 1.932 / [input L106](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_g1/g1_with_hands.xml#L106) | 1.932 / [input L80](https://github.com/unitreerobotics/unitree_ros/blob/adb48c7910ef8404ca34a07df95fc3acbb09f318/robots/g1_description/g1_29dof_with_hand_rev_1_0.xml#L80) | 1.932 / [input L80](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/g1_description/g1_29dof_with_hand_rev_1_0.xml#L80) |
| left_ankle_pitch_link | 0.074 / [input L112](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_g1/g1_with_hands.xml#L112) | 0.074 / [input L85](https://github.com/unitreerobotics/unitree_ros/blob/adb48c7910ef8404ca34a07df95fc3acbb09f318/robots/g1_description/g1_29dof_with_hand_rev_1_0.xml#L85) | 0.074 / [input L85](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/g1_description/g1_29dof_with_hand_rev_1_0.xml#L85) |
| left_ankle_roll_link | 0.608 / [input L118](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_g1/g1_with_hands.xml#L118) | 0.608 / [input L90](https://github.com/unitreerobotics/unitree_ros/blob/adb48c7910ef8404ca34a07df95fc3acbb09f318/robots/g1_description/g1_29dof_with_hand_rev_1_0.xml#L90) | 0.608 / [input L90](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/g1_description/g1_29dof_with_hand_rev_1_0.xml#L90) |
| right_hip_pitch_link | 1.35 / [input L134](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_g1/g1_with_hands.xml#L134) | 1.35 / [input L104](https://github.com/unitreerobotics/unitree_ros/blob/adb48c7910ef8404ca34a07df95fc3acbb09f318/robots/g1_description/g1_29dof_with_hand_rev_1_0.xml#L104) | 1.35 / [input L104](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/g1_description/g1_29dof_with_hand_rev_1_0.xml#L104) |
| right_hip_roll_link | 1.52 / [input L140](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_g1/g1_with_hands.xml#L140) | 1.52 / [input L109](https://github.com/unitreerobotics/unitree_ros/blob/adb48c7910ef8404ca34a07df95fc3acbb09f318/robots/g1_description/g1_29dof_with_hand_rev_1_0.xml#L109) | 1.52 / [input L109](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/g1_description/g1_29dof_with_hand_rev_1_0.xml#L109) |
| right_hip_yaw_link | 1.702 / [input L146](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_g1/g1_with_hands.xml#L146) | 1.702 / [input L114](https://github.com/unitreerobotics/unitree_ros/blob/adb48c7910ef8404ca34a07df95fc3acbb09f318/robots/g1_description/g1_29dof_with_hand_rev_1_0.xml#L114) | 1.702 / [input L114](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/g1_description/g1_29dof_with_hand_rev_1_0.xml#L114) |
| right_knee_link | 1.932 / [input L152](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_g1/g1_with_hands.xml#L152) | 1.932 / [input L119](https://github.com/unitreerobotics/unitree_ros/blob/adb48c7910ef8404ca34a07df95fc3acbb09f318/robots/g1_description/g1_29dof_with_hand_rev_1_0.xml#L119) | 1.932 / [input L119](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/g1_description/g1_29dof_with_hand_rev_1_0.xml#L119) |
| right_ankle_pitch_link | 0.074 / [input L158](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_g1/g1_with_hands.xml#L158) | 0.074 / [input L124](https://github.com/unitreerobotics/unitree_ros/blob/adb48c7910ef8404ca34a07df95fc3acbb09f318/robots/g1_description/g1_29dof_with_hand_rev_1_0.xml#L124) | 0.074 / [input L124](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/g1_description/g1_29dof_with_hand_rev_1_0.xml#L124) |
| right_ankle_roll_link | 0.608 / [input L164](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_g1/g1_with_hands.xml#L164) | 0.608 / [input L129](https://github.com/unitreerobotics/unitree_ros/blob/adb48c7910ef8404ca34a07df95fc3acbb09f318/robots/g1_description/g1_29dof_with_hand_rev_1_0.xml#L129) | 0.608 / [input L129](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/g1_description/g1_29dof_with_hand_rev_1_0.xml#L129) |
| waist_yaw_link | 0.214 / [input L180](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_g1/g1_with_hands.xml#L180) | 0.214 / [input L143](https://github.com/unitreerobotics/unitree_ros/blob/adb48c7910ef8404ca34a07df95fc3acbb09f318/robots/g1_description/g1_29dof_with_hand_rev_1_0.xml#L143) | 0.214 / [input L143](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/g1_description/g1_29dof_with_hand_rev_1_0.xml#L143) |
| waist_roll_link | 0.086 / [input L184](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_g1/g1_with_hands.xml#L184) | 0.086 / [input L147](https://github.com/unitreerobotics/unitree_ros/blob/adb48c7910ef8404ca34a07df95fc3acbb09f318/robots/g1_description/g1_29dof_with_hand_rev_1_0.xml#L147) | 0.086 / [input L147](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/g1_description/g1_29dof_with_hand_rev_1_0.xml#L147) |
| torso_link | 7.818 / [input L189](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_g1/g1_with_hands.xml#L189) | 7.818 / [input L151](https://github.com/unitreerobotics/unitree_ros/blob/adb48c7910ef8404ca34a07df95fc3acbb09f318/robots/g1_description/g1_29dof_with_hand_rev_1_0.xml#L151) | 7.818 / [input L151](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/g1_description/g1_29dof_with_hand_rev_1_0.xml#L151) |
| left_shoulder_pitch_link | 0.718 / [input L200](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_g1/g1_with_hands.xml#L200) | 0.718 / [input L161](https://github.com/unitreerobotics/unitree_ros/blob/adb48c7910ef8404ca34a07df95fc3acbb09f318/robots/g1_description/g1_29dof_with_hand_rev_1_0.xml#L161) | 0.718 / [input L161](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/g1_description/g1_29dof_with_hand_rev_1_0.xml#L161) |
| left_shoulder_roll_link | 0.643 / [input L207](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_g1/g1_with_hands.xml#L207) | 0.643 / [input L166](https://github.com/unitreerobotics/unitree_ros/blob/adb48c7910ef8404ca34a07df95fc3acbb09f318/robots/g1_description/g1_29dof_with_hand_rev_1_0.xml#L166) | 0.643 / [input L166](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/g1_description/g1_29dof_with_hand_rev_1_0.xml#L166) |
| left_shoulder_yaw_link | 0.734 / [input L213](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_g1/g1_with_hands.xml#L213) | 0.734 / [input L171](https://github.com/unitreerobotics/unitree_ros/blob/adb48c7910ef8404ca34a07df95fc3acbb09f318/robots/g1_description/g1_29dof_with_hand_rev_1_0.xml#L171) | 0.734 / [input L171](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/g1_description/g1_29dof_with_hand_rev_1_0.xml#L171) |
| left_elbow_link | 0.6 / [input L219](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_g1/g1_with_hands.xml#L219) | 0.6 / [input L176](https://github.com/unitreerobotics/unitree_ros/blob/adb48c7910ef8404ca34a07df95fc3acbb09f318/robots/g1_description/g1_29dof_with_hand_rev_1_0.xml#L176) | 0.6 / [input L176](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/g1_description/g1_29dof_with_hand_rev_1_0.xml#L176) |
| left_wrist_roll_link | 0.085445 / [input L225](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_g1/g1_with_hands.xml#L225) | 0.085445 / [input L181](https://github.com/unitreerobotics/unitree_ros/blob/adb48c7910ef8404ca34a07df95fc3acbb09f318/robots/g1_description/g1_29dof_with_hand_rev_1_0.xml#L181) | 0.085445 / [input L181](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/g1_description/g1_29dof_with_hand_rev_1_0.xml#L181) |
| left_wrist_pitch_link | 0.48405 / [input L231](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_g1/g1_with_hands.xml#L231) | 0.48405 / [input L186](https://github.com/unitreerobotics/unitree_ros/blob/adb48c7910ef8404ca34a07df95fc3acbb09f318/robots/g1_description/g1_29dof_with_hand_rev_1_0.xml#L186) | 0.48405 / [input L186](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/g1_description/g1_29dof_with_hand_rev_1_0.xml#L186) |
| left_wrist_yaw_link | 0.457415 / [input L237](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_g1/g1_with_hands.xml#L237) | 0.457415 / [input L191](https://github.com/unitreerobotics/unitree_ros/blob/adb48c7910ef8404ca34a07df95fc3acbb09f318/robots/g1_description/g1_29dof_with_hand_rev_1_0.xml#L191) | 0.457415 / [input L191](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/g1_description/g1_29dof_with_hand_rev_1_0.xml#L191) |
| left_hand_thumb_0_link | 0.0862366 / [input L246](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_g1/g1_with_hands.xml#L246) | 0.0862366 / [input L198](https://github.com/unitreerobotics/unitree_ros/blob/adb48c7910ef8404ca34a07df95fc3acbb09f318/robots/g1_description/g1_29dof_with_hand_rev_1_0.xml#L198) | 0.0862366 / [input L198](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/g1_description/g1_29dof_with_hand_rev_1_0.xml#L198) |
| left_hand_thumb_1_link | 0.0588507 / [input L253](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_g1/g1_with_hands.xml#L253) | 0.0588507 / [input L203](https://github.com/unitreerobotics/unitree_ros/blob/adb48c7910ef8404ca34a07df95fc3acbb09f318/robots/g1_description/g1_29dof_with_hand_rev_1_0.xml#L203) | 0.0588507 / [input L203](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/g1_description/g1_29dof_with_hand_rev_1_0.xml#L203) |
| left_hand_thumb_2_link | 0.0203063 / [input L260](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_g1/g1_with_hands.xml#L260) | 0.0203063 / [input L208](https://github.com/unitreerobotics/unitree_ros/blob/adb48c7910ef8404ca34a07df95fc3acbb09f318/robots/g1_description/g1_29dof_with_hand_rev_1_0.xml#L208) | 0.0203063 / [input L208](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/g1_description/g1_29dof_with_hand_rev_1_0.xml#L208) |
| left_hand_middle_0_link | 0.0588507 / [input L269](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_g1/g1_with_hands.xml#L269) | 0.0588507 / [input L216](https://github.com/unitreerobotics/unitree_ros/blob/adb48c7910ef8404ca34a07df95fc3acbb09f318/robots/g1_description/g1_29dof_with_hand_rev_1_0.xml#L216) | 0.0588507 / [input L216](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/g1_description/g1_29dof_with_hand_rev_1_0.xml#L216) |
| left_hand_middle_1_link | 0.0203063 / [input L276](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_g1/g1_with_hands.xml#L276) | 0.0203063 / [input L221](https://github.com/unitreerobotics/unitree_ros/blob/adb48c7910ef8404ca34a07df95fc3acbb09f318/robots/g1_description/g1_29dof_with_hand_rev_1_0.xml#L221) | 0.0203063 / [input L221](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/g1_description/g1_29dof_with_hand_rev_1_0.xml#L221) |
| left_hand_index_0_link | 0.0588507 / [input L284](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_g1/g1_with_hands.xml#L284) | 0.0588507 / [input L228](https://github.com/unitreerobotics/unitree_ros/blob/adb48c7910ef8404ca34a07df95fc3acbb09f318/robots/g1_description/g1_29dof_with_hand_rev_1_0.xml#L228) | 0.0588507 / [input L228](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/g1_description/g1_29dof_with_hand_rev_1_0.xml#L228) |
| left_hand_index_1_link | 0.0203063 / [input L291](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_g1/g1_with_hands.xml#L291) | 0.0203063 / [input L233](https://github.com/unitreerobotics/unitree_ros/blob/adb48c7910ef8404ca34a07df95fc3acbb09f318/robots/g1_description/g1_29dof_with_hand_rev_1_0.xml#L233) | 0.0203063 / [input L233](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/g1_description/g1_29dof_with_hand_rev_1_0.xml#L233) |
| right_shoulder_pitch_link | 0.718 / [input L307](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_g1/g1_with_hands.xml#L307) | 0.718 / [input L247](https://github.com/unitreerobotics/unitree_ros/blob/adb48c7910ef8404ca34a07df95fc3acbb09f318/robots/g1_description/g1_29dof_with_hand_rev_1_0.xml#L247) | 0.718 / [input L247](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/g1_description/g1_29dof_with_hand_rev_1_0.xml#L247) |
| right_shoulder_roll_link | 0.643 / [input L314](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_g1/g1_with_hands.xml#L314) | 0.643 / [input L252](https://github.com/unitreerobotics/unitree_ros/blob/adb48c7910ef8404ca34a07df95fc3acbb09f318/robots/g1_description/g1_29dof_with_hand_rev_1_0.xml#L252) | 0.643 / [input L252](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/g1_description/g1_29dof_with_hand_rev_1_0.xml#L252) |
| right_shoulder_yaw_link | 0.734 / [input L320](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_g1/g1_with_hands.xml#L320) | 0.734 / [input L257](https://github.com/unitreerobotics/unitree_ros/blob/adb48c7910ef8404ca34a07df95fc3acbb09f318/robots/g1_description/g1_29dof_with_hand_rev_1_0.xml#L257) | 0.734 / [input L257](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/g1_description/g1_29dof_with_hand_rev_1_0.xml#L257) |
| right_elbow_link | 0.6 / [input L326](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_g1/g1_with_hands.xml#L326) | 0.6 / [input L262](https://github.com/unitreerobotics/unitree_ros/blob/adb48c7910ef8404ca34a07df95fc3acbb09f318/robots/g1_description/g1_29dof_with_hand_rev_1_0.xml#L262) | 0.6 / [input L262](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/g1_description/g1_29dof_with_hand_rev_1_0.xml#L262) |
| right_wrist_roll_link | 0.085445 / [input L332](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_g1/g1_with_hands.xml#L332) | 0.085445 / [input L267](https://github.com/unitreerobotics/unitree_ros/blob/adb48c7910ef8404ca34a07df95fc3acbb09f318/robots/g1_description/g1_29dof_with_hand_rev_1_0.xml#L267) | 0.085445 / [input L267](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/g1_description/g1_29dof_with_hand_rev_1_0.xml#L267) |
| right_wrist_pitch_link | 0.48405 / [input L338](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_g1/g1_with_hands.xml#L338) | 0.48405 / [input L272](https://github.com/unitreerobotics/unitree_ros/blob/adb48c7910ef8404ca34a07df95fc3acbb09f318/robots/g1_description/g1_29dof_with_hand_rev_1_0.xml#L272) | 0.48405 / [input L272](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/g1_description/g1_29dof_with_hand_rev_1_0.xml#L272) |
| right_wrist_yaw_link | 0.457415 / [input L344](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_g1/g1_with_hands.xml#L344) | 0.457415 / [input L277](https://github.com/unitreerobotics/unitree_ros/blob/adb48c7910ef8404ca34a07df95fc3acbb09f318/robots/g1_description/g1_29dof_with_hand_rev_1_0.xml#L277) | 0.457415 / [input L277](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/g1_description/g1_29dof_with_hand_rev_1_0.xml#L277) |
| right_hand_thumb_0_link | 0.0862366 / [input L353](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_g1/g1_with_hands.xml#L353) | 0.0862366 / [input L284](https://github.com/unitreerobotics/unitree_ros/blob/adb48c7910ef8404ca34a07df95fc3acbb09f318/robots/g1_description/g1_29dof_with_hand_rev_1_0.xml#L284) | 0.0862366 / [input L284](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/g1_description/g1_29dof_with_hand_rev_1_0.xml#L284) |
| right_hand_thumb_1_link | 0.0588507 / [input L360](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_g1/g1_with_hands.xml#L360) | 0.0588507 / [input L289](https://github.com/unitreerobotics/unitree_ros/blob/adb48c7910ef8404ca34a07df95fc3acbb09f318/robots/g1_description/g1_29dof_with_hand_rev_1_0.xml#L289) | 0.0588507 / [input L289](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/g1_description/g1_29dof_with_hand_rev_1_0.xml#L289) |
| right_hand_thumb_2_link | 0.0203063 / [input L367](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_g1/g1_with_hands.xml#L367) | 0.0203063 / [input L294](https://github.com/unitreerobotics/unitree_ros/blob/adb48c7910ef8404ca34a07df95fc3acbb09f318/robots/g1_description/g1_29dof_with_hand_rev_1_0.xml#L294) | 0.0203063 / [input L294](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/g1_description/g1_29dof_with_hand_rev_1_0.xml#L294) |
| right_hand_middle_0_link | 0.0588507 / [input L376](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_g1/g1_with_hands.xml#L376) | 0.0588507 / [input L302](https://github.com/unitreerobotics/unitree_ros/blob/adb48c7910ef8404ca34a07df95fc3acbb09f318/robots/g1_description/g1_29dof_with_hand_rev_1_0.xml#L302) | 0.0588507 / [input L302](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/g1_description/g1_29dof_with_hand_rev_1_0.xml#L302) |
| right_hand_middle_1_link | 0.0203063 / [input L383](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_g1/g1_with_hands.xml#L383) | 0.0203063 / [input L307](https://github.com/unitreerobotics/unitree_ros/blob/adb48c7910ef8404ca34a07df95fc3acbb09f318/robots/g1_description/g1_29dof_with_hand_rev_1_0.xml#L307) | 0.0203063 / [input L307](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/g1_description/g1_29dof_with_hand_rev_1_0.xml#L307) |
| right_hand_index_0_link | 0.0588507 / [input L391](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_g1/g1_with_hands.xml#L391) | 0.0588507 / [input L314](https://github.com/unitreerobotics/unitree_ros/blob/adb48c7910ef8404ca34a07df95fc3acbb09f318/robots/g1_description/g1_29dof_with_hand_rev_1_0.xml#L314) | 0.0588507 / [input L314](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/g1_description/g1_29dof_with_hand_rev_1_0.xml#L314) |
| right_hand_index_1_link | 0.0203063 / [input L398](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_g1/g1_with_hands.xml#L398) | 0.0203063 / [input L319](https://github.com/unitreerobotics/unitree_ros/blob/adb48c7910ef8404ca34a07df95fc3acbb09f318/robots/g1_description/g1_29dof_with_hand_rev_1_0.xml#L319) | 0.0203063 / [input L319](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/g1_description/g1_29dof_with_hand_rev_1_0.xml#L319) |

## Coverage and unmatched elements

```json
{
  "mapping_h": {
    "bodies": {
      "pelvis": "pelvis",
      "left_hip_pitch_link": "left_hip_pitch_link",
      "left_hip_roll_link": "left_hip_roll_link",
      "left_hip_yaw_link": "left_hip_yaw_link",
      "left_knee_link": "left_knee_link",
      "left_ankle_pitch_link": "left_ankle_pitch_link",
      "left_ankle_roll_link": "left_ankle_roll_link",
      "right_hip_pitch_link": "right_hip_pitch_link",
      "right_hip_roll_link": "right_hip_roll_link",
      "right_hip_yaw_link": "right_hip_yaw_link",
      "right_knee_link": "right_knee_link",
      "right_ankle_pitch_link": "right_ankle_pitch_link",
      "right_ankle_roll_link": "right_ankle_roll_link",
      "waist_yaw_link": "waist_yaw_link",
      "waist_roll_link": "waist_roll_link",
      "torso_link": "torso_link",
      "left_shoulder_pitch_link": "left_shoulder_pitch_link",
      "left_shoulder_roll_link": "left_shoulder_roll_link",
      "left_shoulder_yaw_link": "left_shoulder_yaw_link",
      "left_elbow_link": "left_elbow_link",
      "left_wrist_roll_link": "left_wrist_roll_link",
      "left_wrist_pitch_link": "left_wrist_pitch_link",
      "left_wrist_yaw_link": "left_wrist_yaw_link",
      "left_hand_thumb_0_link": "left_hand_thumb_0_link",
      "left_hand_thumb_1_link": "left_hand_thumb_1_link",
      "left_hand_thumb_2_link": "left_hand_thumb_2_link",
      "left_hand_middle_0_link": "left_hand_middle_0_link",
      "left_hand_middle_1_link": "left_hand_middle_1_link",
      "left_hand_index_0_link": "left_hand_index_0_link",
      "left_hand_index_1_link": "left_hand_index_1_link",
      "right_shoulder_pitch_link": "right_shoulder_pitch_link",
      "right_shoulder_roll_link": "right_shoulder_roll_link",
      "right_shoulder_yaw_link": "right_shoulder_yaw_link",
      "right_elbow_link": "right_elbow_link",
      "right_wrist_roll_link": "right_wrist_roll_link",
      "right_wrist_pitch_link": "right_wrist_pitch_link",
      "right_wrist_yaw_link": "right_wrist_yaw_link",
      "right_hand_thumb_0_link": "right_hand_thumb_0_link",
      "right_hand_thumb_1_link": "right_hand_thumb_1_link",
      "right_hand_thumb_2_link": "right_hand_thumb_2_link",
      "right_hand_middle_0_link": "right_hand_middle_0_link",
      "right_hand_middle_1_link": "right_hand_middle_1_link",
      "right_hand_index_0_link": "right_hand_index_0_link",
      "right_hand_index_1_link": "right_hand_index_1_link"
    },
    "joints": {
      "left_hip_pitch_joint": "left_hip_pitch_joint",
      "left_hip_roll_joint": "left_hip_roll_joint",
      "left_hip_yaw_joint": "left_hip_yaw_joint",
      "left_knee_joint": "left_knee_joint",
      "left_ankle_pitch_joint": "left_ankle_pitch_joint",
      "left_ankle_roll_joint": "left_ankle_roll_joint",
      "right_hip_pitch_joint": "right_hip_pitch_joint",
      "right_hip_roll_joint": "right_hip_roll_joint",
      "right_hip_yaw_joint": "right_hip_yaw_joint",
      "right_knee_joint": "right_knee_joint",
      "right_ankle_pitch_joint": "right_ankle_pitch_joint",
      "right_ankle_roll_joint": "right_ankle_roll_joint",
      "waist_yaw_joint": "waist_yaw_joint",
      "waist_roll_joint": "waist_roll_joint",
      "waist_pitch_joint": "waist_pitch_joint",
      "left_shoulder_pitch_joint": "left_shoulder_pitch_joint",
      "left_shoulder_roll_joint": "left_shoulder_roll_joint",
      "left_shoulder_yaw_joint": "left_shoulder_yaw_joint",
      "left_elbow_joint": "left_elbow_joint",
      "left_wrist_roll_joint": "left_wrist_roll_joint",
      "left_wrist_pitch_joint": "left_wrist_pitch_joint",
      "left_wrist_yaw_joint": "left_wrist_yaw_joint",
      "left_hand_thumb_0_joint": "left_hand_thumb_0_joint",
      "left_hand_thumb_1_joint": "left_hand_thumb_1_joint",
      "left_hand_thumb_2_joint": "left_hand_thumb_2_joint",
      "left_hand_middle_0_joint": "left_hand_middle_0_joint",
      "left_hand_middle_1_joint": "left_hand_middle_1_joint",
      "left_hand_index_0_joint": "left_hand_index_0_joint",
      "left_hand_index_1_joint": "left_hand_index_1_joint",
      "right_shoulder_pitch_joint": "right_shoulder_pitch_joint",
      "right_shoulder_roll_joint": "right_shoulder_roll_joint",
      "right_shoulder_yaw_joint": "right_shoulder_yaw_joint",
      "right_elbow_joint": "right_elbow_joint",
      "right_wrist_roll_joint": "right_wrist_roll_joint",
      "right_wrist_pitch_joint": "right_wrist_pitch_joint",
      "right_wrist_yaw_joint": "right_wrist_yaw_joint",
      "right_hand_thumb_0_joint": "right_hand_thumb_0_joint",
      "right_hand_thumb_1_joint": "right_hand_thumb_1_joint",
      "right_hand_thumb_2_joint": "right_hand_thumb_2_joint",
      "right_hand_middle_0_joint": "right_hand_middle_0_joint",
      "right_hand_middle_1_joint": "right_hand_middle_1_joint",
      "right_hand_index_0_joint": "right_hand_index_0_joint",
      "right_hand_index_1_joint": "right_hand_index_1_joint"
    },
    "body_methods": {
      "pelvis": "name",
      "left_hip_pitch_link": "name",
      "left_hip_roll_link": "name",
      "left_hip_yaw_link": "name",
      "left_knee_link": "name",
      "left_ankle_pitch_link": "name",
      "left_ankle_roll_link": "name",
      "right_hip_pitch_link": "name",
      "right_hip_roll_link": "name",
      "right_hip_yaw_link": "name",
      "right_knee_link": "name",
      "right_ankle_pitch_link": "name",
      "right_ankle_roll_link": "name",
      "waist_yaw_link": "name",
      "waist_roll_link": "name",
      "torso_link": "name",
      "left_shoulder_pitch_link": "name",
      "left_shoulder_roll_link": "name",
      "left_shoulder_yaw_link": "name",
      "left_elbow_link": "name",
      "left_wrist_roll_link": "name",
      "left_wrist_pitch_link": "name",
      "left_wrist_yaw_link": "name",
      "left_hand_thumb_0_link": "name",
      "left_hand_thumb_1_link": "name",
      "left_hand_thumb_2_link": "name",
      "left_hand_middle_0_link": "name",
      "left_hand_middle_1_link": "name",
      "left_hand_index_0_link": "name",
      "left_hand_index_1_link": "name",
      "right_shoulder_pitch_link": "name",
      "right_shoulder_roll_link": "name",
      "right_shoulder_yaw_link": "name",
      "right_elbow_link": "name",
      "right_wrist_roll_link": "name",
      "right_wrist_pitch_link": "name",
      "right_wrist_yaw_link": "name",
      "right_hand_thumb_0_link": "name",
      "right_hand_thumb_1_link": "name",
      "right_hand_thumb_2_link": "name",
      "right_hand_middle_0_link": "name",
      "right_hand_middle_1_link": "name",
      "right_hand_index_0_link": "name",
      "right_hand_index_1_link": "name"
    },
    "joint_methods": {
      "left_hip_pitch_joint": "name",
      "left_hip_roll_joint": "name",
      "left_hip_yaw_joint": "name",
      "left_knee_joint": "name",
      "left_ankle_pitch_joint": "name",
      "left_ankle_roll_joint": "name",
      "right_hip_pitch_joint": "name",
      "right_hip_roll_joint": "name",
      "right_hip_yaw_joint": "name",
      "right_knee_joint": "name",
      "right_ankle_pitch_joint": "name",
      "right_ankle_roll_joint": "name",
      "waist_yaw_joint": "name",
      "waist_roll_joint": "name",
      "waist_pitch_joint": "name",
      "left_shoulder_pitch_joint": "name",
      "left_shoulder_roll_joint": "name",
      "left_shoulder_yaw_joint": "name",
      "left_elbow_joint": "name",
      "left_wrist_roll_joint": "name",
      "left_wrist_pitch_joint": "name",
      "left_wrist_yaw_joint": "name",
      "left_hand_thumb_0_joint": "name",
      "left_hand_thumb_1_joint": "name",
      "left_hand_thumb_2_joint": "name",
      "left_hand_middle_0_joint": "name",
      "left_hand_middle_1_joint": "name",
      "left_hand_index_0_joint": "name",
      "left_hand_index_1_joint": "name",
      "right_shoulder_pitch_joint": "name",
      "right_shoulder_roll_joint": "name",
      "right_shoulder_yaw_joint": "name",
      "right_elbow_joint": "name",
      "right_wrist_roll_joint": "name",
      "right_wrist_pitch_joint": "name",
      "right_wrist_yaw_joint": "name",
      "right_hand_thumb_0_joint": "name",
      "right_hand_thumb_1_joint": "name",
      "right_hand_thumb_2_joint": "name",
      "right_hand_middle_0_joint": "name",
      "right_hand_middle_1_joint": "name",
      "right_hand_index_0_joint": "name",
      "right_hand_index_1_joint": "name"
    },
    "unmatched_m_bodies": [],
    "unmatched_upstream_bodies": [],
    "unmatched_m_joints": [],
    "unmatched_upstream_joints": [],
    "registration_anchor": {
      "M": "pelvis",
      "H": "pelvis",
      "root_unmatched": false
    }
  },
  "mapping_s": {
    "bodies": {
      "pelvis": "pelvis",
      "left_hip_pitch_link": "left_hip_pitch_link",
      "left_hip_roll_link": "left_hip_roll_link",
      "left_hip_yaw_link": "left_hip_yaw_link",
      "left_knee_link": "left_knee_link",
      "left_ankle_pitch_link": "left_ankle_pitch_link",
      "left_ankle_roll_link": "left_ankle_roll_link",
      "right_hip_pitch_link": "right_hip_pitch_link",
      "right_hip_roll_link": "right_hip_roll_link",
      "right_hip_yaw_link": "right_hip_yaw_link",
      "right_knee_link": "right_knee_link",
      "right_ankle_pitch_link": "right_ankle_pitch_link",
      "right_ankle_roll_link": "right_ankle_roll_link",
      "waist_yaw_link": "waist_yaw_link",
      "waist_roll_link": "waist_roll_link",
      "torso_link": "torso_link",
      "left_shoulder_pitch_link": "left_shoulder_pitch_link",
      "left_shoulder_roll_link": "left_shoulder_roll_link",
      "left_shoulder_yaw_link": "left_shoulder_yaw_link",
      "left_elbow_link": "left_elbow_link",
      "left_wrist_roll_link": "left_wrist_roll_link",
      "left_wrist_pitch_link": "left_wrist_pitch_link",
      "left_wrist_yaw_link": "left_wrist_yaw_link",
      "left_hand_thumb_0_link": "left_hand_thumb_0_link",
      "left_hand_thumb_1_link": "left_hand_thumb_1_link",
      "left_hand_thumb_2_link": "left_hand_thumb_2_link",
      "left_hand_middle_0_link": "left_hand_middle_0_link",
      "left_hand_middle_1_link": "left_hand_middle_1_link",
      "left_hand_index_0_link": "left_hand_index_0_link",
      "left_hand_index_1_link": "left_hand_index_1_link",
      "right_shoulder_pitch_link": "right_shoulder_pitch_link",
      "right_shoulder_roll_link": "right_shoulder_roll_link",
      "right_shoulder_yaw_link": "right_shoulder_yaw_link",
      "right_elbow_link": "right_elbow_link",
      "right_wrist_roll_link": "right_wrist_roll_link",
      "right_wrist_pitch_link": "right_wrist_pitch_link",
      "right_wrist_yaw_link": "right_wrist_yaw_link",
      "right_hand_thumb_0_link": "right_hand_thumb_0_link",
      "right_hand_thumb_1_link": "right_hand_thumb_1_link",
      "right_hand_thumb_2_link": "right_hand_thumb_2_link",
      "right_hand_middle_0_link": "right_hand_middle_0_link",
      "right_hand_middle_1_link": "right_hand_middle_1_link",
      "right_hand_index_0_link": "right_hand_index_0_link",
      "right_hand_index_1_link": "right_hand_index_1_link"
    },
    "joints": {
      "left_hip_pitch_joint": "left_hip_pitch_joint",
      "left_hip_roll_joint": "left_hip_roll_joint",
      "left_hip_yaw_joint": "left_hip_yaw_joint",
      "left_knee_joint": "left_knee_joint",
      "left_ankle_pitch_joint": "left_ankle_pitch_joint",
      "left_ankle_roll_joint": "left_ankle_roll_joint",
      "right_hip_pitch_joint": "right_hip_pitch_joint",
      "right_hip_roll_joint": "right_hip_roll_joint",
      "right_hip_yaw_joint": "right_hip_yaw_joint",
      "right_knee_joint": "right_knee_joint",
      "right_ankle_pitch_joint": "right_ankle_pitch_joint",
      "right_ankle_roll_joint": "right_ankle_roll_joint",
      "waist_yaw_joint": "waist_yaw_joint",
      "waist_roll_joint": "waist_roll_joint",
      "waist_pitch_joint": "waist_pitch_joint",
      "left_shoulder_pitch_joint": "left_shoulder_pitch_joint",
      "left_shoulder_roll_joint": "left_shoulder_roll_joint",
      "left_shoulder_yaw_joint": "left_shoulder_yaw_joint",
      "left_elbow_joint": "left_elbow_joint",
      "left_wrist_roll_joint": "left_wrist_roll_joint",
      "left_wrist_pitch_joint": "left_wrist_pitch_joint",
      "left_wrist_yaw_joint": "left_wrist_yaw_joint",
      "left_hand_thumb_0_joint": "left_hand_thumb_0_joint",
      "left_hand_thumb_1_joint": "left_hand_thumb_1_joint",
      "left_hand_thumb_2_joint": "left_hand_thumb_2_joint",
      "left_hand_middle_0_joint": "left_hand_middle_0_joint",
      "left_hand_middle_1_joint": "left_hand_middle_1_joint",
      "left_hand_index_0_joint": "left_hand_index_0_joint",
      "left_hand_index_1_joint": "left_hand_index_1_joint",
      "right_shoulder_pitch_joint": "right_shoulder_pitch_joint",
      "right_shoulder_roll_joint": "right_shoulder_roll_joint",
      "right_shoulder_yaw_joint": "right_shoulder_yaw_joint",
      "right_elbow_joint": "right_elbow_joint",
      "right_wrist_roll_joint": "right_wrist_roll_joint",
      "right_wrist_pitch_joint": "right_wrist_pitch_joint",
      "right_wrist_yaw_joint": "right_wrist_yaw_joint",
      "right_hand_thumb_0_joint": "right_hand_thumb_0_joint",
      "right_hand_thumb_1_joint": "right_hand_thumb_1_joint",
      "right_hand_thumb_2_joint": "right_hand_thumb_2_joint",
      "right_hand_middle_0_joint": "right_hand_middle_0_joint",
      "right_hand_middle_1_joint": "right_hand_middle_1_joint",
      "right_hand_index_0_joint": "right_hand_index_0_joint",
      "right_hand_index_1_joint": "right_hand_index_1_joint"
    },
    "body_methods": {
      "pelvis": "name",
      "left_hip_pitch_link": "name",
      "left_hip_roll_link": "name",
      "left_hip_yaw_link": "name",
      "left_knee_link": "name",
      "left_ankle_pitch_link": "name",
      "left_ankle_roll_link": "name",
      "right_hip_pitch_link": "name",
      "right_hip_roll_link": "name",
      "right_hip_yaw_link": "name",
      "right_knee_link": "name",
      "right_ankle_pitch_link": "name",
      "right_ankle_roll_link": "name",
      "waist_yaw_link": "name",
      "waist_roll_link": "name",
      "torso_link": "name",
      "left_shoulder_pitch_link": "name",
      "left_shoulder_roll_link": "name",
      "left_shoulder_yaw_link": "name",
      "left_elbow_link": "name",
      "left_wrist_roll_link": "name",
      "left_wrist_pitch_link": "name",
      "left_wrist_yaw_link": "name",
      "left_hand_thumb_0_link": "name",
      "left_hand_thumb_1_link": "name",
      "left_hand_thumb_2_link": "name",
      "left_hand_middle_0_link": "name",
      "left_hand_middle_1_link": "name",
      "left_hand_index_0_link": "name",
      "left_hand_index_1_link": "name",
      "right_shoulder_pitch_link": "name",
      "right_shoulder_roll_link": "name",
      "right_shoulder_yaw_link": "name",
      "right_elbow_link": "name",
      "right_wrist_roll_link": "name",
      "right_wrist_pitch_link": "name",
      "right_wrist_yaw_link": "name",
      "right_hand_thumb_0_link": "name",
      "right_hand_thumb_1_link": "name",
      "right_hand_thumb_2_link": "name",
      "right_hand_middle_0_link": "name",
      "right_hand_middle_1_link": "name",
      "right_hand_index_0_link": "name",
      "right_hand_index_1_link": "name"
    },
    "joint_methods": {
      "left_hip_pitch_joint": "name",
      "left_hip_roll_joint": "name",
      "left_hip_yaw_joint": "name",
      "left_knee_joint": "name",
      "left_ankle_pitch_joint": "name",
      "left_ankle_roll_joint": "name",
      "right_hip_pitch_joint": "name",
      "right_hip_roll_joint": "name",
      "right_hip_yaw_joint": "name",
      "right_knee_joint": "name",
      "right_ankle_pitch_joint": "name",
      "right_ankle_roll_joint": "name",
      "waist_yaw_joint": "name",
      "waist_roll_joint": "name",
      "waist_pitch_joint": "name",
      "left_shoulder_pitch_joint": "name",
      "left_shoulder_roll_joint": "name",
      "left_shoulder_yaw_joint": "name",
      "left_elbow_joint": "name",
      "left_wrist_roll_joint": "name",
      "left_wrist_pitch_joint": "name",
      "left_wrist_yaw_joint": "name",
      "left_hand_thumb_0_joint": "name",
      "left_hand_thumb_1_joint": "name",
      "left_hand_thumb_2_joint": "name",
      "left_hand_middle_0_joint": "name",
      "left_hand_middle_1_joint": "name",
      "left_hand_index_0_joint": "name",
      "left_hand_index_1_joint": "name",
      "right_shoulder_pitch_joint": "name",
      "right_shoulder_roll_joint": "name",
      "right_shoulder_yaw_joint": "name",
      "right_elbow_joint": "name",
      "right_wrist_roll_joint": "name",
      "right_wrist_pitch_joint": "name",
      "right_wrist_yaw_joint": "name",
      "right_hand_thumb_0_joint": "name",
      "right_hand_thumb_1_joint": "name",
      "right_hand_thumb_2_joint": "name",
      "right_hand_middle_0_joint": "name",
      "right_hand_middle_1_joint": "name",
      "right_hand_index_0_joint": "name",
      "right_hand_index_1_joint": "name"
    },
    "unmatched_m_bodies": [],
    "unmatched_upstream_bodies": [],
    "unmatched_m_joints": [],
    "unmatched_upstream_joints": [],
    "registration_anchor": {
      "M": "pelvis",
      "S": "pelvis"
    }
  },
  "unavailable": [
    {
      "entity": "left_hip_pitch_joint",
      "other_entity": "left_hip_pitch_joint",
      "quantity": "effort",
      "tolerance": "limit",
      "m": 88.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_hip_pitch_joint",
      "other_entity": "left_hip_pitch_joint",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_hip_roll_joint",
      "other_entity": "left_hip_roll_joint",
      "quantity": "effort",
      "tolerance": "limit",
      "m": 139.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_hip_roll_joint",
      "other_entity": "left_hip_roll_joint",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_hip_yaw_joint",
      "other_entity": "left_hip_yaw_joint",
      "quantity": "effort",
      "tolerance": "limit",
      "m": 88.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_hip_yaw_joint",
      "other_entity": "left_hip_yaw_joint",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_knee_joint",
      "other_entity": "left_knee_joint",
      "quantity": "effort",
      "tolerance": "limit",
      "m": 139.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_knee_joint",
      "other_entity": "left_knee_joint",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_ankle_pitch_joint",
      "other_entity": "left_ankle_pitch_joint",
      "quantity": "effort",
      "tolerance": "limit",
      "m": 50.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_ankle_pitch_joint",
      "other_entity": "left_ankle_pitch_joint",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_ankle_roll_joint",
      "other_entity": "left_ankle_roll_joint",
      "quantity": "effort",
      "tolerance": "limit",
      "m": 50.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_ankle_roll_joint",
      "other_entity": "left_ankle_roll_joint",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "right_hip_pitch_joint",
      "other_entity": "right_hip_pitch_joint",
      "quantity": "effort",
      "tolerance": "limit",
      "m": 88.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "right_hip_pitch_joint",
      "other_entity": "right_hip_pitch_joint",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "right_hip_roll_joint",
      "other_entity": "right_hip_roll_joint",
      "quantity": "effort",
      "tolerance": "limit",
      "m": 139.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "right_hip_roll_joint",
      "other_entity": "right_hip_roll_joint",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "right_hip_yaw_joint",
      "other_entity": "right_hip_yaw_joint",
      "quantity": "effort",
      "tolerance": "limit",
      "m": 88.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "right_hip_yaw_joint",
      "other_entity": "right_hip_yaw_joint",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "right_knee_joint",
      "other_entity": "right_knee_joint",
      "quantity": "effort",
      "tolerance": "limit",
      "m": 139.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "right_knee_joint",
      "other_entity": "right_knee_joint",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "right_ankle_pitch_joint",
      "other_entity": "right_ankle_pitch_joint",
      "quantity": "effort",
      "tolerance": "limit",
      "m": 50.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "right_ankle_pitch_joint",
      "other_entity": "right_ankle_pitch_joint",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "right_ankle_roll_joint",
      "other_entity": "right_ankle_roll_joint",
      "quantity": "effort",
      "tolerance": "limit",
      "m": 50.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "right_ankle_roll_joint",
      "other_entity": "right_ankle_roll_joint",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "waist_yaw_joint",
      "other_entity": "waist_yaw_joint",
      "quantity": "effort",
      "tolerance": "limit",
      "m": 88.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "waist_yaw_joint",
      "other_entity": "waist_yaw_joint",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "waist_roll_joint",
      "other_entity": "waist_roll_joint",
      "quantity": "effort",
      "tolerance": "limit",
      "m": 50.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "waist_roll_joint",
      "other_entity": "waist_roll_joint",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "waist_pitch_joint",
      "other_entity": "waist_pitch_joint",
      "quantity": "effort",
      "tolerance": "limit",
      "m": 50.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "waist_pitch_joint",
      "other_entity": "waist_pitch_joint",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_shoulder_pitch_joint",
      "other_entity": "left_shoulder_pitch_joint",
      "quantity": "effort",
      "tolerance": "limit",
      "m": 25.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_shoulder_pitch_joint",
      "other_entity": "left_shoulder_pitch_joint",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_shoulder_roll_joint",
      "other_entity": "left_shoulder_roll_joint",
      "quantity": "effort",
      "tolerance": "limit",
      "m": 25.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_shoulder_roll_joint",
      "other_entity": "left_shoulder_roll_joint",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_shoulder_yaw_joint",
      "other_entity": "left_shoulder_yaw_joint",
      "quantity": "effort",
      "tolerance": "limit",
      "m": 25.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_shoulder_yaw_joint",
      "other_entity": "left_shoulder_yaw_joint",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_elbow_joint",
      "other_entity": "left_elbow_joint",
      "quantity": "effort",
      "tolerance": "limit",
      "m": 25.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_elbow_joint",
      "other_entity": "left_elbow_joint",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_wrist_roll_joint",
      "other_entity": "left_wrist_roll_joint",
      "quantity": "effort",
      "tolerance": "limit",
      "m": 25.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_wrist_roll_joint",
      "other_entity": "left_wrist_roll_joint",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_wrist_pitch_joint",
      "other_entity": "left_wrist_pitch_joint",
      "quantity": "effort",
      "tolerance": "limit",
      "m": 5.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_wrist_pitch_joint",
      "other_entity": "left_wrist_pitch_joint",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_wrist_yaw_joint",
      "other_entity": "left_wrist_yaw_joint",
      "quantity": "effort",
      "tolerance": "limit",
      "m": 5.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_wrist_yaw_joint",
      "other_entity": "left_wrist_yaw_joint",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_hand_thumb_0_joint",
      "other_entity": "left_hand_thumb_0_joint",
      "quantity": "effort",
      "tolerance": "limit",
      "m": 2.45,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_hand_thumb_0_joint",
      "other_entity": "left_hand_thumb_0_joint",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_hand_thumb_1_joint",
      "other_entity": "left_hand_thumb_1_joint",
      "quantity": "effort",
      "tolerance": "limit",
      "m": 1.4,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_hand_thumb_1_joint",
      "other_entity": "left_hand_thumb_1_joint",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_hand_thumb_2_joint",
      "other_entity": "left_hand_thumb_2_joint",
      "quantity": "effort",
      "tolerance": "limit",
      "m": 1.4,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_hand_thumb_2_joint",
      "other_entity": "left_hand_thumb_2_joint",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_hand_middle_0_joint",
      "other_entity": "left_hand_middle_0_joint",
      "quantity": "effort",
      "tolerance": "limit",
      "m": 1.4,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_hand_middle_0_joint",
      "other_entity": "left_hand_middle_0_joint",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_hand_middle_1_joint",
      "other_entity": "left_hand_middle_1_joint",
      "quantity": "effort",
      "tolerance": "limit",
      "m": 1.4,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_hand_middle_1_joint",
      "other_entity": "left_hand_middle_1_joint",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_hand_index_0_joint",
      "other_entity": "left_hand_index_0_joint",
      "quantity": "effort",
      "tolerance": "limit",
      "m": 1.4,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_hand_index_0_joint",
      "other_entity": "left_hand_index_0_joint",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_hand_index_1_joint",
      "other_entity": "left_hand_index_1_joint",
      "quantity": "effort",
      "tolerance": "limit",
      "m": 1.4,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_hand_index_1_joint",
      "other_entity": "left_hand_index_1_joint",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "right_shoulder_pitch_joint",
      "other_entity": "right_shoulder_pitch_joint",
      "quantity": "effort",
      "tolerance": "limit",
      "m": 25.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "right_shoulder_pitch_joint",
      "other_entity": "right_shoulder_pitch_joint",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "right_shoulder_roll_joint",
      "other_entity": "right_shoulder_roll_joint",
      "quantity": "effort",
      "tolerance": "limit",
      "m": 25.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "right_shoulder_roll_joint",
      "other_entity": "right_shoulder_roll_joint",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "right_shoulder_yaw_joint",
      "other_entity": "right_shoulder_yaw_joint",
      "quantity": "effort",
      "tolerance": "limit",
      "m": 25.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "right_shoulder_yaw_joint",
      "other_entity": "right_shoulder_yaw_joint",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "right_elbow_joint",
      "other_entity": "right_elbow_joint",
      "quantity": "effort",
      "tolerance": "limit",
      "m": 25.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "right_elbow_joint",
      "other_entity": "right_elbow_joint",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "right_wrist_roll_joint",
      "other_entity": "right_wrist_roll_joint",
      "quantity": "effort",
      "tolerance": "limit",
      "m": 25.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "right_wrist_roll_joint",
      "other_entity": "right_wrist_roll_joint",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "right_wrist_pitch_joint",
      "other_entity": "right_wrist_pitch_joint",
      "quantity": "effort",
      "tolerance": "limit",
      "m": 5.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "right_wrist_pitch_joint",
      "other_entity": "right_wrist_pitch_joint",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "right_wrist_yaw_joint",
      "other_entity": "right_wrist_yaw_joint",
      "quantity": "effort",
      "tolerance": "limit",
      "m": 5.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "right_wrist_yaw_joint",
      "other_entity": "right_wrist_yaw_joint",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "right_hand_thumb_0_joint",
      "other_entity": "right_hand_thumb_0_joint",
      "quantity": "effort",
      "tolerance": "limit",
      "m": 2.45,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "right_hand_thumb_0_joint",
      "other_entity": "right_hand_thumb_0_joint",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "right_hand_thumb_1_joint",
      "other_entity": "right_hand_thumb_1_joint",
      "quantity": "effort",
      "tolerance": "limit",
      "m": 1.4,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "right_hand_thumb_1_joint",
      "other_entity": "right_hand_thumb_1_joint",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "right_hand_thumb_2_joint",
      "other_entity": "right_hand_thumb_2_joint",
      "quantity": "effort",
      "tolerance": "limit",
      "m": 1.4,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "right_hand_thumb_2_joint",
      "other_entity": "right_hand_thumb_2_joint",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "right_hand_middle_0_joint",
      "other_entity": "right_hand_middle_0_joint",
      "quantity": "effort",
      "tolerance": "limit",
      "m": 1.4,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "right_hand_middle_0_joint",
      "other_entity": "right_hand_middle_0_joint",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "right_hand_middle_1_joint",
      "other_entity": "right_hand_middle_1_joint",
      "quantity": "effort",
      "tolerance": "limit",
      "m": 1.4,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "right_hand_middle_1_joint",
      "other_entity": "right_hand_middle_1_joint",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "right_hand_index_0_joint",
      "other_entity": "right_hand_index_0_joint",
      "quantity": "effort",
      "tolerance": "limit",
      "m": 1.4,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "right_hand_index_0_joint",
      "other_entity": "right_hand_index_0_joint",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "right_hand_index_1_joint",
      "other_entity": "right_hand_index_1_joint",
      "quantity": "effort",
      "tolerance": "limit",
      "m": 1.4,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "right_hand_index_1_joint",
      "other_entity": "right_hand_index_1_joint",
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
| left_hip_pitch_joint / effort | 88 | unavailable | unavailable |
| left_hip_pitch_joint / velocity | unavailable | unavailable | unavailable |
| left_hip_roll_joint / effort | 139 | unavailable | unavailable |
| left_hip_roll_joint / velocity | unavailable | unavailable | unavailable |
| left_hip_yaw_joint / effort | 88 | unavailable | unavailable |
| left_hip_yaw_joint / velocity | unavailable | unavailable | unavailable |
| left_knee_joint / effort | 139 | unavailable | unavailable |
| left_knee_joint / velocity | unavailable | unavailable | unavailable |
| left_ankle_pitch_joint / effort | 50 | unavailable | unavailable |
| left_ankle_pitch_joint / velocity | unavailable | unavailable | unavailable |
| left_ankle_roll_joint / effort | 50 | unavailable | unavailable |
| left_ankle_roll_joint / velocity | unavailable | unavailable | unavailable |
| right_hip_pitch_joint / effort | 88 | unavailable | unavailable |
| right_hip_pitch_joint / velocity | unavailable | unavailable | unavailable |
| right_hip_roll_joint / effort | 139 | unavailable | unavailable |
| right_hip_roll_joint / velocity | unavailable | unavailable | unavailable |
| right_hip_yaw_joint / effort | 88 | unavailable | unavailable |
| right_hip_yaw_joint / velocity | unavailable | unavailable | unavailable |
| right_knee_joint / effort | 139 | unavailable | unavailable |
| right_knee_joint / velocity | unavailable | unavailable | unavailable |
| right_ankle_pitch_joint / effort | 50 | unavailable | unavailable |
| right_ankle_pitch_joint / velocity | unavailable | unavailable | unavailable |
| right_ankle_roll_joint / effort | 50 | unavailable | unavailable |
| right_ankle_roll_joint / velocity | unavailable | unavailable | unavailable |
| waist_yaw_joint / effort | 88 | unavailable | unavailable |
| waist_yaw_joint / velocity | unavailable | unavailable | unavailable |
| waist_roll_joint / effort | 50 | unavailable | unavailable |
| waist_roll_joint / velocity | unavailable | unavailable | unavailable |
| waist_pitch_joint / effort | 50 | unavailable | unavailable |
| waist_pitch_joint / velocity | unavailable | unavailable | unavailable |
| left_shoulder_pitch_joint / effort | 25 | unavailable | unavailable |
| left_shoulder_pitch_joint / velocity | unavailable | unavailable | unavailable |
| left_shoulder_roll_joint / effort | 25 | unavailable | unavailable |
| left_shoulder_roll_joint / velocity | unavailable | unavailable | unavailable |
| left_shoulder_yaw_joint / effort | 25 | unavailable | unavailable |
| left_shoulder_yaw_joint / velocity | unavailable | unavailable | unavailable |
| left_elbow_joint / effort | 25 | unavailable | unavailable |
| left_elbow_joint / velocity | unavailable | unavailable | unavailable |
| left_wrist_roll_joint / effort | 25 | unavailable | unavailable |
| left_wrist_roll_joint / velocity | unavailable | unavailable | unavailable |
| left_wrist_pitch_joint / effort | 5 | unavailable | unavailable |
| left_wrist_pitch_joint / velocity | unavailable | unavailable | unavailable |
| left_wrist_yaw_joint / effort | 5 | unavailable | unavailable |
| left_wrist_yaw_joint / velocity | unavailable | unavailable | unavailable |
| left_hand_thumb_0_joint / effort | 2.45 | unavailable | unavailable |
| left_hand_thumb_0_joint / velocity | unavailable | unavailable | unavailable |
| left_hand_thumb_1_joint / effort | 1.4 | unavailable | unavailable |
| left_hand_thumb_1_joint / velocity | unavailable | unavailable | unavailable |
| left_hand_thumb_2_joint / effort | 1.4 | unavailable | unavailable |
| left_hand_thumb_2_joint / velocity | unavailable | unavailable | unavailable |
| left_hand_middle_0_joint / effort | 1.4 | unavailable | unavailable |
| left_hand_middle_0_joint / velocity | unavailable | unavailable | unavailable |
| left_hand_middle_1_joint / effort | 1.4 | unavailable | unavailable |
| left_hand_middle_1_joint / velocity | unavailable | unavailable | unavailable |
| left_hand_index_0_joint / effort | 1.4 | unavailable | unavailable |
| left_hand_index_0_joint / velocity | unavailable | unavailable | unavailable |
| left_hand_index_1_joint / effort | 1.4 | unavailable | unavailable |
| left_hand_index_1_joint / velocity | unavailable | unavailable | unavailable |
| right_shoulder_pitch_joint / effort | 25 | unavailable | unavailable |
| right_shoulder_pitch_joint / velocity | unavailable | unavailable | unavailable |
| right_shoulder_roll_joint / effort | 25 | unavailable | unavailable |
| right_shoulder_roll_joint / velocity | unavailable | unavailable | unavailable |
| right_shoulder_yaw_joint / effort | 25 | unavailable | unavailable |
| right_shoulder_yaw_joint / velocity | unavailable | unavailable | unavailable |
| right_elbow_joint / effort | 25 | unavailable | unavailable |
| right_elbow_joint / velocity | unavailable | unavailable | unavailable |
| right_wrist_roll_joint / effort | 25 | unavailable | unavailable |
| right_wrist_roll_joint / velocity | unavailable | unavailable | unavailable |
| right_wrist_pitch_joint / effort | 5 | unavailable | unavailable |
| right_wrist_pitch_joint / velocity | unavailable | unavailable | unavailable |
| right_wrist_yaw_joint / effort | 5 | unavailable | unavailable |
| right_wrist_yaw_joint / velocity | unavailable | unavailable | unavailable |
| right_hand_thumb_0_joint / effort | 2.45 | unavailable | unavailable |
| right_hand_thumb_0_joint / velocity | unavailable | unavailable | unavailable |
| right_hand_thumb_1_joint / effort | 1.4 | unavailable | unavailable |
| right_hand_thumb_1_joint / velocity | unavailable | unavailable | unavailable |
| right_hand_thumb_2_joint / effort | 1.4 | unavailable | unavailable |
| right_hand_thumb_2_joint / velocity | unavailable | unavailable | unavailable |
| right_hand_middle_0_joint / effort | 1.4 | unavailable | unavailable |
| right_hand_middle_0_joint / velocity | unavailable | unavailable | unavailable |
| right_hand_middle_1_joint / effort | 1.4 | unavailable | unavailable |
| right_hand_middle_1_joint / velocity | unavailable | unavailable | unavailable |
| right_hand_index_0_joint / effort | 1.4 | unavailable | unavailable |
| right_hand_index_0_joint / velocity | unavailable | unavailable | unavailable |
| right_hand_index_1_joint / effort | 1.4 | unavailable | unavailable |
| right_hand_index_1_joint / velocity | unavailable | unavailable | unavailable |
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
  "https://github.com/unitreerobotics/unitree_ros robots/g1_description/g1_pl.urdf at 157ff950351e5f535e03c5d85a16b7d594b3dbcc: ValueError: Resource missing at 157ff950351e5f535e03c5d85a16b7d594b3dbcc: robots/g1_description/meshes/meshes/pelvis_ver0529.STL",
  "https://github.com/unitreerobotics/unitree_ros robots/g1_description/g1_comp.urdf at 157ff950351e5f535e03c5d85a16b7d594b3dbcc: ValueError: Resource missing at 157ff950351e5f535e03c5d85a16b7d594b3dbcc: robots/g1_description/meshes/meshes/pelvis.STL",
  "https://github.com/unitreerobotics/unitree_ros robots/g1_description/g1_23dof.urdf at 157ff950351e5f535e03c5d85a16b7d594b3dbcc: ValueError: Resource missing at 157ff950351e5f535e03c5d85a16b7d594b3dbcc: robots/g1_description/meshes/meshes/pelvis.STL",
  "https://github.com/unitreerobotics/unitree_ros robots/g1_description/g1_29dof.urdf at 157ff950351e5f535e03c5d85a16b7d594b3dbcc: ValueError: Resource missing at 157ff950351e5f535e03c5d85a16b7d594b3dbcc: robots/g1_description/meshes/meshes/pelvis.STL",
  "https://github.com/unitreerobotics/unitree_ros robots/g1_description/g1_dual_arm.urdf at 157ff950351e5f535e03c5d85a16b7d594b3dbcc: ValueError: Resource missing at 157ff950351e5f535e03c5d85a16b7d594b3dbcc: robots/g1_description/meshes/meshes/waist_yaw_link.STL",
  "https://github.com/unitreerobotics/unitree_ros robots/g1_description/g1_23dof_mode_10.urdf at 157ff950351e5f535e03c5d85a16b7d594b3dbcc: ValueError: Resource missing at 157ff950351e5f535e03c5d85a16b7d594b3dbcc: robots/g1_description/meshes/meshes/pelvis_ver0529.STL",
  "https://github.com/unitreerobotics/unitree_ros robots/g1_description/g1_23dof_rev_1_0.urdf at 157ff950351e5f535e03c5d85a16b7d594b3dbcc: ValueError: Resource missing at 157ff950351e5f535e03c5d85a16b7d594b3dbcc: robots/g1_description/meshes/meshes/pelvis.STL",
  "https://github.com/unitreerobotics/unitree_ros robots/g1_description/g1_29dof_mode_11.urdf at 157ff950351e5f535e03c5d85a16b7d594b3dbcc: ValueError: Resource missing at 157ff950351e5f535e03c5d85a16b7d594b3dbcc: robots/g1_description/meshes/meshes/pelvis_ver0529.STL",
  "https://github.com/unitreerobotics/unitree_ros robots/g1_description/g1_29dof_mode_12.urdf at 157ff950351e5f535e03c5d85a16b7d594b3dbcc: ValueError: Resource missing at 157ff950351e5f535e03c5d85a16b7d594b3dbcc: robots/g1_description/meshes/meshes/pelvis_ver0529.STL",
  "https://github.com/unitreerobotics/unitree_ros robots/g1_description/g1_29dof_mode_13.urdf at 157ff950351e5f535e03c5d85a16b7d594b3dbcc: ValueError: Resource missing at 157ff950351e5f535e03c5d85a16b7d594b3dbcc: robots/g1_description/meshes/meshes/pelvis.STL",
  "https://github.com/unitreerobotics/unitree_ros robots/g1_description/g1_29dof_mode_14.urdf at 157ff950351e5f535e03c5d85a16b7d594b3dbcc: ValueError: Resource missing at 157ff950351e5f535e03c5d85a16b7d594b3dbcc: robots/g1_description/meshes/meshes/pelvis.STL",
  "https://github.com/unitreerobotics/unitree_ros robots/g1_description/g1_29dof_mode_15.urdf at 157ff950351e5f535e03c5d85a16b7d594b3dbcc: ValueError: Resource missing at 157ff950351e5f535e03c5d85a16b7d594b3dbcc: robots/g1_description/meshes/meshes/pelvis_ver0529.STL",
  "https://github.com/unitreerobotics/unitree_ros robots/g1_description/g1_29dof_mode_16.urdf at 157ff950351e5f535e03c5d85a16b7d594b3dbcc: ValueError: Resource missing at 157ff950351e5f535e03c5d85a16b7d594b3dbcc: robots/g1_description/meshes/meshes/pelvis_ver0529.STL",
  "https://github.com/unitreerobotics/unitree_ros robots/g1_description/g1_29dof_mode_18.urdf at 157ff950351e5f535e03c5d85a16b7d594b3dbcc: ValueError: Resource missing at 157ff950351e5f535e03c5d85a16b7d594b3dbcc: robots/g1_description/meshes/meshes/pelvis_ver0529.STL",
  "https://github.com/unitreerobotics/unitree_ros robots/g1_description/g1_29dof_rev_1_0.urdf at 157ff950351e5f535e03c5d85a16b7d594b3dbcc: ValueError: Resource missing at 157ff950351e5f535e03c5d85a16b7d594b3dbcc: robots/g1_description/meshes/meshes/pelvis.STL",
  "https://github.com/unitreerobotics/unitree_ros robots/g1_description/g1_29dof_with_hand.urdf at 157ff950351e5f535e03c5d85a16b7d594b3dbcc: ValueError: Resource missing at 157ff950351e5f535e03c5d85a16b7d594b3dbcc: robots/g1_description/meshes/meshes/pelvis.STL",
  "https://github.com/unitreerobotics/unitree_ros robots/g1_description/g1_29dof_lock_waist.urdf at 157ff950351e5f535e03c5d85a16b7d594b3dbcc: ValueError: Resource missing at 157ff950351e5f535e03c5d85a16b7d594b3dbcc: robots/g1_description/meshes/meshes/pelvis.STL",
  "https://github.com/unitreerobotics/unitree_ros robots/g1_description/g1_29dof_with_hand_rev_1_0.urdf at 157ff950351e5f535e03c5d85a16b7d594b3dbcc: ValueError: Resource missing at 157ff950351e5f535e03c5d85a16b7d594b3dbcc: robots/g1_description/meshes/meshes/pelvis.STL",
  "https://github.com/unitreerobotics/unitree_ros robots/g1_description/inspire_hand/DFQ_left_hand.urdf at 157ff950351e5f535e03c5d85a16b7d594b3dbcc: ValueError: Resource missing at 157ff950351e5f535e03c5d85a16b7d594b3dbcc: robots/g1_description/inspire_hand/meshes/meshes/L_hand_base_link.STL",
  "https://github.com/unitreerobotics/unitree_ros robots/g1_description/inspire_hand/FTP_left_hand.urdf at 157ff950351e5f535e03c5d85a16b7d594b3dbcc: ValueError: Resource missing at 157ff950351e5f535e03c5d85a16b7d594b3dbcc: robots/g1_description/inspire_hand/meshes/meshes/left_base_link.STL",
  "https://github.com/unitreerobotics/unitree_ros robots/g1_description/g1_29dof_lock_waist_rev_1_0.urdf at 157ff950351e5f535e03c5d85a16b7d594b3dbcc: ValueError: Resource missing at 157ff950351e5f535e03c5d85a16b7d594b3dbcc: robots/g1_description/meshes/meshes/pelvis.STL",
  "https://github.com/unitreerobotics/unitree_ros robots/g1_description/inspire_hand/DFQ_right_hand.urdf at 157ff950351e5f535e03c5d85a16b7d594b3dbcc: ValueError: Resource missing at 157ff950351e5f535e03c5d85a16b7d594b3dbcc: robots/g1_description/inspire_hand/meshes/meshes/R_hand_base_link.STL",
  "https://github.com/unitreerobotics/unitree_ros robots/g1_description/inspire_hand/FTP_right_hand.urdf at 157ff950351e5f535e03c5d85a16b7d594b3dbcc: ValueError: Resource missing at 157ff950351e5f535e03c5d85a16b7d594b3dbcc: robots/g1_description/inspire_hand/meshes/meshes/right_base_link.STL",
  "https://github.com/unitreerobotics/unitree_ros robots/g1_description/g1_29dof_mode_15_with_dex1_1.urdf at 157ff950351e5f535e03c5d85a16b7d594b3dbcc: ValueError: Resource missing at 157ff950351e5f535e03c5d85a16b7d594b3dbcc: robots/g1_description/meshes/meshes/pelvis_ver0529.STL",
  "https://github.com/unitreerobotics/unitree_ros robots/g1_description/g1_29dof_lock_waist_with_hand_rev_1_0.urdf at 157ff950351e5f535e03c5d85a16b7d594b3dbcc: ValueError: Resource missing at 157ff950351e5f535e03c5d85a16b7d594b3dbcc: robots/g1_description/meshes/meshes/pelvis.STL",
  "https://github.com/unitreerobotics/unitree_ros robots/g1_description/g1_29dof_rev_1_0_with_inspire_hand_DFQ.urdf at 157ff950351e5f535e03c5d85a16b7d594b3dbcc: ValueError: Resource missing at 157ff950351e5f535e03c5d85a16b7d594b3dbcc: robots/g1_description/meshes/meshes/pelvis.STL",
  "https://github.com/unitreerobotics/unitree_ros robots/g1_description/g1_29dof_rev_1_0_with_inspire_hand_FTP.urdf at 157ff950351e5f535e03c5d85a16b7d594b3dbcc: ValueError: Resource missing at 157ff950351e5f535e03c5d85a16b7d594b3dbcc: robots/g1_description/meshes/meshes/pelvis.STL"
]
```

## Self comparisons

```json
[
  {
    "file": "unitree_g1/g1.xml",
    "status": "passed",
    "findings": 0
  },
  {
    "file": "unitree_g1/g1_mjlab.xml",
    "status": "passed",
    "findings": 0
  },
  {
    "file": "unitree_g1/g1_mjx.xml",
    "status": "passed",
    "findings": 0
  },
  {
    "file": "unitree_g1/g1_with_hands.xml",
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
        0.793
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
        0.793
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
        0.793
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
  "self_variants_recompiled": 4,
  "historical_snapshots_reused": 3,
  "primary_physics_unchanged": true,
  "source_matching": "original raw-value provenance criteria retained; kinematic guard applies to reported CoM"
}
```
