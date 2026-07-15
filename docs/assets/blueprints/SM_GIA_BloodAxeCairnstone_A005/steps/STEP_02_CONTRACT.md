# Step 02 Contract - Source Authority And Scanline Lock

Status: approved and executed through candidate output review

Artifact classification: `authoritative`

Date: 2026-07-15

## Decision

Prove whether the confirmed A02 source and its scanline record are intact,
pixel-exact, and the sole asset-specific source authority for A005.

## Governing Core Principle

Evidence-Bound Decision Rule and closed-world authorization. Exact source
evidence must be proven before measurement or interpretation begins.

## Authorizing Plan Section

`docs/projects/assetforge/BLOODAXE_CAIRNSTONE_PIXEL_EXACT_FRESH_START_MULTISTEP_PLAN.md`,
Section 13, `Step 02 - Source Authority And Scanline Lock`.

## Approval

- Approver: Flamestrike
- Statement: `approved`
- Date: 2026-07-15
- Scope: this exact Step 02 contract only
- Exclusion: candidate output approval, Step 03, and every production action

## Approved Inputs

- current authoritative A005 governance records;
- the exact confirmed A02 source path;
- the exact A02 scanline-manifest path;
- proof files explicitly referenced by that manifest, provided every resolved
  path remains within its exact `ScanlineCapture` directory;
- generic non-asset-specific hashing and image-verification utilities.

## Allowed Actions

- create required checkpoints;
- perform non-mutating source, manifest, path, file, and pixel inspection;
- perform a fresh in-memory scanline reconstruction;
- create only the Step 02 authority, validation, output, status, index,
  approval-log, and handoff records;
- run focused validators;
- open the source and approval records in visible desktop windows;
- after separate output approval, checkpoint, commit, and push only the scoped
  Step 02 tracked records.

## Blocked Actions And Files

- modifying, copying, cleaning, recoloring, resizing, or resampling the source;
- panel extraction, crops, masks, coordinates, component measurements, or
  formulas;
- filled overlays, inferred contours, hidden-surface interpretation, geometry,
  texture, FBX, Unreal, collision, LOD, or performance work;
- all A001-A004 asset-specific artifacts, scripts, manifests, and outputs;
- A005 production-root creation;
- Step 03;
- staging or committing unrelated worktree changes.

## Expected Outputs

- `SM_GIA_BloodAxeCairnstone_A005_SOURCE_AUTHORITY_LOCK.md`;
- `steps/STEP_02_CONTRACT.md`;
- `steps/STEP_02_OUTPUT_RECORD.md`;
- `manifests/STEP_02_VALIDATION_MANIFEST.json`;
- `handoffs/STEP_02_TO_STEP_03_HANDOFF.md`;
- scoped updates to RESET_RESUME_STATE, ARTIFACT_INDEX, and APPROVAL_LOG.

## Validators And Pass Conditions

- expected source file hash, decoded pixel hash, dimensions, format, and mode;
- valid contained manifest paths;
- valid scan-record signature, metadata, and all sequential row indices;
- target, scan, stored rebuild, and fresh rebuild pixel hashes match;
- `changed_pixels = 0`;
- `max_rgb_delta = 0`;
- `pixel_exact = true`;
- difference image contains only zero RGB values;
- no legacy asset-specific input access;
- no source mutation or A005 production-root creation;
- focused JSON, scoped diff, and staged-file audits.

## Visible Review

The untouched source image and Step 02 source-lock/output records must be
opened automatically in visible desktop windows before output approval.

## Artifact Status

- Technical pass before approval: source-lock package is `candidate` and the
  validation manifest is `proof only`.
- After Flamestrike output approval: source and scanline evidence become
  `authoritative`.
- On verification failure: no promotion; Step 02 is `blocked`.
- On prohibited access or drift: affected output is `quarantined` and Core
  Recovery begins.

## Stop Conditions

Missing inputs, hash or metadata mismatch, nonzero pixel difference, malformed
or escaping paths, source mutation, legacy access, unexpected A005 overlap,
required interpretation, or authority conflict.

## Smallest Sufficient Change

Verify the existing source and scanline evidence and record the authority
decision. Produce no image transformation or production artifact.

## Context And Checkpoints

Context demand: low to moderate; one read-only verification and documentation
pass with no build or render loop.

Checkpoint points:

- after contract approval and before source access;
- after candidate validation and before visible review;
- after output approval and before scoped commit/push;
- after successful closeout or failure.
