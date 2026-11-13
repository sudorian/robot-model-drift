# seeed_rebot_devarm

Status: **partial history**. Provenance: **dated match**, confidence **medium**.

Source selected using the ordered amended provenance rules.

M: `https://github.com/google-deepmind/mujoco_menagerie`, `seeed_rebot_devarm/seeed_rebot_devarm.xml`, commit `370c43965323c0944b433b202aac5058b5f907a9`.
H: `https://github.com/Seeed-Projects/reBot-Isaacsim`, `urdf/00-arm-rs_asm-v3/urdf/00-arm-rs_asm-v3.urdf`, commit `51aa87625e6aaa1ccb8514b0d0c66e3aa1c711bf`.
S: `6a18beabefa9564d9b66c93fd671a8c7a4548601` (2026-08-03T01:28:12+02:00). Menagerie release/change: 2026-08-09T12:35:18-07:00.

Limit semantics: MJCF effort values are supported actuator torque/force envelopes. URDF effort and velocity values are manufacturer declarations retained from XML; MuJoCo does not enforce those tags. Such declaration comparisons are explicitly distinct from compiled inertial/range quantities.


## Source evidence

```json
[
  {
    "url": "https://github.com/3dlg-hcvc/visacd",
    "document": "seeed_rebot_devarm/README.md",
    "commit": "370c43965323c0944b433b202aac5058b5f907a9",
    "current": true
  },
  {
    "url": "https://github.com/Seeed-Projects/reBot-Isaacsim",
    "document": "seeed_rebot_devarm/README.md",
    "commit": "370c43965323c0944b433b202aac5058b5f907a9",
    "current": true
  },
  {
    "url": "https://github.com/discoverse-dev/urdf-to-mjcf",
    "document": "seeed_rebot_devarm/README.md",
    "commit": "370c43965323c0944b433b202aac5058b5f907a9",
    "current": true
  }
]
```


## README derivation evidence

Documentation labels are conservative: an automated documented label requires an explicit affected entity and quantity. Broader conversion notes are retained here for review.

