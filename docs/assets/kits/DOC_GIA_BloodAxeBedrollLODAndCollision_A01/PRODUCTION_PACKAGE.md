# DOC_GIA_BloodAxeBedrollLODAndCollision_A01 Production Package

## Art Direction Summary

- Asset name: `DOC_GIA_BloodAxeBedrollLODAndCollision_A01`
- Asset type: Non-shipping docs-only LOD and collision planning package
- Parent kit: `KIT_GIA_BloodAxeBedrollHideBundles_A01`
- Source planning row: `BloodAxeCamp.png#Review_LODCollisionRows_A01`
- Faction/theme: Blood Axe Tribe, hostile Giant sub-faction only
- Status: docs-only planning package ready

`DOC_GIA_BloodAxeBedrollLODAndCollision_A01` defines LOD0-LOD3 reduction policy and collision-limit guidance for Blood Axe hide rolls, rough bedding, tied bundles, lashings, shelter-adjacent piles, review rows, and scale rows. It is a planning reference only and does not claim any mesh, collision proxy, source asset, Unreal asset, validator, review actor, or final visual approval exists.

The policy preserves rough Blood Axe Giant camp dressing: low hide rolls, soot-dark bedding, lumpy tied bundles, thick rawhide lashings, rope coils, stake anchors, shelter-edge piles, ash, mud, and restrained oxide red cloth. Blood Axe remains a hostile Giant sub-faction and must stay separate from neutral/civilized Giant cave-town bedding, warm hearth domestic craft, refined highland textiles, civic stoneworker symbols, and restrained blue-rune culture.

This package stops before collision proxies, UCX meshes, nav blockers, gameplay volumes, validator files, DCC, FBX, Unreal Content, runtime implementation, final visual approval, first DCC target selection, implementation target selection, source concept movement, and Hermes work.

## Gameplay Purpose

The purpose is production guardrail planning only. This document gives future artists and implementers a shared policy for reducing bedroll and bundle detail while keeping collision simple, disabled by default, and non-gameplay-readable if a later approved lane opens.

Allowed planning uses:

- Define LOD0, LOD1, LOD2, and LOD3 expectations for hide rolls, hide roll stacks, open hide rolls, bedding pallets, ground bedding, fur sleep layers, tied bundles, rawhide lashings, rope coils, stake anchors, shelter piles, review rows, and scale rows.
- Protect MMO camera readability by preserving the primary low bedding mass, bundle silhouette, thick strap/lashing read, rope coil footprint, stake-anchor read, and shelter-edge pile composition before small detail is reduced.
- Establish collision guidance that defaults to disabled collision and allows only simple non-blocking query shapes in future separately approved review contexts.
- Keep review rows and scale rows non-shipping planning artifacts.

Out of scope:

- Collision proxies, UCX meshes, physics bodies, cloth collision, rope constraints, nav blockers, nav modifiers, gameplay volumes, trigger volumes, objective volumes, interaction volumes, pickup volumes, rest volumes, sleep markers, validator files, DCC source creation, FBX export, Unreal Content creation, material instance creation, runtime source, Blueprint behavior, sockets, startup placement, final visual approval, first DCC target selection, implementation target selection, inventory behavior, pickup behavior, loot behavior, resource behavior, bed/rest behavior, interaction behavior, AI behavior, encounter logic, VFX/audio, source concept movement, or Hermes files/config.

## Silhouette Notes

LOD policy must protect the major Blood Axe bedroll reads before preserving small dressing.

Silhouette families covered:

- Hide rolls: flattened cylinder mass, broad end caps, two thick straps, one restrained red tag, and compressed underside.
- Hide roll stacks: two to five low stacked roll masses with varied lengths, visible end caps, thick lashings, and uneven contact compression.
- Open hide rolls and ground bedding: broad low hide spread, rough flap edges, shallow dirt depression, and sparse fur edges.
- Rough bedding pallets and sleeping rows: long low Giant-scale bedding footprint, support layer, soot-dark bedding, broad folds, and row rhythm.
- Tied bundles and tied bundle sets: lumpy hide-wrapped masses, two thick straps, large knots, rope wraps, and varied squat/long/overstuffed shapes.
- Frame-strapped bundles: hide bundle lashed to crude timber frame or sled-like support as static dressing only.
- Rawhide lashings, rope coils, and stake anchors: thick loops, strap bands, large knots, blunt tied ends, ground stakes, tie rings, and rawhide anchor straps.
- Shelter-adjacent piles: readable composed groupings beside lean-tos or hide tents without becoming storage, loot, rest, or nav assets.
- Review rows and scale rows: non-shipping comparison layouts for readability, spacing, and scale. They are not Unreal actors, validators, captures, or startup placements.

