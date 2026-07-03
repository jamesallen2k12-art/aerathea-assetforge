# SK_OGR_Base_A01 Production Package

## Art Direction Summary

Ogres are a war-created race built around brutal battlefield mass, instinctual Teknomancy, and a constant drive to make weapons and armor bigger, louder, and harder to stop. They are not as tall as Giants, but they are much broader than most playable races: thick torsos, heavy arms, slab-like hands, dense legs, and a terrifying front-line presence. Their culture blends rough stone cairns, defensive walls, forge heat, scavenged metal, oversized mechanisms, shamanic fetishes, and necromantic war trophies.

They are fascinated by magic and technology, but their craft is not gnomish precision. Ogre Teknomancy should feel instinctive, overbuilt, dangerous, and passionate: massive coils, bolted plates, crude pressure tanks, rune-choked engines, oversized guns, heavy armor rigs, and battlefield repairs hammered into place. Ogres are jealous of Gnome Mekgineer craft, and conflicts between Ogre Teknomancers and Gnome Mek pilots should read as a legendary rivalry.

Current source concept scan: 41 Ogre-related PNG files, including body/class sheets, Teknomancy and Gnome Mek encounter references, settlement boards, interiors, fortifications, forge references, and necropolis/shamanic architecture.

Current final-art fit source: `docs/assets/kits/KIT_GNM_OGR_RivalryEncounter_A01/OGRE_SHARED_RIG_FINAL_ART_FIT_PLAN.md`. The 2026-06-28 shared-skeleton baseline validates the male Ogre base, Teknomancer, Warrior, Shaman, and Necromancer review meshes against `/Game/Aerathea/Characters/Ogres/Base/SK_OGR_Base_Male_A01_Skeleton`.

## Gameplay Purpose

Ogres support large-race player/NPC bodies, enemy warbands, faction settlements, and class variants:

- Warriors: huge melee bruisers with brutal weapons and heavy armor.
- Teknomancers: oversized weapon/armor inventors using crude magic-tech rigs.
- Shamans: primal spellcasters using cairn stones, bones, storm/fire charms, and ritual fetishes.
- Necromancers: grim battlefield casters using green-black magic, bone ornaments, and corpse-war trophies.

They do not care about honor as a social rule; they care about winning. Their gameplay identity should support raw pressure, siege strength, dirty tactics, and dangerous prototype gear.

## Silhouette Notes

- Females: 10'0"-10'6" tall, broad and heavily muscled, visibly smaller than male Ogres but still massive next to Minotaurs and Valar.
- Males: 10'4"-11'0" tall, extremely broad shoulders, barrel chest, long heavy arms, thick neck, heavy jaw, and oversized hands/feet.
- Posture should be powerful and forward-driving, not hunched caricature.
- Primary silhouette anchors: huge shoulders, heavy forearms, thick boots, waist-hung plates, massive belts, broad armor slabs, and either shamanic/necromantic charms or Teknomancy hardware.
- Class readability must remain strong from distance: Teknomancers need coils/tanks/tools; Shamans need cairn-stone and fetish language; Necromancers need bone, green-black magic, and corpse-war trophies; Warriors need simple brutal weapon mass.

## Scale Notes

- Female Ogre scale: 10'0"-10'6" / 305-320 cm.
- Male Ogre scale: 10'4"-11'0" / 315-335 cm.
- Ogres sit above Minotaurs and below Giants in production scale.
- Use Unreal centimeters. Base skeletal mesh should be authored at real scale with a shared Ogre skeleton and sex-specific proportion meshes.
- Door, stair, weapon, and camera tests must account for an 11 ft playable/NPC body. Ogre settlements can use oversized entries, heavy stone steps, broad platforms, and defensive walls sized around Ogre mass.

## Materials And Color Palette

- Skin: weathered gray, umber, ochre, or ash-brown tones with hand-painted roughness variation.
- Armor: blackened iron, dark steel, crude brass/copper, heavy riveted plates, scorched leather, chain, straps, and fur/hide.
- Teknomancy: oversized coils, pressure vessels, blunt pistons, glowing Aetherium cores, rune-stamped metal, crude conduits, and heat glow.
- Shamanic: cairn stone, carved bone, hide wraps, storm charms, embers, totems, and ritual paint.
- Necromantic: bone, tarnished iron, grave green glow, black cloth scraps, skull motifs, and corpse-war trophies.
- Settlement: giant cairn stones, rough stone walls, charred timber, furnace orange light, heavy gates, crude iron bands, and smoke-darkened masonry.

## Concept Image Prompt

Create an original stylized fantasy MMORPG concept image of an Ogre base body and class lineup for the world of Aerathea. The design should emphasize massive broad silhouettes, heavily muscled 10-11 ft bodies, crude blackened iron armor, rough stone cairn culture, oversized instinctive Teknomancy, shamanic charms, necromantic war trophies, battlefield intimidation, and a race created for war. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, sparing emissive accents for Aetherium cores, runes, shamanic fire, and necromantic magic, and MMO-friendly production design. Present it as a character concept sheet with female Ogre, male Ogre, Warrior, Teknomancer, Shaman, and Necromancer variants on a clean background. Avoid copying any existing franchise and avoid excessive micro-detail that would not translate to a mid-poly Unreal asset.

## Modeling Notes

