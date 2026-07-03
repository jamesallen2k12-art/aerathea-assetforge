# SM_GIA_BloodAxeTieDownRopeCoil_A01 Production Package

## 1. Art Direction Summary

- Asset name: `SM_GIA_BloodAxeTieDownRopeCoil_A01`
- Asset type: Static Mesh prop planning package
- Parent kit: `KIT_GIA_BloodAxeCampTools_A01`
- Intake row: `BloodAxeGate.png#CampTools_RopeCoil_TieDown_A01`
- Faction/theme: Blood Axe Tribe, hostile Giant sub-faction only
- Status: docs-only production package ready

Rope coil variant with heavy tie loop, ring, or stake-anchor language for Blood Axe gates, shelters, and banner-line support dressing. It must read as visual tie-down equipment only, not functional gate logic or rope gameplay. Blood Axe remains a hostile Giant sub-faction separate from neutral/civilized Giant culture.

Guardrails: no DCC, no FBX, no Unreal Content, no runtime source, no validator, no source concept movement, no first DCC target, no implementation target, no rope physics, no climbing, no tripwire, no trap, no gate behavior, no pickup, no loot, no resource, no workstation, no interaction, no nav/pathfinding, no final visual approval.

## 2. Gameplay Purpose

Static non-interactive visual support prop for gates, shelter edges, perimeter dressing, and banner-line areas. It communicates crude tie-down utility at Giant scale without defining gate operation, rope simulation, trap use, climbing, pickup, resource, crafting, workstation, interaction, or nav/pathfinding behavior.

## 3. Silhouette Notes

Use a rope coil with a pronounced tie loop, oversized dark metal ring or stake anchor, thick knot, and short heavy rope tail. The anchor silhouette should differentiate this from the plain rope coil. Keep the anchor broad and readable. Avoid trap spikes, tripwire layout, climbable dangling rope, moving pulley language, polished hardware, and refined civilized Giant craft.

## 4. Scale Notes

- Female Giant scale lock: 442 cm / 14'6".
- Male Giant scale lock: 470 cm / 15'5".
- Approved Giant range remains females 14-15 ft / 427-457 cm and males 14'10"-16'0" / 452-488 cm.
- Author in centimeters; 1 Unreal unit = 1 cm.
- Target coil diameter: 130-260 cm.
- Target coil thickness: 30-75 cm.
- Tie loop or knot: 35-70 cm.
- Ring or stake anchor: 45-120 cm depending on variant.

## 5. Materials and Color Palette

Primary materials: dirty thick rope, hide ties, blackened iron ring or stake hardware, dark steel plate accents, mud, ash, soot, oil grime, and restrained dull Blood Axe red cloth. Avoid blue-gray civilized Giant stone, warm hearth craft, blue runes, magic glow, active forge glow, bright rope dye, and default emissive.

## 6. Concept Image Prompt

Create an original stylized fantasy MMORPG concept image of `SM_GIA_BloodAxeTieDownRopeCoil_A01` for the world of Aerathea. The design should emphasize a Giant-scale Blood Axe tie-down rope coil, thick readable rope turns, heavy tie loop, oversized blackened iron ring or stake anchor, large knot, muddy underside, soot, ash, dull red cloth tie, hostile raider camp identity, female Giant scale 442 cm / 14'6", male Giant scale 470 cm / 15'5", and a gameplay role as static non-interactive camp dressing. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, no emissive glow, and MMO-friendly production design. Present it as a prop concept sheet with top, side, scale callout, material swatches, LOD notes, and collision notes. Avoid copying any existing franchise, avoid neutral/civilized Giant culture, avoid rope physics, avoid climbing/tripwire/trap/gate logic, avoid pickup/resource/workstation diagrams, and avoid interaction prompts.

## 7. Modeling Notes

Model the coil mass, major rope turns, tie loop, knot, rope tail, and anchor hardware as geometry. Keep the ring or stake oversized with simple hammered forms. Use texture and normals for fiber twist, fray, rope cuts, iron pitting, soot, mud, small scratches, and chipped red paint. Do not define rigged rope, physics constraints, climb points, tripwire endpoints, gate sockets, trap triggers, moving hardware, or gameplay affordances.

## 8. Texture and Material Notes

Required future map set: `BC`, `N`, and packed `ORM`. No emissive map for baseline `A01`.

Texture names:

- `T_GIA_BloodAxeTieDownRopeCoil_A01_BC`
- `T_GIA_BloodAxeTieDownRopeCoil_A01_N`
- `T_GIA_BloodAxeTieDownRopeCoil_A01_ORM`

