# KIT_ABY_ShadowFlame_A01 Production Package

## Art Direction Summary

- Asset name: `KIT_ABY_ShadowFlame_A01`
- Asset type: Production kit / multi-creature enemy hierarchy
- World: Aerathea
- Faction/theme: Abyss/Anathema
- Source concepts: 45 Abyss/Anathema source images plus `Gnome Mek fighting Demon.png`
- Generated lore set: `docs/lore/images/abyss-shadow-flame/`
- Current status: Visual intake complete; concept directions proposed; final creature approvals pending before DCC build
- Proposed naming codes: `ABY` for Abyss entities, `ANA` for Anathema siege entities

Ancient entropic beings of shadow and flame that seek the destruction of anything that creates, heals, orders, or builds. The hierarchy should feel like a war-host from a sealed cosmic prison: rank troops, duelists, casters, hounds, siege beasts, commanders, lords, and Anathema war constructs.

This package is not final art approval. It creates a build-ready planning structure and first ten proposed child packages so selection can happen without losing hierarchy, scale, or performance control.

## Gameplay Purpose

Supports the first Abyss enemy roster, lore encounter planning, creature scale tiers, combat-role readability, future summoning/binding mechanics, and production scheduling. The kit should let designers choose from standard infantry, elites, casters, beasts, siege threats, and boss-class lords.

## Silhouette Notes

Use horn crowns, black flame crowns, torn banners, hooked weapons, crescent blades, void bows, shield slabs, wing spans, crawling hound profiles, siege-drake cannon silhouettes, and towering lord forms. Preserve the read from game camera distance before adding internal detail.

The Abyss visual language must remain distinct from Dark Elves: rough entropy, charred iron, scorched basalt, ember fissures, violet void magic, ruin sigils, and broken binding chains instead of refined lunar elegance.

## Scale Notes

- Lesser troops: 180-230 cm tall.
- Elite humanoid demons: 230-320 cm tall.
- Winged ravagers and hounds: 280-450 cm long or wide depending pose.
- Siege brutes: 450-700 cm tall.
- Abyss lords: 600-1000 cm tall depending encounter tier.
- Anathema siege drake: 900-1600 cm long, raid or world-event scale only.

Author in centimeters. Keep combat capsules conservative and use physics bodies only where gameplay needs accurate hit or VFX locations.

## Materials And Color Palette

Primary palette: obsidian black, charred iron, scorched basalt, ember orange, deep blood red, violet void glow, sulfur smoke, ash gray, and bone-white horn highlights.

Anathema variants add dark brass, blackened steel plates, blue-white bound-core energy, and rune-tech cannon elements. Blue energy should read as bound or stolen power, not friendly Aetherium.

## Concept Image Prompt

Create an original stylized fantasy MMORPG enemy hierarchy sheet of Abyss creatures for the world of Aerathea. The design should emphasize ancient entropic beings of shadow and flame, readable horned silhouettes, rank troops, elite duelists, ward-breaking mages, hounds, siege brutes, Abyss lords, and Anathema siege constructs, with charred iron, scorched basalt, ember fissures, violet void magic, torn war banners, broken binding chains, and sparing emissive eyes, runes, cores, and weapons. Use hand-painted texture detail, baked-AO-style depth, normal-map-style surface detail, and MMO-friendly production design. Present it as a creature hierarchy production board with scale callouts, role labels, material swatches, socket callouts, LOD notes, and a 180 cm humanoid comparison. Avoid copied franchise designs, photoreal micro-detail, gore, readable text, and excessive particles.

## Modeling Notes

Model real geometry for bodies, horns, wings, claws, major armor plates, weapon heads, shields, large banners, hound legs, siege-drake cannons, and large binding-chain links. Use texture and normal detail for small cracks, pitted iron, ash, fine rune scratches, skin fissures, cloth tears, and tiny spikes.

Keep each child asset silhouette-first. If a detail is not readable at gameplay camera distance, make it a texture or material mask unless it affects sockets, animation, or collision.

## Texture And Material Notes

Shared material families:

- `MI_ABY_CharredFlesh_A01`
- `MI_ABY_ScorchedIron_A01`
- `MI_ABY_VoidFlame_A01`
- `MI_ABY_BoneHorn_A01`
- `MI_ANA_BoundCore_Blue_A01`

