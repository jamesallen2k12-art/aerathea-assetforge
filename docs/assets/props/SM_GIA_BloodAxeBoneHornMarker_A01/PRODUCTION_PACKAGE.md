# SM_GIA_BloodAxeBoneHornMarker_A01 Production Package

## 1. Art Direction Summary

- Asset name: `SM_GIA_BloodAxeBoneHornMarker_A01`
- Asset type: Static Mesh prop production package
- Parent planning kit: `KIT_GIA_BloodAxeCamp_A01`
- Source planning row: `BloodAxeCamp.png#Clutter_BoneHornMarkers`
- Related path-marker kit: `KIT_GIA_BloodAxePathMarkers_A01`
- Faction/theme: Blood Axe Tribe, hostile Giant sub-faction only
- Status: docs-only production package ready

`SM_GIA_BloodAxeBoneHornMarker_A01` is a sparse, non-graphic territory marker for hostile Blood Axe camp dressing. It should read as crude Giant-made warning clutter from MMO camera distance: one dominant old horn or blunt bone shape lashed to a heavy stake, low cairn side, or mud-and-ash base, with restrained oxide red cloth and dark lashings for faction read.

The marker is intimidation dressing, not a gore prop, ritual object, loot object, crafting resource, or interactable gameplay marker. Blood Axe visual language must remain separate from neutral/civilized Giant culture; do not use refined cave-town masonry, civic wayfinding, warm hearth settlement language, terrace/waterwork motifs, or restrained blue-rune Giant culture cues.

This package is planning only. It does not authorize DCC source creation, FBX export, Unreal Content creation, material graph authoring, startup placement, source concept movement, final visual approval, or first DCC target selection.

## 2. Gameplay Purpose

The asset supports visual territory dressing around Blood Axe camp approaches, shelter edges, forge-adjacent clutter, gate flanks, rough path bends, and perimeter thresholds. Its purpose is to make the camp feel claimed by a hostile Giant sub-faction without adding mechanics.

Allowed planning uses:

- Mark a Blood Axe camp edge, approach beat, or warning cluster as visual dressing only.
- Break up ground-plane emptiness near larger camp modules such as gates, shelters, banner lines, watch platforms, and packed-earth paths.
- Add low-to-mid-height hostile silhouette rhythm without reading as a quest marker, route arrow, interactable object, or resource node.
- Provide a reusable camp-clutter marker distinct from the path-marker child candidate `SM_GIA_BloodAxeBoneHornPathMarker_A01`.

Out of scope:

- Gore escalation, fresh remains, dismemberment, loot drops, pickup behavior, inventory behavior, resource nodes, harvesting, crafting behavior, economy behavior, ritual behavior, waypoint behavior, objective logic, trail-marker gameplay, nav/pathfinding behavior, AI patrol markers, spawn markers, combat cover, damage volumes, destructible behavior, interaction prompts, VFX pulses, audio cues, material-state gameplay, or startup placement.

## 3. Silhouette Notes

Primary read:

- One dominant horn fork, curved horn pair, or blunt old bone shape set into a crude Blood Axe base.
- Heavy vertical or leaning stake between 90 and 220 cm tall, or a low cairn-side variant using two or three large stones.
- Thick rope, hide, or sinew lashings that visibly bind the horn/bone to the stake or cairn.
- Optional single torn oxide red cloth strip for faction read; keep it static, broad, and readable.
- Low ash, mud, soot, and trampled-earth base that grounds the marker without becoming a decal gameplay trail.

Model as real geometry in a future approved DCC task:

- Main horn/bone silhouette, stake shaft, major cairn stones, broad red cloth piece, large lashings, major hide wraps, simple iron clamp, and low base shape.

Keep in textures, normals, or baked detail:

- Small chips, hairline cracks, subtle horn rings, bone pitting, rope fibers, cloth weave, tiny fray, soot speckles, ash flecks, mud streaks, and minor wood grain.

