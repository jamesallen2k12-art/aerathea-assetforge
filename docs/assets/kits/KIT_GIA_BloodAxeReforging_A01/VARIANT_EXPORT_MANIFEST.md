# KIT_GIA_BloodAxeReforging_A01 Variant Export Manifest

## Scope

- Task: `AET-MA-20260629-087`
- Scope type: docs-only variant/export manifest for future DCC planning
- Parent kit: `KIT_GIA_BloodAxeReforging_A01`
- Parent armory: `KIT_GIA_BloodAxeArmory_A01`
- Related feedstock kit: `KIT_GIA_BloodAxeScrapPile_A01`
- Source concept region: `BloodAxeArmory.png#Forge_RaidedReforged_Process`
- Faction/theme: Blood Axe Tribe, hostile Giant sub-faction
- Status: export planning only; no DCC target selected

This manifest splits the Blood Axe reforging process into future mesh/export candidates so the kit does not enter DCC as one collapsed process prop. It is a planning document only. It defines planned names, planned source/export paths, pivots, scale notes, material slots, LOD expectations, collision policy, and blockers for later approval.

Blood Axe remains a hostile Giant sub-faction only. This document must not overwrite neutral or civilized Giant culture, which remains tied to mountain stonework, cave halls, hidden highland settlements, terraces, bridges, waterworks, warm hearth presentation, restrained blue-gray craft language, and non-raider Giant identity.

## Dependencies

- Production package: `docs/assets/kits/KIT_GIA_BloodAxeReforging_A01/PRODUCTION_PACKAGE.md`
- Child intake: `docs/assets/kits/KIT_GIA_BloodAxeReforging_A01/CHILD_ASSET_INTAKE.md`
- Feedstock reference: `docs/assets/kits/KIT_GIA_BloodAxeScrapPile_A01/PRODUCTION_PACKAGE.md`
- Material dependency: `docs/assets/materials/MI_GIA_BloodAxeReforgedMetal_A01/PRODUCTION_PACKAGE.md`
- Armory readiness: `docs/assets/kits/KIT_GIA_BloodAxeArmory_A01/PACKAGE_CLOSURE_AND_DCC_READINESS.md`
- Primary planned material dependency: `MI_GIA_BloodAxeReforgedMetal_A01`
- Optional future support material: shared scorched wood/leather/cloth support material, approval-gated and not authored here
- Optional future heat-state material or emissive mask: approval-gated and not authored here

## Giant Scale Lock

- Approved Giant ranges: females 14-15 ft / 427-457 cm; males 14'10"-16'0" / 452-488 cm.
- Validated `SK_GIA_Base_A01` planning baselines: female Giant 442 cm / 14'6"; male Giant 470 cm / 15'5".
- Author future DCC in centimeters. 1 Unreal unit = 1 cm.
- Import scale target for any later Unreal work: 1.0.
- Normal humanoid compatibility is not required.
- All future mesh dimensions must read as Giant-operated forge-process props, not player-scale crafting stations.

## Source-Storage Guardrail

The source concept remains external only at `/home/Flamestrike/Desktop/Aerathea/Aerathea Creative/ASSET CONCEPTS/BloodAxeArmory.png`. Do not copy, move, edit, embed, crop, commit, or recreate the source concept inside this repository for this docs-only manifest.

All `SourceAssets/Blender/...` and `SourceAssets/Exports/...` entries below are planned path strings only. This task does not create directories, Blender files, FBX files, proof renders, Unreal assets, validators, or startup-scene actors.

## Docs-Only and No-Build Guardrails

- No DCC work, Blender source creation, source-folder creation, mesh authoring, proof rendering, or first DCC target selection.
- No FBX export, export-folder creation, Unreal import, Unreal Content asset creation, Blueprint creation, validator creation, startup placement, runtime source change, or final visual approval.
- No material graph authoring, shader authoring, texture authoring, material instance creation, emissive map creation, heat-state effects, heat shimmer, steam VFX, quench VFX, animated material timing, or forge glow implementation.
- No crafting system, crafting recipe, salvage loop, upgrade bench, economy/resource behavior, vendor data, inventory data, loot table, reward object, harvest node, player interaction, pickup behavior, destructible behavior, hazard volume, burn damage, water interaction, or encounter behavior.
- No neutral/civilized Giant culture changes. Blood Axe red-black raider language, stolen-metal reforging, crude warning markers, and hostile camp identity stay isolated to the Blood Axe sub-faction.

## Variant Export Table

