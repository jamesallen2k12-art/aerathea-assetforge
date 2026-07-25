# Twin Hammer Head, Contact, And Rotational Measurement Authority Lock A03 Core Recovery Contract

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
- A02 status:
  `blocked before writer; no A02 lock or validation exists; preserved as proof-only failure evidence`
- A03 authority lock created by this draft: `false`
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

> Do you approve drafting exactly one candidate A03 Core recovery contract
> that corrects the pre-writer harness, preserves A01/A02 as failure
> evidence, and performs no lock execution or production work?

Flamestrike replied:

> approved

That reply authorizes only creation and visible review of this candidate A03
recovery contract. It does not authorize A03 execution, creation of an A03
lock, modification of A01 or A02, authority promotion, or production.

## Core Recovery Assessment

### Last Known Core-Valid State

The last valid authority state remains:

`Flamestrike-approved candidate measurement resolution; valid authority lock absent; production remains blocked`

Its controlling candidate manifest is:

`TWIN_HAMMER_HEAD_CORRESPONDENCE_CONTACT_ROTATIONAL_STATION_AUTHORITY_A01.json`

SHA-256:

`7a7c633587b4d39797339077685109eb28c31ca8e28e36f1e888d0506fec2ceb`

The manifest's independent audit remains:

`PASS 261/261`

### Preserved A01 Failure

A01 created a candidate lock record, then failed independent validation
`59/61` because two zero-match `rg -c` / `rg -ci` pipelines emitted empty
numeric operands.

The A01 lock remains:

`invalid; proof only`

No A01 result is repaired, rerun, promoted, or used as A03 authority.

### First Failed A02 Action

A02 completed governing-input checks `H01-H18` as `PASS 18/18`.

Immediately afterward, the inline evaluator called `record_preflight` with
two arguments while its implementation referenced a third positional
argument under `set -u`.

The shell terminated with:

```text
environment: line 28: $3: unbound variable
```

The remaining A02 preflight gates and `Q01-Q04` were unevaluated. The A02
contract classified unevaluated gates as failure and prohibited an
in-execution retry.

No A02 lock, validation, or review was created.

### A02 Root Cause

The A02 counter design was correct, but the surrounding pre-writer recorder
interface was not arity-safe.

The failure occurred before any A02 writer action. It was an evaluator
implementation failure, not a measurement, visual, geometry, or production
failure.

### Affected Outputs

| Artifact | Status |
|---|---|
| A02 Core recovery contract | `approved and consumed; reference only` |
| A02 output record | `proof only; pre-writer execution block` |
| A02 handoff | `proof only; pre-writer block handoff` |
| A02 authority lock | `not created` |
| A02 validation | `not created` |
| A02 review | `not created` |
| A01 lock package | `unchanged; invalid / proof only` |
| Approved measurement manifest | `valid approved candidate; unchanged` |
| Prior measurement audit | `proof only; PASS 261/261; unchanged` |

No geometry, imagery, render, Blender, export, Step 13/14, or Unreal output
was affected.

### Smallest Sufficient Recovery

Create a clean A03 lock package from the last valid approved measurement
manifest, with:

1. no A01 or A02 record used as numeric or semantic measurement authority;
2. no modification, repair, or rerun of A01 or A02;
3. one arity-guarded gate recorder for every execution gate;
4. mandatory recorder self-certification before official preflight;
5. deterministic counters that always emit one nonnegative integer;
6. the same five explicitly approved measurement subsets;
7. independent fail-closed validation; and
8. no production authority.

## A01 And A02 Preservation And Exclusion

All A01 and A02 records must remain byte-identical.

A03 may read A01 and A02 records only to:

- verify exact hashes;
- record failure lineage;
- prove that A01 remains invalid;
- prove that A02 stopped before writer and created no lock;
- enforce the two anti-repeat rules; and
- prove that neither failed attempt supplies authority.

A03 must not:

- copy the A01 lock or A02 contract as a lock seed or value template;
- source any numeric measurement value from an A01 or A02 lock-attempt
  record;
- source any semantic measurement authority from A01 or A02;
- modify, rename, replace, delete, or further quarantine A01 or A02;
- rerun either failed evaluator;
- reinterpret either failed attempt as passing;
- repair either attempt forward; or
- cite either attempt as measurement authority.

Every A03 authority value must replay directly from the hash-locked approved
measurement manifest or an independently cited governing authority.

