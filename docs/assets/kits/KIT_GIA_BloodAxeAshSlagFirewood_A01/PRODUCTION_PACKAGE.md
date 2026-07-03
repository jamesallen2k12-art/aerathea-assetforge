# KIT_GIA_BloodAxeAshSlagFirewood_A01 Production Package

## Art Direction Summary

- Asset name: `KIT_GIA_BloodAxeAshSlagFirewood_A01`
- Asset type: Production kit / static Blood Axe Giant forge and camp clutter split
- Task: `AET-MA-20260629-142`
- Parent intake row: `KIT_GIA_BloodAxeCamp_A01#Clutter_AshSlagFirewood`
- Source route reference: `BloodAxeForge.png#Clutter_AshSlagFirewood`
- Related packages: `KIT_GIA_BloodAxeCamp_A01`, `SM_GIA_BloodAxeForgeHearth_A01`, `SM_GIA_BloodAxeAnvilQuench_A01`, `KIT_GIA_BloodAxeForgeScrapSorting_A01`, `SM_GIA_BloodAxeCookingPit_A01`, and `MI_GIA_BloodAxeReforgedMetal_A01`
- Faction/theme: Blood Axe Tribe, hostile Giant sub-faction only
- Status: docs-only production package ready; no DCC, FBX, Unreal Content, material graph, VFX, runtime source, validator, startup placement, first DCC target selection, final visual approval, or source concept movement is included
- Source-storage guardrail: external source concept images remain outside the repository. Do not copy, move, edit, crop, embed, rename, inspect for visual approval, or commit external source concepts for this package.

`KIT_GIA_BloodAxeAshSlagFirewood_A01` defines the inert forge and camp clutter that sits around Blood Axe hearths, quench zones, cooking pits, and rough shelter edges: ash piles, cooled slag lumps, charcoal heaps, Giant-scale firewood stacks, scorched debris, and review composition rows. The kit should read as a brutal, soot-heavy field-camp residue layer, not as a functional resource system.

The Blood Axe Tribe remains a hostile Giant sub-faction. This kit must stay separate from neutral/civilized Giant culture such as hidden cave-town terraces, blue-gray master stonework, warm communal hearths, restrained blue runes, peaceful highland masonry, and civic forge craft. The visual language is raider-built, temporary, dirty, and practical: black ash, matte slag, charred wood, snapped fuel, red warning cloth, and small fragments of blackened stolen metal.

Ash, slag, charcoal, scorched wood, and soot are static visual art-direction cues only. They do not authorize gatherable resource behavior, heat or damage behavior, VFX or material graph authoring, crafting or economy behavior, interaction behavior, startup placement, DCC source creation, FBX export, Unreal import, or first DCC target selection.

## Gameplay Purpose

The kit supports non-interactive environmental storytelling for hostile Blood Axe camps and forge yards. It gives level artists a controlled static dressing vocabulary for the dirty residue around forge hearths, quench areas, cooking pits, log stores, and ruined work edges without implying gameplay systems.

Allowed visual planning purpose:

- Add ash banks and soot falloff around `SM_GIA_BloodAxeForgeHearth_A01` without merging into the hearth mesh.
- Provide cooled slag lumps and slag banks that support the forge story without becoming metal resources.
- Provide charcoal heaps and broken fuel piles that read at Giant scale.
- Provide firewood stacks sized for female 442 cm / 14'6" and male 470 cm / 15'5" Giants.
- Provide scorched debris rows for hostile camp edges, forge corners, and burned work lanes.
- Provide review composition rows that let a later DCC or Unreal review compare child silhouettes, material variants, scale, and LOD density.

Out of scope:

- Gatherable resources, resource nodes, firewood pickups, charcoal pickups, ore or slag harvesting, salvage systems, inventory items, loot drops, resource tables, crafting stations, recipes, upgrades, vendors, economy data, UI markers, or pickup prompts.
- Heat damage, burn damage, fire hazards, damage volumes, hot-surface gameplay, destructible burning states, physics puzzles, cover behavior, nav behavior, encounter hazards, or interaction behavior.
- VFX authoring, Niagara systems, animated smoke, sparks, ember particles, heat shimmer, material graph authoring, emissive-state authoring, shader work, Blueprint behavior, runtime source, validators, startup placement, first build target selection, final visual approval, DCC source, FBX export, Unreal import, or source concept movement.

