# A005 Source-Versus-Measurement Dual-Option Feasibility Contract A02

Status: `candidate contract; preparation approved; execution not approved`

Artifact classification: `candidate`

Contract ID: `A005-CR-SMR-A02`

Date: 2026-07-17

## Plain-English Purpose

The approved A01 reconciliation test proved that shrinking all of C-004 while
allowing C-003 only one rigid movement cannot preserve all 16 approved
C-003/C-004 contacts.

This contract proposes two separate local tests before Flamestrike chooses a
new adjustment rule:

- Option A tests whether scaling C-003 with the C-004 inner contact can preserve
  CL-003 without breaking the adjacent C-002/C-003 contact at CL-002.
- Option B tests whether the C-004 inner CL-003 contact can remain fixed while
  only source-visible outer C-004 apron boundaries move toward the approved
  physical targets.

The tests must use the same evidence, targets, reports, and decision gates.
They may not be combined into a hybrid. This contract does not execute either
test, create an adjusted silhouette, revise Step 10, or create geometry.

## Preparation Authority

On 2026-07-17, Flamestrike approved the exact next gate:

> prepare and visibly present a dual-option local feasibility-test contract
> only; do not execute either test yet.

That approval authorizes only this candidate contract and its visible
presentation. Execution requires a separate explicit approval of this exact
contract.

## Step ID And Name

- Step ID: `A005-CR-SMR-A02`.
- Name: `Source-Versus-Measurement Dual-Option Feasibility A02`.
- Pipeline role: bounded Core-recovery interpretation-feasibility gate before
  any Step 10 revision.

## One Decision

Determine which, if either, of these independent adjustment rules is feasible
without changing the source drawings, changing the six physical targets,
breaking authoritative visible contacts, inventing hidden surfaces, or
claiming unproved world/cross-view authority:

1. `OPTION_A_C003_SCALE_WITH_C004_INNER_CONTACT`;
2. `OPTION_B_C004_OUTER_ONLY_CONTACT_LOCKED_ADJUSTMENT`.

Allowed result classifications are:

- `option_A_feasible_option_B_blocked`;
- `option_B_feasible_option_A_blocked`;
- `both_options_feasible_pending_Flamestrike_visual_selection`;
- `both_options_blocked`.

The execution may recommend an option from the evidence, but no technical
score or agent recommendation selects production authority. Flamestrike must
approve, reject, or leave blocked any future adjustment rule separately.

## Governing Core Principle

- First Principles: test the exact unresolved contact rule rather than repair
  forward from a blocked proposal.
- Evidence-Bound Decision: preserve source pixels, physical-target intent,
  component IDs, and authoritative contact samples as controlling inputs.
- Kaizen: compare the two smallest sufficient recovery alternatives with one
  shared audit instead of creating production artifacts.
- Stop-the-line: stop an option at its first failed hard gate and do not hide
  the failure with a hybrid, tolerance, warp, or visual approximation.
- Whole-System Value: prefer the feasible rule with the least source
  deviation, fewest affected components, and narrowest downstream impact,
  subject to Flamestrike's visual decision.

## Exact Authorizing Plan Section

This proposed gate is authorized in structure by:

- `docs/projects/assetforge/BLOODAXE_CAIRNSTONE_PIXEL_EXACT_FRESH_START_MULTISTEP_PLAN.md`:
  - Section 4, Evidence And Interpretation Boundary;
  - Section 8, Standard Step Contract;
  - Step 10, Unknowns And Interpretation Decision Gate;
  - Section 14, Efficiency Controls;
- `AGENTS.md`, especially Core, closed-world authorization, evidence versus
  interpretation control, and recovery rules;
- Flamestrike's 2026-07-17 contract-preparation approval quoted above.

This is a recovery feasibility gate, not Step 10 execution. It may only inform
a later separately approved Step 10 revision contract.

## Approved Inputs

Execution may read only the following A005 asset-specific authority and the
general process authorities named above:

- the authoritative A02 source, Step 03 lossless panels, and their approved
  hashes;
- the approved Step 04R component/ownership inventory and recovered top
  contact evidence;