Avoid:

- Dense skull piles, graphic trophies, fresh blood, readable text, UI arrow shapes, glowing markers, polished carved Giant signs, civic stoneworker marks, blue runes, warm lantern or hearth motifs, excessive hanging pieces, or a one-note red-only palette.

## 4. Scale Notes

Use the validated `SK_GIA_Base_A01` scale lock:

- Female Giant baseline: 442 cm / 14'6".
- Male Giant baseline: 470 cm / 15'5".
- Approved Giant ranges: females 14-15 ft / 427-457 cm; males 14'10"-16'0" / 452-488 cm.
- Author all future source in centimeters. 1 Unreal unit = 1 cm.

Planning dimensions:

- Standard stake marker: 120-220 cm tall, 80-180 cm wide, 80-180 cm deep.
- Low cairn-side marker: 80-160 cm tall, 120-250 cm footprint.
- Leaning horn marker: 90-180 cm tall, 100-240 cm footprint.
- Base ash/mud pad: 150-300 cm footprint, very low height, collision disabled by default.
- Recommended repeated spacing in a camp scene: irregular 300-900 cm gaps when used in groups, never as a fence or UI path line.

The marker should feel Giant-placed and oversized for normal humanoids, but still smaller than major Blood Axe gates, watch platforms, shelters, and banner poles.

## 5. Materials and Color Palette

Primary materials:

- Old horn, dull bone, sun-weathered bone edges, and darker worn horn tips.
- Scorched timber, raw stake cuts, rough field stone, soot-stained cairn slabs, and mud-packed base stones.
- Hide ties, rope lashings, sinew cord, dirty leather wraps, and simple blackened iron clamps.
- Torn oxide red cloth or faded red paint used sparingly for Blood Axe identity.
- Packed earth, trampled mud, ash, soot, charcoal, and burned grass around the base.

Palette targets:

- Dull bone and old horn: `#9E8C6B` to `#CDB78A`
- Dark horn tips: `#2A2118` to `#4A3A27`
- Blood Axe red cloth or paint: `#5F1513` to `#8B211B`
- Charcoal and blackened iron: `#111214` to `#2A2C2E`
- Scorched timber: `#22170F` to `#4A2B17`
- Rough stone and ash: `#2E2C28` to `#6C6254`
- Rope, hide, and rawhide: `#6C5434` to `#A88958`
- Mud and soot: `#0B0A09` to `#403025`

No default emissive is approved. Signal glow, ritual glow, shamanic accents, VFX pulses, animated material states, or magic marker states require a separate approved package.

## 6. Concept Image Prompt

Create an original stylized fantasy MMORPG concept sheet of `SM_GIA_BloodAxeBoneHornMarker_A01` for the world of Aerathea. The design should emphasize a sparse non-graphic Blood Axe Giant territory marker, one dominant old horn or blunt bone silhouette, crude scorched timber stake, optional low cairn base, heavy rope or hide lashings, restrained oxide red cloth, soot, mud, ash, hostile Giant sub-faction identity, clear separation from neutral/civilized Giant culture, and the gameplay role of static camp territory dressing only. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, no default emissive glow, and MMO-friendly mid-poly production design. Present it as a single prop production sheet with front/side/back views, material swatches, LOD/collision notes, and scale markers beside a 442 cm female Giant and a 470 cm male Giant on a clean background. Avoid copying any existing franchise, avoid making Blood Axe culture the default Giant culture, avoid neutral Giant cave-town architecture, avoid graphic gore, avoid fresh remains, avoid dense trophy piles, avoid readable text, avoid loot or pickup affordances, avoid crafting resource language, avoid ritual behavior, avoid VFX or material graph claims, avoid waypoint or objective marker design, and avoid excessive micro-detail that would not translate to a mid-poly Unreal asset.

## 7. Modeling Notes

