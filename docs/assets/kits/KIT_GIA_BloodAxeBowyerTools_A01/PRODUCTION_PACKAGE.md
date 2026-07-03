# KIT_GIA_BloodAxeBowyerTools_A01 Production Package

## Art Direction Summary

- Asset name: `KIT_GIA_BloodAxeBowyerTools_A01`
- Asset type: Production kit / oversized static workshop prop set
- Parent source: `KIT_GIA_BloodAxeArmory_A01`
- Source concept region: `BloodAxeArmory.png#BowyerTools_Set`
- Faction/theme: Blood Axe Tribe, hostile Giant sub-faction
- Status: docs-only kit production package ready
- Scope guardrail: this package creates no DCC source, FBX export, Unreal Content asset, runtime source, startup-scene placement, crafting system, usable workstation behavior, inventory rule, economy rule, or copied concept art.

`KIT_GIA_BloodAxeBowyerTools_A01` defines the static workshop tools used around Blood Axe Giant bow-making and repair areas. The set should read as brutal, oversized, field-made equipment for hostile Giant raiders: clamped bow staves, heavy draw knives, a tall stringing frame, a glue pot, measuring jig, rasp, blade scraper, tool rack, and rough repair bench pieces. This language must stay separate from neutral/civilized Giant craft culture, which remains tied to mountain stonework, hidden cave towns, warm hearths, and restrained rune or storm accents.

## Gameplay Purpose

This kit supports environmental storytelling and set dressing only:

- Blood Axe bowyer shelter, armory, forge-camp, raid camp, and repair bench dressing.
- Static props that explain how Giant bows, arrows, straps, and broken weapons are maintained.
- Scale references for future Blood Axe bow, quiver, arrow, and camp packages.
- Reusable workshop clutter that can populate racks, benches, wall mounts, and ground piles without becoming dense micro-detail.

This package does not define crafting stations, player interaction, NPC work loops, usable repair benches, recipe logic, inventory contents, ammunition counts, pickup behavior, loot tables, vendor behavior, economy hooks, bow animation timing, or projectile behavior.

## Silhouette Notes

Primary read should be Giant-scale utility with hostile Blood Axe weight:

- Clamps: broad jaw silhouettes, thick screw or wedge bodies, blackened iron plates, and oversized handles.
- Draw knives: long two-handle blade forms with heavy curved cutting edges sized for Giant hands.
- Stringing frame: tall forked or A-frame structure with massive tension posts and simple string guides.
- Glue pot: heavy cauldron or lidded pitch pot with a squat base, rim, handle lugs, and cold resin/glue surface.
- Measuring jig: long straight-edge board or notched measuring rail with large stops and brutal hash marks.
- Rasp: oversized hand file with a strong rectangular or curved profile and chunky grip.
- Blade scraper: flat scraping blade with a blunt handle, readable edge, and simple hanging loop.
- Tool rack: rough wall or floor rack with clear silhouettes for hanging knives, clamps, rasps, and scrapers.
- Repair bench pieces: giant-height table slabs, vise blocks, stave supports, wedge trays, and battered support legs.

Model the big forms, thick clamps, frame posts, bench slabs, handles, jaw plates, pot rim, major hooks, and large buckles as geometry. Paint or normal-map small scratches, tooth marks, soot, rough wood grain, iron pitting, stitch lines, tiny rivets, tally cuts, and glue streaks.

## Scale Notes

Use the validated `SK_GIA_Base_A01` scale lock exactly:

- Female Giant baseline: 442 cm / 14'6".
- Male Giant baseline: 470 cm / 15'5".
- Approved Giant ranges: females 14-15 ft / 427-457 cm; males 14'10"-16'0" / 452-488 cm.
- Author in centimeters. 1 Unreal unit = 1 cm.
- Normal humanoid compatibility is not required.

Suggested production scale targets:

