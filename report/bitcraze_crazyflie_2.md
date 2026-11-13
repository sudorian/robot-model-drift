# bitcraze_crazyflie_2

Status: **complete**. Provenance: **dated match**, confidence **medium**.

Source selected using the ordered amended provenance rules.

M: `https://github.com/google-deepmind/mujoco_menagerie`, `bitcraze_crazyflie_2/cf2.xml`, commit `370c43965323c0944b433b202aac5058b5f907a9`.
H: `https://github.com/whoenig/crazyflie_ros`, `crazyflie_description/urdf/crazyflie2.urdf.xacro`, commit `df3ce76f700953cfa2794b8fd4628ea6b93c92c4`.
S: `3a8717c4ab31a7be19293abc08a8922e5c51a89f` (2016-10-30T03:33:03-04:00). Menagerie release/change: 2024-03-03T11:26:23+05:30.

Limit semantics: MJCF effort values are supported actuator torque/force envelopes. URDF effort and velocity values are manufacturer declarations retained from XML; MuJoCo does not enforce those tags. Such declaration comparisons are explicitly distinct from compiled inertial/range quantities.


## Source evidence

```json
[
  {
    "url": "https://github.com/kevinzakka/obj2mjcf",
    "document": "bitcraze_crazyflie_2/README.md",
    "commit": "370c43965323c0944b433b202aac5058b5f907a9",
    "current": true
  },
  {
    "url": "https://github.com/whoenig/crazyflie_ros",
    "document": "bitcraze_crazyflie_2/README.md",
    "commit": "370c43965323c0944b433b202aac5058b5f907a9",
    "current": true
  }
]
```


## README derivation evidence

Documentation labels are conservative: an automated documented label requires an explicit affected entity and quantity. Broader conversion notes are retained here for review.

