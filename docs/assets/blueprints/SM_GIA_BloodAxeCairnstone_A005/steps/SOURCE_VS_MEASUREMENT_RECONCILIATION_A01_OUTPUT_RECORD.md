# A005 Source-Versus-Measurement Reconciliation A01 Output Record

Status: `candidate; blocked under approved adjustment rules`

Artifact classification: `candidate`

Contract: `A005-CR-SMR-A01`

Date: 2026-07-17

## Plain-English Result

The proposed adjustment cannot be made under the approved rules.

To meet the fixed measurements, C-004 must become smaller in X, Y, and Z.
However, C-004 touches C-003 at multiple approved visible points. Scaling all
of C-004 moves those contact points by different amounts. C-003 is allowed only
one rigid movement, so it cannot follow every contact point at once.

A valid adjusted silhouette would require at least one new permission:

- scale C-003 along with the inner part of C-004; or
- change only the outer part of C-004 while holding its inner C-003 contact in
  place; or
- change one or more measurements.

All three are outside this contract. The work therefore stopped before an
adjusted silhouette was created.

## Controlling Decision

`blocked_contact_preservation_requires_unapproved_C003_scale_or_local_C004_deformation`

## Measurement Factors Tested

The test preserved the six approved targets and used C-001 or the complete
asset as the unchanged review reference. The whole-C-004 size changes required
by the source annotation proportions are:

| View | Axis | Required C-004 factor | Change |
|---|---|---:|---:|
| Front | X | `0.925287356322` | `-7.47%` |
| Front | Z | `0.962243401760` | `-3.78%` |
| Back validation | X | `0.900000000000` | `-10.00%` |
| Back validation | Z | `0.841346153846` | `-15.87%` |
| Left | Y | `0.912592592593` | `-8.74%` |
| Left | Z | `0.847465034965` | `-15.25%` |
| Right validation | Y | `0.911917098446` | `-8.81%` |
| Right validation | Z | `0.859767891683` | `-14.02%` |
| Top | X | `0.891826923077` | `-10.82%` |
| Top | Y | `0.820634920635` | `-17.94%` |

These are feasibility factors only. They were not applied to source pixels or
promoted as component transforms.

## Contact-Preservation Test

- Contact tested: `CL-003`, between C-003 and C-004.
- Approved top-view contact samples tested: `16`.
- Permitted C-003 correction: one rigid translation only.
- Median mismatch after the best rigid-translation diagnostic: `15.45 px`.
- RMS mismatch: `15.38 px`.
- Maximum mismatch: `18.99 px`.
- All mismatches zero: `false`.
- One rigid translation can preserve all contacts: `false`.

The best-translation calculation is diagnostic only. It is not a physical
center, anchor, pivot, or proposed component transform.

## What Was And Was Not Created

- Original source panels changed: no.
- Physical measurements changed: no.
- Diagnostic contact overlay: yes, `proof only`.
- Adjusted silhouette: no.
- Closed contact or hidden surface: no.
- Center, origin, pivot, anchor, topology, or geometry: no.
- Existing Step 01-Step 10 records changed: no.
- Step 10 revised: no.
- Step 11 or production started: no.
- Commit or push: no.

## Artifact Status Before Flamestrike's Decision

- Input lock and validation: `proof only`.
- Review board: `proof only`.
- Rules, adjustment ledger, this output record, and blocked handoff:
  `candidate`.
- Original source and previous A005 authority: unchanged.

## Checkpoints

- Pre-action: `Saved/ProjectRecovery/20260717-094024/`.
- After input lock and rule record: `Saved/ProjectRecovery/20260717-094646/`.
- After board and adjustment ledger: `Saved/ProjectRecovery/20260717-095106/`.

## Required Flamestrike Decision

Approve recording this proposal as blocked and keep later work stopped, or
reject the result. A separate future decision is required before choosing any
new adjustment rule.

