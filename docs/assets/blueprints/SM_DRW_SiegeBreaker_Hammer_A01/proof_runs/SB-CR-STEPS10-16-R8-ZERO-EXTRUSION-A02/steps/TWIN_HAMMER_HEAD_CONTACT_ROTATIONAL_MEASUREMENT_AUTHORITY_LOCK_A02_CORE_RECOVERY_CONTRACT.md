# Twin Hammer Head, Contact, And Rotational Measurement Authority Lock A02 Core Recovery Contract

- Date: `2026-07-24`
- Run: `SB-CR-STEPS10-16-R8-ZERO-EXTRUSION-A02`
- Assets:
  - `SM_DRW_SiegeBreaker_Hammer_A01`
  - `SM_DRW_FoeHammer_Hammer_A01`
- Artifact status:
  `candidate Core recovery contract pending exact-hash Flamestrike execution approval`
- Current authorized action:
  `draft and visibly review this one recovery contract only`
- A01 status: `invalid; preserved as proof-only failure evidence`
- A02 authority lock created by this draft: `false`
- Measurement authority promoted by this draft: `false`
- Production authority: `false`
- Builder authority: `false`
- Blender authority: `false`
- Geometry authority: `false`
- Imagery / render authority: `false`
- Export authority: `false`
- Step 13 / Step 14 authority: `false / false`
- Unreal authority: `false`

## Current Draft Authorization

Codex asked:

> Do you approve drafting exactly one candidate Core recovery contract for a
> clean A02 lock attempt from the last valid approved measurement state,
> preserving A01 as invalid and performing no production, Blender, geometry,
> imagery, rendering, export, Step 13/14, or Unreal work?

Flamestrike replied:

> approved

That reply authorizes only creation and visible review of this candidate
recovery contract. It does not authorize A02 execution, creation of an A02
lock, modification of A01, authority promotion, or production.

## Core Recovery Assessment

### Last Known Core-Valid State

The last valid authority state is:

`Flamestrike-approved candidate measurement resolution; valid authority lock absent; production remains blocked`

Its controlling candidate manifest is:

`TWIN_HAMMER_HEAD_CORRESPONDENCE_CONTACT_ROTATIONAL_STATION_AUTHORITY_A01.json`

SHA-256:

`7a7c633587b4d39797339077685109eb28c31ca8e28e36f1e888d0506fec2ceb`

The manifest's independent audit remains:

`PASS 261/261`

### First Failed Action

A01 wrote a candidate authority-lock record, then ran an independent
validation. Checks `E08` and `E09` attempted to count zero matches with:

- an `rg -c` pipeline; and
- an `rg -ci` pipeline.

For zero matches, the pipelines emitted no numeric line. The later integer
assertions received empty operands and failed.

The contracted A01 result is:

`FAIL 59/61`

### Root Cause

The validation logic did not normalize a zero-match result into an explicit
integer `0`.

The failure was in the validation evaluator, not in discovered production or
visual output. A read-only diagnosis observed:

- new A01 project authority-lock tools: `0`; and
- forbidden A01 output extensions: `0`.

The diagnosis cannot be retroactively substituted for the failed A01
validation.

### Affected Outputs

| Artifact | Status |
|---|---|
| A01 lock JSON | `invalid; proof only` |
| A01 validation JSON | `proof only; FAIL 59/61` |
| A01 output record | `proof only; failed execution` |
| A01 review | `blocked review` |
| A01 handoff | `proof only; failed-lock handoff` |
| Approved measurement manifest | `valid approved candidate; unchanged` |
| Prior measurement independent audit | `proof only; PASS 261/261; unchanged` |

No geometry, imagery, render, Blender, export, Step 13/14, or Unreal output
was affected. This was a validation failure, not a production-geometry drift
event.

### Smallest Sufficient Recovery

Create a clean A02 lock package from the last valid approved measurement
manifest, with:

1. no A01 lock content used as numeric or semantic authority;
2. no modification or repair of A01;
3. deterministic counters that always emit one nonnegative integer;
4. counter self-tests before any A02 lock is written;
5. the same five explicitly approved measurement subsets;
6. independent fail-closed validation; and
7. no production authority.

