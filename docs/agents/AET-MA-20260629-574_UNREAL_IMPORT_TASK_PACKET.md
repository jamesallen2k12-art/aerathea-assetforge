# AET-MA-20260629-574 Unreal Import Task Packet

## Task ID

`AET-MA-20260629-574`

## Goal

Import and configure the approved first Blood Axe moved-camp static prop target `SM_GIA_BloodAxeMovedCampLowCairnRemnant_A01` in Unreal as a first-pass review target.

## Assigned Agent

Unreal Implementation + QA / Validation

## Skill

`docs/agents/skills/aerathea-unreal-implementation/`, `docs/agents/skills/aerathea-qa-validation/`

## Standing Approval Source

`docs/agents/AET-MA-20260630_PIPELINE_APPROVAL_POLICY.md` authorizes scoped technical Unreal import/configuration work when exact files, validators, and subjective approval gates are named. This packet does not authorize final visual approval, startup showcase approval, runtime gameplay behavior, combat feel, playstyle, economy, backend, source-concept movement, or Hermes work.

## Source Inputs

- Target-selection approval: `docs/agents/AET-MA-20260629-571_BUILD_TARGET_SELECTION.md`
- DCC packet: `docs/agents/AET-MA-20260629-572_DCC_TASK_PACKET.md`
- DCC validation: `docs/agents/AET-MA-20260629-573_VALIDATION_SUMMARY.md`
- DCC build status: `docs/assets/props/SM_GIA_BloodAxeMovedCampLowCairnRemnant_A01/DCC_BUILD_STATUS.md`
- Production package: `docs/assets/props/SM_GIA_BloodAxeMovedCampLowCairnRemnant_A01/PRODUCTION_PACKAGE.md`
- Implementation readiness matrix: `docs/assets/props/SM_GIA_BloodAxeMovedCampLowCairnRemnant_A01/IMPLEMENTATION_READINESS_MATRIX.md`

## Allowed Files

- `docs/agents/AET-MA-20260629-574_UNREAL_IMPORT_TASK_PACKET.md`
- `docs/agents/AET-MA-20260629-574_VALIDATION_SUMMARY.md`
- `docs/agents/AGENT_TASK_BOARD.md`
- `docs/assets/props/SM_GIA_BloodAxeMovedCampLowCairnRemnant_A01/BUILD_IMPORT_STATUS.md`
- `Tools/DCC/build_bloodaxe_moved_camp_low_cairn_remnant.py`
- `SourceAssets/Blender/Props/Giants/BloodAxe/MovedCamp/SM_GIA_BloodAxeMovedCampLowCairnRemnant_A01/SM_GIA_BloodAxeMovedCampLowCairnRemnant_A01.blend`
- `SourceAssets/Exports/Props/Giants/BloodAxe/MovedCamp/SM_GIA_BloodAxeMovedCampLowCairnRemnant_A01/SM_GIA_BloodAxeMovedCampLowCairnRemnant_A01.fbx`
- `Saved/Automation/DCC/SM_GIA_BloodAxeMovedCampLowCairnRemnant_A01/SM_GIA_BloodAxeMovedCampLowCairnRemnant_A01_DCCReview.png`
- `Tools/Unreal/import_bloodaxe_moved_camp_low_cairn_remnant.py`
- `Tools/Unreal/validate_bloodaxe_moved_camp_low_cairn_remnant.py`
- `Content/Aerathea/Props/Giants/BloodAxe/MovedCamp/SM_GIA_BloodAxeMovedCampLowCairnRemnant_A01.uasset`
- `Content/Aerathea/Materials/Giants/BloodAxe/M_GIA_BloodAxeMovedCampVertexColor_Blockout_A01.uasset`
- `Content/Aerathea/Materials/Instances/MI_GIA_BloodAxeMovedCampLowCairnRemnant_A01.uasset`

## Blocked Files

- Startup maps and placement files.
- Runtime source, Blueprints, gameplay data, quest/objective/UI/audio/VFX files, nav/pathfinding files, pickup/loot/resource/economy files, backend/vendor files, source concepts outside the repo, Hermes files or configuration, and any unrelated `Content/`, `Tools/Unreal/`, `Tools/DCC/`, `SourceAssets/`, or global docs/index files.

## Dependencies

- `AET-MA-20260629-573` DCC build validation complete.
- Source FBX exists at `SourceAssets/Exports/Props/Giants/BloodAxe/MovedCamp/SM_GIA_BloodAxeMovedCampLowCairnRemnant_A01/SM_GIA_BloodAxeMovedCampLowCairnRemnant_A01.fbx`.
- DCC source uses metric scale length `0.01`; Unreal import must use `import_uniform_scale=0.01`.

