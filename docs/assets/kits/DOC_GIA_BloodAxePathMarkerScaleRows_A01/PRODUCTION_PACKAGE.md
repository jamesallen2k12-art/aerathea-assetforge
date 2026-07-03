# DOC_GIA_BloodAxePathMarkerScaleRows_A01 Production Package

## Art Direction Summary

- Asset name: `DOC_GIA_BloodAxePathMarkerScaleRows_A01`
- Asset type: Non-shipping docs-only scale-row package
- Parent kit: `KIT_GIA_BloodAxePathMarkers_A01`
- Source planning row: `Blood Axe Village.png#Review_ScaleRows_A01`
- Faction/theme: Blood Axe Tribe, hostile Giant sub-faction only
- Status: docs-only scale package ready

`DOC_GIA_BloodAxePathMarkerScaleRows_A01` defines non-shipping scale comparison rows for Blood Axe path-marker modules beside the validated Giant baselines. The rows help future DCC and visual review avoid human-scaled marker drift, but they do not change the Giant scale lock, approve shipped marker proportions, create Unreal assets, run capture automation, or select implementation targets.

Blood Axe markers must remain a hostile Giant sub-faction language, not neutral/civilized Giant wayfinding.

## Gameplay Purpose

The scale rows support production planning by showing how path-marker categories read beside Giant baselines and other marker families.

Allowed planning uses:

- Compare low cairns, cloth stakes, bone/horn markers, broken shield markers, ash bases, and mixed clusters beside Giant scale references.
- Keep low, mid, and broad footprint markers from drifting into banner, gate, or full encounter-prop scale.
- Preserve clear MMO camera readability while keeping static dressing separate from gameplay markers.
- Document proportion relationships for later DCC handoff.

Out of scope:

- Scale-lock changes, shipped marker approval, DCC source creation, FBX export, Unreal import, validator creation, capture automation, startup placement, final visual approval, implementation target selection, waypoint behavior, objective logic, nav/pathfinding behavior, pickup/loot behavior, combat cover, encounter rules, VFX/audio, or Hermes work.

## Silhouette Notes

Scale rows should compare:

- Low ash/base elements.
- Single cairn markers.
- Cairn clusters.
- Cloth stake markers.
- Cloth stake sets.
- Low red rag markers.
- Bone/horn markers.
- Horn fork markers.
- Broken shield markers and scrap shield lean markers.
- Mixed marker clusters.

The rows should make the major category reads obvious: ground base, low cairn, mid stake, horn warning, shield warning, and mixed cluster. Avoid fine-detail comparison as the purpose of the rows is proportion and readability.

## Scale Notes

Use the validated `SK_GIA_Base_A01` scale lock:

- Female Giant baseline: 442 cm / 14 ft 6 in.
- Male Giant baseline: 470 cm / 15 ft 5 in.
- Approved Giant ranges: females 14-15 ft / 427-457 cm; males 14 ft 10 in-16 ft 0 in / 452-488 cm.
- Author future source in centimeters. 1 Unreal unit = 1 cm.

Recommended row references:

- Female baseline marker: 442 cm.
- Male baseline marker: 470 cm.
- Low rag or ash base: 20-120 cm vertical emphasis.
- Single cairn: 80-180 cm.
- Cairn cluster: 120-260 cm.
- Cloth stake: 140-280 cm.
- Bone/horn marker: 80-260 cm.
- Broken shield marker: 100-240 cm.
- Mixed cluster: 120-300 cm height range with 300-900 cm footprint.

This package does not alter scale values or approve final shipping proportions.

## Materials and Color Palette

Scale rows should use simplified material reads:

- Rough field stone and soot-stained boulders.
- Scorched timber and raw pole cuts.
- Torn oxide red cloth and faded paint.
- Rope, hide, dirty leather, and sinew ties.
- Old horn, dull bone, blackened iron, broken shield wood, and scrap plate.
- Ash, charcoal, soot, trampled mud, and packed earth.

Palette targets:

- Blood Axe red: `#5F1513` to `#8B211B`
- Charcoal and blackened iron: `#111214` to `#2A2C2E`
- Scorched timber: `#22170F` to `#4A2B17`
- Rough stone and ash: `#2E2C28` to `#6C6254`
- Rope and hide: `#6C5434` to `#A88958`
- Bone and horn: `#9E8C6B` to `#CDB78A`

No default emissive, signal glow, shamanic glow, or VFX material is approved.

## Concept Image Prompt

Create an original stylized fantasy MMORPG scale comparison sheet of `DOC_GIA_BloodAxePathMarkerScaleRows_A01` for the world of Aerathea. The sheet should show non-shipping Blood Axe Giant path-marker scale rows beside a 442 cm female Giant and a 470 cm male Giant, comparing low ash bases, single cairns, cairn clusters, cloth stakes, low red rag markers, bone and horn markers, broken shield markers, and mixed path-marker clusters. Emphasize clear proportion relationships, static hostile Giant sub-faction dressing, rough field stone, scorched timber, oxide red cloth, blackened scrap, dull bone and horn, soot, ash, mud, and clear separation from neutral/civilized Giant culture. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, no default emissive glow, and MMO-friendly mid-poly production design. Present it as non-shipping scale rows with callout heights and material swatches on a clean background. Avoid copying any existing franchise, avoid scale-lock changes, avoid shipped marker approval claims, avoid Unreal actor claims, avoid validator or capture claims, avoid waypoint behavior, avoid objective logic, avoid nav/pathfinding diagrams, avoid pickup or loot behavior, and avoid excessive micro-detail.

