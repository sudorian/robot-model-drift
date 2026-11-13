# boston_dynamics_spot

Status: **partial history**. Provenance: **unknown**, confidence **incomplete**.

Unresolved historical compilation prevents selecting or rejecting a matching source. Pairwise M/H differences are reported with unknown provenance.

M: `https://github.com/google-deepmind/mujoco_menagerie`, `boston_dynamics_spot/spot.xml`, commit `370c43965323c0944b433b202aac5058b5f907a9`.
H: `https://github.com/rai-opensource/spot_description`, `spot_description/urdf/spot.urdf.xacro`, commit `156d1802bfb117f219dbfce7597d283d5fabc968`.
S: unavailable. A machine-readable H can still be compared to M; no-match differences are never counted as STALE.

Limit semantics: MJCF effort values are supported actuator torque/force envelopes. URDF effort and velocity values are manufacturer declarations retained from XML; MuJoCo does not enforce those tags. Such declaration comparisons are explicitly distinct from compiled inertial/range quantities.


## Source evidence

```json
[
  {
    "url": "https://github.com/bdaiinstitute/spot_ros2",
    "document": "boston_dynamics_spot/README.md",
    "commit": "370c43965323c0944b433b202aac5058b5f907a9",
    "current": true
  },
  {
    "url": "https://github.com/bdaiinstitute/spot_ros2/blob/main/spot_description/urdf/spot_arm_macro.urdf",
    "document": "boston_dynamics_spot/README.md",
    "commit": "370c43965323c0944b433b202aac5058b5f907a9",
    "current": true
  },
  {
    "url": "https://github.com/bdaiinstitute/spot_ros2/blob/main/spot_description/urdf/spot_simple.urdf.xacro",
    "document": "boston_dynamics_spot/README.md",
    "commit": "370c43965323c0944b433b202aac5058b5f907a9",
    "current": true
  },
  {
    "url": "https://github.com/kevinzakka/obj2mjcf",
    "document": "boston_dynamics_spot/README.md",
    "commit": "370c43965323c0944b433b202aac5058b5f907a9",
    "current": true
  },
  {
    "url": "https://github.com/rai-opensource/spot_description",
    "document": ".gitmodules",
    "commit": "949feb7b0d702d1923e5b5dd5c0a4a7728ddc88f",
    "parent_repo": "https://github.com/bdaiinstitute/spot_ros2"
  },
  {
    "url": "https://github.com/rai-opensource/spot_description",
    "document": ".gitmodules",
    "commit": "949feb7b0d702d1923e5b5dd5c0a4a7728ddc88f",
    "parent_repo": "https://github.com/bdaiinstitute/spot_ros2"
  },
  {
    "url": "https://github.com/rai-opensource/spot_description",
    "document": ".gitmodules",
    "commit": "949feb7b0d702d1923e5b5dd5c0a4a7728ddc88f",
    "parent_repo": "https://github.com/bdaiinstitute/spot_ros2"
  }
]
```


## README derivation evidence

Documentation labels are conservative: an automated documented label requires an explicit affected entity and quantity. Broader conversion notes are retained here for review.