Future geometry should spend form on primary roll, bedding, bundle, lashing, rope, stake, and pile silhouettes. Tiny hide grain, fur strands, rope fibers, cloth weave, fray, stitches, scratches, soot speckles, ash flecks, mud spatters, paint chips, pitting, and wood grain belong in future texture, normal, AO, or mask detail.

Do not let simplification produce storage-container reads, loot bags, usable beds, spawn markers, UI markers, objective icons, cover blocks, clean domestic bedding, warm hearth comfort, or neutral/civilized Giant craft.

## Scale Notes

Use the validated `SK_GIA_Base_A01` Giant scale lock exactly:

- Female Giant baseline: 442 cm / 14 ft 6 in.
- Male Giant baseline: 470 cm / 15 ft 5 in.
- Approved Giant ranges: females 14-15 ft / 427-457 cm; males 14 ft 10 in-16 ft 0 in / 452-488 cm.
- Future source, if separately authorized, should be authored in centimeters with 1 Unreal unit = 1 cm.

Planning references inherited from `KIT_GIA_BloodAxeBedrollHideBundles_A01`:

- Single hide roll: 240-480 cm long.
- Ground bedding: 450-620 cm long.
- Rough bedding pallet: 500-650 cm long.
- Tied camp bundle: 260-360 cm long.
- Rope coil tie: 130-260 cm outer diameter.
- Bundle stake anchor: 80-180 cm visible height above ground.
- Shelter pile or sleeping row: size varies by composition, but must read against the 442 cm and 470 cm Giant baselines.

These numbers are not gameplay measurements, path-width rules, nav/pathfinding values, collision dimensions, traversal guarantees, rest-system dimensions, objective ranges, encounter spacing, validator targets, camera approval metrics, or final placement rules.

## Materials and Color Palette

LOD and collision planning must support the established Blood Axe bedroll material read:

- Rough smoked hide, patched leather, dark sleeping hide, sparse dirty fur edges, thick rope, rawhide lashings, scorched timber, blackened iron, soot, ash, dried mud, and restrained oxide red cloth.
- Palette targets: dark umber, smoked brown, soot black, dirty tan, rawhide ochre, charcoal, dull gunmetal, ash gray, dried mud brown, faded maroon, and deep oxide red.
- Excluded language: neutral/civilized Giant blue-gray stone, refined cave-town bedding, polished highland domestic craft, warm hearth blankets, civic stoneworker symbols, clean nomad textiles, restrained blue runes, and default emissive.

Collision policy ignores material micro-detail. Hide pores, fur strands, rope fibers, cloth weave, soot speckles, ash flecks, mud spatters, scratches, pitting, red paint chips, and wood grain should never create collision detail.

## Concept Image Prompt

Create an original stylized fantasy MMORPG documentation planning sheet of `DOC_GIA_BloodAxeBedrollLODAndCollision_A01` for the world of Aerathea. The design should emphasize docs-only LOD0-LOD3 reduction policy, disabled-by-default collision intent, simple non-blocking future collision notes, Blood Axe Giant hide rolls, rough bedding pallets, ground bedding, fur sleep layers, tied bundles, rawhide lashings, rope coils, bundle stake anchors, shelter-adjacent piles, review rows, scale rows, female 442 cm Giant and male 470 cm Giant scale references, rough smoked hide, patched leather, scorched timber, blackened iron, rope, rawhide, soot, ash, mud, oxide red cloth, hostile Giant sub-faction identity, and strict separation from neutral/civilized Giant culture. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, no emissive glow, and MMO-friendly production design. Present it as a clean non-shipping policy board with LOD comparison rows, collision-limit callouts, material swatches, and scale references on a clean background. Avoid copying any existing franchise, avoid collision proxy diagrams that imply creation, avoid UCX mesh diagrams, avoid nav/pathfinding diagrams, avoid gameplay volumes, avoid usable-bed diagrams, avoid interaction volumes, avoid validators, avoid DCC or FBX claims, avoid Unreal Content claims, avoid runtime implementation, avoid final visual approval language, avoid implementation target selection, avoid pickup or loot behavior, avoid UI markers, avoid VFX/audio, avoid neutral Giant cave-town bedding as Blood Axe default language, and avoid excessive micro-detail.