## Silhouette Notes

Primary read: a low, heavy, dirty Blood Axe forge-clutter kit made of broad ash banks, matte cooled slag, broken black charcoal, crude Giant-scale logs, and charred debris rows. It should make a Blood Axe camp feel used and hostile while remaining readable as inert set dressing.

Required child silhouette reads:

- Ash piles: low wind-swept banks and shoveled heaps with soft broad mounds, dark soot cores, and pale gray edges.
- Slag lumps: cooled black-gray clumps, crusted shards, lumpy spill strips, and tray-adjacent residue with irregular chunky outlines.
- Charcoal heaps: broken matte black chunks, crushed fuel mounds, and rough sacks or shallow bins only as static support shapes.
- Firewood stacks: Giant-scale rough logs, split trunks, tied bundles, low crib stacks, leaning fuel rows, and charred end caps.
- Scorched debris: burned beams, broken plank sections, snapped stakes, collapsed log ends, ash-stained stones, bent blackened plate scraps, and restrained red cloth tags.
- Review composition rows: deliberate lineup rows that compare ash, slag, charcoal, wood, debris, and material variants at consistent scale.

Model real geometry for main mound forms, large slag chunks, log bodies, stack silhouettes, broad debris beams, shallow tray shapes, large broken charcoal chunks, row dividers, and red cloth tags. Use texture and normal detail for soot speckles, fine ash dust, small cracks, bark grain, tiny charcoal pores, slag bubbles, hairline scorch marks, minor chips, small nails, and tiny metal pitting.

Avoid treasure-pile silhouettes, shiny ore piles, crystal resource reads, collectible firewood bundles, UI-friendly pickup shapes, glowing coals, active flame language, dense tiny debris, polished civilized Giant craft, warm civic hearth mood, readable text labels, excessive red cloth, graphic gore, or micro-detail that would not translate to mid-poly static meshes.

## Scale Notes

Use the validated `SK_GIA_Base_A01` Giant scale lock exactly:

- Female Giant baseline: 442 cm / 14'6".
- Male Giant baseline: 470 cm / 15'5".
- Approved Giant ranges: females 14-15 ft / 427-457 cm; males 14'10"-16'0" / 452-488 cm.
- Author future source in centimeters. 1 Unreal unit = 1 cm.
- Normal humanoid compatibility is not required.

Suggested production scale targets:

- Full clutter kit review layout: 1000-1800 cm wide, 500-1000 cm deep, split into modular child rows rather than one collapsed mesh.
- Forge-adjacent static cluster: 650-1300 cm wide, 350-850 cm deep, kept below major hearth and anvil silhouettes.
- Ash piles: 180-600 cm wide, 90-380 cm deep, 15-90 cm high.
- Slag lump sets: 120-420 cm wide per cluster, 60-260 cm deep, 20-110 cm high; individual large lumps can be 35-140 cm across.
- Charcoal heaps: 160-500 cm wide, 90-320 cm deep, 30-140 cm high.
- Firewood stacks: 300-850 cm long, 130-360 cm deep, 90-260 cm high; individual Giant-scale logs can be 240-620 cm long and 30-95 cm thick.
- Scorched debris rows: 300-900 cm long, 80-260 cm deep, 40-220 cm high, with vertical broken stakes kept sparse.
- Review composition rows: 1200-2200 cm long, 250-600 cm deep per row, with consistent spacing and optional static scale markers only in future review scenes.

Future DCC validation must compare the child pieces and any composed rows against both the female 442 cm and male 470 cm Giant baselines before any Unreal placement or visual approval. The kit should feel too large and heavy for normal humanoids to treat as casual handheld clutter.

## Materials and Color Palette

Primary material language:

- Matte ash, gray soot, black dust, and pale forge residue.
- Cooled slag in black, dark gray, iron blue-gray, and dull brown crust tones.
- Charcoal chunks with blackened bark, dull fracture planes, and soft gray ash edges.
- Firewood with dark bark, split raw interiors, smoke stains, and charred ends.
- Scorched debris with burned timber, blackened field stone, dull metal scraps, scorched hide ties, and restrained deep red Blood Axe cloth.
- Optional blackened metal scraps can reference `MI_GIA_BloodAxeReforgedMetal_A01`, but metal stock and organized scrap sorting remain owned by `KIT_GIA_BloodAxeForgeScrapSorting_A01`.

Suggested palette:

- Soot black: `#0B0A09` to `#24201C`
- Ash gray: `#5F5B52` to `#9A9386`
- Pale ash edge: `#B5AA98` to `#D0C3AA`
- Cooled slag black: `#141414` to `#2B2A27`
- Oxidized slag brown: `#4B3021` to `#6D432B`
- Charcoal fracture gray: `#30302C` to `#5B5A51`
- Charred bark: `#1D130F` to `#3C261B`
- Split raw wood: `#6A4930` to `#A36C3A`
- Oxide red cloth or paint: `#5F1513` to `#8B211B`

Avoid neutral/civilized Giant blue-gray civic masonry, warm peaceful hearth symbolism, restrained blue runes, polished stoneworker craft, cave-town terrace language, bright resource-node colors, default emissive glow, active orange fire, magical fuel, or shamanic storm language as the baseline.

## Concept Image Prompt

Create an original stylized fantasy MMORPG concept image of `KIT_GIA_BloodAxeAshSlagFirewood_A01` for the world of Aerathea. The design should emphasize hostile Blood Axe Giant forge and camp clutter, validated Giant scale with female 442 cm / 14'6" and male 470 cm / 15'5" baselines, low ash piles, cooled slag lumps, matte charcoal heaps, Giant-scale firewood stacks, scorched debris, deliberate review composition rows, soot black, ash gray, cooled slag, charred bark, split raw wood, blackened stolen metal scraps, restrained oxide red cloth tags, Blood Axe raider sub-faction identity, and a static environment-dressing role rather than resource, crafting, heat, interaction, or VFX gameplay. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, no default emissive glow, and MMO-friendly mid-poly production design. Present it as a clean production asset board with child split labels, top-down row callouts, scale callouts beside a female 442 cm Giant and a male 470 cm Giant, material swatches, LOD/collision notes, and clear labels that all pieces are non-interactive set dressing. Avoid copying any existing franchise, avoid making Blood Axe culture the default Giant culture, avoid neutral/civilized Giant cave-town motifs, avoid gatherable resource UI, avoid heat damage diagrams, avoid crafting/economy markers, avoid interaction prompts, avoid active flames, avoid smoke or particle VFX, and avoid excessive micro-detail that would not translate to a mid-poly Unreal asset.

## Modeling Notes

This is a docs-only modeling plan. No mesh, sculpt, retopo, UV, bake, collision proxy, proof render, FBX, Unreal import, material graph, VFX, Blueprint, validator, startup actor, runtime behavior, or final visual approval is created or approved here.

Future modeling should build reusable child meshes and a few composed review rows:

- Ash piles: build low mound modules with broad soft silhouettes, darker cores, pale edges, and shallow shovel cuts.
- Slag lumps: build irregular cooled clumps, spill strips, and crusted bank modules with large forms and sparse surface pores.
- Charcoal heaps: build broken large charcoal chunks and mound modules with a few silhouette chunks on top.
- Firewood stacks: build rough log stacks, tied bundles, split-log rows, and leaning piles with clear Giant-scale log thickness.
- Scorched debris: build burned beams, broken stakes, ash-stained stones, bent plate scraps, red cloth tags, and collapsed camp edge pieces.
- Review rows: build layout-only arrangements that compare children in ordered lines and leave clear ground spacing for scale review. These rows are review planning only, not startup placement.