This is a docs-only modeling plan. No DCC source, sculpt, retopo, UV, bake, FBX export, Unreal asset, collision proxy, proof render, material graph, validator, startup actor, runtime source, or final visual approval is created or authorized by this package.

Future modeling should prioritize:

- A single readable hero silhouette: dominant horn/bone first, support stake or cairn second, base dressing third.
- Ground-centered pivot at the base center so later placement can sit on uneven camp terrain without scale changes.
- Primary read facing +X unless a future DCC/export task confirms another project convention.
- Thick, chunky lashings that can be read from distance; avoid many small cords.
- Static cloth geometry with one or two broad tears only; do not rely on cloth simulation.
- Low cairn stones built from a few large, beveled pieces rather than many pebbles.
- Base mud/ash as simple low geometry or a future shared ground-dressing mesh, not a gameplay trail system.
- Optional variant planning only: `StakeHorn`, `CairnBone`, and `LowPairedHorn`. Do not create variants or select one for DCC in this task.

Suggested future mesh groups:

- `Marker_Base_AshMud`
- `Marker_StakeOrCairn`
- `Marker_BoneHorn`
- `Marker_Lashings`
- `Marker_RedCloth_Optional`
- `Marker_IronClamp_Optional`

Do not introduce sockets, character attachment fit, physics setup, destructible states, pickup affordances, resource affordances, ritual anchors, VFX locators, interaction prompts, waypoint helpers, nav helpers, combat cover definitions, or startup placement in this package.

## 8. Texture and Material Notes

Target material strategy:

- Default target: 1 material slot using a compact shared prop atlas.
- Optional 2-slot setup only if a future art pass needs separate reusable `BoneHorn` and `BaseClothHardware` materials.
- Avoid unique material slots for each horn, bone, rope tie, cloth strip, ash patch, mud stain, or clamp.

Suggested future material instances:

- `MI_GIA_BloodAxeBoneHornMarker_A01`
- `MI_GIA_BloodAxeBoneHorn_A01`
- `MI_GIA_BloodAxeClothHide_A01`
- `MI_GIA_BloodAxeAshMud_A01`

Required texture names if this asset receives a unique texture set later:

- `T_GIA_BloodAxeBoneHornMarker_A01_BC`
- `T_GIA_BloodAxeBoneHornMarker_A01_N`
- `T_GIA_BloodAxeBoneHornMarker_A01_ORM`

Optional only with later approval:

- `T_GIA_BloodAxeBoneHornMarker_A01_E` for a separately approved signal or ritual variant. This is not part of the default asset.

Texture set targets:

- 512-1K texture set for standard use.
- 1K preferred if the marker is repeatedly viewed near camp paths or gate flanks.
- 2K is not justified for the default asset.

Packed `ORM` plan:

- R: Ambient occlusion around horn/bone contact, lashings, stake base, cairn stones, and ash/mud contact.
- G: High roughness for bone, horn, timber, cloth, rope, hide, soot, ash, and mud; medium-high varied roughness for blackened iron.
- B: Metallic only for optional iron clamp or small scrap plate accents.

## 9. Triangle Budget

Target budget:

- LOD0: 800-3k tris, 1 material target, 2 material maximum.
- LOD1: 500-1.8k tris.
- LOD2: 250-900 tris.
- LOD3: 100-400 tris.

Budget notes:

- Spend geometry on the main horn/bone silhouette, stake or cairn profile, broad lashings, and base read.
- Use bevels sparingly on large silhouette edges only.
- Do not spend geometry on tiny chips, hairline cracks, small rope fibers, dense ash clumps, many cloth holes, many scratches, or repeated small trophies.
- If a future composed cluster uses multiple markers, prefer instancing this prop rather than making one heavy unique mesh.

## 10. LOD Plan

All important future static mesh variants require LOD0-LOD3.

