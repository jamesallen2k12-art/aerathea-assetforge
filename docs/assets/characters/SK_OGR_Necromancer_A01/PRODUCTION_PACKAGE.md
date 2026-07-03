# SK_OGR_Necromancer_A01 Production Package

## 1. Art Direction Summary

- Asset name: `SK_OGR_Necromancer_A01`
- Asset type: Skeletal Mesh class outfit / Ogre caster class package
- Parent body: `SK_OGR_Base_A01`
- World: Aerathea
- Theme: Ogre battlefield necromancer, grave-cairn caster, corpse-war ritualist
- Primary source references: `OgreNecromancer.png`, `OgreNecropolis.png`, `OgreMale2.png`, `SK_OGR_Base_A01`
- Current status: first-pass DCC source, FBX export, Unreal skeletal import, material instances, physics asset, anim Blueprint, sockets, startup review placement, validation, and build/import status complete; final art polish and animation set pending
- Shared final-art fit source: `docs/assets/kits/KIT_GNM_OGR_RivalryEncounter_A01/OGRE_SHARED_RIG_FINAL_ART_FIT_PLAN.md`; this class remains bound to `/Game/Aerathea/Characters/Ogres/Base/SK_OGR_Base_Male_A01_Skeleton` and should be the fourth class overlay fit after Shaman.

Ogre Necromancers are grim battlefield casters who turn casualties, grave cairns, and corpse trophies into weapons. They are still Ogres first: huge, broad, aggressive, and physically terrifying. Their class identity is defined by grave-green lantern magic, skull belts, corpse-war trophies, tombstone-like armor plates, blackened iron, torn dark cloth, bone spikes, and a heavy staff or grave-lantern focus.

This class must stay visually separate from Ogre Shamans. Necromancer magic is green-black, corpse-bound, and grave-cairn based; Shaman magic is ember-orange, storm-white, and ritual-cairn elemental.

## 2. Gameplay Purpose

- Supports Ogre player/NPC necromancer identity.
- Adds enemy commanders, graveyard elites, warband support casters, and necropolis quest NPCs.
- Establishes sockets and animation hooks for corpse-raise, drain, curse, green-black channel, and undead command gestures.
- Provides source direction for future `KIT_OGR_Necropolis_A01`, `SM_OGR_GraveLantern_A01`, `SM_OGR_BoneTotem_A01`, and necropolis VFX/material packages.
- Gives the Ogre lineup a darker magical class that is not Teknomancy and not shamanism.

## 3. Silhouette Notes

- Preserve Ogre base scale: females 10'0"-10'6", males 10'4"-11'0".
- Use a massive male baseline first at roughly 330 cm, with modular fit notes for female Ogres.
- Primary read: huge Ogre torso, heavy skull belt, tall grave-lantern staff, bone shoulder trophies, torn black cloth, tombstone plates, and a glowing cast hand.
- Staff should include a large lantern cage, skull housing, or grave marker head with green-black light.
- Armor should feel like grave metal and scavenged tomb plates, not polished robes.
- Hanging corpse-war trophies should be large silhouette clusters, not many tiny trinkets.
- Avoid Teknomancy reactors, precise machinery, warm shamanic rune wheels, or noble priestly elegance.

## 4. Scale Notes

- Author in centimeters at full Ogre scale.
- Male review baseline: 330 cm.
- Female fit target: 315 cm after male class silhouette is approved.
- Staff target height: 350-420 cm.
- Lantern/grave focus target: 65-100 cm tall or wide enough to read above the hand.
- Skull and bone trophies should be oversized and readable through LOD1.

## 5. Materials And Color Palette

