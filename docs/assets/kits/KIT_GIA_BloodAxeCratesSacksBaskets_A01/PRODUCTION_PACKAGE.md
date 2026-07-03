# KIT_GIA_BloodAxeCratesSacksBaskets_A01 Production Package

## Art Direction Summary

- Asset name: `KIT_GIA_BloodAxeCratesSacksBaskets_A01`
- Asset type: Production kit / static hostile Giant camp storage clutter split
- Parent planning kit: `KIT_GIA_BloodAxeCamp_A01`
- Source planning row: `BloodAxeCamp.png#Clutter_CratesSacksBaskets`
- Related packages: `KIT_GIA_BloodAxeCamp_A01`, `KIT_GIA_BloodAxeCampShelters_A01`, `KIT_GIA_BloodAxeForgeScrapSorting_A01`, `KIT_GIA_BloodAxePathMarkers_A01`, and `KIT_GIA_BloodAxeBannerLine_A01`
- Faction/theme: Blood Axe Tribe, hostile Giant sub-faction only
- Status: docs-only production package ready
- Scope guardrail: planning only; no DCC, FBX, Unreal Content, runtime source, external source concepts, loot tables, resource/economy/vendor behavior, inventory behavior, interaction behavior, destructible behavior, startup placement, final visual approval, or first DCC target selection.

`KIT_GIA_BloodAxeCratesSacksBaskets_A01` defines inert Giant-scale storage clutter for hostile Blood Axe camps: oversized rough crates, heavy sacks, woven baskets, rope bindings, hide-covered bundles, stacked storage clusters, and non-shipping review composition rows. The kit should read as brutal camp utility dressing from MMO camera distance, not as player-facing loot, vendor stock, gatherable resources, or inventory containers.

Blood Axe identity must remain separate from neutral/civilized Giant culture. These props belong to raider camps with crude timber, blackened iron straps, rough hide, heavy rope, dirty canvas, oxide red warning marks, soot, mud, and stolen field materials. They must not use civilized Giant blue-gray masonry, warm hearth presentation, refined cave-town storage, terrace craft language, restrained blue runes, or peaceful highland settlement identity.

## Gameplay Purpose

The kit supports non-interactive environmental storytelling and scale readability in Blood Axe camp spaces. It explains how hostile Giant raiders store supplies, hides, field bundles, tools, and rough goods without creating gameplay systems.

Allowed planning uses:

- Dress shelter edges, forge approaches, gate interiors, camp paths, watch-platform bases, and stronghold approach laydowns with Giant-scale storage clutter.
- Provide visual weight beside female 442 cm / 14'6" and male 470 cm / 15'5" Giant baselines.
- Break up broad camp ground planes with readable low and mid-height shapes that do not compete with gates, shelters, banners, or watch towers.
- Support future level-art composition with reusable static child meshes and optional composed clusters.
- Show storage density and camp utility without implying loot, resource, vendor, inventory, pickup, interaction, or destructible behavior.

Out of scope:

- Loot tables, loot containers, reward chests, pickups, inventory behavior, storage UI, vendor/economy behavior, resource nodes, gatherable supplies, crafting stations, workstation behavior, salvage systems, cooking systems, destructible crates, physics breakage, interaction prompts, AI cover, nav/pathfinding behavior, encounter scripting, startup placement, DCC source creation, FBX export, Unreal Content creation, material graph work, runtime source, validators, source concept movement, and final visual approval.

## Silhouette Notes

Primary read:

- A low-to-mid-height, heavy, practical storage kit made for hostile Giants, with big readable masses rather than many tiny camp objects.
- Oversized crates should be squat and rough, with thick planks, broad blackened iron straps, rope lashings, and blunt corner protection.
- Sacks should sag heavily, with broad tied necks, patched fabric, hide reinforcement, and dirt-weighted bases.
- Baskets should be giant woven utility containers using large reed, split timber, rawhide strips, or rope weave, with simplified broad weave geometry.
- Rope bindings should read as heavy lashings, coils, tied bundle bands, and thick tension wraps, not fine decorative twine.
- Covered bundles should use hide, canvas, or coarse cloth tarps pulled over bulky contents, with a few large folds and tie-down points.
- Stacked clusters should combine crates, sacks, baskets, and covered bundles into readable triangular or stepped piles for camp corners and shelter edges.
- Review composition rows should remain non-shipping planning rows, visually distinct from final assets.

