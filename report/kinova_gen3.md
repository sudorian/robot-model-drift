# kinova_gen3

Status: **complete**. Provenance: **none**, confidence **none**.

No public revision matches all comparable quantities. Class: NO MATCHING SOURCE; never counted as STALE.

M: `https://github.com/google-deepmind/mujoco_menagerie`, `kinova_gen3/gen3.xml`, commit `370c43965323c0944b433b202aac5058b5f907a9`.
H: `https://github.com/Kinovarobotics/ros_kortex`, `kortex_description/robots/gen3.xacro`, commit `c3280d8a6a6b5d96590d51538e3f265710a6c77d`.
S: unavailable. A machine-readable H can still be compared to M; no-match differences are never counted as STALE.

Limit semantics: MJCF effort values are supported actuator torque/force envelopes. URDF effort and velocity values are manufacturer declarations retained from XML; MuJoCo does not enforce those tags. Such declaration comparisons are explicitly distinct from compiled inertial/range quantities.


## Source evidence

```json
[
  {
    "url": "https://github.com/Kinovarobotics/ros_kortex/blob/noetic-devel/kortex_description/robots/gen3.xacro",
    "document": "kinova_gen3/README.md",
    "commit": "370c43965323c0944b433b202aac5058b5f907a9",
    "current": true
  }
]
```


## README derivation evidence

Documentation labels are conservative: an automated documented label requires an explicit affected entity and quantity. Broader conversion notes are retained here for review.

>   <compiler meshdir="assets" discardvisual="false" fusestatic="false"/>
> Note `fusestatic="false"` is needed so that base_link is preserved.
>     - Added position actuators with joint limits on joints 2, 4, and 6.

## Kinematics consistency

A proper Kabsch rigid transform aligns all matched zero-pose body origins. The maximum per-origin residual and signed hinge/slide axis angles determine whether CoM can be compared; RMS is also recorded. Fewer than three non-collinear origins give insufficient kinematic coverage. CoM records that fail either required M/H or M/S check are excluded from counts and largest discrepancies. Masses, principal moments and raw joint ranges remain unchanged; a flagged range still requires convention review.

| Pair | Status | Origins / rank | RMS / maximum mm | Disagreeing / checked axes |
|---|---|---:|---:|---:|
| M/H | consistent | 8 / 2 | 0.000447702533 / 0.000927811035 | 0 / 7 |

Exact fitted transforms, per-origin residuals, thresholds and axis vectors:

```json
{
  "M/H": {
    "status": "consistent",
    "matched_body_origins": 8,
    "position_threshold_m": 0.005,
    "axis_threshold_rad": 0.005,
    "residual_definition": "maximum Euclidean residual over matched body origins; Kabsch minimizes RMS, which is also recorded",
    "coordinate_frames": "each snapshot registered to its matched report anchor",
    "anchor_m": "base_link",
    "anchor_other": "base_link",
    "rotation_other_to_m": [
      [
        1.0,
        0.0,
        0.0
      ],
      [
        0.0,
        0.9999999999629587,
        8.607140860265949e-06
      ],
      [
        0.0,
        -8.607140860306811e-06,
        0.9999999999629586
      ]
    ],
    "translation_other_to_m": [
      6.428068737832536e-17,
      -9.277897664375367e-07,
      6.2821401414225875e-09
    ],
    "rms_residual_m": 4.477025330839188e-07,
    "max_residual_m": 9.278110346352728e-07,
    "fit_rank": 2,
    "axis_checks": [
      {
        "joint_m": "joint_1",
        "joint_other": "joint_1",
        "axis_m": [
          0.0,
          0.0,
          -1.0
        ],
        "axis_other_aligned": [
          -2.762899999925444e-18,
          -1.2607306536622171e-06,
          -0.9999999999992053
        ],
        "angle_rad": 1.260730653662551e-06,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "joint_2",
        "joint_other": "joint_2",
        "axis_m": [
          0.0,
          1.0,
          2.2204460492503136e-16
        ],
        "axis_other_aligned": [
          -1.1102004795037241e-16,
          0.99999999999709,
          2.412474449722731e-06
        ],
        "angle_rad": 2.4124744495030263e-06,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "joint_3",
        "joint_other": "joint_3",
        "axis_m": [
          0.0,
          4.474228634151479e-17,
          -1.0
        ],
        "axis_other_aligned": [
          3.098000999981099e-16,
          -1.2607306535705427e-06,
          -0.9999999999992053
        ],
        "angle_rad": 1.2607306536156189e-06,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "joint_4",
        "joint_other": "joint_4",
        "axis_m": [
          0.0,
          1.0,
          4.440892098500628e-16
        ],
        "axis_other_aligned": [
          -2.7754980201347445e-16,
          0.99999999999709,
          2.412474449722731e-06
        ],
        "angle_rad": 2.4124744492809817e-06,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "joint_5",
        "joint_other": "joint_5",
        "axis_m": [
          0.0,
          -1.2446570643470759e-18,
          -1.0
        ],
        "axis_other_aligned": [
          3.065752843992188e-16,
          -1.2607306535705427e-06,
          -0.9999999999992053
        ],
        "angle_rad": 1.260730653569632e-06,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "joint_6",
        "joint_other": "joint_6",
        "axis_m": [
          0.0,
          1.0,
          7.771561172376102e-16
        ],
        "axis_other_aligned": [
          -8.271209801958048e-15,
          0.99999999999709,
          2.412474449722731e-06
        ],
        "angle_rad": 2.412474448947915e-06,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      },
      {
        "joint_m": "joint_7",
        "joint_other": "joint_7",
        "axis_m": [
          0.0,
          -4.723160047020898e-17,
          -1.0
        ],
        "axis_other_aligned": [
          2.101794883040784e-16,
          -1.2607306535705427e-06,
          -0.9999999999992053
        ],
        "angle_rad": 1.260730653523645e-06,
        "axis_source_m": "MuJoCo xaxis at zero pose",
        "axis_source_other": "MuJoCo xaxis at zero pose",
        "type_agrees": true
      }
    ],
    "axis_disagreements": [],
    "com_eligible": true,
    "covariance_singular_values": [
      1.2292947564843546,
      2.4231316318297075e-05,
      0.0
    ],
    "origin_residuals_m": {
      "base_link": 9.278110346352728e-07,
      "shoulder_link": 4.1867232554357296e-07,
      "half_arm_1_link": 5.806246170675935e-07,
      "half_arm_2_link": 7.29786514413242e-08,
      "forearm_link": 3.382222423506133e-07,
      "spherical_wrist_1_link": 1.6494172329121927e-07,
      "spherical_wrist_2_link": 3.2512443695177535e-08,
      "bracelet_link": 2.8683215834691545e-07
    },
    "reason": "Unique proper rigid fit and matched signed axes meet the configured thresholds"
  }
}
```


## Every reported quantity difference

Counts are quantity records, including correlated total/subtree/body mass records; they are not independent robot defects.

