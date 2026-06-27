# SK_ABY_WingedRavager_A01 Production Package

## Art Direction Summary

- Asset name: `SK_ABY_WingedRavager_A01`
- Asset type: Skeletal Mesh creature / winged elite enemy
- Parent kit: `KIT_ABY_ShadowFlame_A01`
- Source concepts: `AbyssalDemon14.png`, `AbyssalTroops5.png`, `AbyssalDemon5.png`
- Generated lore reference: `AET_LORE_ABYSS_03_AshWingMalgor.png`
- Current status: Concept direction proposed; approval pending before DCC build

Winged Abyss assault demon built for air-to-ground attacks, burning dives, and battlefield disruption. It should read as a demon with leathery/charred wings and a weapon or claw silhouette, not a dragon.

## Gameplay Purpose

Air assault enemy for vertical combat reads, dive attacks, ranged-pressure disruption, and encounter escalation. Also tests wing sockets, airborne collision, and VFX trails.

## Silhouette Notes

Primary read is a horned humanoid demon with broad damaged wings, long legs/claws, and spear or talon attack lines. Preserve wing shape, horn crown, and diving pose.

## Scale Notes

Standing height: 260-340 cm. Wingspan: 500-800 cm. Author in centimeters with pivot at ground center for landed pose and center of mass for airborne export tests.

## Materials And Color Palette

Charred membrane wings, blackened bone struts, obsidian skin, ember cracks, scorched iron weapon plates, violet or green abyssal wing-edge glow.

## Concept Image Prompt

Create an original stylized fantasy MMORPG enemy production sheet of an Abyss Winged Ravager for Aerathea. The design should emphasize a horned humanoid demon with broad torn wings, charred wing membranes, blackened bone struts, long claws, spear or talon attack silhouette, ember fissures, violet abyssal wing-edge glow, air assault mood, and elite flying enemy gameplay role. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, sparing emissive accents, and MMO-friendly production design. Present it as a turnaround with landed pose, diving pose, wing-spread view, material swatches, and scale beside a 180 cm humanoid.

## Modeling Notes

Model body, horns, large wing bones, membrane outline, claws, weapon, and major armor plates as geometry. Use texture/normal detail for membrane veins, burns, small tears, scratches, and minor scales.

## Texture And Material Notes

Material slots: body/armor, wings, weapon/emissive accents. Maps: `T_ABY_WingedRavager_A01_BC`, `T_ABY_WingedRavager_A01_N`, `T_ABY_WingedRavager_A01_ORM`, `T_ABY_WingedRavager_A01_E`.

## Triangle Budget

LOD0: 38k-50k tris. LOD1: 24k-32k. LOD2: 12k-18k. LOD3: 4k-7k.

## LOD Plan

Preserve wing span, horn crown, claw/weapon silhouette, and torso mass. Reduce wing membrane holes, small spikes, inner wing bevels, finger claws, and armor cuts first.

## Collision Notes

Use capsule or custom airborne collision tuned by gameplay. Physics bodies for head, chest, pelvis, limbs, wing upper/lower bones, and attack claw/weapon traces. No per-membrane collision.

## Animation Notes

Ground idle, wing idle, takeoff, flight loop, glide, dive attack, landing, claw swipe, spear thrust variant, hit wing, hit body, crash death, portal spawn.

## Unreal Import Notes

- Unreal folder: `/Game/Aerathea/Creatures/Abyss/Flying/WingedRavager/`
- Skeletal mesh: `SK_ABY_WingedRavager_A01`
- Skeleton: `SKEL_ABY_Winged_A01`
- Physics asset: `PHYS_ABY_WingedRavager_A01`
- Animation Blueprint: `ABP_ABY_WingedRavager_A01`
- Sockets: `socket_wing_l_vfx`, `socket_wing_r_vfx`, `socket_claw_l`, `socket_claw_r`, `socket_head_vfx`, `socket_dive_trail`

## Folder And Naming Recommendation

- Docs: `docs/assets/creatures/SK_ABY_WingedRavager_A01/`
- Source: `SourceAssets/Blender/Creatures/Abyss/SK_ABY_WingedRavager_A01/`
- Export: `SourceAssets/Exports/Creatures/Abyss/SK_ABY_WingedRavager_A01/`

## Quality Gate Checklist

- Reads as winged demon, not dragon or manticore.
- Wings remain readable through LODs.
- Flight and dive sockets are planned.
- Triangle budget, maps, LODs, collision, animations, sockets, and Unreal path are defined.
- Not approved for DCC build until Flamestrike selects it.
