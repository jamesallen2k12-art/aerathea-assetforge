# KIT_GIA_BloodAxeCairnVariantBatch_A01 Texture Material Status

## Scope

- Pass date: 2026-07-03
- Current asset status: `Unreal import candidate`
- Texture/material pass status: texture/material candidate pending Flamestrike review
- DCC builder: `Tools/DCC/build_bloodaxe_cairn_variant_textures.py`
- Unreal import script: `Tools/Unreal/import_bloodaxe_cairn_variant_textures.py`
- Unreal validation script: `Tools/Unreal/validate_bloodaxe_cairn_variant_textures.py`
- Review placement script: `Tools/Unreal/place_bloodaxe_cairn_variant_texture_review.py`

This pass authored and imported a shared BC/N/ORM candidate for the twelve Blood Axe cairn variants. The pass does not promote any asset to `Fully game-ready`, final visual approval, gameplay placement approval, or approved library status.

## Authored Source Textures

- `SourceAssets/Textures/Props/Giants/BloodAxe/Cairns/KIT_GIA_BloodAxeCairnVariantBatch_A01/T_GIA_BloodAxeCairnVariants_A01_BC.png`
- `SourceAssets/Textures/Props/Giants/BloodAxe/Cairns/KIT_GIA_BloodAxeCairnVariantBatch_A01/T_GIA_BloodAxeCairnVariants_A01_N.png`
- `SourceAssets/Textures/Props/Giants/BloodAxe/Cairns/KIT_GIA_BloodAxeCairnVariantBatch_A01/T_GIA_BloodAxeCairnVariants_A01_ORM.png`
- Proof sheet: `docs/assets/kits/KIT_GIA_BloodAxeCairnVariantBatch_A01/BloodAxeCairnVariants_A01_TextureReviewSheet.png`

The source maps are derived from existing approved Blood Axe cairn texture swatches and are intentionally neutral enough to preserve the variant vertex-color identity: dark highland stone, cave stone, ash/mud, oxide-red cloth, rawhide, iron, and bone.

## Unreal Texture Assets

- `/Game/Aerathea/Textures/Giants/BloodAxe/Cairns/KIT_GIA_BloodAxeCairnVariantBatch_A01/T_GIA_BloodAxeCairnVariants_A01_BC`
- `/Game/Aerathea/Textures/Giants/BloodAxe/Cairns/KIT_GIA_BloodAxeCairnVariantBatch_A01/T_GIA_BloodAxeCairnVariants_A01_N`
- `/Game/Aerathea/Textures/Giants/BloodAxe/Cairns/KIT_GIA_BloodAxeCairnVariantBatch_A01/T_GIA_BloodAxeCairnVariants_A01_ORM`

Texture settings validated in Unreal:

- BC: sRGB enabled.
- N: sRGB disabled, normal-map compression.
- ORM: sRGB disabled, masks compression.

## Shared Material Setup

- Parent material: `/Game/Aerathea/Materials/Giants/BloodAxe/Cairns/M_GIA_BloodAxeCairnVariants_VertexBlend_A01`
- Material instance: `/Game/Aerathea/Materials/Instances/MI_GIA_BloodAxeCairnVariants_A01`
- Material slot count: 1 shared slot per cairn variant.
- Material mode metadata: `shared_BC_N_ORM_texture_candidate_vertex_color_detail_multiplier`
- Texture set metadata: `T_GIA_BloodAxeCairnVariants_A01_BC_N_ORM`

The material keeps vertex color as the broad identity layer and applies the shared BC as a neutral detail multiplier. The normal and ORM maps provide shared stone grain, AO/contact value, roughness, and zero metallic response. No emissive map, waypoint color, quest marking, route marking, or gameplay state material is approved for this batch.

## Validation Performed

- `python3 -m py_compile` passed for the texture builder, Unreal texture import script, texture review placement script, and texture validation script.
- `python3 Tools/DCC/build_bloodaxe_cairn_variant_textures.py` authored the source BC/N/ORM maps and proof sheet.
- Unreal texture import completed with `Tools/Unreal/import_bloodaxe_cairn_variant_textures.py`.
- Unreal validation passed with `Tools/Unreal/validate_bloodaxe_cairn_variant_textures.py`.
- Validation confirmed all twelve imported meshes still have one shared material slot assigned to `MI_GIA_BloodAxeCairnVariants_A01`.
- Validation confirmed mesh metadata remains `Aerathea.StaticMesh.Status=unreal_import_candidate` and final approval remains pending.

## Review Captures

- Unlit close material review: `Saved/Automation/ReviewIsland/BloodAxeCairnVariants_A01_TextureReview_Close_Unlit.png`
- Lit close material review: `Saved/Automation/ReviewIsland/BloodAxeCairnVariants_A01_TextureReview_Close_Lit.png`

The clean close captures show the twelve variants in review-map order with readable stone value grouping, round dirt/soil bases, and retained oxide-red Blood Axe cloth accents. The lit capture is the best approval-facing view for texture/material read; the unlit capture is retained as a material identity check.

## Remaining Gates

- Flamestrike close visual review and final texture/material approval.
- Any requested material value/color adjustment from review.
- Startup or gameplay placement review, if these cairns are promoted beyond the review island.
- Performance and gameplay validation in an approved gameplay or library-review map.

## Boundary

This pass is a texture/material candidate only. Do not call the batch `Fully game-ready` until it has final visual approval, Unreal gameplay/library placement validation, collision and LOD validation in context, and performance approval.
