# KIT_GIA_BloodAxeScrapPile_A01 Child Asset Intake

## Source

- Source concept: `/home/Flamestrike/Desktop/Aerathea/Aerathea Creative/ASSET CONCEPTS/BloodAxeArmory.png`
- Source region: `BloodAxeArmory.png#Display_ScrapPileWeapons`
- Parent kit: `KIT_GIA_BloodAxeArmory_A01`
- Material dependency: `MI_GIA_BloodAxeReforgedMetal_A01`
- Faction/theme: Blood Axe Tribe, hostile Giant sub-faction
- Intake status: first-pass scrap-pile child breakdown complete
- Proposed code: `GIA` for Giant race assets, with `BloodAxe` in asset names to keep this hostile sub-faction separate from neutral/civilized Giant culture
- Source-storage guardrail: source concept remains in the external concept folder only. Do not copy, move, edit, embed, or commit the source image for this docs-only package.

## Notes

This intake covers the Blood Axe scrap-pile and reforging-feedstock subset from the armory catalog. It is a set dressing kit, not a gameplay object. Children should support reusable camp and forge layouts while staying clearly non-interactive.

Giant scale lock exactly: female baseline 442 cm / 14'6" and male baseline 470 cm / 15'5", approved ranges females 14-15 ft and males 14'10"-16'0".

All children must preserve Blood Axe hostile raider identity through blackened iron, dark steel, hammered stolen scrap, soot, ash, chipped oxide-red paint, torn red cloth warnings, heavy chain, and scorched support materials. They must not import neutral/civilized Giant blue-gray stoneworker language, warm hearth identity, or restrained blue rune language into this sub-faction kit.

This package does not create DCC source, FBX exports, Unreal Content assets, runtime source, startup-scene placement, gameplay pickups, loot nodes, resource harvesting, destructible props, crafting systems, economy data, or copied concept art.

## Child Asset Table

| Child ID | Type | Proposed asset/package | Variant scope | Material dependency | LOD0 target | Collision plan | Status | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `BloodAxeArmory.png#Scrap_MetalChunks_A01` | Metal chunks | `SM_GIA_BloodAxeMetalChunks_A01` | Reusable large offcuts, shield fragments, plate chunks, and blunt scrap masses | `MI_GIA_BloodAxeReforgedMetal_A01` | 500-2.5k tris per chunk set | Simple box or low-count convex hull only when standalone | Defined in kit package | Build several Giant-scale chunks with broad chipped edges. Use texture/normal detail for pitting, small dents, soot, and scratches. |
| `BloodAxeArmory.png#Scrap_BrokenBlades_A01` | Broken blades | `SM_GIA_BloodAxeBrokenBlades_A01` | Snapped axe arcs, cleaver slabs, spear tips, and bent blade fragments | `MI_GIA_BloodAxeReforgedMetal_A01` | 800-3k tris per blade-fragment set | Simple box/capsule around fragment; no sharp-edge per-poly collision | Defined in kit package | Reads as broken weapon feedstock, not a usable weapon pickup. Keep fragments large enough to show Giant scale. |
| `BloodAxeArmory.png#Scrap_FailedCasts_A01` | Failed casts | `SM_GIA_BloodAxeFailedCasts_A01` | Warped axe-head blanks, collapsed hammer blocks, malformed socket collars, unusable plate casts | `MI_GIA_BloodAxeReforgedMetal_A01` | 1k-4k tris per group | One simplified convex hull per group | Defined in kit package | Shows Blood Axe brute-force reforging process. Avoid precise master-smith polish or neutral Giant craft language. |
| `BloodAxeArmory.png#Scrap_ChainedBundles_A01` | Chained bundles | `SM_GIA_BloodAxeChainedScrapBundle_A01` | Bound scrap stacks, transport bundles, and chained forge feed piles | `MI_GIA_BloodAxeReforgedMetal_A01` plus optional shared leather/cloth slot | 2k-6k tris | One box or convex hull around bundle mass; no per-chain collision | Defined in kit package | Use a few thick chain loops and one or two red cloth warnings. Do not simulate chains or imply pickup handling. |
| `BloodAxeArmory.png#Scrap_ForgeBins_A01` | Forge bins | `SM_GIA_BloodAxeForgeBin_A01` | Squat sorted-scrap bins for forge and armory corners | `MI_GIA_BloodAxeReforgedMetal_A01` plus optional scorched wood/leather support material | 3k-7k tris | Blocking around outer bin shell only; no per-scrap collision | Defined in kit package | Must read as a storage bin for feedstock, not a treasure chest, vendor crate, or resource container. |
| `BloodAxeArmory.png#Scrap_RackScatter_A01` | Rack scatter | `SM_GIA_BloodAxeRackScatter_A01` | Leaning fragments, broken rack supports, and armory wall scatter | `MI_GIA_BloodAxeReforgedMetal_A01` plus optional rack support material | 3k-8k tris | Grouped boxes around leaning pieces and rack footprint | Defined in kit package | Useful for corners, walls, and behind weapon displays. Preserve a clean silhouette and avoid dense shard fields. |
| `BloodAxeArmory.png#Scrap_SlagTrays_A01` | Slag trays | `SM_GIA_BloodAxeSlagTray_A01` | Shallow troughs with cooled slag, ash, soot crust, and heavy rim forms | `MI_GIA_BloodAxeReforgedMetal_A01` with matte slag/ash treatment | 1.5k-5k tris | Tray footprint only; no per-lump collision | Defined in kit package | Baseline is cooled, matte, and non-emissive. Hot slag or forge-heat glow needs separate approval. |
| `BloodAxeArmory.png#Scrap_ReforgingStock_A01` | Reforging stock | `SM_GIA_BloodAxeReforgingStock_A01` | Stacked bars, billets, rough ingots, cut plates, and prepared stock | `MI_GIA_BloodAxeReforgedMetal_A01` | 1k-4k tris per stock stack | Grouped box or low-count convex hull for stack | Defined in kit package | Reads as future Blood Axe weapon material. Do not attach resource-node, inventory, crafting, or economy behavior. |
| `BloodAxeArmory.png#Scrap_ComposedPile_A01` | Composed placement mesh | `SM_GIA_BloodAxeScrapPile_A01` | Ready-to-place non-interactive heap made from the child sets | `MI_GIA_BloodAxeReforgedMetal_A01` plus optional support material | 8k-18k tris | Grouped low-count convex hulls or boxes; walkable collision disabled by default | Defined in kit package | Optional assembly for level dressing. Pivot at ground center. Must remain inert set dressing unless a later task approves gameplay behavior. |

