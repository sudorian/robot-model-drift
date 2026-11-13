# robotstudio_so101

Status: **complete**. Provenance: **pinned**, confidence **high**.

Source selected using the ordered amended provenance rules.

M: `https://github.com/google-deepmind/mujoco_menagerie`, `robotstudio_so101/so101.xml`, commit `370c43965323c0944b433b202aac5058b5f907a9`.
H: `https://github.com/TheRobotStudio/SO-ARM100`, `Simulation/SO101/so101_new_calib.xml`, commit `a758567c3978dfeefe282ede0500085a48fe8f78`.
S: `aec17bbc256d1a7342d53aaa4950595d4c30b40d` (2025-11-27T13:51:43+01:00). Menagerie release/change: 2026-09-28T12:43:05-07:00.

Limit semantics: MJCF effort values are supported actuator torque/force envelopes. URDF effort and velocity values are manufacturer declarations retained from XML; MuJoCo does not enforce those tags. Such declaration comparisons are explicitly distinct from compiled inertial/range quantities.


## Source evidence

```json
[
  {
    "url": "https://github.com/TheRobotStudio/SO-ARM100/blob/608122e9ac330a753735f2e18aee73338e9ac407/Simulation/SO101/so101_new_calib.xml#L1",
    "document": "robotstudio_so101/README.md",
    "commit": "370c43965323c0944b433b202aac5058b5f907a9",
    "current": true
  },
  {
    "url": "https://github.com/TheRobotStudio/SO-ARM100/tree/main/Simulation/SO101",
    "document": "robotstudio_so101/README.md",
    "commit": "370c43965323c0944b433b202aac5058b5f907a9",
    "current": true
  }
]
```


## README derivation evidence

Documentation labels are conservative: an automated documented label requires an explicit affected entity and quantity. Broader conversion notes are retained here for review.

> 4. Use default `forcerange` for actuators rather than 3.35 N/m.

## Kinematics consistency

A proper Kabsch rigid transform aligns all matched zero-pose body origins. The maximum per-origin residual and signed hinge/slide axis angles determine whether CoM can be compared; RMS is also recorded. Fewer than three non-collinear origins give insufficient kinematic coverage. CoM records that fail either required M/H or M/S check are excluded from counts and largest discrepancies. Masses, principal moments and raw joint ranges remain unchanged; a flagged range still requires convention review.

