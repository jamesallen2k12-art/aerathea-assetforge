# SM_GIA_BloodAxeCairnstone_A002 Core Recovery Status - Phase 6C Empty FBX

Status: `superseded by Phase 3 analytic proof-shell dataset quarantine; reference only for Phase 6C/7D history`

Date: 2026-07-05

## Supersession Notice

This record remains valid as history for the Phase 6C empty-FBX recovery and the Phase 7D visual capture block.

It is no longer the current A002 recovery status.

Superseding record:

- `docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A002/SM_GIA_BloodAxeCairnstone_A002_CORE_RECOVERY_STATUS_20260705_PHASE3_ANALYTIC_PROOF_SHELL_DATASET.md`

Superseding decision:

- A002 Phase 3B/3C generated and advanced analytic oval proof-shell geometry instead of strict source-pixel-owned reconstruction geometry.
- Phase 3C through Phase 7D generated outputs are now `quarantined`.
- A002 production is blocked pending an approved strict-pixel recovery contract.

## Core Trigger

Phase 7C Unreal import failed before Static Mesh creation.

Unreal evidence:

- Import command: `/home/james/UnrealEngine/UE_5.8.0/Engine/Binaries/Linux/UnrealEditor-Cmd /home/james/Projects/Aerathea/Aerathea.uproject -NullRHI -NoRHIThread -NoSplash -Unattended -nop4 -ExecutePythonScript=/home/james/Projects/Aerathea/Tools/Unreal/import_bloodaxe_cairnstone_a002.py`
- Unreal log error: `There was nothing to import from the provided source data`
- Python error: `Import did not produce expected static mesh: /Game/Aerathea/Props/Giants/BloodAxe/Cairns/SM_GIA_BloodAxeCairnstone_A002`

Shell evidence:

- `SM_GIA_BloodAxeCairnstone_A002_DCCGameReady_A01.fbx`: `3980` bytes
- `SM_GIA_BloodAxeCairnstone_A002_DCCGameReady_A01_LOD0.fbx`: `3980` bytes
- `SM_GIA_BloodAxeCairnstone_A002_DCCGameReady_A01_LOD1.fbx`: `3980` bytes
- `SM_GIA_BloodAxeCairnstone_A002_DCCGameReady_A01_LOD2.fbx`: `3980` bytes
- `SM_GIA_BloodAxeCairnstone_A002_DCCGameReady_A01_LOD3.fbx`: `3980` bytes
- `SM_GIA_BloodAxeCairnstone_A002_DCCGameReady_A01_UCX.fbx`: `14492` bytes
- `strings ...DCCGameReady_A01.fbx | rg "Geometry|Model|Mesh|Vertices|PolygonVertexIndex|LayerElementMaterial"` returned no matches

## Last Known Core-Valid State

- Phase 5D texture/UV/material candidate audit pass remains valid for the pre-FBX DCC source.
- Phase 6A DCC game-ready plan remains valid authority.
- Phase 7A/7B plan/script records remain valid as written constraints but cannot proceed against the failed Phase 6C FBX output.

## First Drift Action

Phase 6C exported hidden visual LOD objects to FBX.

The audit then checked for FBX file presence but did not verify FBX mesh contents, imported object count, or triangle count.

## Assumption That Caused Drift

The workflow treated non-empty FBX files as evidence of valid visual geometry.

That was not proven evidence. The Phase 7C Unreal importer proved the assumption false.

## Affected Outputs

Invalid visual FBX exports:

- `SourceAssets/Exports/Props/Giants/BloodAxe/Cairns/SM_GIA_BloodAxeCairnstone_A002_DCCGameReady_A01/SM_GIA_BloodAxeCairnstone_A002_DCCGameReady_A01.fbx`
- `SourceAssets/Exports/Props/Giants/BloodAxe/Cairns/SM_GIA_BloodAxeCairnstone_A002_DCCGameReady_A01/SM_GIA_BloodAxeCairnstone_A002_DCCGameReady_A01_LOD0.fbx`
- `SourceAssets/Exports/Props/Giants/BloodAxe/Cairns/SM_GIA_BloodAxeCairnstone_A002_DCCGameReady_A01/SM_GIA_BloodAxeCairnstone_A002_DCCGameReady_A01_LOD1.fbx`
- `SourceAssets/Exports/Props/Giants/BloodAxe/Cairns/SM_GIA_BloodAxeCairnstone_A002_DCCGameReady_A01/SM_GIA_BloodAxeCairnstone_A002_DCCGameReady_A01_LOD2.fbx`
- `SourceAssets/Exports/Props/Giants/BloodAxe/Cairns/SM_GIA_BloodAxeCairnstone_A002_DCCGameReady_A01/SM_GIA_BloodAxeCairnstone_A002_DCCGameReady_A01_LOD3.fbx`

Partial/reference-only collision export:

- `SourceAssets/Exports/Props/Giants/BloodAxe/Cairns/SM_GIA_BloodAxeCairnstone_A002_DCCGameReady_A01/SM_GIA_BloodAxeCairnstone_A002_DCCGameReady_A01_UCX.fbx`

