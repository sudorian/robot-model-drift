# wonik_allegro

Status: **partial history**. Provenance: **unknown**, confidence **incomplete**.

Unresolved historical compilation prevents selecting or rejecting a matching source. Pairwise M/H differences are reported with unknown provenance.

M: `https://github.com/google-deepmind/mujoco_menagerie`, `wonik_allegro/left_hand.xml`, commit `370c43965323c0944b433b202aac5058b5f907a9`.
H: `https://github.com/simlabrobotics/allegro_hand_ros`, `allegro_hand_description/allegro_hand_description_right.urdf`, commit `296ef6bae4b535ffb91420237cdc8a87f6e9f6df`.
S: unavailable. A machine-readable H can still be compared to M; no-match differences are never counted as STALE.

Limit semantics: MJCF effort values are supported actuator torque/force envelopes. URDF effort and velocity values are manufacturer declarations retained from XML; MuJoCo does not enforce those tags. Such declaration comparisons are explicitly distinct from compiled inertial/range quantities.


## Source evidence

```json
[
  {
    "url": "https://github.com/simlabrobotics/allegro_hand_ros/blob/master/allegro_hand_description/",
    "document": "wonik_allegro/README.md",
    "commit": "370c43965323c0944b433b202aac5058b5f907a9",
    "current": true
  },
  {
    "url": "https://github.com/simlabrobotics/allegro_hand_ros/blob/master/allegro_hand_description/allegro_hand_description_right.urdf",
    "document": "wonik_allegro/README.md",
    "commit": "370c43965323c0944b433b202aac5058b5f907a9",
    "current": true
  }
]
```


## README derivation evidence

Documentation labels are conservative: an automated documented label requires an explicit affected entity and quantity. Broader conversion notes are retained here for review.