| Material family | Palette | Use |
| --- | --- | --- |
| Ogre skin | ash-brown, gray-umber, corpse-pale scar tissue, bruise red | Exposed body, face, hands |
| Grave cloth | black, soot brown, dirty gray, rotten dark red | Skirt, wraps, torn cloth |
| Bone trophies | yellow ivory, gray bone, cracked white, smoke stained | Skulls, ribs, trophy chains |
| Tomb metal | blackened iron, tarnished steel, dull bronze, corroded green | Armor plates, staff cage, chains |
| Cairn stone | dark slate, grave gray, moss-stained stone | Tombstone plates, necropolis charms |
| Necromantic glow | grave green, sickly yellow-green, black-green core | Staff lantern, cast hand, skull eyes, drain/raise VFX |

Keep emissive focused. The staff lantern, cast hand, skull eyes, and corpse-raise sockets can glow, but the whole character should not become a green silhouette.

## 6. Concept Image Prompt

Create an original stylized fantasy MMORPG character production sheet of `SK_OGR_Necromancer_A01`, an Ogre Necromancer for the world of Aerathea. The design should emphasize a massive broad 10-11 ft Ogre body, skull belt, bone shoulder trophies, tombstone-like armor plates, torn black grave cloth, a huge grave-lantern staff with green-black magic, corpse-war trophies, tarnished blackened iron, dark cairn necropolis identity, and the gameplay role of a curse, drain, and corpse-raise battlefield caster. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, sparing emissive accents, and MMO-friendly production design. Present it as a character production sheet with front, side, back, three-quarter view, staff/lantern callout, skull trophy callout, socket callouts, material swatches, and scale beside an Ogre Shaman and Ogre Warrior. Avoid copied franchise designs, polished wizard robes, precise gnomish machinery, warm shamanic rune language, excessive micro-detail, text, and watermarks.

## 7. Modeling Notes

- Build modular class gear over `SK_OGR_Base_A01`; do not duplicate the base body sculpt unless a fit pass requires a class-specific body mesh.
- Model real geometry for the grave-lantern staff, skull belt, large bone trophies, tombstone plates, heavy chains, shoulder guard, large cloth strips, bracers, and boot bands.
- Use texture and normal maps for small cracks, bone pores, rust, cloth weave, tiny runes, dried grime, scratches, and minor chain wear.
- Staff and lantern must clear walk, run, drain cast, corpse raise, curse gesture, and hit-react poses.
- Keep the class silhouette tall and ominous without turning into a thin robed wizard; the Ogre body mass stays dominant.
- Avoid many small dangling bones that will skin poorly or disappear into noisy LODs.

## 8. Texture And Material Notes

Texture maps:

- `T_OGR_Necromancer_A01_BC`
- `T_OGR_Necromancer_A01_N`
- `T_OGR_Necromancer_A01_ORM`
- `T_OGR_Necromancer_A01_E`

Material slots:

1. Base Ogre skin/body inherited from `SK_OGR_Base_A01`.
2. `MI_OGR_Necromancer_A01_GraveCloth`
3. `MI_OGR_Necromancer_A01_BoneTrophies`
4. `MI_OGR_Necromancer_A01_TombMetal`
5. Optional `MI_OGR_Necromancer_A01_NecroGlow`

Packed ORM is required. Emissive map is limited to staff lantern, cast hand, skull eyes, curse runes, and corpse-raise/drain telegraph points.

## 9. Triangle Budget

- Class gear over base body LOD0 target: 22k-35k tris.
- Full equipped character target with base body: 55k-70k tris for hero/NPC review; normal gameplay target should stay closer to 50k-60k.
- Material slot target: 4-5 total for the fully equipped variant.

The grave-lantern staff, skull belt, tomb plates, and bone trophy clusters get geometry priority over small runes, tiny bone chips, and minor chain links.

## 10. LOD Plan

- LOD0: full Ogre body, grave-lantern staff, skull belt, bone trophies, tomb plates, cloth strips, bracers, socket markers.
- LOD1: simplify cloth strips, secondary bone clusters, chain bevels, and small plate cuts.
- LOD2: merge trophy clusters, remove small chains, reduce lantern cage bevels, simplify torn cloth.
- LOD3: preserve broad Ogre body, staff/lantern silhouette, skull belt mass, tomb-plate shoulder read, and green-black glow color blocks.

