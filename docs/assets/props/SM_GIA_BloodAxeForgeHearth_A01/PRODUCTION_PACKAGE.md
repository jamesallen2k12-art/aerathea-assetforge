# SM_GIA_BloodAxeForgeHearth_A01 Production Package

## Art Direction Summary

- Asset name: `SM_GIA_BloodAxeForgeHearth_A01`
- Asset type: Static Mesh production package / hostile Blood Axe Giant forge hearth and windbreak prop
- Task: `AET-MA-20260629-110`
- Parent route: `KIT_GIA_BloodAxeCamp_A01#Zone_ForgeHearth`
- Source route reference: `BloodAxeForge.png#Zone_ForgeHearth`
- Related planning references: `KIT_GIA_BloodAxeCamp_A01`, `KIT_GIA_BloodAxeReforging_A01`, `SK_GIA_BloodAxeForgeGuard_A01`, and `MI_GIA_BloodAxeReforgedMetal_A01`
- Faction/theme: Blood Axe Tribe, hostile Giant sub-faction only
- Status: docs-only production package ready; no DCC, FBX, Unreal Content, material graph, VFX, runtime source, validator, startup placement, first build target selection, final visual approval, or source concept movement is included
- Source-storage guardrail: external source concept images remain outside the repository. Do not copy, move, edit, crop, embed, rename, or commit external source concepts for this package.

`SM_GIA_BloodAxeForgeHearth_A01` defines a static visual forge hearth for hostile Blood Axe Giant camp spaces. It should read as a brutal field-forge anchor: a huge soot-blackened stone and scrap-metal firebox, crude windbreak slabs, coal and ash bed, slag crust, red warning cloth, blackened iron braces, and enough Giant-scale clearance to sell that 442 cm female Giants and 470 cm male Giants work around it.

The hearth is not a neutral Giant civic hearth. Blood Axe language must stay hostile, temporary, raider-built, and separate from civilized Giant mountain stonework, cave-town craft, blue-gray masonry, warm communal hearth culture, restrained blue runes, terraces, and waterworks.

This package is static visual production planning only. Soot, fire, ember, coal, and heat color are visual art-direction cues, not gameplay, VFX, material graph, damage, crafting, resource, economy, salvage, repair, or interaction behavior.

## Gameplay Purpose

The hearth supports non-interactive Blood Axe camp and forge-yard dressing. It gives environment artists a readable focal prop for hostile Giant production spaces without defining a functional workstation.

Allowed visual planning purpose:

- Mark a Blood Axe forge zone in hostile Giant camps.
- Support forge-yard composition near future anvil/quench, scrap sorting, cooling rack, forge guard, weapon rack, and reforging-process props.
- Provide a large static silhouette that explains soot, ash, slag, and crude field-forge activity at MMO camera distance.
- Preserve Giant scale and Blood Axe faction identity for future DCC and Unreal implementation tasks.

Out of scope:

- Crafting station behavior, repair loops, salvage loops, refining, recipes, upgrades, economy, resource nodes, harvestables, vendor data, inventory data, loot containers, pickup prompts, or UI markers.
- Heat damage, burn hazards, steam damage, fire damage, encounter hazards, damage volumes, destructible states, physics puzzles, or player interaction behavior.
- VFX authoring, Niagara systems, animated flames, smoke systems, heat shimmer, material graph authoring, emissive-state authoring, sound cues, Blueprint behavior, runtime source, validators, startup placement, first build target selection, final visual approval, DCC source, FBX export, Unreal import, or source concept movement.

## Silhouette Notes

Primary read: a Giant-scale hostile forge hearth with a low, heavy firebox and taller crude windbreak, built from ash-stained field stone, stolen metal slabs, and rough Blood Axe camp hardware.

Required silhouette elements:

- Broad rectangular or slightly U-shaped hearth body with a deep coal/ash basin.
- Heavy rear and side windbreak slabs that shield the forge bed and create an asymmetric, raider-built profile.
- Oversized blackened iron bands, brace plates, scrap-metal lips, and hammered corner clamps.
- Soot-blackened upper rim, ash banks, slag shelves, charcoal chunks, and cooled crusts as large readable masses.
- One or two red cloth warning strips, painted red slashes, or crude tags as Blood Axe identifiers.
- Optional large bellows-rest, tool-rest, or fuel-stack contact zones only as visual placement surfaces; the actual bellows, tools, anvil, quench trough, and scrap sorting are separate package lanes unless a later task approves variants.

