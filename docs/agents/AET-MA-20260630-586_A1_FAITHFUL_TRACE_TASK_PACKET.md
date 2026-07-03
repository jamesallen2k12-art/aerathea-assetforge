# AET-MA-20260630-586 A1 Faithful Trace Task Packet

## Task ID

`AET-MA-20260630-586`

## Goal

Create a separate faithful trace/projection proof for `SM_GIA_BloodAxeCairnSlabCluster_A01` using A1 as the locked source image, so the concept can be captured before final stone-shell modeling.

## Assigned Agent

DCC / Modeling Prep + Visual Art Direction + QA / Validation + Docs / Index

## Allowed Files

- `Tools/DCC/build_bloodaxe_cairn_a1_faithful_trace.py`
- `SourceAssets/Blender/Props/Giants/BloodAxe/Cairns/SM_GIA_BloodAxeCairnSlabCluster_A01_FaithfulTrace/`
- `SourceAssets/Exports/Props/Giants/BloodAxe/Cairns/SM_GIA_BloodAxeCairnSlabCluster_A01_FaithfulTrace/`
- `SourceAssets/Textures/Props/Giants/BloodAxe/Cairns/SM_GIA_BloodAxeCairnSlabCluster_A01_FaithfulTrace/`
- `Saved/Automation/DCC/SM_GIA_BloodAxeCairnSlabCluster_A01_FaithfulTrace/`
- `docs/assets/props/SM_GIA_BloodAxeCairnSlabCluster_A01/FAITHFUL_TRACE_STATUS.md`
- `docs/agents/AET-MA-20260630-586_A1_FAITHFUL_TRACE_TASK_PACKET.md`
- `docs/agents/AET-MA-20260630-586_VALIDATION_SUMMARY.md`
- `docs/agents/AGENT_TASK_BOARD.md`

## Blocked Files

`Content/Aerathea/`, `Tools/Unreal/`, runtime source, unrelated `SourceAssets/`, unrelated `Tools/DCC/`, global indexes, external source concept folders, Hermes files or configuration.

## Approval Gate

Stop before marking A1 as approved canon, final art, final 360-degree game mesh, Unreal import, startup placement, gameplay behavior, collision correctness, or material final.

## Required Validators

- `python -m py_compile Tools/DCC/build_bloodaxe_cairn_a1_faithful_trace.py`
- Blender build command
- Output file type and size checks
- Workflow validator
- `git diff --check`
- Targeted ASCII and trailing-whitespace scans
- Overclaim scan

## Expected Deliverables

- Separate faithful trace Blender source.
- Projection texture copy.
- Main FBX plus LOD0-LOD3 exports.
- Exact projection review render.
- Cutout trace review render.
- Overlay fit review render.
- Faithful trace status doc and validation summary.
