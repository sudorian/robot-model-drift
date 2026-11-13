# berkeley_humanoid

Status: **complete**. Provenance: **dated match**, confidence **medium**.

Source selected using the ordered amended provenance rules.

M: `https://github.com/google-deepmind/mujoco_menagerie`, `berkeley_humanoid/berkeley_humanoid.xml`, commit `370c43965323c0944b433b202aac5058b5f907a9`.
H: `https://github.com/HybridRobotics/berkeley_humanoid_description`, `urdf/robot.urdf`, commit `d0d13d3f81d795480e25ed1910eaf83d5f0a1d0b`.
S: `f6dbbb3319746655b75239790ef6e9224067dbca` (2024-08-23T14:55:32-07:00). Menagerie release/change: 2024-12-06T12:21:30-08:00.

Limit semantics: MJCF effort values are supported actuator torque/force envelopes. URDF effort and velocity values are manufacturer declarations retained from XML; MuJoCo does not enforce those tags. Such declaration comparisons are explicitly distinct from compiled inertial/range quantities.


## Source evidence

```json
[
  {
    "url": "https://github.com/HybridRobotics/berkeley_humanoid_description",
    "document": "berkeley_humanoid/README.md",
    "commit": "370c43965323c0944b433b202aac5058b5f907a9",
    "current": true
  },
  {
    "url": "https://github.com/HybridRobotics/isaac_berkeley_humanoid",
    "document": "berkeley_humanoid/README.md",
    "commit": "370c43965323c0944b433b202aac5058b5f907a9",
    "current": true
  }
]
```


## Kinematics consistency

A proper Kabsch rigid transform aligns all matched zero-pose body origins. The maximum per-origin residual and signed hinge/slide axis angles determine whether CoM can be compared; RMS is also recorded. Fewer than three non-collinear origins give insufficient kinematic coverage. CoM records that fail either required M/H or M/S check are excluded from counts and largest discrepancies. Masses, principal moments and raw joint ranges remain unchanged; a flagged range still requires convention review.

| Pair | Status | Origins / rank | RMS / maximum mm | Disagreeing / checked axes |
|---|---|---:|---:|---:|
| M/H | consistent | 13 / 3 | 1.2279147e-05 / 2.01699976e-05 | 0 / 12 |
| M/S | consistent | 13 / 3 | 1.2279147e-05 / 2.01699976e-05 | 0 / 12 |

Exact fitted transforms, per-origin residuals, thresholds and axis vectors:

```json
{
  "M/H": {
    "status": "consistent",
    "matched_body_origins": 13,
    "position_threshold_m": 0.005,
    "axis_threshold_rad": 0.005,
    "residual_definition": "maximum Euclidean residual over matched body origins; Kabsch minimizes RMS, which is also recorded",
    "coordinate_frames": "each snapshot registered to its matched report anchor",
    "anchor_m": "torso",
    "anchor_other": "torso",
    "rotation_other_to_m": [
      [
        0.9999999999988957,
        -1.9148635559705988e-12,
        -1.4860689117880687e-06
      ],
      [
        1.914896107025056e-12,
        1.0,
        6.689023383411617e-14
      ],
      [
        1.4860689120238524e-06,
        -6.6917322630467e-14,
        0.9999999999988958
      ]
    ],
    "translation_other_to_m": [
      -1.4065456738557303e-08,
      1.1562858387706308e-14,
      -3.347738197767569e-10
    ],
    "rms_residual_m": 1.2279146955841725e-08,
    "max_residual_m": 2.016999756584117e-08,
    "fit_rank": 3,
    "axis_checks": [
      {
        "joint_m": "LL_HR",
        "joint_other": "LL_HR",
        "axis_m": [
          0.7071059632710104,
          0.0,
          0.7071075991011386
        ],
        "axis_other_aligned": [
          0.7071057303763714,
          1.4025906344513598e-12,
          0.7071078319951621
        ],
        "angle_rad": 3.293623218633083e-07,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "LL_HAA",
        "joint_other": "LL_HAA",
        "axis_m": [
          -0.7071075991011387,
          0.0,
          0.7071059632710102
        ],
        "axis_other_aligned": [
          -0.7071078319951609,
          -1.3044329307681217e-12,
          0.7071057303763725
        ],
        "angle_rad": 3.293623199755258e-07,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "LL_HFE",
        "joint_other": "LL_HFE",
        "axis_m": [
          1.796078637917135e-17,
          1.0,
          3.3306690738754706e-16
        ],
        "axis_other_aligned": [
          -1.934236936201211e-12,
          1.0,
          -7.468891259302976e-14
        ],
        "angle_rad": 1.9357092508764415e-12,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "LL_KFE",
        "joint_other": "LL_KFE",
        "axis_m": [
          1.796078637917135e-17,
          1.0,
          3.3306690738754706e-16
        ],
        "axis_other_aligned": [
          -1.897433056133871e-12,
          1.0,
          -6.580707370291668e-14
        ],
        "angle_rad": 1.8986034024544577e-12,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "LL_FFE",
        "joint_other": "LL_FFE",
        "axis_m": [
          1.796078637917135e-17,
          1.0,
          3.3306690738754706e-16
        ],
        "axis_other_aligned": [
          -1.897433056133871e-12,
          1.0,
          -6.580707370291668e-14
        ],
        "angle_rad": 1.8986034024544577e-12,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "LL_FAA",
        "joint_other": "LL_FAA",
        "axis_m": [
          0.9999999999988018,
          -7.347198057734409e-17,
          1.5480468545936439e-06
        ],
        "axis_other_aligned": [
          0.9999999999988958,
          1.8975766278409027e-12,
          1.4860688940382396e-06
        ],
        "angle_rad": 6.19779605845267e-08,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "LR_HR",
        "joint_other": "LR_HR",
        "axis_m": [
          0.7071059632710104,
          0.0,
          0.7071075991011386
        ],
        "axis_other_aligned": [
          0.707105730376361,
          1.3998625988043766e-12,
          0.7071078319951726
        ],
        "angle_rad": 3.293623365737517e-07,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "LR_HAA",
        "joint_other": "LR_HAA",
        "axis_m": [
          -0.7071075991011387,
          0.0,
          0.7071059632710102
        ],
        "axis_other_aligned": [
          -0.707107831995153,
          -1.3042985655296033e-12,
          0.7071057303763804
        ],
        "angle_rad": 3.2936230887329503e-07,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "LR_HFE",
        "joint_other": "LR_HFE",
        "axis_m": [
          1.796078637917135e-17,
          1.0,
          3.3306690738754706e-16
        ],
        "axis_other_aligned": [
          -1.933126700307617e-12,
          1.0,
          -8.334865053522849e-14
        ],
        "angle_rad": 1.9349550151231856e-12,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "LR_KFE",
        "joint_other": "LR_KFE",
        "axis_m": [
          1.796078637917135e-17,
          1.0,
          3.3306690738754706e-16
        ],
        "axis_other_aligned": [
          -1.945949778881812e-12,
          1.0,
          -8.157231275180471e-14
        ],
        "angle_rad": 1.9476906671867703e-12,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "LR_FFE",
        "joint_other": "LR_FFE",
        "axis_m": [
          1.796078637917135e-17,
          1.0,
          3.3306690738754706e-16
        ],
        "axis_other_aligned": [
          -1.9433962626254413e-12,
          1.0,
          -8.379275500635636e-14
        ],
        "angle_rad": 1.9452341755356945e-12,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "LR_FAA",
        "joint_other": "LR_FAA",
        "axis_m": [
          0.9999999999988018,
          -7.347198057734409e-17,
          1.5480468545936439e-06
        ],
        "axis_other_aligned": [
          0.9999999999988958,
          1.9433733276066896e-12,
          1.4860688884871245e-06
        ],
        "angle_rad": 6.197796613706097e-08,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      }
    ],
    "axis_disagreements": [],
    "com_eligible": true,
    "covariance_singular_values": [
      0.5682664271083674,
      0.1879232799999972,
      0.002641279680092128
    ],
    "origin_residuals_m": {
      "torso": 1.4069440172756293e-08,
      "ll_hr": 1.4069574454354729e-08,
      "ll_haa": 1.2714662174098818e-08,
      "ll_hfe": 2.0169670897539195e-08,
      "ll_kfe": 7.093730170824241e-09,
      "ll_ffe": 5.932895769039236e-09,
      "ll_faa": 5.3962627515840924e-09,
      "lr_hr": 1.4069304900829228e-08,
      "lr_haa": 1.2714753491049438e-08,
      "lr_hfe": 2.016999756584117e-08,
      "lr_kfe": 7.093849333498513e-09,
      "lr_ffe": 5.933146699675645e-09,
      "lr_faa": 5.396534148258921e-09
    },
    "reason": "Unique proper rigid fit and matched signed axes meet the configured thresholds"
  },
  "M/S": {
    "status": "consistent",
    "matched_body_origins": 13,
    "position_threshold_m": 0.005,
    "axis_threshold_rad": 0.005,
    "residual_definition": "maximum Euclidean residual over matched body origins; Kabsch minimizes RMS, which is also recorded",
    "coordinate_frames": "each snapshot registered to its matched report anchor",
    "anchor_m": "torso",
    "anchor_other": "torso",
    "rotation_other_to_m": [
      [
        0.9999999999988957,
        -1.9148635559705988e-12,
        -1.4860689117880687e-06
      ],
      [
        1.914896107025056e-12,
        1.0,
        6.689023383411617e-14
      ],
      [
        1.4860689120238524e-06,
        -6.6917322630467e-14,
        0.9999999999988958
      ]
    ],
    "translation_other_to_m": [
      -1.4065456738557303e-08,
      1.1562858387706308e-14,
      -3.347738197767569e-10
    ],
    "rms_residual_m": 1.2279146955841725e-08,
    "max_residual_m": 2.016999756584117e-08,
    "fit_rank": 3,
    "axis_checks": [
      {
        "joint_m": "LL_HR",
        "joint_other": "LL_HR",
        "axis_m": [
          0.7071059632710104,
          0.0,
          0.7071075991011386
        ],
        "axis_other_aligned": [
          0.7071057303763714,
          1.4025906344513598e-12,
          0.7071078319951621
        ],
        "angle_rad": 3.293623218633083e-07,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "LL_HAA",
        "joint_other": "LL_HAA",
        "axis_m": [
          -0.7071075991011387,
          0.0,
          0.7071059632710102
        ],
        "axis_other_aligned": [
          -0.7071078319951609,
          -1.3044329307681217e-12,
          0.7071057303763725
        ],
        "angle_rad": 3.293623199755258e-07,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "LL_HFE",
        "joint_other": "LL_HFE",
        "axis_m": [
          1.796078637917135e-17,
          1.0,
          3.3306690738754706e-16
        ],
        "axis_other_aligned": [
          -1.934236936201211e-12,
          1.0,
          -7.468891259302976e-14
        ],
        "angle_rad": 1.9357092508764415e-12,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "LL_KFE",
        "joint_other": "LL_KFE",
        "axis_m": [
          1.796078637917135e-17,
          1.0,
          3.3306690738754706e-16
        ],
        "axis_other_aligned": [
          -1.897433056133871e-12,
          1.0,
          -6.580707370291668e-14
        ],
        "angle_rad": 1.8986034024544577e-12,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "LL_FFE",
        "joint_other": "LL_FFE",
        "axis_m": [
          1.796078637917135e-17,
          1.0,
          3.3306690738754706e-16
        ],
        "axis_other_aligned": [
          -1.897433056133871e-12,
          1.0,
          -6.580707370291668e-14
        ],
        "angle_rad": 1.8986034024544577e-12,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "LL_FAA",
        "joint_other": "LL_FAA",
        "axis_m": [
          0.9999999999988018,
          -7.347198057734409e-17,
          1.5480468545936439e-06
        ],
        "axis_other_aligned": [
          0.9999999999988958,
          1.8975766278409027e-12,
          1.4860688940382396e-06
        ],
        "angle_rad": 6.19779605845267e-08,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "LR_HR",
        "joint_other": "LR_HR",
        "axis_m": [
          0.7071059632710104,
          0.0,
          0.7071075991011386
        ],
        "axis_other_aligned": [
          0.707105730376361,
          1.3998625988043766e-12,
          0.7071078319951726
        ],
        "angle_rad": 3.293623365737517e-07,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "LR_HAA",
        "joint_other": "LR_HAA",
        "axis_m": [
          -0.7071075991011387,
          0.0,
          0.7071059632710102
        ],
        "axis_other_aligned": [
          -0.707107831995153,
          -1.3042985655296033e-12,
          0.7071057303763804
        ],
        "angle_rad": 3.2936230887329503e-07,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "LR_HFE",
        "joint_other": "LR_HFE",
        "axis_m": [
          1.796078637917135e-17,
          1.0,
          3.3306690738754706e-16
        ],
        "axis_other_aligned": [
          -1.933126700307617e-12,
          1.0,
          -8.334865053522849e-14
        ],
        "angle_rad": 1.9349550151231856e-12,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "LR_KFE",
        "joint_other": "LR_KFE",
        "axis_m": [
          1.796078637917135e-17,
          1.0,
          3.3306690738754706e-16
        ],
        "axis_other_aligned": [
          -1.945949778881812e-12,
          1.0,
          -8.157231275180471e-14
        ],
        "angle_rad": 1.9476906671867703e-12,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "LR_FFE",
        "joint_other": "LR_FFE",
        "axis_m": [
          1.796078637917135e-17,
          1.0,
          3.3306690738754706e-16
        ],
        "axis_other_aligned": [
          -1.9433962626254413e-12,
          1.0,
          -8.379275500635636e-14
        ],
        "angle_rad": 1.9452341755356945e-12,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "LR_FAA",
        "joint_other": "LR_FAA",
        "axis_m": [
          0.9999999999988018,
          -7.347198057734409e-17,
          1.5480468545936439e-06
        ],
        "axis_other_aligned": [
          0.9999999999988958,
          1.9433733276066896e-12,
          1.4860688884871245e-06
        ],
        "angle_rad": 6.197796613706097e-08,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      }
    ],
    "axis_disagreements": [],
    "com_eligible": true,
    "covariance_singular_values": [
      0.5682664271083674,
      0.1879232799999972,
      0.002641279680092128
    ],
    "origin_residuals_m": {
      "torso": 1.4069440172756293e-08,
      "ll_hr": 1.4069574454354729e-08,
      "ll_haa": 1.2714662174098818e-08,
      "ll_hfe": 2.0169670897539195e-08,
      "ll_kfe": 7.093730170824241e-09,
      "ll_ffe": 5.932895769039236e-09,
      "ll_faa": 5.3962627515840924e-09,
      "lr_hr": 1.4069304900829228e-08,
      "lr_haa": 1.2714753491049438e-08,
      "lr_hfe": 2.016999756584117e-08,
      "lr_kfe": 7.093849333498513e-09,
      "lr_ffe": 5.933146699675645e-09,
      "lr_faa": 5.396534148258921e-09
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
| robot / total_com_registered | [0.00708147067, -0.000789023017, -0.088085051] | [0.00708129451, -0.000789023134, -0.088085092] | [0.00708129451, -0.000789023134, -0.088085092] | [-1.76157478e-07, -1.17023414e-10, -4.1058261e-08] | eligible; compared after Kabsch alignment | [aggregate inputs](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/berkeley_humanoid/berkeley_humanoid.xml#L1) | [aggregate inputs](https://github.com/HybridRobotics/berkeley_humanoid_description/blob/f6dbbb3319746655b75239790ef6e9224067dbca/urdf/robot.urdf#L1) | [aggregate inputs](https://github.com/HybridRobotics/berkeley_humanoid_description/blob/d0d13d3f81d795480e25ed1910eaf83d5f0a1d0b/urdf/robot.urdf#L1) |
| torso / com_registered | [0.0123294, -0.0023557, 0.114047] | [0.0123294, -0.0023557, 0.114047] | [0.0123294, -0.0023557, 0.114047] | [3.2959746e-17, -7.80625564e-18, -2.77555756e-17] | eligible; compared after Kabsch alignment | [CoM/kinematic input L68](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/berkeley_humanoid/berkeley_humanoid.xml#L68) | [CoM/kinematic input L20](https://github.com/HybridRobotics/berkeley_humanoid_description/blob/f6dbbb3319746655b75239790ef6e9224067dbca/urdf/robot.urdf#L20) | [CoM/kinematic input L20](https://github.com/HybridRobotics/berkeley_humanoid_description/blob/d0d13d3f81d795480e25ed1910eaf83d5f0a1d0b/urdf/robot.urdf#L20) |
| ll_hr / com_registered | [-0.047732924, 0.070638, -0.0375860263] | [-0.047733, 0.070638, -0.037586] | [-0.047733, 0.070638, -0.037586] | [-7.59836193e-08, -2.08166817e-16, 2.62532039e-08] | eligible; compared after Kabsch alignment | [CoM/kinematic input L73](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/berkeley_humanoid/berkeley_humanoid.xml#L73) | [CoM/kinematic input L38](https://github.com/HybridRobotics/berkeley_humanoid_description/blob/f6dbbb3319746655b75239790ef6e9224067dbca/urdf/robot.urdf#L38) | [CoM/kinematic input L38](https://github.com/HybridRobotics/berkeley_humanoid_description/blob/d0d13d3f81d795480e25ed1910eaf83d5f0a1d0b/urdf/robot.urdf#L38) |
| ll_haa / com_registered | [0.00885013252, 0.060265, -0.0999160065] | [0.00885, 0.060265, -0.099916] | [0.00885, 0.060265, -0.099916] | [-1.32524979e-07, -2.08166817e-17, 6.52285601e-09] | eligible; compared after Kabsch alignment | [CoM/kinematic input L78](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/berkeley_humanoid/berkeley_humanoid.xml#L78) | [CoM/kinematic input L62](https://github.com/HybridRobotics/berkeley_humanoid_description/blob/f6dbbb3319746655b75239790ef6e9224067dbca/urdf/robot.urdf#L62) | [CoM/kinematic input L62](https://github.com/HybridRobotics/berkeley_humanoid_description/blob/d0d13d3f81d795480e25ed1910eaf83d5f0a1d0b/urdf/robot.urdf#L62) |
| ll_hfe / com_registered | [0.0101732118, 0.131273, -0.162795957] | [0.010173, 0.131273, -0.162796] | [0.010173, 0.131273, -0.162796] | [-2.11812847e-07, -1.11022302e-16, -4.26792571e-08] | eligible; compared after Kabsch alignment | [CoM/kinematic input L85](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/berkeley_humanoid/berkeley_humanoid.xml#L85) | [CoM/kinematic input L92](https://github.com/HybridRobotics/berkeley_humanoid_description/blob/f6dbbb3319746655b75239790ef6e9224067dbca/urdf/robot.urdf#L92) | [CoM/kinematic input L92](https://github.com/HybridRobotics/berkeley_humanoid_description/blob/d0d13d3f81d795480e25ed1910eaf83d5f0a1d0b/urdf/robot.urdf#L92) |
| ll_kfe / com_registered | [0.00189258962, 0.157768, -0.40879097] | [0.001892, 0.157768, -0.408791] | [0.001892, 0.157768, -0.408791] | [-5.89624647e-07, 8.32667268e-17, -2.9860171e-08] | eligible; compared after Kabsch alignment | [CoM/kinematic input L94](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/berkeley_humanoid/berkeley_humanoid.xml#L94) | [CoM/kinematic input L116](https://github.com/HybridRobotics/berkeley_humanoid_description/blob/f6dbbb3319746655b75239790ef6e9224067dbca/urdf/robot.urdf#L116) | [CoM/kinematic input L116](https://github.com/HybridRobotics/berkeley_humanoid_description/blob/d0d13d3f81d795480e25ed1910eaf83d5f0a1d0b/urdf/robot.urdf#L116) |
| ll_ffe / com_registered | [0.0349437273, 0.160068, -0.504174289] | [0.034943, 0.160068, -0.50417434] | [0.034943, 0.160068, -0.50417434] | [-7.27282535e-07, 5.55111512e-17, -5.10247669e-08] | eligible; compared after Kabsch alignment | [CoM/kinematic input L101](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/berkeley_humanoid/berkeley_humanoid.xml#L101) | [CoM/kinematic input L134](https://github.com/HybridRobotics/berkeley_humanoid_description/blob/f6dbbb3319746655b75239790ef6e9224067dbca/urdf/robot.urdf#L134) | [CoM/kinematic input L134](https://github.com/HybridRobotics/berkeley_humanoid_description/blob/d0d13d3f81d795480e25ed1910eaf83d5f0a1d0b/urdf/robot.urdf#L134) |
| ll_faa / com_registered | [0.044011751, 0.159971, -0.519493905] | [0.044011, 0.159971, -0.519494] | [0.044011, 0.159971, -0.519494] | [-7.5099803e-07, -1.47104551e-15, -9.50624787e-08] | eligible; compared after Kabsch alignment | [CoM/kinematic input L106](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/berkeley_humanoid/berkeley_humanoid.xml#L106) | [CoM/kinematic input L164](https://github.com/HybridRobotics/berkeley_humanoid_description/blob/f6dbbb3319746655b75239790ef6e9224067dbca/urdf/robot.urdf#L164) | [CoM/kinematic input L164](https://github.com/HybridRobotics/berkeley_humanoid_description/blob/d0d13d3f81d795480e25ed1910eaf83d5f0a1d0b/urdf/robot.urdf#L164) |
| lr_hr / com_registered | [-0.047732924, -0.070638, -0.0375860263] | [-0.047733, -0.070638, -0.037586] | [-0.047733, -0.070638, -0.037586] | [-7.59836182e-08, -7.21644966e-16, 2.6253204e-08] | eligible; compared after Kabsch alignment | [CoM/kinematic input L120](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/berkeley_humanoid/berkeley_humanoid.xml#L120) | [CoM/kinematic input L250](https://github.com/HybridRobotics/berkeley_humanoid_description/blob/f6dbbb3319746655b75239790ef6e9224067dbca/urdf/robot.urdf#L250) | [CoM/kinematic input L250](https://github.com/HybridRobotics/berkeley_humanoid_description/blob/d0d13d3f81d795480e25ed1910eaf83d5f0a1d0b/urdf/robot.urdf#L250) |
| lr_haa / com_registered | [0.00885013252, -0.060265, -0.0999160065] | [0.00885, -0.060265, -0.099916] | [0.00885, -0.060265, -0.099916] | [-1.32524977e-07, 3.46944695e-17, 6.52285637e-09] | eligible; compared after Kabsch alignment | [CoM/kinematic input L125](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/berkeley_humanoid/berkeley_humanoid.xml#L125) | [CoM/kinematic input L274](https://github.com/HybridRobotics/berkeley_humanoid_description/blob/f6dbbb3319746655b75239790ef6e9224067dbca/urdf/robot.urdf#L274) | [CoM/kinematic input L274](https://github.com/HybridRobotics/berkeley_humanoid_description/blob/d0d13d3f81d795480e25ed1910eaf83d5f0a1d0b/urdf/robot.urdf#L274) |
| lr_hfe / com_registered | [0.0101732118, -0.131273, -0.162795957] | [0.010173, -0.131273, -0.162796] | [0.010173, -0.131273, -0.162796] | [-2.11812846e-07, -1.19348975e-15, -4.26792557e-08] | eligible; compared after Kabsch alignment | [CoM/kinematic input L132](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/berkeley_humanoid/berkeley_humanoid.xml#L132) | [CoM/kinematic input L304](https://github.com/HybridRobotics/berkeley_humanoid_description/blob/f6dbbb3319746655b75239790ef6e9224067dbca/urdf/robot.urdf#L304) | [CoM/kinematic input L304](https://github.com/HybridRobotics/berkeley_humanoid_description/blob/d0d13d3f81d795480e25ed1910eaf83d5f0a1d0b/urdf/robot.urdf#L304) |
| lr_kfe / com_registered | [0.00189258962, -0.157768, -0.40879097] | [0.001892, -0.157768, -0.408791] | [0.001892, -0.157768, -0.408791] | [-5.89624647e-07, -4.41313652e-15, -2.98601687e-08] | eligible; compared after Kabsch alignment | [CoM/kinematic input L141](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/berkeley_humanoid/berkeley_humanoid.xml#L141) | [CoM/kinematic input L328](https://github.com/HybridRobotics/berkeley_humanoid_description/blob/f6dbbb3319746655b75239790ef6e9224067dbca/urdf/robot.urdf#L328) | [CoM/kinematic input L328](https://github.com/HybridRobotics/berkeley_humanoid_description/blob/d0d13d3f81d795480e25ed1910eaf83d5f0a1d0b/urdf/robot.urdf#L328) |
| lr_ffe / com_registered | [0.0349437273, -0.160068, -0.504174289] | [0.034943, -0.160068, -0.50417434] | [0.034943, -0.160068, -0.50417434] | [-7.27282535e-07, -5.93969318e-15, -5.10247662e-08] | eligible; compared after Kabsch alignment | [CoM/kinematic input L148](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/berkeley_humanoid/berkeley_humanoid.xml#L148) | [CoM/kinematic input L346](https://github.com/HybridRobotics/berkeley_humanoid_description/blob/f6dbbb3319746655b75239790ef6e9224067dbca/urdf/robot.urdf#L346) | [CoM/kinematic input L346](https://github.com/HybridRobotics/berkeley_humanoid_description/blob/d0d13d3f81d795480e25ed1910eaf83d5f0a1d0b/urdf/robot.urdf#L346) |
| lr_faa / com_registered | [0.0440117509, -0.159971, -0.519432905] | [0.044011, -0.159971, -0.519433] | [0.044011, -0.159971, -0.519433] | [-7.50903599e-07, -5.77315973e-15, -9.50624729e-08] | eligible; compared after Kabsch alignment | [CoM/kinematic input L153](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/berkeley_humanoid/berkeley_humanoid.xml#L153) | [CoM/kinematic input L376](https://github.com/HybridRobotics/berkeley_humanoid_description/blob/f6dbbb3319746655b75239790ef6e9224067dbca/urdf/robot.urdf#L376) | [CoM/kinematic input L376](https://github.com/HybridRobotics/berkeley_humanoid_description/blob/d0d13d3f81d795480e25ed1910eaf83d5f0a1d0b/urdf/robot.urdf#L376) |

## Mass accounting

Every contributing compiled body mass is listed here so total/subtree sums can be checked. Links point to explicit inertials or to geometry inputs when the compiler inferred a mass. CoM links identify inertial inputs; world coordinates additionally use the ancestor transforms and the registration recorded below.

| M body | M kg / source | S kg / source | H kg / source |
|---|---|---|---|
| torso | 5.37812 / [input L68](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/berkeley_humanoid/berkeley_humanoid.xml#L68) | 5.3781181 / [input L21](https://github.com/HybridRobotics/berkeley_humanoid_description/blob/f6dbbb3319746655b75239790ef6e9224067dbca/urdf/robot.urdf#L21) | 5.3781181 / [input L21](https://github.com/HybridRobotics/berkeley_humanoid_description/blob/d0d13d3f81d795480e25ed1910eaf83d5f0a1d0b/urdf/robot.urdf#L21) |
| ll_hr | 0.797 / [input L73](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/berkeley_humanoid/berkeley_humanoid.xml#L73) | 0.797 / [input L39](https://github.com/HybridRobotics/berkeley_humanoid_description/blob/f6dbbb3319746655b75239790ef6e9224067dbca/urdf/robot.urdf#L39) | 0.797 / [input L39](https://github.com/HybridRobotics/berkeley_humanoid_description/blob/d0d13d3f81d795480e25ed1910eaf83d5f0a1d0b/urdf/robot.urdf#L39) |
| ll_haa | 0.897 / [input L78](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/berkeley_humanoid/berkeley_humanoid.xml#L78) | 0.897 / [input L63](https://github.com/HybridRobotics/berkeley_humanoid_description/blob/f6dbbb3319746655b75239790ef6e9224067dbca/urdf/robot.urdf#L63) | 0.897 / [input L63](https://github.com/HybridRobotics/berkeley_humanoid_description/blob/d0d13d3f81d795480e25ed1910eaf83d5f0a1d0b/urdf/robot.urdf#L63) |
| ll_hfe | 2.689 / [input L85](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/berkeley_humanoid/berkeley_humanoid.xml#L85) | 2.689 / [input L93](https://github.com/HybridRobotics/berkeley_humanoid_description/blob/f6dbbb3319746655b75239790ef6e9224067dbca/urdf/robot.urdf#L93) | 2.689 / [input L93](https://github.com/HybridRobotics/berkeley_humanoid_description/blob/d0d13d3f81d795480e25ed1910eaf83d5f0a1d0b/urdf/robot.urdf#L93) |
| ll_kfe | 0.35 / [input L94](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/berkeley_humanoid/berkeley_humanoid.xml#L94) | 0.35 / [input L117](https://github.com/HybridRobotics/berkeley_humanoid_description/blob/f6dbbb3319746655b75239790ef6e9224067dbca/urdf/robot.urdf#L117) | 0.35 / [input L117](https://github.com/HybridRobotics/berkeley_humanoid_description/blob/d0d13d3f81d795480e25ed1910eaf83d5f0a1d0b/urdf/robot.urdf#L117) |
| ll_ffe | 0.0993228 / [input L101](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/berkeley_humanoid/berkeley_humanoid.xml#L101) | 0.09932275 / [input L135](https://github.com/HybridRobotics/berkeley_humanoid_description/blob/f6dbbb3319746655b75239790ef6e9224067dbca/urdf/robot.urdf#L135) | 0.09932275 / [input L135](https://github.com/HybridRobotics/berkeley_humanoid_description/blob/d0d13d3f81d795480e25ed1910eaf83d5f0a1d0b/urdf/robot.urdf#L135) |
| ll_faa | 0.507 / [input L106](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/berkeley_humanoid/berkeley_humanoid.xml#L106) | 0.507 / [input L165](https://github.com/HybridRobotics/berkeley_humanoid_description/blob/f6dbbb3319746655b75239790ef6e9224067dbca/urdf/robot.urdf#L165) | 0.507 / [input L165](https://github.com/HybridRobotics/berkeley_humanoid_description/blob/d0d13d3f81d795480e25ed1910eaf83d5f0a1d0b/urdf/robot.urdf#L165) |
| lr_hr | 0.797 / [input L120](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/berkeley_humanoid/berkeley_humanoid.xml#L120) | 0.797 / [input L251](https://github.com/HybridRobotics/berkeley_humanoid_description/blob/f6dbbb3319746655b75239790ef6e9224067dbca/urdf/robot.urdf#L251) | 0.797 / [input L251](https://github.com/HybridRobotics/berkeley_humanoid_description/blob/d0d13d3f81d795480e25ed1910eaf83d5f0a1d0b/urdf/robot.urdf#L251) |
| lr_haa | 0.897 / [input L125](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/berkeley_humanoid/berkeley_humanoid.xml#L125) | 0.897 / [input L275](https://github.com/HybridRobotics/berkeley_humanoid_description/blob/f6dbbb3319746655b75239790ef6e9224067dbca/urdf/robot.urdf#L275) | 0.897 / [input L275](https://github.com/HybridRobotics/berkeley_humanoid_description/blob/d0d13d3f81d795480e25ed1910eaf83d5f0a1d0b/urdf/robot.urdf#L275) |
| lr_hfe | 2.689 / [input L132](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/berkeley_humanoid/berkeley_humanoid.xml#L132) | 2.689 / [input L305](https://github.com/HybridRobotics/berkeley_humanoid_description/blob/f6dbbb3319746655b75239790ef6e9224067dbca/urdf/robot.urdf#L305) | 2.689 / [input L305](https://github.com/HybridRobotics/berkeley_humanoid_description/blob/d0d13d3f81d795480e25ed1910eaf83d5f0a1d0b/urdf/robot.urdf#L305) |
| lr_kfe | 0.35 / [input L141](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/berkeley_humanoid/berkeley_humanoid.xml#L141) | 0.35 / [input L329](https://github.com/HybridRobotics/berkeley_humanoid_description/blob/f6dbbb3319746655b75239790ef6e9224067dbca/urdf/robot.urdf#L329) | 0.35 / [input L329](https://github.com/HybridRobotics/berkeley_humanoid_description/blob/d0d13d3f81d795480e25ed1910eaf83d5f0a1d0b/urdf/robot.urdf#L329) |
| lr_ffe | 0.0993223 / [input L148](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/berkeley_humanoid/berkeley_humanoid.xml#L148) | 0.09932228 / [input L347](https://github.com/HybridRobotics/berkeley_humanoid_description/blob/f6dbbb3319746655b75239790ef6e9224067dbca/urdf/robot.urdf#L347) | 0.09932228 / [input L347](https://github.com/HybridRobotics/berkeley_humanoid_description/blob/d0d13d3f81d795480e25ed1910eaf83d5f0a1d0b/urdf/robot.urdf#L347) |
| lr_faa | 0.507 / [input L153](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/berkeley_humanoid/berkeley_humanoid.xml#L153) | 0.507 / [input L377](https://github.com/HybridRobotics/berkeley_humanoid_description/blob/f6dbbb3319746655b75239790ef6e9224067dbca/urdf/robot.urdf#L377) | 0.507 / [input L377](https://github.com/HybridRobotics/berkeley_humanoid_description/blob/d0d13d3f81d795480e25ed1910eaf83d5f0a1d0b/urdf/robot.urdf#L377) |
| upstream-only LL_FOOT | unavailable | unavailable | 1e-09 / [input L173](https://github.com/HybridRobotics/berkeley_humanoid_description/blob/d0d13d3f81d795480e25ed1910eaf83d5f0a1d0b/urdf/robot.urdf#L173) |
| upstream-only LR_FOOT | unavailable | unavailable | 1e-09 / [input L385](https://github.com/HybridRobotics/berkeley_humanoid_description/blob/d0d13d3f81d795480e25ed1910eaf83d5f0a1d0b/urdf/robot.urdf#L385) |

## Coverage and unmatched elements

```json
{
  "mapping_h": {
    "bodies": {
      "torso": "torso",
      "ll_hr": "ll_hr",
      "ll_haa": "ll_haa",
      "ll_hfe": "ll_hfe",
      "ll_kfe": "ll_kfe",
      "ll_ffe": "ll_ffe",
      "ll_faa": "ll_faa",
      "lr_hr": "lr_hr",
      "lr_haa": "lr_haa",
      "lr_hfe": "lr_hfe",
      "lr_kfe": "lr_kfe",
      "lr_ffe": "lr_ffe",
      "lr_faa": "lr_faa"
    },
    "joints": {
      "LL_HR": "LL_HR",
      "LL_HAA": "LL_HAA",
      "LL_HFE": "LL_HFE",
      "LL_KFE": "LL_KFE",
      "LL_FFE": "LL_FFE",
      "LL_FAA": "LL_FAA",
      "LR_HR": "LR_HR",
      "LR_HAA": "LR_HAA",
      "LR_HFE": "LR_HFE",
      "LR_KFE": "LR_KFE",
      "LR_FFE": "LR_FFE",
      "LR_FAA": "LR_FAA"
    },
    "body_methods": {
      "torso": "name",
      "ll_hr": "name",
      "ll_haa": "name",
      "ll_hfe": "name",
      "ll_kfe": "name",
      "ll_ffe": "name",
      "ll_faa": "name",
      "lr_hr": "name",
      "lr_haa": "name",
      "lr_hfe": "name",
      "lr_kfe": "name",
      "lr_ffe": "name",
      "lr_faa": "name"
    },
    "joint_methods": {
      "LL_HR": "name",
      "LL_HAA": "name",
      "LL_HFE": "name",
      "LL_KFE": "name",
      "LL_FFE": "name",
      "LL_FAA": "name",
      "LR_HR": "name",
      "LR_HAA": "name",
      "LR_HFE": "name",
      "LR_KFE": "name",
      "LR_FFE": "name",
      "LR_FAA": "name"
    },
    "unmatched_m_bodies": [],
    "unmatched_upstream_bodies": [
      "LL_FOOT",
      "LR_FOOT"
    ],
    "unmatched_m_joints": [],
    "unmatched_upstream_joints": [],
    "registration_anchor": {
      "M": "torso",
      "H": "torso",
      "root_unmatched": false
    }
  },
  "mapping_s": {
    "bodies": {
      "torso": "torso",
      "ll_hr": "ll_hr",
      "ll_haa": "ll_haa",
      "ll_hfe": "ll_hfe",
      "ll_kfe": "ll_kfe",
      "ll_ffe": "ll_ffe",
      "ll_faa": "ll_faa",
      "lr_hr": "lr_hr",
      "lr_haa": "lr_haa",
      "lr_hfe": "lr_hfe",
      "lr_kfe": "lr_kfe",
      "lr_ffe": "lr_ffe",
      "lr_faa": "lr_faa"
    },
    "joints": {
      "LL_HR": "LL_HR",
      "LL_HAA": "LL_HAA",
      "LL_HFE": "LL_HFE",
      "LL_KFE": "LL_KFE",
      "LL_FFE": "LL_FFE",
      "LL_FAA": "LL_FAA",
      "LR_HR": "LR_HR",
      "LR_HAA": "LR_HAA",
      "LR_HFE": "LR_HFE",
      "LR_KFE": "LR_KFE",
      "LR_FFE": "LR_FFE",
      "LR_FAA": "LR_FAA"
    },
    "body_methods": {
      "torso": "name",
      "ll_hr": "name",
      "ll_haa": "name",
      "ll_hfe": "name",
      "ll_kfe": "name",
      "ll_ffe": "name",
      "ll_faa": "name",
      "lr_hr": "name",
      "lr_haa": "name",
      "lr_hfe": "name",
      "lr_kfe": "name",
      "lr_ffe": "name",
      "lr_faa": "name"
    },
    "joint_methods": {
      "LL_HR": "name",
      "LL_HAA": "name",
      "LL_HFE": "name",
      "LL_KFE": "name",
      "LL_FFE": "name",
      "LL_FAA": "name",
      "LR_HR": "name",
      "LR_HAA": "name",
      "LR_HFE": "name",
      "LR_KFE": "name",
      "LR_FFE": "name",
      "LR_FAA": "name"
    },
    "unmatched_m_bodies": [],
    "unmatched_upstream_bodies": [
      "LL_FOOT",
      "LR_FOOT"
    ],
    "unmatched_m_joints": [],
    "unmatched_upstream_joints": [],
    "registration_anchor": {
      "M": "torso",
      "S": "torso"
    }
  },
  "unavailable": [
    {
      "entity": "LL_HR",
      "other_entity": "LL_HR",
      "quantity": "force",
      "tolerance": "limit",
      "m": 20.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "LL_HR",
      "other_entity": "LL_HR",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 23.0,
      "s": 23.0,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "LL_HAA",
      "other_entity": "LL_HAA",
      "quantity": "force",
      "tolerance": "limit",
      "m": 20.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "LL_HAA",
      "other_entity": "LL_HAA",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 23.0,
      "s": 23.0,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "LL_HFE",
      "other_entity": "LL_HFE",
      "quantity": "force",
      "tolerance": "limit",
      "m": 30.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "LL_HFE",
      "other_entity": "LL_HFE",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 20.0,
      "s": 20.0,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "LL_KFE",
      "other_entity": "LL_KFE",
      "quantity": "force",
      "tolerance": "limit",
      "m": 30.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "LL_KFE",
      "other_entity": "LL_KFE",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 14.0,
      "s": 14.0,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "LL_FFE",
      "other_entity": "LL_FFE",
      "quantity": "force",
      "tolerance": "limit",
      "m": 20.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "LL_FFE",
      "other_entity": "LL_FFE",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 20.0,
      "s": 20.0,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "LL_FAA",
      "other_entity": "LL_FAA",
      "quantity": "force",
      "tolerance": "limit",
      "m": 5.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "LL_FAA",
      "other_entity": "LL_FAA",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 42.0,
      "s": 42.0,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "LR_HR",
      "other_entity": "LR_HR",
      "quantity": "force",
      "tolerance": "limit",
      "m": 20.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "LR_HR",
      "other_entity": "LR_HR",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 23.0,
      "s": 23.0,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "LR_HAA",
      "other_entity": "LR_HAA",
      "quantity": "force",
      "tolerance": "limit",
      "m": 20.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "LR_HAA",
      "other_entity": "LR_HAA",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 23.0,
      "s": 23.0,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "LR_HFE",
      "other_entity": "LR_HFE",
      "quantity": "force",
      "tolerance": "limit",
      "m": 30.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "LR_HFE",
      "other_entity": "LR_HFE",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 20.0,
      "s": 20.0,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "LR_KFE",
      "other_entity": "LR_KFE",
      "quantity": "force",
      "tolerance": "limit",
      "m": 30.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "LR_KFE",
      "other_entity": "LR_KFE",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 14.0,
      "s": 14.0,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "LR_FFE",
      "other_entity": "LR_FFE",
      "quantity": "force",
      "tolerance": "limit",
      "m": 20.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "LR_FFE",
      "other_entity": "LR_FFE",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 23.0,
      "s": 23.0,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "LR_FAA",
      "other_entity": "LR_FAA",
      "quantity": "force",
      "tolerance": "limit",
      "m": 5.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "LR_FAA",
      "other_entity": "LR_FAA",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 42.0,
      "s": 42.0,
      "reason": "quantity absent or not enforced/declared on one side"
    }
  ]
}
```

## Limits unavailable for a like-for-like simulator comparison

URDF effort and velocity tags are manufacturer declarations; MuJoCo ignores them. Missing enforced quantities are not interpreted as zero. The available values are shown for review and excluded from STALE counts.

| Joint / quantity | M | S | H / declared upstream |
|---|---|---|---|
| LL_HR / force | 20 | unavailable | unavailable |
| LL_HR / velocity | unavailable | 23 | 23 |
| LL_HAA / force | 20 | unavailable | unavailable |
| LL_HAA / velocity | unavailable | 23 | 23 |
| LL_HFE / force | 30 | unavailable | unavailable |
| LL_HFE / velocity | unavailable | 20 | 20 |
| LL_KFE / force | 30 | unavailable | unavailable |
| LL_KFE / velocity | unavailable | 14 | 14 |
| LL_FFE / force | 20 | unavailable | unavailable |
| LL_FFE / velocity | unavailable | 20 | 20 |
| LL_FAA / force | 5 | unavailable | unavailable |
| LL_FAA / velocity | unavailable | 42 | 42 |
| LR_HR / force | 20 | unavailable | unavailable |
| LR_HR / velocity | unavailable | 23 | 23 |
| LR_HAA / force | 20 | unavailable | unavailable |
| LR_HAA / velocity | unavailable | 23 | 23 |
| LR_HFE / force | 30 | unavailable | unavailable |
| LR_HFE / velocity | unavailable | 20 | 20 |
| LR_KFE / force | 30 | unavailable | unavailable |
| LR_KFE / velocity | unavailable | 14 | 14 |
| LR_FFE / force | 20 | unavailable | unavailable |
| LR_FFE / velocity | unavailable | 23 | 23 |
| LR_FAA / force | 5 | unavailable | unavailable |
| LR_FAA / velocity | unavailable | 42 | 42 |
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
    "file": "berkeley_humanoid/berkeley_humanoid.xml",
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
    "registration": {
      "translation": [
        0.0,
        0.0,
        0.6
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
  "historical_snapshots_reused": 10,
  "primary_physics_unchanged": true,
  "source_matching": "original raw-value provenance criteria retained; kinematic guard applies to reported CoM"
}
```
