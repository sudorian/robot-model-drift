# franka_emika_panda

Status: **complete**. Provenance: **none**, confidence **none**.

No public revision matches all comparable quantities. Class: NO MATCHING SOURCE; never counted as STALE.

M: `https://github.com/google-deepmind/mujoco_menagerie`, `franka_emika_panda/panda_nohand.xml`, commit `370c43965323c0944b433b202aac5058b5f907a9`.
H: `https://github.com/frankaemika/franka_ros`, `franka_description/robots/panda/panda.urdf.xacro`, commit `ddd2fffd9de44b02ad15b4bbb2bfa2cec4d60d98`.
S: unavailable. A machine-readable H can still be compared to M; no-match differences are never counted as STALE.

Limit semantics: MJCF effort values are supported actuator torque/force envelopes. URDF effort and velocity values are manufacturer declarations retained from XML; MuJoCo does not enforce those tags. Such declaration comparisons are explicitly distinct from compiled inertial/range quantities.


## Source evidence

```json
[
  {
    "url": "https://github.com/frankaemika/franka_ros/blob/develop/franka_description/robots/common/inertial.yaml",
    "document": "franka_emika_panda/README.md",
    "commit": "370c43965323c0944b433b202aac5058b5f907a9",
    "current": true
  },
  {
    "url": "https://github.com/frankaemika/franka_ros/tree/develop/franka_description",
    "document": "franka_emika_panda/README.md",
    "commit": "370c43965323c0944b433b202aac5058b5f907a9",
    "current": true
  },
  {
    "url": "https://github.com/frankaemika/franka_ros/tree/develop/franka_description/meshes/collision",
    "document": "franka_emika_panda/README.md",
    "commit": "370c43965323c0944b433b202aac5058b5f907a9",
    "current": true
  },
  {
    "url": "https://github.com/frankaemika/franka_ros/tree/develop/franka_description/meshes/visual",
    "document": "franka_emika_panda/README.md",
    "commit": "370c43965323c0944b433b202aac5058b5f907a9",
    "current": true
  },
  {
    "url": "https://github.com/frankaemika/franka_ros/tree/develop/franka_description/robots",
    "document": "franka_emika_panda/README.md",
    "commit": "370c43965323c0944b433b202aac5058b5f907a9",
    "current": true
  },
  {
    "url": "https://github.com/kevinzakka/obj2mjcf",
    "document": "franka_emika_panda/README.md",
    "commit": "370c43965323c0944b433b202aac5058b5f907a9",
    "current": true
  },
  {
    "url": "https://github.com/kmammou/v-hacd",
    "document": "franka_emika_panda/README.md",
    "commit": "370c43965323c0944b433b202aac5058b5f907a9",
    "current": true
  },
  {
    "url": "https://github.com/frankaemika/franka_ros/blob/develop/franka_description/robots/inertial.yaml",
    "document": "franka_emika_panda/README.md",
    "commit": "1b93125c79bb95e4e55a1d6471adb2cd92c71feb",
    "current": false
  }
]
```


## README derivation evidence

Documentation labels are conservative: an automated documented label requires an explicit affected entity and quantity. Broader conversion notes are retained here for review.