- LOD0: Full horn/bone shape, stake or cairn support, broad lashings, optional cloth, simple clamp, base ash/mud, and readable baked detail.
- LOD1: 55-65 percent of LOD0; simplify horn/bone bevels, reduce lashing loops, merge small base forms, and reduce cloth edge cuts.
- LOD2: 30-40 percent of LOD0; preserve horn/bone silhouette, stake/cairn mass, red cloth read, and base footprint while removing back-side accents and small cuts.
- LOD3: 12-20 percent of LOD0; preserve only the broad marker silhouette, dominant horn/bone read, and rough base shape.

Reduction order:

1. Tiny chips, scratches, soot flecks, ash flecks, cloth holes, and paint chips.
2. Minor rope fibers, small secondary ties, tiny knots, and extra wraps.
3. Small stone chips, small horn chips, small bone chips, and minor clamp cuts.
4. Back-facing cloth tears, underside detail, and interior base cuts.
5. Small bevels on lashings, stake cuts, and base undercuts.

Never reduce the primary horn/bone silhouette, hostile Blood Axe red/black accent read, or Giant-scale marker size before removing small detail.

## 11. Collision Notes

Default collision should be disabled unless a later placement task proves player contact is needed.

If collision is approved later:

- Use one simple capsule or slim box for a stake marker.
- Use one low-count convex hull or simple box around a cairn-side marker.
- Use no per-bone, per-horn, per-rope, per-cloth, per-stone, per-ash, or per-clamp collision.
- Keep ash/mud base collision disabled.
- Do not add gameplay volumes, nav blockers, cover volumes, damage volumes, pickup collision, loot collision, crafting/resource collision, ritual collision, destructible collision, or interaction collision.

This package does not create collision proxies or assign collision settings in Unreal.

## 12. Animation Notes

Baseline asset is static.

Allowed planning:

- Static mesh only.
- Optional static wear variants in a future material or mesh-variant task.
- Optional static cloth pose as modeled geometry only.

Not approved here:

- Cloth simulation, vertex wind, dangling secondary physics, skeletal animation, runtime animation, destructible collapse, material-state animation, VFX pulses, audio cues, waypoint behavior, objective marker behavior, pickup/loot behavior, resource behavior, crafting behavior, ritual behavior, AI behavior, or startup placement.

Any moving, glowing, interactive, pickup, resource, ritual, or gameplay-readable version must be split into a separately named and approved asset.

## 13. Unreal Import Notes

This section is planning only. No Unreal Content asset, material instance, texture, socket, Blueprint, validator, runtime source, startup actor, VFX asset, material graph, or placement is created or authorized by this package.

Planned future import target after approval:

- Asset name: `SM_GIA_BloodAxeBoneHornMarker_A01`
- Asset type: Static Mesh
- Planned folder: `/Game/Aerathea/Props/Giants/BloodAxeCamp/Clutter/`
- Material folder reference: `/Game/Aerathea/Materials/Giants/BloodAxe/`
- Naming convention: `SM_GIA_BloodAxeBoneHornMarker_A01`, `MI_GIA_BloodAxeBoneHornMarker_A01`, `T_GIA_BloodAxeBoneHornMarker_A01_BC`, `T_GIA_BloodAxeBoneHornMarker_A01_N`, `T_GIA_BloodAxeBoneHornMarker_A01_ORM`
- Pivot: ground/base center.
- Orientation: primary marker read faces +X unless a future DCC/export task confirms a different project convention.
- Scale: centimeter-authored source, Unreal import scale 1.0 after future DCC/export approval.
- Collision type: disabled by default; simple primitive only if later placement requires contact.
- LOD plan: LOD0-LOD3 required before shipping import approval.
- Material slot count: 1 target, 2 maximum.
- Texture list: `T_GIA_BloodAxeBoneHornMarker_A01_BC`, `T_GIA_BloodAxeBoneHornMarker_A01_N`, `T_GIA_BloodAxeBoneHornMarker_A01_ORM`; no emissive texture for default asset.
- Sockets: none.
- Animation list: none.
- Blueprint behavior: none.
- Performance notes: use low material count, shared Blood Axe camp material language, simple collision or none, aggressive LOD reduction of micro-detail, and instancing for repeated placement.

