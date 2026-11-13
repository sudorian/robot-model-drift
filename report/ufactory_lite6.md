# ufactory_lite6

Status: **partial history**. Provenance: **dated match**, confidence **medium**.

Source selected using the ordered amended provenance rules.

M: `https://github.com/google-deepmind/mujoco_menagerie`, `ufactory_lite6/lite6.xml`, commit `370c43965323c0944b433b202aac5058b5f907a9`.
H: `https://github.com/xArm-Developer/xarm_ros2`, `xarm_description/urdf/xarm_device.urdf.xacro`, commit `ac736c92b02de7ca7e0be6f737d77d46707464d8`.
S: `65a1e29398045818d1475868c22f64053176d9f4` (2023-08-28T16:31:10+08:00). Menagerie release/change: 2023-11-03T10:16:12-07:00.

Limit semantics: MJCF effort values are supported actuator torque/force envelopes. URDF effort and velocity values are manufacturer declarations retained from XML; MuJoCo does not enforce those tags. Such declaration comparisons are explicitly distinct from compiled inertial/range quantities.


## Source evidence

```json
[
  {
    "url": "https://github.com/xArm-Developer/xarm_ros2/tree/master/xarm_description/urdf/lite6",
    "document": "ufactory_lite6/README.md",
    "commit": "370c43965323c0944b433b202aac5058b5f907a9",
    "current": true
  }
]
```


## README derivation evidence

Documentation labels are conservative: an automated documented label requires an explicit affected entity and quantity. Broader conversion notes are retained here for review.

