# SM_GIA_BloodAxeCairnstone_A002 Recovery Authority - A21 Strict Pixel

Status: `approved recovery authority; no production rebuild executed`

Date: 2026-07-05

## Core Decision

Flamestrike approved using `SM_GIA_BloodAxeCairnstone_A02_StrictPixelA21` as the A002 strict-pixel recovery authority.

This reclassifies A21 from `reference/candidate recovery evidence only` to:

- `authoritative for A002 strict-pixel recovery method`
- `authoritative as local source-pixel evidence package for A002 recovery planning`
- `candidate DCC game-ready source for A002 recovery, pending A002 naming/handoff plan and review`

This does not make A002 fully game-ready.

## What Is Approved

Approved:

- Use A21's strict-pixel source hierarchy and evidence records as the recovery authority for A002.
- Use A21's passed strict gate as evidence that this is the correct local pixel-accurate data family.
- Use A21's declared coordinate frame, source hierarchy, pixel convention, contact/center results, LOD counts, texture package, and audit gate as the recovery baseline.
- Draft the next A002 production handoff around A21 instead of the quarantined A002 analytic proof-shell branch.

## What Is Not Approved By This Record

Not approved:

- copying, renaming, or moving A21 source/export/texture files
- rebuilding geometry
- generating new A002 files
- importing to Unreal
- editing `L_Aerathea_Startup.umap`
- creating a new review capture
- claiming final Flamestrike visual approval
- claiming `Fully game-ready`

## Authority Evidence

A21 blueprint:

- `docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A02_StrictPixelA21/SM_GIA_BloodAxeCairnstone_A02_StrictPixelA21_3D_GAME_ASSET_BLUEPRINT.md`

A21 strict gate:

- `Saved/Automation/DCC/SM_GIA_BloodAxeCairnstone_A02_StrictPixelA21/SM_GIA_BloodAxeCairnstone_A02_StrictPixelA21_StrictPixelGate.json`

A21 build manifest:

- `Saved/Automation/DCC/SM_GIA_BloodAxeCairnstone_A02_StrictPixelA21/SM_GIA_BloodAxeCairnstone_A02_StrictPixelA21_3DBuildManifest.json`

## A21 Evidence Summary

A21 records prove:

- source template: `docs/assets/reference/bloodaxe_cairnstone_asset/REF_GIA_BloodAxeCairnstoneAsset_A02_BlueprintTemplate.png`
- fresh data only: `true`
- prior generated outputs used: `false`
- strict gate: `passed`
- failed strict-gate checks: none
- source scanline exact: passed
- visible per-view pixels exact: front, back, left, right, top
- visible atlas source regions exact: front, back, left, right, top
- no visible atlas filtered resize
- no measured visible geometry replaced by superellipse
- no visible averaged measurements
- contact gaps: zero
- center offsets: zero
- rotations: zeroed
- meshes: closed with no boundary/non-manifold edges
- bounds: `[139.38864135742188, 109.5358657836914, 220.0]`
- LOD triangle counts: `[13300, 4628, 1812, 716]`

## A24 Status

`SM_GIA_BloodAxeCairnstone_A02_StrictPixelViewOwnedA24` remains `reference only`.

Reason:

- its strict gate failed component-owner and component-scope checks.

## Quarantined Branch Status

The A002 analytic proof-shell branch remains quarantined:

- `Saved/Automation/DCC/SM_GIA_BloodAxeCairnstone_A002/CoreRecovery/20260705_Phase3_AnalyticProofShellDataset_Quarantine/`

It must not be used as geometry, texture, export, Unreal import, or visual approval authority unless Flamestrike explicitly reclassifies a specific artifact later.

## Current A002 Status

A002 is in Core Recovery.

A21 is now the approved strict-pixel recovery authority, but no active A002 production asset has been rebuilt or imported from it yet.

## Next Core-Valid Step

Draft the A002 A21 handoff plan.

That plan must decide the exact non-ambiguous production route before any production file action:

- whether to keep the A21 asset name as the imported asset name, or produce an A002-named derivative package from A21
- which files may be copied or renamed
- how to preserve A21 evidence lineage inside A002 records
- which strict gate must pass after any rename or package change
- what Unreal import path and map repair actions are allowed
- what review artifact must be opened for Flamestrike

No production file action is authorized until that handoff plan is approved.
