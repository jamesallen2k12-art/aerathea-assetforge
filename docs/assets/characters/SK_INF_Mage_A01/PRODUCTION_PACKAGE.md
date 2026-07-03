# SK_INF_Mage_A01 Production Package

## 1. Art Direction Summary

- Asset name: `SK_INF_Mage_A01`
- Asset type: Skeletal Mesh class outfit / Infernal caster class package
- Parent body: `SK_INF_Base_A01`
- World: Aerathea
- Theme: Balgoroth-chosen Infernal mage, abyssal brand-channeler, natural-weapon sorcerer
- Primary source references: `InfernalMaleSorcererLit.png`, `InfernalMaleSorcerer2.png`, `InfernalMaleSorcerer3.png`, `InfernalFemaleLit3.png`, `SK_INF_Base_A01`, `MI_INF_BrandGlowStates_A01`
- Review references: `docs/assets/characters/reviews/INFERNAL_ADULT_A03_BATCH_REVIEW.png`, `docs/assets/characters/reviews/INFERNAL_MALE_SORCERER_LIT_A03_REVIEW_SHEET.png`
- Current status: approved by Flamestrike on 2026-06-28 as the first Infernal class DCC child; first-pass DCC/Unreal review implementation imported and validated

`SK_INF_Mage_A01` defines the first adult Infernal class overlay. Infernal mages do not read as robed mortal scholars. They are predatory ritual casters who use their own bodies as the focus: horns, claws, wings, tail, eyes, brands, scar channels, and open hands. Armor, skull trophies, bone ornaments, obsidian plates, and ritual cloth are allowed, but mortal staffs, wands, and weapons should not become the primary silhouette. Combat spellcasting VFX are defined in `docs/assets/vfx/VFX_INF_AbyssalSpellcasting_A01/PRODUCTION_PACKAGE.md`.

All source imagery must pass through `docs/assets/characters/INFERNAL_VISUAL_CLEANSE_STANDARD.md`. Use A03-style cleanup as the default: preserve skulls, fire, lightning-like abyssal energy, glowing eyes, anger, and menace while removing artifact speckle, tiny repeated rivets, broken micro-chains, malformed micro-spikes, and noisy ground/sigil clutter.

## First-Pass Build Status

The approved first-pass review lane is complete. This pass establishes the Standard-band Mage class read at `213.49 cm` visible height including horns, the no-weapon casting silhouette, skull/bone belt mass, obsidian chest plate, ritual cloth panels, folded/half-spread wing mantle, tail line, hand/brand glow markers, shared tall Infernal skeleton binding, generated LOD0-LOD3, physics assignment, placeholder animation Blueprint, and startup-scene placement.

Generated and imported review files:

- Blender source: `SourceAssets/Blender/Characters/Infernals/Mage/SK_INF_Mage_A01/SK_INF_Mage_A01.blend`
- FBX export: `SourceAssets/Exports/Characters/Infernals/Mage/SK_INF_Mage_A01/SK_INF_Mage_A01.fbx`
- DCC proof render: `Saved/Automation/InfernalMageReview/SK_INF_Mage_A01_DCCReview.png`
- Unreal skeletal mesh: `/Game/Aerathea/Characters/Infernals/Mage/SK_INF_Mage_A01`
- Shared skeleton: `/Game/Aerathea/Characters/Infernals/Base/SK_INF_Base_Tall_A01_Skeleton`
- Startup actor: `AET_PROD_INF_Mage_A01`

Validation is passing:

- Focused validator: visible height `213.49 cm`, bounds radius `183.37 cm`, `21` required sockets present.
- Startup validator: `161 assets`, `50 expected actors`, `25 ground tiles`.

This is not final art. Use it as the locked production foundation for final sculpt, retopo, UVs, authored textures, tuned physics, real animation, and socket-driven VFX.

## 2. Gameplay Purpose

- Supports the Infernal mage playable/NPC class identity.
- Establishes a caster silhouette that obeys the Infernal natural-weapon doctrine.
- Provides hooks for abyssal bolt, brand-channel, invisible-sight reveal, regeneration flare, wing-mantle cast, and worthiness judgment rituals.
- Connects adult Infernal bodies to `MI_INF_BrandGlowStates_A01`, `VFX_INF_WorthinessJudgment_A01`, and `VFX_INF_AbyssalSpellcasting_A01`.
- Creates the first starter class variant after `SK_INF_Base_A01` and `SK_INF_Lesser_A01`.

## 3. Silhouette Notes

- Preserve the race read first: horn crown, large leathery wings, long thick tail, black claws, reddish skin, predatory upright posture.
- Primary mage read: open clawed casting hands, bright eyes, chest/forearm/hand brand channels, wing mantle or half-spread, ritual skirt or robe strips, skull/bone belt, and focused abyssal hand magic.
- Use the Standard, Greater, and Exalted adult bands first. Compact mages are allowed later, but the first package should prove the common adult and elite caster silhouettes.
- Major skull belts, bone pauldrons, horned chest pieces, and obsidian ornaments are acceptable as villain hierarchy cues.
- Avoid staff-dependent wizard silhouettes, full mortal robes, book props, weapon-centered poses, or action poses that crop the feet/wings.
- Keep spell circles and floor sigils secondary. They may support review boards, but the character must read without them.

