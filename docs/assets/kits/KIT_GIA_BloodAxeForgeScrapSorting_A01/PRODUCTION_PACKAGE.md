# KIT_GIA_BloodAxeForgeScrapSorting_A01 Production Package

## Art Direction Summary

- Asset name: `KIT_GIA_BloodAxeForgeScrapSorting_A01`
- Asset type: Production kit / static forge-yard dressing split
- Parent intake row: `KIT_GIA_BloodAxeCamp_A01` child `BloodAxeForge.png#Zone_ScrapSorting`
- Related packages: `KIT_GIA_BloodAxeScrapPile_A01`, `KIT_GIA_BloodAxeReforging_A01`, `SM_GIA_BloodAxeForgeHearth_A01`, future `SM_GIA_BloodAxeAnvilQuench_A01`
- Primary material dependency: `MI_GIA_BloodAxeReforgedMetal_A01`
- Faction/theme: Blood Axe Tribe, hostile Giant sub-faction
- Status: docs-only production package ready
- Scope guardrail: planning only; no DCC, FBX, Unreal Content, runtime source, resource/economy/crafting behavior, loot tables, interaction behavior, startup placement, or first DCC target selection.

`KIT_GIA_BloodAxeForgeScrapSorting_A01` defines the camp-local sorting zone beside a Blood Axe forge. It is more organized than `KIT_GIA_BloodAxeScrapPile_A01` and less procedural than the full `KIT_GIA_BloodAxeReforging_A01` process line: sorted metal piles, bent plate stacks, crude bins, broken weapon bundles, quenched slag, and path-safe clutter rows arranged to keep Giant-scale work lanes visually readable.

Blood Axe must remain a hostile Giant sub-faction, not neutral or civilized Giant culture. This kit belongs to brutal raider forge yards with blackened stolen metal, soot, rough bins, red warning cloth, and crude sorting discipline. It must stay separate from neutral/civilized Giant culture such as blue-gray masonry, hidden cave-town terraces, warm hearth craft, restrained blue runes, and peaceful highland stoneworker language.

## Gameplay Purpose

The kit supports non-interactive environmental storytelling for hostile Blood Axe camps and forge yards. It explains how raiders sort stolen armor, broken weapons, ruined plates, and quenched forge waste before the material moves toward armory or reforging props.

Expected visual uses:

- Forge-side dressing near `SM_GIA_BloodAxeForgeHearth_A01` and the future anvil/quench package.
- Camp-local transition between random scrap heaps and organized reforging workflow props.
- Giant-scale composition markers that help level artists keep clear visual work lanes around heavy forge dressing.
- Reusable static child assets for sorted piles, bins, stacks, bundles, slag, and path-safe clutter rows.
- Scale reference dressing beside female 442 cm / 14'6" and male 470 cm / 15'5" Giants.

Explicit exclusions:

- Not a loot pile, pickup, reward container, harvest node, resource node, inventory object, vendor object, economy object, salvage system, crafting station, upgrade bench, workstation, destructible prop, heat hazard, or interaction object.
- Not a navmesh, pathfinding, AI patrol, cover, encounter, or collision-behavior definition.
- Not a material graph, shader, VFX, DCC, FBX, Unreal import, runtime source, startup-scene, source concept, or final visual approval task.

## Silhouette Notes

Primary read: a low, heavy, Giant-scale sorting yard with ordered rows rather than a chaotic heap. The silhouette should communicate that hostile Blood Axe Giants sort stolen metal quickly and brutally, leaving usable pieces in broad rows and rejected material in slag/ash zones.

Required child silhouette reads:

- Sorted metal piles: low mounds of large plate chunks, snapped blade arcs, cut bars, and usable dark-metal stock.
- Bent plate stacks: leaning and stacked slabs of warped armor plates, shield faces, and failed forge plates with a clear broad-rectangle read.
- Crude bins: squat oversized bins made from dark timber, blackened plate, hide lashings, and heavy rims, filled with a few visible large pieces.
- Broken weapon bundles: tied or chained groups of snapped axe heads, cleaver pieces, spear tips, bow hardware, and ruined blades, not display-ready weapons.
- Quenched slag: matte black and gray lumps, crusted trays, ash banks, and cooled residue separated from usable stock.
- Path-safe clutter rows: low boundary rows that flank forge lanes without creating a dense hazard silhouette; they should read as intentional edge dressing, not random scatter.

