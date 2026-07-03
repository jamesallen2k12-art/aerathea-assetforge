# KIT_GIA_BloodAxePathMarkerCluster_A01 Production Package

## 1. Art Direction Summary

- Asset name: `KIT_GIA_BloodAxePathMarkerCluster_A01`
- Asset type: Docs-only production package for a composed static visual marker cluster
- Parent kit: `KIT_GIA_BloodAxePathMarkers_A01`
- Source planning row: `Blood Axe Village.png#PathMarkers_MixedCluster_A01`
- Task ID: `AET-MA-20260629-366`
- Faction/theme: Blood Axe Tribe, hostile Giant sub-faction only
- Package status: production direction ready, docs-only

`KIT_GIA_BloodAxePathMarkerCluster_A01` defines a compact Blood Axe path-marker composition made from one cairn, one cloth stake, one horn/bone marker, one broken shield accent, and one ash-stained base. The cluster should read as crude hostile Giant route dressing from MMO camera distance: a rough cairn anchors the mass, a scorched stake lifts the silhouette, a blunt horn or old bone adds warning identity, a broken shield fragment adds raider violence, and ash-stained ground ties the group into burned camp terrain.

Blood Axe culture is a hostile Giant sub-faction and must remain visually separate from neutral/civilized Giant culture. This package must not become default Giant wayfinding, cave-town masonry language, civic stoneworker culture, highland nomad trail marking, warm hearth settlement dressing, refined blue-gray carved stone, or restrained blue-rune route language.

This is a docs-only package. It does not create or authorize a review actor, implementation task, objective cluster, route scripting, encounter setup, DCC work, Unreal work, startup placement, final approval, implementation target, Hermes work, external source concept edits, global index edits, runtime source edits, or any asset file outside this document.

## 2. Gameplay Purpose

The cluster supports static visual readability for Blood Axe camp approaches, path bends, trampled ground edges, and hostile threshold dressing. It tells the player that a path belongs to the Blood Axe raider sub-faction through shape, material, and placement language, not through interactive systems.

Allowed purpose:

- Provide a low-to-mid-height visual beat that combines stone, cloth, horn/bone, shield scrap, and ash in one reusable composition.
- Break up large dirt or ash ground planes with a Giant-scale cluster that feels placed by raiders, not by civilized masons.
- Reinforce hostile Blood Axe territory at camp paths, shelter approaches, forge-adjacent trails, and stronghold approach bends.
- Complement larger Blood Axe gates, palisades, banner lines, shelters, scrap piles, and cairn guideposts without replacing those packages.
- Serve as a future visual planning reference for composition, scale, materials, LOD expectations, and collision limits.

Out of scope:

- No review actor, implementation task, objective cluster, route scripting, encounter setup, DCC, Unreal, startup, final approval, implementation target, or Hermes work.
- No waypoint behavior, trail-marker gameplay, nav/pathfinding helper, quest marker, UI arrow, patrol marker, spawn marker, combat cover, pickup, loot, salvage, crafting resource, damage field, aura volume, faction buff, morale system, AI behavior, audio cue, VFX pulse, destructible state, or interaction prompt.

## 3. Silhouette Notes

Primary silhouette:

- One chunky cairn forms the heavy base read, using three to six large field stones rather than many small pebbles.
- One scorched cloth stake rises above the cairn and shield accent, with a broad torn oxide red strip visible at distance.
- One horn/bone marker sits lashed to the stake or wedged into the cairn side, creating an asymmetrical warning prong without graphic gore.
- One broken shield accent leans or jams into the lower cluster, with a large readable shield rim, split plank, or dull blackened plate.
- One ash-stained base spreads below all pieces as a low irregular footprint of soot, charcoal, trampled mud, and burned grass.

Composition rules:

- Use a dominant triangular read: cairn mass low, stake vertical, horn or shield offset to one side.
- Keep the cluster rough and improvised, but still readable as deliberate Blood Axe path dressing.
- Preserve strong negative space between the cloth stake, horn/bone element, and cairn cap so the silhouette does not merge into a noisy pile.
- Let the broken shield accent be a secondary read, not a usable shield or loot object.
- Keep the ash base broad and low, never a glowing decal, gameplay trail, or objective marker.

Model as real geometry in a later approved asset task:

- Main cairn stones, stake shaft, broad cloth strip, major horn/bone shape, large shield fragment, heavy lashings, large rope loops, and the outer ash base silhouette.

Keep in texture or normal maps:

- Fine stone cracks, tiny chips, cloth weave, small fray, rope fibers, stitch lines, wood grain, soot speckles, ash flecks, shield scratches, paint chips, horn pitting, and dried mud streaks.

Avoid:

- Dense skull piles, gore, readable text, elegant civic signage, polished stone carving, default blue runes, warm lantern language, refined highland markers, UI arrows, symmetrical fence posts, excessive small bones, or a one-note red-only palette.

## 4. Scale Notes

Use the validated `SK_GIA_Base_A01` scale lock:

- Female Giant baseline: 442 cm / 14 ft 6 in.
- Male Giant baseline: 470 cm / 15 ft 5 in.
- Approved Giant range: females 14-15 ft / 427-457 cm; males 14 ft 10 in-16 ft 0 in / 452-488 cm.
- Author any future source in centimeters. 1 Unreal unit = 1 cm.

Cluster planning dimensions:

- Overall footprint: 300-900 cm wide, depending on terrain use and camera distance.
- Overall height: 160-320 cm, with the cloth stake as the high point.
- Cairn portion: 90-190 cm tall, 140-320 cm footprint.
- Cloth stake: 180-320 cm above ground, with a 50-150 cm torn cloth drop or strip.
- Horn/bone marker: 80-220 cm visible height, attached to the stake or cairn side.
- Broken shield accent: 90-220 cm tall, large enough to feel Giant-scale and too damaged to read as usable gear.
- Ash-stained base: 300-900 cm footprint, very low profile, irregular oval or crescent shape.

The cluster must feel built and placed by hostile Giants. It should not look like human-scale camp dressing enlarged after the fact. The female 442 cm / 14 ft 6 in and male 470 cm / 15 ft 5 in baselines should make the cluster read as knee-to-waist-height route dressing for Giants and large, intimidating ground dressing for smaller races.

## 5. Materials and Color Palette

Primary materials:

- Rough field stone, soot-dark cairn rock, mud-packed stone contact, and chipped slab edges.
- Scorched timber, raw cut stake ends, blackened bark, hide wrap, rope lashing, and dirty leather ties.
- Oxide red cloth, faded raider paint, soot-dark cloth hems, and weathered maroon staining.
- Dull horn, old bone, blackened iron, dark steel, broken shield wood, cracked shield rim, and hammered scrap plate.
- Ash, charcoal, trampled mud, burned grass, packed earth, and greasy soot at the base.

Palette targets:

- Blood Axe red cloth/paint: `#5F1513` to `#8B211B`
- Charcoal and blackened iron: `#111214` to `#2A2C2E`
- Scorched timber: `#22170F` to `#4A2B17`
- Rough stone and ash: `#2E2C28` to `#6C6254`
- Rope, hide, and rawhide: `#6C5434` to `#A88958`
- Bone and horn: `#9E8C6B` to `#CDB78A`
- Mud and soot: `#0B0A09` to `#403025`

Forbidden default reads:

- No neutral/civilized Giant blue-gray masonry, civic stoneworker ornament, warm hearth light, refined terrace motifs, highland clan trail marks, polished cave-town stone, restrained blue runes, or default emissive glow.
- No ritual glow, shamanic glow, signal glow, animated material state, magic marker state, gameplay VFX, or UI-like color coding in this package.

## 6. Concept Image Prompt

Create an original stylized fantasy MMORPG production asset board of `KIT_GIA_BloodAxePathMarkerCluster_A01` for the world of Aerathea. The design should emphasize a composed hostile Giant path-marker cluster made from one crude cairn, one scorched cloth stake, one blunt horn or old bone warning marker, one broken shield accent, and one ash-stained base; rough field stone, scorched timber, hide ties, rope lashings, oxide red cloth, blackened iron, dull horn, old bone, soot, charcoal, mud, Blood Axe raider identity, separation from neutral/civilized Giant culture, and the gameplay role of static visual path readability only. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, no default emissive glow, and MMO-friendly mid-poly production design. Present it as a clean concept sheet with front and three-quarter views, material swatches, scale markers beside a 442 cm / 14 ft 6 in female Giant and a 470 cm / 15 ft 5 in male Giant, and small callouts for silhouette, LOD simplification, and simple collision boundaries. Avoid copying any existing franchise, avoid making Blood Axe culture the default Giant culture, avoid neutral Giant cave-town architecture, avoid graphic gore, avoid readable text, avoid UI arrows, avoid waypoint behavior, avoid objective cluster language, avoid route scripting, avoid encounter setup, avoid pickup or loot behavior, avoid Unreal/startup/final-approval claims, and avoid excessive micro-detail that would not translate to a mid-poly game asset.

