# sharpa_wave

Status: **complete**. Provenance: **pinned**, confidence **high**.

Source selected using the ordered amended provenance rules.

M: `https://github.com/google-deepmind/mujoco_menagerie`, `sharpa_wave/left_hand.xml`, commit `370c43965323c0944b433b202aac5058b5f907a9`.
H: `https://github.com/sharpa-robotics/sharpa-urdf-usd-xml`, `wave_01/left_sharpa_wave/left_sharpa_wave_with_flange.urdf`, commit `d323b371d02f4fc04a0873c19c5234cae6d803dd`.
S: `6eea427eb24189519f32b9f21674cd534d3f973c` (2026-05-16T09:52:29+08:00). Menagerie release/change: 2026-08-04T09:17:52-07:00.

Limit semantics: MJCF effort values are supported actuator torque/force envelopes. URDF effort and velocity values are manufacturer declarations retained from XML; MuJoCo does not enforce those tags. Such declaration comparisons are explicitly distinct from compiled inertial/range quantities.


## Source evidence

```json
[
  {
    "url": "https://github.com/sharpa-robotics/sharpa-urdf-usd-xml",
    "document": "sharpa_wave/README.md",
    "commit": "370c43965323c0944b433b202aac5058b5f907a9",
    "current": true
  },
  {
    "url": "https://github.com/sharpa-robotics/sharpa-urdf-usd-xml/commit/6eea427eb24189519f32b9f21674cd534d3f973c",
    "document": "sharpa_wave/README.md",
    "commit": "370c43965323c0944b433b202aac5058b5f907a9",
    "current": true
  },
  {
    "url": "https://github.com/sharpa-robotics/sharpa-urdf-usd-xml/commit/6eea427eb24189519f32b9f21674cd534d3f973c",
    "document": "sharpa_wave/CHANGELOG.md",
    "commit": "370c43965323c0944b433b202aac5058b5f907a9",
    "current": true
  }
]
```


## README derivation evidence

Documentation labels are conservative: an automated documented label requires an explicit affected entity and quantity. Broader conversion notes are retained here for review.

