# DOC_GIA_BloodAxePathMarkerLODAndCollision_A01 Production Package

## Art Direction Summary

- Asset name: `DOC_GIA_BloodAxePathMarkerLODAndCollision_A01`
- Asset type: Non-shipping docs-only LOD and collision planning package
- Parent kit: `KIT_GIA_BloodAxePathMarkers_A01`
- Source planning row: `Blood Axe Village.png#Review_LODCollisionRows_A01`
- Related docs: `DOC_GIA_BloodAxePathMarkerReviewRows_A01`, `DOC_GIA_BloodAxePathMarkerScaleRows_A01`, and `KIT_GIA_BloodAxePathMarkers_A01`
- Faction/theme: Blood Axe Tribe, hostile Giant sub-faction only
- Status: docs-only planning package ready
- Scope: cairns, stakes, horn/bone warnings, shield scraps, ash bases, mixed clusters, review rows, and scale rows

`DOC_GIA_BloodAxePathMarkerLODAndCollision_A01` defines LOD0-LOD3 reduction policy and collision-limit guidance for the Blood Axe path-marker family. It is a planning reference for future separately approved work only. It does not claim any mesh, collision proxy, source asset, Unreal asset, validator, review actor, or final visual approval exists.

The visual direction remains crude Blood Axe Giant route dressing: rough field stone, scorched timber, oxide red cloth, old horn, dull bone, broken shield scrap, blackened iron, soot, ash, mud, and trampled camp ground. Blood Axe remains a hostile Giant sub-faction language and must stay separate from neutral/civilized Giant cave-town masonry, refined highland route markers, civic stoneworker motifs, warm hearth settlement language, terraces, waterworks, and restrained blue-rune culture.

This package stops before collision proxies, UCX meshes, nav blockers, gameplay volumes, validator files, DCC, FBX, Unreal Content, runtime implementation, final visual approval, first DCC target selection, implementation target selection, source concept movement, and Hermes work.

## Gameplay Purpose

The purpose is production guardrail planning only. The document gives future artists and implementers a shared policy for reducing path-marker detail and keeping collision simple, non-blocking, and non-gameplay-readable if a later approved lane opens.

Allowed planning uses:

- Define LOD0, LOD1, LOD2, and LOD3 expectations for cairn markers, cloth stakes, low red rags, horn/bone warnings, broken shield scraps, ash bases, mixed clusters, review rows, and scale rows.
- Protect MMO camera readability by preserving the main cairn, stake, cloth, horn, shield, ash, and mixed-cluster silhouettes before small detail is reduced.
- Establish collision guidance that defaults to disabled collision and allows only simple non-blocking query shapes in future separately approved temporary or review contexts.
- Keep review rows and scale rows non-shipping planning artifacts.
- Keep future path-marker dressing from becoming waypoint behavior, objective markers, nav/pathfinding helpers, or gameplay lanes.

Out of scope:

- Collision proxies, UCX meshes, nav blockers, nav modifiers, gameplay volumes, trigger volumes, objective volumes, damage volumes, aura volumes, interaction volumes, pickup volumes, collision correctness claims, traversal guarantees, DCC source creation, FBX export, Unreal Content creation, material instance creation, validator files, runtime source, Blueprint behavior, sockets, startup placement, final visual approval, first DCC target selection, implementation target selection, waypoint behavior, trail-marker gameplay, objective logic, nav/pathfinding behavior, pickup/loot behavior, resource behavior, crafting/economy behavior, AI behavior, encounter logic, VFX/audio, source concept movement, or Hermes files/config.

## Silhouette Notes

The LOD policy must protect the main Blood Axe marker reads before preserving small dressing. The future family should read as Giant-built hostile camp path dressing, not human-scale trail signage, neutral Giant civic wayfinding, polished monuments, ritual activation props, or UI markers.

Silhouette families covered by this reference:

- Cairn single markers: a few chunky stacked stones, broad base contact, soot and mud grounding, and no dense pebble piles.
- Cairn clusters: two to five rough marker beats with one dominant mass, uneven spacing, and readable path-bend compression without becoming a waypoint chain.
- Cloth stakes and low red rags: scorched timber, static broad oxide red cloth strips, hide ties, and simple torn shapes that do not require cloth simulation.
- Horn/bone warnings: blunt old horn, dull bone, horn forks, and sparse token forms used as non-graphic hostile cues.
- Broken shield scraps: large shield fragments, dull scrap plates, thick rims, rope ties, and faded red paint smears as static warning dressing only.
- Ash bases and ash path pads: low soot, cold ash, charcoal, burned grass, trampled mud, and irregular ground contact that supports markers without defining a gameplay path.
- Mixed clusters: one dominant cairn, stake, horn, or shield silhouette with two or three supporting elements and broad ash/mud grounding.
- Review rows and scale rows: non-shipping comparison layouts for policy, readability, and scale reference only. They are not final assets, Unreal actors, validators, captures, or startup placements.

Future geometry should spend form on primary stone masses, major stake shafts, broad cloth silhouettes, large horn/bone shapes, shield fragments, scrap plates, heavy lashings, and broad base shapes. Tiny stone chips, cloth weave, fray fibers, small rope fibers, scratches, pitting, soot speckles, ash flecks, red paint chips, wood grain, and mud streaks belong in future texture, normal, AO, or mask detail.

Do not let simplification produce UI arrows, readable text, objective frames, route signs, formal guideposts, polished civic markers, blue runes, warm hearth motifs, graphic gore, dense trophy piles, or a continuous breadcrumb trail.

## Scale Notes

Use the validated `SK_GIA_Base_A01` Giant scale lock exactly:

- Female Giant baseline: 442 cm / 14 ft 6 in.
- Male Giant baseline: 470 cm / 15 ft 5 in.
- Approved Giant ranges: females 14-15 ft / 427-457 cm; males 14 ft 10 in-16 ft 0 in / 452-488 cm.
- Future source, if separately authorized, should be authored in centimeters with 1 Unreal unit = 1 cm.

Planning references inherited from `KIT_GIA_BloodAxePathMarkers_A01`:

- Low rag or ash base: 20-120 cm vertical emphasis, with broad ground footprint as visual dressing only.
- Cairn single marker: 80-180 cm tall, 120-300 cm footprint.
- Cairn cluster: 120-260 cm tall, 250-600 cm footprint.
- Cloth stake marker: 140-280 cm above ground, with 40-160 cm static cloth drops or strips.
- Cloth stake pair or row: 250-700 cm combined footprint with rough uneven spacing, not fence spacing.
- Bone/horn marker: 80-220 cm tall, 80-250 cm footprint.
- Broken shield marker: 100-240 cm tall, 100-280 cm footprint.
- Mixed marker cluster: 120-300 cm height range with a 300-900 cm footprint and one dominant silhouette.
- Review rows and scale rows may show the 442 cm and 470 cm Giant references for comparison only.

These numbers are not gameplay measurements, path-width rules, nav/pathfinding values, collision dimensions, traversal guarantees, objective ranges, encounter-lane spacing, validator targets, camera approval metrics, terrain integration proof, or final placement rules.

## Materials and Color Palette

LOD and collision planning must support the established Blood Axe path-marker material read:

- Rough field stone, soot-stained boulders, cracked cairn slabs, mud-packed bases, and chipped gray stone planes.
- Scorched timber, raw pole cuts, dirty leather, hide ties, rawhide, rope lashings, and sinew cord.
- Torn oxide red cloth, faded red paint, dull maroon staining, soot-dark cloth edges, and weathered red wraps.
- Old horn, dull bone, blackened iron, dark steel, broken shield wood, scrap plate, and hammered shield rims.
- Packed earth, trampled mud, cold ash, charcoal, soot, burned grass, and camp grit.

Palette targets:

- Blood Axe red cloth and paint: `#5F1513` to `#8B211B`
- Charcoal and blackened iron: `#111214` to `#2A2C2E`
- Scorched timber: `#22170F` to `#4A2B17`
- Rough stone and ash: `#2E2C28` to `#6C6254`
- Rope, hide, and rawhide: `#6C5434` to `#A88958`
- Bone and horn accents: `#9E8C6B` to `#CDB78A`
- Mud and soot: `#0B0A09` to `#403025`

