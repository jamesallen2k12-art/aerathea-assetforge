# A005 S10R-006-R7-A Cross-View Corner-Ownership Rule A01 Contract

Status: candidate contract prepared for visible Flamestrike review; execution not authorized

Artifact classification: `candidate`

Contract ID: `A005-CR-S10R-006-R7-A-CVCOR-A01`

Rule ID: `S10R-006-R7-A-CVCOR-A01`

Date: 2026-07-20

## Preparation Authority

Flamestrike selected `S10R-006-R6-A`, authorizing preparation only of one
separate bounded cross-view corner-ownership rule contract. The authoritative
R6 output, option registry, approval log, reset/resume record, artifact index,
and post-decision handoff all identify this contract preparation as the exact
next task.

This authorizes:

- the bounded Core reassessment recorded in this contract;
- preparation and validation of this one candidate contract;
- exact A005 status updates for the prepared-contract state;
- visible presentation of the on-disk contract;
- checkpointing; and
- stopping when exact contract-execution approval becomes the next task.

It does not authorize contract execution, rule registration, rule approval,
gap allocation, a per-point owner, q evaluation, sampling, a seam, a join,
closure, interpolation, a field, a fill, a surface, topology, geometry,
Step 10 closeout, Step 11, DCC, Unreal, production, staging, commit, or push.

## Controlling First Principles

- Actual project goal: advance A005 toward a coherent 360-degree production
  asset without converting bounded interpretation into source evidence.
- Exact Blueprint authority: Step 10 permits written interpretation options,
  explicit rule proposals, and approval, rejection, or blocked decisions. It
  prohibits implementation, geometry creation, interpretation presented as
  measurement, and silent rule selection.
- Exact R6 authority: prepare one bounded cross-view corner-ownership rule
  contract that addresses all four exact R5 gaps, labels every proposal as
  interpretation, preserves a mandatory BLOCK fallback, and stops before any
  rule instance, seam, join, closure, field, or geometry is created.
- Proven evidence: Step 05 cardinal axis mappings; the approved R5 q
  orientation; four pairwise-disjoint owned lane intervals; four exact open,
  nonempty, unowned corner gaps; twelve front/left construction records; and
  fourteen proof-only back/right holdouts.
- Historical limit: I10-010-A is a revision-required candidate, not current
  authority. Its whole-surface dominant-normal and joint-tie wording cannot be
  copied forward as an approved rule.
- Interpretation proposed here: a gap-local bisector rule, expressed only in
  the existing abstract q ledger, with a single-owner half-open tie policy.
- Decision required after later execution: whether this exact candidate rule
  is deterministic, total over the four open gaps, bounded to abstract upright
  owner labels, and safely non-implementing—not whether it is recovered
  physical correspondence, a seam plan, a closed field, or geometry.

## Evidence And Interpretation Boundary

### Evidence

- Step 05 fixes the cardinal owner directions as +X, +Y, -X, and -Y for the
  four approved front/left construction lanes.
- R5 fixes increasing q as counterclockwise in the +X,+Y plane when viewed
  from +Z, with q = 0 centered on +X.
- R5 fixes four owned closed intervals and four intervening open gaps.
- R5 fixes q as dimensionless, non-periodic, unwrapped, and unevaluated.
- R5 fixes back/right records as proof only and excludes them from
  construction ownership.
- R6 selected preparation of this rule contract only; it approved no corner
  rule and resolved no block.

### Candidate Interpretation

- each exact R5 gap has one predecessor lane and one counterclockwise
  successor lane;
- the exact rational midpoint of a gap is a rule threshold, not a measured or
  physical angle;
- the predecessor label owns the lower open half of a gap;
- the successor label owns the midpoint and upper open half; and
- the successor-at-tie choice is an explicit production interpretation used
  to avoid joint ownership, not a source-authored preference.

The candidate rule does not recover a source point, source normal, target
coordinate, physical azimuth, physical pair, center, pivot, anchor, seam, or
surface.

## Last Known Core-Valid State

- R6 selected option: `S10R-006-R6-A`.
- R6 authority: preparation only of this separate bounded rule contract.
- R5 rule status:
  `approved_bounded_symbolic_rule_four_blocked_corner_gaps_unowned`.