| Pair | Status | Origins / rank | RMS / maximum mm | Disagreeing / checked axes |
|---|---|---:|---:|---:|
| M/H | consistent | 7 / 3 | 2.20410088e-06 / 3.80169448e-06 | 0 / 6 |
| M/S | consistent | 7 / 3 | 2.20410088e-06 / 3.80169448e-06 | 0 / 6 |

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
    "anchor_m": "base",
    "anchor_other": "base",
    "rotation_other_to_m": [
      [
        0.9999999999999999,
        7.468364174525115e-09,
        -7.34614067602543e-10
      ],
      [
        -7.468363927154883e-09,
        0.9999999999999996,
        3.1052209445168266e-08
      ],
      [
        7.346141334130252e-10,
        -3.105220972021705e-08,
        0.9999999999999994
      ]
    ],
    "translation_other_to_m": [
      1.5873272141142536e-10,
      3.788353718399418e-09,
      -2.757914729922817e-10
    ],
    "rms_residual_m": 2.2041008774285685e-09,
    "max_residual_m": 3.801694478667719e-09,
    "fit_rank": 3,
    "axis_checks": [
      {
        "joint_m": "shoulder_pan",
        "joint_other": "shoulder_pan",
        "axis_m": [
          0.0,
          0.0,
          -1.0
        ],
        "axis_other_aligned": [
          7.346133552685493e-10,
          -3.105220861589827e-08,
          -0.9999999999999996
        ],
        "angle_rad": 3.106089690763945e-08,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "shoulder_lift",
        "joint_other": "shoulder_lift",
        "axis_m": [
          0.0,
          1.0,
          0.0
        ],
        "axis_other_aligned": [
          7.46836173203446e-09,
          0.9999999999999996,
          -3.105220883203863e-08
        ],
        "angle_rad": 3.1937690904463566e-08,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "elbow_flex",
        "joint_other": "elbow_flex",
        "axis_m": [
          0.0,
          1.0,
          2.2204460492503136e-16
        ],
        "axis_other_aligned": [
          7.468361585382058e-09,
          0.9999999999999994,
          -3.1052208609994025e-08
        ],
        "angle_rad": 3.1937690870170134e-08,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "wrist_flex",
        "joint_other": "wrist_flex",
        "axis_m": [
          2.465190328815663e-32,
          1.0,
          4.440892098500628e-16
        ],
        "axis_other_aligned": [
          7.46836400799166e-09,
          0.9999999999999994,
          -3.105220849897172e-08
        ],
        "angle_rad": 3.193769154462137e-08,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "wrist_roll",
        "joint_other": "wrist_roll",
        "axis_m": [
          -1.0,
          -3.526315678860507e-17,
          2.2204460492503136e-16
        ],
        "axis_other_aligned": [
          -1.0,
          7.468363751819834e-09,
          -7.346129121676927e-10
        ],
        "angle_rad": 7.504406313171603e-09,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "gripper",
        "joint_other": "gripper",
        "axis_m": [
          4.2826119472035783e-17,
          -0.998815386375634,
          -0.04866029119613848
        ],
        "axis_other_aligned": [
          -7.423770436358345e-09,
          -0.9988153878866431,
          -0.04866026018071407
        ],
        "angle_rad": 3.1927293461288614e-08,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      }
    ],
    "axis_disagreements": [],
    "com_eligible": true,
    "covariance_singular_values": [
      0.150533818859318,
      0.011230936238101214,
      0.00048770209240361895
    ],
    "origin_residuals_m": {
      "base": 3.801694478667719e-09,
      "shoulder": 3.5510129929962814e-09,
      "upper_arm": 2.1135200807484784e-09,
      "lower_arm": 1.2639935818039317e-09,
      "wrist": 6.023453922439388e-10,
      "gripper": 1.1543730423510082e-10,
      "moving_jaw_so101_v1": 7.092657543357826e-10
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
    "anchor_m": "base",
    "anchor_other": "base",
    "rotation_other_to_m": [
      [
        0.9999999999999999,
        7.468364174525115e-09,
        -7.34614067602543e-10
      ],
      [
        -7.468363927154883e-09,
        0.9999999999999996,
        3.1052209445168266e-08
      ],
      [
        7.346141334130252e-10,
        -3.105220972021705e-08,
        0.9999999999999994
      ]
    ],
    "translation_other_to_m": [
      1.5873272141142536e-10,
      3.788353718399418e-09,
      -2.757914729922817e-10
    ],
    "rms_residual_m": 2.2041008774285685e-09,
    "max_residual_m": 3.801694478667719e-09,
    "fit_rank": 3,
    "axis_checks": [
      {
        "joint_m": "shoulder_pan",
        "joint_other": "shoulder_pan",
        "axis_m": [
          0.0,
          0.0,
          -1.0
        ],
        "axis_other_aligned": [
          7.346133552685493e-10,
          -3.105220861589827e-08,
          -0.9999999999999996
        ],
        "angle_rad": 3.106089690763945e-08,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "shoulder_lift",
        "joint_other": "shoulder_lift",
        "axis_m": [
          0.0,
          1.0,
          0.0
        ],
        "axis_other_aligned": [
          7.46836173203446e-09,
          0.9999999999999996,
          -3.105220883203863e-08
        ],
        "angle_rad": 3.1937690904463566e-08,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "elbow_flex",
        "joint_other": "elbow_flex",
        "axis_m": [
          0.0,
          1.0,
          2.2204460492503136e-16
        ],
        "axis_other_aligned": [
          7.468361585382058e-09,
          0.9999999999999994,
          -3.1052208609994025e-08
        ],
        "angle_rad": 3.1937690870170134e-08,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "wrist_flex",
        "joint_other": "wrist_flex",
        "axis_m": [
          2.465190328815663e-32,
          1.0,
          4.440892098500628e-16
        ],
        "axis_other_aligned": [
          7.46836400799166e-09,
          0.9999999999999994,
          -3.105220849897172e-08
        ],
        "angle_rad": 3.193769154462137e-08,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "wrist_roll",
        "joint_other": "wrist_roll",
        "axis_m": [
          -1.0,
          -3.526315678860507e-17,
          2.2204460492503136e-16
        ],
        "axis_other_aligned": [
          -1.0,
          7.468363751819834e-09,
          -7.346129121676927e-10
        ],
        "angle_rad": 7.504406313171603e-09,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "gripper",
        "joint_other": "gripper",
        "axis_m": [
          4.2826119472035783e-17,
          -0.998815386375634,
          -0.04866029119613848
        ],
        "axis_other_aligned": [
          -7.423770436358345e-09,
          -0.9988153878866431,
          -0.04866026018071407
        ],
        "angle_rad": 3.1927293461288614e-08,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      }
    ],
    "axis_disagreements": [],
    "com_eligible": true,
    "covariance_singular_values": [
      0.150533818859318,
      0.011230936238101214,
      0.00048770209240361895
    ],
    "origin_residuals_m": {
      "base": 3.801694478667719e-09,
      "shoulder": 3.5510129929962814e-09,
      "upper_arm": 2.1135200807484784e-09,
      "lower_arm": 1.2639935818039317e-09,
      "wrist": 6.023453922439388e-10,
      "gripper": 1.1543730423510082e-10,
      "moving_jaw_so101_v1": 7.092657543357826e-10
    },
    "reason": "Unique proper rigid fit and matched signed axes meet the configured thresholds"
  }
}
```


## Every reported quantity difference

Counts are quantity records, including correlated total/subtree/body mass records; they are not independent robot defects.

| Entity / quantity | M | S | H | H − M | Class | M source | S source | H source |
|---|---|---|---|---|---|---|---|---|
| robot / total_mass | 0.64545 | 0.632006 | 0.632006 | -0.013444 | undocumented derivation difference | [aggregate inputs](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/robotstudio_so101/so101.xml#L1) | [aggregate inputs](https://github.com/TheRobotStudio/SO-ARM100/blob/aec17bbc256d1a7342d53aaa4950595d4c30b40d/Simulation/SO101/so101_new_calib.xml#L1) | [aggregate inputs](https://github.com/TheRobotStudio/SO-ARM100/blob/a758567c3978dfeefe282ede0500085a48fe8f78/Simulation/SO101/so101_new_calib.xml#L1) |
| robot / total_com_registered | [0.147133191, 0.00225186317, 0.161538864] | [0.143249358, 0.00121542264, 0.159956569] | [0.143249358, 0.00121542264, 0.159956569] | [-0.00388383229, -0.00103644053, -0.00158229517] | undocumented derivation difference | [aggregate inputs](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/robotstudio_so101/so101.xml#L1) | [aggregate inputs](https://github.com/TheRobotStudio/SO-ARM100/blob/aec17bbc256d1a7342d53aaa4950595d4c30b40d/Simulation/SO101/so101_new_calib.xml#L1) | [aggregate inputs](https://github.com/TheRobotStudio/SO-ARM100/blob/a758567c3978dfeefe282ede0500085a48fe8f78/Simulation/SO101/so101_new_calib.xml#L1) |
| base / subtree_mass | 0.64545 | 0.632006 | 0.632006 | -0.013444 | undocumented derivation difference | [subtree root L84](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/robotstudio_so101/so101.xml#L84) | [subtree root L36](https://github.com/TheRobotStudio/SO-ARM100/blob/aec17bbc256d1a7342d53aaa4950595d4c30b40d/Simulation/SO101/so101_new_calib.xml#L36) | [subtree root L36](https://github.com/TheRobotStudio/SO-ARM100/blob/a758567c3978dfeefe282ede0500085a48fe8f78/Simulation/SO101/so101_new_calib.xml#L36) |
| shoulder / subtree_mass | 0.49845 | 0.485006 | 0.485006 | -0.013444 | undocumented derivation difference | [subtree root L102](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/robotstudio_so101/so101.xml#L102) | [subtree root L49](https://github.com/TheRobotStudio/SO-ARM100/blob/aec17bbc256d1a7342d53aaa4950595d4c30b40d/Simulation/SO101/so101_new_calib.xml#L49) | [subtree root L49](https://github.com/TheRobotStudio/SO-ARM100/blob/a758567c3978dfeefe282ede0500085a48fe8f78/Simulation/SO101/so101_new_calib.xml#L49) |
| upper_arm / subtree_mass | 0.398444 | 0.385 | 0.385 | -0.013444 | undocumented derivation difference | [subtree root L119](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/robotstudio_so101/so101.xml#L119) | [subtree root L63](https://github.com/TheRobotStudio/SO-ARM100/blob/aec17bbc256d1a7342d53aaa4950595d4c30b40d/Simulation/SO101/so101_new_calib.xml#L63) | [subtree root L63](https://github.com/TheRobotStudio/SO-ARM100/blob/a758567c3978dfeefe282ede0500085a48fe8f78/Simulation/SO101/so101_new_calib.xml#L63) |
| lower_arm / subtree_mass | 0.295444 | 0.282 | 0.282 | -0.013444 | undocumented derivation difference | [subtree root L133](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/robotstudio_so101/so101.xml#L133) | [subtree root L74](https://github.com/TheRobotStudio/SO-ARM100/blob/aec17bbc256d1a7342d53aaa4950595d4c30b40d/Simulation/SO101/so101_new_calib.xml#L74) | [subtree root L74](https://github.com/TheRobotStudio/SO-ARM100/blob/a758567c3978dfeefe282ede0500085a48fe8f78/Simulation/SO101/so101_new_calib.xml#L74) |
| wrist / subtree_mass | 0.191444 | 0.178 | 0.178 | -0.013444 | undocumented derivation difference | [subtree root L151](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/robotstudio_so101/so101.xml#L151) | [subtree root L89](https://github.com/TheRobotStudio/SO-ARM100/blob/aec17bbc256d1a7342d53aaa4950595d4c30b40d/Simulation/SO101/so101_new_calib.xml#L89) | [subtree root L89](https://github.com/TheRobotStudio/SO-ARM100/blob/a758567c3978dfeefe282ede0500085a48fe8f78/Simulation/SO101/so101_new_calib.xml#L89) |
| gripper / subtree_mass | 0.112444 | 0.099 | 0.099 | -0.013444 | undocumented derivation difference | [subtree root L165](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/robotstudio_so101/so101.xml#L165) | [subtree root L100](https://github.com/TheRobotStudio/SO-ARM100/blob/aec17bbc256d1a7342d53aaa4950595d4c30b40d/Simulation/SO101/so101_new_calib.xml#L100) | [subtree root L100](https://github.com/TheRobotStudio/SO-ARM100/blob/a758567c3978dfeefe282ede0500085a48fe8f78/Simulation/SO101/so101_new_calib.xml#L100) |
| shoulder_pan / effort | 2.94 | 3.35 | 3.35 | 0.41 | undocumented derivation difference | [inherited actuator input L38](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/robotstudio_so101/so101.xml#L38) | [input L157](https://github.com/TheRobotStudio/SO-ARM100/blob/aec17bbc256d1a7342d53aaa4950595d4c30b40d/Simulation/SO101/so101_new_calib.xml#L157) | [input L157](https://github.com/TheRobotStudio/SO-ARM100/blob/a758567c3978dfeefe282ede0500085a48fe8f78/Simulation/SO101/so101_new_calib.xml#L157) |
| shoulder_pan / force | 2.94 | 3.35 | 3.35 | 0.41 | undocumented derivation difference | [inherited actuator input L38](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/robotstudio_so101/so101.xml#L38) | [input L157](https://github.com/TheRobotStudio/SO-ARM100/blob/aec17bbc256d1a7342d53aaa4950595d4c30b40d/Simulation/SO101/so101_new_calib.xml#L157) | [input L157](https://github.com/TheRobotStudio/SO-ARM100/blob/a758567c3978dfeefe282ede0500085a48fe8f78/Simulation/SO101/so101_new_calib.xml#L157) |
| shoulder_lift / effort | 2.94 | 3.35 | 3.35 | 0.41 | undocumented derivation difference | [inherited actuator input L38](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/robotstudio_so101/so101.xml#L38) | [input L158](https://github.com/TheRobotStudio/SO-ARM100/blob/aec17bbc256d1a7342d53aaa4950595d4c30b40d/Simulation/SO101/so101_new_calib.xml#L158) | [input L158](https://github.com/TheRobotStudio/SO-ARM100/blob/a758567c3978dfeefe282ede0500085a48fe8f78/Simulation/SO101/so101_new_calib.xml#L158) |
| shoulder_lift / force | 2.94 | 3.35 | 3.35 | 0.41 | undocumented derivation difference | [inherited actuator input L38](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/robotstudio_so101/so101.xml#L38) | [input L158](https://github.com/TheRobotStudio/SO-ARM100/blob/aec17bbc256d1a7342d53aaa4950595d4c30b40d/Simulation/SO101/so101_new_calib.xml#L158) | [input L158](https://github.com/TheRobotStudio/SO-ARM100/blob/a758567c3978dfeefe282ede0500085a48fe8f78/Simulation/SO101/so101_new_calib.xml#L158) |
| elbow_flex / effort | 2.94 | 3.35 | 3.35 | 0.41 | undocumented derivation difference | [inherited actuator input L38](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/robotstudio_so101/so101.xml#L38) | [input L159](https://github.com/TheRobotStudio/SO-ARM100/blob/aec17bbc256d1a7342d53aaa4950595d4c30b40d/Simulation/SO101/so101_new_calib.xml#L159) | [input L159](https://github.com/TheRobotStudio/SO-ARM100/blob/a758567c3978dfeefe282ede0500085a48fe8f78/Simulation/SO101/so101_new_calib.xml#L159) |
| elbow_flex / force | 2.94 | 3.35 | 3.35 | 0.41 | undocumented derivation difference | [inherited actuator input L38](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/robotstudio_so101/so101.xml#L38) | [input L159](https://github.com/TheRobotStudio/SO-ARM100/blob/aec17bbc256d1a7342d53aaa4950595d4c30b40d/Simulation/SO101/so101_new_calib.xml#L159) | [input L159](https://github.com/TheRobotStudio/SO-ARM100/blob/a758567c3978dfeefe282ede0500085a48fe8f78/Simulation/SO101/so101_new_calib.xml#L159) |
| wrist_flex / effort | 2.94 | 3.35 | 3.35 | 0.41 | undocumented derivation difference | [inherited actuator input L38](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/robotstudio_so101/so101.xml#L38) | [input L160](https://github.com/TheRobotStudio/SO-ARM100/blob/aec17bbc256d1a7342d53aaa4950595d4c30b40d/Simulation/SO101/so101_new_calib.xml#L160) | [input L160](https://github.com/TheRobotStudio/SO-ARM100/blob/a758567c3978dfeefe282ede0500085a48fe8f78/Simulation/SO101/so101_new_calib.xml#L160) |
| wrist_flex / force | 2.94 | 3.35 | 3.35 | 0.41 | undocumented derivation difference | [inherited actuator input L38](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/robotstudio_so101/so101.xml#L38) | [input L160](https://github.com/TheRobotStudio/SO-ARM100/blob/aec17bbc256d1a7342d53aaa4950595d4c30b40d/Simulation/SO101/so101_new_calib.xml#L160) | [input L160](https://github.com/TheRobotStudio/SO-ARM100/blob/a758567c3978dfeefe282ede0500085a48fe8f78/Simulation/SO101/so101_new_calib.xml#L160) |
| wrist_roll / effort | 2.94 | 3.35 | 3.35 | 0.41 | undocumented derivation difference | [inherited actuator input L38](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/robotstudio_so101/so101.xml#L38) | [input L161](https://github.com/TheRobotStudio/SO-ARM100/blob/aec17bbc256d1a7342d53aaa4950595d4c30b40d/Simulation/SO101/so101_new_calib.xml#L161) | [input L161](https://github.com/TheRobotStudio/SO-ARM100/blob/a758567c3978dfeefe282ede0500085a48fe8f78/Simulation/SO101/so101_new_calib.xml#L161) |
| wrist_roll / force | 2.94 | 3.35 | 3.35 | 0.41 | undocumented derivation difference | [inherited actuator input L38](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/robotstudio_so101/so101.xml#L38) | [input L161](https://github.com/TheRobotStudio/SO-ARM100/blob/aec17bbc256d1a7342d53aaa4950595d4c30b40d/Simulation/SO101/so101_new_calib.xml#L161) | [input L161](https://github.com/TheRobotStudio/SO-ARM100/blob/a758567c3978dfeefe282ede0500085a48fe8f78/Simulation/SO101/so101_new_calib.xml#L161) |
| gripper / effort | 2.94 | 3.35 | 3.35 | 0.41 | undocumented derivation difference | [inherited actuator input L38](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/robotstudio_so101/so101.xml#L38) | [input L162](https://github.com/TheRobotStudio/SO-ARM100/blob/aec17bbc256d1a7342d53aaa4950595d4c30b40d/Simulation/SO101/so101_new_calib.xml#L162) | [input L162](https://github.com/TheRobotStudio/SO-ARM100/blob/a758567c3978dfeefe282ede0500085a48fe8f78/Simulation/SO101/so101_new_calib.xml#L162) |
| gripper / force | 2.94 | 3.35 | 3.35 | 0.41 | undocumented derivation difference | [inherited actuator input L38](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/robotstudio_so101/so101.xml#L38) | [input L162](https://github.com/TheRobotStudio/SO-ARM100/blob/aec17bbc256d1a7342d53aaa4950595d4c30b40d/Simulation/SO101/so101_new_calib.xml#L162) | [input L162](https://github.com/TheRobotStudio/SO-ARM100/blob/a758567c3978dfeefe282ede0500085a48fe8f78/Simulation/SO101/so101_new_calib.xml#L162) |

## Raw CoM records and reporting decisions

Raw values retain the previous root-anchor registration before Kabsch; original world coordinates also remain in the snapshots. Eligible findings above use the fitted transform into M. Excluded raw records below are diagnostic numbers, not findings. No CoM suppression applies to mass or principal inertia moments.

| Entity / quantity | Raw M | Raw S | Raw H | Raw H − M | Decision | M source | S source | H source |
|---|---|---|---|---|---|---|---|---|
| robot / total_com_registered | [0.147133191, 0.00225186317, 0.161538864] | [0.143249358, 0.00121541495, 0.159956569] | [0.143249358, 0.00121541495, 0.159956569] | [-0.00388383234, -0.00103644821, -0.00158229496] | eligible; compared after Kabsch alignment | [aggregate inputs](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/robotstudio_so101/so101.xml#L1) | [aggregate inputs](https://github.com/TheRobotStudio/SO-ARM100/blob/aec17bbc256d1a7342d53aaa4950595d4c30b40d/Simulation/SO101/so101_new_calib.xml#L1) | [aggregate inputs](https://github.com/TheRobotStudio/SO-ARM100/blob/a758567c3978dfeefe282ede0500085a48fe8f78/Simulation/SO101/so101_new_calib.xml#L1) |
| base / com_registered | [0.0137179, -5.19711e-05, 0.0334843] | [0.0137179, -5.19711e-05, 0.0334843] | [0.0137179, -5.19711e-05, 0.0334843] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L86](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/robotstudio_so101/so101.xml#L86) | [CoM/kinematic input L37](https://github.com/TheRobotStudio/SO-ARM100/blob/aec17bbc256d1a7342d53aaa4950595d4c30b40d/Simulation/SO101/so101_new_calib.xml#L37) | [CoM/kinematic input L37](https://github.com/TheRobotStudio/SO-ARM100/blob/a758567c3978dfeefe282ede0500085a48fe8f78/Simulation/SO101/so101_new_calib.xml#L37) |
| shoulder / com_registered | [0.0695957, -1.7e-05, 0.0876713] | [0.0695957, -1.66816766e-05, 0.0876713] | [0.0695957, -1.66816766e-05, 0.0876713] | [1.38777878e-17, 3.1832343e-07, -1.38777878e-17] | eligible; compared after Kabsch alignment | [CoM/kinematic input L106](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/robotstudio_so101/so101.xml#L106) | [CoM/kinematic input L52](https://github.com/TheRobotStudio/SO-ARM100/blob/aec17bbc256d1a7342d53aaa4950595d4c30b40d/Simulation/SO101/so101_new_calib.xml#L52) | [CoM/kinematic input L52](https://github.com/TheRobotStudio/SO-ARM100/blob/a758567c3978dfeefe282ede0500085a48fe8f78/Simulation/SO101/so101_new_calib.xml#L52) |
| upper_arm / com_registered | [0.0776165, 0.0001312, 0.206447] | [0.07761674, 0.000131091023, 0.2064471] | [0.07761674, 0.000131091023, 0.2064471] | [2.4e-07, -1.0897657e-07, 1e-07] | eligible; compared after Kabsch alignment | [CoM/kinematic input L123](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/robotstudio_so101/so101.xml#L123) | [CoM/kinematic input L66](https://github.com/TheRobotStudio/SO-ARM100/blob/aec17bbc256d1a7342d53aaa4950595d4c30b40d/Simulation/SO101/so101_new_calib.xml#L66) | [CoM/kinematic input L66](https://github.com/TheRobotStudio/SO-ARM100/blob/a758567c3978dfeefe282ede0500085a48fe8f78/Simulation/SO101/so101_new_calib.xml#L66) |
| lower_arm / com_registered | [0.1953045, 5.2e-06, 0.2324138] | [0.1953046, 5.29102343e-06, 0.23241376] | [0.1953046, 5.29102343e-06, 0.23241376] | [1e-07, 9.10234304e-08, -4.00000001e-08] | eligible; compared after Kabsch alignment | [CoM/kinematic input L138](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/robotstudio_so101/so101.xml#L138) | [CoM/kinematic input L78](https://github.com/TheRobotStudio/SO-ARM100/blob/aec17bbc256d1a7342d53aaa4950595d4c30b40d/Simulation/SO101/so101_new_calib.xml#L78) | [CoM/kinematic input L78](https://github.com/TheRobotStudio/SO-ARM100/blob/a758567c3978dfeefe282ede0500085a48fe8f78/Simulation/SO101/so101_new_calib.xml#L78) |
| wrist / com_registered | [0.2707488, 0.0098378, 0.234473312] | [0.2707488, 0.00983779102, 0.234473312] | [0.2707488, 0.00983779102, 0.234473312] | [1.66533454e-16, -8.97656944e-09, -1.66533454e-16] | eligible; compared after Kabsch alignment | [CoM/kinematic input L155](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/robotstudio_so101/so101.xml#L155) | [CoM/kinematic input L92](https://github.com/TheRobotStudio/SO-ARM100/blob/aec17bbc256d1a7342d53aaa4950595d4c30b40d/Simulation/SO101/so101_new_calib.xml#L92) | [CoM/kinematic input L92](https://github.com/TheRobotStudio/SO-ARM100/blob/a758567c3978dfeefe282ede0500085a48fe8f78/Simulation/SO101/so101_new_calib.xml#L92) |
| gripper / com_registered | [0.3184215, 5.64964673e-05, 0.234595668] | [0.3184215, 5.66434776e-05, 0.234595302] | [0.3184215, 5.66434776e-05, 0.234595302] | [1.66533454e-16, 1.47010243e-07, -3.65843019e-07] | eligible; compared after Kabsch alignment | [CoM/kinematic input L169](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/robotstudio_so101/so101.xml#L169) | [CoM/kinematic input L103](https://github.com/TheRobotStudio/SO-ARM100/blob/aec17bbc256d1a7342d53aaa4950595d4c30b40d/Simulation/SO101/so101_new_calib.xml#L103) | [CoM/kinematic input L103](https://github.com/TheRobotStudio/SO-ARM100/blob/a758567c3978dfeefe282ede0500085a48fe8f78/Simulation/SO101/so101_new_calib.xml#L103) |
| moving_jaw_so101_v1 / com_registered | [0.3466589, -0.00155903464, 0.252949799] | [0.3466589, -0.00155904613, 0.25294985] | [0.3466589, -0.00155904613, 0.25294985] | [8.25720603e-11, -1.14861815e-08, 5.15130318e-08] | eligible; compared after Kabsch alignment | [CoM/kinematic input L224](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/robotstudio_so101/so101.xml#L224) | [CoM/kinematic input L116](https://github.com/TheRobotStudio/SO-ARM100/blob/aec17bbc256d1a7342d53aaa4950595d4c30b40d/Simulation/SO101/so101_new_calib.xml#L116) | [CoM/kinematic input L116](https://github.com/TheRobotStudio/SO-ARM100/blob/a758567c3978dfeefe282ede0500085a48fe8f78/Simulation/SO101/so101_new_calib.xml#L116) |

## Mass accounting

Every contributing compiled body mass is listed here so total/subtree sums can be checked. Links point to explicit inertials or to geometry inputs when the compiler inferred a mass. CoM links identify inertial inputs; world coordinates additionally use the ancestor transforms and the registration recorded below.

| M body | M kg / source | S kg / source | H kg / source |
|---|---|---|---|
| base | 0.147 / [input L86](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/robotstudio_so101/so101.xml#L86) | 0.147 / [input L37](https://github.com/TheRobotStudio/SO-ARM100/blob/aec17bbc256d1a7342d53aaa4950595d4c30b40d/Simulation/SO101/so101_new_calib.xml#L37) | 0.147 / [input L37](https://github.com/TheRobotStudio/SO-ARM100/blob/a758567c3978dfeefe282ede0500085a48fe8f78/Simulation/SO101/so101_new_calib.xml#L37) |
| shoulder | 0.100006 / [input L106](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/robotstudio_so101/so101.xml#L106) | 0.100006 / [input L52](https://github.com/TheRobotStudio/SO-ARM100/blob/aec17bbc256d1a7342d53aaa4950595d4c30b40d/Simulation/SO101/so101_new_calib.xml#L52) | 0.100006 / [input L52](https://github.com/TheRobotStudio/SO-ARM100/blob/a758567c3978dfeefe282ede0500085a48fe8f78/Simulation/SO101/so101_new_calib.xml#L52) |
| upper_arm | 0.103 / [input L123](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/robotstudio_so101/so101.xml#L123) | 0.103 / [input L66](https://github.com/TheRobotStudio/SO-ARM100/blob/aec17bbc256d1a7342d53aaa4950595d4c30b40d/Simulation/SO101/so101_new_calib.xml#L66) | 0.103 / [input L66](https://github.com/TheRobotStudio/SO-ARM100/blob/a758567c3978dfeefe282ede0500085a48fe8f78/Simulation/SO101/so101_new_calib.xml#L66) |
| lower_arm | 0.104 / [input L138](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/robotstudio_so101/so101.xml#L138) | 0.104 / [input L78](https://github.com/TheRobotStudio/SO-ARM100/blob/aec17bbc256d1a7342d53aaa4950595d4c30b40d/Simulation/SO101/so101_new_calib.xml#L78) | 0.104 / [input L78](https://github.com/TheRobotStudio/SO-ARM100/blob/a758567c3978dfeefe282ede0500085a48fe8f78/Simulation/SO101/so101_new_calib.xml#L78) |
| wrist | 0.079 / [input L155](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/robotstudio_so101/so101.xml#L155) | 0.079 / [input L92](https://github.com/TheRobotStudio/SO-ARM100/blob/aec17bbc256d1a7342d53aaa4950595d4c30b40d/Simulation/SO101/so101_new_calib.xml#L92) | 0.079 / [input L92](https://github.com/TheRobotStudio/SO-ARM100/blob/a758567c3978dfeefe282ede0500085a48fe8f78/Simulation/SO101/so101_new_calib.xml#L92) |
| gripper | 0.087 / [input L169](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/robotstudio_so101/so101.xml#L169) | 0.087 / [input L103](https://github.com/TheRobotStudio/SO-ARM100/blob/aec17bbc256d1a7342d53aaa4950595d4c30b40d/Simulation/SO101/so101_new_calib.xml#L103) | 0.087 / [input L103](https://github.com/TheRobotStudio/SO-ARM100/blob/a758567c3978dfeefe282ede0500085a48fe8f78/Simulation/SO101/so101_new_calib.xml#L103) |
| camera_mount | 0.013444 / [geometry/inference input L203](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/robotstudio_so101/so101.xml#L203) | unavailable | unmatched |
| moving_jaw_so101_v1 | 0.012 / [input L224](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/robotstudio_so101/so101.xml#L224) | 0.012 / [input L116](https://github.com/TheRobotStudio/SO-ARM100/blob/aec17bbc256d1a7342d53aaa4950595d4c30b40d/Simulation/SO101/so101_new_calib.xml#L116) | 0.012 / [input L116](https://github.com/TheRobotStudio/SO-ARM100/blob/a758567c3978dfeefe282ede0500085a48fe8f78/Simulation/SO101/so101_new_calib.xml#L116) |

## Coverage and unmatched elements

```json
{
  "mapping_h": {
    "bodies": {
      "base": "base",
      "shoulder": "shoulder",
      "upper_arm": "upper_arm",
      "lower_arm": "lower_arm",
      "wrist": "wrist",
      "gripper": "gripper",
      "moving_jaw_so101_v1": "moving_jaw_so101_v1"
    },
    "joints": {
      "shoulder_pan": "shoulder_pan",
      "shoulder_lift": "shoulder_lift",
      "elbow_flex": "elbow_flex",
      "wrist_flex": "wrist_flex",
      "wrist_roll": "wrist_roll",
      "gripper": "gripper"
    },
    "body_methods": {
      "base": "name",
      "shoulder": "name",
      "upper_arm": "name",
      "lower_arm": "name",
      "wrist": "name",
      "gripper": "name",
      "moving_jaw_so101_v1": "name"
    },
    "joint_methods": {
      "shoulder_pan": "name",
      "shoulder_lift": "name",
      "elbow_flex": "name",
      "wrist_flex": "name",
      "wrist_roll": "name",
      "gripper": "name"
    },
    "unmatched_m_bodies": [
      "camera_mount"
    ],
    "unmatched_upstream_bodies": [],
    "unmatched_m_joints": [],
    "unmatched_upstream_joints": [],
    "registration_anchor": {
      "M": "base",
      "H": "base",
      "root_unmatched": false
    }
  },
  "mapping_s": {
    "bodies": {
      "base": "base",
      "shoulder": "shoulder",
      "upper_arm": "upper_arm",
      "lower_arm": "lower_arm",
      "wrist": "wrist",
      "gripper": "gripper",
      "moving_jaw_so101_v1": "moving_jaw_so101_v1"
    },
    "joints": {
      "shoulder_pan": "shoulder_pan",
      "shoulder_lift": "shoulder_lift",
      "elbow_flex": "elbow_flex",
      "wrist_flex": "wrist_flex",
      "wrist_roll": "wrist_roll",
      "gripper": "gripper"
    },
    "body_methods": {
      "base": "name",
      "shoulder": "name",
      "upper_arm": "name",
      "lower_arm": "name",
      "wrist": "name",
      "gripper": "name",
      "moving_jaw_so101_v1": "name"
    },
    "joint_methods": {
      "shoulder_pan": "name",
      "shoulder_lift": "name",
      "elbow_flex": "name",
      "wrist_flex": "name",
      "wrist_roll": "name",
      "gripper": "name"
    },
    "unmatched_m_bodies": [
      "camera_mount"
    ],
    "unmatched_upstream_bodies": [],
    "unmatched_m_joints": [],
    "unmatched_upstream_joints": [],
    "registration_anchor": {
      "M": "base",
      "S": "base"
    }
  },
  "unavailable": [
    {
      "entity": "shoulder_pan",
      "other_entity": "shoulder_pan",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "shoulder_lift",
      "other_entity": "shoulder_lift",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "elbow_flex",
      "other_entity": "elbow_flex",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "wrist_flex",
      "other_entity": "wrist_flex",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "wrist_roll",
      "other_entity": "wrist_roll",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "gripper",
      "other_entity": "gripper",
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
| shoulder_pan / velocity | unavailable | unavailable | unavailable |
| shoulder_lift / velocity | unavailable | unavailable | unavailable |
| elbow_flex / velocity | unavailable | unavailable | unavailable |
| wrist_flex / velocity | unavailable | unavailable | unavailable |
| wrist_roll / velocity | unavailable | unavailable | unavailable |
| gripper / velocity | unavailable | unavailable | unavailable |
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
    "file": "robotstudio_so101/so101.xml",
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
      "undocumented derivation difference": 20
    },
    "classifications_changed": 0,
    "finding_membership_changes": 0
  },
  "2": {
    "provenance_method": "pinned",
    "counts": {
      "undocumented derivation difference": 20
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
      "camera_mount"
    ],
    "assets_loaded": 18,
    "mesh_conversions": [],
    "xacro_arguments": {},
    "source_dependencies": [
      "robotstudio_so101/so101.xml"
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
      "Simulation/SO101/so101_new_calib.xml"
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
  "S": {
    "geometry_stripped": true,
    "missing_explicit_inertials": [],
    "assets_loaded": 0,
    "mesh_conversions": [],
    "xacro_arguments": {},
    "source_dependencies": [
      "Simulation/SO101/so101_new_calib.xml"
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
  "historical_snapshots_reused": 6,
  "primary_physics_unchanged": true,
  "source_matching": "original raw-value provenance criteria retained; kinematic guard applies to reported CoM"
}
```