## 7. Modeling Notes

This section is a docs-only modeling handoff. It does not create or authorize DCC source, sculpting, retopo, UVs, bakes, proof renders, exports, collision proxies, Unreal assets, runtime source, startup placement, validators, or final visual approval.

Future modeling direction, only if separately approved:

- Build the cluster as a single composed static prop or as tightly grouped reusable sub-meshes, depending on later ownership.
- Keep the pivot at the center of the ash base footprint on the ground plane.
- Face the primary read toward +X in any future source convention unless a later technical task chooses a different project standard.
- Use a few large cairn stones with soft bevels and clear stacking contact. Do not model a pile of tiny rocks.
- Shape the cloth strip as static geometry with broad tears and folds. Do not rely on cloth simulation to make it readable.
- Make the horn/bone marker one major silhouette element, lashed with a few thick rope bands.
- Make the shield accent a damaged, leaning warning shape. Avoid hand-ready grips, pickup readability, or usable equipment proportions.
- Keep the ash base broad and low, with an irregular edge that can sit on uneven Blood Axe camp terrain.
- Design all parts to support aggressive LOD reduction without destroying the cairn/stake/horn/shield silhouette.

Detail assignment:

- Geometry: major stones, stake, cloth silhouette, horn/bone form, shield fragment, thick rope bands, main ash base edge.
- Texture/normal: cracks, chips, cloth weave, fiber fray, rope strands, soot, ash, mud streaks, small dents, scratches, paint chips, bone pitting, and wood grain.

Do not add sockets, simulated cloth, physics chains, destructible states, pickup affordances, nav blockers, objective markers, route scripting markers, encounter markers, Blueprint hooks, review actors, startup scene placement, or Hermes references.

## 8. Texture and Material Notes

Target material strategy for a future approved asset:

- 1 material minimum for distant or repeated cluster use.
- 2 material target for normal use: stone/ash/mud and cloth/hide/horn/shield.
- 3 material maximum only if a close-review variant needs separate stone/ash, cloth/hide, and shield/horn/metal reuse.
- No unique material per stone, cloth strip, rope, horn, shield scratch, ash patch, or mud stain.

Required map set if this cluster is promoted later:

- Base Color / Albedo
- Normal
- Ambient Occlusion
- Packed ORM: Occlusion, Roughness, Metallic

Suggested texture names, naming only:

- `T_GIA_BloodAxePathMarkerCluster_A01_BC`
- `T_GIA_BloodAxePathMarkerCluster_A01_N`
- `T_GIA_BloodAxePathMarkerCluster_A01_ORM`

No emissive map is approved for the default cluster. A texture named `T_GIA_BloodAxePathMarkerCluster_A01_E` should not be created unless a separate later approval explicitly changes the cluster into a ritual or signal variant.

Packed `ORM` guidance:

- R: strong ambient occlusion at cairn contacts, rope lashings, shield overlap, stake base, horn/bone tie points, and ash/mud contact.
- G: high roughness for stone, cloth, rope, hide, bone, horn, ash, soot, and mud; medium-high roughness for blackened iron or shield rim metal.
- B: metallic only for shield rim, scrap plate, nails, clamps, or blackened iron fragments.

Texture style should be hand-painted, MMO-readable, and restrained. Fine surface noise must not overwhelm the main silhouette or imply photorealistic over-detail.

## 9. Triangle Budget

Recommended future LOD0 budget:

- Total cluster: 4k-10k tris.
- Cairn stones: 1.2k-3.5k tris.
- Cloth stake and cloth strip: 700-2k tris.
- Horn/bone marker and lashings: 600-1.5k tris.
- Broken shield accent: 800-2k tris.
- Ash-stained base: 300-1k tris.
- Optional large rope or hide wraps: 200-800 tris total.

