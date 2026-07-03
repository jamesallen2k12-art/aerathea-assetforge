# KIT_GIA_BloodAxeRopeBundleSet_A01 Production Package

## 1. Art Direction Summary

- Asset name: `KIT_GIA_BloodAxeRopeBundleSet_A01`
- Asset type: Static Mesh kit planning package
- Parent kit: `KIT_GIA_BloodAxeCampTools_A01`
- Intake row: `Blood Axe Village.png#CampTools_RopeBundle_Spare_A01`
- Faction/theme: Blood Axe Tribe, hostile Giant sub-faction only
- Status: docs-only production package ready

Small set of spare Blood Axe rope bundles, tied lengths, knots, and coil variants for repeated camp dressing. The kit should provide reusable static pieces and low composed arrangements without becoming rope gameplay, trap logic, resource storage, or pickup clutter. Blood Axe remains a hostile Giant sub-faction separate from neutral/civilized Giant culture.

Guardrails: no DCC, no FBX, no Unreal Content, no runtime source, no validator, no source concept movement, no first DCC target, no implementation target, no rope physics, no climbing, no tripwire, no trap, no pickup, no loot, no resource, no workstation, no interaction, no nav/pathfinding, no final visual approval.

## 2. Gameplay Purpose

Static non-interactive rope dressing kit for camps, path edges, shelter support, gate approaches, and utility clusters. It supports visual repetition and scale only. It is not a climb system, rope simulation set, tripwire kit, trap kit, crafting resource, harvest node, loot set, pickup set, workstation, inventory item set, economy set, nav/pathfinding tool, or interaction set.

## 3. Silhouette Notes

Kit silhouettes should include one small spare coil, one loose tied rope length, one thick knot bundle, and one low stacked rope grouping. Each piece must use broad rope masses and large negative spaces. Avoid dense fiber strands, thin human-scale rope, trap layouts, climb affordances, pulley systems, glowing markers, readable text tags, and refined civilized Giant craft.

## 4. Scale Notes

- Female Giant scale lock: 442 cm / 14'6".
- Male Giant scale lock: 470 cm / 15'5".
- Approved Giant range remains females 14-15 ft / 427-457 cm and males 14'10"-16'0" / 452-488 cm.
- Author in centimeters; 1 Unreal unit = 1 cm.
- Spare coil diameter: 90-180 cm.
- Loose tied length footprint: 160-360 cm long, 45-120 cm wide.
- Knot bundle footprint: 80-160 cm wide, 40-95 cm tall.
- Low stacked grouping: 180-420 cm wide, 90-220 cm deep, 45-120 cm tall.
- Rope strand thickness: 10-26 cm, stylized and readable.

## 5. Materials and Color Palette

Primary materials: dirty thick rope, hide ties, mud, soot, ash, oil-dark grime, frayed rope ends, dull Blood Axe red cloth ties, and optional sparse blackened iron ring accents. Avoid blue-gray civilized Giant stone, refined peaceful highland craft, blue runes, magic glow, forge glow, bright rope dye, and default emissive.

## 6. Concept Image Prompt

Create an original stylized fantasy MMORPG concept image of `KIT_GIA_BloodAxeRopeBundleSet_A01` for the world of Aerathea. The design should emphasize a small static set of Giant-scale Blood Axe spare rope bundles, broad rope coils, loose tied rope lengths, thick knot bundles, low stacked rope grouping, dirty fiber, hide ties, mud, soot, ash, dull red cloth ties, hostile raider camp identity, female Giant scale 442 cm / 14'6", male Giant scale 470 cm / 15'5", and a gameplay role as static non-interactive camp dressing. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, no emissive glow, and MMO-friendly production design. Present it as an asset board with labeled variants, scale row, material swatches, LOD notes, and collision notes. Avoid copying any existing franchise, avoid neutral/civilized Giant culture, avoid dense rope micro-strands, avoid rope physics, avoid climbing/tripwire/trap language, avoid pickup/resource/workstation diagrams, and avoid interaction prompts.

## 7. Modeling Notes

Plan four static child variants: spare coil, loose tied length, knot bundle, and low stacked grouping. Model major coil volumes, rope lengths, knots, rope ends, and hide ties as geometry. Use texture and normals for fiber twist, fray, cuts, dirt, soot, cloth weave, and mud. Avoid individual micro-strands. Do not define rigged rope, simulated rope, per-segment physics, climb points, tripwire endpoints, trap parts, resource counts, sockets, inventory states, or gameplay affordances.

## 8. Texture and Material Notes

Required future map set: `BC`, `N`, and packed `ORM`. No emissive map for baseline `A01`.

Texture names:

- `T_GIA_BloodAxeRopeBundleSet_A01_BC`
- `T_GIA_BloodAxeRopeBundleSet_A01_N`
- `T_GIA_BloodAxeRopeBundleSet_A01_ORM`

