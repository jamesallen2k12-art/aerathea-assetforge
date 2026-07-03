# SM_GIA_BloodAxePathEdgeUtilityCluster_A01 Production Package

## 1. Art Direction Summary

- Asset name: `SM_GIA_BloodAxePathEdgeUtilityCluster_A01`
- Asset type: Static Mesh production package, docs-only
- Parent kit: `KIT_GIA_BloodAxeCampTools_A01`
- Child intake row: `Blood Axe Village.png#CampTools_UtilityCluster_PathEdge_A01`
- Faction/theme: Blood Axe Tribe, hostile Giant sub-faction only
- Status: package-ready planning document; no implementation target selected

This cluster is a low path-edge dressing set with a mud-dark base, thick rope, blunt wedges, a battered bucket or ring peg, and one dull red tie. It should mark rough camp labor and hostile occupation without becoming a waypoint, nav marker, encounter prop, loot pile, or resource node.

Blood Axe remains a hostile Giant sub-faction separate from neutral/civilized Giant culture. Avoid peaceful highland trail language, refined civic masonry, blue-gray cave-town craft, warm hearth presentation, and restrained blue rune or storm motifs.

Guardrails: no-DCC, no-Unreal, no-startup, no-nav, no-encounter, no-workstation, no-loot, no-resource, no-material-instance, no-validator, no-capture, no-final-signoff, no-implementation-target.

## 2. Gameplay Purpose

This asset provides static visual dressing near Blood Axe path edges and camp circulation lanes. It reinforces Giant scale while preserving readable movement space and sightlines.

It does not define pathfinding, nav blockers, encounter cover, route markers, objective logic, player guidance, pickup behavior, loot behavior, resource behavior, crafting/economy systems, workstation use, NPC routines, startup placement, or runtime gameplay.

## 3. Silhouette Notes

The silhouette should be flatter and longer than the general utility cluster, with the highest element kept near the bucket rim or mallet head. Use a rope coil, wedge group, ring peg, and small hook set to create an asymmetric edge composition that reads from the side of a path.

Keep negative space clear around the cluster so it does not read as a barricade. Model large forms only; reserve rope fiber, scratches, mud, soot, and chipped paint for future texture work.

Avoid tall stakes, signpost reads, route arrows, glowing markers, stacked crates, cover-wall silhouettes, trap reads, or dense clutter that narrows Giant-scale visual lanes.

## 4. Scale Notes

Use the validated Giant scale lock:

- Female Giant baseline: 442 cm / 14'6".
- Male Giant baseline: 470 cm / 15'5".
- Approved Giant ranges: females 14-15 ft / 427-457 cm; males 14'10"-16'0" / 452-488 cm.
- Author in centimeters. 1 Unreal unit = 1 cm.

Suggested footprint: 300-700 cm wide along path, 120-300 cm deep, and 60-180 cm tall. Rope coil diameter should remain 120-240 cm, wedges 50-130 cm long, bucket/ring-peg elements 70-160 cm tall. The cluster must remain oversized for Giant handling and not become humanoid trail clutter.

## 5. Materials and Color Palette

Use mud-dark ground contact, blackened iron, dark steel, scorched timber, thick rope, hide ties, dirty leather, dull red cloth ties, chipped red paint, ash, soot, and grime.

Avoid civilized Giant carved stone, clean trail markers, polished metal, bright flags, default emissive, blue runes, warm hearth colors, and high-density red decoration.

## 6. Concept Image Prompt

Create an original stylized fantasy MMORPG concept image of `SM_GIA_BloodAxePathEdgeUtilityCluster_A01` for the world of Aerathea. The design should emphasize a low path-edge hostile Giant camp utility cluster, mud-dark base, thick rope coil, blunt wedges, battered ring peg, small blackened hook set, restrained dull Blood Axe red tie, soot-stained timber, dark steel, hide lashings, preserved Giant-scale visual lane, female Giant scale 442 cm / 14'6", male Giant scale 470 cm / 15'5", and a gameplay role as static non-interactive path-edge dressing. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, no default emissive glow, and MMO-friendly production design. Present it as a clean production asset board with side-read, top footprint, scale callouts, material swatches, LOD notes, and collision notes. Avoid copying any existing franchise and avoid excessive micro-detail that would not translate to a mid-poly Unreal asset.

## 7. Modeling Notes

Future modeling should use a wide, low footprint with strong side readability. Reuse bucket, rope, wedge, hook, and ring-peg forms from the parent camp-tools kit where possible. Keep any base dirt or mud implied through material, not as a large terrain slab.