Quarantined Phase 6C records as FBX-validity authority:

- `Saved/Automation/DCC/SM_GIA_BloodAxeCairnstone_A002/DCCGameReadyA01/SM_GIA_BloodAxeCairnstone_A002_DCCGameReadyA01Manifest.json`
- `Saved/Automation/DCC/SM_GIA_BloodAxeCairnstone_A002/DCCGameReadyA01/SM_GIA_BloodAxeCairnstone_A002_DCCGameReadyA01Audit.json`
- `Saved/Automation/DCC/SM_GIA_BloodAxeCairnstone_A002/DCCGameReadyA01/SM_GIA_BloodAxeCairnstone_A002_DCCGameReadyA01Handoff.md`
- `docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A002/SM_GIA_BloodAxeCairnstone_A002_PHASE_6C_DCC_GAME_READY_CANDIDATE_OUTPUT_RECORD.md`

Partial Unreal outputs created before failure:

- `Content/Aerathea/Textures/Giants/BloodAxe/Cairns/SM_GIA_BloodAxeCairnstone_A002/T_GIA_BloodAxeCairnstone_A002_SourceTemplate_BC.uasset`
- `Content/Aerathea/Materials/Giants/BloodAxe/Cairns/M_GIA_BloodAxeCairnstone_A002_SourceTemplate.uasset`
- `Content/Aerathea/Materials/Giants/BloodAxe/Cairns/M_GIA_BloodAxeCairnstone_A002_InferredHidden.uasset`
- `Content/Aerathea/Materials/Instances/MI_GIA_BloodAxeCairnstone_A002_SourceTemplate.uasset`
- `Content/Aerathea/Materials/Instances/MI_GIA_BloodAxeCairnstone_A002_InferredHidden.uasset`

## Artifact Statuses

- Phase 5D output: `authoritative`
- Phase 6A plan: `authoritative`
- Phase 6B scripts: `candidate; correction required`
- Phase 6C visual FBX exports: `invalid`
- Phase 6C UCX FBX: `partial/reference only`
- Phase 6C manifest/audit/handoff/output record: `quarantined as FBX-validity authority`
- Phase 7B Unreal scripts: `candidate`
- Phase 7C partial Unreal texture/material outputs: `quarantined`

## Checkpoints

Before Phase 7C Unreal import:

- `Saved/ProjectRecovery/20260705-190226`

After failed Phase 7C Unreal import:

- `Saved/ProjectRecovery/20260705-190307`

## Smallest Sufficient Recovery

Proposed recovery sequence:

1. Correct `Tools/DCC/build_bloodaxe_cairnstone_a002_dcc_game_ready_a01.py` so visual LOD objects are export-visible during FBX export.
2. Correct `Tools/DCC/audit_bloodaxe_cairnstone_a002_dcc_game_ready_a01.py` so each visual FBX is re-imported or otherwise proven to contain mesh geometry and triangle counts.
3. Rerun Phase 6C generator and audit.
4. Record a recovery Phase 6C output only if the corrected audit passes.
5. Rerun Phase 7C import, placement, and validation only after recovered Phase 6C passes.

## Recovery Completion

Flamestrike approved the proposed recovery sequence on 2026-07-05.

Completed recovery:

- invalid Phase 6C FBXs preserved under `Saved/Automation/DCC/SM_GIA_BloodAxeCairnstone_A002/CoreRecovery/20260705_Phase6C_EmptyFBX_Quarantine/`
- Phase 6 generator corrected
- Phase 6 audit strengthened to prove visual FBX mesh/triangle contents
- recovered Phase 6C audit passed
- Phase 7C Unreal import, startup placement, and validation passed

Current status:

- A002 is an `Unreal import candidate`
- final visual approval remains pending
- A002 is not `Fully game-ready`

## Phase 7D Recovery Reopen

Phase 7D startup review capture was attempted after Phase 7C technical validation passed.

Blocked capture:

- `Saved/Automation/StartupReview/AeratheaStartupReview_BloodAxeCairnstone_A002_Phase7D.png`

Blocked record:

- `docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A002/SM_GIA_BloodAxeCairnstone_A002_PHASE_7D_STARTUP_REVIEW_CAPTURE_BLOCKED_RECORD.md`

Reason:

- the capture is framed and non-empty, but it does not match the recovered DCC game-ready proof/source authority closely enough to present for visual approval
- Phase 7C technical validation proved presence, LODs, collision, materials, placement, and metadata, but did not prove rendered visual match against the DCC proof

Current status after Phase 7D:

- Phase 7D capture PNG is `proof only; blocked evidence`
- Phase 7C Unreal import candidate is `candidate; visual-match recovery required before review`
- final visual approval remains pending
- A002 is not `Fully game-ready`

Recovery need:

- Superseded by the Phase 3 dataset root-cause finding.
- Flamestrike approval is required before any A002 rebuild, A21 reclassification, Unreal repair, second import, second placement, validator change, or second review capture.
