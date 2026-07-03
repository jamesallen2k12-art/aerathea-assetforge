# KIT_GIA_BloodAxeScrapPile_A01 Production Package

## Art Direction Summary

- Asset name: `KIT_GIA_BloodAxeScrapPile_A01`
- Asset type: Production kit / Giant-scale armory dressing and reforging feedstock set
- Parent source: `KIT_GIA_BloodAxeArmory_A01`
- Source concept region: `BloodAxeArmory.png#Display_ScrapPileWeapons`
- Primary material dependency: `MI_GIA_BloodAxeReforgedMetal_A01`
- Faction/theme: Blood Axe Tribe, hostile Giant sub-faction
- Status: docs-only kit production package ready
- Scope guardrail: this package creates no DCC source, FBX export, Unreal Content asset, runtime source, startup-scene placement, gameplay pickup, economy object, crafting system, destructible prop, or lootable resource node.

`KIT_GIA_BloodAxeScrapPile_A01` defines hostile Blood Axe Giant scrap piles used as readable armory dressing and reforging feedstock. The kit should look like brutal field-forge residue: huge blackened metal chunks, broken blades, failed casts, chained bundles, forge bins, rack scatter, slag trays, and stacked reforging stock. It tells players that the Blood Axe Tribe strips stolen metal into war gear, but it must not imply a player-harvestable resource, interactable crafting station, loot pile, destructible cover object, or economy item.

Blood Axe language must remain separate from neutral and civilized Giant culture. This kit belongs to hostile raider camps, forge corners, weapon yards, and armory dressing, not to normal Giant cave towns, stoneworker halls, or highland nomad camps.

## Gameplay Purpose

The kit supports environmental storytelling and composition for Blood Axe locations:

- Armory dressing around weapon racks, banner stands, quivers, bowyer corners, and forge staging.
- Reforging feedstock piles that explain how stolen weapons, armor plates, shield fragments, and failed casts become Blood Axe war gear.
- Scale reference props beside Giant weapons and armor so camp spaces feel built for female 442 cm / 14'6" and male 470 cm / 15'5" Giants.
- Non-interactive set dressing for camps, barracks, forge yards, raid staging areas, and boss arenas.
- Reusable child meshes for DCC and Unreal layout without rebuilding a unique pile for every scene.

Explicit exclusions:

- Not a lootable resource node.
- Not a gameplay pickup.
- Not a destructible prop.
- Not a crafting station or crafting-system component.
- Not an economy object, vendor object, inventory object, salvage system, or reward container.
- Not walkable cover unless a later encounter-specific environment package approves that behavior.

## Silhouette Notes

Primary read: a Giant-scale heap of brutal reforging feedstock, low and heavy at the base with several strong metal silhouettes rising out of it. The player should recognize broken weapon blades, slab scrap plates, chained bundles, forge bins, rack scatter, slag trays, and reforging bars from normal MMO camera distance.

Child silhouette direction:

- Metal chunks: blunt triangular, rectangular, and shield-fragment masses with broad chipped edges and clear weight.
- Broken blades: snapped axe arcs, cleaver slabs, spear tips, knife-like fragments, and bent sword-scale pieces that read as Giant scrap.
- Failed casts: half-formed axe heads, warped hammer blocks, collapsed sockets, and malformed plate blanks.
- Chained bundles: bound scrap stacks with a few thick chain loops and one or two red cloth warning strips.
- Forge bins: squat Giant-scale metal or timber bins filled with sorted scrap, not treasure chests.
- Rack scatter: loose pieces leaning against simple broken rack elements, with a readable fan or pile direction.
- Slag trays: shallow troughs with cooled slag lumps, ash, soot, and matte black crusts.
- Reforging stock: stacked ingots, bars, rough billet plates, and cut stock ready for future Blood Axe weapons.