Required maps per creature family: `BC`, `N`, `ORM`, and `E` only for eyes, cores, runes, weapon edges, portals, or cannon throats. Avoid full-body glow.

## Triangle Budget

- Lesser troop LOD0: 18k-28k tris.
- Elite humanoid demon LOD0: 25k-40k tris.
- Hound or winged ravager LOD0: 30k-50k tris.
- Siege brute LOD0: 45k-70k tris.
- Abyss lord LOD0: 60k-90k tris.
- Anathema siege drake LOD0: 80k-100k tris, with aggressive LODs and strict material limits.

Use 2K texture sets for normal enemies and 4K only for boss or cinematic review variants.

## LOD Plan

All important child assets require LOD0-LOD3.

- LOD0: full silhouette, major horns, weapons, armor plates, wings, claws, banners, cores, and readable VFX sockets.
- LOD1: reduce secondary cuts, cloth tears, small spikes, inner armor gaps, and minor weapon bevels.
- LOD2: merge armor groups, simplify fingers/claws, reduce chain links, fold small banners into planes.
- LOD3: preserve only class read: horn crown, weapon type, wing/hound/siege/lord mass, and core or eye glow.

Never remove the main weapon, horn crown, wing outline, hound stance, siege cannon, or lord crown first.

## Collision Notes

Use movement capsules and simple physics assets. Do not use complex-as-simple collision on skeletal creatures. Suggested physics bodies: head, chest, pelvis, upper/lower limbs, horns only if used for hit traces, wings, tail, weapon trace proxy, and VFX core sockets.

Large siege creatures need separate navigation and encounter collision plans before implementation.

## Animation Notes

Shared animation planning:

- Idle, alert idle, patrol walk, combat walk, turn in place.
- Primary attack, secondary attack, heavy attack, cast or channel, hit reactions, stagger, death.
- Role-specific additions: bow draw/release, shield brace, wing takeoff/land, hound lunge, siege cannon charge/fire/recover, lord summon/binding break.

## Unreal Import Notes

- Suggested Unreal root: `/Game/Aerathea/Creatures/Abyss/`
- Abyss skeletal meshes: `/Game/Aerathea/Creatures/Abyss/<Role>/`
- Anathema skeletal meshes: `/Game/Aerathea/Creatures/Anathema/`
- Shared materials: `/Game/Aerathea/Materials/Abyss/`
- Shared VFX: `/Game/Aerathea/VFX/Abyss/`
- Pivot: ground center under body mass for creatures; center of mass for airborne-only variants.
- Scale: centimeters.
- Required sockets: `socket_head_vfx`, `socket_eye_l`, `socket_eye_r`, `socket_weapon_r`, `socket_weapon_l`, `socket_cast_core`, `socket_chest_core`, `socket_back_vfx`, `socket_ground_rift`.

## Folder And Naming Recommendation

- Docs: `docs/assets/kits/KIT_ABY_ShadowFlame_A01/`
- Child packages: `docs/assets/creatures/SK_ABY_*` and `docs/assets/creatures/SK_ANA_*`
- Source concepts remain in `/home/Flamestrike/Desktop/Aerathea/Aerathea Creative/ASSET CONCEPTS/`

Proposed first ten child packages:

1. `SK_ABY_BlackPikeTrooper_A01`
2. `SK_ABY_CrescentReaver_A01`
3. `SK_ABY_VoidbowStalker_A01`
4. `SK_ABY_WardbreakerMage_A01`
5. `SK_ABY_BulwarkDemon_A01`
6. `SK_ABY_WingedRavager_A01`
7. `SK_ABY_RiftHound_A01`
8. `SK_ABY_SiegeBrute_A01`
9. `SK_ABY_CinderLord_A01`
10. `SK_ANA_SiegeDrake_A01`

## Quality Gate Checklist

- Original to Aerathea and not copied from any franchise.
- Shadow/flame entropy language is distinct from Dark Elven lunar-shadow language.
- Hierarchy includes troops, elites, casters, beasts, siege, lords, and Anathema.
- Each proposed child has source concepts, gameplay role, scale, materials, triangle budget, LODs, collision, animation notes, sockets, and Unreal path.
- Emissive effects are sparing and role-based.
- No child is marked approved for DCC build until Flamestrike selects the direction.
