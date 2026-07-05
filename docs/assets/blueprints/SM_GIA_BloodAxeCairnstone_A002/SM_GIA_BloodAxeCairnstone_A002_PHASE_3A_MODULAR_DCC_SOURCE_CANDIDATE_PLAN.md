# SM_GIA_BloodAxeCairnstone_A002 Phase 3A Modular DCC Source Candidate Plan

Status: `A002 modular DCC source candidate plan recorded; geometry not generated`

Date: 2026-07-05

## Core Authority

- `AGENTS.md`
- `docs/projects/assetforge/AETHERFORGE_BLUEPRINTS.md`
- `docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A002/SM_GIA_BloodAxeCairnstone_A002_CORE_RECONSTRUCTION_ASSET_BLUEPRINT.md`
- `docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A002/SM_GIA_BloodAxeCairnstone_A002_PHASE_1_SOURCE_EVIDENCE_LOCK.md`
- `docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A002/SM_GIA_BloodAxeCairnstone_A002_PHASE_2B_MEASUREMENT_FORMULA_LOCK_DRAFT.md`
- `docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A002/SM_GIA_BloodAxeCairnstone_A002_PHASE_2C_PRE_GEOMETRY_FORMULA_AUDIT.md`

## Purpose

Define the exact A002 modular DCC source candidate generation plan before running Blender or creating geometry.

This plan does not generate geometry. It exists to prevent A001/A02 generator drift, component merging, UV/material escalation, and source-authority confusion.

## Authorized Phase 3 Goal

Generate three separate DCC source candidates:

- `primary_monolith`
- `upper_socket_ring`
- `support_base`

Each component must remain independently identifiable before any assembly proof.

## Planned A002 Component Assets

### `primary_monolith`

- Planned DCC asset: `SM_GIA_BloodAxeCairnstone_A002_PrimaryMonolith`
- Source role: vertical main Blood Axe stone.
- Source authority: A002 Phase 2 formula lock candidate, approved `120 cm x 90 cm` primary footprint candidate, and front/back/left/right primary-to-ring contact evidence.
- Center candidate: `[541, 1222]`, revalidated source-owned pixel-count center.
- Pivot policy: component-local origin at source-derived component center after cm calibration; no old shared center.
- Construction plan:
  - Build as a separate source component.
  - Use primary top footprint candidate only for the primary.
  - Use per-view primary-to-ring contact stations for bottom loop.
  - Do not flatten to old `35 cm`.
  - Do not borrow support/base pixels or upper ring geometry.
- Blocked:
  - support/base projection onto primary
  - old radial trace as footprint authority
  - old `35 cm` contact flattening
  - cross-view averaging
  - visual fitting

### `upper_socket_ring`

- Planned DCC asset: `SM_GIA_BloodAxeCairnstone_A002_UpperSocketRing`
- Source role: independent receiver layer between primary monolith and support base.
- Source authority: A002 Phase 2 per-view layered contact intervals and surface-edge markers.
- Center candidate: `[528, 1223]`, revalidated source-owned pixel-count center candidate.
- Pivot policy: component-local origin at source-derived component center after cm calibration; do not inherit primary or support pivot.
- Construction plan:
  - Build as an independent interval component.
  - Use per-view top and bottom contact stations exactly; no global average.
  - Keep top footprint diagnostic/shared/occluded unless a separate A002 formula is declared.
  - Tag hidden/occluded contact surfaces as inferred; they cannot override visible source data.
- Blocked:
  - merging into primary
  - copying/scaling support
  - same-plane annulus bridge as exterior fix
  - unapproved full cap
  - stretch strips
  - cover planes

### `support_base`

- Planned DCC asset: `SM_GIA_BloodAxeCairnstone_A002_SupportBase`
- Source role: lower support and foundation piece.
- Source authority: A002 Phase 2 formula lock candidate, approved `140 cm x 110 cm` support/base footprint candidate, and ring-bottom contact evidence.
- Center candidate: `[528, 1223]`, revalidated source-owned pixel-count center candidate.
- Pivot policy: component-local origin at source-derived component center after cm calibration.
- Construction plan:
  - Build as its own component from the support/base footprint candidate.
  - Use approved upper-ring-to-support contact stations for top contact loop.
  - Keep visible support top/annulus outside the primary component mask.
  - Do not copy, resize, or project support/base pixels into the primary component.
- Blocked:
  - full top cap sampling under primary
  - base layer copied onto primary
  - old A02/A23/A26 generator logic
  - stretch patches
  - detached shells

## Planned Output Locations

Planned DCC source folder root:

- `SourceAssets/Blender/Props/Giants/BloodAxe/Cairns/SM_GIA_BloodAxeCairnstone_A002_ModularDCCSource_A01/`

Planned automation folder:

- `Saved/Automation/DCC/SM_GIA_BloodAxeCairnstone_A002/ModularDCCSourceA01/`

Planned component source files:

- `SM_GIA_BloodAxeCairnstone_A002_PrimaryMonolith.blend`
- `SM_GIA_BloodAxeCairnstone_A002_UpperSocketRing.blend`
- `SM_GIA_BloodAxeCairnstone_A002_SupportBase.blend`

Planned manifests:

- `SM_GIA_BloodAxeCairnstone_A002_ModularDCCSourceA01Manifest.json`
- `SM_GIA_BloodAxeCairnstone_A002_ModularDCCSourceA01Audit.json`

Planned proof renders for each component:

- front
- back
- left
- right
- top
- angle

Proof renders must show component identity and socket/contact markers. They must not use UVs, texture nodes, FBX export, Unreal import, or final assembly merge.

## Generator Policy

The generator must be A002-owned and source/formula-driven.

Allowed:

- a new A002 transient generator script that reads A002 formula records
- neutral utility functions that do not carry A001/A02 asset-specific assumptions
- Blender background execution only after this plan is complete and the next action is stated

Blocked:

- copying A001 generator logic
- copying A02/A21/A23/A26 generator logic
- using old generated meshes, renders, textures, materials, exports, or Unreal assets
- inheriting contact fixes, annulus tricks, stretch passes, hidden offsets, or tuned constants
- UV generation
- texture node generation
- FBX export
- Unreal import
- final assembly merge

## Required Audit For Phase 3 Output

The Phase 3 audit must verify:

- component identity
- component-local pivot policy
- source-derived centers
- declared dimensions
- source ownership
- no UVs
- no texture nodes
- no FBX export
- no Unreal output
- no source-image pixel modification
- no A001 generated output used as source
- no A001/A02 generator inheritance
- upper socket ring remains independent
- primary/support/ring lineage remains preserved
- proof renders exist for each component

## Phase 3A Decision

Decision: `plan complete`

Phase 3A is sufficient to proceed to A002 Phase 3B generator creation, but no geometry has been generated and no DCC source candidate exists yet.

## Next Core-Valid Step

Begin A002 Phase 3B: Create A002 Modular DCC Source Candidate Generator.

The next task is to create the A002-owned Blender generator and audit script for `primary_monolith`, `upper_socket_ring`, and `support_base`, without running Blender yet.
