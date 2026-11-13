# low_cost_robot_arm

Status: **complete**. Provenance: **none**, confidence **none**.

No public revision matches all comparable quantities. Class: NO MATCHING SOURCE; never counted as STALE.

M: `https://github.com/google-deepmind/mujoco_menagerie`, `low_cost_robot_arm/low_cost_robot_arm.xml`, commit `370c43965323c0944b433b202aac5058b5f907a9`.
H: `https://github.com/s1lent4gnt/koch-v1-1`, `simulation/follower.urdf`, commit `cc1a4eb9b27978b6bc3bb34f12fa5a7d229f1fde`.
S: unavailable. A machine-readable H can still be compared to M; no-match differences are never counted as STALE.

Limit semantics: MJCF effort values are supported actuator torque/force envelopes. URDF effort and velocity values are manufacturer declarations retained from XML; MuJoCo does not enforce those tags. Such declaration comparisons are explicitly distinct from compiled inertial/range quantities.


## Source evidence

```json
[
  {
    "url": "https://github.com/AlexanderKoch-Koch/low_cost_robot/tree/main",
    "document": "low_cost_robot_arm/README.md",
    "commit": "370c43965323c0944b433b202aac5058b5f907a9",
    "current": true
  },
  {
    "url": "https://github.com/jess-moss/koch-v1-1/tree/main",
    "document": "low_cost_robot_arm/README.md",
    "commit": "370c43965323c0944b433b202aac5058b5f907a9",
    "current": true
  },
  {
    "url": "https://github.com/kevinzakka/obj2mjcf/tree/main",
    "document": "low_cost_robot_arm/README.md",
    "commit": "370c43965323c0944b433b202aac5058b5f907a9",
    "current": true
  },
  {
    "url": "https://github.com/s1lent4gnt/koch-v1-1/blob/main/simulation/follower.urdf",
    "document": "low_cost_robot_arm/README.md",
    "commit": "370c43965323c0944b433b202aac5058b5f907a9",
    "current": true
  }
]
```


## README derivation evidence

Documentation labels are conservative: an automated documented label requires an explicit affected entity and quantity. Broader conversion notes are retained here for review.

> 7. Added approximate joint limits.

## Kinematics consistency

A proper Kabsch rigid transform aligns all matched zero-pose body origins. The maximum per-origin residual and signed hinge/slide axis angles determine whether CoM can be compared; RMS is also recorded. Fewer than three non-collinear origins give insufficient kinematic coverage. CoM records that fail either required M/H or M/S check are excluded from counts and largest discrepancies. Masses, principal moments and raw joint ranges remain unchanged; a flagged range still requires convention review.

| Pair | Status | Origins / rank | RMS / maximum mm | Disagreeing / checked axes |
|---|---|---:|---:|---:|
| M/H | consistent | 7 / 3 | 1.28552697e-14 / 2.43016123e-14 | 0 / 5 |

Exact fitted transforms, per-origin residuals, thresholds and axis vectors:

```json
{
  "M/H": {
    "status": "consistent",
    "matched_body_origins": 7,
    "position_threshold_m": 0.005,
    "axis_threshold_rad": 0.005,
    "residual_definition": "maximum Euclidean residual over matched body origins; Kabsch minimizes RMS, which is also recorded",
    "coordinate_frames": "each snapshot registered to its matched report anchor",
    "anchor_m": "base_link",
    "anchor_other": "base_link",
    "rotation_other_to_m": [
      [
        1.0,
        2.1803533471014893e-16,
        2.351122069804602e-17
      ],
      [
        -2.497453252327128e-16,
        1.0000000000000002,
        -1.975801380879895e-16
      ],
      [
        3.122502256758253e-17,
        -1.5265566588595902e-16,
        1.0
      ]
    ],
    "translation_other_to_m": [
      0.0,
      1.0408340855860843e-17,
      0.0
    ],
    "rms_residual_m": 1.2855269670218212e-17,
    "max_residual_m": 2.43016123303191e-17,
    "fit_rank": 3,
    "axis_checks": [
      {
        "joint_m": "base_rotation",
        "joint_other": "joint_1",
        "axis_m": [
          0.0,
          0.0,
          -1.0
        ],
        "axis_other_aligned": [
          -2.351122069804602e-17,
          1.975801380879895e-16,
          -1.0
        ],
        "angle_rad": 1.9897408993530094e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "pitch",
        "joint_other": "joint_2",
        "axis_m": [
          0.0,
          1.0,
          0.0
        ],
        "axis_other_aligned": [
          2.1803533471014888e-16,
          1.0,
          -1.52655665885959e-16
        ],
        "angle_rad": 2.6616378324116936e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "wrist_pitch",
        "joint_other": "joint_4",
        "axis_m": [
          0.0,
          1.0,
          0.0
        ],
        "axis_other_aligned": [
          2.1803533471014888e-16,
          1.0,
          -1.52655665885959e-16
        ],
        "angle_rad": 2.6616378324116936e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "wrist_roll",
        "joint_other": "joint_5",
        "axis_m": [
          1.0,
          0.0,
          0.0
        ],
        "axis_other_aligned": [
          1.0,
          -2.497453252327128e-16,
          3.122502256758253e-17
        ],
        "angle_rad": 2.51689748519759e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "gripper",
        "joint_other": "joint_6",
        "axis_m": [
          0.0,
          0.0,
          -1.0
        ],
        "axis_other_aligned": [
          -2.351122069804602e-17,
          1.975801380879895e-16,
          -1.0
        ],
        "angle_rad": 1.9897408993530094e-16,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      }
    ],
    "axis_disagreements": [],
    "com_eligible": true,
    "covariance_singular_values": [
      0.06297358396520873,
      0.008716219833446727,
      0.0002626213513616862
    ],
    "origin_residuals_m": {
      "base_link": 1.0408340855860843e-17,
      "shoulder_rotation": 1.8594813269915578e-18,
      "shoulder_to_elbow": 1.0408340855860843e-17,
      "elbow_to_wrist_extension": 2.43016123303191e-17,
      "elbow_to_wrist": 0.0,
      "gripper_static_finger": 1.4094628242311558e-17,
      "gripper_moving_finger": 1.214306433183765e-17
    },
    "reason": "Unique proper rigid fit and matched signed axes meet the configured thresholds"
  }
}
```


## Every reported quantity difference

Counts are quantity records, including correlated total/subtree/body mass records; they are not independent robot defects.

