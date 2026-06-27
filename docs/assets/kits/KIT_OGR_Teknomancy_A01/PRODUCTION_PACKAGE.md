# KIT_OGR_Teknomancy_A01 Production Package

## Art Direction Summary

`KIT_OGR_Teknomancy_A01` is the shared prop, weapon, armor-module, and workshop kit for Ogre Teknomancy. The kit should feel like an arsenal built by passionate war-creators who understand magic and machines instinctively: massive cannons, hammer engines, pressure tanks, crude field pylons, hoists, rune-burned plates, forge reactors, chained crates, shield barricades, and field repair rigs. It should not resemble gnome precision engineering. Ogre Teknomancy is larger, heavier, rougher, hotter, and more reckless.

Primary source references:

- `/home/Flamestrike/Desktop/Aerathea/Aerathea Creative/ASSET CONCEPTS/OgreTekShop.png`
- `/home/Flamestrike/Desktop/Aerathea/Aerathea Creative/ASSET CONCEPTS/Ogres10.png`
- `/home/Flamestrike/Desktop/Aerathea/Aerathea Creative/ASSET CONCEPTS/Ogres11.png`
- `/home/Flamestrike/Desktop/Aerathea/Aerathea Creative/ASSET CONCEPTS/OgreMaleTek.png`
- `/home/Flamestrike/Desktop/Aerathea/Aerathea Creative/ASSET CONCEPTS/OgreSmiths.png`
- `/home/Flamestrike/Desktop/Aerathea/Aerathea Creative/ASSET CONCEPTS/OgreTekvsGnomeMek.png`

## Gameplay Purpose

This kit supports `SK_OGR_Teknomancer_A01`, Ogre forge interiors, siege yards, loot props, crafting stations, battlefield cover, enemy artillery, encounter set dressing, and Gnome Mek rivalry scenes. It should supply reusable pieces for class gear and environment dressing rather than one monolithic prop.

## Silhouette Notes

- Primary silhouettes: huge cannon barrel, squat pressure tank, heavy forge reactor, crude field pylon, blocky hammer engine, chained workbench, shield barricade, and backpack coil rig.
- Forms should be chunky and readable, with large riveted plates and reinforced bands.
- Use hanging chains, hoist hooks, skull plates, and banners sparingly as silhouette breaks.
- Avoid hundreds of modeled small bolts or wires; paint and normal-map that detail.

## Scale Notes

- Ogre-use props should be authored at 10-11 ft body ergonomics.
- Siege cannon: 320-520 cm long depending on variant.
- Forge reactor tower: 250-420 cm tall for interior/world prop variants.
- Powered hammer: 190-240 cm long.
- Bracer modules: sized to Ogre forearms, not human or gnome scale.
- Workbench height: 115-150 cm, wide enough for Ogre hands and tools.

## Materials And Color Palette

- Blackened iron, dark steel, crude brass/copper, scorched leather, chains, bone, stone, furnace ash, red banners, and orange rune heat.
- Use blue-white electrical accents only for anti-gnome Mek disruption or exposed Aetherium interaction.
- Emissive should be limited to rune cuts, reactor windows, furnace cores, pressure gauges, vents, and charged weapon cores.

## Concept Image Prompt

Create an original stylized fantasy MMORPG concept image of `KIT_OGR_Teknomancy_A01`, an Ogre Teknomancy prop and gear kit for the world of Aerathea. The design should emphasize giant overbuilt siege cannons, pressure tanks, forge reactors, crude field pylons, powered hammers, massive bracer modules, chained workbenches, hoists, shield barricades, rune-burned blackened iron, crude brass, scorched leather, bone trophies, forge-orange heat, and jealous anti-gnome battlefield technology. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, sparing emissive accents, and MMO-friendly production design. Present it as an asset board with labeled child props, scale callouts beside an Ogre body, material swatches, socket notes, and Unreal-ready modular breakdowns on a clean background. Avoid copying any existing franchise and avoid excessive micro-detail that would not translate to a mid-poly Unreal asset.

## Modeling Notes

- Build as modular static meshes and skeletal attachments where needed.
- Model real geometry for main barrels, wheel hubs, armor plates, hammer heads, reactor cages, pressure tanks, large chains, hoist hooks, shield slabs, and major brackets.
- Use normal maps for small rivets, scratches, minor runes, leather stitching, pipe seams, and small wire bundles.
- Separate carryable/equippable props from world-placement props.
- Use shared material instances across the kit to keep memory and art language consistent.

