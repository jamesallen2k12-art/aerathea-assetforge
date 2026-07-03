# KIT_GIA_BloodAxeCairnVariantBatch_A01 Unreal Import Status

## Scope

- Import date: 2026-07-03
- Source status: `DCC game-ready candidate`
- Current status: `Unreal import candidate`
- Import script: `Tools/Unreal/import_bloodaxe_cairn_variant_batch.py`
- Validation script: `Tools/Unreal/validate_bloodaxe_cairn_variant_batch.py`
- Review placement script: `Tools/Unreal/place_bloodaxe_cairn_variant_batch_review.py`
- Review capture: `Saved/Automation/ReviewIsland/BloodAxeCairnVariants_A01_UnrealReview_Unlit.png`

This pass imported the twelve Blood Axe cairn variants into Unreal, validated their static mesh setup, and placed them on `/Game/Aerathea/Maps/L_Aerathea_ReviewIsland` for batch review. The pass promotes the assets to `Unreal import candidate` only. It does not approve final hand-painted textures, final material polish, gameplay use, route logic, waypoint logic, quest markers, salvage/loot behavior, destructible behavior, or `Fully game-ready` status.

## Shared Unreal Assets

- Parent material: `/Game/Aerathea/Materials/Giants/BloodAxe/Cairns/M_GIA_BloodAxeCairnVariants_VertexBlend_A01`
- Material instance: `/Game/Aerathea/Materials/Instances/MI_GIA_BloodAxeCairnVariants_A01`
- Review material mode: shared vertex-color review material, not final BC/N/ORM texture art.
- Review map: `/Game/Aerathea/Maps/L_Aerathea_ReviewIsland`
- Batch review tag: `AET_BLOODAXE_CAIRN_VARIANT_BATCH_REVIEW`

## Import Adjustment

Initial import testing found that the Unreal Interchange/FBX path treated the DCC `UCX_` collision proxies in the main FBX as renderable sections, producing extra material slots. The final import therefore uses a visual-only `*_UnrealImport.fbx` for each asset. The original main FBX and `_LOD0.fbx` still retain UCX-style proxies for DCC audit and parity, while the Unreal import script adds broad simple collision fallback and records the collision policy in mesh metadata.

Validated import source requirements:

- Twelve `*_UnrealImport.fbx` files exist.
- Visual import FBXs do not contain `UCX_` proxy geometry.
- Visual import FBXs contain vertex color data.
- `_LOD1.fbx`, `_LOD2.fbx`, and `_LOD3.fbx` exist for all twelve variants.

## Imported Static Meshes

