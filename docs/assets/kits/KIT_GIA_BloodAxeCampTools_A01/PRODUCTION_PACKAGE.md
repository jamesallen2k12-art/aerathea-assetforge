# KIT_GIA_BloodAxeCampTools_A01 Production Package

## Art Direction Summary

- Asset name: `KIT_GIA_BloodAxeCampTools_A01`
- Asset type: Production kit / static camp utility dressing split
- Parent intake row: `KIT_GIA_BloodAxeCamp_A01` child `BloodAxeCamp.png#Clutter_ToolBucketRopeCoils`
- Related package: `KIT_GIA_BloodAxeBowyerTools_A01`
- Faction/theme: Blood Axe Tribe, hostile Giant sub-faction
- Status: docs-only production package ready
- Scope guardrail: planning only; no DCC, FBX, Unreal Content, runtime source, usable workstation behavior, tool pickup behavior, crafting/resource/economy behavior, interaction behavior, startup placement, or first DCC target selection.

`KIT_GIA_BloodAxeCampTools_A01` defines static camp-local utility clutter for Blood Axe Giant camps: tool buckets, rope coils, large hooks, splitting wedges, mallets, crude carry tubs, tie-down hardware, and small composed utility clusters. It is more general and camp-facing than `KIT_GIA_BloodAxeBowyerTools_A01`, which owns specialized bowyer workshop equipment.

The set should read as brutal, practical, oversized, and field-made for a hostile raider camp. Blood Axe language must remain a hostile Giant sub-faction identity, not the default neutral/civilized Giant culture. Do not import blue-gray cave-town masonry, refined stoneworker tools, warm hearth presentation, restrained blue runes, terrace craft, or peaceful highland settlement language into this baseline kit.

## Gameplay Purpose

This kit supports non-interactive environmental storytelling and visual scale only:

- Camp utility dressing near shelters, gates, forge support areas, paths, banners, and watch points.
- Scale anchors for Blood Axe camp work lanes beside female 442 cm / 14'6" and male 470 cm / 15'5" Giants.
- Reusable static child assets for buckets, rope coils, hooks, wedges, mallets, and small clusters.
- Low-density clutter that explains rough camp maintenance without becoming a loot pile, crafting station, pickup set, or economy prop.
- Review composition rows that later art directors can use to judge density, silhouette, scale, and material discipline in documentation.

This package does not define usable workstations, tool pickup behavior, crafting recipes, resource nodes, economy data, loot tables, vendor data, inventory contents, interaction prompts, NPC work loops, encounter behavior, nav/pathfinding behavior, collision gameplay, startup-scene placement, material graph authoring, VFX, audio, DCC, FBX, Unreal Content, runtime source, or final visual approval.

## Silhouette Notes

Primary read: a Giant-scale camp utility kit with readable chunky silhouettes and large negative spaces between props. The kit should look useful to Blood Axe raiders without becoming a dense field of small tools.

Required silhouette reads:

- Tool buckets: oversized open buckets, battered carry tubs, iron-rimmed pails, and crude wood or hide-lined containers with a few visible large tool handles.
- Rope coils: thick coils and looped bundles sized for Giant hands, with broad rope forms and large knots rather than dense fiber detail.
- Hooks: heavy blackened iron S-hooks, wall hooks, tie-down hooks, and stake hooks with strong curved silhouettes.
- Wedges: blunt splitting wedges and chock blocks with broad triangular profiles, chipped edges, and stacked or scattered variants.
- Mallets: heavy wood and iron mallets with thick heads, long handles, and simple wrap bands.
- Camp utility clusters: small composed dressing groups that combine one or two buckets, a rope coil, hooks, wedges, mallets, and tie hardware in readable low clusters.
- Review composition rows: documentation-only rows for scale, spacing, LOD/collision planning, material discipline, and clutter-density approval.

Model the large bucket bodies, rims, handles, rope coil volumes, major knots, hook curves, wedge masses, mallet heads, handles, large tie rings, and cluster bases as geometry. Paint or normal-map rope fibers, wood grain, soot, scratches, dents, minor rivets, stitch lines, grime, chipped red paint, and small edge wear.

Avoid tiny scattered hand tools, human-scale pails, polished smithy gear, clean workshop organization, graphic gore, shiny treasure reads, UI-like markers, glowing interaction affordances, dense red decoration, or neutral/civilized Giant craft language.

## Scale Notes

Use the validated `SK_GIA_Base_A01` scale lock:

- Female Giant baseline: 442 cm / 14'6".
- Male Giant baseline: 470 cm / 15'5".
- Approved Giant ranges: females 14-15 ft / 427-457 cm; males 14'10"-16'0" / 452-488 cm.
- Author in centimeters. 1 Unreal unit = 1 cm.
- Normal humanoid compatibility is not required.

Suggested production scale targets:

- Tool buckets and tubs: 90-180 cm diameter, 80-160 cm tall, with handles readable beside Giant hands.
- Rope coils: 120-260 cm diameter, 25-70 cm coil thickness, with large knots or tie loops up to 55 cm.
- Heavy hooks: 70-180 cm long depending on wall, stake, or loose display use; hook thickness should read from MMO camera distance.
- Wedges and chocks: 50-140 cm long, 25-70 cm tall, broad enough to read as Giant tools.
- Mallets: 140-260 cm long overall, with heads 55-120 cm wide and 35-80 cm deep.
- Small utility clusters: 250-600 cm wide, 180-420 cm deep, 80-220 cm tall, kept low enough to sit near shelters, paths, and work areas without blocking main camp silhouettes.
- Larger composed camp utility rows: 600-1200 cm wide, 250-600 cm deep, split into child assets rather than one fixed all-purpose mesh.

Future DCC validation must compare child assets against the female 442 cm and male 470 cm Giant baselines before any Unreal placement or visual approval. Do not shrink this kit into ordinary humanoid camp props.

## Materials and Color Palette

Primary material language:

- Blackened iron, dark steel, and dull hammered metal for hooks, bucket rims, rings, wedge faces, mallet bands, and tie hardware.
- Scorched timber, raw wood, cracked handles, battered pail boards, and rough tool shafts.
- Thick rope, hide lashings, sinew ties, scorched leather wraps, and dirty carry straps.
- Dull Blood Axe red cloth ties, chipped red paint, and rough red warning marks as restrained sub-faction identifiers.
- Mud, soot, ash, charcoal dust, grime, oil-dark stains, and broad hand-painted wear.
- Sparse bone or horn spacers only as hostile accent pieces, never the main read.

Avoid neutral/civilized Giant blue-gray carved stone, refined cave-town craft, warm hearth colors, peaceful highland clan markers, and restrained blue rune or storm motifs. Default emissive is not planned. Forge glow, ritual glow, signal glow, magic marks, or active material states require a separate approval-gated package.

## Concept Image Prompt

Create an original stylized fantasy MMORPG concept image of `KIT_GIA_BloodAxeCampTools_A01` for the world of Aerathea. The design should emphasize oversized hostile Giant camp utility tools, battered tool buckets, thick rope coils, heavy blackened hooks, broad splitting wedges, massive mallets, camp utility clusters, scorched timber, dark steel, blackened iron, hide lashings, soot, mud, grime, dull Blood Axe red cloth ties, restrained chipped red paint, hostile raider camp identity, female Giant scale 442 cm / 14'6", male Giant scale 470 cm / 15'5", and a gameplay role as static non-interactive camp dressing. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, no default emissive glow, and MMO-friendly production design. Present it as a clean production asset board with front and side callouts, child split labels, scale rows, material swatches, LOD notes, collision notes, and review composition rows. Avoid copying any existing franchise, avoid graphic gore, avoid player interaction markers, avoid usable workstation behavior, avoid tool pickup behavior, avoid crafting/resource/economy diagrams, avoid making Blood Axe visual language the default Giant culture, and avoid excessive micro-detail that would not translate to mid-poly Unreal assets.

## Modeling Notes

This is a docs-only package. Future modeling should build reusable static child meshes and a few composed static clusters, not one collapsed clutter object.

- Tool buckets: model large open bucket forms, thick rims, battered side panels, carry handles, feet, and a few large visible tool handles. Use texture for small dents and scratches.
- Rope coils: model broad coil volumes with simplified turns, large knots, rope ends, and tie loops. Fine fibers, fray, and twist noise belong in textures and normals.
- Hooks: model heavy hook curves, tie rings, stake bases, wall plates, and broad hammered profiles. Keep hook counts sparse.
- Wedges: model blunt wedge masses, stacked variants, broad chipped corners, and large faces. Do not model tiny surface chips individually.
- Mallets: model large heads, long shafts, handle wraps, broad metal bands, and weighted ends. Use texture for wood grain, soot, and denting.
- Tie hardware: optional rings, pegs, spike anchors, short chain lengths, and latch plates can support clusters, but they must remain secondary.
- Camp utility clusters: compose low, path-safe dressing groups from buckets, rope, hooks, wedges, mallets, and tie hardware with clear spacing between shapes.
- Review rows: keep review composition as documentation planning only. Do not create a mesh, scene, validator, capture pass, or startup placement in this package.