## Modeling Notes

This is not a modeling task. It creates no DCC source, mesh, sculpt, retopo, UVs, bake, proof render, LOD source, collision proxy, UCX mesh, FBX export, Unreal asset, material instance, texture asset, validator, runtime source, Blueprint, socket, animation, startup placement, final approval artifact, implementation file, or Hermes file/config.

Future separately scoped modeling packages should follow these rules:

- Build large silhouette carriers as geometry: main hide-roll bodies, broad end caps, large bedding folds, support logs, lumpy bundle masses, thick strap bands, large knots, rope coil turns, ground stakes, tie rings, and shelter-pile composition masses.
- Keep small surface language in texture or normal detail: hide grain, fur strands, cloth weave, tiny stitches, fray fibers, rope fibers, scratches, pitting, soot speckles, ash flecks, mud spatters, red paint chips, wood grain, and small cracks.
- Preserve one dominant silhouette per asset or composed pile so distant LODs can simplify without losing category read.
- Avoid dense strap fields, fine rope nets, simulated cloth strips, high-frequency damage, graphic trophy reads, storage compartments, inventory labels, rest markers, or material-slot sprawl.

No future module should be treated as selected for DCC, FBX, Unreal, runtime implementation, visual approval, first DCC target, or implementation target from this document alone.

## Texture and Material Notes

This package creates no texture, material instance, material graph, mask, atlas, source asset, or engine content. It defines texture and material policy only.

Future packages should use standard Aerathea texture outputs if separately authorized:

- Base Color / Albedo (`BC`)
- Normal (`N`)
- Packed Occlusion/Roughness/Metallic (`ORM`)
- Emissive (`E`) only for a separately scoped glowing variant; this baseline reference assumes no emissive

Texture detail should support LOD reduction:

- LOD0 can use normal and AO detail for broad hide folds, strap pressure, rope direction, soot, ash, mud, patched leather, scorched timber, and blackened iron wear.
- LOD1 should preserve broad material value changes while reducing reliance on tiny normal detail.
- LOD2 should preserve hide, bedding, rope/rawhide, timber, ash/mud, and red-cloth reads through large color blocks and baked-AO-style value separation.
- LOD3 should keep only broad dark hide mass, ash/soot grounding, thick strap/lashing reads, and the strongest red accent where needed.

Material slot policy for future child assets:

- Small props such as rope coils, stake anchors, single rolls, and threshold bundles: 1 material target, 2 maximum.
- Larger bedding pallets, hide roll stacks, tied bundle sets, shelter piles, and sleeping rows: 1-2 material target, 3 maximum only if hide/leather, timber/iron, and rope/red cloth must be split for reuse.
- Review rows and scale rows: 1 simple utility material only if a later task creates temporary non-shipping row geometry.

Do not create unique materials for every strap, knot, hide patch, fur edge, mud spot, ash streak, red cloth strip, rope turn, timber scratch, iron chip, or review label.

## Triangle Budget

This package creates no mesh and has no shipping triangle budget. The values below are planning caps for future separately scoped packages, not minimum detail requirements or approval to model.

Future LOD0 budget bands:

- Single hide roll, rope coil, stake anchor, or threshold bundle: 800-3,500 tris.
- Open hide roll, ground bedding, fur sleep layer, or tied camp bundle: 1,500-6,000 tris.
- Rough bedding pallet, hide roll stack, tied bundle set, shelter pile, lean-to edge pile, or sleeping row: 3,000-10,000 tris depending on composition.
- Non-shipping review, scale, or LOD/collision row: 300-3,000 tris only if a later planning task creates temporary row geometry; no mesh by default.

LOD percentage planning targets:

- LOD1: 55-70 percent of LOD0.
- LOD2: 30-45 percent of LOD0.
- LOD3: 10-25 percent of LOD0.

