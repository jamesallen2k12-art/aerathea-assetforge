# SK_ABY_BulwarkDemon_A01 Production Package

## Art Direction Summary

- Asset name: `SK_ABY_BulwarkDemon_A01`
- Asset type: Skeletal Mesh creature / shield elite
- Parent kit: `KIT_ABY_ShadowFlame_A01`
- Source concepts: `AbyssalDemon13.png`, `AbyssalDemon4.png`
- Current status: Concept direction proposed; approval pending before DCC build

A shield-bearing Abyss elite that advances through fire and broken wards. It should contrast with the agile reaver by using a broad shield, heavy stance, and dark defensive magic.

## Gameplay Purpose

Frontline elite for guarding casters, anchoring troop groups, shield-bashing players, and forcing positional attacks. Useful for testing shield sockets and defensive VFX.

## Silhouette Notes

Primary read is a broad demon with a large abyssal shield and one heavy weapon or claw. Preserve shield slab, horn crest, heavy shoulders, and braced stance.

## Scale Notes

Height: 260-340 cm. Shield height: 180-240 cm. Author in centimeters with pivot at ground center.

## Materials And Color Palette

Scorched basalt shield face, charred iron rim, blackened bone horns, ember cracks, green or violet ward glow, ash cloth straps.

## Concept Image Prompt

Create an original stylized fantasy MMORPG enemy production sheet of an Abyss Bulwark Demon for Aerathea. The design should emphasize a broad horned shield-bearing silhouette, scorched basalt shield slab, charred iron armor, heavy braced stance, blackened bone horns, ember fissures, green or violet ward glow, defensive elite mood, and shield enemy gameplay role. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, sparing emissive shield and eye accents, and MMO-friendly production design. Present it as a turnaround with shield front/back detail, bash pose, material swatches, and scale beside a 180 cm humanoid.

## Modeling Notes

Model body, shield slab/rim, horns, shoulders, boots, gauntlets, major armor, and weapon/claw as geometry. Texture small shield cracks, pitted iron, cloth fray, rune scratches, and minor spikes.

## Texture And Material Notes

Material slots: body/armor, shield, emissive ward accents. Maps: `T_ABY_BulwarkDemon_A01_BC`, `T_ABY_BulwarkDemon_A01_N`, `T_ABY_BulwarkDemon_A01_ORM`, `T_ABY_BulwarkDemon_A01_E`.

## Triangle Budget

LOD0: 32k-44k tris. LOD1: 20k-28k. LOD2: 10k-15k. LOD3: 3k-6k.

## LOD Plan

Preserve shield slab, horn crown, heavy stance, and shoulder mass. Reduce small spikes, shield interior straps, finger detail, minor bevels, and cloth strips first.

## Collision Notes

Use humanoid movement capsule. Shield block uses gameplay traces or sockets, not blocking mesh collision. Physics bodies for body, limbs, shield proxy, and weapon/claw trace.

## Animation Notes

Idle brace, combat walk, shield raise, shield bash, heavy swing, guard caster, stagger from rear, hit shield, hit body, death, summon arrival.

## Unreal Import Notes

- Unreal folder: `/Game/Aerathea/Creatures/Abyss/Elites/BulwarkDemon/`
- Skeletal mesh: `SK_ABY_BulwarkDemon_A01`
- Skeleton: shared `SKEL_ABY_Humanoid_A01` if proportions allow
- Physics asset: `PHYS_ABY_BulwarkDemon_A01`
- Animation Blueprint: `ABP_ABY_BulwarkDemon_A01`
- Sockets: `socket_shield`, `socket_shield_vfx`, `socket_weapon_r`, `socket_head_vfx`, `socket_ground_rift`

## Folder And Naming Recommendation

- Docs: `docs/assets/creatures/SK_ABY_BulwarkDemon_A01/`
- Source: `SourceAssets/Blender/Creatures/Abyss/SK_ABY_BulwarkDemon_A01/`
- Export: `SourceAssets/Exports/Creatures/Abyss/SK_ABY_BulwarkDemon_A01/`

## Quality Gate Checklist

- Reads as defensive Abyss elite at gameplay distance.
- Shield silhouette stays dominant through LODs.
- Glow is limited to shield wards, eyes, or fissures.
- Triangle budget, maps, LODs, collision, animations, sockets, and Unreal path are defined.
- Not approved for DCC build until Flamestrike selects it.
