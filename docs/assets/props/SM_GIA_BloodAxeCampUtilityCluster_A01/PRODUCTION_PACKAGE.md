# SM_GIA_BloodAxeCampUtilityCluster_A01 Production Package

## 1. Art Direction Summary

- Asset name: `SM_GIA_BloodAxeCampUtilityCluster_A01`
- Asset type: Static Mesh production package, docs-only
- Parent kit: `KIT_GIA_BloodAxeCampTools_A01`
- Child intake row: `BloodAxeCamp.png#CampTools_UtilityCluster_Small_A01`
- Faction/theme: Blood Axe Tribe, hostile Giant sub-faction only
- Status: package-ready planning document; no implementation target selected

This cluster is a low, sparse composition of one battered Giant-scale bucket or carry tub, one thick rope coil, two or three blunt wedges, one heavy mallet, sparse hooks, and minor tie hardware. It should read as rough camp utility dressing for hostile Blood Axe raiders, not as neutral/civilized Giant craft culture.

Blood Axe visual language must stay separate from neutral/civilized Giant culture. Use soot-black utility gear, dull red faction ties, mud, ash, hide, and brutal field-made construction. Do not import refined highland masonry, peaceful cave-town stoneworker identity, warm hearth presentation, restrained blue runes, or civic Giant settlement language.

Guardrails: no-DCC, no-Unreal, no-startup, no-nav, no-encounter, no-workstation, no-loot, no-resource, no-material-instance, no-validator, no-capture, no-final-signoff, no-implementation-target.

## 2. Gameplay Purpose

This is non-interactive environmental dressing for Blood Axe camp interiors and open utility spaces. It reinforces hostile Giant scale and rough camp maintenance without creating gameplay affordances.

It may support visual storytelling beside shelters, gates, paths, and general camp work lanes. It must not define usable workstation behavior, pickup behavior, crafting behavior, resource behavior, economy behavior, salvage behavior, loot behavior, NPC routines, nav/pathfinding behavior, encounter behavior, objective logic, startup placement, or runtime gameplay.

## 3. Silhouette Notes

The silhouette should be broad, low, and readable from an MMO camera. Keep the composition around 250-600 cm wide, with clear air between the bucket, rope coil, wedge stack, mallet, and hooks. The cluster should look heavy enough for Giant hands while staying low enough to preserve camp sightlines.

Model the bucket body, bucket rim, major handle, rope coil mass, large knot, wedge bodies, mallet head, mallet shaft, hook curves, and large tie rings as future geometry. Keep rope fiber, tiny chips, soot speckles, scratches, pitting, stitch lines, and small red paint wear in future texture or normal detail.

Avoid dense tool scatter, human-scale pails, polished workshop order, treasure reads, glow rings, UI markers, quest markers, loot beams, graphic gore, or decorative clutter that competes with primary camp architecture.

## 4. Scale Notes

Use the validated Giant scale lock:

- Female Giant baseline: 442 cm / 14'6".
- Male Giant baseline: 470 cm / 15'5".
- Approved Giant ranges: females 14-15 ft / 427-457 cm; males 14'10"-16'0" / 452-488 cm.
- Author in centimeters. 1 Unreal unit = 1 cm.

Suggested cluster scale: 250-600 cm wide, 180-420 cm deep, and 80-220 cm tall. Bucket or tub diameter should sit near 90-180 cm, rope coil diameter near 120-260 cm, mallet length near 140-260 cm, and wedges near 50-140 cm long. Do not shrink the cluster into ordinary humanoid camp clutter.

## 5. Materials and Color Palette

Use blackened iron, dark steel, scorched timber, rough bucket boards, thick rope, hide lashings, scorched leather, dull Blood Axe red cloth ties, chipped red paint, soot, ash, mud, grime, and sparse non-graphic bone or horn spacers.

Avoid neutral/civilized Giant blue-gray carved stone, refined stoneworker tools, warm hearth tones, clean highland craft, restrained blue runes, storm glow, default emissive, bright treasure metal, or high-saturation red coverage.

## 6. Concept Image Prompt

Create an original stylized fantasy MMORPG concept image of `SM_GIA_BloodAxeCampUtilityCluster_A01` for the world of Aerathea. The design should emphasize a low sparse hostile Giant camp utility cluster, one battered bucket or carry tub, one thick rope coil, blunt wedges, a massive mallet, sparse blackened hooks, tie hardware, soot-dark wood, dark steel, hide lashings, mud, ash, dull Blood Axe red cloth ties, hostile raider camp identity, female Giant scale 442 cm / 14'6", male Giant scale 470 cm / 15'5", and a gameplay role as static non-interactive camp dressing. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, no default emissive glow, and MMO-friendly production design. Present it as a clean production asset board on a neutral background with front, side, top, scale callouts, material swatches, LOD notes, and collision notes. Avoid copying any existing franchise and avoid excessive micro-detail that would not translate to a mid-poly Unreal asset.

