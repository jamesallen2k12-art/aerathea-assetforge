# Step 04 Contract - Physical Component And Source-Ownership Inventory

Status: approved and executed through output review

Artifact classification: `authoritative`

Date: 2026-07-15

## Decision

Identify every visibly separate physical component or layer, assign fresh
neutral IDs, and record visible contacts, occlusions, and ambiguous boundaries
without solving them.

## Governing Core Principle

Evidence-Bound Decision Rule, closed-world authorization, and strict
evidence-versus-interpretation separation. Step 04 may inventory only what the
approved source visibly owns; it may not convert a visible layer, color change,
or ambiguous seam into inferred physical construction.

## Authorizing Plan Section

`docs/projects/assetforge/BLOODAXE_CAIRNSTONE_PIXEL_EXACT_FRESH_START_MULTISTEP_PLAN.md`,
Section 13, `Step 04 - Physical Component And Source-Ownership Inventory`.

## Approval

- Approver: Flamestrike
- Statement: `approve`
- Date: 2026-07-15
- Scope: this exact Step 04 contract only
- Exclusion: Step 04 output approval, Step 05, and every production action
  outside this contract

## Approved Inputs

- authoritative A005 governance and source-lock records;
- authoritative Step 03 crop manifest and six lossless crops;
- generic inspection and validation utilities containing no Cairn Stone
  component assumptions.

## Allowed Actions

- create the required checkpoints;
- inspect only approved A005 source inputs;
- assign fresh neutral sequential IDs such as `C-001` without preloading
  semantic names or legacy counts;
- mark only source-visible points, boundary segments, and exact contact
  segments, stopping every segment where visibility becomes ambiguous;
- classify observations as `visible`, `occluded`, or `ambiguous`, using
  `occluded` only when occlusion is directly evidenced;
- classify unsupported presence, absence, or ownership as `ambiguous`;
- create source-only evidence boards with thin marks, leader labels, and no
  fills;
- record the component inventory, source-view ownership matrix, contact-line
  inventory, and blocked unknowns;
- use perspective only for uncalibrated visual corroboration;
- create only the scoped Step 04 contract, inventory manifest, evidence
  boards, output record, validation manifest, status/index/log updates, and
  Step 04-to-Step 05 handoff;
- run focused validators;
- open all review artifacts automatically in visible desktop windows;
- after separate output approval, checkpoint, commit, and push only scoped
  Step 04 tracked outputs.

## Blocked Actions And Files

- A001-A004 asset-specific access or inherited component terminology;
- inferred component fills, masks, threshold-derived geometry, smoothed
  contours, or completed hidden boundaries;
- cross-view pixel registration, measurement formulas, calibration, centers,
  scale, or coordinate-frame decisions;
- hidden geometry, mesh planning, DCC, texture, UV, FBX, Unreal, collision,
  LOD, or production-root creation;
- Step 05 or adjacent work;
- staging or committing unrelated worktree changes.

## Expected Outputs

- `steps/STEP_04_CONTRACT.md`;
- `manifests/STEP_04_COMPONENT_OWNERSHIP_INVENTORY.json`, containing the fresh
  inventory, source-view matrix, initial contact lines, and blocked unknowns;
- A005-namespaced source-only evidence boards;
- `steps/STEP_04_OUTPUT_RECORD.md`;
- `manifests/STEP_04_VALIDATION_MANIFEST.json`;
- `handoffs/STEP_04_TO_STEP_05_HANDOFF.md`;
- scoped updates to RESET_RESUME_STATE, ARTIFACT_INDEX, and APPROVAL_LOG.

## Validators And Pass Conditions

- approved Step 03 input file identities remain unchanged;
- every ID is fresh, neutral, unique, and supported by at least one visible
  source observation;
- every evidence mark remains inside its approved crop and contains no fill;
- no boundary is extended through an occluded or ambiguous region;
- every view observation and visible contact has an explicit classification;
- every unresolved ownership question is recorded as a blocked unknown;
- perspective remains corroboration only;
- no legacy access, interpretation artifact, production root, or unrelated
  change occurs;
- focused JSON, scoped-diff, and staged-file audits;
- Flamestrike visibly approves the decomposition or marks Step 04 blocked.

## Visible Review

The untouched approved crops, source-only evidence boards, complete inventory,
source-view matrix, contact-line inventory, blocked-unknown list, and Step 04
output record must be opened automatically in visible desktop windows before
output approval.

## Artifact Status

- Technical pass before approval: inventory and records are `candidate`;
  evidence boards and validation are `proof only`.
- After separate Flamestrike output approval: approved inventory, ownership
  matrix, contact inventory, and blocked-unknown record become `authoritative`;
  evidence boards remain `proof only`.
- Output approval does not resolve blocked unknowns or authorize Step 05.
- On prohibited access or interpretation drift: affected output is
  `quarantined` and Core Recovery begins.

## Stop Conditions

Source mismatch, authority conflict, legacy access, a required boundary that
cannot be represented without inference, evidence-board fill or interpretation
drift, or any unknown that cannot be recorded honestly without inventing an
answer.

## Smallest Sufficient Change

Create one neutral source-owned inventory and the minimum unfilled evidence
boards needed to review the visible decomposition. Produce no measurement,
registration, calibration, interpretation, or production artifact.

## Context And Checkpoints

Context demand: moderate; one source-observation, evidence, validation, and
visible-review pass with no build or render loop.

Checkpoint points:

- after contract approval and before source access;
- after candidate validation and before visible review;
- after output approval and before scoped commit/push;
- after successful closeout or failure.

Pre-action checkpoint:

- `Saved/ProjectRecovery/20260715-131308/`