> description](https://github.com/xArm-Developer/xarm_ros2/tree/master/xarm_description/urdf/lite6). 3 versions are provided: no gripper, wide gripper, and narrow gripper. The gripper fingers can be attached in two orientations, narrrow (so that they close fully) or wide (so that wider objects can be gripped). This provides some flexibility with the limited range of the gripper.
> 1. Added `<mujoco> <compiler discardvisual="false" strippath="false" fusestatic="false"/> </mujoco>` to the URDF's
> The URDF only contains a gripper model for the Lite 6 with the fingers fused to the gripper body. To separate the fingers, the .step file of the fused body from the [Ufactory website](https://www.ufactory.cc/download/) was loaded into Onshape ([file here](https://cad.onshape.com/documents/f60aac1c8ff6af8f490dc855/w/5c0df4bc7414802fc89a514e/e/7dc41825dd66894c14b085ca?renderMode=0&uiState=66bdfb41f48d6a182064f4a4)) and split along the tracks that the fingers run on.  Because MuJoCo forms a convex hull for collision meshes, it was necessary to separate the wide fingers into the base and tip for realistic gripping.
> The moments of inertia were estimated in Onshape due to not having any data from the manufacturer. This was done by choosing a density that matched the mass of the actual part, and assuming a uniform mass distribution (which is not the actual case but should be close enough).

## Kinematics consistency

A proper Kabsch rigid transform aligns all matched zero-pose body origins. The maximum per-origin residual and signed hinge/slide axis angles determine whether CoM can be compared; RMS is also recorded. Fewer than three non-collinear origins give insufficient kinematic coverage. CoM records that fail either required M/H or M/S check are excluded from counts and largest discrepancies. Masses, principal moments and raw joint ranges remain unchanged; a flagged range still requires convention review.

| Pair | Status | Origins / rank | RMS / maximum mm | Disagreeing / checked axes |
|---|---|---:|---:|---:|
| M/H | consistent | 7 / 2 | 0.000191824405 / 0.000317558264 | 0 / 6 |
| M/S | consistent | 7 / 2 | 0.000191824405 / 0.000317558264 | 0 / 6 |

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
    "anchor_m": "link_base",
    "anchor_other": "link_base",
    "rotation_other_to_m": [
      [
        0.9999999999294868,
        1.1728573413117905e-05,
        -1.861881003662355e-06
      ],
      [
        -1.1728573264950411e-05,
        0.9999999999312171,
        7.963899108539542e-08
      ],
      [
        1.8618819376725687e-06,
        -7.961715399362115e-08,
        0.9999999999982634
      ]
    ],
    "translation_other_to_m": [
      3.13617216550488e-07,
      -1.8530604071477684e-08,
      4.630452832277143e-08
    ],
    "rms_residual_m": 1.9182440467753212e-07,
    "max_residual_m": 3.175582641773379e-07,
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
          -1.8618810036623553e-06,
          7.963899108539544e-08,
          0.9999999999982636
        ],
        "angle_rad": 1.863583440767775e-06,
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
          0.0
        ],
        "axis_other_aligned": [
          7.089581033229622e-07,
          0.9999999999997455,
          -7.962417867107436e-08
        ],
        "angle_rad": 7.134154484565226e-07,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "joint3",
        "joint_other": "joint3",
        "axis_m": [
          2.97262026045438e-11,
          -0.9999999999730153,
          7.346403971486561e-06
        ],
        "axis_other_aligned": [
          -7.089178116658638e-07,
          -0.9999999999721757,
          7.426034385588786e-06
        ],
        "angle_rad": 7.134056449878862e-07,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "joint4",
        "joint_other": "joint4",
        "axis_m": [
          -4.242642374320035e-06,
          -3.103761597437719e-06,
          -0.9999999999861833
        ],
        "axis_other_aligned": [
          -5.484531807128554e-06,
          -3.7528253938801913e-06,
          -0.9999999999779181
        ],
        "angle_rad": 1.401275552931119e-06,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "joint5",
        "joint_other": "joint5",
        "axis_m": [
          -1.172618828938776e-11,
          0.9999999999951834,
          -3.1037615972895347e-06
        ],
        "axis_other_aligned": [
          7.089581032863115e-07,
          0.9999999999997455,
          -7.962417889311901e-08
        ],
        "angle_rad": 3.106130284530762e-06,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "joint6",
        "joint_other": "joint6",
        "axis_m": [
          -4.2426423743200374e-06,
          -3.103761597563999e-06,
          -0.9999999999861834
        ],
        "axis_other_aligned": [
          -5.4845318071285555e-06,
          -3.752825394043241e-06,
          -0.9999999999779181
        ],
        "angle_rad": 1.4012755529481503e-06,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      }
    ],
    "axis_disagreements": [],
    "com_eligible": true,
    "covariance_singular_values": [
      0.10424922664629427,
      0.012633879332917982,
      8.137408844875788e-19
    ],
    "origin_residuals_m": {
      "link_base": 3.175582641773379e-07,
      "link1": 1.4722466043709818e-07,
      "link2": 1.4722466043709818e-07,
      "link3": 2.282546418183092e-07,
      "link4": 1.0656370587711601e-07,
      "link5": 1.0656370587711601e-07,
      "link6": 1.9639484425038264e-07
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
    "anchor_m": "link_base",
    "anchor_other": "link_base",
    "rotation_other_to_m": [
      [
        0.9999999999294868,
        1.1728573413117905e-05,
        -1.861881003662355e-06
      ],
      [
        -1.1728573264950411e-05,
        0.9999999999312171,
        7.963899108539542e-08
      ],
      [
        1.8618819376725687e-06,
        -7.961715399362115e-08,
        0.9999999999982634
      ]
    ],
    "translation_other_to_m": [
      3.13617216550488e-07,
      -1.8530604071477684e-08,
      4.630452832277143e-08
    ],
    "rms_residual_m": 1.9182440467753212e-07,
    "max_residual_m": 3.175582641773379e-07,
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
          -1.8618810036623553e-06,
          7.963899108539544e-08,
          0.9999999999982636
        ],
        "angle_rad": 1.863583440767775e-06,
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
          0.0
        ],
        "axis_other_aligned": [
          7.089581033229622e-07,
          0.9999999999997455,
          -7.962417867107436e-08
        ],
        "angle_rad": 7.134154484565226e-07,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "joint3",
        "joint_other": "joint3",
        "axis_m": [
          2.97262026045438e-11,
          -0.9999999999730153,
          7.346403971486561e-06
        ],
        "axis_other_aligned": [
          -7.089178116658638e-07,
          -0.9999999999721757,
          7.426034385588786e-06
        ],
        "angle_rad": 7.134056449878862e-07,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "joint4",
        "joint_other": "joint4",
        "axis_m": [
          -4.242642374320035e-06,
          -3.103761597437719e-06,
          -0.9999999999861833
        ],
        "axis_other_aligned": [
          -5.484531807128554e-06,
          -3.7528253938801913e-06,
          -0.9999999999779181
        ],
        "angle_rad": 1.401275552931119e-06,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "joint5",
        "joint_other": "joint5",
        "axis_m": [
          -1.172618828938776e-11,
          0.9999999999951834,
          -3.1037615972895347e-06
        ],
        "axis_other_aligned": [
          7.089581032863115e-07,
          0.9999999999997455,
          -7.962417889311901e-08
        ],
        "angle_rad": 3.106130284530762e-06,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "joint6",
        "joint_other": "joint6",
        "axis_m": [
          -4.2426423743200374e-06,
          -3.103761597563999e-06,
          -0.9999999999861834
        ],
        "axis_other_aligned": [
          -5.4845318071285555e-06,
          -3.752825394043241e-06,
          -0.9999999999779181
        ],
        "angle_rad": 1.4012755529481503e-06,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      }
    ],
    "axis_disagreements": [],
    "com_eligible": true,
    "covariance_singular_values": [
      0.10424922664629427,
      0.012633879332917982,
      8.137408844875788e-19
    ],
    "origin_residuals_m": {
      "link_base": 3.175582641773379e-07,
      "link1": 1.4722466043709818e-07,
      "link2": 1.4722466043709818e-07,
      "link3": 2.282546418183092e-07,
      "link4": 1.0656370587711601e-07,
      "link5": 1.0656370587711601e-07,
      "link6": 1.9639484425038264e-07
    },
    "reason": "Unique proper rigid fit and matched signed axes meet the configured thresholds"
  }
}
```


## Every reported quantity difference

Counts are quantity records, including correlated total/subtree/body mass records; they are not independent robot defects.

| Entity / quantity | M | S | H | H − M | Class | M source | S source | H source |
|---|---|---|---|---|---|---|---|---|
| joint1 / effort | 50 | 50 | 81.6 | 31.6 | STALE | [inherited actuator input L12](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ufactory_lite6/lite6.xml#L12) | [geometry/inference input L30](https://github.com/xArm-Developer/xarm_ros2/blob/65a1e29398045818d1475868c22f64053176d9f4/xarm_description/urdf/lite6/lite6.ros2_control.xacro#L30) | [geometry/inference input L30](https://github.com/xArm-Developer/xarm_ros2/blob/ac736c92b02de7ca7e0be6f737d77d46707464d8/xarm_description/urdf/lite6/lite6.ros2_control.xacro#L30) |
| joint2 / effort | 50 | 50 | 81.6 | 31.6 | STALE | [inherited actuator input L12](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ufactory_lite6/lite6.xml#L12) | [geometry/inference input L43](https://github.com/xArm-Developer/xarm_ros2/blob/65a1e29398045818d1475868c22f64053176d9f4/xarm_description/urdf/lite6/lite6.ros2_control.xacro#L43) | [geometry/inference input L43](https://github.com/xArm-Developer/xarm_ros2/blob/ac736c92b02de7ca7e0be6f737d77d46707464d8/xarm_description/urdf/lite6/lite6.ros2_control.xacro#L43) |
| joint3 / effort | 32 | 32 | 30.6 | -1.4 | STALE | [inherited actuator input L15](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ufactory_lite6/lite6.xml#L15) | [geometry/inference input L56](https://github.com/xArm-Developer/xarm_ros2/blob/65a1e29398045818d1475868c22f64053176d9f4/xarm_description/urdf/lite6/lite6.ros2_control.xacro#L56) | [geometry/inference input L56](https://github.com/xArm-Developer/xarm_ros2/blob/ac736c92b02de7ca7e0be6f737d77d46707464d8/xarm_description/urdf/lite6/lite6.ros2_control.xacro#L56) |
| joint4 / effort | 32 | 32 | 1.364505 | -30.635495 | STALE | [inherited actuator input L15](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ufactory_lite6/lite6.xml#L15) | [geometry/inference input L69](https://github.com/xArm-Developer/xarm_ros2/blob/65a1e29398045818d1475868c22f64053176d9f4/xarm_description/urdf/lite6/lite6.ros2_control.xacro#L69) | [geometry/inference input L69](https://github.com/xArm-Developer/xarm_ros2/blob/ac736c92b02de7ca7e0be6f737d77d46707464d8/xarm_description/urdf/lite6/lite6.ros2_control.xacro#L69) |
| joint5 / effort | 32 | 32 | 3.274812 | -28.725188 | STALE | [inherited actuator input L15](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ufactory_lite6/lite6.xml#L15) | [geometry/inference input L82](https://github.com/xArm-Developer/xarm_ros2/blob/65a1e29398045818d1475868c22f64053176d9f4/xarm_description/urdf/lite6/lite6.ros2_control.xacro#L82) | [geometry/inference input L82](https://github.com/xArm-Developer/xarm_ros2/blob/ac736c92b02de7ca7e0be6f737d77d46707464d8/xarm_description/urdf/lite6/lite6.ros2_control.xacro#L82) |
| joint6 / effort | 20 | 20 | 1.364505 | -18.635495 | STALE | [inherited actuator input L18](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ufactory_lite6/lite6.xml#L18) | [geometry/inference input L95](https://github.com/xArm-Developer/xarm_ros2/blob/65a1e29398045818d1475868c22f64053176d9f4/xarm_description/urdf/lite6/lite6.ros2_control.xacro#L95) | [geometry/inference input L95](https://github.com/xArm-Developer/xarm_ros2/blob/ac736c92b02de7ca7e0be6f737d77d46707464d8/xarm_description/urdf/lite6/lite6.ros2_control.xacro#L95) |

## Raw CoM records and reporting decisions

Raw values retain the previous root-anchor registration before Kabsch; original world coordinates also remain in the snapshots. Eligible findings above use the fitted transform into M. Excluded raw records below are diagnostic numbers, not findings. No CoM suppression applies to mass or principal inertia moments.

| Entity / quantity | Raw M | Raw S | Raw H | Raw H − M | Decision | M source | S source | H source |
|---|---|---|---|---|---|---|---|---|
| robot / total_com_registered | [0.0323107043, 0.0233402781, 0.259803729] | [0.0323108009, 0.0233406848, 0.259803741] | [0.0323108009, 0.0233406848, 0.259803741] | [9.66144237e-08, 4.06653829e-07, 1.20271801e-08] | eligible; compared after Kabsch alignment | [aggregate inputs](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ufactory_lite6/lite6.xml#L1) | [aggregate inputs](https://github.com/xArm-Developer/xarm_ros2/blob/65a1e29398045818d1475868c22f64053176d9f4/xarm_description/urdf/xarm_device.urdf.xacro#L1) | [aggregate inputs](https://github.com/xArm-Developer/xarm_ros2/blob/ac736c92b02de7ca7e0be6f737d77d46707464d8/xarm_description/urdf/xarm_device.urdf.xacro#L1) |
| link_base / com_registered | [-0.00829545, 3.26357e-05, 0.0631195] | [-0.00829544579, 3.26357432e-05, 0.0631194585] | [-0.00829544579, 3.26357432e-05, 0.0631194585] | [4.20946808e-09, 4.32323433e-11, -4.15012911e-08] | eligible; compared after Kabsch alignment | [CoM/kinematic input L52](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ufactory_lite6/lite6.xml#L52) | [CoM/kinematic input L30](https://github.com/xArm-Developer/xarm_ros2/blob/65a1e29398045818d1475868c22f64053176d9f4/xarm_description/urdf/lite6/lite6.urdf.xacro#L30) | [CoM/kinematic input L42](https://github.com/xArm-Developer/xarm_ros2/blob/ac736c92b02de7ca7e0be6f737d77d46707464d8/xarm_description/urdf/lite6/lite6.urdf.xacro#L42) |
| link1 / com_registered | [-0.00036, 0.04195, 0.241] | [-0.00036, 0.04195, 0.241] | [-0.00036, 0.04195, 0.241] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L57](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ufactory_lite6/lite6.xml#L57) | [geometry/inference input L46](https://github.com/xArm-Developer/xarm_ros2/blob/65a1e29398045818d1475868c22f64053176d9f4/xarm_description/urdf/lite6/lite6.urdf.xacro#L46) | [geometry/inference input L60](https://github.com/xArm-Developer/xarm_ros2/blob/ac736c92b02de7ca7e0be6f737d77d46707464d8/xarm_description/urdf/lite6/lite6.urdf.xacro#L60) |
| link2 / com_registered | [0, 0.0584, 0.4225] | [1.39581794e-08, 0.0584, 0.4225] | [1.39581794e-08, 0.0584, 0.4225] | [1.39581794e-08, 1.28447947e-12, -4.19664303e-13] | eligible; compared after Kabsch alignment | [CoM/kinematic input L63](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ufactory_lite6/lite6.xml#L63) | [geometry/inference input L72](https://github.com/xArm-Developer/xarm_ros2/blob/65a1e29398045818d1475868c22f64053176d9f4/xarm_description/urdf/lite6/lite6.urdf.xacro#L72) | [geometry/inference input L89](https://github.com/xArm-Developer/xarm_ros2/blob/ac736c92b02de7ca7e0be6f737d77d46707464d8/xarm_description/urdf/lite6/lite6.urdf.xacro#L89) |
| link3 / com_registered | [0.0719998485, 0.000999737733, 0.407999687] | [0.0720004621, 0.00100053115, 0.407999464] | [0.0720004621, 0.00100053115, 0.407999464] | [6.13548734e-07, 7.93415117e-07, -2.23471985e-07] | eligible; compared after Kabsch alignment | [CoM/kinematic input L69](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ufactory_lite6/lite6.xml#L69) | [geometry/inference input L98](https://github.com/xArm-Developer/xarm_ros2/blob/65a1e29398045818d1475868c22f64053176d9f4/xarm_description/urdf/lite6/lite6.urdf.xacro#L98) | [geometry/inference input L118](https://github.com/xArm-Developer/xarm_ros2/blob/ac736c92b02de7ca7e0be6f737d77d46707464d8/xarm_description/urdf/lite6/lite6.urdf.xacro#L118) |
| link4 / com_registered | [0.0849993793, 0.0284985802, 0.297389551] | [0.0849993465, 0.0284995632, 0.297389271] | [0.0849993465, 0.0284995632, 0.297389271] | [-3.27876353e-08, 9.82955508e-07, -2.80047897e-07] | eligible; compared after Kabsch alignment | [CoM/kinematic input L75](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ufactory_lite6/lite6.xml#L75) | [geometry/inference input L124](https://github.com/xArm-Developer/xarm_ros2/blob/65a1e29398045818d1475868c22f64053176d9f4/xarm_description/urdf/lite6/lite6.urdf.xacro#L124) | [geometry/inference input L147](https://github.com/xArm-Developer/xarm_ros2/blob/ac736c92b02de7ca7e0be6f737d77d46707464d8/xarm_description/urdf/lite6/lite6.urdf.xacro#L147) |
| link5 / com_registered | [0.0869989919, 0.00189829685, 0.206089625] | [0.0869989689, 0.00189928658, 0.206089361] | [0.0869989689, 0.00189928658, 0.206089361] | [-2.30362806e-08, 9.89732121e-07, -2.64127754e-07] | eligible; compared after Kabsch alignment | [CoM/kinematic input L81](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ufactory_lite6/lite6.xml#L81) | [geometry/inference input L150](https://github.com/xArm-Developer/xarm_ros2/blob/65a1e29398045818d1475868c22f64053176d9f4/xarm_description/urdf/lite6/lite6.urdf.xacro#L150) | [geometry/inference input L176](https://github.com/xArm-Developer/xarm_ros2/blob/ac736c92b02de7ca7e0be6f737d77d46707464d8/xarm_description/urdf/lite6/lite6.urdf.xacro#L176) |
| link6 / com_registered | [0.0869988124, 0.00193816556, 0.163789625] | [0.0869986577, 0.00193932404, 0.163789354] | [0.0869986577, 0.00193932404, 0.163789354] | [-1.54766909e-07, 1.15848506e-06, -2.71129133e-07] | eligible; compared after Kabsch alignment | [CoM/kinematic input L87](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ufactory_lite6/lite6.xml#L87) | [geometry/inference input L176](https://github.com/xArm-Developer/xarm_ros2/blob/65a1e29398045818d1475868c22f64053176d9f4/xarm_description/urdf/lite6/lite6.urdf.xacro#L176) | [geometry/inference input L205](https://github.com/xArm-Developer/xarm_ros2/blob/ac736c92b02de7ca7e0be6f737d77d46707464d8/xarm_description/urdf/lite6/lite6.urdf.xacro#L205) |

## Mass accounting

Every contributing compiled body mass is listed here so total/subtree sums can be checked. Links point to explicit inertials or to geometry inputs when the compiler inferred a mass. CoM links identify inertial inputs; world coordinates additionally use the ancestor transforms and the registration recorded below.

| M body | M kg / source | S kg / source | H kg / source |
|---|---|---|---|
| link_base | 1.65394 / [input L52](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ufactory_lite6/lite6.xml#L52) | 1.65393502 / [input L31](https://github.com/xArm-Developer/xarm_ros2/blob/65a1e29398045818d1475868c22f64053176d9f4/xarm_description/urdf/lite6/lite6.urdf.xacro#L31) | 1.65393502 / [input L43](https://github.com/xArm-Developer/xarm_ros2/blob/ac736c92b02de7ca7e0be6f737d77d46707464d8/xarm_description/urdf/lite6/lite6.urdf.xacro#L43) |
| link1 | 1.411 / [input L57](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ufactory_lite6/lite6.xml#L57) | 1.411 / [geometry/inference input L46](https://github.com/xArm-Developer/xarm_ros2/blob/65a1e29398045818d1475868c22f64053176d9f4/xarm_description/urdf/lite6/lite6.urdf.xacro#L46) | 1.411 / [geometry/inference input L60](https://github.com/xArm-Developer/xarm_ros2/blob/ac736c92b02de7ca7e0be6f737d77d46707464d8/xarm_description/urdf/lite6/lite6.urdf.xacro#L60) |
| link2 | 1.34 / [input L63](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ufactory_lite6/lite6.xml#L63) | 1.34 / [geometry/inference input L72](https://github.com/xArm-Developer/xarm_ros2/blob/65a1e29398045818d1475868c22f64053176d9f4/xarm_description/urdf/lite6/lite6.urdf.xacro#L72) | 1.34 / [geometry/inference input L89](https://github.com/xArm-Developer/xarm_ros2/blob/ac736c92b02de7ca7e0be6f737d77d46707464d8/xarm_description/urdf/lite6/lite6.urdf.xacro#L89) |
| link3 | 0.953 / [input L69](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ufactory_lite6/lite6.xml#L69) | 0.953 / [geometry/inference input L98](https://github.com/xArm-Developer/xarm_ros2/blob/65a1e29398045818d1475868c22f64053176d9f4/xarm_description/urdf/lite6/lite6.urdf.xacro#L98) | 0.953 / [geometry/inference input L118](https://github.com/xArm-Developer/xarm_ros2/blob/ac736c92b02de7ca7e0be6f737d77d46707464d8/xarm_description/urdf/lite6/lite6.urdf.xacro#L118) |
| link4 | 1.284 / [input L75](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ufactory_lite6/lite6.xml#L75) | 1.284 / [geometry/inference input L124](https://github.com/xArm-Developer/xarm_ros2/blob/65a1e29398045818d1475868c22f64053176d9f4/xarm_description/urdf/lite6/lite6.urdf.xacro#L124) | 1.284 / [geometry/inference input L147](https://github.com/xArm-Developer/xarm_ros2/blob/ac736c92b02de7ca7e0be6f737d77d46707464d8/xarm_description/urdf/lite6/lite6.urdf.xacro#L147) |
| link5 | 0.804 / [input L81](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ufactory_lite6/lite6.xml#L81) | 0.804 / [geometry/inference input L150](https://github.com/xArm-Developer/xarm_ros2/blob/65a1e29398045818d1475868c22f64053176d9f4/xarm_description/urdf/lite6/lite6.urdf.xacro#L150) | 0.804 / [geometry/inference input L176](https://github.com/xArm-Developer/xarm_ros2/blob/ac736c92b02de7ca7e0be6f737d77d46707464d8/xarm_description/urdf/lite6/lite6.urdf.xacro#L176) |
| link6 | 0.13 / [input L87](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ufactory_lite6/lite6.xml#L87) | 0.13 / [geometry/inference input L176](https://github.com/xArm-Developer/xarm_ros2/blob/65a1e29398045818d1475868c22f64053176d9f4/xarm_description/urdf/lite6/lite6.urdf.xacro#L176) | 0.13 / [geometry/inference input L205](https://github.com/xArm-Developer/xarm_ros2/blob/ac736c92b02de7ca7e0be6f737d77d46707464d8/xarm_description/urdf/lite6/lite6.urdf.xacro#L205) |
| upstream-only link_eef | unavailable | unavailable | 0 / [geometry/inference input L238](https://github.com/xArm-Developer/xarm_ros2/blob/ac736c92b02de7ca7e0be6f737d77d46707464d8/xarm_description/urdf/xarm_device_macro.xacro#L238) |

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
      "link6": "link6"
    },
    "joints": {
      "joint1": "joint1",
      "joint2": "joint2",
      "joint3": "joint3",
      "joint4": "joint4",
      "joint5": "joint5",
      "joint6": "joint6"
    },
    "body_methods": {
      "link_base": "name",
      "link1": "name",
      "link2": "name",
      "link3": "name",
      "link4": "name",
      "link5": "name",
      "link6": "name"
    },
    "joint_methods": {
      "joint1": "name",
      "joint2": "name",
      "joint3": "name",
      "joint4": "name",
      "joint5": "name",
      "joint6": "name"
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
      "link6": "link6"
    },
    "joints": {
      "joint1": "joint1",
      "joint2": "joint2",
      "joint3": "joint3",
      "joint4": "joint4",
      "joint5": "joint5",
      "joint6": "joint6"
    },
    "body_methods": {
      "link_base": "name",
      "link1": "name",
      "link2": "name",
      "link3": "name",
      "link4": "name",
      "link5": "name",
      "link6": "name"
    },
    "joint_methods": {
      "joint1": "name",
      "joint2": "name",
      "joint3": "name",
      "joint4": "name",
      "joint5": "name",
      "joint6": "name"
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
      "m": 32.0,
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
      "m": 32.0,
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
      "m": 32.0,
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
| joint3 / force | 32 | unavailable | unavailable |
| joint3 / velocity | unavailable | 3.14 | 3.14 |
| joint4 / force | 32 | unavailable | unavailable |
| joint4 / velocity | unavailable | 3.14 | 3.14 |
| joint5 / force | 32 | unavailable | unavailable |
| joint5 / velocity | unavailable | 3.14 | 3.14 |
| joint6 / force | 20 | unavailable | unavailable |
| joint6 / velocity | unavailable | 3.14 | 3.14 |
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
  "https://github.com/xArm-Developer/xarm_ros2 xarm_description/urdf/lite6/lite6.urdf.xacro at ac736c92b02de7ca7e0be6f737d77d46707464d8: XacroException: name 'use_xacro_load_yaml' is not defined \nwhen evaluating expression 'use_xacro_load_yaml'",
  "https://github.com/xArm-Developer/xarm_ros2 xarm_description/urdf/lite6/lite6.gazebo.xacro at ac736c92b02de7ca7e0be6f737d77d46707464d8: ValueError: XML has no robot bodies; it is an include/extension fragment, not a standalone source",
  "https://github.com/xArm-Developer/xarm_ros2 xarm_description/urdf/lite6/lite6.ros2_control.xacro at ac736c92b02de7ca7e0be6f737d77d46707464d8: ValueError: XML has no robot bodies; it is an include/extension fragment, not a standalone source",
  "https://github.com/xArm-Developer/xarm_ros2 xarm_description/urdf/lite6/lite6.transmission.xacro at ac736c92b02de7ca7e0be6f737d77d46707464d8: ValueError: XML has no robot bodies; it is an include/extension fragment, not a standalone source",
  "https://github.com/xArm-Developer/xarm_ros2 xarm_description/urdf/lite6/lite6_robot_macro.xacro at ac736c92b02de7ca7e0be6f737d77d46707464d8: XacroException: name 'is_ros2' is not defined \nwhen evaluating expression 'is_ros2'"
]
```