Model the large rows, bin rims, plate slabs, broken blade silhouettes, chain loops, stock bars, slag chunks, tray bodies, and end-cap markers as geometry. Paint or normal-map pitting, soot streaks, hammer marks, tiny dents, small scratches, minor rivets, water stains, slag bubbles, and fine cracks.

Avoid treasure-pile silhouettes, shiny coin-like scrap, tiny unreadable shards, polished smithy order, neutral Giant stoneworker elegance, glowing interaction affordances, quest markers, or dense red clutter. Red cloth and chipped paint should mark Blood Axe hostility without overwhelming the blackened metal read.

## Scale Notes

Use the validated `SK_GIA_Base_A01` scale lock:

- Female Giant baseline: 442 cm / 14'6".
- Male Giant baseline: 470 cm / 15'5".
- Approved Giant ranges: females 14-15 ft / 427-457 cm; males 14'10"-16'0" / 452-488 cm.
- Author in centimeters. 1 Unreal unit = 1 cm.
- Normal humanoid compatibility is not required.

Suggested production scale targets:

- Full scrap-sorting composition: 900-1600 cm wide, 450-900 cm deep, split into modular child assets rather than one fixed mesh.
- Clear visual work lane between rows: 500-800 cm wide for Giant-scale staging; this is layout guidance only, not navmesh behavior.
- Sorted metal piles: 260-600 cm wide, 180-420 cm deep, 60-160 cm high.
- Bent plate stacks: 180-420 cm wide, 80-240 cm deep, 120-260 cm high, with individual plates 100-260 cm long.
- Crude bins: 220-380 cm wide, 140-260 cm deep, 100-190 cm high.
- Broken weapon bundles: 220-520 cm long, 100-240 cm wide, 60-180 cm high.
- Quenched slag trays or banks: 160-380 cm wide, 90-220 cm deep, 25-90 cm high.
- Path-safe clutter rows: 350-900 cm long per module, 60-160 cm deep, 40-120 cm high, with sparse vertical markers up to 220 cm.

Future DCC validation must compare all child pieces against the female 442 cm and male 470 cm Giant baselines before any Unreal placement or visual approval.

## Materials and Color Palette

Primary material dependency:

- `MI_GIA_BloodAxeReforgedMetal_A01` for blackened iron, dark steel, hammered stolen metal, broad worn edges, soot, grime, chipped oxide-red paint, and dull reforged plates.

Supporting material language:

- Matte cooled slag, charcoal dust, ash, quench stains, and dark water residue.
- Scorched timber and crude blackened plate for bins and row dividers.
- Scorched hide, heavy leather straps, thick rope, and large chain loops for bundles.
- Torn deep red cloth, crude red tags, and chipped red paint as restrained Blood Axe identifiers.
- Bone or trophy fragments only as rare background markers, never the main sorting read.

Avoid neutral/civilized Giant blue-gray stoneworker motifs, warm hearth presentation, restrained blue runes, polished cave-town masonry, terrace craft language, or peaceful highland nomad identity. No default emissive is planned. Any future forge-heat or shamanic glow variant requires separate approval and must remain restrained.

## Concept Image Prompt

Create an original stylized fantasy MMORPG concept image of `KIT_GIA_BloodAxeForgeScrapSorting_A01` for the world of Aerathea. The design should emphasize a hostile Blood Axe Giant forge-yard scrap sorting kit, sorted metal piles, bent plate stacks, crude bins, broken weapon bundles, quenched slag, path-safe clutter rows, blackened iron, dark steel, hammered stolen metal, matte slag, ash, soot, scorched timber, thick chains, chipped red paint, torn red warning cloth, Giant-scale work lanes, and `MI_GIA_BloodAxeReforgedMetal_A01` material language. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, no default emissive glow, and MMO-friendly production design. Present it as a clean production asset board and top-down layout callout with child split labels, scale callouts against a female 442 cm / 14'6" Giant and a male 470 cm / 15'5" Giant, material-slot notes, LOD/collision notes, and a clear label that it is non-interactive set dressing rather than loot, resource, crafting, economy, salvage, workstation, interaction, destruction, or startup gameplay. Avoid copying any existing franchise, avoid graphic gore, avoid making Blood Axe visual language the default Giant culture, avoid neutral/civilized Giant cave-town motifs, avoid player interaction markers, and avoid excessive micro-detail that would not translate to mid-poly Unreal assets.