- R5 artifact classification: authoritative for bounded S10R-006-R5-A
  symbolic coupling rule only.
- Owned lane intervals: 4, pairwise disjoint.
- Blocked corner gaps: 4, open, nonempty, and unowned.
- Abstract parameter: q, dimensionless, non-periodic, and unevaluated.
- Construction lanes and records: 4 and 12.
- Proof-only back/right holdouts: 14.
- Gap assignments, per-point owners, evaluated q instances, samples,
  coordinates, seams, joins, closures, fields, fills, surfaces, topology, and
  geometry: 0.
- `S10R-BLOCK-006`:
  `active_pending_separate_cross_view_corner_ownership_rule_contract`.
- `S10R-BLOCK-008` and `S10R-BLOCK-009`: active unchanged.
- Resolved block IDs: none.
- Every evaluation, implementation, downstream, and Git authorization flag:
  false.

## Exact Preserved Lane And Gap Ledger

| Lane ID | Cardinal label | Existing owned q interval | Status |
|---|---|---|---|
| AFM-FRONT-RIGHT | +X | `[-1/2,1/2]` | approved R5 bounded interpretation |
| AFM-LEFT-LEFT | +Y | `[3/2,5/2]` | approved R5 bounded interpretation |
| AFM-FRONT-LEFT | -X | `[7/2,9/2]` | approved R5 bounded interpretation |
| AFM-LEFT-RIGHT | -Y | `[11/2,13/2]` | approved R5 bounded interpretation |

| Gap ID | Exact open interval | Predecessor label | Successor label |
|---|---|---|---|
| G_0 | `(1/2,3/2)` | AFM-FRONT-RIGHT / +X | AFM-LEFT-LEFT / +Y |
| G_1 | `(5/2,7/2)` | AFM-LEFT-LEFT / +Y | AFM-FRONT-LEFT / -X |
| G_2 | `(9/2,11/2)` | AFM-FRONT-LEFT / -X | AFM-LEFT-RIGHT / -Y |
| G_3 | `(13/2,15/2)` | AFM-LEFT-RIGHT / -Y | AFM-FRONT-RIGHT / +X label-only successor |

The G_3 successor entry is an adjacency label only. It does not create a new
lane, duplicate a construction record, set q modulo 8, identify q = 15/2
with q = -1/2, or authorize periodic closure.

## Proposed Bounded Gap-Ownership Rule

For each gap G_k = (a_k,b_k), define the exact symbolic threshold:

    m_k = (a_k + b_k) / 2

Let P_k be the predecessor owner label and S_k the counterclockwise successor
owner label from the exact ledger above. Propose the unevaluated rule:

    O_k(q) = P_k  when a_k < q < m_k
    O_k(q) = S_k  when m_k <= q < b_k

This is a half-open successor-at-tie convention. It proposes exactly one
abstract owner label for every q in each existing open gap while keeping the
existing R5 lane endpoints under their already approved lane owners.

The rule is total only over G_0 through G_3. It does not own:

- any top/upright transition;
- any bottom or hidden surface;
- any source pixel or source-space sector;
- any target-space coordinate or physical surface point;
- any back/right construction record; or
- any Step 10 unknown outside these four exact upright corner gaps.

The midpoint expression and branch relations are candidate rule definitions,
not instantiated q samples or per-record values. Later execution may register
the strings and exact rational relations only; it may not enumerate, sample,
plot, rasterize, fill, or mesh the rule.

## Revision Of Historical I10-010-A

This candidate does not copy historical I10-010-A. It revises that candidate
in four bounded ways:

1. Scope is limited to the four exact R5 q gaps, not all visible surfaces.
2. Ownership uses the approved R5 symbolic ledger, not an intended physical
   outward normal.
3. Exact ties receive one explicit successor label; no joint ownership or
   implicit interpolation is introduced.
4. Top/upright ownership, source-to-target placement, seams, topology, and
   implementation remain separate blocked decisions.

Historical I10-010-A remains candidate history classified
`requires_revision`. This contract neither reclassifies nor modifies it.

