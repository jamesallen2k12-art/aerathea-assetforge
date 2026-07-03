# KIT_GIA_BloodAxeReforging_A01 Production Package

## Art Direction Summary

- Asset name: `KIT_GIA_BloodAxeReforging_A01`
- Asset type: Production kit / Giant-scale forge-process prop split
- Parent kit: `KIT_GIA_BloodAxeArmory_A01`
- Source concept region: `BloodAxeArmory.png#Forge_RaidedReforged_Process`
- Primary docs-only material dependency: `MI_GIA_BloodAxeReforgedMetal_A01`
- Faction/theme: Blood Axe Tribe, hostile Giant sub-faction
- Status: docs-only production package ready
- Scope guardrail: this is a forge-process prop/package split, not a functional crafting, salvage, economy, resource, loot, vendor, inventory, or progression system.
- Source-storage guardrail: keep `BloodAxeArmory.png` in the external concept folder only. Do not copy, move, edit, embed, or commit the source image for this package.

`KIT_GIA_BloodAxeReforging_A01` defines the visual process by which hostile Blood Axe Giants break down stolen metal and remake it into brutal raider weapons. The kit should read as an environmental story sequence: seized scrap arrives, metal is broken apart, billets and ingots are stacked, blanks are heated, crude weapon forms are hammered out, hot pieces cool on racks, and finished remade weapons return to the armory.

Blood Axe remains a hostile Giant sub-faction only. This package must not overwrite neutral or civilized Giant culture, which remains tied to mountain stonework, cave halls, hidden highland settlements, terraces, bridges, waterworks, warm hearth presentation, and restrained blue-gray craft language.

Docs-only guardrails: no DCC, FBX, Unreal import, crafting system, economy/resource behavior, material graph authoring, source concept copying, startup placement, or final visual approval.

## Gameplay Purpose

The package supports non-interactive Blood Axe camp and forge dressing. It gives level artists a readable process line that explains how stolen weapons, armor, shields, and scrap are converted into Blood Axe war gear without creating any gameplay system.

Expected use cases:

- Armory and forge-yard set dressing for hostile Blood Axe Giant camps.
- Visual storytelling near `KIT_GIA_BloodAxeScrapPile_A01`, weapon racks, quivers, bowyer corners, and barracks.
- Giant-scale process props that communicate raiding, stripping, heating, hammering, cooling, and remaking stolen metal.
- Static mesh child packages for stolen scrap, broken metal, billets/ingots, heated blanks, remade weapon stages, cooling racks, quench troughs, and process signage or markers.
- Scale and material reference for future Blood Axe forge environments.

Explicit exclusions:

- Not a crafting station.
- Not a player-interactable forge.
- Not a salvage system.
- Not an economy object, inventory object, vendor object, loot container, harvestable resource node, reward chest, or upgrade bench.
- Not a destructible prop, physics puzzle, encounter hazard, or damage source unless a later gameplay task approves a separate variant.
- Not a material graph, shader, texture-authoring, DCC, FBX, Unreal Content, runtime source, startup-scene, or final visual approval task.

## Silhouette Notes

Primary read: a Giant-scale, hostile reforging workflow with heavy, crude, process-readable stations. It should be more organized than a random scrap heap but less refined than a master smithy. The silhouette should show Blood Axe pragmatism: stolen metal goes in, broken and sorted pieces move through rough heating and hammering stages, and oversized remade weapons come out.

Process silhouettes:

- Stolen scrap intake: lopsided stacks of seized shields, broken armor plates, hacked weapon bundles, chains, and red warning tags.
- Broken metal sorting: low heavy tables, split blade arcs, cracked plates, snapped spearheads, and sorted bins of usable metal.
- Billets and ingots: rectangular bars, rough ingot slabs, cut stock, and stacked blocks sized for Giant hands and tongs.
- Heated blanks: broad flat glowing-hot forms, axe-head blanks, hammer blocks, cleaver slabs, socket collars, and plate blanks.
- Remade weapon stages: progression pieces showing rough stock becoming Blood Axe axe heads, cleaver blades, hammer faces, hook spear heads, and heavy fittings.
- Cooling racks: wide open racks, heavy hooks, spaced crossbars, and large blank silhouettes cooling in organized rows.
- Quench trough: long dark trough with ash, soot, quenched metal stains, steam-readiness implied by form only, and no gameplay hazard read.
- Process signage and markers: crude red-cloth tags, tally stakes, warning plaques, hammered metal direction markers, and Blood Axe sub-faction marks that do not rely on readable small text.

