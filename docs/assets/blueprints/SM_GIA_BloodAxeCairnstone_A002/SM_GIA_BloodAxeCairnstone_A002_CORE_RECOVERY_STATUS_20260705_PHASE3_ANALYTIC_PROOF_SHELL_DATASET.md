# SM_GIA_BloodAxeCairnstone_A002 Core Recovery Status - Phase 3 Analytic Proof Shell Dataset

Status: `Core Recovery; A21 strict-pixel recovery authority approved; production blocked before handoff plan`

Date: 2026-07-05

## Core Trigger

Flamestrike rejected the Phase 7D Unreal startup capture. The subsequent root-cause audit found that the failure was not created by the capture step. The capture exposed a bad A002 generated dataset that began in Phase 3B/3C.

The A002 branch used the approved A02 source template path, but generated analytic oval proof-shell geometry instead of strict source-pixel-owned reconstruction geometry.

## Last Known Core-Valid State

The last Core-valid A002 state is before Phase 3 production geometry:

- Phase 1 source evidence lock: approved source template and scanline evidence.
- Phase 2B measurement formula lock draft: candidate formulas recorded, geometry not authorized.
- Phase 2C pre-geometry audit: formula/crop/center/contact/snap data validated for controlled planning.

Phase 3A remained valid as a plan boundary only where it required a source/formula-driven modular DCC candidate and blocked drift. It did not authorize replacing measured visible geometry with analytic shell geometry.

## First Drift Action

Phase 3B/3C generated and advanced the analytic oval proof-shell dataset:

- `Tools/DCC/build_bloodaxe_cairnstone_a002_modular_dcc_source_a01.py`
- `Saved/Automation/DCC/SM_GIA_BloodAxeCairnstone_A002/ModularDCCSourceA01/`
- `SourceAssets/Blender/Props/Giants/BloodAxe/Cairns/SM_GIA_BloodAxeCairnstone_A002_ModularDCCSource_A01/`

The generator used source-named formula constants and cardinal contact stations, but its visible geometry was built from analytic oval loops and shell segments, not from source-owned pixel contours.

## Assumption That Caused Drift

The workflow treated formula-owned dimensions, centers, and per-view contact station heights as sufficient authority for geometry generation.

That was not enough for this asset. The A002 Core blueprint required scan-verified pixel evidence and declared formulas for geometry-defining measurements, and explicitly blocked generic primitive replacement, old generator behavior, visual fitting, and unapproved inference.

## Affected Outputs

The following output lineage is quarantined:

- Phase 3C modular DCC source output
- Phase 3D visual review decision as advancement authority
- Phase 4 snap assembly source output
- Phase 5 texture/UV/material candidate output
- Phase 6 DCC game-ready source/export outputs, including recovered Phase 6C outputs
- Phase 7C Unreal import candidate outputs
- Phase 7D startup review capture

The mixed startup map is not moved, but the local `Content/Aerathea/Maps/L_Aerathea_Startup.umap` state is tainted because it may still contain references to the quarantined A002 actor/content.

## Artifact Statuses

- Phase 1 source evidence lock: `authoritative`
- Phase 2B/2C formula and audit records: `authoritative for recovery analysis; not geometry output authority by themselves`
- Phase 3A plan: `authoritative as boundary record; insufficient as proof of final geometry authority`
- Phase 3B generator/audit scripts: `evidence; not production authority`
- Phase 3C through Phase 7D generated outputs: `quarantined`
- Phase 7D capture: `proof only; rejected visual evidence`
- A02 StrictPixelA21: `approved recovery authority for A002 strict-pixel recovery planning`
- A02 StrictPixelViewOwnedA24: `reference only; strict gate failed`
- A002 final visual approval: `pending`
- A002 `Fully game-ready`: `false`

## Correct Pixel Data Evidence Found

The strongest local strict-pixel evidence found is:

- `docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A02_StrictPixelA21/SM_GIA_BloodAxeCairnstone_A02_StrictPixelA21_3D_GAME_ASSET_BLUEPRINT.md`
- `Saved/Automation/DCC/SM_GIA_BloodAxeCairnstone_A02_StrictPixelA21/SM_GIA_BloodAxeCairnstone_A02_StrictPixelA21_StrictPixelGate.json`

A21 evidence states:

- fresh source-only rebuild from the approved A02 template
- prior generated outputs not used as source data
- visible per-view pixels exact
- visible atlas source regions exact
- no measured visible geometry replaced by superellipse
- strict gate PASS

A24 was also present, but its strict gate failed component-owner/scope checks, so it is not the clean recovery authority.

## Quarantine Location

Quarantine manifest:

- `Saved/Automation/DCC/SM_GIA_BloodAxeCairnstone_A002/CoreRecovery/20260705_Phase3_AnalyticProofShellDataset_Quarantine/QUARANTINE_MANIFEST.md`

Quarantine root:

- `Saved/Automation/DCC/SM_GIA_BloodAxeCairnstone_A002/CoreRecovery/20260705_Phase3_AnalyticProofShellDataset_Quarantine/`

## Checkpoint

Before quarantine:

- `Saved/ProjectRecovery/20260705-194054`

Checkpoint note:

- `A002 before analytic proof shell dataset quarantine`

## Recovery Decision

Flamestrike approved quarantine of the identified wrong A002 dataset on 2026-07-05.

Completed quarantine:

- generated A002 DCC source folders moved out of active `SourceAssets/Blender`
- generated A002 FBX/LOD/UCX export folder moved out of active `SourceAssets/Exports`
- A002 automation output folders moved under CoreRecovery
- A002 Unreal Content mesh/material/texture assets moved out of active `Content`
- rejected Phase 7D capture moved under CoreRecovery

No A21/A24/A001 data was moved by this action.

## A21 Recovery Authority Approval

After quarantine, Flamestrike approved using `SM_GIA_BloodAxeCairnstone_A02_StrictPixelA21` as the A002 strict-pixel recovery authority.

Approval record:

- `docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A002/SM_GIA_BloodAxeCairnstone_A002_RECOVERY_AUTHORITY_20260705_A21_STRICT_PIXEL.md`

This approval reclassifies A21 from `reference/candidate recovery evidence only` to `approved recovery authority for A002 strict-pixel recovery planning`.

This approval does not authorize copying, renaming, rebuilding, Unreal import, map repair, review capture, final visual approval, or `Fully game-ready` status.

## Current State

A002 production is blocked before the A21 handoff plan.

The next Core-valid task is to draft the A002 A21 handoff plan for Flamestrike approval.

No rebuild, copy, rename, import, map repair, visual capture, or asset status advancement is authorized by this recovery status record.
