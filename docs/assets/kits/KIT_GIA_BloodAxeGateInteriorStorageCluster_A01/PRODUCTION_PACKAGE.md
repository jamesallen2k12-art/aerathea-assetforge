# KIT_GIA_BloodAxeGateInteriorStorageCluster_A01 Production Package

Docs-only production package for a Blood Axe Giant gate-interior storage cluster. This package creates no DCC source, no SourceAssets output, no Unreal Content, no runtime source, no validator, no startup placement, no final visual approval, no source concept movement, no Hermes work, and no implementation target.

## Art Direction Summary

- Asset name: `KIT_GIA_BloodAxeGateInteriorStorageCluster_A01`
- Asset type: Docs-only kit package / future static gate-adjacent storage dressing
- Parent kit: `KIT_GIA_BloodAxeCratesSacksBaskets_A01`
- Source planning row: `BloodAxeGate.png#Storage_GateInteriorCluster_A01`
- Faction/theme: Blood Axe Tribe, hostile Giant sub-faction only
- Status: docs-only production package ready

This kit defines a heavier storage pile inside or near a Blood Axe gate threshold. It uses crates, covered bundles, rope lashings, sacks, and blackened iron hardware as hostile camp dressing. It must read as inert supply clutter, not a barricade, loot cache, vendor stall, quest objective, cover object, or gate interaction component.

## Gameplay Purpose

The cluster supports gate-interior worldbuilding and scale. It helps frame the inside face of a hostile Giant camp gate without defining gate behavior.

Allowed use:

- Static gate-adjacent dressing only.
- Visual rhythm between gate structure, camp path, and supply clutter.
- Giant-scale weight and rough logistics near a threshold.

Out of scope: gate opening logic, barricade behavior, cover rules, loot cache behavior, vendor stall language, quest objective use, gate interaction, nav/pathfinding behavior, destructible behavior, VFX/audio, DCC, Unreal, startup placement, final approval, and implementation target selection.

## Silhouette Notes

- Primary read: heavier, denser pile than the shelter-edge cluster, but still visibly storage rather than fortification.
- Use two or three broad crate masses, one large covered bundle, thick rope bindings, and a few sacks/baskets for secondary shape.
- Leave visual gaps or stepped edges so it does not become a wall or barricade.
- Red accents should be restrained: tied cloth scraps, rubbed marks, or crude paint on a few surfaces.
- Model broad crate bodies, plank slabs, large hardware, covered-bundle folds, rope coils, large knots, and thick lashings as future geometry.
- Put grain, scratches, fibers, weave, soot, mud, paint chips, and minor cracks into future texture/normal detail.

Avoid treasure piles, reward chests, vendor display lines, objective markers, cover silhouettes, player-blocking wall reads, gate-control levers, locks meant for interaction, readable labels, refined market storage, and neutral/civilized Giant language.

## Scale Notes

- Giant scale lock: female 442 cm / 14 ft 6 in baseline and male 470 cm / 15 ft 5 in baseline.
- Approved Giant ranges: females 14-15 ft / 427-457 cm and males 14 ft 10 in-16 ft 0 in / 452-488 cm.
- Future source must use centimeters; 1 Unreal unit equals 1 cm.
- Suggested footprint: 550-1100 cm wide, 250-650 cm deep.
- Suggested height: 170-360 cm. Avoid wall-like vertical profiles above 420 cm unless a future gate composition task approves it.
- Must not imply gameplay clearance, path width, nav validity, or gate collision.

## Materials and Color Palette

Use rough timber, scorched crate boards, blackened iron straps, heavy rope, rawhide, patched hide covers, dirty sackcloth, soot, ash, mud, and restrained oxide red Blood Axe accents.

Palette targets:

- Rough timber: `#2A1A10` to `#5C3A22`
- Scorched wood: `#11100D` to `#2E2118`
- Blackened iron: `#121315` to `#333538`
- Rope/rawhide: `#6B5435` to `#A98B5B`
- Sackcloth/canvas: `#6A604E` to `#A39370`
- Hide/leather: `#2F1D14` to `#77543A`
- Soot/ash/mud: `#0B0A09` to `#4B4032`
- Blood Axe red: `#5F1513` to `#8B211B`

No default emissive is approved. Avoid civilized Giant masonry, refined stoneworker storage, blue-gray civic craft, warm hearth supply rows, restrained blue runes, and clean settlement market styling.

## Concept Image Prompt

Create an original stylized fantasy MMORPG concept image of `KIT_GIA_BloodAxeGateInteriorStorageCluster_A01` for the world of Aerathea. The design should emphasize a heavy Blood Axe Giant gate-interior storage pile, rough oversized crates, one large covered bundle, thick rope lashings, sacks, baskets, blackened iron straps, soot, ash, mud, restrained oxide red cloth marks, validated Giant scale with a female 442 cm / 14 ft 6 in marker and male 470 cm / 15 ft 5 in marker, hostile Giant sub-faction identity, separation from neutral/civilized Giant culture, and the gameplay role of inert static gate-adjacent dressing. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, no emissive glow, and MMO-friendly mid-poly production design. Present it as a clean asset board with front, side, three-quarter, top footprint, material swatches, scale callouts, LOD/collision notes, and no-build guardrails. Avoid copying any existing franchise, avoid barricade readability, avoid loot-cache presentation, avoid vendor stall layout, avoid quest-objective cues, avoid cover language, avoid gate interaction parts, avoid nav/pathfinding diagrams, avoid neutral Giant cave-town language, and avoid excessive micro-detail.

