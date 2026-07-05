# SM_GIA_BloodAxeCairnstone_A002 Phase 7B Unreal Import Script Record

Status: `Unreal import candidate scripts created; Unreal not run`

Date: 2026-07-05

## Core Authority

- `AGENTS.md`
- `docs/projects/assetforge/AETHERFORGE_BLUEPRINTS.md`
- `docs/assets/CONCEPT_ART_TO_GAME_READY_ASSET_PIPELINE.md`
- `docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A002/SM_GIA_BloodAxeCairnstone_A002_CORE_RECONSTRUCTION_ASSET_BLUEPRINT.md`
- `docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A002/SM_GIA_BloodAxeCairnstone_A002_PHASE_6C_DCC_GAME_READY_CANDIDATE_OUTPUT_RECORD.md`
- `docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A002/SM_GIA_BloodAxeCairnstone_A002_PHASE_7A_UNREAL_IMPORT_CANDIDATE_PLAN.md`

## Purpose

Create A002-owned Unreal import, startup review placement, and validation scripts before running Unreal.

This record does not import `.uasset` content, create Unreal materials, edit maps, run validation inside Unreal, capture review images, request subjective visual approval, or claim `Fully game-ready`.

## Created Scripts

Import script:

- `Tools/Unreal/import_bloodaxe_cairnstone_a002.py`

Startup review placement script:

- `Tools/Unreal/place_bloodaxe_cairnstone_a002_startup_review.py`

Validation script:

- `Tools/Unreal/validate_bloodaxe_cairnstone_a002.py`

## Script Scope

The scripts are limited to the approved Phase 7A candidate:

- Static Mesh package: `SM_GIA_BloodAxeCairnstone_A002`
- Source DCC package: `SM_GIA_BloodAxeCairnstone_A002_DCCGameReady_A01`
- Review actor label: `AET_PROD_GIA_BloodAxeCairnstone_A002`
- Review map: `/Game/Aerathea/Maps/L_Aerathea_Startup`

The import script is prepared to:

- verify the Phase 6C DCC manifest and audit before import
- require the Phase 6C audit status to be `pass`
- import the Phase 6C DCC game-ready FBX as an Unreal Static Mesh candidate
- import or set up LOD0-LOD3
- create simple collision without complex-as-simple collision
- record the simple-collision fallback as DCC UCX-source-verified metadata
- import the approved A002 source template as the Base Color texture source
- create A002-owned parent materials and material instances
- assign source-template and inferred-hidden material instances by DCC material-slot name
- write metadata preserving A002 source, package, collision, approval, and non-final status

The placement script is prepared to:

- load `/Game/Aerathea/Maps/L_Aerathea_Startup`
- create or update `AET_PROD_GIA_BloodAxeCairnstone_A002`
- place it at `(12480.0, 10360.0, 0.0)`
- set yaw to `-18.0`
- tag it for technical startup review
- keep final visual approval pending

The validation script is prepared to verify:

- all Phase 6C source files exist and are non-empty
- DCC manifest and audit sources exist
- DCC audit status is `pass`
- DCC manifest records three UCX collision proxies
- imported texture, material instances, mesh, LODs, simple collision, metadata, actor placement, tags, and collision state are present
- collision metadata records the fallback source, UCX FBX source path, expected proxy count, imported collision count, and no complex-as-simple claim
- no metadata claims `Fully game-ready`

## Blocked Outputs

Phase 7B scripts are not authorized to create:

- Unreal `.uasset` output
- map edits
- imported Static Mesh content
- material or texture assets
- validation reports from a live Unreal run
- review captures
- runtime mesh merge
- source-image pixel edits
- A001 or A02 generated source authority
- final visual approval
- `Fully game-ready` status

## Validation

Python syntax validation completed:

- `python3 -m py_compile Tools/Unreal/import_bloodaxe_cairnstone_a002.py Tools/Unreal/place_bloodaxe_cairnstone_a002_startup_review.py Tools/Unreal/validate_bloodaxe_cairnstone_a002.py`

Result:

- `pass`

Scoped whitespace/diff validation completed:

- `git diff --check -- Tools/Unreal/import_bloodaxe_cairnstone_a002.py Tools/Unreal/place_bloodaxe_cairnstone_a002_startup_review.py Tools/Unreal/validate_bloodaxe_cairnstone_a002.py docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A002/SM_GIA_BloodAxeCairnstone_A002_PHASE_7A_UNREAL_IMPORT_CANDIDATE_PLAN.md`

Result:

- `pass`

## Artifact Status

The Phase 7B scripts are `candidate` support artifacts.

They are not authoritative Unreal output until a future Phase 7C run completes, validates, and is recorded.

## Phase 7B Decision

Decision: `scripts_created`

Phase 7B is complete as a script-preparation step. Unreal has not been run, no `.uasset` files have been created, and no startup map placement has been changed by this step.

## Next Core-Valid Step

Begin A002 Phase 7C: Unreal Import Candidate Run.

The next task is to create a manual checkpoint, run the Phase 7B Unreal import script, run the startup review placement script, run the validator, and record the output only if validation passes.
