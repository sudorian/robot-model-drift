# toddlerbot_2xm

Status: **complete**. Provenance: **dated match**, confidence **medium**.

Source selected using the ordered amended provenance rules.

M: `https://github.com/google-deepmind/mujoco_menagerie`, `toddlerbot_2xm/toddlerbot_2xm.xml`, commit `370c43965323c0944b433b202aac5058b5f907a9`.
H: `https://github.com/hshi74/toddlerbot`, `toddlerbot/descriptions/toddlerbot_2xm/toddlerbot_2xm.xml`, commit `e337f3b177b4b53abff70b31d1695a7b66cc6d2e`.
S: `957aadb8e6db85e02fbb9ef90bbcdb4b4c0c9f6c` (2025-08-29T22:11:17-04:00). Menagerie release/change: 2025-08-29T22:32:48-04:00.

Limit semantics: MJCF effort values are supported actuator torque/force envelopes. URDF effort and velocity values are manufacturer declarations retained from XML; MuJoCo does not enforce those tags. Such declaration comparisons are explicitly distinct from compiled inertial/range quantities.


## Source evidence

```json
[
  {
    "url": "https://github.com/hshi74/toddlerbot",
    "document": "toddlerbot_2xm/README.md",
    "commit": "370c43965323c0944b433b202aac5058b5f907a9",
    "current": true
  }
]
```


## Kinematics consistency

A proper Kabsch rigid transform aligns all matched zero-pose body origins. The maximum per-origin residual and signed hinge/slide axis angles determine whether CoM can be compared; RMS is also recorded. Fewer than three non-collinear origins give insufficient kinematic coverage. CoM records that fail either required M/H or M/S check are excluded from counts and largest discrepancies. Masses, principal moments and raw joint ranges remain unchanged; a flagged range still requires convention review.

