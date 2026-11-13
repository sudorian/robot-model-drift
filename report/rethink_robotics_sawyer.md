# rethink_robotics_sawyer

Status: **incomplete**. Provenance: **unknown**, confidence **unknown**.

Machine-readable sources were identified, but no standalone source entry compiled. See all candidate errors.

M: `https://github.com/google-deepmind/mujoco_menagerie`, `rethink_robotics_sawyer/sawyer.xml`, commit `370c43965323c0944b433b202aac5058b5f907a9`.
S: unavailable. A machine-readable H can still be compared to M; no-match differences are never counted as STALE.

Limit semantics: MJCF effort values are supported actuator torque/force envelopes. URDF effort and velocity values are manufacturer declarations retained from XML; MuJoCo does not enforce those tags. Such declaration comparisons are explicitly distinct from compiled inertial/range quantities.


## Source evidence

```json
[
  {
    "url": "https://github.com/RethinkRobotics/sawyer_robot/blob/master/sawyer_description/urdf/",
    "document": "rethink_robotics_sawyer/README.md",
    "commit": "370c43965323c0944b433b202aac5058b5f907a9",
    "current": true
  },
  {
    "url": "https://github.com/RethinkRobotics/sawyer_robot/tree/master/sawyer_description",
    "document": "rethink_robotics_sawyer/README.md",
    "commit": "370c43965323c0944b433b202aac5058b5f907a9",
    "current": true
  },
  {
    "url": "https://github.com/RethinkRobotics/sawyer_robot/tree/master/sawyer_description/meshes",
    "document": "rethink_robotics_sawyer/README.md",
    "commit": "370c43965323c0944b433b202aac5058b5f907a9",
    "current": true
  },
  {
    "url": "https://github.com/kevinzakka/obj2mjcf",
    "document": "rethink_robotics_sawyer/README.md",
    "commit": "370c43965323c0944b433b202aac5058b5f907a9",
    "current": true
  }
]
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
  "https://github.com/RethinkRobotics/sawyer_robot sawyer_description/urdf/sawyer.urdf.xacro at d1ef3d0ca83d0a943839783efd9b162e6930f2b7: ValueError: Error: error 'inertia must have positive eigenvalues' in fullinertia\nElement name 'right_hand', id 20",
  "https://github.com/RethinkRobotics/sawyer_robot sawyer_description/urdf/sawyer_base.urdf.xacro at d1ef3d0ca83d0a943839783efd9b162e6930f2b7: ValueError: Error: error 'inertia must have positive eigenvalues' in fullinertia\nElement name 'right_hand', id 20",
  "https://github.com/RethinkRobotics/sawyer_robot sawyer_description/urdf/sawyer_base.gazebo.xacro at d1ef3d0ca83d0a943839783efd9b162e6930f2b7: ValueError: XML Error: URDF joint parent or child missing\nElement 'joint', line 1\n",
  "https://github.com/RethinkRobotics/sawyer_robot sawyer_description/urdf/sawyer_electric_gripper.urdf.xacro at d1ef3d0ca83d0a943839783efd9b162e6930f2b7: XacroException: No such file or directory: .cache/RethinkRobotics__sawyer_robot/.drift_xacro/tmpebhov2n1/.unresolved_package/intera_tools_description/urdf/electric_gripper/rethink_electric_gripper.xacro [Errno 2] No such file or directory: '.cache/RethinkRobotics__sawyer_robot/.drift_xacro/tmpebhov2n1/.unresolved_package/intera_tools_description/urdf/electric_gripper/rethink_electric_gripper.xacro'"
]
```

## Self comparisons

```json
[
  {
    "file": "rethink_robotics_sawyer/sawyer.xml",
    "status": "passed",
    "findings": 0
  }
]
```

## Rerun

```json
{
  "mode": "frozen revisions",
  "self_variants_recompiled": 1,
  "upstream_comparison": "unavailable, previously recorded source/compilation gap retained"
}
```