## Placement And Use Rules

- Use child meshes as modular dressing near Blood Axe armories, weapon racks, forge staging, barracks, camp edges, and boss staging areas.
- Keep composed piles sized for Giant handling and readable beside a 470 cm male Giant.
- Use the scrap pile to communicate Blood Axe reforging practice, not player harvesting or economy value.
- Do not place neutral Giant blue-gray stoneworker ornament, warm hearth presentation, peaceful masonry motifs, or restrained blue rune language in this hostile sub-faction kit.
- Keep gore absent or only implied through non-graphic hostile camp dressing; the scrap pile should primarily read as metal feedstock.
- Keep collision simple and display-only. No per-shard, per-chain, pickup, harvest, or destructible collision.

## Immediate Package Priority

Suggested promotion order for future child package or DCC work:

1. `SM_GIA_BloodAxeMetalChunks_A01`
2. `SM_GIA_BloodAxeBrokenBlades_A01`
3. `SM_GIA_BloodAxeReforgingStock_A01`
4. `SM_GIA_BloodAxeForgeBin_A01`
5. `SM_GIA_BloodAxeChainedScrapBundle_A01`
6. `SM_GIA_BloodAxeSlagTray_A01`
7. `SM_GIA_BloodAxeFailedCasts_A01`
8. `SM_GIA_BloodAxeRackScatter_A01`
9. `SM_GIA_BloodAxeScrapPile_A01`

## Approval Gates

- Stop before DCC source creation, FBX export, Unreal Content asset creation, runtime source changes, startup-scene placement, or source-concept copying.
- Stop before adding gameplay pickup, loot, resource harvesting, salvage, crafting, economy, vendor, inventory, destructible, physics-simulation, or encounter-cover behavior.
- Stop if the kit collapses metal chunks, broken blades, failed casts, chained bundles, forge bins, rack scatter, slag trays, and reforging stock into one uneditable mesh assumption.
- Stop if collision becomes dense per-shard or per-chain collision rather than simple display collision.
- Stop if Blood Axe hostile sub-faction language starts replacing neutral/civilized Giant culture.
- Stop before changing the validated Giant scale lock or `SK_GIA_Base_A01` assumptions without a new approval task.