## Import Requirements

- Destination path: `/Game/Aerathea/Props/Giants/BloodAxe/MovedCamp`.
- Static mesh asset: `/Game/Aerathea/Props/Giants/BloodAxe/MovedCamp/SM_GIA_BloodAxeMovedCampLowCairnRemnant_A01`.
- Material parent: `/Game/Aerathea/Materials/Giants/BloodAxe/M_GIA_BloodAxeMovedCampVertexColor_Blockout_A01`.
- Material instance: `/Game/Aerathea/Materials/Instances/MI_GIA_BloodAxeMovedCampLowCairnRemnant_A01`.
- Import one combined static mesh from the LOD0 FBX.
- Preserve one material slot by using vertex color for first-pass stone, ash, mud, red residue, and rawhide color reads.
- Generate four review LODs in Unreal because the current FBX export contains LOD0 only.
- Disable auto-generated collision and make no collision correctness claim.
- Add no sockets, no Blueprint behavior, no runtime state, no VFX/audio, no startup actor, no review actor, and no gameplay helpers.
- Stamp metadata showing `StartupPlaced=false`, `FinalArtAuthored=false`, `CollisionPolicy=disabled_no_correctness_claim`, and `GameplayBehavior=none_static_environmental_storytelling`.

## Approval Gate

Standing pipeline approval covers this exact technical import/configuration pass. Stop before final visual approval, final shipped startup composition, runtime behavior, gameplay behavior, combat feel, playstyle, economy/vendor/reward/backend direction, VFX/audio behavior, source-concept movement, or Hermes work unless Flamestrike explicitly approves that subjective or out-of-scope decision.

If the Unreal validator shows the prop reading as a route marker, waypoint, breadcrumb, objective marker, pickup, loot pile, salvage/resource node, active signal, neutral/civilized Giant marker, or gameplay helper, return to lead and do not mark the import complete.

## Required Validators

- `python -m py_compile Tools/DCC/build_bloodaxe_moved_camp_low_cairn_remnant.py Tools/Unreal/import_bloodaxe_moved_camp_low_cairn_remnant.py Tools/Unreal/validate_bloodaxe_moved_camp_low_cairn_remnant.py`
- `blender --background --python Tools/DCC/build_bloodaxe_moved_camp_low_cairn_remnant.py`
- `UnrealEditor-Cmd ... -ExecutePythonScript=Tools/Unreal/import_bloodaxe_moved_camp_low_cairn_remnant.py`
- `UnrealEditor-Cmd ... -ExecutePythonScript=Tools/Unreal/validate_bloodaxe_moved_camp_low_cairn_remnant.py`
- Confirm the FBX contains vertex color data for the one-material visual-marker strategy.
- Confirm the imported static mesh exists at the expected Unreal path.
- Confirm four review LODs exist.
- Confirm one material slot is assigned to the Blood Axe vertex-color material instance.
- Confirm imported bounds remain within the DCC scale envelope: roughly 330 cm wide, 236 cm deep, and 130 cm tall.
- Confirm no sockets and no startup placement metadata.
- Run `git diff --check` on changed text files.
- Run ASCII and trailing-whitespace scans on changed text files.
- Run `python Tools/Agents/validate_agent_workflow.py` after task-board edits.

Startup validation is not required for this lane unless startup placement is separately approved and performed.

## Expected Deliverables

- DCC FBX refreshed only if needed to preserve vertex-color visual markers.
- Unreal import script.
- Focused Unreal validator.
- First-pass Unreal static mesh import.
- One first-pass vertex-color material parent and one material instance.
- Asset-local build/import status.
- Validation summary with exact pass/fail evidence and residual risks.

## Integration Owner

Lead Producer / Orchestrator

## QA Owner

QA / Validation

## Docs Owner

Docs / Index after validation evidence exists.

## Non-Authorization Statement

This packet does not authorize startup placement, review actor placement, final visual approval, final collision approval, runtime source, Blueprint behavior, sockets, VFX/audio, interaction behavior, pickup behavior, loot behavior, salvage behavior, resource behavior, navigation/pathfinding, waypoint behavior, breadcrumb behavior, tracking behavior, objective logic, combat feel, playstyle, economy/vendor/reward/backend direction, source concept movement, Hermes work, or global docs/index integration beyond the task-board and asset-local status files named above.
