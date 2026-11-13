# booster_t1

Status: **complete**. Provenance: **dated match**, confidence **medium**.

Source selected using the ordered amended provenance rules.

M: `https://github.com/google-deepmind/mujoco_menagerie`, `booster_t1/t1.xml`, commit `370c43965323c0944b433b202aac5058b5f907a9`.
H: `https://github.com/BoosterRobotics/booster_gym`, `resources/T1/T1_serial.urdf`, commit `da396a06d6eed99e2de72d7749c48ee8748950f9`.
S: `687a33d08b08875fe45dc8d91b54db83766df8b9` (2025-01-09T17:05:05+08:00). Menagerie release/change: 2025-02-07T13:33:47-08:00.

Limit semantics: MJCF effort values are supported actuator torque/force envelopes. URDF effort and velocity values are manufacturer declarations retained from XML; MuJoCo does not enforce those tags. Such declaration comparisons are explicitly distinct from compiled inertial/range quantities.


## Source evidence

```json
[
  {
    "url": "https://github.com/BoosterRobotics/booster_gym/blob/main/resources/T1/T1_serial.urdf",
    "document": "booster_t1/README.md",
    "commit": "370c43965323c0944b433b202aac5058b5f907a9",
    "current": true
  }
]
```


## README derivation evidence

Documentation labels are conservative: an automated documented label requires an explicit affected entity and quantity. Broader conversion notes are retained here for review.

> 2. Added the following to the URDF `<robot>` tag `<mujoco><compiler balanceinertia="true" discardvisual="false" fusestatic="false" strippath="false"/></mujoco>`.

## Kinematics consistency

A proper Kabsch rigid transform aligns all matched zero-pose body origins. The maximum per-origin residual and signed hinge/slide axis angles determine whether CoM can be compared; RMS is also recorded. Fewer than three non-collinear origins give insufficient kinematic coverage. CoM records that fail either required M/H or M/S check are excluded from counts and largest discrepancies. Masses, principal moments and raw joint ranges remain unchanged; a flagged range still requires convention review.

| Pair | Status | Origins / rank | RMS / maximum mm | Disagreeing / checked axes |
|---|---|---:|---:|---:|
| M/H | consistent | 24 / 3 | 5.33127086e-12 / 1.1935422e-11 | 0 / 23 |
| M/S | consistent | 24 / 3 | 5.33127086e-12 / 1.1935422e-11 | 0 / 23 |

Exact fitted transforms, per-origin residuals, thresholds and axis vectors:

```json
{
  "M/H": {
    "status": "consistent",
    "matched_body_origins": 24,
    "position_threshold_m": 0.005,
    "axis_threshold_rad": 0.005,
    "residual_definition": "maximum Euclidean residual over matched body origins; Kabsch minimizes RMS, which is also recorded",
    "coordinate_frames": "each snapshot registered to its matched report anchor",
    "anchor_m": "Trunk",
    "anchor_other": "Trunk",
    "rotation_other_to_m": [
      [
        1.0,
        2.303608133649402e-17,
        -4.852687162179156e-18
      ],
      [
        -2.303608133649402e-17,
        1.0,
        -1.928671092301675e-17
      ],
      [
        -1.734723475976807e-18,
        1.928671092301675e-17,
        0.9999999999999999
      ]
    ],
    "translation_other_to_m": [
      0.0,
      -3.4912304044203964e-19,
      2.2898349882893854e-15
    ],
    "rms_residual_m": 5.331270862363089e-15,
    "max_residual_m": 1.1935421954481479e-14,
    "fit_rank": 3,
    "axis_checks": [
      {
        "joint_m": "AAHead_yaw",
        "joint_other": "AAHead_yaw",
        "axis_m": [
          0.0,
          0.0,
          1.0
        ],
        "axis_other_aligned": [
          -4.852687162179157e-18,
          -1.9286710923016753e-17,
          1.0
        ],
        "angle_rad": 1.9887830221569976e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "Head_pitch",
        "joint_other": "Head_pitch",
        "axis_m": [
          0.0,
          1.0,
          0.0
        ],
        "axis_other_aligned": [
          2.303608133649402e-17,
          1.0,
          1.928671092301675e-17
        ],
        "angle_rad": 3.004393884911866e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "Left_Shoulder_Pitch",
        "joint_other": "Left_Shoulder_Pitch",
        "axis_m": [
          0.0,
          1.0,
          0.0
        ],
        "axis_other_aligned": [
          2.303608133649402e-17,
          1.0,
          1.928671092301675e-17
        ],
        "angle_rad": 3.004393884911866e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "Left_Shoulder_Roll",
        "joint_other": "Left_Shoulder_Roll",
        "axis_m": [
          0.9999996118050369,
          0.0,
          -0.0008811298289748864
        ],
        "axis_other_aligned": [
          0.9999996118049868,
          -2.301907829660553e-17,
          -0.0008811298859832416
        ],
        "angle_rad": 5.7008377294010465e-11,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "Left_Elbow_Pitch",
        "joint_other": "Left_Elbow_Pitch",
        "axis_m": [
          0.0,
          1.0,
          0.0
        ],
        "axis_other_aligned": [
          2.303608133649402e-17,
          1.0,
          1.928671092301675e-17
        ],
        "angle_rad": 3.004393884911866e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "Left_Elbow_Yaw",
        "joint_other": "Left_Elbow_Yaw",
        "axis_m": [
          0.0008811298289748864,
          0.0,
          0.9999996118050369
        ],
        "axis_other_aligned": [
          0.0008811298859832352,
          -1.9307001215733275e-17,
          0.9999996118049868
        ],
        "angle_rad": 5.700837089721627e-11,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "Right_Shoulder_Pitch",
        "joint_other": "Right_Shoulder_Pitch",
        "axis_m": [
          0.0,
          1.0,
          0.0
        ],
        "axis_other_aligned": [
          2.303608133649402e-17,
          1.0,
          1.928671092301675e-17
        ],
        "angle_rad": 3.004393884911866e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "Right_Shoulder_Roll",
        "joint_other": "Right_Shoulder_Roll",
        "axis_m": [
          0.9999996118050369,
          0.0,
          -0.0008811298289748864
        ],
        "axis_other_aligned": [
          0.9999996118049868,
          -2.301907829660553e-17,
          -0.0008811298859832416
        ],
        "angle_rad": 5.7008377294010465e-11,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "Right_Elbow_Pitch",
        "joint_other": "Right_Elbow_Pitch",
        "axis_m": [
          0.0,
          1.0,
          0.0
        ],
        "axis_other_aligned": [
          2.303608133649402e-17,
          1.0,
          1.928671092301675e-17
        ],
        "angle_rad": 3.004393884911866e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "Right_Elbow_Yaw",
        "joint_other": "Right_Elbow_Yaw",
        "axis_m": [
          0.0008811298289748864,
          0.0,
          0.9999996118050369
        ],
        "axis_other_aligned": [
          0.0008811298859832352,
          -1.9307001215733275e-17,
          0.9999996118049868
        ],
        "angle_rad": 5.700837089721627e-11,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "Waist",
        "joint_other": "Waist",
        "axis_m": [
          0.0,
          0.0,
          1.0
        ],
        "axis_other_aligned": [
          -4.852687162179157e-18,
          -1.9286710923016753e-17,
          1.0
        ],
        "angle_rad": 1.9887830221569976e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "Left_Hip_Pitch",
        "joint_other": "Left_Hip_Pitch",
        "axis_m": [
          0.0,
          1.0,
          0.0
        ],
        "axis_other_aligned": [
          2.303608133649402e-17,
          1.0,
          1.928671092301675e-17
        ],
        "angle_rad": 3.004393884911866e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "Left_Hip_Roll",
        "joint_other": "Left_Hip_Roll",
        "axis_m": [
          1.0,
          0.0,
          0.0
        ],
        "axis_other_aligned": [
          1.0,
          -2.303608133649402e-17,
          -1.734723475976807e-18
        ],
        "angle_rad": 2.3101305350124118e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "Left_Hip_Yaw",
        "joint_other": "Left_Hip_Yaw",
        "axis_m": [
          0.0,
          0.0,
          1.0
        ],
        "axis_other_aligned": [
          -4.852687162179157e-18,
          -1.9286710923016753e-17,
          1.0
        ],
        "angle_rad": 1.9887830221569976e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "Left_Knee_Pitch",
        "joint_other": "Left_Knee_Pitch",
        "axis_m": [
          0.0,
          1.0,
          0.0
        ],
        "axis_other_aligned": [
          2.303608133649402e-17,
          1.0,
          1.928671092301675e-17
        ],
        "angle_rad": 3.004393884911866e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "Left_Ankle_Pitch",
        "joint_other": "Left_Ankle_Pitch",
        "axis_m": [
          0.0,
          1.0,
          0.0
        ],
        "axis_other_aligned": [
          2.303608133649402e-17,
          1.0,
          1.928671092301675e-17
        ],
        "angle_rad": 3.004393884911866e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "Left_Ankle_Roll",
        "joint_other": "Left_Ankle_Roll",
        "axis_m": [
          1.0,
          0.0,
          0.0
        ],
        "axis_other_aligned": [
          1.0,
          -2.303608133649402e-17,
          -1.734723475976807e-18
        ],
        "angle_rad": 2.3101305350124118e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "Right_Hip_Pitch",
        "joint_other": "Right_Hip_Pitch",
        "axis_m": [
          0.0,
          1.0,
          0.0
        ],
        "axis_other_aligned": [
          2.303608133649402e-17,
          1.0,
          1.928671092301675e-17
        ],
        "angle_rad": 3.004393884911866e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "Right_Hip_Roll",
        "joint_other": "Right_Hip_Roll",
        "axis_m": [
          1.0,
          0.0,
          0.0
        ],
        "axis_other_aligned": [
          1.0,
          -2.303608133649402e-17,
          -1.734723475976807e-18
        ],
        "angle_rad": 2.3101305350124118e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "Right_Hip_Yaw",
        "joint_other": "Right_Hip_Yaw",
        "axis_m": [
          0.0,
          0.0,
          1.0
        ],
        "axis_other_aligned": [
          -4.852687162179157e-18,
          -1.9286710923016753e-17,
          1.0
        ],
        "angle_rad": 1.9887830221569976e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "Right_Knee_Pitch",
        "joint_other": "Right_Knee_Pitch",
        "axis_m": [
          0.0,
          1.0,
          0.0
        ],
        "axis_other_aligned": [
          2.303608133649402e-17,
          1.0,
          1.928671092301675e-17
        ],
        "angle_rad": 3.004393884911866e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "Right_Ankle_Pitch",
        "joint_other": "Right_Ankle_Pitch",
        "axis_m": [
          0.0,
          1.0,
          0.0
        ],
        "axis_other_aligned": [
          2.303608133649402e-17,
          1.0,
          1.928671092301675e-17
        ],
        "angle_rad": 3.004393884911866e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "Right_Ankle_Roll",
        "joint_other": "Right_Ankle_Roll",
        "axis_m": [
          1.0,
          0.0,
          0.0
        ],
        "axis_other_aligned": [
          1.0,
          -2.303608133649402e-17,
          -1.734723475976807e-18
        ],
        "angle_rad": 2.3101305350124118e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      }
    ],
    "axis_disagreements": [],
    "com_eligible": true,
    "covariance_singular_values": [
      2.4115979179611373,
      0.5564577850000003,
      0.0036468318489220573
    ],
    "origin_residuals_m": {
      "Trunk": 2.2898350149041627e-15,
      "H1": 2.275966412572291e-15,
      "H2": 2.164948479181279e-15,
      "AL1": 2.275957200481571e-15,
      "AL2": 2.2761370122754635e-15,
      "AL3": 1.1935026609722786e-14,
      "left_hand_link": 1.1935413886351996e-14,
      "AR1": 2.275957200481571e-15,
      "AR2": 2.2761370122754635e-15,
      "AR3": 1.193503467811407e-14,
      "right_hand_link": 1.1935421954481479e-14,
      "Waist": 2.34534618055726e-15,
      "Hip_Pitch_Left": 2.345346139520643e-15,
      "Hip_Roll_Left": 2.3869795029440866e-15,
      "Hip_Yaw_Left": 2.3869795029440866e-15,
      "Shank_Left": 2.3869795029440866e-15,
      "Ankle_Cross_Left": 2.5535506677393078e-15,
      "left_foot_link": 2.5535506677393078e-15,
      "Hip_Pitch_Right": 2.345346139520643e-15,
      "Hip_Roll_Right": 2.3314683517128287e-15,
      "Hip_Yaw_Right": 2.3869795029440866e-15,
      "Shank_Right": 2.3869795029440866e-15,
      "Ankle_Cross_Right": 2.5535506677393078e-15,
      "right_foot_link": 2.5535506677393078e-15
    },
    "reason": "Unique proper rigid fit and matched signed axes meet the configured thresholds"
  },
  "M/S": {
    "status": "consistent",
    "matched_body_origins": 24,
    "position_threshold_m": 0.005,
    "axis_threshold_rad": 0.005,
    "residual_definition": "maximum Euclidean residual over matched body origins; Kabsch minimizes RMS, which is also recorded",
    "coordinate_frames": "each snapshot registered to its matched report anchor",
    "anchor_m": "Trunk",
    "anchor_other": "Trunk",
    "rotation_other_to_m": [
      [
        1.0,
        2.303608133649402e-17,
        -4.852687162179156e-18
      ],
      [
        -2.303608133649402e-17,
        1.0,
        -1.928671092301675e-17
      ],
      [
        -1.734723475976807e-18,
        1.928671092301675e-17,
        0.9999999999999999
      ]
    ],
    "translation_other_to_m": [
      0.0,
      -3.4912304044203964e-19,
      2.2898349882893854e-15
    ],
    "rms_residual_m": 5.331270862363089e-15,
    "max_residual_m": 1.1935421954481479e-14,
    "fit_rank": 3,
    "axis_checks": [
      {
        "joint_m": "AAHead_yaw",
        "joint_other": "AAHead_yaw",
        "axis_m": [
          0.0,
          0.0,
          1.0
        ],
        "axis_other_aligned": [
          -4.852687162179157e-18,
          -1.9286710923016753e-17,
          1.0
        ],
        "angle_rad": 1.9887830221569976e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "Head_pitch",
        "joint_other": "Head_pitch",
        "axis_m": [
          0.0,
          1.0,
          0.0
        ],
        "axis_other_aligned": [
          2.303608133649402e-17,
          1.0,
          1.928671092301675e-17
        ],
        "angle_rad": 3.004393884911866e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "Left_Shoulder_Pitch",
        "joint_other": "Left_Shoulder_Pitch",
        "axis_m": [
          0.0,
          1.0,
          0.0
        ],
        "axis_other_aligned": [
          2.303608133649402e-17,
          1.0,
          1.928671092301675e-17
        ],
        "angle_rad": 3.004393884911866e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "Left_Shoulder_Roll",
        "joint_other": "Left_Shoulder_Roll",
        "axis_m": [
          0.9999996118050369,
          0.0,
          -0.0008811298289748864
        ],
        "axis_other_aligned": [
          0.9999996118049868,
          -2.301907829660553e-17,
          -0.0008811298859832416
        ],
        "angle_rad": 5.7008377294010465e-11,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "Left_Elbow_Pitch",
        "joint_other": "Left_Elbow_Pitch",
        "axis_m": [
          0.0,
          1.0,
          0.0
        ],
        "axis_other_aligned": [
          2.303608133649402e-17,
          1.0,
          1.928671092301675e-17
        ],
        "angle_rad": 3.004393884911866e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "Left_Elbow_Yaw",
        "joint_other": "Left_Elbow_Yaw",
        "axis_m": [
          0.0008811298289748864,
          0.0,
          0.9999996118050369
        ],
        "axis_other_aligned": [
          0.0008811298859832352,
          -1.9307001215733275e-17,
          0.9999996118049868
        ],
        "angle_rad": 5.700837089721627e-11,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "Right_Shoulder_Pitch",
        "joint_other": "Right_Shoulder_Pitch",
        "axis_m": [
          0.0,
          1.0,
          0.0
        ],
        "axis_other_aligned": [
          2.303608133649402e-17,
          1.0,
          1.928671092301675e-17
        ],
        "angle_rad": 3.004393884911866e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "Right_Shoulder_Roll",
        "joint_other": "Right_Shoulder_Roll",
        "axis_m": [
          0.9999996118050369,
          0.0,
          -0.0008811298289748864
        ],
        "axis_other_aligned": [
          0.9999996118049868,
          -2.301907829660553e-17,
          -0.0008811298859832416
        ],
        "angle_rad": 5.7008377294010465e-11,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "Right_Elbow_Pitch",
        "joint_other": "Right_Elbow_Pitch",
        "axis_m": [
          0.0,
          1.0,
          0.0
        ],
        "axis_other_aligned": [
          2.303608133649402e-17,
          1.0,
          1.928671092301675e-17
        ],
        "angle_rad": 3.004393884911866e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "Right_Elbow_Yaw",
        "joint_other": "Right_Elbow_Yaw",
        "axis_m": [
          0.0008811298289748864,
          0.0,
          0.9999996118050369
        ],
        "axis_other_aligned": [
          0.0008811298859832352,
          -1.9307001215733275e-17,
          0.9999996118049868
        ],
        "angle_rad": 5.700837089721627e-11,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "Waist",
        "joint_other": "Waist",
        "axis_m": [
          0.0,
          0.0,
          1.0
        ],
        "axis_other_aligned": [
          -4.852687162179157e-18,
          -1.9286710923016753e-17,
          1.0
        ],
        "angle_rad": 1.9887830221569976e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "Left_Hip_Pitch",
        "joint_other": "Left_Hip_Pitch",
        "axis_m": [
          0.0,
          1.0,
          0.0
        ],
        "axis_other_aligned": [
          2.303608133649402e-17,
          1.0,
          1.928671092301675e-17
        ],
        "angle_rad": 3.004393884911866e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "Left_Hip_Roll",
        "joint_other": "Left_Hip_Roll",
        "axis_m": [
          1.0,
          0.0,
          0.0
        ],
        "axis_other_aligned": [
          1.0,
          -2.303608133649402e-17,
          -1.734723475976807e-18
        ],
        "angle_rad": 2.3101305350124118e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "Left_Hip_Yaw",
        "joint_other": "Left_Hip_Yaw",
        "axis_m": [
          0.0,
          0.0,
          1.0
        ],
        "axis_other_aligned": [
          -4.852687162179157e-18,
          -1.9286710923016753e-17,
          1.0
        ],
        "angle_rad": 1.9887830221569976e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "Left_Knee_Pitch",
        "joint_other": "Left_Knee_Pitch",
        "axis_m": [
          0.0,
          1.0,
          0.0
        ],
        "axis_other_aligned": [
          2.303608133649402e-17,
          1.0,
          1.928671092301675e-17
        ],
        "angle_rad": 3.004393884911866e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "Left_Ankle_Pitch",
        "joint_other": "Left_Ankle_Pitch",
        "axis_m": [
          0.0,
          1.0,
          0.0
        ],
        "axis_other_aligned": [
          2.303608133649402e-17,
          1.0,
          1.928671092301675e-17
        ],
        "angle_rad": 3.004393884911866e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "Left_Ankle_Roll",
        "joint_other": "Left_Ankle_Roll",
        "axis_m": [
          1.0,
          0.0,
          0.0
        ],
        "axis_other_aligned": [
          1.0,
          -2.303608133649402e-17,
          -1.734723475976807e-18
        ],
        "angle_rad": 2.3101305350124118e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "Right_Hip_Pitch",
        "joint_other": "Right_Hip_Pitch",
        "axis_m": [
          0.0,
          1.0,
          0.0
        ],
        "axis_other_aligned": [
          2.303608133649402e-17,
          1.0,
          1.928671092301675e-17
        ],
        "angle_rad": 3.004393884911866e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "Right_Hip_Roll",
        "joint_other": "Right_Hip_Roll",
        "axis_m": [
          1.0,
          0.0,
          0.0
        ],
        "axis_other_aligned": [
          1.0,
          -2.303608133649402e-17,
          -1.734723475976807e-18
        ],
        "angle_rad": 2.3101305350124118e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "Right_Hip_Yaw",
        "joint_other": "Right_Hip_Yaw",
        "axis_m": [
          0.0,
          0.0,
          1.0
        ],
        "axis_other_aligned": [
          -4.852687162179157e-18,
          -1.9286710923016753e-17,
          1.0
        ],
        "angle_rad": 1.9887830221569976e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "Right_Knee_Pitch",
        "joint_other": "Right_Knee_Pitch",
        "axis_m": [
          0.0,
          1.0,
          0.0
        ],
        "axis_other_aligned": [
          2.303608133649402e-17,
          1.0,
          1.928671092301675e-17
        ],
        "angle_rad": 3.004393884911866e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "Right_Ankle_Pitch",
        "joint_other": "Right_Ankle_Pitch",
        "axis_m": [
          0.0,
          1.0,
          0.0
        ],
        "axis_other_aligned": [
          2.303608133649402e-17,
          1.0,
          1.928671092301675e-17
        ],
        "angle_rad": 3.004393884911866e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "Right_Ankle_Roll",
        "joint_other": "Right_Ankle_Roll",
        "axis_m": [
          1.0,
          0.0,
          0.0
        ],
        "axis_other_aligned": [
          1.0,
          -2.303608133649402e-17,
          -1.734723475976807e-18
        ],
        "angle_rad": 2.3101305350124118e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      }
    ],
    "axis_disagreements": [],
    "com_eligible": true,
    "covariance_singular_values": [
      2.4115979179611373,
      0.5564577850000003,
      0.0036468318489220573
    ],
    "origin_residuals_m": {
      "Trunk": 2.2898350149041627e-15,
      "H1": 2.275966412572291e-15,
      "H2": 2.164948479181279e-15,
      "AL1": 2.275957200481571e-15,
      "AL2": 2.2761370122754635e-15,
      "AL3": 1.1935026609722786e-14,
      "left_hand_link": 1.1935413886351996e-14,
      "AR1": 2.275957200481571e-15,
      "AR2": 2.2761370122754635e-15,
      "AR3": 1.193503467811407e-14,
      "right_hand_link": 1.1935421954481479e-14,
      "Waist": 2.34534618055726e-15,
      "Hip_Pitch_Left": 2.345346139520643e-15,
      "Hip_Roll_Left": 2.3869795029440866e-15,
      "Hip_Yaw_Left": 2.3869795029440866e-15,
      "Shank_Left": 2.3869795029440866e-15,
      "Ankle_Cross_Left": 2.5535506677393078e-15,
      "left_foot_link": 2.5535506677393078e-15,
      "Hip_Pitch_Right": 2.345346139520643e-15,
      "Hip_Roll_Right": 2.3314683517128287e-15,
      "Hip_Yaw_Right": 2.3869795029440866e-15,
      "Shank_Right": 2.3869795029440866e-15,
      "Ankle_Cross_Right": 2.5535506677393078e-15,
      "right_foot_link": 2.5535506677393078e-15
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
| robot / total_com_registered | [0.055661025, -0.000214324572, -0.0688251004] | [0.0556610399, -0.000214324567, -0.0688249701] | [0.0556610399, -0.000214324567, -0.0688249701] | [1.48928486e-08, 5.23419174e-12, 1.30261524e-07] | eligible; compared after Kabsch alignment | [aggregate inputs](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/booster_t1/t1.xml#L1) | [aggregate inputs](https://github.com/BoosterRobotics/booster_gym/blob/687a33d08b08875fe45dc8d91b54db83766df8b9/resources/T1/T1_serial.urdf#L1) | [aggregate inputs](https://github.com/BoosterRobotics/booster_gym/blob/da396a06d6eed99e2de72d7749c48ee8748950f9/resources/T1/T1_serial.urdf#L1) |
| Trunk / com_registered | [0.0551365, -1.42058e-06, 0.105062] | [0.0551365401, -1.42058018e-06, 0.105062333] | [0.0551365401, -1.42058018e-06, 0.105062333] | [4.01093076e-08, -1.7623659e-13, 3.32707657e-07] | eligible; compared after Kabsch alignment | [CoM/kinematic input L55](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/booster_t1/t1.xml#L55) | [CoM/kinematic input L12](https://github.com/BoosterRobotics/booster_gym/blob/687a33d08b08875fe45dc8d91b54db83766df8b9/resources/T1/T1_serial.urdf#L12) | [CoM/kinematic input L12](https://github.com/BoosterRobotics/booster_gym/blob/da396a06d6eed99e2de72d7749c48ee8748950f9/resources/T1/T1_serial.urdf#L12) |
| H1 / com_registered | [0.061992, -0.001403, 0.300432] | [0.061992, -0.001403, 0.300432] | [0.061992, -0.001403, 0.300432] | [0, 0, -5.55111512e-17] | eligible; compared after Kabsch alignment | [CoM/kinematic input L61](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/booster_t1/t1.xml#L61) | [CoM/kinematic input L51](https://github.com/BoosterRobotics/booster_gym/blob/687a33d08b08875fe45dc8d91b54db83766df8b9/resources/T1/T1_serial.urdf#L51) | [CoM/kinematic input L51](https://github.com/BoosterRobotics/booster_gym/blob/da396a06d6eed99e2de72d7749c48ee8748950f9/resources/T1/T1_serial.urdf#L51) |
| H2 / com_registered | [0.070302, 0.001262, 0.403481] | [0.070302, 0.001262, 0.403481] | [0.070302, 0.001262, 0.403481] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L66](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/booster_t1/t1.xml#L66) | [CoM/kinematic input L100](https://github.com/BoosterRobotics/booster_gym/blob/687a33d08b08875fe45dc8d91b54db83766df8b9/resources/T1/T1_serial.urdf#L100) | [CoM/kinematic input L100](https://github.com/BoosterRobotics/booster_gym/blob/da396a06d6eed99e2de72d7749c48ee8748950f9/resources/T1/T1_serial.urdf#L100) |
| AL1 / com_registered | [0.0568230003, 0.151274, 0.219000597] | [0.0568230003, 0.151274, 0.219000597] | [0.0568230003, 0.151274, 0.219000597] | [3.46944695e-17, 0, 3.85802501e-14] | eligible; compared after Kabsch alignment | [CoM/kinematic input L74](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/booster_t1/t1.xml#L74) | [CoM/kinematic input L157](https://github.com/BoosterRobotics/booster_gym/blob/687a33d08b08875fe45dc8d91b54db83766df8b9/resources/T1/T1_serial.urdf#L157) | [CoM/kinematic input L157](https://github.com/BoosterRobotics/booster_gym/blob/da396a06d6eed99e2de72d7749c48ee8748950f9/resources/T1/T1_serial.urdf#L157) |
| AL2 / com_registered | [0.0613619985, 0.191276, 0.218996597] | [0.0613619985, 0.191276, 0.218996597] | [0.0613619985, 0.191276, 0.218996597] | [-1.94289029e-16, -2.77555756e-17, -2.2012947e-13] | eligible; compared after Kabsch alignment | [CoM/kinematic input L79](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/booster_t1/t1.xml#L79) | [CoM/kinematic input L206](https://github.com/BoosterRobotics/booster_gym/blob/687a33d08b08875fe45dc8d91b54db83766df8b9/resources/T1/T1_serial.urdf#L206) | [CoM/kinematic input L206](https://github.com/BoosterRobotics/booster_gym/blob/da396a06d6eed99e2de72d7749c48ee8748950f9/resources/T1/T1_serial.urdf#L206) |
| AL3 / com_registered | [0.0577499127, 0.299153, 0.21890078] | [0.0577499127, 0.299153, 0.21890078] | [0.0577499127, 0.299153, 0.21890078] | [-5.65519853e-15, -5.55111512e-17, -1.41830991e-14] | eligible; compared after Kabsch alignment | [CoM/kinematic input L84](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/booster_t1/t1.xml#L84) | [CoM/kinematic input L255](https://github.com/BoosterRobotics/booster_gym/blob/687a33d08b08875fe45dc8d91b54db83766df8b9/resources/T1/T1_serial.urdf#L255) | [CoM/kinematic input L255](https://github.com/BoosterRobotics/booster_gym/blob/da396a06d6eed99e2de72d7749c48ee8748950f9/resources/T1/T1_serial.urdf#L255) |
| left_hand_link / com_registered | [0.0576425207, 0.470473, 0.219590875] | [0.0576425207, 0.470473, 0.219590875] | [0.0576425207, 0.470473, 0.219590875] | [3.36883299e-14, -1.11022302e-16, -8.10462808e-15] | eligible; compared after Kabsch alignment | [CoM/kinematic input L90](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/booster_t1/t1.xml#L90) | [CoM/kinematic input L312](https://github.com/BoosterRobotics/booster_gym/blob/687a33d08b08875fe45dc8d91b54db83766df8b9/resources/T1/T1_serial.urdf#L312) | [CoM/kinematic input L312](https://github.com/BoosterRobotics/booster_gym/blob/da396a06d6eed99e2de72d7749c48ee8748950f9/resources/T1/T1_serial.urdf#L312) |
| AR1 / com_registered | [0.0568230003, -0.151274, 0.219000597] | [0.0568230003, -0.151274, 0.219000597] | [0.0568230003, -0.151274, 0.219000597] | [3.46944695e-17, 0, 3.85802501e-14] | eligible; compared after Kabsch alignment | [CoM/kinematic input L100](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/booster_t1/t1.xml#L100) | [CoM/kinematic input L369](https://github.com/BoosterRobotics/booster_gym/blob/687a33d08b08875fe45dc8d91b54db83766df8b9/resources/T1/T1_serial.urdf#L369) | [CoM/kinematic input L369](https://github.com/BoosterRobotics/booster_gym/blob/da396a06d6eed99e2de72d7749c48ee8748950f9/resources/T1/T1_serial.urdf#L369) |
| AR2 / com_registered | [0.0613619985, -0.191276, 0.218996597] | [0.0613619985, -0.191276, 0.218996597] | [0.0613619985, -0.191276, 0.218996597] | [-1.94289029e-16, 2.77555756e-17, -2.2012947e-13] | eligible; compared after Kabsch alignment | [CoM/kinematic input L105](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/booster_t1/t1.xml#L105) | [CoM/kinematic input L418](https://github.com/BoosterRobotics/booster_gym/blob/687a33d08b08875fe45dc8d91b54db83766df8b9/resources/T1/T1_serial.urdf#L418) | [CoM/kinematic input L418](https://github.com/BoosterRobotics/booster_gym/blob/da396a06d6eed99e2de72d7749c48ee8748950f9/resources/T1/T1_serial.urdf#L418) |
| AR3 / com_registered | [0.0577499127, -0.299153, 0.21890078] | [0.0577499127, -0.299153, 0.21890078] | [0.0577499127, -0.299153, 0.21890078] | [-5.65519853e-15, 5.55111512e-17, -1.41830991e-14] | eligible; compared after Kabsch alignment | [CoM/kinematic input L110](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/booster_t1/t1.xml#L110) | [CoM/kinematic input L467](https://github.com/BoosterRobotics/booster_gym/blob/687a33d08b08875fe45dc8d91b54db83766df8b9/resources/T1/T1_serial.urdf#L467) | [CoM/kinematic input L467](https://github.com/BoosterRobotics/booster_gym/blob/da396a06d6eed99e2de72d7749c48ee8748950f9/resources/T1/T1_serial.urdf#L467) |
| right_hand_link / com_registered | [0.0576425207, -0.470473, 0.219590875] | [0.0576425207, -0.470473, 0.219590875] | [0.0576425207, -0.470473, 0.219590875] | [3.36883299e-14, 1.11022302e-16, -8.10462808e-15] | eligible; compared after Kabsch alignment | [CoM/kinematic input L116](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/booster_t1/t1.xml#L116) | [CoM/kinematic input L524](https://github.com/BoosterRobotics/booster_gym/blob/687a33d08b08875fe45dc8d91b54db83766df8b9/resources/T1/T1_serial.urdf#L524) | [CoM/kinematic input L524](https://github.com/BoosterRobotics/booster_gym/blob/da396a06d6eed99e2de72d7749c48ee8748950f9/resources/T1/T1_serial.urdf#L524) |
| Waist / com_registered | [0.064784, 3e-06, -0.108199] | [0.064784, 3e-06, -0.108199] | [0.064784, 3e-06, -0.108199] | [0, 0, 4.16333634e-17] | eligible; compared after Kabsch alignment | [CoM/kinematic input L126](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/booster_t1/t1.xml#L126) | [CoM/kinematic input L581](https://github.com/BoosterRobotics/booster_gym/blob/687a33d08b08875fe45dc8d91b54db83766df8b9/resources/T1/T1_serial.urdf#L581) | [CoM/kinematic input L581](https://github.com/BoosterRobotics/booster_gym/blob/da396a06d6eed99e2de72d7749c48ee8748950f9/resources/T1/T1_serial.urdf#L581) |
| Hip_Pitch_Left / com_registered | [0.063034, 0.098704, -0.133583] | [0.063034, 0.098704, -0.133583] | [0.063034, 0.098704, -0.133583] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L131](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/booster_t1/t1.xml#L131) | [CoM/kinematic input L630](https://github.com/BoosterRobotics/booster_gym/blob/687a33d08b08875fe45dc8d91b54db83766df8b9/resources/T1/T1_serial.urdf#L630) | [CoM/kinematic input L630](https://github.com/BoosterRobotics/booster_gym/blob/da396a06d6eed99e2de72d7749c48ee8748950f9/resources/T1/T1_serial.urdf#L630) |
| Hip_Roll_Left / com_registered | [0.063601, 0.106024, -0.18925] | [0.063601, 0.106024, -0.18925] | [0.063601, 0.106024, -0.18925] | [0, 0, 2.77555756e-17] | eligible; compared after Kabsch alignment | [CoM/kinematic input L136](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/booster_t1/t1.xml#L136) | [CoM/kinematic input L679](https://github.com/BoosterRobotics/booster_gym/blob/687a33d08b08875fe45dc8d91b54db83766df8b9/resources/T1/T1_serial.urdf#L679) | [CoM/kinematic input L679](https://github.com/BoosterRobotics/booster_gym/blob/da396a06d6eed99e2de72d7749c48ee8748950f9/resources/T1/T1_serial.urdf#L679) |
| Hip_Yaw_Left / com_registered | [0.055267, 0.106206, -0.306538] | [0.055267, 0.106206, -0.306538] | [0.055267, 0.106206, -0.306538] | [0, 0, 5.55111512e-17] | eligible; compared after Kabsch alignment | [CoM/kinematic input L141](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/booster_t1/t1.xml#L141) | [CoM/kinematic input L728](https://github.com/BoosterRobotics/booster_gym/blob/687a33d08b08875fe45dc8d91b54db83766df8b9/resources/T1/T1_serial.urdf#L728) | [CoM/kinematic input L728](https://github.com/BoosterRobotics/booster_gym/blob/da396a06d6eed99e2de72d7749c48ee8748950f9/resources/T1/T1_serial.urdf#L728) |
| Shank_Left / com_registered | [0.042488, 0.106259, -0.475672] | [0.042488, 0.106259, -0.475672] | [0.042488, 0.106259, -0.475672] | [0, 0, 5.55111512e-17] | eligible; compared after Kabsch alignment | [CoM/kinematic input L147](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/booster_t1/t1.xml#L147) | [CoM/kinematic input L785](https://github.com/BoosterRobotics/booster_gym/blob/687a33d08b08875fe45dc8d91b54db83766df8b9/resources/T1/T1_serial.urdf#L785) | [CoM/kinematic input L785](https://github.com/BoosterRobotics/booster_gym/blob/da396a06d6eed99e2de72d7749c48ee8748950f9/resources/T1/T1_serial.urdf#L785) |
| Ankle_Cross_Left / com_registered | [0.044778, 0.106, -0.639335] | [0.044778, 0.106, -0.639335] | [0.044778, 0.106, -0.639335] | [0, 0, 1.11022302e-16] | eligible; compared after Kabsch alignment | [CoM/kinematic input L153](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/booster_t1/t1.xml#L153) | [CoM/kinematic input L842](https://github.com/BoosterRobotics/booster_gym/blob/687a33d08b08875fe45dc8d91b54db83766df8b9/resources/T1/T1_serial.urdf#L842) | [CoM/kinematic input L842](https://github.com/BoosterRobotics/booster_gym/blob/da396a06d6eed99e2de72d7749c48ee8748950f9/resources/T1/T1_serial.urdf#L842) |
| left_foot_link / com_registered | [0.048251, 0.10625, -0.652494] | [0.048251, 0.10625, -0.652494] | [0.048251, 0.10625, -0.652494] | [0, 0, 1.11022302e-16] | eligible; compared after Kabsch alignment | [CoM/kinematic input L158](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/booster_t1/t1.xml#L158) | [CoM/kinematic input L891](https://github.com/BoosterRobotics/booster_gym/blob/687a33d08b08875fe45dc8d91b54db83766df8b9/resources/T1/T1_serial.urdf#L891) | [CoM/kinematic input L891](https://github.com/BoosterRobotics/booster_gym/blob/da396a06d6eed99e2de72d7749c48ee8748950f9/resources/T1/T1_serial.urdf#L891) |
| Hip_Pitch_Right / com_registered | [0.063034, -0.098486, -0.133582] | [0.063034, -0.098486, -0.133582] | [0.063034, -0.098486, -0.133582] | [0, 0, 8.32667268e-17] | eligible; compared after Kabsch alignment | [CoM/kinematic input L170](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/booster_t1/t1.xml#L170) | [CoM/kinematic input L948](https://github.com/BoosterRobotics/booster_gym/blob/687a33d08b08875fe45dc8d91b54db83766df8b9/resources/T1/T1_serial.urdf#L948) | [CoM/kinematic input L948](https://github.com/BoosterRobotics/booster_gym/blob/da396a06d6eed99e2de72d7749c48ee8748950f9/resources/T1/T1_serial.urdf#L948) |
| Hip_Roll_Right / com_registered | [0.063599, -0.105976, -0.189248] | [0.063599, -0.105976, -0.189248] | [0.063599, -0.105976, -0.189248] | [0, 0, 8.32667268e-17] | eligible; compared after Kabsch alignment | [CoM/kinematic input L175](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/booster_t1/t1.xml#L175) | [CoM/kinematic input L997](https://github.com/BoosterRobotics/booster_gym/blob/687a33d08b08875fe45dc8d91b54db83766df8b9/resources/T1/T1_serial.urdf#L997) | [CoM/kinematic input L997](https://github.com/BoosterRobotics/booster_gym/blob/da396a06d6eed99e2de72d7749c48ee8748950f9/resources/T1/T1_serial.urdf#L997) |
| Hip_Yaw_Right / com_registered | [0.055309, -0.106149, -0.306574] | [0.055309, -0.106149, -0.306574] | [0.055309, -0.106149, -0.306574] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L180](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/booster_t1/t1.xml#L180) | [CoM/kinematic input L1046](https://github.com/BoosterRobotics/booster_gym/blob/687a33d08b08875fe45dc8d91b54db83766df8b9/resources/T1/T1_serial.urdf#L1046) | [CoM/kinematic input L1046](https://github.com/BoosterRobotics/booster_gym/blob/da396a06d6eed99e2de72d7749c48ee8748950f9/resources/T1/T1_serial.urdf#L1046) |
| Shank_Right / com_registered | [0.042759, -0.106541, -0.473956] | [0.042759, -0.106541, -0.473956] | [0.042759, -0.106541, -0.473956] | [0, 0, 5.55111512e-17] | eligible; compared after Kabsch alignment | [CoM/kinematic input L186](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/booster_t1/t1.xml#L186) | [CoM/kinematic input L1103](https://github.com/BoosterRobotics/booster_gym/blob/687a33d08b08875fe45dc8d91b54db83766df8b9/resources/T1/T1_serial.urdf#L1103) | [CoM/kinematic input L1103](https://github.com/BoosterRobotics/booster_gym/blob/da396a06d6eed99e2de72d7749c48ee8748950f9/resources/T1/T1_serial.urdf#L1103) |
| Ankle_Cross_Right / com_registered | [0.044778, -0.106, -0.639335] | [0.044778, -0.106, -0.639335] | [0.044778, -0.106, -0.639335] | [0, 0, 1.11022302e-16] | eligible; compared after Kabsch alignment | [CoM/kinematic input L192](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/booster_t1/t1.xml#L192) | [CoM/kinematic input L1160](https://github.com/BoosterRobotics/booster_gym/blob/687a33d08b08875fe45dc8d91b54db83766df8b9/resources/T1/T1_serial.urdf#L1160) | [CoM/kinematic input L1160](https://github.com/BoosterRobotics/booster_gym/blob/da396a06d6eed99e2de72d7749c48ee8748950f9/resources/T1/T1_serial.urdf#L1160) |
| right_foot_link / com_registered | [0.048252, -0.10625, -0.652494] | [0.048252, -0.10625, -0.652494] | [0.048252, -0.10625, -0.652494] | [0, 0, 1.11022302e-16] | eligible; compared after Kabsch alignment | [CoM/kinematic input L197](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/booster_t1/t1.xml#L197) | [CoM/kinematic input L1209](https://github.com/BoosterRobotics/booster_gym/blob/687a33d08b08875fe45dc8d91b54db83766df8b9/resources/T1/T1_serial.urdf#L1209) | [CoM/kinematic input L1209](https://github.com/BoosterRobotics/booster_gym/blob/da396a06d6eed99e2de72d7749c48ee8748950f9/resources/T1/T1_serial.urdf#L1209) |

## Mass accounting

Every contributing compiled body mass is listed here so total/subtree sums can be checked. Links point to explicit inertials or to geometry inputs when the compiler inferred a mass. CoM links identify inertial inputs; world coordinates additionally use the ancestor transforms and the registration recorded below.

| M body | M kg / source | S kg / source | H kg / source |
|---|---|---|---|
| Trunk | 11.7 / [input L55](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/booster_t1/t1.xml#L55) | 11.7 / [input L14](https://github.com/BoosterRobotics/booster_gym/blob/687a33d08b08875fe45dc8d91b54db83766df8b9/resources/T1/T1_serial.urdf#L14) | 11.7 / [input L14](https://github.com/BoosterRobotics/booster_gym/blob/da396a06d6eed99e2de72d7749c48ee8748950f9/resources/T1/T1_serial.urdf#L14) |
| H1 | 0.44391 / [input L61](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/booster_t1/t1.xml#L61) | 0.44391 / [input L53](https://github.com/BoosterRobotics/booster_gym/blob/687a33d08b08875fe45dc8d91b54db83766df8b9/resources/T1/T1_serial.urdf#L53) | 0.44391 / [input L53](https://github.com/BoosterRobotics/booster_gym/blob/da396a06d6eed99e2de72d7749c48ee8748950f9/resources/T1/T1_serial.urdf#L53) |
| H2 | 0.631019 / [input L66](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/booster_t1/t1.xml#L66) | 0.631019 / [input L102](https://github.com/BoosterRobotics/booster_gym/blob/687a33d08b08875fe45dc8d91b54db83766df8b9/resources/T1/T1_serial.urdf#L102) | 0.631019 / [input L102](https://github.com/BoosterRobotics/booster_gym/blob/da396a06d6eed99e2de72d7749c48ee8748950f9/resources/T1/T1_serial.urdf#L102) |
| AL1 | 0.53 / [input L74](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/booster_t1/t1.xml#L74) | 0.53 / [input L159](https://github.com/BoosterRobotics/booster_gym/blob/687a33d08b08875fe45dc8d91b54db83766df8b9/resources/T1/T1_serial.urdf#L159) | 0.53 / [input L159](https://github.com/BoosterRobotics/booster_gym/blob/da396a06d6eed99e2de72d7749c48ee8748950f9/resources/T1/T1_serial.urdf#L159) |
| AL2 | 0.16 / [input L79](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/booster_t1/t1.xml#L79) | 0.16 / [input L208](https://github.com/BoosterRobotics/booster_gym/blob/687a33d08b08875fe45dc8d91b54db83766df8b9/resources/T1/T1_serial.urdf#L208) | 0.16 / [input L208](https://github.com/BoosterRobotics/booster_gym/blob/da396a06d6eed99e2de72d7749c48ee8748950f9/resources/T1/T1_serial.urdf#L208) |
| AL3 | 1.02 / [input L84](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/booster_t1/t1.xml#L84) | 1.02 / [input L257](https://github.com/BoosterRobotics/booster_gym/blob/687a33d08b08875fe45dc8d91b54db83766df8b9/resources/T1/T1_serial.urdf#L257) | 1.02 / [input L257](https://github.com/BoosterRobotics/booster_gym/blob/da396a06d6eed99e2de72d7749c48ee8748950f9/resources/T1/T1_serial.urdf#L257) |
| left_hand_link | 0.327214 / [input L90](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/booster_t1/t1.xml#L90) | 0.327214391 / [input L314](https://github.com/BoosterRobotics/booster_gym/blob/687a33d08b08875fe45dc8d91b54db83766df8b9/resources/T1/T1_serial.urdf#L314) | 0.327214391 / [input L314](https://github.com/BoosterRobotics/booster_gym/blob/da396a06d6eed99e2de72d7749c48ee8748950f9/resources/T1/T1_serial.urdf#L314) |
| AR1 | 0.53 / [input L100](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/booster_t1/t1.xml#L100) | 0.53 / [input L371](https://github.com/BoosterRobotics/booster_gym/blob/687a33d08b08875fe45dc8d91b54db83766df8b9/resources/T1/T1_serial.urdf#L371) | 0.53 / [input L371](https://github.com/BoosterRobotics/booster_gym/blob/da396a06d6eed99e2de72d7749c48ee8748950f9/resources/T1/T1_serial.urdf#L371) |
| AR2 | 0.16 / [input L105](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/booster_t1/t1.xml#L105) | 0.16 / [input L420](https://github.com/BoosterRobotics/booster_gym/blob/687a33d08b08875fe45dc8d91b54db83766df8b9/resources/T1/T1_serial.urdf#L420) | 0.16 / [input L420](https://github.com/BoosterRobotics/booster_gym/blob/da396a06d6eed99e2de72d7749c48ee8748950f9/resources/T1/T1_serial.urdf#L420) |
| AR3 | 1.02 / [input L110](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/booster_t1/t1.xml#L110) | 1.02 / [input L469](https://github.com/BoosterRobotics/booster_gym/blob/687a33d08b08875fe45dc8d91b54db83766df8b9/resources/T1/T1_serial.urdf#L469) | 1.02 / [input L469](https://github.com/BoosterRobotics/booster_gym/blob/da396a06d6eed99e2de72d7749c48ee8748950f9/resources/T1/T1_serial.urdf#L469) |
| right_hand_link | 0.327214 / [input L116](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/booster_t1/t1.xml#L116) | 0.327214391 / [input L526](https://github.com/BoosterRobotics/booster_gym/blob/687a33d08b08875fe45dc8d91b54db83766df8b9/resources/T1/T1_serial.urdf#L526) | 0.327214391 / [input L526](https://github.com/BoosterRobotics/booster_gym/blob/da396a06d6eed99e2de72d7749c48ee8748950f9/resources/T1/T1_serial.urdf#L526) |
| Waist | 2.581 / [input L126](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/booster_t1/t1.xml#L126) | 2.581 / [input L583](https://github.com/BoosterRobotics/booster_gym/blob/687a33d08b08875fe45dc8d91b54db83766df8b9/resources/T1/T1_serial.urdf#L583) | 2.581 / [input L583](https://github.com/BoosterRobotics/booster_gym/blob/da396a06d6eed99e2de72d7749c48ee8748950f9/resources/T1/T1_serial.urdf#L583) |
| Hip_Pitch_Left | 1.021 / [input L131](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/booster_t1/t1.xml#L131) | 1.021 / [input L632](https://github.com/BoosterRobotics/booster_gym/blob/687a33d08b08875fe45dc8d91b54db83766df8b9/resources/T1/T1_serial.urdf#L632) | 1.021 / [input L632](https://github.com/BoosterRobotics/booster_gym/blob/da396a06d6eed99e2de72d7749c48ee8748950f9/resources/T1/T1_serial.urdf#L632) |
| Hip_Roll_Left | 0.385 / [input L136](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/booster_t1/t1.xml#L136) | 0.385 / [input L681](https://github.com/BoosterRobotics/booster_gym/blob/687a33d08b08875fe45dc8d91b54db83766df8b9/resources/T1/T1_serial.urdf#L681) | 0.385 / [input L681](https://github.com/BoosterRobotics/booster_gym/blob/da396a06d6eed99e2de72d7749c48ee8748950f9/resources/T1/T1_serial.urdf#L681) |
| Hip_Yaw_Left | 2.166 / [input L141](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/booster_t1/t1.xml#L141) | 2.166 / [input L730](https://github.com/BoosterRobotics/booster_gym/blob/687a33d08b08875fe45dc8d91b54db83766df8b9/resources/T1/T1_serial.urdf#L730) | 2.166 / [input L730](https://github.com/BoosterRobotics/booster_gym/blob/da396a06d6eed99e2de72d7749c48ee8748950f9/resources/T1/T1_serial.urdf#L730) |
| Shank_Left | 1.73 / [input L147](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/booster_t1/t1.xml#L147) | 1.73 / [input L787](https://github.com/BoosterRobotics/booster_gym/blob/687a33d08b08875fe45dc8d91b54db83766df8b9/resources/T1/T1_serial.urdf#L787) | 1.73 / [input L787](https://github.com/BoosterRobotics/booster_gym/blob/da396a06d6eed99e2de72d7749c48ee8748950f9/resources/T1/T1_serial.urdf#L787) |
| Ankle_Cross_Left | 0.073 / [input L153](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/booster_t1/t1.xml#L153) | 0.073 / [input L844](https://github.com/BoosterRobotics/booster_gym/blob/687a33d08b08875fe45dc8d91b54db83766df8b9/resources/T1/T1_serial.urdf#L844) | 0.073 / [input L844](https://github.com/BoosterRobotics/booster_gym/blob/da396a06d6eed99e2de72d7749c48ee8748950f9/resources/T1/T1_serial.urdf#L844) |
| left_foot_link | 0.685 / [input L158](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/booster_t1/t1.xml#L158) | 0.685 / [input L893](https://github.com/BoosterRobotics/booster_gym/blob/687a33d08b08875fe45dc8d91b54db83766df8b9/resources/T1/T1_serial.urdf#L893) | 0.685 / [input L893](https://github.com/BoosterRobotics/booster_gym/blob/da396a06d6eed99e2de72d7749c48ee8748950f9/resources/T1/T1_serial.urdf#L893) |
| Hip_Pitch_Right | 1.021 / [input L170](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/booster_t1/t1.xml#L170) | 1.021 / [input L950](https://github.com/BoosterRobotics/booster_gym/blob/687a33d08b08875fe45dc8d91b54db83766df8b9/resources/T1/T1_serial.urdf#L950) | 1.021 / [input L950](https://github.com/BoosterRobotics/booster_gym/blob/da396a06d6eed99e2de72d7749c48ee8748950f9/resources/T1/T1_serial.urdf#L950) |
| Hip_Roll_Right | 0.385 / [input L175](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/booster_t1/t1.xml#L175) | 0.385 / [input L999](https://github.com/BoosterRobotics/booster_gym/blob/687a33d08b08875fe45dc8d91b54db83766df8b9/resources/T1/T1_serial.urdf#L999) | 0.385 / [input L999](https://github.com/BoosterRobotics/booster_gym/blob/da396a06d6eed99e2de72d7749c48ee8748950f9/resources/T1/T1_serial.urdf#L999) |
| Hip_Yaw_Right | 2.17 / [input L180](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/booster_t1/t1.xml#L180) | 2.17 / [input L1048](https://github.com/BoosterRobotics/booster_gym/blob/687a33d08b08875fe45dc8d91b54db83766df8b9/resources/T1/T1_serial.urdf#L1048) | 2.17 / [input L1048](https://github.com/BoosterRobotics/booster_gym/blob/da396a06d6eed99e2de72d7749c48ee8748950f9/resources/T1/T1_serial.urdf#L1048) |
| Shank_Right | 1.79 / [input L186](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/booster_t1/t1.xml#L186) | 1.79 / [input L1105](https://github.com/BoosterRobotics/booster_gym/blob/687a33d08b08875fe45dc8d91b54db83766df8b9/resources/T1/T1_serial.urdf#L1105) | 1.79 / [input L1105](https://github.com/BoosterRobotics/booster_gym/blob/da396a06d6eed99e2de72d7749c48ee8748950f9/resources/T1/T1_serial.urdf#L1105) |
| Ankle_Cross_Right | 0.073 / [input L192](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/booster_t1/t1.xml#L192) | 0.073 / [input L1162](https://github.com/BoosterRobotics/booster_gym/blob/687a33d08b08875fe45dc8d91b54db83766df8b9/resources/T1/T1_serial.urdf#L1162) | 0.073 / [input L1162](https://github.com/BoosterRobotics/booster_gym/blob/da396a06d6eed99e2de72d7749c48ee8748950f9/resources/T1/T1_serial.urdf#L1162) |
| right_foot_link | 0.685 / [input L197](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/booster_t1/t1.xml#L197) | 0.685 / [input L1211](https://github.com/BoosterRobotics/booster_gym/blob/687a33d08b08875fe45dc8d91b54db83766df8b9/resources/T1/T1_serial.urdf#L1211) | 0.685 / [input L1211](https://github.com/BoosterRobotics/booster_gym/blob/da396a06d6eed99e2de72d7749c48ee8748950f9/resources/T1/T1_serial.urdf#L1211) |

## Coverage and unmatched elements

```json
{
  "mapping_h": {
    "bodies": {
      "Trunk": "Trunk",
      "H1": "H1",
      "H2": "H2",
      "AL1": "AL1",
      "AL2": "AL2",
      "AL3": "AL3",
      "left_hand_link": "left_hand_link",
      "AR1": "AR1",
      "AR2": "AR2",
      "AR3": "AR3",
      "right_hand_link": "right_hand_link",
      "Waist": "Waist",
      "Hip_Pitch_Left": "Hip_Pitch_Left",
      "Hip_Roll_Left": "Hip_Roll_Left",
      "Hip_Yaw_Left": "Hip_Yaw_Left",
      "Shank_Left": "Shank_Left",
      "Ankle_Cross_Left": "Ankle_Cross_Left",
      "left_foot_link": "left_foot_link",
      "Hip_Pitch_Right": "Hip_Pitch_Right",
      "Hip_Roll_Right": "Hip_Roll_Right",
      "Hip_Yaw_Right": "Hip_Yaw_Right",
      "Shank_Right": "Shank_Right",
      "Ankle_Cross_Right": "Ankle_Cross_Right",
      "right_foot_link": "right_foot_link"
    },
    "joints": {
      "AAHead_yaw": "AAHead_yaw",
      "Head_pitch": "Head_pitch",
      "Left_Shoulder_Pitch": "Left_Shoulder_Pitch",
      "Left_Shoulder_Roll": "Left_Shoulder_Roll",
      "Left_Elbow_Pitch": "Left_Elbow_Pitch",
      "Left_Elbow_Yaw": "Left_Elbow_Yaw",
      "Right_Shoulder_Pitch": "Right_Shoulder_Pitch",
      "Right_Shoulder_Roll": "Right_Shoulder_Roll",
      "Right_Elbow_Pitch": "Right_Elbow_Pitch",
      "Right_Elbow_Yaw": "Right_Elbow_Yaw",
      "Waist": "Waist",
      "Left_Hip_Pitch": "Left_Hip_Pitch",
      "Left_Hip_Roll": "Left_Hip_Roll",
      "Left_Hip_Yaw": "Left_Hip_Yaw",
      "Left_Knee_Pitch": "Left_Knee_Pitch",
      "Left_Ankle_Pitch": "Left_Ankle_Pitch",
      "Left_Ankle_Roll": "Left_Ankle_Roll",
      "Right_Hip_Pitch": "Right_Hip_Pitch",
      "Right_Hip_Roll": "Right_Hip_Roll",
      "Right_Hip_Yaw": "Right_Hip_Yaw",
      "Right_Knee_Pitch": "Right_Knee_Pitch",
      "Right_Ankle_Pitch": "Right_Ankle_Pitch",
      "Right_Ankle_Roll": "Right_Ankle_Roll"
    },
    "body_methods": {
      "Trunk": "name",
      "H1": "name",
      "H2": "name",
      "AL1": "name",
      "AL2": "name",
      "AL3": "name",
      "left_hand_link": "name",
      "AR1": "name",
      "AR2": "name",
      "AR3": "name",
      "right_hand_link": "name",
      "Waist": "name",
      "Hip_Pitch_Left": "name",
      "Hip_Roll_Left": "name",
      "Hip_Yaw_Left": "name",
      "Shank_Left": "name",
      "Ankle_Cross_Left": "name",
      "left_foot_link": "name",
      "Hip_Pitch_Right": "name",
      "Hip_Roll_Right": "name",
      "Hip_Yaw_Right": "name",
      "Shank_Right": "name",
      "Ankle_Cross_Right": "name",
      "right_foot_link": "name"
    },
    "joint_methods": {
      "AAHead_yaw": "name",
      "Head_pitch": "name",
      "Left_Shoulder_Pitch": "name",
      "Left_Shoulder_Roll": "name",
      "Left_Elbow_Pitch": "name",
      "Left_Elbow_Yaw": "name",
      "Right_Shoulder_Pitch": "name",
      "Right_Shoulder_Roll": "name",
      "Right_Elbow_Pitch": "name",
      "Right_Elbow_Yaw": "name",
      "Waist": "name",
      "Left_Hip_Pitch": "name",
      "Left_Hip_Roll": "name",
      "Left_Hip_Yaw": "name",
      "Left_Knee_Pitch": "name",
      "Left_Ankle_Pitch": "name",
      "Left_Ankle_Roll": "name",
      "Right_Hip_Pitch": "name",
      "Right_Hip_Roll": "name",
      "Right_Hip_Yaw": "name",
      "Right_Knee_Pitch": "name",
      "Right_Ankle_Pitch": "name",
      "Right_Ankle_Roll": "name"
    },
    "unmatched_m_bodies": [],
    "unmatched_upstream_bodies": [],
    "unmatched_m_joints": [],
    "unmatched_upstream_joints": [],
    "registration_anchor": {
      "M": "Trunk",
      "H": "Trunk",
      "root_unmatched": false
    }
  },
  "mapping_s": {
    "bodies": {
      "Trunk": "Trunk",
      "H1": "H1",
      "H2": "H2",
      "AL1": "AL1",
      "AL2": "AL2",
      "AL3": "AL3",
      "left_hand_link": "left_hand_link",
      "AR1": "AR1",
      "AR2": "AR2",
      "AR3": "AR3",
      "right_hand_link": "right_hand_link",
      "Waist": "Waist",
      "Hip_Pitch_Left": "Hip_Pitch_Left",
      "Hip_Roll_Left": "Hip_Roll_Left",
      "Hip_Yaw_Left": "Hip_Yaw_Left",
      "Shank_Left": "Shank_Left",
      "Ankle_Cross_Left": "Ankle_Cross_Left",
      "left_foot_link": "left_foot_link",
      "Hip_Pitch_Right": "Hip_Pitch_Right",
      "Hip_Roll_Right": "Hip_Roll_Right",
      "Hip_Yaw_Right": "Hip_Yaw_Right",
      "Shank_Right": "Shank_Right",
      "Ankle_Cross_Right": "Ankle_Cross_Right",
      "right_foot_link": "right_foot_link"
    },
    "joints": {
      "AAHead_yaw": "AAHead_yaw",
      "Head_pitch": "Head_pitch",
      "Left_Shoulder_Pitch": "Left_Shoulder_Pitch",
      "Left_Shoulder_Roll": "Left_Shoulder_Roll",
      "Left_Elbow_Pitch": "Left_Elbow_Pitch",
      "Left_Elbow_Yaw": "Left_Elbow_Yaw",
      "Right_Shoulder_Pitch": "Right_Shoulder_Pitch",
      "Right_Shoulder_Roll": "Right_Shoulder_Roll",
      "Right_Elbow_Pitch": "Right_Elbow_Pitch",
      "Right_Elbow_Yaw": "Right_Elbow_Yaw",
      "Waist": "Waist",
      "Left_Hip_Pitch": "Left_Hip_Pitch",
      "Left_Hip_Roll": "Left_Hip_Roll",
      "Left_Hip_Yaw": "Left_Hip_Yaw",
      "Left_Knee_Pitch": "Left_Knee_Pitch",
      "Left_Ankle_Pitch": "Left_Ankle_Pitch",
      "Left_Ankle_Roll": "Left_Ankle_Roll",
      "Right_Hip_Pitch": "Right_Hip_Pitch",
      "Right_Hip_Roll": "Right_Hip_Roll",
      "Right_Hip_Yaw": "Right_Hip_Yaw",
      "Right_Knee_Pitch": "Right_Knee_Pitch",
      "Right_Ankle_Pitch": "Right_Ankle_Pitch",
      "Right_Ankle_Roll": "Right_Ankle_Roll"
    },
    "body_methods": {
      "Trunk": "name",
      "H1": "name",
      "H2": "name",
      "AL1": "name",
      "AL2": "name",
      "AL3": "name",
      "left_hand_link": "name",
      "AR1": "name",
      "AR2": "name",
      "AR3": "name",
      "right_hand_link": "name",
      "Waist": "name",
      "Hip_Pitch_Left": "name",
      "Hip_Roll_Left": "name",
      "Hip_Yaw_Left": "name",
      "Shank_Left": "name",
      "Ankle_Cross_Left": "name",
      "left_foot_link": "name",
      "Hip_Pitch_Right": "name",
      "Hip_Roll_Right": "name",
      "Hip_Yaw_Right": "name",
      "Shank_Right": "name",
      "Ankle_Cross_Right": "name",
      "right_foot_link": "name"
    },
    "joint_methods": {
      "AAHead_yaw": "name",
      "Head_pitch": "name",
      "Left_Shoulder_Pitch": "name",
      "Left_Shoulder_Roll": "name",
      "Left_Elbow_Pitch": "name",
      "Left_Elbow_Yaw": "name",
      "Right_Shoulder_Pitch": "name",
      "Right_Shoulder_Roll": "name",
      "Right_Elbow_Pitch": "name",
      "Right_Elbow_Yaw": "name",
      "Waist": "name",
      "Left_Hip_Pitch": "name",
      "Left_Hip_Roll": "name",
      "Left_Hip_Yaw": "name",
      "Left_Knee_Pitch": "name",
      "Left_Ankle_Pitch": "name",
      "Left_Ankle_Roll": "name",
      "Right_Hip_Pitch": "name",
      "Right_Hip_Roll": "name",
      "Right_Hip_Yaw": "name",
      "Right_Knee_Pitch": "name",
      "Right_Ankle_Pitch": "name",
      "Right_Ankle_Roll": "name"
    },
    "unmatched_m_bodies": [],
    "unmatched_upstream_bodies": [],
    "unmatched_m_joints": [],
    "unmatched_upstream_joints": [],
    "registration_anchor": {
      "M": "Trunk",
      "S": "Trunk"
    }
  },
  "unavailable": [
    {
      "entity": "AAHead_yaw",
      "other_entity": "AAHead_yaw",
      "quantity": "force",
      "tolerance": "limit",
      "m": 7.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "AAHead_yaw",
      "other_entity": "AAHead_yaw",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 12.56,
      "s": 12.56,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "Head_pitch",
      "other_entity": "Head_pitch",
      "quantity": "force",
      "tolerance": "limit",
      "m": 7.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "Head_pitch",
      "other_entity": "Head_pitch",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 12.56,
      "s": 12.56,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "Left_Shoulder_Pitch",
      "other_entity": "Left_Shoulder_Pitch",
      "quantity": "force",
      "tolerance": "limit",
      "m": 18.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "Left_Shoulder_Pitch",
      "other_entity": "Left_Shoulder_Pitch",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 18.84,
      "s": 18.84,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "Left_Shoulder_Roll",
      "other_entity": "Left_Shoulder_Roll",
      "quantity": "force",
      "tolerance": "limit",
      "m": 18.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "Left_Shoulder_Roll",
      "other_entity": "Left_Shoulder_Roll",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 18.84,
      "s": 18.84,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "Left_Elbow_Pitch",
      "other_entity": "Left_Elbow_Pitch",
      "quantity": "force",
      "tolerance": "limit",
      "m": 18.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "Left_Elbow_Pitch",
      "other_entity": "Left_Elbow_Pitch",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 18.84,
      "s": 18.84,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "Left_Elbow_Yaw",
      "other_entity": "Left_Elbow_Yaw",
      "quantity": "force",
      "tolerance": "limit",
      "m": 18.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "Left_Elbow_Yaw",
      "other_entity": "Left_Elbow_Yaw",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 18.84,
      "s": 18.84,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "Right_Shoulder_Pitch",
      "other_entity": "Right_Shoulder_Pitch",
      "quantity": "force",
      "tolerance": "limit",
      "m": 18.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "Right_Shoulder_Pitch",
      "other_entity": "Right_Shoulder_Pitch",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 18.84,
      "s": 18.84,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "Right_Shoulder_Roll",
      "other_entity": "Right_Shoulder_Roll",
      "quantity": "force",
      "tolerance": "limit",
      "m": 18.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "Right_Shoulder_Roll",
      "other_entity": "Right_Shoulder_Roll",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 18.84,
      "s": 18.84,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "Right_Elbow_Pitch",
      "other_entity": "Right_Elbow_Pitch",
      "quantity": "force",
      "tolerance": "limit",
      "m": 18.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "Right_Elbow_Pitch",
      "other_entity": "Right_Elbow_Pitch",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 18.84,
      "s": 18.84,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "Right_Elbow_Yaw",
      "other_entity": "Right_Elbow_Yaw",
      "quantity": "force",
      "tolerance": "limit",
      "m": 18.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "Right_Elbow_Yaw",
      "other_entity": "Right_Elbow_Yaw",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 18.84,
      "s": 18.84,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "Waist",
      "other_entity": "Waist",
      "quantity": "force",
      "tolerance": "limit",
      "m": 30.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "Waist",
      "other_entity": "Waist",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 10.88,
      "s": 10.88,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "Left_Hip_Pitch",
      "other_entity": "Left_Hip_Pitch",
      "quantity": "force",
      "tolerance": "limit",
      "m": 45.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "Left_Hip_Pitch",
      "other_entity": "Left_Hip_Pitch",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 12.5,
      "s": 12.5,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "Left_Hip_Roll",
      "other_entity": "Left_Hip_Roll",
      "quantity": "force",
      "tolerance": "limit",
      "m": 30.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "Left_Hip_Roll",
      "other_entity": "Left_Hip_Roll",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 10.9,
      "s": 10.9,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "Left_Hip_Yaw",
      "other_entity": "Left_Hip_Yaw",
      "quantity": "force",
      "tolerance": "limit",
      "m": 30.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "Left_Hip_Yaw",
      "other_entity": "Left_Hip_Yaw",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 10.9,
      "s": 10.9,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "Left_Knee_Pitch",
      "other_entity": "Left_Knee_Pitch",
      "quantity": "force",
      "tolerance": "limit",
      "m": 60.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "Left_Knee_Pitch",
      "other_entity": "Left_Knee_Pitch",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 11.7,
      "s": 11.7,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "Left_Ankle_Pitch",
      "other_entity": "Left_Ankle_Pitch",
      "quantity": "force",
      "tolerance": "limit",
      "m": 20.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "Left_Ankle_Pitch",
      "other_entity": "Left_Ankle_Pitch",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 18.8,
      "s": 18.8,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "Left_Ankle_Roll",
      "other_entity": "Left_Ankle_Roll",
      "quantity": "force",
      "tolerance": "limit",
      "m": 15.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "Left_Ankle_Roll",
      "other_entity": "Left_Ankle_Roll",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 12.4,
      "s": 12.4,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "Right_Hip_Pitch",
      "other_entity": "Right_Hip_Pitch",
      "quantity": "force",
      "tolerance": "limit",
      "m": 45.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "Right_Hip_Pitch",
      "other_entity": "Right_Hip_Pitch",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 12.5,
      "s": 12.5,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "Right_Hip_Roll",
      "other_entity": "Right_Hip_Roll",
      "quantity": "force",
      "tolerance": "limit",
      "m": 30.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "Right_Hip_Roll",
      "other_entity": "Right_Hip_Roll",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 10.9,
      "s": 10.9,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "Right_Hip_Yaw",
      "other_entity": "Right_Hip_Yaw",
      "quantity": "force",
      "tolerance": "limit",
      "m": 30.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "Right_Hip_Yaw",
      "other_entity": "Right_Hip_Yaw",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 10.9,
      "s": 10.9,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "Right_Knee_Pitch",
      "other_entity": "Right_Knee_Pitch",
      "quantity": "force",
      "tolerance": "limit",
      "m": 60.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "Right_Knee_Pitch",
      "other_entity": "Right_Knee_Pitch",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 11.7,
      "s": 11.7,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "Right_Ankle_Pitch",
      "other_entity": "Right_Ankle_Pitch",
      "quantity": "force",
      "tolerance": "limit",
      "m": 20.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "Right_Ankle_Pitch",
      "other_entity": "Right_Ankle_Pitch",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 18.8,
      "s": 18.8,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "Right_Ankle_Roll",
      "other_entity": "Right_Ankle_Roll",
      "quantity": "force",
      "tolerance": "limit",
      "m": 15.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "Right_Ankle_Roll",
      "other_entity": "Right_Ankle_Roll",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 12.4,
      "s": 12.4,
      "reason": "quantity absent or not enforced/declared on one side"
    }
  ]
}
```

## Limits unavailable for a like-for-like simulator comparison

URDF effort and velocity tags are manufacturer declarations; MuJoCo ignores them. Missing enforced quantities are not interpreted as zero. The available values are shown for review and excluded from STALE counts.

| Joint / quantity | M | S | H / declared upstream |
|---|---|---|---|
| AAHead_yaw / force | 7 | unavailable | unavailable |
| AAHead_yaw / velocity | unavailable | 12.56 | 12.56 |
| Head_pitch / force | 7 | unavailable | unavailable |
| Head_pitch / velocity | unavailable | 12.56 | 12.56 |
| Left_Shoulder_Pitch / force | 18 | unavailable | unavailable |
| Left_Shoulder_Pitch / velocity | unavailable | 18.84 | 18.84 |
| Left_Shoulder_Roll / force | 18 | unavailable | unavailable |
| Left_Shoulder_Roll / velocity | unavailable | 18.84 | 18.84 |
| Left_Elbow_Pitch / force | 18 | unavailable | unavailable |
| Left_Elbow_Pitch / velocity | unavailable | 18.84 | 18.84 |
| Left_Elbow_Yaw / force | 18 | unavailable | unavailable |
| Left_Elbow_Yaw / velocity | unavailable | 18.84 | 18.84 |
| Right_Shoulder_Pitch / force | 18 | unavailable | unavailable |
| Right_Shoulder_Pitch / velocity | unavailable | 18.84 | 18.84 |
| Right_Shoulder_Roll / force | 18 | unavailable | unavailable |
| Right_Shoulder_Roll / velocity | unavailable | 18.84 | 18.84 |
| Right_Elbow_Pitch / force | 18 | unavailable | unavailable |
| Right_Elbow_Pitch / velocity | unavailable | 18.84 | 18.84 |
| Right_Elbow_Yaw / force | 18 | unavailable | unavailable |
| Right_Elbow_Yaw / velocity | unavailable | 18.84 | 18.84 |
| Waist / force | 30 | unavailable | unavailable |
| Waist / velocity | unavailable | 10.88 | 10.88 |
| Left_Hip_Pitch / force | 45 | unavailable | unavailable |
| Left_Hip_Pitch / velocity | unavailable | 12.5 | 12.5 |
| Left_Hip_Roll / force | 30 | unavailable | unavailable |
| Left_Hip_Roll / velocity | unavailable | 10.9 | 10.9 |
| Left_Hip_Yaw / force | 30 | unavailable | unavailable |
| Left_Hip_Yaw / velocity | unavailable | 10.9 | 10.9 |
| Left_Knee_Pitch / force | 60 | unavailable | unavailable |
| Left_Knee_Pitch / velocity | unavailable | 11.7 | 11.7 |
| Left_Ankle_Pitch / force | 20 | unavailable | unavailable |
| Left_Ankle_Pitch / velocity | unavailable | 18.8 | 18.8 |
| Left_Ankle_Roll / force | 15 | unavailable | unavailable |
| Left_Ankle_Roll / velocity | unavailable | 12.4 | 12.4 |
| Right_Hip_Pitch / force | 45 | unavailable | unavailable |
| Right_Hip_Pitch / velocity | unavailable | 12.5 | 12.5 |
| Right_Hip_Roll / force | 30 | unavailable | unavailable |
| Right_Hip_Roll / velocity | unavailable | 10.9 | 10.9 |
| Right_Hip_Yaw / force | 30 | unavailable | unavailable |
| Right_Hip_Yaw / velocity | unavailable | 10.9 | 10.9 |
| Right_Knee_Pitch / force | 60 | unavailable | unavailable |
| Right_Knee_Pitch / velocity | unavailable | 11.7 | 11.7 |
| Right_Ankle_Pitch / force | 20 | unavailable | unavailable |
| Right_Ankle_Pitch / velocity | unavailable | 18.8 | 18.8 |
| Right_Ankle_Roll / force | 15 | unavailable | unavailable |
| Right_Ankle_Roll / velocity | unavailable | 12.4 | 12.4 |
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
    "file": "booster_t1/t1.xml",
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
        0.7
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
  "self_variants_recompiled": 1,
  "historical_snapshots_reused": 2,
  "primary_physics_unchanged": true,
  "source_matching": "original raw-value provenance criteria retained; kinematic guard applies to reported CoM"
}
```