## 7. Modeling Notes

Future DCC work should build this as a composed static mesh assembled from reusable camp-tools child forms. Keep the footprint irregular but path-safe, with no tall central obstruction and no dense pile of small tools.

Use real geometry for the bucket/tub body, thick rim, main handle, rope coil volume, main knot, wedge masses, mallet head and shaft, large hooks, big rings, and cluster ground-contact forms. Use texture and normal detail for rope fiber, fray, wood grain, soot, scratches, pitting, small rivets, leather stitching, mud flecks, and chipped red paint.

Do not author DCC source, FBX, collision proxy, proof render, Unreal Content, Blueprint, sockets, material instance, validator, capture setup, startup actor, or implementation target from this package.

## 8. Texture and Material Notes

Future texture set:

- `T_GIA_BloodAxeCampUtilityCluster_A01_BC`
- `T_GIA_BloodAxeCampUtilityCluster_A01_N`
- `T_GIA_BloodAxeCampUtilityCluster_A01_ORM`

Baseline uses no emissive map. Target 1K-2K for the composed cluster. Use 2 material slots target, 3 maximum only if wood/rope/hide and metal separation cannot remain readable. Do not create a material instance in this task; this package is docs-only.

## 9. Triangle Budget

Target LOD0: 5k-14k tris for the composed cluster.

Target material slots: 2, with 3 maximum only if needed for readability. Child source forms should remain efficient enough for reuse across other Blood Axe utility clusters.

## 10. LOD Plan

- LOD0: full bucket/tub, rope coil, knot, hooks, wedges, mallet, tie rings, red ties, and cluster footprint.
- LOD1: 60-70 percent of LOD0; reduce bevels, extra coil turns, minor handle cuts, duplicate ties, and backside details.
- LOD2: 35-45 percent of LOD0; simplify bucket interior, rope turns, hook bevels, wedge chips, mallet wraps, and underside surfaces.
- LOD3: 15-25 percent of LOD0; preserve bucket/tub read, coil mass, wedge triangular read, mallet head, hook curve, and overall footprint.

Remove tiny surface details before reducing the main silhouette.

## 11. Collision Notes

Future collision should be display-only: grouped simple boxes or low-count convex hulls around the bucket/tub, coil mass, mallet, wedge stack, and major hook set. No per-rope, per-hook, per-link, or per-tool collision.

Do not define pickup collision, workstation volumes, resource triggers, economy triggers, loot outlines, nav blockers, encounter cover volumes, damage traces, destructible collision, startup placement collision, or collision proxies in this task.

## 12. Animation Notes

Static mesh baseline. No animation, physics simulation, rope simulation, hanging motion, tool swing, bucket carry state, NPC work cycle, material-state timing, VFX, audio, interaction prompt, pickup behavior, workstation behavior, loot state, or startup behavior is authored here.

## 13. Unreal Import Notes

Planned asset type if later approved: Static Mesh.

Planned folder: `/Game/Aerathea/Props/Giants/BloodAxeCamp/UtilityClusters/`

Planned import name: `SM_GIA_BloodAxeCampUtilityCluster_A01`

Pivot: ground center of full cluster footprint. Import scale: 1.0 cm. Collision: simple display collision only. LODs: LOD0-LOD3 required. Material slots: 2 target, 3 maximum.

This package does not create Unreal assets, material instances, validators, captures, startup placement, Blueprint behavior, runtime source, nav behavior, encounter behavior, or final visual signoff.

## 14. Folder and Naming Recommendation

- Docs folder: `docs/assets/props/SM_GIA_BloodAxeCampUtilityCluster_A01/`
- Production package: `docs/assets/props/SM_GIA_BloodAxeCampUtilityCluster_A01/PRODUCTION_PACKAGE.md`
- Future mesh name: `SM_GIA_BloodAxeCampUtilityCluster_A01`
- Future material instance name, if separately approved: `MI_GIA_BloodAxeCampUtility_A01`

Do not add SourceAssets, FBX exports, Unreal Content, Tools/DCC, Tools/Unreal, runtime source, validators, captures, global indexes, task board updates, material instances, or startup scene files from this package.

## 15. Quality Gate Checklist

- Uses the universal 15-section Aerathea package format.
- Remains docs-only with no-DCC/no-Unreal/no-startup/no-nav/no-encounter/no-workstation/no-loot/no-resource/no-material-instance/no-validator/no-capture/no-final-signoff/no-implementation-target guardrails.
- Preserves female Giant 442 cm / 14'6" and male Giant 470 cm / 15'5" scale lock.
- Keeps Blood Axe as a hostile Giant sub-faction separate from neutral/civilized Giant culture.
- Defines a low, sparse, readable camp utility cluster.
- Includes material, texture, triangle, LOD, collision, animation, Unreal planning, folder, and naming notes.
- Does not claim final visual approval, implementation readiness, runtime behavior, shipped content, source concept approval, or first DCC target selection.