No default emissive is approved. Do not introduce Aetherium, magic glow, ritual activation, shamanic pulse, signal light, route glow, objective highlight, animated material state, or VFX material in this package.

Collision policy ignores material micro-detail. Soot speckles, chips, cloth weave, fray, rope fibers, red paint wear, pitting, scratches, mud streaks, ash flecks, horn rings, bone pores, and fine cracks should never create collision detail.

## Concept Image Prompt

Create an original stylized fantasy MMORPG documentation planning sheet of `DOC_GIA_BloodAxePathMarkerLODAndCollision_A01` for the world of Aerathea. The design should emphasize docs-only LOD0-LOD3 reduction policy, disabled-by-default collision intent, simple non-blocking future collision notes, Blood Axe Giant path-marker cairns, scorched cloth stakes, low red rags, horn and bone warnings, broken shield scraps, ash-stained bases, mixed marker clusters, review rows, scale rows, female 442 cm Giant and male 470 cm Giant scale references, rough field stone, scorched timber, oxide red cloth, blackened iron, dull bone and horn, soot, ash, mud, hostile Giant sub-faction identity, and strict separation from neutral/civilized Giant culture. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, no emissive glow, and MMO-friendly production design. Present it as a clean non-shipping policy board with LOD comparison rows, collision-limit callouts, material swatches, and scale references on a clean background. Avoid copying any existing franchise, avoid collision proxy diagrams that imply creation, avoid UCX mesh diagrams, avoid nav/pathfinding diagrams, avoid gameplay volumes, avoid trigger volumes, avoid objective volumes, avoid validators, avoid DCC or FBX claims, avoid Unreal Content claims, avoid runtime implementation, avoid final visual approval language, avoid implementation target selection, avoid waypoint behavior, avoid route validation, avoid pickup or loot behavior, avoid UI arrows, avoid readable signage, avoid VFX/audio, avoid neutral Giant cave-town architecture as Blood Axe default language, and avoid excessive micro-detail.

## Modeling Notes

This is not a modeling task. It creates no DCC source, mesh, sculpt, retopo, UVs, bake, proof render, LOD source, collision proxy, UCX mesh, FBX export, Unreal asset, material instance, texture asset, validator, runtime source, Blueprint, socket, animation, startup placement, final approval artifact, implementation file, or Hermes file/config.

Future separately scoped modeling packages should follow these rules:

- Build large silhouette carriers as geometry: main cairn stones, large base stones, major stake shafts, broad cloth shapes, large horn/bone warning forms, major shield fragments, scrap plates, heavy rope/rawhide knots, and broad ash/mud base shapes.
- Keep small surface language in texture or normal detail: tiny cracks, chips, soot speckles, ash flecks, cloth weave, rope fibers, stitching, scratches, pitting, paint chips, horn rings, bone pores, dried mud, and subtle wood grain.
- Keep marker modules modular only where it reduces repetition: single cairn, small cairn cluster, cloth stake, low rag, bone/horn marker, shield scrap marker, ash base, and mixed cluster.
- Keep review rows and scale rows visibly non-shipping through document layout and comparison framing, not through in-world finish.
- Preserve one dominant silhouette per marker or cluster so distant LODs can simplify without losing category read.
- Avoid dense pebble carpets, hundreds of cracks, graphic remains, readable route text, UI-like symbols, fine glyph panels, many nails, complex rope nets, cloth simulation strips, high-frequency damage, or material-slot sprawl.

No future module should be treated as selected for DCC, FBX, Unreal, runtime implementation, visual approval, first DCC target, or implementation target from this document alone.

## Texture and Material Notes

This package creates no texture, material instance, material graph, mask, atlas, source asset, or engine content. It defines texture and material policy only.

Future packages should use standard Aerathea texture outputs if separately authorized:

- Base Color / Albedo (`BC`)
- Normal (`N`)
- Packed Occlusion/Roughness/Metallic (`ORM`)
- Emissive (`E`) only for a separately scoped glowing variant; this baseline reference assumes no emissive

