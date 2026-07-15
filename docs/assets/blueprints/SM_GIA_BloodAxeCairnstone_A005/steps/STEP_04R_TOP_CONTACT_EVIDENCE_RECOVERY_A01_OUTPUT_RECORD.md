# Step 04R Top Contact Evidence Recovery A01 Output Record

Status: Step 04R complete and approved; recovery content pushed; mandatory restart

Artifact classification: `authoritative`

Date: 2026-07-15

## Assigned Goal

Replace only the defective Step 04 top-contact proof with exact source-owned,
unfilled evidence for `CL-001`, `CL-002`, and `CL-003`, while preserving the
original quarantined artifacts and leaving downstream authority suspended.

## Approved Decision

The authoritative top panel directly supports discrete visible samples for all
three semantic contact relationships:

- `CL-001`, between `C-001` and `C-002`: `16` exact pixels;
- `CL-002`, between `C-002` and `C-003`: `16` exact pixels;
- `CL-003`, between `C-003` and `C-004`: `16` exact pixels.

Each contact has four manually audited source pixels in each visible cardinal
sector: top, bottom, left, and right. These are discrete observations only.
Continuity between samples and every hidden closure remain blocked.

## Evidence Produced

- recovery inventory:
  `manifests/STEP_04_COMPONENT_OWNERSHIP_INVENTORY_RECOVERY_A01.json`;
- exact point manifest:
  `manifests/STEP_04_TOP_CONTACT_EVIDENCE_RECOVERY_A01.json`;
- unfilled review board:
  `evidence/STEP_04_RECOVERY/SM_GIA_BloodAxeCairnstone_A005_STEP_04_TOP_OWNERSHIP_EVIDENCE_RECOVERY_A01.png`;
- focused validation:
  `manifests/STEP_04_TOP_CONTACT_EVIDENCE_RECOVERY_A01_VALIDATION.json`.

The board contains an untouched authoritative top tile and one exact-resolution
marked copy. Every cross center maps to one manifest coordinate. No line joins
two samples.

## Source-Ownership Method

- fresh manual native-pixel audit of the authoritative Step 03 top crop;
- zero-based integer pixel centers;
- full-source mapping `x_full = x_local + 393`,
  `y_full = y_local + 1073`;
- exact source RGB and 5x5 RGB-neighborhood hashes recorded per point;
- two-pixel inward and outward named-component witness pixels recorded;
- diagnostic searches had no authority;
- original quarantined Step 04 coordinates were not reused.

## Rejected Internal Diagnostic

The first fresh local diagnostic was rejected and preserved as
`invalid internal diagnostic; rejection evidence only` because it contained
two near-white `CL-003` candidates:

- `(195,47)`, RGB `(251,251,251)`;
- `(190,251)`, RGB `(239,240,239)`.

Preserved local path:

`Saved/Automation/DCC/SM_GIA_BloodAxeCairnstone_A005/CoreRecovery/20260715_STEP04_TopContactEvidenceDrift/A005_STEP04R_ContactCandidate_A01_REJECTED.png`

Neither rejected coordinate appears in the recovery manifest or board.

## Validation

- builder validators: `24` passed, `0` failed;
- independent read-only audit validators: `30` passed;
- accepted source pixels: `48`;
- per-contact counts: `16 / 16 / 16`;
- panel-local/full-source coordinate error: `0 px`;
- source tile changed pixels: `0`;
- source tile maximum RGB delta: `0`;
- marked review tile reconstruction: exact;
- original quarantined artifacts: byte-identical;
- semantic component/contact IDs changed: false;
- line interpolation or hidden closure: absent;
- interpretation or geometry: absent;
- Step 05-07 restored: false;
- Step 08 output created: false;
- unrelated staged files: `0`.

## Assumptions And Interpretations

No physical continuity, hidden interface, complete perimeter, component mask,
center, calibration, orientation, transform, or geometry is asserted. Contact
pixels are exact visible observations only.

## Artifact Status

- Step 04R contract: `authoritative` for execution scope;
- recovery inventory and exact contact manifest: `authoritative`;
- recovery board and validation: `proof only`;
- original Step 04 top board and completion proof: remain `quarantined`;
- Step 05-07: remain `quarantined/suspended pending dependency audit`;
- Step 08: stopped with no output authority.

## Checkpoints

- Pre-action: `Saved/ProjectRecovery/20260715-162256/`.
- Validated-candidate checkpoint: `Saved/ProjectRecovery/20260715-163538/`.
- Approved pre-closeout checkpoint: `Saved/ProjectRecovery/20260715-163837/`.
- Final restart-handoff checkpoint: `Saved/ProjectRecovery/20260715-164736/`.

## Output Approval

- Approver: Flamestrike.
- Statement: `approved`.
- Date: 2026-07-15.
- Scope: the visible Step 04R recovered top-contact package only.

The recovered inventory and exact contact observations are authoritative.
Evidence and validation remain proof only. No Step 05-07 restoration or Step
08 action was approved.

## Next Gate

Complete scoped closeout, commit, push, and mandatory restart. The next agent
must perform the Core resume handshake and may present a Step 05-07 dependency-
audit contract only. The audit is not authorized by this output approval or by
the restart handoff.

## Scoped Commit And Push

- Recovery content commit: `a8ae9ec`.
- Push: success to `assetforge/main`.
- Remote advanced from `3e219f0` to `a8ae9ec`.
- Included: seven Step 04R recovery package files and only the single A005
  drift-ledger entry.
- Excluded: every unrelated dirty worktree file and the pre-existing A004
  drift-ledger additions.
