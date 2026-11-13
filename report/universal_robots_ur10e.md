# universal_robots_ur10e

Status: **partial history**. Provenance: **unknown**, confidence **incomplete**.

Unresolved historical compilation prevents selecting or rejecting a matching source. Pairwise M/H differences are reported with unknown provenance.

M: `https://github.com/google-deepmind/mujoco_menagerie`, `universal_robots_ur10e/ur10e.xml`, commit `370c43965323c0944b433b202aac5058b5f907a9`.
H: `https://github.com/ros-industrial/universal_robot`, `ur_description/urdf/ur10e.xacro`, commit `39ad110d8f2e8f66856a201cca88aa7a7025e3eb`.
S: unavailable. A machine-readable H can still be compared to M; no-match differences are never counted as STALE.

Limit semantics: MJCF effort values are supported actuator torque/force envelopes. URDF effort and velocity values are manufacturer declarations retained from XML; MuJoCo does not enforce those tags. Such declaration comparisons are explicitly distinct from compiled inertial/range quantities.


## Source evidence

```json
[
  {
    "url": "https://github.com/kevinzakka/obj2mjcf",
    "document": "universal_robots_ur10e/README.md",
    "commit": "370c43965323c0944b433b202aac5058b5f907a9",
    "current": true
  },
  {
    "url": "https://github.com/ros-industrial/universal_robot/tree/kinetic-devel/ur_e_description",
    "document": "universal_robots_ur10e/README.md",
    "commit": "370c43965323c0944b433b202aac5058b5f907a9",
    "current": true
  },
  {
    "url": "https://github.com/ros-industrial/universal_robot/tree/kinetic-devel/ur_e_description/meshes/ur10e/visual",
    "document": "universal_robots_ur10e/README.md",
    "commit": "370c43965323c0944b433b202aac5058b5f907a9",
    "current": true
  }
]
```


## Kinematics consistency

A proper Kabsch rigid transform aligns all matched zero-pose body origins. The maximum per-origin residual and signed hinge/slide axis angles determine whether CoM can be compared; RMS is also recorded. Fewer than three non-collinear origins give insufficient kinematic coverage. CoM records that fail either required M/H or M/S check are excluded from counts and largest discrepancies. Masses, principal moments and raw joint ranges remain unchanged; a flagged range still requires convention review.

