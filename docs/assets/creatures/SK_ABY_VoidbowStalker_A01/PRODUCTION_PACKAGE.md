# SK_ABY_VoidbowStalker_A01 Production Package

## Art Direction Summary

- Asset name: `SK_ABY_VoidbowStalker_A01`
- Asset type: Skeletal Mesh creature / ranged enemy
- Parent kit: `KIT_ABY_ShadowFlame_A01`
- Source concepts: `AbyssalDemon10.png`, `AbyssalDemon20.png`
- Current status: Concept direction proposed; approval pending before DCC build

Ranged Abyss stalker with an impossible bow of void flame. The silhouette should be lean, arched, and predatory, with the bow reading clearly as a crescent/rift weapon rather than normal woodcraft.

## Gameplay Purpose

Ranged enemy for pressure, snare shots, anti-healer targeting, and line-of-sight combat. Provides a clear backline threat for Abyss troop groups.

## Silhouette Notes

Primary read is a thin demon archer with a glowing crescent bow. Preserve bow arc, drawn-shot pose, horn/head shape, long legs, and narrow shoulder profile.

## Scale Notes

Height: 220-280 cm. Bow height: 180-240 cm. Author in centimeters with pivot at ground center.

## Materials And Color Palette

Blackened sinew, charred bone, scorched iron rings, green or violet void bow energy, ember eyes, muted ash cloth.

## Concept Image Prompt

Create an original stylized fantasy MMORPG enemy production sheet of an Abyss Voidbow Stalker for Aerathea. The design should emphasize a lean demon archer silhouette, crescent void bow, long predatory limbs, blackened sinew, charred bone, scorched iron rings, violet or green abyssal projectile glow, backline hunter mood, and ranged enemy gameplay role. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, sparing emissive bow and eye accents, and MMO-friendly production design. Present it as a turnaround with bow-draw pose, projectile socket callouts, material swatches, and scale beside a 180 cm humanoid.

## Modeling Notes

Model body, horns, major armor, bow limbs, bow core, large claw hands, and quiver or projectile focus as geometry. Texture sinew detail, small runes, scars, cloth fray, and bow-surface pitting.

## Texture And Material Notes

Material slots: body/armor, bow, emissive projectile accents. Maps: `T_ABY_VoidbowStalker_A01_BC`, `T_ABY_VoidbowStalker_A01_N`, `T_ABY_VoidbowStalker_A01_ORM`, `T_ABY_VoidbowStalker_A01_E`.

## Triangle Budget

LOD0: 24k-34k tris. LOD1: 16k-22k. LOD2: 8k-12k. LOD3: 3k-5k.

## LOD Plan

Preserve bow arc, horn/head shape, draw posture, and long limb read. Reduce finger detail, small armor bands, bow bevels, cloth strips, and tiny spikes first.

## Collision Notes

Use humanoid movement capsule. Projectile collision belongs to gameplay/VFX, not mesh collision. Physics bodies for body and bow trace sockets only.

## Animation Notes

Idle, scan, walk, strafe, draw bow, release, charged shot, evasive step, hit reactions, stagger, death, summon arrival.

## Unreal Import Notes

- Unreal folder: `/Game/Aerathea/Creatures/Abyss/Ranged/VoidbowStalker/`
- Skeletal mesh: `SK_ABY_VoidbowStalker_A01`
- Skeleton: shared `SKEL_ABY_Humanoid_A01` if proportions allow
- Physics asset: `PHYS_ABY_VoidbowStalker_A01`
- Animation Blueprint: `ABP_ABY_VoidbowStalker_A01`
- Sockets: `socket_bow_grip`, `socket_arrow_nock`, `socket_projectile_muzzle`, `socket_head_vfx`, `socket_ground_rift`

## Folder And Naming Recommendation

- Docs: `docs/assets/creatures/SK_ABY_VoidbowStalker_A01/`
- Source: `SourceAssets/Blender/Creatures/Abyss/SK_ABY_VoidbowStalker_A01/`
- Export: `SourceAssets/Exports/Creatures/Abyss/SK_ABY_VoidbowStalker_A01/`

## Quality Gate Checklist

- Reads as ranged Abyss enemy at a glance.
- Bow silhouette remains distinct from Elven or Dark Elven bows.
- Void glow is limited to bow, projectile, and eyes.
- Triangle budget, maps, LODs, collision, animations, sockets, and Unreal path are defined.
- Not approved for DCC build until Flamestrike selects it.