Model the large process forms, bin rims, rack frames, trough bodies, billet stacks, blank silhouettes, major chains, and broad weapon-stage shapes. Paint or normal-map small hammer marks, soot streaks, pitting, tiny rivets, scratches, minor weld scars, char, water staining, and small tally cuts.

Avoid treasure-pile readability, neutral Giant craft elegance, clean dwarven smithy precision, player-facing interaction affordances, glowing quest markers, resource-node crystals, dense unreadable shard fields, or graphic gore.

## Scale Notes

Giant scale lock: female Giants 14-15 ft / 427-457 cm; male Giants 14'10"-16'0" / 452-488 cm.

Use the validated `SK_GIA_Base_A01` scale assumptions where applicable:

- Female Giant baseline: 442 cm / 14'6".
- Male Giant baseline: 470 cm / 15'5".
- Author in centimeters. 1 Unreal unit = 1 cm.
- Normal humanoid compatibility is not required.

Suggested production scale targets:

- Full process layout footprint: 900-1800 cm wide, 500-1100 cm deep, broken into modular children rather than one fixed mesh.
- Stolen scrap intake cluster: 350-700 cm wide, 250-500 cm deep, 120-260 cm high.
- Broken metal sorting table or ground sort: 300-650 cm wide, 180-420 cm deep, 90-180 cm high.
- Billet/ingot stacks: 140-360 cm wide, 80-220 cm deep, 60-170 cm high; individual bars 90-260 cm long.
- Heated blanks: 110-320 cm long depending on future weapon type; thick enough to read as Giant-scale stock.
- Remade weapon stage pieces: 160-430 cm long for axe, cleaver, hammer, spear, and fitting blanks.
- Cooling rack: 420-850 cm wide, 140-300 cm deep, 180-360 cm high.
- Quench trough: 380-850 cm long, 140-260 cm wide, 90-180 cm high.
- Process signage/markers: 120-280 cm tall stakes, plaques, and red-cloth tags, readable beside male 470 cm Giants.

Future DCC validation must compare every child against `SK_GIA_Base_A01` female and male baselines before any Unreal placement or visual approval. Props should feel too large for normal humanoids to carry or operate casually.

## Materials and Color Palette

Primary material dependency:

- `MI_GIA_BloodAxeReforgedMetal_A01` for blackened iron, dark steel, hammered stolen scrap, broad edge wear, soot, chipped oxide-red paint, and grime.

Supporting material language:

- Blackened iron and dark steel for stolen metal, billets, weapon stages, rack hardware, trough rims, and forge tools.
- Rough forged plates with broad hammer marks and weld scars.
- Matte soot, ash, charcoal dust, quench stains, and cooled slag residue.
- Scorched timber, dark hide, heavy leather straps, and thick rope only where needed for supports or bundle ties.
- Torn deep red cloth, chipped red paint, and crude metal tags as hostile Blood Axe identifiers.
- Rare bone or trophy accents only as background faction marks, not the main process read.
- Forge orange may appear as restrained painted heat on heated blanks in concept planning, but default emissive/material-state implementation is not included.

Avoid neutral/civilized Giant blue-gray stoneworker motifs, warm hearth calm, peaceful highland craft marks, restrained blue runes, polished masonry, or clean master-smith elegance. Those belong to other Giant packages unless a future stolen/defaced variant is approved.

## Concept Image Prompt

Create an original stylized fantasy MMORPG concept image of `KIT_GIA_BloodAxeReforging_A01` for the world of Aerathea. The design should emphasize a hostile Blood Axe Giant reforging process prop kit, stolen scrap intake, broken metal sorting, billets and ingots, heated blanks, rough remade weapon stages, cooling racks, a quench trough, process signage and markers, blackened iron, dark steel, hammered stolen metal, soot, ash, chipped oxide-red paint, torn red cloth warnings, Giant-scale handling, and `MI_GIA_BloodAxeReforgedMetal_A01` material language. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, restrained or no emissive accents, and MMO-friendly production design. Present it as a clean production asset board and process-flow layout with child split callouts, scale callouts against female Giants 14-15 ft / 427-457 cm and male Giants 14'10"-16'0" / 452-488 cm, material-slot notes, LOD/collision notes, and a clear label that it is non-interactive set dressing rather than crafting, economy, loot, resource, salvage, or upgrade gameplay. Avoid copying any existing franchise, avoid graphic gore, avoid making Blood Axe visual language the default Giant culture, avoid player interaction markers, and avoid excessive micro-detail that would not translate to mid-poly Unreal assets.

## Modeling Notes

This is a docs-only package. Future modeling should build reusable child meshes and a few composed layout variants, not a single collapsed forge-process mesh.