> 4. Set the inertial properties to values obtained from the datasheet and [MIT's system identification](https://groups.csail.mit.edu/robotics-center/public_papers/Landry15.pdf)
>     * These properties are set via inertial tag i.e. `pos ="0 0 0" mass="0.027" diaginertia="2.3951e-5 2.3951e-5 3.2347e-5"`
> 5. Added combined thrust and body moments about a `site` placed at the inertial frame. The `ctrlrange` limits are currently arbitrary and need to be further tuned.

## Kinematics consistency

A proper Kabsch rigid transform aligns all matched zero-pose body origins. The maximum per-origin residual and signed hinge/slide axis angles determine whether CoM can be compared; RMS is also recorded. Fewer than three non-collinear origins give insufficient kinematic coverage. CoM records that fail either required M/H or M/S check are excluded from counts and largest discrepancies. Masses, principal moments and raw joint ranges remain unchanged; a flagged range still requires convention review.

| Pair | Status | Origins / rank | RMS / maximum mm | Disagreeing / checked axes |
|---|---|---:|---:|---:|
| M/H | insufficient kinematic coverage | 1 / 0 | 0 / 0 | 0 / 0 |
| M/S | insufficient kinematic coverage | 1 / 0 | 0 / 0 | 0 / 0 |

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
    "anchor_m": "cf2",
    "anchor_other": "base_link",
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
      "cf2": 0.0
    },
    "reason": "Fewer than three non-collinear matched origins; fitted rotation is underdetermined"
  },
  "M/S": {
    "status": "insufficient kinematic coverage",
    "matched_body_origins": 1,
    "position_threshold_m": 0.005,
    "axis_threshold_rad": 0.005,
    "residual_definition": "maximum Euclidean residual over matched body origins; Kabsch minimizes RMS, which is also recorded",
    "coordinate_frames": "each snapshot registered to its matched report anchor",
    "anchor_m": "cf2",
    "anchor_other": "base_link",
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
      "cf2": 0.0
    },
    "reason": "Fewer than three non-collinear matched origins; fitted rotation is underdetermined"
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
| robot / total_com_registered | [0, 0, 0] | [0, 0, 0] | [0, 0, 0] | [0, 0, 0] | M/H: insufficient kinematic coverage; M/S: insufficient kinematic coverage | [aggregate inputs](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/bitcraze_crazyflie_2/cf2.xml#L1) | [aggregate inputs](https://github.com/whoenig/crazyflie_ros/blob/3a8717c4ab31a7be19293abc08a8922e5c51a89f/crazyflie_description/urdf/crazyflie2.urdf.xacro#L1) | [aggregate inputs](https://github.com/whoenig/crazyflie_ros/blob/df3ce76f700953cfa2794b8fd4628ea6b93c92c4/crazyflie_description/urdf/crazyflie2.urdf.xacro#L1) |
| cf2 / com_registered | [0, 0, 0] | [0, 0, 0] | [0, 0, 0] | [0, 0, 0] | M/H: insufficient kinematic coverage; M/S: insufficient kinematic coverage | [CoM/kinematic input L71](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/bitcraze_crazyflie_2/cf2.xml#L71) | [CoM/kinematic input L11](https://github.com/whoenig/crazyflie_ros/blob/3a8717c4ab31a7be19293abc08a8922e5c51a89f/crazyflie_description/urdf/crazyflie2.urdf.xacro#L11) | [CoM/kinematic input L11](https://github.com/whoenig/crazyflie_ros/blob/df3ce76f700953cfa2794b8fd4628ea6b93c92c4/crazyflie_description/urdf/crazyflie2.urdf.xacro#L11) |

## Mass accounting

Every contributing compiled body mass is listed here so total/subtree sums can be checked. Links point to explicit inertials or to geometry inputs when the compiler inferred a mass. CoM links identify inertial inputs; world coordinates additionally use the ancestor transforms and the registration recorded below.

| M body | M kg / source | S kg / source | H kg / source |
|---|---|---|---|
| cf2 | 0.027 / [input L71](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/bitcraze_crazyflie_2/cf2.xml#L71) | 0.027 / [input L10](https://github.com/whoenig/crazyflie_ros/blob/3a8717c4ab31a7be19293abc08a8922e5c51a89f/crazyflie_description/urdf/crazyflie2.urdf.xacro#L10) | 0.027 / [input L10](https://github.com/whoenig/crazyflie_ros/blob/df3ce76f700953cfa2794b8fd4628ea6b93c92c4/crazyflie_description/urdf/crazyflie2.urdf.xacro#L10) |

## Coverage and unmatched elements

```json
{
  "mapping_h": {
    "bodies": {
      "cf2": "base_link"
    },
    "joints": {},
    "body_methods": {
      "cf2": "unique kinematic subtree"
    },
    "joint_methods": {},
    "unmatched_m_bodies": [],
    "unmatched_upstream_bodies": [],
    "unmatched_m_joints": [],
    "unmatched_upstream_joints": [],
    "registration_anchor": {
      "M": "cf2",
      "H": "base_link",
      "root_unmatched": false
    }
  },
  "mapping_s": {
    "bodies": {
      "cf2": "base_link"
    },
    "joints": {},
    "body_methods": {
      "cf2": "unique kinematic subtree"
    },
    "joint_methods": {},
    "unmatched_m_bodies": [],
    "unmatched_upstream_bodies": [],
    "unmatched_m_joints": [],
    "unmatched_upstream_joints": [],
    "registration_anchor": {
      "M": "cf2",
      "S": "base_link"
    }
  },
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
  "crazyflie_description/urdf/crazyflie2.urdf.xacro"
]
```

## Self comparisons

```json
[
  {
    "file": "bitcraze_crazyflie_2/cf2.xml",
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
    "geometry_stripped": true,
    "missing_explicit_inertials": [],
    "assets_loaded": 0,
    "mesh_conversions": [],
    "nonphysical_normalizations": [],
    "xacro_arguments": {},
    "source_dependencies": [
      "bitcraze_crazyflie_2/cf2.xml"
    ],
    "registration": {
      "translation": [
        0.0,
        0.0,
        0.1
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
    "geometry_stripped": true,
    "missing_explicit_inertials": [],
    "assets_loaded": 0,
    "mesh_conversions": [],
    "nonphysical_normalizations": [],
    "xacro_arguments": {},
    "source_dependencies": [
      "crazyflie_description/urdf/crazyflie2.urdf.xacro"
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
  },
  "S": {
    "geometry_stripped": true,
    "missing_explicit_inertials": [],
    "assets_loaded": 0,
    "mesh_conversions": [],
    "nonphysical_normalizations": [],
    "xacro_arguments": {},
    "source_dependencies": [
      "crazyflie_description/urdf/crazyflie2.urdf.xacro"
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
    "M",
    "S"
  ],
  "self_variants_recompiled": 1,
  "historical_snapshots_reused": 3,
  "primary_physics_unchanged": true,
  "source_matching": "original raw-value provenance criteria retained; kinematic guard applies to reported CoM"
}
```
