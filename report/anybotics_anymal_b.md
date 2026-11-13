# anybotics_anymal_b

Status: **complete**. Provenance: **none**, confidence **none**.

No public revision matches all comparable quantities. Class: NO MATCHING SOURCE; never counted as STALE.

M: `https://github.com/google-deepmind/mujoco_menagerie`, `anybotics_anymal_b/anymal_b.xml`, commit `370c43965323c0944b433b202aac5058b5f907a9`.
H: `https://github.com/ANYbotics/anymal_b_simple_description`, `urdf/anymal.urdf`, commit `988b5df22b84761bdf08111b1c2ccc883793f456`.
S: unavailable. A machine-readable H can still be compared to M; no-match differences are never counted as STALE.

Limit semantics: MJCF effort values are supported actuator torque/force envelopes. URDF effort and velocity values are manufacturer declarations retained from XML; MuJoCo does not enforce those tags. Such declaration comparisons are explicitly distinct from compiled inertial/range quantities.


## Source evidence

```json
[
  {
    "url": "https://github.com/ANYbotics/anymal_b_simple_description",
    "document": "anybotics_anymal_b/README.md",
    "commit": "370c43965323c0944b433b202aac5058b5f907a9",
    "current": true
  },
  {
    "url": "https://github.com/ANYbotics/anymal_b_simple_description/blob/master/urdf/anymal.urdf",
    "document": "anybotics_anymal_b/README.md",
    "commit": "370c43965323c0944b433b202aac5058b5f907a9",
    "current": true
  },
  {
    "url": "https://github.com/ANYbotics/anymal_b_simple_description/tree/master/meshes",
    "document": "anybotics_anymal_b/README.md",
    "commit": "370c43965323c0944b433b202aac5058b5f907a9",
    "current": true
  },
  {
    "url": "https://github.com/kevinzakka/obj2mjcf",
    "document": "anybotics_anymal_b/README.md",
    "commit": "370c43965323c0944b433b202aac5058b5f907a9",
    "current": true
  }
]
```


## Kinematics consistency

A proper Kabsch rigid transform aligns all matched zero-pose body origins. The maximum per-origin residual and signed hinge/slide axis angles determine whether CoM can be compared; RMS is also recorded. Fewer than three non-collinear origins give insufficient kinematic coverage. CoM records that fail either required M/H or M/S check are excluded from counts and largest discrepancies. Masses, principal moments and raw joint ranges remain unchanged; a flagged range still requires convention review.