Model as real geometry when promoted later:

- Crate bodies, major planks, broad lids, large hinges or straps, corner caps, large rope coils, major knots, sack volumes, tied necks, basket rims, large weave ribs, bundle tarp silhouettes, tie-down bands, pallet skids, and cluster footprints.

Keep in textures or normal maps:

- Wood grain, small chips, minor cracks, rope fibers, canvas weave, sack stitching, hide pores, dirt speckles, soot stains, faded red paint chips, tiny nails, small scratches, and fine basket fibers.

Avoid:

- Treasure chest silhouettes, glowing interaction markers, lock icons, readable labels, UI-like arrows, human-scale picnic baskets, refined market crates, neutral Giant civic storage, cozy hearth supplies, shiny loot piles, tiny clutter scatter, dense rivets, excessive scratches, graphic gore, or overuse of red.

## Scale Notes

Use the validated `SK_GIA_Base_A01` scale lock:

- Female Giant baseline: 442 cm / 14'6".
- Male Giant baseline: 470 cm / 15'5".
- Approved Giant ranges: females 14-15 ft / 427-457 cm; males 14'10"-16'0" / 452-488 cm.
- Author all future source in centimeters. 1 Unreal unit = 1 cm.
- Normal humanoid compatibility is not required.

Planning dimensions:

- Oversized crate small variant: 180-320 cm wide, 130-240 cm deep, 100-190 cm high.
- Oversized crate large variant: 300-520 cm wide, 220-380 cm deep, 160-280 cm high.
- Heavy sack single: 120-240 cm wide, 90-190 cm deep, 120-260 cm high, with tied necks large enough to read from camera distance.
- Sack group: 280-650 cm footprint, 100-260 cm high, using three to seven broad masses.
- Woven basket: 140-320 cm diameter or width, 120-260 cm high, with thick rim and simplified weave.
- Rope binding set: 80-260 cm coil or bundle footprint, 25-90 cm high, with rope diameter exaggerated enough for Giant use.
- Covered bundle: 220-520 cm long, 140-360 cm deep, 90-230 cm high.
- Stacked storage cluster: 450-1100 cm footprint, 180-430 cm high, preserving clear ground contact and avoiding tower-like instability.
- Review composition rows: include 442 cm and 470 cm Giant references beside storage variants for later scale checks.

Future DCC validation must compare every child asset against the female 442 cm and male 470 cm Giant baselines before any Unreal import, placement, or visual approval.

## Materials and Color Palette

Primary materials:

- Rough dark timber, split planks, scavenged crate boards, scorched wood, and mud-dark pallet skids.
- Blackened iron, dark steel straps, dull corner caps, broad hinge plates, and worn metal rims.
- Heavy rope, rawhide lashings, sinew cord, dirty leather ties, and coarse fiber wraps.
- Burlap, canvas, rough sackcloth, patched hide, dirty cloth covers, and fur-lined bundle edges used sparingly.
- Giant woven basket material: thick reeds, split timber strips, rope weave, rawhide bands, and mud-dark base wear.
- Soot, ash, dried mud, charcoal dust, grime, grease, and weather staining.
- Oxide red cloth tabs, faded red paint, and crude Blood Axe marks used as restrained faction accents.

Palette targets:

- Rough timber: `#2A1A10` to `#5C3A22`
- Blackened iron: `#121315` to `#333538`
- Rope and rawhide: `#6B5435` to `#A98B5B`
- Sackcloth and canvas: `#6D604C` to `#A89973`
- Dirty hide: `#3A2417` to `#77543A`
- Basket reed and split timber: `#6A4B2B` to `#B08A52`
- Blood Axe red accents: `#5F1513` to `#8B211B`
- Soot, ash, and mud: `#0B0A09` to `#4B4032`

Avoid neutral/civilized Giant default language: no blue-gray carved masonry, polished cave-town storage, refined stoneworker joinery, warm hearth symbols, terrace-market craft, highland civic markings, restrained blue runes, or peaceful settlement color language.

No default emissive is approved. Ritual glow, magic markings, signal lamps, hot forge states, or VFX pulses require a separate approval gate and are not part of baseline `A01`.

## Concept Image Prompt