Use real geometry for bucket bodies, bucket rims, major handles, coil masses, knots, hooks, wedge bodies, mallet heads, shafts, large rings, and cluster footprints. Use texture and normal detail for rope fiber, cloth weave, leather stitching, soot speckles, iron pitting, minor rivets, small scratches, chipped paint, wood grain, and mud splatter.

Do not add gameplay affordance meshes such as glow rings, pickup outlines, interaction icons, crafting plaques, recipe boards, harvest-node markers, economy tags, loot beams, UI arrows, destruction fracture lines, or workstation prompts.

## Texture and Material Notes

Required map set for future texture work:

- Base Color / Albedo (`BC`)
- Normal (`N`)
- Packed Occlusion/Roughness/Metallic (`ORM`)

No emissive map is planned for baseline `A01`.

Material slot plan:

- Slot 0: shared camp utility material for scorched wood, rope, hide, leather wraps, grime, soot, mud, and dull red cloth marks where atlasing is practical.
- Optional slot 1: `MI_GIA_BloodAxeReforgedMetal_A01` or related blackened metal material for hooks, rings, rims, wedge faces, bands, and chain accents.
- Optional slot 2: bucket or cluster variants only if metal, wood, and rope cannot remain readable in 1-2 slots.

Texture naming examples:

- `T_GIA_BloodAxeCampTools_A01_BC`
- `T_GIA_BloodAxeCampTools_A01_N`
- `T_GIA_BloodAxeCampTools_A01_ORM`
- `T_GIA_BloodAxeToolBuckets_A01_BC`
- `T_GIA_BloodAxeRopeCoils_A01_BC`
- `T_GIA_BloodAxeHooks_A01_BC`
- `T_GIA_BloodAxeWedges_A01_BC`
- `T_GIA_BloodAxeMallets_A01_BC`
- `T_GIA_BloodAxeCampUtilityCluster_A01_BC`

Use 512-1K texture sets for small repeated tools, 1K-2K for composed clusters, and 4K only if a later hero camp close-up specifically approves it. Keep Blood Axe red marks sparse enough that soot-black metal, wood, rope, and mud remain the primary read.

## Triangle Budget

Target LOD0 ranges:

- `SM_GIA_BloodAxeToolBucket_A01`: 1.2k-4k tris per bucket or tub variant.
- `SM_GIA_BloodAxeRopeCoil_A01`: 1.5k-5k tris per coil set, depending on visible coil turns and knots.
- `SM_GIA_BloodAxeHeavyHookSet_A01`: 800-3k tris per hook or small hook set.
- `SM_GIA_BloodAxeWedgeSet_A01`: 800-3k tris per wedge or small stacked set.
- `SM_GIA_BloodAxeMallet_A01`: 900-3k tris per mallet variant.
- `KIT_GIA_BloodAxeTieHardware_A01`: 1k-4k tris per ring, peg, hook, and short-chain set.
- `SM_GIA_BloodAxeCampUtilityCluster_A01`: 5k-14k tris per composed cluster built from reusable child assets.
- `SM_GIA_BloodAxeCampToolsReviewRow_A01`: docs-only planning row; no mesh budget until a later approved review task promotes it.
- Full composed kit preview, if later approved: target under 30k tris by reusing buckets, coils, hooks, wedges, mallets, and tie hardware.

Target material slots:

- Small child props: 1 material slot where practical.
- Buckets, rope coils, hooks, wedges, and mallets: 1-2 material slots.
- Composed utility clusters: 2 material slots target, 3 maximum only if necessary.
- Avoid unique material slots for individual scratches, knots, dents, fray, straps, rivets, red ties, or mud patches.

## LOD Plan

All important child meshes need LOD0-LOD3.

- LOD0: full bucket forms, coil silhouettes, major knots, hook curves, wedge profiles, mallet head/shaft mass, large rings, sparse red ties, and full cluster footprint.
- LOD1: 60-70 percent of LOD0; reduce minor bevels, secondary dents, duplicate tie loops, small handle cuts, extra coil turns, small ring subdivisions, and backside cluster detail.
- LOD2: 35-45 percent of LOD0; simplify bucket interiors, coil turn count, hook bevels, wedge chips, mallet wraps, small chain lengths, and cluster underside surfaces.
- LOD3: 15-25 percent of LOD0; preserve bucket silhouette, rope coil mass, hook curve read, wedge triangular read, mallet head read, cluster footprint, and Blood Axe red/black material blocks.

