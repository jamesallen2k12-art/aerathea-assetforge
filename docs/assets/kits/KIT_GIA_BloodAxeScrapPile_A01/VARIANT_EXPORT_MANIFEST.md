# KIT_GIA_BloodAxeScrapPile_A01 Variant Export Manifest

## Scope

- Task ID: `AET-MA-20260629-086`
- Scope type: docs-only variant/export manifest for future DCC planning.
- Kit: `KIT_GIA_BloodAxeScrapPile_A01`
- Parent kit: `KIT_GIA_BloodAxeArmory_A01`
- Source concept region: `BloodAxeArmory.png#Display_ScrapPileWeapons`
- Faction/theme: Blood Axe Tribe, hostile Giant sub-faction only.
- Manifest status: planning-ready, no build authorized.

This manifest defines planned mesh names, planned Blender source paths, planned FBX export paths, planned Unreal target paths, pivots, scale notes, material slots, LOD expectations, collision policy, and implementation blockers for the scrap-pile child rows already supported by the production package and child intake.

All source and export paths below are path plans only. This task creates no folders, creates no Blender files, exports no FBX files, imports no Unreal assets, and does not imply that any `SourceAssets` or `/Game` asset currently exists.

## Dependencies

- Production package: `docs/assets/kits/KIT_GIA_BloodAxeScrapPile_A01/PRODUCTION_PACKAGE.md`
- Child intake: `docs/assets/kits/KIT_GIA_BloodAxeScrapPile_A01/CHILD_ASSET_INTAKE.md`
- Shared material package: `docs/assets/materials/MI_GIA_BloodAxeReforgedMetal_A01/PRODUCTION_PACKAGE.md`
- Adjacent forge-process package: `docs/assets/kits/KIT_GIA_BloodAxeReforging_A01/PRODUCTION_PACKAGE.md`
- Armory readiness context: `docs/assets/kits/KIT_GIA_BloodAxeArmory_A01/PACKAGE_CLOSURE_AND_DCC_READINESS.md`
- Primary material dependency: planned `MI_GIA_BloodAxeReforgedMetal_A01`
- Optional support material dependency: future shared scorched wood/leather/cloth material, only when a child mesh cannot keep supports, straps, or cloth warnings in the primary atlas cleanly.

The Blood Axe scrap pile remains hostile raider set dressing. It must not overwrite neutral or civilized Giant culture, which remains tied to mountain stonework, cave halls, hidden highland settlements, terraces, bridges, waterworks, warm hearth presentation, blue-gray stoneworker language, and restrained blue rune or storm accents.

## Giant Scale Lock

- Female Giant baseline: 442 cm / 14'6".
- Male Giant baseline: 470 cm / 15'5".
- Approved Giant ranges: females 14-15 ft / 427-457 cm; males 14'10"-16'0" / 452-488 cm.
- Authoring unit: centimeters.
- Unreal import scale: 1.0, with 1 Unreal unit = 1 cm.
- Future scale validation must compare all child meshes and any composed pile against `SK_GIA_Base_A01` before Unreal placement.
- Normal humanoid carry or interaction compatibility is not required and must not drive scale decisions.

## Source-Storage Guardrail

- Source concept remains external only: `/home/Flamestrike/Desktop/Aerathea/Aerathea Creative/ASSET CONCEPTS/BloodAxeArmory.png`
- Do not copy, move, edit, crop, embed, package, or commit the source concept from this task.
- Planned Blender source paths in this manifest are future source-storage targets only; they are not created by this task.
- Planned FBX export paths in this manifest are future export targets only; they are not created by this task.

## Docs-Only and No-Build Guardrails

- No first DCC target is selected by this manifest.
- No DCC source creation, Blender source file, source folder creation, proof render, or DCC validation output is authorized.
- No FBX export, export folder creation, or generated LOD file is authorized.
- No Unreal Content import, Static Mesh asset, Material Instance, texture asset, Blueprint, validator, runtime source, or startup-scene placement is authorized.
- No final visual approval is claimed.
- No global indexes, task boards, runtime source, `Content/Aerathea/`, `SourceAssets/`, `Tools/DCC/`, `Tools/Unreal/`, or external source concept folders are changed by this manifest.
- No loot, resource, destructible, crafting, economy, salvage, vendor, inventory, reward, encounter-cover, damage, pickup, harvest, or player interaction behavior is authorized.
- No pickup volumes, harvest volumes, crafting interaction volumes, loot outlines, destructible fracture collision, physics-simulated loose scrap, per-chain collision, per-shard collision, gameplay markers, resource-node crystals, or economy tags are allowed in the baseline `A01` plan.