Spend triangles on primary roll/bedding/bundle/pile mass, end caps, thick straps, large knots, rope coil turns, stake heads, support logs, and broad bedding folds. Do not spend triangles on tiny stitches, hide pores, fur strands, rope fibers, soot speckles, ash flecks, mud grains, small scratches, red paint chips, or hidden underside detail.

## LOD Plan

All important future static bedroll and bundle modules need LOD0, LOD1, LOD2, and LOD3 before any separately scoped production import lane uses them. This package does not create LOD source files, DCC tasks, import settings, validators, or shipping assets.

Global LOD policy:

- LOD0: preserve full roll, bedding, bundle, lashing, rope, stake, and pile forms with major folds, large knots, thick straps, major support shapes, readable red accents, and authored material detail.
- LOD1: reduce secondary bevels, small fold cuts, minor strap wrinkles, rope subdivisions, knot undercuts, small fur-edge cuts, tiny red accents, back-facing detail, and hidden underside forms while keeping category read.
- LOD2: merge smaller folds into larger planes, simplify knots and strap loops, reduce end-cap geometry, remove non-silhouette accents, and preserve only the strongest hide/strap/rope/red reads.
- LOD3: preserve primary asset identity only: flattened roll, broad bedding sheet, lumpy bundle, rope coil, stake anchor, or shelter-pile silhouette plus one restrained Blood Axe material cue where needed.

Reduction order:

1. Remove texture-only detail from geometry assumptions first: hide grain, fur strands, cloth weave, tiny stitches, rope fibers, fray, soot speckles, ash flecks, mud spatters, scratches, red paint chips, pitting, and wood grain.
2. Remove small accent geometry: secondary lashings, tiny knots, cloth holes, minor strap cuts, small tie ends, little hide patches, and optional red fragments.
3. Remove hidden or low-value geometry: underside bevels, buried contact cuts, interior pile clutter, hidden back-facing folds, and non-visible support details.
4. Remove secondary decorations: duplicate tags, minor iron rings, small rope loops, secondary timber chips, and non-silhouette side tokens.
5. Simplify secondary form detail: end-cap layer density, cloth fold geometry, ash/mud ridge geometry, shallow groove subdivisions, support-log bevels, and optional review-row helper detail.
6. Only after small detail is gone, simplify the primary Giant-scale roll, bedding, bundle, rope, stake, or pile silhouette.

Never reduce Giant-scale relationship, hostile Blood Axe sub-faction identity, primary category read, controlled red accent restraint, ash/mud grounding, or non-shipping review-row clarity before small detail is removed.

## Collision Notes

This package creates no collision. It defines disabled-by-default and simple non-blocking collision intent for future separately authorized bedroll and bundle planning, temporary review rows, or static dressing discussions. Do not create collision proxies, UCX meshes, Unreal collision settings, physics bodies, cloth collision, rope constraints, nav blockers, gameplay volumes, trigger volumes, rest volumes, sleep markers, objective volumes, interaction volumes, pickup volumes, validator scripts, runtime setup, startup placement, or implementation files from this package.

Global collision policy:

- Default to collision disabled for all bedroll and bundle visual dressing, review rows, scale rows, cloth, rope, rawhide, fur edges, ash, soot, mud, straps, knots, tags, small stakes, small iron rings, scratches, chips, and texture-only detail.
- If a future separately approved task needs editor selection or review bounds, use one simple non-blocking primitive around the largest visual body or row footprint.
- Use query-only, non-blocking bounds for temporary review purposes; they must not block players, cameras, AI, navmesh, projectiles, or physics.
- Do not use complex-as-simple collision for repeated bedroll, bedding, bundle, lashing, or shelter-pile dressing.
- Do not use collision to prove navigation/pathfinding, traversal widths, usable beds, rest triggers, encounter lanes, objectives, interaction affordances, cover, destructibility, loot pickup, resource gathering, or terrain compatibility.

Family-specific collision intent:

- Single rolls, rope coils, stake anchors, and threshold bundles: collision disabled by default; if separately approved, one simple non-blocking query primitive.
- Ground bedding, fur sleep layers, and open hide rolls: collision disabled by default; no cloth collision, rest volume, or sleep marker.
- Bedding pallets, hide roll stacks, tied bundle sets, shelter piles, lean-to piles, and sleeping rows: collision disabled by default; if separately approved for editor selection, use broad simple query bounds only.
- Review rows and scale rows: collision disabled always. They are non-shipping planning aids and must not receive collision proxies, UCX meshes, nav blockers, validators, startup placement, gameplay volumes, trigger volumes, objective volumes, or blocking collision.

