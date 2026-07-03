# SM_GIA_BloodAxeForgeSupportUtilityCluster_A01 Production Package

## 1. Art Direction Summary

- Asset name: `SM_GIA_BloodAxeForgeSupportUtilityCluster_A01`
- Asset type: Static Mesh production package, docs-only
- Parent kit: `KIT_GIA_BloodAxeCampTools_A01`
- Child intake row: `BloodAxeForge.png#CampTools_UtilityCluster_ForgeSupport_A01`
- Faction/theme: Blood Axe Tribe, hostile Giant sub-faction only
- Status: package-ready planning document; no implementation target selected

This is a forge-adjacent support cluster using a battered bucket or carry tub, iron wedge stack, heavy mallet, blackened hooks, ring pegs, soot, ash, and dull red identifiers. It supports the look of hostile camp labor without becoming a forge workstation or heat/crafting system.

Blood Axe remains a hostile Giant sub-faction separate from neutral/civilized Giant culture. Do not borrow neutral Giant stoneworker dignity, blue-gray cave-town materials, warm hearth craft, refined masonry, restrained blue runes, or peaceful highland workshop identity.

Guardrails: no-DCC, no-Unreal, no-startup, no-nav, no-encounter, no-workstation, no-loot, no-resource, no-material-instance, no-validator, no-capture, no-final-signoff, no-implementation-target.

## 2. Gameplay Purpose

This cluster is static forge support dressing for Blood Axe camp spaces. It visually explains rough tool storage, wedge handling, and brutal field repair near forge areas.

It must not define heat gameplay, forge interaction, crafting recipes, resource behavior, salvage behavior, economy behavior, loot behavior, usable workstation behavior, NPC work loops, material graph behavior, VFX, audio, nav/pathfinding, encounter behavior, startup placement, or runtime gameplay.

## 3. Silhouette Notes

The silhouette should feel heavier and more metal-forward than the general camp utility cluster. Use a low bucket or carry tub, a dark wedge stack, one oversized sledge-style mallet, two or three heavy hooks, and ring pegs. Ashy negative spaces should separate the forms.

Model the large metal wedge masses, mallet head, bucket/tub rim, hook curves, peg rings, and main handles as future geometry. Keep soot, heat staining, pitting, fine scratches, ash flecks, and chipped paint in future textures.

Avoid active fire, glowing coals, animated sparks, furnace parts, anvil station behavior, recipe boards, resource crates, loot shine, UI prompts, or dense forge clutter that implies an approved workstation.

## 4. Scale Notes

Use the validated Giant scale lock:

- Female Giant baseline: 442 cm / 14'6".
- Male Giant baseline: 470 cm / 15'5".
- Approved Giant ranges: females 14-15 ft / 427-457 cm; males 14'10"-16'0" / 452-488 cm.
- Author in centimeters. 1 Unreal unit = 1 cm.

Suggested footprint: 280-650 cm wide, 180-420 cm deep, and 90-230 cm tall. Mallet length should sit near 170-280 cm for the forge support read, wedges 60-150 cm long, and bucket/carry tub elements 90-180 cm across. Keep all forms Giant-scale.

## 5. Materials and Color Palette

Use blackened iron, dark steel, hammered metal, scorched timber, heavy hide wraps, dirty leather, soot, ash, charcoal dust, oil-dark stains, dull Blood Axe red ties, and sparse chipped red marks.

Avoid default emissive, forge glow, active fire, bright molten metal, blue runes, neutral/civilized Giant stone, polished smithy gear, warm heroic hearth colors, and high-density red decoration. Any emissive or active material state requires a separate approval-gated package.

## 6. Concept Image Prompt

Create an original stylized fantasy MMORPG concept image of `SM_GIA_BloodAxeForgeSupportUtilityCluster_A01` for the world of Aerathea. The design should emphasize a hostile Giant forge-adjacent support cluster, battered carry tub, iron wedge stack, oversized sledge mallet, blackened hooks, ring pegs, ash, soot, dark steel, scorched timber, hide wraps, dull Blood Axe red ties, no active fire, no workstation affordance, female Giant scale 442 cm / 14'6", male Giant scale 470 cm / 15'5", and a gameplay role as static non-interactive forge support dressing. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, no default emissive glow, and MMO-friendly production design. Present it as a clean production asset board with front, side, top footprint, scale callouts, material swatches, LOD notes, and collision notes. Avoid copying any existing franchise and avoid excessive micro-detail that would not translate to a mid-poly Unreal asset.

## 7. Modeling Notes

Future modeling should make this cluster look heavy, soot-dark, and field-made, but not active. Use reusable wedge, mallet, bucket, hook, and ring-peg forms. Do not add fire beds, forge mechanisms, anvil gameplay surfaces, bellows, recipe boards, or interactive handles.

