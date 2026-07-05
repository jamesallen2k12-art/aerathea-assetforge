# SM_GIA_BloodAxeCairnstone_A002 Phase 4B Snap Anchor Manifest Draft

Status: `snap anchor manifest draft recorded; assembly generation blocked`

Date: 2026-07-05

## Core Authority

- `AGENTS.md`
- `docs/projects/assetforge/AETHERFORGE_BLUEPRINTS.md`
- `docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A002/SM_GIA_BloodAxeCairnstone_A002_CORE_RECONSTRUCTION_ASSET_BLUEPRINT.md`
- `docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A002/SM_GIA_BloodAxeCairnstone_A002_PHASE_2B_MEASUREMENT_FORMULA_LOCK_DRAFT.md`
- `docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A002/SM_GIA_BloodAxeCairnstone_A002_PHASE_2C_PRE_GEOMETRY_FORMULA_AUDIT.md`
- `docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A002/SM_GIA_BloodAxeCairnstone_A002_PHASE_3D_VISUAL_REVIEW_DECISION.md`
- `docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A002/SM_GIA_BloodAxeCairnstone_A002_PHASE_4A_SNAP_ASSEMBLY_SOURCE_CANDIDATE_PLAN.md`

## Purpose

Record the A002 snap-anchor manifest draft before generating a snap assembly source candidate.

This step does not run Blender, generate assembly geometry, create UVs, create textures, export FBX, or import into Unreal.

## Manifest

Draft manifest:

- `Saved/Automation/DCC/SM_GIA_BloodAxeCairnstone_A002/SnapAssemblySourceA01/SM_GIA_BloodAxeCairnstone_A002_SnapAssemblySourceA01AnchorManifest_DRAFT.json`

Manifest status:

- `draft_assembly_blocked_pending_transform_binding`

## Bound Anchor Pairs

The draft records eight bound contact anchor pairs:

- `A002_PM_TO_USR_FRONT`
- `A002_PM_TO_USR_BACK`
- `A002_PM_TO_USR_LEFT`
- `A002_PM_TO_USR_RIGHT`
- `A002_USR_TO_SB_FRONT`
- `A002_USR_TO_SB_BACK`
- `A002_USR_TO_SB_LEFT`
- `A002_USR_TO_SB_RIGHT`

All contact stations remain per-view and non-averaged.

## Transform Binding Blocker

The primary monolith center differs from the upper socket ring center:

- primary center: `[541, 1222]`
- upper socket ring center: `[528, 1223]`
- delta px: `[13, -1]`
- top cm-per-pixel: `[0.5166051661, 0.4247104247]`
- X offset: `6.7158671593 cm`
- Y offset magnitude: `0.4247104247 cm`

The source records bind the coordinate frame and top-view calibration, but they do not yet explicitly bind source top-view pixel-Y direction to world-Y direction for Phase 4 assembly transform generation.

Assembly generation is blocked until that sign is declared.

## Blocked Methods

Phase 4B blocks:

- manual visual fitting
- choosing the Y sign by convenience
- ignoring the primary center offset
- forcing all component origins to one shared center
- cross-view averaged contacts
- old `35 cm` support-height flattening
- A001 or A02 generated output as source authority
- component deformation to force contact
- UV or texture generation
- FBX or Unreal output

## Phase 4B Decision

Decision: `draft_recorded_assembly_blocked`

The snap-anchor contact pairs are recorded, but the final assembly transform is not yet authorized.

This is a technical manifest gate, not a subjective visual review gate.

## Next Core-Valid Step

Begin A002 Phase 4C: Snap Transform Binding Audit.

The next task is to bind the top-view pixel-Y direction to world-Y direction from approved source evidence and then update the anchor manifest from draft to assembly-ready if the binding passes.
