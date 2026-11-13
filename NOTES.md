# Work log

## 2026-11-13 — setup and acceptance gate

- Scope: work stayed inside this repository; another job was running on this machine, so work was isolated from it. No GPU/MLX; at most two worker processes; heavy commands use `nice -n 15`.
- Network is restricted to git clone/fetch from GitHub for Menagerie and its upstream sources, and pip installs from PyPI. No issues, comments, PRs, pushes, commits, or messages will be sent.
- Initial disk check: `df -h .` completed. Workspace was empty. Workspace disk budget: less than 15 GB, including ignored caches and environment.
- Initial inventory command ended with exit status 1 because `rg --files -g AGENTS.md` found no files in the empty workspace. The disk and directory checks succeeded.
- Acceptance gate: reproduce H1 at Menagerie `370c439` before attempting the survey; stop and explain if a serious attempt cannot reproduce it. Initial expected values are hypotheses, not findings.
- `git init` failed with `Operation not permitted` on `.git` under the workspace sandbox. Retrying with the permission needed for the project initialization. No repository was initialized by that failed command; its later chained directory creation did not run.
- Retried `git init` with sandbox escalation: succeeded. No commit created.
- Interpreter discovery using `command -v -a` failed under zsh (`command not found: -v`); switching to direct path inspection. Python 3.11 is used for this project.

## Network commands

Network commands are recorded here before execution, with outcomes added afterward.

1. `nice -n 15 git clone --filter=blob:none --no-checkout https://github.com/google-deepmind/mujoco_menagerie.git .cache/menagerie` — inspect H1 at the fixed revision and its local history, without fetching meshes into a working tree.
   - Failed: sandbox denied `setpriority`, and DNS resolution for github.com failed. Retrying the same command with sandbox escalation; no upstream data was retrieved by the failed attempt.
2. `nice -n 15 git clone --filter=blob:none --no-checkout https://github.com/google-deepmind/mujoco_menagerie.git .cache/menagerie` (escalated) — same purpose.
   - Succeeded. HEAD is the fixed `370c43965323c0944b433b202aac5058b5f907a9`; H1 has no later fix at this fetched HEAD. Clone size initially 740 KiB.
3. `nice -n 15 .venv/bin/python -m pip install --index-url https://pypi.org/simple --no-cache-dir -r requirements.txt` — install pinned CPU-only compilation, XML expansion, YAML, and test dependencies from PyPI. Python 3.11 selected from `python3.11`.
   - Succeeded with MuJoCo 3.3.7 and the pinned direct dependencies. Full resolved versions will be recorded locally.
4. `nice -n 15 git -C .cache/menagerie fetch --no-tags origin f31557b6354d7961867d68628035097fd218a9cf 5e50a3b59e8b488d32aece5e815c0a00d3b048c9 42b8402e4085a81bf4da151418ad56e47b467ea6` — explicitly fetch only H1 README, CHANGELOG and MJCF blobs. All other Git reads use `GIT_NO_LAZY_FETCH=1` to prevent unlogged network fetches.
   - Failed: `fatal: bad revision` / server did not send all necessary objects. Switching to a size-filtered fetch of the advertised branch.
5. `nice -n 15 git -C .cache/menagerie fetch --no-tags --refetch --filter=blob:limit=100k origin main` — retrieve small text blobs and history while excluding large meshes and images.
   - Succeeded. H1 README says the URDF was provided directly by Unitree and names no GitHub source commit; its derivation describes conversion/default extraction/added actuators but no mass or range edits. The `unitree_ros` source lead will be tested against history, not assumed to be the original source.
6. `nice -n 15 git clone --filter=blob:limit=100k --no-checkout https://github.com/unitreerobotics/unitree_ros.git .cache/unitree_ros` — inspect the upstream named in the task, all H1 source revisions, and the cited `34e7506` update, without a model working tree.
   - Succeeded. Upstream HEAD: `157ff950351e5f535e03c5d85a16b7d594b3dbcc`. Found source `robots/h1_description/urdf/h1.urdf`. Cited update exists with date 2025-12-31.
   - XML-only diagnostic confirms explicit-inertial sums of 51.437 kg (Menagerie) and 59.338 kg (upstream HEAD). These are not yet compiled findings. Original Menagerie H1 (2023-11-06) has the same 51.437 kg. Earliest H1 URDF on upstream history is dated 2023-12-07, later than the conversion; this may prevent a valid historical S.
   - A diagnostic stopped when `git show -s` attempted to access an omitted mesh blob; lazy fetching was disabled, so no network access occurred. Source XML reads succeeded. `git log --follow` similarly failed on an omitted blob; switched to metadata-only full-history inspection. A logo mesh size probe failed because that blob was filtered out.
   - Upstream has bodies without explicit inertials (IMU, logo, and later sensor links). Geometry stripping is therefore not allowed by the explicit-inertial rule. Fetching mesh-sized blobs to compile without stripping upstream geometry.
7. `nice -n 15 git -C .cache/unitree_ros fetch --no-tags --refetch --filter=blob:limit=5m origin master` — fetch manufacturer mesh blobs needed for the strict H1 compilation; remain well below the 15 GB budget.
   - Succeeded. No working-tree model files were created. A second history search with rename detection attempted an omitted DAE blob and failed offline; using `--no-renames` for metadata-only history. All fetched refs include `origin/master` and `origin/update_h1_model`.

## Acceptance diagnostic implementation

- Implemented an offline diagnostic reading Git objects into process memory; no upstream model files enter tracked project files. It compiles with MuJoCo 3.3.7 and `fusestatic=false`.
- Menagerie geometry is stripped only after verifying every body has an explicit inertial. Upstream geometry is retained and package meshes are loaded from the same source commit.
- Tolerances before classification: mass max(0.5% of the larger magnitude, 0.001 kg); world CoM Euclidean distance 0.0005 m; principal moments 1%; ranges 0.005 rad; limits 1%. Scale applies to both relative and absolute thresholds. Missing S is `unknown`, never STALE.
- Strict provenance cutoff is the original Menagerie conversion, rather than an unrelated later formatting, lighting, or collision geometry edit. All upstream file-touching revisions across fetched branches are enumerated and dated.
- `nice -n 15 env OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 PYTHONPATH=src .venv/bin/python -m drift.gate` completed with deliberate exit status 2 (acceptance blocked). Compiled M=51.437 kg and H=59.33801256637062 kg. Both leg subtree differences are 3.387 kg. Both hip-pitch ranges are M=[-1.57, 1.57], H=[-3.14, 2.53] rad. Upstream loaded all 21 meshes; geometry was not stripped.
- The 0.00001256637062 kg difference between the upstream explicit-inertial XML sum and compiled mass comes from three small sensor collision spheres without inertials (each inferred mass 0.000004188790204786391 kg). This is why XML sums are not substituted for compiled totals.
- Enumerated nine upstream H1 source-file revisions across both fetched branches. All postdate original Menagerie conversion `56c951b6e8ba8cd6a330ee42403874dbc2d546c9` (2023-11-06). Earliest is `e197ae10d301c41f17f61fe3a741925a033db1e8` (2023-12-07). `origin/update_h1_model` points to `1a3e648...` (2024-01-19), so it adds no earlier candidate.
- Read the original Menagerie README too: it also says Unitree supplied the original URDF directly and has no pinned source commit. A metadata search for any H1 path before 2023-11-07 returned no commits in the fetched upstream refs. Only Git transport was used; no vendor websites, issue pages, or GitHub API endpoints were accessed.
- **The acceptance gate stopped the survey.** S is unknown; mass or range mismatches alone cannot satisfy the stipulated three-way STALE acceptance. No later edit to unrelated formatting, lighting, or colliders was used to move the conversion cutoff forward.
- Preserved a small offline CLI, configurable comparison primitives, synthetic tests, raw compiled snapshots and a failure report. `./drift report` returns 2 deliberately for the blocked gate. There is no claim that the full CLI or survey is implemented.
- Verification: `nice -n 15 env OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 .venv/bin/python -m pytest -q` — **14 passed in 1.37s**, including real H1 regression assertions that retain `unknown` when provenance is unavailable. This is not a passed H1 STALE acceptance test. No all-model self-check or random survey recheck was run.
- `pip freeze` emitted a cache-permission warning; it read installed versions successfully and made no network request. All resolved library versions were then pinned in `requirements.txt`.
- Workspace size after mesh fetch: 411 MiB, including 128 MiB environment and 260 MiB manufacturer clone. No external directories or other jobs were touched.
- Final artifact inventory succeeded (`git status --short`, `du`, `df`, line counts). A URL scan also named the uncreated `.github` directory and therefore returned status 2; this was an inventory-command error, not a model or test failure. No workflow was created after the acceptance gate failed. Workspace remained 411 MiB.
- Saved `report/unitree_h1.md` with commit-pinned source-line links for every contributing body mass and both hip-pitch ranges, the nine chronological source candidates, compilation details and the explicit stop reason. `report/summary.md` states that other models were not surveyed. The external publication draft is marked HOLD and does not falsely assert completed human verification or a published repository URL.
- Final `nice -n 15 ./drift check unitree_h1` reproduced the same compiled totals and saved the blocked result, exiting 2 as designed. Read back the evidence report and checked Git status: all project artifacts are untracked; nothing is staged or committed. `git diff --check` returned 0 but does not validate untracked file contents.

## 2026-11-13 — resumed with amended provenance

- The survey resumed with the amended methods: pinned, dated match, proxy, none. Proxy classes must say `(inferred)`; no match is `NO MATCHING SOURCE`, never STALE. H1 acceptance now requires reproduced numbers, correct classification under these rules, nine-revision discrepancy table and the direct-provision README quote.
- Resume disk check completed; workspace 411 MiB. The inventory's final `rg` returned 1 because no AGENTS.md was found, not because earlier checks failed.
- Proxy selection will require every comparable compiled physical quantity to match, not just a total mass that can hide offsetting body differences. Unavailable fields and unmatched bodies will be disclosed. The H1 table will independently display total, both leg subtrees and both hip-pitch endpoint differences for all nine revisions.
- First amended nine-revision compile: four revisions compiled and did not match; five failed resolving historical `left_elbow_link.dae`. The missing asset failures are recorded, not treated as proof of no match. Investigating historical asset paths before acceptance can pass.
- Network command: `nice -n 15 .venv/bin/python -m pip install --index-url https://pypi.org/simple --no-cache-dir -r requirements.txt` — add pinned trimesh/pycollada/lxml to convert COLLADA geometry in memory for MuJoCo (which does not load DAE directly). Geometry will not be stripped from bodies lacking inertials.


- Network command `git -C .cache/unitree_ros fetch --no-tags --refetch --filter=blob:limit=20m origin master` — retrieve omitted source/mesh blobs below 20m for CPU compilation. Parent process runs at nice 15; lazy fetching disabled.

- Network outcome: exit 0. From https://github.com/unitreerobotics/unitree_ros
 * branch            master     -> FETCH_HEAD
- PyPI mesh-conversion install succeeded. Pinned the resolved new transitive versions `python-dateutil==4.0.0` and `tzdata==2026.6` as well.
- All nine H1 revisions now compile, including DAE-to-OBJ conversion in memory with retained scene transforms. None matches. Amended acceptance passed: M=51.437 kg; H=59.338012566 kg; class `NO MATCHING SOURCE`. Earliest/closest public ankle masses differ from Menagerie's 0.446 kg, despite some total masses being within the total-mass tolerance.
- Updated `report/unitree_h1.md` with every M/H quantity discrepancy, nine compiled-revision table (total, both leg subtrees and both hip-pitch ranges), source permalinks and the README direct-provision quote.
- Amended tests: 19 passed in 24.64s. Mesh conversion emitted a trimesh deprecation warning 105 times; replaced the deprecated scene concatenation call with `to_geometry()` before continuing.
- Survey implementation fixes in progress: stripping textures left dangling material references in Cassie/ANYmal; remove the texture attribute when stripping. XML actuator/keyframe fragments are inventoried separately instead of compiled as standalone robots. A combined patch to replace `cli.py` was rejected because it contained both delete and add operations for the same path; applying the replacement as a file update instead.

- Offline Git read failed (exit 128): `('show', 'd9415a3076f921fdb9735d45d609a596df722468:apptronik_apollo/CHANGELOG.md')` in `menagerie`. fatal: bad object d9415a3076f921fdb9735d45d609a596df722468:apptronik_apollo/CHANGELOG.md

- Offline Git read failed (exit 128): `('show', 'd9415a3076f921fdb9735d45d609a596df722468:berkeley_humanoid/CHANGELOG.md')` in `menagerie`. fatal: bad object d9415a3076f921fdb9735d45d609a596df722468:berkeley_humanoid/CHANGELOG.md

- Offline Git read failed (exit 128): `('show', 'd9415a3076f921fdb9735d45d609a596df722468:booster_t1/CHANGELOG.md')` in `menagerie`. fatal: bad object d9415a3076f921fdb9735d45d609a596df722468:booster_t1/CHANGELOG.md

- Offline Git read failed (exit 128): `('show', 'd9415a3076f921fdb9735d45d609a596df722468:fourier_n1/CHANGELOG.md')` in `menagerie`. fatal: bad object d9415a3076f921fdb9735d45d609a596df722468:fourier_n1/CHANGELOG.md

- Offline Git read failed (exit 128): `('show', 'fae9ee82330444eec4e87568c838b99a09a39467:rainbow_robotics_rby1/README.md')` in `menagerie`. fatal: path 'rainbow_robotics_rby1/README.md' does not exist in 'fae9ee82330444eec4e87568c838b99a09a39467'

- Offline Git read failed (exit 128): `('show', 'd9415a3076f921fdb9735d45d609a596df722468:unitree_g1/CHANGELOG.md')` in `menagerie`. fatal: bad object d9415a3076f921fdb9735d45d609a596df722468:unitree_g1/CHANGELOG.md

- Network command `git clone --filter=blob:limit=100k --no-checkout https://github.com/agilexrobotics/Piper_ros.git .cache/agilexrobotics__Piper_ros` — retrieve manufacturer source history and small text files. Parent process runs at nice 15; lazy fetching disabled.

- Network outcome: exit 0. Cloning into '.cache/agilexrobotics__Piper_ros'...

- Offline Git read failed (exit 128): `('show', 'ac41fcbcdda598f01b51cf6175ed9a24d0dacadc:src/piper_description/meshes/base_link.STL')` in `agilexrobotics__Piper_ros`. fatal: bad object ac41fcbcdda598f01b51cf6175ed9a24d0dacadc:src/piper_description/meshes/base_link.STL

- Network command `git -C .cache/agilexrobotics__Piper_ros fetch --no-tags --refetch --filter=blob:limit=500k origin HEAD` — retrieve omitted source/mesh blobs below 500k for CPU compilation. Parent process runs at nice 15; lazy fetching disabled.

- Network outcome: exit 0. From https://github.com/agilexrobotics/Piper_ros
 * branch            HEAD       -> FETCH_HEAD

- Offline Git read failed (exit 128): `('show', 'ac41fcbcdda598f01b51cf6175ed9a24d0dacadc:src/piper_description/meshes/base_link.STL')` in `agilexrobotics__Piper_ros`. fatal: bad object ac41fcbcdda598f01b51cf6175ed9a24d0dacadc:src/piper_description/meshes/base_link.STL

- Network command `git -C .cache/agilexrobotics__Piper_ros fetch --no-tags --refetch --filter=blob:limit=5m origin HEAD` — retrieve omitted source/mesh blobs below 5m for CPU compilation. Parent process runs at nice 15; lazy fetching disabled.

- Network outcome: exit 0. From https://github.com/agilexrobotics/Piper_ros
 * branch            HEAD       -> FETCH_HEAD

- https://github.com/agilexrobotics/Piper_ros src/piper_description/urdf/piper_description_v100_camera.urdf at ac41fcbcdda598f01b51cf6175ed9a24d0dacadc: ValueError: $(find piper_camera_moveit_config) is outside the cloned repository

- https://github.com/agilexrobotics/Piper_ros src/piper_description/urdf/piper_description_with_camera.xacro at ac41fcbcdda598f01b51cf6175ed9a24d0dacadc: ValueError: $(find piper_camera_moveit_config) is outside the cloned repository

- Menagerie self-comparison compile failed: agility_cassie/cassie.xml: ValueError: Error: texture 'cassie' not found in material 0
Element name 'cassie', id 0, line 21

- Menagerie self-comparison compile failed: aloha/filtered_cartesian_actuators.xml: ValueError: Error: transmission target 'left/gripper' not found in actuator 0
Element name 'left/X', id 0, line 36

- Menagerie self-comparison compile failed: aloha/joint_position_actuators.xml: ValueError: XML Error: unknown default class name 'waist'
Element 'position', line 3


- Menagerie self-comparison compile failed: aloha/keyframe_ctrl.xml: ValueError: Error: keyframe 'neutral_pose': invalid qpos size, expected 0, got 16
Element name 'neutral_pose', id 0

- Menagerie self-comparison compile failed: aloha/keyframe_no_act.xml: ValueError: Error: keyframe 'neutral_pose': invalid qpos size, expected 0, got 16
Element name 'neutral_pose', id 0

- Menagerie self-comparison compile failed: anybotics_anymal_b/anymal_b.xml: ValueError: Error: texture 'base_uv_texture' not found in material 4
Element name 'carbon_fibre_logo', id 4, line 58

- Menagerie self-comparison compile failed: anybotics_anymal_c/anymal_c.xml: ValueError: Error: texture 'base' not found in material 5
Element name 'base', id 5, line 32

- Menagerie self-comparison compile failed: anybotics_anymal_c/anymal_c_mjx.xml: ValueError: Error: texture 'base' not found in material 5
Element name 'base', id 5, line 32

- Offline Git read failed (exit 128): `('show', '370c43965323c0944b433b202aac5058b5f907a9:apptronik_apollo/assets/neck_mount_fix_link.stl')` in `menagerie`. fatal: bad object 370c43965323c0944b433b202aac5058b5f907a9:apptronik_apollo/assets/neck_mount_fix_link.stl

- Network command `git -C .cache/menagerie fetch --no-tags --refetch --filter=blob:limit=500k origin HEAD` — retrieve omitted source/mesh blobs below 500k for CPU compilation. Parent process runs at nice 15; lazy fetching disabled.

- Network outcome: exit 0. From https://github.com/google-deepmind/mujoco_menagerie
 * branch              HEAD       -> FETCH_HEAD

- Offline Git read failed (exit 128): `('show', '370c43965323c0944b433b202aac5058b5f907a9:apptronik_apollo/assets/neck_mount_fix_link.stl')` in `menagerie`. fatal: bad object 370c43965323c0944b433b202aac5058b5f907a9:apptronik_apollo/assets/neck_mount_fix_link.stl

- Network command `git -C .cache/menagerie fetch --no-tags --refetch --filter=blob:limit=5m origin HEAD` — retrieve omitted source/mesh blobs below 5m for CPU compilation. Parent process runs at nice 15; lazy fetching disabled.

- Network outcome: exit 0. From https://github.com/google-deepmind/mujoco_menagerie
 * branch              HEAD       -> FETCH_HEAD

- Offline Git read failed (exit 128): `('show', '370c43965323c0944b433b202aac5058b5f907a9:apptronik_apollo/assets/torso_link.stl')` in `menagerie`. fatal: bad object 370c43965323c0944b433b202aac5058b5f907a9:apptronik_apollo/assets/torso_link.stl

- Network command `git -C .cache/menagerie fetch --no-tags --refetch --filter=blob:limit=20m origin HEAD` — retrieve omitted source/mesh blobs below 20m for CPU compilation. Parent process runs at nice 15; lazy fetching disabled.

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/menagerie -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `f31557b6354d7961867d68628035097fd218a9cf`

- Network outcome: exit 0.
- Verified all five apparent README source pins in context (ARX L5, flybody, SO101, SHARPA Wave, SO-ARM100); this differs from the initial background count of two. These are observed source-SHA links, not an assumed survey result.
- Added the weekly workflow locally with read-only repository permissions, serialized runs, CPU thread caps, fixed H1 acceptance before the rest of the survey, and report artifacts. It is not pushed or executed here.
- Additional regression tests: 24 passed in 24.85s, including self-comparison, unique-tree renaming, proxy suffixes, no-match deltas and texture stripping. The first survey process still uses its earlier loader; affected entries will be rerun with these fixes.
- A direct shell read of Spot's old linked file failed because `spot_description` is now a submodule. Inspection of `.gitmodules` and README identified its GitHub source repository; the resolver will follow that source submodule explicitly, with a separately logged clone, rather than assume the old file was deleted. A subsequent `rg` in the BAM tree returned 1 because no URDF/XML files were present there.
- Fixed another loader defect: replacing a mesh filename changed MuJoCo's implicit mesh name. The original filename-derived mesh name is now preserved. This affected Apollo and Flexiv self-checks in the first process and will be rechecked.
- A sandboxed `ps` call to identify only this survey process failed (`operation not permitted`). Retrying that read with escalation so the outdated first process can be stopped and resumed with the loader/targeted-fetch fixes; no other job is a target.
- The escalated first process filter returned no match because the executable name resolved differently. A broader exact-task filter identified the survey process group. Group inspection showed only this survey and its own Git children. Interrupted that verified group with SIGINT to load the tested fixes; any in-flight Git command was canceled, not counted as a completed fetch. No other process group was signaled.
- Targeted promisor fetching succeeded on genuinely missing ANYmal and fly model resources; commands and exact object IDs are logged above. This avoids whole-repository mesh-history fetches.
- Latest regression suite: 27 passed in 23.83s. New checks cover xacro local-package resolution and optional unused dependencies, assetdir and filename-derived mesh names.
- Found the fly repository's intermediate build XMLs were being tested alongside its published model. Source discovery now prefers the same model filename as Menagerie when a README gives only a repository/directory, reducing irrelevant build-model downloads. Restarting that in-progress model from saved checkpoints to apply this scope fix. Google/Stretch assetdir and xacro optional-package fixes will also be rechecked.
- Second restart verified and interrupted only survey group 99392 (one process at that instant), then resumed at the unfinished fly model. Flybody completed with pinned provenance and zero findings. Source deletions encountered in Fourier history are being represented as absent values rather than failed numeric compilations.
- Added detection of plain-text source SHAs, not only SHA-bearing URLs. SO101's README contains a different SHA in its “Copied” derivation step than in its overview link; both must be recorded and inspected rather than silently assuming the URL is the only pin.
- Added exact-content rename following with per-revision file paths, avoiding heuristic rename scans that fetch unrelated meshes. Modified-content renames may still require manual source-path review; this limitation will be explicit.
- Added a 0.0005 m prismatic-range tolerance separately from the 0.005 rad hinge tolerance; both are configurable. Overall tolerance sensitivity reselects provenance at half and double the base thresholds.
- Independent XML cross-check code now supports mass/subtrees, FK/world CoM, sorted tensor eigenvalues, ranges and supported limits. It imports no MuJoCo. Sampling shuffles all finding records, with any non-extractable draw disclosed before selecting three.
- MuJoCo emitted repeated duplicate visual-geom-name warnings during Franka compilation; these do not indicate physical quantity failures. Future compiles capture and log warning counts instead of flooding terminal output.
- Fixed acceptance now explicitly pins both fixed reference revisions (`370c439` and `34e7506`) and only their reachable source history. This keeps the nine-revision regression stable for weekly runs. The full survey still reads each current upstream HEAD independently; no expected mass is embedded in the comparison engine.
- Unit/synthetic/loader/direct-parser/history tests after these additions: 29 passed, one integration test deselected (0.16s). Final full integration verification remains scheduled after the survey/repair pass.
- Source audit found Seeed's repository also vendors a Menagerie MJCF (its git history explicitly says so). The README says the conversion came from URDF. Verified the original RS URDF independently: at `6a18bea` it exactly matches all compared M quantities; current HEAD has the same seven physical differences observed through MJCF. Source discovery now gives the README-declared source format priority and tests small repositories' URDF variants even if their filenames lack the marketing model name. The final Seeed report will cite the manufacturer URDF, avoiding circular provenance.
- The first Seeed probe selected no files because none had `devarm` in their URDF path; the corrected probe tested all three URDF variants. Two alternative files did not exist at the historical commit (plain logged Git read failures), while `urdf/00-arm-rs_asm-v3/urdf/00-arm-rs_asm-v3.urdf` existed and matched.
- Latest non-integration tests: 31 passed, one integration test deselected (0.17s), including a physical camera matched through extra zero-mass fixed sensor frames.
- The serial first full survey completed all 71 models. A later poll of its already-closed process ID returned `Unknown process id`; the process had already finished normally. Proceeding with targeted rechecks for the identified implementation/source-selection fixes.
- A patch for history dependency fetching was rejected because it repeated a file update section; no changes from that rejected patch were applied. Consolidating the sections before retrying.
- Source audit caught two important false candidates: empty Gazebo/material extension files could compile without a robot, and a removed A1 directory allowed A2 to be chosen from the same repository. Reject zero-body/zero-mass source fragments and preserve the model-specific path scope. Preliminary affected numbers are superseded and must not be used as findings.
- ANYmal C's overview names the C repository, but its derivation hyperlink points to B. The C URDF fails MuJoCo's inertia triangle check. Reject the explicitly conflicting B-variant repository rather than substitute a different robot when C compilation fails; report that coverage gap.
- A shell read of `unitree_mujoco/README.md` failed because its actual filename is `readme.md`; read the lowercase file afterward. Its current tree has no A1 model. The resolver may use exact model filenames in already-cloned repositories selected from the same manufacturer, recording that fallback explicitly.
- The first targeted repair pass successfully compiled every MS Human variant; source compilation still needed nested include paths resolved against the root model as well as the including file. Added that internal-repository path handling. A RealSense/Seeed rename-history query requested omitted objects even with exact renames; explicit logged object fetches are now supported for those metadata dependencies.
- Found the ALOHA Cartesian actuator fragment has a `<worldbody>` with only sites, so the earlier no-worldbody test was insufficient. It is now excluded as an actuator include fragment; the complete ALOHA robot remains self-checked.
- Source links now resolve actual declaration lines, inherited defaults and available YAML numeric input locations. Every body mass is included in a mass-accounting table, including unchanged and unmatched bodies, so aggregate totals/subtrees can be checked.
- All 71 models now have successful standalone self-comparisons and zero findings. Include fragments are listed separately and tested through their parent models.
- The second repair pass verified MS Human against upstream after internal include resolution, but Seeed rename traversal exceeded the prior 30-object cap. Added an explicitly labeled current-path-history fallback. Incomplete rename traversal cannot justify proxy or definitive no-match provenance; an observed dated matching source remains usable with a partial-history status. This prevents unrelated mesh-renaming metadata from blocking all numerical checks.
- Pinned source paths are now resolved at the pinned revision independently of their current filenames; this fixes moved-file pins such as SO-ARM100. Failed pinned compilation retains the pin with incomplete numeric coverage rather than silently downgrading to another source method.
- Added reviewed xacro entry-point/argument recipes for the two UFactory arms and the Shadow right hand. These select standalone manufacturer wrappers instead of component macro files. They contain no physical numbers or expected findings; all compiled quantities and source-history matching remain automatic.
- Go2's published URDF has multiple material tags under one visual, which MuJoCo rejects. Added a recorded, nonphysical normalization retaining the first material while preserving every geometry, inertial and joint. Missing inertials still forbid geometry stripping. Also handle local `file://` mesh references inside the cloned repository.
- Final non-integration regression run before documentation: 37 passed, one integration test deselected (0.29s). Added checks for macro-only sensor construction, private-property alpha-renaming, extension-fragment rejection and source-reference identity.
- Geometry stripping now additionally refuses compiler-forced `inertiafromgeom=true`, even if inertials are present. Ball-joint cone ranges are retained; free-base placement is registered separately and never treated as a finite joint limit.
- Final provenance audit of all folder commit-message bodies found one additional upstream source reference: Shadow hand commit `bda959328b7934176123af0cc0491c34ecaa23ce`. Commit-message evidence is recorded separately from README pins.
- Expanded history enumeration to the actual include/xacro/YAML/resource dependency graph, with closure across historical versions. This prevents a wrapper file's unchanged timestamp from hiding manufacturer inertia/limit updates in included files. Identical complete compiler inputs (XML plus geometry bytes) are memoized, without supplying or approximating any values.
- During this audit, found the snapshot return structure overwrote recorded xacro arguments with `{}` after compilation. Corrected it; the actual construction arguments had been used, so physical values were unaffected. Re-expanding the affected dependency histories will also regenerate accurate argument metadata before cross-checking and publication.
- A sandbox-only priority probe (`nice -n 15 true`) printed `setpriority: Operation not permitted`; it performed no heavy work. Heavy compilation/network/test commands continue to use escalation and nice 15.
- Dependency closure includes retained geometry bytes as well as xacro/YAML/include files; changed wrapper-only commits are no longer the sole source candidates. Current progress and native compiler warnings are captured in `.cache/dependency-survey.log`.
- Corrected an overly broad variant guard that temporarily rejected Crazyflie's generic `_ros` repository suffix. Variant checks now only compare similarly short actual variant tokens; Crazyflie will be restored in the final recheck.
- Verified FANUC's plain-text source pin in its README: tag v2.3.0 / `fb40c9803a826ba68c7c8e28ba904a25efa7fcd2`. Source-pin auditing includes both SHA-bearing links and plain text, so the initial background count is not assumed.
- Fixed weekly rerun semantics: a full `check all` starts a fresh result set instead of skipping models from the published JSON. The workflow reruns all current folders and validates their self-comparisons afterward. The self-comparison test derives the expected folder set from the current inventory, allowing new models without a hard-coded count.
- Disable background Git maintenance during network acquisition, cap Git pack/index threads at one, and keep the scanner serial. Python/BLAS thread caps remain one.
- A local scan of the installed COLLADA reader modules found no urllib/requests/urlopen/http calls; `rg` returned 1 because there were no matches. This scan made no network request.
- The current dataset contains no case where only post-Menagerie revisions match despite older public nonmatching revisions. That scenario is outside the four specified source-selection cases; the generic selector conservatively returns unknown rather than falsely claim that no public matching values exist or apply an unauthorized proxy.

- Network outcome: exit 0. From https://github.com/google-deepmind/mujoco_menagerie
 * branch              HEAD       -> FETCH_HEAD

- Menagerie self-comparison compile failed: apptronik_apollo/apptronik_apollo.xml: ValueError: Error: mesh 'pelvis_link' not found in geom 0
Element name '', id 0, line 87

- Network command `git clone --filter=blob:limit=100k --no-checkout https://github.com/ARXroboticsX/ARX_Model.git .cache/ARXroboticsX__ARX_Model` — retrieve manufacturer source history and small text files. Parent process runs at nice 15; lazy fetching disabled.

- Network outcome: exit 0. Cloning into '.cache/ARXroboticsX__ARX_Model'...

- Network command `git clone --filter=blob:limit=100k --no-checkout https://github.com/HybridRobotics/berkeley_humanoid_description.git .cache/HybridRobotics__berkeley_humanoid_description` — retrieve manufacturer source history and small text files. Parent process runs at nice 15; lazy fetching disabled.

- Network outcome: exit 0. Cloning into '.cache/HybridRobotics__berkeley_humanoid_description'...

- Network command `git clone --filter=blob:limit=100k --no-checkout https://github.com/HybridRobotics/isaac_berkeley_humanoid.git .cache/HybridRobotics__isaac_berkeley_humanoid` — retrieve manufacturer source history and small text files. Parent process runs at nice 15; lazy fetching disabled.

- Network outcome: exit 0. Cloning into '.cache/HybridRobotics__isaac_berkeley_humanoid'...

- Offline Git read failed (exit 128): `('show', 'd9415a3076f921fdb9735d45d609a596df722468:berkeley_humanoid/berkeley_humanoid.xml')` in `menagerie`. fatal: bad object d9415a3076f921fdb9735d45d609a596df722468:berkeley_humanoid/berkeley_humanoid.xml

- Historical Menagerie compile failed berkeley_humanoid d9415a3076f921fdb9735d45d609a596df722468: Command '['git', '-C', '.cache/menagerie', 'show', 'd9415a3076f921fdb9735d45d609a596df722468:berkeley_humanoid/berkeley_humanoid.xml']' returned non-zero exit status 128.

- Network command `git clone --filter=blob:limit=100k --no-checkout https://github.com/whoenig/crazyflie_ros.git .cache/whoenig__crazyflie_ros` — retrieve manufacturer source history and small text files. Parent process runs at nice 15; lazy fetching disabled.

- Network outcome: exit 0. Cloning into '.cache/whoenig__crazyflie_ros'...

- Network command `git clone --filter=blob:limit=100k --no-checkout https://github.com/BoosterRobotics/booster_gym.git .cache/BoosterRobotics__booster_gym` — retrieve manufacturer source history and small text files. Parent process runs at nice 15; lazy fetching disabled.

- Network outcome: exit 0. Cloning into '.cache/BoosterRobotics__booster_gym'...

- Offline Git read failed (exit 128): `('show', 'd9415a3076f921fdb9735d45d609a596df722468:booster_t1/t1.xml')` in `menagerie`. fatal: bad object d9415a3076f921fdb9735d45d609a596df722468:booster_t1/t1.xml

- Historical Menagerie compile failed booster_t1 d9415a3076f921fdb9735d45d609a596df722468: Command '['git', '-C', '.cache/menagerie', 'show', 'd9415a3076f921fdb9735d45d609a596df722468:booster_t1/t1.xml']' returned non-zero exit status 128.

- Network command `git clone --filter=blob:limit=100k --no-checkout https://github.com/bdaiinstitute/spot_ros2.git .cache/bdaiinstitute__spot_ros2` — retrieve manufacturer source history and small text files. Parent process runs at nice 15; lazy fetching disabled.

- Network outcome: exit 0. Cloning into '.cache/bdaiinstitute__spot_ros2'...

- Network command `git clone --filter=blob:limit=100k --no-checkout https://github.com/rhoban/bam.git .cache/rhoban__bam` — retrieve manufacturer source history and small text files. Parent process runs at nice 15; lazy fetching disabled.

- Network outcome: exit 0. Cloning into '.cache/rhoban__bam'...

- Network command `git clone --filter=blob:limit=100k --no-checkout https://github.com/FANUC-CORPORATION/fanuc_description.git .cache/FANUC-CORPORATION__fanuc_description` — retrieve manufacturer source history and small text files. Parent process runs at nice 15; lazy fetching disabled.

- Network outcome: exit 0. Cloning into '.cache/FANUC-CORPORATION__fanuc_description'...

- Offline Git read failed (exit 128): `('show', 'fb40c9803a826ba68c7c8e28ba904a25efa7fcd2:fanuc_crx_description/meshes/crx5ia/visual/base.dae')` in `FANUC-CORPORATION__fanuc_description`. fatal: bad object fb40c9803a826ba68c7c8e28ba904a25efa7fcd2:fanuc_crx_description/meshes/crx5ia/visual/base.dae

- Network command `git -C .cache/FANUC-CORPORATION__fanuc_description fetch --no-tags --refetch --filter=blob:limit=500k origin HEAD` — retrieve omitted source/mesh blobs below 500k for CPU compilation. Parent process runs at nice 15; lazy fetching disabled.

- Network outcome: exit 0. From https://github.com/FANUC-CORPORATION/fanuc_description
 * branch            HEAD       -> FETCH_HEAD

- Offline Git read failed (exit 128): `('show', 'fb40c9803a826ba68c7c8e28ba904a25efa7fcd2:fanuc_crx_description/meshes/crx5ia/visual/base.dae')` in `FANUC-CORPORATION__fanuc_description`. fatal: bad object fb40c9803a826ba68c7c8e28ba904a25efa7fcd2:fanuc_crx_description/meshes/crx5ia/visual/base.dae

- Network command `git -C .cache/FANUC-CORPORATION__fanuc_description fetch --no-tags --refetch --filter=blob:limit=5m origin HEAD` — retrieve omitted source/mesh blobs below 5m for CPU compilation. Parent process runs at nice 15; lazy fetching disabled.

- Network outcome: exit 0. From https://github.com/FANUC-CORPORATION/fanuc_description
 * branch            HEAD       -> FETCH_HEAD

- Menagerie self-comparison compile failed: flexiv_rizon4/flexiv_rizon4.xml: ValueError: Error: mesh 'link0' not found in geom 0
Element name 'convex_mesh', id 0, line 44

- Menagerie self-comparison compile failed: flexiv_rizon4s/flexiv_rizon4s.xml: ValueError: Error: mesh 'link0' not found in geom 0
Element name 'convex_mesh', id 0, line 44

- Offline Git read failed (exit 128): `('show', '370c43965323c0944b433b202aac5058b5f907a9:flybody/assets/head_red.obj')` in `menagerie`. fatal: bad object 370c43965323c0944b433b202aac5058b5f907a9:flybody/assets/head_red.obj

- Menagerie self-comparison compile failed: flybody/fruitfly.xml: CalledProcessError: Command '['git', '-C', '.cache/menagerie', 'show', '370c43965323c0944b433b202aac5058b5f907a9:flybody/assets/head_red.obj']' returned non-zero exit status 128.

- Network command `git clone --filter=blob:limit=100k --no-checkout https://github.com/FFTAI/Wiki-GRx-Models.git .cache/FFTAI__Wiki-GRx-Models` — retrieve manufacturer source history and small text files. Parent process runs at nice 15; lazy fetching disabled.

- Network outcome: exit 0. Cloning into '.cache/FFTAI__Wiki-GRx-Models'...

- Offline Git read failed (exit 128): `('show', '7d96c758f048fe1bf92b3258864d94771ae0c093:GRX/GR1/gr1t1/meshes/gr1t1/base_link.STL')` in `FFTAI__Wiki-GRx-Models`. fatal: bad object 7d96c758f048fe1bf92b3258864d94771ae0c093:GRX/GR1/gr1t1/meshes/gr1t1/base_link.STL

- Network command `git -C .cache/FFTAI__Wiki-GRx-Models fetch --no-tags --refetch --filter=blob:limit=500k origin HEAD` — retrieve omitted source/mesh blobs below 500k for CPU compilation. Parent process runs at nice 15; lazy fetching disabled.

- Network outcome: exit 0. From https://github.com/FFTAI/Wiki-GRx-Models
 * branch            HEAD       -> FETCH_HEAD

- Offline Git read failed (exit 128): `('show', '7d96c758f048fe1bf92b3258864d94771ae0c093:GRX/GR1/gr1t1/meshes/gr1t1/base_link.STL')` in `FFTAI__Wiki-GRx-Models`. fatal: bad object 7d96c758f048fe1bf92b3258864d94771ae0c093:GRX/GR1/gr1t1/meshes/gr1t1/base_link.STL

- Network command `git -C .cache/FFTAI__Wiki-GRx-Models fetch --no-tags --refetch --filter=blob:limit=5m origin HEAD` — retrieve omitted source/mesh blobs below 5m for CPU compilation. Parent process runs at nice 15; lazy fetching disabled.

- Network outcome: exit 0. From https://github.com/FFTAI/Wiki-GRx-Models
 * branch            HEAD       -> FETCH_HEAD

- Network command `git clone --filter=blob:limit=100k --no-checkout https://github.com/FFTAI/wiki-grx-mjcf.git .cache/FFTAI__wiki-grx-mjcf` — retrieve manufacturer source history and small text files. Parent process runs at nice 15; lazy fetching disabled.

- Network outcome: exit 0. Cloning into '.cache/FFTAI__wiki-grx-mjcf'...

- Offline Git read failed (exit 128): `('show', 'd9415a3076f921fdb9735d45d609a596df722468:fourier_n1/n1.xml')` in `menagerie`. fatal: bad object d9415a3076f921fdb9735d45d609a596df722468:fourier_n1/n1.xml

- Historical Menagerie compile failed fourier_n1 d9415a3076f921fdb9735d45d609a596df722468: Command '['git', '-C', '.cache/menagerie', 'show', 'd9415a3076f921fdb9735d45d609a596df722468:fourier_n1/n1.xml']' returned non-zero exit status 128.

- Offline Git read failed (exit 128): `('show', '11da5a77d366eaeba52d83cc2c92ea61a29a487f:models/N1/mjcf/N1_raw.xml')` in `FFTAI__wiki-grx-mjcf`. fatal: path 'models/N1/mjcf/N1_raw.xml' does not exist in '11da5a77d366eaeba52d83cc2c92ea61a29a487f'

- Network command `git -C .cache/FFTAI__wiki-grx-mjcf fetch --no-tags --refetch --filter=blob:limit=500k origin HEAD` — retrieve omitted source/mesh blobs below 500k for CPU compilation. Parent process runs at nice 15; lazy fetching disabled.

- Network outcome: exit 0. From https://github.com/FFTAI/wiki-grx-mjcf
 * branch            HEAD       -> FETCH_HEAD

- Offline Git read failed (exit 128): `('show', '11da5a77d366eaeba52d83cc2c92ea61a29a487f:models/N1/mjcf/N1_raw.xml')` in `FFTAI__wiki-grx-mjcf`. fatal: path 'models/N1/mjcf/N1_raw.xml' does not exist in '11da5a77d366eaeba52d83cc2c92ea61a29a487f'

- Network command `git -C .cache/FFTAI__wiki-grx-mjcf fetch --no-tags --refetch --filter=blob:limit=5m origin HEAD` — retrieve omitted source/mesh blobs below 5m for CPU compilation. Parent process runs at nice 15; lazy fetching disabled.

- Network outcome: exit 0. From https://github.com/FFTAI/wiki-grx-mjcf
 * branch            HEAD       -> FETCH_HEAD

- Offline Git read failed (exit 128): `('show', '11da5a77d366eaeba52d83cc2c92ea61a29a487f:models/N1/mjcf/N1_raw.xml')` in `FFTAI__wiki-grx-mjcf`. fatal: path 'models/N1/mjcf/N1_raw.xml' does not exist in '11da5a77d366eaeba52d83cc2c92ea61a29a487f'

- Network command `git -C .cache/FFTAI__wiki-grx-mjcf fetch --no-tags --refetch --filter=blob:limit=20m origin HEAD` — retrieve omitted source/mesh blobs below 20m for CPU compilation. Parent process runs at nice 15; lazy fetching disabled.

- Network outcome: exit 0. From https://github.com/FFTAI/wiki-grx-mjcf
 * branch            HEAD       -> FETCH_HEAD

- Offline Git read failed (exit 128): `('show', '11da5a77d366eaeba52d83cc2c92ea61a29a487f:models/N1/mjcf/N1_raw.xml')` in `FFTAI__wiki-grx-mjcf`. fatal: path 'models/N1/mjcf/N1_raw.xml' does not exist in '11da5a77d366eaeba52d83cc2c92ea61a29a487f'

- Historical source compile failed fourier_n1 11da5a77d366eaeba52d83cc2c92ea61a29a487f models/N1/mjcf/N1_raw.xml: Command '['git', '-C', '.cache/FFTAI__wiki-grx-mjcf', 'show', '11da5a77d366eaeba52d83cc2c92ea61a29a487f:models/N1/mjcf/N1_raw.xml']' returned non-zero exit status 128.

- Historical source compile failed fourier_n1 51e935ccefecbe7238a936d8374bd738608543a7 models/N1/mjcf/N1_raw.xml: Error: texture 'texplane' not found in material 0
Element name 'MatPlane', id 0, line 119

- Historical source compile failed fourier_n1 39922911691a45242cf3df408da5fde735185540 models/N1/mjcf/N1_raw.xml: Error: texture 'texplane' not found in material 0
Element name 'MatPlane', id 0, line 119

- Historical source compile failed fourier_n1 f29a87905bdcfc32fdac9c5342644630fd27156a models/N1/mjcf/N1_raw.xml: Error: texture 'texplane' not found in material 0
Element name 'MatPlane', id 0, line 119

- Menagerie self-comparison compile failed: franka_emika_panda/mjx_scene.xml: ValueError: Error: texture 'groundplane' not found in material 5
Element name 'groundplane', id 5, line 121

- Menagerie self-comparison compile failed: franka_emika_panda/mjx_single_cube.xml: ValueError: Error: mesh 'link0_0' not found in geom 1
Element name '', id 1, line 120

- Menagerie self-comparison compile failed: franka_emika_panda/panda_nohand.xml: ValueError: Error: mesh 'link0_0' not found in geom 0
Element name '', id 0, line 99

- Network command `git clone --filter=blob:limit=100k --no-checkout https://github.com/frankaemika/franka_ros.git .cache/frankaemika__franka_ros` — retrieve manufacturer source history and small text files. Parent process runs at nice 15; lazy fetching disabled.

- Network outcome: exit 0. Cloning into '.cache/frankaemika__franka_ros'...

- Offline Git read failed (exit 128): `('show', 'ddd2fffd9de44b02ad15b4bbb2bfa2cec4d60d98:franka_description/meshes/visual/link0.dae')` in `frankaemika__franka_ros`. fatal: bad object ddd2fffd9de44b02ad15b4bbb2bfa2cec4d60d98:franka_description/meshes/visual/link0.dae

- Network command `git -C .cache/frankaemika__franka_ros fetch --no-tags --refetch --filter=blob:limit=500k origin HEAD` — retrieve omitted source/mesh blobs below 500k for CPU compilation. Parent process runs at nice 15; lazy fetching disabled.

- Network outcome: exit 0. From https://github.com/frankaemika/franka_ros
 * branch              HEAD       -> FETCH_HEAD

- Offline Git read failed (exit 128): `('show', 'ddd2fffd9de44b02ad15b4bbb2bfa2cec4d60d98:franka_description/meshes/visual/link0.dae')` in `frankaemika__franka_ros`. fatal: bad object ddd2fffd9de44b02ad15b4bbb2bfa2cec4d60d98:franka_description/meshes/visual/link0.dae

- Network command `git -C .cache/frankaemika__franka_ros fetch --no-tags --refetch --filter=blob:limit=5m origin HEAD` — retrieve omitted source/mesh blobs below 5m for CPU compilation. Parent process runs at nice 15; lazy fetching disabled.

- Network outcome: exit 0. From https://github.com/frankaemika/franka_ros
 * branch              HEAD       -> FETCH_HEAD

- https://github.com/frankaemika/franka_ros franka_gazebo/test/launch/panda-gazebo.urdf at ddd2fffd9de44b02ad15b4bbb2bfa2cec4d60d98: ValueError: Error: size 1 must be positive in geom
Element name '', id 0

- Historical Menagerie compile failed franka_emika_panda 1b428b08bb26ca6024e7b21e8ff21a59f847eb87: Error: mesh 'link0_0' not found in geom 0
Element name '', id 0, line 122

- Menagerie self-comparison compile failed: franka_fr3/fr3.xml: ValueError: Error: mesh 'link0_0' not found in geom 0
Element name '', id 0, line 72

- Offline Git read failed (exit 128): `('show', '370c43965323c0944b433b202aac5058b5f907a9:franka_fr3_duo/assets/fr3_duo_mount.obj')` in `menagerie`. fatal: bad object 370c43965323c0944b433b202aac5058b5f907a9:franka_fr3_duo/assets/fr3_duo_mount.obj

- Menagerie self-comparison compile failed: franka_fr3_duo/fr3_duo.xml: CalledProcessError: Command '['git', '-C', '.cache/menagerie', 'show', '370c43965323c0944b433b202aac5058b5f907a9:franka_fr3_duo/assets/fr3_duo_mount.obj']' returned non-zero exit status 128.

- Offline Git read failed (exit 128): `('show', '370c43965323c0944b433b202aac5058b5f907a9:franka_fr3_duo/assets/fr3_duo_mount.obj')` in `menagerie`. fatal: bad object 370c43965323c0944b433b202aac5058b5f907a9:franka_fr3_duo/assets/fr3_duo_mount.obj

- Menagerie self-comparison compile failed: franka_fr3_duo/fr3_duo_with_spine.xml: CalledProcessError: Command '['git', '-C', '.cache/menagerie', 'show', '370c43965323c0944b433b202aac5058b5f907a9:franka_fr3_duo/assets/fr3_duo_mount.obj']' returned non-zero exit status 128.

- Menagerie self-comparison compile failed: franka_fr3_v2/fr3v2.xml: ValueError: Error: mesh 'link0_0' not found in geom 0
Element name '', id 0, line 71

- Menagerie self-comparison compile failed: google_robot/robot.xml: ValueError: Resource missing at 370c43965323c0944b433b202aac5058b5f907a9: google_robot/robot_texture.png

- Menagerie self-comparison compile failed: hello_robot_stretch/stretch.xml: ValueError: Resource missing at 370c43965323c0944b433b202aac5058b5f907a9: hello_robot_stretch/hand_crush.png

- Menagerie self-comparison compile failed: hello_robot_stretch_3/stretch.xml: ValueError: Resource missing at 370c43965323c0944b433b202aac5058b5f907a9: hello_robot_stretch_3/hand_crush.png

- Menagerie self-comparison compile failed: i2rt_yam/yam.xml: ValueError: Error: mesh 'model2' not found in geom 0
Element name '', id 0, line 59

- Menagerie self-comparison compile failed: i2rt_yam/yam_linear_4310.xml: ValueError: Error: mesh 'model2' not found in geom 0
Element name '', id 0, line 65

- Network command `git clone --filter=blob:limit=100k --no-checkout https://github.com/NMMI/SoftFoot_MuJoCo.git .cache/NMMI__SoftFoot_MuJoCo` — retrieve manufacturer source history and small text files. Parent process runs at nice 15; lazy fetching disabled.

- Network outcome: exit 0. Cloning into '.cache/NMMI__SoftFoot_MuJoCo'...

- Network command `git clone --filter=blob:limit=100k --no-checkout https://github.com/Kinovarobotics/ros_kortex.git .cache/Kinovarobotics__ros_kortex` — retrieve manufacturer source history and small text files. Parent process runs at nice 15; lazy fetching disabled.

- Network outcome: exit 0. Cloning into '.cache/Kinovarobotics__ros_kortex'...

- https://github.com/Kinovarobotics/ros_kortex kortex_description/robots/gen3.xacro at c3280d8a6a6b5d96590d51538e3f265710a6c77d: ValueError: $(find robotiq_2f_85_gripper_visualization) is outside the cloned repository

- Network command `git clone --filter=blob:limit=100k --no-checkout https://github.com/RobotLocomotion/drake.git .cache/RobotLocomotion__drake` — retrieve manufacturer source history and small text files. Parent process runs at nice 15; lazy fetching disabled.

- Network outcome: exit 0. Cloning into '.cache/RobotLocomotion__drake'...

- Network command `git clone --filter=blob:limit=100k --no-checkout https://github.com/leap-hand/LEAP_Hand_Sim.git .cache/leap-hand__LEAP_Hand_Sim` — retrieve manufacturer source history and small text files. Parent process runs at nice 15; lazy fetching disabled.

- Network outcome: exit 0. Cloning into '.cache/leap-hand__LEAP_Hand_Sim'...

- Network command `git clone --filter=blob:limit=100k --no-checkout https://github.com/dexsuite/dex-urdf.git .cache/dexsuite__dex-urdf` — retrieve manufacturer source history and small text files. Parent process runs at nice 15; lazy fetching disabled.

- Network outcome: exit 0. Cloning into '.cache/dexsuite__dex-urdf'...

- Offline Git read failed (exit 128): `('show', 'f5e7132f22108164577fea4c25ef99b5cc0e1900:robots/hands/leap_hand/meshes/visual/palm_lower_left.obj')` in `dexsuite__dex-urdf`. fatal: bad object f5e7132f22108164577fea4c25ef99b5cc0e1900:robots/hands/leap_hand/meshes/visual/palm_lower_left.obj

- Network command `git -C .cache/dexsuite__dex-urdf fetch --no-tags --refetch --filter=blob:limit=500k origin HEAD` — retrieve omitted source/mesh blobs below 500k for CPU compilation. Parent process runs at nice 15; lazy fetching disabled.

- Network outcome: exit 0. From https://github.com/dexsuite/dex-urdf
 * branch            HEAD       -> FETCH_HEAD

- Offline Git read failed (exit 128): `('show', 'f5e7132f22108164577fea4c25ef99b5cc0e1900:robots/hands/leap_hand/meshes/visual/palm_lower_left.obj')` in `dexsuite__dex-urdf`. fatal: bad object f5e7132f22108164577fea4c25ef99b5cc0e1900:robots/hands/leap_hand/meshes/visual/palm_lower_left.obj

- Network command `git -C .cache/dexsuite__dex-urdf fetch --no-tags --refetch --filter=blob:limit=5m origin HEAD` — retrieve omitted source/mesh blobs below 5m for CPU compilation. Parent process runs at nice 15; lazy fetching disabled.

- Network outcome: exit 0. From https://github.com/dexsuite/dex-urdf
 * branch            HEAD       -> FETCH_HEAD

- Offline Git read failed (exit 128): `('show', 'f5e7132f22108164577fea4c25ef99b5cc0e1900:robots/hands/leap_hand/meshes/visual/palm_lower_left.glb')` in `dexsuite__dex-urdf`. fatal: bad object f5e7132f22108164577fea4c25ef99b5cc0e1900:robots/hands/leap_hand/meshes/visual/palm_lower_left.glb

- Network command `git -C .cache/dexsuite__dex-urdf fetch --no-tags --refetch --filter=blob:limit=20m origin HEAD` — retrieve omitted source/mesh blobs below 20m for CPU compilation. Parent process runs at nice 15; lazy fetching disabled.

- Offline Git read failed (exit 128): `('show', 'd9415a3076f921fdb9735d45d609a596df722468:apptronik_apollo/CHANGELOG.md')` in `menagerie`. fatal: bad object d9415a3076f921fdb9735d45d609a596df722468:apptronik_apollo/CHANGELOG.md

- Offline Git read failed (exit 128): `('show', 'd9415a3076f921fdb9735d45d609a596df722468:berkeley_humanoid/CHANGELOG.md')` in `menagerie`. fatal: bad object d9415a3076f921fdb9735d45d609a596df722468:berkeley_humanoid/CHANGELOG.md

- Offline Git read failed (exit 128): `('show', 'd9415a3076f921fdb9735d45d609a596df722468:booster_t1/CHANGELOG.md')` in `menagerie`. fatal: bad object d9415a3076f921fdb9735d45d609a596df722468:booster_t1/CHANGELOG.md

- Offline Git read failed (exit 128): `('show', 'd9415a3076f921fdb9735d45d609a596df722468:fourier_n1/CHANGELOG.md')` in `menagerie`. fatal: bad object d9415a3076f921fdb9735d45d609a596df722468:fourier_n1/CHANGELOG.md

- Offline Git read failed (exit 128): `('show', 'fae9ee82330444eec4e87568c838b99a09a39467:rainbow_robotics_rby1/README.md')` in `menagerie`. fatal: path 'rainbow_robotics_rby1/README.md' does not exist in 'fae9ee82330444eec4e87568c838b99a09a39467'

- Offline Git read failed (exit 128): `('show', 'd9415a3076f921fdb9735d45d609a596df722468:unitree_g1/CHANGELOG.md')` in `menagerie`. fatal: bad object d9415a3076f921fdb9735d45d609a596df722468:unitree_g1/CHANGELOG.md

- https://github.com/agilexrobotics/Piper_ros src/piper_description/urdf/piper_description_v100_camera.urdf at ac41fcbcdda598f01b51cf6175ed9a24d0dacadc: ValueError: $(find piper_camera_moveit_config) is outside the cloned repository

- https://github.com/agilexrobotics/Piper_ros src/piper_description/urdf/piper_description_with_camera.xacro at ac41fcbcdda598f01b51cf6175ed9a24d0dacadc: ValueError: $(find piper_camera_moveit_config) is outside the cloned repository

- Menagerie self-comparison compile failed: aloha/filtered_cartesian_actuators.xml: ValueError: Error: transmission target 'left/gripper' not found in actuator 0
Element name 'left/X', id 0, line 36

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 clone --filter=blob:limit=100k --no-checkout https://github.com/ANYbotics/anymal_b_simple_description.git .cache/ANYbotics__anymal_b_simple_description` — retrieve manufacturer source history and small text files. Parent process runs at nice 15; lazy fetching disabled.

- Network outcome: exit 0. Cloning into '.cache/ANYbotics__anymal_b_simple_description'...

- Offline Git read failed (exit 128): `('show', '988b5df22b84761bdf08111b1c2ccc883793f456:meshes/anymal_base.dae')` in `ANYbotics__anymal_b_simple_description`. fatal: bad object 988b5df22b84761bdf08111b1c2ccc883793f456:meshes/anymal_base.dae

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/ANYbotics__anymal_b_simple_description -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `69e3a2b6e2cf27e4f3d325aced662a5e50eb33bd`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '988b5df22b84761bdf08111b1c2ccc883793f456:meshes/anymal_hip_l.dae')` in `ANYbotics__anymal_b_simple_description`. fatal: bad object 988b5df22b84761bdf08111b1c2ccc883793f456:meshes/anymal_hip_l.dae

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/ANYbotics__anymal_b_simple_description -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `45d1a739f928758d340c2713a911dce065e4d32b`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '988b5df22b84761bdf08111b1c2ccc883793f456:meshes/anymal_thigh_l.dae')` in `ANYbotics__anymal_b_simple_description`. fatal: bad object 988b5df22b84761bdf08111b1c2ccc883793f456:meshes/anymal_thigh_l.dae

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/ANYbotics__anymal_b_simple_description -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `c7cb1395c32a4ace333f64dcdd9389f4a45e4448`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '988b5df22b84761bdf08111b1c2ccc883793f456:meshes/anymal_shank_l.dae')` in `ANYbotics__anymal_b_simple_description`. fatal: bad object 988b5df22b84761bdf08111b1c2ccc883793f456:meshes/anymal_shank_l.dae

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/ANYbotics__anymal_b_simple_description -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `6aea0ea6ce115c977009679271d45b713950da33`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '988b5df22b84761bdf08111b1c2ccc883793f456:meshes/anymal_foot.dae')` in `ANYbotics__anymal_b_simple_description`. fatal: bad object 988b5df22b84761bdf08111b1c2ccc883793f456:meshes/anymal_foot.dae

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/ANYbotics__anymal_b_simple_description -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `1d564ee115a03d75c5a4dc4cd0f28521896af60a`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '988b5df22b84761bdf08111b1c2ccc883793f456:meshes/anymal_hip_r.dae')` in `ANYbotics__anymal_b_simple_description`. fatal: bad object 988b5df22b84761bdf08111b1c2ccc883793f456:meshes/anymal_hip_r.dae

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/ANYbotics__anymal_b_simple_description -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `3e3eaf92a323c94332fa0296c82846c8b511219c`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '988b5df22b84761bdf08111b1c2ccc883793f456:meshes/anymal_thigh_r.dae')` in `ANYbotics__anymal_b_simple_description`. fatal: bad object 988b5df22b84761bdf08111b1c2ccc883793f456:meshes/anymal_thigh_r.dae

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/ANYbotics__anymal_b_simple_description -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `eaf15b25a3028deacdb9f327f1fa34f1fc10e793`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '988b5df22b84761bdf08111b1c2ccc883793f456:meshes/anymal_shank_r.dae')` in `ANYbotics__anymal_b_simple_description`. fatal: bad object 988b5df22b84761bdf08111b1c2ccc883793f456:meshes/anymal_shank_r.dae

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/ANYbotics__anymal_b_simple_description -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `63c75cdde81835b09ada37826e22555dc08b681f`

- Network outcome: exit 0.

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 clone --filter=blob:limit=100k --no-checkout https://github.com/ANYbotics/anymal_c_simple_description.git .cache/ANYbotics__anymal_c_simple_description` — retrieve manufacturer source history and small text files. Parent process runs at nice 15; lazy fetching disabled.

- Network outcome: exit 0. Cloning into '.cache/ANYbotics__anymal_c_simple_description'...

- Offline Git read failed (exit 128): `('show', '87b68511622f0f17e78d9ddca7d862f150a93fb4:meshes/base.dae')` in `ANYbotics__anymal_c_simple_description`. fatal: bad object 87b68511622f0f17e78d9ddca7d862f150a93fb4:meshes/base.dae

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/ANYbotics__anymal_c_simple_description -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `c07f525d617d2d8b9d982e072e22168523564a3f`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '87b68511622f0f17e78d9ddca7d862f150a93fb4:meshes/top_shell.dae')` in `ANYbotics__anymal_c_simple_description`. fatal: bad object 87b68511622f0f17e78d9ddca7d862f150a93fb4:meshes/top_shell.dae

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/ANYbotics__anymal_c_simple_description -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `7c7a404d57e7354e725d059532389de6ddb7e103`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '87b68511622f0f17e78d9ddca7d862f150a93fb4:meshes/bottom_shell.dae')` in `ANYbotics__anymal_c_simple_description`. fatal: bad object 87b68511622f0f17e78d9ddca7d862f150a93fb4:meshes/bottom_shell.dae

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/ANYbotics__anymal_c_simple_description -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `77977538b3c1387f7d9bf78566fa69ec04c72184`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '87b68511622f0f17e78d9ddca7d862f150a93fb4:meshes/face.dae')` in `ANYbotics__anymal_c_simple_description`. fatal: bad object 87b68511622f0f17e78d9ddca7d862f150a93fb4:meshes/face.dae

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/ANYbotics__anymal_c_simple_description -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `577887cbe8beeae961496c8952c274d9fc6ec3a7`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '87b68511622f0f17e78d9ddca7d862f150a93fb4:meshes/thigh.dae')` in `ANYbotics__anymal_c_simple_description`. fatal: bad object 87b68511622f0f17e78d9ddca7d862f150a93fb4:meshes/thigh.dae

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/ANYbotics__anymal_c_simple_description -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `3f6c6db01023bbc2f9bd84d609dd48c1cfb10040`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '87b68511622f0f17e78d9ddca7d862f150a93fb4:meshes/shank_l.dae')` in `ANYbotics__anymal_c_simple_description`. fatal: bad object 87b68511622f0f17e78d9ddca7d862f150a93fb4:meshes/shank_l.dae

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/ANYbotics__anymal_c_simple_description -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `177875366ca9634784755b3ef0d5730a76a324c0`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '87b68511622f0f17e78d9ddca7d862f150a93fb4:meshes/foot.dae')` in `ANYbotics__anymal_c_simple_description`. fatal: bad object 87b68511622f0f17e78d9ddca7d862f150a93fb4:meshes/foot.dae

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/ANYbotics__anymal_c_simple_description -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `da4f0a0c73a88aa515c67959e4b8078a075d68fd`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '87b68511622f0f17e78d9ddca7d862f150a93fb4:meshes/shank_r.dae')` in `ANYbotics__anymal_c_simple_description`. fatal: bad object 87b68511622f0f17e78d9ddca7d862f150a93fb4:meshes/shank_r.dae

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/ANYbotics__anymal_c_simple_description -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `d0b8f22c1aaad18fa3d27680b35723d667c5cf65`

- Network outcome: exit 0.

- https://github.com/ANYbotics/anymal_c_simple_description urdf/anymal.urdf at 87b68511622f0f17e78d9ddca7d862f150a93fb4: ValueError: Error: inertia must satisfy A + B >= C; use 'balanceinertia' to fix
Element name 'depth_camera_front_camera', id 8

- Offline Git read failed (exit 128): `('show', 'd9415a3076f921fdb9735d45d609a596df722468:berkeley_humanoid/berkeley_humanoid.xml')` in `menagerie`. fatal: bad object d9415a3076f921fdb9735d45d609a596df722468:berkeley_humanoid/berkeley_humanoid.xml

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/menagerie -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `ecb1d14f4d805e9d629db234b40fc5f1ac246287`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'd9415a3076f921fdb9735d45d609a596df722468:booster_t1/t1.xml')` in `menagerie`. fatal: bad object d9415a3076f921fdb9735d45d609a596df722468:booster_t1/t1.xml

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/menagerie -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `1b22500a490d9f82187958018d65345f28ee235b`

- Network outcome: exit 0.

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 clone --filter=blob:limit=100k --no-checkout https://github.com/rai-opensource/spot_description.git .cache/rai-opensource__spot_description` — retrieve manufacturer source history and small text files. Parent process runs at nice 15; lazy fetching disabled.

- Network outcome: exit 0. Cloning into '.cache/rai-opensource__spot_description'...

- https://github.com/rai-opensource/spot_description spot_description/urdf/spot.urdf.xacro at 156d1802bfb117f219dbfce7597d283d5fabc968: ValueError: $(find velodyne_description) is outside the cloned repository

- https://github.com/rai-opensource/spot_description spot_description/urdf/spot_simple.urdf.xacro at 156d1802bfb117f219dbfce7597d283d5fabc968: ValueError: $(find velodyne_description) is outside the cloned repository

- https://github.com/rai-opensource/spot_description spot_description/urdf/spot_arm_macro.urdf at 156d1802bfb117f219dbfce7597d283d5fabc968: ValueError: $(find velodyne_description) is outside the cloned repository

- https://github.com/rai-opensource/spot_description spot_description/urdf/spot_feet_macro.urdf at 156d1802bfb117f219dbfce7597d283d5fabc968: ValueError: $(find velodyne_description) is outside the cloned repository

- https://github.com/rai-opensource/spot_description spot_description/urdf/spot_gripper_macro.urdf at 156d1802bfb117f219dbfce7597d283d5fabc968: ValueError: $(find velodyne_description) is outside the cloned repository

- Offline Git read failed (exit 128): `('show', '370c43965323c0944b433b202aac5058b5f907a9:flybody/assets/head_red.obj')` in `menagerie`. fatal: bad object 370c43965323c0944b433b202aac5058b5f907a9:flybody/assets/head_red.obj

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/menagerie -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `fcde7b1190290cb45719cfb3398fd2b3c57ac5b1`

- Network outcome: exit 0.

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 clone --filter=blob:limit=100k --no-checkout https://github.com/TuragaLab/flybody.git .cache/TuragaLab__flybody` — retrieve manufacturer source history and small text files. Parent process runs at nice 15; lazy fetching disabled.

- Network outcome: exit 0. Cloning into '.cache/TuragaLab__flybody'...

- Offline Git read failed (exit 128): `('show', 'd015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/assets/head_body.obj')` in `TuragaLab__flybody`. fatal: bad object d015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/assets/head_body.obj

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/TuragaLab__flybody -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `364e79b53f5e54da2351f307322675ee6ab08e81`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'd015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/assets/head_red.obj')` in `TuragaLab__flybody`. fatal: bad object d015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/assets/head_red.obj

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/TuragaLab__flybody -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `fcde7b1190290cb45719cfb3398fd2b3c57ac5b1`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'd015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/assets/head_ocelli.obj')` in `TuragaLab__flybody`. fatal: bad object d015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/assets/head_ocelli.obj

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/TuragaLab__flybody -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `a03182814a359c2b9b24e9ed124f32a6a181b233`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'd015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/assets/head_black.obj')` in `TuragaLab__flybody`. fatal: bad object d015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/assets/head_black.obj

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/TuragaLab__flybody -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `5ad110afebf2f02f5ee1f33a3394ec3852d3d841`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'd015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/assets/haustellum_body.obj')` in `TuragaLab__flybody`. fatal: bad object d015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/assets/haustellum_body.obj

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/TuragaLab__flybody -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `3c9fc683757a09bb8b622b5d77bdf07dc7cb635c`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'd015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/assets/haustellum_black.obj')` in `TuragaLab__flybody`. fatal: bad object d015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/assets/haustellum_black.obj

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/TuragaLab__flybody -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `0f41566d28e3b4692be4b4f34edd77e573ace998`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'd015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/assets/rostrum_body.obj')` in `TuragaLab__flybody`. fatal: bad object d015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/assets/rostrum_body.obj

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/TuragaLab__flybody -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `99b3deb4f7b25c5e05ccdb4e8ffaad98810540c3`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'd015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/assets/rostrum_bristle-brown.obj')` in `TuragaLab__flybody`. fatal: bad object d015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/assets/rostrum_bristle-brown.obj

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/TuragaLab__flybody -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `dcd4152012fd3e0f5be86ce7ae4e11b538aec28c`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'd015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/assets/labrum_left_lower.obj')` in `TuragaLab__flybody`. fatal: bad object d015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/assets/labrum_left_lower.obj

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/TuragaLab__flybody -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `87e43ec25397214e5d325513276cdb3d8c97b6fe`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'd015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/assets/wing_left_brown.obj')` in `TuragaLab__flybody`. fatal: bad object d015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/assets/wing_left_brown.obj

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/TuragaLab__flybody -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `1e69ba80230ca6e16ffdcfc696f200d4db272b45`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'd015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/assets/wing_left_membrane.obj')` in `TuragaLab__flybody`. fatal: bad object d015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/assets/wing_left_membrane.obj

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/TuragaLab__flybody -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `f9e5ec2b41448e4ecb076d773fdcbb5d1f30d841`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'd015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/assets/antenna_left_body.obj')` in `TuragaLab__flybody`. fatal: bad object d015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/assets/antenna_left_body.obj

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/TuragaLab__flybody -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `b5d1339ead15696e207f62045df9c5bdc5891613`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'd015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/assets/antenna_left_black.obj')` in `TuragaLab__flybody`. fatal: bad object d015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/assets/antenna_left_black.obj

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/TuragaLab__flybody -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `1927bae6f6f253edf50858e42793445da672ea87`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'd015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/assets/haltere_left_body.obj')` in `TuragaLab__flybody`. fatal: bad object d015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/assets/haltere_left_body.obj

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/TuragaLab__flybody -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `1f582e77cf888fa0a79a23e7d112e3ec151f4b61`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'd015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/assets/labrum_right_lower.obj')` in `TuragaLab__flybody`. fatal: bad object d015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/assets/labrum_right_lower.obj

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/TuragaLab__flybody -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `1d89d00a36f23c215f4b24ea869673e62f1694a8`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'd015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/assets/wing_right_brown.obj')` in `TuragaLab__flybody`. fatal: bad object d015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/assets/wing_right_brown.obj

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/TuragaLab__flybody -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `74d66dcd3ba858fa1e2089a77e5d48b1a8588671`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'd015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/assets/wing_right_membrane.obj')` in `TuragaLab__flybody`. fatal: bad object d015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/assets/wing_right_membrane.obj

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/TuragaLab__flybody -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `56a487d917cdc2322c43331b1c107a9eedacc60c`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'd015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/assets/antenna_right_body.obj')` in `TuragaLab__flybody`. fatal: bad object d015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/assets/antenna_right_body.obj

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/TuragaLab__flybody -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `b37348331e6580718ae7ead5b9704777f3afd14f`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'd015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/assets/antenna_right_black.obj')` in `TuragaLab__flybody`. fatal: bad object d015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/assets/antenna_right_black.obj

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/TuragaLab__flybody -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `7aff83ed6d52632c91c9829d2fa25116c3f241bf`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'd015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/assets/haltere_right_body.obj')` in `TuragaLab__flybody`. fatal: bad object d015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/assets/haltere_right_body.obj

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/TuragaLab__flybody -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `0e5eb20fdec1c1a69042147e7b0c1fdf5c2b4e50`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'd015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/assets/thorax_body.obj')` in `TuragaLab__flybody`. fatal: bad object d015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/assets/thorax_body.obj

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/TuragaLab__flybody -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `1f8e6cac46959e66a02adcd728528aa77d4cbad1`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'd015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/assets/thorax_black.obj')` in `TuragaLab__flybody`. fatal: bad object d015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/assets/thorax_black.obj

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/TuragaLab__flybody -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `b235e1578b9468d6a4687dbef068ca06904a04a2`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'd015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/assets/abdomen_1_body.obj')` in `TuragaLab__flybody`. fatal: bad object d015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/assets/abdomen_1_body.obj

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/TuragaLab__flybody -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `e91595837b0036f62a7e1358115c58d3d96f03a1`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'd015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/assets/abdomen_1_lower.obj')` in `TuragaLab__flybody`. fatal: bad object d015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/assets/abdomen_1_lower.obj

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/TuragaLab__flybody -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `ecf6a42ff08c02bf82e2e605384b9055e41bae4c`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'd015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/assets/abdomen_2_body.obj')` in `TuragaLab__flybody`. fatal: bad object d015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/assets/abdomen_2_body.obj

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/TuragaLab__flybody -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `a2cd8d2c2bd0124ea893837f8a44362a7319a795`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'd015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/assets/abdomen_2_lower.obj')` in `TuragaLab__flybody`. fatal: bad object d015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/assets/abdomen_2_lower.obj

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/TuragaLab__flybody -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `0fecd5dedd35d6573dad655e8f92c3114b3aa24c`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'd015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/assets/abdomen_3_body.obj')` in `TuragaLab__flybody`. fatal: bad object d015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/assets/abdomen_3_body.obj

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/TuragaLab__flybody -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `1ab89dc0de15a35a203e11e3b900dd0eb924da36`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'd015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/assets/abdomen_3_lower.obj')` in `TuragaLab__flybody`. fatal: bad object d015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/assets/abdomen_3_lower.obj

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/TuragaLab__flybody -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `317a56f2c6a2b82861953b4053379e56e9388f42`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'd015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/assets/abdomen_4_body.obj')` in `TuragaLab__flybody`. fatal: bad object d015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/assets/abdomen_4_body.obj

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/TuragaLab__flybody -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `d5bd4bdaaff33a260538c32c46805b36687055cb`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'd015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/assets/abdomen_4_lower.obj')` in `TuragaLab__flybody`. fatal: bad object d015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/assets/abdomen_4_lower.obj

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/TuragaLab__flybody -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `6843711fac2cd3859de7ea493984dc0670b5f3ba`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'd015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/assets/abdomen_5_body.obj')` in `TuragaLab__flybody`. fatal: bad object d015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/assets/abdomen_5_body.obj

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/TuragaLab__flybody -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `d207b9d81eede267c89ba970d6f9af80069f3362`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'd015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/assets/abdomen_5_lower.obj')` in `TuragaLab__flybody`. fatal: bad object d015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/assets/abdomen_5_lower.obj

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/TuragaLab__flybody -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `8fc3d6a199f3773de69f7fa97ecc45903436f218`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'd015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/assets/abdomen_6_body.obj')` in `TuragaLab__flybody`. fatal: bad object d015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/assets/abdomen_6_body.obj

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/TuragaLab__flybody -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `f7e98f76817aed6fd66703ff6ff65bb62871ce95`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'd015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/assets/abdomen_6_lower.obj')` in `TuragaLab__flybody`. fatal: bad object d015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/assets/abdomen_6_lower.obj

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/TuragaLab__flybody -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `bcaf48f1147531b97d0788e98e119e66af093f59`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'd015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/assets/abdomen_7_body.obj')` in `TuragaLab__flybody`. fatal: bad object d015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/assets/abdomen_7_body.obj

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/TuragaLab__flybody -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `5284cd832a81c26e84d24582e14d4a803c42d877`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'd015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/assets/abdomen_7_lower.obj')` in `TuragaLab__flybody`. fatal: bad object d015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/assets/abdomen_7_lower.obj

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/TuragaLab__flybody -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `bdae0bb6fddbcca54e07ca7f072153db33519a39`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'd015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/assets/abdomen_8_body.obj')` in `TuragaLab__flybody`. fatal: bad object d015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/assets/abdomen_8_body.obj

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/TuragaLab__flybody -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `2d115e358a30a5cb6f456365860fad8a89a84d51`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'd015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/assets/tibia_T1_left_body.obj')` in `TuragaLab__flybody`. fatal: bad object d015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/assets/tibia_T1_left_body.obj

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/TuragaLab__flybody -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `ee66921433cfdb4db6cb2f2e0e725d1e53e9d218`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'd015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/assets/tarsus_T1_1_left_body.obj')` in `TuragaLab__flybody`. fatal: bad object d015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/assets/tarsus_T1_1_left_body.obj

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/TuragaLab__flybody -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `f3c352a9f61c1e660d82586f0843b9596889d95f`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'd015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/assets/tarsus_T1_2_left_body.obj')` in `TuragaLab__flybody`. fatal: bad object d015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/assets/tarsus_T1_2_left_body.obj

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/TuragaLab__flybody -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `32517b6625742a03da3e68ed333f68f7d3f03255`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'd015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/assets/tarsus_T1_3_left_body.obj')` in `TuragaLab__flybody`. fatal: bad object d015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/assets/tarsus_T1_3_left_body.obj

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/TuragaLab__flybody -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `13f021272e166c5ba16d531d5f7e4f8d8dc2a8f7`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'd015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/assets/tarsus_T1_4_left_body.obj')` in `TuragaLab__flybody`. fatal: bad object d015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/assets/tarsus_T1_4_left_body.obj

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/TuragaLab__flybody -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `9edbd0efbdbc3afd471989e1840fb3aeb3630853`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'd015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/assets/tarsal_claw_T1_left_brown.obj')` in `TuragaLab__flybody`. fatal: bad object d015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/assets/tarsal_claw_T1_left_brown.obj

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/TuragaLab__flybody -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `09fdf1e616cd8a3a8c5843680428779aa4d77aa5`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'd015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/assets/tarsus_T2_2_left_body.obj')` in `TuragaLab__flybody`. fatal: bad object d015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/assets/tarsus_T2_2_left_body.obj

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/TuragaLab__flybody -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `73646af98c6d2e961f6126e8df61a829e75ab2ed`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'd015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/assets/tarsus_T2_3_left_body.obj')` in `TuragaLab__flybody`. fatal: bad object d015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/assets/tarsus_T2_3_left_body.obj

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/TuragaLab__flybody -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `2be6bb97cc451b82f05055580aaf285485ccaaef`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'd015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/assets/tarsus_T2_4_left_body.obj')` in `TuragaLab__flybody`. fatal: bad object d015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/assets/tarsus_T2_4_left_body.obj

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/TuragaLab__flybody -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `92d53948c3b5c824bbcd10212629b8940944ef26`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'd015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/assets/tarsal_claw_T2_left_brown.obj')` in `TuragaLab__flybody`. fatal: bad object d015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/assets/tarsal_claw_T2_left_brown.obj

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/TuragaLab__flybody -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `962cd348aaaf909f7e5df1f61a0b4b70bbe47211`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'd015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/assets/tarsus_T2_1_left_body.obj')` in `TuragaLab__flybody`. fatal: bad object d015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/assets/tarsus_T2_1_left_body.obj

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/TuragaLab__flybody -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `fe4a7f0fe47c94f4b04b029d92a3930ba6882069`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'd015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/assets/tarsus_T3_2_left_body.obj')` in `TuragaLab__flybody`. fatal: bad object d015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/assets/tarsus_T3_2_left_body.obj

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/TuragaLab__flybody -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `f49212a89435cdeb0bb9561b27e3e01ba72a99f7`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'd015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/assets/tarsus_T3_3_left_body.obj')` in `TuragaLab__flybody`. fatal: bad object d015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/assets/tarsus_T3_3_left_body.obj

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/TuragaLab__flybody -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `4cb8cf218a5e4f2af702c564c56fddd4890ea170`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'd015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/assets/tarsus_T3_4_left_body.obj')` in `TuragaLab__flybody`. fatal: bad object d015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/assets/tarsus_T3_4_left_body.obj

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/TuragaLab__flybody -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `04f1808adec3e69cf8f9dbf9ee0aee46c0ba205f`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'd015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/assets/tarsal_claw_T3_left_brown.obj')` in `TuragaLab__flybody`. fatal: bad object d015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/assets/tarsal_claw_T3_left_brown.obj

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/TuragaLab__flybody -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `55f8aaf7f83cdac465a89e35a321291748c65dad`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'd015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/assets/tarsus_T3_1_left_body.obj')` in `TuragaLab__flybody`. fatal: bad object d015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/assets/tarsus_T3_1_left_body.obj

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/TuragaLab__flybody -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `3502bbb930aea4e28968e33b14eb6ece2dc0c944`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'd015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/assets/tibia_T2_left_body.obj')` in `TuragaLab__flybody`. fatal: bad object d015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/assets/tibia_T2_left_body.obj

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/TuragaLab__flybody -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `c9ead61fb978b79f0ce071f8c5bebe7b7688dc34`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'd015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/assets/tibia_T3_left_body.obj')` in `TuragaLab__flybody`. fatal: bad object d015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/assets/tibia_T3_left_body.obj

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/TuragaLab__flybody -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `75238e7d4a895ae3b9525e6e1ea8ad5618c0ec5f`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'd015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/assets/femur_T1_left_body.obj')` in `TuragaLab__flybody`. fatal: bad object d015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/assets/femur_T1_left_body.obj

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/TuragaLab__flybody -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `3b56b0bd8df3dbf87dca0159558d87e6fc97220b`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'd015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/assets/femur_T2_left_body.obj')` in `TuragaLab__flybody`. fatal: bad object d015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/assets/femur_T2_left_body.obj

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/TuragaLab__flybody -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `35d76422693d5eff13dedc95a8284ca72c0bd648`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'd015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/assets/femur_T3_left_body.obj')` in `TuragaLab__flybody`. fatal: bad object d015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/assets/femur_T3_left_body.obj

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/TuragaLab__flybody -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `c6179315c01edb8882843cdbddaba5dfc1e30a88`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'd015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/assets/femur_T1_right_body.obj')` in `TuragaLab__flybody`. fatal: bad object d015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/assets/femur_T1_right_body.obj

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/TuragaLab__flybody -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `db8e889bcba2d70588c54b350dcf4ce90899ba8e`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'd015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/assets/tibia_T1_right_body.obj')` in `TuragaLab__flybody`. fatal: bad object d015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/assets/tibia_T1_right_body.obj

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/TuragaLab__flybody -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `fb46344a8617025ce9ef4bdd1ae97de73fb0e0f8`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'd015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/assets/tarsus_T1_1_right_body.obj')` in `TuragaLab__flybody`. fatal: bad object d015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/assets/tarsus_T1_1_right_body.obj

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/TuragaLab__flybody -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `5e1de80a118f4d12f7a7aa153ffb17bf2b022bd1`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'd015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/assets/tarsus_T1_2_right_body.obj')` in `TuragaLab__flybody`. fatal: bad object d015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/assets/tarsus_T1_2_right_body.obj

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/TuragaLab__flybody -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `1166f7519fbdb93cd60bc7c292fc897548bd1598`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'd015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/assets/tarsus_T1_3_right_body.obj')` in `TuragaLab__flybody`. fatal: bad object d015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/assets/tarsus_T1_3_right_body.obj

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/TuragaLab__flybody -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `c8a9c02301864d09a56f5250f054b340628e0bad`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'd015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/assets/tarsus_T1_4_right_body.obj')` in `TuragaLab__flybody`. fatal: bad object d015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/assets/tarsus_T1_4_right_body.obj

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/TuragaLab__flybody -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `a7ea5cc653246ba0f0d0de863dff47611e265b8b`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'd015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/assets/tarsal_claw_T1_right_brown.obj')` in `TuragaLab__flybody`. fatal: bad object d015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/assets/tarsal_claw_T1_right_brown.obj

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/TuragaLab__flybody -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `57bc146367d898a85acdfa5d41106d6600500e73`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'd015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/assets/femur_T2_right_body.obj')` in `TuragaLab__flybody`. fatal: bad object d015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/assets/femur_T2_right_body.obj

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/TuragaLab__flybody -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `9caeefbd0c6260dd1fa9ee4e45de3ae5377f35c6`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'd015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/assets/tibia_T2_right_body.obj')` in `TuragaLab__flybody`. fatal: bad object d015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/assets/tibia_T2_right_body.obj

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/TuragaLab__flybody -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `f147ae1714314db77e1ddd8b8dea486522ece0b1`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'd015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/assets/tarsus_T2_1_right_body.obj')` in `TuragaLab__flybody`. fatal: bad object d015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/assets/tarsus_T2_1_right_body.obj

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/TuragaLab__flybody -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `8ce28017dfd3377920c34846b297c576d1ff8e2c`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'd015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/assets/tarsus_T2_2_right_body.obj')` in `TuragaLab__flybody`. fatal: bad object d015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/assets/tarsus_T2_2_right_body.obj

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/TuragaLab__flybody -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `f7140da27ec4a5a5fb9c85f098c7f850340c391e`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'd015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/assets/tarsus_T2_3_right_body.obj')` in `TuragaLab__flybody`. fatal: bad object d015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/assets/tarsus_T2_3_right_body.obj

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/TuragaLab__flybody -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `ec29505eb4de005ee23b1f6864d4c1810a52dfc5`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'd015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/assets/tarsus_T2_4_right_body.obj')` in `TuragaLab__flybody`. fatal: bad object d015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/assets/tarsus_T2_4_right_body.obj

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/TuragaLab__flybody -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `9ffb6110c30772fb64e9f13ecd33573e9d6efef2`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'd015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/assets/tarsal_claw_T2_right_brown.obj')` in `TuragaLab__flybody`. fatal: bad object d015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/assets/tarsal_claw_T2_right_brown.obj

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/TuragaLab__flybody -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `b4cc24efa435bf477a369047e7fb8920d8388ab3`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'd015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/assets/femur_T3_right_body.obj')` in `TuragaLab__flybody`. fatal: bad object d015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/assets/femur_T3_right_body.obj

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/TuragaLab__flybody -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `910184733fd5ea3d48a75e6d4e11c336755efb6b`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'd015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/assets/tibia_T3_right_body.obj')` in `TuragaLab__flybody`. fatal: bad object d015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/assets/tibia_T3_right_body.obj

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/TuragaLab__flybody -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `cfb3f813a8c23167bf6d95d9f5eb3fcba6cc584a`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'd015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/assets/tarsus_T3_1_right_body.obj')` in `TuragaLab__flybody`. fatal: bad object d015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/assets/tarsus_T3_1_right_body.obj

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/TuragaLab__flybody -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `c2fd12f85e7fd560e2821cd3354c90a2a5f8e05c`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'd015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/assets/tarsus_T3_2_right_body.obj')` in `TuragaLab__flybody`. fatal: bad object d015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/assets/tarsus_T3_2_right_body.obj

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/TuragaLab__flybody -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `a94316a89fe0d57223b8341a9b92db869edd1eec`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'd015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/assets/tarsus_T3_3_right_body.obj')` in `TuragaLab__flybody`. fatal: bad object d015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/assets/tarsus_T3_3_right_body.obj

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/TuragaLab__flybody -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `9f5e1e94c7e53bba273ea636c02b0aa4d95a7190`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'd015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/assets/tarsus_T3_4_right_body.obj')` in `TuragaLab__flybody`. fatal: bad object d015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/assets/tarsus_T3_4_right_body.obj

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/TuragaLab__flybody -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `971b3c1280760b570fa4c8bd9eca27b2844e8a20`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'd015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/assets/tarsal_claw_T3_right_brown.obj')` in `TuragaLab__flybody`. fatal: bad object d015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/assets/tarsal_claw_T3_right_brown.obj

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/TuragaLab__flybody -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `6eacc7816a76cd2253582a53355782c0e7537ca8`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'd015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/assets/coxa_T1_left_body.obj')` in `TuragaLab__flybody`. fatal: bad object d015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/assets/coxa_T1_left_body.obj

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/TuragaLab__flybody -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `40d9239052d5b48569f58e28abd6f2ded13090a5`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'd015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/assets/coxa_T1_right_body.obj')` in `TuragaLab__flybody`. fatal: bad object d015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/assets/coxa_T1_right_body.obj

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/TuragaLab__flybody -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `c379dc967b7404bd5ef7e74984d268c68d118898`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'd015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/assets/coxa_T2_left_body.obj')` in `TuragaLab__flybody`. fatal: bad object d015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/assets/coxa_T2_left_body.obj

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/TuragaLab__flybody -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `1a18a76668f5ce43aac4ca24c5bb8b9c81e929d4`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'd015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/assets/coxa_T2_right_body.obj')` in `TuragaLab__flybody`. fatal: bad object d015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/assets/coxa_T2_right_body.obj

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/TuragaLab__flybody -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `9db7b0096e38467e37e9260d97e8affd27ac0ff6`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'd015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/assets/coxa_T3_left_body.obj')` in `TuragaLab__flybody`. fatal: bad object d015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/assets/coxa_T3_left_body.obj

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/TuragaLab__flybody -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `e2c955ece9d099362a9af9ad8f14360fa6529b6a`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'd015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/assets/coxa_T3_right_body.obj')` in `TuragaLab__flybody`. fatal: bad object d015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/assets/coxa_T3_right_body.obj

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/TuragaLab__flybody -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `147430365f5cbe24c9123eef0ee2a828e0f92fbf`

- Network outcome: exit 0.

- https://github.com/TuragaLab/flybody flybody/fruitfly/build_fruitfly/floor.xml at d015e9bfe441bd90ae431bac24c55cb74bdbce26: ValueError: Resource missing at d015e9bfe441bd90ae431bac24c55cb74bdbce26: flybody/fruitfly/build_fruitfly/head_body.obj

- https://github.com/TuragaLab/flybody flybody/fruitfly/build_fruitfly/fruitfly.xml at d015e9bfe441bd90ae431bac24c55cb74bdbce26: ValueError: Resource missing at d015e9bfe441bd90ae431bac24c55cb74bdbce26: flybody/fruitfly/build_fruitfly/head_body.obj

- https://github.com/TuragaLab/flybody flybody/fruitfly/build_fruitfly/assets/drosophila.xml at d015e9bfe441bd90ae431bac24c55cb74bdbce26: ValueError: Resource missing at d015e9bfe441bd90ae431bac24c55cb74bdbce26: flybody/fruitfly/build_fruitfly/assets/assets/head_body.msh

- Offline Git read failed (exit 128): `('show', 'd015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/build_fruitfly/assets/head_body.msh')` in `TuragaLab__flybody`. fatal: bad object d015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/build_fruitfly/assets/head_body.msh

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/TuragaLab__flybody -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `4236c6db5f21703109a411c993430f25f4561c93`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'd015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/build_fruitfly/assets/head_red.msh')` in `TuragaLab__flybody`. fatal: bad object d015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/build_fruitfly/assets/head_red.msh

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/TuragaLab__flybody -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `53d30f86c0b2c8a7df68d823fe759ebf94078093`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'd015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/build_fruitfly/assets/head_ocelli.msh')` in `TuragaLab__flybody`. fatal: bad object d015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/build_fruitfly/assets/head_ocelli.msh

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/TuragaLab__flybody -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `4a4c281a8fdb52fac1936318f694162c935b691d`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'd015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/build_fruitfly/assets/head_black.msh')` in `TuragaLab__flybody`. fatal: bad object d015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/build_fruitfly/assets/head_black.msh

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/TuragaLab__flybody -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `ffb2f26bd18f69a956f1f32544d3adad3ba3315a`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'd015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/build_fruitfly/assets/haustellum_body.msh')` in `TuragaLab__flybody`. fatal: bad object d015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/build_fruitfly/assets/haustellum_body.msh

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/TuragaLab__flybody -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `f9d83b9984fd69de21d3b53e36e993a53548b684`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'd015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/build_fruitfly/assets/haustellum_black.msh')` in `TuragaLab__flybody`. fatal: bad object d015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/build_fruitfly/assets/haustellum_black.msh

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/TuragaLab__flybody -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `ce3c56f3d9ef3d18db7cb73e873b6fdbac720637`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'd015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/build_fruitfly/assets/rostrum_body.msh')` in `TuragaLab__flybody`. fatal: bad object d015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/build_fruitfly/assets/rostrum_body.msh

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/TuragaLab__flybody -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `f0bd54e3fa5421d3ef05c0c67fb89eee8940603d`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'd015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/build_fruitfly/assets/rostrum_bristle-brown.msh')` in `TuragaLab__flybody`. fatal: bad object d015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/build_fruitfly/assets/rostrum_bristle-brown.msh

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/TuragaLab__flybody -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `f5dca5352236b2587d04903bb4bebc72151d24d5`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'd015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/build_fruitfly/assets/labrum_left_lower.msh')` in `TuragaLab__flybody`. fatal: bad object d015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/build_fruitfly/assets/labrum_left_lower.msh

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/TuragaLab__flybody -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `f00f225670d6d9e246f216f5b7fa7d7f4c111009`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'd015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/build_fruitfly/assets/wing_left_brown.msh')` in `TuragaLab__flybody`. fatal: bad object d015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/build_fruitfly/assets/wing_left_brown.msh

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/TuragaLab__flybody -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `7c30f77473fc62c26a0b45a37878fc6e95576557`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'd015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/build_fruitfly/assets/antenna_left_body.msh')` in `TuragaLab__flybody`. fatal: bad object d015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/build_fruitfly/assets/antenna_left_body.msh

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/TuragaLab__flybody -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `c274dc87d520049f4c106af3437d141a7fad28de`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'd015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/build_fruitfly/assets/antenna_left_black.msh')` in `TuragaLab__flybody`. fatal: bad object d015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/build_fruitfly/assets/antenna_left_black.msh

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/TuragaLab__flybody -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `353f67a6107010f21839aad28f444ffdf9b50cd0`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'd015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/build_fruitfly/assets/haltere_left_body.msh')` in `TuragaLab__flybody`. fatal: bad object d015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/build_fruitfly/assets/haltere_left_body.msh

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/TuragaLab__flybody -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `bc4d52d1b1af0923b0eaee1ee2d04a029a0cf132`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'd015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/build_fruitfly/assets/labrum_right_lower.msh')` in `TuragaLab__flybody`. fatal: bad object d015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/build_fruitfly/assets/labrum_right_lower.msh

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/TuragaLab__flybody -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `b183450cc0c74e27449624d9d960cfb7a8b881cf`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'd015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/build_fruitfly/assets/wing_right_brown.msh')` in `TuragaLab__flybody`. fatal: bad object d015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/build_fruitfly/assets/wing_right_brown.msh

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/TuragaLab__flybody -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `ee5f18ec2032dd8756345b698428439440b8e689`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'd015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/build_fruitfly/assets/antenna_right_body.msh')` in `TuragaLab__flybody`. fatal: bad object d015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/build_fruitfly/assets/antenna_right_body.msh

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/TuragaLab__flybody -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `a0493295a9fa9095aa94c3c78c6d98c6aab7a424`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'd015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/build_fruitfly/assets/antenna_right_black.msh')` in `TuragaLab__flybody`. fatal: bad object d015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/build_fruitfly/assets/antenna_right_black.msh

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/TuragaLab__flybody -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `9a742a36a94e339ce1517b1fd4eeeec0ec6c377a`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'd015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/build_fruitfly/assets/haltere_right_body.msh')` in `TuragaLab__flybody`. fatal: bad object d015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/build_fruitfly/assets/haltere_right_body.msh

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/TuragaLab__flybody -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `545cbab095108b8ec6191c771381d2367ae03208`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'd015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/build_fruitfly/assets/thorax_body.msh')` in `TuragaLab__flybody`. fatal: bad object d015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/build_fruitfly/assets/thorax_body.msh

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/TuragaLab__flybody -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `31965586bcb55d9f36bee80ac0445f9e984c807b`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'd015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/build_fruitfly/assets/thorax_black.msh')` in `TuragaLab__flybody`. fatal: bad object d015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/build_fruitfly/assets/thorax_black.msh

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/TuragaLab__flybody -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `652ba9fc8158ec479c19f761b27edad4c7fe31bd`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'd015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/build_fruitfly/assets/abdomen_1_body.msh')` in `TuragaLab__flybody`. fatal: bad object d015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/build_fruitfly/assets/abdomen_1_body.msh

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/TuragaLab__flybody -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `6fd0e732f4a1dc9d8b6b288063e86b4f70d8f062`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'd015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/build_fruitfly/assets/abdomen_8_body.msh')` in `TuragaLab__flybody`. fatal: bad object d015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/build_fruitfly/assets/abdomen_8_body.msh

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/TuragaLab__flybody -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `e5c53f118653b1d548654c3b7b06900e8993f4e7`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'd015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/build_fruitfly/assets/tibia_T1_left_body.msh')` in `TuragaLab__flybody`. fatal: bad object d015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/build_fruitfly/assets/tibia_T1_left_body.msh

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/TuragaLab__flybody -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `0c6104c166c51db85a8bf1b7de9254da2f6bbe79`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'd015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/build_fruitfly/assets/tarsal_claw_T1_left_brown.msh')` in `TuragaLab__flybody`. fatal: bad object d015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/build_fruitfly/assets/tarsal_claw_T1_left_brown.msh

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/TuragaLab__flybody -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `104fa46fc43ae0f806e5e18d97b40bf29fed01de`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'd015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/build_fruitfly/assets/tarsal_claw_T2_left_brown.msh')` in `TuragaLab__flybody`. fatal: bad object d015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/build_fruitfly/assets/tarsal_claw_T2_left_brown.msh

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/TuragaLab__flybody -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `9fd8426aeedf48c3a2522d2c9b86feae0e93af66`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'd015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/build_fruitfly/assets/tarsus_T2_1_left_body.msh')` in `TuragaLab__flybody`. fatal: bad object d015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/build_fruitfly/assets/tarsus_T2_1_left_body.msh

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/TuragaLab__flybody -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `46ed4fb43eebbee296642d0c119a0a241418eb96`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'd015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/build_fruitfly/assets/tarsal_claw_T3_left_brown.msh')` in `TuragaLab__flybody`. fatal: bad object d015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/build_fruitfly/assets/tarsal_claw_T3_left_brown.msh

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/TuragaLab__flybody -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `4c224a0da45cf6466609147f74aa9cd08fdd656c`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'd015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/build_fruitfly/assets/tarsus_T3_1_left_body.msh')` in `TuragaLab__flybody`. fatal: bad object d015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/build_fruitfly/assets/tarsus_T3_1_left_body.msh

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/TuragaLab__flybody -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `5cf0ad6f86cb32a611601a9a8442b75a0d3b03d1`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'd015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/build_fruitfly/assets/tibia_T2_left_body.msh')` in `TuragaLab__flybody`. fatal: bad object d015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/build_fruitfly/assets/tibia_T2_left_body.msh

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/TuragaLab__flybody -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `ba38624c29ba054a12e5160a3b29f09e220b8f40`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'd015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/build_fruitfly/assets/tibia_T3_left_body.msh')` in `TuragaLab__flybody`. fatal: bad object d015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/build_fruitfly/assets/tibia_T3_left_body.msh

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/TuragaLab__flybody -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `c30f9d4f69deaa1d412079d6f365a8d368b95c77`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'd015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/build_fruitfly/assets/femur_T1_left_body.msh')` in `TuragaLab__flybody`. fatal: bad object d015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/build_fruitfly/assets/femur_T1_left_body.msh

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/TuragaLab__flybody -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `59d3fc7bed926daa7d0a5452c35ea4998f66f509`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'd015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/build_fruitfly/assets/femur_T2_left_body.msh')` in `TuragaLab__flybody`. fatal: bad object d015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/build_fruitfly/assets/femur_T2_left_body.msh

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/TuragaLab__flybody -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `cd49ae925953aaee3da07142c9d1e661d265b1ea`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'd015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/build_fruitfly/assets/femur_T3_left_body.msh')` in `TuragaLab__flybody`. fatal: bad object d015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/build_fruitfly/assets/femur_T3_left_body.msh

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/TuragaLab__flybody -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `a3ce197f74099f975cc8da0fd2a810428453da8a`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'd9415a3076f921fdb9735d45d609a596df722468:apptronik_apollo/CHANGELOG.md')` in `menagerie`. fatal: bad object d9415a3076f921fdb9735d45d609a596df722468:apptronik_apollo/CHANGELOG.md

- Offline Git read failed (exit 128): `('show', 'd9415a3076f921fdb9735d45d609a596df722468:berkeley_humanoid/CHANGELOG.md')` in `menagerie`. fatal: bad object d9415a3076f921fdb9735d45d609a596df722468:berkeley_humanoid/CHANGELOG.md

- Offline Git read failed (exit 128): `('show', 'd9415a3076f921fdb9735d45d609a596df722468:booster_t1/CHANGELOG.md')` in `menagerie`. fatal: bad object d9415a3076f921fdb9735d45d609a596df722468:booster_t1/CHANGELOG.md

- Offline Git read failed (exit 128): `('show', 'd9415a3076f921fdb9735d45d609a596df722468:fourier_n1/CHANGELOG.md')` in `menagerie`. fatal: bad object d9415a3076f921fdb9735d45d609a596df722468:fourier_n1/CHANGELOG.md

- Offline Git read failed (exit 128): `('show', 'fae9ee82330444eec4e87568c838b99a09a39467:rainbow_robotics_rby1/README.md')` in `menagerie`. fatal: path 'rainbow_robotics_rby1/README.md' does not exist in 'fae9ee82330444eec4e87568c838b99a09a39467'

- Offline Git read failed (exit 128): `('show', 'd9415a3076f921fdb9735d45d609a596df722468:unitree_g1/CHANGELOG.md')` in `menagerie`. fatal: bad object d9415a3076f921fdb9735d45d609a596df722468:unitree_g1/CHANGELOG.md

- https://github.com/TuragaLab/flybody flybody/fruitfly/build_fruitfly/fruitfly.xml at d015e9bfe441bd90ae431bac24c55cb74bdbce26: ValueError: Resource missing at d015e9bfe441bd90ae431bac24c55cb74bdbce26: flybody/fruitfly/build_fruitfly/head_body.obj

- https://github.com/TuragaLab/flybody flybody/fruitfly/build_fruitfly/floor.xml at d015e9bfe441bd90ae431bac24c55cb74bdbce26: ValueError: Resource missing at d015e9bfe441bd90ae431bac24c55cb74bdbce26: flybody/fruitfly/build_fruitfly/head_body.obj

- https://github.com/TuragaLab/flybody flybody/fruitfly/build_fruitfly/assets/drosophila.xml at d015e9bfe441bd90ae431bac24c55cb74bdbce26: ValueError: Resource missing at d015e9bfe441bd90ae431bac24c55cb74bdbce26: flybody/fruitfly/build_fruitfly/assets/assets/head_body.msh

- Offline Git read failed (exit 128): `('show', 'd015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/build_fruitfly/assets/femur_T1_right_body.msh')` in `TuragaLab__flybody`. fatal: bad object d015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/build_fruitfly/assets/femur_T1_right_body.msh

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/TuragaLab__flybody -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `0d385990b742b698f202132ece5f72a06ed535c8`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'd015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/build_fruitfly/assets/tibia_T1_right_body.msh')` in `TuragaLab__flybody`. fatal: bad object d015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/build_fruitfly/assets/tibia_T1_right_body.msh

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/TuragaLab__flybody -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `533335e263b2852f537fc2145c183b40cc810ab9`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'd015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/build_fruitfly/assets/tarsal_claw_T1_right_brown.msh')` in `TuragaLab__flybody`. fatal: bad object d015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/build_fruitfly/assets/tarsal_claw_T1_right_brown.msh

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/TuragaLab__flybody -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `51a8ce9020a95f83fa552a4c564bac9c5d355426`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'd015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/build_fruitfly/assets/femur_T2_right_body.msh')` in `TuragaLab__flybody`. fatal: bad object d015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/build_fruitfly/assets/femur_T2_right_body.msh

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/TuragaLab__flybody -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `2804b089fb4f0492ca5cc4684b04f0dbfd9fa302`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'd015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/build_fruitfly/assets/tibia_T2_right_body.msh')` in `TuragaLab__flybody`. fatal: bad object d015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/build_fruitfly/assets/tibia_T2_right_body.msh

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/TuragaLab__flybody -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `61ab8cf526524c75909ecbbe344d6e5622d815ec`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'd015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/build_fruitfly/assets/tarsus_T2_1_right_body.msh')` in `TuragaLab__flybody`. fatal: bad object d015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/build_fruitfly/assets/tarsus_T2_1_right_body.msh

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/TuragaLab__flybody -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `b49ee4c20a1a0f48a802fd92481508eaed5d686f`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'd015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/build_fruitfly/assets/tarsal_claw_T2_right_brown.msh')` in `TuragaLab__flybody`. fatal: bad object d015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/build_fruitfly/assets/tarsal_claw_T2_right_brown.msh

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/TuragaLab__flybody -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `bd8127c62abe147d6a32af1f97cbd21532880aaa`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'd015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/build_fruitfly/assets/femur_T3_right_body.msh')` in `TuragaLab__flybody`. fatal: bad object d015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/build_fruitfly/assets/femur_T3_right_body.msh

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/TuragaLab__flybody -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `93819cee022132025e4debc6f2b1940f80b10409`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'd015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/build_fruitfly/assets/tibia_T3_right_body.msh')` in `TuragaLab__flybody`. fatal: bad object d015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/build_fruitfly/assets/tibia_T3_right_body.msh

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/TuragaLab__flybody -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `8a5575a19d78dbe9247448f4e08e36370553d4e0`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'd015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/build_fruitfly/assets/tarsus_T3_1_right_body.msh')` in `TuragaLab__flybody`. fatal: bad object d015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/build_fruitfly/assets/tarsus_T3_1_right_body.msh

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/TuragaLab__flybody -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `45b35ea01a7e32d204c6fdef43c82e84876200c0`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'd015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/build_fruitfly/assets/tarsal_claw_T3_right_brown.msh')` in `TuragaLab__flybody`. fatal: bad object d015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/build_fruitfly/assets/tarsal_claw_T3_right_brown.msh

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/TuragaLab__flybody -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `f1a125410393a45313b527dadb0fe33017b59d9e`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'd015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/build_fruitfly/assets/coxa_T1_left_body.msh')` in `TuragaLab__flybody`. fatal: bad object d015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/build_fruitfly/assets/coxa_T1_left_body.msh

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/TuragaLab__flybody -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `9df055b0edec171d550030bf5f4594200764fd32`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'd015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/build_fruitfly/assets/coxa_T1_right_body.msh')` in `TuragaLab__flybody`. fatal: bad object d015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/build_fruitfly/assets/coxa_T1_right_body.msh

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/TuragaLab__flybody -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `990dd6c6092d49e00518e6229d945ef609482f4f`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'd015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/build_fruitfly/assets/coxa_T2_left_body.msh')` in `TuragaLab__flybody`. fatal: bad object d015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/build_fruitfly/assets/coxa_T2_left_body.msh

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/TuragaLab__flybody -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `ef693f0e2a48428d78e2c19761d5fbf1adb7aeb5`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'd015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/build_fruitfly/assets/coxa_T2_right_body.msh')` in `TuragaLab__flybody`. fatal: bad object d015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/build_fruitfly/assets/coxa_T2_right_body.msh

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/TuragaLab__flybody -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `98be03ac7dd1c560ed176565deb55e87d56f1415`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'd015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/build_fruitfly/assets/coxa_T3_left_body.msh')` in `TuragaLab__flybody`. fatal: bad object d015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/build_fruitfly/assets/coxa_T3_left_body.msh

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/TuragaLab__flybody -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `256dc0cc5881c3b909ea8b8ae5ff6be547c2a9fb`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'd015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/build_fruitfly/assets/coxa_T3_right_body.msh')` in `TuragaLab__flybody`. fatal: bad object d015e9bfe441bd90ae431bac24c55cb74bdbce26:flybody/fruitfly/build_fruitfly/assets/coxa_T3_right_body.msh

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/TuragaLab__flybody -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `3e7814a1fa971b4ffb403689b9b2300ca97f0660`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'd9415a3076f921fdb9735d45d609a596df722468:fourier_n1/n1.xml')` in `menagerie`. fatal: bad object d9415a3076f921fdb9735d45d609a596df722468:fourier_n1/n1.xml

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/menagerie -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `0f49cb3cb581b50e1e58e2841f4f918ca3a1b309`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '11da5a77d366eaeba52d83cc2c92ea61a29a487f:models/N1/mjcf/N1_raw.xml')` in `FFTAI__wiki-grx-mjcf`. fatal: path 'models/N1/mjcf/N1_raw.xml' does not exist in '11da5a77d366eaeba52d83cc2c92ea61a29a487f'

- Offline Git read failed (exit 128): `('rev-parse', '11da5a77d366eaeba52d83cc2c92ea61a29a487f:models/N1/mjcf/N1_raw.xml')` in `FFTAI__wiki-grx-mjcf`. fatal: path 'models/N1/mjcf/N1_raw.xml' does not exist in '11da5a77d366eaeba52d83cc2c92ea61a29a487f'

- Targeted fetch failed for https://github.com/FFTAI/wiki-grx-mjcf 11da5a77d366eaeba52d83cc2c92ea61a29a487f:models/N1/mjcf/N1_raw.xml: Command '['git', '-C', '.cache/FFTAI__wiki-grx-mjcf', 'rev-parse', '11da5a77d366eaeba52d83cc2c92ea61a29a487f:models/N1/mjcf/N1_raw.xml']' returned non-zero exit status 128.

- Historical source compile failed fourier_n1 11da5a77d366eaeba52d83cc2c92ea61a29a487f models/N1/mjcf/N1_raw.xml: Command '['git', '-C', '.cache/FFTAI__wiki-grx-mjcf', 'show', '11da5a77d366eaeba52d83cc2c92ea61a29a487f:models/N1/mjcf/N1_raw.xml']' returned non-zero exit status 128.

- https://github.com/frankaemika/franka_ros franka_gazebo/test/launch/panda-gazebo.urdf at ddd2fffd9de44b02ad15b4bbb2bfa2cec4d60d98: ValueError: Error: size 1 must be positive in geom
Element name '', id 0

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 clone --filter=blob:limit=100k --no-checkout https://github.com/frankaemika/franka_description.git .cache/frankaemika__franka_description` — retrieve manufacturer source history and small text files. Parent process runs at nice 15; lazy fetching disabled.

- Network outcome: exit 0. Cloning into '.cache/frankaemika__franka_description'...

- Offline Git read failed (exit 128): `('show', '7aeeddc449edf8d62b594f9e36a81da53e7796f9:meshes/robots/fr3/visual/link0.dae')` in `frankaemika__franka_description`. fatal: bad object 7aeeddc449edf8d62b594f9e36a81da53e7796f9:meshes/robots/fr3/visual/link0.dae

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/frankaemika__franka_description -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `e3f75601dce3657c7f65c77793ec553fe32dfcd2`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '7aeeddc449edf8d62b594f9e36a81da53e7796f9:meshes/robots/fr3/visual/link1.dae')` in `frankaemika__franka_description`. fatal: bad object 7aeeddc449edf8d62b594f9e36a81da53e7796f9:meshes/robots/fr3/visual/link1.dae

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/frankaemika__franka_description -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `95751998e1457610c9e7d2ab6df9aa4e7b0dfd8b`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '7aeeddc449edf8d62b594f9e36a81da53e7796f9:meshes/robots/fr3/visual/link2.dae')` in `frankaemika__franka_description`. fatal: bad object 7aeeddc449edf8d62b594f9e36a81da53e7796f9:meshes/robots/fr3/visual/link2.dae

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/frankaemika__franka_description -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `76cdf49c521ab2bb14874b8e72b42d092bf30947`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '7aeeddc449edf8d62b594f9e36a81da53e7796f9:meshes/robots/fr3/visual/link3.dae')` in `frankaemika__franka_description`. fatal: bad object 7aeeddc449edf8d62b594f9e36a81da53e7796f9:meshes/robots/fr3/visual/link3.dae

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/frankaemika__franka_description -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `e165aa32e9f5e659d297823dcdb1399915c77948`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '7aeeddc449edf8d62b594f9e36a81da53e7796f9:meshes/robots/fr3/visual/link4.dae')` in `frankaemika__franka_description`. fatal: bad object 7aeeddc449edf8d62b594f9e36a81da53e7796f9:meshes/robots/fr3/visual/link4.dae

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/frankaemika__franka_description -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `c78787e55e04ae3c8cff829c9b529fb0708fc2b5`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '7aeeddc449edf8d62b594f9e36a81da53e7796f9:meshes/robots/fr3/visual/link5.dae')` in `frankaemika__franka_description`. fatal: bad object 7aeeddc449edf8d62b594f9e36a81da53e7796f9:meshes/robots/fr3/visual/link5.dae

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/frankaemika__franka_description -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `9a0a3db436c4cb9f4f6c154c1c0022108d973651`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '7aeeddc449edf8d62b594f9e36a81da53e7796f9:meshes/robots/fr3/visual/link6.dae')` in `frankaemika__franka_description`. fatal: bad object 7aeeddc449edf8d62b594f9e36a81da53e7796f9:meshes/robots/fr3/visual/link6.dae

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/frankaemika__franka_description -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `d99955ad42ebbadd5596b724cd8e84d7776867e5`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '7aeeddc449edf8d62b594f9e36a81da53e7796f9:meshes/robots/fr3/visual/link7.dae')` in `frankaemika__franka_description`. fatal: bad object 7aeeddc449edf8d62b594f9e36a81da53e7796f9:meshes/robots/fr3/visual/link7.dae

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/frankaemika__franka_description -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `05d6a9548a8db8971b7181d7cda5711ef1e32d93`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '7aeeddc449edf8d62b594f9e36a81da53e7796f9:meshes/robot_ee/franka_hand_white/visual/hand.dae')` in `frankaemika__franka_description`. fatal: bad object 7aeeddc449edf8d62b594f9e36a81da53e7796f9:meshes/robot_ee/franka_hand_white/visual/hand.dae

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/frankaemika__franka_description -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `5f3667d4804f13702d5775ba97e77145bda1a736`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '7aeeddc449edf8d62b594f9e36a81da53e7796f9:meshes/robots/fr3v2/visual/link0.dae')` in `frankaemika__franka_description`. fatal: bad object 7aeeddc449edf8d62b594f9e36a81da53e7796f9:meshes/robots/fr3v2/visual/link0.dae

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/frankaemika__franka_description -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `32ceb428a1258ba65c9bac18f114fe89515e495e`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '7aeeddc449edf8d62b594f9e36a81da53e7796f9:meshes/robots/fr3v2/visual/link1.dae')` in `frankaemika__franka_description`. fatal: bad object 7aeeddc449edf8d62b594f9e36a81da53e7796f9:meshes/robots/fr3v2/visual/link1.dae

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/frankaemika__franka_description -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `fbbe716aacc0cf03acc207053e083b322a4d672a`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '7aeeddc449edf8d62b594f9e36a81da53e7796f9:meshes/robots/fr3v2/visual/link2.dae')` in `frankaemika__franka_description`. fatal: bad object 7aeeddc449edf8d62b594f9e36a81da53e7796f9:meshes/robots/fr3v2/visual/link2.dae

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/frankaemika__franka_description -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `1ab745e1cda590fb940ac8f476986ec0342debcf`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '7aeeddc449edf8d62b594f9e36a81da53e7796f9:meshes/robots/fr3v2/visual/link3.dae')` in `frankaemika__franka_description`. fatal: bad object 7aeeddc449edf8d62b594f9e36a81da53e7796f9:meshes/robots/fr3v2/visual/link3.dae

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/frankaemika__franka_description -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `adb698952d313d32e8718344f4ef93a78bab4004`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '7aeeddc449edf8d62b594f9e36a81da53e7796f9:meshes/robots/fr3v2/visual/link4.dae')` in `frankaemika__franka_description`. fatal: bad object 7aeeddc449edf8d62b594f9e36a81da53e7796f9:meshes/robots/fr3v2/visual/link4.dae

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/frankaemika__franka_description -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `96ef7c8c9ce00b8922505190a57a0e4852a70670`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '7aeeddc449edf8d62b594f9e36a81da53e7796f9:meshes/robots/fr3v2/visual/link5.dae')` in `frankaemika__franka_description`. fatal: bad object 7aeeddc449edf8d62b594f9e36a81da53e7796f9:meshes/robots/fr3v2/visual/link5.dae

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/frankaemika__franka_description -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `6a1ab3e5027ea702b35897d2f2fd01aa404b1901`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '7aeeddc449edf8d62b594f9e36a81da53e7796f9:meshes/robots/fr3v2/visual/link6.dae')` in `frankaemika__franka_description`. fatal: bad object 7aeeddc449edf8d62b594f9e36a81da53e7796f9:meshes/robots/fr3v2/visual/link6.dae

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/frankaemika__franka_description -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `8966052d8ef7859862c1b3137bd0224fae4060db`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '7aeeddc449edf8d62b594f9e36a81da53e7796f9:meshes/robots/fr3v2/visual/link7.dae')` in `frankaemika__franka_description`. fatal: bad object 7aeeddc449edf8d62b594f9e36a81da53e7796f9:meshes/robots/fr3v2/visual/link7.dae

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/frankaemika__franka_description -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `cd7a497621e47664abc89a2d3cadc94bb7528a11`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '7aeeddc449edf8d62b594f9e36a81da53e7796f9:meshes/accessories/fr3_duo_mount_v0_3/visual/fr3_duo_mount.dae')` in `frankaemika__franka_description`. fatal: bad object 7aeeddc449edf8d62b594f9e36a81da53e7796f9:meshes/accessories/fr3_duo_mount_v0_3/visual/fr3_duo_mount.dae

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/frankaemika__franka_description -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `08ab7654b36ea546f85b058be2f7d219fa03f3a1`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '7aeeddc449edf8d62b594f9e36a81da53e7796f9:meshes/accessories/fr3_duo_mount_v0_3/visual/fr3_duo_cover.dae')` in `frankaemika__franka_description`. fatal: bad object 7aeeddc449edf8d62b594f9e36a81da53e7796f9:meshes/accessories/fr3_duo_mount_v0_3/visual/fr3_duo_cover.dae

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/frankaemika__franka_description -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `12f168294441ca5bc39eb8c293d6e154aa197cad`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '7aeeddc449edf8d62b594f9e36a81da53e7796f9:meshes/accessories/franka_head_v0_2/visual/franka_head.dae')` in `frankaemika__franka_description`. fatal: bad object 7aeeddc449edf8d62b594f9e36a81da53e7796f9:meshes/accessories/franka_head_v0_2/visual/franka_head.dae

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/frankaemika__franka_description -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `c068423fe3138f30186820462597c37812578a42`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '7aeeddc449edf8d62b594f9e36a81da53e7796f9:meshes/robots/tmrv0_2/visual/tmrv0_2.dae')` in `frankaemika__franka_description`. fatal: bad object 7aeeddc449edf8d62b594f9e36a81da53e7796f9:meshes/robots/tmrv0_2/visual/tmrv0_2.dae

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/frankaemika__franka_description -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `80c658f53656250c740b6929c89a03fac6219af0`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '7aeeddc449edf8d62b594f9e36a81da53e7796f9:meshes/accessories/franka_spine_v0_1/visual/franka_spine.dae')` in `frankaemika__franka_description`. fatal: bad object 7aeeddc449edf8d62b594f9e36a81da53e7796f9:meshes/accessories/franka_spine_v0_1/visual/franka_spine.dae

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/frankaemika__franka_description -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `4dd2495106993fb7a4fe93d51b502fa9442e8142`

- Network outcome: exit 0.

- Historical source compile failed franka_fr3 7de996b30cef3bb97beadad2f3c5c751e8899f45 robots/fr3/fr3.urdf.xacro: mismatched tag: line 115, column 4

- Historical source compile failed franka_fr3 b7cba8117ba666c4237834d34ebf3a716b44d43d robots/fr3/fr3.urdf.xacro: mismatched tag: line 100, column 4

- Offline Git read failed (exit 128): `('show', '032e7ee892eee227bf80899a0cefe4d07d9808bb:meshes/robot_arms/fr3/visual/link0.dae')` in `frankaemika__franka_description`. fatal: bad object 032e7ee892eee227bf80899a0cefe4d07d9808bb:meshes/robot_arms/fr3/visual/link0.dae

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/frankaemika__franka_description -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `9e678422cdcdb70f17f92e87440b243590e89122`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '032e7ee892eee227bf80899a0cefe4d07d9808bb:meshes/robot_arms/fr3/visual/link1.dae')` in `frankaemika__franka_description`. fatal: bad object 032e7ee892eee227bf80899a0cefe4d07d9808bb:meshes/robot_arms/fr3/visual/link1.dae

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/frankaemika__franka_description -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `4ba4515b9cacd7d455a7f6c035f6f7bfbda68a17`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '032e7ee892eee227bf80899a0cefe4d07d9808bb:meshes/robot_arms/fr3/visual/link2.dae')` in `frankaemika__franka_description`. fatal: bad object 032e7ee892eee227bf80899a0cefe4d07d9808bb:meshes/robot_arms/fr3/visual/link2.dae

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/frankaemika__franka_description -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `2dad137798c4ca19ace2606deb6e49cf4b93012f`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '032e7ee892eee227bf80899a0cefe4d07d9808bb:meshes/robot_arms/fr3/visual/link3.dae')` in `frankaemika__franka_description`. fatal: bad object 032e7ee892eee227bf80899a0cefe4d07d9808bb:meshes/robot_arms/fr3/visual/link3.dae

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/frankaemika__franka_description -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `09716314751b966a12de84437949b40a13c62e81`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '032e7ee892eee227bf80899a0cefe4d07d9808bb:meshes/robot_arms/fr3/visual/link4.dae')` in `frankaemika__franka_description`. fatal: bad object 032e7ee892eee227bf80899a0cefe4d07d9808bb:meshes/robot_arms/fr3/visual/link4.dae

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/frankaemika__franka_description -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `f0bdabf0c56fb642c13976d5600038f2de567e1d`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '032e7ee892eee227bf80899a0cefe4d07d9808bb:meshes/robot_arms/fr3/visual/link5.dae')` in `frankaemika__franka_description`. fatal: bad object 032e7ee892eee227bf80899a0cefe4d07d9808bb:meshes/robot_arms/fr3/visual/link5.dae

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/frankaemika__franka_description -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `8eee1ae8f070e337894bd265885906c9354a4cd6`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '032e7ee892eee227bf80899a0cefe4d07d9808bb:meshes/robot_arms/fr3/visual/link6.dae')` in `frankaemika__franka_description`. fatal: bad object 032e7ee892eee227bf80899a0cefe4d07d9808bb:meshes/robot_arms/fr3/visual/link6.dae

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/frankaemika__franka_description -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `e3df00e9554c542b28ff2c31f1ba3dbcebbeffb1`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '032e7ee892eee227bf80899a0cefe4d07d9808bb:meshes/robot_arms/fr3/visual/link7.dae')` in `frankaemika__franka_description`. fatal: bad object 032e7ee892eee227bf80899a0cefe4d07d9808bb:meshes/robot_arms/fr3/visual/link7.dae

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/frankaemika__franka_description -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `da04ac196a5f75b4f4154e45dbefd1534fe08324`

- Network outcome: exit 0.

- Historical source compile failed franka_fr3 068f0b8ffe9665d0cd4a5e45274c663864c598c5 robots/fr3/fr3.urdf.xacro: Error: inertia must satisfy A + B >= C; use 'balanceinertia' to fix
Element name 'fr3_link2', id 4

- Offline Git read failed (exit 128): `('show', 'd5e8927aae7a100909753bb747799c663a2f4afd:meshes/robot_arms/fr3/visual/link0.dae')` in `frankaemika__franka_description`. fatal: bad object d5e8927aae7a100909753bb747799c663a2f4afd:meshes/robot_arms/fr3/visual/link0.dae

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/frankaemika__franka_description -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `cd741644a72739fb8cc726d3a31d6fb79f2a3f38`

- Network outcome: exit 0.

- Historical source compile failed franka_fr3 d5e8927aae7a100909753bb747799c663a2f4afd robots/fr3/fr3.urdf.xacro: DaeMalformedError: XML Parsing Error: XML declaration allowed only at the start of the document, line 25, column 6 (<string>, line 25)

- Historical source compile failed franka_fr3 b51da21a28af2cd27c028e61cbf328458e8a90f0 robots/fr3/fr3.urdf.xacro: DaeMalformedError: XML Parsing Error: XML declaration allowed only at the start of the document, line 25, column 6 (<string>, line 25)

- Historical source compile failed franka_fr3 1ddff9ba71abb199fb349ffcc3155e86cfdb094e robots/fr3/fr3.urdf.xacro: DaeMalformedError: XML Parsing Error: XML declaration allowed only at the start of the document, line 25, column 6 (<string>, line 25)

- Offline Git read failed (exit 128): `('show', '370c43965323c0944b433b202aac5058b5f907a9:franka_fr3_duo/assets/fr3_duo_mount.obj')` in `menagerie`. fatal: bad object 370c43965323c0944b433b202aac5058b5f907a9:franka_fr3_duo/assets/fr3_duo_mount.obj

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/menagerie -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `68731982c7d5e2e4bdfa2fd2e971b862a9dd1d09`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '370c43965323c0944b433b202aac5058b5f907a9:franka_fr3_duo/assets/franka_head.obj')` in `menagerie`. fatal: bad object 370c43965323c0944b433b202aac5058b5f907a9:franka_fr3_duo/assets/franka_head.obj

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/menagerie -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `25f92dc70037492a0ea0dfeadc49bd13e5add418`

- Network outcome: exit 0.

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 clone --filter=blob:limit=100k --no-checkout https://github.com/frankarobotics/franka_description.git .cache/frankarobotics__franka_description` — retrieve manufacturer source history and small text files. Parent process runs at nice 15; lazy fetching disabled.

- Network outcome: exit 0. Cloning into '.cache/frankarobotics__franka_description'...

- Offline Git read failed (exit 128): `('show', '7aeeddc449edf8d62b594f9e36a81da53e7796f9:meshes/accessories/fr3_duo_mount_v0_3/visual/fr3_duo_mount.dae')` in `frankarobotics__franka_description`. fatal: bad object 7aeeddc449edf8d62b594f9e36a81da53e7796f9:meshes/accessories/fr3_duo_mount_v0_3/visual/fr3_duo_mount.dae

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/frankarobotics__franka_description -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `08ab7654b36ea546f85b058be2f7d219fa03f3a1`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '7aeeddc449edf8d62b594f9e36a81da53e7796f9:meshes/accessories/fr3_duo_mount_v0_3/visual/fr3_duo_cover.dae')` in `frankarobotics__franka_description`. fatal: bad object 7aeeddc449edf8d62b594f9e36a81da53e7796f9:meshes/accessories/fr3_duo_mount_v0_3/visual/fr3_duo_cover.dae

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/frankarobotics__franka_description -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `12f168294441ca5bc39eb8c293d6e154aa197cad`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '7aeeddc449edf8d62b594f9e36a81da53e7796f9:meshes/accessories/franka_head_v0_2/visual/franka_head.dae')` in `frankarobotics__franka_description`. fatal: bad object 7aeeddc449edf8d62b594f9e36a81da53e7796f9:meshes/accessories/franka_head_v0_2/visual/franka_head.dae

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/frankarobotics__franka_description -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `c068423fe3138f30186820462597c37812578a42`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '7aeeddc449edf8d62b594f9e36a81da53e7796f9:meshes/robots/fr3v2/visual/link0.dae')` in `frankarobotics__franka_description`. fatal: bad object 7aeeddc449edf8d62b594f9e36a81da53e7796f9:meshes/robots/fr3v2/visual/link0.dae

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/frankarobotics__franka_description -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `32ceb428a1258ba65c9bac18f114fe89515e495e`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '7aeeddc449edf8d62b594f9e36a81da53e7796f9:meshes/robots/fr3v2/visual/link1.dae')` in `frankarobotics__franka_description`. fatal: bad object 7aeeddc449edf8d62b594f9e36a81da53e7796f9:meshes/robots/fr3v2/visual/link1.dae

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/frankarobotics__franka_description -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `fbbe716aacc0cf03acc207053e083b322a4d672a`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '7aeeddc449edf8d62b594f9e36a81da53e7796f9:meshes/robots/fr3v2/visual/link2.dae')` in `frankarobotics__franka_description`. fatal: bad object 7aeeddc449edf8d62b594f9e36a81da53e7796f9:meshes/robots/fr3v2/visual/link2.dae

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/frankarobotics__franka_description -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `1ab745e1cda590fb940ac8f476986ec0342debcf`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '7aeeddc449edf8d62b594f9e36a81da53e7796f9:meshes/robots/fr3v2/visual/link3.dae')` in `frankarobotics__franka_description`. fatal: bad object 7aeeddc449edf8d62b594f9e36a81da53e7796f9:meshes/robots/fr3v2/visual/link3.dae

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/frankarobotics__franka_description -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `adb698952d313d32e8718344f4ef93a78bab4004`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '7aeeddc449edf8d62b594f9e36a81da53e7796f9:meshes/robots/fr3v2/visual/link4.dae')` in `frankarobotics__franka_description`. fatal: bad object 7aeeddc449edf8d62b594f9e36a81da53e7796f9:meshes/robots/fr3v2/visual/link4.dae

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/frankarobotics__franka_description -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `96ef7c8c9ce00b8922505190a57a0e4852a70670`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '7aeeddc449edf8d62b594f9e36a81da53e7796f9:meshes/robots/fr3v2/visual/link5.dae')` in `frankarobotics__franka_description`. fatal: bad object 7aeeddc449edf8d62b594f9e36a81da53e7796f9:meshes/robots/fr3v2/visual/link5.dae

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/frankarobotics__franka_description -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `6a1ab3e5027ea702b35897d2f2fd01aa404b1901`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '7aeeddc449edf8d62b594f9e36a81da53e7796f9:meshes/robots/fr3v2/visual/link6.dae')` in `frankarobotics__franka_description`. fatal: bad object 7aeeddc449edf8d62b594f9e36a81da53e7796f9:meshes/robots/fr3v2/visual/link6.dae

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/frankarobotics__franka_description -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `8966052d8ef7859862c1b3137bd0224fae4060db`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '7aeeddc449edf8d62b594f9e36a81da53e7796f9:meshes/robots/fr3v2/visual/link7.dae')` in `frankarobotics__franka_description`. fatal: bad object 7aeeddc449edf8d62b594f9e36a81da53e7796f9:meshes/robots/fr3v2/visual/link7.dae

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/frankarobotics__franka_description -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `cd7a497621e47664abc89a2d3cadc94bb7528a11`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '7aeeddc449edf8d62b594f9e36a81da53e7796f9:meshes/robot_ee/franka_hand_white/visual/hand.dae')` in `frankarobotics__franka_description`. fatal: bad object 7aeeddc449edf8d62b594f9e36a81da53e7796f9:meshes/robot_ee/franka_hand_white/visual/hand.dae

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/frankarobotics__franka_description -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `5f3667d4804f13702d5775ba97e77145bda1a736`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '27dca8a406ae48996e0460f3263192e82f51cc03:meshes/robots/fr3/visual/link0.dae')` in `frankarobotics__franka_description`. fatal: bad object 27dca8a406ae48996e0460f3263192e82f51cc03:meshes/robots/fr3/visual/link0.dae

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/frankarobotics__franka_description -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `e3f75601dce3657c7f65c77793ec553fe32dfcd2`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '27dca8a406ae48996e0460f3263192e82f51cc03:meshes/robots/fr3/visual/link1.dae')` in `frankarobotics__franka_description`. fatal: bad object 27dca8a406ae48996e0460f3263192e82f51cc03:meshes/robots/fr3/visual/link1.dae

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/frankarobotics__franka_description -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `95751998e1457610c9e7d2ab6df9aa4e7b0dfd8b`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '27dca8a406ae48996e0460f3263192e82f51cc03:meshes/robots/fr3/visual/link2.dae')` in `frankarobotics__franka_description`. fatal: bad object 27dca8a406ae48996e0460f3263192e82f51cc03:meshes/robots/fr3/visual/link2.dae

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/frankarobotics__franka_description -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `76cdf49c521ab2bb14874b8e72b42d092bf30947`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '27dca8a406ae48996e0460f3263192e82f51cc03:meshes/robots/fr3/visual/link3.dae')` in `frankarobotics__franka_description`. fatal: bad object 27dca8a406ae48996e0460f3263192e82f51cc03:meshes/robots/fr3/visual/link3.dae

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/frankarobotics__franka_description -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `e165aa32e9f5e659d297823dcdb1399915c77948`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '27dca8a406ae48996e0460f3263192e82f51cc03:meshes/robots/fr3/visual/link4.dae')` in `frankarobotics__franka_description`. fatal: bad object 27dca8a406ae48996e0460f3263192e82f51cc03:meshes/robots/fr3/visual/link4.dae

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/frankarobotics__franka_description -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `c78787e55e04ae3c8cff829c9b529fb0708fc2b5`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '27dca8a406ae48996e0460f3263192e82f51cc03:meshes/robots/fr3/visual/link5.dae')` in `frankarobotics__franka_description`. fatal: bad object 27dca8a406ae48996e0460f3263192e82f51cc03:meshes/robots/fr3/visual/link5.dae

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/frankarobotics__franka_description -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `9a0a3db436c4cb9f4f6c154c1c0022108d973651`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '27dca8a406ae48996e0460f3263192e82f51cc03:meshes/robots/fr3/visual/link6.dae')` in `frankarobotics__franka_description`. fatal: bad object 27dca8a406ae48996e0460f3263192e82f51cc03:meshes/robots/fr3/visual/link6.dae

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/frankarobotics__franka_description -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `d99955ad42ebbadd5596b724cd8e84d7776867e5`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '27dca8a406ae48996e0460f3263192e82f51cc03:meshes/robots/fr3/visual/link7.dae')` in `frankarobotics__franka_description`. fatal: bad object 27dca8a406ae48996e0460f3263192e82f51cc03:meshes/robots/fr3/visual/link7.dae

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/frankarobotics__franka_description -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `05d6a9548a8db8971b7181d7cda5711ef1e32d93`

- Network outcome: exit 0.

- Historical source compile failed franka_fr3_duo f4fa7e5aa00908b9ef244ca6edeea861cf40c9fb robots/fr3_duo/fr3_duo.urdf.xacro: Undefined substitution argument kinematics_path'
when evaluating expression 'xacro.load_yaml('$(arg kinematics_path')'

- Historical source compile failed franka_fr3_duo 3bad514b1aa6a9ee46c47f806805bfb3fc993bd6 robots/fr3_duo/fr3_duo.urdf.xacro: Undefined substitution argument kinematics_path'
when evaluating expression 'xacro.load_yaml('$(arg kinematics_path')'

- Offline Git read failed (exit 128): `('show', '467e282f23c46ae4b2abf6771647aa5ac9366b22:meshes/robot_arms/fr3_duo/cover/visual/fr3_duo_cover.dae')` in `frankarobotics__franka_description`. fatal: bad object 467e282f23c46ae4b2abf6771647aa5ac9366b22:meshes/robot_arms/fr3_duo/cover/visual/fr3_duo_cover.dae

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/frankarobotics__franka_description -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `9a2bee68ffbae0474b69ae78834ac7d813f5e0be`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '370c43965323c0944b433b202aac5058b5f907a9:hello_robot_stretch/assets/base_link_8.obj')` in `menagerie`. fatal: bad object 370c43965323c0944b433b202aac5058b5f907a9:hello_robot_stretch/assets/base_link_8.obj

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/menagerie -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `5bb465a31c27edea7e544e7ad4a96a3d6e7b4810`

- Network outcome: exit 0.

- Menagerie self-comparison compile failed: hello_robot_stretch/stretch.xml: ValueError: Error: texture 'hand_crush' not found in material 18
Element name 'Hand_Crush_Sticker', id 18, line 90

- Menagerie self-comparison compile failed: hello_robot_stretch_3/stretch.xml: ValueError: Error: texture 'hand_crush' not found in material 19
Element name 'Hand_Crush_Sticker', id 19, line 109

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 clone --filter=blob:limit=100k --no-checkout https://github.com/i2rt-robotics/i2rt.git .cache/i2rt-robotics__i2rt` — retrieve manufacturer source history and small text files. Parent process runs at nice 15; lazy fetching disabled.

- Network outcome: exit 0. Cloning into '.cache/i2rt-robotics__i2rt'...

- Offline Git read failed (exit 128): `('show', 'c3280d8a6a6b5d96590d51538e3f265710a6c77d:kortex_description/arms/gen3/7dof/meshes/base_link.STL')` in `Kinovarobotics__ros_kortex`. fatal: bad object c3280d8a6a6b5d96590d51538e3f265710a6c77d:kortex_description/arms/gen3/7dof/meshes/base_link.STL

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/Kinovarobotics__ros_kortex -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `0a35a8ae68fa0b8d24507f2cd2a142a59b8fc91e`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'c3280d8a6a6b5d96590d51538e3f265710a6c77d:kortex_description/arms/gen3/7dof/meshes/shoulder_link.STL')` in `Kinovarobotics__ros_kortex`. fatal: bad object c3280d8a6a6b5d96590d51538e3f265710a6c77d:kortex_description/arms/gen3/7dof/meshes/shoulder_link.STL

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/Kinovarobotics__ros_kortex -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `69ecb7695c73980fa9e76563d5a66fca373db44a`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'c3280d8a6a6b5d96590d51538e3f265710a6c77d:kortex_description/arms/gen3/7dof/meshes/half_arm_1_link.STL')` in `Kinovarobotics__ros_kortex`. fatal: bad object c3280d8a6a6b5d96590d51538e3f265710a6c77d:kortex_description/arms/gen3/7dof/meshes/half_arm_1_link.STL

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/Kinovarobotics__ros_kortex -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `1df304c0eb9e8630f3be09b39154c1955ad0771b`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'c3280d8a6a6b5d96590d51538e3f265710a6c77d:kortex_description/arms/gen3/7dof/meshes/half_arm_2_link.STL')` in `Kinovarobotics__ros_kortex`. fatal: bad object c3280d8a6a6b5d96590d51538e3f265710a6c77d:kortex_description/arms/gen3/7dof/meshes/half_arm_2_link.STL

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/Kinovarobotics__ros_kortex -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `78bc722ab2d8ac217b57dc2b85860a9597c771ee`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'c3280d8a6a6b5d96590d51538e3f265710a6c77d:kortex_description/arms/gen3/7dof/meshes/forearm_link.STL')` in `Kinovarobotics__ros_kortex`. fatal: bad object c3280d8a6a6b5d96590d51538e3f265710a6c77d:kortex_description/arms/gen3/7dof/meshes/forearm_link.STL

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/Kinovarobotics__ros_kortex -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `ac791a3548a21d8ae1650b4b14d173605e6f85bb`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'c3280d8a6a6b5d96590d51538e3f265710a6c77d:kortex_description/arms/gen3/7dof/meshes/spherical_wrist_1_link.STL')` in `Kinovarobotics__ros_kortex`. fatal: bad object c3280d8a6a6b5d96590d51538e3f265710a6c77d:kortex_description/arms/gen3/7dof/meshes/spherical_wrist_1_link.STL

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/Kinovarobotics__ros_kortex -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `3bbf04a6de017405f402d8b95c3b22d441389a57`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'c3280d8a6a6b5d96590d51538e3f265710a6c77d:kortex_description/arms/gen3/7dof/meshes/spherical_wrist_2_link.STL')` in `Kinovarobotics__ros_kortex`. fatal: bad object c3280d8a6a6b5d96590d51538e3f265710a6c77d:kortex_description/arms/gen3/7dof/meshes/spherical_wrist_2_link.STL

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/Kinovarobotics__ros_kortex -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `14bbff58f2f200dd1e1b97ba5226da3f768b69e4`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'c3280d8a6a6b5d96590d51538e3f265710a6c77d:kortex_description/arms/gen3/7dof/meshes/bracelet_with_vision_link.STL')` in `Kinovarobotics__ros_kortex`. fatal: bad object c3280d8a6a6b5d96590d51538e3f265710a6c77d:kortex_description/arms/gen3/7dof/meshes/bracelet_with_vision_link.STL

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/Kinovarobotics__ros_kortex -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `146b69b50b2fd61546c3dc7a4860a037874f084e`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'f5e7132f22108164577fea4c25ef99b5cc0e1900:robots/hands/leap_hand/meshes/visual/palm_lower_left.glb')` in `dexsuite__dex-urdf`. fatal: bad object f5e7132f22108164577fea4c25ef99b5cc0e1900:robots/hands/leap_hand/meshes/visual/palm_lower_left.glb

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/dexsuite__dex-urdf -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `0eb5968c555302d7b84addad54e5ca270be80801`

- Network outcome: exit 0.

- https://github.com/dexsuite/dex-urdf robots/hands/leap_hand/leap_hand_left_glb.urdf at f5e7132f22108164577fea4c25ef99b5cc0e1900: ValueError: Error: unknown or unsupported mesh file: 'resource_10.glb'
Element name 'resource_10', id 0

- https://github.com/dexsuite/dex-urdf robots/hands/leap_hand/leap_hand_right_glb.urdf at f5e7132f22108164577fea4c25ef99b5cc0e1900: ValueError: Error: unknown or unsupported mesh file: 'resource_10.glb'
Element name 'resource_10', id 0

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 clone --filter=blob:limit=100k --no-checkout https://github.com/s1lent4gnt/koch-v1-1.git .cache/s1lent4gnt__koch-v1-1` — retrieve manufacturer source history and small text files. Parent process runs at nice 15; lazy fetching disabled.

- Network outcome: exit 0. Cloning into '.cache/s1lent4gnt__koch-v1-1'...

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 clone --filter=blob:limit=100k --no-checkout https://github.com/AlexanderKoch-Koch/low_cost_robot.git .cache/AlexanderKoch-Koch__low_cost_robot` — retrieve manufacturer source history and small text files. Parent process runs at nice 15; lazy fetching disabled.

- Network outcome: exit 0. Cloning into '.cache/AlexanderKoch-Koch__low_cost_robot'...

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 clone --filter=blob:limit=100k --no-checkout https://github.com/jess-moss/koch-v1-1.git .cache/jess-moss__koch-v1-1` — retrieve manufacturer source history and small text files. Parent process runs at nice 15; lazy fetching disabled.

- Network outcome: exit 0. Cloning into '.cache/jess-moss__koch-v1-1'...

- Menagerie self-comparison compile failed: ms_human_700/MS-Human-700-Locomotion.xml: ValueError: Resource missing at 370c43965323c0944b433b202aac5058b5f907a9: geometry/sacrum.stl

- Menagerie self-comparison compile failed: ms_human_700/MS-Human-700-Manipulation.xml: ValueError: Resource missing at 370c43965323c0944b433b202aac5058b5f907a9: geometry/sacrum.stl

- Menagerie self-comparison compile failed: ms_human_700/MS-Human-700.xml: ValueError: Resource missing at 370c43965323c0944b433b202aac5058b5f907a9: geometry/sacrum.stl

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 clone --filter=blob:limit=100k --no-checkout https://github.com/pal-robotics/talos_robot.git .cache/pal-robotics__talos_robot` — retrieve manufacturer source history and small text files. Parent process runs at nice 15; lazy fetching disabled.

- Network outcome: exit 0. Cloning into '.cache/pal-robotics__talos_robot'...

- https://github.com/pal-robotics/talos_robot talos_description/robots/talos_full_v2.urdf.xacro at 79709aa4f4f453ec18a5e467e65f84ff58ea24d0: XacroException: No such file or directory: .cache/pal-robotics__talos_robot/.drift_xacro/tmp9ek636ay/.unresolved_package/pal_urdf_utils/urdf/deg_to_rad.urdf.xacro [Errno 2] No such file or directory: '.cache/pal-robotics__talos_robot/.drift_xacro/tmp9ek636ay/.unresolved_package/pal_urdf_utils/urdf/deg_to_rad.urdf.xacro'

- https://github.com/pal-robotics/talos_robot talos_description/robots/talos_arm_right.urdf.xacro at 79709aa4f4f453ec18a5e467e65f84ff58ea24d0: XacroException: No such file or directory: .cache/pal-robotics__talos_robot/.drift_xacro/tmpd1f6v72q/.unresolved_package/pal_urdf_utils/urdf/deg_to_rad.urdf.xacro [Errno 2] No such file or directory: '.cache/pal-robotics__talos_robot/.drift_xacro/tmpd1f6v72q/.unresolved_package/pal_urdf_utils/urdf/deg_to_rad.urdf.xacro'

- https://github.com/pal-robotics/talos_robot talos_description/urdf/talos_full_common.urdf.xacro at 79709aa4f4f453ec18a5e467e65f84ff58ea24d0: XacroException: No such file or directory: .cache/pal-robotics__talos_robot/.drift_xacro/tmp9h4nspii/.unresolved_package/pal_urdf_utils/urdf/deg_to_rad.urdf.xacro [Errno 2] No such file or directory: '.cache/pal-robotics__talos_robot/.drift_xacro/tmp9h4nspii/.unresolved_package/pal_urdf_utils/urdf/deg_to_rad.urdf.xacro'

- https://github.com/pal-robotics/talos_robot talos_description/robots/talos_lower_body.urdf.xacro at 79709aa4f4f453ec18a5e467e65f84ff58ea24d0: XacroException: No such file or directory: .cache/pal-robotics__talos_robot/.drift_xacro/tmp138mtm_p/.unresolved_package/pal_urdf_utils/urdf/ft_sensors/ati_talos.urdf.xacro [Errno 2] No such file or directory: '.cache/pal-robotics__talos_robot/.drift_xacro/tmp138mtm_p/.unresolved_package/pal_urdf_utils/urdf/ft_sensors/ati_talos.urdf.xacro'

- https://github.com/pal-robotics/talos_robot talos_description/robots/talos_full_no_grippers.urdf.xacro at 79709aa4f4f453ec18a5e467e65f84ff58ea24d0: XacroException: Undefined substitution argument enable_crane

- https://github.com/pal-robotics/talos_robot talos_description/robots/talos_full_fake_grippers.urdf.xacro at 79709aa4f4f453ec18a5e467e65f84ff58ea24d0: XacroException: Undefined substitution argument enable_crane

- https://github.com/pal-robotics/talos_robot talos_description/robots/talos_lower_body_torso_head.urdf.xacro at 79709aa4f4f453ec18a5e467e65f84ff58ea24d0: XacroException: Undefined substitution argument enable_crane

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 clone --filter=blob:limit=100k --no-checkout https://github.com/pal-robotics/tiago_robot.git .cache/pal-robotics__tiago_robot` — retrieve manufacturer source history and small text files. Parent process runs at nice 15; lazy fetching disabled.

- Network outcome: exit 0. Cloning into '.cache/pal-robotics__tiago_robot'...

- https://github.com/pal-robotics/tiago_robot tiago_description/robots/tiago.urdf.xacro at f1c33c92bdde7c1dd79f0c3e739e98a233dbd30b: XacroException: No such file or directory: .cache/pal-robotics__tiago_robot/.drift_xacro/tmpd2a1xwz8/.unresolved_package/pal_urdf_utils/urdf/deg_to_rad.urdf.xacro [Errno 2] No such file or directory: '.cache/pal-robotics__tiago_robot/.drift_xacro/tmpd2a1xwz8/.unresolved_package/pal_urdf_utils/urdf/deg_to_rad.urdf.xacro'

- https://github.com/pal-robotics/tiago_robot tiago_description/urdf/calibration/eye_hand_calibration.urdf.xacro at f1c33c92bdde7c1dd79f0c3e739e98a233dbd30b: XacroException: No such file or directory: .cache/pal-robotics__tiago_robot/.drift_xacro/tmp0k13uqew/.unresolved_package/pal_urdf_utils/urdf/deg_to_rad.urdf.xacro [Errno 2] No such file or directory: '.cache/pal-robotics__tiago_robot/.drift_xacro/tmp0k13uqew/.unresolved_package/pal_urdf_utils/urdf/deg_to_rad.urdf.xacro'

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 clone --filter=blob:limit=100k --no-checkout https://github.com/pal-robotics/tiago_dual_robot.git .cache/pal-robotics__tiago_dual_robot` — retrieve manufacturer source history and small text files. Parent process runs at nice 15; lazy fetching disabled.

- Network outcome: exit 0. Cloning into '.cache/pal-robotics__tiago_dual_robot'...

- https://github.com/pal-robotics/tiago_dual_robot tiago_dual_description/robots/tiago_dual.urdf.xacro at 687f44ed20fa35e7c6124b0cf3961b4f4aeb576d: XacroException: No such file or directory: .cache/pal-robotics__tiago_dual_robot/.drift_xacro/tmpyknxh_5m/.unresolved_package/pal_urdf_utils/urdf/deg_to_rad.urdf.xacro [Errno 2] No such file or directory: '.cache/pal-robotics__tiago_dual_robot/.drift_xacro/tmpyknxh_5m/.unresolved_package/pal_urdf_utils/urdf/deg_to_rad.urdf.xacro'

- https://github.com/pal-robotics/tiago_dual_robot tiago_dual_description/urdf/calibration/eye_hand_calibration.urdf.xacro at 687f44ed20fa35e7c6124b0cf3961b4f4aeb576d: XacroException: No such file or directory: .cache/pal-robotics__tiago_dual_robot/.drift_xacro/tmpazyp4tsl/.unresolved_package/pal_urdf_utils/urdf/deg_to_rad.urdf.xacro [Errno 2] No such file or directory: '.cache/pal-robotics__tiago_dual_robot/.drift_xacro/tmpazyp4tsl/.unresolved_package/pal_urdf_utils/urdf/deg_to_rad.urdf.xacro'

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 clone --filter=blob:limit=100k --no-checkout https://github.com/RainbowRobotics/rby1-sdk.git .cache/RainbowRobotics__rby1-sdk` — retrieve manufacturer source history and small text files. Parent process runs at nice 15; lazy fetching disabled.

- Network outcome: exit 0. Cloning into '.cache/RainbowRobotics__rby1-sdk'...

- Offline Git read failed (exit 128): `('show', '370c43965323c0944b433b202aac5058b5f907a9:realsense_d435i/assets/d435i_8.obj')` in `menagerie`. fatal: bad object 370c43965323c0944b433b202aac5058b5f907a9:realsense_d435i/assets/d435i_8.obj

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/menagerie -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `6c7bc6cfb34fa4bef32fcb3251cb8df1cb9d362d`

- Network outcome: exit 0.

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 clone --filter=blob:limit=100k --no-checkout https://github.com/IntelRealSense/realsense-ros.git .cache/IntelRealSense__realsense-ros` — retrieve manufacturer source history and small text files. Parent process runs at nice 15; lazy fetching disabled.

- Network outcome: exit 0. Cloning into '.cache/IntelRealSense__realsense-ros'...

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 clone --filter=blob:limit=100k --no-checkout https://github.com/RethinkRobotics/sawyer_robot.git .cache/RethinkRobotics__sawyer_robot` — retrieve manufacturer source history and small text files. Parent process runs at nice 15; lazy fetching disabled.

- Network outcome: exit 0. Cloning into '.cache/RethinkRobotics__sawyer_robot'...

- Offline Git read failed (exit 128): `('show', 'd1ef3d0ca83d0a943839783efd9b162e6930f2b7:sawyer_description/meshes/sawyer_pv/pedestal.DAE')` in `RethinkRobotics__sawyer_robot`. fatal: bad object d1ef3d0ca83d0a943839783efd9b162e6930f2b7:sawyer_description/meshes/sawyer_pv/pedestal.DAE

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/RethinkRobotics__sawyer_robot -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `469368870f6b8512392c51da9148dae9ff86f2cd`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'd1ef3d0ca83d0a943839783efd9b162e6930f2b7:sawyer_description/meshes/sawyer_pv/base.DAE')` in `RethinkRobotics__sawyer_robot`. fatal: bad object d1ef3d0ca83d0a943839783efd9b162e6930f2b7:sawyer_description/meshes/sawyer_pv/base.DAE

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/RethinkRobotics__sawyer_robot -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `bf5d904ca07d348063e1161912c0164cf8d029c2`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'd1ef3d0ca83d0a943839783efd9b162e6930f2b7:sawyer_description/meshes/sawyer_mp3/l0.DAE')` in `RethinkRobotics__sawyer_robot`. fatal: bad object d1ef3d0ca83d0a943839783efd9b162e6930f2b7:sawyer_description/meshes/sawyer_mp3/l0.DAE

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/RethinkRobotics__sawyer_robot -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `195317d12729ac1f9e9f6fc5def16d7426411f0c`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'd1ef3d0ca83d0a943839783efd9b162e6930f2b7:sawyer_description/meshes/sawyer_pv/head.DAE')` in `RethinkRobotics__sawyer_robot`. fatal: bad object d1ef3d0ca83d0a943839783efd9b162e6930f2b7:sawyer_description/meshes/sawyer_pv/head.DAE

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/RethinkRobotics__sawyer_robot -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `396dd1776d0c4f4de8d4482eefb6e4a6838173e3`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'd1ef3d0ca83d0a943839783efd9b162e6930f2b7:sawyer_description/meshes/sawyer_mp3/l1.DAE')` in `RethinkRobotics__sawyer_robot`. fatal: bad object d1ef3d0ca83d0a943839783efd9b162e6930f2b7:sawyer_description/meshes/sawyer_mp3/l1.DAE

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/RethinkRobotics__sawyer_robot -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `13151800ab7ca7a6f43627401818355cdb1362e2`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'd1ef3d0ca83d0a943839783efd9b162e6930f2b7:sawyer_description/meshes/sawyer_pv/l2.DAE')` in `RethinkRobotics__sawyer_robot`. fatal: bad object d1ef3d0ca83d0a943839783efd9b162e6930f2b7:sawyer_description/meshes/sawyer_pv/l2.DAE

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/RethinkRobotics__sawyer_robot -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `65cdbf0a55392a74c77ab7c8b1d13f7bca689e92`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'd1ef3d0ca83d0a943839783efd9b162e6930f2b7:sawyer_description/meshes/sawyer_pv/l3.DAE')` in `RethinkRobotics__sawyer_robot`. fatal: bad object d1ef3d0ca83d0a943839783efd9b162e6930f2b7:sawyer_description/meshes/sawyer_pv/l3.DAE

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/RethinkRobotics__sawyer_robot -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `5aa0068ffdef882889c60f39f275fc933020b362`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'd1ef3d0ca83d0a943839783efd9b162e6930f2b7:sawyer_description/meshes/sawyer_pv/l4.DAE')` in `RethinkRobotics__sawyer_robot`. fatal: bad object d1ef3d0ca83d0a943839783efd9b162e6930f2b7:sawyer_description/meshes/sawyer_pv/l4.DAE

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/RethinkRobotics__sawyer_robot -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `c26a0186274eee46d2fe7837a5ca6ca10ab1d846`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'd1ef3d0ca83d0a943839783efd9b162e6930f2b7:sawyer_description/meshes/sawyer_pv/l5.DAE')` in `RethinkRobotics__sawyer_robot`. fatal: bad object d1ef3d0ca83d0a943839783efd9b162e6930f2b7:sawyer_description/meshes/sawyer_pv/l5.DAE

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/RethinkRobotics__sawyer_robot -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `d891f6235d7fd83530258f91c2bcbd533524d49d`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'd1ef3d0ca83d0a943839783efd9b162e6930f2b7:sawyer_description/meshes/sawyer_mp1/l6.DAE')` in `RethinkRobotics__sawyer_robot`. fatal: bad object d1ef3d0ca83d0a943839783efd9b162e6930f2b7:sawyer_description/meshes/sawyer_mp1/l6.DAE

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/RethinkRobotics__sawyer_robot -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `4e8c1f75b1dc097112ae3bedc8d43513c4057914`

- Network outcome: exit 0.

- https://github.com/RethinkRobotics/sawyer_robot sawyer_description/urdf/sawyer.urdf.xacro at d1ef3d0ca83d0a943839783efd9b162e6930f2b7: ValueError: Error: error 'inertia must have positive eigenvalues' in fullinertia
Element name 'right_hand', id 20

- https://github.com/RethinkRobotics/sawyer_robot sawyer_description/urdf/sawyer_base.urdf.xacro at d1ef3d0ca83d0a943839783efd9b162e6930f2b7: ValueError: Error: error 'inertia must have positive eigenvalues' in fullinertia
Element name 'right_hand', id 20

- https://github.com/RethinkRobotics/sawyer_robot sawyer_description/urdf/sawyer_base.gazebo.xacro at d1ef3d0ca83d0a943839783efd9b162e6930f2b7: ValueError: XML Error: URDF joint parent or child missing
Element 'joint', line 1


- https://github.com/RethinkRobotics/sawyer_robot sawyer_description/urdf/sawyer_electric_gripper.urdf.xacro at d1ef3d0ca83d0a943839783efd9b162e6930f2b7: XacroException: No such file or directory: .cache/RethinkRobotics__sawyer_robot/.drift_xacro/tmpebhov2n1/.unresolved_package/intera_tools_description/urdf/electric_gripper/rethink_electric_gripper.xacro [Errno 2] No such file or directory: '.cache/RethinkRobotics__sawyer_robot/.drift_xacro/tmpebhov2n1/.unresolved_package/intera_tools_description/urdf/electric_gripper/rethink_electric_gripper.xacro'

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 clone --filter=blob:limit=100k --no-checkout https://github.com/ros-industrial/robotiq.git .cache/ros-industrial__robotiq` — retrieve manufacturer source history and small text files. Parent process runs at nice 15; lazy fetching disabled.

- Network outcome: exit 0. Cloning into '.cache/ros-industrial__robotiq'...

- Offline Git read failed (exit 128): `('show', '45196f6558fe8ba9d89bc8a105396c68c3e7e892:robotiq_2f_85_gripper_visualization/meshes/visual/robotiq_arg2f_85_base_link.dae')` in `ros-industrial__robotiq`. fatal: bad object 45196f6558fe8ba9d89bc8a105396c68c3e7e892:robotiq_2f_85_gripper_visualization/meshes/visual/robotiq_arg2f_85_base_link.dae

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/ros-industrial__robotiq -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `df98eae4e5c480ac159ffe157c92d58fea2cd554`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '45196f6558fe8ba9d89bc8a105396c68c3e7e892:robotiq_2f_85_gripper_visualization/meshes/visual/robotiq_arg2f_85_outer_finger.dae')` in `ros-industrial__robotiq`. fatal: bad object 45196f6558fe8ba9d89bc8a105396c68c3e7e892:robotiq_2f_85_gripper_visualization/meshes/visual/robotiq_arg2f_85_outer_finger.dae

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/ros-industrial__robotiq -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `605018839ea5b0f67a67d02fa271f40161e10cec`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '45196f6558fe8ba9d89bc8a105396c68c3e7e892:robotiq_2f_85_gripper_visualization/meshes/visual/robotiq_arg2f_85_inner_finger.dae')` in `ros-industrial__robotiq`. fatal: bad object 45196f6558fe8ba9d89bc8a105396c68c3e7e892:robotiq_2f_85_gripper_visualization/meshes/visual/robotiq_arg2f_85_inner_finger.dae

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/ros-industrial__robotiq -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `e9322426f2d1d7e2312f20ed4a64e38aae77f46c`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '45196f6558fe8ba9d89bc8a105396c68c3e7e892:robotiq_2f_85_gripper_visualization/meshes/visual/robotiq_arg2f_85_inner_knuckle.dae')` in `ros-industrial__robotiq`. fatal: bad object 45196f6558fe8ba9d89bc8a105396c68c3e7e892:robotiq_2f_85_gripper_visualization/meshes/visual/robotiq_arg2f_85_inner_knuckle.dae

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/ros-industrial__robotiq -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `c58db533dcc9f51967fbc3d99c5e8a551d010eb9`

- Network outcome: exit 0.

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 clone --filter=blob:limit=100k --no-checkout https://github.com/ROBOTIS-GIT/open_manipulator.git .cache/ROBOTIS-GIT__open_manipulator` — retrieve manufacturer source history and small text files. Parent process runs at nice 15; lazy fetching disabled.

- Network outcome: exit 0. Cloning into '.cache/ROBOTIS-GIT__open_manipulator'...

- Offline Git read failed (exit 128): `('show', 'cb946894a8b5d242d2d4e012f93f01eecac5a3ce:open_manipulator_description/meshes/omy_3m/base_unit.stl')` in `ROBOTIS-GIT__open_manipulator`. fatal: bad object cb946894a8b5d242d2d4e012f93f01eecac5a3ce:open_manipulator_description/meshes/omy_3m/base_unit.stl

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/ROBOTIS-GIT__open_manipulator -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `ac34fc0c613d8ef24d7494871ef5a2b60c9227a3`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'cb946894a8b5d242d2d4e012f93f01eecac5a3ce:open_manipulator_description/meshes/omy_3m/link1.stl')` in `ROBOTIS-GIT__open_manipulator`. fatal: bad object cb946894a8b5d242d2d4e012f93f01eecac5a3ce:open_manipulator_description/meshes/omy_3m/link1.stl

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/ROBOTIS-GIT__open_manipulator -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `95d30dc997bdec7ae301ecd2c28cdf1cd1204103`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'cb946894a8b5d242d2d4e012f93f01eecac5a3ce:open_manipulator_description/meshes/omy_3m/link2.stl')` in `ROBOTIS-GIT__open_manipulator`. fatal: bad object cb946894a8b5d242d2d4e012f93f01eecac5a3ce:open_manipulator_description/meshes/omy_3m/link2.stl

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/ROBOTIS-GIT__open_manipulator -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `f2cd5c069fb10db04bf6d4c1c31df409397e3877`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'cb946894a8b5d242d2d4e012f93f01eecac5a3ce:open_manipulator_description/meshes/omy_3m/link3.stl')` in `ROBOTIS-GIT__open_manipulator`. fatal: bad object cb946894a8b5d242d2d4e012f93f01eecac5a3ce:open_manipulator_description/meshes/omy_3m/link3.stl

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/ROBOTIS-GIT__open_manipulator -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `d816e98efc35e5ddbf2256457c18c81e0550e825`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'cb946894a8b5d242d2d4e012f93f01eecac5a3ce:open_manipulator_description/meshes/omy_3m/link4.stl')` in `ROBOTIS-GIT__open_manipulator`. fatal: bad object cb946894a8b5d242d2d4e012f93f01eecac5a3ce:open_manipulator_description/meshes/omy_3m/link4.stl

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/ROBOTIS-GIT__open_manipulator -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `fcad1a1dc9fe55ce837d04e5907ce463617469b9`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'cb946894a8b5d242d2d4e012f93f01eecac5a3ce:open_manipulator_description/meshes/omy_3m/link5.stl')` in `ROBOTIS-GIT__open_manipulator`. fatal: bad object cb946894a8b5d242d2d4e012f93f01eecac5a3ce:open_manipulator_description/meshes/omy_3m/link5.stl

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/ROBOTIS-GIT__open_manipulator -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `5de66f0d2fd765de349de652e5e4123406eea351`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'cb946894a8b5d242d2d4e012f93f01eecac5a3ce:open_manipulator_description/meshes/omy_3m/link6.stl')` in `ROBOTIS-GIT__open_manipulator`. fatal: bad object cb946894a8b5d242d2d4e012f93f01eecac5a3ce:open_manipulator_description/meshes/omy_3m/link6.stl

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/ROBOTIS-GIT__open_manipulator -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `3a87ccf351d52db0d22d3d304bfe22c266c19ef2`

- Network outcome: exit 0.

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 clone --filter=blob:limit=100k --no-checkout https://github.com/ROBOTIS-GIT/ROBOTIS-OP3-Common.git .cache/ROBOTIS-GIT__ROBOTIS-OP3-Common` — retrieve manufacturer source history and small text files. Parent process runs at nice 15; lazy fetching disabled.

- Network outcome: exit 0. Cloning into '.cache/ROBOTIS-GIT__ROBOTIS-OP3-Common'...

- Offline Git read failed (exit 128): `('show', '0780e54c2064a42089b0cf970d716ae44fec9233:op3_description/meshes/body.stl')` in `ROBOTIS-GIT__ROBOTIS-OP3-Common`. fatal: bad object 0780e54c2064a42089b0cf970d716ae44fec9233:op3_description/meshes/body.stl

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/ROBOTIS-GIT__ROBOTIS-OP3-Common -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `f59d43e7a0dfc09a838cc6d7e368b323a17abe20`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '0780e54c2064a42089b0cf970d716ae44fec9233:op3_description/meshes/ll1.stl')` in `ROBOTIS-GIT__ROBOTIS-OP3-Common`. fatal: bad object 0780e54c2064a42089b0cf970d716ae44fec9233:op3_description/meshes/ll1.stl

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/ROBOTIS-GIT__ROBOTIS-OP3-Common -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `d38f55e5aedd8d4c36885f9b288d5ec14dae5d7c`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '0780e54c2064a42089b0cf970d716ae44fec9233:op3_description/meshes/ll2.stl')` in `ROBOTIS-GIT__ROBOTIS-OP3-Common`. fatal: bad object 0780e54c2064a42089b0cf970d716ae44fec9233:op3_description/meshes/ll2.stl

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/ROBOTIS-GIT__ROBOTIS-OP3-Common -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `daf99592098f68e5d4f40650d47972cac3115464`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '0780e54c2064a42089b0cf970d716ae44fec9233:op3_description/meshes/ll3.stl')` in `ROBOTIS-GIT__ROBOTIS-OP3-Common`. fatal: bad object 0780e54c2064a42089b0cf970d716ae44fec9233:op3_description/meshes/ll3.stl

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/ROBOTIS-GIT__ROBOTIS-OP3-Common -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `16d3b6a16996a212131dfdf34ae418f08eac46b8`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '0780e54c2064a42089b0cf970d716ae44fec9233:op3_description/meshes/ll4.stl')` in `ROBOTIS-GIT__ROBOTIS-OP3-Common`. fatal: bad object 0780e54c2064a42089b0cf970d716ae44fec9233:op3_description/meshes/ll4.stl

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/ROBOTIS-GIT__ROBOTIS-OP3-Common -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `6964c43136d00d7f7e375c1151abf9507a70adda`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '0780e54c2064a42089b0cf970d716ae44fec9233:op3_description/meshes/ll5.stl')` in `ROBOTIS-GIT__ROBOTIS-OP3-Common`. fatal: bad object 0780e54c2064a42089b0cf970d716ae44fec9233:op3_description/meshes/ll5.stl

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/ROBOTIS-GIT__ROBOTIS-OP3-Common -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `c11fcb9e2889e92e44313078eda16d5e317b82bf`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '0780e54c2064a42089b0cf970d716ae44fec9233:op3_description/meshes/ll6.stl')` in `ROBOTIS-GIT__ROBOTIS-OP3-Common`. fatal: bad object 0780e54c2064a42089b0cf970d716ae44fec9233:op3_description/meshes/ll6.stl

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/ROBOTIS-GIT__ROBOTIS-OP3-Common -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `a4a550c934491973e67e6f04bc4bc165d3e06ab8`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '0780e54c2064a42089b0cf970d716ae44fec9233:op3_description/meshes/rl1.stl')` in `ROBOTIS-GIT__ROBOTIS-OP3-Common`. fatal: bad object 0780e54c2064a42089b0cf970d716ae44fec9233:op3_description/meshes/rl1.stl

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/ROBOTIS-GIT__ROBOTIS-OP3-Common -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `8cf53fd147a770c6fc3fb4b750ad34c236ddac18`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '0780e54c2064a42089b0cf970d716ae44fec9233:op3_description/meshes/rl2.stl')` in `ROBOTIS-GIT__ROBOTIS-OP3-Common`. fatal: bad object 0780e54c2064a42089b0cf970d716ae44fec9233:op3_description/meshes/rl2.stl

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/ROBOTIS-GIT__ROBOTIS-OP3-Common -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `09bd506e182a1d4d987ebf9e56c085d55ec7b135`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '0780e54c2064a42089b0cf970d716ae44fec9233:op3_description/meshes/rl3.stl')` in `ROBOTIS-GIT__ROBOTIS-OP3-Common`. fatal: bad object 0780e54c2064a42089b0cf970d716ae44fec9233:op3_description/meshes/rl3.stl

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/ROBOTIS-GIT__ROBOTIS-OP3-Common -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `d5b09ca257f71dcd814226026567f5a6a093a766`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '0780e54c2064a42089b0cf970d716ae44fec9233:op3_description/meshes/rl4.stl')` in `ROBOTIS-GIT__ROBOTIS-OP3-Common`. fatal: bad object 0780e54c2064a42089b0cf970d716ae44fec9233:op3_description/meshes/rl4.stl

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/ROBOTIS-GIT__ROBOTIS-OP3-Common -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `d426003ed7c235951fbabb7f8c70a31d4aa7dfcc`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '0780e54c2064a42089b0cf970d716ae44fec9233:op3_description/meshes/rl5.stl')` in `ROBOTIS-GIT__ROBOTIS-OP3-Common`. fatal: bad object 0780e54c2064a42089b0cf970d716ae44fec9233:op3_description/meshes/rl5.stl

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/ROBOTIS-GIT__ROBOTIS-OP3-Common -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `d40ebd8b742ba0a389fc0cb9e588c2c6119ef37c`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '0780e54c2064a42089b0cf970d716ae44fec9233:op3_description/meshes/rl6.stl')` in `ROBOTIS-GIT__ROBOTIS-OP3-Common`. fatal: bad object 0780e54c2064a42089b0cf970d716ae44fec9233:op3_description/meshes/rl6.stl

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/ROBOTIS-GIT__ROBOTIS-OP3-Common -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `db2e3c016fb6f798a3bfa5fe49395af06f349cf6`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '0780e54c2064a42089b0cf970d716ae44fec9233:op3_description/meshes/la1.stl')` in `ROBOTIS-GIT__ROBOTIS-OP3-Common`. fatal: bad object 0780e54c2064a42089b0cf970d716ae44fec9233:op3_description/meshes/la1.stl

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/ROBOTIS-GIT__ROBOTIS-OP3-Common -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `65365cadeed313ee7579da35297b0ab7b6dc8514`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '0780e54c2064a42089b0cf970d716ae44fec9233:op3_description/meshes/la2.stl')` in `ROBOTIS-GIT__ROBOTIS-OP3-Common`. fatal: bad object 0780e54c2064a42089b0cf970d716ae44fec9233:op3_description/meshes/la2.stl

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/ROBOTIS-GIT__ROBOTIS-OP3-Common -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `3ee632d37a0a93d7f44ab0616f634208f8bef078`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '0780e54c2064a42089b0cf970d716ae44fec9233:op3_description/meshes/la3.stl')` in `ROBOTIS-GIT__ROBOTIS-OP3-Common`. fatal: bad object 0780e54c2064a42089b0cf970d716ae44fec9233:op3_description/meshes/la3.stl

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/ROBOTIS-GIT__ROBOTIS-OP3-Common -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `04d158fe5a30a3cc58841906880ec7aca750cb43`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '0780e54c2064a42089b0cf970d716ae44fec9233:op3_description/meshes/ra1.stl')` in `ROBOTIS-GIT__ROBOTIS-OP3-Common`. fatal: bad object 0780e54c2064a42089b0cf970d716ae44fec9233:op3_description/meshes/ra1.stl

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/ROBOTIS-GIT__ROBOTIS-OP3-Common -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `f883faf977735d3ebe3b1a09ca2308238ba9e204`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '0780e54c2064a42089b0cf970d716ae44fec9233:op3_description/meshes/ra2.stl')` in `ROBOTIS-GIT__ROBOTIS-OP3-Common`. fatal: bad object 0780e54c2064a42089b0cf970d716ae44fec9233:op3_description/meshes/ra2.stl

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/ROBOTIS-GIT__ROBOTIS-OP3-Common -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `9aedd3a599b0d0675b6d41f719ffdabd64378377`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '0780e54c2064a42089b0cf970d716ae44fec9233:op3_description/meshes/ra3.stl')` in `ROBOTIS-GIT__ROBOTIS-OP3-Common`. fatal: bad object 0780e54c2064a42089b0cf970d716ae44fec9233:op3_description/meshes/ra3.stl

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/ROBOTIS-GIT__ROBOTIS-OP3-Common -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `70504647af58acc1e5cacfec233aab2970d42d6e`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '0780e54c2064a42089b0cf970d716ae44fec9233:op3_description/meshes/h1.stl')` in `ROBOTIS-GIT__ROBOTIS-OP3-Common`. fatal: bad object 0780e54c2064a42089b0cf970d716ae44fec9233:op3_description/meshes/h1.stl

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/ROBOTIS-GIT__ROBOTIS-OP3-Common -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `027df367fde5249b4c0ca8c83a3c0774a9b52a9d`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '0780e54c2064a42089b0cf970d716ae44fec9233:op3_description/meshes/h2.stl')` in `ROBOTIS-GIT__ROBOTIS-OP3-Common`. fatal: bad object 0780e54c2064a42089b0cf970d716ae44fec9233:op3_description/meshes/h2.stl

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/ROBOTIS-GIT__ROBOTIS-OP3-Common -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `d6fed6ccdc4b01573076c24f74d550609742d6db`

- Network outcome: exit 0.

- Historical source compile failed robotis_op3 139a7ac0d950755aa28318d418552db0ae0cd93e op3_description/urdf/robotis_op3.urdf.xacro: No such file or directory: .cache/ROBOTIS-GIT__ROBOTIS-OP3-Common/.drift_xacro/tmpzb2o2e4n/.unresolved_package/op3_gazebo_ros2/gazebo/robotis_op3.gazebo.xacro [Errno 2] No such file or directory: '.cache/ROBOTIS-GIT__ROBOTIS-OP3-Common/.drift_xacro/tmpzb2o2e4n/.unresolved_package/op3_gazebo_ros2/gazebo/robotis_op3.gazebo.xacro'

- Historical source compile failed robotis_op3 0f22b4239725f57b70b873d5e589d584d721ee50 op3_description/urdf/robotis_op3.urdf.xacro: unknown macro name: xacro:insert_transmission

- Historical source compile failed robotis_op3 b3947376853ab2afab01e910a80177c18827b1f3 op3_description/urdf/robotis_op3.urdf.xacro: No such file or directory: .cache/ROBOTIS-GIT__ROBOTIS-OP3-Common/.drift_xacro/tmpe1xod5md/.unresolved_package/robotis_op3_description/urdf/robotis_op3.visuals.xacro [Errno 2] No such file or directory: '.cache/ROBOTIS-GIT__ROBOTIS-OP3-Common/.drift_xacro/tmpe1xod5md/.unresolved_package/robotis_op3_description/urdf/robotis_op3.visuals.xacro'

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 clone --filter=blob:limit=100k --no-checkout https://github.com/TheRobotStudio/SO-ARM100.git .cache/TheRobotStudio__SO-ARM100` — retrieve manufacturer source history and small text files. Parent process runs at nice 15; lazy fetching disabled.

- Network outcome: exit 0. Cloning into '.cache/TheRobotStudio__SO-ARM100'...

- Offline Git read failed (exit 128): `('show', 'a758567c3978dfeefe282ede0500085a48fe8f78:Simulation/SO101/assets/base_motor_holder_so101_v1.stl')` in `TheRobotStudio__SO-ARM100`. fatal: bad object a758567c3978dfeefe282ede0500085a48fe8f78:Simulation/SO101/assets/base_motor_holder_so101_v1.stl

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/TheRobotStudio__SO-ARM100 -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `cac2b8dd98d3d8a6dcdf429b36aaa4b576d82041`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'a758567c3978dfeefe282ede0500085a48fe8f78:Simulation/SO101/assets/base_so101_v2.stl')` in `TheRobotStudio__SO-ARM100`. fatal: bad object a758567c3978dfeefe282ede0500085a48fe8f78:Simulation/SO101/assets/base_so101_v2.stl

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/TheRobotStudio__SO-ARM100 -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `ed10aa61d1181f8001c908ee5cae5c4f970ba417`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'a758567c3978dfeefe282ede0500085a48fe8f78:Simulation/SO101/assets/sts3215_03a_v1.stl')` in `TheRobotStudio__SO-ARM100`. fatal: bad object a758567c3978dfeefe282ede0500085a48fe8f78:Simulation/SO101/assets/sts3215_03a_v1.stl

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/TheRobotStudio__SO-ARM100 -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `fe05403dbfac7a26822b8c8cd0fc3d5288a69fc8`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'a758567c3978dfeefe282ede0500085a48fe8f78:Simulation/SO101/assets/motor_holder_so101_base_v1.stl')` in `TheRobotStudio__SO-ARM100`. fatal: bad object a758567c3978dfeefe282ede0500085a48fe8f78:Simulation/SO101/assets/motor_holder_so101_base_v1.stl

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/TheRobotStudio__SO-ARM100 -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `9eaf67243a5ffc2dacb3fbd026b4c0620adcdd66`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'a758567c3978dfeefe282ede0500085a48fe8f78:Simulation/SO101/assets/rotation_pitch_so101_v1.stl')` in `TheRobotStudio__SO-ARM100`. fatal: bad object a758567c3978dfeefe282ede0500085a48fe8f78:Simulation/SO101/assets/rotation_pitch_so101_v1.stl

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/TheRobotStudio__SO-ARM100 -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `5c05dee570623f62c4ab7597d76c7bdea20eacea`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'a758567c3978dfeefe282ede0500085a48fe8f78:Simulation/SO101/assets/upper_arm_so101_v1.stl')` in `TheRobotStudio__SO-ARM100`. fatal: bad object a758567c3978dfeefe282ede0500085a48fe8f78:Simulation/SO101/assets/upper_arm_so101_v1.stl

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/TheRobotStudio__SO-ARM100 -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `9c0f9b275a51f720476e529c92193f4f69d4784c`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'a758567c3978dfeefe282ede0500085a48fe8f78:Simulation/SO101/assets/under_arm_so101_v1.stl')` in `TheRobotStudio__SO-ARM100`. fatal: bad object a758567c3978dfeefe282ede0500085a48fe8f78:Simulation/SO101/assets/under_arm_so101_v1.stl

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/TheRobotStudio__SO-ARM100 -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `480e0583c8bb27ff9affefbebee72b784fb054c8`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'a758567c3978dfeefe282ede0500085a48fe8f78:Simulation/SO101/assets/motor_holder_so101_wrist_v1.stl')` in `TheRobotStudio__SO-ARM100`. fatal: bad object a758567c3978dfeefe282ede0500085a48fe8f78:Simulation/SO101/assets/motor_holder_so101_wrist_v1.stl

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/TheRobotStudio__SO-ARM100 -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `d0aa18b15a9cd63f41fa4d48e82df7a3b618c75d`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'a758567c3978dfeefe282ede0500085a48fe8f78:Simulation/SO101/assets/sts3215_03a_no_horn_v1.stl')` in `TheRobotStudio__SO-ARM100`. fatal: bad object a758567c3978dfeefe282ede0500085a48fe8f78:Simulation/SO101/assets/sts3215_03a_no_horn_v1.stl

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/TheRobotStudio__SO-ARM100 -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `2a89597702f5ec6849b6b1b894c867b35b98ca42`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'a758567c3978dfeefe282ede0500085a48fe8f78:Simulation/SO101/assets/wrist_roll_pitch_so101_v2.stl')` in `TheRobotStudio__SO-ARM100`. fatal: bad object a758567c3978dfeefe282ede0500085a48fe8f78:Simulation/SO101/assets/wrist_roll_pitch_so101_v2.stl

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/TheRobotStudio__SO-ARM100 -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `ac5172a35e6da3e9fdea21e25803f23cc61e31f1`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'a758567c3978dfeefe282ede0500085a48fe8f78:Simulation/SO101/assets/Wrist_Roll_SO101.stl')` in `TheRobotStudio__SO-ARM100`. fatal: bad object a758567c3978dfeefe282ede0500085a48fe8f78:Simulation/SO101/assets/Wrist_Roll_SO101.stl

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/TheRobotStudio__SO-ARM100 -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `d7fb60331e442caf81487ef34f18c98465bb0275`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'a758567c3978dfeefe282ede0500085a48fe8f78:Simulation/SO101/assets/Handle_SO101.stl')` in `TheRobotStudio__SO-ARM100`. fatal: bad object a758567c3978dfeefe282ede0500085a48fe8f78:Simulation/SO101/assets/Handle_SO101.stl

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/TheRobotStudio__SO-ARM100 -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `74e136fecd44afa1a70c47798df9a8480cabd712`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'a758567c3978dfeefe282ede0500085a48fe8f78:Simulation/SO101/assets/Trigger_SO101.stl')` in `TheRobotStudio__SO-ARM100`. fatal: bad object a758567c3978dfeefe282ede0500085a48fe8f78:Simulation/SO101/assets/Trigger_SO101.stl

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/TheRobotStudio__SO-ARM100 -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `bce57b2ae7e38b47313cdd7d812bcabd2e301b40`

- Network outcome: exit 0.

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 clone --filter=blob:limit=100k --no-checkout https://github.com/Seeed-Projects/reBot-Isaacsim.git .cache/Seeed-Projects__reBot-Isaacsim` — retrieve manufacturer source history and small text files. Parent process runs at nice 15; lazy fetching disabled.

- Network outcome: exit 0. Cloning into '.cache/Seeed-Projects__reBot-Isaacsim'...

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 clone --filter=blob:limit=100k --no-checkout https://github.com/shadow-robot/sr_common.git .cache/shadow-robot__sr_common` — retrieve manufacturer source history and small text files. Parent process runs at nice 15; lazy fetching disabled.

- Network outcome: exit 0. Cloning into '.cache/shadow-robot__sr_common'...

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 clone --filter=blob:limit=100k --no-checkout https://github.com/sharpa-robotics/sharpa-urdf-usd-xml.git .cache/sharpa-robotics__sharpa-urdf-usd-xml` — retrieve manufacturer source history and small text files. Parent process runs at nice 15; lazy fetching disabled.

- Network outcome: exit 0. Cloning into '.cache/sharpa-robotics__sharpa-urdf-usd-xml'...

- Offline Git read failed (exit 128): `('show', 'd323b371d02f4fc04a0873c19c5234cae6d803dd:wave_01/left_sharpa_wave/meshes/left_hand_C_MC_visual_.STL')` in `sharpa-robotics__sharpa-urdf-usd-xml`. fatal: bad object d323b371d02f4fc04a0873c19c5234cae6d803dd:wave_01/left_sharpa_wave/meshes/left_hand_C_MC_visual_.STL

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/sharpa-robotics__sharpa-urdf-usd-xml -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `62e64621a36ef1395811b09eb1a4c9800f488734`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'd323b371d02f4fc04a0873c19c5234cae6d803dd:wave_01/left_sharpa_wave/meshes/left_hand_C_MC.STL')` in `sharpa-robotics__sharpa-urdf-usd-xml`. fatal: bad object d323b371d02f4fc04a0873c19c5234cae6d803dd:wave_01/left_sharpa_wave/meshes/left_hand_C_MC.STL

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/sharpa-robotics__sharpa-urdf-usd-xml -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `9e972ff9280ce0000f1af6f47b8b9fe8fcca6a4b`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'd323b371d02f4fc04a0873c19c5234cae6d803dd:wave_01/left_sharpa_wave/meshes/left_thumb_CMC_VL.STL')` in `sharpa-robotics__sharpa-urdf-usd-xml`. fatal: bad object d323b371d02f4fc04a0873c19c5234cae6d803dd:wave_01/left_sharpa_wave/meshes/left_thumb_CMC_VL.STL

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/sharpa-robotics__sharpa-urdf-usd-xml -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `34c051e67e4100c5455c742b7ff495d2e75e9b04`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'd323b371d02f4fc04a0873c19c5234cae6d803dd:wave_01/left_sharpa_wave/meshes/left_thumb_MC_visual.STL')` in `sharpa-robotics__sharpa-urdf-usd-xml`. fatal: bad object d323b371d02f4fc04a0873c19c5234cae6d803dd:wave_01/left_sharpa_wave/meshes/left_thumb_MC_visual.STL

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/sharpa-robotics__sharpa-urdf-usd-xml -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `7beb79bd5532ce2129faa95f035d8046454c3592`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'd323b371d02f4fc04a0873c19c5234cae6d803dd:wave_01/left_sharpa_wave/meshes/left_thumb_MC.STL')` in `sharpa-robotics__sharpa-urdf-usd-xml`. fatal: bad object d323b371d02f4fc04a0873c19c5234cae6d803dd:wave_01/left_sharpa_wave/meshes/left_thumb_MC.STL

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/sharpa-robotics__sharpa-urdf-usd-xml -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `785b7486fe877dd865fa79152d041b62bb9756f2`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'd323b371d02f4fc04a0873c19c5234cae6d803dd:wave_01/left_sharpa_wave/meshes/left_thumb_MCP_VL_visual.STL')` in `sharpa-robotics__sharpa-urdf-usd-xml`. fatal: bad object d323b371d02f4fc04a0873c19c5234cae6d803dd:wave_01/left_sharpa_wave/meshes/left_thumb_MCP_VL_visual.STL

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/sharpa-robotics__sharpa-urdf-usd-xml -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `6e9c0ed1842496f1ddc5e711878bc04440c65625`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'd323b371d02f4fc04a0873c19c5234cae6d803dd:wave_01/left_sharpa_wave/meshes/left_thumb_PP_visual.STL')` in `sharpa-robotics__sharpa-urdf-usd-xml`. fatal: bad object d323b371d02f4fc04a0873c19c5234cae6d803dd:wave_01/left_sharpa_wave/meshes/left_thumb_PP_visual.STL

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/sharpa-robotics__sharpa-urdf-usd-xml -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `7416f3476ab6bbe54aea39a495ea213ee6797a39`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'd323b371d02f4fc04a0873c19c5234cae6d803dd:wave_01/left_sharpa_wave/meshes/DP_Visual_HB1_TH.STL')` in `sharpa-robotics__sharpa-urdf-usd-xml`. fatal: bad object d323b371d02f4fc04a0873c19c5234cae6d803dd:wave_01/left_sharpa_wave/meshes/DP_Visual_HB1_TH.STL

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/sharpa-robotics__sharpa-urdf-usd-xml -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `3070955d8616e1fcb2ad3bd8fb5cdfad25f43e21`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'd323b371d02f4fc04a0873c19c5234cae6d803dd:wave_01/left_sharpa_wave/meshes/DP_HB1_TH.STL')` in `sharpa-robotics__sharpa-urdf-usd-xml`. fatal: bad object d323b371d02f4fc04a0873c19c5234cae6d803dd:wave_01/left_sharpa_wave/meshes/DP_HB1_TH.STL

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/sharpa-robotics__sharpa-urdf-usd-xml -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `29250f09fc1a457615b01650effa248542278fe1`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'd323b371d02f4fc04a0873c19c5234cae6d803dd:wave_01/left_sharpa_wave/meshes/thumb_elastomer_surface.STL')` in `sharpa-robotics__sharpa-urdf-usd-xml`. fatal: bad object d323b371d02f4fc04a0873c19c5234cae6d803dd:wave_01/left_sharpa_wave/meshes/thumb_elastomer_surface.STL

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/sharpa-robotics__sharpa-urdf-usd-xml -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `9afcb28d8a5027aa1a5ffb824982d3978d6c3911`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'd323b371d02f4fc04a0873c19c5234cae6d803dd:wave_01/left_sharpa_wave/meshes/elastomer_HB1_TH.STL')` in `sharpa-robotics__sharpa-urdf-usd-xml`. fatal: bad object d323b371d02f4fc04a0873c19c5234cae6d803dd:wave_01/left_sharpa_wave/meshes/elastomer_HB1_TH.STL

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/sharpa-robotics__sharpa-urdf-usd-xml -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `a07c8d61d63f72d0fdfb540680cccfd1546017fc`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'd323b371d02f4fc04a0873c19c5234cae6d803dd:wave_01/left_sharpa_wave/meshes/left_MCP_VL_visual.STL')` in `sharpa-robotics__sharpa-urdf-usd-xml`. fatal: bad object d323b371d02f4fc04a0873c19c5234cae6d803dd:wave_01/left_sharpa_wave/meshes/left_MCP_VL_visual.STL

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/sharpa-robotics__sharpa-urdf-usd-xml -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `fec8facc64a0c19d9c146c9dc98489888a924b79`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'd323b371d02f4fc04a0873c19c5234cae6d803dd:wave_01/left_sharpa_wave/meshes/left_PP_visual.STL')` in `sharpa-robotics__sharpa-urdf-usd-xml`. fatal: bad object d323b371d02f4fc04a0873c19c5234cae6d803dd:wave_01/left_sharpa_wave/meshes/left_PP_visual.STL

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/sharpa-robotics__sharpa-urdf-usd-xml -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `dc8ce85f002890582a1ee8db267d4520e24a1d32`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'd323b371d02f4fc04a0873c19c5234cae6d803dd:wave_01/left_sharpa_wave/meshes/left_MP_visual.STL')` in `sharpa-robotics__sharpa-urdf-usd-xml`. fatal: bad object d323b371d02f4fc04a0873c19c5234cae6d803dd:wave_01/left_sharpa_wave/meshes/left_MP_visual.STL

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/sharpa-robotics__sharpa-urdf-usd-xml -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `c03a7768e5969991782ee8b73f0dc773ea2391f5`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'd323b371d02f4fc04a0873c19c5234cae6d803dd:wave_01/left_sharpa_wave/meshes/DP_visual_HB1_4F.STL')` in `sharpa-robotics__sharpa-urdf-usd-xml`. fatal: bad object d323b371d02f4fc04a0873c19c5234cae6d803dd:wave_01/left_sharpa_wave/meshes/DP_visual_HB1_4F.STL

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/sharpa-robotics__sharpa-urdf-usd-xml -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `442c00f311f59bdfe39f9990ef2b7ab9270286e2`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'd323b371d02f4fc04a0873c19c5234cae6d803dd:wave_01/left_sharpa_wave/meshes/DP_HB1_4F.STL')` in `sharpa-robotics__sharpa-urdf-usd-xml`. fatal: bad object d323b371d02f4fc04a0873c19c5234cae6d803dd:wave_01/left_sharpa_wave/meshes/DP_HB1_4F.STL

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/sharpa-robotics__sharpa-urdf-usd-xml -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `c30c46a5251b00a0ce79ecd2cfc2d426f60305d3`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'd323b371d02f4fc04a0873c19c5234cae6d803dd:wave_01/left_sharpa_wave/meshes/elastomer_surface.STL')` in `sharpa-robotics__sharpa-urdf-usd-xml`. fatal: bad object d323b371d02f4fc04a0873c19c5234cae6d803dd:wave_01/left_sharpa_wave/meshes/elastomer_surface.STL

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/sharpa-robotics__sharpa-urdf-usd-xml -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `e9d6713d5e80cc56b36ca3eeee20e57730d9dfb4`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'd323b371d02f4fc04a0873c19c5234cae6d803dd:wave_01/left_sharpa_wave/meshes/elastomer_HB1_4F.STL')` in `sharpa-robotics__sharpa-urdf-usd-xml`. fatal: bad object d323b371d02f4fc04a0873c19c5234cae6d803dd:wave_01/left_sharpa_wave/meshes/elastomer_HB1_4F.STL

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/sharpa-robotics__sharpa-urdf-usd-xml -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `4d15d8e667cd51cc86abd56c9a64f39d33df405e`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'd323b371d02f4fc04a0873c19c5234cae6d803dd:wave_01/left_sharpa_wave/meshes/left_pinky_MC_visual.STL')` in `sharpa-robotics__sharpa-urdf-usd-xml`. fatal: bad object d323b371d02f4fc04a0873c19c5234cae6d803dd:wave_01/left_sharpa_wave/meshes/left_pinky_MC_visual.STL

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/sharpa-robotics__sharpa-urdf-usd-xml -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `6a697c8be7675275b3752d7693aa22ca98d6b04c`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'd323b371d02f4fc04a0873c19c5234cae6d803dd:wave_01/right_sharpa_wave/meshes/right_hand_C_MC_visual_.STL')` in `sharpa-robotics__sharpa-urdf-usd-xml`. fatal: bad object d323b371d02f4fc04a0873c19c5234cae6d803dd:wave_01/right_sharpa_wave/meshes/right_hand_C_MC_visual_.STL

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/sharpa-robotics__sharpa-urdf-usd-xml -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `3685a3b5a79917d9f1af8385ee8e318858f90a68`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'd323b371d02f4fc04a0873c19c5234cae6d803dd:wave_01/right_sharpa_wave/meshes/right_hand_C_MC.STL')` in `sharpa-robotics__sharpa-urdf-usd-xml`. fatal: bad object d323b371d02f4fc04a0873c19c5234cae6d803dd:wave_01/right_sharpa_wave/meshes/right_hand_C_MC.STL

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/sharpa-robotics__sharpa-urdf-usd-xml -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `53b224a1fc7f2f7ffa82e9bfb8eb3f5bee5f0fb8`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'd323b371d02f4fc04a0873c19c5234cae6d803dd:wave_01/right_sharpa_wave/meshes/right_thumb_CMC_VL_visual.STL')` in `sharpa-robotics__sharpa-urdf-usd-xml`. fatal: bad object d323b371d02f4fc04a0873c19c5234cae6d803dd:wave_01/right_sharpa_wave/meshes/right_thumb_CMC_VL_visual.STL

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/sharpa-robotics__sharpa-urdf-usd-xml -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `14b2d3bc56c7f56abc5baca7577baf434dbba5fd`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'd323b371d02f4fc04a0873c19c5234cae6d803dd:wave_01/right_sharpa_wave/meshes/right_thumb_MC_visual.STL')` in `sharpa-robotics__sharpa-urdf-usd-xml`. fatal: bad object d323b371d02f4fc04a0873c19c5234cae6d803dd:wave_01/right_sharpa_wave/meshes/right_thumb_MC_visual.STL

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/sharpa-robotics__sharpa-urdf-usd-xml -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `86b5e87de62e347907427fe71260c6afd2073610`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'd323b371d02f4fc04a0873c19c5234cae6d803dd:wave_01/right_sharpa_wave/meshes/right_thumb_MC.STL')` in `sharpa-robotics__sharpa-urdf-usd-xml`. fatal: bad object d323b371d02f4fc04a0873c19c5234cae6d803dd:wave_01/right_sharpa_wave/meshes/right_thumb_MC.STL

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/sharpa-robotics__sharpa-urdf-usd-xml -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `df77b3a89ad8ce1ec597039bc118dfd8eb9df2ab`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'd323b371d02f4fc04a0873c19c5234cae6d803dd:wave_01/right_sharpa_wave/meshes/right_thumb_MCP_VL_visual.STL')` in `sharpa-robotics__sharpa-urdf-usd-xml`. fatal: bad object d323b371d02f4fc04a0873c19c5234cae6d803dd:wave_01/right_sharpa_wave/meshes/right_thumb_MCP_VL_visual.STL

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/sharpa-robotics__sharpa-urdf-usd-xml -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `5a4fbb3e9b7f9019bb3ce453420857fabf33f0dc`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'd323b371d02f4fc04a0873c19c5234cae6d803dd:wave_01/right_sharpa_wave/meshes/right_thumb_PP_visual.STL')` in `sharpa-robotics__sharpa-urdf-usd-xml`. fatal: bad object d323b371d02f4fc04a0873c19c5234cae6d803dd:wave_01/right_sharpa_wave/meshes/right_thumb_PP_visual.STL

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/sharpa-robotics__sharpa-urdf-usd-xml -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `a0054c2c24d127f5beec9c2f9ec0bf7f0ddf67c4`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'd323b371d02f4fc04a0873c19c5234cae6d803dd:wave_01/right_sharpa_wave/meshes/DP_Visual_HB1_TH.STL')` in `sharpa-robotics__sharpa-urdf-usd-xml`. fatal: bad object d323b371d02f4fc04a0873c19c5234cae6d803dd:wave_01/right_sharpa_wave/meshes/DP_Visual_HB1_TH.STL

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/sharpa-robotics__sharpa-urdf-usd-xml -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `649ffb4cce24e3bcd33a50c2fc8fe542361bced9`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'd323b371d02f4fc04a0873c19c5234cae6d803dd:wave_01/right_sharpa_wave/meshes/right_MCP_VL_visual.STL')` in `sharpa-robotics__sharpa-urdf-usd-xml`. fatal: bad object d323b371d02f4fc04a0873c19c5234cae6d803dd:wave_01/right_sharpa_wave/meshes/right_MCP_VL_visual.STL

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/sharpa-robotics__sharpa-urdf-usd-xml -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `6c296133ecdb9d783f886a06f98bfc23cad3dfc1`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'd323b371d02f4fc04a0873c19c5234cae6d803dd:wave_01/right_sharpa_wave/meshes/right_PP_visual.STL')` in `sharpa-robotics__sharpa-urdf-usd-xml`. fatal: bad object d323b371d02f4fc04a0873c19c5234cae6d803dd:wave_01/right_sharpa_wave/meshes/right_PP_visual.STL

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/sharpa-robotics__sharpa-urdf-usd-xml -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `4e391ee4cce1267c7cdc78ac6299ff8720341cf0`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'd323b371d02f4fc04a0873c19c5234cae6d803dd:wave_01/right_sharpa_wave/meshes/right_MP_visual.STL')` in `sharpa-robotics__sharpa-urdf-usd-xml`. fatal: bad object d323b371d02f4fc04a0873c19c5234cae6d803dd:wave_01/right_sharpa_wave/meshes/right_MP_visual.STL

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/sharpa-robotics__sharpa-urdf-usd-xml -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `d17763d618ec50ad539328a7f39b8f395ba991c0`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'd323b371d02f4fc04a0873c19c5234cae6d803dd:wave_01/right_sharpa_wave/meshes/right_pinky_MC_visual.STL')` in `sharpa-robotics__sharpa-urdf-usd-xml`. fatal: bad object d323b371d02f4fc04a0873c19c5234cae6d803dd:wave_01/right_sharpa_wave/meshes/right_pinky_MC_visual.STL

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/sharpa-robotics__sharpa-urdf-usd-xml -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `921ce00ff1e5bbf9dbb62e5839500fb6c547c536`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'd323b371d02f4fc04a0873c19c5234cae6d803dd:wave_01/left_sharpa_wave/meshes/wrist_B.STL')` in `sharpa-robotics__sharpa-urdf-usd-xml`. fatal: bad object d323b371d02f4fc04a0873c19c5234cae6d803dd:wave_01/left_sharpa_wave/meshes/wrist_B.STL

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/sharpa-robotics__sharpa-urdf-usd-xml -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `e8dc40fbeca0d1201181e6382eda9447d564c14c`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'd323b371d02f4fc04a0873c19c5234cae6d803dd:wave_01/left_sharpa_wave/meshes/flange_B.STL')` in `sharpa-robotics__sharpa-urdf-usd-xml`. fatal: bad object d323b371d02f4fc04a0873c19c5234cae6d803dd:wave_01/left_sharpa_wave/meshes/flange_B.STL

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/sharpa-robotics__sharpa-urdf-usd-xml -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `b5f2589c4fa3f2659678b11d6b42e4048a970b71`

- Network outcome: exit 0.

- Menagerie self-comparison compile failed: skydio_x2/x2.xml: ValueError: Error: texture 'X2_lowpoly_texture_SpinningProps_1024' not found in material 0
Element name 'phong3SG', id 0, line 26

- Menagerie self-comparison compile failed: toddlerbot_2xc/toddlerbot_2xc.xml: ValueError: Error: geom 'torso_collision_0' not found in collision 0
Element name '', id 0, line 322

- Menagerie self-comparison compile failed: toddlerbot_2xc/toddlerbot_2xc_mjx.xml: ValueError: Error: geom 'left_ankle_roll_link_collision' not found in collision 0
Element name '', id 0, line 322

- Menagerie self-comparison compile failed: toddlerbot_2xc/toddlerbot_2xc_pos.xml: ValueError: Error: geom 'torso_collision_0' not found in collision 0
Element name '', id 0, line 322

- Menagerie self-comparison compile failed: toddlerbot_2xm/toddlerbot_2xm.xml: ValueError: Error: geom 'torso_collision_0' not found in collision 0
Element name '', id 0, line 322

- Menagerie self-comparison compile failed: toddlerbot_2xm/toddlerbot_2xm_mjx.xml: ValueError: Error: geom 'left_ankle_roll_link_collision' not found in collision 0
Element name '', id 0, line 322

- Menagerie self-comparison compile failed: toddlerbot_2xm/toddlerbot_2xm_pos.xml: ValueError: Error: geom 'torso_collision_0' not found in collision 0
Element name '', id 0, line 322

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 clone --filter=blob:limit=100k --no-checkout https://github.com/Interbotix/interbotix_ros_manipulators.git .cache/Interbotix__interbotix_ros_manipulators` — retrieve manufacturer source history and small text files. Parent process runs at nice 15; lazy fetching disabled.

- Network outcome: exit 0. Cloning into '.cache/Interbotix__interbotix_ros_manipulators'...

- Offline Git read failed (exit 128): `('show', 'a758567c3978dfeefe282ede0500085a48fe8f78:URDF/SO_5DOF_ARM100_8j_URDF.SLDASM/urdf/SO_5DOF_ARM100_8j_URDF.SLDASM.urdf')` in `TheRobotStudio__SO-ARM100`. fatal: path 'URDF/SO_5DOF_ARM100_8j_URDF.SLDASM/urdf/SO_5DOF_ARM100_8j_URDF.SLDASM.urdf' does not exist in 'a758567c3978dfeefe282ede0500085a48fe8f78'

- https://github.com/TheRobotStudio/SO-ARM100 URDF/SO_5DOF_ARM100_8j_URDF.SLDASM/urdf/SO_5DOF_ARM100_8j_URDF.SLDASM.urdf at a758567c3978dfeefe282ede0500085a48fe8f78: CalledProcessError: Command '['git', '-C', '.cache/TheRobotStudio__SO-ARM100', 'show', 'a758567c3978dfeefe282ede0500085a48fe8f78:URDF/SO_5DOF_ARM100_8j_URDF.SLDASM/urdf/SO_5DOF_ARM100_8j_URDF.SLDASM.urdf']' returned non-zero exit status 128.

- Offline Git read failed (exit 128): `('show', '4e9c5588d8a8415b6a6c2142a0ce8c32207cf3e9:Simulation/SO100/so100.urdf')` in `TheRobotStudio__SO-ARM100`. fatal: path 'Simulation/SO100/so100.urdf' does not exist in '4e9c5588d8a8415b6a6c2142a0ce8c32207cf3e9'

- Offline Git read failed (exit 128): `('rev-parse', '4e9c5588d8a8415b6a6c2142a0ce8c32207cf3e9:Simulation/SO100/so100.urdf')` in `TheRobotStudio__SO-ARM100`. fatal: path 'Simulation/SO100/so100.urdf' does not exist in '4e9c5588d8a8415b6a6c2142a0ce8c32207cf3e9'

- Targeted fetch failed for https://github.com/TheRobotStudio/SO-ARM100 4e9c5588d8a8415b6a6c2142a0ce8c32207cf3e9:Simulation/SO100/so100.urdf: Command '['git', '-C', '.cache/TheRobotStudio__SO-ARM100', 'rev-parse', '4e9c5588d8a8415b6a6c2142a0ce8c32207cf3e9:Simulation/SO100/so100.urdf']' returned non-zero exit status 128.

- Pinned source compilation failed trs_so_arm100: Command '['git', '-C', '.cache/TheRobotStudio__SO-ARM100', 'show', '4e9c5588d8a8415b6a6c2142a0ce8c32207cf3e9:Simulation/SO100/so100.urdf']' returned non-zero exit status 128.

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 clone --filter=blob:limit=100k --no-checkout https://github.com/xArm-Developer/xarm_ros2.git .cache/xArm-Developer__xarm_ros2` — retrieve manufacturer source history and small text files. Parent process runs at nice 15; lazy fetching disabled.

- Network outcome: exit 0. Cloning into '.cache/xArm-Developer__xarm_ros2'...

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 clone --filter=blob:limit=100k --no-checkout https://github.com/xArm-Developer/xarm_ros.git .cache/xArm-Developer__xarm_ros` — retrieve manufacturer source history and small text files. Parent process runs at nice 15; lazy fetching disabled.

- Network outcome: exit 0. Cloning into '.cache/xArm-Developer__xarm_ros'...

- https://github.com/pal-robotics/talos_robot talos_description/robots/talos_full_v2.urdf.xacro at 79709aa4f4f453ec18a5e467e65f84ff58ea24d0: XacroException: No such file or directory: .cache/pal-robotics__talos_robot/.drift_xacro/tmpkegt_82s/.unresolved_package/pal_urdf_utils/urdf/deg_to_rad.urdf.xacro [Errno 2] No such file or directory: '.cache/pal-robotics__talos_robot/.drift_xacro/tmpkegt_82s/.unresolved_package/pal_urdf_utils/urdf/deg_to_rad.urdf.xacro'

- https://github.com/pal-robotics/talos_robot talos_description/robots/talos_arm_right.urdf.xacro at 79709aa4f4f453ec18a5e467e65f84ff58ea24d0: XacroException: No such file or directory: .cache/pal-robotics__talos_robot/.drift_xacro/tmpw7r3r31n/.unresolved_package/pal_urdf_utils/urdf/deg_to_rad.urdf.xacro [Errno 2] No such file or directory: '.cache/pal-robotics__talos_robot/.drift_xacro/tmpw7r3r31n/.unresolved_package/pal_urdf_utils/urdf/deg_to_rad.urdf.xacro'

- https://github.com/pal-robotics/talos_robot talos_description/urdf/talos_full_common.urdf.xacro at 79709aa4f4f453ec18a5e467e65f84ff58ea24d0: XacroException: No such file or directory: .cache/pal-robotics__talos_robot/.drift_xacro/tmp4g3gq3z_/.unresolved_package/pal_urdf_utils/urdf/deg_to_rad.urdf.xacro [Errno 2] No such file or directory: '.cache/pal-robotics__talos_robot/.drift_xacro/tmp4g3gq3z_/.unresolved_package/pal_urdf_utils/urdf/deg_to_rad.urdf.xacro'

- https://github.com/pal-robotics/talos_robot talos_description/robots/talos_lower_body.urdf.xacro at 79709aa4f4f453ec18a5e467e65f84ff58ea24d0: XacroException: No such file or directory: .cache/pal-robotics__talos_robot/.drift_xacro/tmp6oww6450/.unresolved_package/pal_urdf_utils/urdf/ft_sensors/ati_talos.urdf.xacro [Errno 2] No such file or directory: '.cache/pal-robotics__talos_robot/.drift_xacro/tmp6oww6450/.unresolved_package/pal_urdf_utils/urdf/ft_sensors/ati_talos.urdf.xacro'

- https://github.com/pal-robotics/talos_robot talos_description/robots/talos_full_no_grippers.urdf.xacro at 79709aa4f4f453ec18a5e467e65f84ff58ea24d0: XacroException: Undefined substitution argument enable_crane

- https://github.com/pal-robotics/talos_robot talos_description/robots/talos_full_fake_grippers.urdf.xacro at 79709aa4f4f453ec18a5e467e65f84ff58ea24d0: XacroException: Undefined substitution argument enable_crane

- https://github.com/pal-robotics/talos_robot talos_description/robots/talos_lower_body_torso_head.urdf.xacro at 79709aa4f4f453ec18a5e467e65f84ff58ea24d0: XacroException: Undefined substitution argument enable_crane

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 clone --filter=blob:limit=100k --no-checkout https://github.com/unitreerobotics/unitree_mujoco.git .cache/unitreerobotics__unitree_mujoco` — retrieve manufacturer source history and small text files. Parent process runs at nice 15; lazy fetching disabled.

- Network outcome: exit 0. Cloning into '.cache/unitreerobotics__unitree_mujoco'...

- Offline Git read failed (exit 128): `('show', '1eb6642e3f3fdfb7fb13a9794fd6a2dd93ea0e7d:unitree_robots/go2/assets/base_0.obj')` in `unitreerobotics__unitree_mujoco`. fatal: bad object 1eb6642e3f3fdfb7fb13a9794fd6a2dd93ea0e7d:unitree_robots/go2/assets/base_0.obj

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/unitreerobotics__unitree_mujoco -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `f2e688236f56bd2738468a213ea61fd2f69baf0b`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '1eb6642e3f3fdfb7fb13a9794fd6a2dd93ea0e7d:unitree_robots/go2/assets/base_1.obj')` in `unitreerobotics__unitree_mujoco`. fatal: bad object 1eb6642e3f3fdfb7fb13a9794fd6a2dd93ea0e7d:unitree_robots/go2/assets/base_1.obj

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/unitreerobotics__unitree_mujoco -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `e9a44eb668902b7f934f8328e4d33c6e38df8db9`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '1eb6642e3f3fdfb7fb13a9794fd6a2dd93ea0e7d:unitree_robots/go2/assets/base_2.obj')` in `unitreerobotics__unitree_mujoco`. fatal: bad object 1eb6642e3f3fdfb7fb13a9794fd6a2dd93ea0e7d:unitree_robots/go2/assets/base_2.obj

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/unitreerobotics__unitree_mujoco -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `bc661591f01c760072cb9f3fb6d80b2545bb1d53`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '1eb6642e3f3fdfb7fb13a9794fd6a2dd93ea0e7d:unitree_robots/go2/assets/base_3.obj')` in `unitreerobotics__unitree_mujoco`. fatal: bad object 1eb6642e3f3fdfb7fb13a9794fd6a2dd93ea0e7d:unitree_robots/go2/assets/base_3.obj

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/unitreerobotics__unitree_mujoco -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `5c98393efeb90c26bef36279e000d738dff8ff9d`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '1eb6642e3f3fdfb7fb13a9794fd6a2dd93ea0e7d:unitree_robots/go2/assets/base_4.obj')` in `unitreerobotics__unitree_mujoco`. fatal: bad object 1eb6642e3f3fdfb7fb13a9794fd6a2dd93ea0e7d:unitree_robots/go2/assets/base_4.obj

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/unitreerobotics__unitree_mujoco -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `1f45bc4fa84604cd8e69124084805104b96be188`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '1eb6642e3f3fdfb7fb13a9794fd6a2dd93ea0e7d:unitree_robots/go2/assets/hip_0.obj')` in `unitreerobotics__unitree_mujoco`. fatal: bad object 1eb6642e3f3fdfb7fb13a9794fd6a2dd93ea0e7d:unitree_robots/go2/assets/hip_0.obj

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/unitreerobotics__unitree_mujoco -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `551f12437a92cf72206aa56dca412c88220b6c4a`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '1eb6642e3f3fdfb7fb13a9794fd6a2dd93ea0e7d:unitree_robots/go2/assets/hip_1.obj')` in `unitreerobotics__unitree_mujoco`. fatal: bad object 1eb6642e3f3fdfb7fb13a9794fd6a2dd93ea0e7d:unitree_robots/go2/assets/hip_1.obj

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/unitreerobotics__unitree_mujoco -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `ed2bebfc4c2febfef45a1c67c40397964a6df6e4`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '1eb6642e3f3fdfb7fb13a9794fd6a2dd93ea0e7d:unitree_robots/go2/assets/thigh_0.obj')` in `unitreerobotics__unitree_mujoco`. fatal: bad object 1eb6642e3f3fdfb7fb13a9794fd6a2dd93ea0e7d:unitree_robots/go2/assets/thigh_0.obj

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/unitreerobotics__unitree_mujoco -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `0b99756ffd7d3391abeff66fc510a1ae7c5a4c8b`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '1eb6642e3f3fdfb7fb13a9794fd6a2dd93ea0e7d:unitree_robots/go2/assets/thigh_1.obj')` in `unitreerobotics__unitree_mujoco`. fatal: bad object 1eb6642e3f3fdfb7fb13a9794fd6a2dd93ea0e7d:unitree_robots/go2/assets/thigh_1.obj

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/unitreerobotics__unitree_mujoco -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `5005be1de988534d0f4b94ec51eaf1ff41ba7970`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '1eb6642e3f3fdfb7fb13a9794fd6a2dd93ea0e7d:unitree_robots/go2/assets/thigh_mirror_0.obj')` in `unitreerobotics__unitree_mujoco`. fatal: bad object 1eb6642e3f3fdfb7fb13a9794fd6a2dd93ea0e7d:unitree_robots/go2/assets/thigh_mirror_0.obj

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/unitreerobotics__unitree_mujoco -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `7c2fd2ce44ed9e4f1d550ca1847c7c9e58f91be1`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '1eb6642e3f3fdfb7fb13a9794fd6a2dd93ea0e7d:unitree_robots/go2/assets/thigh_mirror_1.obj')` in `unitreerobotics__unitree_mujoco`. fatal: bad object 1eb6642e3f3fdfb7fb13a9794fd6a2dd93ea0e7d:unitree_robots/go2/assets/thigh_mirror_1.obj

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/unitreerobotics__unitree_mujoco -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `fb7e0b4963b9889fe6b1127bbca03844163b1bc7`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '1eb6642e3f3fdfb7fb13a9794fd6a2dd93ea0e7d:unitree_robots/go2/assets/calf_0.obj')` in `unitreerobotics__unitree_mujoco`. fatal: bad object 1eb6642e3f3fdfb7fb13a9794fd6a2dd93ea0e7d:unitree_robots/go2/assets/calf_0.obj

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/unitreerobotics__unitree_mujoco -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `1d9be4c392ba62a96a07043096d96d0a981fb9e9`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '1eb6642e3f3fdfb7fb13a9794fd6a2dd93ea0e7d:unitree_robots/go2/assets/calf_1.obj')` in `unitreerobotics__unitree_mujoco`. fatal: bad object 1eb6642e3f3fdfb7fb13a9794fd6a2dd93ea0e7d:unitree_robots/go2/assets/calf_1.obj

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/unitreerobotics__unitree_mujoco -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `01197551ce8ad7d7118590f949897c72a57b0e11`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '1eb6642e3f3fdfb7fb13a9794fd6a2dd93ea0e7d:unitree_robots/go2/assets/calf_mirror_0.obj')` in `unitreerobotics__unitree_mujoco`. fatal: bad object 1eb6642e3f3fdfb7fb13a9794fd6a2dd93ea0e7d:unitree_robots/go2/assets/calf_mirror_0.obj

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/unitreerobotics__unitree_mujoco -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `710bbe9ee5190e182e31730acb0e9ec6ed4c87db`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '1eb6642e3f3fdfb7fb13a9794fd6a2dd93ea0e7d:unitree_robots/go2/assets/calf_mirror_1.obj')` in `unitreerobotics__unitree_mujoco`. fatal: bad object 1eb6642e3f3fdfb7fb13a9794fd6a2dd93ea0e7d:unitree_robots/go2/assets/calf_mirror_1.obj

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/unitreerobotics__unitree_mujoco -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `6b27378a4e44d27bf974ec7ba311f5725c4dc2da`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '1eb6642e3f3fdfb7fb13a9794fd6a2dd93ea0e7d:unitree_robots/go2/assets/foot.obj')` in `unitreerobotics__unitree_mujoco`. fatal: bad object 1eb6642e3f3fdfb7fb13a9794fd6a2dd93ea0e7d:unitree_robots/go2/assets/foot.obj

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/unitreerobotics__unitree_mujoco -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `edc559eeb5b385e3df55573074e35ce1ef227a46`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '1eb6642e3f3fdfb7fb13a9794fd6a2dd93ea0e7d:unitree_robots/h2/meshes/pelvis.stl')` in `unitreerobotics__unitree_mujoco`. fatal: bad object 1eb6642e3f3fdfb7fb13a9794fd6a2dd93ea0e7d:unitree_robots/h2/meshes/pelvis.stl

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/unitreerobotics__unitree_mujoco -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `7a21a5e6e448ba381844d5f3807303eb2ecedea7`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '1eb6642e3f3fdfb7fb13a9794fd6a2dd93ea0e7d:unitree_robots/h2/meshes/left_hip_pitch_link.stl')` in `unitreerobotics__unitree_mujoco`. fatal: bad object 1eb6642e3f3fdfb7fb13a9794fd6a2dd93ea0e7d:unitree_robots/h2/meshes/left_hip_pitch_link.stl

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/unitreerobotics__unitree_mujoco -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `271a18b5f67d5bd743fc43cffb3dda43ea13a3ec`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '1eb6642e3f3fdfb7fb13a9794fd6a2dd93ea0e7d:unitree_robots/h2/meshes/left_hip_roll_link.stl')` in `unitreerobotics__unitree_mujoco`. fatal: bad object 1eb6642e3f3fdfb7fb13a9794fd6a2dd93ea0e7d:unitree_robots/h2/meshes/left_hip_roll_link.stl

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/unitreerobotics__unitree_mujoco -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `bfffc34821aba4621fd83852e26803fcb4bbaec0`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '1eb6642e3f3fdfb7fb13a9794fd6a2dd93ea0e7d:unitree_robots/h2/meshes/left_hip_yaw_link.stl')` in `unitreerobotics__unitree_mujoco`. fatal: bad object 1eb6642e3f3fdfb7fb13a9794fd6a2dd93ea0e7d:unitree_robots/h2/meshes/left_hip_yaw_link.stl

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/unitreerobotics__unitree_mujoco -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `d9e7c0eb8b0c798ff858fa28a2b6195af7c432fa`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '1eb6642e3f3fdfb7fb13a9794fd6a2dd93ea0e7d:unitree_robots/h2/meshes/left_knee_link.stl')` in `unitreerobotics__unitree_mujoco`. fatal: bad object 1eb6642e3f3fdfb7fb13a9794fd6a2dd93ea0e7d:unitree_robots/h2/meshes/left_knee_link.stl

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/unitreerobotics__unitree_mujoco -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `80eb125a451ba848ce4fc65e855855f53318803f`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '1eb6642e3f3fdfb7fb13a9794fd6a2dd93ea0e7d:unitree_robots/h2/meshes/left_ankle_pitch_link.stl')` in `unitreerobotics__unitree_mujoco`. fatal: bad object 1eb6642e3f3fdfb7fb13a9794fd6a2dd93ea0e7d:unitree_robots/h2/meshes/left_ankle_pitch_link.stl

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/unitreerobotics__unitree_mujoco -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `e1e5c1543067b36c56b4342bf9ae9ec3b06f23fd`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '1eb6642e3f3fdfb7fb13a9794fd6a2dd93ea0e7d:unitree_robots/h2/meshes/right_hip_pitch_link.stl')` in `unitreerobotics__unitree_mujoco`. fatal: bad object 1eb6642e3f3fdfb7fb13a9794fd6a2dd93ea0e7d:unitree_robots/h2/meshes/right_hip_pitch_link.stl

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/unitreerobotics__unitree_mujoco -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `3a806b8ce75929637ddcc3d1b1201dd3942de1a6`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '1eb6642e3f3fdfb7fb13a9794fd6a2dd93ea0e7d:unitree_robots/h2/meshes/right_hip_roll_link.stl')` in `unitreerobotics__unitree_mujoco`. fatal: bad object 1eb6642e3f3fdfb7fb13a9794fd6a2dd93ea0e7d:unitree_robots/h2/meshes/right_hip_roll_link.stl

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/unitreerobotics__unitree_mujoco -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `f3979893e1f006e6a58e108b1a3f7f650202a4a6`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '1eb6642e3f3fdfb7fb13a9794fd6a2dd93ea0e7d:unitree_robots/h2/meshes/right_hip_yaw_link.stl')` in `unitreerobotics__unitree_mujoco`. fatal: bad object 1eb6642e3f3fdfb7fb13a9794fd6a2dd93ea0e7d:unitree_robots/h2/meshes/right_hip_yaw_link.stl

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/unitreerobotics__unitree_mujoco -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `fd86ebdcf54133f995cef97b773f66e2effb7ea0`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '1eb6642e3f3fdfb7fb13a9794fd6a2dd93ea0e7d:unitree_robots/h2/meshes/right_knee_link.stl')` in `unitreerobotics__unitree_mujoco`. fatal: bad object 1eb6642e3f3fdfb7fb13a9794fd6a2dd93ea0e7d:unitree_robots/h2/meshes/right_knee_link.stl

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/unitreerobotics__unitree_mujoco -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `a4840778440d7f333e4017c0898e7d33eec2ee52`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '1eb6642e3f3fdfb7fb13a9794fd6a2dd93ea0e7d:unitree_robots/h2/meshes/right_ankle_pitch_link.stl')` in `unitreerobotics__unitree_mujoco`. fatal: bad object 1eb6642e3f3fdfb7fb13a9794fd6a2dd93ea0e7d:unitree_robots/h2/meshes/right_ankle_pitch_link.stl

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/unitreerobotics__unitree_mujoco -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `2b8858d6308a6aebd65762e3815c872653d05faa`

- Offline Git read failed (exit 128): `('show', '6a18beabefa9564d9b66c93fd671a8c7a4548601:urdf/RS/urdf/ReBot_Arm_RS.urdf')` in `Seeed-Projects__reBot-Isaacsim`. fatal: path 'urdf/RS/urdf/ReBot_Arm_RS.urdf' does not exist in '6a18beabefa9564d9b66c93fd671a8c7a4548601'

- Offline Git read failed (exit 128): `('show', '6a18beabefa9564d9b66c93fd671a8c7a4548601:urdf/reBot_B601_DM/urdf/reBot_B601_DM.urdf')` in `Seeed-Projects__reBot-Isaacsim`. fatal: path 'urdf/reBot_B601_DM/urdf/reBot_B601_DM.urdf' does not exist in '6a18beabefa9564d9b66c93fd671a8c7a4548601'

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '1eb6642e3f3fdfb7fb13a9794fd6a2dd93ea0e7d:unitree_robots/h2/meshes/torso_link.stl')` in `unitreerobotics__unitree_mujoco`. fatal: bad object 1eb6642e3f3fdfb7fb13a9794fd6a2dd93ea0e7d:unitree_robots/h2/meshes/torso_link.stl

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/unitreerobotics__unitree_mujoco -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `14b18e4385dd45683e2bef63561abbaf8cb4419f`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '1eb6642e3f3fdfb7fb13a9794fd6a2dd93ea0e7d:unitree_robots/h2/meshes/head_yaw_link.stl')` in `unitreerobotics__unitree_mujoco`. fatal: bad object 1eb6642e3f3fdfb7fb13a9794fd6a2dd93ea0e7d:unitree_robots/h2/meshes/head_yaw_link.stl

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/unitreerobotics__unitree_mujoco -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `5315c4fcf6cee14355b74ac1af4c98396227763b`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '1eb6642e3f3fdfb7fb13a9794fd6a2dd93ea0e7d:unitree_robots/h2/meshes/left_shoulder_pitch_link.stl')` in `unitreerobotics__unitree_mujoco`. fatal: bad object 1eb6642e3f3fdfb7fb13a9794fd6a2dd93ea0e7d:unitree_robots/h2/meshes/left_shoulder_pitch_link.stl

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/unitreerobotics__unitree_mujoco -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `5751053cd0830aa31d8481a48adbc43c9fd50f65`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '1eb6642e3f3fdfb7fb13a9794fd6a2dd93ea0e7d:unitree_robots/h2/meshes/left_shoulder_roll_link.stl')` in `unitreerobotics__unitree_mujoco`. fatal: bad object 1eb6642e3f3fdfb7fb13a9794fd6a2dd93ea0e7d:unitree_robots/h2/meshes/left_shoulder_roll_link.stl

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/unitreerobotics__unitree_mujoco -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `403ef5c8dbf946cc53d45795656c908ce26e79f2`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '1eb6642e3f3fdfb7fb13a9794fd6a2dd93ea0e7d:unitree_robots/h2/meshes/left_shoulder_yaw_link.stl')` in `unitreerobotics__unitree_mujoco`. fatal: bad object 1eb6642e3f3fdfb7fb13a9794fd6a2dd93ea0e7d:unitree_robots/h2/meshes/left_shoulder_yaw_link.stl

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/unitreerobotics__unitree_mujoco -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `ec0aa79ec9d8732a490dfaaf6e118a2703e08372`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '1eb6642e3f3fdfb7fb13a9794fd6a2dd93ea0e7d:unitree_robots/h2/meshes/left_elbow_link.stl')` in `unitreerobotics__unitree_mujoco`. fatal: bad object 1eb6642e3f3fdfb7fb13a9794fd6a2dd93ea0e7d:unitree_robots/h2/meshes/left_elbow_link.stl

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/unitreerobotics__unitree_mujoco -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `df94ac05f614197abbf45797e54b6dda7b07d53f`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '1eb6642e3f3fdfb7fb13a9794fd6a2dd93ea0e7d:unitree_robots/h2/meshes/left_wrist_roll_link.stl')` in `unitreerobotics__unitree_mujoco`. fatal: bad object 1eb6642e3f3fdfb7fb13a9794fd6a2dd93ea0e7d:unitree_robots/h2/meshes/left_wrist_roll_link.stl

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/unitreerobotics__unitree_mujoco -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `7e12a13a5ff0d5f477c9802f72fb8b8b79d8fd16`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '1eb6642e3f3fdfb7fb13a9794fd6a2dd93ea0e7d:unitree_robots/h2/meshes/left_wrist_yaw_link.stl')` in `unitreerobotics__unitree_mujoco`. fatal: bad object 1eb6642e3f3fdfb7fb13a9794fd6a2dd93ea0e7d:unitree_robots/h2/meshes/left_wrist_yaw_link.stl

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/unitreerobotics__unitree_mujoco -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `f5baaae36b21f21de0a4f0211e6d5799c19db900`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '1eb6642e3f3fdfb7fb13a9794fd6a2dd93ea0e7d:unitree_robots/h2/meshes/right_shoulder_pitch_link.stl')` in `unitreerobotics__unitree_mujoco`. fatal: bad object 1eb6642e3f3fdfb7fb13a9794fd6a2dd93ea0e7d:unitree_robots/h2/meshes/right_shoulder_pitch_link.stl

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/unitreerobotics__unitree_mujoco -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `7bba23bf0cdb310a72ebf0edc8fe4abd724ec178`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '1eb6642e3f3fdfb7fb13a9794fd6a2dd93ea0e7d:unitree_robots/h2/meshes/right_shoulder_roll_link.stl')` in `unitreerobotics__unitree_mujoco`. fatal: bad object 1eb6642e3f3fdfb7fb13a9794fd6a2dd93ea0e7d:unitree_robots/h2/meshes/right_shoulder_roll_link.stl

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/unitreerobotics__unitree_mujoco -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `0ba00e9ba0449c289b4378ebe64e3d8da1bc50cb`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '1eb6642e3f3fdfb7fb13a9794fd6a2dd93ea0e7d:unitree_robots/h2/meshes/right_shoulder_yaw_link.stl')` in `unitreerobotics__unitree_mujoco`. fatal: bad object 1eb6642e3f3fdfb7fb13a9794fd6a2dd93ea0e7d:unitree_robots/h2/meshes/right_shoulder_yaw_link.stl

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/unitreerobotics__unitree_mujoco -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `791be68f1584be2a27be9f9a30698c1f8d6767c1`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '1eb6642e3f3fdfb7fb13a9794fd6a2dd93ea0e7d:unitree_robots/h2/meshes/right_elbow_link.stl')` in `unitreerobotics__unitree_mujoco`. fatal: bad object 1eb6642e3f3fdfb7fb13a9794fd6a2dd93ea0e7d:unitree_robots/h2/meshes/right_elbow_link.stl

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/unitreerobotics__unitree_mujoco -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `807a9b4249c3a8088a0033e7f87aca67cc14be03`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '1eb6642e3f3fdfb7fb13a9794fd6a2dd93ea0e7d:unitree_robots/h2/meshes/right_wrist_roll_link.stl')` in `unitreerobotics__unitree_mujoco`. fatal: bad object 1eb6642e3f3fdfb7fb13a9794fd6a2dd93ea0e7d:unitree_robots/h2/meshes/right_wrist_roll_link.stl

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/unitreerobotics__unitree_mujoco -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `985d3124d9662cf8976421c5af4118d3573cd464`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '1eb6642e3f3fdfb7fb13a9794fd6a2dd93ea0e7d:unitree_robots/h2/meshes/right_wrist_yaw_link.stl')` in `unitreerobotics__unitree_mujoco`. fatal: bad object 1eb6642e3f3fdfb7fb13a9794fd6a2dd93ea0e7d:unitree_robots/h2/meshes/right_wrist_yaw_link.stl

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/unitreerobotics__unitree_mujoco -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `8f7b2e1336a3a334dff2d129734bcf29ae640d16`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '1eb6642e3f3fdfb7fb13a9794fd6a2dd93ea0e7d:unitree_robots/a2/qrc_map_flat.xml')` in `unitreerobotics__unitree_mujoco`. fatal: bad object 1eb6642e3f3fdfb7fb13a9794fd6a2dd93ea0e7d:unitree_robots/a2/qrc_map_flat.xml

- https://github.com/unitreerobotics/unitree_mujoco unitree_robots/a2/qrc_map_flat.xml at 1eb6642e3f3fdfb7fb13a9794fd6a2dd93ea0e7d: CalledProcessError: Command '['git', '-C', '.cache/unitreerobotics__unitree_mujoco', 'show', '1eb6642e3f3fdfb7fb13a9794fd6a2dd93ea0e7d:unitree_robots/a2/qrc_map_flat.xml']' returned non-zero exit status 128.

- Offline Git read failed (exit 128): `('show', '1eb6642e3f3fdfb7fb13a9794fd6a2dd93ea0e7d:unitree_robots/a2/qrc_map_sloped.xml')` in `unitreerobotics__unitree_mujoco`. fatal: bad object 1eb6642e3f3fdfb7fb13a9794fd6a2dd93ea0e7d:unitree_robots/a2/qrc_map_sloped.xml

- https://github.com/unitreerobotics/unitree_mujoco unitree_robots/a2/qrc_map_sloped.xml at 1eb6642e3f3fdfb7fb13a9794fd6a2dd93ea0e7d: CalledProcessError: Command '['git', '-C', '.cache/unitreerobotics__unitree_mujoco', 'show', '1eb6642e3f3fdfb7fb13a9794fd6a2dd93ea0e7d:unitree_robots/a2/qrc_map_sloped.xml']' returned non-zero exit status 128.

- https://github.com/unitreerobotics/unitree_ros robots/g1_description/g1_pl.urdf at 157ff950351e5f535e03c5d85a16b7d594b3dbcc: ValueError: Resource missing at 157ff950351e5f535e03c5d85a16b7d594b3dbcc: robots/g1_description/meshes/meshes/pelvis_ver0529.STL

- https://github.com/unitreerobotics/unitree_ros robots/g1_description/g1_comp.urdf at 157ff950351e5f535e03c5d85a16b7d594b3dbcc: ValueError: Resource missing at 157ff950351e5f535e03c5d85a16b7d594b3dbcc: robots/g1_description/meshes/meshes/pelvis.STL

- https://github.com/unitreerobotics/unitree_ros robots/g1_description/g1_23dof.urdf at 157ff950351e5f535e03c5d85a16b7d594b3dbcc: ValueError: Resource missing at 157ff950351e5f535e03c5d85a16b7d594b3dbcc: robots/g1_description/meshes/meshes/pelvis.STL

- https://github.com/unitreerobotics/unitree_ros robots/g1_description/g1_29dof.urdf at 157ff950351e5f535e03c5d85a16b7d594b3dbcc: ValueError: Resource missing at 157ff950351e5f535e03c5d85a16b7d594b3dbcc: robots/g1_description/meshes/meshes/pelvis.STL

- https://github.com/unitreerobotics/unitree_ros robots/g1_description/g1_dual_arm.urdf at 157ff950351e5f535e03c5d85a16b7d594b3dbcc: ValueError: Resource missing at 157ff950351e5f535e03c5d85a16b7d594b3dbcc: robots/g1_description/meshes/meshes/waist_yaw_link.STL

- https://github.com/unitreerobotics/unitree_ros robots/g1_description/g1_23dof_mode_10.urdf at 157ff950351e5f535e03c5d85a16b7d594b3dbcc: ValueError: Resource missing at 157ff950351e5f535e03c5d85a16b7d594b3dbcc: robots/g1_description/meshes/meshes/pelvis_ver0529.STL

- https://github.com/unitreerobotics/unitree_ros robots/g1_description/g1_23dof_rev_1_0.urdf at 157ff950351e5f535e03c5d85a16b7d594b3dbcc: ValueError: Resource missing at 157ff950351e5f535e03c5d85a16b7d594b3dbcc: robots/g1_description/meshes/meshes/pelvis.STL

- https://github.com/unitreerobotics/unitree_ros robots/g1_description/g1_29dof_mode_11.urdf at 157ff950351e5f535e03c5d85a16b7d594b3dbcc: ValueError: Resource missing at 157ff950351e5f535e03c5d85a16b7d594b3dbcc: robots/g1_description/meshes/meshes/pelvis_ver0529.STL

- https://github.com/unitreerobotics/unitree_ros robots/g1_description/g1_29dof_mode_12.urdf at 157ff950351e5f535e03c5d85a16b7d594b3dbcc: ValueError: Resource missing at 157ff950351e5f535e03c5d85a16b7d594b3dbcc: robots/g1_description/meshes/meshes/pelvis_ver0529.STL

- https://github.com/unitreerobotics/unitree_ros robots/g1_description/g1_29dof_mode_13.urdf at 157ff950351e5f535e03c5d85a16b7d594b3dbcc: ValueError: Resource missing at 157ff950351e5f535e03c5d85a16b7d594b3dbcc: robots/g1_description/meshes/meshes/pelvis.STL

- https://github.com/unitreerobotics/unitree_ros robots/g1_description/g1_29dof_mode_14.urdf at 157ff950351e5f535e03c5d85a16b7d594b3dbcc: ValueError: Resource missing at 157ff950351e5f535e03c5d85a16b7d594b3dbcc: robots/g1_description/meshes/meshes/pelvis.STL

- https://github.com/unitreerobotics/unitree_ros robots/g1_description/g1_29dof_mode_15.urdf at 157ff950351e5f535e03c5d85a16b7d594b3dbcc: ValueError: Resource missing at 157ff950351e5f535e03c5d85a16b7d594b3dbcc: robots/g1_description/meshes/meshes/pelvis_ver0529.STL

- https://github.com/unitreerobotics/unitree_ros robots/g1_description/g1_29dof_mode_16.urdf at 157ff950351e5f535e03c5d85a16b7d594b3dbcc: ValueError: Resource missing at 157ff950351e5f535e03c5d85a16b7d594b3dbcc: robots/g1_description/meshes/meshes/pelvis_ver0529.STL

- https://github.com/unitreerobotics/unitree_ros robots/g1_description/g1_29dof_mode_18.urdf at 157ff950351e5f535e03c5d85a16b7d594b3dbcc: ValueError: Resource missing at 157ff950351e5f535e03c5d85a16b7d594b3dbcc: robots/g1_description/meshes/meshes/pelvis_ver0529.STL

- https://github.com/unitreerobotics/unitree_ros robots/g1_description/g1_29dof_rev_1_0.urdf at 157ff950351e5f535e03c5d85a16b7d594b3dbcc: ValueError: Resource missing at 157ff950351e5f535e03c5d85a16b7d594b3dbcc: robots/g1_description/meshes/meshes/pelvis.STL

- https://github.com/unitreerobotics/unitree_ros robots/g1_description/g1_29dof_with_hand.urdf at 157ff950351e5f535e03c5d85a16b7d594b3dbcc: ValueError: Resource missing at 157ff950351e5f535e03c5d85a16b7d594b3dbcc: robots/g1_description/meshes/meshes/pelvis.STL

- https://github.com/unitreerobotics/unitree_ros robots/g1_description/g1_29dof_lock_waist.urdf at 157ff950351e5f535e03c5d85a16b7d594b3dbcc: ValueError: Resource missing at 157ff950351e5f535e03c5d85a16b7d594b3dbcc: robots/g1_description/meshes/meshes/pelvis.STL

- https://github.com/unitreerobotics/unitree_ros robots/g1_description/g1_29dof_with_hand_rev_1_0.urdf at 157ff950351e5f535e03c5d85a16b7d594b3dbcc: ValueError: Resource missing at 157ff950351e5f535e03c5d85a16b7d594b3dbcc: robots/g1_description/meshes/meshes/pelvis.STL

- https://github.com/unitreerobotics/unitree_ros robots/g1_description/inspire_hand/DFQ_left_hand.urdf at 157ff950351e5f535e03c5d85a16b7d594b3dbcc: ValueError: Resource missing at 157ff950351e5f535e03c5d85a16b7d594b3dbcc: robots/g1_description/inspire_hand/meshes/meshes/L_hand_base_link.STL

- https://github.com/unitreerobotics/unitree_ros robots/g1_description/inspire_hand/FTP_left_hand.urdf at 157ff950351e5f535e03c5d85a16b7d594b3dbcc: ValueError: Resource missing at 157ff950351e5f535e03c5d85a16b7d594b3dbcc: robots/g1_description/inspire_hand/meshes/meshes/left_base_link.STL

- https://github.com/unitreerobotics/unitree_ros robots/g1_description/g1_29dof_lock_waist_rev_1_0.urdf at 157ff950351e5f535e03c5d85a16b7d594b3dbcc: ValueError: Resource missing at 157ff950351e5f535e03c5d85a16b7d594b3dbcc: robots/g1_description/meshes/meshes/pelvis.STL

- https://github.com/unitreerobotics/unitree_ros robots/g1_description/inspire_hand/DFQ_right_hand.urdf at 157ff950351e5f535e03c5d85a16b7d594b3dbcc: ValueError: Resource missing at 157ff950351e5f535e03c5d85a16b7d594b3dbcc: robots/g1_description/inspire_hand/meshes/meshes/R_hand_base_link.STL

- https://github.com/unitreerobotics/unitree_ros robots/g1_description/inspire_hand/FTP_right_hand.urdf at 157ff950351e5f535e03c5d85a16b7d594b3dbcc: ValueError: Resource missing at 157ff950351e5f535e03c5d85a16b7d594b3dbcc: robots/g1_description/inspire_hand/meshes/meshes/right_base_link.STL

- https://github.com/unitreerobotics/unitree_ros robots/g1_description/g1_29dof_mode_15_with_dex1_1.urdf at 157ff950351e5f535e03c5d85a16b7d594b3dbcc: ValueError: Resource missing at 157ff950351e5f535e03c5d85a16b7d594b3dbcc: robots/g1_description/meshes/meshes/pelvis_ver0529.STL

- https://github.com/unitreerobotics/unitree_ros robots/g1_description/g1_29dof_lock_waist_with_hand_rev_1_0.urdf at 157ff950351e5f535e03c5d85a16b7d594b3dbcc: ValueError: Resource missing at 157ff950351e5f535e03c5d85a16b7d594b3dbcc: robots/g1_description/meshes/meshes/pelvis.STL

- https://github.com/unitreerobotics/unitree_ros robots/g1_description/g1_29dof_rev_1_0_with_inspire_hand_DFQ.urdf at 157ff950351e5f535e03c5d85a16b7d594b3dbcc: ValueError: Resource missing at 157ff950351e5f535e03c5d85a16b7d594b3dbcc: robots/g1_description/meshes/meshes/pelvis.STL

- https://github.com/unitreerobotics/unitree_ros robots/g1_description/g1_29dof_rev_1_0_with_inspire_hand_FTP.urdf at 157ff950351e5f535e03c5d85a16b7d594b3dbcc: ValueError: Resource missing at 157ff950351e5f535e03c5d85a16b7d594b3dbcc: robots/g1_description/meshes/meshes/pelvis.STL

- Offline Git read failed (exit 128): `('show', 'd9415a3076f921fdb9735d45d609a596df722468:unitree_g1/g1_with_hands.xml')` in `menagerie`. fatal: bad object d9415a3076f921fdb9735d45d609a596df722468:unitree_g1/g1_with_hands.xml

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/menagerie -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `a049a70e29f03f3f4a03dd8aded1e17f8cd8f285`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '157ff950351e5f535e03c5d85a16b7d594b3dbcc:robots/go1_description/meshes/trunk.dae')` in `unitree_ros`. fatal: bad object 157ff950351e5f535e03c5d85a16b7d594b3dbcc:robots/go1_description/meshes/trunk.dae

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/unitree_ros -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `848b762234aab6acec7f657f64ce30a6da95fd16`

- Network outcome: exit 0.

- https://github.com/unitreerobotics/unitree_ros robots/go1_description/xacro/robot.xacro at 157ff950351e5f535e03c5d85a16b7d594b3dbcc: ValueError: could not convert string to float: '${trunk_mass}'

- https://github.com/unitreerobotics/unitree_ros robots/go2_description/xacro/robot.xacro at 157ff950351e5f535e03c5d85a16b7d594b3dbcc: ValueError: Unresolved or ambiguous package path package://go2_description/meshes/trunk.dae: []

- https://github.com/unitreerobotics/unitree_ros robots/go2_description/urdf/go2_description.urdf at 157ff950351e5f535e03c5d85a16b7d594b3dbcc: ValueError: XML Error: repeated element: 'material'
Element 'material', line 13


- https://github.com/unitreerobotics/unitree_ros robots/z1_description/xacro/robot.xacro at 157ff950351e5f535e03c5d85a16b7d594b3dbcc: ValueError: could not convert string to float: '${L00_Mass}'

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 clone --filter=blob:limit=100k --no-checkout https://github.com/ros-industrial/universal_robot.git .cache/ros-industrial__universal_robot` — retrieve manufacturer source history and small text files. Parent process runs at nice 15; lazy fetching disabled.

- Network outcome: exit 0. Cloning into '.cache/ros-industrial__universal_robot'...

- Offline Git read failed (exit 128): `('show', '39ad110d8f2e8f66856a201cca88aa7a7025e3eb:ur_description/meshes/ur10e/visual/base.dae')` in `ros-industrial__universal_robot`. fatal: bad object 39ad110d8f2e8f66856a201cca88aa7a7025e3eb:ur_description/meshes/ur10e/visual/base.dae

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/ros-industrial__universal_robot -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `635873075c01c4b1dd627ee44642dca2b5573633`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '39ad110d8f2e8f66856a201cca88aa7a7025e3eb:ur_description/meshes/ur10e/visual/shoulder.dae')` in `ros-industrial__universal_robot`. fatal: bad object 39ad110d8f2e8f66856a201cca88aa7a7025e3eb:ur_description/meshes/ur10e/visual/shoulder.dae

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/ros-industrial__universal_robot -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `8c6a487e28d8f727696673a2f94d87f3c15a0488`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '39ad110d8f2e8f66856a201cca88aa7a7025e3eb:ur_description/meshes/ur10e/visual/upperarm.dae')` in `ros-industrial__universal_robot`. fatal: bad object 39ad110d8f2e8f66856a201cca88aa7a7025e3eb:ur_description/meshes/ur10e/visual/upperarm.dae

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/ros-industrial__universal_robot -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `501607b0b7942ed92ffdc152d9d7bd856776882a`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '39ad110d8f2e8f66856a201cca88aa7a7025e3eb:ur_description/meshes/ur10e/visual/forearm.dae')` in `ros-industrial__universal_robot`. fatal: bad object 39ad110d8f2e8f66856a201cca88aa7a7025e3eb:ur_description/meshes/ur10e/visual/forearm.dae

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/ros-industrial__universal_robot -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `e6d6c8c79153509f1989a7f801b04065eb4821ad`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '39ad110d8f2e8f66856a201cca88aa7a7025e3eb:ur_description/meshes/ur10e/visual/wrist1.dae')` in `ros-industrial__universal_robot`. fatal: bad object 39ad110d8f2e8f66856a201cca88aa7a7025e3eb:ur_description/meshes/ur10e/visual/wrist1.dae

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/ros-industrial__universal_robot -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `1cc3e20f4396e226aadc3ef1dc60f65bab57501f`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '39ad110d8f2e8f66856a201cca88aa7a7025e3eb:ur_description/meshes/ur10e/visual/wrist2.dae')` in `ros-industrial__universal_robot`. fatal: bad object 39ad110d8f2e8f66856a201cca88aa7a7025e3eb:ur_description/meshes/ur10e/visual/wrist2.dae

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/ros-industrial__universal_robot -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `d8ff99c63f5f0c5541aeaccc415f8451adc91fb6`

- Network outcome: exit 0.

- Historical source compile failed universal_robots_ur10e 8c84f2bc37883692b2d25c9081beeaa7330cfe59 ur_description/urdf/ur10e.xacro: Property names must not start with double underscore:__joint_limit_parameters

- Offline Git read failed (exit 128): `('show', '39ad110d8f2e8f66856a201cca88aa7a7025e3eb:ur_description/meshes/ur5e/visual/base.dae')` in `ros-industrial__universal_robot`. fatal: bad object 39ad110d8f2e8f66856a201cca88aa7a7025e3eb:ur_description/meshes/ur5e/visual/base.dae

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/ros-industrial__universal_robot -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `6933608f553ce3fa008db290231363e89c1915aa`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '39ad110d8f2e8f66856a201cca88aa7a7025e3eb:ur_description/meshes/ur5e/visual/shoulder.dae')` in `ros-industrial__universal_robot`. fatal: bad object 39ad110d8f2e8f66856a201cca88aa7a7025e3eb:ur_description/meshes/ur5e/visual/shoulder.dae

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/ros-industrial__universal_robot -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `3aad8fc4c146c960d0ea685aa22132c715854bdd`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '39ad110d8f2e8f66856a201cca88aa7a7025e3eb:ur_description/meshes/ur5e/visual/upperarm.dae')` in `ros-industrial__universal_robot`. fatal: bad object 39ad110d8f2e8f66856a201cca88aa7a7025e3eb:ur_description/meshes/ur5e/visual/upperarm.dae

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/ros-industrial__universal_robot -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `ac7d16fd300fd41543c8f6e0d853dbe5128ceb83`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '39ad110d8f2e8f66856a201cca88aa7a7025e3eb:ur_description/meshes/ur5e/visual/forearm.dae')` in `ros-industrial__universal_robot`. fatal: bad object 39ad110d8f2e8f66856a201cca88aa7a7025e3eb:ur_description/meshes/ur5e/visual/forearm.dae

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/ros-industrial__universal_robot -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `91938d0877e7882b134d4fb316e0cc3c688c11c8`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '39ad110d8f2e8f66856a201cca88aa7a7025e3eb:ur_description/meshes/ur5e/visual/wrist1.dae')` in `ros-industrial__universal_robot`. fatal: bad object 39ad110d8f2e8f66856a201cca88aa7a7025e3eb:ur_description/meshes/ur5e/visual/wrist1.dae

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/ros-industrial__universal_robot -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `347c3559124b0fd534cfb1017d264f7ad62ed3f2`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '39ad110d8f2e8f66856a201cca88aa7a7025e3eb:ur_description/meshes/ur5e/visual/wrist2.dae')` in `ros-industrial__universal_robot`. fatal: bad object 39ad110d8f2e8f66856a201cca88aa7a7025e3eb:ur_description/meshes/ur5e/visual/wrist2.dae

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/ros-industrial__universal_robot -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `ce9e7ec53a95099d32349ab2f50a3fdc085a4528`

- Network outcome: exit 0.

- Historical source compile failed universal_robots_ur5e 8c84f2bc37883692b2d25c9081beeaa7330cfe59 ur_description/urdf/ur5e.xacro: Property names must not start with double underscore:__joint_limit_parameters

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 clone --filter=blob:limit=100k --no-checkout https://github.com/simlabrobotics/allegro_hand_ros.git .cache/simlabrobotics__allegro_hand_ros` — retrieve manufacturer source history and small text files. Parent process runs at nice 15; lazy fetching disabled.

- Network outcome: exit 0. Cloning into '.cache/simlabrobotics__allegro_hand_ros'...

- Offline Git read failed (exit 128): `('show', '296ef6bae4b535ffb91420237cdc8a87f6e9f6df:allegro_hand_description/meshes/base_link.STL')` in `simlabrobotics__allegro_hand_ros`. fatal: bad object 296ef6bae4b535ffb91420237cdc8a87f6e9f6df:allegro_hand_description/meshes/base_link.STL

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/simlabrobotics__allegro_hand_ros -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `5901473f09f0cfad82e41fcd36d03782108c4eb2`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '296ef6bae4b535ffb91420237cdc8a87f6e9f6df:allegro_hand_description/meshes/link_12.0_right.STL')` in `simlabrobotics__allegro_hand_ros`. fatal: bad object 296ef6bae4b535ffb91420237cdc8a87f6e9f6df:allegro_hand_description/meshes/link_12.0_right.STL

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/simlabrobotics__allegro_hand_ros -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `7eecece57038320ffdc83558af35f57bc3f71772`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '296ef6bae4b535ffb91420237cdc8a87f6e9f6df:allegro_hand_description/meshes/base_link_left.STL')` in `simlabrobotics__allegro_hand_ros`. fatal: bad object 296ef6bae4b535ffb91420237cdc8a87f6e9f6df:allegro_hand_description/meshes/base_link_left.STL

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/simlabrobotics__allegro_hand_ros -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `365d7e7f7b850eb9b6013923f32274c6e1626d5a`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '296ef6bae4b535ffb91420237cdc8a87f6e9f6df:allegro_hand_description/meshes/link_12.0_left.STL')` in `simlabrobotics__allegro_hand_ros`. fatal: bad object 296ef6bae4b535ffb91420237cdc8a87f6e9f6df:allegro_hand_description/meshes/link_12.0_left.STL

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/simlabrobotics__allegro_hand_ros -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `aeaa37a195840df8149f0872866671a159529fbc`

- Network outcome: exit 0.

- Rejected unrelated historical README template for agilex_piper: 0bee963312f0f4a25b53cdf9afe744ca73f2d68a heading '## UMI-Gripper Description (MJCF)'

- Offline Git read failed (exit 128): `('show', '400b5f5b9fec382583f69b53b094a154d9dc7635:agilex_piper/CHANGELOG.md')` in `menagerie`. fatal: path 'agilex_piper/CHANGELOG.md' does not exist in '400b5f5b9fec382583f69b53b094a154d9dc7635'

- Offline Git read failed (exit 128): `('show', 'd9415a3076f921fdb9735d45d609a596df722468:apptronik_apollo/CHANGELOG.md')` in `menagerie`. fatal: bad object d9415a3076f921fdb9735d45d609a596df722468:apptronik_apollo/CHANGELOG.md

- Offline Git read failed (exit 128): `('show', '400b5f5b9fec382583f69b53b094a154d9dc7635:arx_l5/CHANGELOG.md')` in `menagerie`. fatal: path 'arx_l5/CHANGELOG.md' does not exist in '400b5f5b9fec382583f69b53b094a154d9dc7635'

- Offline Git read failed (exit 128): `('show', 'd9415a3076f921fdb9735d45d609a596df722468:berkeley_humanoid/CHANGELOG.md')` in `menagerie`. fatal: bad object d9415a3076f921fdb9735d45d609a596df722468:berkeley_humanoid/CHANGELOG.md

- Offline Git read failed (exit 128): `('show', 'd9415a3076f921fdb9735d45d609a596df722468:booster_t1/CHANGELOG.md')` in `menagerie`. fatal: bad object d9415a3076f921fdb9735d45d609a596df722468:booster_t1/CHANGELOG.md

- Offline Git read failed (exit 128): `('show', 'd9415a3076f921fdb9735d45d609a596df722468:fourier_n1/CHANGELOG.md')` in `menagerie`. fatal: bad object d9415a3076f921fdb9735d45d609a596df722468:fourier_n1/CHANGELOG.md

- Offline Git read failed (exit 128): `('show', '400b5f5b9fec382583f69b53b094a154d9dc7635:fourier_n1/CHANGELOG.md')` in `menagerie`. fatal: path 'fourier_n1/CHANGELOG.md' does not exist in '400b5f5b9fec382583f69b53b094a154d9dc7635'

- Offline Git read failed (exit 128): `('show', 'db140ade7ee4cb59629f9687aafc65af663d5bbe:franka_fr3_v2/README.md')` in `menagerie`. fatal: path 'franka_fr3_v2/README.md' does not exist in 'db140ade7ee4cb59629f9687aafc65af663d5bbe'

- Offline Git read failed (exit 128): `('show', 'cd7fc51b704c3cba05748bd5537cb17990b341eb:franka_fr3_v2/README.md')` in `menagerie`. fatal: path 'franka_fr3_v2/README.md' does not exist in 'cd7fc51b704c3cba05748bd5537cb17990b341eb'

- Offline Git read failed (exit 128): `('show', '400b5f5b9fec382583f69b53b094a154d9dc7635:franka_fr3_v2/README.md')` in `menagerie`. fatal: path 'franka_fr3_v2/README.md' does not exist in '400b5f5b9fec382583f69b53b094a154d9dc7635'

- Offline Git read failed (exit 128): `('show', 'acbbf1636fcfef9b437a6eb8c6f84380fb4aa998:franka_fr3_v2/README.md')` in `menagerie`. fatal: path 'franka_fr3_v2/README.md' does not exist in 'acbbf1636fcfef9b437a6eb8c6f84380fb4aa998'

- Offline Git read failed (exit 128): `('show', '7876dcdef0d912387441616526ed236142f047d3:franka_fr3_v2/README.md')` in `menagerie`. fatal: path 'franka_fr3_v2/README.md' does not exist in '7876dcdef0d912387441616526ed236142f047d3'

- Offline Git read failed (exit 128): `('show', 'b5ebfe0cf079d2b96acf0a5c0e29ee0c95ba32f4:google_robot/README.md')` in `menagerie`. fatal: path 'google_robot/README.md' does not exist in 'b5ebfe0cf079d2b96acf0a5c0e29ee0c95ba32f4'

- Offline Git read failed (exit 128): `('show', '5ce04bea98bbfca277a8d50b55ba3c7c4a62bdec:i2rt_yam/CHANGELOG.md')` in `menagerie`. fatal: path 'i2rt_yam/CHANGELOG.md' does not exist in '5ce04bea98bbfca277a8d50b55ba3c7c4a62bdec'

- Offline Git read failed (exit 128): `('show', 'a88bc450470d97ebc1f282e5969675fb4d1f0ed7:low_cost_robot_arm/README.md')` in `menagerie`. fatal: path 'low_cost_robot_arm/README.md' does not exist in 'a88bc450470d97ebc1f282e5969675fb4d1f0ed7'

- Offline Git read failed (exit 128): `('show', 'd74280a600a9afdfcb98d8917d0c79c86539aa61:low_cost_robot_arm/README.md')` in `menagerie`. fatal: path 'low_cost_robot_arm/README.md' does not exist in 'd74280a600a9afdfcb98d8917d0c79c86539aa61'

- Offline Git read failed (exit 128): `('show', '13d6c48b8f59d2c4badee7756b4ea3532613cddf:low_cost_robot_arm/README.md')` in `menagerie`. fatal: path 'low_cost_robot_arm/README.md' does not exist in '13d6c48b8f59d2c4badee7756b4ea3532613cddf'

- Offline Git read failed (exit 128): `('show', 'fae9ee82330444eec4e87568c838b99a09a39467:rainbow_robotics_rby1/README.md')` in `menagerie`. fatal: path 'rainbow_robotics_rby1/README.md' does not exist in 'fae9ee82330444eec4e87568c838b99a09a39467'

- Offline Git read failed (exit 128): `('show', '04674c8d0a4e12e33980a9e47fb604adc281fcc8:robotstudio_so101/CHANGELOG.md')` in `menagerie`. fatal: path 'robotstudio_so101/CHANGELOG.md' does not exist in '04674c8d0a4e12e33980a9e47fb604adc281fcc8'

- Offline Git read failed (exit 128): `('show', '5ce04bea98bbfca277a8d50b55ba3c7c4a62bdec:robotstudio_so101/CHANGELOG.md')` in `menagerie`. fatal: path 'robotstudio_so101/CHANGELOG.md' does not exist in '5ce04bea98bbfca277a8d50b55ba3c7c4a62bdec'

- Offline Git read failed (exit 128): `('show', '4a7015530bd7a4161103ae8f0905a96481e4cc1a:robotstudio_so101/CHANGELOG.md')` in `menagerie`. fatal: path 'robotstudio_so101/CHANGELOG.md' does not exist in '4a7015530bd7a4161103ae8f0905a96481e4cc1a'

- Offline Git read failed (exit 128): `('show', 'bf110a75a56e5bd146c7ed76965737c71d48425d:shadow_dexee/README.md')` in `menagerie`. fatal: path 'shadow_dexee/README.md' does not exist in 'bf110a75a56e5bd146c7ed76965737c71d48425d'

- Offline Git read failed (exit 128): `('show', '04674c8d0a4e12e33980a9e47fb604adc281fcc8:tetheria_aero_hand_open/CHANGELOG.md')` in `menagerie`. fatal: path 'tetheria_aero_hand_open/CHANGELOG.md' does not exist in '04674c8d0a4e12e33980a9e47fb604adc281fcc8'

- Offline Git read failed (exit 128): `('show', '400b5f5b9fec382583f69b53b094a154d9dc7635:tetheria_aero_hand_open/CHANGELOG.md')` in `menagerie`. fatal: path 'tetheria_aero_hand_open/CHANGELOG.md' does not exist in '400b5f5b9fec382583f69b53b094a154d9dc7635'

- Offline Git read failed (exit 128): `('show', '04674c8d0a4e12e33980a9e47fb604adc281fcc8:toddlerbot_2xc/CHANGELOG.md')` in `menagerie`. fatal: path 'toddlerbot_2xc/CHANGELOG.md' does not exist in '04674c8d0a4e12e33980a9e47fb604adc281fcc8'

- Offline Git read failed (exit 128): `('show', '9e7f8d4dda07f5c281b6c0c6f0d07b9dd267b762:toddlerbot_2xc/CHANGELOG.md')` in `menagerie`. fatal: path 'toddlerbot_2xc/CHANGELOG.md' does not exist in '9e7f8d4dda07f5c281b6c0c6f0d07b9dd267b762'

- Offline Git read failed (exit 128): `('show', '400b5f5b9fec382583f69b53b094a154d9dc7635:toddlerbot_2xc/CHANGELOG.md')` in `menagerie`. fatal: path 'toddlerbot_2xc/CHANGELOG.md' does not exist in '400b5f5b9fec382583f69b53b094a154d9dc7635'

- Offline Git read failed (exit 128): `('show', '04674c8d0a4e12e33980a9e47fb604adc281fcc8:toddlerbot_2xm/CHANGELOG.md')` in `menagerie`. fatal: path 'toddlerbot_2xm/CHANGELOG.md' does not exist in '04674c8d0a4e12e33980a9e47fb604adc281fcc8'

- Offline Git read failed (exit 128): `('show', '9e7f8d4dda07f5c281b6c0c6f0d07b9dd267b762:toddlerbot_2xm/CHANGELOG.md')` in `menagerie`. fatal: path 'toddlerbot_2xm/CHANGELOG.md' does not exist in '9e7f8d4dda07f5c281b6c0c6f0d07b9dd267b762'

- Offline Git read failed (exit 128): `('show', '400b5f5b9fec382583f69b53b094a154d9dc7635:toddlerbot_2xm/CHANGELOG.md')` in `menagerie`. fatal: path 'toddlerbot_2xm/CHANGELOG.md' does not exist in '400b5f5b9fec382583f69b53b094a154d9dc7635'

- Offline Git read failed (exit 128): `('show', '400b5f5b9fec382583f69b53b094a154d9dc7635:trossen_wxai/README.md')` in `menagerie`. fatal: path 'trossen_wxai/README.md' does not exist in '400b5f5b9fec382583f69b53b094a154d9dc7635'

- Offline Git read failed (exit 128): `('show', '477ec56566682d663b996d86a188c75499e74b98:trossen_wxai/README.md')` in `menagerie`. fatal: path 'trossen_wxai/README.md' does not exist in '477ec56566682d663b996d86a188c75499e74b98'

- Offline Git read failed (exit 128): `('show', 'd9415a3076f921fdb9735d45d609a596df722468:unitree_g1/CHANGELOG.md')` in `menagerie`. fatal: bad object d9415a3076f921fdb9735d45d609a596df722468:unitree_g1/CHANGELOG.md

- Menagerie self-comparison compile failed: aloha/filtered_cartesian_actuators.xml: ValueError: Error: transmission target 'left/gripper' not found in actuator 0
Element name 'left/X', id 0, line 36

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 clone --filter=blob:limit=100k --no-checkout https://github.com/LNSGroup/MS-Human-700.git .cache/LNSGroup__MS-Human-700` — retrieve manufacturer source history and small text files. Parent process runs at nice 15; lazy fetching disabled.

- Network outcome: exit 0. Cloning into '.cache/LNSGroup__MS-Human-700'...

- Offline Git read failed (exit 128): `('show', '2d686957aefd5739cf4d2859a6acfd94c8f84400:Body_Primary/Body_Torso_Simple.xml')` in `LNSGroup__MS-Human-700`. fatal: bad object 2d686957aefd5739cf4d2859a6acfd94c8f84400:Body_Primary/Body_Torso_Simple.xml

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/LNSGroup__MS-Human-700 -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `45a75eb4bf24ddbdb0c2800b395a8b9607f83af2`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '2d686957aefd5739cf4d2859a6acfd94c8f84400:Body_Primary/Body_Primary/Body_Arm_r.xml')` in `LNSGroup__MS-Human-700`. fatal: path 'Body_Primary/Body_Primary/Body_Arm_r.xml' does not exist in '2d686957aefd5739cf4d2859a6acfd94c8f84400'

- Offline Git read failed (exit 128): `('rev-parse', '2d686957aefd5739cf4d2859a6acfd94c8f84400:Body_Primary/Body_Primary/Body_Arm_r.xml')` in `LNSGroup__MS-Human-700`. fatal: path 'Body_Primary/Body_Primary/Body_Arm_r.xml' does not exist in '2d686957aefd5739cf4d2859a6acfd94c8f84400'

- Targeted fetch failed for https://github.com/LNSGroup/MS-Human-700 2d686957aefd5739cf4d2859a6acfd94c8f84400:Body_Primary/Body_Primary/Body_Arm_r.xml: Command '['git', '-C', '.cache/LNSGroup__MS-Human-700', 'rev-parse', '2d686957aefd5739cf4d2859a6acfd94c8f84400:Body_Primary/Body_Primary/Body_Arm_r.xml']' returned non-zero exit status 128.

- https://github.com/LNSGroup/MS-Human-700 MS-Human-700.xml at 2d686957aefd5739cf4d2859a6acfd94c8f84400: CalledProcessError: Command '['git', '-C', '.cache/LNSGroup__MS-Human-700', 'show', '2d686957aefd5739cf4d2859a6acfd94c8f84400:Body_Primary/Body_Primary/Body_Arm_r.xml']' returned non-zero exit status 128.

- Offline Git read failed (exit 128): `('show', '2d686957aefd5739cf4d2859a6acfd94c8f84400:Body_Locomotion/Body_Torso_Simple.xml')` in `LNSGroup__MS-Human-700`. fatal: bad object 2d686957aefd5739cf4d2859a6acfd94c8f84400:Body_Locomotion/Body_Torso_Simple.xml

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/LNSGroup__MS-Human-700 -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `f117dfbf0a1c059a3e38692003228e37148cf7b2`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '2d686957aefd5739cf4d2859a6acfd94c8f84400:Body_Locomotion/Body_Locomotion/Body_Arm_r.xml')` in `LNSGroup__MS-Human-700`. fatal: path 'Body_Locomotion/Body_Locomotion/Body_Arm_r.xml' does not exist in '2d686957aefd5739cf4d2859a6acfd94c8f84400'

- Offline Git read failed (exit 128): `('rev-parse', '2d686957aefd5739cf4d2859a6acfd94c8f84400:Body_Locomotion/Body_Locomotion/Body_Arm_r.xml')` in `LNSGroup__MS-Human-700`. fatal: path 'Body_Locomotion/Body_Locomotion/Body_Arm_r.xml' does not exist in '2d686957aefd5739cf4d2859a6acfd94c8f84400'

- Targeted fetch failed for https://github.com/LNSGroup/MS-Human-700 2d686957aefd5739cf4d2859a6acfd94c8f84400:Body_Locomotion/Body_Locomotion/Body_Arm_r.xml: Command '['git', '-C', '.cache/LNSGroup__MS-Human-700', 'rev-parse', '2d686957aefd5739cf4d2859a6acfd94c8f84400:Body_Locomotion/Body_Locomotion/Body_Arm_r.xml']' returned non-zero exit status 128.

- https://github.com/LNSGroup/MS-Human-700 MS-Human-700-Locomotion.xml at 2d686957aefd5739cf4d2859a6acfd94c8f84400: CalledProcessError: Command '['git', '-C', '.cache/LNSGroup__MS-Human-700', 'show', '2d686957aefd5739cf4d2859a6acfd94c8f84400:Body_Locomotion/Body_Locomotion/Body_Arm_r.xml']' returned non-zero exit status 128.

- Offline Git read failed (exit 128): `('show', '2d686957aefd5739cf4d2859a6acfd94c8f84400:Body_Manipulation/Body_Torso_Unimanual.xml')` in `LNSGroup__MS-Human-700`. fatal: bad object 2d686957aefd5739cf4d2859a6acfd94c8f84400:Body_Manipulation/Body_Torso_Unimanual.xml

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/LNSGroup__MS-Human-700 -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `96178313c5f7d252f2cc40db4c1f8dace8bdb3a3`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '2d686957aefd5739cf4d2859a6acfd94c8f84400:Body_Manipulation/Body_Manipulation/Body_Arm_Hand_r.xml')` in `LNSGroup__MS-Human-700`. fatal: path 'Body_Manipulation/Body_Manipulation/Body_Arm_Hand_r.xml' does not exist in '2d686957aefd5739cf4d2859a6acfd94c8f84400'

- Offline Git read failed (exit 128): `('rev-parse', '2d686957aefd5739cf4d2859a6acfd94c8f84400:Body_Manipulation/Body_Manipulation/Body_Arm_Hand_r.xml')` in `LNSGroup__MS-Human-700`. fatal: path 'Body_Manipulation/Body_Manipulation/Body_Arm_Hand_r.xml' does not exist in '2d686957aefd5739cf4d2859a6acfd94c8f84400'

- Targeted fetch failed for https://github.com/LNSGroup/MS-Human-700 2d686957aefd5739cf4d2859a6acfd94c8f84400:Body_Manipulation/Body_Manipulation/Body_Arm_Hand_r.xml: Command '['git', '-C', '.cache/LNSGroup__MS-Human-700', 'rev-parse', '2d686957aefd5739cf4d2859a6acfd94c8f84400:Body_Manipulation/Body_Manipulation/Body_Arm_Hand_r.xml']' returned non-zero exit status 128.

- https://github.com/LNSGroup/MS-Human-700 MS-Human-700-Manipulation.xml at 2d686957aefd5739cf4d2859a6acfd94c8f84400: CalledProcessError: Command '['git', '-C', '.cache/LNSGroup__MS-Human-700', 'show', '2d686957aefd5739cf4d2859a6acfd94c8f84400:Body_Manipulation/Body_Manipulation/Body_Arm_Hand_r.xml']' returned non-zero exit status 128.

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 clone --filter=blob:limit=100k --no-checkout https://github.com/hshi74/toddlerbot.git .cache/hshi74__toddlerbot` — retrieve manufacturer source history and small text files. Parent process runs at nice 15; lazy fetching disabled.

- Network outcome: exit 0. Cloning into '.cache/hshi74__toddlerbot'...

- Offline Git read failed (exit 128): `('show', '156d1802bfb117f219dbfce7597d283d5fabc968:spot_description/meshes/base/visual/body.obj')` in `rai-opensource__spot_description`. fatal: bad object 156d1802bfb117f219dbfce7597d283d5fabc968:spot_description/meshes/base/visual/body.obj

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/rai-opensource__spot_description -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `50fb5b5f8b88989dd2555e0d0070e4904145952e`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '156d1802bfb117f219dbfce7597d283d5fabc968:spot_description/meshes/base/visual/front_left_hip.obj')` in `rai-opensource__spot_description`. fatal: bad object 156d1802bfb117f219dbfce7597d283d5fabc968:spot_description/meshes/base/visual/front_left_hip.obj

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/rai-opensource__spot_description -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `6501e809c10acc646a23180731c6634c3e447a93`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '156d1802bfb117f219dbfce7597d283d5fabc968:spot_description/meshes/base/visual/front_left_upper_leg.obj')` in `rai-opensource__spot_description`. fatal: bad object 156d1802bfb117f219dbfce7597d283d5fabc968:spot_description/meshes/base/visual/front_left_upper_leg.obj

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/rai-opensource__spot_description -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `5bf27a14284c3bfb99a16c13ae0d6b0bca289d7e`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '156d1802bfb117f219dbfce7597d283d5fabc968:spot_description/meshes/base/visual/front_left_lower_leg.obj')` in `rai-opensource__spot_description`. fatal: bad object 156d1802bfb117f219dbfce7597d283d5fabc968:spot_description/meshes/base/visual/front_left_lower_leg.obj

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/rai-opensource__spot_description -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `46c68f2f350c44a8d30e4d2df62ec43766bb5071`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '156d1802bfb117f219dbfce7597d283d5fabc968:spot_description/meshes/base/visual/front_right_hip.obj')` in `rai-opensource__spot_description`. fatal: bad object 156d1802bfb117f219dbfce7597d283d5fabc968:spot_description/meshes/base/visual/front_right_hip.obj

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/rai-opensource__spot_description -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `ba2ce00eea6c175b5db2bd974b01636da876cfa1`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '156d1802bfb117f219dbfce7597d283d5fabc968:spot_description/meshes/base/visual/front_right_upper_leg.obj')` in `rai-opensource__spot_description`. fatal: bad object 156d1802bfb117f219dbfce7597d283d5fabc968:spot_description/meshes/base/visual/front_right_upper_leg.obj

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/rai-opensource__spot_description -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `546f414fbe9e21d87c41a7e7e0f9be111e5d4a96`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '156d1802bfb117f219dbfce7597d283d5fabc968:spot_description/meshes/base/visual/front_right_lower_leg.obj')` in `rai-opensource__spot_description`. fatal: bad object 156d1802bfb117f219dbfce7597d283d5fabc968:spot_description/meshes/base/visual/front_right_lower_leg.obj

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/rai-opensource__spot_description -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `f41214056ce4a50efceea95a5c9e899d2d742767`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '156d1802bfb117f219dbfce7597d283d5fabc968:spot_description/meshes/base/visual/rear_left_hip.obj')` in `rai-opensource__spot_description`. fatal: bad object 156d1802bfb117f219dbfce7597d283d5fabc968:spot_description/meshes/base/visual/rear_left_hip.obj

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/rai-opensource__spot_description -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `70198637b68b94dc1273745dc21b84e2c4a643ee`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '156d1802bfb117f219dbfce7597d283d5fabc968:spot_description/meshes/base/visual/rear_left_upper_leg.obj')` in `rai-opensource__spot_description`. fatal: bad object 156d1802bfb117f219dbfce7597d283d5fabc968:spot_description/meshes/base/visual/rear_left_upper_leg.obj

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/rai-opensource__spot_description -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `3a699e6f7b3a9a33dc5560920a539056b9f7a09b`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '156d1802bfb117f219dbfce7597d283d5fabc968:spot_description/meshes/base/visual/rear_left_lower_leg.obj')` in `rai-opensource__spot_description`. fatal: bad object 156d1802bfb117f219dbfce7597d283d5fabc968:spot_description/meshes/base/visual/rear_left_lower_leg.obj

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/rai-opensource__spot_description -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `3a1f50c7c4182269e605cd0b85e6969411e64618`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '156d1802bfb117f219dbfce7597d283d5fabc968:spot_description/meshes/base/visual/rear_right_hip.obj')` in `rai-opensource__spot_description`. fatal: bad object 156d1802bfb117f219dbfce7597d283d5fabc968:spot_description/meshes/base/visual/rear_right_hip.obj

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/rai-opensource__spot_description -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `82b9d260f946f091eb7868ef1424295864fd2a2d`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '156d1802bfb117f219dbfce7597d283d5fabc968:spot_description/meshes/base/visual/rear_right_upper_leg.obj')` in `rai-opensource__spot_description`. fatal: bad object 156d1802bfb117f219dbfce7597d283d5fabc968:spot_description/meshes/base/visual/rear_right_upper_leg.obj

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/rai-opensource__spot_description -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `392b2a62c7c86a0c0c0cd4e46ea7f3d4059ac62f`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '156d1802bfb117f219dbfce7597d283d5fabc968:spot_description/meshes/base/visual/rear_right_lower_leg.obj')` in `rai-opensource__spot_description`. fatal: bad object 156d1802bfb117f219dbfce7597d283d5fabc968:spot_description/meshes/base/visual/rear_right_lower_leg.obj

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/rai-opensource__spot_description -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `00dae988bb8f0e2febbd7fa91fa5345dcbdb0d9b`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '7a87097c499e3b0b69518d54a8e7a9ac1924e87c:realsense2_description/meshes/d435.dae')` in `IntelRealSense__realsense-ros`. fatal: bad object 7a87097c499e3b0b69518d54a8e7a9ac1924e87c:realsense2_description/meshes/d435.dae

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/IntelRealSense__realsense-ros -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `0ed32368fc5ba6912be530395a72553de9f21d9e`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('log', '--all', '--follow', '--find-renames=100%', '--format=@@@%H|%ct|%cI|%s', '--name-status', '--', 'realsense2_description/urdf/_d435i.urdf.xacro')` in `IntelRealSense__realsense-ros`. warning: lazy fetching disabled; some objects may not be available
fatal: could not fetch 6c6c82b0585c375526839fb94d52f173291457ed from promisor remote

- Repair check failed realsense_d435i: CalledProcessError: Command '['git', '-C', '.cache/IntelRealSense__realsense-ros', 'log', '--all', '--follow', '--find-renames=100%', '--format=@@@%H|%ct|%cI|%s', '--name-status', '--', 'realsense2_description/urdf/_d435i.urdf.xacro']' returned non-zero exit status 128.

- https://github.com/shadow-robot/sr_common sr_description/hand/xacro/forearm/forearm_e.urdf.xacro at 172c3d9c3715ee75eb10dfe4ee57e26a342b4529: ValueError: Macro-only input has no uniquely identified robot macro

- https://github.com/xArm-Developer/xarm_ros2 xarm_description/urdf/lite6/lite6.urdf.xacro at ac736c92b02de7ca7e0be6f737d77d46707464d8: XacroException: name 'use_xacro_load_yaml' is not defined
when evaluating expression 'use_xacro_load_yaml'

- https://github.com/xArm-Developer/xarm_ros2 xarm_description/urdf/lite6/lite6_robot_macro.xacro at ac736c92b02de7ca7e0be6f737d77d46707464d8: XacroException: name 'is_ros2' is not defined
when evaluating expression 'is_ros2'

- https://github.com/xArm-Developer/xarm_ros xarm_description/urdf/xarm7/xarm7.urdf.xacro at cf51617d98bc55a88d9aa735acfa43a0bbb8e425: XacroException: name 'mesh_suffix' is not defined
when evaluating expression 'mesh_suffix == 'dae' or (model_num >= 1305 and model_num != 1380)'

- https://github.com/xArm-Developer/xarm_ros xarm_description/urdf/xarm7/xarm7_robot_macro.xacro at cf51617d98bc55a88d9aa735acfa43a0bbb8e425: XacroException: name 'is_ros2' is not defined
when evaluating expression 'is_ros2'

- https://github.com/pal-robotics/talos_robot talos_description/urdf/arm/arm.urdf.xacro at 79709aa4f4f453ec18a5e467e65f84ff58ea24d0: ValueError: Macro talos_arm requires unsupported explicit arguments: ['side', 'reflect']

- https://github.com/pal-robotics/talos_robot talos_description/urdf/leg/leg.urdf.xacro at 79709aa4f4f453ec18a5e467e65f84ff58ea24d0: ValueError: Macro talos_leg requires unsupported explicit arguments: ['reflect']

- https://github.com/pal-robotics/talos_robot talos_description/gazebo/gazebo.urdf.xacro at 79709aa4f4f453ec18a5e467e65f84ff58ea24d0: XacroException: No such file or directory: .cache/pal-robotics__talos_robot/.drift_xacro/tmp3trprj_5/.unresolved_package/pal_urdf_utils/urdf/interaction_sensors/imu_talos.gazebo.xacro [Errno 2] No such file or directory: '.cache/pal-robotics__talos_robot/.drift_xacro/tmp3trprj_5/.unresolved_package/pal_urdf_utils/urdf/interaction_sensors/imu_talos.gazebo.xacro'

- https://github.com/pal-robotics/talos_robot talos_description/urdf/arm/wrist.urdf.xacro at 79709aa4f4f453ec18a5e467e65f84ff58ea24d0: ValueError: Macro talos_wrist requires unsupported explicit arguments: ['side', 'reflect']

- https://github.com/pal-robotics/talos_robot talos_description/urdf/head/head.urdf.xacro at 79709aa4f4f453ec18a5e467e65f84ff58ea24d0: ValueError: Macro-only input has no uniquely identified robot macro

- https://github.com/pal-robotics/talos_robot talos_description/urdf/crane/crane.urdf.xacro at 79709aa4f4f453ec18a5e467e65f84ff58ea24d0: XacroException: No such file or directory: .cache/pal-robotics__talos_robot/.drift_xacro/tmpv4i45_kc/.unresolved_package/pal_urdf_utils/urdf/deg_to_rad.urdf.xacro [Errno 2] No such file or directory: '.cache/pal-robotics__talos_robot/.drift_xacro/tmpv4i45_kc/.unresolved_package/pal_urdf_utils/urdf/deg_to_rad.urdf.xacro'

- https://github.com/pal-robotics/talos_robot talos_description/urdf/torso/torso.urdf.xacro at 79709aa4f4f453ec18a5e467e65f84ff58ea24d0: XacroException: No such file or directory: .cache/pal-robotics__talos_robot/.drift_xacro/tmpvsu75ztq/.unresolved_package/pal_urdf_utils/urdf/deg_to_rad.urdf.xacro [Errno 2] No such file or directory: '.cache/pal-robotics__talos_robot/.drift_xacro/tmpvsu75ztq/.unresolved_package/pal_urdf_utils/urdf/deg_to_rad.urdf.xacro'

- https://github.com/pal-robotics/talos_robot talos_description/urdf/capsule_collision.xacro at 79709aa4f4f453ec18a5e467e65f84ff58ea24d0: ValueError: Macro capsule-collision requires unsupported explicit arguments: ['e1', 'e2', 'rad', 'clen', 'rpy', 'mid']

- https://github.com/pal-robotics/talos_robot talos_description/robots/talos_full_v2.urdf.xacro at 79709aa4f4f453ec18a5e467e65f84ff58ea24d0: XacroException: No such file or directory: .cache/pal-robotics__talos_robot/.drift_xacro/tmpqs1cxmx9/.unresolved_package/pal_urdf_utils/urdf/deg_to_rad.urdf.xacro [Errno 2] No such file or directory: '.cache/pal-robotics__talos_robot/.drift_xacro/tmpqs1cxmx9/.unresolved_package/pal_urdf_utils/urdf/deg_to_rad.urdf.xacro'

- https://github.com/pal-robotics/talos_robot talos_description/urdf/arm/arm.ros2_control.xacro at 79709aa4f4f453ec18a5e467e65f84ff58ea24d0: ValueError: Macro ros2_control_arm requires unsupported explicit arguments: ['side', 'number', 'joint_offset']

- https://github.com/pal-robotics/talos_robot talos_description/urdf/arm/arm.transmission.xacro at 79709aa4f4f453ec18a5e467e65f84ff58ea24d0: ValueError: Macro talos_arm_simple_transmission requires unsupported explicit arguments: ['side', 'number', 'reduction', 'offset_value']

- https://github.com/pal-robotics/talos_robot talos_description/urdf/gripper/gripper.urdf.xacro at 79709aa4f4f453ec18a5e467e65f84ff58ea24d0: ValueError: Macro talos_gripper requires unsupported explicit arguments: ['reflect']

- https://github.com/pal-robotics/talos_robot talos_description/urdf/leg/foot_frames.urdf.xacro at 79709aa4f4f453ec18a5e467e65f84ff58ea24d0: ValueError: Macro talos_foot_frames requires unsupported explicit arguments: ['side']

- https://github.com/pal-robotics/talos_robot talos_description/urdf/leg/leg.ros2_control.xacro at 79709aa4f4f453ec18a5e467e65f84ff58ea24d0: ValueError: Macro ros2_control_leg requires unsupported explicit arguments: ['side', 'number']

- https://github.com/pal-robotics/talos_robot talos_description/urdf/leg/leg.transmission.xacro at 79709aa4f4f453ec18a5e467e65f84ff58ea24d0: ValueError: Macro talos_leg_simple_transmission requires unsupported explicit arguments: ['side', 'number', 'reduction']

- https://github.com/pal-robotics/talos_robot talos_description/robots/talos_arm_right.urdf.xacro at 79709aa4f4f453ec18a5e467e65f84ff58ea24d0: XacroException: No such file or directory: .cache/pal-robotics__talos_robot/.drift_xacro/tmpvd7_51z_/.unresolved_package/pal_urdf_utils/urdf/deg_to_rad.urdf.xacro [Errno 2] No such file or directory: '.cache/pal-robotics__talos_robot/.drift_xacro/tmpvd7_51z_/.unresolved_package/pal_urdf_utils/urdf/deg_to_rad.urdf.xacro'

- https://github.com/pal-robotics/talos_robot talos_description/urdf/arm/wrist.ros2_control.xacro at 79709aa4f4f453ec18a5e467e65f84ff58ea24d0: ValueError: Macro ros2_control_wrist requires unsupported explicit arguments: ['side', 'joint_5_offset', 'joint_6_offset', 'joint_7_offset']

- https://github.com/pal-robotics/talos_robot talos_description/urdf/arm/wrist.transmission.xacro at 79709aa4f4f453ec18a5e467e65f84ff58ea24d0: ValueError: Macro-only input has no uniquely identified robot macro

- https://github.com/pal-robotics/talos_robot talos_description/urdf/head/head.ros2_control.xacro at 79709aa4f4f453ec18a5e467e65f84ff58ea24d0: ValueError: Macro ros2_control_head requires unsupported explicit arguments: ['number_1', 'number_2', 'offset_value_1', 'offset_value_2']

- https://github.com/pal-robotics/talos_robot talos_description/urdf/head/head.transmission.xacro at 79709aa4f4f453ec18a5e467e65f84ff58ea24d0: ValueError: Macro talos_head_differential_transmission requires unsupported explicit arguments: ['number1', 'number2', 'act_reduction1', 'act_reduction2', 'jnt_reduction1', 'jnt_reduction2', 'offset_value_1', 'offset_value_2']

- https://github.com/pal-robotics/talos_robot talos_description/urdf/talos_full_common.urdf.xacro at 79709aa4f4f453ec18a5e467e65f84ff58ea24d0: XacroException: No such file or directory: .cache/pal-robotics__talos_robot/.drift_xacro/tmprprhl1__/.unresolved_package/pal_urdf_utils/urdf/deg_to_rad.urdf.xacro [Errno 2] No such file or directory: '.cache/pal-robotics__talos_robot/.drift_xacro/tmprprhl1__/.unresolved_package/pal_urdf_utils/urdf/deg_to_rad.urdf.xacro'

- https://github.com/pal-robotics/talos_robot talos_description/robots/talos_lower_body.urdf.xacro at 79709aa4f4f453ec18a5e467e65f84ff58ea24d0: XacroException: No such file or directory: .cache/pal-robotics__talos_robot/.drift_xacro/tmpfjpx2b1l/.unresolved_package/pal_urdf_utils/urdf/ft_sensors/ati_talos.urdf.xacro [Errno 2] No such file or directory: '.cache/pal-robotics__talos_robot/.drift_xacro/tmpfjpx2b1l/.unresolved_package/pal_urdf_utils/urdf/ft_sensors/ati_talos.urdf.xacro'

- https://github.com/pal-robotics/talos_robot talos_description/urdf/torso/torso.ros2_control.xacro at 79709aa4f4f453ec18a5e467e65f84ff58ea24d0: ValueError: XML Error: missing element: 'parent'
Element 'joint', line 1


- https://github.com/pal-robotics/talos_robot talos_description/urdf/torso/torso.transmission.xacro at 79709aa4f4f453ec18a5e467e65f84ff58ea24d0: ValueError: Macro talos_torso_differential_transmission requires unsupported explicit arguments: ['number1', 'number2', 'act_reduction1', 'act_reduction2', 'jnt_reduction1', 'jnt_reduction2']

- https://github.com/pal-robotics/talos_robot talos_description/ros2_control/ros2_control.urdf.xacro at 79709aa4f4f453ec18a5e467e65f84ff58ea24d0: XacroException: No such file or directory: .cache/pal-robotics__talos_robot/.drift_xacro/tmp683hdbw8/.unresolved_package/pal_urdf_utils/urdf/interaction_sensors/imu_sensors.ros2_control.xacro [Errno 2] No such file or directory: '.cache/pal-robotics__talos_robot/.drift_xacro/tmp683hdbw8/.unresolved_package/pal_urdf_utils/urdf/interaction_sensors/imu_sensors.ros2_control.xacro'

- https://github.com/pal-robotics/talos_robot talos_description/urdf/arm/arm_specifics_v1.urdf.xacro at 79709aa4f4f453ec18a5e467e65f84ff58ea24d0: ValueError: Macro arm_1_joint_limits requires unsupported explicit arguments: ['reflect']

- https://github.com/pal-robotics/talos_robot talos_description/urdf/arm/arm_specifics_v2.urdf.xacro at 79709aa4f4f453ec18a5e467e65f84ff58ea24d0: ValueError: Macro arm_1_joint_limits requires unsupported explicit arguments: ['reflect']

- https://github.com/pal-robotics/talos_robot talos_description/urdf/gripper/gripper.ros2_control.xacro at 79709aa4f4f453ec18a5e467e65f84ff58ea24d0: ValueError: XML Error: missing element: 'parent'
Element 'joint', line 1


- https://github.com/pal-robotics/talos_robot talos_description/urdf/gripper/gripper.transmission.xacro at 79709aa4f4f453ec18a5e467e65f84ff58ea24d0: ValueError: Macro gripper_transmission requires unsupported explicit arguments: ['reduction']

- https://github.com/pal-robotics/talos_robot talos_description/robots/talos_full_no_grippers.urdf.xacro at 79709aa4f4f453ec18a5e467e65f84ff58ea24d0: XacroException: Undefined substitution argument enable_crane

- https://github.com/pal-robotics/talos_robot talos_description/robots/talos_full_fake_grippers.urdf.xacro at 79709aa4f4f453ec18a5e467e65f84ff58ea24d0: XacroException: Undefined substitution argument enable_crane

- https://github.com/pal-robotics/talos_robot talos_description/urdf/leg/foot_collision_default.urdf.xacro at 79709aa4f4f453ec18a5e467e65f84ff58ea24d0: XacroException: name 'reflect' is not defined
when evaluating expression 'reflect*1.05'

- https://github.com/pal-robotics/talos_robot talos_description/robots/talos_lower_body_torso_head.urdf.xacro at 79709aa4f4f453ec18a5e467e65f84ff58ea24d0: XacroException: Undefined substitution argument enable_crane

- Historical Menagerie compile failed umi_gripper d6bab9ddb7f3028aaf4714c804183b09239998c1: Resource missing at d6bab9ddb7f3028aaf4714c804183b09239998c1: umi_gripper/assets/base_link.stl

- Offline Git read failed (exit 128): `('ls-tree', '-r', '--name-only', 'f29a87905bdcfc32fdac9c5342644630fd27156a')` in `FFTAI__Wiki-GRx-Models`. fatal: not a tree object

- Source discovery https://github.com/FFTAI/Wiki-GRx-Models: CalledProcessError: Command '['git', '-C', '.cache/FFTAI__Wiki-GRx-Models', 'ls-tree', '-r', '--name-only', 'f29a87905bdcfc32fdac9c5342644630fd27156a']' returned non-zero exit status 128.

- Offline Git read failed (exit 128): `('show', 'a758567c3978dfeefe282ede0500085a48fe8f78:URDF/SO_5DOF_ARM100_8j_URDF.SLDASM/urdf/SO_5DOF_ARM100_8j_URDF.SLDASM.urdf')` in `TheRobotStudio__SO-ARM100`. fatal: path 'URDF/SO_5DOF_ARM100_8j_URDF.SLDASM/urdf/SO_5DOF_ARM100_8j_URDF.SLDASM.urdf' does not exist in 'a758567c3978dfeefe282ede0500085a48fe8f78'

- https://github.com/TheRobotStudio/SO-ARM100 URDF/SO_5DOF_ARM100_8j_URDF.SLDASM/urdf/SO_5DOF_ARM100_8j_URDF.SLDASM.urdf at a758567c3978dfeefe282ede0500085a48fe8f78: CalledProcessError: Command '['git', '-C', '.cache/TheRobotStudio__SO-ARM100', 'show', 'a758567c3978dfeefe282ede0500085a48fe8f78:URDF/SO_5DOF_ARM100_8j_URDF.SLDASM/urdf/SO_5DOF_ARM100_8j_URDF.SLDASM.urdf']' returned non-zero exit status 128.

- Offline Git read failed (exit 128): `('show', '4e9c5588d8a8415b6a6c2142a0ce8c32207cf3e9:Simulation/SO100/so100.urdf')` in `TheRobotStudio__SO-ARM100`. fatal: path 'Simulation/SO100/so100.urdf' does not exist in '4e9c5588d8a8415b6a6c2142a0ce8c32207cf3e9'

- Offline Git read failed (exit 128): `('rev-parse', '4e9c5588d8a8415b6a6c2142a0ce8c32207cf3e9:Simulation/SO100/so100.urdf')` in `TheRobotStudio__SO-ARM100`. fatal: path 'Simulation/SO100/so100.urdf' does not exist in '4e9c5588d8a8415b6a6c2142a0ce8c32207cf3e9'

- Targeted fetch failed for https://github.com/TheRobotStudio/SO-ARM100 4e9c5588d8a8415b6a6c2142a0ce8c32207cf3e9:Simulation/SO100/so100.urdf: Command '['git', '-C', '.cache/TheRobotStudio__SO-ARM100', 'rev-parse', '4e9c5588d8a8415b6a6c2142a0ce8c32207cf3e9:Simulation/SO100/so100.urdf']' returned non-zero exit status 128.

- Pinned source compilation failed trs_so_arm100: Command '['git', '-C', '.cache/TheRobotStudio__SO-ARM100', 'show', '4e9c5588d8a8415b6a6c2142a0ce8c32207cf3e9:Simulation/SO100/so100.urdf']' returned non-zero exit status 128.

- Offline Git read failed (exit 128): `('log', '--all', '--follow', '--find-renames=100%', '--format=@@@%H|%ct|%cI|%s', '--name-status', '--', 'urdf/00-arm-rs_asm-v3/urdf/00-arm-rs_asm-v3.urdf')` in `Seeed-Projects__reBot-Isaacsim`. warning: lazy fetching disabled; some objects may not be available
fatal: could not fetch d91aac9cb500116a7b06841effb7d93156a7ac1e from promisor remote

- Repair check failed seeed_rebot_devarm: CalledProcessError: Command '['git', '-C', '.cache/Seeed-Projects__reBot-Isaacsim', 'log', '--all', '--follow', '--find-renames=100%', '--format=@@@%H|%ct|%cI|%s', '--name-status', '--', 'urdf/00-arm-rs_asm-v3/urdf/00-arm-rs_asm-v3.urdf']' returned non-zero exit status 128.

- Rejected unrelated historical README template for agilex_piper: 0bee963312f0f4a25b53cdf9afe744ca73f2d68a heading '## UMI-Gripper Description (MJCF)'

- Offline Git read failed (exit 128): `('show', '400b5f5b9fec382583f69b53b094a154d9dc7635:agilex_piper/CHANGELOG.md')` in `menagerie`. fatal: path 'agilex_piper/CHANGELOG.md' does not exist in '400b5f5b9fec382583f69b53b094a154d9dc7635'

- Rejected conflicting robot-variant link for anybotics_anymal_c: https://github.com/ANYbotics/anymal_b_simple_description/blob/master/urdf/anymal.urdf (repository variant b, model variant c)

- Offline Git read failed (exit 128): `('show', 'd9415a3076f921fdb9735d45d609a596df722468:apptronik_apollo/CHANGELOG.md')` in `menagerie`. fatal: bad object d9415a3076f921fdb9735d45d609a596df722468:apptronik_apollo/CHANGELOG.md

- Offline Git read failed (exit 128): `('show', '400b5f5b9fec382583f69b53b094a154d9dc7635:arx_l5/CHANGELOG.md')` in `menagerie`. fatal: path 'arx_l5/CHANGELOG.md' does not exist in '400b5f5b9fec382583f69b53b094a154d9dc7635'

- Offline Git read failed (exit 128): `('show', 'd9415a3076f921fdb9735d45d609a596df722468:berkeley_humanoid/CHANGELOG.md')` in `menagerie`. fatal: bad object d9415a3076f921fdb9735d45d609a596df722468:berkeley_humanoid/CHANGELOG.md

- Rejected conflicting robot-variant link for bitcraze_crazyflie_2: https://github.com/whoenig/crazyflie_ros (repository variant ros, model variant 2)

- Offline Git read failed (exit 128): `('show', 'd9415a3076f921fdb9735d45d609a596df722468:booster_t1/CHANGELOG.md')` in `menagerie`. fatal: bad object d9415a3076f921fdb9735d45d609a596df722468:booster_t1/CHANGELOG.md

- Offline Git read failed (exit 128): `('show', 'd9415a3076f921fdb9735d45d609a596df722468:fourier_n1/CHANGELOG.md')` in `menagerie`. fatal: bad object d9415a3076f921fdb9735d45d609a596df722468:fourier_n1/CHANGELOG.md

- Offline Git read failed (exit 128): `('show', '400b5f5b9fec382583f69b53b094a154d9dc7635:fourier_n1/CHANGELOG.md')` in `menagerie`. fatal: path 'fourier_n1/CHANGELOG.md' does not exist in '400b5f5b9fec382583f69b53b094a154d9dc7635'

- Offline Git read failed (exit 128): `('show', 'db140ade7ee4cb59629f9687aafc65af663d5bbe:franka_fr3_v2/README.md')` in `menagerie`. fatal: path 'franka_fr3_v2/README.md' does not exist in 'db140ade7ee4cb59629f9687aafc65af663d5bbe'

- Offline Git read failed (exit 128): `('show', 'cd7fc51b704c3cba05748bd5537cb17990b341eb:franka_fr3_v2/README.md')` in `menagerie`. fatal: path 'franka_fr3_v2/README.md' does not exist in 'cd7fc51b704c3cba05748bd5537cb17990b341eb'

- Offline Git read failed (exit 128): `('show', '400b5f5b9fec382583f69b53b094a154d9dc7635:franka_fr3_v2/README.md')` in `menagerie`. fatal: path 'franka_fr3_v2/README.md' does not exist in '400b5f5b9fec382583f69b53b094a154d9dc7635'

- Offline Git read failed (exit 128): `('show', 'acbbf1636fcfef9b437a6eb8c6f84380fb4aa998:franka_fr3_v2/README.md')` in `menagerie`. fatal: path 'franka_fr3_v2/README.md' does not exist in 'acbbf1636fcfef9b437a6eb8c6f84380fb4aa998'

- Offline Git read failed (exit 128): `('show', '7876dcdef0d912387441616526ed236142f047d3:franka_fr3_v2/README.md')` in `menagerie`. fatal: path 'franka_fr3_v2/README.md' does not exist in '7876dcdef0d912387441616526ed236142f047d3'

- Offline Git read failed (exit 128): `('show', 'b5ebfe0cf079d2b96acf0a5c0e29ee0c95ba32f4:google_robot/README.md')` in `menagerie`. fatal: path 'google_robot/README.md' does not exist in 'b5ebfe0cf079d2b96acf0a5c0e29ee0c95ba32f4'

- Offline Git read failed (exit 128): `('show', '5ce04bea98bbfca277a8d50b55ba3c7c4a62bdec:i2rt_yam/CHANGELOG.md')` in `menagerie`. fatal: path 'i2rt_yam/CHANGELOG.md' does not exist in '5ce04bea98bbfca277a8d50b55ba3c7c4a62bdec'

- Offline Git read failed (exit 128): `('show', 'a88bc450470d97ebc1f282e5969675fb4d1f0ed7:low_cost_robot_arm/README.md')` in `menagerie`. fatal: path 'low_cost_robot_arm/README.md' does not exist in 'a88bc450470d97ebc1f282e5969675fb4d1f0ed7'

- Offline Git read failed (exit 128): `('show', 'd74280a600a9afdfcb98d8917d0c79c86539aa61:low_cost_robot_arm/README.md')` in `menagerie`. fatal: path 'low_cost_robot_arm/README.md' does not exist in 'd74280a600a9afdfcb98d8917d0c79c86539aa61'

- Offline Git read failed (exit 128): `('show', '13d6c48b8f59d2c4badee7756b4ea3532613cddf:low_cost_robot_arm/README.md')` in `menagerie`. fatal: path 'low_cost_robot_arm/README.md' does not exist in '13d6c48b8f59d2c4badee7756b4ea3532613cddf'

- Offline Git read failed (exit 128): `('show', 'fae9ee82330444eec4e87568c838b99a09a39467:rainbow_robotics_rby1/README.md')` in `menagerie`. fatal: path 'rainbow_robotics_rby1/README.md' does not exist in 'fae9ee82330444eec4e87568c838b99a09a39467'

- Offline Git read failed (exit 128): `('show', '04674c8d0a4e12e33980a9e47fb604adc281fcc8:robotstudio_so101/CHANGELOG.md')` in `menagerie`. fatal: path 'robotstudio_so101/CHANGELOG.md' does not exist in '04674c8d0a4e12e33980a9e47fb604adc281fcc8'

- Offline Git read failed (exit 128): `('show', '5ce04bea98bbfca277a8d50b55ba3c7c4a62bdec:robotstudio_so101/CHANGELOG.md')` in `menagerie`. fatal: path 'robotstudio_so101/CHANGELOG.md' does not exist in '5ce04bea98bbfca277a8d50b55ba3c7c4a62bdec'

- Offline Git read failed (exit 128): `('show', '4a7015530bd7a4161103ae8f0905a96481e4cc1a:robotstudio_so101/CHANGELOG.md')` in `menagerie`. fatal: path 'robotstudio_so101/CHANGELOG.md' does not exist in '4a7015530bd7a4161103ae8f0905a96481e4cc1a'

- Offline Git read failed (exit 128): `('show', 'bf110a75a56e5bd146c7ed76965737c71d48425d:shadow_dexee/README.md')` in `menagerie`. fatal: path 'shadow_dexee/README.md' does not exist in 'bf110a75a56e5bd146c7ed76965737c71d48425d'

- Offline Git read failed (exit 128): `('show', '04674c8d0a4e12e33980a9e47fb604adc281fcc8:tetheria_aero_hand_open/CHANGELOG.md')` in `menagerie`. fatal: path 'tetheria_aero_hand_open/CHANGELOG.md' does not exist in '04674c8d0a4e12e33980a9e47fb604adc281fcc8'

- Offline Git read failed (exit 128): `('show', '400b5f5b9fec382583f69b53b094a154d9dc7635:tetheria_aero_hand_open/CHANGELOG.md')` in `menagerie`. fatal: path 'tetheria_aero_hand_open/CHANGELOG.md' does not exist in '400b5f5b9fec382583f69b53b094a154d9dc7635'

- Offline Git read failed (exit 128): `('show', '04674c8d0a4e12e33980a9e47fb604adc281fcc8:toddlerbot_2xc/CHANGELOG.md')` in `menagerie`. fatal: path 'toddlerbot_2xc/CHANGELOG.md' does not exist in '04674c8d0a4e12e33980a9e47fb604adc281fcc8'

- Offline Git read failed (exit 128): `('show', '9e7f8d4dda07f5c281b6c0c6f0d07b9dd267b762:toddlerbot_2xc/CHANGELOG.md')` in `menagerie`. fatal: path 'toddlerbot_2xc/CHANGELOG.md' does not exist in '9e7f8d4dda07f5c281b6c0c6f0d07b9dd267b762'

- Offline Git read failed (exit 128): `('show', '400b5f5b9fec382583f69b53b094a154d9dc7635:toddlerbot_2xc/CHANGELOG.md')` in `menagerie`. fatal: path 'toddlerbot_2xc/CHANGELOG.md' does not exist in '400b5f5b9fec382583f69b53b094a154d9dc7635'

- Offline Git read failed (exit 128): `('show', '04674c8d0a4e12e33980a9e47fb604adc281fcc8:toddlerbot_2xm/CHANGELOG.md')` in `menagerie`. fatal: path 'toddlerbot_2xm/CHANGELOG.md' does not exist in '04674c8d0a4e12e33980a9e47fb604adc281fcc8'

- Offline Git read failed (exit 128): `('show', '9e7f8d4dda07f5c281b6c0c6f0d07b9dd267b762:toddlerbot_2xm/CHANGELOG.md')` in `menagerie`. fatal: path 'toddlerbot_2xm/CHANGELOG.md' does not exist in '9e7f8d4dda07f5c281b6c0c6f0d07b9dd267b762'

- Offline Git read failed (exit 128): `('show', '400b5f5b9fec382583f69b53b094a154d9dc7635:toddlerbot_2xm/CHANGELOG.md')` in `menagerie`. fatal: path 'toddlerbot_2xm/CHANGELOG.md' does not exist in '400b5f5b9fec382583f69b53b094a154d9dc7635'

- Offline Git read failed (exit 128): `('show', '400b5f5b9fec382583f69b53b094a154d9dc7635:trossen_wxai/README.md')` in `menagerie`. fatal: path 'trossen_wxai/README.md' does not exist in '400b5f5b9fec382583f69b53b094a154d9dc7635'

- Offline Git read failed (exit 128): `('show', '477ec56566682d663b996d86a188c75499e74b98:trossen_wxai/README.md')` in `menagerie`. fatal: path 'trossen_wxai/README.md' does not exist in '477ec56566682d663b996d86a188c75499e74b98'

- Offline Git read failed (exit 128): `('show', 'd9415a3076f921fdb9735d45d609a596df722468:unitree_g1/CHANGELOG.md')` in `menagerie`. fatal: bad object d9415a3076f921fdb9735d45d609a596df722468:unitree_g1/CHANGELOG.md

- Offline Git read failed (exit 128): `('show', '2d686957aefd5739cf4d2859a6acfd94c8f84400:Geometry/Rib1L.obj')` in `LNSGroup__MS-Human-700`. fatal: bad object 2d686957aefd5739cf4d2859a6acfd94c8f84400:Geometry/Rib1L.obj

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/LNSGroup__MS-Human-700 -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `046f8f36dabe0e5db2b2c2e668b53b241154330f`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '2d686957aefd5739cf4d2859a6acfd94c8f84400:Geometry/lunate_mirror.obj')` in `LNSGroup__MS-Human-700`. fatal: bad object 2d686957aefd5739cf4d2859a6acfd94c8f84400:Geometry/lunate_mirror.obj

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/LNSGroup__MS-Human-700 -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `50f0fffab7a415b6a6fbe2b36df66a6dfa0dfd1d`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '2d686957aefd5739cf4d2859a6acfd94c8f84400:Geometry/scaphoid_mirror.obj')` in `LNSGroup__MS-Human-700`. fatal: bad object 2d686957aefd5739cf4d2859a6acfd94c8f84400:Geometry/scaphoid_mirror.obj

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/LNSGroup__MS-Human-700 -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `3497f8a3e97741e3da2934b3e213eeb8bd8b9e85`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '2d686957aefd5739cf4d2859a6acfd94c8f84400:Geometry/pisiform_mirror.obj')` in `LNSGroup__MS-Human-700`. fatal: bad object 2d686957aefd5739cf4d2859a6acfd94c8f84400:Geometry/pisiform_mirror.obj

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/LNSGroup__MS-Human-700 -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `43471b636b156d61677c4f0279065b82a720c4b6`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '2d686957aefd5739cf4d2859a6acfd94c8f84400:Geometry/triquetral_mirror.obj')` in `LNSGroup__MS-Human-700`. fatal: bad object 2d686957aefd5739cf4d2859a6acfd94c8f84400:Geometry/triquetral_mirror.obj

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/LNSGroup__MS-Human-700 -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `1176431c2bb8737cdd0d1c687c83855c4ecc73d2`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '2d686957aefd5739cf4d2859a6acfd94c8f84400:Geometry/capitate_mirror.obj')` in `LNSGroup__MS-Human-700`. fatal: bad object 2d686957aefd5739cf4d2859a6acfd94c8f84400:Geometry/capitate_mirror.obj

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/LNSGroup__MS-Human-700 -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `56add29d1d033f23b292c0245e808370cfd97efc`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '2d686957aefd5739cf4d2859a6acfd94c8f84400:Geometry/trapezium_mirror.obj')` in `LNSGroup__MS-Human-700`. fatal: bad object 2d686957aefd5739cf4d2859a6acfd94c8f84400:Geometry/trapezium_mirror.obj

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/LNSGroup__MS-Human-700 -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `f69ad48862ee5c0f4bcb4d9d4c209b5ca81c845a`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '2d686957aefd5739cf4d2859a6acfd94c8f84400:Geometry/1mc_mirror.obj')` in `LNSGroup__MS-Human-700`. fatal: bad object 2d686957aefd5739cf4d2859a6acfd94c8f84400:Geometry/1mc_mirror.obj

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/LNSGroup__MS-Human-700 -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `f21126c696ece42ea7f03db17308eef63a989767`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '2d686957aefd5739cf4d2859a6acfd94c8f84400:Geometry/thumbprox_mirror.obj')` in `LNSGroup__MS-Human-700`. fatal: bad object 2d686957aefd5739cf4d2859a6acfd94c8f84400:Geometry/thumbprox_mirror.obj

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/LNSGroup__MS-Human-700 -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `a0a08107ce16e136a1e032ed768e7540e3d85a09`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '2d686957aefd5739cf4d2859a6acfd94c8f84400:Geometry/thumbdist_mirror.obj')` in `LNSGroup__MS-Human-700`. fatal: bad object 2d686957aefd5739cf4d2859a6acfd94c8f84400:Geometry/thumbdist_mirror.obj

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/LNSGroup__MS-Human-700 -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `cfc109622b4504a93437fa1ec7a357ceecb942bf`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '2d686957aefd5739cf4d2859a6acfd94c8f84400:Geometry/trapezoid_mirror.obj')` in `LNSGroup__MS-Human-700`. fatal: bad object 2d686957aefd5739cf4d2859a6acfd94c8f84400:Geometry/trapezoid_mirror.obj

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/LNSGroup__MS-Human-700 -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `e750f2d292f488c525a19fbe4c546801ed4eda21`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '2d686957aefd5739cf4d2859a6acfd94c8f84400:Geometry/hamate_mirror.obj')` in `LNSGroup__MS-Human-700`. fatal: bad object 2d686957aefd5739cf4d2859a6acfd94c8f84400:Geometry/hamate_mirror.obj

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/LNSGroup__MS-Human-700 -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `3685429baa1a3efaf7a0687cfde7e5390f546c5c`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '2d686957aefd5739cf4d2859a6acfd94c8f84400:Geometry/2mc_mirror.obj')` in `LNSGroup__MS-Human-700`. fatal: bad object 2d686957aefd5739cf4d2859a6acfd94c8f84400:Geometry/2mc_mirror.obj

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/LNSGroup__MS-Human-700 -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `01f144e0e69d25c1f59d17507c2c63bf07268495`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '2d686957aefd5739cf4d2859a6acfd94c8f84400:Geometry/2proxph_mirror.obj')` in `LNSGroup__MS-Human-700`. fatal: bad object 2d686957aefd5739cf4d2859a6acfd94c8f84400:Geometry/2proxph_mirror.obj

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/LNSGroup__MS-Human-700 -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `3fe618dac04cd72981b30623e5ba57be03f24992`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '2d686957aefd5739cf4d2859a6acfd94c8f84400:Geometry/2distph_mirror.obj')` in `LNSGroup__MS-Human-700`. fatal: bad object 2d686957aefd5739cf4d2859a6acfd94c8f84400:Geometry/2distph_mirror.obj

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/LNSGroup__MS-Human-700 -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `d01e82327f011a1638f7f248dd492b6ba2888d72`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '2d686957aefd5739cf4d2859a6acfd94c8f84400:Geometry/3mc_mirror.obj')` in `LNSGroup__MS-Human-700`. fatal: bad object 2d686957aefd5739cf4d2859a6acfd94c8f84400:Geometry/3mc_mirror.obj

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/LNSGroup__MS-Human-700 -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `5f0249ac6d2518f584131ad50fa82ed1e0998e0c`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '2d686957aefd5739cf4d2859a6acfd94c8f84400:Geometry/3proxph_mirror.obj')` in `LNSGroup__MS-Human-700`. fatal: bad object 2d686957aefd5739cf4d2859a6acfd94c8f84400:Geometry/3proxph_mirror.obj

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/LNSGroup__MS-Human-700 -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `75a2dbbf9a984e3f39cf9e1ca0ddfe908ab80876`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '2d686957aefd5739cf4d2859a6acfd94c8f84400:Geometry/3midph_mirror.obj')` in `LNSGroup__MS-Human-700`. fatal: bad object 2d686957aefd5739cf4d2859a6acfd94c8f84400:Geometry/3midph_mirror.obj

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/LNSGroup__MS-Human-700 -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `76be10f6ff6ebf77da2c8920dac1bcc34efa23aa`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '2d686957aefd5739cf4d2859a6acfd94c8f84400:Geometry/3distph_mirror.obj')` in `LNSGroup__MS-Human-700`. fatal: bad object 2d686957aefd5739cf4d2859a6acfd94c8f84400:Geometry/3distph_mirror.obj

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/LNSGroup__MS-Human-700 -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `7e1982282218a3b6691142238462be5225168ddc`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '2d686957aefd5739cf4d2859a6acfd94c8f84400:Geometry/4mc_new_mirror.obj')` in `LNSGroup__MS-Human-700`. fatal: bad object 2d686957aefd5739cf4d2859a6acfd94c8f84400:Geometry/4mc_new_mirror.obj

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/LNSGroup__MS-Human-700 -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `d2a315821a04150fbfa1a06b7bd50dde7b661bec`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '2d686957aefd5739cf4d2859a6acfd94c8f84400:Geometry/4proxph_new_mirror.obj')` in `LNSGroup__MS-Human-700`. fatal: bad object 2d686957aefd5739cf4d2859a6acfd94c8f84400:Geometry/4proxph_new_mirror.obj

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/LNSGroup__MS-Human-700 -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `c12c83ef6a70008c3383f6a80f15602ac5f60269`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '2d686957aefd5739cf4d2859a6acfd94c8f84400:Geometry/4midph_new_mirror.obj')` in `LNSGroup__MS-Human-700`. fatal: bad object 2d686957aefd5739cf4d2859a6acfd94c8f84400:Geometry/4midph_new_mirror.obj

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/LNSGroup__MS-Human-700 -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `ccbd45765a460f4445e7ee8cbdca1a894786c654`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '2d686957aefd5739cf4d2859a6acfd94c8f84400:Geometry/4distph_new_mirror.obj')` in `LNSGroup__MS-Human-700`. fatal: bad object 2d686957aefd5739cf4d2859a6acfd94c8f84400:Geometry/4distph_new_mirror.obj

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/LNSGroup__MS-Human-700 -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `048845ff7e3d253a8ee4b4adbaf4fac81e1e5a90`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '2d686957aefd5739cf4d2859a6acfd94c8f84400:Geometry/5mc_new_mirror.obj')` in `LNSGroup__MS-Human-700`. fatal: bad object 2d686957aefd5739cf4d2859a6acfd94c8f84400:Geometry/5mc_new_mirror.obj

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/LNSGroup__MS-Human-700 -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `8c325efd52104fe044f9e8d9ea4408bf89bf6f8d`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '2d686957aefd5739cf4d2859a6acfd94c8f84400:Geometry/5proxph_new_mirror.obj')` in `LNSGroup__MS-Human-700`. fatal: bad object 2d686957aefd5739cf4d2859a6acfd94c8f84400:Geometry/5proxph_new_mirror.obj

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/LNSGroup__MS-Human-700 -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `9cacbb35a7c6edac37a92ff2f7ea4c424f9101fc`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '2d686957aefd5739cf4d2859a6acfd94c8f84400:Geometry/5distph_new_mirror.obj')` in `LNSGroup__MS-Human-700`. fatal: bad object 2d686957aefd5739cf4d2859a6acfd94c8f84400:Geometry/5distph_new_mirror.obj

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/LNSGroup__MS-Human-700 -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `84881e514a6af6fdc348779118c1479149d6e0f9`

- Network outcome: exit 0.

- https://github.com/ANYbotics/anymal_c_simple_description urdf/anymal.urdf at 87b68511622f0f17e78d9ddca7d862f150a93fb4: ValueError: Error: inertia must satisfy A + B >= C; use 'balanceinertia' to fix
Element name 'depth_camera_front_camera', id 8

- Offline Git read failed (exit 128): `('log', '--all', '--follow', '--find-renames=100%', '--format=@@@%H|%ct|%cI|%s', '--name-status', '--', 'realsense2_description/urdf/_d435i.urdf.xacro')` in `IntelRealSense__realsense-ros`. warning: lazy fetching disabled; some objects may not be available
fatal: could not fetch 6c6c82b0585c375526839fb94d52f173291457ed from promisor remote

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/IntelRealSense__realsense-ros -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `6c6c82b0585c375526839fb94d52f173291457ed`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('log', '--all', '--follow', '--find-renames=100%', '--format=@@@%H|%ct|%cI|%s', '--name-status', '--', 'realsense2_description/urdf/_d435i.urdf.xacro')` in `IntelRealSense__realsense-ros`. warning: lazy fetching disabled; some objects may not be available
fatal: could not fetch 682bce043b3616214e669f80f385b0d610c2f11b from promisor remote

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/IntelRealSense__realsense-ros -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `682bce043b3616214e669f80f385b0d610c2f11b`

- Network outcome: exit 0.

- Historical source compile failed realsense_d435i d9e15bb2fbb8642acecf19596a2349c7593c7bb6 realsense2_description/urdf/_d435i.urdf.xacro: Resource missing at d9e15bb2fbb8642acecf19596a2349c7593c7bb6: realsense2_description/urdf/file:/realsense2_description/meshes/d435.dae

- Historical source compile failed realsense_d435i afef66f988c45cca14b4d8fd654c9c017c1b0ac1 realsense2_description/urdf/_d435i.urdf.xacro: XML has no robot bodies; it is an include/extension fragment, not a standalone source

- Historical source compile failed realsense_d435i c8a8afd14240f8adee1548771d9bca2e16bcb12b realsense2_description/urdf/_d435i.urdf.xacro: XML or text declaration not at start of entity: line 10, column 0

- Historical source compile failed realsense_d435i c81130c7d9b2141b4130f9ebebf4f02a1a184f7c realsense2_description/urdf/_d435i.urdf.xacro: XML or text declaration not at start of entity: line 10, column 0

- https://github.com/xArm-Developer/xarm_ros2 xarm_description/urdf/lite6/lite6.urdf.xacro at ac736c92b02de7ca7e0be6f737d77d46707464d8: XacroException: name 'use_xacro_load_yaml' is not defined
when evaluating expression 'use_xacro_load_yaml'

- https://github.com/xArm-Developer/xarm_ros2 xarm_description/urdf/lite6/lite6.gazebo.xacro at ac736c92b02de7ca7e0be6f737d77d46707464d8: ValueError: XML has no robot bodies; it is an include/extension fragment, not a standalone source

- https://github.com/xArm-Developer/xarm_ros2 xarm_description/urdf/lite6/lite6.ros2_control.xacro at ac736c92b02de7ca7e0be6f737d77d46707464d8: ValueError: XML has no robot bodies; it is an include/extension fragment, not a standalone source

- https://github.com/xArm-Developer/xarm_ros2 xarm_description/urdf/lite6/lite6.transmission.xacro at ac736c92b02de7ca7e0be6f737d77d46707464d8: ValueError: XML has no robot bodies; it is an include/extension fragment, not a standalone source

- https://github.com/xArm-Developer/xarm_ros2 xarm_description/urdf/lite6/lite6_robot_macro.xacro at ac736c92b02de7ca7e0be6f737d77d46707464d8: XacroException: name 'is_ros2' is not defined
when evaluating expression 'is_ros2'

- https://github.com/xArm-Developer/xarm_ros xarm_description/urdf/xarm7/xarm7.urdf.xacro at cf51617d98bc55a88d9aa735acfa43a0bbb8e425: XacroException: name 'mesh_suffix' is not defined
when evaluating expression 'mesh_suffix == 'dae' or (model_num >= 1305 and model_num != 1380)'

- https://github.com/xArm-Developer/xarm_ros xarm_description/urdf/xarm7/xarm7.gazebo.xacro at cf51617d98bc55a88d9aa735acfa43a0bbb8e425: ValueError: XML has no robot bodies; it is an include/extension fragment, not a standalone source

- https://github.com/xArm-Developer/xarm_ros xarm_description/urdf/xarm7/xarm7.ros2_control.xacro at cf51617d98bc55a88d9aa735acfa43a0bbb8e425: ValueError: XML has no robot bodies; it is an include/extension fragment, not a standalone source

- https://github.com/xArm-Developer/xarm_ros xarm_description/urdf/xarm7/xarm7.transmission.xacro at cf51617d98bc55a88d9aa735acfa43a0bbb8e425: ValueError: XML has no robot bodies; it is an include/extension fragment, not a standalone source

- https://github.com/xArm-Developer/xarm_ros xarm_description/urdf/xarm7/xarm7_robot_macro.xacro at cf51617d98bc55a88d9aa735acfa43a0bbb8e425: XacroException: name 'is_ros2' is not defined
when evaluating expression 'is_ros2'

- https://github.com/pal-robotics/talos_robot talos_description/urdf/arm/arm.urdf.xacro at 79709aa4f4f453ec18a5e467e65f84ff58ea24d0: ValueError: Macro talos_arm requires unsupported explicit arguments: ['side', 'reflect']

- https://github.com/pal-robotics/talos_robot talos_description/urdf/leg/leg.urdf.xacro at 79709aa4f4f453ec18a5e467e65f84ff58ea24d0: ValueError: Macro talos_leg requires unsupported explicit arguments: ['reflect']

- https://github.com/pal-robotics/talos_robot talos_description/gazebo/gazebo.urdf.xacro at 79709aa4f4f453ec18a5e467e65f84ff58ea24d0: XacroException: No such file or directory: .cache/pal-robotics__talos_robot/.drift_xacro/tmpu2_u_n8v/.unresolved_package/pal_urdf_utils/urdf/interaction_sensors/imu_talos.gazebo.xacro [Errno 2] No such file or directory: '.cache/pal-robotics__talos_robot/.drift_xacro/tmpu2_u_n8v/.unresolved_package/pal_urdf_utils/urdf/interaction_sensors/imu_talos.gazebo.xacro'

- https://github.com/pal-robotics/talos_robot talos_description/urdf/arm/wrist.urdf.xacro at 79709aa4f4f453ec18a5e467e65f84ff58ea24d0: ValueError: Macro talos_wrist requires unsupported explicit arguments: ['side', 'reflect']

- https://github.com/pal-robotics/talos_robot talos_description/urdf/head/head.urdf.xacro at 79709aa4f4f453ec18a5e467e65f84ff58ea24d0: ValueError: Macro-only input has no uniquely identified robot macro

- https://github.com/pal-robotics/talos_robot talos_description/urdf/materials.urdf.xacro at 79709aa4f4f453ec18a5e467e65f84ff58ea24d0: ValueError: XML has no robot bodies; it is an include/extension fragment, not a standalone source

- https://github.com/pal-robotics/talos_robot talos_description/urdf/crane/crane.urdf.xacro at 79709aa4f4f453ec18a5e467e65f84ff58ea24d0: XacroException: No such file or directory: .cache/pal-robotics__talos_robot/.drift_xacro/tmplze3w9me/.unresolved_package/pal_urdf_utils/urdf/deg_to_rad.urdf.xacro [Errno 2] No such file or directory: '.cache/pal-robotics__talos_robot/.drift_xacro/tmplze3w9me/.unresolved_package/pal_urdf_utils/urdf/deg_to_rad.urdf.xacro'

- https://github.com/pal-robotics/talos_robot talos_description/urdf/torso/torso.urdf.xacro at 79709aa4f4f453ec18a5e467e65f84ff58ea24d0: XacroException: No such file or directory: .cache/pal-robotics__talos_robot/.drift_xacro/tmp5unkksnf/.unresolved_package/pal_urdf_utils/urdf/deg_to_rad.urdf.xacro [Errno 2] No such file or directory: '.cache/pal-robotics__talos_robot/.drift_xacro/tmp5unkksnf/.unresolved_package/pal_urdf_utils/urdf/deg_to_rad.urdf.xacro'

- https://github.com/pal-robotics/talos_robot talos_description/urdf/capsule_collision.xacro at 79709aa4f4f453ec18a5e467e65f84ff58ea24d0: ValueError: Macro capsule-collision requires unsupported explicit arguments: ['e1', 'e2', 'rad', 'clen', 'rpy', 'mid']

- https://github.com/pal-robotics/talos_robot talos_description/urdf/extras/addons.urdf.xacro at 79709aa4f4f453ec18a5e467e65f84ff58ea24d0: ValueError: XML has no robot bodies; it is an include/extension fragment, not a standalone source

- https://github.com/pal-robotics/talos_robot talos_description/robots/talos_full_v2.urdf.xacro at 79709aa4f4f453ec18a5e467e65f84ff58ea24d0: XacroException: No such file or directory: .cache/pal-robotics__talos_robot/.drift_xacro/tmp20lui0iy/.unresolved_package/pal_urdf_utils/urdf/deg_to_rad.urdf.xacro [Errno 2] No such file or directory: '.cache/pal-robotics__talos_robot/.drift_xacro/tmp20lui0iy/.unresolved_package/pal_urdf_utils/urdf/deg_to_rad.urdf.xacro'

- https://github.com/pal-robotics/talos_robot talos_description/urdf/arm/arm.ros2_control.xacro at 79709aa4f4f453ec18a5e467e65f84ff58ea24d0: ValueError: Macro ros2_control_arm requires unsupported explicit arguments: ['side', 'number', 'joint_offset']

- https://github.com/pal-robotics/talos_robot talos_description/urdf/arm/arm.transmission.xacro at 79709aa4f4f453ec18a5e467e65f84ff58ea24d0: ValueError: Macro talos_arm_simple_transmission requires unsupported explicit arguments: ['side', 'number', 'reduction', 'offset_value']

- https://github.com/pal-robotics/talos_robot talos_description/urdf/gripper/gripper.urdf.xacro at 79709aa4f4f453ec18a5e467e65f84ff58ea24d0: ValueError: Macro talos_gripper requires unsupported explicit arguments: ['reflect']

- https://github.com/pal-robotics/talos_robot talos_description/urdf/leg/foot_frames.urdf.xacro at 79709aa4f4f453ec18a5e467e65f84ff58ea24d0: ValueError: Macro talos_foot_frames requires unsupported explicit arguments: ['side']

- https://github.com/pal-robotics/talos_robot talos_description/urdf/leg/leg.ros2_control.xacro at 79709aa4f4f453ec18a5e467e65f84ff58ea24d0: ValueError: Macro ros2_control_leg requires unsupported explicit arguments: ['side', 'number']

- https://github.com/pal-robotics/talos_robot talos_description/urdf/leg/leg.transmission.xacro at 79709aa4f4f453ec18a5e467e65f84ff58ea24d0: ValueError: Macro talos_leg_simple_transmission requires unsupported explicit arguments: ['side', 'number', 'reduction']

- https://github.com/pal-robotics/talos_robot talos_description/robots/talos_arm_right.urdf.xacro at 79709aa4f4f453ec18a5e467e65f84ff58ea24d0: XacroException: No such file or directory: .cache/pal-robotics__talos_robot/.drift_xacro/tmprs9r67nf/.unresolved_package/pal_urdf_utils/urdf/deg_to_rad.urdf.xacro [Errno 2] No such file or directory: '.cache/pal-robotics__talos_robot/.drift_xacro/tmprs9r67nf/.unresolved_package/pal_urdf_utils/urdf/deg_to_rad.urdf.xacro'

- https://github.com/pal-robotics/talos_robot talos_description/urdf/arm/wrist.ros2_control.xacro at 79709aa4f4f453ec18a5e467e65f84ff58ea24d0: ValueError: Macro ros2_control_wrist requires unsupported explicit arguments: ['side', 'joint_5_offset', 'joint_6_offset', 'joint_7_offset']

- https://github.com/pal-robotics/talos_robot talos_description/urdf/arm/wrist.transmission.xacro at 79709aa4f4f453ec18a5e467e65f84ff58ea24d0: ValueError: Macro-only input has no uniquely identified robot macro

- https://github.com/pal-robotics/talos_robot talos_description/urdf/head/head.ros2_control.xacro at 79709aa4f4f453ec18a5e467e65f84ff58ea24d0: ValueError: Macro ros2_control_head requires unsupported explicit arguments: ['number_1', 'number_2', 'offset_value_1', 'offset_value_2']

- https://github.com/pal-robotics/talos_robot talos_description/urdf/head/head.transmission.xacro at 79709aa4f4f453ec18a5e467e65f84ff58ea24d0: ValueError: Macro talos_head_differential_transmission requires unsupported explicit arguments: ['number1', 'number2', 'act_reduction1', 'act_reduction2', 'jnt_reduction1', 'jnt_reduction2', 'offset_value_1', 'offset_value_2']

- https://github.com/pal-robotics/talos_robot talos_description/urdf/talos_full_common.urdf.xacro at 79709aa4f4f453ec18a5e467e65f84ff58ea24d0: XacroException: No such file or directory: .cache/pal-robotics__talos_robot/.drift_xacro/tmpth1tadmk/.unresolved_package/pal_urdf_utils/urdf/deg_to_rad.urdf.xacro [Errno 2] No such file or directory: '.cache/pal-robotics__talos_robot/.drift_xacro/tmpth1tadmk/.unresolved_package/pal_urdf_utils/urdf/deg_to_rad.urdf.xacro'

- https://github.com/pal-robotics/talos_robot talos_description/robots/talos_lower_body.urdf.xacro at 79709aa4f4f453ec18a5e467e65f84ff58ea24d0: XacroException: No such file or directory: .cache/pal-robotics__talos_robot/.drift_xacro/tmpsh1mjoh6/.unresolved_package/pal_urdf_utils/urdf/ft_sensors/ati_talos.urdf.xacro [Errno 2] No such file or directory: '.cache/pal-robotics__talos_robot/.drift_xacro/tmpsh1mjoh6/.unresolved_package/pal_urdf_utils/urdf/ft_sensors/ati_talos.urdf.xacro'

- https://github.com/pal-robotics/talos_robot talos_description/urdf/torso/torso.ros2_control.xacro at 79709aa4f4f453ec18a5e467e65f84ff58ea24d0: ValueError: XML Error: missing element: 'parent'
Element 'joint', line 1


- https://github.com/pal-robotics/talos_robot talos_description/urdf/torso/torso.transmission.xacro at 79709aa4f4f453ec18a5e467e65f84ff58ea24d0: ValueError: Macro talos_torso_differential_transmission requires unsupported explicit arguments: ['number1', 'number2', 'act_reduction1', 'act_reduction2', 'jnt_reduction1', 'jnt_reduction2']

- https://github.com/pal-robotics/talos_robot talos_description/ros2_control/ros2_control.urdf.xacro at 79709aa4f4f453ec18a5e467e65f84ff58ea24d0: XacroException: No such file or directory: .cache/pal-robotics__talos_robot/.drift_xacro/tmpihp27d28/.unresolved_package/pal_urdf_utils/urdf/interaction_sensors/imu_sensors.ros2_control.xacro [Errno 2] No such file or directory: '.cache/pal-robotics__talos_robot/.drift_xacro/tmpihp27d28/.unresolved_package/pal_urdf_utils/urdf/interaction_sensors/imu_sensors.ros2_control.xacro'

- https://github.com/pal-robotics/talos_robot talos_description/urdf/arm/arm_specifics_v1.urdf.xacro at 79709aa4f4f453ec18a5e467e65f84ff58ea24d0: ValueError: Macro arm_1_joint_limits requires unsupported explicit arguments: ['reflect']

- https://github.com/pal-robotics/talos_robot talos_description/urdf/arm/arm_specifics_v2.urdf.xacro at 79709aa4f4f453ec18a5e467e65f84ff58ea24d0: ValueError: Macro arm_1_joint_limits requires unsupported explicit arguments: ['reflect']

- https://github.com/pal-robotics/talos_robot talos_description/urdf/gripper/gripper.ros2_control.xacro at 79709aa4f4f453ec18a5e467e65f84ff58ea24d0: ValueError: XML Error: missing element: 'parent'
Element 'joint', line 1


- https://github.com/pal-robotics/talos_robot talos_description/urdf/gripper/gripper.transmission.xacro at 79709aa4f4f453ec18a5e467e65f84ff58ea24d0: ValueError: Macro gripper_transmission requires unsupported explicit arguments: ['reduction']

- https://github.com/pal-robotics/talos_robot talos_description/robots/talos_full_no_grippers.urdf.xacro at 79709aa4f4f453ec18a5e467e65f84ff58ea24d0: XacroException: Undefined substitution argument enable_crane

- https://github.com/pal-robotics/talos_robot talos_description/robots/talos_full_fake_grippers.urdf.xacro at 79709aa4f4f453ec18a5e467e65f84ff58ea24d0: XacroException: Undefined substitution argument enable_crane

- https://github.com/pal-robotics/talos_robot talos_description/urdf/leg/foot_collision_default.urdf.xacro at 79709aa4f4f453ec18a5e467e65f84ff58ea24d0: XacroException: name 'reflect' is not defined
when evaluating expression 'reflect*1.05'

- https://github.com/pal-robotics/talos_robot talos_description/urdf/leg/foot_collision_tallbox.urdf.xacro at 79709aa4f4f453ec18a5e467e65f84ff58ea24d0: ValueError: XML has no robot bodies; it is an include/extension fragment, not a standalone source

- https://github.com/pal-robotics/talos_robot talos_description/urdf/leg/foot_collision_thinbox.urdf.xacro at 79709aa4f4f453ec18a5e467e65f84ff58ea24d0: ValueError: XML has no robot bodies; it is an include/extension fragment, not a standalone source

- https://github.com/pal-robotics/talos_robot talos_description/robots/talos_lower_body_torso_head.urdf.xacro at 79709aa4f4f453ec18a5e467e65f84ff58ea24d0: XacroException: Undefined substitution argument enable_crane

- https://github.com/unitreerobotics/unitree_ros robots/go2_description/xacro/leg.xacro at 157ff950351e5f535e03c5d85a16b7d594b3dbcc: ValueError: Macro leg requires unsupported explicit arguments: ['mirror', 'mirror_dae', 'front_hind', 'front_hind_dae']

- https://github.com/unitreerobotics/unitree_ros robots/go2_description/xacro/const.xacro at 157ff950351e5f535e03c5d85a16b7d594b3dbcc: ValueError: XML has no robot bodies; it is an include/extension fragment, not a standalone source

- https://github.com/unitreerobotics/unitree_ros robots/go2_description/xacro/robot.xacro at 157ff950351e5f535e03c5d85a16b7d594b3dbcc: ValueError: Resource missing at 157ff950351e5f535e03c5d85a16b7d594b3dbcc: robots/go2_description/xacro/robots/go2_description/meshes/trunk.dae

- https://github.com/unitreerobotics/unitree_ros robots/go2_description/xacro/gazebo.xacro at 157ff950351e5f535e03c5d85a16b7d594b3dbcc: ValueError: XML has no robot bodies; it is an include/extension fragment, not a standalone source

- https://github.com/unitreerobotics/unitree_ros robots/go2_description/xacro/materials.xacro at 157ff950351e5f535e03c5d85a16b7d594b3dbcc: ValueError: XML has no robot bodies; it is an include/extension fragment, not a standalone source

- https://github.com/unitreerobotics/unitree_ros robots/go2_description/xacro/transmission.xacro at 157ff950351e5f535e03c5d85a16b7d594b3dbcc: ValueError: XML has no robot bodies; it is an include/extension fragment, not a standalone source

- https://github.com/unitreerobotics/unitree_ros robots/go2_description/urdf/go2_description.urdf at 157ff950351e5f535e03c5d85a16b7d594b3dbcc: ValueError: XML Error: repeated element: 'material'
Element 'material', line 13


- Offline Git read failed (exit 128): `('log', '--all', '--follow', '--find-renames=100%', '--format=@@@%H|%ct|%cI|%s', '--name-status', '--', 'urdf/00-arm-rs_asm-v3/urdf/00-arm-rs_asm-v3.urdf')` in `Seeed-Projects__reBot-Isaacsim`. warning: lazy fetching disabled; some objects may not be available
fatal: could not fetch d91aac9cb500116a7b06841effb7d93156a7ac1e from promisor remote

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/Seeed-Projects__reBot-Isaacsim -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `d91aac9cb500116a7b06841effb7d93156a7ac1e`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('log', '--all', '--follow', '--find-renames=100%', '--format=@@@%H|%ct|%cI|%s', '--name-status', '--', 'urdf/00-arm-rs_asm-v3/urdf/00-arm-rs_asm-v3.urdf')` in `Seeed-Projects__reBot-Isaacsim`. warning: lazy fetching disabled; some objects may not be available
fatal: could not fetch 6f003b370073edddb1e737a3c0c85e2099511ba7 from promisor remote

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/Seeed-Projects__reBot-Isaacsim -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `6f003b370073edddb1e737a3c0c85e2099511ba7`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('log', '--all', '--follow', '--find-renames=100%', '--format=@@@%H|%ct|%cI|%s', '--name-status', '--', 'urdf/00-arm-rs_asm-v3/urdf/00-arm-rs_asm-v3.urdf')` in `Seeed-Projects__reBot-Isaacsim`. warning: lazy fetching disabled; some objects may not be available
fatal: could not fetch 08434cd09b9c8bedcdad539477f2fa0c72c155cf from promisor remote

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/Seeed-Projects__reBot-Isaacsim -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `08434cd09b9c8bedcdad539477f2fa0c72c155cf`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('log', '--all', '--follow', '--find-renames=100%', '--format=@@@%H|%ct|%cI|%s', '--name-status', '--', 'urdf/00-arm-rs_asm-v3/urdf/00-arm-rs_asm-v3.urdf')` in `Seeed-Projects__reBot-Isaacsim`. warning: lazy fetching disabled; some objects may not be available
fatal: could not fetch 94a86f6fb845ad43eefc56aa0b5e90a3bff298de from promisor remote

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/Seeed-Projects__reBot-Isaacsim -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `94a86f6fb845ad43eefc56aa0b5e90a3bff298de`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('log', '--all', '--follow', '--find-renames=100%', '--format=@@@%H|%ct|%cI|%s', '--name-status', '--', 'urdf/00-arm-rs_asm-v3/urdf/00-arm-rs_asm-v3.urdf')` in `Seeed-Projects__reBot-Isaacsim`. warning: lazy fetching disabled; some objects may not be available
fatal: could not fetch 725d5f3245c8fb0f0897b5329ae852aa385d2e6d from promisor remote

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/Seeed-Projects__reBot-Isaacsim -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `725d5f3245c8fb0f0897b5329ae852aa385d2e6d`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('log', '--all', '--follow', '--find-renames=100%', '--format=@@@%H|%ct|%cI|%s', '--name-status', '--', 'urdf/00-arm-rs_asm-v3/urdf/00-arm-rs_asm-v3.urdf')` in `Seeed-Projects__reBot-Isaacsim`. warning: lazy fetching disabled; some objects may not be available
fatal: could not fetch 2dc8e9c1e4c1a67c619e73b5310e1d32f14501d9 from promisor remote

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/Seeed-Projects__reBot-Isaacsim -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `2dc8e9c1e4c1a67c619e73b5310e1d32f14501d9`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('log', '--all', '--follow', '--find-renames=100%', '--format=@@@%H|%ct|%cI|%s', '--name-status', '--', 'urdf/00-arm-rs_asm-v3/urdf/00-arm-rs_asm-v3.urdf')` in `Seeed-Projects__reBot-Isaacsim`. warning: lazy fetching disabled; some objects may not be available
fatal: could not fetch a0a12edca6d3b8e7e2a90b9153eee714bd97b238 from promisor remote

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/Seeed-Projects__reBot-Isaacsim -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `a0a12edca6d3b8e7e2a90b9153eee714bd97b238`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('log', '--all', '--follow', '--find-renames=100%', '--format=@@@%H|%ct|%cI|%s', '--name-status', '--', 'urdf/00-arm-rs_asm-v3/urdf/00-arm-rs_asm-v3.urdf')` in `Seeed-Projects__reBot-Isaacsim`. warning: lazy fetching disabled; some objects may not be available
fatal: could not fetch d83d030e7a10b387b2e6a6dc75afcc769c971cf0 from promisor remote

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/Seeed-Projects__reBot-Isaacsim -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `d83d030e7a10b387b2e6a6dc75afcc769c971cf0`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('log', '--all', '--follow', '--find-renames=100%', '--format=@@@%H|%ct|%cI|%s', '--name-status', '--', 'urdf/00-arm-rs_asm-v3/urdf/00-arm-rs_asm-v3.urdf')` in `Seeed-Projects__reBot-Isaacsim`. warning: lazy fetching disabled; some objects may not be available
fatal: could not fetch 36eab64ec041a3c7de347746c050e9bfff0c6461 from promisor remote

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/Seeed-Projects__reBot-Isaacsim -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `36eab64ec041a3c7de347746c050e9bfff0c6461`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('log', '--all', '--follow', '--find-renames=100%', '--format=@@@%H|%ct|%cI|%s', '--name-status', '--', 'urdf/00-arm-rs_asm-v3/urdf/00-arm-rs_asm-v3.urdf')` in `Seeed-Projects__reBot-Isaacsim`. warning: lazy fetching disabled; some objects may not be available
fatal: could not fetch e0dae721076ed05127d634eaa32f6a25354ac9f1 from promisor remote

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/Seeed-Projects__reBot-Isaacsim -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `e0dae721076ed05127d634eaa32f6a25354ac9f1`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('log', '--all', '--follow', '--find-renames=100%', '--format=@@@%H|%ct|%cI|%s', '--name-status', '--', 'urdf/00-arm-rs_asm-v3/urdf/00-arm-rs_asm-v3.urdf')` in `Seeed-Projects__reBot-Isaacsim`. warning: lazy fetching disabled; some objects may not be available
fatal: could not fetch c18e8139a1af784f65bdff9d5e4af42036fb0910 from promisor remote

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/Seeed-Projects__reBot-Isaacsim -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `c18e8139a1af784f65bdff9d5e4af42036fb0910`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('log', '--all', '--follow', '--find-renames=100%', '--format=@@@%H|%ct|%cI|%s', '--name-status', '--', 'urdf/00-arm-rs_asm-v3/urdf/00-arm-rs_asm-v3.urdf')` in `Seeed-Projects__reBot-Isaacsim`. warning: lazy fetching disabled; some objects may not be available
fatal: could not fetch 18c31cbf708661efa9784383a8dead12b2ce943e from promisor remote

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/Seeed-Projects__reBot-Isaacsim -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `18c31cbf708661efa9784383a8dead12b2ce943e`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('log', '--all', '--follow', '--find-renames=100%', '--format=@@@%H|%ct|%cI|%s', '--name-status', '--', 'urdf/00-arm-rs_asm-v3/urdf/00-arm-rs_asm-v3.urdf')` in `Seeed-Projects__reBot-Isaacsim`. warning: lazy fetching disabled; some objects may not be available
fatal: could not fetch f78cc2b9a62c2d915e903ae2b567fb80b270779d from promisor remote

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/Seeed-Projects__reBot-Isaacsim -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `f78cc2b9a62c2d915e903ae2b567fb80b270779d`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('log', '--all', '--follow', '--find-renames=100%', '--format=@@@%H|%ct|%cI|%s', '--name-status', '--', 'urdf/00-arm-rs_asm-v3/urdf/00-arm-rs_asm-v3.urdf')` in `Seeed-Projects__reBot-Isaacsim`. warning: lazy fetching disabled; some objects may not be available
fatal: could not fetch e5f241cf76e96f299f3833d57ec7daa2c1ec2ee1 from promisor remote

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/Seeed-Projects__reBot-Isaacsim -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `e5f241cf76e96f299f3833d57ec7daa2c1ec2ee1`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('log', '--all', '--follow', '--find-renames=100%', '--format=@@@%H|%ct|%cI|%s', '--name-status', '--', 'urdf/00-arm-rs_asm-v3/urdf/00-arm-rs_asm-v3.urdf')` in `Seeed-Projects__reBot-Isaacsim`. warning: lazy fetching disabled; some objects may not be available
fatal: could not fetch ab9103daf614f6ed3ad665030e45ec28604dcaa7 from promisor remote

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/Seeed-Projects__reBot-Isaacsim -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `ab9103daf614f6ed3ad665030e45ec28604dcaa7`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('log', '--all', '--follow', '--find-renames=100%', '--format=@@@%H|%ct|%cI|%s', '--name-status', '--', 'urdf/00-arm-rs_asm-v3/urdf/00-arm-rs_asm-v3.urdf')` in `Seeed-Projects__reBot-Isaacsim`. warning: lazy fetching disabled; some objects may not be available
fatal: could not fetch 305fc0de99f46d50daeca28f75a536ca63f7f627 from promisor remote

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/Seeed-Projects__reBot-Isaacsim -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `305fc0de99f46d50daeca28f75a536ca63f7f627`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('log', '--all', '--follow', '--find-renames=100%', '--format=@@@%H|%ct|%cI|%s', '--name-status', '--', 'urdf/00-arm-rs_asm-v3/urdf/00-arm-rs_asm-v3.urdf')` in `Seeed-Projects__reBot-Isaacsim`. warning: lazy fetching disabled; some objects may not be available
fatal: could not fetch 3df039e5f3f8e3ab7a4d58f0d784f64d23b5737f from promisor remote

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/Seeed-Projects__reBot-Isaacsim -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `3df039e5f3f8e3ab7a4d58f0d784f64d23b5737f`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('log', '--all', '--follow', '--find-renames=100%', '--format=@@@%H|%ct|%cI|%s', '--name-status', '--', 'urdf/00-arm-rs_asm-v3/urdf/00-arm-rs_asm-v3.urdf')` in `Seeed-Projects__reBot-Isaacsim`. warning: lazy fetching disabled; some objects may not be available
fatal: could not fetch 28a8f85aba11e5f99781257ffcff0122f4cfe6a6 from promisor remote

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/Seeed-Projects__reBot-Isaacsim -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `28a8f85aba11e5f99781257ffcff0122f4cfe6a6`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('log', '--all', '--follow', '--find-renames=100%', '--format=@@@%H|%ct|%cI|%s', '--name-status', '--', 'urdf/00-arm-rs_asm-v3/urdf/00-arm-rs_asm-v3.urdf')` in `Seeed-Projects__reBot-Isaacsim`. warning: lazy fetching disabled; some objects may not be available
fatal: could not fetch 3e29f8487bc5f5130bb8bc8ad7e26f59e4244d02 from promisor remote

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/Seeed-Projects__reBot-Isaacsim -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `3e29f8487bc5f5130bb8bc8ad7e26f59e4244d02`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('log', '--all', '--follow', '--find-renames=100%', '--format=@@@%H|%ct|%cI|%s', '--name-status', '--', 'urdf/00-arm-rs_asm-v3/urdf/00-arm-rs_asm-v3.urdf')` in `Seeed-Projects__reBot-Isaacsim`. warning: lazy fetching disabled; some objects may not be available
fatal: could not fetch 0d2b1a097412e6b43fc190ba6e25513cc985a594 from promisor remote

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/Seeed-Projects__reBot-Isaacsim -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `0d2b1a097412e6b43fc190ba6e25513cc985a594`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('log', '--all', '--follow', '--find-renames=100%', '--format=@@@%H|%ct|%cI|%s', '--name-status', '--', 'urdf/00-arm-rs_asm-v3/urdf/00-arm-rs_asm-v3.urdf')` in `Seeed-Projects__reBot-Isaacsim`. warning: lazy fetching disabled; some objects may not be available
fatal: could not fetch c10ecdd0e76894c2895f93561a2ed9274a337605 from promisor remote

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/Seeed-Projects__reBot-Isaacsim -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `c10ecdd0e76894c2895f93561a2ed9274a337605`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('log', '--all', '--follow', '--find-renames=100%', '--format=@@@%H|%ct|%cI|%s', '--name-status', '--', 'urdf/00-arm-rs_asm-v3/urdf/00-arm-rs_asm-v3.urdf')` in `Seeed-Projects__reBot-Isaacsim`. warning: lazy fetching disabled; some objects may not be available
fatal: could not fetch 56688795ab9fa759222f560a4e4b9a4d37a2f689 from promisor remote

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/Seeed-Projects__reBot-Isaacsim -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `56688795ab9fa759222f560a4e4b9a4d37a2f689`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('log', '--all', '--follow', '--find-renames=100%', '--format=@@@%H|%ct|%cI|%s', '--name-status', '--', 'urdf/00-arm-rs_asm-v3/urdf/00-arm-rs_asm-v3.urdf')` in `Seeed-Projects__reBot-Isaacsim`. warning: lazy fetching disabled; some objects may not be available
fatal: could not fetch 71e39112171ab1e714ac43ed174e34332870931d from promisor remote

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/Seeed-Projects__reBot-Isaacsim -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `71e39112171ab1e714ac43ed174e34332870931d`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('log', '--all', '--follow', '--find-renames=100%', '--format=@@@%H|%ct|%cI|%s', '--name-status', '--', 'urdf/00-arm-rs_asm-v3/urdf/00-arm-rs_asm-v3.urdf')` in `Seeed-Projects__reBot-Isaacsim`. warning: lazy fetching disabled; some objects may not be available
fatal: could not fetch b680dfa34ed9a48d9967e844a4c7b60915e21ed4 from promisor remote

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/Seeed-Projects__reBot-Isaacsim -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `b680dfa34ed9a48d9967e844a4c7b60915e21ed4`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('log', '--all', '--follow', '--find-renames=100%', '--format=@@@%H|%ct|%cI|%s', '--name-status', '--', 'urdf/00-arm-rs_asm-v3/urdf/00-arm-rs_asm-v3.urdf')` in `Seeed-Projects__reBot-Isaacsim`. warning: lazy fetching disabled; some objects may not be available
fatal: could not fetch a8af1d5978766e2e6d458416051660faeed8efd5 from promisor remote

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/Seeed-Projects__reBot-Isaacsim -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `a8af1d5978766e2e6d458416051660faeed8efd5`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('log', '--all', '--follow', '--find-renames=100%', '--format=@@@%H|%ct|%cI|%s', '--name-status', '--', 'urdf/00-arm-rs_asm-v3/urdf/00-arm-rs_asm-v3.urdf')` in `Seeed-Projects__reBot-Isaacsim`. warning: lazy fetching disabled; some objects may not be available
fatal: could not fetch 67b2e22a160245fd713acf909df94c9166f8cdfe from promisor remote

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/Seeed-Projects__reBot-Isaacsim -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `67b2e22a160245fd713acf909df94c9166f8cdfe`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('log', '--all', '--follow', '--find-renames=100%', '--format=@@@%H|%ct|%cI|%s', '--name-status', '--', 'urdf/00-arm-rs_asm-v3/urdf/00-arm-rs_asm-v3.urdf')` in `Seeed-Projects__reBot-Isaacsim`. warning: lazy fetching disabled; some objects may not be available
fatal: could not fetch 2bdb6ede01b35f1a921b016ba08a43e0aa577125 from promisor remote

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/Seeed-Projects__reBot-Isaacsim -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `2bdb6ede01b35f1a921b016ba08a43e0aa577125`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('log', '--all', '--follow', '--find-renames=100%', '--format=@@@%H|%ct|%cI|%s', '--name-status', '--', 'urdf/00-arm-rs_asm-v3/urdf/00-arm-rs_asm-v3.urdf')` in `Seeed-Projects__reBot-Isaacsim`. warning: lazy fetching disabled; some objects may not be available
fatal: could not fetch 6da0443e5d1360d68f48ca3126a1d9820035a775 from promisor remote

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/Seeed-Projects__reBot-Isaacsim -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `6da0443e5d1360d68f48ca3126a1d9820035a775`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('log', '--all', '--follow', '--find-renames=100%', '--format=@@@%H|%ct|%cI|%s', '--name-status', '--', 'urdf/00-arm-rs_asm-v3/urdf/00-arm-rs_asm-v3.urdf')` in `Seeed-Projects__reBot-Isaacsim`. warning: lazy fetching disabled; some objects may not be available
fatal: could not fetch 7175ca67501920fb9b9cdcb04130bf65e53c44df from promisor remote

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/Seeed-Projects__reBot-Isaacsim -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `7175ca67501920fb9b9cdcb04130bf65e53c44df`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('log', '--all', '--follow', '--find-renames=100%', '--format=@@@%H|%ct|%cI|%s', '--name-status', '--', 'urdf/00-arm-rs_asm-v3/urdf/00-arm-rs_asm-v3.urdf')` in `Seeed-Projects__reBot-Isaacsim`. warning: lazy fetching disabled; some objects may not be available
fatal: could not fetch 68af2a872a6d70e3290c1134f79c6269d73ae1e3 from promisor remote

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/Seeed-Projects__reBot-Isaacsim -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `68af2a872a6d70e3290c1134f79c6269d73ae1e3`

- Network outcome: exit 0.

- Repair check failed seeed_rebot_devarm: ValueError: Rename-following dependency fetch exceeded 30 objects; history is unresolved

- Rejected unrelated historical README template for agilex_piper: 0bee963312f0f4a25b53cdf9afe744ca73f2d68a heading '## UMI-Gripper Description (MJCF)'

- Offline Git read failed (exit 128): `('show', '400b5f5b9fec382583f69b53b094a154d9dc7635:agilex_piper/CHANGELOG.md')` in `menagerie`. fatal: path 'agilex_piper/CHANGELOG.md' does not exist in '400b5f5b9fec382583f69b53b094a154d9dc7635'

- Rejected conflicting robot-variant link for anybotics_anymal_c: https://github.com/ANYbotics/anymal_b_simple_description/blob/master/urdf/anymal.urdf (repository variant b, model variant c)

- Offline Git read failed (exit 128): `('show', 'd9415a3076f921fdb9735d45d609a596df722468:apptronik_apollo/CHANGELOG.md')` in `menagerie`. fatal: bad object d9415a3076f921fdb9735d45d609a596df722468:apptronik_apollo/CHANGELOG.md

- Offline Git read failed (exit 128): `('show', '400b5f5b9fec382583f69b53b094a154d9dc7635:arx_l5/CHANGELOG.md')` in `menagerie`. fatal: path 'arx_l5/CHANGELOG.md' does not exist in '400b5f5b9fec382583f69b53b094a154d9dc7635'

- Offline Git read failed (exit 128): `('show', 'd9415a3076f921fdb9735d45d609a596df722468:berkeley_humanoid/CHANGELOG.md')` in `menagerie`. fatal: bad object d9415a3076f921fdb9735d45d609a596df722468:berkeley_humanoid/CHANGELOG.md

- Rejected conflicting robot-variant link for bitcraze_crazyflie_2: https://github.com/whoenig/crazyflie_ros (repository variant ros, model variant 2)

- Offline Git read failed (exit 128): `('show', 'd9415a3076f921fdb9735d45d609a596df722468:booster_t1/CHANGELOG.md')` in `menagerie`. fatal: bad object d9415a3076f921fdb9735d45d609a596df722468:booster_t1/CHANGELOG.md

- Offline Git read failed (exit 128): `('show', 'd9415a3076f921fdb9735d45d609a596df722468:fourier_n1/CHANGELOG.md')` in `menagerie`. fatal: bad object d9415a3076f921fdb9735d45d609a596df722468:fourier_n1/CHANGELOG.md

- Offline Git read failed (exit 128): `('show', '400b5f5b9fec382583f69b53b094a154d9dc7635:fourier_n1/CHANGELOG.md')` in `menagerie`. fatal: path 'fourier_n1/CHANGELOG.md' does not exist in '400b5f5b9fec382583f69b53b094a154d9dc7635'

- Offline Git read failed (exit 128): `('show', 'db140ade7ee4cb59629f9687aafc65af663d5bbe:franka_fr3_v2/README.md')` in `menagerie`. fatal: path 'franka_fr3_v2/README.md' does not exist in 'db140ade7ee4cb59629f9687aafc65af663d5bbe'

- Offline Git read failed (exit 128): `('show', 'cd7fc51b704c3cba05748bd5537cb17990b341eb:franka_fr3_v2/README.md')` in `menagerie`. fatal: path 'franka_fr3_v2/README.md' does not exist in 'cd7fc51b704c3cba05748bd5537cb17990b341eb'

- Offline Git read failed (exit 128): `('show', '400b5f5b9fec382583f69b53b094a154d9dc7635:franka_fr3_v2/README.md')` in `menagerie`. fatal: path 'franka_fr3_v2/README.md' does not exist in '400b5f5b9fec382583f69b53b094a154d9dc7635'

- Offline Git read failed (exit 128): `('show', 'acbbf1636fcfef9b437a6eb8c6f84380fb4aa998:franka_fr3_v2/README.md')` in `menagerie`. fatal: path 'franka_fr3_v2/README.md' does not exist in 'acbbf1636fcfef9b437a6eb8c6f84380fb4aa998'

- Offline Git read failed (exit 128): `('show', '7876dcdef0d912387441616526ed236142f047d3:franka_fr3_v2/README.md')` in `menagerie`. fatal: path 'franka_fr3_v2/README.md' does not exist in '7876dcdef0d912387441616526ed236142f047d3'

- Offline Git read failed (exit 128): `('show', 'b5ebfe0cf079d2b96acf0a5c0e29ee0c95ba32f4:google_robot/README.md')` in `menagerie`. fatal: path 'google_robot/README.md' does not exist in 'b5ebfe0cf079d2b96acf0a5c0e29ee0c95ba32f4'

- Offline Git read failed (exit 128): `('show', '5ce04bea98bbfca277a8d50b55ba3c7c4a62bdec:i2rt_yam/CHANGELOG.md')` in `menagerie`. fatal: path 'i2rt_yam/CHANGELOG.md' does not exist in '5ce04bea98bbfca277a8d50b55ba3c7c4a62bdec'

- Offline Git read failed (exit 128): `('show', 'a88bc450470d97ebc1f282e5969675fb4d1f0ed7:low_cost_robot_arm/README.md')` in `menagerie`. fatal: path 'low_cost_robot_arm/README.md' does not exist in 'a88bc450470d97ebc1f282e5969675fb4d1f0ed7'

- Offline Git read failed (exit 128): `('show', 'd74280a600a9afdfcb98d8917d0c79c86539aa61:low_cost_robot_arm/README.md')` in `menagerie`. fatal: path 'low_cost_robot_arm/README.md' does not exist in 'd74280a600a9afdfcb98d8917d0c79c86539aa61'

- Offline Git read failed (exit 128): `('show', '13d6c48b8f59d2c4badee7756b4ea3532613cddf:low_cost_robot_arm/README.md')` in `menagerie`. fatal: path 'low_cost_robot_arm/README.md' does not exist in '13d6c48b8f59d2c4badee7756b4ea3532613cddf'

- Offline Git read failed (exit 128): `('show', 'fae9ee82330444eec4e87568c838b99a09a39467:rainbow_robotics_rby1/README.md')` in `menagerie`. fatal: path 'rainbow_robotics_rby1/README.md' does not exist in 'fae9ee82330444eec4e87568c838b99a09a39467'

- Offline Git read failed (exit 128): `('show', '04674c8d0a4e12e33980a9e47fb604adc281fcc8:robotstudio_so101/CHANGELOG.md')` in `menagerie`. fatal: path 'robotstudio_so101/CHANGELOG.md' does not exist in '04674c8d0a4e12e33980a9e47fb604adc281fcc8'

- Offline Git read failed (exit 128): `('show', '5ce04bea98bbfca277a8d50b55ba3c7c4a62bdec:robotstudio_so101/CHANGELOG.md')` in `menagerie`. fatal: path 'robotstudio_so101/CHANGELOG.md' does not exist in '5ce04bea98bbfca277a8d50b55ba3c7c4a62bdec'

- Offline Git read failed (exit 128): `('show', '4a7015530bd7a4161103ae8f0905a96481e4cc1a:robotstudio_so101/CHANGELOG.md')` in `menagerie`. fatal: path 'robotstudio_so101/CHANGELOG.md' does not exist in '4a7015530bd7a4161103ae8f0905a96481e4cc1a'

- Offline Git read failed (exit 128): `('show', 'bf110a75a56e5bd146c7ed76965737c71d48425d:shadow_dexee/README.md')` in `menagerie`. fatal: path 'shadow_dexee/README.md' does not exist in 'bf110a75a56e5bd146c7ed76965737c71d48425d'

- Offline Git read failed (exit 128): `('show', '04674c8d0a4e12e33980a9e47fb604adc281fcc8:tetheria_aero_hand_open/CHANGELOG.md')` in `menagerie`. fatal: path 'tetheria_aero_hand_open/CHANGELOG.md' does not exist in '04674c8d0a4e12e33980a9e47fb604adc281fcc8'

- Offline Git read failed (exit 128): `('show', '400b5f5b9fec382583f69b53b094a154d9dc7635:tetheria_aero_hand_open/CHANGELOG.md')` in `menagerie`. fatal: path 'tetheria_aero_hand_open/CHANGELOG.md' does not exist in '400b5f5b9fec382583f69b53b094a154d9dc7635'

- Offline Git read failed (exit 128): `('show', '04674c8d0a4e12e33980a9e47fb604adc281fcc8:toddlerbot_2xc/CHANGELOG.md')` in `menagerie`. fatal: path 'toddlerbot_2xc/CHANGELOG.md' does not exist in '04674c8d0a4e12e33980a9e47fb604adc281fcc8'

- Offline Git read failed (exit 128): `('show', '9e7f8d4dda07f5c281b6c0c6f0d07b9dd267b762:toddlerbot_2xc/CHANGELOG.md')` in `menagerie`. fatal: path 'toddlerbot_2xc/CHANGELOG.md' does not exist in '9e7f8d4dda07f5c281b6c0c6f0d07b9dd267b762'

- Offline Git read failed (exit 128): `('show', '400b5f5b9fec382583f69b53b094a154d9dc7635:toddlerbot_2xc/CHANGELOG.md')` in `menagerie`. fatal: path 'toddlerbot_2xc/CHANGELOG.md' does not exist in '400b5f5b9fec382583f69b53b094a154d9dc7635'

- Offline Git read failed (exit 128): `('show', '04674c8d0a4e12e33980a9e47fb604adc281fcc8:toddlerbot_2xm/CHANGELOG.md')` in `menagerie`. fatal: path 'toddlerbot_2xm/CHANGELOG.md' does not exist in '04674c8d0a4e12e33980a9e47fb604adc281fcc8'

- Offline Git read failed (exit 128): `('show', '9e7f8d4dda07f5c281b6c0c6f0d07b9dd267b762:toddlerbot_2xm/CHANGELOG.md')` in `menagerie`. fatal: path 'toddlerbot_2xm/CHANGELOG.md' does not exist in '9e7f8d4dda07f5c281b6c0c6f0d07b9dd267b762'

- Offline Git read failed (exit 128): `('show', '400b5f5b9fec382583f69b53b094a154d9dc7635:toddlerbot_2xm/CHANGELOG.md')` in `menagerie`. fatal: path 'toddlerbot_2xm/CHANGELOG.md' does not exist in '400b5f5b9fec382583f69b53b094a154d9dc7635'

- Offline Git read failed (exit 128): `('show', '400b5f5b9fec382583f69b53b094a154d9dc7635:trossen_wxai/README.md')` in `menagerie`. fatal: path 'trossen_wxai/README.md' does not exist in '400b5f5b9fec382583f69b53b094a154d9dc7635'

- Offline Git read failed (exit 128): `('show', '477ec56566682d663b996d86a188c75499e74b98:trossen_wxai/README.md')` in `menagerie`. fatal: path 'trossen_wxai/README.md' does not exist in '477ec56566682d663b996d86a188c75499e74b98'

- Offline Git read failed (exit 128): `('show', 'd9415a3076f921fdb9735d45d609a596df722468:unitree_g1/CHANGELOG.md')` in `menagerie`. fatal: bad object d9415a3076f921fdb9735d45d609a596df722468:unitree_g1/CHANGELOG.md

- Offline Git read failed (exit 128): `('log', '--all', '--follow', '--find-renames=100%', '--format=@@@%H|%ct|%cI|%s', '--name-status', '--', 'urdf/00-arm-rs_asm-v3/urdf/00-arm-rs_asm-v3.urdf')` in `Seeed-Projects__reBot-Isaacsim`. warning: lazy fetching disabled; some objects may not be available
fatal: could not fetch b69ef48da4705cc5bb2e1e457f4c712026499b81 from promisor remote

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/Seeed-Projects__reBot-Isaacsim -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `b69ef48da4705cc5bb2e1e457f4c712026499b81`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('log', '--all', '--follow', '--find-renames=100%', '--format=@@@%H|%ct|%cI|%s', '--name-status', '--', 'urdf/00-arm-rs_asm-v3/urdf/00-arm-rs_asm-v3.urdf')` in `Seeed-Projects__reBot-Isaacsim`. warning: lazy fetching disabled; some objects may not be available
fatal: could not fetch e2b4e9ed4a6563cb5585f0fe6bd47b2dfe03ee65 from promisor remote

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/Seeed-Projects__reBot-Isaacsim -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `e2b4e9ed4a6563cb5585f0fe6bd47b2dfe03ee65`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('log', '--all', '--follow', '--find-renames=100%', '--format=@@@%H|%ct|%cI|%s', '--name-status', '--', 'urdf/00-arm-rs_asm-v3/urdf/00-arm-rs_asm-v3.urdf')` in `Seeed-Projects__reBot-Isaacsim`. warning: lazy fetching disabled; some objects may not be available
fatal: could not fetch 5b990e4f9311c6c7ac83b8d19ae3a8aef04a957c from promisor remote

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/Seeed-Projects__reBot-Isaacsim -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `5b990e4f9311c6c7ac83b8d19ae3a8aef04a957c`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('log', '--all', '--follow', '--find-renames=100%', '--format=@@@%H|%ct|%cI|%s', '--name-status', '--', 'urdf/00-arm-rs_asm-v3/urdf/00-arm-rs_asm-v3.urdf')` in `Seeed-Projects__reBot-Isaacsim`. warning: lazy fetching disabled; some objects may not be available
fatal: could not fetch d1d766ab4aaa09640577c4ccfb421460b609fde3 from promisor remote

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/Seeed-Projects__reBot-Isaacsim -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `d1d766ab4aaa09640577c4ccfb421460b609fde3`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('log', '--all', '--follow', '--find-renames=100%', '--format=@@@%H|%ct|%cI|%s', '--name-status', '--', 'urdf/00-arm-rs_asm-v3/urdf/00-arm-rs_asm-v3.urdf')` in `Seeed-Projects__reBot-Isaacsim`. warning: lazy fetching disabled; some objects may not be available
fatal: could not fetch 8b17509603fd7332a63235a11c878a0b9c58bb65 from promisor remote

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/Seeed-Projects__reBot-Isaacsim -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `8b17509603fd7332a63235a11c878a0b9c58bb65`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('log', '--all', '--follow', '--find-renames=100%', '--format=@@@%H|%ct|%cI|%s', '--name-status', '--', 'urdf/00-arm-rs_asm-v3/urdf/00-arm-rs_asm-v3.urdf')` in `Seeed-Projects__reBot-Isaacsim`. warning: lazy fetching disabled; some objects may not be available
fatal: could not fetch 1179aaa835f3949b8a0738dbd9e02d7656bd59cd from promisor remote

- History coverage warning for https://github.com/Seeed-Projects/reBot-Isaacsim urdf/00-arm-rs_asm-v3/urdf/00-arm-rs_asm-v3.urdf: Exact-rename traversal required unavailable unrelated blobs; current-path history was inspected, older renamed paths remain unresolved

- Offline Git read failed (exit 128): `('show', 'a758567c3978dfeefe282ede0500085a48fe8f78:URDF/SO_5DOF_ARM100_8j_URDF.SLDASM/urdf/SO_5DOF_ARM100_8j_URDF.SLDASM.urdf')` in `TheRobotStudio__SO-ARM100`. fatal: path 'URDF/SO_5DOF_ARM100_8j_URDF.SLDASM/urdf/SO_5DOF_ARM100_8j_URDF.SLDASM.urdf' does not exist in 'a758567c3978dfeefe282ede0500085a48fe8f78'

- https://github.com/TheRobotStudio/SO-ARM100 URDF/SO_5DOF_ARM100_8j_URDF.SLDASM/urdf/SO_5DOF_ARM100_8j_URDF.SLDASM.urdf at a758567c3978dfeefe282ede0500085a48fe8f78: CalledProcessError: Command '['git', '-C', '.cache/TheRobotStudio__SO-ARM100', 'show', 'a758567c3978dfeefe282ede0500085a48fe8f78:URDF/SO_5DOF_ARM100_8j_URDF.SLDASM/urdf/SO_5DOF_ARM100_8j_URDF.SLDASM.urdf']' returned non-zero exit status 128.

- https://github.com/unitreerobotics/unitree_ros robots/go2_description/xacro/leg.xacro at 157ff950351e5f535e03c5d85a16b7d594b3dbcc: ValueError: Macro leg requires unsupported explicit arguments: ['mirror', 'mirror_dae', 'front_hind', 'front_hind_dae']

- https://github.com/unitreerobotics/unitree_ros robots/go2_description/xacro/const.xacro at 157ff950351e5f535e03c5d85a16b7d594b3dbcc: ValueError: XML has no robot bodies; it is an include/extension fragment, not a standalone source

- https://github.com/unitreerobotics/unitree_ros robots/go2_description/xacro/robot.xacro at 157ff950351e5f535e03c5d85a16b7d594b3dbcc: ValueError: Resource missing at 157ff950351e5f535e03c5d85a16b7d594b3dbcc: robots/go2_description/xacro/robots/go2_description/meshes/trunk.dae

- https://github.com/unitreerobotics/unitree_ros robots/go2_description/xacro/gazebo.xacro at 157ff950351e5f535e03c5d85a16b7d594b3dbcc: ValueError: XML has no robot bodies; it is an include/extension fragment, not a standalone source

- https://github.com/unitreerobotics/unitree_ros robots/go2_description/xacro/materials.xacro at 157ff950351e5f535e03c5d85a16b7d594b3dbcc: ValueError: XML has no robot bodies; it is an include/extension fragment, not a standalone source

- https://github.com/unitreerobotics/unitree_ros robots/go2_description/xacro/transmission.xacro at 157ff950351e5f535e03c5d85a16b7d594b3dbcc: ValueError: XML has no robot bodies; it is an include/extension fragment, not a standalone source

- https://github.com/unitreerobotics/unitree_ros robots/go2_description/urdf/go2_description.urdf at 157ff950351e5f535e03c5d85a16b7d594b3dbcc: ValueError: XML Error: repeated element: 'material'
Element 'material', line 13


- Historical source compile failed realsense_d435i afef66f988c45cca14b4d8fd654c9c017c1b0ac1 realsense2_description/urdf/_d435i.urdf.xacro: XML has no robot bodies; it is an include/extension fragment, not a standalone source

- Historical source compile failed realsense_d435i c8a8afd14240f8adee1548771d9bca2e16bcb12b realsense2_description/urdf/_d435i.urdf.xacro: XML or text declaration not at start of entity: line 10, column 0

- Historical source compile failed realsense_d435i c81130c7d9b2141b4130f9ebebf4f02a1a184f7c realsense2_description/urdf/_d435i.urdf.xacro: XML or text declaration not at start of entity: line 10, column 0

- Offline Git read failed (exit 128): `('log', '--all', '--follow', '--find-renames=100%', '--format=@@@%H|%ct|%cI|%s', '--name-status', '--', 'ur_description/urdf/ur10e.xacro')` in `ros-industrial__universal_robot`. warning: lazy fetching disabled; some objects may not be available
fatal: could not fetch 701a9f0f17d584f8d5c6c1e0cfe1a63c4ce94b61 from promisor remote

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/ros-industrial__universal_robot -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `701a9f0f17d584f8d5c6c1e0cfe1a63c4ce94b61`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('log', '--all', '--follow', '--find-renames=100%', '--format=@@@%H|%ct|%cI|%s', '--name-status', '--', 'ur_description/urdf/ur10e.xacro')` in `ros-industrial__universal_robot`. warning: lazy fetching disabled; some objects may not be available
fatal: could not fetch d70067a265c37aa5878cd1f1aa0459e03c7ed39e from promisor remote

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/ros-industrial__universal_robot -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `d70067a265c37aa5878cd1f1aa0459e03c7ed39e`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('log', '--all', '--follow', '--find-renames=100%', '--format=@@@%H|%ct|%cI|%s', '--name-status', '--', 'ur_description/urdf/ur10e.xacro')` in `ros-industrial__universal_robot`. warning: lazy fetching disabled; some objects may not be available
fatal: could not fetch 22567d65995d29e87e9a5b018ba5d4e5f8fa76fd from promisor remote

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/ros-industrial__universal_robot -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `22567d65995d29e87e9a5b018ba5d4e5f8fa76fd`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('log', '--all', '--follow', '--find-renames=100%', '--format=@@@%H|%ct|%cI|%s', '--name-status', '--', 'ur_description/urdf/ur10e.xacro')` in `ros-industrial__universal_robot`. warning: lazy fetching disabled; some objects may not be available
fatal: could not fetch 010ff9638cde4cbbb233dec584679293e023dedf from promisor remote

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/ros-industrial__universal_robot -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `010ff9638cde4cbbb233dec584679293e023dedf`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('log', '--all', '--follow', '--find-renames=100%', '--format=@@@%H|%ct|%cI|%s', '--name-status', '--', 'ur_description/urdf/ur10e.xacro')` in `ros-industrial__universal_robot`. warning: lazy fetching disabled; some objects may not be available
fatal: could not fetch 4c454f12ff08e53441104ccc47a6f78b60df7bac from promisor remote

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/ros-industrial__universal_robot -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `4c454f12ff08e53441104ccc47a6f78b60df7bac`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('log', '--all', '--follow', '--find-renames=100%', '--format=@@@%H|%ct|%cI|%s', '--name-status', '--', 'ur_description/urdf/ur10e.xacro')` in `ros-industrial__universal_robot`. warning: lazy fetching disabled; some objects may not be available
fatal: could not fetch a6e38438715189913696ac6af4c4de780e2dca3a from promisor remote

- History coverage warning for https://github.com/ros-industrial/universal_robot ur_description/urdf/ur10e.xacro: Exact-rename traversal required unavailable unrelated blobs; current-path history was inspected, older renamed paths remain unresolved

- Offline Git read failed (exit 128): `('log', '--all', '--follow', '--find-renames=100%', '--format=@@@%H|%ct|%cI|%s', '--name-status', '--', 'ur_description/urdf/ur5e.xacro')` in `ros-industrial__universal_robot`. warning: lazy fetching disabled; some objects may not be available
fatal: could not fetch a6e38438715189913696ac6af4c4de780e2dca3a from promisor remote

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/ros-industrial__universal_robot -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `a6e38438715189913696ac6af4c4de780e2dca3a`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('log', '--all', '--follow', '--find-renames=100%', '--format=@@@%H|%ct|%cI|%s', '--name-status', '--', 'ur_description/urdf/ur5e.xacro')` in `ros-industrial__universal_robot`. warning: lazy fetching disabled; some objects may not be available
fatal: could not fetch d567e95e0b050dc677960000901df9a9abc3e47e from promisor remote

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/ros-industrial__universal_robot -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `d567e95e0b050dc677960000901df9a9abc3e47e`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('log', '--all', '--follow', '--find-renames=100%', '--format=@@@%H|%ct|%cI|%s', '--name-status', '--', 'ur_description/urdf/ur5e.xacro')` in `ros-industrial__universal_robot`. warning: lazy fetching disabled; some objects may not be available
fatal: could not fetch d50686d07d108a52a4dbdfe48203e2fc46f7b518 from promisor remote

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/ros-industrial__universal_robot -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `d50686d07d108a52a4dbdfe48203e2fc46f7b518`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('log', '--all', '--follow', '--find-renames=100%', '--format=@@@%H|%ct|%cI|%s', '--name-status', '--', 'ur_description/urdf/ur5e.xacro')` in `ros-industrial__universal_robot`. warning: lazy fetching disabled; some objects may not be available
fatal: could not fetch fbe420c8c0de21079378a9d0a3f260ca15bc0c08 from promisor remote

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/ros-industrial__universal_robot -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `fbe420c8c0de21079378a9d0a3f260ca15bc0c08`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('log', '--all', '--follow', '--find-renames=100%', '--format=@@@%H|%ct|%cI|%s', '--name-status', '--', 'ur_description/urdf/ur5e.xacro')` in `ros-industrial__universal_robot`. warning: lazy fetching disabled; some objects may not be available
fatal: could not fetch d0429681d4b3bb28c2df0cfc05c53f900e336a3c from promisor remote

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/ros-industrial__universal_robot -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `d0429681d4b3bb28c2df0cfc05c53f900e336a3c`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('log', '--all', '--follow', '--find-renames=100%', '--format=@@@%H|%ct|%cI|%s', '--name-status', '--', 'ur_description/urdf/ur5e.xacro')` in `ros-industrial__universal_robot`. warning: lazy fetching disabled; some objects may not be available
fatal: could not fetch a6a41cf132c01f27239255594fef845f67bafc61 from promisor remote

- History coverage warning for https://github.com/ros-industrial/universal_robot ur_description/urdf/ur5e.xacro: Exact-rename traversal required unavailable unrelated blobs; current-path history was inspected, older renamed paths remain unresolved

- Rejected unrelated historical README template for agilex_piper: 0bee963312f0f4a25b53cdf9afe744ca73f2d68a heading '## UMI-Gripper Description (MJCF)'

- Offline Git read failed (exit 128): `('show', '400b5f5b9fec382583f69b53b094a154d9dc7635:agilex_piper/CHANGELOG.md')` in `menagerie`. fatal: path 'agilex_piper/CHANGELOG.md' does not exist in '400b5f5b9fec382583f69b53b094a154d9dc7635'

- Rejected conflicting robot-variant link for anybotics_anymal_c: https://github.com/ANYbotics/anymal_b_simple_description/blob/master/urdf/anymal.urdf (repository variant b, model variant c)

- Offline Git read failed (exit 128): `('show', 'd9415a3076f921fdb9735d45d609a596df722468:apptronik_apollo/CHANGELOG.md')` in `menagerie`. fatal: bad object d9415a3076f921fdb9735d45d609a596df722468:apptronik_apollo/CHANGELOG.md

- Offline Git read failed (exit 128): `('show', '400b5f5b9fec382583f69b53b094a154d9dc7635:arx_l5/CHANGELOG.md')` in `menagerie`. fatal: path 'arx_l5/CHANGELOG.md' does not exist in '400b5f5b9fec382583f69b53b094a154d9dc7635'

- Offline Git read failed (exit 128): `('show', 'd9415a3076f921fdb9735d45d609a596df722468:berkeley_humanoid/CHANGELOG.md')` in `menagerie`. fatal: bad object d9415a3076f921fdb9735d45d609a596df722468:berkeley_humanoid/CHANGELOG.md

- Rejected conflicting robot-variant link for bitcraze_crazyflie_2: https://github.com/whoenig/crazyflie_ros (repository variant ros, model variant 2)

- Offline Git read failed (exit 128): `('show', 'd9415a3076f921fdb9735d45d609a596df722468:booster_t1/CHANGELOG.md')` in `menagerie`. fatal: bad object d9415a3076f921fdb9735d45d609a596df722468:booster_t1/CHANGELOG.md

- Offline Git read failed (exit 128): `('show', 'd9415a3076f921fdb9735d45d609a596df722468:fourier_n1/CHANGELOG.md')` in `menagerie`. fatal: bad object d9415a3076f921fdb9735d45d609a596df722468:fourier_n1/CHANGELOG.md

- Offline Git read failed (exit 128): `('show', '400b5f5b9fec382583f69b53b094a154d9dc7635:fourier_n1/CHANGELOG.md')` in `menagerie`. fatal: path 'fourier_n1/CHANGELOG.md' does not exist in '400b5f5b9fec382583f69b53b094a154d9dc7635'

- Offline Git read failed (exit 128): `('show', 'db140ade7ee4cb59629f9687aafc65af663d5bbe:franka_fr3_v2/README.md')` in `menagerie`. fatal: path 'franka_fr3_v2/README.md' does not exist in 'db140ade7ee4cb59629f9687aafc65af663d5bbe'

- Offline Git read failed (exit 128): `('show', 'cd7fc51b704c3cba05748bd5537cb17990b341eb:franka_fr3_v2/README.md')` in `menagerie`. fatal: path 'franka_fr3_v2/README.md' does not exist in 'cd7fc51b704c3cba05748bd5537cb17990b341eb'

- Offline Git read failed (exit 128): `('show', '400b5f5b9fec382583f69b53b094a154d9dc7635:franka_fr3_v2/README.md')` in `menagerie`. fatal: path 'franka_fr3_v2/README.md' does not exist in '400b5f5b9fec382583f69b53b094a154d9dc7635'

- Offline Git read failed (exit 128): `('show', 'acbbf1636fcfef9b437a6eb8c6f84380fb4aa998:franka_fr3_v2/README.md')` in `menagerie`. fatal: path 'franka_fr3_v2/README.md' does not exist in 'acbbf1636fcfef9b437a6eb8c6f84380fb4aa998'

- Offline Git read failed (exit 128): `('show', '7876dcdef0d912387441616526ed236142f047d3:franka_fr3_v2/README.md')` in `menagerie`. fatal: path 'franka_fr3_v2/README.md' does not exist in '7876dcdef0d912387441616526ed236142f047d3'

- Offline Git read failed (exit 128): `('show', 'b5ebfe0cf079d2b96acf0a5c0e29ee0c95ba32f4:google_robot/README.md')` in `menagerie`. fatal: path 'google_robot/README.md' does not exist in 'b5ebfe0cf079d2b96acf0a5c0e29ee0c95ba32f4'

- Offline Git read failed (exit 128): `('show', '5ce04bea98bbfca277a8d50b55ba3c7c4a62bdec:i2rt_yam/CHANGELOG.md')` in `menagerie`. fatal: path 'i2rt_yam/CHANGELOG.md' does not exist in '5ce04bea98bbfca277a8d50b55ba3c7c4a62bdec'

- Offline Git read failed (exit 128): `('show', 'a88bc450470d97ebc1f282e5969675fb4d1f0ed7:low_cost_robot_arm/README.md')` in `menagerie`. fatal: path 'low_cost_robot_arm/README.md' does not exist in 'a88bc450470d97ebc1f282e5969675fb4d1f0ed7'

- Offline Git read failed (exit 128): `('show', 'd74280a600a9afdfcb98d8917d0c79c86539aa61:low_cost_robot_arm/README.md')` in `menagerie`. fatal: path 'low_cost_robot_arm/README.md' does not exist in 'd74280a600a9afdfcb98d8917d0c79c86539aa61'

- Offline Git read failed (exit 128): `('show', '13d6c48b8f59d2c4badee7756b4ea3532613cddf:low_cost_robot_arm/README.md')` in `menagerie`. fatal: path 'low_cost_robot_arm/README.md' does not exist in '13d6c48b8f59d2c4badee7756b4ea3532613cddf'

- Offline Git read failed (exit 128): `('show', 'fae9ee82330444eec4e87568c838b99a09a39467:rainbow_robotics_rby1/README.md')` in `menagerie`. fatal: path 'rainbow_robotics_rby1/README.md' does not exist in 'fae9ee82330444eec4e87568c838b99a09a39467'

- Offline Git read failed (exit 128): `('show', '04674c8d0a4e12e33980a9e47fb604adc281fcc8:robotstudio_so101/CHANGELOG.md')` in `menagerie`. fatal: path 'robotstudio_so101/CHANGELOG.md' does not exist in '04674c8d0a4e12e33980a9e47fb604adc281fcc8'

- Offline Git read failed (exit 128): `('show', '5ce04bea98bbfca277a8d50b55ba3c7c4a62bdec:robotstudio_so101/CHANGELOG.md')` in `menagerie`. fatal: path 'robotstudio_so101/CHANGELOG.md' does not exist in '5ce04bea98bbfca277a8d50b55ba3c7c4a62bdec'

- Offline Git read failed (exit 128): `('show', '4a7015530bd7a4161103ae8f0905a96481e4cc1a:robotstudio_so101/CHANGELOG.md')` in `menagerie`. fatal: path 'robotstudio_so101/CHANGELOG.md' does not exist in '4a7015530bd7a4161103ae8f0905a96481e4cc1a'

- Offline Git read failed (exit 128): `('show', 'bf110a75a56e5bd146c7ed76965737c71d48425d:shadow_dexee/README.md')` in `menagerie`. fatal: path 'shadow_dexee/README.md' does not exist in 'bf110a75a56e5bd146c7ed76965737c71d48425d'

- Offline Git read failed (exit 128): `('show', '04674c8d0a4e12e33980a9e47fb604adc281fcc8:tetheria_aero_hand_open/CHANGELOG.md')` in `menagerie`. fatal: path 'tetheria_aero_hand_open/CHANGELOG.md' does not exist in '04674c8d0a4e12e33980a9e47fb604adc281fcc8'

- Offline Git read failed (exit 128): `('show', '400b5f5b9fec382583f69b53b094a154d9dc7635:tetheria_aero_hand_open/CHANGELOG.md')` in `menagerie`. fatal: path 'tetheria_aero_hand_open/CHANGELOG.md' does not exist in '400b5f5b9fec382583f69b53b094a154d9dc7635'

- Offline Git read failed (exit 128): `('show', '04674c8d0a4e12e33980a9e47fb604adc281fcc8:toddlerbot_2xc/CHANGELOG.md')` in `menagerie`. fatal: path 'toddlerbot_2xc/CHANGELOG.md' does not exist in '04674c8d0a4e12e33980a9e47fb604adc281fcc8'

- Offline Git read failed (exit 128): `('show', '9e7f8d4dda07f5c281b6c0c6f0d07b9dd267b762:toddlerbot_2xc/CHANGELOG.md')` in `menagerie`. fatal: path 'toddlerbot_2xc/CHANGELOG.md' does not exist in '9e7f8d4dda07f5c281b6c0c6f0d07b9dd267b762'

- Offline Git read failed (exit 128): `('show', '400b5f5b9fec382583f69b53b094a154d9dc7635:toddlerbot_2xc/CHANGELOG.md')` in `menagerie`. fatal: path 'toddlerbot_2xc/CHANGELOG.md' does not exist in '400b5f5b9fec382583f69b53b094a154d9dc7635'

- Offline Git read failed (exit 128): `('show', '04674c8d0a4e12e33980a9e47fb604adc281fcc8:toddlerbot_2xm/CHANGELOG.md')` in `menagerie`. fatal: path 'toddlerbot_2xm/CHANGELOG.md' does not exist in '04674c8d0a4e12e33980a9e47fb604adc281fcc8'

- Offline Git read failed (exit 128): `('show', '9e7f8d4dda07f5c281b6c0c6f0d07b9dd267b762:toddlerbot_2xm/CHANGELOG.md')` in `menagerie`. fatal: path 'toddlerbot_2xm/CHANGELOG.md' does not exist in '9e7f8d4dda07f5c281b6c0c6f0d07b9dd267b762'

- Offline Git read failed (exit 128): `('show', '400b5f5b9fec382583f69b53b094a154d9dc7635:toddlerbot_2xm/CHANGELOG.md')` in `menagerie`. fatal: path 'toddlerbot_2xm/CHANGELOG.md' does not exist in '400b5f5b9fec382583f69b53b094a154d9dc7635'

- Offline Git read failed (exit 128): `('show', '400b5f5b9fec382583f69b53b094a154d9dc7635:trossen_wxai/README.md')` in `menagerie`. fatal: path 'trossen_wxai/README.md' does not exist in '400b5f5b9fec382583f69b53b094a154d9dc7635'

- Offline Git read failed (exit 128): `('show', '477ec56566682d663b996d86a188c75499e74b98:trossen_wxai/README.md')` in `menagerie`. fatal: path 'trossen_wxai/README.md' does not exist in '477ec56566682d663b996d86a188c75499e74b98'

- Offline Git read failed (exit 128): `('show', 'd9415a3076f921fdb9735d45d609a596df722468:unitree_g1/CHANGELOG.md')` in `menagerie`. fatal: bad object d9415a3076f921fdb9735d45d609a596df722468:unitree_g1/CHANGELOG.md

- https://github.com/unitreerobotics/unitree_ros robots/go2_description/xacro/leg.xacro at 157ff950351e5f535e03c5d85a16b7d594b3dbcc: ValueError: Macro leg requires unsupported explicit arguments: ['mirror', 'mirror_dae', 'front_hind', 'front_hind_dae']

- https://github.com/unitreerobotics/unitree_ros robots/go2_description/xacro/const.xacro at 157ff950351e5f535e03c5d85a16b7d594b3dbcc: ValueError: XML has no robot bodies; it is an include/extension fragment, not a standalone source

- https://github.com/unitreerobotics/unitree_ros robots/go2_description/xacro/robot.xacro at 157ff950351e5f535e03c5d85a16b7d594b3dbcc: ValueError: Resource missing at 157ff950351e5f535e03c5d85a16b7d594b3dbcc: robots/go2_description/xacro/robots/go2_description/meshes/trunk.dae

- https://github.com/unitreerobotics/unitree_ros robots/go2_description/xacro/gazebo.xacro at 157ff950351e5f535e03c5d85a16b7d594b3dbcc: ValueError: XML has no robot bodies; it is an include/extension fragment, not a standalone source

- https://github.com/unitreerobotics/unitree_ros robots/go2_description/xacro/materials.xacro at 157ff950351e5f535e03c5d85a16b7d594b3dbcc: ValueError: XML has no robot bodies; it is an include/extension fragment, not a standalone source

- https://github.com/unitreerobotics/unitree_ros robots/go2_description/xacro/transmission.xacro at 157ff950351e5f535e03c5d85a16b7d594b3dbcc: ValueError: XML has no robot bodies; it is an include/extension fragment, not a standalone source

- Offline Git read failed (exit 128): `('show', 'ac736c92b02de7ca7e0be6f737d77d46707464d8:xarm_description/meshes/lite6/visual/link_base.stl')` in `xArm-Developer__xarm_ros2`. fatal: bad object ac736c92b02de7ca7e0be6f737d77d46707464d8:xarm_description/meshes/lite6/visual/link_base.stl

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/xArm-Developer__xarm_ros2 -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `56cf92dbee47b65c03e767cad4043b5f18593c9e`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'ac736c92b02de7ca7e0be6f737d77d46707464d8:xarm_description/meshes/lite6/visual/link1.stl')` in `xArm-Developer__xarm_ros2`. fatal: bad object ac736c92b02de7ca7e0be6f737d77d46707464d8:xarm_description/meshes/lite6/visual/link1.stl

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/xArm-Developer__xarm_ros2 -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `c846dbb08d0996823522313a62e8a4b113df388d`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'ac736c92b02de7ca7e0be6f737d77d46707464d8:xarm_description/meshes/lite6/visual/link2.stl')` in `xArm-Developer__xarm_ros2`. fatal: bad object ac736c92b02de7ca7e0be6f737d77d46707464d8:xarm_description/meshes/lite6/visual/link2.stl

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/xArm-Developer__xarm_ros2 -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `d1b1f83135d99cc6612a27b2c0b19833f1dcacfb`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'ac736c92b02de7ca7e0be6f737d77d46707464d8:xarm_description/meshes/lite6/visual/link3.stl')` in `xArm-Developer__xarm_ros2`. fatal: bad object ac736c92b02de7ca7e0be6f737d77d46707464d8:xarm_description/meshes/lite6/visual/link3.stl

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/xArm-Developer__xarm_ros2 -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `e2833e791ef10beaa533b34c0f6266600a8cf79e`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'ac736c92b02de7ca7e0be6f737d77d46707464d8:xarm_description/meshes/lite6/visual/link4.stl')` in `xArm-Developer__xarm_ros2`. fatal: bad object ac736c92b02de7ca7e0be6f737d77d46707464d8:xarm_description/meshes/lite6/visual/link4.stl

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/xArm-Developer__xarm_ros2 -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `8eec2c438dfe9a9b3476cdcf1e9b447b8b9da3c2`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'ac736c92b02de7ca7e0be6f737d77d46707464d8:xarm_description/meshes/lite6/collision/link4.stl')` in `xArm-Developer__xarm_ros2`. fatal: bad object ac736c92b02de7ca7e0be6f737d77d46707464d8:xarm_description/meshes/lite6/collision/link4.stl

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/xArm-Developer__xarm_ros2 -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `9a93c31810d3c89a2eb7766fc0f56bf2cedd3091`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'ac736c92b02de7ca7e0be6f737d77d46707464d8:xarm_description/meshes/lite6/visual/link5.stl')` in `xArm-Developer__xarm_ros2`. fatal: bad object ac736c92b02de7ca7e0be6f737d77d46707464d8:xarm_description/meshes/lite6/visual/link5.stl

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/xArm-Developer__xarm_ros2 -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `2c465633381d683f7e31852b4f8ee5fcbfc7ae02`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'ac736c92b02de7ca7e0be6f737d77d46707464d8:xarm_description/meshes/lite6/collision/link5.stl')` in `xArm-Developer__xarm_ros2`. fatal: bad object ac736c92b02de7ca7e0be6f737d77d46707464d8:xarm_description/meshes/lite6/collision/link5.stl

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/xArm-Developer__xarm_ros2 -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `ef7c2dba3153967b6f6301c113b1609d24e1167d`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'ac736c92b02de7ca7e0be6f737d77d46707464d8:xarm_description/meshes/lite6/visual/link6.stl')` in `xArm-Developer__xarm_ros2`. fatal: bad object ac736c92b02de7ca7e0be6f737d77d46707464d8:xarm_description/meshes/lite6/visual/link6.stl

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/xArm-Developer__xarm_ros2 -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `60a915e2f4f35c15480a898c64f70dfc3056d059`

- Network outcome: exit 0.

- https://github.com/xArm-Developer/xarm_ros2 xarm_description/urdf/lite6/lite6.urdf.xacro at ac736c92b02de7ca7e0be6f737d77d46707464d8: XacroException: name 'use_xacro_load_yaml' is not defined
when evaluating expression 'use_xacro_load_yaml'

- https://github.com/xArm-Developer/xarm_ros2 xarm_description/urdf/lite6/lite6.gazebo.xacro at ac736c92b02de7ca7e0be6f737d77d46707464d8: ValueError: XML has no robot bodies; it is an include/extension fragment, not a standalone source

- https://github.com/xArm-Developer/xarm_ros2 xarm_description/urdf/lite6/lite6.ros2_control.xacro at ac736c92b02de7ca7e0be6f737d77d46707464d8: ValueError: XML has no robot bodies; it is an include/extension fragment, not a standalone source

- https://github.com/xArm-Developer/xarm_ros2 xarm_description/urdf/lite6/lite6.transmission.xacro at ac736c92b02de7ca7e0be6f737d77d46707464d8: ValueError: XML has no robot bodies; it is an include/extension fragment, not a standalone source

- https://github.com/xArm-Developer/xarm_ros2 xarm_description/urdf/lite6/lite6_robot_macro.xacro at ac736c92b02de7ca7e0be6f737d77d46707464d8: XacroException: name 'is_ros2' is not defined
when evaluating expression 'is_ros2'

- Historical source compile failed ufactory_lite6 e82e45df62a6b9b290df35fe97c8ef980f3dead6 xarm_description/urdf/xarm_device.urdf.xacro: Resource missing at e82e45df62a6b9b290df35fe97c8ef980f3dead6: ../../../xarm_description/meshes/lite6/visual/base.stl

- Historical source compile failed ufactory_lite6 43f3be4da51d6cc81901f9833cc7d420822e6cea xarm_description/urdf/xarm_device.urdf.xacro: Resource missing at 43f3be4da51d6cc81901f9833cc7d420822e6cea: ../../../xarm_description/meshes/lite6/visual/base.stl

- Historical source compile failed ufactory_lite6 72d9e0b5db59433866b71fbc9dcad97dcc4d0993 xarm_description/urdf/xarm_device.urdf.xacro: Resource missing at 72d9e0b5db59433866b71fbc9dcad97dcc4d0993: ../../../xarm_description/meshes/lite6/visual/base.stl

- Historical source compile failed ufactory_lite6 3c153bbb8841d491f8a65434eb2fc5ce0da7b6c7 xarm_description/urdf/xarm_device.urdf.xacro: Resource missing at 3c153bbb8841d491f8a65434eb2fc5ce0da7b6c7: ../../../xarm_description/meshes/lite6/visual/base.stl

- Historical source compile failed ufactory_lite6 5b4bc59ba8e8aa1a4e7c78543fc8f4d3cb3b53ab xarm_description/urdf/xarm_device.urdf.xacro: Resource missing at 5b4bc59ba8e8aa1a4e7c78543fc8f4d3cb3b53ab: ../../../xarm_description/meshes/lite6/visual/base.stl

- Historical source compile failed ufactory_lite6 31743052d1f8533850da79abb1e3f81515b28764 xarm_description/urdf/xarm_device.urdf.xacro: Resource missing at 31743052d1f8533850da79abb1e3f81515b28764: ../../../xarm_description/meshes/lite6/visual/base.stl

- Historical source compile failed ufactory_lite6 7d3918e4590322a850d2f29564269f5ce6708f8a xarm_description/urdf/xarm_device.urdf.xacro: Resource missing at 7d3918e4590322a850d2f29564269f5ce6708f8a: ../../../xarm_description/meshes/lite6/visual/base.stl

- Historical source compile failed ufactory_lite6 27874699082c12ee4a390bf3b57108a7c5b3f468 xarm_description/urdf/xarm_device.urdf.xacro: Resource missing at 27874699082c12ee4a390bf3b57108a7c5b3f468: ../../../xarm_description/meshes/lite6/visual/base.stl

- Historical source compile failed ufactory_lite6 175000bcfa9259f1177ac0b669b41f5202b065a3 xarm_description/urdf/xarm_device.urdf.xacro: Resource missing at 175000bcfa9259f1177ac0b669b41f5202b065a3: ../../../xarm_description/meshes/lite6/visual/base.stl

- Historical source compile failed ufactory_lite6 e5a1e3feb2334e6f4d5ee1d5c99ace0e00b5b0bb xarm_description/urdf/xarm_device.urdf.xacro: Resource missing at e5a1e3feb2334e6f4d5ee1d5c99ace0e00b5b0bb: ../../../xarm_description/meshes/lite6/visual/base.stl

- Historical source compile failed ufactory_lite6 f0ad415d615f658ba747fc533757e2c923d294c8 xarm_description/urdf/xarm_device.urdf.xacro: Resource missing at f0ad415d615f658ba747fc533757e2c923d294c8: ../../../xarm_description/meshes/lite6/visual/base.stl

- Historical source compile failed ufactory_lite6 7a2ba61a7090d155e68d5f0ba8bb2bb8c55bb746 xarm_description/urdf/xarm_device.urdf.xacro: Resource missing at 7a2ba61a7090d155e68d5f0ba8bb2bb8c55bb746: ../../../xarm_description/meshes/lite6/visual/base.stl

- Historical source compile failed ufactory_lite6 32cf9ff739ad0b4794e76bcb0df7d1d7b712bb8f xarm_description/urdf/xarm_device.urdf.xacro: Resource missing at 32cf9ff739ad0b4794e76bcb0df7d1d7b712bb8f: ../../../xarm_description/meshes/xarm6/visual/base.stl

- Historical source compile failed ufactory_lite6 eb02b6cfffd318ab049ce695e37941b8ddf8cd99 xarm_description/urdf/xarm_device.urdf.xacro: Resource missing at eb02b6cfffd318ab049ce695e37941b8ddf8cd99: ../../../xarm_description/meshes/xarm6/visual/base.stl

- Offline Git read failed (exit 128): `('show', '02bf5f1bb07a3dad8f477b5ddc0ba03c582f5168:xarm_description/meshes/xarm6/visual/base.stl')` in `xArm-Developer__xarm_ros2`. fatal: bad object 02bf5f1bb07a3dad8f477b5ddc0ba03c582f5168:xarm_description/meshes/xarm6/visual/base.stl

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/xArm-Developer__xarm_ros2 -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `1b2c31cbed1dca3861a02fa44e6c199d8124b5f0`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '02bf5f1bb07a3dad8f477b5ddc0ba03c582f5168:xarm_description/meshes/xarm6/visual/link1.stl')` in `xArm-Developer__xarm_ros2`. fatal: bad object 02bf5f1bb07a3dad8f477b5ddc0ba03c582f5168:xarm_description/meshes/xarm6/visual/link1.stl

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/xArm-Developer__xarm_ros2 -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `431d81a4e492a630a6621ac86ed731a46a8f9372`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '02bf5f1bb07a3dad8f477b5ddc0ba03c582f5168:xarm_description/meshes/xarm6/visual/link2.stl')` in `xArm-Developer__xarm_ros2`. fatal: bad object 02bf5f1bb07a3dad8f477b5ddc0ba03c582f5168:xarm_description/meshes/xarm6/visual/link2.stl

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/xArm-Developer__xarm_ros2 -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `f040cfd6c925f47f5cbfdf604a52b168e303172e`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '02bf5f1bb07a3dad8f477b5ddc0ba03c582f5168:xarm_description/meshes/xarm6/visual/link3.stl')` in `xArm-Developer__xarm_ros2`. fatal: bad object 02bf5f1bb07a3dad8f477b5ddc0ba03c582f5168:xarm_description/meshes/xarm6/visual/link3.stl

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/xArm-Developer__xarm_ros2 -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `1e53f1023cf6e3e65079a261e4adf4d075de1b21`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '02bf5f1bb07a3dad8f477b5ddc0ba03c582f5168:xarm_description/meshes/xarm6/visual/link4.stl')` in `xArm-Developer__xarm_ros2`. fatal: bad object 02bf5f1bb07a3dad8f477b5ddc0ba03c582f5168:xarm_description/meshes/xarm6/visual/link4.stl

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/xArm-Developer__xarm_ros2 -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `a1e60179e8dcb9aaafb268ca7b5bbecad9c03718`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '02bf5f1bb07a3dad8f477b5ddc0ba03c582f5168:xarm_description/meshes/xarm6/visual/link5.stl')` in `xArm-Developer__xarm_ros2`. fatal: bad object 02bf5f1bb07a3dad8f477b5ddc0ba03c582f5168:xarm_description/meshes/xarm6/visual/link5.stl

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/xArm-Developer__xarm_ros2 -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `510b4100d389b26b591b180f04e3180debc3294e`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '02bf5f1bb07a3dad8f477b5ddc0ba03c582f5168:xarm_description/meshes/xarm6/visual/link6.stl')` in `xArm-Developer__xarm_ros2`. fatal: bad object 02bf5f1bb07a3dad8f477b5ddc0ba03c582f5168:xarm_description/meshes/xarm6/visual/link6.stl

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/xArm-Developer__xarm_ros2 -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `80f0fdc0e6815b798e5393c5151fb3a80e673ae2`

- Network outcome: exit 0.

- Historical source compile failed ufactory_lite6 02bf5f1bb07a3dad8f477b5ddc0ba03c582f5168 xarm_description/urdf/xarm_device.urdf.xacro: Error: inertia must satisfy A + B >= C; use 'balanceinertia' to fix
Element name 'link2', id 3

- Historical source compile failed ufactory_lite6 d17f59ebd0c9a9c6afd0bf61ee843d6e3b12ce61 xarm_description/urdf/xarm_device.urdf.xacro: Error: inertia must satisfy A + B >= C; use 'balanceinertia' to fix
Element name 'link2', id 3

- Historical source compile failed ufactory_lite6 bcceb1a87b32341dd4e11d8f8735835c9fc1c6f8 xarm_description/urdf/xarm_device.urdf.xacro: Error: inertia must satisfy A + B >= C; use 'balanceinertia' to fix
Element name 'link2', id 3

- Historical source compile failed ufactory_lite6 08ca7e445fdee4ddd5828f76e66a3b965d1e8c9b xarm_description/urdf/xarm_device.urdf.xacro: Error: inertia must satisfy A + B >= C; use 'balanceinertia' to fix
Element name 'link2', id 3

- Historical source compile failed ufactory_lite6 27be56de2e00e36d8e6db5a6b55a37d91ed894b8 xarm_description/urdf/xarm_device.urdf.xacro: Error: inertia must satisfy A + B >= C; use 'balanceinertia' to fix
Element name 'link2', id 3

- Offline Git read failed (exit 128): `('show', 'cf51617d98bc55a88d9aa735acfa43a0bbb8e425:xarm_description/meshes/xarm7/visual/link_base.stl')` in `xArm-Developer__xarm_ros`. fatal: bad object cf51617d98bc55a88d9aa735acfa43a0bbb8e425:xarm_description/meshes/xarm7/visual/link_base.stl

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/xArm-Developer__xarm_ros -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `555d6f2ea304faf0a97de76e0dc47a34d4acbe94`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'cf51617d98bc55a88d9aa735acfa43a0bbb8e425:xarm_description/meshes/xarm7/visual/link1.stl')` in `xArm-Developer__xarm_ros`. fatal: bad object cf51617d98bc55a88d9aa735acfa43a0bbb8e425:xarm_description/meshes/xarm7/visual/link1.stl

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/xArm-Developer__xarm_ros -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `a5ca309d62ecfdcaba798f1ea20533b1111cf7d7`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'cf51617d98bc55a88d9aa735acfa43a0bbb8e425:xarm_description/meshes/xarm7/visual/link2.stl')` in `xArm-Developer__xarm_ros`. fatal: bad object cf51617d98bc55a88d9aa735acfa43a0bbb8e425:xarm_description/meshes/xarm7/visual/link2.stl

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/xArm-Developer__xarm_ros -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `1539adb628e97b42bf6ba3598aa97c4217e7085c`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'cf51617d98bc55a88d9aa735acfa43a0bbb8e425:xarm_description/meshes/xarm7/visual/link3.stl')` in `xArm-Developer__xarm_ros`. fatal: bad object cf51617d98bc55a88d9aa735acfa43a0bbb8e425:xarm_description/meshes/xarm7/visual/link3.stl

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/xArm-Developer__xarm_ros -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `23926351ee6b7514c8c8f199ce3f94f18a2b4f40`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'cf51617d98bc55a88d9aa735acfa43a0bbb8e425:xarm_description/meshes/xarm7/visual/link4.stl')` in `xArm-Developer__xarm_ros`. fatal: bad object cf51617d98bc55a88d9aa735acfa43a0bbb8e425:xarm_description/meshes/xarm7/visual/link4.stl

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/xArm-Developer__xarm_ros -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `a24cc91df0608a9f83886d411584bb121d04f1c6`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'cf51617d98bc55a88d9aa735acfa43a0bbb8e425:xarm_description/meshes/xarm7/visual/link5.stl')` in `xArm-Developer__xarm_ros`. fatal: bad object cf51617d98bc55a88d9aa735acfa43a0bbb8e425:xarm_description/meshes/xarm7/visual/link5.stl

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/xArm-Developer__xarm_ros -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `7f91e37cfaa95173a63e35a7bc1d869ab3803c88`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'cf51617d98bc55a88d9aa735acfa43a0bbb8e425:xarm_description/meshes/xarm7/visual/link6.stl')` in `xArm-Developer__xarm_ros`. fatal: bad object cf51617d98bc55a88d9aa735acfa43a0bbb8e425:xarm_description/meshes/xarm7/visual/link6.stl

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/xArm-Developer__xarm_ros -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `04fc4805665c38e5f7a65b90adfe012200b41662`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'cf51617d98bc55a88d9aa735acfa43a0bbb8e425:xarm_description/meshes/xarm7/visual/link7.stl')` in `xArm-Developer__xarm_ros`. fatal: bad object cf51617d98bc55a88d9aa735acfa43a0bbb8e425:xarm_description/meshes/xarm7/visual/link7.stl

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/xArm-Developer__xarm_ros -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `0e9963c387d349ce36cb27f65fae6ebe72de6094`

- Network outcome: exit 0.

- https://github.com/xArm-Developer/xarm_ros xarm_description/urdf/xarm7/xarm7.urdf.xacro at cf51617d98bc55a88d9aa735acfa43a0bbb8e425: XacroException: name 'mesh_suffix' is not defined
when evaluating expression 'mesh_suffix == 'dae' or (model_num >= 1305 and model_num != 1380)'

- https://github.com/xArm-Developer/xarm_ros xarm_description/urdf/xarm7/xarm7.gazebo.xacro at cf51617d98bc55a88d9aa735acfa43a0bbb8e425: ValueError: XML has no robot bodies; it is an include/extension fragment, not a standalone source

- https://github.com/xArm-Developer/xarm_ros xarm_description/urdf/xarm7/xarm7.ros2_control.xacro at cf51617d98bc55a88d9aa735acfa43a0bbb8e425: ValueError: XML has no robot bodies; it is an include/extension fragment, not a standalone source

- https://github.com/xArm-Developer/xarm_ros xarm_description/urdf/xarm7/xarm7.transmission.xacro at cf51617d98bc55a88d9aa735acfa43a0bbb8e425: ValueError: XML has no robot bodies; it is an include/extension fragment, not a standalone source

- https://github.com/xArm-Developer/xarm_ros xarm_description/urdf/xarm7/xarm7_robot_macro.xacro at cf51617d98bc55a88d9aa735acfa43a0bbb8e425: XacroException: name 'is_ros2' is not defined
when evaluating expression 'is_ros2'

- Offline Git read failed (exit 128): `('log', '--all', '--follow', '--find-renames=100%', '--format=@@@%H|%ct|%cI|%s', '--name-status', '--', 'xarm_description/urdf/xarm_device.urdf.xacro')` in `xArm-Developer__xarm_ros`. warning: lazy fetching disabled; some objects may not be available
fatal: could not fetch 960e9cedc30891479b15b17e324a9b32fd2997b4 from promisor remote

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/xArm-Developer__xarm_ros -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `960e9cedc30891479b15b17e324a9b32fd2997b4`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('log', '--all', '--follow', '--find-renames=100%', '--format=@@@%H|%ct|%cI|%s', '--name-status', '--', 'xarm_description/urdf/xarm_device.urdf.xacro')` in `xArm-Developer__xarm_ros`. warning: lazy fetching disabled; some objects may not be available
fatal: could not fetch 7a3837015ac036f83e549897457351c238c79923 from promisor remote

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/xArm-Developer__xarm_ros -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `7a3837015ac036f83e549897457351c238c79923`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('log', '--all', '--follow', '--find-renames=100%', '--format=@@@%H|%ct|%cI|%s', '--name-status', '--', 'xarm_description/urdf/xarm_device.urdf.xacro')` in `xArm-Developer__xarm_ros`. warning: lazy fetching disabled; some objects may not be available
fatal: could not fetch ab552b0aecc61f624569d8bc7de5f71d01af1797 from promisor remote

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/xArm-Developer__xarm_ros -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `ab552b0aecc61f624569d8bc7de5f71d01af1797`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('log', '--all', '--follow', '--find-renames=100%', '--format=@@@%H|%ct|%cI|%s', '--name-status', '--', 'xarm_description/urdf/xarm_device.urdf.xacro')` in `xArm-Developer__xarm_ros`. warning: lazy fetching disabled; some objects may not be available
fatal: could not fetch 7c5608c52c87619a774b570255f96c1b1d710a5c from promisor remote

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/xArm-Developer__xarm_ros -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `7c5608c52c87619a774b570255f96c1b1d710a5c`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('log', '--all', '--follow', '--find-renames=100%', '--format=@@@%H|%ct|%cI|%s', '--name-status', '--', 'xarm_description/urdf/xarm_device.urdf.xacro')` in `xArm-Developer__xarm_ros`. warning: lazy fetching disabled; some objects may not be available
fatal: could not fetch dd128a0e3fec06c9d150ce3594d836fe10bbff2c from promisor remote

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/xArm-Developer__xarm_ros -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `dd128a0e3fec06c9d150ce3594d836fe10bbff2c`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('log', '--all', '--follow', '--find-renames=100%', '--format=@@@%H|%ct|%cI|%s', '--name-status', '--', 'xarm_description/urdf/xarm_device.urdf.xacro')` in `xArm-Developer__xarm_ros`. warning: lazy fetching disabled; some objects may not be available
fatal: could not fetch 352a95d3d9fc6c53fee3de2ebd06930f14246077 from promisor remote

- History coverage warning for https://github.com/xArm-Developer/xarm_ros xarm_description/urdf/xarm_device.urdf.xacro: Exact-rename traversal required unavailable unrelated blobs; current-path history was inspected, older renamed paths remain unresolved

- Historical source compile failed ufactory_xarm7 b9d492275b968d24317ca33a9f2579e1633acbbf xarm_description/urdf/xarm_device.urdf.xacro: Use of invalid name(s):  __len__
when evaluating expression 'robot_sn.__len__()'
when evaluating expression 'robot_sn_len >= 14 and (robot_sn[0] == 'X' or robot_sn[0] == 'L' or robot_sn[0] == 'F')'

- Historical source compile failed ufactory_xarm7 f8d572f768d990122dca304144f92bcf09a1f2ec xarm_description/urdf/xarm_device.urdf.xacro: Use of invalid name(s):  __len__
when evaluating expression 'robot_sn.__len__()'
when evaluating expression 'robot_sn_len >= 14 and (robot_sn[0] == 'X' or robot_sn[0] == 'L' or robot_sn[0] == 'F')'

- Historical source compile failed ufactory_xarm7 74e75cf87e6904d0876b869113d09a8bc9f6e176 xarm_description/urdf/xarm_device.urdf.xacro: Use of invalid name(s):  __len__
when evaluating expression 'robot_sn.__len__()'
when evaluating expression 'robot_sn_len >= 14 and (robot_sn[0] == 'X' or robot_sn[0] == 'L' or robot_sn[0] == 'F')'

- Historical source compile failed ufactory_xarm7 281d6c301092d93d3deac12b6b6b6dd86fb05df1 xarm_description/urdf/xarm_device.urdf.xacro: Use of invalid name(s):  __len__
when evaluating expression 'robot_sn.__len__()'
when evaluating expression 'robot_sn_len >= 14 and (robot_sn[0] == 'X' or robot_sn[0] == 'L' or robot_sn[0] == 'F')'

- Historical source compile failed ufactory_xarm7 75956706e0108c2abcb98ed91eb6403604844acf xarm_description/urdf/xarm_device.urdf.xacro: Use of invalid name(s):  __len__
when evaluating expression 'robot_sn.__len__()'
when evaluating expression 'robot_sn_len >= 14 and (robot_sn[0] == 'X' or robot_sn[0] == 'L')'

- Historical source compile failed ufactory_xarm7 9f263958f4df3223dd29f0c8176f9d8f48668ef5 xarm_description/urdf/xarm_device.urdf.xacro: Error: inertia must satisfy A + B >= C; use 'balanceinertia' to fix
Element name 'link4', id 5

- Historical source compile failed ufactory_xarm7 00fcc0833845f12afaa85c1bafba4ec327078ce1 xarm_description/urdf/xarm_device.urdf.xacro: Error: inertia must satisfy A + B >= C; use 'balanceinertia' to fix
Element name 'link4', id 5

- Historical source compile failed ufactory_xarm7 e027c47bf4d600f11f03bd2aa359d22bc8d9dfdd xarm_description/urdf/xarm_device.urdf.xacro: Use of invalid name(s):  __len__
when evaluating expression 'robot_sn.__len__()'
when evaluating expression 'robot_sn_len >= 14 and (robot_sn[0] == 'X' or robot_sn[0] == 'L')'

- Historical source compile failed ufactory_xarm7 91d6608a22d92f90202bfc6b81afc44f145d07be xarm_description/urdf/xarm_device.urdf.xacro: Error: inertia must satisfy A + B >= C; use 'balanceinertia' to fix
Element name 'link4', id 5

- Offline Git read failed (exit 128): `('show', '172c3d9c3715ee75eb10dfe4ee57e26a342b4529:sr_description/meshes/components/forearm/forearm_E3M5.dae')` in `shadow-robot__sr_common`. fatal: bad object 172c3d9c3715ee75eb10dfe4ee57e26a342b4529:sr_description/meshes/components/forearm/forearm_E3M5.dae

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/shadow-robot__sr_common -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `febe9374cbe2dbacbab69e5657f03a7412bd552d`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '172c3d9c3715ee75eb10dfe4ee57e26a342b4529:sr_description/meshes/components/wrist/wrist_E3M5.dae')` in `shadow-robot__sr_common`. fatal: bad object 172c3d9c3715ee75eb10dfe4ee57e26a342b4529:sr_description/meshes/components/wrist/wrist_E3M5.dae

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/shadow-robot__sr_common -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `5f1f221ec54c32f42fee41a1237b04cd06a95743`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '172c3d9c3715ee75eb10dfe4ee57e26a342b4529:sr_description/meshes/components/palm/palm_E3M5.dae')` in `shadow-robot__sr_common`. fatal: bad object 172c3d9c3715ee75eb10dfe4ee57e26a342b4529:sr_description/meshes/components/palm/palm_E3M5.dae

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/shadow-robot__sr_common -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `3a0b71055323f7598dd191d7fdc9461e2586c536`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '172c3d9c3715ee75eb10dfe4ee57e26a342b4529:sr_description/meshes/components/f_distal/pst/f_distal_pst.dae')` in `shadow-robot__sr_common`. fatal: bad object 172c3d9c3715ee75eb10dfe4ee57e26a342b4529:sr_description/meshes/components/f_distal/pst/f_distal_pst.dae

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/shadow-robot__sr_common -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `8bd625f2087f91b131cbf0304a9ffba56d341005`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '172c3d9c3715ee75eb10dfe4ee57e26a342b4529:sr_description/meshes/components/th_distal/pst/th_distal_pst.dae')` in `shadow-robot__sr_common`. fatal: bad object 172c3d9c3715ee75eb10dfe4ee57e26a342b4529:sr_description/meshes/components/th_distal/pst/th_distal_pst.dae

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/shadow-robot__sr_common -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `f1ed0b6ea79d88002c0ce4ecd7ea99326bdae51d`

- Network outcome: exit 0.

- https://github.com/shadow-robot/sr_common sr_description/hand/xacro/forearm/forearm_e.urdf.xacro at 172c3d9c3715ee75eb10dfe4ee57e26a342b4529: ValueError: Macro-only input has no uniquely identified robot macro

- Offline Git read failed (exit 128): `('show', 'bda959328b7934176123af0cc0491c34ecaa23ce:sr_description/meshes/components/forearm/forearm_E3M5.dae')` in `shadow-robot__sr_common`. fatal: bad object bda959328b7934176123af0cc0491c34ecaa23ce:sr_description/meshes/components/forearm/forearm_E3M5.dae

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/shadow-robot__sr_common -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `d888ebf1bb054ab45a199019041befd69acf7272`

- Network outcome: exit 0.

- Historical source compile failed shadow_hand bda959328b7934176123af0cc0491c34ecaa23ce sr_description/robots/sr_hand.urdf.xacro: DaeMalformedError: XML Parsing Error: XML declaration allowed only at the start of the document, line 26, column 6 (<string>, line 26)

- Offline Git read failed (exit 128): `('show', '8ae940d250799b74a1bae0da2da14e2e4508551f:sr_description/meshes/components/forearm/forearm_E3M5.dae')` in `shadow-robot__sr_common`. fatal: bad object 8ae940d250799b74a1bae0da2da14e2e4508551f:sr_description/meshes/components/forearm/forearm_E3M5.dae

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/shadow-robot__sr_common -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `7a2a16e53fe48b839039d9a7add96242fe352c5d`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '8ae940d250799b74a1bae0da2da14e2e4508551f:sr_description/meshes/components/wrist/wrist_E3M5.dae')` in `shadow-robot__sr_common`. fatal: bad object 8ae940d250799b74a1bae0da2da14e2e4508551f:sr_description/meshes/components/wrist/wrist_E3M5.dae

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/shadow-robot__sr_common -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `32276c255ac94b3d25718011c99db60f6d0bba68`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '8ae940d250799b74a1bae0da2da14e2e4508551f:sr_description/meshes/components/palm/palm_E3M5.dae')` in `shadow-robot__sr_common`. fatal: bad object 8ae940d250799b74a1bae0da2da14e2e4508551f:sr_description/meshes/components/palm/palm_E3M5.dae

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/shadow-robot__sr_common -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `1c384f94f732ff01ac7dea2456a5f9c04c1715db`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '8ae940d250799b74a1bae0da2da14e2e4508551f:sr_description/meshes/components/f_distal/pst/f_distal_pst.dae')` in `shadow-robot__sr_common`. fatal: bad object 8ae940d250799b74a1bae0da2da14e2e4508551f:sr_description/meshes/components/f_distal/pst/f_distal_pst.dae

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/shadow-robot__sr_common -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `3432e6d57a37ad7682a0d4e04e93ebc76e7faf2a`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '8ae940d250799b74a1bae0da2da14e2e4508551f:sr_description/meshes/components/th_distal/pst/th_distal_pst.dae')` in `shadow-robot__sr_common`. fatal: bad object 8ae940d250799b74a1bae0da2da14e2e4508551f:sr_description/meshes/components/th_distal/pst/th_distal_pst.dae

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/shadow-robot__sr_common -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `69818dde53743357192f47f98e028a282146257c`

- Network outcome: exit 0.

- Rejected unrelated historical README template for agilex_piper: 0bee963312f0f4a25b53cdf9afe744ca73f2d68a heading '## UMI-Gripper Description (MJCF)'

- Offline Git read failed (exit 128): `('show', '400b5f5b9fec382583f69b53b094a154d9dc7635:agilex_piper/CHANGELOG.md')` in `menagerie`. fatal: path 'agilex_piper/CHANGELOG.md' does not exist in '400b5f5b9fec382583f69b53b094a154d9dc7635'

- Rejected conflicting robot-variant link for anybotics_anymal_c: https://github.com/ANYbotics/anymal_b_simple_description/blob/master/urdf/anymal.urdf (repository variant b, model variant c)

- Offline Git read failed (exit 128): `('show', 'd9415a3076f921fdb9735d45d609a596df722468:apptronik_apollo/CHANGELOG.md')` in `menagerie`. fatal: bad object d9415a3076f921fdb9735d45d609a596df722468:apptronik_apollo/CHANGELOG.md

- Offline Git read failed (exit 128): `('show', '400b5f5b9fec382583f69b53b094a154d9dc7635:arx_l5/CHANGELOG.md')` in `menagerie`. fatal: path 'arx_l5/CHANGELOG.md' does not exist in '400b5f5b9fec382583f69b53b094a154d9dc7635'

- Offline Git read failed (exit 128): `('show', 'd9415a3076f921fdb9735d45d609a596df722468:berkeley_humanoid/CHANGELOG.md')` in `menagerie`. fatal: bad object d9415a3076f921fdb9735d45d609a596df722468:berkeley_humanoid/CHANGELOG.md

- Rejected conflicting robot-variant link for bitcraze_crazyflie_2: https://github.com/whoenig/crazyflie_ros (repository variant ros, model variant 2)

- Offline Git read failed (exit 128): `('show', 'd9415a3076f921fdb9735d45d609a596df722468:booster_t1/CHANGELOG.md')` in `menagerie`. fatal: bad object d9415a3076f921fdb9735d45d609a596df722468:booster_t1/CHANGELOG.md

- Offline Git read failed (exit 128): `('show', 'd9415a3076f921fdb9735d45d609a596df722468:fourier_n1/CHANGELOG.md')` in `menagerie`. fatal: bad object d9415a3076f921fdb9735d45d609a596df722468:fourier_n1/CHANGELOG.md

- Offline Git read failed (exit 128): `('show', '400b5f5b9fec382583f69b53b094a154d9dc7635:fourier_n1/CHANGELOG.md')` in `menagerie`. fatal: path 'fourier_n1/CHANGELOG.md' does not exist in '400b5f5b9fec382583f69b53b094a154d9dc7635'

- Offline Git read failed (exit 128): `('show', 'db140ade7ee4cb59629f9687aafc65af663d5bbe:franka_fr3_v2/README.md')` in `menagerie`. fatal: path 'franka_fr3_v2/README.md' does not exist in 'db140ade7ee4cb59629f9687aafc65af663d5bbe'

- Offline Git read failed (exit 128): `('show', 'cd7fc51b704c3cba05748bd5537cb17990b341eb:franka_fr3_v2/README.md')` in `menagerie`. fatal: path 'franka_fr3_v2/README.md' does not exist in 'cd7fc51b704c3cba05748bd5537cb17990b341eb'

- Offline Git read failed (exit 128): `('show', '400b5f5b9fec382583f69b53b094a154d9dc7635:franka_fr3_v2/README.md')` in `menagerie`. fatal: path 'franka_fr3_v2/README.md' does not exist in '400b5f5b9fec382583f69b53b094a154d9dc7635'

- Offline Git read failed (exit 128): `('show', 'acbbf1636fcfef9b437a6eb8c6f84380fb4aa998:franka_fr3_v2/README.md')` in `menagerie`. fatal: path 'franka_fr3_v2/README.md' does not exist in 'acbbf1636fcfef9b437a6eb8c6f84380fb4aa998'

- Offline Git read failed (exit 128): `('show', '7876dcdef0d912387441616526ed236142f047d3:franka_fr3_v2/README.md')` in `menagerie`. fatal: path 'franka_fr3_v2/README.md' does not exist in '7876dcdef0d912387441616526ed236142f047d3'

- Offline Git read failed (exit 128): `('show', 'b5ebfe0cf079d2b96acf0a5c0e29ee0c95ba32f4:google_robot/README.md')` in `menagerie`. fatal: path 'google_robot/README.md' does not exist in 'b5ebfe0cf079d2b96acf0a5c0e29ee0c95ba32f4'

- Offline Git read failed (exit 128): `('show', '5ce04bea98bbfca277a8d50b55ba3c7c4a62bdec:i2rt_yam/CHANGELOG.md')` in `menagerie`. fatal: path 'i2rt_yam/CHANGELOG.md' does not exist in '5ce04bea98bbfca277a8d50b55ba3c7c4a62bdec'

- Offline Git read failed (exit 128): `('show', 'a88bc450470d97ebc1f282e5969675fb4d1f0ed7:low_cost_robot_arm/README.md')` in `menagerie`. fatal: path 'low_cost_robot_arm/README.md' does not exist in 'a88bc450470d97ebc1f282e5969675fb4d1f0ed7'

- Offline Git read failed (exit 128): `('show', 'd74280a600a9afdfcb98d8917d0c79c86539aa61:low_cost_robot_arm/README.md')` in `menagerie`. fatal: path 'low_cost_robot_arm/README.md' does not exist in 'd74280a600a9afdfcb98d8917d0c79c86539aa61'

- Offline Git read failed (exit 128): `('show', '13d6c48b8f59d2c4badee7756b4ea3532613cddf:low_cost_robot_arm/README.md')` in `menagerie`. fatal: path 'low_cost_robot_arm/README.md' does not exist in '13d6c48b8f59d2c4badee7756b4ea3532613cddf'

- Offline Git read failed (exit 128): `('show', 'fae9ee82330444eec4e87568c838b99a09a39467:rainbow_robotics_rby1/README.md')` in `menagerie`. fatal: path 'rainbow_robotics_rby1/README.md' does not exist in 'fae9ee82330444eec4e87568c838b99a09a39467'

- Offline Git read failed (exit 128): `('show', '04674c8d0a4e12e33980a9e47fb604adc281fcc8:robotstudio_so101/CHANGELOG.md')` in `menagerie`. fatal: path 'robotstudio_so101/CHANGELOG.md' does not exist in '04674c8d0a4e12e33980a9e47fb604adc281fcc8'

- Offline Git read failed (exit 128): `('show', '5ce04bea98bbfca277a8d50b55ba3c7c4a62bdec:robotstudio_so101/CHANGELOG.md')` in `menagerie`. fatal: path 'robotstudio_so101/CHANGELOG.md' does not exist in '5ce04bea98bbfca277a8d50b55ba3c7c4a62bdec'

- Offline Git read failed (exit 128): `('show', '4a7015530bd7a4161103ae8f0905a96481e4cc1a:robotstudio_so101/CHANGELOG.md')` in `menagerie`. fatal: path 'robotstudio_so101/CHANGELOG.md' does not exist in '4a7015530bd7a4161103ae8f0905a96481e4cc1a'

- Offline Git read failed (exit 128): `('show', 'bf110a75a56e5bd146c7ed76965737c71d48425d:shadow_dexee/README.md')` in `menagerie`. fatal: path 'shadow_dexee/README.md' does not exist in 'bf110a75a56e5bd146c7ed76965737c71d48425d'

- Offline Git read failed (exit 128): `('show', '04674c8d0a4e12e33980a9e47fb604adc281fcc8:tetheria_aero_hand_open/CHANGELOG.md')` in `menagerie`. fatal: path 'tetheria_aero_hand_open/CHANGELOG.md' does not exist in '04674c8d0a4e12e33980a9e47fb604adc281fcc8'

- Offline Git read failed (exit 128): `('show', '400b5f5b9fec382583f69b53b094a154d9dc7635:tetheria_aero_hand_open/CHANGELOG.md')` in `menagerie`. fatal: path 'tetheria_aero_hand_open/CHANGELOG.md' does not exist in '400b5f5b9fec382583f69b53b094a154d9dc7635'

- Offline Git read failed (exit 128): `('show', '04674c8d0a4e12e33980a9e47fb604adc281fcc8:toddlerbot_2xc/CHANGELOG.md')` in `menagerie`. fatal: path 'toddlerbot_2xc/CHANGELOG.md' does not exist in '04674c8d0a4e12e33980a9e47fb604adc281fcc8'

- Offline Git read failed (exit 128): `('show', '9e7f8d4dda07f5c281b6c0c6f0d07b9dd267b762:toddlerbot_2xc/CHANGELOG.md')` in `menagerie`. fatal: path 'toddlerbot_2xc/CHANGELOG.md' does not exist in '9e7f8d4dda07f5c281b6c0c6f0d07b9dd267b762'

- Offline Git read failed (exit 128): `('show', '400b5f5b9fec382583f69b53b094a154d9dc7635:toddlerbot_2xc/CHANGELOG.md')` in `menagerie`. fatal: path 'toddlerbot_2xc/CHANGELOG.md' does not exist in '400b5f5b9fec382583f69b53b094a154d9dc7635'

- Offline Git read failed (exit 128): `('show', '04674c8d0a4e12e33980a9e47fb604adc281fcc8:toddlerbot_2xm/CHANGELOG.md')` in `menagerie`. fatal: path 'toddlerbot_2xm/CHANGELOG.md' does not exist in '04674c8d0a4e12e33980a9e47fb604adc281fcc8'

- Offline Git read failed (exit 128): `('show', '9e7f8d4dda07f5c281b6c0c6f0d07b9dd267b762:toddlerbot_2xm/CHANGELOG.md')` in `menagerie`. fatal: path 'toddlerbot_2xm/CHANGELOG.md' does not exist in '9e7f8d4dda07f5c281b6c0c6f0d07b9dd267b762'

- Offline Git read failed (exit 128): `('show', '400b5f5b9fec382583f69b53b094a154d9dc7635:toddlerbot_2xm/CHANGELOG.md')` in `menagerie`. fatal: path 'toddlerbot_2xm/CHANGELOG.md' does not exist in '400b5f5b9fec382583f69b53b094a154d9dc7635'

- Offline Git read failed (exit 128): `('show', '400b5f5b9fec382583f69b53b094a154d9dc7635:trossen_wxai/README.md')` in `menagerie`. fatal: path 'trossen_wxai/README.md' does not exist in '400b5f5b9fec382583f69b53b094a154d9dc7635'

- Offline Git read failed (exit 128): `('show', '477ec56566682d663b996d86a188c75499e74b98:trossen_wxai/README.md')` in `menagerie`. fatal: path 'trossen_wxai/README.md' does not exist in '477ec56566682d663b996d86a188c75499e74b98'

- Offline Git read failed (exit 128): `('show', 'd9415a3076f921fdb9735d45d609a596df722468:unitree_g1/CHANGELOG.md')` in `menagerie`. fatal: bad object d9415a3076f921fdb9735d45d609a596df722468:unitree_g1/CHANGELOG.md

- Historical source compile failed boston_dynamics_spot 456b8025acc937fefe8ffa7e1477f6b692f7b961 spot_description/urdf/spot.urdf.xacro: mismatched tag: line 169, column 14

- https://github.com/TuragaLab/flybody flybody/fruitfly/build_fruitfly/fruitfly.xml at d015e9bfe441bd90ae431bac24c55cb74bdbce26: ValueError: Resource missing at d015e9bfe441bd90ae431bac24c55cb74bdbce26: flybody/fruitfly/build_fruitfly/head_body.obj

- https://github.com/TuragaLab/flybody flybody/fruitfly/build_fruitfly/floor.xml at d015e9bfe441bd90ae431bac24c55cb74bdbce26: ValueError: Resource missing at d015e9bfe441bd90ae431bac24c55cb74bdbce26: flybody/fruitfly/build_fruitfly/head_body.obj

- https://github.com/TuragaLab/flybody flybody/fruitfly/build_fruitfly/assets/drosophila.xml at d015e9bfe441bd90ae431bac24c55cb74bdbce26: ValueError: Resource missing at d015e9bfe441bd90ae431bac24c55cb74bdbce26: flybody/fruitfly/build_fruitfly/assets/assets/head_body.msh

- https://github.com/TuragaLab/flybody flybody/fruitfly/build_fruitfly/assets/drosophila_defaults.xml at d015e9bfe441bd90ae431bac24c55cb74bdbce26: ValueError: XML has no robot bodies; it is an include/extension fragment, not a standalone source

- Pinned source candidate failed flybody flybody/fruitfly/build_fruitfly/fruitfly.xml: Resource missing at 736608121847c3c025fd02a629bdb016a3294f9a: flybody/fruitfly/build_fruitfly/head_body.obj

- https://github.com/frankaemika/franka_ros franka_description/robots/common/utils.xacro at ddd2fffd9de44b02ad15b4bbb2bfa2cec4d60d98: ValueError: Macro-only input has no uniquely identified robot macro

- https://github.com/frankaemika/franka_ros franka_description/robots/common/franka_arm.xacro at ddd2fffd9de44b02ad15b4bbb2bfa2cec4d60d98: ValueError: Macro franka_arm requires unsupported explicit arguments: ['0', "0'", '0', "0'", 'joint_limits']

- https://github.com/frankaemika/franka_ros franka_description/robots/common/franka_hand.xacro at ddd2fffd9de44b02ad15b4bbb2bfa2cec4d60d98: ValueError: Macro franka_hand requires unsupported explicit arguments: ['0', "0'", '0', "0'", '0', "0.1034'", '0', "0'"]

- https://github.com/frankaemika/franka_ros franka_description/robots/common/franka_robot.xacro at ddd2fffd9de44b02ad15b4bbb2bfa2cec4d60d98: ValueError: Macro franka_robot requires unsupported explicit arguments: ['arm_id', 'joint_limits', '0', "0'", '0', "0'", '0', "0.1034'", '0', "0'"]

- Historical source compile failed franka_fr3 7de996b30cef3bb97beadad2f3c5c751e8899f45 robots/fr3/fr3.urdf.xacro: mismatched tag: line 115, column 4

- Historical source compile failed franka_fr3 b7cba8117ba666c4237834d34ebf3a716b44d43d robots/fr3/fr3.urdf.xacro: mismatched tag: line 100, column 4

- Historical source compile failed franka_fr3 1f718bebc0597cb0d63c1ebdb65f9af63f7ce980 robots/fr3/fr3.urdf.xacro: name 'arm_name' is not defined
when evaluating expression 'arm_name'

- Historical source compile failed franka_fr3 648987f4f4d616dd52426f4bf34f65216238371e robots/fr3/fr3.urdf.xacro: name 'arm_name' is not defined
when evaluating expression 'arm_name'

- Historical source compile failed franka_fr3 068f0b8ffe9665d0cd4a5e45274c663864c598c5 robots/fr3/fr3.urdf.xacro: Error: inertia must satisfy A + B >= C; use 'balanceinertia' to fix
Element name 'fr3_link2', id 4

- Historical source compile failed franka_fr3 e3278521f5639639196c5330cefd6c962bd3550b robots/fr3/fr3.urdf.xacro: Unresolved or ambiguous package path package://franka_description/meshes/robot_ee/franka_hand/visual/franka_hand.dae: []

- Historical source compile failed franka_fr3 4bb824f21dc553767b3bd2fafa363f8dc57a522d robots/fr3/fr3.urdf.xacro: DaeMalformedError: XML Parsing Error: XML declaration allowed only at the start of the document, line 25, column 6 (<string>, line 25)

- Historical source compile failed franka_fr3 de0dc86219272db8c0ab6be706940a38ddce73b4 robots/fr3/fr3.urdf.xacro: DaeMalformedError: XML Parsing Error: XML declaration allowed only at the start of the document, line 25, column 6 (<string>, line 25)

- Historical source compile failed franka_fr3 d5e8927aae7a100909753bb747799c663a2f4afd robots/fr3/fr3.urdf.xacro: DaeMalformedError: XML Parsing Error: XML declaration allowed only at the start of the document, line 25, column 6 (<string>, line 25)

- Historical source compile failed franka_fr3 b51da21a28af2cd27c028e61cbf328458e8a90f0 robots/fr3/fr3.urdf.xacro: DaeMalformedError: XML Parsing Error: XML declaration allowed only at the start of the document, line 25, column 6 (<string>, line 25)

- Historical source compile failed franka_fr3 1ddff9ba71abb199fb349ffcc3155e86cfdb094e robots/fr3/fr3.urdf.xacro: DaeMalformedError: XML Parsing Error: XML declaration allowed only at the start of the document, line 25, column 6 (<string>, line 25)

- https://github.com/frankarobotics/franka_description robots/fr3_duo/fr3_duo.xacro at 7aeeddc449edf8d62b594f9e36a81da53e7796f9: ValueError: Macro fr3_duo requires unsupported explicit arguments: ['robot_types', 'hand', 'ee_id', 'special_connection', 'xyz_ee', 'rpy_ee', 'tcp_xyz', 'tcp_rpy', 'safety_distance', 'with_sc', 'include_self_collision_geometry', 'description_pkg', 'base_mount', 'connected_to', 'arm_prefixes', '**arm0_extras', '**arm1_extras']

- Historical source compile failed franka_fr3_duo 1f718bebc0597cb0d63c1ebdb65f9af63f7ce980 robots/fr3_duo/fr3_duo.urdf.xacro: name 'arm_name' is not defined
when evaluating expression 'arm_name'

- Historical source compile failed franka_fr3_duo 648987f4f4d616dd52426f4bf34f65216238371e robots/fr3_duo/fr3_duo.urdf.xacro: name 'arm_name' is not defined
when evaluating expression 'arm_name'

- Historical source compile failed franka_fr3_duo f4fa7e5aa00908b9ef244ca6edeea861cf40c9fb robots/fr3_duo/fr3_duo.urdf.xacro: Undefined substitution argument kinematics_path'
when evaluating expression 'xacro.load_yaml('$(arg kinematics_path')'

- Historical source compile failed franka_fr3_duo 3bad514b1aa6a9ee46c47f806805bfb3fc993bd6 robots/fr3_duo/fr3_duo.urdf.xacro: Undefined substitution argument kinematics_path'
when evaluating expression 'xacro.load_yaml('$(arg kinematics_path')'

- Offline Git read failed (exit 128): `('show', '8b71e0d5154b1548bee3cc2f9e41dd2538a8ce16:meshes/robot_arms/fr3_duo/mount/visual/fr3_duo_mount.dae')` in `frankarobotics__franka_description`. fatal: bad object 8b71e0d5154b1548bee3cc2f9e41dd2538a8ce16:meshes/robot_arms/fr3_duo/mount/visual/fr3_duo_mount.dae

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/frankarobotics__franka_description -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `57a6ce324b6d007528a3ca9d7d5ff1690f2faeff`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '8b71e0d5154b1548bee3cc2f9e41dd2538a8ce16:meshes/robot_arms/fr3_duo/cover/visual/fr3_duo_cover.dae')` in `frankarobotics__franka_description`. fatal: bad object 8b71e0d5154b1548bee3cc2f9e41dd2538a8ce16:meshes/robot_arms/fr3_duo/cover/visual/fr3_duo_cover.dae

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/frankarobotics__franka_description -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `8f1d6772196f6bc6cdaa18aa19694b72f52c48fa`

- Network outcome: exit 0.

- Historical source compile failed franka_fr3_duo 1bda71e15b433bc355fa19bb0391dd7b6618a723 robots/fr3_duo/fr3_duo.urdf.xacro: Undefined substitution argument kinematics_path'
when evaluating expression 'xacro.load_yaml('$(arg kinematics_path')'

- Historical source compile failed franka_fr3_duo b6acf758a1a2bda99eef217b0a39b26ddad189e8 robots/fr3_duo/fr3_duo.urdf.xacro: Undefined substitution argument kinematics_path'
when evaluating expression 'xacro.load_yaml('$(arg kinematics_path')'

- Historical source compile failed franka_fr3_v2 1f718bebc0597cb0d63c1ebdb65f9af63f7ce980 robots/fr3v2/fr3v2.urdf.xacro: name 'arm_name' is not defined
when evaluating expression 'arm_name'

- Historical source compile failed franka_fr3_v2 648987f4f4d616dd52426f4bf34f65216238371e robots/fr3v2/fr3v2.urdf.xacro: name 'arm_name' is not defined
when evaluating expression 'arm_name'

- Historical source compile failed realsense_d435i d7e8792fe9d2de6a8a249b8f6c12205ed9c99b5c realsense2_description/urdf/_d435i.urdf.xacro: <class 'xacro.substitution_args.SubstitutionException'>: Unknown substitution command [realsense2_description]. Valid commands are ['find', 'env', 'optenv', 'dirname', 'arg'] Unknown substitution command [realsense2_description]. Valid commands are ['find', 'env', 'optenv', 'dirname', 'arg']

- Historical source compile failed realsense_d435i 487084f7fab58d23b3fe6e1c1d657fd78d8b048a realsense2_description/urdf/_d435i.urdf.xacro: Undefined substitution argument add_plug

- Historical source compile failed realsense_d435i ff2a81ce9ba7ab6f6b4e8c33c3d490b36093aa53 realsense2_description/urdf/_d435i.urdf.xacro: XML has no robot bodies; it is an include/extension fragment, not a standalone source

- Historical source compile failed realsense_d435i afef66f988c45cca14b4d8fd654c9c017c1b0ac1 realsense2_description/urdf/_d435i.urdf.xacro: XML has no robot bodies; it is an include/extension fragment, not a standalone source

- Historical source compile failed realsense_d435i c8a8afd14240f8adee1548771d9bca2e16bcb12b realsense2_description/urdf/_d435i.urdf.xacro: XML or text declaration not at start of entity: line 10, column 0

- Historical source compile failed realsense_d435i c81130c7d9b2141b4130f9ebebf4f02a1a184f7c realsense2_description/urdf/_d435i.urdf.xacro: XML or text declaration not at start of entity: line 10, column 0

- https://github.com/ros-industrial/robotiq robotiq_2f_85_gripper_visualization/urdf/robotiq_arg2f_transmission.xacro at 45196f6558fe8ba9d89bc8a105396c68c3e7e892: ValueError: XML has no robot bodies; it is an include/extension fragment, not a standalone source

- https://github.com/ros-industrial/robotiq robotiq_2f_85_gripper_visualization/urdf/robotiq_arg2f_85_model_macro.xacro at 45196f6558fe8ba9d89bc8a105396c68c3e7e892: ValueError: Macro-only input has no uniquely identified robot macro

- Offline Git read failed (exit 128): `('log', '--all', '--follow', '--find-renames=100%', '--format=@@@%H|%ct|%cI|%s', '--name-status', '--', 'robotiq_2f_85_gripper_visualization/urdf/robotiq_arg2f.xacro')` in `ros-industrial__robotiq`. warning: lazy fetching disabled; some objects may not be available
fatal: could not fetch d0f3a2ca2e5994acfcb52bfc88cbf273bd1e4724 from promisor remote

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/ros-industrial__robotiq -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `d0f3a2ca2e5994acfcb52bfc88cbf273bd1e4724`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('log', '--all', '--follow', '--find-renames=100%', '--format=@@@%H|%ct|%cI|%s', '--name-status', '--', 'robotiq_2f_85_gripper_visualization/urdf/robotiq_arg2f.xacro')` in `ros-industrial__robotiq`. warning: lazy fetching disabled; some objects may not be available
fatal: could not fetch 576a8a19bca0a4874c0dfea6066c50fd87a2b608 from promisor remote

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/ros-industrial__robotiq -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `576a8a19bca0a4874c0dfea6066c50fd87a2b608`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('log', '--all', '--follow', '--find-renames=100%', '--format=@@@%H|%ct|%cI|%s', '--name-status', '--', 'robotiq_2f_85_gripper_visualization/urdf/robotiq_arg2f.xacro')` in `ros-industrial__robotiq`. warning: lazy fetching disabled; some objects may not be available
fatal: could not fetch 687c937f6a35f68d5ada6173e76fd709d4a46454 from promisor remote

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/ros-industrial__robotiq -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `687c937f6a35f68d5ada6173e76fd709d4a46454`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('log', '--all', '--follow', '--find-renames=100%', '--format=@@@%H|%ct|%cI|%s', '--name-status', '--', 'robotiq_2f_85_gripper_visualization/urdf/robotiq_arg2f.xacro')` in `ros-industrial__robotiq`. warning: lazy fetching disabled; some objects may not be available
fatal: could not fetch 077325f42ddd18747eb8114b4cdbd7cf4fcb54ed from promisor remote

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/ros-industrial__robotiq -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `077325f42ddd18747eb8114b4cdbd7cf4fcb54ed`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('log', '--all', '--follow', '--find-renames=100%', '--format=@@@%H|%ct|%cI|%s', '--name-status', '--', 'robotiq_2f_85_gripper_visualization/urdf/robotiq_arg2f.xacro')` in `ros-industrial__robotiq`. warning: lazy fetching disabled; some objects may not be available
fatal: could not fetch 262506677f65f1afacfa1ef89e6702b2ec072c38 from promisor remote

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/ros-industrial__robotiq -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `262506677f65f1afacfa1ef89e6702b2ec072c38`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('log', '--all', '--follow', '--find-renames=100%', '--format=@@@%H|%ct|%cI|%s', '--name-status', '--', 'robotiq_2f_85_gripper_visualization/urdf/robotiq_arg2f.xacro')` in `ros-industrial__robotiq`. warning: lazy fetching disabled; some objects may not be available
fatal: could not fetch ca10dbc8a4bc7ef399dee84faff6fef3c6c51b25 from promisor remote

- History coverage warning for https://github.com/ros-industrial/robotiq robotiq_2f_85_gripper_visualization/urdf/robotiq_arg2f.xacro: Exact-rename traversal required unavailable unrelated blobs; current-path history was inspected, older renamed paths remain unresolved

- https://github.com/ros-industrial/robotiq robotiq_2f_85_gripper_visualization/urdf/robotiq_arg2f_transmission.xacro at 45196f6558fe8ba9d89bc8a105396c68c3e7e892: ValueError: XML has no robot bodies; it is an include/extension fragment, not a standalone source

- https://github.com/ros-industrial/robotiq robotiq_2f_85_gripper_visualization/urdf/robotiq_arg2f_85_model_macro.xacro at 45196f6558fe8ba9d89bc8a105396c68c3e7e892: ValueError: Macro-only input has no uniquely identified robot macro

- Offline Git read failed (exit 128): `('log', '--all', '--follow', '--find-renames=100%', '--format=@@@%H|%ct|%cI|%s', '--name-status', '--', 'robotiq_2f_85_gripper_visualization/urdf/robotiq_arg2f.xacro')` in `ros-industrial__robotiq`. warning: lazy fetching disabled; some objects may not be available
fatal: could not fetch ca10dbc8a4bc7ef399dee84faff6fef3c6c51b25 from promisor remote

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/ros-industrial__robotiq -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `ca10dbc8a4bc7ef399dee84faff6fef3c6c51b25`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('log', '--all', '--follow', '--find-renames=100%', '--format=@@@%H|%ct|%cI|%s', '--name-status', '--', 'robotiq_2f_85_gripper_visualization/urdf/robotiq_arg2f.xacro')` in `ros-industrial__robotiq`. warning: lazy fetching disabled; some objects may not be available
fatal: could not fetch 57ce41301ebbbcbda849b3ec4b0e86c26d88d376 from promisor remote

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/ros-industrial__robotiq -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `57ce41301ebbbcbda849b3ec4b0e86c26d88d376`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('log', '--all', '--follow', '--find-renames=100%', '--format=@@@%H|%ct|%cI|%s', '--name-status', '--', 'robotiq_2f_85_gripper_visualization/urdf/robotiq_arg2f.xacro')` in `ros-industrial__robotiq`. warning: lazy fetching disabled; some objects may not be available
fatal: could not fetch 79a7ab3361c62bb1e31f36ef1d207ee19b4e4f24 from promisor remote

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/ros-industrial__robotiq -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `79a7ab3361c62bb1e31f36ef1d207ee19b4e4f24`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('log', '--all', '--follow', '--find-renames=100%', '--format=@@@%H|%ct|%cI|%s', '--name-status', '--', 'robotiq_2f_85_gripper_visualization/urdf/robotiq_arg2f.xacro')` in `ros-industrial__robotiq`. warning: lazy fetching disabled; some objects may not be available
fatal: could not fetch c7ed58b3484c803192c0211746a144680b96ea96 from promisor remote

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/ros-industrial__robotiq -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `c7ed58b3484c803192c0211746a144680b96ea96`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('log', '--all', '--follow', '--find-renames=100%', '--format=@@@%H|%ct|%cI|%s', '--name-status', '--', 'robotiq_2f_85_gripper_visualization/urdf/robotiq_arg2f.xacro')` in `ros-industrial__robotiq`. warning: lazy fetching disabled; some objects may not be available
fatal: could not fetch 45ad02ac47672b5fdaa5911b542da4e5467dc503 from promisor remote

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/ros-industrial__robotiq -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `45ad02ac47672b5fdaa5911b542da4e5467dc503`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('log', '--all', '--follow', '--find-renames=100%', '--format=@@@%H|%ct|%cI|%s', '--name-status', '--', 'robotiq_2f_85_gripper_visualization/urdf/robotiq_arg2f.xacro')` in `ros-industrial__robotiq`. warning: lazy fetching disabled; some objects may not be available
fatal: could not fetch cebd4c2a281fd473a319d57bc7782d7f2470a386 from promisor remote

- History coverage warning for https://github.com/ros-industrial/robotiq robotiq_2f_85_gripper_visualization/urdf/robotiq_arg2f.xacro: Exact-rename traversal required unavailable unrelated blobs; current-path history was inspected, older renamed paths remain unresolved

- Offline Git read failed (exit 128): `('log', '--all', '--follow', '--find-renames=100%', '--format=@@@%H|%ct|%cI|%s', '--name-status', '--', 'open_manipulator_description/urdf/omy_3m/omy_3m.urdf')` in `ROBOTIS-GIT__open_manipulator`. warning: lazy fetching disabled; some objects may not be available
fatal: could not fetch 0d1e1d1ef00d063a9e83d0b13d9d658de23aa177 from promisor remote

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/ROBOTIS-GIT__open_manipulator -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `0d1e1d1ef00d063a9e83d0b13d9d658de23aa177`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('log', '--all', '--follow', '--find-renames=100%', '--format=@@@%H|%ct|%cI|%s', '--name-status', '--', 'open_manipulator_description/urdf/omy_3m/omy_3m.urdf')` in `ROBOTIS-GIT__open_manipulator`. warning: lazy fetching disabled; some objects may not be available
fatal: could not fetch 28217502943ce144c3e17f1e0bfc0440c87eadd0 from promisor remote

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/ROBOTIS-GIT__open_manipulator -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `28217502943ce144c3e17f1e0bfc0440c87eadd0`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('log', '--all', '--follow', '--find-renames=100%', '--format=@@@%H|%ct|%cI|%s', '--name-status', '--', 'open_manipulator_description/urdf/omy_3m/omy_3m.urdf')` in `ROBOTIS-GIT__open_manipulator`. warning: lazy fetching disabled; some objects may not be available
fatal: could not fetch 2392e1e9e74d9b68b070c7fc0140667d196b7389 from promisor remote

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/ROBOTIS-GIT__open_manipulator -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `2392e1e9e74d9b68b070c7fc0140667d196b7389`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('log', '--all', '--follow', '--find-renames=100%', '--format=@@@%H|%ct|%cI|%s', '--name-status', '--', 'open_manipulator_description/urdf/omy_3m/omy_3m.urdf')` in `ROBOTIS-GIT__open_manipulator`. warning: lazy fetching disabled; some objects may not be available
fatal: could not fetch 09c9ea822384fc9b863ebf02715d4aa1544153ad from promisor remote

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/ROBOTIS-GIT__open_manipulator -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `09c9ea822384fc9b863ebf02715d4aa1544153ad`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('log', '--all', '--follow', '--find-renames=100%', '--format=@@@%H|%ct|%cI|%s', '--name-status', '--', 'open_manipulator_description/urdf/omy_3m/omy_3m.urdf')` in `ROBOTIS-GIT__open_manipulator`. warning: lazy fetching disabled; some objects may not be available
fatal: could not fetch 2da8d37f3e3da0cd4c6312fb1be0c287ef94268b from promisor remote

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/ROBOTIS-GIT__open_manipulator -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `2da8d37f3e3da0cd4c6312fb1be0c287ef94268b`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('log', '--all', '--follow', '--find-renames=100%', '--format=@@@%H|%ct|%cI|%s', '--name-status', '--', 'open_manipulator_description/urdf/omy_3m/omy_3m.urdf')` in `ROBOTIS-GIT__open_manipulator`. warning: lazy fetching disabled; some objects may not be available
fatal: could not fetch 13684fdef0918523f74e033ef79714e4383fe79a from promisor remote

- History coverage warning for https://github.com/ROBOTIS-GIT/open_manipulator open_manipulator_description/urdf/omy_3m/omy_3m.urdf: Exact-rename traversal required unavailable unrelated blobs; current-path history was inspected, older renamed paths remain unresolved

- https://github.com/ROBOTIS-GIT/ROBOTIS-OP3-Common op3_description/urdf/gazebo_harness.xacro at 0780e54c2064a42089b0cf970d716ae44fec9233: ValueError: Macro add_sim_harness requires unsupported explicit arguments: ['harnessed_link']

- https://github.com/ROBOTIS-GIT/ROBOTIS-OP3-Common op3_description/urdf/robotis_op3.gazebo.xacro at 0780e54c2064a42089b0cf970d716ae44fec9233: ValueError: XML has no robot bodies; it is an include/extension fragment, not a standalone source

- https://github.com/ROBOTIS-GIT/ROBOTIS-OP3-Common op3_description/urdf/robotis_op3.inertia.xacro at 0780e54c2064a42089b0cf970d716ae44fec9233: ValueError: Macro-only input has no uniquely identified robot macro

- https://github.com/ROBOTIS-GIT/ROBOTIS-OP3-Common op3_description/urdf/robotis_op3.visuals.xacro at 0780e54c2064a42089b0cf970d716ae44fec9233: ValueError: Macro-only input has no uniquely identified robot macro

- https://github.com/ROBOTIS-GIT/ROBOTIS-OP3-Common op3_description/urdf/robotis_op3.transmissions.xacro at 0780e54c2064a42089b0cf970d716ae44fec9233: ValueError: XML has no robot bodies; it is an include/extension fragment, not a standalone source

- https://github.com/ROBOTIS-GIT/ROBOTIS-OP3-Common op3_description/urdf/robotis_op3.structure.head.xacro at 0780e54c2064a42089b0cf970d716ae44fec9233: XacroException: unknown macro name: xacro:insert_transmission

- https://github.com/ROBOTIS-GIT/ROBOTIS-OP3-Common op3_description/urdf/robotis_op3.structure.larm.xacro at 0780e54c2064a42089b0cf970d716ae44fec9233: XacroException: unknown macro name: xacro:insert_transmission

- https://github.com/ROBOTIS-GIT/ROBOTIS-OP3-Common op3_description/urdf/robotis_op3.structure.lleg.xacro at 0780e54c2064a42089b0cf970d716ae44fec9233: XacroException: unknown macro name: xacro:insert_transmission

- https://github.com/ROBOTIS-GIT/ROBOTIS-OP3-Common op3_description/urdf/robotis_op3.structure.rarm.xacro at 0780e54c2064a42089b0cf970d716ae44fec9233: XacroException: unknown macro name: xacro:insert_transmission

- https://github.com/ROBOTIS-GIT/ROBOTIS-OP3-Common op3_description/urdf/robotis_op3.structure.rleg.xacro at 0780e54c2064a42089b0cf970d716ae44fec9233: XacroException: unknown macro name: xacro:insert_transmission

- Offline Git read failed (exit 128): `('log', '--all', '--follow', '--find-renames=100%', '--format=@@@%H|%ct|%cI|%s', '--name-status', '--', 'op3_description/urdf/robotis_op3.urdf.xacro')` in `ROBOTIS-GIT__ROBOTIS-OP3-Common`. warning: lazy fetching disabled; some objects may not be available
fatal: could not fetch 1d9697d981afdaac96b4e3b6596d0143f56fd3aa from promisor remote

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/ROBOTIS-GIT__ROBOTIS-OP3-Common -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `1d9697d981afdaac96b4e3b6596d0143f56fd3aa`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('log', '--all', '--follow', '--find-renames=100%', '--format=@@@%H|%ct|%cI|%s', '--name-status', '--', 'op3_description/urdf/robotis_op3.urdf.xacro')` in `ROBOTIS-GIT__ROBOTIS-OP3-Common`. warning: lazy fetching disabled; some objects may not be available
fatal: could not fetch 681898c320d9341b82ba6de19856ab65761542c5 from promisor remote

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/ROBOTIS-GIT__ROBOTIS-OP3-Common -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `681898c320d9341b82ba6de19856ab65761542c5`

- Network outcome: exit 0.

- Historical source compile failed robotis_op3 139a7ac0d950755aa28318d418552db0ae0cd93e op3_description/urdf/robotis_op3.urdf.xacro: No such file or directory: .cache/ROBOTIS-GIT__ROBOTIS-OP3-Common/.drift_xacro/tmp3im9yp7r/.unresolved_package/op3_gazebo_ros2/gazebo/robotis_op3.gazebo.xacro [Errno 2] No such file or directory: '.cache/ROBOTIS-GIT__ROBOTIS-OP3-Common/.drift_xacro/tmp3im9yp7r/.unresolved_package/op3_gazebo_ros2/gazebo/robotis_op3.gazebo.xacro'

- Historical source compile failed robotis_op3 0f22b4239725f57b70b873d5e589d584d721ee50 op3_description/urdf/robotis_op3.urdf.xacro: unknown macro name: xacro:insert_transmission

- Historical source compile failed robotis_op3 b3947376853ab2afab01e910a80177c18827b1f3 op3_description/urdf/robotis_op3.urdf.xacro: No such file or directory: .cache/ROBOTIS-GIT__ROBOTIS-OP3-Common/.drift_xacro/tmp9v6eosm0/.unresolved_package/robotis_op3_description/urdf/robotis_op3.visuals.xacro [Errno 2] No such file or directory: '.cache/ROBOTIS-GIT__ROBOTIS-OP3-Common/.drift_xacro/tmp9v6eosm0/.unresolved_package/robotis_op3_description/urdf/robotis_op3.visuals.xacro'

- https://github.com/shadow-robot/sr_common sr_description/hand/xacro/forearm/forearm_e.urdf.xacro at 172c3d9c3715ee75eb10dfe4ee57e26a342b4529: ValueError: Macro-only input has no uniquely identified robot macro

- https://github.com/shadow-robot/sr_common sr_description/mujoco_models/urdfs/shadowhand_motor.urdf at 172c3d9c3715ee75eb10dfe4ee57e26a342b4529: ParseError: XML or text declaration not at start of entity: line 26, column 0

- https://github.com/shadow-robot/sr_common sr_description/mujoco_models/urdfs/shadowhand_motor_left.urdf at 172c3d9c3715ee75eb10dfe4ee57e26a342b4529: ParseError: XML or text declaration not at start of entity: line 26, column 0

- https://github.com/shadow-robot/sr_common sr_description/mujoco_models/urdfs/shadowhand_motor_plus.urdf at 172c3d9c3715ee75eb10dfe4ee57e26a342b4529: ParseError: XML or text declaration not at start of entity: line 26, column 0

- https://github.com/shadow-robot/sr_common sr_description/mujoco_models/urdfs/shadowhand_motor_plus_left.urdf at 172c3d9c3715ee75eb10dfe4ee57e26a342b4529: ParseError: XML or text declaration not at start of entity: line 26, column 0

- Offline Git read failed (exit 128): `('show', 'efa7d38707acc6eef1b1f1cfd45e9ef478dd910c:sr_description/meshes/components/forearm/forearm_E3M5.dae')` in `shadow-robot__sr_common`. fatal: bad object efa7d38707acc6eef1b1f1cfd45e9ef478dd910c:sr_description/meshes/components/forearm/forearm_E3M5.dae

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/shadow-robot__sr_common -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `945e051fae3d5715dd89612494ae553304634346`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', 'efa7d38707acc6eef1b1f1cfd45e9ef478dd910c:sr_description/meshes/components/th_distal/pst/th_distal_pst.dae')` in `shadow-robot__sr_common`. fatal: bad object efa7d38707acc6eef1b1f1cfd45e9ef478dd910c:sr_description/meshes/components/th_distal/pst/th_distal_pst.dae

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/shadow-robot__sr_common -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `d0313da2eb7ecdbfdc9d45acde55a5169f19a545`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '76eb3d8f0de2a8d7aa41c71c2904a3a28cc81036:sr_description/meshes/components/forearm/forearm_E3M5.dae')` in `shadow-robot__sr_common`. fatal: bad object 76eb3d8f0de2a8d7aa41c71c2904a3a28cc81036:sr_description/meshes/components/forearm/forearm_E3M5.dae

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/shadow-robot__sr_common -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `485dac18cd6210346d36fcd2ce5309993ba8e4f4`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '76eb3d8f0de2a8d7aa41c71c2904a3a28cc81036:sr_description/meshes/components/th_distal/pst/th_distal_pst.dae')` in `shadow-robot__sr_common`. fatal: bad object 76eb3d8f0de2a8d7aa41c71c2904a3a28cc81036:sr_description/meshes/components/th_distal/pst/th_distal_pst.dae

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/shadow-robot__sr_common -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `904afa422f056827678707b9e895e57d43de3f9b`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('show', '1039a5904aaf2b9a1ee8b71f5706fc18d1d059d5:sr_description/meshes/components/th_distal/pst/th_distal_pst.dae')` in `shadow-robot__sr_common`. fatal: bad object 1039a5904aaf2b9a1ee8b71f5706fc18d1d059d5:sr_description/meshes/components/th_distal/pst/th_distal_pst.dae

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/shadow-robot__sr_common -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `0097003f4940e718e37ba9817a6f80586ee28be9`

- Network outcome: exit 0.

- Historical source compile failed shadow_hand ac0af1a9476c95475be95ace0121c906f6882b08 sr_description/robots/sr_hand.urdf.xacro: DaeMalformedError: XML Parsing Error: XML declaration allowed only at the start of the document, line 26, column 6 (<string>, line 26)

- Historical source compile failed shadow_hand bda959328b7934176123af0cc0491c34ecaa23ce sr_description/robots/sr_hand.urdf.xacro: DaeMalformedError: XML Parsing Error: XML declaration allowed only at the start of the document, line 26, column 6 (<string>, line 26)

- https://github.com/xArm-Developer/xarm_ros2 xarm_description/urdf/lite6/lite6.urdf.xacro at ac736c92b02de7ca7e0be6f737d77d46707464d8: XacroException: name 'use_xacro_load_yaml' is not defined
when evaluating expression 'use_xacro_load_yaml'

- https://github.com/xArm-Developer/xarm_ros2 xarm_description/urdf/lite6/lite6.gazebo.xacro at ac736c92b02de7ca7e0be6f737d77d46707464d8: ValueError: XML has no robot bodies; it is an include/extension fragment, not a standalone source

- https://github.com/xArm-Developer/xarm_ros2 xarm_description/urdf/lite6/lite6.ros2_control.xacro at ac736c92b02de7ca7e0be6f737d77d46707464d8: ValueError: XML has no robot bodies; it is an include/extension fragment, not a standalone source

- https://github.com/xArm-Developer/xarm_ros2 xarm_description/urdf/lite6/lite6.transmission.xacro at ac736c92b02de7ca7e0be6f737d77d46707464d8: ValueError: XML has no robot bodies; it is an include/extension fragment, not a standalone source

- https://github.com/xArm-Developer/xarm_ros2 xarm_description/urdf/lite6/lite6_robot_macro.xacro at ac736c92b02de7ca7e0be6f737d77d46707464d8: XacroException: name 'is_ros2' is not defined
when evaluating expression 'is_ros2'

- Historical source compile failed ufactory_lite6 e82e45df62a6b9b290df35fe97c8ef980f3dead6 xarm_description/urdf/xarm_device.urdf.xacro: Resource missing at e82e45df62a6b9b290df35fe97c8ef980f3dead6: ../../../xarm_description/meshes/lite6/visual/base.stl

- Historical source compile failed ufactory_lite6 43f3be4da51d6cc81901f9833cc7d420822e6cea xarm_description/urdf/xarm_device.urdf.xacro: Resource missing at 43f3be4da51d6cc81901f9833cc7d420822e6cea: ../../../xarm_description/meshes/lite6/visual/base.stl

- Historical source compile failed ufactory_lite6 72d9e0b5db59433866b71fbc9dcad97dcc4d0993 xarm_description/urdf/xarm_device.urdf.xacro: Resource missing at 72d9e0b5db59433866b71fbc9dcad97dcc4d0993: ../../../xarm_description/meshes/lite6/visual/base.stl

- Historical source compile failed ufactory_lite6 26cac4b33c195bd121b20bb76f9b6b6f13c52488 xarm_description/urdf/xarm_device.urdf.xacro: Resource missing at 26cac4b33c195bd121b20bb76f9b6b6f13c52488: ../../../xarm_description/meshes/lite6/visual/base.stl

- Historical source compile failed ufactory_lite6 4b21786c471d92d66bb1060d5a80b428137bb537 xarm_description/urdf/xarm_device.urdf.xacro: Resource missing at 4b21786c471d92d66bb1060d5a80b428137bb537: ../../../xarm_description/meshes/lite6/visual/base.stl

- Historical source compile failed ufactory_lite6 ab2ce303a9a58cdc0af1bd32e9dd6bc8eeb20c05 xarm_description/urdf/xarm_device.urdf.xacro: Resource missing at ab2ce303a9a58cdc0af1bd32e9dd6bc8eeb20c05: ../../../xarm_description/meshes/lite6/visual/base.stl

- Historical source compile failed ufactory_lite6 046756a2e26707b9afe17592735ff3e49e5700d0 xarm_description/urdf/xarm_device.urdf.xacro: Resource missing at 046756a2e26707b9afe17592735ff3e49e5700d0: ../../../xarm_description/meshes/lite6/visual/base.stl

- Historical source compile failed ufactory_lite6 4c5908625f334bd7a599239a5c556ba56f129578 xarm_description/urdf/xarm_device.urdf.xacro: Resource missing at 4c5908625f334bd7a599239a5c556ba56f129578: ../../../xarm_description/meshes/lite6/visual/base.stl

- Historical source compile failed ufactory_lite6 6dd2963bd3b2419f965f7a1bf022e7c680c58b54 xarm_description/urdf/xarm_device.urdf.xacro: Resource missing at 6dd2963bd3b2419f965f7a1bf022e7c680c58b54: ../../../xarm_description/meshes/lite6/visual/base.stl

- Historical source compile failed ufactory_lite6 3c153bbb8841d491f8a65434eb2fc5ce0da7b6c7 xarm_description/urdf/xarm_device.urdf.xacro: Resource missing at 3c153bbb8841d491f8a65434eb2fc5ce0da7b6c7: ../../../xarm_description/meshes/lite6/visual/base.stl

- Historical source compile failed ufactory_lite6 5b4bc59ba8e8aa1a4e7c78543fc8f4d3cb3b53ab xarm_description/urdf/xarm_device.urdf.xacro: Resource missing at 5b4bc59ba8e8aa1a4e7c78543fc8f4d3cb3b53ab: ../../../xarm_description/meshes/lite6/visual/base.stl

- Historical source compile failed ufactory_lite6 31743052d1f8533850da79abb1e3f81515b28764 xarm_description/urdf/xarm_device.urdf.xacro: Resource missing at 31743052d1f8533850da79abb1e3f81515b28764: ../../../xarm_description/meshes/lite6/visual/base.stl

- Historical source compile failed ufactory_lite6 7d3918e4590322a850d2f29564269f5ce6708f8a xarm_description/urdf/xarm_device.urdf.xacro: Resource missing at 7d3918e4590322a850d2f29564269f5ce6708f8a: ../../../xarm_description/meshes/lite6/visual/base.stl

- Historical source compile failed ufactory_lite6 27874699082c12ee4a390bf3b57108a7c5b3f468 xarm_description/urdf/xarm_device.urdf.xacro: Resource missing at 27874699082c12ee4a390bf3b57108a7c5b3f468: ../../../xarm_description/meshes/lite6/visual/base.stl

- Historical source compile failed ufactory_lite6 175000bcfa9259f1177ac0b669b41f5202b065a3 xarm_description/urdf/xarm_device.urdf.xacro: Resource missing at 175000bcfa9259f1177ac0b669b41f5202b065a3: ../../../xarm_description/meshes/lite6/visual/base.stl

- Historical source compile failed ufactory_lite6 e5a1e3feb2334e6f4d5ee1d5c99ace0e00b5b0bb xarm_description/urdf/xarm_device.urdf.xacro: Resource missing at e5a1e3feb2334e6f4d5ee1d5c99ace0e00b5b0bb: ../../../xarm_description/meshes/lite6/visual/base.stl

- Historical source compile failed ufactory_lite6 3bfa3f167262d4ff0b04402afa81eaeb5761fd6c xarm_description/urdf/xarm_device.urdf.xacro: Resource missing at 3bfa3f167262d4ff0b04402afa81eaeb5761fd6c: ../../../xarm_description/meshes/lite6/visual/base.stl

- Historical source compile failed ufactory_lite6 d33de50aaff5ca0768c7501fcf124a1d61802bdc xarm_description/urdf/xarm_device.urdf.xacro: Resource missing at d33de50aaff5ca0768c7501fcf124a1d61802bdc: ../../../xarm_description/meshes/lite6/visual/base.stl

- Historical source compile failed ufactory_lite6 0f8ebb37378d5da713ae773e0031bd89c0fd8e0e xarm_description/urdf/xarm_device.urdf.xacro: Resource missing at 0f8ebb37378d5da713ae773e0031bd89c0fd8e0e: ../../../xarm_description/meshes/lite6/visual/base.stl

- Historical source compile failed ufactory_lite6 ea976435eca4a20a8e29fe8549bf3f6f5abbbeb7 xarm_description/urdf/xarm_device.urdf.xacro: Resource missing at ea976435eca4a20a8e29fe8549bf3f6f5abbbeb7: ../../../xarm_description/meshes/lite6/visual/base.stl

- Historical source compile failed ufactory_lite6 f0ad415d615f658ba747fc533757e2c923d294c8 xarm_description/urdf/xarm_device.urdf.xacro: Resource missing at f0ad415d615f658ba747fc533757e2c923d294c8: ../../../xarm_description/meshes/lite6/visual/base.stl

- Historical source compile failed ufactory_lite6 7a2ba61a7090d155e68d5f0ba8bb2bb8c55bb746 xarm_description/urdf/xarm_device.urdf.xacro: Resource missing at 7a2ba61a7090d155e68d5f0ba8bb2bb8c55bb746: ../../../xarm_description/meshes/lite6/visual/base.stl

- Historical source compile failed ufactory_lite6 32cf9ff739ad0b4794e76bcb0df7d1d7b712bb8f xarm_description/urdf/xarm_device.urdf.xacro: Resource missing at 32cf9ff739ad0b4794e76bcb0df7d1d7b712bb8f: ../../../xarm_description/meshes/xarm6/visual/base.stl

- Historical source compile failed ufactory_lite6 eb02b6cfffd318ab049ce695e37941b8ddf8cd99 xarm_description/urdf/xarm_device.urdf.xacro: Resource missing at eb02b6cfffd318ab049ce695e37941b8ddf8cd99: ../../../xarm_description/meshes/xarm6/visual/base.stl

- Historical source compile failed ufactory_lite6 53a43be71f4b79bb5e2cdbe2f655a89655002548 xarm_description/urdf/xarm_device.urdf.xacro: Error: inertia must satisfy A + B >= C; use 'balanceinertia' to fix
Element name 'link2', id 3

- Historical source compile failed ufactory_lite6 02bf5f1bb07a3dad8f477b5ddc0ba03c582f5168 xarm_description/urdf/xarm_device.urdf.xacro: Error: inertia must satisfy A + B >= C; use 'balanceinertia' to fix
Element name 'link2', id 3

- Historical source compile failed ufactory_lite6 db64c562277909bc08c558b2f629bccf882db6a6 xarm_description/urdf/xarm_device.urdf.xacro: Error: inertia must satisfy A + B >= C; use 'balanceinertia' to fix
Element name 'link2', id 3

- Historical source compile failed ufactory_lite6 d17f59ebd0c9a9c6afd0bf61ee843d6e3b12ce61 xarm_description/urdf/xarm_device.urdf.xacro: Error: inertia must satisfy A + B >= C; use 'balanceinertia' to fix
Element name 'link2', id 3

- Historical source compile failed ufactory_lite6 bcceb1a87b32341dd4e11d8f8735835c9fc1c6f8 xarm_description/urdf/xarm_device.urdf.xacro: Error: inertia must satisfy A + B >= C; use 'balanceinertia' to fix
Element name 'link2', id 3

- Historical source compile failed ufactory_lite6 08ca7e445fdee4ddd5828f76e66a3b965d1e8c9b xarm_description/urdf/xarm_device.urdf.xacro: Error: inertia must satisfy A + B >= C; use 'balanceinertia' to fix
Element name 'link2', id 3

- Historical source compile failed ufactory_lite6 27be56de2e00e36d8e6db5a6b55a37d91ed894b8 xarm_description/urdf/xarm_device.urdf.xacro: Error: inertia must satisfy A + B >= C; use 'balanceinertia' to fix
Element name 'link2', id 3

- https://github.com/xArm-Developer/xarm_ros xarm_description/urdf/xarm7/xarm7.urdf.xacro at cf51617d98bc55a88d9aa735acfa43a0bbb8e425: XacroException: name 'mesh_suffix' is not defined
when evaluating expression 'mesh_suffix == 'dae' or (model_num >= 1305 and model_num != 1380)'

- https://github.com/xArm-Developer/xarm_ros xarm_description/urdf/xarm7/xarm7.gazebo.xacro at cf51617d98bc55a88d9aa735acfa43a0bbb8e425: ValueError: XML has no robot bodies; it is an include/extension fragment, not a standalone source

- https://github.com/xArm-Developer/xarm_ros xarm_description/urdf/xarm7/xarm7.ros2_control.xacro at cf51617d98bc55a88d9aa735acfa43a0bbb8e425: ValueError: XML has no robot bodies; it is an include/extension fragment, not a standalone source

- https://github.com/xArm-Developer/xarm_ros xarm_description/urdf/xarm7/xarm7.transmission.xacro at cf51617d98bc55a88d9aa735acfa43a0bbb8e425: ValueError: XML has no robot bodies; it is an include/extension fragment, not a standalone source

- https://github.com/xArm-Developer/xarm_ros xarm_description/urdf/xarm7/xarm7_robot_macro.xacro at cf51617d98bc55a88d9aa735acfa43a0bbb8e425: XacroException: name 'is_ros2' is not defined
when evaluating expression 'is_ros2'

- Offline Git read failed (exit 128): `('log', '--all', '--follow', '--find-renames=100%', '--format=@@@%H|%ct|%cI|%s', '--name-status', '--', 'xarm_description/urdf/xarm_device.urdf.xacro')` in `xArm-Developer__xarm_ros`. warning: lazy fetching disabled; some objects may not be available
fatal: could not fetch 352a95d3d9fc6c53fee3de2ebd06930f14246077 from promisor remote

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/xArm-Developer__xarm_ros -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `352a95d3d9fc6c53fee3de2ebd06930f14246077`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('log', '--all', '--follow', '--find-renames=100%', '--format=@@@%H|%ct|%cI|%s', '--name-status', '--', 'xarm_description/urdf/xarm_device.urdf.xacro')` in `xArm-Developer__xarm_ros`. warning: lazy fetching disabled; some objects may not be available
fatal: could not fetch 8b662f3c3721edac4f0d30c2b66ea6b6ac52a65a from promisor remote

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/xArm-Developer__xarm_ros -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `8b662f3c3721edac4f0d30c2b66ea6b6ac52a65a`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('log', '--all', '--follow', '--find-renames=100%', '--format=@@@%H|%ct|%cI|%s', '--name-status', '--', 'xarm_description/urdf/xarm_device.urdf.xacro')` in `xArm-Developer__xarm_ros`. warning: lazy fetching disabled; some objects may not be available
fatal: could not fetch 9a93c31810d3c89a2eb7766fc0f56bf2cedd3091 from promisor remote

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/xArm-Developer__xarm_ros -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `9a93c31810d3c89a2eb7766fc0f56bf2cedd3091`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('log', '--all', '--follow', '--find-renames=100%', '--format=@@@%H|%ct|%cI|%s', '--name-status', '--', 'xarm_description/urdf/xarm_device.urdf.xacro')` in `xArm-Developer__xarm_ros`. warning: lazy fetching disabled; some objects may not be available
fatal: could not fetch ef7c2dba3153967b6f6301c113b1609d24e1167d from promisor remote

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/xArm-Developer__xarm_ros -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `ef7c2dba3153967b6f6301c113b1609d24e1167d`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('log', '--all', '--follow', '--find-renames=100%', '--format=@@@%H|%ct|%cI|%s', '--name-status', '--', 'xarm_description/urdf/xarm_device.urdf.xacro')` in `xArm-Developer__xarm_ros`. warning: lazy fetching disabled; some objects may not be available
fatal: could not fetch 56cf92dbee47b65c03e767cad4043b5f18593c9e from promisor remote

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/xArm-Developer__xarm_ros -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `56cf92dbee47b65c03e767cad4043b5f18593c9e`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('log', '--all', '--follow', '--find-renames=100%', '--format=@@@%H|%ct|%cI|%s', '--name-status', '--', 'xarm_description/urdf/xarm_device.urdf.xacro')` in `xArm-Developer__xarm_ros`. warning: lazy fetching disabled; some objects may not be available
fatal: could not fetch 84d3e5d074b544b72286472f68ee551f555de65c from promisor remote

- History coverage warning for https://github.com/xArm-Developer/xarm_ros xarm_description/urdf/xarm_device.urdf.xacro: Exact-rename traversal required unavailable unrelated blobs; current-path history was inspected, older renamed paths remain unresolved

- Historical source compile failed ufactory_xarm7 5b7bfe4585819fddb962b018d7362d30db892960 xarm_description/urdf/xarm_device.urdf.xacro: Use of invalid name(s):  __len__
when evaluating expression 'robot_sn.__len__()'
when evaluating expression 'robot_sn_len >= 14 and (robot_sn[0] == 'X' or robot_sn[0] == 'L' or robot_sn[0] == 'F')'

- Historical source compile failed ufactory_xarm7 b9d492275b968d24317ca33a9f2579e1633acbbf xarm_description/urdf/xarm_device.urdf.xacro: Use of invalid name(s):  __len__
when evaluating expression 'robot_sn.__len__()'
when evaluating expression 'robot_sn_len >= 14 and (robot_sn[0] == 'X' or robot_sn[0] == 'L' or robot_sn[0] == 'F')'

- Historical source compile failed ufactory_xarm7 9bf2158860c8df275186f36f852647ea7a5cfb0e xarm_description/urdf/xarm_device.urdf.xacro: Use of invalid name(s):  __len__
when evaluating expression 'robot_sn.__len__()'
when evaluating expression 'robot_sn_len >= 14 and (robot_sn[0] == 'X' or robot_sn[0] == 'L' or robot_sn[0] == 'F')'

- Historical source compile failed ufactory_xarm7 f8d572f768d990122dca304144f92bcf09a1f2ec xarm_description/urdf/xarm_device.urdf.xacro: Use of invalid name(s):  __len__
when evaluating expression 'robot_sn.__len__()'
when evaluating expression 'robot_sn_len >= 14 and (robot_sn[0] == 'X' or robot_sn[0] == 'L' or robot_sn[0] == 'F')'

- Historical source compile failed ufactory_xarm7 de625f9f102d126a54ca92b40df9962ce03ea620 xarm_description/urdf/xarm_device.urdf.xacro: Use of invalid name(s):  __len__
when evaluating expression 'robot_sn.__len__()'
when evaluating expression 'robot_sn_len >= 14 and (robot_sn[0] == 'X' or robot_sn[0] == 'L' or robot_sn[0] == 'F')'

- Historical source compile failed ufactory_xarm7 74e75cf87e6904d0876b869113d09a8bc9f6e176 xarm_description/urdf/xarm_device.urdf.xacro: Use of invalid name(s):  __len__
when evaluating expression 'robot_sn.__len__()'
when evaluating expression 'robot_sn_len >= 14 and (robot_sn[0] == 'X' or robot_sn[0] == 'L' or robot_sn[0] == 'F')'

- Historical source compile failed ufactory_xarm7 c7eeca9ea1ff779c7b4e084968cd364ba4b32e4c xarm_description/urdf/xarm_device.urdf.xacro: Use of invalid name(s):  __len__
when evaluating expression 'robot_sn.__len__()'
when evaluating expression 'robot_sn_len >= 14 and (robot_sn[0] == 'X' or robot_sn[0] == 'L' or robot_sn[0] == 'F')'

- Historical source compile failed ufactory_xarm7 281d6c301092d93d3deac12b6b6b6dd86fb05df1 xarm_description/urdf/xarm_device.urdf.xacro: Use of invalid name(s):  __len__
when evaluating expression 'robot_sn.__len__()'
when evaluating expression 'robot_sn_len >= 14 and (robot_sn[0] == 'X' or robot_sn[0] == 'L' or robot_sn[0] == 'F')'

- Historical source compile failed ufactory_xarm7 bed4ea09157bb044b543d2ca5fcf7780cef8a6da xarm_description/urdf/xarm_device.urdf.xacro: Use of invalid name(s):  __len__
when evaluating expression 'robot_sn.__len__()'
when evaluating expression 'robot_sn_len >= 14 and (robot_sn[0] == 'X' or robot_sn[0] == 'L' or robot_sn[0] == 'F')'

- Historical source compile failed ufactory_xarm7 87ce4faaffec776b683a5d7c480146ffae1f7bdb xarm_description/urdf/xarm_device.urdf.xacro: Use of invalid name(s):  __len__
when evaluating expression 'robot_sn.__len__()'
when evaluating expression 'robot_sn_len >= 14 and (robot_sn[0] == 'X' or robot_sn[0] == 'L')'

- Historical source compile failed ufactory_xarm7 75956706e0108c2abcb98ed91eb6403604844acf xarm_description/urdf/xarm_device.urdf.xacro: Use of invalid name(s):  __len__
when evaluating expression 'robot_sn.__len__()'
when evaluating expression 'robot_sn_len >= 14 and (robot_sn[0] == 'X' or robot_sn[0] == 'L')'

- Historical source compile failed ufactory_xarm7 d8f863a37fa7810f9b0cef156088530f8340afb9 xarm_description/urdf/xarm_device.urdf.xacro: Use of invalid name(s):  __len__
when evaluating expression 'robot_sn.__len__()'
when evaluating expression 'robot_sn_len >= 14 and (robot_sn[0] == 'X' or robot_sn[0] == 'L')'

- Historical source compile failed ufactory_xarm7 79d6c2d2a16c10abdd2ae21b8fd6efe80bec3a41 xarm_description/urdf/xarm_device.urdf.xacro: Error: inertia must satisfy A + B >= C; use 'balanceinertia' to fix
Element name 'link4', id 5

- Historical source compile failed ufactory_xarm7 5fd541a9e85716ce4c3a9cc793cc5cfed2c11084 xarm_description/urdf/xarm_device.urdf.xacro: Use of invalid name(s):  __len__
when evaluating expression 'robot_sn.__len__()'
when evaluating expression 'robot_sn_len >= 14 and (robot_sn[0] == 'X' or robot_sn[0] == 'L')'

- Historical source compile failed ufactory_xarm7 467f381a3241753867fbf8e2c3647302716bc015 xarm_description/urdf/xarm_device.urdf.xacro: Error: inertia must satisfy A + B >= C; use 'balanceinertia' to fix
Element name 'link4', id 5

- Historical source compile failed ufactory_xarm7 9f263958f4df3223dd29f0c8176f9d8f48668ef5 xarm_description/urdf/xarm_device.urdf.xacro: Error: inertia must satisfy A + B >= C; use 'balanceinertia' to fix
Element name 'link4', id 5

- Historical source compile failed ufactory_xarm7 012b3ccf3d8ea5fe7db03a5cbdb9d9785a1d9b7c xarm_description/urdf/xarm_device.urdf.xacro: Use of invalid name(s):  __len__
when evaluating expression 'robot_sn.__len__()'
when evaluating expression 'robot_sn_len >= 14 and (robot_sn[0] == 'X' or robot_sn[0] == 'L')'

- Historical source compile failed ufactory_xarm7 00fcc0833845f12afaa85c1bafba4ec327078ce1 xarm_description/urdf/xarm_device.urdf.xacro: Error: inertia must satisfy A + B >= C; use 'balanceinertia' to fix
Element name 'link4', id 5

- Historical source compile failed ufactory_xarm7 d1d076e8bdb126016b29523bc19304dddf409151 xarm_description/urdf/xarm_device.urdf.xacro: Error: inertia must satisfy A + B >= C; use 'balanceinertia' to fix
Element name 'link4', id 5

- Historical source compile failed ufactory_xarm7 e027c47bf4d600f11f03bd2aa359d22bc8d9dfdd xarm_description/urdf/xarm_device.urdf.xacro: Use of invalid name(s):  __len__
when evaluating expression 'robot_sn.__len__()'
when evaluating expression 'robot_sn_len >= 14 and (robot_sn[0] == 'X' or robot_sn[0] == 'L')'

- A sandboxed `ps -p <survey-process> -o pid,pgid,ni,etime,rss,command` inspection failed with “operation not permitted”. No process was changed; progress remains available through the survey log. A later combined `rg` inspection named nonexistent `tests/test_acceptance.py`; actual test files were used instead.
- The final history-closure pass still reproduces the three STALE models. The independent XML reader now uses the common three-way registration anchor saved by the comparison. Report rendering saves resolved source-line links in JSON so published results remain reviewable without the ignored clones. Weekly runtime allowance is six hours because exhaustive dependency history can take longer than the original three-hour limit.

- Historical source compile failed ufactory_xarm7 91d6608a22d92f90202bfc6b81afc44f145d07be xarm_description/urdf/xarm_device.urdf.xacro: Error: inertia must satisfy A + B >= C; use 'balanceinertia' to fix
Element name 'link4', id 5

- New cache acquisition now starts with a `--filter=blob:none` clone, followed by a separately logged bounded small-blob bootstrap. Existing caches remain bounded partial clones; the earlier 100k clone filters are recorded in the original network log. `check --fetch` now explicitly refreshes existing manufacturer default branches before choosing H; offline runs keep their cached revisions. No network was performed by this code edit.

- https://github.com/unitreerobotics/unitree_ros robots/go1_description/xacro/leg.xacro at 157ff950351e5f535e03c5d85a16b7d594b3dbcc: ValueError: Macro leg requires unsupported explicit arguments: ['mirror', 'mirror_dae', 'front_hind', 'front_hind_dae']

- https://github.com/unitreerobotics/unitree_ros robots/go1_description/xacro/const.xacro at 157ff950351e5f535e03c5d85a16b7d594b3dbcc: ValueError: XML has no robot bodies; it is an include/extension fragment, not a standalone source

- https://github.com/unitreerobotics/unitree_ros robots/go1_description/xacro/gazebo.xacro at 157ff950351e5f535e03c5d85a16b7d594b3dbcc: ValueError: XML has no robot bodies; it is an include/extension fragment, not a standalone source

- https://github.com/unitreerobotics/unitree_ros robots/go1_description/xacro/materials.xacro at 157ff950351e5f535e03c5d85a16b7d594b3dbcc: ValueError: XML has no robot bodies; it is an include/extension fragment, not a standalone source

- https://github.com/unitreerobotics/unitree_ros robots/go1_description/xacro/ultraSound.xacro at 157ff950351e5f535e03c5d85a16b7d594b3dbcc: ValueError: XML Error: URDF joint parent or child missing
Element 'joint', line 1


- https://github.com/unitreerobotics/unitree_ros robots/go1_description/xacro/depthCamera.xacro at 157ff950351e5f535e03c5d85a16b7d594b3dbcc: ValueError: Macro depthCamera requires unsupported explicit arguments: ['camID']

- https://github.com/unitreerobotics/unitree_ros robots/go1_description/xacro/transmission.xacro at 157ff950351e5f535e03c5d85a16b7d594b3dbcc: ValueError: XML has no robot bodies; it is an include/extension fragment, not a standalone source

- https://github.com/unitreerobotics/unitree_ros robots/go2_description/xacro/leg.xacro at 157ff950351e5f535e03c5d85a16b7d594b3dbcc: ValueError: Macro leg requires unsupported explicit arguments: ['mirror', 'mirror_dae', 'front_hind', 'front_hind_dae']

- https://github.com/unitreerobotics/unitree_ros robots/go2_description/xacro/const.xacro at 157ff950351e5f535e03c5d85a16b7d594b3dbcc: ValueError: XML has no robot bodies; it is an include/extension fragment, not a standalone source

- https://github.com/unitreerobotics/unitree_ros robots/go2_description/xacro/robot.xacro at 157ff950351e5f535e03c5d85a16b7d594b3dbcc: ValueError: Resource missing at 157ff950351e5f535e03c5d85a16b7d594b3dbcc: robots/go2_description/xacro/robots/go2_description/meshes/trunk.dae

- https://github.com/unitreerobotics/unitree_ros robots/go2_description/xacro/gazebo.xacro at 157ff950351e5f535e03c5d85a16b7d594b3dbcc: ValueError: XML has no robot bodies; it is an include/extension fragment, not a standalone source

- https://github.com/unitreerobotics/unitree_ros robots/go2_description/xacro/materials.xacro at 157ff950351e5f535e03c5d85a16b7d594b3dbcc: ValueError: XML has no robot bodies; it is an include/extension fragment, not a standalone source

- https://github.com/unitreerobotics/unitree_ros robots/go2_description/xacro/transmission.xacro at 157ff950351e5f535e03c5d85a16b7d594b3dbcc: ValueError: XML has no robot bodies; it is an include/extension fragment, not a standalone source

- https://github.com/unitreerobotics/unitree_ros robots/z1_description/xacro/const.xacro at 157ff950351e5f535e03c5d85a16b7d594b3dbcc: ValueError: XML has no robot bodies; it is an include/extension fragment, not a standalone source

- https://github.com/unitreerobotics/unitree_ros robots/z1_description/xacro/gazebo.xacro at 157ff950351e5f535e03c5d85a16b7d594b3dbcc: ValueError: XML has no robot bodies; it is an include/extension fragment, not a standalone source

- https://github.com/unitreerobotics/unitree_ros robots/z1_description/xacro/transmission.xacro at 157ff950351e5f535e03c5d85a16b7d594b3dbcc: ValueError: XML has no robot bodies; it is an include/extension fragment, not a standalone source

- Historical source compile failed unitree_z1 6e033297dcf1fc9b4c73a900aa4f6fdea75d4ddd robots/z1_description/xacro/z1.urdf: Unresolved or ambiguous package path package://z1_description/meshes/z1_Link00.dae: []

- Offline Git read failed (exit 128): `('log', '--all', '--follow', '--find-renames=100%', '--format=@@@%H|%ct|%cI|%s', '--name-status', '--', 'ur_description/urdf/ur10e.xacro')` in `ros-industrial__universal_robot`. warning: lazy fetching disabled; some objects may not be available
fatal: could not fetch a6a41cf132c01f27239255594fef845f67bafc61 from promisor remote

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/ros-industrial__universal_robot -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `a6a41cf132c01f27239255594fef845f67bafc61`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('log', '--all', '--follow', '--find-renames=100%', '--format=@@@%H|%ct|%cI|%s', '--name-status', '--', 'ur_description/urdf/ur10e.xacro')` in `ros-industrial__universal_robot`. warning: lazy fetching disabled; some objects may not be available
fatal: could not fetch a49389857cc968fdb92e843cc672fc31022732aa from promisor remote

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/ros-industrial__universal_robot -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `a49389857cc968fdb92e843cc672fc31022732aa`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('log', '--all', '--follow', '--find-renames=100%', '--format=@@@%H|%ct|%cI|%s', '--name-status', '--', 'ur_description/urdf/ur10e.xacro')` in `ros-industrial__universal_robot`. warning: lazy fetching disabled; some objects may not be available
fatal: could not fetch 68fc0c696fe31dac5f2bc0264c64d668e171fc81 from promisor remote

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/ros-industrial__universal_robot -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `68fc0c696fe31dac5f2bc0264c64d668e171fc81`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('log', '--all', '--follow', '--find-renames=100%', '--format=@@@%H|%ct|%cI|%s', '--name-status', '--', 'ur_description/urdf/ur10e.xacro')` in `ros-industrial__universal_robot`. warning: lazy fetching disabled; some objects may not be available
fatal: could not fetch f3d4a509fa6c286ec32283d9a8e2cfac566bc7f4 from promisor remote

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/ros-industrial__universal_robot -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `f3d4a509fa6c286ec32283d9a8e2cfac566bc7f4`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('log', '--all', '--follow', '--find-renames=100%', '--format=@@@%H|%ct|%cI|%s', '--name-status', '--', 'ur_description/urdf/ur10e.xacro')` in `ros-industrial__universal_robot`. warning: lazy fetching disabled; some objects may not be available
fatal: could not fetch a7d8cdde3d8254ff409a0ba6510db2a010d16d5a from promisor remote

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/ros-industrial__universal_robot -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `a7d8cdde3d8254ff409a0ba6510db2a010d16d5a`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('log', '--all', '--follow', '--find-renames=100%', '--format=@@@%H|%ct|%cI|%s', '--name-status', '--', 'ur_description/urdf/ur10e.xacro')` in `ros-industrial__universal_robot`. warning: lazy fetching disabled; some objects may not be available
fatal: could not fetch 147d0ffb2b444e85501f9d3a08dfbff868884158 from promisor remote

- History coverage warning for https://github.com/ros-industrial/universal_robot ur_description/urdf/ur10e.xacro: Exact-rename traversal required unavailable unrelated blobs; current-path history was inspected, older renamed paths remain unresolved

- Offline Git read failed (exit 128): `('log', '--all', '--follow', '--find-renames=100%', '--format=@@@%H|%ct|%cI|%s', '--name-status', '--', 'ur_description/urdf/ur5e.xacro')` in `ros-industrial__universal_robot`. warning: lazy fetching disabled; some objects may not be available
fatal: could not fetch 147d0ffb2b444e85501f9d3a08dfbff868884158 from promisor remote

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/ros-industrial__universal_robot -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `147d0ffb2b444e85501f9d3a08dfbff868884158`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('log', '--all', '--follow', '--find-renames=100%', '--format=@@@%H|%ct|%cI|%s', '--name-status', '--', 'ur_description/urdf/ur5e.xacro')` in `ros-industrial__universal_robot`. warning: lazy fetching disabled; some objects may not be available
fatal: could not fetch bb46e96264fa0da1d532c3e7a0a09782b59a613f from promisor remote

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/ros-industrial__universal_robot -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `bb46e96264fa0da1d532c3e7a0a09782b59a613f`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('log', '--all', '--follow', '--find-renames=100%', '--format=@@@%H|%ct|%cI|%s', '--name-status', '--', 'ur_description/urdf/ur5e.xacro')` in `ros-industrial__universal_robot`. warning: lazy fetching disabled; some objects may not be available
fatal: could not fetch f607c2246f1759ea3e61d34157e6e33d6308e72c from promisor remote

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/ros-industrial__universal_robot -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `f607c2246f1759ea3e61d34157e6e33d6308e72c`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('log', '--all', '--follow', '--find-renames=100%', '--format=@@@%H|%ct|%cI|%s', '--name-status', '--', 'ur_description/urdf/ur5e.xacro')` in `ros-industrial__universal_robot`. warning: lazy fetching disabled; some objects may not be available
fatal: could not fetch b789be2878dcaacfc39f1ca0be1033de21b15dad from promisor remote

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/ros-industrial__universal_robot -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `b789be2878dcaacfc39f1ca0be1033de21b15dad`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('log', '--all', '--follow', '--find-renames=100%', '--format=@@@%H|%ct|%cI|%s', '--name-status', '--', 'ur_description/urdf/ur5e.xacro')` in `ros-industrial__universal_robot`. warning: lazy fetching disabled; some objects may not be available
fatal: could not fetch 81610ed617fdc177dacc7eb00341071b14e01cae from promisor remote

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -C .cache/ros-industrial__universal_robot -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `81610ed617fdc177dacc7eb00341071b14e01cae`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('log', '--all', '--follow', '--find-renames=100%', '--format=@@@%H|%ct|%cI|%s', '--name-status', '--', 'ur_description/urdf/ur5e.xacro')` in `ros-industrial__universal_robot`. warning: lazy fetching disabled; some objects may not be available
fatal: could not fetch 6c3bb2c6af7a6b32e442ab9e3bfb7496b7265472 from promisor remote

- History coverage warning for https://github.com/ros-industrial/universal_robot ur_description/urdf/ur5e.xacro: Exact-rename traversal required unavailable unrelated blobs; current-path history was inspected, older renamed paths remain unresolved

- https://github.com/simlabrobotics/allegro_hand_ros allegro_hand_description/allegro_hand_description_right.urdf at 296ef6bae4b535ffb91420237cdc8a87f6e9f6df: ValueError: Resource missing at 296ef6bae4b535ffb91420237cdc8a87f6e9f6df: allegro_hand_description/.unresolved_package/allegro_hand_description/meshes/base_link.STL

- https://github.com/simlabrobotics/allegro_hand_ros allegro_hand_description/allegro_hand_description_left.urdf at 296ef6bae4b535ffb91420237cdc8a87f6e9f6df: ValueError: Resource missing at 296ef6bae4b535ffb91420237cdc8a87f6e9f6df: allegro_hand_description/.unresolved_package/allegro_hand_description/meshes/base_link_left.STL

- https://github.com/simlabrobotics/allegro_hand_ros allegro_hand_description/allegro_hand_description_left.xacro at 296ef6bae4b535ffb91420237cdc8a87f6e9f6df: XacroException: unknown macro name: xacro:finger

- https://github.com/simlabrobotics/allegro_hand_ros allegro_hand_description/allegro_hand_description_right.xacro at 296ef6bae4b535ffb91420237cdc8a87f6e9f6df: XacroException: unknown macro name: xacro:finger

- Full dependency-history recheck completed for 28 models. The expanded inputs confirmed the three STALE models but exposed additional invalid historical revisions, now reported as partial coverage. One Allegro recheck revealed a resolver defect: legacy ROS package directories lacked package.xml. Added a unique local-directory fallback (recorded as expansion metadata), with a regression test; no host ROS search or external package download. Final targeted checks cover that resolver and the Crazyflie variant-link / CAD-only / no-standalone-descriptor discovery corrections.
- Regression suite before the final source-refresh/package-directory tests: 43 passed in 14.96 seconds. Final complete suite will be rerun after these corrections.

- Rejected unrelated historical README template for agilex_piper: 0bee963312f0f4a25b53cdf9afe744ca73f2d68a heading '## UMI-Gripper Description (MJCF)'

- Offline Git read failed (exit 128): `('show', '400b5f5b9fec382583f69b53b094a154d9dc7635:agilex_piper/CHANGELOG.md')` in `menagerie`. fatal: path 'agilex_piper/CHANGELOG.md' does not exist in '400b5f5b9fec382583f69b53b094a154d9dc7635'

- Rejected conflicting robot-variant link for anybotics_anymal_c: https://github.com/ANYbotics/anymal_b_simple_description/blob/master/urdf/anymal.urdf (repository variant b, model variant c)

- Offline Git read failed (exit 128): `('show', 'd9415a3076f921fdb9735d45d609a596df722468:apptronik_apollo/CHANGELOG.md')` in `menagerie`. fatal: bad object d9415a3076f921fdb9735d45d609a596df722468:apptronik_apollo/CHANGELOG.md

- Offline Git read failed (exit 128): `('show', '400b5f5b9fec382583f69b53b094a154d9dc7635:arx_l5/CHANGELOG.md')` in `menagerie`. fatal: path 'arx_l5/CHANGELOG.md' does not exist in '400b5f5b9fec382583f69b53b094a154d9dc7635'

- Offline Git read failed (exit 128): `('show', 'd9415a3076f921fdb9735d45d609a596df722468:berkeley_humanoid/CHANGELOG.md')` in `menagerie`. fatal: bad object d9415a3076f921fdb9735d45d609a596df722468:berkeley_humanoid/CHANGELOG.md

- Offline Git read failed (exit 128): `('show', 'd9415a3076f921fdb9735d45d609a596df722468:booster_t1/CHANGELOG.md')` in `menagerie`. fatal: bad object d9415a3076f921fdb9735d45d609a596df722468:booster_t1/CHANGELOG.md

- Offline Git read failed (exit 128): `('show', 'd9415a3076f921fdb9735d45d609a596df722468:fourier_n1/CHANGELOG.md')` in `menagerie`. fatal: bad object d9415a3076f921fdb9735d45d609a596df722468:fourier_n1/CHANGELOG.md

- Offline Git read failed (exit 128): `('show', '400b5f5b9fec382583f69b53b094a154d9dc7635:fourier_n1/CHANGELOG.md')` in `menagerie`. fatal: path 'fourier_n1/CHANGELOG.md' does not exist in '400b5f5b9fec382583f69b53b094a154d9dc7635'

- Offline Git read failed (exit 128): `('show', 'db140ade7ee4cb59629f9687aafc65af663d5bbe:franka_fr3_v2/README.md')` in `menagerie`. fatal: path 'franka_fr3_v2/README.md' does not exist in 'db140ade7ee4cb59629f9687aafc65af663d5bbe'

- Offline Git read failed (exit 128): `('show', 'cd7fc51b704c3cba05748bd5537cb17990b341eb:franka_fr3_v2/README.md')` in `menagerie`. fatal: path 'franka_fr3_v2/README.md' does not exist in 'cd7fc51b704c3cba05748bd5537cb17990b341eb'

- Offline Git read failed (exit 128): `('show', '400b5f5b9fec382583f69b53b094a154d9dc7635:franka_fr3_v2/README.md')` in `menagerie`. fatal: path 'franka_fr3_v2/README.md' does not exist in '400b5f5b9fec382583f69b53b094a154d9dc7635'

- Offline Git read failed (exit 128): `('show', 'acbbf1636fcfef9b437a6eb8c6f84380fb4aa998:franka_fr3_v2/README.md')` in `menagerie`. fatal: path 'franka_fr3_v2/README.md' does not exist in 'acbbf1636fcfef9b437a6eb8c6f84380fb4aa998'

- Offline Git read failed (exit 128): `('show', '7876dcdef0d912387441616526ed236142f047d3:franka_fr3_v2/README.md')` in `menagerie`. fatal: path 'franka_fr3_v2/README.md' does not exist in '7876dcdef0d912387441616526ed236142f047d3'

- Offline Git read failed (exit 128): `('show', 'b5ebfe0cf079d2b96acf0a5c0e29ee0c95ba32f4:google_robot/README.md')` in `menagerie`. fatal: path 'google_robot/README.md' does not exist in 'b5ebfe0cf079d2b96acf0a5c0e29ee0c95ba32f4'

- Offline Git read failed (exit 128): `('show', '5ce04bea98bbfca277a8d50b55ba3c7c4a62bdec:i2rt_yam/CHANGELOG.md')` in `menagerie`. fatal: path 'i2rt_yam/CHANGELOG.md' does not exist in '5ce04bea98bbfca277a8d50b55ba3c7c4a62bdec'

- Offline Git read failed (exit 128): `('show', 'a88bc450470d97ebc1f282e5969675fb4d1f0ed7:low_cost_robot_arm/README.md')` in `menagerie`. fatal: path 'low_cost_robot_arm/README.md' does not exist in 'a88bc450470d97ebc1f282e5969675fb4d1f0ed7'

- Offline Git read failed (exit 128): `('show', 'd74280a600a9afdfcb98d8917d0c79c86539aa61:low_cost_robot_arm/README.md')` in `menagerie`. fatal: path 'low_cost_robot_arm/README.md' does not exist in 'd74280a600a9afdfcb98d8917d0c79c86539aa61'

- Offline Git read failed (exit 128): `('show', '13d6c48b8f59d2c4badee7756b4ea3532613cddf:low_cost_robot_arm/README.md')` in `menagerie`. fatal: path 'low_cost_robot_arm/README.md' does not exist in '13d6c48b8f59d2c4badee7756b4ea3532613cddf'

- Offline Git read failed (exit 128): `('show', 'fae9ee82330444eec4e87568c838b99a09a39467:rainbow_robotics_rby1/README.md')` in `menagerie`. fatal: path 'rainbow_robotics_rby1/README.md' does not exist in 'fae9ee82330444eec4e87568c838b99a09a39467'

- Offline Git read failed (exit 128): `('show', '04674c8d0a4e12e33980a9e47fb604adc281fcc8:robotstudio_so101/CHANGELOG.md')` in `menagerie`. fatal: path 'robotstudio_so101/CHANGELOG.md' does not exist in '04674c8d0a4e12e33980a9e47fb604adc281fcc8'

- Offline Git read failed (exit 128): `('show', '5ce04bea98bbfca277a8d50b55ba3c7c4a62bdec:robotstudio_so101/CHANGELOG.md')` in `menagerie`. fatal: path 'robotstudio_so101/CHANGELOG.md' does not exist in '5ce04bea98bbfca277a8d50b55ba3c7c4a62bdec'

- Offline Git read failed (exit 128): `('show', '4a7015530bd7a4161103ae8f0905a96481e4cc1a:robotstudio_so101/CHANGELOG.md')` in `menagerie`. fatal: path 'robotstudio_so101/CHANGELOG.md' does not exist in '4a7015530bd7a4161103ae8f0905a96481e4cc1a'

- Offline Git read failed (exit 128): `('show', 'bf110a75a56e5bd146c7ed76965737c71d48425d:shadow_dexee/README.md')` in `menagerie`. fatal: path 'shadow_dexee/README.md' does not exist in 'bf110a75a56e5bd146c7ed76965737c71d48425d'

- Offline Git read failed (exit 128): `('show', '04674c8d0a4e12e33980a9e47fb604adc281fcc8:tetheria_aero_hand_open/CHANGELOG.md')` in `menagerie`. fatal: path 'tetheria_aero_hand_open/CHANGELOG.md' does not exist in '04674c8d0a4e12e33980a9e47fb604adc281fcc8'

- Offline Git read failed (exit 128): `('show', '400b5f5b9fec382583f69b53b094a154d9dc7635:tetheria_aero_hand_open/CHANGELOG.md')` in `menagerie`. fatal: path 'tetheria_aero_hand_open/CHANGELOG.md' does not exist in '400b5f5b9fec382583f69b53b094a154d9dc7635'

- Offline Git read failed (exit 128): `('show', '04674c8d0a4e12e33980a9e47fb604adc281fcc8:toddlerbot_2xc/CHANGELOG.md')` in `menagerie`. fatal: path 'toddlerbot_2xc/CHANGELOG.md' does not exist in '04674c8d0a4e12e33980a9e47fb604adc281fcc8'

- Offline Git read failed (exit 128): `('show', '9e7f8d4dda07f5c281b6c0c6f0d07b9dd267b762:toddlerbot_2xc/CHANGELOG.md')` in `menagerie`. fatal: path 'toddlerbot_2xc/CHANGELOG.md' does not exist in '9e7f8d4dda07f5c281b6c0c6f0d07b9dd267b762'

- Offline Git read failed (exit 128): `('show', '400b5f5b9fec382583f69b53b094a154d9dc7635:toddlerbot_2xc/CHANGELOG.md')` in `menagerie`. fatal: path 'toddlerbot_2xc/CHANGELOG.md' does not exist in '400b5f5b9fec382583f69b53b094a154d9dc7635'

- Offline Git read failed (exit 128): `('show', '04674c8d0a4e12e33980a9e47fb604adc281fcc8:toddlerbot_2xm/CHANGELOG.md')` in `menagerie`. fatal: path 'toddlerbot_2xm/CHANGELOG.md' does not exist in '04674c8d0a4e12e33980a9e47fb604adc281fcc8'

- Offline Git read failed (exit 128): `('show', '9e7f8d4dda07f5c281b6c0c6f0d07b9dd267b762:toddlerbot_2xm/CHANGELOG.md')` in `menagerie`. fatal: path 'toddlerbot_2xm/CHANGELOG.md' does not exist in '9e7f8d4dda07f5c281b6c0c6f0d07b9dd267b762'

- Offline Git read failed (exit 128): `('show', '400b5f5b9fec382583f69b53b094a154d9dc7635:toddlerbot_2xm/CHANGELOG.md')` in `menagerie`. fatal: path 'toddlerbot_2xm/CHANGELOG.md' does not exist in '400b5f5b9fec382583f69b53b094a154d9dc7635'

- Offline Git read failed (exit 128): `('show', '400b5f5b9fec382583f69b53b094a154d9dc7635:trossen_wxai/README.md')` in `menagerie`. fatal: path 'trossen_wxai/README.md' does not exist in '400b5f5b9fec382583f69b53b094a154d9dc7635'

- Offline Git read failed (exit 128): `('show', '477ec56566682d663b996d86a188c75499e74b98:trossen_wxai/README.md')` in `menagerie`. fatal: path 'trossen_wxai/README.md' does not exist in '477ec56566682d663b996d86a188c75499e74b98'

- Offline Git read failed (exit 128): `('show', 'd9415a3076f921fdb9735d45d609a596df722468:unitree_g1/CHANGELOG.md')` in `menagerie`. fatal: bad object d9415a3076f921fdb9735d45d609a596df722468:unitree_g1/CHANGELOG.md

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -c gc.auto=0 -c maintenance.auto=false -C .cache/whoenig__crazyflie_ros fetch --filter=blob:none --no-tags origin HEAD '+refs/heads/*:refs/remotes/origin/*'` — refresh the upstream branch tips before selecting latest H. Parent process runs at nice 15; lazy fetching disabled.

- Network outcome: exit 0. From https://github.com/whoenig/crazyflie_ros
 * branch            HEAD       -> FETCH_HEAD

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -c gc.auto=0 -c maintenance.auto=false -C .cache/rhoban__bam fetch --filter=blob:none --no-tags origin HEAD '+refs/heads/*:refs/remotes/origin/*'` — refresh the upstream branch tips before selecting latest H. Parent process runs at nice 15; lazy fetching disabled.

- Network outcome: exit 0. From https://github.com/rhoban/bam
 * branch            HEAD       -> FETCH_HEAD

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -c gc.auto=0 -c maintenance.auto=false -C .cache/simlabrobotics__allegro_hand_ros fetch --filter=blob:none --no-tags origin HEAD '+refs/heads/*:refs/remotes/origin/*'` — refresh the upstream branch tips before selecting latest H. Parent process runs at nice 15; lazy fetching disabled.

- Network outcome: exit 0. From https://github.com/simlabrobotics/allegro_hand_ros
 * branch            HEAD       -> FETCH_HEAD

- https://github.com/simlabrobotics/allegro_hand_ros allegro_hand_description/allegro_hand_description_left.xacro at 296ef6bae4b535ffb91420237cdc8a87f6e9f6df: XacroException: unknown macro name: xacro:finger

- https://github.com/simlabrobotics/allegro_hand_ros allegro_hand_description/allegro_hand_description_right.xacro at 296ef6bae4b535ffb91420237cdc8a87f6e9f6df: XacroException: unknown macro name: xacro:finger

- Offline Git read failed (exit 128): `('log', '--all', '--follow', '--find-renames=100%', '--format=@@@%H|%ct|%cI|%s', '--name-status', '--', 'allegro_hand_description/allegro_hand_description_right.urdf')` in `simlabrobotics__allegro_hand_ros`. warning: lazy fetching disabled; some objects may not be available
fatal: could not fetch ec2254144f03132c1acba6f3772fc22965a3d1d5 from promisor remote

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -c gc.auto=0 -c maintenance.auto=false -C .cache/simlabrobotics__allegro_hand_ros -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `ec2254144f03132c1acba6f3772fc22965a3d1d5`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('log', '--all', '--follow', '--find-renames=100%', '--format=@@@%H|%ct|%cI|%s', '--name-status', '--', 'allegro_hand_description/allegro_hand_description_right.urdf')` in `simlabrobotics__allegro_hand_ros`. warning: lazy fetching disabled; some objects may not be available
fatal: could not fetch f6ae09ad124b1d22f7707adb498be224e6a00119 from promisor remote

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -c gc.auto=0 -c maintenance.auto=false -C .cache/simlabrobotics__allegro_hand_ros -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `f6ae09ad124b1d22f7707adb498be224e6a00119`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('log', '--all', '--follow', '--find-renames=100%', '--format=@@@%H|%ct|%cI|%s', '--name-status', '--', 'allegro_hand_description/allegro_hand_description_right.urdf')` in `simlabrobotics__allegro_hand_ros`. warning: lazy fetching disabled; some objects may not be available
fatal: could not fetch 9b6bc549b531b4361f1d103107c61163866215c9 from promisor remote

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -c gc.auto=0 -c maintenance.auto=false -C .cache/simlabrobotics__allegro_hand_ros -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `9b6bc549b531b4361f1d103107c61163866215c9`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('log', '--all', '--follow', '--find-renames=100%', '--format=@@@%H|%ct|%cI|%s', '--name-status', '--', 'allegro_hand_description/allegro_hand_description_right.urdf')` in `simlabrobotics__allegro_hand_ros`. warning: lazy fetching disabled; some objects may not be available
fatal: could not fetch 0a04f194e8c27742a9aed243f104502638466d99 from promisor remote

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -c gc.auto=0 -c maintenance.auto=false -C .cache/simlabrobotics__allegro_hand_ros -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `0a04f194e8c27742a9aed243f104502638466d99`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('log', '--all', '--follow', '--find-renames=100%', '--format=@@@%H|%ct|%cI|%s', '--name-status', '--', 'allegro_hand_description/allegro_hand_description_right.urdf')` in `simlabrobotics__allegro_hand_ros`. warning: lazy fetching disabled; some objects may not be available
fatal: could not fetch 2ea47729168de3a81103ccfdf732098ba725e2ec from promisor remote

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -c gc.auto=0 -c maintenance.auto=false -C .cache/simlabrobotics__allegro_hand_ros -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `2ea47729168de3a81103ccfdf732098ba725e2ec`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('log', '--all', '--follow', '--find-renames=100%', '--format=@@@%H|%ct|%cI|%s', '--name-status', '--', 'allegro_hand_description/allegro_hand_description_right.urdf')` in `simlabrobotics__allegro_hand_ros`. warning: lazy fetching disabled; some objects may not be available
fatal: could not fetch 94a37a1a80c729e7a8b42132d35d5f5e95ed5ff3 from promisor remote

- History coverage warning for https://github.com/simlabrobotics/allegro_hand_ros allegro_hand_description/allegro_hand_description_right.urdf: Exact-rename traversal required unavailable unrelated blobs; current-path history was inspected, older renamed paths remain unresolved

- Final classification refresh re-evaluated saved compiled snapshots with the common three-way frame, configured tolerances and amended provenance selector; no physical values were invented or replaced. Source-reference caches will be rebuilt by report rendering.

- Final numeric/classification snapshot: all 71 folders listed, 47 with a compiled M/H comparison, 119 standalone self-comparisons passed. Statuses: 30 complete, 17 partial history, 19 unknown upstream, 5 current-source compilation gaps. Provenance: 7 pinned, 13 dated match, 0 proxy, 15 none, 36 unknown. Findings: 350 NO MATCHING SOURCE, 92 undocumented derivation differences, 200 unknown, 20 STALE, 11 needs a human look (673 total quantity records). Half tolerance: 689 records, 16 membership changes, 7 label changes, 20 STALE. Double: 654 records, 19 membership changes, 4 label changes, 19 STALE.
- `nice -n 15 ./drift acceptance` passed and saved report/acceptance.json with the fixed nine-revision fixture and NO MATCHING SOURCE. `.venv/bin/python -m pip check` found no broken requirements; pip warned that its default user cache is not writable and disabled it. No install or network was performed by that check.

- Direct XML random cross-checks: 3 selected, seed 20261113; agreements [True, True, True]; skipped draws 0.

- Additional direct XML audit of every STALE record: 20/20 agree. See report/stale_cross_checks.json for all raw values/errors.

- Final verification: `nice -n 15 env OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 .venv/bin/python -m pytest -q` — **47 passed in 14.58 seconds**, including real H1, all-survey self-comparisons and the added proxy/no-match tests.
- Required random independent check: `nice -n 15 ./drift cross-check` — **3/3 agree**, seed 20261113, all 673 reported findings shuffled, zero skipped draws. Selected UR10e wrist_1_link principal moments, H1 pelvis principal moments and Franka FR3 link7 subtree mass. No MuJoCo import in the independent extractor.
- Additional independent audit (`nice -n 15 ... .venv/bin/python .cache/audit_stale.py`): **20/20 STALE records agree** in direct XML M/S/H values and resulting class. This includes every CoM/inertia and every effort declaration, independently of the required random sample. Full raw values saved in report/stale_cross_checks.json.

- A final low-coverage audit probe failed with ModuleNotFoundError because PYTHONPATH=src was omitted; reran with the project import path. The probe identified two Robotiq source candidates that instantiated a fixed base macro rather than the full gripper. These are not valid whole-robot comparisons and must be corrected or explicitly treated as coverage gaps before delivery.

- Rejected unrelated historical README template for agilex_piper: 0bee963312f0f4a25b53cdf9afe744ca73f2d68a heading '## UMI-Gripper Description (MJCF)'

- Offline Git read failed (exit 128): `('show', '400b5f5b9fec382583f69b53b094a154d9dc7635:agilex_piper/CHANGELOG.md')` in `menagerie`. fatal: path 'agilex_piper/CHANGELOG.md' does not exist in '400b5f5b9fec382583f69b53b094a154d9dc7635'

- Rejected conflicting robot-variant link for anybotics_anymal_c: https://github.com/ANYbotics/anymal_b_simple_description/blob/master/urdf/anymal.urdf (repository variant b, model variant c)

- Offline Git read failed (exit 128): `('show', 'd9415a3076f921fdb9735d45d609a596df722468:apptronik_apollo/CHANGELOG.md')` in `menagerie`. fatal: bad object d9415a3076f921fdb9735d45d609a596df722468:apptronik_apollo/CHANGELOG.md

- Offline Git read failed (exit 128): `('show', '400b5f5b9fec382583f69b53b094a154d9dc7635:arx_l5/CHANGELOG.md')` in `menagerie`. fatal: path 'arx_l5/CHANGELOG.md' does not exist in '400b5f5b9fec382583f69b53b094a154d9dc7635'

- Offline Git read failed (exit 128): `('show', 'd9415a3076f921fdb9735d45d609a596df722468:berkeley_humanoid/CHANGELOG.md')` in `menagerie`. fatal: bad object d9415a3076f921fdb9735d45d609a596df722468:berkeley_humanoid/CHANGELOG.md

- Offline Git read failed (exit 128): `('show', 'd9415a3076f921fdb9735d45d609a596df722468:booster_t1/CHANGELOG.md')` in `menagerie`. fatal: bad object d9415a3076f921fdb9735d45d609a596df722468:booster_t1/CHANGELOG.md

- Offline Git read failed (exit 128): `('show', 'd9415a3076f921fdb9735d45d609a596df722468:fourier_n1/CHANGELOG.md')` in `menagerie`. fatal: bad object d9415a3076f921fdb9735d45d609a596df722468:fourier_n1/CHANGELOG.md

- Offline Git read failed (exit 128): `('show', '400b5f5b9fec382583f69b53b094a154d9dc7635:fourier_n1/CHANGELOG.md')` in `menagerie`. fatal: path 'fourier_n1/CHANGELOG.md' does not exist in '400b5f5b9fec382583f69b53b094a154d9dc7635'

- Offline Git read failed (exit 128): `('show', 'db140ade7ee4cb59629f9687aafc65af663d5bbe:franka_fr3_v2/README.md')` in `menagerie`. fatal: path 'franka_fr3_v2/README.md' does not exist in 'db140ade7ee4cb59629f9687aafc65af663d5bbe'

- Offline Git read failed (exit 128): `('show', 'cd7fc51b704c3cba05748bd5537cb17990b341eb:franka_fr3_v2/README.md')` in `menagerie`. fatal: path 'franka_fr3_v2/README.md' does not exist in 'cd7fc51b704c3cba05748bd5537cb17990b341eb'

- Offline Git read failed (exit 128): `('show', '400b5f5b9fec382583f69b53b094a154d9dc7635:franka_fr3_v2/README.md')` in `menagerie`. fatal: path 'franka_fr3_v2/README.md' does not exist in '400b5f5b9fec382583f69b53b094a154d9dc7635'

- Offline Git read failed (exit 128): `('show', 'acbbf1636fcfef9b437a6eb8c6f84380fb4aa998:franka_fr3_v2/README.md')` in `menagerie`. fatal: path 'franka_fr3_v2/README.md' does not exist in 'acbbf1636fcfef9b437a6eb8c6f84380fb4aa998'

- Offline Git read failed (exit 128): `('show', '7876dcdef0d912387441616526ed236142f047d3:franka_fr3_v2/README.md')` in `menagerie`. fatal: path 'franka_fr3_v2/README.md' does not exist in '7876dcdef0d912387441616526ed236142f047d3'

- Offline Git read failed (exit 128): `('show', 'b5ebfe0cf079d2b96acf0a5c0e29ee0c95ba32f4:google_robot/README.md')` in `menagerie`. fatal: path 'google_robot/README.md' does not exist in 'b5ebfe0cf079d2b96acf0a5c0e29ee0c95ba32f4'

- Offline Git read failed (exit 128): `('show', '5ce04bea98bbfca277a8d50b55ba3c7c4a62bdec:i2rt_yam/CHANGELOG.md')` in `menagerie`. fatal: path 'i2rt_yam/CHANGELOG.md' does not exist in '5ce04bea98bbfca277a8d50b55ba3c7c4a62bdec'

- Offline Git read failed (exit 128): `('show', 'a88bc450470d97ebc1f282e5969675fb4d1f0ed7:low_cost_robot_arm/README.md')` in `menagerie`. fatal: path 'low_cost_robot_arm/README.md' does not exist in 'a88bc450470d97ebc1f282e5969675fb4d1f0ed7'

- Offline Git read failed (exit 128): `('show', 'd74280a600a9afdfcb98d8917d0c79c86539aa61:low_cost_robot_arm/README.md')` in `menagerie`. fatal: path 'low_cost_robot_arm/README.md' does not exist in 'd74280a600a9afdfcb98d8917d0c79c86539aa61'

- Offline Git read failed (exit 128): `('show', '13d6c48b8f59d2c4badee7756b4ea3532613cddf:low_cost_robot_arm/README.md')` in `menagerie`. fatal: path 'low_cost_robot_arm/README.md' does not exist in '13d6c48b8f59d2c4badee7756b4ea3532613cddf'

- Offline Git read failed (exit 128): `('show', 'fae9ee82330444eec4e87568c838b99a09a39467:rainbow_robotics_rby1/README.md')` in `menagerie`. fatal: path 'rainbow_robotics_rby1/README.md' does not exist in 'fae9ee82330444eec4e87568c838b99a09a39467'

- Offline Git read failed (exit 128): `('show', '04674c8d0a4e12e33980a9e47fb604adc281fcc8:robotstudio_so101/CHANGELOG.md')` in `menagerie`. fatal: path 'robotstudio_so101/CHANGELOG.md' does not exist in '04674c8d0a4e12e33980a9e47fb604adc281fcc8'

- Offline Git read failed (exit 128): `('show', '5ce04bea98bbfca277a8d50b55ba3c7c4a62bdec:robotstudio_so101/CHANGELOG.md')` in `menagerie`. fatal: path 'robotstudio_so101/CHANGELOG.md' does not exist in '5ce04bea98bbfca277a8d50b55ba3c7c4a62bdec'

- Offline Git read failed (exit 128): `('show', '4a7015530bd7a4161103ae8f0905a96481e4cc1a:robotstudio_so101/CHANGELOG.md')` in `menagerie`. fatal: path 'robotstudio_so101/CHANGELOG.md' does not exist in '4a7015530bd7a4161103ae8f0905a96481e4cc1a'

- Offline Git read failed (exit 128): `('show', 'bf110a75a56e5bd146c7ed76965737c71d48425d:shadow_dexee/README.md')` in `menagerie`. fatal: path 'shadow_dexee/README.md' does not exist in 'bf110a75a56e5bd146c7ed76965737c71d48425d'

- Offline Git read failed (exit 128): `('show', '04674c8d0a4e12e33980a9e47fb604adc281fcc8:tetheria_aero_hand_open/CHANGELOG.md')` in `menagerie`. fatal: path 'tetheria_aero_hand_open/CHANGELOG.md' does not exist in '04674c8d0a4e12e33980a9e47fb604adc281fcc8'

- Offline Git read failed (exit 128): `('show', '400b5f5b9fec382583f69b53b094a154d9dc7635:tetheria_aero_hand_open/CHANGELOG.md')` in `menagerie`. fatal: path 'tetheria_aero_hand_open/CHANGELOG.md' does not exist in '400b5f5b9fec382583f69b53b094a154d9dc7635'

- Offline Git read failed (exit 128): `('show', '04674c8d0a4e12e33980a9e47fb604adc281fcc8:toddlerbot_2xc/CHANGELOG.md')` in `menagerie`. fatal: path 'toddlerbot_2xc/CHANGELOG.md' does not exist in '04674c8d0a4e12e33980a9e47fb604adc281fcc8'

- Offline Git read failed (exit 128): `('show', '9e7f8d4dda07f5c281b6c0c6f0d07b9dd267b762:toddlerbot_2xc/CHANGELOG.md')` in `menagerie`. fatal: path 'toddlerbot_2xc/CHANGELOG.md' does not exist in '9e7f8d4dda07f5c281b6c0c6f0d07b9dd267b762'

- Offline Git read failed (exit 128): `('show', '400b5f5b9fec382583f69b53b094a154d9dc7635:toddlerbot_2xc/CHANGELOG.md')` in `menagerie`. fatal: path 'toddlerbot_2xc/CHANGELOG.md' does not exist in '400b5f5b9fec382583f69b53b094a154d9dc7635'

- Offline Git read failed (exit 128): `('show', '04674c8d0a4e12e33980a9e47fb604adc281fcc8:toddlerbot_2xm/CHANGELOG.md')` in `menagerie`. fatal: path 'toddlerbot_2xm/CHANGELOG.md' does not exist in '04674c8d0a4e12e33980a9e47fb604adc281fcc8'

- Offline Git read failed (exit 128): `('show', '9e7f8d4dda07f5c281b6c0c6f0d07b9dd267b762:toddlerbot_2xm/CHANGELOG.md')` in `menagerie`. fatal: path 'toddlerbot_2xm/CHANGELOG.md' does not exist in '9e7f8d4dda07f5c281b6c0c6f0d07b9dd267b762'

- Offline Git read failed (exit 128): `('show', '400b5f5b9fec382583f69b53b094a154d9dc7635:toddlerbot_2xm/CHANGELOG.md')` in `menagerie`. fatal: path 'toddlerbot_2xm/CHANGELOG.md' does not exist in '400b5f5b9fec382583f69b53b094a154d9dc7635'

- Offline Git read failed (exit 128): `('show', '400b5f5b9fec382583f69b53b094a154d9dc7635:trossen_wxai/README.md')` in `menagerie`. fatal: path 'trossen_wxai/README.md' does not exist in '400b5f5b9fec382583f69b53b094a154d9dc7635'

- Offline Git read failed (exit 128): `('show', '477ec56566682d663b996d86a188c75499e74b98:trossen_wxai/README.md')` in `menagerie`. fatal: path 'trossen_wxai/README.md' does not exist in '477ec56566682d663b996d86a188c75499e74b98'

- Offline Git read failed (exit 128): `('show', 'd9415a3076f921fdb9735d45d609a596df722468:unitree_g1/CHANGELOG.md')` in `menagerie`. fatal: bad object d9415a3076f921fdb9735d45d609a596df722468:unitree_g1/CHANGELOG.md

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -c gc.auto=0 -c maintenance.auto=false -C .cache/ros-industrial__robotiq fetch --filter=blob:none --no-tags origin HEAD '+refs/heads/*:refs/remotes/origin/*'` — refresh the upstream branch tips before selecting latest H. Parent process runs at nice 15; lazy fetching disabled.

- Network outcome: exit 0. From https://github.com/ros-industrial/robotiq
 * branch            HEAD       -> FETCH_HEAD

- https://github.com/ros-industrial/robotiq robotiq_2f_85_gripper_visualization/urdf/robotiq_arg2f_transmission.xacro at 45196f6558fe8ba9d89bc8a105396c68c3e7e892: ValueError: XML has no robot bodies; it is an include/extension fragment, not a standalone source

- https://github.com/ros-industrial/robotiq robotiq_2f_85_gripper_visualization/urdf/robotiq_arg2f_85_model_macro.xacro at 45196f6558fe8ba9d89bc8a105396c68c3e7e892: ValueError: Macro-only input has no uniquely identified robot macro

- Offline Git read failed (exit 128): `('log', '--all', '--follow', '--find-renames=100%', '--format=@@@%H|%ct|%cI|%s', '--name-status', '--', 'robotiq_2f_85_gripper_visualization/urdf/robotiq_arg2f_85_model.xacro')` in `ros-industrial__robotiq`. warning: lazy fetching disabled; some objects may not be available
fatal: could not fetch cebd4c2a281fd473a319d57bc7782d7f2470a386 from promisor remote

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -c gc.auto=0 -c maintenance.auto=false -C .cache/ros-industrial__robotiq -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `cebd4c2a281fd473a319d57bc7782d7f2470a386`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('log', '--all', '--follow', '--find-renames=100%', '--format=@@@%H|%ct|%cI|%s', '--name-status', '--', 'robotiq_2f_85_gripper_visualization/urdf/robotiq_arg2f_85_model.xacro')` in `ros-industrial__robotiq`. warning: lazy fetching disabled; some objects may not be available
fatal: could not fetch c4bffda1a5e6b1d10911dea67e9a0617417cfb52 from promisor remote

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -c gc.auto=0 -c maintenance.auto=false -C .cache/ros-industrial__robotiq -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `c4bffda1a5e6b1d10911dea67e9a0617417cfb52`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('log', '--all', '--follow', '--find-renames=100%', '--format=@@@%H|%ct|%cI|%s', '--name-status', '--', 'robotiq_2f_85_gripper_visualization/urdf/robotiq_arg2f_85_model.xacro')` in `ros-industrial__robotiq`. warning: lazy fetching disabled; some objects may not be available
fatal: could not fetch eee411244cf1c3968134a2bad5c308287391c86f from promisor remote

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -c gc.auto=0 -c maintenance.auto=false -C .cache/ros-industrial__robotiq -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `eee411244cf1c3968134a2bad5c308287391c86f`

- Network outcome: exit 0.

- Offline Git read failed (exit 128): `('log', '--all', '--follow', '--find-renames=100%', '--format=@@@%H|%ct|%cI|%s', '--name-status', '--', 'robotiq_2f_85_gripper_visualization/urdf/robotiq_arg2f_85_model.xacro')` in `ros-industrial__robotiq`. warning: lazy fetching disabled; some objects may not be available
fatal: could not fetch 3723af04c15aea30234a540172f84fa6ca8b0c38 from promisor remote

- Network command `git -c pack.threads=1 -c index.threads=1 -c fetch.parallel=1 -c gc.auto=0 -c maintenance.auto=false -C .cache/ros-industrial__robotiq -c fetch.negotiationAlgorithm=noop fetch origin --no-tags --no-write-fetch-head --recurse-submodules=no --filter=blob:none --stdin` — retrieve only specifically required source/resource blobs using the promisor-fetch protocol. Parent process runs at nice 15; lazy fetching disabled.

- Network command stdin object IDs: `3723af04c15aea30234a540172f84fa6ca8b0c38`

- Network outcome: exit 0.

- https://github.com/ros-industrial/robotiq robotiq_2f_85_gripper_visualization/urdf/robotiq_arg2f_transmission.xacro at 45196f6558fe8ba9d89bc8a105396c68c3e7e892: ValueError: XML has no robot bodies; it is an include/extension fragment, not a standalone source

- https://github.com/ros-industrial/robotiq robotiq_2f_85_gripper_visualization/urdf/robotiq_arg2f_85_model_macro.xacro at 45196f6558fe8ba9d89bc8a105396c68c3e7e892: ValueError: Macro-only input has no uniquely identified robot macro

- Final classification refresh re-evaluated saved compiled snapshots with the common three-way frame, configured tolerances and amended provenance selector; no physical values were invented or replaced. Source-reference caches will be rebuilt by report rendering.

- Final Robotiq correction: complete moving gripper entry selected in both folders by preferring mobility-compatible source assemblies before numeric coverage ties. Both now compile through history and receive NO MATCHING SOURCE, with two aggregate differences each; no physical-body mappings were invented. This supersedes their former fixed-helper comparisons. Final statuses: **32 complete, 15 partial history, 19 unknown upstream, 5 incomplete**. Final provenance: **7 pinned, 13 dated match, 17 none, 34 unknown**. Final class totals: **354 NO MATCHING SOURCE, 92 undocumented derivation differences, 196 unknown, 20 STALE, 11 needs a human look**. Total record and tolerance sensitivity counts remain unchanged. Added a regression requiring complete moving Robotiq models.

- Direct XML random cross-checks: 3 selected, seed 20261113; agreements [True, True, True]; skipped draws 0.

- The added Robotiq regression initially failed: it incorrectly required the source to have at least as many moving joints as Menagerie (source 6 versus Menagerie 8). Closed-loop conversion can change that count. The source selection was correct: the complete model has 11 bodies and six moving joints. Corrected the regression to require articulation and both left/right finger branches, which the formerly selected fixed base helper lacked. This is a test-assumption correction, not a replacement of any measured value. The failed run was 1 failed / 47 passed in 14.98 seconds.

- Final source-link audit: all STALE links already resolved, but 82 other generated Franka/Trossen references still pointed to unresolved wrapper locations. Added a separate annotated xacro expansion for provenance links only (never compiled), carrying original declaration locations through parameterized macros; YAML field links identify numeric inputs. Also substitute the recorded $(arg ...) bindings when locating source names. No physical compilation input or measured result is changed by this report-only trace. Added a synthetic source-map regression.

- Annotated source-location pass relinked 6 models; unresolved finding references remaining: 0. See report/source_link_audit.json.

- Final offline artifact validation: {"model_reports": 71, "provenance_files": 71, "source_link_occurrences": 1494, "unique_source_line_targets_checked": 1019, "unresolved_finding_source_references": 0, "all_link_targets_exist_at_exact_shas": true, "workflow_yaml_valid": true}

- Summary upstream-change column uses selected S when available, otherwise the earliest successfully compiled public revision. Its baseline is now stated explicitly in summary.md; three-way findings are unchanged.

- Final source-link audit resolved all generated identities: **0 unresolved finding references**. Offline validation checked **1,494 source-link occurrences / 1,019 unique source-line targets**, verifying each file and line exists at its full SHA. There are 71 model reports and 71 provenance YAMLs; the weekly YAML parses with read-only contents permission and was not run remotely.
- Final full test suite after the source-map regression: **49 passed in 14.46 seconds**. The final three seeded direct XML checks still agree 3/3 with zero skipped draws. The additional all-STALE audit remains 20/20; source-link and summary-only edits do not alter physical values or findings.
- Removed the temporary tracked-candidate repair script; reproducible public entry points are the drift CLI and tests. Exploratory/finalization utilities and raw console logs remain in ignored .cache for this local investigation. The external publication draft intentionally contains a publication URL placeholder and a conditional owner review statement: no published repository URL or completed human review is invented.

- Final resource and repository inspection: `du -sh .` **3.0 GiB**; `df -h .` completed, below the 15 GB project limit. `git rev-list --all --count` **0**; `git diff --cached --stat` empty. All deliverables remain unstaged/uncommitted, and ignored clones/environment are not publication files. No push, issue, comment, pull request, external message, GPU or MLX action was performed. All work remained inside this project; another job was running on this machine and was not accessed. Final offline rendering succeeded for all 71 model reports and summary.md.

## 2026-11-13 — kinematic convention checks and first local commit

- Added Kabsch zero-pose body-origin alignment and matched-axis consistency checks, CoM exclusion for convention mismatches, survey/test/XML reruns and refreshed publication files before the first local commit. The initial identity check paused the work; configured name Dorian and the public GitHub noreply address were verified before continuing without changing Git identity. No push was performed.
- Initial resource check completed; 3.0 GiB project use. Git remains uncommitted. `rg --files -g AGENTS.md` found no applicable file and returned status 1; resource and Git checks succeeded. Preserved the previous measured results and H1 acceptance JSON in ignored .cache for exact before/after checks.

- Preliminary Kabsch measurements on saved zero-pose snapshots: UR5e RMS 64.131 mm, UR10e 77.453 mm, RBY1 16.278 mm with opposed axes. Panda has only one matched origin, insufficient to certify a unique rigid alignment. Added explicit insufficient-coverage status and CoM exclusion for underdetermined fits as well as the convention-differs guard. Default guard is 5 mm RMS and 0.005 rad signed-axis angle; both configurable and fixed during physical half/double tolerance sensitivity.
- Synthetic check initially failed 1/53 because a test modified the shared compiler-cache snapshot, contaminating a later test. Isolated each synthetic cloud with a deep copy; production comparisons do not mutate snapshots. No measured model value was changed.
- Rerun mode recompiles all Menagerie self-test variants and each available primary M/S/H at the saved commits, asserts physical values match the earlier compiles, then reevaluates provenance, kinematic guards and sensitivity using saved historical compiler snapshots. This avoids refetching or recompiling unchanged historical inputs. Original raw-value provenance criteria are retained so independent mass/inertia classifications do not change just because of the new CoM guard.

- Rejected unrelated historical README template for agilex_piper: 0bee963312f0f4a25b53cdf9afe744ca73f2d68a heading '## UMI-Gripper Description (MJCF)'

- Offline Git read failed (exit 128): `('show', '400b5f5b9fec382583f69b53b094a154d9dc7635:agilex_piper/CHANGELOG.md')` in `menagerie`. fatal: path 'agilex_piper/CHANGELOG.md' does not exist in '400b5f5b9fec382583f69b53b094a154d9dc7635'

- Rejected conflicting robot-variant link for anybotics_anymal_c: https://github.com/ANYbotics/anymal_b_simple_description/blob/master/urdf/anymal.urdf (repository variant b, model variant c)

- Offline Git read failed (exit 128): `('show', 'd9415a3076f921fdb9735d45d609a596df722468:apptronik_apollo/CHANGELOG.md')` in `menagerie`. fatal: bad object d9415a3076f921fdb9735d45d609a596df722468:apptronik_apollo/CHANGELOG.md

- Offline Git read failed (exit 128): `('show', '400b5f5b9fec382583f69b53b094a154d9dc7635:arx_l5/CHANGELOG.md')` in `menagerie`. fatal: path 'arx_l5/CHANGELOG.md' does not exist in '400b5f5b9fec382583f69b53b094a154d9dc7635'

- Offline Git read failed (exit 128): `('show', 'd9415a3076f921fdb9735d45d609a596df722468:berkeley_humanoid/CHANGELOG.md')` in `menagerie`. fatal: bad object d9415a3076f921fdb9735d45d609a596df722468:berkeley_humanoid/CHANGELOG.md

- Offline Git read failed (exit 128): `('show', 'd9415a3076f921fdb9735d45d609a596df722468:booster_t1/CHANGELOG.md')` in `menagerie`. fatal: bad object d9415a3076f921fdb9735d45d609a596df722468:booster_t1/CHANGELOG.md

- Offline Git read failed (exit 128): `('show', 'd9415a3076f921fdb9735d45d609a596df722468:fourier_n1/CHANGELOG.md')` in `menagerie`. fatal: bad object d9415a3076f921fdb9735d45d609a596df722468:fourier_n1/CHANGELOG.md

- Offline Git read failed (exit 128): `('show', '400b5f5b9fec382583f69b53b094a154d9dc7635:fourier_n1/CHANGELOG.md')` in `menagerie`. fatal: path 'fourier_n1/CHANGELOG.md' does not exist in '400b5f5b9fec382583f69b53b094a154d9dc7635'

- Offline Git read failed (exit 128): `('show', 'db140ade7ee4cb59629f9687aafc65af663d5bbe:franka_fr3_v2/README.md')` in `menagerie`. fatal: path 'franka_fr3_v2/README.md' does not exist in 'db140ade7ee4cb59629f9687aafc65af663d5bbe'

- Offline Git read failed (exit 128): `('show', 'cd7fc51b704c3cba05748bd5537cb17990b341eb:franka_fr3_v2/README.md')` in `menagerie`. fatal: path 'franka_fr3_v2/README.md' does not exist in 'cd7fc51b704c3cba05748bd5537cb17990b341eb'

- Offline Git read failed (exit 128): `('show', '400b5f5b9fec382583f69b53b094a154d9dc7635:franka_fr3_v2/README.md')` in `menagerie`. fatal: path 'franka_fr3_v2/README.md' does not exist in '400b5f5b9fec382583f69b53b094a154d9dc7635'

- Offline Git read failed (exit 128): `('show', 'acbbf1636fcfef9b437a6eb8c6f84380fb4aa998:franka_fr3_v2/README.md')` in `menagerie`. fatal: path 'franka_fr3_v2/README.md' does not exist in 'acbbf1636fcfef9b437a6eb8c6f84380fb4aa998'

- Offline Git read failed (exit 128): `('show', '7876dcdef0d912387441616526ed236142f047d3:franka_fr3_v2/README.md')` in `menagerie`. fatal: path 'franka_fr3_v2/README.md' does not exist in '7876dcdef0d912387441616526ed236142f047d3'

- Offline Git read failed (exit 128): `('show', 'b5ebfe0cf079d2b96acf0a5c0e29ee0c95ba32f4:google_robot/README.md')` in `menagerie`. fatal: path 'google_robot/README.md' does not exist in 'b5ebfe0cf079d2b96acf0a5c0e29ee0c95ba32f4'

- Offline Git read failed (exit 128): `('show', '5ce04bea98bbfca277a8d50b55ba3c7c4a62bdec:i2rt_yam/CHANGELOG.md')` in `menagerie`. fatal: path 'i2rt_yam/CHANGELOG.md' does not exist in '5ce04bea98bbfca277a8d50b55ba3c7c4a62bdec'

- Offline Git read failed (exit 128): `('show', 'a88bc450470d97ebc1f282e5969675fb4d1f0ed7:low_cost_robot_arm/README.md')` in `menagerie`. fatal: path 'low_cost_robot_arm/README.md' does not exist in 'a88bc450470d97ebc1f282e5969675fb4d1f0ed7'

- Offline Git read failed (exit 128): `('show', 'd74280a600a9afdfcb98d8917d0c79c86539aa61:low_cost_robot_arm/README.md')` in `menagerie`. fatal: path 'low_cost_robot_arm/README.md' does not exist in 'd74280a600a9afdfcb98d8917d0c79c86539aa61'

- Offline Git read failed (exit 128): `('show', '13d6c48b8f59d2c4badee7756b4ea3532613cddf:low_cost_robot_arm/README.md')` in `menagerie`. fatal: path 'low_cost_robot_arm/README.md' does not exist in '13d6c48b8f59d2c4badee7756b4ea3532613cddf'

- Offline Git read failed (exit 128): `('show', 'fae9ee82330444eec4e87568c838b99a09a39467:rainbow_robotics_rby1/README.md')` in `menagerie`. fatal: path 'rainbow_robotics_rby1/README.md' does not exist in 'fae9ee82330444eec4e87568c838b99a09a39467'

- Offline Git read failed (exit 128): `('show', '04674c8d0a4e12e33980a9e47fb604adc281fcc8:robotstudio_so101/CHANGELOG.md')` in `menagerie`. fatal: path 'robotstudio_so101/CHANGELOG.md' does not exist in '04674c8d0a4e12e33980a9e47fb604adc281fcc8'

- Offline Git read failed (exit 128): `('show', '5ce04bea98bbfca277a8d50b55ba3c7c4a62bdec:robotstudio_so101/CHANGELOG.md')` in `menagerie`. fatal: path 'robotstudio_so101/CHANGELOG.md' does not exist in '5ce04bea98bbfca277a8d50b55ba3c7c4a62bdec'

- Offline Git read failed (exit 128): `('show', '4a7015530bd7a4161103ae8f0905a96481e4cc1a:robotstudio_so101/CHANGELOG.md')` in `menagerie`. fatal: path 'robotstudio_so101/CHANGELOG.md' does not exist in '4a7015530bd7a4161103ae8f0905a96481e4cc1a'

- Offline Git read failed (exit 128): `('show', 'bf110a75a56e5bd146c7ed76965737c71d48425d:shadow_dexee/README.md')` in `menagerie`. fatal: path 'shadow_dexee/README.md' does not exist in 'bf110a75a56e5bd146c7ed76965737c71d48425d'

- Offline Git read failed (exit 128): `('show', '04674c8d0a4e12e33980a9e47fb604adc281fcc8:tetheria_aero_hand_open/CHANGELOG.md')` in `menagerie`. fatal: path 'tetheria_aero_hand_open/CHANGELOG.md' does not exist in '04674c8d0a4e12e33980a9e47fb604adc281fcc8'

- Offline Git read failed (exit 128): `('show', '400b5f5b9fec382583f69b53b094a154d9dc7635:tetheria_aero_hand_open/CHANGELOG.md')` in `menagerie`. fatal: path 'tetheria_aero_hand_open/CHANGELOG.md' does not exist in '400b5f5b9fec382583f69b53b094a154d9dc7635'

- Offline Git read failed (exit 128): `('show', '04674c8d0a4e12e33980a9e47fb604adc281fcc8:toddlerbot_2xc/CHANGELOG.md')` in `menagerie`. fatal: path 'toddlerbot_2xc/CHANGELOG.md' does not exist in '04674c8d0a4e12e33980a9e47fb604adc281fcc8'

- Offline Git read failed (exit 128): `('show', '9e7f8d4dda07f5c281b6c0c6f0d07b9dd267b762:toddlerbot_2xc/CHANGELOG.md')` in `menagerie`. fatal: path 'toddlerbot_2xc/CHANGELOG.md' does not exist in '9e7f8d4dda07f5c281b6c0c6f0d07b9dd267b762'

- Offline Git read failed (exit 128): `('show', '400b5f5b9fec382583f69b53b094a154d9dc7635:toddlerbot_2xc/CHANGELOG.md')` in `menagerie`. fatal: path 'toddlerbot_2xc/CHANGELOG.md' does not exist in '400b5f5b9fec382583f69b53b094a154d9dc7635'

- Offline Git read failed (exit 128): `('show', '04674c8d0a4e12e33980a9e47fb604adc281fcc8:toddlerbot_2xm/CHANGELOG.md')` in `menagerie`. fatal: path 'toddlerbot_2xm/CHANGELOG.md' does not exist in '04674c8d0a4e12e33980a9e47fb604adc281fcc8'

- Offline Git read failed (exit 128): `('show', '9e7f8d4dda07f5c281b6c0c6f0d07b9dd267b762:toddlerbot_2xm/CHANGELOG.md')` in `menagerie`. fatal: path 'toddlerbot_2xm/CHANGELOG.md' does not exist in '9e7f8d4dda07f5c281b6c0c6f0d07b9dd267b762'

- Offline Git read failed (exit 128): `('show', '400b5f5b9fec382583f69b53b094a154d9dc7635:toddlerbot_2xm/CHANGELOG.md')` in `menagerie`. fatal: path 'toddlerbot_2xm/CHANGELOG.md' does not exist in '400b5f5b9fec382583f69b53b094a154d9dc7635'

- Offline Git read failed (exit 128): `('show', '400b5f5b9fec382583f69b53b094a154d9dc7635:trossen_wxai/README.md')` in `menagerie`. fatal: path 'trossen_wxai/README.md' does not exist in '400b5f5b9fec382583f69b53b094a154d9dc7635'

- Offline Git read failed (exit 128): `('show', '477ec56566682d663b996d86a188c75499e74b98:trossen_wxai/README.md')` in `menagerie`. fatal: path 'trossen_wxai/README.md' does not exist in '477ec56566682d663b996d86a188c75499e74b98'

- Offline Git read failed (exit 128): `('show', 'd9415a3076f921fdb9735d45d609a596df722468:unitree_g1/CHANGELOG.md')` in `menagerie`. fatal: bad object d9415a3076f921fdb9735d45d609a596df722468:unitree_g1/CHANGELOG.md

- Implemented proper (det=+1) Kabsch registration in report anchor frames, RMS and maximum residuals, per-origin residuals, signed axis vectors/angles and explicit CoM eligibility. Mass, subtree mass, principal moments, ranges, limits and raw provenance matching are unchanged. Eligible CoM is compared after rigid alignment; excluded values remain in separate raw report tables. A three-way CoM needs both M/H and M/S checks when S exists. Underdetermined fits are excluded as insufficient coverage instead of asserting an arbitrary axis mismatch.
- Added CLI --kinematic-residual / --kinematic-axis-angle, --recompare for a frozen-revision primary-recompile survey, and cross-check --all-stale so the full independent STALE audit is reproducible without an ignored helper script. Direct CoM checks fit XML-derived body origins independently, never cached transforms.
- First complete new suite: **56 passed in 16.96 seconds**, including H1 and tests for proper rigid fits, reflection rejection, axis reversal, configurable residuals, underdetermined fits, source-side gating, preserved raw numbers and independent XML registration. No network commands have been needed for this revision.

- Frozen-rerun before/after validation: {"models_rerun": 71, "self_comparisons_recompiled": 119, "frame_independent_and_raw_range_limit_records_unchanged": 3502, "stale_records_unchanged": 20, "stale_models_unchanged": ["seeed_rebot_devarm", "ufactory_lite6", "ufactory_xarm7"], "h1_acceptance_unchanged": true, "convention_differs_models": ["arx_l5", "rainbow_robotics_rby1", "trs_so_arm100", "universal_robots_ur10e", "universal_robots_ur5e"], "insufficient_coverage_models": ["bitcraze_crazyflie_2", "boston_dynamics_spot", "franka_emika_panda", "i2rt_yam", "kuka_iiwa_14", "leap_hand", "realsense_d435i", "robotiq_2f85", "robotiq_2f85_v4", "trossen_vx300s", "wonik_allegro"], "excluded_raw_com_findings": 59, "class_counts": {"NO MATCHING SOURCE": 334, "undocumented derivation difference": 82, "unknown": 157, "STALE": 20, "needs a human look": 4}, "total_findings": 597}

- Direct XML random cross-checks: 3 selected, seed 20261113; agreements [True, True, False]; skipped draws 0.

- Frozen survey completed all 71 folders, recompiling 119 self-test variants and available primary views. Exit status **2** is intentional coverage signaling for the retained partial-history/current-source gaps, not a stopped run. Before/after validation confirmed all 3,502 non-CoM records and their classes unchanged, exactly the same 20 STALE record identities in three models, and unchanged H1 masses/ranges/NO MATCHING SOURCE acceptance. Five models have convention differences; eleven have insufficient fit coverage.
- The new total is 597. An initial membership-audit assertion incorrectly assumed alignment could only remove records; it failed because two non-STALE CoM records cross into reporting after alignment. The detailed audit shows **78 removed (59 excluded, 19 resolved by alignment) and 2 added**, a net reduction of 76. An earlier progress sentence described the net alignment reduction of 17 as 17 removed; this is corrected here and in the final publication counts. No finding was discarded to satisfy that assumption.

- The first guarded random XML sample reported **2/3 agree** (exit 2). Its third draw, FR3 link0 CoM, exposed an existing direct-parser bug: a geometry-derived CoM had been returned as the body origin. Corrected missing-inertial bodies to mark CoM as geometry-derived/unextractable, added a regression, and retain all skipped draws explicitly. No simulator quantity was changed to obtain agreement. The first guarded full suite before this correction passed 58 tests in 15.27 seconds.
- Final guard refinement: Kabsch still minimizes squared origin residuals and records RMS, but the configurable 5 mm threshold applies to the **maximum individual origin residual**. Piper demonstrated why RMS alone was insufficient: RMS 4.690 mm, maximum 6.633 mm; the fitted transform introduced two spurious-looking CoM records at the base. The maximum guard rejects that fit uniformly, rather than special-casing Piper or suppressing individual numbers. This supersedes the initial RMS-threshold trial and its intermediate 597-record counts. Added an outlier regression. The three STALE models and H1 all have sub-micrometre maximum residuals and are unaffected.

- Rejected unrelated historical README template for agilex_piper: 0bee963312f0f4a25b53cdf9afe744ca73f2d68a heading '## UMI-Gripper Description (MJCF)'

- Offline Git read failed (exit 128): `('show', '400b5f5b9fec382583f69b53b094a154d9dc7635:agilex_piper/CHANGELOG.md')` in `menagerie`. fatal: path 'agilex_piper/CHANGELOG.md' does not exist in '400b5f5b9fec382583f69b53b094a154d9dc7635'

- Rejected conflicting robot-variant link for anybotics_anymal_c: https://github.com/ANYbotics/anymal_b_simple_description/blob/master/urdf/anymal.urdf (repository variant b, model variant c)

- Offline Git read failed (exit 128): `('show', 'd9415a3076f921fdb9735d45d609a596df722468:apptronik_apollo/CHANGELOG.md')` in `menagerie`. fatal: bad object d9415a3076f921fdb9735d45d609a596df722468:apptronik_apollo/CHANGELOG.md

- Offline Git read failed (exit 128): `('show', '400b5f5b9fec382583f69b53b094a154d9dc7635:arx_l5/CHANGELOG.md')` in `menagerie`. fatal: path 'arx_l5/CHANGELOG.md' does not exist in '400b5f5b9fec382583f69b53b094a154d9dc7635'

- Offline Git read failed (exit 128): `('show', 'd9415a3076f921fdb9735d45d609a596df722468:berkeley_humanoid/CHANGELOG.md')` in `menagerie`. fatal: bad object d9415a3076f921fdb9735d45d609a596df722468:berkeley_humanoid/CHANGELOG.md

- Offline Git read failed (exit 128): `('show', 'd9415a3076f921fdb9735d45d609a596df722468:booster_t1/CHANGELOG.md')` in `menagerie`. fatal: bad object d9415a3076f921fdb9735d45d609a596df722468:booster_t1/CHANGELOG.md

- Offline Git read failed (exit 128): `('show', 'd9415a3076f921fdb9735d45d609a596df722468:fourier_n1/CHANGELOG.md')` in `menagerie`. fatal: bad object d9415a3076f921fdb9735d45d609a596df722468:fourier_n1/CHANGELOG.md

- Offline Git read failed (exit 128): `('show', '400b5f5b9fec382583f69b53b094a154d9dc7635:fourier_n1/CHANGELOG.md')` in `menagerie`. fatal: path 'fourier_n1/CHANGELOG.md' does not exist in '400b5f5b9fec382583f69b53b094a154d9dc7635'

- Offline Git read failed (exit 128): `('show', 'db140ade7ee4cb59629f9687aafc65af663d5bbe:franka_fr3_v2/README.md')` in `menagerie`. fatal: path 'franka_fr3_v2/README.md' does not exist in 'db140ade7ee4cb59629f9687aafc65af663d5bbe'

- Offline Git read failed (exit 128): `('show', 'cd7fc51b704c3cba05748bd5537cb17990b341eb:franka_fr3_v2/README.md')` in `menagerie`. fatal: path 'franka_fr3_v2/README.md' does not exist in 'cd7fc51b704c3cba05748bd5537cb17990b341eb'

- Offline Git read failed (exit 128): `('show', '400b5f5b9fec382583f69b53b094a154d9dc7635:franka_fr3_v2/README.md')` in `menagerie`. fatal: path 'franka_fr3_v2/README.md' does not exist in '400b5f5b9fec382583f69b53b094a154d9dc7635'

- Offline Git read failed (exit 128): `('show', 'acbbf1636fcfef9b437a6eb8c6f84380fb4aa998:franka_fr3_v2/README.md')` in `menagerie`. fatal: path 'franka_fr3_v2/README.md' does not exist in 'acbbf1636fcfef9b437a6eb8c6f84380fb4aa998'

- Offline Git read failed (exit 128): `('show', '7876dcdef0d912387441616526ed236142f047d3:franka_fr3_v2/README.md')` in `menagerie`. fatal: path 'franka_fr3_v2/README.md' does not exist in '7876dcdef0d912387441616526ed236142f047d3'

- Offline Git read failed (exit 128): `('show', 'b5ebfe0cf079d2b96acf0a5c0e29ee0c95ba32f4:google_robot/README.md')` in `menagerie`. fatal: path 'google_robot/README.md' does not exist in 'b5ebfe0cf079d2b96acf0a5c0e29ee0c95ba32f4'

- Offline Git read failed (exit 128): `('show', '5ce04bea98bbfca277a8d50b55ba3c7c4a62bdec:i2rt_yam/CHANGELOG.md')` in `menagerie`. fatal: path 'i2rt_yam/CHANGELOG.md' does not exist in '5ce04bea98bbfca277a8d50b55ba3c7c4a62bdec'

- Offline Git read failed (exit 128): `('show', 'a88bc450470d97ebc1f282e5969675fb4d1f0ed7:low_cost_robot_arm/README.md')` in `menagerie`. fatal: path 'low_cost_robot_arm/README.md' does not exist in 'a88bc450470d97ebc1f282e5969675fb4d1f0ed7'

- Offline Git read failed (exit 128): `('show', 'd74280a600a9afdfcb98d8917d0c79c86539aa61:low_cost_robot_arm/README.md')` in `menagerie`. fatal: path 'low_cost_robot_arm/README.md' does not exist in 'd74280a600a9afdfcb98d8917d0c79c86539aa61'

- Offline Git read failed (exit 128): `('show', '13d6c48b8f59d2c4badee7756b4ea3532613cddf:low_cost_robot_arm/README.md')` in `menagerie`. fatal: path 'low_cost_robot_arm/README.md' does not exist in '13d6c48b8f59d2c4badee7756b4ea3532613cddf'

- Offline Git read failed (exit 128): `('show', 'fae9ee82330444eec4e87568c838b99a09a39467:rainbow_robotics_rby1/README.md')` in `menagerie`. fatal: path 'rainbow_robotics_rby1/README.md' does not exist in 'fae9ee82330444eec4e87568c838b99a09a39467'

- Offline Git read failed (exit 128): `('show', '04674c8d0a4e12e33980a9e47fb604adc281fcc8:robotstudio_so101/CHANGELOG.md')` in `menagerie`. fatal: path 'robotstudio_so101/CHANGELOG.md' does not exist in '04674c8d0a4e12e33980a9e47fb604adc281fcc8'

- Offline Git read failed (exit 128): `('show', '5ce04bea98bbfca277a8d50b55ba3c7c4a62bdec:robotstudio_so101/CHANGELOG.md')` in `menagerie`. fatal: path 'robotstudio_so101/CHANGELOG.md' does not exist in '5ce04bea98bbfca277a8d50b55ba3c7c4a62bdec'

- Offline Git read failed (exit 128): `('show', '4a7015530bd7a4161103ae8f0905a96481e4cc1a:robotstudio_so101/CHANGELOG.md')` in `menagerie`. fatal: path 'robotstudio_so101/CHANGELOG.md' does not exist in '4a7015530bd7a4161103ae8f0905a96481e4cc1a'

- Offline Git read failed (exit 128): `('show', 'bf110a75a56e5bd146c7ed76965737c71d48425d:shadow_dexee/README.md')` in `menagerie`. fatal: path 'shadow_dexee/README.md' does not exist in 'bf110a75a56e5bd146c7ed76965737c71d48425d'

- Offline Git read failed (exit 128): `('show', '04674c8d0a4e12e33980a9e47fb604adc281fcc8:tetheria_aero_hand_open/CHANGELOG.md')` in `menagerie`. fatal: path 'tetheria_aero_hand_open/CHANGELOG.md' does not exist in '04674c8d0a4e12e33980a9e47fb604adc281fcc8'

- Offline Git read failed (exit 128): `('show', '400b5f5b9fec382583f69b53b094a154d9dc7635:tetheria_aero_hand_open/CHANGELOG.md')` in `menagerie`. fatal: path 'tetheria_aero_hand_open/CHANGELOG.md' does not exist in '400b5f5b9fec382583f69b53b094a154d9dc7635'

- Offline Git read failed (exit 128): `('show', '04674c8d0a4e12e33980a9e47fb604adc281fcc8:toddlerbot_2xc/CHANGELOG.md')` in `menagerie`. fatal: path 'toddlerbot_2xc/CHANGELOG.md' does not exist in '04674c8d0a4e12e33980a9e47fb604adc281fcc8'

- Offline Git read failed (exit 128): `('show', '9e7f8d4dda07f5c281b6c0c6f0d07b9dd267b762:toddlerbot_2xc/CHANGELOG.md')` in `menagerie`. fatal: path 'toddlerbot_2xc/CHANGELOG.md' does not exist in '9e7f8d4dda07f5c281b6c0c6f0d07b9dd267b762'

- Offline Git read failed (exit 128): `('show', '400b5f5b9fec382583f69b53b094a154d9dc7635:toddlerbot_2xc/CHANGELOG.md')` in `menagerie`. fatal: path 'toddlerbot_2xc/CHANGELOG.md' does not exist in '400b5f5b9fec382583f69b53b094a154d9dc7635'

- Offline Git read failed (exit 128): `('show', '04674c8d0a4e12e33980a9e47fb604adc281fcc8:toddlerbot_2xm/CHANGELOG.md')` in `menagerie`. fatal: path 'toddlerbot_2xm/CHANGELOG.md' does not exist in '04674c8d0a4e12e33980a9e47fb604adc281fcc8'

- Offline Git read failed (exit 128): `('show', '9e7f8d4dda07f5c281b6c0c6f0d07b9dd267b762:toddlerbot_2xm/CHANGELOG.md')` in `menagerie`. fatal: path 'toddlerbot_2xm/CHANGELOG.md' does not exist in '9e7f8d4dda07f5c281b6c0c6f0d07b9dd267b762'

- Offline Git read failed (exit 128): `('show', '400b5f5b9fec382583f69b53b094a154d9dc7635:toddlerbot_2xm/CHANGELOG.md')` in `menagerie`. fatal: path 'toddlerbot_2xm/CHANGELOG.md' does not exist in '400b5f5b9fec382583f69b53b094a154d9dc7635'

- Offline Git read failed (exit 128): `('show', '400b5f5b9fec382583f69b53b094a154d9dc7635:trossen_wxai/README.md')` in `menagerie`. fatal: path 'trossen_wxai/README.md' does not exist in '400b5f5b9fec382583f69b53b094a154d9dc7635'

- Offline Git read failed (exit 128): `('show', '477ec56566682d663b996d86a188c75499e74b98:trossen_wxai/README.md')` in `menagerie`. fatal: path 'trossen_wxai/README.md' does not exist in '477ec56566682d663b996d86a188c75499e74b98'

- Offline Git read failed (exit 128): `('show', 'd9415a3076f921fdb9735d45d609a596df722468:unitree_g1/CHANGELOG.md')` in `menagerie`. fatal: bad object d9415a3076f921fdb9735d45d609a596df722468:unitree_g1/CHANGELOG.md

- Final maximum-residual/geometry-aware preflight: **59 passed, 1 integration test deselected in 0.94 seconds**. Full final tests and both independent XML audits follow the completed rerun. The weekly workflow now runs the reproducible all-STALE audit as well as the three seeded checks; YAML was parsed locally with read-only repository permissions, and no remote workflow was executed.

- Frozen-rerun before/after validation: {"models_rerun": 71, "self_comparisons_recompiled": 119, "frame_independent_and_raw_range_limit_records_unchanged": 3502, "raw_com_records_and_raw_classes_preserved": 827, "stale_records_unchanged": 20, "stale_models_unchanged": ["seeed_rebot_devarm", "ufactory_lite6", "ufactory_xarm7"], "h1_acceptance_unchanged": true, "convention_differs_models": ["agilex_piper", "arx_l5", "rainbow_robotics_rby1", "trs_so_arm100", "universal_robots_ur10e", "universal_robots_ur5e"], "insufficient_coverage_models": ["bitcraze_crazyflie_2", "boston_dynamics_spot", "franka_emika_panda", "i2rt_yam", "kuka_iiwa_14", "leap_hand", "realsense_d435i", "robotiq_2f85", "robotiq_2f85_v4", "trossen_vx300s", "wonik_allegro"], "excluded_raw_com_findings": 67, "class_counts": {"NO MATCHING SOURCE": 324, "undocumented derivation difference": 82, "unknown": 157, "STALE": 20, "needs a human look": 4}, "total_findings": 587}

- Direct XML random cross-checks: 3 selected, seed 20261113; agreements [True, True, True]; skipped draws 1.

- Final maximum-residual frozen rerun completed all 71 models (exit 2 for the same explicit coverage gaps). Validation: **119 self-variants recompiled**, **3,502 non-CoM records unchanged**, **827 raw CoM records and raw classes preserved**, **20 identical STALE record identities in the same three models**, H1 acceptance/numbers unchanged. Guard: **6 convention-difference models**, **11 insufficient-coverage models**, **67 raw CoM findings excluded**. Another **19 CoM findings resolve after alignment**, so **86 removed, 0 added**, final **587 findings** (324 NO MATCHING SOURCE, 82 undocumented derivation difference, 157 unknown, 20 STALE, 4 needs a human look). This supersedes the RMS-trial counts.
- Final sensitivity: half tolerances **603 records**, 16 memberships / 7 labels changed, 20 STALE; double **568 records**, 19 memberships / 4 labels changed, 19 STALE. Quality thresholds remain fixed at configured values. No raw mass/inertia/range/limit record or source commit was changed to obtain these counts.

- Final offline artifact validation: {"model_reports": 71, "provenance_files": 71, "source_link_occurrences": 3404, "unique_source_line_targets_checked": 2824, "unresolved_finding_source_references": 0, "all_link_targets_exist_at_exact_shas": true, "raw_com_source_links_checked": true, "workflow_yaml_valid": true}

- Every-STALE independent XML audit: 20/20 agree; CoM fits independently recomputed from XML origins.

- Rejected unrelated historical README template for agilex_piper: 0bee963312f0f4a25b53cdf9afe744ca73f2d68a heading '## UMI-Gripper Description (MJCF)'

- Offline Git read failed (exit 128): `('show', '400b5f5b9fec382583f69b53b094a154d9dc7635:agilex_piper/CHANGELOG.md')` in `menagerie`. fatal: path 'agilex_piper/CHANGELOG.md' does not exist in '400b5f5b9fec382583f69b53b094a154d9dc7635'

- Maximum-residual survey verification: **60 tests passed in 16.11 seconds**; required seeded XML checks **3/3 agree**, and the reproducible every-STALE XML audit **20/20 agree**, including independently fitted CoM. Exact-line validation checked **3,404 link occurrences / 2,824 unique targets**, including all raw CoM links, with zero unresolved targets.
- Final axis correctness refinement: use MuJoCo data.xaxis at the zero pose, expressed in the registered frame. Rotating model.jnt_axis by the final body rotation can be wrong when a body has multiple joints with nonzero references. Added a synthetic test demonstrating the difference; all nine kinematics tests pass. The primary-recompile rerun refreshes these actual axes. Legacy archived snapshots retain an explicitly labeled body-frame fallback for sensitivity/source-history data. No physical mass/inertia/range/limit values are modified.

- Rejected conflicting robot-variant link for anybotics_anymal_c: https://github.com/ANYbotics/anymal_b_simple_description/blob/master/urdf/anymal.urdf (repository variant b, model variant c)

- Offline Git read failed (exit 128): `('show', 'd9415a3076f921fdb9735d45d609a596df722468:apptronik_apollo/CHANGELOG.md')` in `menagerie`. fatal: bad object d9415a3076f921fdb9735d45d609a596df722468:apptronik_apollo/CHANGELOG.md

- Offline Git read failed (exit 128): `('show', '400b5f5b9fec382583f69b53b094a154d9dc7635:arx_l5/CHANGELOG.md')` in `menagerie`. fatal: path 'arx_l5/CHANGELOG.md' does not exist in '400b5f5b9fec382583f69b53b094a154d9dc7635'

- Offline Git read failed (exit 128): `('show', 'd9415a3076f921fdb9735d45d609a596df722468:berkeley_humanoid/CHANGELOG.md')` in `menagerie`. fatal: bad object d9415a3076f921fdb9735d45d609a596df722468:berkeley_humanoid/CHANGELOG.md

- Offline Git read failed (exit 128): `('show', 'd9415a3076f921fdb9735d45d609a596df722468:booster_t1/CHANGELOG.md')` in `menagerie`. fatal: bad object d9415a3076f921fdb9735d45d609a596df722468:booster_t1/CHANGELOG.md

- Offline Git read failed (exit 128): `('show', 'd9415a3076f921fdb9735d45d609a596df722468:fourier_n1/CHANGELOG.md')` in `menagerie`. fatal: bad object d9415a3076f921fdb9735d45d609a596df722468:fourier_n1/CHANGELOG.md

- Offline Git read failed (exit 128): `('show', '400b5f5b9fec382583f69b53b094a154d9dc7635:fourier_n1/CHANGELOG.md')` in `menagerie`. fatal: path 'fourier_n1/CHANGELOG.md' does not exist in '400b5f5b9fec382583f69b53b094a154d9dc7635'

- Offline Git read failed (exit 128): `('show', 'db140ade7ee4cb59629f9687aafc65af663d5bbe:franka_fr3_v2/README.md')` in `menagerie`. fatal: path 'franka_fr3_v2/README.md' does not exist in 'db140ade7ee4cb59629f9687aafc65af663d5bbe'

- Offline Git read failed (exit 128): `('show', 'cd7fc51b704c3cba05748bd5537cb17990b341eb:franka_fr3_v2/README.md')` in `menagerie`. fatal: path 'franka_fr3_v2/README.md' does not exist in 'cd7fc51b704c3cba05748bd5537cb17990b341eb'

- Offline Git read failed (exit 128): `('show', '400b5f5b9fec382583f69b53b094a154d9dc7635:franka_fr3_v2/README.md')` in `menagerie`. fatal: path 'franka_fr3_v2/README.md' does not exist in '400b5f5b9fec382583f69b53b094a154d9dc7635'

- Offline Git read failed (exit 128): `('show', 'acbbf1636fcfef9b437a6eb8c6f84380fb4aa998:franka_fr3_v2/README.md')` in `menagerie`. fatal: path 'franka_fr3_v2/README.md' does not exist in 'acbbf1636fcfef9b437a6eb8c6f84380fb4aa998'

- Offline Git read failed (exit 128): `('show', '7876dcdef0d912387441616526ed236142f047d3:franka_fr3_v2/README.md')` in `menagerie`. fatal: path 'franka_fr3_v2/README.md' does not exist in '7876dcdef0d912387441616526ed236142f047d3'

- Offline Git read failed (exit 128): `('show', 'b5ebfe0cf079d2b96acf0a5c0e29ee0c95ba32f4:google_robot/README.md')` in `menagerie`. fatal: path 'google_robot/README.md' does not exist in 'b5ebfe0cf079d2b96acf0a5c0e29ee0c95ba32f4'

- Offline Git read failed (exit 128): `('show', '5ce04bea98bbfca277a8d50b55ba3c7c4a62bdec:i2rt_yam/CHANGELOG.md')` in `menagerie`. fatal: path 'i2rt_yam/CHANGELOG.md' does not exist in '5ce04bea98bbfca277a8d50b55ba3c7c4a62bdec'

- Offline Git read failed (exit 128): `('show', 'a88bc450470d97ebc1f282e5969675fb4d1f0ed7:low_cost_robot_arm/README.md')` in `menagerie`. fatal: path 'low_cost_robot_arm/README.md' does not exist in 'a88bc450470d97ebc1f282e5969675fb4d1f0ed7'

- Offline Git read failed (exit 128): `('show', 'd74280a600a9afdfcb98d8917d0c79c86539aa61:low_cost_robot_arm/README.md')` in `menagerie`. fatal: path 'low_cost_robot_arm/README.md' does not exist in 'd74280a600a9afdfcb98d8917d0c79c86539aa61'

- Offline Git read failed (exit 128): `('show', '13d6c48b8f59d2c4badee7756b4ea3532613cddf:low_cost_robot_arm/README.md')` in `menagerie`. fatal: path 'low_cost_robot_arm/README.md' does not exist in '13d6c48b8f59d2c4badee7756b4ea3532613cddf'

- Offline Git read failed (exit 128): `('show', 'fae9ee82330444eec4e87568c838b99a09a39467:rainbow_robotics_rby1/README.md')` in `menagerie`. fatal: path 'rainbow_robotics_rby1/README.md' does not exist in 'fae9ee82330444eec4e87568c838b99a09a39467'

- Offline Git read failed (exit 128): `('show', '04674c8d0a4e12e33980a9e47fb604adc281fcc8:robotstudio_so101/CHANGELOG.md')` in `menagerie`. fatal: path 'robotstudio_so101/CHANGELOG.md' does not exist in '04674c8d0a4e12e33980a9e47fb604adc281fcc8'

- Offline Git read failed (exit 128): `('show', '5ce04bea98bbfca277a8d50b55ba3c7c4a62bdec:robotstudio_so101/CHANGELOG.md')` in `menagerie`. fatal: path 'robotstudio_so101/CHANGELOG.md' does not exist in '5ce04bea98bbfca277a8d50b55ba3c7c4a62bdec'

- Offline Git read failed (exit 128): `('show', '4a7015530bd7a4161103ae8f0905a96481e4cc1a:robotstudio_so101/CHANGELOG.md')` in `menagerie`. fatal: path 'robotstudio_so101/CHANGELOG.md' does not exist in '4a7015530bd7a4161103ae8f0905a96481e4cc1a'

- Offline Git read failed (exit 128): `('show', 'bf110a75a56e5bd146c7ed76965737c71d48425d:shadow_dexee/README.md')` in `menagerie`. fatal: path 'shadow_dexee/README.md' does not exist in 'bf110a75a56e5bd146c7ed76965737c71d48425d'

- Offline Git read failed (exit 128): `('show', '04674c8d0a4e12e33980a9e47fb604adc281fcc8:tetheria_aero_hand_open/CHANGELOG.md')` in `menagerie`. fatal: path 'tetheria_aero_hand_open/CHANGELOG.md' does not exist in '04674c8d0a4e12e33980a9e47fb604adc281fcc8'

- Offline Git read failed (exit 128): `('show', '400b5f5b9fec382583f69b53b094a154d9dc7635:tetheria_aero_hand_open/CHANGELOG.md')` in `menagerie`. fatal: path 'tetheria_aero_hand_open/CHANGELOG.md' does not exist in '400b5f5b9fec382583f69b53b094a154d9dc7635'

- Offline Git read failed (exit 128): `('show', '04674c8d0a4e12e33980a9e47fb604adc281fcc8:toddlerbot_2xc/CHANGELOG.md')` in `menagerie`. fatal: path 'toddlerbot_2xc/CHANGELOG.md' does not exist in '04674c8d0a4e12e33980a9e47fb604adc281fcc8'

- Offline Git read failed (exit 128): `('show', '9e7f8d4dda07f5c281b6c0c6f0d07b9dd267b762:toddlerbot_2xc/CHANGELOG.md')` in `menagerie`. fatal: path 'toddlerbot_2xc/CHANGELOG.md' does not exist in '9e7f8d4dda07f5c281b6c0c6f0d07b9dd267b762'

- Offline Git read failed (exit 128): `('show', '400b5f5b9fec382583f69b53b094a154d9dc7635:toddlerbot_2xc/CHANGELOG.md')` in `menagerie`. fatal: path 'toddlerbot_2xc/CHANGELOG.md' does not exist in '400b5f5b9fec382583f69b53b094a154d9dc7635'

- Offline Git read failed (exit 128): `('show', '04674c8d0a4e12e33980a9e47fb604adc281fcc8:toddlerbot_2xm/CHANGELOG.md')` in `menagerie`. fatal: path 'toddlerbot_2xm/CHANGELOG.md' does not exist in '04674c8d0a4e12e33980a9e47fb604adc281fcc8'

- Offline Git read failed (exit 128): `('show', '9e7f8d4dda07f5c281b6c0c6f0d07b9dd267b762:toddlerbot_2xm/CHANGELOG.md')` in `menagerie`. fatal: path 'toddlerbot_2xm/CHANGELOG.md' does not exist in '9e7f8d4dda07f5c281b6c0c6f0d07b9dd267b762'

- Offline Git read failed (exit 128): `('show', '400b5f5b9fec382583f69b53b094a154d9dc7635:toddlerbot_2xm/CHANGELOG.md')` in `menagerie`. fatal: path 'toddlerbot_2xm/CHANGELOG.md' does not exist in '400b5f5b9fec382583f69b53b094a154d9dc7635'

- Offline Git read failed (exit 128): `('show', '400b5f5b9fec382583f69b53b094a154d9dc7635:trossen_wxai/README.md')` in `menagerie`. fatal: path 'trossen_wxai/README.md' does not exist in '400b5f5b9fec382583f69b53b094a154d9dc7635'

- Offline Git read failed (exit 128): `('show', '477ec56566682d663b996d86a188c75499e74b98:trossen_wxai/README.md')` in `menagerie`. fatal: path 'trossen_wxai/README.md' does not exist in '477ec56566682d663b996d86a188c75499e74b98'

- Offline Git read failed (exit 128): `('show', 'd9415a3076f921fdb9735d45d609a596df722468:unitree_g1/CHANGELOG.md')` in `menagerie`. fatal: bad object d9415a3076f921fdb9735d45d609a596df722468:unitree_g1/CHANGELOG.md

- Frozen-rerun before/after validation: {"models_rerun": 71, "self_comparisons_recompiled": 119, "frame_independent_and_raw_range_limit_records_unchanged": 3502, "raw_com_records_and_raw_classes_preserved": 827, "stale_records_unchanged": 20, "stale_models_unchanged": ["seeed_rebot_devarm", "ufactory_lite6", "ufactory_xarm7"], "h1_acceptance_unchanged": true, "all_primary_checked_axes_from_mujoco_xaxis": true, "convention_differs_models": ["agilex_piper", "arx_l5", "rainbow_robotics_rby1", "trs_so_arm100", "universal_robots_ur10e", "universal_robots_ur5e"], "insufficient_coverage_models": ["bitcraze_crazyflie_2", "boston_dynamics_spot", "franka_emika_panda", "i2rt_yam", "kuka_iiwa_14", "leap_hand", "realsense_d435i", "robotiq_2f85", "robotiq_2f85_v4", "trossen_vx300s", "wonik_allegro"], "excluded_raw_com_findings": 67, "class_counts": {"NO MATCHING SOURCE": 324, "undocumented derivation difference": 82, "unknown": 157, "STALE": 20, "needs a human look": 4}, "total_findings": 587}

- Direct XML random cross-checks: 3 selected, seed 20261113; agreements [True, True, True]; skipped draws 1.

- Every-STALE independent XML audit: 20/20 agree; CoM fits independently recomputed from XML origins.

- Final offline artifact validation: {"model_reports": 71, "provenance_files": 71, "source_link_occurrences": 3404, "unique_source_line_targets_checked": 2824, "unresolved_finding_source_references": 0, "all_link_targets_exist_at_exact_shas": true, "raw_com_source_links_checked": true, "workflow_yaml_valid": true}

- Final actual-axis rerun completed all 71 folders; all checked primary axes are explicitly MuJoCo xaxis values. Invariants and counts remain: 3,502 unchanged non-CoM records, 827 preserved raw CoM records/classes, 67 excluded raw CoM findings, 19 resolved by rigid alignment, 587 counted records, same 20 STALE identities / three models, unchanged H1 acceptance. All 119 freshly compiled self-comparisons have zero findings.
- Final full suite: **61 passed in 16.62 seconds**. Final seeded XML check **3/3 agree**, every-STALE XML audit **20/20 agree**; direct CoM fits are independently recomputed from XML origins. Final artifact check confirms **71 reports, 71 provenance files, 3,404 source-link occurrences and 2,824 unique exact-SHA line targets**, including raw CoM, zero unresolved links. Final offline report render succeeded. README, summary and the external publication draft use the final 587 / 603-half / 568-double counts and describe convention and insufficient-coverage exclusions.
- Resource check before staging: **3.1 GiB project use**. No new network acquisition, GPU or MLX use in this revision. Source clones and all temporary expansions remain ignored. Another job was running on this machine and was not accessed.
- Git identity rechecked: configured and effective author/committer **Dorian <263460420+sudorian@users.noreply.github.com>**. Hook directory is the project .git/hooks with only inactive sample hooks. Preparing exactly one local commit, with the message `robot-model-drift: provenance and drift survey of MuJoCo Menagerie`; no push, issue, comment or pull request will be performed. Staging is restricted to the project deliverables, code, tests and configuration; ignored source models/environment are excluded.

- Precommit `git diff --cached --check` returned 2 for trailing spaces on empty network-output log lines and extra blank EOF lines in generated reports / two source files. The chained staging summary did not run. Normalized whitespace only, adjusted the log/report writers to avoid reintroducing it, and will rerun the staging check. No numeric result, source link, or quoted value changed.

- Restaged whitespace-clean deliverables: `git diff --cached --check` passes. **194 files** staged: 71 model reports, 71 provenance files plus source/tests/configuration and remaining report artifacts. The staged-name audit confirms no cache, virtual environment, URDF/xacro/XML model file, mesh or temporary file. Next action is a single local commit with the stated message; no publication or push was performed.

## 2026-11-14 — publication privacy cleanup

- Initial offline Git and resource checks succeeded. The optional `rg --files -g AGENTS.md` discovery returned status 1 because no applicable file was present. Host resource figures are omitted from the publication log.
- Converted local paths to repository-relative paths in the existing work log and saved structured results. Targeted prose edits remove unrelated-project names, host disk figures, process identifiers and conversational approval history; methods, failures, model measurements, project sizes/budget and every network-command entry are retained. No network command was run for this cleanup.
- Added shared sanitization at log, JSON, YAML and Markdown output boundaries. Compiler paths and subprocess arguments remain unchanged in memory. Initial publication/logger regression checks: **5 passed in 0.24 seconds**.

- Offline report regeneration completed for all 71 model reports, provenance files and summary. The summary and H1 acceptance JSON are byte-for-byte unchanged. Full tests, including real H1 acceptance and publication regressions: **64 passed in 13.87 seconds**. Git network protocols and lazy fetching were disabled.
- Repeated privacy checks over all 196 tracked/new publication files found zero remaining audited local-path occurrences (previously 808), host-disk passages (6), process-ID passages (2), unrelated-project mentions (3), default-interpreter/Git-version passages (1) and OS-family mentions (1). Existing 1,170 network-command log entries and 1,166 failure-bearing log lines are retained.
- Saved-result comparison permits only path-string substitutions: all numeric values, source choices, classifications and findings are unchanged. Total findings remain 587; the same 20 STALE records comprise Seeed 7, Lite6 6 and xArm7 7. The complete H1 result is unchanged: NO MATCHING SOURCE, M=51.437 kg and H=59.33801256637062 kg.
- Preparing an amendment of the single local commit with its existing message, author/committer identity and original timestamps/timezone. Source caches and virtual environment remain ignored; no network, push or external publication was performed.

## 2026-11-14 — manual workflow and publication archive

- Moved the unpublished issue text outside the repository with unchanged contents and removed repository references to its file. The workflow now has only a manual dispatch trigger; scheduled execution remains disabled until tested. README describes the manual trigger. No network command was run.
- Validation: **64 tests passed in 14.66 seconds**, including offline H1 acceptance. Parsed workflow triggers contain only `workflow_dispatch`; no repository reference to the external draft file remains. The moved file matches its previous committed bytes.
- Preparing the single-commit amendment with unchanged message and author/committer identity. The final ZIP will be generated outside the repository from amended HEAD with `git archive`, then checked for draft, cache and Git-metadata exclusions. No push is performed.
