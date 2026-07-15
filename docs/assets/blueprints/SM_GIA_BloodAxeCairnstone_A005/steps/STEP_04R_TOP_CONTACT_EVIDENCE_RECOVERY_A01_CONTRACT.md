# Step 04R Contract - Top Contact Evidence Recovery A01

Status: approved for execution

Artifact classification: `authoritative` for execution scope

Date: 2026-07-15

## Decision

Determine which exact authoritative top-panel pixels visibly support
`CL-001`, `CL-002`, and `CL-003`, replacing invalid review coordinates without
changing component semantics or inventing hidden contact closure.

## Governing Authority

Core Recovery Protocol, Evidence-Bound Decision Rule, the approved fresh-start
plan's Step 04 scope, the original Step 04 contract, and the current A005 Core
Recovery status.

## Approval

- Approver: Flamestrike
- Statement: `approved`
- Date: 2026-07-15
- Scope: the exact visible Step 04R recovery contract presented after the
  source-ownership drift explanation
- Exclusion: output approval, Step 05-07 authority restoration, Step 08,
  interpretation, geometry, and every adjacent action

## Approved Inputs

- authoritative A02 source and scanline evidence;
- authoritative Step 03 top crop and crop manifest;
- original Step 04 contract;
- existing `C-001` through `C-007`, `CL-001` through `CL-003`, `OS-001`
  through `OS-003`, and `U-001` through `U-009` only as candidate semantic
  inventory;
- quarantined Step 04 board and coordinates only as drift evidence;
- A005 recovery status and drift-ledger entry;
- generic native-pixel validation rules containing no legacy Cairn Stone
  constants.

## Allowed Actions

- checkpoint and verify every input identity and hash;
- re-audit only top-panel observations for `CL-001`, `CL-002`, and `CL-003`;
- record exact integer pixels or discrete source-pixel samples only where the
  named visible component contact is directly supported;
- record panel-local and full-source coordinates with `0 px` round-trip error;
- record source RGB and native-pixel neighborhood evidence;
- keep contacts discontinuous and stop at rubble, shadow, annotation, or
  ambiguous ownership;
- classify unsupported sectors as ambiguous or blocked;
- create an unfilled point-only recovery board and focused validation;
- compare the original quarantined board against the recovered board;
- open the complete review package in visible desktop windows;
- after separate output approval, checkpoint, commit, and push only scoped
  recovery outputs.

## Scoped Writable Outputs

- `manifests/STEP_04_COMPONENT_OWNERSHIP_INVENTORY_RECOVERY_A01.json`;
- `manifests/STEP_04_TOP_CONTACT_EVIDENCE_RECOVERY_A01.json`;
- `manifests/STEP_04_TOP_CONTACT_EVIDENCE_RECOVERY_A01_VALIDATION.json`;
- `evidence/STEP_04_RECOVERY/SM_GIA_BloodAxeCairnstone_A005_STEP_04_TOP_OWNERSHIP_EVIDENCE_RECOVERY_A01.png`;
- this contract;
- `steps/STEP_04R_TOP_CONTACT_EVIDENCE_RECOVERY_A01_OUTPUT_RECORD.md`;
- `handoffs/STEP_04R_TO_STEP_05_07_DEPENDENCY_AUDIT_HANDOFF.md`;
- scoped updates to recovery status, reset state, artifact index, approval log,
  and drift ledger;
- local-only checkpoints and diagnostics under `Saved/`.

## Blocked

- overwriting or deleting original quarantined artifacts;
- changing component IDs or semantic descriptions;
- footprint, center, dimension, calibration, or orientation measurement;
- hidden contact closure or fitted geometry;
- threshold, primitive, or smoothed authority;
- fills, masks, closed contours, geometry previews, or interpretation;
- using or modifying Step 05-07 records to decide recovery coordinates;
- restoring Step 05-07 authority;
- Step 08, A001-A004 data, DCC, texture, export, or Unreal work;
- staging or committing unrelated changes.

## Validators

- source and top-crop hashes unchanged;
- integer coordinates are in bounds with `0 px` coordinate round-trip error;
- every accepted mark lies on a directly visible source-owned contact for the
  declared component pair;
- no accepted point lies on background, grid, label, dimension, arrow, or
  extension-line pixels;
- every board mark maps exactly to one manifest coordinate, without
  interpolated line extension;
- ambiguous sectors remain blocked;
- original quarantined artifacts remain byte-identical;
- recovered source tile has `0` changed pixels and `0` maximum RGB delta;
- no fill, closure, interpretation, geometry, legacy access, production root,
  or unrelated staged file;
- separate Flamestrike approval or rejection.

## Visible Review

Open the untouched top panel, original quarantined board, recovered board,
recovery manifests, validation, and output record automatically in visible
desktop windows before output approval.

## Artifact Status

Original affected artifacts remain `quarantined`. New records begin as
`candidate`; evidence and validation are `proof only`. Accepted observations
become `authoritative` only after separate Flamestrike approval. Step 05-07
remain suspended.

## Stop Conditions

Hash mismatch, inferred closure, ambiguous accepted ownership, convenient
coordinate selection, downstream modification, Step 08 work, legacy-data need,
or unrelated staged change.

## Smallest Sufficient Change

Replace only defective Step 04 top-contact proof with exact, source-owned,
unfilled evidence. Do not redo the remaining Step 04 inventory.

## Context And Checkpoints

Context demand: moderate; one recovery measurement/evidence/validation/review
pass.

Pre-action checkpoint: `Saved/ProjectRecovery/20260715-162256/`.

After completion, a mandatory restart leads to a separate Step 05-07
dependency-audit contract. Step 08 remains paused.