## A01 Preservation And Exclusion

All A01 records must remain byte-identical.

A02 may read A01 records only to:

- verify their exact hashes;
- record failure lineage;
- prove that A01 remains invalid; and
- enforce the anti-repeat counter rule.

A02 must not:

- copy the A01 lock as a seed or template;
- source any numeric value from the A01 lock;
- source any semantic authority from the A01 lock;
- modify, rename, replace, delete, or quarantine A01 further;
- rerun the A01 validation;
- reinterpret A01 as passing;
- repair A01 forward; or
- cite A01 as authority.

Every A02 authority value must replay directly from the hash-locked approved
measurement manifest or an independently cited governing authority.

## Governing Input Package

Every future A02 execution input below must exist and match its cited hash.
Any mismatch is a preflight block.

| ID | Record | SHA-256 | Role |
|---|---|---|---|
| `H01` | `AGENTS.md` | `5d2d2637a58113f0a6f5ec92e40d8bb2bda9e03fb58b4868a0d9dfbb3b57ad55` | Core and closed-world control |
| `H02` | `manifests/SHARED_DEPTH_RECOVERY_BLUEPRINT_A01_AUTHORITY_LOCK.json` | `6889b826481e5e11dd10775f2b81467b1014687b7fda9ebbff62d519bfff09bc` | Shared-depth and production-boundary authority |
| `H03` | `manifests/SHARED_DEPTH_RECOVERY_BLUEPRINT_A01_AUTHORITY_LOCK_VALIDATION.json` | `154ac1ed96c437fe971dfd27c415141f70ea08ae8ee43ae72251d1b30a016739` | Proof-only shared-depth validation |
| `H04` | `steps/TWIN_HAMMER_HEAD_CORRESPONDENCE_CONTACT_AND_ROTATIONAL_STATION_AUTHORITY_RESOLUTION_A01_CONTRACT.md` | `1352b2c008c30bda6e2755fc568126e62fc65e049b8a79c13808f4ea7e1a4548` | Consumed measurement contract |
| `H05` | `manifests/TWIN_HAMMER_HEAD_CORRESPONDENCE_CONTACT_ROTATIONAL_STATION_AUTHORITY_A01.json` | `7a7c633587b4d39797339077685109eb28c31ca8e28e36f1e888d0506fec2ceb` | Exact approved candidate measurement authority source |
| `H06` | `manifests/TWIN_HAMMER_HEAD_CORRESPONDENCE_CONTACT_ROTATIONAL_STATION_AUTHORITY_A01_INDEPENDENT_AUDIT.json` | `837ebb6778867efa4f4228d30ac2f7d8e3c48f4303a3ea651b675f311995eaaa` | Proof only; `261/261 PASS` |
| `H07` | `steps/TWIN_HAMMER_HEAD_CORRESPONDENCE_CONTACT_AND_ROTATIONAL_STATION_AUTHORITY_RESOLUTION_A01_OUTPUT_RECORD.md` | `26941ec8eee3dc55494d8fe0dbc7d5079f6cad47642d2f3df8672356de122c5e` | Flamestrike measurement decision |
| `H08` | `review/TWIN_HAMMER_HEAD_CORRESPONDENCE_CONTACT_ROTATIONAL_STATION_AUTHORITY_A01_REVIEW.md` | `24d0e65baf95dc657f08947bffd7e41596dcd06cf3d3f1463d857b40ad859872` | Visibly reviewed measurement evidence |
| `H09` | `handoffs/TWIN_HAMMER_HEAD_CORRESPONDENCE_CONTACT_ROTATIONAL_STATION_AUTHORITY_A01_HANDOFF.md` | `d6938adf4d4614bbf8ccb5b2a526b54937e1f8a60059092e32cc667f02a8f6be` | Approved scope handoff |
| `H10` | `Tools/DCC/measure_twin_hammer_head_contact_rotational_authority_a01.py` | `8d9abde1846b3d412af4dc0684b492e29f7aa7a59a83c7f324c88d6cd07d77cb` | Immutable measurement resolver; must not run |
| `H11` | `Tools/DCC/audit_twin_hammer_head_contact_rotational_authority_a01.py` | `75d3b54b4d6f5d476be1fec543aeaa32d3416a4e0ec2dd0ccb60da3d5b9bed2e` | Immutable prior auditor; must not run |
| `H12` | `steps/TWIN_HAMMER_HEAD_CONTACT_ROTATIONAL_MEASUREMENT_AUTHORITY_LOCK_A01_CONTRACT.md` | `03f0f933aadc516ba639fc47450465b2144f8eb828642a36d88dd7cbbe93e9e6` | Consumed A01 contract; failure lineage only |
| `H13` | `manifests/TWIN_HAMMER_HEAD_CONTACT_ROTATIONAL_MEASUREMENT_AUTHORITY_LOCK_A01.json` | `e57b88d53724f69b4d7179a2616316820f9ef669699e074d5c74aa1ea59c6cd9` | Invalid A01 lock; reference only |
| `H14` | `manifests/TWIN_HAMMER_HEAD_CONTACT_ROTATIONAL_MEASUREMENT_AUTHORITY_LOCK_A01_VALIDATION.json` | `25b8eea66a442c512e8e59dd02fb48c2487e708495a40e88e40e4e03379d40b5` | Proof-only A01 failure |
| `H15` | `steps/TWIN_HAMMER_HEAD_CONTACT_ROTATIONAL_MEASUREMENT_AUTHORITY_LOCK_A01_OUTPUT_RECORD.md` | `993a70d9d0616e0a8e047f1c7769398feebe90898b6eb39616f35044f9bd51d3` | A01 failed-execution record |
| `H16` | `review/TWIN_HAMMER_HEAD_CONTACT_ROTATIONAL_MEASUREMENT_AUTHORITY_LOCK_A01_REVIEW.md` | `2c14b0664f29ad6b0910d2363f61273305d15ea1fd1805ab7b2da4b4043fe953` | A01 blocked review |
| `H17` | `handoffs/TWIN_HAMMER_HEAD_CONTACT_ROTATIONAL_MEASUREMENT_AUTHORITY_LOCK_A01_HANDOFF.md` | `121d31a22ee1eec91af4d215bae3b2e291d065fb7310e5cb060a67bc6da07f29` | A01 failed-lock handoff |
| `H18` | `manifests/STEP_STATE.json` at draft start | `0e169fe31538fdd9dc715d9ad3523e15914497df6a9e1ee183672315200197da` | Pre-A02 state evidence |

