# SM_GIA_BloodAxeCairnstone_A002 Phase 4C Snap Transform Binding Audit

Status: `snap transform binding passed; assembly generation authorized by manifest`

Date: 2026-07-05

## Core Authority

- `AGENTS.md`
- `docs/projects/assetforge/AETHERFORGE_BLUEPRINTS.md`
- `docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A002/SM_GIA_BloodAxeCairnstone_A002_CORE_RECONSTRUCTION_ASSET_BLUEPRINT.md`
- `docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A002/SM_GIA_BloodAxeCairnstone_A002_PHASE_2B_MEASUREMENT_FORMULA_LOCK_DRAFT.md`
- `docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A002/SM_GIA_BloodAxeCairnstone_A002_PHASE_2C_PRE_GEOMETRY_FORMULA_AUDIT.md`
- `docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A002/SM_GIA_BloodAxeCairnstone_A002_PHASE_4A_SNAP_ASSEMBLY_SOURCE_CANDIDATE_PLAN.md`
- `docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A002/SM_GIA_BloodAxeCairnstone_A002_PHASE_4B_SNAP_ANCHOR_MANIFEST_DRAFT.md`

## Purpose

Resolve the Phase 4B transform binding blocker before assembly generation.

This audit does not run Blender, generate assembly geometry, create UVs, create textures, export FBX, or import into Unreal.

## Evidence

A002 source authority:

- approved source template: `docs/assets/reference/bloodaxe_cairnstone_asset/REF_GIA_BloodAxeCairnstoneAsset_A02_BlueprintTemplate.png`
- approved coordinate frame: front `-Y`, back `+Y`, right `+X`, left `-X`
- approved top-view calibration: `[0.5166051661, 0.4247104247]` cm per pixel

Recovered pre-geometry orientation evidence, rebound as A002 evidence:

- top front direction marker: `[550, 1342]`
- top back direction marker: `[550, 1130]`

The recovered marker coordinates come from pre-geometry source orientation picks only. No A001 generated mesh, render, texture, material, export, or Unreal output is used as A002 authority.

## Binding Result

The front marker has larger source pixel Y than the back marker:

- `1342 > 1130`

The A002 coordinate frame defines:

- front = world `-Y`
- back = world `+Y`

Therefore:

- source image `+Y` maps to world `-Y`
- source image `-Y` maps to world `+Y`

## Primary Center Offset

Approved centers:

- primary monolith center: `[541, 1222]`
- upper socket ring center: `[528, 1223]`

Delta:

- pixel delta: `[13, -1]`
- X offset: `13 * 0.5166051661 = 6.7158671593 cm`
- Y offset: `-1 * 0.4247104247 = +0.4247104247 cm` in world `+Y`

Assembly transform for `primary_monolith` relative to `upper_socket_ring`:

- location: `[6.7158671593, 0.4247104247, 0.0]`
- rotation: `[0.0, 0.0, 0.0]`
- scale: `[1.0, 1.0, 1.0]`

Assembly transforms for `upper_socket_ring` and `support_base`:

- location: `[0.0, 0.0, 0.0]`
- rotation: `[0.0, 0.0, 0.0]`
- scale: `[1.0, 1.0, 1.0]`

## Manifest Update

Assembly-ready manifest:

- `Saved/Automation/DCC/SM_GIA_BloodAxeCairnstone_A002/SnapAssemblySourceA01/SM_GIA_BloodAxeCairnstone_A002_SnapAssemblySourceA01AnchorManifest.json`

Prior draft manifest remains as historical record:

- `Saved/Automation/DCC/SM_GIA_BloodAxeCairnstone_A002/SnapAssemblySourceA01/SM_GIA_BloodAxeCairnstone_A002_SnapAssemblySourceA01AnchorManifest_DRAFT.json`

## Phase 4C Decision

Decision: `transform_binding_passed`

The Phase 4B blocker is resolved. The assembly-ready anchor manifest authorizes Phase 4D generator and audit script creation.

## Next Core-Valid Step

Begin A002 Phase 4D: Snap Assembly Generator And Audit Script Creation.

The next task is to create the A002-owned Blender assembly generator and audit script using the assembly-ready anchor manifest, without running Blender yet.
