# KIT_GIA_BloodAxeCairnVariantBatch_A01 DCC Game-Ready Prep Status

## Scope

- Prep date: 2026-07-03
- Builder: `Tools/DCC/build_bloodaxe_cairn_variant_batch.py`
- Review sheet builder: `Tools/DCC/build_bloodaxe_cairn_variant_review_sheet.py`
- Contact sheet: `docs/assets/kits/KIT_GIA_BloodAxeCairnVariantBatch_A01/BloodAxeCairnVariants_A01_DCCReviewContactSheet.png`
- Status after this pass: `DCC game-ready candidate`
- Current follow-up status: `Unreal import candidate`

This DCC pass moved the twelve Blood Axe cairn variants from `DCC source candidate` to `DCC game-ready candidate` for Unreal import testing. A follow-up Unreal import pass on 2026-07-03 promoted the same twelve assets to `Unreal import candidate`; see `UNREAL_IMPORT_STATUS.md`. They are still not `Gameplay validated asset`, `Approved library asset`, or `Fully game-ready`.

## Completed DCC Gates

- Blender source exists for each variant.
- Main FBX exists for each variant.
- Visual-only `*_UnrealImport.fbx` exists for each variant after the Unreal import adjustment.
- LOD0, LOD1, LOD2, and LOD3 FBX exports exist for each variant.
- UV0 review unwraps are generated for visible mesh objects.
- Broad UCX-style collision proxies are included in each main FBX and LOD0 FBX.
- Ground-center pivot is preserved.
- Scale uses the existing Aerathea Blender centimeter workflow and Giant 442 cm / 470 cm proof markers.
- Proof renders and the tracked contact sheet exist for DCC review.
- Material and texture plan is defined below.
- Unreal import task packet is defined in `UNREAL_IMPORT_TASK_PACKET.md`.

## Material And Texture Plan

Use one material slot per asset for import testing:

- DCC material: `M_GIA_BloodAxeCairnVariants_VertexColor_A01`
- Unreal parent material target: `/Game/Aerathea/Materials/Giants/BloodAxe/Cairns/M_GIA_BloodAxeCairnVariants_VertexBlend_A01`
- Unreal material instance target: `/Game/Aerathea/Materials/Instances/MI_GIA_BloodAxeCairnVariants_A01`
- Shared planned texture root: `/Game/Aerathea/Textures/Giants/BloodAxe/Cairns/KIT_GIA_BloodAxeCairnVariantBatch_A01/`

Planned texture set:

- `T_GIA_BloodAxeCairnVariants_A01_BC`
- `T_GIA_BloodAxeCairnVariants_A01_N`
- `T_GIA_BloodAxeCairnVariants_A01_ORM`

The import-test material should use vertex color to preserve the current dark stone, cave stone, ash/mud, oxide red cloth, rawhide, iron, and bone read. The shared BC/N/ORM set should provide hand-painted stone grain, edge wear, contact darkening, rough ash, cloth fiber, and restrained material variation. No emissive map is approved for this batch.

## UV Plan

- UV channel: `UV0`
- Method: deterministic smart-projected review unwrap generated during the Blender build.
- Intended use: Unreal import testing, material assignment, and early texture/material proofing.
- Boundary: these UVs are not a final hero hand-unwrap. If any variant becomes a foreground hero prop, it needs a hand-authored UV cleanup pass before final texture approval.

## Collision Plan

- Collision type: broad simple static-prop collision.
- Source: UCX-style boxes named `UCX_<AssetName>_<Index>` in each main FBX and LOD0 FBX.
- Single-cairn variants use one collision proxy.
- Paired variants use one proxy per cairn stack.
- Collision should block broad traversal only. It must not define route gates, quest triggers, nav blockers, encounter boundaries, pickup volumes, objective markers, damage volumes, or destructible behavior.
- Unreal import validation must confirm simple collision exists. If the combine-mesh import path does not consume the UCX proxy automatically, the importer should add equivalent simple box collision and record that fallback.

## Validation Performed

- `python3 -m py_compile Tools/DCC/build_bloodaxe_cairn_variant_batch.py Tools/DCC/build_bloodaxe_cairn_variant_review_sheet.py` passed.
- `blender --background --python Tools/DCC/build_bloodaxe_cairn_variant_batch.py` completed.
- `python3 Tools/DCC/build_bloodaxe_cairn_variant_review_sheet.py` completed.
- Scoped LOD size check found no `_LOD1` through `_LOD3` FBX files under 5000 bytes for the twelve variant folders.
- Scoped FBX string check found `UCX_SM_GIA_BloodAxe...` markers in each main and LOD0 FBX.
- Scoped FBX string check found no `UCX_` markers in the visual-only `*_UnrealImport.fbx` files used by Unreal.
- Scoped FBX string check found `LayerElementUV` data across the exported variant FBX set.
- Follow-up Unreal import validation passed for all twelve assets with 4 LODs, 1 shared material slot, simple collision present, mesh metadata, and review island placement.

## Remaining Gates

- Unreal import has run and passed validation; status details are tracked in `UNREAL_IMPORT_STATUS.md`.
- Unreal material parent and material instance exist as shared review material assets.
- Texture maps are planned but not authored in this pass.
- Broad simple collision has been validated in Unreal as import-candidate collision.
- LOD count has been validated in Unreal.
- Review island placement exists; startup/gameplay placement has not been created.
- Gameplay behavior, route logic, waypoint behavior, quest markers, VFX/audio, destructible behavior, pickup/loot/salvage behavior, and final visual approval remain blocked.

## Decision Boundary

The batch source remains valid as `DCC game-ready candidate`, and the imported Unreal assets are now `Unreal import candidate`. Do not call any variant `Fully game-ready` until final texture/material work, gameplay placement, performance checks, and Flamestrike approval are complete.
