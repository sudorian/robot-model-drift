# arx_l5

Status: **complete**. Provenance: **pinned**, confidence **high**.

Source selected using the ordered amended provenance rules.

M: `https://github.com/google-deepmind/mujoco_menagerie`, `arx_l5/arx_l5.xml`, commit `370c43965323c0944b433b202aac5058b5f907a9`.
H: `https://github.com/ARXroboticsX/ARX_Model`, `X5/X5A/urdf/X5A.urdf`, commit `e58172bd0874ff8c940700dc87f64a9ce951718d`.
S: `af6fe43c873008a85bce6195c0f2160f1a1c14ce` (2024-12-06T15:49:46+08:00). Menagerie release/change: 2025-03-19T21:50:12-07:00.

Limit semantics: MJCF effort values are supported actuator torque/force envelopes. URDF effort and velocity values are manufacturer declarations retained from XML; MuJoCo does not enforce those tags. Such declaration comparisons are explicitly distinct from compiled inertial/range quantities.


## Source evidence

```json
[
  {
    "url": "https://github.com/ARXroboticsX/ARX_Model",
    "document": "arx_l5/README.md",
    "commit": "370c43965323c0944b433b202aac5058b5f907a9",
    "current": true
  },
  {
    "url": "https://github.com/ARXroboticsX/ARX_Model/tree/af6fe43c873008a85bce6195c0f2160f1a1c14ce/X5/X5A",
    "document": "arx_l5/README.md",
    "commit": "370c43965323c0944b433b202aac5058b5f907a9",
    "current": true
  },
  {
    "url": "https://github.com/ARXroboticsX/ARX_Model/tree/master/X5/X5A/urdf",
    "document": "arx_l5/README.md",
    "commit": "46c6ec86cd03ceb023450b2003c762ee07f17281",
    "current": false
  }
]
```


## README derivation evidence

Documentation labels are conservative: an automated documented label requires an explicit affected entity and quantity. Broader conversion notes are retained here for review.

> 1.  Added `<mujoco> <compiler balanceinertia="true" discardvisual="false"/> </mujoco>` to the URDF's
> 4.  Merged similar materials between the .objs.

## Kinematics consistency

A proper Kabsch rigid transform aligns all matched zero-pose body origins. The maximum per-origin residual and signed hinge/slide axis angles determine whether CoM can be compared; RMS is also recorded. Fewer than three non-collinear origins give insufficient kinematic coverage. CoM records that fail either required M/H or M/S check are excluded from counts and largest discrepancies. Masses, principal moments and raw joint ranges remain unchanged; a flagged range still requires convention review.

| Pair | Status | Origins / rank | RMS / maximum mm | Disagreeing / checked axes |
|---|---|---:|---:|---:|
| M/H | kinematic convention differs | 9 / 3 | 4.08905718 / 7.8272435 | 1 / 8 |
| M/S | kinematic convention differs | 9 / 3 | 4.08905718 / 7.8272435 | 1 / 8 |

Exact fitted transforms, per-origin residuals, thresholds and axis vectors:

```json
{
  "M/H": {
    "status": "kinematic convention differs",
    "matched_body_origins": 9,
    "position_threshold_m": 0.005,
    "axis_threshold_rad": 0.005,
    "residual_definition": "maximum Euclidean residual over matched body origins; Kabsch minimizes RMS, which is also recorded",
    "coordinate_frames": "each snapshot registered to its matched report anchor",
    "anchor_m": "base_link",
    "anchor_other": "base_link",
    "rotation_other_to_m": [
      [
        0.999990322705605,
        -0.001077827684379565,
        -0.004265299827956173
      ],
      [
        0.0010859936926457894,
        0.9999975811549642,
        0.0019126687953275507
      ],
      [
        0.004263227983478123,
        -0.0019172823745790262,
        0.9999890743980441
      ]
    ],
    "translation_other_to_m": [
      0.002053855492576792,
      -4.94061214944694e-05,
      0.003618825388848501
    ],
    "rms_residual_m": 0.004089057178326385,
    "max_residual_m": 0.007827243499679793,
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
          -0.004265299827956174,
          0.001912668795327551,
          0.9999890743980442
        ],
        "angle_rad": 0.004674531388435576,
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
          -0.001077827684379565,
          0.9999975811549642,
          -0.0019172823745790262
        ],
        "angle_rad": 0.0021994753970366217,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "joint3",
        "joint_other": "joint3",
        "axis_m": [
          0.0,
          -0.9999999999730151,
          7.346419999900879e-06
        ],
        "axis_other_aligned": [
          0.00107785901899267,
          -0.9999975951792288,
          0.0019099360445845983
        ],
        "angle_rad": 0.002186695002228286,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "joint4",
        "joint_other": "joint4",
        "axis_m": [
          0.0,
          -0.9999999999730151,
          7.346419999900879e-06
        ],
        "axis_other_aligned": [
          0.00107785901899267,
          -0.9999975951792288,
          0.0019099360445845983
        ],
        "angle_rad": 0.002186695002228286,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "joint5",
        "joint_other": "joint5",
        "axis_m": [
          0.0,
          -7.346419999900879e-06,
          -0.9999999999730151
        ],
        "axis_other_aligned": [
          0.004265291909676773,
          -0.001905322402839122,
          -0.9999890884562024
        ],
        "angle_rad": 0.0046685315199969935,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "joint6",
        "joint_other": "joint6",
        "axis_m": [
          1.0,
          0.0,
          0.0
        ],
        "axis_other_aligned": [
          0.9999903227056053,
          0.0010859936926457898,
          0.004263227983478125
        ],
        "angle_rad": 0.00439938859460725,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "joint7",
        "joint_other": "joint7",
        "axis_m": [
          0.0,
          1.0,
          2.210291451038415e-22
        ],
        "axis_other_aligned": [
          -0.001077827684379565,
          0.9999975811549642,
          -0.0019172823745790262
        ],
        "angle_rad": 0.0021994753970366217,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "joint8",
        "joint_other": "joint8",
        "axis_m": [
          0.0,
          1.0,
          2.210291451038415e-22
        ],
        "axis_other_aligned": [
          0.001077827684379565,
          -0.9999975811549642,
          0.0019172823745790262
        ],
        "angle_rad": 3.1393931781927567,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      }
    ],
    "axis_disagreements": [
      {
        "joint_m": "joint8",
        "joint_other": "joint8",
        "axis_m": [
          0.0,
          1.0,
          2.210291451038415e-22
        ],
        "axis_other_aligned": [
          0.001077827684379565,
          -0.9999975811549642,
          0.0019172823745790262
        ],
        "angle_rad": 3.1393931781927567,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      }
    ],
    "com_eligible": false,
    "covariance_singular_values": [
      0.1409905667696571,
      0.031706567409211545,
      0.0012398301866632518
    ],
    "origin_residuals_m": {
      "base_link": 0.004161329179986064,
      "link1": 0.007827243499679793,
      "link2": 0.001778171204090636,
      "link3": 0.0016859309776255849,
      "link4": 0.0036574635928367854,
      "link5": 0.005146787665919967,
      "link6": 0.0031710865781215576,
      "link7": 0.0028800977064835816,
      "link8": 0.0027712134405198634
    },
    "reason": "Origin residual exceeds threshold and/or matched signed joint axes disagree"
  },
  "M/S": {
    "status": "kinematic convention differs",
    "matched_body_origins": 9,
    "position_threshold_m": 0.005,
    "axis_threshold_rad": 0.005,
    "residual_definition": "maximum Euclidean residual over matched body origins; Kabsch minimizes RMS, which is also recorded",
    "coordinate_frames": "each snapshot registered to its matched report anchor",
    "anchor_m": "base_link",
    "anchor_other": "base_link",
    "rotation_other_to_m": [
      [
        0.999990322705605,
        -0.001077827684379565,
        -0.004265299827956173
      ],
      [
        0.0010859936926457894,
        0.9999975811549642,
        0.0019126687953275507
      ],
      [
        0.004263227983478123,
        -0.0019172823745790262,
        0.9999890743980441
      ]
    ],
    "translation_other_to_m": [
      0.002053855492576792,
      -4.94061214944694e-05,
      0.003618825388848501
    ],
    "rms_residual_m": 0.004089057178326385,
    "max_residual_m": 0.007827243499679793,
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
          -0.004265299827956174,
          0.001912668795327551,
          0.9999890743980442
        ],
        "angle_rad": 0.004674531388435576,
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
          -0.001077827684379565,
          0.9999975811549642,
          -0.0019172823745790262
        ],
        "angle_rad": 0.0021994753970366217,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "joint3",
        "joint_other": "joint3",
        "axis_m": [
          0.0,
          -0.9999999999730151,
          7.346419999900879e-06
        ],
        "axis_other_aligned": [
          0.00107785901899267,
          -0.9999975951792288,
          0.0019099360445845983
        ],
        "angle_rad": 0.002186695002228286,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "joint4",
        "joint_other": "joint4",
        "axis_m": [
          0.0,
          -0.9999999999730151,
          7.346419999900879e-06
        ],
        "axis_other_aligned": [
          0.00107785901899267,
          -0.9999975951792288,
          0.0019099360445845983
        ],
        "angle_rad": 0.002186695002228286,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "joint5",
        "joint_other": "joint5",
        "axis_m": [
          0.0,
          -7.346419999900879e-06,
          -0.9999999999730151
        ],
        "axis_other_aligned": [
          0.004265291909676773,
          -0.001905322402839122,
          -0.9999890884562024
        ],
        "angle_rad": 0.0046685315199969935,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "joint6",
        "joint_other": "joint6",
        "axis_m": [
          1.0,
          0.0,
          0.0
        ],
        "axis_other_aligned": [
          0.9999903227056053,
          0.0010859936926457898,
          0.004263227983478125
        ],
        "angle_rad": 0.00439938859460725,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "joint7",
        "joint_other": "joint7",
        "axis_m": [
          0.0,
          1.0,
          2.210291451038415e-22
        ],
        "axis_other_aligned": [
          -0.001077827684379565,
          0.9999975811549642,
          -0.0019172823745790262
        ],
        "angle_rad": 0.0021994753970366217,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "joint8",
        "joint_other": "joint8",
        "axis_m": [
          0.0,
          1.0,
          2.210291451038415e-22
        ],
        "axis_other_aligned": [
          0.001077827684379565,
          -0.9999975811549642,
          0.0019172823745790262
        ],
        "angle_rad": 3.1393931781927567,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      }
    ],
    "axis_disagreements": [
      {
        "joint_m": "joint8",
        "joint_other": "joint8",
        "axis_m": [
          0.0,
          1.0,
          2.210291451038415e-22
        ],
        "axis_other_aligned": [
          0.001077827684379565,
          -0.9999975811549642,
          0.0019172823745790262
        ],
        "angle_rad": 3.1393931781927567,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      }
    ],
    "com_eligible": false,
    "covariance_singular_values": [
      0.1409905667696571,
      0.031706567409211545,
      0.0012398301866632518
    ],
    "origin_residuals_m": {
      "base_link": 0.004161329179986064,
      "link1": 0.007827243499679793,
      "link2": 0.001778171204090636,
      "link3": 0.0016859309776255849,
      "link4": 0.0036574635928367854,
      "link5": 0.005146787665919967,
      "link6": 0.0031710865781215576,
      "link7": 0.0028800977064835816,
      "link8": 0.0027712134405198634
    },
    "reason": "Origin residual exceeds threshold and/or matched signed joint axes disagree"
  }
}
```


## Every reported quantity difference

Counts are quantity records, including correlated total/subtree/body mass records; they are not independent robot defects.

