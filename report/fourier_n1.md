# fourier_n1

Status: **complete**. Provenance: **dated match**, confidence **medium**.

Source selected using the ordered amended provenance rules.

M: `https://github.com/google-deepmind/mujoco_menagerie`, `fourier_n1/n1.xml`, commit `370c43965323c0944b433b202aac5058b5f907a9`.
H: `https://github.com/FFTAI/wiki-grx-mjcf`, `models/N1/urdf/N1_raw.urdf`, commit `3079af890e8db4d243e5729abfa9860ecf7487f6`.
S: `f29a87905bdcfc32fdac9c5342644630fd27156a` (2025-05-03T10:48:03+08:00). Menagerie release/change: 2025-05-04T23:15:32+08:00.

Limit semantics: MJCF effort values are supported actuator torque/force envelopes. URDF effort and velocity values are manufacturer declarations retained from XML; MuJoCo does not enforce those tags. Such declaration comparisons are explicitly distinct from compiled inertial/range quantities.


## Source evidence

```json
[
  {
    "url": "https://github.com/FFTAI/Wiki-GRx-Models",
    "document": "fourier_n1/README.md",
    "commit": "370c43965323c0944b433b202aac5058b5f907a9",
    "current": true
  },
  {
    "url": "https://github.com/FFTAI/wiki-grx-mjcf",
    "document": "fourier_n1/README.md",
    "commit": "370c43965323c0944b433b202aac5058b5f907a9",
    "current": true
  }
]
```


## Kinematics consistency

A proper Kabsch rigid transform aligns all matched zero-pose body origins. The maximum per-origin residual and signed hinge/slide axis angles determine whether CoM can be compared; RMS is also recorded. Fewer than three non-collinear origins give insufficient kinematic coverage. CoM records that fail either required M/H or M/S check are excluded from counts and largest discrepancies. Masses, principal moments and raw joint ranges remain unchanged; a flagged range still requires convention review.

| Pair | Status | Origins / rank | RMS / maximum mm | Disagreeing / checked axes |
|---|---|---:|---:|---:|
| M/H | consistent | 29 / 3 | 4.12332845e-05 / 7.78850409e-05 | 0 / 23 |
| M/S | consistent | 29 / 3 | 4.12332845e-05 / 7.78850409e-05 | 0 / 23 |

Exact fitted transforms, per-origin residuals, thresholds and axis vectors:

