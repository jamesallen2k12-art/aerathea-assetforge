# KIT_GIA_BloodAxeBowParts_A01 Variant Export Manifest

## Scope

- Task: `AET-MA-20260629-084`
- Asset kit: `KIT_GIA_BloodAxeBowParts_A01`
- Scope type: docs-only variant/export planning manifest
- Parent kit: `KIT_GIA_BloodAxeArmory_A01`
- Source concept region: `BloodAxeArmory.png#BowStaveParts_Set`
- Faction/theme: Blood Axe Tribe, hostile Giant sub-faction only
- Status: path and variant plan ready for future approval review; no build target selected

This manifest splits the bow-parts child intake into planned DCC/export/Unreal rows for future work. It does not create Blender files, folders, FBX exports, Unreal Content assets, materials, validators, runtime source, startup-scene actors, gameplay behavior, or final visual approval.

## Dependencies

- Planning source: `docs/assets/kits/KIT_GIA_BloodAxeBowParts_A01/PRODUCTION_PACKAGE.md`
- Child split source: `docs/assets/kits/KIT_GIA_BloodAxeBowParts_A01/CHILD_ASSET_INTAKE.md`
- Parent closure gate: `docs/assets/kits/KIT_GIA_BloodAxeArmory_A01/PACKAGE_CLOSURE_AND_DCC_READINESS.md`
- Related shortbow scale/support package: `docs/assets/kits/KIT_GIA_BloodAxeShortbows_A01/PRODUCTION_PACKAGE.md`
- Related quiver/arrow scale package: `docs/assets/kits/KIT_GIA_BloodAxeQuivers_A01/PRODUCTION_PACKAGE.md`
- Longbow support reference: `SM_GIA_BloodAxeLongbow_A01`
- Giant base scale dependency: `SK_GIA_Base_A01`

## Giant Scale Lock

Giant scale is locked exactly to the approved range and baseline:

- Female Giants: 14-15 ft / 427-457 cm.
- Male Giants: 14'10"-16'0" / 452-488 cm.
- Validated baselines: female 442 cm / 14'6"; male 470 cm / 15'5".
- Authoring unit for future DCC: centimeters, with future Unreal import scale 1.0.
- Normal humanoid compatibility is not required for this kit.

All planned children must read as Giant-built Blood Axe bowyer parts beside a 470 cm male Giant and must remain visually aligned to `SM_GIA_BloodAxeLongbow_A01` proportions.

## Source-Storage Guardrail

- The source concept remains in the external concept folder only.
- Do not copy, move, edit, embed, crop, export, or commit the source concept for this docs-only manifest.
- Do not create source folders from this manifest. Every `SourceAssets/Blender/...` and `SourceAssets/Exports/...` entry below is a planned path string only.
- Do not treat any planned path as proof that a file or folder exists.

## Culture Separation

Blood Axe is a hostile Giant sub-faction. This manifest may use dark highland wood, sinew, rawhide, scorched leather, blackened iron, dark steel, horn, bone, torn red cloth markers, soot, resin, and grime. It must not overwrite neutral/civilized Giant culture, which remains separate with mountain stonework, hidden cave towns, warm hearths, restrained rune or storm accents, and blue-gray masonry language in other packages.

## Docs-Only and No-Build Guardrails

- No DCC source creation.
- No Blender source file creation.
- No source folder creation.
- No FBX export.
- No Unreal Content import.
- No material graph, shader, texture, Niagara, Blueprint, validator, runtime source, or startup-scene work.
- No final visual approval claim.
- No first DCC target selection.
- No projectile behavior, projectile collision, projectile stats, arrow stats, arrow damage, hit logic, ammunition counts, inventory behavior, pickup behavior, loot behavior, combat rules, combat traces, bow draw distance, release timing, reload timing, repair interaction timing, animation timing, or animation montage timing.
- No dense per-shaft, per-head, per-string, or per-small-repair-piece collision.
- No collapse of strings, limbs, arrow shafts, arrow heads, wraps, racks, repair pieces, nocks, and bundles into one single mesh assumption.

## Variant and Export Table

All Blender and export paths below are planned paths only. They do not authorize folder creation, file creation, DCC work, FBX export, Unreal import, or promotion to implementation.

