# SM_GIA_BloodAxeFirewoodBundles_A01 Production Package

## Art Direction Summary

- Asset name: `SM_GIA_BloodAxeFirewoodBundles_A01`
- Asset type: Static Mesh production package, docs-only planning
- Task: `AET-MA-20260629-444`
- Parent kit: `KIT_GIA_BloodAxeAshSlagFirewood_A01`
- Child intake row: `BloodAxeForge.png#Clutter_FirewoodStacks_TiedBundles`
- Faction/theme: Blood Axe Tribe, hostile Giant sub-faction only
- Status: production package documentation only; no DCC, FBX, Unreal Content asset, material graph, VFX, Blueprint, validator, startup placement, final approval, or implementation target is created or approved here

`SM_GIA_BloodAxeFirewoodBundles_A01` defines static tied log bundles and rough kindling groups for Blood Axe Giant camp dressing. The asset is static log dressing only, not a gatherable, consumable, pickup-enabled, destructible, crafting, resource, inventory, economy, rope-simulated, physics-simulated, DCC, Unreal implementation, final approval, or implementation-target object.

The Blood Axe Tribe remains a hostile Giant sub-faction. The bundles should look crude, heavy, and raider-made, with static hide straps or thick rope-wrap details used only as visual binding. They must stay separate from neutral/civilized Giant cave-town craft, polished timber storage, civic stonework, warm peaceful hearths, blue-gray masonry, restrained blue runes, terraces, waterworks, and master mason identity.

## Gameplay Purpose

The asset supports static environmental storytelling by showing bundled heavy fuel around hostile Blood Axe shelters, forge edges, and camp storage corners. It gives level artists a smaller companion shape to larger firewood stacks without adding gathering, pickup, resource, inventory, rope, physics, or crafting behavior.

Allowed purpose:

- Static bundled-log dressing only.
- Giant-scale fuel story for hostile Blood Axe camps.
- Visual pairing with firewood stacks, charcoal heaps, ash piles, slag, and scorched debris.
- Broad, readable bundle silhouettes that break up camp floors and wall edges.

Out of scope:

- Gatherable, consumable, pickup, destructible, crafting, resource, inventory, economy, loot, vendor, cooking, workstation, interaction, UI prompt, rope simulation, physics simulation, heat, damage, VFX, audio, DCC, Unreal implementation, final approval, or implementation-target behavior.

## Silhouette Notes

Primary read: heavy tied groups of rough logs and split kindling sized for Giants. The bundle should read as a static strapped prop, with broad log ends, thick visual bindings, uneven log lengths, and a squat stable footprint.

Required silhouette traits:

- Bundled horizontal log mass with clear long-axis read.
- Thick static hide straps or rope-wrap details as visual geometry or baked detail only.
- Uneven log ends and rough split faces.
- Charred tips and soot-darkened bark.
- Optional sparse red tag or cloth scrap that reads as Blood Axe dressing, not UI.
- No carry-handle read, pickup icon read, resource bundle read, destructible fracture staging, rope simulation, physics setup, or inventory presentation.

Model real geometry for major logs, bundle outline, broad strap forms, large split faces, and prominent charred ends. Use texture and normal detail for bark grain, small cuts, cord fibers, hide creases, fine splinters, soot, and knots.

## Scale Notes

Use the validated `SK_GIA_Base_A01` Giant scale lock exactly:

- Female Giant baseline: 442 cm / 14'6".
- Male Giant baseline: 470 cm / 15'5".
- Approved Giant ranges: females 14-15 ft / 427-457 cm; males 14'10"-16'0" / 452-488 cm.
- Author future source in centimeters. 1 Unreal unit = 1 cm.

Suggested production dimensions:

- Small bundle: 260-360 cm long, 80-150 cm deep, 60-100 cm high.
- Medium bundle: 360-500 cm long, 120-210 cm deep, 90-145 cm high.
- Large bundle: 500-650 cm long, 170-260 cm deep, 130-190 cm high.
- Individual bundle logs: 180-520 cm long and 18-65 cm thick.
- Binding width: 18-45 cm for static hide straps or rope-wrap silhouettes.
- Charred end-cap depth: 6-28 cm as material and slight geometry, not heat.

The bundles should feel too large for normal humanoids to gather or carry casually. Future scale review must compare against female 442 cm and male 470 cm Giants before any DCC or Unreal work.

## Materials and Color Palette

Primary material language:

- Dark bark and rough split wood.
- Charred black tips.
- Static hide straps or thick rope-wrap details.
- Soot, ash dust, and scuffed ground-contact grime.
- Restrained Blood Axe red cloth tag only if needed and not presented as interaction language.

Suggested palette:

- Charred bark: `#150D09` to `#332015`
- Split raw wood: `#6B4930` to `#A66E3C`
- Dry grain highlight: `#98724A` to `#BE8B55`
- Soot black: `#0B0A09` to `#24201C`
- Hide strap brown: `#2E1D14` to `#60402A`
- Rope fiber tan: `#6C5338` to `#93724D`
- Pale ash dust: `#8C8578` to `#B8AB98`
- Restrained Blood Axe red: `#5F1513` to `#842018`