- the approved bounded Step 06R/06Q and Step 07R contact/measurement authority;
- the approved Step 08R top contact/calibration records within their exact
  bounds;
- the approved Step 09 semantic cross-view groups and explicit blocked
  physical-correspondence findings;
- `manifests/SCALE_AUTHORITY_RECOVERY_A01_PHYSICAL_BOUNDS.json`, authoritative
  for physical-target intent only;
- `manifests/SOURCE_VS_MEASUREMENT_RECONCILIATION_A01_RULES.json`, `reference
  only` for the tested A01 factors and rules;
- `manifests/SOURCE_VS_MEASUREMENT_RECONCILIATION_A01_ADJUSTMENT_LEDGER.json`,
  `proof only` for the ten factor calculations and 16 CL-003 residuals;
- `manifests/SOURCE_VS_MEASUREMENT_RECONCILIATION_A01_VALIDATION.json`, `proof
  only`;
- `steps/SOURCE_VS_MEASUREMENT_RECONCILIATION_A01_OUTPUT_RECORD.md` and
  `handoffs/SOURCE_VS_MEASUREMENT_RECONCILIATION_A01_TO_STEP10_REVISION_HANDOFF.md`,
  authoritative for the approved blocked decision and routing only;
- `SM_GIA_BloodAxeCairnstone_A005_RESET_RESUME_STATE.md`, the artifact index,
  and approval log.

No A001-A004 artifact, remembered shape, legacy mesh, generated output, or
external reference may enter the test.

## Authority Preserved Unchanged

The execution must preserve:

- every original source pixel and source hash;
- all existing Step 01-Step 10 records;
- the six final physical design targets:
  - complete asset Z: `220 cm`;
  - C-001 X: `120 cm`;
  - C-001 Y: `90 cm`;
  - C-004 X: `140 cm`;
  - C-004 Y: `110 cm`;
  - C-004 Z: `35 cm`;
- all currently authoritative CL-001, CL-002, and CL-003 discrete source
  observations within their approved record boundaries;
- front as primary X/Z source-shape owner;
- left as primary Y/Z source-shape owner;
- back and right as validation views with non-conflicting visible-detail
  ownership only;
- top as visible plan/contact evidence, not world-frame or geometry authority;
- the absence of a recovered world construction frame, physical cross-view
  pixel pairs, closed perimeter, center, origin, pivot, snap anchor, hidden
  fill, topology, and geometry.

## Shared Test Frame

Both options must run from the same immutable input lock and use the same
source-coordinate target-frame evidence.

- The ten A01 whole-C-004 factors may be replayed exactly as per-view
  feasibility targets; they may not be promoted to a unified world transform.
- Front and left own the primary upright comparisons.
- Back and right remain validation-only comparisons; disagreement with them
  must be reported and may not be averaged away.
- Top owns the exact 16-sample CL-003 plan-contact feasibility audit and the
  approved plan-target comparison within its recorded limits.
- Step 09 semantic correspondence groups may be used only as semantic groups.
  The test may not invent physical cross-view pixel pairs.
- Raw pixel movement may be compared only within the same panel. Cross-panel
  comparison must additionally report a normalized percentage of the
  controlling source span; raw pixels from different panels may not be treated
  as commensurate physical distances.
- Any mathematical affine reference point used for a diagnostic must be
  logged and labelled `diagnostic only`; it is not a physical center, pivot,
  anchor, or geometry transform.

## Option A - C-003 Scale With C-004 Inner Contact

Option ID: `OPTION_A_C003_SCALE_WITH_C004_INNER_CONTACT`.

Purpose: test whether the A01 C-004 target adjustment can preserve CL-003 when
C-003 is permitted the minimum matching axis-aligned scale and translation,
without breaking CL-002 or altering another component.

Allowed operations:

1. Replay the existing A01 C-004 per-view target factors without changing
   their values or authority.
2. Apply only to a separate interpretation coordinate set, never to source
   pixels.
3. Permit C-003 one axis-aligned affine feasibility map per applicable source
   view: scale in only the axes required by that view plus one translation.
4. Solve and log the C-003 diagnostic map from the approved source coordinates
   and contact constraints. Do not choose a physical center or anchor.
