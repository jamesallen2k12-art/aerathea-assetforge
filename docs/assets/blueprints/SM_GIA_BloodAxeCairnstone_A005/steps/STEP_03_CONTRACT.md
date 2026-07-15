# Step 03 Contract - Exact Panel Decomposition

Status: approved and executed through candidate output review

Artifact classification: `authoritative`

Date: 2026-07-15

## Decision

Lock lossless full-source crop formulas for the perspective, front, back, left,
right, and top panels while excluding borders and unrelated annotations from
panel ownership.

## Governing Core Principle

Evidence-Bound Decision Rule, closed-world authorization, and strict
evidence-versus-interpretation separation. Step 03 may establish exact source
ownership only; it may not introduce a component or production solution.

## Authorizing Plan Section

`docs/projects/assetforge/BLOODAXE_CAIRNSTONE_PIXEL_EXACT_FRESH_START_MULTISTEP_PLAN.md`,
Section 13, `Step 03 - Exact Panel Decomposition`.

## Approval

- Approver: Flamestrike
- Statement: `approved`
- Date: 2026-07-15
- Scope: this exact Step 03 contract only
- Exclusion: Step 03 output approval, Step 04, and every production action
  outside this contract

## Approved Inputs

- current authoritative A005 governance and Step 02 records;
- the authoritative A02 source PNG;
- its authoritative scanline manifest and explicitly contained proof files;
- generic lossless cropping, hashing, and validation utilities containing no
  Cairn Stone constants.

## Allowed Actions

- create the required checkpoints;
- verify authoritative source identity before extraction;
- declare integer, half-open crop coordinates `(x0, y0, x1, y1)`;
- extract the six panels losslessly with no scaling, filtering, rotation, or
  color transformation;
- create source-only boundary evidence showing source pixels, exact boundary
  lines, panel names, and declared coordinates;
- compare every extracted panel pixel-for-pixel with its corresponding source
  region;
- create only the scoped Step 03 contract, panel images, panel manifest,
  evidence board, output record, validation manifest, status/index/log
  updates, and Step 03-to-Step 04 handoff;
- run focused validators;
- open all review artifacts automatically in visible desktop windows;
- after separate output approval, checkpoint, commit, and push only the scoped
  Step 03 tracked outputs.

## Blocked Actions And Files

- component masks, identities, or component measurements;
- candidate fills, inferred contours, smoothing, or silhouette cleanup;
- removing annotations or altering pixels inside an actual crop;
- physical-dimension or perspective calibration;
- cross-view correspondence or hidden-surface interpretation;
- geometry, DCC, texture synthesis, UV, FBX, Unreal, collision, LOD, or
  performance work;
- every A001-A004 asset-specific artifact, script, manifest, coordinate, and
  output;
- A005 production-root creation;
- Step 04 or adjacent work;
- staging or committing unrelated worktree changes.

## Expected Outputs

- `steps/STEP_03_CONTRACT.md`;
- `manifests/STEP_03_PANEL_CROP_MANIFEST.json`;
- six A005-namespaced lossless panel PNGs;
- source-only crop-boundary evidence board;
- `steps/STEP_03_OUTPUT_RECORD.md`;
- `manifests/STEP_03_VALIDATION_MANIFEST.json`;
- `handoffs/STEP_03_TO_STEP_04_HANDOFF.md`;
- scoped updates to RESET_RESUME_STATE, ARTIFACT_INDEX, and APPROVAL_LOG.

## Validators And Pass Conditions

- source file and decoded-pixel hashes still match Step 02 authority;
- exactly six named panel records exist;
- every crop uses valid integer half-open coordinates within `1055 x 1491`;
- each panel measures exactly `(x1 - x0) x (y1 - y0)`;
- each decoded panel equals its direct source-region extraction with
  `changed_pixels = 0`, `max_rgb_delta = 0`, and matching decoded-pixel
  hashes;
- no scaling, filtering, rotation, cleanup, recoloring, or annotation removal;
- evidence board contains no candidate fill or inferred solution;
- perspective is classified as visual corroboration unless separately
  calibrated;
- no legacy asset-specific data access, production-root creation, or unrelated
  change;
- focused JSON, scoped diff, and staged-file audits;
- Flamestrike visibly approves all six boundaries as source ownership.

## Visible Review

The untouched source, source-only boundary board, all six lossless crops, and
Step 03 output record must be opened automatically in visible desktop windows
before output approval.

## Artifact Status

- Technical pass before approval: panel manifest and crops are `candidate`;
  validation and boundary evidence are `proof only`.
- After Flamestrike output approval: crop formulas and lossless panel crops
  become `authoritative`; the boundary board remains `proof only`.
- Perspective remains visual corroboration unless separately calibrated.
- On ambiguity or validation failure: Step 03 is `blocked`.
- On prohibited access or interpretation drift: affected output is
  `quarantined` and Core Recovery begins.

## Stop Conditions

Source hash mismatch, ambiguous boundary requiring interpretation, unavoidable
annotation editing, required resampling, legacy access, unexpected A005 path
overlap, authority conflict, or failed exact-pixel comparison.

## Smallest Sufficient Change

Create and validate only six source-owned lossless panel crops, their exact
half-open coordinate manifest, and one source-only boundary board. Produce no
component, measurement, calibration, interpretation, or production artifact.

## Context And Checkpoints

Context demand: moderate; one exact extraction, validation, and visible-review
pass with no build or render loop.

Checkpoint points:

- after contract approval and before source access;
- after candidate validation and before visible review;
- after output approval and before scoped commit/push;
- after successful closeout or failure.