| Entity / quantity | M | S | H | H − M | Class | M source | S source | H source |
|---|---|---|---|---|---|---|---|---|
| robot / total_mass | 3.59566038 | 3.454278 | 3.454278 | -0.14138238 | undocumented derivation difference | [aggregate inputs](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/arx_l5/arx_l5.xml#L1) | [aggregate inputs](https://github.com/ARXroboticsX/ARX_Model/blob/af6fe43c873008a85bce6195c0f2160f1a1c14ce/X5/X5A/urdf/X5A.urdf#L1) | [aggregate inputs](https://github.com/ARXroboticsX/ARX_Model/blob/e58172bd0874ff8c940700dc87f64a9ce951718d/X5/X5A/urdf/X5A.urdf#L1) |
| base_link / mass | 0.12842018 | 0.43995 | 0.43995 | 0.31152982 | undocumented derivation difference | [geometry/inference input L39](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/arx_l5/arx_l5.xml#L39) | [input L14](https://github.com/ARXroboticsX/ARX_Model/blob/af6fe43c873008a85bce6195c0f2160f1a1c14ce/X5/X5A/urdf/X5A.urdf#L14) | [input L14](https://github.com/ARXroboticsX/ARX_Model/blob/e58172bd0874ff8c940700dc87f64a9ce951718d/X5/X5A/urdf/X5A.urdf#L14) |
| base_link / subtree_mass | 3.59566038 | 3.454278 | 3.454278 | -0.14138238 | undocumented derivation difference | [subtree root L39](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/arx_l5/arx_l5.xml#L39) | [subtree root L8](https://github.com/ARXroboticsX/ARX_Model/blob/af6fe43c873008a85bce6195c0f2160f1a1c14ce/X5/X5A/urdf/X5A.urdf#L8) | [subtree root L8](https://github.com/ARXroboticsX/ARX_Model/blob/e58172bd0874ff8c940700dc87f64a9ce951718d/X5/X5A/urdf/X5A.urdf#L8) |
| base_link / principal_moments | [3.79946993e-05, 6.38231873e-05, 6.38231873e-05] | [0.00016, 0.00017, 0.00017] | [0.00016, 0.00017, 0.00017] | [0.000122005301, 0.000106176813, 0.000106176813] | undocumented derivation difference | [geometry/inference input L39](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/arx_l5/arx_l5.xml#L39) | [inertia input L21](https://github.com/ARXroboticsX/ARX_Model/blob/af6fe43c873008a85bce6195c0f2160f1a1c14ce/X5/X5A/urdf/X5A.urdf#L21) | [inertia input L21](https://github.com/ARXroboticsX/ARX_Model/blob/e58172bd0874ff8c940700dc87f64a9ce951718d/X5/X5A/urdf/X5A.urdf#L21) |
| link1 / mass | 0.096804 | 0.066982 | 0.066982 | -0.029822 | undocumented derivation difference | [input L44](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/arx_l5/arx_l5.xml#L44) | [input L54](https://github.com/ARXroboticsX/ARX_Model/blob/af6fe43c873008a85bce6195c0f2160f1a1c14ce/X5/X5A/urdf/X5A.urdf#L54) | [input L54](https://github.com/ARXroboticsX/ARX_Model/blob/e58172bd0874ff8c940700dc87f64a9ce951718d/X5/X5A/urdf/X5A.urdf#L54) |
| link1 / subtree_mass | 3.4672402 | 3.014328 | 3.014328 | -0.4529122 | undocumented derivation difference | [subtree root L42](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/arx_l5/arx_l5.xml#L42) | [subtree root L48](https://github.com/ARXroboticsX/ARX_Model/blob/af6fe43c873008a85bce6195c0f2160f1a1c14ce/X5/X5A/urdf/X5A.urdf#L48) | [subtree root L48](https://github.com/ARXroboticsX/ARX_Model/blob/e58172bd0874ff8c940700dc87f64a9ce951718d/X5/X5A/urdf/X5A.urdf#L48) |
| link1 / principal_moments | [4.70346e-05, 9.40205e-05, 0.000118945] | [3e-05, 7e-05, 9e-05] | [3e-05, 7e-05, 9e-05] | [-1.70346e-05, -2.40205e-05, -2.8945e-05] | undocumented derivation difference | [inertia input L44](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/arx_l5/arx_l5.xml#L44) | [inertia input L61](https://github.com/ARXroboticsX/ARX_Model/blob/af6fe43c873008a85bce6195c0f2160f1a1c14ce/X5/X5A/urdf/X5A.urdf#L61) | [inertia input L61](https://github.com/ARXroboticsX/ARX_Model/blob/e58172bd0874ff8c940700dc87f64a9ce951718d/X5/X5A/urdf/X5A.urdf#L61) |
| link2 / mass | 1.1988 | 1.0795 | 1.0795 | -0.1193 | undocumented derivation difference | [input L50](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/arx_l5/arx_l5.xml#L50) | [input L112](https://github.com/ARXroboticsX/ARX_Model/blob/af6fe43c873008a85bce6195c0f2160f1a1c14ce/X5/X5A/urdf/X5A.urdf#L112) | [input L112](https://github.com/ARXroboticsX/ARX_Model/blob/e58172bd0874ff8c940700dc87f64a9ce951718d/X5/X5A/urdf/X5A.urdf#L112) |
| link2 / subtree_mass | 3.3704362 | 2.947346 | 2.947346 | -0.4230902 | undocumented derivation difference | [subtree root L48](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/arx_l5/arx_l5.xml#L48) | [subtree root L106](https://github.com/ARXroboticsX/ARX_Model/blob/af6fe43c873008a85bce6195c0f2160f1a1c14ce/X5/X5A/urdf/X5A.urdf#L106) | [subtree root L106](https://github.com/ARXroboticsX/ARX_Model/blob/e58172bd0874ff8c940700dc87f64a9ce951718d/X5/X5A/urdf/X5A.urdf#L106) |
| link2 / principal_moments | [0.000649595, 0.01646, 0.0164704] | [0.000509890581, 0.0159900064, 0.016050103] | [0.000509890581, 0.0159900064, 0.016050103] | [-0.000139704419, -0.000469993551, -0.00042029703] | undocumented derivation difference | [inertia input L50](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/arx_l5/arx_l5.xml#L50) | [inertia input L119](https://github.com/ARXroboticsX/ARX_Model/blob/af6fe43c873008a85bce6195c0f2160f1a1c14ce/X5/X5A/urdf/X5A.urdf#L119) | [inertia input L119](https://github.com/ARXroboticsX/ARX_Model/blob/e58172bd0874ff8c940700dc87f64a9ce951718d/X5/X5A/urdf/X5A.urdf#L119) |
| link3 / mass | 0.84082 | 0.54534 | 0.54534 | -0.29548 | undocumented derivation difference | [input L56](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/arx_l5/arx_l5.xml#L56) | [input L170](https://github.com/ARXroboticsX/ARX_Model/blob/af6fe43c873008a85bce6195c0f2160f1a1c14ce/X5/X5A/urdf/X5A.urdf#L170) | [input L170](https://github.com/ARXroboticsX/ARX_Model/blob/e58172bd0874ff8c940700dc87f64a9ce951718d/X5/X5A/urdf/X5A.urdf#L170) |
| link3 / subtree_mass | 2.1716362 | 1.867846 | 1.867846 | -0.3037902 | undocumented derivation difference | [subtree root L54](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/arx_l5/arx_l5.xml#L54) | [subtree root L164](https://github.com/ARXroboticsX/ARX_Model/blob/af6fe43c873008a85bce6195c0f2160f1a1c14ce/X5/X5A/urdf/X5A.urdf#L164) | [subtree root L164](https://github.com/ARXroboticsX/ARX_Model/blob/e58172bd0874ff8c940700dc87f64a9ce951718d/X5/X5A/urdf/X5A.urdf#L164) |
| link3 / principal_moments | [0.000747034, 0.00841207, 0.0084909] | [0.000320578084, 0.0042210016, 0.00424842032] | [0.000320578084, 0.0042210016, 0.00424842032] | [-0.000426455916, -0.0041910684, -0.00424247968] | undocumented derivation difference | [inertia input L56](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/arx_l5/arx_l5.xml#L56) | [inertia input L177](https://github.com/ARXroboticsX/ARX_Model/blob/af6fe43c873008a85bce6195c0f2160f1a1c14ce/X5/X5A/urdf/X5A.urdf#L177) | [inertia input L177](https://github.com/ARXroboticsX/ARX_Model/blob/e58172bd0874ff8c940700dc87f64a9ce951718d/X5/X5A/urdf/X5A.urdf#L177) |
| link4 / mass | 0.12432 | 0.11714 | 0.11714 | -0.00718 | undocumented derivation difference | [input L64](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/arx_l5/arx_l5.xml#L64) | [input L228](https://github.com/ARXroboticsX/ARX_Model/blob/af6fe43c873008a85bce6195c0f2160f1a1c14ce/X5/X5A/urdf/X5A.urdf#L228) | [input L228](https://github.com/ARXroboticsX/ARX_Model/blob/e58172bd0874ff8c940700dc87f64a9ce951718d/X5/X5A/urdf/X5A.urdf#L228) |
| link4 / subtree_mass | 1.3308162 | 1.322506 | 1.322506 | -0.0083102 | undocumented derivation difference | [subtree root L62](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/arx_l5/arx_l5.xml#L62) | [subtree root L222](https://github.com/ARXroboticsX/ARX_Model/blob/af6fe43c873008a85bce6195c0f2160f1a1c14ce/X5/X5A/urdf/X5A.urdf#L222) | [subtree root L222](https://github.com/ARXroboticsX/ARX_Model/blob/e58172bd0874ff8c940700dc87f64a9ce951718d/X5/X5A/urdf/X5A.urdf#L222) |
| link4 / principal_moments | [0.000101491, 0.000235316, 0.000303193] | [7.14977172e-05, 0.000212859771, 0.000275642512] | [7.14977172e-05, 0.000212859771, 0.000275642512] | [-2.99932828e-05, -2.24562292e-05, -2.7550488e-05] | undocumented derivation difference | [inertia input L64](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/arx_l5/arx_l5.xml#L64) | [inertia input L235](https://github.com/ARXroboticsX/ARX_Model/blob/af6fe43c873008a85bce6195c0f2160f1a1c14ce/X5/X5A/urdf/X5A.urdf#L235) | [inertia input L235](https://github.com/ARXroboticsX/ARX_Model/blob/e58172bd0874ff8c940700dc87f64a9ce951718d/X5/X5A/urdf/X5A.urdf#L235) |
| link5 / principal_moments | [0.000251671, 0.00082, 0.000848329] | [0.000251529388, 0.00082, 0.000838470612] | [0.000251529388, 0.00082, 0.000838470612] | [-1.41611817e-07, -2.16840434e-19, -9.85838818e-06] | undocumented derivation difference | [inertia input L70](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/arx_l5/arx_l5.xml#L70) | [inertia input L293](https://github.com/ARXroboticsX/ARX_Model/blob/af6fe43c873008a85bce6195c0f2160f1a1c14ce/X5/X5A/urdf/X5A.urdf#L293) | [inertia input L293](https://github.com/ARXroboticsX/ARX_Model/blob/e58172bd0874ff8c940700dc87f64a9ce951718d/X5/X5A/urdf/X5A.urdf#L293) |
| joint1 / range | [-3.14, 3.14] | [-10, 10] | [-10, 10] | [-6.86, 6.86] | undocumented derivation difference | [input L45](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/arx_l5/arx_l5.xml#L45) | [input L103](https://github.com/ARXroboticsX/ARX_Model/blob/af6fe43c873008a85bce6195c0f2160f1a1c14ce/X5/X5A/urdf/X5A.urdf#L103) | [input L103](https://github.com/ARXroboticsX/ARX_Model/blob/e58172bd0874ff8c940700dc87f64a9ce951718d/X5/X5A/urdf/X5A.urdf#L103) |
| joint2 / range | [0, 3.14] | [-10, 10] | [-10, 10] | [-10, 6.86] | undocumented derivation difference | [input L51](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/arx_l5/arx_l5.xml#L51) | [input L161](https://github.com/ARXroboticsX/ARX_Model/blob/af6fe43c873008a85bce6195c0f2160f1a1c14ce/X5/X5A/urdf/X5A.urdf#L161) | [input L161](https://github.com/ARXroboticsX/ARX_Model/blob/e58172bd0874ff8c940700dc87f64a9ce951718d/X5/X5A/urdf/X5A.urdf#L161) |
| joint3 / range | [0, 3.14] | [-10, 10] | [-10, 10] | [-10, 6.86] | undocumented derivation difference | [input L57](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/arx_l5/arx_l5.xml#L57) | [input L219](https://github.com/ARXroboticsX/ARX_Model/blob/af6fe43c873008a85bce6195c0f2160f1a1c14ce/X5/X5A/urdf/X5A.urdf#L219) | [input L219](https://github.com/ARXroboticsX/ARX_Model/blob/e58172bd0874ff8c940700dc87f64a9ce951718d/X5/X5A/urdf/X5A.urdf#L219) |
| joint4 / range | [-1.7, 1.7] | [-10, 10] | [-10, 10] | [-8.3, 8.3] | undocumented derivation difference | [input L65](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/arx_l5/arx_l5.xml#L65) | [input L277](https://github.com/ARXroboticsX/ARX_Model/blob/af6fe43c873008a85bce6195c0f2160f1a1c14ce/X5/X5A/urdf/X5A.urdf#L277) | [input L277](https://github.com/ARXroboticsX/ARX_Model/blob/e58172bd0874ff8c940700dc87f64a9ce951718d/X5/X5A/urdf/X5A.urdf#L277) |
| joint5 / range | [-1.7, 1.7] | [-10, 10] | [-10, 10] | [-8.3, 8.3] | undocumented derivation difference | [input L71](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/arx_l5/arx_l5.xml#L71) | [input L335](https://github.com/ARXroboticsX/ARX_Model/blob/af6fe43c873008a85bce6195c0f2160f1a1c14ce/X5/X5A/urdf/X5A.urdf#L335) | [input L335](https://github.com/ARXroboticsX/ARX_Model/blob/e58172bd0874ff8c940700dc87f64a9ce951718d/X5/X5A/urdf/X5A.urdf#L335) |
| joint6 / range | [-3.14, 3.14] | [-10, 10] | [-10, 10] | [-6.86, 6.86] | undocumented derivation difference | [input L77](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/arx_l5/arx_l5.xml#L77) | [input L393](https://github.com/ARXroboticsX/ARX_Model/blob/af6fe43c873008a85bce6195c0f2160f1a1c14ce/X5/X5A/urdf/X5A.urdf#L393) | [input L393](https://github.com/ARXroboticsX/ARX_Model/blob/e58172bd0874ff8c940700dc87f64a9ce951718d/X5/X5A/urdf/X5A.urdf#L393) |
| joint7 / effort | 10 | 100 | 100 | 90 | undocumented derivation difference | [inherited actuator input L12](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/arx_l5/arx_l5.xml#L12) | [input L451](https://github.com/ARXroboticsX/ARX_Model/blob/af6fe43c873008a85bce6195c0f2160f1a1c14ce/X5/X5A/urdf/X5A.urdf#L451) | [input L451](https://github.com/ARXroboticsX/ARX_Model/blob/e58172bd0874ff8c940700dc87f64a9ce951718d/X5/X5A/urdf/X5A.urdf#L451) |
| joint8 / range | [-0.044, 0] | [0, 0.044] | [0, 0.044] | [0.044, 0.044] | undocumented derivation difference | [input L95](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/arx_l5/arx_l5.xml#L95) | [input L509](https://github.com/ARXroboticsX/ARX_Model/blob/af6fe43c873008a85bce6195c0f2160f1a1c14ce/X5/X5A/urdf/X5A.urdf#L509) | [input L509](https://github.com/ARXroboticsX/ARX_Model/blob/e58172bd0874ff8c940700dc87f64a9ce951718d/X5/X5A/urdf/X5A.urdf#L509) |

## Raw CoM records and reporting decisions

Raw values retain the previous root-anchor registration before Kabsch; original world coordinates also remain in the snapshots. Eligible findings above use the fitted transform into M. Excluded raw records below are diagnostic numbers, not findings. No CoM suppression applies to mass or principal inertia moments.

| Entity / quantity | Raw M | Raw S | Raw H | Raw H − M | Decision | M source | S source | H source |
|---|---|---|---|---|---|---|---|---|
| robot / total_com_registered | [-0.0169051302, -0.00105505264, 0.141761421] | [-0.00489104218, 7.11060129e-05, 0.127308276] | [-0.00489104218, 7.11060129e-05, 0.127308276] | [0.0120140881, 0.00112615865, -0.0144531452] | M/H: kinematic convention differs; M/S: kinematic convention differs | [aggregate inputs](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/arx_l5/arx_l5.xml#L1) | [aggregate inputs](https://github.com/ARXroboticsX/ARX_Model/blob/af6fe43c873008a85bce6195c0f2160f1a1c14ce/X5/X5A/urdf/X5A.urdf#L1) | [aggregate inputs](https://github.com/ARXroboticsX/ARX_Model/blob/e58172bd0874ff8c940700dc87f64a9ce951718d/X5/X5A/urdf/X5A.urdf#L1) |
| base_link / com_registered | [-0.00016559881, 4.08236753e-05, 0.0291059054] | [-3.0001e-05, 3.0589e-05, 0.027324] | [-3.0001e-05, 3.0589e-05, 0.027324] | [0.00013559781, -1.02346753e-05, -0.0017819054] | M/H: kinematic convention differs; M/S: kinematic convention differs | [geometry/inference input L39](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/arx_l5/arx_l5.xml#L39) | [CoM/kinematic input L12](https://github.com/ARXroboticsX/ARX_Model/blob/af6fe43c873008a85bce6195c0f2160f1a1c14ce/X5/X5A/urdf/X5A.urdf#L12) | [CoM/kinematic input L12](https://github.com/ARXroboticsX/ARX_Model/blob/e58172bd0874ff8c940700dc87f64a9ce951718d/X5/X5A/urdf/X5A.urdf#L12) |
| link1 / com_registered | [0.0050395, -0.0077407, 0.077397] | [0.0054231, -0.0080289, 0.077586] | [0.0054231, -0.0080289, 0.077586] | [0.0003836, -0.0002882, 0.000189] | M/H: kinematic convention differs; M/S: kinematic convention differs | [CoM/kinematic input L44](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/arx_l5/arx_l5.xml#L44) | [CoM/kinematic input L52](https://github.com/ARXroboticsX/ARX_Model/blob/af6fe43c873008a85bce6195c0f2160f1a1c14ce/X5/X5A/urdf/X5A.urdf#L52) | [CoM/kinematic input L52](https://github.com/ARXroboticsX/ARX_Model/blob/e58172bd0874ff8c940700dc87f64a9ce951718d/X5/X5A/urdf/X5A.urdf#L52) |
| link2 / com_registered | [-0.10992, -0.0011822, 0.103473634] | [-0.11237, 0.0020852, 0.10060549] | [-0.11237, 0.0020852, 0.10060549] | [-0.00245, 0.0032674, -0.002868144] | M/H: kinematic convention differs; M/S: kinematic convention differs | [CoM/kinematic input L50](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/arx_l5/arx_l5.xml#L50) | [CoM/kinematic input L110](https://github.com/ARXroboticsX/ARX_Model/blob/af6fe43c873008a85bce6195c0f2160f1a1c14ce/X5/X5A/urdf/X5A.urdf#L110) | [CoM/kinematic input L110](https://github.com/ARXroboticsX/ARX_Model/blob/e58172bd0874ff8c940700dc87f64a9ce951718d/X5/X5A/urdf/X5A.urdf#L110) |
| link3 / com_registered | [-0.08219, -0.00117189925, 0.158050009] | [-0.05869, -0.000684139354, 0.152137995] | [-0.05869, -0.000684139354, 0.152137995] | [0.0235, 0.000487759899, -0.00591201364] | M/H: kinematic convention differs; M/S: kinematic convention differs | [CoM/kinematic input L56](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/arx_l5/arx_l5.xml#L56) | [CoM/kinematic input L168](https://github.com/ARXroboticsX/ARX_Model/blob/af6fe43c873008a85bce6195c0f2160f1a1c14ce/X5/X5A/urdf/X5A.urdf#L168) | [CoM/kinematic input L168](https://github.com/ARXroboticsX/ARX_Model/blob/e58172bd0874ff8c940700dc87f64a9ce951718d/X5/X5A/urdf/X5A.urdf#L168) |
| link4 / com_registered | [0.042751, -0.00537291406, 0.196870039] | [0.041231, -0.00448137098, 0.191834967] | [0.041231, -0.00448137098, 0.191834967] | [-0.00152, 0.00089154308, -0.00503507239] | M/H: kinematic convention differs; M/S: kinematic convention differs | [CoM/kinematic input L64](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/arx_l5/arx_l5.xml#L64) | [CoM/kinematic input L226](https://github.com/ARXroboticsX/ARX_Model/blob/af6fe43c873008a85bce6195c0f2160f1a1c14ce/X5/X5A/urdf/X5A.urdf#L226) | [CoM/kinematic input L226](https://github.com/ARXroboticsX/ARX_Model/blob/e58172bd0874ff8c940700dc87f64a9ce951718d/X5/X5A/urdf/X5A.urdf#L226) |
| link5 / com_registered | [0.074830565, 1.60978098e-05, 0.194675] | [0.072362, -0.000485186239, 0.187785996] | [0.072362, -0.000485186239, 0.187785996] | [-0.002468565, -0.000501284049, -0.00688900345] | M/H: kinematic convention differs; M/S: kinematic convention differs | [CoM/kinematic input L70](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/arx_l5/arx_l5.xml#L70) | [CoM/kinematic input L284](https://github.com/ARXroboticsX/ARX_Model/blob/af6fe43c873008a85bce6195c0f2160f1a1c14ce/X5/X5A/urdf/X5A.urdf#L284) | [CoM/kinematic input L284](https://github.com/ARXroboticsX/ARX_Model/blob/e58172bd0874ff8c940700dc87f64a9ce951718d/X5/X5A/urdf/X5A.urdf#L284) |
| link6 / com_registered | [0.141897, 2.48087852e-05, 0.16364464] | [0.139397, -0.000476043399, 0.156644636] | [0.139397, -0.000476043399, 0.156644636] | [-0.0025, -0.000500852184, -0.00700000367] | M/H: kinematic convention differs; M/S: kinematic convention differs | [CoM/kinematic input L76](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/arx_l5/arx_l5.xml#L76) | [CoM/kinematic input L342](https://github.com/ARXroboticsX/ARX_Model/blob/af6fe43c873008a85bce6195c0f2160f1a1c14ce/X5/X5A/urdf/X5A.urdf#L342) | [CoM/kinematic input L342](https://github.com/ARXroboticsX/ARX_Model/blob/e58172bd0874ff8c940700dc87f64a9ce951718d/X5/X5A/urdf/X5A.urdf#L342) |
| link7 / com_registered | [0.18641478, 0.0170694408, 0.1602681] | [0.18391478, 0.0165685886, 0.153268096] | [0.18391478, 0.0165685886, 0.153268096] | [-0.0025, -0.000500852184, -0.00700000367] | M/H: kinematic convention differs; M/S: kinematic convention differs | [CoM/kinematic input L86](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/arx_l5/arx_l5.xml#L86) | [CoM/kinematic input L400](https://github.com/ARXroboticsX/ARX_Model/blob/af6fe43c873008a85bce6195c0f2160f1a1c14ce/X5/X5A/urdf/X5A.urdf#L400) | [CoM/kinematic input L400](https://github.com/ARXroboticsX/ARX_Model/blob/e58172bd0874ff8c940700dc87f64a9ce951718d/X5/X5A/urdf/X5A.urdf#L400) |
| link8 / com_registered | [0.186414777, -0.0170718692, 0.1656764] | [0.18391478, -0.0175727114, 0.158676436] | [0.18391478, -0.0175727114, 0.158676436] | [-0.002499997, -0.000500842184, -0.00699996367] | M/H: kinematic convention differs; M/S: kinematic convention differs | [CoM/kinematic input L94](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/arx_l5/arx_l5.xml#L94) | [CoM/kinematic input L458](https://github.com/ARXroboticsX/ARX_Model/blob/af6fe43c873008a85bce6195c0f2160f1a1c14ce/X5/X5A/urdf/X5A.urdf#L458) | [CoM/kinematic input L458](https://github.com/ARXroboticsX/ARX_Model/blob/e58172bd0874ff8c940700dc87f64a9ce951718d/X5/X5A/urdf/X5A.urdf#L458) |

## Mass accounting

Every contributing compiled body mass is listed here so total/subtree sums can be checked. Links point to explicit inertials or to geometry inputs when the compiler inferred a mass. CoM links identify inertial inputs; world coordinates additionally use the ancestor transforms and the registration recorded below.

| M body | M kg / source | S kg / source | H kg / source |
|---|---|---|---|
| base_link | 0.12842018 / [geometry/inference input L39](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/arx_l5/arx_l5.xml#L39) | 0.43995 / [input L14](https://github.com/ARXroboticsX/ARX_Model/blob/af6fe43c873008a85bce6195c0f2160f1a1c14ce/X5/X5A/urdf/X5A.urdf#L14) | 0.43995 / [input L14](https://github.com/ARXroboticsX/ARX_Model/blob/e58172bd0874ff8c940700dc87f64a9ce951718d/X5/X5A/urdf/X5A.urdf#L14) |
| link1 | 0.096804 / [input L44](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/arx_l5/arx_l5.xml#L44) | 0.066982 / [input L54](https://github.com/ARXroboticsX/ARX_Model/blob/af6fe43c873008a85bce6195c0f2160f1a1c14ce/X5/X5A/urdf/X5A.urdf#L54) | 0.066982 / [input L54](https://github.com/ARXroboticsX/ARX_Model/blob/e58172bd0874ff8c940700dc87f64a9ce951718d/X5/X5A/urdf/X5A.urdf#L54) |
| link2 | 1.1988 / [input L50](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/arx_l5/arx_l5.xml#L50) | 1.0795 / [input L112](https://github.com/ARXroboticsX/ARX_Model/blob/af6fe43c873008a85bce6195c0f2160f1a1c14ce/X5/X5A/urdf/X5A.urdf#L112) | 1.0795 / [input L112](https://github.com/ARXroboticsX/ARX_Model/blob/e58172bd0874ff8c940700dc87f64a9ce951718d/X5/X5A/urdf/X5A.urdf#L112) |
| link3 | 0.84082 / [input L56](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/arx_l5/arx_l5.xml#L56) | 0.54534 / [input L170](https://github.com/ARXroboticsX/ARX_Model/blob/af6fe43c873008a85bce6195c0f2160f1a1c14ce/X5/X5A/urdf/X5A.urdf#L170) | 0.54534 / [input L170](https://github.com/ARXroboticsX/ARX_Model/blob/e58172bd0874ff8c940700dc87f64a9ce951718d/X5/X5A/urdf/X5A.urdf#L170) |
| link4 | 0.12432 / [input L64](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/arx_l5/arx_l5.xml#L64) | 0.11714 / [input L228](https://github.com/ARXroboticsX/ARX_Model/blob/af6fe43c873008a85bce6195c0f2160f1a1c14ce/X5/X5A/urdf/X5A.urdf#L228) | 0.11714 / [input L228](https://github.com/ARXroboticsX/ARX_Model/blob/e58172bd0874ff8c940700dc87f64a9ce951718d/X5/X5A/urdf/X5A.urdf#L228) |
| link5 | 0.63601 / [input L70](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/arx_l5/arx_l5.xml#L70) | 0.63488 / [input L286](https://github.com/ARXroboticsX/ARX_Model/blob/af6fe43c873008a85bce6195c0f2160f1a1c14ce/X5/X5A/urdf/X5A.urdf#L286) | 0.63488 / [input L286](https://github.com/ARXroboticsX/ARX_Model/blob/e58172bd0874ff8c940700dc87f64a9ce951718d/X5/X5A/urdf/X5A.urdf#L286) |
| link6 | 0.44089 / [input L76](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/arx_l5/arx_l5.xml#L76) | 0.44089 / [input L344](https://github.com/ARXroboticsX/ARX_Model/blob/af6fe43c873008a85bce6195c0f2160f1a1c14ce/X5/X5A/urdf/X5A.urdf#L344) | 0.44089 / [input L344](https://github.com/ARXroboticsX/ARX_Model/blob/e58172bd0874ff8c940700dc87f64a9ce951718d/X5/X5A/urdf/X5A.urdf#L344) |
| link7 | 0.064798 / [input L86](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/arx_l5/arx_l5.xml#L86) | 0.064798 / [input L402](https://github.com/ARXroboticsX/ARX_Model/blob/af6fe43c873008a85bce6195c0f2160f1a1c14ce/X5/X5A/urdf/X5A.urdf#L402) | 0.064798 / [input L402](https://github.com/ARXroboticsX/ARX_Model/blob/e58172bd0874ff8c940700dc87f64a9ce951718d/X5/X5A/urdf/X5A.urdf#L402) |
| link8 | 0.0647982 / [input L94](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/arx_l5/arx_l5.xml#L94) | 0.064798 / [input L460](https://github.com/ARXroboticsX/ARX_Model/blob/af6fe43c873008a85bce6195c0f2160f1a1c14ce/X5/X5A/urdf/X5A.urdf#L460) | 0.064798 / [input L460](https://github.com/ARXroboticsX/ARX_Model/blob/e58172bd0874ff8c940700dc87f64a9ce951718d/X5/X5A/urdf/X5A.urdf#L460) |

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
      "link7": "link7",
      "link8": "link8"
    },
    "joints": {
      "joint1": "joint1",
      "joint2": "joint2",
      "joint3": "joint3",
      "joint4": "joint4",
      "joint5": "joint5",
      "joint6": "joint6",
      "joint7": "joint7",
      "joint8": "joint8"
    },
    "body_methods": {
      "base_link": "name",
      "link1": "name",
      "link2": "name",
      "link3": "name",
      "link4": "name",
      "link5": "name",
      "link6": "name",
      "link7": "name",
      "link8": "name"
    },
    "joint_methods": {
      "joint1": "name",
      "joint2": "name",
      "joint3": "name",
      "joint4": "name",
      "joint5": "name",
      "joint6": "name",
      "joint7": "name",
      "joint8": "name"
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
      "link7": "link7",
      "link8": "link8"
    },
    "joints": {
      "joint1": "joint1",
      "joint2": "joint2",
      "joint3": "joint3",
      "joint4": "joint4",
      "joint5": "joint5",
      "joint6": "joint6",
      "joint7": "joint7",
      "joint8": "joint8"
    },
    "body_methods": {
      "base_link": "name",
      "link1": "name",
      "link2": "name",
      "link3": "name",
      "link4": "name",
      "link5": "name",
      "link6": "name",
      "link7": "name",
      "link8": "name"
    },
    "joint_methods": {
      "joint1": "name",
      "joint2": "name",
      "joint3": "name",
      "joint4": "name",
      "joint5": "name",
      "joint6": "name",
      "joint7": "name",
      "joint8": "name"
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
      "m": 100.0,
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
      "other": 1000.0,
      "s": 1000.0,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "joint2",
      "other_entity": "joint2",
      "quantity": "force",
      "tolerance": "limit",
      "m": 100.0,
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
      "other": 1000.0,
      "s": 1000.0,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "joint3",
      "other_entity": "joint3",
      "quantity": "force",
      "tolerance": "limit",
      "m": 100.0,
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
      "other": 1000.0,
      "s": 1000.0,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "joint4",
      "other_entity": "joint4",
      "quantity": "force",
      "tolerance": "limit",
      "m": 100.0,
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
      "other": 1000.0,
      "s": 1000.0,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "joint5",
      "other_entity": "joint5",
      "quantity": "force",
      "tolerance": "limit",
      "m": 100.0,
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
      "other": 1000.0,
      "s": 1000.0,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "joint6",
      "other_entity": "joint6",
      "quantity": "force",
      "tolerance": "limit",
      "m": 100.0,
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
      "other": 1000.0,
      "s": 1000.0,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "joint7",
      "other_entity": "joint7",
      "quantity": "force",
      "tolerance": "limit",
      "m": 10.0,
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
      "other": 1000.0,
      "s": 1000.0,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "joint8",
      "other_entity": "joint8",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": 100.0,
      "s": 100.0,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "joint8",
      "other_entity": "joint8",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "joint8",
      "other_entity": "joint8",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 1000.0,
      "s": 1000.0,
      "reason": "quantity absent or not enforced/declared on one side"
    }
  ]
}
```

## Limits unavailable for a like-for-like simulator comparison

URDF effort and velocity tags are manufacturer declarations; MuJoCo ignores them. Missing enforced quantities are not interpreted as zero. The available values are shown for review and excluded from STALE counts.

| Joint / quantity | M | S | H / declared upstream |
|---|---|---|---|
| joint1 / force | 100 | unavailable | unavailable |
| joint1 / velocity | unavailable | 1000 | 1000 |
| joint2 / force | 100 | unavailable | unavailable |
| joint2 / velocity | unavailable | 1000 | 1000 |
| joint3 / force | 100 | unavailable | unavailable |
| joint3 / velocity | unavailable | 1000 | 1000 |
| joint4 / force | 100 | unavailable | unavailable |
| joint4 / velocity | unavailable | 1000 | 1000 |
| joint5 / force | 100 | unavailable | unavailable |
| joint5 / velocity | unavailable | 1000 | 1000 |
| joint6 / force | 100 | unavailable | unavailable |
| joint6 / velocity | unavailable | 1000 | 1000 |
| joint7 / force | 10 | unavailable | unavailable |
| joint7 / velocity | unavailable | 1000 | 1000 |
| joint8 / effort | unavailable | 100 | 100 |
| joint8 / force | unavailable | unavailable | unavailable |
| joint8 / velocity | unavailable | 1000 | 1000 |
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
    "file": "arx_l5/arx_l5.xml",
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
      "undocumented derivation difference": 25
    },
    "classifications_changed": 0,
    "finding_membership_changes": 0
  },
  "2": {
    "provenance_method": "pinned",
    "counts": {
      "undocumented derivation difference": 23
    },
    "classifications_changed": 3,
    "finding_membership_changes": 2
  }
}
```

## Compilation

```json
{
  "M": {
    "geometry_stripped": false,
    "missing_explicit_inertials": [
      "base_link"
    ],
    "assets_loaded": 10,
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
  "self_variants_recompiled": 1,
  "historical_snapshots_reused": 1,
  "primary_physics_unchanged": true,
  "source_matching": "original raw-value provenance criteria retained; kinematic guard applies to reported CoM"
}
```
