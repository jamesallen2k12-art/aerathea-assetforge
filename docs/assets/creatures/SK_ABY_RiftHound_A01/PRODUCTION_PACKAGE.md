# SK_ABY_RiftHound_A01 Production Package

## Art Direction Summary

- Asset name: `SK_ABY_RiftHound_A01`
- Asset type: Skeletal Mesh creature / abyss beast
- Parent kit: `KIT_ABY_ShadowFlame_A01`
- Source concepts: `AbyssalDemon8.png`, `AbyssalLordHound.png`, `AbyssalLord4.png`, `AbyssalTroops9.png`
- Current status: Concept direction proposed; approval pending before DCC build

Low, fast Abyss beast used for pursuit, flanking, and hunting bound souls. It should read as a hound/crawler with rift-torn anatomy and black flame energy, not a normal wolf.

## Gameplay Purpose

Pursuit enemy for packs, ambushes, chase sequences, summoned minions, and lord escort encounters. Establishes non-humanoid Abyss animation and collision needs.

## Silhouette Notes

Primary read is a low forward-leaning hound or crawler with long forelimbs, spined back, horned skull, and glowing maw or chest fissure. Preserve low profile and lunge shape.

## Scale Notes

Shoulder height: 120-180 cm. Body length: 280-420 cm. Larger lord-bound variant can reach 550 cm long. Author in centimeters with pivot under body mass.

## Materials And Color Palette

Obsidian hide, exposed charred bone, black flame maw, green or violet rift glow, ash-gray claws, scorched sinew.

## Concept Image Prompt

Create an original stylized fantasy MMORPG creature production sheet of an Abyss Rift Hound for Aerathea. The design should emphasize a low lunging hound/crawler silhouette, horned skull, long forelimbs, spined back, black flame maw, obsidian hide, charred bone, green or violet rift glow, pursuit predator mood, and fast beast enemy gameplay role. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, sparing emissive maw and chest fissures, and MMO-friendly production design. Present it as a creature turnaround with lunge pose, pack scale, material swatches, collision callout, and scale beside a 180 cm humanoid.

## Modeling Notes

Model skull, spine ridge, body mass, major limbs, claws, tail or tendrils, jaw, and large plates as geometry. Texture sinew, fine cracks, scars, ash, small tooth detail, and minor spikes.

## Texture And Material Notes

Material slots: body/bone, claws/plates, emissive maw/core. Maps: `T_ABY_RiftHound_A01_BC`, `T_ABY_RiftHound_A01_N`, `T_ABY_RiftHound_A01_ORM`, `T_ABY_RiftHound_A01_E`.

## Triangle Budget

LOD0: 30k-45k tris. LOD1: 20k-28k. LOD2: 9k-14k. LOD3: 3k-5k.

## LOD Plan

Preserve low lunge profile, skull, spine ridge, claws, and maw glow. Reduce small spikes, tooth counts, sinew strips, tail tendrils, and claw bevels first.

## Collision Notes

Use beast movement capsule or custom capsule tuned to low profile. Physics bodies for head, jaw, chest, pelvis, limb chains, tail, and bite/claw trace sockets.

## Animation Notes

Idle prowl, sniff/search, walk, run, leap, bite, claw rake, pack howl, hit front, hit side, stagger, death, rift spawn.

## Unreal Import Notes

- Unreal folder: `/Game/Aerathea/Creatures/Abyss/Beasts/RiftHound/`
- Skeletal mesh: `SK_ABY_RiftHound_A01`
- Skeleton: `SKEL_ABY_Quadruped_A01`
- Physics asset: `PHYS_ABY_RiftHound_A01`
- Animation Blueprint: `ABP_ABY_RiftHound_A01`
- Sockets: `socket_mouth_vfx`, `socket_bite`, `socket_claw_l`, `socket_claw_r`, `socket_chest_core`, `socket_ground_rift`

## Folder And Naming Recommendation

- Docs: `docs/assets/creatures/SK_ABY_RiftHound_A01/`
- Source: `SourceAssets/Blender/Creatures/Abyss/SK_ABY_RiftHound_A01/`
- Export: `SourceAssets/Exports/Creatures/Abyss/SK_ABY_RiftHound_A01/`

## Quality Gate Checklist

- Reads as Abyss beast, not a normal animal.
- Low pursuit silhouette is preserved.
- Collision supports fast movement and bite/claw traces.
- Triangle budget, maps, LODs, animations, sockets, and Unreal path are defined.
- Not approved for DCC build until Flamestrike selects it.
