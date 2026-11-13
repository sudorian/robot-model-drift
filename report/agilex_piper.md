# agilex_piper

Status: **complete**. Provenance: **none**, confidence **none**.

No public revision matches all comparable quantities. Class: NO MATCHING SOURCE; never counted as STALE.

M: `https://github.com/google-deepmind/mujoco_menagerie`, `agilex_piper/piper.xml`, commit `370c43965323c0944b433b202aac5058b5f907a9`.
H: `https://github.com/agilexrobotics/Piper_ros`, `src/piper_description/urdf/piper_description_v100.urdf`, commit `ac41fcbcdda598f01b51cf6175ed9a24d0dacadc`.
S: unavailable. A machine-readable H can still be compared to M; no-match differences are never counted as STALE.

Limit semantics: MJCF effort values are supported actuator torque/force envelopes. URDF effort and velocity values are manufacturer declarations retained from XML; MuJoCo does not enforce those tags. Such declaration comparisons are explicitly distinct from compiled inertial/range quantities.


## Source evidence

```json
[
  {
    "url": "https://github.com/agilexrobotics/Piper_ros/tree/ros-noetic-no-aloha/src/piper_description/urdf",
    "document": "agilex_piper/README.md",
    "commit": "370c43965323c0944b433b202aac5058b5f907a9",
    "current": true
  },
  {
    "url": "https://github.com/kevinzakka/obj2mjcf",
    "document": "agilex_piper/README.md",
    "commit": "370c43965323c0944b433b202aac5058b5f907a9",
    "current": true
  }
]
```


## README derivation evidence

Documentation labels are conservative: an automated documented label requires an explicit affected entity and quantity. Broader conversion notes are retained here for review.

> 1.  Added `<mujoco> <compiler balanceinertia="true" discardvisual="false"/> </mujoco>` to the URDF's
> 4. Merged similar materials between the .objs

## Kinematics consistency

A proper Kabsch rigid transform aligns all matched zero-pose body origins. The maximum per-origin residual and signed hinge/slide axis angles determine whether CoM can be compared; RMS is also recorded. Fewer than three non-collinear origins give insufficient kinematic coverage. CoM records that fail either required M/H or M/S check are excluded from counts and largest discrepancies. Masses, principal moments and raw joint ranges remain unchanged; a flagged range still requires convention review.