## Modeling Notes

This is a docs-only scale planning package. No DCC source, sculpt, retopo, UV, bake, FBX export, Unreal asset, collision proxy, proof render, material graph, validator, capture, startup actor, runtime source, final visual approval, or Hermes file is created or authorized.

Future scale-row modeling, if approved, should:

- Use non-shipping comparison markers and simple Giant height rods.
- Show only enough geometry to compare marker height and footprint.
- Keep rows visually distinct from final shipping assets.
- Preserve the 442 cm and 470 cm baseline labels in documentation only.
- Avoid readable in-world text as part of the marker design.

Do not introduce collision, sockets, gameplay volumes, waypoint arrows, pathfinding helpers, objective frames, pickup affordances, or route scripting.

## Texture and Material Notes

Scale rows should use simplified utility materials if ever implemented.

- 1 material preferred for non-shipping rows.
- Use flat color or shared Blood Axe swatches for row readability.
- Do not create material instances, texture assets, material graphs, emissive maps, or VFX materials from this package.

Potential future texture naming only if a temporary review mesh is approved:

- `T_GIA_BloodAxePathMarkerScaleRows_A01_BC`
- `T_GIA_BloodAxePathMarkerScaleRows_A01_N`
- `T_GIA_BloodAxePathMarkerScaleRows_A01_ORM`

These names are planning references only.

## Triangle Budget

Non-shipping scale-row target if later implemented:

- 500-3k tris per row set.
- 1 material preferred.
- Utility texture or shared atlas only.

Spend geometry on broad comparison silhouettes. Do not model tiny chips, cloth weave, rope fibers, scratches, soot speckles, ash flecks, paint chips, or hidden underside detail.

## LOD Plan

If scale rows are ever implemented as temporary assets, use LOD0-LOD3:

- LOD0: clear height rods, baseline silhouettes, and broad marker categories.
- LOD1: 60-70 percent of LOD0; reduce bevels and row detail.
- LOD2: 35-45 percent of LOD0; preserve height comparison only.
- LOD3: 15-25 percent of LOD0; preserve baseline and category silhouettes.

Reduction order:

1. Tiny surface details.
2. Secondary lashings and cloth cuts.
3. Small stones, small bones, and small shield chips.
4. Back-facing detail.
5. Non-shipping row helper detail.

## Collision Notes

Scale rows should have collision disabled if ever implemented.

- No per-marker collision.
- No nav blockers.
- No gameplay volumes.
- No trigger volumes.
- No objective volumes.
- No pickup collision.
- No interaction collision.
- No startup placement collision.

Collision is not created by this package.

## Animation Notes

No animation is planned.

- No cloth simulation.
- No wind animation.
- No physics sway.
- No material animation.
- No VFX pulse.
- No capture automation.
- No startup review motion.

## Unreal Import Notes

Future import path if explicitly approved for temporary review use:

- Static Mesh or review actor folder: `/Game/Aerathea/Review/Giants/BloodAxe/PathMarkers/`

Planning constraints:

- Units: centimeters.
- Pivot: row origin at ground center if temporary meshes are ever approved.
- Collision: disabled.
- LODs: LOD0-LOD3 only if temporary meshes are promoted.

Do not create Unreal assets, review actors, validators, captures, startup placements, material instances, Blueprints, or runtime hooks from this package.

## Folder and Naming Recommendation

Docs:

- `docs/assets/kits/DOC_GIA_BloodAxePathMarkerScaleRows_A01/PRODUCTION_PACKAGE.md`

Future source folders only after approval:

- `SourceAssets/Blender/Review/Giants/BloodAxe/PathMarkers/DOC_GIA_BloodAxePathMarkerScaleRows_A01/`
- `SourceAssets/Exports/Review/Giants/BloodAxe/PathMarkers/DOC_GIA_BloodAxePathMarkerScaleRows_A01/`

Future Unreal naming only after approval:

- `SM_REVIEW_GIA_BloodAxePathMarkerScaleRows_A01`
- `MI_REVIEW_GIA_BloodAxePathMarkerScaleRows_A01`

No source folder, export folder, Unreal asset, review actor, validator, or capture is created by this docs-only package.

## Quality Gate Checklist

- Scale rows are original to Aerathea and Blood Axe hostile Giant culture.
- Neutral/civilized Giant culture remains separate.
- Validated Giant scale is explicit: female 442 cm / 14 ft 6 in and male 470 cm / 15 ft 5 in.
- Rows compare marker proportions without changing the scale lock.
- Rows are non-shipping planning artifacts.
- No scale-lock change, shipped marker approval, Unreal actor, validator, capture automation, startup placement, final visual approval, first DCC target, first implementation target, source concept movement, DCC source, FBX export, Unreal Content, runtime source, or Hermes work is authorized.
- No waypoint behavior, trail-marker gameplay, objective logic, nav/pathfinding behavior, pickup/loot behavior, interaction behavior, VFX/audio, AI behavior, or encounter behavior is defined.
- Triangle budget, LOD policy, collision limits, Unreal import notes, and naming recommendations are included.