## Governing Input Package

Every future A03 execution input below must exist and match its cited hash.
Any mismatch is a pre-writer block.

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
| `H12` | `steps/TWIN_HAMMER_HEAD_CONTACT_ROTATIONAL_MEASUREMENT_AUTHORITY_LOCK_A01_CONTRACT.md` | `03f0f933aadc516ba639fc47450465b2144f8eb828642a36d88dd7cbbe93e9e6` | A01 failure lineage only |
| `H13` | `manifests/TWIN_HAMMER_HEAD_CONTACT_ROTATIONAL_MEASUREMENT_AUTHORITY_LOCK_A01.json` | `e57b88d53724f69b4d7179a2616316820f9ef669699e074d5c74aa1ea59c6cd9` | Invalid A01 lock; reference only |
| `H14` | `manifests/TWIN_HAMMER_HEAD_CONTACT_ROTATIONAL_MEASUREMENT_AUTHORITY_LOCK_A01_VALIDATION.json` | `25b8eea66a442c512e8e59dd02fb48c2487e708495a40e88e40e4e03379d40b5` | Proof-only A01 validation failure |
| `H15` | `steps/TWIN_HAMMER_HEAD_CONTACT_ROTATIONAL_MEASUREMENT_AUTHORITY_LOCK_A01_OUTPUT_RECORD.md` | `993a70d9d0616e0a8e047f1c7769398feebe90898b6eb39616f35044f9bd51d3` | A01 failed-execution record |
| `H16` | `review/TWIN_HAMMER_HEAD_CONTACT_ROTATIONAL_MEASUREMENT_AUTHORITY_LOCK_A01_REVIEW.md` | `2c14b0664f29ad6b0910d2363f61273305d15ea1fd1805ab7b2da4b4043fe953` | A01 blocked review |
| `H17` | `handoffs/TWIN_HAMMER_HEAD_CONTACT_ROTATIONAL_MEASUREMENT_AUTHORITY_LOCK_A01_HANDOFF.md` | `121d31a22ee1eec91af4d215bae3b2e291d065fb7310e5cb060a67bc6da07f29` | A01 failed-lock handoff |
| `H18` | `steps/TWIN_HAMMER_HEAD_CONTACT_ROTATIONAL_MEASUREMENT_AUTHORITY_LOCK_A02_CORE_RECOVERY_CONTRACT.md` | `94ece533df7fb25268df41c5911b1512d10619ffc5d7e48431152acfc43ae96d` | A02 control and failure lineage only |
| `H19` | `steps/TWIN_HAMMER_HEAD_CONTACT_ROTATIONAL_MEASUREMENT_AUTHORITY_LOCK_A02_OUTPUT_RECORD.md` | `67a2119d1d7573bb7a57fe8dc8200cc20db39edb34ed76ab58c44e982133e4da` | A02 pre-writer block evidence |
| `H20` | `handoffs/TWIN_HAMMER_HEAD_CONTACT_ROTATIONAL_MEASUREMENT_AUTHORITY_LOCK_A02_HANDOFF.md` | `08996b82a6ac1d03fd7b58d33ff4640df5f46f599640024816343f0cfd244fa9` | A02 blocked-execution handoff |
| `H21` | `manifests/STEP_STATE.json` at A03 draft start | `4a9401ca6ff986ed66856fdba4de8ad280106fb5e68f3755e0aef741deb39868` | Pre-A03 stop-state evidence |

Relevant repository commits are supporting provenance:

- approved measurement package:
  `69846b0b66611d67e4821b8ad38c560a55a75351`;
- A01 failed-lock evidence:
  `b0a5b983074917e3ba8c362c4dd0f3b4e2e0e63c`;
- A02 Core recovery contract:
  `f38f5c4578fb3da89e22f5dd5cd6e89a985fd7d7`; and
- A02 pre-writer block evidence:
  `dd6b9939cd6691741946df7c800dfa0fd3f84fed`.

File hashes remain the controlling evidence.

## Immutable Approved Measurement Source

The approved measurement manifest and its prior audit must remain
byte-identical.

A03 must:

- reference the exact approved manifest path and whole-file hash;
- promote only the explicitly approved subset through an external A03 lock;
- preserve the manifest's internal candidate labels as historical pre-lock
  status;
- never rewrite, regenerate, normalize, trim, or reorder the manifest;
- never rerun the resolver;
- never rerun the prior auditor; and
- invalidate A03 if the manifest whole-file hash changes.