- Stolen scrap intake: build large seized-object silhouettes, chained stacks, red tags, and a rough receiving platform or ground cluster.
- Broken metal sorting: model a heavy sorting surface or ground mat with separated blade arcs, cracked plates, snapped fittings, and sorted bins.
- Billets and ingots: model reusable stacks of rectangular bars, rough ingot slabs, cut plates, and billet bundles with simple bevels.
- Heated blanks: model broad axe-head blanks, hammer blocks, cleaver slabs, hook-spear forms, socket collars, and plate blanks with heat-readiness expressed through material planning, not complex geometry.
- Remade weapon stages: create clear progression pieces from rough blank to crude Blood Axe weapon-head stage; preserve readable major forms over tiny process detail.
- Cooling racks: model wide rack frames, heavy crossbars, hooks, simple support feet, and spaced blanks; keep gaps readable at MMO distance.
- Quench trough: model a heavy trough shell, dark water or residue plane, ash crust, reinforced rim, and oversized tongs or rest points if needed.
- Process signage/markers: build large red-cloth tags, hammered metal markers, tally stakes, and crude warning plaques without relying on small readable writing.

Use real geometry for primary masses, bins, troughs, racks, billet stacks, blank silhouettes, large chains, thick straps, large hooks, and major weapon-stage forms. Use texture and normal detail for small hammer marks, pitting, soot streaks, scratches, tiny rivets, stitch lines, small tally cuts, water stains, and minor weld texture.

Do not add gameplay affordance meshes such as glowing interaction rings, crafting UI plates, pickup handles, loot beams, harvest outlines, resource-node crystals, economy tags, progress meters, recipe boards, or quest markers.

## Texture and Material Notes

Required map set for future texture work:

- Base Color / Albedo (`BC`)
- Normal (`N`)
- Packed Occlusion/Roughness/Metallic (`ORM`)

No material graph, shader, material instance, texture asset, or Unreal import is authored by this package.

Material slot plan:

- Slot 0: `MI_GIA_BloodAxeReforgedMetal_A01` for stolen scrap, broken metal, billets, ingots, heated blank bases, remade weapon stages, rack hardware, trough rims, and process markers.
- Optional slot 1: shared scorched wood/leather/cloth support material for rack supports, straps, red cloth, marker ties, and platform pieces.
- Optional slot 2: future approval-gated heat-state material or emissive mask for hot blanks only. Baseline `A01` does not author this material state.

Texture naming examples:

- `T_GIA_BloodAxeReforging_A01_BC`
- `T_GIA_BloodAxeReforging_A01_N`
- `T_GIA_BloodAxeReforging_A01_ORM`
- `T_GIA_BloodAxeBilletIngots_A01_BC`
- `T_GIA_BloodAxeHeatedBlanks_A01_BC`
- `T_GIA_BloodAxeRemadeWeaponStages_A01_BC`
- `T_GIA_BloodAxeCoolingRack_A01_BC`
- `T_GIA_BloodAxeQuenchTrough_A01_BC`
- Future approval-gated only: `T_GIA_BloodAxeHeatedBlanks_A01_E`

Use 1K texture sets for small repeated marker and billet children, 2K for racks, troughs, staged weapon sets, and composed process clusters, and 4K only if a later hero forge scene specifically approves close-up review. Keep red paint and cloth accents restrained so the kit reads as blackened metal and process props first.

## Triangle Budget

Target LOD0 ranges:

- `SM_GIA_BloodAxeStolenScrapIntake_A01`: 5k-12k tris.
- `SM_GIA_BloodAxeBrokenMetalSorting_A01`: 4k-10k tris.
- `SM_GIA_BloodAxeBilletIngotStacks_A01`: 1.5k-5k tris per stack set.
- `SM_GIA_BloodAxeHeatedBlanks_A01`: 2k-7k tris per blank-stage set.
- `KIT_GIA_BloodAxeRemadeWeaponStages_A01`: 6k-14k tris for a staged set, using reusable weapon-head children.
- `SM_GIA_BloodAxeCoolingRack_A01`: 5k-12k tris depending on blank count.
- `SM_GIA_BloodAxeQuenchTrough_A01`: 4k-9k tris.
- `SM_GIA_BloodAxeProcessMarkers_A01`: 800-3k tris per marker set.
- `SM_GIA_BloodAxeReforgingProcess_A01` composed preview or placement cluster: 18k-35k tris, built from reusable child meshes.

Target material slots:

- Small child props: 1 material slot where possible.
- Racks, troughs, and composed process clusters: 1-2 material slots.
- Heated blank variants: 1-2 material slots, with any emissive/heat slot future approval-gated.
- Avoid separate material slots for every scrap fragment, tag, soot patch, chain, or tally mark.

