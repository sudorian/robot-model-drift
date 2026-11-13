# pal_tiago

Status: **incomplete**. Provenance: **unknown**, confidence **unknown**.

Machine-readable sources were identified, but no standalone source entry compiled. See all candidate errors.

M: `https://github.com/google-deepmind/mujoco_menagerie`, `pal_tiago/tiago.xml`, commit `370c43965323c0944b433b202aac5058b5f907a9`.
S: unavailable. A machine-readable H can still be compared to M; no-match differences are never counted as STALE.

Limit semantics: MJCF effort values are supported actuator torque/force envelopes. URDF effort and velocity values are manufacturer declarations retained from XML; MuJoCo does not enforce those tags. Such declaration comparisons are explicitly distinct from compiled inertial/range quantities.


## Source evidence

```json
[
  {
    "url": "https://github.com/pal-robotics/tiago_robot/blob/kinetic-devel/tiago_description",
    "document": "pal_tiago/README.md",
    "commit": "370c43965323c0944b433b202aac5058b5f907a9",
    "current": true
  }
]
```


## README derivation evidence

Documentation labels are conservative: an automated documented label requires an explicit affected entity and quantity. Broader conversion notes are retained here for review.

>  2. Added `<mujoco>  <compiler meshdir="../meshes/" strippath="false"balanceinertia="true" autolimits="true" discardvisual="false"/> </mujoco>` to the URDF in order to preserve visual geometries and configure other [parameters](https://mujoco.readthedocs.io/en/stable/XMLreference.html#compiler).
>  4. Removed `package://` shortcuts and fixed file paths to use assets only from the local `assets` folder.
>  6. Added a free joint `<joint  name="reference"  type="free"/>` to the base and fixed the body tree by adding `<body  name="base_link" pos="0 0 0"></body>` around the base geom.
>  7. Added `<inertial pos="0 0 0" mass="28.26649" fullinertia="0.465408937 0.483193291 0.550939703 0.002160024 -0.001760255 -0.000655952"/>` base inertia that was not automatically converted.
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
  "https://github.com/pal-robotics/tiago_robot tiago_description/robots/tiago.urdf.xacro at f1c33c92bdde7c1dd79f0c3e739e98a233dbd30b: XacroException: No such file or directory: .cache/pal-robotics__tiago_robot/.drift_xacro/tmpd2a1xwz8/.unresolved_package/pal_urdf_utils/urdf/deg_to_rad.urdf.xacro [Errno 2] No such file or directory: '.cache/pal-robotics__tiago_robot/.drift_xacro/tmpd2a1xwz8/.unresolved_package/pal_urdf_utils/urdf/deg_to_rad.urdf.xacro'",
  "https://github.com/pal-robotics/tiago_robot tiago_description/urdf/calibration/eye_hand_calibration.urdf.xacro at f1c33c92bdde7c1dd79f0c3e739e98a233dbd30b: XacroException: No such file or directory: .cache/pal-robotics__tiago_robot/.drift_xacro/tmp0k13uqew/.unresolved_package/pal_urdf_utils/urdf/deg_to_rad.urdf.xacro [Errno 2] No such file or directory: '.cache/pal-robotics__tiago_robot/.drift_xacro/tmp0k13uqew/.unresolved_package/pal_urdf_utils/urdf/deg_to_rad.urdf.xacro'"
]
```

## Self comparisons

```json
[
  {
    "file": "pal_tiago/tiago.xml",
    "status": "passed",
    "findings": 0
  },
  {
    "file": "pal_tiago/tiago_motor.xml",
    "status": "passed",
    "findings": 0
  },
  {
    "file": "pal_tiago/tiago_position.xml",
    "status": "passed",
    "findings": 0
  },
  {
    "file": "pal_tiago/tiago_velocity.xml",
    "status": "passed",
    "findings": 0
  }
]
```

## Rerun

```json
{
  "mode": "frozen revisions",
  "self_variants_recompiled": 4,
  "upstream_comparison": "unavailable, previously recorded source/compilation gap retained"
}
```
