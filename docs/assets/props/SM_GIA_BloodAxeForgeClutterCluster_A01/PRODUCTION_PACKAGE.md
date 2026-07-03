# SM_GIA_BloodAxeForgeClutterCluster_A01 Production Package

## Art Direction Summary

- Asset name: `SM_GIA_BloodAxeForgeClutterCluster_A01`
- Asset type: Static Mesh prop production package, docs-only
- Parent kit: `KIT_GIA_BloodAxeAshSlagFirewood_A01`
- Child intake row: `BloodAxeForge.png#Review_Row_ComposedForgeClutter`
- Task: `AET-MA-20260629-446`
- Faction/theme: Blood Axe Tribe, hostile Giant sub-faction only
- Status: package-ready planning document; no DCC, Unreal Content, startup placement, final visual approval, or implementation target is authorized

`SM_GIA_BloodAxeForgeClutterCluster_A01` defines an optional composed static cluster of ash, cooled slag, charcoal, Giant-scale firewood, and scorched debris for later visual review of forge-adjacent clutter density. It is static and non-interactive. It must not merge sibling package ownership or become a forge hearth, anvil/quench station, scrap sorting station, cooking pit, path marker, barricade, crafting station, resource node, heat hazard, or gameplay target.

Blood Axe remains a hostile Giant sub-faction separate from neutral/civilized Giant culture. The cluster should read as dirty raider-camp residue around brutal field work: black ash, matte slag, charcoal, charred wood, split logs, blackened metal scraps, scorched hide, and restrained oxide red tags. Avoid neutral Giant civic masonry, blue-gray stoneworker craft, warm peaceful hearth identity, restrained blue runes, terrace/waterwork forms, or polished highland workshop language.

## Gameplay Purpose

The purpose is static environmental storytelling and composition planning. The cluster helps future reviewers judge whether ash, slag, charcoal, firewood, and scorched debris can coexist near a forge-adjacent space while staying subordinate to the forge hearth and anvil/quench silhouettes.

Allowed planning use:

- Test a static composed cluster of child clutter families around a future forge-adjacent edge.
- Show negative space and work-lane clearance without defining nav behavior.
- Verify that ash/slag/charcoal, firewood, and debris stay visually distinct.
- Preserve ownership boundaries for sibling packages.

Out of scope: forge hearth ownership changes, anvil/quench ownership changes, scrap sorting ownership changes, cooking pit ownership changes, path-marker or barricade ownership changes, crafting/resource/economy behavior, loot behavior, firewood pickups, slag harvesting, heat or damage behavior, destructible behavior, cover rules, interaction prompts, nav behavior, collision gameplay behavior, VFX, material graph authoring, DCC source, FBX export, Unreal Content, runtime source, validators, startup placement, final visual approval, or implementation target selection.

## Silhouette Notes

The cluster should be a low, heavy, irregular composition with readable category grouping rather than one collapsed pile. Ash and soot should make the ground mass, slag and charcoal should create dark chunky low forms, firewood should provide the strongest long-axis rhythm, and scorched debris should create broken edge punctuation.

Key silhouette targets:

- Ash/soot base: broad low mounds and dark ground residue.
- Slag/charcoal: matte chunky clumps and broken fuel pieces, grouped but not collectible.
- Firewood: Giant-scale logs and split trunks with strong length and thickness.
- Scorched debris: burned beam fragments, broken planks, sparse stakes, ash-stained stones, rare bent metal.
- Negative space: clear gaps around the cluster so it does not become a workstation, barricade, cover object, or navigation obstacle claim.
- Blood Axe accents: restrained red cloth or hide tags used sparingly.

Model real geometry for broad ash mounds, large slag/charcoal chunks, log bodies, split trunk planes, burned beams, broad stones, bent metal scraps, and large ties. Use textures and normals for soot speckles, ash dust, slag pores, bark grain, tiny nails, pitting, small cracks, cloth fibers, and surface scorch marks.

## Scale Notes

Use the validated `SK_GIA_Base_A01` Giant scale lock:

- Female Giant baseline: 442 cm / 14'6".
- Male Giant baseline: 470 cm / 15'5".
- Approved Giant ranges: females 14-15 ft / 427-457 cm; males 14'10"-16'0" / 452-488 cm.
- Author future source in centimeters. 1 Unreal unit = 1 cm.

Planning dimensions:

- Standard cluster footprint: 650-1300 cm wide, 350-850 cm deep, 90-260 cm high.
- Compact cluster footprint: 420-750 cm wide, 260-520 cm deep, 60-190 cm high.
- Firewood elements: 240-620 cm long and 30-95 cm thick.
- Ash/slag/charcoal low forms: 120-500 cm wide and 15-140 cm high.
- Scorched debris accents: 160-600 cm long and 30-180 cm high.

These dimensions are visual planning values only. They are not workstation extents, interaction ranges, resource pickup sizes, route widths, nav blockers, collision extents, cover metrics, damage radii, startup placement coordinates, or implementation approval.

## Materials and Color Palette

Primary material families:

- Ash and soot: matte gray residue, black dust, pale ash edges, strong roughness.
- Slag and charcoal: cooled black-gray clumps, dull iron crust, matte charcoal fractures.
- Firewood: dark bark, split raw interiors, smoke stains, charred ends.
- Scorched debris: burned timber, dull stone, blackened metal scraps, scorched hide, restrained oxide red cloth.

Palette targets:

- Soot black: `#0B0A09`, `#171412`, `#24201C`
- Ash gray: `#5F5B52`, `#80796C`, `#9A9386`, `#B5AA98`
- Cooled slag: `#141414`, `#2B2A27`, `#3A3C3F`, `#4B3021`
- Charcoal fracture: `#30302C`, `#45443D`, `#5B5A51`
- Charred bark: `#1D130F`, `#2C1C16`, `#3C261B`
- Split raw wood: `#6A4930`, `#815735`, `#A36C3A`
- Blood Axe red restraint: `#5F1513`, `#7A1C17`, `#8B211B`

Avoid active orange fire, glowing coals, heat shimmer, default emissive, bright resource colors, treasure metal, polished smithy materials, neutral/civilized Giant blue-gray civic stone, warm peaceful hearth language, and excessive red coverage.

## Concept Image Prompt

Create an original stylized fantasy MMORPG concept image of `SM_GIA_BloodAxeForgeClutterCluster_A01` for the world of Aerathea. The design should emphasize a static non-interactive hostile Blood Axe Giant forge-adjacent clutter cluster, broad ash and soot base, cooled slag chunks, matte charcoal heaps, Giant-scale firewood logs, scorched debris beams, rare blackened metal scraps, restrained oxide red cloth tags, clear negative space, female Giant scale 442 cm / 14'6", male Giant scale 470 cm / 15'5", sibling package boundary callouts, and a docs-only production planning role. Use hand-painted texture detail, readable silhouettes, baked-AO-style depth, normal-map-style surface detail, no emissive glow, and MMO-friendly mid-poly production design. Present it as a static mesh prop production sheet with three-quarter view, top footprint, category callouts, material swatches, LOD notes, texture map notes, and simple display collision guardrails. Avoid copying any existing franchise, avoid neutral/civilized Giant culture, avoid startup placement, avoid final visual approval, avoid forge hearth or anvil/quench ownership changes, avoid scrap sorting or cooking pit ownership changes, avoid crafting/resource/economy behavior, avoid firewood pickup or slag harvesting cues, avoid destructible or cover reads, avoid heat or damage hazard language, avoid DCC or Unreal implementation claims, and avoid excessive micro-detail.

## Modeling Notes

This is a docs-only modeling plan. It creates no DCC source, mesh, sculpt, retopo, UVs, bake, collision proxy, FBX, Unreal Content, material instance, Blueprint, validator, startup actor, source concept movement, final visual approval, shipped asset, or implementation target.

Future modeling priorities after separate approval:

- Compose the cluster from clear category groups instead of one dense clutter mound.
- Keep the cluster lower and visually subordinate to future forge hearth and anvil/quench silhouettes.
- Preserve negative space for visual readability without defining nav/pathfinding behavior.
- Use firewood logs as the main long-axis silhouette, with ash/slag/charcoal grounding and scorched debris edge punctuation.
- Keep blackened metal scraps rare so ownership does not drift into forge scrap sorting.
- Do not include hearth basins, anvils, quench troughs, cooling racks, cooking pit stones, sorted metal stock, path signs, barricade stakes, interaction handles, or resource markers.

Suggested future mesh groups:

- `ForgeClutterCluster_AshSootBase`
- `ForgeClutterCluster_SlagCharcoal`
- `ForgeClutterCluster_FirewoodLogs`
- `ForgeClutterCluster_ScorchedDebris`
- `ForgeClutterCluster_MetalClothAccents`

