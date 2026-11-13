# realsense_d435i

Status: **partial history**. Provenance: **unknown**, confidence **incomplete**.

Unresolved historical compilation prevents selecting or rejecting a matching source. Pairwise M/H differences are reported with unknown provenance.

M: `https://github.com/google-deepmind/mujoco_menagerie`, `realsense_d435i/d435i.xml`, commit `370c43965323c0944b433b202aac5058b5f907a9`.
H: `https://github.com/IntelRealSense/realsense-ros`, `realsense2_description/urdf/_d435i.urdf.xacro`, commit `7a87097c499e3b0b69518d54a8e7a9ac1924e87c`.
S: unavailable. A machine-readable H can still be compared to M; no-match differences are never counted as STALE.

Limit semantics: MJCF effort values are supported actuator torque/force envelopes. URDF effort and velocity values are manufacturer declarations retained from XML; MuJoCo does not enforce those tags. Such declaration comparisons are explicitly distinct from compiled inertial/range quantities.


## Source evidence

```json
[
  {
    "url": "https://github.com/IntelRealSense/realsense-ros/blob/ros2-development/realsense2_description/meshes/d435.dae",
    "document": "realsense_d435i/README.md",
    "commit": "370c43965323c0944b433b202aac5058b5f907a9",
    "current": true
  },
  {
    "url": "https://github.com/IntelRealSense/realsense-ros/blob/ros2-development/realsense2_description/urdf/_d435i.urdf.xacro",
    "document": "realsense_d435i/README.md",
    "commit": "370c43965323c0944b433b202aac5058b5f907a9",
    "current": true
  },
  {
    "url": "https://github.com/kevinzakka/obj2mjcf",
    "document": "realsense_d435i/README.md",
    "commit": "370c43965323c0944b433b202aac5058b5f907a9",
    "current": true
  }
]
```


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
    "anchor_m": "d435i",
    "anchor_other": "camera_link",
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
      "d435i": 0.0
    },
    "reason": "Fewer than three non-collinear matched origins; fitted rotation is underdetermined"
  }
}
```


## Every reported quantity difference

Counts are quantity records, including correlated total/subtree/body mass records; they are not independent robot defects.

| Entity / quantity | M | S | H | H − M | Class | M source | S source | H source |
|---|---|---|---|---|---|---|---|---|
| d435i / principal_moments | [4.55466896e-06, 3.7054997e-05, 3.79939974e-05] | unavailable | [0.00049894, 0.003879257, 0.003881243] | [0.000494385331, 0.003842202, 0.003843249] | unknown | [geometry/inference input L41](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/realsense_d435i/d435i.xml#L41) | unavailable | [inertia input L99](https://github.com/IntelRealSense/realsense-ros/blob/7a87097c499e3b0b69518d54a8e7a9ac1924e87c/realsense2_description/urdf/_d435.urdf.xacro#L99) |

## Raw CoM records and reporting decisions

Raw values retain the previous root-anchor registration before Kabsch; original world coordinates also remain in the snapshots. Eligible findings above use the fitted transform into M. Excluded raw records below are diagnostic numbers, not findings. No CoM suppression applies to mass or principal inertia moments.

| Entity / quantity | Raw M | Raw S | Raw H | Raw H − M | Decision | M source | S source | H source |
|---|---|---|---|---|---|---|---|---|
| robot / total_com_registered | [0.00145113482, -0.000319326763, -0.01354119] | unavailable | [0, 0, 0] | [-0.00145113482, 0.000319326763, 0.01354119] | M/H: insufficient kinematic coverage | [aggregate inputs](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/realsense_d435i/d435i.xml#L1) | unavailable | [aggregate inputs](https://github.com/IntelRealSense/realsense-ros/blob/7a87097c499e3b0b69518d54a8e7a9ac1924e87c/realsense2_description/urdf/_d435i.urdf.xacro#L1) |
| d435i / com_registered | [0.00145113482, -0.000319326763, -0.01354119] | unavailable | [0, 0, 0] | [-0.00145113482, 0.000319326763, 0.01354119] | M/H: insufficient kinematic coverage | [geometry/inference input L41](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/realsense_d435i/d435i.xml#L41) | unavailable | [CoM/kinematic input L98](https://github.com/IntelRealSense/realsense-ros/blob/7a87097c499e3b0b69518d54a8e7a9ac1924e87c/realsense2_description/urdf/_d435.urdf.xacro#L98) |

## Mass accounting

Every contributing compiled body mass is listed here so total/subtree sums can be checked. Links point to explicit inertials or to geometry inputs when the compiler inferred a mass. CoM links identify inertial inputs; world coordinates additionally use the ancestor transforms and the registration recorded below.

| M body | M kg / source | S kg / source | H kg / source |
|---|---|---|---|
| d435i | 0.072 / [geometry/inference input L41](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/realsense_d435i/d435i.xml#L41) | unavailable | 0.072 / [input L97](https://github.com/IntelRealSense/realsense-ros/blob/7a87097c499e3b0b69518d54a8e7a9ac1924e87c/realsense2_description/urdf/_d435.urdf.xacro#L97) |
| upstream-only __drift_world | unavailable | unavailable | 0 / [expanded-source inputs; exact declaration unresolved](https://github.com/IntelRealSense/realsense-ros/blob/7a87097c499e3b0b69518d54a8e7a9ac1924e87c/realsense2_description/urdf/_d435i.urdf.xacro#L1) |
| upstream-only camera_bottom_screw_frame | unavailable | unavailable | 0 / [geometry/inference input L64](https://github.com/IntelRealSense/realsense-ros/blob/7a87097c499e3b0b69518d54a8e7a9ac1924e87c/realsense2_description/urdf/_d435.urdf.xacro#L64) |

## Coverage and unmatched elements

```json
{
  "mapping_h": {
    "bodies": {
      "d435i": "camera_link"
    },
    "joints": {},
    "body_methods": {
      "d435i": "unique kinematic subtree"
    },
    "joint_methods": {},
    "unmatched_m_bodies": [],
    "unmatched_upstream_bodies": [
      "__drift_world",
      "camera_bottom_screw_frame"
    ],
    "unmatched_m_joints": [],
    "unmatched_upstream_joints": [],
    "registration_anchor": {
      "M": "d435i",
      "H": "camera_link",
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
  "realsense2_description/meshes/d435.dae",
  "realsense2_description/urdf/_d435.urdf.xacro",
  "realsense2_description/urdf/_d435i.urdf.xacro",
  "realsense2_description/urdf/_d435i_imu_modules.urdf.xacro",
  "realsense2_description/urdf/_materials.urdf.xacro",
  "realsense2_description/urdf/_usb_plug.urdf.xacro"
]
```

## Self comparisons

```json
[
  {
    "file": "realsense_d435i/d435i.xml",
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
      "unknown": 1
    },
    "classifications_changed": 0,
    "finding_membership_changes": 0
  },
  "2": {
    "provenance_method": "unknown",
    "counts": {
      "unknown": 1
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
      "d435i"
    ],
    "assets_loaded": 9,
    "mesh_conversions": [],
    "nonphysical_normalizations": [],
    "xacro_arguments": {},
    "source_dependencies": [
      "realsense_d435i/d435i.xml",
      "realsense_d435i/assets/d435i_0.obj",
      "realsense_d435i/assets/d435i_1.obj",
      "realsense_d435i/assets/d435i_2.obj",
      "realsense_d435i/assets/d435i_3.obj",
      "realsense_d435i/assets/d435i_4.obj",
      "realsense_d435i/assets/d435i_5.obj",
      "realsense_d435i/assets/d435i_6.obj",
      "realsense_d435i/assets/d435i_7.obj",
      "realsense_d435i/assets/d435i_8.obj"
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
      "__drift_world",
      "camera_bottom_screw_frame"
    ],
    "assets_loaded": 1,
    "mesh_conversions": [
      {
        "file": "realsense2_description/meshes/d435.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      }
    ],
    "nonphysical_normalizations": [],
    "xacro_arguments": {
      "__macro_instance__": "sensor_d435i",
      "__macro_parameters__": "{'parent': '__drift_world'}",
      "__macro_origin__": "xyz=0 0 0 rpy=0 0 0"
    },
    "source_dependencies": [
      "realsense2_description/urdf/_d435.urdf.xacro",
      "realsense2_description/urdf/_d435i.urdf.xacro",
      "realsense2_description/urdf/_d435i_imu_modules.urdf.xacro",
      "realsense2_description/urdf/_materials.urdf.xacro",
      "realsense2_description/urdf/_usb_plug.urdf.xacro",
      "realsense2_description/meshes/d435.dae"
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
  "historical_snapshots_reused": 29,
  "primary_physics_unchanged": true,
  "source_matching": "original raw-value provenance criteria retained; kinematic guard applies to reported CoM"
}
```