Use real geometry for wedge stack masses, mallet head and shaft, bucket/tub body, hook curves, ring pegs, large bands, and main handles. Use texture and normal detail for pitting, soot, heat staining, wood grain, leather stitching, small rivets, tiny chips, scratches, ash flecks, and chipped red paint.

Do not create DCC source, FBX, collision proxy, proof render, Unreal Content, Blueprint, sockets, material instance, validator, capture setup, startup actor, workstation logic, material graph, or implementation target from this package.

## 8. Texture and Material Notes

Future texture set:

- `T_GIA_BloodAxeForgeSupportUtilityCluster_A01_BC`
- `T_GIA_BloodAxeForgeSupportUtilityCluster_A01_N`
- `T_GIA_BloodAxeForgeSupportUtilityCluster_A01_ORM`

No emissive map is planned for baseline `A01`. Target 1K-2K. Material slots: 2 target, 3 maximum. Ash, soot, heat staining, pitting, and chipped red marks should be hand-painted or normal/ORM detail, not separate material slots.

## 9. Triangle Budget

Target LOD0: 5k-14k tris.

Target material slots: 2, with 3 maximum only if necessary for metal/wood/rope separation. Avoid unique geometry for tiny dents, pitting, ash, and scratches.

## 10. LOD Plan

- LOD0: full bucket/tub, wedge stack, sledge mallet, hook set, ring pegs, large bands, red ties, and ash-dark footprint.
- LOD1: 60-70 percent of LOD0; reduce bevels, small bands, secondary wedge chips, extra hook subdivisions, and backside details.
- LOD2: 35-45 percent of LOD0; simplify wedge stack, mallet wrap, hook bevels, peg rings, bucket interior, and underside surfaces.
- LOD3: 15-25 percent of LOD0; preserve metal-forward massing, mallet read, wedge triangular read, bucket/tub read, hook curves, and footprint.

Remove soot flecks, pitting, scratches, and small red chips before reducing primary silhouettes.

## 11. Collision Notes

Future collision should use simple display hulls around the bucket/tub, wedge stack, mallet, hooks, and ring pegs. It should not define forge station use or heat gameplay.

Do not define workstation volumes, heat volumes, crafting triggers, resource triggers, economy triggers, loot outlines, pickup collision, nav blockers, encounter cover, damage traces, destructible collision, collision proxies, startup placement collision, or material-state collision in this task.

## 12. Animation Notes

Static mesh baseline. No animation, physics, heat shimmer, sparks, fire, VFX, audio, material-state timing, NPC work cycle, workstation behavior, crafting loop, resource state, pickup behavior, loot state, nav behavior, encounter behavior, or startup behavior is authored here.

## 13. Unreal Import Notes

Planned asset type if later approved: Static Mesh.

Planned folder: `/Game/Aerathea/Props/Giants/BloodAxeCamp/UtilityClusters/`

Planned import name: `SM_GIA_BloodAxeForgeSupportUtilityCluster_A01`

Pivot: ground center of full cluster footprint. Import scale: 1.0 cm. Collision: simple display collision only. LODs: LOD0-LOD3 required. Material slots: 2 target, 3 maximum.

This package does not create Unreal assets, material instances, material graphs, validators, captures, startup placement, Blueprint behavior, runtime source, workstation behavior, heat gameplay, crafting/resource/economy behavior, or final visual signoff.

## 14. Folder and Naming Recommendation

- Docs folder: `docs/assets/props/SM_GIA_BloodAxeForgeSupportUtilityCluster_A01/`
- Production package: `docs/assets/props/SM_GIA_BloodAxeForgeSupportUtilityCluster_A01/PRODUCTION_PACKAGE.md`
- Future mesh name: `SM_GIA_BloodAxeForgeSupportUtilityCluster_A01`
- Future texture prefix: `T_GIA_BloodAxeForgeSupportUtilityCluster_A01`

Do not add SourceAssets, FBX exports, Unreal Content, Tools/DCC, Tools/Unreal, runtime source, validators, captures, global indexes, task board updates, material instances, material graphs, VFX, or startup scene files from this package.

## 15. Quality Gate Checklist

- Uses the universal 15-section Aerathea package format.
- Remains docs-only with no-DCC/no-Unreal/no-startup/no-nav/no-encounter/no-workstation/no-loot/no-resource/no-material-instance/no-validator/no-capture/no-final-signoff/no-implementation-target guardrails.
- Preserves female Giant 442 cm / 14'6" and male Giant 470 cm / 15'5" scale lock.
- Keeps Blood Axe as a hostile Giant sub-faction separate from neutral/civilized Giant culture.
- Defines static forge support dressing without heat, crafting, resource, economy, workstation, VFX, or material-instance claims.
- Includes material, texture, triangle, LOD, collision, animation, Unreal planning, folder, and naming notes.
- Does not claim final visual approval, implementation readiness, runtime behavior, shipped content, or first DCC target selection.
