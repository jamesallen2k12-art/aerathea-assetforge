# SM_GIA_BloodAxeToolBucket_A01 Production Package

## 1. Art Direction Summary

- Asset name: `SM_GIA_BloodAxeToolBucket_A01`
- Asset type: Static Mesh prop planning package
- Parent kit: `KIT_GIA_BloodAxeCampTools_A01`
- Intake row: `BloodAxeCamp.png#CampTools_ToolBucket_Open_A01`
- Faction/theme: Blood Axe Tribe, hostile Giant sub-faction only
- Status: docs-only production package ready

Oversized open bucket for Blood Axe camp utility dressing. The read is crude, heavy, battered, and scaled for raider Giants, with a few massive tool handles visible above a thick rim. Blood Axe remains a hostile Giant sub-faction separate from neutral/civilized Giant culture; do not use civilized Giant cave-town masonry, warm hearth craft, refined highland tools, peaceful terrace language, restrained blue runes, or neutral Giant civic identity.

Guardrails: no DCC, no FBX, no Unreal Content, no runtime source, no validator, no source concept movement, no first DCC target, no implementation target, no pickup, no loot, no resource, no workstation, no interaction, no usable container, no inventory, no economy, no final visual approval.

## 2. Gameplay Purpose

Static non-interactive camp dressing that sells Blood Axe scale and rough field maintenance near shelters, forge support areas, paths, gates, and utility clusters. It is a visual prop only, not a usable bucket, container, loot chest, pickup object, resource node, workstation, crafting ingredient, vendor object, or interaction target.

## 3. Silhouette Notes

Use a broad open bucket silhouette with thick uneven rim, heavy side boards or battered metal panels, squat feet, crude carry handle, and two or three large visible tool handles. Keep the opening readable from MMO camera distance. Avoid dense small tools, shiny treasure reads, human-scale pail proportions, UI markers, glow rings, and polished smithy organization.

## 4. Scale Notes

- Female Giant scale lock: 442 cm / 14'6".
- Male Giant scale lock: 470 cm / 15'5".
- Approved Giant range remains females 14-15 ft / 427-457 cm and males 14'10"-16'0" / 452-488 cm.
- Author in centimeters; 1 Unreal unit = 1 cm.
- Target diameter: 90-150 cm.
- Target height: 85-145 cm, excluding visible tool handles.
- Visible tool handles may rise to 170-220 cm total height, but must read as display contents, not pickup tools.

## 5. Materials and Color Palette

Primary materials: scorched timber, blackened iron rim plates, dark steel bands, soot-dark leather wraps, dirty hide lashings, mud, ash, grime, dull Blood Axe red cloth ties, and sparse chipped red paint. Use broad hand-painted wear. Do not use blue-gray civilized Giant stone, refined carved craft, warm hearth color language, default emissive, magic glow, or peaceful highland markers.

## 6. Concept Image Prompt

Create an original stylized fantasy MMORPG concept image of `SM_GIA_BloodAxeToolBucket_A01` for the world of Aerathea. The design should emphasize an oversized open Blood Axe Giant camp tool bucket, thick battered rim, scorched timber panels, blackened iron bands, crude carry handle, a few massive visible tool handles, dull red cloth ties, soot, mud, grime, hostile Giant raider identity, female Giant scale 442 cm / 14'6", male Giant scale 470 cm / 15'5", and a gameplay role as static non-interactive camp dressing. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, no emissive glow, and MMO-friendly production design. Present it as a single prop concept sheet with front, side, top, scale callout, material swatches, LOD notes, and collision notes on a clean background. Avoid copying any existing franchise, avoid neutral/civilized Giant culture, avoid excessive micro-detail, avoid pickup markers, avoid loot/container UI, avoid resource/workstation diagrams, and avoid interaction prompts.

## 7. Modeling Notes

Model the bucket body, thick rim, major boards or metal panels, large handle, feet, broad straps, and large visible tool handles as geometry. Use texture and normals for scratches, soot speckles, tiny dents, wood grain, leather stitching, minor rivets, chipped paint, and mud flecks. The visible contents should be sparse and fused into the display prop for planning purposes; do not define removable tools, sockets, inventory states, physics, or gameplay affordance meshes.

## 8. Texture and Material Notes

Required future map set: `BC`, `N`, and packed `ORM`. No emissive map for baseline `A01`.

