# robotiq_2f85_v4

Status: **complete**. Provenance: **none**, confidence **none**.

No public revision matches all comparable quantities. Class: NO MATCHING SOURCE; never counted as STALE.

M: `https://github.com/google-deepmind/mujoco_menagerie`, `robotiq_2f85_v4/2f85.xml`, commit `370c43965323c0944b433b202aac5058b5f907a9`.
H: `https://github.com/ros-industrial/robotiq`, `robotiq_2f_85_gripper_visualization/urdf/robotiq_arg2f_85_model.xacro`, commit `45196f6558fe8ba9d89bc8a105396c68c3e7e892`.
S: unavailable. A machine-readable H can still be compared to M; no-match differences are never counted as STALE.

Limit semantics: MJCF effort values are supported actuator torque/force envelopes. URDF effort and velocity values are manufacturer declarations retained from XML; MuJoCo does not enforce those tags. Such declaration comparisons are explicitly distinct from compiled inertial/range quantities.


## Source evidence

```json
[
  {
    "url": "https://github.com/Rhoban/onshape-to-robot",
    "document": "robotiq_2f85_v4/README.md",
    "commit": "370c43965323c0944b433b202aac5058b5f907a9",
    "current": true
  },
  {
    "url": "https://github.com/ros-industrial/robotiq/tree/kinetic-devel/robotiq_2f_85_gripper_visualization",
    "document": "robotiq_2f85_v4/README.md",
    "commit": "370c43965323c0944b433b202aac5058b5f907a9",
    "current": true
  }
]
```


## README derivation evidence

Documentation labels are conservative: an automated documented label requires an explicit affected entity and quantity. Broader conversion notes are retained here for review.

> 3. Created assembly file using onshape and joint limits from robotiq_2f85 XML model.
> 7. Used inertia and mass from robotiq_2f85 model.

## Kinematics consistency

A proper Kabsch rigid transform aligns all matched zero-pose body origins. The maximum per-origin residual and signed hinge/slide axis angles determine whether CoM can be compared; RMS is also recorded. Fewer than three non-collinear origins give insufficient kinematic coverage. CoM records that fail either required M/H or M/S check are excluded from counts and largest discrepancies. Masses, principal moments and raw joint ranges remain unchanged; a flagged range still requires convention review.

| Pair | Status | Origins / rank | RMS / maximum mm | Disagreeing / checked axes |
|---|---|---:|---:|---:|
| M/H | insufficient kinematic coverage | 0 / 0 | unavailable / unavailable | 0 / 0 |

Exact fitted transforms, per-origin residuals, thresholds and axis vectors:

```json
{
  "M/H": {
    "status": "insufficient kinematic coverage",
    "matched_body_origins": 0,
    "position_threshold_m": 0.005,
    "axis_threshold_rad": 0.005,
    "residual_definition": "maximum Euclidean residual over matched body origins; Kabsch minimizes RMS, which is also recorded",
    "coordinate_frames": "each snapshot registered to its matched report anchor",
    "anchor_m": null,
    "anchor_other": null,
    "rotation_other_to_m": null,
    "translation_other_to_m": null,
    "rms_residual_m": null,
    "max_residual_m": null,
    "fit_rank": 0,
    "axis_checks": [],
    "axis_disagreements": [],
    "com_eligible": false,
    "reason": "No matched origins, or zero-pose body-origin data unavailable"
  }
}
```


## Every reported quantity difference

Counts are quantity records, including correlated total/subtree/body mass records; they are not independent robot defects.