> 7. Matched inertial parameters with [inertial.yaml](
>    https://github.com/frankaemika/franka_ros/blob/develop/franka_description/robots/common/inertial.yaml).
> 7. Removed tendon and added position actuator for the gripper. Changed gripper `ctrlrange`.

## Kinematics consistency

A proper Kabsch rigid transform aligns all matched zero-pose body origins. The maximum per-origin residual and signed hinge/slide axis angles determine whether CoM can be compared; RMS is also recorded. Fewer than three non-collinear origins give insufficient kinematic coverage. CoM records that fail either required M/H or M/S check are excluded from counts and largest discrepancies. Masses, principal moments and raw joint ranges remain unchanged; a flagged range still requires convention review.

| Pair | Status | Origins / rank | RMS / maximum mm | Disagreeing / checked axes |
|---|---|---:|---:|---:|
| M/H | insufficient kinematic coverage | 1 / 0 | 0 / 0 | 0 / 0 |

Exact fitted transforms, per-origin residuals, thresholds and axis vectors:

```json
{
  "M/H": {
    "status": "insufficient kinematic coverage",
    "matched_body_origins": 1,
    "position_threshold_m": 0.005,
    "axis_threshold_rad": 0.005,
    "residual_definition": "maximum Euclidean residual over matched body origins; Kabsch minimizes RMS, which is also recorded",
    "coordinate_frames": "each snapshot registered to its matched report anchor",
    "anchor_m": "attachment",
    "anchor_other": "panda_link8",
    "rotation_other_to_m": [
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
    ],
    "translation_other_to_m": [
      0.0,
      0.0,
      0.0
    ],
    "rms_residual_m": 0.0,
    "max_residual_m": 0.0,
    "fit_rank": 0,
    "axis_checks": [],
    "axis_disagreements": [],
    "com_eligible": false,
    "covariance_singular_values": [
      0.0,
      0.0,
      0.0
    ],
    "origin_residuals_m": {
      "attachment": 0.0
    },
    "reason": "Fewer than three non-collinear matched origins; fitted rotation is underdetermined"
  }
}
```


## Every reported quantity difference

Counts are quantity records, including correlated total/subtree/body mass records; they are not independent robot defects.

| Entity / quantity | M | S | H | H − M | Class | M source | S source | H source |
|---|---|---|---|---|---|---|---|---|
| robot / total_mass | 16.691901 | unavailable | 91.6282737 | 74.9363727 | NO MATCHING SOURCE | [aggregate inputs](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/franka_emika_panda/panda_nohand.xml#L1) | unavailable | [aggregate inputs](https://github.com/frankaemika/franka_ros/blob/ddd2fffd9de44b02ad15b4bbb2bfa2cec4d60d98/franka_description/robots/panda/panda.urdf.xacro#L1) |

## Raw CoM records and reporting decisions

Raw values retain the previous root-anchor registration before Kabsch; original world coordinates also remain in the snapshots. Eligible findings above use the fitted transform into M. Excluded raw records below are diagnostic numbers, not findings. No CoM suppression applies to mass or principal inertia moments.

| Entity / quantity | Raw M | Raw S | Raw H | Raw H − M | Decision | M source | S source | H source |
|---|---|---|---|---|---|---|---|---|
| robot / total_com_registered | [0.0429392759, 0.0524065615, 0.332919023] | unavailable | [-0.075223484, -0.00467696682, 0.393390488] | [-0.11816276, -0.0570835283, 0.0604714646] | M/H: insufficient kinematic coverage | [aggregate inputs](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/franka_emika_panda/panda_nohand.xml#L1) | unavailable | [aggregate inputs](https://github.com/frankaemika/franka_ros/blob/ddd2fffd9de44b02ad15b4bbb2bfa2cec4d60d98/franka_description/robots/panda/panda.urdf.xacro#L1) |
| attachment / com_registered | [-1.74271756e-34, 2.81202669e-33, 0.107] | unavailable | [0, 6.57374917e-33, 0.107] | [1.74271756e-34, 3.76172248e-33, 2.35922393e-16] | M/H: insufficient kinematic coverage | [geometry/inference input L187](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/franka_emika_panda/panda_nohand.xml#L187) | unavailable | [geometry/inference input L131](https://github.com/frankaemika/franka_ros/blob/ddd2fffd9de44b02ad15b4bbb2bfa2cec4d60d98/franka_description/robots/common/franka_arm.xacro#L131) |

## Mass accounting

Every contributing compiled body mass is listed here so total/subtree sums can be checked. Links point to explicit inertials or to geometry inputs when the compiler inferred a mass. CoM links identify inertial inputs; world coordinates additionally use the ancestor transforms and the registration recorded below.

| M body | M kg / source | S kg / source | H kg / source |
|---|---|---|---|
| link0 | 0.629769 / [input L99](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/franka_emika_panda/panda_nohand.xml#L99) | unavailable | unmatched |
| link1 | 4.970684 / [input L114](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/franka_emika_panda/panda_nohand.xml#L114) | unavailable | unmatched |
| link2 | 0.646926 / [input L120](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/franka_emika_panda/panda_nohand.xml#L120) | unavailable | unmatched |
| link3 | 3.228604 / [input L127](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/franka_emika_panda/panda_nohand.xml#L127) | unavailable | unmatched |
| link4 | 3.587895 / [input L135](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/franka_emika_panda/panda_nohand.xml#L135) | unavailable | unmatched |
| link5 | 1.225946 / [input L144](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/franka_emika_panda/panda_nohand.xml#L144) | unavailable | unmatched |
| link6 | 1.666555 / [input L154](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/franka_emika_panda/panda_nohand.xml#L154) | unavailable | unmatched |
| link7 | 0.735522 / [input L176](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/franka_emika_panda/panda_nohand.xml#L176) | unavailable | unmatched |
| attachment | 0 / [geometry/inference input L187](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/franka_emika_panda/panda_nohand.xml#L187) | unavailable | 0 / [geometry/inference input L131](https://github.com/frankaemika/franka_ros/blob/ddd2fffd9de44b02ad15b4bbb2bfa2cec4d60d98/franka_description/robots/common/franka_arm.xacro#L131) |
| upstream-only panda_link0 | unavailable | unavailable | 2.99646944 / [input L21](https://github.com/frankaemika/franka_ros/blob/ddd2fffd9de44b02ad15b4bbb2bfa2cec4d60d98/franka_gazebo/test/launch/panda-gazebo.urdf#L21) |
| upstream-only panda_link0_sc | unavailable | unavailable | 6.87066313 / [geometry/inference input L56](https://github.com/frankaemika/franka_ros/blob/ddd2fffd9de44b02ad15b4bbb2bfa2cec4d60d98/franka_description/robots/common/utils.xacro#L56) |
| upstream-only panda_link1 | unavailable | unavailable | 2.9750379 / [input L43](https://github.com/frankaemika/franka_ros/blob/ddd2fffd9de44b02ad15b4bbb2bfa2cec4d60d98/franka_gazebo/test/launch/panda-gazebo.urdf#L43) |
| upstream-only panda_link1_sc | unavailable | unavailable | 13.308729 / [geometry/inference input L56](https://github.com/frankaemika/franka_ros/blob/ddd2fffd9de44b02ad15b4bbb2bfa2cec4d60d98/franka_description/robots/common/utils.xacro#L56) |
| upstream-only panda_link2 | unavailable | unavailable | 3.00425409 / [input L74](https://github.com/frankaemika/franka_ros/blob/ddd2fffd9de44b02ad15b4bbb2bfa2cec4d60d98/franka_gazebo/test/launch/panda-gazebo.urdf#L74) |
| upstream-only panda_link2_sc | unavailable | unavailable | 9.16088418 / [geometry/inference input L56](https://github.com/frankaemika/franka_ros/blob/ddd2fffd9de44b02ad15b4bbb2bfa2cec4d60d98/franka_description/robots/common/utils.xacro#L56) |
| upstream-only panda_link3 | unavailable | unavailable | 2.32783899 / [input L105](https://github.com/frankaemika/franka_ros/blob/ddd2fffd9de44b02ad15b4bbb2bfa2cec4d60d98/franka_gazebo/test/launch/panda-gazebo.urdf#L105) |
| upstream-only panda_link3_sc | unavailable | unavailable | 9.92429119 / [geometry/inference input L56](https://github.com/frankaemika/franka_ros/blob/ddd2fffd9de44b02ad15b4bbb2bfa2cec4d60d98/franka_description/robots/common/utils.xacro#L56) |
| upstream-only panda_link4 | unavailable | unavailable | 2.37380692 / [input L136](https://github.com/frankaemika/franka_ros/blob/ddd2fffd9de44b02ad15b4bbb2bfa2cec4d60d98/franka_gazebo/test/launch/panda-gazebo.urdf#L136) |
| upstream-only panda_link4_sc | unavailable | unavailable | 9.16088418 / [geometry/inference input L56](https://github.com/frankaemika/franka_ros/blob/ddd2fffd9de44b02ad15b4bbb2bfa2cec4d60d98/franka_description/robots/common/utils.xacro#L56) |
| upstream-only panda_link5 | unavailable | unavailable | 3.4191018 / [input L167](https://github.com/frankaemika/franka_ros/blob/ddd2fffd9de44b02ad15b4bbb2bfa2cec4d60d98/franka_gazebo/test/launch/panda-gazebo.urdf#L167) |
| upstream-only panda_link5_sc | unavailable | unavailable | 11.3762306 / [geometry/inference input L56](https://github.com/frankaemika/franka_ros/blob/ddd2fffd9de44b02ad15b4bbb2bfa2cec4d60d98/franka_description/robots/common/utils.xacro#L56) |
| upstream-only panda_link6 | unavailable | unavailable | 1.43494 / [input L198](https://github.com/frankaemika/franka_ros/blob/ddd2fffd9de44b02ad15b4bbb2bfa2cec4d60d98/franka_gazebo/test/launch/panda-gazebo.urdf#L198) |
| upstream-only panda_link6_sc | unavailable | unavailable | 5.89781661 / [geometry/inference input L56](https://github.com/frankaemika/franka_ros/blob/ddd2fffd9de44b02ad15b4bbb2bfa2cec4d60d98/franka_description/robots/common/utils.xacro#L56) |
| upstream-only panda_link7 | unavailable | unavailable | 0.446028348 / [input L229](https://github.com/frankaemika/franka_ros/blob/ddd2fffd9de44b02ad15b4bbb2bfa2cec4d60d98/franka_gazebo/test/launch/panda-gazebo.urdf#L229) |
| upstream-only panda_link7_sc | unavailable | unavailable | 6.95129734 / [geometry/inference input L56](https://github.com/frankaemika/franka_ros/blob/ddd2fffd9de44b02ad15b4bbb2bfa2cec4d60d98/franka_description/robots/common/utils.xacro#L56) |

## Coverage and unmatched elements

```json
{
  "mapping_h": {
    "bodies": {
      "attachment": "panda_link8"
    },
    "joints": {},
    "body_methods": {
      "attachment": "unique kinematic subtree"
    },
    "joint_methods": {},
    "unmatched_m_bodies": [
      "link0",
      "link1",
      "link2",
      "link3",
      "link4",
      "link5",
      "link6",
      "link7"
    ],
    "unmatched_upstream_bodies": [
      "panda_link0",
      "panda_link0_sc",
      "panda_link1",
      "panda_link1_sc",
      "panda_link2",
      "panda_link2_sc",
      "panda_link3",
      "panda_link3_sc",
      "panda_link4",
      "panda_link4_sc",
      "panda_link5",
      "panda_link5_sc",
      "panda_link6",
      "panda_link6_sc",
      "panda_link7",
      "panda_link7_sc"
    ],
    "unmatched_m_joints": [
      "joint1",
      "joint2",
      "joint3",
      "joint4",
      "joint5",
      "joint6",
      "joint7"
    ],
    "unmatched_upstream_joints": [
      "panda_joint1",
      "panda_joint2",
      "panda_joint3",
      "panda_joint4",
      "panda_joint5",
      "panda_joint6",
      "panda_joint7"
    ],
    "registration_anchor": {
      "M": "attachment",
      "H": "panda_link8",
      "root_unmatched": true
    }
  },
  "mapping_s": null,
  "unavailable": []
}
```

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
  "https://github.com/frankaemika/franka_ros franka_description/robots/common/utils.xacro at ddd2fffd9de44b02ad15b4bbb2bfa2cec4d60d98: ValueError: Macro-only input has no uniquely identified robot macro",
  "https://github.com/frankaemika/franka_ros franka_description/robots/common/franka_arm.xacro at ddd2fffd9de44b02ad15b4bbb2bfa2cec4d60d98: ValueError: Macro franka_arm requires unsupported explicit arguments: ['0', \"0'\", '0', \"0'\", 'joint_limits']",
  "https://github.com/frankaemika/franka_ros franka_description/robots/common/franka_hand.xacro at ddd2fffd9de44b02ad15b4bbb2bfa2cec4d60d98: ValueError: Macro franka_hand requires unsupported explicit arguments: ['0', \"0'\", '0', \"0'\", '0', \"0.1034'\", '0', \"0'\"]",
  "https://github.com/frankaemika/franka_ros franka_description/robots/common/franka_robot.xacro at ddd2fffd9de44b02ad15b4bbb2bfa2cec4d60d98: ValueError: Macro franka_robot requires unsupported explicit arguments: ['arm_id', 'joint_limits', '0', \"0'\", '0', \"0'\", '0', \"0.1034'\", '0', \"0'\"]"
]
```

## History inputs

```json
[
  "franka_description/meshes/collision/link0.stl",
  "franka_description/meshes/collision/link1.stl",
  "franka_description/meshes/collision/link2.stl",
  "franka_description/meshes/collision/link3.stl",
  "franka_description/meshes/collision/link4.stl",
  "franka_description/meshes/collision/link5.stl",
  "franka_description/meshes/collision/link6.stl",
  "franka_description/meshes/collision/link7.stl",
  "franka_description/meshes/visual/link0.dae",
  "franka_description/meshes/visual/link1.dae",
  "franka_description/meshes/visual/link2.dae",
  "franka_description/meshes/visual/link3.dae",
  "franka_description/meshes/visual/link4.dae",
  "franka_description/meshes/visual/link5.dae",
  "franka_description/meshes/visual/link6.dae",
  "franka_description/meshes/visual/link7.dae",
  "franka_description/robots/common/franka_arm.xacro",
  "franka_description/robots/common/franka_robot.xacro",
  "franka_description/robots/common/utils.xacro",
  "franka_description/robots/panda/joint_limits.yaml",
  "franka_description/robots/panda/panda.urdf.xacro"
]
```

## Self comparisons

```json
[
  {
    "file": "franka_emika_panda/hand.xml",
    "status": "passed",
    "findings": 0
  },
  {
    "file": "franka_emika_panda/mjx_hand.xml",
    "status": "passed",
    "findings": 0
  },
  {
    "file": "franka_emika_panda/mjx_panda.xml",
    "status": "passed",
    "findings": 0
  },
  {
    "file": "franka_emika_panda/mjx_panda_nohand.xml",
    "status": "passed",
    "findings": 0
  },
  {
    "file": "franka_emika_panda/mjx_scene.xml",
    "status": "passed",
    "findings": 0
  },
  {
    "file": "franka_emika_panda/mjx_single_cube.xml",
    "status": "passed",
    "findings": 0
  },
  {
    "file": "franka_emika_panda/panda.xml",
    "status": "passed",
    "findings": 0
  },
  {
    "file": "franka_emika_panda/panda_nohand.xml",
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
      "NO MATCHING SOURCE": 1
    },
    "classifications_changed": 0,
    "finding_membership_changes": 0
  },
  "2": {
    "provenance_method": "none",
    "counts": {
      "NO MATCHING SOURCE": 1
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
      "attachment"
    ],
    "assets_loaded": 59,
    "mesh_conversions": [],
    "nonphysical_normalizations": [],
    "xacro_arguments": {},
    "source_dependencies": [
      "franka_emika_panda/panda_nohand.xml",
      "franka_emika_panda/assets/link0.stl",
      "franka_emika_panda/assets/link1.stl",
      "franka_emika_panda/assets/link2.stl",
      "franka_emika_panda/assets/link3.stl",
      "franka_emika_panda/assets/link4.stl",
      "franka_emika_panda/assets/link5_collision_0.obj",
      "franka_emika_panda/assets/link5_collision_1.obj",
      "franka_emika_panda/assets/link5_collision_2.obj",
      "franka_emika_panda/assets/link6.stl",
      "franka_emika_panda/assets/link7.stl",
      "franka_emika_panda/assets/link0_0.obj",
      "franka_emika_panda/assets/link0_1.obj",
      "franka_emika_panda/assets/link0_2.obj",
      "franka_emika_panda/assets/link0_3.obj",
      "franka_emika_panda/assets/link0_4.obj",
      "franka_emika_panda/assets/link0_5.obj",
      "franka_emika_panda/assets/link0_7.obj",
      "franka_emika_panda/assets/link0_8.obj",
      "franka_emika_panda/assets/link0_9.obj",
      "franka_emika_panda/assets/link0_10.obj",
      "franka_emika_panda/assets/link0_11.obj",
      "franka_emika_panda/assets/link1.obj",
      "franka_emika_panda/assets/link2.obj",
      "franka_emika_panda/assets/link3_0.obj",
      "franka_emika_panda/assets/link3_1.obj",
      "franka_emika_panda/assets/link3_2.obj",
      "franka_emika_panda/assets/link3_3.obj",
      "franka_emika_panda/assets/link4_0.obj",
      "franka_emika_panda/assets/link4_1.obj",
      "franka_emika_panda/assets/link4_2.obj",
      "franka_emika_panda/assets/link4_3.obj",
      "franka_emika_panda/assets/link5_0.obj",
      "franka_emika_panda/assets/link5_1.obj",
      "franka_emika_panda/assets/link5_2.obj",
      "franka_emika_panda/assets/link6_0.obj",
      "franka_emika_panda/assets/link6_1.obj",
      "franka_emika_panda/assets/link6_2.obj",
      "franka_emika_panda/assets/link6_3.obj",
      "franka_emika_panda/assets/link6_4.obj",
      "franka_emika_panda/assets/link6_5.obj",
      "franka_emika_panda/assets/link6_6.obj",
      "franka_emika_panda/assets/link6_7.obj",
      "franka_emika_panda/assets/link6_8.obj",
      "franka_emika_panda/assets/link6_9.obj",
      "franka_emika_panda/assets/link6_10.obj",
      "franka_emika_panda/assets/link6_11.obj",
      "franka_emika_panda/assets/link6_12.obj",
      "franka_emika_panda/assets/link6_13.obj",
      "franka_emika_panda/assets/link6_14.obj",
      "franka_emika_panda/assets/link6_15.obj",
      "franka_emika_panda/assets/link6_16.obj",
      "franka_emika_panda/assets/link7_0.obj",
      "franka_emika_panda/assets/link7_1.obj",
      "franka_emika_panda/assets/link7_2.obj",
      "franka_emika_panda/assets/link7_3.obj",
      "franka_emika_panda/assets/link7_4.obj",
      "franka_emika_panda/assets/link7_5.obj",
      "franka_emika_panda/assets/link7_6.obj",
      "franka_emika_panda/assets/link7_7.obj"
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
      "panda_link0",
      "panda_link0_sc",
      "panda_link1",
      "panda_link1_sc",
      "panda_link2",
      "panda_link2_sc",
      "panda_link3",
      "panda_link3_sc",
      "panda_link4",
      "panda_link4_sc",
      "panda_link5",
      "panda_link5_sc",
      "panda_link6",
      "panda_link6_sc",
      "panda_link7",
      "panda_link7_sc",
      "panda_link8"
    ],
    "assets_loaded": 16,
    "mesh_conversions": [
      {
        "file": "franka_description/meshes/visual/link0.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "franka_description/meshes/visual/link1.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "franka_description/meshes/visual/link2.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "franka_description/meshes/visual/link3.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "franka_description/meshes/visual/link4.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "franka_description/meshes/visual/link5.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "franka_description/meshes/visual/link6.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "franka_description/meshes/visual/link7.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      }
    ],
    "nonphysical_normalizations": [],
    "xacro_arguments": {
      "arm_id": "panda",
      "hand": "false",
      "tcp_xyz": "0 0 0.1034",
      "tcp_rpy": "0 0 0",
      "gazebo": "false",
      "parent": "world",
      "xyz": "0 0 0",
      "rpy": "0 0 0"
    },
    "source_dependencies": [
      "franka_description/robots/common/franka_arm.xacro",
      "franka_description/robots/common/franka_robot.xacro",
      "franka_description/robots/common/utils.xacro",
      "franka_description/robots/panda/joint_limits.yaml",
      "franka_description/robots/panda/panda.urdf.xacro",
      "franka_description/meshes/visual/link0.dae",
      "franka_description/meshes/collision/link0.stl",
      "franka_description/meshes/visual/link1.dae",
      "franka_description/meshes/collision/link1.stl",
      "franka_description/meshes/visual/link2.dae",
      "franka_description/meshes/collision/link2.stl",
      "franka_description/meshes/visual/link3.dae",
      "franka_description/meshes/collision/link3.stl",
      "franka_description/meshes/visual/link4.dae",
      "franka_description/meshes/collision/link4.stl",
      "franka_description/meshes/visual/link5.dae",
      "franka_description/meshes/collision/link5.stl",
      "franka_description/meshes/visual/link6.dae",
      "franka_description/meshes/collision/link6.stl",
      "franka_description/meshes/visual/link7.dae",
      "franka_description/meshes/collision/link7.stl"
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
  "self_variants_recompiled": 8,
  "historical_snapshots_reused": 7,
  "primary_physics_unchanged": true,
  "source_matching": "original raw-value provenance criteria retained; kinematic guard applies to reported CoM"
}
```
