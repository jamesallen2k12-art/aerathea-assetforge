# KIT_GIA_BloodAxeBowyerTools_A01 Variant Export Manifest

## Scope

- Task ID: `AET-MA-20260629-085`
- Scope type: docs-only variant/export manifest for `KIT_GIA_BloodAxeBowyerTools_A01`.
- Parent kit: `KIT_GIA_BloodAxeArmory_A01`.
- Source concept region: `BloodAxeArmory.png#BowyerTools_Set`.
- Faction/theme: Blood Axe Tribe, hostile Giant sub-faction.
- Status: planning manifest only; no first DCC target is selected.

This manifest defines planned mesh names, planned source paths, planned export paths, planned Unreal target paths, pivots, scale notes, material-slot expectations, LOD expectations, collision policy, and implementation blockers for the bowyer tools child rows already defined in the child intake. The path entries below are source/export path plans only. They do not create folders, verify folders, or imply that any Blender, FBX, or Unreal assets already exist.

## Dependencies

- Production package: `docs/assets/kits/KIT_GIA_BloodAxeBowyerTools_A01/PRODUCTION_PACKAGE.md`.
- Child intake: `docs/assets/kits/KIT_GIA_BloodAxeBowyerTools_A01/CHILD_ASSET_INTAKE.md`.
- Related bow support package: `docs/assets/kits/KIT_GIA_BloodAxeBowParts_A01/PRODUCTION_PACKAGE.md`.
- Armory closure/readiness reference: `docs/assets/kits/KIT_GIA_BloodAxeArmory_A01/PACKAGE_CLOSURE_AND_DCC_READINESS.md`.
- Scale dependency: validated `SK_GIA_Base_A01` Giant scale lock.
- Shared visual dependencies: Blood Axe blackened iron, dark steel, scorched workshop wood, scorched leather, cold glue/pitch, dull red cloth or paint, soot, ash, grime, and sparse bone/horn accents.

## Giant Scale Lock

- Female Giant baseline: 442 cm / 14'6".
- Male Giant baseline: 470 cm / 15'5".
- Approved Giant ranges: females 14-15 ft / 427-457 cm; males 14'10"-16'0" / 452-488 cm.
- Authoring unit expectation: centimeters, with future Unreal import scale 1.0.
- Normal humanoid compatibility is not required.
- All variants must remain sized for Giant work surfaces, Giant grip spacing, Giant bow staves, and hostile Giant camp readability.

Do not change the validated Giant scale lock or `SK_GIA_Base_A01` assumptions from this manifest.

## Source-Storage Guardrail

- Source concept remains in the external concept folder only: `/home/Flamestrike/Desktop/Aerathea/Aerathea Creative/ASSET CONCEPTS/BloodAxeArmory.png`.
- Do not copy, move, edit, embed, crop, commit, or re-export the source concept as part of this docs-only manifest.
- Any later source-storage change requires explicit source-storage approval.

## Docs-Only and No-Build Guardrails

- No DCC source creation.
- No Blender source files.
- No source folders.
- No FBX export.
- No Unreal Content import.
- No material graph, shader, texture asset, Niagara, Blueprint, validator, runtime source, or startup-scene work.
- No proof render, final visual approval, or Unreal visual approval claim.
- No first DCC target selection.
- No crafting system, recipe logic, repair cost, resource loop, salvage loop, or economy behavior.
- No usable workstation behavior, interaction prompt, crafting volume, repair bench behavior, or NPC work-loop behavior.
- No inventory item, pickup behavior, loot table, ammunition count, vendor behavior, vendor data, or shop/economy hook.
- No projectile behavior, bow animation timing, damage trace, sharp-edge gameplay collision, liquid simulation, heat state, or VFX.

The planned `SourceAssets/Blender/...`, `SourceAssets/Exports/...`, and `/Game/Aerathea/...` entries are path plans only. They are not build outputs and must not be treated as existing assets.

## Culture Separation Guardrail

Blood Axe remains a hostile Giant sub-faction only. This manifest does not redefine neutral, nomadic, or civilized Giant culture.

- Use Blood Axe raider language: blackened iron, dark steel, scorched wood, rough hide, sinew, dull red cloth or paint, soot, ash, grime, cold glue/pitch, and crude field repair utility.
- Do not apply neutral/civilized Giant blue-gray stoneworker, hidden cave-town, warm hearth, clean monumental masonry, peaceful highland craft, or restrained blue rune language to this Blood Axe bowyer kit.
- Stop if Blood Axe red-black raider language starts replacing default Giant culture in any unrelated package.

## Variant Export Table

