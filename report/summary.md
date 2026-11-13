# Robot model drift survey

All values and errors below are measured results from this run. Unknown or failed coverage is listed explicitly. Proxy classes carry `(inferred)`; `NO MATCHING SOURCE` never contributes to STALE counts.

**20 STALE quantity records across 3 models:** `seeed_rebot_devarm`, `ufactory_lite6`, `ufactory_xarm7`. 13 of these are limit-declaration/envelope comparisons; see the limit semantics below.

Coverage: 47/71 folders have compiled M/H comparisons; {"complete": 32, "unknown upstream": 19, "incomplete": 5, "partial history": 15}. Body/joint coverage within each comparison is specified by its unmatched lists.

Kinematics guard: **67 raw CoM differences excluded** from counts and largest discrepancies. Convention differs in 6 models; insufficient unique-fit coverage in 11. Raw numbers, residuals, fitted transforms and axis comparisons remain in each model report. Mass and principal-moment records are retained. Joint ranges remain raw and are marked for convention review when flagged.

“Upstream changed?” compares S with H when S compiled, otherwise the earliest successfully compiled public revision with H. It concerns the compared physical quantities, not merely different Git SHAs. It does not assert that every intermediate revision was unchanged.

| Model | Provenance / confidence | Upstream changed? | Class counts | Largest discrepancy | Kinematics / CoM exclusion | Status |
|---|---|---|---|---|---|---|
| [agilex_piper](agilex_piper.md) | none / none | no | {"NO MATCHING SOURCE": 16} | link6 mass: Δ -1.00481286; 167.468809× tolerance | M/H: kinematic convention differs; 8 raw CoM differences excluded | complete |
| [agility_cassie](agility_cassie.md) | unknown / unknown | unknown | {} | unavailable / no discrepancy | unavailable | unknown upstream |
| [aloha](aloha.md) | unknown / unknown | unknown | {} | unavailable / no discrepancy | unavailable | unknown upstream |
| [anybotics_anymal_b](anybotics_anymal_b.md) | none / none | no | {"NO MATCHING SOURCE": 30} | LF_SHANK com_registered: Δ [-0.0388227419, 0.00863217071, 0.151798126]; 313.843213× tolerance | M/H: consistent; 0 raw CoM differences excluded | complete |
| [anybotics_anymal_c](anybotics_anymal_c.md) | unknown / unknown | unknown | {} | unavailable / no discrepancy | unavailable | incomplete |
| [apptronik_apollo](apptronik_apollo.md) | unknown / unknown | unknown | {} | unavailable / no discrepancy | unavailable | unknown upstream |
| [arx_l5](arx_l5.md) | pinned / high | no | {"undocumented derivation difference": 25} | joint2 range: Δ [-10, 6.86]; 2000× tolerance | M/H: kinematic convention differs; M/S: kinematic convention differs; 10 raw CoM differences excluded | complete |
| [berkeley_humanoid](berkeley_humanoid.md) | dated match / medium | no | {} | unavailable / no discrepancy | M/H: consistent; M/S: consistent; 0 raw CoM differences excluded | complete |
| [bitcraze_crazyflie_2](bitcraze_crazyflie_2.md) | dated match / medium | no | {} | unavailable / no discrepancy | M/H: insufficient kinematic coverage; M/S: insufficient kinematic coverage; 0 raw CoM differences excluded | complete |
| [booster_t1](booster_t1.md) | dated match / medium | no | {} | unavailable / no discrepancy | M/H: consistent; M/S: consistent; 0 raw CoM differences excluded | complete |
| [boston_dynamics_spot](boston_dynamics_spot.md) | unknown / incomplete | no | {"unknown": 4} | body principal_moments: Δ [0.0898200886, 1.77619383, 1.81713568]; 93.2545602× tolerance | M/H: insufficient kinematic coverage; 2 raw CoM differences excluded | partial history |
| [dynamixel_2r](dynamixel_2r.md) | unknown / unknown | unknown | {} | unavailable / no discrepancy | unavailable | unknown upstream |
| [fanuc_crx5ia](fanuc_crx5ia.md) | pinned / high | no | {} | unavailable / no discrepancy | M/H: consistent; M/S: consistent; 0 raw CoM differences excluded | complete |
| [flexiv_rizon4](flexiv_rizon4.md) | unknown / unknown | unknown | {} | unavailable / no discrepancy | unavailable | unknown upstream |
| [flexiv_rizon4s](flexiv_rizon4s.md) | unknown / unknown | unknown | {} | unavailable / no discrepancy | unavailable | unknown upstream |
| [flybody](flybody.md) | pinned / high | no | {} | unavailable / no discrepancy | M/H: consistent; M/S: consistent; 0 raw CoM differences excluded | complete |
| [fourier_n1](fourier_n1.md) | dated match / medium | no | {} | unavailable / no discrepancy | M/H: consistent; M/S: consistent; 0 raw CoM differences excluded | complete |
| [franka_emika_panda](franka_emika_panda.md) | none / none | no | {"NO MATCHING SOURCE": 1} | robot total_mass: Δ 74.9363727; 163.566047× tolerance | M/H: insufficient kinematic coverage; 1 raw CoM differences excluded | complete |
| [franka_fr3](franka_fr3.md) | unknown / incomplete | yes | {"unknown": 14} | fr3_link7 subtree_mass: Δ 0.712600286; 106.378631× tolerance | M/H: consistent; 0 raw CoM differences excluded | partial history |
| [franka_fr3_duo](franka_fr3_duo.md) | pinned / high | no | {"undocumented derivation difference": 24} | base mass: Δ -4.09385; 200× tolerance | M/H: consistent; M/S: consistent; 0 raw CoM differences excluded | partial history |
| [franka_fr3_v2](franka_fr3_v2.md) | unknown / incomplete | yes | {"unknown": 22} | fr3v2_link8 subtree_mass: Δ 0.7126; 200× tolerance | M/H: consistent; 0 raw CoM differences excluded | partial history |
| [google_barkour_v0](google_barkour_v0.md) | unknown / unknown | unknown | {} | unavailable / no discrepancy | unavailable | unknown upstream |
| [google_barkour_vb](google_barkour_vb.md) | unknown / unknown | unknown | {} | unavailable / no discrepancy | unavailable | unknown upstream |
| [google_robot](google_robot.md) | unknown / unknown | unknown | {} | unavailable / no discrepancy | unavailable | unknown upstream |
| [hello_robot_stretch](hello_robot_stretch.md) | unknown / unknown | unknown | {} | unavailable / no discrepancy | unavailable | unknown upstream |
| [hello_robot_stretch_3](hello_robot_stretch_3.md) | unknown / unknown | unknown | {} | unavailable / no discrepancy | unavailable | unknown upstream |
| [i2rt_yam](i2rt_yam.md) | none / none | no | {"NO MATCHING SOURCE": 4} | joint1 force: Δ -18; 64.2857143× tolerance | M/H: insufficient kinematic coverage; 1 raw CoM differences excluded | complete |
| [iit_softfoot](iit_softfoot.md) | dated match / medium | no | {} | unavailable / no discrepancy | M/H: consistent; M/S: consistent; 0 raw CoM differences excluded | complete |
| [kinova_gen3](kinova_gen3.md) | none / none | yes | {"NO MATCHING SOURCE": 7} | joint_5 effort: Δ -43; 82.6923077× tolerance | M/H: consistent; 0 raw CoM differences excluded | complete |
| [kuka_iiwa_14](kuka_iiwa_14.md) | none / none | no | {"NO MATCHING SOURCE": 2} | base mass: Δ -5; 200× tolerance | M/H: insufficient kinematic coverage; 1 raw CoM differences excluded | complete |
| [leap_hand](leap_hand.md) | none / none | no | {"NO MATCHING SOURCE": 1} | palm principal_moments: Δ [8.01316016e-05, 4.93172e-05, 0.000121977198]; 30.7173452× tolerance | M/H: insufficient kinematic coverage; 2 raw CoM differences excluded | complete |
| [low_cost_robot_arm](low_cost_robot_arm.md) | none / none | yes | {"NO MATCHING SOURCE": 15} | pitch range: Δ [-1.57, 2.54]; 508× tolerance | M/H: consistent; 0 raw CoM differences excluded | complete |
| [ms_human_700](ms_human_700.md) | dated match / medium | no | {} | unavailable / no discrepancy | M/H: consistent; M/S: consistent; 0 raw CoM differences excluded | complete |
| [pal_talos](pal_talos.md) | unknown / unknown | unknown | {} | unavailable / no discrepancy | unavailable | incomplete |
| [pal_tiago](pal_tiago.md) | unknown / unknown | unknown | {} | unavailable / no discrepancy | unavailable | incomplete |
| [pal_tiago_dual](pal_tiago_dual.md) | unknown / unknown | unknown | {} | unavailable / no discrepancy | unavailable | incomplete |
| [pndbotics_adam_lite](pndbotics_adam_lite.md) | unknown / unknown | unknown | {} | unavailable / no discrepancy | unavailable | unknown upstream |
| [rainbow_robotics_rby1](rainbow_robotics_rby1.md) | none / none | yes | {"NO MATCHING SOURCE": 64} | right_arm_4 range: Δ [3.14159735, -3.14159735]; 628.319469× tolerance | M/H: kinematic convention differs; 13 raw CoM differences excluded | complete |
| [realsense_d435i](realsense_d435i.md) | unknown / incomplete | yes | {"unknown": 1} | d435i principal_moments: Δ [0.000494385331, 0.003842202, 0.003843249]; 99.0871309× tolerance | M/H: insufficient kinematic coverage; 2 raw CoM differences excluded | partial history |
| [rethink_robotics_sawyer](rethink_robotics_sawyer.md) | unknown / unknown | unknown | {} | unavailable / no discrepancy | unavailable | incomplete |
| [robot_soccer_kit](robot_soccer_kit.md) | unknown / unknown | unknown | {} | unavailable / no discrepancy | unavailable | unknown upstream |
| [robotiq_2f85](robotiq_2f85.md) | none / none | yes | {"NO MATCHING SOURCE": 1} | robot total_mass: Δ -0.673171652; 127.905438× tolerance | M/H: insufficient kinematic coverage; 1 raw CoM differences excluded | complete |
| [robotiq_2f85_v4](robotiq_2f85_v4.md) | none / none | yes | {"NO MATCHING SOURCE": 1} | robot total_mass: Δ -0.520563173; 115.680723× tolerance | M/H: insufficient kinematic coverage; 1 raw CoM differences excluded | complete |
| [robotis_omy_3m](robotis_omy_3m.md) | unknown / incomplete | no | {"unknown": 7} | joint3 range: Δ [-3.66519131, 3.66519131]; 733.038261× tolerance | M/H: consistent; 0 raw CoM differences excluded | partial history |
| [robotis_op3](robotis_op3.md) | unknown / incomplete | yes | {"unknown": 20} | head_pan effort: Δ 995; 99.5× tolerance | M/H: consistent; 0 raw CoM differences excluded | partial history |
| [robotstudio_so101](robotstudio_so101.md) | pinned / high | no | {"undocumented derivation difference": 20} | wrist subtree_mass: Δ -0.013444; 13.444× tolerance | M/H: consistent; M/S: consistent; 0 raw CoM differences excluded | complete |
| [seeed_rebot_devarm](seeed_rebot_devarm.md) | dated match / medium | yes | {"STALE": 7} | link6 principal_moments: Δ [-1.02009955e-05, -1.03197228e-05, -1.99336522e-05]; 70× tolerance | M/H: consistent; M/S: consistent; 0 raw CoM differences excluded | partial history |
| [shadow_dexee](shadow_dexee.md) | unknown / unknown | unknown | {} | unavailable / no discrepancy | unavailable | unknown upstream |
| [shadow_hand](shadow_hand.md) | unknown / incomplete | yes | {"unknown": 26} | rh_WRJ1 effort: Δ 25; 83.3333333× tolerance | M/H: consistent; 0 raw CoM differences excluded | partial history |
| [sharpa_wave](sharpa_wave.md) | pinned / high | no | {"undocumented derivation difference": 13} | left_pinky_MC com_registered: Δ [0.00108858542, 2.38214723e-05, 0.0624654091]; 124.949797× tolerance | M/H: consistent; M/S: consistent; 0 raw CoM differences excluded | complete |
| [skydio_x2](skydio_x2.md) | unknown / unknown | unknown | {} | unavailable / no discrepancy | unavailable | unknown upstream |
| [stanford_tidybot](stanford_tidybot.md) | unknown / unknown | unknown | {} | unavailable / no discrepancy | unavailable | unknown upstream |
| [tetheria_aero_hand_open](tetheria_aero_hand_open.md) | unknown / unknown | unknown | {} | unavailable / no discrepancy | unavailable | unknown upstream |
| [toddlerbot_2xc](toddlerbot_2xc.md) | dated match / medium | no | {} | unavailable / no discrepancy | M/H: consistent; M/S: consistent; 0 raw CoM differences excluded | complete |
| [toddlerbot_2xm](toddlerbot_2xm.md) | dated match / medium | no | {} | unavailable / no discrepancy | M/H: consistent; M/S: consistent; 0 raw CoM differences excluded | complete |
| [trossen_vx300s](trossen_vx300s.md) | none / none | yes | {"NO MATCHING SOURCE": 10} | gripper_prop_link principal_moments: Δ [9.84686e-05, 9.71132e-05, 9.57021e-05]; 98.4686× tolerance | M/H: insufficient kinematic coverage; 2 raw CoM differences excluded | complete |
| [trossen_wx250s](trossen_wx250s.md) | none / none | no | {"NO MATCHING SOURCE": 15} | wx250s/gripper_link principal_moments: Δ [-0.00301656894, -0.00305479106, -0.00305055]; 99.4516993× tolerance | M/H: consistent; 0 raw CoM differences excluded | complete |
| [trossen_wxai](trossen_wxai.md) | unknown / unknown | unknown | {} | unavailable / no discrepancy | unavailable | unknown upstream |
| [trs_so_arm100](trs_so_arm100.md) | pinned / high | yes | {"needs a human look": 4, "unknown": 12} | Pitch range: Δ [3.32, 3.326]; 665.2× tolerance | M/H: kinematic convention differs; M/S: kinematic convention differs; 7 raw CoM differences excluded | complete |
| [ufactory_lite6](ufactory_lite6.md) | dated match / medium | yes | {"STALE": 6} | joint4 effort: Δ -30.635495; 95.7359219× tolerance | M/H: consistent; M/S: consistent; 0 raw CoM differences excluded | partial history |
| [ufactory_xarm7](ufactory_xarm7.md) | dated match / medium | yes | {"STALE": 7} | joint1 effort: Δ 113.2; 69.3627451× tolerance | M/H: consistent; M/S: consistent; 0 raw CoM differences excluded | partial history |
| [umi_gripper](umi_gripper.md) | unknown / unknown | unknown | {} | unavailable / no discrepancy | unavailable | unknown upstream |
| [unitree_a1](unitree_a1.md) | none / none | yes | {"NO MATCHING SOURCE": 28} | FR_calf mass: Δ -0.06; 53.0973451× tolerance | M/H: consistent; 0 raw CoM differences excluded | complete |
| [unitree_g1](unitree_g1.md) | dated match / medium | no | {} | unavailable / no discrepancy | M/H: consistent; M/S: consistent; 0 raw CoM differences excluded | complete |
| [unitree_go1](unitree_go1.md) | none / none | yes | {"NO MATCHING SOURCE": 39} | FR_calf mass: Δ -0.06; 60× tolerance | M/H: consistent; 0 raw CoM differences excluded | complete |
| [unitree_go2](unitree_go2.md) | none / none | yes | {"NO MATCHING SOURCE": 23} | FL_calf mass: Δ -0.087352; 72.3855613× tolerance | M/H: consistent; 0 raw CoM differences excluded | complete |
| [unitree_h1](unitree_h1.md) | none / none | yes | {"NO MATCHING SOURCE": 67} | left_hip_pitch range: Δ [-1.57, 0.96]; 314× tolerance | M/H: consistent; 0 raw CoM differences excluded | complete |
| [unitree_z1](unitree_z1.md) | dated match / medium | no | {} | unavailable / no discrepancy | M/H: consistent; M/S: consistent; 0 raw CoM differences excluded | partial history |
| [universal_robots_ur10e](universal_robots_ur10e.md) | unknown / incomplete | yes | {"unknown": 25} | base mass: Δ -4; 200× tolerance | M/H: kinematic convention differs; 7 raw CoM differences excluded | partial history |
| [universal_robots_ur5e](universal_robots_ur5e.md) | unknown / incomplete | yes | {"unknown": 22} | base mass: Δ -4; 200× tolerance | M/H: kinematic convention differs; 7 raw CoM differences excluded | partial history |
| [wonik_allegro](wonik_allegro.md) | unknown / incomplete | yes | {"unknown": 4} | palm principal_moments: Δ [0.000146422845, 0.000225831213, 0.000347331911]; 43.6643272× tolerance | M/H: insufficient kinematic coverage; 2 raw CoM differences excluded | partial history |