- Clamps: 55-110 cm long for loose clamps; 120-190 cm for bench-mounted stave clamps.
- Draw knives: 95-150 cm overall width, with handles sized for Giant grip spacing.
- Stringing frame: 360-520 cm tall, 170-260 cm wide at the base, and stable enough to read beside a 470 cm male Giant.
- Glue pot: 70-120 cm diameter, 65-120 cm tall including stand or base.
- Measuring jig: 220-420 cm long, with large stops and notches readable at MMO camera distance.
- Rasp: 75-130 cm long, 10-24 cm wide.
- Blade scraper: 55-100 cm long, with a broad 25-55 cm scraping edge.
- Tool rack: 220-380 cm wide, 160-280 cm tall, with sparse tool silhouettes.
- Repair bench pieces: bench surface 260-480 cm long, 110-180 cm deep, 105-150 cm high; separate blocks, trays, and supports should remain Giant-scale.

Future placement should validate that work surfaces sit naturally for 442 cm and 470 cm Giant proportions. Do not downscale these into ordinary human workshop props.

## Materials and Color Palette

Primary material plan:

- Blackened iron and dark steel for clamp jaws, scraper blades, rasp bodies, hooks, pot rims, frame plates, and bench hardware.
- Scorched dark wood, rough stave wood, cracked workbench planks, and soot-stained support beams.
- Scorched leather, hide lashings, sinew cord, and wrapped grips.
- Bone, horn, and tooth spacers used sparingly as hostile Blood Axe accent material.
- Dull Blood Axe red cloth strips, red paint marks, and dirty red measurement bands used as sub-faction identifiers.
- Cold glue, hide glue, resin, pitch, soot, ash, dried mud, oil-dark stains, and broad hand-painted wear.

Avoid neutral/civilized Giant blue-gray carved stone, warm hearth craft identity, clean monumental masonry, refined highland tools, and restrained blue rune motifs. Those belong to neutral or civilized Giant packages unless a separate stolen-object variant is approved.

Baseline emissive is not planned. Forge heat, boiling glue glow, ritual marks, magic effects, or active workstation states require a separate approval-gated package.

## Concept Image Prompt

Create an original stylized fantasy MMORPG concept image of `KIT_GIA_BloodAxeBowyerTools_A01` for the world of Aerathea. The design should emphasize oversized hostile Giant bowyer workshop tools, heavy clamps, broad draw knives, a tall stringing frame, a squat glue pot, measuring jig, rasp, blade scraper, tool rack, repair bench pieces, scorched wood, blackened iron, dark steel, hide lashings, dull Blood Axe red cloth, soot, grime, rough field repair utility, hostile Blood Axe sub-faction identity, and a gameplay role as static workshop set dressing. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, sparing or no emissive accents, and MMO-friendly production design. Present it as a clean production asset board with front/side callouts, scale notes against a female Giant baseline 442 cm / 14'6" and male Giant baseline 470 cm / 15'5", material swatches, pivot notes, and static-prop collision notes. Avoid copying any existing franchise, avoid graphic gore, avoid usable crafting UI or economy diagrams, avoid making Blood Axe language the default Giant culture, and avoid excessive micro-detail that would not translate to mid-poly Unreal assets.

## Modeling Notes

This is a docs-only package. Future modeling should build reusable static mesh children instead of one collapsed workshop object.

- Clamps: build two or three large clamp shapes with thick jaw blocks, wedge or screw silhouettes, oversized handles, and optional bench-mount feet. Keep the mechanics chunky and readable, not precision-engineered.
- Draw knives: model the blade mass, two handles, hand stops, grip wraps, and major edge chips. Use texture for scratches and sharpening marks.
- Stringing frame: model large posts, A-frame or forked supports, base braces, tension pegs, and simple string guide points. Do not create moving tension mechanics in this package.
- Glue pot: model the pot body, rim, lug handles, lid option, simple stand, and cold resin/glue surface. No liquid simulation, heat state, or VFX.
- Measuring jig: model a long board or iron rail with large stops, sliding block option, and big notches. Paint small marks instead of modeling many grooves.
- Rasp: model the broad file body, large grip, and major teeth silhouette only. Fine tooth pattern belongs in normal maps.
- Blade scraper: model a flat blade, thick spine, rough handle, and hanging loop.
- Tool rack: model a floor or wall rack with big hooks, sparse hanging points, and enough negative space for tools to read clearly.
- Repair bench pieces: model modular bench slabs, vise block, stave support blocks, wedge tray, low shelf, and heavy legs that can be arranged as camp dressing.

