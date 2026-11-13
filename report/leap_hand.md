# leap_hand

Status: **complete**. Provenance: **none**, confidence **none**.

No public revision matches all comparable quantities. Class: NO MATCHING SOURCE; never counted as STALE.

M: `https://github.com/google-deepmind/mujoco_menagerie`, `leap_hand/right_hand.xml`, commit `370c43965323c0944b433b202aac5058b5f907a9`.
H: `https://github.com/leap-hand/LEAP_Hand_Sim`, `assets/leap_hand/robot.urdf`, commit `150bc3d4b61fd6619193ba5a8ef209f3609ced89`.
S: unavailable. A machine-readable H can still be compared to M; no-match differences are never counted as STALE.

Limit semantics: MJCF effort values are supported actuator torque/force envelopes. URDF effort and velocity values are manufacturer declarations retained from XML; MuJoCo does not enforce those tags. Such declaration comparisons are explicitly distinct from compiled inertial/range quantities.


## Source evidence

```json
[
  {
    "url": "https://github.com/dexsuite/dex-urdf/tree/main/robots/hands/leap_hand",
    "document": "leap_hand/README.md",
    "commit": "370c43965323c0944b433b202aac5058b5f907a9",
    "current": true
  },
  {
    "url": "https://github.com/leap-hand/LEAP_Hand_Sim/blob/master/assets/leap_hand/robot.urdf",
    "document": "leap_hand/README.md",
    "commit": "f59b989dea80a523b0e0b0fbe550c664939c6376",
    "current": false
  }
]
```


## README derivation evidence

Documentation labels are conservative: an automated documented label requires an explicit affected entity and quantity. Broader conversion notes are retained here for review.