Model real geometry for the hearth body, major stones, windbreak slabs, broad metal braces, basin lip, large coal chunks, large slag shelves, and main cloth or tag shapes. Use texture and normal detail for soot speckles, tiny cracks, small chips, dense pitting, fine ash dust, hairline scorch marks, tiny rivets, and minor hammer noise.

Avoid neutral/civilized Giant hearth warmth, polished masonry, orderly civic stonework, blue rune accents, clean master-smith presentation, normal humanoid forge scale, glowing interaction rings, quest markers, resource-node crystals, crafting UI plates, excessive flames, dense coal pebbles, per-stone clutter, graphic gore, or unreadable micro-detail.

## Scale Notes

Use the validated `SK_GIA_Base_A01` Giant scale lock exactly:

- Female Giant baseline: 442 cm / 14'6".
- Male Giant baseline: 470 cm / 15'5".
- Approved Giant ranges: females 14-15 ft / 427-457 cm; males 14'10"-16'0" / 452-488 cm.
- Author future source in centimeters. 1 Unreal unit = 1 cm.
- Normal humanoid compatibility is not required.

Recommended static hearth scale:

- Overall footprint: 520-850 cm wide, 360-620 cm deep.
- Hearth lip/work height: 150-240 cm, sized for Giant hands and tools.
- Basin depth: 55-120 cm below the lip, with coal and ash readable from normal camera height.
- Rear windbreak height: 300-520 cm, staying below full Giant head height so a 470 cm male Giant still reads over or beside it in composition.
- Side windbreak height: 220-420 cm, asymmetrical and rough-built.
- Main working lane in front: 500-700 cm clear width.
- Side service clearance: 350-500 cm minimum where a future level layout expects Giant passage.
- Red cloth/tags: 60-180 cm long so they read at Giant camp scale.

Future DCC validation must compare the hearth footprint, lip height, windbreak height, and work-lane clearance against both the 442 cm female and 470 cm male Giant baselines before any Unreal placement or visual approval. The hearth should feel too large and hostile for normal humanoids to operate casually.

## Materials and Color Palette

Primary material language:

- Ash-stained field stone and cracked hearth blocks, darkened by heavy soot and forge residue.
- Blackened iron, dark steel, and stolen/reforged metal braces using or matching `MI_GIA_BloodAxeReforgedMetal_A01`.
- Charcoal, coal crust, cooled slag, matte ash, oil-dark grime, and dark residue inside the basin.
- Scorched timber or hide only as optional windbreak supports, fuel rests, or red-cloth tie points.
- Deep oxide red cloth, chipped red paint, or crude warning tags as restrained Blood Axe identifiers.
- Warm forge orange and coal red only as painted visual color on coal/ember areas unless a later material/VFX task approves emissive or active fire states.

Suggested palette:

- Soot black: `#0B0A09` to `#24201C`
- Ash gray: `#6A6458` to `#8A8275`
- Burned field stone: `#2B2B27` to `#575247`
- Blackened iron: `#151719` to `#2A2C2E`
- Worn dark steel: `#555A5C` to `#787B78`
- Oxide red cloth/paint: `#5F1513` to `#8B211B`
- Charcoal ember paint: `#8A3A19` to `#B45A24`, restrained and non-glowing by default
- Scorched leather or hide: `#241611` to `#4A2E20`

Avoid civilized Giant blue-gray stoneworker motifs, warm peaceful hearth symbolism, restrained blue runes, polished masonry, orderly cave-town craft, or shamanic storm language as the baseline. No default emissive is approved. Any forge-heat, active flame, glow, smoke, steam, or heat-shimmer state requires separate visual, material, VFX, and Unreal approval.

## Concept Image Prompt