| Child row | Planned mesh name | Planned Blender source path | Planned export path | Planned Unreal path | Pivot | Scale notes | Material slots | LOD expectations | Collision policy | Implementation blockers |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `BloodAxeArmory.png#BowyerTools_Clamps_A01` - clamps | `SM_GIA_BloodAxeBowClamp_Loose_A01`, `SM_GIA_BloodAxeBowClamp_Bench_A01`, `SM_GIA_BloodAxeBowClamp_Wedge_A01` | `SourceAssets/Blender/Giants/BloodAxeArmory/BowyerTools/KIT_GIA_BloodAxeBowClamps_A01/KIT_GIA_BloodAxeBowClamps_A01.blend` | `SourceAssets/Exports/Giants/BloodAxeArmory/BowyerTools/KIT_GIA_BloodAxeBowClamps_A01/<planned mesh>.fbx` | `/Game/Aerathea/Props/Giants/BloodAxeArmory/BowyerTools/Clamps/` | Loose clamps pivot at jaw center; bench-mounted clamps pivot at base contact center. | Loose clamps 55-110 cm long; bench clamps 120-190 cm long; all jaws and handles sized for Giant bow staves and Giant hands. | 1 preferred; 2 maximum if metal and scorched-wood/handle separation is required. | LOD0 600-2k tris per loose clamp, 2k-5k tris per variant set; LOD1 60-70 percent, LOD2 35-45 percent, LOD3 15-25 percent while preserving jaw silhouette. | One simple box or low-count convex hull per clamp; no moving jaw collision. | No DCC, FBX, Unreal import, crafting station, workstation behavior, inventory item, vendor data, or first DCC target selection. Variant count must remain sparse and not collapse the whole kit into one mesh. |
| `BloodAxeArmory.png#BowyerTools_DrawKnife_A01` - draw knives | `SM_GIA_BloodAxeDrawKnife_A01` | `SourceAssets/Blender/Giants/BloodAxeArmory/BowyerTools/SM_GIA_BloodAxeDrawKnife_A01/SM_GIA_BloodAxeDrawKnife_A01.blend` | `SourceAssets/Exports/Giants/BloodAxeArmory/BowyerTools/SM_GIA_BloodAxeDrawKnife_A01/SM_GIA_BloodAxeDrawKnife_A01.fbx` | `/Game/Aerathea/Props/Giants/BloodAxeArmory/BowyerTools/DrawKnives/` | Pivot at grip center for reuse; underside center is allowed only for display-only variants if a later task documents it. | Overall width 95-150 cm with wide Giant grip spacing and a broad cutting edge readable from MMO camera distance. | 1 preferred; 2 maximum for metal blade plus leather/wood grip split. | LOD0 700-2k tris; LOD1 reduce bevels and chips; LOD2 simplify handle stops; LOD3 preserve long two-handle silhouette. | One simple box or capsule; no sharp-edge gameplay collision. | No equip behavior, harvesting, damage trace, pickup, inventory, vendor, crafting, DCC, FBX, Unreal import, final visual approval, or first DCC target selection. |
| `BloodAxeArmory.png#BowyerTools_StringingFrame_A01` - stringing frame | `SM_GIA_BloodAxeStringingFrame_A01` | `SourceAssets/Blender/Giants/BloodAxeArmory/BowyerTools/SM_GIA_BloodAxeStringingFrame_A01/SM_GIA_BloodAxeStringingFrame_A01.blend` | `SourceAssets/Exports/Giants/BloodAxeArmory/BowyerTools/SM_GIA_BloodAxeStringingFrame_A01/SM_GIA_BloodAxeStringingFrame_A01.fbx` | `/Game/Aerathea/Props/Giants/BloodAxeArmory/BowyerTools/StringingFrames/` | Pivot at ground center of the frame footprint. | 360-520 cm tall, 170-260 cm wide at base; should stand naturally beside the 470 cm male Giant baseline. | 2 maximum, usually scorched wood plus blackened hardware. | LOD0 5k-10k tris; LOD1 simplify braces and pegs; LOD2 reduce interior cuts; LOD3 preserve height, A-frame/fork silhouette, and base footprint. | Grouped boxes or low-count convex hulls for posts, base braces, and crossbars; no string, tension, or moving-part collision. | No usable workstation, no stringing mechanics, no bow deformation, no crafting system, no NPC work loop, no DCC, no FBX, no Unreal import, no final visual approval, and no first DCC target selection. |
| `BloodAxeArmory.png#BowyerTools_GluePot_A01` - glue pot | `SM_GIA_BloodAxeGluePot_A01` | `SourceAssets/Blender/Giants/BloodAxeArmory/BowyerTools/SM_GIA_BloodAxeGluePot_A01/SM_GIA_BloodAxeGluePot_A01.blend` | `SourceAssets/Exports/Giants/BloodAxeArmory/BowyerTools/SM_GIA_BloodAxeGluePot_A01/SM_GIA_BloodAxeGluePot_A01.fbx` | `/Game/Aerathea/Props/Giants/BloodAxeArmory/BowyerTools/GluePots/` | Pivot at ground or stand center. | 70-120 cm diameter, 65-120 cm tall including stand/base; cold glue/pitch surface only. | 1-2 slots for blackened pot/stand and cold glue/pitch surface. | LOD0 2k-5k tris, or 3k-7k with stand and lid; LOD1 reduce rim bevels; LOD2 simplify lugs/stand; LOD3 preserve squat pot silhouette. | One cylinder-like simplified hull or grouped box/capsule collision for pot and stand; no liquid surface collision. | No heat state, no VFX, no boiling glue, no cooking, no crafting recipe, no economy/resource behavior, no DCC, no FBX, no Unreal import, no final visual approval, and no first DCC target selection. |
| `BloodAxeArmory.png#BowyerTools_MeasuringJig_A01` - measuring jig | `SM_GIA_BloodAxeMeasuringJig_A01` | `SourceAssets/Blender/Giants/BloodAxeArmory/BowyerTools/SM_GIA_BloodAxeMeasuringJig_A01/SM_GIA_BloodAxeMeasuringJig_A01.blend` | `SourceAssets/Exports/Giants/BloodAxeArmory/BowyerTools/SM_GIA_BloodAxeMeasuringJig_A01/SM_GIA_BloodAxeMeasuringJig_A01.fbx` | `/Game/Aerathea/Props/Giants/BloodAxeArmory/BowyerTools/MeasuringJigs/` | Pivot at underside center or left-end reference stop; later DCC must pick one and document it. | 220-420 cm long; large stops and brutal hash marks sized for Giant bow staves; small marks stay painted. | 1 preferred; 2 maximum if wood/iron separation is needed. | LOD0 1.5k-4k tris; LOD1 reduce stop bevels; LOD2 simplify notches; LOD3 preserve long straight rail/board silhouette. | One long box with optional simple stop-block hulls. | No measurement gameplay, no recipe validation, no inventory/economy hook, no workstation behavior, no DCC, no FBX, no Unreal import, no final visual approval, and no first DCC target selection. |
| `BloodAxeArmory.png#BowyerTools_Rasp_A01` - rasp | `SM_GIA_BloodAxeRasp_A01` | `SourceAssets/Blender/Giants/BloodAxeArmory/BowyerTools/SM_GIA_BloodAxeRasp_A01/SM_GIA_BloodAxeRasp_A01.blend` | `SourceAssets/Exports/Giants/BloodAxeArmory/BowyerTools/SM_GIA_BloodAxeRasp_A01/SM_GIA_BloodAxeRasp_A01.fbx` | `/Game/Aerathea/Props/Giants/BloodAxeArmory/BowyerTools/Rasps/` | Pivot at grip center for loose placement; underside center is acceptable for table-only display if later documented. | 75-130 cm long, 10-24 cm wide; chunky grip and file body sized for Giant hands. | 1 preferred. | LOD0 800-2k tris; LOD1 reduce bevels; LOD2 simplify grip/edge profile; LOD3 preserve large hand-file silhouette. Fine teeth remain normal-map detail. | One simple box or capsule; no per-tooth collision. | No harvesting, damage, inventory item, vendor behavior, crafting, DCC, FBX, Unreal import, final visual approval, or first DCC target selection. |
| `BloodAxeArmory.png#BowyerTools_BladeScraper_A01` - blade scraper | `SM_GIA_BloodAxeBladeScraper_A01` | `SourceAssets/Blender/Giants/BloodAxeArmory/BowyerTools/SM_GIA_BloodAxeBladeScraper_A01/SM_GIA_BloodAxeBladeScraper_A01.blend` | `SourceAssets/Exports/Giants/BloodAxeArmory/BowyerTools/SM_GIA_BloodAxeBladeScraper_A01/SM_GIA_BloodAxeBladeScraper_A01.fbx` | `/Game/Aerathea/Props/Giants/BloodAxeArmory/BowyerTools/BladeScrapers/` | Pivot at grip center or underside display center; later DCC must choose based on rack/table use. | 55-100 cm long with a 25-55 cm broad scraping edge; readable thick spine and hanging loop. | 1 preferred. | LOD0 700-1.8k tris; LOD1 reduce edge chips; LOD2 simplify hanging loop and handle; LOD3 preserve flat blade and blunt handle read. | One simple box or capsule; no sharp-edge gameplay collision. | No damage, harvesting, equip, inventory, vendor, crafting, DCC, FBX, Unreal import, final visual approval, or first DCC target selection. |
| `BloodAxeArmory.png#BowyerTools_ToolRack_A01` - tool rack | `SM_GIA_BloodAxeToolRack_A01`, optional later `SM_GIA_BloodAxeToolRack_Wall_A01` | `SourceAssets/Blender/Giants/BloodAxeArmory/BowyerTools/SM_GIA_BloodAxeToolRack_A01/SM_GIA_BloodAxeToolRack_A01.blend` | `SourceAssets/Exports/Giants/BloodAxeArmory/BowyerTools/SM_GIA_BloodAxeToolRack_A01/<planned mesh>.fbx` | `/Game/Aerathea/Props/Giants/BloodAxeArmory/BowyerTools/ToolRacks/` | Ground center for standing rack; back-plane center for wall rack variants. | 220-380 cm wide, 160-280 cm tall; sparse hooks and enough negative space for Giant-scale tools to read clearly. | 1-2 slots for scorched wood plus blackened iron/hardware. | LOD0 3k-7k tris; LOD1 reduce minor hooks; LOD2 simplify interior supports; LOD3 preserve rack outline and broad hook zones. | Grouped boxes for rack frame and large hook zones; no per-tool or per-hook collision if tools are merged into a display variant. | No inventory display system, vendor rack, pickup behavior, usable workstation, dense per-tool collision, DCC, FBX, Unreal import, final visual approval, or first DCC target selection. |
| `BloodAxeArmory.png#BowyerTools_RepairBenchPieces_A01` - repair bench pieces | `SM_GIA_BloodAxeRepairBench_A01`, `SM_GIA_BloodAxeViseBlock_A01`, `SM_GIA_BloodAxeStaveSupport_A01`, `SM_GIA_BloodAxeWedgeTray_A01` | `SourceAssets/Blender/Giants/BloodAxeArmory/BowyerTools/KIT_GIA_BloodAxeRepairBenchPieces_A01/KIT_GIA_BloodAxeRepairBenchPieces_A01.blend` | `SourceAssets/Exports/Giants/BloodAxeArmory/BowyerTools/KIT_GIA_BloodAxeRepairBenchPieces_A01/<planned mesh>.fbx` | `/Game/Aerathea/Props/Giants/BloodAxeArmory/BowyerTools/RepairBenchPieces/` | Ground center for assembled bench pieces; contact center for modular blocks, supports, and trays. | Bench surface 260-480 cm long, 110-180 cm deep, 105-150 cm high; modular pieces must stay Giant-scale and not become normal humanoid props. | 2 maximum for scorched wood plus blackened hardware/glue-pitch accents. | LOD0 6k-12k tris for modular pieces; composed layout under 16k tris; LOD1 reduce underside detail; LOD2 simplify supports/trays; LOD3 preserve bench mass and work-surface silhouette. | Simple grouped boxes for tabletop, legs, vise block, tray, and large supports; walkable collision off unless later environment-cover approval promotes it. | No usable repair bench, crafting recipes, repair costs, resource loop, economy behavior, inventory/vendor behavior, NPC work loop, DCC, FBX, Unreal import, final visual approval, or first DCC target selection. |