> 2. Run it through drake's fix_inertia tool (v. 1.30.0)
>       <compiler balanceinertia="true" discardvisual="false" fusestatic="false"/>
>     python -m mujoco.viewer --mjcf=<name_of_inertia_fixed_urdf>.urdf
> 10. Delete the actuatorfrcrange field for all joints.

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
    "anchor_m": "palm",
    "anchor_other": "palm_lower",
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
      "palm": 0.0
    },
    "reason": "Fewer than three non-collinear matched origins; fitted rotation is underdetermined"
  }
}
```


## Every reported quantity difference

Counts are quantity records, including correlated total/subtree/body mass records; they are not independent robot defects.

| Entity / quantity | M | S | H | H − M | Class | M source | S source | H source |
|---|---|---|---|---|---|---|---|---|
| palm / principal_moments | [0.000180736, 0.000304759, 0.000407345] | unavailable | [0.000260867602, 0.0003540762, 0.000529322198] | [8.01316016e-05, 4.93172e-05, 0.000121977198] | NO MATCHING SOURCE | [inertia input L166](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/leap_hand/right_hand.xml#L166) | unavailable | [inertia input L21](https://github.com/leap-hand/LEAP_Hand_Sim/blob/150bc3d4b61fd6619193ba5a8ef209f3609ced89/assets/leap_hand/robot.urdf#L21) |

## Raw CoM records and reporting decisions

Raw values retain the previous root-anchor registration before Kabsch; original world coordinates also remain in the snapshots. Eligible findings above use the fitted transform into M. Excluded raw records below are diagnostic numbers, not findings. No CoM suppression applies to mass or principal inertia moments.

| Entity / quantity | Raw M | Raw S | Raw H | Raw H − M | Decision | M source | S source | H source |
|---|---|---|---|---|---|---|---|---|
| robot / total_com_registered | [-0.00136602413, -0.0242739233, -0.0120285105] | unavailable | [0.00194533316, -0.00697232189, -0.0101450456] | [0.00331135729, 0.0173016014, 0.00188346493] | M/H: insufficient kinematic coverage | [aggregate inputs](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/leap_hand/right_hand.xml#L1) | unavailable | [aggregate inputs](https://github.com/leap-hand/LEAP_Hand_Sim/blob/150bc3d4b61fd6619193ba5a8ef209f3609ced89/assets/leap_hand/robot.urdf#L1) |
| palm / com_registered | [-0.049542, -0.042914, -0.010227] | unavailable | [0, 0, 0] | [0.049542, 0.042914, 0.010227] | M/H: insufficient kinematic coverage | [CoM/kinematic input L166](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/leap_hand/right_hand.xml#L166) | unavailable | [CoM/kinematic input L19](https://github.com/leap-hand/LEAP_Hand_Sim/blob/150bc3d4b61fd6619193ba5a8ef209f3609ced89/assets/leap_hand/robot.urdf#L19) |

## Mass accounting

Every contributing compiled body mass is listed here so total/subtree sums can be checked. Links point to explicit inertials or to geometry inputs when the compiler inferred a mass. CoM links identify inertial inputs; world coordinates additionally use the ancestor transforms and the registration recorded below.

| M body | M kg / source | S kg / source | H kg / source |
|---|---|---|---|
| palm | 0.237 / [input L166](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/leap_hand/right_hand.xml#L166) | unavailable | 0.237 / [input L20](https://github.com/leap-hand/LEAP_Hand_Sim/blob/150bc3d4b61fd6619193ba5a8ef209f3609ced89/assets/leap_hand/robot.urdf#L20) |
| if_bs | 0.044 / [input L184](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/leap_hand/right_hand.xml#L184) | unavailable | unmatched |
| if_px | 0.032 / [input L196](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/leap_hand/right_hand.xml#L196) | unavailable | unmatched |
| if_md | 0.037 / [input L205](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/leap_hand/right_hand.xml#L205) | unavailable | unmatched |
| if_ds | 0.016 / [input L218](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/leap_hand/right_hand.xml#L218) | unavailable | unmatched |
| mf_bs | 0.044 / [input L237](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/leap_hand/right_hand.xml#L237) | unavailable | unmatched |
| mf_px | 0.032 / [input L249](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/leap_hand/right_hand.xml#L249) | unavailable | unmatched |
| mf_md | 0.037 / [input L258](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/leap_hand/right_hand.xml#L258) | unavailable | unmatched |
| mf_ds | 0.016 / [input L271](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/leap_hand/right_hand.xml#L271) | unavailable | unmatched |
| rf_bs | 0.044 / [input L290](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/leap_hand/right_hand.xml#L290) | unavailable | unmatched |
| rf_px | 0.032 / [input L302](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/leap_hand/right_hand.xml#L302) | unavailable | unmatched |
| rf_md | 0.037 / [input L311](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/leap_hand/right_hand.xml#L311) | unavailable | unmatched |
| rf_ds | 0.016 / [input L324](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/leap_hand/right_hand.xml#L324) | unavailable | unmatched |
| th_mp | 0.032 / [input L343](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/leap_hand/right_hand.xml#L343) | unavailable | unmatched |
| th_bs | 0.003 / [input L352](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/leap_hand/right_hand.xml#L352) | unavailable | unmatched |
| th_px | 0.038 / [input L362](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/leap_hand/right_hand.xml#L362) | unavailable | unmatched |
| th_ds | 0.049 / [input L374](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/leap_hand/right_hand.xml#L374) | unavailable | unmatched |
| upstream-only dip | unavailable | unavailable | 0.037 / [input L89](https://github.com/leap-hand/LEAP_Hand_Sim/blob/150bc3d4b61fd6619193ba5a8ef209f3609ced89/assets/leap_hand/robot.urdf#L89) |
| upstream-only dip_2 | unavailable | unavailable | 0.037 / [input L217](https://github.com/leap-hand/LEAP_Hand_Sim/blob/150bc3d4b61fd6619193ba5a8ef209f3609ced89/assets/leap_hand/robot.urdf#L217) |
| upstream-only dip_3 | unavailable | unavailable | 0.037 / [input L345](https://github.com/leap-hand/LEAP_Hand_Sim/blob/150bc3d4b61fd6619193ba5a8ef209f3609ced89/assets/leap_hand/robot.urdf#L345) |
| upstream-only fingertip | unavailable | unavailable | 0.016 / [input L112](https://github.com/leap-hand/LEAP_Hand_Sim/blob/150bc3d4b61fd6619193ba5a8ef209f3609ced89/assets/leap_hand/robot.urdf#L112) |
| upstream-only fingertip_2 | unavailable | unavailable | 0.016 / [input L240](https://github.com/leap-hand/LEAP_Hand_Sim/blob/150bc3d4b61fd6619193ba5a8ef209f3609ced89/assets/leap_hand/robot.urdf#L240) |
| upstream-only fingertip_3 | unavailable | unavailable | 0.016 / [input L368](https://github.com/leap-hand/LEAP_Hand_Sim/blob/150bc3d4b61fd6619193ba5a8ef209f3609ced89/assets/leap_hand/robot.urdf#L368) |
| upstream-only mcp_joint | unavailable | unavailable | 0.044 / [input L43](https://github.com/leap-hand/LEAP_Hand_Sim/blob/150bc3d4b61fd6619193ba5a8ef209f3609ced89/assets/leap_hand/robot.urdf#L43) |
| upstream-only mcp_joint_2 | unavailable | unavailable | 0.044 / [input L171](https://github.com/leap-hand/LEAP_Hand_Sim/blob/150bc3d4b61fd6619193ba5a8ef209f3609ced89/assets/leap_hand/robot.urdf#L171) |
| upstream-only mcp_joint_3 | unavailable | unavailable | 0.044 / [input L299](https://github.com/leap-hand/LEAP_Hand_Sim/blob/150bc3d4b61fd6619193ba5a8ef209f3609ced89/assets/leap_hand/robot.urdf#L299) |
| upstream-only pip | unavailable | unavailable | 0.032 / [input L66](https://github.com/leap-hand/LEAP_Hand_Sim/blob/150bc3d4b61fd6619193ba5a8ef209f3609ced89/assets/leap_hand/robot.urdf#L66) |
| upstream-only pip_2 | unavailable | unavailable | 0.032 / [input L194](https://github.com/leap-hand/LEAP_Hand_Sim/blob/150bc3d4b61fd6619193ba5a8ef209f3609ced89/assets/leap_hand/robot.urdf#L194) |
| upstream-only pip_3 | unavailable | unavailable | 0.032 / [input L322](https://github.com/leap-hand/LEAP_Hand_Sim/blob/150bc3d4b61fd6619193ba5a8ef209f3609ced89/assets/leap_hand/robot.urdf#L322) |
| upstream-only pip_4 | unavailable | unavailable | 0.032 / [input L427](https://github.com/leap-hand/LEAP_Hand_Sim/blob/150bc3d4b61fd6619193ba5a8ef209f3609ced89/assets/leap_hand/robot.urdf#L427) |
| upstream-only thumb_dip | unavailable | unavailable | 0.038 / [input L473](https://github.com/leap-hand/LEAP_Hand_Sim/blob/150bc3d4b61fd6619193ba5a8ef209f3609ced89/assets/leap_hand/robot.urdf#L473) |
| upstream-only thumb_fingertip | unavailable | unavailable | 0.049 / [input L496](https://github.com/leap-hand/LEAP_Hand_Sim/blob/150bc3d4b61fd6619193ba5a8ef209f3609ced89/assets/leap_hand/robot.urdf#L496) |
| upstream-only thumb_pip | unavailable | unavailable | 0.003 / [input L450](https://github.com/leap-hand/LEAP_Hand_Sim/blob/150bc3d4b61fd6619193ba5a8ef209f3609ced89/assets/leap_hand/robot.urdf#L450) |

## Coverage and unmatched elements

```json
{
  "mapping_h": {
    "bodies": {
      "palm": "palm_lower"
    },
    "joints": {},
    "body_methods": {
      "palm": "unique kinematic subtree"
    },
    "joint_methods": {},
    "unmatched_m_bodies": [
      "if_bs",
      "if_ds",
      "if_md",
      "if_px",
      "mf_bs",
      "mf_ds",
      "mf_md",
      "mf_px",
      "rf_bs",
      "rf_ds",
      "rf_md",
      "rf_px",
      "th_bs",
      "th_ds",
      "th_mp",
      "th_px"
    ],
    "unmatched_upstream_bodies": [
      "dip",
      "dip_2",
      "dip_3",
      "fingertip",
      "fingertip_2",
      "fingertip_3",
      "mcp_joint",
      "mcp_joint_2",
      "mcp_joint_3",
      "pip",
      "pip_2",
      "pip_3",
      "pip_4",
      "thumb_dip",
      "thumb_fingertip",
      "thumb_pip"
    ],
    "unmatched_m_joints": [
      "if_dip",
      "if_mcp",
      "if_pip",
      "if_rot",
      "mf_dip",
      "mf_mcp",
      "mf_pip",
      "mf_rot",
      "rf_dip",
      "rf_mcp",
      "rf_pip",
      "rf_rot",
      "th_axl",
      "th_cmc",
      "th_ipl",
      "th_mcp"
    ],
    "unmatched_upstream_joints": [
      "0",
      "1",
      "10",
      "11",
      "12",
      "13",
      "14",
      "15",
      "2",
      "3",
      "4",
      "5",
      "6",
      "7",
      "8",
      "9"
    ],
    "registration_anchor": {
      "M": "palm",
      "H": "palm_lower",
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
[
  "https://github.com/dexsuite/dex-urdf robots/hands/leap_hand/leap_hand_left_glb.urdf at f5e7132f22108164577fea4c25ef99b5cc0e1900: ValueError: Error: unknown or unsupported mesh file: 'resource_10.glb'\nElement name 'resource_10', id 0",
  "https://github.com/dexsuite/dex-urdf robots/hands/leap_hand/leap_hand_right_glb.urdf at f5e7132f22108164577fea4c25ef99b5cc0e1900: ValueError: Error: unknown or unsupported mesh file: 'resource_10.glb'\nElement name 'resource_10', id 0"
]
```

## Self comparisons

```json
[
  {
    "file": "leap_hand/left_hand.xml",
    "status": "passed",
    "findings": 0
  },
  {
    "file": "leap_hand/right_hand.xml",
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
    "geometry_stripped": true,
    "missing_explicit_inertials": [],
    "assets_loaded": 0,
    "mesh_conversions": [],
    "xacro_arguments": {},
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
          -1.0,
          0.0
        ],
        [
          0.0,
          0.0,
          -1.0
        ]
      ]
    }
  },
  "H": {
    "geometry_stripped": true,
    "missing_explicit_inertials": [],
    "assets_loaded": 0,
    "mesh_conversions": [],
    "xacro_arguments": {},
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
    }
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
  "historical_snapshots_reused": 1,
  "primary_physics_unchanged": true,
  "source_matching": "original raw-value provenance criteria retained; kinematic guard applies to reported CoM"
}
```
