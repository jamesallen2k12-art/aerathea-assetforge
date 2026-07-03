# SK_INF_Mage_A01 Modeling Handoff

## Purpose

Create the DCC source, class gear, brand-channel surface plan, socket plan, LODs, and Unreal import path for the Infernal Mage class package. The result should fit over `SK_INF_Base_A01` and prove the first Infernal caster silhouette without relying on mortal staffs, wands, books, or weapons.

Current implementation state: first-pass Blender source, FBX export, DCC review render, Unreal skeletal mesh import, generated LOD0-LOD3, sockets, physics asset, placeholder ABP, startup actor, focused validator, and startup validator are complete as of 2026-06-28. Final sculpt, retopo, authored UVs/textures, tuned physics, socket-driven VFX, and authored animation remain pending.

## Source References

- Production package: `docs/assets/characters/SK_INF_Mage_A01/PRODUCTION_PACKAGE.md`
- Infernal base package: `docs/assets/characters/SK_INF_Base_A01/PRODUCTION_PACKAGE.md`
- Infernal visual cleanse standard: `docs/assets/characters/INFERNAL_VISUAL_CLEANSE_STANDARD.md`
- Review index: `docs/assets/characters/reviews/INFERNAL_A03_CLEANSE_REVIEW_INDEX.md`
- A03 adult batch review: `docs/assets/characters/reviews/INFERNAL_ADULT_A03_BATCH_REVIEW.png`
- Source concepts:
  - `/home/Flamestrike/Desktop/Aerathea/Aerathea Creative/ASSET CONCEPTS/InfernalMaleSorcererLit.png`
  - `/home/Flamestrike/Desktop/Aerathea/Aerathea Creative/ASSET CONCEPTS/InfernalMaleSorcerer2.png`
  - `/home/Flamestrike/Desktop/Aerathea/Aerathea Creative/ASSET CONCEPTS/InfernalMaleSorcerer3.png`
  - `/home/Flamestrike/Desktop/Aerathea/Aerathea Creative/ASSET CONCEPTS/InfernalFemaleLit3.png`
- Material dependency: `docs/assets/materials/MI_INF_BrandGlowStates_A01/PRODUCTION_PACKAGE.md`
- VFX dependency: `docs/assets/vfx/VFX_INF_WorthinessJudgment_A01/PRODUCTION_PACKAGE.md`
- Combat VFX dependency: `docs/assets/vfx/VFX_INF_AbyssalSpellcasting_A01/PRODUCTION_PACKAGE.md`
- Animation dependency: `docs/assets/characters/SK_INF_Base_A01/ANIMATION_HANDOFF.md`

## Production Target

- Asset: `SK_INF_Mage_A01`
- Type: Skeletal Mesh class outfit and caster overlay.
- Parent body: `SK_INF_Base_A01`.
- First fit targets: Standard adult 190-203 cm and Greater adult 230-244 cm.
- Optional later fit: Exalted 260-274 cm named leader variant.
- Unreal path: `/Game/Aerathea/Characters/Infernals/Mage/`
- DCC state: first-pass review implementation imported and validated; final art-model pass pending.

## Modeling Constraints

- Author at real scale in centimeters.
- Use existing Infernal base proportions, wing/tail/claw requirements, and skeleton direction.
- Model large readable forms: skull belt, obsidian chest plate, ritual cloth panels, large bone ornaments, shoulder plates, bracers, hand/claw silhouette, and raised major brand ridges if approved.
- Do not model tiny repeated rivets, artifact speckles, malformed micro-spikes, broken micro-chains, tiny brand filigree, dense floor sigils, or noisy magic circles.
- Keep hands open and readable for casting; avoid weapon grip defaults.
- Preserve folded wing navigation and half-spread mage cast clearance.
- Apply A03 cleanup interpretation to all concept references before sculpting details.

## Blender Setup

- Collection: `SK_INF_Mage_A01`
- Mesh groups:
  - `Infernal_Base_Reference`
  - `Mage_RitualCloth`
  - `Mage_ObsidianArmor`
  - `Mage_BoneSkullOrnaments`
  - `Mage_BrandRidges`
  - `Mage_GlowMarkers`
- Skeleton: inherit the final Infernal base skeleton when locked.
- Current first-pass skeleton: `/Game/Aerathea/Characters/Infernals/Base/SK_INF_Base_Tall_A01_Skeleton`.
- Add empties/socket markers for hands, eyes, chest brands, forearms, wing roots, tail tip, regeneration core, sorcerer focus, and worthiness mark.

## Modeling Sequence