## Counts

```json
{
  "NO MATCHING SOURCE": 324,
  "undocumented derivation difference": 82,
  "unknown": 157,
  "STALE": 20,
  "needs a human look": 4
}
```

Models listed: 71. Machine-readable detailed results: `report/results.json`.

Eligible CoM values use a best-fit proper rigid alignment of matched body origins at zero pose. A maximum per-origin residual exceeding the configured 5 mm default, or a matched signed axis disagreement above the 0.005 rad default, is marked kinematic convention differs. RMS residual is also recorded. Underdetermined fits are marked insufficient kinematic coverage. Both exclude CoM from counts and largest discrepancies; raw coordinates and transforms remain available. Joint effort/velocity declarations from URDF are metadata: MuJoCo does not enforce those tags. MJCF force/effort values are reported only for supported direct scalar actuators. Missing limits are coverage gaps, never zero limits.

## Tolerance sensitivity

Physical relative and absolute thresholds are multiplied together. The configurable kinematic quality thresholds remain fixed. Matching and provenance are reselected at each scale; counts exclude gated CoM records and apply only to models with a compiled comparison.

| Scale | Models evaluated | Changed quantity classifications | Findings added/removed | Total finding records |
|---|---:|---:|---:|---:|
| 0.5 | 47 | 7 | 16 | 603 |
| 2 | 47 | 4 | 19 | 568 |