## Decision-Threshold, Seam, Join, And Closure Policy

- m_k is an abstract rule threshold only, not a geometry seam.
- An owner-label change does not define vertex placement, edge placement,
  continuity, blending, interpolation, material ownership, or topology.
- No equality or continuity is asserted between adjacent lane boundary
  formulas at a threshold.
- No cross-lane seam is selected.
- No cross-view physical seam is selected.
- No endpoint join is selected.
- No top/upright join is selected.
- No side-to-side or front/left geometry join is selected.
- No periodic wrap or final/first endpoint identification is selected.
- No closed 360-degree field or surface is selected.
- No back/right holdout enters construction.

## Fail-Closed Falsification Matrix

| ID | Required check | Pass condition | Fail result |
|---|---|---|---|
| F01 | Input integrity | all locked hashes match | blocked_integrity_or_scope_failure |
| F02 | R6 authority | R6-A is selected and grants preparation only of this contract | blocked_authority_mismatch |
| F03 | R5 state | four exact owned intervals and four exact open gaps replay unchanged | blocked_r5_state_conflict |
| F04 | Axis replay | Step 05 yields the exact +X,+Y,-X,-Y adjacency order | blocked_axis_mapping_conflict |
| F05 | Gap adjacency | every gap has exactly one predecessor and one successor from approved construction lanes | blocked_gap_adjacency_conflict |
| F06 | Midpoint exactness | every m_k is the exact rational midpoint of its locked gap endpoints | blocked_threshold_definition_conflict |
| F07 | Lower branch | a_k < q < m_k maps only to P_k symbolically | blocked_rule_branch_conflict |
| F08 | Upper branch | m_k <= q < b_k maps only to S_k symbolically | blocked_rule_branch_conflict |
| F09 | Totality | the two branches cover each open G_k with no unowned q relation | blocked_incomplete_gap_rule |
| F10 | Single ownership | the two branches are disjoint and no q relation receives two labels | blocked_joint_ownership |
| F11 | Endpoint preservation | a_k and b_k remain owned only through existing R5 lane intervals | blocked_endpoint_authority_mutation |
| F12 | G_3 no-wrap | +X successor is label-only; no modulo, wrap, or endpoint identification exists | blocked_closure_implication |
| F13 | Historical boundary | I10-010-A remains revision-required candidate history | blocked_historical_authority_expansion |
| F14 | Holdout policy | all fourteen back/right records remain proof only | blocked_holdout_authority_expansion |
| F15 | Interpretation labeling | every new threshold and branch claim is labeled candidate interpretation | blocked_evidence_interpretation_conflation |
| F16 | Top/upright stop | no top/upright owner or join is defined | blocked_scope_expansion |
| F17 | No seam or interpolation | no seam, continuity, blend, or interpolation behavior is defined | blocked_scope_expansion |
| F18 | Zero instances | q instances, samples, coordinates, owner instances, fields, fills, surfaces, topology, and geometry remain 0 | blocked_output_or_authority_expansion |
| F19 | Block fallback | any failed gate registers no candidate rule | blocked_rule_registration |
| F20 | Write scope | changed paths match the execution allowlist and none is staged | blocked_integrity_or_scope_failure |
| F21 | Authority stops | rule approval, evaluation, implementation, downstream, and Git flags remain false | blocked_authority_expansion |
| F22 | Visibility stop | output and handoff are visibly verified before stop | blocked_review_visibility_failure |

No tolerance, approximate equality, visual judgment, numeric sampling,
physical-normal inference, or repair-forward path is permitted.

## Mandatory BLOCK Fallback

If any validation or falsification gate fails:

- result:
  `blocked_cross_view_corner_ownership_rule_dependency_or_definition_failure`;
- register no candidate corner-ownership rule;
- preserve all four gaps as unowned;
- set `S10R-BLOCK-006` to
  `active_approved_lane_boundary_coupling_rule_four_corner_gaps_unowned_no_field`;
- preserve `S10R-BLOCK-008` and `S10R-BLOCK-009` active unchanged;
- resolve no block;
- quarantine any affected partial output if it cannot be removed from the
  decision path cleanly;
