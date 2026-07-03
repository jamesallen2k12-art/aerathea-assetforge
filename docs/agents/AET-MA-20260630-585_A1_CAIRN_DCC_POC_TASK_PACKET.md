# AET-MA-20260630-585 A1 Cairn DCC POC Task Packet

## Task ID

`AET-MA-20260630-585`

## Goal

Create a Blender proof-of-concept static mesh for one Blood Axe cairn candidate, using `A1` from `VC-GIA-BloodAxe-CairnStones-A01` as the visual reference. The target asset is `SM_GIA_BloodAxeCairnSlabCluster_A01`.

## Assigned Agent

DCC / Modeling Prep + Visual Art Direction + QA / Validation + Docs / Index

## Allowed Files

- `Tools/DCC/build_bloodaxe_cairn_slab_cluster_poc.py`
- `SourceAssets/Blender/Props/Giants/BloodAxe/Cairns/SM_GIA_BloodAxeCairnSlabCluster_A01/`
- `SourceAssets/Exports/Props/Giants/BloodAxe/Cairns/SM_GIA_BloodAxeCairnSlabCluster_A01/`
- `SourceAssets/Textures/Props/Giants/BloodAxe/Cairns/SM_GIA_BloodAxeCairnSlabCluster_A01/`
- `SourceAssets/ArmorPaint/Props/Giants/BloodAxe/Cairns/SM_GIA_BloodAxeCairnSlabCluster_A01/`
- `Saved/Automation/DCC/SM_GIA_BloodAxeCairnSlabCluster_A01/`
- `Tools/DCC/launch_armorpaint_cairn_A01.sh`
- `docs/assets/props/SM_GIA_BloodAxeCairnSlabCluster_A01/PRODUCTION_PACKAGE.md`
- `docs/assets/props/SM_GIA_BloodAxeCairnSlabCluster_A01/DCC_BUILD_STATUS.md`
- `docs/agents/AET-MA-20260630-585_A1_CAIRN_DCC_POC_TASK_PACKET.md`
- `docs/agents/AET-MA-20260630-585_VALIDATION_SUMMARY.md`
- `docs/agents/AGENT_TASK_BOARD.md`
- `docs/assets/visual_canon/VC_GIA_BloodAxe_CairnStones_A01_A1_Crop.png`

## Blocked Files

`Content/Aerathea/`, `Tools/Unreal/`, runtime source, unrelated `SourceAssets/`, unrelated `Tools/DCC/`, global indexes, external source concept folders, Hermes files or configuration.

## Dependencies

- `docs/assets/visual_canon/VC_GIA_BloodAxe_CairnStones_A01_CandidateBoard.png`
- `docs/assets/visual_canon/VC_GIA_BloodAxe_CairnStones_A01_A1_Crop.png`
- `docs/assets/VISUAL_CANON_REGISTRY.md`
- `docs/assets/visual_canon/BLOODAXE_CAIRN_STONES_A01.md`
- validated Giant scale lock: female 442 cm and male 470 cm baselines.

## Approval Gate

This POC may create a Blender source, LOD source meshes, collision proxy source, FBX export, and proof render. Stop before marking `A1` as approved visual canon, final art, Unreal implementation, startup placement, gameplay behavior, collision correctness, or final visual approval.
After the user-approved ArmorPaint installation, this POC may also stage paint-target files and starter maps for manual texture approval. Stop before claiming the painted result is final until Flamestrike approves it.

## Required Validators

- `python -m py_compile Tools/DCC/build_bloodaxe_cairn_slab_cluster_poc.py`
- Blender build command
- output file existence and size checks
- ArmorPaint handoff file checks
- DCC proof visual inspection
- focused source metadata and bounds scan
- `python Tools/Agents/validate_agent_workflow.py`
- `git diff --check`
- targeted ASCII and trailing-whitespace scans

## Expected Deliverables

- Blender source for `SM_GIA_BloodAxeCairnSlabCluster_A01`.
- FBX export for DCC-to-Unreal handoff.
- Hidden LOD1-LOD3 source collections.
- Simple UCX collision proxy source.
- DCC proof render comparing the POC to the A1 visual direction.
- ArmorPaint handoff with paint target FBX, concept reference, current review image, starter maps, and export targets.
- Production package and DCC build status docs.

## Integration Owner

Lead Producer / Orchestrator
