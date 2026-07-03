# KIT_GIA_BloodAxeQuivers_A01 Variant Export Manifest

## Scope

- Task: `AET-MA-20260629-082`
- Scope type: docs-only variant/export manifest
- Parent kit: `KIT_GIA_BloodAxeArmory_A01`
- Package: `KIT_GIA_BloodAxeQuivers_A01`
- Source concept region: `BloodAxeArmory.png#QuiverArrow_Set`
- Faction/theme: Blood Axe Tribe, hostile Giant sub-faction
- Status: variant/export planning ready; no DCC target selected

This manifest splits the Blood Axe Giant quiver mini-kit into planned child mesh/export rows before any source work begins. It does not create folders, Blender files, FBX files, Unreal Content assets, runtime code, validators, startup-scene actors, or final visual approval.

Blood Axe remains a hostile Giant sub-faction only. This kit must not overwrite neutral or civilized Giant culture, which stays tied to highland stonework, cave settlements, terraces, waterworks, warm hearth language, and restrained blue rune motifs in separate Giant packages.

## Dependencies

- Source package: `docs/assets/kits/KIT_GIA_BloodAxeQuivers_A01/PRODUCTION_PACKAGE.md`.
- Child intake: `docs/assets/kits/KIT_GIA_BloodAxeQuivers_A01/CHILD_ASSET_INTAKE.md`.
- Parent closure: `docs/assets/kits/KIT_GIA_BloodAxeArmory_A01/PACKAGE_CLOSURE_AND_DCC_READINESS.md`.
- Bow scale references: `SM_GIA_BloodAxeLongbow_A01`, `SM_GIA_BloodAxeLongbow_A02`, and `SM_GIA_BloodAxeLongbow_A03`.
- Character scale and attachment dependency: future validation against `SK_GIA_Base_A01` and later approved socket ownership.
- Candidate attachment references only: `back_quiver`, `belt_quiver_l`, `belt_quiver_r`, `belt_tool_l`, `belt_tool_r`, and `back_large_weapon`.
- Shared material planning targets: `MI_GIA_BloodAxeScorchedLeather_A01`, `MI_GIA_BloodAxeBlackenedIron_A01`, `MI_GIA_BloodAxeArrowWood_A01`, `MI_GIA_BloodAxeRedCloth_A01`, and `MI_GIA_BloodAxeBoneTrophy_A01`.

## Giant Scale Lock

Use the validated Giant scale lock exactly:

- Female Giant baseline: 442 cm / 14'6".
- Male Giant baseline: 470 cm / 15'5".
- Approved Giant ranges: females 14-15 ft / 427-457 cm; males 14'10"-16'0" / 452-488 cm.
- Authoring unit: centimeters; 1 Unreal unit = 1 cm.
- Normal humanoid compatibility is not required.

All carry variants must clear Giant pelvis, thighs, spine, shoulders, elbows, hand reach, armor volume, `back_large_weapon`, and quiver socket space before any future promotion. Rack and display variants must read as Giant-made Blood Axe armory props beside a 470 cm male Giant.

## Source-Storage Guardrail

The source concept remains in the external concept folder only. Do not copy, move, edit, embed, crop, relink, or commit the source image for this docs-only package. The planned `SourceAssets/Blender/...` and `SourceAssets/Exports/...` paths below are uncreated path plans only and do not imply any folder or file currently exists.

## Docs-Only and No-Build Guardrails

This manifest does not authorize or perform:

- No first DCC target selection.
- No Blender source creation.
- No source folder creation.
- No DCC modeling work.
- No FBX export.
- No Unreal Content import.
- No material graph, texture asset, Blueprint, validator, runtime source, or startup-scene work.
- No final visual approval or review capture.
- No projectile behavior, arrow flight, combat traces, damage values, ammunition counts, arrow inventory, equip rules, pickup behavior, loot behavior, or rarity rules.
- No bow draw timing, release timing, reload timing, animation montage timing, cloth simulation, physics setup, or runtime attachment behavior.
- No promotion of Blood Axe red-black raider language into neutral or civilized Giant culture.

## Variant Export Table