| Entity / quantity | M | S | H | H − M | Class | M source | S source | H source |
|---|---|---|---|---|---|---|---|---|
| robot / total_mass | 0.89999986 | unavailable | 0.379436687 | -0.520563173 | NO MATCHING SOURCE | [aggregate inputs](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/robotiq_2f85_v4/2f85.xml#L1) | unavailable | [aggregate inputs](https://github.com/ros-industrial/robotiq/blob/45196f6558fe8ba9d89bc8a105396c68c3e7e892/robotiq_2f_85_gripper_visualization/urdf/robotiq_arg2f_85_model.xacro#L1) |

## Raw CoM records and reporting decisions

Raw values retain the previous root-anchor registration before Kabsch; original world coordinates also remain in the snapshots. Eligible findings above use the fitted transform into M. Excluded raw records below are diagnostic numbers, not findings. No CoM suppression applies to mass or principal inertia moments.

| Entity / quantity | Raw M | Raw S | Raw H | Raw H − M | Decision | M source | S source | H source |
|---|---|---|---|---|---|---|---|---|
| robot / total_com_registered | [6.71320861e-05, 7.27955266e-05, 0.03955232] | unavailable | [5.14904085e-08, -2.78095965e-06, 0.0527726313] | [-6.70805957e-05, -7.55764862e-05, 0.0132203114] | M/H: insufficient kinematic coverage | [aggregate inputs](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/robotiq_2f85_v4/2f85.xml#L1) | unavailable | [aggregate inputs](https://github.com/ros-industrial/robotiq/blob/45196f6558fe8ba9d89bc8a105396c68c3e7e892/robotiq_2f_85_gripper_visualization/urdf/robotiq_arg2f_85_model.xacro#L1) |

## Mass accounting

Every contributing compiled body mass is listed here so total/subtree sums can be checked. Links point to explicit inertials or to geometry inputs when the compiler inferred a mass. CoM links identify inertial inputs; world coordinates additionally use the ancestor transforms and the registration recorded below.

| M body | M kg / source | S kg / source | H kg / source |
|---|---|---|---|
| base | 0.777441 / [input L61](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/robotiq_2f85_v4/2f85.xml#L61) | unavailable | unmatched |
| left_driver | 0.00899563 / [input L69](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/robotiq_2f85_v4/2f85.xml#L69) | unavailable | unmatched |
| left_coupler | 0.0140974 / [input L75](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/robotiq_2f85_v4/2f85.xml#L75) | unavailable | unmatched |
| left_spring_link | 0.0221642 / [input L82](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/robotiq_2f85_v4/2f85.xml#L82) | unavailable | unmatched |
| left_follower | 0.0125222 / [input L88](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/robotiq_2f85_v4/2f85.xml#L88) | unavailable | unmatched |
| left_pad | 0.0035 / [geometry/inference input L95](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/robotiq_2f85_v4/2f85.xml#L95) | unavailable | unmatched |
| right_driver | 0.00899563 / [input L104](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/robotiq_2f85_v4/2f85.xml#L104) | unavailable | unmatched |
| right_coupler | 0.0140974 / [input L110](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/robotiq_2f85_v4/2f85.xml#L110) | unavailable | unmatched |
| right_spring_link | 0.0221642 / [input L117](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/robotiq_2f85_v4/2f85.xml#L117) | unavailable | unmatched |
| right_follower | 0.0125222 / [input L123](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/robotiq_2f85_v4/2f85.xml#L123) | unavailable | unmatched |
| right_pad | 0.0035 / [geometry/inference input L129](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/robotiq_2f85_v4/2f85.xml#L129) | unavailable | unmatched |
| upstream-only left_inner_finger | unavailable | unavailable | 0.0131878223 / [geometry/inference input L81](https://github.com/ros-industrial/robotiq/blob/45196f6558fe8ba9d89bc8a105396c68c3e7e892/robotiq_2f_85_gripper_visualization/urdf/robotiq_arg2f_85_model_macro.xacro#L81) |
| upstream-only left_inner_finger_pad | unavailable | unavailable | 0.00523875 / [geometry/inference input L107](https://github.com/ros-industrial/robotiq/blob/45196f6558fe8ba9d89bc8a105396c68c3e7e892/robotiq_2f_85_gripper_visualization/urdf/robotiq_arg2f_85_model_macro.xacro#L107) |
| upstream-only left_inner_knuckle | unavailable | unavailable | 0.0273082584 / [geometry/inference input L56](https://github.com/ros-industrial/robotiq/blob/45196f6558fe8ba9d89bc8a105396c68c3e7e892/robotiq_2f_85_gripper_visualization/urdf/robotiq_arg2f_85_model_macro.xacro#L56) |
| upstream-only left_outer_finger | unavailable | unavailable | 0.017784572 / [geometry/inference input L31](https://github.com/ros-industrial/robotiq/blob/45196f6558fe8ba9d89bc8a105396c68c3e7e892/robotiq_2f_85_gripper_visualization/urdf/robotiq_arg2f_85_model_macro.xacro#L31) |
| upstream-only left_outer_knuckle | unavailable | unavailable | 0.0129389409 / [geometry/inference input L6](https://github.com/ros-industrial/robotiq/blob/45196f6558fe8ba9d89bc8a105396c68c3e7e892/robotiq_2f_85_gripper_visualization/urdf/robotiq_arg2f_85_model_macro.xacro#L6) |
| upstream-only right_inner_finger | unavailable | unavailable | 0.0131878223 / [geometry/inference input L81](https://github.com/ros-industrial/robotiq/blob/45196f6558fe8ba9d89bc8a105396c68c3e7e892/robotiq_2f_85_gripper_visualization/urdf/robotiq_arg2f_85_model_macro.xacro#L81) |
| upstream-only right_inner_finger_pad | unavailable | unavailable | 0.00523875 / [geometry/inference input L107](https://github.com/ros-industrial/robotiq/blob/45196f6558fe8ba9d89bc8a105396c68c3e7e892/robotiq_2f_85_gripper_visualization/urdf/robotiq_arg2f_85_model_macro.xacro#L107) |
| upstream-only right_inner_knuckle | unavailable | unavailable | 0.0273082584 / [geometry/inference input L56](https://github.com/ros-industrial/robotiq/blob/45196f6558fe8ba9d89bc8a105396c68c3e7e892/robotiq_2f_85_gripper_visualization/urdf/robotiq_arg2f_85_model_macro.xacro#L56) |
| upstream-only right_outer_finger | unavailable | unavailable | 0.017784572 / [geometry/inference input L31](https://github.com/ros-industrial/robotiq/blob/45196f6558fe8ba9d89bc8a105396c68c3e7e892/robotiq_2f_85_gripper_visualization/urdf/robotiq_arg2f_85_model_macro.xacro#L31) |
| upstream-only right_outer_knuckle | unavailable | unavailable | 0.0129389409 / [geometry/inference input L6](https://github.com/ros-industrial/robotiq/blob/45196f6558fe8ba9d89bc8a105396c68c3e7e892/robotiq_2f_85_gripper_visualization/urdf/robotiq_arg2f_85_model_macro.xacro#L6) |
| upstream-only robotiq_arg2f_base_link | unavailable | unavailable | 0.22652 / [input L7](https://github.com/ros-industrial/robotiq/blob/45196f6558fe8ba9d89bc8a105396c68c3e7e892/robotiq_2f_85_gripper_visualization/urdf/robotiq_arg2f.xacro#L7) |

## Coverage and unmatched elements

```json
{
  "mapping_h": {
    "bodies": {},
    "joints": {},
    "body_methods": {},
    "joint_methods": {},
    "unmatched_m_bodies": [
      "base",
      "left_coupler",
      "left_driver",
      "left_follower",
      "left_pad",
      "left_spring_link",
      "right_coupler",
      "right_driver",
      "right_follower",
      "right_pad",
      "right_spring_link"
    ],
    "unmatched_upstream_bodies": [
      "left_inner_finger",
      "left_inner_finger_pad",
      "left_inner_knuckle",
      "left_outer_finger",
      "left_outer_knuckle",
      "right_inner_finger",
      "right_inner_finger_pad",
      "right_inner_knuckle",
      "right_outer_finger",
      "right_outer_knuckle",
      "robotiq_arg2f_base_link"
    ],
    "unmatched_m_joints": [
      "left_driver_joint",
      "left_follower",
      "left_spring_link_joint",
      "right_driver_joint",
      "right_follower_joint",
      "right_spring_link_joint"
    ],
    "unmatched_upstream_joints": [
      "finger_joint",
      "left_inner_finger_joint",
      "left_inner_knuckle_joint",
      "right_inner_finger_joint",
      "right_inner_knuckle_joint",
      "right_outer_knuckle_joint"
    ],
    "registration_anchor": {
      "M": null,
      "H": null,
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
  "https://github.com/ros-industrial/robotiq robotiq_2f_85_gripper_visualization/urdf/robotiq_arg2f_transmission.xacro at 45196f6558fe8ba9d89bc8a105396c68c3e7e892: ValueError: XML has no robot bodies; it is an include/extension fragment, not a standalone source",
  "https://github.com/ros-industrial/robotiq robotiq_2f_85_gripper_visualization/urdf/robotiq_arg2f_85_model_macro.xacro at 45196f6558fe8ba9d89bc8a105396c68c3e7e892: ValueError: Macro-only input has no uniquely identified robot macro"
]
```

## History inputs

```json
[
  "robotiq_2f_85_gripper_visualization/meshes/collision/robotiq_arg2f_85_inner_finger.dae",
  "robotiq_2f_85_gripper_visualization/meshes/collision/robotiq_arg2f_85_inner_knuckle.dae",
  "robotiq_2f_85_gripper_visualization/meshes/collision/robotiq_arg2f_85_outer_finger.dae",
  "robotiq_2f_85_gripper_visualization/meshes/collision/robotiq_arg2f_85_outer_knuckle.dae",
  "robotiq_2f_85_gripper_visualization/meshes/collision/robotiq_arg2f_base_link.stl",
  "robotiq_2f_85_gripper_visualization/meshes/visual/robotiq_arg2f_85_base_link.dae",
  "robotiq_2f_85_gripper_visualization/meshes/visual/robotiq_arg2f_85_inner_finger.dae",
  "robotiq_2f_85_gripper_visualization/meshes/visual/robotiq_arg2f_85_inner_knuckle.dae",
  "robotiq_2f_85_gripper_visualization/meshes/visual/robotiq_arg2f_85_outer_finger.dae",
  "robotiq_2f_85_gripper_visualization/meshes/visual/robotiq_arg2f_85_outer_knuckle.dae",
  "robotiq_2f_85_gripper_visualization/urdf/robotiq_arg2f.xacro",
  "robotiq_2f_85_gripper_visualization/urdf/robotiq_arg2f_85_model.xacro",
  "robotiq_2f_85_gripper_visualization/urdf/robotiq_arg2f_85_model_macro.xacro",
  "robotiq_2f_85_gripper_visualization/urdf/robotiq_arg2f_transmission.xacro"
]
```

## Self comparisons

```json
[
  {
    "file": "robotiq_2f85_v4/2f85.xml",
    "status": "passed",
    "findings": 0
  },
  {
    "file": "robotiq_2f85_v4/mjx_2f85.xml",
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
      "left_pad",
      "right_pad"
    ],
    "assets_loaded": 8,
    "mesh_conversions": [],
    "nonphysical_normalizations": [],
    "xacro_arguments": {},
    "source_dependencies": [
      "robotiq_2f85_v4/2f85.xml",
      "robotiq_2f85_v4/assets/base.stl",
      "robotiq_2f85_v4/assets/base_coupling.stl",
      "robotiq_2f85_v4/assets/c-a01-85-open.stl",
      "robotiq_2f85_v4/assets/driver.stl",
      "robotiq_2f85_v4/assets/coupler.stl",
      "robotiq_2f85_v4/assets/spring_link.stl",
      "robotiq_2f85_v4/assets/follower.stl",
      "robotiq_2f85_v4/assets/tongue.stl"
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
      "left_outer_knuckle",
      "left_outer_finger",
      "left_inner_finger",
      "left_inner_finger_pad",
      "left_inner_knuckle",
      "right_outer_knuckle",
      "right_outer_finger",
      "right_inner_finger",
      "right_inner_finger_pad",
      "right_inner_knuckle"
    ],
    "assets_loaded": 18,
    "mesh_conversions": [
      {
        "file": "robotiq_2f_85_gripper_visualization/meshes/visual/robotiq_arg2f_85_base_link.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "robotiq_2f_85_gripper_visualization/meshes/visual/robotiq_arg2f_85_outer_knuckle.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "robotiq_2f_85_gripper_visualization/meshes/collision/robotiq_arg2f_85_outer_knuckle.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "robotiq_2f_85_gripper_visualization/meshes/visual/robotiq_arg2f_85_outer_finger.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "robotiq_2f_85_gripper_visualization/meshes/collision/robotiq_arg2f_85_outer_finger.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "robotiq_2f_85_gripper_visualization/meshes/visual/robotiq_arg2f_85_inner_finger.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "robotiq_2f_85_gripper_visualization/meshes/collision/robotiq_arg2f_85_inner_finger.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "robotiq_2f_85_gripper_visualization/meshes/visual/robotiq_arg2f_85_inner_knuckle.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "robotiq_2f_85_gripper_visualization/meshes/collision/robotiq_arg2f_85_inner_knuckle.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "robotiq_2f_85_gripper_visualization/meshes/visual/robotiq_arg2f_85_outer_knuckle.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "robotiq_2f_85_gripper_visualization/meshes/collision/robotiq_arg2f_85_outer_knuckle.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "robotiq_2f_85_gripper_visualization/meshes/visual/robotiq_arg2f_85_outer_finger.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "robotiq_2f_85_gripper_visualization/meshes/collision/robotiq_arg2f_85_outer_finger.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "robotiq_2f_85_gripper_visualization/meshes/visual/robotiq_arg2f_85_inner_finger.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "robotiq_2f_85_gripper_visualization/meshes/collision/robotiq_arg2f_85_inner_finger.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "robotiq_2f_85_gripper_visualization/meshes/visual/robotiq_arg2f_85_inner_knuckle.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "robotiq_2f_85_gripper_visualization/meshes/collision/robotiq_arg2f_85_inner_knuckle.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      }
    ],
    "nonphysical_normalizations": [],
    "xacro_arguments": {},
    "source_dependencies": [
      "robotiq_2f_85_gripper_visualization/urdf/robotiq_arg2f.xacro",
      "robotiq_2f_85_gripper_visualization/urdf/robotiq_arg2f_85_model.xacro",
      "robotiq_2f_85_gripper_visualization/urdf/robotiq_arg2f_85_model_macro.xacro",
      "robotiq_2f_85_gripper_visualization/urdf/robotiq_arg2f_transmission.xacro",
      "robotiq_2f_85_gripper_visualization/meshes/visual/robotiq_arg2f_85_base_link.dae",
      "robotiq_2f_85_gripper_visualization/meshes/collision/robotiq_arg2f_base_link.stl",
      "robotiq_2f_85_gripper_visualization/meshes/visual/robotiq_arg2f_85_outer_knuckle.dae",
      "robotiq_2f_85_gripper_visualization/meshes/collision/robotiq_arg2f_85_outer_knuckle.dae",
      "robotiq_2f_85_gripper_visualization/meshes/visual/robotiq_arg2f_85_outer_finger.dae",
      "robotiq_2f_85_gripper_visualization/meshes/collision/robotiq_arg2f_85_outer_finger.dae",
      "robotiq_2f_85_gripper_visualization/meshes/visual/robotiq_arg2f_85_inner_finger.dae",
      "robotiq_2f_85_gripper_visualization/meshes/collision/robotiq_arg2f_85_inner_finger.dae",
      "robotiq_2f_85_gripper_visualization/meshes/visual/robotiq_arg2f_85_inner_knuckle.dae",
      "robotiq_2f_85_gripper_visualization/meshes/collision/robotiq_arg2f_85_inner_knuckle.dae",
      "robotiq_2f_85_gripper_visualization/meshes/visual/robotiq_arg2f_85_outer_knuckle.dae",
      "robotiq_2f_85_gripper_visualization/meshes/collision/robotiq_arg2f_85_outer_knuckle.dae",
      "robotiq_2f_85_gripper_visualization/meshes/visual/robotiq_arg2f_85_outer_finger.dae",
      "robotiq_2f_85_gripper_visualization/meshes/collision/robotiq_arg2f_85_outer_finger.dae",
      "robotiq_2f_85_gripper_visualization/meshes/visual/robotiq_arg2f_85_inner_finger.dae",
      "robotiq_2f_85_gripper_visualization/meshes/collision/robotiq_arg2f_85_inner_finger.dae",
      "robotiq_2f_85_gripper_visualization/meshes/visual/robotiq_arg2f_85_inner_knuckle.dae",
      "robotiq_2f_85_gripper_visualization/meshes/collision/robotiq_arg2f_85_inner_knuckle.dae"
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
  "historical_snapshots_reused": 3,
  "primary_physics_unchanged": true,
  "source_matching": "original raw-value provenance criteria retained; kinematic guard applies to reported CoM"
}
```