| Entity / quantity | M | S | H | H − M | Class | M source | S source | H source |
|---|---|---|---|---|---|---|---|---|
| joint_1 / effort | 105 | unavailable | 39 | -66 | NO MATCHING SOURCE | [inherited actuator input L15](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/kinova_gen3/gen3.xml#L15) | unavailable | [input L65](https://github.com/Kinovarobotics/ros_kortex/blob/c3280d8a6a6b5d96590d51538e3f265710a6c77d/kortex_description/arms/gen3/7dof/urdf/gen3_macro.xacro#L65) |
| joint_2 / effort | 105 | unavailable | 39 | -66 | NO MATCHING SOURCE | [inherited actuator input L15](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/kinova_gen3/gen3.xml#L15) | unavailable | [input L99](https://github.com/Kinovarobotics/ros_kortex/blob/c3280d8a6a6b5d96590d51538e3f265710a6c77d/kortex_description/arms/gen3/7dof/urdf/gen3_macro.xacro#L99) |
| joint_3 / effort | 105 | unavailable | 39 | -66 | NO MATCHING SOURCE | [inherited actuator input L15](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/kinova_gen3/gen3.xml#L15) | unavailable | [input L135](https://github.com/Kinovarobotics/ros_kortex/blob/c3280d8a6a6b5d96590d51538e3f265710a6c77d/kortex_description/arms/gen3/7dof/urdf/gen3_macro.xacro#L135) |
| joint_4 / effort | 105 | unavailable | 39 | -66 | NO MATCHING SOURCE | [inherited actuator input L15](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/kinova_gen3/gen3.xml#L15) | unavailable | [input L169](https://github.com/Kinovarobotics/ros_kortex/blob/c3280d8a6a6b5d96590d51538e3f265710a6c77d/kortex_description/arms/gen3/7dof/urdf/gen3_macro.xacro#L169) |
| joint_5 / effort | 52 | unavailable | 9 | -43 | NO MATCHING SOURCE | [inherited actuator input L18](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/kinova_gen3/gen3.xml#L18) | unavailable | [input L205](https://github.com/Kinovarobotics/ros_kortex/blob/c3280d8a6a6b5d96590d51538e3f265710a6c77d/kortex_description/arms/gen3/7dof/urdf/gen3_macro.xacro#L205) |
| joint_6 / effort | 52 | unavailable | 9 | -43 | NO MATCHING SOURCE | [inherited actuator input L18](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/kinova_gen3/gen3.xml#L18) | unavailable | [input L239](https://github.com/Kinovarobotics/ros_kortex/blob/c3280d8a6a6b5d96590d51538e3f265710a6c77d/kortex_description/arms/gen3/7dof/urdf/gen3_macro.xacro#L239) |
| joint_7 / effort | 52 | unavailable | 9 | -43 | NO MATCHING SOURCE | [inherited actuator input L18](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/kinova_gen3/gen3.xml#L18) | unavailable | [input L301](https://github.com/Kinovarobotics/ros_kortex/blob/c3280d8a6a6b5d96590d51538e3f265710a6c77d/kortex_description/arms/gen3/7dof/urdf/gen3_macro.xacro#L301) |

## Raw CoM records and reporting decisions

Raw values retain the previous root-anchor registration before Kabsch; original world coordinates also remain in the snapshots. Eligible findings above use the fitted transform into M. Excluded raw records below are diagnostic numbers, not findings. No CoM suppression applies to mass or principal inertia moments.

| Entity / quantity | Raw M | Raw S | Raw H | Raw H − M | Decision | M source | S source | H source |
|---|---|---|---|---|---|---|---|---|
| robot / total_com_registered | [-0.000135397123, -0.0117361914, 0.526440417] | unavailable | [-0.000135397123, -0.0117396866, 0.526440298] | [-3.86247024e-17, -3.49522496e-06, -1.18755934e-07] | eligible; compared after Kabsch alignment | [aggregate inputs](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/kinova_gen3/gen3.xml#L1) | unavailable | [aggregate inputs](https://github.com/Kinovarobotics/ros_kortex/blob/c3280d8a6a6b5d96590d51538e3f265710a6c77d/kortex_description/robots/gen3.xacro#L1) |
| base_link / com_registered | [-0.000648, -0.000166, 0.084487] | unavailable | [-0.000648, -0.000166, 0.084487] | [0, 0, 0] | eligible; compared after Kabsch alignment | [CoM/kinematic input L37](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/kinova_gen3/gen3.xml#L37) | unavailable | [CoM/kinematic input L11](https://github.com/Kinovarobotics/ros_kortex/blob/c3280d8a6a6b5d96590d51538e3f265710a6c77d/kortex_description/arms/gen3/7dof/urdf/gen3_macro.xacro#L11) |
| shoulder_link / com_registered | [-2.3e-05, 0.010364, 0.22979] | unavailable | [-2.3e-05, 0.0103634611, 0.229790076] | [2.06676039e-19, -5.38932932e-07, 7.61362158e-08] | eligible; compared after Kabsch alignment | [CoM/kinematic input L42](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/kinova_gen3/gen3.xml#L42) | unavailable | [CoM/kinematic input L33](https://github.com/Kinovarobotics/ros_kortex/blob/c3280d8a6a6b5d96590d51538e3f265710a6c77d/kortex_description/arms/gen3/7dof/urdf/gen3_macro.xacro#L33) |
| half_arm_1_link / com_registered | [-4.4e-05, -0.018653, 0.38439] | unavailable | [-4.4e-05, -0.0186550405, 0.384389814] | [-2.71050543e-20, -2.04046448e-06, -1.85814917e-07] | eligible; compared after Kabsch alignment | [CoM/kinematic input L48](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/kinova_gen3/gen3.xml#L48) | unavailable | [CoM/kinematic input L69](https://github.com/Kinovarobotics/ros_kortex/blob/c3280d8a6a6b5d96590d51538e3f265710a6c77d/kortex_description/arms/gen3/7dof/urdf/gen3_macro.xacro#L69) |
| half_arm_2_link / com_registered | [-4.4e-05, -0.005109, 0.613082] | unavailable | [-4.4e-05, -0.00511312752, 0.613081939] | [-4.01222566e-17, -4.12752145e-06, -6.09689113e-08] | eligible; compared after Kabsch alignment | [CoM/kinematic input L54](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/kinova_gen3/gen3.xml#L54) | unavailable | [CoM/kinematic input L103](https://github.com/Kinovarobotics/ros_kortex/blob/c3280d8a6a6b5d96590d51538e3f265710a6c77d/kortex_description/arms/gen3/7dof/urdf/gen3_macro.xacro#L103) |
| forearm_link / com_registered | [-1.8e-05, -0.033131, 0.781048] | unavailable | [-1.8e-05, -0.0331366387, 0.781047678] | [-8.14879577e-17, -5.6387135e-06, -3.21957212e-07] | eligible; compared after Kabsch alignment | [CoM/kinematic input L60](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/kinova_gen3/gen3.xml#L60) | unavailable | [CoM/kinematic input L139](https://github.com/Kinovarobotics/ros_kortex/blob/c3280d8a6a6b5d96590d51538e3f265710a6c77d/kortex_description/arms/gen3/7dof/urdf/gen3_macro.xacro#L139) |
| spherical_wrist_1_link / com_registered | [1e-06, -0.015068, 0.977883] | unavailable | [1e-06, -0.0150755731, 0.977882842] | [-1.36269178e-16, -7.5731049e-06, -1.57565368e-07] | eligible; compared after Kabsch alignment | [CoM/kinematic input L66](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/kinova_gen3/gen3.xml#L66) | unavailable | [CoM/kinematic input L173](https://github.com/Kinovarobotics/ros_kortex/blob/c3280d8a6a6b5d96590d51538e3f265710a6c77d/kortex_description/arms/gen3/7dof/urdf/gen3_macro.xacro#L173) |
| spherical_wrist_2_link / com_registered | [1e-06, -0.03432505, 1.065413] | unavailable | [1e-06, -0.0343334332, 1.06541267] | [-8.27515191e-17, -8.38320372e-06, -3.34485882e-07] | eligible; compared after Kabsch alignment | [CoM/kinematic input L72](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/kinova_gen3/gen3.xml#L72) | unavailable | [CoM/kinematic input L209](https://github.com/Kinovarobotics/ros_kortex/blob/c3280d8a6a6b5d96590d51538e3f265710a6c77d/kortex_description/arms/gen3/7dof/urdf/gen3_macro.xacro#L209) |
| bracelet_link / com_registered | [0.000281, -0.0362521, 1.155658] | unavailable | [0.000281, -0.0362613682, 1.15565769] | [-9.07477218e-17, -9.26821501e-06, -3.13843821e-07] | eligible; compared after Kabsch alignment | [CoM/kinematic input L78](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/kinova_gen3/gen3.xml#L78) | unavailable | [CoM/kinematic input L244](https://github.com/Kinovarobotics/ros_kortex/blob/c3280d8a6a6b5d96590d51538e3f265710a6c77d/kortex_description/arms/gen3/7dof/urdf/gen3_macro.xacro#L244) |

## Mass accounting

Every contributing compiled body mass is listed here so total/subtree sums can be checked. Links point to explicit inertials or to geometry inputs when the compiler inferred a mass. CoM links identify inertial inputs; world coordinates additionally use the ancestor transforms and the registration recorded below.

| M body | M kg / source | S kg / source | H kg / source |
|---|---|---|---|
| base_link | 1.697 / [input L37](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/kinova_gen3/gen3.xml#L37) | unavailable | 1.697 / [input L12](https://github.com/Kinovarobotics/ros_kortex/blob/c3280d8a6a6b5d96590d51538e3f265710a6c77d/kortex_description/arms/gen3/7dof/urdf/gen3_macro.xacro#L12) |
| shoulder_link | 1.3773 / [input L42](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/kinova_gen3/gen3.xml#L42) | unavailable | 1.3773 / [input L34](https://github.com/Kinovarobotics/ros_kortex/blob/c3280d8a6a6b5d96590d51538e3f265710a6c77d/kortex_description/arms/gen3/7dof/urdf/gen3_macro.xacro#L34) |
| half_arm_1_link | 1.1636 / [input L48](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/kinova_gen3/gen3.xml#L48) | unavailable | 1.1636 / [input L70](https://github.com/Kinovarobotics/ros_kortex/blob/c3280d8a6a6b5d96590d51538e3f265710a6c77d/kortex_description/arms/gen3/7dof/urdf/gen3_macro.xacro#L70) |
| half_arm_2_link | 1.1636 / [input L54](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/kinova_gen3/gen3.xml#L54) | unavailable | 1.1636 / [input L104](https://github.com/Kinovarobotics/ros_kortex/blob/c3280d8a6a6b5d96590d51538e3f265710a6c77d/kortex_description/arms/gen3/7dof/urdf/gen3_macro.xacro#L104) |
| forearm_link | 0.9302 / [input L60](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/kinova_gen3/gen3.xml#L60) | unavailable | 0.9302 / [input L140](https://github.com/Kinovarobotics/ros_kortex/blob/c3280d8a6a6b5d96590d51538e3f265710a6c77d/kortex_description/arms/gen3/7dof/urdf/gen3_macro.xacro#L140) |
| spherical_wrist_1_link | 0.6781 / [input L66](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/kinova_gen3/gen3.xml#L66) | unavailable | 0.6781 / [input L174](https://github.com/Kinovarobotics/ros_kortex/blob/c3280d8a6a6b5d96590d51538e3f265710a6c77d/kortex_description/arms/gen3/7dof/urdf/gen3_macro.xacro#L174) |
| spherical_wrist_2_link | 0.6781 / [input L72](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/kinova_gen3/gen3.xml#L72) | unavailable | 0.6781 / [input L210](https://github.com/Kinovarobotics/ros_kortex/blob/c3280d8a6a6b5d96590d51538e3f265710a6c77d/kortex_description/arms/gen3/7dof/urdf/gen3_macro.xacro#L210) |
| bracelet_link | 0.5 / [input L78](https://github.com/google-deepmind/mujoco_menagerie/blob/370c43965323c0944b433b202aac5058b5f907a9/kinova_gen3/gen3.xml#L78) | unavailable | 0.5 / [input L245](https://github.com/Kinovarobotics/ros_kortex/blob/c3280d8a6a6b5d96590d51538e3f265710a6c77d/kortex_description/arms/gen3/7dof/urdf/gen3_macro.xacro#L245) |
| upstream-only camera_color_frame | unavailable | unavailable | 0 / [geometry/inference input L328](https://github.com/Kinovarobotics/ros_kortex/blob/c3280d8a6a6b5d96590d51538e3f265710a6c77d/kortex_description/arms/gen3/7dof/urdf/gen3_macro.xacro#L328) |
| upstream-only camera_depth_frame | unavailable | unavailable | 0 / [geometry/inference input L322](https://github.com/Kinovarobotics/ros_kortex/blob/c3280d8a6a6b5d96590d51538e3f265710a6c77d/kortex_description/arms/gen3/7dof/urdf/gen3_macro.xacro#L322) |
| upstream-only camera_link | unavailable | unavailable | 0 / [geometry/inference input L316](https://github.com/Kinovarobotics/ros_kortex/blob/c3280d8a6a6b5d96590d51538e3f265710a6c77d/kortex_description/arms/gen3/7dof/urdf/gen3_macro.xacro#L316) |
| upstream-only end_effector_link | unavailable | unavailable | 0 / [geometry/inference input L303](https://github.com/Kinovarobotics/ros_kortex/blob/c3280d8a6a6b5d96590d51538e3f265710a6c77d/kortex_description/arms/gen3/7dof/urdf/gen3_macro.xacro#L303) |
| upstream-only tool_frame | unavailable | unavailable | 0 / [geometry/inference input L46](https://github.com/Kinovarobotics/ros_kortex/blob/c3280d8a6a6b5d96590d51538e3f265710a6c77d/kortex_description/robots/kortex_robot.xacro#L46) |

## Coverage and unmatched elements

```json
{
  "mapping_h": {
    "bodies": {
      "base_link": "base_link",
      "shoulder_link": "shoulder_link",
      "half_arm_1_link": "half_arm_1_link",
      "half_arm_2_link": "half_arm_2_link",
      "forearm_link": "forearm_link",
      "spherical_wrist_1_link": "spherical_wrist_1_link",
      "spherical_wrist_2_link": "spherical_wrist_2_link",
      "bracelet_link": "bracelet_link"
    },
    "joints": {
      "joint_1": "joint_1",
      "joint_2": "joint_2",
      "joint_3": "joint_3",
      "joint_4": "joint_4",
      "joint_5": "joint_5",
      "joint_6": "joint_6",
      "joint_7": "joint_7"
    },
    "body_methods": {
      "base_link": "name",
      "shoulder_link": "name",
      "half_arm_1_link": "name",
      "half_arm_2_link": "name",
      "forearm_link": "name",
      "spherical_wrist_1_link": "name",
      "spherical_wrist_2_link": "name",
      "bracelet_link": "name"
    },
    "joint_methods": {
      "joint_1": "name",
      "joint_2": "name",
      "joint_3": "name",
      "joint_4": "name",
      "joint_5": "name",
      "joint_6": "name",
      "joint_7": "name"
    },
    "unmatched_m_bodies": [],
    "unmatched_upstream_bodies": [
      "camera_color_frame",
      "camera_depth_frame",
      "camera_link",
      "end_effector_link",
      "tool_frame"
    ],
    "unmatched_m_joints": [],
    "unmatched_upstream_joints": [],
    "registration_anchor": {
      "M": "base_link",
      "H": "base_link",
      "root_unmatched": false
    }
  },
  "mapping_s": null,
  "unavailable": [
    {
      "entity": "joint_1",
      "other_entity": "joint_1",
      "quantity": "range",
      "tolerance": "range",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "joint_1",
      "other_entity": "joint_1",
      "quantity": "force",
      "tolerance": "limit",
      "m": 105.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "joint_1",
      "other_entity": "joint_1",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 1.3963,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "joint_2",
      "other_entity": "joint_2",
      "quantity": "force",
      "tolerance": "limit",
      "m": 105.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "joint_2",
      "other_entity": "joint_2",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 1.3963,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "joint_3",
      "other_entity": "joint_3",
      "quantity": "range",
      "tolerance": "range",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "joint_3",
      "other_entity": "joint_3",
      "quantity": "force",
      "tolerance": "limit",
      "m": 105.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "joint_3",
      "other_entity": "joint_3",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 1.3963,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "joint_4",
      "other_entity": "joint_4",
      "quantity": "force",
      "tolerance": "limit",
      "m": 105.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "joint_4",
      "other_entity": "joint_4",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 1.3963,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "joint_5",
      "other_entity": "joint_5",
      "quantity": "range",
      "tolerance": "range",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "joint_5",
      "other_entity": "joint_5",
      "quantity": "force",
      "tolerance": "limit",
      "m": 52.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "joint_5",
      "other_entity": "joint_5",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 1.2218,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "joint_6",
      "other_entity": "joint_6",
      "quantity": "force",
      "tolerance": "limit",
      "m": 52.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "joint_6",
      "other_entity": "joint_6",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 1.2218,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "joint_7",
      "other_entity": "joint_7",
      "quantity": "range",
      "tolerance": "range",
      "m": null,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "joint_7",
      "other_entity": "joint_7",
      "quantity": "force",
      "tolerance": "limit",
      "m": 52.0,
      "other": null,
      "s": null,
      "reason": "quantity absent or not enforced/declared on one side"
    },
    {
      "entity": "joint_7",
      "other_entity": "joint_7",
      "quantity": "velocity",
      "tolerance": "limit",
      "m": null,
      "other": 1.2218,
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
| joint_1 / force | 105 | unavailable | unavailable |
| joint_1 / velocity | unavailable | unavailable | 1.3963 |
| joint_2 / force | 105 | unavailable | unavailable |
| joint_2 / velocity | unavailable | unavailable | 1.3963 |
| joint_3 / force | 105 | unavailable | unavailable |
| joint_3 / velocity | unavailable | unavailable | 1.3963 |
| joint_4 / force | 105 | unavailable | unavailable |
| joint_4 / velocity | unavailable | unavailable | 1.3963 |
| joint_5 / force | 52 | unavailable | unavailable |
| joint_5 / velocity | unavailable | unavailable | 1.2218 |
| joint_6 / force | 52 | unavailable | unavailable |
| joint_6 / velocity | unavailable | unavailable | 1.2218 |
| joint_7 / force | 52 | unavailable | unavailable |
| joint_7 / velocity | unavailable | unavailable | 1.2218 |
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
  "kortex_description/arms/gen3/7dof/meshes/base_link.STL",
  "kortex_description/arms/gen3/7dof/meshes/bracelet_link.STL",
  "kortex_description/arms/gen3/7dof/meshes/bracelet_with_vision_link.STL",
  "kortex_description/arms/gen3/7dof/meshes/forearm_link.STL",
  "kortex_description/arms/gen3/7dof/meshes/half_arm_1_link.STL",
  "kortex_description/arms/gen3/7dof/meshes/half_arm_2_link.STL",
  "kortex_description/arms/gen3/7dof/meshes/shoulder_link.STL",
  "kortex_description/arms/gen3/7dof/meshes/spherical_wrist_1_link.STL",
  "kortex_description/arms/gen3/7dof/meshes/spherical_wrist_2_link.STL",
  "kortex_description/arms/gen3/7dof/urdf/gen3_macro.xacro",
  "kortex_description/arms/gen3/meshes/base_link.STL",
  "kortex_description/arms/gen3/meshes/bracelet_link.STL",
  "kortex_description/arms/gen3/meshes/forearm_link.STL",
  "kortex_description/arms/gen3/meshes/half_arm_1_link.STL",
  "kortex_description/arms/gen3/meshes/half_arm_2_link.STL",
  "kortex_description/arms/gen3/meshes/shoulder_link.STL",
  "kortex_description/arms/gen3/meshes/spherical_wrist_1_link.STL",
  "kortex_description/arms/gen3/meshes/spherical_wrist_2_link.STL",
  "kortex_description/arms/gen3/urdf/gen3_macro.xacro",
  "kortex_description/robots/gen3.xacro",
  "kortex_description/robots/kortex_robot.xacro"
]
```

## Self comparisons

```json
[
  {
    "file": "kinova_gen3/gen3.xml",
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
      "NO MATCHING SOURCE": 7
    },
    "classifications_changed": 0,
    "finding_membership_changes": 0
  },
  "2": {
    "provenance_method": "none",
    "counts": {
      "NO MATCHING SOURCE": 7
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
      "kinova_gen3/gen3.xml"
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
      "end_effector_link",
      "camera_link",
      "camera_depth_frame",
      "camera_color_frame",
      "tool_frame"
    ],
    "assets_loaded": 16,
    "mesh_conversions": [],
    "nonphysical_normalizations": [],
    "xacro_arguments": {
      "arm": "gen3",
      "dof": "7",
      "vision": "true",
      "gripper": "",
      "sim": "false",
      "prefix": ""
    },
    "source_dependencies": [
      "kortex_description/arms/gen3/7dof/urdf/gen3_macro.xacro",
      "kortex_description/robots/gen3.xacro",
      "kortex_description/robots/kortex_robot.xacro",
      "kortex_description/arms/gen3/7dof/meshes/base_link.STL",
      "kortex_description/arms/gen3/7dof/meshes/base_link.STL",
      "kortex_description/arms/gen3/7dof/meshes/shoulder_link.STL",
      "kortex_description/arms/gen3/7dof/meshes/shoulder_link.STL",
      "kortex_description/arms/gen3/7dof/meshes/half_arm_1_link.STL",
      "kortex_description/arms/gen3/7dof/meshes/half_arm_1_link.STL",
      "kortex_description/arms/gen3/7dof/meshes/half_arm_2_link.STL",
      "kortex_description/arms/gen3/7dof/meshes/half_arm_2_link.STL",
      "kortex_description/arms/gen3/7dof/meshes/forearm_link.STL",
      "kortex_description/arms/gen3/7dof/meshes/forearm_link.STL",
      "kortex_description/arms/gen3/7dof/meshes/spherical_wrist_1_link.STL",
      "kortex_description/arms/gen3/7dof/meshes/spherical_wrist_1_link.STL",
      "kortex_description/arms/gen3/7dof/meshes/spherical_wrist_2_link.STL",
      "kortex_description/arms/gen3/7dof/meshes/spherical_wrist_2_link.STL",
      "kortex_description/arms/gen3/7dof/meshes/bracelet_with_vision_link.STL",
      "kortex_description/arms/gen3/7dof/meshes/bracelet_with_vision_link.STL"
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
  "historical_snapshots_reused": 13,
  "primary_physics_unchanged": true,
  "source_matching": "original raw-value provenance criteria retained; kinematic guard applies to reported CoM"
}
```