> 2. Added `<mujoco> <compiler discardvisual="false" strippath="false" fusestatic="false"/> </mujoco>` to the URDF's
>    joint `armature` values (not identified from hardware; arm and wrist `forcerange`
>    limits follow the Spot Arm URDF joint effort limits).

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
    "anchor_m": "body",
    "anchor_other": "body",
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
      "body": 0.0
    },
    "reason": "Fewer than three non-collinear matched origins; fitted rotation is underdetermined"
  }
}
```


## Every reported quantity difference

Counts are quantity records, including correlated total/subtree/body mass records; they are not independent robot defects.

| Entity / quantity | M | S | H | H − M | Class | M source | S source | H source |
|---|---|---|---|---|---|---|---|---|
| robot / total_mass | 50.34 | unavailable | 84.0633145 | 33.7233145 | unknown | [aggregate inputs](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/boston_dynamics_spot/spot.xml#L1) | unavailable | [aggregate inputs](https://github.com/rai-opensource/spot_description/blob/156d1802bfb117f219dbfce7597d283d5fabc968/spot_description/urdf/spot.urdf.xacro#L1) |
| body / mass | 32.86 | unavailable | 33.7233125 | 0.863312453 | unknown | [input L59](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/boston_dynamics_spot/spot.xml#L59) | unavailable | [geometry/inference input L15](https://github.com/rai-opensource/spot_description/blob/156d1802bfb117f219dbfce7597d283d5fabc968/spot_description/urdf/spot_macro.xacro#L15) |
| body / subtree_mass | 50.34 | unavailable | 84.0633145 | 33.7233145 | unknown | [subtree root L57](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/boston_dynamics_spot/spot.xml#L57) | unavailable | [subtree root L15](https://github.com/rai-opensource/spot_description/blob/156d1802bfb117f219dbfce7597d283d5fabc968/spot_description/urdf/spot_macro.xacro#L15) |
| body / principal_moments | [0.13144, 0.13144, 0.13144] | unavailable | [0.221260089, 1.90763383, 1.94857568] | [0.0898200886, 1.77619383, 1.81713568] | unknown | [inertia input L59](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/boston_dynamics_spot/spot.xml#L59) | unavailable | [geometry/inference input L15](https://github.com/rai-opensource/spot_description/blob/156d1802bfb117f219dbfce7597d283d5fabc968/spot_description/urdf/spot_macro.xacro#L15) |

## Raw CoM records and reporting decisions

Raw values retain the previous root-anchor registration before Kabsch; original world coordinates also remain in the snapshots. Eligible findings above use the fitted transform into M. Excluded raw records below are diagnostic numbers, not findings. No CoM suppression applies to mass or principal inertia moments.

| Entity / quantity | Raw M | Raw S | Raw H | Raw H − M | Decision | M source | S source | H source |
|---|---|---|---|---|---|---|---|---|
| robot / total_com_registered | [0.00588823368, -6.27685613e-05, -0.0358126962] | unavailable | [0.00448818818, -0.000523866228, -0.0211616107] | [-0.00140004549, -0.000461097666, 0.0146510855] | M/H: insufficient kinematic coverage | [aggregate inputs](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/boston_dynamics_spot/spot.xml#L1) | unavailable | [aggregate inputs](https://github.com/rai-opensource/spot_description/blob/156d1802bfb117f219dbfce7597d283d5fabc968/spot_description/urdf/spot.urdf.xacro#L1) |
| body / com_registered | [0.0063944, -9.81216e-05, 0.000911379] | unavailable | [0.00346923147, 6.73257399e-05, 0.000739236428] | [-0.00292516853, 0.00016544734, -0.000172142572] | M/H: insufficient kinematic coverage | [CoM/kinematic input L59](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/boston_dynamics_spot/spot.xml#L59) | unavailable | [geometry/inference input L15](https://github.com/rai-opensource/spot_description/blob/156d1802bfb117f219dbfce7597d283d5fabc968/spot_description/urdf/spot_macro.xacro#L15) |

## Mass accounting

Every contributing compiled body mass is listed here so total/subtree sums can be checked. Links point to explicit inertials or to geometry inputs when the compiler inferred a mass. CoM links identify inertial inputs; world coordinates additionally use the ancestor transforms and the registration recorded below.

| M body | M kg / source | S kg / source | H kg / source |
|---|---|---|---|
| body | 32.86 / [input L59](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/boston_dynamics_spot/spot.xml#L59) | unavailable | 33.7233125 / [geometry/inference input L15](https://github.com/rai-opensource/spot_description/blob/156d1802bfb117f219dbfce7597d283d5fabc968/spot_description/urdf/spot_macro.xacro#L15) |
| fl_hip | 1.68 / [input L65](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/boston_dynamics_spot/spot.xml#L65) | unavailable | unmatched |
| fl_uleg | 2.34 / [input L69](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/boston_dynamics_spot/spot.xml#L69) | unavailable | unmatched |
| fl_lleg | 0.35 / [input L76](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/boston_dynamics_spot/spot.xml#L76) | unavailable | unmatched |
| fr_hip | 1.68 / [input L86](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/boston_dynamics_spot/spot.xml#L86) | unavailable | unmatched |
| fr_uleg | 2.34 / [input L90](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/boston_dynamics_spot/spot.xml#L90) | unavailable | unmatched |
| fr_lleg | 0.35 / [input L97](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/boston_dynamics_spot/spot.xml#L97) | unavailable | unmatched |
| hl_hip | 1.68 / [input L107](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/boston_dynamics_spot/spot.xml#L107) | unavailable | unmatched |
| hl_uleg | 2.34 / [input L111](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/boston_dynamics_spot/spot.xml#L111) | unavailable | unmatched |
| hl_lleg | 0.35 / [input L118](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/boston_dynamics_spot/spot.xml#L118) | unavailable | unmatched |
| hr_hip | 1.68 / [input L128](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/boston_dynamics_spot/spot.xml#L128) | unavailable | unmatched |
| hr_uleg | 2.34 / [input L132](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/boston_dynamics_spot/spot.xml#L132) | unavailable | unmatched |
| hr_lleg | 0.35 / [input L139](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/boston_dynamics_spot/spot.xml#L139) | unavailable | unmatched |
| upstream-only base_link | unavailable | unavailable | 32.86 / [input L33](https://github.com/rai-opensource/spot_description/blob/156d1802bfb117f219dbfce7597d283d5fabc968/spot_description/urdf/spot_macro.xacro#L33) |
| upstream-only front_left_hip | unavailable | unavailable | 1.68 / [input L80](https://github.com/rai-opensource/spot_description/blob/156d1802bfb117f219dbfce7597d283d5fabc968/spot_description/urdf/spot_macro.xacro#L80) |
| upstream-only front_left_lower_leg | unavailable | unavailable | 0.35 / [input L166](https://github.com/rai-opensource/spot_description/blob/156d1802bfb117f219dbfce7597d283d5fabc968/spot_description/urdf/spot_macro.xacro#L166) |
| upstream-only front_left_upper_leg | unavailable | unavailable | 2.34 / [input L120](https://github.com/rai-opensource/spot_description/blob/156d1802bfb117f219dbfce7597d283d5fabc968/spot_description/urdf/spot_macro.xacro#L120) |
| upstream-only front_rail | unavailable | unavailable | 1e-06 / [input L47](https://github.com/rai-opensource/spot_description/blob/156d1802bfb117f219dbfce7597d283d5fabc968/spot_description/urdf/spot_macro.xacro#L47) |
| upstream-only front_right_hip | unavailable | unavailable | 1.68 / [input L201](https://github.com/rai-opensource/spot_description/blob/156d1802bfb117f219dbfce7597d283d5fabc968/spot_description/urdf/spot_macro.xacro#L201) |
| upstream-only front_right_lower_leg | unavailable | unavailable | 0.35 / [input L287](https://github.com/rai-opensource/spot_description/blob/156d1802bfb117f219dbfce7597d283d5fabc968/spot_description/urdf/spot_macro.xacro#L287) |
| upstream-only front_right_upper_leg | unavailable | unavailable | 2.34 / [input L241](https://github.com/rai-opensource/spot_description/blob/156d1802bfb117f219dbfce7597d283d5fabc968/spot_description/urdf/spot_macro.xacro#L241) |
| upstream-only rear_left_hip | unavailable | unavailable | 1.68 / [input L322](https://github.com/rai-opensource/spot_description/blob/156d1802bfb117f219dbfce7597d283d5fabc968/spot_description/urdf/spot_macro.xacro#L322) |
| upstream-only rear_left_lower_leg | unavailable | unavailable | 0.35 / [input L408](https://github.com/rai-opensource/spot_description/blob/156d1802bfb117f219dbfce7597d283d5fabc968/spot_description/urdf/spot_macro.xacro#L408) |
| upstream-only rear_left_upper_leg | unavailable | unavailable | 2.34 / [input L362](https://github.com/rai-opensource/spot_description/blob/156d1802bfb117f219dbfce7597d283d5fabc968/spot_description/urdf/spot_macro.xacro#L362) |
| upstream-only rear_rail | unavailable | unavailable | 1e-06 / [input L60](https://github.com/rai-opensource/spot_description/blob/156d1802bfb117f219dbfce7597d283d5fabc968/spot_description/urdf/spot_macro.xacro#L60) |
| upstream-only rear_right_hip | unavailable | unavailable | 1.68 / [input L443](https://github.com/rai-opensource/spot_description/blob/156d1802bfb117f219dbfce7597d283d5fabc968/spot_description/urdf/spot_macro.xacro#L443) |
| upstream-only rear_right_lower_leg | unavailable | unavailable | 0.35 / [input L529](https://github.com/rai-opensource/spot_description/blob/156d1802bfb117f219dbfce7597d283d5fabc968/spot_description/urdf/spot_macro.xacro#L529) |
| upstream-only rear_right_upper_leg | unavailable | unavailable | 2.34 / [input L483](https://github.com/rai-opensource/spot_description/blob/156d1802bfb117f219dbfce7597d283d5fabc968/spot_description/urdf/spot_macro.xacro#L483) |

## Coverage and unmatched elements

```json
{
  "mapping_h": {
    "bodies": {
      "body": "body"
    },
    "joints": {},
    "body_methods": {
      "body": "name"
    },
    "joint_methods": {},
    "unmatched_m_bodies": [
      "fl_hip",
      "fl_lleg",
      "fl_uleg",
      "fr_hip",
      "fr_lleg",
      "fr_uleg",
      "hl_hip",
      "hl_lleg",
      "hl_uleg",
      "hr_hip",
      "hr_lleg",
      "hr_uleg"
    ],
    "unmatched_upstream_bodies": [
      "base_link",
      "front_left_hip",
      "front_left_lower_leg",
      "front_left_upper_leg",
      "front_rail",
      "front_right_hip",
      "front_right_lower_leg",
      "front_right_upper_leg",
      "rear_left_hip",
      "rear_left_lower_leg",
      "rear_left_upper_leg",
      "rear_rail",
      "rear_right_hip",
      "rear_right_lower_leg",
      "rear_right_upper_leg"
    ],
    "unmatched_m_joints": [
      "fl_hx",
      "fl_hy",
      "fl_kn",
      "fr_hx",
      "fr_hy",
      "fr_kn",
      "hl_hx",
      "hl_hy",
      "hl_kn",
      "hr_hx",
      "hr_hy",
      "hr_kn"
    ],
    "unmatched_upstream_joints": [
      "front_left_hip_x",
      "front_left_hip_y",
      "front_left_knee",
      "front_right_hip_x",
      "front_right_hip_y",
      "front_right_knee",
      "rear_left_hip_x",
      "rear_left_hip_y",
      "rear_left_knee",
      "rear_right_hip_x",
      "rear_right_hip_y",
      "rear_right_knee"
    ],
    "registration_anchor": {
      "M": "body",
      "H": "body",
      "root_unmatched": false
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
[]
```

## History inputs

```json
[
  "meshes/base/collision/body_collision.obj",
  "meshes/base/collision/left_lower_leg_collision.obj",
  "meshes/base/collision/left_upper_leg_collision.obj",
  "meshes/base/collision/right_lower_leg_collision.obj",
  "meshes/base/collision/right_upper_leg_collision.obj",
  "meshes/base/visual/body.obj",
  "meshes/base/visual/front_left_hip.obj",
  "meshes/base/visual/front_left_lower_leg.obj",
  "meshes/base/visual/front_left_upper_leg.obj",
  "meshes/base/visual/front_right_hip.obj",
  "meshes/base/visual/front_right_lower_leg.obj",
  "meshes/base/visual/front_right_upper_leg.obj",
  "meshes/base/visual/rear_left_hip.obj",
  "meshes/base/visual/rear_left_lower_leg.obj",
  "meshes/base/visual/rear_left_upper_leg.obj",
  "meshes/base/visual/rear_right_hip.obj",
  "meshes/base/visual/rear_right_lower_leg.obj",
  "meshes/base/visual/rear_right_upper_leg.obj",
  "spot_description/meshes/base/collision/body_collision.obj",
  "spot_description/meshes/base/collision/left_lower_leg_collision.obj",
  "spot_description/meshes/base/collision/left_upper_leg_collision.obj",
  "spot_description/meshes/base/collision/right_lower_leg_collision.obj",
  "spot_description/meshes/base/collision/right_upper_leg_collision.obj",
  "spot_description/meshes/base/visual/body.obj",
  "spot_description/meshes/base/visual/front_left_hip.obj",
  "spot_description/meshes/base/visual/front_left_lower_leg.obj",
  "spot_description/meshes/base/visual/front_left_upper_leg.obj",
  "spot_description/meshes/base/visual/front_right_hip.obj",
  "spot_description/meshes/base/visual/front_right_lower_leg.obj",
  "spot_description/meshes/base/visual/front_right_upper_leg.obj",
  "spot_description/meshes/base/visual/rear_left_hip.obj",
  "spot_description/meshes/base/visual/rear_left_lower_leg.obj",
  "spot_description/meshes/base/visual/rear_left_upper_leg.obj",
  "spot_description/meshes/base/visual/rear_right_hip.obj",
  "spot_description/meshes/base/visual/rear_right_lower_leg.obj",
  "spot_description/meshes/base/visual/rear_right_upper_leg.obj",
  "spot_description/urdf/accessories.urdf.xacro",
  "spot_description/urdf/empty.urdf",
  "spot_description/urdf/spot.ros2_control.xacro",
  "spot_description/urdf/spot.urdf.xacro",
  "spot_description/urdf/spot_macro.xacro",
  "urdf/accessories.urdf.xacro",
  "urdf/empty.urdf",
  "urdf/spot.ros2_control.xacro",
  "urdf/spot.urdf.xacro",
  "urdf/spot_macro.xacro"
]
```

## Self comparisons

```json
[
  {
    "file": "boston_dynamics_spot/spot.xml",
    "status": "passed",
    "findings": 0
  },
  {
    "file": "boston_dynamics_spot/spot_arm.xml",
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
      "unknown": 4
    },
    "classifications_changed": 0,
    "finding_membership_changes": 0
  },
  "2": {
    "provenance_method": "unknown",
    "counts": {
      "unknown": 4
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
      "boston_dynamics_spot/spot.xml"
    ],
    "registration": {
      "translation": [
        0.0,
        0.0,
        0.75
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
      "body"
    ],
    "assets_loaded": 22,
    "mesh_conversions": [],
    "nonphysical_normalizations": [],
    "xacro_arguments": {
      "tf_prefix": "",
      "arm": "false",
      "gripperless": "false",
      "feet": "false",
      "add_ros2_control_tag": "false",
      "hardware_interface_type": "mock",
      "hostname": "10.0.0.3",
      "port": "0",
      "certificate": "",
      "username": "username",
      "password": "password",
      "leasing": "direct",
      "k_q_p": "",
      "k_qd_p": "",
      "include_transmissions": "false"
    },
    "source_dependencies": [
      "spot_description/urdf/accessories.urdf.xacro",
      "spot_description/urdf/empty.urdf",
      "spot_description/urdf/spot.ros2_control.xacro",
      "spot_description/urdf/spot.urdf.xacro",
      "spot_description/urdf/spot_macro.xacro",
      "spot_description/meshes/base/visual/body.obj",
      "spot_description/meshes/base/collision/body_collision.obj",
      "spot_description/meshes/base/visual/front_left_hip.obj",
      "spot_description/meshes/base/visual/front_left_upper_leg.obj",
      "spot_description/meshes/base/collision/left_upper_leg_collision.obj",
      "spot_description/meshes/base/visual/front_left_lower_leg.obj",
      "spot_description/meshes/base/collision/left_lower_leg_collision.obj",
      "spot_description/meshes/base/visual/front_right_hip.obj",
      "spot_description/meshes/base/visual/front_right_upper_leg.obj",
      "spot_description/meshes/base/collision/right_upper_leg_collision.obj",
      "spot_description/meshes/base/visual/front_right_lower_leg.obj",
      "spot_description/meshes/base/collision/right_lower_leg_collision.obj",
      "spot_description/meshes/base/visual/rear_left_hip.obj",
      "spot_description/meshes/base/visual/rear_left_upper_leg.obj",
      "spot_description/meshes/base/collision/left_upper_leg_collision.obj",
      "spot_description/meshes/base/visual/rear_left_lower_leg.obj",
      "spot_description/meshes/base/collision/left_lower_leg_collision.obj",
      "spot_description/meshes/base/visual/rear_right_hip.obj",
      "spot_description/meshes/base/visual/rear_right_upper_leg.obj",
      "spot_description/meshes/base/collision/right_upper_leg_collision.obj",
      "spot_description/meshes/base/visual/rear_right_lower_leg.obj",
      "spot_description/meshes/base/collision/right_lower_leg_collision.obj"
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
  "self_variants_recompiled": 2,
  "historical_snapshots_reused": 22,
  "primary_physics_unchanged": true,
  "source_matching": "original raw-value provenance criteria retained; kinematic guard applies to reported CoM"
}
```
