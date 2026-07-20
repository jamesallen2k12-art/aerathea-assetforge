# A005 S10R-006-R9-A Corner-Gap-To-Field Coupling Rule A01 Contract

Status: candidate bounded rule contract prepared for visible Flamestrike review; execution not authorized

Artifact classification: `candidate`

Contract ID: `A005-CR-S10R-006-R9-A-CGFC-A01`

Proposed rule ID: `S10R-006-R9-A-CGFC-A01`

Date: 2026-07-20

## Preparation Authority

Flamestrike explicitly selected `S10R-006-R8-A` by stating
`I agree we will follow your recommendation`. The authoritative selected
result is:

`later preparation only of a bounded corner-gap-to-field coupling rule contract`.

Flamestrike then stated `proceed` directly to the active preparation-only step
contract. This authorizes preparation and validation of this one bounded
candidate contract, exact A005 status updates, visible presentation,
checkpointing, and a mandatory stop for separate execution approval.

It does not authorize contract execution, candidate-rule registration, rule
approval, rule evaluation, q/u/owner/record instances, sampling, source or
target assignments, transforms, physical correspondence, seam, join,
continuity, interpolation, wrap, closure, field, fill, surface, topology,
geometry, Step 10 closeout, Step 11, DCC, Unreal, production, staging, commit,
or push.

## Controlling First Principles

- Actual project goal: advance A005 toward one coherent 360-degree game object
  while preserving the line between approved symbolic interpretation, source
  evidence, and physical geometry authority.
- Blueprint authority: Step 10 permits written interpretation options and
  explicit rule proposals; it forbids implementation, geometry, silently
  chosen rules, and interpretation presented as measurement.
- R3 authority: one approved unevaluated within-lane record-weight method over
  `0 <= u <= 1`, with no cross-lane interpolation.
- R5 authority: one approved unevaluated q/B_v/C_L descriptor over four closed
  lane intervals only; all four open corner gaps remain outside its coupling
  scope.
- R7 authority: one approved unevaluated predecessor/successor owner-label
  rule over the four open gaps, with successor ownership at each symbolic
  midpoint and no seam, join, closure, or physical correspondence claim.
- R8-A authority: prepare one bounded contract describing how R7 gap ownership
  may connect to R5 q/B_v/C_L descriptors.
- Decision produced by this preparation: whether this exact bounded symbolic
  rule may later be registered as a candidate for a separate Flamestrike
  decision.

## Proven Dependency Gap

The current approved records do not define:

- a gap-local relation from `q` to the analytic `B_v(q)` descriptor;
- a relation from R7 `O_k(q)` owner labels to the R3/R5 lane descriptor;
- a gap record-weight descriptor;
- a unified symbolic lane-plus-gap boundary descriptor; or
- any seam, continuity rule, closure, field, source correspondence, target
  coordinate, surface, topology, or geometry.

The R5 inverse lane relation may not be extrapolated into a gap. For a lane
`L`, `q_L(u) = c_L + u - 1/2` is approved only for `0 <= u <= 1`. Any attempt
to solve for a gap q would produce a lane-local u outside that authority.

This contract therefore introduces no extrapolated lane-local u.

## Evidence And Interpretation Boundary

Evidence replayed unchanged:

- R3 `W_lane(u,v)` and its exact `u=0`, `u=1/2`, and `u=1` identities;
- R5 q orientation, four closed lane intervals, endpoint ownership,
  `B_v(q)`, and `C_L(u,v)=B_v(q_L(u))` strings;
- R7 four open gap intervals, four midpoint definitions, eight owner branches,
  and successor-at-tie policy;
- non-periodic unwrapped q and the absence of wrap or final/first endpoint
  identification;
- fourteen proof-only back/right records; and
- every zero-output count and active block.

Candidate interpretation introduced by this contract:

- an owner-selected endpoint selector `e_k(q)` within each gap;
- a gap record-weight descriptor referencing only an already approved lane
  endpoint identity;
- a gap analytic boundary descriptor `C^G_k(q,v)=B_v(q)`;
- a bounded coupling tuple joining owner label, endpoint weight descriptor,
  and analytic boundary descriptor; and
- a unified symbolic lane-plus-gap descriptor.

None of those candidate relations is source evidence, physical
correspondence, target geometry, or authority until separately executed and
then separately approved by Flamestrike.

## Locked Approved Domains

### R5 Owned Lane Domain