Use real geometry for primary mound silhouettes, log cylinders, split trunk planes, large slag chunks, broad charcoal pieces, broken beams, major metal scraps, row dividers, and large cloth tags. Use texture and normal detail for bark grain, fine ash dust, soot falloff, slag bubbles, tiny pores, small cracks, minor chips, tiny nails, pitting, and hairline scorch marks.

Do not add gameplay affordance meshes such as glowing interaction rings, pickup handles, harvest outlines, resource-node crystals, loot beams, recipe boards, progress meters, economy tags, hot-surface warning plates, damage-radius markers, UI labels, destructible fracture chunks, physics-simulated loose logs, or quest markers.

## Texture and Material Notes

Required future map set:

- Base Color / Albedo (`BC`)
- Normal (`N`)
- Packed Occlusion/Roughness/Metallic (`ORM`)

No material graph, shader, material instance, texture asset, emissive map, VFX graph, or Unreal import is authored by this package. No emissive map is planned for baseline `A01`.

Material slot plan:

- Slot 0: planned ash/slag/charcoal material for ash banks, soot, cooled slag, charcoal chunks, pale ash edges, and dark residue.
- Slot 1: planned scorched wood material for firewood stacks, charred beams, split logs, bark, and burned plank debris.
- Optional slot 2: `MI_GIA_BloodAxeReforgedMetal_A01` or a consuming Blood Axe hardware instance for rare bent plate scraps, blackened nails, broken bands, and red paint masks.
- Optional slot 3: planned red cloth/hide tie material only if cloth tags cannot be cleanly atlased with Slot 1. Keep this slot optional and sparse.

Texture naming examples:

- `T_GIA_BloodAxeAshSlagFirewood_A01_BC`
- `T_GIA_BloodAxeAshSlagFirewood_A01_N`
- `T_GIA_BloodAxeAshSlagFirewood_A01_ORM`
- `T_GIA_BloodAxeAshPiles_A01_BC`
- `T_GIA_BloodAxeSlagLumps_A01_BC`
- `T_GIA_BloodAxeCharcoalHeaps_A01_BC`
- `T_GIA_BloodAxeFirewoodStacks_A01_BC`
- `T_GIA_BloodAxeScorchedDebris_A01_BC`

Texture resolution targets:

- Small repeated child props: 512 to 1K texture sets.
- Firewood stacks, scorched debris rows, and composed clusters: 1K to 2K texture sets.
- Review composition rows: reuse child materials; do not create unique hero textures unless a later review task approves it.
- 4K is not planned for baseline camp clutter.

Packed `ORM` guidance:

- R: strong ambient occlusion under ash banks, log overlaps, slag bases, charcoal pile interiors, debris contacts, and cloth ties.
- G: high roughness for ash, soot, charcoal, scorched bark, burned wood, and cooled slag; slightly lower roughness only on rare worn metal edges.
- B: metallic only for rare blackened metal scraps, bent plates, nail heads, bands, and hardware fragments.

Keep ash and soot broad enough to support the silhouette. Do not fill the kit with high-frequency gray noise, tiny bark strokes, excessive red paint, or dense pebbled debris.

## Triangle Budget

Target LOD0 ranges:

- `SM_GIA_BloodAxeAshPiles_A01`: 800-3k tris per reusable pile set.
- `SM_GIA_BloodAxeSlagLumps_A01`: 1k-4k tris per lump cluster or spill strip.
- `SM_GIA_BloodAxeCharcoalHeaps_A01`: 1k-4k tris per heap set.
- `SM_GIA_BloodAxeFirewoodStacks_A01`: 2k-7k tris per stack or tied bundle set.
- `SM_GIA_BloodAxeScorchedDebris_A01`: 2k-8k tris per debris row set.
- `KIT_GIA_BloodAxeAshSlagFirewoodReviewRows_A01`: 8k-22k tris for an optional composed review layout built from reusable children.
- `SM_GIA_BloodAxeForgeClutterCluster_A01`: 6k-16k tris for an optional composed forge-adjacent static cluster.

Target material slots:

- Ash, slag, and charcoal child sets: 1 material slot where possible.
- Firewood stacks: 1-2 material slots.
- Scorched debris rows: 1-3 material slots depending on rare metal and cloth accents.
- Review rows and composed clusters: reuse child materials; 3 slots target, 4 maximum only if later approved.