Create an original stylized fantasy MMORPG concept image of `SM_GIA_BloodAxeForgeHearth_A01` for the world of Aerathea. The design should emphasize a hostile Blood Axe Giant forge hearth and windbreak, validated Giant scale with female 442 cm / 14'6" and male 470 cm / 15'5" baselines, a huge U-shaped soot-blackened firebox, crude ash-stained field stone, stolen scrap-metal braces, blackened iron lips, charcoal and slag basin, rough windbreak slabs, deep oxide red warning cloth, chipped red paint, soot, ash, grime, painted coal warmth as visual language only, Blood Axe raider sub-faction identity, and a static environment-dressing role rather than a crafting station. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, no default emissive glow, no VFX, and MMO-friendly mid-poly production design. Present it as a static prop production sheet with front, side, back, top-down footprint, scale callouts beside 442 cm female and 470 cm male Giants, material swatches, LOD/collision notes, and clear labels that it is non-interactive set dressing. Avoid copying any existing franchise, avoid making Blood Axe culture the default Giant culture, avoid neutral/civilized Giant warm-hearth motifs, avoid heat damage diagrams, avoid crafting/economy/resource UI, avoid interaction prompts, avoid final visual approval framing, and avoid excessive micro-detail that would not translate to a mid-poly Unreal asset.

## Modeling Notes

This is a docs-only modeling plan. No mesh, sculpt, retopo, UV, bake, collision proxy, proof render, FBX, Unreal import, material graph, VFX, Blueprint, validator, startup actor, runtime behavior, or final visual approval is created or approved here.

Future modeling should prioritize large readable forms:

- Hearth body: build a heavy U-shaped or rectangular firebox with thick stones, uneven stacked blocks, and a deep basin.
- Windbreak: model rear and side slabs as large crude pieces, reinforced with blackened metal bands or stolen shield plates.
- Basin and lip: create a broad coal/ash bed, raised lip, slag shelves, and one or two large rest points for future visual tools.
- Metal hardware: model wide brace plates, corner bands, hammered rim strips, and a few oversized rivets where they are silhouette-readable.
- Red faction marks: model one or two cloth tags, red-painted metal slashes, or tied warning strips as bold shapes, not dense small flags.
- Ground contact: include ash buildup, soot falloff, and a rough base footprint that can sit in packed earth or camp forge-yard ground modules.
- Adjacency: leave clear visual space for separate `SM_GIA_BloodAxeAnvilQuench_A01`, `KIT_GIA_BloodAxeForgeScrapSorting_A01`, `KIT_GIA_BloodAxeReforging_A01`, and forge guard assets. Do not collapse those into this hearth mesh.

Use texture, normal maps, or material masks for:

- Fine stone cracks.
- Small soot speckles.
- Ash dust.
- Tiny chips.
- Dense pitting.
- Small hammer marks.
- Minor weld scars.
- Hairline scorch marks.
- Small red paint chips.
- Fine charcoal breakup.

Do not add gameplay affordance geometry such as glowing rings, button plates, recipe boards, progress meters, resource crystals, pickup handles, UI labels, loot beams, harvest outlines, destructible fracture chunks, or hazard boundary markers.

## Texture and Material Notes

Required future map set:

- Base Color / Albedo (`BC`)
- Normal (`N`)
- Packed Occlusion/Roughness/Metallic (`ORM`)

No material graph, shader, material instance, texture asset, emissive map, VFX graph, or Unreal import is authored by this package.

Material slot target:

- Slot 0: planned soot/ash/stone material for hearth blocks, ash banks, basin residue, and burned field stone.
- Slot 1: `MI_GIA_BloodAxeReforgedMetal_A01` or a consuming Blood Axe hardware instance for blackened braces, scrap-metal lips, stolen shield plates, bands, and broad red paint masks.
- Slot 2: planned scorched timber/hide/red-cloth support material for optional windbreak supports, warning strips, tags, and tie points.
- Optional future slot 3: approval-gated coal/ember or forge-heat material state only if a later visual/material/VFX task promotes an active-fire variant. Baseline `A01` does not author this slot.

Texture naming examples:

- `T_GIA_BloodAxeForgeHearth_A01_BC`
- `T_GIA_BloodAxeForgeHearth_A01_N`
- `T_GIA_BloodAxeForgeHearth_A01_ORM`
- `T_GIA_BloodAxeForgeHearth_StoneAsh_A01_BC`
- `T_GIA_BloodAxeForgeHearth_CoalSlag_A01_BC`
- `T_GIA_BloodAxeForgeHearth_Hardware_A01_BC`
- Future approval-gated only: `T_GIA_BloodAxeForgeHearth_A01_E`

