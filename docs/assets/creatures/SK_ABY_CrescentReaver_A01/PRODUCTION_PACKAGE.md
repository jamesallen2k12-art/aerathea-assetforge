# SK_ABY_CrescentReaver_A01 Production Package

## Art Direction Summary

- Asset name: `SK_ABY_CrescentReaver_A01`
- Asset type: Skeletal Mesh creature / elite melee enemy
- Parent kit: `KIT_ABY_ShadowFlame_A01`
- Source concepts: `AbyssalDemon12.png`, `AbyssalDemon18.png`, generated lore reference `AET_LORE_ABYSS_08_ShadowspurVex.png`
- Current status: Concept direction proposed; approval pending before DCC build

An agile Abyss duelist built around crescent blades, hooked limbs, and void-shadow speed. It should feel like a destroyer of casters and wounded enemies, not a heavy brute.

## Gameplay Purpose

Elite melee enemy for flanking, gap closing, interrupting casts, and forcing players to reposition. It creates a readable mid-tier threat between rank troops and large demons.

## Silhouette Notes

Primary read is a lean horned figure with two crescent weapons forming a circular or hook silhouette. Preserve long arms, blade arcs, narrow waist, aggressive forward posture, and violet blade glow.

## Scale Notes

Height: 240-300 cm. Blade radius: 90-140 cm each. Author in centimeters with pivot at ground center under the feet.

## Materials And Color Palette

Obsidian skin, charred iron bracers, bone horn arcs, dark leather wraps, violet-black crescent blade energy, ember cracks around joints.

## Concept Image Prompt

Create an original stylized fantasy MMORPG enemy production sheet of an Abyss Crescent Reaver for Aerathea. The design should emphasize a lean horned duelist silhouette, twin crescent blades, hooked limbs, obsidian skin, charred iron bracers, bone horn arcs, violet abyssal blade glow, swift predatory mood, and elite melee gameplay role. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, sparing emissive accents, and MMO-friendly production design. Present it as a turnaround with attack-pose inset, blade detail, material swatches, and scale beside a 180 cm humanoid.

## Modeling Notes

Model body, horns, hands/claws, blade bodies, major bracers, hip armor, and large cloth strips. Texture small cracks, rune cuts, skin fissures, weapon scratches, and fine cloth tears.

## Texture And Material Notes

Material slots: body/armor, weapons, emissive accents. Maps: `T_ABY_CrescentReaver_A01_BC`, `T_ABY_CrescentReaver_A01_N`, `T_ABY_CrescentReaver_A01_ORM`, `T_ABY_CrescentReaver_A01_E`.

## Triangle Budget

LOD0: 28k-38k tris. LOD1: 18k-24k. LOD2: 9k-13k. LOD3: 3k-5k.

## LOD Plan

Preserve crescent blade arcs, horn crown, forward stance, and long limb silhouette. Reduce small cloth cuts, finger claws, inner blade bevels, spine spikes, and minor armor details first.

## Collision Notes

Use humanoid movement capsule with weapon trace sockets. Physics bodies for head, chest, pelvis, limbs, hands, and blade proxies for animation traces only.

## Animation Notes

Idle twitch, combat idle, sprint, side-step, leap slash, twin sweep, spin strike, cast interrupt, hit reactions, stagger, death, portal arrival.

## Unreal Import Notes

- Unreal folder: `/Game/Aerathea/Creatures/Abyss/Elites/CrescentReaver/`
- Skeletal mesh: `SK_ABY_CrescentReaver_A01`
- Skeleton: shared `SKEL_ABY_Humanoid_A01` if proportions allow
- Physics asset: `PHYS_ABY_CrescentReaver_A01`
- Animation Blueprint: `ABP_ABY_CrescentReaver_A01`
- Sockets: `socket_blade_l`, `socket_blade_r`, `socket_head_vfx`, `socket_chest_core`, `socket_shadowstep_vfx`

## Folder And Naming Recommendation

- Docs: `docs/assets/creatures/SK_ABY_CrescentReaver_A01/`
- Source: `SourceAssets/Blender/Creatures/Abyss/SK_ABY_CrescentReaver_A01/`
- Export: `SourceAssets/Exports/Creatures/Abyss/SK_ABY_CrescentReaver_A01/`

## Quality Gate Checklist

- Reads as agile elite, not a rank troop or boss.
- Crescent weapons define the silhouette.
- Emissive blade accents are restrained and readable.
- Mid-poly detail is concentrated on large forms.
- LOD, collision, animation, sockets, maps, and Unreal paths are defined.
- Not approved for DCC build until Flamestrike selects it.
