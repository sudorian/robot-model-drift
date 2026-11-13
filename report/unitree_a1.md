# unitree_a1

Status: **complete**. Provenance: **none**, confidence **none**.

No public revision matches all comparable quantities. Class: NO MATCHING SOURCE; never counted as STALE.

M: `https://github.com/google-deepmind/mujoco_menagerie`, `unitree_a1/a1.xml`, commit `370c43965323c0944b433b202aac5058b5f907a9`.
H: `https://github.com/unitreerobotics/unitree_ros`, `robots/a1_description/urdf/a1.urdf`, commit `157ff950351e5f535e03c5d85a16b7d594b3dbcc`.
S: unavailable. A machine-readable H can still be compared to M; no-match differences are never counted as STALE.

Limit semantics: MJCF effort values are supported actuator torque/force envelopes. URDF effort and velocity values are manufacturer declarations retained from XML; MuJoCo does not enforce those tags. Such declaration comparisons are explicitly distinct from compiled inertial/range quantities.


## Source evidence

```json
[
  {
    "url": "https://github.com/kevinzakka/obj2mjcf",
    "document": "unitree_a1/README.md",
    "commit": "370c43965323c0944b433b202aac5058b5f907a9",
    "current": true
  },
  {
    "url": "https://github.com/unitreerobotics/unitree_mujoco/tree/main/data/a1/meshes",
    "document": "unitree_a1/README.md",
    "commit": "370c43965323c0944b433b202aac5058b5f907a9",
    "current": true
  },
  {
    "url": "https://github.com/unitreerobotics/unitree_mujoco/tree/main/data/a1/urdf",
    "document": "unitree_a1/README.md",
    "commit": "370c43965323c0944b433b202aac5058b5f907a9",
    "current": true
  },
  {
    "url": "https://github.com/unitreerobotics/unitree_ros",
    "file": "robots/a1_description/urdf/a1.urdf",
    "document": "manufacturer source Git tree",
    "reason": "README-linked path missing at current HEAD; exact model filename in same-manufacturer referenced source repository"
  }
]
```


## README derivation evidence

Documentation labels are conservative: an automated documented label requires an explicit affected entity and quantity. Broader conversion notes are retained here for review.

> 8. Shifted joint reference values and ranges so that 0 corresponds to standing pose.

## Kinematics consistency

A proper Kabsch rigid transform aligns all matched zero-pose body origins. The maximum per-origin residual and signed hinge/slide axis angles determine whether CoM can be compared; RMS is also recorded. Fewer than three non-collinear origins give insufficient kinematic coverage. CoM records that fail either required M/H or M/S check are excluded from counts and largest discrepancies. Masses, principal moments and raw joint ranges remain unchanged; a flagged range still requires convention review.

| Pair | Status | Origins / rank | RMS / maximum mm | Disagreeing / checked axes |
|---|---|---:|---:|---:|
| M/H | consistent | 13 / 3 | 2.59437261 / 2.79508497 | 0 / 12 |

Exact fitted transforms, per-origin residuals, thresholds and axis vectors:

```json
{
  "M/H": {
    "status": "consistent",
    "matched_body_origins": 13,
    "position_threshold_m": 0.005,
    "axis_threshold_rad": 0.005,
    "residual_definition": "maximum Euclidean residual over matched body origins; Kabsch minimizes RMS, which is also recorded",
    "coordinate_frames": "each snapshot registered to its matched report anchor",
    "anchor_m": "trunk",
    "anchor_other": "trunk",
    "rotation_other_to_m": [
      [
        1.0,
        1.5989891474754136e-18,
        1.12467706399589e-18
      ],
      [
        -1.598989147475413e-18,
        0.9999999999999997,
        4.365651278919109e-17
      ],
      [
        -1.1246770639958894e-18,
        -8.521918741192588e-17,
        0.9999999999999998
      ]
    ],
    "translation_other_to_m": [
      -4.200877660004701e-18,
      2.6865546331809903e-18,
      -1.3877787807814457e-17
    ],
    "rms_residual_m": 0.0025943726083138734,
    "max_residual_m": 0.0027950849718747645,
    "fit_rank": 3,
    "axis_checks": [
      {
        "joint_m": "FR_hip_joint",
        "joint_other": "FR_hip_joint",
        "axis_m": [
          1.0,
          0.0,
          0.0
        ],
        "axis_other_aligned": [
          1.0,
          -1.598989147475413e-18,
          -1.1246770639958894e-18
        ],
        "angle_rad": 1.954907873026901e-18,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "FR_thigh_joint",
        "joint_other": "FR_thigh_joint",
        "axis_m": [
          0.0,
          1.0,
          0.0
        ],
        "axis_other_aligned": [
          1.5989891474754141e-18,
          1.0,
          -8.52191874119259e-17
        ],
        "angle_rad": 8.523418721054771e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "FR_calf_joint",
        "joint_other": "FR_calf_joint",
        "axis_m": [
          0.0,
          1.0,
          0.0
        ],
        "axis_other_aligned": [
          1.5989891474754141e-18,
          1.0,
          -8.52191874119259e-17
        ],
        "angle_rad": 8.523418721054771e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "FL_hip_joint",
        "joint_other": "FL_hip_joint",
        "axis_m": [
          1.0,
          0.0,
          0.0
        ],
        "axis_other_aligned": [
          1.0,
          -1.598989147475413e-18,
          -1.1246770639958894e-18
        ],
        "angle_rad": 1.954907873026901e-18,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "FL_thigh_joint",
        "joint_other": "FL_thigh_joint",
        "axis_m": [
          0.0,
          1.0,
          0.0
        ],
        "axis_other_aligned": [
          1.5989891474754141e-18,
          1.0,
          -8.52191874119259e-17
        ],
        "angle_rad": 8.523418721054771e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "FL_calf_joint",
        "joint_other": "FL_calf_joint",
        "axis_m": [
          0.0,
          1.0,
          0.0
        ],
        "axis_other_aligned": [
          1.5989891474754141e-18,
          1.0,
          -8.52191874119259e-17
        ],
        "angle_rad": 8.523418721054771e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "RR_hip_joint",
        "joint_other": "RR_hip_joint",
        "axis_m": [
          1.0,
          0.0,
          0.0
        ],
        "axis_other_aligned": [
          1.0,
          -1.598989147475413e-18,
          -1.1246770639958894e-18
        ],
        "angle_rad": 1.954907873026901e-18,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "RR_thigh_joint",
        "joint_other": "RR_thigh_joint",
        "axis_m": [
          0.0,
          1.0,
          0.0
        ],
        "axis_other_aligned": [
          1.5989891474754141e-18,
          1.0,
          -8.52191874119259e-17
        ],
        "angle_rad": 8.523418721054771e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "RR_calf_joint",
        "joint_other": "RR_calf_joint",
        "axis_m": [
          0.0,
          1.0,
          0.0
        ],
        "axis_other_aligned": [
          1.5989891474754141e-18,
          1.0,
          -8.52191874119259e-17
        ],
        "angle_rad": 8.523418721054771e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "RL_hip_joint",
        "joint_other": "RL_hip_joint",
        "axis_m": [
          1.0,
          0.0,
          0.0
        ],
        "axis_other_aligned": [
          1.0,
          -1.598989147475413e-18,
          -1.1246770639958894e-18
        ],
        "angle_rad": 1.954907873026901e-18,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "RL_thigh_joint",
        "joint_other": "RL_thigh_joint",
        "axis_m": [
          0.0,
          1.0,
          0.0
        ],
        "axis_other_aligned": [
          1.5989891474754141e-18,
          1.0,
          -8.52191874119259e-17
        ],
        "angle_rad": 8.523418721054771e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "RL_calf_joint",
        "joint_other": "RL_calf_joint",
        "axis_m": [
          0.0,
          1.0,
          0.0
        ],
        "axis_other_aligned": [
          1.5989891474754141e-18,
          1.0,
          -8.52191874119259e-17
        ],
        "angle_rad": 8.523418721054771e-17,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      }
    ],
    "axis_disagreements": [],
    "com_eligible": true,
    "covariance_singular_values": [
      0.39637799999999995,
      0.14701311999999997,
      0.11076923076923079
    ],
    "origin_residuals_m": {
      "trunk": 1.4746455280850256e-17,
      "FR_hip": 0.0025000000000000022,
      "FR_thigh": 0.0027950849718747645,
      "FR_calf": 0.0027950849718747645,
      "FL_hip": 0.0025000000000000022,
      "FL_thigh": 0.0027950849718747645,
      "FL_calf": 0.0027950849718747645,
      "RR_hip": 0.0025000000000000022,
      "RR_thigh": 0.0027950849718747645,
      "RR_calf": 0.0027950849718747645,
      "RL_hip": 0.0025000000000000022,
      "RL_thigh": 0.0027950849718747645,
      "RL_calf": 0.0027950849718747645
    },
    "reason": "Unique proper rigid fit and matched signed axes meet the configured thresholds"
  }
}
```


## Every reported quantity difference

Counts are quantity records, including correlated total/subtree/body mass records; they are not independent robot defects.

