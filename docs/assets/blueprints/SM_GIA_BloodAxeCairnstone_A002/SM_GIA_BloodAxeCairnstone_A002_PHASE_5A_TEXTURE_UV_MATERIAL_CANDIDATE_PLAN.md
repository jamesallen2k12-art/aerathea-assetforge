# SM_GIA_BloodAxeCairnstone_A002 Phase 5A Texture UV Material Candidate Plan

Status: `texture UV material plan recorded; no UVs or textures generated`

Date: 2026-07-05

## Core Authority

- `AGENTS.md`
- `docs/projects/assetforge/AETHERFORGE_BLUEPRINTS.md`
- `docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A002/SM_GIA_BloodAxeCairnstone_A002_CORE_RECONSTRUCTION_ASSET_BLUEPRINT.md`
- `docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A002/SM_GIA_BloodAxeCairnstone_A002_PHASE_2B_MEASUREMENT_FORMULA_LOCK_DRAFT.md`
- `docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A002/SM_GIA_BloodAxeCairnstone_A002_PHASE_3D_VISUAL_REVIEW_DECISION.md`
- `docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A002/SM_GIA_BloodAxeCairnstone_A002_PHASE_4E_SNAP_ASSEMBLY_SOURCE_OUTPUT_RECORD.md`

## Purpose

Define the Phase 5 texture, UV, and material plan before generating UVs, textures, material nodes, atlases, or inferred fills.

This plan does not modify `.blend` files, generate UV layers, generate textures, create material nodes, export FBX, or import into Unreal.

## Authorized Phase 5 Goal

Create a texture/UV/material candidate that preserves visible source-pixel ownership and keeps component lineage intact.

Approved components:

- `primary_monolith`
- `upper_socket_ring`
- `support_base`

Approved assembly source:

- `SourceAssets/Blender/Props/Giants/BloodAxe/Cairns/SM_GIA_BloodAxeCairnstone_A002_SnapAssemblySource_A01/SM_GIA_BloodAxeCairnstone_A002_Assembled_Proof.blend`

## Required Pre-UV Gate

Before UV or texture generation, A002 must record a Phase 5B UV and texture ownership manifest.

The manifest must define:

- component ownership for every mesh surface
- source-view ownership for every visible exterior face
- whether each surface is visible measured, hidden inferred, diagnostic, or blocked
- UV region ownership
- texture source ownership
- source-pixel exactness requirements
- inferred-fill zones and methods
- blocked regions that may not sample visible source pixels

## Visible Source Ownership Rules

Visible surfaces must use approved source views:

- front-facing surfaces use the front source view
- back-facing surfaces use the back source view
- left-facing surfaces use the left source view
- right-facing surfaces use the right source view
- top-facing visible surfaces use the top source view only where the component owns the top region

Visible source pixels must copy exactly into visible texture outputs unless a later audit proves a color-management-only preview difference.

## Component UV Ownership Rules

Each component must retain its own UV ownership record:

- `primary_monolith`: owns its side faces and visible primary top region only
- `upper_socket_ring`: owns its independent receiver layer surfaces and tagged contact/inferred areas only
- `support_base`: owns its support/base exterior and visible top annulus outside the primary/ring ownership masks

Blocked:

- primary top UVs sampling full support/base mask
- support/base top UVs sampling inside the primary component mask
- upper socket ring UVs copied from support/base
- copied or scaled UV islands from another component
- visible side UVs sampling the wrong source view

## Hidden Or Inferred Fill Policy

Known hidden/inferred candidates:

- void under removed `primary_monolith` where it seats into `upper_socket_ring`
- void under removed `upper_socket_ring` where it seats into `support_base`
- hidden contact faces not visible in the source template

Inferred fill may be generated only after the Phase 5B ownership manifest tags the exact fill area, adjacent source, method, and affected component.

Inferred fill must not replace visible measured source pixels.

## Planned Output Locations

Planned DCC source folder:

- `SourceAssets/Blender/Props/Giants/BloodAxe/Cairns/SM_GIA_BloodAxeCairnstone_A002_TextureUVMaterial_A01/`

Planned automation folder:

- `Saved/Automation/DCC/SM_GIA_BloodAxeCairnstone_A002/TextureUVMaterialA01/`

Planned manifests:

- `SM_GIA_BloodAxeCairnstone_A002_TextureUVMaterialA01OwnershipManifest.json`
- `SM_GIA_BloodAxeCairnstone_A002_TextureUVMaterialA01Manifest.json`
- `SM_GIA_BloodAxeCairnstone_A002_TextureUVMaterialA01Audit.json`

## Material Plan

Initial material slot target:

- `1` shared source-matched stone material if audit proves component source ownership can be preserved by UV regions and metadata

Fallback material slot target:

- up to `3` component-specific material slots only if needed to preserve ownership, readability, or auditability

No emissive map is planned for this asset unless later source evidence requires it.

## Proof Requirements

Phase 5 proof outputs must include:

- UV ownership proof
- source-view ownership proof
- visible pixel exactness proof
- inferred-fill proof for hidden zones
- unlit color proof
- material assignment proof

Technical proof outputs do not require Flamestrike subjective visual review unless they expose a production decision that cannot be resolved from approved authority.

## Audit Requirements

The Phase 5 audit must verify:

- UV ownership manifest exists
- visible faces sample only their source-owned view
- visible UVs stay inside measured source regions
- primary top UVs do not sample support/base ownership
- support/base top UVs do not sample primary ownership
- inferred fills are tagged and do not replace visible measured pixels
- no A001 generated textures or materials are used as source data
- no FBX export exists
- no Unreal output exists

## Blocked Methods

Phase 5 may not use:

- A001 generated textures or materials as source authority
- A02 generated textures or materials as source authority
- texture synthesis over visible measured pixels
- manual texture painting over visible measured pixels
- UV islands copied from another component
- wrong-view side projection
- full top cap sampling across multiple components
- visible seam UVs sampling crop background or untagged padding
- FBX export
- Unreal output

## Phase 5A Decision

Decision: `plan_complete`

Phase 5A is sufficient to proceed to a UV and texture ownership manifest, but no UV or texture work has been generated.

## Next Core-Valid Step

Begin A002 Phase 5B: UV And Texture Ownership Manifest.

The next task is to create the ownership manifest from approved source records and current DCC component lineage before any UV or texture generation occurs.
