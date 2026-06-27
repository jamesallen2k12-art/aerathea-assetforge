# SM_OGR_CrudeTekPylon_A01 Production Package

## 1. Art Direction Summary

- Asset name: `SM_OGR_CrudeTekPylon_A01`
- Asset type: Static Mesh prop / VFX hook / future Blueprint objective
- Parent kit: `KIT_OGR_Teknomancy_A01`
- Encounter kit: `KIT_GNM_OGR_RivalryEncounter_A01`
- World: Aerathea
- Theme: Ogre crude Teknomancy battlefield power pylon
- Primary source references: `OgreTekShop.png`, `Ogres10.png`, `Ogres11.png`, `OgreMaleTek.png`, `OgreTekvsGnomeMek.png`, `GnomevsOgre3.png`
- Current status: production package, modeling handoff, and build/import status ready; DCC build not started

`SM_OGR_CrudeTekPylon_A01` is a large unstable field pylon that channels Ogre Teknomancy into cannons, bracers, barricades, or anti-Mek disruption. It should feel overbuilt, hot, dangerous, and made by Ogres who understand magic-machines by instinct rather than gnomish precision. The pylon is not a clean generator, not a refined magical obelisk, and not a gnome Aetherium device.

## 2. Gameplay Purpose

- Provides a battlefield objective for the Gnome/Ogre rivalry encounter.
- Can feed Ogre Teknomancer overloads, siege cannons, shield barricades, or anti-Mek disruption pulses.
- Supports disabled, idle, charged, overload, damaged, and destroyed states in a future Blueprint.
- Gives level designers a reusable powered prop for Tek shops, siege yards, fortifications, and encounter staging.
- Establishes sockets for future Niagara arcs, furnace vents, electrical discharges, hit impacts, and repair/disable interactions.

## 3. Silhouette Notes

- Broad triangular or four-foot base made from blackened iron skids, stone ballast, and heavy brace plates.
- Vertical central reactor column with furnace windows, rune-burned plates, crude brass bands, and a visible unstable core.
- Two to four side pressure tanks or coil drums strapped to the column with chain and thick brackets.
- Horn-like conductor arms, forked antennae, or crude lightning rods at the top.
- Large cable sockets and chain hook points near the base.
- Optional skull plate, red rag banner, or warning trophy as a small Ogre identity accent.
- Avoid clean symmetry, thin elegant pylons, precise gnome coils, hundreds of small wires, or purely magical monolith shapes.

## 4. Scale Notes

- Author in centimeters.
- Height target: 360-520 cm.
- Base footprint target: 260-380 cm wide.
- Central column diameter target: 90-140 cm.
- Pressure tanks target: 80-160 cm tall each.
- Pivot: bottom center on the ground, aligned to the middle of the base.
- Designed for 10-11 ft Ogre operators; handles, crank points, and repair panels should sit around Ogre waist/chest height.

## 5. Materials And Color Palette

| Material family | Palette | Use |
| --- | --- | --- |
| Blackened iron | soot black, dark steel, worn bright edges | Base, braces, conductor arms, cage plates |
| Crude brass/copper | dull brass, scorched copper, greenish oxidation | Bands, pressure tanks, gauges, pipe collars |
| Cairn stone ballast | blue-gray, ash gray, chipped dark stone | Base weights and stabilizing slabs |
| Scorched leather | dark brown, burnt tan, dirty straps | Tank wraps, cable bindings, patch repairs |
| Bone/trophy accent | aged ivory, smoke-stained bone | Optional warning plates and trophies |
| Rune heat | forge orange, ember yellow, hot red | Furnace windows, rune cuts, core pulse, vent glow |
| Disruption accent | brief blue-white electrical arcs | Anti-Mek discharge only; keep secondary to forge orange |

Emissive must be localized to rune windows, core vents, pressure gauges, and active discharge sockets. Do not flood the whole pylon with glow.

## 6. Concept Image Prompt

Create an original stylized fantasy MMORPG static mesh concept sheet of `SM_OGR_CrudeTekPylon_A01`, an Ogre crude Teknomancy battlefield power pylon for the world of Aerathea. The design should emphasize a heavy blackened-iron and cairn-stone base, a vertical overbuilt reactor column, crude brass pressure tanks, chain lashings, thick conductor arms, forked lightning rods, furnace-orange rune heat, scorched leather straps, optional skull warning plates, unstable anti-Mek blue-white discharge sockets, and a gameplay role as an encounter objective powering Ogre siege and anti-gnome devices. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, sparing emissive accents, and MMO-friendly production design. Present it as a static mesh production sheet with front, side, top footprint, damaged state, socket callouts, collision blocks, material swatches, and scale beside an Ogre Teknomancer and a Gnome Heavy Mek. Avoid copied franchise designs, polished gnome precision, elegant wizard obelisks, excessive micro-wires, unreadable clutter, text, and watermarks.

## 7. Modeling Notes

- Build as a modular static mesh with an optional future Blueprint wrapper.
- Model real geometry for the base skids, large stone ballast, central reactor column, pressure tanks, conductor arms, large vents, major brackets, thick cables, large chain silhouettes, and main rune windows.
- Use texture and normal maps for tiny rivets, fine wire wraps, scratches, surface pitting, leather stitching, minor runes, small soot streaks, and gauge ticks.
- Keep top conductors and core windows readable from the startup review camera and MMO gameplay distance.
- Use asymmetry: one tank larger, one brace crooked, uneven patch plates, and crude repairs.
- Keep cables as a few thick readable hoses, not many spaghetti wires.

