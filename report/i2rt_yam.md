# i2rt_yam

Status: **complete**. Provenance: **none**, confidence **none**.

No public revision matches all comparable quantities. Class: NO MATCHING SOURCE; never counted as STALE.

M: `https://github.com/google-deepmind/mujoco_menagerie`, `i2rt_yam/yam_linear_4310.xml`, commit `370c43965323c0944b433b202aac5058b5f907a9`.
H: `https://github.com/i2rt-robotics/i2rt`, `i2rt/robot_models/arm/yam/v1/yam.xml`, commit `61b1ebda80d0b3839843bb06fadf42b6b83bd3c4`.
S: unavailable. A machine-readable H can still be compared to M; no-match differences are never counted as STALE.

Limit semantics: MJCF effort values are supported actuator torque/force envelopes. URDF effort and velocity values are manufacturer declarations retained from XML; MuJoCo does not enforce those tags. Such declaration comparisons are explicitly distinct from compiled inertial/range quantities.


## Source evidence

```json
[
  {
    "url": "https://github.com/i2rt-robotics/i2rt",
    "document": "i2rt_yam/README.md",
    "commit": "370c43965323c0944b433b202aac5058b5f907a9",
    "current": true
  },
  {
    "url": "https://github.com/i2rt-robotics/i2rt/blob/main/robot_models/yam/yam.urdf",
    "document": "i2rt_yam/README.md",
    "commit": "370c43965323c0944b433b202aac5058b5f907a9",
    "current": true
  }
]
```


## README derivation evidence

Documentation labels are conservative: an automated documented label requires an explicit affected entity and quantity. Broader conversion notes are retained here for review.

