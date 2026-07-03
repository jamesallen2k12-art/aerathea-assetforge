# SM_GIA_BloodAxeIronRimToolBucket_A01 Production Package

## 1. Art Direction Summary

- Asset name: `SM_GIA_BloodAxeIronRimToolBucket_A01`
- Asset type: Static Mesh prop planning package
- Parent kit: `KIT_GIA_BloodAxeCampTools_A01`
- Intake row: `BloodAxecamp.png#CampTools_ToolBucket_IronRim_A01`
- Faction/theme: Blood Axe Tribe, hostile Giant sub-faction only
- Status: docs-only production package ready

Heavy iron-rimmed bucket variant for Blood Axe gate, shelter, and forge-support dressing. It should feel tougher and more metal-forward than the open timber bucket, with a dark iron lip, hammered side bands, hide-wrapped handle, and one restrained dull red cloth tie. Blood Axe remains a hostile Giant sub-faction separate from neutral/civilized Giant culture.

Guardrails: no DCC, no FBX, no Unreal Content, no runtime source, no validator, no source concept movement, no first DCC target, no implementation target, no pickup, no loot, no resource, no workstation, no interaction, no usable container, no vendor/economy/storage behavior, no final visual approval.

## 2. Gameplay Purpose

Static non-interactive environmental dressing for rough Blood Axe camp utility zones. It provides scale and material contrast beside gates, shelters, forge support props, and low camp clusters. It is not a storage container, loot object, pickup, resource node, crafting input, workstation, vendor container, economy object, or interaction target.

## 3. Silhouette Notes

Use a compact heavy bucket silhouette with oversized dark iron rim, thick lower band, hammered side plates, hide-wrapped handle, and a slightly uneven open top. The rim should be the primary silhouette difference from `SM_GIA_BloodAxeToolBucket_A01`. Avoid ornate metalwork, treasure chest reads, bright polish, dense rivets, human-scale pail proportions, and refined civilized Giant craft.

## 4. Scale Notes

- Female Giant scale lock: 442 cm / 14'6".
- Male Giant scale lock: 470 cm / 15'5".
- Approved Giant range remains females 14-15 ft / 427-457 cm and males 14'10"-16'0" / 452-488 cm.
- Author in centimeters; 1 Unreal unit = 1 cm.
- Target diameter: 100-165 cm.
- Target height: 90-155 cm.
- Handle apex may reach 170-210 cm when upright, but no carry animation or usable state is defined.

## 5. Materials and Color Palette

Primary materials: blackened iron, dark steel, dull hammered plates, soot-stained wood inserts, hide handle wrap, dirty leather lashings, oil-dark grime, mud, ash, and one restrained Blood Axe red cloth tie or chipped red paint mark. Do not use blue-gray carved civilized Giant stone, refined stoneworker craft, warm hearth colors, blue runes, storm motifs, or default emissive.

## 6. Concept Image Prompt

Create an original stylized fantasy MMORPG concept image of `SM_GIA_BloodAxeIronRimToolBucket_A01` for the world of Aerathea. The design should emphasize a Giant-scale heavy iron-rimmed Blood Axe tool bucket, thick blackened iron lip, hammered dark steel bands, battered side panels, hide-wrapped carry handle, oil-dark grime, soot, mud, dull red cloth tie, hostile raider camp identity, female Giant scale 442 cm / 14'6", male Giant scale 470 cm / 15'5", and a gameplay role as static non-interactive camp dressing. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, no emissive glow, and MMO-friendly production design. Present it as a single prop concept sheet with scale callouts, material swatches, LOD notes, and collision notes. Avoid copying any existing franchise, avoid neutral/civilized Giant culture, avoid excessive micro-detail, avoid loot/container UI, avoid pickup markers, avoid resource/workstation diagrams, and avoid interaction prompts.

## 7. Modeling Notes

Model the iron rim, main bucket shell, hammered bands, handle, handle lugs, broad side plates, and grounded base as geometry. Use wider forms and fewer, larger fasteners than human props. Texture handles minor rivets, pitting, scratches, grime streaks, soot, chipped red paint, and leather stitch detail. Do not model dense bolt fields, removable contents, latch logic, open/closed states, socketed tools, inventory compartments, or gameplay affordances.

## 8. Texture and Material Notes

Required future map set: `BC`, `N`, and packed `ORM`. No emissive map for baseline `A01`.

Texture names:

- `T_GIA_BloodAxeIronRimToolBucket_A01_BC`
- `T_GIA_BloodAxeIronRimToolBucket_A01_N`
- `T_GIA_BloodAxeIronRimToolBucket_A01_ORM`

