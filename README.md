# robot-model-drift

This tool checks whether a robot simulation model has fallen behind its manufacturer’s robot description. It starts with MuJoCo Menagerie and compares compiled physical values across source history. It does not change any model or contact its maintainers.

The survey covers all **71 model folders** at Menagerie commit [`370c439`](https://github.com/google-deepmind/mujoco_menagerie/tree/370c43965323c0944b433b202aac5058b5f907a9), excluding `test/`. It detects **20 STALE quantity records across three models**: seven inertia/centre-of-mass records in `seeed_rebot_devarm`, six effort-limit declarations in `ufactory_lite6`, and seven in `ufactory_xarm7`. Quantity records can describe related effects and are not independent defects. URDF effort declarations are reported separately from quantities enforced by MuJoCo.

H1 reproduces **51.437 kg versus 59.338012566 kg**, with **3.387 kg more per leg** and different hip-pitch ranges. Its original URDF was provided privately by Unitree. None of the nine public revisions matches all comparable values, so H1 is **NO MATCHING SOURCE** and contributes no STALE findings. The [H1 report](report/unitree_h1.md) includes all nine revisions and quotes the README’s source statement.

The tool compiled a comparable current upstream description for **47/71 folders**. Coverage is **32 complete, 15 with partial history, 19 without a machine-readable upstream, and 5 whose identified current source could not compile**. There are seven pinned sources, thirteen dated matches, no proxies, seventeen exhaustive no-matches, and thirty-four unresolved/unknown sources (including unavailable upstreams). Some of those 47 comparisons have only aggregate quantities or limited body matches; the unmatched lists define their actual coverage. These limits prevent a claim that all remaining models are current.

At default tolerance there are **587 reported quantity records** across all classes. At half tolerance, **16 finding memberships and 7 classifications change** (603 records, 20 STALE); at double tolerance, **19 memberships and 4 classifications change** (568 records, 19 STALE). The three affected STALE models remain the same. A membership change means a quantity crosses the reporting threshold; a class change means its three-way label changes.

The kinematic guard flags **six models** with convention differences and **eleven** with insufficient alignment coverage. It excludes **67 raw CoM differences** from counts and largest discrepancies. Rigid alignment resolves another **19** previously reported CoM differences, reducing the total from 673 to 587 with no new records. All **827 raw CoM records and their raw classes** are preserved. All **3,502 non-CoM records** keep their values and classes, including masses, principal moments, ranges and limits. The [before/after validation](report/kinematics_validation.json) records these checks and confirms the same three STALE models and unchanged H1 acceptance.

Read the [one-row-per-model summary](report/summary.md), [three independent XML checks](report/cross_checks.md), [additional audit of all STALE records](report/stale_cross_checks.md), and [full run log](NOTES.md). Each model report links every finding to source lines at full commit SHAs. The companion files in `provenance/` record source selection, dates, evidence, errors and compilation processing. `report/results.json` contains all measured snapshots, comparisons, unmatched elements and unavailable quantities.

The method compares three values for each available quantity:

- **M:** the Menagerie model.
- **S:** the selected manufacturer source revision.
- **H:** the manufacturer repository’s latest default-branch revision when acquired for this run.

Source selection uses these rules in order:

1. **pinned:** use the commit named by the model README.
2. **dated match:** use the newest matching revision at or before the Menagerie change that introduced its current physical values.
3. **proxy:** only when there is no public revision from before that change, use the earliest later revision that matches. Every classification then carries **“(inferred)”**, and both dates are reported.
4. **none:** every successfully evaluated revision differs. Report **NO MATCHING SOURCE**, with M/H differences, and never count it as STALE.

A match requires all comparable quantities to meet tolerance and physical bodies/movable joints to be accounted for. An equal total mass alone is insufficient. If missing files, invalid historical descriptions or unresolved history prevent selecting or rejecting a source, provenance is **unknown**, with the coverage failure reported. If an older nonmatching revision exists but only a later revision matches, the explicit proxy rule does not apply; this case remains unknown. A pinned commit is retained even when its values differ from M.

| Three-way comparison | Class |
|---|---|
| M≈S and S≈H | unchanged |
| M≈S and S≠H | STALE |
| M≠S and S≈H | derivation difference: documented or undocumented |
| M≈H and M≠S | already synced |
| M≠S and S≠H, with M≠H | needs a human look |

A documented derivation label requires the README to identify the affected entity and quantity explicitly. Broader conversion instructions remain visible for manual review.

Default tolerances are stated below. Relative thresholds use the larger absolute value on the two sides; vectors must meet the threshold at each component, except CoM, which uses Euclidean distance.

| Quantity | Default tolerance |
|---|---|
| Total, body and subtree mass | larger of 0.5% or 0.001 kg |
| Body and total centre of mass | 0.0005 m |
| Sorted principal moments about the CoM | 1% |
| Angular joint-range endpoints | 0.005 rad |
| Prismatic joint-range endpoints | 0.0005 m |
| Effort, force and velocity limits | 1% |
| Kinematic maximum body-origin residual (quality guard) | 0.005 m |
| Matched signed hinge/slide axis angle (quality guard) | 0.005 rad |

Physical thresholds are configurable through `--mass-relative`, `--mass-absolute`, `--com-absolute`, `--inertia-relative`, `--range-absolute`, `--slide-range-absolute` and `--limit-relative`. The quality guards use `--kinematic-residual` (maximum origin residual in metres) and `--kinematic-axis-angle` (radians). `--tolerance-scale` multiplies the physical thresholds; quality thresholds remain fixed. Each survey reselects provenance and recalculates findings at half and double its physical tolerances, reporting changes in classes and finding membership.

MuJoCo 3.3.7 compiles both MJCF and URDF with `fusestatic=false`. The tool compares body/subtree/total masses, world-frame body and total CoM at zero joint position, sorted inertia eigenvalues, joint ranges and available limits. It first registers both models to the same matched root frame, then fits a proper rigid transform with Kabsch over matched zero-pose body origins for M/H and M/S. CoM values use that fit only when the maximum per-origin residual and signed matched joint axes from MuJoCo’s zero-pose `xaxis` pass the quality guard. Reflections are not allowed. A failed fit/axis check is marked **kinematic convention differs**. Fewer than three non-collinear origins are marked **insufficient kinematic coverage**, because no unique 3-D alignment can be certified. Both cases exclude CoM records from finding counts and the largest-discrepancy column. Each model report retains the raw numbers, fitted transform, per-origin residuals, axis vectors and exclusion reason. Original world coordinates remain in JSON.

Mass, subtree mass, principal moments, raw ranges and limit comparisons retain their previous values and source selection. The original raw-value provenance matching rules remain unchanged; the new guard controls reported CoM. In particular, RBY1’s range difference is retained with a convention-review flag. Bodies and joints match by name first, then by a unique compatible kinematic tree. Unmatched elements are listed.

Xacro expands using the pinned PyPI package. Its recorded arguments select one assembly; alternative manufacturer options can produce different physics, so a no-match does not rule out every possible macro configuration. Package paths resolve inside the cloned source repository, and effective arguments are recorded. Three standalone assembly recipes in `config/xacro_recipes.yaml` supply manufacturer macro arguments for Lite6, xArm7 and Shadow Hand; they contain no physical values. The history search covers the source file and its discovered includes, YAML inputs and retained geometry resources. Identical fully expanded compiler inputs can reuse a compiled result. Exact file renames are followed; unresolved or modified-content renames limit confidence.

Geometry is stripped only when every body has an explicit inertial and the compiler is not instructed to derive inertia from geometry. Otherwise it is retained, resolved at the same commit, and compiled. COLLADA meshes are converted on the CPU when needed, preserving scene transforms. All such processing is recorded. Unresolvable meshes or invalid inertias produce coverage gaps rather than guessed numbers.

To run, use Python 3.11 and Git. All work stays in this directory. Source repositories and temporary expanded files live under ignored `.cache/`; no source model files are part of this project’s published files. Logs, saved error strings and generated reports express local paths relative to the repository root; external Python interpreter paths are displayed as `python3.11`. This changes only published text, not compiler inputs or commands.

```sh
python3.11 -m venv .venv
# Record this network command and its purpose before installing.
printf '\n- Network: pinned dependency install from PyPI (command below).\n' >> NOTES.md
printf '%s\n' 'nice -n 15 .venv/bin/python -m pip install --index-url https://pypi.org/simple --no-cache-dir -r requirements.txt' >> NOTES.md
nice -n 15 .venv/bin/python -m pip install --index-url https://pypi.org/simple --no-cache-dir -r requirements.txt

# Acquire source through logged GitHub clone/fetch commands; run H1 first.
nice -n 15 ./drift check unitree_h1 --fetch --menagerie-ref 370c439
nice -n 15 ./drift acceptance
nice -n 15 ./drift check all --fetch --menagerie-ref 370c439
nice -n 15 ./drift report
nice -n 15 ./drift cross-check
nice -n 15 ./drift cross-check --all-stale
nice -n 15 env OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 .venv/bin/python -m pytest -q
```

`./drift` caps BLAS thread counts at one. The scanner is serial and uses no viewer, GPU or MLX. New clones use `--filter=blob:none`, with separately logged small-blob bootstrap and targeted resource fetches. Rename history recovers missing blobs in batches of up to 64, using a streamed tree-metadata index of related file versions and directory neighbors. Each source has a per-run budget of 4,096 requested objects and 2 GiB of added object-store bytes; Git pack files are limited during reception, and batch counts/bytes are logged. Reaching a cap or encountering an unavailable object preserves the explicit `history_incomplete` fallback. README-pinned commits missing from branch history are fetched explicitly by full SHA into the source cache without moving its default HEAD. A disk guard stops network acquisition at 12 GB of project use or below 3 GB free, before the 15 GB project cap. Actual final disk use is recorded in NOTES.md.

To rerun the saved survey at exactly its existing source commits with a new comparison guard, use `nice -n 15 ./drift check all --recompare --menagerie-ref 370c439`. This recompiles every standalone Menagerie variant and the available selected M/S/H inputs, verifies unchanged physical values, and reuses historical compiled snapshots while re-evaluating provenance, kinematic consistency and sensitivity. The current kinematic revision was surveyed in this frozen mode; no source tips were moved or fetched. Acquisition/compilation gaps from the original survey remain explicit. `--recompare` cannot be combined with `--fetch` or `--resume`.

Without `--fetch`, checks use only cached Git objects and do no networking. With `--fetch`, existing source default branches are refreshed explicitly. Omit `--menagerie-ref` for current Menagerie. `--resume` retains completed model entries after an interrupted run; start without it when changing the target revision or tolerances. `check` prints a final count per status and exits 2 only if a selected model has status `error`; `incomplete`, `partial history` and `unknown upstream` are reported coverage, so they exit 0. Resumed checks include saved statuses in that summary. Failed acceptance or direct-XML checks still exit 2. `report` renders saved results offline, including cached source links. The H1 acceptance fixture uses fixed Menagerie and Unitree commits so later changes cannot alter its nine-revision regression test.

Offline regression suite: **83 tests passed**. Published survey verification: **119 variant self-comparisons had zero findings**, the three seeded random XML checks agreed, and all **20 STALE records** also agreed in a separate direct-XML audit. An offline link audit checked **2,824 unique exact-SHA source-line targets**, with no unresolved finding references.

Tests cover every available Menagerie variant against itself, synthetic changes across the quantity families and classification table, proxy and no-match provenance, name/tree matching, geometry safeguards, macro expansion, source links, H1, rigid/reflection registration, signed axes and CoM exclusion. Direct CoM checks independently fit XML-derived origins rather than trusting the cached transform. Three seeded random findings are independently recomputed from XML without importing MuJoCo; skipped draws needing geometry inference are disclosed. This checks the extractor rather than the source-identification judgment.

Coverage has limits. Some robots have no public machine-readable source; some source histories cannot compile with the pinned tools. The report lists every such model. Drift uses one compatible standalone variant per folder; every standalone variant is self-checked. Zero pose does not test dynamics, actuator control behavior, contact, mesh appearance or closed-loop mechanism equivalence. URDF effort/velocity tags are declarations ignored by MuJoCo; only supported direct scalar MJCF actuator envelopes/joint force caps are compared. Tendon, site and complex actuator limits can remain unavailable. Missing limits are never interpreted as zero. Dates and matching establish evidence for source selection, not proof of the author’s private conversion inputs.

The [workflow](.github/workflows/weekly.yml) runs only when started manually with `workflow_dispatch`. It uses `ubuntu-24.04` and the v6 checkout, Python setup and artifact-upload actions (Node 24). It reruns H1, tests, the survey and direct XML checks, then uploads reports as artifacts with read-only repository permissions. Scheduled runs remain disabled; coverage gaps are reported without failing the survey step.

The six-model cold-cache regression recorded in [NOTES.md](NOTES.md) completed with exit 0 and no history-coverage warnings. KUKA iiwa 14, low_cost_robot_arm, both Robotiq 2F85 models and Unitree Go1 reproduce the published statuses and class counts. i2rt differs: its older `d4efb66` pin is fetchable by full SHA but absent from all advertised branch/tag histories. The selected camera/gripper variant uses its separate README pin, `120c3c8`, and now reports pinned provenance, one “needs a human look” record and six unavailable/unknown records. Its preferred URDF history contains a missing mesh at `db582ea`, so status remains partial history despite complete Git history traversal. The published i2rt MJCF comparison had four NO MATCHING SOURCE records. These acquisition checks leave the published `report/` and `provenance/` files unchanged.

License: MIT, copyright sudorian.