## 4. Scale Notes

- Adult canon range: 5'0"-9'0" / 152-274 cm.
- First class-fit target: Standard adult 190-203 cm and Greater adult 230-244 cm.
- Exalted leader variant target: 260-274 cm if a named cult lord or boss mage is approved.
- Wings must clear folded navigation and half-spread cast poses.
- Tail must remain thick enough to read behind robes/cloth and must not be hidden by skirt strips.
- Horns and wing tips must stay inside production sheet framing.

## 5. Materials And Color Palette

| Material family | Palette | Use |
| --- | --- | --- |
| Infernal skin | ember red, ash red, crimson, dark umber | exposed body, face, hands, tail |
| Horn/claw | black keratin, charcoal bone, worn dark tips | horns, hands, feet, tail hooks |
| Wings | dark leather, red-brown membrane, blackened leading fingers | folded mantle, half-spread cast, intimidation poses |
| Ritual cloth | charcoal black, ash cloth, burnt red, soot brown | skirt strips, wraps, hanging panels |
| Armor/ornament | blackened iron, obsidian, scorched bronze, aged bone | pauldrons, belts, chest plates, skull/bone hierarchy cues |
| Mage glow | ember orange, deep red, focused violet core | eyes, brands, hands, chest channel, spell impact telegraphs |

Glow must be powerful and readable without becoming constant full-body fire. The strongest emissive points are eyes, hand sigils, brand intersections, chest/forearm channels, and major spell events.

## 6. Concept Image Prompt

Create an original stylized fantasy MMORPG character production sheet of `SK_INF_Mage_A01`, an Infernal Mage for the world of Aerathea. The design should emphasize a mortal-descended demonic caster blessed by Balgoroth, reddish skin, black claws, required horns, large leathery wings, a long thick tail, open clawed spellcasting hands, glowing eyes, chest and forearm brand channels, skull and bone villain hierarchy ornaments, obsidian and blackened iron armor plates, ash-black ritual cloth, focused flame and lightning-like abyssal power, natural-weapon doctrine, and the gameplay role of a predatory mage who casts through body, brands, wings, tail, and claws rather than mortal weapons. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, focused emissive accents, and MMO-friendly production design. Present it as a clean character production sheet with front, side, back, three-quarter view, folded and half-spread wing callouts, hand-cast callouts, brand mask callouts, skull/bone ornament callouts, socket callouts, material swatches, and scale beside Standard and Greater Infernal body bands. Clean the design for production readability: full body visible, feet and wings uncropped, readable midtone lighting, clear separation between red skin, black armor, dark wings, and background. If the source is too dark, start from a roughly 30 percent brighter pass. Use A03-style cleanup by default: reduce tiny repeated rivets, random speckle artifacts, malformed micro-spikes, broken micro-chains, torn-strip noise, dense spell clutter that hides anatomy, and photoreal surface garbage. Preserve skulls, bones, flame, lightning, glowing eyes, anger, and villain threat. Avoid copied franchise designs, gore, readable text, watermarks, staff-dependent wizard silhouettes, and weapon-focused poses.

## 7. Modeling Notes

- Build the class as modular mage gear over `SK_INF_Base_A01`; do not duplicate the base body sculpt unless a fit pass requires class-specific torso or hand variations.
- Model real geometry for large shoulder plates, skull belt, major bone/horn ornaments, obsidian chest plate, ritual cloth strips, bracers, claw caps if used, and large raised scar/brand ridges only when they affect silhouette.
- Use texture and normal maps for tiny rivets, small scratches, skin cracks, membrane veins, small brand lines, cloth weave, leather wear, micro chains, and minor ornament scratches.
- Preserve clawed hands for open palm, hooked hand, brand-channel, and spell-release poses.
- Wing mantle should have folded, half-spread cast, intimidation flare, and hit-react clearance.
- Keep cloth strips and hanging chains large and few enough to skin cleanly.
- Do not model dense tiny spell circles around the body; use VFX or material overlays for active casts.

## 8. Texture And Material Notes

Texture maps:

- `T_INF_Mage_A01_BC`
- `T_INF_Mage_A01_N`
- `T_INF_Mage_A01_ORM`
- `T_INF_Mage_A01_E`
- Optional shared mask dependency: `T_INF_BrandGlow_A01_Mask`

Material slots:

1. Base Infernal skin/body inherited from `SK_INF_Base_A01`.
2. `MI_INF_Mage_A01_RitualCloth`
3. `MI_INF_Mage_A01_ObsidianArmor`
4. `MI_INF_Mage_A01_BoneOrnaments`
5. `MI_INF_Mage_A01_AbyssalGlow`

Use `MI_INF_BrandGlowStates_A01` for inactive, smolder, trial active, accepted, rejected, and sorcerer focus states. Packed ORM is required. Emissive map is limited to eyes, brands, hand magic, chest channels, wing-root pulses, and selected spell telegraph points.

