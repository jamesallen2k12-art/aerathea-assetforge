# SK_ABY_BlackPikeTrooper_A01 Production Package

## Art Direction Summary

- Asset name: `SK_ABY_BlackPikeTrooper_A01`
- Asset type: Skeletal Mesh creature / enemy infantry
- Parent kit: `KIT_ABY_ShadowFlame_A01`
- Source concepts: `AbyssalTroops3.png`, `AbyssalTroops8.png`, `AbyssalDemon2.png`, `AbyssalTroops2.png`, `AbyssalTroops6.png`
- Current status: Concept direction proposed; approval pending before DCC build

Standard Abyss infantry for readable war-host encounters. The design should be disciplined and frightening rather than chaotic: horned helmet or skull crest, black pike or spear, charred armor plates, torn banner cloth, ember cracks, and violet-black weapon glow.

## Gameplay Purpose

Baseline melee enemy for Abyss encounters, patrol groups, army lines, fortress assaults, and early combat readability tests. It establishes the average humanoid scale before elite and boss entities are built.

## Silhouette Notes

Primary read is a tall horned infantry shape with a long pike. Preserve the pike line, shoulder spikes, narrow helm crest, and shield or banner variants at distance. Avoid overloading the torso with small spikes.

## Scale Notes

Height: 200-230 cm. Pike length: 260-340 cm. Author in centimeters with pivot at ground center under the feet.

## Materials And Color Palette

Charred iron, blackened leather, scorched bone horn, ember fissures, ash-gray cloth, and restrained violet edge glow on the pike head or eyes.

## Concept Image Prompt

Create an original stylized fantasy MMORPG enemy production sheet of an Abyss Black Pike Trooper for Aerathea. The design should emphasize a tall horned infantry silhouette, long black pike, charred iron armor, scorched bone crest, torn ash cloth, ember fissures, violet abyssal weapon glow, disciplined war-host identity, and standard melee enemy gameplay role. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, sparing emissive eyes and weapon accents, and MMO-friendly production design. Present it as a turnaround with front, side, back, weapon detail, material swatches, and scale beside a 180 cm humanoid.

## Modeling Notes

Model body, horn crest, shoulder plates, pike shaft/head, large armor slabs, boots, and readable cloth strips as geometry. Texture fine pitting, cracks, cloth fray, small runes, scratches, and minor straps.

## Texture And Material Notes

Material slots: body/armor, weapon, emissive accents. Maps: `T_ABY_BlackPikeTrooper_A01_BC`, `T_ABY_BlackPikeTrooper_A01_N`, `T_ABY_BlackPikeTrooper_A01_ORM`, `T_ABY_BlackPikeTrooper_A01_E`.

## Triangle Budget

LOD0: 22k-28k tris. LOD1: 14k-18k. LOD2: 7k-10k. LOD3: 2k-4k.

## LOD Plan

Preserve horn crest, pike, shoulder width, and stance first. Reduce cloth cuts, small spikes, strap loops, finger detail, inner armor gaps, and minor pike bevels before changing the primary outline.

## Collision Notes

Use a humanoid movement capsule. Physics bodies for head, chest, pelvis, upper/lower arms, hands, upper/lower legs, feet, and simple pike trace proxy. No complex-as-simple collision.

## Animation Notes

Idle, patrol walk, combat walk, turn, pike thrust, sweeping pike attack, shield brace variant, hit front, hit side, stagger, death, summon/portal spawn.

## Unreal Import Notes

- Unreal folder: `/Game/Aerathea/Creatures/Abyss/Troops/BlackPikeTrooper/`
- Skeletal mesh: `SK_ABY_BlackPikeTrooper_A01`
- Skeleton: `SKEL_ABY_Humanoid_A01` if shared, otherwise generated on first import
- Physics asset: `PHYS_ABY_BlackPikeTrooper_A01`
- Animation Blueprint: `ABP_ABY_Trooper_A01`
- Sockets: `socket_weapon_r`, `socket_weapon_l`, `socket_head_vfx`, `socket_chest_core`, `socket_ground_rift`

## Folder And Naming Recommendation

- Docs: `docs/assets/creatures/SK_ABY_BlackPikeTrooper_A01/`
- Source: `SourceAssets/Blender/Creatures/Abyss/SK_ABY_BlackPikeTrooper_A01/`
- Export: `SourceAssets/Exports/Creatures/Abyss/SK_ABY_BlackPikeTrooper_A01/`

## Quality Gate Checklist

- Reads clearly as standard Abyss infantry.
- Pike, horn crest, armor mass, and stance remain readable from game camera.
- Uses shadow/flame materials distinct from Dark Elves.
- Glow is limited to eyes, weapon edge, or small chest fissures.
- Triangle budget, maps, LODs, collision, animation list, sockets, and Unreal path are defined.
- Not approved for DCC build until Flamestrike selects it.