## Implementation Stop Conditions

Stop and request a new approved task before any of the following:

- Creating `SourceAssets/Blender` folders or `.blend` files.
- Creating `SourceAssets/Exports` folders or `.fbx` files.
- Importing, authoring, or editing `/Game/Aerathea` Unreal Content assets.
- Creating material graphs, material instances, textures, Blueprints, validators, runtime source, or startup-scene actors.
- Selecting `KIT_GIA_BloodAxeBowyerTools_A01` or any row above as the first DCC build target.
- Claiming final visual approval, Unreal visual approval, or DCC readiness beyond this manifest.
- Defining crafting, repair, economy, workstation, inventory, vendor, loot, projectile, animation, heat, liquid, or VFX behavior.
- Collapsing clamps, draw knives, stringing frame, glue pot, measuring jig, rasp, blade scraper, tool rack, and repair bench pieces into one single mesh.
- Changing the Blood Axe hostile sub-faction identity into default Giant culture.

## Quality Gate Checklist

- Scope is docs-only and manifest-only.
- All child rows from the intake are represented: clamps, draw knives, stringing frame, glue pot, measuring jig, rasp, blade scraper, tool rack, and repair bench pieces.
- Giant scale lock is explicit and unchanged: female baseline 442 cm / 14'6", male baseline 470 cm / 15'5", approved ranges females 14-15 ft and males 14'10"-16'0".
- Planned Blender source paths, planned export paths, and planned Unreal paths are documented as path plans only.
- No folders, DCC files, FBX exports, Unreal assets, runtime source, validators, materials, textures, or startup-scene work are created or claimed.
- Crafting systems, economy/workstation behavior, inventory/vendor behavior, projectile behavior, animation timing, final visual approval, and first DCC target selection are explicitly blocked.
- Blood Axe remains a hostile Giant sub-faction, separate from neutral/civilized Giant culture.
- LOD0-LOD3 expectations, material slot targets, pivots, scale notes, collision policies, and implementation blockers are present for every row.