Never reduce the Ogre body mass, staff lantern, skull belt, or tomb-plate shoulder silhouette before small trophy detail.

## 11. Collision Notes

- Use the Ogre character capsule from `SK_OGR_Base_A01` for movement.
- Equipped outfit collision disabled by default.
- Staff uses simplified auxiliary collision only for weapon traces, blocking preview, or ragdoll contact if needed.
- Large trophy clusters should use simplified collision only if needed for ragdoll readability.
- Curse, drain, and corpse-raise effects should use socket-driven traces and gameplay volumes, not mesh detail collision.

## 12. Animation Notes

Required first-pass class poses:

- Idle grave-channel stance.
- Staff raise.
- Corpse-raise cast.
- Soul-drain channel.
- Curse gesture.
- Green-black channel loop.
- Undead command gesture.
- Staff ground plant.
- Heavy hit react.
- Death.

Socket requirements:

- `hand_r_staff`
- `hand_l_cast`
- `hand_l_offhand`
- `staff_lantern_fx`
- `staff_ground_fx`
- `skull_belt_fx`
- `back_trophy_fx`
- `vfx_cast_hand_l`
- `vfx_cast_hand_r`
- `vfx_necro_orb`
- `vfx_soul_drain`
- `vfx_corpse_raise`
- `vfx_eye_l`
- `vfx_eye_r`

## 13. Unreal Import Notes

- Asset type: Skeletal Mesh class outfit / gear configuration.
- Primary mesh: `SK_OGR_Necromancer_A01`.
- Parent body: `SK_OGR_Base_A01`.
- Skeleton: use `/Game/Aerathea/Characters/Ogres/Base/SK_OGR_Base_Male_A01_Skeleton` for the first male fit unless the final Ogre base skeleton is renamed.
- Physics asset: inherit base physics; add simplified staff/large trophy auxiliary bodies only if needed.
- Animation Blueprint: `ABP_OGR_Necromancer_A01`, derived from future Ogre base locomotion.
- Unreal path: `/Game/Aerathea/Characters/Ogres/Necromancer/`.
- Scale: centimeters, 1 Unreal unit = 1 cm.
- Pivot: inherited from base body at ground center between feet.
- Material slot count: 4-5.

## 14. Folder And Naming Recommendation

- Docs: `docs/assets/characters/SK_OGR_Necromancer_A01/`
- Source: `SourceAssets/Blender/Characters/Ogres/Necromancer/SK_OGR_Necromancer_A01/`
- Export: `SourceAssets/Exports/Characters/Ogres/Necromancer/SK_OGR_Necromancer_A01/`
- Unreal: `/Game/Aerathea/Characters/Ogres/Necromancer/`
- Materials: `MI_OGR_Necromancer_A01_*`
- Textures: `T_OGR_Necromancer_A01_*`

Related follow-up assets:

- `SM_OGR_GraveLantern_A01`
- `SM_OGR_BoneTotem_A01`
- `SM_OGR_GraveCairn_A01`
- `KIT_OGR_Necropolis_A01`

## 15. Quality Gate Checklist

- Reads as a broad 10-11 ft Ogre, not a tall human caster.
- Final art follows the Ogre shared rig fit plan and remains bound to the validated male Ogre skeleton.
- Necromancer silhouette is distinct from Shaman and Teknomancer at MMO camera distance.
- Grave-cairn, skull, bone, black cloth, and green-black magic language is clear.
- Glow is focused on necromantic staff/hand/skull telegraphs, not the whole character.
- Major staff, lantern, skull, bone, and tomb-plate shapes are real geometry; fine decay detail stays in maps.
- Triangle budget, material slots, texture maps, LOD plan, sockets, collision, animation notes, and Unreal paths are included.