Texture resolution targets:

- Default camp prop: 2K texture set.
- Repeated background or distant variant: 1K texture set.
- Close-up hero forge-yard variant: 2K, with 4K only if a later hero-review task explicitly approves it.

Packed `ORM` guidance:

- R: strong ambient occlusion under stone overlaps, basin lip, metal bands, windbreak joints, slag shelves, and cloth ties.
- G: high roughness for soot, ash, coal, burned stone, scorched hide, and matte blackened metal; slightly lower roughness only on worn steel edges.
- B: metallic only for iron, steel, scrap plates, braces, bands, rivets, and stolen shield fragments.

Keep soot broad and directional so it supports the hearth silhouette. Do not fill the asset with high-frequency ash noise, tiny crack carpets, or red paint overuse.

## Triangle Budget

Default static hearth target:

- LOD0: 9k-18k tris.
- LOD0 hard cap: 22k tris for a larger hero forge-yard variant with a broader windbreak and richer basin silhouette.
- Material slots: 3 target, 4 maximum only for a separately approved active-fire or hero-review variant.
- Texture target: 2K default.

Variant guidance:

- Compact repeated camp hearth: 6k-10k tris, 2-3 material slots.
- Standard hearth and windbreak: 9k-18k tris, 3 material slots.
- Hero forge-yard hearth with expanded base, larger windbreak, and more readable slag/brace shapes: 16k-22k tris, 3-4 material slots by approval.

Spend geometry on the hearth mass, windbreak slab outline, basin depth, major stones, broad braces, large coal chunks, slag shelves, and red faction shapes. Do not spend geometry on tiny ash pebbles, dense cracks, soot specks, small rivets, fine pitting, micro hammer marks, per-coal clutter, or many individual stone chips.

## LOD Plan

All important hearth variants require LOD0-LOD3.

- LOD0: full hearth body, basin lip, windbreak slabs, major stones, broad metal braces, large coal/slag forms, red cloth/tag shapes, large soot/ash value breaks, and readable ground-contact footprint.
- LOD1: 60-70 percent of LOD0; reduce small stone chips, minor brace bevels, secondary coal chunks, cloth edge cuts, small rivets, and inner basin subdivisions.
- LOD2: 35-45 percent of LOD0; simplify stone stack interiors, metal band bevels, windbreak back-side detail, slag shelf cuts, red tag folds, and coal-bed breakup while preserving hearth and windbreak read.
- LOD3: 15-25 percent of LOD0; preserve the U-shaped or rectangular hearth silhouette, tall windbreak mass, dark basin block, red Blood Axe accents, and broad soot/ash material zones.

LOD reduction order:

1. Tiny cracks, ash flecks, soot speckles, small chips, and minor red paint flakes.
2. Small rivets, minor metal band bevels, cloth edge nicks, and fine coal shapes.
3. Secondary coal chunks, slag bubbles, small tied strips, and inner basin detail.
4. Back-side windbreak detail and underside stone overlaps.
5. Secondary stone bevels and non-silhouette brace cuts.
6. Only after secondary details are reduced, simplify the hearth body, basin lip, windbreak slabs, and main red/black faction read.

Never reduce the Giant-scale footprint, hearth opening, windbreak silhouette, or dark forge-basin read before removing small detail.

## Collision Notes

Collision remains simple, static, and display-focused.

Recommended future collision:

- Hearth body: low-count convex hull or grouped boxes around the main stone/firebox footprint.
- Basin: no detailed inner collision; use a simple blocked volume only if the basin must prevent player entry.
- Windbreak slabs: simple boxes or low-count convex hulls following the broad wall shapes.
- Metal braces, coal chunks, cloth tags, slag shelves, ash piles, and small protrusions: no individual collision.
- Ground-contact ash and soot: no collision.
- Optional hero base stones: fold into the main hull; do not add per-stone collision.

Do not add heat damage volumes, burn hazards, crafting interaction volumes, salvage triggers, resource harvesting volumes, pickup collision, loot outlines, recipe zones, economy/resource triggers, destructible fracture collision, physics-simulated coal, per-stone collision, per-coal collision, per-chain collision, VFX collision, or encounter hazard volumes.

