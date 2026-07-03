# SM_GIA_BloodAxeFirewoodStacks_A01 Production Package

## Art Direction Summary

- Asset name: `SM_GIA_BloodAxeFirewoodStacks_A01`
- Asset type: Static Mesh production package, docs-only planning
- Task: `AET-MA-20260629-444`
- Parent kit: `KIT_GIA_BloodAxeAshSlagFirewood_A01`
- Child intake row: `BloodAxeForge.png#Clutter_FirewoodStacks_GiantLogs`
- Faction/theme: Blood Axe Tribe, hostile Giant sub-faction only
- Status: production package documentation only; no DCC, FBX, Unreal Content asset, material graph, VFX, Blueprint, validator, startup placement, final approval, or implementation target is created or approved here

`SM_GIA_BloodAxeFirewoodStacks_A01` defines Giant-scale stacked logs, split trunks, crude crib stacks, and charred end-cap dressing for Blood Axe camp and forge spaces. The asset is static log dressing only, not a gatherable, consumable, pickup-enabled, destructible, crafting, resource, inventory, economy, rope-simulated, physics-simulated, DCC, Unreal implementation, final approval, or implementation-target object.

The Blood Axe Tribe remains a hostile Giant sub-faction. The stack language should feel rough, temporary, raider-built, and oversized, separate from neutral/civilized Giant cave-town timber craft, civic stonework, warm peaceful hearths, blue-gray masonry, restrained blue runes, terraces, waterworks, and master mason identity.

## Gameplay Purpose

The asset supports static environmental storytelling by showing that Blood Axe camps consume massive fuel around forges, cooking areas, palisade edges, and rough shelters. It gives level artists readable Giant-scale log masses without adding resource, gathering, destruction, crafting, or inventory systems.

Allowed purpose:

- Static log stack dressing only.
- Giant-scale fuel story for hostile camps and forge yards.
- Visual pairing with ash piles, charcoal heaps, cooled slag, and scorched debris.
- Broad shape breakup along shelter edges, hearth work lanes, and storage corners.

Out of scope:

- Gatherable, consumable, pickup, destructible, crafting, resource, inventory, economy, loot, vendor, cooking, workstation, interaction, UI prompt, rope simulation, physics simulation, heat, damage, VFX, audio, DCC, Unreal implementation, final approval, or implementation-target behavior.

## Silhouette Notes

Primary read: long, heavy, Giant-scale logs stacked in crude rows or cribbed piles. The silhouette should emphasize broad log cylinders, split trunk planes, uneven charred ends, and rough pile rhythm rather than tidy human-scale firewood.

Required silhouette traits:

- Oversized log lengths and thicknesses matched to Giant use.
- Low to mid-height stacks with stable broad footprints.
- Cribbed, leaned, or rough horizontal rows with readable negative space.
- Chunky split faces and charred end caps.
- Sparse wedges, stones, or rough stops to prevent a perfectly neat pile.
- No gatherable bundle read, pickup handle read, destructible fracture staging, rope-simulated parts, active fire language, or cooking station composition.

Model real geometry for major logs, split trunk planes, large bark breaks, charred end caps, broad support wedges, and stack outline pieces. Use texture and normal detail for bark grain, smaller cracks, saw or axe marks, soot, fine splinters, and small knots.

## Scale Notes

Use the validated `SK_GIA_Base_A01` Giant scale lock exactly:

- Female Giant baseline: 442 cm / 14'6".
- Male Giant baseline: 470 cm / 15'5".
- Approved Giant ranges: females 14-15 ft / 427-457 cm; males 14'10"-16'0" / 452-488 cm.
- Author future source in centimeters. 1 Unreal unit = 1 cm.

Suggested production dimensions:

- Short stack: 300-450 cm long, 130-220 cm deep, 90-150 cm high.
- Medium stack: 450-650 cm long, 180-300 cm deep, 130-210 cm high.
- Large stack: 650-850 cm long, 240-360 cm deep, 180-260 cm high.
- Individual Giant-scale logs: 240-620 cm long and 30-95 cm thick.
- Split log face width: 30-120 cm depending on trunk size.
- Charred end-cap depth: 8-35 cm as texture and slight geometry, not glowing heat.

The stacks must feel too large for normal humanoid firewood handling. Future scale review must compare against female 442 cm and male 470 cm Giants before any DCC or Unreal work.

## Materials and Color Palette

Primary material language:

- Dark bark and rough stripped wood.
- Split raw wood interiors.
- Charred black end caps.
- Soot stains and pale ash dust on lower contact areas.
- Dull hide or dark iron stops only if needed as static support details.
- Restrained Blood Axe red cloth tag or paint mark only if it does not read as a UI marker.

Suggested palette:

- Charred bark: `#160E0A` to `#332015`
- Dark bark brown: `#2B1A10` to `#4C3020`
- Split raw wood: `#6A4930` to `#A36C3A`
- Dry exposed grain: `#9A744A` to `#C09057`
- Soot black: `#0B0A09` to `#24201C`
- Pale ash dust: `#8D8678` to `#BAAE9A`
- Restrained Blood Axe red: `#5E1512` to `#842019`

No emissive color is planned. Avoid active flame orange, glowing coal interiors, heat shimmer, blue Aetherium, polished civilized Giant craft, resource highlight colors, or clean merchant stockpile language.

## Concept Image Prompt

Create an original stylized fantasy MMORPG concept image of `SM_GIA_BloodAxeFirewoodStacks_A01` for the world of Aerathea. The design should emphasize Giant-scale stacked logs, rough crib stacks, split trunks, charred end caps, dark bark, soot stains, pale ash dust, broad MMO-readable silhouettes, female 442 cm / 14'6" and male 470 cm / 15'5" Giant scale callouts, hostile Blood Axe raider camp identity, separation from neutral/civilized Giant culture, and a static log-dressing role only. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, no emissive glow, and MMO-friendly production design. Present it as a clean prop concept sheet with side, front, top, and three-quarter views, three size variants, material swatches, and LOD/collision callouts. Avoid copying any existing franchise, avoid gatherable resource framing, pickup prompts, destructible fracture diagrams, crafting or inventory UI, rope or physics simulation notes, active fire, smoke, sparks, heat shimmer, VFX, and excessive micro-detail that would not translate to a mid-poly Unreal asset.

## Modeling Notes

This is a docs-only modeling plan. No mesh, sculpt, retopo, UV, bake, collision proxy, proof render, FBX, Unreal import, material graph, VFX, Blueprint, validator, startup actor, runtime behavior, final approval, or implementation target is created or approved here.

Future modeling guidance:

- Build three reusable stack variants: short row stack, crib stack, and uneven leaning stack.
- Use low-sided faceted cylinders or split-log forms, not high-resolution round trunks.
- Give each stack a stable ground footprint and clear long-axis orientation.
- Vary log lengths, rotations, and broken ends enough to avoid repetition.
- Model a few large split faces and missing-bark plates for silhouette interest.
- Keep support wedges or stones sparse and static.
- Avoid detachable pickup logs, resource-count rows, destructible fracture chunk planning, cooking hooks, axe/tool staging, rope simulation, physics setup, or interaction affordances.

Use real geometry for log bodies, broad split planes, large bark gaps, support wedges, and stack outline. Use texture and normal maps for bark grain, axe marks, soot, small cracks, fine splinters, and knots.

## Texture and Material Notes

Required future texture map set:

- Base Color / Albedo: `T_GIA_BloodAxeFirewoodStacks_A01_BC`
- Normal: `T_GIA_BloodAxeFirewoodStacks_A01_N`
- Packed Occlusion/Roughness/Metallic: `T_GIA_BloodAxeFirewoodStacks_A01_ORM`

Material slot target:

- Slot 0: bark, split wood, charred ends, soot, and ash dust atlased into one material.
- Optional Slot 1: hide stops, dark iron bands, or sparse Blood Axe cloth tags only if later approved and not cleanly atlased.

Texture resolution target:

- 1K for short and medium stack variants.
- 1K to 2K for the large stack if log ends need readable variation.
- No 4K hero texture is planned.

Packed `ORM` guidance:

- R: strong occlusion between stacked logs, under crib intersections, inside split faces, and at ground contact.
- G: high roughness for bark, charred ends, soot, ash, and dry split wood.
- B: metallic at 0.0 unless optional dark iron stops are approved later.

No emissive map is planned. No material graph, shader, texture asset, or material instance is authored by this package.

## Triangle Budget

Target LOD0 budget:

- Short stack: 2,000-3,500 tris.
- Medium stack: 3,500-5,500 tris.
- Large stack: 5,500-7,000 tris.
- Combined variant review mesh: keep under 14,000 tris if variants are temporarily composed for review by a later approved task.

Material slots:

- 1 material slot target.
- 2 material slots maximum only for optional support material separation.

Spend geometry on log silhouettes, split faces, large end caps, stack rhythm, and broad support pieces. Do not spend geometry on fine bark hairs, tiny splinters, small knots, dense cracks, ash specks, individual saw fibers, or hidden interior log intersections.

## LOD Plan

All important variants require LOD0-LOD3.

- LOD0: full log count, split faces, charred end caps, support wedges, readable bark plates, and broad stack rhythm.
- LOD1: 60-70 percent of LOD0; reduce small bevels, minor splits, hidden log intersections, small bark plates, and duplicate end-cap cuts.
- LOD2: 35-45 percent of LOD0; merge interior logs, simplify cylinders, remove non-silhouette supports, and simplify split faces.
- LOD3: 15-25 percent of LOD0; preserve stack footprint, long-log read, major silhouette, and dark charred-end rhythm.

LOD reduction order:

1. Bark hairlines, fine cracks, ash speckles, tiny splinters, and small knots.
2. Small split-face bevels, minor bark plates, and hidden underside cuts.
3. Interior logs, duplicate support wedges, and non-silhouette log-end detail.
4. Back-side row detail and concealed intersections.
5. Main log count and broad stack footprint only after smaller details are removed.

Never reduce Giant-scale log thickness, stack height rhythm, or long-axis read before removing minor details.

## Collision Notes

Collision remains simple, static, and display-focused.

Recommended future collision:

- Collision disabled by default if used as purely visual dressing.
- If blocking is needed, use one to three simple boxes or convex hulls around the stack mass.
- Keep walkable collision disabled unless a later approved level-design task requires it.
- Do not use per-log collision.

Do not add gatherable collision, pickup collision, consumable triggers, destructible fracture collision, crafting or resource volumes, inventory triggers, economy or loot volumes, rope simulation, physics simulation, cooking interaction, heat damage volumes, VFX collision, cover volumes, nav rules, or encounter hazard volumes.

## Animation Notes

Baseline asset is static.

Approved for this package:

- Fixed stacked-log silhouettes.
- Painted bark, split wood, soot, and ash variation only.
- No runtime motion claim.

Not included:

- Rolling logs, falling logs, rope simulation, physics simulation, destructible collapse, burning states, smoke, sparks, embers, active flame, heat shimmer, animated material states, emissive pulsing, audio, interaction, gatherable behavior, pickup, crafting, resource, inventory, economy, cooking, or Blueprint state.

## Unreal Import Notes

This section is future planning only. No Unreal Content asset, import, material instance, texture asset, Blueprint, Niagara system, validator, startup actor, runtime source, final approval, or implementation target is created by this package.

Planned future asset type:

- Static Mesh: `SM_GIA_BloodAxeFirewoodStacks_A01`

Import planning:

- Author in centimeters and import at scale 1.0.
- Pivot at ground center of the stack footprint, with long axis aligned for grid placement.
- Assign LOD0, LOD1, LOD2, and LOD3.
- Material slots: 1 target, 2 maximum if optional supports are separated.
- Collision: disabled by default or one to three simple display hulls if explicitly needed later.
- Sockets: none.
- Animation list: none.
- Blueprint behavior: none.
- Performance note: preserve log thickness and stack rhythm; remove bark, split, ash, and hidden intersection detail first.

Texture list:

- `T_GIA_BloodAxeFirewoodStacks_A01_BC`
- `T_GIA_BloodAxeFirewoodStacks_A01_N`
- `T_GIA_BloodAxeFirewoodStacks_A01_ORM`

## Folder and Naming Recommendation

Documentation path:

- `docs/assets/props/SM_GIA_BloodAxeFirewoodStacks_A01/PRODUCTION_PACKAGE.md`

Future planning folders, pending separate approval:

- Static Mesh: `/Game/Aerathea/Props/Giants/BloodAxeCamp/ForgeClutter/`
- Materials: `/Game/Aerathea/Materials/Giants/BloodAxe/`
- Textures: `/Game/Aerathea/Textures/Giants/BloodAxe/Camp/ForgeClutter/`

Recommended names:

- Static Mesh: `SM_GIA_BloodAxeFirewoodStacks_A01`
- Material Instance: `MI_GIA_BloodAxeFirewood_A01`
- Base Color: `T_GIA_BloodAxeFirewoodStacks_A01_BC`
- Normal: `T_GIA_BloodAxeFirewoodStacks_A01_N`
- ORM: `T_GIA_BloodAxeFirewoodStacks_A01_ORM`

Do not create or edit `Content/Aerathea`, `SourceAssets`, DCC files, FBX exports, Unreal imports, runtime source, tools, validators, startup placements, external concepts, global indexes, task-board files, backlog files, bootstrap files, or sibling package files from this task.

## Quality Gate Checklist

- Blood Axe remains a hostile Giant sub-faction, separate from neutral/civilized Giant culture.
- Female Giant baseline 442 cm / 14'6" and male Giant baseline 470 cm / 15'5" are preserved.
- Asset is static log dressing only.
- No gatherable, consumable, pickup, destructible, crafting, resource, inventory, economy, rope simulation, physics simulation, DCC, Unreal implementation, final approval, or implementation target is claimed.
- Silhouette uses broad Giant-scale logs, stable stack footprints, and readable charred end caps.
- Materials use dark bark, split raw wood, soot, pale ash, restrained Blood Axe accents, and no emissive glow.
- Fine bark grain, tiny splinters, small knots, ash specks, and hairline cracks are texture or normal detail, not geometry.
- Triangle budget, LOD0-LOD3 plan, simple display collision guidance, texture map plan, and Unreal import planning are included.
- Folder and naming recommendations preserve `GIA` and `BloodAxe` naming.
- Package remains docs-only and does not modify external source concepts, global indexes, task board, DCC, Unreal, source, tools, validators, Hermes files, or unrelated packages.
