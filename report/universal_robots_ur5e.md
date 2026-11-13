# universal_robots_ur5e

Status: **partial history**. Provenance: **unknown**, confidence **incomplete**.

Unresolved historical compilation prevents selecting or rejecting a matching source. Pairwise M/H differences are reported with unknown provenance.

M: `https://github.com/google-deepmind/mujoco_menagerie`, `universal_robots_ur5e/ur5e.xml`, commit `370c43965323c0944b433b202aac5058b5f907a9`.
H: `https://github.com/ros-industrial/universal_robot`, `ur_description/urdf/ur5e.xacro`, commit `39ad110d8f2e8f66856a201cca88aa7a7025e3eb`.
S: unavailable. A machine-readable H can still be compared to M; no-match differences are never counted as STALE.

Limit semantics: MJCF effort values are supported actuator torque/force envelopes. URDF effort and velocity values are manufacturer declarations retained from XML; MuJoCo does not enforce those tags. Such declaration comparisons are explicitly distinct from compiled inertial/range quantities.


## Source evidence

```json
[
  {
    "url": "https://github.com/kevinzakka/obj2mjcf",
    "document": "universal_robots_ur5e/README.md",
    "commit": "370c43965323c0944b433b202aac5058b5f907a9",
    "current": true
  },
  {
    "url": "https://github.com/ros-industrial/universal_robot/tree/kinetic-devel/ur_e_description",
    "document": "universal_robots_ur5e/README.md",
    "commit": "370c43965323c0944b433b202aac5058b5f907a9",
    "current": true
  },
  {
    "url": "https://github.com/ros-industrial/universal_robot/tree/kinetic-devel/ur_e_description/meshes/ur5e/visual",
    "document": "universal_robots_ur5e/README.md",
    "commit": "370c43965323c0944b433b202aac5058b5f907a9",
    "current": true
  }
]
```


## Kinematics consistency

A proper Kabsch rigid transform aligns all matched zero-pose body origins. The maximum per-origin residual and signed hinge/slide axis angles determine whether CoM can be compared; RMS is also recorded. Fewer than three non-collinear origins give insufficient kinematic coverage. CoM records that fail either required M/H or M/S check are excluded from counts and largest discrepancies. Masses, principal moments and raw joint ranges remain unchanged; a flagged range still requires convention review.

| Pair | Status | Origins / rank | RMS / maximum mm | Disagreeing / checked axes |
|---|---|---:|---:|---:|
| M/H | kinematic convention differs | 7 / 3 | 64.1309564 / 102.08647 | 6 / 6 |

Exact fitted transforms, per-origin residuals, thresholds and axis vectors:

```json
{
  "M/H": {
    "status": "kinematic convention differs",
    "matched_body_origins": 7,
    "position_threshold_m": 0.005,
    "axis_threshold_rad": 0.005,
    "residual_definition": "maximum Euclidean residual over matched body origins; Kabsch minimizes RMS, which is also recorded",
    "coordinate_frames": "each snapshot registered to its matched report anchor",
    "anchor_m": "base",
    "anchor_other": "base",
    "rotation_other_to_m": [
      [
        -0.9879566568982976,
        -0.14747242582097467,
        -0.046835111965442024
      ],
      [
        0.13780889631745286,
        -0.9762702415839286,
        0.16704826695725472
      ],
      [
        -0.07035873923048858,
        0.15858215227488204,
        0.9848356963441981
      ]
    ],
    "translation_other_to_m": [
      -0.00047046901193703583,
      0.028458778531504865,
      -0.0012886757436793572
    ],
    "rms_residual_m": 0.06413095642270522,
    "max_residual_m": 0.1020864699298386,
    "fit_rank": 3,
    "axis_checks": [
      {
        "joint_m": "shoulder_pan_joint",
        "joint_other": "shoulder_pan_joint",
        "axis_m": [
          0.0,
          0.0,
          1.0
        ],
        "axis_other_aligned": [
          -0.04683511196544204,
          0.16704826695725478,
          0.9848356963441984
        ],
        "angle_rad": 0.17437193246725863,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "shoulder_lift_joint",
        "joint_other": "shoulder_lift_joint",
        "axis_m": [
          0.0,
          1.0,
          0.0
        ],
        "axis_other_aligned": [
          0.14747242583058076,
          0.9762702415496669,
          -0.15858215247687535
        ],
        "angle_rad": 0.21828516732146636,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "elbow_joint",
        "joint_other": "elbow_joint",
        "axis_m": [
          0.0,
          1.0,
          0.0
        ],
        "axis_other_aligned": [
          0.14747242583058076,
          0.9762702415496669,
          -0.15858215247687535
        ],
        "angle_rad": 0.21828516732146636,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "wrist_1_joint",
        "joint_other": "wrist_1_joint",
        "axis_m": [
          0.0,
          1.0,
          0.0
        ],
        "axis_other_aligned": [
          0.14747242583058076,
          0.9762702415496669,
          -0.15858215247687535
        ],
        "angle_rad": 0.21828516732146636,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "wrist_2_joint",
        "joint_other": "wrist_2_joint",
        "axis_m": [
          4.474228634151479e-17,
          0.0,
          -1.0
        ],
        "axis_other_aligned": [
          0.04683511190494781,
          -0.1670482673577277,
          -0.9848356962791469
        ],
        "angle_rad": 0.17437193284221775,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "wrist_3_joint",
        "joint_other": "wrist_3_joint",
        "axis_m": [
          0.0,
          1.0,
          0.0
        ],
        "axis_other_aligned": [
          0.14747242583058065,
          0.9762702415496669,
          -0.15858215247687535
        ],
        "angle_rad": 0.21828516732146633,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      }
    ],
    "axis_disagreements": [
      {
        "joint_m": "shoulder_pan_joint",
        "joint_other": "shoulder_pan_joint",
        "axis_m": [
          0.0,
          0.0,
          1.0
        ],
        "axis_other_aligned": [
          -0.04683511196544204,
          0.16704826695725478,
          0.9848356963441984
        ],
        "angle_rad": 0.17437193246725863,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "shoulder_lift_joint",
        "joint_other": "shoulder_lift_joint",
        "axis_m": [
          0.0,
          1.0,
          0.0
        ],
        "axis_other_aligned": [
          0.14747242583058076,
          0.9762702415496669,
          -0.15858215247687535
        ],
        "angle_rad": 0.21828516732146636,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "elbow_joint",
        "joint_other": "elbow_joint",
        "axis_m": [
          0.0,
          1.0,
          0.0
        ],
        "axis_other_aligned": [
          0.14747242583058076,
          0.9762702415496669,
          -0.15858215247687535
        ],
        "angle_rad": 0.21828516732146636,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "wrist_1_joint",
        "joint_other": "wrist_1_joint",
        "axis_m": [
          0.0,
          1.0,
          0.0
        ],
        "axis_other_aligned": [
          0.14747242583058076,
          0.9762702415496669,
          -0.15858215247687535
        ],
        "angle_rad": 0.21828516732146636,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "wrist_2_joint",
        "joint_other": "wrist_2_joint",
        "axis_m": [
          4.474228634151479e-17,
          0.0,
          -1.0
        ],
        "axis_other_aligned": [
          0.04683511190494781,
          -0.1670482673577277,
          -0.9848356962791469
        ],
        "angle_rad": 0.17437193284221775,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "wrist_3_joint",
        "joint_other": "wrist_3_joint",
        "axis_m": [
          0.0,
          1.0,
          0.0
        ],
        "axis_other_aligned": [
          0.14747242583058065,
          0.9762702415496669,
          -0.15858215247687535
        ],
        "angle_rad": 0.21828516732146633,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      }
    ],
    "com_eligible": false,
    "covariance_singular_values": [
      1.0240888864747177,
      0.02621632780098209,
      0.006138240073576136
    ],
    "origin_residuals_m": {
      "base": 0.02849182517440367,
      "shoulder_link": 0.056349008019282484,
      "upper_arm_link": 0.08290038031896445,
      "forearm_link": 0.03051925902923546,
      "wrist_1_link": 0.07353103524081904,
      "wrist_2_link": 0.1020864699298386,
      "wrist_3_link": 0.03420677535614165
    },
    "reason": "Origin residual exceeds threshold and/or matched signed joint axes disagree"
  }
}
```


## Every reported quantity difference

Counts are quantity records, including correlated total/subtree/body mass records; they are not independent robot defects.