> 7. Scaled the global density to be `1000 * actual_mass / current_mass`.

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
| robot / total_mass | 0.646556334 | unavailable | 0.801471618 | 0.154915284 | unknown | [aggregate inputs](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/wonik_allegro/left_hand.xml#L1) | unavailable | [aggregate inputs](https://github.com/simlabrobotics/allegro_hand_ros/blob/296ef6bae4b535ffb91420237cdc8a87f6e9f6df/allegro_hand_description/allegro_hand_description_right.urdf#L1) |
| palm / mass | 0.351587488 | unavailable | 0.437988 | 0.0864005124 | unknown | [geometry/inference input L127](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/wonik_allegro/left_hand.xml#L127) | unavailable | [geometry/inference input L25](https://github.com/simlabrobotics/allegro_hand_ros/blob/296ef6bae4b535ffb91420237cdc8a87f6e9f6df/allegro_hand_description/allegro_hand_description_right.urdf#L25) |
| palm / subtree_mass | 0.646556334 | unavailable | 0.801471618 | 0.154915284 | unknown | [subtree root L127](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/wonik_allegro/left_hand.xml#L127) | unavailable | [subtree root L25](https://github.com/simlabrobotics/allegro_hand_ros/blob/296ef6bae4b535ffb91420237cdc8a87f6e9f6df/allegro_hand_description/allegro_hand_description_right.urdf#L25) |
| palm / principal_moments | [0.000243738325, 0.000300982213, 0.000448127295] | unavailable | [0.00039016117, 0.000526813426, 0.000795459206] | [0.000146422845, 0.000225831213, 0.000347331911] | unknown | [geometry/inference input L127](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/wonik_allegro/left_hand.xml#L127) | unavailable | [geometry/inference input L25](https://github.com/simlabrobotics/allegro_hand_ros/blob/296ef6bae4b535ffb91420237cdc8a87f6e9f6df/allegro_hand_description/allegro_hand_description_right.urdf#L25) |

## Raw CoM records and reporting decisions

Raw values retain the previous root-anchor registration before Kabsch; original world coordinates also remain in the snapshots. Eligible findings above use the fitted transform into M. Excluded raw records below are diagnostic numbers, not findings. No CoM suppression applies to mass or principal inertia moments.

| Entity / quantity | Raw M | Raw S | Raw H | Raw H − M | Decision | M source | S source | H source |
|---|---|---|---|---|---|---|---|---|
| robot / total_com_registered | [-0.00667469828, -0.00900809656, -0.0108432532] | unavailable | [-0.00682612029, 0.0121478384, -0.0154195979] | [-0.00015142201, 0.021155935, -0.00457634475] | M/H: insufficient kinematic coverage | [aggregate inputs](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/wonik_allegro/left_hand.xml#L1) | unavailable | [aggregate inputs](https://github.com/simlabrobotics/allegro_hand_ros/blob/296ef6bae4b535ffb91420237cdc8a87f6e9f6df/allegro_hand_description/allegro_hand_description_right.urdf#L1) |
| palm / com_registered | [-0.00898160187, 0.00395364658, -0.0402573276] | unavailable | [-0.0093, 0, -0.0475] | [-0.000318398133, -0.00395364658, -0.00724267238] | M/H: insufficient kinematic coverage | [geometry/inference input L127](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/wonik_allegro/left_hand.xml#L127) | unavailable | [geometry/inference input L25](https://github.com/simlabrobotics/allegro_hand_ros/blob/296ef6bae4b535ffb91420237cdc8a87f6e9f6df/allegro_hand_description/allegro_hand_description_right.urdf#L25) |

## Mass accounting

Every contributing compiled body mass is listed here so total/subtree sums can be checked. Links point to explicit inertials or to geometry inputs when the compiler inferred a mass. CoM links identify inertial inputs; world coordinates additionally use the ancestor transforms and the registration recorded below.

| M body | M kg / source | S kg / source | H kg / source |
|---|---|---|---|
| palm | 0.351587488 / [geometry/inference input L127](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/wonik_allegro/left_hand.xml#L127) | unavailable | 0.437988 / [geometry/inference input L25](https://github.com/simlabrobotics/allegro_hand_ros/blob/296ef6bae4b535ffb91420237cdc8a87f6e9f6df/allegro_hand_description/allegro_hand_description_right.urdf#L25) |
| rf_base | 0.00723201635 / [geometry/inference input L131](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/wonik_allegro/left_hand.xml#L131) | unavailable | unmatched |
| rf_proximal | 0.027276123 / [geometry/inference input L135](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/wonik_allegro/left_hand.xml#L135) | unavailable | unmatched |
| rf_medial | 0.0184637457 / [geometry/inference input L139](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/wonik_allegro/left_hand.xml#L139) | unavailable | unmatched |
| rf_distal | 0.00751231169 / [geometry/inference input L143](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/wonik_allegro/left_hand.xml#L143) | unavailable | unmatched |
| rf_tip | 0.00684452138 / [geometry/inference input L147](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/wonik_allegro/left_hand.xml#L147) | unavailable | unmatched |
| mf_base | 0.00723201635 / [geometry/inference input L156](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/wonik_allegro/left_hand.xml#L156) | unavailable | unmatched |
| mf_proximal | 0.027276123 / [geometry/inference input L160](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/wonik_allegro/left_hand.xml#L160) | unavailable | unmatched |
| mf_medial | 0.0184637457 / [geometry/inference input L164](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/wonik_allegro/left_hand.xml#L164) | unavailable | unmatched |
| mf_distal | 0.00751231169 / [geometry/inference input L168](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/wonik_allegro/left_hand.xml#L168) | unavailable | unmatched |
| mf_tip | 0.00684452138 / [geometry/inference input L172](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/wonik_allegro/left_hand.xml#L172) | unavailable | unmatched |
| ff_base | 0.00723201635 / [geometry/inference input L181](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/wonik_allegro/left_hand.xml#L181) | unavailable | unmatched |
| ff_proximal | 0.027276123 / [geometry/inference input L185](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/wonik_allegro/left_hand.xml#L185) | unavailable | unmatched |
| ff_medial | 0.0184637457 / [geometry/inference input L189](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/wonik_allegro/left_hand.xml#L189) | unavailable | unmatched |
| ff_distal | 0.00751231169 / [geometry/inference input L193](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/wonik_allegro/left_hand.xml#L193) | unavailable | unmatched |
| ff_tip | 0.00684452138 / [geometry/inference input L197](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/wonik_allegro/left_hand.xml#L197) | unavailable | unmatched |
| th_base | 0.0400878892 / [geometry/inference input L206](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/wonik_allegro/left_hand.xml#L206) | unavailable | unmatched |
| th_proximal | 0.0072193122 / [geometry/inference input L210](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/wonik_allegro/left_hand.xml#L210) | unavailable | unmatched |
| th_medial | 0.0224964724 / [geometry/inference input L214](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/wonik_allegro/left_hand.xml#L214) | unavailable | unmatched |
| th_distal | 0.0163344967 / [geometry/inference input L218](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/wonik_allegro/left_hand.xml#L218) | unavailable | unmatched |
| th_tip | 0.00684452138 / [geometry/inference input L222](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/wonik_allegro/left_hand.xml#L222) | unavailable | unmatched |
| upstream-only link_0.0 | unavailable | unavailable | 0.0088396 / [geometry/inference input L49](https://github.com/simlabrobotics/allegro_hand_ros/blob/296ef6bae4b535ffb91420237cdc8a87f6e9f6df/allegro_hand_description/allegro_hand_description_right.urdf#L49) |
| upstream-only link_1.0 | unavailable | unavailable | 0.029106 / [geometry/inference input L70](https://github.com/simlabrobotics/allegro_hand_ros/blob/296ef6bae4b535ffb91420237cdc8a87f6e9f6df/allegro_hand_description/allegro_hand_description_right.urdf#L70) |
| upstream-only link_10.0 | unavailable | unavailable | 0.0206976 / [geometry/inference input L299](https://github.com/simlabrobotics/allegro_hand_ros/blob/296ef6bae4b535ffb91420237cdc8a87f6e9f6df/allegro_hand_description/allegro_hand_description_right.urdf#L299) |
| upstream-only link_11.0 | unavailable | unavailable | 0.0143913 / [geometry/inference input L320](https://github.com/simlabrobotics/allegro_hand_ros/blob/296ef6bae4b535ffb91420237cdc8a87f6e9f6df/allegro_hand_description/allegro_hand_description_right.urdf#L320) |
| upstream-only link_11.0_tip | unavailable | unavailable | 0.00723822947 / [geometry/inference input L341](https://github.com/simlabrobotics/allegro_hand_ros/blob/296ef6bae4b535ffb91420237cdc8a87f6e9f6df/allegro_hand_description/allegro_hand_description_right.urdf#L341) |
| upstream-only link_12.0 | unavailable | unavailable | 0.0553826 / [geometry/inference input L362](https://github.com/simlabrobotics/allegro_hand_ros/blob/296ef6bae4b535ffb91420237cdc8a87f6e9f6df/allegro_hand_description/allegro_hand_description_right.urdf#L362) |
| upstream-only link_13.0 | unavailable | unavailable | 0.0095403 / [geometry/inference input L391](https://github.com/simlabrobotics/allegro_hand_ros/blob/296ef6bae4b535ffb91420237cdc8a87f6e9f6df/allegro_hand_description/allegro_hand_description_right.urdf#L391) |
| upstream-only link_14.0 | unavailable | unavailable | 0.0277046 / [geometry/inference input L417](https://github.com/simlabrobotics/allegro_hand_ros/blob/296ef6bae4b535ffb91420237cdc8a87f6e9f6df/allegro_hand_description/allegro_hand_description_right.urdf#L417) |
| upstream-only link_15.0 | unavailable | unavailable | 0.0227997 / [geometry/inference input L439](https://github.com/simlabrobotics/allegro_hand_ros/blob/296ef6bae4b535ffb91420237cdc8a87f6e9f6df/allegro_hand_description/allegro_hand_description_right.urdf#L439) |
| upstream-only link_15.0_tip | unavailable | unavailable | 0.00723822947 / [geometry/inference input L461](https://github.com/simlabrobotics/allegro_hand_ros/blob/296ef6bae4b535ffb91420237cdc8a87f6e9f6df/allegro_hand_description/allegro_hand_description_right.urdf#L461) |
| upstream-only link_2.0 | unavailable | unavailable | 0.0206976 / [geometry/inference input L91](https://github.com/simlabrobotics/allegro_hand_ros/blob/296ef6bae4b535ffb91420237cdc8a87f6e9f6df/allegro_hand_description/allegro_hand_description_right.urdf#L91) |
| upstream-only link_3.0 | unavailable | unavailable | 0.0143913 / [geometry/inference input L112](https://github.com/simlabrobotics/allegro_hand_ros/blob/296ef6bae4b535ffb91420237cdc8a87f6e9f6df/allegro_hand_description/allegro_hand_description_right.urdf#L112) |
| upstream-only link_3.0_tip | unavailable | unavailable | 0.00723822947 / [geometry/inference input L133](https://github.com/simlabrobotics/allegro_hand_ros/blob/296ef6bae4b535ffb91420237cdc8a87f6e9f6df/allegro_hand_description/allegro_hand_description_right.urdf#L133) |
| upstream-only link_4.0 | unavailable | unavailable | 0.0088396 / [geometry/inference input L153](https://github.com/simlabrobotics/allegro_hand_ros/blob/296ef6bae4b535ffb91420237cdc8a87f6e9f6df/allegro_hand_description/allegro_hand_description_right.urdf#L153) |
| upstream-only link_5.0 | unavailable | unavailable | 0.029106 / [geometry/inference input L174](https://github.com/simlabrobotics/allegro_hand_ros/blob/296ef6bae4b535ffb91420237cdc8a87f6e9f6df/allegro_hand_description/allegro_hand_description_right.urdf#L174) |
| upstream-only link_6.0 | unavailable | unavailable | 0.0206976 / [geometry/inference input L195](https://github.com/simlabrobotics/allegro_hand_ros/blob/296ef6bae4b535ffb91420237cdc8a87f6e9f6df/allegro_hand_description/allegro_hand_description_right.urdf#L195) |
| upstream-only link_7.0 | unavailable | unavailable | 0.0143913 / [geometry/inference input L216](https://github.com/simlabrobotics/allegro_hand_ros/blob/296ef6bae4b535ffb91420237cdc8a87f6e9f6df/allegro_hand_description/allegro_hand_description_right.urdf#L216) |
| upstream-only link_7.0_tip | unavailable | unavailable | 0.00723822947 / [geometry/inference input L237](https://github.com/simlabrobotics/allegro_hand_ros/blob/296ef6bae4b535ffb91420237cdc8a87f6e9f6df/allegro_hand_description/allegro_hand_description_right.urdf#L237) |
| upstream-only link_8.0 | unavailable | unavailable | 0.0088396 / [geometry/inference input L257](https://github.com/simlabrobotics/allegro_hand_ros/blob/296ef6bae4b535ffb91420237cdc8a87f6e9f6df/allegro_hand_description/allegro_hand_description_right.urdf#L257) |
| upstream-only link_9.0 | unavailable | unavailable | 0.029106 / [geometry/inference input L278](https://github.com/simlabrobotics/allegro_hand_ros/blob/296ef6bae4b535ffb91420237cdc8a87f6e9f6df/allegro_hand_description/allegro_hand_description_right.urdf#L278) |

## Coverage and unmatched elements

```json
{
  "mapping_h": {
    "bodies": {
      "palm": "base_link"
    },
    "joints": {},
    "body_methods": {
      "palm": "unique kinematic subtree"
    },
    "joint_methods": {},
    "unmatched_m_bodies": [
      "ff_base",
      "ff_distal",
      "ff_medial",
      "ff_proximal",
      "ff_tip",
      "mf_base",
      "mf_distal",
      "mf_medial",
      "mf_proximal",
      "mf_tip",
      "rf_base",
      "rf_distal",
      "rf_medial",
      "rf_proximal",
      "rf_tip",
      "th_base",
      "th_distal",
      "th_medial",
      "th_proximal",
      "th_tip"
    ],
    "unmatched_upstream_bodies": [
      "link_0.0",
      "link_1.0",
      "link_10.0",
      "link_11.0",
      "link_11.0_tip",
      "link_12.0",
      "link_13.0",
      "link_14.0",
      "link_15.0",
      "link_15.0_tip",
      "link_2.0",
      "link_3.0",
      "link_3.0_tip",
      "link_4.0",
      "link_5.0",
      "link_6.0",
      "link_7.0",
      "link_7.0_tip",
      "link_8.0",
      "link_9.0"
    ],
    "unmatched_m_joints": [
      "ffj0",
      "ffj1",
      "ffj2",
      "ffj3",
      "mfj0",
      "mfj1",
      "mfj2",
      "mfj3",
      "rfj0",
      "rfj1",
      "rfj2",
      "rfj3",
      "thj0",
      "thj1",
      "thj2",
      "thj3"
    ],
    "unmatched_upstream_joints": [
      "joint_0.0",
      "joint_1.0",
      "joint_10.0",
      "joint_11.0",
      "joint_12.0",
      "joint_13.0",
      "joint_14.0",
      "joint_15.0",
      "joint_2.0",
      "joint_3.0",
      "joint_4.0",
      "joint_5.0",
      "joint_6.0",
      "joint_7.0",
      "joint_8.0",
      "joint_9.0"
    ],
    "registration_anchor": {
      "M": "palm",
      "H": "base_link",
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
  "https://github.com/simlabrobotics/allegro_hand_ros allegro_hand_description/allegro_hand_description_left.xacro at 296ef6bae4b535ffb91420237cdc8a87f6e9f6df: XacroException: unknown macro name: xacro:finger",
  "https://github.com/simlabrobotics/allegro_hand_ros allegro_hand_description/allegro_hand_description_right.xacro at 296ef6bae4b535ffb91420237cdc8a87f6e9f6df: XacroException: unknown macro name: xacro:finger"
]
```

## History inputs

```json
[
  "allegro_hand_description/allegro_hand_description_right.urdf",
  "allegro_hand_description/meshes/base_link.STL",
  "allegro_hand_description/meshes/link_0.0.STL",
  "allegro_hand_description/meshes/link_1.0.STL",
  "allegro_hand_description/meshes/link_12.0_left.STL",
  "allegro_hand_description/meshes/link_12.0_right.STL",
  "allegro_hand_description/meshes/link_13.0.STL",
  "allegro_hand_description/meshes/link_14.0.STL",
  "allegro_hand_description/meshes/link_15.0.STL",
  "allegro_hand_description/meshes/link_15.0_tip.STL",
  "allegro_hand_description/meshes/link_2.0.STL",
  "allegro_hand_description/meshes/link_3.0.STL",
  "allegro_hand_description/meshes/link_3.0_tip.STL"
]
```

## Self comparisons

```json
[
  {
    "file": "wonik_allegro/left_hand.xml",
    "status": "passed",
    "findings": 0
  },
  {
    "file": "wonik_allegro/right_hand.xml",
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
    "geometry_stripped": false,
    "missing_explicit_inertials": [
      "palm",
      "rf_base",
      "rf_proximal",
      "rf_medial",
      "rf_distal",
      "rf_tip",
      "mf_base",
      "mf_proximal",
      "mf_medial",
      "mf_distal",
      "mf_tip",
      "ff_base",
      "ff_proximal",
      "ff_medial",
      "ff_distal",
      "ff_tip",
      "th_base",
      "th_proximal",
      "th_medial",
      "th_distal",
      "th_tip"
    ],
    "assets_loaded": 11,
    "mesh_conversions": [],
    "nonphysical_normalizations": [],
    "xacro_arguments": {},
    "source_dependencies": [
      "wonik_allegro/left_hand.xml",
      "wonik_allegro/assets/base_link_left.stl",
      "wonik_allegro/assets/link_0.0.stl",
      "wonik_allegro/assets/link_1.0.stl",
      "wonik_allegro/assets/link_2.0.stl",
      "wonik_allegro/assets/link_3.0.stl",
      "wonik_allegro/assets/link_3.0_tip.stl",
      "wonik_allegro/assets/link_12.0_left.stl",
      "wonik_allegro/assets/link_13.0.stl",
      "wonik_allegro/assets/link_14.0.stl",
      "wonik_allegro/assets/link_15.0.stl",
      "wonik_allegro/assets/link_15.0_tip.stl"
    ],
    "registration": {
      "translation": [
        0.0,
        0.0,
        0.0
      ],
      "rotation": [
        [
          0.0,
          0.0,
          0.9999999999999998
        ],
        [
          0.0,
          -0.9999999999999998,
          0.0
        ],
        [
          0.9999999999999998,
          0.0,
          0.0
        ]
      ]
    },
    "compiler_warnings": [],
    "limit_semantics": "Effort from supported scalar actuator envelopes; force from joint caps or supported envelopes; velocity unavailable unless explicitly represented"
  },
  "H": {
    "geometry_stripped": false,
    "missing_explicit_inertials": [
      "base_link",
      "link_0.0",
      "link_1.0",
      "link_2.0",
      "link_3.0",
      "link_3.0_tip",
      "link_4.0",
      "link_5.0",
      "link_6.0",
      "link_7.0",
      "link_7.0_tip",
      "link_8.0",
      "link_9.0",
      "link_10.0",
      "link_11.0",
      "link_11.0_tip",
      "link_12.0",
      "link_13.0",
      "link_14.0",
      "link_15.0",
      "link_15.0_tip"
    ],
    "assets_loaded": 21,
    "mesh_conversions": [],
    "nonphysical_normalizations": [],
    "xacro_arguments": {
      "__package_directory_fallbacks__": "{'allegro_hand_description': 'allegro_hand_description'}"
    },
    "source_dependencies": [
      "allegro_hand_description/allegro_hand_description_right.urdf",
      "allegro_hand_description/meshes/base_link.STL",
      "allegro_hand_description/meshes/link_0.0.STL",
      "allegro_hand_description/meshes/link_1.0.STL",
      "allegro_hand_description/meshes/link_2.0.STL",
      "allegro_hand_description/meshes/link_3.0.STL",
      "allegro_hand_description/meshes/link_3.0_tip.STL",
      "allegro_hand_description/meshes/link_0.0.STL",
      "allegro_hand_description/meshes/link_1.0.STL",
      "allegro_hand_description/meshes/link_2.0.STL",
      "allegro_hand_description/meshes/link_3.0.STL",
      "allegro_hand_description/meshes/link_3.0_tip.STL",
      "allegro_hand_description/meshes/link_0.0.STL",
      "allegro_hand_description/meshes/link_1.0.STL",
      "allegro_hand_description/meshes/link_2.0.STL",
      "allegro_hand_description/meshes/link_3.0.STL",
      "allegro_hand_description/meshes/link_3.0_tip.STL",
      "allegro_hand_description/meshes/link_12.0_right.STL",
      "allegro_hand_description/meshes/link_13.0.STL",
      "allegro_hand_description/meshes/link_14.0.STL",
      "allegro_hand_description/meshes/link_15.0.STL",
      "allegro_hand_description/meshes/link_15.0_tip.STL"
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
  "historical_snapshots_reused": 4,
  "primary_physics_unchanged": true,
  "source_matching": "original raw-value provenance criteria retained; kinematic guard applies to reported CoM"
}
```
