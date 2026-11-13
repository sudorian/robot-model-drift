# umi_gripper

Status: **unknown upstream**. Provenance: **unknown**, confidence **unknown**.

Current README describes a SolidWorks conversion from a Google Docs CAD source. No public machine-readable upstream is named; unrelated historical template links are retained only as evidence.

M: `https://github.com/google-deepmind/mujoco_menagerie`, `umi_gripper/umi_gripper.xml`, commit `370c43965323c0944b433b202aac5058b5f907a9`.
S: unavailable. A machine-readable H can still be compared to M; no-match differences are never counted as STALE.

Limit semantics: MJCF effort values are supported actuator torque/force envelopes. URDF effort and velocity values are manufacturer declarations retained from XML; MuJoCo does not enforce those tags. Such declaration comparisons are explicitly distinct from compiled inertial/range quantities.


## Source evidence

```json
[
  {
    "url": "https://github.com/pal-robotics/talos_robot/tree/kinetic-devel/talos_description",
    "document": "umi_gripper/README.md",
    "commit": "884e0e1983c7c80db91740af56a648fdeb3989dd",
    "current": false
  }
]
```


## README derivation evidence

Documentation labels are conservative: an automated documented label requires an explicit affected entity and quantity. Broader conversion notes are retained here for review.

> 2.  Added `<mujoco> <compiler balanceinertia="true" discardvisual="false"/> </mujoco>` to the URDF's
> 7. Added a `<tendon>` section with a fixed tendon named split to synchronize the movement of both fingers.
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
    "file": "umi_gripper/umi_gripper.xml",
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
