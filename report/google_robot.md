# google_robot

Status: **unknown upstream**. Provenance: **unknown**, confidence **unknown**.

No machine-readable upstream repository found in README, CHANGELOG, or their history. Vendor/CAD/web descriptions were not fetched under the network rules.

M: `https://github.com/google-deepmind/mujoco_menagerie`, `google_robot/robot.xml`, commit `370c43965323c0944b433b202aac5058b5f907a9`.
S: unavailable. A machine-readable H can still be compared to M; no-match differences are never counted as STALE.

Limit semantics: MJCF effort values are supported actuator torque/force envelopes. URDF effort and velocity values are manufacturer declarations retained from XML; MuJoCo does not enforce those tags. Such declaration comparisons are explicitly distinct from compiled inertial/range quantities.


## README derivation evidence

Documentation labels are conservative: an automated documented label requires an explicit affected entity and quantity. Broader conversion notes are retained here for review.

> This package contains a simplified robot description (MJCF) of a [mobile manipulator](https://rl-at-scale.github.io/) with a 7 degree-of-freedom (DoF) arm and a parallel jaw gripper developed by Google.
>     @inproceedings{rlscale2023rss,
>         title={Deep RL at Scale: Sorting Waste in Office Buildings with a Fleet of Mobile Manipulators},
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
    "file": "google_robot/robot.xml",
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