## History inputs

```json
[
  "xarm_description/config/kinematics/default/lite6_default_kinematics.yaml",
  "xarm_description/config/link_inertial/xarm6_type9_HT_BR2.yaml",
  "xarm_description/config/lite6/joint_limits.yaml",
  "xarm_description/meshes/lite6/collision/link1.stl",
  "xarm_description/meshes/lite6/collision/link2.stl",
  "xarm_description/meshes/lite6/collision/link3.stl",
  "xarm_description/meshes/lite6/collision/link4.stl",
  "xarm_description/meshes/lite6/collision/link5.stl",
  "xarm_description/meshes/lite6/collision/link6.stl",
  "xarm_description/meshes/lite6/collision/link_base.stl",
  "xarm_description/meshes/lite6/visual/base.stl",
  "xarm_description/meshes/lite6/visual/link1.stl",
  "xarm_description/meshes/lite6/visual/link2.stl",
  "xarm_description/meshes/lite6/visual/link3.stl",
  "xarm_description/meshes/lite6/visual/link4.stl",
  "xarm_description/meshes/lite6/visual/link5.stl",
  "xarm_description/meshes/lite6/visual/link6.stl",
  "xarm_description/meshes/lite6/visual/link_base.stl",
  "xarm_description/urdf/_private_macro.xacro",
  "xarm_description/urdf/common/common.gazebo.xacro",
  "xarm_description/urdf/common/common.link.xacro",
  "xarm_description/urdf/common/common.material.xacro",
  "xarm_description/urdf/lite6/lite6.gazebo.xacro",
  "xarm_description/urdf/lite6/lite6.ros2_control.xacro",
  "xarm_description/urdf/lite6/lite6.transmission.xacro",
  "xarm_description/urdf/lite6/lite6.urdf.xacro",
  "xarm_description/urdf/lite6/lite6_robot_macro.xacro",
  "xarm_description/urdf/xarm_device.urdf.xacro",
  "xarm_description/urdf/xarm_device_macro.xacro"
]
```