## Modeling Notes

This is a docs-only package. Future modeling should build reusable child meshes and a few composed layout variants, not one collapsed scrap field.

- Sorted metal piles: build low mound modules with large plate chunks, cut bars, snapped blade arcs, and a small number of top-visible usable pieces.
- Bent plate stacks: build leaning slab groups with broad silhouettes, simple bevels, chipped corners, and sparse strap or chain control.
- Crude bins: build heavy bin shells with oversized rims, bent plate patches, timber braces, hide lashings, and a few large visible contents near the top.
- Broken weapon bundles: build tied or chained groups of broken axe heads, cleaver pieces, spear tips, blade fragments, and damaged fittings; avoid clean ready-to-equip weapon reads.
- Quenched slag: build shallow trays, ash banks, cooled slag lumps, and dark residue planes; use material roughness and normals for crust.
- Path-safe clutter rows: build long low boundary modules with deliberate spacing, end caps, red cloth tags, and sparse vertical markers that preserve clear visual lanes.
- Sorting markers: optional crude stakes, hammered plaques, or red tags can help distinguish usable stock, plate scrap, broken weapon pieces, and slag without relying on tiny readable text.

Use real geometry for primary masses, bin bodies, row shapes, plate slabs, large broken silhouettes, chain loops, broad bars, tray rims, and major markers. Use texture and normal detail for pitting, soot, hammer noise, fine scratches, tiny rivets, small weld scars, quench staining, and minor slag pores.

Do not add gameplay affordance meshes such as glowing interaction rings, pickup handles, harvest outlines, loot beams, resource-node crystals, recipe boards, progress meters, UI plaques, crafting station symbols, economy tags, destruction fracture cuts, or quest markers.

## Texture and Material Notes

Required map set for future texture work:

- Base Color / Albedo (`BC`)
- Normal (`N`)
- Packed Occlusion/Roughness/Metallic (`ORM`)

No emissive map is planned for baseline `A01`.

Material slot plan:

- Slot 0: `MI_GIA_BloodAxeReforgedMetal_A01` for metal piles, bent plates, broken weapon pieces, bin patches, chains, row caps, and dark stock.
- Optional slot 1: shared scorched wood/leather/cloth material for bin braces, hide lashings, red tags, rope, and timber dividers.
- Optional slot 2: matte slag/ash material for quenched slag trays or banks only if it cannot be cleanly atlased into Slot 0.

Texture naming examples:

- `T_GIA_BloodAxeForgeScrapSorting_A01_BC`
- `T_GIA_BloodAxeForgeScrapSorting_A01_N`
- `T_GIA_BloodAxeForgeScrapSorting_A01_ORM`
- `T_GIA_BloodAxeSortedMetalPiles_A01_BC`
- `T_GIA_BloodAxeBentPlateStacks_A01_BC`
- `T_GIA_BloodAxeCrudeScrapBins_A01_BC`
- `T_GIA_BloodAxeBrokenWeaponBundles_A01_BC`
- `T_GIA_BloodAxeQuenchedSlag_A01_BC`
- `T_GIA_BloodAxePathSafeClutterRows_A01_BC`

Use 1K texture sets for small repeated children, 2K for composed row/bin/bundle variants, and 4K only if a later hero forge scene specifically approves close-up use. Keep red paint and cloth masks restrained so the kit reads as blackened metal, ash, and sorting order first.

## Triangle Budget

Target LOD0 ranges:

- `SM_GIA_BloodAxeSortedMetalPiles_A01`: 2k-6k tris per reusable pile set.
- `SM_GIA_BloodAxeBentPlateStacks_A01`: 2k-6k tris per stack set.
- `SM_GIA_BloodAxeCrudeScrapBins_A01`: 3k-8k tris depending on visible contents.
- `SM_GIA_BloodAxeBrokenWeaponBundles_A01`: 3k-8k tris per bundle set.
- `SM_GIA_BloodAxeQuenchedSlag_A01`: 1k-4k tris per tray or bank set.
- `KIT_GIA_BloodAxePathSafeClutterRows_A01`: 4k-10k tris per row set, using repeated row pieces.
- `SM_GIA_BloodAxeScrapSortMarkers_A01`: 600-2.5k tris per marker set.
- `SM_GIA_BloodAxeForgeScrapSortingCluster_A01`: 12k-28k tris for an optional composed preview or placement cluster built from reusable children.