Create an original stylized fantasy MMORPG production asset board of `KIT_GIA_BloodAxeCratesSacksBaskets_A01` for the world of Aerathea. The design should emphasize inert Blood Axe Giant camp storage clutter, oversized rough crates, heavy sacks, woven baskets, thick rope bindings, hide-covered bundles, dirty canvas covers, stacked storage clusters, scorched timber, blackened iron straps, rawhide lashings, burlap, mud, soot, oxide red warning marks, hostile Giant sub-faction identity, separation from neutral/civilized Giant culture, and the gameplay role of non-interactive environmental dressing. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, no default emissive glow, and MMO-friendly mid-poly production design. Present it as a clean asset board with child asset callouts, material swatches, LOD/collision notes, scale markers beside a female 442 cm / 14'6" Giant and a male 470 cm / 15'5" Giant, plus review composition rows for stacked storage readability. Avoid copying any existing franchise, avoid making Blood Axe storage language the default Giant culture, avoid neutral Giant cave-town architecture, avoid treasure chest or loot readability, avoid vendor stall presentation, avoid inventory or pickup markers, avoid destructible crate language, avoid readable text labels, avoid graphic gore, and avoid excessive micro-detail that would not translate to mid-poly Unreal assets.

## Modeling Notes

This is a docs-only modeling plan. No DCC source, sculpt, retopo, UV, bake, proof render, FBX export, Unreal asset, collision proxy, validator, runtime source, startup actor, material graph, or final visual approval is created or authorized by this package.

Future modeling should prioritize separate reusable modules:

- Oversized rough crates with thick planks, broad lids, heavy straps, large hinges, rope lashings, and blunt corner caps.
- Crate variants that avoid treasure chest readability: open-top utility crate, lidless supply crate, broken-rim crate, half-covered crate, and flat stacked crate.
- Heavy sacks with big sagging forms, tied necks, patched cloth, dirt-weighted bases, and readable cloth folds.
- Sack groups with a few large masses instead of many small grain bags.
- Woven baskets with thick rims, simplified broad weave ribs, reinforced bases, and large side handles or rope loops only when they affect silhouette.
- Rope binding sets with large coils, heavy knots, crossed tie-downs, bundle bands, and ground coils scaled for Giants.
- Covered bundles with broad hide or canvas covers, clear tie-down bands, large folds, and bulky silhouettes under the cover.
- Stacked clusters that combine the child types into stable triangular or stepped piles for shelter edges, forge outskirts, gate interiors, and camp paths.
- Review composition rows as simplified non-shipping layout studies, visually distinct from final meshes.

Use real geometry for major structure, silhouette-defining folds, large lashings, broad basket ribs, thick rims, large knots, straps, and tie-down bands. Use textures and normals for fine weave, fibers, wood grain, small chips, dirt speckles, stitching, small scratches, minor cracks, and paint wear.

Do not create gameplay affordances such as glowing outlines, pickup handles, loot lids, lock mechanisms, vendor tags, inventory labels, interaction rings, breakage seams, fracture cuts, reward glints, resource-node crystals, crafting symbols, workstation indicators, UI plaques, or quest markers.

## Texture and Material Notes

Target material strategy:

- Keep most small and medium children to 1 material slot.
- Use 2 material slots for crates and covered bundles where hard materials and cloth/hide need clean separation.
- Use 2-3 material slots for composed clusters only when crate wood/metal, sack cloth, and basket/rope materials must remain reusable.
- Avoid unique material slots for each plank, sack patch, rope tie, basket strip, dirt patch, red mark, or metal strap.

Suggested future material instances:

- `MI_GIA_BloodAxeStorageWood_A01`
- `MI_GIA_BloodAxeStorageClothHide_A01`
- `MI_GIA_BloodAxeStorageRopeRawhide_A01`
- `MI_GIA_BloodAxeStorageBasketWeave_A01`
- `MI_GIA_BloodAxeStorageBlackIron_A01`
- `MI_GIA_BloodAxeStorageSootMud_A01`
- `MI_GIA_BloodAxeStorageReview_A01` for non-shipping review rows only

Required map set for future texture work:

- Base Color / Albedo (`BC`)
- Normal (`N`)
- Packed Occlusion/Roughness/Metallic (`ORM`)

No emissive map is planned for baseline `A01`.

Texture naming examples:

- `T_GIA_BloodAxeStorageCrates_A01_BC`
- `T_GIA_BloodAxeStorageCrates_A01_N`
- `T_GIA_BloodAxeStorageCrates_A01_ORM`
- `T_GIA_BloodAxeStorageSacks_A01_BC`
- `T_GIA_BloodAxeStorageBaskets_A01_BC`
- `T_GIA_BloodAxeRopeBindings_A01_BC`
- `T_GIA_BloodAxeCoveredBundles_A01_BC`
- `T_GIA_BloodAxeStorageClusters_A01_BC`

Texture set targets:

- Small child props and rope sets: 512-1K.
- Crates, sacks, baskets, and covered bundles: 1K-2K.
- Stacked clusters: 2K shared atlas where practical.
- 4K only if a later hero camp review explicitly approves close-up use.

Packed `ORM` guidance:

- R: Ambient occlusion under crate lids, sack folds, basket rims, rope overlaps, lashing contacts, bundle covers, and stack contact points.
- G: High roughness for wood, rope, cloth, hide, basket weave, soot, ash, and mud; medium-high varied roughness for blackened iron.
- B: Metallic only for iron straps, hinge plates, corner caps, rings, and dull hardware.

## Triangle Budget

Suggested LOD0 budgets for future approved children:

- `SM_GIA_BloodAxeOversizedCrate_A01`: 2k-7k tris, 1-2 materials.
- `SM_GIA_BloodAxeHeavySack_A01`: 1k-4k tris, 1 material.
- `KIT_GIA_BloodAxeSackGroup_A01`: 3k-10k tris, 1-2 materials.
- `SM_GIA_BloodAxeWovenBasket_A01`: 2k-6k tris, 1-2 materials.
- `KIT_GIA_BloodAxeRopeBindings_A01`: 1k-5k tris per reusable set, 1 material.
- `SM_GIA_BloodAxeCoveredBundle_A01`: 2k-7k tris, 1-2 materials.
- `KIT_GIA_BloodAxeStorageStackCluster_A01`: 8k-28k tris using repeated children and shared materials.
- `DOC_GIA_BloodAxeStorageReviewRows_A01`: docs-only planning row; no shipping triangle budget until a later implementation task defines a review mesh.

Spend triangles on broad crate profiles, heavy lids, large straps, sack mass, tied necks, basket rims, large weave ribs, rope knots, covered-bundle folds, and cluster silhouette. Do not spend triangles on dense nails, tiny rope fibers, small weave threads, fine wood grain, many little scratches, small dirt flecks, tiny cloth fray, or miniature labels.

## LOD Plan

All important future static meshes require LOD0-LOD3.

- LOD0: full crate forms, sack volumes, basket rims and major ribs, large rope coils and knots, covered-bundle folds, stacked-cluster silhouette, Blood Axe red accents, and broad material zones.
- LOD1: 60-70 percent of LOD0; reduce small bevels, minor straps, secondary folds, small lashing loops, underside detail, and duplicate loose pieces.
- LOD2: 35-45 percent of LOD0; preserve crate/sack/basket/bundle read, major stack footprint, large red accent blocks, and Giant-scale storage mass while simplifying interiors and back-facing detail.
- LOD3: 15-25 percent of LOD0; preserve broad storage silhouettes, ground footprint, and stacked cluster rhythm. Remove most small hardware, rope segments, weave cuts, sack folds, and red micro-marks.

Reduction order:

1. Tiny scratches, nail heads, small chips, dirt flecks, cloth fray, weave fibers, rope fibers, and paint chips.
2. Secondary rope wraps, small knots, minor sack folds, underside struts, and small loose scraps.
3. Minor crate plank splits, small metal tabs, small basket ribs, and extra tie-down tails.
4. Interior/backside detail, hidden contact faces, and non-visible cluster occlusion surfaces.
5. Small accent props and redundant stacked filler shapes.
6. Non-shipping review-row helper detail.

Never reduce the Giant-scale storage read, hostile Blood Axe red/black identity, crate/sack/basket/bundle silhouette, or stacked-cluster footprint before removing small detail.

## Collision Notes

Collision is planning only in this package. Do not create collision proxies, UCX meshes, physics bodies, nav rules, destructible chunks, interaction volumes, or startup placement from this task.

Future collision guidance:

- Oversized crates: one to three simple boxes or low-count convex hulls around the major crate mass; no per-plank collision.
- Heavy sacks: one capsule, box, or simplified convex hull around the sagging mass; no cloth collision.
- Sack groups: grouped low-count hulls around the combined footprint; no per-sack micro-collision unless a later layout task requires it.
- Woven baskets: simple cylinder, box, or convex hull around the outer basket body; no per-weave collision.
- Rope binding sets: collision disabled by default unless used as large blocking dressing; no per-rope collision.
- Covered bundles: one simplified hull around the covered shape; no tarp, tie, or hidden-content collision.
- Stacked clusters: simple grouped display collision around the full footprint and major high points only.
- Review composition rows: collision disabled by default and treated as non-shipping planning rows.

Do not add pickup collision, loot interaction volumes, inventory triggers, vendor triggers, crafting/resource triggers, workstation triggers, destructible fracture collision, physics-simulated crate lids, cloth simulation, per-rope collision, per-basket-rib collision, per-plank collision, navmesh policy, combat cover tagging, damage volumes, or encounter blockers.

## Animation Notes

Baseline kit is static.

Allowed planning:

- Static mesh children with fixed crate, sack, basket, rope, covered-bundle, and stack silhouettes.
- Static material variation for dirt, soot, faded red marks, wet mud, old canvas, and rope color if approved later.
- Non-shipping static review composition rows for future visual comparison.

Not approved here:

- Cloth simulation, dangling rope physics, lid opening, sack settling, basket wobble, physics breakage, destructible collapse, runtime animation, skeletal variants, material-state gameplay, VFX pulses, audio cues, pickup states, inventory states, vendor states, loot states, resource collection states, workstation states, AI behavior, interaction behavior, or startup placement.

## Unreal Import Notes

These are planned import notes only. This task does not create Unreal assets or perform an Unreal import.

Planned asset types:

- Static Mesh children for oversized crates, heavy sacks, sack groups, woven baskets, rope binding sets, covered bundles, stacked storage clusters, and optional non-shipping review rows.
- Optional kit-level composed Static Mesh preview only after a later approved implementation task.
- No Blueprint Actor, UI, VFX, skeletal mesh, runtime source, material graph, or startup-scene actor is created or authorized here.

Planned folder paths:

- `/Game/Aerathea/Props/Giants/BloodAxeCamp/Storage/`
- `/Game/Aerathea/Materials/Giants/BloodAxe/Storage/`

Planned naming:

- `SM_GIA_BloodAxeOversizedCrate_A01`
- `SM_GIA_BloodAxeOversizedCrate_A02`
- `SM_GIA_BloodAxeHeavySack_A01`
- `KIT_GIA_BloodAxeSackGroup_A01`
- `SM_GIA_BloodAxeWovenBasket_A01`
- `KIT_GIA_BloodAxeRopeBindings_A01`
- `SM_GIA_BloodAxeCoveredBundle_A01`
- `KIT_GIA_BloodAxeStorageStackCluster_A01`
- `DOC_GIA_BloodAxeStorageReviewRows_A01`

Pivot planning:

- Crates: ground center of crate footprint, aligned to longest side.
- Sacks: ground contact center of sagging mass.
- Sack groups: ground center of combined footprint.
- Baskets: base center, vertical axis through basket body.
- Rope binding sets: ground center or coil center depending on use.
- Covered bundles: ground center of bundle footprint, aligned to longest axis.
- Stacked clusters: ground center of full cluster footprint.
- Review rows: docs-only planning; no import pivot until a later implementation task.

Scale:

- Author in centimeters and import at scale 1.0.
- Validate against female 442 cm / 14'6" and male 470 cm / 15'5" Giant baselines before any placement.

Collision type:

- Simple static display collision only when needed.
- Default collision disabled for small rope sets and review rows.
- No interaction, loot, inventory, vendor, resource, destructible, nav/pathfinding, or gameplay collision is defined.

LOD plan:

- Assign LOD0-LOD3 for all important static meshes.
- Preserve primary storage silhouettes and reduce small detail first.

Material slot count:

- Target 1 material slot for simple props.
- Target 1-2 material slots for crates, sacks, baskets, rope sets, and covered bundles.
- Target 2-3 material slots maximum for composed clusters.

Texture list:

- `T_GIA_BloodAxeStorageCrates_A01_BC`
- `T_GIA_BloodAxeStorageCrates_A01_N`
- `T_GIA_BloodAxeStorageCrates_A01_ORM`
- `T_GIA_BloodAxeStorageSacks_A01_BC`
- `T_GIA_BloodAxeStorageSacks_A01_N`
- `T_GIA_BloodAxeStorageSacks_A01_ORM`
- `T_GIA_BloodAxeStorageBaskets_A01_BC`
- `T_GIA_BloodAxeStorageBaskets_A01_N`
- `T_GIA_BloodAxeStorageBaskets_A01_ORM`
- `T_GIA_BloodAxeRopeBindings_A01_BC`
- `T_GIA_BloodAxeRopeBindings_A01_N`
- `T_GIA_BloodAxeRopeBindings_A01_ORM`
- `T_GIA_BloodAxeCoveredBundles_A01_BC`
- `T_GIA_BloodAxeCoveredBundles_A01_N`
- `T_GIA_BloodAxeCoveredBundles_A01_ORM`

Sockets:

- None planned for baseline static storage clutter.

Blueprint behavior:

- None. Do not create container, pickup, vendor, crafting, resource, interaction, inventory, destruction, or runtime behavior from this package.

Performance notes:

- Favor instanced repeated children and shared material atlases.
- Keep composed clusters under 3 material slots.
- Use simple collision and aggressive LODs for repeated camp clutter.
- Do not make many small unique variants when material tint, rotation, and scale variation can provide layout variety after implementation approval.

## Folder and Naming Recommendation

- Docs folder: `docs/assets/kits/KIT_GIA_BloodAxeCratesSacksBaskets_A01/`
- Production package: `docs/assets/kits/KIT_GIA_BloodAxeCratesSacksBaskets_A01/PRODUCTION_PACKAGE.md`
- Child intake: `docs/assets/kits/KIT_GIA_BloodAxeCratesSacksBaskets_A01/CHILD_ASSET_INTAKE.md`

Future child package recommendations, if promoted by later tasks:

- `docs/assets/props/SM_GIA_BloodAxeOversizedCrate_A01/`
- `docs/assets/props/SM_GIA_BloodAxeOversizedCrate_A02/`
- `docs/assets/props/SM_GIA_BloodAxeHeavySack_A01/`
- `docs/assets/kits/KIT_GIA_BloodAxeSackGroup_A01/`
- `docs/assets/props/SM_GIA_BloodAxeWovenBasket_A01/`
- `docs/assets/kits/KIT_GIA_BloodAxeRopeBindings_A01/`
- `docs/assets/props/SM_GIA_BloodAxeCoveredBundle_A01/`
- `docs/assets/kits/KIT_GIA_BloodAxeStorageStackCluster_A01/`

Do not add SourceAssets, FBX exports, Unreal Content assets, runtime source, startup-scene actors, copied source concepts, global index entries, task board updates, backlog updates, bootstrap updates, crafting data, economy data, resource behavior, loot definitions, inventory behavior, vendor behavior, destructible components, material graphs, shaders, validators, or pickup interactions from this task packet.

## Quality Gate Checklist

- Package is docs-only and changes no DCC, FBX, Unreal Content, runtime source, startup scene, external concept, validator, global index, task board, backlog, or bootstrap file.
- Universal sections are present: art direction, gameplay purpose, silhouette, scale, materials, concept prompt, modeling, texture/material, triangle budget, LOD, collision, animation, Unreal import notes, folder/naming, and quality gate.
- Child planning covers oversized crates, sacks, baskets, rope bindings, covered bundles, stacked clusters, and review composition rows.
- Blood Axe remains a hostile Giant sub-faction, separate from neutral/civilized Giant culture.
- Giant scale lock is explicit: female 442 cm / 14'6" and male 470 cm / 15'5".
- Storage clutter is static environmental dressing, not loot, reward, resource, vendor, economy, inventory, pickup, crafting, workstation, interaction, destructible, AI, combat, nav/pathfinding, or startup behavior.
- Silhouettes are readable at MMO camera distance and sized for Giant camps.
- Materials use rough timber, blackened iron, rope, hide, sackcloth, basket weave, soot, ash, mud, and restrained oxide red Blood Axe accents.
- Default emissive, ritual glow, shamanic glow, signal glow, UI markers, readable labels, treasure chest language, and neutral/civilized Giant language are absent and approval-gated.
- Fine wood grain, rope fibers, weave threads, cloth fibers, scratches, chips, small nails, stitching, and dirt speckles are assigned to textures or normal maps rather than modeled micro-detail.
- LOD0-LOD3 guidance preserves primary storage silhouette before removing small detail.
- Collision guidance is simple, static, display-focused, and avoids gameplay volumes.
- No first DCC target is selected.
