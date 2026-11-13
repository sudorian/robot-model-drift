# ufactory_xarm7

Status: **partial history**. Provenance: **dated match**, confidence **medium**.

Source selected using the ordered amended provenance rules.

M: `https://github.com/google-deepmind/mujoco_menagerie`, `ufactory_xarm7/xarm7_nohand.xml`, commit `370c43965323c0944b433b202aac5058b5f907a9`.
H: `https://github.com/xArm-Developer/xarm_ros`, `xarm_description/urdf/xarm_device.urdf.xacro`, commit `cf51617d98bc55a88d9aa735acfa43a0bbb8e425`.
S: `fcc2060b1ccd8a72ac3f332ff9c3c590182870e7` (2023-07-07T11:26:39+08:00). Menagerie release/change: 2023-08-24T12:39:42-07:00.

Limit semantics: MJCF effort values are supported actuator torque/force envelopes. URDF effort and velocity values are manufacturer declarations retained from XML; MuJoCo does not enforce those tags. Such declaration comparisons are explicitly distinct from compiled inertial/range quantities.


## Source evidence

```json
[
  {
    "url": "https://github.com/xArm-Developer/xarm_ros/tree/master/xarm_description/urdf/xarm7",
    "document": "ufactory_xarm7/README.md",
    "commit": "370c43965323c0944b433b202aac5058b5f907a9",
    "current": true
  },
  {
    "url": "https://github.com/s1lent4gnt",
    "document": "ufactory_xarm7/README.md",
    "commit": "ffdf57667476eca8e550c33704a5e9fa90c45ce4",
    "current": false
  },
  {
    "url": "https://github.com/google-deepmind/mujoco_menagerie/issues/83",
    "document": "ufactory_xarm7/README.md",
    "commit": "b5a72f92f0630bc3b90711ed41ff640e93b1f90b",
    "current": false
  },
  {
    "url": "https://github.com/google-deepmind/mujoco_menagerie/pull/131",
    "document": "ufactory_xarm7/README.md",
    "commit": "b5a72f92f0630bc3b90711ed41ff640e93b1f90b",
    "current": false
  },
  {
    "url": "https://github.com/s1lent4gnt",
    "document": "ufactory_xarm7/CHANGELOG.md",
    "commit": "370c43965323c0944b433b202aac5058b5f907a9",
    "current": true
  }
]
```


## README derivation evidence

Documentation labels are conservative: an automated documented label requires an explicit affected entity and quantity. Broader conversion notes are retained here for review.

> 1. Added `<mujoco> <compiler discardvisual="false" fusestatic="false"/> </mujoco>` to the URDF's

## Kinematics consistency

A proper Kabsch rigid transform aligns all matched zero-pose body origins. The maximum per-origin residual and signed hinge/slide axis angles determine whether CoM can be compared; RMS is also recorded. Fewer than three non-collinear origins give insufficient kinematic coverage. CoM records that fail either required M/H or M/S check are excluded from counts and largest discrepancies. Masses, principal moments and raw joint ranges remain unchanged; a flagged range still requires convention review.

| Pair | Status | Origins / rank | RMS / maximum mm | Disagreeing / checked axes |
|---|---|---:|---:|---:|
| M/H | consistent | 8 / 2 | 0.000247308396 / 0.000501913535 | 0 / 7 |
| M/S | consistent | 8 / 2 | 0.000247308396 / 0.000501913535 | 0 / 7 |

Exact fitted transforms, per-origin residuals, thresholds and axis vectors:

```json
{
  "M/H": {
    "status": "consistent",
    "matched_body_origins": 8,
    "position_threshold_m": 0.005,
    "axis_threshold_rad": 0.005,
    "residual_definition": "maximum Euclidean residual over matched body origins; Kabsch minimizes RMS, which is also recorded",
    "coordinate_frames": "each snapshot registered to its matched report anchor",
    "anchor_m": "link_base",
    "anchor_other": "link_base",
    "rotation_other_to_m": [
      [
        0.9999999998661562,
        1.636114207912547e-05,
        -4.3011699717584466e-13
      ],
      [
        -1.6361142079097756e-05,
        0.9999999998653668,
        -1.256802575587136e-06
      ],
      [
        -2.0132617796915348e-11,
        1.2568025753363988e-06,
        0.9999999999992103
      ]
    ],
    "translation_other_to_m": [
      -1.2116752046154033e-11,
      1.294738819067963e-07,
      -4.505840145441198e-13
    ],
    "rms_residual_m": 2.473083960231763e-07,
    "max_residual_m": 5.019135347337232e-07,
    "fit_rank": 2,
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
          -4.3011699717584466e-13,
          -1.256802575587136e-06,
          0.9999999999992103
        ],
        "angle_rad": 1.2568025755875403e-06,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "joint2",
        "joint_other": "joint2",
        "axis_m": [
          0.0,
          1.0,
          2.2204460492503136e-16
        ],
        "axis_other_aligned": [
          1.6361142079016674e-05,
          0.9999999998632371,
          -2.416402527863201e-06
        ],
        "angle_rad": 1.6538620599446788e-05,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "joint3",
        "joint_other": "joint3",
        "axis_m": [
          0.0,
          -4.474228634151475e-17,
          1.0
        ],
        "axis_other_aligned": [
          -4.30116996428877e-13,
          -1.256802575541481e-06,
          0.9999999999992103
        ],
        "angle_rad": 1.256802575497143e-06,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "joint4",
        "joint_other": "joint4",
        "axis_m": [
          0.0,
          -1.0,
          4.440892098500629e-16
        ],
        "axis_other_aligned": [
          -1.6361142079013517e-05,
          -0.999999999854004,
          -4.930007678296997e-06
        ],
        "angle_rad": 1.7087771822871834e-05,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "joint5",
        "joint_other": "joint5",
        "axis_m": [
          0.0,
          1.5825390293272476e-16,
          -1.0
        ],
        "axis_other_aligned": [
          1.2062577816117328e-10,
          8.60321278130405e-06,
          -0.9999999999629924
        ],
        "angle_rad": 8.60321278209757e-06,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "joint6",
        "joint_other": "joint6",
        "axis_m": [
          0.0,
          1.0,
          1.443289932012705e-15
        ],
        "axis_other_aligned": [
          1.6361142078127347e-05,
          0.9999999997908013,
          1.2276417885832662e-05
        ],
        "angle_rad": 2.0454764878413456e-05,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "joint7",
        "joint_other": "joint7",
        "axis_m": [
          0.0,
          2.858353069173386e-16,
          -1.0
        ],
        "axis_other_aligned": [
          1.2062577815959272e-10,
          8.603212781207446e-06,
          -0.9999999999629924
        ],
        "angle_rad": 8.603212781873386e-06,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      }
    ],
    "axis_disagreements": [],
    "com_eligible": true,
    "covariance_singular_values": [
      0.27328924962731144,
      0.04077218787617846,
      1.8045061279944904e-22
    ],
    "origin_residuals_m": {
      "link_base": 1.2947388247455059e-07,
      "link1": 2.060924061390032e-07,
      "link2": 2.060924061390032e-07,
      "link3": 5.019135347337232e-07,
      "link4": 3.570464244623598e-07,
      "link5": 6.34926948115455e-08,
      "link6": 6.34926948115455e-08,
      "link7": 1.0858444178060577e-08
    },
    "reason": "Unique proper rigid fit and matched signed axes meet the configured thresholds"
  },
  "M/S": {
    "status": "consistent",
    "matched_body_origins": 8,
    "position_threshold_m": 0.005,
    "axis_threshold_rad": 0.005,
    "residual_definition": "maximum Euclidean residual over matched body origins; Kabsch minimizes RMS, which is also recorded",
    "coordinate_frames": "each snapshot registered to its matched report anchor",
    "anchor_m": "link_base",
    "anchor_other": "link_base",
    "rotation_other_to_m": [
      [
        0.9999999998661562,
        1.636114207912547e-05,
        -4.3011699717584466e-13
      ],
      [
        -1.6361142079097756e-05,
        0.9999999998653668,
        -1.256802575587136e-06
      ],
      [
        -2.0132617796915348e-11,
        1.2568025753363988e-06,
        0.9999999999992103
      ]
    ],
    "translation_other_to_m": [
      -1.2116752046154033e-11,
      1.294738819067963e-07,
      -4.505840145441198e-13
    ],
    "rms_residual_m": 2.473083960231763e-07,
    "max_residual_m": 5.019135347337232e-07,
    "fit_rank": 2,
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
          -4.3011699717584466e-13,
          -1.256802575587136e-06,
          0.9999999999992103
        ],
        "angle_rad": 1.2568025755875403e-06,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "joint2",
        "joint_other": "joint2",
        "axis_m": [
          0.0,
          1.0,
          2.2204460492503136e-16
        ],
        "axis_other_aligned": [
          1.6361142079016674e-05,
          0.9999999998632371,
          -2.416402527863201e-06
        ],
        "angle_rad": 1.6538620599446788e-05,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "joint3",
        "joint_other": "joint3",
        "axis_m": [
          0.0,
          -4.474228634151475e-17,
          1.0
        ],
        "axis_other_aligned": [
          -4.30116996428877e-13,
          -1.256802575541481e-06,
          0.9999999999992103
        ],
        "angle_rad": 1.256802575497143e-06,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "joint4",
        "joint_other": "joint4",
        "axis_m": [
          0.0,
          -1.0,
          4.440892098500629e-16
        ],
        "axis_other_aligned": [
          -1.6361142079013517e-05,
          -0.999999999854004,
          -4.930007678296997e-06
        ],
        "angle_rad": 1.7087771822871834e-05,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "joint5",
        "joint_other": "joint5",
        "axis_m": [
          0.0,
          1.5825390293272476e-16,
          -1.0
        ],
        "axis_other_aligned": [
          1.2062577816117328e-10,
          8.60321278130405e-06,
          -0.9999999999629924
        ],
        "angle_rad": 8.60321278209757e-06,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "joint6",
        "joint_other": "joint6",
        "axis_m": [
          0.0,
          1.0,
          1.443289932012705e-15
        ],
        "axis_other_aligned": [
          1.6361142078127347e-05,
          0.9999999997908013,
          1.2276417885832662e-05
        ],
        "angle_rad": 2.0454764878413456e-05,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "joint7",
        "joint_other": "joint7",
        "axis_m": [
          0.0,
          2.858353069173386e-16,
          -1.0
        ],
        "axis_other_aligned": [
          1.2062577815959272e-10,
          8.603212781207446e-06,
          -0.9999999999629924
        ],
        "angle_rad": 8.603212781873386e-06,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      }
    ],
    "axis_disagreements": [],
    "com_eligible": true,
    "covariance_singular_values": [
      0.27328924962731144,
      0.04077218787617846,
      1.8045061279944904e-22
    ],
    "origin_residuals_m": {
      "link_base": 1.2947388247455059e-07,
      "link1": 2.060924061390032e-07,
      "link2": 2.060924061390032e-07,
      "link3": 5.019135347337232e-07,
      "link4": 3.570464244623598e-07,
      "link5": 6.34926948115455e-08,
      "link6": 6.34926948115455e-08,
      "link7": 1.0858444178060577e-08
    },
    "reason": "Unique proper rigid fit and matched signed axes meet the configured thresholds"
  }
}
```


## Every reported quantity difference

Counts are quantity records, including correlated total/subtree/body mass records; they are not independent robot defects.