Material budget:

- Target: 1-2 material slots.
- Maximum: 3 material slots only for close-review use.

Spend geometry on:

- Chunky cairn mass, vertical stake read, cloth edge silhouette, major horn/bone outline, broken shield rim, and broad ash base edge.

Do not spend geometry on:

- Tiny pebbles, dense splinters, individual ash flecks, many rope fibers, tiny stitch loops, dense scratches, tiny shield chips, small horn pits, or excessive cloth holes.

This cluster should remain within large-prop performance expectations while reading clearly beside the 442 cm female Giant and 470 cm male Giant baselines.

## 10. LOD Plan

All future shipping versions require LOD0-LOD3.

- LOD0: full cairn stack, stake shaft, cloth silhouette, horn/bone form, broken shield accent, major lashings, broad ash base, and readable Blood Axe paint/cloth.
- LOD1: 60-70 percent of LOD0. Reduce stone bevels, simplify cloth tears, merge small lashings, simplify horn/bone bevels, reduce shield edge cuts, and flatten minor ash edge variation.
- LOD2: 35-45 percent of LOD0. Preserve cairn mass, stake height, red cloth read, horn/bone warning read, shield accent silhouette, and ash footprint while removing minor back-side details.
- LOD3: 15-25 percent of LOD0. Preserve the broad triangular read: low cairn, one vertical stake/cloth shape, one side warning accent, and a simple base silhouette.

Reduction order:

1. Tiny ash flecks, stone chips, cloth holes, stitch lines, scratches, paint chips, and horn pits.
2. Minor rope fibers, secondary lashings, small ties, and extra wraps.
3. Small pebbles, small shield splinters, small bone chips, and minor cloth cuts.
4. Back-facing shield detail, underside base detail, and interior cloth folds.
5. Small stone bevels, small stake cuts, and base ground undercuts.

Never reduce the primary Blood Axe read, Giant-scale proportions, cairn/stake/horn/shield silhouette, or red-cloth warning language before removing micro-detail.

## 11. Collision Notes

Default collision should be disabled unless later placement requires player contact handling.

If collision is needed in a later approved asset task:

- Use one simple base box or low-count convex hull around the cairn and shield mass.
- Use one slim capsule or box for the stake if it needs collision at all.
- Do not add cloth collision.
- Do not add per-stone, per-rope, per-bone, per-horn, per-shield-splinter, per-ash-edge, or per-cloth-strip collision.
- Do not create nav helper collision, objective volumes, damage volumes, route scripting volumes, encounter volumes, pickup collision, loot collision, interaction traces, or destructible physics.

The ash-stained base should remain collisionless by default. It is ground dressing, not a gameplay field, trail tracker, or material-state zone.

## 12. Animation Notes

Baseline asset state is fully static.

Allowed planning:

- Static cairn stones.
- Static scorched stake.
- Static cloth strip shaped in mesh form.
- Static horn/bone marker.
- Static broken shield accent.
- Static ash-stained base.
- Optional future material wear variation only if separately approved.

Not approved:

- Cloth simulation, vertex wind, skeletal animation, physics chains, destructible collapse, dangling secondary motion, VFX pulses, material-state gameplay, audio cues, runtime animation, interactive behavior, waypoint behavior, objective behavior, route scripting, encounter setup, AI behavior, patrol markers, pickup/loot behavior, or startup placement.

Any moving, glowing, interactive, pickup, objective, pathfinding, or gameplay-readable version must be split into a separate package and separately approved.

## 13. Unreal Import Notes

These are non-authorizing import guardrails for a possible later handoff. This package performs no Unreal work and selects no implementation target.

