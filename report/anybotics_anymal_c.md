# anybotics_anymal_c

Status: **incomplete**. Provenance: **unknown**, confidence **unknown**.

Machine-readable sources were identified, but no standalone source entry compiled. See all candidate errors.

M: `https://github.com/google-deepmind/mujoco_menagerie`, `anybotics_anymal_c/anymal_c.xml`, commit `370c43965323c0944b433b202aac5058b5f907a9`.
S: unavailable. A machine-readable H can still be compared to M; no-match differences are never counted as STALE.

Limit semantics: MJCF effort values are supported actuator torque/force envelopes. URDF effort and velocity values are manufacturer declarations retained from XML; MuJoCo does not enforce those tags. Such declaration comparisons are explicitly distinct from compiled inertial/range quantities.


## Source evidence

```json
[
  {
    "url": "https://github.com/ANYbotics/anymal_b_simple_description/blob/master/urdf/anymal.urdf",
    "document": "anybotics_anymal_c/README.md",
    "commit": "370c43965323c0944b433b202aac5058b5f907a9",
    "current": true
  },
  {
    "url": "https://github.com/ANYbotics/anymal_c_simple_description",
    "document": "anybotics_anymal_c/README.md",
    "commit": "370c43965323c0944b433b202aac5058b5f907a9",
    "current": true
  },
  {
    "url": "https://github.com/ANYbotics/anymal_c_simple_description/tree/master/meshes",
    "document": "anybotics_anymal_c/README.md",
    "commit": "370c43965323c0944b433b202aac5058b5f907a9",
    "current": true
  },
  {
    "url": "https://github.com/Andrew-Luo1",
    "document": "anybotics_anymal_c/README.md",
    "commit": "370c43965323c0944b433b202aac5058b5f907a9",
    "current": true
  },
  {
    "url": "https://github.com/kevinzakka/obj2mjcf",
    "document": "anybotics_anymal_c/README.md",
    "commit": "370c43965323c0944b433b202aac5058b5f907a9",
    "current": true
  },
  {
    "url": "https://github.com/google-deepmind/mujoco/blob/main/mjx/training_apg.ipynb",
    "document": "anybotics_anymal_c/README.md",
    "commit": "d3694476e267ead94f869c1e7aa5eff2d259e4d9",
    "current": false
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
  "https://github.com/ANYbotics/anymal_c_simple_description urdf/anymal.urdf at 87b68511622f0f17e78d9ddca7d862f150a93fb4: ValueError: Error: inertia must satisfy A + B >= C; use 'balanceinertia' to fix\nElement name 'depth_camera_front_camera', id 8"
]
```

## Self comparisons

```json
[
  {
    "file": "anybotics_anymal_c/anymal_c.xml",
    "status": "passed",
    "findings": 0
  },
  {
    "file": "anybotics_anymal_c/anymal_c_mjx.xml",
    "status": "passed",
    "findings": 0
  }
]
```

## Rerun

```json
{
  "mode": "frozen revisions",
  "self_variants_recompiled": 2,
  "upstream_comparison": "unavailable, previously recorded source/compilation gap retained"
}
```