Model the largest pieces, bin rims, tray silhouettes, large chains, thick bars, failed-cast profiles, and broken blade outlines as geometry. Paint or normal-map small dents, pits, soot streaks, edge scratches, minor hammer marks, small rivets, fine cracks, and tiny weld scars.

Avoid dense trophy clutter, graphic gore, small unreadable weapon fragments, miniature coin-like scrap, or a treasure-pile silhouette. Red cloth and paint should identify the hostile Blood Axe sub-faction without turning the entire pile red.

## Scale Notes

Giant scale lock exactly:

- Female Giant baseline: 442 cm / 14'6".
- Male Giant baseline: 470 cm / 15'5".
- Approved Giant ranges: females 14-15 ft / 427-457 cm; males 14'10"-16'0" / 452-488 cm.
- Author in centimeters. 1 Unreal unit = 1 cm.
- Normal humanoid compatibility is not required.

Suggested production scale targets:

- Composed scrap pile footprint: 350-650 cm wide, 250-500 cm deep, 80-190 cm high.
- Metal chunks: 45-140 cm across, thick enough to read as Giant weapon/armor scrap.
- Broken blades: 90-260 cm long depending on source weapon fragment.
- Failed casts: 80-220 cm across for axe heads, hammer blocks, plate blanks, and socket masses.
- Chained bundles: 160-320 cm long, 80-170 cm wide, 50-120 cm high.
- Forge bins: 180-320 cm wide, 120-240 cm deep, 90-170 cm high.
- Rack scatter: 220-460 cm wide compositions, with a few vertical pieces reaching 220-340 cm.
- Slag trays: 160-320 cm wide, 80-180 cm deep, 35-80 cm high.
- Reforging stock: 90-260 cm bars or billets, grouped in stacks sized for Giant hands and tongs.

Scale validation for any future build should compare the composed pile and child pieces against `SK_GIA_Base_A01` male and female baselines before Unreal placement. The kit should feel too large for normal humanoids to carry casually.

## Materials and Color Palette

Primary material dependency:

- `MI_GIA_BloodAxeReforgedMetal_A01` for blackened iron, dark steel, hammered scrap plates, soot, grime, chipped oxide-red paint, and broad worn edges.

Supporting material language:

- Blackened iron and dark steel with broad hammer marks and chipped edge wear.
- Dull reforged plates, snapped blades, and warped cast shapes.
- Matte cooled slag, charcoal dust, ash, and soot crust.
- Scorched wood or dark timber only for bins and rack fragments.
- Scorched leather, hide cord, and thick chain bindings used sparingly.
- Torn deep red cloth and chipped red paint as Blood Axe identifiers.
- Bone or trophy fragments only as rare background accents, never as the main read.

Avoid neutral/civilized Giant blue-gray stoneworker motifs, warm hearth presentation, restrained blue rune language, peaceful highland craft symbols, or polished masonry identity. Those belong to neutral Giant packages unless a stolen/defaced variant is separately approved.

No default emissive is approved. A future forge-heat or shamanic variant would require a separate visual approval and material-state package.

## Concept Image Prompt

Create an original stylized fantasy MMORPG concept image of `KIT_GIA_BloodAxeScrapPile_A01` for the world of Aerathea. The design should emphasize a hostile Blood Axe Giant scrap pile used as readable armory dressing and reforging feedstock, with huge blackened metal chunks, broken blades, failed casts, chained bundles, forge bins, rack scatter, slag trays, stacked reforging stock, dark steel, soot, ash, chipped red paint, torn red cloth warnings, and `MI_GIA_BloodAxeReforgedMetal_A01` material language. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, no default emissive glow, and MMO-friendly production design. Present it as a clean production asset board with child split callouts, scale callouts against a female 442 cm / 14'6" Giant and a male 470 cm / 15'5" Giant, LOD/collision notes, and a clear label that it is non-interactive set dressing rather than loot, crafting, economy, destruction, or pickup gameplay. Avoid copying any existing franchise, avoid graphic gore, avoid making Blood Axe visual language the default Giant culture, avoid treasure-pile readability, and avoid excessive micro-detail that would not translate to mid-poly Unreal assets.

