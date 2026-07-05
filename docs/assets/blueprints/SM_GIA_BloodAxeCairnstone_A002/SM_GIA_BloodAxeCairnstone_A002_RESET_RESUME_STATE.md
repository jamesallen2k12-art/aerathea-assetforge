# SM_GIA_BloodAxeCairnstone_A002 Reset Resume State

Status: `Core Recovery; A002 analytic proof-shell dataset quarantined; production blocked`

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

- `reference/candidate recovery evidence only`
- strict gate PASS
- not promoted to A002 authority by the quarantine action

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

## Next Core-Valid Step

Stop before production.

The next task is to draft a recovery contract for Flamestrike approval. That contract must decide whether A02 StrictPixelA21 is reclassified/promoted for A002 recovery, or whether A002 must be rebuilt from the approved A02 source template with a new strict-pixel method and gate.

## Hard Boundaries

Do not do any of the following until Flamestrike approves a new recovery contract:

- rebuild A002 geometry
- promote A21 or any A02 output to A002 authority
- edit Unreal Content or maps
- run Blender generation
- export FBX
- import to Unreal
- capture a new review image
- claim DCC game-ready, Unreal import candidate, or Fully game-ready status