## Construction recipe

```json
{
  "file": "xarm_description/urdf/xarm_device.urdf.xacro",
  "arguments": {
    "robot_type": "lite",
    "dof": "6",
    "add_gripper": "false"
  },
  "evidence": "Menagerie describes the six-axis Lite 6 and provides a no-gripper variant; the manufacturer device wrapper declares robot_type, dof and add_gripper arguments."
}
```

## Self comparisons

```json
[
  {
    "file": "ufactory_lite6/lite6.xml",
    "status": "passed",
    "findings": 0
  },
  {
    "file": "ufactory_lite6/lite6_gripper_narrow.xml",
    "status": "passed",
    "findings": 0
  },
  {
    "file": "ufactory_lite6/lite6_gripper_wide.xml",
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
      "STALE": 6
    },
    "classifications_changed": 0,
    "finding_membership_changes": 0
  },
  "2": {
    "provenance_method": "dated match",
    "counts": {
      "STALE": 6
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
      "ufactory_lite6/lite6.xml"
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
    "geometry_stripped": false,
    "missing_explicit_inertials": [
      "world",
      "link_eef"
    ],
    "assets_loaded": 14,
    "mesh_conversions": [],
    "nonphysical_normalizations": [],
    "xacro_arguments": {
      "robot_type": "lite",
      "dof": "6",
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
      "xarm_description/config/kinematics/default/lite6_default_kinematics.yaml",
      "xarm_description/config/link_inertial/xarm6_type9_HT_BR2.yaml",
      "xarm_description/config/lite6/joint_limits.yaml",
      "xarm_description/urdf/_private_macro.xacro",
      "xarm_description/urdf/common/common.gazebo.xacro",
      "xarm_description/urdf/common/common.link.xacro",
      "xarm_description/urdf/common/common.material.xacro",
      "xarm_description/urdf/lite6/lite6.gazebo.xacro",
      "xarm_description/urdf/lite6/lite6.ros2_control.xacro",
      "xarm_description/urdf/lite6/lite6.transmission.xacro",
      "xarm_description/urdf/lite6/lite6.urdf.xacro",
      "xarm_description/urdf/lite6/lite6_robot_macro.xacro",
      "xarm_description/urdf/xarm_device.urdf.xacro",
      "xarm_description/urdf/xarm_device_macro.xacro",
      "xarm_description/meshes/lite6/visual/link_base.stl",
      "xarm_description/meshes/lite6/collision/link_base.stl",
      "xarm_description/meshes/lite6/visual/link1.stl",
      "xarm_description/meshes/lite6/collision/link1.stl",
      "xarm_description/meshes/lite6/visual/link2.stl",
      "xarm_description/meshes/lite6/collision/link2.stl",
      "xarm_description/meshes/lite6/visual/link3.stl",
      "xarm_description/meshes/lite6/collision/link3.stl",
      "xarm_description/meshes/lite6/visual/link4.stl",
      "xarm_description/meshes/lite6/collision/link4.stl",
      "xarm_description/meshes/lite6/visual/link5.stl",
      "xarm_description/meshes/lite6/collision/link5.stl",
      "xarm_description/meshes/lite6/visual/link6.stl",
      "xarm_description/meshes/lite6/collision/link6.stl"
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
    "assets_loaded": 14,
    "mesh_conversions": [],
    "nonphysical_normalizations": [],
    "xacro_arguments": {
      "robot_type": "lite",
      "dof": "6",
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
      "attach_rpy": "0 0 0",
      "mesh_suffix": "stl"
    },
    "source_dependencies": [
      "xarm_description/config/link_inertial/xarm6_type9_HT_BR2.yaml",
      "xarm_description/urdf/_private_macro.xacro",
      "xarm_description/urdf/common/common.gazebo.xacro",
      "xarm_description/urdf/common/common.link.xacro",
      "xarm_description/urdf/common/common.material.xacro",
      "xarm_description/urdf/lite6/lite6.gazebo.xacro",
      "xarm_description/urdf/lite6/lite6.ros2_control.xacro",
      "xarm_description/urdf/lite6/lite6.transmission.xacro",
      "xarm_description/urdf/lite6/lite6.urdf.xacro",
      "xarm_description/urdf/lite6/lite6_robot_macro.xacro",
      "xarm_description/urdf/xarm_device.urdf.xacro",
      "xarm_description/urdf/xarm_device_macro.xacro",
      "xarm_description/meshes/lite6/visual/link_base.stl",
      "xarm_description/meshes/lite6/collision/link_base.stl",
      "xarm_description/meshes/lite6/visual/link1.stl",
      "xarm_description/meshes/lite6/collision/link1.stl",
      "xarm_description/meshes/lite6/visual/link2.stl",
      "xarm_description/meshes/lite6/collision/link2.stl",
      "xarm_description/meshes/lite6/visual/link3.stl",
      "xarm_description/meshes/lite6/collision/link3.stl",
      "xarm_description/meshes/lite6/visual/link4.stl",
      "xarm_description/meshes/lite6/collision/link4.stl",
      "xarm_description/meshes/lite6/visual/link5.stl",
      "xarm_description/meshes/lite6/collision/link5.stl",
      "xarm_description/meshes/lite6/visual/link6.stl",
      "xarm_description/meshes/lite6/collision/link6.stl"
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
  "historical_snapshots_reused": 80,
  "primary_physics_unchanged": true,
  "source_matching": "original raw-value provenance criteria retained; kinematic guard applies to reported CoM"
}
```