| Lane ID | Cardinal | Closed q interval | Existing relation |
|---|---|---|---|
| `AFM-FRONT-RIGHT` | `+X` | `[-1/2,1/2]` | `C_L(u,v)=B_v(q_L(u))` |
| `AFM-LEFT-LEFT` | `+Y` | `[3/2,5/2]` | `C_L(u,v)=B_v(q_L(u))` |
| `AFM-FRONT-LEFT` | `-X` | `[7/2,9/2]` | `C_L(u,v)=B_v(q_L(u))` |
| `AFM-LEFT-RIGHT` | `-Y` | `[11/2,13/2]` | `C_L(u,v)=B_v(q_L(u))` |

Each lane continues to own both endpoints of its closed interval. This
contract does not modify R5 lane authority.

### R7 Open Gap Domain

| Gap | Open q interval | Predecessor owner | Successor owner | Midpoint tie owner |
|---|---|---|---|---|
| `G_0` | `(1/2,3/2)` | `AFM-FRONT-RIGHT / +X` | `AFM-LEFT-LEFT / +Y` | successor |
| `G_1` | `(5/2,7/2)` | `AFM-LEFT-LEFT / +Y` | `AFM-FRONT-LEFT / -X` | successor |
| `G_2` | `(9/2,11/2)` | `AFM-FRONT-LEFT / -X` | `AFM-LEFT-RIGHT / -Y` | successor |
| `G_3` | `(13/2,15/2)` | `AFM-LEFT-RIGHT / -Y` | `AFM-FRONT-RIGHT / +X label-only successor` | successor |

`G_3` remains unwrapped. `q=15/2` is not added to the domain and is not
identified with `q=-1/2`.

## Proposed Bounded Candidate Rule

Later execution may register exactly the following candidate relations and no
others.

### 1. Preserve R7 Owner Labels

For every existing open gap `G_k=(a_k,b_k)` with approved midpoint
`m_k=(a_k+b_k)/2`, retain the approved R7 relation:

~~~text
O_k(q) = P_k  when a_k < q < m_k
O_k(q) = S_k  when m_k <= q < b_k
~~~

`P_k` and `S_k` are the exact predecessor and successor labels already stored
in R7. The midpoint belongs to the successor branch.

### 2. Define Only An Owner Endpoint Selector

Define the candidate symbolic endpoint selector:

~~~text
e_k(q) = 1  when a_k < q < m_k
e_k(q) = 0  when m_k <= q < b_k
~~~

Meaning:

- `e_k(q)=1` references the predecessor lane's already approved `u=1`
  endpoint identity;
- `e_k(q)=0` references the successor lane's already approved `u=0`
  endpoint identity; and
- no other u value exists in a gap.

This selector is not a gap-local coordinate, interpolation parameter, inverse
q map, or lane extrapolation. It selects one of two existing symbolic endpoint
identities only.

### 3. Define A Gap Record-Weight Descriptor

Let `ell(O_k(q))` mean only the exact lane-ID portion of the approved R7 owner
label. Using the approved R3 descriptor, propose:

~~~text
W^G_k(q,v) = W_{ell(O_k(q))}(e_k(q),v)
~~~

Therefore the predecessor half references that lane's `T_2` endpoint identity
and the successor half, including the midpoint, references that lane's `T_0`
endpoint identity.

This is an unevaluated symbolic record-weight reference only. It does not
assign a source pixel, normal, coordinate, transform, physical pair, or target
point. For the upper branch of `G_3`, `AFM-FRONT-RIGHT / +X` remains a
label-only successor. Referencing its `u=0` record identity does not wrap q or
identify the final and first q endpoints.

### 4. Define A Gap Analytic Boundary Descriptor

For `q` strictly inside `G_k` and `0 <= v <= 1`, propose:

~~~text
C^G_k(q,v) = B_v(q)
~~~

where the exact existing R5 analytic string remains:

~~~text
B_v(q) = (a(v)*spow_2_3(cos(theta(q))), b(v)*spow_2_3(sin(theta(q))))
~~~

This extends only the symbolic analytic descriptor into the four open gaps.
It does not evaluate q or v, instantiate a point, or claim physical source
correspondence. Analytic equality at any mathematically repeating angle is
not endpoint identity, wrap, seam, closure, continuity, topology, or geometry.

### 5. Define The Bounded Gap Coupling Tuple

For `q` strictly inside `G_k`, propose the unevaluated symbolic tuple:

~~~text
K_k(q,v) = (O_k(q), e_k(q), W^G_k(q,v), C^G_k(q,v))
~~~