## Texture and Material Notes

Required future map set:

- Base Color / Albedo (`BC`)
- Normal (`N`)
- Packed Occlusion/Roughness/Metallic (`ORM`)

Future texture names if separately approved:

- `T_GIA_BloodAxeForgeClutterCluster_A01_BC`
- `T_GIA_BloodAxeForgeClutterCluster_A01_N`
- `T_GIA_BloodAxeForgeClutterCluster_A01_ORM`

Material slot plan:

- Slot 0: ash, soot, slag, charcoal, and dark residue.
- Slot 1: firewood, charred bark, split wood, and scorched timber.
- Slot 2: rare blackened metal scraps, hide ties, and restrained red cloth if not atlased into the first two slots.
- No emissive map is planned for baseline `A01`.

Target texture resolution: 1K-2K. Reuse child material language where possible. Use texture and normal detail for ash dust, soot speckles, slag pores, bark grain, tiny nail marks, pitting, cloth fibers, small cracks, and scorch marks rather than modeled micro-detail. Do not create material graphs, VFX materials, resource-state materials, heat-state materials, or implementation material instances from this package.

## Triangle Budget

Target LOD0: 6k-16k tris.

Suggested breakdown:

- Compact cluster: 6k-9k tris.
- Standard cluster: 9k-13k tris.
- Dense review cluster: 13k-16k tris.

Target material slots: 2-3, with 4 maximum only if a later approved material task requires it. Spend geometry on the ash footprint, log stack rhythm, chunky slag/charcoal forms, broad scorched beam accents, and readable cluster negative space. Do not spend geometry on ash grains, soot flecks, bark hairlines, tiny splinters, small nails, cloth fibers, pitting, or dense micro-debris.

## LOD Plan

All future static mesh implementation requires LOD0, LOD1, LOD2, and LOD3 before shipping use.

- LOD0: full category grouping, ash/soot base, slag/charcoal chunks, Giant-scale firewood logs, scorched debris, rare metal scraps, red cloth accents, and clear negative spaces.
- LOD1: 60-70 percent of LOD0; reduce small bevels, minor log cuts, secondary slag chips, charcoal top fragments, cloth edge nicks, and backside detail.
- LOD2: 35-45 percent of LOD0; merge small clumps, simplify log stack overlaps, reduce debris interiors, flatten underside detail, and remove non-silhouette metal scraps.
- LOD3: 15-25 percent of LOD0; preserve broad cluster footprint, ash/slag/charcoal/wood/debris category reads, Giant-scale log rhythm, and restrained Blood Axe accent only.

Reduction order:

1. Ash flecks, soot speckles, bark hairlines, slag pores, charcoal pores, pitting, tiny chips, and cloth fibers.
2. Small splinters, minor stones, nail marks, cloth edge nicks, and non-silhouette metal tabs.
3. Backside debris, underside faces, hidden log overlaps, and duplicate small fragments.
4. Secondary slag/charcoal clumps, log bevels, and beam-end notches.
5. Main footprint, log thickness, cluster category reads, and negative-space structure only after all smaller detail is removed.

## Collision Notes

This package creates no collision asset, collision proxy, Unreal collision setting, nav blocker, gameplay volume, trigger, damage volume, resource volume, cover volume, destructible setup, validator, startup placement collision, or collision correctness claim.

Future display collision guidance after separate approval:

- Collision disabled by default for purely decorative cluster review.
- Optional simple display collision may use two to four low-count boxes or convex hulls around the broad ash/log/debris masses if a later review task needs editor selection/display bounds.
- No per-log, per-lump, per-charcoal, per-splinter, per-stone, per-cloth, per-nail, or per-metal-scrap collision.
- No nav/pathfinding behavior, cover behavior, pickup collision, gatherable collision, resource triggers, heat hazard volumes, damage volumes, crafting interaction volumes, destructible collision, or gameplay collision behavior.

## Animation Notes

Baseline asset is static and non-interactive.

Not included: smoke, embers, sparks, heat shimmer, ash drift, material pulse, emissive state, physics simulation, rolling logs, destructible collapse, interaction, pickup state, resource state, crafting/economy behavior, nav behavior, cover behavior, startup behavior, DCC work, Unreal work, final visual approval, shipped content, or implementation target.

Any animated, destructible, gameplay-readable, pickup-readable, resource-readable, burning, smoking, heat, damage, or interaction variant requires a separate approved package.