Texture names:

- `T_GIA_BloodAxeToolBucket_A01_BC`
- `T_GIA_BloodAxeToolBucket_A01_N`
- `T_GIA_BloodAxeToolBucket_A01_ORM`

Material target: 1 material slot preferred, 2 maximum if metal and wood/rope need separation. Use 512-1K texture resolution for repeated use; 2K only if approved for close camp hero dressing.

## 9. Triangle Budget

- LOD0 target: 1.2k-4k tris.
- LOD1 target: 700-2.6k tris.
- LOD2 target: 400-1.6k tris.
- LOD3 target: 180-800 tris.
- Material slots: 1 preferred, 2 maximum.

## 10. LOD Plan

- LOD0: full bucket form, rim, handle, feet, large tool handles, broad straps, and readable red tie.
- LOD1: reduce rim bevels, handle subdivisions, feet bevels, interior edge loops, and small strap detail.
- LOD2: simplify bucket interior, merge panel breaks, reduce visible tool handle geometry, and flatten minor dents into normals.
- LOD3: preserve bucket mass, open top read, handle arc, and red/black material blocks.

Remove scratches, stitches, tiny rivets, soot speckles, chipped paint, and mud flecks before reducing the main bucket silhouette.

## 11. Collision Notes

Planned display collision only: one simple convex hull or grouped boxes around the bucket body and visible contents. No collision on individual tool handles. No pickup collision, no usable container volume, no workstation volume, no resource trigger, no economy trigger, no loot outline, no interaction volume, no physics-simulated loose tools, no nav blocker, no trap volume, no damage trace, and no destructible fracture collision.

## 12. Animation Notes

Static mesh baseline. No animation, no physics simulation, no handle swing, no tool removal, no carry state, no pickup behavior, no loot state, no resource state, no workstation behavior, no crafting loop, no NPC work loop, no interaction prompt, no VFX, no audio, and no startup-scene behavior.

## 13. Unreal Import Notes

Planning notes only; this task does not create Unreal assets or import content.

- Planned asset type: Static Mesh.
- Planned folder: `/Game/Aerathea/Props/Giants/BloodAxeCamp/CampTools/`
- Planned mesh: `SM_GIA_BloodAxeToolBucket_A01`
- Planned material: `MI_GIA_BloodAxeCampUtility_A01`
- Pivot: ground center of bucket footprint.
- Scale: import at 1.0, authored in centimeters.
- LODs: LOD0-LOD3 required.
- Collision: simple display-only hulls.
- Sockets: none.
- Blueprint behavior: none.
- Performance: static dressing only; no Blueprint Actor, gameplay component, pickup item, loot data, resource data, inventory data, workstation actor, interaction volume, runtime source, validator, or startup placement.

## 14. Folder and Naming Recommendation

- Package path: `docs/assets/props/SM_GIA_BloodAxeToolBucket_A01/PRODUCTION_PACKAGE.md`
- Future source folder, if separately approved: `SourceAssets/Props/Giants/BloodAxeCamp/CampTools/SM_GIA_BloodAxeToolBucket_A01/`
- Future texture prefix: `T_GIA_BloodAxeToolBucket_A01`
- Future material instance: `MI_GIA_BloodAxeCampUtility_A01`

Do not create source folders, DCC files, FBX files, Unreal Content, global index edits, task board edits, Hermes files/config, material graphs, shaders, VFX, audio, runtime source, or implementation artifacts from this package.

## 15. Quality Gate Checklist

- Original Aerathea Blood Axe hostile Giant sub-faction prop, not neutral/civilized Giant culture.
- Giant scale lock preserved: female 442 cm / 14'6" and male 470 cm / 15'5".
- Static camp dressing only; no pickup, loot, resource, workstation, interaction, usable container, inventory, or economy behavior.
- Silhouette readable as an oversized open bucket with sparse large tool handles.
- Materials stay in blackened iron, scorched timber, hide, leather, soot, mud, grime, and restrained dull red accents.
- Tiny wear, scratches, stitches, rivets, wood grain, and mud are texture/normal detail.
- LOD0-LOD3, collision, texture maps, material slots, pivot, scale, and Unreal import planning are documented.
- No DCC, FBX, Unreal, runtime, validator, source concept, global index, task board, Hermes, implementation target, or final visual approval work is included.