| Entity / quantity | M | S | H | H − M | Class | M source | S source | H source |
|---|---|---|---|---|---|---|---|---|
| robot / total_mass | 0.344538925 | unavailable | 0.293286 | -0.0512529255 | NO MATCHING SOURCE | [aggregate inputs](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/low_cost_robot_arm/low_cost_robot_arm.xml#L1) | unavailable | [aggregate inputs](https://github.com/s1lent4gnt/koch-v1-1/blob/cc1a4eb9b27978b6bc3bb34f12fa5a7d229f1fde/simulation/follower.urdf#L1) |
| robot / total_com_registered | [-0.02158181, 0.000272608417, 0.0918232448] | unavailable | [-0.0320185968, 0.000836156217, 0.106129391] | [-0.0104367868, 0.0005635478, 0.0143061465] | NO MATCHING SOURCE | [aggregate inputs](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/low_cost_robot_arm/low_cost_robot_arm.xml#L1) | unavailable | [aggregate inputs](https://github.com/s1lent4gnt/koch-v1-1/blob/cc1a4eb9b27978b6bc3bb34f12fa5a7d229f1fde/simulation/follower.urdf#L1) |
| base_link / mass | 0.118518925 | unavailable | 0.067266 | -0.0512529255 | NO MATCHING SOURCE | [geometry/inference input L56](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/low_cost_robot_arm/low_cost_robot_arm.xml#L56) | unavailable | [input L15](https://github.com/s1lent4gnt/koch-v1-1/blob/cc1a4eb9b27978b6bc3bb34f12fa5a7d229f1fde/simulation/follower.urdf#L15) |
| base_link / subtree_mass | 0.344538925 | unavailable | 0.293286 | -0.0512529255 | NO MATCHING SOURCE | [subtree root L56](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/low_cost_robot_arm/low_cost_robot_arm.xml#L56) | unavailable | [subtree root L9](https://github.com/s1lent4gnt/koch-v1-1/blob/cc1a4eb9b27978b6bc3bb34f12fa5a7d229f1fde/simulation/follower.urdf#L9) |
| base_link / com_registered | [0.0360960551, -7.54327812e-05, 0.0122314018] | unavailable | [0.034538, 0.0021165, 0.013963] | [-0.0015580551, 0.00219193278, 0.0017315982] | NO MATCHING SOURCE | [geometry/inference input L56](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/low_cost_robot_arm/low_cost_robot_arm.xml#L56) | unavailable | [CoM/kinematic input L13](https://github.com/s1lent4gnt/koch-v1-1/blob/cc1a4eb9b27978b6bc3bb34f12fa5a7d229f1fde/simulation/follower.urdf#L13) |
| base_link / principal_moments | [6.75025273e-05, 8.85969911e-05, 0.000137198079] | unavailable | [2.17302607e-05, 4.4987357e-05, 5.91193823e-05] | [-4.57722666e-05, -4.36096341e-05, -7.80786963e-05] | NO MATCHING SOURCE | [geometry/inference input L56](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/low_cost_robot_arm/low_cost_robot_arm.xml#L56) | unavailable | [inertia input L22](https://github.com/s1lent4gnt/koch-v1-1/blob/cc1a4eb9b27978b6bc3bb34f12fa5a7d229f1fde/simulation/follower.urdf#L22) |
| base_rotation / range | [-2.2, 2.2] | unavailable | [-3.14, 3.14] | [-0.94, 0.94] | NO MATCHING SOURCE | [input L63](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/low_cost_robot_arm/low_cost_robot_arm.xml#L63) | unavailable | [input L109](https://github.com/s1lent4gnt/koch-v1-1/blob/cc1a4eb9b27978b6bc3bb34f12fa5a7d229f1fde/simulation/follower.urdf#L109) |
| base_rotation / effort | 87 | unavailable | 0.5 | -86.5 | NO MATCHING SOURCE | [input L121](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/low_cost_robot_arm/low_cost_robot_arm.xml#L121) | unavailable | [input L109](https://github.com/s1lent4gnt/koch-v1-1/blob/cc1a4eb9b27978b6bc3bb34f12fa5a7d229f1fde/simulation/follower.urdf#L109) |
| pitch / range | [-1.57, 0.6] | unavailable | [-3.14, 3.14] | [-1.57, 2.54] | NO MATCHING SOURCE | [input L70](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/low_cost_robot_arm/low_cost_robot_arm.xml#L70) | unavailable | [input L165](https://github.com/s1lent4gnt/koch-v1-1/blob/cc1a4eb9b27978b6bc3bb34f12fa5a7d229f1fde/simulation/follower.urdf#L165) |
| pitch / effort | 87 | unavailable | 0.5 | -86.5 | NO MATCHING SOURCE | [input L122](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/low_cost_robot_arm/low_cost_robot_arm.xml#L122) | unavailable | [input L165](https://github.com/s1lent4gnt/koch-v1-1/blob/cc1a4eb9b27978b6bc3bb34f12fa5a7d229f1fde/simulation/follower.urdf#L165) |
| wrist_pitch / range | [-2, 2] | unavailable | [-3.14, 3.14] | [-1.14, 1.14] | NO MATCHING SOURCE | [input L84](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/low_cost_robot_arm/low_cost_robot_arm.xml#L84) | unavailable | [input L277](https://github.com/s1lent4gnt/koch-v1-1/blob/cc1a4eb9b27978b6bc3bb34f12fa5a7d229f1fde/simulation/follower.urdf#L277) |
| wrist_pitch / effort | 12 | unavailable | 0.5 | -11.5 | NO MATCHING SOURCE | [input L124](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/low_cost_robot_arm/low_cost_robot_arm.xml#L124) | unavailable | [input L277](https://github.com/s1lent4gnt/koch-v1-1/blob/cc1a4eb9b27978b6bc3bb34f12fa5a7d229f1fde/simulation/follower.urdf#L277) |
| wrist_roll / effort | 10 | unavailable | 0.5 | -9.5 | NO MATCHING SOURCE | [input L125](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/low_cost_robot_arm/low_cost_robot_arm.xml#L125) | unavailable | [input L333](https://github.com/s1lent4gnt/koch-v1-1/blob/cc1a4eb9b27978b6bc3bb34f12fa5a7d229f1fde/simulation/follower.urdf#L333) |
| gripper / range | [-1.6, 0.032] | unavailable | [-2.45, 0.032] | [-0.85, 0] | NO MATCHING SOURCE | [input L101](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/low_cost_robot_arm/low_cost_robot_arm.xml#L101) | unavailable | [input L374](https://github.com/s1lent4gnt/koch-v1-1/blob/cc1a4eb9b27978b6bc3bb34f12fa5a7d229f1fde/simulation/follower.urdf#L374) |
| gripper / effort | 5 | unavailable | 0.5 | -4.5 | NO MATCHING SOURCE | [input L126](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/low_cost_robot_arm/low_cost_robot_arm.xml#L126) | unavailable | [input L374](https://github.com/s1lent4gnt/koch-v1-1/blob/cc1a4eb9b27978b6bc3bb34f12fa5a7d229f1fde/simulation/follower.urdf#L374) |

## Raw CoM records and reporting decisions

Raw values retain the previous root-anchor registration before Kabsch; original world coordinates also remain in the snapshots. Eligible findings above use the fitted transform into M. Excluded raw records below are diagnostic numbers, not findings. No CoM suppression applies to mass or principal inertia moments.

| Entity / quantity | Raw M | Raw S | Raw H | Raw H − M | Decision | M source | S source | H source |
|---|---|---|---|---|---|---|---|---|
| robot / total_com_registered | [-0.02158181, 0.000272608417, 0.0918232448] | unavailable | [-0.0320185968, 0.000836156217, 0.106129391] | [-0.0104367868, 0.0005635478, 0.0143061465] | eligible; compared after Kabsch alignment | [aggregate inputs](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/low_cost_robot_arm/low_cost_robot_arm.xml#L1) | unavailable | [aggregate inputs](https://github.com/s1lent4gnt/koch-v1-1/blob/cc1a4eb9b27978b6bc3bb34f12fa5a7d229f1fde/simulation/follower.urdf#L1) |
| base_link / com_registered | [0.0360960551, -7.54327812e-05, 0.0122314018] | unavailable | [0.034538, 0.0021165, 0.013963] | [-0.0015580551, 0.00219193278, 0.0017315982] | eligible; compared after Kabsch alignment | [geometry/inference input L56](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/low_cost_robot_arm/low_cost_robot_arm.xml#L56) | unavailable | [CoM/kinematic input L13](https://github.com/s1lent4gnt/koch-v1-1/blob/cc1a4eb9b27978b6bc3bb34f12fa5a7d229f1fde/simulation/follower.urdf#L13) |
| shoulder_rotation / com_registered | [0.023924, -0.00048792, 0.054281] | unavailable | [0.023924, -0.00048792, 0.054281] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L62](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/low_cost_robot_arm/low_cost_robot_arm.xml#L62) | unavailable | [CoM/kinematic input L61](https://github.com/s1lent4gnt/koch-v1-1/blob/cc1a4eb9b27978b6bc3bb34f12fa5a7d229f1fde/simulation/follower.urdf#L61) |
| shoulder_to_elbow / com_registered | [0.0131747, 7e-05, 0.127847] | unavailable | [0.0131747, 7e-05, 0.127847] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L69](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/low_cost_robot_arm/low_cost_robot_arm.xml#L69) | unavailable | [CoM/kinematic input L117](https://github.com/s1lent4gnt/koch-v1-1/blob/cc1a4eb9b27978b6bc3bb34f12fa5a7d229f1fde/simulation/follower.urdf#L117) |
| elbow_to_wrist_extension / com_registered | [-0.05817, 0.000105, 0.1674659] | unavailable | [-0.05817, 0.000105, 0.1674659] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L76](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/low_cost_robot_arm/low_cost_robot_arm.xml#L76) | unavailable | [CoM/kinematic input L173](https://github.com/s1lent4gnt/koch-v1-1/blob/cc1a4eb9b27978b6bc3bb34f12fa5a7d229f1fde/simulation/follower.urdf#L173) |
| elbow_to_wrist / com_registered | [-0.1298, 0.004845, 0.167290839] | unavailable | [-0.1298, 0.004845, 0.167290839] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L83](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/low_cost_robot_arm/low_cost_robot_arm.xml#L83) | unavailable | [CoM/kinematic input L229](https://github.com/s1lent4gnt/koch-v1-1/blob/cc1a4eb9b27978b6bc3bb34f12fa5a7d229f1fde/simulation/follower.urdf#L229) |
| gripper_static_finger / com_registered | [-0.167371, 0.0040849, 0.16748001] | unavailable | [-0.167371, 0.0040849, 0.16748001] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L90](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/low_cost_robot_arm/low_cost_robot_arm.xml#L90) | unavailable | [CoM/kinematic input L285](https://github.com/s1lent4gnt/koch-v1-1/blob/cc1a4eb9b27978b6bc3bb34f12fa5a7d229f1fde/simulation/follower.urdf#L285) |
| gripper_moving_finger / com_registered | [-0.1865, -0.0076713, 0.1676599] | unavailable | [-0.1865, -0.0076713, 0.1676599] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L100](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/low_cost_robot_arm/low_cost_robot_arm.xml#L100) | unavailable | [CoM/kinematic input L341](https://github.com/s1lent4gnt/koch-v1-1/blob/cc1a4eb9b27978b6bc3bb34f12fa5a7d229f1fde/simulation/follower.urdf#L341) |

## Mass accounting

Every contributing compiled body mass is listed here so total/subtree sums can be checked. Links point to explicit inertials or to geometry inputs when the compiler inferred a mass. CoM links identify inertial inputs; world coordinates additionally use the ancestor transforms and the registration recorded below.

| M body | M kg / source | S kg / source | H kg / source |
|---|---|---|---|
| base_link | 0.118518925 / [geometry/inference input L56](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/low_cost_robot_arm/low_cost_robot_arm.xml#L56) | unavailable | 0.067266 / [input L15](https://github.com/s1lent4gnt/koch-v1-1/blob/cc1a4eb9b27978b6bc3bb34f12fa5a7d229f1fde/simulation/follower.urdf#L15) |
| shoulder_rotation | 0.05014 / [input L62](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/low_cost_robot_arm/low_cost_robot_arm.xml#L62) | unavailable | 0.05014 / [input L63](https://github.com/s1lent4gnt/koch-v1-1/blob/cc1a4eb9b27978b6bc3bb34f12fa5a7d229f1fde/simulation/follower.urdf#L63) |
| shoulder_to_elbow | 0.050177 / [input L69](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/low_cost_robot_arm/low_cost_robot_arm.xml#L69) | unavailable | 0.050177 / [input L119](https://github.com/s1lent4gnt/koch-v1-1/blob/cc1a4eb9b27978b6bc3bb34f12fa5a7d229f1fde/simulation/follower.urdf#L119) |
| elbow_to_wrist_extension | 0.06379 / [input L76](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/low_cost_robot_arm/low_cost_robot_arm.xml#L76) | unavailable | 0.06379 / [input L175](https://github.com/s1lent4gnt/koch-v1-1/blob/cc1a4eb9b27978b6bc3bb34f12fa5a7d229f1fde/simulation/follower.urdf#L175) |
| elbow_to_wrist | 0.019805 / [input L83](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/low_cost_robot_arm/low_cost_robot_arm.xml#L83) | unavailable | 0.019805 / [input L231](https://github.com/s1lent4gnt/koch-v1-1/blob/cc1a4eb9b27978b6bc3bb34f12fa5a7d229f1fde/simulation/follower.urdf#L231) |
| gripper_static_finger | 0.029277 / [input L90](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/low_cost_robot_arm/low_cost_robot_arm.xml#L90) | unavailable | 0.029277 / [input L287](https://github.com/s1lent4gnt/koch-v1-1/blob/cc1a4eb9b27978b6bc3bb34f12fa5a7d229f1fde/simulation/follower.urdf#L287) |
| gripper_moving_finger | 0.012831 / [input L100](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/low_cost_robot_arm/low_cost_robot_arm.xml#L100) | unavailable | 0.012831 / [input L343](https://github.com/s1lent4gnt/koch-v1-1/blob/cc1a4eb9b27978b6bc3bb34f12fa5a7d229f1fde/simulation/follower.urdf#L343) |

## Coverage and unmatched elements

```json
{
  "mapping_h": {
    "bodies": {
      "base_link": "base_link",
      "shoulder_rotation": "link_1",
      "shoulder_to_elbow": "link_2",
      "elbow_to_wrist_extension": "link_3",
      "elbow_to_wrist": "link_4",
      "gripper_static_finger": "link_5",
      "gripper_moving_finger": "link_6"
    },
    "joints": {
      "base_rotation": "joint_1",
      "pitch": "joint_2",
      "wrist_pitch": "joint_4",
      "wrist_roll": "joint_5",
      "gripper": "joint_6"
    },
    "body_methods": {
      "base_link": "name",
      "shoulder_rotation": "unique kinematic subtree",
      "shoulder_to_elbow": "unique kinematic subtree",
      "elbow_to_wrist_extension": "unique kinematic subtree",
      "elbow_to_wrist": "unique kinematic subtree",
      "gripper_static_finger": "unique kinematic subtree",
      "gripper_moving_finger": "unique kinematic subtree"
    },
    "joint_methods": {
      "base_rotation": "unique joint on matched body with same type and axis",
      "pitch": "unique joint on matched body with same type and axis",
      "wrist_pitch": "unique joint on matched body with same type and axis",
      "wrist_roll": "unique joint on matched body with same type and axis",
      "gripper": "unique joint on matched body with same type and axis"
    },
    "unmatched_m_bodies": [],
    "unmatched_upstream_bodies": [],
    "unmatched_m_joints": [
      "elbow"
    ],
    "unmatched_upstream_joints": [
      "joint_3"
    ],
    "registration_anchor": {
      "M": "base_link",
      "H": "base_link",
      "root_unmatched": false
    }
  },
  "mapping_s": null,
  "unavailable": [
    {
      "entity": "base_rotation",
      "other_entity": "joint_1",
      "quantity": "force",
      "tolerance": "limit",
      "m": 87.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "base_rotation",
      "other_entity": "joint_1",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 100.0,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "pitch",
      "other_entity": "joint_2",
      "quantity": "force",
      "tolerance": "limit",
      "m": 87.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "pitch",
      "other_entity": "joint_2",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 100.0,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "wrist_pitch",
      "other_entity": "joint_4",
      "quantity": "force",
      "tolerance": "limit",
      "m": 12.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "wrist_pitch",
      "other_entity": "joint_4",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 100.0,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "wrist_roll",
      "other_entity": "joint_5",
      "quantity": "force",
      "tolerance": "limit",
      "m": 10.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "wrist_roll",
      "other_entity": "joint_5",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 100.0,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "gripper",
      "other_entity": "joint_6",
      "quantity": "force",
      "tolerance": "limit",
      "m": 5.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "gripper",
      "other_entity": "joint_6",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 100.0,
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
| base_rotation / force | 87 | unavailable | unavailable |
| base_rotation / velocity | unavailable | unavailable | 100 |
| pitch / force | 87 | unavailable | unavailable |
| pitch / velocity | unavailable | unavailable | 100 |
| wrist_pitch / force | 12 | unavailable | unavailable |
| wrist_pitch / velocity | unavailable | unavailable | 100 |
| wrist_roll / force | 10 | unavailable | unavailable |
| wrist_roll / velocity | unavailable | unavailable | 100 |
| gripper / force | 5 | unavailable | unavailable |
| gripper / velocity | unavailable | unavailable | 100 |
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
    "file": "low_cost_robot_arm/low_cost_robot_arm.xml",
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
      "NO MATCHING SOURCE": 15
    },
    "classifications_changed": 0,
    "finding_membership_changes": 0
  },
  "2": {
    "provenance_method": "none",
    "counts": {
      "NO MATCHING SOURCE": 15
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
      "base_link"
    ],
    "assets_loaded": 22,
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
  "self_variants_recompiled": 1,
  "historical_snapshots_reused": 3,
  "primary_physics_unchanged": true,
  "source_matching": "original raw-value provenance criteria retained; kinematic guard applies to reported CoM"
}
```