The relevant repository commits are supporting provenance:

- approved measurement package:
  `69846b0b66611d67e4821b8ad38c560a55a75351`;
- A01 candidate contract:
  `87ac6724edeeaa81e09f0690287638d140b30261`; and
- A01 failed-lock evidence:
  `b0a5b983074917e3ba8c362c4dd0f3b4e2e0e63c`.

File hashes remain the controlling evidence.

## Immutable Approved Measurement Source

The approved measurement manifest and its prior audit must remain
byte-identical.

A02 must:

- reference the exact approved manifest path and whole-file hash;
- promote only the explicitly approved subset through an external A02 lock;
- preserve the manifest's internal candidate labels as historical pre-lock
  status;
- never rewrite, regenerate, normalize, trim, or reorder the manifest;
- never rerun the resolver;
- never rerun the prior auditor; and
- invalidate A02 if the manifest whole-file hash changes.

## Exact A02 Partial-Lock Scope

Canonicalization remains exactly:

```text
jq -cS '<selector>' APPROVED_MANIFEST | sha256sum
```

The digest includes the single trailing newline emitted by `jq`.

| Approved subset | Exact selector | SHA-256 |
|---|---|---|
| Source-role split | `.source_role_and_lineage_matrix` | `3d1035aacddad1cae0340a847dbbc750847269b9ed6861650457af822ac29aae` |
| Projected contact and C04 boundary expansion | `.projected_contact_expansion` | `d7192621b27d67002124f09943a6265d90c84bb1191c156dbe5a3d40966d5b3c` |
| C06-C11 station and physical-Z authority | `.c06_c11_half_open_station_table` | `72cc13e2ab54fa132f4dc8675f198d17eb5262b2bd348def3d25147ba7a3a72d` |
| All 155 C08 radius-by-Z rows | `.c08_radius_by_z_table` | `eb82dba6e3d994533cca2150b4194d38ab2024fb8156a78c82bbd0f532c9ca6d` |
| Five governing stop conditions | `.remaining_blocks` | `f260d07eda22ef5faec9047d43a846b31f4849d16d08c1076cb68d1bf880bad4` |

