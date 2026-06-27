# SK_ABY_CinderLord_A01 Production Package

## Art Direction Summary

- Asset name: `SK_ABY_CinderLord_A01`
- Asset type: Skeletal Mesh creature / boss-class Abyss lord
- Parent kit: `KIT_ABY_ShadowFlame_A01`
- Source concepts: `AbyssalLord3.png`, `AbyssalLord.png`, `AbyssalLord1.png`
- Generated lore references: `AET_LORE_ABYSS_01_Vorgath_CinderRuin.png`, `AET_LORE_ABYSS_07_KrazulWorldBreaker.png`
- Current status: Concept direction proposed; approval pending before DCC build

Boss-class Abyss commander with crown-like horns, world-burning aura, and war-host leadership. It should feel ancient, intelligent, and destructive, not merely oversized.

## Gameplay Purpose

Dungeon, raid, or world-event boss candidate. Provides summoning, troop command, area denial, binding-break mechanics, and cinematic scale reference for the Abyss hierarchy.

## Silhouette Notes

Primary read is a towering horn-crowned lord with huge shoulders, burning chest or crown core, weapon or staff option, and troops beneath it for scale. Preserve crown, scale, and chest/weapon glow.

## Scale Notes

Height: 700-1000 cm depending encounter tier. Weapon length: 500-850 cm. Author in centimeters with pivot under body mass. Requires scale sheet before DCC build.

## Materials And Color Palette

Scorched basalt flesh, molten ember fissures, charred iron armor, bone horn crown, red-orange cinder light, violet-black rift smoke, ash cloak fragments.

## Concept Image Prompt

Create an original stylized fantasy MMORPG boss creature production sheet of an Abyss Cinder Lord for Aerathea. The design should emphasize a towering horn-crowned commander silhouette, massive shoulders, burning chest or crown core, charred iron armor, scorched basalt flesh, molten ember fissures, violet-black rift smoke, ancient destructive intelligence, and boss-class gameplay role. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, sparing emissive core and eye accents, and MMO-friendly production design. Present it as a boss turnaround with scale beside troops and 180 cm humanoid, weapon options, material swatches, VFX sockets, and LOD callout.

## Modeling Notes

Model body mass, crown horns, armor plates, weapon/staff, claws, cloak chunks, and chest core as geometry. Texture small cracks, molten seams, ash, runes, scars, and armor pitting.

## Texture And Material Notes

Material slots: body, armor/horns, weapon, emissive core. Maps: `T_ABY_CinderLord_A01_Body_BC`, `T_ABY_CinderLord_A01_Body_N`, `T_ABY_CinderLord_A01_Body_ORM`, `T_ABY_CinderLord_A01_E`, plus armor/weapon sets if separated.

## Triangle Budget

LOD0: 70k-90k tris. LOD1: 45k-60k. LOD2: 22k-32k. LOD3: 8k-12k.

## LOD Plan

Preserve horn crown, huge shoulder mass, weapon/staff, chest core, and boss silhouette. Reduce small spikes, cloak tears, chain links, inner armor layers, finger detail, and minor horn cuts first.

## Collision Notes

Use boss movement capsule tuned by encounter. Physics bodies for head, horns as nonblocking hit proxies if needed, chest, pelvis, arms, legs, hands, weapon, and VFX core sockets. Raid collision must be designed with encounter rules.

## Animation Notes

Idle looming, command gesture, slow walk, weapon slam, sweeping strike, summon troops, binding break, cinder nova, stagger phase, kneel/phase change, death or banishment.

## Unreal Import Notes

- Unreal folder: `/Game/Aerathea/Creatures/Abyss/Lords/CinderLord/`
- Skeletal mesh: `SK_ABY_CinderLord_A01`
- Skeleton: `SKEL_ABY_BossLord_A01`
- Physics asset: `PHYS_ABY_CinderLord_A01`
- Animation Blueprint: `ABP_ABY_CinderLord_A01`
- Sockets: `socket_crown_vfx`, `socket_chest_core`, `socket_weapon_r`, `socket_summon_l`, `socket_summon_r`, `socket_ground_rift`

## Folder And Naming Recommendation

- Docs: `docs/assets/creatures/SK_ABY_CinderLord_A01/`
- Source: `SourceAssets/Blender/Creatures/Abyss/SK_ABY_CinderLord_A01/`
- Export: `SourceAssets/Exports/Creatures/Abyss/SK_ABY_CinderLord_A01/`

## Quality Gate Checklist

- Reads as Abyss lord, not a normal elite.
- Scale, crown, and commander role are unmistakable.
- Emissive effects are limited to core, eyes, weapon, and specific VFX sockets.
- Boss collision and animation needs are separated from art approval.
- Triangle budget, maps, LODs, collision, animations, sockets, and Unreal path are defined.
- Not approved for DCC build until Flamestrike selects it.
