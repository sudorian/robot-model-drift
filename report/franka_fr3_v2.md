# franka_fr3_v2

Status: **partial history**. Provenance: **unknown**, confidence **incomplete**.

Unresolved historical compilation prevents selecting or rejecting a matching source. Pairwise M/H differences are reported with unknown provenance.

M: `https://github.com/google-deepmind/mujoco_menagerie`, `franka_fr3_v2/fr3v2.xml`, commit `370c43965323c0944b433b202aac5058b5f907a9`.
H: `https://github.com/frankaemika/franka_description`, `robots/fr3v2/fr3v2.urdf.xacro`, commit `7aeeddc449edf8d62b594f9e36a81da53e7796f9`.
S: unavailable. A machine-readable H can still be compared to M; no-match differences are never counted as STALE.

Limit semantics: MJCF effort values are supported actuator torque/force envelopes. URDF effort and velocity values are manufacturer declarations retained from XML; MuJoCo does not enforce those tags. Such declaration comparisons are explicitly distinct from compiled inertial/range quantities.


## Source evidence

```json
[
  {
    "url": "https://github.com/frankaemika/franka_description",
    "document": "franka_fr3_v2/README.md",
    "commit": "370c43965323c0944b433b202aac5058b5f907a9",
    "current": true
  },
  {
    "url": "https://github.com/frankaemika/franka_description/blob/main/scripts/create_urdf.sh",
    "document": "franka_fr3_v2/README.md",
    "commit": "370c43965323c0944b433b202aac5058b5f907a9",
    "current": true
  },
  {
    "url": "https://github.com/kevinzakka/obj2mjcf",
    "document": "franka_fr3_v2/README.md",
    "commit": "370c43965323c0944b433b202aac5058b5f907a9",
    "current": true
  }
]
```


## README derivation evidence

Documentation labels are conservative: an automated documented label requires an explicit affected entity and quantity. Broader conversion notes are retained here for review.

> 4. Added `<mujoco> <compiler discardvisual="true" strippath="false" fusestatic="false" balanceinertia="true"/> </mujoco>` to the URDF's `<robot>` clause.

## Kinematics consistency

A proper Kabsch rigid transform aligns all matched zero-pose body origins. The maximum per-origin residual and signed hinge/slide axis angles determine whether CoM can be compared; RMS is also recorded. Fewer than three non-collinear origins give insufficient kinematic coverage. CoM records that fail either required M/H or M/S check are excluded from counts and largest discrepancies. Masses, principal moments and raw joint ranges remain unchanged; a flagged range still requires convention review.

| Pair | Status | Origins / rank | RMS / maximum mm | Disagreeing / checked axes |
|---|---|---:|---:|---:|
| M/H | consistent | 10 / 2 | 1.68415271e-13 / 2.31046543e-13 | 0 / 7 |

Exact fitted transforms, per-origin residuals, thresholds and axis vectors:

```json
{
  "M/H": {
    "status": "consistent",
    "matched_body_origins": 10,
    "position_threshold_m": 0.005,
    "axis_threshold_rad": 0.005,
    "residual_definition": "maximum Euclidean residual over matched body origins; Kabsch minimizes RMS, which is also recorded",
    "coordinate_frames": "each snapshot registered to its matched report anchor",
    "anchor_m": "base",
    "anchor_other": "base",
    "rotation_other_to_m": [
      [
        1.0000000000000002,
        7.653249761626894e-16,
        -5.1489591510474055e-17
      ],
      [
        -7.653249761626893e-16,
        1.0,
        5.0589926663629503e-17
      ],
      [
        3.3306690738754696e-16,
        -5.0589926663629454e-17,
        1.0000000000000002
      ]
    ],
    "translation_other_to_m": [
      1.3877787807814457e-17,
      -5.990491664700776e-17,
      -1.1102230246251565e-16
    ],
    "rms_residual_m": 1.684152708130685e-16,
    "max_residual_m": 2.3104654278758763e-16,
    "fit_rank": 2,
    "axis_checks": [
      {
        "joint_m": "fr3v2_joint1",
        "joint_other": "fr3v2_joint1",
        "axis_m": [
          0.0,
          0.0,
          1.0
        ],
        "axis_other_aligned": [
          -5.148959151047404e-17,
          5.058992666362949e-17,
          1.0
        ],
        "angle_rad": 7.218392282043759e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "fr3v2_joint2",
        "joint_other": "fr3v2_joint2",
        "axis_m": [
          0.0,
          1.0,
          2.2204460492503136e-16
        ],
        "axis_other_aligned": [
          7.653249761626894e-16,
          1.0,
          -4.946791365136922e-16
        ],
        "angle_rad": 1.0485300380439006e-15,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "fr3v2_joint3",
        "joint_other": "fr3v2_joint3",
        "axis_m": [
          0.0,
          -4.474228634151475e-17,
          1.0
        ],
        "axis_other_aligned": [
          -5.1489591510474025e-17,
          7.088299937876859e-17,
          1.0
        ],
        "angle_rad": 1.2657165848566824e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "fr3v2_joint4",
        "joint_other": "fr3v2_joint4",
        "axis_m": [
          0.0,
          -1.0,
          4.440892098500629e-16
        ],
        "axis_other_aligned": [
          -7.653249761626894e-16,
          -1.0,
          -3.9349928318643325e-16
        ],
        "angle_rad": 1.134582215093102e-15,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "fr3v2_joint5",
        "joint_other": "fr3v2_joint5",
        "axis_m": [
          0.0,
          -1.582539029327245e-16,
          1.0
        ],
        "axis_other_aligned": [
          -5.148959151047406e-17,
          3.0296853948490395e-17,
          1.0
        ],
        "angle_rad": 1.954547670290865e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "fr3v2_joint6",
        "joint_other": "fr3v2_joint6",
        "axis_m": [
          0.0,
          -1.0,
          7.771561172376104e-16
        ],
        "axis_other_aligned": [
          -7.653249761626894e-16,
          -1.0,
          -3.9349928318643325e-16
        ],
        "angle_rad": 1.3986266069542645e-15,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "fr3v2_joint7",
        "joint_other": "fr3v2_joint7",
        "axis_m": [
          0.0,
          2.0424084633858673e-16,
          -1.0
        ],
        "axis_other_aligned": [
          5.148959151047476e-17,
          8.848200935067045e-16,
          -1.0
        ],
        "angle_rad": 6.825242044864325e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      }
    ],
    "axis_disagreements": [],
    "com_eligible": true,
    "covariance_singular_values": [
      1.5394301221792648,
      0.012292802820735175,
      2.465190328815662e-32
    ],
    "origin_residuals_m": {
      "base": 1.2691392231351918e-16,
      "fr3v2_link0": 1.2691392231351918e-16,
      "fr3v2_link1": 7.032923485102898e-17,
      "fr3v2_link2": 7.032923485102898e-17,
      "fr3v2_link3": 1.149331512947231e-16,
      "fr3v2_link4": 1.287298945331882e-16,
      "fr3v2_link5": 2.2981369403245634e-16,
      "fr3v2_link6": 2.2981369403245634e-16,
      "fr3v2_link7": 2.296478971166094e-16,
      "fr3v2_link8": 2.3104654278758763e-16
    },
    "reason": "Unique proper rigid fit and matched signed axes meet the configured thresholds"
  }
}
```