1. Load `SK_INF_Base_A01` reference bodies and confirm Standard/Greater scale markers.
2. Block the mage silhouette in neutral three-quarter stance: horns, wings, tail, open hands, skull belt, ritual cloth, and obsidian chest/shoulder armor.
3. Add large skull/bone hierarchy ornaments and cloth panels before small surface treatment.
4. Add brand-channel ridges only where they affect silhouette; use texture masks for smaller marks.
5. Add socket empties for hands, eyes, chest, forearms, wing roots, tail tip, regeneration, sorcerer focus, and worthiness mark.
6. Build LOD0-LOD3 with horns, wing mantle, tail, claw hands, skull belt, and glow blocks preserved.
7. Export skeletal FBX after scale, silhouette, and socket placement review.

## Triangle Budget

- Class gear LOD0 target: 12k-24k tris.
- Full equipped Standard/Greater character with base body: 42k-62k tris.
- Exalted named leader variant: up to 65k tris only if approved.
- LOD1: 55-60 percent.
- LOD2: 25-35 percent.
- LOD3: 10-15 percent.

## Texture Deliverables

- `T_INF_Mage_A01_BC`
- `T_INF_Mage_A01_N`
- `T_INF_Mage_A01_ORM`
- `T_INF_Mage_A01_E`
- Optional shared mask: `T_INF_BrandGlow_A01_Mask`

Material instances:

- `MI_INF_Mage_A01_RitualCloth`
- `MI_INF_Mage_A01_ObsidianArmor`
- `MI_INF_Mage_A01_BoneOrnaments`
- `MI_INF_Mage_A01_AbyssalGlow`

## Collision Deliverables

- Base Infernal capsule and physics asset inheritance.
- Class outfit collision disabled by default.
- Optional simplified auxiliary bodies for large wing mantle or boss-only skull pauldrons.
- No per-chain, per-skull-chip, per-cloth-strip, or per-sigil collision.
- Spell traces and ability shapes must come from sockets and gameplay volumes.

## Export Targets

- Blender source: `SourceAssets/Blender/Characters/Infernals/Mage/SK_INF_Mage_A01/SK_INF_Mage_A01.blend`
- FBX export: `SourceAssets/Exports/Characters/Infernals/Mage/SK_INF_Mage_A01/SK_INF_Mage_A01.fbx`
- DCC proof render: `Saved/Automation/InfernalMageReview/SK_INF_Mage_A01_DCCReview.png`
- Unreal skeletal mesh: `/Game/Aerathea/Characters/Infernals/Mage/SK_INF_Mage_A01`
- Physics asset: `/Game/Aerathea/Characters/Infernals/Mage/PHYS_INF_Mage_A01`
- Animation Blueprint: `/Game/Aerathea/Characters/Infernals/Mage/ABP_INF_Mage_A01`
- Startup actor: `AET_PROD_INF_Mage_A01`

## Unreal Validation

- Imports at centimeter scale and matches the intended Standard/Greater Infernal body range.
- Binds to the final Infernal base skeleton or documented first-pass skeleton.
- Horns, wings, thick tail, black claws, open casting hands, and skull/bone hierarchy read at startup review distance.
- Required sockets exist:
  - `hand_l_cast`
  - `hand_r_cast`
  - `hand_l_claw`
  - `hand_r_claw`
  - `vfx_eye_l`
  - `vfx_eye_r`
  - `vfx_brand_chest`
  - `vfx_brand_forearm_l`
  - `vfx_brand_forearm_r`
  - `vfx_hand_l`
  - `vfx_hand_r`
  - `vfx_wing_root_l`
  - `vfx_wing_root_r`
  - `vfx_tail_tip`
  - `vfx_regen_core`
  - `vfx_sorcerer_focus`
  - `vfx_worthiness_mark`
- Emissive states can be driven by `MI_INF_BrandGlowStates_A01` or future mage VFX parameters.

2026-06-28 validation results:

- `Tools/Unreal/validate_infernal_mage.py` passed: visible height `213.49 cm`, bounds radius `183.37 cm`, and `21` sockets present.
- `Tools/Unreal/validate_startup_scene.py` passed with `161 assets`, `50 expected actors`, and `25 ground tiles`.

## Acceptance Checklist

- Infernal race traits remain dominant over class costume.
- Mage class reads through body, brands, claws, wings, tail, eyes, and hand magic rather than mortal weapons.
- A03 visual cleanse rules are followed.
- Major skull/bone villain cues are preserved without noisy micro-detail.
- Cloth, chains, and ornaments can skin cleanly through cast, wing, tail, and hit-react poses.
- LODs preserve horn crown, wing mantle, tail line, claw hands, skull belt, and broad glow blocks.
- Final sculpt, retopo, UVs, textures, skin weighting, physics tuning, VFX package, and animation set remain pending.