| Child row | Planned mesh name | Planned Blender source path | Planned export path | Planned Unreal path | Pivot | Scale notes | Material slots | LOD expectations | Collision policy | Implementation blockers |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `BloodAxeArmory.png#BowParts_StringCoils_A01` | `SM_GIA_BloodAxeBowStringCoil_A01` | `SourceAssets/Blender/Props/Giants/BloodAxeArmory/BowParts/SM_GIA_BloodAxeBowStringCoil_A01.blend` | `SourceAssets/Exports/Props/Giants/BloodAxeArmory/BowParts/SM_GIA_BloodAxeBowStringCoil_A01.fbx` | `/Game/Aerathea/Props/Giants/BloodAxeArmory/BowParts/SM_GIA_BloodAxeBowStringCoil_A01` | Center of coil mass. | 45-85 cm coil diameter; 8-16 cm cord thickness; Giant hand readable. | 1 preferred: shared bow string/rawhide material. | LOD0-LOD3; remove fiber loops first, preserve coil mass and large loop ends. | One simple box or capsule only if world placement needs collision. | Needs future DCC approval, source folder approval, material reuse decision, and no string deformation or animation timing. |
| `BloodAxeArmory.png#BowParts_StringRack_A01` | `SM_GIA_BloodAxeBowStringRack_A01` | `SourceAssets/Blender/Props/Giants/BloodAxeArmory/BowRacks/SM_GIA_BloodAxeBowStringRack_A01.blend` | `SourceAssets/Exports/Props/Giants/BloodAxeArmory/BowRacks/SM_GIA_BloodAxeBowStringRack_A01.fbx` | `/Game/Aerathea/Props/Giants/BloodAxeArmory/BowRacks/SM_GIA_BloodAxeBowStringRack_A01` | Ground center for floor variant; back-plane center for wall variant if split later. | 240-430 cm long; sized for longbow/shortbow support strings. | 1-2: rack wood/leather plus metal or bone accents. | LOD0-LOD3; reduce secondary braces and extra string loops before rack footprint. | Grouped boxes or low-count convex hulls for feet/uprights/crossbars; no per-string collision. | Needs future rack variant approval; no runtime tension simulation, projectile logic, or animation timing. |
| `BloodAxeArmory.png#BowParts_ReplacementLimbs_A01` | `SM_GIA_BloodAxeReplacementLimb_A01` | `SourceAssets/Blender/Weapons/Giants/BloodAxe/Support/SM_GIA_BloodAxeReplacementLimb_A01.blend` | `SourceAssets/Exports/Weapons/Giants/BloodAxe/Support/SM_GIA_BloodAxeReplacementLimb_A01.fbx` | `/Game/Aerathea/Weapons/Giants/BloodAxe/Support/SM_GIA_BloodAxeReplacementLimb_A01` | Center of limb section; optional lower-end lean pivot requires later split approval. | 180-260 cm per half limb; 12-24 cm thick at major sections; aligns to longbow limb scale. | 1 preferred; 2 max if metal/horn tip separation is required. | LOD0-LOD3; preserve curved limb silhouette, horn/iron tips, and broad repairs. | One narrow box or capsule along limb length; no per-splinter collision. | Needs visual approval for longbow fit and future DCC approval; no equipped behavior or bow stat claims. |
| `BloodAxeArmory.png#BowParts_StaveBlanks_A01` | `SM_GIA_BloodAxeStaveBlank_A01` | `SourceAssets/Blender/Weapons/Giants/BloodAxe/Support/SM_GIA_BloodAxeStaveBlank_A01.blend` | `SourceAssets/Exports/Weapons/Giants/BloodAxe/Support/SM_GIA_BloodAxeStaveBlank_A01.fbx` | `/Game/Aerathea/Weapons/Giants/BloodAxe/Support/SM_GIA_BloodAxeStaveBlank_A01` | Part center for rack placement; separate lean variant pivot only by later approval. | 330-455 cm full spare stave or rough blank; 18-34 cm thick before shaping. | 1 preferred: bow wood with texture-only grain/cracks. | LOD0-LOD3; simplify bevels and split cuts while preserving stave length. | One long box or capsule; no per-crack collision. | Needs future build target approval; no proof that Blender/export paths exist. |
| `BloodAxeArmory.png#BowParts_ArrowShafts_A01` | `SM_GIA_BloodAxeArrowShaftSet_A01` | `SourceAssets/Blender/Props/Giants/BloodAxeArmory/ArrowParts/SM_GIA_BloodAxeArrowShaftSet_A01.blend` | `SourceAssets/Exports/Props/Giants/BloodAxeArmory/ArrowParts/SM_GIA_BloodAxeArrowShaftSet_A01.fbx` | `/Game/Aerathea/Props/Giants/BloodAxeArmory/ArrowParts/SM_GIA_BloodAxeArrowShaftSet_A01` | Bundle center or lower tie point for rack insertion. | 180-260 cm shafts; 3-8 cm diameter; grouped stock only. | 1 preferred: shared arrow wood/string binding material. | LOD0-LOD3; reduce duplicate interior shafts before reducing shaft direction. | One long box or capsule around grouped shafts; no per-shaft collision. | Blocks projectile behavior, projectile stats, arrow stats, ammunition counts, hit logic, and launch behavior. |
| `BloodAxeArmory.png#BowParts_ArrowHeads_A01` | `SM_GIA_BloodAxeArrowHeadTray_A01` | `SourceAssets/Blender/Props/Giants/BloodAxeArmory/ArrowParts/SM_GIA_BloodAxeArrowHeadTray_A01.blend` | `SourceAssets/Exports/Props/Giants/BloodAxeArmory/ArrowParts/SM_GIA_BloodAxeArrowHeadTray_A01.fbx` | `/Game/Aerathea/Props/Giants/BloodAxeArmory/ArrowParts/SM_GIA_BloodAxeArrowHeadTray_A01` | Tray or backing center. | 25-70 cm heads; broadhead, barbed, bodkin, blunt, and unfinished display silhouettes only. | 1-2: blackened iron heads plus backing material if needed. | LOD0-LOD3; simplify interior cuts and small bevels before head silhouettes. | One simple box around tray/backing; no per-head collision. | Needs future shape set approval; blocks arrow damage, projectile collision, and combat trace claims. |
| `BloodAxeArmory.png#BowParts_Wraps_A01` | `SM_GIA_BloodAxeWrapBundle_A01` | `SourceAssets/Blender/Props/Giants/BloodAxeArmory/BowParts/SM_GIA_BloodAxeWrapBundle_A01.blend` | `SourceAssets/Exports/Props/Giants/BloodAxeArmory/BowParts/SM_GIA_BloodAxeWrapBundle_A01.fbx` | `/Game/Aerathea/Props/Giants/BloodAxeArmory/BowParts/SM_GIA_BloodAxeWrapBundle_A01` | Center of roll or grouped bundle mass. | 30-90 cm rolls; 8-18 cm strip width; broad strips must read at distance. | 1 preferred: scorched leather/rawhide/red cloth atlas. | LOD0-LOD3; remove tiny stitch/fiber detail first, preserve roll and strip silhouettes. | One simple box/capsule only if used as world placement. | Needs material atlas decision; no cloth simulation or repair interaction timing. |
| `BloodAxeArmory.png#BowParts_NockCaps_A01` | `SM_GIA_BloodAxeBowNockParts_A01` | `SourceAssets/Blender/Props/Giants/BloodAxeArmory/BowParts/SM_GIA_BloodAxeBowNockParts_A01.blend` | `SourceAssets/Exports/Props/Giants/BloodAxeArmory/BowParts/SM_GIA_BloodAxeBowNockParts_A01.fbx` | `/Game/Aerathea/Props/Giants/BloodAxeArmory/BowParts/SM_GIA_BloodAxeBowNockParts_A01` | Grouped display center. | 25-55 cm nock caps/tip parts; grooves must align visually to Giant longbow tips. | 1 preferred; 2 max if horn/bone and blackened iron must separate. | LOD0-LOD3; preserve large grooves, caps, plates, and anchor hooks. | One simple grouped box; no per-groove or per-hook collision. | Needs `SM_GIA_BloodAxeLongbow_A01` fit review; no draw mechanics or string timing. |
| `BloodAxeArmory.png#BowParts_RepairPieces_A01` | `SM_GIA_BloodAxeBowRepairPieces_A01` | `SourceAssets/Blender/Props/Giants/BloodAxeArmory/BowParts/SM_GIA_BloodAxeBowRepairPieces_A01.blend` | `SourceAssets/Exports/Props/Giants/BloodAxeArmory/BowParts/SM_GIA_BloodAxeBowRepairPieces_A01.fbx` | `/Game/Aerathea/Props/Giants/BloodAxeArmory/BowParts/SM_GIA_BloodAxeBowRepairPieces_A01` | Grouped display center or tray center if tray variant is approved. | 35-110 cm splints/clamps; oversized for Giant hands and longbow limbs. | 1-2: blackened iron/bone/horn plus wood/resin backing if needed. | LOD0-LOD3; reduce minor wedges and clamp bevels before splint/clamp silhouettes. | Collision disabled for small dressing; one grouped box only for larger trays. | Needs future approval to avoid becoming a full bowyer tools kit; no interactive repair behavior. |
| `BloodAxeArmory.png#BowParts_FloorRack_A01` | `SM_GIA_BloodAxeBowPartsRack_A01` | `SourceAssets/Blender/Props/Giants/BloodAxeArmory/BowRacks/SM_GIA_BloodAxeBowPartsRack_A01.blend` | `SourceAssets/Exports/Props/Giants/BloodAxeArmory/BowRacks/SM_GIA_BloodAxeBowPartsRack_A01.fbx` | `/Game/Aerathea/Props/Giants/BloodAxeArmory/BowRacks/SM_GIA_BloodAxeBowPartsRack_A01` | Ground center of rack footprint. | 220-340 cm tall, 140-320 cm wide; stable Giant-scale floor contact. | 1-2: rack wood/leather plus metal/bone accents. | LOD0-LOD3; preserve rack footprint, uprights, crossbars, and part silhouette groups. | Grouped boxes or low-count convex hulls for feet/uprights/crossbars/shelves. | Candidate only, not first DCC target; needs lead approval before build and child density review. |
| `BloodAxeArmory.png#BowParts_WallRack_A01` | `SM_GIA_BloodAxeBowPartsWallRack_A01` | `SourceAssets/Blender/Props/Giants/BloodAxeArmory/BowRacks/SM_GIA_BloodAxeBowPartsWallRack_A01.blend` | `SourceAssets/Exports/Props/Giants/BloodAxeArmory/BowRacks/SM_GIA_BloodAxeBowPartsWallRack_A01.fbx` | `/Game/Aerathea/Props/Giants/BloodAxeArmory/BowRacks/SM_GIA_BloodAxeBowPartsWallRack_A01` | Back-plane center for wall snapping. | Wall-leaning or mounted storage; maintains Giant-scale vertical display. | 1-2: rack structure plus accents. | LOD0-LOD3; simplify secondary braces before wall-rack outline and held-part reads. | Grouped simple boxes; no per-part collision inside dense rack. | Needs future wall mounting clearance approval; no Unreal placement or startup scene work. |
| `BloodAxeArmory.png#BowParts_WorkbenchCradle_A01` | `SM_GIA_BloodAxeBowWorkbenchCradle_A01` | `SourceAssets/Blender/Props/Giants/BloodAxeArmory/BowRacks/SM_GIA_BloodAxeBowWorkbenchCradle_A01.blend` | `SourceAssets/Exports/Props/Giants/BloodAxeArmory/BowRacks/SM_GIA_BloodAxeBowWorkbenchCradle_A01.fbx` | `/Game/Aerathea/Props/Giants/BloodAxeArmory/BowRacks/SM_GIA_BloodAxeBowWorkbenchCradle_A01` | Ground or bench contact center, decided in future DCC task. | Low cradle for stave repair and nock fitting; Giant-scale clamp/contact points only. | 1-2: wood/leather plus blackened iron or bone accents. | LOD0-LOD3; preserve cradle supports and clamp silhouettes. | Grouped boxes/low-count hulls for base and major supports only. | Needs future approval for bench-vs-ground variant; no repair interaction, crafting, or animation timing. |
| `BloodAxeArmory.png#BowParts_LimbBundle_A01` | `SM_GIA_BloodAxeLimbBundle_A01` | `SourceAssets/Blender/Props/Giants/BloodAxeArmory/BowParts/SM_GIA_BloodAxeLimbBundle_A01.blend` | `SourceAssets/Exports/Props/Giants/BloodAxeArmory/BowParts/SM_GIA_BloodAxeLimbBundle_A01.fbx` | `/Game/Aerathea/Props/Giants/BloodAxeArmory/BowParts/SM_GIA_BloodAxeLimbBundle_A01` | Bundle center or lower tie point depending on display use. | 90-280 cm tied spare limb/stave mass; 2-5 readable silhouettes. | 1 preferred using shared bow wood/leather/red cloth atlas. | LOD0-LOD3; reduce interior duplicate limbs before bundle outline and red tie. | One box/capsule around bundle mass. | Needs future bundle count approval; no carry/equip behavior without a separate task. |
| `BloodAxeArmory.png#BowParts_ArrowPartsBundle_A01` | `SM_GIA_BloodAxeArrowPartsBundle_A01` | `SourceAssets/Blender/Props/Giants/BloodAxeArmory/ArrowParts/SM_GIA_BloodAxeArrowPartsBundle_A01.blend` | `SourceAssets/Exports/Props/Giants/BloodAxeArmory/ArrowParts/SM_GIA_BloodAxeArrowPartsBundle_A01.fbx` | `/Game/Aerathea/Props/Giants/BloodAxeArmory/ArrowParts/SM_GIA_BloodAxeArrowPartsBundle_A01` | Bundle center or lower tie point. | 90-280 cm mixed shaft/head/wrap mass; implies supply stock without ammunition quantity. | 1 preferred through shared arrow/binding atlas. | LOD0-LOD3; reduce visible shaft/head count before main bundle direction. | One capsule or box around bundle; no per-arrow or per-head collision. | Blocks projectile behavior, ammunition counts, arrow stats, and inventory claims. |
| `BloodAxeArmory.png#BowParts_MixedRepairBundle_A01` | `SM_GIA_BloodAxeBowPartsBundle_A01` | `SourceAssets/Blender/Props/Giants/BloodAxeArmory/BowParts/SM_GIA_BloodAxeBowPartsBundle_A01.blend` | `SourceAssets/Exports/Props/Giants/BloodAxeArmory/BowParts/SM_GIA_BloodAxeBowPartsBundle_A01.fbx` | `/Game/Aerathea/Props/Giants/BloodAxeArmory/BowParts/SM_GIA_BloodAxeBowPartsBundle_A01` | Grouped display center. | 90-280 cm combined strings, wraps, nocks, splints, and trays; shelf/cart/bench filler. | 1 preferred; 2 max if tray backing needs separate material. | LOD0-LOD3; collapse tiny contents into grouped masses before losing bundle silhouette. | One simple box around grouped prop. | Needs future child-density approval; no crafting, repair interaction, loot, or pickup behavior. |

