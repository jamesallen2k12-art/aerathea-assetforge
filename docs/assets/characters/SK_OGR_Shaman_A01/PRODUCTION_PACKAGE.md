# SK_OGR_Shaman_A01 Production Package

## 1. Art Direction Summary

- Asset name: `SK_OGR_Shaman_A01`
- Asset type: Skeletal Mesh class outfit / Ogre caster class package
- Parent body: `SK_OGR_Base_A01`
- World: Aerathea
- Theme: Ogre primal shaman, cairn-channel caster, battlefield ritualist
- Primary source references: `OgreShaman.png`, `OgreShamanHut.png`, `OgreFemale2.png`, `SK_OGR_Base_A01`
- Current status: first-pass DCC source, FBX export, Unreal skeletal import, material instances, physics asset, anim Blueprint, sockets, startup review placement, validation, and build/import status complete; final art polish and animation set pending

Ogre Shamans are brutal battlefield mystics. They do not feel refined, scholarly, or nature-druidic. Their magic is instinctive and forceful: cairn stones, carved bone, hide wraps, storm charms, ember runes, ritual paint, and huge staffs used as both spell focus and weapon. They stand with the same broad Ogre mass as Warriors and Teknomancers, but their silhouette is defined by a ritual staff, rune wheel, dangling fetishes, fur and hide, stone charm plates, and a free casting hand.

This class must stay visually separate from Ogre Necromancers. Shaman glow is ember-orange, storm-white, and hot rune light; Necromancer glow is grave green and black.

## 2. Gameplay Purpose

- Supports Ogre player/NPC shaman identity.
- Adds battlefield support, disruption, and area control to Ogre warbands.
- Provides a caster counterpart to the Teknomancer and Warrior rivalry slices.
- Establishes sockets and animation hooks for cairn-channel casts, totem slams, storm/fire spells, and ritual chant loops.
- Provides source direction for future `SM_OGR_ShamanTotem_A01`, `SM_OGR_CairnRuneStone_A01`, and `SM_OGR_ShamanHut_A01`.

## 3. Silhouette Notes

- Preserve Ogre base scale: females 10'0"-10'6", males 10'4"-11'0".
- Use a massive male baseline first at roughly 330 cm, with modular fit notes for female Ogres.
- Primary read: bare or lightly armored broad torso, heavy belt, hide/fur skirt, thick boots, huge forearms, and a dominant ritual staff.
- Staff should include a stone/rune wheel or cairn disk near the head, large bone lashings, tooth charms, and dangling trophies.
- Add stone charm plates and hide wraps around belt, bracers, knees, and shoulders.
- One hand should read as open for casting, not always weapon-locked.
- Avoid Teknomancy reactors, pressure tanks, precision gears, grave-green necromancy lanterns, or corpse-war trophies as the primary read.

## 4. Scale Notes

- Author in centimeters at full Ogre scale.
- Male review baseline: 330 cm.
- Female fit target: 315 cm after male class silhouette is approved.
- Staff target height: 360-430 cm, tall enough to be readable above the Ogre shoulder line.
- Rune wheel/cairn disk target: 70-105 cm diameter.
- Charms and hanging trophies should remain large enough to read in LOD1, not tiny jewelry.

## 5. Materials And Color Palette

| Material family | Palette | Use |
| --- | --- | --- |
| Ogre skin | ash-brown, ochre, gray-umber, scar red | Exposed torso, face, hands |
| Hide and fur | dark brown, soot black, tan hide, dirty cream fur | Skirt, mantle, wraps, belt |
| Cairn stone | blue-gray stone, charcoal, ash, carved black stone | Rune plates, staff disk, talismans |
| Bone and teeth | aged bone, yellow ivory, smoke-stained white | Charms, trophies, staff binding |
| Metal | blackened iron, dull brass, dark steel | Bracers, boot bands, large rings |
| Shamanic glow | ember orange, hot amber, storm white, restrained blue-white | Rune wheel, staff head, cast hand, totem slam |

Keep emissive restrained and focused on runes, staff head, cast hand, eyes if needed, and major spell telegraph sockets.

## 6. Concept Image Prompt

Create an original stylized fantasy MMORPG character production sheet of `SK_OGR_Shaman_A01`, an Ogre Shaman for the world of Aerathea. The design should emphasize a massive broad 10-11 ft Ogre body, bare scarred torso, heavy hide and fur wraps, cairn-stone rune plates, carved bone fetishes, a huge ritual staff with a stone rune wheel, dangling tooth charms, ember-orange and storm-white spell glow, rough battlefield ritual culture, and the gameplay role of a primal support and area-control caster. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, sparing emissive accents, and MMO-friendly production design. Present it as a character production sheet with front, side, back, three-quarter view, staff callout, rune charm callout, socket callouts, material swatches, and scale beside an Ogre Warrior and Gnome Heavy Mek. Avoid copied franchise designs, polished druid elegance, precise gnomish machinery, grave-green necromancer language, excessive micro-detail, text, and watermarks.

## 7. Modeling Notes