## Exact A03 Partial-Lock Scope

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

## Exact Effective Authority After A Valid A03 Execution

If and only if:

- Flamestrike separately approves this contract's exact SHA-256;
- all `K`, `H`, `F`, and `Q` pre-writer gates pass;
- the A03 lock is written directly from the approved manifest; and
- independent A03 validation passes exactly `91/91`;

the A03 lock may classify the five approved subsets as:

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

Every contact has `creates_3d_contact=false`.

These records create no 3D contact, point correspondence, surface, common
ring, or triangle.

C04 records remain projected owner boundaries only:

| Candidate side | Position | Source edge | Owner run | Unit edges |
|---|---|---:|---|---:|
| metal center piece | top | `241` | `[504,557)` | `53` |
| metal center piece | bottom | `651` | `[500,557)` | `57` |
| rune | top | `241` | `[557,620)` | `63` |
| rune | bottom | `651` | `[557,622)` | `65` |

They create no physical C04 contact or perimeter incidence.

The bottom-center record remains:

- sample count: `0`;
- classification:
  `recorded absence of bottom-specific samples`; and
- fill/no-gap authority: `false`.

### C06-C11 Station And Physical-Z Authority

| Component | Source rows | Upper Z | Lower Z | Length |
|---|---|---|---|---|
| `C06_UPPER_HAFT_CAP` | `[600,670)` | `132/1` | `1022124/8591` | `111888/8591` |
| `C07_HAFT` | `[670,870)` | `1022124/8591` | `702444/8591` | `319680/8591` |
| `C07B_HAFT_TO_HANDLE_FERRULE` | `[870,955)` | `702444/8591` | `7980/121` | `135864/8591` |
| `C08_GRIP` | `[955,1110)` | `7980/121` | `2898/121` | `42/1` |
| `C09_LOWER_COLLAR` | `[1110,1150)` | `2898/121` | `18/1` | `720/121` |
| `C10_POMMEL_BODY` | `[1150,1220)` | `18/1` | `918/121` | `1260/121` |
| `C11_POMMEL_TERMINAL_CAP` | `[1220,1271)` | `918/121` | `0/1` | `918/121` |

Exact station edges:

`600, 670, 870, 955, 1110, 1150, 1220, 1271`

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

## Recovered Pre-Writer Harness Contract

### One Recorder Only

The future A03 evaluator must use one gate recorder for every `K`, `H`, `F`,
`Q`, and post-writer validation check.

No separate `record_preflight` function is permitted.

The recorder must:

1. check `"$#"` before dereferencing any positional argument;
2. require exactly three arguments;
3. emit a deterministic arity error and return `97` on any other arity;
4. require nonempty gate ID, outcome, and detail;
5. accept only `PASS` or `FAIL` as an outcome;
6. increment one official total exactly once per official gate;
7. increment the pass total only for `PASS`;
8. append exactly one structured record per official gate; and
9. never infer a missing argument.

Reference interface:

```bash
record_gate() {
  if [[ "$#" -ne 3 ]]; then
    printf 'HARNESS_ARITY_ERROR expected=3 actual=%d\n' "$#" >&2
    return 97
  fi

  local gate_id="$1"
  local outcome="$2"
  local detail="$3"

  if [[ -z "$gate_id" || -z "$outcome" || -z "$detail" ]]; then
    printf 'HARNESS_EMPTY_ARGUMENT\n' >&2
    return 98
  fi

  if [[ "$outcome" != 'PASS' && "$outcome" != 'FAIL' ]]; then
    printf 'HARNESS_BAD_OUTCOME value=%s\n' "$outcome" >&2
    return 99
  fi

  gate_total=$((gate_total+1))
  if [[ "$outcome" == 'PASS' ]]; then
    gate_passed=$((gate_passed+1))
  fi
  gate_records+=("$gate_id"$'\t'"$outcome"$'\t'"$detail")
  printf '%s %s %s\n' "$gate_id" "$outcome" "$detail"
}
```

Every official call must have exactly this form:

```bash
record_gate "$gate_id" "$outcome" "$detail"
```

The A02 two-argument call pattern is forbidden.

### Mandatory Recorder Self-Certification

Before `H01`, the evaluator must probe the recorder without writing any
project file:

| ID | Test | Exact expected result |
|---|---|---|
| `K01` | valid three-argument probe | return `0`; exact one-line record |
| `K02` | controlled two-argument probe | return `97`; exact arity diagnostic; no unbound-argument abort |
| `K03` | controlled empty-detail three-argument probe | return `98`; exact empty-argument diagnostic |
| `K04` | reset after probes | official totals and official record array all exactly `0` before `K01-K04` are officially recorded |

Nonzero probes must run in a controlled conditional context so `set -e` does
not terminate the shell before their exact return codes and diagnostics are
checked.

After probe observations are captured:

1. reset `gate_total`, `gate_passed`, and `gate_records`;
2. verify the reset;
3. record `K01-K04` with the certified three-argument interface; and
4. stop before `H01` if any `K` result is `FAIL`.

No probe result may be counted twice.

## Deterministic Counter Recovery Rule

A03 validation must not use:

- `rg -c`;
- `rg -ci`;
- a counter that emits no line for zero matches;
- an unset or empty value interpreted as zero; or
- `|| true` as a substitute for a numeric result.

Every count must be produced by an evaluator that always emits exactly one
nonnegative base-10 integer.

### Required New-Tool Counter

```text
rg --files Tools/DCC |
awk '/twin_hammer_head_contact_rotational_measurement_authority_lock_a03/ {
  n++
}
END {
  print n+0
}'
```

### Required Forbidden-Extension Counter

```text
rg --files RUN_ROOT |
awk '
/TWIN_HAMMER_HEAD_CONTACT_ROTATIONAL_MEASUREMENT_AUTHORITY_LOCK_A03/ &&
/\.(png|svg|blend|fbx|glb|uasset|umap|exr|jpg|jpeg|tga|obj)$/ {
  n++
}
END {
  print n+0
}'
```

The actual inline implementation may format the `awk` programs differently,
but matching semantics and `END { print n+0 }` normalization must be
identical.

Every returned value must pass both:

1. exactly one output line matching `^[0-9]+$`; and
2. exact integer comparison with the expected value.

### Mandatory Counter Self-Tests

Before any A03 lock file is created:

| ID | Test | Exact expected result |
|---|---|---:|
| `Q01` | new-tool counter over zero matching lines | `0` |
| `Q02` | new-tool counter over one synthetic matching line | `1` |
| `Q03` | forbidden-extension counter over zero matching lines | `0` |
| `Q04` | forbidden-extension counter over one synthetic matching `.png` line | `1` |

Each result must be a nonempty single-line base-10 integer.

## Exact Named Future Execution Preflight

Every pre-writer condition is named and recorded through the certified
three-argument recorder:

| ID | Required PASS condition |
|---|---|
| `F01` | Flamestrike approved this contract's exact SHA-256 for execution |
| `F02` | approved manifest result is exactly `PASS_MEASUREMENT_PROCESS_WITH_PARTIAL_AUTHORITY_RESOLUTION` |
| `F03` | prior measurement audit is exactly `PASS 261/261` |
| `F04` | approved measurement output decision is exactly `approved` |
| `F05` | all five canonical section digests match |
| `F06` | A01 remains exactly invalid and has no valid authority-lock effect |
| `F07` | A01 records are byte-identical and reference only |
| `F08` | A02 remains a pre-writer block and no A02 lock, validation, or review exists |
| `F09` | `STEP_STATE.json` reports no valid measurement authority lock |
| `F10` | production, builder, Blender, geometry, imagery, render, export, Step 13/14, and Unreal authorities remain false |
| `F11` | all five A03 future output paths are absent |
| `F12` | a manual recovery checkpoint was created immediately before the evaluator |

The future pre-writer phase must record exactly:

- `K01-K04`: `4`;
- `H01-H21`: `21`;
- `F01-F12`: `12`; and
- `Q01-Q04`: `4`.

Exact pre-writer result:

`41/41 PASS`

Skipped, duplicated, unreadable, missing, conflicting, malformed, or
unevaluated gates are failure.

If any pre-writer gate fails:

1. create no A03 lock, validation, or review;
2. create only the allowed A03 output record, handoff, minimal
   `STEP_STATE.json` update, recovery-journal entry, and checkpoint;
3. open the output record visibly;
4. do not adjust or retry A03 inside the same execution; and
5. stop for Flamestrike.

## Exact Allowed Future Outputs

After separate exact-hash approval of this contract, a future A03 execution
may create exactly one clean authority lock:

- `../manifests/TWIN_HAMMER_HEAD_CONTACT_ROTATIONAL_MEASUREMENT_AUTHORITY_LOCK_A03.json`

On a completed writer path, it may also create only:

- `../manifests/TWIN_HAMMER_HEAD_CONTACT_ROTATIONAL_MEASUREMENT_AUTHORITY_LOCK_A03_VALIDATION.json`
- `TWIN_HAMMER_HEAD_CONTACT_ROTATIONAL_MEASUREMENT_AUTHORITY_LOCK_A03_OUTPUT_RECORD.md`
- `../review/TWIN_HAMMER_HEAD_CONTACT_ROTATIONAL_MEASUREMENT_AUTHORITY_LOCK_A03_REVIEW.md`
- `../handoffs/TWIN_HAMMER_HEAD_CONTACT_ROTATIONAL_MEASUREMENT_AUTHORITY_LOCK_A03_HANDOFF.md`

Minimum `STEP_STATE.json`, recovery-journal, and checkpoint updates are
allowed only to record the observed A03 result and stop state.

No project tool may be created or modified.

## A03 Lock Writer Requirements

The A03 lock must be newly constructed from:

- this exact approved A03 contract;
- the approved measurement manifest;
- the approved measurement-decision records;
- the authoritative shared-depth boundary; and
- direct independent replay.

The writer must not read A01 or A02 lock-attempt fields as measurement input
values.

The A03 lock JSON must contain:

1. schema, date, run, and both asset IDs;
2. artifact status:
   `authoritative measurement-only partial authority; production remains blocked`;
3. this A03 contract's exact approved hash;
4. every `H01-H21` path and hash, with A01/A02 classified reference only;
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
16. A01/A02 exclusion and non-seeding declarations;
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

The independent A03 validation must execute exactly `91` checks:

| IDs | Count | Purpose |
|---|---:|---|
| `K01-K04` | `4` | recorder interface and reset certification |
| `H01-H21` | `21` | governing input hashes |
| `F01-F12` | `12` | named pre-writer conditions |
| `Q01-Q04` | `4` | deterministic counter self-tests |
| `J01-J02` | `2` | A03 JSON/schema/status |
| `C01-C03` | `3` | contract approval, manifest decision, exact five-section registry |
| `D01-D06` | `6` | five recomputed section digests plus registry equality |
| `S01` | `1` | source-role replay |
| `P01-P07` | `7` | projected contacts, C04 boundaries, bottom gap, non-3D boundary |
| `Z01-Z08` | `8` | intervals, station edges, exact fractions, formulas, continuity |
| `R01-R04` | `4` | C08 rows, scale, range, and no-resampling rules |
| `T01-T02` | `2` | transition-table exclusion |
| `B01-B04` | `4` | five stop conditions, head counts, head-Z conflict |
| `A01` | `1` | complete authority-boundary replay |
| `I01` | `1` | invalidation-rule replay |
| `E01-E10` | `10` | source result, prior audit, unchanged inputs, tools/outputs, observations |
| `N01` | `1` | stop and next-gate boundary |

Total:

`4+21+12+4+2+3+6+1+7+8+4+2+4+1+1+10+1 = 91`

The validator must:

- be an inline, read-only process;
- not import or execute the resolver;
- not import or execute the prior auditor;
- not import A01 or A02 content as measurement authority;
- not trust A03 writer-authored pass booleans;
- not create a project validation tool;
- retain the exact observed `K/H/F/Q` pre-writer records;
- independently evaluate all post-writer checks;
- record every check ID and status exactly once;
- report exactly `91/91 PASS` or fail;
- treat an empty or malformed counter as failure;
- treat a duplicate, extra, or missing check ID as failure; and
- stop after any failure without retrying A03 inside the same execution.

### Exact Post-Writer Check Meanings

- `J01`: A03 lock is valid JSON with the required schema, run, date, and
  assets.
- `J02`: declared artifact status and production block are exact.
- `C01`: exact-hash execution approval is recorded.
- `C02`: approved manifest whole-file path, hash, and decision are exact.
- `C03`: section registry contains exactly the five approved selectors and no
  others.
- `D01-D05`: recompute each approved section digest independently.
- `D06`: recomputed digest registry equals the A03 lock registry.
- `S01`: source-role rules replay exactly.
- `P01-P07`: replay all projected-contact, C04, bottom-gap, total-edge, and
  non-3D boundaries.