Walkable collision should be disabled by default on the hearth, basin, windbreak, and rim unless a later level-design task explicitly promotes a variant for traversal or cover.

## Animation Notes

Baseline asset is static.

Approved for this docs-only package:

- Static mesh with fixed hearth, windbreak, coal, ash, slag, and red-cloth silhouettes.
- Painted non-emissive coal warmth or soot gradients as visual material language only.
- No runtime motion claim.

Approval-gated future work:

- Active flame or ember VFX.
- Smoke, steam, sparks, heat shimmer, or quench effects.
- Animated material states, emissive maps, pulsing heat, or bloom.
- Bellows motion, hammering loops, forge work loops, tool animation, physics-simulated coal, destructible states, or hanging prop sway.
- Any interaction, crafting, salvage, repair, heat gameplay, burn damage, encounter hazard, audio cue, or Blueprint state.

Baseline `A01` stays inert set dressing.

## Unreal Import Notes

This section is planning only. No Unreal Content asset, material instance, texture, Blueprint, Niagara system, validator, startup actor, runtime source, or import script is created by this package.

Planned future Unreal asset:

- Asset name: `SM_GIA_BloodAxeForgeHearth_A01`
- Asset type: Static Mesh
- Planned folder: `/Game/Aerathea/Environment/Giants/BloodAxeCamp/Props/Forge/`
- Planned material folder: `/Game/Aerathea/Materials/Giants/BloodAxe/`
- Planned texture folder: `/Game/Aerathea/Textures/Giants/BloodAxe/Camp/Forge/`
- Import scale: centimeter-authored source, import scale 1.0 after future DCC/export validation
- Pivot: ground-contact center of the hearth footprint, aligned to the full base footprint
- Orientation: primary open/work side faces +X unless a future project import convention overrides it
- Collision type: simple custom collision or generated primitive collision following the display-focused rules above
- LODs: LOD0, LOD1, LOD2, LOD3 required before production import approval
- Material slot count: 3 target, 4 maximum only for approved hero or active-fire variant
- Blueprint behavior: none
- Animation list: none
- Sockets: none required for baseline static mesh
- Performance notes: preserve hearth footprint, basin read, windbreak silhouette, and red/black Blood Axe material blocks; reduce soot noise, tiny chips, coal clutter, brace bevels, and back-side detail before primary silhouette.

Potential future sockets or markers, not authorized by this package:

- `hearth_coal_bed`
- `hearth_smoke_origin`
- `hearth_spark_origin`
- `hearth_tool_rest_l`
- `hearth_tool_rest_r`

These are planning notes only. Do not author sockets, VFX hooks, material states, Blueprint behavior, validator checks, or startup placement from this package.

Planned texture names:

- `T_GIA_BloodAxeForgeHearth_A01_BC`
- `T_GIA_BloodAxeForgeHearth_A01_N`
- `T_GIA_BloodAxeForgeHearth_A01_ORM`
- Optional future approval-gated `T_GIA_BloodAxeForgeHearth_A01_E`

Import guardrails:

- Do not import a Static Mesh, material, texture, Blueprint, Niagara system, validator, or startup actor from this docs-only package.
- Do not add crafting UI, resource behavior, economy data, salvage data, heat volumes, damage volumes, VFX graphs, material graphs, audio cues, loot tables, interaction prompts, or encounter logic.
- Do not claim final visual approval, final source concept approval, first DCC target selection, or production import readiness.

## Folder and Naming Recommendation

Docs:

- `docs/assets/props/SM_GIA_BloodAxeForgeHearth_A01/PRODUCTION_PACKAGE.md`

Planned future source/export paths, pending approval:

- Source: `SourceAssets/Blender/Props/Giants/BloodAxeCamp/SM_GIA_BloodAxeForgeHearth_A01/`
- Export: `SourceAssets/Exports/Props/Giants/BloodAxeCamp/SM_GIA_BloodAxeForgeHearth_A01.fbx`
- Unreal: `/Game/Aerathea/Environment/Giants/BloodAxeCamp/Props/Forge/`

Recommended future names:

- Static mesh: `SM_GIA_BloodAxeForgeHearth_A01`
- Compact repeated variant: `SM_GIA_BloodAxeForgeHearth_Compact_A01`
- Hero forge-yard variant, if approved: `SM_GIA_BloodAxeForgeHearth_Hero_A01`
- Stone/ash material instance: `MI_GIA_BloodAxeForgeHearth_StoneAsh_A01`
- Hardware material instance: `MI_GIA_BloodAxeReforgedMetal_A01`
- Cloth/support material instance: `MI_GIA_BloodAxeForgeHearth_Support_A01`
- Textures: `T_GIA_BloodAxeForgeHearth_A01_BC`, `T_GIA_BloodAxeForgeHearth_A01_N`, `T_GIA_BloodAxeForgeHearth_A01_ORM`

Do not create or edit `Content/Aerathea`, `SourceAssets`, DCC files, FBX exports, Unreal imports, runtime source, tools, validators, startup placements, external concept folders, global indexes, task-board files, backlog files, bootstrap files, or any package outside this owned docs path from this task.

## Approval Gates and Stop Points

- Stop before final Forge Hearth visual approval, final silhouette lock, first playable visual signoff, or first DCC target selection.
- Stop before creating source folders, Blender files, sculpt files, retopo files, UVs, bakes, proof renders, LOD sources, collision proxies, FBX exports, Unreal imports, material graphs, textures, Blueprints, Niagara systems, validators, or startup placements.
- Stop before copying, moving, embedding, cropping, editing, renaming, or committing external source concepts.
- Stop before adding VFX, active flames, smoke, steam, sparks, heat shimmer, emissive maps, animated material states, bloom, audio cues, or material graph behavior.
- Stop before defining heat damage, burn damage, crafting, repair, salvage, refining, recipes, upgrade benches, economy, vendor, inventory, resource harvesting, loot, pickup, interaction prompts, UI markers, destructible behavior, physics puzzles, or encounter hazards.
- Stop before adding Blueprint behavior, runtime source, gameplay tags, data assets, resource tables, economy data, loot tables, validators, navmesh requirements, startup actors, or first build target selection.
- Stop before merging anvil/quench, scrap sorting, bellows, cooling rack, process line, or forge-guard content into this hearth unless a later approved package explicitly expands scope.
- Stop if the asset requires changing the validated Giant scale lock or `SK_GIA_Base_A01` assumptions.
- Stop if Blood Axe red-black raider language starts replacing neutral/civilized Giant culture.
- Stop if soot/fire language starts reading as implemented gameplay, active VFX, heat hazard, interactable crafting, or final visual approval instead of static visual production language.

## Quality Gate Checklist

- Blood Axe remains a hostile Giant sub-faction, separate from neutral/civilized Giant culture.
- Validated Giant scale lock is explicit: female baseline 442 cm / 14'6", male baseline 470 cm / 15'5", approved range females 14-15 ft / 427-457 cm and males 14'10"-16'0" / 452-488 cm.
- Package describes a static forge hearth and windbreak, not anvil/quench, scrap sorting, full reforging process, crafting station, economy object, resource node, loot container, heat hazard, or interaction system.
- Soot, fire, coal, ember, ash, and heat color are visual-only art-direction cues; no VFX, material graph, emissive state, damage volume, active flame, smoke, steam, spark, or heat shimmer is authored.
- Primary silhouette reads at MMO distance: heavy hearth body, deep basin, crude windbreak, blackened braces, coal/ash mass, slag shelves, and restrained red Blood Axe identifiers.
- Materials use soot-blackened field stone, ash, charcoal, cooled slag, blackened iron, dark steel, scorched support materials, and oxide red warning accents consistently.
- No neutral/civilized Giant blue-gray civic stonework, warm peaceful hearth identity, restrained blue runes, polished masonry, or cave-town craft language is used as baseline.
- Tiny stone cracks, ash flecks, soot speckles, pitting, hammer marks, paint chips, coal breakup, and small rivets are assigned to textures or normals instead of geometry.
- Triangle budget, material slot target, texture map list, LOD0-LOD3 plan, collision notes, animation limits, Unreal import planning, folder/naming recommendation, stop gates, and source-storage guardrails are included.
- Package makes no DCC, FBX, Unreal Content, runtime source, material graph, VFX, validator, startup placement, first build target selection, final visual approval, source concept movement, index edit, task-board edit, backlog edit, bootstrap edit, or unrelated package edit claim.