All source and export paths are planned paths only. They must not be treated as existing files or as approval to create folders. Future DCC work must confirm dimensions, pivots, material slots, collision proxies, and LOD0-LOD3 source/export naming before implementation.

| Child row | Planned mesh name | Planned Blender source path | Planned export path | Planned Unreal path | Pivot | Scale notes | Material slots | LOD expectations | Collision policy | Implementation blockers |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Belt quiver | `SM_GIA_BloodAxeBeltQuiver_A01` | `SourceAssets/Blender/Kits/Giants/BloodAxeArmory/Quivers/SM_GIA_BloodAxeBeltQuiver_A01.blend` | `SourceAssets/Exports/Kits/Giants/BloodAxeArmory/Quivers/SM_GIA_BloodAxeBeltQuiver_A01_LOD{0-3}.fbx` | `/Game/Aerathea/Characters/Giants/BloodAxe/Gear/Quivers/SM_GIA_BloodAxeBeltQuiver_A01` | Intended belt attachment point, defaulting to the side/upper loop that aligns to `belt_quiver_l` or `belt_quiver_r`. | 95-130 cm tall, 24-38 cm wide, 20-34 cm deep; angled for Giant hip carry and thigh clearance. | 1-2 slots; scorched leather/hide primary, shared metal/bone/red cloth accents where needed. | LOD0-LOD3 required; keep shell, rim, top mouth, belt loop, and large arrow read before reducing straps and tags. | Equipped collision disabled; world display uses one simple capsule or box around the shell. | Requires later socket/clearance approval against `SK_GIA_Base_A01`; no DCC, FBX, Unreal, pickup, loot, inventory, projectile, animation, or final visual approval in this task. |
| Back quiver | `SM_GIA_BloodAxeBackQuiver_A01` | `SourceAssets/Blender/Kits/Giants/BloodAxeArmory/Quivers/SM_GIA_BloodAxeBackQuiver_A01.blend` | `SourceAssets/Exports/Kits/Giants/BloodAxeArmory/Quivers/SM_GIA_BloodAxeBackQuiver_A01_LOD{0-3}.fbx` | `/Game/Aerathea/Characters/Giants/BloodAxe/Gear/Quivers/SM_GIA_BloodAxeBackQuiver_A01` | Upper-back attachment point aligned to planned `back_quiver`; must consider `back_large_weapon` space. | 145-185 cm tall, 32-48 cm wide, 28-42 cm deep; top rim clears shoulders, head, arms, and back weapon volume. | 1-2 slots; leather/hide shell, blackened iron reinforcement, shared bone/red cloth accents. | LOD0-LOD3 required; preserve tall back-carry silhouette, top rim, bottom cup, cross straps, and visible arrow direction. | Equipped collision disabled; display variant may use one capsule or box around the body; no per-arrow collision. | Requires later back socket, longbow back-carry, and draw-from-quiver clearance approval; no DCC, FBX, Unreal, projectile, inventory, animation timing, or final visual approval here. |
| Rack quiver | `SM_GIA_BloodAxeRackQuiver_A01` | `SourceAssets/Blender/Kits/Giants/BloodAxeArmory/Quivers/SM_GIA_BloodAxeRackQuiver_A01.blend` | `SourceAssets/Exports/Kits/Giants/BloodAxeArmory/Quivers/SM_GIA_BloodAxeRackQuiver_A01_LOD{0-3}.fbx` | `/Game/Aerathea/Props/Giants/BloodAxeArmory/Quivers/SM_GIA_BloodAxeRackQuiver_A01` | Ground center of rack footprint. | 175-230 cm tall, 60-110 cm wide including frame or stand; must read as Giant-scale camp/armory dressing. | 1-2 slots; wood/leather primary with blackened iron and limited trophy accents. | LOD0-LOD3 required; preserve base footprint, frame, open arrow cluster, and red Blood Axe marker at distance. | Grouped boxes or low-count convex hulls for frame/base; no per-arrow collision. | Requires later DCC target approval and dressing placement approval; no source/export/Unreal work, pickup/loot behavior, projectile logic, animation timing, or final visual approval in this manifest. |
| Loose arrow | `SM_GIA_BloodAxeArrow_A01` | `SourceAssets/Blender/Kits/Giants/BloodAxeArmory/Arrows/SM_GIA_BloodAxeArrow_A01.blend` | `SourceAssets/Exports/Kits/Giants/BloodAxeArmory/Arrows/SM_GIA_BloodAxeArrow_A01_LOD{0-3}.fbx` | `/Game/Aerathea/Props/Giants/BloodAxeArmory/Arrows/SM_GIA_BloodAxeArrow_A01` | Shaft midpoint for display placement; future nock/reference locators require separate approval. | 180-260 cm long with Giant-scale shaft diameter; broadhead, barbed, bodkin, or blunt heads remain display variants only. | 1 slot preferred; shared arrow wood, metal head, fletching, and red/bone accent material treatment. | LOD0-LOD3 required; preserve shaft line, head silhouette, nock end, and fletching block before reducing bevels. | Static display may use one simple capsule or box; no projectile collision, damage collision, or runtime trace volume. | Requires arrow length coordination with longbows A01/A02/A03 and future quiver clearance; no projectile behavior, arrow inventory, equip/ammo rules, animation timing, DCC, FBX, Unreal, pickup/loot, or final visual approval. |
| Arrow bundle | `SM_GIA_BloodAxeArrowBundle_A01` | `SourceAssets/Blender/Kits/Giants/BloodAxeArmory/Arrows/SM_GIA_BloodAxeArrowBundle_A01.blend` | `SourceAssets/Exports/Kits/Giants/BloodAxeArmory/Arrows/SM_GIA_BloodAxeArrowBundle_A01_LOD{0-3}.fbx` | `/Game/Aerathea/Props/Giants/BloodAxeArmory/Arrows/SM_GIA_BloodAxeArrowBundle_A01` | Bundle center or lower tie point, selected later by display use. | 4-10 visible Giant arrows; interior arrow count should be implied through grouped silhouette and texture, not dense geometry. | 1 slot preferred; 2 maximum if tie cloth or metal heads need separation. | LOD0-LOD3 required; preserve grouped mass, major arrow heads, fletching read, and tie band before reducing interior shafts. | One capsule or box around bundle mass; no per-arrow or per-head collision. | Requires later visual density and dressing approval; no arrow inventory, loot pickup, projectile behavior, animation timing, DCC, FBX, Unreal import, or final visual approval. |
| Arrow-head display | `SM_GIA_BloodAxeArrowHeadsDisplay_A01` | `SourceAssets/Blender/Kits/Giants/BloodAxeArmory/Arrows/SM_GIA_BloodAxeArrowHeadsDisplay_A01.blend` | `SourceAssets/Exports/Kits/Giants/BloodAxeArmory/Arrows/SM_GIA_BloodAxeArrowHeadsDisplay_A01_LOD{0-3}.fbx` | `/Game/Aerathea/Props/Giants/BloodAxeArmory/Arrows/SM_GIA_BloodAxeArrowHeadsDisplay_A01` | Board/backing center, or lower center if future wall/table placement requires it. | Oversized 28-65 cm arrow heads on hide, wood, or iron backing; must remain readable without a dense head collection. | 1-2 slots; metal heads plus backing material, sharing existing Blood Axe material targets. | LOD0-LOD3 required; preserve large head silhouettes and backing outline; reduce bevels, pitting, and small head cuts first. | One simple box around board/backing or head cluster; no individual head collision. | Requires later visual approval for head shapes and density; no projectile stats, loot/inventory rules, DCC, FBX, Unreal Content, pickup behavior, animation timing, or final approval. |
| Strap variants | `SM_GIA_BloodAxeQuiverStrap_A01` | `SourceAssets/Blender/Kits/Giants/BloodAxeArmory/Quivers/SM_GIA_BloodAxeQuiverStrap_A01.blend` | `SourceAssets/Exports/Kits/Giants/BloodAxeArmory/Quivers/SM_GIA_BloodAxeQuiverStrap_A01_LOD{0-3}.fbx` | `/Game/Aerathea/Characters/Giants/BloodAxe/Gear/Quivers/SM_GIA_BloodAxeQuiverStrap_A01` | Reuse attach-center per strap segment; final anchor points deferred to belt/back quiver DCC. | 8-18 cm wide straps with oversized buckles/rings; sized for Giant carry gear without obscuring torso or armor readability. | 1 slot preferred; reuse scorched leather, blackened iron, and red cloth material targets. | LOD0-LOD3 required for reusable strap clusters; preserve strap width and buckle/ring read before reducing cuts and stitching. | No standalone collision unless a future large world-prop variant is approved. | Requires later carry-fit and quiver ownership approval; no DCC, FBX, Unreal import, runtime attachment, animation/physics, inventory, pickup/loot, or final visual approval. |
| Trophy tags | `SM_GIA_BloodAxeTrophyTag_A01` | `SourceAssets/Blender/Kits/Giants/BloodAxeArmory/Quivers/SM_GIA_BloodAxeTrophyTag_A01.blend` | `SourceAssets/Exports/Kits/Giants/BloodAxeArmory/Quivers/SM_GIA_BloodAxeTrophyTag_A01_LOD{0-3}.fbx` | `/Game/Aerathea/Props/Giants/BloodAxeArmory/Quivers/SM_GIA_BloodAxeTrophyTag_A01` | Lash point at top of tag cluster, or center of backing tie for reusable placement. | 18-45 cm long tags; bone, tooth, broken token, or red cloth accents used sparingly and never as dense gore. | 1 slot preferred; share bone, cloth, leather, and blackened iron material targets. | LOD0-LOD3 required if promoted as reusable mesh set; preserve largest tag silhouette and lash point, remove small scratches/tally marks first. | No standalone collision unless promoted to a large world prop; no per-tag collision for attached use. | Requires later trophy-density and culture review; no DCC, FBX, Unreal, pickup/loot behavior, inventory rules, animation/physics, graphic gore escalation, or final visual approval. |