Do not add waypoint behavior, objective logic, nav/pathfinding behavior, loot/pickup behavior, crafting/resource behavior, ritual behavior, VFX/material graph authoring, startup placement, or first DCC target selection from this package.

## 14. Folder and Naming Recommendation

Docs:

- `docs/assets/props/SM_GIA_BloodAxeBoneHornMarker_A01/PRODUCTION_PACKAGE.md`

Planned future paths after separate approval only:

- Source: `SourceAssets/Blender/Props/Giants/BloodAxeCamp/Clutter/SM_GIA_BloodAxeBoneHornMarker_A01/`
- Export: `SourceAssets/Exports/Props/Giants/BloodAxeCamp/Clutter/SM_GIA_BloodAxeBoneHornMarker_A01/`
- Unreal: `/Game/Aerathea/Props/Giants/BloodAxeCamp/Clutter/`

Suggested future asset names:

- `SM_GIA_BloodAxeBoneHornMarker_A01`
- `MI_GIA_BloodAxeBoneHornMarker_A01`
- `T_GIA_BloodAxeBoneHornMarker_A01_BC`
- `T_GIA_BloodAxeBoneHornMarker_A01_N`
- `T_GIA_BloodAxeBoneHornMarker_A01_ORM`

Related but separate planning candidate:

- `SM_GIA_BloodAxeBoneHornPathMarker_A01` remains a path-marker child candidate under `KIT_GIA_BloodAxePathMarkers_A01`. Do not silently rename this camp-clutter territory marker into the path-marker child without a new task.

Do not add SourceAssets folders, Blender files, sculpt files, retopo files, proof renders, FBX exports, Unreal Content assets, runtime source, tools, validators, startup actors, copied source concepts, external source edits, global index entries, task-board edits, backlog edits, or bootstrap edits from this task.

## 15. Quality Gate Checklist

- Package follows the universal Aerathea production-package format.
- Package is docs-only and planning-only.
- Package changes no DCC, FBX, Unreal Content, runtime source, startup scene, external concept, validator, global index, task board, backlog, or bootstrap file.
- Blood Axe remains a hostile Giant sub-faction, not neutral/civilized Giant culture.
- Giant scale lock is explicit: female baseline 442 cm / 14'6", male baseline 470 cm / 15'5", approved ranges females 14-15 ft and males 14'10"-16'0".
- Asset is sparse, non-graphic, territory dressing only.
- Gameplay purpose is static camp territory readability and ground-plane dressing only.
- Silhouette reads at MMO camera distance through one dominant old horn or blunt bone form, crude stake or cairn support, heavy lashings, restrained red cloth, and low ash/mud base.
- Materials use old horn, dull bone, scorched timber, rough stone, hide, rope, blackened iron, soot, ash, mud, and oxide red cloth consistently.
- Default emissive, ritual glow, shamanic glow, signal glow, VFX pulses, animated material states, gameplay material states, and neutral/civilized Giant cues are absent and approval-gated where applicable.
- Triangle budgets, texture maps, material slot targets, LOD0-LOD3 plan, collision limits, animation limits, Unreal import planning, folder naming, approval gates, and stop gates are included.
- Tiny chips, horn rings, bone pitting, rope fibers, cloth weave, soot speckles, ash flecks, mud streaks, and wood grain are assigned to textures or normals.
- No gore escalation, loot/pickup behavior, crafting resource behavior, ritual behavior, VFX/material graph authoring, startup placement, or first DCC target selection is defined.
- No waypoint behavior, objective logic, nav/pathfinding behavior, AI behavior, combat cover, damage volume, destructible behavior, audio cue, UI marker, or interaction behavior is defined.
- Source concepts remain external and are not copied, moved, edited, embedded, inspected for visual approval, or committed.