| Variant / row | Planned mesh name | Planned Blender source path | Planned export path | Planned Unreal path | Pivot | Scale notes | Material slots | LOD expectations | Collision policy | Implementation blockers |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Stolen scrap intake | `SM_GIA_BloodAxeStolenScrapIntake_A01` | `SourceAssets/Blender/Props/Giants/BloodAxeArmory/Reforging/SM_GIA_BloodAxeStolenScrapIntake_A01.blend` | `SourceAssets/Exports/Props/Giants/BloodAxeArmory/Reforging/SM_GIA_BloodAxeStolenScrapIntake_A01.fbx` | `/Game/Aerathea/Props/Giants/BloodAxeArmory/Reforging/SM_GIA_BloodAxeStolenScrapIntake_A01` | Ground center of cluster footprint | 350-700 cm wide, 250-500 cm deep, 120-260 cm high; seized shields, armor plates, hacked weapon bundles, chains, and red warning tags must feel oversized beside 442 cm and 470 cm Giant baselines | 1-2: reforged metal plus optional support cloth/leather | LOD0 5k-12k tris; LOD1 60-70%; LOD2 35-45%; LOD3 15-25%; preserve lopsided pile silhouette and large stolen-object reads | Grouped low-count convex hulls or boxes around main footprint; no per-shard, per-chain, pickup, loot, harvest, or resource collision | Lead/DCC approval required before source creation. Blocks: no DCC/FBX/Unreal work, no loot/pickup/salvage/resource behavior, no material graph or heat-state work, no final visual approval. |
| Broken metal sorting | `SM_GIA_BloodAxeBrokenMetalSorting_A01` | `SourceAssets/Blender/Props/Giants/BloodAxeArmory/Reforging/SM_GIA_BloodAxeBrokenMetalSorting_A01.blend` | `SourceAssets/Exports/Props/Giants/BloodAxeArmory/Reforging/SM_GIA_BloodAxeBrokenMetalSorting_A01.fbx` | `/Game/Aerathea/Props/Giants/BloodAxeArmory/Reforging/SM_GIA_BloodAxeBrokenMetalSorting_A01` | Ground center of table, mat, or bin cluster footprint | 300-650 cm wide, 180-420 cm deep, 90-180 cm high; split blade arcs, cracked plates, snapped spearheads, and bins must read as sorted process pieces, not treasure | 1-2: reforged metal plus optional scorched support material | LOD0 4k-10k tris; LOD1 60-70%; LOD2 35-45%; LOD3 15-25%; preserve table/bin footprint and separated metal categories | Simple table/bin footprint boxes or low-count hulls; no per-fragment, crafting trigger, salvage trigger, or economy/resource collision | Lead/DCC approval required before source creation. Blocks: no DCC/FBX/Unreal work, no crafting/economy/resource behavior, no salvage or upgrade interactions, no material graph authoring, no final visual approval. |
| Billet/ingot stacks | `SM_GIA_BloodAxeBilletIngotStacks_A01` | `SourceAssets/Blender/Props/Giants/BloodAxeArmory/ForgeStock/SM_GIA_BloodAxeBilletIngotStacks_A01.blend` | `SourceAssets/Exports/Props/Giants/BloodAxeArmory/ForgeStock/SM_GIA_BloodAxeBilletIngotStacks_A01.fbx` | `/Game/Aerathea/Props/Giants/BloodAxeArmory/ForgeStock/SM_GIA_BloodAxeBilletIngotStacks_A01` | Stack base/contact center | 140-360 cm wide, 80-220 cm deep, 60-170 cm high; individual bars 90-260 cm long; bridge scrap feedstock and hot-work stages at Giant scale | 1: reforged metal | LOD0 1.5k-5k tris per stack set; LOD1 60-70%; LOD2 35-45%; LOD3 15-25%; preserve rectangular stock mass and stack silhouette | Grouped box or low-count convex hull per stack; no inventory, resource-node, pickup, or economy collision | Lead/DCC approval required before source creation. Blocks: no first DCC target selection here, no DCC/FBX/Unreal work, no crafting/economy/resource behavior, no loot/salvage/upgrade interactions, no material graph authoring. |
| Heated blanks | `SM_GIA_BloodAxeHeatedBlanks_A01` | `SourceAssets/Blender/Props/Giants/BloodAxeArmory/Reforging/SM_GIA_BloodAxeHeatedBlanks_A01.blend` | `SourceAssets/Exports/Props/Giants/BloodAxeArmory/Reforging/SM_GIA_BloodAxeHeatedBlanks_A01.fbx` | `/Game/Aerathea/Props/Giants/BloodAxeArmory/Reforging/SM_GIA_BloodAxeHeatedBlanks_A01` | Center of blank underside or display support contact point | 110-320 cm long; axe-head blanks, cleaver slabs, hammer blocks, hook-spear forms, socket collars, and plate blanks should read as hot-work stock without becoming hazard objects | 1-2: reforged metal; optional heat/emissive slot is future approval-gated only | LOD0 2k-7k tris per blank-stage set; LOD1 60-70%; LOD2 35-45%; LOD3 15-25%; preserve broad blank silhouettes and major weapon-stage forms | Simple bounds for display placement only; no burn, heat hazard, pickup, crafting, material-state, or gameplay interaction collision | Lead/DCC/material/VFX approval required before any source or heat-state work. Blocks: no DCC/FBX/Unreal work, no material graph, no emissive map, no heat-state effects, no crafting/economy/resource behavior, no final visual approval. |
| Remade weapon stages | `KIT_GIA_BloodAxeRemadeWeaponStages_A01` | `SourceAssets/Blender/Props/Giants/BloodAxeArmory/Reforging/KIT_GIA_BloodAxeRemadeWeaponStages_A01.blend` | `SourceAssets/Exports/Props/Giants/BloodAxeArmory/Reforging/KIT_GIA_BloodAxeRemadeWeaponStages_A01.fbx` | `/Game/Aerathea/Props/Giants/BloodAxeArmory/Reforging/KIT_GIA_BloodAxeRemadeWeaponStages_A01` | Ground/display support contact center for each displayed stage; functional grip pivots belong to later weapon packages | 160-430 cm long staged pieces; show rough stock becoming axe heads, cleavers, hammer faces, hook spear heads, and fittings without claiming combat-ready weapons | 1-2: reforged metal plus optional handle/support material | LOD0 6k-14k tris for staged set; LOD1 60-70%; LOD2 35-45%; LOD3 15-25%; preserve process progression and weapon-head silhouettes | Simple box/capsule/convex hull per displayed stage; no combat traces, equipped collision, pickup, salvage, upgrade, or loot collision | Lead/DCC/gameplay approval required before source or functional weapon work. Blocks: no DCC/FBX/Unreal work, no combat/projectile/equipment behavior, no crafting/economy/resource behavior, no salvage/upgrade interactions, no final visual approval. |
| Cooling rack | `SM_GIA_BloodAxeCoolingRack_A01` | `SourceAssets/Blender/Props/Giants/BloodAxeArmory/Reforging/SM_GIA_BloodAxeCoolingRack_A01.blend` | `SourceAssets/Exports/Props/Giants/BloodAxeArmory/Reforging/SM_GIA_BloodAxeCoolingRack_A01.fbx` | `/Game/Aerathea/Props/Giants/BloodAxeArmory/Reforging/SM_GIA_BloodAxeCoolingRack_A01` | Ground center of rack footprint | 420-850 cm wide, 140-300 cm deep, 180-360 cm high; wide rack frame, hooks, crossbars, blank rests, cooling rows, and red cloth tags should read at MMO distance | 1-2: reforged metal plus optional scorched support material | LOD0 5k-12k tris; LOD1 60-70%; LOD2 35-45%; LOD3 15-25%; preserve rack outline, spacing, and blank silhouettes | Simple rack footprint collision with optional upper bounds; no per-hook, per-blank, physics hanging, heat timing, or interaction collision | Lead/DCC approval required before source creation. Blocks: no DCC/FBX/Unreal work, no material heat state, no steam/VFX, no crafting/economy/resource behavior, no pickup/loot/salvage/upgrade interactions. |
| Quench trough | `SM_GIA_BloodAxeQuenchTrough_A01` | `SourceAssets/Blender/Props/Giants/BloodAxeArmory/Reforging/SM_GIA_BloodAxeQuenchTrough_A01.blend` | `SourceAssets/Exports/Props/Giants/BloodAxeArmory/Reforging/SM_GIA_BloodAxeQuenchTrough_A01.fbx` | `/Game/Aerathea/Props/Giants/BloodAxeArmory/Reforging/SM_GIA_BloodAxeQuenchTrough_A01` | Ground center of trough footprint, aligned to long axis for grid placement | 380-850 cm long, 140-260 cm wide, 90-180 cm high; dark trough, reinforced rim, residue plane, ash crust, tongs/rest points, and staining must stay display-focused | 1-2: reforged metal plus optional dark water/residue or support material | LOD0 4k-9k tris; LOD1 60-70%; LOD2 35-45%; LOD3 15-25%; preserve trough body, rim, residue plane, and long-axis footprint | Outer trough hull and optional shell blocking only; no water interaction, steam trigger, hazard, burn damage, crafting, or resource collision | Lead/DCC/material/VFX approval required before source or effects. Blocks: no DCC/FBX/Unreal work, no water/steam/heat-state effects, no crafting/economy/resource behavior, no pickup/loot/salvage/upgrade interactions, no final visual approval. |
| Process markers | `SM_GIA_BloodAxeProcessMarkers_A01` | `SourceAssets/Blender/Props/Giants/BloodAxeArmory/Reforging/SM_GIA_BloodAxeProcessMarkers_A01.blend` | `SourceAssets/Exports/Props/Giants/BloodAxeArmory/Reforging/SM_GIA_BloodAxeProcessMarkers_A01.fbx` | `/Game/Aerathea/Props/Giants/BloodAxeArmory/Reforging/SM_GIA_BloodAxeProcessMarkers_A01` | Stake, plaque, or tag base center | 120-280 cm tall markers; use crude red-cloth tags, hammered metal arrows, tally stakes, and broad Blood Axe sub-faction marks without small readable text | 1-2: reforged metal plus optional red cloth/support material | LOD0 800-3k tris per marker set; LOD1 60-70%; LOD2 35-45%; LOD3 15-25%; preserve large symbol blocks and red accent reads | Simple box/capsule only if standalone; no quest, recipe, vendor, crafting, resource, or interaction trigger collision | Lead/DCC/UI/gameplay approval required before source or behavior. Blocks: no DCC/FBX/Unreal work, no quest/crafting/economy/resource labels, no pickup/loot/salvage/upgrade interactions, no material graph authoring. |
| Composed process layout | `SM_GIA_BloodAxeReforgingProcess_A01` | `SourceAssets/Blender/Props/Giants/BloodAxeArmory/Reforging/SM_GIA_BloodAxeReforgingProcess_A01.blend` | `SourceAssets/Exports/Props/Giants/BloodAxeArmory/Reforging/SM_GIA_BloodAxeReforgingProcess_A01.fbx` | `/Game/Aerathea/Props/Giants/BloodAxeArmory/Reforging/SM_GIA_BloodAxeReforgingProcess_A01` | Ground center of full process footprint | 900-1800 cm wide and 500-1100 cm deep; composed from reusable children in flow order: stolen scrap, broken metal, billets/ingots, heated blanks, remade weapon stages, cooling rack, quench trough, markers | 1-2: reused child material slots; no extra per-stage material proliferation | LOD0 18k-35k tris; LOD1 60-70%; LOD2 35-45%; LOD3 15-25%; preserve complete process readability and major station silhouettes | Grouped display collision with walkable collision disabled by default; no dense per-child, interaction, crafting, salvage, resource, loot, or hazard collision | Lead approval required before deciding whether this composed layout should ever be built. Blocks: no first DCC target selection, no DCC/FBX/Unreal work, no material graph or heat-state work, no crafting/economy/resource behavior, no pickup/loot/salvage/upgrade interactions, no final visual approval. |