- record the exact failed gate; and
- stop without redesigning the rule in the same task.

## One Result Required From Later Execution

After separate exact execution approval, execution must produce exactly one:

1. `pass_candidate_bounded_cross_view_corner_ownership_rule_registered_no_implementation`
   if every gate passes;
2. `blocked_cross_view_corner_ownership_rule_dependency_or_definition_failure`
   if any authority, adjacency, threshold, totality, single-owner, no-wrap,
   holdout, or scope gate fails; or
3. `blocked_integrity_or_scope_failure` on any hash mismatch, unexpected
   write, output instantiation, authority expansion, staging, or downstream
   action.

A pass would register a candidate rule for a later Flamestrike decision. It
would not approve the rule, resolve a block, authorize q evaluation, define a
seam or join, close a field, or authorize implementation.

## Allowed Actions After Separate Execution Approval

- take a pre-execution checkpoint;
- verify every locked input and this contract hash before output writes;
- copy the exact R5 lane and gap ledger without modification;
- copy the exact R6 preparation-only authority without expansion;
- register m_k and O_k as unevaluated symbolic strings and exact rational
  relations only;
- replay the Step 05 cardinal adjacency order symbolically;
- audit totality, single ownership, endpoint preservation, no-wrap behavior,
  historical I10-010 limits, and all unchanged stops without sampling;
- preserve all fourteen back/right records as proof only;
- run the fail-closed falsification matrix;
- create record-only input, rule, falsification, validation, output, and
  decision-handoff records;
- create one read-only independent auditor;
- update the three A005 status records only with the exact candidate result;
- open the output and handoff visibly;
- take a completion checkpoint; and
- stop for Flamestrike's rule-result decision.

## Allowed Output Paths After Separate Execution Approval

- `manifests/S10R_006_R7_A_CROSS_VIEW_CORNER_OWNERSHIP_RULE_A01_INPUT_LOCK.json`;
- `manifests/S10R_006_R7_A_CROSS_VIEW_CORNER_OWNERSHIP_RULE_A01_RULE_REGISTRY.json`;
- `manifests/S10R_006_R7_A_CROSS_VIEW_CORNER_OWNERSHIP_RULE_A01_FALSIFICATION_AUDIT.json`;
- `manifests/S10R_006_R7_A_CROSS_VIEW_CORNER_OWNERSHIP_RULE_A01_VALIDATION.json`;
- `steps/S10R_006_R7_A_CROSS_VIEW_CORNER_OWNERSHIP_RULE_A01_OUTPUT_RECORD.md`;
- `handoffs/S10R_006_R7_A_CROSS_VIEW_CORNER_OWNERSHIP_RULE_A01_TO_DECISION_HANDOFF.md`;
- `Tools/DCC/audit_bloodaxe_cairnstone_a005_s10r006_r7_a_cross_view_corner_ownership_rule_a01.py`;
- A005 reset/resume, approval log, and artifact index only for the exact
  candidate result and unchanged authority limits; and
- recovery journal and checkpoint metadata through the checkpoint tool only.

No image or diagram is authorized. A corner-sector visual could be mistaken
for selected ownership, a seam, interpolation, a field, or geometry.

## Explicitly Forbidden

- executing this contract without exact approval;
- approving the candidate rule during execution;
- evaluating or enumerating any q or m_k value as a sample or coordinate;
- creating per-record or per-point owner instances;
- assigning source pixels, source normals, target points, physical points, or
  geometry sectors to an owner;
- using intended outward normals as recovered physical evidence;
- copying historical I10-010-A as authority;
- introducing joint ownership, dominant-normal evaluation, fixed panel
  priority, visual matching, tolerance, interpolation, blending, or repair;
- creating or selecting a cross-lane seam, cross-view seam, endpoint join,
  top/upright join, wrap, or closure;
- evaluating q_L, B_v, C_L, W_L, or H_v;
- creating a transform, physical pair, target coordinate, center, pivot, or
  anchor;