## Every reported quantity difference

Counts are quantity records, including correlated total/subtree/body mass records; they are not independent robot defects.

| Entity / quantity | M | S | H | H − M | Class | M source | S source | H source |
|---|---|---|---|---|---|---|---|---|
| robot / total_mass | 17.312176 | unavailable | 16.620422 | -0.691754 | unknown | [aggregate inputs](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/franka_fr3_v2/fr3v2.xml#L1) | unavailable | [aggregate inputs](https://github.com/frankaemika/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/fr3v2/fr3v2.urdf.xacro#L1) |
| robot / total_com_registered | [0.0182406288, 0.00784706018, 0.552066344] | unavailable | [0.0228851457, 0.0073758005, 0.613326339] | [0.00464451685, -0.000471259679, 0.0612599948] | unknown | [aggregate inputs](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/franka_fr3_v2/fr3v2.xml#L1) | unavailable | [aggregate inputs](https://github.com/frankaemika/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/fr3v2/fr3v2.urdf.xacro#L1) |
| base / subtree_mass | 17.312176 | unavailable | 16.620422 | -0.691754 | unknown | [subtree root L69](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/franka_fr3_v2/fr3v2.xml#L69) | unavailable | [macro declaration L26](https://github.com/frankaemika/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/franka_arm.xacro#L26) |
| fr3v2_link0 / mass | 3.85 | unavailable | 2.3966 | -1.4534 | unknown | [input L79](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/franka_fr3_v2/fr3v2.xml#L79) | unavailable | [macro declaration L17](https://github.com/frankaemika/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L17); [YAML numeric inputs L5](https://github.com/frankaemika/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/fr3v2/inertials.yaml#L5) |
| fr3v2_link0 / subtree_mass | 17.312176 | unavailable | 16.620422 | -0.691754 | unknown | [subtree root L70](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/franka_fr3_v2/fr3v2.xml#L70) | unavailable | [macro declaration L41](https://github.com/frankaemika/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L41) |
| fr3v2_link1 / subtree_mass | 13.462176 | unavailable | 14.223822 | 0.761646 | unknown | [subtree root L80](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/franka_fr3_v2/fr3v2.xml#L80) | unavailable | [macro declaration L41](https://github.com/frankaemika/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L41) |
| fr3v2_link2 / subtree_mass | 11.024476 | unavailable | 11.786122 | 0.761646 | unknown | [subtree root L87](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/franka_fr3_v2/fr3v2.xml#L87) | unavailable | [macro declaration L41](https://github.com/frankaemika/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L41) |
| fr3v2_link2 / com_registered | [-0.003473, -0.010479, 0.501509] | unavailable | [0.004541, -0.010479, 0.513691] | [0.008014, 3.98986399e-17, 0.012182] | unknown | [CoM/kinematic input L89](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/franka_fr3_v2/fr3v2.xml#L89) | unavailable | [macro declaration L16](https://github.com/frankaemika/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L16); [YAML numeric inputs L27](https://github.com/frankaemika/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/fr3v2/inertials.yaml#L27) |
| fr3v2_link3 / subtree_mass | 8.786976 | unavailable | 9.548622 | 0.761646 | unknown | [subtree root L94](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/franka_fr3_v2/fr3v2.xml#L94) | unavailable | [macro declaration L41](https://github.com/frankaemika/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L41) |
| fr3v2_link3 / com_registered | [0.092968, 0.01801, 0.682533] | unavailable | [0.08254, 0.019082, 0.691027] | [-0.010428, 0.001072, 0.008494] | unknown | [CoM/kinematic input L96](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/franka_fr3_v2/fr3v2.xml#L96) | unavailable | [macro declaration L16](https://github.com/frankaemika/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L16); [YAML numeric inputs L39](https://github.com/frankaemika/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/fr3v2/inertials.yaml#L39) |
| fr3v2_link4 / subtree_mass | 6.601186 | unavailable | 7.35554 | 0.754354 | unknown | [subtree root L101](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/franka_fr3_v2/fr3v2.xml#L101) | unavailable | [macro declaration L41](https://github.com/frankaemika/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L41) |
| fr3v2_link4 / com_registered | [0.013755, -0.011195, 0.741947] | unavailable | [-0.005033, -0.01012, 0.745335] | [-0.018788, 0.001075, 0.003388] | unknown | [CoM/kinematic input L103](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/franka_fr3_v2/fr3v2.xml#L103) | unavailable | [macro declaration L16](https://github.com/frankaemika/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L16); [YAML numeric inputs L51](https://github.com/frankaemika/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/fr3v2/inertials.yaml#L51) |
| fr3v2_link5 / mass | 2.17482 | unavailable | 2.186881 | 0.012061 | unknown | [input L110](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/franka_fr3_v2/fr3v2.xml#L110) | unavailable | [macro declaration L17](https://github.com/frankaemika/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L17); [YAML numeric inputs L65](https://github.com/frankaemika/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/fr3v2/inertials.yaml#L65) |
| fr3v2_link5 / subtree_mass | 4.425316 | unavailable | 5.174003 | 0.748687 | unknown | [subtree root L108](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/franka_fr3_v2/fr3v2.xml#L108) | unavailable | [macro declaration L41](https://github.com/frankaemika/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L41) |
| fr3v2_link5 / com_registered | [-0.004197, 0.010257, 0.974897] | unavailable | [0.008383, 0.01018, 0.979735] | [0.01258, -7.7e-05, 0.004838] | unknown | [CoM/kinematic input L110](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/franka_fr3_v2/fr3v2.xml#L110) | unavailable | [macro declaration L16](https://github.com/frankaemika/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L16); [YAML numeric inputs L63](https://github.com/frankaemika/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/fr3v2/inertials.yaml#L63) |
| fr3v2_link6 / mass | 1.56762 | unavailable | 1.579681 | 0.012061 | unknown | [input L117](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/franka_fr3_v2/fr3v2.xml#L117) | unavailable | [macro declaration L17](https://github.com/frankaemika/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L17); [YAML numeric inputs L77](https://github.com/frankaemika/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/fr3v2/inertials.yaml#L77) |
| fr3v2_link6 / subtree_mass | 2.250496 | unavailable | 2.987122 | 0.736626 | unknown | [subtree root L115](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/franka_fr3_v2/fr3v2.xml#L115) | unavailable | [macro declaration L41](https://github.com/frankaemika/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L41) |
| fr3v2_link6 / com_registered | [0.070958, 0.035324, 1.018863] | unavailable | [0.070391, 0.035025, 1.016926] | [-0.000567, -0.000299, -0.001937] | unknown | [CoM/kinematic input L117](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/franka_fr3_v2/fr3v2.xml#L117) | unavailable | [macro declaration L16](https://github.com/frankaemika/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L16); [YAML numeric inputs L75](https://github.com/frankaemika/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/fr3v2/inertials.yaml#L75) |
| fr3v2_link7 / mass | 0.682876 | unavailable | 0.694841 | 0.011965 | unknown | [input L133](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/franka_fr3_v2/fr3v2.xml#L133) | unavailable | [macro declaration L17](https://github.com/frankaemika/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L17); [YAML numeric inputs L89](https://github.com/frankaemika/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/fr3v2/inertials.yaml#L89) |
| fr3v2_link7 / subtree_mass | 0.682876 | unavailable | 1.407441 | 0.724565 | unknown | [subtree root L131](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/franka_fr3_v2/fr3v2.xml#L131) | unavailable | [macro declaration L41](https://github.com/frankaemika/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L41) |
| fr3v2_link7 / com_registered | [0.096204, -0.001156, 0.971984] | unavailable | [0.078892, -0.018151, 0.968054] | [-0.017312, -0.016995, -0.00393] | unknown | [CoM/kinematic input L133](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/franka_fr3_v2/fr3v2.xml#L133) | unavailable | [macro declaration L16](https://github.com/frankaemika/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L16); [YAML numeric inputs L87](https://github.com/frankaemika/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/fr3v2/inertials.yaml#L87) |
| fr3v2_link8 / subtree_mass | 0 | unavailable | 0.7126 | 0.7126 | unknown | [subtree root L144](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/franka_fr3_v2/fr3v2.xml#L144) | unavailable | [subtree root L148](https://github.com/frankaemika/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/franka_arm.xacro#L148) |

## Raw CoM records and reporting decisions

Raw values retain the previous root-anchor registration before Kabsch; original world coordinates also remain in the snapshots. Eligible findings above use the fitted transform into M. Excluded raw records below are diagnostic numbers, not findings. No CoM suppression applies to mass or principal inertia moments.

| Entity / quantity | Raw M | Raw S | Raw H | Raw H − M | Decision | M source | S source | H source |
|---|---|---|---|---|---|---|---|---|
| robot / total_com_registered | [0.0182406288, 0.00784706018, 0.552066344] | unavailable | [0.0228851457, 0.0073758005, 0.613326339] | [0.00464451685, -0.000471259679, 0.0612599948] | eligible; compared after Kabsch alignment | [aggregate inputs](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/franka_fr3_v2/fr3v2.xml#L1) | unavailable | [aggregate inputs](https://github.com/frankaemika/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/fr3v2/fr3v2.urdf.xacro#L1) |
| base / com_registered | [0, 0, 0] | unavailable | [0, 0, 0] | [0, 0, 0] | eligible; compared after Kabsch alignment | [geometry/inference input L69](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/franka_fr3_v2/fr3v2.xml#L69) | unavailable | [macro declaration L26](https://github.com/frankaemika/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/franka_arm.xacro#L26) |
| fr3v2_link0 / com_registered | [-0.0172, 0.0004, 0.0745] | unavailable | [-0.0172, 0.0004, 0.0745] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L79](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/franka_fr3_v2/fr3v2.xml#L79) | unavailable | [macro declaration L16](https://github.com/frankaemika/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L16); [YAML numeric inputs L3](https://github.com/frankaemika/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/fr3v2/inertials.yaml#L3) |
| fr3v2_link1 / com_registered | [-0.00458, 0.027016, 0.2712] | unavailable | [-0.00458, 0.027016, 0.2712] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L82](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/franka_fr3_v2/fr3v2.xml#L82) | unavailable | [macro declaration L16](https://github.com/frankaemika/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L16); [YAML numeric inputs L15](https://github.com/frankaemika/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/fr3v2/inertials.yaml#L15) |
| fr3v2_link2 / com_registered | [-0.003473, -0.010479, 0.501509] | unavailable | [0.004541, -0.010479, 0.513691] | [0.008014, 7.80625564e-17, 0.012182] | eligible; compared after Kabsch alignment | [CoM/kinematic input L89](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/franka_fr3_v2/fr3v2.xml#L89) | unavailable | [macro declaration L16](https://github.com/frankaemika/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L16); [YAML numeric inputs L27](https://github.com/frankaemika/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/fr3v2/inertials.yaml#L27) |
| fr3v2_link3 / com_registered | [0.092968, 0.01801, 0.682533] | unavailable | [0.08254, 0.019082, 0.691027] | [-0.010428, 0.001072, 0.008494] | eligible; compared after Kabsch alignment | [CoM/kinematic input L96](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/franka_fr3_v2/fr3v2.xml#L96) | unavailable | [macro declaration L16](https://github.com/frankaemika/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L16); [YAML numeric inputs L39](https://github.com/frankaemika/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/fr3v2/inertials.yaml#L39) |
| fr3v2_link4 / com_registered | [0.013755, -0.011195, 0.741947] | unavailable | [-0.005033, -0.01012, 0.745335] | [-0.018788, 0.001075, 0.003388] | eligible; compared after Kabsch alignment | [CoM/kinematic input L103](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/franka_fr3_v2/fr3v2.xml#L103) | unavailable | [macro declaration L16](https://github.com/frankaemika/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L16); [YAML numeric inputs L51](https://github.com/frankaemika/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/fr3v2/inertials.yaml#L51) |
| fr3v2_link5 / com_registered | [-0.004197, 0.010257, 0.974897] | unavailable | [0.008383, 0.01018, 0.979735] | [0.01258, -7.7e-05, 0.004838] | eligible; compared after Kabsch alignment | [CoM/kinematic input L110](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/franka_fr3_v2/fr3v2.xml#L110) | unavailable | [macro declaration L16](https://github.com/frankaemika/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L16); [YAML numeric inputs L63](https://github.com/frankaemika/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/fr3v2/inertials.yaml#L63) |
| fr3v2_link6 / com_registered | [0.070958, 0.035324, 1.018863] | unavailable | [0.070391, 0.035025, 1.016926] | [-0.000567, -0.000299, -0.001937] | eligible; compared after Kabsch alignment | [CoM/kinematic input L117](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/franka_fr3_v2/fr3v2.xml#L117) | unavailable | [macro declaration L16](https://github.com/frankaemika/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L16); [YAML numeric inputs L75](https://github.com/frankaemika/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/fr3v2/inertials.yaml#L75) |
| fr3v2_link7 / com_registered | [0.096204, -0.001156, 0.971984] | unavailable | [0.078892, -0.018151, 0.968054] | [-0.017312, -0.016995, -0.00393] | eligible; compared after Kabsch alignment | [CoM/kinematic input L133](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/franka_fr3_v2/fr3v2.xml#L133) | unavailable | [macro declaration L16](https://github.com/frankaemika/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L16); [YAML numeric inputs L87](https://github.com/frankaemika/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/fr3v2/inertials.yaml#L87) |
| fr3v2_link8 / com_registered | [0.088, -2.02413051e-17, 0.819] | unavailable | [0.088, 1.69979678e-16, 0.819] | [6.9388939e-17, 1.90220983e-16, 0] | eligible; compared after Kabsch alignment | [geometry/inference input L144](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/franka_fr3_v2/fr3v2.xml#L144) | unavailable | [geometry/inference input L148](https://github.com/frankaemika/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/franka_arm.xacro#L148) |

## Mass accounting

Every contributing compiled body mass is listed here so total/subtree sums can be checked. Links point to explicit inertials or to geometry inputs when the compiler inferred a mass. CoM links identify inertial inputs; world coordinates additionally use the ancestor transforms and the registration recorded below.

| M body | M kg / source | S kg / source | H kg / source |
|---|---|---|---|
| base | 0 / [geometry/inference input L69](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/franka_fr3_v2/fr3v2.xml#L69) | unavailable | 0 / [macro declaration L26](https://github.com/frankaemika/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/franka_arm.xacro#L26) |
| fr3v2_link0 | 3.85 / [input L79](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/franka_fr3_v2/fr3v2.xml#L79) | unavailable | 2.3966 / [macro declaration L17](https://github.com/frankaemika/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L17); [YAML numeric inputs L5](https://github.com/frankaemika/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/fr3v2/inertials.yaml#L5) |
| fr3v2_link1 | 2.4377 / [input L82](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/franka_fr3_v2/fr3v2.xml#L82) | unavailable | 2.4377 / [macro declaration L17](https://github.com/frankaemika/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L17); [YAML numeric inputs L17](https://github.com/frankaemika/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/fr3v2/inertials.yaml#L17) |
| fr3v2_link2 | 2.2375 / [input L89](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/franka_fr3_v2/fr3v2.xml#L89) | unavailable | 2.2375 / [macro declaration L17](https://github.com/frankaemika/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L17); [YAML numeric inputs L29](https://github.com/frankaemika/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/fr3v2/inertials.yaml#L29) |
| fr3v2_link3 | 2.18579 / [input L96](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/franka_fr3_v2/fr3v2.xml#L96) | unavailable | 2.193082 / [macro declaration L17](https://github.com/frankaemika/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L17); [YAML numeric inputs L41](https://github.com/frankaemika/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/fr3v2/inertials.yaml#L41) |
| fr3v2_link4 | 2.17587 / [input L103](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/franka_fr3_v2/fr3v2.xml#L103) | unavailable | 2.181537 / [macro declaration L17](https://github.com/frankaemika/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L17); [YAML numeric inputs L53](https://github.com/frankaemika/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/fr3v2/inertials.yaml#L53) |
| fr3v2_link5 | 2.17482 / [input L110](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/franka_fr3_v2/fr3v2.xml#L110) | unavailable | 2.186881 / [macro declaration L17](https://github.com/frankaemika/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L17); [YAML numeric inputs L65](https://github.com/frankaemika/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/fr3v2/inertials.yaml#L65) |
| fr3v2_link6 | 1.56762 / [input L117](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/franka_fr3_v2/fr3v2.xml#L117) | unavailable | 1.579681 / [macro declaration L17](https://github.com/frankaemika/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L17); [YAML numeric inputs L77](https://github.com/frankaemika/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/fr3v2/inertials.yaml#L77) |
| fr3v2_link7 | 0.682876 / [input L133](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/franka_fr3_v2/fr3v2.xml#L133) | unavailable | 0.694841 / [macro declaration L17](https://github.com/frankaemika/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L17); [YAML numeric inputs L89](https://github.com/frankaemika/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/fr3v2/inertials.yaml#L89) |
| fr3v2_link8 | 0 / [geometry/inference input L144](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/franka_fr3_v2/fr3v2.xml#L144) | unavailable | 0 / [geometry/inference input L148](https://github.com/frankaemika/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/franka_arm.xacro#L148) |
| upstream-only fr3v2_hand | unavailable | unavailable | 0.6544 / [geometry/inference input L6](https://github.com/frankaemika/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/end_effectors/franka_hand/franka_hand.srdf.xacro#L6) |
| upstream-only fr3v2_hand_tcp | unavailable | unavailable | 0 / [geometry/inference input L37](https://github.com/frankaemika/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/end_effectors/common/franka_hand.xacro#L37) |
| upstream-only fr3v2_leftfinger | unavailable | unavailable | 0.0291 / [geometry/inference input L43](https://github.com/frankaemika/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/end_effectors/common/franka_hand.xacro#L43) |
| upstream-only fr3v2_link0_accelerometer_bottom | unavailable | unavailable | 0 / [geometry/inference input L204](https://github.com/frankaemika/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L204) |
| upstream-only fr3v2_link0_accelerometer_top | unavailable | unavailable | 0 / [geometry/inference input L195](https://github.com/frankaemika/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L195) |
| upstream-only fr3v2_link1_accelerometer_bottom | unavailable | unavailable | 0 / [geometry/inference input L204](https://github.com/frankaemika/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L204) |
| upstream-only fr3v2_link1_accelerometer_top | unavailable | unavailable | 0 / [geometry/inference input L195](https://github.com/frankaemika/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L195) |
| upstream-only fr3v2_link2_accelerometer_bottom | unavailable | unavailable | 0 / [geometry/inference input L204](https://github.com/frankaemika/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L204) |
| upstream-only fr3v2_link2_accelerometer_top | unavailable | unavailable | 0 / [geometry/inference input L195](https://github.com/frankaemika/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L195) |
| upstream-only fr3v2_link3_accelerometer_bottom | unavailable | unavailable | 0 / [geometry/inference input L204](https://github.com/frankaemika/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L204) |
| upstream-only fr3v2_link3_accelerometer_top | unavailable | unavailable | 0 / [geometry/inference input L195](https://github.com/frankaemika/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L195) |
| upstream-only fr3v2_link4_accelerometer_bottom | unavailable | unavailable | 0 / [geometry/inference input L204](https://github.com/frankaemika/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L204) |
| upstream-only fr3v2_link4_accelerometer_top | unavailable | unavailable | 0 / [geometry/inference input L195](https://github.com/frankaemika/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L195) |
| upstream-only fr3v2_link5_accelerometer_bottom | unavailable | unavailable | 0 / [geometry/inference input L204](https://github.com/frankaemika/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L204) |
| upstream-only fr3v2_link5_accelerometer_top | unavailable | unavailable | 0 / [geometry/inference input L195](https://github.com/frankaemika/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L195) |
| upstream-only fr3v2_rightfinger | unavailable | unavailable | 0.0291 / [geometry/inference input L79](https://github.com/frankaemika/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/end_effectors/common/franka_hand.xacro#L79) |

## Coverage and unmatched elements

```json
{
  "mapping_h": {
    "bodies": {
      "base": "base",
      "fr3v2_link0": "fr3v2_link0",
      "fr3v2_link1": "fr3v2_link1",
      "fr3v2_link2": "fr3v2_link2",
      "fr3v2_link3": "fr3v2_link3",
      "fr3v2_link4": "fr3v2_link4",
      "fr3v2_link5": "fr3v2_link5",
      "fr3v2_link6": "fr3v2_link6",
      "fr3v2_link7": "fr3v2_link7",
      "fr3v2_link8": "fr3v2_link8"
    },
    "joints": {
      "fr3v2_joint1": "fr3v2_joint1",
      "fr3v2_joint2": "fr3v2_joint2",
      "fr3v2_joint3": "fr3v2_joint3",
      "fr3v2_joint4": "fr3v2_joint4",
      "fr3v2_joint5": "fr3v2_joint5",
      "fr3v2_joint6": "fr3v2_joint6",
      "fr3v2_joint7": "fr3v2_joint7"
    },
    "body_methods": {
      "base": "name",
      "fr3v2_link0": "name",
      "fr3v2_link1": "name",
      "fr3v2_link2": "name",
      "fr3v2_link3": "name",
      "fr3v2_link4": "name",
      "fr3v2_link5": "name",
      "fr3v2_link6": "name",
      "fr3v2_link7": "name",
      "fr3v2_link8": "name"
    },
    "joint_methods": {
      "fr3v2_joint1": "name",
      "fr3v2_joint2": "name",
      "fr3v2_joint3": "name",
      "fr3v2_joint4": "name",
      "fr3v2_joint5": "name",
      "fr3v2_joint6": "name",
      "fr3v2_joint7": "name"
    },
    "unmatched_m_bodies": [],
    "unmatched_upstream_bodies": [
      "fr3v2_hand",
      "fr3v2_hand_tcp",
      "fr3v2_leftfinger",
      "fr3v2_link0_accelerometer_bottom",
      "fr3v2_link0_accelerometer_top",
      "fr3v2_link1_accelerometer_bottom",
      "fr3v2_link1_accelerometer_top",
      "fr3v2_link2_accelerometer_bottom",
      "fr3v2_link2_accelerometer_top",
      "fr3v2_link3_accelerometer_bottom",
      "fr3v2_link3_accelerometer_top",
      "fr3v2_link4_accelerometer_bottom",
      "fr3v2_link4_accelerometer_top",
      "fr3v2_link5_accelerometer_bottom",
      "fr3v2_link5_accelerometer_top",
      "fr3v2_rightfinger"
    ],
    "unmatched_m_joints": [],
    "unmatched_upstream_joints": [
      "fr3v2_finger_joint1",
      "fr3v2_finger_joint2"
    ],
    "registration_anchor": {
      "M": "base",
      "H": "base",
      "root_unmatched": false
    }
  },
  "mapping_s": null,
  "unavailable": [
    {
      "entity": "fr3v2_joint1",
      "other_entity": "fr3v2_joint1",
      "quantity": "force",
      "tolerance": "limit",
      "m": 87.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "fr3v2_joint1",
      "other_entity": "fr3v2_joint1",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 2.62,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "fr3v2_joint2",
      "other_entity": "fr3v2_joint2",
      "quantity": "force",
      "tolerance": "limit",
      "m": 87.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "fr3v2_joint2",
      "other_entity": "fr3v2_joint2",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 2.62,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "fr3v2_joint3",
      "other_entity": "fr3v2_joint3",
      "quantity": "force",
      "tolerance": "limit",
      "m": 87.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "fr3v2_joint3",
      "other_entity": "fr3v2_joint3",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 2.62,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "fr3v2_joint4",
      "other_entity": "fr3v2_joint4",
      "quantity": "force",
      "tolerance": "limit",
      "m": 87.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "fr3v2_joint4",
      "other_entity": "fr3v2_joint4",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 2.62,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "fr3v2_joint5",
      "other_entity": "fr3v2_joint5",
      "quantity": "force",
      "tolerance": "limit",
      "m": 12.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "fr3v2_joint5",
      "other_entity": "fr3v2_joint5",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 5.26,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "fr3v2_joint6",
      "other_entity": "fr3v2_joint6",
      "quantity": "force",
      "tolerance": "limit",
      "m": 12.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "fr3v2_joint6",
      "other_entity": "fr3v2_joint6",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 4.18,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "fr3v2_joint7",
      "other_entity": "fr3v2_joint7",
      "quantity": "force",
      "tolerance": "limit",
      "m": 12.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "fr3v2_joint7",
      "other_entity": "fr3v2_joint7",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 5.26,
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
| fr3v2_joint1 / force | 87 | unavailable | unavailable |
| fr3v2_joint1 / velocity | unavailable | unavailable | 2.62 |
| fr3v2_joint2 / force | 87 | unavailable | unavailable |
| fr3v2_joint2 / velocity | unavailable | unavailable | 2.62 |
| fr3v2_joint3 / force | 87 | unavailable | unavailable |
| fr3v2_joint3 / velocity | unavailable | unavailable | 2.62 |
| fr3v2_joint4 / force | 87 | unavailable | unavailable |
| fr3v2_joint4 / velocity | unavailable | unavailable | 2.62 |
| fr3v2_joint5 / force | 12 | unavailable | unavailable |
| fr3v2_joint5 / velocity | unavailable | unavailable | 5.26 |
| fr3v2_joint6 / force | 12 | unavailable | unavailable |
| fr3v2_joint6 / velocity | unavailable | unavailable | 4.18 |
| fr3v2_joint7 / force | 12 | unavailable | unavailable |
| fr3v2_joint7 / velocity | unavailable | unavailable | 5.26 |
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
  "end_effectors/common/franka_hand.xacro",
  "end_effectors/common/utils.xacro",
  "end_effectors/franka_hand/franka_hand_arguments.xacro",
  "end_effectors/franka_hand/inertials.yaml",
  "meshes/robot_arms/fr3v2/collision/link0.stl",
  "meshes/robot_arms/fr3v2/collision/link1.stl",
  "meshes/robot_arms/fr3v2/collision/link2.stl",
  "meshes/robot_arms/fr3v2/collision/link3.stl",
  "meshes/robot_arms/fr3v2/collision/link4.stl",
  "meshes/robot_arms/fr3v2/collision/link5.stl",
  "meshes/robot_arms/fr3v2/collision/link6.stl",
  "meshes/robot_arms/fr3v2/collision/link7.stl",
  "meshes/robot_arms/fr3v2/visual/link0.dae",
  "meshes/robot_arms/fr3v2/visual/link1.dae",
  "meshes/robot_arms/fr3v2/visual/link2.dae",
  "meshes/robot_arms/fr3v2/visual/link3.dae",
  "meshes/robot_arms/fr3v2/visual/link4.dae",
  "meshes/robot_arms/fr3v2/visual/link5.dae",
  "meshes/robot_arms/fr3v2/visual/link6.dae",
  "meshes/robot_arms/fr3v2/visual/link7.dae",
  "meshes/robot_ee/franka_hand_white/collision/hand.stl",
  "meshes/robot_ee/franka_hand_white/visual/finger.dae",
  "meshes/robot_ee/franka_hand_white/visual/hand.dae",
  "meshes/robots/fr3v2/collision/link0.stl",
  "meshes/robots/fr3v2/collision/link1.stl",
  "meshes/robots/fr3v2/collision/link2.stl",
  "meshes/robots/fr3v2/collision/link3.stl",
  "meshes/robots/fr3v2/collision/link4.stl",
  "meshes/robots/fr3v2/collision/link5.stl",
  "meshes/robots/fr3v2/collision/link6.stl",
  "meshes/robots/fr3v2/collision/link7.stl",
  "meshes/robots/fr3v2/visual/link0.dae",
  "meshes/robots/fr3v2/visual/link1.dae",
  "meshes/robots/fr3v2/visual/link2.dae",
  "meshes/robots/fr3v2/visual/link3.dae",
  "meshes/robots/fr3v2/visual/link4.dae",
  "meshes/robots/fr3v2/visual/link5.dae",
  "meshes/robots/fr3v2/visual/link6.dae",
  "meshes/robots/fr3v2/visual/link7.dae",
  "robots/common/franka_arm.xacro",
  "robots/common/franka_robot.xacro",
  "robots/common/utils.xacro",
  "robots/fr3v2/accelerometers.yaml",
  "robots/fr3v2/dynamics.yaml",
  "robots/fr3v2/fr3v2.urdf.xacro",
  "robots/fr3v2/inertials.yaml",
  "robots/fr3v2/joint_limits.yaml",
  "robots/fr3v2/kinematics.yaml"
]
```

## Self comparisons

```json
[
  {
    "file": "franka_fr3_v2/fr3v2.xml",
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
      "unknown": 24
    },
    "classifications_changed": 0,
    "finding_membership_changes": 2
  },
  "2": {
    "provenance_method": "unknown",
    "counts": {
      "unknown": 20
    },
    "classifications_changed": 0,
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
      "base",
      "fr3v2_link8"
    ],
    "assets_loaded": 37,
    "mesh_conversions": [],
    "nonphysical_normalizations": [],
    "xacro_arguments": {},
    "source_dependencies": [
      "franka_fr3_v2/fr3v2.xml",
      "franka_fr3_v2/assets/link0_0.obj",
      "franka_fr3_v2/assets/link0_1.obj",
      "franka_fr3_v2/assets/link0_2.obj",
      "franka_fr3_v2/assets/link0_3.obj",
      "franka_fr3_v2/assets/link0_4.obj",
      "franka_fr3_v2/assets/link0_5.obj",
      "franka_fr3_v2/assets/link1_3.obj",
      "franka_fr3_v2/assets/link2_3.obj",
      "franka_fr3_v2/assets/link3_3.obj",
      "franka_fr3_v2/assets/link4_3.obj",
      "franka_fr3_v2/assets/link5_3.obj",
      "franka_fr3_v2/assets/link5_4.obj",
      "franka_fr3_v2/assets/link6_0.obj",
      "franka_fr3_v2/assets/link6_1.obj",
      "franka_fr3_v2/assets/link6_2.obj",
      "franka_fr3_v2/assets/link6_3.obj",
      "franka_fr3_v2/assets/link6_4.obj",
      "franka_fr3_v2/assets/link6_5.obj",
      "franka_fr3_v2/assets/link6_6.obj",
      "franka_fr3_v2/assets/link6_7.obj",
      "franka_fr3_v2/assets/link6_8.obj",
      "franka_fr3_v2/assets/link6_9.obj",
      "franka_fr3_v2/assets/link7_0.obj",
      "franka_fr3_v2/assets/link7_1.obj",
      "franka_fr3_v2/assets/link7_2.obj",
      "franka_fr3_v2/assets/link7_3.obj",
      "franka_fr3_v2/assets/link7_4.obj",
      "franka_fr3_v2/assets/link7_5.obj",
      "franka_fr3_v2/assets/link7_6.obj",
      "franka_fr3_v2/assets/link0.stl",
      "franka_fr3_v2/assets/link1.stl",
      "franka_fr3_v2/assets/link2.stl",
      "franka_fr3_v2/assets/link3.stl",
      "franka_fr3_v2/assets/link4.stl",
      "franka_fr3_v2/assets/link5.stl",
      "franka_fr3_v2/assets/link6.stl",
      "franka_fr3_v2/assets/link7.stl"
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
      "base",
      "fr3v2_link0_accelerometer_top",
      "fr3v2_link0_accelerometer_bottom",
      "fr3v2_link1_accelerometer_top",
      "fr3v2_link1_accelerometer_bottom",
      "fr3v2_link2_accelerometer_top",
      "fr3v2_link2_accelerometer_bottom",
      "fr3v2_link3_accelerometer_top",
      "fr3v2_link3_accelerometer_bottom",
      "fr3v2_link4_accelerometer_top",
      "fr3v2_link4_accelerometer_bottom",
      "fr3v2_link5_accelerometer_top",
      "fr3v2_link5_accelerometer_bottom",
      "fr3v2_link8",
      "fr3v2_hand_tcp"
    ],
    "assets_loaded": 20,
    "mesh_conversions": [
      {
        "file": "meshes/robots/fr3v2/visual/link0.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "meshes/robots/fr3v2/visual/link1.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "meshes/robots/fr3v2/visual/link2.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "meshes/robots/fr3v2/visual/link3.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "meshes/robots/fr3v2/visual/link4.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "meshes/robots/fr3v2/visual/link5.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "meshes/robots/fr3v2/visual/link6.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "meshes/robots/fr3v2/visual/link7.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "meshes/robot_ee/franka_hand_white/visual/hand.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "meshes/robot_ee/franka_hand_white/visual/finger.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "meshes/robot_ee/franka_hand_white/visual/finger.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      }
    ],
    "nonphysical_normalizations": [],
    "xacro_arguments": {
      "robot_type": "fr3v2",
      "arm_prefix": "",
      "no_prefix": "false",
      "hand": "true",
      "ee_id": "franka_hand",
      "special_connection": "",
      "xyz_ee": "0 0 0",
      "rpy_ee": "0 0 -0.7853981633974483",
      "tcp_xyz": "",
      "tcp_rpy": "0 0 0",
      "safety_distance": "0.03",
      "with_sc": "false",
      "connected_to": "base",
      "include_self_collision_geometry": "true",
      "description_pkg": "franka_description",
      "xyz": "0 0 0",
      "rpy": "0 0 0"
    },
    "source_dependencies": [
      "end_effectors/common/franka_hand.xacro",
      "end_effectors/common/utils.xacro",
      "end_effectors/franka_hand/inertials.yaml",
      "robots/common/franka_arm.xacro",
      "robots/common/franka_robot.xacro",
      "robots/common/utils.xacro",
      "robots/fr3v2/accelerometers.yaml",
      "robots/fr3v2/dynamics.yaml",
      "robots/fr3v2/fr3v2.urdf.xacro",
      "robots/fr3v2/inertials.yaml",
      "robots/fr3v2/joint_limits.yaml",
      "robots/fr3v2/kinematics.yaml",
      "meshes/robots/fr3v2/visual/link0.dae",
      "meshes/robots/fr3v2/collision/link0.stl",
      "meshes/robots/fr3v2/visual/link1.dae",
      "meshes/robots/fr3v2/collision/link1.stl",
      "meshes/robots/fr3v2/visual/link2.dae",
      "meshes/robots/fr3v2/collision/link2.stl",
      "meshes/robots/fr3v2/visual/link3.dae",
      "meshes/robots/fr3v2/collision/link3.stl",
      "meshes/robots/fr3v2/visual/link4.dae",
      "meshes/robots/fr3v2/collision/link4.stl",
      "meshes/robots/fr3v2/visual/link5.dae",
      "meshes/robots/fr3v2/collision/link5.stl",
      "meshes/robots/fr3v2/visual/link6.dae",
      "meshes/robots/fr3v2/collision/link6.stl",
      "meshes/robots/fr3v2/visual/link7.dae",
      "meshes/robots/fr3v2/collision/link7.stl",
      "meshes/robot_ee/franka_hand_white/visual/hand.dae",
      "meshes/robot_ee/franka_hand_white/collision/hand.stl",
      "meshes/robot_ee/franka_hand_white/visual/finger.dae",
      "meshes/robot_ee/franka_hand_white/visual/finger.dae"
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
  "historical_snapshots_reused": 41,
  "primary_physics_unchanged": true,
  "source_matching": "original raw-value provenance criteria retained; kinematic guard applies to reported CoM"
}
```
