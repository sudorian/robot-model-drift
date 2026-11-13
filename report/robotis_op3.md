# robotis_op3

Status: **partial history**. Provenance: **unknown**, confidence **incomplete**.

Unresolved historical compilation prevents selecting or rejecting a matching source. Pairwise M/H differences are reported with unknown provenance.

M: `https://github.com/google-deepmind/mujoco_menagerie`, `robotis_op3/op3.xml`, commit `370c43965323c0944b433b202aac5058b5f907a9`.
H: `https://github.com/ROBOTIS-GIT/ROBOTIS-OP3-Common`, `op3_description/urdf/robotis_op3.urdf.xacro`, commit `0780e54c2064a42089b0cf970d716ae44fec9233`.
S: unavailable. A machine-readable H can still be compared to M; no-match differences are never counted as STALE.

Limit semantics: MJCF effort values are supported actuator torque/force envelopes. URDF effort and velocity values are manufacturer declarations retained from XML; MuJoCo does not enforce those tags. Such declaration comparisons are explicitly distinct from compiled inertial/range quantities.


## Source evidence

```json
[
  {
    "url": "https://github.com/ROBOTIS-GIT/ROBOTIS-OP3-Common/tree/master/op3_description/urdf",
    "document": "robotis_op3/README.md",
    "commit": "370c43965323c0944b433b202aac5058b5f907a9",
    "current": true
  }
]
```


## Kinematics consistency

A proper Kabsch rigid transform aligns all matched zero-pose body origins. The maximum per-origin residual and signed hinge/slide axis angles determine whether CoM can be compared; RMS is also recorded. Fewer than three non-collinear origins give insufficient kinematic coverage. CoM records that fail either required M/H or M/S check are excluded from counts and largest discrepancies. Masses, principal moments and raw joint ranges remain unchanged; a flagged range still requires convention review.

| Pair | Status | Origins / rank | RMS / maximum mm | Disagreeing / checked axes |
|---|---|---:|---:|---:|
| M/H | consistent | 21 / 3 | 3.92030626e-14 / 6.40725889e-14 | 0 / 20 |

Exact fitted transforms, per-origin residuals, thresholds and axis vectors:

```json
{
  "M/H": {
    "status": "consistent",
    "matched_body_origins": 21,
    "position_threshold_m": 0.005,
    "axis_threshold_rad": 0.005,
    "residual_definition": "maximum Euclidean residual over matched body origins; Kabsch minimizes RMS, which is also recorded",
    "coordinate_frames": "each snapshot registered to its matched report anchor",
    "anchor_m": "body_link",
    "anchor_other": "body_link",
    "rotation_other_to_m": [
      [
        1.0,
        -8.12127359886603e-17,
        -8.750210550791598e-17
      ],
      [
        -1.949432741973421e-17,
        1.0,
        7.315418681470978e-17
      ],
      [
        6.245004513516506e-17,
        -1.9739679319287842e-16,
        0.9999999999999999
      ]
    ],
    "translation_other_to_m": [
      -1.8431436932253575e-18,
      1.6263032587282567e-18,
      -1.3877787807814457e-17
    ],
    "rms_residual_m": 3.9203062560732384e-17,
    "max_residual_m": 6.407258894787028e-17,
    "fit_rank": 3,
    "axis_checks": [
      {
        "joint_m": "head_pan",
        "joint_other": "head_pan",
        "axis_m": [
          0.0,
          0.0,
          1.0
        ],
        "axis_other_aligned": [
          -8.750210550791599e-17,
          7.315418681470979e-17,
          1.0
        ],
        "angle_rad": 1.1405329244191033e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "head_tilt",
        "joint_other": "head_tilt",
        "axis_m": [
          0.0,
          -1.0,
          0.0
        ],
        "axis_other_aligned": [
          8.12127359886603e-17,
          -1.0,
          1.9739679319287842e-16
        ],
        "angle_rad": 2.1345023412869766e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "l_sho_pitch",
        "joint_other": "l_sho_pitch",
        "axis_m": [
          0.0,
          1.0,
          0.0
        ],
        "axis_other_aligned": [
          -8.12127359886603e-17,
          1.0,
          -1.9739679319287842e-16
        ],
        "angle_rad": 2.1345023412869766e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "l_sho_roll",
        "joint_other": "l_sho_roll",
        "axis_m": [
          -1.0,
          0.0,
          0.0
        ],
        "axis_other_aligned": [
          -1.0,
          1.949432741973421e-17,
          -6.245004513516506e-17
        ],
        "angle_rad": 6.542199124860045e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "l_el",
        "joint_other": "l_el",
        "axis_m": [
          1.0,
          0.0,
          0.0
        ],
        "axis_other_aligned": [
          1.0,
          -1.949432741973421e-17,
          6.245004513516506e-17
        ],
        "angle_rad": 6.542199124860045e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "r_sho_pitch",
        "joint_other": "r_sho_pitch",
        "axis_m": [
          0.0,
          -1.0,
          0.0
        ],
        "axis_other_aligned": [
          8.12127359886603e-17,
          -1.0,
          1.9739679319287842e-16
        ],
        "angle_rad": 2.1345023412869766e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "r_sho_roll",
        "joint_other": "r_sho_roll",
        "axis_m": [
          -1.0,
          0.0,
          0.0
        ],
        "axis_other_aligned": [
          -1.0,
          1.949432741973421e-17,
          -6.245004513516506e-17
        ],
        "angle_rad": 6.542199124860045e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "r_el",
        "joint_other": "r_el",
        "axis_m": [
          1.0,
          0.0,
          0.0
        ],
        "axis_other_aligned": [
          1.0,
          -1.949432741973421e-17,
          6.245004513516506e-17
        ],
        "angle_rad": 6.542199124860045e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "l_hip_yaw",
        "joint_other": "l_hip_yaw",
        "axis_m": [
          0.0,
          0.0,
          -1.0
        ],
        "axis_other_aligned": [
          8.750210550791599e-17,
          -7.315418681470979e-17,
          -1.0
        ],
        "angle_rad": 1.1405329244191033e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "l_hip_roll",
        "joint_other": "l_hip_roll",
        "axis_m": [
          -1.0,
          0.0,
          0.0
        ],
        "axis_other_aligned": [
          -1.0,
          1.949432741973421e-17,
          -6.245004513516506e-17
        ],
        "angle_rad": 6.542199124860045e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "l_hip_pitch",
        "joint_other": "l_hip_pitch",
        "axis_m": [
          0.0,
          1.0,
          0.0
        ],
        "axis_other_aligned": [
          -8.12127359886603e-17,
          1.0,
          -1.9739679319287842e-16
        ],
        "angle_rad": 2.1345023412869766e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "l_knee",
        "joint_other": "l_knee",
        "axis_m": [
          0.0,
          1.0,
          0.0
        ],
        "axis_other_aligned": [
          -8.12127359886603e-17,
          1.0,
          -1.9739679319287842e-16
        ],
        "angle_rad": 2.1345023412869766e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "l_ank_pitch",
        "joint_other": "l_ank_pitch",
        "axis_m": [
          0.0,
          -1.0,
          0.0
        ],
        "axis_other_aligned": [
          8.12127359886603e-17,
          -1.0,
          1.9739679319287842e-16
        ],
        "angle_rad": 2.1345023412869766e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "l_ank_roll",
        "joint_other": "l_ank_roll",
        "axis_m": [
          1.0,
          0.0,
          0.0
        ],
        "axis_other_aligned": [
          1.0,
          -1.949432741973421e-17,
          6.245004513516506e-17
        ],
        "angle_rad": 6.542199124860045e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "r_hip_yaw",
        "joint_other": "r_hip_yaw",
        "axis_m": [
          0.0,
          0.0,
          -1.0
        ],
        "axis_other_aligned": [
          8.750210550791599e-17,
          -7.315418681470979e-17,
          -1.0
        ],
        "angle_rad": 1.1405329244191033e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "r_hip_roll",
        "joint_other": "r_hip_roll",
        "axis_m": [
          -1.0,
          0.0,
          0.0
        ],
        "axis_other_aligned": [
          -1.0,
          1.949432741973421e-17,
          -6.245004513516506e-17
        ],
        "angle_rad": 6.542199124860045e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "r_hip_pitch",
        "joint_other": "r_hip_pitch",
        "axis_m": [
          0.0,
          -1.0,
          0.0
        ],
        "axis_other_aligned": [
          8.12127359886603e-17,
          -1.0,
          1.9739679319287842e-16
        ],
        "angle_rad": 2.1345023412869766e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "r_knee",
        "joint_other": "r_knee",
        "axis_m": [
          0.0,
          -1.0,
          0.0
        ],
        "axis_other_aligned": [
          8.12127359886603e-17,
          -1.0,
          1.9739679319287842e-16
        ],
        "angle_rad": 2.1345023412869766e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "r_ank_pitch",
        "joint_other": "r_ank_pitch",
        "axis_m": [
          0.0,
          1.0,
          0.0
        ],
        "axis_other_aligned": [
          -8.12127359886603e-17,
          1.0,
          -1.9739679319287842e-16
        ],
        "angle_rad": 2.1345023412869766e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "r_ank_roll",
        "joint_other": "r_ank_roll",
        "axis_m": [
          1.0,
          0.0,
          0.0
        ],
        "axis_other_aligned": [
          1.0,
          -1.949432741973421e-17,
          6.245004513516506e-17
        ],
        "angle_rad": 6.542199124860045e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      }
    ],
    "axis_disagreements": [],
    "com_eligible": true,
    "covariance_singular_values": [
      0.39146002111522327,
      0.11201950104615242,
      0.0025067047433864247
    ],
    "origin_residuals_m": {
      "body_link": 1.409379421596435e-17,
      "head_pan_link": 5.838980279735072e-17,
      "head_tilt_link": 5.908255262090379e-17,
      "l_sho_pitch_link": 3.3016760004254755e-17,
      "l_sho_roll_link": 2.8609792490763984e-17,
      "l_el_link": 5.003707553108401e-17,
      "r_sho_pitch_link": 9.813077866773595e-18,
      "r_sho_roll_link": 3.179800655392251e-17,
      "r_el_link": 2.7755575615628914e-17,
      "l_hip_yaw_link": 2.1308229155770223e-17,
      "l_hip_roll_link": 4.9065389333867974e-18,
      "l_hip_pitch_link": 5.101802001556166e-18,
      "l_knee_link": 2.921087759526521e-17,
      "l_ank_pitch_link": 6.128310869405831e-17,
      "l_ank_roll_link": 6.088854689467823e-17,
      "r_hip_yaw_link": 7.04018270159899e-18,
      "r_hip_roll_link": 1.7690777709386487e-17,
      "r_hip_pitch_link": 2.4803894292413963e-17,
      "r_knee_link": 3.215502935578003e-17,
      "r_ank_pitch_link": 6.407258894787028e-17,
      "r_ank_roll_link": 6.283435673255384e-17
    },
    "reason": "Unique proper rigid fit and matched signed axes meet the configured thresholds"
  }
}
```