## 8. Texture And Material Notes

Shared texture families from `KIT_OGR_Teknomancy_A01`:

- `T_OGR_Teknomancy_Iron_A01_BC/N/ORM`
- `T_OGR_Teknomancy_Brass_A01_BC/N/ORM`
- `T_OGR_Teknomancy_Leather_A01_BC/N/ORM`
- `T_OGR_Teknomancy_RuneHeat_A01_BC/N/ORM/E`

Dedicated pylon maps if promoted to hero objective:

- `T_OGR_CrudeTekPylon_A01_BC`
- `T_OGR_CrudeTekPylon_A01_N`
- `T_OGR_CrudeTekPylon_A01_ORM`
- `T_OGR_CrudeTekPylon_A01_E`

Material slots:

1. `MI_OGR_Teknomancy_Iron_A01`
2. `MI_OGR_Teknomancy_Brass_A01`
3. `MI_OGR_Teknomancy_RuneHeat_A01`
4. Optional `MI_OGR_CrudeTekPylon_A01_Damaged`

## 9. Triangle Budget

- LOD0 target: 8k-16k tris.
- Hero encounter objective ceiling: 20k tris only if damage-state silhouettes require it.
- Material slot target: 3, maximum 4.
- Texture target: shared 1K-2K kit materials, dedicated 2K set only for hero objective.

Spend geometry on major pylon silhouette, tanks, conductor arms, thick cables, and base braces before small bolts or wire detail.

## 10. LOD Plan

- LOD0: full base, central reactor, tanks, conductor arms, thick cables, rune windows, sockets, and damage-state silhouette cuts.
- LOD1: 55-60 percent; simplify bevels, minor brackets, cable loops, chain links, and tank straps.
- LOD2: 25-35 percent; merge tank bands, remove small chain pieces, simplify conductor arms, collapse minor vents.
- LOD3: 10-15 percent; preserve base footprint, vertical reactor column, top conductor silhouette, tank side masses, and forge-orange core read.

Never reduce the height, top conductor profile, reactor column, or tank masses before micro-detail.

## 11. Collision Notes

- Use simple UCX collision: base block, central column, tank blocks, and top conductor approximation.
- Leave cables, chains, banners, and small trophies non-blocking.
- Optional interaction overlap volume around the front repair/disable panel.
- Optional damage volume around the core for attacks.
- Do not use complex-as-simple collision.

## 12. Animation Notes

Static mesh by default.

Future Blueprint/VFX states:

- Idle low core pulse.
- Charged pylon with stronger orange rune windows.
- Anti-Mek discharge with brief blue-white arcs.
- Overload shake and venting.
- Disabled state with dim core and smoke vent.
- Destroyed state swap with broken top conductors and shattered tanks.

No many-part mechanical animation is required. Prefer material parameter pulses, Niagara arcs, and one or two simple component transforms.

## 13. Unreal Import Notes

- Asset type: Static Mesh, future Blueprint Actor wrapper.
- Static mesh: `SM_OGR_CrudeTekPylon_A01`.
- Future Blueprint: `BP_OGR_CrudeTekPylon_A01`.
- Unreal path: `/Game/Aerathea/Props/Ogres/Teknomancy/`.
- Pivot: bottom center.
- Scale: centimeters, 1 Unreal unit = 1 cm.
- Collision: UCX simple collision plus optional interaction overlap in Blueprint.
- Material slot count: 3 target, 4 maximum.

Required sockets:

- `socket_core`
- `socket_top_arc`
- `socket_conductor_l`
- `socket_conductor_r`
- `socket_vent_l`
- `socket_vent_r`
- `socket_cable_in`
- `socket_cable_out`
- `socket_hit_core`
- `socket_repair_panel`
- `socket_ground_sparks`
- `socket_overload_burst`

## 14. Folder And Naming Recommendation

- Docs: `docs/assets/props/SM_OGR_CrudeTekPylon_A01/`
- Source: `SourceAssets/Blender/Props/Ogres/Teknomancy/SM_OGR_CrudeTekPylon_A01/`
- Export: `SourceAssets/Exports/Props/Ogres/Teknomancy/SM_OGR_CrudeTekPylon_A01/`
- Unreal: `/Game/Aerathea/Props/Ogres/Teknomancy/`
- Static mesh: `SM_OGR_CrudeTekPylon_A01`
- Future Blueprint: `BP_OGR_CrudeTekPylon_A01`
- Materials: `MI_OGR_Teknomancy_*` plus optional `MI_OGR_CrudeTekPylon_A01_Damaged`
- Textures: shared `T_OGR_Teknomancy_*` or dedicated `T_OGR_CrudeTekPylon_A01_*`

## 15. Quality Gate Checklist

- Reads as Ogre crude Teknomancy, not gnome engineering or a clean magic obelisk.
- Scale and interaction points support 10-11 ft Ogre operators.
- Pylon silhouette is readable beside `SK_OGR_Teknomancer_A01` and `SK_GNM_HeavyMek_Rivalry_A01`.
- Forge-orange heat is dominant; blue-white disruption is secondary and state-driven.
- Major plates, tanks, conductors, and cables are geometry; tiny rivets, scratches, and wire detail are texture/normal detail.
- Triangle budget, material slots, texture maps, LOD plan, sockets, collision, future Blueprint states, and Unreal path are defined.