```json
{
  "M/H": {
    "status": "consistent",
    "matched_body_origins": 29,
    "position_threshold_m": 0.005,
    "axis_threshold_rad": 0.005,
    "residual_definition": "maximum Euclidean residual over matched body origins; Kabsch minimizes RMS, which is also recorded",
    "coordinate_frames": "each snapshot registered to its matched report anchor",
    "anchor_m": "base_link",
    "anchor_other": "base_link",
    "rotation_other_to_m": [
      [
        1.0000000000000002,
        -6.361523519442237e-11,
        -1.2048244828663856e-08
      ],
      [
        6.361542354861469e-11,
        0.9999999999999999,
        -5.7632180409432784e-11
      ],
      [
        1.2048244873996694e-08,
        5.7631670938554e-11,
        1.0000000000000004
      ]
    ],
    "translation_other_to_m": [
      -5.896484099598975e-10,
      -4.317084125078641e-12,
      3.640401844556829e-08
    ],
    "rms_residual_m": 4.1233284539925417e-08,
    "max_residual_m": 7.788504093567402e-08,
    "fit_rank": 3,
    "axis_checks": [
      {
        "joint_m": "left_hip_pitch_joint",
        "joint_other": "left_hip_pitch_joint",
        "axis_m": [
          0.0,
          0.9659259343044767,
          -0.2588186419831924
        ],
        "axis_other_aligned": [
          3.0568747577921058e-09,
          0.9659256678545639,
          -0.2588196363874169
        ],
        "angle_rad": 1.0294875726344576e-06,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "left_hip_roll_joint",
        "joint_other": "left_hip_roll_joint",
        "axis_m": [
          1.0,
          0.0,
          0.0
        ],
        "axis_other_aligned": [
          1.0,
          6.361542354861468e-11,
          1.204824487399669e-08
        ],
        "angle_rad": 1.204841281936757e-08,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "left_hip_yaw_joint",
        "joint_other": "left_hip_yaw_joint",
        "axis_m": [
          0.0,
          2.319286438979564e-17,
          1.0
        ],
        "axis_other_aligned": [
          -1.2048244828663851e-08,
          -5.763216507363269e-11,
          1.0
        ],
        "angle_rad": 1.2048382668248448e-08,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "left_knee_pitch_joint",
        "joint_other": "left_knee_pitch_joint",
        "axis_m": [
          0.0,
          1.0,
          -2.319286438979564e-17
        ],
        "axis_other_aligned": [
          -6.36152351944222e-11,
          1.0,
          5.763165560275394e-11
        ],
        "angle_rad": 8.583885221531667e-11,
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
          0.0
        ],
        "axis_other_aligned": [
          1.0,
          6.361542354861468e-11,
          1.204824487399669e-08
        ],
        "angle_rad": 1.204841281936757e-08,
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
          -2.319286438979564e-17
        ],
        "axis_other_aligned": [
          -6.36152351944222e-11,
          1.0,
          5.763165560275394e-11
        ],
        "angle_rad": 8.583885221531667e-11,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "right_hip_pitch_joint",
        "joint_other": "right_hip_pitch_joint",
        "axis_m": [
          0.0,
          0.9659259343044767,
          0.2588186419831924
        ],
        "axis_other_aligned": [
          -3.179769934872004e-09,
          0.9659256678247315,
          0.2588196364987528
        ],
        "angle_rad": 1.0296032077445987e-06,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "right_hip_roll_joint",
        "joint_other": "right_hip_roll_joint",
        "axis_m": [
          1.0,
          0.0,
          0.0
        ],
        "axis_other_aligned": [
          1.0,
          6.361542354861468e-11,
          1.204824487399669e-08
        ],
        "angle_rad": 1.204841281936757e-08,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "right_hip_yaw_joint",
        "joint_other": "right_hip_yaw_joint",
        "axis_m": [
          0.0,
          -2.319286438979564e-17,
          1.0
        ],
        "axis_other_aligned": [
          -1.2048244828663851e-08,
          -5.7632195745232824e-11,
          1.0
        ],
        "angle_rad": 1.2048382668173282e-08,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "right_knee_pitch_joint",
        "joint_other": "right_knee_pitch_joint",
        "axis_m": [
          0.0,
          1.0,
          2.319286438979564e-17
        ],
        "axis_other_aligned": [
          -6.361523519442256e-11,
          1.0,
          5.763168627435407e-11
        ],
        "angle_rad": 8.583884166494817e-11,
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
          0.0
        ],
        "axis_other_aligned": [
          1.0,
          6.361542354861468e-11,
          1.204824487399669e-08
        ],
        "angle_rad": 1.204841281936757e-08,
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
          2.319286438979564e-17
        ],
        "axis_other_aligned": [
          -6.361523519442256e-11,
          1.0,
          5.763168627435407e-11
        ],
        "angle_rad": 8.583884166494817e-11,
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
          -1.2048244828663851e-08,
          -5.763218040943276e-11,
          1.0
        ],
        "angle_rad": 1.2048382668210866e-08,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "left_shoulder_pitch_joint",
        "joint_other": "left_shoulder_pitch_joint",
        "axis_m": [
          0.0,
          1.0,
          0.0
        ],
        "axis_other_aligned": [
          -6.361523519442238e-11,
          1.0,
          5.763167093855401e-11
        ],
        "angle_rad": 8.583884694013223e-11,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "left_shoulder_roll_joint",
        "joint_other": "left_shoulder_roll_joint",
        "axis_m": [
          1.0,
          0.0,
          0.0
        ],
        "axis_other_aligned": [
          1.0,
          6.361542354861468e-11,
          1.204824487399669e-08
        ],
        "angle_rad": 1.204841281936757e-08,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "left_shoulder_yaw_joint",
        "joint_other": "left_shoulder_yaw_joint",
        "axis_m": [
          0.0,
          0.0,
          1.0
        ],
        "axis_other_aligned": [
          -1.2048244828663851e-08,
          -5.763218040943276e-11,
          1.0
        ],
        "angle_rad": 1.2048382668210866e-08,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "left_elbow_pitch_joint",
        "joint_other": "left_elbow_pitch_joint",
        "axis_m": [
          0.0,
          1.0,
          0.0
        ],
        "axis_other_aligned": [
          -6.361523519442238e-11,
          1.0,
          5.763167093855401e-11
        ],
        "angle_rad": 8.583884694013223e-11,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "left_wrist_yaw_joint",
        "joint_other": "left_wrist_yaw_joint",
        "axis_m": [
          -0.9999999999910001,
          0.0,
          -4.242642374308048e-06
        ],
        "axis_other_aligned": [
          -0.9999999999932094,
          -6.361521185336632e-11,
          -3.685253348067938e-06
        ],
        "angle_rad": 5.573890298747204e-07,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "right_shoulder_pitch_joint",
        "joint_other": "right_shoulder_pitch_joint",
        "axis_m": [
          0.0,
          1.0,
          0.0
        ],
        "axis_other_aligned": [
          -6.361523519442238e-11,
          1.0,
          5.763167093855401e-11
        ],
        "angle_rad": 8.583884694013223e-11,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "right_shoulder_roll_joint",
        "joint_other": "right_shoulder_roll_joint",
        "axis_m": [
          1.0,
          0.0,
          0.0
        ],
        "axis_other_aligned": [
          1.0,
          6.361542354861468e-11,
          1.204824487399669e-08
        ],
        "angle_rad": 1.204841281936757e-08,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "right_shoulder_yaw_joint",
        "joint_other": "right_shoulder_yaw_joint",
        "axis_m": [
          0.0,
          0.0,
          1.0
        ],
        "axis_other_aligned": [
          -1.2048244828663851e-08,
          -5.763218040943276e-11,
          1.0
        ],
        "angle_rad": 1.2048382668210866e-08,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "right_elbow_pitch_joint",
        "joint_other": "right_elbow_pitch_joint",
        "axis_m": [
          0.0,
          1.0,
          0.0
        ],
        "axis_other_aligned": [
          -6.361523519442238e-11,
          1.0,
          5.763167093855401e-11
        ],
        "angle_rad": 8.583884694013223e-11,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "right_wrist_yaw_joint",
        "joint_other": "right_wrist_yaw_joint",
        "axis_m": [
          -0.9999999999910001,
          0.0,
          -4.242642374308048e-06
        ],
        "axis_other_aligned": [
          -0.9999999999932094,
          -6.361521185336632e-11,
          -3.685253348067938e-06
        ],
        "angle_rad": 5.573890298747204e-07,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      }
    ],
    "axis_disagreements": [],
    "com_eligible": true,
    "covariance_singular_values": [
      2.760934277074553,
      0.47671012746008173,
      0.08852967911523676
    ],
    "origin_residuals_m": {
      "base_link": 3.640879375741333e-08,
      "left_thigh_pitch_link": 3.640758341836292e-08,
      "left_thigh_roll_link": 4.008240110485252e-08,
      "left_thigh_yaw_link": 4.010292686027088e-08,
      "left_shank_pitch_link": 4.026338576015246e-08,
      "left_foot_roll_link": 4.07229199512254e-08,
      "left_foot_pitch_link": 4.07229199512254e-08,
      "right_thigh_pitch_link": 3.640180729206082e-08,
      "right_thigh_roll_link": 4.009532681516808e-08,
      "right_thigh_yaw_link": 4.012071211300692e-08,
      "right_shank_pitch_link": 4.0293437464371876e-08,
      "right_foot_roll_link": 4.0769087142328856e-08,
      "right_foot_pitch_link": 4.0769087142328856e-08,
      "imu_link": 3.6423262899752124e-08,
      "waist_yaw_link": 3.641509509135339e-08,
      "torso_link": 3.662621389066108e-08,
      "camera_link": 3.777420839472369e-08,
      "left_upper_arm_pitch_link": 3.663249115676461e-08,
      "left_upper_arm_roll_link": 3.6637505793672225e-08,
      "left_upper_arm_yaw_link": 3.6523835956499773e-08,
      "left_lower_arm_pitch_link": 3.644540649954746e-08,
      "left_hand_yaw_link": 1.9661451329680878e-08,
      "left_end_effector_link": 7.786522843240649e-08,
      "right_upper_arm_pitch_link": 3.661993752236094e-08,
      "right_upper_arm_roll_link": 3.661492471404837e-08,
      "right_upper_arm_yaw_link": 3.650192589686457e-08,
      "right_lower_arm_pitch_link": 3.642425871407712e-08,
      "right_hand_yaw_link": 1.967993680714347e-08,
      "right_end_effector_link": 7.788504093567402e-08
    },
    "reason": "Unique proper rigid fit and matched signed axes meet the configured thresholds"
  },
  "M/S": {
    "status": "consistent",
    "matched_body_origins": 29,
    "position_threshold_m": 0.005,
    "axis_threshold_rad": 0.005,
    "residual_definition": "maximum Euclidean residual over matched body origins; Kabsch minimizes RMS, which is also recorded",
    "coordinate_frames": "each snapshot registered to its matched report anchor",
    "anchor_m": "base_link",
    "anchor_other": "base_link",
    "rotation_other_to_m": [
      [
        1.0000000000000002,
        -6.361523519442237e-11,
        -1.2048244828663856e-08
      ],
      [
        6.361542354861469e-11,
        0.9999999999999999,
        -5.7632180409432784e-11
      ],
      [
        1.2048244873996694e-08,
        5.7631670938554e-11,
        1.0000000000000004
      ]
    ],
    "translation_other_to_m": [
      -5.896484099598975e-10,
      -4.317084125078641e-12,
      3.640401844556829e-08
    ],
    "rms_residual_m": 4.1233284539925417e-08,
    "max_residual_m": 7.788504093567402e-08,
    "fit_rank": 3,
    "axis_checks": [
      {
        "joint_m": "left_hip_pitch_joint",
        "joint_other": "left_hip_pitch_joint",
        "axis_m": [
          0.0,
          0.9659259343044767,
          -0.2588186419831924
        ],
        "axis_other_aligned": [
          3.0568747577921058e-09,
          0.9659256678545639,
          -0.2588196363874169
        ],
        "angle_rad": 1.0294875726344576e-06,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "left_hip_roll_joint",
        "joint_other": "left_hip_roll_joint",
        "axis_m": [
          1.0,
          0.0,
          0.0
        ],
        "axis_other_aligned": [
          1.0,
          6.361542354861468e-11,
          1.204824487399669e-08
        ],
        "angle_rad": 1.204841281936757e-08,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "left_hip_yaw_joint",
        "joint_other": "left_hip_yaw_joint",
        "axis_m": [
          0.0,
          2.319286438979564e-17,
          1.0
        ],
        "axis_other_aligned": [
          -1.2048244828663851e-08,
          -5.763216507363269e-11,
          1.0
        ],
        "angle_rad": 1.2048382668248448e-08,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "left_knee_pitch_joint",
        "joint_other": "left_knee_pitch_joint",
        "axis_m": [
          0.0,
          1.0,
          -2.319286438979564e-17
        ],
        "axis_other_aligned": [
          -6.36152351944222e-11,
          1.0,
          5.763165560275394e-11
        ],
        "angle_rad": 8.583885221531667e-11,
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
          0.0
        ],
        "axis_other_aligned": [
          1.0,
          6.361542354861468e-11,
          1.204824487399669e-08
        ],
        "angle_rad": 1.204841281936757e-08,
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
          -2.319286438979564e-17
        ],
        "axis_other_aligned": [
          -6.36152351944222e-11,
          1.0,
          5.763165560275394e-11
        ],
        "angle_rad": 8.583885221531667e-11,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "right_hip_pitch_joint",
        "joint_other": "right_hip_pitch_joint",
        "axis_m": [
          0.0,
          0.9659259343044767,
          0.2588186419831924
        ],
        "axis_other_aligned": [
          -3.179769934872004e-09,
          0.9659256678247315,
          0.2588196364987528
        ],
        "angle_rad": 1.0296032077445987e-06,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "right_hip_roll_joint",
        "joint_other": "right_hip_roll_joint",
        "axis_m": [
          1.0,
          0.0,
          0.0
        ],
        "axis_other_aligned": [
          1.0,
          6.361542354861468e-11,
          1.204824487399669e-08
        ],
        "angle_rad": 1.204841281936757e-08,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "right_hip_yaw_joint",
        "joint_other": "right_hip_yaw_joint",
        "axis_m": [
          0.0,
          -2.319286438979564e-17,
          1.0
        ],
        "axis_other_aligned": [
          -1.2048244828663851e-08,
          -5.7632195745232824e-11,
          1.0
        ],
        "angle_rad": 1.2048382668173282e-08,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "right_knee_pitch_joint",
        "joint_other": "right_knee_pitch_joint",
        "axis_m": [
          0.0,
          1.0,
          2.319286438979564e-17
        ],
        "axis_other_aligned": [
          -6.361523519442256e-11,
          1.0,
          5.763168627435407e-11
        ],
        "angle_rad": 8.583884166494817e-11,
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
          0.0
        ],
        "axis_other_aligned": [
          1.0,
          6.361542354861468e-11,
          1.204824487399669e-08
        ],
        "angle_rad": 1.204841281936757e-08,
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
          2.319286438979564e-17
        ],
        "axis_other_aligned": [
          -6.361523519442256e-11,
          1.0,
          5.763168627435407e-11
        ],
        "angle_rad": 8.583884166494817e-11,
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
          -1.2048244828663851e-08,
          -5.763218040943276e-11,
          1.0
        ],
        "angle_rad": 1.2048382668210866e-08,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "left_shoulder_pitch_joint",
        "joint_other": "left_shoulder_pitch_joint",
        "axis_m": [
          0.0,
          1.0,
          0.0
        ],
        "axis_other_aligned": [
          -6.361523519442238e-11,
          1.0,
          5.763167093855401e-11
        ],
        "angle_rad": 8.583884694013223e-11,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "left_shoulder_roll_joint",
        "joint_other": "left_shoulder_roll_joint",
        "axis_m": [
          1.0,
          0.0,
          0.0
        ],
        "axis_other_aligned": [
          1.0,
          6.361542354861468e-11,
          1.204824487399669e-08
        ],
        "angle_rad": 1.204841281936757e-08,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "left_shoulder_yaw_joint",
        "joint_other": "left_shoulder_yaw_joint",
        "axis_m": [
          0.0,
          0.0,
          1.0
        ],
        "axis_other_aligned": [
          -1.2048244828663851e-08,
          -5.763218040943276e-11,
          1.0
        ],
        "angle_rad": 1.2048382668210866e-08,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "left_elbow_pitch_joint",
        "joint_other": "left_elbow_pitch_joint",
        "axis_m": [
          0.0,
          1.0,
          0.0
        ],
        "axis_other_aligned": [
          -6.361523519442238e-11,
          1.0,
          5.763167093855401e-11
        ],
        "angle_rad": 8.583884694013223e-11,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "left_wrist_yaw_joint",
        "joint_other": "left_wrist_yaw_joint",
        "axis_m": [
          -0.9999999999910001,
          0.0,
          -4.242642374308048e-06
        ],
        "axis_other_aligned": [
          -0.9999999999932094,
          -6.361521185336632e-11,
          -3.685253348067938e-06
        ],
        "angle_rad": 5.573890298747204e-07,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "right_shoulder_pitch_joint",
        "joint_other": "right_shoulder_pitch_joint",
        "axis_m": [
          0.0,
          1.0,
          0.0
        ],
        "axis_other_aligned": [
          -6.361523519442238e-11,
          1.0,
          5.763167093855401e-11
        ],
        "angle_rad": 8.583884694013223e-11,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "right_shoulder_roll_joint",
        "joint_other": "right_shoulder_roll_joint",
        "axis_m": [
          1.0,
          0.0,
          0.0
        ],
        "axis_other_aligned": [
          1.0,
          6.361542354861468e-11,
          1.204824487399669e-08
        ],
        "angle_rad": 1.204841281936757e-08,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "right_shoulder_yaw_joint",
        "joint_other": "right_shoulder_yaw_joint",
        "axis_m": [
          0.0,
          0.0,
          1.0
        ],
        "axis_other_aligned": [
          -1.2048244828663851e-08,
          -5.763218040943276e-11,
          1.0
        ],
        "angle_rad": 1.2048382668210866e-08,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "right_elbow_pitch_joint",
        "joint_other": "right_elbow_pitch_joint",
        "axis_m": [
          0.0,
          1.0,
          0.0
        ],
        "axis_other_aligned": [
          -6.361523519442238e-11,
          1.0,
          5.763167093855401e-11
        ],
        "angle_rad": 8.583884694013223e-11,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "right_wrist_yaw_joint",
        "joint_other": "right_wrist_yaw_joint",
        "axis_m": [
          -0.9999999999910001,
          0.0,
          -4.242642374308048e-06
        ],
        "axis_other_aligned": [
          -0.9999999999932094,
          -6.361521185336632e-11,
          -3.685253348067938e-06
        ],
        "angle_rad": 5.573890298747204e-07,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      }
    ],
    "axis_disagreements": [],
    "com_eligible": true,
    "covariance_singular_values": [
      2.760934277074553,
      0.47671012746008173,
      0.08852967911523676
    ],
    "origin_residuals_m": {
      "base_link": 3.640879375741333e-08,
      "left_thigh_pitch_link": 3.640758341836292e-08,
      "left_thigh_roll_link": 4.008240110485252e-08,
      "left_thigh_yaw_link": 4.010292686027088e-08,
      "left_shank_pitch_link": 4.026338576015246e-08,
      "left_foot_roll_link": 4.07229199512254e-08,
      "left_foot_pitch_link": 4.07229199512254e-08,
      "right_thigh_pitch_link": 3.640180729206082e-08,
      "right_thigh_roll_link": 4.009532681516808e-08,
      "right_thigh_yaw_link": 4.012071211300692e-08,
      "right_shank_pitch_link": 4.0293437464371876e-08,
      "right_foot_roll_link": 4.0769087142328856e-08,
      "right_foot_pitch_link": 4.0769087142328856e-08,
      "imu_link": 3.6423262899752124e-08,
      "waist_yaw_link": 3.641509509135339e-08,
      "torso_link": 3.662621389066108e-08,
      "camera_link": 3.777420839472369e-08,
      "left_upper_arm_pitch_link": 3.663249115676461e-08,
      "left_upper_arm_roll_link": 3.6637505793672225e-08,
      "left_upper_arm_yaw_link": 3.6523835956499773e-08,
      "left_lower_arm_pitch_link": 3.644540649954746e-08,
      "left_hand_yaw_link": 1.9661451329680878e-08,
      "left_end_effector_link": 7.786522843240649e-08,
      "right_upper_arm_pitch_link": 3.661993752236094e-08,
      "right_upper_arm_roll_link": 3.661492471404837e-08,
      "right_upper_arm_yaw_link": 3.650192589686457e-08,
      "right_lower_arm_pitch_link": 3.642425871407712e-08,
      "right_hand_yaw_link": 1.967993680714347e-08,
      "right_end_effector_link": 7.788504093567402e-08
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
| robot / total_com_registered | [0.00697329859, 4.3907579e-05, -0.0597202979] | [0.00697329857, 4.39075793e-05, -0.0597203304] | [0.00697329857, 4.39075793e-05, -0.0597203304] | [-1.71139231e-11, 3.42979463e-13, -3.25426293e-08] | eligible; compared after Kabsch alignment | [aggregate inputs](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/fourier_n1/n1.xml#L1) | [aggregate inputs](https://github.com/FFTAI/wiki-grx-mjcf/blob/f29a87905bdcfc32fdac9c5342644630fd27156a/models/N1/urdf/N1_raw.urdf#L1) | [aggregate inputs](https://github.com/FFTAI/wiki-grx-mjcf/blob/3079af890e8db4d243e5729abfa9860ecf7487f6/models/N1/urdf/N1_raw.urdf#L1) |
| base_link / com_registered | [0.00025493, 1.049e-05, -0.05502] | [0.00025493, 1.049e-05, -0.05502] | [0.00025493, 1.049e-05, -0.05502] | [0, 0, -4.16333634e-17] | eligible; compared after Kabsch alignment | [CoM/kinematic input L82](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/fourier_n1/n1.xml#L82) | [CoM/kinematic input L12](https://github.com/FFTAI/wiki-grx-mjcf/blob/f29a87905bdcfc32fdac9c5342644630fd27156a/models/N1/urdf/N1_raw.urdf#L12) | [CoM/kinematic input L12](https://github.com/FFTAI/wiki-grx-mjcf/blob/3079af890e8db4d243e5729abfa9860ecf7487f6/models/N1/urdf/N1_raw.urdf#L12) |
| left_thigh_pitch_link / com_registered | [-0.017114, 0.0848225507, -0.0763116492] | [-0.017114, 0.0848225415, -0.0763116845] | [-0.017114, 0.0848225415, -0.0763116845] | [0, -9.21095736e-09, -3.53848454e-08] | eligible; compared after Kabsch alignment | [CoM/kinematic input L88](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/fourier_n1/n1.xml#L88) | [CoM/kinematic input L51](https://github.com/FFTAI/wiki-grx-mjcf/blob/f29a87905bdcfc32fdac9c5342644630fd27156a/models/N1/urdf/N1_raw.urdf#L51) | [CoM/kinematic input L51](https://github.com/FFTAI/wiki-grx-mjcf/blob/3079af890e8db4d243e5729abfa9860ecf7487f6/models/N1/urdf/N1_raw.urdf#L51) |
| left_thigh_roll_link / com_registered | [-0.0029103, 0.119994747, -0.106022942] | [-0.0029103, 0.119994728, -0.106023014] | [-0.0029103, 0.119994728, -0.106023014] | [0, -1.91854677e-08, -7.16011122e-08] | eligible; compared after Kabsch alignment | [CoM/kinematic input L93](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/fourier_n1/n1.xml#L93) | [CoM/kinematic input L109](https://github.com/FFTAI/wiki-grx-mjcf/blob/f29a87905bdcfc32fdac9c5342644630fd27156a/models/N1/urdf/N1_raw.urdf#L109) | [CoM/kinematic input L109](https://github.com/FFTAI/wiki-grx-mjcf/blob/3079af890e8db4d243e5729abfa9860ecf7487f6/models/N1/urdf/N1_raw.urdf#L109) |
| left_thigh_yaw_link / com_registered | [0.0021441, 0.109391667, -0.254115942] | [0.0021441, 0.109391648, -0.254116014] | [0.0021441, 0.109391648, -0.254116014] | [0, -1.91854677e-08, -7.16011123e-08] | eligible; compared after Kabsch alignment | [CoM/kinematic input L99](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/fourier_n1/n1.xml#L99) | [CoM/kinematic input L166](https://github.com/FFTAI/wiki-grx-mjcf/blob/f29a87905bdcfc32fdac9c5342644630fd27156a/models/N1/urdf/N1_raw.urdf#L166) | [CoM/kinematic input L166](https://github.com/FFTAI/wiki-grx-mjcf/blob/3079af890e8db4d243e5729abfa9860ecf7487f6/models/N1/urdf/N1_raw.urdf#L166) |
| left_shank_pitch_link / com_registered | [0.0027736, 0.124996067, -0.510469942] | [0.0027736, 0.124996048, -0.510470014] | [0.0027736, 0.124996048, -0.510470014] | [0, -1.91854677e-08, -7.16011123e-08] | eligible; compared after Kabsch alignment | [CoM/kinematic input L105](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/fourier_n1/n1.xml#L105) | [CoM/kinematic input L223](https://github.com/FFTAI/wiki-grx-mjcf/blob/f29a87905bdcfc32fdac9c5342644630fd27156a/models/N1/urdf/N1_raw.urdf#L223) | [CoM/kinematic input L223](https://github.com/FFTAI/wiki-grx-mjcf/blob/3079af890e8db4d243e5729abfa9860ecf7487f6/models/N1/urdf/N1_raw.urdf#L223) |
| left_foot_roll_link / com_registered | [0, 0.121862167, -0.654999942] | [0, 0.121862148, -0.655000014] | [0, 0.121862148, -0.655000014] | [0, -1.91854677e-08, -7.16011124e-08] | eligible; compared after Kabsch alignment | [CoM/kinematic input L111](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/fourier_n1/n1.xml#L111) | [CoM/kinematic input L280](https://github.com/FFTAI/wiki-grx-mjcf/blob/f29a87905bdcfc32fdac9c5342644630fd27156a/models/N1/urdf/N1_raw.urdf#L280) | [CoM/kinematic input L280](https://github.com/FFTAI/wiki-grx-mjcf/blob/3079af890e8db4d243e5729abfa9860ecf7487f6/models/N1/urdf/N1_raw.urdf#L280) |
| left_foot_pitch_link / com_registered | [0.031083, 0.119889337, -0.686858942] | [0.031083, 0.119889318, -0.686859014] | [0.031083, 0.119889318, -0.686859014] | [0, -1.91854677e-08, -7.16011123e-08] | eligible; compared after Kabsch alignment | [CoM/kinematic input L116](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/fourier_n1/n1.xml#L116) | [CoM/kinematic input L338](https://github.com/FFTAI/wiki-grx-mjcf/blob/f29a87905bdcfc32fdac9c5342644630fd27156a/models/N1/urdf/N1_raw.urdf#L338) | [CoM/kinematic input L338](https://github.com/FFTAI/wiki-grx-mjcf/blob/3079af890e8db4d243e5729abfa9860ecf7487f6/models/N1/urdf/N1_raw.urdf#L338) |
| right_thigh_pitch_link / com_registered | [-0.017114, -0.0848234183, -0.076312275] | [-0.017114, -0.0848234091, -0.0763123104] | [-0.017114, -0.0848234091, -0.0763123104] | [0, 9.21160172e-09, -3.53857386e-08] | eligible; compared after Kabsch alignment | [CoM/kinematic input L130](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/fourier_n1/n1.xml#L130) | [CoM/kinematic input L396](https://github.com/FFTAI/wiki-grx-mjcf/blob/f29a87905bdcfc32fdac9c5342644630fd27156a/models/N1/urdf/N1_raw.urdf#L396) | [CoM/kinematic input L396](https://github.com/FFTAI/wiki-grx-mjcf/blob/3079af890e8db4d243e5729abfa9860ecf7487f6/models/N1/urdf/N1_raw.urdf#L396) |
| right_thigh_roll_link / com_registered | [-0.0029092, -0.119987587, -0.106022942] | [-0.0029092, -0.119987568, -0.106023014] | [-0.0029092, -0.119987568, -0.106023014] | [0, 1.91854677e-08, -7.16011122e-08] | eligible; compared after Kabsch alignment | [CoM/kinematic input L135](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/fourier_n1/n1.xml#L135) | [CoM/kinematic input L454](https://github.com/FFTAI/wiki-grx-mjcf/blob/f29a87905bdcfc32fdac9c5342644630fd27156a/models/N1/urdf/N1_raw.urdf#L454) | [CoM/kinematic input L454](https://github.com/FFTAI/wiki-grx-mjcf/blob/3079af890e8db4d243e5729abfa9860ecf7487f6/models/N1/urdf/N1_raw.urdf#L454) |
| right_thigh_yaw_link / com_registered | [0.002043, -0.109916667, -0.254121942] | [0.002043, -0.109916648, -0.254122014] | [0.002043, -0.109916648, -0.254122014] | [0, 1.91854677e-08, -7.16011123e-08] | eligible; compared after Kabsch alignment | [CoM/kinematic input L141](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/fourier_n1/n1.xml#L141) | [CoM/kinematic input L511](https://github.com/FFTAI/wiki-grx-mjcf/blob/f29a87905bdcfc32fdac9c5342644630fd27156a/models/N1/urdf/N1_raw.urdf#L511) | [CoM/kinematic input L511](https://github.com/FFTAI/wiki-grx-mjcf/blob/3079af890e8db4d243e5729abfa9860ecf7487f6/models/N1/urdf/N1_raw.urdf#L511) |
| right_shank_pitch_link / com_registered | [0.0026916, -0.124783667, -0.510929942] | [0.0026916, -0.124783648, -0.510930014] | [0.0026916, -0.124783648, -0.510930014] | [0, 1.91854677e-08, -7.16011123e-08] | eligible; compared after Kabsch alignment | [CoM/kinematic input L147](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/fourier_n1/n1.xml#L147) | [CoM/kinematic input L568](https://github.com/FFTAI/wiki-grx-mjcf/blob/f29a87905bdcfc32fdac9c5342644630fd27156a/models/N1/urdf/N1_raw.urdf#L568) | [CoM/kinematic input L568](https://github.com/FFTAI/wiki-grx-mjcf/blob/3079af890e8db4d243e5729abfa9860ecf7487f6/models/N1/urdf/N1_raw.urdf#L568) |
| right_foot_roll_link / com_registered | [0, -0.121878967, -0.654999942] | [0, -0.121878948, -0.655000014] | [0, -0.121878948, -0.655000014] | [0, 1.91854677e-08, -7.16011124e-08] | eligible; compared after Kabsch alignment | [CoM/kinematic input L153](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/fourier_n1/n1.xml#L153) | [CoM/kinematic input L625](https://github.com/FFTAI/wiki-grx-mjcf/blob/f29a87905bdcfc32fdac9c5342644630fd27156a/models/N1/urdf/N1_raw.urdf#L625) | [CoM/kinematic input L625](https://github.com/FFTAI/wiki-grx-mjcf/blob/3079af890e8db4d243e5729abfa9860ecf7487f6/models/N1/urdf/N1_raw.urdf#L625) |
| right_foot_pitch_link / com_registered | [0.031082, -0.119841967, -0.686592942] | [0.031082, -0.119841948, -0.686593014] | [0.031082, -0.119841948, -0.686593014] | [0, 1.91854677e-08, -7.16011123e-08] | eligible; compared after Kabsch alignment | [CoM/kinematic input L158](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/fourier_n1/n1.xml#L158) | [CoM/kinematic input L683](https://github.com/FFTAI/wiki-grx-mjcf/blob/f29a87905bdcfc32fdac9c5342644630fd27156a/models/N1/urdf/N1_raw.urdf#L683) | [CoM/kinematic input L683](https://github.com/FFTAI/wiki-grx-mjcf/blob/3079af890e8db4d243e5729abfa9860ecf7487f6/models/N1/urdf/N1_raw.urdf#L683) |
| imu_link / com_registered | [-0.0071125, 0, -0.14647064] | [-0.0071125, 0, -0.14647064] | [-0.0071125, 0, -0.14647064] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L172](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/fourier_n1/n1.xml#L172) | [CoM/kinematic input L741](https://github.com/FFTAI/wiki-grx-mjcf/blob/f29a87905bdcfc32fdac9c5342644630fd27156a/models/N1/urdf/N1_raw.urdf#L741) | [CoM/kinematic input L741](https://github.com/FFTAI/wiki-grx-mjcf/blob/3079af890e8db4d243e5729abfa9860ecf7487f6/models/N1/urdf/N1_raw.urdf#L741) |
| waist_yaw_link / com_registered | [0.00025493, 1.049e-05, -0.02942] | [0.00025493, 1.049e-05, -0.02942] | [0.00025493, 1.049e-05, -0.02942] | [0, 0, 3.46944695e-18] | eligible; compared after Kabsch alignment | [CoM/kinematic input L179](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/fourier_n1/n1.xml#L179) | [CoM/kinematic input L794](https://github.com/FFTAI/wiki-grx-mjcf/blob/f29a87905bdcfc32fdac9c5342644630fd27156a/models/N1/urdf/N1_raw.urdf#L794) | [CoM/kinematic input L794](https://github.com/FFTAI/wiki-grx-mjcf/blob/3079af890e8db4d243e5729abfa9860ecf7487f6/models/N1/urdf/N1_raw.urdf#L794) |
| torso_link / com_registered | [0.0070827, 0.00038627, 0.243653] | [0.0070827, 0.00038627, 0.243653] | [0.0070827, 0.00038627, 0.243653] | [0, 0, 8.32667268e-17] | eligible; compared after Kabsch alignment | [CoM/kinematic input L185](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/fourier_n1/n1.xml#L185) | [CoM/kinematic input L851](https://github.com/FFTAI/wiki-grx-mjcf/blob/f29a87905bdcfc32fdac9c5342644630fd27156a/models/N1/urdf/N1_raw.urdf#L851) | [CoM/kinematic input L851](https://github.com/FFTAI/wiki-grx-mjcf/blob/3079af890e8db4d243e5729abfa9860ecf7487f6/models/N1/urdf/N1_raw.urdf#L851) |
| camera_link / com_registered | [0.0816276787, -0.0038362049, 0.459106138] | [0.0816276769, -0.00383620457, 0.459106135] | [0.0816276769, -0.00383620457, 0.459106135] | [-1.81026552e-09, 3.3459525e-10, -3.10900122e-09] | eligible; compared after Kabsch alignment | [CoM/kinematic input L191](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/fourier_n1/n1.xml#L191) | [CoM/kinematic input L911](https://github.com/FFTAI/wiki-grx-mjcf/blob/f29a87905bdcfc32fdac9c5342644630fd27156a/models/N1/urdf/N1_raw.urdf#L911) | [CoM/kinematic input L911](https://github.com/FFTAI/wiki-grx-mjcf/blob/3079af890e8db4d243e5729abfa9860ecf7487f6/models/N1/urdf/N1_raw.urdf#L911) |
| left_upper_arm_pitch_link / com_registered | [-0.00045952, 0.158509, 0.2854773] | [-0.00045952, 0.158509, 0.2854773] | [-0.00045952, 0.158509, 0.2854773] | [0, 0, 1.66533454e-16] | eligible; compared after Kabsch alignment | [CoM/kinematic input L197](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/fourier_n1/n1.xml#L197) | [CoM/kinematic input L964](https://github.com/FFTAI/wiki-grx-mjcf/blob/f29a87905bdcfc32fdac9c5342644630fd27156a/models/N1/urdf/N1_raw.urdf#L964) | [CoM/kinematic input L964](https://github.com/FFTAI/wiki-grx-mjcf/blob/3079af890e8db4d243e5729abfa9860ecf7487f6/models/N1/urdf/N1_raw.urdf#L964) |
| left_upper_arm_roll_link / com_registered | [0.0049529, 0.17618148, 0.242031] | [0.0049529, 0.17618148, 0.242031] | [0.0049529, 0.17618148, 0.242031] | [0, 0, 1.11022302e-16] | eligible; compared after Kabsch alignment | [CoM/kinematic input L202](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/fourier_n1/n1.xml#L202) | [CoM/kinematic input L1022](https://github.com/FFTAI/wiki-grx-mjcf/blob/f29a87905bdcfc32fdac9c5342644630fd27156a/models/N1/urdf/N1_raw.urdf#L1022) | [CoM/kinematic input L1022](https://github.com/FFTAI/wiki-grx-mjcf/blob/3079af890e8db4d243e5729abfa9860ecf7487f6/models/N1/urdf/N1_raw.urdf#L1022) |
| left_upper_arm_yaw_link / com_registered | [0, 0.17507131, 0.124171] | [0, 0.17507131, 0.124171] | [0, 0.17507131, 0.124171] | [0, 0, 1.66533454e-16] | eligible; compared after Kabsch alignment | [CoM/kinematic input L208](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/fourier_n1/n1.xml#L208) | [CoM/kinematic input L1079](https://github.com/FFTAI/wiki-grx-mjcf/blob/f29a87905bdcfc32fdac9c5342644630fd27156a/models/N1/urdf/N1_raw.urdf#L1079) | [CoM/kinematic input L1079](https://github.com/FFTAI/wiki-grx-mjcf/blob/3079af890e8db4d243e5729abfa9860ecf7487f6/models/N1/urdf/N1_raw.urdf#L1079) |
| left_lower_arm_pitch_link / com_registered | [0.0433700023, 0.1805999, 0.074868544] | [0.043370002, 0.1805999, 0.0748685193] | [0.043370002, 0.1805999, 0.0748685193] | [-3.02637894e-10, 0, -2.46964955e-08] | eligible; compared after Kabsch alignment | [CoM/kinematic input L215](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/fourier_n1/n1.xml#L215) | [CoM/kinematic input L1136](https://github.com/FFTAI/wiki-grx-mjcf/blob/f29a87905bdcfc32fdac9c5342644630fd27156a/models/N1/urdf/N1_raw.urdf#L1136) | [CoM/kinematic input L1136](https://github.com/FFTAI/wiki-grx-mjcf/blob/3079af890e8db4d243e5729abfa9860ecf7487f6/models/N1/urdf/N1_raw.urdf#L1136) |
| left_hand_yaw_link / com_registered | [0.114215009, 0.17571386, 0.0733169846] | [0.114215008, 0.17571386, 0.0733169195] | [0.114215008, 0.17571386, 0.0733169195] | [-1.18616515e-09, 0, -6.50382825e-08] | eligible; compared after Kabsch alignment | [CoM/kinematic input L221](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/fourier_n1/n1.xml#L221) | [CoM/kinematic input L1194](https://github.com/FFTAI/wiki-grx-mjcf/blob/f29a87905bdcfc32fdac9c5342644630fd27156a/models/N1/urdf/N1_raw.urdf#L1194) | [CoM/kinematic input L1194](https://github.com/FFTAI/wiki-grx-mjcf/blob/3079af890e8db4d243e5729abfa9860ecf7487f6/models/N1/urdf/N1_raw.urdf#L1194) |
| left_end_effector_link / com_registered | [0.204999985, 0.17565, 0.0788658697] | [0.204999987, 0.17565, 0.078865753] | [0.204999987, 0.17565, 0.078865753] | [1.97356215e-09, 0, -1.16734633e-07] | eligible; compared after Kabsch alignment | [CoM/kinematic input L228](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/fourier_n1/n1.xml#L228) | [CoM/kinematic input L1251](https://github.com/FFTAI/wiki-grx-mjcf/blob/f29a87905bdcfc32fdac9c5342644630fd27156a/models/N1/urdf/N1_raw.urdf#L1251) | [CoM/kinematic input L1251](https://github.com/FFTAI/wiki-grx-mjcf/blob/3079af890e8db4d243e5729abfa9860ecf7487f6/models/N1/urdf/N1_raw.urdf#L1251) |
| right_upper_arm_pitch_link / com_registered | [-0.00045952, -0.158509, 0.2853227] | [-0.00045952, -0.158509, 0.2853227] | [-0.00045952, -0.158509, 0.2853227] | [0, 0, 5.55111512e-17] | eligible; compared after Kabsch alignment | [CoM/kinematic input L240](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/fourier_n1/n1.xml#L240) | [CoM/kinematic input L1303](https://github.com/FFTAI/wiki-grx-mjcf/blob/f29a87905bdcfc32fdac9c5342644630fd27156a/models/N1/urdf/N1_raw.urdf#L1303) | [CoM/kinematic input L1303](https://github.com/FFTAI/wiki-grx-mjcf/blob/3079af890e8db4d243e5729abfa9860ecf7487f6/models/N1/urdf/N1_raw.urdf#L1303) |
| right_upper_arm_roll_link / com_registered | [0.0049504, -0.1761718, 0.242023] | [0.0049504, -0.1761718, 0.242023] | [0.0049504, -0.1761718, 0.242023] | [0, 0, 1.11022302e-16] | eligible; compared after Kabsch alignment | [CoM/kinematic input L245](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/fourier_n1/n1.xml#L245) | [CoM/kinematic input L1361](https://github.com/FFTAI/wiki-grx-mjcf/blob/f29a87905bdcfc32fdac9c5342644630fd27156a/models/N1/urdf/N1_raw.urdf#L1361) | [CoM/kinematic input L1361](https://github.com/FFTAI/wiki-grx-mjcf/blob/3079af890e8db4d243e5729abfa9860ecf7487f6/models/N1/urdf/N1_raw.urdf#L1361) |
| right_upper_arm_yaw_link / com_registered | [0, -0.17509331, 0.124171] | [0, -0.17509331, 0.124171] | [0, -0.17509331, 0.124171] | [0, 0, 1.66533454e-16] | eligible; compared after Kabsch alignment | [CoM/kinematic input L252](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/fourier_n1/n1.xml#L252) | [CoM/kinematic input L1418](https://github.com/FFTAI/wiki-grx-mjcf/blob/f29a87905bdcfc32fdac9c5342644630fd27156a/models/N1/urdf/N1_raw.urdf#L1418) | [CoM/kinematic input L1418](https://github.com/FFTAI/wiki-grx-mjcf/blob/3079af890e8db4d243e5729abfa9860ecf7487f6/models/N1/urdf/N1_raw.urdf#L1418) |
| right_lower_arm_pitch_link / com_registered | [0.0433770022, -0.1806004, 0.074878384] | [0.0433770019, -0.1806004, 0.0748783593] | [0.0433770019, -0.1806004, 0.0748783593] | [-2.97034605e-10, 0, -2.47004815e-08] | eligible; compared after Kabsch alignment | [CoM/kinematic input L259](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/fourier_n1/n1.xml#L259) | [CoM/kinematic input L1475](https://github.com/FFTAI/wiki-grx-mjcf/blob/f29a87905bdcfc32fdac9c5342644630fd27156a/models/N1/urdf/N1_raw.urdf#L1475) | [CoM/kinematic input L1475](https://github.com/FFTAI/wiki-grx-mjcf/blob/3079af890e8db4d243e5729abfa9860ecf7487f6/models/N1/urdf/N1_raw.urdf#L1475) |
| right_hand_yaw_link / com_registered | [0.114215001, -0.1756694, 0.0751932946] | [0.114215001, -0.1756694, 0.0751932295] | [0.114215001, -0.1756694, 0.0751932295] | [-1.17724316e-10, 0, -6.50382783e-08] | eligible; compared after Kabsch alignment | [CoM/kinematic input L265](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/fourier_n1/n1.xml#L265) | [CoM/kinematic input L1533](https://github.com/FFTAI/wiki-grx-mjcf/blob/f29a87905bdcfc32fdac9c5342644630fd27156a/models/N1/urdf/N1_raw.urdf#L1533) | [CoM/kinematic input L1533](https://github.com/FFTAI/wiki-grx-mjcf/blob/3079af890e8db4d243e5729abfa9860ecf7487f6/models/N1/urdf/N1_raw.urdf#L1533) |
| right_end_effector_link / com_registered | [0.204999985, -0.17565, 0.0788658697] | [0.204999987, -0.17565, 0.078865753] | [0.204999987, -0.17565, 0.078865753] | [1.97356215e-09, 0, -1.16734633e-07] | eligible; compared after Kabsch alignment | [CoM/kinematic input L272](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/fourier_n1/n1.xml#L272) | [CoM/kinematic input L1590](https://github.com/FFTAI/wiki-grx-mjcf/blob/f29a87905bdcfc32fdac9c5342644630fd27156a/models/N1/urdf/N1_raw.urdf#L1590) | [CoM/kinematic input L1590](https://github.com/FFTAI/wiki-grx-mjcf/blob/3079af890e8db4d243e5729abfa9860ecf7487f6/models/N1/urdf/N1_raw.urdf#L1590) |

## Mass accounting

Every contributing compiled body mass is listed here so total/subtree sums can be checked. Links point to explicit inertials or to geometry inputs when the compiler inferred a mass. CoM links identify inertial inputs; world coordinates additionally use the ancestor transforms and the registration recorded below.

| M body | M kg / source | S kg / source | H kg / source |
|---|---|---|---|
| base_link | 3.18 / [input L82](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/fourier_n1/n1.xml#L82) | 3.18 / [input L14](https://github.com/FFTAI/wiki-grx-mjcf/blob/f29a87905bdcfc32fdac9c5342644630fd27156a/models/N1/urdf/N1_raw.urdf#L14) | 3.18 / [input L14](https://github.com/FFTAI/wiki-grx-mjcf/blob/3079af890e8db4d243e5729abfa9860ecf7487f6/models/N1/urdf/N1_raw.urdf#L14) |
| left_thigh_pitch_link | 1.31 / [input L88](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/fourier_n1/n1.xml#L88) | 1.31 / [input L53](https://github.com/FFTAI/wiki-grx-mjcf/blob/f29a87905bdcfc32fdac9c5342644630fd27156a/models/N1/urdf/N1_raw.urdf#L53) | 1.31 / [input L53](https://github.com/FFTAI/wiki-grx-mjcf/blob/3079af890e8db4d243e5729abfa9860ecf7487f6/models/N1/urdf/N1_raw.urdf#L53) |
| left_thigh_roll_link | 1.35 / [input L93](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/fourier_n1/n1.xml#L93) | 1.35 / [input L111](https://github.com/FFTAI/wiki-grx-mjcf/blob/f29a87905bdcfc32fdac9c5342644630fd27156a/models/N1/urdf/N1_raw.urdf#L111) | 1.35 / [input L111](https://github.com/FFTAI/wiki-grx-mjcf/blob/3079af890e8db4d243e5729abfa9860ecf7487f6/models/N1/urdf/N1_raw.urdf#L111) |
| left_thigh_yaw_link | 3.37 / [input L99](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/fourier_n1/n1.xml#L99) | 3.37 / [input L168](https://github.com/FFTAI/wiki-grx-mjcf/blob/f29a87905bdcfc32fdac9c5342644630fd27156a/models/N1/urdf/N1_raw.urdf#L168) | 3.37 / [input L168](https://github.com/FFTAI/wiki-grx-mjcf/blob/3079af890e8db4d243e5729abfa9860ecf7487f6/models/N1/urdf/N1_raw.urdf#L168) |
| left_shank_pitch_link | 2.21 / [input L105](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/fourier_n1/n1.xml#L105) | 2.21 / [input L225](https://github.com/FFTAI/wiki-grx-mjcf/blob/f29a87905bdcfc32fdac9c5342644630fd27156a/models/N1/urdf/N1_raw.urdf#L225) | 2.21 / [input L225](https://github.com/FFTAI/wiki-grx-mjcf/blob/3079af890e8db4d243e5729abfa9860ecf7487f6/models/N1/urdf/N1_raw.urdf#L225) |
| left_foot_roll_link | 0.113 / [input L111](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/fourier_n1/n1.xml#L111) | 0.113 / [input L282](https://github.com/FFTAI/wiki-grx-mjcf/blob/f29a87905bdcfc32fdac9c5342644630fd27156a/models/N1/urdf/N1_raw.urdf#L282) | 0.113 / [input L282](https://github.com/FFTAI/wiki-grx-mjcf/blob/3079af890e8db4d243e5729abfa9860ecf7487f6/models/N1/urdf/N1_raw.urdf#L282) |
| left_foot_pitch_link | 0.528 / [input L116](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/fourier_n1/n1.xml#L116) | 0.528 / [input L340](https://github.com/FFTAI/wiki-grx-mjcf/blob/f29a87905bdcfc32fdac9c5342644630fd27156a/models/N1/urdf/N1_raw.urdf#L340) | 0.528 / [input L340](https://github.com/FFTAI/wiki-grx-mjcf/blob/3079af890e8db4d243e5729abfa9860ecf7487f6/models/N1/urdf/N1_raw.urdf#L340) |
| right_thigh_pitch_link | 1.31 / [input L130](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/fourier_n1/n1.xml#L130) | 1.31 / [input L398](https://github.com/FFTAI/wiki-grx-mjcf/blob/f29a87905bdcfc32fdac9c5342644630fd27156a/models/N1/urdf/N1_raw.urdf#L398) | 1.31 / [input L398](https://github.com/FFTAI/wiki-grx-mjcf/blob/3079af890e8db4d243e5729abfa9860ecf7487f6/models/N1/urdf/N1_raw.urdf#L398) |
| right_thigh_roll_link | 1.35 / [input L135](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/fourier_n1/n1.xml#L135) | 1.35 / [input L456](https://github.com/FFTAI/wiki-grx-mjcf/blob/f29a87905bdcfc32fdac9c5342644630fd27156a/models/N1/urdf/N1_raw.urdf#L456) | 1.35 / [input L456](https://github.com/FFTAI/wiki-grx-mjcf/blob/3079af890e8db4d243e5729abfa9860ecf7487f6/models/N1/urdf/N1_raw.urdf#L456) |
| right_thigh_yaw_link | 3.37 / [input L141](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/fourier_n1/n1.xml#L141) | 3.37 / [input L513](https://github.com/FFTAI/wiki-grx-mjcf/blob/f29a87905bdcfc32fdac9c5342644630fd27156a/models/N1/urdf/N1_raw.urdf#L513) | 3.37 / [input L513](https://github.com/FFTAI/wiki-grx-mjcf/blob/3079af890e8db4d243e5729abfa9860ecf7487f6/models/N1/urdf/N1_raw.urdf#L513) |
| right_shank_pitch_link | 2.21 / [input L147](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/fourier_n1/n1.xml#L147) | 2.21 / [input L570](https://github.com/FFTAI/wiki-grx-mjcf/blob/f29a87905bdcfc32fdac9c5342644630fd27156a/models/N1/urdf/N1_raw.urdf#L570) | 2.21 / [input L570](https://github.com/FFTAI/wiki-grx-mjcf/blob/3079af890e8db4d243e5729abfa9860ecf7487f6/models/N1/urdf/N1_raw.urdf#L570) |
| right_foot_roll_link | 0.113 / [input L153](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/fourier_n1/n1.xml#L153) | 0.113 / [input L627](https://github.com/FFTAI/wiki-grx-mjcf/blob/f29a87905bdcfc32fdac9c5342644630fd27156a/models/N1/urdf/N1_raw.urdf#L627) | 0.113 / [input L627](https://github.com/FFTAI/wiki-grx-mjcf/blob/3079af890e8db4d243e5729abfa9860ecf7487f6/models/N1/urdf/N1_raw.urdf#L627) |
| right_foot_pitch_link | 0.528 / [input L158](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/fourier_n1/n1.xml#L158) | 0.528 / [input L685](https://github.com/FFTAI/wiki-grx-mjcf/blob/f29a87905bdcfc32fdac9c5342644630fd27156a/models/N1/urdf/N1_raw.urdf#L685) | 0.528 / [input L685](https://github.com/FFTAI/wiki-grx-mjcf/blob/3079af890e8db4d243e5729abfa9860ecf7487f6/models/N1/urdf/N1_raw.urdf#L685) |
| imu_link | 0.038 / [input L172](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/fourier_n1/n1.xml#L172) | 0.038 / [input L743](https://github.com/FFTAI/wiki-grx-mjcf/blob/f29a87905bdcfc32fdac9c5342644630fd27156a/models/N1/urdf/N1_raw.urdf#L743) | 0.038 / [input L743](https://github.com/FFTAI/wiki-grx-mjcf/blob/3079af890e8db4d243e5729abfa9860ecf7487f6/models/N1/urdf/N1_raw.urdf#L743) |
| waist_yaw_link | 3.18 / [input L179](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/fourier_n1/n1.xml#L179) | 3.18 / [input L796](https://github.com/FFTAI/wiki-grx-mjcf/blob/f29a87905bdcfc32fdac9c5342644630fd27156a/models/N1/urdf/N1_raw.urdf#L796) | 3.18 / [input L796](https://github.com/FFTAI/wiki-grx-mjcf/blob/3079af890e8db4d243e5729abfa9860ecf7487f6/models/N1/urdf/N1_raw.urdf#L796) |
| torso_link | 7.99 / [input L185](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/fourier_n1/n1.xml#L185) | 7.99 / [input L853](https://github.com/FFTAI/wiki-grx-mjcf/blob/f29a87905bdcfc32fdac9c5342644630fd27156a/models/N1/urdf/N1_raw.urdf#L853) | 7.99 / [input L853](https://github.com/FFTAI/wiki-grx-mjcf/blob/3079af890e8db4d243e5729abfa9860ecf7487f6/models/N1/urdf/N1_raw.urdf#L853) |
| camera_link | 0.0382 / [input L191](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/fourier_n1/n1.xml#L191) | 0.0382 / [input L913](https://github.com/FFTAI/wiki-grx-mjcf/blob/f29a87905bdcfc32fdac9c5342644630fd27156a/models/N1/urdf/N1_raw.urdf#L913) | 0.0382 / [input L913](https://github.com/FFTAI/wiki-grx-mjcf/blob/3079af890e8db4d243e5729abfa9860ecf7487f6/models/N1/urdf/N1_raw.urdf#L913) |
| left_upper_arm_pitch_link | 0.885 / [input L197](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/fourier_n1/n1.xml#L197) | 0.885 / [input L966](https://github.com/FFTAI/wiki-grx-mjcf/blob/f29a87905bdcfc32fdac9c5342644630fd27156a/models/N1/urdf/N1_raw.urdf#L966) | 0.885 / [input L966](https://github.com/FFTAI/wiki-grx-mjcf/blob/3079af890e8db4d243e5729abfa9860ecf7487f6/models/N1/urdf/N1_raw.urdf#L966) |
| left_upper_arm_roll_link | 0.716 / [input L202](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/fourier_n1/n1.xml#L202) | 0.716 / [input L1024](https://github.com/FFTAI/wiki-grx-mjcf/blob/f29a87905bdcfc32fdac9c5342644630fd27156a/models/N1/urdf/N1_raw.urdf#L1024) | 0.716 / [input L1024](https://github.com/FFTAI/wiki-grx-mjcf/blob/3079af890e8db4d243e5729abfa9860ecf7487f6/models/N1/urdf/N1_raw.urdf#L1024) |
| left_upper_arm_yaw_link | 0.913 / [input L208](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/fourier_n1/n1.xml#L208) | 0.913 / [input L1081](https://github.com/FFTAI/wiki-grx-mjcf/blob/f29a87905bdcfc32fdac9c5342644630fd27156a/models/N1/urdf/N1_raw.urdf#L1081) | 0.913 / [input L1081](https://github.com/FFTAI/wiki-grx-mjcf/blob/3079af890e8db4d243e5729abfa9860ecf7487f6/models/N1/urdf/N1_raw.urdf#L1081) |
| left_lower_arm_pitch_link | 0.716 / [input L215](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/fourier_n1/n1.xml#L215) | 0.716 / [input L1138](https://github.com/FFTAI/wiki-grx-mjcf/blob/f29a87905bdcfc32fdac9c5342644630fd27156a/models/N1/urdf/N1_raw.urdf#L1138) | 0.716 / [input L1138](https://github.com/FFTAI/wiki-grx-mjcf/blob/3079af890e8db4d243e5729abfa9860ecf7487f6/models/N1/urdf/N1_raw.urdf#L1138) |
| left_hand_yaw_link | 0.44 / [input L221](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/fourier_n1/n1.xml#L221) | 0.44 / [input L1196](https://github.com/FFTAI/wiki-grx-mjcf/blob/f29a87905bdcfc32fdac9c5342644630fd27156a/models/N1/urdf/N1_raw.urdf#L1196) | 0.44 / [input L1196](https://github.com/FFTAI/wiki-grx-mjcf/blob/3079af890e8db4d243e5729abfa9860ecf7487f6/models/N1/urdf/N1_raw.urdf#L1196) |
| left_end_effector_link | 0.0994 / [input L228](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/fourier_n1/n1.xml#L228) | 0.0994 / [input L1253](https://github.com/FFTAI/wiki-grx-mjcf/blob/f29a87905bdcfc32fdac9c5342644630fd27156a/models/N1/urdf/N1_raw.urdf#L1253) | 0.0994 / [input L1253](https://github.com/FFTAI/wiki-grx-mjcf/blob/3079af890e8db4d243e5729abfa9860ecf7487f6/models/N1/urdf/N1_raw.urdf#L1253) |
| right_upper_arm_pitch_link | 0.885 / [input L240](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/fourier_n1/n1.xml#L240) | 0.885 / [input L1305](https://github.com/FFTAI/wiki-grx-mjcf/blob/f29a87905bdcfc32fdac9c5342644630fd27156a/models/N1/urdf/N1_raw.urdf#L1305) | 0.885 / [input L1305](https://github.com/FFTAI/wiki-grx-mjcf/blob/3079af890e8db4d243e5729abfa9860ecf7487f6/models/N1/urdf/N1_raw.urdf#L1305) |
| right_upper_arm_roll_link | 0.716 / [input L245](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/fourier_n1/n1.xml#L245) | 0.716 / [input L1363](https://github.com/FFTAI/wiki-grx-mjcf/blob/f29a87905bdcfc32fdac9c5342644630fd27156a/models/N1/urdf/N1_raw.urdf#L1363) | 0.716 / [input L1363](https://github.com/FFTAI/wiki-grx-mjcf/blob/3079af890e8db4d243e5729abfa9860ecf7487f6/models/N1/urdf/N1_raw.urdf#L1363) |
| right_upper_arm_yaw_link | 0.913 / [input L252](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/fourier_n1/n1.xml#L252) | 0.913 / [input L1420](https://github.com/FFTAI/wiki-grx-mjcf/blob/f29a87905bdcfc32fdac9c5342644630fd27156a/models/N1/urdf/N1_raw.urdf#L1420) | 0.913 / [input L1420](https://github.com/FFTAI/wiki-grx-mjcf/blob/3079af890e8db4d243e5729abfa9860ecf7487f6/models/N1/urdf/N1_raw.urdf#L1420) |
| right_lower_arm_pitch_link | 0.716 / [input L259](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/fourier_n1/n1.xml#L259) | 0.716 / [input L1477](https://github.com/FFTAI/wiki-grx-mjcf/blob/f29a87905bdcfc32fdac9c5342644630fd27156a/models/N1/urdf/N1_raw.urdf#L1477) | 0.716 / [input L1477](https://github.com/FFTAI/wiki-grx-mjcf/blob/3079af890e8db4d243e5729abfa9860ecf7487f6/models/N1/urdf/N1_raw.urdf#L1477) |
| right_hand_yaw_link | 0.44 / [input L265](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/fourier_n1/n1.xml#L265) | 0.44 / [input L1535](https://github.com/FFTAI/wiki-grx-mjcf/blob/f29a87905bdcfc32fdac9c5342644630fd27156a/models/N1/urdf/N1_raw.urdf#L1535) | 0.44 / [input L1535](https://github.com/FFTAI/wiki-grx-mjcf/blob/3079af890e8db4d243e5729abfa9860ecf7487f6/models/N1/urdf/N1_raw.urdf#L1535) |
| right_end_effector_link | 0.0994 / [input L272](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/fourier_n1/n1.xml#L272) | 0.0994 / [input L1592](https://github.com/FFTAI/wiki-grx-mjcf/blob/f29a87905bdcfc32fdac9c5342644630fd27156a/models/N1/urdf/N1_raw.urdf#L1592) | 0.0994 / [input L1592](https://github.com/FFTAI/wiki-grx-mjcf/blob/3079af890e8db4d243e5729abfa9860ecf7487f6/models/N1/urdf/N1_raw.urdf#L1592) |

## Coverage and unmatched elements

```json
{
  "mapping_h": {
    "bodies": {
      "base_link": "base_link",
      "left_thigh_pitch_link": "left_thigh_pitch_link",
      "left_thigh_roll_link": "left_thigh_roll_link",
      "left_thigh_yaw_link": "left_thigh_yaw_link",
      "left_shank_pitch_link": "left_shank_pitch_link",
      "left_foot_roll_link": "left_foot_roll_link",
      "left_foot_pitch_link": "left_foot_pitch_link",
      "right_thigh_pitch_link": "right_thigh_pitch_link",
      "right_thigh_roll_link": "right_thigh_roll_link",
      "right_thigh_yaw_link": "right_thigh_yaw_link",
      "right_shank_pitch_link": "right_shank_pitch_link",
      "right_foot_roll_link": "right_foot_roll_link",
      "right_foot_pitch_link": "right_foot_pitch_link",
      "imu_link": "imu_link",
      "waist_yaw_link": "waist_yaw_link",
      "torso_link": "torso_link",
      "camera_link": "camera_link",
      "left_upper_arm_pitch_link": "left_upper_arm_pitch_link",
      "left_upper_arm_roll_link": "left_upper_arm_roll_link",
      "left_upper_arm_yaw_link": "left_upper_arm_yaw_link",
      "left_lower_arm_pitch_link": "left_lower_arm_pitch_link",
      "left_hand_yaw_link": "left_hand_yaw_link",
      "left_end_effector_link": "left_end_effector_link",
      "right_upper_arm_pitch_link": "right_upper_arm_pitch_link",
      "right_upper_arm_roll_link": "right_upper_arm_roll_link",
      "right_upper_arm_yaw_link": "right_upper_arm_yaw_link",
      "right_lower_arm_pitch_link": "right_lower_arm_pitch_link",
      "right_hand_yaw_link": "right_hand_yaw_link",
      "right_end_effector_link": "right_end_effector_link"
    },
    "joints": {
      "left_hip_pitch_joint": "left_hip_pitch_joint",
      "left_hip_roll_joint": "left_hip_roll_joint",
      "left_hip_yaw_joint": "left_hip_yaw_joint",
      "left_knee_pitch_joint": "left_knee_pitch_joint",
      "left_ankle_roll_joint": "left_ankle_roll_joint",
      "left_ankle_pitch_joint": "left_ankle_pitch_joint",
      "right_hip_pitch_joint": "right_hip_pitch_joint",
      "right_hip_roll_joint": "right_hip_roll_joint",
      "right_hip_yaw_joint": "right_hip_yaw_joint",
      "right_knee_pitch_joint": "right_knee_pitch_joint",
      "right_ankle_roll_joint": "right_ankle_roll_joint",
      "right_ankle_pitch_joint": "right_ankle_pitch_joint",
      "waist_yaw_joint": "waist_yaw_joint",
      "left_shoulder_pitch_joint": "left_shoulder_pitch_joint",
      "left_shoulder_roll_joint": "left_shoulder_roll_joint",
      "left_shoulder_yaw_joint": "left_shoulder_yaw_joint",
      "left_elbow_pitch_joint": "left_elbow_pitch_joint",
      "left_wrist_yaw_joint": "left_wrist_yaw_joint",
      "right_shoulder_pitch_joint": "right_shoulder_pitch_joint",
      "right_shoulder_roll_joint": "right_shoulder_roll_joint",
      "right_shoulder_yaw_joint": "right_shoulder_yaw_joint",
      "right_elbow_pitch_joint": "right_elbow_pitch_joint",
      "right_wrist_yaw_joint": "right_wrist_yaw_joint"
    },
    "body_methods": {
      "base_link": "name",
      "left_thigh_pitch_link": "name",
      "left_thigh_roll_link": "name",
      "left_thigh_yaw_link": "name",
      "left_shank_pitch_link": "name",
      "left_foot_roll_link": "name",
      "left_foot_pitch_link": "name",
      "right_thigh_pitch_link": "name",
      "right_thigh_roll_link": "name",
      "right_thigh_yaw_link": "name",
      "right_shank_pitch_link": "name",
      "right_foot_roll_link": "name",
      "right_foot_pitch_link": "name",
      "imu_link": "name",
      "waist_yaw_link": "name",
      "torso_link": "name",
      "camera_link": "name",
      "left_upper_arm_pitch_link": "name",
      "left_upper_arm_roll_link": "name",
      "left_upper_arm_yaw_link": "name",
      "left_lower_arm_pitch_link": "name",
      "left_hand_yaw_link": "name",
      "left_end_effector_link": "name",
      "right_upper_arm_pitch_link": "name",
      "right_upper_arm_roll_link": "name",
      "right_upper_arm_yaw_link": "name",
      "right_lower_arm_pitch_link": "name",
      "right_hand_yaw_link": "name",
      "right_end_effector_link": "name"
    },
    "joint_methods": {
      "left_hip_pitch_joint": "name",
      "left_hip_roll_joint": "name",
      "left_hip_yaw_joint": "name",
      "left_knee_pitch_joint": "name",
      "left_ankle_roll_joint": "name",
      "left_ankle_pitch_joint": "name",
      "right_hip_pitch_joint": "name",
      "right_hip_roll_joint": "name",
      "right_hip_yaw_joint": "name",
      "right_knee_pitch_joint": "name",
      "right_ankle_roll_joint": "name",
      "right_ankle_pitch_joint": "name",
      "waist_yaw_joint": "name",
      "left_shoulder_pitch_joint": "name",
      "left_shoulder_roll_joint": "name",
      "left_shoulder_yaw_joint": "name",
      "left_elbow_pitch_joint": "name",
      "left_wrist_yaw_joint": "name",
      "right_shoulder_pitch_joint": "name",
      "right_shoulder_roll_joint": "name",
      "right_shoulder_yaw_joint": "name",
      "right_elbow_pitch_joint": "name",
      "right_wrist_yaw_joint": "name"
    },
    "unmatched_m_bodies": [],
    "unmatched_upstream_bodies": [],
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
      "left_thigh_pitch_link": "left_thigh_pitch_link",
      "left_thigh_roll_link": "left_thigh_roll_link",
      "left_thigh_yaw_link": "left_thigh_yaw_link",
      "left_shank_pitch_link": "left_shank_pitch_link",
      "left_foot_roll_link": "left_foot_roll_link",
      "left_foot_pitch_link": "left_foot_pitch_link",
      "right_thigh_pitch_link": "right_thigh_pitch_link",
      "right_thigh_roll_link": "right_thigh_roll_link",
      "right_thigh_yaw_link": "right_thigh_yaw_link",
      "right_shank_pitch_link": "right_shank_pitch_link",
      "right_foot_roll_link": "right_foot_roll_link",
      "right_foot_pitch_link": "right_foot_pitch_link",
      "imu_link": "imu_link",
      "waist_yaw_link": "waist_yaw_link",
      "torso_link": "torso_link",
      "camera_link": "camera_link",
      "left_upper_arm_pitch_link": "left_upper_arm_pitch_link",
      "left_upper_arm_roll_link": "left_upper_arm_roll_link",
      "left_upper_arm_yaw_link": "left_upper_arm_yaw_link",
      "left_lower_arm_pitch_link": "left_lower_arm_pitch_link",
      "left_hand_yaw_link": "left_hand_yaw_link",
      "left_end_effector_link": "left_end_effector_link",
      "right_upper_arm_pitch_link": "right_upper_arm_pitch_link",
      "right_upper_arm_roll_link": "right_upper_arm_roll_link",
      "right_upper_arm_yaw_link": "right_upper_arm_yaw_link",
      "right_lower_arm_pitch_link": "right_lower_arm_pitch_link",
      "right_hand_yaw_link": "right_hand_yaw_link",
      "right_end_effector_link": "right_end_effector_link"
    },
    "joints": {
      "left_hip_pitch_joint": "left_hip_pitch_joint",
      "left_hip_roll_joint": "left_hip_roll_joint",
      "left_hip_yaw_joint": "left_hip_yaw_joint",
      "left_knee_pitch_joint": "left_knee_pitch_joint",
      "left_ankle_roll_joint": "left_ankle_roll_joint",
      "left_ankle_pitch_joint": "left_ankle_pitch_joint",
      "right_hip_pitch_joint": "right_hip_pitch_joint",
      "right_hip_roll_joint": "right_hip_roll_joint",
      "right_hip_yaw_joint": "right_hip_yaw_joint",
      "right_knee_pitch_joint": "right_knee_pitch_joint",
      "right_ankle_roll_joint": "right_ankle_roll_joint",
      "right_ankle_pitch_joint": "right_ankle_pitch_joint",
      "waist_yaw_joint": "waist_yaw_joint",
      "left_shoulder_pitch_joint": "left_shoulder_pitch_joint",
      "left_shoulder_roll_joint": "left_shoulder_roll_joint",
      "left_shoulder_yaw_joint": "left_shoulder_yaw_joint",
      "left_elbow_pitch_joint": "left_elbow_pitch_joint",
      "left_wrist_yaw_joint": "left_wrist_yaw_joint",
      "right_shoulder_pitch_joint": "right_shoulder_pitch_joint",
      "right_shoulder_roll_joint": "right_shoulder_roll_joint",
      "right_shoulder_yaw_joint": "right_shoulder_yaw_joint",
      "right_elbow_pitch_joint": "right_elbow_pitch_joint",
      "right_wrist_yaw_joint": "right_wrist_yaw_joint"
    },
    "body_methods": {
      "base_link": "name",
      "left_thigh_pitch_link": "name",
      "left_thigh_roll_link": "name",
      "left_thigh_yaw_link": "name",
      "left_shank_pitch_link": "name",
      "left_foot_roll_link": "name",
      "left_foot_pitch_link": "name",
      "right_thigh_pitch_link": "name",
      "right_thigh_roll_link": "name",
      "right_thigh_yaw_link": "name",
      "right_shank_pitch_link": "name",
      "right_foot_roll_link": "name",
      "right_foot_pitch_link": "name",
      "imu_link": "name",
      "waist_yaw_link": "name",
      "torso_link": "name",
      "camera_link": "name",
      "left_upper_arm_pitch_link": "name",
      "left_upper_arm_roll_link": "name",
      "left_upper_arm_yaw_link": "name",
      "left_lower_arm_pitch_link": "name",
      "left_hand_yaw_link": "name",
      "left_end_effector_link": "name",
      "right_upper_arm_pitch_link": "name",
      "right_upper_arm_roll_link": "name",
      "right_upper_arm_yaw_link": "name",
      "right_lower_arm_pitch_link": "name",
      "right_hand_yaw_link": "name",
      "right_end_effector_link": "name"
    },
    "joint_methods": {
      "left_hip_pitch_joint": "name",
      "left_hip_roll_joint": "name",
      "left_hip_yaw_joint": "name",
      "left_knee_pitch_joint": "name",
      "left_ankle_roll_joint": "name",
      "left_ankle_pitch_joint": "name",
      "right_hip_pitch_joint": "name",
      "right_hip_roll_joint": "name",
      "right_hip_yaw_joint": "name",
      "right_knee_pitch_joint": "name",
      "right_ankle_roll_joint": "name",
      "right_ankle_pitch_joint": "name",
      "waist_yaw_joint": "name",
      "left_shoulder_pitch_joint": "name",
      "left_shoulder_roll_joint": "name",
      "left_shoulder_yaw_joint": "name",
      "left_elbow_pitch_joint": "name",
      "left_wrist_yaw_joint": "name",
      "right_shoulder_pitch_joint": "name",
      "right_shoulder_roll_joint": "name",
      "right_shoulder_yaw_joint": "name",
      "right_elbow_pitch_joint": "name",
      "right_wrist_yaw_joint": "name"
    },
    "unmatched_m_bodies": [],
    "unmatched_upstream_bodies": [],
    "unmatched_m_joints": [],
    "unmatched_upstream_joints": [],
    "registration_anchor": {
      "M": "base_link",
      "S": "base_link"
    }
  },
  "unavailable": [
    {
      "entity": "left_hip_pitch_joint",
      "other_entity": "left_hip_pitch_joint",
      "quantity": "force",
      "tolerance": "limit",
      "m": 95.0,
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
      "other": 12.356,
      "s": 12.356,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_hip_roll_joint",
      "other_entity": "left_hip_roll_joint",
      "quantity": "force",
      "tolerance": "limit",
      "m": 54.0,
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
      "other": 14.738,
      "s": 14.738,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_hip_yaw_joint",
      "other_entity": "left_hip_yaw_joint",
      "quantity": "force",
      "tolerance": "limit",
      "m": 54.0,
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
      "other": 14.738,
      "s": 14.738,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_knee_pitch_joint",
      "other_entity": "left_knee_pitch_joint",
      "quantity": "force",
      "tolerance": "limit",
      "m": 95.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_knee_pitch_joint",
      "other_entity": "left_knee_pitch_joint",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 12.356,
      "s": 12.356,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_ankle_roll_joint",
      "other_entity": "left_ankle_roll_joint",
      "quantity": "force",
      "tolerance": "limit",
      "m": 30.0,
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
      "other": 16.747,
      "s": 16.747,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_ankle_pitch_joint",
      "other_entity": "left_ankle_pitch_joint",
      "quantity": "force",
      "tolerance": "limit",
      "m": 30.0,
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
      "other": 16.747,
      "s": 16.747,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "right_hip_pitch_joint",
      "other_entity": "right_hip_pitch_joint",
      "quantity": "force",
      "tolerance": "limit",
      "m": 95.0,
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
      "other": 12.356,
      "s": 12.356,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "right_hip_roll_joint",
      "other_entity": "right_hip_roll_joint",
      "quantity": "force",
      "tolerance": "limit",
      "m": 54.0,
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
      "other": 14.738,
      "s": 14.738,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "right_hip_yaw_joint",
      "other_entity": "right_hip_yaw_joint",
      "quantity": "force",
      "tolerance": "limit",
      "m": 54.0,
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
      "other": 14.738,
      "s": 14.738,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "right_knee_pitch_joint",
      "other_entity": "right_knee_pitch_joint",
      "quantity": "force",
      "tolerance": "limit",
      "m": 95.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "right_knee_pitch_joint",
      "other_entity": "right_knee_pitch_joint",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 12.356,
      "s": 12.356,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "right_ankle_roll_joint",
      "other_entity": "right_ankle_roll_joint",
      "quantity": "force",
      "tolerance": "limit",
      "m": 30.0,
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
      "other": 16.747,
      "s": 16.747,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "right_ankle_pitch_joint",
      "other_entity": "right_ankle_pitch_joint",
      "quantity": "force",
      "tolerance": "limit",
      "m": 30.0,
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
      "other": 16.747,
      "s": 16.747,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "waist_yaw_joint",
      "other_entity": "waist_yaw_joint",
      "quantity": "force",
      "tolerance": "limit",
      "m": 54.0,
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
      "other": 14.738,
      "s": 14.738,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_shoulder_pitch_joint",
      "other_entity": "left_shoulder_pitch_joint",
      "quantity": "force",
      "tolerance": "limit",
      "m": 54.0,
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
      "other": 14.738,
      "s": 14.738,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_shoulder_roll_joint",
      "other_entity": "left_shoulder_roll_joint",
      "quantity": "force",
      "tolerance": "limit",
      "m": 30.0,
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
      "other": 16.747,
      "s": 16.747,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_shoulder_yaw_joint",
      "other_entity": "left_shoulder_yaw_joint",
      "quantity": "force",
      "tolerance": "limit",
      "m": 30.0,
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
      "other": 16.747,
      "s": 16.747,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_elbow_pitch_joint",
      "other_entity": "left_elbow_pitch_joint",
      "quantity": "force",
      "tolerance": "limit",
      "m": 30.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_elbow_pitch_joint",
      "other_entity": "left_elbow_pitch_joint",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 16.747,
      "s": 16.747,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_wrist_yaw_joint",
      "other_entity": "left_wrist_yaw_joint",
      "quantity": "force",
      "tolerance": "limit",
      "m": 30.0,
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
      "other": 16.747,
      "s": 16.747,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "right_shoulder_pitch_joint",
      "other_entity": "right_shoulder_pitch_joint",
      "quantity": "force",
      "tolerance": "limit",
      "m": 54.0,
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
      "other": 14.738,
      "s": 14.738,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "right_shoulder_roll_joint",
      "other_entity": "right_shoulder_roll_joint",
      "quantity": "force",
      "tolerance": "limit",
      "m": 30.0,
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
      "other": 16.747,
      "s": 16.747,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "right_shoulder_yaw_joint",
      "other_entity": "right_shoulder_yaw_joint",
      "quantity": "force",
      "tolerance": "limit",
      "m": 30.0,
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
      "other": 16.747,
      "s": 16.747,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "right_elbow_pitch_joint",
      "other_entity": "right_elbow_pitch_joint",
      "quantity": "force",
      "tolerance": "limit",
      "m": 30.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "right_elbow_pitch_joint",
      "other_entity": "right_elbow_pitch_joint",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 16.747,
      "s": 16.747,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "right_wrist_yaw_joint",
      "other_entity": "right_wrist_yaw_joint",
      "quantity": "force",
      "tolerance": "limit",
      "m": 30.0,
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
      "other": 16.747,
      "s": 16.747,
      "reason": "quantity absent or not enforced/declared on one side"
    }
  ]
}
```

## Limits unavailable for a like-for-like simulator comparison

URDF effort and velocity tags are manufacturer declarations; MuJoCo ignores them. Missing enforced quantities are not interpreted as zero. The available values are shown for review and excluded from STALE counts.

| Joint / quantity | M | S | H / declared upstream |
|---|---|---|---|
| left_hip_pitch_joint / force | 95 | unavailable | unavailable |
| left_hip_pitch_joint / velocity | unavailable | 12.356 | 12.356 |
| left_hip_roll_joint / force | 54 | unavailable | unavailable |
| left_hip_roll_joint / velocity | unavailable | 14.738 | 14.738 |
| left_hip_yaw_joint / force | 54 | unavailable | unavailable |
| left_hip_yaw_joint / velocity | unavailable | 14.738 | 14.738 |
| left_knee_pitch_joint / force | 95 | unavailable | unavailable |
| left_knee_pitch_joint / velocity | unavailable | 12.356 | 12.356 |
| left_ankle_roll_joint / force | 30 | unavailable | unavailable |
| left_ankle_roll_joint / velocity | unavailable | 16.747 | 16.747 |
| left_ankle_pitch_joint / force | 30 | unavailable | unavailable |
| left_ankle_pitch_joint / velocity | unavailable | 16.747 | 16.747 |
| right_hip_pitch_joint / force | 95 | unavailable | unavailable |
| right_hip_pitch_joint / velocity | unavailable | 12.356 | 12.356 |
| right_hip_roll_joint / force | 54 | unavailable | unavailable |
| right_hip_roll_joint / velocity | unavailable | 14.738 | 14.738 |
| right_hip_yaw_joint / force | 54 | unavailable | unavailable |
| right_hip_yaw_joint / velocity | unavailable | 14.738 | 14.738 |
| right_knee_pitch_joint / force | 95 | unavailable | unavailable |
| right_knee_pitch_joint / velocity | unavailable | 12.356 | 12.356 |
| right_ankle_roll_joint / force | 30 | unavailable | unavailable |
| right_ankle_roll_joint / velocity | unavailable | 16.747 | 16.747 |
| right_ankle_pitch_joint / force | 30 | unavailable | unavailable |
| right_ankle_pitch_joint / velocity | unavailable | 16.747 | 16.747 |
| waist_yaw_joint / force | 54 | unavailable | unavailable |
| waist_yaw_joint / velocity | unavailable | 14.738 | 14.738 |
| left_shoulder_pitch_joint / force | 54 | unavailable | unavailable |
| left_shoulder_pitch_joint / velocity | unavailable | 14.738 | 14.738 |
| left_shoulder_roll_joint / force | 30 | unavailable | unavailable |
| left_shoulder_roll_joint / velocity | unavailable | 16.747 | 16.747 |
| left_shoulder_yaw_joint / force | 30 | unavailable | unavailable |
| left_shoulder_yaw_joint / velocity | unavailable | 16.747 | 16.747 |
| left_elbow_pitch_joint / force | 30 | unavailable | unavailable |
| left_elbow_pitch_joint / velocity | unavailable | 16.747 | 16.747 |
| left_wrist_yaw_joint / force | 30 | unavailable | unavailable |
| left_wrist_yaw_joint / velocity | unavailable | 16.747 | 16.747 |
| right_shoulder_pitch_joint / force | 54 | unavailable | unavailable |
| right_shoulder_pitch_joint / velocity | unavailable | 14.738 | 14.738 |
| right_shoulder_roll_joint / force | 30 | unavailable | unavailable |
| right_shoulder_roll_joint / velocity | unavailable | 16.747 | 16.747 |
| right_shoulder_yaw_joint / force | 30 | unavailable | unavailable |
| right_shoulder_yaw_joint / velocity | unavailable | 16.747 | 16.747 |
| right_elbow_pitch_joint / force | 30 | unavailable | unavailable |
| right_elbow_pitch_joint / velocity | unavailable | 16.747 | 16.747 |
| right_wrist_yaw_joint / force | 30 | unavailable | unavailable |
| right_wrist_yaw_joint / velocity | unavailable | 16.747 | 16.747 |
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
  "Source discovery https://github.com/FFTAI/Wiki-GRx-Models: CalledProcessError: Command '['git', '-C', '.cache/FFTAI__Wiki-GRx-Models', 'ls-tree', '-r', '--name-only', 'f29a87905bdcfc32fdac9c5342644630fd27156a']' returned non-zero exit status 128."
]
```

## Self comparisons

```json
[
  {
    "file": "fourier_n1/n1.xml",
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
      "fourier_n1/n1.xml"
    ],
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
      "models/N1/urdf/N1_raw.urdf"
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
      "models/N1/urdf/N1_raw.urdf"
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
  "historical_snapshots_reused": 1,
  "primary_physics_unchanged": true,
  "source_matching": "original raw-value provenance criteria retained; kinematic guard applies to reported CoM"
}
```