## Every reported quantity difference

Counts are quantity records, including correlated total/subtree/body mass records; they are not independent robot defects.

| Entity / quantity | M | S | H | H − M | Class | M source | S source | H source |
|---|---|---|---|---|---|---|---|---|
| head_pan / effort | 5 | unavailable | 1000 | 995 | unknown | [inherited actuator input L62](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/robotis_op3/op3.xml#L62) | unavailable | [input L17](https://github.com/ROBOTIS-GIT/ROBOTIS-OP3-Common/blob/0780e54c2064a42089b0cf970d716ae44fec9233/op3_description/urdf/robotis_op3.structure.head.xacro#L17) |
| head_tilt / effort | 5 | unavailable | 1000 | 995 | unknown | [inherited actuator input L62](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/robotis_op3/op3.xml#L62) | unavailable | [input L41](https://github.com/ROBOTIS-GIT/ROBOTIS-OP3-Common/blob/0780e54c2064a42089b0cf970d716ae44fec9233/op3_description/urdf/robotis_op3.structure.head.xacro#L41) |
| l_sho_pitch / effort | 5 | unavailable | 1000 | 995 | unknown | [inherited actuator input L62](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/robotis_op3/op3.xml#L62) | unavailable | [input L17](https://github.com/ROBOTIS-GIT/ROBOTIS-OP3-Common/blob/0780e54c2064a42089b0cf970d716ae44fec9233/op3_description/urdf/robotis_op3.structure.larm.xacro#L17) |
| l_sho_roll / effort | 5 | unavailable | 1000 | 995 | unknown | [inherited actuator input L62](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/robotis_op3/op3.xml#L62) | unavailable | [input L41](https://github.com/ROBOTIS-GIT/ROBOTIS-OP3-Common/blob/0780e54c2064a42089b0cf970d716ae44fec9233/op3_description/urdf/robotis_op3.structure.larm.xacro#L41) |
| l_el / effort | 5 | unavailable | 1000 | 995 | unknown | [inherited actuator input L62](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/robotis_op3/op3.xml#L62) | unavailable | [input L65](https://github.com/ROBOTIS-GIT/ROBOTIS-OP3-Common/blob/0780e54c2064a42089b0cf970d716ae44fec9233/op3_description/urdf/robotis_op3.structure.larm.xacro#L65) |
| r_sho_pitch / effort | 5 | unavailable | 1000 | 995 | unknown | [inherited actuator input L62](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/robotis_op3/op3.xml#L62) | unavailable | [input L17](https://github.com/ROBOTIS-GIT/ROBOTIS-OP3-Common/blob/0780e54c2064a42089b0cf970d716ae44fec9233/op3_description/urdf/robotis_op3.structure.rarm.xacro#L17) |
| r_sho_roll / effort | 5 | unavailable | 1000 | 995 | unknown | [inherited actuator input L62](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/robotis_op3/op3.xml#L62) | unavailable | [input L41](https://github.com/ROBOTIS-GIT/ROBOTIS-OP3-Common/blob/0780e54c2064a42089b0cf970d716ae44fec9233/op3_description/urdf/robotis_op3.structure.rarm.xacro#L41) |
| r_el / effort | 5 | unavailable | 1000 | 995 | unknown | [inherited actuator input L62](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/robotis_op3/op3.xml#L62) | unavailable | [input L65](https://github.com/ROBOTIS-GIT/ROBOTIS-OP3-Common/blob/0780e54c2064a42089b0cf970d716ae44fec9233/op3_description/urdf/robotis_op3.structure.rarm.xacro#L65) |
| l_hip_yaw / effort | 5 | unavailable | 1000 | 995 | unknown | [inherited actuator input L62](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/robotis_op3/op3.xml#L62) | unavailable | [input L17](https://github.com/ROBOTIS-GIT/ROBOTIS-OP3-Common/blob/0780e54c2064a42089b0cf970d716ae44fec9233/op3_description/urdf/robotis_op3.structure.lleg.xacro#L17) |
| l_hip_roll / effort | 5 | unavailable | 1000 | 995 | unknown | [inherited actuator input L62](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/robotis_op3/op3.xml#L62) | unavailable | [input L41](https://github.com/ROBOTIS-GIT/ROBOTIS-OP3-Common/blob/0780e54c2064a42089b0cf970d716ae44fec9233/op3_description/urdf/robotis_op3.structure.lleg.xacro#L41) |
| l_hip_pitch / effort | 5 | unavailable | 1000 | 995 | unknown | [inherited actuator input L62](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/robotis_op3/op3.xml#L62) | unavailable | [input L65](https://github.com/ROBOTIS-GIT/ROBOTIS-OP3-Common/blob/0780e54c2064a42089b0cf970d716ae44fec9233/op3_description/urdf/robotis_op3.structure.lleg.xacro#L65) |
| l_knee / effort | 5 | unavailable | 1000 | 995 | unknown | [inherited actuator input L62](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/robotis_op3/op3.xml#L62) | unavailable | [input L89](https://github.com/ROBOTIS-GIT/ROBOTIS-OP3-Common/blob/0780e54c2064a42089b0cf970d716ae44fec9233/op3_description/urdf/robotis_op3.structure.lleg.xacro#L89) |
| l_ank_pitch / effort | 5 | unavailable | 1000 | 995 | unknown | [inherited actuator input L62](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/robotis_op3/op3.xml#L62) | unavailable | [input L113](https://github.com/ROBOTIS-GIT/ROBOTIS-OP3-Common/blob/0780e54c2064a42089b0cf970d716ae44fec9233/op3_description/urdf/robotis_op3.structure.lleg.xacro#L113) |
| l_ank_roll / effort | 5 | unavailable | 1000 | 995 | unknown | [inherited actuator input L62](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/robotis_op3/op3.xml#L62) | unavailable | [input L137](https://github.com/ROBOTIS-GIT/ROBOTIS-OP3-Common/blob/0780e54c2064a42089b0cf970d716ae44fec9233/op3_description/urdf/robotis_op3.structure.lleg.xacro#L137) |
| r_hip_yaw / effort | 5 | unavailable | 1000 | 995 | unknown | [inherited actuator input L62](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/robotis_op3/op3.xml#L62) | unavailable | [input L17](https://github.com/ROBOTIS-GIT/ROBOTIS-OP3-Common/blob/0780e54c2064a42089b0cf970d716ae44fec9233/op3_description/urdf/robotis_op3.structure.rleg.xacro#L17) |
| r_hip_roll / effort | 5 | unavailable | 1000 | 995 | unknown | [inherited actuator input L62](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/robotis_op3/op3.xml#L62) | unavailable | [input L41](https://github.com/ROBOTIS-GIT/ROBOTIS-OP3-Common/blob/0780e54c2064a42089b0cf970d716ae44fec9233/op3_description/urdf/robotis_op3.structure.rleg.xacro#L41) |
| r_hip_pitch / effort | 5 | unavailable | 1000 | 995 | unknown | [inherited actuator input L62](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/robotis_op3/op3.xml#L62) | unavailable | [input L65](https://github.com/ROBOTIS-GIT/ROBOTIS-OP3-Common/blob/0780e54c2064a42089b0cf970d716ae44fec9233/op3_description/urdf/robotis_op3.structure.rleg.xacro#L65) |
| r_knee / effort | 5 | unavailable | 1000 | 995 | unknown | [inherited actuator input L62](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/robotis_op3/op3.xml#L62) | unavailable | [input L89](https://github.com/ROBOTIS-GIT/ROBOTIS-OP3-Common/blob/0780e54c2064a42089b0cf970d716ae44fec9233/op3_description/urdf/robotis_op3.structure.rleg.xacro#L89) |
| r_ank_pitch / effort | 5 | unavailable | 1000 | 995 | unknown | [inherited actuator input L62](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/robotis_op3/op3.xml#L62) | unavailable | [input L113](https://github.com/ROBOTIS-GIT/ROBOTIS-OP3-Common/blob/0780e54c2064a42089b0cf970d716ae44fec9233/op3_description/urdf/robotis_op3.structure.rleg.xacro#L113) |
| r_ank_roll / effort | 5 | unavailable | 1000 | 995 | unknown | [inherited actuator input L62](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/robotis_op3/op3.xml#L62) | unavailable | [input L137](https://github.com/ROBOTIS-GIT/ROBOTIS-OP3-Common/blob/0780e54c2064a42089b0cf970d716ae44fec9233/op3_description/urdf/robotis_op3.structure.rleg.xacro#L137) |

## Raw CoM records and reporting decisions

Raw values retain the previous root-anchor registration before Kabsch; original world coordinates also remain in the snapshots. Eligible findings above use the fitted transform into M. Excluded raw records below are diagnostic numbers, not findings. No CoM suppression applies to mass or principal inertia moments.

| Entity / quantity | Raw M | Raw S | Raw H | Raw H − M | Decision | M source | S source | H source |
|---|---|---|---|---|---|---|---|---|
| robot / total_com_registered | [-0.0105675148, 7.17532177e-05, -0.00483834572] | unavailable | [-0.0105675148, 7.17532177e-05, -0.00483834572] | [0, -7.58941521e-19, 9.36750677e-17] | eligible; compared after Kabsch alignment | [aggregate inputs](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/robotis_op3/op3.xml#L1) | unavailable | [aggregate inputs](https://github.com/ROBOTIS-GIT/ROBOTIS-OP3-Common/blob/0780e54c2064a42089b0cf970d716ae44fec9233/op3_description/urdf/robotis_op3.urdf.xacro#L1) |
| body_link / com_registered | [-0.01501, 0.00013, 0.06582] | unavailable | [-0.01501, 0.00013, 0.06582] | [0, 0, 1.38777878e-17] | eligible; compared after Kabsch alignment | [CoM/kinematic input L77](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/robotis_op3/op3.xml#L77) | unavailable | [geometry/inference input L44](https://github.com/ROBOTIS-GIT/ROBOTIS-OP3-Common/blob/0780e54c2064a42089b0cf970d716ae44fec9233/op3_description/urdf/robotis_op3.urdf.xacro#L44) |
| head_pan_link / com_registered | [0.00133, 0, 0.14473] | unavailable | [0.00133, 0, 0.14473] | [0, 0, -2.77555756e-17] | eligible; compared after Kabsch alignment | [CoM/kinematic input L88](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/robotis_op3/op3.xml#L88) | unavailable | [geometry/inference input L23](https://github.com/ROBOTIS-GIT/ROBOTIS-OP3-Common/blob/0780e54c2064a42089b0cf970d716ae44fec9233/op3_description/urdf/robotis_op3.structure.head.xacro#L23) |
| head_tilt_link / com_registered | [0.0113, 0.00037, 0.1927] | unavailable | [0.0113, 0.00037, 0.1927] | [0, 0, -2.77555756e-17] | eligible; compared after Kabsch alignment | [CoM/kinematic input L94](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/robotis_op3/op3.xml#L94) | unavailable | [geometry/inference input L47](https://github.com/ROBOTIS-GIT/ROBOTIS-OP3-Common/blob/0780e54c2064a42089b0cf970d716ae44fec9233/op3_description/urdf/robotis_op3.structure.head.xacro#L47) |
| l_sho_pitch_link / com_registered | [-0.001, 0.06823, 0.10867] | unavailable | [-0.001, 0.06823, 0.10867] | [0, 0, 1.38777878e-17] | eligible; compared after Kabsch alignment | [CoM/kinematic input L106](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/robotis_op3/op3.xml#L106) | unavailable | [geometry/inference input L23](https://github.com/ROBOTIS-GIT/ROBOTIS-OP3-Common/blob/0780e54c2064a42089b0cf970d716ae44fec9233/op3_description/urdf/robotis_op3.structure.larm.xacro#L23) |
| l_sho_roll_link / com_registered | [-0.00044, 0.13364, 0.10128] | unavailable | [-0.00044, 0.13364, 0.10128] | [0, 0, 2.77555756e-17] | eligible; compared after Kabsch alignment | [CoM/kinematic input L112](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/robotis_op3/op3.xml#L112) | unavailable | [geometry/inference input L47](https://github.com/ROBOTIS-GIT/ROBOTIS-OP3-Common/blob/0780e54c2064a42089b0cf970d716ae44fec9233/op3_description/urdf/robotis_op3.structure.larm.xacro#L47) |
| l_el_link / com_registered | [-0.001, 0.24923, 0.1047] | unavailable | [-0.001, 0.24923, 0.1047] | [0, 0, -1.38777878e-17] | eligible; compared after Kabsch alignment | [CoM/kinematic input L118](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/robotis_op3/op3.xml#L118) | unavailable | [geometry/inference input L71](https://github.com/ROBOTIS-GIT/ROBOTIS-OP3-Common/blob/0780e54c2064a42089b0cf970d716ae44fec9233/op3_description/urdf/robotis_op3.structure.larm.xacro#L71) |
| r_sho_pitch_link / com_registered | [-0.001, -0.06823, 0.10867] | unavailable | [-0.001, -0.06823, 0.10867] | [0, 0, 1.38777878e-17] | eligible; compared after Kabsch alignment | [CoM/kinematic input L127](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/robotis_op3/op3.xml#L127) | unavailable | [geometry/inference input L23](https://github.com/ROBOTIS-GIT/ROBOTIS-OP3-Common/blob/0780e54c2064a42089b0cf970d716ae44fec9233/op3_description/urdf/robotis_op3.structure.rarm.xacro#L23) |
| r_sho_roll_link / com_registered | [-0.00044, -0.13364, 0.10128] | unavailable | [-0.00044, -0.13364, 0.10128] | [0, 0, 2.77555756e-17] | eligible; compared after Kabsch alignment | [CoM/kinematic input L133](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/robotis_op3/op3.xml#L133) | unavailable | [geometry/inference input L47](https://github.com/ROBOTIS-GIT/ROBOTIS-OP3-Common/blob/0780e54c2064a42089b0cf970d716ae44fec9233/op3_description/urdf/robotis_op3.structure.rarm.xacro#L47) |
| r_el_link / com_registered | [-0.001, -0.24923, 0.1047] | unavailable | [-0.001, -0.24923, 0.1047] | [0, 0, -1.38777878e-17] | eligible; compared after Kabsch alignment | [CoM/kinematic input L139](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/robotis_op3/op3.xml#L139) | unavailable | [geometry/inference input L71](https://github.com/ROBOTIS-GIT/ROBOTIS-OP3-Common/blob/0780e54c2064a42089b0cf970d716ae44fec9233/op3_description/urdf/robotis_op3.structure.rarm.xacro#L71) |
| l_hip_yaw_link / com_registered | [-0.00157, 0.035, -0.00774] | unavailable | [-0.00157, 0.035, -0.00774] | [0, 0, 2.42861287e-17] | eligible; compared after Kabsch alignment | [CoM/kinematic input L148](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/robotis_op3/op3.xml#L148) | unavailable | [geometry/inference input L23](https://github.com/ROBOTIS-GIT/ROBOTIS-OP3-Common/blob/0780e54c2064a42089b0cf970d716ae44fec9233/op3_description/urdf/robotis_op3.structure.lleg.xacro#L23) |
| l_hip_roll_link / com_registered | [-0.02012, 0.03528, -0.04064] | unavailable | [-0.02012, 0.03528, -0.04064] | [0, 0, 6.9388939e-18] | eligible; compared after Kabsch alignment | [CoM/kinematic input L154](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/robotis_op3/op3.xml#L154) | unavailable | [geometry/inference input L47](https://github.com/ROBOTIS-GIT/ROBOTIS-OP3-Common/blob/0780e54c2064a42089b0cf970d716ae44fec9233/op3_description/urdf/robotis_op3.structure.lleg.xacro#L47) |
| l_hip_pitch_link / com_registered | [0.00069, 0.03499, -0.11258] | unavailable | [0.00069, 0.03499, -0.11258] | [0, 0, 1.38777878e-17] | eligible; compared after Kabsch alignment | [CoM/kinematic input L160](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/robotis_op3/op3.xml#L160) | unavailable | [geometry/inference input L71](https://github.com/ROBOTIS-GIT/ROBOTIS-OP3-Common/blob/0780e54c2064a42089b0cf970d716ae44fec9233/op3_description/urdf/robotis_op3.structure.lleg.xacro#L71) |
| l_knee_link / com_registered | [0.0001, 0.03249, -0.19365] | unavailable | [0.0001, 0.03249, -0.19365] | [0, 0, 2.77555756e-17] | eligible; compared after Kabsch alignment | [CoM/kinematic input L165](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/robotis_op3/op3.xml#L165) | unavailable | [geometry/inference input L95](https://github.com/ROBOTIS-GIT/ROBOTIS-OP3-Common/blob/0780e54c2064a42089b0cf970d716ae44fec9233/op3_description/urdf/robotis_op3.structure.lleg.xacro#L95) |
| l_ank_pitch_link / com_registered | [-0.02012, 0.03528, -0.23651] | unavailable | [-0.02012, 0.03528, -0.23651] | [0, 0, 5.55111512e-17] | eligible; compared after Kabsch alignment | [CoM/kinematic input L171](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/robotis_op3/op3.xml#L171) | unavailable | [geometry/inference input L119](https://github.com/ROBOTIS-GIT/ROBOTIS-OP3-Common/blob/0780e54c2064a42089b0cf970d716ae44fec9233/op3_description/urdf/robotis_op3.structure.lleg.xacro#L119) |
| l_ank_roll_link / com_registered | [-0.00027, 0.04537, -0.27625] | unavailable | [-0.00027, 0.04537, -0.27625] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L177](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/robotis_op3/op3.xml#L177) | unavailable | [geometry/inference input L143](https://github.com/ROBOTIS-GIT/ROBOTIS-OP3-Common/blob/0780e54c2064a42089b0cf970d716ae44fec9233/op3_description/urdf/robotis_op3.structure.lleg.xacro#L143) |
| r_hip_yaw_link / com_registered | [-0.00157, -0.035, -0.00774] | unavailable | [-0.00157, -0.035, -0.00774] | [0, 0, 2.42861287e-17] | eligible; compared after Kabsch alignment | [CoM/kinematic input L191](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/robotis_op3/op3.xml#L191) | unavailable | [geometry/inference input L23](https://github.com/ROBOTIS-GIT/ROBOTIS-OP3-Common/blob/0780e54c2064a42089b0cf970d716ae44fec9233/op3_description/urdf/robotis_op3.structure.rleg.xacro#L23) |
| r_hip_roll_link / com_registered | [-0.02012, -0.03528, -0.04064] | unavailable | [-0.02012, -0.03528, -0.04064] | [0, 0, 6.9388939e-18] | eligible; compared after Kabsch alignment | [CoM/kinematic input L197](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/robotis_op3/op3.xml#L197) | unavailable | [geometry/inference input L47](https://github.com/ROBOTIS-GIT/ROBOTIS-OP3-Common/blob/0780e54c2064a42089b0cf970d716ae44fec9233/op3_description/urdf/robotis_op3.structure.rleg.xacro#L47) |
| r_hip_pitch_link / com_registered | [0.00069, -0.03499, -0.11258] | unavailable | [0.00069, -0.03499, -0.11258] | [0, 0, 1.38777878e-17] | eligible; compared after Kabsch alignment | [CoM/kinematic input L203](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/robotis_op3/op3.xml#L203) | unavailable | [geometry/inference input L71](https://github.com/ROBOTIS-GIT/ROBOTIS-OP3-Common/blob/0780e54c2064a42089b0cf970d716ae44fec9233/op3_description/urdf/robotis_op3.structure.rleg.xacro#L71) |
| r_knee_link / com_registered | [0.0001, -0.03249, -0.19365] | unavailable | [0.0001, -0.03249, -0.19365] | [0, 0, 2.77555756e-17] | eligible; compared after Kabsch alignment | [CoM/kinematic input L208](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/robotis_op3/op3.xml#L208) | unavailable | [geometry/inference input L95](https://github.com/ROBOTIS-GIT/ROBOTIS-OP3-Common/blob/0780e54c2064a42089b0cf970d716ae44fec9233/op3_description/urdf/robotis_op3.structure.rleg.xacro#L95) |
| r_ank_pitch_link / com_registered | [-0.02012, -0.03528, -0.23651] | unavailable | [-0.02012, -0.03528, -0.23651] | [0, 0, 5.55111512e-17] | eligible; compared after Kabsch alignment | [CoM/kinematic input L214](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/robotis_op3/op3.xml#L214) | unavailable | [geometry/inference input L119](https://github.com/ROBOTIS-GIT/ROBOTIS-OP3-Common/blob/0780e54c2064a42089b0cf970d716ae44fec9233/op3_description/urdf/robotis_op3.structure.rleg.xacro#L119) |
| r_ank_roll_link / com_registered | [-0.00027, -0.04537, -0.27625] | unavailable | [-0.00027, -0.04537, -0.27625] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L220](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/robotis_op3/op3.xml#L220) | unavailable | [geometry/inference input L143](https://github.com/ROBOTIS-GIT/ROBOTIS-OP3-Common/blob/0780e54c2064a42089b0cf970d716ae44fec9233/op3_description/urdf/robotis_op3.structure.rleg.xacro#L143) |

## Mass accounting

Every contributing compiled body mass is listed here so total/subtree sums can be checked. Links point to explicit inertials or to geometry inputs when the compiler inferred a mass. CoM links identify inertial inputs; world coordinates additionally use the ancestor transforms and the registration recorded below.

| M body | M kg / source | S kg / source | H kg / source |
|---|---|---|---|
| body_link | 1.34928 / [input L77](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/robotis_op3/op3.xml#L77) | unavailable | 1.34928 / [geometry/inference input L44](https://github.com/ROBOTIS-GIT/ROBOTIS-OP3-Common/blob/0780e54c2064a42089b0cf970d716ae44fec9233/op3_description/urdf/robotis_op3.urdf.xacro#L44) |
| head_pan_link | 0.01176 / [input L88](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/robotis_op3/op3.xml#L88) | unavailable | 0.01176 / [geometry/inference input L23](https://github.com/ROBOTIS-GIT/ROBOTIS-OP3-Common/blob/0780e54c2064a42089b0cf970d716ae44fec9233/op3_description/urdf/robotis_op3.structure.head.xacro#L23) |
| head_tilt_link | 0.13631 / [input L94](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/robotis_op3/op3.xml#L94) | unavailable | 0.13631 / [geometry/inference input L47](https://github.com/ROBOTIS-GIT/ROBOTIS-OP3-Common/blob/0780e54c2064a42089b0cf970d716ae44fec9233/op3_description/urdf/robotis_op3.structure.head.xacro#L47) |
| l_sho_pitch_link | 0.01176 / [input L106](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/robotis_op3/op3.xml#L106) | unavailable | 0.01176 / [geometry/inference input L23](https://github.com/ROBOTIS-GIT/ROBOTIS-OP3-Common/blob/0780e54c2064a42089b0cf970d716ae44fec9233/op3_description/urdf/robotis_op3.structure.larm.xacro#L23) |
| l_sho_roll_link | 0.17758 / [input L112](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/robotis_op3/op3.xml#L112) | unavailable | 0.17758 / [geometry/inference input L47](https://github.com/ROBOTIS-GIT/ROBOTIS-OP3-Common/blob/0780e54c2064a42089b0cf970d716ae44fec9233/op3_description/urdf/robotis_op3.structure.larm.xacro#L47) |
| l_el_link | 0.04127 / [input L118](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/robotis_op3/op3.xml#L118) | unavailable | 0.04127 / [geometry/inference input L71](https://github.com/ROBOTIS-GIT/ROBOTIS-OP3-Common/blob/0780e54c2064a42089b0cf970d716ae44fec9233/op3_description/urdf/robotis_op3.structure.larm.xacro#L71) |
| r_sho_pitch_link | 0.01176 / [input L127](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/robotis_op3/op3.xml#L127) | unavailable | 0.01176 / [geometry/inference input L23](https://github.com/ROBOTIS-GIT/ROBOTIS-OP3-Common/blob/0780e54c2064a42089b0cf970d716ae44fec9233/op3_description/urdf/robotis_op3.structure.rarm.xacro#L23) |
| r_sho_roll_link | 0.17758 / [input L133](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/robotis_op3/op3.xml#L133) | unavailable | 0.17758 / [geometry/inference input L47](https://github.com/ROBOTIS-GIT/ROBOTIS-OP3-Common/blob/0780e54c2064a42089b0cf970d716ae44fec9233/op3_description/urdf/robotis_op3.structure.rarm.xacro#L47) |
| r_el_link | 0.04127 / [input L139](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/robotis_op3/op3.xml#L139) | unavailable | 0.04127 / [geometry/inference input L71](https://github.com/ROBOTIS-GIT/ROBOTIS-OP3-Common/blob/0780e54c2064a42089b0cf970d716ae44fec9233/op3_description/urdf/robotis_op3.structure.rarm.xacro#L71) |
| l_hip_yaw_link | 0.01181 / [input L148](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/robotis_op3/op3.xml#L148) | unavailable | 0.01181 / [geometry/inference input L23](https://github.com/ROBOTIS-GIT/ROBOTIS-OP3-Common/blob/0780e54c2064a42089b0cf970d716ae44fec9233/op3_description/urdf/robotis_op3.structure.lleg.xacro#L23) |
| l_hip_roll_link | 0.17886 / [input L154](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/robotis_op3/op3.xml#L154) | unavailable | 0.17886 / [geometry/inference input L47](https://github.com/ROBOTIS-GIT/ROBOTIS-OP3-Common/blob/0780e54c2064a42089b0cf970d716ae44fec9233/op3_description/urdf/robotis_op3.structure.lleg.xacro#L47) |
| l_hip_pitch_link | 0.11543 / [input L160](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/robotis_op3/op3.xml#L160) | unavailable | 0.11543 / [geometry/inference input L71](https://github.com/ROBOTIS-GIT/ROBOTIS-OP3-Common/blob/0780e54c2064a42089b0cf970d716ae44fec9233/op3_description/urdf/robotis_op3.structure.lleg.xacro#L71) |
| l_knee_link | 0.04015 / [input L165](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/robotis_op3/op3.xml#L165) | unavailable | 0.04015 / [geometry/inference input L95](https://github.com/ROBOTIS-GIT/ROBOTIS-OP3-Common/blob/0780e54c2064a42089b0cf970d716ae44fec9233/op3_description/urdf/robotis_op3.structure.lleg.xacro#L95) |
| l_ank_pitch_link | 0.17886 / [input L171](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/robotis_op3/op3.xml#L171) | unavailable | 0.17886 / [geometry/inference input L119](https://github.com/ROBOTIS-GIT/ROBOTIS-OP3-Common/blob/0780e54c2064a42089b0cf970d716ae44fec9233/op3_description/urdf/robotis_op3.structure.lleg.xacro#L119) |
| l_ank_roll_link | 0.06934 / [input L177](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/robotis_op3/op3.xml#L177) | unavailable | 0.06934 / [geometry/inference input L143](https://github.com/ROBOTIS-GIT/ROBOTIS-OP3-Common/blob/0780e54c2064a42089b0cf970d716ae44fec9233/op3_description/urdf/robotis_op3.structure.lleg.xacro#L143) |
| r_hip_yaw_link | 0.01181 / [input L191](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/robotis_op3/op3.xml#L191) | unavailable | 0.01181 / [geometry/inference input L23](https://github.com/ROBOTIS-GIT/ROBOTIS-OP3-Common/blob/0780e54c2064a42089b0cf970d716ae44fec9233/op3_description/urdf/robotis_op3.structure.rleg.xacro#L23) |
| r_hip_roll_link | 0.17886 / [input L197](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/robotis_op3/op3.xml#L197) | unavailable | 0.17886 / [geometry/inference input L47](https://github.com/ROBOTIS-GIT/ROBOTIS-OP3-Common/blob/0780e54c2064a42089b0cf970d716ae44fec9233/op3_description/urdf/robotis_op3.structure.rleg.xacro#L47) |
| r_hip_pitch_link | 0.11543 / [input L203](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/robotis_op3/op3.xml#L203) | unavailable | 0.11543 / [geometry/inference input L71](https://github.com/ROBOTIS-GIT/ROBOTIS-OP3-Common/blob/0780e54c2064a42089b0cf970d716ae44fec9233/op3_description/urdf/robotis_op3.structure.rleg.xacro#L71) |
| r_knee_link | 0.04015 / [input L208](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/robotis_op3/op3.xml#L208) | unavailable | 0.04015 / [geometry/inference input L95](https://github.com/ROBOTIS-GIT/ROBOTIS-OP3-Common/blob/0780e54c2064a42089b0cf970d716ae44fec9233/op3_description/urdf/robotis_op3.structure.rleg.xacro#L95) |
| r_ank_pitch_link | 0.17886 / [input L214](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/robotis_op3/op3.xml#L214) | unavailable | 0.17886 / [geometry/inference input L119](https://github.com/ROBOTIS-GIT/ROBOTIS-OP3-Common/blob/0780e54c2064a42089b0cf970d716ae44fec9233/op3_description/urdf/robotis_op3.structure.rleg.xacro#L119) |
| r_ank_roll_link | 0.06934 / [input L220](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/robotis_op3/op3.xml#L220) | unavailable | 0.06934 / [geometry/inference input L143](https://github.com/ROBOTIS-GIT/ROBOTIS-OP3-Common/blob/0780e54c2064a42089b0cf970d716ae44fec9233/op3_description/urdf/robotis_op3.structure.rleg.xacro#L143) |
| upstream-only cam_gazebo_link | unavailable | unavailable | 0 / [geometry/inference input L77](https://github.com/ROBOTIS-GIT/ROBOTIS-OP3-Common/blob/0780e54c2064a42089b0cf970d716ae44fec9233/op3_description/urdf/robotis_op3.structure.head.xacro#L77) |
| upstream-only cam_link | unavailable | unavailable | 0 / [geometry/inference input L73](https://github.com/ROBOTIS-GIT/ROBOTIS-OP3-Common/blob/0780e54c2064a42089b0cf970d716ae44fec9233/op3_description/urdf/robotis_op3.structure.head.xacro#L73) |

## Coverage and unmatched elements

```json
{
  "mapping_h": {
    "bodies": {
      "body_link": "body_link",
      "head_pan_link": "head_pan_link",
      "head_tilt_link": "head_tilt_link",
      "l_sho_pitch_link": "l_sho_pitch_link",
      "l_sho_roll_link": "l_sho_roll_link",
      "l_el_link": "l_el_link",
      "r_sho_pitch_link": "r_sho_pitch_link",
      "r_sho_roll_link": "r_sho_roll_link",
      "r_el_link": "r_el_link",
      "l_hip_yaw_link": "l_hip_yaw_link",
      "l_hip_roll_link": "l_hip_roll_link",
      "l_hip_pitch_link": "l_hip_pitch_link",
      "l_knee_link": "l_knee_link",
      "l_ank_pitch_link": "l_ank_pitch_link",
      "l_ank_roll_link": "l_ank_roll_link",
      "r_hip_yaw_link": "r_hip_yaw_link",
      "r_hip_roll_link": "r_hip_roll_link",
      "r_hip_pitch_link": "r_hip_pitch_link",
      "r_knee_link": "r_knee_link",
      "r_ank_pitch_link": "r_ank_pitch_link",
      "r_ank_roll_link": "r_ank_roll_link"
    },
    "joints": {
      "head_pan": "head_pan",
      "head_tilt": "head_tilt",
      "l_sho_pitch": "l_sho_pitch",
      "l_sho_roll": "l_sho_roll",
      "l_el": "l_el",
      "r_sho_pitch": "r_sho_pitch",
      "r_sho_roll": "r_sho_roll",
      "r_el": "r_el",
      "l_hip_yaw": "l_hip_yaw",
      "l_hip_roll": "l_hip_roll",
      "l_hip_pitch": "l_hip_pitch",
      "l_knee": "l_knee",
      "l_ank_pitch": "l_ank_pitch",
      "l_ank_roll": "l_ank_roll",
      "r_hip_yaw": "r_hip_yaw",
      "r_hip_roll": "r_hip_roll",
      "r_hip_pitch": "r_hip_pitch",
      "r_knee": "r_knee",
      "r_ank_pitch": "r_ank_pitch",
      "r_ank_roll": "r_ank_roll"
    },
    "body_methods": {
      "body_link": "name",
      "head_pan_link": "name",
      "head_tilt_link": "name",
      "l_sho_pitch_link": "name",
      "l_sho_roll_link": "name",
      "l_el_link": "name",
      "r_sho_pitch_link": "name",
      "r_sho_roll_link": "name",
      "r_el_link": "name",
      "l_hip_yaw_link": "name",
      "l_hip_roll_link": "name",
      "l_hip_pitch_link": "name",
      "l_knee_link": "name",
      "l_ank_pitch_link": "name",
      "l_ank_roll_link": "name",
      "r_hip_yaw_link": "name",
      "r_hip_roll_link": "name",
      "r_hip_pitch_link": "name",
      "r_knee_link": "name",
      "r_ank_pitch_link": "name",
      "r_ank_roll_link": "name"
    },
    "joint_methods": {
      "head_pan": "name",
      "head_tilt": "name",
      "l_sho_pitch": "name",
      "l_sho_roll": "name",
      "l_el": "name",
      "r_sho_pitch": "name",
      "r_sho_roll": "name",
      "r_el": "name",
      "l_hip_yaw": "name",
      "l_hip_roll": "name",
      "l_hip_pitch": "name",
      "l_knee": "name",
      "l_ank_pitch": "name",
      "l_ank_roll": "name",
      "r_hip_yaw": "name",
      "r_hip_roll": "name",
      "r_hip_pitch": "name",
      "r_knee": "name",
      "r_ank_pitch": "name",
      "r_ank_roll": "name"
    },
    "unmatched_m_bodies": [],
    "unmatched_upstream_bodies": [
      "cam_gazebo_link",
      "cam_link"
    ],
    "unmatched_m_joints": [],
    "unmatched_upstream_joints": [],
    "registration_anchor": {
      "M": "body_link",
      "H": "body_link",
      "root_unmatched": false
    }
  },
  "mapping_s": null,
  "unavailable": [
    {
      "entity": "head_pan",
      "other_entity": "head_pan",
      "quantity": "range",
      "tolerance": "range",
      "m": null,
      "other": [
        -2.827433388230814,
        2.827433388230814
      ],
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "head_pan",
      "other_entity": "head_pan",
      "quantity": "force",
      "tolerance": "limit",
      "m": 5.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "head_pan",
      "other_entity": "head_pan",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 100.0,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "head_tilt",
      "other_entity": "head_tilt",
      "quantity": "range",
      "tolerance": "range",
      "m": null,
      "other": [
        -2.827433388230814,
        2.827433388230814
      ],
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "head_tilt",
      "other_entity": "head_tilt",
      "quantity": "force",
      "tolerance": "limit",
      "m": 5.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "head_tilt",
      "other_entity": "head_tilt",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 100.0,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "l_sho_pitch",
      "other_entity": "l_sho_pitch",
      "quantity": "range",
      "tolerance": "range",
      "m": null,
      "other": [
        -2.827433388230814,
        2.827433388230814
      ],
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "l_sho_pitch",
      "other_entity": "l_sho_pitch",
      "quantity": "force",
      "tolerance": "limit",
      "m": 5.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "l_sho_pitch",
      "other_entity": "l_sho_pitch",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 100.0,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "l_sho_roll",
      "other_entity": "l_sho_roll",
      "quantity": "range",
      "tolerance": "range",
      "m": null,
      "other": [
        -2.827433388230814,
        2.827433388230814
      ],
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "l_sho_roll",
      "other_entity": "l_sho_roll",
      "quantity": "force",
      "tolerance": "limit",
      "m": 5.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "l_sho_roll",
      "other_entity": "l_sho_roll",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 100.0,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "l_el",
      "other_entity": "l_el",
      "quantity": "range",
      "tolerance": "range",
      "m": null,
      "other": [
        -2.827433388230814,
        2.827433388230814
      ],
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "l_el",
      "other_entity": "l_el",
      "quantity": "force",
      "tolerance": "limit",
      "m": 5.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "l_el",
      "other_entity": "l_el",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 100.0,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "r_sho_pitch",
      "other_entity": "r_sho_pitch",
      "quantity": "range",
      "tolerance": "range",
      "m": null,
      "other": [
        -2.827433388230814,
        2.827433388230814
      ],
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "r_sho_pitch",
      "other_entity": "r_sho_pitch",
      "quantity": "force",
      "tolerance": "limit",
      "m": 5.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "r_sho_pitch",
      "other_entity": "r_sho_pitch",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 100.0,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "r_sho_roll",
      "other_entity": "r_sho_roll",
      "quantity": "range",
      "tolerance": "range",
      "m": null,
      "other": [
        -2.827433388230814,
        2.827433388230814
      ],
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "r_sho_roll",
      "other_entity": "r_sho_roll",
      "quantity": "force",
      "tolerance": "limit",
      "m": 5.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "r_sho_roll",
      "other_entity": "r_sho_roll",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 100.0,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "r_el",
      "other_entity": "r_el",
      "quantity": "range",
      "tolerance": "range",
      "m": null,
      "other": [
        -2.827433388230814,
        2.827433388230814
      ],
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "r_el",
      "other_entity": "r_el",
      "quantity": "force",
      "tolerance": "limit",
      "m": 5.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "r_el",
      "other_entity": "r_el",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 100.0,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "l_hip_yaw",
      "other_entity": "l_hip_yaw",
      "quantity": "range",
      "tolerance": "range",
      "m": null,
      "other": [
        -2.827433388230814,
        2.827433388230814
      ],
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "l_hip_yaw",
      "other_entity": "l_hip_yaw",
      "quantity": "force",
      "tolerance": "limit",
      "m": 5.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "l_hip_yaw",
      "other_entity": "l_hip_yaw",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 100.0,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "l_hip_roll",
      "other_entity": "l_hip_roll",
      "quantity": "range",
      "tolerance": "range",
      "m": null,
      "other": [
        -2.827433388230814,
        2.827433388230814
      ],
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "l_hip_roll",
      "other_entity": "l_hip_roll",
      "quantity": "force",
      "tolerance": "limit",
      "m": 5.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "l_hip_roll",
      "other_entity": "l_hip_roll",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 100.0,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "l_hip_pitch",
      "other_entity": "l_hip_pitch",
      "quantity": "range",
      "tolerance": "range",
      "m": null,
      "other": [
        -2.827433388230814,
        2.827433388230814
      ],
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "l_hip_pitch",
      "other_entity": "l_hip_pitch",
      "quantity": "force",
      "tolerance": "limit",
      "m": 5.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "l_hip_pitch",
      "other_entity": "l_hip_pitch",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 100.0,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "l_knee",
      "other_entity": "l_knee",
      "quantity": "range",
      "tolerance": "range",
      "m": null,
      "other": [
        -2.827433388230814,
        2.827433388230814
      ],
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "l_knee",
      "other_entity": "l_knee",
      "quantity": "force",
      "tolerance": "limit",
      "m": 5.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "l_knee",
      "other_entity": "l_knee",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 100.0,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "l_ank_pitch",
      "other_entity": "l_ank_pitch",
      "quantity": "range",
      "tolerance": "range",
      "m": null,
      "other": [
        -2.827433388230814,
        2.827433388230814
      ],
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "l_ank_pitch",
      "other_entity": "l_ank_pitch",
      "quantity": "force",
      "tolerance": "limit",
      "m": 5.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "l_ank_pitch",
      "other_entity": "l_ank_pitch",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 100.0,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "l_ank_roll",
      "other_entity": "l_ank_roll",
      "quantity": "range",
      "tolerance": "range",
      "m": null,
      "other": [
        -2.827433388230814,
        2.827433388230814
      ],
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "l_ank_roll",
      "other_entity": "l_ank_roll",
      "quantity": "force",
      "tolerance": "limit",
      "m": 5.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "l_ank_roll",
      "other_entity": "l_ank_roll",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 100.0,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "r_hip_yaw",
      "other_entity": "r_hip_yaw",
      "quantity": "range",
      "tolerance": "range",
      "m": null,
      "other": [
        -2.827433388230814,
        2.827433388230814
      ],
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "r_hip_yaw",
      "other_entity": "r_hip_yaw",
      "quantity": "force",
      "tolerance": "limit",
      "m": 5.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "r_hip_yaw",
      "other_entity": "r_hip_yaw",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 100.0,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "r_hip_roll",
      "other_entity": "r_hip_roll",
      "quantity": "range",
      "tolerance": "range",
      "m": null,
      "other": [
        -2.827433388230814,
        2.827433388230814
      ],
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "r_hip_roll",
      "other_entity": "r_hip_roll",
      "quantity": "force",
      "tolerance": "limit",
      "m": 5.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "r_hip_roll",
      "other_entity": "r_hip_roll",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 100.0,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "r_hip_pitch",
      "other_entity": "r_hip_pitch",
      "quantity": "range",
      "tolerance": "range",
      "m": null,
      "other": [
        -2.827433388230814,
        2.827433388230814
      ],
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "r_hip_pitch",
      "other_entity": "r_hip_pitch",
      "quantity": "force",
      "tolerance": "limit",
      "m": 5.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "r_hip_pitch",
      "other_entity": "r_hip_pitch",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 100.0,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "r_knee",
      "other_entity": "r_knee",
      "quantity": "range",
      "tolerance": "range",
      "m": null,
      "other": [
        -2.827433388230814,
        2.827433388230814
      ],
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "r_knee",
      "other_entity": "r_knee",
      "quantity": "force",
      "tolerance": "limit",
      "m": 5.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "r_knee",
      "other_entity": "r_knee",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 100.0,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "r_ank_pitch",
      "other_entity": "r_ank_pitch",
      "quantity": "range",
      "tolerance": "range",
      "m": null,
      "other": [
        -2.827433388230814,
        2.827433388230814
      ],
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "r_ank_pitch",
      "other_entity": "r_ank_pitch",
      "quantity": "force",
      "tolerance": "limit",
      "m": 5.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "r_ank_pitch",
      "other_entity": "r_ank_pitch",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 100.0,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "r_ank_roll",
      "other_entity": "r_ank_roll",
      "quantity": "range",
      "tolerance": "range",
      "m": null,
      "other": [
        -2.827433388230814,
        2.827433388230814
      ],
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "r_ank_roll",
      "other_entity": "r_ank_roll",
      "quantity": "force",
      "tolerance": "limit",
      "m": 5.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "r_ank_roll",
      "other_entity": "r_ank_roll",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 100.0,
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
| head_pan / force | 5 | unavailable | unavailable |
| head_pan / velocity | unavailable | unavailable | 100 |
| head_tilt / force | 5 | unavailable | unavailable |
| head_tilt / velocity | unavailable | unavailable | 100 |
| l_sho_pitch / force | 5 | unavailable | unavailable |
| l_sho_pitch / velocity | unavailable | unavailable | 100 |
| l_sho_roll / force | 5 | unavailable | unavailable |
| l_sho_roll / velocity | unavailable | unavailable | 100 |
| l_el / force | 5 | unavailable | unavailable |
| l_el / velocity | unavailable | unavailable | 100 |
| r_sho_pitch / force | 5 | unavailable | unavailable |
| r_sho_pitch / velocity | unavailable | unavailable | 100 |
| r_sho_roll / force | 5 | unavailable | unavailable |
| r_sho_roll / velocity | unavailable | unavailable | 100 |
| r_el / force | 5 | unavailable | unavailable |
| r_el / velocity | unavailable | unavailable | 100 |
| l_hip_yaw / force | 5 | unavailable | unavailable |
| l_hip_yaw / velocity | unavailable | unavailable | 100 |
| l_hip_roll / force | 5 | unavailable | unavailable |
| l_hip_roll / velocity | unavailable | unavailable | 100 |
| l_hip_pitch / force | 5 | unavailable | unavailable |
| l_hip_pitch / velocity | unavailable | unavailable | 100 |
| l_knee / force | 5 | unavailable | unavailable |
| l_knee / velocity | unavailable | unavailable | 100 |
| l_ank_pitch / force | 5 | unavailable | unavailable |
| l_ank_pitch / velocity | unavailable | unavailable | 100 |
| l_ank_roll / force | 5 | unavailable | unavailable |
| l_ank_roll / velocity | unavailable | unavailable | 100 |
| r_hip_yaw / force | 5 | unavailable | unavailable |
| r_hip_yaw / velocity | unavailable | unavailable | 100 |
| r_hip_roll / force | 5 | unavailable | unavailable |
| r_hip_roll / velocity | unavailable | unavailable | 100 |
| r_hip_pitch / force | 5 | unavailable | unavailable |
| r_hip_pitch / velocity | unavailable | unavailable | 100 |
| r_knee / force | 5 | unavailable | unavailable |
| r_knee / velocity | unavailable | unavailable | 100 |
| r_ank_pitch / force | 5 | unavailable | unavailable |
| r_ank_pitch / velocity | unavailable | unavailable | 100 |
| r_ank_roll / force | 5 | unavailable | unavailable |
| r_ank_roll / velocity | unavailable | unavailable | 100 |
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
  "https://github.com/ROBOTIS-GIT/ROBOTIS-OP3-Common op3_description/urdf/gazebo_harness.xacro at 0780e54c2064a42089b0cf970d716ae44fec9233: ValueError: Macro add_sim_harness requires unsupported explicit arguments: ['harnessed_link']",
  "https://github.com/ROBOTIS-GIT/ROBOTIS-OP3-Common op3_description/urdf/robotis_op3.gazebo.xacro at 0780e54c2064a42089b0cf970d716ae44fec9233: ValueError: XML has no robot bodies; it is an include/extension fragment, not a standalone source",
  "https://github.com/ROBOTIS-GIT/ROBOTIS-OP3-Common op3_description/urdf/robotis_op3.inertia.xacro at 0780e54c2064a42089b0cf970d716ae44fec9233: ValueError: Macro-only input has no uniquely identified robot macro",
  "https://github.com/ROBOTIS-GIT/ROBOTIS-OP3-Common op3_description/urdf/robotis_op3.visuals.xacro at 0780e54c2064a42089b0cf970d716ae44fec9233: ValueError: Macro-only input has no uniquely identified robot macro",
  "https://github.com/ROBOTIS-GIT/ROBOTIS-OP3-Common op3_description/urdf/robotis_op3.transmissions.xacro at 0780e54c2064a42089b0cf970d716ae44fec9233: ValueError: XML has no robot bodies; it is an include/extension fragment, not a standalone source",
  "https://github.com/ROBOTIS-GIT/ROBOTIS-OP3-Common op3_description/urdf/robotis_op3.structure.head.xacro at 0780e54c2064a42089b0cf970d716ae44fec9233: XacroException: unknown macro name: xacro:insert_transmission",
  "https://github.com/ROBOTIS-GIT/ROBOTIS-OP3-Common op3_description/urdf/robotis_op3.structure.larm.xacro at 0780e54c2064a42089b0cf970d716ae44fec9233: XacroException: unknown macro name: xacro:insert_transmission",
  "https://github.com/ROBOTIS-GIT/ROBOTIS-OP3-Common op3_description/urdf/robotis_op3.structure.lleg.xacro at 0780e54c2064a42089b0cf970d716ae44fec9233: XacroException: unknown macro name: xacro:insert_transmission",
  "https://github.com/ROBOTIS-GIT/ROBOTIS-OP3-Common op3_description/urdf/robotis_op3.structure.rarm.xacro at 0780e54c2064a42089b0cf970d716ae44fec9233: XacroException: unknown macro name: xacro:insert_transmission",
  "https://github.com/ROBOTIS-GIT/ROBOTIS-OP3-Common op3_description/urdf/robotis_op3.structure.rleg.xacro at 0780e54c2064a42089b0cf970d716ae44fec9233: XacroException: unknown macro name: xacro:insert_transmission"
]
```

## History inputs

```json
[
  "op3_description/meshes/body.stl",
  "op3_description/meshes/h1.stl",
  "op3_description/meshes/h2.stl",
  "op3_description/meshes/la1.stl",
  "op3_description/meshes/la2.stl",
  "op3_description/meshes/la3.stl",
  "op3_description/meshes/ll1.stl",
  "op3_description/meshes/ll2.stl",
  "op3_description/meshes/ll3.stl",
  "op3_description/meshes/ll4.stl",
  "op3_description/meshes/ll5.stl",
  "op3_description/meshes/ll6.stl",
  "op3_description/meshes/ra1.stl",
  "op3_description/meshes/ra2.stl",
  "op3_description/meshes/ra3.stl",
  "op3_description/meshes/rl1.stl",
  "op3_description/meshes/rl2.stl",
  "op3_description/meshes/rl3.stl",
  "op3_description/meshes/rl4.stl",
  "op3_description/meshes/rl5.stl",
  "op3_description/meshes/rl6.stl",
  "op3_description/urdf/robotis_op3.gazebo.xacro",
  "op3_description/urdf/robotis_op3.inertia.xacro",
  "op3_description/urdf/robotis_op3.ros2.gazebo.xacro",
  "op3_description/urdf/robotis_op3.structure.head.xacro",
  "op3_description/urdf/robotis_op3.structure.larm.xacro",
  "op3_description/urdf/robotis_op3.structure.lleg.xacro",
  "op3_description/urdf/robotis_op3.structure.rarm.xacro",
  "op3_description/urdf/robotis_op3.structure.rleg.xacro",
  "op3_description/urdf/robotis_op3.transmissions.xacro",
  "op3_description/urdf/robotis_op3.urdf.xacro",
  "op3_description/urdf/robotis_op3.visuals.xacro",
  "robotis_op3_description/meshes/body.stl",
  "robotis_op3_description/meshes/h1.stl",
  "robotis_op3_description/meshes/h2.stl",
  "robotis_op3_description/meshes/la1.stl",
  "robotis_op3_description/meshes/la2.stl",
  "robotis_op3_description/meshes/la3.stl",
  "robotis_op3_description/meshes/ll1.stl",
  "robotis_op3_description/meshes/ll2.stl",
  "robotis_op3_description/meshes/ll3.stl",
  "robotis_op3_description/meshes/ll4.stl",
  "robotis_op3_description/meshes/ll5.stl",
  "robotis_op3_description/meshes/ll6.stl",
  "robotis_op3_description/meshes/ra1.stl",
  "robotis_op3_description/meshes/ra2.stl",
  "robotis_op3_description/meshes/ra3.stl",
  "robotis_op3_description/meshes/rl1.stl",
  "robotis_op3_description/meshes/rl2.stl",
  "robotis_op3_description/meshes/rl3.stl",
  "robotis_op3_description/meshes/rl4.stl",
  "robotis_op3_description/meshes/rl5.stl",
  "robotis_op3_description/meshes/rl6.stl",
  "robotis_op3_description/stl/body.stl",
  "robotis_op3_description/stl/h1.stl",
  "robotis_op3_description/stl/h2.stl",
  "robotis_op3_description/stl/la1.stl",
  "robotis_op3_description/stl/la2.stl",
  "robotis_op3_description/stl/la3.stl",
  "robotis_op3_description/stl/ll1.stl",
  "robotis_op3_description/stl/ll2.stl",
  "robotis_op3_description/stl/ll3.stl",
  "robotis_op3_description/stl/ll4.stl",
  "robotis_op3_description/stl/ll5.stl",
  "robotis_op3_description/stl/ll6.stl",
  "robotis_op3_description/stl/ra1.stl",
  "robotis_op3_description/stl/ra2.stl",
  "robotis_op3_description/stl/ra3.stl",
  "robotis_op3_description/stl/rl1.stl",
  "robotis_op3_description/stl/rl2.stl",
  "robotis_op3_description/stl/rl3.stl",
  "robotis_op3_description/stl/rl4.stl",
  "robotis_op3_description/stl/rl5.stl",
  "robotis_op3_description/stl/rl6.stl",
  "robotis_op3_description/urdf/gazebo_harness.xacro",
  "robotis_op3_description/urdf/robotis_op3.gazebo.xacro",
  "robotis_op3_description/urdf/robotis_op3.inertia.xacro",
  "robotis_op3_description/urdf/robotis_op3.structure.head.xacro",
  "robotis_op3_description/urdf/robotis_op3.structure.larm.xacro",
  "robotis_op3_description/urdf/robotis_op3.structure.lleg.xacro",
  "robotis_op3_description/urdf/robotis_op3.structure.rarm.xacro",
  "robotis_op3_description/urdf/robotis_op3.structure.rleg.xacro",
  "robotis_op3_description/urdf/robotis_op3.transmissions.xacro",
  "robotis_op3_description/urdf/robotis_op3.urdf.xacro",
  "robotis_op3_description/urdf/robotis_op3.visuals.xacro"
]
```

## Self comparisons

```json
[
  {
    "file": "robotis_op3/op3.xml",
    "status": "passed",
    "findings": 0
  }
]
```

## Sensitivity

```json
{
  "0.5": {
    "provenance_method": "unknown",
    "counts": {
      "unknown": 20
    },
    "classifications_changed": 0,
    "finding_membership_changes": 0
  },
  "2": {
    "provenance_method": "unknown",
    "counts": {
      "unknown": 20
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
      "robotis_op3/op3.xml"
    ],
    "registration": {
      "translation": [
        0.0,
        0.0,
        0.3
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
      "cam_link",
      "cam_gazebo_link"
    ],
    "assets_loaded": 42,
    "mesh_conversions": [],
    "nonphysical_normalizations": [],
    "xacro_arguments": {},
    "source_dependencies": [
      "op3_description/urdf/robotis_op3.gazebo.xacro",
      "op3_description/urdf/robotis_op3.inertia.xacro",
      "op3_description/urdf/robotis_op3.structure.head.xacro",
      "op3_description/urdf/robotis_op3.structure.larm.xacro",
      "op3_description/urdf/robotis_op3.structure.lleg.xacro",
      "op3_description/urdf/robotis_op3.structure.rarm.xacro",
      "op3_description/urdf/robotis_op3.structure.rleg.xacro",
      "op3_description/urdf/robotis_op3.transmissions.xacro",
      "op3_description/urdf/robotis_op3.urdf.xacro",
      "op3_description/urdf/robotis_op3.visuals.xacro",
      "op3_description/meshes/body.stl",
      "op3_description/meshes/body.stl",
      "op3_description/meshes/ll1.stl",
      "op3_description/meshes/ll1.stl",
      "op3_description/meshes/ll2.stl",
      "op3_description/meshes/ll2.stl",
      "op3_description/meshes/ll3.stl",
      "op3_description/meshes/ll3.stl",
      "op3_description/meshes/ll4.stl",
      "op3_description/meshes/ll4.stl",
      "op3_description/meshes/ll5.stl",
      "op3_description/meshes/ll5.stl",
      "op3_description/meshes/ll6.stl",
      "op3_description/meshes/ll6.stl",
      "op3_description/meshes/rl1.stl",
      "op3_description/meshes/rl1.stl",
      "op3_description/meshes/rl2.stl",
      "op3_description/meshes/rl2.stl",
      "op3_description/meshes/rl3.stl",
      "op3_description/meshes/rl3.stl",
      "op3_description/meshes/rl4.stl",
      "op3_description/meshes/rl4.stl",
      "op3_description/meshes/rl5.stl",
      "op3_description/meshes/rl5.stl",
      "op3_description/meshes/rl6.stl",
      "op3_description/meshes/rl6.stl",
      "op3_description/meshes/la1.stl",
      "op3_description/meshes/la1.stl",
      "op3_description/meshes/la2.stl",
      "op3_description/meshes/la2.stl",
      "op3_description/meshes/la3.stl",
      "op3_description/meshes/la3.stl",
      "op3_description/meshes/ra1.stl",
      "op3_description/meshes/ra1.stl",
      "op3_description/meshes/ra2.stl",
      "op3_description/meshes/ra2.stl",
      "op3_description/meshes/ra3.stl",
      "op3_description/meshes/ra3.stl",
      "op3_description/meshes/h1.stl",
      "op3_description/meshes/h1.stl",
      "op3_description/meshes/h2.stl",
      "op3_description/meshes/h2.stl"
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
    "M"
  ],
  "self_variants_recompiled": 1,
  "historical_snapshots_reused": 11,
  "primary_physics_unchanged": true,
  "source_matching": "original raw-value provenance criteria retained; kinematic guard applies to reported CoM"
}
```