Material target: 1 material slot for rope, hide, grime, and dull red ties; optional second slot only if blackened iron rings are included. Use 512-1K textures for repeated rope bundles; 2K only if a later hero camp close-up approves it.

## 9. Triangle Budget

- Spare coil LOD0 target: 900-3k tris.
- Loose tied length LOD0 target: 800-2.8k tris.
- Knot bundle LOD0 target: 900-3.2k tris.
- Low stacked grouping LOD0 target: 2k-6k tris.
- Full kit preview, if later approved: under 12k tris by reusing child variants.
- Material slots: 1 preferred, 2 maximum.

## 10. LOD Plan

- LOD0: full child silhouettes, major rope turns, knots, rope ends, hide ties, and low stacked footprints.
- LOD1: 60-70 percent of LOD0; reduce turn subdivisions, knot bevels, tie folds, rope-end cuts, and underside detail.
- LOD2: 35-45 percent of LOD0; merge secondary turns, simplify knot forms, reduce rope-end silhouettes, and flatten fray into normals.
- LOD3: 15-25 percent of LOD0; preserve each child footprint, rope mass, knot block, and dull red/mud material accents.

Remove fiber strands, fray, cloth weave, soot speckles, mud flecks, and small cuts before reducing the main rope masses.

## 11. Collision Notes

Planned display collision only: one simple hull per child variant, using low cylinder-like or box-like shapes around the visual footprint. No per-rope, per-knot, per-strand, or per-ring collision. No rope physics collision, no climb collision, no tripwire trigger, no trap trigger, no pickup collision, no resource trigger, no workstation volume, no interaction volume, no nav blocker, no pathfinding device, no physics constraint, no damage trace, and no destructible collision.

## 12. Animation Notes

Static mesh kit baseline. No animation, no rope simulation, no physics simulation, no cloth simulation, no hanging motion, no uncoiling state, no climbing state, no tripwire or trap state, no pickup behavior, no resource behavior, no workstation behavior, no crafting loop, no interaction prompt, no NPC work loop, no VFX, no audio, and no startup-scene behavior.

## 13. Unreal Import Notes

Planning notes only; this task does not create Unreal assets or import content.

- Planned asset type: Static Mesh kit children.
- Planned folder: `/Game/Aerathea/Props/Giants/BloodAxeCamp/CampTools/`
- Planned meshes: `SM_GIA_BloodAxeRopeBundle_SpareCoil_A01`, `SM_GIA_BloodAxeRopeBundle_TiedLength_A01`, `SM_GIA_BloodAxeRopeBundle_KnotBundle_A01`, `SM_GIA_BloodAxeRopeBundle_Stack_A01`
- Planned kit label: `KIT_GIA_BloodAxeRopeBundleSet_A01`
- Planned material: `MI_GIA_BloodAxeRopeHide_A01`
- Pivot: ground center of each child footprint.
- Scale: import at 1.0, authored in centimeters.
- LODs: LOD0-LOD3 required for important child meshes.
- Collision: simple display-only hulls.
- Sockets: none.
- Blueprint behavior: none.
- Performance: static dressing only; no Blueprint Actor, gameplay component, rope component, climb component, trap logic, pickup item, resource data, interaction volume, nav behavior, runtime source, validator, or startup placement.

## 14. Folder and Naming Recommendation

- Package path: `docs/assets/kits/KIT_GIA_BloodAxeRopeBundleSet_A01/PRODUCTION_PACKAGE.md`
- Future source folder, if separately approved: `SourceAssets/Props/Giants/BloodAxeCamp/CampTools/KIT_GIA_BloodAxeRopeBundleSet_A01/`
- Future texture prefix: `T_GIA_BloodAxeRopeBundleSet_A01`
- Future material instance: `MI_GIA_BloodAxeRopeHide_A01`

Do not create source folders, DCC files, FBX files, Unreal Content, global index edits, task board edits, Hermes files/config, material graphs, shaders, VFX, audio, runtime source, rope simulation assets, or implementation artifacts from this package.

## 15. Quality Gate Checklist

- Original Aerathea Blood Axe hostile Giant sub-faction kit, not neutral/civilized Giant culture.
- Giant scale lock preserved: female 442 cm / 14'6" and male 470 cm / 15'5".
- Static camp dressing only; no rope physics, climbing, tripwire, trap, pickup, loot, resource, workstation, interaction, nav/pathfinding, inventory, or economy behavior.
- Child silhouettes cover spare coil, tied length, knot bundle, and low stacked grouping.
- Materials stay in dirty rope, hide, soot, ash, mud, grime, and restrained dull red accents.
- Fiber, fray, weave, small cuts, soot, and mud are texture/normal detail.
- LOD0-LOD3, collision, texture maps, material slots, pivot, scale, and Unreal import planning are documented.
- No DCC, FBX, Unreal, runtime, validator, source concept, global index, task board, Hermes, implementation target, or final visual approval work is included.