- `Z01-Z08`: replay intervals, edges, exact fractions, formulas, and both
  continuity points.
- `R01-R04`: replay all C08 constraints and prohibited transformations.
- `T01-T02`: prove the full transition table and equal-radius row remain
  excluded.
- `B01-B04`: replay five blocks, head sample/correspondence/triangle counts,
  and the unresolved head-Z conflict.
- `A01`: replay every required authority-boundary boolean.
- `I01`: replay the fail-closed invalidation rule.
- `E01`: approved source result remains exact.
- `E02`: prior audit remains `PASS 261/261`.
- `E03`: all `H01-H21` inputs remain byte-identical.
- `E04`: approved manifest and audit were not rewritten or regenerated.
- `E05`: A01 and A02 remain unchanged and non-authoritative.
- `E06`: resolver, prior auditor, A01 evaluator, and A02 evaluator were not
  rerun.
- `E07`: no A03 project authority-lock tool exists.
- `E08`: actual normalized A03 new-tool count is exactly `0`.
- `E09`: actual normalized A03 forbidden-extension count is exactly `0`.
- `E10`: execution observations show no Blender, geometry, imagery, render,
  export, Step 13/14, Unreal, or production action.
- `N01`: production remains blocked and the next gate is a separately
  approved block-resolution contract.

### Recovered `E08`

`E08` must:

1. run the normalized new-tool counter against actual `Tools/DCC`;
2. verify exactly one nonempty integer line;
3. verify the integer is exactly `0`; and
4. record the raw integer string.

### Recovered `E09`

`E09` must:

1. run the normalized forbidden-extension counter against the actual run
   root;
2. verify exactly one nonempty integer line;
3. verify the integer is exactly `0`; and
4. record the raw integer string.

Neither gate may use an A01 or A02 counter expression.

## Result Classification

### Pass

Only exact `91/91 PASS` may make the A03 lock effective as:

`authoritative measurement-only partial authority; production remains blocked`

### Pre-Writer Block

If any `K`, `H`, `F`, or `Q` gate fails:

- create no A03 lock, validation, or review;
- preserve exact evidence;
- create only the allowed output, handoff, state, journal, and checkpoint
  records;
- open the output record visibly; and
- stop.

### Post-Writer Validation Failure

If the A03 lock is written but any validation check fails:

- classify A03 `invalid`;
- preserve it and the validation as failure evidence;
- do not repair forward;
- do not rerun A03;
- do not promote measurement authority;
- create the allowed output, review, handoff, state, journal, and checkpoint
  records;
- open the review visibly; and
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

- editing, deleting, replacing, renaming, or promoting A01 or A02;
- using A01 or A02 lock-attempt content as A03 measurement input;
- rerunning A01 or A02 validation/evaluation;
- rerunning the measurement resolver or prior auditor;
- modifying the approved measurement manifest or audit;
- using `rg -c` or `rg -ci` for any A03 validation count;
- interpreting an empty count as zero;
- using a recorder that dereferences missing positional arguments;
- defining or calling a separate `record_preflight` helper;
- retrying a failed A03 evaluator inside the same execution;
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

This A03 Core recovery contract is the current review artifact.

It must be opened automatically in a visible desktop text-editor window.
A terminal path or clickable link alone does not satisfy review visibility.

After visible review, stop for:

`approve / revise / reject / blocked`

Approval must identify this contract by exact SHA-256. No A03 action follows
from the present drafting approval.

## Future Checkpoint And Repository Rule

A later approved A03 execution must:

1. checkpoint before any evaluator or writer action;
2. certify the recorder through `K01-K04`;
3. pass exact pre-writer result `41/41`;
4. checkpoint after pass, block, validation failure, or drift;
5. stage only the exact dependency-complete approved scope;
6. commit and push only valid scoped tracked records to `assetforge/main`;
7. preserve every unrelated dirty worktree entry; and
8. stop after the appropriate A03 output or review record is visibly open.

This candidate recovery contract does not authorize future execution.

## Exact Next Gate

No valid measurement authority lock or production action is active.

The next possible action is separate Flamestrike approval of this contract's
exact SHA-256 for A03 execution.

Even after a valid A03 lock, production remains blocked until the missing
head, C04, rotational-transition, terminal-cap, and head-Z authorities are
resolved through separate approved contracts.
