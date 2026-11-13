# shadow_hand

Status: **partial history**. Provenance: **unknown**, confidence **incomplete**.

Unresolved historical compilation prevents selecting or rejecting a matching source. Pairwise M/H differences are reported with unknown provenance.

XML include fragments (checked through their parent models, not as standalone robots): `shadow_hand/keyframes.xml`

M: `https://github.com/google-deepmind/mujoco_menagerie`, `shadow_hand/right_hand.xml`, commit `370c43965323c0944b433b202aac5058b5f907a9`.
H: `https://github.com/shadow-robot/sr_common`, `sr_description/robots/sr_hand.urdf.xacro`, commit `172c3d9c3715ee75eb10dfe4ee57e26a342b4529`.
S: unavailable. A machine-readable H can still be compared to M; no-match differences are never counted as STALE.

Limit semantics: MJCF effort values are supported actuator torque/force envelopes. URDF effort and velocity values are manufacturer declarations retained from XML; MuJoCo does not enforce those tags. Such declaration comparisons are explicitly distinct from compiled inertial/range quantities.


## Source evidence

```json
[
  {
    "url": "https://github.com/shadow-robot/sr_common/commit/bda959328b7934176123af0cc0491c34ecaa23ce",
    "document": "git commit message",
    "commit": "e946426aaaa56f59e14ad24ed2c22a3b1a04f124",
    "current": false
  },
  {
    "url": "https://github.com/kevinzakka/obj2mjcf",
    "document": "shadow_hand/README.md",
    "commit": "370c43965323c0944b433b202aac5058b5f907a9",
    "current": true
  },
  {
    "url": "https://github.com/shadow-robot/sr_common/blob/noetic-devel/sr_description/hand/xacro/forearm/forearm_e.urdf.xacro",
    "document": "shadow_hand/README.md",
    "commit": "370c43965323c0944b433b202aac5058b5f907a9",
    "current": true
  },
  {
    "url": "https://github.com/shadow-robot/sr_common/tree/noetic-devel/sr_description/meshes/",
    "document": "shadow_hand/README.md",
    "commit": "370c43965323c0944b433b202aac5058b5f907a9",
    "current": true
  }
]
```


## README derivation evidence

Documentation labels are conservative: an automated documented label requires an explicit affected entity and quantity. Broader conversion notes are retained here for review.

> 6. Added forearm body and its corresponding inertial specs.

## Kinematics consistency

A proper Kabsch rigid transform aligns all matched zero-pose body origins. The maximum per-origin residual and signed hinge/slide axis angles determine whether CoM can be compared; RMS is also recorded. Fewer than three non-collinear origins give insufficient kinematic coverage. CoM records that fail either required M/H or M/S check are excluded from counts and largest discrepancies. Masses, principal moments and raw joint ranges remain unchanged; a flagged range still requires convention review.

| Pair | Status | Origins / rank | RMS / maximum mm | Disagreeing / checked axes |
|---|---|---:|---:|---:|
| M/H | consistent | 25 / 3 | 0.0358795836 / 0.0807232347 | 0 / 24 |

Exact fitted transforms, per-origin residuals, thresholds and axis vectors:

```json
{
  "M/H": {
    "status": "consistent",
    "matched_body_origins": 25,
    "position_threshold_m": 0.005,
    "axis_threshold_rad": 0.005,
    "residual_definition": "maximum Euclidean residual over matched body origins; Kabsch minimizes RMS, which is also recorded",
    "coordinate_frames": "each snapshot registered to its matched report anchor",
    "anchor_m": "rh_forearm",
    "anchor_other": "rh_forearm",
    "rotation_other_to_m": [
      [
        -6.805465379201898e-06,
        -0.9999999999746527,
        -2.0929912021138766e-06
      ],
      [
        0.9999999965201144,
        -6.805291329223593e-06,
        -8.314721428000433e-05
      ],
      [
        8.314720003469193e-05,
        -2.0935570503484435e-06,
        0.9999999965410803
      ]
    ],
    "translation_other_to_m": [
      7.456687610447182e-07,
      2.694343020669815e-05,
      -1.6816428154264873e-05
    ],
    "rms_residual_m": 3.58795836081648e-05,
    "max_residual_m": 8.07232347411734e-05,
    "fit_rank": 3,
    "axis_checks": [
      {
        "joint_m": "rh_WRJ2",
        "joint_other": "rh_WRJ2",
        "axis_m": [
          -1.0,
          -4.440892098500628e-16,
          -2.465190328815663e-32
        ],
        "axis_other_aligned": [
          -0.9999999999746525,
          -6.805291329223591e-06,
          -2.093557050348443e-06
        ],
        "angle_rad": 7.120040111788825e-06,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "rh_WRJ1",
        "joint_other": "rh_WRJ1",
        "axis_m": [
          2.465190328815663e-32,
          1.0,
          4.440892098500628e-16
        ],
        "axis_other_aligned": [
          -6.805465379201898e-06,
          0.9999999965201144,
          8.314720003469193e-05
        ],
        "angle_rad": 8.342524347407611e-05,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "rh_FFJ4",
        "joint_other": "rh_FFJ4",
        "axis_m": [
          1.0,
          4.440892098500628e-16,
          2.465190328815663e-32
        ],
        "axis_other_aligned": [
          0.9999999999746525,
          6.805291329223591e-06,
          2.093557050348443e-06
        ],
        "angle_rad": 7.120040111788825e-06,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "rh_FFJ3",
        "joint_other": "rh_FFJ3",
        "axis_m": [
          2.465190328815663e-32,
          1.0,
          4.440892098500628e-16
        ],
        "axis_other_aligned": [
          -6.805465379201898e-06,
          0.9999999965201144,
          8.314720003469193e-05
        ],
        "angle_rad": 8.342524347407611e-05,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "rh_FFJ2",
        "joint_other": "rh_FFJ2",
        "axis_m": [
          2.465190328815663e-32,
          1.0,
          4.440892098500628e-16
        ],
        "axis_other_aligned": [
          -6.805465379201898e-06,
          0.9999999965201144,
          8.314720003469193e-05
        ],
        "angle_rad": 8.342524347407611e-05,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "rh_FFJ1",
        "joint_other": "rh_FFJ1",
        "axis_m": [
          2.465190328815663e-32,
          1.0,
          4.440892098500628e-16
        ],
        "axis_other_aligned": [
          -6.805465379201898e-06,
          0.9999999965201144,
          8.314720003469193e-05
        ],
        "angle_rad": 8.342524347407611e-05,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "rh_MFJ4",
        "joint_other": "rh_MFJ4",
        "axis_m": [
          1.0,
          4.440892098500628e-16,
          2.465190328815663e-32
        ],
        "axis_other_aligned": [
          0.9999999999746525,
          6.805291329223591e-06,
          2.093557050348443e-06
        ],
        "angle_rad": 7.120040111788825e-06,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "rh_MFJ3",
        "joint_other": "rh_MFJ3",
        "axis_m": [
          2.465190328815663e-32,
          1.0,
          4.440892098500628e-16
        ],
        "axis_other_aligned": [
          -6.805465379201898e-06,
          0.9999999965201144,
          8.314720003469193e-05
        ],
        "angle_rad": 8.342524347407611e-05,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "rh_MFJ2",
        "joint_other": "rh_MFJ2",
        "axis_m": [
          2.465190328815663e-32,
          1.0,
          4.440892098500628e-16
        ],
        "axis_other_aligned": [
          -6.805465379201898e-06,
          0.9999999965201144,
          8.314720003469193e-05
        ],
        "angle_rad": 8.342524347407611e-05,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "rh_MFJ1",
        "joint_other": "rh_MFJ1",
        "axis_m": [
          2.465190328815663e-32,
          1.0,
          4.440892098500628e-16
        ],
        "axis_other_aligned": [
          -6.805465379201898e-06,
          0.9999999965201144,
          8.314720003469193e-05
        ],
        "angle_rad": 8.342524347407611e-05,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "rh_RFJ4",
        "joint_other": "rh_RFJ4",
        "axis_m": [
          -1.0,
          -4.440892098500628e-16,
          -2.465190328815663e-32
        ],
        "axis_other_aligned": [
          -0.9999999999746525,
          -6.805291329223591e-06,
          -2.093557050348443e-06
        ],
        "angle_rad": 7.120040111788825e-06,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "rh_RFJ3",
        "joint_other": "rh_RFJ3",
        "axis_m": [
          2.465190328815663e-32,
          1.0,
          4.440892098500628e-16
        ],
        "axis_other_aligned": [
          -6.805465379201898e-06,
          0.9999999965201144,
          8.314720003469193e-05
        ],
        "angle_rad": 8.342524347407611e-05,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "rh_RFJ2",
        "joint_other": "rh_RFJ2",
        "axis_m": [
          2.465190328815663e-32,
          1.0,
          4.440892098500628e-16
        ],
        "axis_other_aligned": [
          -6.805465379201898e-06,
          0.9999999965201144,
          8.314720003469193e-05
        ],
        "angle_rad": 8.342524347407611e-05,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "rh_RFJ1",
        "joint_other": "rh_RFJ1",
        "axis_m": [
          2.465190328815663e-32,
          1.0,
          4.440892098500628e-16
        ],
        "axis_other_aligned": [
          -6.805465379201898e-06,
          0.9999999965201144,
          8.314720003469193e-05
        ],
        "angle_rad": 8.342524347407611e-05,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "rh_LFJ5",
        "joint_other": "rh_LFJ5",
        "axis_m": [
          3.3306690738754706e-16,
          0.5735761643640092,
          0.8191522347362981
        ],
        "axis_other_aligned": [
          -5.618068587464623e-06,
          0.5735337916376149,
          0.819181902765325
        ],
        "angle_rad": 5.203078496138226e-05,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "rh_LFJ4",
        "joint_other": "rh_LFJ4",
        "axis_m": [
          -1.0,
          -4.440892098500628e-16,
          -2.465190328815663e-32
        ],
        "axis_other_aligned": [
          -0.9999999999746525,
          -6.805291329223591e-06,
          -2.093557050348443e-06
        ],
        "angle_rad": 7.120040111788825e-06,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "rh_LFJ3",
        "joint_other": "rh_LFJ3",
        "axis_m": [
          2.465190328815663e-32,
          1.0,
          4.440892098500628e-16
        ],
        "axis_other_aligned": [
          -6.805465379201898e-06,
          0.9999999965201144,
          8.314720003468438e-05
        ],
        "angle_rad": 8.342524347406858e-05,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "rh_LFJ2",
        "joint_other": "rh_LFJ2",
        "axis_m": [
          2.465190328815663e-32,
          1.0,
          4.440892098500628e-16
        ],
        "axis_other_aligned": [
          -6.805465379201898e-06,
          0.9999999965201144,
          8.314720003468438e-05
        ],
        "angle_rad": 8.342524347406858e-05,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "rh_LFJ1",
        "joint_other": "rh_LFJ1",
        "axis_m": [
          2.465190328815663e-32,
          1.0,
          4.440892098500628e-16
        ],
        "axis_other_aligned": [
          -6.805465379201898e-06,
          0.9999999965201144,
          8.314720003468438e-05
        ],
        "angle_rad": 8.342524347406858e-05,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "rh_THJ5",
        "joint_other": "rh_THJ5",
        "axis_m": [
          -4.440892098500628e-16,
          -0.7071059632710103,
          -0.7071075991011386
        ],
        "axis_other_aligned": [
          6.2921589908680895e-06,
          -0.7070479847668425,
          -0.7071655726897031
        ],
        "angle_rad": 8.223159481104973e-05,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "rh_THJ4",
        "joint_other": "rh_THJ4",
        "axis_m": [
          -8.04413302343329e-18,
          0.7071075991011389,
          -0.70710596327101
        ],
        "axis_other_aligned": [
          -3.332222447007479e-06,
          0.707165572684951,
          -0.7070479847917407
        ],
        "angle_rad": 8.205817563542553e-05,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "rh_THJ3",
        "joint_other": "rh_THJ3",
        "axis_m": [
          -8.04413302343329e-18,
          0.7071075991011389,
          -0.70710596327101
        ],
        "axis_other_aligned": [
          -3.332222447007479e-06,
          0.707165572684951,
          -0.7070479847917407
        ],
        "angle_rad": 8.205817563542553e-05,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "rh_THJ2",
        "joint_other": "rh_THJ2",
        "axis_m": [
          1.0,
          5.551115123125786e-16,
          -8.044133023433287e-18
        ],
        "axis_other_aligned": [
          0.9999999999746526,
          6.805291329556659e-06,
          2.093557050350866e-06
        ],
        "angle_rad": 7.120040112004131e-06,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "rh_THJ1",
        "joint_other": "rh_THJ1",
        "axis_m": [
          1.0,
          -1.0787707097189735e-17,
          6.661338147750943e-16
        ],
        "axis_other_aligned": [
          0.9999999999746526,
          6.805291329556659e-06,
          2.093557050350866e-06
        ],
        "angle_rad": 7.1200401123467815e-06,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      }
    ],
    "axis_disagreements": [],
    "com_eligible": true,
    "covariance_singular_values": [
      0.1800812047962056,
      0.025275199935477298,
      0.00023122623454764483
    ],
    "origin_residuals_m": {
      "rh_forearm": 3.1769430417808315e-05,
      "rh_wrist": 1.920152891005223e-05,
      "rh_palm": 1.800202892340842e-05,
      "rh_ffknuckle": 1.4126307031486154e-05,
      "rh_ffproximal": 1.4126307031486154e-05,
      "rh_ffmiddle": 1.4975711274475007e-05,
      "rh_ffdistal": 1.5814902327399415e-05,
      "rh_mfknuckle": 1.5979195948328917e-05,
      "rh_mfproximal": 1.5979195948328917e-05,
      "rh_mfmiddle": 1.6808221119475732e-05,
      "rh_mfdistal": 1.7598960268960113e-05,
      "rh_rfknuckle": 1.77688892272023e-05,
      "rh_rfproximal": 1.77688892272023e-05,
      "rh_rfmiddle": 1.8449834414654236e-05,
      "rh_rfdistal": 1.9136464073261886e-05,
      "rh_lfmetacarpal": 2.0113837768137207e-05,
      "rh_lfknuckle": 8.046098182839529e-05,
      "rh_lfproximal": 8.046098182839529e-05,
      "rh_lfmiddle": 8.05813952516373e-05,
      "rh_lfdistal": 8.07232347411734e-05,
      "rh_thbase": 1.4547323132851861e-05,
      "rh_thproximal": 1.4547323132851861e-05,
      "rh_thhub": 1.1907715008278777e-05,
      "rh_thmiddle": 1.1907715008278777e-05,
      "rh_thdistal": 9.906343361552039e-06
    },
    "reason": "Unique proper rigid fit and matched signed axes meet the configured thresholds"
  }
}
```