No other manifest section may be promoted.

The complete `rotational_transition_contact_table`, including the
coordinate-equal C08/C09 row at source edge `1110`, remains proof-only
candidate evidence.

## Exact Effective Authority After A Valid A02 Execution

If and only if:

- Flamestrike separately approves this contract's exact SHA-256;
- every preflight and counter self-test passes;
- the A02 lock is written from the approved manifest; and
- independent A02 validation passes exactly `72/72`;

the A02 lock may classify the five approved subsets as:

`authoritative measurement-only partial authority; production remains blocked`

### Source-Role Authority

- New-R8 owns current view-local pixels, contours, component station
  observations, color observations, and view-local measurements.
- The original six-view lineage remains reference only for current numeric
  work.
- Step 09A owns component membership, protected negative space, projected
  boundaries, and source order only.
- Step 09A does not own hidden surfaces, point pairing, or triangulation.
- The shared-depth blueprint owns validation bounds and twin identity only.
- No exact cross-lineage coordinate mapping is created.

### Projected Contact Authority

The following remain exact two-dimensional projected contacts only:

| Contact | Source edge | Half-open intersection | Unit edges |
|---|---:|---|---:|
| `FRONT_C01_C06_CONTACT` | `600` | `[504,619)` | `115` |
| `FRONT_C06_C07_CONTACT` | `670` | `[527,596)` | `69` |
| `FRONT_C12_RESERVED_C01_CONTACT` | `295` | `[487,636)` | `149` |

Total unit edges: `333`.

These records create no 3D contact, point correspondence, surface, common
ring, or triangle.

C04 records remain projected owner boundaries only. The bottom-center record
remains an absence of bottom-specific samples and provides no fill/no-gap
authority.

### C06-C11 Station And Physical-Z Authority

| Component | Source rows |
|---|---|
| `C06_UPPER_HAFT_CAP` | `[600,670)` |
| `C07_HAFT` | `[670,870)` |
| `C07B_HAFT_TO_HANDLE_FERRULE` | `[870,955)` |
| `C08_GRIP` | `[955,1110)` |
| `C09_LOWER_COLLAR` | `[1110,1150)` |
| `C10_POMMEL_BODY` | `[1150,1220)` |
| `C11_POMMEL_TERMINAL_CAP` | `[1220,1271)` |

Exact physical-Z formulas:

```text
600 <= y <= 955:
Z(y) = 132-(y-600)*(7992/42955)

955 <= y <= 1110:
Z(y) = 7980/121-(y-955)*(42/155)

1110 <= y <= 1271:
Z(y) = (1271-y)*(18/121)
```

Continuity is mandatory at `955` and `1110`.

This authority applies only to C06-C11. It does not reconcile the conflicting
head registration at source edge `600`.

### C08 Radius-By-Z Authority

- source rows: `[955,1110)`;
- row count: `155`;
- source axis edge: `x=562`;
- radial scale: `11/136 cm/px`;
- minimum distance: `33 px`;
- maximum distance: `38 px`;
- exact radius range:
  `363/136 cm` through `209/68 cm`; and
- exact row contents:
  immutable manifest and section-digest reference.

No smoothing, interpolation between unrecorded rows, resampling, nearby-row
substitution, or fixed segment count is allowed.

### Authoritative Stop Conditions

All five approved manifest `remaining_blocks` records become authoritative
stop conditions only. They remain unsolved.

## Preserved Non-Authority

### Blueprint block: source authority missing

- complete head XYZ embedding;
- physical head corner incidence;
- hidden-boundary owner;
- bottom center-gap disposition; and
- exact C04 adjacent stone owner and full perimeter incidence.