This package makes no claim of collision correctness, terrain integration, traversal clearance, player movement validity, rest-system validity, combat cover, route blocking, camera clearance, objective-zone behavior, interaction behavior, runtime performance validation, nav/pathfinding validity, or final implementation readiness.

## Animation Notes

Baseline policy is static.

Allowed planning language:

- Static hide rolls, bedding spreads, fur layers, tied bundles, lashings, rope coils, stake anchors, shelter-adjacent piles, review rows, and scale rows.
- Static material variation for hide tone, soot, ash, mud, fur age, rawhide color, rope wear, timber scorch, blackened iron roughness, and red cloth intensity if later material packages define it.

Not part of this package:

- Skeletal animation, cloth simulation, vertex wind, rope physics, dangling motion, physics collapse, destructible breakage, material pulse, glow, particles, VFX, audio, Blueprint state, interaction state, quest state, objective state, encounter state, rest state, pickup state, inventory state, nav/pathfinding behavior, startup placement, runtime behavior, final approval, implementation target selection, first DCC target selection, or source concept movement.

Any moving, glowing, interactive, rest-linked, lootable, inventory-linked, audio-linked, route-affecting, or gameplay-readable variant needs a separately named package and explicit scope.

## Unreal Import Notes

This section is planning policy only. No Unreal Content asset, import script, material instance, texture asset, socket, collision proxy, UCX mesh, Blueprint, validator, runtime source, review actor, startup actor, placement file, DCC source, FBX export, source asset folder, game-content folder, collision setup, nav/pathfinding setup, trigger setup, objective setup, quest/UI setup, interaction setup, rest setup, VFX/audio setup, final approval, first DCC target, or implementation target is created or authorized.

Documentation identity:

- Asset name: `DOC_GIA_BloodAxeBedrollLODAndCollision_A01`
- Asset type: Documentation-only LOD and collision planning package, not Static Mesh, Blueprint Actor, Material, VFX, UI, validator, or runtime source
- Documentation path: `docs/assets/kits/DOC_GIA_BloodAxeBedrollLODAndCollision_A01/PRODUCTION_PACKAGE.md`
- Parent kit: `KIT_GIA_BloodAxeBedrollHideBundles_A01`
- Game asset status: none selected and none created
- Unreal folder path: not applicable; no game-content folder is selected
- Content path: blocked. Do not create, edit, move, import, or reference live files under `Content/Aerathea/` for this task.

## Folder and Naming Recommendation

Documentation path:

- `docs/assets/kits/DOC_GIA_BloodAxeBedrollLODAndCollision_A01/PRODUCTION_PACKAGE.md`

Document identity:

- `DOC_GIA_BloodAxeBedrollLODAndCollision_A01`
- Parent: `KIT_GIA_BloodAxeBedrollHideBundles_A01`
- Related review docs: `DOC_GIA_BloodAxeBedrollReviewRows_A01`, `DOC_GIA_BloodAxeBedrollScaleRows_A01`, and `DOC_GIA_BloodAxeBedrollMaterialDiscipline_A01`

No DCC folder, SourceAssets path, FBX export path, Unreal path, validator path, startup actor, source concept copy, first DCC target, implementation target, or Hermes file is created or selected by this package.

## Quality Gate Checklist

- Uses the 442 cm / 14 ft 6 in female Giant and 470 cm / 15 ft 5 in male Giant scale lock.
- Covers hide rolls, rough bedding, tied bundles, lashings, shelter-adjacent piles, review rows, and scale rows.
- Protects Blood Axe hostile Giant identity and excludes neutral/civilized Giant bedding, cave-town craft, warm hearth domestic language, blue runes, and default emissive.
- Defines LOD0-LOD3 planning and reduction order without creating LOD source files.
- Defines disabled-by-default/simple-query collision policy without creating collision proxies, UCX meshes, physics bodies, nav blockers, gameplay volumes, rest volumes, or validators.
- Keeps review and scale rows non-shipping.
- Does not authorize DCC, FBX, Unreal Content, runtime source, startup placement, final visual approval, first DCC target, implementation target, source concept movement, or Hermes work.