| Entity / quantity | M | S | H | H − M | Class | M source | S source | H source |
|---|---|---|---|---|---|---|---|---|
| joint1 / effort | 50 | 50 | 163.2 | 113.2 | STALE | [inherited actuator input L28](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ufactory_xarm7/xarm7_nohand.xml#L28) | [geometry/inference input L9](https://github.com/xArm-Developer/xarm_ros/blob/fcc2060b1ccd8a72ac3f332ff9c3c590182870e7/xarm_description/urdf/xarm7/xarm7.transmission.xacro#L9) | [geometry/inference input L9](https://github.com/xArm-Developer/xarm_ros/blob/cf51617d98bc55a88d9aa735acfa43a0bbb8e425/xarm_description/urdf/xarm7/xarm7.transmission.xacro#L9) |
| joint2 / effort | 50 | 50 | 163.2 | 113.2 | STALE | [inherited actuator input L28](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ufactory_xarm7/xarm7_nohand.xml#L28) | [geometry/inference input L20](https://github.com/xArm-Developer/xarm_ros/blob/fcc2060b1ccd8a72ac3f332ff9c3c590182870e7/xarm_description/urdf/xarm7/xarm7.transmission.xacro#L20) | [geometry/inference input L20](https://github.com/xArm-Developer/xarm_ros/blob/cf51617d98bc55a88d9aa735acfa43a0bbb8e425/xarm_description/urdf/xarm7/xarm7.transmission.xacro#L20) |
| joint3 / effort | 30 | 30 | 81.6 | 51.6 | STALE | [inherited actuator input L32](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ufactory_xarm7/xarm7_nohand.xml#L32) | [geometry/inference input L31](https://github.com/xArm-Developer/xarm_ros/blob/fcc2060b1ccd8a72ac3f332ff9c3c590182870e7/xarm_description/urdf/xarm7/xarm7.transmission.xacro#L31) | [geometry/inference input L31](https://github.com/xArm-Developer/xarm_ros/blob/cf51617d98bc55a88d9aa735acfa43a0bbb8e425/xarm_description/urdf/xarm7/xarm7.transmission.xacro#L31) |
| joint4 / effort | 30 | 30 | 81.6 | 51.6 | STALE | [inherited actuator input L32](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ufactory_xarm7/xarm7_nohand.xml#L32) | [geometry/inference input L42](https://github.com/xArm-Developer/xarm_ros/blob/fcc2060b1ccd8a72ac3f332ff9c3c590182870e7/xarm_description/urdf/xarm7/xarm7.transmission.xacro#L42) | [geometry/inference input L42](https://github.com/xArm-Developer/xarm_ros/blob/cf51617d98bc55a88d9aa735acfa43a0bbb8e425/xarm_description/urdf/xarm7/xarm7.transmission.xacro#L42) |
| joint5 / effort | 30 | 30 | 81.6 | 51.6 | STALE | [inherited actuator input L32](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ufactory_xarm7/xarm7_nohand.xml#L32) | [geometry/inference input L53](https://github.com/xArm-Developer/xarm_ros/blob/fcc2060b1ccd8a72ac3f332ff9c3c590182870e7/xarm_description/urdf/xarm7/xarm7.transmission.xacro#L53) | [geometry/inference input L53](https://github.com/xArm-Developer/xarm_ros/blob/cf51617d98bc55a88d9aa735acfa43a0bbb8e425/xarm_description/urdf/xarm7/xarm7.transmission.xacro#L53) |
| joint6 / effort | 20 | 20 | 30.6 | 10.6 | STALE | [inherited actuator input L36](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ufactory_xarm7/xarm7_nohand.xml#L36) | [geometry/inference input L64](https://github.com/xArm-Developer/xarm_ros/blob/fcc2060b1ccd8a72ac3f332ff9c3c590182870e7/xarm_description/urdf/xarm7/xarm7.transmission.xacro#L64) | [geometry/inference input L64](https://github.com/xArm-Developer/xarm_ros/blob/cf51617d98bc55a88d9aa735acfa43a0bbb8e425/xarm_description/urdf/xarm7/xarm7.transmission.xacro#L64) |
| joint7 / effort | 20 | 20 | 30.6 | 10.6 | STALE | [inherited actuator input L36](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ufactory_xarm7/xarm7_nohand.xml#L36) | [geometry/inference input L75](https://github.com/xArm-Developer/xarm_ros/blob/fcc2060b1ccd8a72ac3f332ff9c3c590182870e7/xarm_description/urdf/xarm7/xarm7.transmission.xacro#L75) | [geometry/inference input L75](https://github.com/xArm-Developer/xarm_ros/blob/cf51617d98bc55a88d9aa735acfa43a0bbb8e425/xarm_description/urdf/xarm7/xarm7.transmission.xacro#L75) |

## Raw CoM records and reporting decisions

Raw values retain the previous root-anchor registration before Kabsch; original world coordinates also remain in the snapshots. Eligible findings above use the fitted transform into M. Excluded raw records below are diagnostic numbers, not findings. No CoM suppression applies to mass or principal inertia moments.

| Entity / quantity | Raw M | Raw S | Raw H | Raw H − M | Decision | M source | S source | H source |
|---|---|---|---|---|---|---|---|---|
| robot / total_com_registered | [0.0648688298, 0.00419261001, 0.323104139] | [0.0648688298, 0.00419368846, 0.323104136] | [0.0648688298, 0.00419368846, 0.323104136] | [1.38777878e-17, 1.07844867e-06, -2.62888317e-09] | eligible; compared after Kabsch alignment | [aggregate inputs](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ufactory_xarm7/xarm7_nohand.xml#L1) | [aggregate inputs](https://github.com/xArm-Developer/xarm_ros/blob/fcc2060b1ccd8a72ac3f332ff9c3c590182870e7/xarm_description/urdf/xarm_device.urdf.xacro#L1) | [aggregate inputs](https://github.com/xArm-Developer/xarm_ros/blob/cf51617d98bc55a88d9aa735acfa43a0bbb8e425/xarm_description/urdf/xarm_device.urdf.xacro#L1) |
| link_base / com_registered | [-0.021131, -0.0016302, 0.056488] | [-0.021131, -0.0016302, 0.056488] | [-0.021131, -0.0016302, 0.056488] | [0, 0, 1.38777878e-17] | eligible; compared after Kabsch alignment | [CoM/kinematic input L45](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ufactory_xarm7/xarm7_nohand.xml#L45) | [CoM/kinematic input L43](https://github.com/xArm-Developer/xarm_ros/blob/fcc2060b1ccd8a72ac3f332ff9c3c590182870e7/xarm_description/urdf/xarm7/xarm7.urdf.xacro#L43) | [CoM/kinematic input L70](https://github.com/xArm-Developer/xarm_ros/blob/cf51617d98bc55a88d9aa735acfa43a0bbb8e425/xarm_description/urdf/xarm7/xarm7.urdf.xacro#L70) |
| link1 / com_registered | [-0.0002, 0.02905, 0.25467] | [-0.0002, 0.02905, 0.25467] | [-0.0002, 0.02905, 0.25467] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L49](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ufactory_xarm7/xarm7_nohand.xml#L49) | [geometry/inference input L59](https://github.com/xArm-Developer/xarm_ros/blob/fcc2060b1ccd8a72ac3f332ff9c3c590182870e7/xarm_description/urdf/xarm7/xarm7.urdf.xacro#L59) | [geometry/inference input L88](https://github.com/xArm-Developer/xarm_ros/blob/cf51617d98bc55a88d9aa735acfa43a0bbb8e425/xarm_description/urdf/xarm7/xarm7.urdf.xacro#L88) |
| link2 / com_registered | [0.00022, 0.01735, 0.39556] | [0.00022, 0.0173504722, 0.395559936] | [0.00022, 0.0173504722, 0.395559936] | [2.71050543e-20, 4.72227131e-07, -6.37309758e-08] | eligible; compared after Kabsch alignment | [CoM/kinematic input L54](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ufactory_xarm7/xarm7_nohand.xml#L54) | [geometry/inference input L85](https://github.com/xArm-Developer/xarm_ros/blob/fcc2060b1ccd8a72ac3f332ff9c3c590182870e7/xarm_description/urdf/xarm7/xarm7.urdf.xacro#L85) | [geometry/inference input L117](https://github.com/xArm-Developer/xarm_ros/blob/cf51617d98bc55a88d9aa735acfa43a0bbb8e425/xarm_description/urdf/xarm7/xarm7.urdf.xacro#L117) |
| link3 / com_registered | [0.0466, -0.02463, 0.55232] | [0.0466, -0.0246289238, 0.55232] | [0.0466, -0.0246289238, 0.55232] | [1.38777878e-17, 1.0762491e-06, -1.97653005e-12] | eligible; compared after Kabsch alignment | [CoM/kinematic input L59](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ufactory_xarm7/xarm7_nohand.xml#L59) | [geometry/inference input L111](https://github.com/xArm-Developer/xarm_ros/blob/fcc2060b1ccd8a72ac3f332ff9c3c590182870e7/xarm_description/urdf/xarm7/xarm7.urdf.xacro#L111) | [geometry/inference input L146](https://github.com/xArm-Developer/xarm_ros/blob/cf51617d98bc55a88d9aa735acfa43a0bbb8e425/xarm_description/urdf/xarm7/xarm7.urdf.xacro#L146) |
| link4 / com_registered | [0.12297, -0.012, 0.44425] | [0.12297, -0.0119984986, 0.444249956] | [0.12297, -0.0119984986, 0.444249956] | [2.77555756e-17, 1.50142267e-06, -4.40796569e-08] | eligible; compared after Kabsch alignment | [CoM/kinematic input L64](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ufactory_xarm7/xarm7_nohand.xml#L64) | [geometry/inference input L137](https://github.com/xArm-Developer/xarm_ros/blob/fcc2060b1ccd8a72ac3f332ff9c3c590182870e7/xarm_description/urdf/xarm7/xarm7.urdf.xacro#L137) | [geometry/inference input L175](https://github.com/xArm-Developer/xarm_ros/blob/cf51617d98bc55a88d9aa735acfa43a0bbb8e425/xarm_description/urdf/xarm7/xarm7.urdf.xacro#L175) |
| link5 / com_registered | [0.12968, -0.01604, 0.2435] | [0.12968, -0.0160378567, 0.243499882] | [0.12968, -0.0160378567, 0.243499882] | [2.77555756e-17, 2.14331561e-06, -1.17836787e-07] | eligible; compared after Kabsch alignment | [CoM/kinematic input L69](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ufactory_xarm7/xarm7_nohand.xml#L69) | [geometry/inference input L163](https://github.com/xArm-Developer/xarm_ros/blob/fcc2060b1ccd8a72ac3f332ff9c3c590182870e7/xarm_description/urdf/xarm7/xarm7.urdf.xacro#L163) | [geometry/inference input L204](https://github.com/xArm-Developer/xarm_ros/blob/cf51617d98bc55a88d9aa735acfa43a0bbb8e425/xarm_description/urdf/xarm7/xarm7.urdf.xacro#L204) |
| link6 / com_registered | [0.19469, 0.02141, 0.18472] | [0.19469, 0.0214126955, 0.184720236] | [0.19469, 0.0214126955, 0.184720236] | [5.55111512e-17, 2.69554353e-06, 2.35932288e-07] | eligible; compared after Kabsch alignment | [CoM/kinematic input L74](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ufactory_xarm7/xarm7_nohand.xml#L74) | [geometry/inference input L189](https://github.com/xArm-Developer/xarm_ros/blob/fcc2060b1ccd8a72ac3f332ff9c3c590182870e7/xarm_description/urdf/xarm7/xarm7.urdf.xacro#L189) | [geometry/inference input L233](https://github.com/xArm-Developer/xarm_ros/blob/cf51617d98bc55a88d9aa735acfa43a0bbb8e425/xarm_description/urdf/xarm7/xarm7.urdf.xacro#L233) |
| link7 / com_registered | [0.206, 0.00677, 0.13148] | [0.206, 0.00677332256, 0.13148005] | [0.206, 0.00677332256, 0.13148005] | [5.55111512e-17, 3.32256076e-06, 4.97411242e-08] | eligible; compared after Kabsch alignment | [CoM/kinematic input L79](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ufactory_xarm7/xarm7_nohand.xml#L79) | [geometry/inference input L215](https://github.com/xArm-Developer/xarm_ros/blob/fcc2060b1ccd8a72ac3f332ff9c3c590182870e7/xarm_description/urdf/xarm7/xarm7.urdf.xacro#L215) | [geometry/inference input L262](https://github.com/xArm-Developer/xarm_ros/blob/cf51617d98bc55a88d9aa735acfa43a0bbb8e425/xarm_description/urdf/xarm7/xarm7.urdf.xacro#L262) |

## Mass accounting

Every contributing compiled body mass is listed here so total/subtree sums can be checked. Links point to explicit inertials or to geometry inputs when the compiler inferred a mass. CoM links identify inertial inputs; world coordinates additionally use the ancestor transforms and the registration recorded below.

| M body | M kg / source | S kg / source | H kg / source |
|---|---|---|---|
| link_base | 0.88556 / [input L45](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ufactory_xarm7/xarm7_nohand.xml#L45) | 0.88556 / [input L44](https://github.com/xArm-Developer/xarm_ros/blob/fcc2060b1ccd8a72ac3f332ff9c3c590182870e7/xarm_description/urdf/xarm7/xarm7.urdf.xacro#L44) | 0.88556 / [input L71](https://github.com/xArm-Developer/xarm_ros/blob/cf51617d98bc55a88d9aa735acfa43a0bbb8e425/xarm_description/urdf/xarm7/xarm7.urdf.xacro#L71) |
| link1 | 2.382 / [input L49](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ufactory_xarm7/xarm7_nohand.xml#L49) | 2.382 / [geometry/inference input L59](https://github.com/xArm-Developer/xarm_ros/blob/fcc2060b1ccd8a72ac3f332ff9c3c590182870e7/xarm_description/urdf/xarm7/xarm7.urdf.xacro#L59) | 2.382 / [geometry/inference input L88](https://github.com/xArm-Developer/xarm_ros/blob/cf51617d98bc55a88d9aa735acfa43a0bbb8e425/xarm_description/urdf/xarm7/xarm7.urdf.xacro#L88) |
| link2 | 1.869 / [input L54](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ufactory_xarm7/xarm7_nohand.xml#L54) | 1.869 / [geometry/inference input L85](https://github.com/xArm-Developer/xarm_ros/blob/fcc2060b1ccd8a72ac3f332ff9c3c590182870e7/xarm_description/urdf/xarm7/xarm7.urdf.xacro#L85) | 1.869 / [geometry/inference input L117](https://github.com/xArm-Developer/xarm_ros/blob/cf51617d98bc55a88d9aa735acfa43a0bbb8e425/xarm_description/urdf/xarm7/xarm7.urdf.xacro#L117) |
| link3 | 1.6383 / [input L59](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ufactory_xarm7/xarm7_nohand.xml#L59) | 1.6383 / [geometry/inference input L111](https://github.com/xArm-Developer/xarm_ros/blob/fcc2060b1ccd8a72ac3f332ff9c3c590182870e7/xarm_description/urdf/xarm7/xarm7.urdf.xacro#L111) | 1.6383 / [geometry/inference input L146](https://github.com/xArm-Developer/xarm_ros/blob/cf51617d98bc55a88d9aa735acfa43a0bbb8e425/xarm_description/urdf/xarm7/xarm7.urdf.xacro#L146) |
| link4 | 1.7269 / [input L64](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ufactory_xarm7/xarm7_nohand.xml#L64) | 1.7269 / [geometry/inference input L137](https://github.com/xArm-Developer/xarm_ros/blob/fcc2060b1ccd8a72ac3f332ff9c3c590182870e7/xarm_description/urdf/xarm7/xarm7.urdf.xacro#L137) | 1.7269 / [geometry/inference input L175](https://github.com/xArm-Developer/xarm_ros/blob/cf51617d98bc55a88d9aa735acfa43a0bbb8e425/xarm_description/urdf/xarm7/xarm7.urdf.xacro#L175) |
| link5 | 1.3203 / [input L69](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ufactory_xarm7/xarm7_nohand.xml#L69) | 1.3203 / [geometry/inference input L163](https://github.com/xArm-Developer/xarm_ros/blob/fcc2060b1ccd8a72ac3f332ff9c3c590182870e7/xarm_description/urdf/xarm7/xarm7.urdf.xacro#L163) | 1.3203 / [geometry/inference input L204](https://github.com/xArm-Developer/xarm_ros/blob/cf51617d98bc55a88d9aa735acfa43a0bbb8e425/xarm_description/urdf/xarm7/xarm7.urdf.xacro#L204) |
| link6 | 1.325 / [input L74](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ufactory_xarm7/xarm7_nohand.xml#L74) | 1.325 / [geometry/inference input L189](https://github.com/xArm-Developer/xarm_ros/blob/fcc2060b1ccd8a72ac3f332ff9c3c590182870e7/xarm_description/urdf/xarm7/xarm7.urdf.xacro#L189) | 1.325 / [geometry/inference input L233](https://github.com/xArm-Developer/xarm_ros/blob/cf51617d98bc55a88d9aa735acfa43a0bbb8e425/xarm_description/urdf/xarm7/xarm7.urdf.xacro#L233) |
| link7 | 0.17 / [input L79](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ufactory_xarm7/xarm7_nohand.xml#L79) | 0.17 / [geometry/inference input L215](https://github.com/xArm-Developer/xarm_ros/blob/fcc2060b1ccd8a72ac3f332ff9c3c590182870e7/xarm_description/urdf/xarm7/xarm7.urdf.xacro#L215) | 0.17 / [geometry/inference input L262](https://github.com/xArm-Developer/xarm_ros/blob/cf51617d98bc55a88d9aa735acfa43a0bbb8e425/xarm_description/urdf/xarm7/xarm7.urdf.xacro#L262) |
| upstream-only link_eef | unavailable | unavailable | 0 / [geometry/inference input L238](https://github.com/xArm-Developer/xarm_ros/blob/cf51617d98bc55a88d9aa735acfa43a0bbb8e425/xarm_description/urdf/xarm_device_macro.xacro#L238) |

## Coverage and unmatched elements

```json
{
  "mapping_h": {
    "bodies": {
      "link_base": "link_base",
      "link1": "link1",
      "link2": "link2",
      "link3": "link3",
      "link4": "link4",
      "link5": "link5",
      "link6": "link6",
      "link7": "link7"
    },
    "joints": {
      "joint1": "joint1",
      "joint2": "joint2",
      "joint3": "joint3",
      "joint4": "joint4",
      "joint5": "joint5",
      "joint6": "joint6",
      "joint7": "joint7"
    },
    "body_methods": {
      "link_base": "name",
      "link1": "name",
      "link2": "name",
      "link3": "name",
      "link4": "name",
      "link5": "name",
      "link6": "name",
      "link7": "name"
    },
    "joint_methods": {
      "joint1": "name",
      "joint2": "name",
      "joint3": "name",
      "joint4": "name",
      "joint5": "name",
      "joint6": "name",
      "joint7": "name"
    },
    "unmatched_m_bodies": [],
    "unmatched_upstream_bodies": [
      "link_eef"
    ],
    "unmatched_m_joints": [],
    "unmatched_upstream_joints": [],
    "registration_anchor": {
      "M": "link_base",
      "H": "link_base",
      "root_unmatched": false
    }
  },
  "mapping_s": {
    "bodies": {
      "link_base": "link_base",
      "link1": "link1",
      "link2": "link2",
      "link3": "link3",
      "link4": "link4",
      "link5": "link5",
      "link6": "link6",
      "link7": "link7"
    },
    "joints": {
      "joint1": "joint1",
      "joint2": "joint2",
      "joint3": "joint3",
      "joint4": "joint4",
      "joint5": "joint5",
      "joint6": "joint6",
      "joint7": "joint7"
    },
    "body_methods": {
      "link_base": "name",
      "link1": "name",
      "link2": "name",
      "link3": "name",
      "link4": "name",
      "link5": "name",
      "link6": "name",
      "link7": "name"
    },
    "joint_methods": {
      "joint1": "name",
      "joint2": "name",
      "joint3": "name",
      "joint4": "name",
      "joint5": "name",
      "joint6": "name",
      "joint7": "name"
    },
    "unmatched_m_bodies": [],
    "unmatched_upstream_bodies": [
      "link_eef"
    ],
    "unmatched_m_joints": [],
    "unmatched_upstream_joints": [],
    "registration_anchor": {
      "M": "link_base",
      "S": "link_base"
    }
  },
  "unavailable": [
    {
      "entity": "joint1",
      "other_entity": "joint1",
      "quantity": "force",
      "tolerance": "limit",
      "m": 50.0,
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
      "other": 3.14,
      "s": 3.14,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "joint2",
      "other_entity": "joint2",
      "quantity": "force",
      "tolerance": "limit",
      "m": 50.0,
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
      "other": 3.14,
      "s": 3.14,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "joint3",
      "other_entity": "joint3",
      "quantity": "force",
      "tolerance": "limit",
      "m": 30.0,
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
      "other": 3.14,
      "s": 3.14,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "joint4",
      "other_entity": "joint4",
      "quantity": "force",
      "tolerance": "limit",
      "m": 30.0,
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
      "other": 3.14,
      "s": 3.14,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "joint5",
      "other_entity": "joint5",
      "quantity": "force",
      "tolerance": "limit",
      "m": 30.0,
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
      "other": 3.14,
      "s": 3.14,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "joint6",
      "other_entity": "joint6",
      "quantity": "force",
      "tolerance": "limit",
      "m": 20.0,
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
      "other": 3.14,
      "s": 3.14,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "joint7",
      "other_entity": "joint7",
      "quantity": "force",
      "tolerance": "limit",
      "m": 20.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "joint7",
      "other_entity": "joint7",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 3.14,
      "s": 3.14,
      "reason": "quantity absent or not enforced/declared on one side"
    }
  ]
}
```

## Limits unavailable for a like-for-like simulator comparison

URDF effort and velocity tags are manufacturer declarations; MuJoCo ignores them. Missing enforced quantities are not interpreted as zero. The available values are shown for review and excluded from STALE counts.

| Joint / quantity | M | S | H / declared upstream |
|---|---|---|---|
| joint1 / force | 50 | unavailable | unavailable |
| joint1 / velocity | unavailable | 3.14 | 3.14 |
| joint2 / force | 50 | unavailable | unavailable |
| joint2 / velocity | unavailable | 3.14 | 3.14 |
| joint3 / force | 30 | unavailable | unavailable |
| joint3 / velocity | unavailable | 3.14 | 3.14 |
| joint4 / force | 30 | unavailable | unavailable |
| joint4 / velocity | unavailable | 3.14 | 3.14 |
| joint5 / force | 30 | unavailable | unavailable |
| joint5 / velocity | unavailable | 3.14 | 3.14 |
| joint6 / force | 20 | unavailable | unavailable |
| joint6 / velocity | unavailable | 3.14 | 3.14 |
| joint7 / force | 20 | unavailable | unavailable |
| joint7 / velocity | unavailable | 3.14 | 3.14 |
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
  "https://github.com/xArm-Developer/xarm_ros xarm_description/urdf/xarm7/xarm7.urdf.xacro at cf51617d98bc55a88d9aa735acfa43a0bbb8e425: XacroException: name 'mesh_suffix' is not defined \nwhen evaluating expression 'mesh_suffix == 'dae' or (model_num >= 1305 and model_num != 1380)'",
  "https://github.com/xArm-Developer/xarm_ros xarm_description/urdf/xarm7/xarm7.gazebo.xacro at cf51617d98bc55a88d9aa735acfa43a0bbb8e425: ValueError: XML has no robot bodies; it is an include/extension fragment, not a standalone source",
  "https://github.com/xArm-Developer/xarm_ros xarm_description/urdf/xarm7/xarm7.ros2_control.xacro at cf51617d98bc55a88d9aa735acfa43a0bbb8e425: ValueError: XML has no robot bodies; it is an include/extension fragment, not a standalone source",
  "https://github.com/xArm-Developer/xarm_ros xarm_description/urdf/xarm7/xarm7.transmission.xacro at cf51617d98bc55a88d9aa735acfa43a0bbb8e425: ValueError: XML has no robot bodies; it is an include/extension fragment, not a standalone source",
  "https://github.com/xArm-Developer/xarm_ros xarm_description/urdf/xarm7/xarm7_robot_macro.xacro at cf51617d98bc55a88d9aa735acfa43a0bbb8e425: XacroException: name 'is_ros2' is not defined \nwhen evaluating expression 'is_ros2'"
]
```

## History inputs

```json
[
  "xarm_description/config/kinematics/default/xarm7_default_kinematics.yaml",
  "xarm_description/config/link_inertial/xarm7_type7_HT_BR2.yaml",
  "xarm_description/config/xarm7/joint_limits.yaml",
  "xarm_description/meshes/end_tool/collision/end_tool.STL",
  "xarm_description/meshes/end_tool/collision/end_tool.stl",
  "xarm_description/meshes/xarm7/visual/link1.STL",
  "xarm_description/meshes/xarm7/visual/link1.stl",
  "xarm_description/meshes/xarm7/visual/link2.STL",
  "xarm_description/meshes/xarm7/visual/link2.stl",
  "xarm_description/meshes/xarm7/visual/link3.STL",
  "xarm_description/meshes/xarm7/visual/link3.stl",
  "xarm_description/meshes/xarm7/visual/link4.STL",
  "xarm_description/meshes/xarm7/visual/link4.stl",
  "xarm_description/meshes/xarm7/visual/link5.STL",
  "xarm_description/meshes/xarm7/visual/link5.stl",
  "xarm_description/meshes/xarm7/visual/link6.STL",
  "xarm_description/meshes/xarm7/visual/link6.stl",
  "xarm_description/meshes/xarm7/visual/link7.STL",
  "xarm_description/meshes/xarm7/visual/link7.stl",
  "xarm_description/meshes/xarm7/visual/link_base.STL",
  "xarm_description/meshes/xarm7/visual/link_base.stl",
  "xarm_description/urdf/_private_macro.xacro",
  "xarm_description/urdf/common/common.gazebo.xacro",
  "xarm_description/urdf/common/common.link.xacro",
  "xarm_description/urdf/common/common.material.xacro",
  "xarm_description/urdf/xarm7/xarm7.gazebo.xacro",
  "xarm_description/urdf/xarm7/xarm7.transmission.xacro",
  "xarm_description/urdf/xarm7/xarm7.urdf.xacro",
  "xarm_description/urdf/xarm7/xarm7_robot_macro.xacro",
  "xarm_description/urdf/xarm_device.urdf.xacro",
  "xarm_description/urdf/xarm_device_macro.xacro"
]
```

## Construction recipe

```json
{
  "file": "xarm_description/urdf/xarm_device.urdf.xacro",
  "arguments": {
    "robot_type": "xarm",
    "dof": "7",
    "add_gripper": "false"
  },
  "evidence": "Menagerie names xArm 7; the manufacturer device wrapper declares robot_type, dof and add_gripper arguments."
}
```

## Self comparisons

```json
[
  {
    "file": "ufactory_xarm7/hand.xml",
    "status": "passed",
    "findings": 0
  },
  {
    "file": "ufactory_xarm7/xarm7.xml",
    "status": "passed",
    "findings": 0
  },
  {
    "file": "ufactory_xarm7/xarm7_nohand.xml",
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
      "STALE": 7
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
      "ufactory_xarm7/xarm7_nohand.xml"
    ],
    "registration": {
      "translation": [
        0.0,
        0.0,
        0.12
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
      "world",
      "link_eef"
    ],
    "assets_loaded": 16,
    "mesh_conversions": [],
    "nonphysical_normalizations": [],
    "xacro_arguments": {
      "robot_type": "xarm",
      "dof": "7",
      "add_gripper": "false",
      "prefix": "",
      "hw_ns": "xarm",
      "limited": "false",
      "effort_control": "false",
      "velocity_control": "false",
      "add_vacuum_gripper": "false",
      "add_bio_gripper": "false",
      "model1300": "false",
      "robot_ip": "",
      "robot_sn": "",
      "report_type": "normal",
      "ros2_control_plugin": "uf_robot_hardware/UFRobotSystemHardware",
      "ros2_control_params": "",
      "add_realsense_d435i": "false",
      "add_d435i_links": "true",
      "use_gazebo_camera": "false",
      "add_other_geometry": "false",
      "geometry_type": "box",
      "geometry_mass": "0.1",
      "geometry_height": "0.1",
      "geometry_radius": "0.1",
      "geometry_length": "0.1",
      "geometry_width": "0.1",
      "geometry_mesh_filename": "",
      "geometry_mesh_origin_xyz": "0 0 0",
      "geometry_mesh_origin_rpy": "0 0 0",
      "geometry_mesh_tcp_xyz": "0 0 0",
      "geometry_mesh_tcp_rpy": "0 0 0",
      "baud_checkset": "true",
      "default_gripper_baud": "2000000",
      "attach_to": "world",
      "attach_xyz": "0 0 0",
      "attach_rpy": "0 0 0",
      "mesh_suffix": "stl",
      "kinematics_suffix": "",
      "gripper_version": "G1"
    },
    "source_dependencies": [
      "xarm_description/config/kinematics/default/xarm7_default_kinematics.yaml",
      "xarm_description/config/link_inertial/xarm7_type7_HT_BR2.yaml",
      "xarm_description/config/xarm7/joint_limits.yaml",
      "xarm_description/urdf/_private_macro.xacro",
      "xarm_description/urdf/common/common.gazebo.xacro",
      "xarm_description/urdf/common/common.link.xacro",
      "xarm_description/urdf/common/common.material.xacro",
      "xarm_description/urdf/xarm7/xarm7.gazebo.xacro",
      "xarm_description/urdf/xarm7/xarm7.transmission.xacro",
      "xarm_description/urdf/xarm7/xarm7.urdf.xacro",
      "xarm_description/urdf/xarm7/xarm7_robot_macro.xacro",
      "xarm_description/urdf/xarm_device.urdf.xacro",
      "xarm_description/urdf/xarm_device_macro.xacro",
      "xarm_description/meshes/xarm7/visual/link_base.stl",
      "xarm_description/meshes/xarm7/visual/link_base.stl",
      "xarm_description/meshes/xarm7/visual/link1.stl",
      "xarm_description/meshes/xarm7/visual/link1.stl",
      "xarm_description/meshes/xarm7/visual/link2.stl",
      "xarm_description/meshes/xarm7/visual/link2.stl",
      "xarm_description/meshes/xarm7/visual/link3.stl",
      "xarm_description/meshes/xarm7/visual/link3.stl",
      "xarm_description/meshes/xarm7/visual/link4.stl",
      "xarm_description/meshes/xarm7/visual/link4.stl",
      "xarm_description/meshes/xarm7/visual/link5.stl",
      "xarm_description/meshes/xarm7/visual/link5.stl",
      "xarm_description/meshes/xarm7/visual/link6.stl",
      "xarm_description/meshes/xarm7/visual/link6.stl",
      "xarm_description/meshes/xarm7/visual/link7.stl",
      "xarm_description/meshes/end_tool/collision/end_tool.stl"
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
    "geometry_stripped": false,
    "missing_explicit_inertials": [
      "world",
      "link_eef"
    ],
    "assets_loaded": 16,
    "mesh_conversions": [],
    "nonphysical_normalizations": [],
    "xacro_arguments": {
      "robot_type": "xarm",
      "dof": "7",
      "add_gripper": "false",
      "prefix": "",
      "hw_ns": "xarm",
      "limited": "false",
      "effort_control": "false",
      "velocity_control": "false",
      "add_vacuum_gripper": "false",
      "model1300": "false",
      "robot_ip": "",
      "robot_sn": "",
      "report_type": "normal",
      "ros2_control_plugin": "uf_robot_hardware/UFRobotSystemHardware",
      "ros2_control_params": "",
      "add_realsense_d435i": "false",
      "add_d435i_links": "true",
      "use_gazebo_camera": "false",
      "add_other_geometry": "false",
      "geometry_type": "box",
      "geometry_mass": "0.1",
      "geometry_height": "0.1",
      "geometry_radius": "0.1",
      "geometry_length": "0.1",
      "geometry_width": "0.1",
      "geometry_mesh_filename": "",
      "geometry_mesh_origin_xyz": "0 0 0",
      "geometry_mesh_origin_rpy": "0 0 0",
      "geometry_mesh_tcp_xyz": "0 0 0",
      "geometry_mesh_tcp_rpy": "0 0 0",
      "baud_checkset": "true",
      "default_gripper_baud": "2000000",
      "attach_to": "world",
      "attach_xyz": "0 0 0",
      "attach_rpy": "0 0 0"
    },
    "source_dependencies": [
      "xarm_description/config/link_inertial/xarm7_type7_HT_BR2.yaml",
      "xarm_description/urdf/_private_macro.xacro",
      "xarm_description/urdf/common/common.gazebo.xacro",
      "xarm_description/urdf/common/common.link.xacro",
      "xarm_description/urdf/common/common.material.xacro",
      "xarm_description/urdf/xarm7/xarm7.gazebo.xacro",
      "xarm_description/urdf/xarm7/xarm7.transmission.xacro",
      "xarm_description/urdf/xarm7/xarm7.urdf.xacro",
      "xarm_description/urdf/xarm7/xarm7_robot_macro.xacro",
      "xarm_description/urdf/xarm_device.urdf.xacro",
      "xarm_description/urdf/xarm_device_macro.xacro",
      "xarm_description/meshes/xarm7/visual/link_base.STL",
      "xarm_description/meshes/xarm7/visual/link_base.STL",
      "xarm_description/meshes/xarm7/visual/link1.STL",
      "xarm_description/meshes/xarm7/visual/link1.STL",
      "xarm_description/meshes/xarm7/visual/link2.STL",
      "xarm_description/meshes/xarm7/visual/link2.STL",
      "xarm_description/meshes/xarm7/visual/link3.STL",
      "xarm_description/meshes/xarm7/visual/link3.STL",
      "xarm_description/meshes/xarm7/visual/link4.STL",
      "xarm_description/meshes/xarm7/visual/link4.STL",
      "xarm_description/meshes/xarm7/visual/link5.STL",
      "xarm_description/meshes/xarm7/visual/link5.STL",
      "xarm_description/meshes/xarm7/visual/link6.STL",
      "xarm_description/meshes/xarm7/visual/link6.STL",
      "xarm_description/meshes/xarm7/visual/link7.STL",
      "xarm_description/meshes/end_tool/collision/end_tool.STL"
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
  "self_variants_recompiled": 3,
  "historical_snapshots_reused": 11,
  "primary_physics_unchanged": true,
  "source_matching": "original raw-value provenance criteria retained; kinematic guard applies to reported CoM"
}
```
