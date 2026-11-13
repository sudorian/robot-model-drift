# pal_talos

Status: **incomplete**. Provenance: **unknown**, confidence **unknown**.

Machine-readable sources were identified, but no standalone source entry compiled. See all candidate errors.

M: `https://github.com/google-deepmind/mujoco_menagerie`, `pal_talos/talos.xml`, commit `370c43965323c0944b433b202aac5058b5f907a9`.
S: unavailable. A machine-readable H can still be compared to M; no-match differences are never counted as STALE.

Limit semantics: MJCF effort values are supported actuator torque/force envelopes. URDF effort and velocity values are manufacturer declarations retained from XML; MuJoCo does not enforce those tags. Such declaration comparisons are explicitly distinct from compiled inertial/range quantities.


## Source evidence

```json
[
  {
    "url": "https://github.com/pal-robotics/talos_robot/tree/kinetic-devel/talos_description",
    "document": "pal_talos/README.md",
    "commit": "370c43965323c0944b433b202aac5058b5f907a9",
    "current": true
  }
]
```


## README derivation evidence

Documentation labels are conservative: an automated documented label requires an explicit affected entity and quantity. Broader conversion notes are retained here for review.

>  2. Added `<mujoco> <compiler meshdir="../meshes/" strippath="false" balanceinertia="true" autolimits="true" discardvisual="false"/> </mujoco>` to the URDF in order to preserve visual geometries and configure other [parameters](https://mujoco.readthedocs.io/en/stable/XMLreference.html#compiler).
>  3. Removed `package://` shortcuts and fixed file paths to use assets only from the local `assets` folder.
>  5. Added a free joint `<joint name="reference" type="free"/>` to the base and fixed the body tree by adding `<body  name="base_link"  pos="0 0 0"></body>` around the base geom.
>  6. Added `<inertial pos="-0.05709419 0.00153054 -0.0762521" mass="15.36284" fullinertia="0.20105075811 0.08411496729 0.2318908414 0.00023244734 0.0040167728 -0.00087206649"/> <geom type="mesh" class="visual" density="0" rgba="0.9 0.9 0.9 1" mesh="base_link"/>` base inertia that was not automatically converted.
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
  "https://github.com/pal-robotics/talos_robot talos_description/robots/talos_full_v2.urdf.xacro at 79709aa4f4f453ec18a5e467e65f84ff58ea24d0: XacroException: No such file or directory: .cache/pal-robotics__talos_robot/.drift_xacro/tmp9ek636ay/.unresolved_package/pal_urdf_utils/urdf/deg_to_rad.urdf.xacro [Errno 2] No such file or directory: '.cache/pal-robotics__talos_robot/.drift_xacro/tmp9ek636ay/.unresolved_package/pal_urdf_utils/urdf/deg_to_rad.urdf.xacro'",
  "https://github.com/pal-robotics/talos_robot talos_description/robots/talos_arm_right.urdf.xacro at 79709aa4f4f453ec18a5e467e65f84ff58ea24d0: XacroException: No such file or directory: .cache/pal-robotics__talos_robot/.drift_xacro/tmpd1f6v72q/.unresolved_package/pal_urdf_utils/urdf/deg_to_rad.urdf.xacro [Errno 2] No such file or directory: '.cache/pal-robotics__talos_robot/.drift_xacro/tmpd1f6v72q/.unresolved_package/pal_urdf_utils/urdf/deg_to_rad.urdf.xacro'",
  "https://github.com/pal-robotics/talos_robot talos_description/urdf/talos_full_common.urdf.xacro at 79709aa4f4f453ec18a5e467e65f84ff58ea24d0: XacroException: No such file or directory: .cache/pal-robotics__talos_robot/.drift_xacro/tmp9h4nspii/.unresolved_package/pal_urdf_utils/urdf/deg_to_rad.urdf.xacro [Errno 2] No such file or directory: '.cache/pal-robotics__talos_robot/.drift_xacro/tmp9h4nspii/.unresolved_package/pal_urdf_utils/urdf/deg_to_rad.urdf.xacro'",
  "https://github.com/pal-robotics/talos_robot talos_description/robots/talos_lower_body.urdf.xacro at 79709aa4f4f453ec18a5e467e65f84ff58ea24d0: XacroException: No such file or directory: .cache/pal-robotics__talos_robot/.drift_xacro/tmp138mtm_p/.unresolved_package/pal_urdf_utils/urdf/ft_sensors/ati_talos.urdf.xacro [Errno 2] No such file or directory: '.cache/pal-robotics__talos_robot/.drift_xacro/tmp138mtm_p/.unresolved_package/pal_urdf_utils/urdf/ft_sensors/ati_talos.urdf.xacro'",
  "https://github.com/pal-robotics/talos_robot talos_description/robots/talos_full_no_grippers.urdf.xacro at 79709aa4f4f453ec18a5e467e65f84ff58ea24d0: XacroException: Undefined substitution argument enable_crane",
  "https://github.com/pal-robotics/talos_robot talos_description/robots/talos_full_fake_grippers.urdf.xacro at 79709aa4f4f453ec18a5e467e65f84ff58ea24d0: XacroException: Undefined substitution argument enable_crane",
  "https://github.com/pal-robotics/talos_robot talos_description/robots/talos_lower_body_torso_head.urdf.xacro at 79709aa4f4f453ec18a5e467e65f84ff58ea24d0: XacroException: Undefined substitution argument enable_crane"
]
```

## Self comparisons

```json
[
  {
    "file": "pal_talos/talos.xml",
    "status": "passed",
    "findings": 0
  },
  {
    "file": "pal_talos/talos_motor.xml",
    "status": "passed",
    "findings": 0
  },
  {
    "file": "pal_talos/talos_position.xml",
    "status": "passed",
    "findings": 0
  }
]
```

## Rerun

```json
{
  "mode": "frozen revisions",
  "self_variants_recompiled": 3,
  "upstream_comparison": "unavailable, previously recorded source/compilation gap retained"
}
```