## Modeling Notes

Future DCC work, if separately approved, should use reusable crate, sack, basket, rope, and covered-bundle components. The pile should frame a gate interior without becoming a gate component. Keep elements stable, broad, and readable, with a rough raider arrangement rather than a tidy warehouse stack.

Do not create source folders, Blender files, FBX exports, proof renders, collision proxies, sockets, gate linkage, openable lids, pickup handles, readable cargo labels, nav hints, cover markers, UI signs, destructible seams, quest tags, or gate-control props from this package.

## Texture and Material Notes

Future texture set: Base Color, Normal, packed ORM. No emissive map is planned.

Recommended material families:

- `MI_GIA_BloodAxeStorageTimberIron_A01`
- `MI_GIA_BloodAxeStorageClothHide_A01`
- `MI_GIA_BloodAxeStorageRopeBasket_A01`
- `MI_GIA_BloodAxeStorageSootMud_A01` only if a later material lane approves shared grime

Target 3 material slots for the full cluster; 4 maximum. Avoid material slots for individual crates, ropes, sacks, stains, or red marks.

## Triangle Budget

- LOD0 compact cluster: 10k-16k tris.
- LOD0 standard cluster: 14k-24k tris.
- Hard cap: 28k tris only if a later approved gate-review task needs close readability.
- Material slots: 3 target, 4 maximum.
- Texture set: 1K-2K baseline.

Spend triangles on crate massing, covered-bundle silhouette, thick rope, large knots, blackened iron straps, sack shapes, basket rims, and gate-adjacent ground contact. Do not spend triangles on tiny hardware, fibers, labels, scratches, soot flecks, or hidden underside detail.

## LOD Plan

- LOD0: full heavy storage pile with crates, covered bundle, rope bindings, sacks, baskets, major straps, and restrained red accents.
- LOD1: reduce secondary bevels, minor rope turns, small folds, underside detail, and duplicate contact creases.
- LOD2: simplify smaller components, merge minor crate offsets, collapse basket weave into normals, reduce rope coils to broad loops.
- LOD3: preserve a broad gate-interior storage mass with visible crate blocks, one dark covered-bundle read, and small Blood Axe red accent.

Never reduce the non-barricade storage read, Giant-scale mass, or Blood Axe/civilized Giant separation before removing small detail.

## Collision Notes

Docs-only collision planning. Future collision should be disabled by default or handled as simple low blocking/query only if a later placement task owns collision. This package authorizes no collision proxy, UCX mesh, nav blocker, cover volume, gameplay volume, gate collision, gate interaction volume, player-blocking claim, path-clearance claim, or collision correctness claim.

## Animation Notes

No animation is planned. No gate animation, cloth simulation, rope simulation, physics pile, breakage animation, VFX pulse, audio cue, material-state animation, or Blueprint state behavior is authorized.

## Unreal Import Notes

Future Unreal work, if separately approved, should import as Static Mesh assets under `/Game/Aerathea/Props/Giants/BloodAxeCamp/Storage/` with LOD0-LOD3, shared material instances, centimeter scale, and disabled/simple collision policy. No Unreal Content, import script, material instance, texture asset, Blueprint, socket, validator, review actor, startup actor, or map placement is created by this package.

## Folder and Naming Recommendation

Future planning paths only:

- Package: `docs/assets/kits/KIT_GIA_BloodAxeGateInteriorStorageCluster_A01/PRODUCTION_PACKAGE.md`
- Possible DCC root: `SourceAssets/Blender/Kits/Giants/BloodAxeCamp/CratesSacksBaskets/GateInteriorStorageCluster/`
- Possible export root: `SourceAssets/Exports/Kits/Giants/BloodAxeCamp/CratesSacksBaskets/GateInteriorStorageCluster/`
- Possible Unreal root: `/Game/Aerathea/Props/Giants/BloodAxeCamp/Storage/GateInteriorStorageCluster/`
- Mesh name if later approved: `SM_GIA_BloodAxeGateInteriorStorageCluster_A01`

These are references only and do not authorize folder creation.

## Quality Gate Checklist

- [x] Docs-only package with no DCC, FBX, Unreal, runtime, startup, validator, source-concept movement, Hermes work, final approval, or implementation target.
- [x] Includes all universal Aerathea package sections.
- [x] Uses female 442 cm and male 470 cm Giant scale lock.
- [x] Keeps Blood Axe as a hostile Giant sub-faction separate from neutral/civilized Giant culture.
- [x] Defines static gate-adjacent storage dressing only.
- [x] Blocks barricade behavior, loot cache behavior, vendor stall language, quest objective use, cover rules, gate interaction, nav/pathfinding behavior, destructible behavior, VFX/audio, and material-state behavior.
- [x] Preserves MMO-readable forms and pushes micro-detail to textures/normals.