### Blueprint block: rule missing

- cyclic head boundary incidence;
- hidden-closure equation;
- unequal-radius rotational shoulder/contact equations; and
- terminal-cap closure.

### Blueprint block: source authority conflict

- front global-view source edge `A=600` maps to `114070/1063 cm`;
- later physical station authority maps it to `132 cm`; and
- no approved head-Z reconciliation exists.

### Head And Transition Exclusions

- head boundary samples: `2,566`, all incomplete in XYZ;
- complete head XYZ samples: `0`;
- approved point correspondences: `0`;
- head triangle index triplets: `0`;
- hidden head surfaces: blocked;
- every rotational-transition table row: proof-only candidate evidence;
- unequal-radius shoulders: blocked; and
- terminal-cap closure: blocked.

## Deterministic Counter Recovery Rule

A02 validation must not use:

- `rg -c`;
- `rg -ci`;
- a counter that emits no line for zero matches;
- an unset or empty value interpreted as zero; or
- `|| true` as a substitute for a numeric result.

Every count must be produced by an evaluator that always emits exactly one
nonnegative base-10 integer.

### Required New-Tool Counter

The functional form is:

```text
rg --files Tools/DCC |
awk '/twin_hammer_head_contact_rotational_measurement_authority_lock_a02/ {
  n++
}
END {
  print n+0
}'
```

### Required Forbidden-Extension Counter

The functional form is:

```text
rg --files RUN_ROOT |
awk '
/TWIN_HAMMER_HEAD_CONTACT_ROTATIONAL_MEASUREMENT_AUTHORITY_LOCK_A02/ &&
/\.(png|svg|blend|fbx|glb|uasset|umap|exr|jpg|jpeg|tga|obj)$/ {
  n++
}
END {
  print n+0
}'
```

The actual inline implementation may format the `awk` program differently,
but its matching semantics and `END { print n+0 }` normalization must be
identical.

Every returned value must pass both:

1. exactly one output line matching `^[0-9]+$`; and
2. exact integer comparison with the expected value.

## Mandatory Pre-Writer Counter Self-Tests

Before any A02 lock file is created, the independent evaluator must execute
and pass:

| ID | Test | Exact expected result |
|---|---|---:|
| `Q01` | new-tool counter over zero matching lines | `0` |
| `Q02` | new-tool counter over one synthetic matching line | `1` |
| `Q03` | forbidden-extension counter over zero matching lines | `0` |
| `Q04` | forbidden-extension counter over one synthetic matching `.png` line | `1` |

Each result must be a nonempty single-line base-10 integer.

If any `Q` gate fails:

1. create no A02 lock;
2. record a pre-writer block in the allowed output/handoff/state records;
3. preserve all source evidence;
4. do not adjust and retry inside the same execution; and
5. stop for Flamestrike.

## Future Execution Preflight

A later A02 execution must stop before any writer action unless:

1. Flamestrike approved the exact SHA-256 of this contract for execution.
2. All `H01` through `H18` inputs match.
3. The approved manifest result remains
   `PASS_MEASUREMENT_PROCESS_WITH_PARTIAL_AUTHORITY_RESOLUTION`.
4. The prior measurement audit remains `PASS 261/261`.
5. The approved output decision remains `approved`.
6. All five canonical section digests match.
7. A01 remains exactly `invalid`.
8. A01 remains byte-identical and reference only.
9. `STEP_STATE.json` reports no valid measurement authority lock.
10. Production, builder, Blender, geometry, render, Step 13/14, and Unreal
    authorities remain false.
11. All five A02 future output paths are absent.
12. `Q01-Q04` pass before writer action.
13. A manual recovery checkpoint is created immediately before execution.

Skipped, unreadable, missing, conflicting, or unevaluated gates are failure.

## Exact Allowed Future Outputs

After separate exact-hash approval of this contract, a later execution may
create exactly one clean A02 authority lock:

- `../manifests/TWIN_HAMMER_HEAD_CONTACT_ROTATIONAL_MEASUREMENT_AUTHORITY_LOCK_A02.json`

