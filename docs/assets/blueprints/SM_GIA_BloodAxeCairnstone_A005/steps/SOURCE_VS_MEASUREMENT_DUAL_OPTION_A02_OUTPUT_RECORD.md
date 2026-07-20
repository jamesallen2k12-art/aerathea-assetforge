# A005 Source-Versus-Measurement Dual-Option Feasibility A02 Output Record

Status: `approved result; both options ineligible`

Artifact classification: `authoritative for bounded A02 decision only`

Contract: `A005-CR-SMR-A02`

Date: 2026-07-17

## Plain-English Result

Neither option is ready to choose.

Option A failed. Scaling C-003 together with the C-004 inner contact preserves
CL-003, but it moves different C-002/C-003 contact samples by different
amounts. One translation cannot keep scaled C-003 connected to unchanged C-002
at every exact CL-002 sample.

Option B was not disproved, but it is blocked before a candidate adjustment can
be drawn. Existing authority owns isolated source-visible C-004 outer points
and discontinuous CL-003 samples. It does not own a continuous outer-to-inner
transition, and the top C-004 perimeter is explicitly blocked. Drawing a
transition would therefore add a new interpretation rule outside this
contract.

## Controlling Result

`both_options_blocked`

## Option A — C-003 Scale With C-004 Inner Contact

- Result: `fail_CL002_exact_contact_preservation`.
- Views audited: `5`.
- CL-003 samples preserved after the shared C-003/C-004 map:
  `47` of
  `47`.
- CL-002 samples re-audited: `40`.
- Views preserving all exact CL-002 samples: `0` of
  `5`.
- Top median / maximum CL-002 residual after the best diagnostic translation:
  `14.16 px / 17.12 px`.
- Ten A01 target factors replayed exactly; formula mismatches: `0`.
- Candidate silhouette created: no.

The diagnostic translation has no center, pivot, anchor, transform, or geometry
authority.

## Option B — C-004 Outer-Only Contact-Locked Adjustment

- Result:
  `blocked_missing_source_owned_C004_outer_to_inner_transition_authority`.
- CL-003 samples held at zero displacement across the five views:
  `47`.
- C-001, C-002, and C-003 changed: no.
- Source-visible outer observation groups audited: `20` across five views,
  including the top view's explicit zero-observation block.
- Top C-004 perimeter status:
  `blocked_by_rubble_shadow_and_discontinuous_CL_003_ownership`.
- Candidate transition or silhouette created: no.
- Option concept disproved: no.

Option B remains the narrower-impact hypothesis, but it is not eligible for
selection without a separately approved boundary-interpretation rule.

## Shared Gates

- Input hashes: `30` matched, `0` mismatched.
- Original source panels changed: no.
- Six physical targets changed: no.
- Existing Step 01-Step 10 records changed: no.
- Hybrid created: no.
- Physical cross-view pixel pairs created: no.
- World frame, center, pivot, anchor, closed perimeter, or filled footprint
  created: no.
- Step 10 revised: no.
- Geometry or production started: no.
- Commit or push: no.

## Approved Artifact Routing

- Contract after execution approval: `authoritative for completed execution
  scope only`.
- Input lock, option registry, option audits, comparison, validation, and board:
  `proof only`.
- Option A rule: `rejected candidate`; not authority.
- Option B rule: `blocked candidate`; not authority and not disproved.
- Technical recommendation: `reference only`; select neither from A02.
- This output: `authoritative for bounded A02 decision only`.
- A02 handoff: `authoritative for blocked routing only`.
- Original source, targets, contacts, and prior A005 authority: unchanged.

## Checkpoints

- Pre-action: `Saved/ProjectRecovery/20260717-101552/`.
- After input lock and option registry: `Saved/ProjectRecovery/20260717-101928/`.
- After both independent option audits: `Saved/ProjectRecovery/20260717-102259/`.

## Required Flamestrike Decision

Flamestrike approved recording the bounded `both_options_blocked` result and
accepted the recommendation to reject Option A while preserving Option B as
blocked but not disproved.

Approval of this output did not authorize a C-004 transition, target change,
hybrid, Step 10 revision, geometry, commit, or push.

## Output Approval

- Date: 2026-07-17.
- Approver: Flamestrike.
- Statement: `I approve your recommendation`.
- Decision: accept `both_options_blocked`.
- Option A classification: `rejected candidate`.
- Option B classification: `blocked candidate; not disproved`.
- Downstream state: stopped.
- Output-decision checkpoint: `Saved/ProjectRecovery/20260717-103156/`.
- Commit and push authorized: false.