No emissive color is planned. Avoid glowing coals, active fire orange, magical fuel, blue Aetherium, clean merchant-bundle presentation, resource highlight colors, or polished civilized Giant craft.

## Concept Image Prompt

Create an original stylized fantasy MMORPG concept image of `SM_GIA_BloodAxeFirewoodBundles_A01` for the world of Aerathea. The design should emphasize Giant-scale tied log bundles, rough split kindling groups, static hide straps or rope-wrap details, charred tips, dark bark, split raw wood, soot, ash dust, broad MMO-readable silhouettes, female 442 cm / 14'6" and male 470 cm / 15'5" Giant scale callouts, hostile Blood Axe raider camp identity, separation from neutral/civilized Giant culture, and a static log-dressing role only. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, no emissive glow, and MMO-friendly production design. Present it as a clean prop concept sheet with side, top, front, and three-quarter views, three bundle sizes, material swatches, and LOD/collision callouts. Avoid copying any existing franchise, avoid gatherable resource framing, pickup prompts, carry handles, destructible fracture diagrams, crafting or inventory UI, rope or physics simulation, active fire, smoke, sparks, heat shimmer, VFX, and excessive micro-detail that would not translate to a mid-poly Unreal asset.

## Modeling Notes

This is a docs-only modeling plan. No mesh, sculpt, retopo, UV, bake, collision proxy, proof render, FBX, Unreal import, material graph, VFX, Blueprint, validator, startup actor, runtime behavior, final approval, or implementation target is created or approved here.

Future modeling guidance:

- Build three reusable bundle variants: short heavy bundle, medium split-log bundle, and large rough trunk bundle.
- Use faceted cylinders and split-log forms with broad end caps.
- Use thick static bindings as simplified geometry or baked strap detail; do not plan rope simulation or physics behavior.
- Offset log lengths and rotations to avoid perfectly manufactured bundles.
- Keep the underside stable for ground placement.
- Add a few large cracked or split faces for readability.
- Avoid carry handles, detachable pickup logs, resource-count presentation, inventory-friendly bundle silhouettes, destructible fracture chunks, cooking hooks, rope simulation controls, physics setup, or interaction affordances.

Use real geometry for major logs, bundle silhouette, thick straps or rope-wrap bands, split faces, and large charred ends. Use texture and normal maps for bark grain, small cuts, cord fibers, hide folds, soot, knots, and fine splinters.

## Texture and Material Notes

Required future texture map set:

- Base Color / Albedo: `T_GIA_BloodAxeFirewoodBundles_A01_BC`
- Normal: `T_GIA_BloodAxeFirewoodBundles_A01_N`
- Packed Occlusion/Roughness/Metallic: `T_GIA_BloodAxeFirewoodBundles_A01_ORM`

Material slot target:

- Slot 0: bark, split wood, charred ends, soot, ash, and static binding details atlased into one material.
- Optional Slot 1: hide strap, rope-wrap, or sparse Blood Axe cloth accents only if later approved and not cleanly atlased.

Texture resolution target:

- 1K for standard bundle variants.
- 512 for small alternate bindings if split later.
- 1K to 2K maximum for a large bundle set if later approved.
- No 4K hero texture is planned.

Packed `ORM` guidance:

- R: strong occlusion between bundled logs, under straps, in split faces, and at ground contact.
- G: high roughness for bark, charred ends, dry split wood, hide, rope fibers, soot, and ash.
- B: metallic at 0.0 for the baseline asset.

No emissive map is planned. No material graph, shader, texture asset, or material instance is authored by this package.

## Triangle Budget

Target LOD0 budget:

- Small bundle: 1,800-3,000 tris.
- Medium bundle: 3,000-4,800 tris.
- Large bundle: 4,800-6,500 tris.
- Combined variant review mesh: keep under 13,000 tris if variants are temporarily composed for review by a later approved task.

Material slots:

- 1 material slot target.
- 2 material slots maximum only for optional binding or cloth material separation.

Spend geometry on log silhouettes, bundle mass, large split faces, thick bindings, and charred end caps. Do not spend geometry on fine cord fibers, tiny bark hairs, small knots, tiny splinters, ash specks, hairline cracks, or hidden log intersections.

## LOD Plan

All important variants require LOD0-LOD3.

- LOD0: full bundle silhouette, individual major logs, thick bindings, split faces, charred tips, and broad material zones.
- LOD1: 60-70 percent of LOD0; reduce small bevels, minor split cuts, small binding ridges, hidden intersections, and duplicate end-cap detail.
- LOD2: 35-45 percent of LOD0; merge interior logs, simplify bindings, reduce split faces, and remove non-silhouette log variation.
- LOD3: 15-25 percent of LOD0; preserve bundle footprint, long-axis read, thick binding silhouette, and major log-end rhythm.

LOD reduction order:

1. Cord fibers, bark hairlines, fine cracks, ash speckles, tiny splinters, and small knots.
2. Small binding ridges, minor split-face bevels, and hidden underside cuts.
3. Interior logs, duplicate log-end cuts, and non-silhouette binding detail.
4. Back-side and underside detail.
5. Main bundle mass and thick binding read only after smaller details are removed.

Never reduce the bundle into a generic cylinder before the Giant-scale tied-log read is preserved at distance.

## Collision Notes

Collision remains simple, static, and display-focused.

Recommended future collision:

- Collision disabled by default if used as purely visual dressing.
- If blocking is needed, use one or two simple boxes or convex hulls around the bundle mass.
- Keep walkable collision disabled.
- Do not use per-log, per-strap, or per-rope-wrap collision.

Do not add gatherable collision, pickup collision, consumable triggers, destructible fracture collision, crafting or resource volumes, inventory triggers, economy or loot volumes, rope simulation, physics simulation, cooking interaction, heat damage volumes, VFX collision, cover volumes, nav rules, or encounter hazard volumes.

## Animation Notes

Baseline asset is static.

Approved for this package:

- Fixed bundled-log silhouettes.
- Painted bark, split wood, soot, ash, and static binding variation only.
- No runtime motion claim.

Not included:

- Rope simulation, physics simulation, loosening bindings, rolling logs, falling logs, destructible collapse, burning states, smoke, sparks, embers, active flame, heat shimmer, animated material states, emissive pulsing, audio, interaction, gatherable behavior, pickup, crafting, resource, inventory, economy, cooking, or Blueprint state.

## Unreal Import Notes

This section is future planning only. No Unreal Content asset, import, material instance, texture asset, Blueprint, Niagara system, validator, startup actor, runtime source, final approval, or implementation target is created by this package.

Planned future asset type:

- Static Mesh: `SM_GIA_BloodAxeFirewoodBundles_A01`

Import planning:

- Author in centimeters and import at scale 1.0.
- Pivot at ground center of the bundle footprint, with long axis aligned for placement.
- Assign LOD0, LOD1, LOD2, and LOD3.
- Material slots: 1 target, 2 maximum if optional bindings are separated.
- Collision: disabled by default or one to two simple display hulls if explicitly needed later.
- Sockets: none.
- Animation list: none.
- Blueprint behavior: none.
- Performance note: preserve long-axis bundle read and thick binding silhouette; remove bark, cord, split, ash, and hidden intersection detail first.

Texture list:

- `T_GIA_BloodAxeFirewoodBundles_A01_BC`
- `T_GIA_BloodAxeFirewoodBundles_A01_N`
- `T_GIA_BloodAxeFirewoodBundles_A01_ORM`

## Folder and Naming Recommendation

Documentation path:

- `docs/assets/props/SM_GIA_BloodAxeFirewoodBundles_A01/PRODUCTION_PACKAGE.md`

Future planning folders, pending separate approval:

- Static Mesh: `/Game/Aerathea/Props/Giants/BloodAxeCamp/ForgeClutter/`
- Materials: `/Game/Aerathea/Materials/Giants/BloodAxe/`
- Textures: `/Game/Aerathea/Textures/Giants/BloodAxe/Camp/ForgeClutter/`

Recommended names:

- Static Mesh: `SM_GIA_BloodAxeFirewoodBundles_A01`
- Material Instance: `MI_GIA_BloodAxeFirewoodBundles_A01`
- Base Color: `T_GIA_BloodAxeFirewoodBundles_A01_BC`
- Normal: `T_GIA_BloodAxeFirewoodBundles_A01_N`
- ORM: `T_GIA_BloodAxeFirewoodBundles_A01_ORM`

Do not create or edit `Content/Aerathea`, `SourceAssets`, DCC files, FBX exports, Unreal imports, runtime source, tools, validators, startup placements, external concepts, global indexes, task-board files, backlog files, bootstrap files, or sibling package files from this task.

## Quality Gate Checklist

- Blood Axe remains a hostile Giant sub-faction, separate from neutral/civilized Giant culture.
- Female Giant baseline 442 cm / 14'6" and male Giant baseline 470 cm / 15'5" are preserved.
- Asset is static log dressing only.
- No gatherable, consumable, pickup, destructible, crafting, resource, inventory, economy, rope simulation, physics simulation, DCC, Unreal implementation, final approval, or implementation target is claimed.
- Silhouette uses broad Giant-scale log bundles, thick static bindings, uneven log ends, and stable footprints.
- Materials use dark bark, split raw wood, charred tips, hide or rope-wrap detail, soot, pale ash, restrained Blood Axe accents, and no emissive glow.
- Fine bark grain, cord fibers, tiny splinters, small knots, ash specks, and hairline cracks are texture or normal detail, not geometry.
- Triangle budget, LOD0-LOD3 plan, simple display collision guidance, texture map plan, and Unreal import planning are included.
- Folder and naming recommendations preserve `GIA` and `BloodAxe` naming.
- Package remains docs-only and does not modify external source concepts, global indexes, task board, DCC, Unreal, source, tools, validators, Hermes files, or unrelated packages.