| Asset | Unreal Static Mesh Path | Bounds | Collision |
| --- | --- | --- | --- |
| `SM_GIA_BloodAxeApproachCairnMarker_A01` | `/Game/Aerathea/Props/Giants/BloodAxe/StrongholdApproach/CairnMarkers/SM_GIA_BloodAxeApproachCairnMarker_A01` | 109.22h x 364.00w x 212.00d cm | broad simple |
| `SM_GIA_BloodAxeRitualCairnGuidepost_A01` | `/Game/Aerathea/Props/Giants/BloodAxe/RitualStones/Guideposts/SM_GIA_BloodAxeRitualCairnGuidepost_A01` | 182.97h x 252.00w x 180.00d cm | broad simple |
| `SM_GIA_BloodAxeLowThresholdCairn_A01` | `/Game/Aerathea/Props/Giants/BloodAxe/CaveApproachMarkers/SM_GIA_BloodAxeLowThresholdCairn_A01` | 111.73h x 310.00w x 220.00d cm | broad simple |
| `SM_GIA_BloodAxeCollapsedThresholdCairn_A01` | `/Game/Aerathea/Props/Giants/BloodAxe/CaveApproachMarkers/SM_GIA_BloodAxeCollapsedThresholdCairn_A01` | 121.85h x 356.00w x 256.00d cm | broad simple |
| `SM_GIA_BloodAxeCaveRemnantCairn_A01` | `/Game/Aerathea/Props/Giants/BloodAxe/CaveApproachMarkers/SM_GIA_BloodAxeCaveRemnantCairn_A01` | 146.11h x 330.00w x 236.00d cm | broad simple |
| `SM_GIA_BloodAxeCollapsedCaveRemnantCairn_A01` | `/Game/Aerathea/Props/Giants/BloodAxe/CaveApproachMarkers/SM_GIA_BloodAxeCollapsedCaveRemnantCairn_A01` | 88.14h x 372.00w x 264.00d cm | broad simple |
| `SM_GIA_BloodAxeCaveThresholdCairnPair_A01` | `/Game/Aerathea/Props/Giants/BloodAxe/CaveApproachMarkers/SM_GIA_BloodAxeCaveThresholdCairnPair_A01` | 111.73h x 620.00w x 252.00d cm | broad simple |
| `SM_GIA_BloodAxeMovedCampCairnPair_A01` | `/Game/Aerathea/Props/Giants/BloodAxe/MovedCamp/SM_GIA_BloodAxeMovedCampCairnPair_A01` | 121.85h x 588.00w x 292.00d cm | broad simple |
| `SM_GIA_BloodAxePairedCairnClosePair_A01` | `/Game/Aerathea/Props/Giants/BloodAxe/CairnGuideposts/SM_GIA_BloodAxePairedCairnClosePair_A01` | 154.21h x 480.00w x 224.00d cm | broad simple |
| `SM_GIA_BloodAxePairedCairnStaggeredPair_A01` | `/Game/Aerathea/Props/Giants/BloodAxe/CairnGuideposts/SM_GIA_BloodAxePairedCairnStaggeredPair_A01` | 154.21h x 595.00w x 334.00d cm | broad simple |
| `SM_GIA_BloodAxeCairnPathMarker_A01` | `/Game/Aerathea/Props/Giants/BloodAxe/PathMarkers/SM_GIA_BloodAxeCairnPathMarker_A01` | 126.56h x 264.00w x 184.00d cm | broad simple |
| `SM_GIA_BloodAxeCairnScrapCap_A01` | `/Game/Aerathea/Props/Giants/BloodAxe/PathMarkers/SM_GIA_BloodAxeCairnScrapCap_A01` | 126.43h x 310.00w x 220.00d cm | broad simple |

## Validation Performed

- `python3 -m py_compile` passed for the DCC builder and all Blood Axe cairn variant Unreal automation scripts.
- `blender --background --python Tools/DCC/build_bloodaxe_cairn_variant_batch.py` completed after adding visual-only Unreal import FBXs.
- Corrected Unreal import completed with `Tools/Unreal/import_bloodaxe_cairn_variant_batch.py`.
- Unreal validation passed for all twelve static meshes with 4 LODs each.
- Each imported mesh has 1 material slot assigned to the shared material instance.
- Each imported mesh has simple collision present.
- Each imported mesh has no sockets and no Blueprint/gameplay behavior.
- Mesh metadata records `Aerathea.StaticMesh.Status=unreal_import_candidate`, source status, package doc, import packet, collision policy, final-art boundary, material mode, and review placement state.
- Review island placement completed and saved the batch actors in contact-sheet order.
- Clean offscreen review capture completed at `Saved/Automation/ReviewIsland/BloodAxeCairnVariants_A01_UnrealReview_Unlit.png`.

## Boundaries

- Not `Fully game-ready`.
- Not final visual approval.
- Not final hand-painted BC/N/ORM texture art.
- Not final material polish.
- Not startup-scene gameplay placement.
- Not gameplay route, waypoint, quest, pickup, loot, salvage, destructible, physics, encounter, VFX, audio, or nav/pathfinding approval.

## Next Gate

The next useful gate is Flamestrike review of the Unreal batch capture and/or live review island. After that, choose whether the batch needs final texture/material authoring, silhouette revisions, route-context placement, or selected promotion into an approved asset library set.
