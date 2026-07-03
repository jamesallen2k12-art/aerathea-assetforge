# SM_GIA_BloodAxeShelterEdgeUtilityCluster_A01 Production Package

## 1. Art Direction Summary

- Asset name: `SM_GIA_BloodAxeShelterEdgeUtilityCluster_A01`
- Asset type: Static Mesh production package, docs-only
- Parent kit: `KIT_GIA_BloodAxeCampTools_A01`
- Child intake row: `BloodAxeShelter.png#CampTools_UtilityCluster_ShelterEdge_A01`
- Faction/theme: Blood Axe Tribe, hostile Giant sub-faction only
- Status: package-ready planning document; no implementation target selected

This cluster is shelter-edge dressing made from a rope coil, hanging hook rail language, battered bucket, mallet pair, hide ties, soot, mud, and dull red identifiers. It should sit near Blood Axe shelters as rough static utility clutter without implying shelter interaction, NPC routines, cloth physics, pickup behavior, or workstation behavior.

Blood Axe must remain a hostile Giant sub-faction separate from neutral/civilized Giant culture. Avoid refined highland home craft, peaceful cave-town domestic tools, warm hearth comfort, blue-gray civic masonry, restrained blue runes, and neutral Giant settlement identity.

Guardrails: no-DCC, no-Unreal, no-startup, no-nav, no-encounter, no-workstation, no-loot, no-resource, no-material-instance, no-validator, no-capture, no-final-signoff, no-implementation-target.

## 2. Gameplay Purpose

This asset provides static shelter-edge set dressing and Giant-scale visual context. It should make shelters feel occupied by hostile Blood Axe raiders without creating interactive storage, tool pickup, sleeping, shelter, crafting, resource, economy, loot, NPC, nav, encounter, or startup behavior.

It remains visual-only and non-shipping until a later approved implementation task exists.

## 3. Silhouette Notes

The silhouette should lean slightly vertical at the hook rail or leaned mallets while remaining mostly low and edge-safe. Combine a thick rope coil, bucket or tub, two leaned or crossed mallets, sparse hook rail, and broad hide ties with clear negative space.

Model the rope coil mass, bucket body, major handles, mallet heads and shafts, hook rail bar, hook curves, and large tie rings as future geometry. Keep rope fibers, cloth weave, fray, stitching, scratches, soot, mud, and chipped red paint as future texture or normal detail.

Avoid readable storage chests, bedroll interaction, shelter door logic, hanging physics, cloth simulation, pickup outlines, UI markers, loot piles, or dense domestic clutter.

## 4. Scale Notes

Use the validated Giant scale lock:

- Female Giant baseline: 442 cm / 14'6".
- Male Giant baseline: 470 cm / 15'5".
- Approved Giant ranges: females 14-15 ft / 427-457 cm; males 14'10"-16'0" / 452-488 cm.
- Author in centimeters. 1 Unreal unit = 1 cm.

Suggested footprint: 250-650 cm wide, 160-380 cm deep, and 100-260 cm tall if hook rail or leaned mallets are included. Rope coil diameter should be 120-240 cm, mallets 140-260 cm long, and buckets/tubs 90-170 cm across. Keep all elements readable beside 442 cm and 470 cm Giants.

## 5. Materials and Color Palette

Use scorched timber, rough bucket boards, blackened iron, dark steel, thick rope, hide lashings, scorched leather, dirty cloth ties, dull Blood Axe red, chipped red paint, soot, ash, mud, and grime.

Avoid warm domestic hearth presentation, clean shelter props, civilized Giant blue-gray stone, refined tools, bright cloth, default emissive, blue runes, and excessive red coverage.

## 6. Concept Image Prompt

Create an original stylized fantasy MMORPG concept image of `SM_GIA_BloodAxeShelterEdgeUtilityCluster_A01` for the world of Aerathea. The design should emphasize a hostile Giant shelter-edge utility cluster, thick rope coil, sparse hook rail, battered bucket, two heavy mallets, hide ties, scorched timber, blackened iron, mud, soot, dull Blood Axe red cloth ties, no interaction affordances, female Giant scale 442 cm / 14'6", male Giant scale 470 cm / 15'5", and a gameplay role as static non-interactive shelter-edge dressing. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, no default emissive glow, and MMO-friendly production design. Present it as a clean production asset board with front, side, top footprint, scale callouts, material swatches, LOD notes, and collision notes. Avoid copying any existing franchise and avoid excessive micro-detail that would not translate to a mid-poly Unreal asset.

## 7. Modeling Notes

Future modeling should compose the asset to sit against shelter edges without requiring shelter-specific sockets or startup placement. Keep the hook rail sparse and chunky; do not model dense small hooks or hanging soft goods.