## Export Planning Notes

- The rows above are path plans only. They do not imply that `SourceAssets/Blender`, `SourceAssets/Exports`, Unreal folders, `.blend` files, `.fbx` files, or Unreal assets currently exist.
- Future DCC work should preserve reusable child meshes first; the composed process layout is optional and must not replace editable child exports.
- Future LOD source planning should include LOD0-LOD3 for every important child mesh before export.
- Future collision proxies should remain simple, display-only, and separate from gameplay interaction volumes.
- Future material assignment should keep `MI_GIA_BloodAxeReforgedMetal_A01` as the primary docs-only dependency and keep red accents restrained.
- Future material or VFX lanes must separately approve heat states, emissive masks, steam, quench effects, shader graphs, material instances, texture assets, and validators before any implementation.

## Approval Gates

- Lead approval is required before selecting a first DCC target from this manifest.
- DCC approval is required before creating Blender source, folders, source meshes, LOD source files, collision proxies, proof renders, or FBX exports.
- Unreal approval is required before creating Static Mesh assets, materials, textures, Blueprints, validators, startup actors, or Content Browser folders.
- Material/VFX approval is required before material graphs, shaders, texture assets, material instances, emissive maps, heat-state effects, steam VFX, quench VFX, or animated material states.
- Gameplay approval is required before crafting, economy, resource, loot, pickup, salvage, upgrade, vendor, inventory, destructible, hazard, water interaction, damage, encounter, or player interaction behavior.
- Culture approval is required if Blood Axe hostile raider language starts replacing neutral/civilized Giant material, architecture, craft, or settlement identity.
- Source-storage approval is required before any external source concept enters the repository.

## Quality Gate Checklist

- Variant rows cover stolen scrap intake, broken metal sorting, billet/ingot stacks, heated blanks, remade weapon stages, cooling rack, quench trough, process markers, and composed process layout.
- Each row includes planned mesh name, planned Blender source path, planned export path, planned Unreal path, pivot, scale notes, material slots, LOD expectations, collision policy, and implementation blockers.
- Giant scale lock is explicit and unchanged.
- Source/export paths are planning strings only, with no folder or asset creation implied.
- Blood Axe remains a hostile Giant sub-faction and does not overwrite neutral/civilized Giant culture.
- Docs-only/no-build guardrails explicitly block DCC, FBX, Unreal, material graph, heat-state effects, crafting, economy/resource behavior, pickup, loot, salvage, upgrade interactions, final visual approval, and first DCC target selection.
