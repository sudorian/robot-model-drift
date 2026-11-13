# apptronik_apollo

Status: **unknown upstream**. Provenance: **unknown**, confidence **unknown**.

No machine-readable upstream repository found in README, CHANGELOG, or their history. Vendor/CAD/web descriptions were not fetched under the network rules.

M: `https://github.com/google-deepmind/mujoco_menagerie`, `apptronik_apollo/apptronik_apollo.xml`, commit `370c43965323c0944b433b202aac5058b5f907a9`.
S: unavailable. A machine-readable H can still be compared to M; no-match differences are never counted as STALE.

Limit semantics: MJCF effort values are supported actuator torque/force envelopes. URDF effort and velocity values are manufacturer declarations retained from XML; MuJoCo does not enforce those tags. Such declaration comparisons are explicitly distinct from compiled inertial/range quantities.


## Source evidence

```json
[
  {
    "url": "https://github.com/google-deepmind/mujoco_menagerie/issues/136.",
    "document": "apptronik_apollo/README.md",
    "commit": "23ab4678660a14aef753d3f602efc7af82f2b4c3",
    "current": false
  },
  {
    "url": "https://github.com/google-deepmind/mujoco_menagerie/issues/136.",
    "document": "apptronik_apollo/CHANGELOG.md",
    "commit": "370c43965323c0944b433b202aac5058b5f907a9",
    "current": true
  },
  {
    "url": "https://github.com/google-deepmind/mujoco_menagerie/issues/318",
    "document": "apptronik_apollo/CHANGELOG.md",
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
[]
```

## Self comparisons

```json
[
  {
    "file": "apptronik_apollo/apptronik_apollo.xml",
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