The tuple records only which approved symbolic owner endpoint descriptor is
associated with which unevaluated analytic gap-boundary descriptor.

### 6. Define A Unified Symbolic Descriptor Without Closure

Let `D_L` remain the union of the four approved R5 closed lane intervals and
let `D_G=G_0 union G_1 union G_2 union G_3`. Propose:

~~~text
C*(q,v) = C_L(u,v)       when q=q_L(u), q in the owned interval of L, 0 <= u <= 1
C*(q,v) = C^G_k(q,v)     when q in G_k
~~~

The combined symbolic domain is `D_L union D_G = [-1/2,15/2)`. The upper
endpoint remains excluded. Existing lane endpoints remain lane-owned, so the
piecewise cases do not overlap.

`C*` is a symbolic descriptor only. It is not a field instance, seam,
continuity claim, join, closure, wrap, fill, surface, topology, or geometry.

## Exact Branch Replay Required From Later Execution

| Gap | Lower branch endpoint reference | Upper branch endpoint reference |
|---|---|---|
| `G_0` | `AFM-FRONT-RIGHT / +X`, `u=1` | `AFM-LEFT-LEFT / +Y`, `u=0` |
| `G_1` | `AFM-LEFT-LEFT / +Y`, `u=1` | `AFM-FRONT-LEFT / -X`, `u=0` |
| `G_2` | `AFM-FRONT-LEFT / -X`, `u=1` | `AFM-LEFT-RIGHT / -Y`, `u=0` |
| `G_3` | `AFM-LEFT-RIGHT / -Y`, `u=1` | `AFM-FRONT-RIGHT / +X label-only successor`, `u=0`, no wrap |

Later execution must register exactly four gap tuples, eight symbolic endpoint
selector branches, four gap analytic-descriptor declarations, and one unified
piecewise descriptor. Every evaluated-instance count must remain zero.

## Explicit Non-Claims

The proposed rule does not define or claim:

- a gap-local continuous u coordinate;
- extrapolated lane-local u;
- interpolation between predecessor and successor records;
- cross-lane or cross-view blending;
- physical source ownership or correspondence;
- source pixels, normals, target coordinates, transforms, or physical pairs;
- an evaluated q, u, v, owner, endpoint, weight, or boundary sample;
- continuity at a gap midpoint or lane endpoint;
- a seam, join, top/upright relation, closure, or wrap;
- a closed or implemented field;
- a fill, surface, topology, or geometry; or
- resolution of `S10R-BLOCK-006`, `S10R-BLOCK-008`, or
  `S10R-BLOCK-009`.

## Required Validation Gates For Later Execution

Later execution must fail closed unless:

1. every locked preparation input and this contract hash match;
2. Flamestrike separately approves execution of this exact contract;
3. R8-A remains the only selected route;
4. R3, R5, and R7 remain approved, bounded, and unevaluated;
5. the four R5 closed lane intervals and four R7 open gaps replay exactly;
6. R5 endpoint ownership and R7 successor-at-tie policy remain unchanged;
7. q remains non-periodic and unwrapped, with `15/2` excluded and no
   final/first identification;
8. `e_k(q)` contains exactly the eight approved predecessor-`u=1` and
   successor-`u=0` symbolic branches;
9. `W^G_k(q,v)` references only R3 endpoint identities and creates no source
   or physical assignment;
10. `C^G_k(q,v)=B_v(q)` is registered as an unevaluated gap descriptor only;
11. the unified descriptor uses existing R5 C_L authority on lanes and the
    proposed C^G_k relation only inside gaps;
12. no lane-local u is extrapolated outside `0 <= u <= 1`;
13. exactly one candidate rule is registered and remains unapproved;
14. all q/u/v/owner/record/weight/boundary instances and samples remain zero;
15. all source assignments, normals, transforms, pairs, and target
    coordinates remain zero;
16. all seams, joins, closures, fields, fills, surfaces, topology, and
    geometry remain zero;
17. all fourteen back/right records remain proof only;
18. all three blocks remain active and resolved block IDs remain empty;
19. evaluation, implementation, downstream, and Git authority flags remain
    false;
20. changed paths match the later execution allowlist and no path is staged;
21. the independent read-only auditor passes every gate in its first complete
    run; and
22. final output and handoff records are visibly presented before the
    mandatory stop.

## Mandatory BLOCK Fallback

If any input, formula, branch, count, authority, scope, visibility, or audit
gate fails during later execution:

- result:
  `blocked_corner_gap_to_field_coupling_rule_dependency_or_scope_failure`;