Do not increase geometry just to express fine pitting, micro scratches, dense hammer marks, small soot flecks, tiny rivets, chain clutter, minor cracks, or small label cuts.

## LOD Plan

All important child meshes need LOD0-LOD3.

- LOD0: full primary process silhouettes, large scrap forms, broken blade profiles, billet stacks, heated blank shapes, remade weapon stages, cooling rack frames, quench trough body, marker shapes, large chains, red cloth accents, and broad material zones.
- LOD1: 60-70 percent of LOD0; reduce small bevels, secondary chips, minor chain subdivisions, small marker ties, inner pile details, and dense blank-edge cuts.
- LOD2: 35-45 percent of LOD0; simplify rack crossbar count, trough rim bevels, billet stack interiors, weapon-stage cutouts, small hanging markers, and back-side details.
- LOD3: 15-25 percent of LOD0; preserve process read, rack/trough/scrap/blank silhouettes, major Blood Axe red accent blocks, and large dark-metal material areas.

Remove tiny rivets, scratches, pitting, small straps, tally cuts, duplicate chain segments, minor labels, and interior/backside details before reducing the major process stations, billet stacks, blank silhouettes, cooling rack outline, or quench trough footprint.

## Collision Notes

Collision remains simple, static, and display-focused.

- Stolen scrap intake: grouped low-count convex hulls or boxes around the main footprint; no per-shard collision.
- Broken metal sorting: box or low-count hull around table/ground cluster and large bins only.
- Billet/ingot stacks: grouped box or simple convex hull per stack.
- Heated blanks: simple bounds for display placement only; no burn, hazard, pickup, or crafting trigger collision.
- Remade weapon stages: simple box/capsule/convex hull for each displayed stage; combat traces belong to future weapon packages, not this process kit.
- Cooling rack: simple rack footprint collision and optional upper bounds; no per-hook or per-blank collision unless a later environment task requires it.
- Quench trough: outer trough hull and optional blocking volume around the shell; no water interaction, damage, steam, or crafting trigger volumes.
- Process markers: simple box/capsule collision only if standalone; otherwise no collision.
- Composed process cluster: grouped display collision with walkable collision disabled by default.

Do not add pickup collision, harvest volumes, crafting interaction volumes, recipe zones, economy/resource triggers, loot outlines, destructible fracture collision, physics-simulated loose scrap, per-chain collision, per-shard collision, or encounter hazard volumes.

## Animation Notes

Static mesh baseline. No animations, physics simulation, material-state timing, heat shimmer, steam VFX, quench effects, hammering loops, crafting loops, UI progress states, player interaction states, economy presentation, pickup animations, salvage loops, or destruction states are authored here.

Future approval-gated variants may add:

- NPC-only forge activity around the props through a separate Giant camp or encounter task.
- Subtle forge-heat material state for hot blanks through a separate approved material/VFX package.
- Ambient steam or sound markers through a separate environment/VFX task.
- Encounter hazard behavior only through a separate gameplay task.

Baseline `A01` stays inert set dressing.

## Unreal Import Notes

These are planned import notes only. This task does not create Unreal assets or perform an Unreal import.

Planned asset types:

- Static Mesh children for stolen scrap, broken metal, billet/ingot stacks, heated blanks, remade weapon stages, cooling racks, quench troughs, process markers, and optional composed process clusters.
- Optional kit-level composed Static Mesh preview for non-interactive set dressing.
- Docs-only Material Instance dependency: `MI_GIA_BloodAxeReforgedMetal_A01`.

Planned folders:

- `/Game/Aerathea/Props/Giants/BloodAxeArmory/Reforging/`
- `/Game/Aerathea/Props/Giants/BloodAxeArmory/ForgeStock/`
- `/Game/Aerathea/Materials/Giants/BloodAxe/`

Planned naming:

- `SM_GIA_BloodAxeStolenScrapIntake_A01`
- `SM_GIA_BloodAxeBrokenMetalSorting_A01`
- `SM_GIA_BloodAxeBilletIngotStacks_A01`
- `SM_GIA_BloodAxeHeatedBlanks_A01`
- `KIT_GIA_BloodAxeRemadeWeaponStages_A01`
- `SM_GIA_BloodAxeCoolingRack_A01`
- `SM_GIA_BloodAxeQuenchTrough_A01`
- `SM_GIA_BloodAxeProcessMarkers_A01`
- `SM_GIA_BloodAxeReforgingProcess_A01`
- `MI_GIA_BloodAxeReforgedMetal_A01`

