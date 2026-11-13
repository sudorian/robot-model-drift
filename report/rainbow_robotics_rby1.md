# rainbow_robotics_rby1

Status: **complete**. Provenance: **none**, confidence **none**.

No public revision matches all comparable quantities. Class: NO MATCHING SOURCE; never counted as STALE.

M: `https://github.com/google-deepmind/mujoco_menagerie`, `rainbow_robotics_rby1/rby1a_1.2_no_gripper.xml`, commit `370c43965323c0944b433b202aac5058b5f907a9`.
H: `https://github.com/RainbowRobotics/rby1-sdk`, `models/rby1a/urdf/model.urdf`, commit `300a585c297d1bdf8554312c3a1659610a9823f5`.
S: unavailable. A machine-readable H can still be compared to M; no-match differences are never counted as STALE.

Limit semantics: MJCF effort values are supported actuator torque/force envelopes. URDF effort and velocity values are manufacturer declarations retained from XML; MuJoCo does not enforce those tags. Such declaration comparisons are explicitly distinct from compiled inertial/range quantities.


## Source evidence

```json
[
  {
    "url": "https://github.com/RainbowRobotics/rby1-sdk/blob/main/models/rby1a/urdf/model.urdf",
    "document": "rainbow_robotics_rby1/README.md",
    "commit": "370c43965323c0944b433b202aac5058b5f907a9",
    "current": true
  },
  {
    "url": "https://github.com/RainbowRobotics",
    "document": "rainbow_robotics_rby1/README.md",
    "commit": "2af6ce4e9cdaf9b12d3b7097571bd440ab9adfc8",
    "current": false
  },
  {
    "url": "https://github.com/kevinzakka/obj2mjcf",
    "document": "rainbow_robotics_rby1/README.md",
    "commit": "2af6ce4e9cdaf9b12d3b7097571bd440ab9adfc8",
    "current": false
  }
]
```


## README derivation evidence

Documentation labels are conservative: an automated documented label requires an explicit affected entity and quantity. Broader conversion notes are retained here for review.

> - configured wheel/torso/arm/head/gripper actuators and control ranges

## Kinematics consistency

A proper Kabsch rigid transform aligns all matched zero-pose body origins. The maximum per-origin residual and signed hinge/slide axis angles determine whether CoM can be compared; RMS is also recorded. Fewer than three non-collinear origins give insufficient kinematic coverage. CoM records that fail either required M/H or M/S check are excluded from counts and largest discrepancies. Masses, principal moments and raw joint ranges remain unchanged; a flagged range still requires convention review.

| Pair | Status | Origins / rank | RMS / maximum mm | Disagreeing / checked axes |
|---|---|---:|---:|---:|
| M/H | kinematic convention differs | 25 / 3 | 16.2775033 / 55.1996971 | 2 / 24 |

Exact fitted transforms, per-origin residuals, thresholds and axis vectors:

```json
{
  "M/H": {
    "status": "kinematic convention differs",
    "matched_body_origins": 25,
    "position_threshold_m": 0.005,
    "axis_threshold_rad": 0.005,
    "residual_definition": "maximum Euclidean residual over matched body origins; Kabsch minimizes RMS, which is also recorded",
    "coordinate_frames": "each snapshot registered to its matched report anchor",
    "anchor_m": "base",
    "anchor_other": "base",
    "rotation_other_to_m": [
      [
        0.9999999999390365,
        -4.532932961622305e-11,
        1.1042087355457115e-05
      ],
      [
        4.5327956244349395e-11,
        1.0000000000000002,
        1.2185018639153624e-10
      ],
      [
        -1.1042087355819796e-05,
        -1.2184938513461863e-10,
        0.9999999999390363
      ]
    ],
    "translation_other_to_m": [
      -1.0131523020748268e-05,
      -1.1282103449030639e-10,
      0.00480054621565984
    ],
    "rms_residual_m": 0.016277503326059022,
    "max_residual_m": 0.05519969710148168,
    "fit_rank": 3,
    "axis_checks": [
      {
        "joint_m": "right_wheel",
        "joint_other": "right_wheel",
        "axis_m": [
          0.0,
          1.0,
          0.0
        ],
        "axis_other_aligned": [
          4.5329329616223035e-11,
          -1.0,
          1.218493851346186e-10
        ],
        "angle_rad": 3.1415926534597856,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "left_wheel",
        "joint_other": "left_wheel",
        "axis_m": [
          0.0,
          1.0,
          0.0
        ],
        "axis_other_aligned": [
          4.5329329616223035e-11,
          -1.0,
          1.218493851346186e-10
        ],
        "angle_rad": 3.1415926534597856,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "torso_0",
        "joint_other": "torso_0",
        "axis_m": [
          1.0,
          0.0,
          0.0
        ],
        "axis_other_aligned": [
          0.9999999999390361,
          4.5327956244349375e-11,
          -1.1042087355819791e-05
        ],
        "angle_rad": 1.1042087356137215e-05,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "torso_1",
        "joint_other": "torso_1",
        "axis_m": [
          0.0,
          1.0,
          0.0
        ],
        "axis_other_aligned": [
          -4.5329329616223035e-11,
          1.0,
          -1.218493851346186e-10
        ],
        "angle_rad": 1.3000777200283377e-10,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "torso_2",
        "joint_other": "torso_2",
        "axis_m": [
          0.0,
          1.0,
          0.0
        ],
        "axis_other_aligned": [
          -4.5329329616223035e-11,
          1.0,
          -1.218493851346186e-10
        ],
        "angle_rad": 1.3000777200283377e-10,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "torso_3",
        "joint_other": "torso_3",
        "axis_m": [
          0.0,
          1.0,
          0.0
        ],
        "axis_other_aligned": [
          -4.5329329616223035e-11,
          1.0,
          -1.218493851346186e-10
        ],
        "angle_rad": 1.3000777200283377e-10,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "torso_4",
        "joint_other": "torso_4",
        "axis_m": [
          1.0,
          0.0,
          0.0
        ],
        "axis_other_aligned": [
          0.9999999999390361,
          4.5327956244349375e-11,
          -1.1042087355819791e-05
        ],
        "angle_rad": 1.1042087356137215e-05,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "torso_5",
        "joint_other": "torso_5",
        "axis_m": [
          0.0,
          0.0,
          1.0
        ],
        "axis_other_aligned": [
          1.1042087355457114e-05,
          1.218501863915362e-10,
          0.9999999999390361
        ],
        "angle_rad": 1.1042087356353815e-05,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "right_arm_0",
        "joint_other": "right_arm_0",
        "axis_m": [
          0.0,
          0.9396927698085815,
          -0.3420197338889618
        ],
        "axis_other_aligned": [
          -3.7766588659270347e-06,
          0.9396926217211488,
          -0.3420201407352655
        ],
        "angle_rad": 3.8013952691334228e-06,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "right_arm_1",
        "joint_other": "right_arm_1",
        "axis_m": [
          1.0,
          0.0,
          0.0
        ],
        "axis_other_aligned": [
          0.9999999999390361,
          4.5327956244349375e-11,
          -1.1042087355819791e-05
        ],
        "angle_rad": 1.1042087356137215e-05,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "right_arm_2",
        "joint_other": "right_arm_2",
        "axis_m": [
          0.0,
          -6.281291979363405e-18,
          1.0
        ],
        "axis_other_aligned": [
          1.1042087355457114e-05,
          1.218501863915362e-10,
          0.9999999999390361
        ],
        "angle_rad": 1.1042087356353815e-05,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "right_arm_3",
        "joint_other": "right_arm_3",
        "axis_m": [
          0.0,
          1.0,
          6.281291979363405e-18
        ],
        "axis_other_aligned": [
          -4.5329329616223035e-11,
          1.0,
          -1.218493851346186e-10
        ],
        "angle_rad": 1.3000777788995543e-10,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "right_arm_4",
        "joint_other": "right_arm_4",
        "axis_m": [
          0.0,
          -6.281291979363405e-18,
          1.0
        ],
        "axis_other_aligned": [
          1.1042087355457114e-05,
          1.218501863915362e-10,
          0.9999999999390361
        ],
        "angle_rad": 1.1042087356353815e-05,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "right_arm_5",
        "joint_other": "right_arm_5",
        "axis_m": [
          0.0,
          1.0,
          6.281291979363405e-18
        ],
        "axis_other_aligned": [
          -4.5329329616223035e-11,
          1.0,
          -1.218493851346186e-10
        ],
        "angle_rad": 1.3000777788995543e-10,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "right_arm_6",
        "joint_other": "right_arm_6",
        "axis_m": [
          0.0,
          -6.281291979363405e-18,
          1.0
        ],
        "axis_other_aligned": [
          1.1042087355457114e-05,
          1.218501863915362e-10,
          0.9999999999390361
        ],
        "angle_rad": 1.1042087356353815e-05,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "left_arm_0",
        "joint_other": "left_arm_0",
        "axis_m": [
          0.0,
          0.9396927698085815,
          0.3420197338889618
        ],
        "axis_other_aligned": [
          3.776573674653855e-06,
          0.9396926218044992,
          0.34202014050626356
        ],
        "angle_rad": 3.8012828832585337e-06,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "left_arm_1",
        "joint_other": "left_arm_1",
        "axis_m": [
          1.0,
          0.0,
          0.0
        ],
        "axis_other_aligned": [
          0.9999999999390361,
          4.5327956244349375e-11,
          -1.1042087355819791e-05
        ],
        "angle_rad": 1.1042087356137215e-05,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "left_arm_2",
        "joint_other": "left_arm_2",
        "axis_m": [
          0.0,
          6.281291979363405e-18,
          1.0
        ],
        "axis_other_aligned": [
          1.1042087355457114e-05,
          1.218501863915362e-10,
          0.9999999999390361
        ],
        "angle_rad": 1.1042087356353815e-05,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "left_arm_3",
        "joint_other": "left_arm_3",
        "axis_m": [
          0.0,
          1.0,
          -6.281291979363405e-18
        ],
        "axis_other_aligned": [
          -4.5329329616223035e-11,
          1.0,
          -1.218493851346186e-10
        ],
        "angle_rad": 1.3000776611571216e-10,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "left_arm_4",
        "joint_other": "left_arm_4",
        "axis_m": [
          0.0,
          6.281291979363405e-18,
          1.0
        ],
        "axis_other_aligned": [
          1.1042087355457114e-05,
          1.218501863915362e-10,
          0.9999999999390361
        ],
        "angle_rad": 1.1042087356353815e-05,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "left_arm_5",
        "joint_other": "left_arm_5",
        "axis_m": [
          0.0,
          1.0,
          -6.281291979363405e-18
        ],
        "axis_other_aligned": [
          -4.5329329616223035e-11,
          1.0,
          -1.218493851346186e-10
        ],
        "angle_rad": 1.3000776611571216e-10,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "left_arm_6",
        "joint_other": "left_arm_6",
        "axis_m": [
          0.0,
          6.281291979363405e-18,
          1.0
        ],
        "axis_other_aligned": [
          1.1042087355457114e-05,
          1.218501863915362e-10,
          0.9999999999390361
        ],
        "angle_rad": 1.1042087356353815e-05,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "head_0",
        "joint_other": "head_0",
        "axis_m": [
          0.0,
          0.0,
          1.0
        ],
        "axis_other_aligned": [
          1.1042087355457114e-05,
          1.218501863915362e-10,
          0.9999999999390361
        ],
        "angle_rad": 1.1042087356353815e-05,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "head_1",
        "joint_other": "head_1",
        "axis_m": [
          0.0,
          1.0,
          0.0
        ],
        "axis_other_aligned": [
          -4.5329329616223035e-11,
          1.0,
          -1.218493851346186e-10
        ],
        "angle_rad": 1.3000777200283377e-10,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      }
    ],
    "axis_disagreements": [
      {
        "joint_m": "right_wheel",
        "joint_other": "right_wheel",
        "axis_m": [
          0.0,
          1.0,
          0.0
        ],
        "axis_other_aligned": [
          4.5329329616223035e-11,
          -1.0,
          1.218493851346186e-10
        ],
        "angle_rad": 3.1415926534597856,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "left_wheel",
        "joint_other": "left_wheel",
        "axis_m": [
          0.0,
          1.0,
          0.0
        ],
        "axis_other_aligned": [
          4.5329329616223035e-11,
          -1.0,
          1.218493851346186e-10
        ],
        "angle_rad": 3.1415926534597856,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      }
    ],
    "com_eligible": false,
    "covariance_singular_values": [
      5.157281322978045,
      0.8180500000000002,
      0.07148118352166487
    ],
    "origin_residuals_m": {
      "base": 0.004800556906906192,
      "wheel_r": 0.004798037138212244,
      "wheel_l": 0.004798037073677385,
      "link_torso_0": 0.0048005513521594935,
      "link_torso_1": 0.0048005513521594935,
      "link_torso_2": 0.004800547223524697,
      "link_torso_3": 0.0048005462062296455,
      "link_torso_4": 0.0048005462062296455,
      "link_torso_5": 0.004800096359257508,
      "link_right_arm_0": 0.004800048759075157,
      "link_right_arm_1": 0.004800048759075157,
      "link_right_arm_2": 0.004800048759075157,
      "link_right_arm_3": 0.00479970426658538,
      "link_right_arm_4": 0.004800046271723667,
      "link_right_arm_5": 0.004800046271723667,
      "link_right_arm_6": 0.004800046271723667,
      "link_left_arm_0": 0.0048000491664403075,
      "link_left_arm_1": 0.0048000491664403075,
      "link_left_arm_2": 0.0048000491664403075,
      "link_left_arm_3": 0.0047997046739633765,
      "link_left_arm_4": 0.004800046679113433,
      "link_left_arm_5": 0.004800046679113433,
      "link_left_arm_6": 0.004800046679113433,
      "link_head_1": 0.05519969710148168,
      "link_head_2": 0.05519969710148168
    },
    "reason": "Origin residual exceeds threshold and/or matched signed joint axes disagree"
  }
}
```