- register no candidate rule;
- preserve R3, R5, R7, and the R8-A route selection unchanged;
- preserve every zero-output count and active block;
- quarantine any affected partial output if it cannot be removed from the
  decision path cleanly; and
- stop without rerunning, repairing forward, or redesigning the rule in the
  same execution task.

## One Result Required From Later Execution

After separate exact execution approval, execution must produce exactly one:

1. `pass_candidate_bounded_corner_gap_to_field_coupling_rule_registered_no_implementation`
   if all gates pass;
2. `blocked_corner_gap_to_field_coupling_rule_dependency_or_scope_failure`
   if any dependency, rule, count, visibility, or authority gate fails; or
3. `blocked_integrity_or_scope_failure` on any hash mismatch, unexpected
   write, staging, output instantiation, or downstream action.

A pass registers only one candidate symbolic rule for a later separate
Flamestrike approve/reject/blocked decision. It does not approve or evaluate
the rule.

## Allowed Output Paths After Separate Execution Approval

- `manifests/S10R_006_R9_A_CORNER_GAP_TO_FIELD_COUPLING_RULE_A01_INPUT_LOCK.json`;
- `manifests/S10R_006_R9_A_CORNER_GAP_TO_FIELD_COUPLING_RULE_A01_RULE_REGISTRY.json`;
- `manifests/S10R_006_R9_A_CORNER_GAP_TO_FIELD_COUPLING_RULE_A01_VALIDATION.json`;
- `steps/S10R_006_R9_A_CORNER_GAP_TO_FIELD_COUPLING_RULE_A01_OUTPUT_RECORD.md`;
- `handoffs/S10R_006_R9_A_CORNER_GAP_TO_FIELD_COUPLING_RULE_A01_TO_DECISION_HANDOFF.md`;
- `Tools/DCC/audit_bloodaxe_cairnstone_a005_s10r006_r9_a_corner_gap_to_field_coupling_rule_a01.py`;
- exact A005 reset/resume, approval-log, and artifact-index updates; and
- recovery-journal and checkpoint metadata through the checkpoint tool only.

## Explicitly Forbidden

- executing this contract without separate exact approval;
- modifying R3, R5, R7, or the R8-A selection records;
- introducing any route other than selected R8-A;
- registering more than one candidate rule;
- approving, evaluating, or implementing the candidate rule;
- defining a continuous gap-local u or extrapolating lane-local u;
- creating q/u/v/owner/record/weight/boundary instances or samples;
- assigning source pixels, normals, coordinates, transforms, pairs, centers,
  pivots, or anchors;
- defining continuity, interpolation, a seam, join, wrap, closure, field,
  fill, surface, topology, or geometry;
- resolving any block;
- Step 10 closeout, Step 11, DCC, Blender, Unreal, rendering, or production;
  and
- staging, commit, or push.

## Machine-Verified Preparation Input Lock