It may also create only:

- `../manifests/TWIN_HAMMER_HEAD_CONTACT_ROTATIONAL_MEASUREMENT_AUTHORITY_LOCK_A02_VALIDATION.json`
- `TWIN_HAMMER_HEAD_CONTACT_ROTATIONAL_MEASUREMENT_AUTHORITY_LOCK_A02_OUTPUT_RECORD.md`
- `../review/TWIN_HAMMER_HEAD_CONTACT_ROTATIONAL_MEASUREMENT_AUTHORITY_LOCK_A02_REVIEW.md`
- `../handoffs/TWIN_HAMMER_HEAD_CONTACT_ROTATIONAL_MEASUREMENT_AUTHORITY_LOCK_A02_HANDOFF.md`

Minimum `STEP_STATE.json`, recovery-journal, and checkpoint updates are
allowed only to record the observed A02 result and stop state.

No project tool may be created or modified.

## A02 Lock Writer Requirements

The A02 lock must be newly constructed from:

- this exact approved A02 contract;
- the approved measurement manifest;
- the approved measurement-decision records;
- the authoritative shared-depth boundary; and
- direct independent replay.

The A02 writer must not read A01 lock fields as input values.

The A02 lock JSON must contain:

1. schema, date, run, and both asset IDs;
2. artifact status:
   `authoritative measurement-only partial authority; production remains blocked`;
3. this A02 contract's exact approved hash;
4. every `H01-H18` path and hash with A01 records classified reference only;
5. the approved manifest path and whole-file hash;
6. the five exact section selectors and canonical digests;
7. the approved source-role rules;
8. the three projected contacts with `creates_3d_contact=false`;
9. C04 projected-boundary-only and bottom-gap boundaries;
10. seven C06-C11 intervals;
11. eight station edges and three physical-Z formulas;
12. C08 scale, domain, row count, radius range, and section digest;
13. explicit proof-only status for the complete transition table;
14. all five authoritative stop conditions;
15. all authority-boundary booleans;
16. A01 exclusion and non-seeding declarations;
17. invalidation rules; and
18. the next block-resolution gate.

Required authority-boundary booleans:

```text
measurement_partial_authority = true
complete_head_authority = false
head_correspondence_authority = false
head_closure_authority = false
c04_physical_contact_authority = false
rotational_transition_table_authority = false
unequal_radius_transition_authority = false
terminal_cap_closure_authority = false
builder_change_authority = false
builder_run_authority = false
blender_authority = false
geometry_authority = false
imagery_authority = false
render_authority = false
export_authority = false
step_13_authority = false
step_14_authority = false
unreal_authority = false
production_authority = false
```

## Exact Independent Validation Registry

The independent A02 validation must execute exactly `72` checks:

| IDs | Count | Purpose |
|---|---:|---|
| `H01-H18` | `18` | governing input hashes |
| `Q01-Q04` | `4` | deterministic counter self-tests |
| `J01-J02` | `2` | A02 JSON/schema/status |
| `C01-C03` | `3` | contract approval, manifest decision, exact five-section registry |
| `D01-D06` | `6` | five recomputed section digests plus registry equality |
| `S01` | `1` | source-role replay |
| `P01-P07` | `7` | projected contacts, C04 boundaries, bottom gap, non-3D boundary |
| `Z01-Z08` | `8` | intervals, station edges, exact fractions, formulas, continuity |
| `R01-R04` | `4` | C08 rows, scale, range, and no-resampling rules |
| `T01-T02` | `2` | transition-table exclusion |
| `B01-B04` | `4` | five stop conditions, head counts, head-Z conflict |
| `A01` | `1` | complete authority-boundary replay |
| `I01` | `1` | invalidation rule replay |
| `E01-E10` | `10` | source result, prior audit, unchanged inputs, tools/outputs, observations |
| `N01` | `1` | stop and next-gate boundary |

Total:

`18+4+2+3+6+1+7+8+4+2+4+1+1+10+1 = 72`

The validator must:

- be an inline, read-only process;
- not import or execute the resolver;
- not import or execute the prior auditor;
- not import A01 lock content as authority;
- not trust A02 writer-authored pass booleans;
- not create a project validation tool;
- record every check ID and status;
- report exactly `72/72 PASS` or fail;
- treat an empty counter as failure;
- treat a malformed counter as failure;
- treat an extra or missing check ID as failure; and
- stop after any failure without retrying A02 inside the same execution.

### Recovered `E08`

`E08` must:

1. run the required normalized new-tool counter against actual `Tools/DCC`;
2. verify the result is one nonempty integer line;
3. verify the integer is exactly `0`; and
4. record the raw integer string.

### Recovered `E09`

`E09` must:

1. run the required normalized forbidden-extension counter against the actual
   run root;
2. verify the result is one nonempty integer line;
3. verify the integer is exactly `0`; and
4. record the raw integer string.

Neither gate may use the A01 counter expression.

## Result Classification

### Pass

Only exact `72/72 PASS` may make the A02 lock effective as:

`authoritative measurement-only partial authority; production remains blocked`

### Pre-Writer Block

If any input, path-absence, or `Q01-Q04` gate fails:

- do not create the A02 lock;
- preserve exact evidence;
- record the block in allowed records; and
- stop.

### Post-Writer Validation Failure

If the A02 lock is written but any validation check fails:

- classify A02 `invalid`;
- preserve it as failure evidence;
- do not repair forward;
- do not rerun A02;
- do not promote measurement authority; and
- stop for Flamestrike.

### Drift

If execution creates geometry, imagery, solution overlays, candidate
surfaces, inferred coordinates, uncited equations, or production output:

1. stop immediately;
2. identify the last valid state and first drift action;
3. classify and quarantine affected output;
4. record the event in `docs/projects/assetforge/DRIFT_LEDGER.md` and both
   affected asset status records; and
5. do not repair forward.

## Explicitly Forbidden

- editing, deleting, replacing, renaming, or promoting A01;
- using A01 lock content as A02 writer input;
- rerunning A01 validation;
- rerunning the measurement resolver or prior auditor;
- modifying the approved measurement manifest or audit;
- using `rg -c` or `rg -ci` for any A02 validation count;
- interpreting an empty count as zero;
- retrying a failed A02 validator inside the same execution;
- promoting the whole candidate manifest;
- promoting the transition table;
- promoting head correspondence, incidence, closure, or triangles;
- converting a 2D projected contact into a 3D contact;
- treating C04 projected boundaries as physical contact;
- resolving the bottom center gap by inference;
- choosing one conflicting head-Z value without a new approved rule;
- creating or modifying production code;
- opening Blender;
- creating, modifying, copying, relinking, or saving geometry;
- images, image generation, renders, overlays, inferred fills, or previews;
- UV, texture, material, LOD, collision, FBX, GLB, or export work;
- Step 13 or Step 14 advancement;
- Unreal work;
- automatic production-contract drafting;
- automatic authority expansion; and
- self-approval of this contract.

## Review Visibility And Stop

This A02 Core recovery contract is the current review artifact.

It must be opened automatically in a visible desktop text-editor window.
A terminal path or clickable link alone does not satisfy review visibility.

After visible review, stop for:

`approve / revise / reject / blocked`

Approval must identify this contract by exact SHA-256. No A02 action follows
from the present drafting approval.

## Future Checkpoint And Repository Rule

A later approved A02 execution must:

1. checkpoint before any evaluator or writer action;
2. run `Q01-Q04` before the A02 lock path is created;
3. checkpoint after pass, block, validation failure, or drift;
4. stage only the exact dependency-complete approved scope;
5. commit and push only valid scoped tracked records to `assetforge/main`;
6. preserve every unrelated dirty worktree entry; and
7. stop after the A02 review is visibly open.

This candidate recovery contract does not authorize future execution.

## Exact Next Gate

No valid measurement authority lock or production action is active.

The next possible action is separate Flamestrike approval of this contract's
exact SHA-256 for A02 execution.

Even after a valid A02 lock, production remains blocked until the missing
head, C04, rotational-transition, terminal-cap, and head-Z authorities are
resolved through separate approved contracts.