## Variant Reuse Rules

- Belt, back, and rack quivers must remain separate child mesh plans. Do not collapse the mini-kit into one exported mesh assumption.
- Loose arrows, arrow bundles, and arrow-head display assets are display geometry and scale references only.
- Strap variants and trophy tags should support reuse across quivers without unique material slots per buckle, strap, tag, or cloth strip.
- Texture and normal maps should carry small stitches, pitting, soot, leather grain, tiny cuts, tally marks, minor rivets, and small binding fibers.
- Real geometry should carry quiver volumes, top rims, bottom cups, rack frames, broad straps, buckles, rings, major arrow heads, fletching blocks, and the largest trophy tags.

## Approval Gates

- Lead approval is required before selecting a first DCC target.
- DCC approval is required before creating Blender source files, source folders, collision proxy meshes, LOD source files, or proof renders.
- Export approval is required before writing FBX files to any `SourceAssets/Exports/...` path.
- Unreal approval is required before importing Static Meshes, materials, textures, Blueprints, validators, or startup actors.
- Gameplay approval is required before projectile behavior, ammunition counts, arrow inventory, pickup behavior, loot rules, equip logic, combat traces, damage values, or hit behavior.
- Animation approval is required before draw timing, release timing, reload timing, montage timing, runtime attachment behavior, cloth simulation, or physics setup.
- Visual approval is required before final silhouette, trophy density, arrow count, red cloth placement, and Blood Axe quiver identity are locked.
- Culture approval is required if Blood Axe raider visuals begin to bleed into neutral or civilized Giant packages.

## Quality Gate Checklist

- Belt quiver, back quiver, rack quiver, loose arrow, arrow bundle, arrow-head display, strap variants, and trophy tags each have separate planned export rows.
- Giant scale lock remains explicit and unchanged.
- Planned Blender source paths and planned FBX export paths are documented as uncreated path plans only.
- Docs-only/no-build guardrails block source folders, Blender files, DCC, FBX, Unreal Content, runtime source, validators, startup-scene work, and final visual approval.
- Projectile behavior, arrow inventory, animation timing, gameplay pickup, and loot behavior are explicitly blocked.
- Blood Axe remains a hostile Giant sub-faction and does not overwrite neutral/civilized Giant culture.
- LOD0-LOD3, pivot, material slot, collision, and implementation blockers are documented for every child row.