## Modeling Notes

This is a docs-only package. Future modeling should build the kit as reusable child meshes and composed variants rather than one collapsed scrap mass.

- Metal chunks: build several large readable chunks, shield/plate fragments, and blunt offcuts with simple bevels and chipped profiles.
- Broken blades: create snapped axe arcs, cracked cleaver slabs, spear tips, and bent long fragments that read as broken Blood Axe or stolen weapon stock.
- Failed casts: model warped axe head blanks, collapsed hammer blocks, malformed socket collars, and unusable plate casts.
- Chained bundles: stack a limited number of large chunks and bars, then bind them with thick chain loops, heavy rings, or scorched hide straps.
- Forge bins: model squat bins with thick rims, dented panels, a few large contents near the top, and no chest/loot silhouette.
- Rack scatter: create leaning fragments and broken rack supports for camp corners and armory walls; keep individual pieces sparse and readable.
- Slag trays: model shallow troughs and large cooled slag lumps; use normal and roughness for crust texture.
- Reforging stock: model bars, billets, ingot-like slabs, cut plates, and rough stock stacks sized for Giant handling.

Use real geometry for primary masses, large broken silhouettes, bin/tray rims, chain loops, major plates, broad stock bars, and obvious failed-cast forms. Use texture and normal detail for pitting, soot, hammer noise, fine edge cracks, tiny rivets, small scratches, minor slag bubbles, and dense weld texture.

Composition variants should support:

- Low heap at forge edge.
- Sorted bin cluster.
- Armory rack scatter.
- Chained transport bundle.
- Reforging stock stack.

Do not add gameplay affordance meshes such as glowing interaction markers, pickup handles, loot sparkles, harvest outlines, health-state fracture cuts, resource-node crystals, or economy tags.

## Texture and Material Notes

Required map set for future texture work:

- Base Color / Albedo (`BC`)
- Normal (`N`)
- Packed Occlusion/Roughness/Metallic (`ORM`)

No emissive map is planned for the baseline kit.

Material plan:

- Slot 0: `MI_GIA_BloodAxeReforgedMetal_A01` for most metal chunks, broken blades, failed casts, bins, trays, and stock.
- Optional slot 1: shared scorched wood/leather/cloth material for rack fragments, straps, red cloth, and bin supports when the atlas cannot include them cleanly.
- Optional slag overlay or material function may be planned later, but it should remain matte and non-interactive.

Texture naming examples:

- `T_GIA_BloodAxeScrapPile_A01_BC`
- `T_GIA_BloodAxeScrapPile_A01_N`
- `T_GIA_BloodAxeScrapPile_A01_ORM`
- `T_GIA_BloodAxeMetalChunks_A01_BC`
- `T_GIA_BloodAxeBrokenBlades_A01_BC`
- `T_GIA_BloodAxeForgeBins_A01_BC`
- `T_GIA_BloodAxeSlagTrays_A01_BC`

Use 1K texture sets for small repeated children, 2K for composed pile or bin/rack variants, and 4K only if a later hero forge scene specifically approves close-up use. Keep red paint masks and cloth accents restrained so the pile reads as blackened metal first.

## Triangle Budget

Target LOD0 ranges:

- `SM_GIA_BloodAxeMetalChunks_A01`: 500-2.5k tris per reusable chunk set.
- `SM_GIA_BloodAxeBrokenBlades_A01`: 800-3k tris per blade-fragment set.
- `SM_GIA_BloodAxeFailedCasts_A01`: 1k-4k tris per failed-cast group.
- `SM_GIA_BloodAxeChainedScrapBundle_A01`: 2k-6k tris.
- `SM_GIA_BloodAxeForgeBin_A01`: 3k-7k tris depending on visible contents.
- `SM_GIA_BloodAxeRackScatter_A01`: 3k-8k tris.
- `SM_GIA_BloodAxeSlagTray_A01`: 1.5k-5k tris.
- `SM_GIA_BloodAxeReforgingStock_A01`: 1k-4k tris per stock stack.
- `SM_GIA_BloodAxeScrapPile_A01` composed preview or placement mesh: 8k-18k tris.

