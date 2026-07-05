# SM_GIA_BloodAxeCairnstone_A002 Reset Resume State

Status: `Core Recovery; A21 handoff plan drafted; pending Flamestrike approval before production file action`

Date: 2026-07-05

## Resume Instruction

On reset/resume, read this file first, then read the listed authority records before taking production action.

Do not rely on conversation memory.

## Core Authority

- `AGENTS.md`
- `docs/projects/assetforge/AETHERFORGE_BLUEPRINTS.md`
- `docs/projects/assetforge/DRIFT_LEDGER.md`
- `docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A002/SM_GIA_BloodAxeCairnstone_A002_CORE_RECONSTRUCTION_ASSET_BLUEPRINT.md`
- `docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A002/SM_GIA_BloodAxeCairnstone_A002_CORE_RECOVERY_STATUS_20260705_PHASE3_ANALYTIC_PROOF_SHELL_DATASET.md`

## Current A002 State

A002 is in Core Recovery.

Root-cause finding:

- The wrong A002 dataset began at Phase 3B/3C.
- The branch used the correct A02 source template path, but generated analytic oval proof-shell geometry instead of strict source-pixel-owned reconstruction geometry.
- The bad dataset propagated through Phase 4, Phase 5, Phase 6, Phase 7C, and the rejected Phase 7D capture.

Current status:

- Phase 3C through Phase 7D generated outputs are `quarantined`.
- A002 active generated DCC source/export/Unreal Content outputs have been moved out of active production locations.
- The Phase 7D capture is `proof only; rejected visual evidence`.
- `Content/Aerathea/Maps/L_Aerathea_Startup.umap` is `tainted/mixed local map state`; it was not moved.
- A21 is approved as the strict-pixel recovery authority for A002 planning.
- A21 handoff plan is drafted and pending Flamestrike approval.
- A002 has no valid active DCC game-ready candidate.
- A002 has no valid active Unreal import candidate.
- A002 is not `Fully game-ready`.

## Latest Recovery Checkpoint

Manual checkpoint before quarantine:

- `Saved/ProjectRecovery/20260705-194054`

Checkpoint note:

- `A002 before analytic proof shell dataset quarantine`

## Quarantine Location

Quarantine manifest:

- `Saved/Automation/DCC/SM_GIA_BloodAxeCairnstone_A002/CoreRecovery/20260705_Phase3_AnalyticProofShellDataset_Quarantine/QUARANTINE_MANIFEST.md`

Quarantine root:

- `Saved/Automation/DCC/SM_GIA_BloodAxeCairnstone_A002/CoreRecovery/20260705_Phase3_AnalyticProofShellDataset_Quarantine/`

## Correct Pixel Data Evidence Found

Strongest local strict-pixel evidence:

- `docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A02_StrictPixelA21/SM_GIA_BloodAxeCairnstone_A02_StrictPixelA21_3D_GAME_ASSET_BLUEPRINT.md`
- `Saved/Automation/DCC/SM_GIA_BloodAxeCairnstone_A02_StrictPixelA21/SM_GIA_BloodAxeCairnstone_A02_StrictPixelA21_StrictPixelGate.json`

A21 status:

- `approved recovery authority for A002 strict-pixel recovery planning`
- strict gate PASS
- not yet copied, renamed, rebuilt, imported, or visually approved as A002

A24 status:

- `reference only`
- strict gate failed

## Required Read Before Continuing

Read in this order:

1. `docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A002/SM_GIA_BloodAxeCairnstone_A002_CORE_RECONSTRUCTION_ASSET_BLUEPRINT.md`
2. `docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A002/SM_GIA_BloodAxeCairnstone_A002_CORE_RECOVERY_STATUS_20260705_PHASE3_ANALYTIC_PROOF_SHELL_DATASET.md`
3. `docs/projects/assetforge/DRIFT_LEDGER.md`
4. `Saved/Automation/DCC/SM_GIA_BloodAxeCairnstone_A002/CoreRecovery/20260705_Phase3_AnalyticProofShellDataset_Quarantine/QUARANTINE_MANIFEST.md`
5. `docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A02_StrictPixelA21/SM_GIA_BloodAxeCairnstone_A02_StrictPixelA21_3D_GAME_ASSET_BLUEPRINT.md`
6. `docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A002/SM_GIA_BloodAxeCairnstone_A002_RECOVERY_AUTHORITY_20260705_A21_STRICT_PIXEL.md`
7. `docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A002/SM_GIA_BloodAxeCairnstone_A002_A21_HANDOFF_PLAN_DRAFT.md`

## Next Core-Valid Step

Stop before production file actions.

The next task is to wait for Flamestrike approval or rejection of the A002 A21 handoff plan.

Pending plan:

- `docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A002/SM_GIA_BloodAxeCairnstone_A002_A21_HANDOFF_PLAN_DRAFT.md`

## Hard Boundaries

Do not do any of the following until Flamestrike approves the A21 handoff plan:

- rebuild A002 geometry
- copy, rename, or move A21 files
- edit Unreal Content or maps
- run Blender generation
- export FBX
- import to Unreal
- capture a new review image
- claim DCC game-ready, Unreal import candidate, or Fully game-ready status