## 9. Triangle Budget

- Class gear over base body LOD0 target: 12k-24k tris.
- Full equipped Standard/Greater character with base body: 42k-62k tris.
- Exalted named leader variant may reach 65k tris if wing mantle, skull hierarchy, and ritual armor justify it.
- Material slot target: 4-5 total for the fully equipped class variant.
- First-pass review import uses seven blockout material families for readability: skin, horn/claw, wing, ritual cloth, obsidian armor, bone ornaments, and abyssal glow. Final art should consolidate toward the 4-5 slot target where practical.

Geometry priority goes to horns, claws, wings, tail, major armor plates, skull belt, hand silhouettes, and readable wing mantle. Tiny rivets, speckles, micro-chains, small scratches, and small brand filigree must stay in maps or VFX.

## 10. LOD Plan

- LOD0: full base body, mage gear, skull/bone hierarchy pieces, wing mantle, major cloth strips, hand brand channels, socket markers.
- LOD1: simplify cloth strips, secondary bone pieces, armor bevels, and small ornament clusters.
- LOD2: merge ornament clusters, reduce skull/bone belt complexity, simplify wing membrane edge cuts, remove minor chains.
- LOD3: preserve body height, horn crown, folded wing mass, tail line, clawed hands, skull/bone belt mass, and broad glow color blocks.

Never reduce horns, wings, tail, black claws, hand-cast silhouette, or major skull/bone hierarchy before small decoration.

## 11. Collision Notes

- Use the Infernal base movement capsule from `SK_INF_Base_A01`.
- Equipped class gear collision disabled by default.
- Wings and tail use base auxiliary bodies; class cloth/ornaments should not add blocking collision.
- Spell gameplay uses socket-driven traces, cones, projectiles, and ability volumes, not mesh collision.
- Optional boss/leader skull pauldron or wing mantle bodies should be simplified and disabled for normal movement.

## 12. Animation Notes

Required first-pass class poses:

- Idle predatory caster.
- Idle controlled rage.
- Brand-channel loop.
- Two-hand abyssal bolt.
- One-hand claw cast.
- Wing-mantle cast.
- Invisible-sight reveal.
- Regeneration flare.
- Worthiness judgment gesture.
- Tail counterbalance cast.
- Leap or hover-cast anticipation.
- Heavy hit react.
- Death.

Socket requirements:

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

## 13. Unreal Import Notes

- Asset type: Skeletal Mesh class outfit / gear configuration.
- Primary mesh: `SK_INF_Mage_A01`.
- Parent body: `SK_INF_Base_A01`.
- Skeleton: use the final Infernal base skeleton; first-pass fit may use `/Game/Aerathea/Characters/Infernals/Base/` imported `SK_INF_Base_*` skeletons until naming is locked.
- Physics asset: inherit Infernal base physics; add simplified bodies only for large mage mantle pieces if needed.
- Animation Blueprint: `ABP_INF_Mage_A01`, derived from future Infernal base locomotion.
- Unreal path: `/Game/Aerathea/Characters/Infernals/Mage/`.
- Scale: centimeters, 1 Unreal unit = 1 cm.
- Pivot: inherited from base body at ground center between feet.
- Material slot count: 4-5.

## 14. Folder And Naming Recommendation

- Docs: `docs/assets/characters/SK_INF_Mage_A01/`
- Source: `SourceAssets/Blender/Characters/Infernals/Mage/SK_INF_Mage_A01/`
- Export: `SourceAssets/Exports/Characters/Infernals/Mage/SK_INF_Mage_A01/`
- Unreal: `/Game/Aerathea/Characters/Infernals/Mage/`
- Materials: `MI_INF_Mage_A01_*`
- Textures: `T_INF_Mage_A01_*`

Related follow-up assets:

- `VFX_INF_AbyssalSpellcasting_A01`
- `ABP_INF_Mage_A01`
- `MI_INF_BrandGlowStates_A01`
- `KIT_INF_BalgorothCult_A01`
- `docs/assets/characters/SK_INF_Base_A01/ANIMATION_HANDOFF.md`

## 15. Quality Gate Checklist

- Reads as an Infernal mage, not a mortal wizard, true Abyss demon, or weapon user.
- Approved first Infernal class child; DCC follows this package, its modeling handoff, `VFX_INF_AbyssalSpellcasting_A01`, and `SK_INF_Base_A01/ANIMATION_HANDOFF.md`.
- Horns, wings, thick tail, black claws, red skin, and predatory posture remain clear.
- Skull/bone villain hierarchy, flame, lightning-like energy, eye glow, and brand channels are preserved.
- A03 cleanse standard is applied before using source images as production targets.
- Major forms are real geometry; tiny rivets, speckles, micro-chains, minor scratches, and small brand lines stay in maps/VFX.
- Triangle budget, material slots, texture maps, LOD plan, sockets, collision, animation notes, and Unreal paths are included.
- First-pass DCC/Unreal review implementation is validated; final sculpt, retopo, UVs, authored textures, tuned physics, VFX hookup, and animation are still required before final visual approval.
