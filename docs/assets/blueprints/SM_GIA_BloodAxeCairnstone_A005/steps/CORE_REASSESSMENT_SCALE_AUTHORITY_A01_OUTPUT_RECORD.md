# A005 Scale-Authority Core Reassessment A01 Output Record

Status: `reassessment approved; recovery routing authoritative`

Artifact classification: `authoritative for recovery routing only`

Date: 2026-07-16

## Decision Produced

The field-level Core reassessment confirms `A005-CR-ROLE-A`: the six printed centimeter labels were intended as approximate production targets, and using them as exact per-view pixel calibration premises was retrospective source-role drift.

The last whole-step unaffected boundary is Step 04R. Step 05 is mixed but largely preserved. The first explicit affected action is Step 06's exact centimeter-per-pixel calibration rule.

Flamestrike approved this result after visible review. It is authoritative only for the field-level recovery routing and status override recorded here. It does not perform recovery.

## Input Lock

- pre-action checkpoint: `Saved/ProjectRecovery/20260716-110355/`;
- pre-output A005 Markdown/JSON universe: `101` records;
- all paths, sizes, modification times, and SHA-256 hashes recorded before reassessment output paths opened;
- JSON parse failures: `0`;
- original Step 01-Step 10 records modified: `0`.

## Field-Level Coverage

- direct lexical dimension/calibration records: `70`;
- field or line matches classified: `883`;
- field-level file impacts:
  - `38` unaffected-authority records;
  - `41` mixed records requiring override;
  - `15` reference-only pending-recovery records;
  - `7` pending Step 10 records requiring revision.

The pointer/heading index preserves mixed files rather than invalidating whole records.

## Core Boundary

### Last Whole-Step Unaffected Boundary

Step 04R recovered source-visible component/semantic inventory and discrete contact evidence.

### Mixed Boundary

Step 05:

- preserved: pixel convention, panel coordinate spaces, world-axis meanings, view normals, source orientation marks, semantic IDs, and blocked physical correspondence;
- affected: the future units policy and exact-centimeter meaning assigned to labeled stations.

### First Drift Action

Step 06 front/back calibration applied:

`cm_per_px = declared_real_span_cm / pixel_span`

using the printed labels as exact premises before cross-view scale/projection coherence was proven.

## Preserved Evidence

- source identity, scanline proof, panel pixels, crop formulas, and hashes;
- printed annotation pixels, text, endpoints, and numeric values;
- printed values as approximate-target evidence;
- raw integer pixel coordinates, spans, visible row samples, landmarks, and contacts;
- recovered semantic and contact authority within existing recovery bounds;
- valid Step 05 orientation/frame fields;
- Step 09 provenance and semantic role groups without physical-pair or exact-centimeter claims;
- all existing blocked findings.

## Authoritative Recovery-Routing Supersessions

- exact printed-span calibration premises;
- centimeter-per-pixel results from Steps 06, 07, and 08R;
- derived expected/world centimeter conclusions;
- Step 09 direct-dimension authority as exact construction scale;
- pending Step 10's dimension-locked `I10-001-A` chain and dependent candidate recommendations.

Formula replay remains historical reproducibility evidence. It no longer proves that the formula premise is valid production authority.

## Approved Direction Preserved Without Production Promotion

- approximate production-target labels;
- candidate front X/Z and left Y/Z source priority;
- candidate top X/Y factor `1.1260059213` or `+12.60059213%` X relative to Y;
- candidate original-coordinate analytic transform method.

No absolute production scale, transform, corrected image, rectification, Step 10 decision, or geometry was created.

## Files Created

- `steps/CORE_REASSESSMENT_SCALE_AUTHORITY_A01_CONTRACT.md`;
- `manifests/CORE_REASSESSMENT_SCALE_AUTHORITY_A01_INPUT_INDEX.json`;
- `manifests/CORE_REASSESSMENT_SCALE_AUTHORITY_A01_AFFECTED_RECORD_INDEX.json`;
- `manifests/CORE_REASSESSMENT_SCALE_AUTHORITY_A01_CLASSIFICATION.json`;
- `manifests/CORE_REASSESSMENT_SCALE_AUTHORITY_A01_VALIDATION.json`;
- `SM_GIA_BloodAxeCairnstone_A005_CORE_REASSESSMENT_STATUS_20260716_SCALE_AUTHORITY.md`;
- `handoffs/CORE_REASSESSMENT_SCALE_AUTHORITY_A01_TO_RECOVERY_HANDOFF.md`;
- this output record.

## Files Updated

- `SM_GIA_BloodAxeCairnstone_A005_RESET_RESUME_STATE.md`;
- `SM_GIA_BloodAxeCairnstone_A005_ARTIFACT_INDEX.md`;
- `SM_GIA_BloodAxeCairnstone_A005_APPROVAL_LOG.md`;
- `docs/projects/assetforge/DRIFT_LEDGER.md`.

Only the exact contract allowlist was used.

## Artifact Status

- approved execution contract: `authoritative for execution scope only`;
- input index and validation: `proof only`;
- affected-record index, classification, status, output record, status/index/log updates, Drift Ledger entry, and handoff: `authoritative for recovery routing only`;
- existing A005 records: unchanged in place;
- A01/A02: local `proof only` and `reference only`;
- Step 10: `candidate; revision required`; no decisions approved;
- production: not started.

## Checkpoints

- before execution: `Saved/ProjectRecovery/20260716-110355/`;
- after field-level classification and before status/drift writes: `Saved/ProjectRecovery/20260716-110717/`;
- post-validation checkpoint: `Saved/ProjectRecovery/20260716-111329`.
- post-output-decision checkpoint: `Saved/ProjectRecovery/20260716-111546`.

## Output Approval Decision

Flamestrike approved this bounded reassessment result on 2026-07-16 with the statement `approved` after visible review.

The approval promotes only the field-level recovery routing and status override. It does not authorize the later recovery execution, rectification, Step 10 revision, Step 11, geometry, commit, or push.

## Next Step After Approval

After mandatory restart, prepare one separate scale-authority recovery contract. Do not execute it without a new explicit approval.