## Shared Material Expectations

Future DCC and Unreal work should reuse the planned Blood Axe material language from the package:

- `MI_GIA_BloodAxeBowWood_A01`
- `MI_GIA_BloodAxeBowString_A01`
- `MI_GIA_BloodAxeScorchedLeather_A01`
- `MI_GIA_BloodAxeBlackenedIron_A01`
- `MI_GIA_BloodAxeBoneHorn_A01`
- `MI_GIA_BloodAxeRedCloth_A01`
- `MI_GIA_BloodAxeSootResin_A01`

Baseline texture expectation remains `BC`, `N`, and packed `ORM`. No emissive map is planned for this baseline kit.

## Approval Gates Before Any Future Implementation

- Lead approval is required before selecting a first DCC target.
- DCC approval is required before creating Blender source, source folders, FBX exports, proof renders, or collision proxy files.
- Unreal approval is required before importing Static Meshes, materials, textures, validators, Blueprints, or startup actors.
- Gameplay approval is required before projectile behavior, projectile stats, arrow stats, damage, hit logic, ammunition, pickup, loot, inventory, combat trace, repair interaction, crafting, or economy behavior.
- Animation approval is required before draw timing, release timing, reload timing, string deformation timing, montage timing, cloth, physics, or runtime equip behavior.
- Visual approval is required before claiming final Blood Axe bow-parts shape language, rack density, repair density, or material color lock.
- Culture approval is required if Blood Axe raider language starts bleeding into neutral/civilized Giant packages.
- Source-storage approval is required before any external concept image enters the repository.

## Quality Gate Checklist

- Variant rows cover strings, limbs, arrow shafts, arrow heads, wraps, racks, repair pieces, nocks, and bundles from the child intake.
- Every row includes planned mesh name, planned Blender source path, planned export path, planned Unreal path, pivot, scale notes, material slots, LOD expectations, collision policy, and implementation blockers.
- Planned paths are path plans only and do not imply files or folders exist.
- Giant scale lock is explicit and unchanged.
- Blood Axe remains a hostile Giant sub-faction, separate from neutral/civilized Giant culture.
- Projectile behavior, arrow stats, animation timing, DCC work, FBX export, Unreal work, final visual approval, and first DCC target selection are explicitly blocked.
- Source concept storage remains external.
- The manifest makes no build, import, runtime, validator, startup-scene, source-copy, or gameplay claim.