## Every reported quantity difference

Counts are quantity records, including correlated total/subtree/body mass records; they are not independent robot defects.

| Entity / quantity | M | S | H | H − M | Class | M source | S source | H source |
|---|---|---|---|---|---|---|---|---|
| rh_ffdistal / com_registered | [0.01, 0.033, 0.4250869] | unavailable | [0.00999963364, 0.0329917561, 0.423995947] | [-3.6636105e-07, -8.24388204e-06, -0.0010909531] | unknown | [CoM/kinematic input L147](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/shadow_hand/right_hand.xml#L147) | unavailable | [CoM/kinematic input L43](https://github.com/shadow-robot/sr_common/blob/172c3d9c3715ee75eb10dfe4ee57e26a342b4529/sr_description/hand/xacro/finger/distal/distal.urdf.xacro#L43) |
| rh_ffdistal / principal_moments | [5.3e-07, 1.12092e-06, 1.28092e-06] | unavailable | [5.3e-07, 9.4e-07, 1.1e-06] | [0, -1.8092e-07, -1.8092e-07] | unknown | [inertia input L147](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/shadow_hand/right_hand.xml#L147) | unavailable | [inertia input L44](https://github.com/shadow-robot/sr_common/blob/172c3d9c3715ee75eb10dfe4ee57e26a342b4529/sr_description/hand/xacro/finger/distal/distal.urdf.xacro#L44) |
| rh_mfdistal / com_registered | [0.01, 0.011, 0.4290869] | unavailable | [0.00999977499, 0.0109914236, 0.427994118] | [-2.25012776e-07, -8.57639434e-06, -0.00109278235] | unknown | [CoM/kinematic input L172](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/shadow_hand/right_hand.xml#L172) | unavailable | [CoM/kinematic input L43](https://github.com/shadow-robot/sr_common/blob/172c3d9c3715ee75eb10dfe4ee57e26a342b4529/sr_description/hand/xacro/finger/distal/distal.urdf.xacro#L43) |
| rh_mfdistal / principal_moments | [5.3e-07, 1.12092e-06, 1.28092e-06] | unavailable | [5.3e-07, 9.4e-07, 1.1e-06] | [0, -1.8092e-07, -1.8092e-07] | unknown | [inertia input L172](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/shadow_hand/right_hand.xml#L172) | unavailable | [inertia input L44](https://github.com/shadow-robot/sr_common/blob/172c3d9c3715ee75eb10dfe4ee57e26a342b4529/sr_description/hand/xacro/finger/distal/distal.urdf.xacro#L44) |
| rh_rfdistal / com_registered | [0.01, -0.011, 0.4250869] | unavailable | [0.00999993308, -0.0110082437, 0.423992288] | [-6.69205729e-08, -8.24372893e-06, -0.00109461158] | unknown | [CoM/kinematic input L197](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/shadow_hand/right_hand.xml#L197) | unavailable | [CoM/kinematic input L43](https://github.com/shadow-robot/sr_common/blob/172c3d9c3715ee75eb10dfe4ee57e26a342b4529/sr_description/hand/xacro/finger/distal/distal.urdf.xacro#L43) |
| rh_rfdistal / principal_moments | [5.3e-07, 1.12092e-06, 1.28092e-06] | unavailable | [5.3e-07, 9.4e-07, 1.1e-06] | [0, -1.8092e-07, -1.8092e-07] | unknown | [inertia input L197](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/shadow_hand/right_hand.xml#L197) | unavailable | [inertia input L44](https://github.com/shadow-robot/sr_common/blob/172c3d9c3715ee75eb10dfe4ee57e26a342b4529/sr_description/hand/xacro/finger/distal/distal.urdf.xacro#L44) |
| rh_lfmetacarpal / com_registered | [0.01, -0.033, 0.30772] | unavailable | [0.0100003293, -0.0330974347, 0.306528568] | [3.29319807e-07, -9.74346637e-05, -0.00119143197] | unknown | [CoM/kinematic input L206](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/shadow_hand/right_hand.xml#L206) | unavailable | [CoM/kinematic input L41](https://github.com/shadow-robot/sr_common/blob/172c3d9c3715ee75eb10dfe4ee57e26a342b4529/sr_description/hand/xacro/finger/lfmetacarpal/lfmetacarpal.urdf.xacro#L41) |
| rh_lfdistal / com_registered | [0.01, -0.033, 0.4165869] | unavailable | [0.0100001004, -0.0330075476, 0.415590457] | [1.00380813e-07, -7.54761058e-06, -0.000996443069] | unknown | [CoM/kinematic input L227](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/shadow_hand/right_hand.xml#L227) | unavailable | [CoM/kinematic input L43](https://github.com/shadow-robot/sr_common/blob/172c3d9c3715ee75eb10dfe4ee57e26a342b4529/sr_description/hand/xacro/finger/distal/distal.urdf.xacro#L43) |
| rh_lfdistal / principal_moments | [5.3e-07, 1.12092e-06, 1.28092e-06] | unavailable | [5.3e-07, 9.4e-07, 1.1e-06] | [0, -1.8092e-07, -1.8092e-07] | unknown | [inertia input L227](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/shadow_hand/right_hand.xml#L227) | unavailable | [inertia input L44](https://github.com/shadow-robot/sr_common/blob/172c3d9c3715ee75eb10dfe4ee57e26a342b4529/sr_description/hand/xacro/finger/distal/distal.urdf.xacro#L44) |
| rh_thdistal / mass | 0.017 | unavailable | 0.016 | -0.001 | unknown | [input L257](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/shadow_hand/right_hand.xml#L257) | unavailable | [input L42](https://github.com/shadow-robot/sr_common/blob/172c3d9c3715ee75eb10dfe4ee57e26a342b4529/sr_description/hand/xacro/finger/distal/distal.urdf.xacro#L42) |
| rh_thdistal / com_registered | [0.01858, 0.0937920317, 0.33580217] | unavailable | [0.0185794096, 0.093219389, 0.335221165] | [-5.9037235e-07, -0.000572642711, -0.000581004818] | unknown | [CoM/kinematic input L257](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/shadow_hand/right_hand.xml#L257) | unavailable | [CoM/kinematic input L43](https://github.com/shadow-robot/sr_common/blob/172c3d9c3715ee75eb10dfe4ee57e26a342b4529/sr_description/hand/xacro/finger/distal/distal.urdf.xacro#L43) |
| rh_thdistal / principal_moments | [1e-06, 2.27794e-06, 2.37794e-06] | unavailable | [1e-06, 2.1e-06, 2.2e-06] | [0, -1.7794e-07, -1.7794e-07] | unknown | [inertia input L257](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/shadow_hand/right_hand.xml#L257) | unavailable | [inertia input L44](https://github.com/shadow-robot/sr_common/blob/172c3d9c3715ee75eb10dfe4ee57e26a342b4529/sr_description/hand/xacro/finger/distal/distal.urdf.xacro#L44) |
| rh_WRJ1 / effort | 5 | unavailable | 30 | 25 | unknown | [inherited actuator input L20](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/shadow_hand/right_hand.xml#L20) | unavailable | [geometry/inference input L41](https://github.com/shadow-robot/sr_common/blob/172c3d9c3715ee75eb10dfe4ee57e26a342b4529/sr_description/hand/xacro/finger/distal/distal.transmission.xacro#L41) |
| rh_FFJ4 / effort | 1 | unavailable | 2 | 1 | unknown | [inherited actuator input L10](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/shadow_hand/right_hand.xml#L10) | unavailable | [geometry/inference input L40](https://github.com/shadow-robot/sr_common/blob/172c3d9c3715ee75eb10dfe4ee57e26a342b4529/sr_description/hand/xacro/finger/knuckle/knuckle.transmission.xacro#L40) |
| rh_FFJ3 / effort | 1 | unavailable | 2 | 1 | unknown | [inherited actuator input L10](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/shadow_hand/right_hand.xml#L10) | unavailable | [geometry/inference input L40](https://github.com/shadow-robot/sr_common/blob/172c3d9c3715ee75eb10dfe4ee57e26a342b4529/sr_description/hand/xacro/finger/proximal/proximal.transmission.xacro#L40) |
| rh_MFJ4 / effort | 1 | unavailable | 2 | 1 | unknown | [inherited actuator input L10](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/shadow_hand/right_hand.xml#L10) | unavailable | [geometry/inference input L40](https://github.com/shadow-robot/sr_common/blob/172c3d9c3715ee75eb10dfe4ee57e26a342b4529/sr_description/hand/xacro/finger/knuckle/knuckle.transmission.xacro#L40) |
| rh_MFJ3 / effort | 1 | unavailable | 2 | 1 | unknown | [inherited actuator input L10](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/shadow_hand/right_hand.xml#L10) | unavailable | [geometry/inference input L40](https://github.com/shadow-robot/sr_common/blob/172c3d9c3715ee75eb10dfe4ee57e26a342b4529/sr_description/hand/xacro/finger/proximal/proximal.transmission.xacro#L40) |
| rh_RFJ4 / effort | 1 | unavailable | 2 | 1 | unknown | [inherited actuator input L10](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/shadow_hand/right_hand.xml#L10) | unavailable | [geometry/inference input L40](https://github.com/shadow-robot/sr_common/blob/172c3d9c3715ee75eb10dfe4ee57e26a342b4529/sr_description/hand/xacro/finger/knuckle/knuckle.transmission.xacro#L40) |
| rh_RFJ3 / effort | 1 | unavailable | 2 | 1 | unknown | [inherited actuator input L10](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/shadow_hand/right_hand.xml#L10) | unavailable | [geometry/inference input L40](https://github.com/shadow-robot/sr_common/blob/172c3d9c3715ee75eb10dfe4ee57e26a342b4529/sr_description/hand/xacro/finger/proximal/proximal.transmission.xacro#L40) |
| rh_LFJ5 / effort | 1 | unavailable | 2 | 1 | unknown | [inherited actuator input L10](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/shadow_hand/right_hand.xml#L10) | unavailable | [geometry/inference input L40](https://github.com/shadow-robot/sr_common/blob/172c3d9c3715ee75eb10dfe4ee57e26a342b4529/sr_description/hand/xacro/finger/lfmetacarpal/lfmetacarpal.transmission.xacro#L40) |
| rh_LFJ4 / effort | 1 | unavailable | 2 | 1 | unknown | [inherited actuator input L10](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/shadow_hand/right_hand.xml#L10) | unavailable | [geometry/inference input L40](https://github.com/shadow-robot/sr_common/blob/172c3d9c3715ee75eb10dfe4ee57e26a342b4529/sr_description/hand/xacro/finger/knuckle/knuckle.transmission.xacro#L40) |
| rh_LFJ3 / effort | 1 | unavailable | 2 | 1 | unknown | [inherited actuator input L10](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/shadow_hand/right_hand.xml#L10) | unavailable | [geometry/inference input L40](https://github.com/shadow-robot/sr_common/blob/172c3d9c3715ee75eb10dfe4ee57e26a342b4529/sr_description/hand/xacro/finger/proximal/proximal.transmission.xacro#L40) |
| rh_THJ5 / effort | 3 | unavailable | 5 | 2 | unknown | [inherited actuator input L27](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/shadow_hand/right_hand.xml#L27) | unavailable | [geometry/inference input L40](https://github.com/shadow-robot/sr_common/blob/172c3d9c3715ee75eb10dfe4ee57e26a342b4529/sr_description/hand/xacro/thumb/thbase.transmission.xacro#L40) |
| rh_THJ4 / effort | 2 | unavailable | 3 | 1 | unknown | [inherited actuator input L31](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/shadow_hand/right_hand.xml#L31) | unavailable | [geometry/inference input L40](https://github.com/shadow-robot/sr_common/blob/172c3d9c3715ee75eb10dfe4ee57e26a342b4529/sr_description/hand/xacro/finger/knuckle/knuckle.transmission.xacro#L40) |
| rh_THJ3 / effort | 1 | unavailable | 2 | 1 | unknown | [inherited actuator input L10](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/shadow_hand/right_hand.xml#L10) | unavailable | [geometry/inference input L40](https://github.com/shadow-robot/sr_common/blob/172c3d9c3715ee75eb10dfe4ee57e26a342b4529/sr_description/hand/xacro/finger/proximal/proximal.transmission.xacro#L40) |
| rh_THJ2 / effort | 1 | unavailable | 2 | 1 | unknown | [inherited actuator input L10](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/shadow_hand/right_hand.xml#L10) | unavailable | [geometry/inference input L44](https://github.com/shadow-robot/sr_common/blob/172c3d9c3715ee75eb10dfe4ee57e26a342b4529/sr_description/hand/xacro/finger/middle/middle.transmission.xacro#L44) |

## Raw CoM records and reporting decisions

Raw values retain the previous root-anchor registration before Kabsch; original world coordinates also remain in the snapshots. Eligible findings above use the fitted transform into M. Excluded raw records below are diagnostic numbers, not findings. No CoM suppression applies to mass or principal inertia moments.

| Entity / quantity | Raw M | Raw S | Raw H | Raw H − M | Decision | M source | S source | H source |
|---|---|---|---|---|---|---|---|---|
| robot / total_com_registered | [0.00230083289, 0.00120977587, 0.136934933] | unavailable | [0.00120899417, -0.00230083289, 0.136927458] | [-0.00109183873, -0.00351060876, -7.47443549e-06] | eligible; compared after Kabsch alignment | [aggregate inputs](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/shadow_hand/right_hand.xml#L1) | unavailable | [aggregate inputs](https://github.com/shadow-robot/sr_common/blob/172c3d9c3715ee75eb10dfe4ee57e26a342b4529/sr_description/robots/sr_hand.urdf.xacro#L1) |
| rh_forearm / com_registered | [0, 0, 0.09] | unavailable | [0, 0, 0.09] | [0, 0, 6.9388939e-17] | eligible; compared after Kabsch alignment | [CoM/kinematic input L98](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/shadow_hand/right_hand.xml#L98) | unavailable | [CoM/kinematic input L47](https://github.com/shadow-robot/sr_common/blob/172c3d9c3715ee75eb10dfe4ee57e26a342b4529/sr_description/hand/xacro/forearm/forearm_e.urdf.xacro#L47) |
| rh_wrist / com_registered | [0.01, 0, 0.24201] | unavailable | [0, -0.01, 0.24201] | [-0.01, -0.01, 2.22044605e-16] | eligible; compared after Kabsch alignment | [CoM/kinematic input L105](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/shadow_hand/right_hand.xml#L105) | unavailable | [CoM/kinematic input L33](https://github.com/shadow-robot/sr_common/blob/172c3d9c3715ee75eb10dfe4ee57e26a342b4529/sr_description/hand/xacro/wrist/wrist.urdf.xacro#L33) |
| rh_palm / com_registered | [0.01, 0, 0.28201] | unavailable | [0, -0.01, 0.28201] | [-0.01, -0.01, 2.22044605e-16] | eligible; compared after Kabsch alignment | [CoM/kinematic input L116](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/shadow_hand/right_hand.xml#L116) | unavailable | [CoM/kinematic input L42](https://github.com/shadow-robot/sr_common/blob/172c3d9c3715ee75eb10dfe4ee57e26a342b4529/sr_description/hand/xacro/palm/palm_e.urdf.xacro#L42) |
| rh_ffknuckle / com_registered | [0.01, 0.033, 0.34201] | unavailable | [0.033, -0.01, 0.34201] | [0.023, -0.043, 3.33066907e-16] | eligible; compared after Kabsch alignment | [CoM/kinematic input L131](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/shadow_hand/right_hand.xml#L131) | unavailable | [CoM/kinematic input L41](https://github.com/shadow-robot/sr_common/blob/172c3d9c3715ee75eb10dfe4ee57e26a342b4529/sr_description/hand/xacro/finger/knuckle/knuckle.urdf.xacro#L41) |
| rh_ffproximal / com_registered | [0.01, 0.033, 0.36451] | unavailable | [0.033, -0.01, 0.36451] | [0.023, -0.043, 3.88578059e-16] | eligible; compared after Kabsch alignment | [CoM/kinematic input L136](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/shadow_hand/right_hand.xml#L136) | unavailable | [CoM/kinematic input L42](https://github.com/shadow-robot/sr_common/blob/172c3d9c3715ee75eb10dfe4ee57e26a342b4529/sr_description/hand/xacro/finger/proximal/proximal.urdf.xacro#L42) |
| rh_ffmiddle / com_registered | [0.01, 0.033, 0.39951] | unavailable | [0.033, -0.01, 0.39951] | [0.023, -0.043, 3.88578059e-16] | eligible; compared after Kabsch alignment | [CoM/kinematic input L141](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/shadow_hand/right_hand.xml#L141) | unavailable | [CoM/kinematic input L41](https://github.com/shadow-robot/sr_common/blob/172c3d9c3715ee75eb10dfe4ee57e26a342b4529/sr_description/hand/xacro/finger/middle/middle.urdf.xacro#L41) |
| rh_ffdistal / com_registered | [0.01, 0.033, 0.4250869] | unavailable | [0.033, -0.01, 0.42401] | [0.023, -0.043, -0.0010769] | eligible; compared after Kabsch alignment | [CoM/kinematic input L147](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/shadow_hand/right_hand.xml#L147) | unavailable | [CoM/kinematic input L43](https://github.com/shadow-robot/sr_common/blob/172c3d9c3715ee75eb10dfe4ee57e26a342b4529/sr_description/hand/xacro/finger/distal/distal.urdf.xacro#L43) |
| rh_mfknuckle / com_registered | [0.01, 0.011, 0.34601] | unavailable | [0.011, -0.01, 0.34601] | [0.001, -0.021, 3.33066907e-16] | eligible; compared after Kabsch alignment | [CoM/kinematic input L156](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/shadow_hand/right_hand.xml#L156) | unavailable | [CoM/kinematic input L41](https://github.com/shadow-robot/sr_common/blob/172c3d9c3715ee75eb10dfe4ee57e26a342b4529/sr_description/hand/xacro/finger/knuckle/knuckle.urdf.xacro#L41) |
| rh_mfproximal / com_registered | [0.01, 0.011, 0.36851] | unavailable | [0.011, -0.01, 0.36851] | [0.001, -0.021, 3.88578059e-16] | eligible; compared after Kabsch alignment | [CoM/kinematic input L161](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/shadow_hand/right_hand.xml#L161) | unavailable | [CoM/kinematic input L42](https://github.com/shadow-robot/sr_common/blob/172c3d9c3715ee75eb10dfe4ee57e26a342b4529/sr_description/hand/xacro/finger/proximal/proximal.urdf.xacro#L42) |
| rh_mfmiddle / com_registered | [0.01, 0.011, 0.40351] | unavailable | [0.011, -0.01, 0.40351] | [0.001, -0.021, 3.88578059e-16] | eligible; compared after Kabsch alignment | [CoM/kinematic input L166](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/shadow_hand/right_hand.xml#L166) | unavailable | [CoM/kinematic input L41](https://github.com/shadow-robot/sr_common/blob/172c3d9c3715ee75eb10dfe4ee57e26a342b4529/sr_description/hand/xacro/finger/middle/middle.urdf.xacro#L41) |
| rh_mfdistal / com_registered | [0.01, 0.011, 0.4290869] | unavailable | [0.011, -0.01, 0.42801] | [0.001, -0.021, -0.0010769] | eligible; compared after Kabsch alignment | [CoM/kinematic input L172](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/shadow_hand/right_hand.xml#L172) | unavailable | [CoM/kinematic input L43](https://github.com/shadow-robot/sr_common/blob/172c3d9c3715ee75eb10dfe4ee57e26a342b4529/sr_description/hand/xacro/finger/distal/distal.urdf.xacro#L43) |
| rh_rfknuckle / com_registered | [0.01, -0.011, 0.34201] | unavailable | [-0.011, -0.01, 0.34201] | [-0.021, 0.001, 3.33066907e-16] | eligible; compared after Kabsch alignment | [CoM/kinematic input L181](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/shadow_hand/right_hand.xml#L181) | unavailable | [CoM/kinematic input L41](https://github.com/shadow-robot/sr_common/blob/172c3d9c3715ee75eb10dfe4ee57e26a342b4529/sr_description/hand/xacro/finger/knuckle/knuckle.urdf.xacro#L41) |
| rh_rfproximal / com_registered | [0.01, -0.011, 0.36451] | unavailable | [-0.011, -0.01, 0.36451] | [-0.021, 0.001, 3.88578059e-16] | eligible; compared after Kabsch alignment | [CoM/kinematic input L186](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/shadow_hand/right_hand.xml#L186) | unavailable | [CoM/kinematic input L42](https://github.com/shadow-robot/sr_common/blob/172c3d9c3715ee75eb10dfe4ee57e26a342b4529/sr_description/hand/xacro/finger/proximal/proximal.urdf.xacro#L42) |
| rh_rfmiddle / com_registered | [0.01, -0.011, 0.39951] | unavailable | [-0.011, -0.01, 0.39951] | [-0.021, 0.001, 3.88578059e-16] | eligible; compared after Kabsch alignment | [CoM/kinematic input L191](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/shadow_hand/right_hand.xml#L191) | unavailable | [CoM/kinematic input L41](https://github.com/shadow-robot/sr_common/blob/172c3d9c3715ee75eb10dfe4ee57e26a342b4529/sr_description/hand/xacro/finger/middle/middle.urdf.xacro#L41) |
| rh_rfdistal / com_registered | [0.01, -0.011, 0.4250869] | unavailable | [-0.011, -0.01, 0.42401] | [-0.021, 0.001, -0.0010769] | eligible; compared after Kabsch alignment | [CoM/kinematic input L197](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/shadow_hand/right_hand.xml#L197) | unavailable | [CoM/kinematic input L43](https://github.com/shadow-robot/sr_common/blob/172c3d9c3715ee75eb10dfe4ee57e26a342b4529/sr_description/hand/xacro/finger/distal/distal.urdf.xacro#L43) |
| rh_lfmetacarpal / com_registered | [0.01, -0.033, 0.30772] | unavailable | [-0.0330989576, -0.01, 0.306548117] | [-0.0430989576, 0.023, -0.00117188333] | eligible; compared after Kabsch alignment | [CoM/kinematic input L206](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/shadow_hand/right_hand.xml#L206) | unavailable | [CoM/kinematic input L41](https://github.com/shadow-robot/sr_common/blob/172c3d9c3715ee75eb10dfe4ee57e26a342b4529/sr_description/hand/xacro/finger/lfmetacarpal/lfmetacarpal.urdf.xacro#L41) |
| rh_lfknuckle / com_registered | [0.01, -0.033, 0.33351] | unavailable | [-0.0330000024, -0.01, 0.333609998] | [-0.0430000024, 0.023, 9.99977189e-05] | eligible; compared after Kabsch alignment | [CoM/kinematic input L211](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/shadow_hand/right_hand.xml#L211) | unavailable | [CoM/kinematic input L41](https://github.com/shadow-robot/sr_common/blob/172c3d9c3715ee75eb10dfe4ee57e26a342b4529/sr_description/hand/xacro/finger/knuckle/knuckle.urdf.xacro#L41) |
| rh_lfproximal / com_registered | [0.01, -0.033, 0.35601] | unavailable | [-0.0330000024, -0.01, 0.356109998] | [-0.0430000024, 0.023, 9.99977189e-05] | eligible; compared after Kabsch alignment | [CoM/kinematic input L216](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/shadow_hand/right_hand.xml#L216) | unavailable | [CoM/kinematic input L42](https://github.com/shadow-robot/sr_common/blob/172c3d9c3715ee75eb10dfe4ee57e26a342b4529/sr_description/hand/xacro/finger/proximal/proximal.urdf.xacro#L42) |
| rh_lfmiddle / com_registered | [0.01, -0.033, 0.39101] | unavailable | [-0.0330000024, -0.01, 0.391109998] | [-0.0430000024, 0.023, 9.99977189e-05] | eligible; compared after Kabsch alignment | [CoM/kinematic input L221](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/shadow_hand/right_hand.xml#L221) | unavailable | [CoM/kinematic input L41](https://github.com/shadow-robot/sr_common/blob/172c3d9c3715ee75eb10dfe4ee57e26a342b4529/sr_description/hand/xacro/finger/middle/middle.urdf.xacro#L41) |
| rh_lfdistal / com_registered | [0.01, -0.033, 0.4165869] | unavailable | [-0.0330000024, -0.01, 0.415609998] | [-0.0430000024, 0.023, -0.000976902281] | eligible; compared after Kabsch alignment | [CoM/kinematic input L227](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/shadow_hand/right_hand.xml#L227) | unavailable | [CoM/kinematic input L43](https://github.com/shadow-robot/sr_common/blob/172c3d9c3715ee75eb10dfe4ee57e26a342b4529/sr_description/hand/xacro/finger/distal/distal.urdf.xacro#L43) |
| rh_thbase / com_registered | [0.01858, 0.034, 0.27601] | unavailable | [0.034, -0.01858, 0.27601] | [0.01542, -0.05258, 2.77555756e-16] | eligible; compared after Kabsch alignment | [CoM/kinematic input L237](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/shadow_hand/right_hand.xml#L237) | unavailable | [CoM/kinematic input L42](https://github.com/shadow-robot/sr_common/blob/172c3d9c3715ee75eb10dfe4ee57e26a342b4529/sr_description/hand/xacro/thumb/thbase.urdf.xacro#L42) |
| rh_thproximal / com_registered | [0.01858, 0.0474350133, 0.289445044] | unavailable | [0.0474350288, -0.01858, 0.289445029] | [0.0288550288, -0.0660150133, -1.5540377e-08] | eligible; compared after Kabsch alignment | [CoM/kinematic input L241](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/shadow_hand/right_hand.xml#L241) | unavailable | [CoM/kinematic input L42](https://github.com/shadow-robot/sr_common/blob/172c3d9c3715ee75eb10dfe4ee57e26a342b4529/sr_description/hand/xacro/finger/proximal/proximal.urdf.xacro#L42) |
| rh_thhub / com_registered | [0.01858, 0.0608700266, 0.302880089] | unavailable | [0.0608700577, -0.01858, 0.302880058] | [0.0422900577, -0.0794500266, -3.10807541e-08] | eligible; compared after Kabsch alignment | [CoM/kinematic input L246](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/shadow_hand/right_hand.xml#L246) | unavailable | [CoM/kinematic input L42](https://github.com/shadow-robot/sr_common/blob/172c3d9c3715ee75eb10dfe4ee57e26a342b4529/sr_description/hand/xacro/thumb/thhub.urdf.xacro#L42) |
| rh_thmiddle / com_registered | [0.01858, 0.072183722, 0.31419381] | unavailable | [0.0721837662, -0.01858, 0.314193766] | [0.0536037662, -0.090763722, -4.41673875e-08] | eligible; compared after Kabsch alignment | [CoM/kinematic input L250](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/shadow_hand/right_hand.xml#L250) | unavailable | [CoM/kinematic input L41](https://github.com/shadow-robot/sr_common/blob/172c3d9c3715ee75eb10dfe4ee57e26a342b4529/sr_description/hand/xacro/finger/middle/middle.urdf.xacro#L41) |
| rh_thdistal / com_registered | [0.01858, 0.0937920317, 0.33580217] | unavailable | [0.0932201929, -0.01858, 0.335230193] | [0.0746401929, -0.112372032, -0.000571977126] | eligible; compared after Kabsch alignment | [CoM/kinematic input L257](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/shadow_hand/right_hand.xml#L257) | unavailable | [CoM/kinematic input L43](https://github.com/shadow-robot/sr_common/blob/172c3d9c3715ee75eb10dfe4ee57e26a342b4529/sr_description/hand/xacro/finger/distal/distal.urdf.xacro#L43) |

## Mass accounting

Every contributing compiled body mass is listed here so total/subtree sums can be checked. Links point to explicit inertials or to geometry inputs when the compiler inferred a mass. CoM links identify inertial inputs; world coordinates additionally use the ancestor transforms and the registration recorded below.

| M body | M kg / source | S kg / source | H kg / source |
|---|---|---|---|
| rh_forearm | 3 / [input L98](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/shadow_hand/right_hand.xml#L98) | unavailable | 3 / [input L48](https://github.com/shadow-robot/sr_common/blob/172c3d9c3715ee75eb10dfe4ee57e26a342b4529/sr_description/hand/xacro/forearm/forearm_e.urdf.xacro#L48) |
| rh_wrist | 0.1 / [input L105](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/shadow_hand/right_hand.xml#L105) | unavailable | 0.1 / [input L34](https://github.com/shadow-robot/sr_common/blob/172c3d9c3715ee75eb10dfe4ee57e26a342b4529/sr_description/hand/xacro/wrist/wrist.urdf.xacro#L34) |
| rh_palm | 0.3 / [input L116](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/shadow_hand/right_hand.xml#L116) | unavailable | 0.3 / [input L43](https://github.com/shadow-robot/sr_common/blob/172c3d9c3715ee75eb10dfe4ee57e26a342b4529/sr_description/hand/xacro/palm/palm_e.urdf.xacro#L43) |
| rh_ffknuckle | 0.008 / [input L131](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/shadow_hand/right_hand.xml#L131) | unavailable | 0.008 / [input L42](https://github.com/shadow-robot/sr_common/blob/172c3d9c3715ee75eb10dfe4ee57e26a342b4529/sr_description/hand/xacro/finger/knuckle/knuckle.urdf.xacro#L42) |
| rh_ffproximal | 0.03 / [input L136](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/shadow_hand/right_hand.xml#L136) | unavailable | 0.03 / [input L41](https://github.com/shadow-robot/sr_common/blob/172c3d9c3715ee75eb10dfe4ee57e26a342b4529/sr_description/hand/xacro/finger/proximal/proximal.urdf.xacro#L41) |
| rh_ffmiddle | 0.017 / [input L141](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/shadow_hand/right_hand.xml#L141) | unavailable | 0.017 / [input L42](https://github.com/shadow-robot/sr_common/blob/172c3d9c3715ee75eb10dfe4ee57e26a342b4529/sr_description/hand/xacro/finger/middle/middle.urdf.xacro#L42) |
| rh_ffdistal | 0.013 / [input L147](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/shadow_hand/right_hand.xml#L147) | unavailable | 0.012 / [input L42](https://github.com/shadow-robot/sr_common/blob/172c3d9c3715ee75eb10dfe4ee57e26a342b4529/sr_description/hand/xacro/finger/distal/distal.urdf.xacro#L42) |
| rh_mfknuckle | 0.008 / [input L156](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/shadow_hand/right_hand.xml#L156) | unavailable | 0.008 / [input L42](https://github.com/shadow-robot/sr_common/blob/172c3d9c3715ee75eb10dfe4ee57e26a342b4529/sr_description/hand/xacro/finger/knuckle/knuckle.urdf.xacro#L42) |
| rh_mfproximal | 0.03 / [input L161](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/shadow_hand/right_hand.xml#L161) | unavailable | 0.03 / [input L41](https://github.com/shadow-robot/sr_common/blob/172c3d9c3715ee75eb10dfe4ee57e26a342b4529/sr_description/hand/xacro/finger/proximal/proximal.urdf.xacro#L41) |
| rh_mfmiddle | 0.017 / [input L166](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/shadow_hand/right_hand.xml#L166) | unavailable | 0.017 / [input L42](https://github.com/shadow-robot/sr_common/blob/172c3d9c3715ee75eb10dfe4ee57e26a342b4529/sr_description/hand/xacro/finger/middle/middle.urdf.xacro#L42) |
| rh_mfdistal | 0.013 / [input L172](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/shadow_hand/right_hand.xml#L172) | unavailable | 0.012 / [input L42](https://github.com/shadow-robot/sr_common/blob/172c3d9c3715ee75eb10dfe4ee57e26a342b4529/sr_description/hand/xacro/finger/distal/distal.urdf.xacro#L42) |
| rh_rfknuckle | 0.008 / [input L181](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/shadow_hand/right_hand.xml#L181) | unavailable | 0.008 / [input L42](https://github.com/shadow-robot/sr_common/blob/172c3d9c3715ee75eb10dfe4ee57e26a342b4529/sr_description/hand/xacro/finger/knuckle/knuckle.urdf.xacro#L42) |
| rh_rfproximal | 0.03 / [input L186](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/shadow_hand/right_hand.xml#L186) | unavailable | 0.03 / [input L41](https://github.com/shadow-robot/sr_common/blob/172c3d9c3715ee75eb10dfe4ee57e26a342b4529/sr_description/hand/xacro/finger/proximal/proximal.urdf.xacro#L41) |
| rh_rfmiddle | 0.017 / [input L191](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/shadow_hand/right_hand.xml#L191) | unavailable | 0.017 / [input L42](https://github.com/shadow-robot/sr_common/blob/172c3d9c3715ee75eb10dfe4ee57e26a342b4529/sr_description/hand/xacro/finger/middle/middle.urdf.xacro#L42) |
| rh_rfdistal | 0.013 / [input L197](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/shadow_hand/right_hand.xml#L197) | unavailable | 0.012 / [input L42](https://github.com/shadow-robot/sr_common/blob/172c3d9c3715ee75eb10dfe4ee57e26a342b4529/sr_description/hand/xacro/finger/distal/distal.urdf.xacro#L42) |
| rh_lfmetacarpal | 0.03 / [input L206](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/shadow_hand/right_hand.xml#L206) | unavailable | 0.03 / [input L42](https://github.com/shadow-robot/sr_common/blob/172c3d9c3715ee75eb10dfe4ee57e26a342b4529/sr_description/hand/xacro/finger/lfmetacarpal/lfmetacarpal.urdf.xacro#L42) |
| rh_lfknuckle | 0.008 / [input L211](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/shadow_hand/right_hand.xml#L211) | unavailable | 0.008 / [input L42](https://github.com/shadow-robot/sr_common/blob/172c3d9c3715ee75eb10dfe4ee57e26a342b4529/sr_description/hand/xacro/finger/knuckle/knuckle.urdf.xacro#L42) |
| rh_lfproximal | 0.03 / [input L216](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/shadow_hand/right_hand.xml#L216) | unavailable | 0.03 / [input L41](https://github.com/shadow-robot/sr_common/blob/172c3d9c3715ee75eb10dfe4ee57e26a342b4529/sr_description/hand/xacro/finger/proximal/proximal.urdf.xacro#L41) |
| rh_lfmiddle | 0.017 / [input L221](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/shadow_hand/right_hand.xml#L221) | unavailable | 0.017 / [input L42](https://github.com/shadow-robot/sr_common/blob/172c3d9c3715ee75eb10dfe4ee57e26a342b4529/sr_description/hand/xacro/finger/middle/middle.urdf.xacro#L42) |
| rh_lfdistal | 0.013 / [input L227](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/shadow_hand/right_hand.xml#L227) | unavailable | 0.012 / [input L42](https://github.com/shadow-robot/sr_common/blob/172c3d9c3715ee75eb10dfe4ee57e26a342b4529/sr_description/hand/xacro/finger/distal/distal.urdf.xacro#L42) |
| rh_thbase | 0.01 / [input L237](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/shadow_hand/right_hand.xml#L237) | unavailable | 0.01 / [input L41](https://github.com/shadow-robot/sr_common/blob/172c3d9c3715ee75eb10dfe4ee57e26a342b4529/sr_description/hand/xacro/thumb/thbase.urdf.xacro#L41) |
| rh_thproximal | 0.04 / [input L241](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/shadow_hand/right_hand.xml#L241) | unavailable | 0.04 / [input L41](https://github.com/shadow-robot/sr_common/blob/172c3d9c3715ee75eb10dfe4ee57e26a342b4529/sr_description/hand/xacro/finger/proximal/proximal.urdf.xacro#L41) |
| rh_thhub | 0.005 / [input L246](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/shadow_hand/right_hand.xml#L246) | unavailable | 0.005 / [input L41](https://github.com/shadow-robot/sr_common/blob/172c3d9c3715ee75eb10dfe4ee57e26a342b4529/sr_description/hand/xacro/thumb/thhub.urdf.xacro#L41) |
| rh_thmiddle | 0.02 / [input L250](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/shadow_hand/right_hand.xml#L250) | unavailable | 0.02 / [input L42](https://github.com/shadow-robot/sr_common/blob/172c3d9c3715ee75eb10dfe4ee57e26a342b4529/sr_description/hand/xacro/finger/middle/middle.urdf.xacro#L42) |
| rh_thdistal | 0.017 / [input L257](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/shadow_hand/right_hand.xml#L257) | unavailable | 0.016 / [input L42](https://github.com/shadow-robot/sr_common/blob/172c3d9c3715ee75eb10dfe4ee57e26a342b4529/sr_description/hand/xacro/finger/distal/distal.urdf.xacro#L42) |
| upstream-only rh_fftip | unavailable | unavailable | 0.001 / [input L103](https://github.com/shadow-robot/sr_common/blob/172c3d9c3715ee75eb10dfe4ee57e26a342b4529/sr_description/hand/xacro/finger/distal/distal.urdf.xacro#L103) |
| upstream-only rh_imu | unavailable | unavailable | 0 / [geometry/inference input L29](https://github.com/shadow-robot/sr_common/blob/172c3d9c3715ee75eb10dfe4ee57e26a342b4529/sr_description/hand/xacro/palm/imu.urdf.xacro#L29) |
| upstream-only rh_lftip | unavailable | unavailable | 0.001 / [input L103](https://github.com/shadow-robot/sr_common/blob/172c3d9c3715ee75eb10dfe4ee57e26a342b4529/sr_description/hand/xacro/finger/distal/distal.urdf.xacro#L103) |
| upstream-only rh_manipulator | unavailable | unavailable | 0 / [geometry/inference input L113](https://github.com/shadow-robot/sr_common/blob/172c3d9c3715ee75eb10dfe4ee57e26a342b4529/sr_description/hand/xacro/palm/palm_e.urdf.xacro#L113) |
| upstream-only rh_mftip | unavailable | unavailable | 0.001 / [input L103](https://github.com/shadow-robot/sr_common/blob/172c3d9c3715ee75eb10dfe4ee57e26a342b4529/sr_description/hand/xacro/finger/distal/distal.urdf.xacro#L103) |
| upstream-only rh_rftip | unavailable | unavailable | 0.001 / [input L103](https://github.com/shadow-robot/sr_common/blob/172c3d9c3715ee75eb10dfe4ee57e26a342b4529/sr_description/hand/xacro/finger/distal/distal.urdf.xacro#L103) |
| upstream-only rh_thtip | unavailable | unavailable | 0.001 / [input L103](https://github.com/shadow-robot/sr_common/blob/172c3d9c3715ee75eb10dfe4ee57e26a342b4529/sr_description/hand/xacro/finger/distal/distal.urdf.xacro#L103) |

## Coverage and unmatched elements

```json
{
  "mapping_h": {
    "bodies": {
      "rh_forearm": "rh_forearm",
      "rh_wrist": "rh_wrist",
      "rh_palm": "rh_palm",
      "rh_ffknuckle": "rh_ffknuckle",
      "rh_ffproximal": "rh_ffproximal",
      "rh_ffmiddle": "rh_ffmiddle",
      "rh_ffdistal": "rh_ffdistal",
      "rh_mfknuckle": "rh_mfknuckle",
      "rh_mfproximal": "rh_mfproximal",
      "rh_mfmiddle": "rh_mfmiddle",
      "rh_mfdistal": "rh_mfdistal",
      "rh_rfknuckle": "rh_rfknuckle",
      "rh_rfproximal": "rh_rfproximal",
      "rh_rfmiddle": "rh_rfmiddle",
      "rh_rfdistal": "rh_rfdistal",
      "rh_lfmetacarpal": "rh_lfmetacarpal",
      "rh_lfknuckle": "rh_lfknuckle",
      "rh_lfproximal": "rh_lfproximal",
      "rh_lfmiddle": "rh_lfmiddle",
      "rh_lfdistal": "rh_lfdistal",
      "rh_thbase": "rh_thbase",
      "rh_thproximal": "rh_thproximal",
      "rh_thhub": "rh_thhub",
      "rh_thmiddle": "rh_thmiddle",
      "rh_thdistal": "rh_thdistal"
    },
    "joints": {
      "rh_WRJ2": "rh_WRJ2",
      "rh_WRJ1": "rh_WRJ1",
      "rh_FFJ4": "rh_FFJ4",
      "rh_FFJ3": "rh_FFJ3",
      "rh_FFJ2": "rh_FFJ2",
      "rh_FFJ1": "rh_FFJ1",
      "rh_MFJ4": "rh_MFJ4",
      "rh_MFJ3": "rh_MFJ3",
      "rh_MFJ2": "rh_MFJ2",
      "rh_MFJ1": "rh_MFJ1",
      "rh_RFJ4": "rh_RFJ4",
      "rh_RFJ3": "rh_RFJ3",
      "rh_RFJ2": "rh_RFJ2",
      "rh_RFJ1": "rh_RFJ1",
      "rh_LFJ5": "rh_LFJ5",
      "rh_LFJ4": "rh_LFJ4",
      "rh_LFJ3": "rh_LFJ3",
      "rh_LFJ2": "rh_LFJ2",
      "rh_LFJ1": "rh_LFJ1",
      "rh_THJ5": "rh_THJ5",
      "rh_THJ4": "rh_THJ4",
      "rh_THJ3": "rh_THJ3",
      "rh_THJ2": "rh_THJ2",
      "rh_THJ1": "rh_THJ1"
    },
    "body_methods": {
      "rh_forearm": "name",
      "rh_wrist": "name",
      "rh_palm": "name",
      "rh_ffknuckle": "name",
      "rh_ffproximal": "name",
      "rh_ffmiddle": "name",
      "rh_ffdistal": "name",
      "rh_mfknuckle": "name",
      "rh_mfproximal": "name",
      "rh_mfmiddle": "name",
      "rh_mfdistal": "name",
      "rh_rfknuckle": "name",
      "rh_rfproximal": "name",
      "rh_rfmiddle": "name",
      "rh_rfdistal": "name",
      "rh_lfmetacarpal": "name",
      "rh_lfknuckle": "name",
      "rh_lfproximal": "name",
      "rh_lfmiddle": "name",
      "rh_lfdistal": "name",
      "rh_thbase": "name",
      "rh_thproximal": "name",
      "rh_thhub": "name",
      "rh_thmiddle": "name",
      "rh_thdistal": "name"
    },
    "joint_methods": {
      "rh_WRJ2": "name",
      "rh_WRJ1": "name",
      "rh_FFJ4": "name",
      "rh_FFJ3": "name",
      "rh_FFJ2": "name",
      "rh_FFJ1": "name",
      "rh_MFJ4": "name",
      "rh_MFJ3": "name",
      "rh_MFJ2": "name",
      "rh_MFJ1": "name",
      "rh_RFJ4": "name",
      "rh_RFJ3": "name",
      "rh_RFJ2": "name",
      "rh_RFJ1": "name",
      "rh_LFJ5": "name",
      "rh_LFJ4": "name",
      "rh_LFJ3": "name",
      "rh_LFJ2": "name",
      "rh_LFJ1": "name",
      "rh_THJ5": "name",
      "rh_THJ4": "name",
      "rh_THJ3": "name",
      "rh_THJ2": "name",
      "rh_THJ1": "name"
    },
    "unmatched_m_bodies": [],
    "unmatched_upstream_bodies": [
      "rh_fftip",
      "rh_imu",
      "rh_lftip",
      "rh_manipulator",
      "rh_mftip",
      "rh_rftip",
      "rh_thtip"
    ],
    "unmatched_m_joints": [],
    "unmatched_upstream_joints": [],
    "registration_anchor": {
      "M": "rh_forearm",
      "H": "rh_forearm",
      "root_unmatched": false
    }
  },
  "mapping_s": null,
  "unavailable": [
    {
      "entity": "rh_WRJ2",
      "other_entity": "rh_WRJ2",
      "quantity": "force",
      "tolerance": "limit",
      "m": 10.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "rh_WRJ2",
      "other_entity": "rh_WRJ2",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 2.0,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "rh_WRJ1",
      "other_entity": "rh_WRJ1",
      "quantity": "force",
      "tolerance": "limit",
      "m": 5.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "rh_WRJ1",
      "other_entity": "rh_WRJ1",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 2.0,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "rh_FFJ4",
      "other_entity": "rh_FFJ4",
      "quantity": "force",
      "tolerance": "limit",
      "m": 1.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "rh_FFJ4",
      "other_entity": "rh_FFJ4",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 2.0,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "rh_FFJ3",
      "other_entity": "rh_FFJ3",
      "quantity": "force",
      "tolerance": "limit",
      "m": 1.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "rh_FFJ3",
      "other_entity": "rh_FFJ3",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 2.0,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "rh_FFJ2",
      "other_entity": "rh_FFJ2",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": 2.0,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "rh_FFJ2",
      "other_entity": "rh_FFJ2",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "rh_FFJ2",
      "other_entity": "rh_FFJ2",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 2.0,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "rh_FFJ1",
      "other_entity": "rh_FFJ1",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": 2.0,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "rh_FFJ1",
      "other_entity": "rh_FFJ1",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "rh_FFJ1",
      "other_entity": "rh_FFJ1",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 2.0,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "rh_MFJ4",
      "other_entity": "rh_MFJ4",
      "quantity": "force",
      "tolerance": "limit",
      "m": 1.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "rh_MFJ4",
      "other_entity": "rh_MFJ4",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 2.0,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "rh_MFJ3",
      "other_entity": "rh_MFJ3",
      "quantity": "force",
      "tolerance": "limit",
      "m": 1.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "rh_MFJ3",
      "other_entity": "rh_MFJ3",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 2.0,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "rh_MFJ2",
      "other_entity": "rh_MFJ2",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": 2.0,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "rh_MFJ2",
      "other_entity": "rh_MFJ2",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "rh_MFJ2",
      "other_entity": "rh_MFJ2",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 2.0,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "rh_MFJ1",
      "other_entity": "rh_MFJ1",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": 2.0,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "rh_MFJ1",
      "other_entity": "rh_MFJ1",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "rh_MFJ1",
      "other_entity": "rh_MFJ1",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 2.0,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "rh_RFJ4",
      "other_entity": "rh_RFJ4",
      "quantity": "force",
      "tolerance": "limit",
      "m": 1.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "rh_RFJ4",
      "other_entity": "rh_RFJ4",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 2.0,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "rh_RFJ3",
      "other_entity": "rh_RFJ3",
      "quantity": "force",
      "tolerance": "limit",
      "m": 1.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "rh_RFJ3",
      "other_entity": "rh_RFJ3",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 2.0,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "rh_RFJ2",
      "other_entity": "rh_RFJ2",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": 2.0,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "rh_RFJ2",
      "other_entity": "rh_RFJ2",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "rh_RFJ2",
      "other_entity": "rh_RFJ2",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 2.0,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "rh_RFJ1",
      "other_entity": "rh_RFJ1",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": 2.0,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "rh_RFJ1",
      "other_entity": "rh_RFJ1",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "rh_RFJ1",
      "other_entity": "rh_RFJ1",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 2.0,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "rh_LFJ5",
      "other_entity": "rh_LFJ5",
      "quantity": "force",
      "tolerance": "limit",
      "m": 1.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "rh_LFJ5",
      "other_entity": "rh_LFJ5",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 2.0,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "rh_LFJ4",
      "other_entity": "rh_LFJ4",
      "quantity": "force",
      "tolerance": "limit",
      "m": 1.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "rh_LFJ4",
      "other_entity": "rh_LFJ4",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 2.0,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "rh_LFJ3",
      "other_entity": "rh_LFJ3",
      "quantity": "force",
      "tolerance": "limit",
      "m": 1.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "rh_LFJ3",
      "other_entity": "rh_LFJ3",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 2.0,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "rh_LFJ2",
      "other_entity": "rh_LFJ2",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": 2.0,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "rh_LFJ2",
      "other_entity": "rh_LFJ2",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "rh_LFJ2",
      "other_entity": "rh_LFJ2",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 2.0,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "rh_LFJ1",
      "other_entity": "rh_LFJ1",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": 2.0,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "rh_LFJ1",
      "other_entity": "rh_LFJ1",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "rh_LFJ1",
      "other_entity": "rh_LFJ1",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 2.0,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "rh_THJ5",
      "other_entity": "rh_THJ5",
      "quantity": "force",
      "tolerance": "limit",
      "m": 3.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "rh_THJ5",
      "other_entity": "rh_THJ5",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 4.0,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "rh_THJ4",
      "other_entity": "rh_THJ4",
      "quantity": "force",
      "tolerance": "limit",
      "m": 2.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "rh_THJ4",
      "other_entity": "rh_THJ4",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 4.0,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "rh_THJ3",
      "other_entity": "rh_THJ3",
      "quantity": "force",
      "tolerance": "limit",
      "m": 1.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "rh_THJ3",
      "other_entity": "rh_THJ3",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 4.0,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "rh_THJ2",
      "other_entity": "rh_THJ2",
      "quantity": "force",
      "tolerance": "limit",
      "m": 1.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "rh_THJ2",
      "other_entity": "rh_THJ2",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 2.0,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "rh_THJ1",
      "other_entity": "rh_THJ1",
      "quantity": "force",
      "tolerance": "limit",
      "m": 1.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "rh_THJ1",
      "other_entity": "rh_THJ1",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 4.0,
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
| rh_WRJ2 / force | 10 | unavailable | unavailable |
| rh_WRJ2 / velocity | unavailable | unavailable | 2 |
| rh_WRJ1 / force | 5 | unavailable | unavailable |
| rh_WRJ1 / velocity | unavailable | unavailable | 2 |
| rh_FFJ4 / force | 1 | unavailable | unavailable |
| rh_FFJ4 / velocity | unavailable | unavailable | 2 |
| rh_FFJ3 / force | 1 | unavailable | unavailable |
| rh_FFJ3 / velocity | unavailable | unavailable | 2 |
| rh_FFJ2 / effort | unavailable | unavailable | 2 |
| rh_FFJ2 / force | unavailable | unavailable | unavailable |
| rh_FFJ2 / velocity | unavailable | unavailable | 2 |
| rh_FFJ1 / effort | unavailable | unavailable | 2 |
| rh_FFJ1 / force | unavailable | unavailable | unavailable |
| rh_FFJ1 / velocity | unavailable | unavailable | 2 |
| rh_MFJ4 / force | 1 | unavailable | unavailable |
| rh_MFJ4 / velocity | unavailable | unavailable | 2 |
| rh_MFJ3 / force | 1 | unavailable | unavailable |
| rh_MFJ3 / velocity | unavailable | unavailable | 2 |
| rh_MFJ2 / effort | unavailable | unavailable | 2 |
| rh_MFJ2 / force | unavailable | unavailable | unavailable |
| rh_MFJ2 / velocity | unavailable | unavailable | 2 |
| rh_MFJ1 / effort | unavailable | unavailable | 2 |
| rh_MFJ1 / force | unavailable | unavailable | unavailable |
| rh_MFJ1 / velocity | unavailable | unavailable | 2 |
| rh_RFJ4 / force | 1 | unavailable | unavailable |
| rh_RFJ4 / velocity | unavailable | unavailable | 2 |
| rh_RFJ3 / force | 1 | unavailable | unavailable |
| rh_RFJ3 / velocity | unavailable | unavailable | 2 |
| rh_RFJ2 / effort | unavailable | unavailable | 2 |
| rh_RFJ2 / force | unavailable | unavailable | unavailable |
| rh_RFJ2 / velocity | unavailable | unavailable | 2 |
| rh_RFJ1 / effort | unavailable | unavailable | 2 |
| rh_RFJ1 / force | unavailable | unavailable | unavailable |
| rh_RFJ1 / velocity | unavailable | unavailable | 2 |
| rh_LFJ5 / force | 1 | unavailable | unavailable |
| rh_LFJ5 / velocity | unavailable | unavailable | 2 |
| rh_LFJ4 / force | 1 | unavailable | unavailable |
| rh_LFJ4 / velocity | unavailable | unavailable | 2 |
| rh_LFJ3 / force | 1 | unavailable | unavailable |
| rh_LFJ3 / velocity | unavailable | unavailable | 2 |
| rh_LFJ2 / effort | unavailable | unavailable | 2 |
| rh_LFJ2 / force | unavailable | unavailable | unavailable |
| rh_LFJ2 / velocity | unavailable | unavailable | 2 |
| rh_LFJ1 / effort | unavailable | unavailable | 2 |
| rh_LFJ1 / force | unavailable | unavailable | unavailable |
| rh_LFJ1 / velocity | unavailable | unavailable | 2 |
| rh_THJ5 / force | 3 | unavailable | unavailable |
| rh_THJ5 / velocity | unavailable | unavailable | 4 |
| rh_THJ4 / force | 2 | unavailable | unavailable |
| rh_THJ4 / velocity | unavailable | unavailable | 4 |
| rh_THJ3 / force | 1 | unavailable | unavailable |
| rh_THJ3 / velocity | unavailable | unavailable | 4 |
| rh_THJ2 / force | 1 | unavailable | unavailable |
| rh_THJ2 / velocity | unavailable | unavailable | 2 |
| rh_THJ1 / force | 1 | unavailable | unavailable |
| rh_THJ1 / velocity | unavailable | unavailable | 4 |
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
  "https://github.com/shadow-robot/sr_common sr_description/hand/xacro/forearm/forearm_e.urdf.xacro at 172c3d9c3715ee75eb10dfe4ee57e26a342b4529: ValueError: Macro-only input has no uniquely identified robot macro",
  "https://github.com/shadow-robot/sr_common sr_description/mujoco_models/urdfs/shadowhand_motor.urdf at 172c3d9c3715ee75eb10dfe4ee57e26a342b4529: ParseError: XML or text declaration not at start of entity: line 26, column 0",
  "https://github.com/shadow-robot/sr_common sr_description/mujoco_models/urdfs/shadowhand_motor_left.urdf at 172c3d9c3715ee75eb10dfe4ee57e26a342b4529: ParseError: XML or text declaration not at start of entity: line 26, column 0",
  "https://github.com/shadow-robot/sr_common sr_description/mujoco_models/urdfs/shadowhand_motor_plus.urdf at 172c3d9c3715ee75eb10dfe4ee57e26a342b4529: ParseError: XML or text declaration not at start of entity: line 26, column 0",
  "https://github.com/shadow-robot/sr_common sr_description/mujoco_models/urdfs/shadowhand_motor_plus_left.urdf at 172c3d9c3715ee75eb10dfe4ee57e26a342b4529: ParseError: XML or text declaration not at start of entity: line 26, column 0"
]
```

## History inputs

```json
[
  "sr_description/hand/xacro/finger/distal/distal.gazebo.xacro",
  "sr_description/hand/xacro/finger/distal/distal.transmission.xacro",
  "sr_description/hand/xacro/finger/distal/distal.urdf.xacro",
  "sr_description/hand/xacro/finger/distal/f_distal_mstXL.urdf.xacro",
  "sr_description/hand/xacro/finger/fingers.urdf.xacro",
  "sr_description/hand/xacro/finger/knuckle/knuckle.gazebo.xacro",
  "sr_description/hand/xacro/finger/knuckle/knuckle.transmission.xacro",
  "sr_description/hand/xacro/finger/knuckle/knuckle.urdf.xacro",
  "sr_description/hand/xacro/finger/lfmetacarpal/lfmetacarpal.gazebo.xacro",
  "sr_description/hand/xacro/finger/lfmetacarpal/lfmetacarpal.transmission.xacro",
  "sr_description/hand/xacro/finger/lfmetacarpal/lfmetacarpal.urdf.xacro",
  "sr_description/hand/xacro/finger/middle/middle.gazebo.xacro",
  "sr_description/hand/xacro/finger/middle/middle.transmission.xacro",
  "sr_description/hand/xacro/finger/middle/middle.urdf.xacro",
  "sr_description/hand/xacro/finger/middle/middle_and_distal_bt_2p.urdf.xacro",
  "sr_description/hand/xacro/finger/proximal/proximal.gazebo.xacro",
  "sr_description/hand/xacro/finger/proximal/proximal.transmission.xacro",
  "sr_description/hand/xacro/finger/proximal/proximal.urdf.xacro",
  "sr_description/hand/xacro/forearm/forearm_e.urdf.xacro",
  "sr_description/hand/xacro/hand.urdf.xacro",
  "sr_description/hand/xacro/hand_e.urdf.xacro",
  "sr_description/hand/xacro/palm/imu.urdf.xacro",
  "sr_description/hand/xacro/palm/palm.gazebo.xacro",
  "sr_description/hand/xacro/palm/palm.transmission.xacro",
  "sr_description/hand/xacro/palm/palm_e.urdf.xacro",
  "sr_description/hand/xacro/process_fingers_parameter.xacro",
  "sr_description/hand/xacro/process_hand_type_version_side_parameters.xacro",
  "sr_description/hand/xacro/process_sensor_parameters.xacro",
  "sr_description/hand/xacro/thumb/th_distal_mst.urdf.xacro",
  "sr_description/hand/xacro/thumb/thbase.gazebo.xacro",
  "sr_description/hand/xacro/thumb/thbase.transmission.xacro",
  "sr_description/hand/xacro/thumb/thbase.urdf.xacro",
  "sr_description/hand/xacro/thumb/thdistal.gazebo.xacro",
  "sr_description/hand/xacro/thumb/thdistal.transmission.xacro",
  "sr_description/hand/xacro/thumb/thdistal.urdf.xacro",
  "sr_description/hand/xacro/thumb/thhub.gazebo.xacro",
  "sr_description/hand/xacro/thumb/thhub.transmission.xacro",
  "sr_description/hand/xacro/thumb/thhub.urdf.xacro",
  "sr_description/hand/xacro/thumb/thmiddle.gazebo.xacro",
  "sr_description/hand/xacro/thumb/thmiddle.transmission.xacro",
  "sr_description/hand/xacro/thumb/thmiddle.urdf.xacro",
  "sr_description/hand/xacro/thumb/thproximal.gazebo.xacro",
  "sr_description/hand/xacro/thumb/thproximal.transmission.xacro",
  "sr_description/hand/xacro/thumb/thproximal.urdf.xacro",
  "sr_description/hand/xacro/thumb/thumb.urdf.xacro",
  "sr_description/hand/xacro/validate_macros.xacro",
  "sr_description/hand/xacro/wrist/wrist.transmission.xacro",
  "sr_description/hand/xacro/wrist/wrist.urdf.xacro",
  "sr_description/meshes/components/f_distal/pst/f_distal_pst.dae",
  "sr_description/meshes/components/f_knuckle/f_knuckle_E3M5.dae",
  "sr_description/meshes/components/f_middle/f_middle_E3M5.dae",
  "sr_description/meshes/components/f_proximal/f_proximal_E3M5.dae",
  "sr_description/meshes/components/forearm/forearm_E3M5.dae",
  "sr_description/meshes/components/forearm/forearm_collision_E3M5.dae",
  "sr_description/meshes/components/lf_metacarpal/lf_metacarpal_E3M5.dae",
  "sr_description/meshes/components/palm/palm_E3M5.dae",
  "sr_description/meshes/components/th_distal/pst/th_distal_pst.dae",
  "sr_description/meshes/components/th_middle/th_middle_E3M5.dae",
  "sr_description/meshes/components/th_proximal/th_proximal_E3M5.dae",
  "sr_description/meshes/components/wrist/wrist_E3M5.dae",
  "sr_description/other/xacro/gazebo.urdf.xacro",
  "sr_description/other/xacro/materials.urdf.xacro",
  "sr_description/robots/sr_hand.urdf.xacro"
]
```

## Construction recipe

```json
{
  "file": "sr_description/robots/sr_hand.urdf.xacro",
  "arguments": {
    "side": "right",
    "hand_type": "hand_e",
    "hand_version": "E3M5"
  },
  "evidence": "The README links a component macro; the manufacturer's standalone hand wrapper supplies the complete right-hand E-series construction. Both Menagerie hand variants are self-checked; this recipe compares the right hand."
}
```

## Self comparisons

```json
[
  {
    "file": "shadow_hand/left_hand.xml",
    "status": "passed",
    "findings": 0
  },
  {
    "file": "shadow_hand/right_hand.xml",
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
      "unknown": 30
    },
    "classifications_changed": 0,
    "finding_membership_changes": 4
  },
  "2": {
    "provenance_method": "unknown",
    "counts": {
      "unknown": 23
    },
    "classifications_changed": 0,
    "finding_membership_changes": 3
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
      "shadow_hand/right_hand.xml"
    ],
    "registration": {
      "translation": [
        0.0,
        0.0,
        0.0
      ],
      "rotation": [
        [
          0.0,
          0.0,
          0.9999999999999998
        ],
        [
          0.0,
          -0.9999999999999998,
          0.0
        ],
        [
          0.9999999999999998,
          0.0,
          0.0
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
      "rh_manipulator",
      "rh_imu"
    ],
    "assets_loaded": 29,
    "mesh_conversions": [
      {
        "file": "sr_description/meshes/components/forearm/forearm_E3M5.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "sr_description/meshes/components/forearm/forearm_collision_E3M5.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "sr_description/meshes/components/wrist/wrist_E3M5.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "sr_description/meshes/components/palm/palm_E3M5.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "sr_description/meshes/components/f_knuckle/f_knuckle_E3M5.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "sr_description/meshes/components/f_proximal/f_proximal_E3M5.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "sr_description/meshes/components/f_middle/f_middle_E3M5.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "sr_description/meshes/components/f_distal/pst/f_distal_pst.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "sr_description/meshes/components/f_distal/pst/f_distal_pst.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "sr_description/meshes/components/f_knuckle/f_knuckle_E3M5.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "sr_description/meshes/components/f_proximal/f_proximal_E3M5.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "sr_description/meshes/components/f_middle/f_middle_E3M5.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "sr_description/meshes/components/f_distal/pst/f_distal_pst.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "sr_description/meshes/components/f_distal/pst/f_distal_pst.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "sr_description/meshes/components/f_knuckle/f_knuckle_E3M5.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "sr_description/meshes/components/f_proximal/f_proximal_E3M5.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "sr_description/meshes/components/f_middle/f_middle_E3M5.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "sr_description/meshes/components/f_distal/pst/f_distal_pst.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "sr_description/meshes/components/f_distal/pst/f_distal_pst.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "sr_description/meshes/components/lf_metacarpal/lf_metacarpal_E3M5.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "sr_description/meshes/components/f_knuckle/f_knuckle_E3M5.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "sr_description/meshes/components/f_proximal/f_proximal_E3M5.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "sr_description/meshes/components/f_middle/f_middle_E3M5.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "sr_description/meshes/components/f_distal/pst/f_distal_pst.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "sr_description/meshes/components/f_distal/pst/f_distal_pst.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "sr_description/meshes/components/th_proximal/th_proximal_E3M5.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "sr_description/meshes/components/th_middle/th_middle_E3M5.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "sr_description/meshes/components/th_distal/pst/th_distal_pst.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "sr_description/meshes/components/th_distal/pst/th_distal_pst.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      }
    ],
    "nonphysical_normalizations": [],
    "xacro_arguments": {
      "side": "right",
      "hand_type": "hand_e",
      "hand_version": "E3M5",
      "fingers": "all",
      "tip_sensors": "pst",
      "mid_sensors": "none",
      "prox_sensors": "none",
      "palm_sensor": "none",
      "mounting_plate": "false"
    },
    "source_dependencies": [
      "sr_description/hand/xacro/finger/distal/distal.gazebo.xacro",
      "sr_description/hand/xacro/finger/distal/distal.transmission.xacro",
      "sr_description/hand/xacro/finger/distal/distal.urdf.xacro",
      "sr_description/hand/xacro/finger/distal/f_distal_mstXL.urdf.xacro",
      "sr_description/hand/xacro/finger/fingers.urdf.xacro",
      "sr_description/hand/xacro/finger/knuckle/knuckle.gazebo.xacro",
      "sr_description/hand/xacro/finger/knuckle/knuckle.transmission.xacro",
      "sr_description/hand/xacro/finger/knuckle/knuckle.urdf.xacro",
      "sr_description/hand/xacro/finger/lfmetacarpal/lfmetacarpal.gazebo.xacro",
      "sr_description/hand/xacro/finger/lfmetacarpal/lfmetacarpal.transmission.xacro",
      "sr_description/hand/xacro/finger/lfmetacarpal/lfmetacarpal.urdf.xacro",
      "sr_description/hand/xacro/finger/middle/middle.gazebo.xacro",
      "sr_description/hand/xacro/finger/middle/middle.transmission.xacro",
      "sr_description/hand/xacro/finger/middle/middle.urdf.xacro",
      "sr_description/hand/xacro/finger/middle/middle_and_distal_bt_2p.urdf.xacro",
      "sr_description/hand/xacro/finger/proximal/proximal.gazebo.xacro",
      "sr_description/hand/xacro/finger/proximal/proximal.transmission.xacro",
      "sr_description/hand/xacro/finger/proximal/proximal.urdf.xacro",
      "sr_description/hand/xacro/forearm/forearm_e.urdf.xacro",
      "sr_description/hand/xacro/hand.urdf.xacro",
      "sr_description/hand/xacro/hand_e.urdf.xacro",
      "sr_description/hand/xacro/palm/imu.urdf.xacro",
      "sr_description/hand/xacro/palm/palm.gazebo.xacro",
      "sr_description/hand/xacro/palm/palm.transmission.xacro",
      "sr_description/hand/xacro/palm/palm_e.urdf.xacro",
      "sr_description/hand/xacro/process_fingers_parameter.xacro",
      "sr_description/hand/xacro/process_hand_type_version_side_parameters.xacro",
      "sr_description/hand/xacro/process_sensor_parameters.xacro",
      "sr_description/hand/xacro/thumb/th_distal_mst.urdf.xacro",
      "sr_description/hand/xacro/thumb/thbase.gazebo.xacro",
      "sr_description/hand/xacro/thumb/thbase.transmission.xacro",
      "sr_description/hand/xacro/thumb/thbase.urdf.xacro",
      "sr_description/hand/xacro/thumb/thdistal.gazebo.xacro",
      "sr_description/hand/xacro/thumb/thdistal.transmission.xacro",
      "sr_description/hand/xacro/thumb/thdistal.urdf.xacro",
      "sr_description/hand/xacro/thumb/thhub.gazebo.xacro",
      "sr_description/hand/xacro/thumb/thhub.transmission.xacro",
      "sr_description/hand/xacro/thumb/thhub.urdf.xacro",
      "sr_description/hand/xacro/thumb/thmiddle.gazebo.xacro",
      "sr_description/hand/xacro/thumb/thmiddle.transmission.xacro",
      "sr_description/hand/xacro/thumb/thmiddle.urdf.xacro",
      "sr_description/hand/xacro/thumb/thproximal.gazebo.xacro",
      "sr_description/hand/xacro/thumb/thproximal.transmission.xacro",
      "sr_description/hand/xacro/thumb/thproximal.urdf.xacro",
      "sr_description/hand/xacro/thumb/thumb.urdf.xacro",
      "sr_description/hand/xacro/validate_macros.xacro",
      "sr_description/hand/xacro/wrist/wrist.transmission.xacro",
      "sr_description/hand/xacro/wrist/wrist.urdf.xacro",
      "sr_description/other/xacro/gazebo.urdf.xacro",
      "sr_description/other/xacro/materials.urdf.xacro",
      "sr_description/robots/sr_hand.urdf.xacro",
      "sr_description/meshes/components/forearm/forearm_E3M5.dae",
      "sr_description/meshes/components/forearm/forearm_collision_E3M5.dae",
      "sr_description/meshes/components/wrist/wrist_E3M5.dae",
      "sr_description/meshes/components/palm/palm_E3M5.dae",
      "sr_description/meshes/components/f_knuckle/f_knuckle_E3M5.dae",
      "sr_description/meshes/components/f_proximal/f_proximal_E3M5.dae",
      "sr_description/meshes/components/f_middle/f_middle_E3M5.dae",
      "sr_description/meshes/components/f_distal/pst/f_distal_pst.dae",
      "sr_description/meshes/components/f_distal/pst/f_distal_pst.dae",
      "sr_description/meshes/components/f_knuckle/f_knuckle_E3M5.dae",
      "sr_description/meshes/components/f_proximal/f_proximal_E3M5.dae",
      "sr_description/meshes/components/f_middle/f_middle_E3M5.dae",
      "sr_description/meshes/components/f_distal/pst/f_distal_pst.dae",
      "sr_description/meshes/components/f_distal/pst/f_distal_pst.dae",
      "sr_description/meshes/components/f_knuckle/f_knuckle_E3M5.dae",
      "sr_description/meshes/components/f_proximal/f_proximal_E3M5.dae",
      "sr_description/meshes/components/f_middle/f_middle_E3M5.dae",
      "sr_description/meshes/components/f_distal/pst/f_distal_pst.dae",
      "sr_description/meshes/components/f_distal/pst/f_distal_pst.dae",
      "sr_description/meshes/components/lf_metacarpal/lf_metacarpal_E3M5.dae",
      "sr_description/meshes/components/f_knuckle/f_knuckle_E3M5.dae",
      "sr_description/meshes/components/f_proximal/f_proximal_E3M5.dae",
      "sr_description/meshes/components/f_middle/f_middle_E3M5.dae",
      "sr_description/meshes/components/f_distal/pst/f_distal_pst.dae",
      "sr_description/meshes/components/f_distal/pst/f_distal_pst.dae",
      "sr_description/meshes/components/th_proximal/th_proximal_E3M5.dae",
      "sr_description/meshes/components/th_middle/th_middle_E3M5.dae",
      "sr_description/meshes/components/th_distal/pst/th_distal_pst.dae",
      "sr_description/meshes/components/th_distal/pst/th_distal_pst.dae"
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
  "self_variants_recompiled": 2,
  "historical_snapshots_reused": 26,
  "primary_physics_unchanged": true,
  "source_matching": "original raw-value provenance criteria retained; kinematic guard applies to reported CoM"
}
```