The composed kit should reuse child meshes and material atlases. Do not increase geometry just to express tiny pitting, scratches, fine slag pores, or many small scrap shards.

## LOD Plan

All important child meshes need LOD0-LOD3.

- LOD0: full primary scrap silhouettes, broken blade profiles, failed-cast forms, bin/tray rims, chain loops, stock bars, red cloth accents, and broad material zones.
- LOD1: 60-70 percent of LOD0; reduce small bevels, secondary chips, interior pile pieces, chain subdivisions, and minor rack fragments.
- LOD2: 35-45 percent of LOD0; simplify pile interiors, failed-cast cutouts, bin contents, tray contents, chain loops, and blade-edge chips.
- LOD3: 15-25 percent of LOD0; preserve overall heap footprint, broken blade reads, bin/tray mass, chained bundle shape, and Blood Axe red accent blocks.

Remove tiny scratches, pitting, small shards, minor straps, duplicate chain segments, and interior/backside details before reducing the pile footprint, large broken blades, bin shapes, or stock-bar silhouettes.

## Collision Notes

Collision remains simple and display-focused.

- Composed scrap pile: grouped low-count convex hulls or boxes around the main footprint; walkable collision disabled unless a future environment-cover task approves it.
- Metal chunks: simple box or convex hull only when placed as standalone world dressing.
- Broken blades: simple box/capsule around the fragment; no sharp-edge per-poly collision.
- Failed casts: one simplified convex hull per group.
- Chained bundles: one box or convex hull around the bundle mass; no per-chain collision.
- Forge bins: blocking around outer bin shell only; no per-scrap collision.
- Rack scatter: grouped boxes around leaning pieces and base footprint.
- Slag trays: tray footprint collision only; no per-lump collision.
- Reforging stock: grouped box or low-count convex hull for the stack.

Do not add pickup collision, harvest volumes, destructible fracture collision, physics-simulated loose scrap, per-shard collision, crafting interaction volumes, or loot-outline trigger volumes in this package.

## Animation Notes

Static mesh baseline. No animations, physics simulation, destruction states, gameplay interaction states, pickup animations, salvage loops, crafting loops, economy presentation, or material-state timing are authored here.

Future approval-gated variants may add:

- Subtle forge-heat material state for a separate hot-stock package.
- Scripted camp activity where Giant NPCs move nearby but do not require the pile itself to animate.
- Encounter-specific breakable cover or hazard state, only through a separate gameplay and environment task.

Baseline `A01` stays inert set dressing.

## Unreal Import Notes

These are planned import notes only. This task does not create Unreal assets.

Planned asset types:

- Static Mesh children for metal chunks, broken blades, failed casts, chained bundles, forge bins, rack scatter, slag trays, and reforging stock.
- Optional composed Static Mesh layout variant for a ready-to-place non-interactive scrap-pile cluster.
- Material Instance dependency: `MI_GIA_BloodAxeReforgedMetal_A01`.

Planned folders:

- `/Game/Aerathea/Props/Giants/BloodAxeArmory/ScrapPile/`
- `/Game/Aerathea/Props/Giants/BloodAxeArmory/ForgeStock/`
- `/Game/Aerathea/Materials/Giants/BloodAxe/`

Planned naming:

- `SM_GIA_BloodAxeScrapPile_A01`
- `SM_GIA_BloodAxeMetalChunks_A01`
- `SM_GIA_BloodAxeBrokenBlades_A01`
- `SM_GIA_BloodAxeFailedCasts_A01`
- `SM_GIA_BloodAxeChainedScrapBundle_A01`
- `SM_GIA_BloodAxeForgeBin_A01`
- `SM_GIA_BloodAxeRackScatter_A01`
- `SM_GIA_BloodAxeSlagTray_A01`
- `SM_GIA_BloodAxeReforgingStock_A01`
- `MI_GIA_BloodAxeReforgedMetal_A01`

Pivot planning:

- Composed pile: pivot at ground center of the footprint.
- Metal chunks and broken blades: pivot near base/contact center for easy scattering.
- Failed casts: pivot at ground or support contact center.
- Chained bundles: pivot at bundle center with bottom aligned to ground.
- Forge bins: pivot at ground center of bin footprint.
- Rack scatter: pivot at ground center of the support/rack footprint.
- Slag trays: pivot at tray footprint center.
- Reforging stock: pivot at stack center or base contact center.

Import rules:

- Author in centimeters and import at scale 1.0.
- Assign LOD0-LOD3 for all important static meshes.
- Target 1-2 material slots per child mesh.
- Use `MI_GIA_BloodAxeReforgedMetal_A01` for primary metal surfaces.
- Keep collision simple and display-only.
- Do not create Blueprint interaction, pickup behavior, destruction components, loot tables, crafting recipes, economy data, or resource-node markers.

## Folder and Naming Recommendation

- Docs folder: `docs/assets/kits/KIT_GIA_BloodAxeScrapPile_A01/`
- Production package: `docs/assets/kits/KIT_GIA_BloodAxeScrapPile_A01/PRODUCTION_PACKAGE.md`
- Child intake: `docs/assets/kits/KIT_GIA_BloodAxeScrapPile_A01/CHILD_ASSET_INTAKE.md`

Future package names, if promoted by later tasks:

- `SM_GIA_BloodAxeScrapPile_A01`
- `SM_GIA_BloodAxeMetalChunks_A01`
- `SM_GIA_BloodAxeBrokenBlades_A01`
- `SM_GIA_BloodAxeFailedCasts_A01`
- `SM_GIA_BloodAxeChainedScrapBundle_A01`
- `SM_GIA_BloodAxeForgeBin_A01`
- `SM_GIA_BloodAxeRackScatter_A01`
- `SM_GIA_BloodAxeSlagTray_A01`
- `SM_GIA_BloodAxeReforgingStock_A01`

Do not add SourceAssets, FBX exports, Unreal Content assets, runtime source, startup-scene actors, copied source concepts, global index entries, crafting data, economy data, loot definitions, destructible components, or pickup interactions from this task packet.

## Quality Gate Checklist

- Blood Axe remains a hostile Giant sub-faction, separate from neutral/civilized Giant culture.
- Giant scale lock is explicit: female baseline 442 cm / 14'6", male baseline 470 cm / 15'5", with approved ranges females 14-15 ft and males 14'10"-16'0".
- Kit reads as armory dressing and reforging feedstock, not treasure, loot, crafting, economy, destruction, or pickup gameplay.
- Child split covers metal chunks, broken blades, failed casts, chained bundles, forge bins, rack scatter, slag trays, and reforging stock.
- Primary material plan is tied to `MI_GIA_BloodAxeReforgedMetal_A01`.
- Primary silhouettes are readable at MMO distance and buildable as mid-poly static meshes.
- Tiny dents, pitting, scratches, soot, slag texture, weld scars, and minor hammer noise are assigned to textures/normals instead of geometry.
- Emissive is absent by default and approval-gated for any future forge-heat or shamanic variant.
- Triangle budgets, texture maps, LOD0-LOD3, collision, Unreal import notes, pivots, folders, and naming are included.
- Package makes no DCC, FBX, Unreal Content, runtime, startup-scene, source concept, global index, gameplay pickup, crafting, economy, resource-node, loot, or destruction claim.
