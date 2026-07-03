# AET-MA-20260630-587 A1 Game-Ready Faithful Task Packet

## Task ID

`AET-MA-20260630-587`

## Goal

Promote the A1 faithful trace proof into a DCC game-ready static-mesh candidate with actual slab-shell depth, concept-projected front UVs, side/back materials, LOD0-LOD3 FBX exports, collision proxy source, texture maps, and review renders.

## Assigned Agent

DCC / Modeling Prep + Visual Art Direction + QA / Validation + Docs / Index

## Allowed Files

- `Tools/DCC/build_bloodaxe_cairn_a1_game_ready.py`
- `SourceAssets/Blender/Props/Giants/BloodAxe/Cairns/SM_GIA_BloodAxeCairnSlabCluster_A01_GameReady/`
- `SourceAssets/Exports/Props/Giants/BloodAxe/Cairns/SM_GIA_BloodAxeCairnSlabCluster_A01_GameReady/`
- `SourceAssets/Textures/Props/Giants/BloodAxe/Cairns/SM_GIA_BloodAxeCairnSlabCluster_A01_GameReady/`
- `Saved/Automation/DCC/SM_GIA_BloodAxeCairnSlabCluster_A01_GameReady/`
- `docs/assets/props/SM_GIA_BloodAxeCairnSlabCluster_A01/GAME_READY_FAITHFUL_STATUS.md`
- `docs/assets/props/SM_GIA_BloodAxeCairnSlabCluster_A01/PRODUCTION_PACKAGE.md`
- `docs/assets/props/SM_GIA_BloodAxeCairnSlabCluster_A01/DCC_BUILD_STATUS.md`
- `docs/agents/AET-MA-20260630-587_A1_GAME_READY_TASK_PACKET.md`
- `docs/agents/AET-MA-20260630-587_VALIDATION_SUMMARY.md`
- `docs/agents/AGENT_TASK_BOARD.md`

## Blocked Files

- `Content/Aerathea/`
- `Tools/Unreal/`
- runtime source
- unrelated `SourceAssets/`
- unrelated `Tools/DCC/`
- global indexes unless a follow-up integration task assigns them
- external source concept folders
- Hermes files or configuration

## Dependencies

- `AET-MA-20260630-586`
- `docs/assets/visual_canon/VC_GIA_BloodAxe_CairnStones_A01_A1_Crop.png`

## Approval Gate

Stop before marking A1 as approved canon, final all-angle sculpt, Unreal imported, startup placed, gameplay approved, collision correct, or material final. Flamestrike must approve subjective visual quality before Unreal import or canon lock.

## Required Validators

- Python compile
- Blender build
- output file checks
- review render inspection
- workflow validator
- `git diff --check`
- targeted ASCII/trailing-whitespace scans
- overclaim scan

## Expected Deliverables

- Blender source for `SM_GIA_BloodAxeCairnSlabCluster_A01_GameReady`
- main FBX with collision proxy
- LOD0-LOD3 FBX exports
- concept projection texture copy
- side/back BC/N/ORM texture maps
- front match and perspective review renders
- status doc
- validation summary