Target material slots:

- Small child props: 1 material slot where possible.
- Bins, row sets, and composed clusters: 1-2 material slots.
- Slag-heavy variants: up to 2 material slots if a separate slag/ash material is required.
- Avoid one-off material slots for each shard, tag, chain, soot patch, or broken piece.

Do not increase geometry for fine pitting, micro scratches, tiny chips, dense hammer marks, soot speckles, minor cracks, small rivets, fine chain links, or tiny slag pores.

## LOD Plan

All important child meshes need LOD0-LOD3.

- LOD0: full row layout, large scrap silhouettes, bent plate profiles, bin bodies, visible top pieces, broken weapon bundle outlines, slag tray forms, path-safe row markers, red cloth accents, and broad material zones.
- LOD1: 60-70 percent of LOD0; reduce small bevels, secondary chips, minor chain subdivisions, inner pile pieces, small marker ties, and duplicate loose fragments.
- LOD2: 35-45 percent of LOD0; simplify pile interiors, plate-stack overlaps, bin contents, bundle interiors, slag lump count, row-end detail, and back-side surfaces.
- LOD3: 15-25 percent of LOD0; preserve sorted-row footprint, bin/block silhouettes, bent plate stacks, broken weapon bundle mass, slag zone shape, and major Blood Axe red accent blocks.

Remove tiny rivets, scratches, pitting, small straps, small tags, duplicate chain segments, minor labels, and interior/backside details before reducing the row footprint, bin shapes, large plates, broken weapon silhouettes, or path-safe clutter row read.

## Collision Notes

Collision remains simple, static, and display-focused.

- Sorted metal piles: grouped low-count convex hulls or boxes around the footprint; no per-shard collision.
- Bent plate stacks: one or two simplified hulls around the stack mass; no thin-plate per-poly collision.
- Crude bins: blocking around the outer bin shell only; contents do not need individual collision.
- Broken weapon bundles: one grouped box, capsule, or low-count convex hull around the bundle mass.
- Quenched slag: tray or bank footprint collision only; no per-lump collision.
- Path-safe clutter rows: simple low boxes or convex hulls along the row footprint if placed as blocking dressing; no navmesh, AI, pathfinding, or player-route behavior is defined here.
- Composed sorting cluster: grouped display collision with walkable collision disabled unless a later environment task explicitly approves a different use.

Do not add pickup collision, harvest volumes, crafting interaction volumes, resource triggers, loot outlines, workstation triggers, destructible fracture collision, physics-simulated loose scrap, per-chain collision, per-shard collision, heat hazards, damage volumes, or encounter cover volumes.

## Animation Notes

Static mesh baseline. No animations, physics simulation, material-state timing, heat shimmer, steam VFX, quench effects, sorting loops, crafting loops, player interaction states, NPC workstation states, economy presentation, pickup animations, loot states, salvage loops, resource collection states, destruction states, or startup-scene behaviors are authored here.

Future approval-gated variants may add NPC-only forge activity near the kit, subtle forge-heat material states for separate hot-stock props, or encounter-specific blocking variants through separate gameplay and environment tasks. Baseline `A01` stays inert set dressing.

## Unreal Import Notes

These are planned import notes only. This task does not create Unreal assets or perform an Unreal import.

Planned asset types:

- Static Mesh children for sorted metal piles, bent plate stacks, crude bins, broken weapon bundles, quenched slag, path-safe clutter rows, sorting markers, and optional composed clusters.
- Optional kit-level composed Static Mesh preview for non-interactive forge-yard dressing.
- Docs-only Material Instance dependency: `MI_GIA_BloodAxeReforgedMetal_A01`.

Planned folders:

- `/Game/Aerathea/Props/Giants/BloodAxeCamp/ForgeScrapSorting/`
- `/Game/Aerathea/Props/Giants/BloodAxeArmory/ForgeStock/`
- `/Game/Aerathea/Materials/Giants/BloodAxe/`

Planned naming:

- `SM_GIA_BloodAxeSortedMetalPiles_A01`
- `SM_GIA_BloodAxeBentPlateStacks_A01`
- `SM_GIA_BloodAxeCrudeScrapBins_A01`
- `SM_GIA_BloodAxeBrokenWeaponBundles_A01`
- `SM_GIA_BloodAxeQuenchedSlag_A01`
- `KIT_GIA_BloodAxePathSafeClutterRows_A01`
- `SM_GIA_BloodAxeScrapSortMarkers_A01`
- `SM_GIA_BloodAxeForgeScrapSortingCluster_A01`
- `MI_GIA_BloodAxeReforgedMetal_A01`