Use real geometry for coil mass, wedges, ring peg, hook curves, large knot, bucket rim if present, and primary ground-contact forms. Use texture or normal detail for fibers, fray, pitting, scratches, soot, mud, small stitch lines, tiny chips, and paint wear.

Do not create DCC source, FBX, collision proxy, proof render, Unreal Content, Blueprint, sockets, material instance, validator, capture setup, startup actor, nav setup, or implementation target from this package.

## 8. Texture and Material Notes

Future texture set:

- `T_GIA_BloodAxePathEdgeUtilityCluster_A01_BC`
- `T_GIA_BloodAxePathEdgeUtilityCluster_A01_N`
- `T_GIA_BloodAxePathEdgeUtilityCluster_A01_ORM`

No emissive map is planned. Target 1K-2K. Material slots: 2 target, 3 maximum if metal/wood/rope separation requires it. Do not create a material instance in this docs-only package.

## 9. Triangle Budget

Target LOD0: 4.5k-12k tris.

Target material slots: 2, with 3 maximum only if required. Keep the path-edge cluster lighter than larger camp review compositions.

## 10. LOD Plan

- LOD0: full rope coil, wedges, bucket or ring peg, hooks, major knots, red tie, and path-edge footprint.
- LOD1: 60-70 percent of LOD0; reduce bevels, extra coil turns, small ties, backside detail, and duplicate hook detail.
- LOD2: 35-45 percent of LOD0; simplify coil turns, wedge chips, hook bevels, peg bands, and underside surfaces.
- LOD3: 15-25 percent of LOD0; preserve the low path-edge silhouette, rope mass, wedge read, peg/bucket read, and red/dark material blocks.

Do not reduce the path-lane silhouette before removing small texture-only detail.

## 11. Collision Notes

Future collision should use simple display collision: one or more low-count hulls around the coil, wedge stack, peg/bucket, and hook set. Collision must not become a path blocker or nav rule.

Do not define nav blockers, pathfinding volumes, encounter cover, trap collision, pickup collision, loot outlines, resource triggers, workstation volumes, destructible collision, collision proxies, startup placement collision, or gameplay traces in this task.

## 12. Animation Notes

Static mesh baseline. No animation, physics simulation, rope simulation, cloth motion, hanging motion, material-state timing, VFX, audio, player interaction, NPC work loop, pickup behavior, loot state, nav behavior, encounter behavior, or startup behavior is authored here.

## 13. Unreal Import Notes

Planned asset type if later approved: Static Mesh.

Planned folder: `/Game/Aerathea/Props/Giants/BloodAxeCamp/UtilityClusters/`

Planned import name: `SM_GIA_BloodAxePathEdgeUtilityCluster_A01`

Pivot: ground center of the path-edge footprint, aligned so the long axis can sit parallel to camp paths. Import scale: 1.0 cm. Collision: simple display collision only. LODs: LOD0-LOD3 required. Material slots: 2 target, 3 maximum.

This package does not create Unreal assets, nav/pathfinding behavior, encounter behavior, material instances, validators, captures, startup placement, runtime source, Blueprint behavior, or final visual signoff.

## 14. Folder and Naming Recommendation

- Docs folder: `docs/assets/props/SM_GIA_BloodAxePathEdgeUtilityCluster_A01/`
- Production package: `docs/assets/props/SM_GIA_BloodAxePathEdgeUtilityCluster_A01/PRODUCTION_PACKAGE.md`
- Future mesh name: `SM_GIA_BloodAxePathEdgeUtilityCluster_A01`
- Future texture prefix: `T_GIA_BloodAxePathEdgeUtilityCluster_A01`

Do not add SourceAssets, FBX exports, Unreal Content, Tools/DCC, Tools/Unreal, runtime source, validators, captures, global indexes, task board updates, material instances, nav data, or startup scene files from this package.

## 15. Quality Gate Checklist

- Uses the universal 15-section Aerathea package format.
- Remains docs-only with no-DCC/no-Unreal/no-startup/no-nav/no-encounter/no-workstation/no-loot/no-resource/no-material-instance/no-validator/no-capture/no-final-signoff/no-implementation-target guardrails.
- Preserves female Giant 442 cm / 14'6" and male Giant 470 cm / 15'5" scale lock.
- Keeps Blood Axe as a hostile Giant sub-faction separate from neutral/civilized Giant culture.
- Defines a low path-edge cluster that preserves Giant-scale visual lanes.
- Includes material, texture, triangle, LOD, collision, animation, Unreal planning, folder, and naming notes.
- Does not claim pathfinding, encounter, runtime, shipped content, final approval, or first DCC target selection.
