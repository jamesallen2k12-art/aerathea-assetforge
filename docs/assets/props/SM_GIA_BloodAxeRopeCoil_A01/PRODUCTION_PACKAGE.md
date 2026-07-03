# SM_GIA_BloodAxeRopeCoil_A01 Production Package

## 1. Art Direction Summary

- Asset name: `SM_GIA_BloodAxeRopeCoil_A01`
- Asset type: Static Mesh prop planning package
- Parent kit: `KIT_GIA_BloodAxeCampTools_A01`
- Intake row: `BloodAxeCamp.png#CampTools_RopeCoil_Large_A01`
- Faction/theme: Blood Axe Tribe, hostile Giant sub-faction only
- Status: docs-only production package ready

Large thick rope coil for Blood Axe camp dressing. The prop should read as massive, rough, muddy, and useful to hostile Giant raiders while remaining inert set dressing. Blood Axe remains a hostile Giant sub-faction separate from neutral/civilized Giant culture.

Guardrails: no DCC, no FBX, no Unreal Content, no runtime source, no validator, no source concept movement, no first DCC target, no implementation target, no rope physics, no climbing, no tripwire, no trap, no pickup, no loot, no resource, no workstation, no interaction, no nav/pathfinding, no final visual approval.

## 2. Gameplay Purpose

Static non-interactive rope dressing for camp floors, shelter edges, gate support areas, and utility clusters. It provides scale, material contrast, and camp utility storytelling only. It is not a climbable rope, simulated rope, trap component, tripwire, pickup, resource node, crafting ingredient, workstation part, loot object, nav/pathfinding device, or interaction target.

## 3. Silhouette Notes

Use a broad circular or oval coil with thick rope turns, one large knot or tied hide band, visible rope end, and muddy flattened underside. The silhouette should read from a distance through mass and loop rhythm, not dense fiber detail. Avoid dense micro-strands, thin human-scale rope, glowing interaction markers, tripwire lines, trap teeth, climb affordances, and refined civilized Giant craft.

## 4. Scale Notes

- Female Giant scale lock: 442 cm / 14'6".
- Male Giant scale lock: 470 cm / 15'5".
- Approved Giant range remains females 14-15 ft / 427-457 cm and males 14'10"-16'0" / 452-488 cm.
- Author in centimeters; 1 Unreal unit = 1 cm.
- Target coil diameter: 120-260 cm.
- Target coil thickness: 25-70 cm.
- Knot or tie loop: 25-55 cm.
- Rope strand thickness: 12-28 cm, stylized and readable.

## 5. Materials and Color Palette

Primary materials: thick dirty rope, mud-stained fiber, hide tie, soot, ash, oil-dark grime, darkened rope ends, and optional dull Blood Axe red cloth tie. Avoid blue-gray civilized Giant stone, refined peaceful highland craft, blue runes, magic glow, forge glow, bright dyed rope, and default emissive.

## 6. Concept Image Prompt

Create an original stylized fantasy MMORPG concept image of `SM_GIA_BloodAxeRopeCoil_A01` for the world of Aerathea. The design should emphasize a massive thick Blood Axe Giant rope coil, broad readable rope turns, large knot, hide tie, muddy underside, soot and ash stains, dull red cloth accent, hostile raider camp identity, female Giant scale 442 cm / 14'6", male Giant scale 470 cm / 15'5", and a gameplay role as static non-interactive camp dressing. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, no emissive glow, and MMO-friendly production design. Present it as a single prop concept sheet with top, side, scale callout, material swatches, LOD notes, and collision notes. Avoid copying any existing franchise, avoid neutral/civilized Giant culture, avoid dense rope micro-strands, avoid rope physics, avoid climbing/tripwire/trap language, avoid pickup/resource/workstation diagrams, and avoid interaction prompts.

## 7. Modeling Notes

Model simplified rope coil volumes, major rope turns, rope ends, the large knot, and the hide tie as geometry. Use enough coil separation to read the form without modeling individual fibers. Texture and normals handle fiber twist, fray, dirt, soot, small cuts, cloth weave, and mud. Do not define rope simulation, per-segment rigging, climb points, trap endpoints, tripwire lines, physics constraints, sockets, or gameplay affordances.

## 8. Texture and Material Notes

Required future map set: `BC`, `N`, and packed `ORM`. No emissive map for baseline `A01`.

Texture names:

- `T_GIA_BloodAxeRopeCoil_A01_BC`
- `T_GIA_BloodAxeRopeCoil_A01_N`
- `T_GIA_BloodAxeRopeCoil_A01_ORM`

Material target: 1 material slot. Use 512-1K textures for repeated coils; 2K only if approved for a close camp hero arrangement. Fiber, fray, weave, and small mud flecks must be texture/normal detail.

## 9. Triangle Budget

- LOD0 target: 1.5k-5k tris.
- LOD1 target: 900-3.2k tris.
- LOD2 target: 450-1.9k tris.
- LOD3 target: 220-950 tris.
- Material slots: 1 preferred, 2 maximum only if a hide tie requires separation.

## 10. LOD Plan

- LOD0: full coil mass, major rope turns, knot, rope ends, tie band, and flattened underside.
- LOD1: reduce coil turn subdivisions, knot bevels, rope-end cuts, tie folds, and underside detail.
- LOD2: merge secondary turns, simplify knot geometry, reduce rope-end silhouette, and flatten fray into normals.
- LOD3: preserve coil footprint, thick rope ring read, knot block, and mud/dull red material accents.

Remove fiber strands, fray, cloth weave, soot speckles, mud flecks, and small cuts before reducing the main coil silhouette.

## 11. Collision Notes

Planned display collision only: one low cylinder-like or convex hull around the coil footprint. No per-rope collision and no per-knot collision. No rope physics collision, no climb collision, no tripwire trigger, no trap trigger, no pickup collision, no resource trigger, no workstation volume, no interaction volume, no nav blocker, no pathfinding device, no damage trace, no physics constraint, and no destructible collision.

## 12. Animation Notes

Static mesh baseline. No animation, no rope simulation, no physics simulation, no cloth simulation, no hanging motion, no uncoiling state, no climbing state, no tripwire or trap state, no pickup behavior, no resource behavior, no workstation behavior, no crafting loop, no interaction prompt, no VFX, no audio, and no startup-scene behavior.

## 13. Unreal Import Notes

Planning notes only; this task does not create Unreal assets or import content.

- Planned asset type: Static Mesh.
- Planned folder: `/Game/Aerathea/Props/Giants/BloodAxeCamp/CampTools/`
- Planned mesh: `SM_GIA_BloodAxeRopeCoil_A01`
- Planned material: `MI_GIA_BloodAxeRopeHide_A01`
- Pivot: ground center of coil footprint.
- Scale: import at 1.0, authored in centimeters.
- LODs: LOD0-LOD3 required.
- Collision: simple display-only hull.
- Sockets: none.
- Blueprint behavior: none.
- Performance: static dressing only; no Blueprint Actor, gameplay component, rope component, climb component, trap logic, pickup item, resource data, interaction volume, nav behavior, runtime source, validator, or startup placement.

## 14. Folder and Naming Recommendation

- Package path: `docs/assets/props/SM_GIA_BloodAxeRopeCoil_A01/PRODUCTION_PACKAGE.md`
- Future source folder, if separately approved: `SourceAssets/Props/Giants/BloodAxeCamp/CampTools/SM_GIA_BloodAxeRopeCoil_A01/`
- Future texture prefix: `T_GIA_BloodAxeRopeCoil_A01`
- Future material instance: `MI_GIA_BloodAxeRopeHide_A01`

Do not create source folders, DCC files, FBX files, Unreal Content, global index edits, task board edits, Hermes files/config, material graphs, shaders, VFX, audio, runtime source, rope simulation assets, or implementation artifacts from this package.

## 15. Quality Gate Checklist

- Original Aerathea Blood Axe hostile Giant sub-faction prop, not neutral/civilized Giant culture.
- Giant scale lock preserved: female 442 cm / 14'6" and male 470 cm / 15'5".
- Static camp dressing only; no rope physics, climbing, tripwire, trap, pickup, loot, resource, workstation, interaction, nav/pathfinding, or economy behavior.
- Silhouette readable as a massive thick Giant rope coil.
- Materials stay in dirty rope, hide, soot, ash, mud, grime, and restrained dull red accents.
- Fiber, fray, weave, small cuts, soot, and mud are texture/normal detail.
- LOD0-LOD3, collision, texture maps, material slots, pivot, scale, and Unreal import planning are documented.
- No DCC, FBX, Unreal, runtime, validator, source concept, global index, task board, Hermes, implementation target, or final visual approval work is included.