- using back/right holdouts for construction;
- creating a field, raster, mask, fill, surface, topology, or geometry;
- creating imagery, overlays, DCC, Blender, texture, FBX, collision, LOD,
  Unreal, render, or production work;
- Step 10 closeout or Step 11;
- editing locked source evidence or historical authority records;
- staging, commit, or push; and
- continuing into rule approval or implementation in the same task.

## Required Validation Gates For Later Execution

Execution must fail closed unless:

1. all sixteen locked inputs match;
2. this contract hash and exact execution approval match;
3. R6-A remains the selected preparation-only route;
4. R5 remains approved bounded interpretation for four owned arcs only;
5. all four R5 lane intervals and four open gaps replay exactly;
6. q remains non-periodic, unwrapped, and unevaluated;
7. all four gap adjacencies use only the approved construction lane labels;
8. every m_k is an exact symbolic rational midpoint;
9. each lower branch maps only to its predecessor label;
10. each upper branch maps only to its successor label;
11. the branches are total and pairwise disjoint over each open gap;
12. existing R5 endpoint ownership is unchanged;
13. G_3 creates no q wrap, modulo, new lane, or endpoint identification;
14. historical I10-010-A remains revision-required candidate history;
15. all fourteen back/right records remain proof only;
16. no top/upright ownership, seam, join, interpolation, or closure is
    defined;
17. the candidate rule is registered but unapproved;
18. per-point owner instances, q instances, samples, coordinates, transforms,
    pairs, centers, pivots, and anchors remain 0;
19. fields, fills, surfaces, topology, and geometry remain 0;
20. all three blocks remain active and resolved block IDs remain empty;
21. evaluation, implementation, downstream, and Git authorization flags
    remain false;
22. changed paths match the execution allowlist and no path is staged; and
23. output and handoff visibility are verified before the mandatory stop.

## Machine-Verified Input Lock At Preparation

~~~text
5d2d2637a58113f0a6f5ec92e40d8bb2bda9e03fb58b4868a0d9dfbb3b57ad55  AGENTS.md
ba6784498d792dc85dd431c807f59620d6851af97b4cd15efe89c44a397b10b6  docs/projects/assetforge/BLOODAXE_CAIRNSTONE_PIXEL_EXACT_FRESH_START_MULTISTEP_PLAN.md
1383a975b0c376be4c493fd41f3b81a2f94c2e62dce4a9b758e7a1d2e9e51d90  docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A005/SM_GIA_BloodAxeCairnstone_A005_PROJECT_CHARTER.md
8a599ef21348c99bee154b41a1d10306392a6f93f1aabc583e8ed3369b08729f  docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A005/SM_GIA_BloodAxeCairnstone_A005_RESET_RESUME_STATE.md
3d0242426ac38f62c1a0abeb65e32b5c9a112f428d5d4d74c367cde9e73356c5  docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A005/SM_GIA_BloodAxeCairnstone_A005_APPROVAL_LOG.md
86aae09f2aa71bfac29cd0c8ef148ae3cce9ba3b9fcdfcd29b4b607872091f1f  docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A005/SM_GIA_BloodAxeCairnstone_A005_ARTIFACT_INDEX.md
ccfce6b8316369b512ff83eee11fd4385dd15b546f7b92da9e80b9e7ed959d1d  docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A005/manifests/STEP_05_PIXEL_COORDINATE_FRAME_RECORD.json
ca83a60d1ec2e607b688b14605f100333c473cf094f1b3d4036ac52767ca64ea  docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A005/manifests/STEP_10_INTERPRETATION_OPTION_REGISTRY.json
b6a380a4ff0d456c45f30061b372d68600f747974d0c80170f520491f7c0f84a  docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A005/manifests/STEP_10R_N3_INTEGRATION_AUTHORITY_DELTA.json
0eb0e0a8abcc554209746f2437e9073951ae7896aca9606a70dd98b202e1edc3  docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A005/manifests/S10R_006_R5_A_LANE_BOUNDARY_COUPLING_RULE_A01_RULE_REGISTRY.json
ee155e6ce7f1da3dfdd1f448fcdaaf6d30038072da14fdcac60df98aed399b1d  docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A005/manifests/S10R_006_R5_A_LANE_BOUNDARY_COUPLING_RULE_A01_VALIDATION.json
d39d9414c597769bceff1a441ec2f84d0735749ab49b0758bf27d2b3015539bb  docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A005/steps/S10R_006_R5_A_LANE_BOUNDARY_COUPLING_RULE_A01_OUTPUT_RECORD.md
3529c2f8dc30361b6412c9e86aa813ad7631dad99705107d331400a8de1b2c08  docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A005/manifests/S10R_006_R6_A_CROSS_VIEW_CORNER_OWNERSHIP_AUTHORITY_OPTION_REGISTRY.json
690054802be12ef93d19198e77f9d4195843e41342502e275f0d7c7c52e8658d  docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A005/manifests/S10R_006_R6_A_CROSS_VIEW_CORNER_OWNERSHIP_AUTHORITY_VALIDATION.json
400b0769aba37a108e24e3ed47c97f5b07ca676dbf12be9f701f4168d13b7c8a  docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A005/steps/S10R_006_R6_A_CROSS_VIEW_CORNER_OWNERSHIP_AUTHORITY_DECISION_OUTPUT_RECORD.md
d0b1370c5b7c6f8a9745c25c4896aec8f1d666c681f66e0ae7febe041a3cee13  docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A005/handoffs/S10R_006_R6_A_CROSS_VIEW_CORNER_OWNERSHIP_AUTHORITY_TO_DECISION_HANDOFF.md
~~~

