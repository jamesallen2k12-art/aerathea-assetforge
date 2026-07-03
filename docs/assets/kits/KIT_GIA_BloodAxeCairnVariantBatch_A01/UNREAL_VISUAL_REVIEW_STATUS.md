# KIT_GIA_BloodAxeCairnVariantBatch_A01 Unreal Visual Review Status

## Scope

- Review date: 2026-07-03
- Review type: Codex Unreal visual gate, not Flamestrike final visual approval
- Source comparison: `docs/assets/kits/KIT_GIA_BloodAxeCairnVariantBatch_A01/BloodAxeCairnVariants_A01_DCCReviewContactSheet.png`
- Unreal capture: `Saved/Automation/ReviewIsland/BloodAxeCairnVariants_A01_UnrealReview_Unlit.png`
- Current asset status: `Unreal import candidate`
- Initial review decision: approved to proceed to final texture/material pass
- Texture/material follow-up: `TEXTURE_MATERIAL_STATUS.md`
- Concept geometry audit: `CONCEPT_GEOMETRY_AUDIT.md`
- Current concept-geometry decision: requested changes

## Visual Comparison Result

The Unreal review capture preserves the DCC contact-sheet order, broad silhouette family, low/paired/vertical variation, oxide-red cloth accents, dark Blood Axe stone value range, and non-civilized Giant cairn read. No UCX collision proxy geometry is visible in the review capture, and the prior single-cairn review target is no longer blocking the batch view.

This result only compares the Unreal import against the DCC batch handoff. It does not prove that the batch matches the approved concept cairn geometry. The earlier conclusion that no geometry rebuild was required is superseded by `CONCEPT_GEOMETRY_AUDIT.md`.

## Texture Material Follow-Up

The shared BC/N/ORM texture/material candidate was authored and imported on 2026-07-03. The follow-up pass preserved the broad dark-stone, dirt-base, and oxide-red Blood Axe cloth read while adding shared candidate map support through the one-slot Unreal material.

- Texture proof sheet: `docs/assets/kits/KIT_GIA_BloodAxeCairnVariantBatch_A01/BloodAxeCairnVariants_A01_TextureReviewSheet.png`
- Close unlit capture: `docs/assets/kits/KIT_GIA_BloodAxeCairnVariantBatch_A01/BloodAxeCairnVariants_A01_TextureReview_Close_Unlit.png`
- Close lit capture: `docs/assets/kits/KIT_GIA_BloodAxeCairnVariantBatch_A01/BloodAxeCairnVariants_A01_TextureReview_Close_Lit.png`
- Texture/material status: texture/material candidate pending Flamestrike review

The close captures are useful for identifying the mismatch, but they are not acceptable as final texture/material approval evidence until the geometry matches the approved concept targets. The batch remains `Unreal import candidate` and is still not final visual approval.

## Observed Limits

- The Unreal proof is an overview batch frame, not a final close-up beauty review.
- The current material is a shared BC/N/ORM texture/material candidate, not final Flamestrike-approved texture art.
- Small cloth, edge wear, ash, mud, rawhide, and stone-grain reads may still need review-driven polish.
- The current batch reads as generalized A1-inspired cairn variants, not confirmed A2-A5 or B1-B5 concept matches.
- Round soil bases and simplified stone piles do not match the stronger authored concept geometry.
- Flamestrike has not given final visual approval for the imported batch.

## Texture And Material Pass Requirements

- Author shared `T_GIA_BloodAxeCairnVariants_A01_BC`, `T_GIA_BloodAxeCairnVariants_A01_N`, and `T_GIA_BloodAxeCairnVariants_A01_ORM`.
- Preserve the current broad dark-stone and muted oxide-red value structure.
- Add hand-painted stone grain, chipped edges, soot, ash, mud contact darkening, cloth fiber, rawhide wear, and subtle iron/bone accents through texture detail rather than extra modeled micro-detail.
- Keep material slots at 1 unless a later approved hero variant justifies a split.
- Do not add emissive effects, route markings, readable symbols, UI arrows, waypoint glow, quest paint, or gameplay-colored material states.

## Boundary

This review does not promote any asset to `Fully game-ready`, `Approved library asset`, `Gameplay validated asset`, or final visual approval. The batch remains `Unreal import candidate` and now carries a concept-geometry requested-changes gate.