| Pair | Status | Origins / rank | RMS / maximum mm | Disagreeing / checked axes |
|---|---|---:|---:|---:|
| M/H | consistent | 13 / 3 | 1.27710411e-13 / 2.2887834e-13 | 0 / 12 |

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
    "anchor_m": "base",
    "anchor_other": "base",
    "rotation_other_to_m": [
      [
        1.0,
        8.686526225731558e-18,
        -5.93414729475916e-18
      ],
      [
        -8.686526225731565e-18,
        1.0000000000000007,
        -1.263313355693855e-16
      ],
      [
        5.934147294759161e-18,
        8.173377006494777e-17,
        1.0000000000000002
      ]
    ],
    "translation_other_to_m": [
      -4.564728688276277e-19,
      -9.717795043798886e-18,
      1.3877787807814457e-17
    ],
    "rms_residual_m": 1.2771041144355181e-16,
    "max_residual_m": 2.2887833992611187e-16,
    "fit_rank": 3,
    "axis_checks": [
      {
        "joint_m": "LF_HAA",
        "joint_other": "LF_HAA",
        "axis_m": [
          1.0,
          0.0,
          0.0
        ],
        "axis_other_aligned": [
          1.0,
          -8.686526225731565e-18,
          5.934147294759161e-18
        ],
        "angle_rad": 1.0519973478399065e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "LF_HFE",
        "joint_other": "LF_HFE",
        "axis_m": [
          0.0,
          1.0,
          0.0
        ],
        "axis_other_aligned": [
          8.686526225731552e-18,
          1.0,
          8.173377006494772e-17
        ],
        "angle_rad": 8.219406856276228e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "LF_KFE",
        "joint_other": "LF_KFE",
        "axis_m": [
          0.0,
          1.0,
          0.0
        ],
        "axis_other_aligned": [
          8.686526225731552e-18,
          1.0,
          8.173377006494772e-17
        ],
        "angle_rad": 8.219406856276228e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "RF_HAA",
        "joint_other": "RF_HAA",
        "axis_m": [
          1.0,
          0.0,
          0.0
        ],
        "axis_other_aligned": [
          1.0,
          -8.686526225731565e-18,
          5.934147294759161e-18
        ],
        "angle_rad": 1.0519973478399065e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "RF_HFE",
        "joint_other": "RF_HFE",
        "axis_m": [
          0.0,
          1.0,
          0.0
        ],
        "axis_other_aligned": [
          8.686526225731552e-18,
          1.0,
          8.173377006494772e-17
        ],
        "angle_rad": 8.219406856276228e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "RF_KFE",
        "joint_other": "RF_KFE",
        "axis_m": [
          0.0,
          1.0,
          0.0
        ],
        "axis_other_aligned": [
          8.686526225731552e-18,
          1.0,
          8.173377006494772e-17
        ],
        "angle_rad": 8.219406856276228e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "LH_HAA",
        "joint_other": "LH_HAA",
        "axis_m": [
          1.0,
          0.0,
          0.0
        ],
        "axis_other_aligned": [
          1.0,
          -8.686526225731565e-18,
          5.934147294759161e-18
        ],
        "angle_rad": 1.0519973478399065e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "LH_HFE",
        "joint_other": "LH_HFE",
        "axis_m": [
          0.0,
          1.0,
          0.0
        ],
        "axis_other_aligned": [
          8.686526225731552e-18,
          1.0,
          8.173377006494772e-17
        ],
        "angle_rad": 8.219406856276228e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "LH_KFE",
        "joint_other": "LH_KFE",
        "axis_m": [
          0.0,
          1.0,
          0.0
        ],
        "axis_other_aligned": [
          8.686526225731552e-18,
          1.0,
          8.173377006494772e-17
        ],
        "angle_rad": 8.219406856276228e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "RH_HAA",
        "joint_other": "RH_HAA",
        "axis_m": [
          1.0,
          0.0,
          0.0
        ],
        "axis_other_aligned": [
          1.0,
          -8.686526225731565e-18,
          5.934147294759161e-18
        ],
        "angle_rad": 1.0519973478399065e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "RH_HFE",
        "joint_other": "RH_HFE",
        "axis_m": [
          0.0,
          1.0,
          0.0
        ],
        "axis_other_aligned": [
          8.686526225731552e-18,
          1.0,
          8.173377006494772e-17
        ],
        "angle_rad": 8.219406856276228e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "RH_KFE",
        "joint_other": "RH_KFE",
        "axis_m": [
          0.0,
          1.0,
          0.0
        ],
        "axis_other_aligned": [
          8.686526225731552e-18,
          1.0,
          8.173377006494772e-17
        ],
        "angle_rad": 8.219406856276228e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      }
    ],
    "axis_disagreements": [],
    "com_eligible": true,
    "covariance_singular_values": [
      1.234438,
      0.43544400000000005,
      0.17307692307692307
    ],
    "origin_residuals_m": {
      "base": 1.6948064858029708e-17,
      "LF_HIP": 6.088202620573634e-17,
      "LF_THIGH": 1.1467954096648224e-16,
      "LF_SHANK": 2.2887833992611187e-16,
      "RF_HIP": 9.733212991297046e-17,
      "RF_THIGH": 1.11064634335138e-16,
      "RF_SHANK": 1.2412670766236366e-16,
      "LH_HIP": 7.270744419456325e-17,
      "LH_THIGH": 1.1373442195020432e-16,
      "LH_SHANK": 2.2887833992611187e-16,
      "RH_HIP": 8.331222192757738e-17,
      "RH_THIGH": 1.1102658353749596e-16,
      "RH_SHANK": 1.2412670766236366e-16
    },
    "reason": "Unique proper rigid fit and matched signed axes meet the configured thresholds"
  }
}
```


## Every reported quantity difference

Counts are quantity records, including correlated total/subtree/body mass records; they are not independent robot defects.

| Entity / quantity | M | S | H | H − M | Class | M source | S source | H source |
|---|---|---|---|---|---|---|---|---|
| robot / total_mass | 33.330552 | unavailable | 70.6143421 | 37.2837901 | NO MATCHING SOURCE | [aggregate inputs](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/anybotics_anymal_b/anymal_b.xml#L1) | unavailable | [aggregate inputs](https://github.com/ANYbotics/anymal_b_simple_description/blob/988b5df22b84761bdf08111b1c2ccc883793f456/urdf/anymal.urdf#L1) |
| robot / total_com_registered | [0.00144038269, 0, -0.0359202229] | unavailable | [-0.000466260113, -0.000336091554, 0.0175822394] | [-0.0019066428, -0.000336091554, 0.0535024622] | NO MATCHING SOURCE | [aggregate inputs](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/anybotics_anymal_b/anymal_b.xml#L1) | unavailable | [aggregate inputs](https://github.com/ANYbotics/anymal_b_simple_description/blob/988b5df22b84761bdf08111b1c2ccc883793f456/urdf/anymal.urdf#L1) |
| base / mass | 19.2035 | unavailable | 39.6937927 | 20.4902927 | NO MATCHING SOURCE | [input L136](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/anybotics_anymal_b/anymal_b.xml#L136) | unavailable | [geometry/inference input L13](https://github.com/ANYbotics/anymal_b_simple_description/blob/988b5df22b84761bdf08111b1c2ccc883793f456/urdf/anymal.urdf#L13) |
| base / subtree_mass | 33.330552 | unavailable | 70.6143421 | 37.2837901 | NO MATCHING SOURCE | [subtree root L133](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/anybotics_anymal_b/anymal_b.xml#L133) | unavailable | [subtree root L13](https://github.com/ANYbotics/anymal_b_simple_description/blob/988b5df22b84761bdf08111b1c2ccc883793f456/urdf/anymal.urdf#L13) |
| base / com_registered | [0.0025, 0, 0.0502071] | unavailable | [-7.54689392e-19, -1.77182407e-17, 0.0644886222] | [-0.0025, -1.77182407e-17, 0.0142815222] | NO MATCHING SOURCE | [CoM/kinematic input L136](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/anybotics_anymal_b/anymal_b.xml#L136) | unavailable | [geometry/inference input L13](https://github.com/ANYbotics/anymal_b_simple_description/blob/988b5df22b84761bdf08111b1c2ccc883793f456/urdf/anymal.urdf#L13) |
| base / principal_moments | [0.217374, 0.624031, 0.639559] | unavailable | [0.494962644, 1.29714756, 1.31110827] | [0.277588644, 0.673116565, 0.671549267] | NO MATCHING SOURCE | [inertia input L136](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/anybotics_anymal_b/anymal_b.xml#L136) | unavailable | [geometry/inference input L13](https://github.com/ANYbotics/anymal_b_simple_description/blob/988b5df22b84761bdf08111b1c2ccc883793f456/urdf/anymal.urdf#L13) |
| LF_SHANK / mass | 0.472163 | unavailable | 0.207204302 | -0.264958698 | NO MATCHING SOURCE | [input L181](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/anybotics_anymal_b/anymal_b.xml#L181) | unavailable | [input L186](https://github.com/ANYbotics/anymal_b_simple_description/blob/988b5df22b84761bdf08111b1c2ccc883793f456/urdf/anymal.urdf#L186) |
| LF_SHANK / com_registered | [0.4101396, 0.2527506, -0.400905] | unavailable | [0.371316858, 0.261382771, -0.249106874] | [-0.0388227419, 0.00863217071, 0.151798126] | NO MATCHING SOURCE | [CoM/kinematic input L181](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/anybotics_anymal_b/anymal_b.xml#L181) | unavailable | [CoM/kinematic input L185](https://github.com/ANYbotics/anymal_b_simple_description/blob/988b5df22b84761bdf08111b1c2ccc883793f456/urdf/anymal.urdf#L185) |
| LF_SHANK / principal_moments | [0.000723761, 0.0110666, 0.0116034] | unavailable | [0.00020338297, 0.000545293162, 0.000683114778] | [-0.00052037803, -0.0105213068, -0.0109202852] | NO MATCHING SOURCE | [inertia input L181](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/anybotics_anymal_b/anymal_b.xml#L181) | unavailable | [inertia input L187](https://github.com/ANYbotics/anymal_b_simple_description/blob/988b5df22b84761bdf08111b1c2ccc883793f456/urdf/anymal.urdf#L187) |
| RF_SHANK / mass | 0.472163 | unavailable | 0.207204302 | -0.264958698 | NO MATCHING SOURCE | [input L225](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/anybotics_anymal_b/anymal_b.xml#L225) | unavailable | [input L346](https://github.com/ANYbotics/anymal_b_simple_description/blob/988b5df22b84761bdf08111b1c2ccc883793f456/urdf/anymal.urdf#L346) |
| RF_SHANK / com_registered | [0.4101396, -0.2527506, -0.400905] | unavailable | [0.371316858, -0.261382771, -0.249106874] | [-0.0388227419, -0.00863217071, 0.151798126] | NO MATCHING SOURCE | [CoM/kinematic input L225](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/anybotics_anymal_b/anymal_b.xml#L225) | unavailable | [CoM/kinematic input L345](https://github.com/ANYbotics/anymal_b_simple_description/blob/988b5df22b84761bdf08111b1c2ccc883793f456/urdf/anymal.urdf#L345) |
| RF_SHANK / principal_moments | [0.000723761, 0.0110666, 0.0116034] | unavailable | [0.00020338297, 0.000545293162, 0.000683114778] | [-0.00052037803, -0.0105213068, -0.0109202852] | NO MATCHING SOURCE | [inertia input L225](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/anybotics_anymal_b/anymal_b.xml#L225) | unavailable | [inertia input L347](https://github.com/ANYbotics/anymal_b_simple_description/blob/988b5df22b84761bdf08111b1c2ccc883793f456/urdf/anymal.urdf#L347) |
| LH_SHANK / mass | 0.472163 | unavailable | 0.207204302 | -0.264958698 | NO MATCHING SOURCE | [input L269](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/anybotics_anymal_b/anymal_b.xml#L269) | unavailable | [input L506](https://github.com/ANYbotics/anymal_b_simple_description/blob/988b5df22b84761bdf08111b1c2ccc883793f456/urdf/anymal.urdf#L506) |
| LH_SHANK / com_registered | [-0.4101396, 0.2527506, -0.400905] | unavailable | [-0.371316858, 0.261382771, -0.249106874] | [0.0388227419, 0.00863217071, 0.151798126] | NO MATCHING SOURCE | [CoM/kinematic input L269](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/anybotics_anymal_b/anymal_b.xml#L269) | unavailable | [CoM/kinematic input L505](https://github.com/ANYbotics/anymal_b_simple_description/blob/988b5df22b84761bdf08111b1c2ccc883793f456/urdf/anymal.urdf#L505) |
| LH_SHANK / principal_moments | [0.000723761, 0.0110666, 0.0116034] | unavailable | [0.00020338297, 0.000545293162, 0.000683114778] | [-0.00052037803, -0.0105213068, -0.0109202852] | NO MATCHING SOURCE | [inertia input L269](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/anybotics_anymal_b/anymal_b.xml#L269) | unavailable | [inertia input L507](https://github.com/ANYbotics/anymal_b_simple_description/blob/988b5df22b84761bdf08111b1c2ccc883793f456/urdf/anymal.urdf#L507) |
| RH_SHANK / mass | 0.472163 | unavailable | 0.207204302 | -0.264958698 | NO MATCHING SOURCE | [input L313](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/anybotics_anymal_b/anymal_b.xml#L313) | unavailable | [input L666](https://github.com/ANYbotics/anymal_b_simple_description/blob/988b5df22b84761bdf08111b1c2ccc883793f456/urdf/anymal.urdf#L666) |
| RH_SHANK / com_registered | [-0.4101396, -0.2527506, -0.400905] | unavailable | [-0.371316858, -0.261382771, -0.249106874] | [0.0388227419, -0.00863217071, 0.151798126] | NO MATCHING SOURCE | [CoM/kinematic input L313](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/anybotics_anymal_b/anymal_b.xml#L313) | unavailable | [CoM/kinematic input L665](https://github.com/ANYbotics/anymal_b_simple_description/blob/988b5df22b84761bdf08111b1c2ccc883793f456/urdf/anymal.urdf#L665) |
| RH_SHANK / principal_moments | [0.000723761, 0.0110666, 0.0116034] | unavailable | [0.00020338297, 0.000545293162, 0.000683114778] | [-0.00052037803, -0.0105213068, -0.0109202852] | NO MATCHING SOURCE | [inertia input L313](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/anybotics_anymal_b/anymal_b.xml#L313) | unavailable | [inertia input L667](https://github.com/ANYbotics/anymal_b_simple_description/blob/988b5df22b84761bdf08111b1c2ccc883793f456/urdf/anymal.urdf#L667) |
| LF_HAA / effort | 40 | unavailable | 80 | 40 | NO MATCHING SOURCE | [inherited actuator input L65](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/anybotics_anymal_b/anymal_b.xml#L65) | unavailable | [input L123](https://github.com/ANYbotics/anymal_b_simple_description/blob/988b5df22b84761bdf08111b1c2ccc883793f456/urdf/anymal.urdf#L123) |
| LF_HFE / effort | 40 | unavailable | 80 | 40 | NO MATCHING SOURCE | [inherited actuator input L65](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/anybotics_anymal_b/anymal_b.xml#L65) | unavailable | [input L167](https://github.com/ANYbotics/anymal_b_simple_description/blob/988b5df22b84761bdf08111b1c2ccc883793f456/urdf/anymal.urdf#L167) |
| LF_KFE / effort | 40 | unavailable | 80 | 40 | NO MATCHING SOURCE | [inherited actuator input L65](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/anybotics_anymal_b/anymal_b.xml#L65) | unavailable | [input L196](https://github.com/ANYbotics/anymal_b_simple_description/blob/988b5df22b84761bdf08111b1c2ccc883793f456/urdf/anymal.urdf#L196) |
| RF_HAA / effort | 40 | unavailable | 80 | 40 | NO MATCHING SOURCE | [inherited actuator input L65](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/anybotics_anymal_b/anymal_b.xml#L65) | unavailable | [input L283](https://github.com/ANYbotics/anymal_b_simple_description/blob/988b5df22b84761bdf08111b1c2ccc883793f456/urdf/anymal.urdf#L283) |
| RF_HFE / effort | 40 | unavailable | 80 | 40 | NO MATCHING SOURCE | [inherited actuator input L65](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/anybotics_anymal_b/anymal_b.xml#L65) | unavailable | [input L327](https://github.com/ANYbotics/anymal_b_simple_description/blob/988b5df22b84761bdf08111b1c2ccc883793f456/urdf/anymal.urdf#L327) |
| RF_KFE / effort | 40 | unavailable | 80 | 40 | NO MATCHING SOURCE | [inherited actuator input L65](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/anybotics_anymal_b/anymal_b.xml#L65) | unavailable | [input L356](https://github.com/ANYbotics/anymal_b_simple_description/blob/988b5df22b84761bdf08111b1c2ccc883793f456/urdf/anymal.urdf#L356) |
| LH_HAA / effort | 40 | unavailable | 80 | 40 | NO MATCHING SOURCE | [inherited actuator input L65](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/anybotics_anymal_b/anymal_b.xml#L65) | unavailable | [input L443](https://github.com/ANYbotics/anymal_b_simple_description/blob/988b5df22b84761bdf08111b1c2ccc883793f456/urdf/anymal.urdf#L443) |
| LH_HFE / effort | 40 | unavailable | 80 | 40 | NO MATCHING SOURCE | [inherited actuator input L65](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/anybotics_anymal_b/anymal_b.xml#L65) | unavailable | [input L487](https://github.com/ANYbotics/anymal_b_simple_description/blob/988b5df22b84761bdf08111b1c2ccc883793f456/urdf/anymal.urdf#L487) |
| LH_KFE / effort | 40 | unavailable | 80 | 40 | NO MATCHING SOURCE | [inherited actuator input L65](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/anybotics_anymal_b/anymal_b.xml#L65) | unavailable | [input L516](https://github.com/ANYbotics/anymal_b_simple_description/blob/988b5df22b84761bdf08111b1c2ccc883793f456/urdf/anymal.urdf#L516) |
| RH_HAA / effort | 40 | unavailable | 80 | 40 | NO MATCHING SOURCE | [inherited actuator input L65](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/anybotics_anymal_b/anymal_b.xml#L65) | unavailable | [input L603](https://github.com/ANYbotics/anymal_b_simple_description/blob/988b5df22b84761bdf08111b1c2ccc883793f456/urdf/anymal.urdf#L603) |
| RH_HFE / effort | 40 | unavailable | 80 | 40 | NO MATCHING SOURCE | [inherited actuator input L65](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/anybotics_anymal_b/anymal_b.xml#L65) | unavailable | [input L647](https://github.com/ANYbotics/anymal_b_simple_description/blob/988b5df22b84761bdf08111b1c2ccc883793f456/urdf/anymal.urdf#L647) |
| RH_KFE / effort | 40 | unavailable | 80 | 40 | NO MATCHING SOURCE | [inherited actuator input L65](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/anybotics_anymal_b/anymal_b.xml#L65) | unavailable | [input L676](https://github.com/ANYbotics/anymal_b_simple_description/blob/988b5df22b84761bdf08111b1c2ccc883793f456/urdf/anymal.urdf#L676) |

## Raw CoM records and reporting decisions

Raw values retain the previous root-anchor registration before Kabsch; original world coordinates also remain in the snapshots. Eligible findings above use the fitted transform into M. Excluded raw records below are diagnostic numbers, not findings. No CoM suppression applies to mass or principal inertia moments.

| Entity / quantity | Raw M | Raw S | Raw H | Raw H − M | Decision | M source | S source | H source |
|---|---|---|---|---|---|---|---|---|
| robot / total_com_registered | [0.00144038269, 0, -0.0359202229] | unavailable | [-0.000466260113, -0.000336091554, 0.0175822394] | [-0.0019066428, -0.000336091554, 0.0535024622] | eligible; compared after Kabsch alignment | [aggregate inputs](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/anybotics_anymal_b/anymal_b.xml#L1) | unavailable | [aggregate inputs](https://github.com/ANYbotics/anymal_b_simple_description/blob/988b5df22b84761bdf08111b1c2ccc883793f456/urdf/anymal.urdf#L1) |
| base / com_registered | [0.0025, 0, 0.0502071] | unavailable | [8.44684599e-20, 1.46488161e-19, 0.0644886222] | [-0.0025, 1.46488161e-19, 0.0142815222] | eligible; compared after Kabsch alignment | [CoM/kinematic input L136](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/anybotics_anymal_b/anymal_b.xml#L136) | unavailable | [geometry/inference input L13](https://github.com/ANYbotics/anymal_b_simple_description/blob/988b5df22b84761bdf08111b1c2ccc883793f456/urdf/anymal.urdf#L13) |
| LF_HIP / com_registered | [0.3415163, 0.1122129, -0.000152184] | unavailable | [0.341516258, 0.112212898, -0.000152184388] | [-4.1853e-08, -1.702e-09, -3.87999945e-10] | eligible; compared after Kabsch alignment | [CoM/kinematic input L155](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/anybotics_anymal_b/anymal_b.xml#L155) | unavailable | [CoM/kinematic input L112](https://github.com/ANYbotics/anymal_b_simple_description/blob/988b5df22b84761bdf08111b1c2ccc883793f456/urdf/anymal.urdf#L112) |
| LF_THIGH / com_registered | [0.33660203, 0.2112266, -0.214583] | unavailable | [0.336602032, 0.211226619, -0.214583374] | [1.91799998e-09, 1.8537e-08, -3.73795e-07] | eligible; compared after Kabsch alignment | [CoM/kinematic input L168](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/anybotics_anymal_b/anymal_b.xml#L168) | unavailable | [CoM/kinematic input L156](https://github.com/ANYbotics/anymal_b_simple_description/blob/988b5df22b84761bdf08111b1c2ccc883793f456/urdf/anymal.urdf#L156) |
| LF_SHANK / com_registered | [0.4101396, 0.2527506, -0.400905] | unavailable | [0.371316858, 0.261382771, -0.249106874] | [-0.0388227419, 0.00863217071, 0.151798126] | eligible; compared after Kabsch alignment | [CoM/kinematic input L181](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/anybotics_anymal_b/anymal_b.xml#L181) | unavailable | [CoM/kinematic input L185](https://github.com/ANYbotics/anymal_b_simple_description/blob/988b5df22b84761bdf08111b1c2ccc883793f456/urdf/anymal.urdf#L185) |
| RF_HIP / com_registered | [0.3415163, -0.1122129, -0.000152184] | unavailable | [0.341516258, -0.112212898, -0.000152184388] | [-4.1853e-08, 1.702e-09, -3.87999945e-10] | eligible; compared after Kabsch alignment | [CoM/kinematic input L199](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/anybotics_anymal_b/anymal_b.xml#L199) | unavailable | [CoM/kinematic input L272](https://github.com/ANYbotics/anymal_b_simple_description/blob/988b5df22b84761bdf08111b1c2ccc883793f456/urdf/anymal.urdf#L272) |
| RF_THIGH / com_registered | [0.33660203, -0.2112266, -0.214583] | unavailable | [0.336602032, -0.211226619, -0.214583374] | [1.91799998e-09, -1.8537e-08, -3.73795e-07] | eligible; compared after Kabsch alignment | [CoM/kinematic input L212](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/anybotics_anymal_b/anymal_b.xml#L212) | unavailable | [CoM/kinematic input L316](https://github.com/ANYbotics/anymal_b_simple_description/blob/988b5df22b84761bdf08111b1c2ccc883793f456/urdf/anymal.urdf#L316) |
| RF_SHANK / com_registered | [0.4101396, -0.2527506, -0.400905] | unavailable | [0.371316858, -0.261382771, -0.249106874] | [-0.0388227419, -0.00863217071, 0.151798126] | eligible; compared after Kabsch alignment | [CoM/kinematic input L225](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/anybotics_anymal_b/anymal_b.xml#L225) | unavailable | [CoM/kinematic input L345](https://github.com/ANYbotics/anymal_b_simple_description/blob/988b5df22b84761bdf08111b1c2ccc883793f456/urdf/anymal.urdf#L345) |
| LH_HIP / com_registered | [-0.3415163, 0.1122129, -0.000152184] | unavailable | [-0.341516258, 0.112212898, -0.000152184388] | [4.1853e-08, -1.702e-09, -3.87999945e-10] | eligible; compared after Kabsch alignment | [CoM/kinematic input L243](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/anybotics_anymal_b/anymal_b.xml#L243) | unavailable | [CoM/kinematic input L432](https://github.com/ANYbotics/anymal_b_simple_description/blob/988b5df22b84761bdf08111b1c2ccc883793f456/urdf/anymal.urdf#L432) |
| LH_THIGH / com_registered | [-0.33660203, 0.2112266, -0.214583] | unavailable | [-0.336602032, 0.211226619, -0.214583374] | [-1.91799998e-09, 1.8537e-08, -3.73795e-07] | eligible; compared after Kabsch alignment | [CoM/kinematic input L256](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/anybotics_anymal_b/anymal_b.xml#L256) | unavailable | [CoM/kinematic input L476](https://github.com/ANYbotics/anymal_b_simple_description/blob/988b5df22b84761bdf08111b1c2ccc883793f456/urdf/anymal.urdf#L476) |
| LH_SHANK / com_registered | [-0.4101396, 0.2527506, -0.400905] | unavailable | [-0.371316858, 0.261382771, -0.249106874] | [0.0388227419, 0.00863217071, 0.151798126] | eligible; compared after Kabsch alignment | [CoM/kinematic input L269](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/anybotics_anymal_b/anymal_b.xml#L269) | unavailable | [CoM/kinematic input L505](https://github.com/ANYbotics/anymal_b_simple_description/blob/988b5df22b84761bdf08111b1c2ccc883793f456/urdf/anymal.urdf#L505) |
| RH_HIP / com_registered | [-0.3415163, -0.1122129, -0.000152184] | unavailable | [-0.341516258, -0.112212898, -0.000152184388] | [4.1853e-08, 1.702e-09, -3.87999945e-10] | eligible; compared after Kabsch alignment | [CoM/kinematic input L287](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/anybotics_anymal_b/anymal_b.xml#L287) | unavailable | [CoM/kinematic input L592](https://github.com/ANYbotics/anymal_b_simple_description/blob/988b5df22b84761bdf08111b1c2ccc883793f456/urdf/anymal.urdf#L592) |
| RH_THIGH / com_registered | [-0.33660203, -0.2112266, -0.214583] | unavailable | [-0.336602032, -0.211226619, -0.214583374] | [-1.91799998e-09, -1.8537e-08, -3.73795e-07] | eligible; compared after Kabsch alignment | [CoM/kinematic input L300](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/anybotics_anymal_b/anymal_b.xml#L300) | unavailable | [CoM/kinematic input L636](https://github.com/ANYbotics/anymal_b_simple_description/blob/988b5df22b84761bdf08111b1c2ccc883793f456/urdf/anymal.urdf#L636) |
| RH_SHANK / com_registered | [-0.4101396, -0.2527506, -0.400905] | unavailable | [-0.371316858, -0.261382771, -0.249106874] | [0.0388227419, -0.00863217071, 0.151798126] | eligible; compared after Kabsch alignment | [CoM/kinematic input L313](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/anybotics_anymal_b/anymal_b.xml#L313) | unavailable | [CoM/kinematic input L665](https://github.com/ANYbotics/anymal_b_simple_description/blob/988b5df22b84761bdf08111b1c2ccc883793f456/urdf/anymal.urdf#L665) |

## Mass accounting

Every contributing compiled body mass is listed here so total/subtree sums can be checked. Links point to explicit inertials or to geometry inputs when the compiler inferred a mass. CoM links identify inertial inputs; world coordinates additionally use the ancestor transforms and the registration recorded below.

| M body | M kg / source | S kg / source | H kg / source |
|---|---|---|---|
| base | 19.2035 / [input L136](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/anybotics_anymal_b/anymal_b.xml#L136) | unavailable | 39.6937927 / [geometry/inference input L13](https://github.com/ANYbotics/anymal_b_simple_description/blob/988b5df22b84761bdf08111b1c2ccc883793f456/urdf/anymal.urdf#L13) |
| LF_HIP | 1.42462 / [input L155](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/anybotics_anymal_b/anymal_b.xml#L155) | unavailable | 1.42462064 / [input L113](https://github.com/ANYbotics/anymal_b_simple_description/blob/988b5df22b84761bdf08111b1c2ccc883793f456/urdf/anymal.urdf#L113) |
| LF_THIGH | 1.63498 / [input L168](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/anybotics_anymal_b/anymal_b.xml#L168) | unavailable | 1.63497647 / [input L157](https://github.com/ANYbotics/anymal_b_simple_description/blob/988b5df22b84761bdf08111b1c2ccc883793f456/urdf/anymal.urdf#L157) |
| LF_SHANK | 0.472163 / [input L181](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/anybotics_anymal_b/anymal_b.xml#L181) | unavailable | 0.207204302 / [input L186](https://github.com/ANYbotics/anymal_b_simple_description/blob/988b5df22b84761bdf08111b1c2ccc883793f456/urdf/anymal.urdf#L186) |
| RF_HIP | 1.42462 / [input L199](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/anybotics_anymal_b/anymal_b.xml#L199) | unavailable | 1.42462064 / [input L273](https://github.com/ANYbotics/anymal_b_simple_description/blob/988b5df22b84761bdf08111b1c2ccc883793f456/urdf/anymal.urdf#L273) |
| RF_THIGH | 1.63498 / [input L212](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/anybotics_anymal_b/anymal_b.xml#L212) | unavailable | 1.63497647 / [input L317](https://github.com/ANYbotics/anymal_b_simple_description/blob/988b5df22b84761bdf08111b1c2ccc883793f456/urdf/anymal.urdf#L317) |
| RF_SHANK | 0.472163 / [input L225](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/anybotics_anymal_b/anymal_b.xml#L225) | unavailable | 0.207204302 / [input L346](https://github.com/ANYbotics/anymal_b_simple_description/blob/988b5df22b84761bdf08111b1c2ccc883793f456/urdf/anymal.urdf#L346) |
| LH_HIP | 1.42462 / [input L243](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/anybotics_anymal_b/anymal_b.xml#L243) | unavailable | 1.42462064 / [input L433](https://github.com/ANYbotics/anymal_b_simple_description/blob/988b5df22b84761bdf08111b1c2ccc883793f456/urdf/anymal.urdf#L433) |
| LH_THIGH | 1.63498 / [input L256](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/anybotics_anymal_b/anymal_b.xml#L256) | unavailable | 1.63497647 / [input L477](https://github.com/ANYbotics/anymal_b_simple_description/blob/988b5df22b84761bdf08111b1c2ccc883793f456/urdf/anymal.urdf#L477) |
| LH_SHANK | 0.472163 / [input L269](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/anybotics_anymal_b/anymal_b.xml#L269) | unavailable | 0.207204302 / [input L506](https://github.com/ANYbotics/anymal_b_simple_description/blob/988b5df22b84761bdf08111b1c2ccc883793f456/urdf/anymal.urdf#L506) |
| RH_HIP | 1.42462 / [input L287](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/anybotics_anymal_b/anymal_b.xml#L287) | unavailable | 1.42462064 / [input L593](https://github.com/ANYbotics/anymal_b_simple_description/blob/988b5df22b84761bdf08111b1c2ccc883793f456/urdf/anymal.urdf#L593) |
| RH_THIGH | 1.63498 / [input L300](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/anybotics_anymal_b/anymal_b.xml#L300) | unavailable | 1.63497647 / [input L637](https://github.com/ANYbotics/anymal_b_simple_description/blob/988b5df22b84761bdf08111b1c2ccc883793f456/urdf/anymal.urdf#L637) |
| RH_SHANK | 0.472163 / [input L313](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/anybotics_anymal_b/anymal_b.xml#L313) | unavailable | 0.207204302 / [input L666](https://github.com/ANYbotics/anymal_b_simple_description/blob/988b5df22b84761bdf08111b1c2ccc883793f456/urdf/anymal.urdf#L666) |
| upstream-only LF_ADAPTER | unavailable | unavailable | 0.140170767 / [input L223](https://github.com/ANYbotics/anymal_b_simple_description/blob/988b5df22b84761bdf08111b1c2ccc883793f456/urdf/anymal.urdf#L223) |
| upstream-only LF_FOOT | unavailable | unavailable | 0.124788249 / [geometry/inference input L234](https://github.com/ANYbotics/anymal_b_simple_description/blob/988b5df22b84761bdf08111b1c2ccc883793f456/urdf/anymal.urdf#L234) |
| upstream-only LH_ADAPTER | unavailable | unavailable | 0.140170767 / [input L543](https://github.com/ANYbotics/anymal_b_simple_description/blob/988b5df22b84761bdf08111b1c2ccc883793f456/urdf/anymal.urdf#L543) |
| upstream-only LH_FOOT | unavailable | unavailable | 0.124788249 / [geometry/inference input L554](https://github.com/ANYbotics/anymal_b_simple_description/blob/988b5df22b84761bdf08111b1c2ccc883793f456/urdf/anymal.urdf#L554) |
| upstream-only RF_ADAPTER | unavailable | unavailable | 0.140170767 / [input L383](https://github.com/ANYbotics/anymal_b_simple_description/blob/988b5df22b84761bdf08111b1c2ccc883793f456/urdf/anymal.urdf#L383) |
| upstream-only RF_FOOT | unavailable | unavailable | 0.124788249 / [geometry/inference input L394](https://github.com/ANYbotics/anymal_b_simple_description/blob/988b5df22b84761bdf08111b1c2ccc883793f456/urdf/anymal.urdf#L394) |
| upstream-only RH_ADAPTER | unavailable | unavailable | 0.140170767 / [input L703](https://github.com/ANYbotics/anymal_b_simple_description/blob/988b5df22b84761bdf08111b1c2ccc883793f456/urdf/anymal.urdf#L703) |
| upstream-only RH_FOOT | unavailable | unavailable | 0.124788249 / [geometry/inference input L714](https://github.com/ANYbotics/anymal_b_simple_description/blob/988b5df22b84761bdf08111b1c2ccc883793f456/urdf/anymal.urdf#L714) |
| upstream-only base_inertia | unavailable | unavailable | 16.7935078 / [input L85](https://github.com/ANYbotics/anymal_b_simple_description/blob/988b5df22b84761bdf08111b1c2ccc883793f456/urdf/anymal.urdf#L85) |

## Coverage and unmatched elements

```json
{
  "mapping_h": {
    "bodies": {
      "base": "base",
      "LF_HIP": "LF_HIP",
      "LF_THIGH": "LF_THIGH",
      "LF_SHANK": "LF_SHANK",
      "RF_HIP": "RF_HIP",
      "RF_THIGH": "RF_THIGH",
      "RF_SHANK": "RF_SHANK",
      "LH_HIP": "LH_HIP",
      "LH_THIGH": "LH_THIGH",
      "LH_SHANK": "LH_SHANK",
      "RH_HIP": "RH_HIP",
      "RH_THIGH": "RH_THIGH",
      "RH_SHANK": "RH_SHANK"
    },
    "joints": {
      "LF_HAA": "LF_HAA",
      "LF_HFE": "LF_HFE",
      "LF_KFE": "LF_KFE",
      "RF_HAA": "RF_HAA",
      "RF_HFE": "RF_HFE",
      "RF_KFE": "RF_KFE",
      "LH_HAA": "LH_HAA",
      "LH_HFE": "LH_HFE",
      "LH_KFE": "LH_KFE",
      "RH_HAA": "RH_HAA",
      "RH_HFE": "RH_HFE",
      "RH_KFE": "RH_KFE"
    },
    "body_methods": {
      "base": "name",
      "LF_HIP": "name",
      "LF_THIGH": "name",
      "LF_SHANK": "name",
      "RF_HIP": "name",
      "RF_THIGH": "name",
      "RF_SHANK": "name",
      "LH_HIP": "name",
      "LH_THIGH": "name",
      "LH_SHANK": "name",
      "RH_HIP": "name",
      "RH_THIGH": "name",
      "RH_SHANK": "name"
    },
    "joint_methods": {
      "LF_HAA": "name",
      "LF_HFE": "name",
      "LF_KFE": "name",
      "RF_HAA": "name",
      "RF_HFE": "name",
      "RF_KFE": "name",
      "LH_HAA": "name",
      "LH_HFE": "name",
      "LH_KFE": "name",
      "RH_HAA": "name",
      "RH_HFE": "name",
      "RH_KFE": "name"
    },
    "unmatched_m_bodies": [],
    "unmatched_upstream_bodies": [
      "LF_ADAPTER",
      "LF_FOOT",
      "LH_ADAPTER",
      "LH_FOOT",
      "RF_ADAPTER",
      "RF_FOOT",
      "RH_ADAPTER",
      "RH_FOOT",
      "base_inertia"
    ],
    "unmatched_m_joints": [],
    "unmatched_upstream_joints": [],
    "registration_anchor": {
      "M": "base",
      "H": "base",
      "root_unmatched": false
    }
  },
  "mapping_s": null,
  "unavailable": [
    {
      "entity": "LF_HAA",
      "other_entity": "LF_HAA",
      "quantity": "range",
      "tolerance": "range",
      "m": null,
      "other": [
        -9.42,
        9.42
      ],
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "LF_HAA",
      "other_entity": "LF_HAA",
      "quantity": "force",
      "tolerance": "limit",
      "m": 40.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "LF_HAA",
      "other_entity": "LF_HAA",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 15.0,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "LF_HFE",
      "other_entity": "LF_HFE",
      "quantity": "range",
      "tolerance": "range",
      "m": null,
      "other": [
        -9.42,
        9.42
      ],
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "LF_HFE",
      "other_entity": "LF_HFE",
      "quantity": "force",
      "tolerance": "limit",
      "m": 40.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "LF_HFE",
      "other_entity": "LF_HFE",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 15.0,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "LF_KFE",
      "other_entity": "LF_KFE",
      "quantity": "range",
      "tolerance": "range",
      "m": null,
      "other": [
        -9.42,
        9.42
      ],
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "LF_KFE",
      "other_entity": "LF_KFE",
      "quantity": "force",
      "tolerance": "limit",
      "m": 40.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "LF_KFE",
      "other_entity": "LF_KFE",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 15.0,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "RF_HAA",
      "other_entity": "RF_HAA",
      "quantity": "range",
      "tolerance": "range",
      "m": null,
      "other": [
        -9.42,
        9.42
      ],
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "RF_HAA",
      "other_entity": "RF_HAA",
      "quantity": "force",
      "tolerance": "limit",
      "m": 40.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "RF_HAA",
      "other_entity": "RF_HAA",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 15.0,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "RF_HFE",
      "other_entity": "RF_HFE",
      "quantity": "range",
      "tolerance": "range",
      "m": null,
      "other": [
        -9.42,
        9.42
      ],
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "RF_HFE",
      "other_entity": "RF_HFE",
      "quantity": "force",
      "tolerance": "limit",
      "m": 40.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "RF_HFE",
      "other_entity": "RF_HFE",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 15.0,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "RF_KFE",
      "other_entity": "RF_KFE",
      "quantity": "range",
      "tolerance": "range",
      "m": null,
      "other": [
        -9.42,
        9.42
      ],
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "RF_KFE",
      "other_entity": "RF_KFE",
      "quantity": "force",
      "tolerance": "limit",
      "m": 40.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "RF_KFE",
      "other_entity": "RF_KFE",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 15.0,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "LH_HAA",
      "other_entity": "LH_HAA",
      "quantity": "range",
      "tolerance": "range",
      "m": null,
      "other": [
        -9.42,
        9.42
      ],
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "LH_HAA",
      "other_entity": "LH_HAA",
      "quantity": "force",
      "tolerance": "limit",
      "m": 40.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "LH_HAA",
      "other_entity": "LH_HAA",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 15.0,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "LH_HFE",
      "other_entity": "LH_HFE",
      "quantity": "range",
      "tolerance": "range",
      "m": null,
      "other": [
        -9.42,
        9.42
      ],
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "LH_HFE",
      "other_entity": "LH_HFE",
      "quantity": "force",
      "tolerance": "limit",
      "m": 40.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "LH_HFE",
      "other_entity": "LH_HFE",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 15.0,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "LH_KFE",
      "other_entity": "LH_KFE",
      "quantity": "range",
      "tolerance": "range",
      "m": null,
      "other": [
        -9.42,
        9.42
      ],
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "LH_KFE",
      "other_entity": "LH_KFE",
      "quantity": "force",
      "tolerance": "limit",
      "m": 40.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "LH_KFE",
      "other_entity": "LH_KFE",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 15.0,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "RH_HAA",
      "other_entity": "RH_HAA",
      "quantity": "range",
      "tolerance": "range",
      "m": null,
      "other": [
        -9.42,
        9.42
      ],
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "RH_HAA",
      "other_entity": "RH_HAA",
      "quantity": "force",
      "tolerance": "limit",
      "m": 40.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "RH_HAA",
      "other_entity": "RH_HAA",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 15.0,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "RH_HFE",
      "other_entity": "RH_HFE",
      "quantity": "range",
      "tolerance": "range",
      "m": null,
      "other": [
        -9.42,
        9.42
      ],
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "RH_HFE",
      "other_entity": "RH_HFE",
      "quantity": "force",
      "tolerance": "limit",
      "m": 40.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "RH_HFE",
      "other_entity": "RH_HFE",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 15.0,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "RH_KFE",
      "other_entity": "RH_KFE",
      "quantity": "range",
      "tolerance": "range",
      "m": null,
      "other": [
        -9.42,
        9.42
      ],
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "RH_KFE",
      "other_entity": "RH_KFE",
      "quantity": "force",
      "tolerance": "limit",
      "m": 40.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "RH_KFE",
      "other_entity": "RH_KFE",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 15.0,
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
| LF_HAA / force | 40 | unavailable | unavailable |
| LF_HAA / velocity | unavailable | unavailable | 15 |
| LF_HFE / force | 40 | unavailable | unavailable |
| LF_HFE / velocity | unavailable | unavailable | 15 |
| LF_KFE / force | 40 | unavailable | unavailable |
| LF_KFE / velocity | unavailable | unavailable | 15 |
| RF_HAA / force | 40 | unavailable | unavailable |
| RF_HAA / velocity | unavailable | unavailable | 15 |
| RF_HFE / force | 40 | unavailable | unavailable |
| RF_HFE / velocity | unavailable | unavailable | 15 |
| RF_KFE / force | 40 | unavailable | unavailable |
| RF_KFE / velocity | unavailable | unavailable | 15 |
| LH_HAA / force | 40 | unavailable | unavailable |
| LH_HAA / velocity | unavailable | unavailable | 15 |
| LH_HFE / force | 40 | unavailable | unavailable |
| LH_HFE / velocity | unavailable | unavailable | 15 |
| LH_KFE / force | 40 | unavailable | unavailable |
| LH_KFE / velocity | unavailable | unavailable | 15 |
| RH_HAA / force | 40 | unavailable | unavailable |
| RH_HAA / velocity | unavailable | unavailable | 15 |
| RH_HFE / force | 40 | unavailable | unavailable |
| RH_HFE / velocity | unavailable | unavailable | 15 |
| RH_KFE / force | 40 | unavailable | unavailable |
| RH_KFE / velocity | unavailable | unavailable | 15 |
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
  "meshes/anymal_base.dae",
  "meshes/anymal_foot.dae",
  "meshes/anymal_hip_l.dae",
  "meshes/anymal_hip_r.dae",
  "meshes/anymal_shank_l.dae",
  "meshes/anymal_shank_r.dae",
  "meshes/anymal_thigh_l.dae",
  "meshes/anymal_thigh_r.dae",
  "urdf/anymal.urdf"
]
```

## Self comparisons

```json
[
  {
    "file": "anybotics_anymal_b/anymal_b.xml",
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
      "NO MATCHING SOURCE": 30
    },
    "classifications_changed": 0,
    "finding_membership_changes": 0
  },
  "2": {
    "provenance_method": "none",
    "counts": {
      "NO MATCHING SOURCE": 30
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
      "anybotics_anymal_b/anymal_b.xml"
    ],
    "registration": {
      "translation": [
        0.0,
        0.0,
        0.58
      ],
      "rotation": [
        [
          -1.0,
          0.0,
          0.0
        ],
        [
          0.0,
          -1.0,
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
      "base",
      "LF_FOOT",
      "RF_FOOT",
      "LH_FOOT",
      "RH_FOOT"
    ],
    "assets_loaded": 17,
    "mesh_conversions": [
      {
        "file": "meshes/anymal_base.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "meshes/anymal_hip_l.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "meshes/anymal_thigh_l.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "meshes/anymal_shank_l.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "meshes/anymal_foot.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "meshes/anymal_hip_r.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "meshes/anymal_thigh_r.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "meshes/anymal_shank_r.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "meshes/anymal_foot.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "meshes/anymal_hip_r.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "meshes/anymal_thigh_r.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "meshes/anymal_shank_r.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "meshes/anymal_foot.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "meshes/anymal_hip_l.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "meshes/anymal_thigh_l.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "meshes/anymal_shank_l.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "meshes/anymal_foot.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      }
    ],
    "nonphysical_normalizations": [],
    "xacro_arguments": {},
    "source_dependencies": [
      "urdf/anymal.urdf",
      "meshes/anymal_base.dae",
      "meshes/anymal_hip_l.dae",
      "meshes/anymal_thigh_l.dae",
      "meshes/anymal_shank_l.dae",
      "meshes/anymal_foot.dae",
      "meshes/anymal_hip_r.dae",
      "meshes/anymal_thigh_r.dae",
      "meshes/anymal_shank_r.dae",
      "meshes/anymal_foot.dae",
      "meshes/anymal_hip_r.dae",
      "meshes/anymal_thigh_r.dae",
      "meshes/anymal_shank_r.dae",
      "meshes/anymal_foot.dae",
      "meshes/anymal_hip_l.dae",
      "meshes/anymal_thigh_l.dae",
      "meshes/anymal_shank_l.dae",
      "meshes/anymal_foot.dae"
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
  "historical_snapshots_reused": 1,
  "primary_physics_unchanged": true,
  "source_matching": "original raw-value provenance criteria retained; kinematic guard applies to reported CoM"
}
```