Preparation checkpoint: `Saved/ProjectRecovery/20260720-095818/`.

The three A005 status records may change after this lock only to record this
prepared contract and its required next-task stop. Every other locked input
must remain byte-identical before later execution.

Preparation Git state:

- branch: `main`;
- HEAD: `f5259456b05a95ff5f7422ba2cabf0e288a85d03`;
- staged paths: `0`; and
- pre-existing R7 artifacts: `0`.

## Artifact Classification After Preparation

- this contract: candidate;
- approved R5 rule and closeout records: unchanged authoritative within their
  bounded scope;
- selected R6 route and post-decision routing: unchanged authoritative within
  their preparation-only scope;
- R5/R6 validations and diagnostics: proof only;
- historical I10-010 options: unchanged candidate historical records;
- proposed R7 rule: candidate and unexecuted;
- original source evidence and prior classifications: unchanged; and
- authoritative corner ownership, rule evaluation, seams, joins, closure,
  field, geometry, and downstream authority: absent.

## Preparation Validation

Result: `pass_candidate_contract_content_validated_pending_external_visibility_record`.

- locked inputs before controlled status updates: `16/16` matched;
- R6 selected preparation route: exact;
- R5 owned lane intervals and blocked gaps: `4` and `4`;
- Step 05 cardinal adjacency: +X, +Y, -X, -Y;
- gap rule branches: exactly predecessor-lower and successor-upper;
- tie policy: single successor owner label, candidate interpretation only;
- historical I10-010-A: unchanged and `requires_revision`;
- selected or approved R7 rule: none;
- q instances, owner instances, samples, coordinates, seams, joins, closures,
  fields, fills, surfaces, topology, and geometry: `0`;
- R7 artifacts created during initial preparation: this contract only;
- controlled A005 status updates: exact prepared-contract state only;
- staged paths: `0`; and
- visible review: final on-disk exact-title verification is required and must
  be recorded in the authoritative A005 status records after verification.

## Required Next-Task Stop

After final preparation validation, visible presentation, status recording,
and checkpointing, stop. Execution of this contract is the next task and
requires its own exact approval.

> Do you approve execution of
> `A005-CR-S10R-006-R7-A-CVCOR-A01` exactly as written, limited to registering
> one candidate, unevaluated, half-open successor-at-tie owner-label rule over
> G_0 through G_3; preserving Step 05, R5, R6, proof-only holdouts, no-wrap,
> no-seam, no-join, no-closure, zero-instance, and all downstream stops;
> validating independently; opening the output and handoff visibly;
> checkpointing; and stopping for the separate rule-result decision?

Approval of contract execution does not approve the candidate rule.