| Pair | Status | Origins / rank | RMS / maximum mm | Disagreeing / checked axes |
|---|---|---:|---:|---:|
| M/H | kinematic convention differs | 7 / 3 | 77.4531163 / 115.910012 | 6 / 6 |

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
        -0.99134597182044,
        -0.12289971072255901,
        -0.04613919439802058
      ],
      [
        0.10787908918813191,
        -0.9629602812560761,
        0.24712263926876168
      ],
      [
        -0.07480151249357275,
        0.24000657871718986,
        0.9678851047005235
      ]
    ],
    "translation_other_to_m": [
      -0.0005672062565716951,
      0.03247689480009641,
      -0.0013709610332010291
    ],
    "rms_residual_m": 0.07745311633091659,
    "max_residual_m": 0.11591001197960527,
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
          -0.04613919439802058,
          0.24712263926876168,
          0.9678851047005235
        ],
        "angle_rad": 0.25411917356529606,
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
          0.12289971073202229,
          0.9629602812053902,
          -0.24000657891570643
        ],
        "angle_rad": 0.27302256807675346,
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
          0.12289971073202229,
          0.9629602812053902,
          -0.24000657891570643
        ],
        "angle_rad": 0.27302256807675346,
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
          0.12289971073202229,
          0.9629602812053902,
          -0.24000657891570643
        ],
        "angle_rad": 0.27302256807675346,
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
          0.04613919434760626,
          -0.24712263966377476,
          -0.9678851046020711
        ],
        "angle_rad": 0.25411917395692346,
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
          0.12289971073202216,
          0.9629602812053902,
          -0.24000657891570643
        ],
        "angle_rad": 0.2730225680767534,
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
          -0.04613919439802058,
          0.24712263926876168,
          0.9678851047005235
        ],
        "angle_rad": 0.25411917356529606,
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
          0.12289971073202229,
          0.9629602812053902,
          -0.24000657891570643
        ],
        "angle_rad": 0.27302256807675346,
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
          0.12289971073202229,
          0.9629602812053902,
          -0.24000657891570643
        ],
        "angle_rad": 0.27302256807675346,
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
          0.12289971073202229,
          0.9629602812053902,
          -0.24000657891570643
        ],
        "angle_rad": 0.27302256807675346,
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
          0.04613919434760626,
          -0.24712263966377476,
          -0.9678851046020711
        ],
        "angle_rad": 0.25411917395692346,
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
          0.12289971073202216,
          0.9629602812053902,
          -0.24000657891570643
        ],
        "angle_rad": 0.2730225680767534,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      }
    ],
    "com_eligible": false,
    "covariance_singular_values": [
      2.141370215428064,
      0.03355086743253802,
      0.007670880969135473
    ],
    "origin_residuals_m": {
      "base": 0.03251076672348069,
      "shoulder_link": 0.07800315549243804,
      "upper_arm_link": 0.09954920318495253,
      "forearm_link": 0.04963631372751381,
      "wrist_1_link": 0.08745014261434535,
      "wrist_2_link": 0.11591001197960527,
      "wrist_3_link": 0.03734954578399488
    },
    "reason": "Origin residual exceeds threshold and/or matched signed joint axes disagree"
  }
}
```


## Every reported quantity difference

Counts are quantity records, including correlated total/subtree/body mass records; they are not independent robot defects.

| Entity / quantity | M | S | H | H − M | Class | M source | S source | H source |
|---|---|---|---|---|---|---|---|---|
| robot / total_mass | 32.7 | unavailable | 33.104 | 0.404 | unknown | [aggregate inputs](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/universal_robots_ur10e/ur10e.xml#L1) | unavailable | [aggregate inputs](https://github.com/ros-industrial/universal_robot/blob/39ad110d8f2e8f66856a201cca88aa7a7025e3eb/ur_description/urdf/ur10e.xacro#L1) |
| base / mass | 4 | unavailable | 0 | -4 | unknown | [input L71](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/universal_robots_ur10e/ur10e.xml#L71) | unavailable | [geometry/inference input L365](https://github.com/ros-industrial/universal_robot/blob/39ad110d8f2e8f66856a201cca88aa7a7025e3eb/ur_description/urdf/inc/ur_macro.xacro#L365) |
| base / subtree_mass | 32.7 | unavailable | 0 | -32.7 | unknown | [subtree root L70](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/universal_robots_ur10e/ur10e.xml#L70) | unavailable | [subtree root L365](https://github.com/ros-industrial/universal_robot/blob/39ad110d8f2e8f66856a201cca88aa7a7025e3eb/ur_description/urdf/inc/ur_macro.xacro#L365) |
| base / principal_moments | [0.00610633089, 0.00610633089, 0.01125] | unavailable | [0, 0, 0] | [-0.00610633089, -0.00610633089, -0.01125] | unknown | [inertia input L71](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/universal_robots_ur10e/ur10e.xml#L71) | unavailable | [geometry/inference input L365](https://github.com/ros-industrial/universal_robot/blob/39ad110d8f2e8f66856a201cca88aa7a7025e3eb/ur_description/urdf/inc/ur_macro.xacro#L365) |
| shoulder_link / mass | 7.778 | unavailable | 7.369 | -0.409 | unknown | [input L75](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/universal_robots_ur10e/ur10e.xml#L75) | unavailable | [input L117](https://github.com/ros-industrial/universal_robot/blob/39ad110d8f2e8f66856a201cca88aa7a7025e3eb/ur_description/urdf/inc/ur_macro.xacro#L117) |
| shoulder_link / subtree_mass | 28.7 | unavailable | 29.104 | 0.404 | unknown | [subtree root L74](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/universal_robots_ur10e/ur10e.xml#L74) | unavailable | [subtree root L100](https://github.com/ros-industrial/universal_robot/blob/39ad110d8f2e8f66856a201cca88aa7a7025e3eb/ur_description/urdf/inc/ur_macro.xacro#L100) |
| shoulder_link / principal_moments | [0.0218756, 0.0314743, 0.0314743] | unavailable | [0.0202531695, 0.0352902506, 0.0353865799] | [-0.00162243053, 0.00381595064, 0.00391227988] | unknown | [inertia input L75](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/universal_robots_ur10e/ur10e.xml#L75) | unavailable | [inertia input L126](https://github.com/ros-industrial/universal_robot/blob/39ad110d8f2e8f66856a201cca88aa7a7025e3eb/ur_description/urdf/inc/ur_macro.xacro#L126) |
| upper_arm_link / mass | 12.93 | unavailable | 13.051 | 0.121 | unknown | [input L82](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/universal_robots_ur10e/ur10e.xml#L82) | unavailable | [input L146](https://github.com/ros-industrial/universal_robot/blob/39ad110d8f2e8f66856a201cca88aa7a7025e3eb/ur_description/urdf/inc/ur_macro.xacro#L146) |
| upper_arm_link / subtree_mass | 20.922 | unavailable | 21.735 | 0.813 | unknown | [subtree root L81](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/universal_robots_ur10e/ur10e.xml#L81) | unavailable | [subtree root L129](https://github.com/ros-industrial/universal_robot/blob/39ad110d8f2e8f66856a201cca88aa7a7025e3eb/ur_description/urdf/inc/ur_macro.xacro#L129) |
| upper_arm_link / principal_moments | [0.0363656, 0.423074, 0.423074] | unavailable | [0.0278114286, 0.769758179, 0.770680393] | [-0.00855417138, 0.346684179, 0.347606393] | unknown | [inertia input L82](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/universal_robots_ur10e/ur10e.xml#L82) | unavailable | [inertia input L155](https://github.com/ros-industrial/universal_robot/blob/39ad110d8f2e8f66856a201cca88aa7a7025e3eb/ur_description/urdf/inc/ur_macro.xacro#L155) |
| forearm_link / mass | 3.87 | unavailable | 3.989 | 0.119 | unknown | [input L91](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/universal_robots_ur10e/ur10e.xml#L91) | unavailable | [input L175](https://github.com/ros-industrial/universal_robot/blob/39ad110d8f2e8f66856a201cca88aa7a7025e3eb/ur_description/urdf/inc/ur_macro.xacro#L175) |
| forearm_link / subtree_mass | 7.992 | unavailable | 8.684 | 0.692 | unknown | [subtree root L90](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/universal_robots_ur10e/ur10e.xml#L90) | unavailable | [subtree root L158](https://github.com/ros-industrial/universal_robot/blob/39ad110d8f2e8f66856a201cca88aa7a7025e3eb/ur_description/urdf/inc/ur_macro.xacro#L158) |
| forearm_link / principal_moments | [0.0108844, 0.11059, 0.11059] | unavailable | [0.00985708996, 0.306742886, 0.309280024] | [-0.00102731004, 0.196152886, 0.198690024] | unknown | [inertia input L91](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/universal_robots_ur10e/ur10e.xml#L91) | unavailable | [inertia input L184](https://github.com/ros-industrial/universal_robot/blob/39ad110d8f2e8f66856a201cca88aa7a7025e3eb/ur_description/urdf/inc/ur_macro.xacro#L184) |
| wrist_1_link / mass | 1.96 | unavailable | 2.1 | 0.14 | unknown | [input L101](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/universal_robots_ur10e/ur10e.xml#L101) | unavailable | [input L205](https://github.com/ros-industrial/universal_robot/blob/39ad110d8f2e8f66856a201cca88aa7a7025e3eb/ur_description/urdf/inc/ur_macro.xacro#L205) |
| wrist_1_link / subtree_mass | 4.122 | unavailable | 4.695 | 0.573 | unknown | [subtree root L99](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/universal_robots_ur10e/ur10e.xml#L99) | unavailable | [subtree root L187](https://github.com/ros-industrial/universal_robot/blob/39ad110d8f2e8f66856a201cca88aa7a7025e3eb/ur_description/urdf/inc/ur_macro.xacro#L187) |
| wrist_1_link / principal_moments | [0.00510825, 0.00510825, 0.0055125] | unavailable | [0.00209990698, 0.00269992314, 0.00296016988] | [-0.00300834302, -0.00240832686, -0.00255233012] | unknown | [inertia input L101](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/universal_robots_ur10e/ur10e.xml#L101) | unavailable | [inertia input L214](https://github.com/ros-industrial/universal_robot/blob/39ad110d8f2e8f66856a201cca88aa7a7025e3eb/ur_description/urdf/inc/ur_macro.xacro#L214) |
| wrist_2_link / mass | 1.96 | unavailable | 1.98 | 0.02 | unknown | [input L109](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/universal_robots_ur10e/ur10e.xml#L109) | unavailable | [input L234](https://github.com/ros-industrial/universal_robot/blob/39ad110d8f2e8f66856a201cca88aa7a7025e3eb/ur_description/urdf/inc/ur_macro.xacro#L234) |
| wrist_2_link / subtree_mass | 2.162 | unavailable | 2.595 | 0.433 | unknown | [subtree root L107](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/universal_robots_ur10e/ur10e.xml#L107) | unavailable | [subtree root L217](https://github.com/ros-industrial/universal_robot/blob/39ad110d8f2e8f66856a201cca88aa7a7025e3eb/ur_description/urdf/inc/ur_macro.xacro#L217) |
| wrist_2_link / principal_moments | [0.00510825, 0.00510825, 0.0055125] | unavailable | [0.00209990698, 0.00269992314, 0.00296016988] | [-0.00300834302, -0.00240832686, -0.00255233012] | unknown | [inertia input L109](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/universal_robots_ur10e/ur10e.xml#L109) | unavailable | [inertia input L243](https://github.com/ros-industrial/universal_robot/blob/39ad110d8f2e8f66856a201cca88aa7a7025e3eb/ur_description/urdf/inc/ur_macro.xacro#L243) |
| wrist_3_link / mass | 0.202 | unavailable | 0.615 | 0.413 | unknown | [input L118](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/universal_robots_ur10e/ur10e.xml#L118) | unavailable | [input L267](https://github.com/ros-industrial/universal_robot/blob/39ad110d8f2e8f66856a201cca88aa7a7025e3eb/ur_description/urdf/inc/ur_macro.xacro#L267) |
| wrist_3_link / subtree_mass | 0.202 | unavailable | 0.615 | 0.413 | unknown | [subtree root L116](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/universal_robots_ur10e/ur10e.xml#L116) | unavailable | [subtree root L246](https://github.com/ros-industrial/universal_robot/blob/39ad110d8f2e8f66856a201cca88aa7a7025e3eb/ur_description/urdf/inc/ur_macro.xacro#L246) |
| wrist_3_link / principal_moments | [0.000144346, 0.000144346, 0.000204525] | unavailable | [0.00034, 0.0004, 0.00041] | [0.000195654, 0.000255654, 0.000205475] | unknown | [inertia input L118](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/universal_robots_ur10e/ur10e.xml#L118) | unavailable | [inertia input L276](https://github.com/ros-industrial/universal_robot/blob/39ad110d8f2e8f66856a201cca88aa7a7025e3eb/ur_description/urdf/inc/ur_macro.xacro#L276) |
| wrist_1_joint / effort | 56 | unavailable | 54 | -2 | unknown | [inherited actuator input L26](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/universal_robots_ur10e/ur10e.xml#L26) | unavailable | [input L333](https://github.com/ros-industrial/universal_robot/blob/39ad110d8f2e8f66856a201cca88aa7a7025e3eb/ur_description/urdf/inc/ur_macro.xacro#L333) |
| wrist_2_joint / effort | 56 | unavailable | 54 | -2 | unknown | [inherited actuator input L26](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/universal_robots_ur10e/ur10e.xml#L26) | unavailable | [input L345](https://github.com/ros-industrial/universal_robot/blob/39ad110d8f2e8f66856a201cca88aa7a7025e3eb/ur_description/urdf/inc/ur_macro.xacro#L345) |
| wrist_3_joint / effort | 56 | unavailable | 54 | -2 | unknown | [inherited actuator input L26](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/universal_robots_ur10e/ur10e.xml#L26) | unavailable | [input L357](https://github.com/ros-industrial/universal_robot/blob/39ad110d8f2e8f66856a201cca88aa7a7025e3eb/ur_description/urdf/inc/ur_macro.xacro#L357) |

## Raw CoM records and reporting decisions

Raw values retain the previous root-anchor registration before Kabsch; original world coordinates also remain in the snapshots. Eligible findings above use the fitted transform into M. Excluded raw records below are diagnostic numbers, not findings. No CoM suppression applies to mass or principal inertia moments.

| Entity / quantity | Raw M | Raw S | Raw H | Raw H − M | Decision | M source | S source | H source |
|---|---|---|---|---|---|---|---|---|
| robot / total_com_registered | [0.37677945, 0.0967101529, 0.150925382] | unavailable | [-0.368803942, -0.104396312, 0.148747645] | [-0.745583392, -0.201106465, -0.00217773698] | M/H: kinematic convention differs | [aggregate inputs](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/universal_robots_ur10e/ur10e.xml#L1) | unavailable | [aggregate inputs](https://github.com/ros-industrial/universal_robot/blob/39ad110d8f2e8f66856a201cca88aa7a7025e3eb/ur_description/urdf/ur10e.xacro#L1) |
| base / com_registered | [0, 0, 0] | unavailable | [0, 0, 0] | [0, 0, 0] | M/H: kinematic convention differs | [CoM/kinematic input L71](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/universal_robots_ur10e/ur10e.xml#L71) | unavailable | [geometry/inference input L365](https://github.com/ros-industrial/universal_robot/blob/39ad110d8f2e8f66856a201cca88aa7a7025e3eb/ur_description/urdf/inc/ur_macro.xacro#L365) |
| shoulder_link / com_registered | [0, 0, 0.181] | unavailable | [0.021, -0.027, 0.1807] | [0.021, -0.027, -0.0003] | M/H: kinematic convention differs | [CoM/kinematic input L75](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/universal_robots_ur10e/ur10e.xml#L75) | unavailable | [CoM/kinematic input L118](https://github.com/ros-industrial/universal_robot/blob/39ad110d8f2e8f66856a201cca88aa7a7025e3eb/ur_description/urdf/inc/ur_macro.xacro#L118) |
| upper_arm_link / com_registered | [0.3065, 0.176, 0.181] | unavailable | [-0.2327, -0.158, 0.1807] | [-0.5392, -0.334, -0.000300000032] | M/H: kinematic convention differs | [CoM/kinematic input L82](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/universal_robots_ur10e/ur10e.xml#L82) | unavailable | [CoM/kinematic input L147](https://github.com/ros-industrial/universal_robot/blob/39ad110d8f2e8f66856a201cca88aa7a7025e3eb/ur_description/urdf/inc/ur_macro.xacro#L147) |
| forearm_link / com_registered | [0.8985, 0.039, 0.181] | unavailable | [-0.94425, -0.068, 0.1807] | [-1.84275, -0.107, -0.000300000014] | M/H: kinematic convention differs | [CoM/kinematic input L91](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/universal_robots_ur10e/ur10e.xml#L91) | unavailable | [CoM/kinematic input L176](https://github.com/ros-industrial/universal_robot/blob/39ad110d8f2e8f66856a201cca88aa7a7025e3eb/ur_description/urdf/inc/ur_macro.xacro#L176) |
| wrist_1_link / com_registered | [1.184, 0.174, 0.181] | unavailable | [-1.18425, -0.18115, 0.1627] | [-2.36825, -0.35515, -0.0183] | M/H: kinematic convention differs | [CoM/kinematic input L101](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/universal_robots_ur10e/ur10e.xml#L101) | unavailable | [CoM/kinematic input L206](https://github.com/ros-industrial/universal_robot/blob/39ad110d8f2e8f66856a201cca88aa7a7025e3eb/ur_description/urdf/inc/ur_macro.xacro#L206) |
| wrist_2_link / com_registered | [1.184, 0.174, 0.061] | unavailable | [-1.18425, -0.19215, 0.06785] | [-2.36825, -0.36615, 0.00684999996] | M/H: kinematic convention differs | [CoM/kinematic input L109](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/universal_robots_ur10e/ur10e.xml#L109) | unavailable | [CoM/kinematic input L235](https://github.com/ros-industrial/universal_robot/blob/39ad110d8f2e8f66856a201cca88aa7a7025e3eb/ur_description/urdf/inc/ur_macro.xacro#L235) |
| wrist_3_link / com_registered | [1.184, 0.266, 0.061] | unavailable | [-1.18425, -0.2647, 0.0608499999] | [-2.36825, -0.5307, -0.000150000054] | M/H: kinematic convention differs | [CoM/kinematic input L118](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/universal_robots_ur10e/ur10e.xml#L118) | unavailable | [CoM/kinematic input L268](https://github.com/ros-industrial/universal_robot/blob/39ad110d8f2e8f66856a201cca88aa7a7025e3eb/ur_description/urdf/inc/ur_macro.xacro#L268) |

## Mass accounting

Every contributing compiled body mass is listed here so total/subtree sums can be checked. Links point to explicit inertials or to geometry inputs when the compiler inferred a mass. CoM links identify inertial inputs; world coordinates additionally use the ancestor transforms and the registration recorded below.

| M body | M kg / source | S kg / source | H kg / source |
|---|---|---|---|
| base | 4 / [input L71](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/universal_robots_ur10e/ur10e.xml#L71) | unavailable | 0 / [geometry/inference input L365](https://github.com/ros-industrial/universal_robot/blob/39ad110d8f2e8f66856a201cca88aa7a7025e3eb/ur_description/urdf/inc/ur_macro.xacro#L365) |
| shoulder_link | 7.778 / [input L75](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/universal_robots_ur10e/ur10e.xml#L75) | unavailable | 7.369 / [input L117](https://github.com/ros-industrial/universal_robot/blob/39ad110d8f2e8f66856a201cca88aa7a7025e3eb/ur_description/urdf/inc/ur_macro.xacro#L117) |
| upper_arm_link | 12.93 / [input L82](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/universal_robots_ur10e/ur10e.xml#L82) | unavailable | 13.051 / [input L146](https://github.com/ros-industrial/universal_robot/blob/39ad110d8f2e8f66856a201cca88aa7a7025e3eb/ur_description/urdf/inc/ur_macro.xacro#L146) |
| forearm_link | 3.87 / [input L91](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/universal_robots_ur10e/ur10e.xml#L91) | unavailable | 3.989 / [input L175](https://github.com/ros-industrial/universal_robot/blob/39ad110d8f2e8f66856a201cca88aa7a7025e3eb/ur_description/urdf/inc/ur_macro.xacro#L175) |
| wrist_1_link | 1.96 / [input L101](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/universal_robots_ur10e/ur10e.xml#L101) | unavailable | 2.1 / [input L205](https://github.com/ros-industrial/universal_robot/blob/39ad110d8f2e8f66856a201cca88aa7a7025e3eb/ur_description/urdf/inc/ur_macro.xacro#L205) |
| wrist_2_link | 1.96 / [input L109](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/universal_robots_ur10e/ur10e.xml#L109) | unavailable | 1.98 / [input L234](https://github.com/ros-industrial/universal_robot/blob/39ad110d8f2e8f66856a201cca88aa7a7025e3eb/ur_description/urdf/inc/ur_macro.xacro#L234) |
| wrist_3_link | 0.202 / [input L118](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/universal_robots_ur10e/ur10e.xml#L118) | unavailable | 0.615 / [input L267](https://github.com/ros-industrial/universal_robot/blob/39ad110d8f2e8f66856a201cca88aa7a7025e3eb/ur_description/urdf/inc/ur_macro.xacro#L267) |
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
      "m": 330.0,
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
      "other": 2.0943951023931953,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "shoulder_lift_joint",
      "other_entity": "shoulder_lift_joint",
      "quantity": "force",
      "tolerance": "limit",
      "m": 330.0,
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
      "other": 2.0943951023931953,
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
      "m": 56.0,
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
      "m": 56.0,
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
      "m": 56.0,
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
| shoulder_pan_joint / force | 330 | unavailable | unavailable |
| shoulder_pan_joint / velocity | unavailable | unavailable | 2.0943951 |
| shoulder_lift_joint / force | 330 | unavailable | unavailable |
| shoulder_lift_joint / velocity | unavailable | unavailable | 2.0943951 |
| elbow_joint / force | 150 | unavailable | unavailable |
| elbow_joint / velocity | unavailable | unavailable | 3.14159265 |
| wrist_1_joint / force | 56 | unavailable | unavailable |
| wrist_1_joint / velocity | unavailable | unavailable | 3.14159265 |
| wrist_2_joint / force | 56 | unavailable | unavailable |
| wrist_2_joint / velocity | unavailable | unavailable | 3.14159265 |
| wrist_3_joint / force | 56 | unavailable | unavailable |
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
  "ur_description/config/ur10e/default_kinematics.yaml",
  "ur_description/config/ur10e/joint_limits.yaml",
  "ur_description/config/ur10e/physical_parameters.yaml",
  "ur_description/config/ur10e/visual_parameters.yaml",
  "ur_description/meshes/ur10e/collision/base.stl",
  "ur_description/meshes/ur10e/collision/forearm.stl",
  "ur_description/meshes/ur10e/collision/shoulder.stl",
  "ur_description/meshes/ur10e/collision/upperarm.stl",
  "ur_description/meshes/ur10e/collision/wrist1.stl",
  "ur_description/meshes/ur10e/collision/wrist2.stl",
  "ur_description/meshes/ur10e/collision/wrist3.stl",
  "ur_description/meshes/ur10e/visual/base.dae",
  "ur_description/meshes/ur10e/visual/forearm.dae",
  "ur_description/meshes/ur10e/visual/shoulder.dae",
  "ur_description/meshes/ur10e/visual/upperarm.dae",
  "ur_description/meshes/ur10e/visual/wrist1.dae",
  "ur_description/meshes/ur10e/visual/wrist2.dae",
  "ur_description/meshes/ur10e/visual/wrist3.dae",
  "ur_description/urdf/inc/ur10e_macro.xacro",
  "ur_description/urdf/inc/ur_common.xacro",
  "ur_description/urdf/inc/ur_macro.xacro",
  "ur_description/urdf/inc/ur_transmissions.xacro",
  "ur_description/urdf/ur10e.xacro"
]
```

