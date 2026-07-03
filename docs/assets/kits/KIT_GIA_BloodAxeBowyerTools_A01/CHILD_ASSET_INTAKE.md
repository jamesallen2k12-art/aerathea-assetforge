# KIT_GIA_BloodAxeBowyerTools_A01 Child Asset Intake

## Source

- Source concept: `/home/Flamestrike/Desktop/Aerathea/Aerathea Creative/ASSET CONCEPTS/BloodAxeArmory.png`
- Source region: `BloodAxeArmory.png#BowyerTools_Set`
- Parent kit: `KIT_GIA_BloodAxeArmory_A01`
- Faction/theme: Blood Axe Tribe, hostile Giant sub-faction
- Intake status: first-pass bowyer tools mini-kit child breakdown complete
- Proposed code: `GIA` for Giant race assets, with `BloodAxe` in asset names to keep this hostile sub-faction separate from neutral/civilized Giant culture
- Source-storage guardrail: source concept remains in the external concept folder only. Do not copy, move, edit, embed, or commit the source image for this docs-only package.

## Notes

This intake covers static bowyer workshop props for Blood Axe Giant camps and armories. The children are planning targets for oversized static set dressing: clamps, draw knives, stringing frame, glue pot, measuring jig, rasp, blade scraper, tool rack, and repair bench pieces.

Giant scale lock exactly: female baseline 442 cm / 14'6" and male baseline 470 cm / 15'5", approved ranges females 14-15 ft and males 14'10"-16'0". All child props must be sized for Giant work surfaces, Giant grip spacing, and Giant camp readability, not normal humanoid workshop scale.

The kit must preserve Blood Axe hostile raider identity through blackened iron, dark steel, scorched wood, rough hide, sinew, dull red cloth/paint, soot, ash, cold glue/pitch, and grime. It must not import neutral/civilized Giant blue-gray stoneworker, hidden cave-town, warm hearth, or restrained rune language into this sub-faction kit.

This package does not create DCC source, FBX exports, Unreal Content assets, runtime source, startup-scene placement, crafting systems, usable workstation behavior, interaction prompts, inventory rules, economy rules, projectile behavior, animation timing, or copied concept art.

## Child Asset Table

