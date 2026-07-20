# A005 Source-Versus-Measurement Reconciliation Contract A01

Status: `candidate contract; preparation approved; execution not approved`

Artifact classification: `candidate`

Contract ID: `A005-CR-SMR-A01`

Date: 2026-07-17

## Plain-English Purpose

The drawings and the requested measurements do not have the same proportions.
Flamestrike has chosen the following direction for the next proposed test:

- keep the requested measurements as the final intended sizes;
- preserve the appearance of the drawings as closely as possible;
- allow only the smallest component adjustments needed to meet the sizes;
- show and record every adjustment before any 3D work.

This contract proposes how to make that test safely. It does not perform the
test, change a drawing, revise Step 10, or create a 3D model.

## Preparation Authority

On 2026-07-17, Flamestrike approved preparation of this short reconciliation
contract after the A01 scale-authority result was recorded as blocked.

That approval authorizes only this contract file, its validation, and visible
presentation. Execution requires a separate explicit approval of this exact
contract.

## One Decision

Create a clearly labelled 2D interpretation proposal that answers:

> Can the approved final measurements be honored with small, controlled
> component adjustments while keeping the original drawings untouched and
> preserving their overall visual character?

Possible output decisions:

- `approve bounded reconciliation rules`;
- `reject bounded reconciliation rules`;
- `blocked because the required adjustment is too large or unclear`.

None of those decisions creates geometry authority by itself.

## Controlling Authority

- `AGENTS.md` and Core;
- `docs/projects/assetforge/BLOODAXE_CAIRNSTONE_PIXEL_EXACT_FRESH_START_MULTISTEP_PLAN.md`, especially Step 10's interpretation rules;
- `steps/SCALE_AUTHORITY_RECOVERY_A01_CONTRACT.md`;
- `manifests/SCALE_AUTHORITY_RECOVERY_A01_PHYSICAL_BOUNDS.json`;
- `manifests/SCALE_AUTHORITY_RECOVERY_A01_DISTORTION_HOLDOUT.json`;
- `manifests/SCALE_AUTHORITY_RECOVERY_A01_WORLD_INTEGRATION_OVERRIDE.json`;
- `steps/SCALE_AUTHORITY_RECOVERY_A01_OUTPUT_RECORD.md`;
- `handoffs/SCALE_AUTHORITY_RECOVERY_A01_TO_STEP10_REVISION_HANDOFF.md`;
- `SM_GIA_BloodAxeCairnstone_A005_RESET_RESUME_STATE.md`;
- Flamestrike's 2026-07-17 approval to prepare this contract.

## Starting State

- Original source drawings and Step 03 panels remain unchanged.
- The drawings remain visual evidence.
- The six requested sizes remain approved physical-target intent.
- Scale-Authority Recovery A01 found `10` source/target proportion conflicts.
- A single transform applied to each whole drawing cannot resolve them.
- No world-space construction frame was recovered.
- Step 10 revision, Step 11, interpretation execution, geometry, and production
  are stopped.

## Measurements That Must Be Preserved

If execution is later approved, the interpretation proposal must use:

| Object | Final intended measurement |
|---|---:|
| Complete asset height | `220 cm` |
| C-001 maximum width | `120 cm` |
| C-001 maximum depth | `90 cm` |
| C-004 maximum footprint width | `140 cm` |
| C-004 maximum footprint depth | `110 cm` |
| C-004 base height | `35 cm` |

These measurements control final intended size. They do not turn the printed
labels into exact historical pixel rulers and do not authorize editing the
source images.

## Source-View Roles

- Front supplies the primary visible X/Z silhouette and detail placement.
- Left supplies the primary visible Y/Z silhouette and detail placement.
- The physical `220 cm` and `35 cm` targets control the two specified absolute
  Z dimensions where the front and left source proportions disagree.
- Back and right are validation views and retain only non-conflicting visible
  details.