## Unreal Import Notes

This section is planning only because the universal package format requires import notes. No Unreal Content asset, import script, material instance, texture asset, Blueprint, validator, startup actor, runtime source, DCC file, FBX export, final visual approval, shipped asset, or implementation target is created or authorized.

Potential future import identity after separate approval:

- Asset name: `SM_GIA_BloodAxeForgeClutterCluster_A01`
- Asset type: Static Mesh prop
- Candidate future folder: `/Game/Aerathea/Props/Giants/BloodAxeCamp/ForgeClutter/`
- Pivot: ground center of full cluster footprint.
- Scale: centimeter-authored source, import scale 1.0, preserving female 442 cm and male 470 cm Giant baselines.
- Collision: disabled by default; simple display hulls only if separately approved.
- LODs: LOD0-LOD3 required.
- Material slots: 2-3 target, 4 maximum only with later approval.
- Texture list: BC, N, ORM only by default.
- Sockets: none.
- Animation list: none.
- Blueprint behavior: none.

No startup placement, final visual approval, forge hearth/anvil/quench ownership change, scrap sorting ownership change, cooking pit ownership change, crafting/resource/economy behavior, firewood pickup behavior, slag harvesting, heat damage, nav behavior, cover behavior, destructible behavior, VFX component, material graph, runtime source, or shipped content is authorized.

## Folder and Naming Recommendation

Documentation path:

- `docs/assets/props/SM_GIA_BloodAxeForgeClutterCluster_A01/PRODUCTION_PACKAGE.md`

Potential future naming after separate approval:

- Mesh: `SM_GIA_BloodAxeForgeClutterCluster_A01`
- Textures: `T_GIA_BloodAxeForgeClutterCluster_A01_BC`, `T_GIA_BloodAxeForgeClutterCluster_A01_N`, `T_GIA_BloodAxeForgeClutterCluster_A01_ORM`
- Material instance: `MI_GIA_BloodAxeForgeClutterCluster_A01`

Sibling ownership boundaries:

- `SM_GIA_BloodAxeForgeHearth_A01` owns the main forge hearth, windbreak, basin, and forge focal silhouette.
- `SM_GIA_BloodAxeAnvilQuench_A01` owns the anvil block, quench trough, slag tray, cooling rack, and workstation-adjacent silhouette.
- `KIT_GIA_BloodAxeForgeScrapSorting_A01` owns organized metal stock, bins, broken weapon bundles, and sorted scrap rows.
- `SM_GIA_BloodAxeCookingPit_A01` owns cooking pit composition.
- This cluster owns only static ash, slag, charcoal, firewood, and scorched debris composition planning.

Do not add SourceAssets, FBX exports, Unreal Content, Tools/DCC, Tools/Unreal, runtime source, validators, captures, global index edits, task board edits, material graphs, VFX, startup scene files, forge hearth edits, anvil/quench edits, scrap sorting edits, cooking pit edits, or sibling package ownership changes from this package.

## Quality Gate Checklist

- Uses the universal 15-section Aerathea package format.
- Keeps Blood Axe as a hostile Giant sub-faction separate from neutral/civilized Giant culture.
- Preserves female Giant 442 cm / 14'6" and male Giant 470 cm / 15'5" scale lock.
- Defines a static non-interactive forge clutter cluster, not a forge hearth, anvil/quench station, scrap sorting station, cooking pit, path marker, barricade, crafting station, resource node, heat hazard, cover object, destructible object, or gameplay target.
- Preserves sibling package ownership and does not merge forge hearth, anvil/quench, scrap sorting, cooking pit, path marker, barricade, or shelter content.
- Excludes crafting/resource/economy behavior, firewood pickup behavior, slag harvesting, loot behavior, destructible behavior, cover rules, heat/damage behavior, interaction behavior, VFX, material graph authoring, nav behavior, and gameplay collision behavior.
- Uses mid-poly MMO budgets, LOD0-LOD3, texture map planning, simple display collision guidance, and Unreal planning notes without implementation claims.
- Assigns tiny soot, ash, bark, pitting, nails, scratches, cloth fibers, slag pores, charcoal pores, and cracks to textures or normals rather than geometry.
- Makes no DCC, FBX, Unreal Content, runtime source, material graph, VFX, validator, startup placement, final approval, first DCC target, source concept movement, global index edit, or task board edit claim.
