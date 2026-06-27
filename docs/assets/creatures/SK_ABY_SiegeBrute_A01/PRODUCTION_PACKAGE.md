# SK_ABY_SiegeBrute_A01 Production Package

## Art Direction Summary

- Asset name: `SK_ABY_SiegeBrute_A01`
- Asset type: Skeletal Mesh creature / large siege enemy
- Parent kit: `KIT_ABY_ShadowFlame_A01`
- Source concepts: `AbyssalSieger.png`, `AbyssalDemon15.png`
- Generated lore reference: `AET_LORE_ABYSS_05_RiftMawReaver.png`
- Current status: Concept direction proposed; approval pending before DCC build

Large Abyss wall-breaker that uses mass, extra limbs, axes, and ruin magic to crack gates and scatter infantry. It should feel like a siege role, not just a scaled-up troop.

## Gameplay Purpose

Mini-boss or event enemy for fortification attacks, target priority, stagger mechanics, heavy area attacks, and destructible-object encounters.

## Silhouette Notes

Primary read is a huge horned brute with broad shoulders, extra arms or oversized weapon arms, furnace/void core, and heavy forward mass. Preserve scale and weapon mass first.

## Scale Notes

Height: 450-700 cm. Arm span: 500-850 cm. Author in centimeters with pivot under body mass. Requires 180 cm humanoid and gnome scale callouts.

## Materials And Color Palette

Charred iron armor, scorched basalt plates, ember furnace cracks, black flame core, bone horns, violet void residue, ash-stained cloth or chains.

## Concept Image Prompt

Create an original stylized fantasy MMORPG creature production sheet of an Abyss Siege Brute for Aerathea. The design should emphasize a huge horned wall-breaker silhouette, broad shoulders, extra weapon arms or oversized axe arms, furnace-like chest core, charred iron armor, scorched basalt plates, ember cracks, violet void residue, siege-destruction mood, and mini-boss gameplay role. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, sparing emissive core and weapon accents, and MMO-friendly production design. Present it as a turnaround with attack pose, scale beside 180 cm humanoid and 110 cm gnome, material swatches, collision callout, and LOD callout.

## Modeling Notes

Model major body mass, horns, armor plates, weapons, extra arms, claws, chains, and chest core as geometry. Texture small cracks, armor pitting, runes, scars, and chain wear.

## Texture And Material Notes

Material slots: body/armor, weapons/chains, emissive core. Maps: `T_ABY_SiegeBrute_A01_BC`, `T_ABY_SiegeBrute_A01_N`, `T_ABY_SiegeBrute_A01_ORM`, `T_ABY_SiegeBrute_A01_E`.

## Triangle Budget

LOD0: 50k-70k tris. LOD1: 32k-45k. LOD2: 16k-24k. LOD3: 5k-8k.

## LOD Plan

Preserve huge shoulder mass, horns, weapon arms, and chest core. Reduce small spikes, chain links, inner armor layers, finger detail, and minor weapon cuts first.

## Collision Notes

Use large movement capsule plus physics bodies for head, chest, pelvis, major arm chains, hands, weapon proxies, and feet. Destructible interactions should use gameplay traces and tagged sockets.

## Animation Notes

Idle heavy, stomp walk, turn, overhead slam, ground sweep, gate breaker charge, roar, summon shockwave, hit heavy, stagger, knockdown, death.

## Unreal Import Notes

- Unreal folder: `/Game/Aerathea/Creatures/Abyss/Siege/SiegeBrute/`
- Skeletal mesh: `SK_ABY_SiegeBrute_A01`
- Skeleton: `SKEL_ABY_LargeBrute_A01`
- Physics asset: `PHYS_ABY_SiegeBrute_A01`
- Animation Blueprint: `ABP_ABY_SiegeBrute_A01`
- Sockets: `socket_chest_core`, `socket_weapon_l`, `socket_weapon_r`, `socket_slam_vfx`, `socket_head_vfx`, `socket_ground_rift`

## Folder And Naming Recommendation

- Docs: `docs/assets/creatures/SK_ABY_SiegeBrute_A01/`
- Source: `SourceAssets/Blender/Creatures/Abyss/SK_ABY_SiegeBrute_A01/`
- Export: `SourceAssets/Exports/Creatures/Abyss/SK_ABY_SiegeBrute_A01/`

## Quality Gate Checklist

- Reads as siege unit at gameplay distance.
- Scale is clear beside humanoid and gnome references.
- Heavy attacks and core sockets are planned.
- Triangle budget, maps, LODs, collision, animations, sockets, and Unreal path are defined.
- Not approved for DCC build until Flamestrike selects it.