- Top supplies non-conflicting visible plan-shape character. The `120/90 cm`
  C-001 and `140/110 cm` C-004 targets control the specified X/Y extents.
- The previous top factor `1.1260059213` remains review evidence only. It cannot
  become a geometry scale or silently override the physical targets.

## Meaning Of “Limited Adjustment”

The original source pixels may never be changed.

Any proposed adjustment must appear only in a separate interpretation diagram
and must obey all of these rules:

1. Adjust only what is necessary to meet the six listed measurements.
2. C-001 may receive one axis-aligned component-scale proposal in X and one in
   Y. Its visible shape character and internal feature order must be retained.
3. C-004 may receive one axis-aligned component-scale proposal in X, Y, and Z.
   Its visible shape character and internal feature order must be retained.
4. The complete interpreted assembly may receive one global Z scale to set the
   `220 cm` overall height before the separate C-004 `35 cm` height is checked.
5. C-002 and C-003 may be translated rigidly only when necessary to preserve an
   already approved visible contact relationship. They may not be stretched,
   reshaped, smoothed, or redesigned in this pass.
6. No component may be rotated unless a later, separately approved rule names
   the exact angle and reason. Rotation is not proposed by this contract.
7. No freeform, cage, lattice, spline, perspective, row, feature, or
   content-aware warp is permitted.
8. No discretionary cleanup, symmetry correction, stylization, silhouette
   improvement, or new design detail is permitted.
9. Every moved source-owned point or boundary segment used in the proposal must
   retain its original coordinate, proposed target coordinate, movement amount,
   component ID, axis, reason, and controlling measurement.
10. Any source-owned region not required to move must be shown as unchanged.

These are interpretation rules for a review proposal only. They do not approve
the proposed adjusted shapes in advance.

## Evidence And Interpretation Separation

The future review board must show separate, unmistakably labelled areas:

- `ORIGINAL SOURCE EVIDENCE - UNCHANGED`;
- `MEASUREMENT TARGET FRAME`;
- `INTERPRETATION PROPOSAL - NOT GEOMETRY`;
- `DIFFERENCE / MOVEMENT AUDIT`;
- `BLOCKED OR UNKNOWN`.

Source pixels and interpretation marks may be shown side by side. An
interpretation overlay may be used only when its color, label, legend, and
artifact status make it impossible to mistake for source evidence.

No inferred hidden surface, filled contact, closed unseen contour, physical
center, origin, pivot, snap anchor, topology, or 3D form may be added.

## Proposed Execution Outputs

Execution, if separately approved, may create only:

- `manifests/SOURCE_VS_MEASUREMENT_RECONCILIATION_A01_INPUT_LOCK.json`;
- `manifests/SOURCE_VS_MEASUREMENT_RECONCILIATION_A01_RULES.json`;
- `manifests/SOURCE_VS_MEASUREMENT_RECONCILIATION_A01_ADJUSTMENT_LEDGER.json`;
- `manifests/SOURCE_VS_MEASUREMENT_RECONCILIATION_A01_VALIDATION.json`;
- `evidence/SOURCE_VS_MEASUREMENT_RECONCILIATION_A01/SM_GIA_BloodAxeCairnstone_A005_SOURCE_VS_MEASUREMENT_RECONCILIATION_A01_REVIEW_BOARD.png`;
- `steps/SOURCE_VS_MEASUREMENT_RECONCILIATION_A01_OUTPUT_RECORD.md`;
- `handoffs/SOURCE_VS_MEASUREMENT_RECONCILIATION_A01_TO_STEP10_REVISION_HANDOFF.md`.

A local-only working directory may be used at:

`Saved/AssetForgeResearch/A005_SourceVsMeasurementReconciliation_A01/`.

No other tracked path may be created or changed during execution. After a
visible output decision, the reset/resume state, artifact index, and approval
log may be updated only to record that decision.

## Required Adjustment Ledger

The ledger must record, for every proposed change:

- component ID;
- source view and source record;
- source-owned point, span, or visible boundary segment;
- original coordinate or exact source span;
- target coordinate or intended physical span;
- transform type;
- X, Y, and Z change as applicable;
- absolute and percentage change;
- controlling measurement;
- visible contact affected, if any;
- unchanged internal-order check;
- source-versus-interpretation classification;
- permitted future consumer;
- blocked consumer.

No mean, convenient average, hand-tuned correction, or unlogged adjustment may
enter the proposal.

## Validation Requirements

Validation must prove:

- every input used was allowed and hash-locked before output writes;
- original source and all Step 03 panel hashes remain unchanged;
- no existing Step 01-Step 10 record changed;
- all six intended measurements appear exactly and retain their component/axis
  roles;
- every proposed adjustment is present in the ledger;
- only C-001 and C-004 receive the permitted axis-aligned component scales;
- C-002 and C-003 receive at most a logged rigid translation;
- no rotation or forbidden warp exists;
- source and interpretation are visibly separated;
- the complete proposal reports maximum, median, and per-component movement;
- front/left ownership and back/right validation roles are obeyed;
- top review evidence is not promoted to geometry authority;
- no hidden surface, filled unknown, center, pivot, topology, or geometry was
  created;
- only allowlisted paths changed;
- the review board opens visibly;
- Step 10 revision, Step 11, and production remain stopped.

No automatic visual pass threshold may be invented. Flamestrike decides
whether the visible adjustment is acceptable.

## Stop Conditions

Stop and report `blocked` if:

- a required component or boundary cannot be traced to approved evidence;
- the six measurements cannot all be met under the listed adjustment rules;
- C-002 or C-003 would need reshaping rather than rigid translation;
- an approved visible contact cannot be preserved without an unapproved
  deformation;
- a hidden contour or surface would have to be invented;
- the source and interpretation cannot be shown separately and clearly;
- any change would fall outside the allowed files;
- execution begins deciding Step 10 geometry unknowns rather than preparing
  the bounded reconciliation proposal.

On a stop, preserve valid diagnostics as `proof only`, create a checkpoint,
write the exact blocker, and do not repair forward.

## Explicitly Blocked Work

- editing, repainting, resampling, or replacing original source panels;
- treating an interpretation diagram as corrected source evidence;
- changing any of the six measurements;
- unlogged local or feature-level reshaping;
- selecting a center, origin, pivot, snap anchor, topology, or hidden fill;
- revising or approving the existing Step 10 records;
- beginning Step 11;
- Blender, geometry, FBX, UV, texture, material, collision, LOD, Unreal, or
  performance work;
- generic Core, pipeline, blueprint, or plan changes;
- commit or push.

## Artifact Status Before Output Approval

- This contract after execution approval: `authoritative for execution scope
  only`.
- Input lock and validation: `proof only`.
- Interpretation board: `proof only candidate interpretation`; never source or
  geometry authority.
- Rules, adjustment ledger, output record, and handoff: `candidate`.
- Current A005 authority and stop state: unchanged.

## Smallest Sufficient Change

Prepare one visibly reviewable, fully logged 2D reconciliation proposal. Stop
before Step 10 revision or 3D work.

## Planned Checkpoints

1. before any execution output path opens;
2. after the input lock and rule record;
3. after the interpretation board and adjustment ledger;
4. after validation, before visible review;
5. after Flamestrike's output decision, before any separately approved
   closeout.

## Plain-English Execution Approval Question

Do you approve creating a review proposal that:

- keeps the six measurements fixed;
- leaves every original drawing untouched;
- allows only whole-component X/Y/Z size adjustments to C-001 and C-004;
- allows C-002 and C-003 to move without changing shape only when necessary to
  preserve an approved visible contact;
- shows the original and proposed result separately;
- lists every adjustment and how large it is;
- stops for your visual decision before Step 10 or any 3D work?

Approval of this contract would authorize the review proposal only. It would
not approve the proposed adjusted shapes, Step 10, or geometry in advance.