>    across the fixed joint, and preserved all six components of every URDF
>    inertia tensor, including the products of inertia. This keeps the MJCF
> 3. Fixed the base to the world and added the base link inertial.
> 5. Added position-controlled actuators with `ctrlrange` equal to the joint
>    limits. Joint torque limits come from the actuator ratings (RS-06: 36 N·m,
> Mass, center of mass, and the full compiled inertia tensor were verified against

## Kinematics consistency

A proper Kabsch rigid transform aligns all matched zero-pose body origins. The maximum per-origin residual and signed hinge/slide axis angles determine whether CoM can be compared; RMS is also recorded. Fewer than three non-collinear origins give insufficient kinematic coverage. CoM records that fail either required M/H or M/S check are excluded from counts and largest discrepancies. Masses, principal moments and raw joint ranges remain unchanged; a flagged range still requires convention review.

| Pair | Status | Origins / rank | RMS / maximum mm | Disagreeing / checked axes |
|---|---|---:|---:|---:|
| M/H | consistent | 10 / 3 | 0.000226729952 / 0.000293584627 | 0 / 8 |
| M/S | consistent | 10 / 3 | 0.000226729952 / 0.000293584627 | 0 / 8 |

Exact fitted transforms, per-origin residuals, thresholds and axis vectors:

```json
{
  "M/H": {
    "status": "consistent",
    "matched_body_origins": 10,
    "position_threshold_m": 0.005,
    "axis_threshold_rad": 0.005,
    "residual_definition": "maximum Euclidean residual over matched body origins; Kabsch minimizes RMS, which is also recorded",
    "coordinate_frames": "each snapshot registered to its matched report anchor",
    "anchor_m": "base_link",
    "anchor_other": "base_link",
    "rotation_other_to_m": [
      [
        0.9999999999990652,
        -1.790145620021164e-07,
        1.3553187252375752e-06
      ],
      [
        1.7901642359224945e-07,
        0.9999999999990403,
        -1.3735055512996677e-06
      ],
      [
        -1.3553184794066683e-06,
        1.3735057940583717e-06,
        0.9999999999981377
      ]
    ],
    "translation_other_to_m": [
      -2.3157102138626762e-07,
      1.1313776224729233e-07,
      -1.2290999121256085e-07
    ],
    "rms_residual_m": 2.2672995243387892e-07,
    "max_residual_m": 2.9358462686182025e-07,
    "fit_rank": 3,
    "axis_checks": [
      {
        "joint_m": "joint1",
        "joint_other": "joint1",
        "axis_m": [
          0.0,
          0.0,
          1.0
        ],
        "axis_other_aligned": [
          1.355318725237576e-06,
          -1.3735055512996686e-06,
          0.9999999999981384
        ],
        "angle_rad": 1.9296130043185435e-06,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "joint2",
        "joint_other": "joint2",
        "axis_m": [
          0.0,
          -1.0,
          2.2204460492503126e-16
        ],
        "axis_other_aligned": [
          1.790195403645668e-07,
          -0.9999999999973397,
          2.2996993091380762e-06
        ],
        "angle_rad": 2.306656651361587e-06,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "joint3",
        "joint_other": "joint3",
        "axis_m": [
          0.0,
          1.0,
          -2.2204460492503126e-16
        ],
        "axis_other_aligned": [
          -1.790195403645668e-07,
          0.9999999999973397,
          -2.2996993091380762e-06
        ],
        "angle_rad": 2.306656651361587e-06,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "joint4",
        "joint_other": "joint4",
        "axis_m": [
          0.0,
          1.0,
          -2.2204460492503126e-16
        ],
        "axis_other_aligned": [
          -1.790195403645668e-07,
          0.9999999999973397,
          -2.2996993091380762e-06
        ],
        "angle_rad": 2.306656651361587e-06,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "joint5",
        "joint_other": "joint5",
        "axis_m": [
          0.0,
          -8.53284317717928e-17,
          -1.0
        ],
        "axis_other_aligned": [
          -1.3553174100865975e-06,
          -5.972904655313237e-06,
          -0.9999999999812438
        ],
        "angle_rad": 6.124742876480296e-06,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "joint6",
        "joint_other": "joint6",
        "axis_m": [
          1.0,
          -1.874606153089679e-33,
          -4.440892098500624e-16
        ],
        "axis_other_aligned": [
          0.9999999999972977,
          1.790383632949033e-07,
          2.3178866240487654e-06
        ],
        "angle_rad": 2.3247909883565734e-06,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "joint_left",
        "joint_other": "gripper_joint1",
        "axis_m": [
          -2.4651903288156608e-32,
          -1.0,
          -4.440892098500624e-16
        ],
        "axis_other_aligned": [
          3.852219665252906e-06,
          -0.999999999991637,
          -1.3734972798714432e-06
        ],
        "angle_rad": 4.089754409013921e-06,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "joint_right",
        "joint_other": "gripper_joint2",
        "axis_m": [
          -2.4651903288156608e-32,
          1.0,
          -4.440892098500624e-16
        ],
        "axis_other_aligned": [
          3.4941905412510883e-06,
          0.9999999999929521,
          1.3735143082267697e-06
        ],
        "angle_rad": 3.754451903375297e-06,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      }
    ],
    "axis_disagreements": [],
    "com_eligible": true,
    "covariance_singular_values": [
      0.2447883359290944,
      0.041205811067849776,
      0.0007735867046753285
    ],
    "origin_residuals_m": {
      "base_link": 2.855383636782908e-07,
      "link1": 1.7961576105563658e-07,
      "link2": 1.4616336906097472e-07,
      "link3": 2.4396523390889764e-07,
      "link4": 1.5232473545520535e-07,
      "link5": 2.9358462686182025e-07,
      "link6": 2.306607956704905e-07,
      "gripper_end": 1.907581448795916e-07,
      "gripper_left": 2.4526511639350725e-07,
      "gripper_right": 2.4544889644420984e-07
    },
    "reason": "Unique proper rigid fit and matched signed axes meet the configured thresholds"
  },
  "M/S": {
    "status": "consistent",
    "matched_body_origins": 10,
    "position_threshold_m": 0.005,
    "axis_threshold_rad": 0.005,
    "residual_definition": "maximum Euclidean residual over matched body origins; Kabsch minimizes RMS, which is also recorded",
    "coordinate_frames": "each snapshot registered to its matched report anchor",
    "anchor_m": "base_link",
    "anchor_other": "base_link",
    "rotation_other_to_m": [
      [
        0.9999999999990652,
        -1.790145620021164e-07,
        1.3553187252375752e-06
      ],
      [
        1.7901642359224945e-07,
        0.9999999999990403,
        -1.3735055512996677e-06
      ],
      [
        -1.3553184794066683e-06,
        1.3735057940583717e-06,
        0.9999999999981377
      ]
    ],
    "translation_other_to_m": [
      -2.3157102138626762e-07,
      1.1313776224729233e-07,
      -1.2290999121256085e-07
    ],
    "rms_residual_m": 2.2672995243387892e-07,
    "max_residual_m": 2.9358462686182025e-07,
    "fit_rank": 3,
    "axis_checks": [
      {
        "joint_m": "joint1",
        "joint_other": "joint1",
        "axis_m": [
          0.0,
          0.0,
          1.0
        ],
        "axis_other_aligned": [
          1.355318725237576e-06,
          -1.3735055512996686e-06,
          0.9999999999981384
        ],
        "angle_rad": 1.9296130043185435e-06,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "joint2",
        "joint_other": "joint2",
        "axis_m": [
          0.0,
          -1.0,
          2.2204460492503126e-16
        ],
        "axis_other_aligned": [
          1.790195403645668e-07,
          -0.9999999999973397,
          2.2996993091380762e-06
        ],
        "angle_rad": 2.306656651361587e-06,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "joint3",
        "joint_other": "joint3",
        "axis_m": [
          0.0,
          1.0,
          -2.2204460492503126e-16
        ],
        "axis_other_aligned": [
          -1.790195403645668e-07,
          0.9999999999973397,
          -2.2996993091380762e-06
        ],
        "angle_rad": 2.306656651361587e-06,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "joint4",
        "joint_other": "joint4",
        "axis_m": [
          0.0,
          1.0,
          -2.2204460492503126e-16
        ],
        "axis_other_aligned": [
          -1.790195403645668e-07,
          0.9999999999973397,
          -2.2996993091380762e-06
        ],
        "angle_rad": 2.306656651361587e-06,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "joint5",
        "joint_other": "joint5",
        "axis_m": [
          0.0,
          -8.53284317717928e-17,
          -1.0
        ],
        "axis_other_aligned": [
          -1.3553174100865975e-06,
          -5.972904655313237e-06,
          -0.9999999999812438
        ],
        "angle_rad": 6.124742876480296e-06,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "joint6",
        "joint_other": "joint6",
        "axis_m": [
          1.0,
          -1.874606153089679e-33,
          -4.440892098500624e-16
        ],
        "axis_other_aligned": [
          0.9999999999972977,
          1.790383632949033e-07,
          2.3178866240487654e-06
        ],
        "angle_rad": 2.3247909883565734e-06,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "joint_left",
        "joint_other": "joint_left",
        "axis_m": [
          -2.4651903288156608e-32,
          -1.0,
          -4.440892098500624e-16
        ],
        "axis_other_aligned": [
          3.852219665252906e-06,
          -0.999999999991637,
          -1.3734972798714432e-06
        ],
        "angle_rad": 4.089754409013921e-06,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "joint_right",
        "joint_other": "joint_right",
        "axis_m": [
          -2.4651903288156608e-32,
          1.0,
          -4.440892098500624e-16
        ],
        "axis_other_aligned": [
          3.4941905412510883e-06,
          0.9999999999929521,
          1.3735143082267697e-06
        ],
        "angle_rad": 3.754451903375297e-06,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      }
    ],
    "axis_disagreements": [],
    "com_eligible": true,
    "covariance_singular_values": [
      0.2447883359290944,
      0.041205811067849776,
      0.0007735867046753285
    ],
    "origin_residuals_m": {
      "base_link": 2.855383636782908e-07,
      "link1": 1.7961576105563658e-07,
      "link2": 1.4616336906097472e-07,
      "link3": 2.4396523390889764e-07,
      "link4": 1.5232473545520535e-07,
      "link5": 2.9358462686182025e-07,
      "link6": 2.306607956704905e-07,
      "gripper_end": 1.907581448795916e-07,
      "gripper_left": 2.4526511639350725e-07,
      "gripper_right": 2.4544889644420984e-07
    },
    "reason": "Unique proper rigid fit and matched signed axes meet the configured thresholds"
  }
}
```


## Every reported quantity difference

Counts are quantity records, including correlated total/subtree/body mass records; they are not independent robot defects.

| Entity / quantity | M | S | H | H − M | Class | M source | S source | H source |
|---|---|---|---|---|---|---|---|---|
| robot / total_com_registered | [-0.0118333513, -0.000454569709, 0.155504459] | [-0.0118333712, -0.000454568678, 0.155504503] | [-0.0110671924, -0.000454566541, 0.155839368] | [0.00076615885, 3.16774009e-09, 0.000334909402] | STALE | [aggregate inputs](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/seeed_rebot_devarm/seeed_rebot_devarm.xml#L1) | [aggregate inputs](https://github.com/Seeed-Projects/reBot-Isaacsim/blob/6a18beabefa9564d9b66c93fd671a8c7a4548601/urdf/00-arm-rs_asm-v3/urdf/00-arm-rs_asm-v3.urdf#L1) | [aggregate inputs](https://github.com/Seeed-Projects/reBot-Isaacsim/blob/51aa87625e6aaa1ccb8514b0d0c66e3aa1c711bf/urdf/00-arm-rs_asm-v3/urdf/00-arm-rs_asm-v3.urdf#L1) |
| link2 / principal_moments | [0.000577462044, 0.00988484192, 0.0100847594] | [0.000577462044, 0.00988484192, 0.0100847594] | [0.000733733989, 0.0125598636, 0.0128138824] | [0.000156271945, 0.00267502165, 0.00272912305] | STALE | [inertia input L181](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/seeed_rebot_devarm/seeed_rebot_devarm.xml#L181) | [inertia input L119](https://github.com/Seeed-Projects/reBot-Isaacsim/blob/6a18beabefa9564d9b66c93fd671a8c7a4548601/urdf/00-arm-rs_asm-v3/urdf/00-arm-rs_asm-v3.urdf#L119) | [inertia input L119](https://github.com/Seeed-Projects/reBot-Isaacsim/blob/51aa87625e6aaa1ccb8514b0d0c66e3aa1c711bf/urdf/00-arm-rs_asm-v3/urdf/00-arm-rs_asm-v3.urdf#L119) |
| link3 / principal_moments | [0.000551215327, 0.0074591298, 0.00764228384] | [0.000551215327, 0.0074591298, 0.00764228384] | [0.000467564439, 0.00632715323, 0.00648251233] | [-8.36508882e-05, -0.00113197657, -0.00115977151] | STALE | [inertia input L193](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/seeed_rebot_devarm/seeed_rebot_devarm.xml#L193) | [inertia input L233](https://github.com/Seeed-Projects/reBot-Isaacsim/blob/6a18beabefa9564d9b66c93fd671a8c7a4548601/urdf/00-arm-rs_asm-v3/urdf/00-arm-rs_asm-v3.urdf#L233) | [inertia input L233](https://github.com/Seeed-Projects/reBot-Isaacsim/blob/51aa87625e6aaa1ccb8514b0d0c66e3aa1c711bf/urdf/00-arm-rs_asm-v3/urdf/00-arm-rs_asm-v3.urdf#L233) |
| link4 / principal_moments | [0.00022528902, 0.000465171515, 0.00061974492] | [0.00022528902, 0.000465171515, 0.00061974492] | [0.000323240768, 0.00066742, 0.000889199232] | [9.79517478e-05, 0.000202248485, 0.000269454312] | STALE | [inertia input L207](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/seeed_rebot_devarm/seeed_rebot_devarm.xml#L207) | [inertia input L347](https://github.com/Seeed-Projects/reBot-Isaacsim/blob/6a18beabefa9564d9b66c93fd671a8c7a4548601/urdf/00-arm-rs_asm-v3/urdf/00-arm-rs_asm-v3.urdf#L347) | [inertia input L347](https://github.com/Seeed-Projects/reBot-Isaacsim/blob/51aa87625e6aaa1ccb8514b0d0c66e3aa1c711bf/urdf/00-arm-rs_asm-v3/urdf/00-arm-rs_asm-v3.urdf#L347) |
| link5 / com_registered | [0.0875601078, -4.62077393e-06, 0.217697252] | [0.0875601712, -4.7004308e-06, 0.217697107] | [0.110440309, -4.63660584e-06, 0.227697076] | [0.0228802015, -1.58319056e-08, 0.00999982386] | STALE | [CoM/kinematic input L220](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/seeed_rebot_devarm/seeed_rebot_devarm.xml#L220) | [CoM/kinematic input L424](https://github.com/Seeed-Projects/reBot-Isaacsim/blob/6a18beabefa9564d9b66c93fd671a8c7a4548601/urdf/00-arm-rs_asm-v3/urdf/00-arm-rs_asm-v3.urdf#L424) | [CoM/kinematic input L424](https://github.com/Seeed-Projects/reBot-Isaacsim/blob/51aa87625e6aaa1ccb8514b0d0c66e3aa1c711bf/urdf/00-arm-rs_asm-v3/urdf/00-arm-rs_asm-v3.urdf#L424) |
| link5 / principal_moments | [7.09762071e-05, 7.39221452e-05, 9.84572417e-05] | [7.09762071e-05, 7.39221452e-05, 9.84572417e-05] | [5.2955957e-05, 5.51539467e-05, 7.34597927e-05] | [-1.80202501e-05, -1.87681985e-05, -2.4997449e-05] | STALE | [inertia input L220](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/seeed_rebot_devarm/seeed_rebot_devarm.xml#L220) | [inertia input L433](https://github.com/Seeed-Projects/reBot-Isaacsim/blob/6a18beabefa9564d9b66c93fd671a8c7a4548601/urdf/00-arm-rs_asm-v3/urdf/00-arm-rs_asm-v3.urdf#L433) | [inertia input L433](https://github.com/Seeed-Projects/reBot-Isaacsim/blob/51aa87625e6aaa1ccb8514b0d0c66e3aa1c711bf/urdf/00-arm-rs_asm-v3/urdf/00-arm-rs_asm-v3.urdf#L433) |
| link6 / principal_moments | [1.45728507e-05, 1.47424612e-05, 2.8476646e-05] | [1.45728507e-05, 1.47424612e-05, 2.8476646e-05] | [4.37185522e-06, 4.42273835e-06, 8.5429938e-06] | [-1.02009955e-05, -1.03197228e-05, -1.99336522e-05] | STALE | [inertia input L234](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/seeed_rebot_devarm/seeed_rebot_devarm.xml#L234) | [inertia input L533](https://github.com/Seeed-Projects/reBot-Isaacsim/blob/6a18beabefa9564d9b66c93fd671a8c7a4548601/urdf/00-arm-rs_asm-v3/urdf/00-arm-rs_asm-v3.urdf#L533) | [inertia input L533](https://github.com/Seeed-Projects/reBot-Isaacsim/blob/51aa87625e6aaa1ccb8514b0d0c66e3aa1c711bf/urdf/00-arm-rs_asm-v3/urdf/00-arm-rs_asm-v3.urdf#L533) |

## Raw CoM records and reporting decisions

Raw values retain the previous root-anchor registration before Kabsch; original world coordinates also remain in the snapshots. Eligible findings above use the fitted transform into M. Excluded raw records below are diagnostic numbers, not findings. No CoM suppression applies to mass or principal inertia moments.

| Entity / quantity | Raw M | Raw S | Raw H | Raw H − M | Decision | M source | S source | H source |
|---|---|---|---|---|---|---|---|---|
| robot / total_com_registered | [-0.0118333513, -0.000454569709, 0.155504459] | [-0.0118333504, -0.000454466111, 0.15550461] | [-0.0110671722, -0.000454463651, 0.155839477] | [0.000766179127, 1.06057569e-07, 0.000335017937] | eligible; compared after Kabsch alignment | [aggregate inputs](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/seeed_rebot_devarm/seeed_rebot_devarm.xml#L1) | [aggregate inputs](https://github.com/Seeed-Projects/reBot-Isaacsim/blob/6a18beabefa9564d9b66c93fd671a8c7a4548601/urdf/00-arm-rs_asm-v3/urdf/00-arm-rs_asm-v3.urdf#L1) | [aggregate inputs](https://github.com/Seeed-Projects/reBot-Isaacsim/blob/51aa87625e6aaa1ccb8514b0d0c66e3aa1c711bf/urdf/00-arm-rs_asm-v3/urdf/00-arm-rs_asm-v3.urdf#L1) |
| base_link / com_registered | [2.87641888e-06, -0.000122302489, 0.0243376122] | [2.87641888e-06, -0.000122302489, 0.0243376122] | [2.87641888e-06, -0.000122302489, 0.0243376122] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L155](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/seeed_rebot_devarm/seeed_rebot_devarm.xml#L155) | [CoM/kinematic input L12](https://github.com/Seeed-Projects/reBot-Isaacsim/blob/6a18beabefa9564d9b66c93fd671a8c7a4548601/urdf/00-arm-rs_asm-v3/urdf/00-arm-rs_asm-v3.urdf#L12) | [CoM/kinematic input L12](https://github.com/Seeed-Projects/reBot-Isaacsim/blob/51aa87625e6aaa1ccb8514b0d0c66e3aa1c711bf/urdf/00-arm-rs_asm-v3/urdf/00-arm-rs_asm-v3.urdf#L12) |
| link1 / com_registered | [0.0078336928, 0.000239012119, 0.108141966] | [0.0078336928, 0.000239012119, 0.108141966] | [0.0078336928, 0.000239012119, 0.108141966] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L166](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/seeed_rebot_devarm/seeed_rebot_devarm.xml#L166) | [CoM/kinematic input L52](https://github.com/Seeed-Projects/reBot-Isaacsim/blob/6a18beabefa9564d9b66c93fd671a8c7a4548601/urdf/00-arm-rs_asm-v3/urdf/00-arm-rs_asm-v3.urdf#L52) | [CoM/kinematic input L52](https://github.com/Seeed-Projects/reBot-Isaacsim/blob/51aa87625e6aaa1ccb8514b0d0c66e3aa1c711bf/urdf/00-arm-rs_asm-v3/urdf/00-arm-rs_asm-v3.urdf#L52) |
| link2 / com_registered | [-0.0978646427, -0.00090502385, 0.148422264] | [-0.0978646427, -0.000905011279, 0.148422364] | [-0.0978646427, -0.000905011279, 0.148422364] | [4.16333634e-17, 1.25708613e-08, 9.97465736e-08] | eligible; compared after Kabsch alignment | [CoM/kinematic input L181](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/seeed_rebot_devarm/seeed_rebot_devarm.xml#L181) | [CoM/kinematic input L110](https://github.com/Seeed-Projects/reBot-Isaacsim/blob/6a18beabefa9564d9b66c93fd671a8c7a4548601/urdf/00-arm-rs_asm-v3/urdf/00-arm-rs_asm-v3.urdf#L110) | [CoM/kinematic input L110](https://github.com/Seeed-Projects/reBot-Isaacsim/blob/51aa87625e6aaa1ccb8514b0d0c66e3aa1c711bf/urdf/00-arm-rs_asm-v3/urdf/00-arm-rs_asm-v3.urdf#L110) |
| link3 / com_registered | [-0.112572676, -0.000856698772, 0.211413791] | [-0.112572676, -0.00085645482, 0.211413891] | [-0.112572676, -0.00085645482, 0.211413891] | [4.16333634e-17, 2.4395166e-07, 9.95686406e-08] | eligible; compared after Kabsch alignment | [CoM/kinematic input L193](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/seeed_rebot_devarm/seeed_rebot_devarm.xml#L193) | [CoM/kinematic input L224](https://github.com/Seeed-Projects/reBot-Isaacsim/blob/6a18beabefa9564d9b66c93fd671a8c7a4548601/urdf/00-arm-rs_asm-v3/urdf/00-arm-rs_asm-v3.urdf#L224) | [CoM/kinematic input L224](https://github.com/Seeed-Projects/reBot-Isaacsim/blob/51aa87625e6aaa1ccb8514b0d0c66e3aa1c711bf/urdf/00-arm-rs_asm-v3/urdf/00-arm-rs_asm-v3.urdf#L224) |
| link4 / com_registered | [0.0595546241, -0.000661022492, 0.261857347] | [0.0595546241, -0.000660593251, 0.261857446] | [0.0595546241, -0.000660593251, 0.261857446] | [-2.08166817e-17, 4.29241185e-07, 9.88495412e-08] | eligible; compared after Kabsch alignment | [CoM/kinematic input L207](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/seeed_rebot_devarm/seeed_rebot_devarm.xml#L207) | [CoM/kinematic input L338](https://github.com/Seeed-Projects/reBot-Isaacsim/blob/6a18beabefa9564d9b66c93fd671a8c7a4548601/urdf/00-arm-rs_asm-v3/urdf/00-arm-rs_asm-v3.urdf#L338) | [CoM/kinematic input L338](https://github.com/Seeed-Projects/reBot-Isaacsim/blob/51aa87625e6aaa1ccb8514b0d0c66e3aa1c711bf/urdf/00-arm-rs_asm-v3/urdf/00-arm-rs_asm-v3.urdf#L338) |
| link5 / com_registered | [0.0875601078, -4.62077393e-06, 0.217697252] | [0.0875601078, -4.53023475e-06, 0.217697348] | [0.110440232, -4.45677064e-06, 0.227697348] | [0.0228801245, 1.64003289e-07, 0.0100000965] | eligible; compared after Kabsch alignment | [CoM/kinematic input L220](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/seeed_rebot_devarm/seeed_rebot_devarm.xml#L220) | [CoM/kinematic input L424](https://github.com/Seeed-Projects/reBot-Isaacsim/blob/6a18beabefa9564d9b66c93fd671a8c7a4548601/urdf/00-arm-rs_asm-v3/urdf/00-arm-rs_asm-v3.urdf#L424) | [CoM/kinematic input L424](https://github.com/Seeed-Projects/reBot-Isaacsim/blob/51aa87625e6aaa1ccb8514b0d0c66e3aa1c711bf/urdf/00-arm-rs_asm-v3/urdf/00-arm-rs_asm-v3.urdf#L424) |
| link6 / com_registered | [0.139848228, 1.45166541e-07, 0.21776402] | [0.139848228, 2.36196348e-07, 0.217764132] | [0.139848228, 2.36196348e-07, 0.217764132] | [-6.62190858e-11, 9.10298073e-08, 1.12393604e-07] | eligible; compared after Kabsch alignment | [CoM/kinematic input L234](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/seeed_rebot_devarm/seeed_rebot_devarm.xml#L234) | [CoM/kinematic input L524](https://github.com/Seeed-Projects/reBot-Isaacsim/blob/6a18beabefa9564d9b66c93fd671a8c7a4548601/urdf/00-arm-rs_asm-v3/urdf/00-arm-rs_asm-v3.urdf#L524) | [CoM/kinematic input L524](https://github.com/Seeed-Projects/reBot-Isaacsim/blob/51aa87625e6aaa1ccb8514b0d0c66e3aa1c711bf/urdf/00-arm-rs_asm-v3/urdf/00-arm-rs_asm-v3.urdf#L524) |
| gripper_end / com_registered | [0.188958477, 0.00012861307, 0.217740274] | [0.188958477, 0.000128703972, 0.217740981] | [0.188958477, 0.000128703972, 0.217740981] | [-1.12138077e-12, 9.09017957e-08, 7.06945535e-07] | eligible; compared after Kabsch alignment | [CoM/kinematic input L246](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/seeed_rebot_devarm/seeed_rebot_devarm.xml#L246) | [CoM/kinematic input L582](https://github.com/Seeed-Projects/reBot-Isaacsim/blob/6a18beabefa9564d9b66c93fd671a8c7a4548601/urdf/00-arm-rs_asm-v3/urdf/00-arm-rs_asm-v3.urdf#L582) | [CoM/kinematic input L582](https://github.com/Seeed-Projects/reBot-Isaacsim/blob/51aa87625e6aaa1ccb8514b0d0c66e3aa1c711bf/urdf/00-arm-rs_asm-v3/urdf/00-arm-rs_asm-v3.urdf#L582) |
| gripper_left / com_registered | [0.241062134, -0.00939510069, 0.215565913] | [0.241062177, -0.00939507851, 0.215566551] | [0.241062177, -0.00939507851, 0.215566551] | [4.22482359e-08, 2.21797336e-08, 6.3822355e-07] | eligible; compared after Kabsch alignment | [CoM/kinematic input L261](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/seeed_rebot_devarm/seeed_rebot_devarm.xml#L261) | [CoM/kinematic input L677](https://github.com/Seeed-Projects/reBot-Isaacsim/blob/6a18beabefa9564d9b66c93fd671a8c7a4548601/urdf/00-arm-rs_asm-v3/urdf/00-arm-rs_asm-v3.urdf#L677) | [CoM/kinematic input L677](https://github.com/Seeed-Projects/reBot-Isaacsim/blob/51aa87625e6aaa1ccb8514b0d0c66e3aa1c711bf/urdf/00-arm-rs_asm-v3/urdf/00-arm-rs_asm-v3.urdf#L677) |
| gripper_right / com_registered | [0.241062134, 0.00939544069, 0.219926087] | [0.241062161, 0.00939560031, 0.219926725] | [0.241062161, 0.00939560031, 0.219926725] | [2.62324223e-08, 1.59623858e-07, 6.38223521e-07] | eligible; compared after Kabsch alignment | [CoM/kinematic input L276](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/seeed_rebot_devarm/seeed_rebot_devarm.xml#L276) | [CoM/kinematic input L763](https://github.com/Seeed-Projects/reBot-Isaacsim/blob/6a18beabefa9564d9b66c93fd671a8c7a4548601/urdf/00-arm-rs_asm-v3/urdf/00-arm-rs_asm-v3.urdf#L763) | [CoM/kinematic input L763](https://github.com/Seeed-Projects/reBot-Isaacsim/blob/51aa87625e6aaa1ccb8514b0d0c66e3aa1c711bf/urdf/00-arm-rs_asm-v3/urdf/00-arm-rs_asm-v3.urdf#L763) |

## Mass accounting

Every contributing compiled body mass is listed here so total/subtree sums can be checked. Links point to explicit inertials or to geometry inputs when the compiler inferred a mass. CoM links identify inertial inputs; world coordinates additionally use the ancestor transforms and the registration recorded below.

| M body | M kg / source | S kg / source | H kg / source |
|---|---|---|---|
| base_link | 1.1774 / [input L155](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/seeed_rebot_devarm/seeed_rebot_devarm.xml#L155) | 1.1774 / [input L14](https://github.com/Seeed-Projects/reBot-Isaacsim/blob/6a18beabefa9564d9b66c93fd671a8c7a4548601/urdf/00-arm-rs_asm-v3/urdf/00-arm-rs_asm-v3.urdf#L14) | 1.1774 / [input L14](https://github.com/Seeed-Projects/reBot-Isaacsim/blob/51aa87625e6aaa1ccb8514b0d0c66e3aa1c711bf/urdf/00-arm-rs_asm-v3/urdf/00-arm-rs_asm-v3.urdf#L14) |
| link1 | 0.4655 / [input L166](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/seeed_rebot_devarm/seeed_rebot_devarm.xml#L166) | 0.4655 / [input L54](https://github.com/Seeed-Projects/reBot-Isaacsim/blob/6a18beabefa9564d9b66c93fd671a8c7a4548601/urdf/00-arm-rs_asm-v3/urdf/00-arm-rs_asm-v3.urdf#L54) | 0.4655 / [input L54](https://github.com/Seeed-Projects/reBot-Isaacsim/blob/51aa87625e6aaa1ccb8514b0d0c66e3aa1c711bf/urdf/00-arm-rs_asm-v3/urdf/00-arm-rs_asm-v3.urdf#L54) |
| link2 | 1.552 / [input L181](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/seeed_rebot_devarm/seeed_rebot_devarm.xml#L181) | 1.552 / [input L112](https://github.com/Seeed-Projects/reBot-Isaacsim/blob/6a18beabefa9564d9b66c93fd671a8c7a4548601/urdf/00-arm-rs_asm-v3/urdf/00-arm-rs_asm-v3.urdf#L112) | 1.552 / [input L112](https://github.com/Seeed-Projects/reBot-Isaacsim/blob/51aa87625e6aaa1ccb8514b0d0c66e3aa1c711bf/urdf/00-arm-rs_asm-v3/urdf/00-arm-rs_asm-v3.urdf#L112) |
| link3 | 1.252 / [input L193](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/seeed_rebot_devarm/seeed_rebot_devarm.xml#L193) | 1.252 / [input L226](https://github.com/Seeed-Projects/reBot-Isaacsim/blob/6a18beabefa9564d9b66c93fd671a8c7a4548601/urdf/00-arm-rs_asm-v3/urdf/00-arm-rs_asm-v3.urdf#L226) | 1.252 / [input L226](https://github.com/Seeed-Projects/reBot-Isaacsim/blob/51aa87625e6aaa1ccb8514b0d0c66e3aa1c711bf/urdf/00-arm-rs_asm-v3/urdf/00-arm-rs_asm-v3.urdf#L226) |
| link4 | 0.46 / [input L207](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/seeed_rebot_devarm/seeed_rebot_devarm.xml#L207) | 0.46 / [input L340](https://github.com/Seeed-Projects/reBot-Isaacsim/blob/6a18beabefa9564d9b66c93fd671a8c7a4548601/urdf/00-arm-rs_asm-v3/urdf/00-arm-rs_asm-v3.urdf#L340) | 0.46 / [input L340](https://github.com/Seeed-Projects/reBot-Isaacsim/blob/51aa87625e6aaa1ccb8514b0d0c66e3aa1c711bf/urdf/00-arm-rs_asm-v3/urdf/00-arm-rs_asm-v3.urdf#L340) |
| link5 | 0.201204572 / [input L220](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/seeed_rebot_devarm/seeed_rebot_devarm.xml#L220) | 0.201204572 / [input L426](https://github.com/Seeed-Projects/reBot-Isaacsim/blob/6a18beabefa9564d9b66c93fd671a8c7a4548601/urdf/00-arm-rs_asm-v3/urdf/00-arm-rs_asm-v3.urdf#L426) | 0.201204572 / [input L426](https://github.com/Seeed-Projects/reBot-Isaacsim/blob/51aa87625e6aaa1ccb8514b0d0c66e3aa1c711bf/urdf/00-arm-rs_asm-v3/urdf/00-arm-rs_asm-v3.urdf#L426) |
| link6 | 0.1 / [input L234](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/seeed_rebot_devarm/seeed_rebot_devarm.xml#L234) | 0.1 / [input L526](https://github.com/Seeed-Projects/reBot-Isaacsim/blob/6a18beabefa9564d9b66c93fd671a8c7a4548601/urdf/00-arm-rs_asm-v3/urdf/00-arm-rs_asm-v3.urdf#L526) | 0.1 / [input L526](https://github.com/Seeed-Projects/reBot-Isaacsim/blob/51aa87625e6aaa1ccb8514b0d0c66e3aa1c711bf/urdf/00-arm-rs_asm-v3/urdf/00-arm-rs_asm-v3.urdf#L526) |
| gripper_end | 0.65 / [input L246](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/seeed_rebot_devarm/seeed_rebot_devarm.xml#L246) | 0.65 / [input L584](https://github.com/Seeed-Projects/reBot-Isaacsim/blob/6a18beabefa9564d9b66c93fd671a8c7a4548601/urdf/00-arm-rs_asm-v3/urdf/00-arm-rs_asm-v3.urdf#L584) | 0.65 / [input L584](https://github.com/Seeed-Projects/reBot-Isaacsim/blob/51aa87625e6aaa1ccb8514b0d0c66e3aa1c711bf/urdf/00-arm-rs_asm-v3/urdf/00-arm-rs_asm-v3.urdf#L584) |
| gripper_left | 0.0752 / [input L261](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/seeed_rebot_devarm/seeed_rebot_devarm.xml#L261) | 0.0752 / [input L679](https://github.com/Seeed-Projects/reBot-Isaacsim/blob/6a18beabefa9564d9b66c93fd671a8c7a4548601/urdf/00-arm-rs_asm-v3/urdf/00-arm-rs_asm-v3.urdf#L679) | 0.0752 / [input L679](https://github.com/Seeed-Projects/reBot-Isaacsim/blob/51aa87625e6aaa1ccb8514b0d0c66e3aa1c711bf/urdf/00-arm-rs_asm-v3/urdf/00-arm-rs_asm-v3.urdf#L679) |
| gripper_right | 0.0752 / [input L276](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/seeed_rebot_devarm/seeed_rebot_devarm.xml#L276) | 0.0752 / [input L765](https://github.com/Seeed-Projects/reBot-Isaacsim/blob/6a18beabefa9564d9b66c93fd671a8c7a4548601/urdf/00-arm-rs_asm-v3/urdf/00-arm-rs_asm-v3.urdf#L765) | 0.0752 / [input L765](https://github.com/Seeed-Projects/reBot-Isaacsim/blob/51aa87625e6aaa1ccb8514b0d0c66e3aa1c711bf/urdf/00-arm-rs_asm-v3/urdf/00-arm-rs_asm-v3.urdf#L765) |

## Coverage and unmatched elements

```json
{
  "mapping_h": {
    "bodies": {
      "base_link": "base_link",
      "link1": "link1",
      "link2": "link2",
      "link3": "link3",
      "link4": "link4",
      "link5": "link5",
      "link6": "link6",
      "gripper_end": "gripper_end",
      "gripper_left": "gripper_left",
      "gripper_right": "gripper_right"
    },
    "joints": {
      "joint1": "joint1",
      "joint2": "joint2",
      "joint3": "joint3",
      "joint4": "joint4",
      "joint5": "joint5",
      "joint6": "joint6",
      "joint_left": "gripper_joint1",
      "joint_right": "gripper_joint2"
    },
    "body_methods": {
      "base_link": "name",
      "link1": "name",
      "link2": "name",
      "link3": "name",
      "link4": "name",
      "link5": "name",
      "link6": "name",
      "gripper_end": "name",
      "gripper_left": "name",
      "gripper_right": "name"
    },
    "joint_methods": {
      "joint1": "name",
      "joint2": "name",
      "joint3": "name",
      "joint4": "name",
      "joint5": "name",
      "joint6": "name",
      "joint_left": "unique joint on matched body with same type and axis",
      "joint_right": "unique joint on matched body with same type and axis"
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
      "link1": "link1",
      "link2": "link2",
      "link3": "link3",
      "link4": "link4",
      "link5": "link5",
      "link6": "link6",
      "gripper_end": "gripper_end",
      "gripper_left": "gripper_left",
      "gripper_right": "gripper_right"
    },
    "joints": {
      "joint1": "joint1",
      "joint2": "joint2",
      "joint3": "joint3",
      "joint4": "joint4",
      "joint5": "joint5",
      "joint6": "joint6",
      "joint_left": "joint_left",
      "joint_right": "joint_right"
    },
    "body_methods": {
      "base_link": "name",
      "link1": "name",
      "link2": "name",
      "link3": "name",
      "link4": "name",
      "link5": "name",
      "link6": "name",
      "gripper_end": "name",
      "gripper_left": "name",
      "gripper_right": "name"
    },
    "joint_methods": {
      "joint1": "name",
      "joint2": "name",
      "joint3": "name",
      "joint4": "name",
      "joint5": "name",
      "joint6": "name",
      "joint_left": "name",
      "joint_right": "name"
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
      "entity": "joint1",
      "other_entity": "joint1",
      "quantity": "force",
      "tolerance": "limit",
      "m": 36.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "joint1",
      "other_entity": "joint1",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 50.0,
      "s": 50.0,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "joint2",
      "other_entity": "joint2",
      "quantity": "force",
      "tolerance": "limit",
      "m": 36.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "joint2",
      "other_entity": "joint2",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 50.0,
      "s": 50.0,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "joint3",
      "other_entity": "joint3",
      "quantity": "force",
      "tolerance": "limit",
      "m": 36.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "joint3",
      "other_entity": "joint3",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 50.0,
      "s": 50.0,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "joint4",
      "other_entity": "joint4",
      "quantity": "force",
      "tolerance": "limit",
      "m": 14.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "joint4",
      "other_entity": "joint4",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 40.0,
      "s": 40.0,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "joint5",
      "other_entity": "joint5",
      "quantity": "force",
      "tolerance": "limit",
      "m": 14.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "joint5",
      "other_entity": "joint5",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 40.0,
      "s": 40.0,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "joint6",
      "other_entity": "joint6",
      "quantity": "force",
      "tolerance": "limit",
      "m": 14.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "joint6",
      "other_entity": "joint6",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 40.0,
      "s": 40.0,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "joint_left",
      "other_entity": "gripper_joint1",
      "quantity": "force",
      "tolerance": "limit",
      "m": 1904.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "joint_left",
      "other_entity": "gripper_joint1",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 0.243,
      "s": 0.243,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "joint_right",
      "other_entity": "gripper_joint2",
      "quantity": "force",
      "tolerance": "limit",
      "m": 1904.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "joint_right",
      "other_entity": "gripper_joint2",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 0.243,
      "s": 0.243,
      "reason": "quantity absent or not enforced/declared on one side"
    }
  ]
}
```

## Limits unavailable for a like-for-like simulator comparison

URDF effort and velocity tags are manufacturer declarations; MuJoCo ignores them. Missing enforced quantities are not interpreted as zero. The available values are shown for review and excluded from STALE counts.

| Joint / quantity | M | S | H / declared upstream |
|---|---|---|---|
| joint1 / force | 36 | unavailable | unavailable |
| joint1 / velocity | unavailable | 50 | 50 |
| joint2 / force | 36 | unavailable | unavailable |
| joint2 / velocity | unavailable | 50 | 50 |
| joint3 / force | 36 | unavailable | unavailable |
| joint3 / velocity | unavailable | 50 | 50 |
| joint4 / force | 14 | unavailable | unavailable |
| joint4 / velocity | unavailable | 40 | 40 |
| joint5 / force | 14 | unavailable | unavailable |
| joint5 / velocity | unavailable | 40 | 40 |
| joint6 / force | 14 | unavailable | unavailable |
| joint6 / velocity | unavailable | 40 | 40 |
| joint_left / force | 1904 | unavailable | unavailable |
| joint_left / velocity | unavailable | 0.243 | 0.243 |
| joint_right / force | 1904 | unavailable | unavailable |
| joint_right / velocity | unavailable | 0.243 | 0.243 |
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
    "file": "seeed_rebot_devarm/seeed_rebot_devarm.xml",
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
    "counts": {
      "STALE": 7
    },
    "classifications_changed": 0,
    "finding_membership_changes": 0
  },
  "2": {
    "provenance_method": "dated match",
    "counts": {
      "STALE": 6
    },
    "classifications_changed": 1,
    "finding_membership_changes": 1
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
      "seeed_rebot_devarm/seeed_rebot_devarm.xml"
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
      "urdf/00-arm-rs_asm-v3/urdf/00-arm-rs_asm-v3.urdf"
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
      "urdf/00-arm-rs_asm-v3/urdf/00-arm-rs_asm-v3.urdf"
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
  "historical_snapshots_reused": 6,
  "primary_physics_unchanged": true,
  "source_matching": "original raw-value provenance criteria retained; kinematic guard applies to reported CoM"
}
```