## Every reported quantity difference

Counts are quantity records, including correlated total/subtree/body mass records; they are not independent robot defects.

| Entity / quantity | M | S | H | H − M | Class | M source | S source | H source |
|---|---|---|---|---|---|---|---|---|
| robot / total_mass | 127.657602 | unavailable | 128.470988 | 0.81338632 | NO MATCHING SOURCE | [aggregate inputs](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/rainbow_robotics_rby1/rby1a_1.2_no_gripper.xml#L1) | unavailable | [aggregate inputs](https://github.com/RainbowRobotics/rby1-sdk/blob/300a585c297d1bdf8554312c3a1659610a9823f5/models/rby1a/urdf/model.urdf#L1) |
| base / subtree_mass | 127.657602 | unavailable | 128.470988 | 0.81338632 | NO MATCHING SOURCE | [subtree root L99](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/rainbow_robotics_rby1/rby1a_1.2_no_gripper.xml#L99) | unavailable | [subtree root L6](https://github.com/RainbowRobotics/rby1-sdk/blob/300a585c297d1bdf8554312c3a1659610a9823f5/models/rby1a/urdf/model.urdf#L6) |
| link_torso_0 / subtree_mass | 64.8215219 | unavailable | 65.6348871 | 0.81336521 | NO MATCHING SOURCE | [subtree root L125](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/rainbow_robotics_rby1/rby1a_1.2_no_gripper.xml#L125) | unavailable | [subtree root L49](https://github.com/RainbowRobotics/rby1-sdk/blob/300a585c297d1bdf8554312c3a1659610a9823f5/models/rby1a/urdf/model.urdf#L49) |
| link_torso_1 / subtree_mass | 62.5787019 | unavailable | 63.3920659 | 0.81336398 | NO MATCHING SOURCE | [subtree root L132](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/rainbow_robotics_rby1/rby1a_1.2_no_gripper.xml#L132) | unavailable | [subtree root L72](https://github.com/RainbowRobotics/rby1-sdk/blob/300a585c297d1bdf8554312c3a1659610a9823f5/models/rby1a/urdf/model.urdf#L72) |
| link_torso_2 / subtree_mass | 52.8570719 | unavailable | 53.6704391 | 0.81336722 | NO MATCHING SOURCE | [subtree root L141](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/rainbow_robotics_rby1/rby1a_1.2_no_gripper.xml#L141) | unavailable | [subtree root L95](https://github.com/RainbowRobotics/rby1-sdk/blob/300a585c297d1bdf8554312c3a1659610a9823f5/models/rby1a/urdf/model.urdf#L95) |
| link_torso_3 / subtree_mass | 43.6401519 | unavailable | 44.4535206 | 0.81336872 | NO MATCHING SOURCE | [subtree root L150](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/rainbow_robotics_rby1/rby1a_1.2_no_gripper.xml#L150) | unavailable | [subtree root L118](https://github.com/RainbowRobotics/rby1-sdk/blob/300a585c297d1bdf8554312c3a1659610a9823f5/models/rby1a/urdf/model.urdf#L118) |
| link_torso_4 / subtree_mass | 39.4533619 | unavailable | 40.2667287 | 0.81336676 | NO MATCHING SOURCE | [subtree root L156](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/rainbow_robotics_rby1/rby1a_1.2_no_gripper.xml#L156) | unavailable | [subtree root L133](https://github.com/RainbowRobotics/rby1-sdk/blob/300a585c297d1bdf8554312c3a1659610a9823f5/models/rby1a/urdf/model.urdf#L133) |
| link_torso_5 / mass | 12.6659 | unavailable | 12.5901234 | -0.07577659 | NO MATCHING SOURCE | [input L165](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/rainbow_robotics_rby1/rby1a_1.2_no_gripper.xml#L165) | unavailable | [input L159](https://github.com/RainbowRobotics/rby1-sdk/blob/300a585c297d1bdf8554312c3a1659610a9823f5/models/rby1a/urdf/model.urdf#L159) |
| link_torso_5 / subtree_mass | 34.9977019 | unavailable | 35.8110659 | 0.813364 | NO MATCHING SOURCE | [subtree root L163](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/rainbow_robotics_rby1/rby1a_1.2_no_gripper.xml#L163) | unavailable | [subtree root L157](https://github.com/RainbowRobotics/rby1-sdk/blob/300a585c297d1bdf8554312c3a1659610a9823f5/models/rby1a/urdf/model.urdf#L157) |
| link_right_arm_0 / subtree_mass | 10.7091337 | unavailable | 11.5173809 | 0.80824719 | NO MATCHING SOURCE | [subtree root L185](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/rainbow_robotics_rby1/rby1a_1.2_no_gripper.xml#L185) | unavailable | [subtree root L180](https://github.com/RainbowRobotics/rby1-sdk/blob/300a585c297d1bdf8554312c3a1659610a9823f5/models/rby1a/urdf/model.urdf#L180) |
| link_right_arm_1 / subtree_mass | 9.44749373 | unavailable | 10.2557385 | 0.80824477 | NO MATCHING SOURCE | [subtree root L193](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/rainbow_robotics_rby1/rby1a_1.2_no_gripper.xml#L193) | unavailable | [subtree root L202](https://github.com/RainbowRobotics/rby1-sdk/blob/300a585c297d1bdf8554312c3a1659610a9823f5/models/rby1a/urdf/model.urdf#L202) |
| link_right_arm_2 / subtree_mass | 7.17462373 | unavailable | 7.98286819 | 0.80824446 | NO MATCHING SOURCE | [subtree root L200](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/rainbow_robotics_rby1/rby1a_1.2_no_gripper.xml#L200) | unavailable | [subtree root L225](https://github.com/RainbowRobotics/rby1-sdk/blob/300a585c297d1bdf8554312c3a1659610a9823f5/models/rby1a/urdf/model.urdf#L225) |
| link_right_arm_3 / subtree_mass | 4.70553373 | unavailable | 5.5137738 | 0.80824007 | NO MATCHING SOURCE | [subtree root L210](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/rainbow_robotics_rby1/rby1a_1.2_no_gripper.xml#L210) | unavailable | [subtree root L248](https://github.com/RainbowRobotics/rby1-sdk/blob/300a585c297d1bdf8554312c3a1659610a9823f5/models/rby1a/urdf/model.urdf#L248) |
| link_right_arm_4 / subtree_mass | 2.44454373 | unavailable | 3.25277887 | 0.80823514 | NO MATCHING SOURCE | [subtree root L219](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/rainbow_robotics_rby1/rby1a_1.2_no_gripper.xml#L219) | unavailable | [subtree root L271](https://github.com/RainbowRobotics/rby1-sdk/blob/300a585c297d1bdf8554312c3a1659610a9823f5/models/rby1a/urdf/model.urdf#L271) |
| link_right_arm_5 / subtree_mass | 2.01945673 | unavailable | 2.82769177 | 0.80823504 | NO MATCHING SOURCE | [subtree root L226](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/rainbow_robotics_rby1/rby1a_1.2_no_gripper.xml#L226) | unavailable | [subtree root L293](https://github.com/RainbowRobotics/rby1-sdk/blob/300a585c297d1bdf8554312c3a1659610a9823f5/models/rby1a/urdf/model.urdf#L293) |
| link_right_arm_6 / mass | 0.42751673 | unavailable | 0.21137279 | -0.21614394 | NO MATCHING SOURCE | [input L239](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/rainbow_robotics_rby1/rby1a_1.2_no_gripper.xml#L239) | unavailable | [input L318](https://github.com/RainbowRobotics/rby1-sdk/blob/300a585c297d1bdf8554312c3a1659610a9823f5/models/rby1a/urdf/model.urdf#L318) |
| link_right_arm_6 / subtree_mass | 0.42751673 | unavailable | 1.23574782 | 0.80823109 | NO MATCHING SOURCE | [subtree root L237](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/rainbow_robotics_rby1/rby1a_1.2_no_gripper.xml#L237) | unavailable | [subtree root L316](https://github.com/RainbowRobotics/rby1-sdk/blob/300a585c297d1bdf8554312c3a1659610a9823f5/models/rby1a/urdf/model.urdf#L316) |
| link_right_arm_6 / principal_moments | [0.000295799701, 0.000306800493, 0.000489499806] | unavailable | [0.000134519712, 0.000145103152, 0.000254327137] | [-0.000161279989, -0.000161697341, -0.00023517267] | NO MATCHING SOURCE | [inertia input L239](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/rainbow_robotics_rby1/rby1a_1.2_no_gripper.xml#L239) | unavailable | [inertia input L321](https://github.com/RainbowRobotics/rby1-sdk/blob/300a585c297d1bdf8554312c3a1659610a9823f5/models/rby1a/urdf/model.urdf#L321) |
| link_left_arm_0 / subtree_mass | 9.96527616 | unavailable | 11.5173809 | 1.55210476 | NO MATCHING SOURCE | [subtree root L253](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/rainbow_robotics_rby1/rby1a_1.2_no_gripper.xml#L253) | unavailable | [subtree root L331](https://github.com/RainbowRobotics/rby1-sdk/blob/300a585c297d1bdf8554312c3a1659610a9823f5/models/rby1a/urdf/model.urdf#L331) |
| link_left_arm_1 / mass | 1.88139 | unavailable | 2.27287031 | 0.39148031 | NO MATCHING SOURCE | [input L263](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/rainbow_robotics_rby1/rby1a_1.2_no_gripper.xml#L263) | unavailable | [input L355](https://github.com/RainbowRobotics/rby1-sdk/blob/300a585c297d1bdf8554312c3a1659610a9823f5/models/rby1a/urdf/model.urdf#L355) |
| link_left_arm_1 / subtree_mass | 8.70363616 | unavailable | 10.2557385 | 1.55210234 | NO MATCHING SOURCE | [subtree root L261](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/rainbow_robotics_rby1/rby1a_1.2_no_gripper.xml#L261) | unavailable | [subtree root L353](https://github.com/RainbowRobotics/rby1-sdk/blob/300a585c297d1bdf8554312c3a1659610a9823f5/models/rby1a/urdf/model.urdf#L353) |
| link_left_arm_1 / principal_moments | [0.0022966, 0.00296561, 0.00355382] | unavailable | [0.00286406973, 0.00389783733, 0.00447674293] | [0.000567469731, 0.000932227335, 0.000922922934] | NO MATCHING SOURCE | [inertia input L263](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/rainbow_robotics_rby1/rby1a_1.2_no_gripper.xml#L263) | unavailable | [inertia input L358](https://github.com/RainbowRobotics/rby1-sdk/blob/300a585c297d1bdf8554312c3a1659610a9823f5/models/rby1a/urdf/model.urdf#L358) |
| link_left_arm_2 / mass | 2.35634 | unavailable | 2.46909439 | 0.11275439 | NO MATCHING SOURCE | [input L271](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/rainbow_robotics_rby1/rby1a_1.2_no_gripper.xml#L271) | unavailable | [input L377](https://github.com/RainbowRobotics/rby1-sdk/blob/300a585c297d1bdf8554312c3a1659610a9823f5/models/rby1a/urdf/model.urdf#L377) |
| link_left_arm_2 / subtree_mass | 6.82224616 | unavailable | 7.98286819 | 1.16062203 | NO MATCHING SOURCE | [subtree root L268](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/rainbow_robotics_rby1/rby1a_1.2_no_gripper.xml#L268) | unavailable | [subtree root L375](https://github.com/RainbowRobotics/rby1-sdk/blob/300a585c297d1bdf8554312c3a1659610a9823f5/models/rby1a/urdf/model.urdf#L375) |
| link_left_arm_2 / principal_moments | [0.00293109, 0.00802394, 0.00845197] | unavailable | [0.00322201929, 0.00928024359, 0.00984469712] | [0.000290929294, 0.00125630359, 0.00139272712] | NO MATCHING SOURCE | [inertia input L271](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/rainbow_robotics_rby1/rby1a_1.2_no_gripper.xml#L271) | unavailable | [inertia input L380](https://github.com/RainbowRobotics/rby1-sdk/blob/300a585c297d1bdf8554312c3a1659610a9823f5/models/rby1a/urdf/model.urdf#L380) |
| link_left_arm_3 / mass | 2.00906 | unavailable | 2.26099493 | 0.25193493 | NO MATCHING SOURCE | [input L281](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/rainbow_robotics_rby1/rby1a_1.2_no_gripper.xml#L281) | unavailable | [input L399](https://github.com/RainbowRobotics/rby1-sdk/blob/300a585c297d1bdf8554312c3a1659610a9823f5/models/rby1a/urdf/model.urdf#L399) |
| link_left_arm_3 / subtree_mass | 4.46590616 | unavailable | 5.5137738 | 1.04786764 | NO MATCHING SOURCE | [subtree root L279](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/rainbow_robotics_rby1/rby1a_1.2_no_gripper.xml#L279) | unavailable | [subtree root L397](https://github.com/RainbowRobotics/rby1-sdk/blob/300a585c297d1bdf8554312c3a1659610a9823f5/models/rby1a/urdf/model.urdf#L397) |
| link_left_arm_3 / principal_moments | [0.00146823, 0.00783637, 0.00798526] | unavailable | [0.00187523368, 0.00849326349, 0.00867240283] | [0.000407003681, 0.000656893492, 0.000687142827] | NO MATCHING SOURCE | [inertia input L281](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/rainbow_robotics_rby1/rby1a_1.2_no_gripper.xml#L281) | unavailable | [inertia input L402](https://github.com/RainbowRobotics/rby1-sdk/blob/300a585c297d1bdf8554312c3a1659610a9823f5/models/rby1a/urdf/model.urdf#L402) |
| link_left_arm_4 / subtree_mass | 2.45684616 | unavailable | 3.25277887 | 0.79593271 | NO MATCHING SOURCE | [subtree root L288](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/rainbow_robotics_rby1/rby1a_1.2_no_gripper.xml#L288) | unavailable | [subtree root L419](https://github.com/RainbowRobotics/rby1-sdk/blob/300a585c297d1bdf8554312c3a1659610a9823f5/models/rby1a/urdf/model.urdf#L419) |
| link_left_arm_5 / mass | 1.60424243 | unavailable | 1.59194395 | -0.01229848 | NO MATCHING SOURCE | [input L297](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/rainbow_robotics_rby1/rby1a_1.2_no_gripper.xml#L297) | unavailable | [input L443](https://github.com/RainbowRobotics/rby1-sdk/blob/300a585c297d1bdf8554312c3a1659610a9823f5/models/rby1a/urdf/model.urdf#L443) |
| link_left_arm_5 / subtree_mass | 2.03175916 | unavailable | 2.82769177 | 0.79593261 | NO MATCHING SOURCE | [subtree root L295](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/rainbow_robotics_rby1/rby1a_1.2_no_gripper.xml#L295) | unavailable | [subtree root L441](https://github.com/RainbowRobotics/rby1-sdk/blob/300a585c297d1bdf8554312c3a1659610a9823f5/models/rby1a/urdf/model.urdf#L441) |
| link_left_arm_5 / principal_moments | [0.00161471846, 0.00246608096, 0.00274367059] | unavailable | [0.00151658242, 0.00255036012, 0.00262684747] | [-9.81360381e-05, 8.42791589e-05, -0.000116823121] | NO MATCHING SOURCE | [inertia input L297](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/rainbow_robotics_rby1/rby1a_1.2_no_gripper.xml#L297) | unavailable | [inertia input L446](https://github.com/RainbowRobotics/rby1-sdk/blob/300a585c297d1bdf8554312c3a1659610a9823f5/models/rby1a/urdf/model.urdf#L446) |
| link_left_arm_6 / mass | 0.42751673 | unavailable | 0.21137279 | -0.21614394 | NO MATCHING SOURCE | [input L307](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/rainbow_robotics_rby1/rby1a_1.2_no_gripper.xml#L307) | unavailable | [input L465](https://github.com/RainbowRobotics/rby1-sdk/blob/300a585c297d1bdf8554312c3a1659610a9823f5/models/rby1a/urdf/model.urdf#L465) |
| link_left_arm_6 / subtree_mass | 0.42751673 | unavailable | 1.23574782 | 0.80823109 | NO MATCHING SOURCE | [subtree root L305](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/rainbow_robotics_rby1/rby1a_1.2_no_gripper.xml#L305) | unavailable | [subtree root L463](https://github.com/RainbowRobotics/rby1-sdk/blob/300a585c297d1bdf8554312c3a1659610a9823f5/models/rby1a/urdf/model.urdf#L463) |
| link_left_arm_6 / principal_moments | [0.000295799701, 0.000306800493, 0.000489499806] | unavailable | [0.000134519712, 0.000145103152, 0.000254327137] | [-0.000161279989, -0.000161697341, -0.00023517267] | NO MATCHING SOURCE | [inertia input L307](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/rainbow_robotics_rby1/rby1a_1.2_no_gripper.xml#L307) | unavailable | [inertia input L468](https://github.com/RainbowRobotics/rby1-sdk/blob/300a585c297d1bdf8554312c3a1659610a9823f5/models/rby1a/urdf/model.urdf#L468) |
| link_head_1 / mass | 0.704765 | unavailable | 0.0745058 | -0.6302592 | NO MATCHING SOURCE | [input L323](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/rainbow_robotics_rby1/rby1a_1.2_no_gripper.xml#L323) | unavailable | [input L615](https://github.com/RainbowRobotics/rby1-sdk/blob/300a585c297d1bdf8554312c3a1659610a9823f5/models/rby1a/urdf/model.urdf#L615) |
| link_head_1 / subtree_mass | 1.657392 | unavailable | 0.11035954 | -1.54703246 | NO MATCHING SOURCE | [subtree root L321](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/rainbow_robotics_rby1/rby1a_1.2_no_gripper.xml#L321) | unavailable | [subtree root L613](https://github.com/RainbowRobotics/rby1-sdk/blob/300a585c297d1bdf8554312c3a1659610a9823f5/models/rby1a/urdf/model.urdf#L613) |
| link_head_1 / principal_moments | [0.000359954, 0.000593368, 0.000662227] | unavailable | [1.7261443e-05, 2.18237001e-05, 2.45448568e-05] | [-0.000342692557, -0.0005715443, -0.000637682143] | NO MATCHING SOURCE | [inertia input L323](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/rainbow_robotics_rby1/rby1a_1.2_no_gripper.xml#L323) | unavailable | [inertia input L618](https://github.com/RainbowRobotics/rby1-sdk/blob/300a585c297d1bdf8554312c3a1659610a9823f5/models/rby1a/urdf/model.urdf#L618) |
| link_head_2 / mass | 0.952627 | unavailable | 0.03585374 | -0.91677326 | NO MATCHING SOURCE | [input L329](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/rainbow_robotics_rby1/rby1a_1.2_no_gripper.xml#L329) | unavailable | [input L630](https://github.com/RainbowRobotics/rby1-sdk/blob/300a585c297d1bdf8554312c3a1659610a9823f5/models/rby1a/urdf/model.urdf#L630) |
| link_head_2 / subtree_mass | 0.952627 | unavailable | 0.03585374 | -0.91677326 | NO MATCHING SOURCE | [subtree root L327](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/rainbow_robotics_rby1/rby1a_1.2_no_gripper.xml#L327) | unavailable | [subtree root L628](https://github.com/RainbowRobotics/rby1-sdk/blob/300a585c297d1bdf8554312c3a1659610a9823f5/models/rby1a/urdf/model.urdf#L628) |
| link_head_2 / principal_moments | [0.000633984, 0.00136285, 0.00173533] | unavailable | [1.02242109e-05, 1.31161163e-05, 2.04696728e-05] | [-0.000623759789, -0.00134973388, -0.00171486033] | NO MATCHING SOURCE | [inertia input L329](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/rainbow_robotics_rby1/rby1a_1.2_no_gripper.xml#L329) | unavailable | [inertia input L633](https://github.com/RainbowRobotics/rby1-sdk/blob/300a585c297d1bdf8554312c3a1659610a9823f5/models/rby1a/urdf/model.urdf#L633) |
| torso_0 / range | [-0.349066, 0.349066] | unavailable | [-0.261799388, 0.261799388] | [0.087266612, -0.087266612] | NO MATCHING SOURCE | [input L128](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/rainbow_robotics_rby1/rby1a_1.2_no_gripper.xml#L128) | unavailable | [input L673](https://github.com/RainbowRobotics/rby1-sdk/blob/300a585c297d1bdf8554312c3a1659610a9823f5/models/rby1a/urdf/model.urdf#L673) |
| torso_1 / range | [-1.0472, 1.52173] | unavailable | [-0.523598776, 1.57079633] | [0.523601224, 0.049066327] | NO MATCHING SOURCE | [input L135](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/rainbow_robotics_rby1/rby1a_1.2_no_gripper.xml#L135) | unavailable | [input L688](https://github.com/RainbowRobotics/rby1-sdk/blob/300a585c297d1bdf8554312c3a1659610a9823f5/models/rby1a/urdf/model.urdf#L688) |
| torso_2 / range | [-2.47837, 1.5708] | unavailable | [-2.44346095, 1.3962634] | [0.0349090472, -0.174536598] | NO MATCHING SOURCE | [input L144](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/rainbow_robotics_rby1/rby1a_1.2_no_gripper.xml#L144) | unavailable | [input L703](https://github.com/RainbowRobotics/rby1-sdk/blob/300a585c297d1bdf8554312c3a1659610a9823f5/models/rby1a/urdf/model.urdf#L703) |
| torso_3 / effort | 270 | unavailable | 120 | -150 | NO MATCHING SOURCE | [input L355](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/rainbow_robotics_rby1/rby1a_1.2_no_gripper.xml#L355) | unavailable | [input L718](https://github.com/RainbowRobotics/rby1-sdk/blob/300a585c297d1bdf8554312c3a1659610a9823f5/models/rby1a/urdf/model.urdf#L718) |
| torso_5 / range | [-1.5708, 1.5708] | unavailable | [-2.35619449, 2.35619449] | [-0.78539449, 0.78539449] | NO MATCHING SOURCE | [input L166](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/rainbow_robotics_rby1/rby1a_1.2_no_gripper.xml#L166) | unavailable | [input L748](https://github.com/RainbowRobotics/rby1-sdk/blob/300a585c297d1bdf8554312c3a1659610a9823f5/models/rby1a/urdf/model.urdf#L748) |
| right_arm_0 / range | [-2.35619, 2.35619] | unavailable | [-3.14159265, 3.14159265] | [-0.785402654, 0.785402654] | NO MATCHING SOURCE | [input L188](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/rainbow_robotics_rby1/rby1a_1.2_no_gripper.xml#L188) | unavailable | [input L763](https://github.com/RainbowRobotics/rby1-sdk/blob/300a585c297d1bdf8554312c3a1659610a9823f5/models/rby1a/urdf/model.urdf#L763) |
| right_arm_1 / range | [-3.14159, 0.05] | unavailable | [-3.14159265, 0.017453293] | [-2.654e-06, -0.032546707] | NO MATCHING SOURCE | [input L196](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/rainbow_robotics_rby1/rby1a_1.2_no_gripper.xml#L196) | unavailable | [input L778](https://github.com/RainbowRobotics/rby1-sdk/blob/300a585c297d1bdf8554312c3a1659610a9823f5/models/rby1a/urdf/model.urdf#L778) |
| right_arm_2 / range | [-2.0944, 2.0944] | unavailable | [-3.14159265, 3.14159265] | [-1.04719265, 1.04719265] | NO MATCHING SOURCE | [input L203](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/rainbow_robotics_rby1/rby1a_1.2_no_gripper.xml#L203) | unavailable | [input L793](https://github.com/RainbowRobotics/rby1-sdk/blob/300a585c297d1bdf8554312c3a1659610a9823f5/models/rby1a/urdf/model.urdf#L793) |
| right_arm_3 / range | [-2.61799, 0.01] | unavailable | [-2.61799388, 0.017453293] | [-3.878e-06, 0.007453293] | NO MATCHING SOURCE | [input L213](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/rainbow_robotics_rby1/rby1a_1.2_no_gripper.xml#L213) | unavailable | [input L808](https://github.com/RainbowRobotics/rby1-sdk/blob/300a585c297d1bdf8554312c3a1659610a9823f5/models/rby1a/urdf/model.urdf#L808) |
| right_arm_4 / range | [-6.28319, 6.28319] | unavailable | [-3.14159265, 3.14159265] | [3.14159735, -3.14159735] | NO MATCHING SOURCE | [input L222](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/rainbow_robotics_rby1/rby1a_1.2_no_gripper.xml#L222) | unavailable | [input L823](https://github.com/RainbowRobotics/rby1-sdk/blob/300a585c297d1bdf8554312c3a1659610a9823f5/models/rby1a/urdf/model.urdf#L823) |
| right_arm_5 / range | [-1.74533, 2.00713] | unavailable | [-1.57079633, 1.91986218] | [0.174533673, -0.087267823] | NO MATCHING SOURCE | [input L231](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/rainbow_robotics_rby1/rby1a_1.2_no_gripper.xml#L231) | unavailable | [input L838](https://github.com/RainbowRobotics/rby1-sdk/blob/300a585c297d1bdf8554312c3a1659610a9823f5/models/rby1a/urdf/model.urdf#L838) |
| right_arm_6 / range | [-2.96706, 2.96706] | unavailable | [-2.70526034, 2.70526034] | [0.26179966, -0.26179966] | NO MATCHING SOURCE | [input L241](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/rainbow_robotics_rby1/rby1a_1.2_no_gripper.xml#L241) | unavailable | [input L853](https://github.com/RainbowRobotics/rby1-sdk/blob/300a585c297d1bdf8554312c3a1659610a9823f5/models/rby1a/urdf/model.urdf#L853) |
| left_arm_0 / range | [-2.35619, 2.35619] | unavailable | [-3.14159265, 3.14159265] | [-0.785402654, 0.785402654] | NO MATCHING SOURCE | [input L256](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/rainbow_robotics_rby1/rby1a_1.2_no_gripper.xml#L256) | unavailable | [input L868](https://github.com/RainbowRobotics/rby1-sdk/blob/300a585c297d1bdf8554312c3a1659610a9823f5/models/rby1a/urdf/model.urdf#L868) |
| left_arm_1 / range | [-0.05, 3.14159] | unavailable | [-0.017453293, 3.14159265] | [0.032546707, 2.654e-06] | NO MATCHING SOURCE | [input L264](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/rainbow_robotics_rby1/rby1a_1.2_no_gripper.xml#L264) | unavailable | [input L883](https://github.com/RainbowRobotics/rby1-sdk/blob/300a585c297d1bdf8554312c3a1659610a9823f5/models/rby1a/urdf/model.urdf#L883) |
| left_arm_2 / range | [-2.0944, 2.0944] | unavailable | [-3.14159265, 3.14159265] | [-1.04719265, 1.04719265] | NO MATCHING SOURCE | [input L272](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/rainbow_robotics_rby1/rby1a_1.2_no_gripper.xml#L272) | unavailable | [input L898](https://github.com/RainbowRobotics/rby1-sdk/blob/300a585c297d1bdf8554312c3a1659610a9823f5/models/rby1a/urdf/model.urdf#L898) |
| left_arm_3 / range | [-2.61799, 0.01] | unavailable | [-2.61799388, 0.017453293] | [-3.878e-06, 0.007453293] | NO MATCHING SOURCE | [input L282](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/rainbow_robotics_rby1/rby1a_1.2_no_gripper.xml#L282) | unavailable | [input L913](https://github.com/RainbowRobotics/rby1-sdk/blob/300a585c297d1bdf8554312c3a1659610a9823f5/models/rby1a/urdf/model.urdf#L913) |
| left_arm_4 / range | [-6.28319, 6.28319] | unavailable | [-3.14159265, 3.14159265] | [3.14159735, -3.14159735] | NO MATCHING SOURCE | [input L291](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/rainbow_robotics_rby1/rby1a_1.2_no_gripper.xml#L291) | unavailable | [input L928](https://github.com/RainbowRobotics/rby1-sdk/blob/300a585c297d1bdf8554312c3a1659610a9823f5/models/rby1a/urdf/model.urdf#L928) |
| left_arm_5 / range | [-1.74533, 2.00713] | unavailable | [-1.57079633, 1.91986218] | [0.174533673, -0.087267823] | NO MATCHING SOURCE | [input L299](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/rainbow_robotics_rby1/rby1a_1.2_no_gripper.xml#L299) | unavailable | [input L943](https://github.com/RainbowRobotics/rby1-sdk/blob/300a585c297d1bdf8554312c3a1659610a9823f5/models/rby1a/urdf/model.urdf#L943) |
| left_arm_6 / range | [-2.96706, 2.96706] | unavailable | [-2.70526034, 2.70526034] | [0.26179966, -0.26179966] | NO MATCHING SOURCE | [input L309](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/rainbow_robotics_rby1/rby1a_1.2_no_gripper.xml#L309) | unavailable | [input L958](https://github.com/RainbowRobotics/rby1-sdk/blob/300a585c297d1bdf8554312c3a1659610a9823f5/models/rby1a/urdf/model.urdf#L958) |
| head_0 / range | [-1.57, 1.57] | unavailable | [-0.523, 0.523] | [1.047, -1.047] | NO MATCHING SOURCE | [input L324](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/rainbow_robotics_rby1/rby1a_1.2_no_gripper.xml#L324) | unavailable | [input L1033](https://github.com/RainbowRobotics/rby1-sdk/blob/300a585c297d1bdf8554312c3a1659610a9823f5/models/rby1a/urdf/model.urdf#L1033) |
| head_0 / effort | 7.3 | unavailable | 1000 | 992.7 | NO MATCHING SOURCE | [input L388](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/rainbow_robotics_rby1/rby1a_1.2_no_gripper.xml#L388) | unavailable | [input L1033](https://github.com/RainbowRobotics/rby1-sdk/blob/300a585c297d1bdf8554312c3a1659610a9823f5/models/rby1a/urdf/model.urdf#L1033) |
| head_1 / range | [-1.57, 1.57] | unavailable | [-0.35, 1.57] | [1.22, 0] | NO MATCHING SOURCE | [input L330](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/rainbow_robotics_rby1/rby1a_1.2_no_gripper.xml#L330) | unavailable | [input L1041](https://github.com/RainbowRobotics/rby1-sdk/blob/300a585c297d1bdf8554312c3a1659610a9823f5/models/rby1a/urdf/model.urdf#L1041) |
| head_1 / effort | 7.3 | unavailable | 1000 | 992.7 | NO MATCHING SOURCE | [input L389](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/rainbow_robotics_rby1/rby1a_1.2_no_gripper.xml#L389) | unavailable | [input L1041](https://github.com/RainbowRobotics/rby1-sdk/blob/300a585c297d1bdf8554312c3a1659610a9823f5/models/rby1a/urdf/model.urdf#L1041) |

## Raw CoM records and reporting decisions

Raw values retain the previous root-anchor registration before Kabsch; original world coordinates also remain in the snapshots. Eligible findings above use the fitted transform into M. Excluded raw records below are diagnostic numbers, not findings. No CoM suppression applies to mass or principal inertia moments.

| Entity / quantity | Raw M | Raw S | Raw H | Raw H − M | Decision | M source | S source | H source |
|---|---|---|---|---|---|---|---|---|
| robot / total_com_registered | [-0.0280715292, -0.00527943564, 0.541779715] | unavailable | [-0.0285707098, -0.00377508993, 0.535527903] | [-0.000499180545, 0.00150434571, -0.00625181161] | M/H: kinematic convention differs | [aggregate inputs](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/rainbow_robotics_rby1/rby1a_1.2_no_gripper.xml#L1) | unavailable | [aggregate inputs](https://github.com/RainbowRobotics/rby1-sdk/blob/300a585c297d1bdf8554312c3a1659610a9823f5/models/rby1a/urdf/model.urdf#L1) |
| base / com_registered | [-0.0615794, -0.00142271, 0.135139] | unavailable | [-0.06157942, -0.00142271, 0.13513861] | [-2e-08, 0, -3.9e-07] | M/H: kinematic convention differs | [CoM/kinematic input L101](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/rainbow_robotics_rby1/rby1a_1.2_no_gripper.xml#L101) | unavailable | [CoM/kinematic input L9](https://github.com/RainbowRobotics/rby1-sdk/blob/300a585c297d1bdf8554312c3a1659610a9823f5/models/rby1a/urdf/model.urdf#L9) |
| wheel_r / com_registered | [0.228, -0.26573938, 0.1] | unavailable | [0.228, -0.26573938, 0.1] | [0, 0, 0] | M/H: kinematic convention differs | [CoM/kinematic input L113](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/rainbow_robotics_rby1/rby1a_1.2_no_gripper.xml#L113) | unavailable | [CoM/kinematic input L24](https://github.com/RainbowRobotics/rby1-sdk/blob/300a585c297d1bdf8554312c3a1659610a9823f5/models/rby1a/urdf/model.urdf#L24) |
| wheel_l / com_registered | [0.228, 0.26573938, 0.1] | unavailable | [0.228, 0.26573938, 0.1] | [0, 0, 0] | M/H: kinematic convention differs | [CoM/kinematic input L120](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/rainbow_robotics_rby1/rby1a_1.2_no_gripper.xml#L120) | unavailable | [CoM/kinematic input L38](https://github.com/RainbowRobotics/rby1-sdk/blob/300a585c297d1bdf8554312c3a1659610a9823f5/models/rby1a/urdf/model.urdf#L38) |
| link_torso_0 / com_registered | [-0.0884841, 0.00021367, 0.28050046] | unavailable | [-0.08848415, 0.00021367, 0.28050046] | [-5e-08, 0, 0] | M/H: kinematic convention differs | [CoM/kinematic input L127](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/rainbow_robotics_rby1/rby1a_1.2_no_gripper.xml#L127) | unavailable | [CoM/kinematic input L52](https://github.com/RainbowRobotics/rby1-sdk/blob/300a585c297d1bdf8554312c3a1659610a9823f5/models/rby1a/urdf/model.urdf#L52) |
| link_torso_1 / com_registered | [0.00728955, -0.0172852, 0.3496138] | unavailable | [0.00728955, -0.01728522, 0.3496138] | [0, -2e-08, 0] | M/H: kinematic convention differs | [CoM/kinematic input L134](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/rainbow_robotics_rby1/rby1a_1.2_no_gripper.xml#L134) | unavailable | [CoM/kinematic input L75](https://github.com/RainbowRobotics/rby1-sdk/blob/300a585c297d1bdf8554312c3a1659610a9823f5/models/rby1a/urdf/model.urdf#L75) |
| link_torso_2 / com_registered | [0.00653835, -0.0176954, 0.6868658] | unavailable | [0.00653835, -0.01769536, 0.68686582] | [0, 4e-08, 2e-08] | M/H: kinematic convention differs | [CoM/kinematic input L143](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/rainbow_robotics_rby1/rby1a_1.2_no_gripper.xml#L143) | unavailable | [CoM/kinematic input L98](https://github.com/RainbowRobotics/rby1-sdk/blob/300a585c297d1bdf8554312c3a1659610a9823f5/models/rby1a/urdf/model.urdf#L98) |
| link_torso_3 / com_registered | [-0.00574156, -0.0172598, 0.9805561] | unavailable | [-0.00574156, -0.01725975, 0.9805561] | [0, 5e-08, 0] | M/H: kinematic convention differs | [CoM/kinematic input L152](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/rainbow_robotics_rby1/rby1a_1.2_no_gripper.xml#L152) | unavailable | [CoM/kinematic input L121](https://github.com/RainbowRobotics/rby1-sdk/blob/300a585c297d1bdf8554312c3a1659610a9823f5/models/rby1a/urdf/model.urdf#L121) |
| link_torso_4 / com_registered | [-0.0909709, 5.085e-05, 1.0065195] | unavailable | [-0.09097095, 5.085e-05, 1.0065195] | [-5e-08, 0, 0] | M/H: kinematic convention differs | [CoM/kinematic input L158](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/rainbow_robotics_rby1/rby1a_1.2_no_gripper.xml#L158) | unavailable | [CoM/kinematic input L136](https://github.com/RainbowRobotics/rby1-sdk/blob/300a585c297d1bdf8554312c3a1659610a9823f5/models/rby1a/urdf/model.urdf#L136) |
| link_torso_5 / com_registered | [-0.0132199, 0.000254676, 1.2580509] | unavailable | [-0.01338376, 0.00025621, 1.25720168] | [-0.00016386, 1.534e-06, -0.000849221539] | M/H: kinematic convention differs | [CoM/kinematic input L165](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/rainbow_robotics_rby1/rby1a_1.2_no_gripper.xml#L165) | unavailable | [CoM/kinematic input L160](https://github.com/RainbowRobotics/rby1-sdk/blob/300a585c297d1bdf8554312c3a1659610a9823f5/models/rby1a/urdf/model.urdf#L160) |
| link_right_arm_0 / com_registered | [-0.00316662, -0.187701171, 1.35824438] | unavailable | [-0.00316662, -0.18562819, 1.3699997] | [8.67361738e-19, 0.00207298066, 0.0117553158] | M/H: kinematic convention differs | [CoM/kinematic input L187](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/rainbow_robotics_rby1/rby1a_1.2_no_gripper.xml#L187) | unavailable | [CoM/kinematic input L183](https://github.com/RainbowRobotics/rby1-sdk/blob/300a585c297d1bdf8554312c3a1659610a9823f5/models/rby1a/urdf/model.urdf#L183) |
| link_right_arm_1 / com_registered | [-0.00307855, -0.22124741, 1.3570573] | unavailable | [-0.00307855, -0.22124741, 1.35705676] | [1.30104261e-18, 0, -5.4e-07] | M/H: kinematic convention differs | [CoM/kinematic input L195](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/rainbow_robotics_rby1/rby1a_1.2_no_gripper.xml#L195) | unavailable | [CoM/kinematic input L205](https://github.com/RainbowRobotics/rby1-sdk/blob/300a585c297d1bdf8554312c3a1659610a9823f5/models/rby1a/urdf/model.urdf#L205) |
| link_right_arm_2 / com_registered | [0.00115434, -0.22196635, 1.2080755] | unavailable | [0.00115434, -0.21803365, 1.20807476] | [-4.33680869e-19, 0.0039327, -7.4e-07] | M/H: kinematic convention differs | [CoM/kinematic input L202](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/rainbow_robotics_rby1/rby1a_1.2_no_gripper.xml#L202) | unavailable | [CoM/kinematic input L228](https://github.com/RainbowRobotics/rby1-sdk/blob/300a585c297d1bdf8554312c3a1659610a9823f5/models/rby1a/urdf/model.urdf#L228) |
| link_right_arm_3 / com_registered | [0.0149687, -0.22692891, 1.0485024] | unavailable | [0.01496865, -0.22692891, 1.04850189] | [-5e-08, 0, -5.1e-07] | M/H: kinematic convention differs | [CoM/kinematic input L212](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/rainbow_robotics_rby1/rby1a_1.2_no_gripper.xml#L212) | unavailable | [CoM/kinematic input L251](https://github.com/RainbowRobotics/rby1-sdk/blob/300a585c297d1bdf8554312c3a1659610a9823f5/models/rby1a/urdf/model.urdf#L251) |
| link_right_arm_4 / com_registered | [-1.1e-07, -0.2469604, 0.8998216] | unavailable | [-1.1e-07, -0.24696036, 0.8998211] | [5.29395592e-23, 4e-08, -5e-07] | M/H: kinematic convention differs | [CoM/kinematic input L221](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/rainbow_robotics_rby1/rby1a_1.2_no_gripper.xml#L221) | unavailable | [CoM/kinematic input L274](https://github.com/RainbowRobotics/rby1-sdk/blob/300a585c297d1bdf8554312c3a1659610a9823f5/models/rby1a/urdf/model.urdf#L274) |
| link_right_arm_5 / com_registered | [0.00318034, -0.22532264, 0.8099039] | unavailable | [0.00318034, -0.22532264, 0.80990345] | [-1.30104261e-18, 0, -4.5e-07] | M/H: kinematic convention differs | [CoM/kinematic input L229](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/rainbow_robotics_rby1/rby1a_1.2_no_gripper.xml#L229) | unavailable | [CoM/kinematic input L296](https://github.com/RainbowRobotics/rby1-sdk/blob/300a585c297d1bdf8554312c3a1659610a9823f5/models/rby1a/urdf/model.urdf#L296) |
| link_right_arm_6 / com_registered | [0.00024951, -0.22019562, 0.73088736] | unavailable | [0.0006681, -0.22031708, 0.74163957] | [0.00041859, -0.00012146, 0.01075221] | M/H: kinematic convention differs | [CoM/kinematic input L239](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/rainbow_robotics_rby1/rby1a_1.2_no_gripper.xml#L239) | unavailable | [CoM/kinematic input L319](https://github.com/RainbowRobotics/rby1-sdk/blob/300a585c297d1bdf8554312c3a1659610a9823f5/models/rby1a/urdf/model.urdf#L319) |
| link_left_arm_0 / com_registered | [-0.00316662, 0.187700522, 1.35824704] | unavailable | [-0.00316662, 0.18562819, 1.3699997] | [8.67361738e-19, -0.00207233227, 0.0117526577] | M/H: kinematic convention differs | [CoM/kinematic input L255](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/rainbow_robotics_rby1/rby1a_1.2_no_gripper.xml#L255) | unavailable | [CoM/kinematic input L334](https://github.com/RainbowRobotics/rby1-sdk/blob/300a585c297d1bdf8554312c3a1659610a9823f5/models/rby1a/urdf/model.urdf#L334) |
| link_left_arm_1 / com_registered | [-0.0018347, 0.22040596, 1.3599132] | unavailable | [-0.00307855, 0.22124741, 1.35705676] | [-0.00124385, 0.00084145, -0.00285643954] | M/H: kinematic convention differs | [CoM/kinematic input L263](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/rainbow_robotics_rby1/rby1a_1.2_no_gripper.xml#L263) | unavailable | [CoM/kinematic input L356](https://github.com/RainbowRobotics/rby1-sdk/blob/300a585c297d1bdf8554312c3a1659610a9823f5/models/rby1a/urdf/model.urdf#L356) |
| link_left_arm_2 / com_registered | [0.00066086, 0.21961417, 1.2125705] | unavailable | [0.00115434, 0.21803365, 1.20807476] | [0.00049348, -0.00158052, -0.00449573954] | M/H: kinematic convention differs | [CoM/kinematic input L271](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/rainbow_robotics_rby1/rby1a_1.2_no_gripper.xml#L271) | unavailable | [CoM/kinematic input L378](https://github.com/RainbowRobotics/rby1-sdk/blob/300a585c297d1bdf8554312c3a1659610a9823f5/models/rby1a/urdf/model.urdf#L378) |
| link_left_arm_3 / com_registered | [0.015347, 0.22793126, 1.0440211] | unavailable | [0.01496865, 0.22692891, 1.04850189] | [-0.00037835, -0.00100235, 0.00448079046] | M/H: kinematic convention differs | [CoM/kinematic input L281](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/rainbow_robotics_rby1/rby1a_1.2_no_gripper.xml#L281) | unavailable | [CoM/kinematic input L400](https://github.com/RainbowRobotics/rby1-sdk/blob/300a585c297d1bdf8554312c3a1659610a9823f5/models/rby1a/urdf/model.urdf#L400) |
| link_left_arm_4 / com_registered | [1.1e-07, 0.2469604, 0.8998216] | unavailable | [1.1e-07, 0.24696036, 0.8998211] | [-5.29395592e-23, -4e-08, -4.99539e-07] | M/H: kinematic convention differs | [CoM/kinematic input L290](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/rainbow_robotics_rby1/rby1a_1.2_no_gripper.xml#L290) | unavailable | [CoM/kinematic input L422](https://github.com/RainbowRobotics/rby1-sdk/blob/300a585c297d1bdf8554312c3a1659610a9823f5/models/rby1a/urdf/model.urdf#L422) |
| link_left_arm_5 / com_registered | [0.00592398, 0.20832944, 0.81216015] | unavailable | [0.00318034, 0.22532264, 0.80990345] | [-0.00274364, 0.0169932, -0.00225669954] | M/H: kinematic convention differs | [CoM/kinematic input L297](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/rainbow_robotics_rby1/rby1a_1.2_no_gripper.xml#L297) | unavailable | [CoM/kinematic input L444](https://github.com/RainbowRobotics/rby1-sdk/blob/300a585c297d1bdf8554312c3a1659610a9823f5/models/rby1a/urdf/model.urdf#L444) |
| link_left_arm_6 / com_registered | [-0.00024951, 0.22019562, 0.73088736] | unavailable | [-0.0006681, 0.22031708, 0.74163957] | [-0.00041859, 0.00012146, 0.0107522105] | M/H: kinematic convention differs | [CoM/kinematic input L307](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/rainbow_robotics_rby1/rby1a_1.2_no_gripper.xml#L307) | unavailable | [CoM/kinematic input L466](https://github.com/RainbowRobotics/rby1-sdk/blob/300a585c297d1bdf8554312c3a1659610a9823f5/models/rby1a/urdf/model.urdf#L466) |
| link_head_1 / com_registered | [0.02158357, 0.00593524, 1.48710084] | unavailable | [0.01049321, -0.0011427, 1.42968421] | [-0.01109036, -0.00707794, -0.05741663] | M/H: kinematic convention differs | [CoM/kinematic input L323](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/rainbow_robotics_rby1/rby1a_1.2_no_gripper.xml#L323) | unavailable | [CoM/kinematic input L616](https://github.com/RainbowRobotics/rby1-sdk/blob/300a585c297d1bdf8554312c3a1659610a9823f5/models/rby1a/urdf/model.urdf#L616) |
| link_head_2 / com_registered | [0.0751532, 0.00547509, 1.5491391] | unavailable | [0.02118034, 0.00099024, 1.45283704] | [-0.05397286, -0.00448485, -0.09630206] | M/H: kinematic convention differs | [CoM/kinematic input L329](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/rainbow_robotics_rby1/rby1a_1.2_no_gripper.xml#L329) | unavailable | [CoM/kinematic input L631](https://github.com/RainbowRobotics/rby1-sdk/blob/300a585c297d1bdf8554312c3a1659610a9823f5/models/rby1a/urdf/model.urdf#L631) |

## Mass accounting

Every contributing compiled body mass is listed here so total/subtree sums can be checked. Links point to explicit inertials or to geometry inputs when the compiler inferred a mass. CoM links identify inertial inputs; world coordinates additionally use the ancestor transforms and the registration recorded below.

| M body | M kg / source | S kg / source | H kg / source |
|---|---|---|---|
| base | 60.0804 / [input L101](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/rainbow_robotics_rby1/rby1a_1.2_no_gripper.xml#L101) | unavailable | 60.0804264 / [input L8](https://github.com/RainbowRobotics/rby1-sdk/blob/300a585c297d1bdf8554312c3a1659610a9823f5/models/rby1a/urdf/model.urdf#L8) |
| wheel_r | 1.37784 / [input L113](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/rainbow_robotics_rby1/rby1a_1.2_no_gripper.xml#L113) | unavailable | 1.37783736 / [input L23](https://github.com/RainbowRobotics/rby1-sdk/blob/300a585c297d1bdf8554312c3a1659610a9823f5/models/rby1a/urdf/model.urdf#L23) |
| wheel_l | 1.37784 / [input L120](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/rainbow_robotics_rby1/rby1a_1.2_no_gripper.xml#L120) | unavailable | 1.37783736 / [input L37](https://github.com/RainbowRobotics/rby1-sdk/blob/300a585c297d1bdf8554312c3a1659610a9823f5/models/rby1a/urdf/model.urdf#L37) |
| link_torso_0 | 2.24282 / [input L127](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/rainbow_robotics_rby1/rby1a_1.2_no_gripper.xml#L127) | unavailable | 2.24282123 / [input L51](https://github.com/RainbowRobotics/rby1-sdk/blob/300a585c297d1bdf8554312c3a1659610a9823f5/models/rby1a/urdf/model.urdf#L51) |
| link_torso_1 | 9.72163 / [input L134](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/rainbow_robotics_rby1/rby1a_1.2_no_gripper.xml#L134) | unavailable | 9.72162676 / [input L74](https://github.com/RainbowRobotics/rby1-sdk/blob/300a585c297d1bdf8554312c3a1659610a9823f5/models/rby1a/urdf/model.urdf#L74) |
| link_torso_2 | 9.21692 / [input L143](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/rainbow_robotics_rby1/rby1a_1.2_no_gripper.xml#L143) | unavailable | 9.2169185 / [input L97](https://github.com/RainbowRobotics/rby1-sdk/blob/300a585c297d1bdf8554312c3a1659610a9823f5/models/rby1a/urdf/model.urdf#L97) |
| link_torso_3 | 4.18679 / [input L152](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/rainbow_robotics_rby1/rby1a_1.2_no_gripper.xml#L152) | unavailable | 4.18679196 / [input L120](https://github.com/RainbowRobotics/rby1-sdk/blob/300a585c297d1bdf8554312c3a1659610a9823f5/models/rby1a/urdf/model.urdf#L120) |
| link_torso_4 | 4.45566 / [input L158](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/rainbow_robotics_rby1/rby1a_1.2_no_gripper.xml#L158) | unavailable | 4.45566276 / [input L135](https://github.com/RainbowRobotics/rby1-sdk/blob/300a585c297d1bdf8554312c3a1659610a9823f5/models/rby1a/urdf/model.urdf#L135) |
| link_torso_5 | 12.6659 / [input L165](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/rainbow_robotics_rby1/rby1a_1.2_no_gripper.xml#L165) | unavailable | 12.5901234 / [input L159](https://github.com/RainbowRobotics/rby1-sdk/blob/300a585c297d1bdf8554312c3a1659610a9823f5/models/rby1a/urdf/model.urdf#L159) |
| NECK_0 | 0 / [input L181](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/rainbow_robotics_rby1/rby1a_1.2_no_gripper.xml#L181) | unavailable | unmatched |
| link_right_arm_0 | 1.26164 / [input L187](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/rainbow_robotics_rby1/rby1a_1.2_no_gripper.xml#L187) | unavailable | 1.26164242 / [input L182](https://github.com/RainbowRobotics/rby1-sdk/blob/300a585c297d1bdf8554312c3a1659610a9823f5/models/rby1a/urdf/model.urdf#L182) |
| link_right_arm_1 | 2.27287 / [input L195](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/rainbow_robotics_rby1/rby1a_1.2_no_gripper.xml#L195) | unavailable | 2.27287031 / [input L204](https://github.com/RainbowRobotics/rby1-sdk/blob/300a585c297d1bdf8554312c3a1659610a9823f5/models/rby1a/urdf/model.urdf#L204) |
| link_right_arm_2 | 2.46909 / [input L202](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/rainbow_robotics_rby1/rby1a_1.2_no_gripper.xml#L202) | unavailable | 2.46909439 / [input L227](https://github.com/RainbowRobotics/rby1-sdk/blob/300a585c297d1bdf8554312c3a1659610a9823f5/models/rby1a/urdf/model.urdf#L227) |
| link_right_arm_3 | 2.26099 / [input L212](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/rainbow_robotics_rby1/rby1a_1.2_no_gripper.xml#L212) | unavailable | 2.26099493 / [input L250](https://github.com/RainbowRobotics/rby1-sdk/blob/300a585c297d1bdf8554312c3a1659610a9823f5/models/rby1a/urdf/model.urdf#L250) |
| link_right_arm_4 | 0.425087 / [input L221](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/rainbow_robotics_rby1/rby1a_1.2_no_gripper.xml#L221) | unavailable | 0.4250871 / [input L273](https://github.com/RainbowRobotics/rby1-sdk/blob/300a585c297d1bdf8554312c3a1659610a9823f5/models/rby1a/urdf/model.urdf#L273) |
| link_right_arm_5 | 1.59194 / [input L229](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/rainbow_robotics_rby1/rby1a_1.2_no_gripper.xml#L229) | unavailable | 1.59194395 / [input L295](https://github.com/RainbowRobotics/rby1-sdk/blob/300a585c297d1bdf8554312c3a1659610a9823f5/models/rby1a/urdf/model.urdf#L295) |
| link_right_arm_6 | 0.42751673 / [input L239](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/rainbow_robotics_rby1/rby1a_1.2_no_gripper.xml#L239) | unavailable | 0.21137279 / [input L318](https://github.com/RainbowRobotics/rby1-sdk/blob/300a585c297d1bdf8554312c3a1659610a9823f5/models/rby1a/urdf/model.urdf#L318) |
| link_left_arm_0 | 1.26164 / [input L255](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/rainbow_robotics_rby1/rby1a_1.2_no_gripper.xml#L255) | unavailable | 1.26164242 / [input L333](https://github.com/RainbowRobotics/rby1-sdk/blob/300a585c297d1bdf8554312c3a1659610a9823f5/models/rby1a/urdf/model.urdf#L333) |
| link_left_arm_1 | 1.88139 / [input L263](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/rainbow_robotics_rby1/rby1a_1.2_no_gripper.xml#L263) | unavailable | 2.27287031 / [input L355](https://github.com/RainbowRobotics/rby1-sdk/blob/300a585c297d1bdf8554312c3a1659610a9823f5/models/rby1a/urdf/model.urdf#L355) |
| link_left_arm_2 | 2.35634 / [input L271](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/rainbow_robotics_rby1/rby1a_1.2_no_gripper.xml#L271) | unavailable | 2.46909439 / [input L377](https://github.com/RainbowRobotics/rby1-sdk/blob/300a585c297d1bdf8554312c3a1659610a9823f5/models/rby1a/urdf/model.urdf#L377) |
| link_left_arm_3 | 2.00906 / [input L281](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/rainbow_robotics_rby1/rby1a_1.2_no_gripper.xml#L281) | unavailable | 2.26099493 / [input L399](https://github.com/RainbowRobotics/rby1-sdk/blob/300a585c297d1bdf8554312c3a1659610a9823f5/models/rby1a/urdf/model.urdf#L399) |
| link_left_arm_4 | 0.425087 / [input L290](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/rainbow_robotics_rby1/rby1a_1.2_no_gripper.xml#L290) | unavailable | 0.4250871 / [input L421](https://github.com/RainbowRobotics/rby1-sdk/blob/300a585c297d1bdf8554312c3a1659610a9823f5/models/rby1a/urdf/model.urdf#L421) |
| link_left_arm_5 | 1.60424243 / [input L297](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/rainbow_robotics_rby1/rby1a_1.2_no_gripper.xml#L297) | unavailable | 1.59194395 / [input L443](https://github.com/RainbowRobotics/rby1-sdk/blob/300a585c297d1bdf8554312c3a1659610a9823f5/models/rby1a/urdf/model.urdf#L443) |
| link_left_arm_6 | 0.42751673 / [input L307](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/rainbow_robotics_rby1/rby1a_1.2_no_gripper.xml#L307) | unavailable | 0.21137279 / [input L465](https://github.com/RainbowRobotics/rby1-sdk/blob/300a585c297d1bdf8554312c3a1659610a9823f5/models/rby1a/urdf/model.urdf#L465) |
| link_head_1 | 0.704765 / [input L323](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/rainbow_robotics_rby1/rby1a_1.2_no_gripper.xml#L323) | unavailable | 0.0745058 / [input L615](https://github.com/RainbowRobotics/rby1-sdk/blob/300a585c297d1bdf8554312c3a1659610a9823f5/models/rby1a/urdf/model.urdf#L615) |
| link_head_2 | 0.952627 / [input L329](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/rainbow_robotics_rby1/rby1a_1.2_no_gripper.xml#L329) | unavailable | 0.03585374 / [input L630](https://github.com/RainbowRobotics/rby1-sdk/blob/300a585c297d1bdf8554312c3a1659610a9823f5/models/rby1a/urdf/model.urdf#L630) |
| upstream-only FT_sensor_L | unavailable | unavailable | 0.49078507 / [input L495](https://github.com/RainbowRobotics/rby1-sdk/blob/300a585c297d1bdf8554312c3a1659610a9823f5/models/rby1a/urdf/model.urdf#L495) |
| upstream-only FT_sensor_R | unavailable | unavailable | 0.49078507 / [input L480](https://github.com/RainbowRobotics/rby1-sdk/blob/300a585c297d1bdf8554312c3a1659610a9823f5/models/rby1a/urdf/model.urdf#L480) |
| upstream-only ee_finger_l1 | unavailable | unavailable | 0.03326999 / [input L570](https://github.com/RainbowRobotics/rby1-sdk/blob/300a585c297d1bdf8554312c3a1659610a9823f5/models/rby1a/urdf/model.urdf#L570) |
| upstream-only ee_finger_l2 | unavailable | unavailable | 0.03326999 / [input L585](https://github.com/RainbowRobotics/rby1-sdk/blob/300a585c297d1bdf8554312c3a1659610a9823f5/models/rby1a/urdf/model.urdf#L585) |
| upstream-only ee_finger_r1 | unavailable | unavailable | 0.03326999 / [input L525](https://github.com/RainbowRobotics/rby1-sdk/blob/300a585c297d1bdf8554312c3a1659610a9823f5/models/rby1a/urdf/model.urdf#L525) |
| upstream-only ee_finger_r2 | unavailable | unavailable | 0.03326999 / [input L540](https://github.com/RainbowRobotics/rby1-sdk/blob/300a585c297d1bdf8554312c3a1659610a9823f5/models/rby1a/urdf/model.urdf#L540) |
| upstream-only ee_left | unavailable | unavailable | 0.46704998 / [input L555](https://github.com/RainbowRobotics/rby1-sdk/blob/300a585c297d1bdf8554312c3a1659610a9823f5/models/rby1a/urdf/model.urdf#L555) |
| upstream-only ee_right | unavailable | unavailable | 0.46704998 / [input L510](https://github.com/RainbowRobotics/rby1-sdk/blob/300a585c297d1bdf8554312c3a1659610a9823f5/models/rby1a/urdf/model.urdf#L510) |
| upstream-only link_head_0 | unavailable | unavailable | 0.0758211 / [input L600](https://github.com/RainbowRobotics/rby1-sdk/blob/300a585c297d1bdf8554312c3a1659610a9823f5/models/rby1a/urdf/model.urdf#L600) |

## Coverage and unmatched elements

```json
{
  "mapping_h": {
    "bodies": {
      "base": "base",
      "wheel_r": "wheel_r",
      "wheel_l": "wheel_l",
      "link_torso_0": "link_torso_0",
      "link_torso_1": "link_torso_1",
      "link_torso_2": "link_torso_2",
      "link_torso_3": "link_torso_3",
      "link_torso_4": "link_torso_4",
      "link_torso_5": "link_torso_5",
      "link_right_arm_0": "link_right_arm_0",
      "link_right_arm_1": "link_right_arm_1",
      "link_right_arm_2": "link_right_arm_2",
      "link_right_arm_3": "link_right_arm_3",
      "link_right_arm_4": "link_right_arm_4",
      "link_right_arm_5": "link_right_arm_5",
      "link_right_arm_6": "link_right_arm_6",
      "link_left_arm_0": "link_left_arm_0",
      "link_left_arm_1": "link_left_arm_1",
      "link_left_arm_2": "link_left_arm_2",
      "link_left_arm_3": "link_left_arm_3",
      "link_left_arm_4": "link_left_arm_4",
      "link_left_arm_5": "link_left_arm_5",
      "link_left_arm_6": "link_left_arm_6",
      "link_head_1": "link_head_1",
      "link_head_2": "link_head_2"
    },
    "joints": {
      "right_wheel": "right_wheel",
      "left_wheel": "left_wheel",
      "torso_0": "torso_0",
      "torso_1": "torso_1",
      "torso_2": "torso_2",
      "torso_3": "torso_3",
      "torso_4": "torso_4",
      "torso_5": "torso_5",
      "right_arm_0": "right_arm_0",
      "right_arm_1": "right_arm_1",
      "right_arm_2": "right_arm_2",
      "right_arm_3": "right_arm_3",
      "right_arm_4": "right_arm_4",
      "right_arm_5": "right_arm_5",
      "right_arm_6": "right_arm_6",
      "left_arm_0": "left_arm_0",
      "left_arm_1": "left_arm_1",
      "left_arm_2": "left_arm_2",
      "left_arm_3": "left_arm_3",
      "left_arm_4": "left_arm_4",
      "left_arm_5": "left_arm_5",
      "left_arm_6": "left_arm_6",
      "head_0": "head_0",
      "head_1": "head_1"
    },
    "body_methods": {
      "base": "name",
      "wheel_r": "name",
      "wheel_l": "name",
      "link_torso_0": "name",
      "link_torso_1": "name",
      "link_torso_2": "name",
      "link_torso_3": "name",
      "link_torso_4": "name",
      "link_torso_5": "name",
      "link_right_arm_0": "name",
      "link_right_arm_1": "name",
      "link_right_arm_2": "name",
      "link_right_arm_3": "name",
      "link_right_arm_4": "name",
      "link_right_arm_5": "name",
      "link_right_arm_6": "name",
      "link_left_arm_0": "name",
      "link_left_arm_1": "name",
      "link_left_arm_2": "name",
      "link_left_arm_3": "name",
      "link_left_arm_4": "name",
      "link_left_arm_5": "name",
      "link_left_arm_6": "name",
      "link_head_1": "name",
      "link_head_2": "name"
    },
    "joint_methods": {
      "right_wheel": "name",
      "left_wheel": "name",
      "torso_0": "name",
      "torso_1": "name",
      "torso_2": "name",
      "torso_3": "name",
      "torso_4": "name",
      "torso_5": "name",
      "right_arm_0": "name",
      "right_arm_1": "name",
      "right_arm_2": "name",
      "right_arm_3": "name",
      "right_arm_4": "name",
      "right_arm_5": "name",
      "right_arm_6": "name",
      "left_arm_0": "name",
      "left_arm_1": "name",
      "left_arm_2": "name",
      "left_arm_3": "name",
      "left_arm_4": "name",
      "left_arm_5": "name",
      "left_arm_6": "name",
      "head_0": "name",
      "head_1": "name"
    },
    "unmatched_m_bodies": [
      "NECK_0"
    ],
    "unmatched_upstream_bodies": [
      "FT_sensor_L",
      "FT_sensor_R",
      "ee_finger_l1",
      "ee_finger_l2",
      "ee_finger_r1",
      "ee_finger_r2",
      "ee_left",
      "ee_right",
      "link_head_0"
    ],
    "unmatched_m_joints": [],
    "unmatched_upstream_joints": [
      "gripper_finger_l1",
      "gripper_finger_l2",
      "gripper_finger_r1",
      "gripper_finger_r2"
    ],
    "registration_anchor": {
      "M": "base",
      "H": "base",
      "root_unmatched": false
    }
  },
  "mapping_s": null,
  "unavailable": [
    {
      "entity": "right_wheel",
      "other_entity": "right_wheel",
      "quantity": "range",
      "tolerance": "range",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "right_wheel",
      "other_entity": "right_wheel",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "right_wheel",
      "other_entity": "right_wheel",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "right_wheel",
      "other_entity": "right_wheel",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 15.707963268,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_wheel",
      "other_entity": "left_wheel",
      "quantity": "range",
      "tolerance": "range",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_wheel",
      "other_entity": "left_wheel",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_wheel",
      "other_entity": "left_wheel",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_wheel",
      "other_entity": "left_wheel",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 15.707963268,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "torso_0",
      "other_entity": "torso_0",
      "quantity": "force",
      "tolerance": "limit",
      "m": 270.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "torso_0",
      "other_entity": "torso_0",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 2.0943951,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "torso_1",
      "other_entity": "torso_1",
      "quantity": "force",
      "tolerance": "limit",
      "m": 270.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "torso_1",
      "other_entity": "torso_1",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 2.0943951,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "torso_2",
      "other_entity": "torso_2",
      "quantity": "force",
      "tolerance": "limit",
      "m": 270.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "torso_2",
      "other_entity": "torso_2",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 2.0943951,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "torso_3",
      "other_entity": "torso_3",
      "quantity": "force",
      "tolerance": "limit",
      "m": 270.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "torso_3",
      "other_entity": "torso_3",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 3.141592654,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "torso_4",
      "other_entity": "torso_4",
      "quantity": "force",
      "tolerance": "limit",
      "m": 120.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "torso_4",
      "other_entity": "torso_4",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 3.141592654,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "torso_5",
      "other_entity": "torso_5",
      "quantity": "force",
      "tolerance": "limit",
      "m": 120.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "torso_5",
      "other_entity": "torso_5",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 3.141592654,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "right_arm_0",
      "other_entity": "right_arm_0",
      "quantity": "force",
      "tolerance": "limit",
      "m": 70.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "right_arm_0",
      "other_entity": "right_arm_0",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 3.141592654,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "right_arm_1",
      "other_entity": "right_arm_1",
      "quantity": "force",
      "tolerance": "limit",
      "m": 70.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "right_arm_1",
      "other_entity": "right_arm_1",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 3.141592654,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "right_arm_2",
      "other_entity": "right_arm_2",
      "quantity": "force",
      "tolerance": "limit",
      "m": 70.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "right_arm_2",
      "other_entity": "right_arm_2",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 3.141592654,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "right_arm_3",
      "other_entity": "right_arm_3",
      "quantity": "force",
      "tolerance": "limit",
      "m": 40.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "right_arm_3",
      "other_entity": "right_arm_3",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 3.141592654,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "right_arm_4",
      "other_entity": "right_arm_4",
      "quantity": "force",
      "tolerance": "limit",
      "m": 10.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "right_arm_4",
      "other_entity": "right_arm_4",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 6.283185308,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "right_arm_5",
      "other_entity": "right_arm_5",
      "quantity": "force",
      "tolerance": "limit",
      "m": 10.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "right_arm_5",
      "other_entity": "right_arm_5",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 6.283185308,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "right_arm_6",
      "other_entity": "right_arm_6",
      "quantity": "force",
      "tolerance": "limit",
      "m": 8.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "right_arm_6",
      "other_entity": "right_arm_6",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 2.094395102,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_arm_0",
      "other_entity": "left_arm_0",
      "quantity": "force",
      "tolerance": "limit",
      "m": 70.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_arm_0",
      "other_entity": "left_arm_0",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 3.141592654,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_arm_1",
      "other_entity": "left_arm_1",
      "quantity": "force",
      "tolerance": "limit",
      "m": 70.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_arm_1",
      "other_entity": "left_arm_1",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 3.141592654,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_arm_2",
      "other_entity": "left_arm_2",
      "quantity": "force",
      "tolerance": "limit",
      "m": 70.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_arm_2",
      "other_entity": "left_arm_2",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 3.141592654,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_arm_3",
      "other_entity": "left_arm_3",
      "quantity": "force",
      "tolerance": "limit",
      "m": 40.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_arm_3",
      "other_entity": "left_arm_3",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 3.141592654,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_arm_4",
      "other_entity": "left_arm_4",
      "quantity": "force",
      "tolerance": "limit",
      "m": 10.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_arm_4",
      "other_entity": "left_arm_4",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 6.283185308,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_arm_5",
      "other_entity": "left_arm_5",
      "quantity": "force",
      "tolerance": "limit",
      "m": 10.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_arm_5",
      "other_entity": "left_arm_5",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 6.283185308,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_arm_6",
      "other_entity": "left_arm_6",
      "quantity": "force",
      "tolerance": "limit",
      "m": 8.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_arm_6",
      "other_entity": "left_arm_6",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 2.094395102,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "head_0",
      "other_entity": "head_0",
      "quantity": "force",
      "tolerance": "limit",
      "m": 7.3,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "head_0",
      "other_entity": "head_0",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 3.14,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "head_1",
      "other_entity": "head_1",
      "quantity": "force",
      "tolerance": "limit",
      "m": 7.3,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "head_1",
      "other_entity": "head_1",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 3.14,
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
| right_wheel / effort | unavailable | unavailable | unavailable |
| right_wheel / force | unavailable | unavailable | unavailable |
| right_wheel / velocity | unavailable | unavailable | 15.7079633 |
| left_wheel / effort | unavailable | unavailable | unavailable |
| left_wheel / force | unavailable | unavailable | unavailable |
| left_wheel / velocity | unavailable | unavailable | 15.7079633 |
| torso_0 / force | 270 | unavailable | unavailable |
| torso_0 / velocity | unavailable | unavailable | 2.0943951 |
| torso_1 / force | 270 | unavailable | unavailable |
| torso_1 / velocity | unavailable | unavailable | 2.0943951 |
| torso_2 / force | 270 | unavailable | unavailable |
| torso_2 / velocity | unavailable | unavailable | 2.0943951 |
| torso_3 / force | 270 | unavailable | unavailable |
| torso_3 / velocity | unavailable | unavailable | 3.14159265 |
| torso_4 / force | 120 | unavailable | unavailable |
| torso_4 / velocity | unavailable | unavailable | 3.14159265 |
| torso_5 / force | 120 | unavailable | unavailable |
| torso_5 / velocity | unavailable | unavailable | 3.14159265 |
| right_arm_0 / force | 70 | unavailable | unavailable |
| right_arm_0 / velocity | unavailable | unavailable | 3.14159265 |
| right_arm_1 / force | 70 | unavailable | unavailable |
| right_arm_1 / velocity | unavailable | unavailable | 3.14159265 |
| right_arm_2 / force | 70 | unavailable | unavailable |
| right_arm_2 / velocity | unavailable | unavailable | 3.14159265 |
| right_arm_3 / force | 40 | unavailable | unavailable |
| right_arm_3 / velocity | unavailable | unavailable | 3.14159265 |
| right_arm_4 / force | 10 | unavailable | unavailable |
| right_arm_4 / velocity | unavailable | unavailable | 6.28318531 |
| right_arm_5 / force | 10 | unavailable | unavailable |
| right_arm_5 / velocity | unavailable | unavailable | 6.28318531 |
| right_arm_6 / force | 8 | unavailable | unavailable |
| right_arm_6 / velocity | unavailable | unavailable | 2.0943951 |
| left_arm_0 / force | 70 | unavailable | unavailable |
| left_arm_0 / velocity | unavailable | unavailable | 3.14159265 |
| left_arm_1 / force | 70 | unavailable | unavailable |
| left_arm_1 / velocity | unavailable | unavailable | 3.14159265 |
| left_arm_2 / force | 70 | unavailable | unavailable |
| left_arm_2 / velocity | unavailable | unavailable | 3.14159265 |
| left_arm_3 / force | 40 | unavailable | unavailable |
| left_arm_3 / velocity | unavailable | unavailable | 3.14159265 |
| left_arm_4 / force | 10 | unavailable | unavailable |
| left_arm_4 / velocity | unavailable | unavailable | 6.28318531 |
| left_arm_5 / force | 10 | unavailable | unavailable |
| left_arm_5 / velocity | unavailable | unavailable | 6.28318531 |
| left_arm_6 / force | 8 | unavailable | unavailable |
| left_arm_6 / velocity | unavailable | unavailable | 2.0943951 |
| head_0 / force | 7.3 | unavailable | unavailable |
| head_0 / velocity | unavailable | unavailable | 3.14 |
| head_1 / force | 7.3 | unavailable | unavailable |
| head_1 / velocity | unavailable | unavailable | 3.14 |
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
    "file": "rainbow_robotics_rby1/rby1a_1.2.xml",
    "status": "passed",
    "findings": 0
  },
  {
    "file": "rainbow_robotics_rby1/rby1a_1.2_no_gripper.xml",
    "status": "passed",
    "findings": 0
  },
  {
    "file": "rainbow_robotics_rby1/rby1m_1.2.xml",
    "status": "passed",
    "findings": 0
  },
  {
    "file": "rainbow_robotics_rby1/rby1m_1.2_no_gripper.xml",
    "status": "passed",
    "findings": 0
  },
  {
    "file": "rainbow_robotics_rby1/rby1m_1.3.xml",
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
      "NO MATCHING SOURCE": 65
    },
    "classifications_changed": 0,
    "finding_membership_changes": 1
  },
  "2": {
    "provenance_method": "none",
    "counts": {
      "NO MATCHING SOURCE": 58
    },
    "classifications_changed": 0,
    "finding_membership_changes": 6
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
  "self_variants_recompiled": 5,
  "historical_snapshots_reused": 14,
  "primary_physics_unchanged": true,
  "source_matching": "original raw-value provenance criteria retained; kinematic guard applies to reported CoM"
}
```