## Texture And Material Notes

- Shared texture families:
  - `T_OGR_Teknomancy_Iron_A01_BC/N/ORM`
  - `T_OGR_Teknomancy_Brass_A01_BC/N/ORM`
  - `T_OGR_Teknomancy_Leather_A01_BC/N/ORM`
  - `T_OGR_Teknomancy_RuneHeat_A01_BC/N/ORM/E`
- Child hero props may get dedicated 2K sets.
- Small props can share 1K atlases.
- Emissive map is required only for powered variants.

## Triangle Budget

- Small module props: 800-4k tris, 1 material.
- Powered hammer / bracer module: 4k-10k tris, 1-2 materials.
- Workbench / pressure tank / field engine: 6k-14k tris, 1-3 materials.
- Siege cannon: 18k-35k tris, 2-4 materials.
- Forge reactor tower: 18k-35k tris, 2-4 materials.
- Full hero workshop assembly: 40k-70k tris split into modular pieces and HLOD-friendly groups.

## LOD Plan

- LOD0: full silhouette, major plates, primary barrels, large chains, readable reactor shapes.
- LOD1: 55-65% triangle count; simplify bevels, plate layering, minor brackets, and non-silhouette chain links.
- LOD2: 25-35% triangle count; remove small hanging pieces, small pipes, minor rings, and secondary teeth.
- LOD3: 10-15% triangle count; preserve barrel, reactor, hammer, barricade, and workbench block shapes with baked color/emissive reads.

## Collision Notes

- Use simple convex hulls for standalone props.
- Siege cannon needs simplified barrel/base collision; no per-rivet or per-chain collision.
- Workbench and forge props need blocking collision only on table tops, bases, and player-facing obstacles.
- Carryable weapons use pickup/display bounds plus weapon trace sockets.
- Large workshop assemblies should be collision-split by module, not one complex collision mesh.

## Animation Notes

- Static props by default.
- Optional limited animations:
  - reactor glow pulse
  - pressure gauge twitch
  - furnace vent open/close
  - cannon recoil
  - hammer core spin
  - hanging chain sway
- Avoid continuous complex machinery with many moving micro-parts.

## Unreal Import Notes

- Asset type: Static Mesh kit, with optional Skeletal Mesh attachments for animated cannon/hammer variants.
- Unreal path: `/Game/Aerathea/Props/Ogres/Teknomancy/`.
- Class gear path: `/Game/Aerathea/Characters/Ogres/Teknomancer/Gear/`.
- Scale: centimeters.
- Pivot: bottom center for world props; grip point for weapons; attachment point for armor modules.
- Collision: simple convex or custom UCX per child mesh.
- Material slot target: 1-3 per normal prop, 4 max for hero siege/forge assets.
- Required sockets:
  - `socket_muzzle`
  - `socket_recoil`
  - `socket_core`
  - `socket_vent`
  - `socket_chain_hook`
  - `socket_hand_r_grip`
  - `socket_hand_l_grip`

## Folder And Naming Recommendation

- Docs: `docs/assets/kits/KIT_OGR_Teknomancy_A01/`
- Source: `SourceAssets/Blender/Props/Ogres/Teknomancy/`
- Export: `SourceAssets/Exports/Props/Ogres/Teknomancy/`
- Unreal: `/Game/Aerathea/Props/Ogres/Teknomancy/`
- Primary material instances:
  - `MI_OGR_Teknomancy_Iron_A01`
  - `MI_OGR_Teknomancy_Brass_A01`
  - `MI_OGR_Teknomancy_Leather_A01`
  - `MI_OGR_Teknomancy_RuneHeat_A01`

## Quality Gate Checklist

- Original to Aerathea and aligned with Ogre war-created culture.
- Clearly larger and rougher than gnome Mekgineer tech.
- Readable silhouettes at MMO camera distance.
- Materials match blackened iron, crude brass, scorched leather, bone, stone, and orange rune heat.
- Glow is sparing and justified by powered components.
- Child props are modular, collision-safe, and LOD-ready.
- Triangle budgets, material counts, texture maps, sockets, collision, and Unreal paths are defined.