## Variant Export Table

| Child row | Planned mesh name | Planned Blender source path | Planned export path | Planned Unreal path | Pivot | Scale notes | Material slots | LOD expectations | Collision policy | Implementation blockers |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Metal chunks | `SM_GIA_BloodAxeMetalChunks_A01` | `SourceAssets/Blender/Giants/BloodAxeArmory/ScrapPile/SM_GIA_BloodAxeMetalChunks_A01.blend` | `SourceAssets/Exports/Giants/BloodAxeArmory/ScrapPile/SM_GIA_BloodAxeMetalChunks_A01/SM_GIA_BloodAxeMetalChunks_A01_LOD#.fbx` | `/Game/Aerathea/Props/Giants/BloodAxeArmory/ScrapPile/SM_GIA_BloodAxeMetalChunks_A01` | Base/contact center for scatter placement. | 45-140 cm large offcuts, shield fragments, plate chunks, and blunt scrap masses sized for Giant handling. | 1 slot: `MI_GIA_BloodAxeReforgedMetal_A01`. | LOD0 500-2.5k tris per reusable chunk set; LOD1 60-70 percent; LOD2 35-45 percent; LOD3 15-25 percent. | Simple box or low-count convex hull only when standalone; no per-chip collision. | Blocked until lead approves DCC work, source paths, material authoring, export, Unreal import, and visual review; no first DCC target selected. |
| Broken blades | `SM_GIA_BloodAxeBrokenBlades_A01` | `SourceAssets/Blender/Giants/BloodAxeArmory/ScrapPile/SM_GIA_BloodAxeBrokenBlades_A01.blend` | `SourceAssets/Exports/Giants/BloodAxeArmory/ScrapPile/SM_GIA_BloodAxeBrokenBlades_A01/SM_GIA_BloodAxeBrokenBlades_A01_LOD#.fbx` | `/Game/Aerathea/Props/Giants/BloodAxeArmory/ScrapPile/SM_GIA_BloodAxeBrokenBlades_A01` | Base/contact center near the fragment's stable resting point. | 90-260 cm snapped axe arcs, cleaver slabs, spear tips, and bent blade fragments; must read as feedstock, not usable pickups. | 1 slot: `MI_GIA_BloodAxeReforgedMetal_A01`. | LOD0 800-3k tris per blade-fragment set; LOD1 60-70 percent; LOD2 35-45 percent; LOD3 15-25 percent. | Simple box or capsule around fragment; no sharp-edge per-poly collision. | Blocked until DCC target approval, blade-shape visual approval, export approval, Unreal approval, and explicit non-pickup review. |
| Failed casts | `SM_GIA_BloodAxeFailedCasts_A01` | `SourceAssets/Blender/Giants/BloodAxeArmory/ScrapPile/SM_GIA_BloodAxeFailedCasts_A01.blend` | `SourceAssets/Exports/Giants/BloodAxeArmory/ScrapPile/SM_GIA_BloodAxeFailedCasts_A01/SM_GIA_BloodAxeFailedCasts_A01_LOD#.fbx` | `/Game/Aerathea/Props/Giants/BloodAxeArmory/ScrapPile/SM_GIA_BloodAxeFailedCasts_A01` | Ground or support contact center for each failed-cast group. | 80-220 cm warped axe-head blanks, hammer blocks, socket collars, and unusable plate casts; crude Blood Axe reforging only. | 1 slot: `MI_GIA_BloodAxeReforgedMetal_A01`. | LOD0 1k-4k tris per group; LOD1 60-70 percent; LOD2 35-45 percent; LOD3 15-25 percent. | One simplified convex hull per group; no per-cutout collision. | Blocked until future DCC approval confirms failed-cast silhouettes without master-smith polish or neutral Giant craft language. |
| Chained bundles | `SM_GIA_BloodAxeChainedScrapBundle_A01` | `SourceAssets/Blender/Giants/BloodAxeArmory/ScrapPile/SM_GIA_BloodAxeChainedScrapBundle_A01.blend` | `SourceAssets/Exports/Giants/BloodAxeArmory/ScrapPile/SM_GIA_BloodAxeChainedScrapBundle_A01/SM_GIA_BloodAxeChainedScrapBundle_A01_LOD#.fbx` | `/Game/Aerathea/Props/Giants/BloodAxeArmory/ScrapPile/SM_GIA_BloodAxeChainedScrapBundle_A01` | Bundle center with bottom aligned to ground. | 160-320 cm long, 80-170 cm wide, 50-120 cm high bound stacks; chain loops and red cloth warnings must remain sparse. | 1-2 slots: primary `MI_GIA_BloodAxeReforgedMetal_A01`; optional scorched leather/cloth support slot. | LOD0 2k-6k tris; LOD1 reduces chain subdivisions and minor straps; LOD2 simplifies bundle interiors; LOD3 preserves bundle mass and red accent blocks. | One box or low-count convex hull around bundle mass; no per-chain collision and no physics-simulated loose scrap. | Blocked until chain density, cloth use, DCC, export, Unreal import, and no-pickup/no-transport behavior are separately approved. |
| Forge bins | `SM_GIA_BloodAxeForgeBin_A01` | `SourceAssets/Blender/Giants/BloodAxeArmory/ScrapPile/SM_GIA_BloodAxeForgeBin_A01.blend` | `SourceAssets/Exports/Giants/BloodAxeArmory/ScrapPile/SM_GIA_BloodAxeForgeBin_A01/SM_GIA_BloodAxeForgeBin_A01_LOD#.fbx` | `/Game/Aerathea/Props/Giants/BloodAxeArmory/ScrapPile/SM_GIA_BloodAxeForgeBin_A01` | Ground center of bin footprint. | 180-320 cm wide, 120-240 cm deep, 90-170 cm high sorted-scrap bins; must not read as treasure chests, vendor crates, or resource containers. | 1-2 slots: primary `MI_GIA_BloodAxeReforgedMetal_A01`; optional scorched wood/leather support slot. | LOD0 3k-7k tris; LOD1 reduces contents and bevels; LOD2 simplifies bin contents and rim details; LOD3 keeps squat bin silhouette. | Blocking around outer bin shell only; no per-scrap collision, chest trigger, or interaction volume. | Blocked until future approval confirms bin silhouette, support material, source path creation, export, Unreal import, and no container behavior. |
| Rack scatter | `SM_GIA_BloodAxeRackScatter_A01` | `SourceAssets/Blender/Giants/BloodAxeArmory/ScrapPile/SM_GIA_BloodAxeRackScatter_A01.blend` | `SourceAssets/Exports/Giants/BloodAxeArmory/ScrapPile/SM_GIA_BloodAxeRackScatter_A01/SM_GIA_BloodAxeRackScatter_A01_LOD#.fbx` | `/Game/Aerathea/Props/Giants/BloodAxeArmory/ScrapPile/SM_GIA_BloodAxeRackScatter_A01` | Ground center of support/rack footprint. | 220-460 cm wide compositions with a few vertical fragments reaching 220-340 cm; useful for walls and armory corners. | 1-2 slots: primary `MI_GIA_BloodAxeReforgedMetal_A01`; optional rack support material. | LOD0 3k-8k tris; LOD1 reduces minor rack fragments; LOD2 simplifies leaning-piece interiors; LOD3 preserves fan direction and rack footprint. | Grouped boxes around leaning pieces and base footprint; no dense shard collision. | Blocked until DCC approval keeps scatter sparse, readable, non-interactive, and separate from neutral Giant workshop language. |
| Slag trays | `SM_GIA_BloodAxeSlagTray_A01` | `SourceAssets/Blender/Giants/BloodAxeArmory/ForgeStock/SM_GIA_BloodAxeSlagTray_A01.blend` | `SourceAssets/Exports/Giants/BloodAxeArmory/ForgeStock/SM_GIA_BloodAxeSlagTray_A01/SM_GIA_BloodAxeSlagTray_A01_LOD#.fbx` | `/Game/Aerathea/Props/Giants/BloodAxeArmory/ForgeStock/SM_GIA_BloodAxeSlagTray_A01` | Tray footprint center on ground. | 160-320 cm wide, 80-180 cm deep, 35-80 cm high shallow troughs with cooled matte slag, ash, soot crust, and heavy rim forms. | 1 slot baseline: `MI_GIA_BloodAxeReforgedMetal_A01` with matte slag/ash treatment. | LOD0 1.5k-5k tris; LOD1 reduces slag lump detail; LOD2 simplifies tray contents; LOD3 preserves tray footprint and rim mass. | Tray footprint collision only; no per-lump collision, burn hazard, water interaction, or hot-slag trigger. | Blocked until cooled non-emissive visual state is approved; any forge-heat or emissive variant requires separate material/VFX approval. |
| Reforging stock | `SM_GIA_BloodAxeReforgingStock_A01` | `SourceAssets/Blender/Giants/BloodAxeArmory/ForgeStock/SM_GIA_BloodAxeReforgingStock_A01.blend` | `SourceAssets/Exports/Giants/BloodAxeArmory/ForgeStock/SM_GIA_BloodAxeReforgingStock_A01/SM_GIA_BloodAxeReforgingStock_A01_LOD#.fbx` | `/Game/Aerathea/Props/Giants/BloodAxeArmory/ForgeStock/SM_GIA_BloodAxeReforgingStock_A01` | Stack center or base contact center. | 90-260 cm bars, billets, rough ingots, cut plates, and prepared stock stacks sized for Giant hands and tongs. | 1 slot: `MI_GIA_BloodAxeReforgedMetal_A01`. | LOD0 1k-4k tris per stock stack; LOD1 reduces bevels and duplicate bars; LOD2 simplifies stack interiors; LOD3 preserves bar-stack silhouette. | Grouped box or low-count convex hull for stack; no resource-node, inventory, crafting, economy, pickup, or harvest collision. | Blocked until DCC/export/Unreal approval and explicit gameplay approval if anyone later proposes resource, crafting, salvage, or economy behavior. |
| Composed scrap pile | `SM_GIA_BloodAxeScrapPile_A01` | `SourceAssets/Blender/Giants/BloodAxeArmory/ScrapPile/SM_GIA_BloodAxeScrapPile_A01.blend` | `SourceAssets/Exports/Giants/BloodAxeArmory/ScrapPile/SM_GIA_BloodAxeScrapPile_A01/SM_GIA_BloodAxeScrapPile_A01_LOD#.fbx` | `/Game/Aerathea/Props/Giants/BloodAxeArmory/ScrapPile/SM_GIA_BloodAxeScrapPile_A01` | Ground center of full composed footprint. | 350-650 cm wide, 250-500 cm deep, 80-190 cm high non-interactive heap assembled from supported child sets. | 1-2 slots: primary `MI_GIA_BloodAxeReforgedMetal_A01`; optional support material for cloth, straps, racks, or bin support pieces. | LOD0 8k-18k tris; LOD1 60-70 percent; LOD2 35-45 percent; LOD3 15-25 percent while preserving heap footprint, broken blade reads, bin/tray masses, stock bars, and red accents. | Grouped low-count convex hulls or boxes around main footprint; walkable collision disabled by default; no cover behavior unless a later encounter package approves it. | Optional composed placement mesh is supported by intake, but blocked until child meshes, composition approval, DCC/export/Unreal approval, scale validation, and final visual approval are complete. |

