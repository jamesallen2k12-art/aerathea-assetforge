# SM_GIA_BloodAxeCairnstone_A002 Phase 5B UV Texture Ownership Manifest

Status: `ownership manifest recorded; UV and texture generation not authorized`

Date: 2026-07-05

## Core Authority

- `AGENTS.md`
- `docs/projects/assetforge/AETHERFORGE_BLUEPRINTS.md`
- `docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A002/SM_GIA_BloodAxeCairnstone_A002_CORE_RECONSTRUCTION_ASSET_BLUEPRINT.md`
- `docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A002/SM_GIA_BloodAxeCairnstone_A002_PHASE_2B_MEASUREMENT_FORMULA_LOCK_DRAFT.md`
- `docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A002/SM_GIA_BloodAxeCairnstone_A002_PHASE_4E_SNAP_ASSEMBLY_SOURCE_OUTPUT_RECORD.md`
- `docs/assets/blueprints/SM_GIA_BloodAxeCairnstone_A002/SM_GIA_BloodAxeCairnstone_A002_PHASE_5A_TEXTURE_UV_MATERIAL_CANDIDATE_PLAN.md`

## Purpose

Record the UV, texture, material, visible source, and inferred-fill ownership rules before generating UVs, textures, material nodes, atlases, or inferred fills.

This step does not modify `.blend` files, generate UV layers, generate textures, create material nodes, export FBX, or import into Unreal.

## Manifest

Ownership manifest:

- `Saved/Automation/DCC/SM_GIA_BloodAxeCairnstone_A002/TextureUVMaterialA01/SM_GIA_BloodAxeCairnstone_A002_TextureUVMaterialA01OwnershipManifest.json`

Manifest status:

- `ownership_manifest_recorded_uv_texture_generation_not_authorized`

## Source Authority

Approved source:

- `docs/assets/reference/bloodaxe_cairnstone_asset/REF_GIA_BloodAxeCairnstoneAsset_A02_BlueprintTemplate.png`

Approved scanline manifest:

- `docs/assets/reference/bloodaxe_cairnstone_asset/ScanlineCapture/REF_GIA_BloodAxeCairnstoneAsset_A02_BlueprintTemplate_ScanlineManifest.json`

Visible pixels must copy exactly from approved source regions.

## Component Ownership

The manifest records ownership for:

- `primary_monolith`
- `upper_socket_ring`
- `support_base`

Each component has:

- visible measured source-view ownership
- hidden/contact/inferred ownership
- component-specific UV record requirement
- material-slot strategy

## Global Source-View Rules

- Front-facing surfaces use the front source view.
- Back-facing surfaces use the back source view.
- Left-facing surfaces use the left source view.
- Right-facing surfaces use the right source view.
- Top-facing surfaces use the top source view only where the component owns the sampled top region.
- Hidden/contact surfaces use tagged inferred fill only.

## Inferred Fill Rules

Known inferred areas are tagged for:

- primary bottom contact face
- upper socket primary receiver void
- upper socket bottom contact face
- support/base upper socket receiver void
- support/base underside

Inferred fill:

- may source-match adjacent material appearance
- must be labeled inferred
- must not overwrite visible measured pixels
- must not become visual-canon source data
- must not alter silhouette, contact geometry, or assembly behavior

## Material Strategy

Initial target:

- `1` shared stone material: `MI_GIA_BloodAxeCairnstone_A002_Stone`

Condition:

- allowed only if UV region metadata and audit preserve component/source ownership

Fallback:

- `3` component-specific material slots if needed for auditability or readability

No emissive map is planned.

## Blocked Methods

Phase 5B blocks:

- A001 generated textures or materials as source authority
- A02 generated textures or materials as source authority
- texture synthesis over visible measured pixels
- manual texture painting over visible measured pixels
- UV islands copied from another component
- wrong-view side projection
- full top cap sampling across multiple components
- support/base top pixels sampled inside the primary mask
- primary top UVs sampled from the full support/base top mask
- visible seam UVs sampling crop background or untagged padding
- FBX export
- Unreal output

## Phase 5B Decision

Decision: `ownership_manifest_recorded`

Phase 5B is complete as an ownership-manifest step. UV and texture generation is still blocked until generator and audit scripts are created for the approved manifest.

## Next Core-Valid Step

Begin A002 Phase 5C: Texture UV Material Generator And Audit Script Creation.

The next task is to create the A002-owned UV/texture/material generator and audit scripts from this ownership manifest, without running Blender or generating textures yet.
