# DOC_GIA_BloodAxeStorageLODAndCollision_A01 Production Package

Docs-only LOD and collision policy package for Blood Axe Giant storage clutter. This package creates no collision proxies, no UCX meshes, no nav blockers, no gameplay volumes, no validators, no DCC source, no Unreal Content, no startup placement, no final approval, no source concept movement, no Hermes work, and no implementation target.

## Art Direction Summary

- Asset name: `DOC_GIA_BloodAxeStorageLODAndCollision_A01`
- Asset type: Docs-only policy package
- Parent kit: `KIT_GIA_BloodAxeCratesSacksBaskets_A01`
- Source planning row: `Blood Axe Village.png#Review_StorageLODAndCollisionRows_A01`
- Faction/theme: Blood Axe Tribe, hostile Giant sub-faction only
- Status: docs-only LOD/collision policy ready

This document sets policy for future LOD0-LOD3 reduction and collision limits across crates, sacks, baskets, rope bindings, covered bundles, shelter-edge clusters, gate-interior clusters, and storage stack clusters.

## Gameplay Purpose

The policy keeps future static storage dressing performant and prevents documentation from overclaiming collision, navigation, cover, destruction, or interaction behavior.

Out of scope: collision proxy creation, UCX meshes, nav blockers, gameplay volumes, validator files, DCC, Unreal Content, startup placement, final approval, implementation target selection, cover rules, destructible behavior, nav/pathfinding behavior, route clearance, loot, pickup, interaction, resource, vendor, economy, VFX/audio, and runtime behavior.

## Silhouette Notes

LOD policy must protect the primary storage read:

- Crates keep block mass, broad planks, large straps, and major lids.
- Sacks keep sagging bodies, tied necks, and grounded bases.
- Baskets keep thick rims and broad weave ribs.
- Rope bindings keep large coils and knots, not fiber detail.
- Covered bundles keep tarp/hide silhouette and major tie-downs.
- Clusters keep broad footprint, stepped mass, and clear non-barricade storage identity.

Remove tiny detail before primary silhouette, Giant scale, or Blood Axe/civilized Giant separation.

## Scale Notes

- Giant scale lock: female 442 cm / 14 ft 6 in baseline and male 470 cm / 15 ft 5 in baseline.
- Approved Giant ranges: females 14-15 ft / 427-457 cm and males 14 ft 10 in-16 ft 0 in / 452-488 cm.
- LOD and collision decisions must be validated against Giant-scale storage mass in future implementation lanes.
- This policy does not define player clearance, route clearance, or gameplay collision.

## Materials and Color Palette

LOD reduction must preserve material-family readability: rough timber, blackened iron, rope/rawhide, dirty sackcloth, basket weave, hide covers, soot, ash, mud, and restrained oxide red accents. Do not preserve tiny wear before preserving material read and silhouette. No emissive baseline is approved.

## Concept Image Prompt

Create an original stylized fantasy MMORPG production planning board of `DOC_GIA_BloodAxeStorageLODAndCollision_A01` for the world of Aerathea. The design should emphasize docs-only LOD0-LOD3 and collision-limit policy for Blood Axe Giant storage clutter, crates, sacks, baskets, rope bindings, covered bundles, shelter-edge clusters, gate-interior clusters, storage stack clusters, silhouette-protection rows, disabled-by-default collision guidance, simple low collision exceptions only as future approval notes, female Giant baseline 442 cm / 14 ft 6 in, male Giant baseline 470 cm / 15 ft 5 in, hostile Giant sub-faction identity, and separation from neutral/civilized Giant culture. Use readable shapes, hand-painted material swatches, baked-AO-style depth, no emissive glow, and MMO-friendly mid-poly planning discipline. Present it as a clean policy board with LOD rows, collision guardrails, scale references, and no-build callouts. Avoid copying any existing franchise, avoid collision proxy claims, avoid navmesh diagrams, avoid gameplay volume diagrams, avoid validator creation, avoid Unreal implementation screenshots, avoid DCC source claims, avoid final approval, avoid cover/destructible/interaction behavior, and avoid excessive micro-detail.

## Modeling Notes

Future modelers should create LOD0-LOD3 only under a separate approved DCC task. This policy recommends broad silhouette simplification and texture-backed micro-detail. It does not create source files, collision meshes, proxy geometry, validators, or import assets.

## Texture and Material Notes

Small details removed from geometry should move to Base Color, Normal, and ORM maps in future implementation: grain, weave, fibers, stitching, scratches, soot, ash, mud, paint wear, and metal pitting. No texture assets or materials are created here.

## Triangle Budget

Future budget guidance:

- Small props: 800-5k tris LOD0.
- Medium crates/sacks/baskets: 2k-8k tris LOD0.
- Rope/binding sets: 1k-5k tris LOD0.
- Covered bundles: 2k-7k tris LOD0.
- Composed clusters: 8k-28k tris LOD0 depending on footprint.

LOD targets: LOD1 at 55-70 percent, LOD2 at 30-45 percent, LOD3 at 10-25 percent of LOD0. These are planning targets only.

## LOD Plan

- LOD0: full silhouette and main material zones.
- LOD1: remove small bevels, minor folds, tiny hardware, secondary lashing loops, and hidden underside detail.
- LOD2: simplify smaller components, collapse weave/fiber/folds into normal maps, reduce rope coils, and remove backside-only detail.
- LOD3: preserve broad storage mass, footprint, material read, and one restrained Blood Axe accent.

Reduction order: micro-detail, secondary ropes, minor folds, small hardware, hidden backsides, redundant filler, then non-shipping helper detail.

## Collision Notes

Collision default: disabled for purely visual dressing. If later placement needs collision, use simple low blocking/query volumes that approximate broad mass only. Do not create or claim UCX collision, nav blockers, cover volumes, gameplay trigger volumes, destructible collision, gate collision, route clearance, player clearance, physics piles, or collision correctness from this policy.

## Animation Notes

No animation is planned. LOD/collision policy does not authorize cloth, rope, physics, breakage, material-state, VFX, audio, or runtime animation behavior.

## Unreal Import Notes

Future Unreal imports, if separately approved, must confirm LOD0-LOD3, material slot count, disabled/simple collision, centimeter scale, and no gameplay components. This package creates no Unreal Content, import scripts, validators, review actors, startup actors, Blueprints, materials, textures, or map edits.

## Folder and Naming Recommendation

- Package: `docs/assets/kits/DOC_GIA_BloodAxeStorageLODAndCollision_A01/PRODUCTION_PACKAGE.md`
- Policy ID: `DOC_GIA_BloodAxeStorageLODAndCollision_A01`
- No source, export, validator, collision, or Unreal folder is selected.

## Quality Gate Checklist

- [x] Docs-only policy package.
- [x] Includes all universal Aerathea package sections.
- [x] Uses female 442 cm and male 470 cm Giant scale lock.
- [x] Keeps Blood Axe as a hostile Giant sub-faction separate from neutral/civilized Giant culture.
- [x] Blocks collision proxies, UCX meshes, nav blockers, gameplay volumes, validators, DCC, Unreal Content, startup placement, final approval, and implementation target selection.
- [x] Preserves silhouette-first LOD policy without claiming runtime collision or gameplay behavior.