Texture detail should support LOD reduction:

- LOD0 can use normal and AO detail for broad cracks, chips, soot, ash, mud, cloth weave, rope direction, chipped paint, stone pitting, and large contact grime.
- LOD1 should preserve broad material value changes while reducing reliance on tiny normal detail.
- LOD2 should preserve stone, ash/mud, red cloth, horn/bone, and shield-scrap reads through large color blocks and baked-AO-style value separation.
- LOD3 should keep only broad dark stone mass, ash/soot grounding value, controlled red accents, and the strongest horn/shield silhouette cue where needed.

Material slot policy for future child assets:

- Cairn single, cloth stake, low red rag, bone/horn marker, broken shield marker, or ash base: 1 material target.
- Cairn cluster, cloth stake set, ash path base set, or shield lean marker: 1-2 material target.
- Mixed marker cluster: 1-2 material target, 3 maximum only if stone/ash, cloth/hide, and shield/metal/horn accents must be split for reuse.
- Review rows and scale rows: 1 simple utility material only if a later task creates temporary non-shipping row geometry.

Do not create unique materials for individual stones, cloth strips, ash patches, rope ties, horn chips, bone tokens, shield chips, iron scraps, soot speckles, lichen flecks, paint marks, mud streaks, or review labels.

## Triangle Budget

This package creates no mesh and has no shipping triangle budget. The values below are planning caps for future separately scoped path-marker packages, not minimum detail requirements or approval to model.

Future LOD0 budget bands:

- Cairn single marker: 1k-4k tris, 1 material target.
- Cairn cluster: 3k-8k tris, 1-2 material target.
- Cloth stake marker: 500-2k tris, 1 material target.
- Cloth stake pair or small row: 1.5k-5k tris, 1-2 material target.
- Low red rag marker: 300-1.2k tris, 1 material target.
- Bone/horn marker: 800-3k tris, 1 material target.
- Horn fork marker: 1k-3.5k tris, 1 material target.
- Broken shield marker or scrap shield lean marker: 1.5k-4k tris, 1-2 material target.
- Ash-stained base or ash trail pad: 300-1.2k tris, 1 material target.
- Mixed marker cluster: 4k-10k tris, 1-3 material target.
- Non-shipping review, scale, or LOD/collision row: 300-3k tris only if a later planning task creates temporary row geometry; no mesh by default.

LOD percentage planning targets:

- LOD1: 55-70 percent of LOD0 depending on silhouette complexity.
- LOD2: 30-45 percent of LOD0.
- LOD3: 10-25 percent of LOD0.

Spend triangles on primary stone masses, marker height silhouettes, broad cloth outlines, large horn/bone warning shapes, large shield fragments, chunky base contact, and strong mixed-cluster composition. Do not spend triangles on tiny cracks, pebble scatter, cloth weave, rope fibers, soot speckles, ash flecks, paint chips, mud flecks, small scratches, hidden underside bevels, or repeated tiny tokens.

## LOD Plan

All important future static path-marker modules need LOD0, LOD1, LOD2, and LOD3 before any separately scoped production import lane uses them. This package does not create LOD source files, DCC tasks, import settings, validators, or shipping assets.

Global LOD policy:

- LOD0: preserve full marker forms, major cairn stacking, stake shafts, broad cloth silhouettes, horn/bone warning shapes, shield fragments, ash/mud bases, large lashings, readable red paint or cloth marks, and authored material detail.
- LOD1: reduce secondary bevels, small chips, cloth edge cuts, rope subdivisions, minor knots, small stone wedges, shield splinters, minor base undercuts, back-facing detail, and hidden underside forms while keeping the marker category readable.
- LOD2: merge smaller stones into larger planes, simplify cloth to broad strips, flatten shallow fold and crack geometry, remove non-silhouette accents, reduce ash/mud ridge geometry, and preserve only the strongest red/stone/ash/horn/shield reads.
- LOD3: preserve primary asset identity only: broad cairn, stake, cloth, horn, shield, ash-base, or mixed-cluster silhouette plus one restrained Blood Axe material cue where needed.

Reduction order:

1. Remove texture-only detail from geometry assumptions first: tiny cracks, soot speckles, ash flecks, paint chips, cloth weave, rope fibers, fray, mud flecks, small scratches, horn rings, bone pores, and iron pitting.
2. Remove small accent geometry: minor lashings, small knots, cloth holes, tiny horn chips, little stone wedges, small metal nicks, small bone tokens, tiny rubble, and optional paint-chip geometry.
3. Remove hidden or low-value geometry: back-facing stones, underside bevels, buried contact cuts, interior clutter, and non-visible ash/mud undercuts.
4. Remove secondary decorations: duplicate foot stones, minor blackened iron scraps, small cloth tears, small horn or bone punctuation, and non-silhouette side tokens.
5. Simplify secondary form detail: stone bevel density, cloth fold geometry, ash/mud ridge geometry, shallow groove subdivisions, shield rim cuts, and optional review-row helper detail.
6. Only after small detail is gone, simplify the primary Giant-scale marker silhouette while preserving the Blood Axe identity cue.

Family-specific requirements:

- Cairn single markers must preserve the stacked large-stone read through LOD3.
- Cairn clusters must preserve uneven marker rhythm without simplifying into a continuous breadcrumb line.
- Cloth stakes and low red rags must preserve one broad oxide red cue where the variant depends on it; fray, knots, holes, and rope segment detail reduce first.
- Horn/bone warnings must preserve blunt non-graphic warning silhouettes; small token scatter reduces first.
- Broken shield scraps must preserve the largest shield or scrap plate read; small dents, cuts, and splinters reduce first.
- Ash bases must preserve broad dark grounding as value and shape, not as gameplay path information.
- Mixed clusters must preserve one dominant silhouette and reduce supporting tokens first.
- Review rows and scale rows use LOD terminology only to compare readability. They do not create LOD source files, DCC tasks, Unreal LOD groups, validators, captures, startup placement, or shipping assets.

Never reduce Giant-scale relationship, hostile Blood Axe sub-faction identity, primary marker category read, controlled red accent restraint, ash/mud grounding, or non-shipping review-row clarity before small detail is removed.

## Collision Notes

This package creates no collision. It defines disabled-by-default and simple non-blocking collision intent for future separately authorized path-marker planning, temporary review rows, or static dressing discussions. Do not create collision proxies, UCX meshes, Unreal collision settings, physics bodies, nav blockers, pathfinding helpers, smart links, gameplay volumes, trigger volumes, damage volumes, aura volumes, objective volumes, interaction volumes, pickup volumes, validator scripts, runtime setup, startup placement, or implementation files from this package.

Global collision policy:

- Default to collision disabled for all path-marker visual dressing, review rows, scale rows, ash, soot, mud, cloth, rope, rawhide, small stakes, horn chips, bone tokens, blackened iron scraps, paint, small stones, minor chips, scratches, and texture-only detail.
- If a future separately approved task needs selection, review, or editor query bounds, use one simple non-blocking primitive around the largest visual body or row footprint.
- Use query-only, non-blocking bounds for temporary review purposes; they must not block players, cameras, AI, navmesh, projectiles, or physics.
- Do not use complex-as-simple collision for repeated path-marker dressing.
- Do not use collision to prove navigation/pathfinding, traversal widths, route gates, encounter lanes, objectives, ritual boundaries, damage fields, aura fields, interaction affordances, cover, destructibility, loot pickup, resource gathering, quest logic, or terrain compatibility.

Family-specific collision intent:

- Cairn single markers: collision disabled by default. If separately approved for review selection, use one simple non-blocking box or low-count convex query hull around the main stone mass.
- Cairn clusters: collision disabled by default. If separately approved, use one to three simple non-blocking query primitives around major stone masses only; no per-stone collision.
- Cloth stakes and low red rags: collision disabled by default. If separately approved, use one slim non-blocking query capsule or box around the shaft only; no cloth collision.
- Bone/horn warnings: collision disabled by default. If separately approved, use one simple non-blocking query primitive around the main warning shape only; no per-bone or per-horn collision.
- Broken shield scraps: collision disabled by default. If separately approved, use one simple non-blocking query primitive around the largest fragment only; no pickup, loot, shield-use, cover, or interaction collision.
- Ash bases and ash path pads: collision disabled always unless a later separate task changes scope; no gameplay decal, trigger area, damage field, aura field, trail tracker, or route marker is defined.
- Mixed clusters: collision disabled by default. If separately approved for editor selection, use simple non-blocking query bounds around the cluster footprint or dominant mass only; no gameplay volume or nav helper collision.
- Review rows and scale rows: collision disabled always. They are non-shipping planning aids and must not receive collision proxies, UCX meshes, nav blockers, validators, startup placement, gameplay volumes, trigger volumes, objective volumes, or blocking collision.

This package makes no claim of collision correctness, collision guarantee, terrain integration, pathing validity, traversal clearance, player movement validity, combat cover, route blocking, camera clearance, objective-zone behavior, interaction behavior, runtime performance validation, route validation, nav/pathfinding validity, or final implementation readiness.

## Animation Notes

Baseline policy is static.

Allowed planning language:

- Static cairn markers, cairn clusters, cloth stakes, low red rags, horn/bone warnings, broken shield scraps, ash bases, mixed clusters, review rows, and scale rows.
- Static material variation for stone value, soot, ash, mud, cloth age, red paint wear, horn/bone age, blackened iron roughness, and grime if later material packages define it.
- Static non-shipping review and scale rows for LOD reduction, collision intent, and Giant-scale readability.

Not part of this package:

- Skeletal animation, cloth simulation, vertex wind, rope physics, dangling motion, flag waving, moving stones, physics collapse, destructible breakage, material pulse, glow, particles, VFX, audio, Blueprint state, interaction state, quest state, objective state, encounter state, damage state, aura state, waypoint behavior, route behavior, nav/pathfinding behavior, startup placement, runtime behavior, final approval, implementation target selection, first DCC target selection, or source concept movement.

Any moving, glowing, interactive, damaging, objective-readable, UI-readable, audio-linked, route-affecting, or gameplay-readable variant needs a separately named package and explicit scope.

## Unreal Import Notes

This section is planning policy only. No Unreal Content asset, import script, material instance, texture asset, socket, collision proxy, UCX mesh, Blueprint, validator, runtime source, review actor, startup actor, placement file, DCC source, FBX export, source asset folder, game-content folder, collision setup, nav/pathfinding setup, trigger setup, objective setup, quest/UI setup, interaction setup, VFX/audio setup, final approval, first DCC target, or implementation target is created or authorized.

Documentation identity:

- Asset name: `DOC_GIA_BloodAxePathMarkerLODAndCollision_A01`
- Asset type: Documentation-only LOD and collision planning package, not Static Mesh, Blueprint Actor, Material, VFX, UI, validator, or runtime source
- Documentation path: `docs/assets/kits/DOC_GIA_BloodAxePathMarkerLODAndCollision_A01/PRODUCTION_PACKAGE.md`
- Parent kit: `KIT_GIA_BloodAxePathMarkers_A01`
- Game asset status: none selected and none created
- Unreal folder path: not applicable; no game-content folder is selected
- Content path: blocked. Do not create, edit, move, import, or reference live files under `Content/Aerathea/` for this task.
- Source path: blocked. Do not create or edit `SourceAssets/`, DCC files, FBX files, proof renders, texture files, external source concept folders, runtime source, tool scripts, or Hermes files/config.
- Pivot guidance: not applicable to this documentation package
- Orientation guidance: not applicable to this documentation package
- Scale reference: female Giant 442 cm / 14 ft 6 in and male Giant 470 cm / 15 ft 5 in; approved Giant ranges remain females 14-15 ft / 427-457 cm and males 14 ft 10 in-16 ft 0 in / 452-488 cm
- Collision type: not applicable here; future policy is disabled by default and simple non-blocking query-only for separately authorized temporary review or selection needs
- LOD plan: planning reference only; no LOD source is created
- Material slot count: not applicable here; future child assets should keep material slots low as described above
- Texture list: not applicable here; future packages may use `BC`, `N`, and `ORM` outputs, with no baseline emissive
- Sockets: none
- Animation list: none
- Blueprint behavior: none
- Performance notes: preserve primary marker silhouettes through LODs, keep material slots low, keep collision disabled on review rows and small detail, avoid complex-as-simple collision, avoid blocking/nav/gameplay collision, and avoid gameplay-readable marker drift.