5. Re-audit every authoritative CL-003 sample used in that view.
6. Re-audit every currently authoritative CL-002 sample and every affected
   source-visible C-003 boundary/landmark in that view.
7. Report the effect on CL-001 as unchanged; if the calculation requires C-002
   or C-001 to move, scale, or deform, Option A fails.

Option A hard-pass conditions:

- every tested CL-003 sample remains exactly coincident in the analytic
  coordinate result;
- every tested CL-002 sample remains exactly coincident;
- C-001 and C-002 remain unchanged;
- no rotation, shear, local deformation, hidden closure, or unlogged transform
  is used;
- all target-frame errors and source-visible deviations are fully reported;
- no validation-view disagreement is silently selected, averaged, or erased.

Option A fails if any hard-pass condition is false. A near match is not a pass,
and no tolerance may be invented to rescue it.

## Option B - C-004 Outer-Only Contact-Locked Adjustment

Option ID: `OPTION_B_C004_OUTER_ONLY_CONTACT_LOCKED_ADJUSTMENT`.

Purpose: test whether the approved C-004 target extents can be approached while
the source-visible inner C-004 boundary at CL-003 remains fixed and only
source-visible outer apron evidence is adjusted.

Allowed operations:

1. Lock every authoritative CL-003 sample used by the test to its original
   source coordinate.
2. Keep C-001, C-002, and C-003 unchanged.
3. Identify each outer C-004 segment or extremum used by the test by exact
   source record, view, component ownership, and original coordinate/span.
4. Move only source-visible outer C-004 points or boundary segments required
   by the six target-frame comparisons.
5. Record every original and candidate coordinate, axis displacement, source
   span, normalized displacement percentage, reason, and target consumer.
6. Use only a deterministic, declared line/point constraint calculation.
   Candidate evidence may show source and proposed boundary lines, but may not
   resample the source raster, fill a footprint, close an occluded sector, or
   invent a hidden surface.
7. If a continuous outer-to-inner transition cannot be represented from
   source-visible owned evidence without closing an unknown, retain the
   partial line/point diagnostic as `proof only` and fail Option B.

Option B hard-pass conditions:

- every tested CL-003 coordinate has exactly zero displacement;
- C-001, C-002, C-003, CL-001, and CL-002 remain unchanged;
- only source-visible owned C-004 outer evidence moves;
- the primary-view target-frame errors reach zero for the six controlling
  physical-target roles, or the option fails and reports each nonzero error;
- no hidden contour, filled footprint, source raster warp, freeform cleanup,
  smoothing, symmetry correction, or unlogged movement is used;
- every transition shown is traceable to source-visible owned evidence;
- validation-view conflicts remain disclosed rather than averaged away.

Option B fails if any hard-pass condition is false. A visually plausible but
untraceable transition is not a pass.

## No-Hybrid Rule

- Option A may not use any Option B local outer-only adjustment.
- Option B may not scale, translate, or deform C-003.
- A failed option may not borrow operations from the other option.
- A hybrid may be proposed only through a later separately reviewed contract
  after both independent results are visible.

## Pre-Registered Comparison Gates

Each option must receive an independent `pass`, `fail`, or `blocked` result for
every gate below:

1. input and source-hash integrity;
2. six physical targets unchanged;
3. primary-view target-frame error by component and axis;
4. CL-003 preservation;
5. CL-002 preservation;
6. CL-001 and unaffected-component preservation;
7. maximum, median, and RMS source-coordinate displacement per panel;
8. normalized displacement as a percentage of the controlling source span;
9. count of affected components, contacts, source-visible points, and boundary
   segments;
10. front/left source-owner compliance;
11. back/right validation disagreement disclosure;
12. top evidence-role compliance;
13. source-versus-interpretation visibility and classification;
14. hidden/occluded-sector non-invention;
15. forbidden-operation audit;
16. write-scope and downstream stop-state audit.

No weights, pass tolerance, ranking threshold, or preferred result may be
added after execution begins.

## Comparison And Recommendation Rule

An option that fails any hard-pass condition is not eligible for selection.

If both options pass, the technical report may recommend the option with, in
this order:

1. fewer affected components and authoritative contact sets;
2. lower maximum normalized source deviation;
3. lower median normalized source deviation;
4. fewer moved source-visible points/segments;
5. narrower downstream interpretation impact;
6. no worse validation-view disagreement.

The order is pre-registered only to prevent post-result goal changes. It does
not replace Flamestrike's visual judgment. A recommendation remains
`reference only` until Flamestrike approves a later rule.

## Evidence And Interpretation Separation

The review artifact must keep each option in a separate column or page and
must show unmistakably labelled regions:

- `ORIGINAL SOURCE EVIDENCE - UNCHANGED`;
- `OPTION A INTERPRETATION DIAGNOSTIC - NOT SOURCE OR GEOMETRY`;
- `OPTION B INTERPRETATION DIAGNOSTIC - NOT SOURCE OR GEOMETRY`;
- `CONTACT AND TARGET ERROR AUDIT`;
- `BLOCKED / UNKNOWN`;
- `A/B COMPARISON - NO OPTION APPROVED`.

Candidate lines must be unfilled and visibly distinct from exact source marks.
No option may be presented as approved geometry, corrected source, a closed
footprint, or a 3D solution.

## Allowed Execution Outputs

If execution is separately approved, it may create only:

- `manifests/SOURCE_VS_MEASUREMENT_DUAL_OPTION_A02_INPUT_LOCK.json`;
- `manifests/SOURCE_VS_MEASUREMENT_DUAL_OPTION_A02_OPTION_REGISTRY.json`;
- `manifests/SOURCE_VS_MEASUREMENT_DUAL_OPTION_A02_OPTION_A_C003_SCALE_AUDIT.json`;
- `manifests/SOURCE_VS_MEASUREMENT_DUAL_OPTION_A02_OPTION_B_C004_OUTER_AUDIT.json`;
- `manifests/SOURCE_VS_MEASUREMENT_DUAL_OPTION_A02_COMPARISON.json`;
- `manifests/SOURCE_VS_MEASUREMENT_DUAL_OPTION_A02_VALIDATION.json`;
- `evidence/SOURCE_VS_MEASUREMENT_DUAL_OPTION_A02/SM_GIA_BloodAxeCairnstone_A005_SOURCE_VS_MEASUREMENT_DUAL_OPTION_A02_REVIEW_BOARD.png`;
- `steps/SOURCE_VS_MEASUREMENT_DUAL_OPTION_A02_OUTPUT_RECORD.md`;
- `handoffs/SOURCE_VS_MEASUREMENT_DUAL_OPTION_A02_TO_RULE_DECISION_HANDOFF.md`.

A local-only working directory may be used at:

`Saved/AssetForgeResearch/A005_SourceVsMeasurementDualOption_A02/`.

No other tracked path may be created or changed during execution. After a
visible output decision, the reset/resume state, artifact index, and approval
log may be updated only through a separately stated closeout scope.

## Blocked Files And Actions

- modifying or replacing original A02 source or Step 03 panels;
- modifying any existing Step 01-Step 10 record or prior recovery artifact;
- changing or averaging the six physical targets;
- accessing any A001-A004 asset-specific artifact;
- treating per-view factors as one unified world transform;
- inventing physical cross-view pixel correspondence;
- creating filled footprints, closed perimeters, centers, pivots, anchors,
  hidden contacts, hidden surfaces, topology, or 3D form;
- resampling, repainting, or warping source rasters;
- combining Options A and B;
- creating geometry, DCC, FBX, UV, texture, material, LOD, collision, Unreal,
  or performance artifacts;
- revising or approving Step 10;
- beginning Step 11;
- editing generic Core, pipeline, blueprint, or plan records;
- commit or push.

## Expected Execution Outputs

The bounded execution must produce:

- one immutable input lock;
- one option registry that restates every rule before calculations begin;
- one complete independent audit per option;
- one comparison record using only the pre-registered gates;
- one focused validation manifest;
- one visibly reviewable A/B board;
- one output record with exact pass/fail/blocked results;
- one handoff that keeps later work stopped pending Flamestrike's option
  decision.

## Validators

Validation must prove:

- every input used was allowlisted and hash-locked before output writes;
- all source and existing authority hashes remain unchanged;
- the six targets are unchanged and appear exactly once in the option registry;
- both options use the same input lock and comparison gates;
- all authoritative contact samples used are identified by source record and
  exact coordinate;
- Option A re-audits CL-003 and CL-002 after its C-003 map;
- Option B holds CL-003 at zero displacement and leaves C-001/C-002/C-003
  unchanged;
- no hybrid operation exists;
- all per-view raw and normalized deviations replay independently;
- no cross-panel raw-pixel value is treated as a physical distance;
- front/left ownership and back/right validation roles remain intact;
- no world frame, physical cross-view pairing, filled unknown, geometry, or
  source modification was created;
- the review board clearly separates evidence and interpretation;
- only allowlisted paths changed;
- Step 10, Step 11, geometry, production, commit, and push remain stopped.

## Visible Review Requirement

After technical validation, the A/B board and plain-English output record must
open automatically in visible desktop windows. The board must show both
options at matched orientation, framing, and scale wherever the source records
permit direct within-panel comparison.

No result classification or downstream recommendation may be presented for
approval until the visible-artifact requirement is verified.

## Artifact Status On Technical Pass

- This contract after separate execution approval: `authoritative for
  completed execution scope only`.
- Input lock, option audits, calculations, validation, and review board: `proof
  only`.
- Candidate option lines: `candidate interpretation; not source or geometry`.
- Comparison recommendation: `reference only`.
- Output record and handoff before Flamestrike's result decision: `candidate`.
- Original A005 source, targets, and prior authority: unchanged.
- No option becomes an approved rule from technical pass alone.

## Artifact Status On Failure Or Block

- valid diagnostics: `proof only`;
- incomplete or untraceable candidate option: `quarantined`;
- forbidden or contaminated output: `invalid` and quarantined;
- failed option rule: `rejected candidate` after Flamestrike accepts the
  result;
- A005 production status: remains blocked.

## Stop Conditions

Stop the affected option immediately if:

- required source ownership or a contact sample cannot be traced to approved
  authority;
- an input hash differs unexpectedly;
- Option A requires C-001 or C-002 movement, C-003 local deformation, rotation,
  shear, or a broken CL-002/CL-003 sample;
- Option B requires C-003 movement, a hidden contour, a filled footprint, a
  source raster warp, or an untraceable outer-to-inner transition;
- a physical cross-view pixel pair or world transform would have to be
  invented;
- an option cannot meet the hard target/contact gates under its declared
  operations;
- source and interpretation cannot be shown separately;
- execution would write outside the allowlist or begin Step 10/production.

One option may continue after the other stops only if its work is independent,
uses no failed-option output, and remains inside this exact contract. If the
shared input lock or common authority fails, stop both options.

Do not repair forward. Record the exact blocker and preserve only valid bounded
evidence.

## Smallest Sufficient Change

Run two independent local 2D feasibility calculations from one locked input
set, produce one matched A/B review board, and stop for Flamestrike's rule
decision. Create no corrected source, construction blueprint, or geometry.

## Estimated Context Demand

- Contract execution: medium.
- Blender, Unreal, TRELLIS, image generation, and external research: none.
- Specialist agents: none unless Flamestrike separately approves disjoint
  lanes; the shared evidence and comparison gate favor one controlled lane.

## Planned Checkpoints

1. before opening any execution output path;
2. after the immutable input lock and option registry;
3. after both independent option audits;
4. after comparison and validation, before visible review;
5. after Flamestrike's result decision, before any separately approved
   closeout.

## Execution Approval Question

Do you approve executing `A005-CR-SMR-A02` exactly as written to:

- test C-003 scaling and C-004 outer-only adjustment independently;
- preserve the original drawings, six physical targets, and authoritative
  contacts;
- apply the same pre-registered pass/fail gates to both options;
- create only local `proof only` calculations and clearly separated candidate
  interpretation lines;
- open the matched A/B result visibly;
- stop for your option decision before Step 10, geometry, commit, or push?

Approval of this contract would authorize the bounded A/B feasibility test
only. It would not approve either adjustment rule or any downstream artifact
in advance.