Spend geometry on large mound profiles, log stack silhouettes, chunky slag shapes, broad charcoal pieces, broken beam outlines, and row composition. Do not spend geometry on fine ash dust, soot specks, bark hairlines, tiny pores, small nails, dense cracks, many individual pebbles, tiny splinters, or per-chip clutter.

## LOD Plan

All important child meshes and composed review rows require LOD0-LOD3.

- LOD0: full child silhouettes, ash mound profiles, large slag lumps, charcoal top chunks, log stack forms, scorched debris beams, rare metal scraps, red cloth tags, and broad material zones.
- LOD1: 60-70 percent of LOD0; reduce small bevels, secondary charcoal chunks, minor log-end cuts, small slag chips, cloth edge nicks, and duplicate loose fragments.
- LOD2: 35-45 percent of LOD0; simplify mound interiors, reduce slag chunk count, merge charcoal clusters, simplify log stack overlaps, reduce debris row interiors, and remove back-side details.
- LOD3: 15-25 percent of LOD0; preserve ash/slag/charcoal/wood/debris category reads, broad footprint, log-stack rhythm, dark residue mass, and restrained red Blood Axe accents.

LOD reduction order:

1. Tiny ash flecks, soot speckles, bark hairlines, fine slag pores, tiny chips, and small cracks.
2. Small nails, minor ties, cloth edge nicks, fine charcoal pieces, and small splinters.
3. Secondary slag chips, duplicate log cuts, non-silhouette debris pieces, and inner mound subdivisions.
4. Back-side or underside debris, concealed log overlaps, and non-visible ash-bank detail.
5. Secondary bevels and minor metal-scrap cuts.
6. Only after secondary details are reduced, simplify the main ash mound, slag lump, charcoal heap, firewood stack, scorched debris, and review-row footprints.

Never reduce the Giant-scale log thickness, clutter category read, review-row spacing, or broad ash/slag/charcoal silhouette before removing small detail.

## Collision Notes

Collision remains simple, static, and display-focused.

Recommended future collision:

- Ash piles: no collision or one shallow low-count hull around the broad mound if blocking is required.
- Slag lumps: grouped simple hulls or boxes around cluster footprints; no per-lump collision.
- Charcoal heaps: one low hull or box around the heap; no per-chunk collision.
- Firewood stacks: one to three simplified boxes or convex hulls around the stack mass; no per-log collision.
- Scorched debris rows: grouped hulls around the broad row footprint; no per-splinter, per-nail, per-cloth, or per-metal-scrap collision.
- Review composition rows: collision disabled by default unless a later review implementation task explicitly needs display collision.
- Walkable collision disabled by default for all pieces.

Do not add gatherable collision, pickup collision, harvest volumes, resource triggers, loot outlines, crafting interaction volumes, economy triggers, heat damage volumes, burn hazards, damage volumes, VFX collision, destructible fracture collision, physics-simulated logs, per-log collision, per-lump collision, per-charcoal collision, navmesh rules, cover volumes, or encounter hazard volumes.

## Animation Notes

Baseline kit is static.

Approved for this docs-only package:

- Static meshes with fixed ash, slag, charcoal, firewood, scorched debris, and review-row silhouettes.
- Painted soot, ash, and charred color variation as visual material language only.
- No runtime motion claim.

Approval-gated future work:

- Smoke, ember, spark, flame, heat shimmer, ash drift, or dust VFX.
- Animated material states, emissive maps, pulsing heat, bloom, or shader-driven glow.
- Physics-simulated falling logs, rolling charcoal, shifting ash, destructible burning debris, or wind movement.
- Any interaction, resource gathering, pickup, crafting, economy, heat damage, burn damage, encounter hazard, audio cue, UI marker, Blueprint state, or startup-scene behavior.

Baseline `A01` stays inert set dressing.

## Unreal Import Notes

This section is planning only. No Unreal Content asset, material instance, texture, Blueprint, Niagara system, validator, startup actor, runtime source, or import script is created by this package.