Use real geometry for large hardware, bench legs, major supports, pot rim, hooks, handles, and thick bindings. Use texture and normal detail for wood grain, iron pitting, soot, small cuts, glue streaks, minor rivets, stitched leather, and surface wear.

## Texture and Material Notes

Required map set for future texture work:

- Base Color / Albedo (`BC`)
- Normal (`N`)
- Packed Occlusion/Roughness/Metallic (`ORM`)

No emissive map is planned for the baseline kit.

Shared material targets:

- `MI_GIA_BloodAxeReforgedMetal_A01` for blackened iron, dark steel, and hammered hardware.
- `MI_GIA_BloodAxeScorchedWorkshopWood_A01` for bench slabs, stave supports, racks, and measuring jigs.
- `MI_GIA_BloodAxeScorchedLeather_A01` for wraps, lashings, grips, and hanging straps.
- `MI_GIA_BloodAxeGluePitch_A01` for cold glue, resin, and pitch surfaces.
- `MI_GIA_BloodAxeRedCloth_A01` for sparing Blood Axe red accents.
- `MI_GIA_BloodAxeBoneTrophy_A01` only for large spacers or rare hostile accents.

Texture naming examples:

- `T_GIA_BloodAxeBowClamp_A01_BC`
- `T_GIA_BloodAxeBowClamp_A01_N`
- `T_GIA_BloodAxeBowClamp_A01_ORM`
- `T_GIA_BloodAxeDrawKnife_A01_BC`
- `T_GIA_BloodAxeDrawKnife_A01_N`
- `T_GIA_BloodAxeDrawKnife_A01_ORM`
- `T_GIA_BloodAxeStringingFrame_A01_BC`
- `T_GIA_BloodAxeStringingFrame_A01_N`
- `T_GIA_BloodAxeStringingFrame_A01_ORM`
- `T_GIA_BloodAxeRepairBenchPieces_A01_BC`
- `T_GIA_BloodAxeRepairBenchPieces_A01_N`
- `T_GIA_BloodAxeRepairBenchPieces_A01_ORM`

Material slot targets:

- Small tools: 1 material slot where practical.
- Glue pot and tool rack: 1-2 slots.
- Stringing frame and repair bench pieces: 2 slots maximum for wood/hardware separation.
- Avoid unique slots for each scratch, notch, binding, red strip, tooth mark, or small metal insert.

## Triangle Budget

Target LOD0 ranges:

- `KIT_GIA_BloodAxeBowClamps_A01`: 600-2k tris per loose clamp, 2k-5k tris for a clamp variant set.
- `SM_GIA_BloodAxeDrawKnife_A01`: 700-2k tris.
- `SM_GIA_BloodAxeStringingFrame_A01`: 5k-10k tris.
- `SM_GIA_BloodAxeGluePot_A01`: 2k-5k tris, or 3k-7k tris with simple stand and lid.
- `SM_GIA_BloodAxeMeasuringJig_A01`: 1.5k-4k tris.
- `SM_GIA_BloodAxeRasp_A01`: 800-2k tris.
- `SM_GIA_BloodAxeBladeScraper_A01`: 700-1.8k tris.
- `SM_GIA_BloodAxeToolRack_A01`: 3k-7k tris depending on included hooks and hanging points.
- `KIT_GIA_BloodAxeRepairBenchPieces_A01`: 6k-12k tris for modular bench pieces; keep a composed repair bench layout under 16k tris.
- Composed bowyer workshop preview: target under 38k tris by reusing small tools, clamps, hooks, and bench pieces.

These are planning budgets. Future DCC work should preserve large silhouettes before adding tool clutter.

## LOD Plan

All important child meshes need LOD0-LOD3.

