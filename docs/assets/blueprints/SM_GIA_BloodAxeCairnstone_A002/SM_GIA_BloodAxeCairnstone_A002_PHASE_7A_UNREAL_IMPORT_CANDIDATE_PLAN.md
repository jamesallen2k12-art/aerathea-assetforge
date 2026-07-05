# SM_GIA_BloodAxeCairnstone_A002 Phase 7A Unreal Import Candidate Plan

Status: `Unreal import candidate plan recorded; Unreal import not run`

Date: 2026-07-05

## Core Authority

- `AGENTS.md`
- `docs/projects/assetforge/AETHERFORGE_BLUEPRINTS.md`
- `docs/assets/CONCEPT_ART_TO_GAME_READY_ASSET_PIPELINE.md`
- `docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A002/SM_GIA_BloodAxeCairnstone_A002_CORE_RECONSTRUCTION_ASSET_BLUEPRINT.md`
- `docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A002/SM_GIA_BloodAxeCairnstone_A002_PHASE_6C_DCC_GAME_READY_CANDIDATE_OUTPUT_RECORD.md`

## Purpose

Define the Phase 7 Unreal import candidate plan before creating Unreal import scripts, running Unreal, modifying `.uasset` files, placing review actors, validating maps, or capturing review images.

This plan does not import anything into Unreal, create materials, edit maps, run validation, or request subjective visual approval.

## Authorized Phase 7 Goal

Create an Unreal import candidate from the passed A002 DCC game-ready candidate.

The future Phase 7 candidate must include:

- Static Mesh import.
- LOD0-LOD3 setup.
- simple collision setup from the DCC UCX proxy source.
- material and texture assignment.
- review-map placement.
- validation report.
- offscreen review capture only after validation.

The asset may become `Unreal import candidate` only after a future Unreal import, placement, validation, and capture pass.

It must not be called `Fully game-ready` until Unreal validation, final asset blueprint archive, and Flamestrike final approval are complete.

## Approved Inputs

Phase 7 may use these A002 records and outputs:

- Phase 6C output record:
  `docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A002/SM_GIA_BloodAxeCairnstone_A002_PHASE_6C_DCC_GAME_READY_CANDIDATE_OUTPUT_RECORD.md`
- DCC handoff:
  `Saved/Automation/DCC/SM_GIA_BloodAxeCairnstone_A002/DCCGameReadyA01/SM_GIA_BloodAxeCairnstone_A002_DCCGameReadyA01Handoff.md`
- DCC manifest:
  `Saved/Automation/DCC/SM_GIA_BloodAxeCairnstone_A002/DCCGameReadyA01/SM_GIA_BloodAxeCairnstone_A002_DCCGameReadyA01Manifest.json`
- DCC audit:
  `Saved/Automation/DCC/SM_GIA_BloodAxeCairnstone_A002/DCCGameReadyA01/SM_GIA_BloodAxeCairnstone_A002_DCCGameReadyA01Audit.json`

Required source FBX files:

- `SourceAssets/Exports/Props/Giants/BloodAxe/Cairns/SM_GIA_BloodAxeCairnstone_A002_DCCGameReady_A01/SM_GIA_BloodAxeCairnstone_A002_DCCGameReady_A01.fbx`
- `SourceAssets/Exports/Props/Giants/BloodAxe/Cairns/SM_GIA_BloodAxeCairnstone_A002_DCCGameReady_A01/SM_GIA_BloodAxeCairnstone_A002_DCCGameReady_A01_LOD0.fbx`
- `SourceAssets/Exports/Props/Giants/BloodAxe/Cairns/SM_GIA_BloodAxeCairnstone_A002_DCCGameReady_A01/SM_GIA_BloodAxeCairnstone_A002_DCCGameReady_A01_LOD1.fbx`
- `SourceAssets/Exports/Props/Giants/BloodAxe/Cairns/SM_GIA_BloodAxeCairnstone_A002_DCCGameReady_A01/SM_GIA_BloodAxeCairnstone_A002_DCCGameReady_A01_LOD2.fbx`
- `SourceAssets/Exports/Props/Giants/BloodAxe/Cairns/SM_GIA_BloodAxeCairnstone_A002_DCCGameReady_A01/SM_GIA_BloodAxeCairnstone_A002_DCCGameReady_A01_LOD3.fbx`
- `SourceAssets/Exports/Props/Giants/BloodAxe/Cairns/SM_GIA_BloodAxeCairnstone_A002_DCCGameReady_A01/SM_GIA_BloodAxeCairnstone_A002_DCCGameReady_A01_UCX.fbx`

Approved source texture authority:

- `docs/assets/reference/bloodaxe_cairnstone_asset/REF_GIA_BloodAxeCairnstoneAsset_A02_BlueprintTemplate.png`

Phase 7 must not use A001 or A02 generated meshes, textures, materials, exports, or Unreal assets as source authority.

## Planned Unreal Content Paths

Static Mesh destination:

- `/Game/Aerathea/Props/Giants/BloodAxe/Cairns/SM_GIA_BloodAxeCairnstone_A002`

