# KIT_GIA_BloodAxeShelterEdgeStorageCluster_A01 Production Package

Docs-only production package for a Blood Axe Giant shelter-edge storage cluster. This package creates no DCC source, no SourceAssets output, no Unreal Content, no runtime source, no validator, no startup placement, no final visual approval, no source concept movement, no Hermes work, and no implementation target.

## Art Direction Summary

- Asset name: `KIT_GIA_BloodAxeShelterEdgeStorageCluster_A01`
- Asset type: Docs-only kit package / future static level-art dressing cluster
- Parent kit: `KIT_GIA_BloodAxeCratesSacksBaskets_A01`
- Source planning row: `BloodAxeCamp.png#Storage_ShelterEdgeCluster_A01`
- Faction/theme: Blood Axe Tribe, hostile Giant sub-faction only
- Status: docs-only production package ready

This kit defines a lower shelter-wall or lean-to-edge storage composition made from rough crates, heavy sacks, basket forms, rope bindings, and covered hide bundles. It should sit below major sightline height so shelters, Giant silhouettes, and camp gates remain readable. Blood Axe materials must stay rough, raider-made, and separate from neutral/civilized Giant cave-town culture.

## Gameplay Purpose

The cluster supports static environmental storytelling around Blood Axe shelters. It explains where raiders stack inert supplies without creating storage gameplay.

Allowed use:

- Shelter-edge and lean-to-edge dressing only.
- Visual scale support beside validated Giant baselines.
- Low, broad silhouette that fills ground-plane edges without becoming cover, a blocker, a navigation tool, or an interaction object.

Out of scope: shelter interaction, usable storage, loot, pickup, inventory, resource, vendor, crafting, economy, cover rules, nav/pathfinding behavior, destructible behavior, gameplay collision definition, VFX/audio, DCC, Unreal, startup placement, final approval, and implementation target selection.

## Silhouette Notes

- Primary read: low stepped pile tucked against a shelter wall or lean-to edge.
- Height should remain under typical Giant torso read, with broad ground contact and a soft sloping profile.
- Use one or two low crates as structure, two to five sacks or hide bundles as mass, and a few rope/basket accents.
- Keep the shelter-side edge compressed and the open side readable from an MMO camera.
- Model broad crate bodies, large lids, sack masses, tied necks, basket rims, rope coils, large knots, tarp folds, and major lashings as future geometry.
- Push small wood grain, rope fibers, cloth weave, stitching, scratches, ash flecks, soot speckles, and chipped paint into future textures and normal maps.

Avoid tidy household storage, neutral Giant domestic bedding, treasure chest reads, route markers, barricade walls, cover silhouettes, trap language, destructible seams, glowing signals, readable labels, and dense micro-detail.

## Scale Notes

- Giant scale lock: female 442 cm / 14 ft 6 in baseline and male 470 cm / 15 ft 5 in baseline.
- Approved Giant ranges: females 14-15 ft / 427-457 cm and males 14 ft 10 in-16 ft 0 in / 452-488 cm.
- Future source must use centimeters; 1 Unreal unit equals 1 cm.
- Suggested footprint: 450-850 cm wide, 180-420 cm deep.
- Suggested height: 120-260 cm, with exceptional back-edge masses up to 320 cm only if they do not become a wall or cover object.
- Normal humanoid scale is not a design target.

## Materials and Color Palette

Use rough timber, blackened iron, heavy rope, rawhide, dirty sackcloth, patched hide, mud, soot, ash, and restrained oxide red Blood Axe accents.

Palette targets:

- Rough timber: `#2A1A10` to `#5C3A22`
- Blackened iron: `#121315` to `#333538`
- Rope/rawhide: `#6B5435` to `#A98B5B`
- Sackcloth/canvas: `#6A604E` to `#A39370`
- Hide/leather: `#2F1D14` to `#77543A`
- Ash/mud: `#0B0A09` to `#4B4032`
- Blood Axe red: `#5F1513` to `#8B211B`

Do not use civilized Giant blue-gray masonry, hearth-market storage, polished stoneworker joinery, terrace motifs, restrained blue runes, default emissive, or refined highland domestic styling.

## Concept Image Prompt

Create an original stylized fantasy MMORPG concept image of `KIT_GIA_BloodAxeShelterEdgeStorageCluster_A01` for the world of Aerathea. The design should emphasize a low Blood Axe Giant shelter-edge storage cluster, rough crates, heavy sacks, covered hide bundles, basket accents, thick rope bindings, blackened iron straps, soot, ash, mud, restrained oxide red cloth marks, validated Giant scale with a female 442 cm / 14 ft 6 in marker and male 470 cm / 15 ft 5 in marker, hostile Giant sub-faction identity, separation from neutral/civilized Giant culture, and the gameplay role of static non-interactive shelter-edge dressing. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, no emissive glow, and MMO-friendly mid-poly production design. Present it as a clean asset board with front, side, three-quarter, top footprint, scale callouts, material swatches, LOD/collision planning notes, and no-build guardrails. Avoid copying any existing franchise, avoid cover-object readability, avoid route markers, avoid treasure or loot presentation, avoid shelter interaction cues, avoid destructible language, avoid UI markers, avoid neutral Giant cave-town language, and avoid excessive micro-detail.