- Build a shared Ogre skeletal base first, then sex-specific body meshes and modular class armor.
- Emphasize real geometry for the body mass, hands, feet, shoulder pads, belts, large armor plates, primary weapons, Teknomancy coils/tanks, cairn-stone charms, and large bone trophies.
- Use textures and normals for fine scratches, leather stitching, small rivets, cloth weave, minor runes, scars, and skin pores.
- Keep the base body clean enough to support Warrior, Teknomancer, Shaman, and Necromancer outfits without clipping.
- Hands and forearms need extra attention because oversized Ogre weapons and Teknomancy rigs will stress sockets and grip poses.

## Texture And Material Notes

- Base body: 2K texture set, 4K only for hero/NPC variants.
- Suggested base material slots: skin, eyes/teeth/nails, hair/fur/accessory.
- Outfit variants may add armor, leather/cloth, and emissive magic-tech material slots.
- Texture list:
  - `T_OGR_Base_A01_BC`
  - `T_OGR_Base_A01_N`
  - `T_OGR_Base_A01_ORM`
  - `T_OGR_Base_A01_E` for eyes, runes, Aetherium, shamanic fire, or necromantic effects only.
- Packed ORM: Occlusion/Roughness/Metallic.
- Keep emissive accents sparse and readable; do not turn the whole silhouette into glow.

## Triangle Budget

- Base body LOD0 target: 35k-55k tris per sex-specific body.
- Class armor LOD0 target: 12k-30k additional tris depending on role.
- Hero Teknomancer/Necromancer variants may reach 65k tris total only when justified by class readability.
- Material slot target: 3 for base body, 4-5 for fully geared class variants.

## LOD Plan

- LOD0: full body shape, face, hands, major armor, class-defining gear, sockets.
- LOD1: 55-60% triangle count; simplify small straps, small charms, minor plates, and secondary belts.
- LOD2: 25-35% triangle count; remove minor hanging pieces, small rivets, small bones, and most small mechanisms.
- LOD3: 10-15% triangle count; preserve body mass, shoulder width, head silhouette, major weapon/gear shape, and faction color blocks.
- Never reduce the broad Ogre silhouette before reducing small Teknomancy or charm detail.

## Collision Notes

- Use a large humanoid capsule per gameplay role. Initial male test capsule: radius 70-85 cm, half-height 168 cm. Female test capsule: radius 65-80 cm, half-height 160 cm.
- Add physics bodies for head, torso, pelvis, upper/lower arms, hands, upper/lower legs, feet, and large attached gear only when needed.
- Teknomancy backpacks, cannons, or tank rigs should use simplified auxiliary collision and socket rules, not per-bolt collision.
- Settlement scale tests should verify Ogre movement through gates, barracks, forge interiors, walls, and cairn defensives.

## Animation Notes

- Required base set: idle, walk, run, turn in place, jump/land or heavy step, hit react, death, interact, emote/roar.
- Combat: two-handed heavy swing, one-handed smash, shield shove, stomp, shoulder bash, and throw/launch.
- Teknomancer: crank/prime weapon, brace cannon, tool repair, overload cast, recoil, and rig failure reaction.
- Shaman: cairn-channel cast, totem slam, storm/fire cast, ritual chant.
- Necromancer: corpse-raise cast, drain cast, curse gesture, green-black channel loop.

## Unreal Import Notes

- Asset type: Skeletal Mesh.
- Primary asset name: `SK_OGR_Base_A01`.
- Skeleton: `SKEL_OGR_Base_A01`.
- Physics asset: `PHYS_OGR_Base_A01`.
- Animation Blueprint: `ABP_OGR_Base_A01`.
- Folder path: `/Game/Aerathea/Characters/Ogres/Base/`.
- Scale: centimeters, full production scale, no import scaling.
- Pivot: between feet at ground center.
- Collision: character capsule plus physics asset; gear collision only when gameplay requires it.
- Sockets:
  - `hand_l_weapon`, `hand_r_weapon`
  - `back_weapon`
  - `spine_teknomancy_pack`
  - `shoulder_l_large`, `shoulder_r_large`
  - `belt_front`, `belt_back`
  - `vfx_mouth`, `vfx_eye_l`, `vfx_eye_r`, `vfx_chest_core`
- Blueprint behavior: base body package only; class Blueprint logic belongs in follow-up class packages.

## Folder And Naming Recommendation

- Base package: `docs/assets/characters/SK_OGR_Base_A01/`.
- Unreal base folder: `/Game/Aerathea/Characters/Ogres/Base/`.
- Class follow-up packages:
  - `SK_OGR_Warrior_A01`
  - `SK_OGR_Teknomancer_A01`
  - `SK_OGR_Shaman_A01`
  - `SK_OGR_Necromancer_A01`
  - `KIT_OGR_Teknomancy_A01`
  - `KIT_OGR_CairnFortifications_A01`
  - `KIT_OGR_Necropolis_A01`

## Quality Gate Checklist

- Ogre female and male scales are clearly below Giants and above Minotaurs.
- Final art follows the shared rig fit plan without renaming or rescaling the validated skeleton.
- The body reads as heavily muscled, broad, and war-created, not just a tall human.
- Teknomancy reads as instinctive, oversized, and crude, not gnomish precision craft.
- Warrior, Teknomancer, Shaman, and Necromancer variants remain readable at MMO camera distance.
- Stone cairn, defensive wall, and fortress culture are represented in follow-up environment packages.
- Glow is limited to Aetherium cores, runes, shamanic fire/storm, necromantic effects, and eyes if needed.
- Triangle/material budgets are MMO-safe.
- LODs preserve the primary Ogre silhouette before reducing class detail.
- Unreal scale, sockets, collision, and folder paths are specified.
