# AET-MA-20260629-578 Startup Review Task Packet

## Task ID

`AET-MA-20260629-579`

## Goal

Place the first-pass visually approved `SM_GIA_BloodAxeMovedCampLowCairnRemnant_A01` as a startup review actor and validate the placement without adding gameplay behavior.

## Assigned Agent

Unreal Implementation + QA / Validation

## Allowed Files

- `Tools/Unreal/place_bloodaxe_moved_camp_low_cairn_remnant_startup_review.py`
- `Tools/Unreal/validate_bloodaxe_moved_camp_low_cairn_remnant_startup_review.py`
- `Tools/Unreal/validate_bloodaxe_moved_camp_low_cairn_remnant.py`
- `Content/Aerathea/Maps/L_Aerathea_Startup.umap`
- `Content/Aerathea/Props/Giants/BloodAxe/MovedCamp/SM_GIA_BloodAxeMovedCampLowCairnRemnant_A01.uasset`
- `docs/assets/props/SM_GIA_BloodAxeMovedCampLowCairnRemnant_A01/BUILD_IMPORT_STATUS.md`
- `docs/agents/AET-MA-20260629-579_VALIDATION_SUMMARY.md`
- `docs/agents/AGENT_TASK_BOARD.md`

## Blocked Files

- unrelated `Content/Aerathea/` assets
- `SourceAssets/`
- `Tools/DCC/`
- runtime source
- gameplay Blueprints/classes
- collision gameplay setup
- VFX/audio assets
- authored BC/N/ORM texture assets
- source concept folders outside the repo
- Hermes files or configuration

## Dependencies

- `AET-MA-20260629-577`
- `AET-MA-20260629-574` Unreal import evidence
- `AET-MA-20260629-575` QA evidence
- current `BUILD_IMPORT_STATUS.md`

## Approval Gate

First-pass visual/readability approval is resolved by `AET-MA-20260629-577`.

Do not claim final shipped startup composition, final visual art, final collision, runtime behavior, gameplay behavior, combat feel, playstyle, economy/backend direction, VFX/audio, or next implementation target selection.

## Required Validators

- `python -m py_compile Tools/Unreal/place_bloodaxe_moved_camp_low_cairn_remnant_startup_review.py Tools/Unreal/validate_bloodaxe_moved_camp_low_cairn_remnant_startup_review.py Tools/Unreal/validate_bloodaxe_moved_camp_low_cairn_remnant.py`
- `UnrealEditor-Cmd ... -ExecutePythonScript=Tools/Unreal/place_bloodaxe_moved_camp_low_cairn_remnant_startup_review.py`
- `UnrealEditor-Cmd ... -ExecutePythonScript=Tools/Unreal/validate_bloodaxe_moved_camp_low_cairn_remnant.py`
- `UnrealEditor-Cmd ... -ExecutePythonScript=Tools/Unreal/validate_bloodaxe_moved_camp_low_cairn_remnant_startup_review.py`
- `UnrealEditor-Cmd ... -ExecutePythonScript=Tools/Unreal/validate_startup_scene.py`
- `python Tools/Agents/validate_agent_workflow.py` if board changes
- `git diff --check`
- ASCII and trailing-whitespace scans for changed text files

## Expected Deliverables

- Startup review actor: `AET_PROD_GIA_BloodAxeMovedCampLowCairnRemnant_A01`
- Actor tags: `AET_FIRST_SLICE`, `AET_BLOODAXE_MOVED_CAMP_REVIEW`, `AET_STATIC_REVIEW_TARGET`
- Static mesh: `/Game/Aerathea/Props/Giants/BloodAxe/MovedCamp/SM_GIA_BloodAxeMovedCampLowCairnRemnant_A01`
- Material instance: `/Game/Aerathea/Materials/Instances/MI_GIA_BloodAxeMovedCampLowCairnRemnant_A01`
- No collision correctness claim and no gameplay behavior
- Updated current build/import status
- Validation summary with exact pass/fail output

## Integration Owner

Lead Producer / Orchestrator
