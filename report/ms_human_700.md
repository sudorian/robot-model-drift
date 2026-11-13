# ms_human_700

Status: **complete**. Provenance: **dated match**, confidence **medium**.

Source selected using the ordered amended provenance rules.

M: `https://github.com/google-deepmind/mujoco_menagerie`, `ms_human_700/MS-Human-700-Manipulation.xml`, commit `370c43965323c0944b433b202aac5058b5f907a9`.
H: `https://github.com/LNSGroup/MS-Human-700`, `MS-Human-700-Manipulation.xml`, commit `2d686957aefd5739cf4d2859a6acfd94c8f84400`.
S: `4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d` (2026-02-25T16:10:23+08:00). Menagerie release/change: 2026-04-06T19:50:56+08:00.

Limit semantics: MJCF effort values are supported actuator torque/force envelopes. URDF effort and velocity values are manufacturer declarations retained from XML; MuJoCo does not enforce those tags. Such declaration comparisons are explicitly distinct from compiled inertial/range quantities.


## Source evidence

```json
[
  {
    "url": "https://github.com/LNSGroup/MS-Human-700",
    "document": "ms_human_700/README.md",
    "commit": "370c43965323c0944b433b202aac5058b5f907a9",
    "current": true
  }
]
```


## Kinematics consistency

A proper Kabsch rigid transform aligns all matched zero-pose body origins. The maximum per-origin residual and signed hinge/slide axis angles determine whether CoM can be compared; RMS is also recorded. Fewer than three non-collinear origins give insufficient kinematic coverage. CoM records that fail either required M/H or M/S check are excluded from counts and largest discrepancies. Masses, principal moments and raw joint ranges remain unchanged; a flagged range still requires convention review.

| Pair | Status | Origins / rank | RMS / maximum mm | Disagreeing / checked axes |
|---|---|---:|---:|---:|
| M/H | consistent | 129 / 3 | 2.05296126e-13 / 4.8013937e-13 | 0 / 48 |
| M/S | consistent | 129 / 3 | 2.05296126e-13 / 4.8013937e-13 | 0 / 48 |

Exact fitted transforms, per-origin residuals, thresholds and axis vectors:

```json
{
  "M/H": {
    "status": "consistent",
    "matched_body_origins": 129,
    "position_threshold_m": 0.005,
    "axis_threshold_rad": 0.005,
    "residual_definition": "maximum Euclidean residual over matched body origins; Kabsch minimizes RMS, which is also recorded",
    "coordinate_frames": "each snapshot registered to its matched report anchor",
    "anchor_m": "pelvis",
    "anchor_other": "pelvis",
    "rotation_other_to_m": [
      [
        0.9999999999999999,
        -2.807754441850095e-17,
        2.3331766229069473e-16
      ],
      [
        1.0455477107111144e-16,
        0.9999999999999996,
        1.3981393759945259e-16
      ],
      [
        -3.885780586188048e-16,
        -8.673617379884035e-17,
        0.9999999999999993
      ]
    ],
    "translation_other_to_m": [
      -6.938893903907228e-18,
      2.7755575615628914e-17,
      -5.204170427930421e-18
    ],
    "rms_residual_m": 2.0529612592073526e-16,
    "max_residual_m": 4.801393697075383e-16,
    "fit_rank": 3,
    "axis_checks": [
      {
        "joint_m": "sternoclavicular_r2_r",
        "joint_other": "sternoclavicular_r2_r",
        "axis_m": [
          -0.023328076082097478,
          0.9904072301057558,
          -0.1361958862100926
        ],
        "axis_other_aligned": [
          -0.023328076082097544,
          0.9904072301057558,
          -0.13619588621009265
        ],
        "angle_rad": 8.653210372566878e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "sternoclavicular_r3_r",
        "joint_other": "sternoclavicular_r3_r",
        "axis_m": [
          -0.9306888527188436,
          -0.07124305061133122,
          -0.3588073120276037
        ],
        "axis_other_aligned": [
          -0.9306888527188437,
          -0.07124305061133136,
          -0.3588073120276032
        ],
        "angle_rad": 5.2222956368572725e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "unrotscap_r3_r",
        "joint_other": "unrotscap_r3_r",
        "axis_m": [
          -0.9306888527188436,
          -0.07124305061133122,
          -0.3588073120276037
        ],
        "axis_other_aligned": [
          -0.9306888527188437,
          -0.07124305061133136,
          -0.3588073120276032
        ],
        "angle_rad": 5.2222956368572725e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "unrotscap_r2_r",
        "joint_other": "unrotscap_r2_r",
        "axis_m": [
          -0.023328076082097478,
          0.9904072301057558,
          -0.1361958862100926
        ],
        "axis_other_aligned": [
          -0.023328076082097544,
          0.9904072301057558,
          -0.13619588621009265
        ],
        "angle_rad": 8.653210372566878e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "acromioclavicular_r2_r",
        "joint_other": "acromioclavicular_r2_r",
        "axis_m": [
          0.05946790230964638,
          0.9545920900456824,
          -0.29192038335324644
        ],
        "axis_other_aligned": [
          0.0594679023096463,
          0.9545920900456822,
          -0.29192038335324644
        ],
        "angle_rad": 7.351626287044711e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "acromioclavicular_r3_r",
        "joint_other": "acromioclavicular_r3_r",
        "axis_m": [
          -0.7208547250965776,
          0.24328413468601107,
          0.6489848188640598
        ],
        "axis_other_aligned": [
          -0.7208547250965776,
          0.243284134686011,
          0.6489848188640598
        ],
        "angle_rad": 6.206335383118183e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "acromioclavicular_r1_r",
        "joint_other": "acromioclavicular_r1_r",
        "axis_m": [
          0.6905116116648125,
          0.17180473339016292,
          0.7026214113879525
        ],
        "axis_other_aligned": [
          0.6905116116648129,
          0.17180473339016314,
          0.7026214113879521
        ],
        "angle_rad": 6.550551057807855e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "unrothum_r1_r",
        "joint_other": "unrothum_r1_r",
        "axis_m": [
          0.6905116116648125,
          0.17180473339016292,
          0.7026214113879525
        ],
        "axis_other_aligned": [
          0.6905116116648129,
          0.17180473339016314,
          0.7026214113879521
        ],
        "angle_rad": 6.550551057807855e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "unrothum_r3_r",
        "joint_other": "unrothum_r3_r",
        "axis_m": [
          -0.7208547250965776,
          0.24328413468601107,
          0.6489848188640598
        ],
        "axis_other_aligned": [
          -0.7208547250965776,
          0.243284134686011,
          0.6489848188640598
        ],
        "angle_rad": 6.206335383118183e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "unrothum_r2_r",
        "joint_other": "unrothum_r2_r",
        "axis_m": [
          0.05946790230964638,
          0.9545920900456824,
          -0.29192038335324644
        ],
        "axis_other_aligned": [
          0.0594679023096463,
          0.9545920900456822,
          -0.29192038335324644
        ],
        "angle_rad": 7.351626287044711e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "elv_angle_r",
        "joint_other": "elv_angle_r",
        "axis_m": [
          -0.06780332743512969,
          0.9968218361558799,
          0.04182027919018272
        ],
        "axis_other_aligned": [
          -0.06780332743512972,
          0.9968218361558799,
          0.04182027919018265
        ],
        "angle_rad": 7.498039971595757e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "shoulder_elv_r",
        "joint_other": "shoulder_elv_r",
        "axis_m": [
          -0.9866183831797913,
          -0.07321765555013006,
          0.14568232867248154
        ],
        "axis_other_aligned": [
          -0.9866183831797913,
          -0.0732176555501301,
          0.14568232867248185
        ],
        "angle_rad": 3.085321648821679e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "shoulder1_r2_r",
        "joint_other": "shoulder1_r2_r",
        "axis_m": [
          -0.06780332743512969,
          0.9968218361558799,
          0.04182027919018272
        ],
        "axis_other_aligned": [
          -0.06780332743512972,
          0.9968218361558799,
          0.04182027919018265
        ],
        "angle_rad": 7.498039971595757e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "shoulder_rot_r",
        "joint_other": "shoulder_rot_r",
        "axis_m": [
          -0.06780332743512969,
          0.9968218361558799,
          0.04182027919018272
        ],
        "axis_other_aligned": [
          -0.06780332743512972,
          0.9968218361558799,
          0.04182027919018265
        ],
        "angle_rad": 7.498039971595757e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "elbow_flexion_r",
        "joint_other": "elbow_flexion_r",
        "axis_m": [
          0.13301628840283014,
          0.04688931329049195,
          0.9900040703546028
        ],
        "axis_other_aligned": [
          0.13301628840283042,
          0.04688931329049212,
          0.9900040703546027
        ],
        "angle_rad": 3.2742187586505674e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "pro_sup_r",
        "joint_other": "pro_sup_r",
        "axis_m": [
          -0.10321128619189612,
          0.9876690682082944,
          -0.11771678770325915
        ],
        "axis_other_aligned": [
          -0.10321128619189622,
          0.9876690682082944,
          -0.11771678770325918
        ],
        "angle_rad": 1.0140345331252273e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "deviation_r",
        "joint_other": "deviation_r",
        "axis_m": [
          -0.8516612801697739,
          -0.2012013308257751,
          -0.4839329378473001
        ],
        "axis_other_aligned": [
          -0.8516612801697743,
          -0.2012013308257752,
          -0.4839329378472996
        ],
        "angle_rad": 6.300271117485416e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "flexion_r",
        "joint_other": "flexion_r",
        "axis_m": [
          0.9820415468042459,
          -0.17777074489107225,
          0.06318198011456644
        ],
        "axis_other_aligned": [
          0.9820415468042459,
          -0.17777074489107209,
          0.06318198011456605
        ],
        "angle_rad": 4.2030814102805256e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "wrist_hand_r1_r",
        "joint_other": "wrist_hand_r1_r",
        "axis_m": [
          0.8967960779322267,
          -0.28142546250060774,
          -0.34140372531900504
        ],
        "axis_other_aligned": [
          0.8967960779322267,
          -0.2814254625006075,
          -0.3414037253190052
        ],
        "angle_rad": 2.3592239273284576e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "wrist_hand_r3_r",
        "joint_other": "wrist_hand_r3_r",
        "axis_m": [
          0.9830828652717561,
          0.08598504433218035,
          -0.16172399995135953
        ],
        "axis_other_aligned": [
          0.983082865271756,
          0.08598504433218038,
          -0.16172399995135983
        ],
        "angle_rad": 3.363037852658521e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "cmc_flexion",
        "joint_other": "cmc_flexion",
        "axis_m": [
          -0.07344194500752081,
          0.6616103078649415,
          -0.7462426423358356
        ],
        "axis_other_aligned": [
          -0.07344194500752103,
          0.6616103078649415,
          -0.7462426423358355
        ],
        "angle_rad": 2.332541980949955e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "cmc_abduction",
        "joint_other": "cmc_abduction",
        "axis_m": [
          0.4770492845499966,
          0.770394287765569,
          0.4229853679366677
        ],
        "axis_other_aligned": [
          0.47704928454999684,
          0.7703942877655691,
          0.42298536793666724
        ],
        "angle_rad": 5.064917260848195e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "mp_flexion",
        "joint_other": "mp_flexion",
        "axis_m": [
          -0.016573578819913302,
          0.20281462182568985,
          -0.9790768844471831
        ],
        "axis_other_aligned": [
          -0.016573578819913545,
          0.20281462182568977,
          -0.9790768844471831
        ],
        "angle_rad": 2.552789414337386e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "ip_flexion",
        "joint_other": "ip_flexion",
        "axis_m": [
          -0.06297487662564752,
          0.47620558120992046,
          -0.8770760567581961
        ],
        "axis_other_aligned": [
          -0.06297487662564777,
          0.4762055812099204,
          -0.8770760567581961
        ],
        "angle_rad": 2.5909591973639336e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "2mcp_abduction",
        "joint_other": "2mcp_abduction",
        "axis_m": [
          0.2817848689300059,
          0.21363852970067548,
          0.9353907559247274
        ],
        "axis_other_aligned": [
          0.2817848689300062,
          0.21363852970067565,
          0.9353907559247273
        ],
        "angle_rad": 3.390840864445248e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "2mcp_flexion",
        "joint_other": "2mcp_flexion",
        "axis_m": [
          0.9541970315101842,
          0.09917720047301809,
          -0.282262126335588
        ],
        "axis_other_aligned": [
          0.9541970315101842,
          0.09917720047301812,
          -0.2822621263355883
        ],
        "angle_rad": 2.7971575570698805e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "2pm_flexion",
        "joint_other": "2pm_flexion",
        "axis_m": [
          0.9448448639590873,
          0.19940637248118728,
          -0.2598177855036641
        ],
        "axis_other_aligned": [
          0.9448448639590872,
          0.1994063724811873,
          -0.25981778550366436
        ],
        "angle_rad": 3.140951470513929e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "2md_flexion",
        "joint_other": "2md_flexion",
        "axis_m": [
          0.974946329860523,
          0.22215123934181055,
          -0.011334934953230985
        ],
        "axis_other_aligned": [
          0.974946329860523,
          0.2221512393418106,
          -0.011334934953231377
        ],
        "angle_rad": 3.95193699647667e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "3mcp_abduction",
        "joint_other": "3mcp_abduction",
        "axis_m": [
          0.055839491188762275,
          0.12351926194185028,
          0.9907698739632331
        ],
        "axis_other_aligned": [
          0.05583949118876254,
          0.12351926194185044,
          0.990769873963233
        ],
        "angle_rad": 3.1867960929430274e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "3mcp_flexion",
        "joint_other": "3mcp_flexion",
        "axis_m": [
          0.9875997535185798,
          0.12309764181608948,
          -0.09743560657869581
        ],
        "axis_other_aligned": [
          0.9875997535185796,
          0.12309764181608951,
          -0.09743560657869613
        ],
        "angle_rad": 3.376299569779874e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "3pm_flexion",
        "joint_other": "3pm_flexion",
        "axis_m": [
          0.9997803109886432,
          0.014348495363896735,
          0.015279085059134938
        ],
        "axis_other_aligned": [
          0.9997803109886432,
          0.014348495363896836,
          0.015279085059134539
        ],
        "angle_rad": 4.1154063119141427e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "3md_flexion",
        "joint_other": "3md_flexion",
        "axis_m": [
          0.9936239160105462,
          0.11226928600353216,
          0.010349925223116722
        ],
        "axis_other_aligned": [
          0.9936239160105462,
          0.11226928600353223,
          0.010349925223116322
        ],
        "angle_rad": 4.0755163990155153e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "4cmc_flexion",
        "joint_other": "4cmc_flexion",
        "axis_m": [
          0.6241124359432589,
          -0.7551510418175946,
          -0.20057560006833555
        ],
        "axis_other_aligned": [
          0.624112435943259,
          -0.7551510418175945,
          -0.20057560006833564
        ],
        "angle_rad": 1.8824747269678055e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "4mcp_abduction",
        "joint_other": "4mcp_abduction",
        "axis_m": [
          0.053009413439229866,
          0.1488461099164688,
          0.9874385234785826
        ],
        "axis_other_aligned": [
          0.053009413439230116,
          0.14884610991646896,
          0.9874385234785826
        ],
        "angle_rad": 3.0150272531948617e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "4mcp_flexion",
        "joint_other": "4mcp_flexion",
        "axis_m": [
          0.993122669544568,
          0.010400643412515528,
          -0.11661556436975554
        ],
        "axis_other_aligned": [
          0.993122669544568,
          0.010400643412515615,
          -0.11661556436975587
        ],
        "angle_rad": 3.4424107053751306e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "4pm_flexion",
        "joint_other": "4pm_flexion",
        "axis_m": [
          0.9991116393820398,
          0.04182302782492728,
          0.005173624927265578
        ],
        "axis_other_aligned": [
          0.99911163938204,
          0.04182302782492738,
          0.005173624927265184
        ],
        "angle_rad": 4.0594488325762537e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "4md_flexion",
        "joint_other": "4md_flexion",
        "axis_m": [
          0.9803649425936615,
          -0.06536383413705772,
          0.18604340493613353
        ],
        "axis_other_aligned": [
          0.9803649425936616,
          -0.06536383413705758,
          0.18604340493613308
        ],
        "angle_rad": 4.652811653304674e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "CMC5_r1",
        "joint_other": "CMC5_r1",
        "axis_m": [
          0.4643723212269116,
          -0.8334242229387436,
          0.29960375814946233
        ],
        "axis_other_aligned": [
          0.46437232122691174,
          -0.8334242229387435,
          0.29960375814946216
        ],
        "angle_rad": 2.3221980631040627e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "5mcp_abduction",
        "joint_other": "5mcp_abduction",
        "axis_m": [
          0.04348720476586676,
          0.22016733676098177,
          0.9744922815729369
        ],
        "axis_other_aligned": [
          0.04348720476586701,
          0.22016733676098196,
          0.9744922815729369
        ],
        "angle_rad": 2.981757037776785e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "5mcp_flexion",
        "joint_other": "5mcp_flexion",
        "axis_m": [
          0.9830116880470507,
          -0.13923433516784692,
          -0.11959022147841102
        ],
        "axis_other_aligned": [
          0.9830116880470507,
          -0.13923433516784678,
          -0.11959022147841132
        ],
        "angle_rad": 3.4051875089965907e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "5pm_flexion",
        "joint_other": "5pm_flexion",
        "axis_m": [
          0.9623157051720419,
          -0.2548300600528955,
          0.09492167335584373
        ],
        "axis_other_aligned": [
          0.962315705172042,
          -0.2548300600528953,
          0.09492167335584334
        ],
        "angle_rad": 4.3021142204224816e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "5md_flexion",
        "joint_other": "5md_flexion",
        "axis_m": [
          0.9318759880761684,
          -0.3566806166079947,
          0.06622749114382655
        ],
        "axis_other_aligned": [
          0.9318759880761684,
          -0.3566806166079945,
          0.06622749114382619
        ],
        "angle_rad": 4.1540741810552243e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "objTx",
        "joint_other": "objTx",
        "axis_m": [
          1.0,
          0.0,
          0.0
        ],
        "axis_other_aligned": [
          1.0,
          1.0455477107111145e-16,
          -3.885780586188048e-16
        ],
        "angle_rad": 4.023985683295752e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "objTy",
        "joint_other": "objTy",
        "axis_m": [
          0.0,
          0.0,
          -1.0
        ],
        "axis_other_aligned": [
          -2.333176622906949e-16,
          -1.3981393759945268e-16,
          -1.0
        ],
        "angle_rad": 2.7200196448529264e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "objTz",
        "joint_other": "objTz",
        "axis_m": [
          0.0,
          1.0,
          0.0
        ],
        "axis_other_aligned": [
          -2.807754441850096e-17,
          1.0,
          -8.673617379884039e-17
        ],
        "angle_rad": 9.116749610379536e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "objRx",
        "joint_other": "objRx",
        "axis_m": [
          1.0,
          0.0,
          0.0
        ],
        "axis_other_aligned": [
          1.0,
          1.0455477107111145e-16,
          -3.885780586188048e-16
        ],
        "angle_rad": 4.023985683295752e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "objRy",
        "joint_other": "objRy",
        "axis_m": [
          0.0,
          0.0,
          -1.0
        ],
        "axis_other_aligned": [
          -2.333176622906949e-16,
          -1.3981393759945268e-16,
          -1.0
        ],
        "angle_rad": 2.7200196448529264e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "objRz",
        "joint_other": "objRz",
        "axis_m": [
          0.0,
          1.0,
          0.0
        ],
        "axis_other_aligned": [
          -2.807754441850096e-17,
          1.0,
          -8.673617379884039e-17
        ],
        "angle_rad": 9.116749610379536e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      }
    ],
    "axis_disagreements": [],
    "com_eligible": true,
    "covariance_singular_values": [
      16.51900072783451,
      2.8207767054565784,
      0.7394443144982121
    ],
    "origin_residuals_m": {
      "pelvis": 2.9079264368403834e-17,
      "femur_r": 7.757919228897728e-17,
      "tibia_r": 2.800598096570984e-16,
      "talus_r": 3.4021815010030383e-16,
      "calcn_r": 4.528924144620228e-16,
      "toes_r": 4.443059973708341e-16,
      "patella_r": 2.2633986948989007e-16,
      "femur_l": 9.539401966176753e-17,
      "tibia_l": 2.9901721968504993e-16,
      "talus_l": 3.66646846595234e-16,
      "calcn_l": 4.801393697075383e-16,
      "toes_l": 4.579669976578771e-16,
      "patella_l": 2.5514002453611344e-16,
      "sacrum": 4.022649815853993e-17,
      "Abdomen": 4.174689099396789e-17,
      "lumbar5": 2.743352958152082e-17,
      "lumbar4": 1.964707976458835e-17,
      "lumbar3": 3.2594336629461464e-17,
      "lumbar2": 5.624507694030135e-17,
      "lumbar1": 5.806368685448389e-17,
      "thoracic12": 8.415240460911181e-17,
      "thoracic11": 5.888750210979312e-17,
      "thoracic10": 1.6717371819461942e-16,
      "thoracic9": 1.127961985039598e-16,
      "thoracic8": 1.1181903331232706e-16,
      "thoracic7": 1.124782769297866e-16,
      "thoracic6": 1.6675421813609516e-16,
      "thoracic5": 1.6717545080187868e-16,
      "thoracic4": 2.220448819930661e-16,
      "thoracic3": 2.2255559890579477e-16,
      "thoracic2": 2.2233687649740926e-16,
      "thoracic1": 2.231077425696022e-16,
      "sternum": 2.269632985128089e-16,
      "clavicle_r": 2.3290721952371135e-16,
      "clavphant_r": 2.626717347901611e-16,
      "scapula_r": 2.626717347901611e-16,
      "scapphant_r": 2.651347637902923e-16,
      "humphant_r": 2.651347637902923e-16,
      "humphant1_r": 2.651347637902923e-16,
      "humerus_r": 2.651347637902923e-16,
      "ulna_r": 1.1775693440128312e-16,
      "radius_r": 1.195827321860277e-16,
      "proximal_row": 1.7444108782428046e-16,
      "capitate": 1.7444108782428046e-16,
      "trapezium": 1.8177385842962546e-16,
      "firstmc1": 1.8177385842962546e-16,
      "firstmc": 1.798766884999431e-16,
      "proximal_thumb": 1.6079679568759646e-16,
      "distal_thumb": 1.7826341206873999e-16,
      "trapezoid": 1.8177385842962546e-16,
      "hamate": 1.7490362921768729e-16,
      "secondmc": 1.8253379971363983e-16,
      "2proxph": 2.0062885096040707e-16,
      "2midph": 2.2073972817097756e-16,
      "2distph": 2.2073972817097756e-16,
      "thirdmc": 1.8293726260460532e-16,
      "3proxph": 2.0062885096040707e-16,
      "3midph": 2.2215299868541707e-16,
      "3distph": 2.2215299868541707e-16,
      "fourthmc": 1.8304055820388216e-16,
      "4proxph": 2.0187413561148406e-16,
      "4midph": 2.024992467494254e-16,
      "4distph": 2.22798831039709e-16,
      "fifthmc": 1.6312166687570793e-16,
      "5proxph": 1.8424037361508207e-16,
      "5midph": 1.8619006149354548e-16,
      "5distph": 1.8619006149354548e-16,
      "clavicle_l": 2.246332941915114e-16,
      "clavphant_l": 2.420669712248692e-16,
      "scapula_l": 2.420669712248692e-16,
      "scapphant_l": 2.5172027167143304e-16,
      "humphant_l": 2.5172027167143304e-16,
      "humphant1_l": 2.5172027167143304e-16,
      "humerus_l": 2.5172027167143304e-16,
      "ulna_l": 1.4488835837920476e-16,
      "radius_l": 1.4703252574089423e-16,
      "proximal_row_l": 1.539512110316623e-16,
      "capitate_l": 1.539512110316623e-16,
      "trapezium_l": 1.582691578899265e-16,
      "firstmc1_l": 1.582691578899265e-16,
      "firstmc_l": 1.3597399555105182e-16,
      "proximal_thumb_l": 1.3329179921125024e-16,
      "distal_thumb_l": 1.5515838457795457e-16,
      "trapezoid_l": 1.582691578899265e-16,
      "hamate_l": 1.5367823853893093e-16,
      "secondmc_l": 1.594436429147036e-16,
      "2proxph_l": 1.7109685898544713e-16,
      "2midph_l": 1.8619006149354548e-16,
      "2distph_l": 1.8619006149354548e-16,
      "thirdmc_l": 1.5884801395362454e-16,
      "3proxph_l": 1.7109685898544713e-16,
      "3midph_l": 2.0770370905276122e-16,
      "3distph_l": 2.0770370905276122e-16,
      "fourthmc_l": 1.5812708634263468e-16,
      "4proxph_l": 1.9332635098005857e-16,
      "4midph_l": 1.9338483522389913e-16,
      "4distph_l": 2.0684447151138411e-16,
      "fifthmc_l": 1.5743272623002425e-16,
      "5proxph_l": 1.9242142079520307e-16,
      "5midph_l": 1.9242142079520307e-16,
      "5distph_l": 1.9242142079520307e-16,
      "head_neck": 2.229623545695847e-16,
      "rib1_R": 2.2516683988987807e-16,
      "rib1_L": 2.225860458774576e-16,
      "rib2_R": 2.237994986951949e-16,
      "rib2_L": 2.226468755882386e-16,
      "rib3_R": 2.232946947441042e-16,
      "rib3_L": 2.224846260672635e-16,
      "rib4_R": 2.2291027918243403e-16,
      "rib4_L": 2.225387223846558e-16,
      "rib5_R": 2.227212004505268e-16,
      "rib5_L": 2.227212004505268e-16,
      "rib6_R": 1.6883057536160649e-16,
      "rib6_L": 1.7010907505015192e-16,
      "rib7_R": 1.688662199466889e-16,
      "rib7_L": 1.705684004216481e-16,
      "rib8_R": 1.1455743979190591e-16,
      "rib8_L": 1.1736016516649439e-16,
      "rib9_R": 1.147673963296451e-16,
      "rib9_L": 1.1775693440128312e-16,
      "rib10_R": 1.6915110622252185e-16,
      "rib10_L": 1.7169381238494628e-16,
      "rib11_R": 6.293006791785826e-17,
      "rib11_L": 6.947562107041945e-17,
      "rib12_R": 8.505453752507596e-17,
      "rib12_L": 9.26413801423296e-17,
      "waterbottle": 2.944387421548177e-16,
      "target": 2.944387421548177e-16,
      "table": 2.0905569983530426e-16
    },
    "reason": "Unique proper rigid fit and matched signed axes meet the configured thresholds"
  },
  "M/S": {
    "status": "consistent",
    "matched_body_origins": 129,
    "position_threshold_m": 0.005,
    "axis_threshold_rad": 0.005,
    "residual_definition": "maximum Euclidean residual over matched body origins; Kabsch minimizes RMS, which is also recorded",
    "coordinate_frames": "each snapshot registered to its matched report anchor",
    "anchor_m": "pelvis",
    "anchor_other": "pelvis",
    "rotation_other_to_m": [
      [
        0.9999999999999999,
        -2.807754441850095e-17,
        2.3331766229069473e-16
      ],
      [
        1.0455477107111144e-16,
        0.9999999999999996,
        1.3981393759945259e-16
      ],
      [
        -3.885780586188048e-16,
        -8.673617379884035e-17,
        0.9999999999999993
      ]
    ],
    "translation_other_to_m": [
      -6.938893903907228e-18,
      2.7755575615628914e-17,
      -5.204170427930421e-18
    ],
    "rms_residual_m": 2.0529612592073526e-16,
    "max_residual_m": 4.801393697075383e-16,
    "fit_rank": 3,
    "axis_checks": [
      {
        "joint_m": "sternoclavicular_r2_r",
        "joint_other": "sternoclavicular_r2_r",
        "axis_m": [
          -0.023328076082097478,
          0.9904072301057558,
          -0.1361958862100926
        ],
        "axis_other_aligned": [
          -0.023328076082097544,
          0.9904072301057558,
          -0.13619588621009265
        ],
        "angle_rad": 8.653210372566878e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "sternoclavicular_r3_r",
        "joint_other": "sternoclavicular_r3_r",
        "axis_m": [
          -0.9306888527188436,
          -0.07124305061133122,
          -0.3588073120276037
        ],
        "axis_other_aligned": [
          -0.9306888527188437,
          -0.07124305061133136,
          -0.3588073120276032
        ],
        "angle_rad": 5.2222956368572725e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "unrotscap_r3_r",
        "joint_other": "unrotscap_r3_r",
        "axis_m": [
          -0.9306888527188436,
          -0.07124305061133122,
          -0.3588073120276037
        ],
        "axis_other_aligned": [
          -0.9306888527188437,
          -0.07124305061133136,
          -0.3588073120276032
        ],
        "angle_rad": 5.2222956368572725e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "unrotscap_r2_r",
        "joint_other": "unrotscap_r2_r",
        "axis_m": [
          -0.023328076082097478,
          0.9904072301057558,
          -0.1361958862100926
        ],
        "axis_other_aligned": [
          -0.023328076082097544,
          0.9904072301057558,
          -0.13619588621009265
        ],
        "angle_rad": 8.653210372566878e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "acromioclavicular_r2_r",
        "joint_other": "acromioclavicular_r2_r",
        "axis_m": [
          0.05946790230964638,
          0.9545920900456824,
          -0.29192038335324644
        ],
        "axis_other_aligned": [
          0.0594679023096463,
          0.9545920900456822,
          -0.29192038335324644
        ],
        "angle_rad": 7.351626287044711e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "acromioclavicular_r3_r",
        "joint_other": "acromioclavicular_r3_r",
        "axis_m": [
          -0.7208547250965776,
          0.24328413468601107,
          0.6489848188640598
        ],
        "axis_other_aligned": [
          -0.7208547250965776,
          0.243284134686011,
          0.6489848188640598
        ],
        "angle_rad": 6.206335383118183e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "acromioclavicular_r1_r",
        "joint_other": "acromioclavicular_r1_r",
        "axis_m": [
          0.6905116116648125,
          0.17180473339016292,
          0.7026214113879525
        ],
        "axis_other_aligned": [
          0.6905116116648129,
          0.17180473339016314,
          0.7026214113879521
        ],
        "angle_rad": 6.550551057807855e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "unrothum_r1_r",
        "joint_other": "unrothum_r1_r",
        "axis_m": [
          0.6905116116648125,
          0.17180473339016292,
          0.7026214113879525
        ],
        "axis_other_aligned": [
          0.6905116116648129,
          0.17180473339016314,
          0.7026214113879521
        ],
        "angle_rad": 6.550551057807855e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "unrothum_r3_r",
        "joint_other": "unrothum_r3_r",
        "axis_m": [
          -0.7208547250965776,
          0.24328413468601107,
          0.6489848188640598
        ],
        "axis_other_aligned": [
          -0.7208547250965776,
          0.243284134686011,
          0.6489848188640598
        ],
        "angle_rad": 6.206335383118183e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "unrothum_r2_r",
        "joint_other": "unrothum_r2_r",
        "axis_m": [
          0.05946790230964638,
          0.9545920900456824,
          -0.29192038335324644
        ],
        "axis_other_aligned": [
          0.0594679023096463,
          0.9545920900456822,
          -0.29192038335324644
        ],
        "angle_rad": 7.351626287044711e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "elv_angle_r",
        "joint_other": "elv_angle_r",
        "axis_m": [
          -0.06780332743512969,
          0.9968218361558799,
          0.04182027919018272
        ],
        "axis_other_aligned": [
          -0.06780332743512972,
          0.9968218361558799,
          0.04182027919018265
        ],
        "angle_rad": 7.498039971595757e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "shoulder_elv_r",
        "joint_other": "shoulder_elv_r",
        "axis_m": [
          -0.9866183831797913,
          -0.07321765555013006,
          0.14568232867248154
        ],
        "axis_other_aligned": [
          -0.9866183831797913,
          -0.0732176555501301,
          0.14568232867248185
        ],
        "angle_rad": 3.085321648821679e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "shoulder1_r2_r",
        "joint_other": "shoulder1_r2_r",
        "axis_m": [
          -0.06780332743512969,
          0.9968218361558799,
          0.04182027919018272
        ],
        "axis_other_aligned": [
          -0.06780332743512972,
          0.9968218361558799,
          0.04182027919018265
        ],
        "angle_rad": 7.498039971595757e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "shoulder_rot_r",
        "joint_other": "shoulder_rot_r",
        "axis_m": [
          -0.06780332743512969,
          0.9968218361558799,
          0.04182027919018272
        ],
        "axis_other_aligned": [
          -0.06780332743512972,
          0.9968218361558799,
          0.04182027919018265
        ],
        "angle_rad": 7.498039971595757e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "elbow_flexion_r",
        "joint_other": "elbow_flexion_r",
        "axis_m": [
          0.13301628840283014,
          0.04688931329049195,
          0.9900040703546028
        ],
        "axis_other_aligned": [
          0.13301628840283042,
          0.04688931329049212,
          0.9900040703546027
        ],
        "angle_rad": 3.2742187586505674e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "pro_sup_r",
        "joint_other": "pro_sup_r",
        "axis_m": [
          -0.10321128619189612,
          0.9876690682082944,
          -0.11771678770325915
        ],
        "axis_other_aligned": [
          -0.10321128619189622,
          0.9876690682082944,
          -0.11771678770325918
        ],
        "angle_rad": 1.0140345331252273e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "deviation_r",
        "joint_other": "deviation_r",
        "axis_m": [
          -0.8516612801697739,
          -0.2012013308257751,
          -0.4839329378473001
        ],
        "axis_other_aligned": [
          -0.8516612801697743,
          -0.2012013308257752,
          -0.4839329378472996
        ],
        "angle_rad": 6.300271117485416e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "flexion_r",
        "joint_other": "flexion_r",
        "axis_m": [
          0.9820415468042459,
          -0.17777074489107225,
          0.06318198011456644
        ],
        "axis_other_aligned": [
          0.9820415468042459,
          -0.17777074489107209,
          0.06318198011456605
        ],
        "angle_rad": 4.2030814102805256e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "wrist_hand_r1_r",
        "joint_other": "wrist_hand_r1_r",
        "axis_m": [
          0.8967960779322267,
          -0.28142546250060774,
          -0.34140372531900504
        ],
        "axis_other_aligned": [
          0.8967960779322267,
          -0.2814254625006075,
          -0.3414037253190052
        ],
        "angle_rad": 2.3592239273284576e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "wrist_hand_r3_r",
        "joint_other": "wrist_hand_r3_r",
        "axis_m": [
          0.9830828652717561,
          0.08598504433218035,
          -0.16172399995135953
        ],
        "axis_other_aligned": [
          0.983082865271756,
          0.08598504433218038,
          -0.16172399995135983
        ],
        "angle_rad": 3.363037852658521e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "cmc_flexion",
        "joint_other": "cmc_flexion",
        "axis_m": [
          -0.07344194500752081,
          0.6616103078649415,
          -0.7462426423358356
        ],
        "axis_other_aligned": [
          -0.07344194500752103,
          0.6616103078649415,
          -0.7462426423358355
        ],
        "angle_rad": 2.332541980949955e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "cmc_abduction",
        "joint_other": "cmc_abduction",
        "axis_m": [
          0.4770492845499966,
          0.770394287765569,
          0.4229853679366677
        ],
        "axis_other_aligned": [
          0.47704928454999684,
          0.7703942877655691,
          0.42298536793666724
        ],
        "angle_rad": 5.064917260848195e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "mp_flexion",
        "joint_other": "mp_flexion",
        "axis_m": [
          -0.016573578819913302,
          0.20281462182568985,
          -0.9790768844471831
        ],
        "axis_other_aligned": [
          -0.016573578819913545,
          0.20281462182568977,
          -0.9790768844471831
        ],
        "angle_rad": 2.552789414337386e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "ip_flexion",
        "joint_other": "ip_flexion",
        "axis_m": [
          -0.06297487662564752,
          0.47620558120992046,
          -0.8770760567581961
        ],
        "axis_other_aligned": [
          -0.06297487662564777,
          0.4762055812099204,
          -0.8770760567581961
        ],
        "angle_rad": 2.5909591973639336e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "2mcp_abduction",
        "joint_other": "2mcp_abduction",
        "axis_m": [
          0.2817848689300059,
          0.21363852970067548,
          0.9353907559247274
        ],
        "axis_other_aligned": [
          0.2817848689300062,
          0.21363852970067565,
          0.9353907559247273
        ],
        "angle_rad": 3.390840864445248e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "2mcp_flexion",
        "joint_other": "2mcp_flexion",
        "axis_m": [
          0.9541970315101842,
          0.09917720047301809,
          -0.282262126335588
        ],
        "axis_other_aligned": [
          0.9541970315101842,
          0.09917720047301812,
          -0.2822621263355883
        ],
        "angle_rad": 2.7971575570698805e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "2pm_flexion",
        "joint_other": "2pm_flexion",
        "axis_m": [
          0.9448448639590873,
          0.19940637248118728,
          -0.2598177855036641
        ],
        "axis_other_aligned": [
          0.9448448639590872,
          0.1994063724811873,
          -0.25981778550366436
        ],
        "angle_rad": 3.140951470513929e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "2md_flexion",
        "joint_other": "2md_flexion",
        "axis_m": [
          0.974946329860523,
          0.22215123934181055,
          -0.011334934953230985
        ],
        "axis_other_aligned": [
          0.974946329860523,
          0.2221512393418106,
          -0.011334934953231377
        ],
        "angle_rad": 3.95193699647667e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "3mcp_abduction",
        "joint_other": "3mcp_abduction",
        "axis_m": [
          0.055839491188762275,
          0.12351926194185028,
          0.9907698739632331
        ],
        "axis_other_aligned": [
          0.05583949118876254,
          0.12351926194185044,
          0.990769873963233
        ],
        "angle_rad": 3.1867960929430274e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "3mcp_flexion",
        "joint_other": "3mcp_flexion",
        "axis_m": [
          0.9875997535185798,
          0.12309764181608948,
          -0.09743560657869581
        ],
        "axis_other_aligned": [
          0.9875997535185796,
          0.12309764181608951,
          -0.09743560657869613
        ],
        "angle_rad": 3.376299569779874e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "3pm_flexion",
        "joint_other": "3pm_flexion",
        "axis_m": [
          0.9997803109886432,
          0.014348495363896735,
          0.015279085059134938
        ],
        "axis_other_aligned": [
          0.9997803109886432,
          0.014348495363896836,
          0.015279085059134539
        ],
        "angle_rad": 4.1154063119141427e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "3md_flexion",
        "joint_other": "3md_flexion",
        "axis_m": [
          0.9936239160105462,
          0.11226928600353216,
          0.010349925223116722
        ],
        "axis_other_aligned": [
          0.9936239160105462,
          0.11226928600353223,
          0.010349925223116322
        ],
        "angle_rad": 4.0755163990155153e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "4cmc_flexion",
        "joint_other": "4cmc_flexion",
        "axis_m": [
          0.6241124359432589,
          -0.7551510418175946,
          -0.20057560006833555
        ],
        "axis_other_aligned": [
          0.624112435943259,
          -0.7551510418175945,
          -0.20057560006833564
        ],
        "angle_rad": 1.8824747269678055e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "4mcp_abduction",
        "joint_other": "4mcp_abduction",
        "axis_m": [
          0.053009413439229866,
          0.1488461099164688,
          0.9874385234785826
        ],
        "axis_other_aligned": [
          0.053009413439230116,
          0.14884610991646896,
          0.9874385234785826
        ],
        "angle_rad": 3.0150272531948617e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "4mcp_flexion",
        "joint_other": "4mcp_flexion",
        "axis_m": [
          0.993122669544568,
          0.010400643412515528,
          -0.11661556436975554
        ],
        "axis_other_aligned": [
          0.993122669544568,
          0.010400643412515615,
          -0.11661556436975587
        ],
        "angle_rad": 3.4424107053751306e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "4pm_flexion",
        "joint_other": "4pm_flexion",
        "axis_m": [
          0.9991116393820398,
          0.04182302782492728,
          0.005173624927265578
        ],
        "axis_other_aligned": [
          0.99911163938204,
          0.04182302782492738,
          0.005173624927265184
        ],
        "angle_rad": 4.0594488325762537e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "4md_flexion",
        "joint_other": "4md_flexion",
        "axis_m": [
          0.9803649425936615,
          -0.06536383413705772,
          0.18604340493613353
        ],
        "axis_other_aligned": [
          0.9803649425936616,
          -0.06536383413705758,
          0.18604340493613308
        ],
        "angle_rad": 4.652811653304674e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "CMC5_r1",
        "joint_other": "CMC5_r1",
        "axis_m": [
          0.4643723212269116,
          -0.8334242229387436,
          0.29960375814946233
        ],
        "axis_other_aligned": [
          0.46437232122691174,
          -0.8334242229387435,
          0.29960375814946216
        ],
        "angle_rad": 2.3221980631040627e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "5mcp_abduction",
        "joint_other": "5mcp_abduction",
        "axis_m": [
          0.04348720476586676,
          0.22016733676098177,
          0.9744922815729369
        ],
        "axis_other_aligned": [
          0.04348720476586701,
          0.22016733676098196,
          0.9744922815729369
        ],
        "angle_rad": 2.981757037776785e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "5mcp_flexion",
        "joint_other": "5mcp_flexion",
        "axis_m": [
          0.9830116880470507,
          -0.13923433516784692,
          -0.11959022147841102
        ],
        "axis_other_aligned": [
          0.9830116880470507,
          -0.13923433516784678,
          -0.11959022147841132
        ],
        "angle_rad": 3.4051875089965907e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "5pm_flexion",
        "joint_other": "5pm_flexion",
        "axis_m": [
          0.9623157051720419,
          -0.2548300600528955,
          0.09492167335584373
        ],
        "axis_other_aligned": [
          0.962315705172042,
          -0.2548300600528953,
          0.09492167335584334
        ],
        "angle_rad": 4.3021142204224816e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "5md_flexion",
        "joint_other": "5md_flexion",
        "axis_m": [
          0.9318759880761684,
          -0.3566806166079947,
          0.06622749114382655
        ],
        "axis_other_aligned": [
          0.9318759880761684,
          -0.3566806166079945,
          0.06622749114382619
        ],
        "angle_rad": 4.1540741810552243e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "objTx",
        "joint_other": "objTx",
        "axis_m": [
          1.0,
          0.0,
          0.0
        ],
        "axis_other_aligned": [
          1.0,
          1.0455477107111145e-16,
          -3.885780586188048e-16
        ],
        "angle_rad": 4.023985683295752e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "objTy",
        "joint_other": "objTy",
        "axis_m": [
          0.0,
          0.0,
          -1.0
        ],
        "axis_other_aligned": [
          -2.333176622906949e-16,
          -1.3981393759945268e-16,
          -1.0
        ],
        "angle_rad": 2.7200196448529264e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "objTz",
        "joint_other": "objTz",
        "axis_m": [
          0.0,
          1.0,
          0.0
        ],
        "axis_other_aligned": [
          -2.807754441850096e-17,
          1.0,
          -8.673617379884039e-17
        ],
        "angle_rad": 9.116749610379536e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "objRx",
        "joint_other": "objRx",
        "axis_m": [
          1.0,
          0.0,
          0.0
        ],
        "axis_other_aligned": [
          1.0,
          1.0455477107111145e-16,
          -3.885780586188048e-16
        ],
        "angle_rad": 4.023985683295752e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "objRy",
        "joint_other": "objRy",
        "axis_m": [
          0.0,
          0.0,
          -1.0
        ],
        "axis_other_aligned": [
          -2.333176622906949e-16,
          -1.3981393759945268e-16,
          -1.0
        ],
        "angle_rad": 2.7200196448529264e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "objRz",
        "joint_other": "objRz",
        "axis_m": [
          0.0,
          1.0,
          0.0
        ],
        "axis_other_aligned": [
          -2.807754441850096e-17,
          1.0,
          -8.673617379884039e-17
        ],
        "angle_rad": 9.116749610379536e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      }
    ],
    "axis_disagreements": [],
    "com_eligible": true,
    "covariance_singular_values": [
      16.51900072783451,
      2.8207767054565784,
      0.7394443144982121
    ],
    "origin_residuals_m": {
      "pelvis": 2.9079264368403834e-17,
      "femur_r": 7.757919228897728e-17,
      "tibia_r": 2.800598096570984e-16,
      "talus_r": 3.4021815010030383e-16,
      "calcn_r": 4.528924144620228e-16,
      "toes_r": 4.443059973708341e-16,
      "patella_r": 2.2633986948989007e-16,
      "femur_l": 9.539401966176753e-17,
      "tibia_l": 2.9901721968504993e-16,
      "talus_l": 3.66646846595234e-16,
      "calcn_l": 4.801393697075383e-16,
      "toes_l": 4.579669976578771e-16,
      "patella_l": 2.5514002453611344e-16,
      "sacrum": 4.022649815853993e-17,
      "Abdomen": 4.174689099396789e-17,
      "lumbar5": 2.743352958152082e-17,
      "lumbar4": 1.964707976458835e-17,
      "lumbar3": 3.2594336629461464e-17,
      "lumbar2": 5.624507694030135e-17,
      "lumbar1": 5.806368685448389e-17,
      "thoracic12": 8.415240460911181e-17,
      "thoracic11": 5.888750210979312e-17,
      "thoracic10": 1.6717371819461942e-16,
      "thoracic9": 1.127961985039598e-16,
      "thoracic8": 1.1181903331232706e-16,
      "thoracic7": 1.124782769297866e-16,
      "thoracic6": 1.6675421813609516e-16,
      "thoracic5": 1.6717545080187868e-16,
      "thoracic4": 2.220448819930661e-16,
      "thoracic3": 2.2255559890579477e-16,
      "thoracic2": 2.2233687649740926e-16,
      "thoracic1": 2.231077425696022e-16,
      "sternum": 2.269632985128089e-16,
      "clavicle_r": 2.3290721952371135e-16,
      "clavphant_r": 2.626717347901611e-16,
      "scapula_r": 2.626717347901611e-16,
      "scapphant_r": 2.651347637902923e-16,
      "humphant_r": 2.651347637902923e-16,
      "humphant1_r": 2.651347637902923e-16,
      "humerus_r": 2.651347637902923e-16,
      "ulna_r": 1.1775693440128312e-16,
      "radius_r": 1.195827321860277e-16,
      "proximal_row": 1.7444108782428046e-16,
      "capitate": 1.7444108782428046e-16,
      "trapezium": 1.8177385842962546e-16,
      "firstmc1": 1.8177385842962546e-16,
      "firstmc": 1.798766884999431e-16,
      "proximal_thumb": 1.6079679568759646e-16,
      "distal_thumb": 1.7826341206873999e-16,
      "trapezoid": 1.8177385842962546e-16,
      "hamate": 1.7490362921768729e-16,
      "secondmc": 1.8253379971363983e-16,
      "2proxph": 2.0062885096040707e-16,
      "2midph": 2.2073972817097756e-16,
      "2distph": 2.2073972817097756e-16,
      "thirdmc": 1.8293726260460532e-16,
      "3proxph": 2.0062885096040707e-16,
      "3midph": 2.2215299868541707e-16,
      "3distph": 2.2215299868541707e-16,
      "fourthmc": 1.8304055820388216e-16,
      "4proxph": 2.0187413561148406e-16,
      "4midph": 2.024992467494254e-16,
      "4distph": 2.22798831039709e-16,
      "fifthmc": 1.6312166687570793e-16,
      "5proxph": 1.8424037361508207e-16,
      "5midph": 1.8619006149354548e-16,
      "5distph": 1.8619006149354548e-16,
      "clavicle_l": 2.246332941915114e-16,
      "clavphant_l": 2.420669712248692e-16,
      "scapula_l": 2.420669712248692e-16,
      "scapphant_l": 2.5172027167143304e-16,
      "humphant_l": 2.5172027167143304e-16,
      "humphant1_l": 2.5172027167143304e-16,
      "humerus_l": 2.5172027167143304e-16,
      "ulna_l": 1.4488835837920476e-16,
      "radius_l": 1.4703252574089423e-16,
      "proximal_row_l": 1.539512110316623e-16,
      "capitate_l": 1.539512110316623e-16,
      "trapezium_l": 1.582691578899265e-16,
      "firstmc1_l": 1.582691578899265e-16,
      "firstmc_l": 1.3597399555105182e-16,
      "proximal_thumb_l": 1.3329179921125024e-16,
      "distal_thumb_l": 1.5515838457795457e-16,
      "trapezoid_l": 1.582691578899265e-16,
      "hamate_l": 1.5367823853893093e-16,
      "secondmc_l": 1.594436429147036e-16,
      "2proxph_l": 1.7109685898544713e-16,
      "2midph_l": 1.8619006149354548e-16,
      "2distph_l": 1.8619006149354548e-16,
      "thirdmc_l": 1.5884801395362454e-16,
      "3proxph_l": 1.7109685898544713e-16,
      "3midph_l": 2.0770370905276122e-16,
      "3distph_l": 2.0770370905276122e-16,
      "fourthmc_l": 1.5812708634263468e-16,
      "4proxph_l": 1.9332635098005857e-16,
      "4midph_l": 1.9338483522389913e-16,
      "4distph_l": 2.0684447151138411e-16,
      "fifthmc_l": 1.5743272623002425e-16,
      "5proxph_l": 1.9242142079520307e-16,
      "5midph_l": 1.9242142079520307e-16,
      "5distph_l": 1.9242142079520307e-16,
      "head_neck": 2.229623545695847e-16,
      "rib1_R": 2.2516683988987807e-16,
      "rib1_L": 2.225860458774576e-16,
      "rib2_R": 2.237994986951949e-16,
      "rib2_L": 2.226468755882386e-16,
      "rib3_R": 2.232946947441042e-16,
      "rib3_L": 2.224846260672635e-16,
      "rib4_R": 2.2291027918243403e-16,
      "rib4_L": 2.225387223846558e-16,
      "rib5_R": 2.227212004505268e-16,
      "rib5_L": 2.227212004505268e-16,
      "rib6_R": 1.6883057536160649e-16,
      "rib6_L": 1.7010907505015192e-16,
      "rib7_R": 1.688662199466889e-16,
      "rib7_L": 1.705684004216481e-16,
      "rib8_R": 1.1455743979190591e-16,
      "rib8_L": 1.1736016516649439e-16,
      "rib9_R": 1.147673963296451e-16,
      "rib9_L": 1.1775693440128312e-16,
      "rib10_R": 1.6915110622252185e-16,
      "rib10_L": 1.7169381238494628e-16,
      "rib11_R": 6.293006791785826e-17,
      "rib11_L": 6.947562107041945e-17,
      "rib12_R": 8.505453752507596e-17,
      "rib12_L": 9.26413801423296e-17,
      "waterbottle": 2.944387421548177e-16,
      "target": 2.944387421548177e-16,
      "table": 2.0905569983530426e-16
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
| robot / total_com_registered | [0.174434826, -0.0707324291, 0.00240647996] | [0.174434826, -0.0707324291, 0.00240647996] | [0.174434826, -0.0707324291, 0.00240647996] | [0, 0, 0] | eligible; compared after Kabsch alignment | [aggregate inputs](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/MS-Human-700-Manipulation.xml#L1) | [aggregate inputs](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/MS-Human-700-Manipulation.xml#L1) | [aggregate inputs](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/MS-Human-700-Manipulation.xml#L1) |
| pelvis / com_registered | [-0.0707, 0, 0] | [-0.0707, 0, 0] | [-0.0707, 0, 0] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L54](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/MS-Human-700-Manipulation.xml#L54) | [CoM/kinematic input L63](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/MS-Human-700-Manipulation.xml#L63) | [CoM/kinematic input L63](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/MS-Human-700-Manipulation.xml#L63) |
| femur_r / com_registered | [-0.056276, -0.24849, 0.07726] | [-0.056276, -0.24849, 0.07726] | [-0.056276, -0.24849, 0.07726] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L3](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Leg_Foot_Vis_r.xml#L3) | [CoM/kinematic input L3](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Leg_Foot_Vis_r.xml#L3) | [CoM/kinematic input L3](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Leg_Foot_Vis_r.xml#L3) |
| tibia_r / com_registered | [-0.05627646, -0.669615, 0.07599474] | [-0.05627646, -0.669615, 0.07599474] | [-0.05627646, -0.669615, 0.07599474] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L73](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Leg_Foot_Vis_r.xml#L73) | [CoM/kinematic input L64](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Leg_Foot_Vis_r.xml#L64) | [CoM/kinematic input L64](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Leg_Foot_Vis_r.xml#L64) |
| talus_r / com_registered | [-0.06033917, -0.882571488, 0.07431075] | [-0.06033917, -0.882571488, 0.07431075] | [-0.06033917, -0.882571488, 0.07431075] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L132](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Leg_Foot_Vis_r.xml#L132) | [CoM/kinematic input L117](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Leg_Foot_Vis_r.xml#L117) | [CoM/kinematic input L117](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Leg_Foot_Vis_r.xml#L117) |
| calcn_r / com_registered | [-0.04306506, -0.9099598, 0.07939655] | [-0.04306506, -0.9099598, 0.07939655] | [-0.04306506, -0.9099598, 0.07939655] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L136](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Leg_Foot_Vis_r.xml#L136) | [CoM/kinematic input L120](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Leg_Foot_Vis_r.xml#L120) | [CoM/kinematic input L120](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Leg_Foot_Vis_r.xml#L120) |
| toes_r / com_registered | [0.08541184, -0.92814138, 0.09415728] | [0.08541184, -0.92814138, 0.09415728] | [0.08541184, -0.92814138, 0.09415728] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L163](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Leg_Foot_Vis_r.xml#L163) | [CoM/kinematic input L146](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Leg_Foot_Vis_r.xml#L146) | [CoM/kinematic input L146](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Leg_Foot_Vis_r.xml#L146) |
| patella_r / com_registered | [-0.06189133, -0.4584833, 0.077999699] | [-0.06189133, -0.4584833, 0.077999699] | [-0.06189133, -0.4584833, 0.077999699] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L180](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Leg_Foot_Vis_r.xml#L180) | [CoM/kinematic input L162](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Leg_Foot_Vis_r.xml#L162) | [CoM/kinematic input L162](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Leg_Foot_Vis_r.xml#L162) |
| femur_l / com_registered | [-0.056276, -0.24849, -0.07726] | [-0.056276, -0.24849, -0.07726] | [-0.056276, -0.24849, -0.07726] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L3](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Leg_Foot_Vis_l.xml#L3) | [CoM/kinematic input L3](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Leg_Foot_Vis_l.xml#L3) | [CoM/kinematic input L3](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Leg_Foot_Vis_l.xml#L3) |
| tibia_l / com_registered | [-0.05627646, -0.669615, -0.07599474] | [-0.05627646, -0.669615, -0.07599474] | [-0.05627646, -0.669615, -0.07599474] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L73](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Leg_Foot_Vis_l.xml#L73) | [CoM/kinematic input L64](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Leg_Foot_Vis_l.xml#L64) | [CoM/kinematic input L64](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Leg_Foot_Vis_l.xml#L64) |
| talus_l / com_registered | [-0.06033917, -0.882571488, -0.07431075] | [-0.06033917, -0.882571488, -0.07431075] | [-0.06033917, -0.882571488, -0.07431075] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L132](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Leg_Foot_Vis_l.xml#L132) | [CoM/kinematic input L117](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Leg_Foot_Vis_l.xml#L117) | [CoM/kinematic input L117](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Leg_Foot_Vis_l.xml#L117) |
| calcn_l / com_registered | [-0.04306506, -0.9099598, -0.07939655] | [-0.04306506, -0.9099598, -0.07939655] | [-0.04306506, -0.9099598, -0.07939655] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L136](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Leg_Foot_Vis_l.xml#L136) | [CoM/kinematic input L120](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Leg_Foot_Vis_l.xml#L120) | [CoM/kinematic input L120](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Leg_Foot_Vis_l.xml#L120) |
| toes_l / com_registered | [0.08541184, -0.92814138, -0.09415728] | [0.08541184, -0.92814138, -0.09415728] | [0.08541184, -0.92814138, -0.09415728] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L163](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Leg_Foot_Vis_l.xml#L163) | [CoM/kinematic input L146](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Leg_Foot_Vis_l.xml#L146) | [CoM/kinematic input L146](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Leg_Foot_Vis_l.xml#L146) |
| patella_l / com_registered | [-0.06189133, -0.4584833, -0.077999699] | [-0.06189133, -0.4584833, -0.077999699] | [-0.06189133, -0.4584833, -0.077999699] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L180](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Leg_Foot_Vis_l.xml#L180) | [CoM/kinematic input L162](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Leg_Foot_Vis_l.xml#L162) | [CoM/kinematic input L162](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Leg_Foot_Vis_l.xml#L162) |
| sacrum / com_registered | [-0.115, -0.02, 0] | [-0.115, -0.02, 0] | [-0.115, -0.02, 0] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L217](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Torso_Unimanual.xml#L217) | [CoM/kinematic input L207](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Torso_Unimanual.xml#L207) | [CoM/kinematic input L207](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Torso_Unimanual.xml#L207) |
| Abdomen / com_registered | [0.027, 0.141, 0] | [0.027, 0.141, 0] | [0.027, 0.141, 0] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L267](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Torso_Unimanual.xml#L267) | [CoM/kinematic input L256](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Torso_Unimanual.xml#L256) | [CoM/kinematic input L256](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Torso_Unimanual.xml#L256) |
| lumbar5 / com_registered | [-0.0612257918, 0.0694750117, 0] | [-0.0612257918, 0.0694750117, 0] | [-0.0612257918, 0.0694750117, 0] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L301](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Torso_Unimanual.xml#L301) | [CoM/kinematic input L289](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Torso_Unimanual.xml#L289) | [CoM/kinematic input L289](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Torso_Unimanual.xml#L289) |
| lumbar4 / com_registered | [-0.0505785516, 0.106324975, 0] | [-0.0505785516, 0.106324975, 0] | [-0.0505785516, 0.106324975, 0] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L339](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Torso_Unimanual.xml#L339) | [CoM/kinematic input L324](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Torso_Unimanual.xml#L324) | [CoM/kinematic input L324](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Torso_Unimanual.xml#L324) |
| lumbar3 / com_registered | [-0.0422170144, 0.142855012, 0] | [-0.0422170144, 0.142855012, 0] | [-0.0422170144, 0.142855012, 0] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L411](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Torso_Unimanual.xml#L411) | [CoM/kinematic input L393](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Torso_Unimanual.xml#L393) | [CoM/kinematic input L393](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Torso_Unimanual.xml#L393) |
| lumbar2 / com_registered | [-0.0414442701, 0.177380029, 0] | [-0.0414442701, 0.177380029, 0] | [-0.0414442701, 0.177380029, 0] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L485](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Torso_Unimanual.xml#L485) | [CoM/kinematic input L464](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Torso_Unimanual.xml#L464) | [CoM/kinematic input L464](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Torso_Unimanual.xml#L464) |
| lumbar1 / com_registered | [-0.0442738485, 0.210205039, 0] | [-0.0442738485, 0.210205039, 0] | [-0.0442738485, 0.210205039, 0] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L577](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Torso_Unimanual.xml#L577) | [CoM/kinematic input L553](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Torso_Unimanual.xml#L553) | [CoM/kinematic input L553](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Torso_Unimanual.xml#L553) |
| thoracic12 / com_registered | [-0.0455857284, 0.242560028, 0] | [-0.0455857284, 0.242560028, 0] | [-0.0455857284, 0.242560028, 0] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L615](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Torso_Unimanual.xml#L615) | [CoM/kinematic input L590](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Torso_Unimanual.xml#L590) | [CoM/kinematic input L590](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Torso_Unimanual.xml#L590) |
| thoracic11 / com_registered | [-0.052213715, 0.272660016, 0] | [-0.052213715, 0.272660016, 0] | [-0.052213715, 0.272660016, 0] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L647](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Torso_Unimanual.xml#L647) | [CoM/kinematic input L621](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Torso_Unimanual.xml#L621) | [CoM/kinematic input L621](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Torso_Unimanual.xml#L621) |
| thoracic10 / com_registered | [-0.0562568849, 0.301095, 0] | [-0.0562568849, 0.301095, 0] | [-0.0562568849, 0.301095, 0] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L675](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Torso_Unimanual.xml#L675) | [CoM/kinematic input L648](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Torso_Unimanual.xml#L648) | [CoM/kinematic input L648](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Torso_Unimanual.xml#L648) |
| thoracic9 / com_registered | [-0.0572871462, 0.327800009, 0] | [-0.0572871462, 0.327800009, 0] | [-0.0572871462, 0.327800009, 0] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L707](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Torso_Unimanual.xml#L707) | [CoM/kinematic input L679](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Torso_Unimanual.xml#L679) | [CoM/kinematic input L679](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Torso_Unimanual.xml#L679) |
| thoracic8 / com_registered | [-0.0640921231, 0.352569969, 0] | [-0.0640921231, 0.352569969, 0] | [-0.0640921231, 0.352569969, 0] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L735](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Torso_Unimanual.xml#L735) | [CoM/kinematic input L706](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Torso_Unimanual.xml#L706) | [CoM/kinematic input L706](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Torso_Unimanual.xml#L706) |
| thoracic7 / com_registered | [-0.0678394391, 0.377805001, 0] | [-0.0678394391, 0.377805001, 0] | [-0.0678394391, 0.377805001, 0] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L763](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Torso_Unimanual.xml#L763) | [CoM/kinematic input L733](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Torso_Unimanual.xml#L733) | [CoM/kinematic input L733](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Torso_Unimanual.xml#L733) |
| thoracic6 / com_registered | [-0.0684874975, 0.40338497, 0] | [-0.0684874975, 0.40338497, 0] | [-0.0684874975, 0.40338497, 0] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L791](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Torso_Unimanual.xml#L791) | [CoM/kinematic input L760](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Torso_Unimanual.xml#L760) | [CoM/kinematic input L760](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Torso_Unimanual.xml#L760) |
| thoracic5 / com_registered | [-0.0684888315, 0.428654995, 0] | [-0.0684888315, 0.428654995, 0] | [-0.0684888315, 0.428654995, 0] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L817](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Torso_Unimanual.xml#L817) | [CoM/kinematic input L785](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Torso_Unimanual.xml#L785) | [CoM/kinematic input L785](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Torso_Unimanual.xml#L785) |
| thoracic4 / com_registered | [-0.0671530674, 0.452625039, 0] | [-0.0671530674, 0.452625039, 0] | [-0.0671530674, 0.452625039, 0] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L843](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Torso_Unimanual.xml#L843) | [CoM/kinematic input L810](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Torso_Unimanual.xml#L810) | [CoM/kinematic input L810](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Torso_Unimanual.xml#L810) |
| thoracic3 / com_registered | [-0.0697574439, 0.473949984, 0] | [-0.0697574439, 0.473949984, 0] | [-0.0697574439, 0.473949984, 0] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L865](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Torso_Unimanual.xml#L865) | [CoM/kinematic input L831](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Torso_Unimanual.xml#L831) | [CoM/kinematic input L831](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Torso_Unimanual.xml#L831) |
| thoracic2 / com_registered | [-0.0657032787, 0.492795001, 0] | [-0.0657032787, 0.492795001, 0] | [-0.0657032787, 0.492795001, 0] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L887](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Torso_Unimanual.xml#L887) | [CoM/kinematic input L852](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Torso_Unimanual.xml#L852) | [CoM/kinematic input L852](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Torso_Unimanual.xml#L852) |
| thoracic1 / com_registered | [-0.0710702472, 0.51214498, 0] | [-0.0710702472, 0.51214498, 0] | [-0.0710702472, 0.51214498, 0] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L913](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Torso_Unimanual.xml#L913) | [CoM/kinematic input L877](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Torso_Unimanual.xml#L877) | [CoM/kinematic input L877](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Torso_Unimanual.xml#L877) |
| sternum / com_registered | [0.00964407042, 0.4214506, 0.000940853] | [0.00964407042, 0.4214506, 0.000940853] | [0.00964407042, 0.4214506, 0.000940853] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L948](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Torso_Unimanual.xml#L948) | [CoM/kinematic input L910](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Torso_Unimanual.xml#L910) | [CoM/kinematic input L910](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Torso_Unimanual.xml#L910) |
| clavicle_r / com_registered | [-0.0321772945, 0.471913458, 0.0804652163] | [-0.0321772945, 0.471913458, 0.0804652163] | [-0.0321772945, 0.471913458, 0.0804652163] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L4](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Arm_Hand_r.xml#L4) | [CoM/kinematic input L3](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Arm_Hand_r.xml#L3) | [CoM/kinematic input L3](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Arm_Hand_r.xml#L3) |
| clavphant_r / com_registered | [-0.0575524664, 0.48386516, 0.1607079] | [-0.0575524664, 0.48386516, 0.1607079] | [-0.0575524664, 0.48386516, 0.1607079] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L15](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Arm_Hand_r.xml#L15) | [CoM/kinematic input L14](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Arm_Hand_r.xml#L14) | [CoM/kinematic input L14](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Arm_Hand_r.xml#L14) |
| scapula_r / com_registered | [-0.113673827, 0.442000151, 0.117672097] | [-0.113673827, 0.442000151, 0.117672097] | [-0.113673827, 0.442000151, 0.117672097] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L20](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Arm_Hand_r.xml#L20) | [CoM/kinematic input L18](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Arm_Hand_r.xml#L18) | [CoM/kinematic input L18](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Arm_Hand_r.xml#L18) |
| scapphant_r / com_registered | [-0.063661154, 0.449298079, 0.170506027] | [-0.063661154, 0.449298079, 0.170506027] | [-0.063661154, 0.449298079, 0.170506027] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L94](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Arm_Hand_r.xml#L94) | [CoM/kinematic input L91](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Arm_Hand_r.xml#L91) | [CoM/kinematic input L91](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Arm_Hand_r.xml#L91) |
| humphant_r / com_registered | [-0.063661154, 0.449298079, 0.170506027] | [-0.063661154, 0.449298079, 0.170506027] | [-0.063661154, 0.449298079, 0.170506027] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L99](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Arm_Hand_r.xml#L99) | [CoM/kinematic input L96](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Arm_Hand_r.xml#L96) | [CoM/kinematic input L96](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Arm_Hand_r.xml#L96) |
| humphant1_r / com_registered | [-0.063661154, 0.449298079, 0.170506027] | [-0.063661154, 0.449298079, 0.170506027] | [-0.063661154, 0.449298079, 0.170506027] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L102](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Arm_Hand_r.xml#L102) | [CoM/kinematic input L99](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Arm_Hand_r.xml#L99) | [CoM/kinematic input L99](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Arm_Hand_r.xml#L99) |
| humerus_r / com_registered | [-0.0361297704, 0.310854578, 0.156234076] | [-0.0361297704, 0.310854578, 0.156234076] | [-0.0361297704, 0.310854578, 0.156234076] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L106](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Arm_Hand_r.xml#L106) | [CoM/kinematic input L103](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Arm_Hand_r.xml#L103) | [CoM/kinematic input L103](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Arm_Hand_r.xml#L103) |
| ulna_r / com_registered | [-0.0174194343, 0.0653566252, 0.18106773] | [-0.0174194343, 0.0653566252, 0.18106773] | [-0.0174194343, 0.0653566252, 0.18106773] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L253](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Arm_Hand_r.xml#L253) | [CoM/kinematic input L238](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Arm_Hand_r.xml#L238) | [CoM/kinematic input L238](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Arm_Hand_r.xml#L238) |
| radius_r / com_registered | [0.015128846, -0.0295470511, 0.190218271] | [0.015128846, -0.0295470511, 0.190218271] | [0.015128846, -0.0295470511, 0.190218271] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L284](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Arm_Hand_r.xml#L284) | [CoM/kinematic input L267](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Arm_Hand_r.xml#L267) | [CoM/kinematic input L267](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Arm_Hand_r.xml#L267) |
| proximal_row / com_registered | [0.00723592037, -0.0941615967, 0.200046402] | [0.00723592037, -0.0941615967, 0.200046402] | [0.00723592037, -0.0941615967, 0.200046402] | [0, 0, 0] | eligible; compared after Kabsch alignment | [geometry/inference input L350](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Arm_Hand_r.xml#L350) | [geometry/inference input L330](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Arm_Hand_r.xml#L330) | [geometry/inference input L330](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Arm_Hand_r.xml#L330) |
| capitate / com_registered | [0.0103491448, -0.10563313, 0.202916485] | [0.0103491448, -0.10563313, 0.202916485] | [0.0103491448, -0.10563313, 0.202916485] | [0, 0, 0] | eligible; compared after Kabsch alignment | [geometry/inference input L402](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Arm_Hand_r.xml#L402) | [geometry/inference input L375](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Arm_Hand_r.xml#L375) | [geometry/inference input L375](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Arm_Hand_r.xml#L375) |
| trapezium / com_registered | [0.0249836593, -0.109089379, 0.191313422] | [0.0249836593, -0.109089379, 0.191313422] | [0.0249836593, -0.109089379, 0.191313422] | [0, 0, 0] | eligible; compared after Kabsch alignment | [geometry/inference input L427](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Arm_Hand_r.xml#L427) | [geometry/inference input L400](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Arm_Hand_r.xml#L400) | [geometry/inference input L400](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Arm_Hand_r.xml#L400) |
| firstmc1 / com_registered | [0.0249894814, -0.109090465, 0.191313658] | [0.0249894814, -0.109090465, 0.191313658] | [0.0249894814, -0.109090465, 0.191313658] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L434](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Arm_Hand_r.xml#L434) | [CoM/kinematic input L407](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Arm_Hand_r.xml#L407) | [CoM/kinematic input L407](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Arm_Hand_r.xml#L407) |
| firstmc / com_registered | [0.0412509536, -0.127879707, 0.181254938] | [0.0412509536, -0.127879707, 0.181254938] | [0.0412509536, -0.127879707, 0.181254938] | [0, 0, 0] | eligible; compared after Kabsch alignment | [geometry/inference input L438](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Arm_Hand_r.xml#L438) | [geometry/inference input L410](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Arm_Hand_r.xml#L410) | [geometry/inference input L410](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Arm_Hand_r.xml#L410) |
| proximal_thumb / com_registered | [0.0589903961, -0.157123043, 0.167389313] | [0.0589903961, -0.157123043, 0.167389313] | [0.0589903961, -0.157123043, 0.167389313] | [0, 0, 0] | eligible; compared after Kabsch alignment | [geometry/inference input L459](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Arm_Hand_r.xml#L459) | [geometry/inference input L428](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Arm_Hand_r.xml#L428) | [geometry/inference input L428](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Arm_Hand_r.xml#L428) |
| distal_thumb / com_registered | [0.0708619125, -0.176592244, 0.158272142] | [0.0708619125, -0.176592244, 0.158272142] | [0.0708619125, -0.176592244, 0.158272142] | [0, 0, 0] | eligible; compared after Kabsch alignment | [geometry/inference input L477](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Arm_Hand_r.xml#L477) | [geometry/inference input L443](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Arm_Hand_r.xml#L443) | [geometry/inference input L443](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Arm_Hand_r.xml#L443) |
| trapezoid / com_registered | [0.0195252434, -0.109001744, 0.199663909] | [0.0195252434, -0.109001744, 0.199663909] | [0.0195252434, -0.109001744, 0.199663909] | [0, 0, 0] | eligible; compared after Kabsch alignment | [geometry/inference input L490](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Arm_Hand_r.xml#L490) | [geometry/inference input L454](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Arm_Hand_r.xml#L454) | [geometry/inference input L454](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Arm_Hand_r.xml#L454) |
| hamate / com_registered | [-0.000435080822, -0.108957993, 0.203126795] | [-0.000435080822, -0.108957993, 0.203126795] | [-0.000435080822, -0.108957993, 0.203126795] | [0, 0, 0] | eligible; compared after Kabsch alignment | [geometry/inference input L493](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Arm_Hand_r.xml#L493) | [geometry/inference input L457](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Arm_Hand_r.xml#L457) | [geometry/inference input L457](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Arm_Hand_r.xml#L457) |
| secondmc / com_registered | [0.0281473273, -0.141973377, 0.205809575] | [0.0281473273, -0.141973377, 0.205809575] | [0.0281473273, -0.141973377, 0.205809575] | [0, 0, 0] | eligible; compared after Kabsch alignment | [geometry/inference input L498](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Arm_Hand_r.xml#L498) | [geometry/inference input L462](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Arm_Hand_r.xml#L462) | [geometry/inference input L462](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Arm_Hand_r.xml#L462) |
| 2proxph / com_registered | [0.0401512714, -0.190680045, 0.213360908] | [0.0401512714, -0.190680045, 0.213360908] | [0.0401512714, -0.190680045, 0.213360908] | [0, 0, 0] | eligible; compared after Kabsch alignment | [geometry/inference input L526](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Arm_Hand_r.xml#L526) | [geometry/inference input L486](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Arm_Hand_r.xml#L486) | [geometry/inference input L486](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Arm_Hand_r.xml#L486) |
| 2midph / com_registered | [0.0477016813, -0.222398976, 0.216509996] | [0.0477016813, -0.222398976, 0.216509996] | [0.0477016813, -0.222398976, 0.216509996] | [0, 0, 0] | eligible; compared after Kabsch alignment | [geometry/inference input L557](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Arm_Hand_r.xml#L557) | [geometry/inference input L510](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Arm_Hand_r.xml#L510) | [geometry/inference input L510](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Arm_Hand_r.xml#L510) |
| 2distph / com_registered | [0.0523696008, -0.24287225, 0.217445406] | [0.0523696008, -0.24287225, 0.217445406] | [0.0523696008, -0.24287225, 0.217445406] | [0, 0, 0] | eligible; compared after Kabsch alignment | [geometry/inference input L576](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Arm_Hand_r.xml#L576) | [geometry/inference input L525](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Arm_Hand_r.xml#L525) | [geometry/inference input L525](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Arm_Hand_r.xml#L525) |
| thirdmc / com_registered | [0.0144477936, -0.144580099, 0.210181465] | [0.0144477936, -0.144580099, 0.210181465] | [0.0144477936, -0.144580099, 0.210181465] | [0, 0, 0] | eligible; compared after Kabsch alignment | [geometry/inference input L589](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Arm_Hand_r.xml#L589) | [geometry/inference input L536](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Arm_Hand_r.xml#L536) | [geometry/inference input L536](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Arm_Hand_r.xml#L536) |
| 3proxph / com_registered | [0.019907328, -0.19287215, 0.21594439] | [0.019907328, -0.19287215, 0.21594439] | [0.019907328, -0.19287215, 0.21594439] | [0, 0, 0] | eligible; compared after Kabsch alignment | [geometry/inference input L614](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Arm_Hand_r.xml#L614) | [geometry/inference input L559](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Arm_Hand_r.xml#L559) | [geometry/inference input L559](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Arm_Hand_r.xml#L559) |
| 3midph / com_registered | [0.0246394184, -0.228725899, 0.218095716] | [0.0246394184, -0.228725899, 0.218095716] | [0.0246394184, -0.228725899, 0.218095716] | [0, 0, 0] | eligible; compared after Kabsch alignment | [geometry/inference input L635](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Arm_Hand_r.xml#L635) | [geometry/inference input L576](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Arm_Hand_r.xml#L576) | [geometry/inference input L576](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Arm_Hand_r.xml#L576) |
| 3distph / com_registered | [0.0280817166, -0.25245968, 0.219751637] | [0.0280817166, -0.25245968, 0.219751637] | [0.0280817166, -0.25245968, 0.219751637] | [0, 0, 0] | eligible; compared after Kabsch alignment | [geometry/inference input L649](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Arm_Hand_r.xml#L649) | [geometry/inference input L587](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Arm_Hand_r.xml#L587) | [geometry/inference input L587](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Arm_Hand_r.xml#L587) |
| fourthmc / com_registered | [0.00211110359, -0.145222237, 0.209412059] | [0.00211110359, -0.145222237, 0.209412059] | [0.00211110359, -0.145222237, 0.209412059] | [0, 0, 0] | eligible; compared after Kabsch alignment | [geometry/inference input L661](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Arm_Hand_r.xml#L661) | [geometry/inference input L597](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Arm_Hand_r.xml#L597) | [geometry/inference input L597](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Arm_Hand_r.xml#L597) |
| 4proxph / com_registered | [0.000920412028, -0.191241869, 0.215942077] | [0.000920412028, -0.191241869, 0.215942077] | [0.000920412028, -0.191241869, 0.215942077] | [0, 0, 0] | eligible; compared after Kabsch alignment | [geometry/inference input L682](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Arm_Hand_r.xml#L682) | [geometry/inference input L615](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Arm_Hand_r.xml#L615) | [geometry/inference input L615](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Arm_Hand_r.xml#L615) |
| 4midph / com_registered | [0.000709623863, -0.222186802, 0.22035041] | [0.000709623863, -0.222186802, 0.22035041] | [0.000709623863, -0.222186802, 0.22035041] | [0, 0, 0] | eligible; compared after Kabsch alignment | [geometry/inference input L703](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Arm_Hand_r.xml#L703) | [geometry/inference input L632](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Arm_Hand_r.xml#L632) | [geometry/inference input L632](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Arm_Hand_r.xml#L632) |
| 4distph / com_registered | [0.00100938636, -0.244580636, 0.222276925] | [0.00100938636, -0.244580636, 0.222276925] | [0.00100938636, -0.244580636, 0.222276925] | [0, 0, 0] | eligible; compared after Kabsch alignment | [geometry/inference input L717](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Arm_Hand_r.xml#L717) | [geometry/inference input L643](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Arm_Hand_r.xml#L643) | [geometry/inference input L643](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Arm_Hand_r.xml#L643) |
| fifthmc / com_registered | [-0.0101816808, -0.139253205, 0.206501133] | [-0.0101816808, -0.139253205, 0.206501133] | [-0.0101816808, -0.139253205, 0.206501133] | [0, 0, 0] | eligible; compared after Kabsch alignment | [geometry/inference input L728](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Arm_Hand_r.xml#L728) | [geometry/inference input L653](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Arm_Hand_r.xml#L653) | [geometry/inference input L653](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Arm_Hand_r.xml#L653) |
| 5proxph / com_registered | [-0.0190734519, -0.181951101, 0.21512205] | [-0.0190734519, -0.181951101, 0.21512205] | [-0.0190734519, -0.181951101, 0.21512205] | [0, 0, 0] | eligible; compared after Kabsch alignment | [geometry/inference input L752](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Arm_Hand_r.xml#L752) | [geometry/inference input L675](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Arm_Hand_r.xml#L675) | [geometry/inference input L675](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Arm_Hand_r.xml#L675) |
| 5midph / com_registered | [-0.0255732125, -0.208188663, 0.217263122] | [-0.0255732125, -0.208188663, 0.217263122] | [-0.0255732125, -0.208188663, 0.217263122] | [0, 0, 0] | eligible; compared after Kabsch alignment | [geometry/inference input L777](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Arm_Hand_r.xml#L777) | [geometry/inference input L696](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Arm_Hand_r.xml#L696) | [geometry/inference input L696](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Arm_Hand_r.xml#L696) |
| 5distph / com_registered | [-0.0305671864, -0.22512762, 0.219764266] | [-0.0305671864, -0.22512762, 0.219764266] | [-0.0305671864, -0.22512762, 0.219764266] | [0, 0, 0] | eligible; compared after Kabsch alignment | [geometry/inference input L794](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Arm_Hand_r.xml#L794) | [geometry/inference input L710](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Arm_Hand_r.xml#L710) | [geometry/inference input L710](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Arm_Hand_r.xml#L710) |
| clavicle_l / com_registered | [-0.0321808974, 0.471910976, -0.080454989] | [-0.0321808974, 0.471910976, -0.080454989] | [-0.0321808974, 0.471910976, -0.080454989] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L4](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Arm_Hand_Vis_l.xml#L4) | [CoM/kinematic input L3](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Arm_Hand_Vis_l.xml#L3) | [CoM/kinematic input L3](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Arm_Hand_Vis_l.xml#L3) |
| clavphant_l / com_registered | [-0.0575524664, 0.48386516, -0.1607079] | [-0.0575524664, 0.48386516, -0.1607079] | [-0.0575524664, 0.48386516, -0.1607079] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L13](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Arm_Hand_Vis_l.xml#L13) | [CoM/kinematic input L12](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Arm_Hand_Vis_l.xml#L12) | [CoM/kinematic input L12](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Arm_Hand_Vis_l.xml#L12) |
| scapula_l / com_registered | [-0.113677342, 0.442011516, -0.117664899] | [-0.113677342, 0.442011516, -0.117664899] | [-0.113677342, 0.442011516, -0.117664899] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L16](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Arm_Hand_Vis_l.xml#L16) | [CoM/kinematic input L14](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Arm_Hand_Vis_l.xml#L14) | [CoM/kinematic input L14](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Arm_Hand_Vis_l.xml#L14) |
| scapphant_l / com_registered | [-0.063661154, 0.449298079, -0.170506027] | [-0.063661154, 0.449298079, -0.170506027] | [-0.063661154, 0.449298079, -0.170506027] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L87](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Arm_Hand_Vis_l.xml#L87) | [CoM/kinematic input L84](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Arm_Hand_Vis_l.xml#L84) | [CoM/kinematic input L84](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Arm_Hand_Vis_l.xml#L84) |
| humphant_l / com_registered | [-0.063661154, 0.449298079, -0.170506027] | [-0.063661154, 0.449298079, -0.170506027] | [-0.063661154, 0.449298079, -0.170506027] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L89](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Arm_Hand_Vis_l.xml#L89) | [CoM/kinematic input L86](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Arm_Hand_Vis_l.xml#L86) | [CoM/kinematic input L86](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Arm_Hand_Vis_l.xml#L86) |
| humphant1_l / com_registered | [-0.063661154, 0.449298079, -0.170506027] | [-0.063661154, 0.449298079, -0.170506027] | [-0.063661154, 0.449298079, -0.170506027] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L91](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Arm_Hand_Vis_l.xml#L91) | [CoM/kinematic input L88](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Arm_Hand_Vis_l.xml#L88) | [CoM/kinematic input L88](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Arm_Hand_Vis_l.xml#L88) |
| humerus_l / com_registered | [-0.0361297704, 0.310854578, -0.156234076] | [-0.0361297704, 0.310854578, -0.156234076] | [-0.0361297704, 0.310854578, -0.156234076] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L93](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Arm_Hand_Vis_l.xml#L93) | [CoM/kinematic input L90](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Arm_Hand_Vis_l.xml#L90) | [CoM/kinematic input L90](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Arm_Hand_Vis_l.xml#L90) |
| ulna_l / com_registered | [-0.0174194343, 0.0653566252, -0.18106773] | [-0.0174194343, 0.0653566252, -0.18106773] | [-0.0174194343, 0.0653566252, -0.18106773] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L238](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Arm_Hand_Vis_l.xml#L238) | [CoM/kinematic input L224](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Arm_Hand_Vis_l.xml#L224) | [CoM/kinematic input L224](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Arm_Hand_Vis_l.xml#L224) |
| radius_l / com_registered | [0.015128846, -0.0295470511, -0.190218271] | [0.015128846, -0.0295470511, -0.190218271] | [0.015128846, -0.0295470511, -0.190218271] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L268](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Arm_Hand_Vis_l.xml#L268) | [CoM/kinematic input L252](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Arm_Hand_Vis_l.xml#L252) | [CoM/kinematic input L252](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Arm_Hand_Vis_l.xml#L252) |
| proximal_row_l / com_registered | [0.00537814163, -0.0956718616, -0.198751356] | [0.00537814163, -0.0956718616, -0.198751356] | [0.00537814163, -0.0956718616, -0.198751356] | [0, 0, 0] | eligible; compared after Kabsch alignment | [geometry/inference input L331](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Arm_Hand_Vis_l.xml#L331) | [geometry/inference input L313](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Arm_Hand_Vis_l.xml#L313) | [geometry/inference input L313](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Arm_Hand_Vis_l.xml#L313) |
| capitate_l / com_registered | [0.0103491448, -0.10563313, -0.202916485] | [0.0103491448, -0.10563313, -0.202916485] | [0.0103491448, -0.10563313, -0.202916485] | [0, 0, 0] | eligible; compared after Kabsch alignment | [geometry/inference input L379](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Arm_Hand_Vis_l.xml#L379) | [geometry/inference input L356](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Arm_Hand_Vis_l.xml#L356) | [geometry/inference input L356](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Arm_Hand_Vis_l.xml#L356) |
| trapezium_l / com_registered | [0.0249836593, -0.109089379, -0.191313422] | [0.0249836593, -0.109089379, -0.191313422] | [0.0249836593, -0.109089379, -0.191313422] | [0, 0, 0] | eligible; compared after Kabsch alignment | [geometry/inference input L402](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Arm_Hand_Vis_l.xml#L402) | [geometry/inference input L379](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Arm_Hand_Vis_l.xml#L379) | [geometry/inference input L379](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Arm_Hand_Vis_l.xml#L379) |
| firstmc1_l / com_registered | [0.0249894814, -0.109090465, -0.191313658] | [0.0249894814, -0.109090465, -0.191313658] | [0.0249894814, -0.109090465, -0.191313658] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L408](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Arm_Hand_Vis_l.xml#L408) | [CoM/kinematic input L385](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Arm_Hand_Vis_l.xml#L385) | [CoM/kinematic input L385](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Arm_Hand_Vis_l.xml#L385) |
| firstmc_l / com_registered | [0.0419389165, -0.127720326, -0.181709388] | [0.0419389165, -0.127720326, -0.181709388] | [0.0419389165, -0.127720326, -0.181709388] | [0, 0, 0] | eligible; compared after Kabsch alignment | [geometry/inference input L410](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Arm_Hand_Vis_l.xml#L410) | [geometry/inference input L387](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Arm_Hand_Vis_l.xml#L387) | [geometry/inference input L387](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Arm_Hand_Vis_l.xml#L387) |
| proximal_thumb_l / com_registered | [0.0590026522, -0.156313526, -0.16775753] | [0.0590026522, -0.156313526, -0.16775753] | [0.0590026522, -0.156313526, -0.16775753] | [0, 0, 0] | eligible; compared after Kabsch alignment | [geometry/inference input L427](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Arm_Hand_Vis_l.xml#L427) | [geometry/inference input L403](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Arm_Hand_Vis_l.xml#L403) | [geometry/inference input L403](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Arm_Hand_Vis_l.xml#L403) |
| distal_thumb_l / com_registered | [0.0694393205, -0.175473957, -0.158845384] | [0.0694393205, -0.175473957, -0.158845384] | [0.0694393205, -0.175473957, -0.158845384] | [0, 0, 0] | eligible; compared after Kabsch alignment | [geometry/inference input L441](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Arm_Hand_Vis_l.xml#L441) | [geometry/inference input L416](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Arm_Hand_Vis_l.xml#L416) | [geometry/inference input L416](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Arm_Hand_Vis_l.xml#L416) |
| trapezoid_l / com_registered | [0.0195252434, -0.109001744, -0.199663909] | [0.0195252434, -0.109001744, -0.199663909] | [0.0195252434, -0.109001744, -0.199663909] | [0, 0, 0] | eligible; compared after Kabsch alignment | [geometry/inference input L450](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Arm_Hand_Vis_l.xml#L450) | [geometry/inference input L425](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Arm_Hand_Vis_l.xml#L425) | [geometry/inference input L425](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Arm_Hand_Vis_l.xml#L425) |
| hamate_l / com_registered | [-0.000435080822, -0.108957993, -0.203126795] | [-0.000435080822, -0.108957993, -0.203126795] | [-0.000435080822, -0.108957993, -0.203126795] | [0, 0, 0] | eligible; compared after Kabsch alignment | [geometry/inference input L453](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Arm_Hand_Vis_l.xml#L453) | [geometry/inference input L428](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Arm_Hand_Vis_l.xml#L428) | [geometry/inference input L428](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Arm_Hand_Vis_l.xml#L428) |
| secondmc_l / com_registered | [0.0281154081, -0.141872116, -0.206518106] | [0.0281154081, -0.141872116, -0.206518106] | [0.0281154081, -0.141872116, -0.206518106] | [0, 0, 0] | eligible; compared after Kabsch alignment | [geometry/inference input L458](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Arm_Hand_Vis_l.xml#L458) | [geometry/inference input L433](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Arm_Hand_Vis_l.xml#L433) | [geometry/inference input L433](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Arm_Hand_Vis_l.xml#L433) |
| 2proxph_l / com_registered | [0.0405526589, -0.191857126, -0.21422414] | [0.0405526589, -0.191857126, -0.21422414] | [0.0405526589, -0.191857126, -0.21422414] | [0, 0, 0] | eligible; compared after Kabsch alignment | [geometry/inference input L484](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Arm_Hand_Vis_l.xml#L484) | [geometry/inference input L456](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Arm_Hand_Vis_l.xml#L456) | [geometry/inference input L456](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Arm_Hand_Vis_l.xml#L456) |
| 2midph_l / com_registered | [0.0482314331, -0.223834523, -0.216825915] | [0.0482314331, -0.223834523, -0.216825915] | [0.0482314331, -0.223834523, -0.216825915] | [0, 0, 0] | eligible; compared after Kabsch alignment | [geometry/inference input L509](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Arm_Hand_Vis_l.xml#L509) | [geometry/inference input L477](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Arm_Hand_Vis_l.xml#L477) | [geometry/inference input L477](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Arm_Hand_Vis_l.xml#L477) |
| 2distph_l / com_registered | [0.0524947494, -0.243336444, -0.217722093] | [0.0524947494, -0.243336444, -0.217722093] | [0.0524947494, -0.243336444, -0.217722093] | [0, 0, 0] | eligible; compared after Kabsch alignment | [geometry/inference input L524](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Arm_Hand_Vis_l.xml#L524) | [geometry/inference input L490](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Arm_Hand_Vis_l.xml#L490) | [geometry/inference input L490](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Arm_Hand_Vis_l.xml#L490) |
| thirdmc_l / com_registered | [0.014407816, -0.144153522, -0.209981758] | [0.014407816, -0.144153522, -0.209981758] | [0.014407816, -0.144153522, -0.209981758] | [0, 0, 0] | eligible; compared after Kabsch alignment | [geometry/inference input L533](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Arm_Hand_Vis_l.xml#L533) | [geometry/inference input L499](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Arm_Hand_Vis_l.xml#L499) | [geometry/inference input L499](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Arm_Hand_Vis_l.xml#L499) |
| 3proxph_l / com_registered | [0.0200912877, -0.193960285, -0.21637229] | [0.0200912877, -0.193960285, -0.21637229] | [0.0200912877, -0.193960285, -0.21637229] | [0, 0, 0] | eligible; compared after Kabsch alignment | [geometry/inference input L556](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Arm_Hand_Vis_l.xml#L556) | [geometry/inference input L521](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Arm_Hand_Vis_l.xml#L521) | [geometry/inference input L521](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Arm_Hand_Vis_l.xml#L521) |
| 3midph_l / com_registered | [0.0243607521, -0.229536738, -0.219557743] | [0.0243607521, -0.229536738, -0.219557743] | [0.0243607521, -0.229536738, -0.219557743] | [0, 0, 0] | eligible; compared after Kabsch alignment | [geometry/inference input L571](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Arm_Hand_Vis_l.xml#L571) | [geometry/inference input L535](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Arm_Hand_Vis_l.xml#L535) | [geometry/inference input L535](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Arm_Hand_Vis_l.xml#L535) |
| 3distph_l / com_registered | [0.0274265832, -0.252098501, -0.219776062] | [0.0274265832, -0.252098501, -0.219776062] | [0.0274265832, -0.252098501, -0.219776062] | [0, 0, 0] | eligible; compared after Kabsch alignment | [geometry/inference input L581](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Arm_Hand_Vis_l.xml#L581) | [geometry/inference input L544](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Arm_Hand_Vis_l.xml#L544) | [geometry/inference input L544](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Arm_Hand_Vis_l.xml#L544) |
| fourthmc_l / com_registered | [0.00184924822, -0.146104917, -0.209399667] | [0.00184924822, -0.146104917, -0.209399667] | [0.00184924822, -0.146104917, -0.209399667] | [0, 0, 0] | eligible; compared after Kabsch alignment | [geometry/inference input L589](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Arm_Hand_Vis_l.xml#L589) | [geometry/inference input L552](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Arm_Hand_Vis_l.xml#L552) | [geometry/inference input L552](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Arm_Hand_Vis_l.xml#L552) |
| 4proxph_l / com_registered | [0.000943451269, -0.191524344, -0.216517923] | [0.000943451269, -0.191524344, -0.216517923] | [0.000943451269, -0.191524344, -0.216517923] | [0, 0, 0] | eligible; compared after Kabsch alignment | [geometry/inference input L606](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Arm_Hand_Vis_l.xml#L606) | [geometry/inference input L568](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Arm_Hand_Vis_l.xml#L568) | [geometry/inference input L568](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Arm_Hand_Vis_l.xml#L568) |
| 4midph_l / com_registered | [0.000260743958, -0.223091936, -0.220986948] | [0.000260743958, -0.223091936, -0.220986948] | [0.000260743958, -0.223091936, -0.220986948] | [0, 0, 0] | eligible; compared after Kabsch alignment | [geometry/inference input L621](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Arm_Hand_Vis_l.xml#L621) | [geometry/inference input L582](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Arm_Hand_Vis_l.xml#L582) | [geometry/inference input L582](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Arm_Hand_Vis_l.xml#L582) |
| 4distph_l / com_registered | [0.000577323512, -0.243558885, -0.223136343] | [0.000577323512, -0.243558885, -0.223136343] | [0.000577323512, -0.243558885, -0.223136343] | [0, 0, 0] | eligible; compared after Kabsch alignment | [geometry/inference input L631](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Arm_Hand_Vis_l.xml#L631) | [geometry/inference input L591](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Arm_Hand_Vis_l.xml#L591) | [geometry/inference input L591](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Arm_Hand_Vis_l.xml#L591) |
| fifthmc_l / com_registered | [-0.0109491886, -0.140242658, -0.207536296] | [-0.0109491886, -0.140242658, -0.207536296] | [-0.0109491886, -0.140242658, -0.207536296] | [0, 0, 0] | eligible; compared after Kabsch alignment | [geometry/inference input L639](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Arm_Hand_Vis_l.xml#L639) | [geometry/inference input L599](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Arm_Hand_Vis_l.xml#L599) | [geometry/inference input L599](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Arm_Hand_Vis_l.xml#L599) |
| 5proxph_l / com_registered | [-0.0184474454, -0.180202323, -0.215026393] | [-0.0184474454, -0.180202323, -0.215026393] | [-0.0184474454, -0.180202323, -0.215026393] | [0, 0, 0] | eligible; compared after Kabsch alignment | [geometry/inference input L660](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Arm_Hand_Vis_l.xml#L660) | [geometry/inference input L619](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Arm_Hand_Vis_l.xml#L619) | [geometry/inference input L619](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Arm_Hand_Vis_l.xml#L619) |
| 5midph_l / com_registered | [-0.0258236372, -0.207401842, -0.218167704] | [-0.0258236372, -0.207401842, -0.218167704] | [-0.0258236372, -0.207401842, -0.218167704] | [0, 0, 0] | eligible; compared after Kabsch alignment | [geometry/inference input L679](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Arm_Hand_Vis_l.xml#L679) | [geometry/inference input L637](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Arm_Hand_Vis_l.xml#L637) | [geometry/inference input L637](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Arm_Hand_Vis_l.xml#L637) |
| 5distph_l / com_registered | [-0.0304835653, -0.223576939, -0.220473575] | [-0.0304835653, -0.223576939, -0.220473575] | [-0.0304835653, -0.223576939, -0.220473575] | [0, 0, 0] | eligible; compared after Kabsch alignment | [geometry/inference input L692](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Arm_Hand_Vis_l.xml#L692) | [geometry/inference input L649](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Arm_Hand_Vis_l.xml#L649) | [geometry/inference input L649](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Arm_Hand_Vis_l.xml#L649) |
| head_neck / com_registered | [-0.0485573006, 0.695586706, 9.25669e-06] | [-0.0485573006, 0.695586706, 9.25669e-06] | [-0.0485573006, 0.695586706, 9.25669e-06] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L971](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Torso_Unimanual.xml#L971) | [CoM/kinematic input L930](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Torso_Unimanual.xml#L930) | [CoM/kinematic input L930](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Torso_Unimanual.xml#L930) |
| rib1_R / com_registered | [-0.06462179, 0.506737368, 0.0501811579] | [-0.06462179, 0.506737368, 0.0501811579] | [-0.06462179, 0.506737368, 0.0501811579] | [0, 0, 0] | eligible; compared after Kabsch alignment | [geometry/inference input L1062](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Torso_Unimanual.xml#L1062) | [geometry/inference input L1013](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Torso_Unimanual.xml#L1013) | [geometry/inference input L1013](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Torso_Unimanual.xml#L1013) |
| rib1_L / com_registered | [-0.0646209974, 0.506737031, -0.050181516] | [-0.0646209974, 0.506737031, -0.050181516] | [-0.0646209974, 0.506737031, -0.050181516] | [0, 0, 0] | eligible; compared after Kabsch alignment | [geometry/inference input L1079](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Torso_Unimanual.xml#L1079) | [geometry/inference input L1029](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Torso_Unimanual.xml#L1029) | [geometry/inference input L1029](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Torso_Unimanual.xml#L1029) |
| rib2_R / com_registered | [-0.0707904403, 0.478733106, 0.0662987] | [-0.0707904403, 0.478733106, 0.0662987] | [-0.0707904403, 0.478733106, 0.0662987] | [0, 0, 0] | eligible; compared after Kabsch alignment | [geometry/inference input L1097](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Torso_Unimanual.xml#L1097) | [geometry/inference input L1046](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Torso_Unimanual.xml#L1046) | [geometry/inference input L1046](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Torso_Unimanual.xml#L1046) |
| rib2_L / com_registered | [-0.0707904409, 0.478733504, -0.0662988091] | [-0.0707904409, 0.478733504, -0.0662988091] | [-0.0707904409, 0.478733504, -0.0662988091] | [0, 0, 0] | eligible; compared after Kabsch alignment | [geometry/inference input L1126](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Torso_Unimanual.xml#L1126) | [geometry/inference input L1074](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Torso_Unimanual.xml#L1074) | [geometry/inference input L1074](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Torso_Unimanual.xml#L1074) |
| rib3_R / com_registered | [-0.0709376439, 0.446629438, 0.0806092771] | [-0.0709376439, 0.446629438, 0.0806092771] | [-0.0709376439, 0.446629438, 0.0806092771] | [0, 0, 0] | eligible; compared after Kabsch alignment | [geometry/inference input L1156](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Torso_Unimanual.xml#L1156) | [geometry/inference input L1103](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Torso_Unimanual.xml#L1103) | [geometry/inference input L1103](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Torso_Unimanual.xml#L1103) |
| rib3_L / com_registered | [-0.0709366275, 0.446629377, -0.0806097228] | [-0.0709366275, 0.446629377, -0.0806097228] | [-0.0709366275, 0.446629377, -0.0806097228] | [0, 0, 0] | eligible; compared after Kabsch alignment | [geometry/inference input L1185](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Torso_Unimanual.xml#L1185) | [geometry/inference input L1131](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Torso_Unimanual.xml#L1131) | [geometry/inference input L1131](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Torso_Unimanual.xml#L1131) |
| rib4_R / com_registered | [-0.0703979872, 0.417828204, 0.0951714621] | [-0.0703979872, 0.417828204, 0.0951714621] | [-0.0703979872, 0.417828204, 0.0951714621] | [0, 0, 0] | eligible; compared after Kabsch alignment | [geometry/inference input L1215](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Torso_Unimanual.xml#L1215) | [geometry/inference input L1160](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Torso_Unimanual.xml#L1160) | [geometry/inference input L1160](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Torso_Unimanual.xml#L1160) |
| rib4_L / com_registered | [-0.0699356394, 0.417569931, -0.0952130082] | [-0.0699356394, 0.417569931, -0.0952130082] | [-0.0699356394, 0.417569931, -0.0952130082] | [0, 0, 0] | eligible; compared after Kabsch alignment | [geometry/inference input L1244](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Torso_Unimanual.xml#L1244) | [geometry/inference input L1188](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Torso_Unimanual.xml#L1188) | [geometry/inference input L1188](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Torso_Unimanual.xml#L1188) |
| rib5_R / com_registered | [-0.0737407464, 0.385313506, 0.099377271] | [-0.0737407464, 0.385313506, 0.099377271] | [-0.0737407464, 0.385313506, 0.099377271] | [0, 0, 0] | eligible; compared after Kabsch alignment | [geometry/inference input L1274](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Torso_Unimanual.xml#L1274) | [geometry/inference input L1217](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Torso_Unimanual.xml#L1217) | [geometry/inference input L1217](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Torso_Unimanual.xml#L1217) |
| rib5_L / com_registered | [-0.0736256485, 0.385260307, -0.0993645834] | [-0.0736256485, 0.385260307, -0.0993645834] | [-0.0736256485, 0.385260307, -0.0993645834] | [0, 0, 0] | eligible; compared after Kabsch alignment | [geometry/inference input L1313](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Torso_Unimanual.xml#L1313) | [geometry/inference input L1255](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Torso_Unimanual.xml#L1255) | [geometry/inference input L1255](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Torso_Unimanual.xml#L1255) |
| rib6_R / com_registered | [-0.0881989572, 0.362688819, 0.107749531] | [-0.0881989572, 0.362688819, 0.107749531] | [-0.0881989572, 0.362688819, 0.107749531] | [0, 0, 0] | eligible; compared after Kabsch alignment | [geometry/inference input L1353](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Torso_Unimanual.xml#L1353) | [geometry/inference input L1294](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Torso_Unimanual.xml#L1294) | [geometry/inference input L1294](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Torso_Unimanual.xml#L1294) |
| rib6_L / com_registered | [-0.0881985739, 0.362689167, -0.107750178] | [-0.0881985739, 0.362689167, -0.107750178] | [-0.0881985739, 0.362689167, -0.107750178] | [0, 0, 0] | eligible; compared after Kabsch alignment | [geometry/inference input L1400](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Torso_Unimanual.xml#L1400) | [geometry/inference input L1340](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Torso_Unimanual.xml#L1340) | [geometry/inference input L1340](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Torso_Unimanual.xml#L1340) |
| rib7_R / com_registered | [-0.0978224473, 0.335551299, 0.110260926] | [-0.0978224473, 0.335551299, 0.110260926] | [-0.0978224473, 0.335551299, 0.110260926] | [0, 0, 0] | eligible; compared after Kabsch alignment | [geometry/inference input L1448](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Torso_Unimanual.xml#L1448) | [geometry/inference input L1387](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Torso_Unimanual.xml#L1387) | [geometry/inference input L1387](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Torso_Unimanual.xml#L1387) |
| rib7_L / com_registered | [-0.0978196302, 0.335550325, -0.110261539] | [-0.0978196302, 0.335550325, -0.110261539] | [-0.0978196302, 0.335550325, -0.110261539] | [0, 0, 0] | eligible; compared after Kabsch alignment | [geometry/inference input L1498](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Torso_Unimanual.xml#L1498) | [geometry/inference input L1436](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Torso_Unimanual.xml#L1436) | [geometry/inference input L1436](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Torso_Unimanual.xml#L1436) |
| rib8_R / com_registered | [-0.106010526, 0.306432868, 0.110317216] | [-0.106010526, 0.306432868, 0.110317216] | [-0.106010526, 0.306432868, 0.110317216] | [0, 0, 0] | eligible; compared after Kabsch alignment | [geometry/inference input L1549](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Torso_Unimanual.xml#L1549) | [geometry/inference input L1486](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Torso_Unimanual.xml#L1486) | [geometry/inference input L1486](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Torso_Unimanual.xml#L1486) |
| rib8_L / com_registered | [-0.106010625, 0.306433657, -0.110317483] | [-0.106010625, 0.306433657, -0.110317483] | [-0.106010625, 0.306433657, -0.110317483] | [0, 0, 0] | eligible; compared after Kabsch alignment | [geometry/inference input L1603](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Torso_Unimanual.xml#L1603) | [geometry/inference input L1539](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Torso_Unimanual.xml#L1539) | [geometry/inference input L1539](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Torso_Unimanual.xml#L1539) |
| rib9_R / com_registered | [-0.112476129, 0.278778393, 0.110376814] | [-0.112476129, 0.278778393, 0.110376814] | [-0.112476129, 0.278778393, 0.110376814] | [0, 0, 0] | eligible; compared after Kabsch alignment | [geometry/inference input L1658](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Torso_Unimanual.xml#L1658) | [geometry/inference input L1593](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Torso_Unimanual.xml#L1593) | [geometry/inference input L1593](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Torso_Unimanual.xml#L1593) |
| rib9_L / com_registered | [-0.112686967, 0.278978528, -0.110210144] | [-0.112686967, 0.278978528, -0.110210144] | [-0.112686967, 0.278978528, -0.110210144] | [0, 0, 0] | eligible; compared after Kabsch alignment | [geometry/inference input L1711](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Torso_Unimanual.xml#L1711) | [geometry/inference input L1645](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Torso_Unimanual.xml#L1645) | [geometry/inference input L1645](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Torso_Unimanual.xml#L1645) |
| rib10_R / com_registered | [-0.134193033, 0.26451153, 0.0957065751] | [-0.134193033, 0.26451153, 0.0957065751] | [-0.134193033, 0.26451153, 0.0957065751] | [0, 0, 0] | eligible; compared after Kabsch alignment | [geometry/inference input L1765](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Torso_Unimanual.xml#L1765) | [geometry/inference input L1698](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Torso_Unimanual.xml#L1698) | [geometry/inference input L1698](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Torso_Unimanual.xml#L1698) |
| rib10_L / com_registered | [-0.134186819, 0.264505928, -0.0957128668] | [-0.134186819, 0.264505928, -0.0957128668] | [-0.134186819, 0.264505928, -0.0957128668] | [0, 0, 0] | eligible; compared after Kabsch alignment | [geometry/inference input L1806](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Torso_Unimanual.xml#L1806) | [geometry/inference input L1738](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Torso_Unimanual.xml#L1738) | [geometry/inference input L1738](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Torso_Unimanual.xml#L1738) |
| rib11_R / com_registered | [-0.138058875, 0.235462247, 0.0759469994] | [-0.138058875, 0.235462247, 0.0759469994] | [-0.138058875, 0.235462247, 0.0759469994] | [0, 0, 0] | eligible; compared after Kabsch alignment | [geometry/inference input L1847](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Torso_Unimanual.xml#L1847) | [geometry/inference input L1779](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Torso_Unimanual.xml#L1779) | [geometry/inference input L1779](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Torso_Unimanual.xml#L1779) |
| rib11_L / com_registered | [-0.138059083, 0.23546271, -0.0759472845] | [-0.138059083, 0.23546271, -0.0759472845] | [-0.138059083, 0.23546271, -0.0759472845] | [0, 0, 0] | eligible; compared after Kabsch alignment | [geometry/inference input L1873](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Torso_Unimanual.xml#L1873) | [geometry/inference input L1804](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Torso_Unimanual.xml#L1804) | [geometry/inference input L1804](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Torso_Unimanual.xml#L1804) |
| rib12_R / com_registered | [-0.13667813, 0.209485267, 0.0585629272] | [-0.13667813, 0.209485267, 0.0585629272] | [-0.13667813, 0.209485267, 0.0585629272] | [0, 0, 0] | eligible; compared after Kabsch alignment | [geometry/inference input L1900](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Torso_Unimanual.xml#L1900) | [geometry/inference input L1830](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Torso_Unimanual.xml#L1830) | [geometry/inference input L1830](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Torso_Unimanual.xml#L1830) |
| rib12_L / com_registered | [-0.136678119, 0.209485751, -0.0585628336] | [-0.136678119, 0.209485751, -0.0585628336] | [-0.136678119, 0.209485751, -0.0585628336] | [0, 0, 0] | eligible; compared after Kabsch alignment | [geometry/inference input L1927](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Torso_Unimanual.xml#L1927) | [geometry/inference input L1856](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Torso_Unimanual.xml#L1856) | [geometry/inference input L1856](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Torso_Unimanual.xml#L1856) |
| waterbottle / com_registered | [0.300003901, -0.0106275033, 0.279995281] | [0.300003901, -0.0106275033, 0.279995281] | [0.300003901, -0.0106275033, 0.279995281] | [0, 0, 0] | eligible; compared after Kabsch alignment | [geometry/inference input L2](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Waterbottle.xml#L2) | [geometry/inference input L20](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Waterbottle.xml#L20) | [geometry/inference input L20](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Waterbottle.xml#L20) |
| target / com_registered | [0.30000794, -0.012356929, 0.279990394] | [0.30000794, -0.012356929, 0.279990394] | [0.30000794, -0.012356929, 0.279990394] | [0, 0, 0] | eligible; compared after Kabsch alignment | [geometry/inference input L17](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Waterbottle.xml#L17) | [geometry/inference input L35](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Waterbottle.xml#L35) | [geometry/inference input L35](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Waterbottle.xml#L35) |
| table / com_registered | [0.45, -0.193806908, 8.15052732e-19] | [0.45, -0.193806908, 8.15052732e-19] | [0.45, -0.193806908, 8.15052732e-19] | [0, 0, 0] | eligible; compared after Kabsch alignment | [geometry/inference input L62](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/MS-Human-700-Manipulation.xml#L62) | [geometry/inference input L72](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/MS-Human-700-Manipulation.xml#L72) | [geometry/inference input L72](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/MS-Human-700-Manipulation.xml#L72) |

## Mass accounting

Every contributing compiled body mass is listed here so total/subtree sums can be checked. Links point to explicit inertials or to geometry inputs when the compiler inferred a mass. CoM links identify inertial inputs; world coordinates additionally use the ancestor transforms and the registration recorded below.

| M body | M kg / source | S kg / source | H kg / source |
|---|---|---|---|
| pelvis | 8.147 / [input L54](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/MS-Human-700-Manipulation.xml#L54) | 8.147 / [input L63](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/MS-Human-700-Manipulation.xml#L63) | 8.147 / [input L63](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/MS-Human-700-Manipulation.xml#L63) |
| femur_r | 6.269 / [input L3](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Leg_Foot_Vis_r.xml#L3) | 6.269 / [input L3](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Leg_Foot_Vis_r.xml#L3) | 6.269 / [input L3](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Leg_Foot_Vis_r.xml#L3) |
| tibia_r | 2.836 / [input L73](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Leg_Foot_Vis_r.xml#L73) | 2.836 / [input L64](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Leg_Foot_Vis_r.xml#L64) | 2.836 / [input L64](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Leg_Foot_Vis_r.xml#L64) |
| talus_r | 0.161 / [input L132](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Leg_Foot_Vis_r.xml#L132) | 0.161 / [input L117](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Leg_Foot_Vis_r.xml#L117) | 0.161 / [input L117](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Leg_Foot_Vis_r.xml#L117) |
| calcn_r | 0.617 / [input L136](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Leg_Foot_Vis_r.xml#L136) | 0.617 / [input L120](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Leg_Foot_Vis_r.xml#L120) | 0.617 / [input L120](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Leg_Foot_Vis_r.xml#L120) |
| toes_r | 0.081 / [input L163](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Leg_Foot_Vis_r.xml#L163) | 0.081 / [input L146](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Leg_Foot_Vis_r.xml#L146) | 0.081 / [input L146](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Leg_Foot_Vis_r.xml#L146) |
| patella_r | 0.062 / [input L180](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Leg_Foot_Vis_r.xml#L180) | 0.062 / [input L162](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Leg_Foot_Vis_r.xml#L162) | 0.062 / [input L162](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Leg_Foot_Vis_r.xml#L162) |
| femur_l | 6.269 / [input L3](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Leg_Foot_Vis_l.xml#L3) | 6.269 / [input L3](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Leg_Foot_Vis_l.xml#L3) | 6.269 / [input L3](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Leg_Foot_Vis_l.xml#L3) |
| tibia_l | 2.836 / [input L73](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Leg_Foot_Vis_l.xml#L73) | 2.836 / [input L64](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Leg_Foot_Vis_l.xml#L64) | 2.836 / [input L64](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Leg_Foot_Vis_l.xml#L64) |
| talus_l | 0.161 / [input L132](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Leg_Foot_Vis_l.xml#L132) | 0.161 / [input L117](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Leg_Foot_Vis_l.xml#L117) | 0.161 / [input L117](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Leg_Foot_Vis_l.xml#L117) |
| calcn_l | 0.617 / [input L136](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Leg_Foot_Vis_l.xml#L136) | 0.617 / [input L120](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Leg_Foot_Vis_l.xml#L120) | 0.617 / [input L120](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Leg_Foot_Vis_l.xml#L120) |
| toes_l | 0.081 / [input L163](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Leg_Foot_Vis_l.xml#L163) | 0.081 / [input L146](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Leg_Foot_Vis_l.xml#L146) | 0.081 / [input L146](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Leg_Foot_Vis_l.xml#L146) |
| patella_l | 0.062 / [input L180](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Leg_Foot_Vis_l.xml#L180) | 0.062 / [input L162](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Leg_Foot_Vis_l.xml#L162) | 0.062 / [input L162](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Leg_Foot_Vis_l.xml#L162) |
| sacrum | 0.2 / [input L217](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Torso_Unimanual.xml#L217) | 0.2 / [input L207](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Torso_Unimanual.xml#L207) | 0.2 / [input L207](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Torso_Unimanual.xml#L207) |
| Abdomen | 0.01 / [input L267](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Torso_Unimanual.xml#L267) | 0.01 / [input L256](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Torso_Unimanual.xml#L256) | 0.01 / [input L256](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Torso_Unimanual.xml#L256) |
| lumbar5 | 0.627 / [input L301](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Torso_Unimanual.xml#L301) | 0.627 / [input L289](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Torso_Unimanual.xml#L289) | 0.627 / [input L289](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Torso_Unimanual.xml#L289) |
| lumbar4 | 1.057 / [input L339](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Torso_Unimanual.xml#L339) | 1.057 / [input L324](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Torso_Unimanual.xml#L324) | 1.057 / [input L324](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Torso_Unimanual.xml#L324) |
| lumbar3 | 1.14 / [input L411](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Torso_Unimanual.xml#L411) | 1.14 / [input L393](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Torso_Unimanual.xml#L393) | 1.14 / [input L393](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Torso_Unimanual.xml#L393) |
| lumbar2 | 1.174 / [input L485](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Torso_Unimanual.xml#L485) | 1.174 / [input L464](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Torso_Unimanual.xml#L464) | 1.174 / [input L464](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Torso_Unimanual.xml#L464) |
| lumbar1 | 1.155 / [input L577](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Torso_Unimanual.xml#L577) | 1.155 / [input L553](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Torso_Unimanual.xml#L553) | 1.155 / [input L553](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Torso_Unimanual.xml#L553) |
| thoracic12 | 1.277 / [input L615](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Torso_Unimanual.xml#L615) | 1.277 / [input L590](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Torso_Unimanual.xml#L590) | 1.277 / [input L590](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Torso_Unimanual.xml#L590) |
| thoracic11 | 1.364 / [input L647](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Torso_Unimanual.xml#L647) | 1.364 / [input L621](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Torso_Unimanual.xml#L621) | 1.364 / [input L621](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Torso_Unimanual.xml#L621) |
| thoracic10 | 1.442 / [input L675](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Torso_Unimanual.xml#L675) | 1.442 / [input L648](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Torso_Unimanual.xml#L648) | 1.442 / [input L648](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Torso_Unimanual.xml#L648) |
| thoracic9 | 1.445 / [input L707](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Torso_Unimanual.xml#L707) | 1.445 / [input L679](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Torso_Unimanual.xml#L679) | 1.445 / [input L679](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Torso_Unimanual.xml#L679) |
| thoracic8 | 1.36 / [input L735](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Torso_Unimanual.xml#L735) | 1.36 / [input L706](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Torso_Unimanual.xml#L706) | 1.36 / [input L706](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Torso_Unimanual.xml#L706) |
| thoracic7 | 1.275 / [input L763](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Torso_Unimanual.xml#L763) | 1.275 / [input L733](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Torso_Unimanual.xml#L733) | 1.275 / [input L733](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Torso_Unimanual.xml#L733) |
| thoracic6 | 1.044 / [input L791](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Torso_Unimanual.xml#L791) | 1.044 / [input L760](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Torso_Unimanual.xml#L760) | 1.044 / [input L760](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Torso_Unimanual.xml#L760) |
| thoracic5 | 0.937 / [input L817](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Torso_Unimanual.xml#L817) | 0.937 / [input L785](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Torso_Unimanual.xml#L785) | 0.937 / [input L785](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Torso_Unimanual.xml#L785) |
| thoracic4 | 0.802 / [input L843](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Torso_Unimanual.xml#L843) | 0.802 / [input L810](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Torso_Unimanual.xml#L810) | 0.802 / [input L810](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Torso_Unimanual.xml#L810) |
| thoracic3 | 0.566 / [input L865](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Torso_Unimanual.xml#L865) | 0.566 / [input L831](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Torso_Unimanual.xml#L831) | 0.566 / [input L831](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Torso_Unimanual.xml#L831) |
| thoracic2 | 0.491 / [input L887](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Torso_Unimanual.xml#L887) | 0.491 / [input L852](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Torso_Unimanual.xml#L852) | 0.491 / [input L852](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Torso_Unimanual.xml#L852) |
| thoracic1 | 0.385 / [input L913](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Torso_Unimanual.xml#L913) | 0.385 / [input L877](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Torso_Unimanual.xml#L877) | 0.385 / [input L877](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Torso_Unimanual.xml#L877) |
| sternum | 0.032 / [input L948](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Torso_Unimanual.xml#L948) | 0.032 / [input L910](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Torso_Unimanual.xml#L910) | 0.032 / [input L910](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Torso_Unimanual.xml#L910) |
| clavicle_r | 0.147 / [input L4](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Arm_Hand_r.xml#L4) | 0.147 / [input L3](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Arm_Hand_r.xml#L3) | 0.147 / [input L3](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Arm_Hand_r.xml#L3) |
| clavphant_r | 0.001 / [input L15](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Arm_Hand_r.xml#L15) | 0.001 / [input L14](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Arm_Hand_r.xml#L14) | 0.001 / [input L14](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Arm_Hand_r.xml#L14) |
| scapula_r | 0.432 / [input L20](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Arm_Hand_r.xml#L20) | 0.432 / [input L18](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Arm_Hand_r.xml#L18) | 0.432 / [input L18](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Arm_Hand_r.xml#L18) |
| scapphant_r | 0.001 / [input L94](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Arm_Hand_r.xml#L94) | 0.001 / [input L91](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Arm_Hand_r.xml#L91) | 0.001 / [input L91](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Arm_Hand_r.xml#L91) |
| humphant_r | 0.001 / [input L99](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Arm_Hand_r.xml#L99) | 0.001 / [input L96](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Arm_Hand_r.xml#L96) | 0.001 / [input L96](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Arm_Hand_r.xml#L96) |
| humphant1_r | 0.001 / [input L102](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Arm_Hand_r.xml#L102) | 0.001 / [input L99](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Arm_Hand_r.xml#L99) | 0.001 / [input L99](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Arm_Hand_r.xml#L99) |
| humerus_r | 1.94 / [input L106](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Arm_Hand_r.xml#L106) | 1.94 / [input L103](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Arm_Hand_r.xml#L103) | 1.94 / [input L103](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Arm_Hand_r.xml#L103) |
| ulna_r | 0.563 / [input L253](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Arm_Hand_r.xml#L253) | 0.563 / [input L238](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Arm_Hand_r.xml#L238) | 0.563 / [input L238](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Arm_Hand_r.xml#L238) |
| radius_r | 0.544 / [input L284](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Arm_Hand_r.xml#L284) | 0.544 / [input L267](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Arm_Hand_r.xml#L267) | 0.544 / [input L267](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Arm_Hand_r.xml#L267) |
| proximal_row | 0.00407287984 / [geometry/inference input L350](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Arm_Hand_r.xml#L350) | 0.00407287984 / [geometry/inference input L330](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Arm_Hand_r.xml#L330) | 0.00407287984 / [geometry/inference input L330](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Arm_Hand_r.xml#L330) |
| capitate | 0.00183853621 / [geometry/inference input L402](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Arm_Hand_r.xml#L402) | 0.00183853621 / [geometry/inference input L375](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Arm_Hand_r.xml#L375) | 0.00183853621 / [geometry/inference input L375](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Arm_Hand_r.xml#L375) |
| trapezium | 0.00125660233 / [geometry/inference input L427](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Arm_Hand_r.xml#L427) | 0.00125660233 / [geometry/inference input L400](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Arm_Hand_r.xml#L400) | 0.00125660233 / [geometry/inference input L400](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Arm_Hand_r.xml#L400) |
| firstmc1 | 0.001 / [input L434](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Arm_Hand_r.xml#L434) | 0.001 / [input L407](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Arm_Hand_r.xml#L407) | 0.001 / [input L407](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Arm_Hand_r.xml#L407) |
| firstmc | 0.0190001163 / [geometry/inference input L438](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Arm_Hand_r.xml#L438) | 0.0190001163 / [geometry/inference input L410](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Arm_Hand_r.xml#L410) | 0.0190001163 / [geometry/inference input L410](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Arm_Hand_r.xml#L410) |
| proximal_thumb | 0.012861414 / [geometry/inference input L459](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Arm_Hand_r.xml#L459) | 0.012861414 / [geometry/inference input L428](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Arm_Hand_r.xml#L428) | 0.012861414 / [geometry/inference input L428](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Arm_Hand_r.xml#L428) |
| distal_thumb | 0.00390052757 / [geometry/inference input L477](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Arm_Hand_r.xml#L477) | 0.00390052757 / [geometry/inference input L443](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Arm_Hand_r.xml#L443) | 0.00390052757 / [geometry/inference input L443](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Arm_Hand_r.xml#L443) |
| trapezoid | 0.00077711299 / [geometry/inference input L490](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Arm_Hand_r.xml#L490) | 0.00077711299 / [geometry/inference input L454](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Arm_Hand_r.xml#L454) | 0.00077711299 / [geometry/inference input L454](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Arm_Hand_r.xml#L454) |
| hamate | 0.00132959053 / [geometry/inference input L493](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Arm_Hand_r.xml#L493) | 0.00132959053 / [geometry/inference input L457](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Arm_Hand_r.xml#L457) | 0.00132959053 / [geometry/inference input L457](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Arm_Hand_r.xml#L457) |
| secondmc | 0.0266234797 / [geometry/inference input L498](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Arm_Hand_r.xml#L498) | 0.0266234797 / [geometry/inference input L462](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Arm_Hand_r.xml#L462) | 0.0266234797 / [geometry/inference input L462](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Arm_Hand_r.xml#L462) |
| 2proxph | 0.014393232 / [geometry/inference input L526](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Arm_Hand_r.xml#L526) | 0.014393232 / [geometry/inference input L486](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Arm_Hand_r.xml#L486) | 0.014393232 / [geometry/inference input L486](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Arm_Hand_r.xml#L486) |
| 2midph | 0.00721288768 / [geometry/inference input L557](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Arm_Hand_r.xml#L557) | 0.00721288768 / [geometry/inference input L510](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Arm_Hand_r.xml#L510) | 0.00721288768 / [geometry/inference input L510](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Arm_Hand_r.xml#L510) |
| 2distph | 0.003792145 / [geometry/inference input L576](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Arm_Hand_r.xml#L576) | 0.003792145 / [geometry/inference input L525](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Arm_Hand_r.xml#L525) | 0.003792145 / [geometry/inference input L525](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Arm_Hand_r.xml#L525) |
| thirdmc | 0.0247648464 / [geometry/inference input L589](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Arm_Hand_r.xml#L589) | 0.0247648464 / [geometry/inference input L536](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Arm_Hand_r.xml#L536) | 0.0247648464 / [geometry/inference input L536](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Arm_Hand_r.xml#L536) |
| 3proxph | 0.0155127489 / [geometry/inference input L614](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Arm_Hand_r.xml#L614) | 0.0155127489 / [geometry/inference input L559](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Arm_Hand_r.xml#L559) | 0.0155127489 / [geometry/inference input L559](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Arm_Hand_r.xml#L559) |
| 3midph | 0.00820326943 / [geometry/inference input L635](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Arm_Hand_r.xml#L635) | 0.00820326943 / [geometry/inference input L576](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Arm_Hand_r.xml#L576) | 0.00820326943 / [geometry/inference input L576](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Arm_Hand_r.xml#L576) |
| 3distph | 0.00353210191 / [geometry/inference input L649](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Arm_Hand_r.xml#L649) | 0.00353210191 / [geometry/inference input L587](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Arm_Hand_r.xml#L587) | 0.00353210191 / [geometry/inference input L587](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Arm_Hand_r.xml#L587) |
| fourthmc | 0.0218728933 / [geometry/inference input L661](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Arm_Hand_r.xml#L661) | 0.0218728933 / [geometry/inference input L597](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Arm_Hand_r.xml#L597) | 0.0218728933 / [geometry/inference input L597](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Arm_Hand_r.xml#L597) |
| 4proxph | 0.0129223853 / [geometry/inference input L682](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Arm_Hand_r.xml#L682) | 0.0129223853 / [geometry/inference input L615](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Arm_Hand_r.xml#L615) | 0.0129223853 / [geometry/inference input L615](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Arm_Hand_r.xml#L615) |
| 4midph | 0.00719029855 / [geometry/inference input L703](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Arm_Hand_r.xml#L703) | 0.00719029855 / [geometry/inference input L632](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Arm_Hand_r.xml#L632) | 0.00719029855 / [geometry/inference input L632](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Arm_Hand_r.xml#L632) |
| 4distph | 0.00349118607 / [geometry/inference input L717](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Arm_Hand_r.xml#L717) | 0.00349118607 / [geometry/inference input L643](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Arm_Hand_r.xml#L643) | 0.00349118607 / [geometry/inference input L643](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Arm_Hand_r.xml#L643) |
| fifthmc | 0.0211037328 / [geometry/inference input L728](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Arm_Hand_r.xml#L728) | 0.0211037328 / [geometry/inference input L653](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Arm_Hand_r.xml#L653) | 0.0211037328 / [geometry/inference input L653](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Arm_Hand_r.xml#L653) |
| 5proxph | 0.0104898566 / [geometry/inference input L752](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Arm_Hand_r.xml#L752) | 0.0104898566 / [geometry/inference input L675](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Arm_Hand_r.xml#L675) | 0.0104898566 / [geometry/inference input L675](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Arm_Hand_r.xml#L675) |
| 5midph | 0.00501729243 / [geometry/inference input L777](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Arm_Hand_r.xml#L777) | 0.00501729243 / [geometry/inference input L696](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Arm_Hand_r.xml#L696) | 0.00501729243 / [geometry/inference input L696](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Arm_Hand_r.xml#L696) |
| 5distph | 0.0034391013 / [geometry/inference input L794](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Arm_Hand_r.xml#L794) | 0.0034391013 / [geometry/inference input L710](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Arm_Hand_r.xml#L710) | 0.0034391013 / [geometry/inference input L710](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Arm_Hand_r.xml#L710) |
| clavicle_l | 0.147 / [input L4](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Arm_Hand_Vis_l.xml#L4) | 0.147 / [input L3](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Arm_Hand_Vis_l.xml#L3) | 0.147 / [input L3](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Arm_Hand_Vis_l.xml#L3) |
| clavphant_l | 0.001 / [input L13](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Arm_Hand_Vis_l.xml#L13) | 0.001 / [input L12](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Arm_Hand_Vis_l.xml#L12) | 0.001 / [input L12](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Arm_Hand_Vis_l.xml#L12) |
| scapula_l | 0.432 / [input L16](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Arm_Hand_Vis_l.xml#L16) | 0.432 / [input L14](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Arm_Hand_Vis_l.xml#L14) | 0.432 / [input L14](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Arm_Hand_Vis_l.xml#L14) |
| scapphant_l | 0.001 / [input L87](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Arm_Hand_Vis_l.xml#L87) | 0.001 / [input L84](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Arm_Hand_Vis_l.xml#L84) | 0.001 / [input L84](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Arm_Hand_Vis_l.xml#L84) |
| humphant_l | 0.001 / [input L89](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Arm_Hand_Vis_l.xml#L89) | 0.001 / [input L86](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Arm_Hand_Vis_l.xml#L86) | 0.001 / [input L86](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Arm_Hand_Vis_l.xml#L86) |
| humphant1_l | 0.001 / [input L91](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Arm_Hand_Vis_l.xml#L91) | 0.001 / [input L88](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Arm_Hand_Vis_l.xml#L88) | 0.001 / [input L88](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Arm_Hand_Vis_l.xml#L88) |
| humerus_l | 1.94 / [input L93](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Arm_Hand_Vis_l.xml#L93) | 1.94 / [input L90](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Arm_Hand_Vis_l.xml#L90) | 1.94 / [input L90](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Arm_Hand_Vis_l.xml#L90) |
| ulna_l | 0.563 / [input L238](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Arm_Hand_Vis_l.xml#L238) | 0.563 / [input L224](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Arm_Hand_Vis_l.xml#L224) | 0.563 / [input L224](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Arm_Hand_Vis_l.xml#L224) |
| radius_l | 0.544 / [input L268](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Arm_Hand_Vis_l.xml#L268) | 0.544 / [input L252](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Arm_Hand_Vis_l.xml#L252) | 0.544 / [input L252](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Arm_Hand_Vis_l.xml#L252) |
| proximal_row_l | 0.00407287936 / [geometry/inference input L331](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Arm_Hand_Vis_l.xml#L331) | 0.00407287936 / [geometry/inference input L313](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Arm_Hand_Vis_l.xml#L313) | 0.00407287936 / [geometry/inference input L313](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Arm_Hand_Vis_l.xml#L313) |
| capitate_l | 0.00183853621 / [geometry/inference input L379](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Arm_Hand_Vis_l.xml#L379) | 0.00183853621 / [geometry/inference input L356](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Arm_Hand_Vis_l.xml#L356) | 0.00183853621 / [geometry/inference input L356](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Arm_Hand_Vis_l.xml#L356) |
| trapezium_l | 0.00125660233 / [geometry/inference input L402](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Arm_Hand_Vis_l.xml#L402) | 0.00125660233 / [geometry/inference input L379](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Arm_Hand_Vis_l.xml#L379) | 0.00125660233 / [geometry/inference input L379](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Arm_Hand_Vis_l.xml#L379) |
| firstmc1_l | 0.001 / [input L408](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Arm_Hand_Vis_l.xml#L408) | 0.001 / [input L385](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Arm_Hand_Vis_l.xml#L385) | 0.001 / [input L385](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Arm_Hand_Vis_l.xml#L385) |
| firstmc_l | 0.00354450666 / [geometry/inference input L410](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Arm_Hand_Vis_l.xml#L410) | 0.00354450666 / [geometry/inference input L387](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Arm_Hand_Vis_l.xml#L387) | 0.00354450666 / [geometry/inference input L387](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Arm_Hand_Vis_l.xml#L387) |
| proximal_thumb_l | 0.00157369258 / [geometry/inference input L427](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Arm_Hand_Vis_l.xml#L427) | 0.00157369258 / [geometry/inference input L403](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Arm_Hand_Vis_l.xml#L403) | 0.00157369258 / [geometry/inference input L403](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Arm_Hand_Vis_l.xml#L403) |
| distal_thumb_l | 0.000404290907 / [geometry/inference input L441](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Arm_Hand_Vis_l.xml#L441) | 0.000404290907 / [geometry/inference input L416](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Arm_Hand_Vis_l.xml#L416) | 0.000404290907 / [geometry/inference input L416](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Arm_Hand_Vis_l.xml#L416) |
| trapezoid_l | 0.00077711299 / [geometry/inference input L450](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Arm_Hand_Vis_l.xml#L450) | 0.00077711299 / [geometry/inference input L425](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Arm_Hand_Vis_l.xml#L425) | 0.00077711299 / [geometry/inference input L425](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Arm_Hand_Vis_l.xml#L425) |
| hamate_l | 0.00132959053 / [geometry/inference input L453](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Arm_Hand_Vis_l.xml#L453) | 0.00132959053 / [geometry/inference input L428](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Arm_Hand_Vis_l.xml#L428) | 0.00132959053 / [geometry/inference input L428](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Arm_Hand_Vis_l.xml#L428) |
| secondmc_l | 0.00484177062 / [geometry/inference input L458](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Arm_Hand_Vis_l.xml#L458) | 0.00484177062 / [geometry/inference input L433](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Arm_Hand_Vis_l.xml#L433) | 0.00484177062 / [geometry/inference input L433](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Arm_Hand_Vis_l.xml#L433) |
| 2proxph_l | 0.0021787198 / [geometry/inference input L484](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Arm_Hand_Vis_l.xml#L484) | 0.0021787198 / [geometry/inference input L456](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Arm_Hand_Vis_l.xml#L456) | 0.0021787198 / [geometry/inference input L456](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Arm_Hand_Vis_l.xml#L456) |
| 2midph_l | 0.000644864638 / [geometry/inference input L509](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Arm_Hand_Vis_l.xml#L509) | 0.000644864638 / [geometry/inference input L477](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Arm_Hand_Vis_l.xml#L477) | 0.000644864638 / [geometry/inference input L477](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Arm_Hand_Vis_l.xml#L477) |
| 2distph_l | 0.000200257395 / [geometry/inference input L524](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Arm_Hand_Vis_l.xml#L524) | 0.000200257395 / [geometry/inference input L490](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Arm_Hand_Vis_l.xml#L490) | 0.000200257395 / [geometry/inference input L490](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Arm_Hand_Vis_l.xml#L490) |
| thirdmc_l | 0.00423977437 / [geometry/inference input L533](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Arm_Hand_Vis_l.xml#L533) | 0.00423977437 / [geometry/inference input L499](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Arm_Hand_Vis_l.xml#L499) | 0.00423977437 / [geometry/inference input L499](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Arm_Hand_Vis_l.xml#L499) |
| 3proxph_l | 0.00228036062 / [geometry/inference input L556](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Arm_Hand_Vis_l.xml#L556) | 0.00228036062 / [geometry/inference input L521](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Arm_Hand_Vis_l.xml#L521) | 0.00228036062 / [geometry/inference input L521](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Arm_Hand_Vis_l.xml#L521) |
| 3midph_l | 0.000830998672 / [geometry/inference input L571](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Arm_Hand_Vis_l.xml#L571) | 0.000830998672 / [geometry/inference input L535](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Arm_Hand_Vis_l.xml#L535) | 0.000830998672 / [geometry/inference input L535](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Arm_Hand_Vis_l.xml#L535) |
| 3distph_l | 0.000248090391 / [geometry/inference input L581](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Arm_Hand_Vis_l.xml#L581) | 0.000248090391 / [geometry/inference input L544](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Arm_Hand_Vis_l.xml#L544) | 0.000248090391 / [geometry/inference input L544](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Arm_Hand_Vis_l.xml#L544) |
| fourthmc_l | 0.00323277689 / [geometry/inference input L589](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Arm_Hand_Vis_l.xml#L589) | 0.00323277689 / [geometry/inference input L552](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Arm_Hand_Vis_l.xml#L552) | 0.00323277689 / [geometry/inference input L552](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Arm_Hand_Vis_l.xml#L552) |
| 4proxph_l | 0.00172574904 / [geometry/inference input L606](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Arm_Hand_Vis_l.xml#L606) | 0.00172574904 / [geometry/inference input L568](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Arm_Hand_Vis_l.xml#L568) | 0.00172574904 / [geometry/inference input L568](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Arm_Hand_Vis_l.xml#L568) |
| 4midph_l | 0.000622275504 / [geometry/inference input L621](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Arm_Hand_Vis_l.xml#L621) | 0.000622275504 / [geometry/inference input L582](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Arm_Hand_Vis_l.xml#L582) | 0.000622275504 / [geometry/inference input L582](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Arm_Hand_Vis_l.xml#L582) |
| 4distph_l | 0.000207174551 / [geometry/inference input L631](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Arm_Hand_Vis_l.xml#L631) | 0.000207174551 / [geometry/inference input L591](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Arm_Hand_Vis_l.xml#L591) | 0.000207174551 / [geometry/inference input L591](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Arm_Hand_Vis_l.xml#L591) |
| fifthmc_l | 0.00309193489 / [geometry/inference input L639](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Arm_Hand_Vis_l.xml#L639) | 0.00309193489 / [geometry/inference input L599](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Arm_Hand_Vis_l.xml#L599) | 0.00309193489 / [geometry/inference input L599](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Arm_Hand_Vis_l.xml#L599) |
| 5proxph_l | 0.00132897247 / [geometry/inference input L660](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Arm_Hand_Vis_l.xml#L660) | 0.00132897247 / [geometry/inference input L619](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Arm_Hand_Vis_l.xml#L619) | 0.00132897247 / [geometry/inference input L619](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Arm_Hand_Vis_l.xml#L619) |
| 5midph_l | 0.000459888691 / [geometry/inference input L679](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Arm_Hand_Vis_l.xml#L679) | 0.000459888691 / [geometry/inference input L637](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Arm_Hand_Vis_l.xml#L637) | 0.000459888691 / [geometry/inference input L637](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Arm_Hand_Vis_l.xml#L637) |
| 5distph_l | 0.000155089784 / [geometry/inference input L692](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Arm_Hand_Vis_l.xml#L692) | 0.000155089784 / [geometry/inference input L649](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Arm_Hand_Vis_l.xml#L649) | 0.000155089784 / [geometry/inference input L649](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Arm_Hand_Vis_l.xml#L649) |
| head_neck | 3.664 / [input L971](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Torso_Unimanual.xml#L971) | 3.664 / [input L930](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Torso_Unimanual.xml#L930) | 3.664 / [input L930](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Torso_Unimanual.xml#L930) |
| rib1_R | 0.0125874541 / [geometry/inference input L1062](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Torso_Unimanual.xml#L1062) | 0.0125874541 / [geometry/inference input L1013](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Torso_Unimanual.xml#L1013) | 0.0125874541 / [geometry/inference input L1013](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Torso_Unimanual.xml#L1013) |
| rib1_L | 0.0125880437 / [geometry/inference input L1079](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Torso_Unimanual.xml#L1079) | 0.0125880437 / [geometry/inference input L1029](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Torso_Unimanual.xml#L1029) | 0.0125880437 / [geometry/inference input L1029](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Torso_Unimanual.xml#L1029) |
| rib2_R | 0.0413889961 / [geometry/inference input L1097](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Torso_Unimanual.xml#L1097) | 0.0413889961 / [geometry/inference input L1046](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Torso_Unimanual.xml#L1046) | 0.0413889961 / [geometry/inference input L1046](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Torso_Unimanual.xml#L1046) |
| rib2_L | 0.0413883475 / [geometry/inference input L1126](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Torso_Unimanual.xml#L1126) | 0.0413883475 / [geometry/inference input L1074](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Torso_Unimanual.xml#L1074) | 0.0413883475 / [geometry/inference input L1074](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Torso_Unimanual.xml#L1074) |
| rib3_R | 0.100856241 / [geometry/inference input L1156](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Torso_Unimanual.xml#L1156) | 0.100856241 / [geometry/inference input L1103](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Torso_Unimanual.xml#L1103) | 0.100856241 / [geometry/inference input L1103](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Torso_Unimanual.xml#L1103) |
| rib3_L | 0.100857661 / [geometry/inference input L1185](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Torso_Unimanual.xml#L1185) | 0.100857661 / [geometry/inference input L1131](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Torso_Unimanual.xml#L1131) | 0.100857661 / [geometry/inference input L1131](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Torso_Unimanual.xml#L1131) |
| rib4_R | 0.128835666 / [geometry/inference input L1215](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Torso_Unimanual.xml#L1215) | 0.128835666 / [geometry/inference input L1160](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Torso_Unimanual.xml#L1160) | 0.128835666 / [geometry/inference input L1160](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Torso_Unimanual.xml#L1160) |
| rib4_L | 0.130534027 / [geometry/inference input L1244](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Torso_Unimanual.xml#L1244) | 0.130534027 / [geometry/inference input L1188](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Torso_Unimanual.xml#L1188) | 0.130534027 / [geometry/inference input L1188](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Torso_Unimanual.xml#L1188) |
| rib5_R | 0.181572997 / [geometry/inference input L1274](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Torso_Unimanual.xml#L1274) | 0.181572997 / [geometry/inference input L1217](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Torso_Unimanual.xml#L1217) | 0.181572997 / [geometry/inference input L1217](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Torso_Unimanual.xml#L1217) |
| rib5_L | 0.181933559 / [geometry/inference input L1313](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Torso_Unimanual.xml#L1313) | 0.181933559 / [geometry/inference input L1255](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Torso_Unimanual.xml#L1255) | 0.181933559 / [geometry/inference input L1255](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Torso_Unimanual.xml#L1255) |
| rib6_R | 0.15439328 / [geometry/inference input L1353](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Torso_Unimanual.xml#L1353) | 0.15439328 / [geometry/inference input L1294](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Torso_Unimanual.xml#L1294) | 0.15439328 / [geometry/inference input L1294](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Torso_Unimanual.xml#L1294) |
| rib6_L | 0.154392115 / [geometry/inference input L1400](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Torso_Unimanual.xml#L1400) | 0.154392115 / [geometry/inference input L1340](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Torso_Unimanual.xml#L1340) | 0.154392115 / [geometry/inference input L1340](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Torso_Unimanual.xml#L1340) |
| rib7_R | 0.182215769 / [geometry/inference input L1448](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Torso_Unimanual.xml#L1448) | 0.182215769 / [geometry/inference input L1387](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Torso_Unimanual.xml#L1387) | 0.182215769 / [geometry/inference input L1387](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Torso_Unimanual.xml#L1387) |
| rib7_L | 0.182223787 / [geometry/inference input L1498](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Torso_Unimanual.xml#L1498) | 0.182223787 / [geometry/inference input L1436](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Torso_Unimanual.xml#L1436) | 0.182223787 / [geometry/inference input L1436](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Torso_Unimanual.xml#L1436) |
| rib8_R | 0.13463873 / [geometry/inference input L1549](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Torso_Unimanual.xml#L1549) | 0.13463873 / [geometry/inference input L1486](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Torso_Unimanual.xml#L1486) | 0.13463873 / [geometry/inference input L1486](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Torso_Unimanual.xml#L1486) |
| rib8_L | 0.134638701 / [geometry/inference input L1603](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Torso_Unimanual.xml#L1603) | 0.134638701 / [geometry/inference input L1539](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Torso_Unimanual.xml#L1539) | 0.134638701 / [geometry/inference input L1539](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Torso_Unimanual.xml#L1539) |
| rib9_R | 0.139182739 / [geometry/inference input L1658](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Torso_Unimanual.xml#L1658) | 0.139182739 / [geometry/inference input L1593](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Torso_Unimanual.xml#L1593) | 0.139182739 / [geometry/inference input L1593](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Torso_Unimanual.xml#L1593) |
| rib9_L | 0.139365867 / [geometry/inference input L1711](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Torso_Unimanual.xml#L1711) | 0.139365867 / [geometry/inference input L1645](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Torso_Unimanual.xml#L1645) | 0.139365867 / [geometry/inference input L1645](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Torso_Unimanual.xml#L1645) |
| rib10_R | 0.0815638614 / [geometry/inference input L1765](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Torso_Unimanual.xml#L1765) | 0.0815638614 / [geometry/inference input L1698](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Torso_Unimanual.xml#L1698) | 0.0815638614 / [geometry/inference input L1698](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Torso_Unimanual.xml#L1698) |
| rib10_L | 0.0815764924 / [geometry/inference input L1806](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Torso_Unimanual.xml#L1806) | 0.0815764924 / [geometry/inference input L1738](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Torso_Unimanual.xml#L1738) | 0.0815764924 / [geometry/inference input L1738](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Torso_Unimanual.xml#L1738) |
| rib11_R | 0.0401365508 / [geometry/inference input L1847](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Torso_Unimanual.xml#L1847) | 0.0401365508 / [geometry/inference input L1779](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Torso_Unimanual.xml#L1779) | 0.0401365508 / [geometry/inference input L1779](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Torso_Unimanual.xml#L1779) |
| rib11_L | 0.0401364281 / [geometry/inference input L1873](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Torso_Unimanual.xml#L1873) | 0.0401364281 / [geometry/inference input L1804](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Torso_Unimanual.xml#L1804) | 0.0401364281 / [geometry/inference input L1804](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Torso_Unimanual.xml#L1804) |
| rib12_R | 0.0137579267 / [geometry/inference input L1900](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Torso_Unimanual.xml#L1900) | 0.0137579267 / [geometry/inference input L1830](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Torso_Unimanual.xml#L1830) | 0.0137579267 / [geometry/inference input L1830](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Torso_Unimanual.xml#L1830) |
| rib12_L | 0.0137578208 / [geometry/inference input L1927](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Torso_Unimanual.xml#L1927) | 0.0137578208 / [geometry/inference input L1856](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Torso_Unimanual.xml#L1856) | 0.0137578208 / [geometry/inference input L1856](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Torso_Unimanual.xml#L1856) |
| waterbottle | 0.537983178 / [geometry/inference input L2](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Waterbottle.xml#L2) | 0.537983178 / [geometry/inference input L20](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Waterbottle.xml#L20) | 0.537983178 / [geometry/inference input L20](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Waterbottle.xml#L20) |
| target | 0.264298857 / [geometry/inference input L17](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/assets/body_manipulation/Body_Waterbottle.xml#L17) | 0.264298857 / [geometry/inference input L35](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/Body_Manipulation/Body_Waterbottle.xml#L35) | 0.264298857 / [geometry/inference input L35](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/Body_Manipulation/Body_Waterbottle.xml#L35) |
| table | 49.4722817 / [geometry/inference input L62](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/ms_human_700/MS-Human-700-Manipulation.xml#L62) | 49.4722817 / [geometry/inference input L72](https://github.com/LNSGroup/MS-Human-700/blob/4b86de9d0e0ac7f91ac30124db22f1c8e4c7553d/MS-Human-700-Manipulation.xml#L72) | 49.4722817 / [geometry/inference input L72](https://github.com/LNSGroup/MS-Human-700/blob/2d686957aefd5739cf4d2859a6acfd94c8f84400/MS-Human-700-Manipulation.xml#L72) |

## Coverage and unmatched elements

```json
{
  "mapping_h": {
    "bodies": {
      "pelvis": "pelvis",
      "femur_r": "femur_r",
      "tibia_r": "tibia_r",
      "talus_r": "talus_r",
      "calcn_r": "calcn_r",
      "toes_r": "toes_r",
      "patella_r": "patella_r",
      "femur_l": "femur_l",
      "tibia_l": "tibia_l",
      "talus_l": "talus_l",
      "calcn_l": "calcn_l",
      "toes_l": "toes_l",
      "patella_l": "patella_l",
      "sacrum": "sacrum",
      "Abdomen": "Abdomen",
      "lumbar5": "lumbar5",
      "lumbar4": "lumbar4",
      "lumbar3": "lumbar3",
      "lumbar2": "lumbar2",
      "lumbar1": "lumbar1",
      "thoracic12": "thoracic12",
      "thoracic11": "thoracic11",
      "thoracic10": "thoracic10",
      "thoracic9": "thoracic9",
      "thoracic8": "thoracic8",
      "thoracic7": "thoracic7",
      "thoracic6": "thoracic6",
      "thoracic5": "thoracic5",
      "thoracic4": "thoracic4",
      "thoracic3": "thoracic3",
      "thoracic2": "thoracic2",
      "thoracic1": "thoracic1",
      "sternum": "sternum",
      "clavicle_r": "clavicle_r",
      "clavphant_r": "clavphant_r",
      "scapula_r": "scapula_r",
      "scapphant_r": "scapphant_r",
      "humphant_r": "humphant_r",
      "humphant1_r": "humphant1_r",
      "humerus_r": "humerus_r",
      "ulna_r": "ulna_r",
      "radius_r": "radius_r",
      "proximal_row": "proximal_row",
      "capitate": "capitate",
      "trapezium": "trapezium",
      "firstmc1": "firstmc1",
      "firstmc": "firstmc",
      "proximal_thumb": "proximal_thumb",
      "distal_thumb": "distal_thumb",
      "trapezoid": "trapezoid",
      "hamate": "hamate",
      "secondmc": "secondmc",
      "2proxph": "2proxph",
      "2midph": "2midph",
      "2distph": "2distph",
      "thirdmc": "thirdmc",
      "3proxph": "3proxph",
      "3midph": "3midph",
      "3distph": "3distph",
      "fourthmc": "fourthmc",
      "4proxph": "4proxph",
      "4midph": "4midph",
      "4distph": "4distph",
      "fifthmc": "fifthmc",
      "5proxph": "5proxph",
      "5midph": "5midph",
      "5distph": "5distph",
      "clavicle_l": "clavicle_l",
      "clavphant_l": "clavphant_l",
      "scapula_l": "scapula_l",
      "scapphant_l": "scapphant_l",
      "humphant_l": "humphant_l",
      "humphant1_l": "humphant1_l",
      "humerus_l": "humerus_l",
      "ulna_l": "ulna_l",
      "radius_l": "radius_l",
      "proximal_row_l": "proximal_row_l",
      "capitate_l": "capitate_l",
      "trapezium_l": "trapezium_l",
      "firstmc1_l": "firstmc1_l",
      "firstmc_l": "firstmc_l",
      "proximal_thumb_l": "proximal_thumb_l",
      "distal_thumb_l": "distal_thumb_l",
      "trapezoid_l": "trapezoid_l",
      "hamate_l": "hamate_l",
      "secondmc_l": "secondmc_l",
      "2proxph_l": "2proxph_l",
      "2midph_l": "2midph_l",
      "2distph_l": "2distph_l",
      "thirdmc_l": "thirdmc_l",
      "3proxph_l": "3proxph_l",
      "3midph_l": "3midph_l",
      "3distph_l": "3distph_l",
      "fourthmc_l": "fourthmc_l",
      "4proxph_l": "4proxph_l",
      "4midph_l": "4midph_l",
      "4distph_l": "4distph_l",
      "fifthmc_l": "fifthmc_l",
      "5proxph_l": "5proxph_l",
      "5midph_l": "5midph_l",
      "5distph_l": "5distph_l",
      "head_neck": "head_neck",
      "rib1_R": "rib1_R",
      "rib1_L": "rib1_L",
      "rib2_R": "rib2_R",
      "rib2_L": "rib2_L",
      "rib3_R": "rib3_R",
      "rib3_L": "rib3_L",
      "rib4_R": "rib4_R",
      "rib4_L": "rib4_L",
      "rib5_R": "rib5_R",
      "rib5_L": "rib5_L",
      "rib6_R": "rib6_R",
      "rib6_L": "rib6_L",
      "rib7_R": "rib7_R",
      "rib7_L": "rib7_L",
      "rib8_R": "rib8_R",
      "rib8_L": "rib8_L",
      "rib9_R": "rib9_R",
      "rib9_L": "rib9_L",
      "rib10_R": "rib10_R",
      "rib10_L": "rib10_L",
      "rib11_R": "rib11_R",
      "rib11_L": "rib11_L",
      "rib12_R": "rib12_R",
      "rib12_L": "rib12_L",
      "waterbottle": "waterbottle",
      "target": "target",
      "table": "table"
    },
    "joints": {
      "sternoclavicular_r2_r": "sternoclavicular_r2_r",
      "sternoclavicular_r3_r": "sternoclavicular_r3_r",
      "unrotscap_r3_r": "unrotscap_r3_r",
      "unrotscap_r2_r": "unrotscap_r2_r",
      "acromioclavicular_r2_r": "acromioclavicular_r2_r",
      "acromioclavicular_r3_r": "acromioclavicular_r3_r",
      "acromioclavicular_r1_r": "acromioclavicular_r1_r",
      "unrothum_r1_r": "unrothum_r1_r",
      "unrothum_r3_r": "unrothum_r3_r",
      "unrothum_r2_r": "unrothum_r2_r",
      "elv_angle_r": "elv_angle_r",
      "shoulder_elv_r": "shoulder_elv_r",
      "shoulder1_r2_r": "shoulder1_r2_r",
      "shoulder_rot_r": "shoulder_rot_r",
      "elbow_flexion_r": "elbow_flexion_r",
      "pro_sup_r": "pro_sup_r",
      "deviation_r": "deviation_r",
      "flexion_r": "flexion_r",
      "wrist_hand_r1_r": "wrist_hand_r1_r",
      "wrist_hand_r3_r": "wrist_hand_r3_r",
      "cmc_flexion": "cmc_flexion",
      "cmc_abduction": "cmc_abduction",
      "mp_flexion": "mp_flexion",
      "ip_flexion": "ip_flexion",
      "2mcp_abduction": "2mcp_abduction",
      "2mcp_flexion": "2mcp_flexion",
      "2pm_flexion": "2pm_flexion",
      "2md_flexion": "2md_flexion",
      "3mcp_abduction": "3mcp_abduction",
      "3mcp_flexion": "3mcp_flexion",
      "3pm_flexion": "3pm_flexion",
      "3md_flexion": "3md_flexion",
      "4cmc_flexion": "4cmc_flexion",
      "4mcp_abduction": "4mcp_abduction",
      "4mcp_flexion": "4mcp_flexion",
      "4pm_flexion": "4pm_flexion",
      "4md_flexion": "4md_flexion",
      "CMC5_r1": "CMC5_r1",
      "5mcp_abduction": "5mcp_abduction",
      "5mcp_flexion": "5mcp_flexion",
      "5pm_flexion": "5pm_flexion",
      "5md_flexion": "5md_flexion",
      "objTx": "objTx",
      "objTy": "objTy",
      "objTz": "objTz",
      "objRx": "objRx",
      "objRy": "objRy",
      "objRz": "objRz"
    },
    "body_methods": {
      "pelvis": "name",
      "femur_r": "name",
      "tibia_r": "name",
      "talus_r": "name",
      "calcn_r": "name",
      "toes_r": "name",
      "patella_r": "name",
      "femur_l": "name",
      "tibia_l": "name",
      "talus_l": "name",
      "calcn_l": "name",
      "toes_l": "name",
      "patella_l": "name",
      "sacrum": "name",
      "Abdomen": "name",
      "lumbar5": "name",
      "lumbar4": "name",
      "lumbar3": "name",
      "lumbar2": "name",
      "lumbar1": "name",
      "thoracic12": "name",
      "thoracic11": "name",
      "thoracic10": "name",
      "thoracic9": "name",
      "thoracic8": "name",
      "thoracic7": "name",
      "thoracic6": "name",
      "thoracic5": "name",
      "thoracic4": "name",
      "thoracic3": "name",
      "thoracic2": "name",
      "thoracic1": "name",
      "sternum": "name",
      "clavicle_r": "name",
      "clavphant_r": "name",
      "scapula_r": "name",
      "scapphant_r": "name",
      "humphant_r": "name",
      "humphant1_r": "name",
      "humerus_r": "name",
      "ulna_r": "name",
      "radius_r": "name",
      "proximal_row": "name",
      "capitate": "name",
      "trapezium": "name",
      "firstmc1": "name",
      "firstmc": "name",
      "proximal_thumb": "name",
      "distal_thumb": "name",
      "trapezoid": "name",
      "hamate": "name",
      "secondmc": "name",
      "2proxph": "name",
      "2midph": "name",
      "2distph": "name",
      "thirdmc": "name",
      "3proxph": "name",
      "3midph": "name",
      "3distph": "name",
      "fourthmc": "name",
      "4proxph": "name",
      "4midph": "name",
      "4distph": "name",
      "fifthmc": "name",
      "5proxph": "name",
      "5midph": "name",
      "5distph": "name",
      "clavicle_l": "name",
      "clavphant_l": "name",
      "scapula_l": "name",
      "scapphant_l": "name",
      "humphant_l": "name",
      "humphant1_l": "name",
      "humerus_l": "name",
      "ulna_l": "name",
      "radius_l": "name",
      "proximal_row_l": "name",
      "capitate_l": "name",
      "trapezium_l": "name",
      "firstmc1_l": "name",
      "firstmc_l": "name",
      "proximal_thumb_l": "name",
      "distal_thumb_l": "name",
      "trapezoid_l": "name",
      "hamate_l": "name",
      "secondmc_l": "name",
      "2proxph_l": "name",
      "2midph_l": "name",
      "2distph_l": "name",
      "thirdmc_l": "name",
      "3proxph_l": "name",
      "3midph_l": "name",
      "3distph_l": "name",
      "fourthmc_l": "name",
      "4proxph_l": "name",
      "4midph_l": "name",
      "4distph_l": "name",
      "fifthmc_l": "name",
      "5proxph_l": "name",
      "5midph_l": "name",
      "5distph_l": "name",
      "head_neck": "name",
      "rib1_R": "name",
      "rib1_L": "name",
      "rib2_R": "name",
      "rib2_L": "name",
      "rib3_R": "name",
      "rib3_L": "name",
      "rib4_R": "name",
      "rib4_L": "name",
      "rib5_R": "name",
      "rib5_L": "name",
      "rib6_R": "name",
      "rib6_L": "name",
      "rib7_R": "name",
      "rib7_L": "name",
      "rib8_R": "name",
      "rib8_L": "name",
      "rib9_R": "name",
      "rib9_L": "name",
      "rib10_R": "name",
      "rib10_L": "name",
      "rib11_R": "name",
      "rib11_L": "name",
      "rib12_R": "name",
      "rib12_L": "name",
      "waterbottle": "name",
      "target": "name",
      "table": "name"
    },
    "joint_methods": {
      "sternoclavicular_r2_r": "name",
      "sternoclavicular_r3_r": "name",
      "unrotscap_r3_r": "name",
      "unrotscap_r2_r": "name",
      "acromioclavicular_r2_r": "name",
      "acromioclavicular_r3_r": "name",
      "acromioclavicular_r1_r": "name",
      "unrothum_r1_r": "name",
      "unrothum_r3_r": "name",
      "unrothum_r2_r": "name",
      "elv_angle_r": "name",
      "shoulder_elv_r": "name",
      "shoulder1_r2_r": "name",
      "shoulder_rot_r": "name",
      "elbow_flexion_r": "name",
      "pro_sup_r": "name",
      "deviation_r": "name",
      "flexion_r": "name",
      "wrist_hand_r1_r": "name",
      "wrist_hand_r3_r": "name",
      "cmc_flexion": "name",
      "cmc_abduction": "name",
      "mp_flexion": "name",
      "ip_flexion": "name",
      "2mcp_abduction": "name",
      "2mcp_flexion": "name",
      "2pm_flexion": "name",
      "2md_flexion": "name",
      "3mcp_abduction": "name",
      "3mcp_flexion": "name",
      "3pm_flexion": "name",
      "3md_flexion": "name",
      "4cmc_flexion": "name",
      "4mcp_abduction": "name",
      "4mcp_flexion": "name",
      "4pm_flexion": "name",
      "4md_flexion": "name",
      "CMC5_r1": "name",
      "5mcp_abduction": "name",
      "5mcp_flexion": "name",
      "5pm_flexion": "name",
      "5md_flexion": "name",
      "objTx": "name",
      "objTy": "name",
      "objTz": "name",
      "objRx": "name",
      "objRy": "name",
      "objRz": "name"
    },
    "unmatched_m_bodies": [],
    "unmatched_upstream_bodies": [],
    "unmatched_m_joints": [],
    "unmatched_upstream_joints": [],
    "registration_anchor": {
      "M": "pelvis",
      "H": "pelvis",
      "root_unmatched": false
    }
  },
  "mapping_s": {
    "bodies": {
      "pelvis": "pelvis",
      "femur_r": "femur_r",
      "tibia_r": "tibia_r",
      "talus_r": "talus_r",
      "calcn_r": "calcn_r",
      "toes_r": "toes_r",
      "patella_r": "patella_r",
      "femur_l": "femur_l",
      "tibia_l": "tibia_l",
      "talus_l": "talus_l",
      "calcn_l": "calcn_l",
      "toes_l": "toes_l",
      "patella_l": "patella_l",
      "sacrum": "sacrum",
      "Abdomen": "Abdomen",
      "lumbar5": "lumbar5",
      "lumbar4": "lumbar4",
      "lumbar3": "lumbar3",
      "lumbar2": "lumbar2",
      "lumbar1": "lumbar1",
      "thoracic12": "thoracic12",
      "thoracic11": "thoracic11",
      "thoracic10": "thoracic10",
      "thoracic9": "thoracic9",
      "thoracic8": "thoracic8",
      "thoracic7": "thoracic7",
      "thoracic6": "thoracic6",
      "thoracic5": "thoracic5",
      "thoracic4": "thoracic4",
      "thoracic3": "thoracic3",
      "thoracic2": "thoracic2",
      "thoracic1": "thoracic1",
      "sternum": "sternum",
      "clavicle_r": "clavicle_r",
      "clavphant_r": "clavphant_r",
      "scapula_r": "scapula_r",
      "scapphant_r": "scapphant_r",
      "humphant_r": "humphant_r",
      "humphant1_r": "humphant1_r",
      "humerus_r": "humerus_r",
      "ulna_r": "ulna_r",
      "radius_r": "radius_r",
      "proximal_row": "proximal_row",
      "capitate": "capitate",
      "trapezium": "trapezium",
      "firstmc1": "firstmc1",
      "firstmc": "firstmc",
      "proximal_thumb": "proximal_thumb",
      "distal_thumb": "distal_thumb",
      "trapezoid": "trapezoid",
      "hamate": "hamate",
      "secondmc": "secondmc",
      "2proxph": "2proxph",
      "2midph": "2midph",
      "2distph": "2distph",
      "thirdmc": "thirdmc",
      "3proxph": "3proxph",
      "3midph": "3midph",
      "3distph": "3distph",
      "fourthmc": "fourthmc",
      "4proxph": "4proxph",
      "4midph": "4midph",
      "4distph": "4distph",
      "fifthmc": "fifthmc",
      "5proxph": "5proxph",
      "5midph": "5midph",
      "5distph": "5distph",
      "clavicle_l": "clavicle_l",
      "clavphant_l": "clavphant_l",
      "scapula_l": "scapula_l",
      "scapphant_l": "scapphant_l",
      "humphant_l": "humphant_l",
      "humphant1_l": "humphant1_l",
      "humerus_l": "humerus_l",
      "ulna_l": "ulna_l",
      "radius_l": "radius_l",
      "proximal_row_l": "proximal_row_l",
      "capitate_l": "capitate_l",
      "trapezium_l": "trapezium_l",
      "firstmc1_l": "firstmc1_l",
      "firstmc_l": "firstmc_l",
      "proximal_thumb_l": "proximal_thumb_l",
      "distal_thumb_l": "distal_thumb_l",
      "trapezoid_l": "trapezoid_l",
      "hamate_l": "hamate_l",
      "secondmc_l": "secondmc_l",
      "2proxph_l": "2proxph_l",
      "2midph_l": "2midph_l",
      "2distph_l": "2distph_l",
      "thirdmc_l": "thirdmc_l",
      "3proxph_l": "3proxph_l",
      "3midph_l": "3midph_l",
      "3distph_l": "3distph_l",
      "fourthmc_l": "fourthmc_l",
      "4proxph_l": "4proxph_l",
      "4midph_l": "4midph_l",
      "4distph_l": "4distph_l",
      "fifthmc_l": "fifthmc_l",
      "5proxph_l": "5proxph_l",
      "5midph_l": "5midph_l",
      "5distph_l": "5distph_l",
      "head_neck": "head_neck",
      "rib1_R": "rib1_R",
      "rib1_L": "rib1_L",
      "rib2_R": "rib2_R",
      "rib2_L": "rib2_L",
      "rib3_R": "rib3_R",
      "rib3_L": "rib3_L",
      "rib4_R": "rib4_R",
      "rib4_L": "rib4_L",
      "rib5_R": "rib5_R",
      "rib5_L": "rib5_L",
      "rib6_R": "rib6_R",
      "rib6_L": "rib6_L",
      "rib7_R": "rib7_R",
      "rib7_L": "rib7_L",
      "rib8_R": "rib8_R",
      "rib8_L": "rib8_L",
      "rib9_R": "rib9_R",
      "rib9_L": "rib9_L",
      "rib10_R": "rib10_R",
      "rib10_L": "rib10_L",
      "rib11_R": "rib11_R",
      "rib11_L": "rib11_L",
      "rib12_R": "rib12_R",
      "rib12_L": "rib12_L",
      "waterbottle": "waterbottle",
      "target": "target",
      "table": "table"
    },
    "joints": {
      "sternoclavicular_r2_r": "sternoclavicular_r2_r",
      "sternoclavicular_r3_r": "sternoclavicular_r3_r",
      "unrotscap_r3_r": "unrotscap_r3_r",
      "unrotscap_r2_r": "unrotscap_r2_r",
      "acromioclavicular_r2_r": "acromioclavicular_r2_r",
      "acromioclavicular_r3_r": "acromioclavicular_r3_r",
      "acromioclavicular_r1_r": "acromioclavicular_r1_r",
      "unrothum_r1_r": "unrothum_r1_r",
      "unrothum_r3_r": "unrothum_r3_r",
      "unrothum_r2_r": "unrothum_r2_r",
      "elv_angle_r": "elv_angle_r",
      "shoulder_elv_r": "shoulder_elv_r",
      "shoulder1_r2_r": "shoulder1_r2_r",
      "shoulder_rot_r": "shoulder_rot_r",
      "elbow_flexion_r": "elbow_flexion_r",
      "pro_sup_r": "pro_sup_r",
      "deviation_r": "deviation_r",
      "flexion_r": "flexion_r",
      "wrist_hand_r1_r": "wrist_hand_r1_r",
      "wrist_hand_r3_r": "wrist_hand_r3_r",
      "cmc_flexion": "cmc_flexion",
      "cmc_abduction": "cmc_abduction",
      "mp_flexion": "mp_flexion",
      "ip_flexion": "ip_flexion",
      "2mcp_abduction": "2mcp_abduction",
      "2mcp_flexion": "2mcp_flexion",
      "2pm_flexion": "2pm_flexion",
      "2md_flexion": "2md_flexion",
      "3mcp_abduction": "3mcp_abduction",
      "3mcp_flexion": "3mcp_flexion",
      "3pm_flexion": "3pm_flexion",
      "3md_flexion": "3md_flexion",
      "4cmc_flexion": "4cmc_flexion",
      "4mcp_abduction": "4mcp_abduction",
      "4mcp_flexion": "4mcp_flexion",
      "4pm_flexion": "4pm_flexion",
      "4md_flexion": "4md_flexion",
      "CMC5_r1": "CMC5_r1",
      "5mcp_abduction": "5mcp_abduction",
      "5mcp_flexion": "5mcp_flexion",
      "5pm_flexion": "5pm_flexion",
      "5md_flexion": "5md_flexion",
      "objTx": "objTx",
      "objTy": "objTy",
      "objTz": "objTz",
      "objRx": "objRx",
      "objRy": "objRy",
      "objRz": "objRz"
    },
    "body_methods": {
      "pelvis": "name",
      "femur_r": "name",
      "tibia_r": "name",
      "talus_r": "name",
      "calcn_r": "name",
      "toes_r": "name",
      "patella_r": "name",
      "femur_l": "name",
      "tibia_l": "name",
      "talus_l": "name",
      "calcn_l": "name",
      "toes_l": "name",
      "patella_l": "name",
      "sacrum": "name",
      "Abdomen": "name",
      "lumbar5": "name",
      "lumbar4": "name",
      "lumbar3": "name",
      "lumbar2": "name",
      "lumbar1": "name",
      "thoracic12": "name",
      "thoracic11": "name",
      "thoracic10": "name",
      "thoracic9": "name",
      "thoracic8": "name",
      "thoracic7": "name",
      "thoracic6": "name",
      "thoracic5": "name",
      "thoracic4": "name",
      "thoracic3": "name",
      "thoracic2": "name",
      "thoracic1": "name",
      "sternum": "name",
      "clavicle_r": "name",
      "clavphant_r": "name",
      "scapula_r": "name",
      "scapphant_r": "name",
      "humphant_r": "name",
      "humphant1_r": "name",
      "humerus_r": "name",
      "ulna_r": "name",
      "radius_r": "name",
      "proximal_row": "name",
      "capitate": "name",
      "trapezium": "name",
      "firstmc1": "name",
      "firstmc": "name",
      "proximal_thumb": "name",
      "distal_thumb": "name",
      "trapezoid": "name",
      "hamate": "name",
      "secondmc": "name",
      "2proxph": "name",
      "2midph": "name",
      "2distph": "name",
      "thirdmc": "name",
      "3proxph": "name",
      "3midph": "name",
      "3distph": "name",
      "fourthmc": "name",
      "4proxph": "name",
      "4midph": "name",
      "4distph": "name",
      "fifthmc": "name",
      "5proxph": "name",
      "5midph": "name",
      "5distph": "name",
      "clavicle_l": "name",
      "clavphant_l": "name",
      "scapula_l": "name",
      "scapphant_l": "name",
      "humphant_l": "name",
      "humphant1_l": "name",
      "humerus_l": "name",
      "ulna_l": "name",
      "radius_l": "name",
      "proximal_row_l": "name",
      "capitate_l": "name",
      "trapezium_l": "name",
      "firstmc1_l": "name",
      "firstmc_l": "name",
      "proximal_thumb_l": "name",
      "distal_thumb_l": "name",
      "trapezoid_l": "name",
      "hamate_l": "name",
      "secondmc_l": "name",
      "2proxph_l": "name",
      "2midph_l": "name",
      "2distph_l": "name",
      "thirdmc_l": "name",
      "3proxph_l": "name",
      "3midph_l": "name",
      "3distph_l": "name",
      "fourthmc_l": "name",
      "4proxph_l": "name",
      "4midph_l": "name",
      "4distph_l": "name",
      "fifthmc_l": "name",
      "5proxph_l": "name",
      "5midph_l": "name",
      "5distph_l": "name",
      "head_neck": "name",
      "rib1_R": "name",
      "rib1_L": "name",
      "rib2_R": "name",
      "rib2_L": "name",
      "rib3_R": "name",
      "rib3_L": "name",
      "rib4_R": "name",
      "rib4_L": "name",
      "rib5_R": "name",
      "rib5_L": "name",
      "rib6_R": "name",
      "rib6_L": "name",
      "rib7_R": "name",
      "rib7_L": "name",
      "rib8_R": "name",
      "rib8_L": "name",
      "rib9_R": "name",
      "rib9_L": "name",
      "rib10_R": "name",
      "rib10_L": "name",
      "rib11_R": "name",
      "rib11_L": "name",
      "rib12_R": "name",
      "rib12_L": "name",
      "waterbottle": "name",
      "target": "name",
      "table": "name"
    },
    "joint_methods": {
      "sternoclavicular_r2_r": "name",
      "sternoclavicular_r3_r": "name",
      "unrotscap_r3_r": "name",
      "unrotscap_r2_r": "name",
      "acromioclavicular_r2_r": "name",
      "acromioclavicular_r3_r": "name",
      "acromioclavicular_r1_r": "name",
      "unrothum_r1_r": "name",
      "unrothum_r3_r": "name",
      "unrothum_r2_r": "name",
      "elv_angle_r": "name",
      "shoulder_elv_r": "name",
      "shoulder1_r2_r": "name",
      "shoulder_rot_r": "name",
      "elbow_flexion_r": "name",
      "pro_sup_r": "name",
      "deviation_r": "name",
      "flexion_r": "name",
      "wrist_hand_r1_r": "name",
      "wrist_hand_r3_r": "name",
      "cmc_flexion": "name",
      "cmc_abduction": "name",
      "mp_flexion": "name",
      "ip_flexion": "name",
      "2mcp_abduction": "name",
      "2mcp_flexion": "name",
      "2pm_flexion": "name",
      "2md_flexion": "name",
      "3mcp_abduction": "name",
      "3mcp_flexion": "name",
      "3pm_flexion": "name",
      "3md_flexion": "name",
      "4cmc_flexion": "name",
      "4mcp_abduction": "name",
      "4mcp_flexion": "name",
      "4pm_flexion": "name",
      "4md_flexion": "name",
      "CMC5_r1": "name",
      "5mcp_abduction": "name",
      "5mcp_flexion": "name",
      "5pm_flexion": "name",
      "5md_flexion": "name",
      "objTx": "name",
      "objTy": "name",
      "objTz": "name",
      "objRx": "name",
      "objRy": "name",
      "objRz": "name"
    },
    "unmatched_m_bodies": [],
    "unmatched_upstream_bodies": [],
    "unmatched_m_joints": [],
    "unmatched_upstream_joints": [],
    "registration_anchor": {
      "M": "pelvis",
      "S": "pelvis"
    }
  },
  "unavailable": [
    {
      "entity": "sternoclavicular_r2_r",
      "other_entity": "sternoclavicular_r2_r",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "sternoclavicular_r2_r",
      "other_entity": "sternoclavicular_r2_r",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "sternoclavicular_r2_r",
      "other_entity": "sternoclavicular_r2_r",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "sternoclavicular_r3_r",
      "other_entity": "sternoclavicular_r3_r",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "sternoclavicular_r3_r",
      "other_entity": "sternoclavicular_r3_r",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "sternoclavicular_r3_r",
      "other_entity": "sternoclavicular_r3_r",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "unrotscap_r3_r",
      "other_entity": "unrotscap_r3_r",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "unrotscap_r3_r",
      "other_entity": "unrotscap_r3_r",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "unrotscap_r3_r",
      "other_entity": "unrotscap_r3_r",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "unrotscap_r2_r",
      "other_entity": "unrotscap_r2_r",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "unrotscap_r2_r",
      "other_entity": "unrotscap_r2_r",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "unrotscap_r2_r",
      "other_entity": "unrotscap_r2_r",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "acromioclavicular_r2_r",
      "other_entity": "acromioclavicular_r2_r",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "acromioclavicular_r2_r",
      "other_entity": "acromioclavicular_r2_r",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "acromioclavicular_r2_r",
      "other_entity": "acromioclavicular_r2_r",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "acromioclavicular_r3_r",
      "other_entity": "acromioclavicular_r3_r",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "acromioclavicular_r3_r",
      "other_entity": "acromioclavicular_r3_r",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "acromioclavicular_r3_r",
      "other_entity": "acromioclavicular_r3_r",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "acromioclavicular_r1_r",
      "other_entity": "acromioclavicular_r1_r",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "acromioclavicular_r1_r",
      "other_entity": "acromioclavicular_r1_r",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "acromioclavicular_r1_r",
      "other_entity": "acromioclavicular_r1_r",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "unrothum_r1_r",
      "other_entity": "unrothum_r1_r",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "unrothum_r1_r",
      "other_entity": "unrothum_r1_r",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "unrothum_r1_r",
      "other_entity": "unrothum_r1_r",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "unrothum_r3_r",
      "other_entity": "unrothum_r3_r",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "unrothum_r3_r",
      "other_entity": "unrothum_r3_r",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "unrothum_r3_r",
      "other_entity": "unrothum_r3_r",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "unrothum_r2_r",
      "other_entity": "unrothum_r2_r",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "unrothum_r2_r",
      "other_entity": "unrothum_r2_r",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "unrothum_r2_r",
      "other_entity": "unrothum_r2_r",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "elv_angle_r",
      "other_entity": "elv_angle_r",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "elv_angle_r",
      "other_entity": "elv_angle_r",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "elv_angle_r",
      "other_entity": "elv_angle_r",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "shoulder_elv_r",
      "other_entity": "shoulder_elv_r",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "shoulder_elv_r",
      "other_entity": "shoulder_elv_r",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "shoulder_elv_r",
      "other_entity": "shoulder_elv_r",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "shoulder1_r2_r",
      "other_entity": "shoulder1_r2_r",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "shoulder1_r2_r",
      "other_entity": "shoulder1_r2_r",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "shoulder1_r2_r",
      "other_entity": "shoulder1_r2_r",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "shoulder_rot_r",
      "other_entity": "shoulder_rot_r",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "shoulder_rot_r",
      "other_entity": "shoulder_rot_r",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "shoulder_rot_r",
      "other_entity": "shoulder_rot_r",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "elbow_flexion_r",
      "other_entity": "elbow_flexion_r",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "elbow_flexion_r",
      "other_entity": "elbow_flexion_r",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "elbow_flexion_r",
      "other_entity": "elbow_flexion_r",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "pro_sup_r",
      "other_entity": "pro_sup_r",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "pro_sup_r",
      "other_entity": "pro_sup_r",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "pro_sup_r",
      "other_entity": "pro_sup_r",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "deviation_r",
      "other_entity": "deviation_r",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "deviation_r",
      "other_entity": "deviation_r",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "deviation_r",
      "other_entity": "deviation_r",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "flexion_r",
      "other_entity": "flexion_r",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "flexion_r",
      "other_entity": "flexion_r",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "flexion_r",
      "other_entity": "flexion_r",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "wrist_hand_r1_r",
      "other_entity": "wrist_hand_r1_r",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "wrist_hand_r1_r",
      "other_entity": "wrist_hand_r1_r",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "wrist_hand_r1_r",
      "other_entity": "wrist_hand_r1_r",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "wrist_hand_r3_r",
      "other_entity": "wrist_hand_r3_r",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "wrist_hand_r3_r",
      "other_entity": "wrist_hand_r3_r",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "wrist_hand_r3_r",
      "other_entity": "wrist_hand_r3_r",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "cmc_flexion",
      "other_entity": "cmc_flexion",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "cmc_flexion",
      "other_entity": "cmc_flexion",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "cmc_flexion",
      "other_entity": "cmc_flexion",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "cmc_abduction",
      "other_entity": "cmc_abduction",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "cmc_abduction",
      "other_entity": "cmc_abduction",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "cmc_abduction",
      "other_entity": "cmc_abduction",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "mp_flexion",
      "other_entity": "mp_flexion",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "mp_flexion",
      "other_entity": "mp_flexion",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "mp_flexion",
      "other_entity": "mp_flexion",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "ip_flexion",
      "other_entity": "ip_flexion",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "ip_flexion",
      "other_entity": "ip_flexion",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "ip_flexion",
      "other_entity": "ip_flexion",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "2mcp_abduction",
      "other_entity": "2mcp_abduction",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "2mcp_abduction",
      "other_entity": "2mcp_abduction",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "2mcp_abduction",
      "other_entity": "2mcp_abduction",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "2mcp_flexion",
      "other_entity": "2mcp_flexion",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "2mcp_flexion",
      "other_entity": "2mcp_flexion",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "2mcp_flexion",
      "other_entity": "2mcp_flexion",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "2pm_flexion",
      "other_entity": "2pm_flexion",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "2pm_flexion",
      "other_entity": "2pm_flexion",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "2pm_flexion",
      "other_entity": "2pm_flexion",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "2md_flexion",
      "other_entity": "2md_flexion",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "2md_flexion",
      "other_entity": "2md_flexion",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "2md_flexion",
      "other_entity": "2md_flexion",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "3mcp_abduction",
      "other_entity": "3mcp_abduction",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "3mcp_abduction",
      "other_entity": "3mcp_abduction",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "3mcp_abduction",
      "other_entity": "3mcp_abduction",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "3mcp_flexion",
      "other_entity": "3mcp_flexion",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "3mcp_flexion",
      "other_entity": "3mcp_flexion",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "3mcp_flexion",
      "other_entity": "3mcp_flexion",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "3pm_flexion",
      "other_entity": "3pm_flexion",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "3pm_flexion",
      "other_entity": "3pm_flexion",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "3pm_flexion",
      "other_entity": "3pm_flexion",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "3md_flexion",
      "other_entity": "3md_flexion",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "3md_flexion",
      "other_entity": "3md_flexion",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "3md_flexion",
      "other_entity": "3md_flexion",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "4cmc_flexion",
      "other_entity": "4cmc_flexion",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "4cmc_flexion",
      "other_entity": "4cmc_flexion",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "4cmc_flexion",
      "other_entity": "4cmc_flexion",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "4mcp_abduction",
      "other_entity": "4mcp_abduction",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "4mcp_abduction",
      "other_entity": "4mcp_abduction",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "4mcp_abduction",
      "other_entity": "4mcp_abduction",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "4mcp_flexion",
      "other_entity": "4mcp_flexion",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "4mcp_flexion",
      "other_entity": "4mcp_flexion",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "4mcp_flexion",
      "other_entity": "4mcp_flexion",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "4pm_flexion",
      "other_entity": "4pm_flexion",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "4pm_flexion",
      "other_entity": "4pm_flexion",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "4pm_flexion",
      "other_entity": "4pm_flexion",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "4md_flexion",
      "other_entity": "4md_flexion",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "4md_flexion",
      "other_entity": "4md_flexion",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "4md_flexion",
      "other_entity": "4md_flexion",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "CMC5_r1",
      "other_entity": "CMC5_r1",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "CMC5_r1",
      "other_entity": "CMC5_r1",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "CMC5_r1",
      "other_entity": "CMC5_r1",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "5mcp_abduction",
      "other_entity": "5mcp_abduction",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "5mcp_abduction",
      "other_entity": "5mcp_abduction",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "5mcp_abduction",
      "other_entity": "5mcp_abduction",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "5mcp_flexion",
      "other_entity": "5mcp_flexion",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "5mcp_flexion",
      "other_entity": "5mcp_flexion",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "5mcp_flexion",
      "other_entity": "5mcp_flexion",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "5pm_flexion",
      "other_entity": "5pm_flexion",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "5pm_flexion",
      "other_entity": "5pm_flexion",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "5pm_flexion",
      "other_entity": "5pm_flexion",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "5md_flexion",
      "other_entity": "5md_flexion",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "5md_flexion",
      "other_entity": "5md_flexion",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "5md_flexion",
      "other_entity": "5md_flexion",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "objTx",
      "other_entity": "objTx",
      "quantity": "range",
      "tolerance": "slide_range",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "objTx",
      "other_entity": "objTx",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "objTx",
      "other_entity": "objTx",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "objTx",
      "other_entity": "objTx",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "objTy",
      "other_entity": "objTy",
      "quantity": "range",
      "tolerance": "slide_range",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "objTy",
      "other_entity": "objTy",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "objTy",
      "other_entity": "objTy",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "objTy",
      "other_entity": "objTy",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "objTz",
      "other_entity": "objTz",
      "quantity": "range",
      "tolerance": "slide_range",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "objTz",
      "other_entity": "objTz",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "objTz",
      "other_entity": "objTz",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "objTz",
      "other_entity": "objTz",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "objRx",
      "other_entity": "objRx",
      "quantity": "range",
      "tolerance": "range",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "objRx",
      "other_entity": "objRx",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "objRx",
      "other_entity": "objRx",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "objRx",
      "other_entity": "objRx",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "objRy",
      "other_entity": "objRy",
      "quantity": "range",
      "tolerance": "range",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "objRy",
      "other_entity": "objRy",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "objRy",
      "other_entity": "objRy",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "objRy",
      "other_entity": "objRy",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "objRz",
      "other_entity": "objRz",
      "quantity": "range",
      "tolerance": "range",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "objRz",
      "other_entity": "objRz",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "objRz",
      "other_entity": "objRz",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "objRz",
      "other_entity": "objRz",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
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
| sternoclavicular_r2_r / effort | unavailable | unavailable | unavailable |
| sternoclavicular_r2_r / force | unavailable | unavailable | unavailable |
| sternoclavicular_r2_r / velocity | unavailable | unavailable | unavailable |
| sternoclavicular_r3_r / effort | unavailable | unavailable | unavailable |
| sternoclavicular_r3_r / force | unavailable | unavailable | unavailable |
| sternoclavicular_r3_r / velocity | unavailable | unavailable | unavailable |
| unrotscap_r3_r / effort | unavailable | unavailable | unavailable |
| unrotscap_r3_r / force | unavailable | unavailable | unavailable |
| unrotscap_r3_r / velocity | unavailable | unavailable | unavailable |
| unrotscap_r2_r / effort | unavailable | unavailable | unavailable |
| unrotscap_r2_r / force | unavailable | unavailable | unavailable |
| unrotscap_r2_r / velocity | unavailable | unavailable | unavailable |
| acromioclavicular_r2_r / effort | unavailable | unavailable | unavailable |
| acromioclavicular_r2_r / force | unavailable | unavailable | unavailable |
| acromioclavicular_r2_r / velocity | unavailable | unavailable | unavailable |
| acromioclavicular_r3_r / effort | unavailable | unavailable | unavailable |
| acromioclavicular_r3_r / force | unavailable | unavailable | unavailable |
| acromioclavicular_r3_r / velocity | unavailable | unavailable | unavailable |
| acromioclavicular_r1_r / effort | unavailable | unavailable | unavailable |
| acromioclavicular_r1_r / force | unavailable | unavailable | unavailable |
| acromioclavicular_r1_r / velocity | unavailable | unavailable | unavailable |
| unrothum_r1_r / effort | unavailable | unavailable | unavailable |
| unrothum_r1_r / force | unavailable | unavailable | unavailable |
| unrothum_r1_r / velocity | unavailable | unavailable | unavailable |
| unrothum_r3_r / effort | unavailable | unavailable | unavailable |
| unrothum_r3_r / force | unavailable | unavailable | unavailable |
| unrothum_r3_r / velocity | unavailable | unavailable | unavailable |
| unrothum_r2_r / effort | unavailable | unavailable | unavailable |
| unrothum_r2_r / force | unavailable | unavailable | unavailable |
| unrothum_r2_r / velocity | unavailable | unavailable | unavailable |
| elv_angle_r / effort | unavailable | unavailable | unavailable |
| elv_angle_r / force | unavailable | unavailable | unavailable |
| elv_angle_r / velocity | unavailable | unavailable | unavailable |
| shoulder_elv_r / effort | unavailable | unavailable | unavailable |
| shoulder_elv_r / force | unavailable | unavailable | unavailable |
| shoulder_elv_r / velocity | unavailable | unavailable | unavailable |
| shoulder1_r2_r / effort | unavailable | unavailable | unavailable |
| shoulder1_r2_r / force | unavailable | unavailable | unavailable |
| shoulder1_r2_r / velocity | unavailable | unavailable | unavailable |
| shoulder_rot_r / effort | unavailable | unavailable | unavailable |
| shoulder_rot_r / force | unavailable | unavailable | unavailable |
| shoulder_rot_r / velocity | unavailable | unavailable | unavailable |
| elbow_flexion_r / effort | unavailable | unavailable | unavailable |
| elbow_flexion_r / force | unavailable | unavailable | unavailable |
| elbow_flexion_r / velocity | unavailable | unavailable | unavailable |
| pro_sup_r / effort | unavailable | unavailable | unavailable |
| pro_sup_r / force | unavailable | unavailable | unavailable |
| pro_sup_r / velocity | unavailable | unavailable | unavailable |
| deviation_r / effort | unavailable | unavailable | unavailable |
| deviation_r / force | unavailable | unavailable | unavailable |
| deviation_r / velocity | unavailable | unavailable | unavailable |
| flexion_r / effort | unavailable | unavailable | unavailable |
| flexion_r / force | unavailable | unavailable | unavailable |
| flexion_r / velocity | unavailable | unavailable | unavailable |
| wrist_hand_r1_r / effort | unavailable | unavailable | unavailable |
| wrist_hand_r1_r / force | unavailable | unavailable | unavailable |
| wrist_hand_r1_r / velocity | unavailable | unavailable | unavailable |
| wrist_hand_r3_r / effort | unavailable | unavailable | unavailable |
| wrist_hand_r3_r / force | unavailable | unavailable | unavailable |
| wrist_hand_r3_r / velocity | unavailable | unavailable | unavailable |
| cmc_flexion / effort | unavailable | unavailable | unavailable |
| cmc_flexion / force | unavailable | unavailable | unavailable |
| cmc_flexion / velocity | unavailable | unavailable | unavailable |
| cmc_abduction / effort | unavailable | unavailable | unavailable |
| cmc_abduction / force | unavailable | unavailable | unavailable |
| cmc_abduction / velocity | unavailable | unavailable | unavailable |
| mp_flexion / effort | unavailable | unavailable | unavailable |
| mp_flexion / force | unavailable | unavailable | unavailable |
| mp_flexion / velocity | unavailable | unavailable | unavailable |
| ip_flexion / effort | unavailable | unavailable | unavailable |
| ip_flexion / force | unavailable | unavailable | unavailable |
| ip_flexion / velocity | unavailable | unavailable | unavailable |
| 2mcp_abduction / effort | unavailable | unavailable | unavailable |
| 2mcp_abduction / force | unavailable | unavailable | unavailable |
| 2mcp_abduction / velocity | unavailable | unavailable | unavailable |
| 2mcp_flexion / effort | unavailable | unavailable | unavailable |
| 2mcp_flexion / force | unavailable | unavailable | unavailable |
| 2mcp_flexion / velocity | unavailable | unavailable | unavailable |
| 2pm_flexion / effort | unavailable | unavailable | unavailable |
| 2pm_flexion / force | unavailable | unavailable | unavailable |
| 2pm_flexion / velocity | unavailable | unavailable | unavailable |
| 2md_flexion / effort | unavailable | unavailable | unavailable |
| 2md_flexion / force | unavailable | unavailable | unavailable |
| 2md_flexion / velocity | unavailable | unavailable | unavailable |
| 3mcp_abduction / effort | unavailable | unavailable | unavailable |
| 3mcp_abduction / force | unavailable | unavailable | unavailable |
| 3mcp_abduction / velocity | unavailable | unavailable | unavailable |
| 3mcp_flexion / effort | unavailable | unavailable | unavailable |
| 3mcp_flexion / force | unavailable | unavailable | unavailable |
| 3mcp_flexion / velocity | unavailable | unavailable | unavailable |
| 3pm_flexion / effort | unavailable | unavailable | unavailable |
| 3pm_flexion / force | unavailable | unavailable | unavailable |
| 3pm_flexion / velocity | unavailable | unavailable | unavailable |
| 3md_flexion / effort | unavailable | unavailable | unavailable |
| 3md_flexion / force | unavailable | unavailable | unavailable |
| 3md_flexion / velocity | unavailable | unavailable | unavailable |
| 4cmc_flexion / effort | unavailable | unavailable | unavailable |
| 4cmc_flexion / force | unavailable | unavailable | unavailable |
| 4cmc_flexion / velocity | unavailable | unavailable | unavailable |
| 4mcp_abduction / effort | unavailable | unavailable | unavailable |
| 4mcp_abduction / force | unavailable | unavailable | unavailable |
| 4mcp_abduction / velocity | unavailable | unavailable | unavailable |
| 4mcp_flexion / effort | unavailable | unavailable | unavailable |
| 4mcp_flexion / force | unavailable | unavailable | unavailable |
| 4mcp_flexion / velocity | unavailable | unavailable | unavailable |
| 4pm_flexion / effort | unavailable | unavailable | unavailable |
| 4pm_flexion / force | unavailable | unavailable | unavailable |
| 4pm_flexion / velocity | unavailable | unavailable | unavailable |
| 4md_flexion / effort | unavailable | unavailable | unavailable |
| 4md_flexion / force | unavailable | unavailable | unavailable |
| 4md_flexion / velocity | unavailable | unavailable | unavailable |
| CMC5_r1 / effort | unavailable | unavailable | unavailable |
| CMC5_r1 / force | unavailable | unavailable | unavailable |
| CMC5_r1 / velocity | unavailable | unavailable | unavailable |
| 5mcp_abduction / effort | unavailable | unavailable | unavailable |
| 5mcp_abduction / force | unavailable | unavailable | unavailable |
| 5mcp_abduction / velocity | unavailable | unavailable | unavailable |
| 5mcp_flexion / effort | unavailable | unavailable | unavailable |
| 5mcp_flexion / force | unavailable | unavailable | unavailable |
| 5mcp_flexion / velocity | unavailable | unavailable | unavailable |
| 5pm_flexion / effort | unavailable | unavailable | unavailable |
| 5pm_flexion / force | unavailable | unavailable | unavailable |
| 5pm_flexion / velocity | unavailable | unavailable | unavailable |
| 5md_flexion / effort | unavailable | unavailable | unavailable |
| 5md_flexion / force | unavailable | unavailable | unavailable |
| 5md_flexion / velocity | unavailable | unavailable | unavailable |
| objTx / effort | unavailable | unavailable | unavailable |
| objTx / force | unavailable | unavailable | unavailable |
| objTx / velocity | unavailable | unavailable | unavailable |
| objTy / effort | unavailable | unavailable | unavailable |
| objTy / force | unavailable | unavailable | unavailable |
| objTy / velocity | unavailable | unavailable | unavailable |
| objTz / effort | unavailable | unavailable | unavailable |
| objTz / force | unavailable | unavailable | unavailable |
| objTz / velocity | unavailable | unavailable | unavailable |
| objRx / effort | unavailable | unavailable | unavailable |
| objRx / force | unavailable | unavailable | unavailable |
| objRx / velocity | unavailable | unavailable | unavailable |
| objRy / effort | unavailable | unavailable | unavailable |
| objRy / force | unavailable | unavailable | unavailable |
| objRy / velocity | unavailable | unavailable | unavailable |
| objRz / effort | unavailable | unavailable | unavailable |
| objRz / force | unavailable | unavailable | unavailable |
| objRz / velocity | unavailable | unavailable | unavailable |
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

## History inputs

```json
[
  "Asset/Asset_Lowerbody.xml",
  "Asset/Asset_Others.xml",
  "Asset/Asset_Torso.xml",
  "Asset/Asset_Upperbody.xml",
  "Asset/marble.png",
  "Body_Manipulation/Body_Arm_Hand_Vis_l.xml",
  "Body_Manipulation/Body_Arm_Hand_r.xml",
  "Body_Manipulation/Body_Leg_Foot_Vis_l.xml",
  "Body_Manipulation/Body_Leg_Foot_Vis_r.xml",
  "Body_Manipulation/Body_Torso_Unimanual.xml",
  "Body_Manipulation/Body_Waterbottle.xml",
  "Contact/Contact_Upperbody.xml",
  "Equality/Equality_Upperbody_r.xml",
  "Geometry/1mc.stl",
  "Geometry/1mc_mirror.obj",
  "Geometry/2distph.stl",
  "Geometry/2distph_mirror.obj",
  "Geometry/2mc.stl",
  "Geometry/2mc_mirror.obj",
  "Geometry/2midph.stl",
  "Geometry/2midph_mirror.obj",
  "Geometry/2proxph.stl",
  "Geometry/2proxph_mirror.obj",
  "Geometry/3distph.stl",
  "Geometry/3distph_mirror.obj",
  "Geometry/3mc.stl",
  "Geometry/3mc_mirror.obj",
  "Geometry/3midph.stl",
  "Geometry/3midph_mirror.obj",
  "Geometry/3proxph.stl",
  "Geometry/3proxph_mirror.obj",
  "Geometry/4distph_new.stl",
  "Geometry/4distph_new_mirror.obj",
  "Geometry/4mc_new.stl",
  "Geometry/4mc_new_mirror.obj",
  "Geometry/4midph_new.stl",
  "Geometry/4midph_new_mirror.obj",
  "Geometry/4proxph_new.stl",
  "Geometry/4proxph_new_mirror.obj",
  "Geometry/5distph_new.stl",
  "Geometry/5distph_new_mirror.obj",
  "Geometry/5mc_new.stl",
  "Geometry/5mc_new_mirror.obj",
  "Geometry/5midph_new.stl",
  "Geometry/5midph_new_mirror.obj",
  "Geometry/5proxph_new.stl",
  "Geometry/5proxph_new_mirror.obj",
  "Geometry/Rib10L.obj",
  "Geometry/Rib10R.obj",
  "Geometry/Rib11L.obj",
  "Geometry/Rib11R.obj",
  "Geometry/Rib12L.obj",
  "Geometry/Rib12R.obj",
  "Geometry/Rib1L.obj",
  "Geometry/Rib1R.obj",
  "Geometry/Rib2L.obj",
  "Geometry/Rib2R.obj",
  "Geometry/Rib3L.obj",
  "Geometry/Rib3R.obj",
  "Geometry/Rib4L.obj",
  "Geometry/Rib4R.obj",
  "Geometry/Rib5L.obj",
  "Geometry/Rib5R.obj",
  "Geometry/Rib6L.obj",
  "Geometry/Rib6R.obj",
  "Geometry/Rib7L.obj",
  "Geometry/Rib7R.obj",
  "Geometry/Rib8L.obj",
  "Geometry/Rib8R.obj",
  "Geometry/Rib9L.obj",
  "Geometry/Rib9R.obj",
  "Geometry/Sternum.obj",
  "Geometry/capitate.stl",
  "Geometry/capitate_mirror.obj",
  "Geometry/cerv1.stl",
  "Geometry/cerv2.stl",
  "Geometry/cerv3.stl",
  "Geometry/cerv4.stl",
  "Geometry/cerv5.stl",
  "Geometry/cerv6.stl",
  "Geometry/clavicle.stl",
  "Geometry/clavicle_mirror.stl",
  "Geometry/hamate.stl",
  "Geometry/hamate_mirror.obj",
  "Geometry/hand_1mc.stl",
  "Geometry/hand_1mc_mirror.stl",
  "Geometry/hand_2distph.stl",
  "Geometry/hand_2distph_mirror.stl",
  "Geometry/hand_2midph.stl",
  "Geometry/hand_2midph_mirror.stl",
  "Geometry/hand_2proxph.stl",
  "Geometry/hand_2proxph_mirror.stl",
  "Geometry/hand_3distph.stl",
  "Geometry/hand_3distph_mirror.stl",
  "Geometry/hand_3midph.stl",
  "Geometry/hand_3midph_mirror.stl",
  "Geometry/hand_3proxph.stl",
  "Geometry/hand_3proxph_mirror.stl",
  "Geometry/hand_4distph.stl",
  "Geometry/hand_4distph_mirror.stl",
  "Geometry/hand_4midph.stl",
  "Geometry/hand_4midph_mirror.stl",
  "Geometry/hand_4proxph.stl",
  "Geometry/hand_4proxph_mirror.stl",
  "Geometry/hand_5distph.stl",
  "Geometry/hand_5distph_mirror.stl",
  "Geometry/hand_5midph.stl",
  "Geometry/hand_5midph_mirror.stl",
  "Geometry/hand_5proxph.stl",
  "Geometry/hand_5proxph_mirror.stl",
  "Geometry/hand_capitate.stl",
  "Geometry/hand_capitate_mirror.stl",
  "Geometry/hand_lunate.stl",
  "Geometry/hand_lunate_mirror.stl",
  "Geometry/hand_thumbdist.stl",
  "Geometry/hand_thumbdist_mirror.stl",
  "Geometry/hand_thumbprox.stl",
  "Geometry/hand_thumbprox_mirror.stl",
  "Geometry/humerus.stl",
  "Geometry/humerus_mirror.stl",
  "Geometry/jaw.stl",
  "Geometry/l_bofoot.stl",
  "Geometry/l_femur.stl",
  "Geometry/l_fibula.stl",
  "Geometry/l_foot.stl",
  "Geometry/l_patella.stl",
  "Geometry/l_pelvis.stl",
  "Geometry/l_talus.stl",
  "Geometry/l_tibia.stl",
  "Geometry/lumbar1.stl",
  "Geometry/lumbar2.stl",
  "Geometry/lumbar3.stl",
  "Geometry/lumbar4.stl",
  "Geometry/lumbar5.stl",
  "Geometry/lunate.stl",
  "Geometry/lunate_mirror.obj",
  "Geometry/pisiform.stl",
  "Geometry/pisiform_mirror.obj",
  "Geometry/r_bofoot.stl",
  "Geometry/r_femur.stl",
  "Geometry/r_fibula.stl",
  "Geometry/r_foot.stl",
  "Geometry/r_patella.stl",
  "Geometry/r_pelvis.stl",
  "Geometry/r_talus.stl",
  "Geometry/r_tibia.stl",
  "Geometry/radius.stl",
  "Geometry/radius_mirror.stl",
  "Geometry/rotatedcerv7.stl",
  "Geometry/sacrum.stl",
  "Geometry/scaphoid.stl",
  "Geometry/scaphoid_mirror.obj",
  "Geometry/scapula.stl",
  "Geometry/scapula_mirror.stl",
  "Geometry/sdfastPISIFORMw.stl",
  "Geometry/sdfastPISIFORMw_mirror.stl",
  "Geometry/sdfastSCAPHOIDw.stl",
  "Geometry/sdfastSCAPHOIDw_mirror.stl",
  "Geometry/sdfastTRIQUETRALw.stl",
  "Geometry/sdfastTRIQUETRALw_mirror.stl",
  "Geometry/sdfast_1seg_hand_fr_c_2mc.stl",
  "Geometry/sdfast_1seg_hand_fr_c_2mc_mirror.stl",
  "Geometry/sdfast_1seg_hand_fr_c_3mc.stl",
  "Geometry/sdfast_1seg_hand_fr_c_3mc_mirror.stl",
  "Geometry/sdfast_1seg_hand_fr_c_4mc.stl",
  "Geometry/sdfast_1seg_hand_fr_c_4mc_mirror.stl",
  "Geometry/sdfast_1seg_hand_fr_c_5mc.stl",
  "Geometry/sdfast_1seg_hand_fr_c_5mc_mirror.stl",
  "Geometry/sdfast_1seg_hand_fr_c_hamate.stl",
  "Geometry/sdfast_1seg_hand_fr_c_hamate_mirror.stl",
  "Geometry/sdfast_1seg_hand_fr_c_trapezium.stl",
  "Geometry/sdfast_1seg_hand_fr_c_trapezium_mirror.stl",
  "Geometry/sdfast_1seg_hand_fr_c_trapezoid.stl",
  "Geometry/sdfast_1seg_hand_fr_c_trapezoid_mirror.stl",
  "Geometry/skull.stl",
  "Geometry/thoracic1.stl",
  "Geometry/thoracic10.stl",
  "Geometry/thoracic11.stl",
  "Geometry/thoracic12.stl",
  "Geometry/thoracic2.stl",
  "Geometry/thoracic3.stl",
  "Geometry/thoracic4.stl",
  "Geometry/thoracic5.stl",
  "Geometry/thoracic6.stl",
  "Geometry/thoracic7.stl",
  "Geometry/thoracic8.stl",
  "Geometry/thoracic9.stl",
  "Geometry/thumbdist.stl",
  "Geometry/thumbdist_mirror.obj",
  "Geometry/thumbprox.stl",
  "Geometry/thumbprox_mirror.obj",
  "Geometry/trapezium.stl",
  "Geometry/trapezium_mirror.obj",
  "Geometry/trapezoid.stl",
  "Geometry/trapezoid_mirror.obj",
  "Geometry/triquetral.stl",
  "Geometry/triquetral_mirror.obj",
  "Geometry/ulna.stl",
  "Geometry/ulna_mirror.stl",
  "Geometry/waterbottle/waterbottle.stl",
  "Geometry/waterbottle/waterbottle_contact0.stl",
  "Geometry/waterbottle/waterbottle_contact1.stl",
  "MS-Human-700-Manipulation.xml",
  "Muscle/Muscle_Arm_Hand_r.xml",
  "Tendon/Tendon_Arm_Hand_l.xml",
  "Tendon/Tendon_Arm_Hand_r.xml",
  "Tendon/Tendon_Leg_l.xml",
  "Tendon/Tendon_Leg_r.xml",
  "Tendon/Tendon_Torso.xml"
]
```

## Self comparisons

```json
[
  {
    "file": "ms_human_700/MS-Human-700-Locomotion.xml",
    "status": "passed",
    "findings": 0
  },
  {
    "file": "ms_human_700/MS-Human-700-Manipulation.xml",
    "status": "passed",
    "findings": 0
  },
  {
    "file": "ms_human_700/MS-Human-700.xml",
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
    "geometry_stripped": false,
    "missing_explicit_inertials": [
      "proximal_row",
      "capitate",
      "trapezium",
      "firstmc",
      "proximal_thumb",
      "distal_thumb",
      "trapezoid",
      "hamate",
      "secondmc",
      "2proxph",
      "2midph",
      "2distph",
      "thirdmc",
      "3proxph",
      "3midph",
      "3distph",
      "fourthmc",
      "4proxph",
      "4midph",
      "4distph",
      "fifthmc",
      "5proxph",
      "5midph",
      "5distph",
      "proximal_row_l",
      "capitate_l",
      "trapezium_l",
      "firstmc_l",
      "proximal_thumb_l",
      "distal_thumb_l",
      "trapezoid_l",
      "hamate_l",
      "secondmc_l",
      "2proxph_l",
      "2midph_l",
      "2distph_l",
      "thirdmc_l",
      "3proxph_l",
      "3midph_l",
      "3distph_l",
      "fourthmc_l",
      "4proxph_l",
      "4midph_l",
      "4distph_l",
      "fifthmc_l",
      "5proxph_l",
      "5midph_l",
      "5distph_l",
      "rib1_R",
      "rib1_L",
      "rib2_R",
      "rib2_L",
      "rib3_R",
      "rib3_L",
      "rib4_R",
      "rib4_L",
      "rib5_R",
      "rib5_L",
      "rib6_R",
      "rib6_L",
      "rib7_R",
      "rib7_L",
      "rib8_R",
      "rib8_L",
      "rib9_R",
      "rib9_L",
      "rib10_R",
      "rib10_L",
      "rib11_R",
      "rib11_L",
      "rib12_R",
      "rib12_L",
      "waterbottle",
      "target",
      "table"
    ],
    "assets_loaded": 190,
    "mesh_conversions": [],
    "nonphysical_normalizations": [],
    "xacro_arguments": {},
    "source_dependencies": [
      "ms_human_700/MS-Human-700-Manipulation.xml",
      "ms_human_700/assets/asset/Asset_Lowerbody.xml",
      "ms_human_700/assets/asset/Asset_Others.xml",
      "ms_human_700/assets/asset/Asset_Torso.xml",
      "ms_human_700/assets/asset/Asset_Upperbody.xml",
      "ms_human_700/assets/body_manipulation/Body_Arm_Hand_Vis_l.xml",
      "ms_human_700/assets/body_manipulation/Body_Arm_Hand_r.xml",
      "ms_human_700/assets/body_manipulation/Body_Leg_Foot_Vis_l.xml",
      "ms_human_700/assets/body_manipulation/Body_Leg_Foot_Vis_r.xml",
      "ms_human_700/assets/body_manipulation/Body_Torso_Unimanual.xml",
      "ms_human_700/assets/body_manipulation/Body_Waterbottle.xml",
      "ms_human_700/assets/contact/Contact_Upperbody.xml",
      "ms_human_700/assets/equality/Equality_Upperbody_r.xml",
      "ms_human_700/assets/muscle/Muscle_Arm_Hand_r.xml",
      "ms_human_700/assets/tendon/Tendon_Arm_Hand_l.xml",
      "ms_human_700/assets/tendon/Tendon_Arm_Hand_r.xml",
      "ms_human_700/assets/tendon/Tendon_Leg_l.xml",
      "ms_human_700/assets/tendon/Tendon_Leg_r.xml",
      "ms_human_700/assets/tendon/Tendon_Torso.xml",
      "ms_human_700/assets/geometry/sacrum.stl",
      "ms_human_700/assets/geometry/r_pelvis.stl",
      "ms_human_700/assets/geometry/l_pelvis.stl",
      "ms_human_700/assets/geometry/r_femur.stl",
      "ms_human_700/assets/geometry/r_tibia.stl",
      "ms_human_700/assets/geometry/r_fibula.stl",
      "ms_human_700/assets/geometry/r_talus.stl",
      "ms_human_700/assets/geometry/r_foot.stl",
      "ms_human_700/assets/geometry/r_bofoot.stl",
      "ms_human_700/assets/geometry/r_patella.stl",
      "ms_human_700/assets/geometry/l_femur.stl",
      "ms_human_700/assets/geometry/l_tibia.stl",
      "ms_human_700/assets/geometry/l_fibula.stl",
      "ms_human_700/assets/geometry/l_talus.stl",
      "ms_human_700/assets/geometry/l_foot.stl",
      "ms_human_700/assets/geometry/l_bofoot.stl",
      "ms_human_700/assets/geometry/l_patella.stl",
      "ms_human_700/assets/geometry/lumbar5.stl",
      "ms_human_700/assets/geometry/lumbar4.stl",
      "ms_human_700/assets/geometry/lumbar3.stl",
      "ms_human_700/assets/geometry/lumbar2.stl",
      "ms_human_700/assets/geometry/lumbar1.stl",
      "ms_human_700/assets/geometry/thoracic12.stl",
      "ms_human_700/assets/geometry/thoracic11.stl",
      "ms_human_700/assets/geometry/thoracic10.stl",
      "ms_human_700/assets/geometry/thoracic9.stl",
      "ms_human_700/assets/geometry/thoracic8.stl",
      "ms_human_700/assets/geometry/thoracic7.stl",
      "ms_human_700/assets/geometry/thoracic6.stl",
      "ms_human_700/assets/geometry/thoracic5.stl",
      "ms_human_700/assets/geometry/thoracic4.stl",
      "ms_human_700/assets/geometry/thoracic3.stl",
      "ms_human_700/assets/geometry/thoracic2.stl",
      "ms_human_700/assets/geometry/thoracic1.stl",
      "ms_human_700/assets/geometry/rotatedcerv7.stl",
      "ms_human_700/assets/geometry/cerv6.stl",
      "ms_human_700/assets/geometry/cerv5.stl",
      "ms_human_700/assets/geometry/cerv4.stl",
      "ms_human_700/assets/geometry/cerv3.stl",
      "ms_human_700/assets/geometry/cerv2.stl",
      "ms_human_700/assets/geometry/cerv1.stl",
      "ms_human_700/assets/geometry/jaw.stl",
      "ms_human_700/assets/geometry/skull.stl",
      "ms_human_700/assets/geometry/Rib1R.obj",
      "ms_human_700/assets/geometry/Sternum.obj",
      "ms_human_700/assets/geometry/Rib1L.obj",
      "ms_human_700/assets/geometry/Rib2R.obj",
      "ms_human_700/assets/geometry/Rib2L.obj",
      "ms_human_700/assets/geometry/Rib3R.obj",
      "ms_human_700/assets/geometry/Rib3L.obj",
      "ms_human_700/assets/geometry/Rib4R.obj",
      "ms_human_700/assets/geometry/Rib4L.obj",
      "ms_human_700/assets/geometry/Rib5R.obj",
      "ms_human_700/assets/geometry/Rib5L.obj",
      "ms_human_700/assets/geometry/Rib6R.obj",
      "ms_human_700/assets/geometry/Rib6L.obj",
      "ms_human_700/assets/geometry/Rib7R.obj",
      "ms_human_700/assets/geometry/Rib7L.obj",
      "ms_human_700/assets/geometry/Rib8R.obj",
      "ms_human_700/assets/geometry/Rib8L.obj",
      "ms_human_700/assets/geometry/Rib9R.obj",
      "ms_human_700/assets/geometry/Rib9L.obj",
      "ms_human_700/assets/geometry/Rib10R.obj",
      "ms_human_700/assets/geometry/Rib10L.obj",
      "ms_human_700/assets/geometry/Rib11R.obj",
      "ms_human_700/assets/geometry/Rib11L.obj",
      "ms_human_700/assets/geometry/Rib12R.obj",
      "ms_human_700/assets/geometry/Rib12L.obj",
      "ms_human_700/assets/geometry/clavicle.stl",
      "ms_human_700/assets/geometry/scapula.stl",
      "ms_human_700/assets/geometry/humerus.stl",
      "ms_human_700/assets/geometry/ulna.stl",
      "ms_human_700/assets/geometry/radius.stl",
      "ms_human_700/assets/geometry/hand_lunate.stl",
      "ms_human_700/assets/geometry/sdfastSCAPHOIDw.stl",
      "ms_human_700/assets/geometry/sdfastPISIFORMw.stl",
      "ms_human_700/assets/geometry/sdfastTRIQUETRALw.stl",
      "ms_human_700/assets/geometry/sdfast_1seg_hand_fr_c_5mc.stl",
      "ms_human_700/assets/geometry/sdfast_1seg_hand_fr_c_4mc.stl",
      "ms_human_700/assets/geometry/sdfast_1seg_hand_fr_c_3mc.stl",
      "ms_human_700/assets/geometry/sdfast_1seg_hand_fr_c_2mc.stl",
      "ms_human_700/assets/geometry/sdfast_1seg_hand_fr_c_trapezium.stl",
      "ms_human_700/assets/geometry/sdfast_1seg_hand_fr_c_trapezoid.stl",
      "ms_human_700/assets/geometry/sdfast_1seg_hand_fr_c_hamate.stl",
      "ms_human_700/assets/geometry/hand_capitate.stl",
      "ms_human_700/assets/geometry/hand_2proxph.stl",
      "ms_human_700/assets/geometry/hand_2midph.stl",
      "ms_human_700/assets/geometry/hand_2distph.stl",
      "ms_human_700/assets/geometry/hand_3proxph.stl",
      "ms_human_700/assets/geometry/hand_3midph.stl",
      "ms_human_700/assets/geometry/hand_3distph.stl",
      "ms_human_700/assets/geometry/hand_4proxph.stl",
      "ms_human_700/assets/geometry/hand_4midph.stl",
      "ms_human_700/assets/geometry/hand_4distph.stl",
      "ms_human_700/assets/geometry/hand_5proxph.stl",
      "ms_human_700/assets/geometry/hand_5midph.stl",
      "ms_human_700/assets/geometry/hand_5distph.stl",
      "ms_human_700/assets/geometry/hand_thumbprox.stl",
      "ms_human_700/assets/geometry/hand_thumbdist.stl",
      "ms_human_700/assets/geometry/hand_1mc.stl",
      "ms_human_700/assets/geometry/clavicle_mirror.stl",
      "ms_human_700/assets/geometry/scapula_mirror.stl",
      "ms_human_700/assets/geometry/humerus_mirror.stl",
      "ms_human_700/assets/geometry/ulna_mirror.stl",
      "ms_human_700/assets/geometry/radius_mirror.stl",
      "ms_human_700/assets/geometry/hand_lunate_mirror.stl",
      "ms_human_700/assets/geometry/sdfastSCAPHOIDw_mirror.stl",
      "ms_human_700/assets/geometry/sdfastPISIFORMw_mirror.stl",
      "ms_human_700/assets/geometry/sdfastTRIQUETRALw_mirror.stl",
      "ms_human_700/assets/geometry/sdfast_1seg_hand_fr_c_5mc_mirror.stl",
      "ms_human_700/assets/geometry/sdfast_1seg_hand_fr_c_4mc_mirror.stl",
      "ms_human_700/assets/geometry/sdfast_1seg_hand_fr_c_3mc_mirror.stl",
      "ms_human_700/assets/geometry/sdfast_1seg_hand_fr_c_2mc_mirror.stl",
      "ms_human_700/assets/geometry/sdfast_1seg_hand_fr_c_trapezium_mirror.stl",
      "ms_human_700/assets/geometry/sdfast_1seg_hand_fr_c_trapezoid_mirror.stl",
      "ms_human_700/assets/geometry/sdfast_1seg_hand_fr_c_hamate_mirror.stl",
      "ms_human_700/assets/geometry/hand_capitate_mirror.stl",
      "ms_human_700/assets/geometry/hand_2proxph_mirror.stl",
      "ms_human_700/assets/geometry/hand_2midph_mirror.stl",
      "ms_human_700/assets/geometry/hand_2distph_mirror.stl",
      "ms_human_700/assets/geometry/hand_3proxph_mirror.stl",
      "ms_human_700/assets/geometry/hand_3midph_mirror.stl",
      "ms_human_700/assets/geometry/hand_3distph_mirror.stl",
      "ms_human_700/assets/geometry/hand_4proxph_mirror.stl",
      "ms_human_700/assets/geometry/hand_4midph_mirror.stl",
      "ms_human_700/assets/geometry/hand_4distph_mirror.stl",
      "ms_human_700/assets/geometry/hand_5proxph_mirror.stl",
      "ms_human_700/assets/geometry/hand_5midph_mirror.stl",
      "ms_human_700/assets/geometry/hand_5distph_mirror.stl",
      "ms_human_700/assets/geometry/hand_thumbprox_mirror.stl",
      "ms_human_700/assets/geometry/hand_thumbdist_mirror.stl",
      "ms_human_700/assets/geometry/hand_1mc_mirror.stl",
      "ms_human_700/assets/geometry/lunate.stl",
      "ms_human_700/assets/geometry/scaphoid.stl",
      "ms_human_700/assets/geometry/pisiform.stl",
      "ms_human_700/assets/geometry/triquetral.stl",
      "ms_human_700/assets/geometry/capitate.stl",
      "ms_human_700/assets/geometry/trapezium.stl",
      "ms_human_700/assets/geometry/1mc.stl",
      "ms_human_700/assets/geometry/thumbprox.stl",
      "ms_human_700/assets/geometry/thumbdist.stl",
      "ms_human_700/assets/geometry/trapezoid.stl",
      "ms_human_700/assets/geometry/hamate.stl",
      "ms_human_700/assets/geometry/2mc.stl",
      "ms_human_700/assets/geometry/2proxph.stl",
      "ms_human_700/assets/geometry/2midph.stl",
      "ms_human_700/assets/geometry/2distph.stl",
      "ms_human_700/assets/geometry/3mc.stl",
      "ms_human_700/assets/geometry/3proxph.stl",
      "ms_human_700/assets/geometry/3midph.stl",
      "ms_human_700/assets/geometry/3distph.stl",
      "ms_human_700/assets/geometry/4mc_new.stl",
      "ms_human_700/assets/geometry/4proxph_new.stl",
      "ms_human_700/assets/geometry/4midph_new.stl",
      "ms_human_700/assets/geometry/4distph_new.stl",
      "ms_human_700/assets/geometry/5mc_new.stl",
      "ms_human_700/assets/geometry/5proxph_new.stl",
      "ms_human_700/assets/geometry/5midph_new.stl",
      "ms_human_700/assets/geometry/5distph_new.stl",
      "ms_human_700/assets/geometry/lunate_mirror.obj",
      "ms_human_700/assets/geometry/scaphoid_mirror.obj",
      "ms_human_700/assets/geometry/pisiform_mirror.obj",
      "ms_human_700/assets/geometry/triquetral_mirror.obj",
      "ms_human_700/assets/geometry/capitate_mirror.obj",
      "ms_human_700/assets/geometry/trapezium_mirror.obj",
      "ms_human_700/assets/geometry/1mc_mirror.obj",
      "ms_human_700/assets/geometry/thumbprox_mirror.obj",
      "ms_human_700/assets/geometry/thumbdist_mirror.obj",
      "ms_human_700/assets/geometry/trapezoid_mirror.obj",
      "ms_human_700/assets/geometry/hamate_mirror.obj",
      "ms_human_700/assets/geometry/2mc_mirror.obj",
      "ms_human_700/assets/geometry/2proxph_mirror.obj",
      "ms_human_700/assets/geometry/2midph_mirror.obj",
      "ms_human_700/assets/geometry/2distph_mirror.obj",
      "ms_human_700/assets/geometry/3mc_mirror.obj",
      "ms_human_700/assets/geometry/3proxph_mirror.obj",
      "ms_human_700/assets/geometry/3midph_mirror.obj",
      "ms_human_700/assets/geometry/3distph_mirror.obj",
      "ms_human_700/assets/geometry/4mc_new_mirror.obj",
      "ms_human_700/assets/geometry/4proxph_new_mirror.obj",
      "ms_human_700/assets/geometry/4midph_new_mirror.obj",
      "ms_human_700/assets/geometry/4distph_new_mirror.obj",
      "ms_human_700/assets/geometry/5mc_new_mirror.obj",
      "ms_human_700/assets/geometry/5proxph_new_mirror.obj",
      "ms_human_700/assets/geometry/5midph_new_mirror.obj",
      "ms_human_700/assets/geometry/5distph_new_mirror.obj",
      "ms_human_700/assets/asset/marble.png",
      "ms_human_700/assets/geometry/waterbottle/waterbottle.stl",
      "ms_human_700/assets/geometry/waterbottle/waterbottle_contact0.stl",
      "ms_human_700/assets/geometry/waterbottle/waterbottle_contact1.stl"
    ],
    "registration": {
      "translation": [
        0.0,
        0.0,
        0.94
      ],
      "rotation": [
        [
          0.9999999999999998,
          0.0,
          0.0
        ],
        [
          0.0,
          0.0,
          -0.9999999999999998
        ],
        [
          0.0,
          0.9999999999999998,
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
      "proximal_row",
      "capitate",
      "trapezium",
      "firstmc",
      "proximal_thumb",
      "distal_thumb",
      "trapezoid",
      "hamate",
      "secondmc",
      "2proxph",
      "2midph",
      "2distph",
      "thirdmc",
      "3proxph",
      "3midph",
      "3distph",
      "fourthmc",
      "4proxph",
      "4midph",
      "4distph",
      "fifthmc",
      "5proxph",
      "5midph",
      "5distph",
      "proximal_row_l",
      "capitate_l",
      "trapezium_l",
      "firstmc_l",
      "proximal_thumb_l",
      "distal_thumb_l",
      "trapezoid_l",
      "hamate_l",
      "secondmc_l",
      "2proxph_l",
      "2midph_l",
      "2distph_l",
      "thirdmc_l",
      "3proxph_l",
      "3midph_l",
      "3distph_l",
      "fourthmc_l",
      "4proxph_l",
      "4midph_l",
      "4distph_l",
      "fifthmc_l",
      "5proxph_l",
      "5midph_l",
      "5distph_l",
      "rib1_R",
      "rib1_L",
      "rib2_R",
      "rib2_L",
      "rib3_R",
      "rib3_L",
      "rib4_R",
      "rib4_L",
      "rib5_R",
      "rib5_L",
      "rib6_R",
      "rib6_L",
      "rib7_R",
      "rib7_L",
      "rib8_R",
      "rib8_L",
      "rib9_R",
      "rib9_L",
      "rib10_R",
      "rib10_L",
      "rib11_R",
      "rib11_L",
      "rib12_R",
      "rib12_L",
      "waterbottle",
      "target",
      "table"
    ],
    "assets_loaded": 190,
    "mesh_conversions": [],
    "nonphysical_normalizations": [],
    "xacro_arguments": {},
    "source_dependencies": [
      "Asset/Asset_Lowerbody.xml",
      "Asset/Asset_Others.xml",
      "Asset/Asset_Torso.xml",
      "Asset/Asset_Upperbody.xml",
      "Body_Manipulation/Body_Arm_Hand_Vis_l.xml",
      "Body_Manipulation/Body_Arm_Hand_r.xml",
      "Body_Manipulation/Body_Leg_Foot_Vis_l.xml",
      "Body_Manipulation/Body_Leg_Foot_Vis_r.xml",
      "Body_Manipulation/Body_Torso_Unimanual.xml",
      "Body_Manipulation/Body_Waterbottle.xml",
      "Contact/Contact_Upperbody.xml",
      "Equality/Equality_Upperbody_r.xml",
      "MS-Human-700-Manipulation.xml",
      "Muscle/Muscle_Arm_Hand_r.xml",
      "Tendon/Tendon_Arm_Hand_l.xml",
      "Tendon/Tendon_Arm_Hand_r.xml",
      "Tendon/Tendon_Leg_l.xml",
      "Tendon/Tendon_Leg_r.xml",
      "Tendon/Tendon_Torso.xml",
      "Geometry/sacrum.stl",
      "Geometry/r_pelvis.stl",
      "Geometry/l_pelvis.stl",
      "Geometry/r_femur.stl",
      "Geometry/r_tibia.stl",
      "Geometry/r_fibula.stl",
      "Geometry/r_talus.stl",
      "Geometry/r_foot.stl",
      "Geometry/r_bofoot.stl",
      "Geometry/r_patella.stl",
      "Geometry/l_femur.stl",
      "Geometry/l_tibia.stl",
      "Geometry/l_fibula.stl",
      "Geometry/l_talus.stl",
      "Geometry/l_foot.stl",
      "Geometry/l_bofoot.stl",
      "Geometry/l_patella.stl",
      "Geometry/lumbar5.stl",
      "Geometry/lumbar4.stl",
      "Geometry/lumbar3.stl",
      "Geometry/lumbar2.stl",
      "Geometry/lumbar1.stl",
      "Geometry/thoracic12.stl",
      "Geometry/thoracic11.stl",
      "Geometry/thoracic10.stl",
      "Geometry/thoracic9.stl",
      "Geometry/thoracic8.stl",
      "Geometry/thoracic7.stl",
      "Geometry/thoracic6.stl",
      "Geometry/thoracic5.stl",
      "Geometry/thoracic4.stl",
      "Geometry/thoracic3.stl",
      "Geometry/thoracic2.stl",
      "Geometry/thoracic1.stl",
      "Geometry/rotatedcerv7.stl",
      "Geometry/cerv6.stl",
      "Geometry/cerv5.stl",
      "Geometry/cerv4.stl",
      "Geometry/cerv3.stl",
      "Geometry/cerv2.stl",
      "Geometry/cerv1.stl",
      "Geometry/jaw.stl",
      "Geometry/skull.stl",
      "Geometry/Rib1R.obj",
      "Geometry/Sternum.obj",
      "Geometry/Rib1L.obj",
      "Geometry/Rib2R.obj",
      "Geometry/Rib2L.obj",
      "Geometry/Rib3R.obj",
      "Geometry/Rib3L.obj",
      "Geometry/Rib4R.obj",
      "Geometry/Rib4L.obj",
      "Geometry/Rib5R.obj",
      "Geometry/Rib5L.obj",
      "Geometry/Rib6R.obj",
      "Geometry/Rib6L.obj",
      "Geometry/Rib7R.obj",
      "Geometry/Rib7L.obj",
      "Geometry/Rib8R.obj",
      "Geometry/Rib8L.obj",
      "Geometry/Rib9R.obj",
      "Geometry/Rib9L.obj",
      "Geometry/Rib10R.obj",
      "Geometry/Rib10L.obj",
      "Geometry/Rib11R.obj",
      "Geometry/Rib11L.obj",
      "Geometry/Rib12R.obj",
      "Geometry/Rib12L.obj",
      "Geometry/clavicle.stl",
      "Geometry/scapula.stl",
      "Geometry/humerus.stl",
      "Geometry/ulna.stl",
      "Geometry/radius.stl",
      "Geometry/hand_lunate.stl",
      "Geometry/sdfastSCAPHOIDw.stl",
      "Geometry/sdfastPISIFORMw.stl",
      "Geometry/sdfastTRIQUETRALw.stl",
      "Geometry/sdfast_1seg_hand_fr_c_5mc.stl",
      "Geometry/sdfast_1seg_hand_fr_c_4mc.stl",
      "Geometry/sdfast_1seg_hand_fr_c_3mc.stl",
      "Geometry/sdfast_1seg_hand_fr_c_2mc.stl",
      "Geometry/sdfast_1seg_hand_fr_c_trapezium.stl",
      "Geometry/sdfast_1seg_hand_fr_c_trapezoid.stl",
      "Geometry/sdfast_1seg_hand_fr_c_hamate.stl",
      "Geometry/hand_capitate.stl",
      "Geometry/hand_2proxph.stl",
      "Geometry/hand_2midph.stl",
      "Geometry/hand_2distph.stl",
      "Geometry/hand_3proxph.stl",
      "Geometry/hand_3midph.stl",
      "Geometry/hand_3distph.stl",
      "Geometry/hand_4proxph.stl",
      "Geometry/hand_4midph.stl",
      "Geometry/hand_4distph.stl",
      "Geometry/hand_5proxph.stl",
      "Geometry/hand_5midph.stl",
      "Geometry/hand_5distph.stl",
      "Geometry/hand_thumbprox.stl",
      "Geometry/hand_thumbdist.stl",
      "Geometry/hand_1mc.stl",
      "Geometry/clavicle_mirror.stl",
      "Geometry/scapula_mirror.stl",
      "Geometry/humerus_mirror.stl",
      "Geometry/ulna_mirror.stl",
      "Geometry/radius_mirror.stl",
      "Geometry/hand_lunate_mirror.stl",
      "Geometry/sdfastSCAPHOIDw_mirror.stl",
      "Geometry/sdfastPISIFORMw_mirror.stl",
      "Geometry/sdfastTRIQUETRALw_mirror.stl",
      "Geometry/sdfast_1seg_hand_fr_c_5mc_mirror.stl",
      "Geometry/sdfast_1seg_hand_fr_c_4mc_mirror.stl",
      "Geometry/sdfast_1seg_hand_fr_c_3mc_mirror.stl",
      "Geometry/sdfast_1seg_hand_fr_c_2mc_mirror.stl",
      "Geometry/sdfast_1seg_hand_fr_c_trapezium_mirror.stl",
      "Geometry/sdfast_1seg_hand_fr_c_trapezoid_mirror.stl",
      "Geometry/sdfast_1seg_hand_fr_c_hamate_mirror.stl",
      "Geometry/hand_capitate_mirror.stl",
      "Geometry/hand_2proxph_mirror.stl",
      "Geometry/hand_2midph_mirror.stl",
      "Geometry/hand_2distph_mirror.stl",
      "Geometry/hand_3proxph_mirror.stl",
      "Geometry/hand_3midph_mirror.stl",
      "Geometry/hand_3distph_mirror.stl",
      "Geometry/hand_4proxph_mirror.stl",
      "Geometry/hand_4midph_mirror.stl",
      "Geometry/hand_4distph_mirror.stl",
      "Geometry/hand_5proxph_mirror.stl",
      "Geometry/hand_5midph_mirror.stl",
      "Geometry/hand_5distph_mirror.stl",
      "Geometry/hand_thumbprox_mirror.stl",
      "Geometry/hand_thumbdist_mirror.stl",
      "Geometry/hand_1mc_mirror.stl",
      "Geometry/lunate.stl",
      "Geometry/scaphoid.stl",
      "Geometry/pisiform.stl",
      "Geometry/triquetral.stl",
      "Geometry/capitate.stl",
      "Geometry/trapezium.stl",
      "Geometry/1mc.stl",
      "Geometry/thumbprox.stl",
      "Geometry/thumbdist.stl",
      "Geometry/trapezoid.stl",
      "Geometry/hamate.stl",
      "Geometry/2mc.stl",
      "Geometry/2proxph.stl",
      "Geometry/2midph.stl",
      "Geometry/2distph.stl",
      "Geometry/3mc.stl",
      "Geometry/3proxph.stl",
      "Geometry/3midph.stl",
      "Geometry/3distph.stl",
      "Geometry/4mc_new.stl",
      "Geometry/4proxph_new.stl",
      "Geometry/4midph_new.stl",
      "Geometry/4distph_new.stl",
      "Geometry/5mc_new.stl",
      "Geometry/5proxph_new.stl",
      "Geometry/5midph_new.stl",
      "Geometry/5distph_new.stl",
      "Geometry/lunate_mirror.obj",
      "Geometry/scaphoid_mirror.obj",
      "Geometry/pisiform_mirror.obj",
      "Geometry/triquetral_mirror.obj",
      "Geometry/capitate_mirror.obj",
      "Geometry/trapezium_mirror.obj",
      "Geometry/1mc_mirror.obj",
      "Geometry/thumbprox_mirror.obj",
      "Geometry/thumbdist_mirror.obj",
      "Geometry/trapezoid_mirror.obj",
      "Geometry/hamate_mirror.obj",
      "Geometry/2mc_mirror.obj",
      "Geometry/2proxph_mirror.obj",
      "Geometry/2midph_mirror.obj",
      "Geometry/2distph_mirror.obj",
      "Geometry/3mc_mirror.obj",
      "Geometry/3proxph_mirror.obj",
      "Geometry/3midph_mirror.obj",
      "Geometry/3distph_mirror.obj",
      "Geometry/4mc_new_mirror.obj",
      "Geometry/4proxph_new_mirror.obj",
      "Geometry/4midph_new_mirror.obj",
      "Geometry/4distph_new_mirror.obj",
      "Geometry/5mc_new_mirror.obj",
      "Geometry/5proxph_new_mirror.obj",
      "Geometry/5midph_new_mirror.obj",
      "Geometry/5distph_new_mirror.obj",
      "Asset/marble.png",
      "Geometry/waterbottle/waterbottle.stl",
      "Geometry/waterbottle/waterbottle_contact0.stl",
      "Geometry/waterbottle/waterbottle_contact1.stl"
    ],
    "registration": {
      "translation": [
        0.0,
        0.0,
        0.94
      ],
      "rotation": [
        [
          0.9999999999999998,
          0.0,
          0.0
        ],
        [
          0.0,
          0.0,
          -0.9999999999999998
        ],
        [
          0.0,
          0.9999999999999998,
          0.0
        ]
      ]
    },
    "compiler_warnings": [],
    "limit_semantics": "Effort from supported scalar actuator envelopes; force from joint caps or supported envelopes; velocity unavailable unless explicitly represented"
  },
  "S": {
    "geometry_stripped": false,
    "missing_explicit_inertials": [
      "proximal_row",
      "capitate",
      "trapezium",
      "firstmc",
      "proximal_thumb",
      "distal_thumb",
      "trapezoid",
      "hamate",
      "secondmc",
      "2proxph",
      "2midph",
      "2distph",
      "thirdmc",
      "3proxph",
      "3midph",
      "3distph",
      "fourthmc",
      "4proxph",
      "4midph",
      "4distph",
      "fifthmc",
      "5proxph",
      "5midph",
      "5distph",
      "proximal_row_l",
      "capitate_l",
      "trapezium_l",
      "firstmc_l",
      "proximal_thumb_l",
      "distal_thumb_l",
      "trapezoid_l",
      "hamate_l",
      "secondmc_l",
      "2proxph_l",
      "2midph_l",
      "2distph_l",
      "thirdmc_l",
      "3proxph_l",
      "3midph_l",
      "3distph_l",
      "fourthmc_l",
      "4proxph_l",
      "4midph_l",
      "4distph_l",
      "fifthmc_l",
      "5proxph_l",
      "5midph_l",
      "5distph_l",
      "rib1_R",
      "rib1_L",
      "rib2_R",
      "rib2_L",
      "rib3_R",
      "rib3_L",
      "rib4_R",
      "rib4_L",
      "rib5_R",
      "rib5_L",
      "rib6_R",
      "rib6_L",
      "rib7_R",
      "rib7_L",
      "rib8_R",
      "rib8_L",
      "rib9_R",
      "rib9_L",
      "rib10_R",
      "rib10_L",
      "rib11_R",
      "rib11_L",
      "rib12_R",
      "rib12_L",
      "waterbottle",
      "target",
      "table"
    ],
    "assets_loaded": 190,
    "mesh_conversions": [],
    "nonphysical_normalizations": [],
    "xacro_arguments": {},
    "source_dependencies": [
      "Asset/Asset_Lowerbody.xml",
      "Asset/Asset_Others.xml",
      "Asset/Asset_Torso.xml",
      "Asset/Asset_Upperbody.xml",
      "Body_Manipulation/Body_Arm_Hand_Vis_l.xml",
      "Body_Manipulation/Body_Arm_Hand_r.xml",
      "Body_Manipulation/Body_Leg_Foot_Vis_l.xml",
      "Body_Manipulation/Body_Leg_Foot_Vis_r.xml",
      "Body_Manipulation/Body_Torso_Unimanual.xml",
      "Body_Manipulation/Body_Waterbottle.xml",
      "Contact/Contact_Upperbody.xml",
      "Equality/Equality_Upperbody_r.xml",
      "MS-Human-700-Manipulation.xml",
      "Muscle/Muscle_Arm_Hand_r.xml",
      "Tendon/Tendon_Arm_Hand_l.xml",
      "Tendon/Tendon_Arm_Hand_r.xml",
      "Tendon/Tendon_Leg_l.xml",
      "Tendon/Tendon_Leg_r.xml",
      "Tendon/Tendon_Torso.xml",
      "Geometry/sacrum.stl",
      "Geometry/r_pelvis.stl",
      "Geometry/l_pelvis.stl",
      "Geometry/r_femur.stl",
      "Geometry/r_tibia.stl",
      "Geometry/r_fibula.stl",
      "Geometry/r_talus.stl",
      "Geometry/r_foot.stl",
      "Geometry/r_bofoot.stl",
      "Geometry/r_patella.stl",
      "Geometry/l_femur.stl",
      "Geometry/l_tibia.stl",
      "Geometry/l_fibula.stl",
      "Geometry/l_talus.stl",
      "Geometry/l_foot.stl",
      "Geometry/l_bofoot.stl",
      "Geometry/l_patella.stl",
      "Geometry/lumbar5.stl",
      "Geometry/lumbar4.stl",
      "Geometry/lumbar3.stl",
      "Geometry/lumbar2.stl",
      "Geometry/lumbar1.stl",
      "Geometry/thoracic12.stl",
      "Geometry/thoracic11.stl",
      "Geometry/thoracic10.stl",
      "Geometry/thoracic9.stl",
      "Geometry/thoracic8.stl",
      "Geometry/thoracic7.stl",
      "Geometry/thoracic6.stl",
      "Geometry/thoracic5.stl",
      "Geometry/thoracic4.stl",
      "Geometry/thoracic3.stl",
      "Geometry/thoracic2.stl",
      "Geometry/thoracic1.stl",
      "Geometry/rotatedcerv7.stl",
      "Geometry/cerv6.stl",
      "Geometry/cerv5.stl",
      "Geometry/cerv4.stl",
      "Geometry/cerv3.stl",
      "Geometry/cerv2.stl",
      "Geometry/cerv1.stl",
      "Geometry/jaw.stl",
      "Geometry/skull.stl",
      "Geometry/Rib1R.obj",
      "Geometry/Sternum.obj",
      "Geometry/Rib1L.obj",
      "Geometry/Rib2R.obj",
      "Geometry/Rib2L.obj",
      "Geometry/Rib3R.obj",
      "Geometry/Rib3L.obj",
      "Geometry/Rib4R.obj",
      "Geometry/Rib4L.obj",
      "Geometry/Rib5R.obj",
      "Geometry/Rib5L.obj",
      "Geometry/Rib6R.obj",
      "Geometry/Rib6L.obj",
      "Geometry/Rib7R.obj",
      "Geometry/Rib7L.obj",
      "Geometry/Rib8R.obj",
      "Geometry/Rib8L.obj",
      "Geometry/Rib9R.obj",
      "Geometry/Rib9L.obj",
      "Geometry/Rib10R.obj",
      "Geometry/Rib10L.obj",
      "Geometry/Rib11R.obj",
      "Geometry/Rib11L.obj",
      "Geometry/Rib12R.obj",
      "Geometry/Rib12L.obj",
      "Geometry/clavicle.stl",
      "Geometry/scapula.stl",
      "Geometry/humerus.stl",
      "Geometry/ulna.stl",
      "Geometry/radius.stl",
      "Geometry/hand_lunate.stl",
      "Geometry/sdfastSCAPHOIDw.stl",
      "Geometry/sdfastPISIFORMw.stl",
      "Geometry/sdfastTRIQUETRALw.stl",
      "Geometry/sdfast_1seg_hand_fr_c_5mc.stl",
      "Geometry/sdfast_1seg_hand_fr_c_4mc.stl",
      "Geometry/sdfast_1seg_hand_fr_c_3mc.stl",
      "Geometry/sdfast_1seg_hand_fr_c_2mc.stl",
      "Geometry/sdfast_1seg_hand_fr_c_trapezium.stl",
      "Geometry/sdfast_1seg_hand_fr_c_trapezoid.stl",
      "Geometry/sdfast_1seg_hand_fr_c_hamate.stl",
      "Geometry/hand_capitate.stl",
      "Geometry/hand_2proxph.stl",
      "Geometry/hand_2midph.stl",
      "Geometry/hand_2distph.stl",
      "Geometry/hand_3proxph.stl",
      "Geometry/hand_3midph.stl",
      "Geometry/hand_3distph.stl",
      "Geometry/hand_4proxph.stl",
      "Geometry/hand_4midph.stl",
      "Geometry/hand_4distph.stl",
      "Geometry/hand_5proxph.stl",
      "Geometry/hand_5midph.stl",
      "Geometry/hand_5distph.stl",
      "Geometry/hand_thumbprox.stl",
      "Geometry/hand_thumbdist.stl",
      "Geometry/hand_1mc.stl",
      "Geometry/clavicle_mirror.stl",
      "Geometry/scapula_mirror.stl",
      "Geometry/humerus_mirror.stl",
      "Geometry/ulna_mirror.stl",
      "Geometry/radius_mirror.stl",
      "Geometry/hand_lunate_mirror.stl",
      "Geometry/sdfastSCAPHOIDw_mirror.stl",
      "Geometry/sdfastPISIFORMw_mirror.stl",
      "Geometry/sdfastTRIQUETRALw_mirror.stl",
      "Geometry/sdfast_1seg_hand_fr_c_5mc_mirror.stl",
      "Geometry/sdfast_1seg_hand_fr_c_4mc_mirror.stl",
      "Geometry/sdfast_1seg_hand_fr_c_3mc_mirror.stl",
      "Geometry/sdfast_1seg_hand_fr_c_2mc_mirror.stl",
      "Geometry/sdfast_1seg_hand_fr_c_trapezium_mirror.stl",
      "Geometry/sdfast_1seg_hand_fr_c_trapezoid_mirror.stl",
      "Geometry/sdfast_1seg_hand_fr_c_hamate_mirror.stl",
      "Geometry/hand_capitate_mirror.stl",
      "Geometry/hand_2proxph_mirror.stl",
      "Geometry/hand_2midph_mirror.stl",
      "Geometry/hand_2distph_mirror.stl",
      "Geometry/hand_3proxph_mirror.stl",
      "Geometry/hand_3midph_mirror.stl",
      "Geometry/hand_3distph_mirror.stl",
      "Geometry/hand_4proxph_mirror.stl",
      "Geometry/hand_4midph_mirror.stl",
      "Geometry/hand_4distph_mirror.stl",
      "Geometry/hand_5proxph_mirror.stl",
      "Geometry/hand_5midph_mirror.stl",
      "Geometry/hand_5distph_mirror.stl",
      "Geometry/hand_thumbprox_mirror.stl",
      "Geometry/hand_thumbdist_mirror.stl",
      "Geometry/hand_1mc_mirror.stl",
      "Geometry/lunate.stl",
      "Geometry/scaphoid.stl",
      "Geometry/pisiform.stl",
      "Geometry/triquetral.stl",
      "Geometry/capitate.stl",
      "Geometry/trapezium.stl",
      "Geometry/1mc.stl",
      "Geometry/thumbprox.stl",
      "Geometry/thumbdist.stl",
      "Geometry/trapezoid.stl",
      "Geometry/hamate.stl",
      "Geometry/2mc.stl",
      "Geometry/2proxph.stl",
      "Geometry/2midph.stl",
      "Geometry/2distph.stl",
      "Geometry/3mc.stl",
      "Geometry/3proxph.stl",
      "Geometry/3midph.stl",
      "Geometry/3distph.stl",
      "Geometry/4mc_new.stl",
      "Geometry/4proxph_new.stl",
      "Geometry/4midph_new.stl",
      "Geometry/4distph_new.stl",
      "Geometry/5mc_new.stl",
      "Geometry/5proxph_new.stl",
      "Geometry/5midph_new.stl",
      "Geometry/5distph_new.stl",
      "Geometry/lunate_mirror.obj",
      "Geometry/scaphoid_mirror.obj",
      "Geometry/pisiform_mirror.obj",
      "Geometry/triquetral_mirror.obj",
      "Geometry/capitate_mirror.obj",
      "Geometry/trapezium_mirror.obj",
      "Geometry/1mc_mirror.obj",
      "Geometry/thumbprox_mirror.obj",
      "Geometry/thumbdist_mirror.obj",
      "Geometry/trapezoid_mirror.obj",
      "Geometry/hamate_mirror.obj",
      "Geometry/2mc_mirror.obj",
      "Geometry/2proxph_mirror.obj",
      "Geometry/2midph_mirror.obj",
      "Geometry/2distph_mirror.obj",
      "Geometry/3mc_mirror.obj",
      "Geometry/3proxph_mirror.obj",
      "Geometry/3midph_mirror.obj",
      "Geometry/3distph_mirror.obj",
      "Geometry/4mc_new_mirror.obj",
      "Geometry/4proxph_new_mirror.obj",
      "Geometry/4midph_new_mirror.obj",
      "Geometry/4distph_new_mirror.obj",
      "Geometry/5mc_new_mirror.obj",
      "Geometry/5proxph_new_mirror.obj",
      "Geometry/5midph_new_mirror.obj",
      "Geometry/5distph_new_mirror.obj",
      "Asset/marble.png",
      "Geometry/waterbottle/waterbottle.stl",
      "Geometry/waterbottle/waterbottle_contact0.stl",
      "Geometry/waterbottle/waterbottle_contact1.stl"
    ],
    "registration": {
      "translation": [
        0.0,
        0.0,
        0.94
      ],
      "rotation": [
        [
          0.9999999999999998,
          0.0,
          0.0
        ],
        [
          0.0,
          0.0,
          -0.9999999999999998
        ],
        [
          0.0,
          0.9999999999999998,
          0.0
        ]
      ]
    },
    "compiler_warnings": [],
    "limit_semantics": "Effort from supported scalar actuator envelopes; force from joint caps or supported envelopes; velocity unavailable unless explicitly represented"
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
  "historical_snapshots_reused": 1,
  "primary_physics_unchanged": true,
  "source_matching": "original raw-value provenance criteria retained; kinematic guard applies to reported CoM"
}
```