## Modeling Notes

Future DCC work, if separately approved, should compose reusable storage children rather than sculpting one dense unique pile. Use broad crate slabs, sack volumes, basket rims, rope coils, covered-bundle masses, and a few large lashing bands. Preserve an uneven but stable shelter-edge footprint.

Do not create source folders, Blender files, FBX exports, proof renders, collision proxies, sockets, nav blockers, gameplay volumes, destructible cuts, pickup handles, readable tags, UI shapes, or shelter attachment logic from this package.

## Texture and Material Notes

Future texture set: Base Color, Normal, packed ORM. No emissive map is planned.

Recommended material families:

- `MI_GIA_BloodAxeStorageTimberIron_A01`
- `MI_GIA_BloodAxeStorageClothHide_A01`
- `MI_GIA_BloodAxeStorageRopeBasket_A01`
- Optional shared grime only under a future material task

Target 2-3 material slots for a full cluster. Avoid unique slots for each sack, crate, stain, rope, or red tag.

## Triangle Budget

- LOD0 compact cluster: 7k-13k tris.
- LOD0 standard cluster: 12k-20k tris.
- Hard cap: 24k tris if a later approved task requires close shelter readability.
- Material slots: 2-3 target, 4 maximum.
- Texture set: 1K-2K baseline.

Spend triangles on the low cluster silhouette, crate profiles, sack masses, basket rims, rope coils, knots, and tarp folds. Do not spend triangles on fibers, tiny scratches, individual stitch lines, small nails, soot speckles, or hidden underside detail.

## LOD Plan

- LOD0: full low shelter-edge cluster with crates, sacks, basket/rope accents, covered bundle, broad folds, and restrained red accents.
- LOD1: reduce small bevels, secondary rope turns, minor folds, and hidden contact detail.
- LOD2: simplify sacks and covered bundles, collapse basket weave into normals, remove most underside/back detail.
- LOD3: preserve a low stepped storage mass, one or two crate reads, dark cloth/hide masses, and a small Blood Axe red accent.

Never reduce the low shelter-edge read, Giant-scale mass, or Blood Axe/civilized Giant separation before removing small detail.

## Collision Notes

Docs-only collision planning. Future collision should be disabled by default for background dressing or use a simple low blocking/query hull only if a later placement task proves it is needed. This package authorizes no collision proxy, UCX mesh, nav blocker, cover volume, gameplay volume, shelter collision, route clearance, player-blocking claim, or collision correctness claim.

## Animation Notes

No animation is planned. No cloth simulation, rope simulation, physics pile, breakage animation, idle motion, VFX pulse, audio cue, or material-state animation is authorized.

## Unreal Import Notes

Future Unreal work, if separately approved, should import as Static Mesh assets under `/Game/Aerathea/Props/Giants/BloodAxeCamp/Storage/` with LOD0-LOD3, shared material instances, centimeter scale, and disabled/simple collision policy. No Unreal Content, import script, material instance, texture asset, Blueprint, socket, validator, review actor, startup actor, or map placement is created by this package.

## Folder and Naming Recommendation

Future planning paths only:

- Package: `docs/assets/kits/KIT_GIA_BloodAxeShelterEdgeStorageCluster_A01/PRODUCTION_PACKAGE.md`
- Possible DCC root: `SourceAssets/Blender/Kits/Giants/BloodAxeCamp/CratesSacksBaskets/ShelterEdgeStorageCluster/`
- Possible export root: `SourceAssets/Exports/Kits/Giants/BloodAxeCamp/CratesSacksBaskets/ShelterEdgeStorageCluster/`
- Possible Unreal root: `/Game/Aerathea/Props/Giants/BloodAxeCamp/Storage/ShelterEdgeStorageCluster/`
- Mesh name if later approved: `SM_GIA_BloodAxeShelterEdgeStorageCluster_A01`

These are references only and do not authorize folder creation.

## Quality Gate Checklist

- [x] Docs-only package with no DCC, FBX, Unreal, runtime, startup, validator, source-concept movement, Hermes work, final approval, or implementation target.
- [x] Includes all universal Aerathea package sections.
- [x] Uses female 442 cm and male 470 cm Giant scale lock.
- [x] Keeps Blood Axe as a hostile Giant sub-faction separate from neutral/civilized Giant culture.
- [x] Defines low shelter-edge static dressing only.
- [x] Blocks shelter interaction, cover rules, nav/pathfinding behavior, destructible behavior, gameplay collision, loot, pickup, inventory, vendor, resource, crafting, economy, VFX/audio, and material-state behavior.
- [x] Preserves MMO-readable forms and pushes micro-detail to textures/normals.
