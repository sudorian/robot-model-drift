# flybody

Status: **complete**. Provenance: **pinned**, confidence **high**.

Source selected using the ordered amended provenance rules.

M: `https://github.com/google-deepmind/mujoco_menagerie`, `flybody/fruitfly.xml`, commit `370c43965323c0944b433b202aac5058b5f907a9`.
H: `https://github.com/TuragaLab/flybody`, `flybody/fruitfly/assets/fruitfly.xml`, commit `d015e9bfe441bd90ae431bac24c55cb74bdbce26`.
S: `736608121847c3c025fd02a629bdb016a3294f9a` (2024-03-29T20:14:40-04:00). Menagerie release/change: 2024-04-19T13:03:27-07:00.

Limit semantics: MJCF effort values are supported actuator torque/force envelopes. URDF effort and velocity values are manufacturer declarations retained from XML; MuJoCo does not enforce those tags. Such declaration comparisons are explicitly distinct from compiled inertial/range quantities.


## Source evidence

```json
[
  {
    "url": "https://github.com/TuragaLab/flybody",
    "document": "flybody/README.md",
    "commit": "370c43965323c0944b433b202aac5058b5f907a9",
    "current": true
  },
  {
    "url": "https://github.com/TuragaLab/flybody/blob/main/flybody/fruitfly/build_fruitfly/README.md",
    "document": "flybody/README.md",
    "commit": "370c43965323c0944b433b202aac5058b5f907a9",
    "current": true
  },
  {
    "url": "https://github.com/TuragaLab/flybody/commit/736608121847c3c025fd02a629bdb016a3294f9a",
    "document": "flybody/README.md",
    "commit": "370c43965323c0944b433b202aac5058b5f907a9",
    "current": true
  },
  {
    "url": "https://github.com/TuragaLab/flybody/tree/main/flybody/fruitfly/build_fruitfly",
    "document": "flybody/README.md",
    "commit": "370c43965323c0944b433b202aac5058b5f907a9",
    "current": true
  }
]
```


## Kinematics consistency

A proper Kabsch rigid transform aligns all matched zero-pose body origins. The maximum per-origin residual and signed hinge/slide axis angles determine whether CoM can be compared; RMS is also recorded. Fewer than three non-collinear origins give insufficient kinematic coverage. CoM records that fail either required M/H or M/S check are excluded from counts and largest discrepancies. Masses, principal moments and raw joint ranges remain unchanged; a flagged range still requires convention review.

| Pair | Status | Origins / rank | RMS / maximum mm | Disagreeing / checked axes |
|---|---|---:|---:|---:|
| M/H | consistent | 67 / 3 | 6.35466876e-14 / 1.28369537e-13 | 0 / 102 |
| M/S | consistent | 67 / 3 | 6.35466876e-14 / 1.28369537e-13 | 0 / 102 |

Exact fitted transforms, per-origin residuals, thresholds and axis vectors:

```json
{
  "M/H": {
    "status": "consistent",
    "matched_body_origins": 67,
    "position_threshold_m": 0.005,
    "axis_threshold_rad": 0.005,
    "residual_definition": "maximum Euclidean residual over matched body origins; Kabsch minimizes RMS, which is also recorded",
    "coordinate_frames": "each snapshot registered to its matched report anchor",
    "anchor_m": "thorax",
    "anchor_other": "thorax",
    "rotation_other_to_m": [
      [
        1.0000000000000002,
        2.0933677313570685e-18,
        1.1266262308749278e-17
      ],
      [
        -1.0131445798261423e-17,
        1.0,
        2.2579105666728496e-16
      ],
      [
        3.469446951953614e-18,
        -7.717351063751821e-16,
        1.0
      ]
    ],
    "translation_other_to_m": [
      3.469446951953614e-18,
      1.3674499900473425e-17,
      0.0
    ],
    "rms_residual_m": 6.354668759377765e-17,
    "max_residual_m": 1.2836953722228372e-16,
    "fit_rank": 3,
    "axis_checks": [
      {
        "joint_m": "head_abduct",
        "joint_other": "head_abduct",
        "axis_m": [
          0.24411389103728615,
          -5.3282905872842995e-19,
          0.9697465690594816
        ],
        "axis_other_aligned": [
          0.2441138910372862,
          2.159540468130392e-16,
          0.9697465690594816
        ],
        "angle_rad": 2.234906157666082e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "head_twist",
        "joint_other": "head_twist",
        "axis_m": [
          0.9697465690594816,
          2.220446049250314e-16,
          -0.24411389103728623
        ],
        "axis_other_aligned": [
          0.9697465690594816,
          1.5710093671808391e-16,
          -0.24411389103728617
        ],
        "angle_rad": 8.543516811707964e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "head",
        "joint_other": "head",
        "axis_m": [
          2.2204460492503136e-16,
          -1.0,
          5.3282905872843e-19
        ],
        "axis_other_aligned": [
          2.1995123719367434e-16,
          -1.0,
          7.722679354339105e-16
        ],
        "angle_rad": 7.717379455491173e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "rostrum",
        "joint_other": "rostrum",
        "axis_m": [
          -4.2663997490421945e-07,
          0.9999999999998738,
          2.65212952625248e-07
        ],
        "axis_other_aligned": [
          -4.2663997490212617e-07,
          0.9999999999998738,
          2.652129518535129e-07
        ],
        "angle_rad": 7.717379453196546e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "haustellum_abduct",
        "joint_other": "haustellum_abduct",
        "axis_m": [
          0.5385389065472009,
          -4.4794945554231175e-07,
          0.8426006445136063
        ],
        "axis_other_aligned": [
          0.5385389065472009,
          -4.4794945535751616e-07,
          0.8426006445136062
        ],
        "angle_rad": 2.1558141646208078e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "haustellum",
        "joint_other": "haustellum",
        "axis_m": [
          -9.500167585940747e-08,
          -0.9999999999998846,
          -4.7090796726602347e-07
        ],
        "axis_other_aligned": [
          -9.500167586150086e-08,
          -0.9999999999998846,
          -4.7090796649428836e-07
        ],
        "angle_rad": 7.717379456067849e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "labrum_left",
        "joint_other": "labrum_left",
        "axis_m": [
          0.8790101872450702,
          -0.09820906073223772,
          0.4665791155950707
        ],
        "axis_other_aligned": [
          0.8790101872450702,
          -0.09820906073223759,
          0.46657911559507065
        ],
        "angle_rad": 1.2412670766236366e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "labrum_right",
        "joint_other": "labrum_right",
        "axis_m": [
          -0.8530133323579225,
          0.0233971138936859,
          -0.5213643926095053
        ],
        "axis_other_aligned": [
          -0.8530133323579225,
          0.023397113893685786,
          -0.5213643926095052
        ],
        "angle_rad": 1.5824063492849165e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "antenna_abduct_left",
        "joint_other": "antenna_abduct_left",
        "axis_m": [
          0.9666141302172969,
          0.24632276471098843,
          0.07058483441500597
        ],
        "axis_other_aligned": [
          0.9666141302172969,
          0.2463227647109884,
          0.07058483441500578
        ],
        "angle_rad": 2.0137741281361153e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "antenna_twist_left",
        "joint_other": "antenna_twist_left",
        "axis_m": [
          -0.0028952045314268125,
          0.2859491565430624,
          -0.9582404174647573
        ],
        "axis_other_aligned": [
          -0.0028952045314268233,
          0.2859491565430622,
          -0.9582404174647575
        ],
        "angle_rad": 2.7775939287815005e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "antenna_left",
        "joint_other": "antenna_left",
        "axis_m": [
          0.2562201027534335,
          -0.9260443701343075,
          -0.2771156500228268
        ],
        "axis_other_aligned": [
          0.25622010275343354,
          -0.9260443701343077,
          -0.27711565002282607
        ],
        "angle_rad": 7.510691584075471e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "antenna_abduct_right",
        "joint_other": "antenna_abduct_right",
        "axis_m": [
          -0.9666141302172969,
          0.24632276471098835,
          -0.07058483441500575
        ],
        "axis_other_aligned": [
          -0.9666141302172969,
          0.24632276471098827,
          -0.07058483441500593
        ],
        "angle_rad": 2.0540180827887779e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "antenna_twist_right",
        "joint_other": "antenna_twist_right",
        "axis_m": [
          0.002895204531426857,
          0.28594915654306235,
          0.9582404174647574
        ],
        "axis_other_aligned": [
          0.0028952045314268693,
          0.28594915654306263,
          0.9582404174647573
        ],
        "angle_rad": 2.778344806292934e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "antenna_right",
        "joint_other": "antenna_right",
        "axis_m": [
          -0.25622010275343304,
          -0.9260443701343076,
          0.2771156500228266
        ],
        "axis_other_aligned": [
          -0.2562201027534331,
          -0.9260443701343074,
          0.27711565002282734
        ],
        "angle_rad": 7.488863730937846e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "wing_yaw_left",
        "joint_other": "wing_yaw_left",
        "axis_m": [
          0.7377600201673812,
          0.0,
          0.6750630730847492
        ],
        "axis_other_aligned": [
          0.7377600201673812,
          1.4494862893242004e-16,
          0.6750630730847491
        ],
        "angle_rad": 1.5521466728504744e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "wing_roll_left",
        "joint_other": "wing_roll_left",
        "axis_m": [
          -0.675063073084749,
          0.0,
          0.7377600201673814
        ],
        "axis_other_aligned": [
          -0.675063073084749,
          1.734189794558364e-16,
          0.7377600201673813
        ],
        "angle_rad": 1.8208687582174449e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "wing_pitch_left",
        "joint_other": "wing_pitch_left",
        "axis_m": [
          0.0,
          -1.0,
          0.0
        ],
        "axis_other_aligned": [
          -2.0933677313570685e-18,
          -1.0,
          7.717351063751821e-16
        ],
        "angle_rad": 7.717379455491173e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "wing_yaw_right",
        "joint_other": "wing_yaw_right",
        "axis_m": [
          -0.7377600201673814,
          0.0,
          -0.675063073084749
        ],
        "axis_other_aligned": [
          -0.7377600201673814,
          -1.4494862893241999e-16,
          -0.6750630730847489
        ],
        "angle_rad": 1.8258164385684197e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "wing_roll_right",
        "joint_other": "wing_roll_right",
        "axis_m": [
          0.6750630730847492,
          0.0,
          -0.7377600201673812
        ],
        "axis_other_aligned": [
          0.6750630730847492,
          -1.7341897945583638e-16,
          -0.7377600201673811
        ],
        "angle_rad": 1.8208687582174444e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "wing_pitch_right",
        "joint_other": "wing_pitch_right",
        "axis_m": [
          0.0,
          -1.0,
          0.0
        ],
        "axis_other_aligned": [
          -2.0933677313570685e-18,
          -1.0,
          7.717351063751821e-16
        ],
        "angle_rad": 7.717379455491173e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "abdomen_abduct",
        "joint_other": "abdomen_abduct",
        "axis_m": [
          0.24029730346049255,
          -0.001526786393565999,
          0.9706981378744498
        ],
        "axis_other_aligned": [
          0.2402973034604926,
          -0.0015267863935657822,
          0.9706981378744498
        ],
        "angle_rad": 2.2391728658487786e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "abdomen",
        "joint_other": "abdomen",
        "axis_m": [
          0.005717171218317164,
          0.9999836444307237,
          0.00015755731772261835
        ],
        "axis_other_aligned": [
          0.0057171712183171665,
          0.9999836444307237,
          0.00015755731772184664
        ],
        "angle_rad": 7.717250024977674e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "abdomen_abduct_2",
        "joint_other": "abdomen_abduct_2",
        "axis_m": [
          -0.1433813065006881,
          -0.00041777459898618323,
          0.989667432226877
        ],
        "axis_other_aligned": [
          -0.14338130650068812,
          -0.0004177745989859583,
          0.989667432226877
        ],
        "angle_rad": 2.2661773902229914e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "abdomen_2",
        "joint_other": "abdomen_2",
        "axis_m": [
          0.0028661746304406996,
          0.9999955419081754,
          0.0008373808945249356
        ],
        "axis_other_aligned": [
          0.0028661746304407022,
          0.9999955419081754,
          0.0008373808945241638
        ],
        "angle_rad": 7.717426693487776e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "abdomen_abduct_3",
        "joint_other": "abdomen_abduct_3",
        "axis_m": [
          -0.3201635806386771,
          0.0001621516447790372,
          0.947362261935457
        ],
        "axis_other_aligned": [
          -0.32016358063867717,
          0.00016215164477925438,
          0.947362261935457
        ],
        "angle_rad": 2.2413822617344993e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "abdomen_3",
        "joint_other": "abdomen_3",
        "axis_m": [
          0.001876288751271549,
          0.9999981326137026,
          0.0004629358805615286
        ],
        "axis_other_aligned": [
          0.0018762887512715515,
          0.9999981326137026,
          0.0004629358805607569
        ],
        "angle_rad": 7.717408539481911e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "abdomen_abduct_4",
        "joint_other": "abdomen_abduct_4",
        "axis_m": [
          -0.3823547221337876,
          0.0005988379327101619,
          0.9240154261997603
        ],
        "axis_other_aligned": [
          -0.38235472213378763,
          0.0005988379327103743,
          0.9240154261997602
        ],
        "angle_rad": 2.3972697030832225e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "abdomen_4",
        "joint_other": "abdomen_4",
        "axis_m": [
          0.002408635682517369,
          0.9999970384697133,
          0.00034860572534126615
        ],
        "axis_other_aligned": [
          0.0024086356825173717,
          0.9999970384697133,
          0.0003486057253404944
        ],
        "angle_rad": 7.717417339962948e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "abdomen_abduct_5",
        "joint_other": "abdomen_abduct_5",
        "axis_m": [
          -0.4493017867745893,
          0.0007004853791207976,
          0.8933797701545493
        ],
        "axis_other_aligned": [
          -0.4493017867745894,
          0.0007004853791210038,
          0.8933797701545492
        ],
        "angle_rad": 2.1360323740389975e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "abdomen_5",
        "joint_other": "abdomen_5",
        "axis_m": [
          0.0029642228302857463,
          0.9999953569706526,
          0.0007066966461413178
        ],
        "axis_other_aligned": [
          0.0029642228302857493,
          0.9999953569706526,
          0.0007066966461405461
        ],
        "angle_rad": 7.717444746643737e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "abdomen_abduct_6",
        "joint_other": "abdomen_abduct_6",
        "axis_m": [
          -0.5633647358681209,
          0.0014437776776368737,
          0.8262070502520903
        ],
        "axis_other_aligned": [
          -0.563364735868121,
          0.0014437776776370659,
          0.8262070502520903
        ],
        "angle_rad": 1.9984219612402395e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "abdomen_6",
        "joint_other": "abdomen_6",
        "axis_m": [
          0.003727295789724529,
          0.9999927383392677,
          0.0007940622323022701
        ],
        "axis_other_aligned": [
          0.003727295789724532,
          0.9999927383392677,
          0.0007940622323014984
        ],
        "angle_rad": 7.717464475479155e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "abdomen_abduct_7",
        "joint_other": "abdomen_abduct_7",
        "axis_m": [
          -0.71927727869623,
          0.0021638952480858213,
          0.6947197376703078
        ],
        "axis_other_aligned": [
          -0.71927727869623,
          0.0021638952480859852,
          0.6947197376703077
        ],
        "angle_rad": 1.981162247081252e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "abdomen_7",
        "joint_other": "abdomen_7",
        "axis_m": [
          0.0040108279595154625,
          0.9999914180176448,
          0.0010378584389755068
        ],
        "axis_other_aligned": [
          0.004010827959515465,
          0.9999914180176448,
          0.001037858438974735
        ],
        "angle_rad": 7.717457130624166e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "haltere_left",
        "joint_other": "haltere_left",
        "axis_m": [
          -0.7477324342301064,
          -0.08140466236689724,
          -0.6589912653026984
        ],
        "axis_other_aligned": [
          -0.7477324342301065,
          -0.08140466236689738,
          -0.6589912653026982
        ],
        "angle_rad": 2.161106224862407e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "haltere_right",
        "joint_other": "haltere_right",
        "axis_m": [
          0.758308906403606,
          -0.09627560577285599,
          0.6447469350078656
        ],
        "axis_other_aligned": [
          0.7583089064036059,
          -0.09627560577285582,
          0.6447469350078655
        ],
        "angle_rad": 1.5823112613210482e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "coxa_abduct_T1_left",
        "joint_other": "coxa_abduct_T1_left",
        "axis_m": [
          0.2949660567764698,
          0.8519198456970055,
          -0.4326980492876421
        ],
        "axis_other_aligned": [
          0.2949660567764698,
          0.8519198456970053,
          -0.4326980492876427
        ],
        "angle_rad": 6.353541660708337e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "coxa_twist_T1_left",
        "joint_other": "coxa_twist_T1_left",
        "axis_m": [
          -0.514065480937252,
          -0.24023527667369277,
          -0.8234219411396967
        ],
        "axis_other_aligned": [
          -0.5140654809372521,
          -0.24023527667369296,
          -0.8234219411396965
        ],
        "angle_rad": 3.0309546078301995e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "coxa_T1_left",
        "joint_other": "coxa_T1_left",
        "axis_m": [
          0.8054388286260429,
          -0.4653166538488653,
          -0.36708133293917755
        ],
        "axis_other_aligned": [
          0.8054388286260431,
          -0.46531665384886534,
          -0.36708133293917716
        ],
        "angle_rad": 4.379755957367586e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "femur_twist_T1_left",
        "joint_other": "femur_twist_T1_left",
        "axis_m": [
          0.5926392454383669,
          0.625148079653836,
          0.5079060969031228
        ],
        "axis_other_aligned": [
          0.592639245438367,
          0.6251480796538361,
          0.5079060969031224
        ],
        "angle_rad": 4.710277376051325e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "femur_T1_left",
        "joint_other": "femur_T1_left",
        "axis_m": [
          -0.805438828626043,
          0.46531665384886517,
          0.3670813329391775
        ],
        "axis_other_aligned": [
          -0.8054388286260432,
          0.4653166538488652,
          0.3670813329391771
        ],
        "angle_rad": 4.509747244882933e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "tibia_T1_left",
        "joint_other": "tibia_T1_left",
        "axis_m": [
          0.6812580219621415,
          -0.7314673940347922,
          0.029033755805622685
        ],
        "axis_other_aligned": [
          0.6812580219621416,
          -0.7314673940347922,
          0.02903375580562325
        ],
        "angle_rad": 5.7540544971738895e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "tarsus_T1_left",
        "joint_other": "tarsus_T1_left",
        "axis_m": [
          0.6135432754114323,
          -0.789641090695886,
          -0.005621128180635147
        ],
        "axis_other_aligned": [
          0.6135432754114324,
          -0.789641090695886,
          -0.0056211281806345355
        ],
        "angle_rad": 6.219183260247376e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "tarsus2_T1_left",
        "joint_other": "tarsus2_T1_left",
        "axis_m": [
          0.6135432754114323,
          -0.789641090695886,
          -0.005621128180635147
        ],
        "axis_other_aligned": [
          0.6135432754114324,
          -0.789641090695886,
          -0.0056211281806345355
        ],
        "angle_rad": 6.219183260247376e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "tarsus3_T1_left",
        "joint_other": "tarsus3_T1_left",
        "axis_m": [
          0.6135432754114323,
          -0.789641090695886,
          -0.005621128180635147
        ],
        "axis_other_aligned": [
          0.6135432754114324,
          -0.789641090695886,
          -0.0056211281806345355
        ],
        "angle_rad": 6.219183260247376e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "tarsus4_T1_left",
        "joint_other": "tarsus4_T1_left",
        "axis_m": [
          0.6135432754114323,
          -0.789641090695886,
          -0.005621128180635147
        ],
        "axis_other_aligned": [
          0.6135432754114324,
          -0.789641090695886,
          -0.0056211281806345355
        ],
        "angle_rad": 6.219183260247376e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "tarsus5_T1_left",
        "joint_other": "tarsus5_T1_left",
        "axis_m": [
          0.6135432754114323,
          -0.789641090695886,
          -0.005621128180635147
        ],
        "axis_other_aligned": [
          0.6135432754114324,
          -0.789641090695886,
          -0.0056211281806345355
        ],
        "angle_rad": 6.219183260247376e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "coxa_abduct_T1_right",
        "joint_other": "coxa_abduct_T1_right",
        "axis_m": [
          -0.36336085400715673,
          0.8364192471463129,
          0.41033124762609174
        ],
        "axis_other_aligned": [
          -0.36336085400715684,
          0.8364192471463131,
          0.41033124762609113
        ],
        "angle_rad": 6.707437923744493e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "coxa_twist_T1_right",
        "joint_other": "coxa_twist_T1_right",
        "axis_m": [
          0.4835575635207805,
          -0.2071447134318214,
          0.8504487935549648
        ],
        "axis_other_aligned": [
          0.4835575635207805,
          -0.20714471343182114,
          0.8504487935549647
        ],
        "angle_rad": 2.37549462997806e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "coxa_T1_right",
        "joint_other": "coxa_T1_right",
        "axis_m": [
          -0.7963296883433622,
          -0.5074385782540031,
          0.3291885732563021
        ],
        "axis_other_aligned": [
          -0.7963296883433623,
          -0.5074385782540028,
          0.32918857325630235
        ],
        "angle_rad": 3.387999773988764e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "femur_twist_T1_right",
        "joint_other": "femur_twist_T1_right",
        "axis_m": [
          -0.6007891463958077,
          0.6005096314058102,
          -0.5276746953965624
        ],
        "axis_other_aligned": [
          -0.6007891463958077,
          0.6005096314058099,
          -0.5276746953965628
        ],
        "angle_rad": 4.335559509131366e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "femur_T1_right",
        "joint_other": "femur_T1_right",
        "axis_m": [
          0.796329688343362,
          0.5074385782540032,
          -0.3291885732563022
        ],
        "axis_other_aligned": [
          0.796329688343362,
          0.507438578254003,
          -0.3291885732563025
        ],
        "angle_rad": 4.08865160135725e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "tibia_T1_right",
        "joint_other": "tibia_T1_right",
        "axis_m": [
          -0.6759535582690055,
          -0.7364519017854366,
          -0.02693294302678191
        ],
        "axis_other_aligned": [
          -0.6759535582690056,
          -0.7364519017854366,
          -0.026932943026781345
        ],
        "angle_rad": 5.804043602503624e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "tarsus_T1_right",
        "joint_other": "tarsus_T1_right",
        "axis_m": [
          -0.7689281250033315,
          -0.6356698520091335,
          -0.0683621081122247
        ],
        "axis_other_aligned": [
          -0.7689281250033315,
          -0.6356698520091334,
          -0.0683621081122242
        ],
        "angle_rad": 5.054449595385899e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "tarsus2_T1_right",
        "joint_other": "tarsus2_T1_right",
        "axis_m": [
          -0.7689281250033315,
          -0.6356698520091335,
          -0.0683621081122247
        ],
        "axis_other_aligned": [
          -0.7689281250033315,
          -0.6356698520091334,
          -0.0683621081122242
        ],
        "angle_rad": 5.054449595385899e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "tarsus3_T1_right",
        "joint_other": "tarsus3_T1_right",
        "axis_m": [
          -0.7689281250033315,
          -0.6356698520091335,
          -0.0683621081122247
        ],
        "axis_other_aligned": [
          -0.7689281250033315,
          -0.6356698520091334,
          -0.0683621081122242
        ],
        "angle_rad": 5.054449595385899e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "tarsus4_T1_right",
        "joint_other": "tarsus4_T1_right",
        "axis_m": [
          -0.7689281250033315,
          -0.6356698520091335,
          -0.0683621081122247
        ],
        "axis_other_aligned": [
          -0.7689281250033315,
          -0.6356698520091334,
          -0.0683621081122242
        ],
        "angle_rad": 5.054449595385899e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "tarsus5_T1_right",
        "joint_other": "tarsus5_T1_right",
        "axis_m": [
          -0.7689281250033315,
          -0.6356698520091335,
          -0.0683621081122247
        ],
        "axis_other_aligned": [
          -0.7689281250033315,
          -0.6356698520091334,
          -0.0683621081122242
        ],
        "angle_rad": 5.054449595385899e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "coxa_abduct_T2_left",
        "joint_other": "coxa_abduct_T2_left",
        "axis_m": [
          -0.03893764147142324,
          0.6988747831123311,
          -0.7141833781364108
        ],
        "axis_other_aligned": [
          -0.038937641471423236,
          0.6988747831123306,
          -0.714183378136411
        ],
        "angle_rad": 4.999857065771612e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "coxa_twist_T2_left",
        "joint_other": "coxa_twist_T2_left",
        "axis_m": [
          -0.2847649410049134,
          -0.6928489262967475,
          -0.6624721078686352
        ],
        "axis_other_aligned": [
          -0.2847649410049135,
          -0.6928489262967478,
          -0.6624721078686348
        ],
        "angle_rad": 4.972820174300705e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "coxa_T2_left",
        "joint_other": "coxa_T2_left",
        "axis_m": [
          0.9578062374254571,
          -0.17757928612069782,
          -0.22599293946880797
        ],
        "axis_other_aligned": [
          0.9578062374254571,
          -0.17757928612069784,
          -0.22599293946880777
        ],
        "angle_rad": 2.0062885096040707e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "femur_twist_T2_left",
        "joint_other": "femur_twist_T2_left",
        "axis_m": [
          0.26555407795775876,
          0.8475569923871896,
          0.4594868619836546
        ],
        "axis_other_aligned": [
          0.26555407795775887,
          0.8475569923871898,
          0.459486861983654
        ],
        "angle_rad": 6.521083742145178e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "femur_T2_left",
        "joint_other": "femur_T2_left",
        "axis_m": [
          -0.9578062374254572,
          0.17757928612069776,
          0.22599293946880789
        ],
        "axis_other_aligned": [
          -0.9578062374254572,
          0.1775792861206978,
          0.22599293946880772
        ],
        "angle_rad": 1.738881828270098e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "tibia_T2_left",
        "joint_other": "tibia_T2_left",
        "axis_m": [
          0.9384694602991496,
          -0.34510534608974985,
          -0.01331811496034316
        ],
        "axis_other_aligned": [
          0.9384694602991496,
          -0.3451053460897498,
          -0.013318114960342887
        ],
        "angle_rad": 2.7698732319435293e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "tarsus_T2_left",
        "joint_other": "tarsus_T2_left",
        "axis_m": [
          0.9830828373145147,
          -0.10869127394190793,
          0.14742571670685037
        ],
        "axis_other_aligned": [
          0.9830828373145147,
          -0.10869127394190789,
          0.14742571670685042
        ],
        "angle_rad": 7.076311083754595e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "tarsus2_T2_left",
        "joint_other": "tarsus2_T2_left",
        "axis_m": [
          0.9830828373145147,
          -0.10869127394190793,
          0.14742571670685037
        ],
        "axis_other_aligned": [
          0.9830828373145147,
          -0.10869127394190789,
          0.14742571670685042
        ],
        "angle_rad": 7.076311083754595e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "tarsus3_T2_left",
        "joint_other": "tarsus3_T2_left",
        "axis_m": [
          0.9830828373145147,
          -0.10869127394190793,
          0.14742571670685037
        ],
        "axis_other_aligned": [
          0.9830828373145147,
          -0.10869127394190789,
          0.14742571670685042
        ],
        "angle_rad": 7.076311083754595e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "tarsus4_T2_left",
        "joint_other": "tarsus4_T2_left",
        "axis_m": [
          0.9830828373145147,
          -0.10869127394190793,
          0.14742571670685037
        ],
        "axis_other_aligned": [
          0.9830828373145147,
          -0.10869127394190789,
          0.14742571670685042
        ],
        "angle_rad": 7.076311083754595e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "tarsus5_T2_left",
        "joint_other": "tarsus5_T2_left",
        "axis_m": [
          0.9830828373145147,
          -0.10869127394190793,
          0.14742571670685037
        ],
        "axis_other_aligned": [
          0.9830828373145147,
          -0.10869127394190789,
          0.14742571670685042
        ],
        "angle_rad": 7.076311083754595e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "coxa_abduct_T2_right",
        "joint_other": "coxa_abduct_T2_right",
        "axis_m": [
          0.035646688476469436,
          0.7031509535060095,
          0.7101464991001865
        ],
        "axis_other_aligned": [
          0.035646688476469464,
          0.7031509535060099,
          0.7101464991001861
        ],
        "angle_rad": 5.006232825943491e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "coxa_twist_T2_right",
        "joint_other": "coxa_twist_T2_right",
        "axis_m": [
          0.28391209943970647,
          -0.6884445341525965,
          0.6674114496973755
        ],
        "axis_other_aligned": [
          0.28391209943970647,
          -0.6884445341525963,
          0.667411449697376
        ],
        "angle_rad": 5.185169430563076e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "coxa_T2_right",
        "joint_other": "coxa_T2_right",
        "axis_m": [
          -0.958187472988663,
          -0.17782817543630036,
          0.22417383127518845
        ],
        "axis_other_aligned": [
          -0.958187472988663,
          -0.17782817543630025,
          0.22417383127518853
        ],
        "angle_rad": 1.3092278833360673e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "femur_twist_T2_right",
        "joint_other": "femur_twist_T2_right",
        "axis_m": [
          -0.2642496429364298,
          0.8504635747773598,
          -0.45484484627714944
        ],
        "axis_other_aligned": [
          -0.2642496429364298,
          0.8504635747773596,
          -0.45484484627715005
        ],
        "angle_rad": 6.318585897742262e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "femur_T2_right",
        "joint_other": "femur_T2_right",
        "axis_m": [
          0.958187472988663,
          0.17782817543630028,
          -0.2241738312751883
        ],
        "axis_other_aligned": [
          0.958187472988663,
          0.1778281754363002,
          -0.2241738312751884
        ],
        "angle_rad": 1.2276156489239667e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "tibia_T2_right",
        "joint_other": "tibia_T2_right",
        "axis_m": [
          -0.952664470676777,
          -0.3034154294651218,
          -0.019221952882896808
        ],
        "axis_other_aligned": [
          -0.952664470676777,
          -0.30341542946512173,
          -0.01922195288289657
        ],
        "angle_rad": 2.461168543934297e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "tarsus_T2_right",
        "joint_other": "tarsus_T2_right",
        "axis_m": [
          -0.9828333313510451,
          -0.1146220750719764,
          -0.14456978485008887
        ],
        "axis_other_aligned": [
          -0.9828333313510452,
          -0.1146220750719764,
          -0.14456978485008876
        ],
        "angle_rad": 1.1236938283130691e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "tarsus2_T2_right",
        "joint_other": "tarsus2_T2_right",
        "axis_m": [
          -0.9828333313510451,
          -0.1146220750719764,
          -0.14456978485008887
        ],
        "axis_other_aligned": [
          -0.9828333313510452,
          -0.1146220750719764,
          -0.14456978485008876
        ],
        "angle_rad": 1.1236938283130691e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "tarsus3_T2_right",
        "joint_other": "tarsus3_T2_right",
        "axis_m": [
          -0.9828333313510451,
          -0.1146220750719764,
          -0.14456978485008887
        ],
        "axis_other_aligned": [
          -0.9828333313510452,
          -0.1146220750719764,
          -0.14456978485008876
        ],
        "angle_rad": 1.1236938283130691e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "tarsus4_T2_right",
        "joint_other": "tarsus4_T2_right",
        "axis_m": [
          -0.9828333313510451,
          -0.1146220750719764,
          -0.14456978485008887
        ],
        "axis_other_aligned": [
          -0.9828333313510452,
          -0.1146220750719764,
          -0.14456978485008876
        ],
        "angle_rad": 1.1236938283130691e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "tarsus5_T2_right",
        "joint_other": "tarsus5_T2_right",
        "axis_m": [
          -0.9828333313510451,
          -0.1146220750719764,
          -0.14456978485008887
        ],
        "axis_other_aligned": [
          -0.9828333313510452,
          -0.1146220750719764,
          -0.14456978485008876
        ],
        "angle_rad": 1.1236938283130691e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "coxa_abduct_T3_left",
        "joint_other": "coxa_abduct_T3_left",
        "axis_m": [
          -0.6474104020187451,
          0.633039967650513,
          0.42440566762823106
        ],
        "axis_other_aligned": [
          -0.6474104020187452,
          0.6330399676505131,
          0.42440566762823057
        ],
        "angle_rad": 5.117875266520903e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "coxa_twist_T3_left",
        "joint_other": "coxa_twist_T3_left",
        "axis_m": [
          -0.5853202314654957,
          -0.05633939520659714,
          -0.8088424439808617
        ],
        "axis_other_aligned": [
          -0.5853202314654958,
          -0.056339395206597316,
          -0.8088424439808617
        ],
        "angle_rad": 1.993045536433795e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "coxa_T3_left",
        "joint_other": "coxa_T3_left",
        "axis_m": [
          0.4881188359355798,
          0.7720662354388984,
          -0.40700581089230414
        ],
        "axis_other_aligned": [
          0.4881188359355798,
          0.7720662354388981,
          -0.40700581089230464
        ],
        "angle_rad": 5.715222817774257e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "femur_twist_T3_left",
        "joint_other": "femur_twist_T3_left",
        "axis_m": [
          -0.5808430987048643,
          0.6354299955824776,
          0.5087730490120167
        ],
        "axis_other_aligned": [
          -0.5808430987048644,
          0.6354299955824777,
          0.5087730490120163
        ],
        "angle_rad": 4.710277376051325e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "femur_T3_left",
        "joint_other": "femur_T3_left",
        "axis_m": [
          -0.4881188359355799,
          -0.7720662354388984,
          0.4070058108923042
        ],
        "axis_other_aligned": [
          -0.4881188359355799,
          -0.7720662354388981,
          0.4070058108923047
        ],
        "angle_rad": 5.828670879282072e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "tibia_T3_left",
        "joint_other": "tibia_T3_left",
        "axis_m": [
          0.6727348461975776,
          0.7226234019472612,
          -0.15888123133236595
        ],
        "axis_other_aligned": [
          0.6727348461975776,
          0.722623401947261,
          -0.15888123133236648
        ],
        "angle_rad": 5.342497709481851e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "tarsus_T3_left",
        "joint_other": "tarsus_T3_left",
        "axis_m": [
          0.47978636236419925,
          0.8771654340067409,
          -0.019643010795076844
        ],
        "axis_other_aligned": [
          0.4797863623641993,
          0.8771654340067407,
          -0.019643010795077517
        ],
        "angle_rad": 6.835889108847827e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "tarsus2_T3_left",
        "joint_other": "tarsus2_T3_left",
        "axis_m": [
          0.47978636236419925,
          0.8771654340067409,
          -0.019643010795076844
        ],
        "axis_other_aligned": [
          0.4797863623641993,
          0.8771654340067407,
          -0.019643010795077517
        ],
        "angle_rad": 6.835889108847827e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "tarsus3_T3_left",
        "joint_other": "tarsus3_T3_left",
        "axis_m": [
          0.47978636236419925,
          0.8771654340067409,
          -0.019643010795076844
        ],
        "axis_other_aligned": [
          0.4797863623641993,
          0.8771654340067407,
          -0.019643010795077517
        ],
        "angle_rad": 6.835889108847827e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "tarsus4_T3_left",
        "joint_other": "tarsus4_T3_left",
        "axis_m": [
          0.47978636236419925,
          0.8771654340067409,
          -0.019643010795076844
        ],
        "axis_other_aligned": [
          0.4797863623641993,
          0.8771654340067407,
          -0.019643010795077517
        ],
        "angle_rad": 6.835889108847827e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "tarsus5_T3_left",
        "joint_other": "tarsus5_T3_left",
        "axis_m": [
          0.47978636236419925,
          0.8771654340067409,
          -0.019643010795076844
        ],
        "axis_other_aligned": [
          0.4797863623641993,
          0.8771654340067407,
          -0.019643010795077517
        ],
        "angle_rad": 6.835889108847827e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "coxa_abduct_T3_right",
        "joint_other": "coxa_abduct_T3_right",
        "axis_m": [
          0.6540247233925172,
          0.6322551000338703,
          -0.4153373925768088
        ],
        "axis_other_aligned": [
          0.654024723392517,
          0.63225510003387,
          -0.41533739257680924
        ],
        "angle_rad": 5.382005793715205e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "coxa_twist_T3_right",
        "joint_other": "coxa_twist_T3_right",
        "axis_m": [
          0.5882856267667127,
          -0.07992661678517708,
          0.8046935797363933
        ],
        "axis_other_aligned": [
          0.5882856267667128,
          -0.0799266167851769,
          0.8046935797363934
        ],
        "angle_rad": 1.9292121753525026e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "coxa_T3_right",
        "joint_other": "coxa_T3_right",
        "axis_m": [
          -0.47557510713980555,
          0.7706265142145293,
          0.4242205712345012
        ],
        "axis_other_aligned": [
          -0.4755751071398057,
          0.7706265142145295,
          0.42422057123450063
        ],
        "angle_rad": 6.473657049138937e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "femur_twist_T3_right",
        "joint_other": "femur_twist_T3_right",
        "axis_m": [
          0.5740415301876588,
          0.6372862694464577,
          -0.514142521480988
        ],
        "axis_other_aligned": [
          0.5740415301876588,
          0.6372862694464575,
          -0.5141425214809884
        ],
        "angle_rad": 4.335559509131367e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "femur_T3_right",
        "joint_other": "femur_T3_right",
        "axis_m": [
          0.47557510713980533,
          -0.7706265142145294,
          -0.4242205712345012
        ],
        "axis_other_aligned": [
          0.4755751071398055,
          -0.7706265142145297,
          -0.42422057123450063
        ],
        "angle_rad": 6.473657049138937e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "tibia_T3_right",
        "joint_other": "tibia_T3_right",
        "axis_m": [
          -0.6709506420385306,
          0.7230627444391755,
          0.16433351317418843
        ],
        "axis_other_aligned": [
          -0.6709506420385307,
          0.7230627444391755,
          0.16433351317418787
        ],
        "angle_rad": 5.703416235967739e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "tarsus_T3_right",
        "joint_other": "tarsus_T3_right",
        "axis_m": [
          -0.48369145144949144,
          0.8749144193497184,
          0.023818870851270806
        ],
        "axis_other_aligned": [
          -0.48369145144949155,
          0.8749144193497184,
          0.02381887085127013
        ],
        "angle_rad": 6.779285139611376e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "tarsus2_T3_right",
        "joint_other": "tarsus2_T3_right",
        "axis_m": [
          -0.48369145144949144,
          0.8749144193497184,
          0.023818870851270806
        ],
        "axis_other_aligned": [
          -0.48369145144949155,
          0.8749144193497184,
          0.02381887085127013
        ],
        "angle_rad": 6.779285139611376e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "tarsus3_T3_right",
        "joint_other": "tarsus3_T3_right",
        "axis_m": [
          -0.48369145144949144,
          0.8749144193497184,
          0.023818870851270806
        ],
        "axis_other_aligned": [
          -0.48369145144949155,
          0.8749144193497184,
          0.02381887085127013
        ],
        "angle_rad": 6.779285139611376e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "tarsus4_T3_right",
        "joint_other": "tarsus4_T3_right",
        "axis_m": [
          -0.48369145144949144,
          0.8749144193497184,
          0.023818870851270806
        ],
        "axis_other_aligned": [
          -0.48369145144949155,
          0.8749144193497184,
          0.02381887085127013
        ],
        "angle_rad": 6.779285139611376e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "tarsus5_T3_right",
        "joint_other": "tarsus5_T3_right",
        "axis_m": [
          -0.48369145144949144,
          0.8749144193497184,
          0.023818870851270806
        ],
        "axis_other_aligned": [
          -0.48369145144949155,
          0.8749144193497184,
          0.02381887085127013
        ],
        "angle_rad": 6.779285139611376e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      }
    ],
    "axis_disagreements": [],
    "com_eligible": true,
    "covariance_singular_values": [
      0.4790572719123735,
      0.3942342995019165,
      0.12726245349878376
    ],
    "origin_residuals_m": {
      "thorax": 1.4107764163058153e-17,
      "head": 1.8618168967019294e-17,
      "rostrum": 1.4728799896498942e-17,
      "haustellum": 2.122142710759789e-17,
      "labrum_left": 1.3985787785349405e-17,
      "labrum_right": 1.3985787785349405e-17,
      "antenna_left": 3.084593289525303e-17,
      "antenna_right": 3.109227384499446e-17,
      "wing_left": 3.5804289117824333e-17,
      "wing_right": 3.5804289117824333e-17,
      "abdomen": 1.6591127512380074e-17,
      "abdomen_2": 2.1051398297025365e-17,
      "abdomen_3": 2.068703487927255e-17,
      "abdomen_4": 3.081657532689489e-17,
      "abdomen_5": 3.00201172172477e-17,
      "abdomen_6": 2.932332211559956e-17,
      "abdomen_7": 2.8690415109637346e-17,
      "haltere_left": 2.281672496420498e-17,
      "haltere_right": 2.281672496420498e-17,
      "coxa_T1_left": 1.993045536433795e-17,
      "femur_T1_left": 1.4821483875836085e-17,
      "tibia_T1_left": 4.443059973708341e-17,
      "tarsus_T1_left": 5.721958498152797e-17,
      "tarsus2_T1_left": 5.887846720064156e-17,
      "tarsus3_T1_left": 7.211110073938365e-17,
      "tarsus4_T1_left": 7.211110073938365e-17,
      "claw_T1_left": 7.211110073938365e-17,
      "coxa_T1_right": 1.993045536433795e-17,
      "femur_T1_right": 1.4821483875836085e-17,
      "tibia_T1_right": 4.443059973708341e-17,
      "tarsus_T1_right": 5.721958498152797e-17,
      "tarsus2_T1_right": 5.887846720064156e-17,
      "tarsus3_T1_right": 7.211110073938365e-17,
      "tarsus4_T1_right": 7.211110073938365e-17,
      "claw_T1_right": 7.211110073938365e-17,
      "coxa_T2_left": 2.110382192020081e-17,
      "femur_T2_left": 6.938893903907228e-18,
      "tibia_T2_left": 6.068145509697911e-17,
      "tarsus_T2_left": 8.333897564733124e-17,
      "tarsus2_T2_left": 1.1464934308770758e-16,
      "tarsus3_T2_left": 1.1464934308770758e-16,
      "tarsus4_T2_left": 1.2813490069415586e-16,
      "claw_T2_left": 1.2836953722228372e-16,
      "coxa_T2_right": 2.110382192020081e-17,
      "femur_T2_right": 6.938893903907228e-18,
      "tibia_T2_right": 6.066459950017194e-17,
      "tarsus_T2_right": 8.333897564733124e-17,
      "tarsus2_T2_right": 1.1464934308770758e-16,
      "tarsus3_T2_right": 1.1464934308770758e-16,
      "tarsus4_T2_right": 1.2813490069415586e-16,
      "claw_T2_right": 1.2836953722228372e-16,
      "coxa_T3_left": 1.4304896245381992e-17,
      "femur_T3_left": 9.813077866773595e-18,
      "tibia_T3_left": 5.341145691818931e-17,
      "tarsus_T3_left": 6.206335383118183e-17,
      "tarsus2_T3_left": 7.601177430610147e-17,
      "tarsus3_T3_left": 7.601177430610147e-17,
      "tarsus4_T3_left": 8.886119947416683e-17,
      "claw_T3_left": 8.886119947416683e-17,
      "coxa_T3_right": 1.4304896245381992e-17,
      "femur_T3_right": 1.5515838457795457e-17,
      "tibia_T3_right": 4.7697009830883764e-17,
      "tarsus_T3_right": 6.206335383118183e-17,
      "tarsus2_T3_right": 7.601177430610147e-17,
      "tarsus3_T3_right": 7.601177430610147e-17,
      "tarsus4_T3_right": 8.886119947416683e-17,
      "claw_T3_right": 8.886119947416683e-17
    },
    "reason": "Unique proper rigid fit and matched signed axes meet the configured thresholds"
  },
  "M/S": {
    "status": "consistent",
    "matched_body_origins": 67,
    "position_threshold_m": 0.005,
    "axis_threshold_rad": 0.005,
    "residual_definition": "maximum Euclidean residual over matched body origins; Kabsch minimizes RMS, which is also recorded",
    "coordinate_frames": "each snapshot registered to its matched report anchor",
    "anchor_m": "thorax",
    "anchor_other": "thorax",
    "rotation_other_to_m": [
      [
        1.0000000000000002,
        2.0933677313570685e-18,
        1.1266262308749278e-17
      ],
      [
        -1.0131445798261423e-17,
        1.0,
        2.2579105666728496e-16
      ],
      [
        3.469446951953614e-18,
        -7.717351063751821e-16,
        1.0
      ]
    ],
    "translation_other_to_m": [
      3.469446951953614e-18,
      1.3674499900473425e-17,
      0.0
    ],
    "rms_residual_m": 6.354668759377765e-17,
    "max_residual_m": 1.2836953722228372e-16,
    "fit_rank": 3,
    "axis_checks": [
      {
        "joint_m": "head_abduct",
        "joint_other": "head_abduct",
        "axis_m": [
          0.24411389103728615,
          -5.3282905872842995e-19,
          0.9697465690594816
        ],
        "axis_other_aligned": [
          0.2441138910372862,
          2.159540468130392e-16,
          0.9697465690594816
        ],
        "angle_rad": 2.234906157666082e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "head_twist",
        "joint_other": "head_twist",
        "axis_m": [
          0.9697465690594816,
          2.220446049250314e-16,
          -0.24411389103728623
        ],
        "axis_other_aligned": [
          0.9697465690594816,
          1.5710093671808391e-16,
          -0.24411389103728617
        ],
        "angle_rad": 8.543516811707964e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "head",
        "joint_other": "head",
        "axis_m": [
          2.2204460492503136e-16,
          -1.0,
          5.3282905872843e-19
        ],
        "axis_other_aligned": [
          2.1995123719367434e-16,
          -1.0,
          7.722679354339105e-16
        ],
        "angle_rad": 7.717379455491173e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "rostrum",
        "joint_other": "rostrum",
        "axis_m": [
          -4.2663997490421945e-07,
          0.9999999999998738,
          2.65212952625248e-07
        ],
        "axis_other_aligned": [
          -4.2663997490212617e-07,
          0.9999999999998738,
          2.652129518535129e-07
        ],
        "angle_rad": 7.717379453196546e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "haustellum_abduct",
        "joint_other": "haustellum_abduct",
        "axis_m": [
          0.5385389065472009,
          -4.4794945554231175e-07,
          0.8426006445136063
        ],
        "axis_other_aligned": [
          0.5385389065472009,
          -4.4794945535751616e-07,
          0.8426006445136062
        ],
        "angle_rad": 2.1558141646208078e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "haustellum",
        "joint_other": "haustellum",
        "axis_m": [
          -9.500167585940747e-08,
          -0.9999999999998846,
          -4.7090796726602347e-07
        ],
        "axis_other_aligned": [
          -9.500167586150086e-08,
          -0.9999999999998846,
          -4.7090796649428836e-07
        ],
        "angle_rad": 7.717379456067849e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "labrum_left",
        "joint_other": "labrum_left",
        "axis_m": [
          0.8790101872450702,
          -0.09820906073223772,
          0.4665791155950707
        ],
        "axis_other_aligned": [
          0.8790101872450702,
          -0.09820906073223759,
          0.46657911559507065
        ],
        "angle_rad": 1.2412670766236366e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "labrum_right",
        "joint_other": "labrum_right",
        "axis_m": [
          -0.8530133323579225,
          0.0233971138936859,
          -0.5213643926095053
        ],
        "axis_other_aligned": [
          -0.8530133323579225,
          0.023397113893685786,
          -0.5213643926095052
        ],
        "angle_rad": 1.5824063492849165e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "antenna_abduct_left",
        "joint_other": "antenna_abduct_left",
        "axis_m": [
          0.9666141302172969,
          0.24632276471098843,
          0.07058483441500597
        ],
        "axis_other_aligned": [
          0.9666141302172969,
          0.2463227647109884,
          0.07058483441500578
        ],
        "angle_rad": 2.0137741281361153e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "antenna_twist_left",
        "joint_other": "antenna_twist_left",
        "axis_m": [
          -0.0028952045314268125,
          0.2859491565430624,
          -0.9582404174647573
        ],
        "axis_other_aligned": [
          -0.0028952045314268233,
          0.2859491565430622,
          -0.9582404174647575
        ],
        "angle_rad": 2.7775939287815005e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "antenna_left",
        "joint_other": "antenna_left",
        "axis_m": [
          0.2562201027534335,
          -0.9260443701343075,
          -0.2771156500228268
        ],
        "axis_other_aligned": [
          0.25622010275343354,
          -0.9260443701343077,
          -0.27711565002282607
        ],
        "angle_rad": 7.510691584075471e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "antenna_abduct_right",
        "joint_other": "antenna_abduct_right",
        "axis_m": [
          -0.9666141302172969,
          0.24632276471098835,
          -0.07058483441500575
        ],
        "axis_other_aligned": [
          -0.9666141302172969,
          0.24632276471098827,
          -0.07058483441500593
        ],
        "angle_rad": 2.0540180827887779e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "antenna_twist_right",
        "joint_other": "antenna_twist_right",
        "axis_m": [
          0.002895204531426857,
          0.28594915654306235,
          0.9582404174647574
        ],
        "axis_other_aligned": [
          0.0028952045314268693,
          0.28594915654306263,
          0.9582404174647573
        ],
        "angle_rad": 2.778344806292934e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "antenna_right",
        "joint_other": "antenna_right",
        "axis_m": [
          -0.25622010275343304,
          -0.9260443701343076,
          0.2771156500228266
        ],
        "axis_other_aligned": [
          -0.2562201027534331,
          -0.9260443701343074,
          0.27711565002282734
        ],
        "angle_rad": 7.488863730937846e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "wing_yaw_left",
        "joint_other": "wing_yaw_left",
        "axis_m": [
          0.7377600201673812,
          0.0,
          0.6750630730847492
        ],
        "axis_other_aligned": [
          0.7377600201673812,
          1.4494862893242004e-16,
          0.6750630730847491
        ],
        "angle_rad": 1.5521466728504744e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "wing_roll_left",
        "joint_other": "wing_roll_left",
        "axis_m": [
          -0.675063073084749,
          0.0,
          0.7377600201673814
        ],
        "axis_other_aligned": [
          -0.675063073084749,
          1.734189794558364e-16,
          0.7377600201673813
        ],
        "angle_rad": 1.8208687582174449e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "wing_pitch_left",
        "joint_other": "wing_pitch_left",
        "axis_m": [
          0.0,
          -1.0,
          0.0
        ],
        "axis_other_aligned": [
          -2.0933677313570685e-18,
          -1.0,
          7.717351063751821e-16
        ],
        "angle_rad": 7.717379455491173e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "wing_yaw_right",
        "joint_other": "wing_yaw_right",
        "axis_m": [
          -0.7377600201673814,
          0.0,
          -0.675063073084749
        ],
        "axis_other_aligned": [
          -0.7377600201673814,
          -1.4494862893241999e-16,
          -0.6750630730847489
        ],
        "angle_rad": 1.8258164385684197e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "wing_roll_right",
        "joint_other": "wing_roll_right",
        "axis_m": [
          0.6750630730847492,
          0.0,
          -0.7377600201673812
        ],
        "axis_other_aligned": [
          0.6750630730847492,
          -1.7341897945583638e-16,
          -0.7377600201673811
        ],
        "angle_rad": 1.8208687582174444e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "wing_pitch_right",
        "joint_other": "wing_pitch_right",
        "axis_m": [
          0.0,
          -1.0,
          0.0
        ],
        "axis_other_aligned": [
          -2.0933677313570685e-18,
          -1.0,
          7.717351063751821e-16
        ],
        "angle_rad": 7.717379455491173e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "abdomen_abduct",
        "joint_other": "abdomen_abduct",
        "axis_m": [
          0.24029730346049255,
          -0.001526786393565999,
          0.9706981378744498
        ],
        "axis_other_aligned": [
          0.2402973034604926,
          -0.0015267863935657822,
          0.9706981378744498
        ],
        "angle_rad": 2.2391728658487786e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "abdomen",
        "joint_other": "abdomen",
        "axis_m": [
          0.005717171218317164,
          0.9999836444307237,
          0.00015755731772261835
        ],
        "axis_other_aligned": [
          0.0057171712183171665,
          0.9999836444307237,
          0.00015755731772184664
        ],
        "angle_rad": 7.717250024977674e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "abdomen_abduct_2",
        "joint_other": "abdomen_abduct_2",
        "axis_m": [
          -0.1433813065006881,
          -0.00041777459898618323,
          0.989667432226877
        ],
        "axis_other_aligned": [
          -0.14338130650068812,
          -0.0004177745989859583,
          0.989667432226877
        ],
        "angle_rad": 2.2661773902229914e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "abdomen_2",
        "joint_other": "abdomen_2",
        "axis_m": [
          0.0028661746304406996,
          0.9999955419081754,
          0.0008373808945249356
        ],
        "axis_other_aligned": [
          0.0028661746304407022,
          0.9999955419081754,
          0.0008373808945241638
        ],
        "angle_rad": 7.717426693487776e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "abdomen_abduct_3",
        "joint_other": "abdomen_abduct_3",
        "axis_m": [
          -0.3201635806386771,
          0.0001621516447790372,
          0.947362261935457
        ],
        "axis_other_aligned": [
          -0.32016358063867717,
          0.00016215164477925438,
          0.947362261935457
        ],
        "angle_rad": 2.2413822617344993e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "abdomen_3",
        "joint_other": "abdomen_3",
        "axis_m": [
          0.001876288751271549,
          0.9999981326137026,
          0.0004629358805615286
        ],
        "axis_other_aligned": [
          0.0018762887512715515,
          0.9999981326137026,
          0.0004629358805607569
        ],
        "angle_rad": 7.717408539481911e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "abdomen_abduct_4",
        "joint_other": "abdomen_abduct_4",
        "axis_m": [
          -0.3823547221337876,
          0.0005988379327101619,
          0.9240154261997603
        ],
        "axis_other_aligned": [
          -0.38235472213378763,
          0.0005988379327103743,
          0.9240154261997602
        ],
        "angle_rad": 2.3972697030832225e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "abdomen_4",
        "joint_other": "abdomen_4",
        "axis_m": [
          0.002408635682517369,
          0.9999970384697133,
          0.00034860572534126615
        ],
        "axis_other_aligned": [
          0.0024086356825173717,
          0.9999970384697133,
          0.0003486057253404944
        ],
        "angle_rad": 7.717417339962948e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "abdomen_abduct_5",
        "joint_other": "abdomen_abduct_5",
        "axis_m": [
          -0.4493017867745893,
          0.0007004853791207976,
          0.8933797701545493
        ],
        "axis_other_aligned": [
          -0.4493017867745894,
          0.0007004853791210038,
          0.8933797701545492
        ],
        "angle_rad": 2.1360323740389975e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "abdomen_5",
        "joint_other": "abdomen_5",
        "axis_m": [
          0.0029642228302857463,
          0.9999953569706526,
          0.0007066966461413178
        ],
        "axis_other_aligned": [
          0.0029642228302857493,
          0.9999953569706526,
          0.0007066966461405461
        ],
        "angle_rad": 7.717444746643737e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "abdomen_abduct_6",
        "joint_other": "abdomen_abduct_6",
        "axis_m": [
          -0.5633647358681209,
          0.0014437776776368737,
          0.8262070502520903
        ],
        "axis_other_aligned": [
          -0.563364735868121,
          0.0014437776776370659,
          0.8262070502520903
        ],
        "angle_rad": 1.9984219612402395e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "abdomen_6",
        "joint_other": "abdomen_6",
        "axis_m": [
          0.003727295789724529,
          0.9999927383392677,
          0.0007940622323022701
        ],
        "axis_other_aligned": [
          0.003727295789724532,
          0.9999927383392677,
          0.0007940622323014984
        ],
        "angle_rad": 7.717464475479155e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "abdomen_abduct_7",
        "joint_other": "abdomen_abduct_7",
        "axis_m": [
          -0.71927727869623,
          0.0021638952480858213,
          0.6947197376703078
        ],
        "axis_other_aligned": [
          -0.71927727869623,
          0.0021638952480859852,
          0.6947197376703077
        ],
        "angle_rad": 1.981162247081252e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "abdomen_7",
        "joint_other": "abdomen_7",
        "axis_m": [
          0.0040108279595154625,
          0.9999914180176448,
          0.0010378584389755068
        ],
        "axis_other_aligned": [
          0.004010827959515465,
          0.9999914180176448,
          0.001037858438974735
        ],
        "angle_rad": 7.717457130624166e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "haltere_left",
        "joint_other": "haltere_left",
        "axis_m": [
          -0.7477324342301064,
          -0.08140466236689724,
          -0.6589912653026984
        ],
        "axis_other_aligned": [
          -0.7477324342301065,
          -0.08140466236689738,
          -0.6589912653026982
        ],
        "angle_rad": 2.161106224862407e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "haltere_right",
        "joint_other": "haltere_right",
        "axis_m": [
          0.758308906403606,
          -0.09627560577285599,
          0.6447469350078656
        ],
        "axis_other_aligned": [
          0.7583089064036059,
          -0.09627560577285582,
          0.6447469350078655
        ],
        "angle_rad": 1.5823112613210482e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "coxa_abduct_T1_left",
        "joint_other": "coxa_abduct_T1_left",
        "axis_m": [
          0.2949660567764698,
          0.8519198456970055,
          -0.4326980492876421
        ],
        "axis_other_aligned": [
          0.2949660567764698,
          0.8519198456970053,
          -0.4326980492876427
        ],
        "angle_rad": 6.353541660708337e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "coxa_twist_T1_left",
        "joint_other": "coxa_twist_T1_left",
        "axis_m": [
          -0.514065480937252,
          -0.24023527667369277,
          -0.8234219411396967
        ],
        "axis_other_aligned": [
          -0.5140654809372521,
          -0.24023527667369296,
          -0.8234219411396965
        ],
        "angle_rad": 3.0309546078301995e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "coxa_T1_left",
        "joint_other": "coxa_T1_left",
        "axis_m": [
          0.8054388286260429,
          -0.4653166538488653,
          -0.36708133293917755
        ],
        "axis_other_aligned": [
          0.8054388286260431,
          -0.46531665384886534,
          -0.36708133293917716
        ],
        "angle_rad": 4.379755957367586e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "femur_twist_T1_left",
        "joint_other": "femur_twist_T1_left",
        "axis_m": [
          0.5926392454383669,
          0.625148079653836,
          0.5079060969031228
        ],
        "axis_other_aligned": [
          0.592639245438367,
          0.6251480796538361,
          0.5079060969031224
        ],
        "angle_rad": 4.710277376051325e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "femur_T1_left",
        "joint_other": "femur_T1_left",
        "axis_m": [
          -0.805438828626043,
          0.46531665384886517,
          0.3670813329391775
        ],
        "axis_other_aligned": [
          -0.8054388286260432,
          0.4653166538488652,
          0.3670813329391771
        ],
        "angle_rad": 4.509747244882933e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "tibia_T1_left",
        "joint_other": "tibia_T1_left",
        "axis_m": [
          0.6812580219621415,
          -0.7314673940347922,
          0.029033755805622685
        ],
        "axis_other_aligned": [
          0.6812580219621416,
          -0.7314673940347922,
          0.02903375580562325
        ],
        "angle_rad": 5.7540544971738895e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "tarsus_T1_left",
        "joint_other": "tarsus_T1_left",
        "axis_m": [
          0.6135432754114323,
          -0.789641090695886,
          -0.005621128180635147
        ],
        "axis_other_aligned": [
          0.6135432754114324,
          -0.789641090695886,
          -0.0056211281806345355
        ],
        "angle_rad": 6.219183260247376e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "tarsus2_T1_left",
        "joint_other": "tarsus2_T1_left",
        "axis_m": [
          0.6135432754114323,
          -0.789641090695886,
          -0.005621128180635147
        ],
        "axis_other_aligned": [
          0.6135432754114324,
          -0.789641090695886,
          -0.0056211281806345355
        ],
        "angle_rad": 6.219183260247376e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "tarsus3_T1_left",
        "joint_other": "tarsus3_T1_left",
        "axis_m": [
          0.6135432754114323,
          -0.789641090695886,
          -0.005621128180635147
        ],
        "axis_other_aligned": [
          0.6135432754114324,
          -0.789641090695886,
          -0.0056211281806345355
        ],
        "angle_rad": 6.219183260247376e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "tarsus4_T1_left",
        "joint_other": "tarsus4_T1_left",
        "axis_m": [
          0.6135432754114323,
          -0.789641090695886,
          -0.005621128180635147
        ],
        "axis_other_aligned": [
          0.6135432754114324,
          -0.789641090695886,
          -0.0056211281806345355
        ],
        "angle_rad": 6.219183260247376e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "tarsus5_T1_left",
        "joint_other": "tarsus5_T1_left",
        "axis_m": [
          0.6135432754114323,
          -0.789641090695886,
          -0.005621128180635147
        ],
        "axis_other_aligned": [
          0.6135432754114324,
          -0.789641090695886,
          -0.0056211281806345355
        ],
        "angle_rad": 6.219183260247376e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "coxa_abduct_T1_right",
        "joint_other": "coxa_abduct_T1_right",
        "axis_m": [
          -0.36336085400715673,
          0.8364192471463129,
          0.41033124762609174
        ],
        "axis_other_aligned": [
          -0.36336085400715684,
          0.8364192471463131,
          0.41033124762609113
        ],
        "angle_rad": 6.707437923744493e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "coxa_twist_T1_right",
        "joint_other": "coxa_twist_T1_right",
        "axis_m": [
          0.4835575635207805,
          -0.2071447134318214,
          0.8504487935549648
        ],
        "axis_other_aligned": [
          0.4835575635207805,
          -0.20714471343182114,
          0.8504487935549647
        ],
        "angle_rad": 2.37549462997806e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "coxa_T1_right",
        "joint_other": "coxa_T1_right",
        "axis_m": [
          -0.7963296883433622,
          -0.5074385782540031,
          0.3291885732563021
        ],
        "axis_other_aligned": [
          -0.7963296883433623,
          -0.5074385782540028,
          0.32918857325630235
        ],
        "angle_rad": 3.387999773988764e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "femur_twist_T1_right",
        "joint_other": "femur_twist_T1_right",
        "axis_m": [
          -0.6007891463958077,
          0.6005096314058102,
          -0.5276746953965624
        ],
        "axis_other_aligned": [
          -0.6007891463958077,
          0.6005096314058099,
          -0.5276746953965628
        ],
        "angle_rad": 4.335559509131366e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "femur_T1_right",
        "joint_other": "femur_T1_right",
        "axis_m": [
          0.796329688343362,
          0.5074385782540032,
          -0.3291885732563022
        ],
        "axis_other_aligned": [
          0.796329688343362,
          0.507438578254003,
          -0.3291885732563025
        ],
        "angle_rad": 4.08865160135725e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "tibia_T1_right",
        "joint_other": "tibia_T1_right",
        "axis_m": [
          -0.6759535582690055,
          -0.7364519017854366,
          -0.02693294302678191
        ],
        "axis_other_aligned": [
          -0.6759535582690056,
          -0.7364519017854366,
          -0.026932943026781345
        ],
        "angle_rad": 5.804043602503624e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "tarsus_T1_right",
        "joint_other": "tarsus_T1_right",
        "axis_m": [
          -0.7689281250033315,
          -0.6356698520091335,
          -0.0683621081122247
        ],
        "axis_other_aligned": [
          -0.7689281250033315,
          -0.6356698520091334,
          -0.0683621081122242
        ],
        "angle_rad": 5.054449595385899e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "tarsus2_T1_right",
        "joint_other": "tarsus2_T1_right",
        "axis_m": [
          -0.7689281250033315,
          -0.6356698520091335,
          -0.0683621081122247
        ],
        "axis_other_aligned": [
          -0.7689281250033315,
          -0.6356698520091334,
          -0.0683621081122242
        ],
        "angle_rad": 5.054449595385899e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "tarsus3_T1_right",
        "joint_other": "tarsus3_T1_right",
        "axis_m": [
          -0.7689281250033315,
          -0.6356698520091335,
          -0.0683621081122247
        ],
        "axis_other_aligned": [
          -0.7689281250033315,
          -0.6356698520091334,
          -0.0683621081122242
        ],
        "angle_rad": 5.054449595385899e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "tarsus4_T1_right",
        "joint_other": "tarsus4_T1_right",
        "axis_m": [
          -0.7689281250033315,
          -0.6356698520091335,
          -0.0683621081122247
        ],
        "axis_other_aligned": [
          -0.7689281250033315,
          -0.6356698520091334,
          -0.0683621081122242
        ],
        "angle_rad": 5.054449595385899e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "tarsus5_T1_right",
        "joint_other": "tarsus5_T1_right",
        "axis_m": [
          -0.7689281250033315,
          -0.6356698520091335,
          -0.0683621081122247
        ],
        "axis_other_aligned": [
          -0.7689281250033315,
          -0.6356698520091334,
          -0.0683621081122242
        ],
        "angle_rad": 5.054449595385899e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "coxa_abduct_T2_left",
        "joint_other": "coxa_abduct_T2_left",
        "axis_m": [
          -0.03893764147142324,
          0.6988747831123311,
          -0.7141833781364108
        ],
        "axis_other_aligned": [
          -0.038937641471423236,
          0.6988747831123306,
          -0.714183378136411
        ],
        "angle_rad": 4.999857065771612e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "coxa_twist_T2_left",
        "joint_other": "coxa_twist_T2_left",
        "axis_m": [
          -0.2847649410049134,
          -0.6928489262967475,
          -0.6624721078686352
        ],
        "axis_other_aligned": [
          -0.2847649410049135,
          -0.6928489262967478,
          -0.6624721078686348
        ],
        "angle_rad": 4.972820174300705e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "coxa_T2_left",
        "joint_other": "coxa_T2_left",
        "axis_m": [
          0.9578062374254571,
          -0.17757928612069782,
          -0.22599293946880797
        ],
        "axis_other_aligned": [
          0.9578062374254571,
          -0.17757928612069784,
          -0.22599293946880777
        ],
        "angle_rad": 2.0062885096040707e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "femur_twist_T2_left",
        "joint_other": "femur_twist_T2_left",
        "axis_m": [
          0.26555407795775876,
          0.8475569923871896,
          0.4594868619836546
        ],
        "axis_other_aligned": [
          0.26555407795775887,
          0.8475569923871898,
          0.459486861983654
        ],
        "angle_rad": 6.521083742145178e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "femur_T2_left",
        "joint_other": "femur_T2_left",
        "axis_m": [
          -0.9578062374254572,
          0.17757928612069776,
          0.22599293946880789
        ],
        "axis_other_aligned": [
          -0.9578062374254572,
          0.1775792861206978,
          0.22599293946880772
        ],
        "angle_rad": 1.738881828270098e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "tibia_T2_left",
        "joint_other": "tibia_T2_left",
        "axis_m": [
          0.9384694602991496,
          -0.34510534608974985,
          -0.01331811496034316
        ],
        "axis_other_aligned": [
          0.9384694602991496,
          -0.3451053460897498,
          -0.013318114960342887
        ],
        "angle_rad": 2.7698732319435293e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "tarsus_T2_left",
        "joint_other": "tarsus_T2_left",
        "axis_m": [
          0.9830828373145147,
          -0.10869127394190793,
          0.14742571670685037
        ],
        "axis_other_aligned": [
          0.9830828373145147,
          -0.10869127394190789,
          0.14742571670685042
        ],
        "angle_rad": 7.076311083754595e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "tarsus2_T2_left",
        "joint_other": "tarsus2_T2_left",
        "axis_m": [
          0.9830828373145147,
          -0.10869127394190793,
          0.14742571670685037
        ],
        "axis_other_aligned": [
          0.9830828373145147,
          -0.10869127394190789,
          0.14742571670685042
        ],
        "angle_rad": 7.076311083754595e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "tarsus3_T2_left",
        "joint_other": "tarsus3_T2_left",
        "axis_m": [
          0.9830828373145147,
          -0.10869127394190793,
          0.14742571670685037
        ],
        "axis_other_aligned": [
          0.9830828373145147,
          -0.10869127394190789,
          0.14742571670685042
        ],
        "angle_rad": 7.076311083754595e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "tarsus4_T2_left",
        "joint_other": "tarsus4_T2_left",
        "axis_m": [
          0.9830828373145147,
          -0.10869127394190793,
          0.14742571670685037
        ],
        "axis_other_aligned": [
          0.9830828373145147,
          -0.10869127394190789,
          0.14742571670685042
        ],
        "angle_rad": 7.076311083754595e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "tarsus5_T2_left",
        "joint_other": "tarsus5_T2_left",
        "axis_m": [
          0.9830828373145147,
          -0.10869127394190793,
          0.14742571670685037
        ],
        "axis_other_aligned": [
          0.9830828373145147,
          -0.10869127394190789,
          0.14742571670685042
        ],
        "angle_rad": 7.076311083754595e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "coxa_abduct_T2_right",
        "joint_other": "coxa_abduct_T2_right",
        "axis_m": [
          0.035646688476469436,
          0.7031509535060095,
          0.7101464991001865
        ],
        "axis_other_aligned": [
          0.035646688476469464,
          0.7031509535060099,
          0.7101464991001861
        ],
        "angle_rad": 5.006232825943491e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "coxa_twist_T2_right",
        "joint_other": "coxa_twist_T2_right",
        "axis_m": [
          0.28391209943970647,
          -0.6884445341525965,
          0.6674114496973755
        ],
        "axis_other_aligned": [
          0.28391209943970647,
          -0.6884445341525963,
          0.667411449697376
        ],
        "angle_rad": 5.185169430563076e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "coxa_T2_right",
        "joint_other": "coxa_T2_right",
        "axis_m": [
          -0.958187472988663,
          -0.17782817543630036,
          0.22417383127518845
        ],
        "axis_other_aligned": [
          -0.958187472988663,
          -0.17782817543630025,
          0.22417383127518853
        ],
        "angle_rad": 1.3092278833360673e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "femur_twist_T2_right",
        "joint_other": "femur_twist_T2_right",
        "axis_m": [
          -0.2642496429364298,
          0.8504635747773598,
          -0.45484484627714944
        ],
        "axis_other_aligned": [
          -0.2642496429364298,
          0.8504635747773596,
          -0.45484484627715005
        ],
        "angle_rad": 6.318585897742262e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "femur_T2_right",
        "joint_other": "femur_T2_right",
        "axis_m": [
          0.958187472988663,
          0.17782817543630028,
          -0.2241738312751883
        ],
        "axis_other_aligned": [
          0.958187472988663,
          0.1778281754363002,
          -0.2241738312751884
        ],
        "angle_rad": 1.2276156489239667e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "tibia_T2_right",
        "joint_other": "tibia_T2_right",
        "axis_m": [
          -0.952664470676777,
          -0.3034154294651218,
          -0.019221952882896808
        ],
        "axis_other_aligned": [
          -0.952664470676777,
          -0.30341542946512173,
          -0.01922195288289657
        ],
        "angle_rad": 2.461168543934297e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "tarsus_T2_right",
        "joint_other": "tarsus_T2_right",
        "axis_m": [
          -0.9828333313510451,
          -0.1146220750719764,
          -0.14456978485008887
        ],
        "axis_other_aligned": [
          -0.9828333313510452,
          -0.1146220750719764,
          -0.14456978485008876
        ],
        "angle_rad": 1.1236938283130691e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "tarsus2_T2_right",
        "joint_other": "tarsus2_T2_right",
        "axis_m": [
          -0.9828333313510451,
          -0.1146220750719764,
          -0.14456978485008887
        ],
        "axis_other_aligned": [
          -0.9828333313510452,
          -0.1146220750719764,
          -0.14456978485008876
        ],
        "angle_rad": 1.1236938283130691e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "tarsus3_T2_right",
        "joint_other": "tarsus3_T2_right",
        "axis_m": [
          -0.9828333313510451,
          -0.1146220750719764,
          -0.14456978485008887
        ],
        "axis_other_aligned": [
          -0.9828333313510452,
          -0.1146220750719764,
          -0.14456978485008876
        ],
        "angle_rad": 1.1236938283130691e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "tarsus4_T2_right",
        "joint_other": "tarsus4_T2_right",
        "axis_m": [
          -0.9828333313510451,
          -0.1146220750719764,
          -0.14456978485008887
        ],
        "axis_other_aligned": [
          -0.9828333313510452,
          -0.1146220750719764,
          -0.14456978485008876
        ],
        "angle_rad": 1.1236938283130691e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "tarsus5_T2_right",
        "joint_other": "tarsus5_T2_right",
        "axis_m": [
          -0.9828333313510451,
          -0.1146220750719764,
          -0.14456978485008887
        ],
        "axis_other_aligned": [
          -0.9828333313510452,
          -0.1146220750719764,
          -0.14456978485008876
        ],
        "angle_rad": 1.1236938283130691e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "coxa_abduct_T3_left",
        "joint_other": "coxa_abduct_T3_left",
        "axis_m": [
          -0.6474104020187451,
          0.633039967650513,
          0.42440566762823106
        ],
        "axis_other_aligned": [
          -0.6474104020187452,
          0.6330399676505131,
          0.42440566762823057
        ],
        "angle_rad": 5.117875266520903e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "coxa_twist_T3_left",
        "joint_other": "coxa_twist_T3_left",
        "axis_m": [
          -0.5853202314654957,
          -0.05633939520659714,
          -0.8088424439808617
        ],
        "axis_other_aligned": [
          -0.5853202314654958,
          -0.056339395206597316,
          -0.8088424439808617
        ],
        "angle_rad": 1.993045536433795e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "coxa_T3_left",
        "joint_other": "coxa_T3_left",
        "axis_m": [
          0.4881188359355798,
          0.7720662354388984,
          -0.40700581089230414
        ],
        "axis_other_aligned": [
          0.4881188359355798,
          0.7720662354388981,
          -0.40700581089230464
        ],
        "angle_rad": 5.715222817774257e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "femur_twist_T3_left",
        "joint_other": "femur_twist_T3_left",
        "axis_m": [
          -0.5808430987048643,
          0.6354299955824776,
          0.5087730490120167
        ],
        "axis_other_aligned": [
          -0.5808430987048644,
          0.6354299955824777,
          0.5087730490120163
        ],
        "angle_rad": 4.710277376051325e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "femur_T3_left",
        "joint_other": "femur_T3_left",
        "axis_m": [
          -0.4881188359355799,
          -0.7720662354388984,
          0.4070058108923042
        ],
        "axis_other_aligned": [
          -0.4881188359355799,
          -0.7720662354388981,
          0.4070058108923047
        ],
        "angle_rad": 5.828670879282072e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "tibia_T3_left",
        "joint_other": "tibia_T3_left",
        "axis_m": [
          0.6727348461975776,
          0.7226234019472612,
          -0.15888123133236595
        ],
        "axis_other_aligned": [
          0.6727348461975776,
          0.722623401947261,
          -0.15888123133236648
        ],
        "angle_rad": 5.342497709481851e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "tarsus_T3_left",
        "joint_other": "tarsus_T3_left",
        "axis_m": [
          0.47978636236419925,
          0.8771654340067409,
          -0.019643010795076844
        ],
        "axis_other_aligned": [
          0.4797863623641993,
          0.8771654340067407,
          -0.019643010795077517
        ],
        "angle_rad": 6.835889108847827e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "tarsus2_T3_left",
        "joint_other": "tarsus2_T3_left",
        "axis_m": [
          0.47978636236419925,
          0.8771654340067409,
          -0.019643010795076844
        ],
        "axis_other_aligned": [
          0.4797863623641993,
          0.8771654340067407,
          -0.019643010795077517
        ],
        "angle_rad": 6.835889108847827e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "tarsus3_T3_left",
        "joint_other": "tarsus3_T3_left",
        "axis_m": [
          0.47978636236419925,
          0.8771654340067409,
          -0.019643010795076844
        ],
        "axis_other_aligned": [
          0.4797863623641993,
          0.8771654340067407,
          -0.019643010795077517
        ],
        "angle_rad": 6.835889108847827e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "tarsus4_T3_left",
        "joint_other": "tarsus4_T3_left",
        "axis_m": [
          0.47978636236419925,
          0.8771654340067409,
          -0.019643010795076844
        ],
        "axis_other_aligned": [
          0.4797863623641993,
          0.8771654340067407,
          -0.019643010795077517
        ],
        "angle_rad": 6.835889108847827e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "tarsus5_T3_left",
        "joint_other": "tarsus5_T3_left",
        "axis_m": [
          0.47978636236419925,
          0.8771654340067409,
          -0.019643010795076844
        ],
        "axis_other_aligned": [
          0.4797863623641993,
          0.8771654340067407,
          -0.019643010795077517
        ],
        "angle_rad": 6.835889108847827e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "coxa_abduct_T3_right",
        "joint_other": "coxa_abduct_T3_right",
        "axis_m": [
          0.6540247233925172,
          0.6322551000338703,
          -0.4153373925768088
        ],
        "axis_other_aligned": [
          0.654024723392517,
          0.63225510003387,
          -0.41533739257680924
        ],
        "angle_rad": 5.382005793715205e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "coxa_twist_T3_right",
        "joint_other": "coxa_twist_T3_right",
        "axis_m": [
          0.5882856267667127,
          -0.07992661678517708,
          0.8046935797363933
        ],
        "axis_other_aligned": [
          0.5882856267667128,
          -0.0799266167851769,
          0.8046935797363934
        ],
        "angle_rad": 1.9292121753525026e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "coxa_T3_right",
        "joint_other": "coxa_T3_right",
        "axis_m": [
          -0.47557510713980555,
          0.7706265142145293,
          0.4242205712345012
        ],
        "axis_other_aligned": [
          -0.4755751071398057,
          0.7706265142145295,
          0.42422057123450063
        ],
        "angle_rad": 6.473657049138937e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "femur_twist_T3_right",
        "joint_other": "femur_twist_T3_right",
        "axis_m": [
          0.5740415301876588,
          0.6372862694464577,
          -0.514142521480988
        ],
        "axis_other_aligned": [
          0.5740415301876588,
          0.6372862694464575,
          -0.5141425214809884
        ],
        "angle_rad": 4.335559509131367e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "femur_T3_right",
        "joint_other": "femur_T3_right",
        "axis_m": [
          0.47557510713980533,
          -0.7706265142145294,
          -0.4242205712345012
        ],
        "axis_other_aligned": [
          0.4755751071398055,
          -0.7706265142145297,
          -0.42422057123450063
        ],
        "angle_rad": 6.473657049138937e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "tibia_T3_right",
        "joint_other": "tibia_T3_right",
        "axis_m": [
          -0.6709506420385306,
          0.7230627444391755,
          0.16433351317418843
        ],
        "axis_other_aligned": [
          -0.6709506420385307,
          0.7230627444391755,
          0.16433351317418787
        ],
        "angle_rad": 5.703416235967739e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "tarsus_T3_right",
        "joint_other": "tarsus_T3_right",
        "axis_m": [
          -0.48369145144949144,
          0.8749144193497184,
          0.023818870851270806
        ],
        "axis_other_aligned": [
          -0.48369145144949155,
          0.8749144193497184,
          0.02381887085127013
        ],
        "angle_rad": 6.779285139611376e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "tarsus2_T3_right",
        "joint_other": "tarsus2_T3_right",
        "axis_m": [
          -0.48369145144949144,
          0.8749144193497184,
          0.023818870851270806
        ],
        "axis_other_aligned": [
          -0.48369145144949155,
          0.8749144193497184,
          0.02381887085127013
        ],
        "angle_rad": 6.779285139611376e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "tarsus3_T3_right",
        "joint_other": "tarsus3_T3_right",
        "axis_m": [
          -0.48369145144949144,
          0.8749144193497184,
          0.023818870851270806
        ],
        "axis_other_aligned": [
          -0.48369145144949155,
          0.8749144193497184,
          0.02381887085127013
        ],
        "angle_rad": 6.779285139611376e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "tarsus4_T3_right",
        "joint_other": "tarsus4_T3_right",
        "axis_m": [
          -0.48369145144949144,
          0.8749144193497184,
          0.023818870851270806
        ],
        "axis_other_aligned": [
          -0.48369145144949155,
          0.8749144193497184,
          0.02381887085127013
        ],
        "angle_rad": 6.779285139611376e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "tarsus5_T3_right",
        "joint_other": "tarsus5_T3_right",
        "axis_m": [
          -0.48369145144949144,
          0.8749144193497184,
          0.023818870851270806
        ],
        "axis_other_aligned": [
          -0.48369145144949155,
          0.8749144193497184,
          0.02381887085127013
        ],
        "angle_rad": 6.779285139611376e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      }
    ],
    "axis_disagreements": [],
    "com_eligible": true,
    "covariance_singular_values": [
      0.4790572719123735,
      0.3942342995019165,
      0.12726245349878376
    ],
    "origin_residuals_m": {
      "thorax": 1.4107764163058153e-17,
      "head": 1.8618168967019294e-17,
      "rostrum": 1.4728799896498942e-17,
      "haustellum": 2.122142710759789e-17,
      "labrum_left": 1.3985787785349405e-17,
      "labrum_right": 1.3985787785349405e-17,
      "antenna_left": 3.084593289525303e-17,
      "antenna_right": 3.109227384499446e-17,
      "wing_left": 3.5804289117824333e-17,
      "wing_right": 3.5804289117824333e-17,
      "abdomen": 1.6591127512380074e-17,
      "abdomen_2": 2.1051398297025365e-17,
      "abdomen_3": 2.068703487927255e-17,
      "abdomen_4": 3.081657532689489e-17,
      "abdomen_5": 3.00201172172477e-17,
      "abdomen_6": 2.932332211559956e-17,
      "abdomen_7": 2.8690415109637346e-17,
      "haltere_left": 2.281672496420498e-17,
      "haltere_right": 2.281672496420498e-17,
      "coxa_T1_left": 1.993045536433795e-17,
      "femur_T1_left": 1.4821483875836085e-17,
      "tibia_T1_left": 4.443059973708341e-17,
      "tarsus_T1_left": 5.721958498152797e-17,
      "tarsus2_T1_left": 5.887846720064156e-17,
      "tarsus3_T1_left": 7.211110073938365e-17,
      "tarsus4_T1_left": 7.211110073938365e-17,
      "claw_T1_left": 7.211110073938365e-17,
      "coxa_T1_right": 1.993045536433795e-17,
      "femur_T1_right": 1.4821483875836085e-17,
      "tibia_T1_right": 4.443059973708341e-17,
      "tarsus_T1_right": 5.721958498152797e-17,
      "tarsus2_T1_right": 5.887846720064156e-17,
      "tarsus3_T1_right": 7.211110073938365e-17,
      "tarsus4_T1_right": 7.211110073938365e-17,
      "claw_T1_right": 7.211110073938365e-17,
      "coxa_T2_left": 2.110382192020081e-17,
      "femur_T2_left": 6.938893903907228e-18,
      "tibia_T2_left": 6.068145509697911e-17,
      "tarsus_T2_left": 8.333897564733124e-17,
      "tarsus2_T2_left": 1.1464934308770758e-16,
      "tarsus3_T2_left": 1.1464934308770758e-16,
      "tarsus4_T2_left": 1.2813490069415586e-16,
      "claw_T2_left": 1.2836953722228372e-16,
      "coxa_T2_right": 2.110382192020081e-17,
      "femur_T2_right": 6.938893903907228e-18,
      "tibia_T2_right": 6.066459950017194e-17,
      "tarsus_T2_right": 8.333897564733124e-17,
      "tarsus2_T2_right": 1.1464934308770758e-16,
      "tarsus3_T2_right": 1.1464934308770758e-16,
      "tarsus4_T2_right": 1.2813490069415586e-16,
      "claw_T2_right": 1.2836953722228372e-16,
      "coxa_T3_left": 1.4304896245381992e-17,
      "femur_T3_left": 9.813077866773595e-18,
      "tibia_T3_left": 5.341145691818931e-17,
      "tarsus_T3_left": 6.206335383118183e-17,
      "tarsus2_T3_left": 7.601177430610147e-17,
      "tarsus3_T3_left": 7.601177430610147e-17,
      "tarsus4_T3_left": 8.886119947416683e-17,
      "claw_T3_left": 8.886119947416683e-17,
      "coxa_T3_right": 1.4304896245381992e-17,
      "femur_T3_right": 1.5515838457795457e-17,
      "tibia_T3_right": 4.7697009830883764e-17,
      "tarsus_T3_right": 6.206335383118183e-17,
      "tarsus2_T3_right": 7.601177430610147e-17,
      "tarsus3_T3_right": 7.601177430610147e-17,
      "tarsus4_T3_right": 8.886119947416683e-17,
      "claw_T3_right": 8.886119947416683e-17
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
| robot / total_com_registered | [-0.035070741, -0.000136575807, -0.0162619625] | [-0.035070741, -0.000136575807, -0.0162619625] | [-0.035070741, -0.000136575807, -0.0162619625] | [0, 0, 0] | eligible; compared after Kabsch alignment | [aggregate inputs](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/flybody/fruitfly.xml#L1) | [aggregate inputs](https://github.com/TuragaLab/flybody/blob/736608121847c3c025fd02a629bdb016a3294f9a/flybody/fruitfly/assets/fruitfly.xml#L1) | [aggregate inputs](https://github.com/TuragaLab/flybody/blob/d015e9bfe441bd90ae431bac24c55cb74bdbce26/flybody/fruitfly/assets/fruitfly.xml#L1) |
| thorax / com_registered | [1.7749687e-06, 3.78096735e-07, 9.60200401e-05] | [1.7749687e-06, 3.78096735e-07, 9.60200401e-05] | [1.7749687e-06, 3.78096735e-07, 9.60200401e-05] | [0, 0, 0] | eligible; compared after Kabsch alignment | [geometry/inference input L299](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/flybody/fruitfly.xml#L299) | [geometry/inference input L308](https://github.com/TuragaLab/flybody/blob/736608121847c3c025fd02a629bdb016a3294f9a/flybody/fruitfly/assets/fruitfly.xml#L308) | [geometry/inference input L308](https://github.com/TuragaLab/flybody/blob/d015e9bfe441bd90ae431bac24c55cb74bdbce26/flybody/fruitfly/assets/fruitfly.xml#L308) |
| head / com_registered | [0.0732494358, 3.49799502e-07, -0.0059259392] | [0.0732494358, 3.49799502e-07, -0.0059259392] | [0.0732494358, 3.49799502e-07, -0.0059259392] | [0, 0, 0] | eligible; compared after Kabsch alignment | [geometry/inference input L316](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/flybody/fruitfly.xml#L316) | [geometry/inference input L326](https://github.com/TuragaLab/flybody/blob/736608121847c3c025fd02a629bdb016a3294f9a/flybody/fruitfly/assets/fruitfly.xml#L326) | [geometry/inference input L326](https://github.com/TuragaLab/flybody/blob/d015e9bfe441bd90ae431bac24c55cb74bdbce26/flybody/fruitfly/assets/fruitfly.xml#L326) |
| rostrum / com_registered | [0.0673446193, 3.52763897e-07, -0.0381657326] | [0.0673446193, 3.52763897e-07, -0.0381657326] | [0.0673446193, 3.52763897e-07, -0.0381657326] | [0, 0, 0] | eligible; compared after Kabsch alignment | [geometry/inference input L332](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/flybody/fruitfly.xml#L332) | [geometry/inference input L338](https://github.com/TuragaLab/flybody/blob/736608121847c3c025fd02a629bdb016a3294f9a/flybody/fruitfly/assets/fruitfly.xml#L338) | [geometry/inference input L338](https://github.com/TuragaLab/flybody/blob/d015e9bfe441bd90ae431bac24c55cb74bdbce26/flybody/fruitfly/assets/fruitfly.xml#L338) |
| haustellum / com_registered | [0.0590803949, 3.23071773e-07, -0.0477715276] | [0.0590803949, 3.23071773e-07, -0.0477715276] | [0.0590803949, 3.23071773e-07, -0.0477715276] | [0, 0, 0] | eligible; compared after Kabsch alignment | [geometry/inference input L343](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/flybody/fruitfly.xml#L343) | [geometry/inference input L345](https://github.com/TuragaLab/flybody/blob/736608121847c3c025fd02a629bdb016a3294f9a/flybody/fruitfly/assets/fruitfly.xml#L345) | [geometry/inference input L345](https://github.com/TuragaLab/flybody/blob/d015e9bfe441bd90ae431bac24c55cb74bdbce26/flybody/fruitfly/assets/fruitfly.xml#L345) |
| labrum_left / com_registered | [0.0689578233, 0.00302614934, -0.0585024449] | [0.0689578233, 0.00302614934, -0.0585024449] | [0.0689578233, 0.00302614934, -0.0585024449] | [0, 0, 0] | eligible; compared after Kabsch alignment | [geometry/inference input L351](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/flybody/fruitfly.xml#L351) | [geometry/inference input L351](https://github.com/TuragaLab/flybody/blob/736608121847c3c025fd02a629bdb016a3294f9a/flybody/fruitfly/assets/fruitfly.xml#L351) | [geometry/inference input L351](https://github.com/TuragaLab/flybody/blob/d015e9bfe441bd90ae431bac24c55cb74bdbce26/flybody/fruitfly/assets/fruitfly.xml#L351) |
| labrum_right / com_registered | [0.0691631748, -0.00300785281, -0.0585704136] | [0.0691631748, -0.00300785281, -0.0585704136] | [0.0691631748, -0.00300785281, -0.0585704136] | [0, 0, 0] | eligible; compared after Kabsch alignment | [geometry/inference input L358](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/flybody/fruitfly.xml#L358) | [geometry/inference input L356](https://github.com/TuragaLab/flybody/blob/736608121847c3c025fd02a629bdb016a3294f9a/flybody/fruitfly/assets/fruitfly.xml#L356) | [geometry/inference input L356](https://github.com/TuragaLab/flybody/blob/d015e9bfe441bd90ae431bac24c55cb74bdbce26/flybody/fruitfly/assets/fruitfly.xml#L356) |
| antenna_left / com_registered | [0.0979642567, 0.0150510206, -0.0101265059] | [0.0979642567, 0.0150510206, -0.0101265059] | [0.0979642567, 0.0150510206, -0.0101265059] | [0, 0, 0] | eligible; compared after Kabsch alignment | [geometry/inference input L367](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/flybody/fruitfly.xml#L367) | [geometry/inference input L363](https://github.com/TuragaLab/flybody/blob/736608121847c3c025fd02a629bdb016a3294f9a/flybody/fruitfly/assets/fruitfly.xml#L363) | [geometry/inference input L363](https://github.com/TuragaLab/flybody/blob/d015e9bfe441bd90ae431bac24c55cb74bdbce26/flybody/fruitfly/assets/fruitfly.xml#L363) |
| antenna_right / com_registered | [0.0982863485, -0.015246513, -0.0103138762] | [0.0982863485, -0.015246513, -0.0103138762] | [0.0982863485, -0.015246513, -0.0103138762] | [0, 0, 0] | eligible; compared after Kabsch alignment | [geometry/inference input L377](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/flybody/fruitfly.xml#L377) | [geometry/inference input L371](https://github.com/TuragaLab/flybody/blob/736608121847c3c025fd02a629bdb016a3294f9a/flybody/fruitfly/assets/fruitfly.xml#L371) | [geometry/inference input L371](https://github.com/TuragaLab/flybody/blob/d015e9bfe441bd90ae431bac24c55cb74bdbce26/flybody/fruitfly/assets/fruitfly.xml#L371) |
| wing_left / com_registered | [-0.0460154234, 0.1912, 0.00899376572] | [-0.0460154234, 0.1912, 0.00899376572] | [-0.0460154234, 0.1912, 0.00899376572] | [0, 0, 0] | eligible; compared after Kabsch alignment | [geometry/inference input L388](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/flybody/fruitfly.xml#L388) | [geometry/inference input L380](https://github.com/TuragaLab/flybody/blob/736608121847c3c025fd02a629bdb016a3294f9a/flybody/fruitfly/assets/fruitfly.xml#L380) | [geometry/inference input L380](https://github.com/TuragaLab/flybody/blob/d015e9bfe441bd90ae431bac24c55cb74bdbce26/flybody/fruitfly/assets/fruitfly.xml#L380) |
| wing_right / com_registered | [-0.0460154234, -0.1912, 0.00899376572] | [-0.0460154234, -0.1912, 0.00899376572] | [-0.0460154234, -0.1912, 0.00899376572] | [0, 0, 0] | eligible; compared after Kabsch alignment | [geometry/inference input L405](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/flybody/fruitfly.xml#L405) | [geometry/inference input L391](https://github.com/TuragaLab/flybody/blob/736608121847c3c025fd02a629bdb016a3294f9a/flybody/fruitfly/assets/fruitfly.xml#L391) | [geometry/inference input L391](https://github.com/TuragaLab/flybody/blob/d015e9bfe441bd90ae431bac24c55cb74bdbce26/flybody/fruitfly/assets/fruitfly.xml#L391) |
| abdomen / com_registered | [-0.0532429171, -0.000676619778, -0.00344507679] | [-0.0532429171, -0.000676619778, -0.00344507679] | [-0.0532429171, -0.000676619778, -0.00344507679] | [0, 0, 0] | eligible; compared after Kabsch alignment | [geometry/inference input L422](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/flybody/fruitfly.xml#L422) | [geometry/inference input L402](https://github.com/TuragaLab/flybody/blob/736608121847c3c025fd02a629bdb016a3294f9a/flybody/fruitfly/assets/fruitfly.xml#L402) | [geometry/inference input L402](https://github.com/TuragaLab/flybody/blob/d015e9bfe441bd90ae431bac24c55cb74bdbce26/flybody/fruitfly/assets/fruitfly.xml#L402) |
| abdomen_2 / com_registered | [-0.0706623374, -0.000597713529, -0.00899140303] | [-0.0706623374, -0.000597713529, -0.00899140303] | [-0.0706623374, -0.000597713529, -0.00899140303] | [0, 0, 0] | eligible; compared after Kabsch alignment | [geometry/inference input L430](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/flybody/fruitfly.xml#L430) | [geometry/inference input L408](https://github.com/TuragaLab/flybody/blob/736608121847c3c025fd02a629bdb016a3294f9a/flybody/fruitfly/assets/fruitfly.xml#L408) | [geometry/inference input L408](https://github.com/TuragaLab/flybody/blob/d015e9bfe441bd90ae431bac24c55cb74bdbce26/flybody/fruitfly/assets/fruitfly.xml#L408) |
| abdomen_3 / com_registered | [-0.0914462877, -0.000406967026, -0.0159873159] | [-0.0914462877, -0.000406967026, -0.0159873159] | [-0.0914462877, -0.000406967026, -0.0159873159] | [0, 0, 0] | eligible; compared after Kabsch alignment | [geometry/inference input L438](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/flybody/fruitfly.xml#L438) | [geometry/inference input L414](https://github.com/TuragaLab/flybody/blob/736608121847c3c025fd02a629bdb016a3294f9a/flybody/fruitfly/assets/fruitfly.xml#L414) | [geometry/inference input L414](https://github.com/TuragaLab/flybody/blob/d015e9bfe441bd90ae431bac24c55cb74bdbce26/flybody/fruitfly/assets/fruitfly.xml#L414) |
| abdomen_4 / com_registered | [-0.115260727, -0.000392493814, -0.0246885545] | [-0.115260727, -0.000392493814, -0.0246885545] | [-0.115260727, -0.000392493814, -0.0246885545] | [0, 0, 0] | eligible; compared after Kabsch alignment | [geometry/inference input L446](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/flybody/fruitfly.xml#L446) | [geometry/inference input L420](https://github.com/TuragaLab/flybody/blob/736608121847c3c025fd02a629bdb016a3294f9a/flybody/fruitfly/assets/fruitfly.xml#L420) | [geometry/inference input L420](https://github.com/TuragaLab/flybody/blob/d015e9bfe441bd90ae431bac24c55cb74bdbce26/flybody/fruitfly/assets/fruitfly.xml#L420) |
| abdomen_5 / com_registered | [-0.134128518, 6.21818082e-05, -0.0332111236] | [-0.134128518, 6.21818082e-05, -0.0332111236] | [-0.134128518, 6.21818082e-05, -0.0332111236] | [0, 0, 0] | eligible; compared after Kabsch alignment | [geometry/inference input L454](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/flybody/fruitfly.xml#L454) | [geometry/inference input L426](https://github.com/TuragaLab/flybody/blob/736608121847c3c025fd02a629bdb016a3294f9a/flybody/fruitfly/assets/fruitfly.xml#L426) | [geometry/inference input L426](https://github.com/TuragaLab/flybody/blob/d015e9bfe441bd90ae431bac24c55cb74bdbce26/flybody/fruitfly/assets/fruitfly.xml#L426) |
| abdomen_6 / com_registered | [-0.150410737, -0.000347669379, -0.0417605779] | [-0.150410737, -0.000347669379, -0.0417605779] | [-0.150410737, -0.000347669379, -0.0417605779] | [0, 0, 0] | eligible; compared after Kabsch alignment | [geometry/inference input L462](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/flybody/fruitfly.xml#L462) | [geometry/inference input L432](https://github.com/TuragaLab/flybody/blob/736608121847c3c025fd02a629bdb016a3294f9a/flybody/fruitfly/assets/fruitfly.xml#L432) | [geometry/inference input L432](https://github.com/TuragaLab/flybody/blob/d015e9bfe441bd90ae431bac24c55cb74bdbce26/flybody/fruitfly/assets/fruitfly.xml#L432) |
| abdomen_7 / com_registered | [-0.16662669, -0.000246836805, -0.0531078897] | [-0.16662669, -0.000246836805, -0.0531078897] | [-0.16662669, -0.000246836805, -0.0531078897] | [0, 0, 0] | eligible; compared after Kabsch alignment | [geometry/inference input L471](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/flybody/fruitfly.xml#L471) | [geometry/inference input L438](https://github.com/TuragaLab/flybody/blob/736608121847c3c025fd02a629bdb016a3294f9a/flybody/fruitfly/assets/fruitfly.xml#L438) | [geometry/inference input L438](https://github.com/TuragaLab/flybody/blob/d015e9bfe441bd90ae431bac24c55cb74bdbce26/flybody/fruitfly/assets/fruitfly.xml#L438) |
| haltere_left / com_registered | [-0.0488077176, 0.0347487931, 0.000920864856] | [-0.0488077176, 0.0347487931, 0.000920864856] | [-0.0488077176, 0.0347487931, 0.000920864856] | [0, 0, 0] | eligible; compared after Kabsch alignment | [geometry/inference input L489](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/flybody/fruitfly.xml#L489) | [geometry/inference input L452](https://github.com/TuragaLab/flybody/blob/736608121847c3c025fd02a629bdb016a3294f9a/flybody/fruitfly/assets/fruitfly.xml#L452) | [geometry/inference input L452](https://github.com/TuragaLab/flybody/blob/d015e9bfe441bd90ae431bac24c55cb74bdbce26/flybody/fruitfly/assets/fruitfly.xml#L452) |
| haltere_right / com_registered | [-0.0488956344, -0.0349159055, 0.0012300086] | [-0.0488956344, -0.0349159055, 0.0012300086] | [-0.0488956344, -0.0349159055, 0.0012300086] | [0, 0, 0] | eligible; compared after Kabsch alignment | [geometry/inference input L493](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/flybody/fruitfly.xml#L493) | [geometry/inference input L456](https://github.com/TuragaLab/flybody/blob/736608121847c3c025fd02a629bdb016a3294f9a/flybody/fruitfly/assets/fruitfly.xml#L456) | [geometry/inference input L456](https://github.com/TuragaLab/flybody/blob/d015e9bfe441bd90ae431bac24c55cb74bdbce26/flybody/fruitfly/assets/fruitfly.xml#L456) |
| coxa_T1_left / com_registered | [0.0183754055, 0.0143807245, -0.0481859051] | [0.0183754055, 0.0143807245, -0.0481859051] | [0.0183754055, 0.0143807245, -0.0481859051] | [0, 0, 0] | eligible; compared after Kabsch alignment | [geometry/inference input L497](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/flybody/fruitfly.xml#L497) | [geometry/inference input L460](https://github.com/TuragaLab/flybody/blob/736608121847c3c025fd02a629bdb016a3294f9a/flybody/fruitfly/assets/fruitfly.xml#L460) | [geometry/inference input L460](https://github.com/TuragaLab/flybody/blob/d015e9bfe441bd90ae431bac24c55cb74bdbce26/flybody/fruitfly/assets/fruitfly.xml#L460) |
| femur_T1_left / com_registered | [0.0272855791, 0.0339878467, -0.0476214464] | [0.0272855791, 0.0339878467, -0.0476214464] | [0.0272855791, 0.0339878467, -0.0476214464] | [0, 0, 0] | eligible; compared after Kabsch alignment | [geometry/inference input L504](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/flybody/fruitfly.xml#L504) | [geometry/inference input L466](https://github.com/TuragaLab/flybody/blob/736608121847c3c025fd02a629bdb016a3294f9a/flybody/fruitfly/assets/fruitfly.xml#L466) | [geometry/inference input L466](https://github.com/TuragaLab/flybody/blob/d015e9bfe441bd90ae431bac24c55cb74bdbce26/flybody/fruitfly/assets/fruitfly.xml#L466) |
| tibia_T1_left / com_registered | [0.0620304709, 0.0644416949, -0.0520318007] | [0.0620304709, 0.0644416949, -0.0520318007] | [0.0620304709, 0.0644416949, -0.0520318007] | [0, 0, 0] | eligible; compared after Kabsch alignment | [geometry/inference input L510](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/flybody/fruitfly.xml#L510) | [geometry/inference input L471](https://github.com/TuragaLab/flybody/blob/736608121847c3c025fd02a629bdb016a3294f9a/flybody/fruitfly/assets/fruitfly.xml#L471) | [geometry/inference input L471](https://github.com/TuragaLab/flybody/blob/d015e9bfe441bd90ae431bac24c55cb74bdbce26/flybody/fruitfly/assets/fruitfly.xml#L471) |
| tarsus_T1_left / com_registered | [0.0749855903, 0.0748734848, -0.0833131907] | [0.0749855903, 0.0748734848, -0.0833131907] | [0.0749855903, 0.0748734848, -0.0833131907] | [0, 0, 0] | eligible; compared after Kabsch alignment | [geometry/inference input L515](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/flybody/fruitfly.xml#L515) | [geometry/inference input L475](https://github.com/TuragaLab/flybody/blob/736608121847c3c025fd02a629bdb016a3294f9a/flybody/fruitfly/assets/fruitfly.xml#L475) | [geometry/inference input L475](https://github.com/TuragaLab/flybody/blob/d015e9bfe441bd90ae431bac24c55cb74bdbce26/flybody/fruitfly/assets/fruitfly.xml#L475) |
| tarsus2_T1_left / com_registered | [0.0819851353, 0.0801089705, -0.0995003563] | [0.0819851353, 0.0801089705, -0.0995003563] | [0.0819851353, 0.0801089705, -0.0995003563] | [0, 0, 0] | eligible; compared after Kabsch alignment | [geometry/inference input L522](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/flybody/fruitfly.xml#L522) | [geometry/inference input L480](https://github.com/TuragaLab/flybody/blob/736608121847c3c025fd02a629bdb016a3294f9a/flybody/fruitfly/assets/fruitfly.xml#L480) | [geometry/inference input L480](https://github.com/TuragaLab/flybody/blob/d015e9bfe441bd90ae431bac24c55cb74bdbce26/flybody/fruitfly/assets/fruitfly.xml#L480) |
| tarsus3_T1_left / com_registered | [0.0859963746, 0.0833623183, -0.109404634] | [0.0859963746, 0.0833623183, -0.109404634] | [0.0859963746, 0.0833623183, -0.109404634] | [0, 0, 0] | eligible; compared after Kabsch alignment | [geometry/inference input L528](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/flybody/fruitfly.xml#L528) | [geometry/inference input L484](https://github.com/TuragaLab/flybody/blob/736608121847c3c025fd02a629bdb016a3294f9a/flybody/fruitfly/assets/fruitfly.xml#L484) | [geometry/inference input L484](https://github.com/TuragaLab/flybody/blob/d015e9bfe441bd90ae431bac24c55cb74bdbce26/flybody/fruitfly/assets/fruitfly.xml#L484) |
| tarsus4_T1_left / com_registered | [0.0889365189, 0.085991351, -0.116742834] | [0.0889365189, 0.085991351, -0.116742834] | [0.0889365189, 0.085991351, -0.116742834] | [0, 0, 0] | eligible; compared after Kabsch alignment | [geometry/inference input L534](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/flybody/fruitfly.xml#L534) | [geometry/inference input L488](https://github.com/TuragaLab/flybody/blob/736608121847c3c025fd02a629bdb016a3294f9a/flybody/fruitfly/assets/fruitfly.xml#L488) | [geometry/inference input L488](https://github.com/TuragaLab/flybody/blob/d015e9bfe441bd90ae431bac24c55cb74bdbce26/flybody/fruitfly/assets/fruitfly.xml#L488) |
| claw_T1_left / com_registered | [0.0919127681, 0.08888051, -0.125011272] | [0.0919127681, 0.08888051, -0.125011272] | [0.0919127681, 0.08888051, -0.125011272] | [0, 0, 0] | eligible; compared after Kabsch alignment | [geometry/inference input L540](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/flybody/fruitfly.xml#L540) | [geometry/inference input L492](https://github.com/TuragaLab/flybody/blob/736608121847c3c025fd02a629bdb016a3294f9a/flybody/fruitfly/assets/fruitfly.xml#L492) | [geometry/inference input L492](https://github.com/TuragaLab/flybody/blob/d015e9bfe441bd90ae431bac24c55cb74bdbce26/flybody/fruitfly/assets/fruitfly.xml#L492) |
| coxa_T1_right / com_registered | [0.018050363, -0.0146598446, -0.0484354842] | [0.018050363, -0.0146598446, -0.0484354842] | [0.018050363, -0.0146598446, -0.0484354842] | [0, 0, 0] | eligible; compared after Kabsch alignment | [geometry/inference input L556](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/flybody/fruitfly.xml#L556) | [geometry/inference input L505](https://github.com/TuragaLab/flybody/blob/736608121847c3c025fd02a629bdb016a3294f9a/flybody/fruitfly/assets/fruitfly.xml#L505) | [geometry/inference input L505](https://github.com/TuragaLab/flybody/blob/d015e9bfe441bd90ae431bac24c55cb74bdbce26/flybody/fruitfly/assets/fruitfly.xml#L505) |
| femur_T1_right / com_registered | [0.0290247458, -0.0345736744, -0.0480930263] | [0.0290247458, -0.0345736744, -0.0480930263] | [0.0290247458, -0.0345736744, -0.0480930263] | [0, 0, 0] | eligible; compared after Kabsch alignment | [geometry/inference input L563](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/flybody/fruitfly.xml#L563) | [geometry/inference input L511](https://github.com/TuragaLab/flybody/blob/736608121847c3c025fd02a629bdb016a3294f9a/flybody/fruitfly/assets/fruitfly.xml#L511) | [geometry/inference input L511](https://github.com/TuragaLab/flybody/blob/d015e9bfe441bd90ae431bac24c55cb74bdbce26/flybody/fruitfly/assets/fruitfly.xml#L511) |
| tibia_T1_right / com_registered | [0.0643423004, -0.0636260126, -0.051526271] | [0.0643423004, -0.0636260126, -0.051526271] | [0.0643423004, -0.0636260126, -0.051526271] | [0, 0, 0] | eligible; compared after Kabsch alignment | [geometry/inference input L570](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/flybody/fruitfly.xml#L570) | [geometry/inference input L516](https://github.com/TuragaLab/flybody/blob/736608121847c3c025fd02a629bdb016a3294f9a/flybody/fruitfly/assets/fruitfly.xml#L516) | [geometry/inference input L516](https://github.com/TuragaLab/flybody/blob/d015e9bfe441bd90ae431bac24c55cb74bdbce26/flybody/fruitfly/assets/fruitfly.xml#L516) |
| tarsus_T1_right / com_registered | [0.076669194, -0.0739137138, -0.0832171804] | [0.076669194, -0.0739137138, -0.0832171804] | [0.076669194, -0.0739137138, -0.0832171804] | [0, 0, 0] | eligible; compared after Kabsch alignment | [geometry/inference input L575](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/flybody/fruitfly.xml#L575) | [geometry/inference input L520](https://github.com/TuragaLab/flybody/blob/736608121847c3c025fd02a629bdb016a3294f9a/flybody/fruitfly/assets/fruitfly.xml#L520) | [geometry/inference input L520](https://github.com/TuragaLab/flybody/blob/d015e9bfe441bd90ae431bac24c55cb74bdbce26/flybody/fruitfly/assets/fruitfly.xml#L520) |
| tarsus2_T1_right / com_registered | [0.0830735096, -0.0793747483, -0.0995081407] | [0.0830735096, -0.0793747483, -0.0995081407] | [0.0830735096, -0.0793747483, -0.0995081407] | [0, 0, 0] | eligible; compared after Kabsch alignment | [geometry/inference input L582](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/flybody/fruitfly.xml#L582) | [geometry/inference input L525](https://github.com/TuragaLab/flybody/blob/736608121847c3c025fd02a629bdb016a3294f9a/flybody/fruitfly/assets/fruitfly.xml#L525) | [geometry/inference input L525](https://github.com/TuragaLab/flybody/blob/d015e9bfe441bd90ae431bac24c55cb74bdbce26/flybody/fruitfly/assets/fruitfly.xml#L525) |
| tarsus3_T1_right / com_registered | [0.0867431662, -0.0829957806, -0.109286354] | [0.0867431662, -0.0829957806, -0.109286354] | [0.0867431662, -0.0829957806, -0.109286354] | [0, 0, 0] | eligible; compared after Kabsch alignment | [geometry/inference input L588](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/flybody/fruitfly.xml#L588) | [geometry/inference input L529](https://github.com/TuragaLab/flybody/blob/736608121847c3c025fd02a629bdb016a3294f9a/flybody/fruitfly/assets/fruitfly.xml#L529) | [geometry/inference input L529](https://github.com/TuragaLab/flybody/blob/d015e9bfe441bd90ae431bac24c55cb74bdbce26/flybody/fruitfly/assets/fruitfly.xml#L529) |
| tarsus4_T1_right / com_registered | [0.0894551278, -0.0864131556, -0.11657418] | [0.0894551278, -0.0864131556, -0.11657418] | [0.0894551278, -0.0864131556, -0.11657418] | [0, 0, 0] | eligible; compared after Kabsch alignment | [geometry/inference input L594](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/flybody/fruitfly.xml#L594) | [geometry/inference input L533](https://github.com/TuragaLab/flybody/blob/736608121847c3c025fd02a629bdb016a3294f9a/flybody/fruitfly/assets/fruitfly.xml#L533) | [geometry/inference input L533](https://github.com/TuragaLab/flybody/blob/d015e9bfe441bd90ae431bac24c55cb74bdbce26/flybody/fruitfly/assets/fruitfly.xml#L533) |
| claw_T1_right / com_registered | [0.0916962528, -0.0895226171, -0.124912212] | [0.0916962528, -0.0895226171, -0.124912212] | [0.0916962528, -0.0895226171, -0.124912212] | [0, 0, 0] | eligible; compared after Kabsch alignment | [geometry/inference input L600](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/flybody/fruitfly.xml#L600) | [geometry/inference input L537](https://github.com/TuragaLab/flybody/blob/736608121847c3c025fd02a629bdb016a3294f9a/flybody/fruitfly/assets/fruitfly.xml#L537) | [geometry/inference input L537](https://github.com/TuragaLab/flybody/blob/d015e9bfe441bd90ae431bac24c55cb74bdbce26/flybody/fruitfly/assets/fruitfly.xml#L537) |
| coxa_T2_left / com_registered | [-0.0190086032, 0.00957223165, -0.0526166198] | [-0.0190086032, 0.00957223165, -0.0526166198] | [-0.0190086032, 0.00957223165, -0.0526166198] | [0, 0, 0] | eligible; compared after Kabsch alignment | [geometry/inference input L616](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/flybody/fruitfly.xml#L616) | [geometry/inference input L550](https://github.com/TuragaLab/flybody/blob/736608121847c3c025fd02a629bdb016a3294f9a/flybody/fruitfly/assets/fruitfly.xml#L550) | [geometry/inference input L550](https://github.com/TuragaLab/flybody/blob/d015e9bfe441bd90ae431bac24c55cb74bdbce26/flybody/fruitfly/assets/fruitfly.xml#L550) |
| femur_T2_left / com_registered | [-0.010600741, 0.0399000236, -0.0447533347] | [-0.010600741, 0.0399000236, -0.0447533347] | [-0.010600741, 0.0399000236, -0.0447533347] | [0, 0, 0] | eligible; compared after Kabsch alignment | [geometry/inference input L623](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/flybody/fruitfly.xml#L623) | [geometry/inference input L556](https://github.com/TuragaLab/flybody/blob/736608121847c3c025fd02a629bdb016a3294f9a/flybody/fruitfly/assets/fruitfly.xml#L556) | [geometry/inference input L556](https://github.com/TuragaLab/flybody/blob/d015e9bfe441bd90ae431bac24c55cb74bdbce26/flybody/fruitfly/assets/fruitfly.xml#L556) |
| tibia_T2_left / com_registered | [0.00607012172, 0.0934251728, -0.0503820679] | [0.00607012172, 0.0934251728, -0.0503820679] | [0.00607012172, 0.0934251728, -0.0503820679] | [0, 0, 0] | eligible; compared after Kabsch alignment | [geometry/inference input L629](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/flybody/fruitfly.xml#L629) | [geometry/inference input L561](https://github.com/TuragaLab/flybody/blob/736608121847c3c025fd02a629bdb016a3294f9a/flybody/fruitfly/assets/fruitfly.xml#L561) | [geometry/inference input L561](https://github.com/TuragaLab/flybody/blob/d015e9bfe441bd90ae431bac24c55cb74bdbce26/flybody/fruitfly/assets/fruitfly.xml#L561) |
| tarsus_T2_left / com_registered | [0.0142341406, 0.121533219, -0.0898512911] | [0.0142341406, 0.121533219, -0.0898512911] | [0.0142341406, 0.121533219, -0.0898512911] | [0, 0, 0] | eligible; compared after Kabsch alignment | [geometry/inference input L633](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/flybody/fruitfly.xml#L633) | [geometry/inference input L565](https://github.com/TuragaLab/flybody/blob/736608121847c3c025fd02a629bdb016a3294f9a/flybody/fruitfly/assets/fruitfly.xml#L565) | [geometry/inference input L565](https://github.com/TuragaLab/flybody/blob/d015e9bfe441bd90ae431bac24c55cb74bdbce26/flybody/fruitfly/assets/fruitfly.xml#L565) |
| tarsus2_T2_left / com_registered | [0.0194656674, 0.143134636, -0.106232513] | [0.0194656674, 0.143134636, -0.106232513] | [0.0194656674, 0.143134636, -0.106232513] | [0, 0, 0] | eligible; compared after Kabsch alignment | [geometry/inference input L640](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/flybody/fruitfly.xml#L640) | [geometry/inference input L570](https://github.com/TuragaLab/flybody/blob/736608121847c3c025fd02a629bdb016a3294f9a/flybody/fruitfly/assets/fruitfly.xml#L570) | [geometry/inference input L570](https://github.com/TuragaLab/flybody/blob/d015e9bfe441bd90ae431bac24c55cb74bdbce26/flybody/fruitfly/assets/fruitfly.xml#L570) |
| tarsus3_T2_left / com_registered | [0.0219471568, 0.153176834, -0.115052914] | [0.0219471568, 0.153176834, -0.115052914] | [0.0219471568, 0.153176834, -0.115052914] | [0, 0, 0] | eligible; compared after Kabsch alignment | [geometry/inference input L646](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/flybody/fruitfly.xml#L646) | [geometry/inference input L574](https://github.com/TuragaLab/flybody/blob/736608121847c3c025fd02a629bdb016a3294f9a/flybody/fruitfly/assets/fruitfly.xml#L574) | [geometry/inference input L574](https://github.com/TuragaLab/flybody/blob/d015e9bfe441bd90ae431bac24c55cb74bdbce26/flybody/fruitfly/assets/fruitfly.xml#L574) |
| tarsus4_T2_left / com_registered | [0.0236866735, 0.160437885, -0.120597211] | [0.0236866735, 0.160437885, -0.120597211] | [0.0236866735, 0.160437885, -0.120597211] | [0, 0, 0] | eligible; compared after Kabsch alignment | [geometry/inference input L652](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/flybody/fruitfly.xml#L652) | [geometry/inference input L578](https://github.com/TuragaLab/flybody/blob/736608121847c3c025fd02a629bdb016a3294f9a/flybody/fruitfly/assets/fruitfly.xml#L578) | [geometry/inference input L578](https://github.com/TuragaLab/flybody/blob/d015e9bfe441bd90ae431bac24c55cb74bdbce26/flybody/fruitfly/assets/fruitfly.xml#L578) |
| claw_T2_left / com_registered | [0.0254490463, 0.168318107, -0.126204197] | [0.0254490463, 0.168318107, -0.126204197] | [0.0254490463, 0.168318107, -0.126204197] | [0, 0, 0] | eligible; compared after Kabsch alignment | [geometry/inference input L658](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/flybody/fruitfly.xml#L658) | [geometry/inference input L582](https://github.com/TuragaLab/flybody/blob/736608121847c3c025fd02a629bdb016a3294f9a/flybody/fruitfly/assets/fruitfly.xml#L582) | [geometry/inference input L582](https://github.com/TuragaLab/flybody/blob/d015e9bfe441bd90ae431bac24c55cb74bdbce26/flybody/fruitfly/assets/fruitfly.xml#L582) |
| coxa_T2_right / com_registered | [-0.0190797662, -0.00979620774, -0.0528225679] | [-0.0190797662, -0.00979620774, -0.0528225679] | [-0.0190797662, -0.00979620774, -0.0528225679] | [0, 0, 0] | eligible; compared after Kabsch alignment | [geometry/inference input L674](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/flybody/fruitfly.xml#L674) | [geometry/inference input L595](https://github.com/TuragaLab/flybody/blob/736608121847c3c025fd02a629bdb016a3294f9a/flybody/fruitfly/assets/fruitfly.xml#L595) | [geometry/inference input L595](https://github.com/TuragaLab/flybody/blob/d015e9bfe441bd90ae431bac24c55cb74bdbce26/flybody/fruitfly/assets/fruitfly.xml#L595) |
| femur_T2_right / com_registered | [-0.0105999382, -0.0398808707, -0.044892111] | [-0.0105999382, -0.0398808707, -0.044892111] | [-0.0105999382, -0.0398808707, -0.044892111] | [0, 0, 0] | eligible; compared after Kabsch alignment | [geometry/inference input L682](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/flybody/fruitfly.xml#L682) | [geometry/inference input L601](https://github.com/TuragaLab/flybody/blob/736608121847c3c025fd02a629bdb016a3294f9a/flybody/fruitfly/assets/fruitfly.xml#L601) | [geometry/inference input L601](https://github.com/TuragaLab/flybody/blob/d015e9bfe441bd90ae431bac24c55cb74bdbce26/flybody/fruitfly/assets/fruitfly.xml#L601) |
| tibia_T2_right / com_registered | [0.00609530812, -0.0931178822, -0.0507912742] | [0.00609530812, -0.0931178822, -0.0507912742] | [0.00609530812, -0.0931178822, -0.0507912742] | [0, 0, 0] | eligible; compared after Kabsch alignment | [geometry/inference input L689](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/flybody/fruitfly.xml#L689) | [geometry/inference input L606](https://github.com/TuragaLab/flybody/blob/736608121847c3c025fd02a629bdb016a3294f9a/flybody/fruitfly/assets/fruitfly.xml#L606) | [geometry/inference input L606](https://github.com/TuragaLab/flybody/blob/d015e9bfe441bd90ae431bac24c55cb74bdbce26/flybody/fruitfly/assets/fruitfly.xml#L606) |
| tarsus_T2_right / com_registered | [0.014497626, -0.121520866, -0.0903262241] | [0.014497626, -0.121520866, -0.0903262241] | [0.014497626, -0.121520866, -0.0903262241] | [0, 0, 0] | eligible; compared after Kabsch alignment | [geometry/inference input L694](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/flybody/fruitfly.xml#L694) | [geometry/inference input L610](https://github.com/TuragaLab/flybody/blob/736608121847c3c025fd02a629bdb016a3294f9a/flybody/fruitfly/assets/fruitfly.xml#L610) | [geometry/inference input L610](https://github.com/TuragaLab/flybody/blob/d015e9bfe441bd90ae431bac24c55cb74bdbce26/flybody/fruitfly/assets/fruitfly.xml#L610) |
| tarsus2_T2_right / com_registered | [0.0197076391, -0.142922124, -0.10694856] | [0.0197076391, -0.142922124, -0.10694856] | [0.0197076391, -0.142922124, -0.10694856] | [0, 0, 0] | eligible; compared after Kabsch alignment | [geometry/inference input L701](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/flybody/fruitfly.xml#L701) | [geometry/inference input L615](https://github.com/TuragaLab/flybody/blob/736608121847c3c025fd02a629bdb016a3294f9a/flybody/fruitfly/assets/fruitfly.xml#L615) | [geometry/inference input L615](https://github.com/TuragaLab/flybody/blob/d015e9bfe441bd90ae431bac24c55cb74bdbce26/flybody/fruitfly/assets/fruitfly.xml#L615) |
| tarsus3_T2_right / com_registered | [0.022270365, -0.154062601, -0.114913539] | [0.022270365, -0.154062601, -0.114913539] | [0.022270365, -0.154062601, -0.114913539] | [0, 0, 0] | eligible; compared after Kabsch alignment | [geometry/inference input L707](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/flybody/fruitfly.xml#L707) | [geometry/inference input L619](https://github.com/TuragaLab/flybody/blob/736608121847c3c025fd02a629bdb016a3294f9a/flybody/fruitfly/assets/fruitfly.xml#L619) | [geometry/inference input L619](https://github.com/TuragaLab/flybody/blob/d015e9bfe441bd90ae431bac24c55cb74bdbce26/flybody/fruitfly/assets/fruitfly.xml#L619) |
| tarsus4_T2_right / com_registered | [0.0239404195, -0.160668578, -0.121206576] | [0.0239404195, -0.160668578, -0.121206576] | [0.0239404195, -0.160668578, -0.121206576] | [0, 0, 0] | eligible; compared after Kabsch alignment | [geometry/inference input L713](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/flybody/fruitfly.xml#L713) | [geometry/inference input L623](https://github.com/TuragaLab/flybody/blob/736608121847c3c025fd02a629bdb016a3294f9a/flybody/fruitfly/assets/fruitfly.xml#L623) | [geometry/inference input L623](https://github.com/TuragaLab/flybody/blob/d015e9bfe441bd90ae431bac24c55cb74bdbce26/flybody/fruitfly/assets/fruitfly.xml#L623) |
| claw_T2_right / com_registered | [0.0257365653, -0.169173183, -0.12601501] | [0.0257365653, -0.169173183, -0.12601501] | [0.0257365653, -0.169173183, -0.12601501] | [0, 0, 0] | eligible; compared after Kabsch alignment | [geometry/inference input L719](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/flybody/fruitfly.xml#L719) | [geometry/inference input L627](https://github.com/TuragaLab/flybody/blob/736608121847c3c025fd02a629bdb016a3294f9a/flybody/fruitfly/assets/fruitfly.xml#L627) | [geometry/inference input L627](https://github.com/TuragaLab/flybody/blob/d015e9bfe441bd90ae431bac24c55cb74bdbce26/flybody/fruitfly/assets/fruitfly.xml#L627) |
| coxa_T3_left / com_registered | [-0.0427515724, 0.0114214554, -0.0524920778] | [-0.0427515724, 0.0114214554, -0.0524920778] | [-0.0427515724, 0.0114214554, -0.0524920778] | [0, 0, 0] | eligible; compared after Kabsch alignment | [geometry/inference input L735](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/flybody/fruitfly.xml#L735) | [geometry/inference input L640](https://github.com/TuragaLab/flybody/blob/736608121847c3c025fd02a629bdb016a3294f9a/flybody/fruitfly/assets/fruitfly.xml#L640) | [geometry/inference input L640](https://github.com/TuragaLab/flybody/blob/d015e9bfe441bd90ae431bac24c55cb74bdbce26/flybody/fruitfly/assets/fruitfly.xml#L640) |
| femur_T3_left / com_registered | [-0.0677192497, 0.0336055965, -0.0451796368] | [-0.0677192497, 0.0336055965, -0.0451796368] | [-0.0677192497, 0.0336055965, -0.0451796368] | [0, 0, 0] | eligible; compared after Kabsch alignment | [geometry/inference input L742](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/flybody/fruitfly.xml#L742) | [geometry/inference input L646](https://github.com/TuragaLab/flybody/blob/736608121847c3c025fd02a629bdb016a3294f9a/flybody/fruitfly/assets/fruitfly.xml#L646) | [geometry/inference input L646](https://github.com/TuragaLab/flybody/blob/d015e9bfe441bd90ae431bac24c55cb74bdbce26/flybody/fruitfly/assets/fruitfly.xml#L646) |
| tibia_T3_left / com_registered | [-0.111506351, 0.0696596539, -0.0515600416] | [-0.111506351, 0.0696596539, -0.0515600416] | [-0.111506351, 0.0696596539, -0.0515600416] | [0, 0, 0] | eligible; compared after Kabsch alignment | [geometry/inference input L749](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/flybody/fruitfly.xml#L749) | [geometry/inference input L651](https://github.com/TuragaLab/flybody/blob/736608121847c3c025fd02a629bdb016a3294f9a/flybody/fruitfly/assets/fruitfly.xml#L651) | [geometry/inference input L651](https://github.com/TuragaLab/flybody/blob/d015e9bfe441bd90ae431bac24c55cb74bdbce26/flybody/fruitfly/assets/fruitfly.xml#L651) |
| tarsus_T3_left / com_registered | [-0.136537227, 0.0811749735, -0.0913476371] | [-0.136537227, 0.0811749735, -0.0913476371] | [-0.136537227, 0.0811749735, -0.0913476371] | [0, 0, 0] | eligible; compared after Kabsch alignment | [geometry/inference input L754](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/flybody/fruitfly.xml#L754) | [geometry/inference input L655](https://github.com/TuragaLab/flybody/blob/736608121847c3c025fd02a629bdb016a3294f9a/flybody/fruitfly/assets/fruitfly.xml#L655) | [geometry/inference input L655](https://github.com/TuragaLab/flybody/blob/d015e9bfe441bd90ae431bac24c55cb74bdbce26/flybody/fruitfly/assets/fruitfly.xml#L655) |
| tarsus2_T3_left / com_registered | [-0.158487719, 0.0929350502, -0.105318783] | [-0.158487719, 0.0929350502, -0.105318783] | [-0.158487719, 0.0929350502, -0.105318783] | [0, 0, 0] | eligible; compared after Kabsch alignment | [geometry/inference input L761](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/flybody/fruitfly.xml#L761) | [geometry/inference input L660](https://github.com/TuragaLab/flybody/blob/736608121847c3c025fd02a629bdb016a3294f9a/flybody/fruitfly/assets/fruitfly.xml#L660) | [geometry/inference input L660](https://github.com/TuragaLab/flybody/blob/d015e9bfe441bd90ae431bac24c55cb74bdbce26/flybody/fruitfly/assets/fruitfly.xml#L660) |
| tarsus3_T3_left / com_registered | [-0.169801915, 0.0989583352, -0.113682145] | [-0.169801915, 0.0989583352, -0.113682145] | [-0.169801915, 0.0989583352, -0.113682145] | [0, 0, 0] | eligible; compared after Kabsch alignment | [geometry/inference input L767](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/flybody/fruitfly.xml#L767) | [geometry/inference input L664](https://github.com/TuragaLab/flybody/blob/736608121847c3c025fd02a629bdb016a3294f9a/flybody/fruitfly/assets/fruitfly.xml#L664) | [geometry/inference input L664](https://github.com/TuragaLab/flybody/blob/d015e9bfe441bd90ae431bac24c55cb74bdbce26/flybody/fruitfly/assets/fruitfly.xml#L664) |
| tarsus4_T3_left / com_registered | [-0.177273836, 0.102928352, -0.11984321] | [-0.177273836, 0.102928352, -0.11984321] | [-0.177273836, 0.102928352, -0.11984321] | [0, 0, 0] | eligible; compared after Kabsch alignment | [geometry/inference input L773](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/flybody/fruitfly.xml#L773) | [geometry/inference input L668](https://github.com/TuragaLab/flybody/blob/736608121847c3c025fd02a629bdb016a3294f9a/flybody/fruitfly/assets/fruitfly.xml#L668) | [geometry/inference input L668](https://github.com/TuragaLab/flybody/blob/d015e9bfe441bd90ae431bac24c55cb74bdbce26/flybody/fruitfly/assets/fruitfly.xml#L668) |
| claw_T3_left / com_registered | [-0.18561139, 0.10728139, -0.12646233] | [-0.18561139, 0.10728139, -0.12646233] | [-0.18561139, 0.10728139, -0.12646233] | [0, 0, 0] | eligible; compared after Kabsch alignment | [geometry/inference input L779](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/flybody/fruitfly.xml#L779) | [geometry/inference input L672](https://github.com/TuragaLab/flybody/blob/736608121847c3c025fd02a629bdb016a3294f9a/flybody/fruitfly/assets/fruitfly.xml#L672) | [geometry/inference input L672](https://github.com/TuragaLab/flybody/blob/d015e9bfe441bd90ae431bac24c55cb74bdbce26/flybody/fruitfly/assets/fruitfly.xml#L672) |
| coxa_T3_right / com_registered | [-0.0427806437, -0.0112385753, -0.0524285468] | [-0.0427806437, -0.0112385753, -0.0524285468] | [-0.0427806437, -0.0112385753, -0.0524285468] | [0, 0, 0] | eligible; compared after Kabsch alignment | [geometry/inference input L795](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/flybody/fruitfly.xml#L795) | [geometry/inference input L685](https://github.com/TuragaLab/flybody/blob/736608121847c3c025fd02a629bdb016a3294f9a/flybody/fruitfly/assets/fruitfly.xml#L685) | [geometry/inference input L685](https://github.com/TuragaLab/flybody/blob/d015e9bfe441bd90ae431bac24c55cb74bdbce26/flybody/fruitfly/assets/fruitfly.xml#L685) |
| femur_T3_right / com_registered | [-0.0675262051, -0.0335105447, -0.0449245659] | [-0.0675262051, -0.0335105447, -0.0449245659] | [-0.0675262051, -0.0335105447, -0.0449245659] | [0, 0, 0] | eligible; compared after Kabsch alignment | [geometry/inference input L802](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/flybody/fruitfly.xml#L802) | [geometry/inference input L691](https://github.com/TuragaLab/flybody/blob/736608121847c3c025fd02a629bdb016a3294f9a/flybody/fruitfly/assets/fruitfly.xml#L691) | [geometry/inference input L691](https://github.com/TuragaLab/flybody/blob/d015e9bfe441bd90ae431bac24c55cb74bdbce26/flybody/fruitfly/assets/fruitfly.xml#L691) |
| tibia_T3_right / com_registered | [-0.111723029, -0.069838992, -0.0512409879] | [-0.111723029, -0.069838992, -0.0512409879] | [-0.111723029, -0.069838992, -0.0512409879] | [0, 0, 0] | eligible; compared after Kabsch alignment | [geometry/inference input L809](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/flybody/fruitfly.xml#L809) | [geometry/inference input L696](https://github.com/TuragaLab/flybody/blob/736608121847c3c025fd02a629bdb016a3294f9a/flybody/fruitfly/assets/fruitfly.xml#L696) | [geometry/inference input L696](https://github.com/TuragaLab/flybody/blob/d015e9bfe441bd90ae431bac24c55cb74bdbce26/flybody/fruitfly/assets/fruitfly.xml#L696) |
| tarsus_T3_right / com_registered | [-0.136281452, -0.0813663554, -0.0912621524] | [-0.136281452, -0.0813663554, -0.0912621524] | [-0.136281452, -0.0813663554, -0.0912621524] | [0, 0, 0] | eligible; compared after Kabsch alignment | [geometry/inference input L815](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/flybody/fruitfly.xml#L815) | [geometry/inference input L700](https://github.com/TuragaLab/flybody/blob/736608121847c3c025fd02a629bdb016a3294f9a/flybody/fruitfly/assets/fruitfly.xml#L700) | [geometry/inference input L700](https://github.com/TuragaLab/flybody/blob/d015e9bfe441bd90ae431bac24c55cb74bdbce26/flybody/fruitfly/assets/fruitfly.xml#L700) |
| tarsus2_T3_right / com_registered | [-0.157885653, -0.0930221983, -0.105959253] | [-0.157885653, -0.0930221983, -0.105959253] | [-0.157885653, -0.0930221983, -0.105959253] | [0, 0, 0] | eligible; compared after Kabsch alignment | [geometry/inference input L822](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/flybody/fruitfly.xml#L822) | [geometry/inference input L705](https://github.com/TuragaLab/flybody/blob/736608121847c3c025fd02a629bdb016a3294f9a/flybody/fruitfly/assets/fruitfly.xml#L705) | [geometry/inference input L705](https://github.com/TuragaLab/flybody/blob/d015e9bfe441bd90ae431bac24c55cb74bdbce26/flybody/fruitfly/assets/fruitfly.xml#L705) |
| tarsus3_T3_right / com_registered | [-0.169639507, -0.0993671026, -0.113499647] | [-0.169639507, -0.0993671026, -0.113499647] | [-0.169639507, -0.0993671026, -0.113499647] | [0, 0, 0] | eligible; compared after Kabsch alignment | [geometry/inference input L828](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/flybody/fruitfly.xml#L828) | [geometry/inference input L709](https://github.com/TuragaLab/flybody/blob/736608121847c3c025fd02a629bdb016a3294f9a/flybody/fruitfly/assets/fruitfly.xml#L709) | [geometry/inference input L709](https://github.com/TuragaLab/flybody/blob/d015e9bfe441bd90ae431bac24c55cb74bdbce26/flybody/fruitfly/assets/fruitfly.xml#L709) |
| tarsus4_T3_right / com_registered | [-0.177026196, -0.103327573, -0.119599694] | [-0.177026196, -0.103327573, -0.119599694] | [-0.177026196, -0.103327573, -0.119599694] | [0, 0, 0] | eligible; compared after Kabsch alignment | [geometry/inference input L834](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/flybody/fruitfly.xml#L834) | [geometry/inference input L713](https://github.com/TuragaLab/flybody/blob/736608121847c3c025fd02a629bdb016a3294f9a/flybody/fruitfly/assets/fruitfly.xml#L713) | [geometry/inference input L713](https://github.com/TuragaLab/flybody/blob/d015e9bfe441bd90ae431bac24c55cb74bdbce26/flybody/fruitfly/assets/fruitfly.xml#L713) |
| claw_T3_right / com_registered | [-0.185196579, -0.107619773, -0.12630577] | [-0.185196579, -0.107619773, -0.12630577] | [-0.185196579, -0.107619773, -0.12630577] | [0, 0, 0] | eligible; compared after Kabsch alignment | [geometry/inference input L840](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/flybody/fruitfly.xml#L840) | [geometry/inference input L717](https://github.com/TuragaLab/flybody/blob/736608121847c3c025fd02a629bdb016a3294f9a/flybody/fruitfly/assets/fruitfly.xml#L717) | [geometry/inference input L717](https://github.com/TuragaLab/flybody/blob/d015e9bfe441bd90ae431bac24c55cb74bdbce26/flybody/fruitfly/assets/fruitfly.xml#L717) |

## Mass accounting

Every contributing compiled body mass is listed here so total/subtree sums can be checked. Links point to explicit inertials or to geometry inputs when the compiler inferred a mass. CoM links identify inertial inputs; world coordinates additionally use the ancestor transforms and the registration recorded below.

| M body | M kg / source | S kg / source | H kg / source |
|---|---|---|---|
| thorax | 0.00034 / [geometry/inference input L299](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/flybody/fruitfly.xml#L299) | 0.00034 / [geometry/inference input L308](https://github.com/TuragaLab/flybody/blob/736608121847c3c025fd02a629bdb016a3294f9a/flybody/fruitfly/assets/fruitfly.xml#L308) | 0.00034 / [geometry/inference input L308](https://github.com/TuragaLab/flybody/blob/d015e9bfe441bd90ae431bac24c55cb74bdbce26/flybody/fruitfly/assets/fruitfly.xml#L308) |
| head | 0.00012532987 / [geometry/inference input L316](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/flybody/fruitfly.xml#L316) | 0.00012532987 / [geometry/inference input L326](https://github.com/TuragaLab/flybody/blob/736608121847c3c025fd02a629bdb016a3294f9a/flybody/fruitfly/assets/fruitfly.xml#L326) | 0.00012532987 / [geometry/inference input L326](https://github.com/TuragaLab/flybody/blob/d015e9bfe441bd90ae431bac24c55cb74bdbce26/flybody/fruitfly/assets/fruitfly.xml#L326) |
| rostrum | 1.43419042e-05 / [geometry/inference input L332](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/flybody/fruitfly.xml#L332) | 1.43419042e-05 / [geometry/inference input L338](https://github.com/TuragaLab/flybody/blob/736608121847c3c025fd02a629bdb016a3294f9a/flybody/fruitfly/assets/fruitfly.xml#L338) | 1.43419042e-05 / [geometry/inference input L338](https://github.com/TuragaLab/flybody/blob/d015e9bfe441bd90ae431bac24c55cb74bdbce26/flybody/fruitfly/assets/fruitfly.xml#L338) |
| haustellum | 3.18392749e-06 / [geometry/inference input L343](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/flybody/fruitfly.xml#L343) | 3.18392749e-06 / [geometry/inference input L345](https://github.com/TuragaLab/flybody/blob/736608121847c3c025fd02a629bdb016a3294f9a/flybody/fruitfly/assets/fruitfly.xml#L345) | 3.18392749e-06 / [geometry/inference input L345](https://github.com/TuragaLab/flybody/blob/d015e9bfe441bd90ae431bac24c55cb74bdbce26/flybody/fruitfly/assets/fruitfly.xml#L345) |
| labrum_left | 2.08585071e-06 / [geometry/inference input L351](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/flybody/fruitfly.xml#L351) | 2.08585071e-06 / [geometry/inference input L351](https://github.com/TuragaLab/flybody/blob/736608121847c3c025fd02a629bdb016a3294f9a/flybody/fruitfly/assets/fruitfly.xml#L351) | 2.08585071e-06 / [geometry/inference input L351](https://github.com/TuragaLab/flybody/blob/d015e9bfe441bd90ae431bac24c55cb74bdbce26/flybody/fruitfly/assets/fruitfly.xml#L351) |
| labrum_right | 2.08585122e-06 / [geometry/inference input L358](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/flybody/fruitfly.xml#L358) | 2.08585122e-06 / [geometry/inference input L356](https://github.com/TuragaLab/flybody/blob/736608121847c3c025fd02a629bdb016a3294f9a/flybody/fruitfly/assets/fruitfly.xml#L356) | 2.08585122e-06 / [geometry/inference input L356](https://github.com/TuragaLab/flybody/blob/d015e9bfe441bd90ae431bac24c55cb74bdbce26/flybody/fruitfly/assets/fruitfly.xml#L356) |
| antenna_left | 1.44075791e-06 / [geometry/inference input L367](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/flybody/fruitfly.xml#L367) | 1.44075791e-06 / [geometry/inference input L363](https://github.com/TuragaLab/flybody/blob/736608121847c3c025fd02a629bdb016a3294f9a/flybody/fruitfly/assets/fruitfly.xml#L363) | 1.44075791e-06 / [geometry/inference input L363](https://github.com/TuragaLab/flybody/blob/d015e9bfe441bd90ae431bac24c55cb74bdbce26/flybody/fruitfly/assets/fruitfly.xml#L363) |
| antenna_right | 1.44076188e-06 / [geometry/inference input L377](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/flybody/fruitfly.xml#L377) | 1.44076188e-06 / [geometry/inference input L371](https://github.com/TuragaLab/flybody/blob/736608121847c3c025fd02a629bdb016a3294f9a/flybody/fruitfly/assets/fruitfly.xml#L371) | 1.44076188e-06 / [geometry/inference input L371](https://github.com/TuragaLab/flybody/blob/d015e9bfe441bd90ae431bac24c55cb74bdbce26/flybody/fruitfly/assets/fruitfly.xml#L371) |
| wing_left | 8e-06 / [geometry/inference input L388](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/flybody/fruitfly.xml#L388) | 8e-06 / [geometry/inference input L380](https://github.com/TuragaLab/flybody/blob/736608121847c3c025fd02a629bdb016a3294f9a/flybody/fruitfly/assets/fruitfly.xml#L380) | 8e-06 / [geometry/inference input L380](https://github.com/TuragaLab/flybody/blob/d015e9bfe441bd90ae431bac24c55cb74bdbce26/flybody/fruitfly/assets/fruitfly.xml#L380) |
| wing_right | 8e-06 / [geometry/inference input L405](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/flybody/fruitfly.xml#L405) | 8e-06 / [geometry/inference input L391](https://github.com/TuragaLab/flybody/blob/736608121847c3c025fd02a629bdb016a3294f9a/flybody/fruitfly/assets/fruitfly.xml#L391) | 8e-06 / [geometry/inference input L391](https://github.com/TuragaLab/flybody/blob/d015e9bfe441bd90ae431bac24c55cb74bdbce26/flybody/fruitfly/assets/fruitfly.xml#L391) |
| abdomen | 1.57666981e-05 / [geometry/inference input L422](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/flybody/fruitfly.xml#L422) | 1.57666981e-05 / [geometry/inference input L402](https://github.com/TuragaLab/flybody/blob/736608121847c3c025fd02a629bdb016a3294f9a/flybody/fruitfly/assets/fruitfly.xml#L402) | 1.57666981e-05 / [geometry/inference input L402](https://github.com/TuragaLab/flybody/blob/d015e9bfe441bd90ae431bac24c55cb74bdbce26/flybody/fruitfly/assets/fruitfly.xml#L402) |
| abdomen_2 | 5.55757646e-05 / [geometry/inference input L430](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/flybody/fruitfly.xml#L430) | 5.55757646e-05 / [geometry/inference input L408](https://github.com/TuragaLab/flybody/blob/736608121847c3c025fd02a629bdb016a3294f9a/flybody/fruitfly/assets/fruitfly.xml#L408) | 5.55757646e-05 / [geometry/inference input L408](https://github.com/TuragaLab/flybody/blob/d015e9bfe441bd90ae431bac24c55cb74bdbce26/flybody/fruitfly/assets/fruitfly.xml#L408) |
| abdomen_3 | 8.82948912e-05 / [geometry/inference input L438](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/flybody/fruitfly.xml#L438) | 8.82948912e-05 / [geometry/inference input L414](https://github.com/TuragaLab/flybody/blob/736608121847c3c025fd02a629bdb016a3294f9a/flybody/fruitfly/assets/fruitfly.xml#L414) | 8.82948912e-05 / [geometry/inference input L414](https://github.com/TuragaLab/flybody/blob/d015e9bfe441bd90ae431bac24c55cb74bdbce26/flybody/fruitfly/assets/fruitfly.xml#L414) |
| abdomen_4 | 8.21151979e-05 / [geometry/inference input L446](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/flybody/fruitfly.xml#L446) | 8.21151979e-05 / [geometry/inference input L420](https://github.com/TuragaLab/flybody/blob/736608121847c3c025fd02a629bdb016a3294f9a/flybody/fruitfly/assets/fruitfly.xml#L420) | 8.21151979e-05 / [geometry/inference input L420](https://github.com/TuragaLab/flybody/blob/d015e9bfe441bd90ae431bac24c55cb74bdbce26/flybody/fruitfly/assets/fruitfly.xml#L420) |
| abdomen_5 | 6.44139913e-05 / [geometry/inference input L454](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/flybody/fruitfly.xml#L454) | 6.44139913e-05 / [geometry/inference input L426](https://github.com/TuragaLab/flybody/blob/736608121847c3c025fd02a629bdb016a3294f9a/flybody/fruitfly/assets/fruitfly.xml#L426) | 6.44139913e-05 / [geometry/inference input L426](https://github.com/TuragaLab/flybody/blob/d015e9bfe441bd90ae431bac24c55cb74bdbce26/flybody/fruitfly/assets/fruitfly.xml#L426) |
| abdomen_6 | 4.2752835e-05 / [geometry/inference input L462](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/flybody/fruitfly.xml#L462) | 4.2752835e-05 / [geometry/inference input L432](https://github.com/TuragaLab/flybody/blob/736608121847c3c025fd02a629bdb016a3294f9a/flybody/fruitfly/assets/fruitfly.xml#L432) | 4.2752835e-05 / [geometry/inference input L432](https://github.com/TuragaLab/flybody/blob/d015e9bfe441bd90ae431bac24c55cb74bdbce26/flybody/fruitfly/assets/fruitfly.xml#L432) |
| abdomen_7 | 3.12857154e-05 / [geometry/inference input L471](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/flybody/fruitfly.xml#L471) | 3.12857154e-05 / [geometry/inference input L438](https://github.com/TuragaLab/flybody/blob/736608121847c3c025fd02a629bdb016a3294f9a/flybody/fruitfly/assets/fruitfly.xml#L438) | 3.12857154e-05 / [geometry/inference input L438](https://github.com/TuragaLab/flybody/blob/d015e9bfe441bd90ae431bac24c55cb74bdbce26/flybody/fruitfly/assets/fruitfly.xml#L438) |
| haltere_left | 8.21704264e-07 / [geometry/inference input L489](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/flybody/fruitfly.xml#L489) | 8.21704264e-07 / [geometry/inference input L452](https://github.com/TuragaLab/flybody/blob/736608121847c3c025fd02a629bdb016a3294f9a/flybody/fruitfly/assets/fruitfly.xml#L452) | 8.21704264e-07 / [geometry/inference input L452](https://github.com/TuragaLab/flybody/blob/d015e9bfe441bd90ae431bac24c55cb74bdbce26/flybody/fruitfly/assets/fruitfly.xml#L452) |
| haltere_right | 8.21703548e-07 / [geometry/inference input L493](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/flybody/fruitfly.xml#L493) | 8.21703548e-07 / [geometry/inference input L456](https://github.com/TuragaLab/flybody/blob/736608121847c3c025fd02a629bdb016a3294f9a/flybody/fruitfly/assets/fruitfly.xml#L456) | 8.21703548e-07 / [geometry/inference input L456](https://github.com/TuragaLab/flybody/blob/d015e9bfe441bd90ae431bac24c55cb74bdbce26/flybody/fruitfly/assets/fruitfly.xml#L456) |
| coxa_T1_left | 5.75633824e-06 / [geometry/inference input L497](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/flybody/fruitfly.xml#L497) | 5.75633824e-06 / [geometry/inference input L460](https://github.com/TuragaLab/flybody/blob/736608121847c3c025fd02a629bdb016a3294f9a/flybody/fruitfly/assets/fruitfly.xml#L460) | 5.75633824e-06 / [geometry/inference input L460](https://github.com/TuragaLab/flybody/blob/d015e9bfe441bd90ae431bac24c55cb74bdbce26/flybody/fruitfly/assets/fruitfly.xml#L460) |
| femur_T1_left | 7.86965786e-06 / [geometry/inference input L504](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/flybody/fruitfly.xml#L504) | 7.86965786e-06 / [geometry/inference input L466](https://github.com/TuragaLab/flybody/blob/736608121847c3c025fd02a629bdb016a3294f9a/flybody/fruitfly/assets/fruitfly.xml#L466) | 7.86965786e-06 / [geometry/inference input L466](https://github.com/TuragaLab/flybody/blob/d015e9bfe441bd90ae431bac24c55cb74bdbce26/flybody/fruitfly/assets/fruitfly.xml#L466) |
| tibia_T1_left | 1.97683593e-06 / [geometry/inference input L510](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/flybody/fruitfly.xml#L510) | 1.97683593e-06 / [geometry/inference input L471](https://github.com/TuragaLab/flybody/blob/736608121847c3c025fd02a629bdb016a3294f9a/flybody/fruitfly/assets/fruitfly.xml#L471) | 1.97683593e-06 / [geometry/inference input L471](https://github.com/TuragaLab/flybody/blob/d015e9bfe441bd90ae431bac24c55cb74bdbce26/flybody/fruitfly/assets/fruitfly.xml#L471) |
| tarsus_T1_left | 2.66827878e-07 / [geometry/inference input L515](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/flybody/fruitfly.xml#L515) | 2.66827878e-07 / [geometry/inference input L475](https://github.com/TuragaLab/flybody/blob/736608121847c3c025fd02a629bdb016a3294f9a/flybody/fruitfly/assets/fruitfly.xml#L475) | 2.66827878e-07 / [geometry/inference input L475](https://github.com/TuragaLab/flybody/blob/d015e9bfe441bd90ae431bac24c55cb74bdbce26/flybody/fruitfly/assets/fruitfly.xml#L475) |
| tarsus2_T1_left | 1.04493819e-07 / [geometry/inference input L522](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/flybody/fruitfly.xml#L522) | 1.04493819e-07 / [geometry/inference input L480](https://github.com/TuragaLab/flybody/blob/736608121847c3c025fd02a629bdb016a3294f9a/flybody/fruitfly/assets/fruitfly.xml#L480) | 1.04493819e-07 / [geometry/inference input L480](https://github.com/TuragaLab/flybody/blob/d015e9bfe441bd90ae431bac24c55cb74bdbce26/flybody/fruitfly/assets/fruitfly.xml#L480) |
| tarsus3_T1_left | 6.37197743e-08 / [geometry/inference input L528](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/flybody/fruitfly.xml#L528) | 6.37197743e-08 / [geometry/inference input L484](https://github.com/TuragaLab/flybody/blob/736608121847c3c025fd02a629bdb016a3294f9a/flybody/fruitfly/assets/fruitfly.xml#L484) | 6.37197743e-08 / [geometry/inference input L484](https://github.com/TuragaLab/flybody/blob/d015e9bfe441bd90ae431bac24c55cb74bdbce26/flybody/fruitfly/assets/fruitfly.xml#L484) |
| tarsus4_T1_left | 4.97735742e-08 / [geometry/inference input L534](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/flybody/fruitfly.xml#L534) | 4.97735742e-08 / [geometry/inference input L488](https://github.com/TuragaLab/flybody/blob/736608121847c3c025fd02a629bdb016a3294f9a/flybody/fruitfly/assets/fruitfly.xml#L488) | 4.97735742e-08 / [geometry/inference input L488](https://github.com/TuragaLab/flybody/blob/d015e9bfe441bd90ae431bac24c55cb74bdbce26/flybody/fruitfly/assets/fruitfly.xml#L488) |
| claw_T1_left | 9.32942435e-08 / [geometry/inference input L540](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/flybody/fruitfly.xml#L540) | 9.32942435e-08 / [geometry/inference input L492](https://github.com/TuragaLab/flybody/blob/736608121847c3c025fd02a629bdb016a3294f9a/flybody/fruitfly/assets/fruitfly.xml#L492) | 9.32942435e-08 / [geometry/inference input L492](https://github.com/TuragaLab/flybody/blob/d015e9bfe441bd90ae431bac24c55cb74bdbce26/flybody/fruitfly/assets/fruitfly.xml#L492) |
| coxa_T1_right | 5.75634898e-06 / [geometry/inference input L556](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/flybody/fruitfly.xml#L556) | 5.75634898e-06 / [geometry/inference input L505](https://github.com/TuragaLab/flybody/blob/736608121847c3c025fd02a629bdb016a3294f9a/flybody/fruitfly/assets/fruitfly.xml#L505) | 5.75634898e-06 / [geometry/inference input L505](https://github.com/TuragaLab/flybody/blob/d015e9bfe441bd90ae431bac24c55cb74bdbce26/flybody/fruitfly/assets/fruitfly.xml#L505) |
| femur_T1_right | 7.8745948e-06 / [geometry/inference input L563](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/flybody/fruitfly.xml#L563) | 7.8745948e-06 / [geometry/inference input L511](https://github.com/TuragaLab/flybody/blob/736608121847c3c025fd02a629bdb016a3294f9a/flybody/fruitfly/assets/fruitfly.xml#L511) | 7.8745948e-06 / [geometry/inference input L511](https://github.com/TuragaLab/flybody/blob/d015e9bfe441bd90ae431bac24c55cb74bdbce26/flybody/fruitfly/assets/fruitfly.xml#L511) |
| tibia_T1_right | 1.97545926e-06 / [geometry/inference input L570](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/flybody/fruitfly.xml#L570) | 1.97545926e-06 / [geometry/inference input L516](https://github.com/TuragaLab/flybody/blob/736608121847c3c025fd02a629bdb016a3294f9a/flybody/fruitfly/assets/fruitfly.xml#L516) | 1.97545926e-06 / [geometry/inference input L516](https://github.com/TuragaLab/flybody/blob/d015e9bfe441bd90ae431bac24c55cb74bdbce26/flybody/fruitfly/assets/fruitfly.xml#L516) |
| tarsus_T1_right | 2.66828305e-07 / [geometry/inference input L575](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/flybody/fruitfly.xml#L575) | 2.66828305e-07 / [geometry/inference input L520](https://github.com/TuragaLab/flybody/blob/736608121847c3c025fd02a629bdb016a3294f9a/flybody/fruitfly/assets/fruitfly.xml#L520) | 2.66828305e-07 / [geometry/inference input L520](https://github.com/TuragaLab/flybody/blob/d015e9bfe441bd90ae431bac24c55cb74bdbce26/flybody/fruitfly/assets/fruitfly.xml#L520) |
| tarsus2_T1_right | 1.04493686e-07 / [geometry/inference input L582](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/flybody/fruitfly.xml#L582) | 1.04493686e-07 / [geometry/inference input L525](https://github.com/TuragaLab/flybody/blob/736608121847c3c025fd02a629bdb016a3294f9a/flybody/fruitfly/assets/fruitfly.xml#L525) | 1.04493686e-07 / [geometry/inference input L525](https://github.com/TuragaLab/flybody/blob/d015e9bfe441bd90ae431bac24c55cb74bdbce26/flybody/fruitfly/assets/fruitfly.xml#L525) |
| tarsus3_T1_right | 6.37198148e-08 / [geometry/inference input L588](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/flybody/fruitfly.xml#L588) | 6.37198148e-08 / [geometry/inference input L529](https://github.com/TuragaLab/flybody/blob/736608121847c3c025fd02a629bdb016a3294f9a/flybody/fruitfly/assets/fruitfly.xml#L529) | 6.37198148e-08 / [geometry/inference input L529](https://github.com/TuragaLab/flybody/blob/d015e9bfe441bd90ae431bac24c55cb74bdbce26/flybody/fruitfly/assets/fruitfly.xml#L529) |
| tarsus4_T1_right | 4.97733261e-08 / [geometry/inference input L594](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/flybody/fruitfly.xml#L594) | 4.97733261e-08 / [geometry/inference input L533](https://github.com/TuragaLab/flybody/blob/736608121847c3c025fd02a629bdb016a3294f9a/flybody/fruitfly/assets/fruitfly.xml#L533) | 4.97733261e-08 / [geometry/inference input L533](https://github.com/TuragaLab/flybody/blob/d015e9bfe441bd90ae431bac24c55cb74bdbce26/flybody/fruitfly/assets/fruitfly.xml#L533) |
| claw_T1_right | 9.32946342e-08 / [geometry/inference input L600](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/flybody/fruitfly.xml#L600) | 9.32946342e-08 / [geometry/inference input L537](https://github.com/TuragaLab/flybody/blob/736608121847c3c025fd02a629bdb016a3294f9a/flybody/fruitfly/assets/fruitfly.xml#L537) | 9.32946342e-08 / [geometry/inference input L537](https://github.com/TuragaLab/flybody/blob/d015e9bfe441bd90ae431bac24c55cb74bdbce26/flybody/fruitfly/assets/fruitfly.xml#L537) |
| coxa_T2_left | 2.36008915e-06 / [geometry/inference input L616](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/flybody/fruitfly.xml#L616) | 2.36008915e-06 / [geometry/inference input L550](https://github.com/TuragaLab/flybody/blob/736608121847c3c025fd02a629bdb016a3294f9a/flybody/fruitfly/assets/fruitfly.xml#L550) | 2.36008915e-06 / [geometry/inference input L550](https://github.com/TuragaLab/flybody/blob/d015e9bfe441bd90ae431bac24c55cb74bdbce26/flybody/fruitfly/assets/fruitfly.xml#L550) |
| femur_T2_left | 8.00233072e-06 / [geometry/inference input L623](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/flybody/fruitfly.xml#L623) | 8.00233072e-06 / [geometry/inference input L556](https://github.com/TuragaLab/flybody/blob/736608121847c3c025fd02a629bdb016a3294f9a/flybody/fruitfly/assets/fruitfly.xml#L556) | 8.00233072e-06 / [geometry/inference input L556](https://github.com/TuragaLab/flybody/blob/d015e9bfe441bd90ae431bac24c55cb74bdbce26/flybody/fruitfly/assets/fruitfly.xml#L556) |
| tibia_T2_left | 2.62153514e-06 / [geometry/inference input L629](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/flybody/fruitfly.xml#L629) | 2.62153514e-06 / [geometry/inference input L561](https://github.com/TuragaLab/flybody/blob/736608121847c3c025fd02a629bdb016a3294f9a/flybody/fruitfly/assets/fruitfly.xml#L561) | 2.62153514e-06 / [geometry/inference input L561](https://github.com/TuragaLab/flybody/blob/d015e9bfe441bd90ae431bac24c55cb74bdbce26/flybody/fruitfly/assets/fruitfly.xml#L561) |
| tarsus_T2_left | 4.87065831e-07 / [geometry/inference input L633](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/flybody/fruitfly.xml#L633) | 4.87065831e-07 / [geometry/inference input L565](https://github.com/TuragaLab/flybody/blob/736608121847c3c025fd02a629bdb016a3294f9a/flybody/fruitfly/assets/fruitfly.xml#L565) | 4.87065831e-07 / [geometry/inference input L565](https://github.com/TuragaLab/flybody/blob/d015e9bfe441bd90ae431bac24c55cb74bdbce26/flybody/fruitfly/assets/fruitfly.xml#L565) |
| tarsus2_T2_left | 1.36230783e-07 / [geometry/inference input L640](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/flybody/fruitfly.xml#L640) | 1.36230783e-07 / [geometry/inference input L570](https://github.com/TuragaLab/flybody/blob/736608121847c3c025fd02a629bdb016a3294f9a/flybody/fruitfly/assets/fruitfly.xml#L570) | 1.36230783e-07 / [geometry/inference input L570](https://github.com/TuragaLab/flybody/blob/d015e9bfe441bd90ae431bac24c55cb74bdbce26/flybody/fruitfly/assets/fruitfly.xml#L570) |
| tarsus3_T2_left | 6.80681885e-08 / [geometry/inference input L646](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/flybody/fruitfly.xml#L646) | 6.80681885e-08 / [geometry/inference input L574](https://github.com/TuragaLab/flybody/blob/736608121847c3c025fd02a629bdb016a3294f9a/flybody/fruitfly/assets/fruitfly.xml#L574) | 6.80681885e-08 / [geometry/inference input L574](https://github.com/TuragaLab/flybody/blob/d015e9bfe441bd90ae431bac24c55cb74bdbce26/flybody/fruitfly/assets/fruitfly.xml#L574) |
| tarsus4_T2_left | 5.5094794e-08 / [geometry/inference input L652](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/flybody/fruitfly.xml#L652) | 5.5094794e-08 / [geometry/inference input L578](https://github.com/TuragaLab/flybody/blob/736608121847c3c025fd02a629bdb016a3294f9a/flybody/fruitfly/assets/fruitfly.xml#L578) | 5.5094794e-08 / [geometry/inference input L578](https://github.com/TuragaLab/flybody/blob/d015e9bfe441bd90ae431bac24c55cb74bdbce26/flybody/fruitfly/assets/fruitfly.xml#L578) |
| claw_T2_left | 9.946097e-08 / [geometry/inference input L658](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/flybody/fruitfly.xml#L658) | 9.946097e-08 / [geometry/inference input L582](https://github.com/TuragaLab/flybody/blob/736608121847c3c025fd02a629bdb016a3294f9a/flybody/fruitfly/assets/fruitfly.xml#L582) | 9.946097e-08 / [geometry/inference input L582](https://github.com/TuragaLab/flybody/blob/d015e9bfe441bd90ae431bac24c55cb74bdbce26/flybody/fruitfly/assets/fruitfly.xml#L582) |
| coxa_T2_right | 2.36008993e-06 / [geometry/inference input L674](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/flybody/fruitfly.xml#L674) | 2.36008993e-06 / [geometry/inference input L595](https://github.com/TuragaLab/flybody/blob/736608121847c3c025fd02a629bdb016a3294f9a/flybody/fruitfly/assets/fruitfly.xml#L595) | 2.36008993e-06 / [geometry/inference input L595](https://github.com/TuragaLab/flybody/blob/d015e9bfe441bd90ae431bac24c55cb74bdbce26/flybody/fruitfly/assets/fruitfly.xml#L595) |
| femur_T2_right | 8.00584159e-06 / [geometry/inference input L682](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/flybody/fruitfly.xml#L682) | 8.00584159e-06 / [geometry/inference input L601](https://github.com/TuragaLab/flybody/blob/736608121847c3c025fd02a629bdb016a3294f9a/flybody/fruitfly/assets/fruitfly.xml#L601) | 8.00584159e-06 / [geometry/inference input L601](https://github.com/TuragaLab/flybody/blob/d015e9bfe441bd90ae431bac24c55cb74bdbce26/flybody/fruitfly/assets/fruitfly.xml#L601) |
| tibia_T2_right | 2.62232814e-06 / [geometry/inference input L689](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/flybody/fruitfly.xml#L689) | 2.62232814e-06 / [geometry/inference input L606](https://github.com/TuragaLab/flybody/blob/736608121847c3c025fd02a629bdb016a3294f9a/flybody/fruitfly/assets/fruitfly.xml#L606) | 2.62232814e-06 / [geometry/inference input L606](https://github.com/TuragaLab/flybody/blob/d015e9bfe441bd90ae431bac24c55cb74bdbce26/flybody/fruitfly/assets/fruitfly.xml#L606) |
| tarsus_T2_right | 4.87069884e-07 / [geometry/inference input L694](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/flybody/fruitfly.xml#L694) | 4.87069884e-07 / [geometry/inference input L610](https://github.com/TuragaLab/flybody/blob/736608121847c3c025fd02a629bdb016a3294f9a/flybody/fruitfly/assets/fruitfly.xml#L610) | 4.87069884e-07 / [geometry/inference input L610](https://github.com/TuragaLab/flybody/blob/d015e9bfe441bd90ae431bac24c55cb74bdbce26/flybody/fruitfly/assets/fruitfly.xml#L610) |
| tarsus2_T2_right | 1.36232189e-07 / [geometry/inference input L701](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/flybody/fruitfly.xml#L701) | 1.36232189e-07 / [geometry/inference input L615](https://github.com/TuragaLab/flybody/blob/736608121847c3c025fd02a629bdb016a3294f9a/flybody/fruitfly/assets/fruitfly.xml#L615) | 1.36232189e-07 / [geometry/inference input L615](https://github.com/TuragaLab/flybody/blob/d015e9bfe441bd90ae431bac24c55cb74bdbce26/flybody/fruitfly/assets/fruitfly.xml#L615) |
| tarsus3_T2_right | 6.80686915e-08 / [geometry/inference input L707](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/flybody/fruitfly.xml#L707) | 6.80686915e-08 / [geometry/inference input L619](https://github.com/TuragaLab/flybody/blob/736608121847c3c025fd02a629bdb016a3294f9a/flybody/fruitfly/assets/fruitfly.xml#L619) | 6.80686915e-08 / [geometry/inference input L619](https://github.com/TuragaLab/flybody/blob/d015e9bfe441bd90ae431bac24c55cb74bdbce26/flybody/fruitfly/assets/fruitfly.xml#L619) |
| tarsus4_T2_right | 5.50951795e-08 / [geometry/inference input L713](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/flybody/fruitfly.xml#L713) | 5.50951795e-08 / [geometry/inference input L623](https://github.com/TuragaLab/flybody/blob/736608121847c3c025fd02a629bdb016a3294f9a/flybody/fruitfly/assets/fruitfly.xml#L623) | 5.50951795e-08 / [geometry/inference input L623](https://github.com/TuragaLab/flybody/blob/d015e9bfe441bd90ae431bac24c55cb74bdbce26/flybody/fruitfly/assets/fruitfly.xml#L623) |
| claw_T2_right | 9.946179e-08 / [geometry/inference input L719](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/flybody/fruitfly.xml#L719) | 9.946179e-08 / [geometry/inference input L627](https://github.com/TuragaLab/flybody/blob/736608121847c3c025fd02a629bdb016a3294f9a/flybody/fruitfly/assets/fruitfly.xml#L627) | 9.946179e-08 / [geometry/inference input L627](https://github.com/TuragaLab/flybody/blob/d015e9bfe441bd90ae431bac24c55cb74bdbce26/flybody/fruitfly/assets/fruitfly.xml#L627) |
| coxa_T3_left | 2.99346744e-06 / [geometry/inference input L735](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/flybody/fruitfly.xml#L735) | 2.99346744e-06 / [geometry/inference input L640](https://github.com/TuragaLab/flybody/blob/736608121847c3c025fd02a629bdb016a3294f9a/flybody/fruitfly/assets/fruitfly.xml#L640) | 2.99346744e-06 / [geometry/inference input L640](https://github.com/TuragaLab/flybody/blob/d015e9bfe441bd90ae431bac24c55cb74bdbce26/flybody/fruitfly/assets/fruitfly.xml#L640) |
| femur_T3_left | 1.0745586e-05 / [geometry/inference input L742](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/flybody/fruitfly.xml#L742) | 1.0745586e-05 / [geometry/inference input L646](https://github.com/TuragaLab/flybody/blob/736608121847c3c025fd02a629bdb016a3294f9a/flybody/fruitfly/assets/fruitfly.xml#L646) | 1.0745586e-05 / [geometry/inference input L646](https://github.com/TuragaLab/flybody/blob/d015e9bfe441bd90ae431bac24c55cb74bdbce26/flybody/fruitfly/assets/fruitfly.xml#L646) |
| tibia_T3_left | 3.64000785e-06 / [geometry/inference input L749](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/flybody/fruitfly.xml#L749) | 3.64000785e-06 / [geometry/inference input L651](https://github.com/TuragaLab/flybody/blob/736608121847c3c025fd02a629bdb016a3294f9a/flybody/fruitfly/assets/fruitfly.xml#L651) | 3.64000785e-06 / [geometry/inference input L651](https://github.com/TuragaLab/flybody/blob/d015e9bfe441bd90ae431bac24c55cb74bdbce26/flybody/fruitfly/assets/fruitfly.xml#L651) |
| tarsus_T3_left | 6.34076957e-07 / [geometry/inference input L754](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/flybody/fruitfly.xml#L754) | 6.34076957e-07 / [geometry/inference input L655](https://github.com/TuragaLab/flybody/blob/736608121847c3c025fd02a629bdb016a3294f9a/flybody/fruitfly/assets/fruitfly.xml#L655) | 6.34076957e-07 / [geometry/inference input L655](https://github.com/TuragaLab/flybody/blob/d015e9bfe441bd90ae431bac24c55cb74bdbce26/flybody/fruitfly/assets/fruitfly.xml#L655) |
| tarsus2_T3_left | 1.74093974e-07 / [geometry/inference input L761](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/flybody/fruitfly.xml#L761) | 1.74093974e-07 / [geometry/inference input L660](https://github.com/TuragaLab/flybody/blob/736608121847c3c025fd02a629bdb016a3294f9a/flybody/fruitfly/assets/fruitfly.xml#L660) | 1.74093974e-07 / [geometry/inference input L660](https://github.com/TuragaLab/flybody/blob/d015e9bfe441bd90ae431bac24c55cb74bdbce26/flybody/fruitfly/assets/fruitfly.xml#L660) |
| tarsus3_T3_left | 7.25392396e-08 / [geometry/inference input L767](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/flybody/fruitfly.xml#L767) | 7.25392396e-08 / [geometry/inference input L664](https://github.com/TuragaLab/flybody/blob/736608121847c3c025fd02a629bdb016a3294f9a/flybody/fruitfly/assets/fruitfly.xml#L664) | 7.25392396e-08 / [geometry/inference input L664](https://github.com/TuragaLab/flybody/blob/d015e9bfe441bd90ae431bac24c55cb74bdbce26/flybody/fruitfly/assets/fruitfly.xml#L664) |
| tarsus4_T3_left | 5.9428832e-08 / [geometry/inference input L773](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/flybody/fruitfly.xml#L773) | 5.9428832e-08 / [geometry/inference input L668](https://github.com/TuragaLab/flybody/blob/736608121847c3c025fd02a629bdb016a3294f9a/flybody/fruitfly/assets/fruitfly.xml#L668) | 5.9428832e-08 / [geometry/inference input L668](https://github.com/TuragaLab/flybody/blob/d015e9bfe441bd90ae431bac24c55cb74bdbce26/flybody/fruitfly/assets/fruitfly.xml#L668) |
| claw_T3_left | 9.69841803e-08 / [geometry/inference input L779](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/flybody/fruitfly.xml#L779) | 9.69841803e-08 / [geometry/inference input L672](https://github.com/TuragaLab/flybody/blob/736608121847c3c025fd02a629bdb016a3294f9a/flybody/fruitfly/assets/fruitfly.xml#L672) | 9.69841803e-08 / [geometry/inference input L672](https://github.com/TuragaLab/flybody/blob/d015e9bfe441bd90ae431bac24c55cb74bdbce26/flybody/fruitfly/assets/fruitfly.xml#L672) |
| coxa_T3_right | 2.99347121e-06 / [geometry/inference input L795](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/flybody/fruitfly.xml#L795) | 2.99347121e-06 / [geometry/inference input L685](https://github.com/TuragaLab/flybody/blob/736608121847c3c025fd02a629bdb016a3294f9a/flybody/fruitfly/assets/fruitfly.xml#L685) | 2.99347121e-06 / [geometry/inference input L685](https://github.com/TuragaLab/flybody/blob/d015e9bfe441bd90ae431bac24c55cb74bdbce26/flybody/fruitfly/assets/fruitfly.xml#L685) |
| femur_T3_right | 1.07492896e-05 / [geometry/inference input L802](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/flybody/fruitfly.xml#L802) | 1.07492896e-05 / [geometry/inference input L691](https://github.com/TuragaLab/flybody/blob/736608121847c3c025fd02a629bdb016a3294f9a/flybody/fruitfly/assets/fruitfly.xml#L691) | 1.07492896e-05 / [geometry/inference input L691](https://github.com/TuragaLab/flybody/blob/d015e9bfe441bd90ae431bac24c55cb74bdbce26/flybody/fruitfly/assets/fruitfly.xml#L691) |
| tibia_T3_right | 3.63845577e-06 / [geometry/inference input L809](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/flybody/fruitfly.xml#L809) | 3.63845577e-06 / [geometry/inference input L696](https://github.com/TuragaLab/flybody/blob/736608121847c3c025fd02a629bdb016a3294f9a/flybody/fruitfly/assets/fruitfly.xml#L696) | 3.63845577e-06 / [geometry/inference input L696](https://github.com/TuragaLab/flybody/blob/d015e9bfe441bd90ae431bac24c55cb74bdbce26/flybody/fruitfly/assets/fruitfly.xml#L696) |
| tarsus_T3_right | 6.34079545e-07 / [geometry/inference input L815](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/flybody/fruitfly.xml#L815) | 6.34079545e-07 / [geometry/inference input L700](https://github.com/TuragaLab/flybody/blob/736608121847c3c025fd02a629bdb016a3294f9a/flybody/fruitfly/assets/fruitfly.xml#L700) | 6.34079545e-07 / [geometry/inference input L700](https://github.com/TuragaLab/flybody/blob/d015e9bfe441bd90ae431bac24c55cb74bdbce26/flybody/fruitfly/assets/fruitfly.xml#L700) |
| tarsus2_T3_right | 1.74094443e-07 / [geometry/inference input L822](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/flybody/fruitfly.xml#L822) | 1.74094443e-07 / [geometry/inference input L705](https://github.com/TuragaLab/flybody/blob/736608121847c3c025fd02a629bdb016a3294f9a/flybody/fruitfly/assets/fruitfly.xml#L705) | 1.74094443e-07 / [geometry/inference input L705](https://github.com/TuragaLab/flybody/blob/d015e9bfe441bd90ae431bac24c55cb74bdbce26/flybody/fruitfly/assets/fruitfly.xml#L705) |
| tarsus3_T3_right | 7.25389922e-08 / [geometry/inference input L828](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/flybody/fruitfly.xml#L828) | 7.25389922e-08 / [geometry/inference input L709](https://github.com/TuragaLab/flybody/blob/736608121847c3c025fd02a629bdb016a3294f9a/flybody/fruitfly/assets/fruitfly.xml#L709) | 7.25389922e-08 / [geometry/inference input L709](https://github.com/TuragaLab/flybody/blob/d015e9bfe441bd90ae431bac24c55cb74bdbce26/flybody/fruitfly/assets/fruitfly.xml#L709) |
| tarsus4_T3_right | 5.94290059e-08 / [geometry/inference input L834](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/flybody/fruitfly.xml#L834) | 5.94290059e-08 / [geometry/inference input L713](https://github.com/TuragaLab/flybody/blob/736608121847c3c025fd02a629bdb016a3294f9a/flybody/fruitfly/assets/fruitfly.xml#L713) | 5.94290059e-08 / [geometry/inference input L713](https://github.com/TuragaLab/flybody/blob/d015e9bfe441bd90ae431bac24c55cb74bdbce26/flybody/fruitfly/assets/fruitfly.xml#L713) |
| claw_T3_right | 9.69843473e-08 / [geometry/inference input L840](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/flybody/fruitfly.xml#L840) | 9.69843473e-08 / [geometry/inference input L717](https://github.com/TuragaLab/flybody/blob/736608121847c3c025fd02a629bdb016a3294f9a/flybody/fruitfly/assets/fruitfly.xml#L717) | 9.69843473e-08 / [geometry/inference input L717](https://github.com/TuragaLab/flybody/blob/d015e9bfe441bd90ae431bac24c55cb74bdbce26/flybody/fruitfly/assets/fruitfly.xml#L717) |

## Coverage and unmatched elements

```json
{
  "mapping_h": {
    "bodies": {
      "thorax": "thorax",
      "head": "head",
      "rostrum": "rostrum",
      "haustellum": "haustellum",
      "labrum_left": "labrum_left",
      "labrum_right": "labrum_right",
      "antenna_left": "antenna_left",
      "antenna_right": "antenna_right",
      "wing_left": "wing_left",
      "wing_right": "wing_right",
      "abdomen": "abdomen",
      "abdomen_2": "abdomen_2",
      "abdomen_3": "abdomen_3",
      "abdomen_4": "abdomen_4",
      "abdomen_5": "abdomen_5",
      "abdomen_6": "abdomen_6",
      "abdomen_7": "abdomen_7",
      "haltere_left": "haltere_left",
      "haltere_right": "haltere_right",
      "coxa_T1_left": "coxa_T1_left",
      "femur_T1_left": "femur_T1_left",
      "tibia_T1_left": "tibia_T1_left",
      "tarsus_T1_left": "tarsus_T1_left",
      "tarsus2_T1_left": "tarsus2_T1_left",
      "tarsus3_T1_left": "tarsus3_T1_left",
      "tarsus4_T1_left": "tarsus4_T1_left",
      "claw_T1_left": "claw_T1_left",
      "coxa_T1_right": "coxa_T1_right",
      "femur_T1_right": "femur_T1_right",
      "tibia_T1_right": "tibia_T1_right",
      "tarsus_T1_right": "tarsus_T1_right",
      "tarsus2_T1_right": "tarsus2_T1_right",
      "tarsus3_T1_right": "tarsus3_T1_right",
      "tarsus4_T1_right": "tarsus4_T1_right",
      "claw_T1_right": "claw_T1_right",
      "coxa_T2_left": "coxa_T2_left",
      "femur_T2_left": "femur_T2_left",
      "tibia_T2_left": "tibia_T2_left",
      "tarsus_T2_left": "tarsus_T2_left",
      "tarsus2_T2_left": "tarsus2_T2_left",
      "tarsus3_T2_left": "tarsus3_T2_left",
      "tarsus4_T2_left": "tarsus4_T2_left",
      "claw_T2_left": "claw_T2_left",
      "coxa_T2_right": "coxa_T2_right",
      "femur_T2_right": "femur_T2_right",
      "tibia_T2_right": "tibia_T2_right",
      "tarsus_T2_right": "tarsus_T2_right",
      "tarsus2_T2_right": "tarsus2_T2_right",
      "tarsus3_T2_right": "tarsus3_T2_right",
      "tarsus4_T2_right": "tarsus4_T2_right",
      "claw_T2_right": "claw_T2_right",
      "coxa_T3_left": "coxa_T3_left",
      "femur_T3_left": "femur_T3_left",
      "tibia_T3_left": "tibia_T3_left",
      "tarsus_T3_left": "tarsus_T3_left",
      "tarsus2_T3_left": "tarsus2_T3_left",
      "tarsus3_T3_left": "tarsus3_T3_left",
      "tarsus4_T3_left": "tarsus4_T3_left",
      "claw_T3_left": "claw_T3_left",
      "coxa_T3_right": "coxa_T3_right",
      "femur_T3_right": "femur_T3_right",
      "tibia_T3_right": "tibia_T3_right",
      "tarsus_T3_right": "tarsus_T3_right",
      "tarsus2_T3_right": "tarsus2_T3_right",
      "tarsus3_T3_right": "tarsus3_T3_right",
      "tarsus4_T3_right": "tarsus4_T3_right",
      "claw_T3_right": "claw_T3_right"
    },
    "joints": {
      "head_abduct": "head_abduct",
      "head_twist": "head_twist",
      "head": "head",
      "rostrum": "rostrum",
      "haustellum_abduct": "haustellum_abduct",
      "haustellum": "haustellum",
      "labrum_left": "labrum_left",
      "labrum_right": "labrum_right",
      "antenna_abduct_left": "antenna_abduct_left",
      "antenna_twist_left": "antenna_twist_left",
      "antenna_left": "antenna_left",
      "antenna_abduct_right": "antenna_abduct_right",
      "antenna_twist_right": "antenna_twist_right",
      "antenna_right": "antenna_right",
      "wing_yaw_left": "wing_yaw_left",
      "wing_roll_left": "wing_roll_left",
      "wing_pitch_left": "wing_pitch_left",
      "wing_yaw_right": "wing_yaw_right",
      "wing_roll_right": "wing_roll_right",
      "wing_pitch_right": "wing_pitch_right",
      "abdomen_abduct": "abdomen_abduct",
      "abdomen": "abdomen",
      "abdomen_abduct_2": "abdomen_abduct_2",
      "abdomen_2": "abdomen_2",
      "abdomen_abduct_3": "abdomen_abduct_3",
      "abdomen_3": "abdomen_3",
      "abdomen_abduct_4": "abdomen_abduct_4",
      "abdomen_4": "abdomen_4",
      "abdomen_abduct_5": "abdomen_abduct_5",
      "abdomen_5": "abdomen_5",
      "abdomen_abduct_6": "abdomen_abduct_6",
      "abdomen_6": "abdomen_6",
      "abdomen_abduct_7": "abdomen_abduct_7",
      "abdomen_7": "abdomen_7",
      "haltere_left": "haltere_left",
      "haltere_right": "haltere_right",
      "coxa_abduct_T1_left": "coxa_abduct_T1_left",
      "coxa_twist_T1_left": "coxa_twist_T1_left",
      "coxa_T1_left": "coxa_T1_left",
      "femur_twist_T1_left": "femur_twist_T1_left",
      "femur_T1_left": "femur_T1_left",
      "tibia_T1_left": "tibia_T1_left",
      "tarsus_T1_left": "tarsus_T1_left",
      "tarsus2_T1_left": "tarsus2_T1_left",
      "tarsus3_T1_left": "tarsus3_T1_left",
      "tarsus4_T1_left": "tarsus4_T1_left",
      "tarsus5_T1_left": "tarsus5_T1_left",
      "coxa_abduct_T1_right": "coxa_abduct_T1_right",
      "coxa_twist_T1_right": "coxa_twist_T1_right",
      "coxa_T1_right": "coxa_T1_right",
      "femur_twist_T1_right": "femur_twist_T1_right",
      "femur_T1_right": "femur_T1_right",
      "tibia_T1_right": "tibia_T1_right",
      "tarsus_T1_right": "tarsus_T1_right",
      "tarsus2_T1_right": "tarsus2_T1_right",
      "tarsus3_T1_right": "tarsus3_T1_right",
      "tarsus4_T1_right": "tarsus4_T1_right",
      "tarsus5_T1_right": "tarsus5_T1_right",
      "coxa_abduct_T2_left": "coxa_abduct_T2_left",
      "coxa_twist_T2_left": "coxa_twist_T2_left",
      "coxa_T2_left": "coxa_T2_left",
      "femur_twist_T2_left": "femur_twist_T2_left",
      "femur_T2_left": "femur_T2_left",
      "tibia_T2_left": "tibia_T2_left",
      "tarsus_T2_left": "tarsus_T2_left",
      "tarsus2_T2_left": "tarsus2_T2_left",
      "tarsus3_T2_left": "tarsus3_T2_left",
      "tarsus4_T2_left": "tarsus4_T2_left",
      "tarsus5_T2_left": "tarsus5_T2_left",
      "coxa_abduct_T2_right": "coxa_abduct_T2_right",
      "coxa_twist_T2_right": "coxa_twist_T2_right",
      "coxa_T2_right": "coxa_T2_right",
      "femur_twist_T2_right": "femur_twist_T2_right",
      "femur_T2_right": "femur_T2_right",
      "tibia_T2_right": "tibia_T2_right",
      "tarsus_T2_right": "tarsus_T2_right",
      "tarsus2_T2_right": "tarsus2_T2_right",
      "tarsus3_T2_right": "tarsus3_T2_right",
      "tarsus4_T2_right": "tarsus4_T2_right",
      "tarsus5_T2_right": "tarsus5_T2_right",
      "coxa_abduct_T3_left": "coxa_abduct_T3_left",
      "coxa_twist_T3_left": "coxa_twist_T3_left",
      "coxa_T3_left": "coxa_T3_left",
      "femur_twist_T3_left": "femur_twist_T3_left",
      "femur_T3_left": "femur_T3_left",
      "tibia_T3_left": "tibia_T3_left",
      "tarsus_T3_left": "tarsus_T3_left",
      "tarsus2_T3_left": "tarsus2_T3_left",
      "tarsus3_T3_left": "tarsus3_T3_left",
      "tarsus4_T3_left": "tarsus4_T3_left",
      "tarsus5_T3_left": "tarsus5_T3_left",
      "coxa_abduct_T3_right": "coxa_abduct_T3_right",
      "coxa_twist_T3_right": "coxa_twist_T3_right",
      "coxa_T3_right": "coxa_T3_right",
      "femur_twist_T3_right": "femur_twist_T3_right",
      "femur_T3_right": "femur_T3_right",
      "tibia_T3_right": "tibia_T3_right",
      "tarsus_T3_right": "tarsus_T3_right",
      "tarsus2_T3_right": "tarsus2_T3_right",
      "tarsus3_T3_right": "tarsus3_T3_right",
      "tarsus4_T3_right": "tarsus4_T3_right",
      "tarsus5_T3_right": "tarsus5_T3_right"
    },
    "body_methods": {
      "thorax": "name",
      "head": "name",
      "rostrum": "name",
      "haustellum": "name",
      "labrum_left": "name",
      "labrum_right": "name",
      "antenna_left": "name",
      "antenna_right": "name",
      "wing_left": "name",
      "wing_right": "name",
      "abdomen": "name",
      "abdomen_2": "name",
      "abdomen_3": "name",
      "abdomen_4": "name",
      "abdomen_5": "name",
      "abdomen_6": "name",
      "abdomen_7": "name",
      "haltere_left": "name",
      "haltere_right": "name",
      "coxa_T1_left": "name",
      "femur_T1_left": "name",
      "tibia_T1_left": "name",
      "tarsus_T1_left": "name",
      "tarsus2_T1_left": "name",
      "tarsus3_T1_left": "name",
      "tarsus4_T1_left": "name",
      "claw_T1_left": "name",
      "coxa_T1_right": "name",
      "femur_T1_right": "name",
      "tibia_T1_right": "name",
      "tarsus_T1_right": "name",
      "tarsus2_T1_right": "name",
      "tarsus3_T1_right": "name",
      "tarsus4_T1_right": "name",
      "claw_T1_right": "name",
      "coxa_T2_left": "name",
      "femur_T2_left": "name",
      "tibia_T2_left": "name",
      "tarsus_T2_left": "name",
      "tarsus2_T2_left": "name",
      "tarsus3_T2_left": "name",
      "tarsus4_T2_left": "name",
      "claw_T2_left": "name",
      "coxa_T2_right": "name",
      "femur_T2_right": "name",
      "tibia_T2_right": "name",
      "tarsus_T2_right": "name",
      "tarsus2_T2_right": "name",
      "tarsus3_T2_right": "name",
      "tarsus4_T2_right": "name",
      "claw_T2_right": "name",
      "coxa_T3_left": "name",
      "femur_T3_left": "name",
      "tibia_T3_left": "name",
      "tarsus_T3_left": "name",
      "tarsus2_T3_left": "name",
      "tarsus3_T3_left": "name",
      "tarsus4_T3_left": "name",
      "claw_T3_left": "name",
      "coxa_T3_right": "name",
      "femur_T3_right": "name",
      "tibia_T3_right": "name",
      "tarsus_T3_right": "name",
      "tarsus2_T3_right": "name",
      "tarsus3_T3_right": "name",
      "tarsus4_T3_right": "name",
      "claw_T3_right": "name"
    },
    "joint_methods": {
      "head_abduct": "name",
      "head_twist": "name",
      "head": "name",
      "rostrum": "name",
      "haustellum_abduct": "name",
      "haustellum": "name",
      "labrum_left": "name",
      "labrum_right": "name",
      "antenna_abduct_left": "name",
      "antenna_twist_left": "name",
      "antenna_left": "name",
      "antenna_abduct_right": "name",
      "antenna_twist_right": "name",
      "antenna_right": "name",
      "wing_yaw_left": "name",
      "wing_roll_left": "name",
      "wing_pitch_left": "name",
      "wing_yaw_right": "name",
      "wing_roll_right": "name",
      "wing_pitch_right": "name",
      "abdomen_abduct": "name",
      "abdomen": "name",
      "abdomen_abduct_2": "name",
      "abdomen_2": "name",
      "abdomen_abduct_3": "name",
      "abdomen_3": "name",
      "abdomen_abduct_4": "name",
      "abdomen_4": "name",
      "abdomen_abduct_5": "name",
      "abdomen_5": "name",
      "abdomen_abduct_6": "name",
      "abdomen_6": "name",
      "abdomen_abduct_7": "name",
      "abdomen_7": "name",
      "haltere_left": "name",
      "haltere_right": "name",
      "coxa_abduct_T1_left": "name",
      "coxa_twist_T1_left": "name",
      "coxa_T1_left": "name",
      "femur_twist_T1_left": "name",
      "femur_T1_left": "name",
      "tibia_T1_left": "name",
      "tarsus_T1_left": "name",
      "tarsus2_T1_left": "name",
      "tarsus3_T1_left": "name",
      "tarsus4_T1_left": "name",
      "tarsus5_T1_left": "name",
      "coxa_abduct_T1_right": "name",
      "coxa_twist_T1_right": "name",
      "coxa_T1_right": "name",
      "femur_twist_T1_right": "name",
      "femur_T1_right": "name",
      "tibia_T1_right": "name",
      "tarsus_T1_right": "name",
      "tarsus2_T1_right": "name",
      "tarsus3_T1_right": "name",
      "tarsus4_T1_right": "name",
      "tarsus5_T1_right": "name",
      "coxa_abduct_T2_left": "name",
      "coxa_twist_T2_left": "name",
      "coxa_T2_left": "name",
      "femur_twist_T2_left": "name",
      "femur_T2_left": "name",
      "tibia_T2_left": "name",
      "tarsus_T2_left": "name",
      "tarsus2_T2_left": "name",
      "tarsus3_T2_left": "name",
      "tarsus4_T2_left": "name",
      "tarsus5_T2_left": "name",
      "coxa_abduct_T2_right": "name",
      "coxa_twist_T2_right": "name",
      "coxa_T2_right": "name",
      "femur_twist_T2_right": "name",
      "femur_T2_right": "name",
      "tibia_T2_right": "name",
      "tarsus_T2_right": "name",
      "tarsus2_T2_right": "name",
      "tarsus3_T2_right": "name",
      "tarsus4_T2_right": "name",
      "tarsus5_T2_right": "name",
      "coxa_abduct_T3_left": "name",
      "coxa_twist_T3_left": "name",
      "coxa_T3_left": "name",
      "femur_twist_T3_left": "name",
      "femur_T3_left": "name",
      "tibia_T3_left": "name",
      "tarsus_T3_left": "name",
      "tarsus2_T3_left": "name",
      "tarsus3_T3_left": "name",
      "tarsus4_T3_left": "name",
      "tarsus5_T3_left": "name",
      "coxa_abduct_T3_right": "name",
      "coxa_twist_T3_right": "name",
      "coxa_T3_right": "name",
      "femur_twist_T3_right": "name",
      "femur_T3_right": "name",
      "tibia_T3_right": "name",
      "tarsus_T3_right": "name",
      "tarsus2_T3_right": "name",
      "tarsus3_T3_right": "name",
      "tarsus4_T3_right": "name",
      "tarsus5_T3_right": "name"
    },
    "unmatched_m_bodies": [],
    "unmatched_upstream_bodies": [],
    "unmatched_m_joints": [],
    "unmatched_upstream_joints": [],
    "registration_anchor": {
      "M": "thorax",
      "H": "thorax",
      "root_unmatched": false
    }
  },
  "mapping_s": {
    "bodies": {
      "thorax": "thorax",
      "head": "head",
      "rostrum": "rostrum",
      "haustellum": "haustellum",
      "labrum_left": "labrum_left",
      "labrum_right": "labrum_right",
      "antenna_left": "antenna_left",
      "antenna_right": "antenna_right",
      "wing_left": "wing_left",
      "wing_right": "wing_right",
      "abdomen": "abdomen",
      "abdomen_2": "abdomen_2",
      "abdomen_3": "abdomen_3",
      "abdomen_4": "abdomen_4",
      "abdomen_5": "abdomen_5",
      "abdomen_6": "abdomen_6",
      "abdomen_7": "abdomen_7",
      "haltere_left": "haltere_left",
      "haltere_right": "haltere_right",
      "coxa_T1_left": "coxa_T1_left",
      "femur_T1_left": "femur_T1_left",
      "tibia_T1_left": "tibia_T1_left",
      "tarsus_T1_left": "tarsus_T1_left",
      "tarsus2_T1_left": "tarsus2_T1_left",
      "tarsus3_T1_left": "tarsus3_T1_left",
      "tarsus4_T1_left": "tarsus4_T1_left",
      "claw_T1_left": "claw_T1_left",
      "coxa_T1_right": "coxa_T1_right",
      "femur_T1_right": "femur_T1_right",
      "tibia_T1_right": "tibia_T1_right",
      "tarsus_T1_right": "tarsus_T1_right",
      "tarsus2_T1_right": "tarsus2_T1_right",
      "tarsus3_T1_right": "tarsus3_T1_right",
      "tarsus4_T1_right": "tarsus4_T1_right",
      "claw_T1_right": "claw_T1_right",
      "coxa_T2_left": "coxa_T2_left",
      "femur_T2_left": "femur_T2_left",
      "tibia_T2_left": "tibia_T2_left",
      "tarsus_T2_left": "tarsus_T2_left",
      "tarsus2_T2_left": "tarsus2_T2_left",
      "tarsus3_T2_left": "tarsus3_T2_left",
      "tarsus4_T2_left": "tarsus4_T2_left",
      "claw_T2_left": "claw_T2_left",
      "coxa_T2_right": "coxa_T2_right",
      "femur_T2_right": "femur_T2_right",
      "tibia_T2_right": "tibia_T2_right",
      "tarsus_T2_right": "tarsus_T2_right",
      "tarsus2_T2_right": "tarsus2_T2_right",
      "tarsus3_T2_right": "tarsus3_T2_right",
      "tarsus4_T2_right": "tarsus4_T2_right",
      "claw_T2_right": "claw_T2_right",
      "coxa_T3_left": "coxa_T3_left",
      "femur_T3_left": "femur_T3_left",
      "tibia_T3_left": "tibia_T3_left",
      "tarsus_T3_left": "tarsus_T3_left",
      "tarsus2_T3_left": "tarsus2_T3_left",
      "tarsus3_T3_left": "tarsus3_T3_left",
      "tarsus4_T3_left": "tarsus4_T3_left",
      "claw_T3_left": "claw_T3_left",
      "coxa_T3_right": "coxa_T3_right",
      "femur_T3_right": "femur_T3_right",
      "tibia_T3_right": "tibia_T3_right",
      "tarsus_T3_right": "tarsus_T3_right",
      "tarsus2_T3_right": "tarsus2_T3_right",
      "tarsus3_T3_right": "tarsus3_T3_right",
      "tarsus4_T3_right": "tarsus4_T3_right",
      "claw_T3_right": "claw_T3_right"
    },
    "joints": {
      "head_abduct": "head_abduct",
      "head_twist": "head_twist",
      "head": "head",
      "rostrum": "rostrum",
      "haustellum_abduct": "haustellum_abduct",
      "haustellum": "haustellum",
      "labrum_left": "labrum_left",
      "labrum_right": "labrum_right",
      "antenna_abduct_left": "antenna_abduct_left",
      "antenna_twist_left": "antenna_twist_left",
      "antenna_left": "antenna_left",
      "antenna_abduct_right": "antenna_abduct_right",
      "antenna_twist_right": "antenna_twist_right",
      "antenna_right": "antenna_right",
      "wing_yaw_left": "wing_yaw_left",
      "wing_roll_left": "wing_roll_left",
      "wing_pitch_left": "wing_pitch_left",
      "wing_yaw_right": "wing_yaw_right",
      "wing_roll_right": "wing_roll_right",
      "wing_pitch_right": "wing_pitch_right",
      "abdomen_abduct": "abdomen_abduct",
      "abdomen": "abdomen",
      "abdomen_abduct_2": "abdomen_abduct_2",
      "abdomen_2": "abdomen_2",
      "abdomen_abduct_3": "abdomen_abduct_3",
      "abdomen_3": "abdomen_3",
      "abdomen_abduct_4": "abdomen_abduct_4",
      "abdomen_4": "abdomen_4",
      "abdomen_abduct_5": "abdomen_abduct_5",
      "abdomen_5": "abdomen_5",
      "abdomen_abduct_6": "abdomen_abduct_6",
      "abdomen_6": "abdomen_6",
      "abdomen_abduct_7": "abdomen_abduct_7",
      "abdomen_7": "abdomen_7",
      "haltere_left": "haltere_left",
      "haltere_right": "haltere_right",
      "coxa_abduct_T1_left": "coxa_abduct_T1_left",
      "coxa_twist_T1_left": "coxa_twist_T1_left",
      "coxa_T1_left": "coxa_T1_left",
      "femur_twist_T1_left": "femur_twist_T1_left",
      "femur_T1_left": "femur_T1_left",
      "tibia_T1_left": "tibia_T1_left",
      "tarsus_T1_left": "tarsus_T1_left",
      "tarsus2_T1_left": "tarsus2_T1_left",
      "tarsus3_T1_left": "tarsus3_T1_left",
      "tarsus4_T1_left": "tarsus4_T1_left",
      "tarsus5_T1_left": "tarsus5_T1_left",
      "coxa_abduct_T1_right": "coxa_abduct_T1_right",
      "coxa_twist_T1_right": "coxa_twist_T1_right",
      "coxa_T1_right": "coxa_T1_right",
      "femur_twist_T1_right": "femur_twist_T1_right",
      "femur_T1_right": "femur_T1_right",
      "tibia_T1_right": "tibia_T1_right",
      "tarsus_T1_right": "tarsus_T1_right",
      "tarsus2_T1_right": "tarsus2_T1_right",
      "tarsus3_T1_right": "tarsus3_T1_right",
      "tarsus4_T1_right": "tarsus4_T1_right",
      "tarsus5_T1_right": "tarsus5_T1_right",
      "coxa_abduct_T2_left": "coxa_abduct_T2_left",
      "coxa_twist_T2_left": "coxa_twist_T2_left",
      "coxa_T2_left": "coxa_T2_left",
      "femur_twist_T2_left": "femur_twist_T2_left",
      "femur_T2_left": "femur_T2_left",
      "tibia_T2_left": "tibia_T2_left",
      "tarsus_T2_left": "tarsus_T2_left",
      "tarsus2_T2_left": "tarsus2_T2_left",
      "tarsus3_T2_left": "tarsus3_T2_left",
      "tarsus4_T2_left": "tarsus4_T2_left",
      "tarsus5_T2_left": "tarsus5_T2_left",
      "coxa_abduct_T2_right": "coxa_abduct_T2_right",
      "coxa_twist_T2_right": "coxa_twist_T2_right",
      "coxa_T2_right": "coxa_T2_right",
      "femur_twist_T2_right": "femur_twist_T2_right",
      "femur_T2_right": "femur_T2_right",
      "tibia_T2_right": "tibia_T2_right",
      "tarsus_T2_right": "tarsus_T2_right",
      "tarsus2_T2_right": "tarsus2_T2_right",
      "tarsus3_T2_right": "tarsus3_T2_right",
      "tarsus4_T2_right": "tarsus4_T2_right",
      "tarsus5_T2_right": "tarsus5_T2_right",
      "coxa_abduct_T3_left": "coxa_abduct_T3_left",
      "coxa_twist_T3_left": "coxa_twist_T3_left",
      "coxa_T3_left": "coxa_T3_left",
      "femur_twist_T3_left": "femur_twist_T3_left",
      "femur_T3_left": "femur_T3_left",
      "tibia_T3_left": "tibia_T3_left",
      "tarsus_T3_left": "tarsus_T3_left",
      "tarsus2_T3_left": "tarsus2_T3_left",
      "tarsus3_T3_left": "tarsus3_T3_left",
      "tarsus4_T3_left": "tarsus4_T3_left",
      "tarsus5_T3_left": "tarsus5_T3_left",
      "coxa_abduct_T3_right": "coxa_abduct_T3_right",
      "coxa_twist_T3_right": "coxa_twist_T3_right",
      "coxa_T3_right": "coxa_T3_right",
      "femur_twist_T3_right": "femur_twist_T3_right",
      "femur_T3_right": "femur_T3_right",
      "tibia_T3_right": "tibia_T3_right",
      "tarsus_T3_right": "tarsus_T3_right",
      "tarsus2_T3_right": "tarsus2_T3_right",
      "tarsus3_T3_right": "tarsus3_T3_right",
      "tarsus4_T3_right": "tarsus4_T3_right",
      "tarsus5_T3_right": "tarsus5_T3_right"
    },
    "body_methods": {
      "thorax": "name",
      "head": "name",
      "rostrum": "name",
      "haustellum": "name",
      "labrum_left": "name",
      "labrum_right": "name",
      "antenna_left": "name",
      "antenna_right": "name",
      "wing_left": "name",
      "wing_right": "name",
      "abdomen": "name",
      "abdomen_2": "name",
      "abdomen_3": "name",
      "abdomen_4": "name",
      "abdomen_5": "name",
      "abdomen_6": "name",
      "abdomen_7": "name",
      "haltere_left": "name",
      "haltere_right": "name",
      "coxa_T1_left": "name",
      "femur_T1_left": "name",
      "tibia_T1_left": "name",
      "tarsus_T1_left": "name",
      "tarsus2_T1_left": "name",
      "tarsus3_T1_left": "name",
      "tarsus4_T1_left": "name",
      "claw_T1_left": "name",
      "coxa_T1_right": "name",
      "femur_T1_right": "name",
      "tibia_T1_right": "name",
      "tarsus_T1_right": "name",
      "tarsus2_T1_right": "name",
      "tarsus3_T1_right": "name",
      "tarsus4_T1_right": "name",
      "claw_T1_right": "name",
      "coxa_T2_left": "name",
      "femur_T2_left": "name",
      "tibia_T2_left": "name",
      "tarsus_T2_left": "name",
      "tarsus2_T2_left": "name",
      "tarsus3_T2_left": "name",
      "tarsus4_T2_left": "name",
      "claw_T2_left": "name",
      "coxa_T2_right": "name",
      "femur_T2_right": "name",
      "tibia_T2_right": "name",
      "tarsus_T2_right": "name",
      "tarsus2_T2_right": "name",
      "tarsus3_T2_right": "name",
      "tarsus4_T2_right": "name",
      "claw_T2_right": "name",
      "coxa_T3_left": "name",
      "femur_T3_left": "name",
      "tibia_T3_left": "name",
      "tarsus_T3_left": "name",
      "tarsus2_T3_left": "name",
      "tarsus3_T3_left": "name",
      "tarsus4_T3_left": "name",
      "claw_T3_left": "name",
      "coxa_T3_right": "name",
      "femur_T3_right": "name",
      "tibia_T3_right": "name",
      "tarsus_T3_right": "name",
      "tarsus2_T3_right": "name",
      "tarsus3_T3_right": "name",
      "tarsus4_T3_right": "name",
      "claw_T3_right": "name"
    },
    "joint_methods": {
      "head_abduct": "name",
      "head_twist": "name",
      "head": "name",
      "rostrum": "name",
      "haustellum_abduct": "name",
      "haustellum": "name",
      "labrum_left": "name",
      "labrum_right": "name",
      "antenna_abduct_left": "name",
      "antenna_twist_left": "name",
      "antenna_left": "name",
      "antenna_abduct_right": "name",
      "antenna_twist_right": "name",
      "antenna_right": "name",
      "wing_yaw_left": "name",
      "wing_roll_left": "name",
      "wing_pitch_left": "name",
      "wing_yaw_right": "name",
      "wing_roll_right": "name",
      "wing_pitch_right": "name",
      "abdomen_abduct": "name",
      "abdomen": "name",
      "abdomen_abduct_2": "name",
      "abdomen_2": "name",
      "abdomen_abduct_3": "name",
      "abdomen_3": "name",
      "abdomen_abduct_4": "name",
      "abdomen_4": "name",
      "abdomen_abduct_5": "name",
      "abdomen_5": "name",
      "abdomen_abduct_6": "name",
      "abdomen_6": "name",
      "abdomen_abduct_7": "name",
      "abdomen_7": "name",
      "haltere_left": "name",
      "haltere_right": "name",
      "coxa_abduct_T1_left": "name",
      "coxa_twist_T1_left": "name",
      "coxa_T1_left": "name",
      "femur_twist_T1_left": "name",
      "femur_T1_left": "name",
      "tibia_T1_left": "name",
      "tarsus_T1_left": "name",
      "tarsus2_T1_left": "name",
      "tarsus3_T1_left": "name",
      "tarsus4_T1_left": "name",
      "tarsus5_T1_left": "name",
      "coxa_abduct_T1_right": "name",
      "coxa_twist_T1_right": "name",
      "coxa_T1_right": "name",
      "femur_twist_T1_right": "name",
      "femur_T1_right": "name",
      "tibia_T1_right": "name",
      "tarsus_T1_right": "name",
      "tarsus2_T1_right": "name",
      "tarsus3_T1_right": "name",
      "tarsus4_T1_right": "name",
      "tarsus5_T1_right": "name",
      "coxa_abduct_T2_left": "name",
      "coxa_twist_T2_left": "name",
      "coxa_T2_left": "name",
      "femur_twist_T2_left": "name",
      "femur_T2_left": "name",
      "tibia_T2_left": "name",
      "tarsus_T2_left": "name",
      "tarsus2_T2_left": "name",
      "tarsus3_T2_left": "name",
      "tarsus4_T2_left": "name",
      "tarsus5_T2_left": "name",
      "coxa_abduct_T2_right": "name",
      "coxa_twist_T2_right": "name",
      "coxa_T2_right": "name",
      "femur_twist_T2_right": "name",
      "femur_T2_right": "name",
      "tibia_T2_right": "name",
      "tarsus_T2_right": "name",
      "tarsus2_T2_right": "name",
      "tarsus3_T2_right": "name",
      "tarsus4_T2_right": "name",
      "tarsus5_T2_right": "name",
      "coxa_abduct_T3_left": "name",
      "coxa_twist_T3_left": "name",
      "coxa_T3_left": "name",
      "femur_twist_T3_left": "name",
      "femur_T3_left": "name",
      "tibia_T3_left": "name",
      "tarsus_T3_left": "name",
      "tarsus2_T3_left": "name",
      "tarsus3_T3_left": "name",
      "tarsus4_T3_left": "name",
      "tarsus5_T3_left": "name",
      "coxa_abduct_T3_right": "name",
      "coxa_twist_T3_right": "name",
      "coxa_T3_right": "name",
      "femur_twist_T3_right": "name",
      "femur_T3_right": "name",
      "tibia_T3_right": "name",
      "tarsus_T3_right": "name",
      "tarsus2_T3_right": "name",
      "tarsus3_T3_right": "name",
      "tarsus4_T3_right": "name",
      "tarsus5_T3_right": "name"
    },
    "unmatched_m_bodies": [],
    "unmatched_upstream_bodies": [],
    "unmatched_m_joints": [],
    "unmatched_upstream_joints": [],
    "registration_anchor": {
      "M": "thorax",
      "S": "thorax"
    }
  },
  "unavailable": [
    {
      "entity": "head_abduct",
      "other_entity": "head_abduct",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "head_twist",
      "other_entity": "head_twist",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "head",
      "other_entity": "head",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "rostrum",
      "other_entity": "rostrum",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "haustellum_abduct",
      "other_entity": "haustellum_abduct",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "haustellum",
      "other_entity": "haustellum",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "labrum_left",
      "other_entity": "labrum_left",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "labrum_right",
      "other_entity": "labrum_right",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "antenna_abduct_left",
      "other_entity": "antenna_abduct_left",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "antenna_twist_left",
      "other_entity": "antenna_twist_left",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "antenna_left",
      "other_entity": "antenna_left",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "antenna_abduct_right",
      "other_entity": "antenna_abduct_right",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "antenna_twist_right",
      "other_entity": "antenna_twist_right",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "antenna_right",
      "other_entity": "antenna_right",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "wing_yaw_left",
      "other_entity": "wing_yaw_left",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "wing_roll_left",
      "other_entity": "wing_roll_left",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "wing_pitch_left",
      "other_entity": "wing_pitch_left",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "wing_yaw_right",
      "other_entity": "wing_yaw_right",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "wing_roll_right",
      "other_entity": "wing_roll_right",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "wing_pitch_right",
      "other_entity": "wing_pitch_right",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "abdomen_abduct",
      "other_entity": "abdomen_abduct",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "abdomen_abduct",
      "other_entity": "abdomen_abduct",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "abdomen_abduct",
      "other_entity": "abdomen_abduct",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "abdomen",
      "other_entity": "abdomen",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "abdomen",
      "other_entity": "abdomen",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "abdomen",
      "other_entity": "abdomen",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "abdomen_abduct_2",
      "other_entity": "abdomen_abduct_2",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "abdomen_abduct_2",
      "other_entity": "abdomen_abduct_2",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "abdomen_abduct_2",
      "other_entity": "abdomen_abduct_2",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "abdomen_2",
      "other_entity": "abdomen_2",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "abdomen_2",
      "other_entity": "abdomen_2",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "abdomen_2",
      "other_entity": "abdomen_2",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "abdomen_abduct_3",
      "other_entity": "abdomen_abduct_3",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "abdomen_abduct_3",
      "other_entity": "abdomen_abduct_3",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "abdomen_abduct_3",
      "other_entity": "abdomen_abduct_3",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "abdomen_3",
      "other_entity": "abdomen_3",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "abdomen_3",
      "other_entity": "abdomen_3",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "abdomen_3",
      "other_entity": "abdomen_3",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "abdomen_abduct_4",
      "other_entity": "abdomen_abduct_4",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "abdomen_abduct_4",
      "other_entity": "abdomen_abduct_4",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "abdomen_abduct_4",
      "other_entity": "abdomen_abduct_4",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "abdomen_4",
      "other_entity": "abdomen_4",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "abdomen_4",
      "other_entity": "abdomen_4",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "abdomen_4",
      "other_entity": "abdomen_4",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "abdomen_abduct_5",
      "other_entity": "abdomen_abduct_5",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "abdomen_abduct_5",
      "other_entity": "abdomen_abduct_5",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "abdomen_abduct_5",
      "other_entity": "abdomen_abduct_5",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "abdomen_5",
      "other_entity": "abdomen_5",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "abdomen_5",
      "other_entity": "abdomen_5",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "abdomen_5",
      "other_entity": "abdomen_5",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "abdomen_abduct_6",
      "other_entity": "abdomen_abduct_6",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "abdomen_abduct_6",
      "other_entity": "abdomen_abduct_6",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "abdomen_abduct_6",
      "other_entity": "abdomen_abduct_6",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "abdomen_6",
      "other_entity": "abdomen_6",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "abdomen_6",
      "other_entity": "abdomen_6",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "abdomen_6",
      "other_entity": "abdomen_6",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "abdomen_abduct_7",
      "other_entity": "abdomen_abduct_7",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "abdomen_abduct_7",
      "other_entity": "abdomen_abduct_7",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "abdomen_abduct_7",
      "other_entity": "abdomen_abduct_7",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "abdomen_7",
      "other_entity": "abdomen_7",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "abdomen_7",
      "other_entity": "abdomen_7",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "abdomen_7",
      "other_entity": "abdomen_7",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "haltere_left",
      "other_entity": "haltere_left",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "haltere_left",
      "other_entity": "haltere_left",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "haltere_left",
      "other_entity": "haltere_left",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "haltere_right",
      "other_entity": "haltere_right",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "haltere_right",
      "other_entity": "haltere_right",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "haltere_right",
      "other_entity": "haltere_right",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "coxa_abduct_T1_left",
      "other_entity": "coxa_abduct_T1_left",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "coxa_abduct_T1_left",
      "other_entity": "coxa_abduct_T1_left",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "coxa_abduct_T1_left",
      "other_entity": "coxa_abduct_T1_left",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "coxa_twist_T1_left",
      "other_entity": "coxa_twist_T1_left",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "coxa_twist_T1_left",
      "other_entity": "coxa_twist_T1_left",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "coxa_twist_T1_left",
      "other_entity": "coxa_twist_T1_left",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "coxa_T1_left",
      "other_entity": "coxa_T1_left",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "coxa_T1_left",
      "other_entity": "coxa_T1_left",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "coxa_T1_left",
      "other_entity": "coxa_T1_left",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "femur_twist_T1_left",
      "other_entity": "femur_twist_T1_left",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "femur_twist_T1_left",
      "other_entity": "femur_twist_T1_left",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "femur_twist_T1_left",
      "other_entity": "femur_twist_T1_left",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "femur_T1_left",
      "other_entity": "femur_T1_left",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "femur_T1_left",
      "other_entity": "femur_T1_left",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "femur_T1_left",
      "other_entity": "femur_T1_left",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "tibia_T1_left",
      "other_entity": "tibia_T1_left",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "tibia_T1_left",
      "other_entity": "tibia_T1_left",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "tibia_T1_left",
      "other_entity": "tibia_T1_left",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "tarsus_T1_left",
      "other_entity": "tarsus_T1_left",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "tarsus_T1_left",
      "other_entity": "tarsus_T1_left",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "tarsus_T1_left",
      "other_entity": "tarsus_T1_left",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "tarsus2_T1_left",
      "other_entity": "tarsus2_T1_left",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "tarsus2_T1_left",
      "other_entity": "tarsus2_T1_left",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "tarsus2_T1_left",
      "other_entity": "tarsus2_T1_left",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "tarsus3_T1_left",
      "other_entity": "tarsus3_T1_left",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "tarsus3_T1_left",
      "other_entity": "tarsus3_T1_left",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "tarsus3_T1_left",
      "other_entity": "tarsus3_T1_left",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "tarsus4_T1_left",
      "other_entity": "tarsus4_T1_left",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "tarsus4_T1_left",
      "other_entity": "tarsus4_T1_left",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "tarsus4_T1_left",
      "other_entity": "tarsus4_T1_left",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "tarsus5_T1_left",
      "other_entity": "tarsus5_T1_left",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "tarsus5_T1_left",
      "other_entity": "tarsus5_T1_left",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "tarsus5_T1_left",
      "other_entity": "tarsus5_T1_left",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "coxa_abduct_T1_right",
      "other_entity": "coxa_abduct_T1_right",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "coxa_abduct_T1_right",
      "other_entity": "coxa_abduct_T1_right",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "coxa_abduct_T1_right",
      "other_entity": "coxa_abduct_T1_right",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "coxa_twist_T1_right",
      "other_entity": "coxa_twist_T1_right",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "coxa_twist_T1_right",
      "other_entity": "coxa_twist_T1_right",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "coxa_twist_T1_right",
      "other_entity": "coxa_twist_T1_right",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "coxa_T1_right",
      "other_entity": "coxa_T1_right",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "coxa_T1_right",
      "other_entity": "coxa_T1_right",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "coxa_T1_right",
      "other_entity": "coxa_T1_right",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "femur_twist_T1_right",
      "other_entity": "femur_twist_T1_right",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "femur_twist_T1_right",
      "other_entity": "femur_twist_T1_right",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "femur_twist_T1_right",
      "other_entity": "femur_twist_T1_right",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "femur_T1_right",
      "other_entity": "femur_T1_right",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "femur_T1_right",
      "other_entity": "femur_T1_right",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "femur_T1_right",
      "other_entity": "femur_T1_right",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "tibia_T1_right",
      "other_entity": "tibia_T1_right",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "tibia_T1_right",
      "other_entity": "tibia_T1_right",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "tibia_T1_right",
      "other_entity": "tibia_T1_right",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "tarsus_T1_right",
      "other_entity": "tarsus_T1_right",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "tarsus_T1_right",
      "other_entity": "tarsus_T1_right",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "tarsus_T1_right",
      "other_entity": "tarsus_T1_right",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "tarsus2_T1_right",
      "other_entity": "tarsus2_T1_right",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "tarsus2_T1_right",
      "other_entity": "tarsus2_T1_right",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "tarsus2_T1_right",
      "other_entity": "tarsus2_T1_right",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "tarsus3_T1_right",
      "other_entity": "tarsus3_T1_right",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "tarsus3_T1_right",
      "other_entity": "tarsus3_T1_right",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "tarsus3_T1_right",
      "other_entity": "tarsus3_T1_right",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "tarsus4_T1_right",
      "other_entity": "tarsus4_T1_right",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "tarsus4_T1_right",
      "other_entity": "tarsus4_T1_right",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "tarsus4_T1_right",
      "other_entity": "tarsus4_T1_right",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "tarsus5_T1_right",
      "other_entity": "tarsus5_T1_right",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "tarsus5_T1_right",
      "other_entity": "tarsus5_T1_right",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "tarsus5_T1_right",
      "other_entity": "tarsus5_T1_right",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "coxa_abduct_T2_left",
      "other_entity": "coxa_abduct_T2_left",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "coxa_abduct_T2_left",
      "other_entity": "coxa_abduct_T2_left",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "coxa_abduct_T2_left",
      "other_entity": "coxa_abduct_T2_left",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "coxa_twist_T2_left",
      "other_entity": "coxa_twist_T2_left",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "coxa_twist_T2_left",
      "other_entity": "coxa_twist_T2_left",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "coxa_twist_T2_left",
      "other_entity": "coxa_twist_T2_left",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "coxa_T2_left",
      "other_entity": "coxa_T2_left",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "coxa_T2_left",
      "other_entity": "coxa_T2_left",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "coxa_T2_left",
      "other_entity": "coxa_T2_left",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "femur_twist_T2_left",
      "other_entity": "femur_twist_T2_left",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "femur_twist_T2_left",
      "other_entity": "femur_twist_T2_left",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "femur_twist_T2_left",
      "other_entity": "femur_twist_T2_left",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "femur_T2_left",
      "other_entity": "femur_T2_left",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "femur_T2_left",
      "other_entity": "femur_T2_left",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "femur_T2_left",
      "other_entity": "femur_T2_left",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "tibia_T2_left",
      "other_entity": "tibia_T2_left",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "tibia_T2_left",
      "other_entity": "tibia_T2_left",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "tibia_T2_left",
      "other_entity": "tibia_T2_left",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "tarsus_T2_left",
      "other_entity": "tarsus_T2_left",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "tarsus_T2_left",
      "other_entity": "tarsus_T2_left",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "tarsus_T2_left",
      "other_entity": "tarsus_T2_left",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "tarsus2_T2_left",
      "other_entity": "tarsus2_T2_left",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "tarsus2_T2_left",
      "other_entity": "tarsus2_T2_left",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "tarsus2_T2_left",
      "other_entity": "tarsus2_T2_left",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "tarsus3_T2_left",
      "other_entity": "tarsus3_T2_left",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "tarsus3_T2_left",
      "other_entity": "tarsus3_T2_left",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "tarsus3_T2_left",
      "other_entity": "tarsus3_T2_left",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "tarsus4_T2_left",
      "other_entity": "tarsus4_T2_left",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "tarsus4_T2_left",
      "other_entity": "tarsus4_T2_left",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "tarsus4_T2_left",
      "other_entity": "tarsus4_T2_left",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "tarsus5_T2_left",
      "other_entity": "tarsus5_T2_left",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "tarsus5_T2_left",
      "other_entity": "tarsus5_T2_left",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "tarsus5_T2_left",
      "other_entity": "tarsus5_T2_left",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "coxa_abduct_T2_right",
      "other_entity": "coxa_abduct_T2_right",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "coxa_abduct_T2_right",
      "other_entity": "coxa_abduct_T2_right",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "coxa_abduct_T2_right",
      "other_entity": "coxa_abduct_T2_right",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "coxa_twist_T2_right",
      "other_entity": "coxa_twist_T2_right",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "coxa_twist_T2_right",
      "other_entity": "coxa_twist_T2_right",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "coxa_twist_T2_right",
      "other_entity": "coxa_twist_T2_right",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "coxa_T2_right",
      "other_entity": "coxa_T2_right",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "coxa_T2_right",
      "other_entity": "coxa_T2_right",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "coxa_T2_right",
      "other_entity": "coxa_T2_right",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "femur_twist_T2_right",
      "other_entity": "femur_twist_T2_right",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "femur_twist_T2_right",
      "other_entity": "femur_twist_T2_right",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "femur_twist_T2_right",
      "other_entity": "femur_twist_T2_right",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "femur_T2_right",
      "other_entity": "femur_T2_right",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "femur_T2_right",
      "other_entity": "femur_T2_right",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "femur_T2_right",
      "other_entity": "femur_T2_right",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "tibia_T2_right",
      "other_entity": "tibia_T2_right",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "tibia_T2_right",
      "other_entity": "tibia_T2_right",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "tibia_T2_right",
      "other_entity": "tibia_T2_right",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "tarsus_T2_right",
      "other_entity": "tarsus_T2_right",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "tarsus_T2_right",
      "other_entity": "tarsus_T2_right",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "tarsus_T2_right",
      "other_entity": "tarsus_T2_right",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "tarsus2_T2_right",
      "other_entity": "tarsus2_T2_right",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "tarsus2_T2_right",
      "other_entity": "tarsus2_T2_right",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "tarsus2_T2_right",
      "other_entity": "tarsus2_T2_right",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "tarsus3_T2_right",
      "other_entity": "tarsus3_T2_right",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "tarsus3_T2_right",
      "other_entity": "tarsus3_T2_right",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "tarsus3_T2_right",
      "other_entity": "tarsus3_T2_right",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "tarsus4_T2_right",
      "other_entity": "tarsus4_T2_right",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "tarsus4_T2_right",
      "other_entity": "tarsus4_T2_right",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "tarsus4_T2_right",
      "other_entity": "tarsus4_T2_right",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "tarsus5_T2_right",
      "other_entity": "tarsus5_T2_right",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "tarsus5_T2_right",
      "other_entity": "tarsus5_T2_right",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "tarsus5_T2_right",
      "other_entity": "tarsus5_T2_right",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "coxa_abduct_T3_left",
      "other_entity": "coxa_abduct_T3_left",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "coxa_abduct_T3_left",
      "other_entity": "coxa_abduct_T3_left",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "coxa_abduct_T3_left",
      "other_entity": "coxa_abduct_T3_left",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "coxa_twist_T3_left",
      "other_entity": "coxa_twist_T3_left",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "coxa_twist_T3_left",
      "other_entity": "coxa_twist_T3_left",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "coxa_twist_T3_left",
      "other_entity": "coxa_twist_T3_left",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "coxa_T3_left",
      "other_entity": "coxa_T3_left",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "coxa_T3_left",
      "other_entity": "coxa_T3_left",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "coxa_T3_left",
      "other_entity": "coxa_T3_left",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "femur_twist_T3_left",
      "other_entity": "femur_twist_T3_left",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "femur_twist_T3_left",
      "other_entity": "femur_twist_T3_left",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "femur_twist_T3_left",
      "other_entity": "femur_twist_T3_left",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "femur_T3_left",
      "other_entity": "femur_T3_left",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "femur_T3_left",
      "other_entity": "femur_T3_left",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "femur_T3_left",
      "other_entity": "femur_T3_left",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "tibia_T3_left",
      "other_entity": "tibia_T3_left",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "tibia_T3_left",
      "other_entity": "tibia_T3_left",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "tibia_T3_left",
      "other_entity": "tibia_T3_left",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "tarsus_T3_left",
      "other_entity": "tarsus_T3_left",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "tarsus_T3_left",
      "other_entity": "tarsus_T3_left",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "tarsus_T3_left",
      "other_entity": "tarsus_T3_left",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "tarsus2_T3_left",
      "other_entity": "tarsus2_T3_left",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "tarsus2_T3_left",
      "other_entity": "tarsus2_T3_left",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "tarsus2_T3_left",
      "other_entity": "tarsus2_T3_left",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "tarsus3_T3_left",
      "other_entity": "tarsus3_T3_left",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "tarsus3_T3_left",
      "other_entity": "tarsus3_T3_left",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "tarsus3_T3_left",
      "other_entity": "tarsus3_T3_left",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "tarsus4_T3_left",
      "other_entity": "tarsus4_T3_left",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "tarsus4_T3_left",
      "other_entity": "tarsus4_T3_left",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "tarsus4_T3_left",
      "other_entity": "tarsus4_T3_left",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "tarsus5_T3_left",
      "other_entity": "tarsus5_T3_left",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "tarsus5_T3_left",
      "other_entity": "tarsus5_T3_left",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "tarsus5_T3_left",
      "other_entity": "tarsus5_T3_left",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "coxa_abduct_T3_right",
      "other_entity": "coxa_abduct_T3_right",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "coxa_abduct_T3_right",
      "other_entity": "coxa_abduct_T3_right",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "coxa_abduct_T3_right",
      "other_entity": "coxa_abduct_T3_right",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "coxa_twist_T3_right",
      "other_entity": "coxa_twist_T3_right",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "coxa_twist_T3_right",
      "other_entity": "coxa_twist_T3_right",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "coxa_twist_T3_right",
      "other_entity": "coxa_twist_T3_right",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "coxa_T3_right",
      "other_entity": "coxa_T3_right",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "coxa_T3_right",
      "other_entity": "coxa_T3_right",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "coxa_T3_right",
      "other_entity": "coxa_T3_right",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "femur_twist_T3_right",
      "other_entity": "femur_twist_T3_right",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "femur_twist_T3_right",
      "other_entity": "femur_twist_T3_right",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "femur_twist_T3_right",
      "other_entity": "femur_twist_T3_right",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "femur_T3_right",
      "other_entity": "femur_T3_right",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "femur_T3_right",
      "other_entity": "femur_T3_right",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "femur_T3_right",
      "other_entity": "femur_T3_right",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "tibia_T3_right",
      "other_entity": "tibia_T3_right",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "tibia_T3_right",
      "other_entity": "tibia_T3_right",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "tibia_T3_right",
      "other_entity": "tibia_T3_right",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "tarsus_T3_right",
      "other_entity": "tarsus_T3_right",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "tarsus_T3_right",
      "other_entity": "tarsus_T3_right",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "tarsus_T3_right",
      "other_entity": "tarsus_T3_right",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "tarsus2_T3_right",
      "other_entity": "tarsus2_T3_right",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "tarsus2_T3_right",
      "other_entity": "tarsus2_T3_right",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "tarsus2_T3_right",
      "other_entity": "tarsus2_T3_right",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "tarsus3_T3_right",
      "other_entity": "tarsus3_T3_right",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "tarsus3_T3_right",
      "other_entity": "tarsus3_T3_right",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "tarsus3_T3_right",
      "other_entity": "tarsus3_T3_right",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "tarsus4_T3_right",
      "other_entity": "tarsus4_T3_right",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "tarsus4_T3_right",
      "other_entity": "tarsus4_T3_right",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "tarsus4_T3_right",
      "other_entity": "tarsus4_T3_right",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "tarsus5_T3_right",
      "other_entity": "tarsus5_T3_right",
      "quantity": "effort",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "tarsus5_T3_right",
      "other_entity": "tarsus5_T3_right",
      "quantity": "force",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "tarsus5_T3_right",
      "other_entity": "tarsus5_T3_right",
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
| head_abduct / velocity | unavailable | unavailable | unavailable |
| head_twist / velocity | unavailable | unavailable | unavailable |
| head / velocity | unavailable | unavailable | unavailable |
| rostrum / velocity | unavailable | unavailable | unavailable |
| haustellum_abduct / velocity | unavailable | unavailable | unavailable |
| haustellum / velocity | unavailable | unavailable | unavailable |
| labrum_left / velocity | unavailable | unavailable | unavailable |
| labrum_right / velocity | unavailable | unavailable | unavailable |
| antenna_abduct_left / velocity | unavailable | unavailable | unavailable |
| antenna_twist_left / velocity | unavailable | unavailable | unavailable |
| antenna_left / velocity | unavailable | unavailable | unavailable |
| antenna_abduct_right / velocity | unavailable | unavailable | unavailable |
| antenna_twist_right / velocity | unavailable | unavailable | unavailable |
| antenna_right / velocity | unavailable | unavailable | unavailable |
| wing_yaw_left / velocity | unavailable | unavailable | unavailable |
| wing_roll_left / velocity | unavailable | unavailable | unavailable |
| wing_pitch_left / velocity | unavailable | unavailable | unavailable |
| wing_yaw_right / velocity | unavailable | unavailable | unavailable |
| wing_roll_right / velocity | unavailable | unavailable | unavailable |
| wing_pitch_right / velocity | unavailable | unavailable | unavailable |
| abdomen_abduct / effort | unavailable | unavailable | unavailable |
| abdomen_abduct / force | unavailable | unavailable | unavailable |
| abdomen_abduct / velocity | unavailable | unavailable | unavailable |
| abdomen / effort | unavailable | unavailable | unavailable |
| abdomen / force | unavailable | unavailable | unavailable |
| abdomen / velocity | unavailable | unavailable | unavailable |
| abdomen_abduct_2 / effort | unavailable | unavailable | unavailable |
| abdomen_abduct_2 / force | unavailable | unavailable | unavailable |
| abdomen_abduct_2 / velocity | unavailable | unavailable | unavailable |
| abdomen_2 / effort | unavailable | unavailable | unavailable |
| abdomen_2 / force | unavailable | unavailable | unavailable |
| abdomen_2 / velocity | unavailable | unavailable | unavailable |
| abdomen_abduct_3 / effort | unavailable | unavailable | unavailable |
| abdomen_abduct_3 / force | unavailable | unavailable | unavailable |
| abdomen_abduct_3 / velocity | unavailable | unavailable | unavailable |
| abdomen_3 / effort | unavailable | unavailable | unavailable |
| abdomen_3 / force | unavailable | unavailable | unavailable |
| abdomen_3 / velocity | unavailable | unavailable | unavailable |
| abdomen_abduct_4 / effort | unavailable | unavailable | unavailable |
| abdomen_abduct_4 / force | unavailable | unavailable | unavailable |
| abdomen_abduct_4 / velocity | unavailable | unavailable | unavailable |
| abdomen_4 / effort | unavailable | unavailable | unavailable |
| abdomen_4 / force | unavailable | unavailable | unavailable |
| abdomen_4 / velocity | unavailable | unavailable | unavailable |
| abdomen_abduct_5 / effort | unavailable | unavailable | unavailable |
| abdomen_abduct_5 / force | unavailable | unavailable | unavailable |
| abdomen_abduct_5 / velocity | unavailable | unavailable | unavailable |
| abdomen_5 / effort | unavailable | unavailable | unavailable |
| abdomen_5 / force | unavailable | unavailable | unavailable |
| abdomen_5 / velocity | unavailable | unavailable | unavailable |
| abdomen_abduct_6 / effort | unavailable | unavailable | unavailable |
| abdomen_abduct_6 / force | unavailable | unavailable | unavailable |
| abdomen_abduct_6 / velocity | unavailable | unavailable | unavailable |
| abdomen_6 / effort | unavailable | unavailable | unavailable |
| abdomen_6 / force | unavailable | unavailable | unavailable |
| abdomen_6 / velocity | unavailable | unavailable | unavailable |
| abdomen_abduct_7 / effort | unavailable | unavailable | unavailable |
| abdomen_abduct_7 / force | unavailable | unavailable | unavailable |
| abdomen_abduct_7 / velocity | unavailable | unavailable | unavailable |
| abdomen_7 / effort | unavailable | unavailable | unavailable |
| abdomen_7 / force | unavailable | unavailable | unavailable |
| abdomen_7 / velocity | unavailable | unavailable | unavailable |
| haltere_left / effort | unavailable | unavailable | unavailable |
| haltere_left / force | unavailable | unavailable | unavailable |
| haltere_left / velocity | unavailable | unavailable | unavailable |
| haltere_right / effort | unavailable | unavailable | unavailable |
| haltere_right / force | unavailable | unavailable | unavailable |
| haltere_right / velocity | unavailable | unavailable | unavailable |
| coxa_abduct_T1_left / effort | unavailable | unavailable | unavailable |
| coxa_abduct_T1_left / force | unavailable | unavailable | unavailable |
| coxa_abduct_T1_left / velocity | unavailable | unavailable | unavailable |
| coxa_twist_T1_left / effort | unavailable | unavailable | unavailable |
| coxa_twist_T1_left / force | unavailable | unavailable | unavailable |
| coxa_twist_T1_left / velocity | unavailable | unavailable | unavailable |
| coxa_T1_left / effort | unavailable | unavailable | unavailable |
| coxa_T1_left / force | unavailable | unavailable | unavailable |
| coxa_T1_left / velocity | unavailable | unavailable | unavailable |
| femur_twist_T1_left / effort | unavailable | unavailable | unavailable |
| femur_twist_T1_left / force | unavailable | unavailable | unavailable |
| femur_twist_T1_left / velocity | unavailable | unavailable | unavailable |
| femur_T1_left / effort | unavailable | unavailable | unavailable |
| femur_T1_left / force | unavailable | unavailable | unavailable |
| femur_T1_left / velocity | unavailable | unavailable | unavailable |
| tibia_T1_left / effort | unavailable | unavailable | unavailable |
| tibia_T1_left / force | unavailable | unavailable | unavailable |
| tibia_T1_left / velocity | unavailable | unavailable | unavailable |
| tarsus_T1_left / effort | unavailable | unavailable | unavailable |
| tarsus_T1_left / force | unavailable | unavailable | unavailable |
| tarsus_T1_left / velocity | unavailable | unavailable | unavailable |
| tarsus2_T1_left / effort | unavailable | unavailable | unavailable |
| tarsus2_T1_left / force | unavailable | unavailable | unavailable |
| tarsus2_T1_left / velocity | unavailable | unavailable | unavailable |
| tarsus3_T1_left / effort | unavailable | unavailable | unavailable |
| tarsus3_T1_left / force | unavailable | unavailable | unavailable |
| tarsus3_T1_left / velocity | unavailable | unavailable | unavailable |
| tarsus4_T1_left / effort | unavailable | unavailable | unavailable |
| tarsus4_T1_left / force | unavailable | unavailable | unavailable |
| tarsus4_T1_left / velocity | unavailable | unavailable | unavailable |
| tarsus5_T1_left / effort | unavailable | unavailable | unavailable |
| tarsus5_T1_left / force | unavailable | unavailable | unavailable |
| tarsus5_T1_left / velocity | unavailable | unavailable | unavailable |
| coxa_abduct_T1_right / effort | unavailable | unavailable | unavailable |
| coxa_abduct_T1_right / force | unavailable | unavailable | unavailable |
| coxa_abduct_T1_right / velocity | unavailable | unavailable | unavailable |
| coxa_twist_T1_right / effort | unavailable | unavailable | unavailable |
| coxa_twist_T1_right / force | unavailable | unavailable | unavailable |
| coxa_twist_T1_right / velocity | unavailable | unavailable | unavailable |
| coxa_T1_right / effort | unavailable | unavailable | unavailable |
| coxa_T1_right / force | unavailable | unavailable | unavailable |
| coxa_T1_right / velocity | unavailable | unavailable | unavailable |
| femur_twist_T1_right / effort | unavailable | unavailable | unavailable |
| femur_twist_T1_right / force | unavailable | unavailable | unavailable |
| femur_twist_T1_right / velocity | unavailable | unavailable | unavailable |
| femur_T1_right / effort | unavailable | unavailable | unavailable |
| femur_T1_right / force | unavailable | unavailable | unavailable |
| femur_T1_right / velocity | unavailable | unavailable | unavailable |
| tibia_T1_right / effort | unavailable | unavailable | unavailable |
| tibia_T1_right / force | unavailable | unavailable | unavailable |
| tibia_T1_right / velocity | unavailable | unavailable | unavailable |
| tarsus_T1_right / effort | unavailable | unavailable | unavailable |
| tarsus_T1_right / force | unavailable | unavailable | unavailable |
| tarsus_T1_right / velocity | unavailable | unavailable | unavailable |
| tarsus2_T1_right / effort | unavailable | unavailable | unavailable |
| tarsus2_T1_right / force | unavailable | unavailable | unavailable |
| tarsus2_T1_right / velocity | unavailable | unavailable | unavailable |
| tarsus3_T1_right / effort | unavailable | unavailable | unavailable |
| tarsus3_T1_right / force | unavailable | unavailable | unavailable |
| tarsus3_T1_right / velocity | unavailable | unavailable | unavailable |
| tarsus4_T1_right / effort | unavailable | unavailable | unavailable |
| tarsus4_T1_right / force | unavailable | unavailable | unavailable |
| tarsus4_T1_right / velocity | unavailable | unavailable | unavailable |
| tarsus5_T1_right / effort | unavailable | unavailable | unavailable |
| tarsus5_T1_right / force | unavailable | unavailable | unavailable |
| tarsus5_T1_right / velocity | unavailable | unavailable | unavailable |
| coxa_abduct_T2_left / effort | unavailable | unavailable | unavailable |
| coxa_abduct_T2_left / force | unavailable | unavailable | unavailable |
| coxa_abduct_T2_left / velocity | unavailable | unavailable | unavailable |
| coxa_twist_T2_left / effort | unavailable | unavailable | unavailable |
| coxa_twist_T2_left / force | unavailable | unavailable | unavailable |
| coxa_twist_T2_left / velocity | unavailable | unavailable | unavailable |
| coxa_T2_left / effort | unavailable | unavailable | unavailable |
| coxa_T2_left / force | unavailable | unavailable | unavailable |
| coxa_T2_left / velocity | unavailable | unavailable | unavailable |
| femur_twist_T2_left / effort | unavailable | unavailable | unavailable |
| femur_twist_T2_left / force | unavailable | unavailable | unavailable |
| femur_twist_T2_left / velocity | unavailable | unavailable | unavailable |
| femur_T2_left / effort | unavailable | unavailable | unavailable |
| femur_T2_left / force | unavailable | unavailable | unavailable |
| femur_T2_left / velocity | unavailable | unavailable | unavailable |
| tibia_T2_left / effort | unavailable | unavailable | unavailable |
| tibia_T2_left / force | unavailable | unavailable | unavailable |
| tibia_T2_left / velocity | unavailable | unavailable | unavailable |
| tarsus_T2_left / effort | unavailable | unavailable | unavailable |
| tarsus_T2_left / force | unavailable | unavailable | unavailable |
| tarsus_T2_left / velocity | unavailable | unavailable | unavailable |
| tarsus2_T2_left / effort | unavailable | unavailable | unavailable |
| tarsus2_T2_left / force | unavailable | unavailable | unavailable |
| tarsus2_T2_left / velocity | unavailable | unavailable | unavailable |
| tarsus3_T2_left / effort | unavailable | unavailable | unavailable |
| tarsus3_T2_left / force | unavailable | unavailable | unavailable |
| tarsus3_T2_left / velocity | unavailable | unavailable | unavailable |
| tarsus4_T2_left / effort | unavailable | unavailable | unavailable |
| tarsus4_T2_left / force | unavailable | unavailable | unavailable |
| tarsus4_T2_left / velocity | unavailable | unavailable | unavailable |
| tarsus5_T2_left / effort | unavailable | unavailable | unavailable |
| tarsus5_T2_left / force | unavailable | unavailable | unavailable |
| tarsus5_T2_left / velocity | unavailable | unavailable | unavailable |
| coxa_abduct_T2_right / effort | unavailable | unavailable | unavailable |
| coxa_abduct_T2_right / force | unavailable | unavailable | unavailable |
| coxa_abduct_T2_right / velocity | unavailable | unavailable | unavailable |
| coxa_twist_T2_right / effort | unavailable | unavailable | unavailable |
| coxa_twist_T2_right / force | unavailable | unavailable | unavailable |
| coxa_twist_T2_right / velocity | unavailable | unavailable | unavailable |
| coxa_T2_right / effort | unavailable | unavailable | unavailable |
| coxa_T2_right / force | unavailable | unavailable | unavailable |
| coxa_T2_right / velocity | unavailable | unavailable | unavailable |
| femur_twist_T2_right / effort | unavailable | unavailable | unavailable |
| femur_twist_T2_right / force | unavailable | unavailable | unavailable |
| femur_twist_T2_right / velocity | unavailable | unavailable | unavailable |
| femur_T2_right / effort | unavailable | unavailable | unavailable |
| femur_T2_right / force | unavailable | unavailable | unavailable |
| femur_T2_right / velocity | unavailable | unavailable | unavailable |
| tibia_T2_right / effort | unavailable | unavailable | unavailable |
| tibia_T2_right / force | unavailable | unavailable | unavailable |
| tibia_T2_right / velocity | unavailable | unavailable | unavailable |
| tarsus_T2_right / effort | unavailable | unavailable | unavailable |
| tarsus_T2_right / force | unavailable | unavailable | unavailable |
| tarsus_T2_right / velocity | unavailable | unavailable | unavailable |
| tarsus2_T2_right / effort | unavailable | unavailable | unavailable |
| tarsus2_T2_right / force | unavailable | unavailable | unavailable |
| tarsus2_T2_right / velocity | unavailable | unavailable | unavailable |
| tarsus3_T2_right / effort | unavailable | unavailable | unavailable |
| tarsus3_T2_right / force | unavailable | unavailable | unavailable |
| tarsus3_T2_right / velocity | unavailable | unavailable | unavailable |
| tarsus4_T2_right / effort | unavailable | unavailable | unavailable |
| tarsus4_T2_right / force | unavailable | unavailable | unavailable |
| tarsus4_T2_right / velocity | unavailable | unavailable | unavailable |
| tarsus5_T2_right / effort | unavailable | unavailable | unavailable |
| tarsus5_T2_right / force | unavailable | unavailable | unavailable |
| tarsus5_T2_right / velocity | unavailable | unavailable | unavailable |
| coxa_abduct_T3_left / effort | unavailable | unavailable | unavailable |
| coxa_abduct_T3_left / force | unavailable | unavailable | unavailable |
| coxa_abduct_T3_left / velocity | unavailable | unavailable | unavailable |
| coxa_twist_T3_left / effort | unavailable | unavailable | unavailable |
| coxa_twist_T3_left / force | unavailable | unavailable | unavailable |
| coxa_twist_T3_left / velocity | unavailable | unavailable | unavailable |
| coxa_T3_left / effort | unavailable | unavailable | unavailable |
| coxa_T3_left / force | unavailable | unavailable | unavailable |
| coxa_T3_left / velocity | unavailable | unavailable | unavailable |
| femur_twist_T3_left / effort | unavailable | unavailable | unavailable |
| femur_twist_T3_left / force | unavailable | unavailable | unavailable |
| femur_twist_T3_left / velocity | unavailable | unavailable | unavailable |
| femur_T3_left / effort | unavailable | unavailable | unavailable |
| femur_T3_left / force | unavailable | unavailable | unavailable |
| femur_T3_left / velocity | unavailable | unavailable | unavailable |
| tibia_T3_left / effort | unavailable | unavailable | unavailable |
| tibia_T3_left / force | unavailable | unavailable | unavailable |
| tibia_T3_left / velocity | unavailable | unavailable | unavailable |
| tarsus_T3_left / effort | unavailable | unavailable | unavailable |
| tarsus_T3_left / force | unavailable | unavailable | unavailable |
| tarsus_T3_left / velocity | unavailable | unavailable | unavailable |
| tarsus2_T3_left / effort | unavailable | unavailable | unavailable |
| tarsus2_T3_left / force | unavailable | unavailable | unavailable |
| tarsus2_T3_left / velocity | unavailable | unavailable | unavailable |
| tarsus3_T3_left / effort | unavailable | unavailable | unavailable |
| tarsus3_T3_left / force | unavailable | unavailable | unavailable |
| tarsus3_T3_left / velocity | unavailable | unavailable | unavailable |
| tarsus4_T3_left / effort | unavailable | unavailable | unavailable |
| tarsus4_T3_left / force | unavailable | unavailable | unavailable |
| tarsus4_T3_left / velocity | unavailable | unavailable | unavailable |
| tarsus5_T3_left / effort | unavailable | unavailable | unavailable |
| tarsus5_T3_left / force | unavailable | unavailable | unavailable |
| tarsus5_T3_left / velocity | unavailable | unavailable | unavailable |
| coxa_abduct_T3_right / effort | unavailable | unavailable | unavailable |
| coxa_abduct_T3_right / force | unavailable | unavailable | unavailable |
| coxa_abduct_T3_right / velocity | unavailable | unavailable | unavailable |
| coxa_twist_T3_right / effort | unavailable | unavailable | unavailable |
| coxa_twist_T3_right / force | unavailable | unavailable | unavailable |
| coxa_twist_T3_right / velocity | unavailable | unavailable | unavailable |
| coxa_T3_right / effort | unavailable | unavailable | unavailable |
| coxa_T3_right / force | unavailable | unavailable | unavailable |
| coxa_T3_right / velocity | unavailable | unavailable | unavailable |
| femur_twist_T3_right / effort | unavailable | unavailable | unavailable |
| femur_twist_T3_right / force | unavailable | unavailable | unavailable |
| femur_twist_T3_right / velocity | unavailable | unavailable | unavailable |
| femur_T3_right / effort | unavailable | unavailable | unavailable |
| femur_T3_right / force | unavailable | unavailable | unavailable |
| femur_T3_right / velocity | unavailable | unavailable | unavailable |
| tibia_T3_right / effort | unavailable | unavailable | unavailable |
| tibia_T3_right / force | unavailable | unavailable | unavailable |
| tibia_T3_right / velocity | unavailable | unavailable | unavailable |
| tarsus_T3_right / effort | unavailable | unavailable | unavailable |
| tarsus_T3_right / force | unavailable | unavailable | unavailable |
| tarsus_T3_right / velocity | unavailable | unavailable | unavailable |
| tarsus2_T3_right / effort | unavailable | unavailable | unavailable |
| tarsus2_T3_right / force | unavailable | unavailable | unavailable |
| tarsus2_T3_right / velocity | unavailable | unavailable | unavailable |
| tarsus3_T3_right / effort | unavailable | unavailable | unavailable |
| tarsus3_T3_right / force | unavailable | unavailable | unavailable |
| tarsus3_T3_right / velocity | unavailable | unavailable | unavailable |
| tarsus4_T3_right / effort | unavailable | unavailable | unavailable |
| tarsus4_T3_right / force | unavailable | unavailable | unavailable |
| tarsus4_T3_right / velocity | unavailable | unavailable | unavailable |
| tarsus5_T3_right / effort | unavailable | unavailable | unavailable |
| tarsus5_T3_right / force | unavailable | unavailable | unavailable |
| tarsus5_T3_right / velocity | unavailable | unavailable | unavailable |
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
  "https://github.com/TuragaLab/flybody flybody/fruitfly/build_fruitfly/fruitfly.xml at d015e9bfe441bd90ae431bac24c55cb74bdbce26: ValueError: Resource missing at d015e9bfe441bd90ae431bac24c55cb74bdbce26: flybody/fruitfly/build_fruitfly/head_body.obj",
  "https://github.com/TuragaLab/flybody flybody/fruitfly/build_fruitfly/floor.xml at d015e9bfe441bd90ae431bac24c55cb74bdbce26: ValueError: Resource missing at d015e9bfe441bd90ae431bac24c55cb74bdbce26: flybody/fruitfly/build_fruitfly/head_body.obj",
  "https://github.com/TuragaLab/flybody flybody/fruitfly/build_fruitfly/assets/drosophila.xml at d015e9bfe441bd90ae431bac24c55cb74bdbce26: ValueError: Resource missing at d015e9bfe441bd90ae431bac24c55cb74bdbce26: flybody/fruitfly/build_fruitfly/assets/assets/head_body.msh",
  "https://github.com/TuragaLab/flybody flybody/fruitfly/build_fruitfly/assets/drosophila_defaults.xml at d015e9bfe441bd90ae431bac24c55cb74bdbce26: ValueError: XML has no robot bodies; it is an include/extension fragment, not a standalone source"
]
```

## History inputs

```json
[
  "flybody/fruitfly/assets/abdomen_1_body.msh",
  "flybody/fruitfly/assets/abdomen_1_body.obj",
  "flybody/fruitfly/assets/abdomen_1_lower.msh",
  "flybody/fruitfly/assets/abdomen_1_lower.obj",
  "flybody/fruitfly/assets/abdomen_2_body.msh",
  "flybody/fruitfly/assets/abdomen_2_body.obj",
  "flybody/fruitfly/assets/abdomen_2_lower.msh",
  "flybody/fruitfly/assets/abdomen_2_lower.obj",
  "flybody/fruitfly/assets/abdomen_3_body.msh",
  "flybody/fruitfly/assets/abdomen_3_body.obj",
  "flybody/fruitfly/assets/abdomen_3_lower.msh",
  "flybody/fruitfly/assets/abdomen_3_lower.obj",
  "flybody/fruitfly/assets/abdomen_4_body.msh",
  "flybody/fruitfly/assets/abdomen_4_body.obj",
  "flybody/fruitfly/assets/abdomen_4_lower.msh",
  "flybody/fruitfly/assets/abdomen_4_lower.obj",
  "flybody/fruitfly/assets/abdomen_5_body.msh",
  "flybody/fruitfly/assets/abdomen_5_body.obj",
  "flybody/fruitfly/assets/abdomen_5_lower.msh",
  "flybody/fruitfly/assets/abdomen_5_lower.obj",
  "flybody/fruitfly/assets/abdomen_6_body.msh",
  "flybody/fruitfly/assets/abdomen_6_body.obj",
  "flybody/fruitfly/assets/abdomen_6_lower.msh",
  "flybody/fruitfly/assets/abdomen_6_lower.obj",
  "flybody/fruitfly/assets/abdomen_7_body.msh",
  "flybody/fruitfly/assets/abdomen_7_body.obj",
  "flybody/fruitfly/assets/abdomen_7_lower.msh",
  "flybody/fruitfly/assets/abdomen_7_lower.obj",
  "flybody/fruitfly/assets/abdomen_8_body.msh",
  "flybody/fruitfly/assets/abdomen_8_body.obj",
  "flybody/fruitfly/assets/antenna_left_black.msh",
  "flybody/fruitfly/assets/antenna_left_black.obj",
  "flybody/fruitfly/assets/antenna_left_body.msh",
  "flybody/fruitfly/assets/antenna_left_body.obj",
  "flybody/fruitfly/assets/antenna_right_black.msh",
  "flybody/fruitfly/assets/antenna_right_black.obj",
  "flybody/fruitfly/assets/antenna_right_body.msh",
  "flybody/fruitfly/assets/antenna_right_body.obj",
  "flybody/fruitfly/assets/coxa_T1_left_body.msh",
  "flybody/fruitfly/assets/coxa_T1_left_body.obj",
  "flybody/fruitfly/assets/coxa_T1_right_body.msh",
  "flybody/fruitfly/assets/coxa_T1_right_body.obj",
  "flybody/fruitfly/assets/coxa_T2_left_body.msh",
  "flybody/fruitfly/assets/coxa_T2_left_body.obj",
  "flybody/fruitfly/assets/coxa_T2_right_body.msh",
  "flybody/fruitfly/assets/coxa_T2_right_body.obj",
  "flybody/fruitfly/assets/coxa_T3_left_body.msh",
  "flybody/fruitfly/assets/coxa_T3_left_body.obj",
  "flybody/fruitfly/assets/coxa_T3_right_body.msh",
  "flybody/fruitfly/assets/coxa_T3_right_body.obj",
  "flybody/fruitfly/assets/femur_T1_left_body.msh",
  "flybody/fruitfly/assets/femur_T1_left_body.obj",
  "flybody/fruitfly/assets/femur_T1_right_body.msh",
  "flybody/fruitfly/assets/femur_T1_right_body.obj",
  "flybody/fruitfly/assets/femur_T2_left_body.msh",
  "flybody/fruitfly/assets/femur_T2_left_body.obj",
  "flybody/fruitfly/assets/femur_T2_right_body.msh",
  "flybody/fruitfly/assets/femur_T2_right_body.obj",
  "flybody/fruitfly/assets/femur_T3_left_body.msh",
  "flybody/fruitfly/assets/femur_T3_left_body.obj",
  "flybody/fruitfly/assets/femur_T3_right_body.msh",
  "flybody/fruitfly/assets/femur_T3_right_body.obj",
  "flybody/fruitfly/assets/fruitfly.xml",
  "flybody/fruitfly/assets/haltere_left_body.msh",
  "flybody/fruitfly/assets/haltere_left_body.obj",
  "flybody/fruitfly/assets/haltere_right_body.msh",
  "flybody/fruitfly/assets/haltere_right_body.obj",
  "flybody/fruitfly/assets/haustellum_black.msh",
  "flybody/fruitfly/assets/haustellum_black.obj",
  "flybody/fruitfly/assets/haustellum_body.msh",
  "flybody/fruitfly/assets/haustellum_body.obj",
  "flybody/fruitfly/assets/head_black.msh",
  "flybody/fruitfly/assets/head_black.obj",
  "flybody/fruitfly/assets/head_body.msh",
  "flybody/fruitfly/assets/head_body.obj",
  "flybody/fruitfly/assets/head_ocelli.msh",
  "flybody/fruitfly/assets/head_ocelli.obj",
  "flybody/fruitfly/assets/head_red.msh",
  "flybody/fruitfly/assets/head_red.obj",
  "flybody/fruitfly/assets/labrum_left_lower.msh",
  "flybody/fruitfly/assets/labrum_left_lower.obj",
  "flybody/fruitfly/assets/labrum_right_lower.msh",
  "flybody/fruitfly/assets/labrum_right_lower.obj",
  "flybody/fruitfly/assets/rostrum_body.msh",
  "flybody/fruitfly/assets/rostrum_body.obj",
  "flybody/fruitfly/assets/rostrum_bristle-brown.msh",
  "flybody/fruitfly/assets/rostrum_bristle-brown.obj",
  "flybody/fruitfly/assets/tarsal_claw_T1_left_brown.msh",
  "flybody/fruitfly/assets/tarsal_claw_T1_left_brown.obj",
  "flybody/fruitfly/assets/tarsal_claw_T1_right_brown.msh",
  "flybody/fruitfly/assets/tarsal_claw_T1_right_brown.obj",
  "flybody/fruitfly/assets/tarsal_claw_T2_left_brown.msh",
  "flybody/fruitfly/assets/tarsal_claw_T2_left_brown.obj",
  "flybody/fruitfly/assets/tarsal_claw_T2_right_brown.msh",
  "flybody/fruitfly/assets/tarsal_claw_T2_right_brown.obj",
  "flybody/fruitfly/assets/tarsal_claw_T3_left_brown.msh",
  "flybody/fruitfly/assets/tarsal_claw_T3_left_brown.obj",
  "flybody/fruitfly/assets/tarsal_claw_T3_right_brown.msh",
  "flybody/fruitfly/assets/tarsal_claw_T3_right_brown.obj",
  "flybody/fruitfly/assets/tarsus_T1_1_left_body.msh",
  "flybody/fruitfly/assets/tarsus_T1_1_left_body.obj",
  "flybody/fruitfly/assets/tarsus_T1_1_right_body.msh",
  "flybody/fruitfly/assets/tarsus_T1_1_right_body.obj",
  "flybody/fruitfly/assets/tarsus_T1_2_left_body.msh",
  "flybody/fruitfly/assets/tarsus_T1_2_left_body.obj",
  "flybody/fruitfly/assets/tarsus_T1_2_right_body.msh",
  "flybody/fruitfly/assets/tarsus_T1_2_right_body.obj",
  "flybody/fruitfly/assets/tarsus_T1_3_left_body.msh",
  "flybody/fruitfly/assets/tarsus_T1_3_left_body.obj",
  "flybody/fruitfly/assets/tarsus_T1_3_right_body.msh",
  "flybody/fruitfly/assets/tarsus_T1_3_right_body.obj",
  "flybody/fruitfly/assets/tarsus_T1_4_left_body.msh",
  "flybody/fruitfly/assets/tarsus_T1_4_left_body.obj",
  "flybody/fruitfly/assets/tarsus_T1_4_right_body.msh",
  "flybody/fruitfly/assets/tarsus_T1_4_right_body.obj",
  "flybody/fruitfly/assets/tarsus_T2_1_left_body.msh",
  "flybody/fruitfly/assets/tarsus_T2_1_left_body.obj",
  "flybody/fruitfly/assets/tarsus_T2_1_right_body.msh",
  "flybody/fruitfly/assets/tarsus_T2_1_right_body.obj",
  "flybody/fruitfly/assets/tarsus_T2_2_left_body.msh",
  "flybody/fruitfly/assets/tarsus_T2_2_left_body.obj",
  "flybody/fruitfly/assets/tarsus_T2_2_right_body.msh",
  "flybody/fruitfly/assets/tarsus_T2_2_right_body.obj",
  "flybody/fruitfly/assets/tarsus_T2_3_left_body.msh",
  "flybody/fruitfly/assets/tarsus_T2_3_left_body.obj",
  "flybody/fruitfly/assets/tarsus_T2_3_right_body.msh",
  "flybody/fruitfly/assets/tarsus_T2_3_right_body.obj",
  "flybody/fruitfly/assets/tarsus_T2_4_left_body.msh",
  "flybody/fruitfly/assets/tarsus_T2_4_left_body.obj",
  "flybody/fruitfly/assets/tarsus_T2_4_right_body.msh",
  "flybody/fruitfly/assets/tarsus_T2_4_right_body.obj",
  "flybody/fruitfly/assets/tarsus_T3_1_left_body.msh",
  "flybody/fruitfly/assets/tarsus_T3_1_left_body.obj",
  "flybody/fruitfly/assets/tarsus_T3_1_right_body.msh",
  "flybody/fruitfly/assets/tarsus_T3_1_right_body.obj",
  "flybody/fruitfly/assets/tarsus_T3_2_left_body.msh",
  "flybody/fruitfly/assets/tarsus_T3_2_left_body.obj",
  "flybody/fruitfly/assets/tarsus_T3_2_right_body.msh",
  "flybody/fruitfly/assets/tarsus_T3_2_right_body.obj",
  "flybody/fruitfly/assets/tarsus_T3_3_left_body.msh",
  "flybody/fruitfly/assets/tarsus_T3_3_left_body.obj",
  "flybody/fruitfly/assets/tarsus_T3_3_right_body.msh",
  "flybody/fruitfly/assets/tarsus_T3_3_right_body.obj",
  "flybody/fruitfly/assets/tarsus_T3_4_left_body.msh",
  "flybody/fruitfly/assets/tarsus_T3_4_left_body.obj",
  "flybody/fruitfly/assets/tarsus_T3_4_right_body.msh",
  "flybody/fruitfly/assets/tarsus_T3_4_right_body.obj",
  "flybody/fruitfly/assets/thorax_black.msh",
  "flybody/fruitfly/assets/thorax_black.obj",
  "flybody/fruitfly/assets/thorax_body.msh",
  "flybody/fruitfly/assets/thorax_body.obj",
  "flybody/fruitfly/assets/tibia_T1_left_body.msh",
  "flybody/fruitfly/assets/tibia_T1_left_body.obj",
  "flybody/fruitfly/assets/tibia_T1_right_body.msh",
  "flybody/fruitfly/assets/tibia_T1_right_body.obj",
  "flybody/fruitfly/assets/tibia_T2_left_body.msh",
  "flybody/fruitfly/assets/tibia_T2_left_body.obj",
  "flybody/fruitfly/assets/tibia_T2_right_body.msh",
  "flybody/fruitfly/assets/tibia_T2_right_body.obj",
  "flybody/fruitfly/assets/tibia_T3_left_body.msh",
  "flybody/fruitfly/assets/tibia_T3_left_body.obj",
  "flybody/fruitfly/assets/tibia_T3_right_body.msh",
  "flybody/fruitfly/assets/tibia_T3_right_body.obj",
  "flybody/fruitfly/assets/wing_left_brown.msh",
  "flybody/fruitfly/assets/wing_left_brown.obj",
  "flybody/fruitfly/assets/wing_left_membrane.msh",
  "flybody/fruitfly/assets/wing_left_membrane.obj",
  "flybody/fruitfly/assets/wing_right_brown.msh",
  "flybody/fruitfly/assets/wing_right_brown.obj",
  "flybody/fruitfly/assets/wing_right_membrane.msh",
  "flybody/fruitfly/assets/wing_right_membrane.obj"
]
```

## Self comparisons

```json
[
  {
    "file": "flybody/fruitfly.xml",
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
    "counts": {},
    "classifications_changed": 0,
    "finding_membership_changes": 0
  },
  "2": {
    "provenance_method": "pinned",
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
      "thorax",
      "head",
      "rostrum",
      "haustellum",
      "labrum_left",
      "labrum_right",
      "antenna_left",
      "antenna_right",
      "wing_left",
      "wing_right",
      "abdomen",
      "abdomen_2",
      "abdomen_3",
      "abdomen_4",
      "abdomen_5",
      "abdomen_6",
      "abdomen_7",
      "haltere_left",
      "haltere_right",
      "coxa_T1_left",
      "femur_T1_left",
      "tibia_T1_left",
      "tarsus_T1_left",
      "tarsus2_T1_left",
      "tarsus3_T1_left",
      "tarsus4_T1_left",
      "claw_T1_left",
      "coxa_T1_right",
      "femur_T1_right",
      "tibia_T1_right",
      "tarsus_T1_right",
      "tarsus2_T1_right",
      "tarsus3_T1_right",
      "tarsus4_T1_right",
      "claw_T1_right",
      "coxa_T2_left",
      "femur_T2_left",
      "tibia_T2_left",
      "tarsus_T2_left",
      "tarsus2_T2_left",
      "tarsus3_T2_left",
      "tarsus4_T2_left",
      "claw_T2_left",
      "coxa_T2_right",
      "femur_T2_right",
      "tibia_T2_right",
      "tarsus_T2_right",
      "tarsus2_T2_right",
      "tarsus3_T2_right",
      "tarsus4_T2_right",
      "claw_T2_right",
      "coxa_T3_left",
      "femur_T3_left",
      "tibia_T3_left",
      "tarsus_T3_left",
      "tarsus2_T3_left",
      "tarsus3_T3_left",
      "tarsus4_T3_left",
      "claw_T3_left",
      "coxa_T3_right",
      "femur_T3_right",
      "tibia_T3_right",
      "tarsus_T3_right",
      "tarsus2_T3_right",
      "tarsus3_T3_right",
      "tarsus4_T3_right",
      "claw_T3_right"
    ],
    "assets_loaded": 85,
    "mesh_conversions": [],
    "nonphysical_normalizations": [],
    "xacro_arguments": {},
    "source_dependencies": [
      "flybody/fruitfly.xml",
      "flybody/assets/head_body.obj",
      "flybody/assets/head_red.obj",
      "flybody/assets/head_ocelli.obj",
      "flybody/assets/head_black.obj",
      "flybody/assets/haustellum_body.obj",
      "flybody/assets/haustellum_black.obj",
      "flybody/assets/rostrum_body.obj",
      "flybody/assets/rostrum_bristle-brown.obj",
      "flybody/assets/labrum_left_lower.obj",
      "flybody/assets/wing_left_brown.obj",
      "flybody/assets/wing_left_membrane.obj",
      "flybody/assets/antenna_left_body.obj",
      "flybody/assets/antenna_left_black.obj",
      "flybody/assets/haltere_left_body.obj",
      "flybody/assets/labrum_right_lower.obj",
      "flybody/assets/wing_right_brown.obj",
      "flybody/assets/wing_right_membrane.obj",
      "flybody/assets/antenna_right_body.obj",
      "flybody/assets/antenna_right_black.obj",
      "flybody/assets/haltere_right_body.obj",
      "flybody/assets/thorax_body.obj",
      "flybody/assets/thorax_black.obj",
      "flybody/assets/abdomen_1_body.obj",
      "flybody/assets/abdomen_1_lower.obj",
      "flybody/assets/abdomen_2_body.obj",
      "flybody/assets/abdomen_2_lower.obj",
      "flybody/assets/abdomen_3_body.obj",
      "flybody/assets/abdomen_3_lower.obj",
      "flybody/assets/abdomen_4_body.obj",
      "flybody/assets/abdomen_4_lower.obj",
      "flybody/assets/abdomen_5_body.obj",
      "flybody/assets/abdomen_5_lower.obj",
      "flybody/assets/abdomen_6_body.obj",
      "flybody/assets/abdomen_6_lower.obj",
      "flybody/assets/abdomen_7_body.obj",
      "flybody/assets/abdomen_7_lower.obj",
      "flybody/assets/abdomen_8_body.obj",
      "flybody/assets/tibia_T1_left_body.obj",
      "flybody/assets/tarsus_T1_1_left_body.obj",
      "flybody/assets/tarsus_T1_2_left_body.obj",
      "flybody/assets/tarsus_T1_3_left_body.obj",
      "flybody/assets/tarsus_T1_4_left_body.obj",
      "flybody/assets/tarsal_claw_T1_left_brown.obj",
      "flybody/assets/tarsus_T2_2_left_body.obj",
      "flybody/assets/tarsus_T2_3_left_body.obj",
      "flybody/assets/tarsus_T2_4_left_body.obj",
      "flybody/assets/tarsal_claw_T2_left_brown.obj",
      "flybody/assets/tarsus_T2_1_left_body.obj",
      "flybody/assets/tarsus_T3_2_left_body.obj",
      "flybody/assets/tarsus_T3_3_left_body.obj",
      "flybody/assets/tarsus_T3_4_left_body.obj",
      "flybody/assets/tarsal_claw_T3_left_brown.obj",
      "flybody/assets/tarsus_T3_1_left_body.obj",
      "flybody/assets/tibia_T2_left_body.obj",
      "flybody/assets/tibia_T3_left_body.obj",
      "flybody/assets/femur_T1_left_body.obj",
      "flybody/assets/femur_T2_left_body.obj",
      "flybody/assets/femur_T3_left_body.obj",
      "flybody/assets/femur_T1_right_body.obj",
      "flybody/assets/tibia_T1_right_body.obj",
      "flybody/assets/tarsus_T1_1_right_body.obj",
      "flybody/assets/tarsus_T1_2_right_body.obj",
      "flybody/assets/tarsus_T1_3_right_body.obj",
      "flybody/assets/tarsus_T1_4_right_body.obj",
      "flybody/assets/tarsal_claw_T1_right_brown.obj",
      "flybody/assets/femur_T2_right_body.obj",
      "flybody/assets/tibia_T2_right_body.obj",
      "flybody/assets/tarsus_T2_1_right_body.obj",
      "flybody/assets/tarsus_T2_2_right_body.obj",
      "flybody/assets/tarsus_T2_3_right_body.obj",
      "flybody/assets/tarsus_T2_4_right_body.obj",
      "flybody/assets/tarsal_claw_T2_right_brown.obj",
      "flybody/assets/femur_T3_right_body.obj",
      "flybody/assets/tibia_T3_right_body.obj",
      "flybody/assets/tarsus_T3_1_right_body.obj",
      "flybody/assets/tarsus_T3_2_right_body.obj",
      "flybody/assets/tarsus_T3_3_right_body.obj",
      "flybody/assets/tarsus_T3_4_right_body.obj",
      "flybody/assets/tarsal_claw_T3_right_brown.obj",
      "flybody/assets/coxa_T1_left_body.obj",
      "flybody/assets/coxa_T1_right_body.obj",
      "flybody/assets/coxa_T2_left_body.obj",
      "flybody/assets/coxa_T2_right_body.obj",
      "flybody/assets/coxa_T3_left_body.obj",
      "flybody/assets/coxa_T3_right_body.obj"
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
      "thorax",
      "head",
      "rostrum",
      "haustellum",
      "labrum_left",
      "labrum_right",
      "antenna_left",
      "antenna_right",
      "wing_left",
      "wing_right",
      "abdomen",
      "abdomen_2",
      "abdomen_3",
      "abdomen_4",
      "abdomen_5",
      "abdomen_6",
      "abdomen_7",
      "haltere_left",
      "haltere_right",
      "coxa_T1_left",
      "femur_T1_left",
      "tibia_T1_left",
      "tarsus_T1_left",
      "tarsus2_T1_left",
      "tarsus3_T1_left",
      "tarsus4_T1_left",
      "claw_T1_left",
      "coxa_T1_right",
      "femur_T1_right",
      "tibia_T1_right",
      "tarsus_T1_right",
      "tarsus2_T1_right",
      "tarsus3_T1_right",
      "tarsus4_T1_right",
      "claw_T1_right",
      "coxa_T2_left",
      "femur_T2_left",
      "tibia_T2_left",
      "tarsus_T2_left",
      "tarsus2_T2_left",
      "tarsus3_T2_left",
      "tarsus4_T2_left",
      "claw_T2_left",
      "coxa_T2_right",
      "femur_T2_right",
      "tibia_T2_right",
      "tarsus_T2_right",
      "tarsus2_T2_right",
      "tarsus3_T2_right",
      "tarsus4_T2_right",
      "claw_T2_right",
      "coxa_T3_left",
      "femur_T3_left",
      "tibia_T3_left",
      "tarsus_T3_left",
      "tarsus2_T3_left",
      "tarsus3_T3_left",
      "tarsus4_T3_left",
      "claw_T3_left",
      "coxa_T3_right",
      "femur_T3_right",
      "tibia_T3_right",
      "tarsus_T3_right",
      "tarsus2_T3_right",
      "tarsus3_T3_right",
      "tarsus4_T3_right",
      "claw_T3_right"
    ],
    "assets_loaded": 85,
    "mesh_conversions": [],
    "nonphysical_normalizations": [],
    "xacro_arguments": {},
    "source_dependencies": [
      "flybody/fruitfly/assets/fruitfly.xml",
      "flybody/fruitfly/assets/head_body.obj",
      "flybody/fruitfly/assets/head_red.obj",
      "flybody/fruitfly/assets/head_ocelli.obj",
      "flybody/fruitfly/assets/head_black.obj",
      "flybody/fruitfly/assets/haustellum_body.obj",
      "flybody/fruitfly/assets/haustellum_black.obj",
      "flybody/fruitfly/assets/rostrum_body.obj",
      "flybody/fruitfly/assets/rostrum_bristle-brown.obj",
      "flybody/fruitfly/assets/labrum_left_lower.obj",
      "flybody/fruitfly/assets/wing_left_brown.obj",
      "flybody/fruitfly/assets/wing_left_membrane.obj",
      "flybody/fruitfly/assets/antenna_left_body.obj",
      "flybody/fruitfly/assets/antenna_left_black.obj",
      "flybody/fruitfly/assets/haltere_left_body.obj",
      "flybody/fruitfly/assets/labrum_right_lower.obj",
      "flybody/fruitfly/assets/wing_right_brown.obj",
      "flybody/fruitfly/assets/wing_right_membrane.obj",
      "flybody/fruitfly/assets/antenna_right_body.obj",
      "flybody/fruitfly/assets/antenna_right_black.obj",
      "flybody/fruitfly/assets/haltere_right_body.obj",
      "flybody/fruitfly/assets/thorax_body.obj",
      "flybody/fruitfly/assets/thorax_black.obj",
      "flybody/fruitfly/assets/abdomen_1_body.obj",
      "flybody/fruitfly/assets/abdomen_1_lower.obj",
      "flybody/fruitfly/assets/abdomen_2_body.obj",
      "flybody/fruitfly/assets/abdomen_2_lower.obj",
      "flybody/fruitfly/assets/abdomen_3_body.obj",
      "flybody/fruitfly/assets/abdomen_3_lower.obj",
      "flybody/fruitfly/assets/abdomen_4_body.obj",
      "flybody/fruitfly/assets/abdomen_4_lower.obj",
      "flybody/fruitfly/assets/abdomen_5_body.obj",
      "flybody/fruitfly/assets/abdomen_5_lower.obj",
      "flybody/fruitfly/assets/abdomen_6_body.obj",
      "flybody/fruitfly/assets/abdomen_6_lower.obj",
      "flybody/fruitfly/assets/abdomen_7_body.obj",
      "flybody/fruitfly/assets/abdomen_7_lower.obj",
      "flybody/fruitfly/assets/abdomen_8_body.obj",
      "flybody/fruitfly/assets/tibia_T1_left_body.obj",
      "flybody/fruitfly/assets/tarsus_T1_1_left_body.obj",
      "flybody/fruitfly/assets/tarsus_T1_2_left_body.obj",
      "flybody/fruitfly/assets/tarsus_T1_3_left_body.obj",
      "flybody/fruitfly/assets/tarsus_T1_4_left_body.obj",
      "flybody/fruitfly/assets/tarsal_claw_T1_left_brown.obj",
      "flybody/fruitfly/assets/tarsus_T2_2_left_body.obj",
      "flybody/fruitfly/assets/tarsus_T2_3_left_body.obj",
      "flybody/fruitfly/assets/tarsus_T2_4_left_body.obj",
      "flybody/fruitfly/assets/tarsal_claw_T2_left_brown.obj",
      "flybody/fruitfly/assets/tarsus_T2_1_left_body.obj",
      "flybody/fruitfly/assets/tarsus_T3_2_left_body.obj",
      "flybody/fruitfly/assets/tarsus_T3_3_left_body.obj",
      "flybody/fruitfly/assets/tarsus_T3_4_left_body.obj",
      "flybody/fruitfly/assets/tarsal_claw_T3_left_brown.obj",
      "flybody/fruitfly/assets/tarsus_T3_1_left_body.obj",
      "flybody/fruitfly/assets/tibia_T2_left_body.obj",
      "flybody/fruitfly/assets/tibia_T3_left_body.obj",
      "flybody/fruitfly/assets/femur_T1_left_body.obj",
      "flybody/fruitfly/assets/femur_T2_left_body.obj",
      "flybody/fruitfly/assets/femur_T3_left_body.obj",
      "flybody/fruitfly/assets/femur_T1_right_body.obj",
      "flybody/fruitfly/assets/tibia_T1_right_body.obj",
      "flybody/fruitfly/assets/tarsus_T1_1_right_body.obj",
      "flybody/fruitfly/assets/tarsus_T1_2_right_body.obj",
      "flybody/fruitfly/assets/tarsus_T1_3_right_body.obj",
      "flybody/fruitfly/assets/tarsus_T1_4_right_body.obj",
      "flybody/fruitfly/assets/tarsal_claw_T1_right_brown.obj",
      "flybody/fruitfly/assets/femur_T2_right_body.obj",
      "flybody/fruitfly/assets/tibia_T2_right_body.obj",
      "flybody/fruitfly/assets/tarsus_T2_1_right_body.obj",
      "flybody/fruitfly/assets/tarsus_T2_2_right_body.obj",
      "flybody/fruitfly/assets/tarsus_T2_3_right_body.obj",
      "flybody/fruitfly/assets/tarsus_T2_4_right_body.obj",
      "flybody/fruitfly/assets/tarsal_claw_T2_right_brown.obj",
      "flybody/fruitfly/assets/femur_T3_right_body.obj",
      "flybody/fruitfly/assets/tibia_T3_right_body.obj",
      "flybody/fruitfly/assets/tarsus_T3_1_right_body.obj",
      "flybody/fruitfly/assets/tarsus_T3_2_right_body.obj",
      "flybody/fruitfly/assets/tarsus_T3_3_right_body.obj",
      "flybody/fruitfly/assets/tarsus_T3_4_right_body.obj",
      "flybody/fruitfly/assets/tarsal_claw_T3_right_brown.obj",
      "flybody/fruitfly/assets/coxa_T1_left_body.obj",
      "flybody/fruitfly/assets/coxa_T1_right_body.obj",
      "flybody/fruitfly/assets/coxa_T2_left_body.obj",
      "flybody/fruitfly/assets/coxa_T2_right_body.obj",
      "flybody/fruitfly/assets/coxa_T3_left_body.obj",
      "flybody/fruitfly/assets/coxa_T3_right_body.obj"
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
  "S": {
    "geometry_stripped": false,
    "missing_explicit_inertials": [
      "thorax",
      "head",
      "rostrum",
      "haustellum",
      "labrum_left",
      "labrum_right",
      "antenna_left",
      "antenna_right",
      "wing_left",
      "wing_right",
      "abdomen",
      "abdomen_2",
      "abdomen_3",
      "abdomen_4",
      "abdomen_5",
      "abdomen_6",
      "abdomen_7",
      "haltere_left",
      "haltere_right",
      "coxa_T1_left",
      "femur_T1_left",
      "tibia_T1_left",
      "tarsus_T1_left",
      "tarsus2_T1_left",
      "tarsus3_T1_left",
      "tarsus4_T1_left",
      "claw_T1_left",
      "coxa_T1_right",
      "femur_T1_right",
      "tibia_T1_right",
      "tarsus_T1_right",
      "tarsus2_T1_right",
      "tarsus3_T1_right",
      "tarsus4_T1_right",
      "claw_T1_right",
      "coxa_T2_left",
      "femur_T2_left",
      "tibia_T2_left",
      "tarsus_T2_left",
      "tarsus2_T2_left",
      "tarsus3_T2_left",
      "tarsus4_T2_left",
      "claw_T2_left",
      "coxa_T2_right",
      "femur_T2_right",
      "tibia_T2_right",
      "tarsus_T2_right",
      "tarsus2_T2_right",
      "tarsus3_T2_right",
      "tarsus4_T2_right",
      "claw_T2_right",
      "coxa_T3_left",
      "femur_T3_left",
      "tibia_T3_left",
      "tarsus_T3_left",
      "tarsus2_T3_left",
      "tarsus3_T3_left",
      "tarsus4_T3_left",
      "claw_T3_left",
      "coxa_T3_right",
      "femur_T3_right",
      "tibia_T3_right",
      "tarsus_T3_right",
      "tarsus2_T3_right",
      "tarsus3_T3_right",
      "tarsus4_T3_right",
      "claw_T3_right"
    ],
    "assets_loaded": 85,
    "mesh_conversions": [],
    "nonphysical_normalizations": [],
    "xacro_arguments": {},
    "source_dependencies": [
      "flybody/fruitfly/assets/fruitfly.xml",
      "flybody/fruitfly/assets/head_body.obj",
      "flybody/fruitfly/assets/head_red.obj",
      "flybody/fruitfly/assets/head_ocelli.obj",
      "flybody/fruitfly/assets/head_black.obj",
      "flybody/fruitfly/assets/haustellum_body.obj",
      "flybody/fruitfly/assets/haustellum_black.obj",
      "flybody/fruitfly/assets/rostrum_body.obj",
      "flybody/fruitfly/assets/rostrum_bristle-brown.obj",
      "flybody/fruitfly/assets/labrum_left_lower.obj",
      "flybody/fruitfly/assets/wing_left_brown.obj",
      "flybody/fruitfly/assets/wing_left_membrane.obj",
      "flybody/fruitfly/assets/antenna_left_body.obj",
      "flybody/fruitfly/assets/antenna_left_black.obj",
      "flybody/fruitfly/assets/haltere_left_body.obj",
      "flybody/fruitfly/assets/labrum_right_lower.obj",
      "flybody/fruitfly/assets/wing_right_brown.obj",
      "flybody/fruitfly/assets/wing_right_membrane.obj",
      "flybody/fruitfly/assets/antenna_right_body.obj",
      "flybody/fruitfly/assets/antenna_right_black.obj",
      "flybody/fruitfly/assets/haltere_right_body.obj",
      "flybody/fruitfly/assets/thorax_body.obj",
      "flybody/fruitfly/assets/thorax_black.obj",
      "flybody/fruitfly/assets/abdomen_1_body.obj",
      "flybody/fruitfly/assets/abdomen_1_lower.obj",
      "flybody/fruitfly/assets/abdomen_2_body.obj",
      "flybody/fruitfly/assets/abdomen_2_lower.obj",
      "flybody/fruitfly/assets/abdomen_3_body.obj",
      "flybody/fruitfly/assets/abdomen_3_lower.obj",
      "flybody/fruitfly/assets/abdomen_4_body.obj",
      "flybody/fruitfly/assets/abdomen_4_lower.obj",
      "flybody/fruitfly/assets/abdomen_5_body.obj",
      "flybody/fruitfly/assets/abdomen_5_lower.obj",
      "flybody/fruitfly/assets/abdomen_6_body.obj",
      "flybody/fruitfly/assets/abdomen_6_lower.obj",
      "flybody/fruitfly/assets/abdomen_7_body.obj",
      "flybody/fruitfly/assets/abdomen_7_lower.obj",
      "flybody/fruitfly/assets/abdomen_8_body.obj",
      "flybody/fruitfly/assets/tibia_T1_left_body.obj",
      "flybody/fruitfly/assets/tarsus_T1_1_left_body.obj",
      "flybody/fruitfly/assets/tarsus_T1_2_left_body.obj",
      "flybody/fruitfly/assets/tarsus_T1_3_left_body.obj",
      "flybody/fruitfly/assets/tarsus_T1_4_left_body.obj",
      "flybody/fruitfly/assets/tarsal_claw_T1_left_brown.obj",
      "flybody/fruitfly/assets/tarsus_T2_2_left_body.obj",
      "flybody/fruitfly/assets/tarsus_T2_3_left_body.obj",
      "flybody/fruitfly/assets/tarsus_T2_4_left_body.obj",
      "flybody/fruitfly/assets/tarsal_claw_T2_left_brown.obj",
      "flybody/fruitfly/assets/tarsus_T2_1_left_body.obj",
      "flybody/fruitfly/assets/tarsus_T3_2_left_body.obj",
      "flybody/fruitfly/assets/tarsus_T3_3_left_body.obj",
      "flybody/fruitfly/assets/tarsus_T3_4_left_body.obj",
      "flybody/fruitfly/assets/tarsal_claw_T3_left_brown.obj",
      "flybody/fruitfly/assets/tarsus_T3_1_left_body.obj",
      "flybody/fruitfly/assets/tibia_T2_left_body.obj",
      "flybody/fruitfly/assets/tibia_T3_left_body.obj",
      "flybody/fruitfly/assets/femur_T1_left_body.obj",
      "flybody/fruitfly/assets/femur_T2_left_body.obj",
      "flybody/fruitfly/assets/femur_T3_left_body.obj",
      "flybody/fruitfly/assets/femur_T1_right_body.obj",
      "flybody/fruitfly/assets/tibia_T1_right_body.obj",
      "flybody/fruitfly/assets/tarsus_T1_1_right_body.obj",
      "flybody/fruitfly/assets/tarsus_T1_2_right_body.obj",
      "flybody/fruitfly/assets/tarsus_T1_3_right_body.obj",
      "flybody/fruitfly/assets/tarsus_T1_4_right_body.obj",
      "flybody/fruitfly/assets/tarsal_claw_T1_right_brown.obj",
      "flybody/fruitfly/assets/femur_T2_right_body.obj",
      "flybody/fruitfly/assets/tibia_T2_right_body.obj",
      "flybody/fruitfly/assets/tarsus_T2_1_right_body.obj",
      "flybody/fruitfly/assets/tarsus_T2_2_right_body.obj",
      "flybody/fruitfly/assets/tarsus_T2_3_right_body.obj",
      "flybody/fruitfly/assets/tarsus_T2_4_right_body.obj",
      "flybody/fruitfly/assets/tarsal_claw_T2_right_brown.obj",
      "flybody/fruitfly/assets/femur_T3_right_body.obj",
      "flybody/fruitfly/assets/tibia_T3_right_body.obj",
      "flybody/fruitfly/assets/tarsus_T3_1_right_body.obj",
      "flybody/fruitfly/assets/tarsus_T3_2_right_body.obj",
      "flybody/fruitfly/assets/tarsus_T3_3_right_body.obj",
      "flybody/fruitfly/assets/tarsus_T3_4_right_body.obj",
      "flybody/fruitfly/assets/tarsal_claw_T3_right_brown.obj",
      "flybody/fruitfly/assets/coxa_T1_left_body.obj",
      "flybody/fruitfly/assets/coxa_T1_right_body.obj",
      "flybody/fruitfly/assets/coxa_T2_left_body.obj",
      "flybody/fruitfly/assets/coxa_T2_right_body.obj",
      "flybody/fruitfly/assets/coxa_T3_left_body.obj",
      "flybody/fruitfly/assets/coxa_T3_right_body.obj"
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
  "historical_snapshots_reused": 5,
  "primary_physics_unchanged": true,
  "source_matching": "original raw-value provenance criteria retained; kinematic guard applies to reported CoM"
}
```