| Entity / quantity | M | S | H | H − M | Class | M source | S source | H source |
|---|---|---|---|---|---|---|---|---|
| robot / total_mass | 20.9949 | unavailable | 21.7 | 0.7051 | unknown | [aggregate inputs](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/universal_robots_ur5e/ur5e.xml#L1) | unavailable | [aggregate inputs](https://github.com/ros-industrial/universal_robot/blob/39ad110d8f2e8f66856a201cca88aa7a7025e3eb/ur_description/urdf/ur5e.xacro#L1) |
| base / mass | 4 | unavailable | 0 | -4 | unknown | [input L64](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/universal_robots_ur5e/ur5e.xml#L64) | unavailable | [geometry/inference input L365](https://github.com/ros-industrial/universal_robot/blob/39ad110d8f2e8f66856a201cca88aa7a7025e3eb/ur_description/urdf/inc/ur_macro.xacro#L365) |
| base / subtree_mass | 20.9949 | unavailable | 0 | -20.9949 | unknown | [subtree root L63](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/universal_robots_ur5e/ur5e.xml#L63) | unavailable | [subtree root L365](https://github.com/ros-industrial/universal_robot/blob/39ad110d8f2e8f66856a201cca88aa7a7025e3eb/ur_description/urdf/inc/ur_macro.xacro#L365) |
| base / principal_moments | [0.00443333156, 0.00443333156, 0.0072] | unavailable | [0, 0, 0] | [-0.00443333156, -0.00443333156, -0.0072] | unknown | [inertia input L64](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/universal_robots_ur5e/ur5e.xml#L64) | unavailable | [geometry/inference input L365](https://github.com/ros-industrial/universal_robot/blob/39ad110d8f2e8f66856a201cca88aa7a7025e3eb/ur_description/urdf/inc/ur_macro.xacro#L365) |
| shoulder_link / mass | 3.7 | unavailable | 3.761 | 0.061 | unknown | [input L68](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/universal_robots_ur5e/ur5e.xml#L68) | unavailable | [input L117](https://github.com/ros-industrial/universal_robot/blob/39ad110d8f2e8f66856a201cca88aa7a7025e3eb/ur_description/urdf/inc/ur_macro.xacro#L117) |
| shoulder_link / subtree_mass | 16.9949 | unavailable | 17.7 | 0.7051 | unknown | [subtree root L67](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/universal_robots_ur5e/ur5e.xml#L67) | unavailable | [subtree root L100](https://github.com/ros-industrial/universal_robot/blob/39ad110d8f2e8f66856a201cca88aa7a7025e3eb/ur_description/urdf/inc/ur_macro.xacro#L100) |
| shoulder_link / principal_moments | [0.00666, 0.0102675, 0.0102675] | unavailable | [0.00602477583, 0.00700030488, 0.00703078929] | [-0.000635224169, -0.00326719512, -0.00323671071] | unknown | [inertia input L68](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/universal_robots_ur5e/ur5e.xml#L68) | unavailable | [inertia input L126](https://github.com/ros-industrial/universal_robot/blob/39ad110d8f2e8f66856a201cca88aa7a7025e3eb/ur_description/urdf/inc/ur_macro.xacro#L126) |
| upper_arm_link / mass | 8.393 | unavailable | 8.058 | -0.335 | unknown | [input L75](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/universal_robots_ur5e/ur5e.xml#L75) | unavailable | [input L146](https://github.com/ros-industrial/universal_robot/blob/39ad110d8f2e8f66856a201cca88aa7a7025e3eb/ur_description/urdf/inc/ur_macro.xacro#L146) |
| upper_arm_link / subtree_mass | 13.2949 | unavailable | 13.939 | 0.6441 | unknown | [subtree root L74](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/universal_robots_ur5e/ur5e.xml#L74) | unavailable | [subtree root L129](https://github.com/ros-industrial/universal_robot/blob/39ad110d8f2e8f66856a201cca88aa7a7025e3eb/ur_description/urdf/inc/ur_macro.xacro#L129) |
| upper_arm_link / principal_moments | [0.0151074, 0.133886, 0.133886] | unavailable | [0.0150588408, 0.332472068, 0.333880871] | [-4.8559246e-05, 0.198586068, 0.199994871] | unknown | [inertia input L75](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/universal_robots_ur5e/ur5e.xml#L75) | unavailable | [inertia input L155](https://github.com/ros-industrial/universal_robot/blob/39ad110d8f2e8f66856a201cca88aa7a7025e3eb/ur_description/urdf/inc/ur_macro.xacro#L155) |
| forearm_link / mass | 2.275 | unavailable | 2.846 | 0.571 | unknown | [input L84](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/universal_robots_ur5e/ur5e.xml#L84) | unavailable | [input L175](https://github.com/ros-industrial/universal_robot/blob/39ad110d8f2e8f66856a201cca88aa7a7025e3eb/ur_description/urdf/inc/ur_macro.xacro#L175) |
| forearm_link / subtree_mass | 4.9019 | unavailable | 5.881 | 0.9791 | unknown | [subtree root L83](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/universal_robots_ur5e/ur5e.xml#L83) | unavailable | [subtree root L158](https://github.com/ros-industrial/universal_robot/blob/39ad110d8f2e8f66856a201cca88aa7a7025e3eb/ur_description/urdf/inc/ur_macro.xacro#L158) |
| forearm_link / principal_moments | [0.004095, 0.0311796, 0.0311796] | unavailable | [0.0039710289, 0.0785102224, 0.0787927087] | [-0.000123971095, 0.0473306224, 0.0476131087] | unknown | [inertia input L84](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/universal_robots_ur5e/ur5e.xml#L84) | unavailable | [inertia input L184](https://github.com/ros-industrial/universal_robot/blob/39ad110d8f2e8f66856a201cca88aa7a7025e3eb/ur_description/urdf/inc/ur_macro.xacro#L184) |
| wrist_1_link / mass | 1.219 | unavailable | 1.37 | 0.151 | unknown | [input L93](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/universal_robots_ur5e/ur5e.xml#L93) | unavailable | [input L205](https://github.com/ros-industrial/universal_robot/blob/39ad110d8f2e8f66856a201cca88aa7a7025e3eb/ur_description/urdf/inc/ur_macro.xacro#L205) |
| wrist_1_link / subtree_mass | 2.6269 | unavailable | 3.035 | 0.4081 | unknown | [subtree root L92](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/universal_robots_ur5e/ur5e.xml#L92) | unavailable | [subtree root L187](https://github.com/ros-industrial/universal_robot/blob/39ad110d8f2e8f66856a201cca88aa7a7025e3eb/ur_description/urdf/inc/ur_macro.xacro#L187) |
| wrist_1_link / principal_moments | [0.0021942, 0.0025599, 0.0025599] | unavailable | [0.00119867561, 0.00142362737, 0.00165501702] | [-0.000995524386, -0.00113627263, -0.000904882983] | unknown | [inertia input L93](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/universal_robots_ur5e/ur5e.xml#L93) | unavailable | [inertia input L214](https://github.com/ros-industrial/universal_robot/blob/39ad110d8f2e8f66856a201cca88aa7a7025e3eb/ur_description/urdf/inc/ur_macro.xacro#L214) |
| wrist_2_link / mass | 1.219 | unavailable | 1.3 | 0.081 | unknown | [input L100](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/universal_robots_ur5e/ur5e.xml#L100) | unavailable | [input L234](https://github.com/ros-industrial/universal_robot/blob/39ad110d8f2e8f66856a201cca88aa7a7025e3eb/ur_description/urdf/inc/ur_macro.xacro#L234) |
| wrist_2_link / subtree_mass | 1.4079 | unavailable | 1.665 | 0.2571 | unknown | [subtree root L99](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/universal_robots_ur5e/ur5e.xml#L99) | unavailable | [subtree root L217](https://github.com/ros-industrial/universal_robot/blob/39ad110d8f2e8f66856a201cca88aa7a7025e3eb/ur_description/urdf/inc/ur_macro.xacro#L217) |
| wrist_2_link / principal_moments | [0.0021942, 0.0025599, 0.0025599] | unavailable | [0.000958139662, 0.00128606634, 0.00135637399] | [-0.00123606034, -0.00127383366, -0.00120352601] | unknown | [inertia input L100](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/universal_robots_ur5e/ur5e.xml#L100) | unavailable | [inertia input L243](https://github.com/ros-industrial/universal_robot/blob/39ad110d8f2e8f66856a201cca88aa7a7025e3eb/ur_description/urdf/inc/ur_macro.xacro#L243) |
| wrist_3_link / mass | 0.1889 | unavailable | 0.365 | 0.1761 | unknown | [input L109](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/universal_robots_ur5e/ur5e.xml#L109) | unavailable | [input L267](https://github.com/ros-industrial/universal_robot/blob/39ad110d8f2e8f66856a201cca88aa7a7025e3eb/ur_description/urdf/inc/ur_macro.xacro#L267) |
| wrist_3_link / subtree_mass | 0.1889 | unavailable | 0.365 | 0.1761 | unknown | [subtree root L107](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/universal_robots_ur5e/ur5e.xml#L107) | unavailable | [subtree root L246](https://github.com/ros-industrial/universal_robot/blob/39ad110d8f2e8f66856a201cca88aa7a7025e3eb/ur_description/urdf/inc/ur_macro.xacro#L246) |
| wrist_3_link / principal_moments | [9.90863e-05, 9.90863e-05, 0.000132134] | unavailable | [0.000186938023, 0.000189069206, 0.000257572771] | [8.78517231e-05, 8.99829063e-05, 0.000125438771] | unknown | [inertia input L109](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/universal_robots_ur5e/ur5e.xml#L109) | unavailable | [inertia input L276](https://github.com/ros-industrial/universal_robot/blob/39ad110d8f2e8f66856a201cca88aa7a7025e3eb/ur_description/urdf/inc/ur_macro.xacro#L276) |

## Raw CoM records and reporting decisions

Raw values retain the previous root-anchor registration before Kabsch; original world coordinates also remain in the snapshots. Eligible findings above use the fitted transform into M. Excluded raw records below are diagnostic numbers, not findings. No CoM suppression applies to mass or principal inertia moments.

| Entity / quantity | Raw M | Raw S | Raw H | Raw H − M | Decision | M source | S source | H source |
|---|---|---|---|---|---|---|---|---|
| robot / total_com_registered | [0.254464884, 0.0733864268, 0.125238925] | unavailable | [-0.280708673, -0.0670693583, 0.119533847] | [-0.535173557, -0.140455785, -0.00570507724] | M/H: kinematic convention differs | [aggregate inputs](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/universal_robots_ur5e/ur5e.xml#L1) | unavailable | [aggregate inputs](https://github.com/ros-industrial/universal_robot/blob/39ad110d8f2e8f66856a201cca88aa7a7025e3eb/ur_description/urdf/ur5e.xacro#L1) |
| base / com_registered | [0, 0, 0] | unavailable | [0, 0, 0] | [0, 0, 0] | M/H: kinematic convention differs | [CoM/kinematic input L64](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/universal_robots_ur5e/ur5e.xml#L64) | unavailable | [geometry/inference input L365](https://github.com/ros-industrial/universal_robot/blob/39ad110d8f2e8f66856a201cca88aa7a7025e3eb/ur_description/urdf/inc/ur_macro.xacro#L365) |
| shoulder_link / com_registered | [0, 0, 0.163] | unavailable | [-2.40648351e-35, -0.00193, 0.13689] | [-2.40648351e-35, -0.00193, -0.02611] | M/H: kinematic convention differs | [CoM/kinematic input L68](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/universal_robots_ur5e/ur5e.xml#L68) | unavailable | [CoM/kinematic input L118](https://github.com/ros-industrial/universal_robot/blob/39ad110d8f2e8f66856a201cca88aa7a7025e3eb/ur_description/urdf/inc/ur_macro.xacro#L118) |
| upper_arm_link / com_registered | [0.2125, 0.138, 0.163] | unavailable | [-0.2125, -0.11336, 0.1625] | [-0.425, -0.25136, -0.000500000023] | M/H: kinematic convention differs | [CoM/kinematic input L75](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/universal_robots_ur5e/ur5e.xml#L75) | unavailable | [CoM/kinematic input L147](https://github.com/ros-industrial/universal_robot/blob/39ad110d8f2e8f66856a201cca88aa7a7025e3eb/ur_description/urdf/inc/ur_macro.xacro#L147) |
| forearm_link / com_registered | [0.621, 0.007, 0.163] | unavailable | [-0.6672, -0.0265, 0.1625] | [-1.2882, -0.0335, -0.000500000005] | M/H: kinematic convention differs | [CoM/kinematic input L84](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/universal_robots_ur5e/ur5e.xml#L84) | unavailable | [CoM/kinematic input L176](https://github.com/ros-industrial/universal_robot/blob/39ad110d8f2e8f66856a201cca88aa7a7025e3eb/ur_description/urdf/inc/ur_macro.xacro#L176) |
| wrist_1_link / com_registered | [0.817, 0.134, 0.163] | unavailable | [-0.8172, -0.1315, 0.14616] | [-1.6342, -0.2655, -0.01684] | M/H: kinematic convention differs | [CoM/kinematic input L93](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/universal_robots_ur5e/ur5e.xml#L93) | unavailable | [CoM/kinematic input L206](https://github.com/ros-industrial/universal_robot/blob/39ad110d8f2e8f66856a201cca88aa7a7025e3eb/ur_description/urdf/inc/ur_macro.xacro#L206) |
| wrist_2_link / com_registered | [0.817, 0.134, 0.063] | unavailable | [-0.8172, -0.14964, 0.0646] | [-1.6342, -0.28364, 0.00159999997] | M/H: kinematic convention differs | [CoM/kinematic input L100](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/universal_robots_ur5e/ur5e.xml#L100) | unavailable | [CoM/kinematic input L235](https://github.com/ros-industrial/universal_robot/blob/39ad110d8f2e8f66856a201cca88aa7a7025e3eb/ur_description/urdf/inc/ur_macro.xacro#L235) |
| wrist_3_link / com_registered | [0.817, 0.2111683, 0.063] | unavailable | [-0.8172, -0.231741, 0.0628] | [-1.6342, -0.4429093, -0.000200000048] | M/H: kinematic convention differs | [CoM/kinematic input L109](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/universal_robots_ur5e/ur5e.xml#L109) | unavailable | [CoM/kinematic input L268](https://github.com/ros-industrial/universal_robot/blob/39ad110d8f2e8f66856a201cca88aa7a7025e3eb/ur_description/urdf/inc/ur_macro.xacro#L268) |

## Mass accounting

Every contributing compiled body mass is listed here so total/subtree sums can be checked. Links point to explicit inertials or to geometry inputs when the compiler inferred a mass. CoM links identify inertial inputs; world coordinates additionally use the ancestor transforms and the registration recorded below.

| M body | M kg / source | S kg / source | H kg / source |
|---|---|---|---|
| base | 4 / [input L64](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/universal_robots_ur5e/ur5e.xml#L64) | unavailable | 0 / [geometry/inference input L365](https://github.com/ros-industrial/universal_robot/blob/39ad110d8f2e8f66856a201cca88aa7a7025e3eb/ur_description/urdf/inc/ur_macro.xacro#L365) |
| shoulder_link | 3.7 / [input L68](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/universal_robots_ur5e/ur5e.xml#L68) | unavailable | 3.761 / [input L117](https://github.com/ros-industrial/universal_robot/blob/39ad110d8f2e8f66856a201cca88aa7a7025e3eb/ur_description/urdf/inc/ur_macro.xacro#L117) |
| upper_arm_link | 8.393 / [input L75](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/universal_robots_ur5e/ur5e.xml#L75) | unavailable | 8.058 / [input L146](https://github.com/ros-industrial/universal_robot/blob/39ad110d8f2e8f66856a201cca88aa7a7025e3eb/ur_description/urdf/inc/ur_macro.xacro#L146) |
| forearm_link | 2.275 / [input L84](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/universal_robots_ur5e/ur5e.xml#L84) | unavailable | 2.846 / [input L175](https://github.com/ros-industrial/universal_robot/blob/39ad110d8f2e8f66856a201cca88aa7a7025e3eb/ur_description/urdf/inc/ur_macro.xacro#L175) |
| wrist_1_link | 1.219 / [input L93](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/universal_robots_ur5e/ur5e.xml#L93) | unavailable | 1.37 / [input L205](https://github.com/ros-industrial/universal_robot/blob/39ad110d8f2e8f66856a201cca88aa7a7025e3eb/ur_description/urdf/inc/ur_macro.xacro#L205) |
| wrist_2_link | 1.219 / [input L100](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/universal_robots_ur5e/ur5e.xml#L100) | unavailable | 1.3 / [input L234](https://github.com/ros-industrial/universal_robot/blob/39ad110d8f2e8f66856a201cca88aa7a7025e3eb/ur_description/urdf/inc/ur_macro.xacro#L234) |
| wrist_3_link | 0.1889 / [input L109](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/universal_robots_ur5e/ur5e.xml#L109) | unavailable | 0.365 / [input L267](https://github.com/ros-industrial/universal_robot/blob/39ad110d8f2e8f66856a201cca88aa7a7025e3eb/ur_description/urdf/inc/ur_macro.xacro#L267) |
| upstream-only base_link | unavailable | unavailable | 0 / [geometry/inference input L79](https://github.com/ros-industrial/universal_robot/blob/39ad110d8f2e8f66856a201cca88aa7a7025e3eb/ur_description/urdf/inc/ur_macro.xacro#L79) |
| upstream-only base_link_inertia | unavailable | unavailable | 4 / [geometry/inference input L80](https://github.com/ros-industrial/universal_robot/blob/39ad110d8f2e8f66856a201cca88aa7a7025e3eb/ur_description/urdf/inc/ur_macro.xacro#L80) |
| upstream-only flange | unavailable | unavailable | 0 / [geometry/inference input L378](https://github.com/ros-industrial/universal_robot/blob/39ad110d8f2e8f66856a201cca88aa7a7025e3eb/ur_description/urdf/inc/ur_macro.xacro#L378) |
| upstream-only tool0 | unavailable | unavailable | 0 / [geometry/inference input L386](https://github.com/ros-industrial/universal_robot/blob/39ad110d8f2e8f66856a201cca88aa7a7025e3eb/ur_description/urdf/inc/ur_macro.xacro#L386) |

## Coverage and unmatched elements

```json
{
  "mapping_h": {
    "bodies": {
      "base": "base",
      "shoulder_link": "shoulder_link",
      "upper_arm_link": "upper_arm_link",
      "forearm_link": "forearm_link",
      "wrist_1_link": "wrist_1_link",
      "wrist_2_link": "wrist_2_link",
      "wrist_3_link": "wrist_3_link"
    },
    "joints": {
      "shoulder_pan_joint": "shoulder_pan_joint",
      "shoulder_lift_joint": "shoulder_lift_joint",
      "elbow_joint": "elbow_joint",
      "wrist_1_joint": "wrist_1_joint",
      "wrist_2_joint": "wrist_2_joint",
      "wrist_3_joint": "wrist_3_joint"
    },
    "body_methods": {
      "base": "name",
      "shoulder_link": "name",
      "upper_arm_link": "name",
      "forearm_link": "name",
      "wrist_1_link": "name",
      "wrist_2_link": "name",
      "wrist_3_link": "name"
    },
    "joint_methods": {
      "shoulder_pan_joint": "name",
      "shoulder_lift_joint": "name",
      "elbow_joint": "name",
      "wrist_1_joint": "name",
      "wrist_2_joint": "name",
      "wrist_3_joint": "name"
    },
    "unmatched_m_bodies": [],
    "unmatched_upstream_bodies": [
      "base_link",
      "base_link_inertia",
      "flange",
      "tool0"
    ],
    "unmatched_m_joints": [],
    "unmatched_upstream_joints": [],
    "registration_anchor": {
      "M": "base",
      "H": "base",
      "root_unmatched": false
    }
  },
  "mapping_s": null,
  "unavailable": [
    {
      "entity": "shoulder_pan_joint",
      "other_entity": "shoulder_pan_joint",
      "quantity": "force",
      "tolerance": "limit",
      "m": 150.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "shoulder_pan_joint",
      "other_entity": "shoulder_pan_joint",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 3.141592653589793,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "shoulder_lift_joint",
      "other_entity": "shoulder_lift_joint",
      "quantity": "force",
      "tolerance": "limit",
      "m": 150.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "shoulder_lift_joint",
      "other_entity": "shoulder_lift_joint",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 3.141592653589793,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "elbow_joint",
      "other_entity": "elbow_joint",
      "quantity": "force",
      "tolerance": "limit",
      "m": 150.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "elbow_joint",
      "other_entity": "elbow_joint",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 3.141592653589793,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "wrist_1_joint",
      "other_entity": "wrist_1_joint",
      "quantity": "force",
      "tolerance": "limit",
      "m": 28.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "wrist_1_joint",
      "other_entity": "wrist_1_joint",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 3.141592653589793,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "wrist_2_joint",
      "other_entity": "wrist_2_joint",
      "quantity": "force",
      "tolerance": "limit",
      "m": 28.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "wrist_2_joint",
      "other_entity": "wrist_2_joint",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 3.141592653589793,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "wrist_3_joint",
      "other_entity": "wrist_3_joint",
      "quantity": "force",
      "tolerance": "limit",
      "m": 28.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "wrist_3_joint",
      "other_entity": "wrist_3_joint",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 3.141592653589793,
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
| shoulder_pan_joint / force | 150 | unavailable | unavailable |
| shoulder_pan_joint / velocity | unavailable | unavailable | 3.14159265 |
| shoulder_lift_joint / force | 150 | unavailable | unavailable |
| shoulder_lift_joint / velocity | unavailable | unavailable | 3.14159265 |
| elbow_joint / force | 150 | unavailable | unavailable |
| elbow_joint / velocity | unavailable | unavailable | 3.14159265 |
| wrist_1_joint / force | 28 | unavailable | unavailable |
| wrist_1_joint / velocity | unavailable | unavailable | 3.14159265 |
| wrist_2_joint / force | 28 | unavailable | unavailable |
| wrist_2_joint / velocity | unavailable | unavailable | 3.14159265 |
| wrist_3_joint / force | 28 | unavailable | unavailable |
| wrist_3_joint / velocity | unavailable | unavailable | 3.14159265 |
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
  "ur_description/config/ur5e/default_kinematics.yaml",
  "ur_description/config/ur5e/joint_limits.yaml",
  "ur_description/config/ur5e/physical_parameters.yaml",
  "ur_description/config/ur5e/visual_parameters.yaml",
  "ur_description/meshes/ur5e/collision/base.stl",
  "ur_description/meshes/ur5e/collision/forearm.stl",
  "ur_description/meshes/ur5e/collision/shoulder.stl",
  "ur_description/meshes/ur5e/collision/upperarm.stl",
  "ur_description/meshes/ur5e/collision/wrist1.stl",
  "ur_description/meshes/ur5e/collision/wrist2.stl",
  "ur_description/meshes/ur5e/collision/wrist3.stl",
  "ur_description/meshes/ur5e/visual/base.dae",
  "ur_description/meshes/ur5e/visual/forearm.dae",
  "ur_description/meshes/ur5e/visual/shoulder.dae",
  "ur_description/meshes/ur5e/visual/upperarm.dae",
  "ur_description/meshes/ur5e/visual/wrist1.dae",
  "ur_description/meshes/ur5e/visual/wrist2.dae",
  "ur_description/meshes/ur5e/visual/wrist3.dae",
  "ur_description/urdf/inc/ur5e_macro.xacro",
  "ur_description/urdf/inc/ur_common.xacro",
  "ur_description/urdf/inc/ur_macro.xacro",
  "ur_description/urdf/inc/ur_transmissions.xacro",
  "ur_description/urdf/ur5e.xacro"
]
```

## Self comparisons

```json
[
  {
    "file": "universal_robots_ur5e/ur5e.xml",
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
      "unknown": 22
    },
    "classifications_changed": 0,
    "finding_membership_changes": 0
  },
  "2": {
    "provenance_method": "unknown",
    "counts": {
      "unknown": 22
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
      "universal_robots_ur5e/ur5e.xml"
    ],
    "registration": {
      "translation": [
        0.0,
        0.0,
        0.0
      ],
      "rotation": [
        [
          -1.0,
          0.0,
          0.0
        ],
        [
          0.0,
          -1.0,
          -0.0
        ],
        [
          -0.0,
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
      "base_link",
      "base",
      "flange",
      "tool0"
    ],
    "assets_loaded": 14,
    "mesh_conversions": [
      {
        "file": "ur_description/meshes/ur5e/visual/base.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "ur_description/meshes/ur5e/visual/shoulder.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "ur_description/meshes/ur5e/visual/upperarm.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "ur_description/meshes/ur5e/visual/forearm.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "ur_description/meshes/ur5e/visual/wrist1.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "ur_description/meshes/ur5e/visual/wrist2.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "ur_description/meshes/ur5e/visual/wrist3.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      }
    ],
    "nonphysical_normalizations": [],
    "xacro_arguments": {},
    "source_dependencies": [
      "ur_description/config/ur5e/default_kinematics.yaml",
      "ur_description/config/ur5e/joint_limits.yaml",
      "ur_description/config/ur5e/physical_parameters.yaml",
      "ur_description/config/ur5e/visual_parameters.yaml",
      "ur_description/urdf/inc/ur5e_macro.xacro",
      "ur_description/urdf/inc/ur_common.xacro",
      "ur_description/urdf/inc/ur_macro.xacro",
      "ur_description/urdf/inc/ur_transmissions.xacro",
      "ur_description/urdf/ur5e.xacro",
      "ur_description/meshes/ur5e/visual/base.dae",
      "ur_description/meshes/ur5e/collision/base.stl",
      "ur_description/meshes/ur5e/visual/shoulder.dae",
      "ur_description/meshes/ur5e/collision/shoulder.stl",
      "ur_description/meshes/ur5e/visual/upperarm.dae",
      "ur_description/meshes/ur5e/collision/upperarm.stl",
      "ur_description/meshes/ur5e/visual/forearm.dae",
      "ur_description/meshes/ur5e/collision/forearm.stl",
      "ur_description/meshes/ur5e/visual/wrist1.dae",
      "ur_description/meshes/ur5e/collision/wrist1.stl",
      "ur_description/meshes/ur5e/visual/wrist2.dae",
      "ur_description/meshes/ur5e/collision/wrist2.stl",
      "ur_description/meshes/ur5e/visual/wrist3.dae",
      "ur_description/meshes/ur5e/collision/wrist3.stl"
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
  "historical_snapshots_reused": 10,
  "primary_physics_unchanged": true,
  "source_matching": "original raw-value provenance criteria retained; kinematic guard applies to reported CoM"
}
```