~~~text
5d2d2637a58113f0a6f5ec92e40d8bb2bda9e03fb58b4868a0d9dfbb3b57ad55  AGENTS.md
ba6784498d792dc85dd431c807f59620d6851af97b4cd15efe89c44a397b10b6  docs/projects/assetforge/BLOODAXE_CAIRNSTONE_PIXEL_EXACT_FRESH_START_MULTISTEP_PLAN.md
1383a975b0c376be4c493fd41f3b81a2f94c2e62dce4a9b758e7a1d2e9e51d90  docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A005/SM_GIA_BloodAxeCairnstone_A005_PROJECT_CHARTER.md
3b2f45a5d57234f3a8204cf594ec444ffb58ec4ece04a66580c1364018688fad  docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A005/SM_GIA_BloodAxeCairnstone_A005_RESET_RESUME_STATE.md
b6feed49c36feec7c26cf53d76d9da4f6edfcf570deed69f1b39ecc5ad79c37f  docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A005/SM_GIA_BloodAxeCairnstone_A005_APPROVAL_LOG.md
421011ab74c3f9ab0697e099916b8f241ec23cec9b01998721a98ee8e3a5d006  docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A005/SM_GIA_BloodAxeCairnstone_A005_ARTIFACT_INDEX.md
213a15f1ec8af82673ac73fe91afd45a72ef305bb62e5f1eb5da341b625db9ba  docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A005/manifests/S10R_006_R3_A_ABSTRACT_FIELD_METHOD_A01_METHOD_REGISTRY.json
0eb0e0a8abcc554209746f2437e9073951ae7896aca9606a70dd98b202e1edc3  docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A005/manifests/S10R_006_R5_A_LANE_BOUNDARY_COUPLING_RULE_A01_RULE_REGISTRY.json
1f98ab82521d41566e7a9908b9416ba9d2841487f191c96f54d33d21fa642c54  docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A005/manifests/S10R_006_R7_A_CROSS_VIEW_CORNER_OWNERSHIP_RULE_A01_RULE_REGISTRY.json
372895b6c346b0b6ba8d5a68c08026c3e6f555db08a4f6ce7bc8d73d3cd33713  docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A005/steps/S10R_006_R8_R2_A_GATE10_WORDING_CORRECTION_CONTRACT.md
e8c4b47076e88c5ed4638554f5a0a80ad7c91bfe48e3b5b47e81ecde8b5869a7  docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A005/manifests/S10R_006_R8_R2_A_GATE10_WORDING_CORRECTION_INPUT_LOCK.json
80a3225468e3cec662b7bc9805becdcaf86c0353d66c9ca3cd7874d070fce256  docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A005/manifests/S10R_006_R8_R2_A_GATE10_WORDING_CORRECTION_WORDING_AUTHORITY_AUDIT.json
683f5e4568823819714c6b105bf3196cda3da31a0d849f9362bc604f3e96d985  docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A005/manifests/S10R_006_R8_R2_A_GATE10_WORDING_CORRECTION_OPTION_REGISTRY.json
43fd3f1750d74d66c51f79160e2c111364e9c71e3888c861d9f237a892492c99  docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A005/manifests/S10R_006_R8_R2_A_GATE10_WORDING_CORRECTION_VALIDATION.json
28cdb350802d0c7f7be467642b590461c8db15f4662f00a2a313ad21e1f1bf8a  docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A005/steps/S10R_006_R8_R2_A_GATE10_WORDING_CORRECTION_DECISION_OUTPUT_RECORD.md
86113c39fa265b1323abf5e8a58e6dc46619a97adc1e8c3e23261d1d9371fc1d  docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A005/handoffs/S10R_006_R8_R2_A_GATE10_WORDING_CORRECTION_TO_DECISION_HANDOFF.md
~~~

Locked preparation inputs: `16/16` matched.

Pre-preparation checkpoint: `Saved/ProjectRecovery/20260720-130150/`.

Preparation Git state:

- branch: `main`;
- HEAD: `f5259456b05a95ff5f7422ba2cabf0e288a85d03`;
- staged paths: `0`;
- outside-preparation-allowlist record count: `837`;
- outside-preparation-allowlist porcelain-v1-z SHA-256:
  `b6cd70714f653ff49ca00bceac9f98744785004f264964ab37409cdc74e40e3f`;
  and
- pre-existing R9 contract paths: `0`.

The three A005 status records may change after this lock only to record the
prepared-contract state. Every other locked input must remain byte-identical.

## Preparation Validation

Preparation must confirm:

- locked inputs: `16/16` matched;
- selected route: exactly `S10R-006-R8-A`;
- proposed candidate rules: `1`;
- candidate rules registered or approved during preparation: `0`;
- gap branches described: `8`;
- gap analytic descriptor declarations: `4`;
- lane-local u values permitted in gaps: exactly endpoint selectors `0` and
  `1`, with no interpolation or extrapolation;
- evaluated instances and samples: `0`;
- seams, joins, closures, fields, fills, surfaces, topology, and geometry:
  `0`;
- active blocks: `3`; resolved blocks: `0`;
- changed paths: exactly the preparation allowlist;
- staged paths: `0`; and
- final on-disk contract visibly verified through exact title
  `A005_R9_CGFC_RULE_CONTRACT_REVIEW`.

## Required Next-Task Stop

After preparation validation, controlled status recording, visible
presentation, and checkpointing, stop. Contract execution requires separate
exact approval.

> Do you approve execution of
> `A005-CR-S10R-006-R9-A-CGFC-A01` exactly as written, limited to registration
> of one unapproved, unevaluated candidate symbolic corner-gap-to-field
> coupling rule; preservation of non-periodic unwrapped q, R5 lane endpoints,
> R7 successor-at-tie ownership, all proof-only holdouts, every zero-output
> count, all three active blocks, and every downstream stop; one independent
> complete audit; visible output and decision handoff; checkpointing; and a
> mandatory stop for a separate Flamestrike rule decision?

Approval of execution would not approve or evaluate the candidate rule.