| Pair | Status | Origins / rank | RMS / maximum mm | Disagreeing / checked axes |
|---|---|---:|---:|---:|
| M/H | kinematic convention differs | 9 / 3 | 4.69000283 / 6.6327929 | 0 / 8 |

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
    "anchor_other": "arm_base",
    "rotation_other_to_m": [
      [
        0.9999999981631474,
        4.3586167256253524e-05,
        -4.21182920416464e-05
      ],
      [
        -4.3570667388873086e-05,
        0.9999999313612995,
        0.00036793884398358777
      ],
      [
        4.2134326194838623e-05,
        -0.0003679370081859177,
        0.9999999314235251
      ]
    ],
    "translation_other_to_m": [
      -0.0007766124656439933,
      -5.997405713070443e-05,
      -0.006586532745522539
    ],
    "rms_residual_m": 0.004690002825649177,
    "max_residual_m": 0.006632792899511778,
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
          -4.211829204164644e-05,
          0.0003679388439835881,
          0.999999931423526
        ],
        "angle_rad": 0.000370341666177052,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "joint2",
        "joint_other": "joint2",
        "axis_m": [
          8.242642373965142e-06,
          0.9999999999580294,
          -4.000000000115022e-06
        ],
        "axis_other_aligned": [
          5.080453753037479e-05,
          0.9999999296633164,
          -0.0003716076712199362
        ],
        "angle_rad": 0.00037006340181539656,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "joint3",
        "joint_other": "joint3",
        "axis_m": [
          8.242642373958945e-06,
          0.9999999999580295,
          -4.000000000115023e-06
        ],
        "axis_other_aligned": [
          5.080453753036438e-05,
          0.9999999296633164,
          -0.00037160767122015827
        ],
        "angle_rad": 0.00037006340181561665,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "joint4",
        "joint_other": "joint4",
        "axis_m": [
          0.996196444943833,
          -1.0943433995730883e-05,
          0.08713577314461643
        ],
        "axis_other_aligned": [
          0.9961928162310985,
          -2.188858818757083e-05,
          0.08717724709144356
        ],
        "angle_rad": 4.304709307373172e-05,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "joint5",
        "joint_other": "joint5",
        "axis_m": [
          7.022917054928313e-06,
          0.9999999999695924,
          -3.3902652307737932e-06
        ],
        "axis_other_aligned": [
          5.080453753036522e-05,
          0.9999999296633164,
          -0.0003716076712199363
        ],
        "angle_rad": 0.0003708111310132919,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "joint6",
        "joint_other": "joint6",
        "axis_m": [
          0.9961964450034244,
          -2.458149247648343e-06,
          0.08713577311584898
        ],
        "axis_other_aligned": [
          0.9961924961978582,
          -1.821399378712464e-05,
          0.08718090494673053
        ],
        "angle_rad": 4.7965840571329534e-05,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "joint7",
        "joint_other": "joint7",
        "axis_m": [
          1.4254238568483205e-06,
          -0.9999999999902353,
          4.183023051496094e-06
        ],
        "axis_other_aligned": [
          -4.714530472811464e-05,
          -0.9999999297234742,
          0.00037192790573844424
        ],
        "angle_rad": 0.00037093856759959235,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "joint8",
        "joint_other": "joint8",
        "axis_m": [
          -7.027586644061581e-06,
          -0.9999999999693772,
          3.443651204859677e-06
        ],
        "axis_other_aligned": [
          -5.446374344990247e-05,
          -0.9999999295896667,
          0.0003712874390497149
        ],
        "angle_rad": 0.00037088980541225686,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      }
    ],
    "axis_disagreements": [],
    "com_eligible": false,
    "covariance_singular_values": [
      0.16171614766858694,
      0.036528702871329165,
      1.3160343251927083e-06
    ],
    "origin_residuals_m": {
      "link1": 0.006632792899511778,
      "link2": 0.006632792899511778,
      "link3": 0.0033043128982732993,
      "link4": 0.003314413293325584,
      "link5": 0.003314413293325584,
      "link6": 0.0033176063583781152,
      "link7": 0.0033235862552212906,
      "link8": 0.0033235862552212906,
      "base_link": 0.006632430732179797
    },
    "reason": "Origin residual exceeds threshold and/or matched signed joint axes disagree"
  }
}
```


## Every reported quantity difference

Counts are quantity records, including correlated total/subtree/body mass records; they are not independent robot defects.

| Entity / quantity | M | S | H | H − M | Class | M source | S source | H source |
|---|---|---|---|---|---|---|---|---|
| robot / total_mass | 2.3669165 | unavailable | 1.36210343 | -1.00481307 | NO MATCHING SOURCE | [aggregate inputs](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/agilex_piper/piper.xml#L1) | unavailable | [aggregate inputs](https://github.com/agilexrobotics/Piper_ros/blob/ac41fcbcdda598f01b51cf6175ed9a24d0dacadc/src/piper_description/urdf/piper_description_v100.urdf#L1) |
| base_link / subtree_mass | 2.3669165 | unavailable | 1.36210343 | -1.00481307 | NO MATCHING SOURCE | [subtree root L119](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/agilex_piper/piper.xml#L119) | unavailable | [subtree root L3](https://github.com/agilexrobotics/Piper_ros/blob/ac41fcbcdda598f01b51cf6175ed9a24d0dacadc/src/piper_description/urdf/piper_description_v100.urdf#L3) |
| link1 / subtree_mass | 2.2043675 | unavailable | 1.19955486 | -1.00481264 | NO MATCHING SOURCE | [subtree root L124](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/agilex_piper/piper.xml#L124) | unavailable | [subtree root L34](https://github.com/agilexrobotics/Piper_ros/blob/ac41fcbcdda598f01b51cf6175ed9a24d0dacadc/src/piper_description/urdf/piper_description_v100.urdf#L34) |
| link2 / subtree_mass | 2.1064995 | unavailable | 1.10168687 | -1.00481263 | NO MATCHING SOURCE | [subtree root L130](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/agilex_piper/piper.xml#L130) | unavailable | [subtree root L72](https://github.com/agilexrobotics/Piper_ros/blob/ac41fcbcdda598f01b51cf6175ed9a24d0dacadc/src/piper_description/urdf/piper_description_v100.urdf#L72) |
| link3 / subtree_mass | 1.8156105 | unavailable | 0.810797927 | -1.00481257 | NO MATCHING SOURCE | [subtree root L167](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/agilex_piper/piper.xml#L167) | unavailable | [subtree root L110](https://github.com/agilexrobotics/Piper_ros/blob/ac41fcbcdda598f01b51cf6175ed9a24d0dacadc/src/piper_description/urdf/piper_description_v100.urdf#L110) |
| link4 / subtree_mass | 1.5247625 | unavailable | 0.519950229 | -1.00481227 | NO MATCHING SOURCE | [subtree root L200](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/agilex_piper/piper.xml#L200) | unavailable | [subtree root L148](https://github.com/agilexrobotics/Piper_ros/blob/ac41fcbcdda598f01b51cf6175ed9a24d0dacadc/src/piper_description/urdf/piper_description_v100.urdf#L148) |
| link5 / subtree_mass | 1.3976755 | unavailable | 0.39286288 | -1.00481262 | NO MATCHING SOURCE | [subtree root L210](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/agilex_piper/piper.xml#L210) | unavailable | [subtree root L186](https://github.com/agilexrobotics/Piper_ros/blob/ac41fcbcdda598f01b51cf6175ed9a24d0dacadc/src/piper_description/urdf/piper_description_v100.urdf#L186) |
| link5 / principal_moments | [0.001, 0.001, 0.001] | unavailable | [4.39642485e-05, 4.88652218e-05, 5.63237196e-05] | [-0.000956035751, -0.000951134778, -0.00094367628] | NO MATCHING SOURCE | [inertia input L212](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/agilex_piper/piper.xml#L212) | unavailable | [inertia input L198](https://github.com/agilexrobotics/Piper_ros/blob/ac41fcbcdda598f01b51cf6175ed9a24d0dacadc/src/piper_description/urdf/piper_description_v100.urdf#L198) |
| link6 / mass | 1.2 | unavailable | 0.195187143 | -1.00481286 | NO MATCHING SOURCE | [input L224](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/agilex_piper/piper.xml#L224) | unavailable | [input L229](https://github.com/agilexrobotics/Piper_ros/blob/ac41fcbcdda598f01b51cf6175ed9a24d0dacadc/src/piper_description/urdf/piper_description_v100.urdf#L229) |
| link6 / subtree_mass | 1.2529645 | unavailable | 0.248151638 | -1.00481286 | NO MATCHING SOURCE | [subtree root L222](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/agilex_piper/piper.xml#L222) | unavailable | [subtree root L224](https://github.com/agilexrobotics/Piper_ros/blob/ac41fcbcdda598f01b51cf6175ed9a24d0dacadc/src/piper_description/urdf/piper_description_v100.urdf#L224) |
| link6 / principal_moments | [0.001, 0.001, 0.001] | unavailable | [6.43536034e-05, 0.00012596511, 0.000154293785] | [-0.000935646397, -0.00087403489, -0.000845706215] | NO MATCHING SOURCE | [inertia input L224](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/agilex_piper/piper.xml#L224) | unavailable | [inertia input L236](https://github.com/agilexrobotics/Piper_ros/blob/ac41fcbcdda598f01b51cf6175ed9a24d0dacadc/src/piper_description/urdf/piper_description_v100.urdf#L236) |
| link7 / principal_moments | [0.001, 0.001, 0.001] | unavailable | [5.87020869e-06, 1.00040628e-05, 1.45133962e-05] | [-0.000994129791, -0.000989995937, -0.000985486604] | NO MATCHING SOURCE | [inertia input L230](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/agilex_piper/piper.xml#L230) | unavailable | [inertia input L274](https://github.com/agilexrobotics/Piper_ros/blob/ac41fcbcdda598f01b51cf6175ed9a24d0dacadc/src/piper_description/urdf/piper_description_v100.urdf#L274) |
| link8 / principal_moments | [0.001, 0.001, 0.001] | unavailable | [5.87021108e-06, 1.00039789e-05, 1.45133184e-05] | [-0.000994129789, -0.000989996021, -0.000985486682] | NO MATCHING SOURCE | [inertia input L238](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/agilex_piper/piper.xml#L238) | unavailable | [inertia input L312](https://github.com/agilexrobotics/Piper_ros/blob/ac41fcbcdda598f01b51cf6175ed9a24d0dacadc/src/piper_description/urdf/piper_description_v100.urdf#L312) |
| joint7 / range | [0, 0.035] | unavailable | [0, 0.05] | [0, 0.015] | NO MATCHING SOURCE | [input L231](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/agilex_piper/piper.xml#L231) | unavailable | [input L297](https://github.com/agilexrobotics/Piper_ros/blob/ac41fcbcdda598f01b51cf6175ed9a24d0dacadc/src/piper_description/urdf/piper_description_v100.urdf#L297) |
| joint7 / effort | 10 | unavailable | 100 | 90 | NO MATCHING SOURCE | [inherited actuator input L12](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/agilex_piper/piper.xml#L12) | unavailable | [input L297](https://github.com/agilexrobotics/Piper_ros/blob/ac41fcbcdda598f01b51cf6175ed9a24d0dacadc/src/piper_description/urdf/piper_description_v100.urdf#L297) |
| joint8 / range | [-0.035, 0] | unavailable | [-0.05, 0] | [-0.015, 0] | NO MATCHING SOURCE | [input L239](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/agilex_piper/piper.xml#L239) | unavailable | [input L335](https://github.com/agilexrobotics/Piper_ros/blob/ac41fcbcdda598f01b51cf6175ed9a24d0dacadc/src/piper_description/urdf/piper_description_v100.urdf#L335) |

## Raw CoM records and reporting decisions

Raw values retain the previous root-anchor registration before Kabsch; original world coordinates also remain in the snapshots. Eligible findings above use the fitted transform into M. Excluded raw records below are diagnostic numbers, not findings. No CoM suppression applies to mass or principal inertia moments.

| Entity / quantity | Raw M | Raw S | Raw H | Raw H − M | Decision | M source | S source | H source |
|---|---|---|---|---|---|---|---|---|
| robot / total_com_registered | [0.00496370257, 0.00708199852, 0.175493165] | unavailable | [-0.054629303, 0.000682110722, 0.162503915] | [-0.0595930056, -0.00639988779, -0.0129892495] | M/H: kinematic convention differs | [aggregate inputs](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/agilex_piper/piper.xml#L1) | unavailable | [aggregate inputs](https://github.com/agilexrobotics/Piper_ros/blob/ac41fcbcdda598f01b51cf6175ed9a24d0dacadc/src/piper_description/urdf/piper_description_v100.urdf#L1) |
| base_link / com_registered | [-0.00979275, 1.82906e-06, 0.04101] | unavailable | [-0.00979274766, 1.82905828e-06, 0.0410100126] | [2.34044659e-09, -1.72412862e-12, 1.26360189e-08] | M/H: kinematic convention differs | [CoM/kinematic input L121](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/agilex_piper/piper.xml#L121) | unavailable | [CoM/kinematic input L7](https://github.com/agilexrobotics/Piper_ros/blob/ac41fcbcdda598f01b51cf6175ed9a24d0dacadc/src/piper_description/urdf/piper_description_v100.urdf#L7) |
| link1 / com_registered | [0.000310283413, -0.00131676132, 0.11377125] | unavailable | [0.000310284005, -0.00131676146, 0.113771255] | [5.91820359e-10, -1.42582506e-10, 4.87696564e-09] | M/H: kinematic convention differs | [CoM/kinematic input L126](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/agilex_piper/piper.xml#L126) | unavailable | [CoM/kinematic input L38](https://github.com/agilexrobotics/Piper_ros/blob/ac41fcbcdda598f01b51cf6175ed9a24d0dacadc/src/piper_description/urdf/piper_description_v100.urdf#L38) |
| link2 / com_registered | [-0.148793986, 0.00175276677, 0.120579723] | unavailable | [-0.148787414, 0.00175263055, 0.125774082] | [6.57181994e-06, -1.36226634e-07, 0.00519435868] | M/H: kinematic convention differs | [CoM/kinematic input L132](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/agilex_piper/piper.xml#L132) | unavailable | [CoM/kinematic input L76](https://github.com/agilexrobotics/Piper_ros/blob/ac41fcbcdda598f01b51cf6175ed9a24d0dacadc/src/piper_description/urdf/piper_description_v100.urdf#L76) |
| link3 / com_registered | [-0.180882013, 0.000509730745, 0.176449798] | unavailable | [-0.179706694, 0.000509555457, 0.186329205] | [0.00117531905, -1.75288314e-07, 0.00987940619] | M/H: kinematic convention differs | [CoM/kinematic input L169](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/agilex_piper/piper.xml#L169) | unavailable | [CoM/kinematic input L114](https://github.com/agilexrobotics/Piper_ros/blob/ac41fcbcdda598f01b51cf6175ed9a24d0dacadc/src/piper_description/urdf/piper_description_v100.urdf#L114) |
| link4 / com_registered | [-0.0404327744, 0.00102867702, 0.195344976] | unavailable | [-0.03925747, 0.00102863927, 0.205224319] | [0.00117530432, -3.7748969e-08, 0.00987934269] | M/H: kinematic convention differs | [CoM/kinematic input L202](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/agilex_piper/piper.xml#L202) | unavailable | [CoM/kinematic input L152](https://github.com/agilexrobotics/Piper_ros/blob/ac41fcbcdda598f01b51cf6175ed9a24d0dacadc/src/piper_description/urdf/piper_description_v100.urdf#L152) |
| link5 / com_registered | [0.0207612317, -0.00196099529, 0.200508576] | unavailable | [0.0219365371, -0.00196103475, 0.21038789] | [0.00117530535, -3.94563513e-08, 0.00987931328] | M/H: kinematic convention differs | [CoM/kinematic input L212](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/agilex_piper/piper.xml#L212) | unavailable | [CoM/kinematic input L190](https://github.com/agilexrobotics/Piper_ros/blob/ac41fcbcdda598f01b51cf6175ed9a24d0dacadc/src/piper_description/urdf/piper_description_v100.urdf#L190) |
| link6 / com_registered | [0.0864735096, 0.0135924927, 0.205132566] | unavailable | [0.086497898, 0.00244750858, 0.228169098] | [2.43883728e-05, -0.0111449842, 0.0230365325] | M/H: kinematic convention differs | [CoM/kinematic input L224](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/agilex_piper/piper.xml#L224) | unavailable | [CoM/kinematic input L228](https://github.com/agilexrobotics/Piper_ros/blob/ac41fcbcdda598f01b51cf6175ed9a24d0dacadc/src/piper_description/urdf/piper_description_v100.urdf#L228) |
| link7 / com_registered | [0.142906722, -0.0077942321, 0.210825077] | unavailable | [0.144081954, -0.00779464805, 0.220704649] | [0.00117523224, -4.15948013e-07, 0.00987957163] | M/H: kinematic convention differs | [CoM/kinematic input L230](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/agilex_piper/piper.xml#L230) | unavailable | [CoM/kinematic input L266](https://github.com/agilexrobotics/Piper_ros/blob/ac41fcbcdda598f01b51cf6175ed9a24d0dacadc/src/piper_description/urdf/piper_description_v100.urdf#L266) |
| link8 / com_registered | [0.142858261, 0.010626757, 0.21137848] | unavailable | [0.144033595, 0.0106262934, 0.221258056] | [0.0011753337, -4.63611402e-07, 0.00987957631] | M/H: kinematic convention differs | [CoM/kinematic input L238](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/agilex_piper/piper.xml#L238) | unavailable | [CoM/kinematic input L304](https://github.com/agilexrobotics/Piper_ros/blob/ac41fcbcdda598f01b51cf6175ed9a24d0dacadc/src/piper_description/urdf/piper_description_v100.urdf#L304) |

## Mass accounting

Every contributing compiled body mass is listed here so total/subtree sums can be checked. Links point to explicit inertials or to geometry inputs when the compiler inferred a mass. CoM links identify inertial inputs; world coordinates additionally use the ancestor transforms and the registration recorded below.

| M body | M kg / source | S kg / source | H kg / source |
|---|---|---|---|
| base_link | 0.162549 / [input L121](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/agilex_piper/piper.xml#L121) | unavailable | 0.162548567 / [input L8](https://github.com/agilexrobotics/Piper_ros/blob/ac41fcbcdda598f01b51cf6175ed9a24d0dacadc/src/piper_description/urdf/piper_description_v100.urdf#L8) |
| link1 | 0.097868 / [input L126](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/agilex_piper/piper.xml#L126) | unavailable | 0.0978679932 / [input L39](https://github.com/agilexrobotics/Piper_ros/blob/ac41fcbcdda598f01b51cf6175ed9a24d0dacadc/src/piper_description/urdf/piper_description_v100.urdf#L39) |
| link2 | 0.290889 / [input L132](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/agilex_piper/piper.xml#L132) | unavailable | 0.290888939 / [input L77](https://github.com/agilexrobotics/Piper_ros/blob/ac41fcbcdda598f01b51cf6175ed9a24d0dacadc/src/piper_description/urdf/piper_description_v100.urdf#L77) |
| link3 | 0.290848 / [input L169](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/agilex_piper/piper.xml#L169) | unavailable | 0.290847698 / [input L115](https://github.com/agilexrobotics/Piper_ros/blob/ac41fcbcdda598f01b51cf6175ed9a24d0dacadc/src/piper_description/urdf/piper_description_v100.urdf#L115) |
| link4 | 0.127087 / [input L202](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/agilex_piper/piper.xml#L202) | unavailable | 0.127087348 / [input L153](https://github.com/agilexrobotics/Piper_ros/blob/ac41fcbcdda598f01b51cf6175ed9a24d0dacadc/src/piper_description/urdf/piper_description_v100.urdf#L153) |
| link5 | 0.144711 / [input L212](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/agilex_piper/piper.xml#L212) | unavailable | 0.144711243 / [input L191](https://github.com/agilexrobotics/Piper_ros/blob/ac41fcbcdda598f01b51cf6175ed9a24d0dacadc/src/piper_description/urdf/piper_description_v100.urdf#L191) |
| link6 | 1.2 / [input L224](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/agilex_piper/piper.xml#L224) | unavailable | 0.195187143 / [input L229](https://github.com/agilexrobotics/Piper_ros/blob/ac41fcbcdda598f01b51cf6175ed9a24d0dacadc/src/piper_description/urdf/piper_description_v100.urdf#L229) |
| link7 | 0.0264823 / [input L230](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/agilex_piper/piper.xml#L230) | unavailable | 0.0264822923 / [input L267](https://github.com/agilexrobotics/Piper_ros/blob/ac41fcbcdda598f01b51cf6175ed9a24d0dacadc/src/piper_description/urdf/piper_description_v100.urdf#L267) |
| link8 | 0.0264822 / [input L238](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/agilex_piper/piper.xml#L238) | unavailable | 0.0264822021 / [input L305](https://github.com/agilexrobotics/Piper_ros/blob/ac41fcbcdda598f01b51cf6175ed9a24d0dacadc/src/piper_description/urdf/piper_description_v100.urdf#L305) |

## Coverage and unmatched elements

```json
{
  "mapping_h": {
    "bodies": {
      "link1": "link1",
      "link2": "link2",
      "link3": "link3",
      "link4": "link4",
      "link5": "link5",
      "link6": "link6",
      "link7": "link7",
      "link8": "link8",
      "base_link": "arm_base"
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
      "link1": "name",
      "link2": "name",
      "link3": "name",
      "link4": "name",
      "link5": "name",
      "link6": "name",
      "link7": "name",
      "link8": "name",
      "base_link": "unique kinematic subtree"
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
      "H": "arm_base",
      "root_unmatched": false
    }
  },
  "mapping_s": null,
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
      "other": 3.0,
      "s": null,
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
      "other": 3.0,
      "s": null,
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
      "other": 3.0,
      "s": null,
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
      "other": 3.0,
      "s": null,
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
      "other": 3.0,
      "s": null,
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
      "other": 3.0,
      "s": null,
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
      "other": 1.0,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "joint8",
      "other_entity": "joint8",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": 100.0,
      "s": null,
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
      "other": 1.0,
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
| joint1 / force | 100 | unavailable | unavailable |
| joint1 / velocity | unavailable | unavailable | 3 |
| joint2 / force | 100 | unavailable | unavailable |
| joint2 / velocity | unavailable | unavailable | 3 |
| joint3 / force | 100 | unavailable | unavailable |
| joint3 / velocity | unavailable | unavailable | 3 |
| joint4 / force | 100 | unavailable | unavailable |
| joint4 / velocity | unavailable | unavailable | 3 |
| joint5 / force | 100 | unavailable | unavailable |
| joint5 / velocity | unavailable | unavailable | 3 |
| joint6 / force | 100 | unavailable | unavailable |
| joint6 / velocity | unavailable | unavailable | 3 |
| joint7 / force | 10 | unavailable | unavailable |
| joint7 / velocity | unavailable | unavailable | 1 |
| joint8 / effort | unavailable | unavailable | 100 |
| joint8 / force | unavailable | unavailable | unavailable |
| joint8 / velocity | unavailable | unavailable | 1 |
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
  "https://github.com/agilexrobotics/Piper_ros src/piper_description/urdf/piper_description_v100_camera.urdf at ac41fcbcdda598f01b51cf6175ed9a24d0dacadc: ValueError: $(find piper_camera_moveit_config) is outside the cloned repository",
  "https://github.com/agilexrobotics/Piper_ros src/piper_description/urdf/piper_description_with_camera.xacro at ac41fcbcdda598f01b51cf6175ed9a24d0dacadc: ValueError: $(find piper_camera_moveit_config) is outside the cloned repository"
]
```

## Self comparisons

```json
[
  {
    "file": "agilex_piper/piper.xml",
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
      "NO MATCHING SOURCE": 16
    },
    "classifications_changed": 0,
    "finding_membership_changes": 0
  },
  "2": {
    "provenance_method": "none",
    "counts": {
      "NO MATCHING SOURCE": 16
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
  "self_variants_recompiled": 1,
  "historical_snapshots_reused": 1,
  "primary_physics_unchanged": true,
  "source_matching": "original raw-value provenance criteria retained; kinematic guard applies to reported CoM"
}
```
