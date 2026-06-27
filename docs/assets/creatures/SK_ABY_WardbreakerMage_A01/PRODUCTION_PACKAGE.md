# SK_ABY_WardbreakerMage_A01 Production Package

## Art Direction Summary

- Asset name: `SK_ABY_WardbreakerMage_A01`
- Asset type: Skeletal Mesh creature / caster enemy
- Parent kit: `KIT_ABY_ShadowFlame_A01`
- Source concepts: `AbyssalDemon11.png`, `AbyssalDemon3.png`, `AbyssalTroops1.png`
- Generated lore references: `AET_LORE_ABYSS_04_SableVeilNarax.png`, `AET_LORE_ABYSS_09_CinderEyedHierophant.png`
- Current status: Concept direction proposed; approval pending before DCC build

An Abyss caster that breaks wards, binds lesser entities, and opens rifts. It should read as a ritual threat with clear hand/sigil sockets and a tall robed silhouette.

## Gameplay Purpose

Caster enemy for shield stripping, summons, area denial, binding circles, and encounter escalation. Serves as the first Abyss magic user before boss casters.

## Silhouette Notes

Primary read is a tall horned caster with floating sigil discs or hand-cast void glyphs. Preserve robe column, horn crown, hand spread, and twin magic circles.

## Scale Notes

Height: 240-320 cm. Floating sigil radius: 50-120 cm. Author in centimeters with pivot at ground center.

## Materials And Color Palette

Charred robes, blackened bone mask or horns, smoky violet sigils, ember eyes, green or purple ward-breaking glow, dark iron ritual bands.

## Concept Image Prompt

Create an original stylized fantasy MMORPG enemy production sheet of an Abyss Wardbreaker Mage for Aerathea. The design should emphasize a tall robed horned caster silhouette, floating void sigils, outstretched clawed hands, charred robes, blackened bone mask, smoky violet ward-breaking magic, ember eyes, ritual binding mood, and caster/support enemy gameplay role. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, sparing emissive sigils, and MMO-friendly production design. Present it as a turnaround with casting pose, sigil callouts, material swatches, VFX sockets, and scale beside a 180 cm humanoid.

## Modeling Notes

Model body mass, horns, mask, large robe panels, shoulder mantle, hand claws, ritual bands, and optional sigil-disc meshes. Texture robe weave, small runes, ash stains, fine cracks, and scratches.

## Texture And Material Notes

Material slots: body/robes, bone/iron, emissive sigils. Maps: `T_ABY_WardbreakerMage_A01_BC`, `T_ABY_WardbreakerMage_A01_N`, `T_ABY_WardbreakerMage_A01_ORM`, `T_ABY_WardbreakerMage_A01_E`.

## Triangle Budget

LOD0: 28k-40k tris. LOD1: 18k-26k. LOD2: 9k-14k. LOD3: 3k-5k.

## LOD Plan

Preserve horn crown, robe column, hand spread, and sigil shapes. Reduce robe tears, small bands, finger detail, sigil bevels, and inner cloth layers first.

## Collision Notes

Use humanoid movement capsule. Floating sigils should not block movement. Physics bodies for head, chest, pelvis, limbs, robe proxy, and cast sockets.

## Animation Notes

Idle hover or grounded idle, ritual idle, walk, cast quick ward break, channel summon, ground rift, self shield, hit reactions, interrupt, death, portal spawn.

## Unreal Import Notes

- Unreal folder: `/Game/Aerathea/Creatures/Abyss/Casters/WardbreakerMage/`
- Skeletal mesh: `SK_ABY_WardbreakerMage_A01`
- Skeleton: shared `SKEL_ABY_Humanoid_A01` if proportions allow
- Physics asset: `PHYS_ABY_WardbreakerMage_A01`
- Animation Blueprint: `ABP_ABY_WardbreakerMage_A01`
- Sockets: `socket_hand_l_cast`, `socket_hand_r_cast`, `socket_sigil_l`, `socket_sigil_r`, `socket_head_vfx`, `socket_ground_rift`

## Folder And Naming Recommendation

- Docs: `docs/assets/creatures/SK_ABY_WardbreakerMage_A01/`
- Source: `SourceAssets/Blender/Creatures/Abyss/SK_ABY_WardbreakerMage_A01/`
- Export: `SourceAssets/Exports/Creatures/Abyss/SK_ABY_WardbreakerMage_A01/`

## Quality Gate Checklist

- Reads as caster and not as Dark Elf mage.
- Ward-breaking sigils are clear but not overbright.
- Robe silhouette, horn crown, and hand casts remain readable in LODs.
- Collision and VFX sockets are separated.
- Triangle budget, texture maps, LODs, animations, collision, sockets, and Unreal path are defined.
- Not approved for DCC build until Flamestrike selects it.