Planned future asset types:

- Static Mesh children for ash piles, slag lumps, charcoal heaps, firewood stacks, scorched debris, and optional composed clusters.
- Optional kit-level composed Static Mesh review rows for non-interactive production review only.
- Optional shared material instances for ash/slag/charcoal and scorched wood, pending a future material-authoring task.

Planned folders:

- `/Game/Aerathea/Props/Giants/BloodAxeCamp/ForgeClutter/`
- `/Game/Aerathea/Environment/Giants/BloodAxeCamp/Dressing/`
- `/Game/Aerathea/Materials/Giants/BloodAxe/`
- `/Game/Aerathea/Textures/Giants/BloodAxe/Camp/ForgeClutter/`

Planned naming:

- `SM_GIA_BloodAxeAshPiles_A01`
- `SM_GIA_BloodAxeSlagLumps_A01`
- `SM_GIA_BloodAxeCharcoalHeaps_A01`
- `SM_GIA_BloodAxeFirewoodStacks_A01`
- `SM_GIA_BloodAxeScorchedDebris_A01`
- `KIT_GIA_BloodAxeAshSlagFirewoodReviewRows_A01`
- `SM_GIA_BloodAxeForgeClutterCluster_A01`
- `MI_GIA_BloodAxeAshSlagCharcoal_A01`
- `MI_GIA_BloodAxeScorchedWood_A01`

Pivot planning:

- Ash piles: ground center of pile footprint.
- Slag lumps: ground center of cluster footprint.
- Charcoal heaps: ground center of heap footprint.
- Firewood stacks: ground center of stack footprint, long axis aligned for grid placement.
- Scorched debris rows: ground center of row footprint.
- Review rows: ground center of full review layout, with row axes clearly aligned.
- Composed clusters: ground center of full cluster footprint.

Import rules for any future build:

- Author in centimeters and import at scale 1.0.
- Assign LOD0, LOD1, LOD2, and LOD3 for all important static meshes.
- Target 1-2 material slots per child mesh and 3 material slots for composed clusters.
- Keep collision simple and display-only.
- Blueprint behavior: none.
- Animation list: none.
- Sockets: none required for baseline static clutter.
- Performance notes: preserve child category read and Giant-scale footprints; reduce ash dust, soot noise, bark strokes, tiny pores, minor chips, and back-side detail before primary silhouettes.

Do not create Blueprint interaction, gatherable resources, pickup prompts, heat damage, crafting recipes, resource nodes, economy data, loot tables, upgrade data, material graphs, shaders, VFX, startup placement, runtime source, validators, DCC source, FBX exports, Unreal imports, or final visual approval artifacts from this package.

## Folder and Naming Recommendation

Docs:

- `docs/assets/kits/KIT_GIA_BloodAxeAshSlagFirewood_A01/PRODUCTION_PACKAGE.md`
- `docs/assets/kits/KIT_GIA_BloodAxeAshSlagFirewood_A01/CHILD_ASSET_INTAKE.md`

Future child package recommendations, if promoted by later tasks:

- `docs/assets/props/SM_GIA_BloodAxeAshPiles_A01/`
- `docs/assets/props/SM_GIA_BloodAxeSlagLumps_A01/`
- `docs/assets/props/SM_GIA_BloodAxeCharcoalHeaps_A01/`
- `docs/assets/props/SM_GIA_BloodAxeFirewoodStacks_A01/`
- `docs/assets/props/SM_GIA_BloodAxeScorchedDebris_A01/`
- `docs/assets/kits/KIT_GIA_BloodAxeAshSlagFirewoodReviewRows_A01/`
- `docs/assets/props/SM_GIA_BloodAxeForgeClutterCluster_A01/`

Planned future source/export paths, pending separate approval:

- Source: `SourceAssets/Blender/Props/Giants/BloodAxeCamp/ForgeClutter/`
- Export: `SourceAssets/Exports/Props/Giants/BloodAxeCamp/ForgeClutter/`
- Unreal: `/Game/Aerathea/Props/Giants/BloodAxeCamp/ForgeClutter/`

