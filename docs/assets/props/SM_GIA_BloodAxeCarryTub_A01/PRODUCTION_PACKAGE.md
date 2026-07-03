# SM_GIA_BloodAxeCarryTub_A01 Production Package

## 1. Art Direction Summary

- Asset name: `SM_GIA_BloodAxeCarryTub_A01`
- Asset type: Static Mesh prop planning package
- Parent kit: `KIT_GIA_BloodAxeCampTools_A01`
- Intake row: `BloodAxeForge.png#CampTools_CarryTub_A01`
- Faction/theme: Blood Axe Tribe, hostile Giant sub-faction only
- Status: docs-only production package ready

Low rectangular or oval carry tub for Blood Axe camp utility dressing. It can visually hold wedges, rope lengths, or hooks as fused display shapes, but it must not become a usable container or resource crate. Blood Axe remains a hostile Giant sub-faction separate from neutral/civilized Giant culture.

Guardrails: no DCC, no FBX, no Unreal Content, no runtime source, no validator, no source concept movement, no first DCC target, no implementation target, no pickup, no loot, no resource, no workstation, no interaction, no usable container, no storage/inventory/economy behavior, no final visual approval.

## 2. Gameplay Purpose

Static non-interactive camp dressing for low work lanes near forge support, shelter edges, and path-edge clusters. It helps sell Giant-scale logistics without creating gameplay storage, resource, crafting, salvage, vendor, loot, pickup, workstation, or interaction behavior.

## 3. Silhouette Notes

Use a low wide tub silhouette with battered oval or rectangular footprint, thick rim, reinforced corners, heavy side handles, and optional fused display contents that remain below the rim line or break it sparingly. It should read broader and lower than bucket variants. Avoid crate-like loot language, clean shop storage, dense small contents, polished metal, and refined civilized Giant craft.

## 4. Scale Notes

- Female Giant scale lock: 442 cm / 14'6".
- Male Giant scale lock: 470 cm / 15'5".
- Approved Giant range remains females 14-15 ft / 427-457 cm and males 14'10"-16'0" / 452-488 cm.
- Author in centimeters; 1 Unreal unit = 1 cm.
- Target length: 150-260 cm.
- Target width: 85-170 cm.
- Target height: 55-115 cm.
- Optional fused contents may reach 140 cm, but must not imply usable storage.

## 5. Materials and Color Palette

Primary materials: scorched timber planks, dark iron corner bands, blackened handle plates, hide lashings, dirty rope ties, soot, ash, mud, oil stains, dull Blood Axe red cloth scraps, and restrained chipped red paint. Avoid blue-gray civilized Giant stone, refined masonry, warm hearth colors, peaceful highland craft, blue runes, magic glow, and default emissive.

## 6. Concept Image Prompt

Create an original stylized fantasy MMORPG concept image of `SM_GIA_BloodAxeCarryTub_A01` for the world of Aerathea. The design should emphasize a low wide Giant-scale Blood Axe carry tub, battered oval or rectangular footprint, thick reinforced rim, scorched timber, blackened iron corner bands, heavy side handles, optional fused wedges or rope lengths, soot, mud, dull red cloth scraps, hostile raider camp identity, female Giant scale 442 cm / 14'6", male Giant scale 470 cm / 15'5", and a gameplay role as static non-interactive camp dressing. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, no emissive glow, and MMO-friendly production design. Present it as a prop concept sheet with front, side, top, scale callout, material swatches, LOD notes, and collision notes. Avoid copying any existing franchise, avoid neutral/civilized Giant culture, avoid excessive micro-detail, avoid loot crate language, avoid pickup markers, avoid resource/workstation diagrams, and avoid interaction prompts.

## 7. Modeling Notes

Model the tub shell, thick rim, base rails, side handles, corner bands, and large fused contents if used. Keep contents sparse: one rope length, two wedges, or one hook silhouette maximum for the baseline variant. Use texture and normals for plank grain, soot, scratches, stitch lines, tiny rivets, grime, chipped paint, and mud. Do not define separable contents, sockets, inventory slots, resource states, open/closed states, physics, or usable container affordances.

## 8. Texture and Material Notes

Required future map set: `BC`, `N`, and packed `ORM`. No emissive map for baseline `A01`.

Texture names:

- `T_GIA_BloodAxeCarryTub_A01_BC`
- `T_GIA_BloodAxeCarryTub_A01_N`
- `T_GIA_BloodAxeCarryTub_A01_ORM`

Material target: 1 material preferred, 2 maximum if metal bands require a shared blackened metal material. Use 512-1K textures for repeated dressing; 2K only if later approved for close hero use.

## 9. Triangle Budget

- LOD0 target: 1.8k-5k tris.
- LOD1 target: 1k-3.2k tris.
- LOD2 target: 500-1.9k tris.
- LOD3 target: 250-950 tris.
- Material slots: 1 preferred, 2 maximum.

## 10. LOD Plan

- LOD0: full low tub body, rim, handles, corner bands, base rails, and sparse fused contents.
- LOD1: reduce rim bevels, handle subdivisions, corner band detail, base rail cuts, and underside detail.
- LOD2: simplify tub interior, merge plank breaks, reduce fused content cuts, and flatten minor damage into normals.
- LOD3: preserve low wide footprint, rim silhouette, handle blocks, and red/black material read.

Remove small scratches, stitch lines, rivets, soot speckles, chipped paint, wood grain, mud flecks, and fray before reducing the tub body.

## 11. Collision Notes

Planned display collision only: one box-like or convex hull around the low tub footprint; optional fused contents are covered by the same simple hull. No per-content collision. No pickup collision, no usable container volume, no workstation volume, no loot outline, no resource trigger, no salvage trigger, no economy trigger, no inventory trigger, no interaction volume, no nav blocker, no physics-simulated contents, no trap volume, no damage trace, and no destructible fracture collision.

## 12. Animation Notes

Static mesh baseline. No animation, no physics simulation, no contents shifting, no carry state, no open/close state, no pickup behavior, no loot state, no storage state, no resource state, no workstation behavior, no crafting loop, no NPC work loop, no interaction prompt, no VFX, no audio, and no startup-scene behavior.

## 13. Unreal Import Notes

Planning notes only; this task does not create Unreal assets or import content.

- Planned asset type: Static Mesh.
- Planned folder: `/Game/Aerathea/Props/Giants/BloodAxeCamp/CampTools/`
- Planned mesh: `SM_GIA_BloodAxeCarryTub_A01`
- Planned material: `MI_GIA_BloodAxeCampUtility_A01`
- Pivot: ground center of tub footprint.
- Scale: import at 1.0, authored in centimeters.
- LODs: LOD0-LOD3 required.
- Collision: simple display-only hull.
- Sockets: none.
- Blueprint behavior: none.
- Performance: static dressing only; no Blueprint Actor, gameplay component, pickup item, loot data, resource data, inventory data, workstation actor, interaction volume, runtime source, validator, or startup placement.

## 14. Folder and Naming Recommendation

- Package path: `docs/assets/props/SM_GIA_BloodAxeCarryTub_A01/PRODUCTION_PACKAGE.md`
- Future source folder, if separately approved: `SourceAssets/Props/Giants/BloodAxeCamp/CampTools/SM_GIA_BloodAxeCarryTub_A01/`
- Future texture prefix: `T_GIA_BloodAxeCarryTub_A01`
- Future material instance: `MI_GIA_BloodAxeCampUtility_A01`

Do not create source folders, DCC files, FBX files, Unreal Content, global index edits, task board edits, Hermes files/config, material graphs, shaders, VFX, audio, runtime source, or implementation artifacts from this package.

## 15. Quality Gate Checklist

- Original Aerathea Blood Axe hostile Giant sub-faction prop, not neutral/civilized Giant culture.
- Giant scale lock preserved: female 442 cm / 14'6" and male 470 cm / 15'5".
- Static camp dressing only; no pickup, loot, resource, workstation, interaction, usable container, storage, salvage, vendor, inventory, or economy behavior.
- Silhouette readable as a low wide Giant carry tub.
- Materials stay in scorched timber, blackened iron, hide, rope, soot, ash, mud, grime, and restrained dull red accents.
- Tiny scratches, wood grain, stitch lines, rivets, chipped paint, soot, fray, and mud are texture/normal detail.
- LOD0-LOD3, collision, texture maps, material slots, pivot, scale, and Unreal import planning are documented.
- No DCC, FBX, Unreal, runtime, validator, source concept, global index, task board, Hermes, implementation target, or final visual approval work is included.
