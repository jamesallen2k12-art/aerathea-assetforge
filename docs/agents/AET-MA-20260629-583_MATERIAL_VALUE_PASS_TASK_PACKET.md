# AET-MA-20260629-583 Material Value Pass Task Packet

## Task ID

`AET-MA-20260629-583`

## Goal

Apply the requested first-pass Blood Axe material/value revision to `SM_GIA_BloodAxeMovedCampLowCairnRemnant_A01`, regenerate/reimport the review asset, capture a new focused Unreal review image, and stop for Flamestrike approval.

## Assigned Agent

DCC / Modeling Prep + Unreal Implementation + Visual Art Direction + QA / Validation + Docs / Index

## Allowed Files

- `Tools/DCC/build_bloodaxe_moved_camp_low_cairn_remnant.py`
- `Tools/Unreal/import_bloodaxe_moved_camp_low_cairn_remnant.py`
- `Tools/Unreal/validate_bloodaxe_moved_camp_low_cairn_remnant.py`
- `Tools/Unreal/set_startup_review_camera_preset.py`
- `Content/Aerathea/Props/Giants/BloodAxe/MovedCamp/SM_GIA_BloodAxeMovedCampLowCairnRemnant_A01.uasset`
- `Content/Aerathea/Materials/Giants/BloodAxe/M_GIA_BloodAxeMovedCampVertexColor_Blockout_A01.uasset`
- `Content/Aerathea/Materials/Instances/MI_GIA_BloodAxeMovedCampLowCairnRemnant_A01.uasset`
- `Content/Aerathea/Maps/L_Aerathea_Startup.umap`
- `SourceAssets/Blender/Props/Giants/BloodAxe/MovedCamp/SM_GIA_BloodAxeMovedCampLowCairnRemnant_A01/`
- `SourceAssets/Exports/Props/Giants/BloodAxe/MovedCamp/SM_GIA_BloodAxeMovedCampLowCairnRemnant_A01/`
- `Saved/Automation/DCC/SM_GIA_BloodAxeMovedCampLowCairnRemnant_A01/`
- `Saved/Automation/StartupReview/AeratheaStartupReview_BloodAxeLowCairnRemnant_MaterialValuePass_A01.png`
- `docs/assets/props/SM_GIA_BloodAxeMovedCampLowCairnRemnant_A01/DCC_BUILD_STATUS.md`
- `docs/assets/props/SM_GIA_BloodAxeMovedCampLowCairnRemnant_A01/BUILD_IMPORT_STATUS.md`
- `docs/agents/AET-MA-20260629-582_VISUAL_REVIEW_DECISION.md`
- `docs/agents/AET-MA-20260629-583_MATERIAL_VALUE_PASS_TASK_PACKET.md`
- `docs/agents/AET-MA-20260629-583_VALIDATION_SUMMARY.md`
- `docs/agents/AGENT_TASK_BOARD.md`

## Blocked Files

- unrelated `Content/Aerathea/` assets
- unrelated `SourceAssets/`
- unrelated `Tools/DCC/`
- unrelated `Tools/Unreal/`
- `Source/Aerathea/`
- authored BC/N/ORM texture assets
- gameplay Blueprints/classes
- VFX/audio assets
- source concept folders
- global asset indexes
- Hermes files or configuration

## Dependencies

- `AET-MA-20260629-582`
- `docs/agents/AET-MA-20260629-582_VISUAL_REVIEW_DECISION.md`
- Current DCC builder, FBX export, Unreal import script, focused asset validator, startup placement validator, and focused capture preset.

## Approval Gate

Stop at `Needs Approval` after the revised focused capture. Do not claim final visual art, final shipped startup composition, collision correctness, gameplay behavior, combat feel, playstyle, VFX/audio, economy/backend, Hermes work, or next implementation target selection.

## Required Validators

- Python compile for changed DCC and Unreal scripts.
- Blender build of `Tools/DCC/build_bloodaxe_moved_camp_low_cairn_remnant.py`.
- File existence, file type, and non-empty checks for `.blend`, `.fbx`, DCC proof PNG, and focused Unreal capture.
- Unreal reimport through `Tools/Unreal/import_bloodaxe_moved_camp_low_cairn_remnant.py`.
- Focused asset validator: `Tools/Unreal/validate_bloodaxe_moved_camp_low_cairn_remnant.py`.
- Focused startup placement validator: `Tools/Unreal/validate_bloodaxe_moved_camp_low_cairn_remnant_startup_review.py`.
- Apply focused review camera preset, capture material-value pass image, restore `overview` preset.
- Generic startup scene validator after overview restoration.
- Visual inspection of DCC proof and focused Unreal capture.
- Workflow validator.
- `git diff --check`.
- ASCII and trailing-whitespace scans for changed text/script files.

## Expected Deliverables

- Darker, rougher first-pass Blood Axe vertex-color source and FBX.
- Reimported one-material Unreal static mesh retaining review LODs and metadata.
- New focused Unreal capture ready for Flamestrike approval.
- Updated build/import status docs and validation summary.
- Task board marked `Needs Approval`.

## Integration Owner

Lead Producer / Orchestrator