Do not create or edit `Content/Aerathea`, `SourceAssets`, DCC files, FBX exports, Unreal imports, runtime source, tools, validators, startup placements, external concept folders, global indexes, task-board files, backlog files, bootstrap files, or any package outside this owned docs path from this task.

## Approval Gates and Stop Points

- Stop before final ash/slag/firewood visual approval, final silhouette lock, first playable visual signoff, or first DCC target selection.
- Stop before creating source folders, Blender files, sculpt files, retopo files, UVs, bakes, proof renders, LOD sources, collision proxies, FBX exports, Unreal imports, material graphs, textures, Blueprints, Niagara systems, validators, or startup placements.
- Stop before copying, moving, embedding, cropping, editing, renaming, inspecting for visual approval, or committing external source concepts.
- Stop before adding VFX, active flames, smoke, steam, sparks, heat shimmer, emissive maps, animated material states, bloom, audio cues, or material graph behavior.
- Stop before defining gatherable resource behavior, firewood pickup behavior, charcoal pickup behavior, slag harvesting, salvage loops, recipes, crafting, repair, refining, upgrades, economy, vendors, inventory, loot, pickup prompts, UI markers, destructible behavior, physics puzzles, interaction behavior, heat damage, burn damage, damage volumes, or encounter hazards.
- Stop before adding Blueprint behavior, runtime source, gameplay tags, data assets, resource tables, economy data, loot tables, validators, navmesh requirements, startup actors, or first build target selection.
- Stop before merging forge hearth, anvil/quench, scrap sorting, cooking pit, tool bucket, path marker, barricade, or shelter content into this clutter kit unless a later approved package explicitly expands scope.
- Stop if the asset requires changing the validated Giant scale lock or `SK_GIA_Base_A01` assumptions.
- Stop if Blood Axe red-black raider language starts replacing neutral/civilized Giant culture.
- Stop if ash, slag, charcoal, firewood, or heat language starts reading as implemented gameplay, active VFX, gatherable resource, heat hazard, interactable crafting, economy object, or final visual approval instead of static visual production language.

## Quality Gate Checklist

- Blood Axe remains a hostile Giant sub-faction, separate from neutral/civilized Giant culture.
- Validated Giant scale lock is explicit: female baseline 442 cm / 14'6", male baseline 470 cm / 15'5", approved range females 14-15 ft / 427-457 cm and males 14'10"-16'0" / 452-488 cm.
- Package describes static ash, slag, charcoal, firewood, scorched debris, and review-row dressing, not a forge hearth, anvil/quench, scrap-sorting station, resource node, loot pile, crafting station, economy object, heat hazard, VFX asset, or interaction system.
- Ash, slag, charcoal, soot, scorched wood, and heat residue are visual-only art-direction cues; no VFX, material graph, emissive state, damage volume, active flame, smoke, steam, spark, ash drift, or heat shimmer is authored.
- Child split covers ash piles, slag lumps, charcoal heaps, firewood stacks, scorched debris, and review composition rows.
- Primary silhouettes are readable at MMO distance and buildable as mid-poly static meshes.
- Materials use soot black, ash gray, cooled slag, charcoal, charred bark, split raw wood, rare blackened metal scraps, and restrained oxide red Blood Axe identifiers consistently.
- No neutral/civilized Giant blue-gray civic stonework, warm peaceful hearth identity, restrained blue runes, polished masonry, or cave-town craft language is used as baseline.
- Tiny soot speckles, ash flecks, bark hairlines, fine cracks, slag pores, pitting, chips, nail marks, and charcoal pores are assigned to textures or normals instead of geometry.
- Triangle budget, material slot target, texture map list, LOD0-LOD3 plan, collision notes, animation limits, Unreal import planning, folder/naming recommendation, stop gates, and source-storage guardrails are included.
- Package makes no DCC, FBX, Unreal Content, runtime source, material graph, VFX, validator, startup placement, first DCC target selection, final visual approval, source concept movement, index edit, task-board edit, backlog edit, bootstrap edit, or unrelated package edit claim.