| Entity / quantity | M | S | H | H − M | Class | M source | S source | H source |
|---|---|---|---|---|---|---|---|---|
| robot / total_mass | 12.453 | unavailable | 14.4169702 | 1.96397021 | NO MATCHING SOURCE | [aggregate inputs](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_a1/a1.xml#L1) | unavailable | [aggregate inputs](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/a1_description/urdf/a1.urdf#L1) |
| robot / total_com_registered | [-0.000710149092, 0.00155169839, -0.0331727735] | unavailable | [-0.00061340794, 0.00170632246, -0.028698421] | [9.67411515e-05, 0.000154624069, 0.00447435251] | NO MATCHING SOURCE | [aggregate inputs](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_a1/a1.xml#L1) | unavailable | [aggregate inputs](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/a1_description/urdf/a1.urdf#L1) |
| trunk / mass | 4.713 | unavailable | 6 | 1.287 | NO MATCHING SOURCE | [input L73](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_a1/a1.xml#L73) | unavailable | [input L334](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/a1_description/urdf/a1.urdf#L334) |
| trunk / subtree_mass | 12.453 | unavailable | 14.4169702 | 1.96397021 | NO MATCHING SOURCE | [subtree root L70](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_a1/a1.xml#L70) | unavailable | [subtree root L318](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/a1_description/urdf/a1.urdf#L318) |
| FR_hip / subtree_mass | 1.935 | unavailable | 2.10399255 | 0.168992552 | NO MATCHING SOURCE | [subtree root L83](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_a1/a1.xml#L83) | unavailable | [subtree root L371](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/a1_description/urdf/a1.urdf#L371) |
| FR_hip / com_registered | [0.179689, -0.047635, 3.1e-05] | unavailable | [0.177189, -0.047635, 3.1e-05] | [-0.0025, 1.38777878e-17, -1.32679241e-17] | NO MATCHING SOURCE | [CoM/kinematic input L85](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_a1/a1.xml#L85) | unavailable | [CoM/kinematic input L386](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/a1_description/urdf/a1.urdf#L386) |
| FR_thigh / com_registered | [0.179763, -0.109723, -0.027326] | unavailable | [0.177263, -0.108473, -0.027326] | [-0.0025, 0.00125, 2.08166817e-17] | NO MATCHING SOURCE | [CoM/kinematic input L91](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_a1/a1.xml#L91) | unavailable | [CoM/kinematic input L428](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/a1_description/urdf/a1.urdf#L428) |
| FR_calf / mass | 0.226 | unavailable | 0.166 | -0.06 | NO MATCHING SOURCE | [input L99](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_a1/a1.xml#L99) | unavailable | [input L457](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/a1_description/urdf/a1.urdf#L457) |
| FR_calf / com_registered | [0.18772659, -0.13205, -0.331975] | unavailable | [0.186935, -0.1308, -0.307388] | [-0.00079159, 0.00125, 0.024587] | NO MATCHING SOURCE | [CoM/kinematic input L99](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_a1/a1.xml#L99) | unavailable | [CoM/kinematic input L456](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/a1_description/urdf/a1.urdf#L456) |
| FR_calf / principal_moments | [3.54834e-05, 0.00339393, 0.00340344] | unavailable | [2.57216547e-05, 0.00300467635, 0.003014022] | [-9.76174528e-06, -0.000389253655, -0.000389418] | NO MATCHING SOURCE | [inertia input L99](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_a1/a1.xml#L99) | unavailable | [inertia input L458](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/a1_description/urdf/a1.urdf#L458) |
| FL_hip / subtree_mass | 1.935 | unavailable | 2.10399255 | 0.168992552 | NO MATCHING SOURCE | [subtree root L108](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_a1/a1.xml#L108) | unavailable | [subtree root L523](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/a1_description/urdf/a1.urdf#L523) |
| FL_hip / com_registered | [0.179689, 0.047635, 3.1e-05] | unavailable | [0.177189, 0.047635, 3.1e-05] | [-0.0025, -1.38777878e-17, -2.13858879e-17] | NO MATCHING SOURCE | [CoM/kinematic input L110](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_a1/a1.xml#L110) | unavailable | [CoM/kinematic input L538](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/a1_description/urdf/a1.urdf#L538) |
| FL_thigh / com_registered | [0.179763, 0.109723, -0.027326] | unavailable | [0.177263, 0.108473, -0.027326] | [-0.0025, -0.00125, 0] | NO MATCHING SOURCE | [CoM/kinematic input L117](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_a1/a1.xml#L117) | unavailable | [CoM/kinematic input L580](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/a1_description/urdf/a1.urdf#L580) |
| FL_calf / mass | 0.226 | unavailable | 0.166 | -0.06 | NO MATCHING SOURCE | [input L125](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_a1/a1.xml#L125) | unavailable | [input L609](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/a1_description/urdf/a1.urdf#L609) |
| FL_calf / com_registered | [0.18772659, 0.13205, -0.331975] | unavailable | [0.186935, 0.1308, -0.307388] | [-0.00079159, -0.00125, 0.024587] | NO MATCHING SOURCE | [CoM/kinematic input L125](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_a1/a1.xml#L125) | unavailable | [CoM/kinematic input L608](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/a1_description/urdf/a1.urdf#L608) |
| FL_calf / principal_moments | [3.54834e-05, 0.00339393, 0.00340344] | unavailable | [2.57216547e-05, 0.00300467635, 0.003014022] | [-9.76174528e-06, -0.000389253655, -0.000389418] | NO MATCHING SOURCE | [inertia input L125](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_a1/a1.xml#L125) | unavailable | [inertia input L610](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/a1_description/urdf/a1.urdf#L610) |
| RR_hip / subtree_mass | 1.935 | unavailable | 2.10399255 | 0.168992552 | NO MATCHING SOURCE | [subtree root L134](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_a1/a1.xml#L134) | unavailable | [subtree root L675](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/a1_description/urdf/a1.urdf#L675) |
| RR_hip / com_registered | [-0.179689, -0.047635, 3.1e-05] | unavailable | [-0.177189, -0.047635, 3.1e-05] | [0.0025, 1.38777878e-17, -1.28749008e-17] | NO MATCHING SOURCE | [CoM/kinematic input L136](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_a1/a1.xml#L136) | unavailable | [CoM/kinematic input L690](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/a1_description/urdf/a1.urdf#L690) |
| RR_thigh / com_registered | [-0.186237, -0.109723, -0.027326] | unavailable | [-0.183737, -0.108473, -0.027326] | [0.0025, 0.00125, 2.08166817e-17] | NO MATCHING SOURCE | [CoM/kinematic input L142](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_a1/a1.xml#L142) | unavailable | [CoM/kinematic input L732](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/a1_description/urdf/a1.urdf#L732) |
| RR_calf / mass | 0.226 | unavailable | 0.166 | -0.06 | NO MATCHING SOURCE | [input L150](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_a1/a1.xml#L150) | unavailable | [input L761](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/a1_description/urdf/a1.urdf#L761) |
| RR_calf / com_registered | [-0.17827341, -0.13205, -0.331975] | unavailable | [-0.174065, -0.1308, -0.307388] | [0.00420841, 0.00125, 0.024587] | NO MATCHING SOURCE | [CoM/kinematic input L150](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_a1/a1.xml#L150) | unavailable | [CoM/kinematic input L760](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/a1_description/urdf/a1.urdf#L760) |
| RR_calf / principal_moments | [3.54834e-05, 0.00339393, 0.00340344] | unavailable | [2.57216547e-05, 0.00300467635, 0.003014022] | [-9.76174528e-06, -0.000389253655, -0.000389418] | NO MATCHING SOURCE | [inertia input L150](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_a1/a1.xml#L150) | unavailable | [inertia input L762](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/a1_description/urdf/a1.urdf#L762) |
| RL_hip / subtree_mass | 1.935 | unavailable | 2.10399255 | 0.168992552 | NO MATCHING SOURCE | [subtree root L159](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_a1/a1.xml#L159) | unavailable | [subtree root L827](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/a1_description/urdf/a1.urdf#L827) |
| RL_hip / com_registered | [-0.179689, 0.047635, 3.1e-05] | unavailable | [-0.177189, 0.047635, 3.1e-05] | [0.0025, -1.38777878e-17, -2.09928646e-17] | NO MATCHING SOURCE | [CoM/kinematic input L161](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_a1/a1.xml#L161) | unavailable | [CoM/kinematic input L842](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/a1_description/urdf/a1.urdf#L842) |
| RL_thigh / com_registered | [-0.186237, 0.109723, -0.027326] | unavailable | [-0.183737, 0.108473, -0.027326] | [0.0025, -0.00125, 0] | NO MATCHING SOURCE | [CoM/kinematic input L167](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_a1/a1.xml#L167) | unavailable | [CoM/kinematic input L884](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/a1_description/urdf/a1.urdf#L884) |
| RL_calf / mass | 0.226 | unavailable | 0.166 | -0.06 | NO MATCHING SOURCE | [input L175](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_a1/a1.xml#L175) | unavailable | [input L913](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/a1_description/urdf/a1.urdf#L913) |
| RL_calf / com_registered | [-0.17827341, 0.13205, -0.331975] | unavailable | [-0.174065, 0.1308, -0.307388] | [0.00420841, -0.00125, 0.024587] | NO MATCHING SOURCE | [CoM/kinematic input L175](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_a1/a1.xml#L175) | unavailable | [CoM/kinematic input L912](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/a1_description/urdf/a1.urdf#L912) |
| RL_calf / principal_moments | [3.54834e-05, 0.00339393, 0.00340344] | unavailable | [2.57216547e-05, 0.00300467635, 0.003014022] | [-9.76174528e-06, -0.000389253655, -0.000389418] | NO MATCHING SOURCE | [inertia input L175](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_a1/a1.xml#L175) | unavailable | [inertia input L914](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/a1_description/urdf/a1.urdf#L914) |

## Raw CoM records and reporting decisions

Raw values retain the previous root-anchor registration before Kabsch; original world coordinates also remain in the snapshots. Eligible findings above use the fitted transform into M. Excluded raw records below are diagnostic numbers, not findings. No CoM suppression applies to mass or principal inertia moments.

| Entity / quantity | Raw M | Raw S | Raw H | Raw H − M | Decision | M source | S source | H source |
|---|---|---|---|---|---|---|---|---|
| robot / total_com_registered | [-0.000710149092, 0.00155169839, -0.0331727735] | unavailable | [-0.00061340794, 0.00170632246, -0.028698421] | [9.67411515e-05, 0.000154624069, 0.00447435251] | eligible; compared after Kabsch alignment | [aggregate inputs](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_a1/a1.xml#L1) | unavailable | [aggregate inputs](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/a1_description/urdf/a1.urdf#L1) |
| trunk / com_registered | [0, 0.0041, -0.0005] | unavailable | [0, 0.0041, -0.0005] | [0, 0, 4.33680869e-19] | eligible; compared after Kabsch alignment | [CoM/kinematic input L73](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_a1/a1.xml#L73) | unavailable | [CoM/kinematic input L333](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/a1_description/urdf/a1.urdf#L333) |
| FR_hip / com_registered | [0.179689, -0.047635, 3.1e-05] | unavailable | [0.177189, -0.047635, 3.1e-05] | [-0.0025, 0, -3.24583025e-18] | eligible; compared after Kabsch alignment | [CoM/kinematic input L85](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_a1/a1.xml#L85) | unavailable | [CoM/kinematic input L386](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/a1_description/urdf/a1.urdf#L386) |
| FR_thigh / com_registered | [0.179763, -0.109723, -0.027326] | unavailable | [0.177263, -0.108473, -0.027326] | [-0.0025, 0.00125, 1.73472348e-17] | eligible; compared after Kabsch alignment | [CoM/kinematic input L91](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_a1/a1.xml#L91) | unavailable | [CoM/kinematic input L428](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/a1_description/urdf/a1.urdf#L428) |
| FR_calf / com_registered | [0.18772659, -0.13205, -0.331975] | unavailable | [0.186935, -0.1308, -0.307388] | [-0.00079159, 0.00125, 0.024587] | eligible; compared after Kabsch alignment | [CoM/kinematic input L99](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_a1/a1.xml#L99) | unavailable | [CoM/kinematic input L456](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/a1_description/urdf/a1.urdf#L456) |
| FL_hip / com_registered | [0.179689, 0.047635, 3.1e-05] | unavailable | [0.177189, 0.047635, 3.1e-05] | [-0.0025, 0, -3.24583025e-18] | eligible; compared after Kabsch alignment | [CoM/kinematic input L110](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_a1/a1.xml#L110) | unavailable | [CoM/kinematic input L538](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/a1_description/urdf/a1.urdf#L538) |
| FL_thigh / com_registered | [0.179763, 0.109723, -0.027326] | unavailable | [0.177263, 0.108473, -0.027326] | [-0.0025, -0.00125, 1.73472348e-17] | eligible; compared after Kabsch alignment | [CoM/kinematic input L117](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_a1/a1.xml#L117) | unavailable | [CoM/kinematic input L580](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/a1_description/urdf/a1.urdf#L580) |
| FL_calf / com_registered | [0.18772659, 0.13205, -0.331975] | unavailable | [0.186935, 0.1308, -0.307388] | [-0.00079159, -0.00125, 0.024587] | eligible; compared after Kabsch alignment | [CoM/kinematic input L125](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_a1/a1.xml#L125) | unavailable | [CoM/kinematic input L608](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/a1_description/urdf/a1.urdf#L608) |
| RR_hip / com_registered | [-0.179689, -0.047635, 3.1e-05] | unavailable | [-0.177189, -0.047635, 3.1e-05] | [0.0025, 0, -3.24583025e-18] | eligible; compared after Kabsch alignment | [CoM/kinematic input L136](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_a1/a1.xml#L136) | unavailable | [CoM/kinematic input L690](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/a1_description/urdf/a1.urdf#L690) |
| RR_thigh / com_registered | [-0.186237, -0.109723, -0.027326] | unavailable | [-0.183737, -0.108473, -0.027326] | [0.0025, 0.00125, 1.73472348e-17] | eligible; compared after Kabsch alignment | [CoM/kinematic input L142](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_a1/a1.xml#L142) | unavailable | [CoM/kinematic input L732](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/a1_description/urdf/a1.urdf#L732) |
| RR_calf / com_registered | [-0.17827341, -0.13205, -0.331975] | unavailable | [-0.174065, -0.1308, -0.307388] | [0.00420841, 0.00125, 0.024587] | eligible; compared after Kabsch alignment | [CoM/kinematic input L150](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_a1/a1.xml#L150) | unavailable | [CoM/kinematic input L760](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/a1_description/urdf/a1.urdf#L760) |
| RL_hip / com_registered | [-0.179689, 0.047635, 3.1e-05] | unavailable | [-0.177189, 0.047635, 3.1e-05] | [0.0025, 0, -3.24583025e-18] | eligible; compared after Kabsch alignment | [CoM/kinematic input L161](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_a1/a1.xml#L161) | unavailable | [CoM/kinematic input L842](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/a1_description/urdf/a1.urdf#L842) |
| RL_thigh / com_registered | [-0.186237, 0.109723, -0.027326] | unavailable | [-0.183737, 0.108473, -0.027326] | [0.0025, -0.00125, 1.73472348e-17] | eligible; compared after Kabsch alignment | [CoM/kinematic input L167](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_a1/a1.xml#L167) | unavailable | [CoM/kinematic input L884](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/a1_description/urdf/a1.urdf#L884) |
| RL_calf / com_registered | [-0.17827341, 0.13205, -0.331975] | unavailable | [-0.174065, 0.1308, -0.307388] | [0.00420841, -0.00125, 0.024587] | eligible; compared after Kabsch alignment | [CoM/kinematic input L175](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_a1/a1.xml#L175) | unavailable | [CoM/kinematic input L912](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/a1_description/urdf/a1.urdf#L912) |

## Mass accounting

Every contributing compiled body mass is listed here so total/subtree sums can be checked. Links point to explicit inertials or to geometry inputs when the compiler inferred a mass. CoM links identify inertial inputs; world coordinates additionally use the ancestor transforms and the registration recorded below.

| M body | M kg / source | S kg / source | H kg / source |
|---|---|---|---|
| trunk | 4.713 / [input L73](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_a1/a1.xml#L73) | unavailable | 6 / [input L334](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/a1_description/urdf/a1.urdf#L334) |
| FR_hip | 0.696 / [input L85](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_a1/a1.xml#L85) | unavailable | 0.696 / [input L387](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/a1_description/urdf/a1.urdf#L387) |
| FR_thigh | 1.013 / [input L91](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_a1/a1.xml#L91) | unavailable | 1.013 / [input L429](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/a1_description/urdf/a1.urdf#L429) |
| FR_calf | 0.226 / [input L99](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_a1/a1.xml#L99) | unavailable | 0.166 / [input L457](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/a1_description/urdf/a1.urdf#L457) |
| FL_hip | 0.696 / [input L110](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_a1/a1.xml#L110) | unavailable | 0.696 / [input L539](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/a1_description/urdf/a1.urdf#L539) |
| FL_thigh | 1.013 / [input L117](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_a1/a1.xml#L117) | unavailable | 1.013 / [input L581](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/a1_description/urdf/a1.urdf#L581) |
| FL_calf | 0.226 / [input L125](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_a1/a1.xml#L125) | unavailable | 0.166 / [input L609](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/a1_description/urdf/a1.urdf#L609) |
| RR_hip | 0.696 / [input L136](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_a1/a1.xml#L136) | unavailable | 0.696 / [input L691](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/a1_description/urdf/a1.urdf#L691) |
| RR_thigh | 1.013 / [input L142](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_a1/a1.xml#L142) | unavailable | 1.013 / [input L733](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/a1_description/urdf/a1.urdf#L733) |
| RR_calf | 0.226 / [input L150](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_a1/a1.xml#L150) | unavailable | 0.166 / [input L761](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/a1_description/urdf/a1.urdf#L761) |
| RL_hip | 0.696 / [input L161](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_a1/a1.xml#L161) | unavailable | 0.696 / [input L843](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/a1_description/urdf/a1.urdf#L843) |
| RL_thigh | 1.013 / [input L167](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_a1/a1.xml#L167) | unavailable | 1.013 / [input L885](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/a1_description/urdf/a1.urdf#L885) |
| RL_calf | 0.226 / [input L175](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/unitree_a1/a1.xml#L175) | unavailable | 0.166 / [input L913](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/a1_description/urdf/a1.urdf#L913) |
| upstream-only FL_foot | unavailable | unavailable | 0.06 / [input L633](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/a1_description/urdf/a1.urdf#L633) |
| upstream-only FL_thigh_shoulder | unavailable | unavailable | 0.168992552 / [geometry/inference input L549](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/a1_description/urdf/a1.urdf#L549) |
| upstream-only FR_foot | unavailable | unavailable | 0.06 / [input L481](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/a1_description/urdf/a1.urdf#L481) |
| upstream-only FR_thigh_shoulder | unavailable | unavailable | 0.168992552 / [geometry/inference input L397](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/a1_description/urdf/a1.urdf#L397) |
| upstream-only RL_foot | unavailable | unavailable | 0.06 / [input L937](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/a1_description/urdf/a1.urdf#L937) |
| upstream-only RL_thigh_shoulder | unavailable | unavailable | 0.168992552 / [geometry/inference input L853](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/a1_description/urdf/a1.urdf#L853) |
| upstream-only RR_foot | unavailable | unavailable | 0.06 / [input L785](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/a1_description/urdf/a1.urdf#L785) |
| upstream-only RR_thigh_shoulder | unavailable | unavailable | 0.168992552 / [geometry/inference input L701](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/a1_description/urdf/a1.urdf#L701) |
| upstream-only base | unavailable | unavailable | 0 / [geometry/inference input L305](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/a1_description/urdf/a1.urdf#L305) |
| upstream-only imu_link | unavailable | unavailable | 0.001 / [input L345](https://github.com/unitreerobotics/unitree_ros/blob/157ff950351e5f535e03c5d85a16b7d594b3dbcc/robots/a1_description/urdf/a1.urdf#L345) |

## Coverage and unmatched elements

```json
{
  "mapping_h": {
    "bodies": {
      "trunk": "trunk",
      "FR_hip": "FR_hip",
      "FR_thigh": "FR_thigh",
      "FR_calf": "FR_calf",
      "FL_hip": "FL_hip",
      "FL_thigh": "FL_thigh",
      "FL_calf": "FL_calf",
      "RR_hip": "RR_hip",
      "RR_thigh": "RR_thigh",
      "RR_calf": "RR_calf",
      "RL_hip": "RL_hip",
      "RL_thigh": "RL_thigh",
      "RL_calf": "RL_calf"
    },
    "joints": {
      "FR_hip_joint": "FR_hip_joint",
      "FR_thigh_joint": "FR_thigh_joint",
      "FR_calf_joint": "FR_calf_joint",
      "FL_hip_joint": "FL_hip_joint",
      "FL_thigh_joint": "FL_thigh_joint",
      "FL_calf_joint": "FL_calf_joint",
      "RR_hip_joint": "RR_hip_joint",
      "RR_thigh_joint": "RR_thigh_joint",
      "RR_calf_joint": "RR_calf_joint",
      "RL_hip_joint": "RL_hip_joint",
      "RL_thigh_joint": "RL_thigh_joint",
      "RL_calf_joint": "RL_calf_joint"
    },
    "body_methods": {
      "trunk": "name",
      "FR_hip": "name",
      "FR_thigh": "name",
      "FR_calf": "name",
      "FL_hip": "name",
      "FL_thigh": "name",
      "FL_calf": "name",
      "RR_hip": "name",
      "RR_thigh": "name",
      "RR_calf": "name",
      "RL_hip": "name",
      "RL_thigh": "name",
      "RL_calf": "name"
    },
    "joint_methods": {
      "FR_hip_joint": "name",
      "FR_thigh_joint": "name",
      "FR_calf_joint": "name",
      "FL_hip_joint": "name",
      "FL_thigh_joint": "name",
      "FL_calf_joint": "name",
      "RR_hip_joint": "name",
      "RR_thigh_joint": "name",
      "RR_calf_joint": "name",
      "RL_hip_joint": "name",
      "RL_thigh_joint": "name",
      "RL_calf_joint": "name"
    },
    "unmatched_m_bodies": [],
    "unmatched_upstream_bodies": [
      "FL_foot",
      "FL_thigh_shoulder",
      "FR_foot",
      "FR_thigh_shoulder",
      "RL_foot",
      "RL_thigh_shoulder",
      "RR_foot",
      "RR_thigh_shoulder",
      "base",
      "imu_link"
    ],
    "unmatched_m_joints": [],
    "unmatched_upstream_joints": [],
    "registration_anchor": {
      "M": "trunk",
      "H": "trunk",
      "root_unmatched": false
    }
  },
  "mapping_s": null,
  "unavailable": [
    {
      "entity": "FR_hip_joint",
      "other_entity": "FR_hip_joint",
      "quantity": "force",
      "tolerance": "limit",
      "m": 33.5,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "FR_hip_joint",
      "other_entity": "FR_hip_joint",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 21.0,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "FR_thigh_joint",
      "other_entity": "FR_thigh_joint",
      "quantity": "force",
      "tolerance": "limit",
      "m": 33.5,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "FR_thigh_joint",
      "other_entity": "FR_thigh_joint",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 21.0,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "FR_calf_joint",
      "other_entity": "FR_calf_joint",
      "quantity": "force",
      "tolerance": "limit",
      "m": 33.5,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "FR_calf_joint",
      "other_entity": "FR_calf_joint",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 21.0,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "FL_hip_joint",
      "other_entity": "FL_hip_joint",
      "quantity": "force",
      "tolerance": "limit",
      "m": 33.5,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "FL_hip_joint",
      "other_entity": "FL_hip_joint",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 21.0,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "FL_thigh_joint",
      "other_entity": "FL_thigh_joint",
      "quantity": "force",
      "tolerance": "limit",
      "m": 33.5,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "FL_thigh_joint",
      "other_entity": "FL_thigh_joint",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 21.0,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "FL_calf_joint",
      "other_entity": "FL_calf_joint",
      "quantity": "force",
      "tolerance": "limit",
      "m": 33.5,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "FL_calf_joint",
      "other_entity": "FL_calf_joint",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 21.0,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "RR_hip_joint",
      "other_entity": "RR_hip_joint",
      "quantity": "force",
      "tolerance": "limit",
      "m": 33.5,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "RR_hip_joint",
      "other_entity": "RR_hip_joint",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 21.0,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "RR_thigh_joint",
      "other_entity": "RR_thigh_joint",
      "quantity": "force",
      "tolerance": "limit",
      "m": 33.5,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "RR_thigh_joint",
      "other_entity": "RR_thigh_joint",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 21.0,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "RR_calf_joint",
      "other_entity": "RR_calf_joint",
      "quantity": "force",
      "tolerance": "limit",
      "m": 33.5,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "RR_calf_joint",
      "other_entity": "RR_calf_joint",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 21.0,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "RL_hip_joint",
      "other_entity": "RL_hip_joint",
      "quantity": "force",
      "tolerance": "limit",
      "m": 33.5,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "RL_hip_joint",
      "other_entity": "RL_hip_joint",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 21.0,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "RL_thigh_joint",
      "other_entity": "RL_thigh_joint",
      "quantity": "force",
      "tolerance": "limit",
      "m": 33.5,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "RL_thigh_joint",
      "other_entity": "RL_thigh_joint",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 21.0,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "RL_calf_joint",
      "other_entity": "RL_calf_joint",
      "quantity": "force",
      "tolerance": "limit",
      "m": 33.5,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "RL_calf_joint",
      "other_entity": "RL_calf_joint",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 21.0,
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
| FR_hip_joint / force | 33.5 | unavailable | unavailable |
| FR_hip_joint / velocity | unavailable | unavailable | 21 |
| FR_thigh_joint / force | 33.5 | unavailable | unavailable |
| FR_thigh_joint / velocity | unavailable | unavailable | 21 |
| FR_calf_joint / force | 33.5 | unavailable | unavailable |
| FR_calf_joint / velocity | unavailable | unavailable | 21 |
| FL_hip_joint / force | 33.5 | unavailable | unavailable |
| FL_hip_joint / velocity | unavailable | unavailable | 21 |
| FL_thigh_joint / force | 33.5 | unavailable | unavailable |
| FL_thigh_joint / velocity | unavailable | unavailable | 21 |
| FL_calf_joint / force | 33.5 | unavailable | unavailable |
| FL_calf_joint / velocity | unavailable | unavailable | 21 |
| RR_hip_joint / force | 33.5 | unavailable | unavailable |
| RR_hip_joint / velocity | unavailable | unavailable | 21 |
| RR_thigh_joint / force | 33.5 | unavailable | unavailable |
| RR_thigh_joint / velocity | unavailable | unavailable | 21 |
| RR_calf_joint / force | 33.5 | unavailable | unavailable |
| RR_calf_joint / velocity | unavailable | unavailable | 21 |
| RL_hip_joint / force | 33.5 | unavailable | unavailable |
| RL_hip_joint / velocity | unavailable | unavailable | 21 |
| RL_thigh_joint / force | 33.5 | unavailable | unavailable |
| RL_thigh_joint / velocity | unavailable | unavailable | 21 |
| RL_calf_joint / force | 33.5 | unavailable | unavailable |
| RL_calf_joint / velocity | unavailable | unavailable | 21 |
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
  "robots/a1_description/meshes/calf.dae",
  "robots/a1_description/meshes/hip.dae",
  "robots/a1_description/meshes/thigh.dae",
  "robots/a1_description/meshes/thigh_mirror.dae",
  "robots/a1_description/meshes/trunk.dae",
  "robots/a1_description/urdf/a1.urdf"
]
```

## Self comparisons

```json
[
  {
    "file": "unitree_a1/a1.xml",
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
      "NO MATCHING SOURCE": 28
    },
    "classifications_changed": 0,
    "finding_membership_changes": 0
  },
  "2": {
    "provenance_method": "none",
    "counts": {
      "NO MATCHING SOURCE": 28
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
      "unitree_a1/a1.xml"
    ],
    "registration": {
      "translation": [
        0.0,
        0.0,
        0.43
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
      "FR_thigh_shoulder",
      "FL_thigh_shoulder",
      "RR_thigh_shoulder",
      "RL_thigh_shoulder"
    ],
    "assets_loaded": 13,
    "mesh_conversions": [
      {
        "file": "robots/a1_description/meshes/trunk.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "robots/a1_description/meshes/hip.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "robots/a1_description/meshes/thigh_mirror.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "robots/a1_description/meshes/calf.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "robots/a1_description/meshes/hip.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "robots/a1_description/meshes/thigh.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "robots/a1_description/meshes/calf.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "robots/a1_description/meshes/hip.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "robots/a1_description/meshes/thigh_mirror.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "robots/a1_description/meshes/calf.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "robots/a1_description/meshes/hip.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "robots/a1_description/meshes/thigh.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "robots/a1_description/meshes/calf.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      }
    ],
    "nonphysical_normalizations": [],
    "xacro_arguments": {},
    "source_dependencies": [
      "robots/a1_description/urdf/a1.urdf",
      "robots/a1_description/meshes/trunk.dae",
      "robots/a1_description/meshes/hip.dae",
      "robots/a1_description/meshes/thigh_mirror.dae",
      "robots/a1_description/meshes/calf.dae",
      "robots/a1_description/meshes/hip.dae",
      "robots/a1_description/meshes/thigh.dae",
      "robots/a1_description/meshes/calf.dae",
      "robots/a1_description/meshes/hip.dae",
      "robots/a1_description/meshes/thigh_mirror.dae",
      "robots/a1_description/meshes/calf.dae",
      "robots/a1_description/meshes/hip.dae",
      "robots/a1_description/meshes/thigh.dae",
      "robots/a1_description/meshes/calf.dae"
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
  "historical_snapshots_reused": 3,
  "primary_physics_unchanged": true,
  "source_matching": "original raw-value provenance criteria retained; kinematic guard applies to reported CoM"
}
```