- LOD0: full bench/frame/tool silhouettes, major clamps, handles, hooks, pot rim, large notches, thick wraps, big hardware, and primary Blood Axe color blocks.
- LOD1: 60-70 percent of LOD0; reduce minor bevels, small handle cuts, secondary hooks, repeated clamp variants, small notches, and underside bench detail.
- LOD2: 35-45 percent of LOD0; simplify rack hooks, clamp jaws, frame braces, pot handle lugs, scraper edge chips, jig stops, and bench support cuts.
- LOD3: 15-25 percent of LOD0; preserve stringing frame height, bench mass, tool rack outline, pot silhouette, long draw-knife read, clamp jaw shape, and Blood Axe red/black material read.

Remove tiny scratches, pitting, stitch lines, rasp teeth, small notch marks, fine wood grain, glue drips, and minor rivets before reducing frame posts, bench slabs, clamp jaws, pot body, or tool handles.

## Collision Notes

Collision remains simple and static-display focused:

- Loose clamps: one box or low-count convex hull around the main clamp body; no moving jaw collision.
- Draw knife, rasp, and blade scraper: one simple box or capsule for world display; no sharp-edge gameplay collision.
- Stringing frame: grouped boxes or low-count convex hulls for posts, base braces, and crossbars; no string, tension, or moving-part collision.
- Glue pot: one cylinder-like simplified hull or grouped box/capsule collision for pot and stand; no liquid surface collision.
- Measuring jig: one long box with optional simple stop-block hulls.
- Tool rack: grouped boxes for rack frame and large hook zones; no per-tool collision if tools are merged into a rack display variant.
- Repair bench pieces: simple grouped boxes for tabletop, legs, vise block, tray, and large supports; disable walkable collision unless a later environment-cover task explicitly promotes it.

No crafting interaction volume, pickup collision, inventory trigger, economy trigger, projectile collision, damage trace, or animation notify collision is defined by this package.

## Animation Notes

Static mesh baseline. No animations, moving clamps, bendable bow stave behavior, stringing-frame operation, glue heating, NPC work cycle, cloth simulation, interaction prompt, or Blueprint state behavior is authored here.

Future review, if separately assigned, may check only visual placement and clearance:

- Benches and frames sit at useful Giant working height.
- Hanging tools remain readable and do not create dense visual noise.
- Props do not clip through nearby Blood Axe bows, quivers, racks, or camp walls.

## Unreal Import Notes

These are planned import notes only. This task does not create Unreal assets.

Planned asset type:

- Static Meshes for all child props and mini-kit pieces.
- Material Instances using shared Blood Axe workshop material families.
- No Blueprint Actor, gameplay component, crafting widget, inventory item, economy data, or interactable workstation.

Planned folders:

- `/Game/Aerathea/Props/Giants/BloodAxeArmory/BowyerTools/`
- `/Game/Aerathea/Props/Giants/BloodAxeArmory/Workshop/`
- `/Game/Aerathea/Materials/Giants/BloodAxe/`
- `/Game/Aerathea/Textures/Giants/BloodAxe/BowyerTools/`

Planned naming:

- `SM_GIA_BloodAxeBowClamp_A01`
- `SM_GIA_BloodAxeDrawKnife_A01`
- `SM_GIA_BloodAxeStringingFrame_A01`
- `SM_GIA_BloodAxeGluePot_A01`
- `SM_GIA_BloodAxeMeasuringJig_A01`
- `SM_GIA_BloodAxeRasp_A01`
- `SM_GIA_BloodAxeBladeScraper_A01`
- `SM_GIA_BloodAxeToolRack_A01`
- `SM_GIA_BloodAxeRepairBenchPiece_A01`
- `MI_GIA_BloodAxeScorchedWorkshopWood_A01`
- `MI_GIA_BloodAxeGluePitch_A01`

Pivot planning:

- Small loose tools: pivot at grip center for reuse, or underside center for display-only variants. Pick one per child package and document it.
- Clamps: pivot at jaw center for loose clamps; bench-mounted clamps may pivot at base contact.
- Stringing frame: pivot at ground center of the frame footprint.
- Glue pot: pivot at ground or stand center.
- Measuring jig: pivot at underside center or left-end reference stop, depending on layout use.
- Tool rack: pivot at wall/back center for wall variants or ground center for standing variants.
- Repair bench pieces: pivot at ground center for large assembled pieces; pivot at contact center for modular blocks and trays.