Use real geometry for rope coil volume, bucket/tub body, thick rim, major handles, mallet heads and shafts, hook rail, large hooks, and tie rings. Use texture and normal detail for rope fiber, fray, leather stitching, cloth weave, wood grain, soot, scratches, pitting, mud flecks, and chipped paint.

Do not create DCC source, FBX, collision proxy, proof render, Unreal Content, Blueprint, sockets, material instance, validator, capture setup, startup actor, cloth physics, shelter interaction, or implementation target from this package.

## 8. Texture and Material Notes

Future texture set:

- `T_GIA_BloodAxeShelterEdgeUtilityCluster_A01_BC`
- `T_GIA_BloodAxeShelterEdgeUtilityCluster_A01_N`
- `T_GIA_BloodAxeShelterEdgeUtilityCluster_A01_ORM`

No emissive map is planned. Target 1K-2K. Material slots: 2 target, 3 maximum if needed. Tie cloth and chipped red paint should remain accents within shared material work, not separate high-cost material slots.

## 9. Triangle Budget

Target LOD0: 5k-13k tris.

Target material slots: 2, with 3 maximum only if needed. Keep hook rail and mallet pair simple enough that shelter edges can use several variants without cluttering the scene.

## 10. LOD Plan

- LOD0: full rope coil, bucket/tub, mallet pair, hook rail, hooks, large ties, red accents, and shelter-edge footprint.
- LOD1: 60-70 percent of LOD0; reduce bevels, hook subdivisions, extra coil turns, tie loops, and backside detail.
- LOD2: 35-45 percent of LOD0; simplify coil turn count, hook rail, mallet wraps, bucket interior, and underside surfaces.
- LOD3: 15-25 percent of LOD0; preserve rope mass, bucket read, mallet pair silhouette, hook rail read, and overall footprint.

Remove tiny texture-level detail before reducing the shelter-edge silhouette.

## 11. Collision Notes

Future collision should use simple display hulls around the coil, bucket/tub, mallet pair, and hook rail. If placed near shelters later, collision must stay separate from shelter gameplay or doorway logic.

Do not define shelter interaction, NPC routine volumes, pickup collision, workstation volumes, resource triggers, loot outlines, nav blockers, encounter cover, cloth physics collision, destructible collision, collision proxies, startup placement collision, or gameplay traces in this task.

## 12. Animation Notes

Static mesh baseline. No animation, physics simulation, hanging motion, cloth physics, rope simulation, mallet use, bucket carry state, NPC shelter routine, material-state timing, VFX, audio, pickup behavior, workstation behavior, loot state, nav behavior, encounter behavior, or startup behavior is authored here.

## 13. Unreal Import Notes

Planned asset type if later approved: Static Mesh.

Planned folder: `/Game/Aerathea/Props/Giants/BloodAxeCamp/UtilityClusters/`

Planned import name: `SM_GIA_BloodAxeShelterEdgeUtilityCluster_A01`

Pivot: ground center of full footprint, with local forward aligned for predictable shelter-edge placement in a later approved task. Import scale: 1.0 cm. Collision: simple display collision only. LODs: LOD0-LOD3 required. Material slots: 2 target, 3 maximum.

This package does not create Unreal assets, material instances, validators, captures, startup placement, Blueprint behavior, runtime source, shelter interaction, NPC behavior, cloth physics, or final visual signoff.

## 14. Folder and Naming Recommendation

- Docs folder: `docs/assets/props/SM_GIA_BloodAxeShelterEdgeUtilityCluster_A01/`
- Production package: `docs/assets/props/SM_GIA_BloodAxeShelterEdgeUtilityCluster_A01/PRODUCTION_PACKAGE.md`
- Future mesh name: `SM_GIA_BloodAxeShelterEdgeUtilityCluster_A01`
- Future texture prefix: `T_GIA_BloodAxeShelterEdgeUtilityCluster_A01`

Do not add SourceAssets, FBX exports, Unreal Content, Tools/DCC, Tools/Unreal, runtime source, validators, captures, global indexes, task board updates, material instances, cloth physics assets, or startup scene files from this package.

## 15. Quality Gate Checklist

- Uses the universal 15-section Aerathea package format.
- Remains docs-only with no-DCC/no-Unreal/no-startup/no-nav/no-encounter/no-workstation/no-loot/no-resource/no-material-instance/no-validator/no-capture/no-final-signoff/no-implementation-target guardrails.
- Preserves female Giant 442 cm / 14'6" and male Giant 470 cm / 15'5" scale lock.
- Keeps Blood Axe as a hostile Giant sub-faction separate from neutral/civilized Giant culture.
- Defines static shelter-edge dressing without shelter interaction, NPC routines, cloth physics, pickup behavior, or workstation claims.
- Includes material, texture, triangle, LOD, collision, animation, Unreal planning, folder, and naming notes.
- Does not claim final visual approval, implementation readiness, runtime behavior, shipped content, or first DCC target selection.