## Self comparisons

```json
[
  {
    "file": "universal_robots_ur10e/ur10e.xml",
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
      "unknown": 25
    },
    "classifications_changed": 0,
    "finding_membership_changes": 0
  },
  "2": {
    "provenance_method": "unknown",
    "counts": {
      "unknown": 24
    },
    "classifications_changed": 0,
    "finding_membership_changes": 1
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
      "universal_robots_ur10e/ur10e.xml"
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
        "file": "ur_description/meshes/ur10e/visual/base.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "ur_description/meshes/ur10e/visual/shoulder.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "ur_description/meshes/ur10e/visual/upperarm.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "ur_description/meshes/ur10e/visual/forearm.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "ur_description/meshes/ur10e/visual/wrist1.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "ur_description/meshes/ur10e/visual/wrist2.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      },
      {
        "file": "ur_description/meshes/ur10e/visual/wrist3.dae",
        "conversion": "COLLADA to OBJ with scene transforms, no textures"
      }
    ],
    "nonphysical_normalizations": [],
    "xacro_arguments": {},
    "source_dependencies": [
      "ur_description/config/ur10e/default_kinematics.yaml",
      "ur_description/config/ur10e/joint_limits.yaml",
      "ur_description/config/ur10e/physical_parameters.yaml",
      "ur_description/config/ur10e/visual_parameters.yaml",
      "ur_description/urdf/inc/ur10e_macro.xacro",
      "ur_description/urdf/inc/ur_common.xacro",
      "ur_description/urdf/inc/ur_macro.xacro",
      "ur_description/urdf/inc/ur_transmissions.xacro",
      "ur_description/urdf/ur10e.xacro",
      "ur_description/meshes/ur10e/visual/base.dae",
      "ur_description/meshes/ur10e/collision/base.stl",
      "ur_description/meshes/ur10e/visual/shoulder.dae",
      "ur_description/meshes/ur10e/collision/shoulder.stl",
      "ur_description/meshes/ur10e/visual/upperarm.dae",
      "ur_description/meshes/ur10e/collision/upperarm.stl",
      "ur_description/meshes/ur10e/visual/forearm.dae",
      "ur_description/meshes/ur10e/collision/forearm.stl",
      "ur_description/meshes/ur10e/visual/wrist1.dae",
      "ur_description/meshes/ur10e/collision/wrist1.stl",
      "ur_description/meshes/ur10e/visual/wrist2.dae",
      "ur_description/meshes/ur10e/collision/wrist2.stl",
      "ur_description/meshes/ur10e/visual/wrist3.dae",
      "ur_description/meshes/ur10e/collision/wrist3.stl"
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
  "historical_snapshots_reused": 9,
  "primary_physics_unchanged": true,
  "source_matching": "original raw-value provenance criteria retained; kinematic guard applies to reported CoM"
}
```
