# toddlerbot_2xc

Status: **complete**. Provenance: **dated match**, confidence **medium**.

Source selected using the ordered amended provenance rules.

M: `https://github.com/google-deepmind/mujoco_menagerie`, `toddlerbot_2xc/toddlerbot_2xc.xml`, commit `370c43965323c0944b433b202aac5058b5f907a9`.
H: `https://github.com/hshi74/toddlerbot`, `toddlerbot/descriptions/toddlerbot_2xc/toddlerbot_2xc.xml`, commit `e337f3b177b4b53abff70b31d1695a7b66cc6d2e`.
S: `957aadb8e6db85e02fbb9ef90bbcdb4b4c0c9f6c` (2025-08-29T22:11:17-04:00). Menagerie release/change: 2025-08-29T22:32:48-04:00.

Limit semantics: MJCF effort values are supported actuator torque/force envelopes. URDF effort and velocity values are manufacturer declarations retained from XML; MuJoCo does not enforce those tags. Such declaration comparisons are explicitly distinct from compiled inertial/range quantities.


## Source evidence

```json
[
  {
    "url": "https://github.com/hshi74/toddlerbot",
    "document": "toddlerbot_2xc/README.md",
    "commit": "370c43965323c0944b433b202aac5058b5f907a9",
    "current": true
  }
]
```


## Kinematics consistency

A proper Kabsch rigid transform aligns all matched zero-pose body origins. The maximum per-origin residual and signed hinge/slide axis angles determine whether CoM can be compared; RMS is also recorded. Fewer than three non-collinear origins give insufficient kinematic coverage. CoM records that fail either required M/H or M/S check are excluded from counts and largest discrepancies. Masses, principal moments and raw joint ranges remain unchanged; a flagged range still requires convention review.

| Pair | Status | Origins / rank | RMS / maximum mm | Disagreeing / checked axes |
|---|---|---:|---:|---:|
| M/H | consistent | 45 / 3 | 4.46319846e-14 / 7.40871132e-14 | 0 / 44 |
| M/S | consistent | 45 / 3 | 4.46319846e-14 / 7.40871132e-14 | 0 / 44 |

Exact fitted transforms, per-origin residuals, thresholds and axis vectors:

```json
{
  "M/H": {
    "status": "consistent",
    "matched_body_origins": 45,
    "position_threshold_m": 0.005,
    "axis_threshold_rad": 0.005,
    "residual_definition": "maximum Euclidean residual over matched body origins; Kabsch minimizes RMS, which is also recorded",
    "coordinate_frames": "each snapshot registered to its matched report anchor",
    "anchor_m": "torso",
    "anchor_other": "torso",
    "rotation_other_to_m": [
      [
        1.0000000000000002,
        -4.001311601733842e-16,
        -1.5448775328874618e-16
      ],
      [
        1.8445917450672793e-16,
        0.9999999999999999,
        9.913453007809916e-18
      ],
      [
        1.491862189340054e-16,
        4.217546450968612e-17,
        0.9999999999999998
      ]
    ],
    "translation_other_to_m": [
      0.0,
      3.754050022231059e-18,
      -3.469446951953614e-18
    ],
    "rms_residual_m": 4.4631984569332215e-17,
    "max_residual_m": 7.408711319456051e-17,
    "fit_rank": 3,
    "axis_checks": [
      {
        "joint_m": "neck_yaw_drive",
        "joint_other": "neck_yaw_drive",
        "axis_m": [
          0.0,
          0.0,
          -1.0
        ],
        "axis_other_aligned": [
          1.544877532887462e-16,
          -9.913453007809917e-18,
          -1.0
        ],
        "angle_rad": 1.5480549882592209e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "neck_yaw_driven",
        "joint_other": "neck_yaw_driven",
        "axis_m": [
          0.0,
          0.0,
          1.0
        ],
        "axis_other_aligned": [
          -1.544877532887462e-16,
          9.913453007809917e-18,
          1.0
        ],
        "angle_rad": 1.5480549882592209e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "neck_pitch",
        "joint_other": "neck_pitch",
        "axis_m": [
          0.0,
          1.0,
          0.0
        ],
        "axis_other_aligned": [
          -4.0013116017338423e-16,
          1.0,
          4.217546450968613e-17
        ],
        "angle_rad": 4.023477539993311e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "neck_pitch_act",
        "joint_other": "neck_pitch_act",
        "axis_m": [
          0.0,
          -1.0,
          0.0
        ],
        "axis_other_aligned": [
          4.0013116017338423e-16,
          -1.0,
          -4.217546450968613e-17
        ],
        "angle_rad": 4.023477539993311e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "neck_pitch_front",
        "joint_other": "neck_pitch_front",
        "axis_m": [
          0.0,
          -1.0,
          0.0
        ],
        "axis_other_aligned": [
          4.0013116017338423e-16,
          -1.0,
          -4.217546450968613e-17
        ],
        "angle_rad": 4.023477539993311e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "neck_pitch_back",
        "joint_other": "neck_pitch_back",
        "axis_m": [
          0.0,
          -1.0,
          0.0
        ],
        "axis_other_aligned": [
          4.0013116017338423e-16,
          -1.0,
          -4.217546450968613e-17
        ],
        "angle_rad": 4.023477539993311e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "waist_yaw",
        "joint_other": "waist_yaw",
        "axis_m": [
          0.0,
          0.0,
          1.0
        ],
        "axis_other_aligned": [
          -1.544877532887462e-16,
          9.913453007809917e-18,
          1.0
        ],
        "angle_rad": 1.5480549882592209e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "waist_roll",
        "joint_other": "waist_roll",
        "axis_m": [
          1.0,
          0.0,
          0.0
        ],
        "axis_other_aligned": [
          1.0,
          1.8445917450672788e-16,
          1.4918621893400539e-16
        ],
        "angle_rad": 2.372376761383581e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "waist_act_1",
        "joint_other": "waist_act_1",
        "axis_m": [
          0.0,
          0.0,
          1.0
        ],
        "axis_other_aligned": [
          -1.544877532887462e-16,
          9.913453007809917e-18,
          1.0
        ],
        "angle_rad": 1.5480549882592209e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "waist_act_2",
        "joint_other": "waist_act_2",
        "axis_m": [
          0.0,
          0.0,
          1.0
        ],
        "axis_other_aligned": [
          -1.544877532887462e-16,
          9.913453007809917e-18,
          1.0
        ],
        "angle_rad": 1.5480549882592209e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "left_hip_pitch",
        "joint_other": "left_hip_pitch",
        "axis_m": [
          0.0,
          1.0,
          0.0
        ],
        "axis_other_aligned": [
          -4.0013116017338423e-16,
          1.0,
          4.217546450968613e-17
        ],
        "angle_rad": 4.023477539993311e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "left_hip_roll",
        "joint_other": "left_hip_roll",
        "axis_m": [
          1.0,
          0.0,
          0.0
        ],
        "axis_other_aligned": [
          1.0,
          1.8445917450672788e-16,
          1.4918621893400539e-16
        ],
        "angle_rad": 2.372376761383581e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "left_hip_yaw_driven",
        "joint_other": "left_hip_yaw_driven",
        "axis_m": [
          0.0,
          0.0,
          -1.0
        ],
        "axis_other_aligned": [
          1.544877532887462e-16,
          -9.913453007809917e-18,
          -1.0
        ],
        "angle_rad": 1.5480549882592209e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "left_hip_yaw_drive",
        "joint_other": "left_hip_yaw_drive",
        "axis_m": [
          0.0,
          0.0,
          1.0
        ],
        "axis_other_aligned": [
          -1.544877532887462e-16,
          9.913453007809917e-18,
          1.0
        ],
        "angle_rad": 1.5480549882592209e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "left_knee",
        "joint_other": "left_knee",
        "axis_m": [
          0.0,
          -1.0,
          0.0
        ],
        "axis_other_aligned": [
          4.0013116017338423e-16,
          -1.0,
          -4.217546450968613e-17
        ],
        "angle_rad": 4.023477539993311e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "left_ankle_pitch",
        "joint_other": "left_ankle_pitch",
        "axis_m": [
          0.0,
          1.0,
          0.0
        ],
        "axis_other_aligned": [
          -4.0013116017338423e-16,
          1.0,
          4.217546450968613e-17
        ],
        "angle_rad": 4.023477539993311e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "left_ankle_roll",
        "joint_other": "left_ankle_roll",
        "axis_m": [
          1.0,
          0.0,
          0.0
        ],
        "axis_other_aligned": [
          1.0,
          1.8445917450672788e-16,
          1.4918621893400539e-16
        ],
        "angle_rad": 2.372376761383581e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "right_hip_pitch",
        "joint_other": "right_hip_pitch",
        "axis_m": [
          0.0,
          -1.0,
          0.0
        ],
        "axis_other_aligned": [
          4.0013116017338423e-16,
          -1.0,
          -4.217546450968613e-17
        ],
        "angle_rad": 4.023477539993311e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "right_hip_roll",
        "joint_other": "right_hip_roll",
        "axis_m": [
          -1.0,
          0.0,
          0.0
        ],
        "axis_other_aligned": [
          -1.0,
          -1.8445917450672788e-16,
          -1.4918621893400539e-16
        ],
        "angle_rad": 2.372376761383581e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "right_hip_yaw_driven",
        "joint_other": "right_hip_yaw_driven",
        "axis_m": [
          0.0,
          0.0,
          -1.0
        ],
        "axis_other_aligned": [
          1.544877532887462e-16,
          -9.913453007809917e-18,
          -1.0
        ],
        "angle_rad": 1.5480549882592209e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "right_hip_yaw_drive",
        "joint_other": "right_hip_yaw_drive",
        "axis_m": [
          0.0,
          0.0,
          1.0
        ],
        "axis_other_aligned": [
          -1.544877532887462e-16,
          9.913453007809917e-18,
          1.0
        ],
        "angle_rad": 1.5480549882592209e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "right_knee",
        "joint_other": "right_knee",
        "axis_m": [
          0.0,
          1.0,
          0.0
        ],
        "axis_other_aligned": [
          -4.0013116017338423e-16,
          1.0,
          4.217546450968613e-17
        ],
        "angle_rad": 4.023477539993311e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "right_ankle_pitch",
        "joint_other": "right_ankle_pitch",
        "axis_m": [
          0.0,
          -1.0,
          0.0
        ],
        "axis_other_aligned": [
          4.0013116017338423e-16,
          -1.0,
          -4.217546450968613e-17
        ],
        "angle_rad": 4.023477539993311e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "right_ankle_roll",
        "joint_other": "right_ankle_roll",
        "axis_m": [
          1.0,
          0.0,
          0.0
        ],
        "axis_other_aligned": [
          1.0,
          1.8445917450672788e-16,
          1.4918621893400539e-16
        ],
        "angle_rad": 2.372376761383581e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "left_shoulder_pitch",
        "joint_other": "left_shoulder_pitch",
        "axis_m": [
          0.0,
          1.0,
          0.0
        ],
        "axis_other_aligned": [
          -4.0013116017338423e-16,
          1.0,
          4.217546450968613e-17
        ],
        "angle_rad": 4.023477539993311e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "left_shoulder_roll",
        "joint_other": "left_shoulder_roll",
        "axis_m": [
          1.0,
          0.0,
          0.0
        ],
        "axis_other_aligned": [
          1.0,
          1.8445917450672788e-16,
          1.4918621893400539e-16
        ],
        "angle_rad": 2.372376761383581e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "left_shoulder_yaw_drive",
        "joint_other": "left_shoulder_yaw_drive",
        "axis_m": [
          0.0,
          0.0,
          1.0
        ],
        "axis_other_aligned": [
          -1.544877532887462e-16,
          9.913453007809917e-18,
          1.0
        ],
        "angle_rad": 1.5480549882592209e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "left_shoulder_yaw_driven",
        "joint_other": "left_shoulder_yaw_driven",
        "axis_m": [
          0.0,
          0.0,
          -1.0
        ],
        "axis_other_aligned": [
          1.544877532887462e-16,
          -9.913453007809917e-18,
          -1.0
        ],
        "angle_rad": 1.5480549882592209e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "left_elbow_roll",
        "joint_other": "left_elbow_roll",
        "axis_m": [
          1.0,
          0.0,
          0.0
        ],
        "axis_other_aligned": [
          1.0,
          1.8445917450672788e-16,
          1.4918621893400539e-16
        ],
        "angle_rad": 2.372376761383581e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "left_elbow_yaw_drive",
        "joint_other": "left_elbow_yaw_drive",
        "axis_m": [
          0.0,
          0.0,
          1.0
        ],
        "axis_other_aligned": [
          -1.544877532887462e-16,
          9.913453007809917e-18,
          1.0
        ],
        "angle_rad": 1.5480549882592209e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "left_elbow_yaw_driven",
        "joint_other": "left_elbow_yaw_driven",
        "axis_m": [
          0.0,
          0.0,
          -1.0
        ],
        "axis_other_aligned": [
          1.544877532887462e-16,
          -9.913453007809917e-18,
          -1.0
        ],
        "angle_rad": 1.5480549882592209e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "left_wrist_pitch_driven",
        "joint_other": "left_wrist_pitch_driven",
        "axis_m": [
          0.0,
          -1.0,
          0.0
        ],
        "axis_other_aligned": [
          4.0013116017338423e-16,
          -1.0,
          -4.217546450968613e-17
        ],
        "angle_rad": 4.023477539993311e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "left_wrist_pitch_drive",
        "joint_other": "left_wrist_pitch_drive",
        "axis_m": [
          0.0,
          1.0,
          0.0
        ],
        "axis_other_aligned": [
          -4.0013116017338423e-16,
          1.0,
          4.217546450968613e-17
        ],
        "angle_rad": 4.023477539993311e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "left_wrist_roll",
        "joint_other": "left_wrist_roll",
        "axis_m": [
          -1.0,
          0.0,
          0.0
        ],
        "axis_other_aligned": [
          -1.0,
          -1.8445917450672788e-16,
          -1.4918621893400539e-16
        ],
        "angle_rad": 2.372376761383581e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "right_shoulder_pitch",
        "joint_other": "right_shoulder_pitch",
        "axis_m": [
          0.0,
          -1.0,
          0.0
        ],
        "axis_other_aligned": [
          4.0013116017338423e-16,
          -1.0,
          -4.217546450968613e-17
        ],
        "angle_rad": 4.023477539993311e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "right_shoulder_roll",
        "joint_other": "right_shoulder_roll",
        "axis_m": [
          -1.0,
          0.0,
          0.0
        ],
        "axis_other_aligned": [
          -1.0,
          -1.8445917450672788e-16,
          -1.4918621893400539e-16
        ],
        "angle_rad": 2.372376761383581e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "right_shoulder_yaw_drive",
        "joint_other": "right_shoulder_yaw_drive",
        "axis_m": [
          0.0,
          0.0,
          1.0
        ],
        "axis_other_aligned": [
          -1.544877532887462e-16,
          9.913453007809917e-18,
          1.0
        ],
        "angle_rad": 1.5480549882592209e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "right_shoulder_yaw_driven",
        "joint_other": "right_shoulder_yaw_driven",
        "axis_m": [
          0.0,
          0.0,
          -1.0
        ],
        "axis_other_aligned": [
          1.544877532887462e-16,
          -9.913453007809917e-18,
          -1.0
        ],
        "angle_rad": 1.5480549882592209e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "right_elbow_roll",
        "joint_other": "right_elbow_roll",
        "axis_m": [
          -1.0,
          0.0,
          0.0
        ],
        "axis_other_aligned": [
          -1.0,
          -1.8445917450672788e-16,
          -1.4918621893400539e-16
        ],
        "angle_rad": 2.372376761383581e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "right_elbow_yaw_drive",
        "joint_other": "right_elbow_yaw_drive",
        "axis_m": [
          0.0,
          0.0,
          1.0
        ],
        "axis_other_aligned": [
          -1.544877532887462e-16,
          9.913453007809917e-18,
          1.0
        ],
        "angle_rad": 1.5480549882592209e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "right_elbow_yaw_driven",
        "joint_other": "right_elbow_yaw_driven",
        "axis_m": [
          0.0,
          0.0,
          -1.0
        ],
        "axis_other_aligned": [
          1.544877532887462e-16,
          -9.913453007809917e-18,
          -1.0
        ],
        "angle_rad": 1.5480549882592209e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "right_wrist_pitch_driven",
        "joint_other": "right_wrist_pitch_driven",
        "axis_m": [
          0.0,
          1.0,
          0.0
        ],
        "axis_other_aligned": [
          -4.0013116017338423e-16,
          1.0,
          4.217546450968613e-17
        ],
        "angle_rad": 4.023477539993311e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "right_wrist_pitch_drive",
        "joint_other": "right_wrist_pitch_drive",
        "axis_m": [
          0.0,
          -1.0,
          0.0
        ],
        "axis_other_aligned": [
          4.0013116017338423e-16,
          -1.0,
          -4.217546450968613e-17
        ],
        "angle_rad": 4.023477539993311e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "right_wrist_roll",
        "joint_other": "right_wrist_roll",
        "axis_m": [
          1.0,
          0.0,
          0.0
        ],
        "axis_other_aligned": [
          1.0,
          1.8445917450672788e-16,
          1.4918621893400539e-16
        ],
        "angle_rad": 2.372376761383581e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      }
    ],
    "axis_disagreements": [],
    "com_eligible": true,
    "covariance_singular_values": [
      0.6499211331331678,
      0.21879516546392905,
      0.006026869517233771
    ],
    "origin_residuals_m": {
      "torso": 5.111746641005718e-18,
      "neck_yaw_gear_drive": 3.470792684189829e-17,
      "neck_yaw_link": 3.415734411546883e-17,
      "head": 3.6435000758482575e-17,
      "neck_pitch_plate": 6.546175330706957e-17,
      "neck_rod": 6.371419944489391e-17,
      "neck_rod_2": 6.546714017464125e-17,
      "waist_gears": 6.2919638844085975e-18,
      "pelvis_link": 6.461280324035604e-18,
      "waist_gear_drive": 4.131595016568073e-18,
      "waist_gear_drive_2": 1.4457452296714117e-18,
      "left_hip_pitch_link": 1.3877787807814457e-17,
      "left_hip_roll_link": 2.7758963540648015e-17,
      "left_hip_yaw_link": 2.7755575615628914e-17,
      "left_hip_yaw_gear_drive": 2.8609792490763984e-17,
      "left_knee_link": 3.1031676915590914e-17,
      "left_ankle_pitch_link": 6.378500613402836e-17,
      "left_ankle_roll_link": 5.96906223549092e-17,
      "right_hip_pitch_link": 1.993045536433795e-17,
      "right_hip_roll_link": 2.5962963631595152e-17,
      "right_hip_yaw_link": 3.98609107286759e-17,
      "right_hip_yaw_gear_drive": 3.179800655392251e-17,
      "right_knee_link": 3.94053425015214e-17,
      "right_ankle_pitch_link": 7.152448122690996e-17,
      "right_ankle_roll_link": 7.408711319456051e-17,
      "left_shoulder_pitch_link": 5.763878168445254e-17,
      "left_shoulder_roll_link": 6.359601310784502e-17,
      "left_shoulder_gear_drive": 6.877910602720239e-17,
      "left_shoulder_yaw_link": 5.561946577567963e-17,
      "left_elbow_roll_link": 4.5102810375396984e-17,
      "left_elbow_gear_drive": 5.386728408893287e-17,
      "left_elbow_yaw_link": 4.3885418357208765e-17,
      "left_wrist_pitch_link": 4.291468873614597e-17,
      "left_wrist_gear_drive": 4.6027415078689346e-17,
      "left_hand": 3.3993498887762956e-17,
      "right_shoulder_pitch_link": 2.8609792490763984e-17,
      "right_shoulder_roll_link": 3.785713555622682e-17,
      "right_shoulder_gear_drive": 4.4022346672339675e-17,
      "right_shoulder_yaw_link": 3.6880726988814706e-17,
      "right_elbow_roll_link": 3.8983664739440365e-17,
      "right_elbow_gear_drive": 4.8419065803461866e-17,
      "right_elbow_yaw_link": 3.576224061345498e-17,
      "right_wrist_pitch_link": 5.561946577567963e-17,
      "right_wrist_gear_drive": 5.0515910130503314e-17,
      "right_hand": 5.198565698646572e-17
    },
    "reason": "Unique proper rigid fit and matched signed axes meet the configured thresholds"
  },
  "M/S": {
    "status": "consistent",
    "matched_body_origins": 45,
    "position_threshold_m": 0.005,
    "axis_threshold_rad": 0.005,
    "residual_definition": "maximum Euclidean residual over matched body origins; Kabsch minimizes RMS, which is also recorded",
    "coordinate_frames": "each snapshot registered to its matched report anchor",
    "anchor_m": "torso",
    "anchor_other": "torso",
    "rotation_other_to_m": [
      [
        1.0000000000000002,
        -4.001311601733842e-16,
        -1.5448775328874618e-16
      ],
      [
        1.8445917450672793e-16,
        0.9999999999999999,
        9.913453007809916e-18
      ],
      [
        1.491862189340054e-16,
        4.217546450968612e-17,
        0.9999999999999998
      ]
    ],
    "translation_other_to_m": [
      0.0,
      3.754050022231059e-18,
      -3.469446951953614e-18
    ],
    "rms_residual_m": 4.4631984569332215e-17,
    "max_residual_m": 7.408711319456051e-17,
    "fit_rank": 3,
    "axis_checks": [
      {
        "joint_m": "neck_yaw_drive",
        "joint_other": "neck_yaw_drive",
        "axis_m": [
          0.0,
          0.0,
          -1.0
        ],
        "axis_other_aligned": [
          1.544877532887462e-16,
          -9.913453007809917e-18,
          -1.0
        ],
        "angle_rad": 1.5480549882592209e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "neck_yaw_driven",
        "joint_other": "neck_yaw_driven",
        "axis_m": [
          0.0,
          0.0,
          1.0
        ],
        "axis_other_aligned": [
          -1.544877532887462e-16,
          9.913453007809917e-18,
          1.0
        ],
        "angle_rad": 1.5480549882592209e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "neck_pitch",
        "joint_other": "neck_pitch",
        "axis_m": [
          0.0,
          1.0,
          0.0
        ],
        "axis_other_aligned": [
          -4.0013116017338423e-16,
          1.0,
          4.217546450968613e-17
        ],
        "angle_rad": 4.023477539993311e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "neck_pitch_act",
        "joint_other": "neck_pitch_act",
        "axis_m": [
          0.0,
          -1.0,
          0.0
        ],
        "axis_other_aligned": [
          4.0013116017338423e-16,
          -1.0,
          -4.217546450968613e-17
        ],
        "angle_rad": 4.023477539993311e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "neck_pitch_front",
        "joint_other": "neck_pitch_front",
        "axis_m": [
          0.0,
          -1.0,
          0.0
        ],
        "axis_other_aligned": [
          4.0013116017338423e-16,
          -1.0,
          -4.217546450968613e-17
        ],
        "angle_rad": 4.023477539993311e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "neck_pitch_back",
        "joint_other": "neck_pitch_back",
        "axis_m": [
          0.0,
          -1.0,
          0.0
        ],
        "axis_other_aligned": [
          4.0013116017338423e-16,
          -1.0,
          -4.217546450968613e-17
        ],
        "angle_rad": 4.023477539993311e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "waist_yaw",
        "joint_other": "waist_yaw",
        "axis_m": [
          0.0,
          0.0,
          1.0
        ],
        "axis_other_aligned": [
          -1.544877532887462e-16,
          9.913453007809917e-18,
          1.0
        ],
        "angle_rad": 1.5480549882592209e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "waist_roll",
        "joint_other": "waist_roll",
        "axis_m": [
          1.0,
          0.0,
          0.0
        ],
        "axis_other_aligned": [
          1.0,
          1.8445917450672788e-16,
          1.4918621893400539e-16
        ],
        "angle_rad": 2.372376761383581e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "waist_act_1",
        "joint_other": "waist_act_1",
        "axis_m": [
          0.0,
          0.0,
          1.0
        ],
        "axis_other_aligned": [
          -1.544877532887462e-16,
          9.913453007809917e-18,
          1.0
        ],
        "angle_rad": 1.5480549882592209e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "waist_act_2",
        "joint_other": "waist_act_2",
        "axis_m": [
          0.0,
          0.0,
          1.0
        ],
        "axis_other_aligned": [
          -1.544877532887462e-16,
          9.913453007809917e-18,
          1.0
        ],
        "angle_rad": 1.5480549882592209e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "left_hip_pitch",
        "joint_other": "left_hip_pitch",
        "axis_m": [
          0.0,
          1.0,
          0.0
        ],
        "axis_other_aligned": [
          -4.0013116017338423e-16,
          1.0,
          4.217546450968613e-17
        ],
        "angle_rad": 4.023477539993311e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "left_hip_roll",
        "joint_other": "left_hip_roll",
        "axis_m": [
          1.0,
          0.0,
          0.0
        ],
        "axis_other_aligned": [
          1.0,
          1.8445917450672788e-16,
          1.4918621893400539e-16
        ],
        "angle_rad": 2.372376761383581e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "left_hip_yaw_driven",
        "joint_other": "left_hip_yaw_driven",
        "axis_m": [
          0.0,
          0.0,
          -1.0
        ],
        "axis_other_aligned": [
          1.544877532887462e-16,
          -9.913453007809917e-18,
          -1.0
        ],
        "angle_rad": 1.5480549882592209e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "left_hip_yaw_drive",
        "joint_other": "left_hip_yaw_drive",
        "axis_m": [
          0.0,
          0.0,
          1.0
        ],
        "axis_other_aligned": [
          -1.544877532887462e-16,
          9.913453007809917e-18,
          1.0
        ],
        "angle_rad": 1.5480549882592209e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "left_knee",
        "joint_other": "left_knee",
        "axis_m": [
          0.0,
          -1.0,
          0.0
        ],
        "axis_other_aligned": [
          4.0013116017338423e-16,
          -1.0,
          -4.217546450968613e-17
        ],
        "angle_rad": 4.023477539993311e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "left_ankle_pitch",
        "joint_other": "left_ankle_pitch",
        "axis_m": [
          0.0,
          1.0,
          0.0
        ],
        "axis_other_aligned": [
          -4.0013116017338423e-16,
          1.0,
          4.217546450968613e-17
        ],
        "angle_rad": 4.023477539993311e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "left_ankle_roll",
        "joint_other": "left_ankle_roll",
        "axis_m": [
          1.0,
          0.0,
          0.0
        ],
        "axis_other_aligned": [
          1.0,
          1.8445917450672788e-16,
          1.4918621893400539e-16
        ],
        "angle_rad": 2.372376761383581e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "right_hip_pitch",
        "joint_other": "right_hip_pitch",
        "axis_m": [
          0.0,
          -1.0,
          0.0
        ],
        "axis_other_aligned": [
          4.0013116017338423e-16,
          -1.0,
          -4.217546450968613e-17
        ],
        "angle_rad": 4.023477539993311e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "right_hip_roll",
        "joint_other": "right_hip_roll",
        "axis_m": [
          -1.0,
          0.0,
          0.0
        ],
        "axis_other_aligned": [
          -1.0,
          -1.8445917450672788e-16,
          -1.4918621893400539e-16
        ],
        "angle_rad": 2.372376761383581e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "right_hip_yaw_driven",
        "joint_other": "right_hip_yaw_driven",
        "axis_m": [
          0.0,
          0.0,
          -1.0
        ],
        "axis_other_aligned": [
          1.544877532887462e-16,
          -9.913453007809917e-18,
          -1.0
        ],
        "angle_rad": 1.5480549882592209e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "right_hip_yaw_drive",
        "joint_other": "right_hip_yaw_drive",
        "axis_m": [
          0.0,
          0.0,
          1.0
        ],
        "axis_other_aligned": [
          -1.544877532887462e-16,
          9.913453007809917e-18,
          1.0
        ],
        "angle_rad": 1.5480549882592209e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "right_knee",
        "joint_other": "right_knee",
        "axis_m": [
          0.0,
          1.0,
          0.0
        ],
        "axis_other_aligned": [
          -4.0013116017338423e-16,
          1.0,
          4.217546450968613e-17
        ],
        "angle_rad": 4.023477539993311e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "right_ankle_pitch",
        "joint_other": "right_ankle_pitch",
        "axis_m": [
          0.0,
          -1.0,
          0.0
        ],
        "axis_other_aligned": [
          4.0013116017338423e-16,
          -1.0,
          -4.217546450968613e-17
        ],
        "angle_rad": 4.023477539993311e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "right_ankle_roll",
        "joint_other": "right_ankle_roll",
        "axis_m": [
          1.0,
          0.0,
          0.0
        ],
        "axis_other_aligned": [
          1.0,
          1.8445917450672788e-16,
          1.4918621893400539e-16
        ],
        "angle_rad": 2.372376761383581e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "left_shoulder_pitch",
        "joint_other": "left_shoulder_pitch",
        "axis_m": [
          0.0,
          1.0,
          0.0
        ],
        "axis_other_aligned": [
          -4.0013116017338423e-16,
          1.0,
          4.217546450968613e-17
        ],
        "angle_rad": 4.023477539993311e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "left_shoulder_roll",
        "joint_other": "left_shoulder_roll",
        "axis_m": [
          1.0,
          0.0,
          0.0
        ],
        "axis_other_aligned": [
          1.0,
          1.8445917450672788e-16,
          1.4918621893400539e-16
        ],
        "angle_rad": 2.372376761383581e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "left_shoulder_yaw_drive",
        "joint_other": "left_shoulder_yaw_drive",
        "axis_m": [
          0.0,
          0.0,
          1.0
        ],
        "axis_other_aligned": [
          -1.544877532887462e-16,
          9.913453007809917e-18,
          1.0
        ],
        "angle_rad": 1.5480549882592209e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "left_shoulder_yaw_driven",
        "joint_other": "left_shoulder_yaw_driven",
        "axis_m": [
          0.0,
          0.0,
          -1.0
        ],
        "axis_other_aligned": [
          1.544877532887462e-16,
          -9.913453007809917e-18,
          -1.0
        ],
        "angle_rad": 1.5480549882592209e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "left_elbow_roll",
        "joint_other": "left_elbow_roll",
        "axis_m": [
          1.0,
          0.0,
          0.0
        ],
        "axis_other_aligned": [
          1.0,
          1.8445917450672788e-16,
          1.4918621893400539e-16
        ],
        "angle_rad": 2.372376761383581e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "left_elbow_yaw_drive",
        "joint_other": "left_elbow_yaw_drive",
        "axis_m": [
          0.0,
          0.0,
          1.0
        ],
        "axis_other_aligned": [
          -1.544877532887462e-16,
          9.913453007809917e-18,
          1.0
        ],
        "angle_rad": 1.5480549882592209e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "left_elbow_yaw_driven",
        "joint_other": "left_elbow_yaw_driven",
        "axis_m": [
          0.0,
          0.0,
          -1.0
        ],
        "axis_other_aligned": [
          1.544877532887462e-16,
          -9.913453007809917e-18,
          -1.0
        ],
        "angle_rad": 1.5480549882592209e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "left_wrist_pitch_driven",
        "joint_other": "left_wrist_pitch_driven",
        "axis_m": [
          0.0,
          -1.0,
          0.0
        ],
        "axis_other_aligned": [
          4.0013116017338423e-16,
          -1.0,
          -4.217546450968613e-17
        ],
        "angle_rad": 4.023477539993311e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "left_wrist_pitch_drive",
        "joint_other": "left_wrist_pitch_drive",
        "axis_m": [
          0.0,
          1.0,
          0.0
        ],
        "axis_other_aligned": [
          -4.0013116017338423e-16,
          1.0,
          4.217546450968613e-17
        ],
        "angle_rad": 4.023477539993311e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "left_wrist_roll",
        "joint_other": "left_wrist_roll",
        "axis_m": [
          -1.0,
          0.0,
          0.0
        ],
        "axis_other_aligned": [
          -1.0,
          -1.8445917450672788e-16,
          -1.4918621893400539e-16
        ],
        "angle_rad": 2.372376761383581e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "right_shoulder_pitch",
        "joint_other": "right_shoulder_pitch",
        "axis_m": [
          0.0,
          -1.0,
          0.0
        ],
        "axis_other_aligned": [
          4.0013116017338423e-16,
          -1.0,
          -4.217546450968613e-17
        ],
        "angle_rad": 4.023477539993311e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "right_shoulder_roll",
        "joint_other": "right_shoulder_roll",
        "axis_m": [
          -1.0,
          0.0,
          0.0
        ],
        "axis_other_aligned": [
          -1.0,
          -1.8445917450672788e-16,
          -1.4918621893400539e-16
        ],
        "angle_rad": 2.372376761383581e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "right_shoulder_yaw_drive",
        "joint_other": "right_shoulder_yaw_drive",
        "axis_m": [
          0.0,
          0.0,
          1.0
        ],
        "axis_other_aligned": [
          -1.544877532887462e-16,
          9.913453007809917e-18,
          1.0
        ],
        "angle_rad": 1.5480549882592209e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "right_shoulder_yaw_driven",
        "joint_other": "right_shoulder_yaw_driven",
        "axis_m": [
          0.0,
          0.0,
          -1.0
        ],
        "axis_other_aligned": [
          1.544877532887462e-16,
          -9.913453007809917e-18,
          -1.0
        ],
        "angle_rad": 1.5480549882592209e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "right_elbow_roll",
        "joint_other": "right_elbow_roll",
        "axis_m": [
          -1.0,
          0.0,
          0.0
        ],
        "axis_other_aligned": [
          -1.0,
          -1.8445917450672788e-16,
          -1.4918621893400539e-16
        ],
        "angle_rad": 2.372376761383581e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "right_elbow_yaw_drive",
        "joint_other": "right_elbow_yaw_drive",
        "axis_m": [
          0.0,
          0.0,
          1.0
        ],
        "axis_other_aligned": [
          -1.544877532887462e-16,
          9.913453007809917e-18,
          1.0
        ],
        "angle_rad": 1.5480549882592209e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "right_elbow_yaw_driven",
        "joint_other": "right_elbow_yaw_driven",
        "axis_m": [
          0.0,
          0.0,
          -1.0
        ],
        "axis_other_aligned": [
          1.544877532887462e-16,
          -9.913453007809917e-18,
          -1.0
        ],
        "angle_rad": 1.5480549882592209e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "right_wrist_pitch_driven",
        "joint_other": "right_wrist_pitch_driven",
        "axis_m": [
          0.0,
          1.0,
          0.0
        ],
        "axis_other_aligned": [
          -4.0013116017338423e-16,
          1.0,
          4.217546450968613e-17
        ],
        "angle_rad": 4.023477539993311e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "right_wrist_pitch_drive",
        "joint_other": "right_wrist_pitch_drive",
        "axis_m": [
          0.0,
          -1.0,
          0.0
        ],
        "axis_other_aligned": [
          4.0013116017338423e-16,
          -1.0,
          -4.217546450968613e-17
        ],
        "angle_rad": 4.023477539993311e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "right_wrist_roll",
        "joint_other": "right_wrist_roll",
        "axis_m": [
          1.0,
          0.0,
          0.0
        ],
        "axis_other_aligned": [
          1.0,
          1.8445917450672788e-16,
          1.4918621893400539e-16
        ],
        "angle_rad": 2.372376761383581e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      }
    ],
    "axis_disagreements": [],
    "com_eligible": true,
    "covariance_singular_values": [
      0.6499211331331678,
      0.21879516546392905,
      0.006026869517233771
    ],
    "origin_residuals_m": {
      "torso": 5.111746641005718e-18,
      "neck_yaw_gear_drive": 3.470792684189829e-17,
      "neck_yaw_link": 3.415734411546883e-17,
      "head": 3.6435000758482575e-17,
      "neck_pitch_plate": 6.546175330706957e-17,
      "neck_rod": 6.371419944489391e-17,
      "neck_rod_2": 6.546714017464125e-17,
      "waist_gears": 6.2919638844085975e-18,
      "pelvis_link": 6.461280324035604e-18,
      "waist_gear_drive": 4.131595016568073e-18,
      "waist_gear_drive_2": 1.4457452296714117e-18,
      "left_hip_pitch_link": 1.3877787807814457e-17,
      "left_hip_roll_link": 2.7758963540648015e-17,
      "left_hip_yaw_link": 2.7755575615628914e-17,
      "left_hip_yaw_gear_drive": 2.8609792490763984e-17,
      "left_knee_link": 3.1031676915590914e-17,
      "left_ankle_pitch_link": 6.378500613402836e-17,
      "left_ankle_roll_link": 5.96906223549092e-17,
      "right_hip_pitch_link": 1.993045536433795e-17,
      "right_hip_roll_link": 2.5962963631595152e-17,
      "right_hip_yaw_link": 3.98609107286759e-17,
      "right_hip_yaw_gear_drive": 3.179800655392251e-17,
      "right_knee_link": 3.94053425015214e-17,
      "right_ankle_pitch_link": 7.152448122690996e-17,
      "right_ankle_roll_link": 7.408711319456051e-17,
      "left_shoulder_pitch_link": 5.763878168445254e-17,
      "left_shoulder_roll_link": 6.359601310784502e-17,
      "left_shoulder_gear_drive": 6.877910602720239e-17,
      "left_shoulder_yaw_link": 5.561946577567963e-17,
      "left_elbow_roll_link": 4.5102810375396984e-17,
      "left_elbow_gear_drive": 5.386728408893287e-17,
      "left_elbow_yaw_link": 4.3885418357208765e-17,
      "left_wrist_pitch_link": 4.291468873614597e-17,
      "left_wrist_gear_drive": 4.6027415078689346e-17,
      "left_hand": 3.3993498887762956e-17,
      "right_shoulder_pitch_link": 2.8609792490763984e-17,
      "right_shoulder_roll_link": 3.785713555622682e-17,
      "right_shoulder_gear_drive": 4.4022346672339675e-17,
      "right_shoulder_yaw_link": 3.6880726988814706e-17,
      "right_elbow_roll_link": 3.8983664739440365e-17,
      "right_elbow_gear_drive": 4.8419065803461866e-17,
      "right_elbow_yaw_link": 3.576224061345498e-17,
      "right_wrist_pitch_link": 5.561946577567963e-17,
      "right_wrist_gear_drive": 5.0515910130503314e-17,
      "right_hand": 5.198565698646572e-17
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
| robot / total_com_registered | [-0.0202051442, -0.00114192945, -0.0291883067] | [-0.0202051442, -0.00114192945, -0.0291883067] | [-0.0202051442, -0.00114192945, -0.0291883067] | [0, 0, 0] | eligible; compared after Kabsch alignment | [aggregate inputs](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/toddlerbot_2xc/toddlerbot_2xc.xml#L1) | [aggregate inputs](https://github.com/hshi74/toddlerbot/blob/957aadb8e6db85e02fbb9ef90bbcdb4b4c0c9f6c/toddlerbot/descriptions/toddlerbot_2xc/toddlerbot_2xc.xml#L1) | [aggregate inputs](https://github.com/hshi74/toddlerbot/blob/e337f3b177b4b53abff70b31d1695a7b66cc6d2e/toddlerbot/descriptions/toddlerbot_2xc/toddlerbot_2xc.xml#L1) |
| torso / com_registered | [-0.0185985, -0.00416082, 0.0626827] | [-0.0185985, -0.00416082, 0.0626827] | [-0.0185985, -0.00416082, 0.0626827] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L40](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/toddlerbot_2xc/toddlerbot_2xc.xml#L40) | [CoM/kinematic input L37](https://github.com/hshi74/toddlerbot/blob/957aadb8e6db85e02fbb9ef90bbcdb4b4c0c9f6c/toddlerbot/descriptions/toddlerbot_2xc/toddlerbot_2xc.xml#L37) | [CoM/kinematic input L37](https://github.com/hshi74/toddlerbot/blob/e337f3b177b4b53abff70b31d1695a7b66cc6d2e/toddlerbot/descriptions/toddlerbot_2xc/toddlerbot_2xc.xml#L37) |
| neck_yaw_gear_drive / com_registered | [-0.0215079, 0, 0.1223841] | [-0.0215079, 0, 0.1223841] | [-0.0215079, 0, 0.1223841] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L50](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/toddlerbot_2xc/toddlerbot_2xc.xml#L50) | [CoM/kinematic input L48](https://github.com/hshi74/toddlerbot/blob/957aadb8e6db85e02fbb9ef90bbcdb4b4c0c9f6c/toddlerbot/descriptions/toddlerbot_2xc/toddlerbot_2xc.xml#L48) | [CoM/kinematic input L48](https://github.com/hshi74/toddlerbot/blob/e337f3b177b4b53abff70b31d1695a7b66cc6d2e/toddlerbot/descriptions/toddlerbot_2xc/toddlerbot_2xc.xml#L48) |
| neck_yaw_link / com_registered | [-0.00051128, 0, 0.13221562] | [-0.00051128, 0, 0.13221562] | [-0.00051128, 0, 0.13221562] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L57](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/toddlerbot_2xc/toddlerbot_2xc.xml#L57) | [CoM/kinematic input L55](https://github.com/hshi74/toddlerbot/blob/957aadb8e6db85e02fbb9ef90bbcdb4b4c0c9f6c/toddlerbot/descriptions/toddlerbot_2xc/toddlerbot_2xc.xml#L55) | [CoM/kinematic input L55](https://github.com/hshi74/toddlerbot/blob/e337f3b177b4b53abff70b31d1695a7b66cc6d2e/toddlerbot/descriptions/toddlerbot_2xc/toddlerbot_2xc.xml#L55) |
| head / com_registered | [-0.01099307, 0.00511009, 0.1837856] | [-0.01099307, 0.00511009, 0.1837856] | [-0.01099307, 0.00511009, 0.1837856] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L71](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/toddlerbot_2xc/toddlerbot_2xc.xml#L71) | [CoM/kinematic input L69](https://github.com/hshi74/toddlerbot/blob/957aadb8e6db85e02fbb9ef90bbcdb4b4c0c9f6c/toddlerbot/descriptions/toddlerbot_2xc/toddlerbot_2xc.xml#L69) | [CoM/kinematic input L69](https://github.com/hshi74/toddlerbot/blob/e337f3b177b4b53abff70b31d1695a7b66cc6d2e/toddlerbot/descriptions/toddlerbot_2xc/toddlerbot_2xc.xml#L69) |
| neck_pitch_plate / com_registered | [-0.02750787, -0.00132818, 0.1716157] | [-0.02750787, -0.00132818, 0.1716157] | [-0.02750787, -0.00132818, 0.1716157] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L79](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/toddlerbot_2xc/toddlerbot_2xc.xml#L79) | [CoM/kinematic input L78](https://github.com/hshi74/toddlerbot/blob/957aadb8e6db85e02fbb9ef90bbcdb4b4c0c9f6c/toddlerbot/descriptions/toddlerbot_2xc/toddlerbot_2xc.xml#L78) | [CoM/kinematic input L78](https://github.com/hshi74/toddlerbot/blob/e337f3b177b4b53abff70b31d1695a7b66cc6d2e/toddlerbot/descriptions/toddlerbot_2xc/toddlerbot_2xc.xml#L78) |
| neck_rod / com_registered | [-0.0067893, -0.00559086, 0.15726547] | [-0.0067893, -0.00559086, 0.15726547] | [-0.0067893, -0.00559086, 0.15726547] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L85](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/toddlerbot_2xc/toddlerbot_2xc.xml#L85) | [CoM/kinematic input L85](https://github.com/hshi74/toddlerbot/blob/957aadb8e6db85e02fbb9ef90bbcdb4b4c0c9f6c/toddlerbot/descriptions/toddlerbot_2xc/toddlerbot_2xc.xml#L85) | [CoM/kinematic input L85](https://github.com/hshi74/toddlerbot/blob/e337f3b177b4b53abff70b31d1695a7b66cc6d2e/toddlerbot/descriptions/toddlerbot_2xc/toddlerbot_2xc.xml#L85) |
| neck_rod_2 / com_registered | [-0.02125841, -0.00559086, 0.15334582] | [-0.02125841, -0.00559086, 0.15334582] | [-0.02125841, -0.00559086, 0.15334582] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L96](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/toddlerbot_2xc/toddlerbot_2xc.xml#L96) | [CoM/kinematic input L97](https://github.com/hshi74/toddlerbot/blob/957aadb8e6db85e02fbb9ef90bbcdb4b4c0c9f6c/toddlerbot/descriptions/toddlerbot_2xc/toddlerbot_2xc.xml#L97) | [CoM/kinematic input L97](https://github.com/hshi74/toddlerbot/blob/e337f3b177b4b53abff70b31d1695a7b66cc6d2e/toddlerbot/descriptions/toddlerbot_2xc/toddlerbot_2xc.xml#L97) |
| waist_gears / com_registered | [-0.0165079, 0, -0.01547811] | [-0.0165079, 0, -0.01547811] | [-0.0165079, 0, -0.01547811] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L110](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/toddlerbot_2xc/toddlerbot_2xc.xml#L110) | [CoM/kinematic input L111](https://github.com/hshi74/toddlerbot/blob/957aadb8e6db85e02fbb9ef90bbcdb4b4c0c9f6c/toddlerbot/descriptions/toddlerbot_2xc/toddlerbot_2xc.xml#L111) | [CoM/kinematic input L111](https://github.com/hshi74/toddlerbot/blob/e337f3b177b4b53abff70b31d1695a7b66cc6d2e/toddlerbot/descriptions/toddlerbot_2xc/toddlerbot_2xc.xml#L111) |
| pelvis_link / com_registered | [-0.0166545, 0, -0.04256711] | [-0.0166545, 0, -0.04256711] | [-0.0166545, 0, -0.04256711] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L117](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/toddlerbot_2xc/toddlerbot_2xc.xml#L117) | [CoM/kinematic input L118](https://github.com/hshi74/toddlerbot/blob/957aadb8e6db85e02fbb9ef90bbcdb4b4c0c9f6c/toddlerbot/descriptions/toddlerbot_2xc/toddlerbot_2xc.xml#L118) | [CoM/kinematic input L118](https://github.com/hshi74/toddlerbot/blob/e337f3b177b4b53abff70b31d1695a7b66cc6d2e/toddlerbot/descriptions/toddlerbot_2xc/toddlerbot_2xc.xml#L118) |
| waist_gear_drive / com_registered | [-0.00625, 0, -0.02936827] | [-0.00625, 0, -0.02936827] | [-0.00625, 0, -0.02936827] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L125](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/toddlerbot_2xc/toddlerbot_2xc.xml#L125) | [CoM/kinematic input L127](https://github.com/hshi74/toddlerbot/blob/957aadb8e6db85e02fbb9ef90bbcdb4b4c0c9f6c/toddlerbot/descriptions/toddlerbot_2xc/toddlerbot_2xc.xml#L127) | [CoM/kinematic input L127](https://github.com/hshi74/toddlerbot/blob/e337f3b177b4b53abff70b31d1695a7b66cc6d2e/toddlerbot/descriptions/toddlerbot_2xc/toddlerbot_2xc.xml#L127) |
| waist_gear_drive_2 / com_registered | [-0.02625, 0, -0.02936827] | [-0.02625, 0, -0.02936827] | [-0.02625, 0, -0.02936827] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L132](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/toddlerbot_2xc/toddlerbot_2xc.xml#L132) | [CoM/kinematic input L135](https://github.com/hshi74/toddlerbot/blob/957aadb8e6db85e02fbb9ef90bbcdb4b4c0c9f6c/toddlerbot/descriptions/toddlerbot_2xc/toddlerbot_2xc.xml#L135) | [CoM/kinematic input L135](https://github.com/hshi74/toddlerbot/blob/e337f3b177b4b53abff70b31d1695a7b66cc6d2e/toddlerbot/descriptions/toddlerbot_2xc/toddlerbot_2xc.xml#L135) |
| left_hip_pitch_link / com_registered | [-0.01575402, 0.0365041, -0.07658631] | [-0.01575402, 0.0365041, -0.07658631] | [-0.01575402, 0.0365041, -0.07658631] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L139](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/toddlerbot_2xc/toddlerbot_2xc.xml#L139) | [CoM/kinematic input L143](https://github.com/hshi74/toddlerbot/blob/957aadb8e6db85e02fbb9ef90bbcdb4b4c0c9f6c/toddlerbot/descriptions/toddlerbot_2xc/toddlerbot_2xc.xml#L143) | [CoM/kinematic input L143](https://github.com/hshi74/toddlerbot/blob/e337f3b177b4b53abff70b31d1695a7b66cc6d2e/toddlerbot/descriptions/toddlerbot_2xc/toddlerbot_2xc.xml#L143) |
| left_hip_roll_link / com_registered | [-0.0162425, 0.03699667, -0.10550231] | [-0.0162425, 0.03699667, -0.10550231] | [-0.0162425, 0.03699667, -0.10550231] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L148](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/toddlerbot_2xc/toddlerbot_2xc.xml#L148) | [CoM/kinematic input L153](https://github.com/hshi74/toddlerbot/blob/957aadb8e6db85e02fbb9ef90bbcdb4b4c0c9f6c/toddlerbot/descriptions/toddlerbot_2xc/toddlerbot_2xc.xml#L153) | [CoM/kinematic input L153](https://github.com/hshi74/toddlerbot/blob/e337f3b177b4b53abff70b31d1695a7b66cc6d2e/toddlerbot/descriptions/toddlerbot_2xc/toddlerbot_2xc.xml#L153) |
| left_hip_yaw_link / com_registered | [-0.02592359, 0.03817184, -0.15691701] | [-0.02592359, 0.03817184, -0.15691701] | [-0.02592359, 0.03817184, -0.15691701] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L154](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/toddlerbot_2xc/toddlerbot_2xc.xml#L154) | [CoM/kinematic input L160](https://github.com/hshi74/toddlerbot/blob/957aadb8e6db85e02fbb9ef90bbcdb4b4c0c9f6c/toddlerbot/descriptions/toddlerbot_2xc/toddlerbot_2xc.xml#L160) | [CoM/kinematic input L160](https://github.com/hshi74/toddlerbot/blob/e337f3b177b4b53abff70b31d1695a7b66cc6d2e/toddlerbot/descriptions/toddlerbot_2xc/toddlerbot_2xc.xml#L160) |
| left_hip_yaw_gear_drive / com_registered | [-0.03545, 0.0368, -0.11983651] | [-0.03545, 0.0368, -0.11983651] | [-0.03545, 0.0368, -0.11983651] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L163](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/toddlerbot_2xc/toddlerbot_2xc.xml#L163) | [CoM/kinematic input L170](https://github.com/hshi74/toddlerbot/blob/957aadb8e6db85e02fbb9ef90bbcdb4b4c0c9f6c/toddlerbot/descriptions/toddlerbot_2xc/toddlerbot_2xc.xml#L170) | [CoM/kinematic input L170](https://github.com/hshi74/toddlerbot/blob/e337f3b177b4b53abff70b31d1695a7b66cc6d2e/toddlerbot/descriptions/toddlerbot_2xc/toddlerbot_2xc.xml#L170) |
| left_knee_link / com_registered | [-0.01172668, 0.037, -0.21665601] | [-0.01172668, 0.037, -0.21665601] | [-0.01172668, 0.037, -0.21665601] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L170](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/toddlerbot_2xc/toddlerbot_2xc.xml#L170) | [CoM/kinematic input L178](https://github.com/hshi74/toddlerbot/blob/957aadb8e6db85e02fbb9ef90bbcdb4b4c0c9f6c/toddlerbot/descriptions/toddlerbot_2xc/toddlerbot_2xc.xml#L178) | [CoM/kinematic input L178](https://github.com/hshi74/toddlerbot/blob/e337f3b177b4b53abff70b31d1695a7b66cc6d2e/toddlerbot/descriptions/toddlerbot_2xc/toddlerbot_2xc.xml#L178) |
| left_ankle_pitch_link / com_registered | [-0.0342192, 0.0368074, -0.26399731] | [-0.0342192, 0.0368074, -0.26399731] | [-0.0342192, 0.0368074, -0.26399731] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L179](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/toddlerbot_2xc/toddlerbot_2xc.xml#L179) | [CoM/kinematic input L187](https://github.com/hshi74/toddlerbot/blob/957aadb8e6db85e02fbb9ef90bbcdb4b4c0c9f6c/toddlerbot/descriptions/toddlerbot_2xc/toddlerbot_2xc.xml#L187) | [CoM/kinematic input L187](https://github.com/hshi74/toddlerbot/blob/e337f3b177b4b53abff70b31d1695a7b66cc6d2e/toddlerbot/descriptions/toddlerbot_2xc/toddlerbot_2xc.xml#L187) |
| left_ankle_roll_link / com_registered | [-0.0034068, 0.03699993, -0.30280941] | [-0.0034068, 0.03699993, -0.30280941] | [-0.0034068, 0.03699993, -0.30280941] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L189](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/toddlerbot_2xc/toddlerbot_2xc.xml#L189) | [CoM/kinematic input L197](https://github.com/hshi74/toddlerbot/blob/957aadb8e6db85e02fbb9ef90bbcdb4b4c0c9f6c/toddlerbot/descriptions/toddlerbot_2xc/toddlerbot_2xc.xml#L197) | [CoM/kinematic input L197](https://github.com/hshi74/toddlerbot/blob/e337f3b177b4b53abff70b31d1695a7b66cc6d2e/toddlerbot/descriptions/toddlerbot_2xc/toddlerbot_2xc.xml#L197) |
| right_hip_pitch_link / com_registered | [-0.01674589, -0.036504, -0.07658671] | [-0.01674589, -0.036504, -0.07658671] | [-0.01674589, -0.036504, -0.07658671] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L206](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/toddlerbot_2xc/toddlerbot_2xc.xml#L206) | [CoM/kinematic input L216](https://github.com/hshi74/toddlerbot/blob/957aadb8e6db85e02fbb9ef90bbcdb4b4c0c9f6c/toddlerbot/descriptions/toddlerbot_2xc/toddlerbot_2xc.xml#L216) | [CoM/kinematic input L215](https://github.com/hshi74/toddlerbot/blob/e337f3b177b4b53abff70b31d1695a7b66cc6d2e/toddlerbot/descriptions/toddlerbot_2xc/toddlerbot_2xc.xml#L215) |
| right_hip_roll_link / com_registered | [-0.0162425, -0.03700333, -0.10550231] | [-0.0162425, -0.03700333, -0.10550231] | [-0.0162425, -0.03700333, -0.10550231] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L215](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/toddlerbot_2xc/toddlerbot_2xc.xml#L215) | [CoM/kinematic input L226](https://github.com/hshi74/toddlerbot/blob/957aadb8e6db85e02fbb9ef90bbcdb4b4c0c9f6c/toddlerbot/descriptions/toddlerbot_2xc/toddlerbot_2xc.xml#L226) | [CoM/kinematic input L225](https://github.com/hshi74/toddlerbot/blob/e337f3b177b4b53abff70b31d1695a7b66cc6d2e/toddlerbot/descriptions/toddlerbot_2xc/toddlerbot_2xc.xml#L225) |
| right_hip_yaw_link / com_registered | [-0.02592257, -0.03817152, -0.15691681] | [-0.02592257, -0.03817152, -0.15691681] | [-0.02592257, -0.03817152, -0.15691681] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L221](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/toddlerbot_2xc/toddlerbot_2xc.xml#L221) | [CoM/kinematic input L233](https://github.com/hshi74/toddlerbot/blob/957aadb8e6db85e02fbb9ef90bbcdb4b4c0c9f6c/toddlerbot/descriptions/toddlerbot_2xc/toddlerbot_2xc.xml#L233) | [CoM/kinematic input L232](https://github.com/hshi74/toddlerbot/blob/e337f3b177b4b53abff70b31d1695a7b66cc6d2e/toddlerbot/descriptions/toddlerbot_2xc/toddlerbot_2xc.xml#L232) |
| right_hip_yaw_gear_drive / com_registered | [-0.03545, -0.0368, -0.11983651] | [-0.03545, -0.0368, -0.11983651] | [-0.03545, -0.0368, -0.11983651] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L230](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/toddlerbot_2xc/toddlerbot_2xc.xml#L230) | [CoM/kinematic input L243](https://github.com/hshi74/toddlerbot/blob/957aadb8e6db85e02fbb9ef90bbcdb4b4c0c9f6c/toddlerbot/descriptions/toddlerbot_2xc/toddlerbot_2xc.xml#L243) | [CoM/kinematic input L242](https://github.com/hshi74/toddlerbot/blob/e337f3b177b4b53abff70b31d1695a7b66cc6d2e/toddlerbot/descriptions/toddlerbot_2xc/toddlerbot_2xc.xml#L242) |
| right_knee_link / com_registered | [-0.01172668, -0.037, -0.21665601] | [-0.01172668, -0.037, -0.21665601] | [-0.01172668, -0.037, -0.21665601] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L238](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/toddlerbot_2xc/toddlerbot_2xc.xml#L238) | [CoM/kinematic input L251](https://github.com/hshi74/toddlerbot/blob/957aadb8e6db85e02fbb9ef90bbcdb4b4c0c9f6c/toddlerbot/descriptions/toddlerbot_2xc/toddlerbot_2xc.xml#L251) | [CoM/kinematic input L250](https://github.com/hshi74/toddlerbot/blob/e337f3b177b4b53abff70b31d1695a7b66cc6d2e/toddlerbot/descriptions/toddlerbot_2xc/toddlerbot_2xc.xml#L250) |
| right_ankle_pitch_link / com_registered | [-0.0342192, -0.036812, -0.26399731] | [-0.0342192, -0.036812, -0.26399731] | [-0.0342192, -0.036812, -0.26399731] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L247](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/toddlerbot_2xc/toddlerbot_2xc.xml#L247) | [CoM/kinematic input L260](https://github.com/hshi74/toddlerbot/blob/957aadb8e6db85e02fbb9ef90bbcdb4b4c0c9f6c/toddlerbot/descriptions/toddlerbot_2xc/toddlerbot_2xc.xml#L260) | [CoM/kinematic input L259](https://github.com/hshi74/toddlerbot/blob/e337f3b177b4b53abff70b31d1695a7b66cc6d2e/toddlerbot/descriptions/toddlerbot_2xc/toddlerbot_2xc.xml#L259) |
| right_ankle_roll_link / com_registered | [-0.0034068, -0.03700007, -0.30280941] | [-0.0034068, -0.03700007, -0.30280941] | [-0.0034068, -0.03700007, -0.30280941] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L257](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/toddlerbot_2xc/toddlerbot_2xc.xml#L257) | [CoM/kinematic input L270](https://github.com/hshi74/toddlerbot/blob/957aadb8e6db85e02fbb9ef90bbcdb4b4c0c9f6c/toddlerbot/descriptions/toddlerbot_2xc/toddlerbot_2xc.xml#L270) | [CoM/kinematic input L269](https://github.com/hshi74/toddlerbot/blob/e337f3b177b4b53abff70b31d1695a7b66cc6d2e/toddlerbot/descriptions/toddlerbot_2xc/toddlerbot_2xc.xml#L269) |
| left_shoulder_pitch_link / com_registered | [-0.0200079, 0.0799132, 0.10175] | [-0.0200079, 0.0799132, 0.10175] | [-0.0200079, 0.0799132, 0.10175] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L276](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/toddlerbot_2xc/toddlerbot_2xc.xml#L276) | [CoM/kinematic input L291](https://github.com/hshi74/toddlerbot/blob/957aadb8e6db85e02fbb9ef90bbcdb4b4c0c9f6c/toddlerbot/descriptions/toddlerbot_2xc/toddlerbot_2xc.xml#L291) | [CoM/kinematic input L289](https://github.com/hshi74/toddlerbot/blob/e337f3b177b4b53abff70b31d1695a7b66cc6d2e/toddlerbot/descriptions/toddlerbot_2xc/toddlerbot_2xc.xml#L289) |
| left_shoulder_roll_link / com_registered | [-0.0204677, 0.1057736, 0.09971352] | [-0.0204677, 0.1057736, 0.09971352] | [-0.0204677, 0.1057736, 0.09971352] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L282](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/toddlerbot_2xc/toddlerbot_2xc.xml#L282) | [CoM/kinematic input L298](https://github.com/hshi74/toddlerbot/blob/957aadb8e6db85e02fbb9ef90bbcdb4b4c0c9f6c/toddlerbot/descriptions/toddlerbot_2xc/toddlerbot_2xc.xml#L298) | [CoM/kinematic input L296](https://github.com/hshi74/toddlerbot/blob/e337f3b177b4b53abff70b31d1695a7b66cc6d2e/toddlerbot/descriptions/toddlerbot_2xc/toddlerbot_2xc.xml#L296) |
| left_shoulder_gear_drive / com_registered | [-0.0200079, 0.118, 0.07612614] | [-0.0200079, 0.118, 0.07612614] | [-0.0200079, 0.118, 0.07612614] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L291](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/toddlerbot_2xc/toddlerbot_2xc.xml#L291) | [CoM/kinematic input L308](https://github.com/hshi74/toddlerbot/blob/957aadb8e6db85e02fbb9ef90bbcdb4b4c0c9f6c/toddlerbot/descriptions/toddlerbot_2xc/toddlerbot_2xc.xml#L308) | [CoM/kinematic input L306](https://github.com/hshi74/toddlerbot/blob/e337f3b177b4b53abff70b31d1695a7b66cc6d2e/toddlerbot/descriptions/toddlerbot_2xc/toddlerbot_2xc.xml#L306) |
| left_shoulder_yaw_link / com_registered | [-0.02000811, 0.09400024, 0.0509658] | [-0.02000811, 0.09400024, 0.0509658] | [-0.02000811, 0.09400024, 0.0509658] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L298](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/toddlerbot_2xc/toddlerbot_2xc.xml#L298) | [CoM/kinematic input L316](https://github.com/hshi74/toddlerbot/blob/957aadb8e6db85e02fbb9ef90bbcdb4b4c0c9f6c/toddlerbot/descriptions/toddlerbot_2xc/toddlerbot_2xc.xml#L316) | [CoM/kinematic input L314](https://github.com/hshi74/toddlerbot/blob/e337f3b177b4b53abff70b31d1695a7b66cc6d2e/toddlerbot/descriptions/toddlerbot_2xc/toddlerbot_2xc.xml#L314) |
| left_elbow_roll_link / com_registered | [-0.0204677, 0.1057736, 0.01371352] | [-0.0204677, 0.1057736, 0.01371352] | [-0.0204677, 0.1057736, 0.01371352] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L306](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/toddlerbot_2xc/toddlerbot_2xc.xml#L306) | [CoM/kinematic input L326](https://github.com/hshi74/toddlerbot/blob/957aadb8e6db85e02fbb9ef90bbcdb4b4c0c9f6c/toddlerbot/descriptions/toddlerbot_2xc/toddlerbot_2xc.xml#L326) | [CoM/kinematic input L324](https://github.com/hshi74/toddlerbot/blob/e337f3b177b4b53abff70b31d1695a7b66cc6d2e/toddlerbot/descriptions/toddlerbot_2xc/toddlerbot_2xc.xml#L324) |
| left_elbow_gear_drive / com_registered | [-0.0200079, 0.118, -0.00987386] | [-0.0200079, 0.118, -0.00987386] | [-0.0200079, 0.118, -0.00987386] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L315](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/toddlerbot_2xc/toddlerbot_2xc.xml#L315) | [CoM/kinematic input L336](https://github.com/hshi74/toddlerbot/blob/957aadb8e6db85e02fbb9ef90bbcdb4b4c0c9f6c/toddlerbot/descriptions/toddlerbot_2xc/toddlerbot_2xc.xml#L336) | [CoM/kinematic input L334](https://github.com/hshi74/toddlerbot/blob/e337f3b177b4b53abff70b31d1695a7b66cc6d2e/toddlerbot/descriptions/toddlerbot_2xc/toddlerbot_2xc.xml#L334) |
| left_elbow_yaw_link / com_registered | [-0.02000767, 0.09669789, -0.0426292] | [-0.02000767, 0.09669789, -0.0426292] | [-0.02000767, 0.09669789, -0.0426292] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L322](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/toddlerbot_2xc/toddlerbot_2xc.xml#L322) | [CoM/kinematic input L344](https://github.com/hshi74/toddlerbot/blob/957aadb8e6db85e02fbb9ef90bbcdb4b4c0c9f6c/toddlerbot/descriptions/toddlerbot_2xc/toddlerbot_2xc.xml#L344) | [CoM/kinematic input L342](https://github.com/hshi74/toddlerbot/blob/e337f3b177b4b53abff70b31d1695a7b66cc6d2e/toddlerbot/descriptions/toddlerbot_2xc/toddlerbot_2xc.xml#L342) |
| left_wrist_pitch_link / com_registered | [-0.02042295, 0.0941329, -0.058754] | [-0.02042295, 0.0941329, -0.058754] | [-0.02042295, 0.0941329, -0.058754] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L331](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/toddlerbot_2xc/toddlerbot_2xc.xml#L331) | [CoM/kinematic input L354](https://github.com/hshi74/toddlerbot/blob/957aadb8e6db85e02fbb9ef90bbcdb4b4c0c9f6c/toddlerbot/descriptions/toddlerbot_2xc/toddlerbot_2xc.xml#L354) | [CoM/kinematic input L352](https://github.com/hshi74/toddlerbot/blob/e337f3b177b4b53abff70b31d1695a7b66cc6d2e/toddlerbot/descriptions/toddlerbot_2xc/toddlerbot_2xc.xml#L352) |
| left_wrist_gear_drive / com_registered | [-0.0200079, 0.11803438, -0.04625] | [-0.0200079, 0.11803438, -0.04625] | [-0.0200079, 0.11803438, -0.04625] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L341](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/toddlerbot_2xc/toddlerbot_2xc.xml#L341) | [CoM/kinematic input L364](https://github.com/hshi74/toddlerbot/blob/957aadb8e6db85e02fbb9ef90bbcdb4b4c0c9f6c/toddlerbot/descriptions/toddlerbot_2xc/toddlerbot_2xc.xml#L364) | [CoM/kinematic input L362](https://github.com/hshi74/toddlerbot/blob/e337f3b177b4b53abff70b31d1695a7b66cc6d2e/toddlerbot/descriptions/toddlerbot_2xc/toddlerbot_2xc.xml#L362) |
| left_hand / com_registered | [-0.0213864, 0.09715051, -0.1089045] | [-0.0213864, 0.09715051, -0.1089045] | [-0.0213864, 0.09715051, -0.1089045] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L349](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/toddlerbot_2xc/toddlerbot_2xc.xml#L349) | [CoM/kinematic input L372](https://github.com/hshi74/toddlerbot/blob/957aadb8e6db85e02fbb9ef90bbcdb4b4c0c9f6c/toddlerbot/descriptions/toddlerbot_2xc/toddlerbot_2xc.xml#L372) | [CoM/kinematic input L370](https://github.com/hshi74/toddlerbot/blob/e337f3b177b4b53abff70b31d1695a7b66cc6d2e/toddlerbot/descriptions/toddlerbot_2xc/toddlerbot_2xc.xml#L370) |
| right_shoulder_pitch_link / com_registered | [-0.0200079, -0.0799132, 0.10175] | [-0.0200079, -0.0799132, 0.10175] | [-0.0200079, -0.0799132, 0.10175] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L366](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/toddlerbot_2xc/toddlerbot_2xc.xml#L366) | [CoM/kinematic input L390](https://github.com/hshi74/toddlerbot/blob/957aadb8e6db85e02fbb9ef90bbcdb4b4c0c9f6c/toddlerbot/descriptions/toddlerbot_2xc/toddlerbot_2xc.xml#L390) | [CoM/kinematic input L388](https://github.com/hshi74/toddlerbot/blob/e337f3b177b4b53abff70b31d1695a7b66cc6d2e/toddlerbot/descriptions/toddlerbot_2xc/toddlerbot_2xc.xml#L388) |
| right_shoulder_roll_link / com_registered | [-0.0195481, -0.1057736, 0.09971352] | [-0.0195481, -0.1057736, 0.09971352] | [-0.0195481, -0.1057736, 0.09971352] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L373](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/toddlerbot_2xc/toddlerbot_2xc.xml#L373) | [CoM/kinematic input L397](https://github.com/hshi74/toddlerbot/blob/957aadb8e6db85e02fbb9ef90bbcdb4b4c0c9f6c/toddlerbot/descriptions/toddlerbot_2xc/toddlerbot_2xc.xml#L397) | [CoM/kinematic input L395](https://github.com/hshi74/toddlerbot/blob/e337f3b177b4b53abff70b31d1695a7b66cc6d2e/toddlerbot/descriptions/toddlerbot_2xc/toddlerbot_2xc.xml#L395) |
| right_shoulder_gear_drive / com_registered | [-0.0200079, -0.118, 0.07612614] | [-0.0200079, -0.118, 0.07612614] | [-0.0200079, -0.118, 0.07612614] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L382](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/toddlerbot_2xc/toddlerbot_2xc.xml#L382) | [CoM/kinematic input L407](https://github.com/hshi74/toddlerbot/blob/957aadb8e6db85e02fbb9ef90bbcdb4b4c0c9f6c/toddlerbot/descriptions/toddlerbot_2xc/toddlerbot_2xc.xml#L407) | [CoM/kinematic input L405](https://github.com/hshi74/toddlerbot/blob/e337f3b177b4b53abff70b31d1695a7b66cc6d2e/toddlerbot/descriptions/toddlerbot_2xc/toddlerbot_2xc.xml#L405) |
| right_shoulder_yaw_link / com_registered | [-0.02000769, -0.09400024, 0.0509658] | [-0.02000769, -0.09400024, 0.0509658] | [-0.02000769, -0.09400024, 0.0509658] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L389](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/toddlerbot_2xc/toddlerbot_2xc.xml#L389) | [CoM/kinematic input L415](https://github.com/hshi74/toddlerbot/blob/957aadb8e6db85e02fbb9ef90bbcdb4b4c0c9f6c/toddlerbot/descriptions/toddlerbot_2xc/toddlerbot_2xc.xml#L415) | [CoM/kinematic input L413](https://github.com/hshi74/toddlerbot/blob/e337f3b177b4b53abff70b31d1695a7b66cc6d2e/toddlerbot/descriptions/toddlerbot_2xc/toddlerbot_2xc.xml#L413) |
| right_elbow_roll_link / com_registered | [-0.0195481, -0.1057736, 0.01371352] | [-0.0195481, -0.1057736, 0.01371352] | [-0.0195481, -0.1057736, 0.01371352] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L398](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/toddlerbot_2xc/toddlerbot_2xc.xml#L398) | [CoM/kinematic input L425](https://github.com/hshi74/toddlerbot/blob/957aadb8e6db85e02fbb9ef90bbcdb4b4c0c9f6c/toddlerbot/descriptions/toddlerbot_2xc/toddlerbot_2xc.xml#L425) | [CoM/kinematic input L423](https://github.com/hshi74/toddlerbot/blob/e337f3b177b4b53abff70b31d1695a7b66cc6d2e/toddlerbot/descriptions/toddlerbot_2xc/toddlerbot_2xc.xml#L423) |
| right_elbow_gear_drive / com_registered | [-0.0200079, -0.118, -0.00987386] | [-0.0200079, -0.118, -0.00987386] | [-0.0200079, -0.118, -0.00987386] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L407](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/toddlerbot_2xc/toddlerbot_2xc.xml#L407) | [CoM/kinematic input L435](https://github.com/hshi74/toddlerbot/blob/957aadb8e6db85e02fbb9ef90bbcdb4b4c0c9f6c/toddlerbot/descriptions/toddlerbot_2xc/toddlerbot_2xc.xml#L435) | [CoM/kinematic input L433](https://github.com/hshi74/toddlerbot/blob/e337f3b177b4b53abff70b31d1695a7b66cc6d2e/toddlerbot/descriptions/toddlerbot_2xc/toddlerbot_2xc.xml#L433) |
| right_elbow_yaw_link / com_registered | [-0.02000813, -0.09669789, -0.0426292] | [-0.02000813, -0.09669789, -0.0426292] | [-0.02000813, -0.09669789, -0.0426292] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L414](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/toddlerbot_2xc/toddlerbot_2xc.xml#L414) | [CoM/kinematic input L443](https://github.com/hshi74/toddlerbot/blob/957aadb8e6db85e02fbb9ef90bbcdb4b4c0c9f6c/toddlerbot/descriptions/toddlerbot_2xc/toddlerbot_2xc.xml#L443) | [CoM/kinematic input L441](https://github.com/hshi74/toddlerbot/blob/e337f3b177b4b53abff70b31d1695a7b66cc6d2e/toddlerbot/descriptions/toddlerbot_2xc/toddlerbot_2xc.xml#L441) |
| right_wrist_pitch_link / com_registered | [-0.01959285, -0.0941329, -0.058754] | [-0.01959285, -0.0941329, -0.058754] | [-0.01959285, -0.0941329, -0.058754] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L423](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/toddlerbot_2xc/toddlerbot_2xc.xml#L423) | [CoM/kinematic input L453](https://github.com/hshi74/toddlerbot/blob/957aadb8e6db85e02fbb9ef90bbcdb4b4c0c9f6c/toddlerbot/descriptions/toddlerbot_2xc/toddlerbot_2xc.xml#L453) | [CoM/kinematic input L451](https://github.com/hshi74/toddlerbot/blob/e337f3b177b4b53abff70b31d1695a7b66cc6d2e/toddlerbot/descriptions/toddlerbot_2xc/toddlerbot_2xc.xml#L451) |
| right_wrist_gear_drive / com_registered | [-0.0200079, -0.11803438, -0.04625] | [-0.0200079, -0.11803438, -0.04625] | [-0.0200079, -0.11803438, -0.04625] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L433](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/toddlerbot_2xc/toddlerbot_2xc.xml#L433) | [CoM/kinematic input L463](https://github.com/hshi74/toddlerbot/blob/957aadb8e6db85e02fbb9ef90bbcdb4b4c0c9f6c/toddlerbot/descriptions/toddlerbot_2xc/toddlerbot_2xc.xml#L463) | [CoM/kinematic input L461](https://github.com/hshi74/toddlerbot/blob/e337f3b177b4b53abff70b31d1695a7b66cc6d2e/toddlerbot/descriptions/toddlerbot_2xc/toddlerbot_2xc.xml#L461) |
| right_hand / com_registered | [-0.0213874, -0.09714939, -0.1089053] | [-0.0213874, -0.09714939, -0.1089053] | [-0.0213874, -0.09714939, -0.1089053] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L441](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/toddlerbot_2xc/toddlerbot_2xc.xml#L441) | [CoM/kinematic input L471](https://github.com/hshi74/toddlerbot/blob/957aadb8e6db85e02fbb9ef90bbcdb4b4c0c9f6c/toddlerbot/descriptions/toddlerbot_2xc/toddlerbot_2xc.xml#L471) | [CoM/kinematic input L469](https://github.com/hshi74/toddlerbot/blob/e337f3b177b4b53abff70b31d1695a7b66cc6d2e/toddlerbot/descriptions/toddlerbot_2xc/toddlerbot_2xc.xml#L469) |

## Mass accounting

Every contributing compiled body mass is listed here so total/subtree sums can be checked. Links point to explicit inertials or to geometry inputs when the compiler inferred a mass. CoM links identify inertial inputs; world coordinates additionally use the ancestor transforms and the registration recorded below.

| M body | M kg / source | S kg / source | H kg / source |
|---|---|---|---|
| torso | 1.11503 / [input L40](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/toddlerbot_2xc/toddlerbot_2xc.xml#L40) | 1.11503 / [input L37](https://github.com/hshi74/toddlerbot/blob/957aadb8e6db85e02fbb9ef90bbcdb4b4c0c9f6c/toddlerbot/descriptions/toddlerbot_2xc/toddlerbot_2xc.xml#L37) | 1.11503 / [input L37](https://github.com/hshi74/toddlerbot/blob/e337f3b177b4b53abff70b31d1695a7b66cc6d2e/toddlerbot/descriptions/toddlerbot_2xc/toddlerbot_2xc.xml#L37) |
| neck_yaw_gear_drive | 0.003 / [input L50](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/toddlerbot_2xc/toddlerbot_2xc.xml#L50) | 0.003 / [input L48](https://github.com/hshi74/toddlerbot/blob/957aadb8e6db85e02fbb9ef90bbcdb4b4c0c9f6c/toddlerbot/descriptions/toddlerbot_2xc/toddlerbot_2xc.xml#L48) | 0.003 / [input L48](https://github.com/hshi74/toddlerbot/blob/e337f3b177b4b53abff70b31d1695a7b66cc6d2e/toddlerbot/descriptions/toddlerbot_2xc/toddlerbot_2xc.xml#L48) |
| neck_yaw_link | 0.006 / [input L57](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/toddlerbot_2xc/toddlerbot_2xc.xml#L57) | 0.006 / [input L55](https://github.com/hshi74/toddlerbot/blob/957aadb8e6db85e02fbb9ef90bbcdb4b4c0c9f6c/toddlerbot/descriptions/toddlerbot_2xc/toddlerbot_2xc.xml#L55) | 0.006 / [input L55](https://github.com/hshi74/toddlerbot/blob/e337f3b177b4b53abff70b31d1695a7b66cc6d2e/toddlerbot/descriptions/toddlerbot_2xc/toddlerbot_2xc.xml#L55) |
| head | 0.143321 / [input L71](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/toddlerbot_2xc/toddlerbot_2xc.xml#L71) | 0.143321 / [input L69](https://github.com/hshi74/toddlerbot/blob/957aadb8e6db85e02fbb9ef90bbcdb4b4c0c9f6c/toddlerbot/descriptions/toddlerbot_2xc/toddlerbot_2xc.xml#L69) | 0.143321 / [input L69](https://github.com/hshi74/toddlerbot/blob/e337f3b177b4b53abff70b31d1695a7b66cc6d2e/toddlerbot/descriptions/toddlerbot_2xc/toddlerbot_2xc.xml#L69) |
| neck_pitch_plate | 0.002 / [input L79](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/toddlerbot_2xc/toddlerbot_2xc.xml#L79) | 0.002 / [input L78](https://github.com/hshi74/toddlerbot/blob/957aadb8e6db85e02fbb9ef90bbcdb4b4c0c9f6c/toddlerbot/descriptions/toddlerbot_2xc/toddlerbot_2xc.xml#L78) | 0.002 / [input L78](https://github.com/hshi74/toddlerbot/blob/e337f3b177b4b53abff70b31d1695a7b66cc6d2e/toddlerbot/descriptions/toddlerbot_2xc/toddlerbot_2xc.xml#L78) |
| neck_rod | 0.00297389 / [input L85](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/toddlerbot_2xc/toddlerbot_2xc.xml#L85) | 0.00297389 / [input L85](https://github.com/hshi74/toddlerbot/blob/957aadb8e6db85e02fbb9ef90bbcdb4b4c0c9f6c/toddlerbot/descriptions/toddlerbot_2xc/toddlerbot_2xc.xml#L85) | 0.00297389 / [input L85](https://github.com/hshi74/toddlerbot/blob/e337f3b177b4b53abff70b31d1695a7b66cc6d2e/toddlerbot/descriptions/toddlerbot_2xc/toddlerbot_2xc.xml#L85) |
| neck_rod_2 | 0.00297389 / [input L96](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/toddlerbot_2xc/toddlerbot_2xc.xml#L96) | 0.00297389 / [input L97](https://github.com/hshi74/toddlerbot/blob/957aadb8e6db85e02fbb9ef90bbcdb4b4c0c9f6c/toddlerbot/descriptions/toddlerbot_2xc/toddlerbot_2xc.xml#L97) | 0.00297389 / [input L97](https://github.com/hshi74/toddlerbot/blob/e337f3b177b4b53abff70b31d1695a7b66cc6d2e/toddlerbot/descriptions/toddlerbot_2xc/toddlerbot_2xc.xml#L97) |
| waist_gears | 0.0371617 / [input L110](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/toddlerbot_2xc/toddlerbot_2xc.xml#L110) | 0.0371617 / [input L111](https://github.com/hshi74/toddlerbot/blob/957aadb8e6db85e02fbb9ef90bbcdb4b4c0c9f6c/toddlerbot/descriptions/toddlerbot_2xc/toddlerbot_2xc.xml#L111) | 0.0371617 / [input L111](https://github.com/hshi74/toddlerbot/blob/e337f3b177b4b53abff70b31d1695a7b66cc6d2e/toddlerbot/descriptions/toddlerbot_2xc/toddlerbot_2xc.xml#L111) |
| pelvis_link | 0.1052 / [input L117](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/toddlerbot_2xc/toddlerbot_2xc.xml#L117) | 0.1052 / [input L118](https://github.com/hshi74/toddlerbot/blob/957aadb8e6db85e02fbb9ef90bbcdb4b4c0c9f6c/toddlerbot/descriptions/toddlerbot_2xc/toddlerbot_2xc.xml#L118) | 0.1052 / [input L118](https://github.com/hshi74/toddlerbot/blob/e337f3b177b4b53abff70b31d1695a7b66cc6d2e/toddlerbot/descriptions/toddlerbot_2xc/toddlerbot_2xc.xml#L118) |
| waist_gear_drive | 0.002 / [input L125](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/toddlerbot_2xc/toddlerbot_2xc.xml#L125) | 0.002 / [input L127](https://github.com/hshi74/toddlerbot/blob/957aadb8e6db85e02fbb9ef90bbcdb4b4c0c9f6c/toddlerbot/descriptions/toddlerbot_2xc/toddlerbot_2xc.xml#L127) | 0.002 / [input L127](https://github.com/hshi74/toddlerbot/blob/e337f3b177b4b53abff70b31d1695a7b66cc6d2e/toddlerbot/descriptions/toddlerbot_2xc/toddlerbot_2xc.xml#L127) |
| waist_gear_drive_2 | 0.002 / [input L132](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/toddlerbot_2xc/toddlerbot_2xc.xml#L132) | 0.002 / [input L135](https://github.com/hshi74/toddlerbot/blob/957aadb8e6db85e02fbb9ef90bbcdb4b4c0c9f6c/toddlerbot/descriptions/toddlerbot_2xc/toddlerbot_2xc.xml#L135) | 0.002 / [input L135](https://github.com/hshi74/toddlerbot/blob/e337f3b177b4b53abff70b31d1695a7b66cc6d2e/toddlerbot/descriptions/toddlerbot_2xc/toddlerbot_2xc.xml#L135) |
| left_hip_pitch_link | 0.1106 / [input L139](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/toddlerbot_2xc/toddlerbot_2xc.xml#L139) | 0.1106 / [input L143](https://github.com/hshi74/toddlerbot/blob/957aadb8e6db85e02fbb9ef90bbcdb4b4c0c9f6c/toddlerbot/descriptions/toddlerbot_2xc/toddlerbot_2xc.xml#L143) | 0.1106 / [input L143](https://github.com/hshi74/toddlerbot/blob/e337f3b177b4b53abff70b31d1695a7b66cc6d2e/toddlerbot/descriptions/toddlerbot_2xc/toddlerbot_2xc.xml#L143) |
| left_hip_roll_link | 0.022 / [input L148](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/toddlerbot_2xc/toddlerbot_2xc.xml#L148) | 0.022 / [input L153](https://github.com/hshi74/toddlerbot/blob/957aadb8e6db85e02fbb9ef90bbcdb4b4c0c9f6c/toddlerbot/descriptions/toddlerbot_2xc/toddlerbot_2xc.xml#L153) | 0.022 / [input L153](https://github.com/hshi74/toddlerbot/blob/e337f3b177b4b53abff70b31d1695a7b66cc6d2e/toddlerbot/descriptions/toddlerbot_2xc/toddlerbot_2xc.xml#L153) |
| left_hip_yaw_link | 0.159688 / [input L154](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/toddlerbot_2xc/toddlerbot_2xc.xml#L154) | 0.159688 / [input L160](https://github.com/hshi74/toddlerbot/blob/957aadb8e6db85e02fbb9ef90bbcdb4b4c0c9f6c/toddlerbot/descriptions/toddlerbot_2xc/toddlerbot_2xc.xml#L160) | 0.159688 / [input L160](https://github.com/hshi74/toddlerbot/blob/e337f3b177b4b53abff70b31d1695a7b66cc6d2e/toddlerbot/descriptions/toddlerbot_2xc/toddlerbot_2xc.xml#L160) |
| left_hip_yaw_gear_drive | 0.001 / [input L163](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/toddlerbot_2xc/toddlerbot_2xc.xml#L163) | 0.001 / [input L170](https://github.com/hshi74/toddlerbot/blob/957aadb8e6db85e02fbb9ef90bbcdb4b4c0c9f6c/toddlerbot/descriptions/toddlerbot_2xc/toddlerbot_2xc.xml#L170) | 0.001 / [input L170](https://github.com/hshi74/toddlerbot/blob/e337f3b177b4b53abff70b31d1695a7b66cc6d2e/toddlerbot/descriptions/toddlerbot_2xc/toddlerbot_2xc.xml#L170) |
| left_knee_link | 0.029 / [input L170](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/toddlerbot_2xc/toddlerbot_2xc.xml#L170) | 0.029 / [input L178](https://github.com/hshi74/toddlerbot/blob/957aadb8e6db85e02fbb9ef90bbcdb4b4c0c9f6c/toddlerbot/descriptions/toddlerbot_2xc/toddlerbot_2xc.xml#L178) | 0.029 / [input L178](https://github.com/hshi74/toddlerbot/blob/e337f3b177b4b53abff70b31d1695a7b66cc6d2e/toddlerbot/descriptions/toddlerbot_2xc/toddlerbot_2xc.xml#L178) |
| left_ankle_pitch_link | 0.172721 / [input L179](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/toddlerbot_2xc/toddlerbot_2xc.xml#L179) | 0.172721 / [input L187](https://github.com/hshi74/toddlerbot/blob/957aadb8e6db85e02fbb9ef90bbcdb4b4c0c9f6c/toddlerbot/descriptions/toddlerbot_2xc/toddlerbot_2xc.xml#L187) | 0.172721 / [input L187](https://github.com/hshi74/toddlerbot/blob/e337f3b177b4b53abff70b31d1695a7b66cc6d2e/toddlerbot/descriptions/toddlerbot_2xc/toddlerbot_2xc.xml#L187) |
| left_ankle_roll_link | 0.039 / [input L189](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/toddlerbot_2xc/toddlerbot_2xc.xml#L189) | 0.039 / [input L197](https://github.com/hshi74/toddlerbot/blob/957aadb8e6db85e02fbb9ef90bbcdb4b4c0c9f6c/toddlerbot/descriptions/toddlerbot_2xc/toddlerbot_2xc.xml#L197) | 0.039 / [input L197](https://github.com/hshi74/toddlerbot/blob/e337f3b177b4b53abff70b31d1695a7b66cc6d2e/toddlerbot/descriptions/toddlerbot_2xc/toddlerbot_2xc.xml#L197) |
| right_hip_pitch_link | 0.1106 / [input L206](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/toddlerbot_2xc/toddlerbot_2xc.xml#L206) | 0.1106 / [input L216](https://github.com/hshi74/toddlerbot/blob/957aadb8e6db85e02fbb9ef90bbcdb4b4c0c9f6c/toddlerbot/descriptions/toddlerbot_2xc/toddlerbot_2xc.xml#L216) | 0.1106 / [input L215](https://github.com/hshi74/toddlerbot/blob/e337f3b177b4b53abff70b31d1695a7b66cc6d2e/toddlerbot/descriptions/toddlerbot_2xc/toddlerbot_2xc.xml#L215) |
| right_hip_roll_link | 0.022 / [input L215](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/toddlerbot_2xc/toddlerbot_2xc.xml#L215) | 0.022 / [input L226](https://github.com/hshi74/toddlerbot/blob/957aadb8e6db85e02fbb9ef90bbcdb4b4c0c9f6c/toddlerbot/descriptions/toddlerbot_2xc/toddlerbot_2xc.xml#L226) | 0.022 / [input L225](https://github.com/hshi74/toddlerbot/blob/e337f3b177b4b53abff70b31d1695a7b66cc6d2e/toddlerbot/descriptions/toddlerbot_2xc/toddlerbot_2xc.xml#L225) |
| right_hip_yaw_link | 0.159688 / [input L221](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/toddlerbot_2xc/toddlerbot_2xc.xml#L221) | 0.159688 / [input L233](https://github.com/hshi74/toddlerbot/blob/957aadb8e6db85e02fbb9ef90bbcdb4b4c0c9f6c/toddlerbot/descriptions/toddlerbot_2xc/toddlerbot_2xc.xml#L233) | 0.159688 / [input L232](https://github.com/hshi74/toddlerbot/blob/e337f3b177b4b53abff70b31d1695a7b66cc6d2e/toddlerbot/descriptions/toddlerbot_2xc/toddlerbot_2xc.xml#L232) |
| right_hip_yaw_gear_drive | 0.001 / [input L230](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/toddlerbot_2xc/toddlerbot_2xc.xml#L230) | 0.001 / [input L243](https://github.com/hshi74/toddlerbot/blob/957aadb8e6db85e02fbb9ef90bbcdb4b4c0c9f6c/toddlerbot/descriptions/toddlerbot_2xc/toddlerbot_2xc.xml#L243) | 0.001 / [input L242](https://github.com/hshi74/toddlerbot/blob/e337f3b177b4b53abff70b31d1695a7b66cc6d2e/toddlerbot/descriptions/toddlerbot_2xc/toddlerbot_2xc.xml#L242) |
| right_knee_link | 0.029 / [input L238](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/toddlerbot_2xc/toddlerbot_2xc.xml#L238) | 0.029 / [input L251](https://github.com/hshi74/toddlerbot/blob/957aadb8e6db85e02fbb9ef90bbcdb4b4c0c9f6c/toddlerbot/descriptions/toddlerbot_2xc/toddlerbot_2xc.xml#L251) | 0.029 / [input L250](https://github.com/hshi74/toddlerbot/blob/e337f3b177b4b53abff70b31d1695a7b66cc6d2e/toddlerbot/descriptions/toddlerbot_2xc/toddlerbot_2xc.xml#L250) |
| right_ankle_pitch_link | 0.172721 / [input L247](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/toddlerbot_2xc/toddlerbot_2xc.xml#L247) | 0.172721 / [input L260](https://github.com/hshi74/toddlerbot/blob/957aadb8e6db85e02fbb9ef90bbcdb4b4c0c9f6c/toddlerbot/descriptions/toddlerbot_2xc/toddlerbot_2xc.xml#L260) | 0.172721 / [input L259](https://github.com/hshi74/toddlerbot/blob/e337f3b177b4b53abff70b31d1695a7b66cc6d2e/toddlerbot/descriptions/toddlerbot_2xc/toddlerbot_2xc.xml#L259) |
| right_ankle_roll_link | 0.039 / [input L257](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/toddlerbot_2xc/toddlerbot_2xc.xml#L257) | 0.039 / [input L270](https://github.com/hshi74/toddlerbot/blob/957aadb8e6db85e02fbb9ef90bbcdb4b4c0c9f6c/toddlerbot/descriptions/toddlerbot_2xc/toddlerbot_2xc.xml#L270) | 0.039 / [input L269](https://github.com/hshi74/toddlerbot/blob/e337f3b177b4b53abff70b31d1695a7b66cc6d2e/toddlerbot/descriptions/toddlerbot_2xc/toddlerbot_2xc.xml#L269) |
| left_shoulder_pitch_link | 0.015 / [input L276](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/toddlerbot_2xc/toddlerbot_2xc.xml#L276) | 0.015 / [input L291](https://github.com/hshi74/toddlerbot/blob/957aadb8e6db85e02fbb9ef90bbcdb4b4c0c9f6c/toddlerbot/descriptions/toddlerbot_2xc/toddlerbot_2xc.xml#L291) | 0.015 / [input L289](https://github.com/hshi74/toddlerbot/blob/e337f3b177b4b53abff70b31d1695a7b66cc6d2e/toddlerbot/descriptions/toddlerbot_2xc/toddlerbot_2xc.xml#L289) |
| left_shoulder_roll_link | 0.1152 / [input L282](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/toddlerbot_2xc/toddlerbot_2xc.xml#L282) | 0.1152 / [input L298](https://github.com/hshi74/toddlerbot/blob/957aadb8e6db85e02fbb9ef90bbcdb4b4c0c9f6c/toddlerbot/descriptions/toddlerbot_2xc/toddlerbot_2xc.xml#L298) | 0.1152 / [input L296](https://github.com/hshi74/toddlerbot/blob/e337f3b177b4b53abff70b31d1695a7b66cc6d2e/toddlerbot/descriptions/toddlerbot_2xc/toddlerbot_2xc.xml#L296) |
| left_shoulder_gear_drive | 0.004 / [input L291](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/toddlerbot_2xc/toddlerbot_2xc.xml#L291) | 0.004 / [input L308](https://github.com/hshi74/toddlerbot/blob/957aadb8e6db85e02fbb9ef90bbcdb4b4c0c9f6c/toddlerbot/descriptions/toddlerbot_2xc/toddlerbot_2xc.xml#L308) | 0.004 / [input L306](https://github.com/hshi74/toddlerbot/blob/e337f3b177b4b53abff70b31d1695a7b66cc6d2e/toddlerbot/descriptions/toddlerbot_2xc/toddlerbot_2xc.xml#L306) |
| left_shoulder_yaw_link | 0.0247439 / [input L298](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/toddlerbot_2xc/toddlerbot_2xc.xml#L298) | 0.0247439 / [input L316](https://github.com/hshi74/toddlerbot/blob/957aadb8e6db85e02fbb9ef90bbcdb4b4c0c9f6c/toddlerbot/descriptions/toddlerbot_2xc/toddlerbot_2xc.xml#L316) | 0.0247439 / [input L314](https://github.com/hshi74/toddlerbot/blob/e337f3b177b4b53abff70b31d1695a7b66cc6d2e/toddlerbot/descriptions/toddlerbot_2xc/toddlerbot_2xc.xml#L314) |
| left_elbow_roll_link | 0.1152 / [input L306](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/toddlerbot_2xc/toddlerbot_2xc.xml#L306) | 0.1152 / [input L326](https://github.com/hshi74/toddlerbot/blob/957aadb8e6db85e02fbb9ef90bbcdb4b4c0c9f6c/toddlerbot/descriptions/toddlerbot_2xc/toddlerbot_2xc.xml#L326) | 0.1152 / [input L324](https://github.com/hshi74/toddlerbot/blob/e337f3b177b4b53abff70b31d1695a7b66cc6d2e/toddlerbot/descriptions/toddlerbot_2xc/toddlerbot_2xc.xml#L324) |
| left_elbow_gear_drive | 0.004 / [input L315](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/toddlerbot_2xc/toddlerbot_2xc.xml#L315) | 0.004 / [input L336](https://github.com/hshi74/toddlerbot/blob/957aadb8e6db85e02fbb9ef90bbcdb4b4c0c9f6c/toddlerbot/descriptions/toddlerbot_2xc/toddlerbot_2xc.xml#L336) | 0.004 / [input L334](https://github.com/hshi74/toddlerbot/blob/e337f3b177b4b53abff70b31d1695a7b66cc6d2e/toddlerbot/descriptions/toddlerbot_2xc/toddlerbot_2xc.xml#L334) |
| left_elbow_yaw_link | 0.0302318 / [input L322](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/toddlerbot_2xc/toddlerbot_2xc.xml#L322) | 0.0302318 / [input L344](https://github.com/hshi74/toddlerbot/blob/957aadb8e6db85e02fbb9ef90bbcdb4b4c0c9f6c/toddlerbot/descriptions/toddlerbot_2xc/toddlerbot_2xc.xml#L344) | 0.0302318 / [input L342](https://github.com/hshi74/toddlerbot/blob/e337f3b177b4b53abff70b31d1695a7b66cc6d2e/toddlerbot/descriptions/toddlerbot_2xc/toddlerbot_2xc.xml#L342) |
| left_wrist_pitch_link | 0.1276 / [input L331](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/toddlerbot_2xc/toddlerbot_2xc.xml#L331) | 0.1276 / [input L354](https://github.com/hshi74/toddlerbot/blob/957aadb8e6db85e02fbb9ef90bbcdb4b4c0c9f6c/toddlerbot/descriptions/toddlerbot_2xc/toddlerbot_2xc.xml#L354) | 0.1276 / [input L352](https://github.com/hshi74/toddlerbot/blob/e337f3b177b4b53abff70b31d1695a7b66cc6d2e/toddlerbot/descriptions/toddlerbot_2xc/toddlerbot_2xc.xml#L352) |
| left_wrist_gear_drive | 0.003 / [input L341](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/toddlerbot_2xc/toddlerbot_2xc.xml#L341) | 0.003 / [input L364](https://github.com/hshi74/toddlerbot/blob/957aadb8e6db85e02fbb9ef90bbcdb4b4c0c9f6c/toddlerbot/descriptions/toddlerbot_2xc/toddlerbot_2xc.xml#L364) | 0.003 / [input L362](https://github.com/hshi74/toddlerbot/blob/e337f3b177b4b53abff70b31d1695a7b66cc6d2e/toddlerbot/descriptions/toddlerbot_2xc/toddlerbot_2xc.xml#L362) |
| left_hand | 0.043 / [input L349](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/toddlerbot_2xc/toddlerbot_2xc.xml#L349) | 0.043 / [input L372](https://github.com/hshi74/toddlerbot/blob/957aadb8e6db85e02fbb9ef90bbcdb4b4c0c9f6c/toddlerbot/descriptions/toddlerbot_2xc/toddlerbot_2xc.xml#L372) | 0.043 / [input L370](https://github.com/hshi74/toddlerbot/blob/e337f3b177b4b53abff70b31d1695a7b66cc6d2e/toddlerbot/descriptions/toddlerbot_2xc/toddlerbot_2xc.xml#L370) |
| right_shoulder_pitch_link | 0.015 / [input L366](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/toddlerbot_2xc/toddlerbot_2xc.xml#L366) | 0.015 / [input L390](https://github.com/hshi74/toddlerbot/blob/957aadb8e6db85e02fbb9ef90bbcdb4b4c0c9f6c/toddlerbot/descriptions/toddlerbot_2xc/toddlerbot_2xc.xml#L390) | 0.015 / [input L388](https://github.com/hshi74/toddlerbot/blob/e337f3b177b4b53abff70b31d1695a7b66cc6d2e/toddlerbot/descriptions/toddlerbot_2xc/toddlerbot_2xc.xml#L388) |
| right_shoulder_roll_link | 0.1152 / [input L373](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/toddlerbot_2xc/toddlerbot_2xc.xml#L373) | 0.1152 / [input L397](https://github.com/hshi74/toddlerbot/blob/957aadb8e6db85e02fbb9ef90bbcdb4b4c0c9f6c/toddlerbot/descriptions/toddlerbot_2xc/toddlerbot_2xc.xml#L397) | 0.1152 / [input L395](https://github.com/hshi74/toddlerbot/blob/e337f3b177b4b53abff70b31d1695a7b66cc6d2e/toddlerbot/descriptions/toddlerbot_2xc/toddlerbot_2xc.xml#L395) |
| right_shoulder_gear_drive | 0.004 / [input L382](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/toddlerbot_2xc/toddlerbot_2xc.xml#L382) | 0.004 / [input L407](https://github.com/hshi74/toddlerbot/blob/957aadb8e6db85e02fbb9ef90bbcdb4b4c0c9f6c/toddlerbot/descriptions/toddlerbot_2xc/toddlerbot_2xc.xml#L407) | 0.004 / [input L405](https://github.com/hshi74/toddlerbot/blob/e337f3b177b4b53abff70b31d1695a7b66cc6d2e/toddlerbot/descriptions/toddlerbot_2xc/toddlerbot_2xc.xml#L405) |
| right_shoulder_yaw_link | 0.0247439 / [input L389](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/toddlerbot_2xc/toddlerbot_2xc.xml#L389) | 0.0247439 / [input L415](https://github.com/hshi74/toddlerbot/blob/957aadb8e6db85e02fbb9ef90bbcdb4b4c0c9f6c/toddlerbot/descriptions/toddlerbot_2xc/toddlerbot_2xc.xml#L415) | 0.0247439 / [input L413](https://github.com/hshi74/toddlerbot/blob/e337f3b177b4b53abff70b31d1695a7b66cc6d2e/toddlerbot/descriptions/toddlerbot_2xc/toddlerbot_2xc.xml#L413) |
| right_elbow_roll_link | 0.1152 / [input L398](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/toddlerbot_2xc/toddlerbot_2xc.xml#L398) | 0.1152 / [input L425](https://github.com/hshi74/toddlerbot/blob/957aadb8e6db85e02fbb9ef90bbcdb4b4c0c9f6c/toddlerbot/descriptions/toddlerbot_2xc/toddlerbot_2xc.xml#L425) | 0.1152 / [input L423](https://github.com/hshi74/toddlerbot/blob/e337f3b177b4b53abff70b31d1695a7b66cc6d2e/toddlerbot/descriptions/toddlerbot_2xc/toddlerbot_2xc.xml#L423) |
| right_elbow_gear_drive | 0.004 / [input L407](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/toddlerbot_2xc/toddlerbot_2xc.xml#L407) | 0.004 / [input L435](https://github.com/hshi74/toddlerbot/blob/957aadb8e6db85e02fbb9ef90bbcdb4b4c0c9f6c/toddlerbot/descriptions/toddlerbot_2xc/toddlerbot_2xc.xml#L435) | 0.004 / [input L433](https://github.com/hshi74/toddlerbot/blob/e337f3b177b4b53abff70b31d1695a7b66cc6d2e/toddlerbot/descriptions/toddlerbot_2xc/toddlerbot_2xc.xml#L433) |
| right_elbow_yaw_link | 0.0302318 / [input L414](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/toddlerbot_2xc/toddlerbot_2xc.xml#L414) | 0.0302318 / [input L443](https://github.com/hshi74/toddlerbot/blob/957aadb8e6db85e02fbb9ef90bbcdb4b4c0c9f6c/toddlerbot/descriptions/toddlerbot_2xc/toddlerbot_2xc.xml#L443) | 0.0302318 / [input L441](https://github.com/hshi74/toddlerbot/blob/e337f3b177b4b53abff70b31d1695a7b66cc6d2e/toddlerbot/descriptions/toddlerbot_2xc/toddlerbot_2xc.xml#L441) |
| right_wrist_pitch_link | 0.1276 / [input L423](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/toddlerbot_2xc/toddlerbot_2xc.xml#L423) | 0.1276 / [input L453](https://github.com/hshi74/toddlerbot/blob/957aadb8e6db85e02fbb9ef90bbcdb4b4c0c9f6c/toddlerbot/descriptions/toddlerbot_2xc/toddlerbot_2xc.xml#L453) | 0.1276 / [input L451](https://github.com/hshi74/toddlerbot/blob/e337f3b177b4b53abff70b31d1695a7b66cc6d2e/toddlerbot/descriptions/toddlerbot_2xc/toddlerbot_2xc.xml#L451) |
| right_wrist_gear_drive | 0.003 / [input L433](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/toddlerbot_2xc/toddlerbot_2xc.xml#L433) | 0.003 / [input L463](https://github.com/hshi74/toddlerbot/blob/957aadb8e6db85e02fbb9ef90bbcdb4b4c0c9f6c/toddlerbot/descriptions/toddlerbot_2xc/toddlerbot_2xc.xml#L463) | 0.003 / [input L461](https://github.com/hshi74/toddlerbot/blob/e337f3b177b4b53abff70b31d1695a7b66cc6d2e/toddlerbot/descriptions/toddlerbot_2xc/toddlerbot_2xc.xml#L461) |
| right_hand | 0.043 / [input L441](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/toddlerbot_2xc/toddlerbot_2xc.xml#L441) | 0.043 / [input L471](https://github.com/hshi74/toddlerbot/blob/957aadb8e6db85e02fbb9ef90bbcdb4b4c0c9f6c/toddlerbot/descriptions/toddlerbot_2xc/toddlerbot_2xc.xml#L471) | 0.043 / [input L469](https://github.com/hshi74/toddlerbot/blob/e337f3b177b4b53abff70b31d1695a7b66cc6d2e/toddlerbot/descriptions/toddlerbot_2xc/toddlerbot_2xc.xml#L469) |

## Coverage and unmatched elements

```json
{
  "mapping_h": {
    "bodies": {
      "torso": "torso",
      "neck_yaw_gear_drive": "neck_yaw_gear_drive",
      "neck_yaw_link": "neck_yaw_link",
      "head": "head",
      "neck_pitch_plate": "neck_pitch_plate",
      "neck_rod": "neck_rod",
      "neck_rod_2": "neck_rod_2",
      "waist_gears": "waist_gears",
      "pelvis_link": "pelvis_link",
      "waist_gear_drive": "waist_gear_drive",
      "waist_gear_drive_2": "waist_gear_drive_2",
      "left_hip_pitch_link": "left_hip_pitch_link",
      "left_hip_roll_link": "left_hip_roll_link",
      "left_hip_yaw_link": "left_hip_yaw_link",
      "left_hip_yaw_gear_drive": "left_hip_yaw_gear_drive",
      "left_knee_link": "left_knee_link",
      "left_ankle_pitch_link": "left_ankle_pitch_link",
      "left_ankle_roll_link": "left_ankle_roll_link",
      "right_hip_pitch_link": "right_hip_pitch_link",
      "right_hip_roll_link": "right_hip_roll_link",
      "right_hip_yaw_link": "right_hip_yaw_link",
      "right_hip_yaw_gear_drive": "right_hip_yaw_gear_drive",
      "right_knee_link": "right_knee_link",
      "right_ankle_pitch_link": "right_ankle_pitch_link",
      "right_ankle_roll_link": "right_ankle_roll_link",
      "left_shoulder_pitch_link": "left_shoulder_pitch_link",
      "left_shoulder_roll_link": "left_shoulder_roll_link",
      "left_shoulder_gear_drive": "left_shoulder_gear_drive",
      "left_shoulder_yaw_link": "left_shoulder_yaw_link",
      "left_elbow_roll_link": "left_elbow_roll_link",
      "left_elbow_gear_drive": "left_elbow_gear_drive",
      "left_elbow_yaw_link": "left_elbow_yaw_link",
      "left_wrist_pitch_link": "left_wrist_pitch_link",
      "left_wrist_gear_drive": "left_wrist_gear_drive",
      "left_hand": "left_hand",
      "right_shoulder_pitch_link": "right_shoulder_pitch_link",
      "right_shoulder_roll_link": "right_shoulder_roll_link",
      "right_shoulder_gear_drive": "right_shoulder_gear_drive",
      "right_shoulder_yaw_link": "right_shoulder_yaw_link",
      "right_elbow_roll_link": "right_elbow_roll_link",
      "right_elbow_gear_drive": "right_elbow_gear_drive",
      "right_elbow_yaw_link": "right_elbow_yaw_link",
      "right_wrist_pitch_link": "right_wrist_pitch_link",
      "right_wrist_gear_drive": "right_wrist_gear_drive",
      "right_hand": "right_hand"
    },
    "joints": {
      "neck_yaw_drive": "neck_yaw_drive",
      "neck_yaw_driven": "neck_yaw_driven",
      "neck_pitch": "neck_pitch",
      "neck_pitch_act": "neck_pitch_act",
      "neck_pitch_front": "neck_pitch_front",
      "neck_pitch_back": "neck_pitch_back",
      "waist_yaw": "waist_yaw",
      "waist_roll": "waist_roll",
      "waist_act_1": "waist_act_1",
      "waist_act_2": "waist_act_2",
      "left_hip_pitch": "left_hip_pitch",
      "left_hip_roll": "left_hip_roll",
      "left_hip_yaw_driven": "left_hip_yaw_driven",
      "left_hip_yaw_drive": "left_hip_yaw_drive",
      "left_knee": "left_knee",
      "left_ankle_pitch": "left_ankle_pitch",
      "left_ankle_roll": "left_ankle_roll",
      "right_hip_pitch": "right_hip_pitch",
      "right_hip_roll": "right_hip_roll",
      "right_hip_yaw_driven": "right_hip_yaw_driven",
      "right_hip_yaw_drive": "right_hip_yaw_drive",
      "right_knee": "right_knee",
      "right_ankle_pitch": "right_ankle_pitch",
      "right_ankle_roll": "right_ankle_roll",
      "left_shoulder_pitch": "left_shoulder_pitch",
      "left_shoulder_roll": "left_shoulder_roll",
      "left_shoulder_yaw_drive": "left_shoulder_yaw_drive",
      "left_shoulder_yaw_driven": "left_shoulder_yaw_driven",
      "left_elbow_roll": "left_elbow_roll",
      "left_elbow_yaw_drive": "left_elbow_yaw_drive",
      "left_elbow_yaw_driven": "left_elbow_yaw_driven",
      "left_wrist_pitch_driven": "left_wrist_pitch_driven",
      "left_wrist_pitch_drive": "left_wrist_pitch_drive",
      "left_wrist_roll": "left_wrist_roll",
      "right_shoulder_pitch": "right_shoulder_pitch",
      "right_shoulder_roll": "right_shoulder_roll",
      "right_shoulder_yaw_drive": "right_shoulder_yaw_drive",
      "right_shoulder_yaw_driven": "right_shoulder_yaw_driven",
      "right_elbow_roll": "right_elbow_roll",
      "right_elbow_yaw_drive": "right_elbow_yaw_drive",
      "right_elbow_yaw_driven": "right_elbow_yaw_driven",
      "right_wrist_pitch_driven": "right_wrist_pitch_driven",
      "right_wrist_pitch_drive": "right_wrist_pitch_drive",
      "right_wrist_roll": "right_wrist_roll"
    },
    "body_methods": {
      "torso": "name",
      "neck_yaw_gear_drive": "name",
      "neck_yaw_link": "name",
      "head": "name",
      "neck_pitch_plate": "name",
      "neck_rod": "name",
      "neck_rod_2": "name",
      "waist_gears": "name",
      "pelvis_link": "name",
      "waist_gear_drive": "name",
      "waist_gear_drive_2": "name",
      "left_hip_pitch_link": "name",
      "left_hip_roll_link": "name",
      "left_hip_yaw_link": "name",
      "left_hip_yaw_gear_drive": "name",
      "left_knee_link": "name",
      "left_ankle_pitch_link": "name",
      "left_ankle_roll_link": "name",
      "right_hip_pitch_link": "name",
      "right_hip_roll_link": "name",
      "right_hip_yaw_link": "name",
      "right_hip_yaw_gear_drive": "name",
      "right_knee_link": "name",
      "right_ankle_pitch_link": "name",
      "right_ankle_roll_link": "name",
      "left_shoulder_pitch_link": "name",
      "left_shoulder_roll_link": "name",
      "left_shoulder_gear_drive": "name",
      "left_shoulder_yaw_link": "name",
      "left_elbow_roll_link": "name",
      "left_elbow_gear_drive": "name",
      "left_elbow_yaw_link": "name",
      "left_wrist_pitch_link": "name",
      "left_wrist_gear_drive": "name",
      "left_hand": "name",
      "right_shoulder_pitch_link": "name",
      "right_shoulder_roll_link": "name",
      "right_shoulder_gear_drive": "name",
      "right_shoulder_yaw_link": "name",
      "right_elbow_roll_link": "name",
      "right_elbow_gear_drive": "name",
      "right_elbow_yaw_link": "name",
      "right_wrist_pitch_link": "name",
      "right_wrist_gear_drive": "name",
      "right_hand": "name"
    },
    "joint_methods": {
      "neck_yaw_drive": "name",
      "neck_yaw_driven": "name",
      "neck_pitch": "name",
      "neck_pitch_act": "name",
      "neck_pitch_front": "name",
      "neck_pitch_back": "name",
      "waist_yaw": "name",
      "waist_roll": "name",
      "waist_act_1": "name",
      "waist_act_2": "name",
      "left_hip_pitch": "name",
      "left_hip_roll": "name",
      "left_hip_yaw_driven": "name",
      "left_hip_yaw_drive": "name",
      "left_knee": "name",
      "left_ankle_pitch": "name",
      "left_ankle_roll": "name",
      "right_hip_pitch": "name",
      "right_hip_roll": "name",
      "right_hip_yaw_driven": "name",
      "right_hip_yaw_drive": "name",
      "right_knee": "name",
      "right_ankle_pitch": "name",
      "right_ankle_roll": "name",
      "left_shoulder_pitch": "name",
      "left_shoulder_roll": "name",
      "left_shoulder_yaw_drive": "name",
      "left_shoulder_yaw_driven": "name",
      "left_elbow_roll": "name",
      "left_elbow_yaw_drive": "name",
      "left_elbow_yaw_driven": "name",
      "left_wrist_pitch_driven": "name",
      "left_wrist_pitch_drive": "name",
      "left_wrist_roll": "name",
      "right_shoulder_pitch": "name",
      "right_shoulder_roll": "name",
      "right_shoulder_yaw_drive": "name",
      "right_shoulder_yaw_driven": "name",
      "right_elbow_roll": "name",
      "right_elbow_yaw_drive": "name",
      "right_elbow_yaw_driven": "name",
      "right_wrist_pitch_driven": "name",
      "right_wrist_pitch_drive": "name",
      "right_wrist_roll": "name"
    },
    "unmatched_m_bodies": [],
    "unmatched_upstream_bodies": [],
    "unmatched_m_joints": [],
    "unmatched_upstream_joints": [],
    "registration_anchor": {
      "M": "torso",
      "H": "torso",
      "root_unmatched": false
    }
  },
  "mapping_s": {
    "bodies": {
      "torso": "torso",
      "neck_yaw_gear_drive": "neck_yaw_gear_drive",
      "neck_yaw_link": "neck_yaw_link",
      "head": "head",
      "neck_pitch_plate": "neck_pitch_plate",
      "neck_rod": "neck_rod",
      "neck_rod_2": "neck_rod_2",
      "waist_gears": "waist_gears",
      "pelvis_link": "pelvis_link",
      "waist_gear_drive": "waist_gear_drive",
      "waist_gear_drive_2": "waist_gear_drive_2",
      "left_hip_pitch_link": "left_hip_pitch_link",
      "left_hip_roll_link": "left_hip_roll_link",
      "left_hip_yaw_link": "left_hip_yaw_link",
      "left_hip_yaw_gear_drive": "left_hip_yaw_gear_drive",
      "left_knee_link": "left_knee_link",
      "left_ankle_pitch_link": "left_ankle_pitch_link",
      "left_ankle_roll_link": "left_ankle_roll_link",
      "right_hip_pitch_link": "right_hip_pitch_link",
      "right_hip_roll_link": "right_hip_roll_link",
      "right_hip_yaw_link": "right_hip_yaw_link",
      "right_hip_yaw_gear_drive": "right_hip_yaw_gear_drive",
      "right_knee_link": "right_knee_link",
      "right_ankle_pitch_link": "right_ankle_pitch_link",
      "right_ankle_roll_link": "right_ankle_roll_link",
      "left_shoulder_pitch_link": "left_shoulder_pitch_link",
      "left_shoulder_roll_link": "left_shoulder_roll_link",
      "left_shoulder_gear_drive": "left_shoulder_gear_drive",
      "left_shoulder_yaw_link": "left_shoulder_yaw_link",
      "left_elbow_roll_link": "left_elbow_roll_link",
      "left_elbow_gear_drive": "left_elbow_gear_drive",
      "left_elbow_yaw_link": "left_elbow_yaw_link",
      "left_wrist_pitch_link": "left_wrist_pitch_link",
      "left_wrist_gear_drive": "left_wrist_gear_drive",
      "left_hand": "left_hand",
      "right_shoulder_pitch_link": "right_shoulder_pitch_link",
      "right_shoulder_roll_link": "right_shoulder_roll_link",
      "right_shoulder_gear_drive": "right_shoulder_gear_drive",
      "right_shoulder_yaw_link": "right_shoulder_yaw_link",
      "right_elbow_roll_link": "right_elbow_roll_link",
      "right_elbow_gear_drive": "right_elbow_gear_drive",
      "right_elbow_yaw_link": "right_elbow_yaw_link",
      "right_wrist_pitch_link": "right_wrist_pitch_link",
      "right_wrist_gear_drive": "right_wrist_gear_drive",
      "right_hand": "right_hand"
    },
    "joints": {
      "neck_yaw_drive": "neck_yaw_drive",
      "neck_yaw_driven": "neck_yaw_driven",
      "neck_pitch": "neck_pitch",
      "neck_pitch_act": "neck_pitch_act",
      "neck_pitch_front": "neck_pitch_front",
      "neck_pitch_back": "neck_pitch_back",
      "waist_yaw": "waist_yaw",
      "waist_roll": "waist_roll",
      "waist_act_1": "waist_act_1",
      "waist_act_2": "waist_act_2",
      "left_hip_pitch": "left_hip_pitch",
      "left_hip_roll": "left_hip_roll",
      "left_hip_yaw_driven": "left_hip_yaw_driven",
      "left_hip_yaw_drive": "left_hip_yaw_drive",
      "left_knee": "left_knee",
      "left_ankle_pitch": "left_ankle_pitch",
      "left_ankle_roll": "left_ankle_roll",
      "right_hip_pitch": "right_hip_pitch",
      "right_hip_roll": "right_hip_roll",
      "right_hip_yaw_driven": "right_hip_yaw_driven",
      "right_hip_yaw_drive": "right_hip_yaw_drive",
      "right_knee": "right_knee",
      "right_ankle_pitch": "right_ankle_pitch",
      "right_ankle_roll": "right_ankle_roll",
      "left_shoulder_pitch": "left_shoulder_pitch",
      "left_shoulder_roll": "left_shoulder_roll",
      "left_shoulder_yaw_drive": "left_shoulder_yaw_drive",
      "left_shoulder_yaw_driven": "left_shoulder_yaw_driven",
      "left_elbow_roll": "left_elbow_roll",
      "left_elbow_yaw_drive": "left_elbow_yaw_drive",
      "left_elbow_yaw_driven": "left_elbow_yaw_driven",
      "left_wrist_pitch_driven": "left_wrist_pitch_driven",
      "left_wrist_pitch_drive": "left_wrist_pitch_drive",
      "left_wrist_roll": "left_wrist_roll",
      "right_shoulder_pitch": "right_shoulder_pitch",
      "right_shoulder_roll": "right_shoulder_roll",
      "right_shoulder_yaw_drive": "right_shoulder_yaw_drive",
      "right_shoulder_yaw_driven": "right_shoulder_yaw_driven",
      "right_elbow_roll": "right_elbow_roll",
      "right_elbow_yaw_drive": "right_elbow_yaw_drive",
      "right_elbow_yaw_driven": "right_elbow_yaw_driven",
      "right_wrist_pitch_driven": "right_wrist_pitch_driven",
      "right_wrist_pitch_drive": "right_wrist_pitch_drive",
      "right_wrist_roll": "right_wrist_roll"
    },
    "body_methods": {
      "torso": "name",
      "neck_yaw_gear_drive": "name",
      "neck_yaw_link": "name",
      "head": "name",
      "neck_pitch_plate": "name",
      "neck_rod": "name",
      "neck_rod_2": "name",
      "waist_gears": "name",
      "pelvis_link": "name",
      "waist_gear_drive": "name",
      "waist_gear_drive_2": "name",
      "left_hip_pitch_link": "name",
      "left_hip_roll_link": "name",
      "left_hip_yaw_link": "name",
      "left_hip_yaw_gear_drive": "name",
      "left_knee_link": "name",
      "left_ankle_pitch_link": "name",
      "left_ankle_roll_link": "name",
      "right_hip_pitch_link": "name",
      "right_hip_roll_link": "name",
      "right_hip_yaw_link": "name",
      "right_hip_yaw_gear_drive": "name",
      "right_knee_link": "name",
      "right_ankle_pitch_link": "name",
      "right_ankle_roll_link": "name",
      "left_shoulder_pitch_link": "name",
      "left_shoulder_roll_link": "name",
      "left_shoulder_gear_drive": "name",
      "left_shoulder_yaw_link": "name",
      "left_elbow_roll_link": "name",
      "left_elbow_gear_drive": "name",
      "left_elbow_yaw_link": "name",
      "left_wrist_pitch_link": "name",
      "left_wrist_gear_drive": "name",
      "left_hand": "name",
      "right_shoulder_pitch_link": "name",
      "right_shoulder_roll_link": "name",
      "right_shoulder_gear_drive": "name",
      "right_shoulder_yaw_link": "name",
      "right_elbow_roll_link": "name",
      "right_elbow_gear_drive": "name",
      "right_elbow_yaw_link": "name",
      "right_wrist_pitch_link": "name",
      "right_wrist_gear_drive": "name",
      "right_hand": "name"
    },
    "joint_methods": {
      "neck_yaw_drive": "name",
      "neck_yaw_driven": "name",
      "neck_pitch": "name",
      "neck_pitch_act": "name",
      "neck_pitch_front": "name",
      "neck_pitch_back": "name",
      "waist_yaw": "name",
      "waist_roll": "name",
      "waist_act_1": "name",
      "waist_act_2": "name",
      "left_hip_pitch": "name",
      "left_hip_roll": "name",
      "left_hip_yaw_driven": "name",
      "left_hip_yaw_drive": "name",
      "left_knee": "name",
      "left_ankle_pitch": "name",
      "left_ankle_roll": "name",
      "right_hip_pitch": "name",
      "right_hip_roll": "name",
      "right_hip_yaw_driven": "name",
      "right_hip_yaw_drive": "name",
      "right_knee": "name",
      "right_ankle_pitch": "name",
      "right_ankle_roll": "name",
      "left_shoulder_pitch": "name",
      "left_shoulder_roll": "name",
      "left_shoulder_yaw_drive": "name",
      "left_shoulder_yaw_driven": "name",
      "left_elbow_roll": "name",
      "left_elbow_yaw_drive": "name",
      "left_elbow_yaw_driven": "name",
      "left_wrist_pitch_driven": "name",
      "left_wrist_pitch_drive": "name",
      "left_wrist_roll": "name",
      "right_shoulder_pitch": "name",
      "right_shoulder_roll": "name",
      "right_shoulder_yaw_drive": "name",
      "right_shoulder_yaw_driven": "name",
      "right_elbow_roll": "name",
      "right_elbow_yaw_drive": "name",
      "right_elbow_yaw_driven": "name",
      "right_wrist_pitch_driven": "name",
      "right_wrist_pitch_drive": "name",
      "right_wrist_roll": "name"
    },
    "unmatched_m_bodies": [],
    "unmatched_upstream_bodies": [],
    "unmatched_m_joints": [],
    "unmatched_upstream_joints": [],
    "registration_anchor": {
      "M": "torso",
      "S": "torso"
    }
  },
  "unavailable": [
    {
      "entity": "neck_yaw_drive",
      "other_entity": "neck_yaw_drive",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": 10.0,
      "s": 10.0,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "neck_yaw_drive",
      "other_entity": "neck_yaw_drive",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": 10.0,
      "s": 10.0,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "neck_yaw_drive",
      "other_entity": "neck_yaw_drive",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "neck_yaw_driven",
      "other_entity": "neck_yaw_driven",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "neck_yaw_driven",
      "other_entity": "neck_yaw_driven",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "neck_yaw_driven",
      "other_entity": "neck_yaw_driven",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "neck_pitch",
      "other_entity": "neck_pitch",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "neck_pitch",
      "other_entity": "neck_pitch",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "neck_pitch",
      "other_entity": "neck_pitch",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "neck_pitch_act",
      "other_entity": "neck_pitch_act",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": 10.0,
      "s": 10.0,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "neck_pitch_act",
      "other_entity": "neck_pitch_act",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": 10.0,
      "s": 10.0,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "neck_pitch_act",
      "other_entity": "neck_pitch_act",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "neck_pitch_front",
      "other_entity": "neck_pitch_front",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "neck_pitch_front",
      "other_entity": "neck_pitch_front",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "neck_pitch_front",
      "other_entity": "neck_pitch_front",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "neck_pitch_back",
      "other_entity": "neck_pitch_back",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "neck_pitch_back",
      "other_entity": "neck_pitch_back",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "neck_pitch_back",
      "other_entity": "neck_pitch_back",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "waist_yaw",
      "other_entity": "waist_yaw",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "waist_yaw",
      "other_entity": "waist_yaw",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "waist_yaw",
      "other_entity": "waist_yaw",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "waist_roll",
      "other_entity": "waist_roll",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "waist_roll",
      "other_entity": "waist_roll",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "waist_roll",
      "other_entity": "waist_roll",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "waist_act_1",
      "other_entity": "waist_act_1",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": 10.0,
      "s": 10.0,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "waist_act_1",
      "other_entity": "waist_act_1",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": 10.0,
      "s": 10.0,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "waist_act_1",
      "other_entity": "waist_act_1",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "waist_act_2",
      "other_entity": "waist_act_2",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": 10.0,
      "s": 10.0,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "waist_act_2",
      "other_entity": "waist_act_2",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": 10.0,
      "s": 10.0,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "waist_act_2",
      "other_entity": "waist_act_2",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_hip_pitch",
      "other_entity": "left_hip_pitch",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": 10.0,
      "s": 10.0,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_hip_pitch",
      "other_entity": "left_hip_pitch",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": 10.0,
      "s": 10.0,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_hip_pitch",
      "other_entity": "left_hip_pitch",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_hip_roll",
      "other_entity": "left_hip_roll",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": 10.0,
      "s": 10.0,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_hip_roll",
      "other_entity": "left_hip_roll",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": 10.0,
      "s": 10.0,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_hip_roll",
      "other_entity": "left_hip_roll",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_hip_yaw_driven",
      "other_entity": "left_hip_yaw_driven",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_hip_yaw_driven",
      "other_entity": "left_hip_yaw_driven",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_hip_yaw_driven",
      "other_entity": "left_hip_yaw_driven",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_hip_yaw_drive",
      "other_entity": "left_hip_yaw_drive",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": 10.0,
      "s": 10.0,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_hip_yaw_drive",
      "other_entity": "left_hip_yaw_drive",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": 10.0,
      "s": 10.0,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_hip_yaw_drive",
      "other_entity": "left_hip_yaw_drive",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_knee",
      "other_entity": "left_knee",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": 10.0,
      "s": 10.0,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_knee",
      "other_entity": "left_knee",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": 10.0,
      "s": 10.0,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_knee",
      "other_entity": "left_knee",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_ankle_pitch",
      "other_entity": "left_ankle_pitch",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": 10.0,
      "s": 10.0,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_ankle_pitch",
      "other_entity": "left_ankle_pitch",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": 10.0,
      "s": 10.0,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_ankle_pitch",
      "other_entity": "left_ankle_pitch",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_ankle_roll",
      "other_entity": "left_ankle_roll",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": 10.0,
      "s": 10.0,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_ankle_roll",
      "other_entity": "left_ankle_roll",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": 10.0,
      "s": 10.0,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_ankle_roll",
      "other_entity": "left_ankle_roll",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "right_hip_pitch",
      "other_entity": "right_hip_pitch",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": 10.0,
      "s": 10.0,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "right_hip_pitch",
      "other_entity": "right_hip_pitch",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": 10.0,
      "s": 10.0,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "right_hip_pitch",
      "other_entity": "right_hip_pitch",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "right_hip_roll",
      "other_entity": "right_hip_roll",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": 10.0,
      "s": 10.0,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "right_hip_roll",
      "other_entity": "right_hip_roll",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": 10.0,
      "s": 10.0,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "right_hip_roll",
      "other_entity": "right_hip_roll",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "right_hip_yaw_driven",
      "other_entity": "right_hip_yaw_driven",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "right_hip_yaw_driven",
      "other_entity": "right_hip_yaw_driven",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "right_hip_yaw_driven",
      "other_entity": "right_hip_yaw_driven",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "right_hip_yaw_drive",
      "other_entity": "right_hip_yaw_drive",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": 10.0,
      "s": 10.0,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "right_hip_yaw_drive",
      "other_entity": "right_hip_yaw_drive",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": 10.0,
      "s": 10.0,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "right_hip_yaw_drive",
      "other_entity": "right_hip_yaw_drive",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "right_knee",
      "other_entity": "right_knee",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": 10.0,
      "s": 10.0,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "right_knee",
      "other_entity": "right_knee",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": 10.0,
      "s": 10.0,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "right_knee",
      "other_entity": "right_knee",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "right_ankle_pitch",
      "other_entity": "right_ankle_pitch",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": 10.0,
      "s": 10.0,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "right_ankle_pitch",
      "other_entity": "right_ankle_pitch",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": 10.0,
      "s": 10.0,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "right_ankle_pitch",
      "other_entity": "right_ankle_pitch",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "right_ankle_roll",
      "other_entity": "right_ankle_roll",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": 10.0,
      "s": 10.0,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "right_ankle_roll",
      "other_entity": "right_ankle_roll",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": 10.0,
      "s": 10.0,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "right_ankle_roll",
      "other_entity": "right_ankle_roll",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_shoulder_pitch",
      "other_entity": "left_shoulder_pitch",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": 10.0,
      "s": 10.0,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_shoulder_pitch",
      "other_entity": "left_shoulder_pitch",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": 10.0,
      "s": 10.0,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_shoulder_pitch",
      "other_entity": "left_shoulder_pitch",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_shoulder_roll",
      "other_entity": "left_shoulder_roll",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": 10.0,
      "s": 10.0,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_shoulder_roll",
      "other_entity": "left_shoulder_roll",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": 10.0,
      "s": 10.0,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_shoulder_roll",
      "other_entity": "left_shoulder_roll",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_shoulder_yaw_drive",
      "other_entity": "left_shoulder_yaw_drive",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": 10.0,
      "s": 10.0,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_shoulder_yaw_drive",
      "other_entity": "left_shoulder_yaw_drive",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": 10.0,
      "s": 10.0,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_shoulder_yaw_drive",
      "other_entity": "left_shoulder_yaw_drive",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_shoulder_yaw_driven",
      "other_entity": "left_shoulder_yaw_driven",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_shoulder_yaw_driven",
      "other_entity": "left_shoulder_yaw_driven",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_shoulder_yaw_driven",
      "other_entity": "left_shoulder_yaw_driven",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_elbow_roll",
      "other_entity": "left_elbow_roll",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": 10.0,
      "s": 10.0,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_elbow_roll",
      "other_entity": "left_elbow_roll",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": 10.0,
      "s": 10.0,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_elbow_roll",
      "other_entity": "left_elbow_roll",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_elbow_yaw_drive",
      "other_entity": "left_elbow_yaw_drive",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": 10.0,
      "s": 10.0,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_elbow_yaw_drive",
      "other_entity": "left_elbow_yaw_drive",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": 10.0,
      "s": 10.0,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_elbow_yaw_drive",
      "other_entity": "left_elbow_yaw_drive",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_elbow_yaw_driven",
      "other_entity": "left_elbow_yaw_driven",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_elbow_yaw_driven",
      "other_entity": "left_elbow_yaw_driven",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_elbow_yaw_driven",
      "other_entity": "left_elbow_yaw_driven",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_wrist_pitch_driven",
      "other_entity": "left_wrist_pitch_driven",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_wrist_pitch_driven",
      "other_entity": "left_wrist_pitch_driven",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_wrist_pitch_driven",
      "other_entity": "left_wrist_pitch_driven",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_wrist_pitch_drive",
      "other_entity": "left_wrist_pitch_drive",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": 10.0,
      "s": 10.0,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_wrist_pitch_drive",
      "other_entity": "left_wrist_pitch_drive",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": 10.0,
      "s": 10.0,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_wrist_pitch_drive",
      "other_entity": "left_wrist_pitch_drive",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_wrist_roll",
      "other_entity": "left_wrist_roll",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": 10.0,
      "s": 10.0,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_wrist_roll",
      "other_entity": "left_wrist_roll",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": 10.0,
      "s": 10.0,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_wrist_roll",
      "other_entity": "left_wrist_roll",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "right_shoulder_pitch",
      "other_entity": "right_shoulder_pitch",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": 10.0,
      "s": 10.0,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "right_shoulder_pitch",
      "other_entity": "right_shoulder_pitch",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": 10.0,
      "s": 10.0,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "right_shoulder_pitch",
      "other_entity": "right_shoulder_pitch",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "right_shoulder_roll",
      "other_entity": "right_shoulder_roll",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": 10.0,
      "s": 10.0,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "right_shoulder_roll",
      "other_entity": "right_shoulder_roll",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": 10.0,
      "s": 10.0,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "right_shoulder_roll",
      "other_entity": "right_shoulder_roll",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "right_shoulder_yaw_drive",
      "other_entity": "right_shoulder_yaw_drive",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": 10.0,
      "s": 10.0,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "right_shoulder_yaw_drive",
      "other_entity": "right_shoulder_yaw_drive",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": 10.0,
      "s": 10.0,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "right_shoulder_yaw_drive",
      "other_entity": "right_shoulder_yaw_drive",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "right_shoulder_yaw_driven",
      "other_entity": "right_shoulder_yaw_driven",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "right_shoulder_yaw_driven",
      "other_entity": "right_shoulder_yaw_driven",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "right_shoulder_yaw_driven",
      "other_entity": "right_shoulder_yaw_driven",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "right_elbow_roll",
      "other_entity": "right_elbow_roll",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": 10.0,
      "s": 10.0,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "right_elbow_roll",
      "other_entity": "right_elbow_roll",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": 10.0,
      "s": 10.0,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "right_elbow_roll",
      "other_entity": "right_elbow_roll",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "right_elbow_yaw_drive",
      "other_entity": "right_elbow_yaw_drive",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": 10.0,
      "s": 10.0,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "right_elbow_yaw_drive",
      "other_entity": "right_elbow_yaw_drive",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": 10.0,
      "s": 10.0,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "right_elbow_yaw_drive",
      "other_entity": "right_elbow_yaw_drive",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "right_elbow_yaw_driven",
      "other_entity": "right_elbow_yaw_driven",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "right_elbow_yaw_driven",
      "other_entity": "right_elbow_yaw_driven",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "right_elbow_yaw_driven",
      "other_entity": "right_elbow_yaw_driven",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "right_wrist_pitch_driven",
      "other_entity": "right_wrist_pitch_driven",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "right_wrist_pitch_driven",
      "other_entity": "right_wrist_pitch_driven",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "right_wrist_pitch_driven",
      "other_entity": "right_wrist_pitch_driven",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "right_wrist_pitch_drive",
      "other_entity": "right_wrist_pitch_drive",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": 10.0,
      "s": 10.0,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "right_wrist_pitch_drive",
      "other_entity": "right_wrist_pitch_drive",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": 10.0,
      "s": 10.0,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "right_wrist_pitch_drive",
      "other_entity": "right_wrist_pitch_drive",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "right_wrist_roll",
      "other_entity": "right_wrist_roll",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": 10.0,
      "s": 10.0,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "right_wrist_roll",
      "other_entity": "right_wrist_roll",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": 10.0,
      "s": 10.0,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "right_wrist_roll",
      "other_entity": "right_wrist_roll",
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
| neck_yaw_drive / effort | unavailable | 10 | 10 |
| neck_yaw_drive / force | unavailable | 10 | 10 |
| neck_yaw_drive / velocity | unavailable | unavailable | unavailable |
| neck_yaw_driven / effort | unavailable | unavailable | unavailable |
| neck_yaw_driven / force | unavailable | unavailable | unavailable |
| neck_yaw_driven / velocity | unavailable | unavailable | unavailable |
| neck_pitch / effort | unavailable | unavailable | unavailable |
| neck_pitch / force | unavailable | unavailable | unavailable |
| neck_pitch / velocity | unavailable | unavailable | unavailable |
| neck_pitch_act / effort | unavailable | 10 | 10 |
| neck_pitch_act / force | unavailable | 10 | 10 |
| neck_pitch_act / velocity | unavailable | unavailable | unavailable |
| neck_pitch_front / effort | unavailable | unavailable | unavailable |
| neck_pitch_front / force | unavailable | unavailable | unavailable |
| neck_pitch_front / velocity | unavailable | unavailable | unavailable |
| neck_pitch_back / effort | unavailable | unavailable | unavailable |
| neck_pitch_back / force | unavailable | unavailable | unavailable |
| neck_pitch_back / velocity | unavailable | unavailable | unavailable |
| waist_yaw / effort | unavailable | unavailable | unavailable |
| waist_yaw / force | unavailable | unavailable | unavailable |
| waist_yaw / velocity | unavailable | unavailable | unavailable |
| waist_roll / effort | unavailable | unavailable | unavailable |
| waist_roll / force | unavailable | unavailable | unavailable |
| waist_roll / velocity | unavailable | unavailable | unavailable |
| waist_act_1 / effort | unavailable | 10 | 10 |
| waist_act_1 / force | unavailable | 10 | 10 |
| waist_act_1 / velocity | unavailable | unavailable | unavailable |
| waist_act_2 / effort | unavailable | 10 | 10 |
| waist_act_2 / force | unavailable | 10 | 10 |
| waist_act_2 / velocity | unavailable | unavailable | unavailable |
| left_hip_pitch / effort | unavailable | 10 | 10 |
| left_hip_pitch / force | unavailable | 10 | 10 |
| left_hip_pitch / velocity | unavailable | unavailable | unavailable |
| left_hip_roll / effort | unavailable | 10 | 10 |
| left_hip_roll / force | unavailable | 10 | 10 |
| left_hip_roll / velocity | unavailable | unavailable | unavailable |
| left_hip_yaw_driven / effort | unavailable | unavailable | unavailable |
| left_hip_yaw_driven / force | unavailable | unavailable | unavailable |
| left_hip_yaw_driven / velocity | unavailable | unavailable | unavailable |
| left_hip_yaw_drive / effort | unavailable | 10 | 10 |
| left_hip_yaw_drive / force | unavailable | 10 | 10 |
| left_hip_yaw_drive / velocity | unavailable | unavailable | unavailable |
| left_knee / effort | unavailable | 10 | 10 |
| left_knee / force | unavailable | 10 | 10 |
| left_knee / velocity | unavailable | unavailable | unavailable |
| left_ankle_pitch / effort | unavailable | 10 | 10 |
| left_ankle_pitch / force | unavailable | 10 | 10 |
| left_ankle_pitch / velocity | unavailable | unavailable | unavailable |
| left_ankle_roll / effort | unavailable | 10 | 10 |
| left_ankle_roll / force | unavailable | 10 | 10 |
| left_ankle_roll / velocity | unavailable | unavailable | unavailable |
| right_hip_pitch / effort | unavailable | 10 | 10 |
| right_hip_pitch / force | unavailable | 10 | 10 |
| right_hip_pitch / velocity | unavailable | unavailable | unavailable |
| right_hip_roll / effort | unavailable | 10 | 10 |
| right_hip_roll / force | unavailable | 10 | 10 |
| right_hip_roll / velocity | unavailable | unavailable | unavailable |
| right_hip_yaw_driven / effort | unavailable | unavailable | unavailable |
| right_hip_yaw_driven / force | unavailable | unavailable | unavailable |
| right_hip_yaw_driven / velocity | unavailable | unavailable | unavailable |
| right_hip_yaw_drive / effort | unavailable | 10 | 10 |
| right_hip_yaw_drive / force | unavailable | 10 | 10 |
| right_hip_yaw_drive / velocity | unavailable | unavailable | unavailable |
| right_knee / effort | unavailable | 10 | 10 |
| right_knee / force | unavailable | 10 | 10 |
| right_knee / velocity | unavailable | unavailable | unavailable |
| right_ankle_pitch / effort | unavailable | 10 | 10 |
| right_ankle_pitch / force | unavailable | 10 | 10 |
| right_ankle_pitch / velocity | unavailable | unavailable | unavailable |
| right_ankle_roll / effort | unavailable | 10 | 10 |
| right_ankle_roll / force | unavailable | 10 | 10 |
| right_ankle_roll / velocity | unavailable | unavailable | unavailable |
| left_shoulder_pitch / effort | unavailable | 10 | 10 |
| left_shoulder_pitch / force | unavailable | 10 | 10 |
| left_shoulder_pitch / velocity | unavailable | unavailable | unavailable |
| left_shoulder_roll / effort | unavailable | 10 | 10 |
| left_shoulder_roll / force | unavailable | 10 | 10 |
| left_shoulder_roll / velocity | unavailable | unavailable | unavailable |
| left_shoulder_yaw_drive / effort | unavailable | 10 | 10 |
| left_shoulder_yaw_drive / force | unavailable | 10 | 10 |
| left_shoulder_yaw_drive / velocity | unavailable | unavailable | unavailable |
| left_shoulder_yaw_driven / effort | unavailable | unavailable | unavailable |
| left_shoulder_yaw_driven / force | unavailable | unavailable | unavailable |
| left_shoulder_yaw_driven / velocity | unavailable | unavailable | unavailable |
| left_elbow_roll / effort | unavailable | 10 | 10 |
| left_elbow_roll / force | unavailable | 10 | 10 |
| left_elbow_roll / velocity | unavailable | unavailable | unavailable |
| left_elbow_yaw_drive / effort | unavailable | 10 | 10 |
| left_elbow_yaw_drive / force | unavailable | 10 | 10 |
| left_elbow_yaw_drive / velocity | unavailable | unavailable | unavailable |
| left_elbow_yaw_driven / effort | unavailable | unavailable | unavailable |
| left_elbow_yaw_driven / force | unavailable | unavailable | unavailable |
| left_elbow_yaw_driven / velocity | unavailable | unavailable | unavailable |
| left_wrist_pitch_driven / effort | unavailable | unavailable | unavailable |
| left_wrist_pitch_driven / force | unavailable | unavailable | unavailable |
| left_wrist_pitch_driven / velocity | unavailable | unavailable | unavailable |
| left_wrist_pitch_drive / effort | unavailable | 10 | 10 |
| left_wrist_pitch_drive / force | unavailable | 10 | 10 |
| left_wrist_pitch_drive / velocity | unavailable | unavailable | unavailable |
| left_wrist_roll / effort | unavailable | 10 | 10 |
| left_wrist_roll / force | unavailable | 10 | 10 |
| left_wrist_roll / velocity | unavailable | unavailable | unavailable |
| right_shoulder_pitch / effort | unavailable | 10 | 10 |
| right_shoulder_pitch / force | unavailable | 10 | 10 |
| right_shoulder_pitch / velocity | unavailable | unavailable | unavailable |
| right_shoulder_roll / effort | unavailable | 10 | 10 |
| right_shoulder_roll / force | unavailable | 10 | 10 |
| right_shoulder_roll / velocity | unavailable | unavailable | unavailable |
| right_shoulder_yaw_drive / effort | unavailable | 10 | 10 |
| right_shoulder_yaw_drive / force | unavailable | 10 | 10 |
| right_shoulder_yaw_drive / velocity | unavailable | unavailable | unavailable |
| right_shoulder_yaw_driven / effort | unavailable | unavailable | unavailable |
| right_shoulder_yaw_driven / force | unavailable | unavailable | unavailable |
| right_shoulder_yaw_driven / velocity | unavailable | unavailable | unavailable |
| right_elbow_roll / effort | unavailable | 10 | 10 |
| right_elbow_roll / force | unavailable | 10 | 10 |
| right_elbow_roll / velocity | unavailable | unavailable | unavailable |
| right_elbow_yaw_drive / effort | unavailable | 10 | 10 |
| right_elbow_yaw_drive / force | unavailable | 10 | 10 |
| right_elbow_yaw_drive / velocity | unavailable | unavailable | unavailable |
| right_elbow_yaw_driven / effort | unavailable | unavailable | unavailable |
| right_elbow_yaw_driven / force | unavailable | unavailable | unavailable |
| right_elbow_yaw_driven / velocity | unavailable | unavailable | unavailable |
| right_wrist_pitch_driven / effort | unavailable | unavailable | unavailable |
| right_wrist_pitch_driven / force | unavailable | unavailable | unavailable |
| right_wrist_pitch_driven / velocity | unavailable | unavailable | unavailable |
| right_wrist_pitch_drive / effort | unavailable | 10 | 10 |
| right_wrist_pitch_drive / force | unavailable | 10 | 10 |
| right_wrist_pitch_drive / velocity | unavailable | unavailable | unavailable |
| right_wrist_roll / effort | unavailable | 10 | 10 |
| right_wrist_roll / force | unavailable | 10 | 10 |
| right_wrist_roll / velocity | unavailable | unavailable | unavailable |
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
    "file": "toddlerbot_2xc/toddlerbot_2xc.xml",
    "status": "passed",
    "findings": 0
  },
  {
    "file": "toddlerbot_2xc/toddlerbot_2xc_mjx.xml",
    "status": "passed",
    "findings": 0
  },
  {
    "file": "toddlerbot_2xc/toddlerbot_2xc_pos.xml",
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
    "source_dependencies": [
      "toddlerbot_2xc/toddlerbot_2xc.xml"
    ],
    "registration": {
      "translation": [
        0.0,
        0.0,
        0.315053
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
      "toddlerbot/descriptions/toddlerbot_2xc/toddlerbot_2xc.xml"
    ],
    "registration": {
      "translation": [
        0.0,
        0.0,
        0.315053
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
  "S": {
    "geometry_stripped": true,
    "missing_explicit_inertials": [],
    "assets_loaded": 0,
    "mesh_conversions": [],
    "xacro_arguments": {},
    "source_dependencies": [
      "toddlerbot/descriptions/toddlerbot_2xc/toddlerbot_2xc.xml"
    ],
    "registration": {
      "translation": [
        0.0,
        0.0,
        0.315053
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
  "self_variants_recompiled": 3,
  "historical_snapshots_reused": 4,
  "primary_physics_unchanged": true,
  "source_matching": "original raw-value provenance criteria retained; kinematic guard applies to reported CoM"
}
```
