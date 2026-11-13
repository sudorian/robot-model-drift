# Three independent XML cross-checks

Random seed: 20261113. Reported differences shuffled: 587. Physical values are computed directly from XML without importing MuJoCo. The independent parser handles masses, subtrees, FK/world CoM, inertia eigenvalues, ranges and supported limits. Eligible CoM rigid fits are independently recomputed from XML body origins, without reusing cached transforms. Excluded convention/coverage CoM records are outside the finding population. Xacro uses the prescribed input-expansion package. Every skipped non-extractable draw is recorded in JSON.

| Model / entity / quantity | Compiled M / S / H | Direct XML M / S / H | Agree? |
|---|---|---|---|
| robotis_op3 / head_tilt / effort | {"m": 5.0, "s": null, "h": 1000.0} | {"m": 5.0, "s": null, "h": 1000.0} | yes |
| universal_robots_ur5e / wrist_1_link / principal_moments | {"m": [0.0021942, 0.0025599, 0.0025599], "s": null, "h": [0.0011986756140664695, 0.0014236273687042765, 0.0016550170172292542]} | {"m": [0.0021942, 0.0025599, 0.0025599], "s": null, "h": [0.0011986756140664695, 0.0014236273687040747, 0.0016550170172294559]} | yes |
| robotis_omy_3m / joint1 / effort | {"m": 61.4, "s": null, "h": 1000.0} | {"m": 61.4, "s": null, "h": 1000.0} | yes |

Full sample and skipped draws: `report/cross_checks.json`.