>    fused into the world:
>       <compiler meshdir="meshes" balanceinertia="false"
>                 discardvisual="false" fusestatic="false"/>
>      carrying `armature`, `damping`, `frictionloss`, and `actuatorfrcrange`
>      specs. `armature` is the reflected rotor inertia compted from the manufacturer's
> 4. Replaced the auxiliary massless fingertip link (a TCP marker in the URDF)
>    with a `<site>`, then resaved with `fusestatic="true"`. `fusestatic` merges
>    inertia along, so the per-finger elastomer-pad and fingertip links collapse
>    control range from the joint range via `inheritrange="1.0"`.
>   `quat`, `ipos`, `iquat`, geom/site poses, joint `axis`, and joint `range`
> - **`thumb_DP` mass.** The upstream URDFs disagree on the thumb distal
>   phalange mass (`left_sharpa_wave.urdf`: 0.00988 kg, `right_sharpa_wave.urdf`:

## Kinematics consistency

A proper Kabsch rigid transform aligns all matched zero-pose body origins. The maximum per-origin residual and signed hinge/slide axis angles determine whether CoM can be compared; RMS is also recorded. Fewer than three non-collinear origins give insufficient kinematic coverage. CoM records that fail either required M/H or M/S check are excluded from counts and largest discrepancies. Masses, principal moments and raw joint ranges remain unchanged; a flagged range still requires convention review.

| Pair | Status | Origins / rank | RMS / maximum mm | Disagreeing / checked axes |
|---|---|---:|---:|---:|
| M/H | consistent | 23 / 3 | 1.2126134e-05 / 2.50267666e-05 | 0 / 22 |
| M/S | consistent | 23 / 3 | 1.2126134e-05 / 2.50267666e-05 | 0 / 22 |

Exact fitted transforms, per-origin residuals, thresholds and axis vectors:

```json
{
  "M/H": {
    "status": "consistent",
    "matched_body_origins": 23,
    "position_threshold_m": 0.005,
    "axis_threshold_rad": 0.005,
    "residual_definition": "maximum Euclidean residual over matched body origins; Kabsch minimizes RMS, which is also recorded",
    "coordinate_frames": "each snapshot registered to its matched report anchor",
    "anchor_m": "left_hand_C_MC",
    "anchor_other": "left_hand_C_MC",
    "rotation_other_to_m": [
      [
        0.9999999999999758,
        2.1466619939380074e-07,
        4.193364468985758e-08
      ],
      [
        -2.1466620186558385e-07,
        0.9999999999999745,
        5.7675792234157493e-08
      ],
      [
        -4.193363204590961e-08,
        -5.767580103311146e-08,
        0.9999999999999969
      ]
    ],
    "translation_other_to_m": [
      -2.4432344524275007e-09,
      -1.134020134740954e-09,
      -2.3102539187247473e-09
    ],
    "rms_residual_m": 1.2126134046185929e-08,
    "max_residual_m": 2.5026766555704585e-08,
    "fit_rank": 3,
    "axis_checks": [
      {
        "joint_m": "left_thumb_CMC_FE",
        "joint_other": "left_thumb_CMC_FE",
        "axis_m": [
          0.0,
          0.0,
          1.0
        ],
        "axis_other_aligned": [
          4.193364468985761e-08,
          5.7675792234157526e-08,
          0.9999999999999974
        ],
        "angle_rad": 7.130867806103924e-08,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "left_thumb_CMC_AA",
        "joint_other": "left_thumb_CMC_AA",
        "axis_m": [
          -0.9999999999961355,
          1.8536845257501142e-06,
          -2.0719286031312123e-06
        ],
        "axis_other_aligned": [
          -0.9999999999959023,
          1.2905181478571574e-06,
          -2.5554098965309504e-06
        ],
        "angle_rad": 7.422334742226573e-07,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "left_thumb_MCP_FE",
        "joint_other": "left_thumb_MCP_FE",
        "axis_m": [
          -0.866024603538495,
          0.353556670822765,
          0.35355207053942656
        ],
        "axis_other_aligned": [
          -0.8660252387845293,
          0.3535559277349711,
          0.35355125760158573
        ],
        "angle_rad": 1.2714499308182767e-06,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "left_thumb_MCP_AA",
        "joint_other": "left_thumb_MCP_AA",
        "axis_m": [
          -0.4999977118191863,
          -0.6123734281934986,
          -0.612373311484196
        ],
        "axis_other_aligned": [
          -0.4999971046890222,
          -0.6123738162283598,
          -0.612373419165553
        ],
        "angle_rad": 7.285419440702643e-07,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "left_thumb_IP",
        "joint_other": "left_thumb_IP",
        "axis_m": [
          -0.8660246035384951,
          0.35355667082276504,
          0.3535520705394262
        ],
        "axis_other_aligned": [
          -0.8660252387845294,
          0.3535559277349711,
          0.3535512576015858
        ],
        "angle_rad": 1.2714499306102238e-06,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "left_index_MCP_FE",
        "joint_other": "left_index_MCP_FE",
        "axis_m": [
          3.999999999940489e-06,
          0.9999999999840001,
          -4.000000000115023e-06
        ],
        "axis_other_aligned": [
          3.887871148597083e-06,
          0.9999999999854825,
          -3.730881058257178e-06
        ],
        "angle_rad": 2.9154396610541533e-07,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "left_index_MCP_AA",
        "joint_other": "left_index_MCP_AA",
        "axis_m": [
          -0.9999999999999706,
          -2.426423741162358e-07,
          8.970268972063876e-12
        ],
        "axis_other_aligned": [
          -0.9999999999999761,
          2.1466620182428623e-07,
          4.19471248083725e-08
        ],
        "angle_rad": 4.5922754973424947e-07,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "left_index_PIP",
        "joint_other": "left_index_PIP",
        "axis_m": [
          3.999999999995999e-06,
          0.9999999999840001,
          -4.000000000337066e-06
        ],
        "axis_other_aligned": [
          3.887871148597085e-06,
          0.9999999999854825,
          -3.7308810580351343e-06
        ],
        "angle_rad": 2.9154396653669327e-07,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "left_index_DIP",
        "joint_other": "left_index_DIP",
        "axis_m": [
          3.999999999995999e-06,
          0.9999999999840001,
          -4.000000000337066e-06
        ],
        "axis_other_aligned": [
          3.887871148597085e-06,
          0.9999999999854825,
          -3.7308810580351343e-06
        ],
        "angle_rad": 2.9154396653669327e-07,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "left_middle_MCP_FE",
        "joint_other": "left_middle_MCP_FE",
        "axis_m": [
          3.999999999940489e-06,
          0.9999999999840001,
          -4.000000000115023e-06
        ],
        "axis_other_aligned": [
          3.887871148597083e-06,
          0.9999999999854825,
          -3.730881058257178e-06
        ],
        "angle_rad": 2.9154396610541533e-07,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "left_middle_MCP_AA",
        "joint_other": "left_middle_MCP_AA",
        "axis_m": [
          -0.9999999999999706,
          -2.426423741162358e-07,
          8.970268972063876e-12
        ],
        "axis_other_aligned": [
          -0.9999999999999761,
          2.1466620182428623e-07,
          4.19471248083725e-08
        ],
        "angle_rad": 4.5922754973424947e-07,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "left_middle_PIP",
        "joint_other": "left_middle_PIP",
        "axis_m": [
          3.999999999995999e-06,
          0.9999999999840001,
          -4.000000000337066e-06
        ],
        "axis_other_aligned": [
          3.887871148597085e-06,
          0.9999999999854825,
          -3.7308810580351343e-06
        ],
        "angle_rad": 2.9154396653669327e-07,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "left_middle_DIP",
        "joint_other": "left_middle_DIP",
        "axis_m": [
          3.999999999995999e-06,
          0.9999999999840001,
          -4.000000000337066e-06
        ],
        "axis_other_aligned": [
          3.887871148597085e-06,
          0.9999999999854825,
          -3.7308810580351343e-06
        ],
        "angle_rad": 2.9154396653669327e-07,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "left_ring_MCP_FE",
        "joint_other": "left_ring_MCP_FE",
        "axis_m": [
          3.999999999940489e-06,
          0.9999999999840001,
          -4.000000000115023e-06
        ],
        "axis_other_aligned": [
          3.887871148597083e-06,
          0.9999999999854825,
          -3.730881058257178e-06
        ],
        "angle_rad": 2.9154396610541533e-07,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "left_ring_MCP_AA",
        "joint_other": "left_ring_MCP_AA",
        "axis_m": [
          -0.9999999999999706,
          -2.426423741162358e-07,
          8.970268972063876e-12
        ],
        "axis_other_aligned": [
          -0.9999999999999761,
          2.1466620182428623e-07,
          4.19471248083725e-08
        ],
        "angle_rad": 4.5922754973424947e-07,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "left_ring_PIP",
        "joint_other": "left_ring_PIP",
        "axis_m": [
          3.999999999995999e-06,
          0.9999999999840001,
          -4.000000000337066e-06
        ],
        "axis_other_aligned": [
          3.887871148597085e-06,
          0.9999999999854825,
          -3.7308810580351343e-06
        ],
        "angle_rad": 2.9154396653669327e-07,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "left_ring_DIP",
        "joint_other": "left_ring_DIP",
        "axis_m": [
          3.999999999995999e-06,
          0.9999999999840001,
          -4.000000000337066e-06
        ],
        "axis_other_aligned": [
          3.887871148597085e-06,
          0.9999999999854825,
          -3.7308810580351343e-06
        ],
        "angle_rad": 2.9154396653669327e-07,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "left_pinky_CMC",
        "joint_other": "left_pinky_CMC",
        "axis_m": [
          -5.3969743406743644e-11,
          7.346419999702638e-06,
          -0.999999999973015
        ],
        "axis_other_aligned": [
          -4.1986037405692106e-08,
          7.28873441422415e-06,
          -0.9999999999734364
        ],
        "angle_rad": 7.131567198454983e-08,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "left_pinky_MCP_FE",
        "joint_other": "left_pinky_MCP_FE",
        "axis_m": [
          -3.3464199998202e-06,
          0.999999999967416,
          7.3464119999533395e-06
        ],
        "axis_other_aligned": [
          -3.458538595733413e-06,
          0.9999999999674565,
          7.288721067624432e-06
        ],
        "angle_rad": 1.2609053581665286e-07,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "left_pinky_MCP_AA",
        "joint_other": "left_pinky_MCP_AA",
        "axis_m": [
          -0.9999999999632029,
          -7.589091759662258e-06,
          3.999998216985823e-06
        ],
        "axis_other_aligned": [
          -0.9999999999676678,
          -7.131770777744166e-06,
          3.715139159394247e-06
        ],
        "angle_rad": 5.387830390931308e-07,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "left_pinky_PIP",
        "joint_other": "left_pinky_PIP",
        "axis_m": [
          -3.3464199997646883e-06,
          0.9999999999674158,
          7.3464119998423155e-06
        ],
        "axis_other_aligned": [
          -3.4585385957334136e-06,
          0.9999999999674565,
          7.288721067846479e-06
        ],
        "angle_rad": 1.260905357136221e-07,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "left_pinky_DIP",
        "joint_other": "left_pinky_DIP",
        "axis_m": [
          -3.3464199997646883e-06,
          0.9999999999674158,
          7.3464119998423155e-06
        ],
        "axis_other_aligned": [
          -3.4585385957334136e-06,
          0.9999999999674565,
          7.288721067846479e-06
        ],
        "angle_rad": 1.260905357136221e-07,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      }
    ],
    "axis_disagreements": [],
    "com_eligible": true,
    "covariance_singular_values": [
      0.05689020472352432,
      0.02613618611130399,
      0.00035299177077002916
    ],
    "origin_residuals_m": {
      "left_hand_C_MC": 3.5486151417855462e-09,
      "left_thumb_CMC_VL": 7.516476361961869e-09,
      "left_thumb_MC": 8.150604756529742e-09,
      "left_thumb_MCP_VL": 1.7253324187792882e-08,
      "left_thumb_PP": 1.7253324187792882e-08,
      "left_thumb_DP": 2.5026766555704585e-08,
      "left_index_MCP_VL": 6.490416220333932e-09,
      "left_index_PP": 6.490416220333932e-09,
      "left_index_MP": 8.987418017331942e-09,
      "left_index_DP": 1.703275653044013e-08,
      "left_middle_MCP_VL": 4.907842303160084e-09,
      "left_middle_PP": 4.907842303160084e-09,
      "left_middle_MP": 8.402563663733976e-09,
      "left_middle_DP": 1.688838089622488e-08,
      "left_ring_MCP_VL": 6.11975581561762e-09,
      "left_ring_PP": 6.11975581561762e-09,
      "left_ring_MP": 1.0819202392480615e-08,
      "left_ring_DP": 1.8810773105620018e-08,
      "left_pinky_MC": 8.213815238274106e-09,
      "left_pinky_MCP_VL": 9.507739775068247e-09,
      "left_pinky_PP": 9.507739775068247e-09,
      "left_pinky_MP": 9.144287026181277e-09,
      "left_pinky_DP": 1.6969387546965877e-08
    },
    "reason": "Unique proper rigid fit and matched signed axes meet the configured thresholds"
  },
  "M/S": {
    "status": "consistent",
    "matched_body_origins": 23,
    "position_threshold_m": 0.005,
    "axis_threshold_rad": 0.005,
    "residual_definition": "maximum Euclidean residual over matched body origins; Kabsch minimizes RMS, which is also recorded",
    "coordinate_frames": "each snapshot registered to its matched report anchor",
    "anchor_m": "left_hand_C_MC",
    "anchor_other": "left_hand_C_MC",
    "rotation_other_to_m": [
      [
        0.9999999999999758,
        2.1466619939380074e-07,
        4.193364468985758e-08
      ],
      [
        -2.1466620186558385e-07,
        0.9999999999999745,
        5.7675792234157493e-08
      ],
      [
        -4.193363204590961e-08,
        -5.767580103311146e-08,
        0.9999999999999969
      ]
    ],
    "translation_other_to_m": [
      -2.4432344524275007e-09,
      -1.134020134740954e-09,
      -2.3102539187247473e-09
    ],
    "rms_residual_m": 1.2126134046185929e-08,
    "max_residual_m": 2.5026766555704585e-08,
    "fit_rank": 3,
    "axis_checks": [
      {
        "joint_m": "left_thumb_CMC_FE",
        "joint_other": "left_thumb_CMC_FE",
        "axis_m": [
          0.0,
          0.0,
          1.0
        ],
        "axis_other_aligned": [
          4.193364468985761e-08,
          5.7675792234157526e-08,
          0.9999999999999974
        ],
        "angle_rad": 7.130867806103924e-08,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "left_thumb_CMC_AA",
        "joint_other": "left_thumb_CMC_AA",
        "axis_m": [
          -0.9999999999961355,
          1.8536845257501142e-06,
          -2.0719286031312123e-06
        ],
        "axis_other_aligned": [
          -0.9999999999959023,
          1.2905181478571574e-06,
          -2.5554098965309504e-06
        ],
        "angle_rad": 7.422334742226573e-07,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "left_thumb_MCP_FE",
        "joint_other": "left_thumb_MCP_FE",
        "axis_m": [
          -0.866024603538495,
          0.353556670822765,
          0.35355207053942656
        ],
        "axis_other_aligned": [
          -0.8660252387845293,
          0.3535559277349711,
          0.35355125760158573
        ],
        "angle_rad": 1.2714499308182767e-06,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "left_thumb_MCP_AA",
        "joint_other": "left_thumb_MCP_AA",
        "axis_m": [
          -0.4999977118191863,
          -0.6123734281934986,
          -0.612373311484196
        ],
        "axis_other_aligned": [
          -0.4999971046890222,
          -0.6123738162283598,
          -0.612373419165553
        ],
        "angle_rad": 7.285419440702643e-07,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "left_thumb_IP",
        "joint_other": "left_thumb_IP",
        "axis_m": [
          -0.8660246035384951,
          0.35355667082276504,
          0.3535520705394262
        ],
        "axis_other_aligned": [
          -0.8660252387845294,
          0.3535559277349711,
          0.3535512576015858
        ],
        "angle_rad": 1.2714499306102238e-06,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "left_index_MCP_FE",
        "joint_other": "left_index_MCP_FE",
        "axis_m": [
          3.999999999940489e-06,
          0.9999999999840001,
          -4.000000000115023e-06
        ],
        "axis_other_aligned": [
          3.887871148597083e-06,
          0.9999999999854825,
          -3.730881058257178e-06
        ],
        "angle_rad": 2.9154396610541533e-07,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "left_index_MCP_AA",
        "joint_other": "left_index_MCP_AA",
        "axis_m": [
          -0.9999999999999706,
          -2.426423741162358e-07,
          8.970268972063876e-12
        ],
        "axis_other_aligned": [
          -0.9999999999999761,
          2.1466620182428623e-07,
          4.19471248083725e-08
        ],
        "angle_rad": 4.5922754973424947e-07,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "left_index_PIP",
        "joint_other": "left_index_PIP",
        "axis_m": [
          3.999999999995999e-06,
          0.9999999999840001,
          -4.000000000337066e-06
        ],
        "axis_other_aligned": [
          3.887871148597085e-06,
          0.9999999999854825,
          -3.7308810580351343e-06
        ],
        "angle_rad": 2.9154396653669327e-07,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "left_index_DIP",
        "joint_other": "left_index_DIP",
        "axis_m": [
          3.999999999995999e-06,
          0.9999999999840001,
          -4.000000000337066e-06
        ],
        "axis_other_aligned": [
          3.887871148597085e-06,
          0.9999999999854825,
          -3.7308810580351343e-06
        ],
        "angle_rad": 2.9154396653669327e-07,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "left_middle_MCP_FE",
        "joint_other": "left_middle_MCP_FE",
        "axis_m": [
          3.999999999940489e-06,
          0.9999999999840001,
          -4.000000000115023e-06
        ],
        "axis_other_aligned": [
          3.887871148597083e-06,
          0.9999999999854825,
          -3.730881058257178e-06
        ],
        "angle_rad": 2.9154396610541533e-07,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "left_middle_MCP_AA",
        "joint_other": "left_middle_MCP_AA",
        "axis_m": [
          -0.9999999999999706,
          -2.426423741162358e-07,
          8.970268972063876e-12
        ],
        "axis_other_aligned": [
          -0.9999999999999761,
          2.1466620182428623e-07,
          4.19471248083725e-08
        ],
        "angle_rad": 4.5922754973424947e-07,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "left_middle_PIP",
        "joint_other": "left_middle_PIP",
        "axis_m": [
          3.999999999995999e-06,
          0.9999999999840001,
          -4.000000000337066e-06
        ],
        "axis_other_aligned": [
          3.887871148597085e-06,
          0.9999999999854825,
          -3.7308810580351343e-06
        ],
        "angle_rad": 2.9154396653669327e-07,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "left_middle_DIP",
        "joint_other": "left_middle_DIP",
        "axis_m": [
          3.999999999995999e-06,
          0.9999999999840001,
          -4.000000000337066e-06
        ],
        "axis_other_aligned": [
          3.887871148597085e-06,
          0.9999999999854825,
          -3.7308810580351343e-06
        ],
        "angle_rad": 2.9154396653669327e-07,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "left_ring_MCP_FE",
        "joint_other": "left_ring_MCP_FE",
        "axis_m": [
          3.999999999940489e-06,
          0.9999999999840001,
          -4.000000000115023e-06
        ],
        "axis_other_aligned": [
          3.887871148597083e-06,
          0.9999999999854825,
          -3.730881058257178e-06
        ],
        "angle_rad": 2.9154396610541533e-07,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "left_ring_MCP_AA",
        "joint_other": "left_ring_MCP_AA",
        "axis_m": [
          -0.9999999999999706,
          -2.426423741162358e-07,
          8.970268972063876e-12
        ],
        "axis_other_aligned": [
          -0.9999999999999761,
          2.1466620182428623e-07,
          4.19471248083725e-08
        ],
        "angle_rad": 4.5922754973424947e-07,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "left_ring_PIP",
        "joint_other": "left_ring_PIP",
        "axis_m": [
          3.999999999995999e-06,
          0.9999999999840001,
          -4.000000000337066e-06
        ],
        "axis_other_aligned": [
          3.887871148597085e-06,
          0.9999999999854825,
          -3.7308810580351343e-06
        ],
        "angle_rad": 2.9154396653669327e-07,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "left_ring_DIP",
        "joint_other": "left_ring_DIP",
        "axis_m": [
          3.999999999995999e-06,
          0.9999999999840001,
          -4.000000000337066e-06
        ],
        "axis_other_aligned": [
          3.887871148597085e-06,
          0.9999999999854825,
          -3.7308810580351343e-06
        ],
        "angle_rad": 2.9154396653669327e-07,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "left_pinky_CMC",
        "joint_other": "left_pinky_CMC",
        "axis_m": [
          -5.3969743406743644e-11,
          7.346419999702638e-06,
          -0.999999999973015
        ],
        "axis_other_aligned": [
          -4.1986037405692106e-08,
          7.28873441422415e-06,
          -0.9999999999734364
        ],
        "angle_rad": 7.131567198454983e-08,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "left_pinky_MCP_FE",
        "joint_other": "left_pinky_MCP_FE",
        "axis_m": [
          -3.3464199998202e-06,
          0.999999999967416,
          7.3464119999533395e-06
        ],
        "axis_other_aligned": [
          -3.458538595733413e-06,
          0.9999999999674565,
          7.288721067624432e-06
        ],
        "angle_rad": 1.2609053581665286e-07,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "left_pinky_MCP_AA",
        "joint_other": "left_pinky_MCP_AA",
        "axis_m": [
          -0.9999999999632029,
          -7.589091759662258e-06,
          3.999998216985823e-06
        ],
        "axis_other_aligned": [
          -0.9999999999676678,
          -7.131770777744166e-06,
          3.715139159394247e-06
        ],
        "angle_rad": 5.387830390931308e-07,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "left_pinky_PIP",
        "joint_other": "left_pinky_PIP",
        "axis_m": [
          -3.3464199997646883e-06,
          0.9999999999674158,
          7.3464119998423155e-06
        ],
        "axis_other_aligned": [
          -3.4585385957334136e-06,
          0.9999999999674565,
          7.288721067846479e-06
        ],
        "angle_rad": 1.260905357136221e-07,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "left_pinky_DIP",
        "joint_other": "left_pinky_DIP",
        "axis_m": [
          -3.3464199997646883e-06,
          0.9999999999674158,
          7.3464119998423155e-06
        ],
        "axis_other_aligned": [
          -3.4585385957334136e-06,
          0.9999999999674565,
          7.288721067846479e-06
        ],
        "angle_rad": 1.260905357136221e-07,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      }
    ],
    "axis_disagreements": [],
    "com_eligible": true,
    "covariance_singular_values": [
      0.05689020472352432,
      0.02613618611130399,
      0.00035299177077002916
    ],
    "origin_residuals_m": {
      "left_hand_C_MC": 3.5486151417855462e-09,
      "left_thumb_CMC_VL": 7.516476361961869e-09,
      "left_thumb_MC": 8.150604756529742e-09,
      "left_thumb_MCP_VL": 1.7253324187792882e-08,
      "left_thumb_PP": 1.7253324187792882e-08,
      "left_thumb_DP": 2.5026766555704585e-08,
      "left_index_MCP_VL": 6.490416220333932e-09,
      "left_index_PP": 6.490416220333932e-09,
      "left_index_MP": 8.987418017331942e-09,
      "left_index_DP": 1.703275653044013e-08,
      "left_middle_MCP_VL": 4.907842303160084e-09,
      "left_middle_PP": 4.907842303160084e-09,
      "left_middle_MP": 8.402563663733976e-09,
      "left_middle_DP": 1.688838089622488e-08,
      "left_ring_MCP_VL": 6.11975581561762e-09,
      "left_ring_PP": 6.11975581561762e-09,
      "left_ring_MP": 1.0819202392480615e-08,
      "left_ring_DP": 1.8810773105620018e-08,
      "left_pinky_MC": 8.213815238274106e-09,
      "left_pinky_MCP_VL": 9.507739775068247e-09,
      "left_pinky_PP": 9.507739775068247e-09,
      "left_pinky_MP": 9.144287026181277e-09,
      "left_pinky_DP": 1.6969387546965877e-08
    },
    "reason": "Unique proper rigid fit and matched signed axes meet the configured thresholds"
  }
}
```


## Every reported quantity difference

Counts are quantity records, including correlated total/subtree/body mass records; they are not independent robot defects.

| Entity / quantity | M | S | H | H − M | Class | M source | S source | H source |
|---|---|---|---|---|---|---|---|---|
| robot / total_com_registered | [0.000999633089, -0.00910568703, 0.0649205164] | [0.000795677947, -0.00872231027, 0.0663929371] | [0.000795677947, -0.00872231027, 0.0663929371] | [-0.000203955142, 0.000383376755, 0.00147242068] | undocumented derivation difference | [aggregate inputs](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/sharpa_wave/left_hand.xml#L1) | [aggregate inputs](https://github.com/sharpa-robotics/sharpa-urdf-usd-xml/blob/6eea427eb24189519f32b9f21674cd534d3f973c/wave_01/left_sharpa_wave/left_sharpa_wave_with_flange.urdf#L1) | [aggregate inputs](https://github.com/sharpa-robotics/sharpa-urdf-usd-xml/blob/d323b371d02f4fc04a0873c19c5234cae6d803dd/wave_01/left_sharpa_wave/left_sharpa_wave_with_flange.urdf#L1) |
| left_hand_C_MC / mass | 0.72045 | 0.6506 | 0.6506 | -0.06985 | undocumented derivation difference | [geometry/inference input L101](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/sharpa_wave/left_hand.xml#L101) | [input L97](https://github.com/sharpa-robotics/sharpa-urdf-usd-xml/blob/6eea427eb24189519f32b9f21674cd534d3f973c/wave_01/left_sharpa_wave/left_sharpa_wave_with_flange.urdf#L97) | [input L97](https://github.com/sharpa-robotics/sharpa-urdf-usd-xml/blob/d323b371d02f4fc04a0873c19c5234cae6d803dd/wave_01/left_sharpa_wave/left_sharpa_wave_with_flange.urdf#L97) |
| left_hand_C_MC / subtree_mass | 1.31511 | 1.245265 | 1.245265 | -0.069845 | undocumented derivation difference | [subtree root L101](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/sharpa_wave/left_hand.xml#L101) | [subtree root L91](https://github.com/sharpa-robotics/sharpa-urdf-usd-xml/blob/6eea427eb24189519f32b9f21674cd534d3f973c/wave_01/left_sharpa_wave/left_sharpa_wave_with_flange.urdf#L91) | [subtree root L91](https://github.com/sharpa-robotics/sharpa-urdf-usd-xml/blob/d323b371d02f4fc04a0873c19c5234cae6d803dd/wave_01/left_sharpa_wave/left_sharpa_wave_with_flange.urdf#L91) |
| left_hand_C_MC / com_registered | [-0.00145583083, -0.00556187284, 0.0431600311] | [-0.00216000191, -0.00535999836, 0.0401099981] | [-0.00216000191, -0.00535999836, 0.0401099981] | [-0.00070417108, 0.000201874481, -0.00305003298] | undocumented derivation difference | [geometry/inference input L101](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/sharpa_wave/left_hand.xml#L101) | [CoM/kinematic input L96](https://github.com/sharpa-robotics/sharpa-urdf-usd-xml/blob/6eea427eb24189519f32b9f21674cd534d3f973c/wave_01/left_sharpa_wave/left_sharpa_wave_with_flange.urdf#L96) | [CoM/kinematic input L96](https://github.com/sharpa-robotics/sharpa-urdf-usd-xml/blob/d323b371d02f4fc04a0873c19c5234cae6d803dd/wave_01/left_sharpa_wave/left_sharpa_wave_with_flange.urdf#L96) |
| left_hand_C_MC / principal_moments | [0.000309347513, 0.000633187335, 0.000759773226] | [0.000273139723, 0.000674248205, 0.000814964071] | [0.000273139723, 0.000674248205, 0.000814964071] | [-3.62077896e-05, 4.10608707e-05, 5.51908458e-05] | undocumented derivation difference | [geometry/inference input L101](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/sharpa_wave/left_hand.xml#L101) | [inertia input L105](https://github.com/sharpa-robotics/sharpa-urdf-usd-xml/blob/6eea427eb24189519f32b9f21674cd534d3f973c/wave_01/left_sharpa_wave/left_sharpa_wave_with_flange.urdf#L105) | [inertia input L105](https://github.com/sharpa-robotics/sharpa-urdf-usd-xml/blob/d323b371d02f4fc04a0873c19c5234cae6d803dd/wave_01/left_sharpa_wave/left_sharpa_wave_with_flange.urdf#L105) |
| left_thumb_MCP_VL / com_registered | [0.0155374217, -0.0745466388, 0.0618718528] | [0.0153918215, -0.0762044975, 0.0631194199] | [0.0153918215, -0.0762044975, 0.0631194199] | [-0.000145600198, -0.00165785871, 0.00124756708] | undocumented derivation difference | [geometry/inference input L150](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/sharpa_wave/left_hand.xml#L150) | [CoM/kinematic input L222](https://github.com/sharpa-robotics/sharpa-urdf-usd-xml/blob/6eea427eb24189519f32b9f21674cd534d3f973c/wave_01/left_sharpa_wave/left_sharpa_wave_with_flange.urdf#L222) | [CoM/kinematic input L222](https://github.com/sharpa-robotics/sharpa-urdf-usd-xml/blob/d323b371d02f4fc04a0873c19c5234cae6d803dd/wave_01/left_sharpa_wave/left_sharpa_wave_with_flange.urdf#L222) |
| left_thumb_MCP_VL / principal_moments | [2.11683605e-09, 4.00367999e-09, 4.59106593e-09] | [3.79006832e-08, 6.40993168e-08, 7.9e-08] | [3.79006832e-08, 6.40993168e-08, 7.9e-08] | [3.57838472e-08, 6.00956368e-08, 7.44089341e-08] | undocumented derivation difference | [geometry/inference input L150](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/sharpa_wave/left_hand.xml#L150) | [inertia input L231](https://github.com/sharpa-robotics/sharpa-urdf-usd-xml/blob/6eea427eb24189519f32b9f21674cd534d3f973c/wave_01/left_sharpa_wave/left_sharpa_wave_with_flange.urdf#L231) | [inertia input L231](https://github.com/sharpa-robotics/sharpa-urdf-usd-xml/blob/d323b371d02f4fc04a0873c19c5234cae6d803dd/wave_01/left_sharpa_wave/left_sharpa_wave_with_flange.urdf#L231) |
| left_index_DP / principal_moments | [1.34852e-07, 3.09574e-07, 3.15145e-07] | [1.34069572e-07, 2.93486683e-07, 2.98493745e-07] | [1.34069572e-07, 2.93486683e-07, 2.98493745e-07] | [-7.82427576e-10, -1.60873171e-08, -1.66512554e-08] | undocumented derivation difference | [inertia input L197](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/sharpa_wave/left_hand.xml#L197) | [inertia input L584](https://github.com/sharpa-robotics/sharpa-urdf-usd-xml/blob/6eea427eb24189519f32b9f21674cd534d3f973c/wave_01/left_sharpa_wave/left_sharpa_wave_with_flange.urdf#L584) | [inertia input L584](https://github.com/sharpa-robotics/sharpa-urdf-usd-xml/blob/d323b371d02f4fc04a0873c19c5234cae6d803dd/wave_01/left_sharpa_wave/left_sharpa_wave_with_flange.urdf#L584) |
| left_middle_DP / principal_moments | [1.34852e-07, 3.09574e-07, 3.15145e-07] | [1.34069572e-07, 2.93486683e-07, 2.98493745e-07] | [1.34069572e-07, 2.93486683e-07, 2.98493745e-07] | [-7.82427576e-10, -1.60873171e-08, -1.66512554e-08] | undocumented derivation difference | [inertia input L231](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/sharpa_wave/left_hand.xml#L231) | [inertia input L849](https://github.com/sharpa-robotics/sharpa-urdf-usd-xml/blob/6eea427eb24189519f32b9f21674cd534d3f973c/wave_01/left_sharpa_wave/left_sharpa_wave_with_flange.urdf#L849) | [inertia input L849](https://github.com/sharpa-robotics/sharpa-urdf-usd-xml/blob/d323b371d02f4fc04a0873c19c5234cae6d803dd/wave_01/left_sharpa_wave/left_sharpa_wave_with_flange.urdf#L849) |
| left_ring_DP / principal_moments | [1.34852e-07, 3.09574e-07, 3.15145e-07] | [1.34069572e-07, 2.93486683e-07, 2.98493745e-07] | [1.34069572e-07, 2.93486683e-07, 2.98493745e-07] | [-7.82427576e-10, -1.60873171e-08, -1.66512554e-08] | undocumented derivation difference | [inertia input L265](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/sharpa_wave/left_hand.xml#L265) | [inertia input L1114](https://github.com/sharpa-robotics/sharpa-urdf-usd-xml/blob/6eea427eb24189519f32b9f21674cd534d3f973c/wave_01/left_sharpa_wave/left_sharpa_wave_with_flange.urdf#L1114) | [inertia input L1114](https://github.com/sharpa-robotics/sharpa-urdf-usd-xml/blob/d323b371d02f4fc04a0873c19c5234cae6d803dd/wave_01/left_sharpa_wave/left_sharpa_wave_with_flange.urdf#L1114) |
| left_pinky_MC / com_registered | [-0.000527119874, 0.0322638687, 0.0579471307] | [0.000561465549, 0.0322876902, 0.12041254] | [0.000561465549, 0.0322876902, 0.12041254] | [0.00108858542, 2.38214723e-05, 0.0624654091] | undocumented derivation difference | [geometry/inference input L277](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/sharpa_wave/left_hand.xml#L277) | [CoM/kinematic input L1226](https://github.com/sharpa-robotics/sharpa-urdf-usd-xml/blob/6eea427eb24189519f32b9f21674cd534d3f973c/wave_01/left_sharpa_wave/left_sharpa_wave_with_flange.urdf#L1226) | [CoM/kinematic input L1226](https://github.com/sharpa-robotics/sharpa-urdf-usd-xml/blob/d323b371d02f4fc04a0873c19c5234cae6d803dd/wave_01/left_sharpa_wave/left_sharpa_wave_with_flange.urdf#L1226) |
| left_pinky_MC / principal_moments | [1.97490954e-05, 3.39128957e-05, 4.31565518e-05] | [1.69875916e-05, 3.72569487e-05, 4.47764597e-05] | [1.69875916e-05, 3.72569487e-05, 4.47764597e-05] | [-2.76150375e-06, 3.34405298e-06, 1.61990788e-06] | undocumented derivation difference | [geometry/inference input L277](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/sharpa_wave/left_hand.xml#L277) | [inertia input L1235](https://github.com/sharpa-robotics/sharpa-urdf-usd-xml/blob/6eea427eb24189519f32b9f21674cd534d3f973c/wave_01/left_sharpa_wave/left_sharpa_wave_with_flange.urdf#L1235) | [inertia input L1235](https://github.com/sharpa-robotics/sharpa-urdf-usd-xml/blob/d323b371d02f4fc04a0873c19c5234cae6d803dd/wave_01/left_sharpa_wave/left_sharpa_wave_with_flange.urdf#L1235) |
| left_pinky_DP / principal_moments | [1.34852e-07, 3.09574e-07, 3.15145e-07] | [1.34069572e-07, 2.93486683e-07, 2.98493745e-07] | [1.34069572e-07, 2.93486683e-07, 2.98493745e-07] | [-7.82427576e-10, -1.60873171e-08, -1.66512554e-08] | undocumented derivation difference | [inertia input L304](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/sharpa_wave/left_hand.xml#L304) | [inertia input L1427](https://github.com/sharpa-robotics/sharpa-urdf-usd-xml/blob/6eea427eb24189519f32b9f21674cd534d3f973c/wave_01/left_sharpa_wave/left_sharpa_wave_with_flange.urdf#L1427) | [inertia input L1427](https://github.com/sharpa-robotics/sharpa-urdf-usd-xml/blob/d323b371d02f4fc04a0873c19c5234cae6d803dd/wave_01/left_sharpa_wave/left_sharpa_wave_with_flange.urdf#L1427) |

## Raw CoM records and reporting decisions

Raw values retain the previous root-anchor registration before Kabsch; original world coordinates also remain in the snapshots. Eligible findings above use the fitted transform into M. Excluded raw records below are diagnostic numbers, not findings. No CoM suppression applies to mass or principal inertia moments.

| Entity / quantity | Raw M | Raw S | Raw H | Raw H − M | Decision | M source | S source | H source |
|---|---|---|---|---|---|---|---|---|
| robot / total_com_registered | [0.000999633089, -0.00910568703, 0.0649205164] | [0.000795679479, -0.0087223128, 0.0663929389] | [0.000795679479, -0.0087223128, 0.0663929389] | [-0.000203953611, 0.000383374231, 0.00147242252] | eligible; compared after Kabsch alignment | [aggregate inputs](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/sharpa_wave/left_hand.xml#L1) | [aggregate inputs](https://github.com/sharpa-robotics/sharpa-urdf-usd-xml/blob/6eea427eb24189519f32b9f21674cd534d3f973c/wave_01/left_sharpa_wave/left_sharpa_wave_with_flange.urdf#L1) | [aggregate inputs](https://github.com/sharpa-robotics/sharpa-urdf-usd-xml/blob/d323b371d02f4fc04a0873c19c5234cae6d803dd/wave_01/left_sharpa_wave/left_sharpa_wave_with_flange.urdf#L1) |
| left_hand_C_MC / com_registered | [-0.00145583083, -0.00556187284, 0.0431600311] | [-0.00216, -0.00536, 0.04011] | [-0.00216, -0.00536, 0.04011] | [-0.000704169168, 0.000201872838, -0.00305003107] | eligible; compared after Kabsch alignment | [geometry/inference input L101](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/sharpa_wave/left_hand.xml#L101) | [CoM/kinematic input L96](https://github.com/sharpa-robotics/sharpa-urdf-usd-xml/blob/6eea427eb24189519f32b9f21674cd534d3f973c/wave_01/left_sharpa_wave/left_sharpa_wave_with_flange.urdf#L96) | [CoM/kinematic input L96](https://github.com/sharpa-robotics/sharpa-urdf-usd-xml/blob/d323b371d02f4fc04a0873c19c5234cae6d803dd/wave_01/left_sharpa_wave/left_sharpa_wave_with_flange.urdf#L96) |
| left_thumb_CMC_VL / com_registered | [0.00980000276, -0.0253499992, 0.0214] | [0.00980000239, -0.0253499993, 0.0214] | [0.00980000239, -0.0253499993, 0.0214] | [-3.70134678e-10, -1.13885991e-10, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L138](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/sharpa_wave/left_hand.xml#L138) | [CoM/kinematic input L134](https://github.com/sharpa-robotics/sharpa-urdf-usd-xml/blob/6eea427eb24189519f32b9f21674cd534d3f973c/wave_01/left_sharpa_wave/left_sharpa_wave_with_flange.urdf#L134) | [CoM/kinematic input L134](https://github.com/sharpa-robotics/sharpa-urdf-usd-xml/blob/d323b371d02f4fc04a0873c19c5234cae6d803dd/wave_01/left_sharpa_wave/left_sharpa_wave_with_flange.urdf#L134) |
| left_thumb_MC / com_registered | [0.0101699005, -0.0590006304, 0.0399191933] | [0.0101699164, -0.0590006267, 0.0399192006] | [0.0101699164, -0.0590006267, 0.0399192006] | [1.59386949e-08, 3.74275773e-09, 7.29355468e-09] | eligible; compared after Kabsch alignment | [CoM/kinematic input L145](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/sharpa_wave/left_hand.xml#L145) | [CoM/kinematic input L174](https://github.com/sharpa-robotics/sharpa-urdf-usd-xml/blob/6eea427eb24189519f32b9f21674cd534d3f973c/wave_01/left_sharpa_wave/left_sharpa_wave_with_flange.urdf#L174) | [CoM/kinematic input L174](https://github.com/sharpa-robotics/sharpa-urdf-usd-xml/blob/d323b371d02f4fc04a0873c19c5234cae6d803dd/wave_01/left_sharpa_wave/left_sharpa_wave_with_flange.urdf#L174) |
| left_thumb_MCP_VL / com_registered | [0.0155374217, -0.0745466388, 0.0618718528] | [0.0153918377, -0.0762044967, 0.0631194184] | [0.0153918377, -0.0762044967, 0.0631194184] | [-0.000145584043, -0.00165785791, 0.00124756564] | eligible; compared after Kabsch alignment | [geometry/inference input L150](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/sharpa_wave/left_hand.xml#L150) | [CoM/kinematic input L222](https://github.com/sharpa-robotics/sharpa-urdf-usd-xml/blob/6eea427eb24189519f32b9f21674cd534d3f973c/wave_01/left_sharpa_wave/left_sharpa_wave_with_flange.urdf#L222) | [CoM/kinematic input L222](https://github.com/sharpa-robotics/sharpa-urdf-usd-xml/blob/d323b371d02f4fc04a0873c19c5234cae6d803dd/wave_01/left_sharpa_wave/left_sharpa_wave_with_flange.urdf#L222) |
| left_thumb_PP / com_registered | [0.015754489, -0.0921340048, 0.0772504387] | [0.015754511, -0.0921339916, 0.0772504535] | [0.015754511, -0.0921339916, 0.0772504535] | [2.20468607e-08, 1.32544853e-08, 1.48133854e-08] | eligible; compared after Kabsch alignment | [CoM/kinematic input L155](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/sharpa_wave/left_hand.xml#L155) | [CoM/kinematic input L261](https://github.com/sharpa-robotics/sharpa-urdf-usd-xml/blob/6eea427eb24189519f32b9f21674cd534d3f973c/wave_01/left_sharpa_wave/left_sharpa_wave_with_flange.urdf#L261) | [CoM/kinematic input L261](https://github.com/sharpa-robotics/sharpa-urdf-usd-xml/blob/d323b371d02f4fc04a0873c19c5234cae6d803dd/wave_01/left_sharpa_wave/left_sharpa_wave_with_flange.urdf#L261) |
| left_thumb_DP / com_registered | [0.0153666276, -0.11105053, 0.0950760733] | [0.0153664001, -0.111124091, 0.095120417] | [0.0153664001, -0.111124091, 0.095120417] | [-2.27514299e-07, -7.35611437e-05, 4.43437019e-05] | eligible; compared after Kabsch alignment | [CoM/kinematic input L162](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/sharpa_wave/left_hand.xml#L162) | [CoM/kinematic input L309](https://github.com/sharpa-robotics/sharpa-urdf-usd-xml/blob/6eea427eb24189519f32b9f21674cd534d3f973c/wave_01/left_sharpa_wave/left_sharpa_wave_with_flange.urdf#L309) | [CoM/kinematic input L309](https://github.com/sharpa-robotics/sharpa-urdf-usd-xml/blob/d323b371d02f4fc04a0873c19c5234cae6d803dd/wave_01/left_sharpa_wave/left_sharpa_wave_with_flange.urdf#L309) |
| left_index_MCP_VL / com_registered | [-0.0003, -0.0303000316, 0.0867] | [-0.0003, -0.030300029, 0.0867] | [-0.0003, -0.030300029, 0.0867] | [-5.2160316e-14, 2.58167968e-09, -1.12410081e-15] | eligible; compared after Kabsch alignment | [CoM/kinematic input L176](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/sharpa_wave/left_hand.xml#L176) | [CoM/kinematic input L430](https://github.com/sharpa-robotics/sharpa-urdf-usd-xml/blob/6eea427eb24189519f32b9f21674cd534d3f973c/wave_01/left_sharpa_wave/left_sharpa_wave_with_flange.urdf#L430) | [CoM/kinematic input L430](https://github.com/sharpa-robotics/sharpa-urdf-usd-xml/blob/d323b371d02f4fc04a0873c19c5234cae6d803dd/wave_01/left_sharpa_wave/left_sharpa_wave_with_flange.urdf#L430) |
| left_index_PP / com_registered | [0.00168000013, -0.0308498918, 0.122900002] | [0.00168, -0.0308499008, 0.122900002] | [0.00168, -0.0308499008, 0.122900002] | [-1.3330499e-10, -8.98845973e-09, -1.7970643e-10] | eligible; compared after Kabsch alignment | [CoM/kinematic input L183](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/sharpa_wave/left_hand.xml#L183) | [CoM/kinematic input L479](https://github.com/sharpa-robotics/sharpa-urdf-usd-xml/blob/6eea427eb24189519f32b9f21674cd534d3f973c/wave_01/left_sharpa_wave/left_sharpa_wave_with_flange.urdf#L479) | [CoM/kinematic input L479](https://github.com/sharpa-robotics/sharpa-urdf-usd-xml/blob/d323b371d02f4fc04a0873c19c5234cae6d803dd/wave_01/left_sharpa_wave/left_sharpa_wave_with_flange.urdf#L479) |
| left_index_MP / com_registered | [-0.00015999768, -0.0297197589, 0.155019998] | [-0.000159997869, -0.0297197786, 0.155019998] | [-0.000159997869, -0.0297197786, 0.155019998] | [-1.89217779e-10, -1.96991949e-08, 1.896244e-10] | eligible; compared after Kabsch alignment | [CoM/kinematic input L190](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/sharpa_wave/left_hand.xml#L190) | [CoM/kinematic input L527](https://github.com/sharpa-robotics/sharpa-urdf-usd-xml/blob/6eea427eb24189519f32b9f21674cd534d3f973c/wave_01/left_sharpa_wave/left_sharpa_wave_with_flange.urdf#L527) | [CoM/kinematic input L527](https://github.com/sharpa-robotics/sharpa-urdf-usd-xml/blob/d323b371d02f4fc04a0873c19c5234cae6d803dd/wave_01/left_sharpa_wave/left_sharpa_wave_with_flange.urdf#L527) |
| left_index_DP / com_registered | [-0.00157344043, -0.0304072598, 0.1868856] | [-0.0016300004, -0.0304096551, 0.18716] | [-0.0016300004, -0.0304096551, 0.18716] | [-5.6559973e-05, -2.39535893e-06, 0.000274399974] | eligible; compared after Kabsch alignment | [CoM/kinematic input L197](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/sharpa_wave/left_hand.xml#L197) | [CoM/kinematic input L575](https://github.com/sharpa-robotics/sharpa-urdf-usd-xml/blob/6eea427eb24189519f32b9f21674cd534d3f973c/wave_01/left_sharpa_wave/left_sharpa_wave_with_flange.urdf#L575) | [CoM/kinematic input L575](https://github.com/sharpa-robotics/sharpa-urdf-usd-xml/blob/d323b371d02f4fc04a0873c19c5234cae6d803dd/wave_01/left_sharpa_wave/left_sharpa_wave_with_flange.urdf#L575) |
| left_middle_MCP_VL / com_registered | [-0.0013, -0.0100000316, 0.0897] | [-0.0013, -0.010000029, 0.0897] | [-0.0013, -0.010000029, 0.0897] | [-5.2160316e-14, 2.58167968e-09, -1.12410081e-15] | eligible; compared after Kabsch alignment | [CoM/kinematic input L210](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/sharpa_wave/left_hand.xml#L210) | [CoM/kinematic input L696](https://github.com/sharpa-robotics/sharpa-urdf-usd-xml/blob/6eea427eb24189519f32b9f21674cd534d3f973c/wave_01/left_sharpa_wave/left_sharpa_wave_with_flange.urdf#L696) | [CoM/kinematic input L696](https://github.com/sharpa-robotics/sharpa-urdf-usd-xml/blob/d323b371d02f4fc04a0873c19c5234cae6d803dd/wave_01/left_sharpa_wave/left_sharpa_wave_with_flange.urdf#L696) |
| left_middle_PP / com_registered | [0.000680000134, -0.0105498918, 0.125900002] | [0.00068, -0.0105499008, 0.125900002] | [0.00068, -0.0105499008, 0.125900002] | [-1.3330499e-10, -8.98845973e-09, -1.79706416e-10] | eligible; compared after Kabsch alignment | [CoM/kinematic input L217](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/sharpa_wave/left_hand.xml#L217) | [CoM/kinematic input L744](https://github.com/sharpa-robotics/sharpa-urdf-usd-xml/blob/6eea427eb24189519f32b9f21674cd534d3f973c/wave_01/left_sharpa_wave/left_sharpa_wave_with_flange.urdf#L744) | [CoM/kinematic input L744](https://github.com/sharpa-robotics/sharpa-urdf-usd-xml/blob/d323b371d02f4fc04a0873c19c5234cae6d803dd/wave_01/left_sharpa_wave/left_sharpa_wave_with_flange.urdf#L744) |
| left_middle_MP / com_registered | [-0.00115999768, -0.00941975888, 0.158019998] | [-0.00115999787, -0.00941977858, 0.158019998] | [-0.00115999787, -0.00941977858, 0.158019998] | [-1.89217779e-10, -1.96991949e-08, 1.896244e-10] | eligible; compared after Kabsch alignment | [CoM/kinematic input L224](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/sharpa_wave/left_hand.xml#L224) | [CoM/kinematic input L792](https://github.com/sharpa-robotics/sharpa-urdf-usd-xml/blob/6eea427eb24189519f32b9f21674cd534d3f973c/wave_01/left_sharpa_wave/left_sharpa_wave_with_flange.urdf#L792) | [CoM/kinematic input L792](https://github.com/sharpa-robotics/sharpa-urdf-usd-xml/blob/d323b371d02f4fc04a0873c19c5234cae6d803dd/wave_01/left_sharpa_wave/left_sharpa_wave_with_flange.urdf#L792) |
| left_middle_DP / com_registered | [-0.00257344043, -0.0101072598, 0.1898856] | [-0.0026300004, -0.0101096551, 0.19016] | [-0.0026300004, -0.0101096551, 0.19016] | [-5.6559973e-05, -2.39535893e-06, 0.000274399974] | eligible; compared after Kabsch alignment | [CoM/kinematic input L231](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/sharpa_wave/left_hand.xml#L231) | [CoM/kinematic input L840](https://github.com/sharpa-robotics/sharpa-urdf-usd-xml/blob/6eea427eb24189519f32b9f21674cd534d3f973c/wave_01/left_sharpa_wave/left_sharpa_wave_with_flange.urdf#L840) | [CoM/kinematic input L840](https://github.com/sharpa-robotics/sharpa-urdf-usd-xml/blob/d323b371d02f4fc04a0873c19c5234cae6d803dd/wave_01/left_sharpa_wave/left_sharpa_wave_with_flange.urdf#L840) |
| left_ring_MCP_VL / com_registered | [0.0002, 0.0102999684, 0.0837] | [0.0002, 0.010299971, 0.0837] | [0.0002, 0.010299971, 0.0837] | [-5.2160316e-14, 2.58167968e-09, -1.1379786e-15] | eligible; compared after Kabsch alignment | [CoM/kinematic input L244](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/sharpa_wave/left_hand.xml#L244) | [CoM/kinematic input L961](https://github.com/sharpa-robotics/sharpa-urdf-usd-xml/blob/6eea427eb24189519f32b9f21674cd534d3f973c/wave_01/left_sharpa_wave/left_sharpa_wave_with_flange.urdf#L961) | [CoM/kinematic input L961](https://github.com/sharpa-robotics/sharpa-urdf-usd-xml/blob/d323b371d02f4fc04a0873c19c5234cae6d803dd/wave_01/left_sharpa_wave/left_sharpa_wave_with_flange.urdf#L961) |
| left_ring_PP / com_registered | [0.00218000013, 0.00975010817, 0.119900002] | [0.00218, 0.00975009918, 0.119900002] | [0.00218, 0.00975009918, 0.119900002] | [-1.3330499e-10, -8.98845973e-09, -1.7970643e-10] | eligible; compared after Kabsch alignment | [CoM/kinematic input L251](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/sharpa_wave/left_hand.xml#L251) | [CoM/kinematic input L1009](https://github.com/sharpa-robotics/sharpa-urdf-usd-xml/blob/6eea427eb24189519f32b9f21674cd534d3f973c/wave_01/left_sharpa_wave/left_sharpa_wave_with_flange.urdf#L1009) | [CoM/kinematic input L1009](https://github.com/sharpa-robotics/sharpa-urdf-usd-xml/blob/d323b371d02f4fc04a0873c19c5234cae6d803dd/wave_01/left_sharpa_wave/left_sharpa_wave_with_flange.urdf#L1009) |
| left_ring_MP / com_registered | [0.00034000232, 0.0108802411, 0.152019998] | [0.000340002131, 0.0108802214, 0.152019998] | [0.000340002131, 0.0108802214, 0.152019998] | [-1.89217779e-10, -1.96991949e-08, 1.896244e-10] | eligible; compared after Kabsch alignment | [CoM/kinematic input L258](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/sharpa_wave/left_hand.xml#L258) | [CoM/kinematic input L1057](https://github.com/sharpa-robotics/sharpa-urdf-usd-xml/blob/6eea427eb24189519f32b9f21674cd534d3f973c/wave_01/left_sharpa_wave/left_sharpa_wave_with_flange.urdf#L1057) | [CoM/kinematic input L1057](https://github.com/sharpa-robotics/sharpa-urdf-usd-xml/blob/d323b371d02f4fc04a0873c19c5234cae6d803dd/wave_01/left_sharpa_wave/left_sharpa_wave_with_flange.urdf#L1057) |
| left_ring_DP / com_registered | [-0.00107344043, 0.0101927402, 0.1838856] | [-0.0011300004, 0.0101903449, 0.18416] | [-0.0011300004, 0.0101903449, 0.18416] | [-5.6559973e-05, -2.39535893e-06, 0.000274399974] | eligible; compared after Kabsch alignment | [CoM/kinematic input L265](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/sharpa_wave/left_hand.xml#L265) | [CoM/kinematic input L1105](https://github.com/sharpa-robotics/sharpa-urdf-usd-xml/blob/6eea427eb24189519f32b9f21674cd534d3f973c/wave_01/left_sharpa_wave/left_sharpa_wave_with_flange.urdf#L1105) | [CoM/kinematic input L1105](https://github.com/sharpa-robotics/sharpa-urdf-usd-xml/blob/d323b371d02f4fc04a0873c19c5234cae6d803dd/wave_01/left_sharpa_wave/left_sharpa_wave_with_flange.urdf#L1105) |
| left_pinky_MC / com_registered | [-0.000527119874, 0.0322638687, 0.0579471307] | [0.000561456012, 0.0322876845, 0.120412544] | [0.000561456012, 0.0322876845, 0.120412544] | [0.00108857589, 2.38157819e-05, 0.0624654133] | eligible; compared after Kabsch alignment | [geometry/inference input L277](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/sharpa_wave/left_hand.xml#L277) | [CoM/kinematic input L1226](https://github.com/sharpa-robotics/sharpa-urdf-usd-xml/blob/6eea427eb24189519f32b9f21674cd534d3f973c/wave_01/left_sharpa_wave/left_sharpa_wave_with_flange.urdf#L1226) | [CoM/kinematic input L1226](https://github.com/sharpa-robotics/sharpa-urdf-usd-xml/blob/d323b371d02f4fc04a0873c19c5234cae6d803dd/wave_01/left_sharpa_wave/left_sharpa_wave_with_flange.urdf#L1226) |
| left_pinky_MCP_VL / com_registered | [0.00169992794, 0.0311000018, 0.0777000405] | [0.00169993094, 0.0311000014, 0.07770004] | [0.00169993094, 0.0311000014, 0.07770004] | [3.00655992e-09, -4.24877251e-10, -4.24895022e-10] | eligible; compared after Kabsch alignment | [CoM/kinematic input L283](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/sharpa_wave/left_hand.xml#L283) | [CoM/kinematic input L1274](https://github.com/sharpa-robotics/sharpa-urdf-usd-xml/blob/6eea427eb24189519f32b9f21674cd534d3f973c/wave_01/left_sharpa_wave/left_sharpa_wave_with_flange.urdf#L1274) | [CoM/kinematic input L1274](https://github.com/sharpa-robotics/sharpa-urdf-usd-xml/blob/d323b371d02f4fc04a0873c19c5234cae6d803dd/wave_01/left_sharpa_wave/left_sharpa_wave_with_flange.urdf#L1274) |
| left_pinky_PP / com_registered | [0.00368007691, 0.0305497454, 0.113900029] | [0.00368006796, 0.0305497452, 0.113900029] | [0.00368006796, 0.0305497452, 0.113900029] | [-8.95687181e-09, -1.64508636e-10, 2.22216481e-10] | eligible; compared after Kabsch alignment | [CoM/kinematic input L290](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/sharpa_wave/left_hand.xml#L290) | [CoM/kinematic input L1322](https://github.com/sharpa-robotics/sharpa-urdf-usd-xml/blob/6eea427eb24189519f32b9f21674cd534d3f973c/wave_01/left_sharpa_wave/left_sharpa_wave_with_flange.urdf#L1322) | [CoM/kinematic input L1322](https://github.com/sharpa-robotics/sharpa-urdf-usd-xml/blob/d323b371d02f4fc04a0873c19c5234cae6d803dd/wave_01/left_sharpa_wave/left_sharpa_wave_with_flange.urdf#L1322) |
| left_pinky_MP / com_registered | [0.00184019928, 0.0316795004, 0.146020044] | [0.00184017977, 0.0316795, 0.146020044] | [0.00184017977, 0.0316795, 0.146020044] | [-1.95096028e-08, -3.7807673e-10, -3.79066639e-10] | eligible; compared after Kabsch alignment | [CoM/kinematic input L297](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/sharpa_wave/left_hand.xml#L297) | [CoM/kinematic input L1370](https://github.com/sharpa-robotics/sharpa-urdf-usd-xml/blob/6eea427eb24189519f32b9f21674cd534d3f973c/wave_01/left_sharpa_wave/left_sharpa_wave_with_flange.urdf#L1370) | [CoM/kinematic input L1370](https://github.com/sharpa-robotics/sharpa-urdf-usd-xml/blob/d323b371d02f4fc04a0873c19c5234cae6d803dd/wave_01/left_sharpa_wave/left_sharpa_wave_with_flange.urdf#L1370) |
| left_pinky_DP / com_registered | [0.000426889045, 0.0309916276, 0.177885645] | [0.000370300363, 0.0309892585, 0.178160044] | [0.000370300363, 0.0309892585, 0.178160044] | [-5.65886818e-05, -2.36906308e-06, 0.000274399349] | eligible; compared after Kabsch alignment | [CoM/kinematic input L304](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/sharpa_wave/left_hand.xml#L304) | [CoM/kinematic input L1418](https://github.com/sharpa-robotics/sharpa-urdf-usd-xml/blob/6eea427eb24189519f32b9f21674cd534d3f973c/wave_01/left_sharpa_wave/left_sharpa_wave_with_flange.urdf#L1418) | [CoM/kinematic input L1418](https://github.com/sharpa-robotics/sharpa-urdf-usd-xml/blob/d323b371d02f4fc04a0873c19c5234cae6d803dd/wave_01/left_sharpa_wave/left_sharpa_wave_with_flange.urdf#L1418) |

## Mass accounting

Every contributing compiled body mass is listed here so total/subtree sums can be checked. Links point to explicit inertials or to geometry inputs when the compiler inferred a mass. CoM links identify inertial inputs; world coordinates additionally use the ancestor transforms and the registration recorded below.

| M body | M kg / source | S kg / source | H kg / source |
|---|---|---|---|
| left_hand_C_MC | 0.72045 / [geometry/inference input L101](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/sharpa_wave/left_hand.xml#L101) | 0.6506 / [input L97](https://github.com/sharpa-robotics/sharpa-urdf-usd-xml/blob/6eea427eb24189519f32b9f21674cd534d3f973c/wave_01/left_sharpa_wave/left_sharpa_wave_with_flange.urdf#L97) | 0.6506 / [input L97](https://github.com/sharpa-robotics/sharpa-urdf-usd-xml/blob/d323b371d02f4fc04a0873c19c5234cae6d803dd/wave_01/left_sharpa_wave/left_sharpa_wave_with_flange.urdf#L97) |
| left_thumb_CMC_VL | 0.0025 / [input L138](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/sharpa_wave/left_hand.xml#L138) | 0.0025 / [input L135](https://github.com/sharpa-robotics/sharpa-urdf-usd-xml/blob/6eea427eb24189519f32b9f21674cd534d3f973c/wave_01/left_sharpa_wave/left_sharpa_wave_with_flange.urdf#L135) | 0.0025 / [input L135](https://github.com/sharpa-robotics/sharpa-urdf-usd-xml/blob/d323b371d02f4fc04a0873c19c5234cae6d803dd/wave_01/left_sharpa_wave/left_sharpa_wave_with_flange.urdf#L135) |
| left_thumb_MC | 0.13587 / [input L145](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/sharpa_wave/left_hand.xml#L145) | 0.13587 / [input L175](https://github.com/sharpa-robotics/sharpa-urdf-usd-xml/blob/6eea427eb24189519f32b9f21674cd534d3f973c/wave_01/left_sharpa_wave/left_sharpa_wave_with_flange.urdf#L175) | 0.13587 / [input L175](https://github.com/sharpa-robotics/sharpa-urdf-usd-xml/blob/d323b371d02f4fc04a0873c19c5234cae6d803dd/wave_01/left_sharpa_wave/left_sharpa_wave_with_flange.urdf#L175) |
| left_thumb_MCP_VL | 8e-05 / [geometry/inference input L150](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/sharpa_wave/left_hand.xml#L150) | 8e-05 / [input L223](https://github.com/sharpa-robotics/sharpa-urdf-usd-xml/blob/6eea427eb24189519f32b9f21674cd534d3f973c/wave_01/left_sharpa_wave/left_sharpa_wave_with_flange.urdf#L223) | 8e-05 / [input L223](https://github.com/sharpa-robotics/sharpa-urdf-usd-xml/blob/d323b371d02f4fc04a0873c19c5234cae6d803dd/wave_01/left_sharpa_wave/left_sharpa_wave_with_flange.urdf#L223) |
| left_thumb_PP | 0.03078 / [input L155](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/sharpa_wave/left_hand.xml#L155) | 0.03078 / [input L262](https://github.com/sharpa-robotics/sharpa-urdf-usd-xml/blob/6eea427eb24189519f32b9f21674cd534d3f973c/wave_01/left_sharpa_wave/left_sharpa_wave_with_flange.urdf#L262) | 0.03078 / [input L262](https://github.com/sharpa-robotics/sharpa-urdf-usd-xml/blob/d323b371d02f4fc04a0873c19c5234cae6d803dd/wave_01/left_sharpa_wave/left_sharpa_wave_with_flange.urdf#L262) |
| left_thumb_DP | 0.00998 / [input L162](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/sharpa_wave/left_hand.xml#L162) | 0.00988 / [input L310](https://github.com/sharpa-robotics/sharpa-urdf-usd-xml/blob/6eea427eb24189519f32b9f21674cd534d3f973c/wave_01/left_sharpa_wave/left_sharpa_wave_with_flange.urdf#L310) | 0.00988 / [input L310](https://github.com/sharpa-robotics/sharpa-urdf-usd-xml/blob/d323b371d02f4fc04a0873c19c5234cae6d803dd/wave_01/left_sharpa_wave/left_sharpa_wave_with_flange.urdf#L310) |
| left_index_MCP_VL | 0.00221 / [input L176](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/sharpa_wave/left_hand.xml#L176) | 0.00221 / [input L431](https://github.com/sharpa-robotics/sharpa-urdf-usd-xml/blob/6eea427eb24189519f32b9f21674cd534d3f973c/wave_01/left_sharpa_wave/left_sharpa_wave_with_flange.urdf#L431) | 0.00221 / [input L431](https://github.com/sharpa-robotics/sharpa-urdf-usd-xml/blob/d323b371d02f4fc04a0873c19c5234cae6d803dd/wave_01/left_sharpa_wave/left_sharpa_wave_with_flange.urdf#L431) |
| left_index_PP | 0.04741 / [input L183](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/sharpa_wave/left_hand.xml#L183) | 0.04741 / [input L480](https://github.com/sharpa-robotics/sharpa-urdf-usd-xml/blob/6eea427eb24189519f32b9f21674cd534d3f973c/wave_01/left_sharpa_wave/left_sharpa_wave_with_flange.urdf#L480) | 0.04741 / [input L480](https://github.com/sharpa-robotics/sharpa-urdf-usd-xml/blob/d323b371d02f4fc04a0873c19c5234cae6d803dd/wave_01/left_sharpa_wave/left_sharpa_wave_with_flange.urdf#L480) |
| left_index_MP | 0.01824 / [input L190](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/sharpa_wave/left_hand.xml#L190) | 0.01824 / [input L528](https://github.com/sharpa-robotics/sharpa-urdf-usd-xml/blob/6eea427eb24189519f32b9f21674cd534d3f973c/wave_01/left_sharpa_wave/left_sharpa_wave_with_flange.urdf#L528) | 0.01824 / [input L528](https://github.com/sharpa-robotics/sharpa-urdf-usd-xml/blob/d323b371d02f4fc04a0873c19c5234cae6d803dd/wave_01/left_sharpa_wave/left_sharpa_wave_with_flange.urdf#L528) |
| left_index_DP | 0.00465 / [input L197](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/sharpa_wave/left_hand.xml#L197) | 0.00455 / [input L576](https://github.com/sharpa-robotics/sharpa-urdf-usd-xml/blob/6eea427eb24189519f32b9f21674cd534d3f973c/wave_01/left_sharpa_wave/left_sharpa_wave_with_flange.urdf#L576) | 0.00455 / [input L576](https://github.com/sharpa-robotics/sharpa-urdf-usd-xml/blob/d323b371d02f4fc04a0873c19c5234cae6d803dd/wave_01/left_sharpa_wave/left_sharpa_wave_with_flange.urdf#L576) |
| left_middle_MCP_VL | 0.00221 / [input L210](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/sharpa_wave/left_hand.xml#L210) | 0.00221 / [input L697](https://github.com/sharpa-robotics/sharpa-urdf-usd-xml/blob/6eea427eb24189519f32b9f21674cd534d3f973c/wave_01/left_sharpa_wave/left_sharpa_wave_with_flange.urdf#L697) | 0.00221 / [input L697](https://github.com/sharpa-robotics/sharpa-urdf-usd-xml/blob/d323b371d02f4fc04a0873c19c5234cae6d803dd/wave_01/left_sharpa_wave/left_sharpa_wave_with_flange.urdf#L697) |
| left_middle_PP | 0.04741 / [input L217](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/sharpa_wave/left_hand.xml#L217) | 0.04741 / [input L745](https://github.com/sharpa-robotics/sharpa-urdf-usd-xml/blob/6eea427eb24189519f32b9f21674cd534d3f973c/wave_01/left_sharpa_wave/left_sharpa_wave_with_flange.urdf#L745) | 0.04741 / [input L745](https://github.com/sharpa-robotics/sharpa-urdf-usd-xml/blob/d323b371d02f4fc04a0873c19c5234cae6d803dd/wave_01/left_sharpa_wave/left_sharpa_wave_with_flange.urdf#L745) |
| left_middle_MP | 0.01824 / [input L224](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/sharpa_wave/left_hand.xml#L224) | 0.01824 / [input L793](https://github.com/sharpa-robotics/sharpa-urdf-usd-xml/blob/6eea427eb24189519f32b9f21674cd534d3f973c/wave_01/left_sharpa_wave/left_sharpa_wave_with_flange.urdf#L793) | 0.01824 / [input L793](https://github.com/sharpa-robotics/sharpa-urdf-usd-xml/blob/d323b371d02f4fc04a0873c19c5234cae6d803dd/wave_01/left_sharpa_wave/left_sharpa_wave_with_flange.urdf#L793) |
| left_middle_DP | 0.00465 / [input L231](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/sharpa_wave/left_hand.xml#L231) | 0.00455 / [input L841](https://github.com/sharpa-robotics/sharpa-urdf-usd-xml/blob/6eea427eb24189519f32b9f21674cd534d3f973c/wave_01/left_sharpa_wave/left_sharpa_wave_with_flange.urdf#L841) | 0.00455 / [input L841](https://github.com/sharpa-robotics/sharpa-urdf-usd-xml/blob/d323b371d02f4fc04a0873c19c5234cae6d803dd/wave_01/left_sharpa_wave/left_sharpa_wave_with_flange.urdf#L841) |
| left_ring_MCP_VL | 0.00221 / [input L244](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/sharpa_wave/left_hand.xml#L244) | 0.00221 / [input L962](https://github.com/sharpa-robotics/sharpa-urdf-usd-xml/blob/6eea427eb24189519f32b9f21674cd534d3f973c/wave_01/left_sharpa_wave/left_sharpa_wave_with_flange.urdf#L962) | 0.00221 / [input L962](https://github.com/sharpa-robotics/sharpa-urdf-usd-xml/blob/d323b371d02f4fc04a0873c19c5234cae6d803dd/wave_01/left_sharpa_wave/left_sharpa_wave_with_flange.urdf#L962) |
| left_ring_PP | 0.04741 / [input L251](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/sharpa_wave/left_hand.xml#L251) | 0.04741 / [input L1010](https://github.com/sharpa-robotics/sharpa-urdf-usd-xml/blob/6eea427eb24189519f32b9f21674cd534d3f973c/wave_01/left_sharpa_wave/left_sharpa_wave_with_flange.urdf#L1010) | 0.04741 / [input L1010](https://github.com/sharpa-robotics/sharpa-urdf-usd-xml/blob/d323b371d02f4fc04a0873c19c5234cae6d803dd/wave_01/left_sharpa_wave/left_sharpa_wave_with_flange.urdf#L1010) |
| left_ring_MP | 0.01824 / [input L258](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/sharpa_wave/left_hand.xml#L258) | 0.01824 / [input L1058](https://github.com/sharpa-robotics/sharpa-urdf-usd-xml/blob/6eea427eb24189519f32b9f21674cd534d3f973c/wave_01/left_sharpa_wave/left_sharpa_wave_with_flange.urdf#L1058) | 0.01824 / [input L1058](https://github.com/sharpa-robotics/sharpa-urdf-usd-xml/blob/d323b371d02f4fc04a0873c19c5234cae6d803dd/wave_01/left_sharpa_wave/left_sharpa_wave_with_flange.urdf#L1058) |
| left_ring_DP | 0.00465 / [input L265](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/sharpa_wave/left_hand.xml#L265) | 0.00455 / [input L1106](https://github.com/sharpa-robotics/sharpa-urdf-usd-xml/blob/6eea427eb24189519f32b9f21674cd534d3f973c/wave_01/left_sharpa_wave/left_sharpa_wave_with_flange.urdf#L1106) | 0.00455 / [input L1106](https://github.com/sharpa-robotics/sharpa-urdf-usd-xml/blob/d323b371d02f4fc04a0873c19c5234cae6d803dd/wave_01/left_sharpa_wave/left_sharpa_wave_with_flange.urdf#L1106) |
| left_pinky_MC | 0.12541 / [geometry/inference input L277](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/sharpa_wave/left_hand.xml#L277) | 0.12541 / [input L1227](https://github.com/sharpa-robotics/sharpa-urdf-usd-xml/blob/6eea427eb24189519f32b9f21674cd534d3f973c/wave_01/left_sharpa_wave/left_sharpa_wave_with_flange.urdf#L1227) | 0.12541 / [input L1227](https://github.com/sharpa-robotics/sharpa-urdf-usd-xml/blob/d323b371d02f4fc04a0873c19c5234cae6d803dd/wave_01/left_sharpa_wave/left_sharpa_wave_with_flange.urdf#L1227) |
| left_pinky_MCP_VL | 0.00221 / [input L283](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/sharpa_wave/left_hand.xml#L283) | 0.00221 / [input L1275](https://github.com/sharpa-robotics/sharpa-urdf-usd-xml/blob/6eea427eb24189519f32b9f21674cd534d3f973c/wave_01/left_sharpa_wave/left_sharpa_wave_with_flange.urdf#L1275) | 0.00221 / [input L1275](https://github.com/sharpa-robotics/sharpa-urdf-usd-xml/blob/d323b371d02f4fc04a0873c19c5234cae6d803dd/wave_01/left_sharpa_wave/left_sharpa_wave_with_flange.urdf#L1275) |
| left_pinky_PP | 0.04741 / [input L290](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/sharpa_wave/left_hand.xml#L290) | 0.04741 / [input L1323](https://github.com/sharpa-robotics/sharpa-urdf-usd-xml/blob/6eea427eb24189519f32b9f21674cd534d3f973c/wave_01/left_sharpa_wave/left_sharpa_wave_with_flange.urdf#L1323) | 0.04741 / [input L1323](https://github.com/sharpa-robotics/sharpa-urdf-usd-xml/blob/d323b371d02f4fc04a0873c19c5234cae6d803dd/wave_01/left_sharpa_wave/left_sharpa_wave_with_flange.urdf#L1323) |
| left_pinky_MP | 0.01824 / [input L297](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/sharpa_wave/left_hand.xml#L297) | 0.01824 / [input L1371](https://github.com/sharpa-robotics/sharpa-urdf-usd-xml/blob/6eea427eb24189519f32b9f21674cd534d3f973c/wave_01/left_sharpa_wave/left_sharpa_wave_with_flange.urdf#L1371) | 0.01824 / [input L1371](https://github.com/sharpa-robotics/sharpa-urdf-usd-xml/blob/d323b371d02f4fc04a0873c19c5234cae6d803dd/wave_01/left_sharpa_wave/left_sharpa_wave_with_flange.urdf#L1371) |
| left_pinky_DP | 0.00465 / [input L304](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/sharpa_wave/left_hand.xml#L304) | 0.00455 / [input L1419](https://github.com/sharpa-robotics/sharpa-urdf-usd-xml/blob/6eea427eb24189519f32b9f21674cd534d3f973c/wave_01/left_sharpa_wave/left_sharpa_wave_with_flange.urdf#L1419) | 0.00455 / [input L1419](https://github.com/sharpa-robotics/sharpa-urdf-usd-xml/blob/d323b371d02f4fc04a0873c19c5234cae6d803dd/wave_01/left_sharpa_wave/left_sharpa_wave_with_flange.urdf#L1419) |
| upstream-only left_hand_flange | unavailable | unavailable | 0.016 / [input L12](https://github.com/sharpa-robotics/sharpa-urdf-usd-xml/blob/d323b371d02f4fc04a0873c19c5234cae6d803dd/wave_01/left_sharpa_wave/left_sharpa_wave_with_flange.urdf#L12) |
| upstream-only left_hand_wrist | unavailable | unavailable | 0.0505 / [input L50](https://github.com/sharpa-robotics/sharpa-urdf-usd-xml/blob/d323b371d02f4fc04a0873c19c5234cae6d803dd/wave_01/left_sharpa_wave/left_sharpa_wave_with_flange.urdf#L50) |
| upstream-only left_index_elastomer | unavailable | unavailable | 0.0001 / [input L624](https://github.com/sharpa-robotics/sharpa-urdf-usd-xml/blob/d323b371d02f4fc04a0873c19c5234cae6d803dd/wave_01/left_sharpa_wave/left_sharpa_wave_with_flange.urdf#L624) |
| upstream-only left_index_fingertip | unavailable | unavailable | 1e-06 / [input L671](https://github.com/sharpa-robotics/sharpa-urdf-usd-xml/blob/d323b371d02f4fc04a0873c19c5234cae6d803dd/wave_01/left_sharpa_wave/left_sharpa_wave_with_flange.urdf#L671) |
| upstream-only left_middle_elastomer | unavailable | unavailable | 0.0001 / [input L889](https://github.com/sharpa-robotics/sharpa-urdf-usd-xml/blob/d323b371d02f4fc04a0873c19c5234cae6d803dd/wave_01/left_sharpa_wave/left_sharpa_wave_with_flange.urdf#L889) |
| upstream-only left_middle_fingertip | unavailable | unavailable | 1e-06 / [input L936](https://github.com/sharpa-robotics/sharpa-urdf-usd-xml/blob/d323b371d02f4fc04a0873c19c5234cae6d803dd/wave_01/left_sharpa_wave/left_sharpa_wave_with_flange.urdf#L936) |
| upstream-only left_pinky_elastomer | unavailable | unavailable | 0.0001 / [input L1467](https://github.com/sharpa-robotics/sharpa-urdf-usd-xml/blob/d323b371d02f4fc04a0873c19c5234cae6d803dd/wave_01/left_sharpa_wave/left_sharpa_wave_with_flange.urdf#L1467) |
| upstream-only left_pinky_fingertip | unavailable | unavailable | 1e-06 / [input L1514](https://github.com/sharpa-robotics/sharpa-urdf-usd-xml/blob/d323b371d02f4fc04a0873c19c5234cae6d803dd/wave_01/left_sharpa_wave/left_sharpa_wave_with_flange.urdf#L1514) |
| upstream-only left_ring_elastomer | unavailable | unavailable | 0.0001 / [input L1154](https://github.com/sharpa-robotics/sharpa-urdf-usd-xml/blob/d323b371d02f4fc04a0873c19c5234cae6d803dd/wave_01/left_sharpa_wave/left_sharpa_wave_with_flange.urdf#L1154) |
| upstream-only left_ring_fingertip | unavailable | unavailable | 1e-06 / [input L1201](https://github.com/sharpa-robotics/sharpa-urdf-usd-xml/blob/d323b371d02f4fc04a0873c19c5234cae6d803dd/wave_01/left_sharpa_wave/left_sharpa_wave_with_flange.urdf#L1201) |
| upstream-only left_thumb_elastomer | unavailable | unavailable | 0.0001 / [input L358](https://github.com/sharpa-robotics/sharpa-urdf-usd-xml/blob/d323b371d02f4fc04a0873c19c5234cae6d803dd/wave_01/left_sharpa_wave/left_sharpa_wave_with_flange.urdf#L358) |
| upstream-only left_thumb_fingertip | unavailable | unavailable | 1e-06 / [input L405](https://github.com/sharpa-robotics/sharpa-urdf-usd-xml/blob/d323b371d02f4fc04a0873c19c5234cae6d803dd/wave_01/left_sharpa_wave/left_sharpa_wave_with_flange.urdf#L405) |

## Coverage and unmatched elements

```json
{
  "mapping_h": {
    "bodies": {
      "left_hand_C_MC": "left_hand_C_MC",
      "left_thumb_CMC_VL": "left_thumb_CMC_VL",
      "left_thumb_MC": "left_thumb_MC",
      "left_thumb_MCP_VL": "left_thumb_MCP_VL",
      "left_thumb_PP": "left_thumb_PP",
      "left_thumb_DP": "left_thumb_DP",
      "left_index_MCP_VL": "left_index_MCP_VL",
      "left_index_PP": "left_index_PP",
      "left_index_MP": "left_index_MP",
      "left_index_DP": "left_index_DP",
      "left_middle_MCP_VL": "left_middle_MCP_VL",
      "left_middle_PP": "left_middle_PP",
      "left_middle_MP": "left_middle_MP",
      "left_middle_DP": "left_middle_DP",
      "left_ring_MCP_VL": "left_ring_MCP_VL",
      "left_ring_PP": "left_ring_PP",
      "left_ring_MP": "left_ring_MP",
      "left_ring_DP": "left_ring_DP",
      "left_pinky_MC": "left_pinky_MC",
      "left_pinky_MCP_VL": "left_pinky_MCP_VL",
      "left_pinky_PP": "left_pinky_PP",
      "left_pinky_MP": "left_pinky_MP",
      "left_pinky_DP": "left_pinky_DP"
    },
    "joints": {
      "left_thumb_CMC_FE": "left_thumb_CMC_FE",
      "left_thumb_CMC_AA": "left_thumb_CMC_AA",
      "left_thumb_MCP_FE": "left_thumb_MCP_FE",
      "left_thumb_MCP_AA": "left_thumb_MCP_AA",
      "left_thumb_IP": "left_thumb_IP",
      "left_index_MCP_FE": "left_index_MCP_FE",
      "left_index_MCP_AA": "left_index_MCP_AA",
      "left_index_PIP": "left_index_PIP",
      "left_index_DIP": "left_index_DIP",
      "left_middle_MCP_FE": "left_middle_MCP_FE",
      "left_middle_MCP_AA": "left_middle_MCP_AA",
      "left_middle_PIP": "left_middle_PIP",
      "left_middle_DIP": "left_middle_DIP",
      "left_ring_MCP_FE": "left_ring_MCP_FE",
      "left_ring_MCP_AA": "left_ring_MCP_AA",
      "left_ring_PIP": "left_ring_PIP",
      "left_ring_DIP": "left_ring_DIP",
      "left_pinky_CMC": "left_pinky_CMC",
      "left_pinky_MCP_FE": "left_pinky_MCP_FE",
      "left_pinky_MCP_AA": "left_pinky_MCP_AA",
      "left_pinky_PIP": "left_pinky_PIP",
      "left_pinky_DIP": "left_pinky_DIP"
    },
    "body_methods": {
      "left_hand_C_MC": "name",
      "left_thumb_CMC_VL": "name",
      "left_thumb_MC": "name",
      "left_thumb_MCP_VL": "name",
      "left_thumb_PP": "name",
      "left_thumb_DP": "name",
      "left_index_MCP_VL": "name",
      "left_index_PP": "name",
      "left_index_MP": "name",
      "left_index_DP": "name",
      "left_middle_MCP_VL": "name",
      "left_middle_PP": "name",
      "left_middle_MP": "name",
      "left_middle_DP": "name",
      "left_ring_MCP_VL": "name",
      "left_ring_PP": "name",
      "left_ring_MP": "name",
      "left_ring_DP": "name",
      "left_pinky_MC": "name",
      "left_pinky_MCP_VL": "name",
      "left_pinky_PP": "name",
      "left_pinky_MP": "name",
      "left_pinky_DP": "name"
    },
    "joint_methods": {
      "left_thumb_CMC_FE": "name",
      "left_thumb_CMC_AA": "name",
      "left_thumb_MCP_FE": "name",
      "left_thumb_MCP_AA": "name",
      "left_thumb_IP": "name",
      "left_index_MCP_FE": "name",
      "left_index_MCP_AA": "name",
      "left_index_PIP": "name",
      "left_index_DIP": "name",
      "left_middle_MCP_FE": "name",
      "left_middle_MCP_AA": "name",
      "left_middle_PIP": "name",
      "left_middle_DIP": "name",
      "left_ring_MCP_FE": "name",
      "left_ring_MCP_AA": "name",
      "left_ring_PIP": "name",
      "left_ring_DIP": "name",
      "left_pinky_CMC": "name",
      "left_pinky_MCP_FE": "name",
      "left_pinky_MCP_AA": "name",
      "left_pinky_PIP": "name",
      "left_pinky_DIP": "name"
    },
    "unmatched_m_bodies": [],
    "unmatched_upstream_bodies": [
      "left_hand_flange",
      "left_hand_wrist",
      "left_index_elastomer",
      "left_index_fingertip",
      "left_middle_elastomer",
      "left_middle_fingertip",
      "left_pinky_elastomer",
      "left_pinky_fingertip",
      "left_ring_elastomer",
      "left_ring_fingertip",
      "left_thumb_elastomer",
      "left_thumb_fingertip"
    ],
    "unmatched_m_joints": [],
    "unmatched_upstream_joints": [],
    "registration_anchor": {
      "M": "left_hand_C_MC",
      "H": "left_hand_C_MC",
      "root_unmatched": false
    }
  },
  "mapping_s": {
    "bodies": {
      "left_hand_C_MC": "left_hand_C_MC",
      "left_thumb_CMC_VL": "left_thumb_CMC_VL",
      "left_thumb_MC": "left_thumb_MC",
      "left_thumb_MCP_VL": "left_thumb_MCP_VL",
      "left_thumb_PP": "left_thumb_PP",
      "left_thumb_DP": "left_thumb_DP",
      "left_index_MCP_VL": "left_index_MCP_VL",
      "left_index_PP": "left_index_PP",
      "left_index_MP": "left_index_MP",
      "left_index_DP": "left_index_DP",
      "left_middle_MCP_VL": "left_middle_MCP_VL",
      "left_middle_PP": "left_middle_PP",
      "left_middle_MP": "left_middle_MP",
      "left_middle_DP": "left_middle_DP",
      "left_ring_MCP_VL": "left_ring_MCP_VL",
      "left_ring_PP": "left_ring_PP",
      "left_ring_MP": "left_ring_MP",
      "left_ring_DP": "left_ring_DP",
      "left_pinky_MC": "left_pinky_MC",
      "left_pinky_MCP_VL": "left_pinky_MCP_VL",
      "left_pinky_PP": "left_pinky_PP",
      "left_pinky_MP": "left_pinky_MP",
      "left_pinky_DP": "left_pinky_DP"
    },
    "joints": {
      "left_thumb_CMC_FE": "left_thumb_CMC_FE",
      "left_thumb_CMC_AA": "left_thumb_CMC_AA",
      "left_thumb_MCP_FE": "left_thumb_MCP_FE",
      "left_thumb_MCP_AA": "left_thumb_MCP_AA",
      "left_thumb_IP": "left_thumb_IP",
      "left_index_MCP_FE": "left_index_MCP_FE",
      "left_index_MCP_AA": "left_index_MCP_AA",
      "left_index_PIP": "left_index_PIP",
      "left_index_DIP": "left_index_DIP",
      "left_middle_MCP_FE": "left_middle_MCP_FE",
      "left_middle_MCP_AA": "left_middle_MCP_AA",
      "left_middle_PIP": "left_middle_PIP",
      "left_middle_DIP": "left_middle_DIP",
      "left_ring_MCP_FE": "left_ring_MCP_FE",
      "left_ring_MCP_AA": "left_ring_MCP_AA",
      "left_ring_PIP": "left_ring_PIP",
      "left_ring_DIP": "left_ring_DIP",
      "left_pinky_CMC": "left_pinky_CMC",
      "left_pinky_MCP_FE": "left_pinky_MCP_FE",
      "left_pinky_MCP_AA": "left_pinky_MCP_AA",
      "left_pinky_PIP": "left_pinky_PIP",
      "left_pinky_DIP": "left_pinky_DIP"
    },
    "body_methods": {
      "left_hand_C_MC": "name",
      "left_thumb_CMC_VL": "name",
      "left_thumb_MC": "name",
      "left_thumb_MCP_VL": "name",
      "left_thumb_PP": "name",
      "left_thumb_DP": "name",
      "left_index_MCP_VL": "name",
      "left_index_PP": "name",
      "left_index_MP": "name",
      "left_index_DP": "name",
      "left_middle_MCP_VL": "name",
      "left_middle_PP": "name",
      "left_middle_MP": "name",
      "left_middle_DP": "name",
      "left_ring_MCP_VL": "name",
      "left_ring_PP": "name",
      "left_ring_MP": "name",
      "left_ring_DP": "name",
      "left_pinky_MC": "name",
      "left_pinky_MCP_VL": "name",
      "left_pinky_PP": "name",
      "left_pinky_MP": "name",
      "left_pinky_DP": "name"
    },
    "joint_methods": {
      "left_thumb_CMC_FE": "name",
      "left_thumb_CMC_AA": "name",
      "left_thumb_MCP_FE": "name",
      "left_thumb_MCP_AA": "name",
      "left_thumb_IP": "name",
      "left_index_MCP_FE": "name",
      "left_index_MCP_AA": "name",
      "left_index_PIP": "name",
      "left_index_DIP": "name",
      "left_middle_MCP_FE": "name",
      "left_middle_MCP_AA": "name",
      "left_middle_PIP": "name",
      "left_middle_DIP": "name",
      "left_ring_MCP_FE": "name",
      "left_ring_MCP_AA": "name",
      "left_ring_PIP": "name",
      "left_ring_DIP": "name",
      "left_pinky_CMC": "name",
      "left_pinky_MCP_FE": "name",
      "left_pinky_MCP_AA": "name",
      "left_pinky_PIP": "name",
      "left_pinky_DIP": "name"
    },
    "unmatched_m_bodies": [],
    "unmatched_upstream_bodies": [
      "left_hand_flange",
      "left_hand_wrist",
      "left_index_elastomer",
      "left_index_fingertip",
      "left_middle_elastomer",
      "left_middle_fingertip",
      "left_pinky_elastomer",
      "left_pinky_fingertip",
      "left_ring_elastomer",
      "left_ring_fingertip",
      "left_thumb_elastomer",
      "left_thumb_fingertip"
    ],
    "unmatched_m_joints": [],
    "unmatched_upstream_joints": [],
    "registration_anchor": {
      "M": "left_hand_C_MC",
      "S": "left_hand_C_MC"
    }
  },
  "unavailable": [
    {
      "entity": "left_thumb_CMC_FE",
      "other_entity": "left_thumb_CMC_FE",
      "quantity": "force",
      "tolerance": "limit",
      "m": 3.3,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_thumb_CMC_FE",
      "other_entity": "left_thumb_CMC_FE",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 11.84076833,
      "s": 11.84076833,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_thumb_CMC_AA",
      "other_entity": "left_thumb_CMC_AA",
      "quantity": "force",
      "tolerance": "limit",
      "m": 3.3,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_thumb_CMC_AA",
      "other_entity": "left_thumb_CMC_AA",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 11.84076833,
      "s": 11.84076833,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_thumb_MCP_FE",
      "other_entity": "left_thumb_MCP_FE",
      "quantity": "force",
      "tolerance": "limit",
      "m": 1.864,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_thumb_MCP_FE",
      "other_entity": "left_thumb_MCP_FE",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 16.07692878,
      "s": 16.07692878,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_thumb_MCP_AA",
      "other_entity": "left_thumb_MCP_AA",
      "quantity": "force",
      "tolerance": "limit",
      "m": 1.864,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_thumb_MCP_AA",
      "other_entity": "left_thumb_MCP_AA",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 16.07692878,
      "s": 16.07692878,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_thumb_IP",
      "other_entity": "left_thumb_IP",
      "quantity": "force",
      "tolerance": "limit",
      "m": 0.638,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_thumb_IP",
      "other_entity": "left_thumb_IP",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 11.61831603,
      "s": 11.61831603,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_index_MCP_FE",
      "other_entity": "left_index_MCP_FE",
      "quantity": "force",
      "tolerance": "limit",
      "m": 1.864,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_index_MCP_FE",
      "other_entity": "left_index_MCP_FE",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 16.07692878,
      "s": 16.07692878,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_index_MCP_AA",
      "other_entity": "left_index_MCP_AA",
      "quantity": "force",
      "tolerance": "limit",
      "m": 1.864,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_index_MCP_AA",
      "other_entity": "left_index_MCP_AA",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 16.07692878,
      "s": 16.07692878,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_index_PIP",
      "other_entity": "left_index_PIP",
      "quantity": "force",
      "tolerance": "limit",
      "m": 0.638,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_index_PIP",
      "other_entity": "left_index_PIP",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 11.61831603,
      "s": 11.61831603,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_index_DIP",
      "other_entity": "left_index_DIP",
      "quantity": "force",
      "tolerance": "limit",
      "m": 0.189369,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_index_DIP",
      "other_entity": "left_index_DIP",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 14.66594768,
      "s": 14.66594768,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_middle_MCP_FE",
      "other_entity": "left_middle_MCP_FE",
      "quantity": "force",
      "tolerance": "limit",
      "m": 1.864,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_middle_MCP_FE",
      "other_entity": "left_middle_MCP_FE",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 16.07692878,
      "s": 16.07692878,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_middle_MCP_AA",
      "other_entity": "left_middle_MCP_AA",
      "quantity": "force",
      "tolerance": "limit",
      "m": 1.864,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_middle_MCP_AA",
      "other_entity": "left_middle_MCP_AA",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 16.07692878,
      "s": 16.07692878,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_middle_PIP",
      "other_entity": "left_middle_PIP",
      "quantity": "force",
      "tolerance": "limit",
      "m": 0.638,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_middle_PIP",
      "other_entity": "left_middle_PIP",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 11.61831603,
      "s": 11.61831603,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_middle_DIP",
      "other_entity": "left_middle_DIP",
      "quantity": "force",
      "tolerance": "limit",
      "m": 0.189369,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_middle_DIP",
      "other_entity": "left_middle_DIP",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 14.66594768,
      "s": 14.66594768,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_ring_MCP_FE",
      "other_entity": "left_ring_MCP_FE",
      "quantity": "force",
      "tolerance": "limit",
      "m": 1.864,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_ring_MCP_FE",
      "other_entity": "left_ring_MCP_FE",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 16.07692878,
      "s": 16.07692878,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_ring_MCP_AA",
      "other_entity": "left_ring_MCP_AA",
      "quantity": "force",
      "tolerance": "limit",
      "m": 1.864,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_ring_MCP_AA",
      "other_entity": "left_ring_MCP_AA",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 16.07692878,
      "s": 16.07692878,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_ring_PIP",
      "other_entity": "left_ring_PIP",
      "quantity": "force",
      "tolerance": "limit",
      "m": 0.638,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_ring_PIP",
      "other_entity": "left_ring_PIP",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 11.61831603,
      "s": 11.61831603,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_ring_DIP",
      "other_entity": "left_ring_DIP",
      "quantity": "force",
      "tolerance": "limit",
      "m": 0.189369,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_ring_DIP",
      "other_entity": "left_ring_DIP",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 14.66594768,
      "s": 14.66594768,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_pinky_CMC",
      "other_entity": "left_pinky_CMC",
      "quantity": "force",
      "tolerance": "limit",
      "m": 0.5285,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_pinky_CMC",
      "other_entity": "left_pinky_CMC",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 35.07416159,
      "s": 35.07416159,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_pinky_MCP_FE",
      "other_entity": "left_pinky_MCP_FE",
      "quantity": "force",
      "tolerance": "limit",
      "m": 1.864,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_pinky_MCP_FE",
      "other_entity": "left_pinky_MCP_FE",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 16.07692878,
      "s": 16.07692878,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_pinky_MCP_AA",
      "other_entity": "left_pinky_MCP_AA",
      "quantity": "force",
      "tolerance": "limit",
      "m": 1.864,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_pinky_MCP_AA",
      "other_entity": "left_pinky_MCP_AA",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 16.07692878,
      "s": 16.07692878,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_pinky_PIP",
      "other_entity": "left_pinky_PIP",
      "quantity": "force",
      "tolerance": "limit",
      "m": 0.638,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_pinky_PIP",
      "other_entity": "left_pinky_PIP",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 11.61831603,
      "s": 11.61831603,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_pinky_DIP",
      "other_entity": "left_pinky_DIP",
      "quantity": "force",
      "tolerance": "limit",
      "m": 0.189369,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "left_pinky_DIP",
      "other_entity": "left_pinky_DIP",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 14.66594768,
      "s": 14.66594768,
      "reason": "quantity absent or not enforced/declared on one side"
    }
  ]
}
```

## Limits unavailable for a like-for-like simulator comparison

URDF effort and velocity tags are manufacturer declarations; MuJoCo ignores them. Missing enforced quantities are not interpreted as zero. The available values are shown for review and excluded from STALE counts.

| Joint / quantity | M | S | H / declared upstream |
|---|---|---|---|
| left_thumb_CMC_FE / force | 3.3 | unavailable | unavailable |
| left_thumb_CMC_FE / velocity | unavailable | 11.8407683 | 11.8407683 |
| left_thumb_CMC_AA / force | 3.3 | unavailable | unavailable |
| left_thumb_CMC_AA / velocity | unavailable | 11.8407683 | 11.8407683 |
| left_thumb_MCP_FE / force | 1.864 | unavailable | unavailable |
| left_thumb_MCP_FE / velocity | unavailable | 16.0769288 | 16.0769288 |
| left_thumb_MCP_AA / force | 1.864 | unavailable | unavailable |
| left_thumb_MCP_AA / velocity | unavailable | 16.0769288 | 16.0769288 |
| left_thumb_IP / force | 0.638 | unavailable | unavailable |
| left_thumb_IP / velocity | unavailable | 11.618316 | 11.618316 |
| left_index_MCP_FE / force | 1.864 | unavailable | unavailable |
| left_index_MCP_FE / velocity | unavailable | 16.0769288 | 16.0769288 |
| left_index_MCP_AA / force | 1.864 | unavailable | unavailable |
| left_index_MCP_AA / velocity | unavailable | 16.0769288 | 16.0769288 |
| left_index_PIP / force | 0.638 | unavailable | unavailable |
| left_index_PIP / velocity | unavailable | 11.618316 | 11.618316 |
| left_index_DIP / force | 0.189369 | unavailable | unavailable |
| left_index_DIP / velocity | unavailable | 14.6659477 | 14.6659477 |
| left_middle_MCP_FE / force | 1.864 | unavailable | unavailable |
| left_middle_MCP_FE / velocity | unavailable | 16.0769288 | 16.0769288 |
| left_middle_MCP_AA / force | 1.864 | unavailable | unavailable |
| left_middle_MCP_AA / velocity | unavailable | 16.0769288 | 16.0769288 |
| left_middle_PIP / force | 0.638 | unavailable | unavailable |
| left_middle_PIP / velocity | unavailable | 11.618316 | 11.618316 |
| left_middle_DIP / force | 0.189369 | unavailable | unavailable |
| left_middle_DIP / velocity | unavailable | 14.6659477 | 14.6659477 |
| left_ring_MCP_FE / force | 1.864 | unavailable | unavailable |
| left_ring_MCP_FE / velocity | unavailable | 16.0769288 | 16.0769288 |
| left_ring_MCP_AA / force | 1.864 | unavailable | unavailable |
| left_ring_MCP_AA / velocity | unavailable | 16.0769288 | 16.0769288 |
| left_ring_PIP / force | 0.638 | unavailable | unavailable |
| left_ring_PIP / velocity | unavailable | 11.618316 | 11.618316 |
| left_ring_DIP / force | 0.189369 | unavailable | unavailable |
| left_ring_DIP / velocity | unavailable | 14.6659477 | 14.6659477 |
| left_pinky_CMC / force | 0.5285 | unavailable | unavailable |
| left_pinky_CMC / velocity | unavailable | 35.0741616 | 35.0741616 |
| left_pinky_MCP_FE / force | 1.864 | unavailable | unavailable |
| left_pinky_MCP_FE / velocity | unavailable | 16.0769288 | 16.0769288 |
| left_pinky_MCP_AA / force | 1.864 | unavailable | unavailable |
| left_pinky_MCP_AA / velocity | unavailable | 16.0769288 | 16.0769288 |
| left_pinky_PIP / force | 0.638 | unavailable | unavailable |
| left_pinky_PIP / velocity | unavailable | 11.618316 | 11.618316 |
| left_pinky_DIP / force | 0.189369 | unavailable | unavailable |
| left_pinky_DIP / velocity | unavailable | 14.6659477 | 14.6659477 |
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
    "file": "sharpa_wave/left_hand.xml",
    "status": "passed",
    "findings": 0
  },
  {
    "file": "sharpa_wave/right_hand.xml",
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
      "undocumented derivation difference": 19
    },
    "classifications_changed": 6,
    "finding_membership_changes": 6
  },
  "2": {
    "provenance_method": "pinned",
    "counts": {
      "undocumented derivation difference": 13
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
      "left_hand_C_MC",
      "left_thumb_MCP_VL",
      "left_pinky_MC"
    ],
    "assets_loaded": 54,
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
  "self_variants_recompiled": 2,
  "historical_snapshots_reused": 1,
  "primary_physics_unchanged": true,
  "source_matching": "original raw-value provenance criteria retained; kinematic guard applies to reported CoM"
}
```
