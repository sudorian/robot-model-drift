# franka_fr3

Status: **partial history**. Provenance: **unknown**, confidence **incomplete**.

Unresolved historical compilation prevents selecting or rejecting a matching source. Pairwise M/H differences are reported with unknown provenance.

M: `https://github.com/google-deepmind/mujoco_menagerie`, `franka_fr3/fr3.xml`, commit `370c43965323c0944b433b202aac5058b5f907a9`.
H: `https://github.com/frankaemika/franka_description`, `robots/fr3/fr3.urdf.xacro`, commit `7aeeddc449edf8d62b594f9e36a81da53e7796f9`.
S: unavailable. A machine-readable H can still be compared to M; no-match differences are never counted as STALE.

Limit semantics: MJCF effort values are supported actuator torque/force envelopes. URDF effort and velocity values are manufacturer declarations retained from XML; MuJoCo does not enforce those tags. Such declaration comparisons are explicitly distinct from compiled inertial/range quantities.


## Source evidence

```json
[
  {
    "url": "https://github.com/frankaemika/franka_description",
    "document": "franka_fr3/README.md",
    "commit": "370c43965323c0944b433b202aac5058b5f907a9",
    "current": true
  },
  {
    "url": "https://github.com/frankaemika/franka_description/blob/main/scripts/create_urdf.sh",
    "document": "franka_fr3/README.md",
    "commit": "370c43965323c0944b433b202aac5058b5f907a9",
    "current": true
  },
  {
    "url": "https://github.com/kevinzakka/obj2mjcf",
    "document": "franka_fr3/README.md",
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
| M/H | consistent | 9 / 2 | 1.55709177e-13 / 2.30856614e-13 | 0 / 7 |

Exact fitted transforms, per-origin residuals, thresholds and axis vectors:

```json
{
  "M/H": {
    "status": "consistent",
    "matched_body_origins": 9,
    "position_threshold_m": 0.005,
    "axis_threshold_rad": 0.005,
    "residual_definition": "maximum Euclidean residual over matched body origins; Kabsch minimizes RMS, which is also recorded",
    "coordinate_frames": "each snapshot registered to its matched report anchor",
    "anchor_m": "base",
    "anchor_other": "base",
    "rotation_other_to_m": [
      [
        1.0,
        7.554586324970178e-16,
        -8.044945017610867e-17
      ],
      [
        -6.473387518713048e-16,
        1.0,
        4.1392632616450784e-17
      ],
      [
        -1.5959455978986625e-16,
        -6.661252669949299e-17,
        0.9999999999999999
      ]
    ],
    "translation_other_to_m": [
      3.8163916471489756e-17,
      -5.3457373579342974e-17,
      1.1102230246251565e-16
    ],
    "rms_residual_m": 1.557091772158116e-16,
    "max_residual_m": 2.3085661405987017e-16,
    "fit_rank": 2,
    "axis_checks": [
      {
        "joint_m": "fr3_joint1",
        "joint_other": "fr3_joint1",
        "axis_m": [
          0.0,
          0.0,
          1.0
        ],
        "axis_other_aligned": [
          -8.044945017610868e-17,
          4.139263261645079e-17,
          1.0
        ],
        "angle_rad": 9.047355452594233e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "fr3_joint2",
        "joint_other": "fr3_joint2",
        "axis_m": [
          0.0,
          1.0,
          2.2204460492503136e-16
        ],
        "axis_other_aligned": [
          7.554586324970178e-16,
          1.0,
          -5.107017365495556e-16
        ],
        "angle_rad": 1.0524423719893912e-15,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "fr3_joint3",
        "joint_other": "fr3_joint3",
        "axis_m": [
          0.0,
          -4.474228634151475e-17,
          1.0
        ],
        "axis_other_aligned": [
          -8.044945017610867e-17,
          6.16857053315899e-17,
          1.0
        ],
        "angle_rad": 1.3341301077934126e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "fr3_joint4",
        "joint_other": "fr3_joint4",
        "axis_m": [
          0.0,
          -1.0,
          4.440892098500629e-16
        ],
        "axis_other_aligned": [
          -7.554586324970178e-16,
          -1.0,
          -3.7747668315056957e-16
        ],
        "angle_rad": 1.1161040551651942e-15,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "fr3_joint5",
        "joint_other": "fr3_joint5",
        "axis_m": [
          0.0,
          -1.582539029327245e-16,
          1.0
        ],
        "axis_other_aligned": [
          -8.044945017610869e-17,
          2.1099559901311685e-17,
          1.0
        ],
        "angle_rad": 1.9657003501092987e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "fr3_joint6",
        "joint_other": "fr3_joint6",
        "axis_m": [
          0.0,
          -1.0,
          7.771561172376104e-16
        ],
        "axis_other_aligned": [
          -7.554586324970178e-16,
          -1.0,
          -3.7747668315056957e-16
        ],
        "angle_rad": 1.3798168897163548e-15,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "fr3_joint7",
        "joint_other": "fr3_joint7",
        "axis_m": [
          0.0,
          2.0424084633858673e-16,
          -1.0
        ],
        "axis_other_aligned": [
          8.044945017610938e-17,
          8.940173875538835e-16,
          -1.0
        ],
        "angle_rad": 6.944521515875491e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      }
    ],
    "axis_disagreements": [],
    "com_eligible": true,
    "covariance_singular_values": [
      1.4189014729780494,
      0.009646971466394549,
      2.465190328815662e-32
    ],
    "origin_residuals_m": {
      "base": 1.289966160584168e-16,
      "fr3_link0": 1.289966160584168e-16,
      "fr3_link1": 6.917266900280248e-17,
      "fr3_link2": 6.917266900280248e-17,
      "fr3_link3": 1.1460286728622967e-16,
      "fr3_link4": 6.641133626735695e-17,
      "fr3_link5": 2.3085661405987017e-16,
      "fr3_link6": 2.3085661405987017e-16,
      "fr3_link7": 2.263279155442843e-16
    },
    "reason": "Unique proper rigid fit and matched signed axes meet the configured thresholds"
  }
}
```


## Every reported quantity difference

Counts are quantity records, including correlated total/subtree/body mass records; they are not independent robot defects.

| Entity / quantity | M | S | H | H − M | Class | M source | S source | H source |
|---|---|---|---|---|---|---|---|---|
| robot / total_mass | 18.3154851 | unavailable | 18.604001 | 0.288515972 | unknown | [aggregate inputs](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/franka_fr3/fr3.xml#L1) | unavailable | [aggregate inputs](https://github.com/frankaemika/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/fr3/fr3.urdf.xacro#L1) |
| robot / total_com_registered | [0.0150147808, 0.00353364536, 0.552112796] | unavailable | [0.0207587434, 0.00327078562, 0.578906064] | [0.00574396256, -0.000262859745, 0.0267932682] | unknown | [aggregate inputs](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/franka_fr3/fr3.xml#L1) | unavailable | [aggregate inputs](https://github.com/frankaemika/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/fr3/fr3.urdf.xacro#L1) |
| base / subtree_mass | 18.3154851 | unavailable | 18.604001 | 0.288515972 | unknown | [subtree root L70](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/franka_fr3/fr3.xml#L70) | unavailable | [macro declaration L26](https://github.com/frankaemika/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/franka_arm.xacro#L26) |
| fr3_link0 / mass | 2.82067205 | unavailable | 2.3966 | -0.424072054 | unknown | [geometry/inference input L71](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/franka_fr3/fr3.xml#L71) | unavailable | [macro declaration L17](https://github.com/frankaemika/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L17); [YAML numeric inputs L5](https://github.com/frankaemika/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/fr3/inertials.yaml#L5) |
| fr3_link0 / subtree_mass | 18.3154851 | unavailable | 18.604001 | 0.288515972 | unknown | [subtree root L71](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/franka_fr3/fr3.xml#L71) | unavailable | [macro declaration L41](https://github.com/frankaemika/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L41) |
| fr3_link0 / com_registered | [-0.0298548185, -0.00024835472, 0.057579287] | unavailable | [-0.0172, 0.0004, 0.0745] | [0.0126548185, 0.00064835472, 0.016920713] | unknown | [geometry/inference input L71](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/franka_fr3/fr3.xml#L71) | unavailable | [macro declaration L16](https://github.com/frankaemika/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L16); [YAML numeric inputs L3](https://github.com/frankaemika/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/fr3/inertials.yaml#L3) |
| fr3_link0 / principal_moments | [0.00768510692, 0.0112573665, 0.0114678941] | unavailable | [0.00673443556, 0.0107655644, 0.0115] | [-0.000950671354, -0.000491802053, 3.21059218e-05] | unknown | [geometry/inference input L71](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/franka_fr3/fr3.xml#L71) | unavailable | [macro declaration L20](https://github.com/frankaemika/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L20); [YAML numeric inputs L7](https://github.com/frankaemika/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/fr3/inertials.yaml#L7) |
| fr3_link1 / subtree_mass | 15.494813 | unavailable | 16.207401 | 0.712588026 | unknown | [subtree root L80](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/franka_fr3/fr3.xml#L80) | unavailable | [macro declaration L41](https://github.com/frankaemika/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L41) |
| fr3_link2 / subtree_mass | 12.567343 | unavailable | 13.2799357 | 0.712592681 | unknown | [subtree root L86](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/franka_fr3/fr3.xml#L86) | unavailable | [macro declaration L41](https://github.com/frankaemika/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L41) |
| fr3_link3 / subtree_mass | 9.631803 | unavailable | 10.3443986 | 0.712595647 | unknown | [subtree root L92](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/franka_fr3/fr3.xml#L92) | unavailable | [macro declaration L41](https://github.com/frankaemika/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L41) |
| fr3_link4 / subtree_mass | 7.386903 | unavailable | 8.09949728 | 0.712594277 | unknown | [subtree root L99](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/franka_fr3/fr3.xml#L99) | unavailable | [macro declaration L41](https://github.com/frankaemika/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L41) |
| fr3_link5 / subtree_mass | 4.771303 | unavailable | 5.4839017 | 0.712598698 | unknown | [subtree root L106](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/franka_fr3/fr3.xml#L106) | unavailable | [macro declaration L41](https://github.com/frankaemika/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L41) |
| fr3_link6 / subtree_mass | 2.444183 | unavailable | 3.15678094 | 0.712597939 | unknown | [subtree root L114](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/franka_fr3/fr3.xml#L114) | unavailable | [macro declaration L41](https://github.com/frankaemika/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L41) |
| fr3_link7 / subtree_mass | 0.627143 | unavailable | 1.33974329 | 0.712600286 | unknown | [subtree root L127](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/franka_fr3/fr3.xml#L127) | unavailable | [macro declaration L41](https://github.com/frankaemika/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L41) |

## Raw CoM records and reporting decisions

Raw values retain the previous root-anchor registration before Kabsch; original world coordinates also remain in the snapshots. Eligible findings above use the fitted transform into M. Excluded raw records below are diagnostic numbers, not findings. No CoM suppression applies to mass or principal inertia moments.

| Entity / quantity | Raw M | Raw S | Raw H | Raw H − M | Decision | M source | S source | H source |
|---|---|---|---|---|---|---|---|---|
| robot / total_com_registered | [0.0150147808, 0.00353364536, 0.552112796] | unavailable | [0.0207587434, 0.00327078562, 0.578906064] | [0.00574396256, -0.000262859745, 0.0267932682] | eligible; compared after Kabsch alignment | [aggregate inputs](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/franka_fr3/fr3.xml#L1) | unavailable | [aggregate inputs](https://github.com/frankaemika/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/fr3/fr3.urdf.xacro#L1) |
| base / com_registered | [0, 0, 0] | unavailable | [0, 0, 0] | [0, 0, 0] | eligible; compared after Kabsch alignment | [geometry/inference input L70](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/franka_fr3/fr3.xml#L70) | unavailable | [macro declaration L26](https://github.com/frankaemika/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/franka_arm.xacro#L26) |
| fr3_link0 / com_registered | [-0.0298548185, -0.00024835472, 0.057579287] | unavailable | [-0.0172, 0.0004, 0.0745] | [0.0126548185, 0.00064835472, 0.016920713] | eligible; compared after Kabsch alignment | [geometry/inference input L71](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/franka_fr3/fr3.xml#L71) | unavailable | [macro declaration L16](https://github.com/frankaemika/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L16); [YAML numeric inputs L3](https://github.com/frankaemika/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/fr3/inertials.yaml#L3) |
| fr3_link1 / com_registered | [4.128e-07, -0.0181251, 0.2943964] | unavailable | [4.128e-07, -0.0181251324, 0.294396403] | [0, -3.24e-08, 3.00000003e-09] | eligible; compared after Kabsch alignment | [CoM/kinematic input L82](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/franka_fr3/fr3.xml#L82) | unavailable | [macro declaration L16](https://github.com/frankaemika/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L16); [YAML numeric inputs L15](https://github.com/frankaemika/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/fr3/inertials.yaml#L15) |
| fr3_link2 / com_registered | [0.00318289, 0.00881461, 0.4073222] | unavailable | [0.0031828864, 0.0088146084, 0.407322164] | [-3.6e-09, -1.59999997e-09, -3.56e-08] | eligible; compared after Kabsch alignment | [CoM/kinematic input L88](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/franka_fr3/fr3.xml#L88) | unavailable | [macro declaration L16](https://github.com/frankaemika/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L16); [YAML numeric inputs L27](https://github.com/frankaemika/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/fr3/inertials.yaml#L27) |
| fr3_link3 / com_registered | [0.0407016, -0.00482006, 0.6200269] | unavailable | [0.0407015686, -0.0048200565, 0.620026918] | [-3.14e-08, 3.50000014e-09, 1.77e-08] | eligible; compared after Kabsch alignment | [CoM/kinematic input L94](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/franka_fr3/fr3.xml#L94) | unavailable | [macro declaration L16](https://github.com/frankaemika/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L16); [YAML numeric inputs L39](https://github.com/frankaemika/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/fr3/inertials.yaml#L39) |
| fr3_link4 / com_registered | [0.0365899, 0.00851879, 0.7120493] | unavailable | [0.0365899035, 0.0085187868, 0.712049296] | [3.50000002e-09, -3.19999987e-09, -4e-09] | eligible; compared after Kabsch alignment | [CoM/kinematic input L101](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/franka_fr3/fr3.xml#L101) | unavailable | [macro declaration L16](https://github.com/frankaemika/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L16); [YAML numeric inputs L51](https://github.com/frankaemika/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/fr3/inertials.yaml#L51) |
| fr3_link5 / com_registered | [-0.00160396, 0.0292536, 0.9357034] | unavailable | [-0.0016039605, 0.0292536262, 0.935703401] | [-5.00000015e-10, 2.62e-08, 1.00000019e-09] | eligible; compared after Kabsch alignment | [CoM/kinematic input L108](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/franka_fr3/fr3.xml#L108) | unavailable | [macro declaration L16](https://github.com/frankaemika/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L16); [YAML numeric inputs L63](https://github.com/frankaemika/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/fr3/inertials.yaml#L63) |
| fr3_link6 / com_registered | [0.0597131, 0.0101693, 0.9919705] | unavailable | [0.0597131221, 0.0101692726, 0.991970533] | [2.21e-08, -2.73999999e-08, 3.34000002e-08] | eligible; compared after Kabsch alignment | [CoM/kinematic input L116](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/franka_fr3/fr3.xml#L116) | unavailable | [macro declaration L16](https://github.com/frankaemika/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L16); [YAML numeric inputs L75](https://github.com/frankaemika/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/fr3/inertials.yaml#L75) |
| fr3_link7 / com_registered | [0.09252258, -0.00862619, 1.0491633] | unavailable | [0.0925225817, -0.0086261921, 1.04916333] | [1.70000007e-09, -2.09999999e-09, 2.51000003e-08] | eligible; compared after Kabsch alignment | [CoM/kinematic input L129](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/franka_fr3/fr3.xml#L129) | unavailable | [macro declaration L16](https://github.com/frankaemika/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L16); [YAML numeric inputs L87](https://github.com/frankaemika/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/fr3/inertials.yaml#L87) |

## Mass accounting

Every contributing compiled body mass is listed here so total/subtree sums can be checked. Links point to explicit inertials or to geometry inputs when the compiler inferred a mass. CoM links identify inertial inputs; world coordinates additionally use the ancestor transforms and the registration recorded below.

| M body | M kg / source | S kg / source | H kg / source |
|---|---|---|---|
| base | 0 / [geometry/inference input L70](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/franka_fr3/fr3.xml#L70) | unavailable | 0 / [macro declaration L26](https://github.com/frankaemika/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/franka_arm.xacro#L26) |
| fr3_link0 | 2.82067205 / [geometry/inference input L71](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/franka_fr3/fr3.xml#L71) | unavailable | 2.3966 / [macro declaration L17](https://github.com/frankaemika/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L17); [YAML numeric inputs L5](https://github.com/frankaemika/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/fr3/inertials.yaml#L5) |
| fr3_link1 | 2.92747 / [input L82](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/franka_fr3/fr3.xml#L82) | unavailable | 2.92746535 / [macro declaration L17](https://github.com/frankaemika/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L17); [YAML numeric inputs L17](https://github.com/frankaemika/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/fr3/inertials.yaml#L17) |
| fr3_link2 | 2.93554 / [input L88](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/franka_fr3/fr3.xml#L88) | unavailable | 2.93553703 / [macro declaration L17](https://github.com/frankaemika/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L17); [YAML numeric inputs L29](https://github.com/frankaemika/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/fr3/inertials.yaml#L29) |
| fr3_link3 | 2.2449 / [input L94](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/franka_fr3/fr3.xml#L94) | unavailable | 2.24490137 / [macro declaration L17](https://github.com/frankaemika/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L17); [YAML numeric inputs L41](https://github.com/frankaemika/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/fr3/inertials.yaml#L41) |
| fr3_link4 | 2.6156 / [input L101](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/franka_fr3/fr3.xml#L101) | unavailable | 2.61559558 / [macro declaration L17](https://github.com/frankaemika/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L17); [YAML numeric inputs L53](https://github.com/frankaemika/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/fr3/inertials.yaml#L53) |
| fr3_link5 | 2.32712 / [input L108](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/franka_fr3/fr3.xml#L108) | unavailable | 2.32712076 / [macro declaration L17](https://github.com/frankaemika/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L17); [YAML numeric inputs L65](https://github.com/frankaemika/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/fr3/inertials.yaml#L65) |
| fr3_link6 | 1.81704 / [input L116](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/franka_fr3/fr3.xml#L116) | unavailable | 1.81703765 / [macro declaration L17](https://github.com/frankaemika/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L17); [YAML numeric inputs L77](https://github.com/frankaemika/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/fr3/inertials.yaml#L77) |
| fr3_link7 | 0.627143 / [input L129](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/franka_fr3/fr3.xml#L129) | unavailable | 0.627143286 / [macro declaration L17](https://github.com/frankaemika/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L17); [YAML numeric inputs L89](https://github.com/frankaemika/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/fr3/inertials.yaml#L89) |
| upstream-only fr3_hand | unavailable | unavailable | 0.6544 / [geometry/inference input L6](https://github.com/frankaemika/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/end_effectors/franka_hand/franka_hand.srdf.xacro#L6) |
| upstream-only fr3_hand_tcp | unavailable | unavailable | 0 / [geometry/inference input L37](https://github.com/frankaemika/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/end_effectors/common/franka_hand.xacro#L37) |
| upstream-only fr3_leftfinger | unavailable | unavailable | 0.0291 / [geometry/inference input L43](https://github.com/frankaemika/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/end_effectors/common/franka_hand.xacro#L43) |
| upstream-only fr3_link0_accelerometer_bottom | unavailable | unavailable | 0 / [geometry/inference input L204](https://github.com/frankaemika/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L204) |
| upstream-only fr3_link0_accelerometer_top | unavailable | unavailable | 0 / [geometry/inference input L195](https://github.com/frankaemika/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L195) |
| upstream-only fr3_link1_accelerometer_bottom | unavailable | unavailable | 0 / [geometry/inference input L204](https://github.com/frankaemika/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L204) |
| upstream-only fr3_link1_accelerometer_top | unavailable | unavailable | 0 / [geometry/inference input L195](https://github.com/frankaemika/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L195) |
| upstream-only fr3_link2_accelerometer_bottom | unavailable | unavailable | 0 / [geometry/inference input L204](https://github.com/frankaemika/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L204) |
| upstream-only fr3_link2_accelerometer_top | unavailable | unavailable | 0 / [geometry/inference input L195](https://github.com/frankaemika/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L195) |
| upstream-only fr3_link3_accelerometer_bottom | unavailable | unavailable | 0 / [geometry/inference input L204](https://github.com/frankaemika/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L204) |
| upstream-only fr3_link3_accelerometer_top | unavailable | unavailable | 0 / [geometry/inference input L195](https://github.com/frankaemika/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L195) |
| upstream-only fr3_link4_accelerometer_bottom | unavailable | unavailable | 0 / [geometry/inference input L204](https://github.com/frankaemika/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L204) |
| upstream-only fr3_link4_accelerometer_top | unavailable | unavailable | 0 / [geometry/inference input L195](https://github.com/frankaemika/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L195) |
| upstream-only fr3_link5_accelerometer_bottom | unavailable | unavailable | 0 / [geometry/inference input L204](https://github.com/frankaemika/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L204) |
| upstream-only fr3_link5_accelerometer_top | unavailable | unavailable | 0 / [geometry/inference input L195](https://github.com/frankaemika/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/utils.xacro#L195) |
| upstream-only fr3_link8 | unavailable | unavailable | 0 / [geometry/inference input L148](https://github.com/frankaemika/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/robots/common/franka_arm.xacro#L148) |
| upstream-only fr3_rightfinger | unavailable | unavailable | 0.0291 / [geometry/inference input L79](https://github.com/frankaemika/franka_description/blob/7aeeddc449edf8d62b594f9e36a81da53e7796f9/end_effectors/common/franka_hand.xacro#L79) |

## Coverage and unmatched elements

```json
{
  "mapping_h": {
    "bodies": {
      "base": "base",
      "fr3_link0": "fr3_link0",
      "fr3_link1": "fr3_link1",
      "fr3_link2": "fr3_link2",
      "fr3_link3": "fr3_link3",
      "fr3_link4": "fr3_link4",
      "fr3_link5": "fr3_link5",
      "fr3_link6": "fr3_link6",
      "fr3_link7": "fr3_link7"
    },
    "joints": {
      "fr3_joint1": "fr3_joint1",
      "fr3_joint2": "fr3_joint2",
      "fr3_joint3": "fr3_joint3",
      "fr3_joint4": "fr3_joint4",
      "fr3_joint5": "fr3_joint5",
      "fr3_joint6": "fr3_joint6",
      "fr3_joint7": "fr3_joint7"
    },
    "body_methods": {
      "base": "name",
      "fr3_link0": "name",
      "fr3_link1": "name",
      "fr3_link2": "name",
      "fr3_link3": "name",
      "fr3_link4": "name",
      "fr3_link5": "name",
      "fr3_link6": "name",
      "fr3_link7": "name"
    },
    "joint_methods": {
      "fr3_joint1": "name",
      "fr3_joint2": "name",
      "fr3_joint3": "name",
      "fr3_joint4": "name",
      "fr3_joint5": "name",
      "fr3_joint6": "name",
      "fr3_joint7": "name"
    },
    "unmatched_m_bodies": [],
    "unmatched_upstream_bodies": [
      "fr3_hand",
      "fr3_hand_tcp",
      "fr3_leftfinger",
      "fr3_link0_accelerometer_bottom",
      "fr3_link0_accelerometer_top",
      "fr3_link1_accelerometer_bottom",
      "fr3_link1_accelerometer_top",
      "fr3_link2_accelerometer_bottom",
      "fr3_link2_accelerometer_top",
      "fr3_link3_accelerometer_bottom",
      "fr3_link3_accelerometer_top",
      "fr3_link4_accelerometer_bottom",
      "fr3_link4_accelerometer_top",
      "fr3_link5_accelerometer_bottom",
      "fr3_link5_accelerometer_top",
      "fr3_link8",
      "fr3_rightfinger"
    ],
    "unmatched_m_joints": [],
    "unmatched_upstream_joints": [
      "fr3_finger_joint1",
      "fr3_finger_joint2"
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
      "entity": "fr3_joint1",
      "other_entity": "fr3_joint1",
      "quantity": "force",
      "tolerance": "limit",
      "m": 87.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "fr3_joint1",
      "other_entity": "fr3_joint1",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 2.62,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "fr3_joint2",
      "other_entity": "fr3_joint2",
      "quantity": "force",
      "tolerance": "limit",
      "m": 87.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "fr3_joint2",
      "other_entity": "fr3_joint2",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 2.62,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "fr3_joint3",
      "other_entity": "fr3_joint3",
      "quantity": "force",
      "tolerance": "limit",
      "m": 87.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "fr3_joint3",
      "other_entity": "fr3_joint3",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 2.62,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "fr3_joint4",
      "other_entity": "fr3_joint4",
      "quantity": "force",
      "tolerance": "limit",
      "m": 87.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "fr3_joint4",
      "other_entity": "fr3_joint4",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 2.62,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "fr3_joint5",
      "other_entity": "fr3_joint5",
      "quantity": "force",
      "tolerance": "limit",
      "m": 12.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "fr3_joint5",
      "other_entity": "fr3_joint5",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 5.26,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "fr3_joint6",
      "other_entity": "fr3_joint6",
      "quantity": "force",
      "tolerance": "limit",
      "m": 12.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "fr3_joint6",
      "other_entity": "fr3_joint6",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 4.18,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "fr3_joint7",
      "other_entity": "fr3_joint7",
      "quantity": "force",
      "tolerance": "limit",
      "m": 12.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "fr3_joint7",
      "other_entity": "fr3_joint7",
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
| fr3_joint1 / force | 87 | unavailable | unavailable |
| fr3_joint1 / velocity | unavailable | unavailable | 2.62 |
| fr3_joint2 / force | 87 | unavailable | unavailable |
| fr3_joint2 / velocity | unavailable | unavailable | 2.62 |
| fr3_joint3 / force | 87 | unavailable | unavailable |
| fr3_joint3 / velocity | unavailable | unavailable | 2.62 |
| fr3_joint4 / force | 87 | unavailable | unavailable |
| fr3_joint4 / velocity | unavailable | unavailable | 2.62 |
| fr3_joint5 / force | 12 | unavailable | unavailable |
| fr3_joint5 / velocity | unavailable | unavailable | 5.26 |
| fr3_joint6 / force | 12 | unavailable | unavailable |
| fr3_joint6 / velocity | unavailable | unavailable | 4.18 |
| fr3_joint7 / force | 12 | unavailable | unavailable |
| fr3_joint7 / velocity | unavailable | unavailable | 5.26 |
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
  "meshes/robot_arms/fr3/collision/link0.stl",
  "meshes/robot_arms/fr3/collision/link1.stl",
  "meshes/robot_arms/fr3/collision/link2.stl",
  "meshes/robot_arms/fr3/collision/link3.stl",
  "meshes/robot_arms/fr3/collision/link4.stl",
  "meshes/robot_arms/fr3/collision/link5.stl",
  "meshes/robot_arms/fr3/collision/link6.stl",
  "meshes/robot_arms/fr3/collision/link7.stl",
  "meshes/robot_arms/fr3/visual/link0.dae",
  "meshes/robot_arms/fr3/visual/link1.dae",
  "meshes/robot_arms/fr3/visual/link2.dae",
  "meshes/robot_arms/fr3/visual/link3.dae",
  "meshes/robot_arms/fr3/visual/link4.dae",
  "meshes/robot_arms/fr3/visual/link5.dae",
  "meshes/robot_arms/fr3/visual/link6.dae",
  "meshes/robot_arms/fr3/visual/link7.dae",
  "meshes/robot_ee/franka_hand_white/collision/hand.stl",
  "meshes/robot_ee/franka_hand_white/visual/finger.dae",
  "meshes/robot_ee/franka_hand_white/visual/hand.dae",
  "meshes/robots/fr3/collision/link0.stl",
  "meshes/robots/fr3/collision/link1.stl",
  "meshes/robots/fr3/collision/link2.stl",
  "meshes/robots/fr3/collision/link3.stl",
  "meshes/robots/fr3/collision/link4.stl",
  "meshes/robots/fr3/collision/link5.stl",
  "meshes/robots/fr3/collision/link6.stl",
  "meshes/robots/fr3/collision/link7.stl",
  "meshes/robots/fr3/visual/link0.dae",
  "meshes/robots/fr3/visual/link1.dae",
  "meshes/robots/fr3/visual/link2.dae",
  "meshes/robots/fr3/visual/link3.dae",
  "meshes/robots/fr3/visual/link4.dae",
  "meshes/robots/fr3/visual/link5.dae",
  "meshes/robots/fr3/visual/link6.dae",
  "meshes/robots/fr3/visual/link7.dae",
  "robots/common/franka_arm.xacro",
  "robots/common/franka_robot.xacro",
  "robots/common/utils.xacro",
  "robots/fr3/accelerometers.yaml",
  "robots/fr3/dynamics.yaml",
  "robots/fr3/fr3.urdf.xacro",
  "robots/fr3/inertials.yaml",
  "robots/fr3/joint_limits.yaml",
  "robots/fr3/kinematics.yaml"
]
```

## Self comparisons

```json
[
  {
    "file": "franka_fr3/fr3.xml",
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
      "unknown": 14
    },
    "classifications_changed": 0,
    "finding_membership_changes": 0
  },
  "2": {
    "provenance_method": "unknown",
    "counts": {
      "unknown": 14
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
      "base",
      "fr3_link0"
    ],
    "assets_loaded": 36,
    "mesh_conversions": [],
    "nonphysical_normalizations": [],
    "xacro_arguments": {},
    "source_dependencies": [
      "franka_fr3/fr3.xml",
      "franka_fr3/assets/link0_0.obj",
      "franka_fr3/assets/link0_1.obj",
      "franka_fr3/assets/link0_2.obj",
      "franka_fr3/assets/link0_3.obj",
      "franka_fr3/assets/link0_4.obj",
      "franka_fr3/assets/link0_5.obj",
      "franka_fr3/assets/link0_6.obj",
      "franka_fr3/assets/link1.obj",
      "franka_fr3/assets/link2.obj",
      "franka_fr3/assets/link3_0.obj",
      "franka_fr3/assets/link3_1.obj",
      "franka_fr3/assets/link4_0.obj",
      "franka_fr3/assets/link4_1.obj",
      "franka_fr3/assets/link5_0.obj",
      "franka_fr3/assets/link5_1.obj",
      "franka_fr3/assets/link5_2.obj",
      "franka_fr3/assets/link6_0.obj",
      "franka_fr3/assets/link6_1.obj",
      "franka_fr3/assets/link6_2.obj",
      "franka_fr3/assets/link6_3.obj",
      "franka_fr3/assets/link6_4.obj",
      "franka_fr3/assets/link6_5.obj",
      "franka_fr3/assets/link6_6.obj",
      "franka_fr3/assets/link6_7.obj",
      "franka_fr3/assets/link7_0.obj",
      "franka_fr3/assets/link7_1.obj",
      "franka_fr3/assets/link7_2.obj",
      "franka_fr3/assets/link7_3.obj",
      "franka_fr3/assets/link0.stl",
      "franka_fr3/assets/link1.stl",
      "franka_fr3/assets/link2.stl",
      "franka_fr3/assets/link3.stl",
      "franka_fr3/assets/link4.stl",
      "franka_fr3/assets/link5.stl",
      "franka_fr3/assets/link6.stl",
      "franka_fr3/assets/link7.stl"
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
      "fr3_link0_accelerometer_top",
      "fr3_link0_accelerometer_bottom",
      "fr3_link1_accelerometer_top",
      "fr3_link1_accelerometer_bottom",
      "fr3_link2_accelerometer_top",
      "fr3_link2_accelerometer_bottom",
      "fr3_link3_accelerometer_top",
      "fr3_link3_accelerometer_bottom",
      "fr3_link4_accelerometer_top",
      "fr3_link4_accelerometer_bottom",
      "fr3_link5_accelerometer_top",
      "fr3_link5_accelerometer_bottom",
      "fr3_link8",
      "fr3_hand_tcp"
    ],
    "assets_loaded": 20,
    "mesh_conversions": [
      {
        "file": "meshes/robots/fr3/visual/link0.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "meshes/robots/fr3/visual/link1.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "meshes/robots/fr3/visual/link2.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "meshes/robots/fr3/visual/link3.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "meshes/robots/fr3/visual/link4.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "meshes/robots/fr3/visual/link5.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "meshes/robots/fr3/visual/link6.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "meshes/robots/fr3/visual/link7.dae",
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
      "robot_type": "fr3",
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
      "robots/fr3/accelerometers.yaml",
      "robots/fr3/dynamics.yaml",
      "robots/fr3/fr3.urdf.xacro",
      "robots/fr3/inertials.yaml",
      "robots/fr3/joint_limits.yaml",
      "robots/fr3/kinematics.yaml",
      "meshes/robots/fr3/visual/link0.dae",
      "meshes/robots/fr3/collision/link0.stl",
      "meshes/robots/fr3/visual/link1.dae",
      "meshes/robots/fr3/collision/link1.stl",
      "meshes/robots/fr3/visual/link2.dae",
      "meshes/robots/fr3/collision/link2.stl",
      "meshes/robots/fr3/visual/link3.dae",
      "meshes/robots/fr3/collision/link3.stl",
      "meshes/robots/fr3/visual/link4.dae",
      "meshes/robots/fr3/collision/link4.stl",
      "meshes/robots/fr3/visual/link5.dae",
      "meshes/robots/fr3/collision/link5.stl",
      "meshes/robots/fr3/visual/link6.dae",
      "meshes/robots/fr3/collision/link6.stl",
      "meshes/robots/fr3/visual/link7.dae",
      "meshes/robots/fr3/collision/link7.stl",
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
  "historical_snapshots_reused": 56,
  "primary_physics_unchanged": true,
  "source_matching": "original raw-value provenance criteria retained; kinematic guard applies to reported CoM"
}
```