- Build modular class gear over `SK_OGR_Base_A01`; do not duplicate base body sculpt unless a fit pass requires a class-specific body mesh.
- Model real geometry for the staff, rune wheel, major bone charms, large stone plates, broad fur mantle, belt slabs, bracers, boot bands, and large hanging fetishes.
- Use texture and normal maps for tiny scratches, hide grain, fine fur, stitching, small rune cuts, small teeth, minor bone chips, and soot stains.
- Staff and large charms must clear walk, run, staff slam, two-handed channel, and hit-react poses.
- Keep shaman gear rough and hand-bound: straps, lashings, uneven stone, hammered rings, and battlefield repairs.
- Avoid dense dangling clutter that will skin poorly or create noisy LODs.

## 8. Texture And Material Notes

Texture maps:

- `T_OGR_Shaman_A01_BC`
- `T_OGR_Shaman_A01_N`
- `T_OGR_Shaman_A01_ORM`
- `T_OGR_Shaman_A01_E`

Material slots:

1. Base Ogre skin/body inherited from `SK_OGR_Base_A01`.
2. `MI_OGR_Shaman_A01_HideFur`
3. `MI_OGR_Shaman_A01_StoneBone`
4. `MI_OGR_Shaman_A01_Metal`
5. Optional `MI_OGR_Shaman_A01_RuneGlow`

Packed ORM is required. Emissive map is limited to rune wheel, staff head, cast hand, eyes if needed, and major spell telegraphs.

## 9. Triangle Budget

- Class gear over base body LOD0 target: 18k-30k tris.
- Full equipped character target with base body: 50k-65k tris.
- Material slot target: 4-5 total for the fully equipped variant.

The staff, rune wheel, fur silhouette, and large charms get geometry priority over tiny straps, small teeth, and minor bone chips.

## 10. LOD Plan

- LOD0: full Ogre body, staff, rune wheel, fur/hide mantle, bracers, belt, large bone charms, socket markers.
- LOD1: simplify fur edge loops, belt bevels, small charm geometry, and secondary wraps.
- LOD2: merge charm clusters, reduce rune wheel bevels, remove small dangling pieces, simplify staff bindings.
- LOD3: preserve broad Ogre body, staff silhouette, rune-wheel disk, fur/hide mass, and warm rune color blocks.

Never reduce the Ogre body mass, staff head, or rune disk before small fetish detail.

## 11. Collision Notes

- Use the Ogre character capsule from `SK_OGR_Base_A01` for movement.
- Equipped outfit collision disabled by default.
- Staff uses simplified auxiliary collision only for weapon traces, blocking preview, or ragdoll contact if needed.
- Large dangling charms should not have individual collision.
- Spell effects should use socket-driven traces or area volumes, not mesh detail collision.

## 12. Animation Notes

Required first-pass class poses:

- Idle ritual stance.
- Staff ground plant.
- Cairn-channel cast.
- Totem or staff slam.
- Storm cast.
- Fire/ember cast.
- Ritual chant loop.
- Ward or group buff gesture.
- Heavy hit react.
- Death.

Socket requirements:

- `hand_r_staff`
- `hand_l_cast`
- `hand_l_offhand`
- `staff_head_fx`
- `staff_ground_fx`
- `staff_rune_wheel_fx`
- `belt_charm_fx`
- `vfx_cast_hand_l`
- `vfx_cast_hand_r`
- `vfx_chest_rune`
- `vfx_eye_l`
- `vfx_eye_r`
- `vfx_totem_slam`
- `vfx_storm_channel`

## 13. Unreal Import Notes

- Asset type: Skeletal Mesh class outfit / gear configuration.
- Primary mesh: `SK_OGR_Shaman_A01`.
- Parent body: `SK_OGR_Base_A01`.
- Skeleton: use `/Game/Aerathea/Characters/Ogres/Base/SK_OGR_Base_Male_A01_Skeleton` for the first male fit unless the final Ogre base skeleton is renamed.
- Physics asset: inherit base physics; add simplified staff auxiliary body only if needed.
- Animation Blueprint: `ABP_OGR_Shaman_A01`, derived from future Ogre base locomotion.
- Unreal path: `/Game/Aerathea/Characters/Ogres/Shaman/`.
- Scale: centimeters, 1 Unreal unit = 1 cm.
- Pivot: inherited from base body at ground center between feet.
- Material slot count: 4-5.

## 14. Folder And Naming Recommendation

- Docs: `docs/assets/characters/SK_OGR_Shaman_A01/`
- Source: `SourceAssets/Blender/Characters/Ogres/Shaman/SK_OGR_Shaman_A01/`
- Export: `SourceAssets/Exports/Characters/Ogres/Shaman/SK_OGR_Shaman_A01/`
- Unreal: `/Game/Aerathea/Characters/Ogres/Shaman/`
- Materials: `MI_OGR_Shaman_A01_*`
- Textures: `T_OGR_Shaman_A01_*`

Related follow-up assets:

- `SM_OGR_ShamanStaff_A01`
- `SM_OGR_CairnRuneStone_A01`
- `SM_OGR_ShamanTotem_A01`
- `SM_OGR_ShamanHut_A01`

## 15. Quality Gate Checklist

- Reads as a broad 10-11 ft Ogre, not a tall human caster.
- Shaman silhouette is distinct from Teknomancer and Necromancer at MMO camera distance.
- Cairn stone, bone, hide, fur, and ritual paint language is clear.
- Glow is warm rune/storm spell language, not grave-green necromancy or Gnome Tek.
- Major staff and charm shapes are real geometry; fine texture detail stays in maps.
- Triangle budget, material slots, texture maps, LOD plan, sockets, collision, animation notes, and Unreal paths are included.