No folder path in `Content/Aerathea`, `SourceAssets`, `Tools/DCC`, `Tools/Unreal`, runtime source, validator folders, external source concept folders, startup maps, Hermes config, or any implementation lane is selected by this docs-only package.

## Folder and Naming Recommendation

Documentation path:

- `docs/assets/kits/DOC_GIA_BloodAxePathMarkerLODAndCollision_A01/PRODUCTION_PACKAGE.md`

Package naming:

- Recommended document package name: `DOC_GIA_BloodAxePathMarkerLODAndCollision_A01`
- Keep `GIA` for Giant ownership and `BloodAxe` for the hostile sub-faction.
- Keep `DOC` to show this is a non-shipping planning package, not a mesh, kit implementation, validator, or Unreal asset.
- Keep `LODAndCollision` to indicate policy scope only.

Related planning references:

- `KIT_GIA_BloodAxePathMarkers_A01`
- `DOC_GIA_BloodAxePathMarkerReviewRows_A01`
- `DOC_GIA_BloodAxePathMarkerScaleRows_A01`

Potential future child packages may reference this document for LOD and collision policy, but this package does not select, approve, or authorize any first DCC target, first implementation target, source/export folder, mesh name, material instance, texture, Unreal asset, validator, review actor, startup placement, or runtime behavior.

Do not create folders or files in `Content/Aerathea/`, `SourceAssets/`, `Tools/DCC/`, `Tools/Unreal/`, runtime source, Hermes config, global indexes, backlog/bootstrap, task boards, approval queues, external source concept locations, or neighboring package folders from this task.

## Quality Gate Checklist

- [ ] Package remains docs-only and limited to LOD/collision planning guardrails.
- [ ] Exactly the universal 15 sections are present with the required `##` headings.
- [ ] The document does not claim any mesh, collision proxy, source asset, Unreal asset, validator, review actor, startup placement, or final visual approval exists.
- [ ] Female Giant baseline is stated as 442 cm / 14 ft 6 in and male Giant baseline is stated as 470 cm / 15 ft 5 in.
- [ ] Blood Axe is described as a hostile Giant sub-faction only.
- [ ] Neutral/civilized Giant culture remains separate from Blood Axe raider path-marker language.
- [ ] Cairns, stakes, horn/bone warnings, shield scraps, ash bases, mixed clusters, review rows, and scale rows are all covered.
- [ ] LOD0, LOD1, LOD2, and LOD3 reduction policy is included without creating LOD source files.
- [ ] Collision guidance defaults to disabled collision and allows only simple non-blocking query shapes in future separately approved contexts.
- [ ] Collision guidance blocks collision proxies, UCX meshes, nav blockers, gameplay volumes, interaction volumes, trigger volumes, objective volumes, pickup volumes, blocking collision, and collision-correctness claims.
- [ ] The path-marker family remains visual dressing, not a trail, waypoint chain, route marker, objective line, tracking system, encounter lane, cover system, or navigation aid.
- [ ] No DCC, FBX, Unreal Content, validators, runtime files, startup placement, source concept movement, Hermes files/config, global indexes, approval queues, task board, backlog/bootstrap, first DCC target, or implementation target is authorized.
- [ ] Materials stay within rough field stone, scorched timber, soot, ash, mud, oxide red cloth, rawhide, rope, sparse blackened iron, old horn, dull bone, and broken shield scrap with no default emissive.
- [ ] Tiny stone chips, cloth weave, fray, stitches, scratches, pitting, soot speckles, ash flecks, paint chips, rope fibers, horn rings, bone pores, and wood grain remain texture or normal detail in future packages.
- [ ] Review rows and scale rows remain non-shipping document comparisons and do not imply captures, validators, startup placement, marker validation, final visual signoff, or implementation readiness.