Remove tiny scratches, rope fiber, cloth weave, small stitch lines, minor rivets, pitting, soot speckles, fray, mud flecks, tiny dents, and small paint chips before reducing bucket bodies, coil mass, hooks, wedges, mallet heads, or cluster footprints.

## Collision Notes

Collision remains simple, static, and display-focused:

- Tool buckets and tubs: one low-count convex hull or grouped boxes around the bucket body; no collision on individual visible contents.
- Rope coils: one cylinder-like hull or simplified convex hull around the coil footprint; no per-rope or per-knot collision.
- Hooks: one simple box or convex hull around each loose hook or hook set; no sharp-point gameplay collision.
- Wedges: one box or wedge-like hull around each wedge set; no per-chip collision.
- Mallets: one box or capsule around the head/shaft display footprint; no weapon trace collision.
- Tie hardware: simplified boxes or capsules for large rings, pegs, or short chain bundles; no per-link collision.
- Camp utility clusters: grouped display collision around large shapes only, with walkable collision disabled unless a later environment task explicitly approves another use.

Do not add pickup collision, usable workstation volumes, crafting interaction volumes, resource triggers, economy triggers, inventory triggers, loot outlines, tool-pickup triggers, per-rope collision, per-hook collision, physics-simulated loose tools, nav blockers, encounter cover volumes, damage traces, trap volumes, destructible fracture collision, or startup placement collision.

## Animation Notes

Static mesh baseline. No animations, physics simulation, rope simulation, hanging secondary motion, tool swing, mallet use, hook operation, bucket carry state, material-state timing, NPC work cycle, tool pickup behavior, usable workstation behavior, crafting loop, resource collection state, economy presentation, loot state, interaction prompt, destruction state, VFX, audio, or startup-scene behavior is authored here.

Future approval-gated tasks may create separate active camp props, NPC work-loop dressing, physics-enabled rope, or destructible utility clutter if gameplay and performance rules are approved. Baseline `A01` remains inert static set dressing.

## Unreal Import Notes

These are planned import notes only. This task does not create Unreal assets or perform an Unreal import.

Planned asset types:

- Static Mesh children for tool buckets, rope coils, hook sets, wedge sets, mallets, tie hardware, camp utility clusters, and any future composed preview.
- Material Instances using shared Blood Axe camp material families.
- No Blueprint Actor, gameplay component, pickup item, crafting widget, workstation actor, economy data, inventory data, resource node, interaction volume, runtime source, validator, or startup-scene actor.

Planned folders:

- `/Game/Aerathea/Props/Giants/BloodAxeCamp/CampTools/`
- `/Game/Aerathea/Props/Giants/BloodAxeCamp/UtilityClusters/`
- `/Game/Aerathea/Materials/Giants/BloodAxe/`
- `/Game/Aerathea/Textures/Giants/BloodAxe/CampTools/`

Planned naming:

- `SM_GIA_BloodAxeToolBucket_A01`
- `SM_GIA_BloodAxeRopeCoil_A01`
- `SM_GIA_BloodAxeHeavyHookSet_A01`
- `SM_GIA_BloodAxeWedgeSet_A01`
- `SM_GIA_BloodAxeMallet_A01`
- `KIT_GIA_BloodAxeTieHardware_A01`
- `SM_GIA_BloodAxeCampUtilityCluster_A01`
- `SM_GIA_BloodAxeCampToolsReviewRow_A01`
- `MI_GIA_BloodAxeCampUtility_A01`
- `MI_GIA_BloodAxeRopeHide_A01`

Pivot planning:

- Tool buckets: ground center of bucket footprint, or handle-center only for explicitly documented loose display variants.
- Rope coils: ground center of coil footprint.
- Hook sets: base/contact center for loose display sets; wall or stake contact point for mounted visual variants.
- Wedges: ground contact center, aligned to the long axis.
- Mallets: ground contact or display base center; no weapon socket planning in this package.
- Tie hardware: base/contact center for pegs, rings, or bundled hardware.
- Camp utility clusters: ground center of the full cluster footprint.
- Review rows: documentation-only unless a later approved task creates non-shipping review meshes.

Import rules for any future build:

- Author in centimeters and import at scale 1.0.
- Assign LOD0-LOD3 for all important static meshes.
- Target 1-2 material slots per child mesh, 3 maximum for composed clusters.
- Keep collision simple and display-only.
- Validate visual scale against female 442 cm / 14'6" and male 470 cm / 15'5" Giant baselines before any promotion.
- Do not create Blueprint interaction, usable workstation behavior, tool pickup behavior, crafting/resource/economy rules, inventory data, loot data, nav behavior, startup placement, runtime source, source folders, copied concept art, or final visual approval artifacts.

## Folder and Naming Recommendation

- Docs folder: `docs/assets/kits/KIT_GIA_BloodAxeCampTools_A01/`
- Production package: `docs/assets/kits/KIT_GIA_BloodAxeCampTools_A01/PRODUCTION_PACKAGE.md`
- Child intake: `docs/assets/kits/KIT_GIA_BloodAxeCampTools_A01/CHILD_ASSET_INTAKE.md`

Future child package recommendations, if promoted by later tasks:

- `docs/assets/props/SM_GIA_BloodAxeToolBucket_A01/`
- `docs/assets/props/SM_GIA_BloodAxeRopeCoil_A01/`
- `docs/assets/props/SM_GIA_BloodAxeHeavyHookSet_A01/`
- `docs/assets/props/SM_GIA_BloodAxeWedgeSet_A01/`
- `docs/assets/props/SM_GIA_BloodAxeMallet_A01/`
- `docs/assets/kits/KIT_GIA_BloodAxeTieHardware_A01/`
- `docs/assets/props/SM_GIA_BloodAxeCampUtilityCluster_A01/`

Do not add SourceAssets, FBX exports, Unreal Content assets, runtime source, startup-scene actors, copied source concepts, global index entries, crafting data, resource data, economy data, loot definitions, interaction behavior, pickup behavior, workstation behavior, validators, material graphs, shaders, VFX, audio, or first DCC target selection from this task packet.

## Docs-Only Guardrails and Approval Gates

- Stop before any DCC source, sculpt, retopo, UV, bake, collision proxy, proof render, LOD source, FBX export, Unreal Content asset, material instance, texture asset, validator, runtime source, Blueprint, socket authoring, physics setup, animation asset, VFX, audio, or startup placement work.
- Stop before copying, moving, editing, embedding, inspecting for visual approval, or committing external source concepts.
- Stop before usable workstation behavior, tool pickup behavior, crafting behavior, resource behavior, economy behavior, salvage behavior, vendor behavior, inventory behavior, loot behavior, interaction behavior, quest behavior, NPC work loops, nav/pathfinding behavior, encounter behavior, cover behavior, damage behavior, destructible behavior, or objective logic.
- Stop before selecting a first DCC target.
- Stop before final visual approval claims.
- Stop if Blood Axe camp-tool dressing starts replacing neutral/civilized Giant culture.
- Stop if any row requires changing the validated Giant scale lock from female 442 cm / 14'6" and male 470 cm / 15'5".

## Quality Gate Checklist

- Blood Axe remains a hostile Giant sub-faction, separate from neutral/civilized Giant culture.
- Giant scale lock is explicit: female baseline 442 cm / 14'6" and male baseline 470 cm / 15'5", with approved ranges females 14-15 ft and males 14'10"-16'0".
- Child split covers tool buckets, rope coils, hooks, wedges, mallets, camp utility clusters, tie hardware, and review composition rows.
- Package is docs-only and changes no DCC, FBX, Unreal Content, runtime source, startup scene, external concept, validator, global index, task board, backlog, or bootstrap file.
- No usable workstation behavior, tool pickup behavior, crafting/resource/economy behavior, interaction behavior, startup placement, or first DCC target selection is authorized.
- Silhouettes are readable at MMO camera distance and scaled for Giant camp use.
- Materials use blackened iron, dark steel, scorched timber, thick rope, hide, leather, soot, mud, grime, dull red Blood Axe ties, chipped red paint, and sparse non-graphic bone or horn accents consistently.
- Neutral/civilized Giant cave-town, masonry, warm hearth, blue-rune, refined highland craft, and peaceful stoneworker language are excluded from the baseline.
- Default emissive, magic glow, forge heat glow, UI markers, quest markers, loot beams, and interaction affordances are absent and approval-gated.
- Tiny rope fibers, scratches, pitting, stitch lines, soot speckles, wood grain, mud flecks, small rivets, cloth weave, and chipped paint are assigned to texture or normal detail instead of geometry.
- Triangle budgets, texture maps, material slot targets, LOD0-LOD3, collision, animation scope, Unreal import planning, folder recommendations, docs-only guardrails, and approval gates are included.