Texture destination:

- `/Game/Aerathea/Textures/Giants/BloodAxe/Cairns/SM_GIA_BloodAxeCairnstone_A002`

Planned texture asset:

- `/Game/Aerathea/Textures/Giants/BloodAxe/Cairns/SM_GIA_BloodAxeCairnstone_A002/T_GIA_BloodAxeCairnstone_A002_SourceTemplate_BC`

Material destination:

- `/Game/Aerathea/Materials/Giants/BloodAxe/Cairns`

Planned parent materials:

- `/Game/Aerathea/Materials/Giants/BloodAxe/Cairns/M_GIA_BloodAxeCairnstone_A002_SourceTemplate`
- `/Game/Aerathea/Materials/Giants/BloodAxe/Cairns/M_GIA_BloodAxeCairnstone_A002_InferredHidden`

Planned material instances:

- `/Game/Aerathea/Materials/Instances/MI_GIA_BloodAxeCairnstone_A002_SourceTemplate`
- `/Game/Aerathea/Materials/Instances/MI_GIA_BloodAxeCairnstone_A002_InferredHidden`

Review actor label:

- `AET_PROD_GIA_BloodAxeCairnstone_A002`

Review map target:

- `/Game/Aerathea/Maps/L_Aerathea_Startup`

## Import Rules

Static Mesh import must:

- import the DCC game-ready FBX as `SM_GIA_BloodAxeCairnstone_A002`
- use centimeters without rescale
- preserve `Z` up, `-Y` front, `+X` right
- import or assign LOD0-LOD3
- assign simple collision only
- avoid complex-as-simple collision
- assign the planned material instances to the two DCC material slots
- write metadata recording A002 source records and current status

If separate UCX FBX binding is not supported by the import script, the future script may create equivalent simple box collision from the DCC UCX source and must record that fallback. It may not enable complex-as-simple collision.

## Material And Texture Rules

The approved source template may be imported as the Base Color texture source without editing source pixels.

Material slots must map:

- `M_A002_SourceTemplate_Closest` to `MI_GIA_BloodAxeCairnstone_A002_SourceTemplate`
- `M_A002_TaggedInferredHidden_Neutral` to `MI_GIA_BloodAxeCairnstone_A002_InferredHidden`

Normal and ORM maps are planned-but-not-authored for the first Unreal import candidate unless a later exact-map package is approved and audited.

No emissive map is planned.

## Placement Plan

Future placement may use a Static Mesh Actor in `L_Aerathea_Startup` for technical review.

Initial review placement target:

- location: `(12480.0, 10360.0, 0.0)`
- yaw: `-18.0`
- scale: `(1.0, 1.0, 1.0)`

The placement script must tag the actor with:

- `AET_FIRST_SLICE`
- `AET_BLOODAXE_CAIRNSTONE_A002_REVIEW`
- `AET_STATIC_REVIEW_TARGET`

The placement is a technical review placement, not final world placement.

## Planned Scripts

Future Phase 7B script creation should create:

- `Tools/Unreal/import_bloodaxe_cairnstone_a002.py`
- `Tools/Unreal/place_bloodaxe_cairnstone_a002_startup_review.py`
- `Tools/Unreal/validate_bloodaxe_cairnstone_a002.py`

Phase 7B script creation must not run Unreal.

## Validation Requirements

The future validator must verify:

- source FBX files exist and are non-empty
- DCC manifest and audit exist
- DCC audit status is `pass`
- imported Static Mesh exists
- imported mesh has at least 4 LODs
- simple collision exists
- complex-as-simple is not used
- material instances exist
- material instances are assigned to the mesh
- source texture asset exists and references the approved source template import
- mesh metadata records A002 source, DCC package, and `Unreal import candidate` status
- startup review actor exists after placement
- actor location, yaw, scale, tags, material assignment, and collision state match the plan
- no A001/A02 generated source authority is recorded
- final visual approval remains pending
- fully game-ready status is not claimed

## Review Capture Requirements

After import, placement, and validation pass, use:

- `Tools/Unreal/capture_startup_review_offscreen.sh`

Do not use visible `-game` capture windows unless Flamestrike explicitly asks.

Before presenting any Unreal visual approval, compare the live Unreal capture against the approved source/canon and DCC proof orientation. If the view is clipped, side-on, underside-facing, proxy-only, or scale-mismatched, it is not ready for presentation.

## Blocked Methods

Phase 7A does not authorize:

- Unreal import
- `.uasset` creation
- map edits
- material asset creation
- texture asset creation
- validation command execution
- review capture
- runtime mesh merge
- source-image pixel edits
- A001 or A02 generated texture/material authority
- subjective visual approval request
- fully game-ready claim

## Phase 7A Decision

Decision: `plan_complete`

Phase 7A is sufficient to proceed to Unreal import/placement/validation script creation, but no Unreal work has been run.

## Next Core-Valid Step

Begin A002 Phase 7B: Unreal Import Candidate Script Creation.

The next task is to create the A002-owned Unreal import, placement, and validation scripts from this plan, without running Unreal.
