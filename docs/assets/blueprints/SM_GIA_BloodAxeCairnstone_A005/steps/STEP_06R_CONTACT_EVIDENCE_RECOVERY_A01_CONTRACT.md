# Step 06R Contract - Front And Back Contact Evidence Recovery A01

Status: approved for execution

Artifact classification: `authoritative` for execution scope only

Date: 2026-07-15

## Decision

Recover only the Step 06 front/back contact evidence. Re-audit all 43 recorded
contact samples at native panel resolution, preserve supported observations,
replace unsupported observations with directly visible source-owned samples of
the same named contact, and create a recovery-suffixed candidate package.

## Governing Core Principle

Evidence-Bound Decision Rule, closed-world authorization, Core Recovery, and
strict evidence-versus-interpretation separation. Exact source pixels and the
approved semantic inventory are authority. Thresholds, inferred continuation,
and visual convenience are not authority.

## Approval

- Approver: Flamestrike
- Statement: `approved`
- Date: 2026-07-15
- Scope: `Step 06R Contact Evidence Recovery A01` exactly as presented
- Exclusion: output approval, Step 06 restoration, Step 07, Step 08, geometry,
  DCC, texture, Unreal, commit, push, and every action outside this contract

## Approved Inputs

- authoritative Step 03 front and back lossless panels and crop records;
- restored authoritative Step 05 pixel convention and coordinate frame;
- authoritative Step 04R `CL-001`, `CL-002`, and `CL-003` component-pair
  semantics;
- quarantined Step 06 front/back contact observations only as drift and
  recovery evidence;
- approved Step 05-07 dependency audit and its two exact failure diagnostics;
- A005 recovery/status records and generic native-pixel validation rules.

## Allowed Actions

- checkpoint and verify every input identity and hash;
- re-audit all 21 front and 22 back contact samples at native resolution;
- verify both source-pixel ownership and the claimed named-contact role;
- preserve supported samples and replace unsupported samples only;
- record exact panel-local and full-source integer coordinates, source RGB,
  and zero-error coordinate round trips;
- keep all contact observations discontinuous and open;
- create recovery-suffixed front/back manifests, focused validation, a
  point-only evidence board, and an output record;
- open the completed review artifact visibly.

## Scoped Writable Outputs

- this contract;
- `manifests/STEP_06_FRONT_CONTACT_EVIDENCE_RECOVERY_A01.json`;
- `manifests/STEP_06_BACK_CONTACT_EVIDENCE_RECOVERY_A01.json`;
- `manifests/STEP_06_CONTACT_EVIDENCE_RECOVERY_A01_VALIDATION.json`;
- `evidence/STEP_06_RECOVERY/SM_GIA_BloodAxeCairnstone_A005_STEP_06_FRONT_BACK_CONTACT_EVIDENCE_RECOVERY_A01.png`;
- `steps/STEP_06R_CONTACT_EVIDENCE_RECOVERY_A01_OUTPUT_RECORD.md`;
- local-only checkpoints and diagnostics under `Saved/` or `/tmp`.

## Blocked

- modifying, deleting, or restoring the original Step 06 artifacts;
- changing calibration, visible row samples, C-004 edge observations, feature
  landmarks, formulas, disagreement lists, scales, or world conversions;
- background, grid, annotation, label, dimension, or arrow pixels;
- threshold-only authority, lines, fills, masks, closure, smoothing, fitted
  shapes, inferred geometry, or hidden contacts;
- Step 07 restoration or modification; Step 08; geometry; DCC; texture; UV;
  export; Unreal; commit; or push.

## Validators

- authoritative source file and pixel hashes remain unchanged;
- all 43 recovered observations are integer-valued, in bounds, source-owned,
  and manually verified for the declared semantic contact role;
- panel-local/full-source round-trip error is `0 px`;
- the two proven background coordinates are absent from recovered samples;
- every board mark maps to one recovered manifest coordinate;
- no line interpolation, fill, closure, geometry, or interpretation exists;
- original Step 06 files remain byte-identical and quarantined;
- Step 07 and Step 08 remain unchanged and blocked;
- Flamestrike separately approves, rejects, or blocks the candidate output.

## Stop Conditions

Additional drift, semantic-role uncertainty, source or hash mismatch,
conflicting authority, need to change unaffected Step 06 data, or any required
action outside this contract.

## Artifact Status

This approved contract is `authoritative` only for execution scope. New
recovery manifests and the output record remain `candidate`; evidence and
validation remain `proof only`. Existing Step 06 artifacts remain
`quarantined`. Execution does not restore Step 06 or authorize later steps.

## Smallest Sufficient Change

Recheck all 43 contact samples, replace only unsupported contact pixels, and
produce the minimum source-bounded recovery package needed for a separate
Flamestrike decision.

## Pre-Action Checkpoint

- `Saved/ProjectRecovery/20260715-190453/`