| Pair | Status | Origins / rank | RMS / maximum mm | Disagreeing / checked axes |
|---|---|---:|---:|---:|
| M/H | consistent | 45 / 3 | 8.7538245e-14 / 1.80944215e-13 | 0 / 44 |
| M/S | consistent | 45 / 3 | 8.7538245e-14 / 1.80944215e-13 | 0 / 44 |

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
        -9.457031266610581e-17,
        -1.0938466838299862e-16
      ],
      [
        6.900642257266083e-17,
        0.9999999999999994,
        1.9192241390143285e-16
      ],
      [
        1.1102230246251565e-16,
        9.497611030973019e-17,
        0.9999999999999994
      ]
    ],
    "translation_other_to_m": [
      0.0,
      5.89534931288993e-18,
      -1.0408340855860843e-17
    ],
    "rms_residual_m": 8.753824500748191e-17,
    "max_residual_m": 1.8094421531119201e-16,
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
          1.0938466838299868e-16,
          -1.9192241390143295e-16,
          -1.0
        ],
        "angle_rad": 2.2090545180011184e-16,
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
          -1.0938466838299868e-16,
          1.9192241390143295e-16,
          1.0
        ],
        "angle_rad": 2.2090545180011184e-16,
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
          -9.457031266610586e-17,
          1.0,
          9.497611030973024e-17
        ],
        "angle_rad": 1.3402986819112772e-16,
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
          9.457031266610586e-17,
          -1.0,
          -9.497611030973024e-17
        ],
        "angle_rad": 1.3402986819112772e-16,
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
          9.457031266610586e-17,
          -1.0,
          -9.497611030973024e-17
        ],
        "angle_rad": 1.3402986819112772e-16,
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
          9.457031266610586e-17,
          -1.0,
          -9.497611030973024e-17
        ],
        "angle_rad": 1.3402986819112772e-16,
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
          -1.0938466838299868e-16,
          1.9192241390143295e-16,
          1.0
        ],
        "angle_rad": 2.2090545180011184e-16,
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
          6.900642257266082e-17,
          1.1102230246251563e-16
        ],
        "angle_rad": 1.3072045746689742e-16,
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
          -1.0938466838299868e-16,
          1.9192241390143295e-16,
          1.0
        ],
        "angle_rad": 2.2090545180011184e-16,
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
          -1.0938466838299868e-16,
          1.9192241390143295e-16,
          1.0
        ],
        "angle_rad": 2.2090545180011184e-16,
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
          -9.457031266610586e-17,
          1.0,
          9.497611030973024e-17
        ],
        "angle_rad": 1.3402986819112772e-16,
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
          6.900642257266082e-17,
          1.1102230246251563e-16
        ],
        "angle_rad": 1.3072045746689742e-16,
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
          1.0938466838299868e-16,
          -1.9192241390143295e-16,
          -1.0
        ],
        "angle_rad": 2.2090545180011184e-16,
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
          -1.0938466838299868e-16,
          1.9192241390143295e-16,
          1.0
        ],
        "angle_rad": 2.2090545180011184e-16,
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
          9.457031266610586e-17,
          -1.0,
          -9.497611030973024e-17
        ],
        "angle_rad": 1.3402986819112772e-16,
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
          -9.457031266610586e-17,
          1.0,
          9.497611030973024e-17
        ],
        "angle_rad": 1.3402986819112772e-16,
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
          6.900642257266082e-17,
          1.1102230246251563e-16
        ],
        "angle_rad": 1.3072045746689742e-16,
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
          9.457031266610586e-17,
          -1.0,
          -9.497611030973024e-17
        ],
        "angle_rad": 1.3402986819112772e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "right_hip_roll",
        "joint_other": "right_hip_roll",
        "axis_m": [
          1.0,
          0.0,
          0.0
        ],
        "axis_other_aligned": [
          1.0,
          6.900642257266082e-17,
          1.1102230246251563e-16
        ],
        "angle_rad": 1.3072045746689742e-16,
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
          1.0938466838299868e-16,
          -1.9192241390143295e-16,
          -1.0
        ],
        "angle_rad": 2.2090545180011184e-16,
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
          -1.0938466838299868e-16,
          1.9192241390143295e-16,
          1.0
        ],
        "angle_rad": 2.2090545180011184e-16,
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
          -9.457031266610586e-17,
          1.0,
          9.497611030973024e-17
        ],
        "angle_rad": 1.3402986819112772e-16,
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
          9.457031266610586e-17,
          -1.0,
          -9.497611030973024e-17
        ],
        "angle_rad": 1.3402986819112772e-16,
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
          6.900642257266082e-17,
          1.1102230246251563e-16
        ],
        "angle_rad": 1.3072045746689742e-16,
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
          -9.457031266610586e-17,
          1.0,
          9.497611030973024e-17
        ],
        "angle_rad": 1.3402986819112772e-16,
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
          6.900642257266082e-17,
          1.1102230246251563e-16
        ],
        "angle_rad": 1.3072045746689742e-16,
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
          -1.0938466838299868e-16,
          1.9192241390143295e-16,
          1.0
        ],
        "angle_rad": 2.2090545180011184e-16,
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
          1.0938466838299868e-16,
          -1.9192241390143295e-16,
          -1.0
        ],
        "angle_rad": 2.2090545180011184e-16,
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
          6.900642257266082e-17,
          1.1102230246251563e-16
        ],
        "angle_rad": 1.3072045746689742e-16,
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
          -1.0938466838299868e-16,
          1.9192241390143295e-16,
          1.0
        ],
        "angle_rad": 2.2090545180011184e-16,
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
          1.0938466838299868e-16,
          -1.9192241390143295e-16,
          -1.0
        ],
        "angle_rad": 2.2090545180011184e-16,
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
          9.457031266610586e-17,
          -1.0,
          -9.497611030973024e-17
        ],
        "angle_rad": 1.3402986819112772e-16,
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
          -9.457031266610586e-17,
          1.0,
          9.497611030973024e-17
        ],
        "angle_rad": 1.3402986819112772e-16,
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
          -6.900642257266082e-17,
          -1.1102230246251563e-16
        ],
        "angle_rad": 1.3072045746689742e-16,
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
          9.457031266610586e-17,
          -1.0,
          -9.497611030973024e-17
        ],
        "angle_rad": 1.3402986819112772e-16,
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
          -6.900642257266082e-17,
          -1.1102230246251563e-16
        ],
        "angle_rad": 1.3072045746689742e-16,
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
          -1.0938466838299868e-16,
          1.9192241390143295e-16,
          1.0
        ],
        "angle_rad": 2.2090545180011184e-16,
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
          1.0938466838299868e-16,
          -1.9192241390143295e-16,
          -1.0
        ],
        "angle_rad": 2.2090545180011184e-16,
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
          -6.900642257266082e-17,
          -1.1102230246251563e-16
        ],
        "angle_rad": 1.3072045746689742e-16,
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
          -1.0938466838299868e-16,
          1.9192241390143295e-16,
          1.0
        ],
        "angle_rad": 2.2090545180011184e-16,
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
          1.0938466838299868e-16,
          -1.9192241390143295e-16,
          -1.0
        ],
        "angle_rad": 2.2090545180011184e-16,
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
          -9.457031266610586e-17,
          1.0,
          9.497611030973024e-17
        ],
        "angle_rad": 1.3402986819112772e-16,
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
          9.457031266610586e-17,
          -1.0,
          -9.497611030973024e-17
        ],
        "angle_rad": 1.3402986819112772e-16,
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
          6.900642257266082e-17,
          1.1102230246251563e-16
        ],
        "angle_rad": 1.3072045746689742e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      }
    ],
    "axis_disagreements": [],
    "com_eligible": true,
    "covariance_singular_values": [
      0.6500252923666148,
      0.2189279259598546,
      0.005802999285750275
    ],
    "origin_residuals_m": {
      "torso": 1.1961969022396513e-17,
      "neck_yaw_gear_drive": 8.931311897002864e-17,
      "neck_yaw_link": 8.944052057855243e-17,
      "head": 8.999269903400626e-17,
      "neck_pitch_plate": 1.192117636091223e-16,
      "neck_rod": 1.1979644131284958e-16,
      "neck_rod_2": 1.2091221733348078e-16,
      "waist_gears": 1.2161257223025197e-17,
      "pelvis_link": 4.706159526238268e-18,
      "waist_gear_drive": 1.4195089210720303e-17,
      "waist_gear_drive_2": 4.4847899180502346e-18,
      "left_hip_pitch_link": 3.291406376790657e-17,
      "left_hip_roll_link": 3.98609107286759e-17,
      "left_hip_yaw_link": 6.582812753581314e-17,
      "left_hip_yaw_gear_drive": 6.546139416680338e-17,
      "left_knee_link": 9.126689985681991e-17,
      "left_ankle_pitch_link": 1.7772239894833365e-16,
      "left_ankle_roll_link": 1.8094421531119201e-16,
      "right_hip_pitch_link": 1.471961680016039e-17,
      "right_hip_roll_link": 3.179800655392251e-17,
      "right_hip_yaw_link": 4.443059973708341e-17,
      "right_hip_yaw_gear_drive": 4.443059973708341e-17,
      "right_knee_link": 8.554842949272357e-17,
      "right_ankle_pitch_link": 1.7235854893846466e-16,
      "right_ankle_roll_link": 1.7109685898544713e-16,
      "left_shoulder_pitch_link": 7.757919228897728e-17,
      "left_shoulder_roll_link": 8.554842949272357e-17,
      "left_shoulder_gear_drive": 8.217537263382348e-17,
      "left_shoulder_yaw_link": 7.244417918960238e-17,
      "left_elbow_roll_link": 5.887846720064156e-17,
      "left_elbow_gear_drive": 7.076443975969106e-17,
      "left_elbow_yaw_link": 5.724587470723463e-17,
      "left_wrist_pitch_link": 8.804469334467935e-17,
      "left_wrist_gear_drive": 8.838582090426453e-17,
      "left_hand": 7.505561329662603e-17,
      "right_shoulder_pitch_link": 1.0031442548020353e-16,
      "right_shoulder_roll_link": 1.0841522980384314e-16,
      "right_shoulder_gear_drive": 1.0844450065777683e-16,
      "right_shoulder_yaw_link": 9.813077866773594e-17,
      "right_elbow_roll_link": 6.245004513516506e-17,
      "right_elbow_gear_drive": 7.315850489598577e-17,
      "right_elbow_yaw_link": 5.808086318414842e-17,
      "right_wrist_pitch_link": 5.887846720064156e-17,
      "right_wrist_gear_drive": 4.291468873614597e-17,
      "right_hand": 4.680188215576645e-17
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
        -9.457031266610581e-17,
        -1.0938466838299862e-16
      ],
      [
        6.900642257266083e-17,
        0.9999999999999994,
        1.9192241390143285e-16
      ],
      [
        1.1102230246251565e-16,
        9.497611030973019e-17,
        0.9999999999999994
      ]
    ],
    "translation_other_to_m": [
      0.0,
      5.89534931288993e-18,
      -1.0408340855860843e-17
    ],
    "rms_residual_m": 8.753824500748191e-17,
    "max_residual_m": 1.8094421531119201e-16,
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
          1.0938466838299868e-16,
          -1.9192241390143295e-16,
          -1.0
        ],
        "angle_rad": 2.2090545180011184e-16,
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
          -1.0938466838299868e-16,
          1.9192241390143295e-16,
          1.0
        ],
        "angle_rad": 2.2090545180011184e-16,
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
          -9.457031266610586e-17,
          1.0,
          9.497611030973024e-17
        ],
        "angle_rad": 1.3402986819112772e-16,
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
          9.457031266610586e-17,
          -1.0,
          -9.497611030973024e-17
        ],
        "angle_rad": 1.3402986819112772e-16,
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
          9.457031266610586e-17,
          -1.0,
          -9.497611030973024e-17
        ],
        "angle_rad": 1.3402986819112772e-16,
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
          9.457031266610586e-17,
          -1.0,
          -9.497611030973024e-17
        ],
        "angle_rad": 1.3402986819112772e-16,
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
          -1.0938466838299868e-16,
          1.9192241390143295e-16,
          1.0
        ],
        "angle_rad": 2.2090545180011184e-16,
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
          6.900642257266082e-17,
          1.1102230246251563e-16
        ],
        "angle_rad": 1.3072045746689742e-16,
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
          -1.0938466838299868e-16,
          1.9192241390143295e-16,
          1.0
        ],
        "angle_rad": 2.2090545180011184e-16,
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
          -1.0938466838299868e-16,
          1.9192241390143295e-16,
          1.0
        ],
        "angle_rad": 2.2090545180011184e-16,
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
          -9.457031266610586e-17,
          1.0,
          9.497611030973024e-17
        ],
        "angle_rad": 1.3402986819112772e-16,
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
          6.900642257266082e-17,
          1.1102230246251563e-16
        ],
        "angle_rad": 1.3072045746689742e-16,
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
          1.0938466838299868e-16,
          -1.9192241390143295e-16,
          -1.0
        ],
        "angle_rad": 2.2090545180011184e-16,
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
          -1.0938466838299868e-16,
          1.9192241390143295e-16,
          1.0
        ],
        "angle_rad": 2.2090545180011184e-16,
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
          9.457031266610586e-17,
          -1.0,
          -9.497611030973024e-17
        ],
        "angle_rad": 1.3402986819112772e-16,
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
          -9.457031266610586e-17,
          1.0,
          9.497611030973024e-17
        ],
        "angle_rad": 1.3402986819112772e-16,
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
          6.900642257266082e-17,
          1.1102230246251563e-16
        ],
        "angle_rad": 1.3072045746689742e-16,
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
          9.457031266610586e-17,
          -1.0,
          -9.497611030973024e-17
        ],
        "angle_rad": 1.3402986819112772e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "right_hip_roll",
        "joint_other": "right_hip_roll",
        "axis_m": [
          1.0,
          0.0,
          0.0
        ],
        "axis_other_aligned": [
          1.0,
          6.900642257266082e-17,
          1.1102230246251563e-16
        ],
        "angle_rad": 1.3072045746689742e-16,
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
          1.0938466838299868e-16,
          -1.9192241390143295e-16,
          -1.0
        ],
        "angle_rad": 2.2090545180011184e-16,
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
          -1.0938466838299868e-16,
          1.9192241390143295e-16,
          1.0
        ],
        "angle_rad": 2.2090545180011184e-16,
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
          -9.457031266610586e-17,
          1.0,
          9.497611030973024e-17
        ],
        "angle_rad": 1.3402986819112772e-16,
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
          9.457031266610586e-17,
          -1.0,
          -9.497611030973024e-17
        ],
        "angle_rad": 1.3402986819112772e-16,
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
          6.900642257266082e-17,
          1.1102230246251563e-16
        ],
        "angle_rad": 1.3072045746689742e-16,
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
          -9.457031266610586e-17,
          1.0,
          9.497611030973024e-17
        ],
        "angle_rad": 1.3402986819112772e-16,
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
          6.900642257266082e-17,
          1.1102230246251563e-16
        ],
        "angle_rad": 1.3072045746689742e-16,
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
          -1.0938466838299868e-16,
          1.9192241390143295e-16,
          1.0
        ],
        "angle_rad": 2.2090545180011184e-16,
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
          1.0938466838299868e-16,
          -1.9192241390143295e-16,
          -1.0
        ],
        "angle_rad": 2.2090545180011184e-16,
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
          6.900642257266082e-17,
          1.1102230246251563e-16
        ],
        "angle_rad": 1.3072045746689742e-16,
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
          -1.0938466838299868e-16,
          1.9192241390143295e-16,
          1.0
        ],
        "angle_rad": 2.2090545180011184e-16,
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
          1.0938466838299868e-16,
          -1.9192241390143295e-16,
          -1.0
        ],
        "angle_rad": 2.2090545180011184e-16,
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
          9.457031266610586e-17,
          -1.0,
          -9.497611030973024e-17
        ],
        "angle_rad": 1.3402986819112772e-16,
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
          -9.457031266610586e-17,
          1.0,
          9.497611030973024e-17
        ],
        "angle_rad": 1.3402986819112772e-16,
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
          -6.900642257266082e-17,
          -1.1102230246251563e-16
        ],
        "angle_rad": 1.3072045746689742e-16,
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
          9.457031266610586e-17,
          -1.0,
          -9.497611030973024e-17
        ],
        "angle_rad": 1.3402986819112772e-16,
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
          -6.900642257266082e-17,
          -1.1102230246251563e-16
        ],
        "angle_rad": 1.3072045746689742e-16,
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
          -1.0938466838299868e-16,
          1.9192241390143295e-16,
          1.0
        ],
        "angle_rad": 2.2090545180011184e-16,
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
          1.0938466838299868e-16,
          -1.9192241390143295e-16,
          -1.0
        ],
        "angle_rad": 2.2090545180011184e-16,
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
          -6.900642257266082e-17,
          -1.1102230246251563e-16
        ],
        "angle_rad": 1.3072045746689742e-16,
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
          -1.0938466838299868e-16,
          1.9192241390143295e-16,
          1.0
        ],
        "angle_rad": 2.2090545180011184e-16,
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
          1.0938466838299868e-16,
          -1.9192241390143295e-16,
          -1.0
        ],
        "angle_rad": 2.2090545180011184e-16,
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
          -9.457031266610586e-17,
          1.0,
          9.497611030973024e-17
        ],
        "angle_rad": 1.3402986819112772e-16,
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
          9.457031266610586e-17,
          -1.0,
          -9.497611030973024e-17
        ],
        "angle_rad": 1.3402986819112772e-16,
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
          6.900642257266082e-17,
          1.1102230246251563e-16
        ],
        "angle_rad": 1.3072045746689742e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      }
    ],
    "axis_disagreements": [],
    "com_eligible": true,
    "covariance_singular_values": [
      0.6500252923666148,
      0.2189279259598546,
      0.005802999285750275
    ],
    "origin_residuals_m": {
      "torso": 1.1961969022396513e-17,
      "neck_yaw_gear_drive": 8.931311897002864e-17,
      "neck_yaw_link": 8.944052057855243e-17,
      "head": 8.999269903400626e-17,
      "neck_pitch_plate": 1.192117636091223e-16,
      "neck_rod": 1.1979644131284958e-16,
      "neck_rod_2": 1.2091221733348078e-16,
      "waist_gears": 1.2161257223025197e-17,
      "pelvis_link": 4.706159526238268e-18,
      "waist_gear_drive": 1.4195089210720303e-17,
      "waist_gear_drive_2": 4.4847899180502346e-18,
      "left_hip_pitch_link": 3.291406376790657e-17,
      "left_hip_roll_link": 3.98609107286759e-17,
      "left_hip_yaw_link": 6.582812753581314e-17,
      "left_hip_yaw_gear_drive": 6.546139416680338e-17,
      "left_knee_link": 9.126689985681991e-17,
      "left_ankle_pitch_link": 1.7772239894833365e-16,
      "left_ankle_roll_link": 1.8094421531119201e-16,
      "right_hip_pitch_link": 1.471961680016039e-17,
      "right_hip_roll_link": 3.179800655392251e-17,
      "right_hip_yaw_link": 4.443059973708341e-17,
      "right_hip_yaw_gear_drive": 4.443059973708341e-17,
      "right_knee_link": 8.554842949272357e-17,
      "right_ankle_pitch_link": 1.7235854893846466e-16,
      "right_ankle_roll_link": 1.7109685898544713e-16,
      "left_shoulder_pitch_link": 7.757919228897728e-17,
      "left_shoulder_roll_link": 8.554842949272357e-17,
      "left_shoulder_gear_drive": 8.217537263382348e-17,
      "left_shoulder_yaw_link": 7.244417918960238e-17,
      "left_elbow_roll_link": 5.887846720064156e-17,
      "left_elbow_gear_drive": 7.076443975969106e-17,
      "left_elbow_yaw_link": 5.724587470723463e-17,
      "left_wrist_pitch_link": 8.804469334467935e-17,
      "left_wrist_gear_drive": 8.838582090426453e-17,
      "left_hand": 7.505561329662603e-17,
      "right_shoulder_pitch_link": 1.0031442548020353e-16,
      "right_shoulder_roll_link": 1.0841522980384314e-16,
      "right_shoulder_gear_drive": 1.0844450065777683e-16,
      "right_shoulder_yaw_link": 9.813077866773594e-17,
      "right_elbow_roll_link": 6.245004513516506e-17,
      "right_elbow_gear_drive": 7.315850489598577e-17,
      "right_elbow_yaw_link": 5.808086318414842e-17,
      "right_wrist_pitch_link": 5.887846720064156e-17,
      "right_wrist_gear_drive": 4.291468873614597e-17,
      "right_hand": 4.680188215576645e-17
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
| robot / total_com_registered | [-0.0222324662, -0.00111840398, -0.0276428386] | [-0.0222324662, -0.00111840398, -0.0276428386] | [-0.0222324662, -0.00111840398, -0.0276428386] | [0, 0, 0] | eligible; compared after Kabsch alignment | [aggregate inputs](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/toddlerbot_2xm/toddlerbot_2xm.xml#L1) | [aggregate inputs](https://github.com/hshi74/toddlerbot/blob/957aadb8e6db85e02fbb9ef90bbcdb4b4c0c9f6c/toddlerbot/descriptions/toddlerbot_2xm/toddlerbot_2xm.xml#L1) | [aggregate inputs](https://github.com/hshi74/toddlerbot/blob/e337f3b177b4b53abff70b31d1695a7b66cc6d2e/toddlerbot/descriptions/toddlerbot_2xm/toddlerbot_2xm.xml#L1) |
| torso / com_registered | [-0.0194013, -0.00385148, 0.0614411] | [-0.0194013, -0.00385148, 0.0614411] | [-0.0194013, -0.00385148, 0.0614411] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L40](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/toddlerbot_2xm/toddlerbot_2xm.xml#L40) | [CoM/kinematic input L37](https://github.com/hshi74/toddlerbot/blob/957aadb8e6db85e02fbb9ef90bbcdb4b4c0c9f6c/toddlerbot/descriptions/toddlerbot_2xm/toddlerbot_2xm.xml#L37) | [CoM/kinematic input L37](https://github.com/hshi74/toddlerbot/blob/e337f3b177b4b53abff70b31d1695a7b66cc6d2e/toddlerbot/descriptions/toddlerbot_2xm/toddlerbot_2xm.xml#L37) |
| neck_yaw_gear_drive / com_registered | [-0.0215079, 0, 0.1223841] | [-0.0215079, 0, 0.1223841] | [-0.0215079, 0, 0.1223841] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L50](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/toddlerbot_2xm/toddlerbot_2xm.xml#L50) | [CoM/kinematic input L48](https://github.com/hshi74/toddlerbot/blob/957aadb8e6db85e02fbb9ef90bbcdb4b4c0c9f6c/toddlerbot/descriptions/toddlerbot_2xm/toddlerbot_2xm.xml#L48) | [CoM/kinematic input L48](https://github.com/hshi74/toddlerbot/blob/e337f3b177b4b53abff70b31d1695a7b66cc6d2e/toddlerbot/descriptions/toddlerbot_2xm/toddlerbot_2xm.xml#L48) |
| neck_yaw_link / com_registered | [-0.00051128, 0, 0.13221562] | [-0.00051128, 0, 0.13221562] | [-0.00051128, 0, 0.13221562] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L57](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/toddlerbot_2xm/toddlerbot_2xm.xml#L57) | [CoM/kinematic input L55](https://github.com/hshi74/toddlerbot/blob/957aadb8e6db85e02fbb9ef90bbcdb4b4c0c9f6c/toddlerbot/descriptions/toddlerbot_2xm/toddlerbot_2xm.xml#L55) | [CoM/kinematic input L55](https://github.com/hshi74/toddlerbot/blob/e337f3b177b4b53abff70b31d1695a7b66cc6d2e/toddlerbot/descriptions/toddlerbot_2xm/toddlerbot_2xm.xml#L55) |
| head / com_registered | [-0.01099307, 0.00511009, 0.1837856] | [-0.01099307, 0.00511009, 0.1837856] | [-0.01099307, 0.00511009, 0.1837856] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L71](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/toddlerbot_2xm/toddlerbot_2xm.xml#L71) | [CoM/kinematic input L69](https://github.com/hshi74/toddlerbot/blob/957aadb8e6db85e02fbb9ef90bbcdb4b4c0c9f6c/toddlerbot/descriptions/toddlerbot_2xm/toddlerbot_2xm.xml#L69) | [CoM/kinematic input L69](https://github.com/hshi74/toddlerbot/blob/e337f3b177b4b53abff70b31d1695a7b66cc6d2e/toddlerbot/descriptions/toddlerbot_2xm/toddlerbot_2xm.xml#L69) |
| neck_pitch_plate / com_registered | [-0.02750787, -0.00132818, 0.1716157] | [-0.02750787, -0.00132818, 0.1716157] | [-0.02750787, -0.00132818, 0.1716157] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L79](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/toddlerbot_2xm/toddlerbot_2xm.xml#L79) | [CoM/kinematic input L78](https://github.com/hshi74/toddlerbot/blob/957aadb8e6db85e02fbb9ef90bbcdb4b4c0c9f6c/toddlerbot/descriptions/toddlerbot_2xm/toddlerbot_2xm.xml#L78) | [CoM/kinematic input L78](https://github.com/hshi74/toddlerbot/blob/e337f3b177b4b53abff70b31d1695a7b66cc6d2e/toddlerbot/descriptions/toddlerbot_2xm/toddlerbot_2xm.xml#L78) |
| neck_rod / com_registered | [-0.0067893, -0.00559086, 0.15726547] | [-0.0067893, -0.00559086, 0.15726547] | [-0.0067893, -0.00559086, 0.15726547] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L85](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/toddlerbot_2xm/toddlerbot_2xm.xml#L85) | [CoM/kinematic input L85](https://github.com/hshi74/toddlerbot/blob/957aadb8e6db85e02fbb9ef90bbcdb4b4c0c9f6c/toddlerbot/descriptions/toddlerbot_2xm/toddlerbot_2xm.xml#L85) | [CoM/kinematic input L85](https://github.com/hshi74/toddlerbot/blob/e337f3b177b4b53abff70b31d1695a7b66cc6d2e/toddlerbot/descriptions/toddlerbot_2xm/toddlerbot_2xm.xml#L85) |
| neck_rod_2 / com_registered | [-0.02125841, -0.00559086, 0.15334582] | [-0.02125841, -0.00559086, 0.15334582] | [-0.02125841, -0.00559086, 0.15334582] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L96](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/toddlerbot_2xm/toddlerbot_2xm.xml#L96) | [CoM/kinematic input L97](https://github.com/hshi74/toddlerbot/blob/957aadb8e6db85e02fbb9ef90bbcdb4b4c0c9f6c/toddlerbot/descriptions/toddlerbot_2xm/toddlerbot_2xm.xml#L97) | [CoM/kinematic input L97](https://github.com/hshi74/toddlerbot/blob/e337f3b177b4b53abff70b31d1695a7b66cc6d2e/toddlerbot/descriptions/toddlerbot_2xm/toddlerbot_2xm.xml#L97) |
| waist_gears / com_registered | [-0.0165079, 0, -0.01547811] | [-0.0165079, 0, -0.01547811] | [-0.0165079, 0, -0.01547811] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L110](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/toddlerbot_2xm/toddlerbot_2xm.xml#L110) | [CoM/kinematic input L111](https://github.com/hshi74/toddlerbot/blob/957aadb8e6db85e02fbb9ef90bbcdb4b4c0c9f6c/toddlerbot/descriptions/toddlerbot_2xm/toddlerbot_2xm.xml#L111) | [CoM/kinematic input L111](https://github.com/hshi74/toddlerbot/blob/e337f3b177b4b53abff70b31d1695a7b66cc6d2e/toddlerbot/descriptions/toddlerbot_2xm/toddlerbot_2xm.xml#L111) |
| pelvis_link / com_registered | [-0.0166545, 0, -0.04256711] | [-0.0166545, 0, -0.04256711] | [-0.0166545, 0, -0.04256711] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L117](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/toddlerbot_2xm/toddlerbot_2xm.xml#L117) | [CoM/kinematic input L118](https://github.com/hshi74/toddlerbot/blob/957aadb8e6db85e02fbb9ef90bbcdb4b4c0c9f6c/toddlerbot/descriptions/toddlerbot_2xm/toddlerbot_2xm.xml#L118) | [CoM/kinematic input L118](https://github.com/hshi74/toddlerbot/blob/e337f3b177b4b53abff70b31d1695a7b66cc6d2e/toddlerbot/descriptions/toddlerbot_2xm/toddlerbot_2xm.xml#L118) |
| waist_gear_drive / com_registered | [-0.00625, 0, -0.02936827] | [-0.00625, 0, -0.02936827] | [-0.00625, 0, -0.02936827] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L125](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/toddlerbot_2xm/toddlerbot_2xm.xml#L125) | [CoM/kinematic input L127](https://github.com/hshi74/toddlerbot/blob/957aadb8e6db85e02fbb9ef90bbcdb4b4c0c9f6c/toddlerbot/descriptions/toddlerbot_2xm/toddlerbot_2xm.xml#L127) | [CoM/kinematic input L127](https://github.com/hshi74/toddlerbot/blob/e337f3b177b4b53abff70b31d1695a7b66cc6d2e/toddlerbot/descriptions/toddlerbot_2xm/toddlerbot_2xm.xml#L127) |
| waist_gear_drive_2 / com_registered | [-0.02625, 0, -0.02936827] | [-0.02625, 0, -0.02936827] | [-0.02625, 0, -0.02936827] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L132](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/toddlerbot_2xm/toddlerbot_2xm.xml#L132) | [CoM/kinematic input L135](https://github.com/hshi74/toddlerbot/blob/957aadb8e6db85e02fbb9ef90bbcdb4b4c0c9f6c/toddlerbot/descriptions/toddlerbot_2xm/toddlerbot_2xm.xml#L135) | [CoM/kinematic input L135](https://github.com/hshi74/toddlerbot/blob/e337f3b177b4b53abff70b31d1695a7b66cc6d2e/toddlerbot/descriptions/toddlerbot_2xm/toddlerbot_2xm.xml#L135) |
| left_hip_pitch_link / com_registered | [-0.0365585, 0.0368253, -0.07637271] | [-0.0365585, 0.0368253, -0.07637271] | [-0.0365585, 0.0368253, -0.07637271] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L139](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/toddlerbot_2xm/toddlerbot_2xm.xml#L139) | [CoM/kinematic input L143](https://github.com/hshi74/toddlerbot/blob/957aadb8e6db85e02fbb9ef90bbcdb4b4c0c9f6c/toddlerbot/descriptions/toddlerbot_2xm/toddlerbot_2xm.xml#L143) | [CoM/kinematic input L143](https://github.com/hshi74/toddlerbot/blob/e337f3b177b4b53abff70b31d1695a7b66cc6d2e/toddlerbot/descriptions/toddlerbot_2xm/toddlerbot_2xm.xml#L143) |
| left_hip_roll_link / com_registered | [-0.0146051, 0.03699678, -0.10581831] | [-0.0146051, 0.03699678, -0.10581831] | [-0.0146051, 0.03699678, -0.10581831] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L149](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/toddlerbot_2xm/toddlerbot_2xm.xml#L149) | [CoM/kinematic input L153](https://github.com/hshi74/toddlerbot/blob/957aadb8e6db85e02fbb9ef90bbcdb4b4c0c9f6c/toddlerbot/descriptions/toddlerbot_2xm/toddlerbot_2xm.xml#L153) | [CoM/kinematic input L153](https://github.com/hshi74/toddlerbot/blob/e337f3b177b4b53abff70b31d1695a7b66cc6d2e/toddlerbot/descriptions/toddlerbot_2xm/toddlerbot_2xm.xml#L153) |
| left_hip_yaw_link / com_registered | [-0.02592359, 0.03817184, -0.15691701] | [-0.02592359, 0.03817184, -0.15691701] | [-0.02592359, 0.03817184, -0.15691701] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L155](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/toddlerbot_2xm/toddlerbot_2xm.xml#L155) | [CoM/kinematic input L160](https://github.com/hshi74/toddlerbot/blob/957aadb8e6db85e02fbb9ef90bbcdb4b4c0c9f6c/toddlerbot/descriptions/toddlerbot_2xm/toddlerbot_2xm.xml#L160) | [CoM/kinematic input L160](https://github.com/hshi74/toddlerbot/blob/e337f3b177b4b53abff70b31d1695a7b66cc6d2e/toddlerbot/descriptions/toddlerbot_2xm/toddlerbot_2xm.xml#L160) |
| left_hip_yaw_gear_drive / com_registered | [-0.03545, 0.0368, -0.11983651] | [-0.03545, 0.0368, -0.11983651] | [-0.03545, 0.0368, -0.11983651] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L164](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/toddlerbot_2xm/toddlerbot_2xm.xml#L164) | [CoM/kinematic input L170](https://github.com/hshi74/toddlerbot/blob/957aadb8e6db85e02fbb9ef90bbcdb4b4c0c9f6c/toddlerbot/descriptions/toddlerbot_2xm/toddlerbot_2xm.xml#L170) | [CoM/kinematic input L170](https://github.com/hshi74/toddlerbot/blob/e337f3b177b4b53abff70b31d1695a7b66cc6d2e/toddlerbot/descriptions/toddlerbot_2xm/toddlerbot_2xm.xml#L170) |
| left_knee_link / com_registered | [-0.01172668, 0.037, -0.21665601] | [-0.01172668, 0.037, -0.21665601] | [-0.01172668, 0.037, -0.21665601] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L171](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/toddlerbot_2xm/toddlerbot_2xm.xml#L171) | [CoM/kinematic input L178](https://github.com/hshi74/toddlerbot/blob/957aadb8e6db85e02fbb9ef90bbcdb4b4c0c9f6c/toddlerbot/descriptions/toddlerbot_2xm/toddlerbot_2xm.xml#L178) | [CoM/kinematic input L178](https://github.com/hshi74/toddlerbot/blob/e337f3b177b4b53abff70b31d1695a7b66cc6d2e/toddlerbot/descriptions/toddlerbot_2xm/toddlerbot_2xm.xml#L178) |
| left_ankle_pitch_link / com_registered | [-0.0342192, 0.0368074, -0.26399731] | [-0.0342192, 0.0368074, -0.26399731] | [-0.0342192, 0.0368074, -0.26399731] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L180](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/toddlerbot_2xm/toddlerbot_2xm.xml#L180) | [CoM/kinematic input L187](https://github.com/hshi74/toddlerbot/blob/957aadb8e6db85e02fbb9ef90bbcdb4b4c0c9f6c/toddlerbot/descriptions/toddlerbot_2xm/toddlerbot_2xm.xml#L187) | [CoM/kinematic input L187](https://github.com/hshi74/toddlerbot/blob/e337f3b177b4b53abff70b31d1695a7b66cc6d2e/toddlerbot/descriptions/toddlerbot_2xm/toddlerbot_2xm.xml#L187) |
| left_ankle_roll_link / com_registered | [-0.0034068, 0.03699993, -0.30280941] | [-0.0034068, 0.03699993, -0.30280941] | [-0.0034068, 0.03699993, -0.30280941] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L190](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/toddlerbot_2xm/toddlerbot_2xm.xml#L190) | [CoM/kinematic input L197](https://github.com/hshi74/toddlerbot/blob/957aadb8e6db85e02fbb9ef90bbcdb4b4c0c9f6c/toddlerbot/descriptions/toddlerbot_2xm/toddlerbot_2xm.xml#L197) | [CoM/kinematic input L197](https://github.com/hshi74/toddlerbot/blob/e337f3b177b4b53abff70b31d1695a7b66cc6d2e/toddlerbot/descriptions/toddlerbot_2xm/toddlerbot_2xm.xml#L197) |
| right_hip_pitch_link / com_registered | [-0.0364738, -0.0368253, -0.07637271] | [-0.0364738, -0.0368253, -0.07637271] | [-0.0364738, -0.0368253, -0.07637271] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L208](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/toddlerbot_2xm/toddlerbot_2xm.xml#L208) | [CoM/kinematic input L216](https://github.com/hshi74/toddlerbot/blob/957aadb8e6db85e02fbb9ef90bbcdb4b4c0c9f6c/toddlerbot/descriptions/toddlerbot_2xm/toddlerbot_2xm.xml#L216) | [CoM/kinematic input L215](https://github.com/hshi74/toddlerbot/blob/e337f3b177b4b53abff70b31d1695a7b66cc6d2e/toddlerbot/descriptions/toddlerbot_2xm/toddlerbot_2xm.xml#L215) |
| right_hip_roll_link / com_registered | [-0.0144426, -0.03700322, -0.10581831] | [-0.0144426, -0.03700322, -0.10581831] | [-0.0144426, -0.03700322, -0.10581831] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L218](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/toddlerbot_2xm/toddlerbot_2xm.xml#L218) | [CoM/kinematic input L226](https://github.com/hshi74/toddlerbot/blob/957aadb8e6db85e02fbb9ef90bbcdb4b4c0c9f6c/toddlerbot/descriptions/toddlerbot_2xm/toddlerbot_2xm.xml#L226) | [CoM/kinematic input L225](https://github.com/hshi74/toddlerbot/blob/e337f3b177b4b53abff70b31d1695a7b66cc6d2e/toddlerbot/descriptions/toddlerbot_2xm/toddlerbot_2xm.xml#L225) |
| right_hip_yaw_link / com_registered | [-0.02576007, -0.03817152, -0.15691681] | [-0.02576007, -0.03817152, -0.15691681] | [-0.02576007, -0.03817152, -0.15691681] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L224](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/toddlerbot_2xm/toddlerbot_2xm.xml#L224) | [CoM/kinematic input L233](https://github.com/hshi74/toddlerbot/blob/957aadb8e6db85e02fbb9ef90bbcdb4b4c0c9f6c/toddlerbot/descriptions/toddlerbot_2xm/toddlerbot_2xm.xml#L233) | [CoM/kinematic input L232](https://github.com/hshi74/toddlerbot/blob/e337f3b177b4b53abff70b31d1695a7b66cc6d2e/toddlerbot/descriptions/toddlerbot_2xm/toddlerbot_2xm.xml#L232) |
| right_hip_yaw_gear_drive / com_registered | [-0.0352875, -0.0368, -0.11983651] | [-0.0352875, -0.0368, -0.11983651] | [-0.0352875, -0.0368, -0.11983651] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L233](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/toddlerbot_2xm/toddlerbot_2xm.xml#L233) | [CoM/kinematic input L243](https://github.com/hshi74/toddlerbot/blob/957aadb8e6db85e02fbb9ef90bbcdb4b4c0c9f6c/toddlerbot/descriptions/toddlerbot_2xm/toddlerbot_2xm.xml#L243) | [CoM/kinematic input L242](https://github.com/hshi74/toddlerbot/blob/e337f3b177b4b53abff70b31d1695a7b66cc6d2e/toddlerbot/descriptions/toddlerbot_2xm/toddlerbot_2xm.xml#L242) |
| right_knee_link / com_registered | [-0.01156418, -0.037, -0.21665601] | [-0.01156418, -0.037, -0.21665601] | [-0.01156418, -0.037, -0.21665601] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L240](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/toddlerbot_2xm/toddlerbot_2xm.xml#L240) | [CoM/kinematic input L251](https://github.com/hshi74/toddlerbot/blob/957aadb8e6db85e02fbb9ef90bbcdb4b4c0c9f6c/toddlerbot/descriptions/toddlerbot_2xm/toddlerbot_2xm.xml#L251) | [CoM/kinematic input L250](https://github.com/hshi74/toddlerbot/blob/e337f3b177b4b53abff70b31d1695a7b66cc6d2e/toddlerbot/descriptions/toddlerbot_2xm/toddlerbot_2xm.xml#L250) |
| right_ankle_pitch_link / com_registered | [-0.0340567, -0.036812, -0.26399731] | [-0.0340567, -0.036812, -0.26399731] | [-0.0340567, -0.036812, -0.26399731] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L249](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/toddlerbot_2xm/toddlerbot_2xm.xml#L249) | [CoM/kinematic input L260](https://github.com/hshi74/toddlerbot/blob/957aadb8e6db85e02fbb9ef90bbcdb4b4c0c9f6c/toddlerbot/descriptions/toddlerbot_2xm/toddlerbot_2xm.xml#L260) | [CoM/kinematic input L259](https://github.com/hshi74/toddlerbot/blob/e337f3b177b4b53abff70b31d1695a7b66cc6d2e/toddlerbot/descriptions/toddlerbot_2xm/toddlerbot_2xm.xml#L259) |
| right_ankle_roll_link / com_registered | [-0.0032443, -0.03700007, -0.30280941] | [-0.0032443, -0.03700007, -0.30280941] | [-0.0032443, -0.03700007, -0.30280941] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L259](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/toddlerbot_2xm/toddlerbot_2xm.xml#L259) | [CoM/kinematic input L270](https://github.com/hshi74/toddlerbot/blob/957aadb8e6db85e02fbb9ef90bbcdb4b4c0c9f6c/toddlerbot/descriptions/toddlerbot_2xm/toddlerbot_2xm.xml#L270) | [CoM/kinematic input L269](https://github.com/hshi74/toddlerbot/blob/e337f3b177b4b53abff70b31d1695a7b66cc6d2e/toddlerbot/descriptions/toddlerbot_2xm/toddlerbot_2xm.xml#L269) |
| left_shoulder_pitch_link / com_registered | [-0.0200079, 0.0799132, 0.10175] | [-0.0200079, 0.0799132, 0.10175] | [-0.0200079, 0.0799132, 0.10175] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L278](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/toddlerbot_2xm/toddlerbot_2xm.xml#L278) | [CoM/kinematic input L290](https://github.com/hshi74/toddlerbot/blob/957aadb8e6db85e02fbb9ef90bbcdb4b4c0c9f6c/toddlerbot/descriptions/toddlerbot_2xm/toddlerbot_2xm.xml#L290) | [CoM/kinematic input L289](https://github.com/hshi74/toddlerbot/blob/e337f3b177b4b53abff70b31d1695a7b66cc6d2e/toddlerbot/descriptions/toddlerbot_2xm/toddlerbot_2xm.xml#L289) |
| left_shoulder_roll_link / com_registered | [-0.0204677, 0.1057736, 0.09971352] | [-0.0204677, 0.1057736, 0.09971352] | [-0.0204677, 0.1057736, 0.09971352] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L284](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/toddlerbot_2xm/toddlerbot_2xm.xml#L284) | [CoM/kinematic input L297](https://github.com/hshi74/toddlerbot/blob/957aadb8e6db85e02fbb9ef90bbcdb4b4c0c9f6c/toddlerbot/descriptions/toddlerbot_2xm/toddlerbot_2xm.xml#L297) | [CoM/kinematic input L296](https://github.com/hshi74/toddlerbot/blob/e337f3b177b4b53abff70b31d1695a7b66cc6d2e/toddlerbot/descriptions/toddlerbot_2xm/toddlerbot_2xm.xml#L296) |
| left_shoulder_gear_drive / com_registered | [-0.0200079, 0.118, 0.07612614] | [-0.0200079, 0.118, 0.07612614] | [-0.0200079, 0.118, 0.07612614] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L293](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/toddlerbot_2xm/toddlerbot_2xm.xml#L293) | [CoM/kinematic input L307](https://github.com/hshi74/toddlerbot/blob/957aadb8e6db85e02fbb9ef90bbcdb4b4c0c9f6c/toddlerbot/descriptions/toddlerbot_2xm/toddlerbot_2xm.xml#L307) | [CoM/kinematic input L306](https://github.com/hshi74/toddlerbot/blob/e337f3b177b4b53abff70b31d1695a7b66cc6d2e/toddlerbot/descriptions/toddlerbot_2xm/toddlerbot_2xm.xml#L306) |
| left_shoulder_yaw_link / com_registered | [-0.02000811, 0.09400024, 0.0509658] | [-0.02000811, 0.09400024, 0.0509658] | [-0.02000811, 0.09400024, 0.0509658] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L300](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/toddlerbot_2xm/toddlerbot_2xm.xml#L300) | [CoM/kinematic input L315](https://github.com/hshi74/toddlerbot/blob/957aadb8e6db85e02fbb9ef90bbcdb4b4c0c9f6c/toddlerbot/descriptions/toddlerbot_2xm/toddlerbot_2xm.xml#L315) | [CoM/kinematic input L314](https://github.com/hshi74/toddlerbot/blob/e337f3b177b4b53abff70b31d1695a7b66cc6d2e/toddlerbot/descriptions/toddlerbot_2xm/toddlerbot_2xm.xml#L314) |
| left_elbow_roll_link / com_registered | [-0.0204677, 0.1057736, 0.01371352] | [-0.0204677, 0.1057736, 0.01371352] | [-0.0204677, 0.1057736, 0.01371352] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L308](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/toddlerbot_2xm/toddlerbot_2xm.xml#L308) | [CoM/kinematic input L325](https://github.com/hshi74/toddlerbot/blob/957aadb8e6db85e02fbb9ef90bbcdb4b4c0c9f6c/toddlerbot/descriptions/toddlerbot_2xm/toddlerbot_2xm.xml#L325) | [CoM/kinematic input L324](https://github.com/hshi74/toddlerbot/blob/e337f3b177b4b53abff70b31d1695a7b66cc6d2e/toddlerbot/descriptions/toddlerbot_2xm/toddlerbot_2xm.xml#L324) |
| left_elbow_gear_drive / com_registered | [-0.0200079, 0.118, -0.00987386] | [-0.0200079, 0.118, -0.00987386] | [-0.0200079, 0.118, -0.00987386] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L317](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/toddlerbot_2xm/toddlerbot_2xm.xml#L317) | [CoM/kinematic input L335](https://github.com/hshi74/toddlerbot/blob/957aadb8e6db85e02fbb9ef90bbcdb4b4c0c9f6c/toddlerbot/descriptions/toddlerbot_2xm/toddlerbot_2xm.xml#L335) | [CoM/kinematic input L334](https://github.com/hshi74/toddlerbot/blob/e337f3b177b4b53abff70b31d1695a7b66cc6d2e/toddlerbot/descriptions/toddlerbot_2xm/toddlerbot_2xm.xml#L334) |
| left_elbow_yaw_link / com_registered | [-0.02000767, 0.09669789, -0.0426292] | [-0.02000767, 0.09669789, -0.0426292] | [-0.02000767, 0.09669789, -0.0426292] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L324](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/toddlerbot_2xm/toddlerbot_2xm.xml#L324) | [CoM/kinematic input L343](https://github.com/hshi74/toddlerbot/blob/957aadb8e6db85e02fbb9ef90bbcdb4b4c0c9f6c/toddlerbot/descriptions/toddlerbot_2xm/toddlerbot_2xm.xml#L343) | [CoM/kinematic input L342](https://github.com/hshi74/toddlerbot/blob/e337f3b177b4b53abff70b31d1695a7b66cc6d2e/toddlerbot/descriptions/toddlerbot_2xm/toddlerbot_2xm.xml#L342) |
| left_wrist_pitch_link / com_registered | [-0.02042295, 0.0941329, -0.058754] | [-0.02042295, 0.0941329, -0.058754] | [-0.02042295, 0.0941329, -0.058754] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L333](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/toddlerbot_2xm/toddlerbot_2xm.xml#L333) | [CoM/kinematic input L353](https://github.com/hshi74/toddlerbot/blob/957aadb8e6db85e02fbb9ef90bbcdb4b4c0c9f6c/toddlerbot/descriptions/toddlerbot_2xm/toddlerbot_2xm.xml#L353) | [CoM/kinematic input L352](https://github.com/hshi74/toddlerbot/blob/e337f3b177b4b53abff70b31d1695a7b66cc6d2e/toddlerbot/descriptions/toddlerbot_2xm/toddlerbot_2xm.xml#L352) |
| left_wrist_gear_drive / com_registered | [-0.0200079, 0.11803438, -0.04625] | [-0.0200079, 0.11803438, -0.04625] | [-0.0200079, 0.11803438, -0.04625] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L343](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/toddlerbot_2xm/toddlerbot_2xm.xml#L343) | [CoM/kinematic input L363](https://github.com/hshi74/toddlerbot/blob/957aadb8e6db85e02fbb9ef90bbcdb4b4c0c9f6c/toddlerbot/descriptions/toddlerbot_2xm/toddlerbot_2xm.xml#L363) | [CoM/kinematic input L362](https://github.com/hshi74/toddlerbot/blob/e337f3b177b4b53abff70b31d1695a7b66cc6d2e/toddlerbot/descriptions/toddlerbot_2xm/toddlerbot_2xm.xml#L362) |
| left_hand / com_registered | [-0.0213864, 0.09715051, -0.1089045] | [-0.0213864, 0.09715051, -0.1089045] | [-0.0213864, 0.09715051, -0.1089045] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L351](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/toddlerbot_2xm/toddlerbot_2xm.xml#L351) | [CoM/kinematic input L371](https://github.com/hshi74/toddlerbot/blob/957aadb8e6db85e02fbb9ef90bbcdb4b4c0c9f6c/toddlerbot/descriptions/toddlerbot_2xm/toddlerbot_2xm.xml#L371) | [CoM/kinematic input L370](https://github.com/hshi74/toddlerbot/blob/e337f3b177b4b53abff70b31d1695a7b66cc6d2e/toddlerbot/descriptions/toddlerbot_2xm/toddlerbot_2xm.xml#L370) |
| right_shoulder_pitch_link / com_registered | [-0.0200079, -0.0799132, 0.10175] | [-0.0200079, -0.0799132, 0.10175] | [-0.0200079, -0.0799132, 0.10175] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L368](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/toddlerbot_2xm/toddlerbot_2xm.xml#L368) | [CoM/kinematic input L389](https://github.com/hshi74/toddlerbot/blob/957aadb8e6db85e02fbb9ef90bbcdb4b4c0c9f6c/toddlerbot/descriptions/toddlerbot_2xm/toddlerbot_2xm.xml#L389) | [CoM/kinematic input L388](https://github.com/hshi74/toddlerbot/blob/e337f3b177b4b53abff70b31d1695a7b66cc6d2e/toddlerbot/descriptions/toddlerbot_2xm/toddlerbot_2xm.xml#L388) |
| right_shoulder_roll_link / com_registered | [-0.0195481, -0.1057736, 0.09971352] | [-0.0195481, -0.1057736, 0.09971352] | [-0.0195481, -0.1057736, 0.09971352] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L375](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/toddlerbot_2xm/toddlerbot_2xm.xml#L375) | [CoM/kinematic input L396](https://github.com/hshi74/toddlerbot/blob/957aadb8e6db85e02fbb9ef90bbcdb4b4c0c9f6c/toddlerbot/descriptions/toddlerbot_2xm/toddlerbot_2xm.xml#L396) | [CoM/kinematic input L395](https://github.com/hshi74/toddlerbot/blob/e337f3b177b4b53abff70b31d1695a7b66cc6d2e/toddlerbot/descriptions/toddlerbot_2xm/toddlerbot_2xm.xml#L395) |
| right_shoulder_gear_drive / com_registered | [-0.0200079, -0.118, 0.07612614] | [-0.0200079, -0.118, 0.07612614] | [-0.0200079, -0.118, 0.07612614] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L384](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/toddlerbot_2xm/toddlerbot_2xm.xml#L384) | [CoM/kinematic input L406](https://github.com/hshi74/toddlerbot/blob/957aadb8e6db85e02fbb9ef90bbcdb4b4c0c9f6c/toddlerbot/descriptions/toddlerbot_2xm/toddlerbot_2xm.xml#L406) | [CoM/kinematic input L405](https://github.com/hshi74/toddlerbot/blob/e337f3b177b4b53abff70b31d1695a7b66cc6d2e/toddlerbot/descriptions/toddlerbot_2xm/toddlerbot_2xm.xml#L405) |
| right_shoulder_yaw_link / com_registered | [-0.02000769, -0.09400024, 0.0509658] | [-0.02000769, -0.09400024, 0.0509658] | [-0.02000769, -0.09400024, 0.0509658] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L391](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/toddlerbot_2xm/toddlerbot_2xm.xml#L391) | [CoM/kinematic input L414](https://github.com/hshi74/toddlerbot/blob/957aadb8e6db85e02fbb9ef90bbcdb4b4c0c9f6c/toddlerbot/descriptions/toddlerbot_2xm/toddlerbot_2xm.xml#L414) | [CoM/kinematic input L413](https://github.com/hshi74/toddlerbot/blob/e337f3b177b4b53abff70b31d1695a7b66cc6d2e/toddlerbot/descriptions/toddlerbot_2xm/toddlerbot_2xm.xml#L413) |
| right_elbow_roll_link / com_registered | [-0.0195481, -0.1057736, 0.01371352] | [-0.0195481, -0.1057736, 0.01371352] | [-0.0195481, -0.1057736, 0.01371352] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L400](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/toddlerbot_2xm/toddlerbot_2xm.xml#L400) | [CoM/kinematic input L424](https://github.com/hshi74/toddlerbot/blob/957aadb8e6db85e02fbb9ef90bbcdb4b4c0c9f6c/toddlerbot/descriptions/toddlerbot_2xm/toddlerbot_2xm.xml#L424) | [CoM/kinematic input L423](https://github.com/hshi74/toddlerbot/blob/e337f3b177b4b53abff70b31d1695a7b66cc6d2e/toddlerbot/descriptions/toddlerbot_2xm/toddlerbot_2xm.xml#L423) |
| right_elbow_gear_drive / com_registered | [-0.0200079, -0.118, -0.00987386] | [-0.0200079, -0.118, -0.00987386] | [-0.0200079, -0.118, -0.00987386] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L409](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/toddlerbot_2xm/toddlerbot_2xm.xml#L409) | [CoM/kinematic input L434](https://github.com/hshi74/toddlerbot/blob/957aadb8e6db85e02fbb9ef90bbcdb4b4c0c9f6c/toddlerbot/descriptions/toddlerbot_2xm/toddlerbot_2xm.xml#L434) | [CoM/kinematic input L433](https://github.com/hshi74/toddlerbot/blob/e337f3b177b4b53abff70b31d1695a7b66cc6d2e/toddlerbot/descriptions/toddlerbot_2xm/toddlerbot_2xm.xml#L433) |
| right_elbow_yaw_link / com_registered | [-0.02000813, -0.09669789, -0.0426292] | [-0.02000813, -0.09669789, -0.0426292] | [-0.02000813, -0.09669789, -0.0426292] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L416](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/toddlerbot_2xm/toddlerbot_2xm.xml#L416) | [CoM/kinematic input L442](https://github.com/hshi74/toddlerbot/blob/957aadb8e6db85e02fbb9ef90bbcdb4b4c0c9f6c/toddlerbot/descriptions/toddlerbot_2xm/toddlerbot_2xm.xml#L442) | [CoM/kinematic input L441](https://github.com/hshi74/toddlerbot/blob/e337f3b177b4b53abff70b31d1695a7b66cc6d2e/toddlerbot/descriptions/toddlerbot_2xm/toddlerbot_2xm.xml#L441) |
| right_wrist_pitch_link / com_registered | [-0.01959285, -0.0941329, -0.058754] | [-0.01959285, -0.0941329, -0.058754] | [-0.01959285, -0.0941329, -0.058754] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L425](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/toddlerbot_2xm/toddlerbot_2xm.xml#L425) | [CoM/kinematic input L452](https://github.com/hshi74/toddlerbot/blob/957aadb8e6db85e02fbb9ef90bbcdb4b4c0c9f6c/toddlerbot/descriptions/toddlerbot_2xm/toddlerbot_2xm.xml#L452) | [CoM/kinematic input L451](https://github.com/hshi74/toddlerbot/blob/e337f3b177b4b53abff70b31d1695a7b66cc6d2e/toddlerbot/descriptions/toddlerbot_2xm/toddlerbot_2xm.xml#L451) |
| right_wrist_gear_drive / com_registered | [-0.0200079, -0.11803438, -0.04625] | [-0.0200079, -0.11803438, -0.04625] | [-0.0200079, -0.11803438, -0.04625] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L435](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/toddlerbot_2xm/toddlerbot_2xm.xml#L435) | [CoM/kinematic input L462](https://github.com/hshi74/toddlerbot/blob/957aadb8e6db85e02fbb9ef90bbcdb4b4c0c9f6c/toddlerbot/descriptions/toddlerbot_2xm/toddlerbot_2xm.xml#L462) | [CoM/kinematic input L461](https://github.com/hshi74/toddlerbot/blob/e337f3b177b4b53abff70b31d1695a7b66cc6d2e/toddlerbot/descriptions/toddlerbot_2xm/toddlerbot_2xm.xml#L461) |
| right_hand / com_registered | [-0.0213874, -0.09714939, -0.1089053] | [-0.0213874, -0.09714939, -0.1089053] | [-0.0213874, -0.09714939, -0.1089053] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L443](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/toddlerbot_2xm/toddlerbot_2xm.xml#L443) | [CoM/kinematic input L470](https://github.com/hshi74/toddlerbot/blob/957aadb8e6db85e02fbb9ef90bbcdb4b4c0c9f6c/toddlerbot/descriptions/toddlerbot_2xm/toddlerbot_2xm.xml#L470) | [CoM/kinematic input L469](https://github.com/hshi74/toddlerbot/blob/e337f3b177b4b53abff70b31d1695a7b66cc6d2e/toddlerbot/descriptions/toddlerbot_2xm/toddlerbot_2xm.xml#L469) |

## Mass accounting

Every contributing compiled body mass is listed here so total/subtree sums can be checked. Links point to explicit inertials or to geometry inputs when the compiler inferred a mass. CoM links identify inertial inputs; world coordinates additionally use the ancestor transforms and the registration recorded below.

| M body | M kg / source | S kg / source | H kg / source |
|---|---|---|---|
| torso | 1.27503 / [input L40](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/toddlerbot_2xm/toddlerbot_2xm.xml#L40) | 1.27503 / [input L37](https://github.com/hshi74/toddlerbot/blob/957aadb8e6db85e02fbb9ef90bbcdb4b4c0c9f6c/toddlerbot/descriptions/toddlerbot_2xm/toddlerbot_2xm.xml#L37) | 1.27503 / [input L37](https://github.com/hshi74/toddlerbot/blob/e337f3b177b4b53abff70b31d1695a7b66cc6d2e/toddlerbot/descriptions/toddlerbot_2xm/toddlerbot_2xm.xml#L37) |
| neck_yaw_gear_drive | 0.003 / [input L50](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/toddlerbot_2xm/toddlerbot_2xm.xml#L50) | 0.003 / [input L48](https://github.com/hshi74/toddlerbot/blob/957aadb8e6db85e02fbb9ef90bbcdb4b4c0c9f6c/toddlerbot/descriptions/toddlerbot_2xm/toddlerbot_2xm.xml#L48) | 0.003 / [input L48](https://github.com/hshi74/toddlerbot/blob/e337f3b177b4b53abff70b31d1695a7b66cc6d2e/toddlerbot/descriptions/toddlerbot_2xm/toddlerbot_2xm.xml#L48) |
| neck_yaw_link | 0.006 / [input L57](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/toddlerbot_2xm/toddlerbot_2xm.xml#L57) | 0.006 / [input L55](https://github.com/hshi74/toddlerbot/blob/957aadb8e6db85e02fbb9ef90bbcdb4b4c0c9f6c/toddlerbot/descriptions/toddlerbot_2xm/toddlerbot_2xm.xml#L55) | 0.006 / [input L55](https://github.com/hshi74/toddlerbot/blob/e337f3b177b4b53abff70b31d1695a7b66cc6d2e/toddlerbot/descriptions/toddlerbot_2xm/toddlerbot_2xm.xml#L55) |
| head | 0.143321 / [input L71](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/toddlerbot_2xm/toddlerbot_2xm.xml#L71) | 0.143321 / [input L69](https://github.com/hshi74/toddlerbot/blob/957aadb8e6db85e02fbb9ef90bbcdb4b4c0c9f6c/toddlerbot/descriptions/toddlerbot_2xm/toddlerbot_2xm.xml#L69) | 0.143321 / [input L69](https://github.com/hshi74/toddlerbot/blob/e337f3b177b4b53abff70b31d1695a7b66cc6d2e/toddlerbot/descriptions/toddlerbot_2xm/toddlerbot_2xm.xml#L69) |
| neck_pitch_plate | 0.002 / [input L79](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/toddlerbot_2xm/toddlerbot_2xm.xml#L79) | 0.002 / [input L78](https://github.com/hshi74/toddlerbot/blob/957aadb8e6db85e02fbb9ef90bbcdb4b4c0c9f6c/toddlerbot/descriptions/toddlerbot_2xm/toddlerbot_2xm.xml#L78) | 0.002 / [input L78](https://github.com/hshi74/toddlerbot/blob/e337f3b177b4b53abff70b31d1695a7b66cc6d2e/toddlerbot/descriptions/toddlerbot_2xm/toddlerbot_2xm.xml#L78) |
| neck_rod | 0.00297389 / [input L85](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/toddlerbot_2xm/toddlerbot_2xm.xml#L85) | 0.00297389 / [input L85](https://github.com/hshi74/toddlerbot/blob/957aadb8e6db85e02fbb9ef90bbcdb4b4c0c9f6c/toddlerbot/descriptions/toddlerbot_2xm/toddlerbot_2xm.xml#L85) | 0.00297389 / [input L85](https://github.com/hshi74/toddlerbot/blob/e337f3b177b4b53abff70b31d1695a7b66cc6d2e/toddlerbot/descriptions/toddlerbot_2xm/toddlerbot_2xm.xml#L85) |
| neck_rod_2 | 0.00297389 / [input L96](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/toddlerbot_2xm/toddlerbot_2xm.xml#L96) | 0.00297389 / [input L97](https://github.com/hshi74/toddlerbot/blob/957aadb8e6db85e02fbb9ef90bbcdb4b4c0c9f6c/toddlerbot/descriptions/toddlerbot_2xm/toddlerbot_2xm.xml#L97) | 0.00297389 / [input L97](https://github.com/hshi74/toddlerbot/blob/e337f3b177b4b53abff70b31d1695a7b66cc6d2e/toddlerbot/descriptions/toddlerbot_2xm/toddlerbot_2xm.xml#L97) |
| waist_gears | 0.0371617 / [input L110](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/toddlerbot_2xm/toddlerbot_2xm.xml#L110) | 0.0371617 / [input L111](https://github.com/hshi74/toddlerbot/blob/957aadb8e6db85e02fbb9ef90bbcdb4b4c0c9f6c/toddlerbot/descriptions/toddlerbot_2xm/toddlerbot_2xm.xml#L111) | 0.0371617 / [input L111](https://github.com/hshi74/toddlerbot/blob/e337f3b177b4b53abff70b31d1695a7b66cc6d2e/toddlerbot/descriptions/toddlerbot_2xm/toddlerbot_2xm.xml#L111) |
| pelvis_link | 0.1052 / [input L117](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/toddlerbot_2xm/toddlerbot_2xm.xml#L117) | 0.1052 / [input L118](https://github.com/hshi74/toddlerbot/blob/957aadb8e6db85e02fbb9ef90bbcdb4b4c0c9f6c/toddlerbot/descriptions/toddlerbot_2xm/toddlerbot_2xm.xml#L118) | 0.1052 / [input L118](https://github.com/hshi74/toddlerbot/blob/e337f3b177b4b53abff70b31d1695a7b66cc6d2e/toddlerbot/descriptions/toddlerbot_2xm/toddlerbot_2xm.xml#L118) |
| waist_gear_drive | 0.002 / [input L125](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/toddlerbot_2xm/toddlerbot_2xm.xml#L125) | 0.002 / [input L127](https://github.com/hshi74/toddlerbot/blob/957aadb8e6db85e02fbb9ef90bbcdb4b4c0c9f6c/toddlerbot/descriptions/toddlerbot_2xm/toddlerbot_2xm.xml#L127) | 0.002 / [input L127](https://github.com/hshi74/toddlerbot/blob/e337f3b177b4b53abff70b31d1695a7b66cc6d2e/toddlerbot/descriptions/toddlerbot_2xm/toddlerbot_2xm.xml#L127) |
| waist_gear_drive_2 | 0.002 / [input L132](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/toddlerbot_2xm/toddlerbot_2xm.xml#L132) | 0.002 / [input L135](https://github.com/hshi74/toddlerbot/blob/957aadb8e6db85e02fbb9ef90bbcdb4b4c0c9f6c/toddlerbot/descriptions/toddlerbot_2xm/toddlerbot_2xm.xml#L135) | 0.002 / [input L135](https://github.com/hshi74/toddlerbot/blob/e337f3b177b4b53abff70b31d1695a7b66cc6d2e/toddlerbot/descriptions/toddlerbot_2xm/toddlerbot_2xm.xml#L135) |
| left_hip_pitch_link | 0.188221 / [input L139](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/toddlerbot_2xm/toddlerbot_2xm.xml#L139) | 0.188221 / [input L143](https://github.com/hshi74/toddlerbot/blob/957aadb8e6db85e02fbb9ef90bbcdb4b4c0c9f6c/toddlerbot/descriptions/toddlerbot_2xm/toddlerbot_2xm.xml#L143) | 0.188221 / [input L143](https://github.com/hshi74/toddlerbot/blob/e337f3b177b4b53abff70b31d1695a7b66cc6d2e/toddlerbot/descriptions/toddlerbot_2xm/toddlerbot_2xm.xml#L143) |
| left_hip_roll_link | 0.022 / [input L149](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/toddlerbot_2xm/toddlerbot_2xm.xml#L149) | 0.022 / [input L153](https://github.com/hshi74/toddlerbot/blob/957aadb8e6db85e02fbb9ef90bbcdb4b4c0c9f6c/toddlerbot/descriptions/toddlerbot_2xm/toddlerbot_2xm.xml#L153) | 0.022 / [input L153](https://github.com/hshi74/toddlerbot/blob/e337f3b177b4b53abff70b31d1695a7b66cc6d2e/toddlerbot/descriptions/toddlerbot_2xm/toddlerbot_2xm.xml#L153) |
| left_hip_yaw_link | 0.159688 / [input L155](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/toddlerbot_2xm/toddlerbot_2xm.xml#L155) | 0.159688 / [input L160](https://github.com/hshi74/toddlerbot/blob/957aadb8e6db85e02fbb9ef90bbcdb4b4c0c9f6c/toddlerbot/descriptions/toddlerbot_2xm/toddlerbot_2xm.xml#L160) | 0.159688 / [input L160](https://github.com/hshi74/toddlerbot/blob/e337f3b177b4b53abff70b31d1695a7b66cc6d2e/toddlerbot/descriptions/toddlerbot_2xm/toddlerbot_2xm.xml#L160) |
| left_hip_yaw_gear_drive | 0.001 / [input L164](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/toddlerbot_2xm/toddlerbot_2xm.xml#L164) | 0.001 / [input L170](https://github.com/hshi74/toddlerbot/blob/957aadb8e6db85e02fbb9ef90bbcdb4b4c0c9f6c/toddlerbot/descriptions/toddlerbot_2xm/toddlerbot_2xm.xml#L170) | 0.001 / [input L170](https://github.com/hshi74/toddlerbot/blob/e337f3b177b4b53abff70b31d1695a7b66cc6d2e/toddlerbot/descriptions/toddlerbot_2xm/toddlerbot_2xm.xml#L170) |
| left_knee_link | 0.029 / [input L171](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/toddlerbot_2xm/toddlerbot_2xm.xml#L171) | 0.029 / [input L178](https://github.com/hshi74/toddlerbot/blob/957aadb8e6db85e02fbb9ef90bbcdb4b4c0c9f6c/toddlerbot/descriptions/toddlerbot_2xm/toddlerbot_2xm.xml#L178) | 0.029 / [input L178](https://github.com/hshi74/toddlerbot/blob/e337f3b177b4b53abff70b31d1695a7b66cc6d2e/toddlerbot/descriptions/toddlerbot_2xm/toddlerbot_2xm.xml#L178) |
| left_ankle_pitch_link | 0.172721 / [input L180](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/toddlerbot_2xm/toddlerbot_2xm.xml#L180) | 0.172721 / [input L187](https://github.com/hshi74/toddlerbot/blob/957aadb8e6db85e02fbb9ef90bbcdb4b4c0c9f6c/toddlerbot/descriptions/toddlerbot_2xm/toddlerbot_2xm.xml#L187) | 0.172721 / [input L187](https://github.com/hshi74/toddlerbot/blob/e337f3b177b4b53abff70b31d1695a7b66cc6d2e/toddlerbot/descriptions/toddlerbot_2xm/toddlerbot_2xm.xml#L187) |
| left_ankle_roll_link | 0.039 / [input L190](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/toddlerbot_2xm/toddlerbot_2xm.xml#L190) | 0.039 / [input L197](https://github.com/hshi74/toddlerbot/blob/957aadb8e6db85e02fbb9ef90bbcdb4b4c0c9f6c/toddlerbot/descriptions/toddlerbot_2xm/toddlerbot_2xm.xml#L197) | 0.039 / [input L197](https://github.com/hshi74/toddlerbot/blob/e337f3b177b4b53abff70b31d1695a7b66cc6d2e/toddlerbot/descriptions/toddlerbot_2xm/toddlerbot_2xm.xml#L197) |
| right_hip_pitch_link | 0.188221 / [input L208](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/toddlerbot_2xm/toddlerbot_2xm.xml#L208) | 0.188221 / [input L216](https://github.com/hshi74/toddlerbot/blob/957aadb8e6db85e02fbb9ef90bbcdb4b4c0c9f6c/toddlerbot/descriptions/toddlerbot_2xm/toddlerbot_2xm.xml#L216) | 0.188221 / [input L215](https://github.com/hshi74/toddlerbot/blob/e337f3b177b4b53abff70b31d1695a7b66cc6d2e/toddlerbot/descriptions/toddlerbot_2xm/toddlerbot_2xm.xml#L215) |
| right_hip_roll_link | 0.022 / [input L218](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/toddlerbot_2xm/toddlerbot_2xm.xml#L218) | 0.022 / [input L226](https://github.com/hshi74/toddlerbot/blob/957aadb8e6db85e02fbb9ef90bbcdb4b4c0c9f6c/toddlerbot/descriptions/toddlerbot_2xm/toddlerbot_2xm.xml#L226) | 0.022 / [input L225](https://github.com/hshi74/toddlerbot/blob/e337f3b177b4b53abff70b31d1695a7b66cc6d2e/toddlerbot/descriptions/toddlerbot_2xm/toddlerbot_2xm.xml#L225) |
| right_hip_yaw_link | 0.159688 / [input L224](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/toddlerbot_2xm/toddlerbot_2xm.xml#L224) | 0.159688 / [input L233](https://github.com/hshi74/toddlerbot/blob/957aadb8e6db85e02fbb9ef90bbcdb4b4c0c9f6c/toddlerbot/descriptions/toddlerbot_2xm/toddlerbot_2xm.xml#L233) | 0.159688 / [input L232](https://github.com/hshi74/toddlerbot/blob/e337f3b177b4b53abff70b31d1695a7b66cc6d2e/toddlerbot/descriptions/toddlerbot_2xm/toddlerbot_2xm.xml#L232) |
| right_hip_yaw_gear_drive | 0.001 / [input L233](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/toddlerbot_2xm/toddlerbot_2xm.xml#L233) | 0.001 / [input L243](https://github.com/hshi74/toddlerbot/blob/957aadb8e6db85e02fbb9ef90bbcdb4b4c0c9f6c/toddlerbot/descriptions/toddlerbot_2xm/toddlerbot_2xm.xml#L243) | 0.001 / [input L242](https://github.com/hshi74/toddlerbot/blob/e337f3b177b4b53abff70b31d1695a7b66cc6d2e/toddlerbot/descriptions/toddlerbot_2xm/toddlerbot_2xm.xml#L242) |
| right_knee_link | 0.029 / [input L240](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/toddlerbot_2xm/toddlerbot_2xm.xml#L240) | 0.029 / [input L251](https://github.com/hshi74/toddlerbot/blob/957aadb8e6db85e02fbb9ef90bbcdb4b4c0c9f6c/toddlerbot/descriptions/toddlerbot_2xm/toddlerbot_2xm.xml#L251) | 0.029 / [input L250](https://github.com/hshi74/toddlerbot/blob/e337f3b177b4b53abff70b31d1695a7b66cc6d2e/toddlerbot/descriptions/toddlerbot_2xm/toddlerbot_2xm.xml#L250) |
| right_ankle_pitch_link | 0.172721 / [input L249](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/toddlerbot_2xm/toddlerbot_2xm.xml#L249) | 0.172721 / [input L260](https://github.com/hshi74/toddlerbot/blob/957aadb8e6db85e02fbb9ef90bbcdb4b4c0c9f6c/toddlerbot/descriptions/toddlerbot_2xm/toddlerbot_2xm.xml#L260) | 0.172721 / [input L259](https://github.com/hshi74/toddlerbot/blob/e337f3b177b4b53abff70b31d1695a7b66cc6d2e/toddlerbot/descriptions/toddlerbot_2xm/toddlerbot_2xm.xml#L259) |
| right_ankle_roll_link | 0.039 / [input L259](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/toddlerbot_2xm/toddlerbot_2xm.xml#L259) | 0.039 / [input L270](https://github.com/hshi74/toddlerbot/blob/957aadb8e6db85e02fbb9ef90bbcdb4b4c0c9f6c/toddlerbot/descriptions/toddlerbot_2xm/toddlerbot_2xm.xml#L270) | 0.039 / [input L269](https://github.com/hshi74/toddlerbot/blob/e337f3b177b4b53abff70b31d1695a7b66cc6d2e/toddlerbot/descriptions/toddlerbot_2xm/toddlerbot_2xm.xml#L269) |
| left_shoulder_pitch_link | 0.015 / [input L278](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/toddlerbot_2xm/toddlerbot_2xm.xml#L278) | 0.015 / [input L290](https://github.com/hshi74/toddlerbot/blob/957aadb8e6db85e02fbb9ef90bbcdb4b4c0c9f6c/toddlerbot/descriptions/toddlerbot_2xm/toddlerbot_2xm.xml#L290) | 0.015 / [input L289](https://github.com/hshi74/toddlerbot/blob/e337f3b177b4b53abff70b31d1695a7b66cc6d2e/toddlerbot/descriptions/toddlerbot_2xm/toddlerbot_2xm.xml#L289) |
| left_shoulder_roll_link | 0.1152 / [input L284](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/toddlerbot_2xm/toddlerbot_2xm.xml#L284) | 0.1152 / [input L297](https://github.com/hshi74/toddlerbot/blob/957aadb8e6db85e02fbb9ef90bbcdb4b4c0c9f6c/toddlerbot/descriptions/toddlerbot_2xm/toddlerbot_2xm.xml#L297) | 0.1152 / [input L296](https://github.com/hshi74/toddlerbot/blob/e337f3b177b4b53abff70b31d1695a7b66cc6d2e/toddlerbot/descriptions/toddlerbot_2xm/toddlerbot_2xm.xml#L296) |
| left_shoulder_gear_drive | 0.004 / [input L293](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/toddlerbot_2xm/toddlerbot_2xm.xml#L293) | 0.004 / [input L307](https://github.com/hshi74/toddlerbot/blob/957aadb8e6db85e02fbb9ef90bbcdb4b4c0c9f6c/toddlerbot/descriptions/toddlerbot_2xm/toddlerbot_2xm.xml#L307) | 0.004 / [input L306](https://github.com/hshi74/toddlerbot/blob/e337f3b177b4b53abff70b31d1695a7b66cc6d2e/toddlerbot/descriptions/toddlerbot_2xm/toddlerbot_2xm.xml#L306) |
| left_shoulder_yaw_link | 0.0247439 / [input L300](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/toddlerbot_2xm/toddlerbot_2xm.xml#L300) | 0.0247439 / [input L315](https://github.com/hshi74/toddlerbot/blob/957aadb8e6db85e02fbb9ef90bbcdb4b4c0c9f6c/toddlerbot/descriptions/toddlerbot_2xm/toddlerbot_2xm.xml#L315) | 0.0247439 / [input L314](https://github.com/hshi74/toddlerbot/blob/e337f3b177b4b53abff70b31d1695a7b66cc6d2e/toddlerbot/descriptions/toddlerbot_2xm/toddlerbot_2xm.xml#L314) |
| left_elbow_roll_link | 0.1152 / [input L308](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/toddlerbot_2xm/toddlerbot_2xm.xml#L308) | 0.1152 / [input L325](https://github.com/hshi74/toddlerbot/blob/957aadb8e6db85e02fbb9ef90bbcdb4b4c0c9f6c/toddlerbot/descriptions/toddlerbot_2xm/toddlerbot_2xm.xml#L325) | 0.1152 / [input L324](https://github.com/hshi74/toddlerbot/blob/e337f3b177b4b53abff70b31d1695a7b66cc6d2e/toddlerbot/descriptions/toddlerbot_2xm/toddlerbot_2xm.xml#L324) |
| left_elbow_gear_drive | 0.004 / [input L317](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/toddlerbot_2xm/toddlerbot_2xm.xml#L317) | 0.004 / [input L335](https://github.com/hshi74/toddlerbot/blob/957aadb8e6db85e02fbb9ef90bbcdb4b4c0c9f6c/toddlerbot/descriptions/toddlerbot_2xm/toddlerbot_2xm.xml#L335) | 0.004 / [input L334](https://github.com/hshi74/toddlerbot/blob/e337f3b177b4b53abff70b31d1695a7b66cc6d2e/toddlerbot/descriptions/toddlerbot_2xm/toddlerbot_2xm.xml#L334) |
| left_elbow_yaw_link | 0.0302318 / [input L324](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/toddlerbot_2xm/toddlerbot_2xm.xml#L324) | 0.0302318 / [input L343](https://github.com/hshi74/toddlerbot/blob/957aadb8e6db85e02fbb9ef90bbcdb4b4c0c9f6c/toddlerbot/descriptions/toddlerbot_2xm/toddlerbot_2xm.xml#L343) | 0.0302318 / [input L342](https://github.com/hshi74/toddlerbot/blob/e337f3b177b4b53abff70b31d1695a7b66cc6d2e/toddlerbot/descriptions/toddlerbot_2xm/toddlerbot_2xm.xml#L342) |
| left_wrist_pitch_link | 0.1276 / [input L333](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/toddlerbot_2xm/toddlerbot_2xm.xml#L333) | 0.1276 / [input L353](https://github.com/hshi74/toddlerbot/blob/957aadb8e6db85e02fbb9ef90bbcdb4b4c0c9f6c/toddlerbot/descriptions/toddlerbot_2xm/toddlerbot_2xm.xml#L353) | 0.1276 / [input L352](https://github.com/hshi74/toddlerbot/blob/e337f3b177b4b53abff70b31d1695a7b66cc6d2e/toddlerbot/descriptions/toddlerbot_2xm/toddlerbot_2xm.xml#L352) |
| left_wrist_gear_drive | 0.003 / [input L343](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/toddlerbot_2xm/toddlerbot_2xm.xml#L343) | 0.003 / [input L363](https://github.com/hshi74/toddlerbot/blob/957aadb8e6db85e02fbb9ef90bbcdb4b4c0c9f6c/toddlerbot/descriptions/toddlerbot_2xm/toddlerbot_2xm.xml#L363) | 0.003 / [input L362](https://github.com/hshi74/toddlerbot/blob/e337f3b177b4b53abff70b31d1695a7b66cc6d2e/toddlerbot/descriptions/toddlerbot_2xm/toddlerbot_2xm.xml#L362) |
| left_hand | 0.043 / [input L351](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/toddlerbot_2xm/toddlerbot_2xm.xml#L351) | 0.043 / [input L371](https://github.com/hshi74/toddlerbot/blob/957aadb8e6db85e02fbb9ef90bbcdb4b4c0c9f6c/toddlerbot/descriptions/toddlerbot_2xm/toddlerbot_2xm.xml#L371) | 0.043 / [input L370](https://github.com/hshi74/toddlerbot/blob/e337f3b177b4b53abff70b31d1695a7b66cc6d2e/toddlerbot/descriptions/toddlerbot_2xm/toddlerbot_2xm.xml#L370) |
| right_shoulder_pitch_link | 0.015 / [input L368](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/toddlerbot_2xm/toddlerbot_2xm.xml#L368) | 0.015 / [input L389](https://github.com/hshi74/toddlerbot/blob/957aadb8e6db85e02fbb9ef90bbcdb4b4c0c9f6c/toddlerbot/descriptions/toddlerbot_2xm/toddlerbot_2xm.xml#L389) | 0.015 / [input L388](https://github.com/hshi74/toddlerbot/blob/e337f3b177b4b53abff70b31d1695a7b66cc6d2e/toddlerbot/descriptions/toddlerbot_2xm/toddlerbot_2xm.xml#L388) |
| right_shoulder_roll_link | 0.1152 / [input L375](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/toddlerbot_2xm/toddlerbot_2xm.xml#L375) | 0.1152 / [input L396](https://github.com/hshi74/toddlerbot/blob/957aadb8e6db85e02fbb9ef90bbcdb4b4c0c9f6c/toddlerbot/descriptions/toddlerbot_2xm/toddlerbot_2xm.xml#L396) | 0.1152 / [input L395](https://github.com/hshi74/toddlerbot/blob/e337f3b177b4b53abff70b31d1695a7b66cc6d2e/toddlerbot/descriptions/toddlerbot_2xm/toddlerbot_2xm.xml#L395) |
| right_shoulder_gear_drive | 0.004 / [input L384](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/toddlerbot_2xm/toddlerbot_2xm.xml#L384) | 0.004 / [input L406](https://github.com/hshi74/toddlerbot/blob/957aadb8e6db85e02fbb9ef90bbcdb4b4c0c9f6c/toddlerbot/descriptions/toddlerbot_2xm/toddlerbot_2xm.xml#L406) | 0.004 / [input L405](https://github.com/hshi74/toddlerbot/blob/e337f3b177b4b53abff70b31d1695a7b66cc6d2e/toddlerbot/descriptions/toddlerbot_2xm/toddlerbot_2xm.xml#L405) |
| right_shoulder_yaw_link | 0.0247439 / [input L391](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/toddlerbot_2xm/toddlerbot_2xm.xml#L391) | 0.0247439 / [input L414](https://github.com/hshi74/toddlerbot/blob/957aadb8e6db85e02fbb9ef90bbcdb4b4c0c9f6c/toddlerbot/descriptions/toddlerbot_2xm/toddlerbot_2xm.xml#L414) | 0.0247439 / [input L413](https://github.com/hshi74/toddlerbot/blob/e337f3b177b4b53abff70b31d1695a7b66cc6d2e/toddlerbot/descriptions/toddlerbot_2xm/toddlerbot_2xm.xml#L413) |
| right_elbow_roll_link | 0.1152 / [input L400](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/toddlerbot_2xm/toddlerbot_2xm.xml#L400) | 0.1152 / [input L424](https://github.com/hshi74/toddlerbot/blob/957aadb8e6db85e02fbb9ef90bbcdb4b4c0c9f6c/toddlerbot/descriptions/toddlerbot_2xm/toddlerbot_2xm.xml#L424) | 0.1152 / [input L423](https://github.com/hshi74/toddlerbot/blob/e337f3b177b4b53abff70b31d1695a7b66cc6d2e/toddlerbot/descriptions/toddlerbot_2xm/toddlerbot_2xm.xml#L423) |
| right_elbow_gear_drive | 0.004 / [input L409](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/toddlerbot_2xm/toddlerbot_2xm.xml#L409) | 0.004 / [input L434](https://github.com/hshi74/toddlerbot/blob/957aadb8e6db85e02fbb9ef90bbcdb4b4c0c9f6c/toddlerbot/descriptions/toddlerbot_2xm/toddlerbot_2xm.xml#L434) | 0.004 / [input L433](https://github.com/hshi74/toddlerbot/blob/e337f3b177b4b53abff70b31d1695a7b66cc6d2e/toddlerbot/descriptions/toddlerbot_2xm/toddlerbot_2xm.xml#L433) |
| right_elbow_yaw_link | 0.0302318 / [input L416](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/toddlerbot_2xm/toddlerbot_2xm.xml#L416) | 0.0302318 / [input L442](https://github.com/hshi74/toddlerbot/blob/957aadb8e6db85e02fbb9ef90bbcdb4b4c0c9f6c/toddlerbot/descriptions/toddlerbot_2xm/toddlerbot_2xm.xml#L442) | 0.0302318 / [input L441](https://github.com/hshi74/toddlerbot/blob/e337f3b177b4b53abff70b31d1695a7b66cc6d2e/toddlerbot/descriptions/toddlerbot_2xm/toddlerbot_2xm.xml#L441) |
| right_wrist_pitch_link | 0.1276 / [input L425](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/toddlerbot_2xm/toddlerbot_2xm.xml#L425) | 0.1276 / [input L452](https://github.com/hshi74/toddlerbot/blob/957aadb8e6db85e02fbb9ef90bbcdb4b4c0c9f6c/toddlerbot/descriptions/toddlerbot_2xm/toddlerbot_2xm.xml#L452) | 0.1276 / [input L451](https://github.com/hshi74/toddlerbot/blob/e337f3b177b4b53abff70b31d1695a7b66cc6d2e/toddlerbot/descriptions/toddlerbot_2xm/toddlerbot_2xm.xml#L451) |
| right_wrist_gear_drive | 0.003 / [input L435](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/toddlerbot_2xm/toddlerbot_2xm.xml#L435) | 0.003 / [input L462](https://github.com/hshi74/toddlerbot/blob/957aadb8e6db85e02fbb9ef90bbcdb4b4c0c9f6c/toddlerbot/descriptions/toddlerbot_2xm/toddlerbot_2xm.xml#L462) | 0.003 / [input L461](https://github.com/hshi74/toddlerbot/blob/e337f3b177b4b53abff70b31d1695a7b66cc6d2e/toddlerbot/descriptions/toddlerbot_2xm/toddlerbot_2xm.xml#L461) |
| right_hand | 0.043 / [input L443](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/toddlerbot_2xm/toddlerbot_2xm.xml#L443) | 0.043 / [input L470](https://github.com/hshi74/toddlerbot/blob/957aadb8e6db85e02fbb9ef90bbcdb4b4c0c9f6c/toddlerbot/descriptions/toddlerbot_2xm/toddlerbot_2xm.xml#L470) | 0.043 / [input L469](https://github.com/hshi74/toddlerbot/blob/e337f3b177b4b53abff70b31d1695a7b66cc6d2e/toddlerbot/descriptions/toddlerbot_2xm/toddlerbot_2xm.xml#L469) |

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
    "file": "toddlerbot_2xm/toddlerbot_2xm.xml",
    "status": "passed",
    "findings": 0
  },
  {
    "file": "toddlerbot_2xm/toddlerbot_2xm_mjx.xml",
    "status": "passed",
    "findings": 0
  },
  {
    "file": "toddlerbot_2xm/toddlerbot_2xm_pos.xml",
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
      "toddlerbot_2xm/toddlerbot_2xm.xml"
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
      "toddlerbot/descriptions/toddlerbot_2xm/toddlerbot_2xm.xml"
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
      "toddlerbot/descriptions/toddlerbot_2xm/toddlerbot_2xm.xml"
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