| Child ID | Type | Proposed asset/package | Static prop scope | LOD0 target | Collision plan | Status | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `BloodAxeArmory.png#BowyerTools_Clamps_A01` | Clamps | `KIT_GIA_BloodAxeBowClamps_A01` | Loose clamps, bench clamps, wedge clamps | 600-2k tris per clamp; 2k-5k tris per variant set | One simple box or low-count convex hull per clamp; no moving jaw collision | Defined in mini-kit package | Oversized jaw blocks, blackened iron plates, heavy handles, and rough wedge/screw silhouettes scaled for Giant bow staves. |
| `BloodAxeArmory.png#BowyerTools_DrawKnife_A01` | Draw knife | `SM_GIA_BloodAxeDrawKnife_A01` | Static table, rack, or bench prop | 700-2k tris | One simple box or capsule; no sharp-edge gameplay collision | Defined in mini-kit package | Broad two-handle blade for shaving Giant bow staves. Fine scratches and sharpening marks belong in texture/normal maps. |
| `BloodAxeArmory.png#BowyerTools_StringingFrame_A01` | Stringing frame | `SM_GIA_BloodAxeStringingFrame_A01` | Large standing bow stringing and tension frame | 5k-10k tris | Grouped boxes or low-count convex hulls for posts/base; no string or moving-part collision | Defined in mini-kit package | Tall A-frame or forked posts with heavy braces and tension pegs. Static display only, not a usable workstation. |
| `BloodAxeArmory.png#BowyerTools_GluePot_A01` | Glue pot | `SM_GIA_BloodAxeGluePot_A01` | Cold glue, resin, or pitch pot with simple stand | 2k-5k tris; 3k-7k with stand/lid | Simple cylinder-like hull or grouped box/capsule; no liquid collision | Defined in mini-kit package | Squat pot, heavy rim, lug handles, soot, cold glue surface, and grime. No heat state, VFX, cooking, or crafting behavior. |
| `BloodAxeArmory.png#BowyerTools_MeasuringJig_A01` | Measuring jig | `SM_GIA_BloodAxeMeasuringJig_A01` | Giant bow stave measuring rail or notched board | 1.5k-4k tris | One long box plus optional simple stop-block hulls | Defined in mini-kit package | Long board or iron rail with large stops and readable Blood Axe red measurement bands. Small marks should be painted. |
| `BloodAxeArmory.png#BowyerTools_Rasp_A01` | Rasp | `SM_GIA_BloodAxeRasp_A01` | Static hand file/table or rack prop | 800-2k tris | One simple box or capsule | Defined in mini-kit package | Huge file body with chunky grip. Only the largest tooth silhouette is geometry; fine teeth are normal-map detail. |
| `BloodAxeArmory.png#BowyerTools_BladeScraper_A01` | Blade scraper | `SM_GIA_BloodAxeBladeScraper_A01` | Static scraper tool for stave cleanup | 700-1.8k tris | One simple box or capsule | Defined in mini-kit package | Flat scraper blade, thick spine, blunt handle, hanging loop, and blackened iron edge. No damage or harvesting behavior. |
| `BloodAxeArmory.png#BowyerTools_ToolRack_A01` | Tool rack | `SM_GIA_BloodAxeToolRack_A01` | Wall or standing rack for sparse hanging tools | 3k-7k tris | Grouped boxes for rack and large hook zones; no per-hook collision | Defined in mini-kit package | Rough rack with oversized hooks and negative space. Avoid dense hanging clutter and unique material slots for every tool. |
| `BloodAxeArmory.png#BowyerTools_RepairBenchPieces_A01` | Repair bench pieces | `KIT_GIA_BloodAxeRepairBenchPieces_A01` | Modular bench slabs, vise block, stave supports, wedge tray, shelf, heavy legs | 6k-12k tris for pieces; composed layout under 16k tris | Simple grouped boxes for tabletop, legs, vise block, tray, and supports; walkable off unless approved later | Defined in mini-kit package | Static repair bench dressing only. Do not define usable repair bench behavior, recipes, costs, inventory, or economy hooks. |

## Attachment And Display Rules

- Small tools should support table, rack, wall, and ground display placement without requiring equip sockets.
- If a future package needs a handheld prop variant, it should define a separate pivot and attachment note at that time.
- Stringing frame, tool rack, glue pot, and repair bench pieces should use ground or wall pivots appropriate to static camp dressing.
- Repair bench pieces should remain modular so later DCC work can compose dense or sparse workshop layouts without making one oversized combined mesh.
- Collision stays simple and display-focused. No per-tool collision on merged rack displays, no moving clamp collision, no string collision, no liquid collision, and no crafting interaction volume.

## Suggested Promotion Order

1. `SM_GIA_BloodAxeStringingFrame_A01`
2. `KIT_GIA_BloodAxeRepairBenchPieces_A01`
3. `SM_GIA_BloodAxeToolRack_A01`
4. `KIT_GIA_BloodAxeBowClamps_A01`
5. `SM_GIA_BloodAxeGluePot_A01`
6. `SM_GIA_BloodAxeDrawKnife_A01`
7. `SM_GIA_BloodAxeMeasuringJig_A01`
8. `SM_GIA_BloodAxeRasp_A01`
9. `SM_GIA_BloodAxeBladeScraper_A01`

## Approval Gates

- Stop before DCC source creation, FBX export, Unreal Content asset creation, runtime source changes, startup-scene placement, or source-concept copying.
- Stop before defining crafting systems, usable workstation behavior, interaction prompts, inventory rules, repair costs, recipes, vendors, loot behavior, economy hooks, projectile behavior, bow animation timing, or NPC work loops.
- Stop if clamps, draw knives, stringing frame, glue pot, measuring jig, rasp, blade scraper, tool rack, and repair bench pieces collapse into one mesh assumption.
- Stop if collision becomes dense per-tool, per-hook, per-string, per-liquid, per-notch, or per-rasp-tooth collision rather than simple static prop collision.
- Stop if Blood Axe hostile sub-faction language starts replacing neutral/civilized Giant culture.
- Stop before changing the validated Giant scale lock or `SK_GIA_Base_A01` scale assumptions without a new approval task.