Pivot planning:

- Sorted metal piles: ground center of pile footprint.
- Bent plate stacks: ground contact center, aligned to longest plate axis.
- Crude bins: ground center of bin footprint.
- Broken weapon bundles: bundle base/contact center.
- Quenched slag: tray or bank footprint center.
- Path-safe clutter rows: row module base center, with the long axis aligned for grid placement.
- Sorting markers: base center.
- Composed sorting cluster: ground center of the full layout footprint.

Import rules for any future build:

- Author in centimeters and import at scale 1.0.
- Assign LOD0-LOD3 for all important static meshes.
- Target 1-2 material slots per child mesh, 3 only for slag-heavy composed variants.
- Use `MI_GIA_BloodAxeReforgedMetal_A01` for primary metal surfaces.
- Keep collision simple and display-only.
- Do not create Blueprint interaction, crafting recipes, resource nodes, economy data, loot tables, upgrade data, salvage behavior, material graphs, shaders, startup placement, runtime source, or final visual approval artifacts.

## Folder and Naming Recommendation

- Docs folder: `docs/assets/kits/KIT_GIA_BloodAxeForgeScrapSorting_A01/`
- Production package: `docs/assets/kits/KIT_GIA_BloodAxeForgeScrapSorting_A01/PRODUCTION_PACKAGE.md`
- Child intake: `docs/assets/kits/KIT_GIA_BloodAxeForgeScrapSorting_A01/CHILD_ASSET_INTAKE.md`

Future child package recommendations, if promoted by later tasks:

- `docs/assets/props/SM_GIA_BloodAxeSortedMetalPiles_A01/`
- `docs/assets/props/SM_GIA_BloodAxeBentPlateStacks_A01/`
- `docs/assets/props/SM_GIA_BloodAxeCrudeScrapBins_A01/`
- `docs/assets/props/SM_GIA_BloodAxeBrokenWeaponBundles_A01/`
- `docs/assets/props/SM_GIA_BloodAxeQuenchedSlag_A01/`
- `docs/assets/kits/KIT_GIA_BloodAxePathSafeClutterRows_A01/`
- `docs/assets/props/SM_GIA_BloodAxeScrapSortMarkers_A01/`
- `docs/assets/props/SM_GIA_BloodAxeForgeScrapSortingCluster_A01/`

Do not add SourceAssets, FBX exports, Unreal Content assets, runtime source, startup-scene actors, copied source concepts, global index entries, crafting data, economy data, resource behavior, loot definitions, destructible components, material graphs, shaders, or pickup interactions from this task packet.

## Quality Gate Checklist

- Blood Axe remains a hostile Giant sub-faction, separate from neutral/civilized Giant culture.
- Neutral/civilized Giant separation is explicit: no blue-gray stoneworker motifs, warm hearth craft identity, restrained blue runes, cave-town terrace language, or peaceful Giant cultural replacement.
- Giant scale lock is explicit: female baseline 442 cm / 14'6", male baseline 470 cm / 15'5", with approved ranges females 14-15 ft and males 14'10"-16'0".
- Kit reads as inert forge-yard sorting dressing, not loot, resource, crafting, economy, salvage, interaction, destruction, heat hazard, or workstation gameplay.
- Child split covers sorted metal piles, bent plate stacks, crude bins, broken weapon bundles, quenched slag, and path-safe clutter rows.
- Primary material plan is tied to `MI_GIA_BloodAxeReforgedMetal_A01`.
- Primary silhouettes are readable at MMO distance and buildable as mid-poly static meshes.
- Tiny dents, pitting, scratches, soot, slag texture, weld scars, hammer noise, small rivets, and quench stains are assigned to textures/normals instead of geometry.
- Emissive is absent by default and approval-gated for any future forge-heat or shamanic variant.
- Triangle budgets, material slots, texture maps, LOD0-LOD3, collision, pivot planning, Unreal import notes, folders, naming, and child package recommendations are included.
- Package makes no DCC, FBX, Unreal Content, Unreal import, runtime, startup-scene, source concept, global index, first DCC target, crafting, economy/resource, material graph, shader, final visual approval, gameplay pickup, loot, resource-node, interaction, or destruction claim.