> 2. Added the following to the URDF `<robot>` tag `<mujoco><compiler balanceinertia="true" discardvisual="false" fusestatic="false" strippath="false"/></mujoco>`.
> 7. Added armature based on reflected inertia values provided by the manufacturer.
> 2. Updated arm joint ranges and actuator PD gains to match the YAM Pro + `linear_4310` SDK configuration.
>    - Finger travel is 0 to 47.5 mm, with joint and control limits extending 5 mm past closed to allow grasp squeezing.
>    - Actuator PD gains and force limits match the hardware's 50 N per-pad grip force limit.
> 4. Added the wrist-mounted Intel RealSense D405 camera on `link_6` using extrinsics, intrinsics, and mass properties from I2RT's CAD station model.

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
| robot / total_mass | 4.06115073 | unavailable | 4.291978 | 0.23082727 | NO MATCHING SOURCE | [aggregate inputs](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/i2rt_yam/yam_linear_4310.xml#L1) | unavailable | [aggregate inputs](https://github.com/i2rt-robotics/i2rt/blob/61b1ebda80d0b3839843bb06fadf42b6b83bd3c4/i2rt/robot_models/arm/yam/v1/yam.xml#L1) |
| joint1 / force | 28 | unavailable | 10 | -18 | NO MATCHING SOURCE | [inherited actuator input L16](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/i2rt_yam/yam_linear_4310.xml#L16) | unavailable | [input L19](https://github.com/i2rt-robotics/i2rt/blob/61b1ebda80d0b3839843bb06fadf42b6b83bd3c4/i2rt/robot_models/arm/yam/v1/yam.xml#L19) |
| joint2 / force | 28 | unavailable | 10 | -18 | NO MATCHING SOURCE | [inherited actuator input L16](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/i2rt_yam/yam_linear_4310.xml#L16) | unavailable | [input L23](https://github.com/i2rt-robotics/i2rt/blob/61b1ebda80d0b3839843bb06fadf42b6b83bd3c4/i2rt/robot_models/arm/yam/v1/yam.xml#L23) |
| joint3 / force | 28 | unavailable | 10 | -18 | NO MATCHING SOURCE | [inherited actuator input L16](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/i2rt_yam/yam_linear_4310.xml#L16) | unavailable | [input L27](https://github.com/i2rt-robotics/i2rt/blob/61b1ebda80d0b3839843bb06fadf42b6b83bd3c4/i2rt/robot_models/arm/yam/v1/yam.xml#L27) |

## Raw CoM records and reporting decisions

Raw values retain the previous root-anchor registration before Kabsch; original world coordinates also remain in the snapshots. Eligible findings above use the fitted transform into M. Excluded raw records below are diagnostic numbers, not findings. No CoM suppression applies to mass or principal inertia moments.

| Entity / quantity | Raw M | Raw S | Raw H | Raw H − M | Decision | M source | S source | H source |
|---|---|---|---|---|---|---|---|---|
| robot / total_com_registered | [-0.0142259599, -1.86785985e-05, 0.142967357] | unavailable | [-0.04870585, 0.000246268872, 0.125997246] | [-0.0344798901, 0.000264947471, -0.0169701107] | M/H: insufficient kinematic coverage | [aggregate inputs](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/i2rt_yam/yam_linear_4310.xml#L1) | unavailable | [aggregate inputs](https://github.com/i2rt-robotics/i2rt/blob/61b1ebda80d0b3839843bb06fadf42b6b83bd3c4/i2rt/robot_models/arm/yam/v1/yam.xml#L1) |

## Mass accounting

Every contributing compiled body mass is listed here so total/subtree sums can be checked. Links point to explicit inertials or to geometry inputs when the compiler inferred a mass. CoM links identify inertial inputs; world coordinates additionally use the ancestor transforms and the registration recorded below.

| M body | M kg / source | S kg / source | H kg / source |
|---|---|---|---|
| arm | 0.218956442 / [geometry/inference input L66](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/i2rt_yam/yam_linear_4310.xml#L66) | unavailable | unmatched |
| link_1 | 0.12415 / [input L71](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/i2rt_yam/yam_linear_4310.xml#L71) | unavailable | unmatched |
| link_2 | 1.24434 / [input L76](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/i2rt_yam/yam_linear_4310.xml#L76) | unavailable | unmatched |
| link_3 | 0.853698 / [input L87](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/i2rt_yam/yam_linear_4310.xml#L87) | unavailable | unmatched |
| link_4 | 0.463511 / [input L98](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/i2rt_yam/yam_linear_4310.xml#L98) | unavailable | unmatched |
| link_5 | 0.350962 / [input L104](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/i2rt_yam/yam_linear_4310.xml#L104) | unavailable | unmatched |
| link_6 | 0.553219 / [input L110](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/i2rt_yam/yam_linear_4310.xml#L110) | unavailable | unmatched |
| left_finger | 0.0710042 / [input L124](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/i2rt_yam/yam_linear_4310.xml#L124) | unavailable | unmatched |
| left_pad | 0.000802944 / [geometry/inference input L151](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/i2rt_yam/yam_linear_4310.xml#L151) | unavailable | unmatched |
| right_finger | 0.0710042 / [input L164](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/i2rt_yam/yam_linear_4310.xml#L164) | unavailable | unmatched |
| right_pad | 0.000802944 / [geometry/inference input L192](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/i2rt_yam/yam_linear_4310.xml#L192) | unavailable | unmatched |
| wrist_camera | 0.1087 / [input L212](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/i2rt_yam/yam_linear_4310.xml#L212) | unavailable | unmatched |
| upstream-only base | unavailable | unavailable | 0.873654 / [input L15](https://github.com/i2rt-robotics/i2rt/blob/61b1ebda80d0b3839843bb06fadf42b6b83bd3c4/i2rt/robot_models/arm/yam/v1/yam.xml#L15) |
| upstream-only gripper | unavailable | unavailable | 1e-06 / [input L38](https://github.com/i2rt-robotics/i2rt/blob/61b1ebda80d0b3839843bb06fadf42b6b83bd3c4/i2rt/robot_models/arm/yam/v1/yam.xml#L38) |
| upstream-only link1 | unavailable | unavailable | 0.101218 / [input L18](https://github.com/i2rt-robotics/i2rt/blob/61b1ebda80d0b3839843bb06fadf42b6b83bd3c4/i2rt/robot_models/arm/yam/v1/yam.xml#L18) |
| upstream-only link2 | unavailable | unavailable | 1.46908 / [input L22](https://github.com/i2rt-robotics/i2rt/blob/61b1ebda80d0b3839843bb06fadf42b6b83bd3c4/i2rt/robot_models/arm/yam/v1/yam.xml#L22) |
| upstream-only link3 | unavailable | unavailable | 0.982553 / [input L26](https://github.com/i2rt-robotics/i2rt/blob/61b1ebda80d0b3839843bb06fadf42b6b83bd3c4/i2rt/robot_models/arm/yam/v1/yam.xml#L26) |
| upstream-only link4 | unavailable | unavailable | 0.462165 / [input L30](https://github.com/i2rt-robotics/i2rt/blob/61b1ebda80d0b3839843bb06fadf42b6b83bd3c4/i2rt/robot_models/arm/yam/v1/yam.xml#L30) |
| upstream-only link5 | unavailable | unavailable | 0.403307 / [input L34](https://github.com/i2rt-robotics/i2rt/blob/61b1ebda80d0b3839843bb06fadf42b6b83bd3c4/i2rt/robot_models/arm/yam/v1/yam.xml#L34) |

## Coverage and unmatched elements

```json
{
  "mapping_h": {
    "bodies": {},
    "joints": {
      "joint1": "joint1",
      "joint2": "joint2",
      "joint3": "joint3",
      "joint4": "joint4",
      "joint5": "joint5",
      "joint6": "joint6"
    },
    "body_methods": {},
    "joint_methods": {
      "joint1": "name",
      "joint2": "name",
      "joint3": "name",
      "joint4": "name",
      "joint5": "name",
      "joint6": "name"
    },
    "unmatched_m_bodies": [
      "arm",
      "left_finger",
      "left_pad",
      "link_1",
      "link_2",
      "link_3",
      "link_4",
      "link_5",
      "link_6",
      "right_finger",
      "right_pad",
      "wrist_camera"
    ],
    "unmatched_upstream_bodies": [
      "base",
      "gripper",
      "link1",
      "link2",
      "link3",
      "link4",
      "link5"
    ],
    "unmatched_m_joints": [
      "left_finger",
      "right_finger"
    ],
    "unmatched_upstream_joints": [],
    "registration_anchor": {
      "M": null,
      "H": null,
      "root_unmatched": true
    }
  },
  "mapping_s": null,
  "unavailable": [
    {
      "entity": "joint1",
      "other_entity": "joint1",
      "quantity": "effort",
      "tolerance": "limit",
      "m": 28.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "joint1",
      "other_entity": "joint1",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "joint2",
      "other_entity": "joint2",
      "quantity": "effort",
      "tolerance": "limit",
      "m": 28.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "joint2",
      "other_entity": "joint2",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "joint3",
      "other_entity": "joint3",
      "quantity": "effort",
      "tolerance": "limit",
      "m": 28.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "joint3",
      "other_entity": "joint3",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "joint4",
      "other_entity": "joint4",
      "quantity": "effort",
      "tolerance": "limit",
      "m": 10.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "joint4",
      "other_entity": "joint4",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "joint5",
      "other_entity": "joint5",
      "quantity": "effort",
      "tolerance": "limit",
      "m": 10.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "joint5",
      "other_entity": "joint5",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "joint6",
      "other_entity": "joint6",
      "quantity": "effort",
      "tolerance": "limit",
      "m": 10.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "joint6",
      "other_entity": "joint6",
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
| joint1 / effort | 28 | unavailable | unavailable |
| joint1 / velocity | unavailable | unavailable | unavailable |
| joint2 / effort | 28 | unavailable | unavailable |
| joint2 / velocity | unavailable | unavailable | unavailable |
| joint3 / effort | 28 | unavailable | unavailable |
| joint3 / velocity | unavailable | unavailable | unavailable |
| joint4 / effort | 10 | unavailable | unavailable |
| joint4 / velocity | unavailable | unavailable | unavailable |
| joint5 / effort | 10 | unavailable | unavailable |
| joint5 / velocity | unavailable | unavailable | unavailable |
| joint6 / effort | 10 | unavailable | unavailable |
| joint6 / velocity | unavailable | unavailable | unavailable |
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

## Self comparisons

```json
[
  {
    "file": "i2rt_yam/yam.xml",
    "status": "passed",
    "findings": 0
  },
  {
    "file": "i2rt_yam/yam_linear_4310.xml",
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
      "NO MATCHING SOURCE": 4
    },
    "classifications_changed": 0,
    "finding_membership_changes": 0
  },
  "2": {
    "provenance_method": "none",
    "counts": {
      "NO MATCHING SOURCE": 4
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
      "arm",
      "left_pad",
      "right_pad"
    ],
    "assets_loaded": 15,
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
  "historical_snapshots_reused": 2,
  "primary_physics_unchanged": true,
  "source_matching": "original raw-value provenance criteria retained; kinematic guard applies to reported CoM"
}
```