- Asset name: `KIT_GIA_BloodAxePathMarkerCluster_A01`
- Asset type: Static Mesh cluster candidate / docs-only production package
- Import destination: not selected in this task
- Source destination: not selected in this task
- Pivot: ground center of the ash base footprint for any later source asset.
- Orientation: primary silhouette faces +X unless a later technical handoff chooses a different convention.
- Scale: centimeter-authored source, import scale 1.0 if separately approved later.
- Collision: disabled by default; simple primitive collision only if later placement requires it.
- LODs: LOD0-LOD3 required before any shipping use.
- Material slot count: 1-2 target, 3 maximum for close-review use.
- Texture list: `T_GIA_BloodAxePathMarkerCluster_A01_BC`, `T_GIA_BloodAxePathMarkerCluster_A01_N`, `T_GIA_BloodAxePathMarkerCluster_A01_ORM`.
- Emissive texture: none for default cluster.
- Sockets: none.
- Animation list: none.
- Blueprint behavior: none.
- Performance notes: use shared Blood Axe material language, reduce micro-detail aggressively, keep collision simple or disabled, and preserve the readable cairn/stake/horn/shield silhouette at distance.

Explicit stop line: no review actor, implementation task, objective cluster, route scripting, encounter setup, DCC, Unreal, startup, final approval, implementation target, or Hermes work is included in this package.

## 14. Folder and Naming Recommendation

Allowed documentation file:

- `docs/assets/kits/KIT_GIA_BloodAxePathMarkerCluster_A01/PRODUCTION_PACKAGE.md`

Primary package name:

- `KIT_GIA_BloodAxePathMarkerCluster_A01`

Suggested future mesh/material names, naming only:

- `SM_GIA_BloodAxePathMarkerCluster_A01`
- `MI_GIA_BloodAxePathMarkerCluster_A01`
- `T_GIA_BloodAxePathMarkerCluster_A01_BC`
- `T_GIA_BloodAxePathMarkerCluster_A01_N`
- `T_GIA_BloodAxePathMarkerCluster_A01_ORM`

Component naming notes:

- Cairn element: `Cairn`
- Cloth stake element: `ClothStake`
- Horn/bone element: `HornBone`
- Broken shield element: `BrokenShield`
- Ash base element: `AshBase`

Do not create or edit `Content/Aerathea`, `SourceAssets`, `Tools/DCC`, `Tools/Unreal`, runtime source, external source concept folders, global indexes, Hermes files/configuration, validation-summary files, task-board files, startup maps, material assets, texture assets, Blueprint assets, or DCC files for this task.

## 15. Quality Gate Checklist

- The package is docs-only and edits only `docs/assets/kits/KIT_GIA_BloodAxePathMarkerCluster_A01/PRODUCTION_PACKAGE.md`.
- The cluster combines exactly one cairn, one cloth stake, one horn/bone marker, one broken shield accent, and one ash-stained base.
- Giant scale lock is explicit: female 442 cm / 14 ft 6 in and male 470 cm / 15 ft 5 in.
- Blood Axe identity is a hostile Giant sub-faction and remains separate from neutral/civilized Giant culture.
- The package avoids neutral/civilized Giant cave-town masonry, civic stoneworker motifs, warm hearth language, refined blue-gray stone, highland nomad wayfinding, and default blue-rune culture.
- Gameplay purpose is static visual readability only.
- No review actor, implementation task, objective cluster, route scripting, encounter setup, DCC, Unreal, startup, final approval, implementation target, Hermes work, runtime source, external source concept handling, or global index work is included.
- No waypoint behavior, trail-marker gameplay, nav/pathfinding helper, pickup/loot behavior, combat cover, damage field, interaction prompt, AI behavior, patrol marker, spawn marker, VFX pulse, audio cue, or material-state gameplay is defined.
- Silhouette reads at MMO camera distance through chunky cairn mass, vertical cloth stake, horn/bone warning form, broken shield accent, and broad ash base.
- Materials use rough field stone, scorched timber, hide, rope, oxide red cloth, blackened iron, dull horn/bone, soot, ash, mud, and burned earth.
- Default emissive, ritual glow, shamanic glow, signal glow, animated material states, UI-like markers, readable text, and graphic gore are absent.
- Triangle budgets, material slot targets, texture map list, LOD0-LOD3 plan, collision limits, animation limits, import guardrails, and naming recommendations are included.
- Tiny chips, cloth weave, fray, fibers, scratches, soot speckles, ash flecks, paint chips, horn pitting, and wood grain are assigned to texture or normal detail instead of geometry.
- The package is useful for a future DCC or Unreal handoff without creating the handoff work in this task.
- The final document does not claim visual final approval, source creation, asset export, engine import, startup placement, route scripting, encounter setup, objective setup, or implementation ownership.