Material target: 1-2 slots. Slot 0 can cover shared bucket grime, wood, hide, and red marks; optional slot 1 can use a shared blackened metal material. Use 512-1K textures for normal repeated dressing and 2K only with later hero approval.

## 9. Triangle Budget

- LOD0 target: 1.5k-4.5k tris.
- LOD1 target: 900-3k tris.
- LOD2 target: 450-1.8k tris.
- LOD3 target: 220-900 tris.
- Material slots: 1-2.

## 10. LOD Plan

- LOD0: full rim thickness, hammered band silhouette, handle, lugs, base, side plates, and red tie.
- LOD1: reduce rim bevels, band subdivisions, handle lugs, base bevels, and backside plate cuts.
- LOD2: simplify bucket interior, merge minor band breaks, reduce side plate cuts, and flatten small damage into normals.
- LOD3: preserve heavy iron rim read, bucket mass, handle arc, and dark metal/red accent blocks.

Remove tiny rivets, scratches, pitting, soot speckles, chipped paint, mud flecks, and stitch lines before reducing the main rim or bucket body.

## 11. Collision Notes

Planned display collision only: one convex hull or grouped boxes around the bucket body, with optional simple handle clearance ignored unless needed for display placement. No per-rim collision. No pickup collision, no usable storage volume, no workstation volume, no loot outline, no resource trigger, no economy trigger, no inventory trigger, no interaction volume, no physics simulation, no nav blocker, no trap volume, no damage trace, and no destructible fracture collision.

## 12. Animation Notes

Static mesh baseline. No animation, no handle swing, no physics simulation, no carry state, no open/close state, no tool pickup, no loot state, no storage state, no resource state, no workstation behavior, no crafting loop, no NPC work loop, no interaction prompt, no VFX, no audio, and no startup-scene behavior.

## 13. Unreal Import Notes

Planning notes only; this task does not create Unreal assets or import content.

- Planned asset type: Static Mesh.
- Planned folder: `/Game/Aerathea/Props/Giants/BloodAxeCamp/CampTools/`
- Planned mesh: `SM_GIA_BloodAxeIronRimToolBucket_A01`
- Planned material: `MI_GIA_BloodAxeCampUtility_A01` with optional `MI_GIA_BloodAxeReforgedMetal_A01`
- Pivot: ground center of bucket footprint.
- Scale: import at 1.0, authored in centimeters.
- LODs: LOD0-LOD3 required.
- Collision: simple display-only hull.
- Sockets: none.
- Blueprint behavior: none.
- Performance: static dressing only; no Blueprint Actor, gameplay component, pickup item, loot data, resource data, inventory data, workstation actor, interaction volume, runtime source, validator, or startup placement.

## 14. Folder and Naming Recommendation

- Package path: `docs/assets/props/SM_GIA_BloodAxeIronRimToolBucket_A01/PRODUCTION_PACKAGE.md`
- Future source folder, if separately approved: `SourceAssets/Props/Giants/BloodAxeCamp/CampTools/SM_GIA_BloodAxeIronRimToolBucket_A01/`
- Future texture prefix: `T_GIA_BloodAxeIronRimToolBucket_A01`
- Future material instances: `MI_GIA_BloodAxeCampUtility_A01`, `MI_GIA_BloodAxeReforgedMetal_A01`

Do not create source folders, DCC files, FBX files, Unreal Content, global index edits, task board edits, Hermes files/config, material graphs, shaders, VFX, audio, runtime source, or implementation artifacts from this package.

## 15. Quality Gate Checklist

- Original Aerathea Blood Axe hostile Giant sub-faction prop, not neutral/civilized Giant culture.
- Giant scale lock preserved: female 442 cm / 14'6" and male 470 cm / 15'5".
- Static camp dressing only; no pickup, loot, resource, workstation, interaction, usable container, storage, vendor, inventory, or economy behavior.
- Silhouette readable as a heavy iron-rimmed Giant bucket.
- Materials stay in blackened iron, dark steel, scorched wood, hide, leather, soot, mud, grime, and restrained dull red accents.
- Tiny rivets, pitting, scratches, chipped paint, soot, stitch lines, and mud are texture/normal detail.
- LOD0-LOD3, collision, texture maps, material slots, pivot, scale, and Unreal import planning are documented.
- No DCC, FBX, Unreal, runtime, validator, source concept, global index, task board, Hermes, implementation target, or final visual approval work is included.