## Implementation Blockers

- Lead approval is required before any row becomes a selected first DCC target.
- DCC approval is required before creating Blender source files, source folders, LOD source meshes, collision proxies, or proof renders.
- Export approval is required before creating FBX files under any planned export path.
- Unreal approval is required before importing Static Meshes, creating `/Game` assets, assigning materials, setting collision, adding validators, or placing startup actors.
- Material/texture approval is required before authoring `MI_GIA_BloodAxeReforgedMetal_A01`, support materials, texture assets, material graphs, shader functions, forge-heat states, or emissive maps.
- Visual approval is required before any final silhouette, composition, red-paint density, chain density, support-material usage, or composed-pile layout is locked.
- Gameplay approval is required before any loot, resource, destructible, crafting, economy, salvage, vendor, inventory, pickup, harvest, interaction, cover, hazard, physics, damage, or reward behavior is added.
- Source-storage approval is required before any external concept file enters the repository.
- Culture approval is required if Blood Axe red-black raider language starts bleeding into neutral or civilized Giant packages.

## Quality Gate Checklist

- Child rows cover metal chunks, broken blades, failed casts, chained bundles, forge bins, rack scatter, slag trays, reforging stock, and the intake-supported composed scrap pile.
- Giant scale lock is explicit and unchanged.
- Planned Blender source paths and FBX export paths are documented as uncreated plans only.
- Planned Unreal paths are documented as future targets only.
- `MI_GIA_BloodAxeReforgedMetal_A01` remains the primary material dependency.
- Blood Axe remains a hostile Giant sub-faction only.
- Neutral/civilized Giant culture is not overwritten or redefined.
- No DCC, FBX, Unreal Content, runtime source, startup-scene, material graph, texture authoring, source concept copying, final visual approval, or first DCC target selection is claimed.
- Loot, resource, destructible, crafting, economy, pickup, harvest, salvage, vendor, inventory, reward, interaction, and cover behavior are explicitly blocked.