Scale: centimeter authored, future Unreal import scale 1.0, with visual validation against the approved Giant baselines before any promotion.

Performance notes: keep material slots low, reuse clamps and hooks, avoid unique mesh variants for every notch or scratch, and keep composed workshop layouts sparse enough to read from MMO camera distance.

## Folder and Naming Recommendation

- Docs folder: `docs/assets/kits/KIT_GIA_BloodAxeBowyerTools_A01/`
- Production package: `docs/assets/kits/KIT_GIA_BloodAxeBowyerTools_A01/PRODUCTION_PACKAGE.md`
- Child intake: `docs/assets/kits/KIT_GIA_BloodAxeBowyerTools_A01/CHILD_ASSET_INTAKE.md`

Future package names, if promoted by later tasks:

- `KIT_GIA_BloodAxeBowClamps_A01`
- `SM_GIA_BloodAxeDrawKnife_A01`
- `SM_GIA_BloodAxeStringingFrame_A01`
- `SM_GIA_BloodAxeGluePot_A01`
- `SM_GIA_BloodAxeMeasuringJig_A01`
- `SM_GIA_BloodAxeRasp_A01`
- `SM_GIA_BloodAxeBladeScraper_A01`
- `SM_GIA_BloodAxeToolRack_A01`
- `KIT_GIA_BloodAxeRepairBenchPieces_A01`

Do not add SourceAssets, FBX exports, Unreal Content assets, runtime source, startup-scene actors, copied source concepts, or global index entries from this task packet.

## Docs-Only Guardrails and Approval Gates

- Stop before DCC source creation, FBX export, Unreal Content asset creation, runtime source changes, startup-scene placement, or source-concept copying.
- Stop before adding crafting systems, usable workstation behavior, interaction prompts, inventory logic, repair costs, recipes, vendors, loot rules, economy hooks, ammunition counts, bow projectile behavior, or NPC work-loop behavior.
- Stop if the mini-kit collapses clamps, draw knives, stringing frame, glue pot, measuring jig, rasp, blade scraper, tool rack, and repair bench pieces into one single mesh assumption.
- Stop if collision becomes per-scratch, per-rivet, per-notch, per-rasp-tooth, per-string, or per-tool-hook complexity.
- Stop if Blood Axe hostile sub-faction language starts replacing neutral/civilized Giant culture.
- Stop before changing the validated Giant scale lock or `SK_GIA_Base_A01` scale assumptions without a new approval task.
- Stop if trophy, gore, red cloth, or workshop clutter becomes too dense for mid-poly MMO readability.

## Quality Gate Checklist

- Blood Axe remains a hostile Giant sub-faction, separate from neutral/civilized Giant culture.
- Giant scale lock exactly: female baseline 442 cm / 14'6" and male baseline 470 cm / 15'5", approved ranges females 14-15 ft and males 14'10"-16'0".
- Child split covers clamps, draw knives, stringing frame, glue pot, measuring jig, rasp, blade scraper, tool rack, and repair bench pieces.
- The kit is docs-only and makes no DCC, FBX, Unreal Content, runtime source, startup-scene, copied concept, crafting, inventory, economy, or usable workstation claim.
- Silhouettes are readable at MMO camera distance and scaled for Giant hands, benches, racks, and camp workshop props.
- Materials use blackened iron, dark steel, scorched wood, hide, leather, sinew, dull red Blood Axe accents, cold glue/pitch, soot, ash, grime, and broad hand-painted wear consistently.
- Neutral/civilized Giant stoneworker, cave-town, warm hearth, and restrained rune language are excluded from the baseline.
- Emissive is absent from the baseline.
- Tiny scratches, rasp teeth, pitting, wood grain, minor rivets, stitch lines, and glue streaks are assigned to texture/normal detail instead of geometry.
- Triangle budgets, texture maps, material slot targets, LOD0-LOD3, collision, animation scope, Unreal import planning, folder recommendations, and approval gates are included.