Pivot planning:

- Stolen scrap intake: ground center of cluster footprint.
- Broken metal sorting: ground center of table, mat, or bin cluster footprint.
- Billet/ingot stacks: stack base/contact center.
- Heated blanks: center of blank underside or display support contact point.
- Remade weapon stages: ground/display support contact center for each stage; grip pivots belong to later functional weapon packages.
- Cooling rack: ground center of rack footprint.
- Quench trough: ground center of trough footprint, aligned to long axis for grid placement.
- Process markers: base center for stakes, plaques, or tag stands.
- Composed process cluster: ground center of the full process footprint.

Import rules for any future build:

- Author in centimeters and import at scale 1.0.
- Assign LOD0-LOD3 for all important static meshes.
- Target 1-2 material slots per child mesh.
- Use `MI_GIA_BloodAxeReforgedMetal_A01` for primary metal surfaces.
- Keep collision simple and display-only.
- Do not create Blueprint interaction, crafting recipes, resource nodes, economy data, loot tables, upgrade data, salvage behavior, material graphs, shaders, startup placement, or final visual approval artifacts.

## Folder and Naming Recommendation

- Docs folder: `docs/assets/kits/KIT_GIA_BloodAxeReforging_A01/`
- Production package: `docs/assets/kits/KIT_GIA_BloodAxeReforging_A01/PRODUCTION_PACKAGE.md`
- Child intake: `docs/assets/kits/KIT_GIA_BloodAxeReforging_A01/CHILD_ASSET_INTAKE.md`

Future child package recommendations, if promoted by later tasks:

- `docs/assets/props/SM_GIA_BloodAxeStolenScrapIntake_A01/`
- `docs/assets/props/SM_GIA_BloodAxeBrokenMetalSorting_A01/`
- `docs/assets/props/SM_GIA_BloodAxeBilletIngotStacks_A01/`
- `docs/assets/props/SM_GIA_BloodAxeHeatedBlanks_A01/`
- `docs/assets/kits/KIT_GIA_BloodAxeRemadeWeaponStages_A01/`
- `docs/assets/props/SM_GIA_BloodAxeCoolingRack_A01/`
- `docs/assets/props/SM_GIA_BloodAxeQuenchTrough_A01/`
- `docs/assets/props/SM_GIA_BloodAxeProcessMarkers_A01/`
- `docs/assets/props/SM_GIA_BloodAxeReforgingProcess_A01/`

Do not add SourceAssets, FBX exports, Unreal Content assets, runtime source, startup-scene actors, copied source concepts, global index entries, crafting data, economy data, resource behavior, loot definitions, destructible components, material graphs, shaders, or pickup interactions from this task packet.

## Docs-Only Guardrails

- No DCC source creation.
- No FBX export.
- No Unreal import or Unreal Content asset creation.
- No runtime source changes.
- No material graph authoring or shader authoring.
- No crafting system, crafting recipe, salvage loop, upgrade bench, economy/resource behavior, loot table, vendor data, inventory data, or harvest node.
- No source concept copying, moving, embedding, editing, or committing.
- No startup-scene placement.
- No final visual approval claim.
- No changes to global indexes or task boards from this task packet.

## Quality Gate Checklist

- Blood Axe remains a hostile Giant sub-faction, separate from neutral/civilized Giant culture.
- Giant scale lock is explicit: female Giants 14-15 ft / 427-457 cm; male Giants 14'10"-16'0" / 452-488 cm.
- Package reads as forge-process set dressing, not crafting, economy, loot, resource, salvage, upgrade, destruction, or pickup gameplay.
- Child split covers stolen scrap, broken metal, billets/ingots, heated blanks, remade weapon stages, cooling racks, quench trough, and process signage/markers.
- Primary material plan is tied to docs-only dependency `MI_GIA_BloodAxeReforgedMetal_A01`.
- Primary silhouettes are readable at MMO distance and buildable as mid-poly static meshes.
- Tiny dents, pitting, scratches, soot, water stains, weld scars, hammer noise, small tally cuts, and minor rivets are assigned to textures/normals instead of geometry.
- Emissive is absent by default and approval-gated for any future heated blank, forge-heat, or shamanic variant.
- Triangle budgets, material slots, texture maps, LOD0-LOD3, collision, pivot planning, Unreal import notes, folders, naming, and child package recommendations are included.
- Package makes no DCC, FBX, Unreal Content, Unreal import, runtime, startup-scene, source concept, global index, crafting, economy/resource, material graph, shader, final visual approval, gameplay pickup, loot, resource-node, or destruction claim.