Material target: 1-2 slots. Slot 0 covers rope, hide, grime, and red tie; optional slot 1 covers shared blackened metal ring or stake hardware. Use 512-1K textures for repeated dressing; 2K only with later hero approval.

## 9. Triangle Budget

- LOD0 target: 2k-6k tris.
- LOD1 target: 1.2k-3.8k tris.
- LOD2 target: 600-2.2k tris.
- LOD3 target: 300-1.1k tris.
- Material slots: 1 preferred, 2 maximum.

## 10. LOD Plan

- LOD0: full coil mass, tie loop, knot, rope tail, ring or stake anchor, and red tie.
- LOD1: reduce rope turn subdivisions, ring bevels, stake bevels, knot cuts, and tie folds.
- LOD2: merge secondary coil turns, simplify anchor hardware, reduce rope tail detail, and flatten fray into normals.
- LOD3: preserve coil footprint, tie-down loop read, anchor block, and dark metal/dull red material accents.

Remove fiber strands, fray, pitting, small scratches, soot speckles, chipped paint, mud flecks, and cloth weave before reducing the main coil, loop, or anchor silhouette.

## 11. Collision Notes

Planned display collision only: one low convex hull around the coil plus a simple hull for the large ring or stake if needed for placement. No per-rope, per-knot, or per-ring collision. No rope physics collision, no climb collision, no tripwire trigger, no trap trigger, no gate trigger, no pickup collision, no resource trigger, no workstation volume, no interaction volume, no nav blocker, no pathfinding device, no physics constraint, no damage trace, and no destructible collision.

## 12. Animation Notes

Static mesh baseline. No animation, no rope simulation, no physics simulation, no cloth simulation, no hanging motion, no uncoiling state, no gate operation, no climbing state, no tripwire or trap state, no pickup behavior, no resource behavior, no workstation behavior, no crafting loop, no interaction prompt, no VFX, no audio, and no startup-scene behavior.

## 13. Unreal Import Notes

Planning notes only; this task does not create Unreal assets or import content.

- Planned asset type: Static Mesh.
- Planned folder: `/Game/Aerathea/Props/Giants/BloodAxeCamp/CampTools/`
- Planned mesh: `SM_GIA_BloodAxeTieDownRopeCoil_A01`
- Planned material: `MI_GIA_BloodAxeRopeHide_A01` with optional `MI_GIA_BloodAxeReforgedMetal_A01`
- Pivot: ground center of full coil and anchor footprint.
- Scale: import at 1.0, authored in centimeters.
- LODs: LOD0-LOD3 required.
- Collision: simple display-only hulls.
- Sockets: none.
- Blueprint behavior: none.
- Performance: static dressing only; no Blueprint Actor, gameplay component, rope component, gate behavior, climb component, trap logic, pickup item, resource data, interaction volume, nav behavior, runtime source, validator, or startup placement.

## 14. Folder and Naming Recommendation

- Package path: `docs/assets/props/SM_GIA_BloodAxeTieDownRopeCoil_A01/PRODUCTION_PACKAGE.md`
- Future source folder, if separately approved: `SourceAssets/Props/Giants/BloodAxeCamp/CampTools/SM_GIA_BloodAxeTieDownRopeCoil_A01/`
- Future texture prefix: `T_GIA_BloodAxeTieDownRopeCoil_A01`
- Future material instances: `MI_GIA_BloodAxeRopeHide_A01`, `MI_GIA_BloodAxeReforgedMetal_A01`

Do not create source folders, DCC files, FBX files, Unreal Content, global index edits, task board edits, Hermes files/config, material graphs, shaders, VFX, audio, runtime source, rope simulation assets, gate logic, or implementation artifacts from this package.

## 15. Quality Gate Checklist

- Original Aerathea Blood Axe hostile Giant sub-faction prop, not neutral/civilized Giant culture.
- Giant scale lock preserved: female 442 cm / 14'6" and male 470 cm / 15'5".
- Static camp dressing only; no rope physics, climbing, tripwire, trap, gate behavior, pickup, loot, resource, workstation, interaction, nav/pathfinding, or economy behavior.
- Silhouette readable as a massive tie-down rope coil with anchor hardware.
- Materials stay in dirty rope, hide, blackened iron, soot, ash, mud, grime, and restrained dull red accents.
- Fiber, fray, pitting, scratches, chipped paint, soot, and mud are texture/normal detail.
- LOD0-LOD3, collision, texture maps, material slots, pivot, scale, and Unreal import planning are documented.
- No DCC, FBX, Unreal, runtime, validator, source concept, global index, task board, Hermes, implementation target, or final visual approval work is included.
