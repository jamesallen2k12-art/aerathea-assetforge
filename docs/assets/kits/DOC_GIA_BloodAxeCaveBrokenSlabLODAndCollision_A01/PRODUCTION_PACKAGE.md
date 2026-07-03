# DOC_GIA_BloodAxeCaveBrokenSlabLODAndCollision_A01 Production Package

## Art Direction Summary

- Asset name: `DOC_GIA_BloodAxeCaveBrokenSlabLODAndCollision_A01`
- Asset type: Docs-only LOD and collision policy package
- Task: `AET-MA-20260629-247`
- Parent kit: `KIT_GIA_BloodAxeCaveBrokenSlabRemnants_A01`
- Parent intake row: `BloodAxeCaveBrokenSlabRemnants_A01#LODCollisionReference_A01`
- Parent policy reference: `DOC_GIA_BloodAxeCaveApproachLODAndCollision_A01`
- Material reference: `DOC_GIA_BloodAxeCaveApproachMaterialDiscipline_A01`
- Scale dependency: validated `SK_GIA_Base_A01` Giant scale lock
- Faction/theme: Blood Axe Tribe, hostile Giant sub-faction only
- Scope: documentation policy only; no asset implementation

`DOC_GIA_BloodAxeCaveBrokenSlabLODAndCollision_A01` defines the focused LOD0-LOD3 reduction and disabled/simple collision policy for future Blood Axe broken slab remnant rows: primary broken slab cluster, split slab pair, ash-grounded slab, painted slab, small chock stones, and review rows. It narrows the broader cave approach LOD/collision policy to static broken threshold stones, chipped oxide red paint, cold ash, trampled mud, cave grit, and sparse Giant-scale support stones.

Blood Axe broken slab dressing must remain the language of a hostile Giant sub-faction. It may use rough highland stone, soot, ash, trampled mud, cave grit, chipped oxide red paint, sparse rope or rawhide residue, blackened iron flecks, old horn, and dull bone. It must not become neutral/civilized Giant culture. Neutral/civilized Giant culture remains tied to hidden highland cave towns, skilled stonework, blue-gray civic masonry, terraces, waterworks, warm hearth identity, monumental craft, and restrained civic rune language.

This package defines policy only. It does not create collision proxies, UCX meshes, nav blockers, gameplay volumes, trigger volumes, route blocker setup, objective volumes, validators, DCC files, FBX exports, Unreal Content, runtime source, source asset folders, startup placement, review actors, material instances, texture assets, sockets, animation assets, final approvals, or first implementation target selections.

## Gameplay Purpose

The gameplay purpose is production guardrail planning only. These rules help future broken slab remnant packages keep static cave-edge memory dressing readable, inexpensive, and separate from gameplay behavior.

Allowed planning uses:

- Define LOD0-LOD3 expectations for future primary broken slab clusters, split slab pairs, ash-grounded slabs, painted slabs, small chock stones, and review rows.
- Define disabled-by-default and simple-major-slab-only collision policy aligned with the parent cave approach planning.
- Preserve broken slab remnants as static visual history: damaged threshold stones, old paint, ash, mud, soot, and cave grit.
- Keep Giant-scale broken slab dressing cheap enough for repeated cave approach use.
- Protect neutral/civilized Giant culture from Blood Axe hostile raider visual drift.

Out of scope:

- Collision proxies, UCX meshes, nav blockers, gameplay volumes, trigger volumes, route blocker setup, objective volumes, validator work, DCC work, FBX work, Unreal Content work, runtime implementation, cave gameplay, traversal proof, path widths as gameplay values, route validation, interaction behavior, cover rules, destructible behavior, quest/UI markers, encounter triggers, spawn logic, patrol logic, damage/aura behavior, VFX/audio, material graph behavior, startup placement, final visual approval, final cave approval, or implementation target selection.

## Silhouette Notes

LOD policy must protect the primary broken slab read before preserving decoration. Every future broken slab child row should keep its Giant-scale shape readable at MMO camera distance:

- Primary broken slab cluster: low heavy threshold mass with one to three dominant snapped stones, broad fractured planes, clear slab thickness, and wide contact shadows.
- Split slab pair: two large broken pieces with offset rotation, an obvious split relationship, and no clean doorway, gate, route lane, or blocker silhouette.
- Ash-grounded slab: one broad slab seated into cold ash, trampled mud, soot, and cave grit; the ground mass supports the slab without becoming a gameplay zone.
- Painted slab: a static slab with chipped dirty red paint or broad faded warning swipes; paint must stay visual and must not read as text, UI, glyphs, or objective signs.
- Small chock stones: sparse wedge-like support stones around major slabs, large enough to read at Giant scale and never numerous enough to become rubble clutter.
- Review rows: non-shipping comparison rows for slab width, LOD reduction, paint density, ash/mud grounding, collision policy, and Giant scale readability.

Future asset packages should model real geometry only for silhouette carriers: major slab bodies, large broken planes, slab thickness, chunky chipped corners, few wedge-like chock stones, and major ash or mud lips that affect contact read. Tiny cracks, soot speckles, ash flecks, grit dots, paint chips, lichen, scratches, mud streaks, small pitting, rope fibers, horn rings, and bone pores belong in future textures, normals, AO, roughness, or masks.

LOD reduction must never turn broken slab remnants into UI arrows, readable signs, route blockers, polished monuments, neutral/civilized Giant cave-town masonry, or refined civic stonework.

## Scale Notes

Use the validated `SK_GIA_Base_A01` Giant scale lock in every future broken slab package:

- Female Giant baseline: 442 cm / 14'6".
- Male Giant baseline: 470 cm / 15'5".
- Approved Giant ranges: females 14-15 ft / 427-457 cm and males 14'10"-16'0" / 452-488 cm.
- Future source, if separately approved, should be authored in centimeters with 1 Unreal unit = 1 cm.

Scale guidance for future policy consumers:

- Primary broken slab cluster footprint: roughly 360-950 cm wide by 240-720 cm deep.
- Major slab piece: roughly 180-520 cm long, 80-260 cm wide, and 35-110 cm thick.
- Split slab pair: roughly 320-850 cm total span, with uneven height and offset rotation.
- Ash-grounded slab: roughly 260-650 cm slab footprint on a 380-1050 cm non-circular ash/mud base.
- Painted slab: roughly 160-460 cm long and 80-220 cm wide, with paint occupying about 5-10 percent of visible surface.
- Small chock stones: roughly 30-120 cm tall and 40-180 cm long, used sparsely around major slabs.
- Review rows should place female 442 cm and male 470 cm Giant baselines beside slab cluster, split pair, ash-grounded slab, painted slab, chock stone, LOD, and collision policy examples.

These are visual production planning values only. They are not collision proof, pathing data, traversal clearance, route blocker sizing, encounter spacing, objective ranges, interaction ranges, camera approval, terrain integration proof, or implementation guidance.

## Materials and Color Palette

LOD and collision policy must support the broken slab material discipline:

- Rough highland stone, dark fractured slabs, soot-blackened threshold stone, weathered granite, chipped pale stone edges, and cave-edge field rock.
- Packed earth, trampled mud, cold ash, charcoal dust, cave grit, dry stone dust, and old threshold dirt.
- Chipped oxide red paint, dirty maroon stains, faded red warning swipes, old paint residue, and controlled Blood Axe accent marks.
- Sparse rope residue, rawhide scraps, blackened iron flecks, old horn chips, and dull bone tokens only where they support a secondary hostile read.

Palette policy:

- Deep stone and soot: `#151718`, `#222527`, `#343635`, `#4E4D47`
- Weathered stone and ash: `#67645E`, `#827B70`, `#A49B8E`, `#C0B5A3`
- Cave grit and mud: `#241D17`, `#382C22`, `#554332`, `#6F5B45`
- Chipped Blood Axe red paint: `#551311`, `#6B1A16`, `#81251D`, `#98372B`
- Rope, rawhide, and worn leather residue: `#4E3925`, `#684F33`, `#8E7048`
- Sparse blackened iron, old horn, and dull bone: `#0F1011`, `#383D3E`, `#72664F`, `#AE986B`

Material ratio guidance:

- Stone, soot, ash, grit, and mud should carry roughly 80-90 percent of the visual read.
- Chipped oxide red paint should stay around 5-10 percent of any slab composition.
- Rope residue, rawhide, iron, horn, bone, and lichen should remain sparse accent reads.
- Emissive is absent by default. Glow, signal light, ritual light, shamanic pulse, torch state, UI highlight, or animated material state requires a separately scoped package.

Collision policy must ignore material micro-detail. Paint chips, cracks, soot, ash, mud, grit, pitting, lichen, rope residue, horn chips, bone pores, and iron flecks should never drive collision detail.

## Concept Image Prompt

Create an original stylized fantasy MMORPG production policy sheet of `DOC_GIA_BloodAxeCaveBrokenSlabLODAndCollision_A01` for the world of Aerathea. The design should emphasize broken slab remnant LOD0-LOD3 reduction policy, disabled-by-default and simple-major-slab-only collision policy, primary broken slab cluster, split slab pair, ash-grounded slab, painted slab, small chock stones, review rows, Giant-scale readability, rough highland stone, soot-blackened threshold slabs, cold ash, trampled mud, cave grit, chipped oxide red paint, sparse rope or rawhide residue, blackened iron flecks, old horn, dull bone, hostile Blood Axe Giant sub-faction identity, strict separation from neutral/civilized Giant culture, and the role of static cave-edge memory dressing only. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, no default emissive glow, and MMO-friendly mid-poly production design. Present it as a docs-only policy board with LOD comparison rows, collision-disabled callouts, simple hull policy notes without implementation diagrams, material swatches, and scale markers beside female 442 cm and male 470 cm Giant baselines on a clean background. Avoid copying any existing franchise, avoid cave gameplay, avoid route signs, avoid objective or quest marker language, avoid navigation/pathfinding diagrams, avoid collision proxy diagrams that imply implementation, avoid neutral Giant cave-town architecture, avoid readable text, avoid magic glow, avoid graphic gore, and avoid excessive micro-detail that would not translate to mid-poly Unreal assets.

## Modeling Notes

This is not a modeling task. It creates no DCC source, mesh, sculpt, retopo, UVs, bakes, proof renders, LOD source files, collision proxies, UCX meshes, FBX exports, Unreal assets, material instances, textures, validators, runtime source, review actors, startup placement, or implementation files.

Future modeling packages should follow these policy rules:

- Primary broken slab cluster: model one to three major slab bodies, broad broken planes, clear slab thickness, large chipped corners, and contact-friendly ash or mud base forms only where they support silhouette.
- Split slab pair: model two large snapped stones with offset stance and asymmetry; do not shape the pair as a functional doorframe, gate, route marker, or blocker.
- Ash-grounded slab: model the main slab and only the broad ash/mud lips that read in silhouette; keep ash flecks and grit in texture.
- Painted slab: model the base slab only; chipped red paint remains material detail and never creates raised gameplay symbols or collision-relevant geometry.
- Small chock stones: model a few large wedge stones only; avoid dense pebble carpets, climb-assist shapes, cover silhouettes, or physics-prop reads.
- Review rows: keep row geometry non-shipping and utility-oriented if a later task ever approves it; review rows are not gameplay actors.

LOD modeling policy:

- Future LOD0 meshes carry all large forms and major silhouette cuts.
- Future LOD1 meshes reduce small geometry while preserving the broken slab identity.
- Future LOD2 meshes simplify to broad planes, masses, and color beats.
- Future LOD3 meshes preserve only the primary Giant-scale silhouette, low cave-edge grounding, and strongest Blood Axe red paint beat.

Do not model dense cracks, ash grains, soot puffs, grit flecks, readable text, UI-like signs, magic glyphs, cave trigger markers, route helper arrows, gore-heavy residue, or high-frequency damage.

## Texture and Material Notes

This package creates no texture, material instance, material graph, mask, atlas, trim sheet, or engine content. It defines texture and material policy only.

Future packages should use standard Aerathea texture outputs:

- Base Color / Albedo (`BC`)
- Normal (`N`)
- Packed Occlusion/Roughness/Metallic (`ORM`)
- Emissive (`E`) only for a separately scoped glowing variant; baseline broken slab LOD/collision policy assumes no emissive

Texture detail should carry detail removed through LODs:

- LOD0 can use normal and AO detail for broad cracks, chipped edges, soot, ash, lichen, mud streaks, pitting, and red paint wear.
- LOD1 should keep broad material value changes and reduce reliance on tiny normal detail.
- LOD2 should preserve stone, ash, mud, and red paint reads through large color blocks and baked AO.
- LOD3 should keep only broad dark slab mass, cold ash/mud grounding, and one restrained Blood Axe red paint or accent read where needed.

Material slot policy:

- Single major broken slabs, split slab pairs, painted slabs, and simple chock stone sets: 1 material target.
- Ash-grounded slabs and primary broken slab clusters: 1-2 material target.
- Larger mixed slab compositions: 2 material target, 3 maximum only when stone/soil, paint/rawhide, and iron/horn/bone truly need separation in a separately scoped child package.
- Review rows: 1 simple utility material if a later task defines non-shipping review geometry.
- Do not assign unique material slots for individual cracks, paint chips, ash patches, mud streaks, chock stones, horn chips, bone tokens, iron flecks, soot deposits, or lichen specks.

## Triangle Budget

This package creates no mesh. Triangle values below are future policy targets for separately scoped packages.

Future LOD0 budget bands:

- Single major broken slab: 1.2k-4k tris, 1 material.
- Primary broken slab cluster: 4k-12k tris total, 1-2 materials.
- Split slab pair: 3k-9k tris total, 1 material target.
- Ash-grounded slab: 2.5k-8k tris total, 1-2 materials.
- Painted slab: 1.5k-5k tris, 1-2 materials.
- Small chock stone set: 500-2.5k tris total, usually included in a slab module.
- Non-shipping review row: 300-2k tris per row only if a later planning task creates row geometry.

LOD percentage policy:

- LOD1: 60-70 percent of LOD0, depending on slab complexity.
- LOD2: 35-45 percent of LOD0.
- LOD3: 15-25 percent of LOD0.

Spend triangles on primary silhouette and contact readability: main slab bodies, visible thickness, broad broken planes, large chipped corners, wedge-like chock stones, and major ash/mud grounding forms. Do not spend triangles on tiny cracks, ash flecks, soot speckles, paint chips, grit specks, lichen, mud droplets, rope fibers, hidden underside detail, or small scratches.

## LOD Plan

All important future static broken slab modules need LOD0, LOD1, LOD2, and LOD3 before any production import lane uses them.

Global broken slab LOD policy:

- LOD0: full slab massing, major fractured planes, visible slab thickness, chunky chipped corners, broad contact bases, major ash/mud lips, large chock stones where present, restrained red paint support, and authored material detail.
- LOD1: reduce secondary bevels, small chipped edges, minor chock stone bevels, paint-edge geometry, underside cuts, small ash ridges, rear-facing damage, and non-silhouette rubble.
- LOD2: simplify slabs into larger planes, merge small chock stones into the base read, flatten ash and mud lips, remove non-silhouette accent pieces, and preserve only broad stone/ash/mud/red paint reads.
- LOD3: preserve primary asset identity only: low broken threshold footprint, one or two broad broken planes, cave-edge grounding value, and a restrained Blood Axe red paint beat if needed.

Reduction order for all broken slab families:

1. Remove texture-only detail from geometry assumptions first: tiny cracks, soot speckles, ash flecks, grit dots, lichen specks, paint chips, stone pitting, mud droplets, rope fibers, horn rings, bone pores, and minor scratches.
2. Remove small accent geometry: tiny stone wedges, small chock chips, little paint-edge cuts, minor horn chips, dull bone tokens, small iron nicks, and shallow mud crumbs.
3. Remove hidden or low-value geometry: back-facing stones, underside slab bevels, hidden contact cuts, rear-only damage, interior cluster clutter, and non-visible ash/mud undercuts.
4. Remove secondary decorations: duplicate foot stones, small paint islands, minor blackened iron flecks, little horn or bone pieces, and non-silhouette scraps.
5. Simplify secondary form detail: slab bevel density, ash/mud ridge geometry, shallow groove subdivisions, broken-edge density, and optional review-row helper detail.
6. Only after small detail is gone, simplify primary silhouettes while preserving Giant-scale read, Blood Axe material identity, and static broken threshold readability.

Family-specific LOD requirements:

- Primary broken slab cluster: preserve the low heavy cluster footprint, dominant slab count, broad fractured faces, and contact shadow through LOD3. Remove small shards, underside bevels, redundant chock stones, and paint chips first.
- Split slab pair: preserve the two-piece snapped relationship and offset stance through LOD3. Remove edge chips, small wedges, backside damage, and minor split-line cuts before reducing the two main bodies.
- Ash-grounded slab: preserve the broad slab-on-ash/mud read through LOD3. Remove grit, ash flecks, small pebbles, mud crumbs, and base-edge noise before simplifying the slab footprint.
- Painted slab: preserve one clear restrained oxide red warning beat through LOD3. Remove paint-chip geometry, minor surface cuts, and secondary stains before reducing the slab mass.
- Small chock stones: merge or remove small wedges early unless they carry the Giant-scale support read. Preserve only a few large wedges if they are essential to the composition.
- Review rows: preserve row layout intent only if future non-shipping geometry exists. LODs may be simplified aggressively because review rows are planning aids, and collision remains disabled.

Never reduce the Giant-scale relationship, Blood Axe red/black warning identity, static cave-edge memory read, or primary broken slab silhouettes before removing small detail.

## Collision Notes

This package creates no collision. It defines disabled-by-default and simple-only collision policy for future static broken slab modules. Do not create collision proxies, UCX meshes, Unreal collision settings, physics bodies, nav blockers, pathfinding helpers, smart links, gameplay volumes, trigger volumes, route blocker setup, damage volumes, aura volumes, objective volumes, interaction volumes, validator scripts, or runtime setup from this package.

Global collision policy:

- Default to collision disabled for visual dressing, review rows, ash, mud, soot, cave grit, chipped paint, decals, lichen, small chock stones, tiny chips, horn tokens, bone accents, iron flecks, rope residue, rawhide scraps, and non-contact details.
- Use simple primitive collision only when a later implementation lane explicitly needs basic player or camera blocking on a large static slab body.
- Prefer simple boxes or low-count convex hulls around major slab masses only.
- Do not use complex-as-simple collision for repeated broken slab dressing.
- Do not use collision to prove navigation/pathfinding, traversal widths, route gates, encounter lanes, objectives, cave entry logic, damage fields, aura fields, interaction affordances, cover, destructibility, loot pickup, resource gathering, or quest logic.

Family-specific collision policy:

- Primary broken slab cluster: collision disabled by default. If basic contact is required later, use one simple hull around the dominant slab footprint, with optional simple support hulls only for other major slab masses. Do not define route blocker behavior, walkable surface behavior, cover rules, interaction collision, damage fields, or objective zones.
- Split slab pair: collision disabled by default. If later contact is needed, use one simple primitive or low-count hull per major slab. The pair must not become a gate volume, route validator, nav blocker, puzzle boundary, trigger volume, or objective frame.
- Ash-grounded slab: collision disabled for ash, mud, soot, cave grit, decals, paint, lichen, small pebbles, and contact stains. If later contact is needed, use a simple slab hull only; ash and mud must not become damage zones, aura zones, objective zones, trigger areas, or gameplay fields.
- Painted slab: collision follows the base slab only if separately approved. Paint receives no collision, no interaction collision, no glyph collision, no UI collision, and no material-state collision.
- Small chock stones: collision disabled by default. Only large chock stones that are part of a separately approved major static hull may receive simple collision; no climb-assist, cover, physics-prop, destructible, route-blocker, or interaction behavior is defined.
- Review rows: collision disabled always. Review rows are non-shipping planning aids and must not receive collision proxies, UCX meshes, nav blockers, validators, startup placement, or gameplay volumes.

Small accents with collision always disabled:

- Paint chips, soot marks, ash piles, mud streaks, cave grit, lichen, tiny cracks, minor bevels, small stones, rope residue, rawhide scraps, horn chips, dull bone tokens, blackened iron flecks, scratches, and all texture-only detail.

## Animation Notes

Baseline policy is static.

Allowed planning language:

- Static primary broken slab clusters, split slab pairs, ash-grounded slabs, painted slabs, small chock stones, and review rows.
- Static material variation for stone value, soot, ash, red paint wear, lichen, mud, cave grit, and roughness if a later material task defines it.

Not part of this package:

- Skeletal animation, physics collapse, destructible states, movable slabs, puzzle movement, cloth simulation, vertex wind, rope physics, material pulse, ritual activation, VFX/audio, gameplay state change, quest/objective state, waypoint behavior, route blocker behavior, aura behavior, damage behavior, interaction behavior, patrol/spawn behavior, runtime animation, startup placement, or final approval.

Any future moving, glowing, interactive, damaging, aura-emitting, quest-readable, waypoint-readable, route-affecting, or gameplay-active variant must be split into its own scoped package.

## Unreal Import Notes

This section is planning policy only. No Unreal Content asset, import script, material instance, texture asset, socket, collision proxy, Blueprint, validator, runtime source, review actor, startup actor, placement file, DCC source, FBX export, route blocker setup, trigger setup, gameplay volume setup, nav/pathing setup, or implementation file is created or authorized.

Potential future identity after a separately scoped production lane:

- Asset family: Blood Axe cave broken slab static remnant modules and docs-only review rows.
- Candidate folder family: `/Game/Aerathea/Props/Giants/BloodAxeCamp/CaveApproach/BrokenSlabs/`
- Candidate review folder family: `/Game/Aerathea/Review/Giants/BloodAxe/CaveApproach/BrokenSlabs/`
- Pivot policy: base center for standalone slabs and chock stone sets; cluster center for primary broken slab clusters, split slab pairs, ash-grounded compositions, and review rows.
- Orientation policy: primary readable side faces +X unless a later export convention sets another direction.
- Scale policy: centimeter-authored source, imported at scale 1.0, preserving female 442 cm and male 470 cm Giant baselines.
- Collision policy: disabled by default; simple primitive collision only for major static slab masses when a future lane explicitly needs basic contact; review rows always disabled.
- LOD policy: LOD0-LOD3 required for important shipping modules before production import.
- Material slot policy: 1 target for stone-only slabs, split pairs, and chock stone sets; 2 target for ash-grounded or painted variants; 3 maximum for larger mixed clusters only under separate approval.
- Texture policy: `BC`, `N`, and `ORM` by default; no baseline emissive.
- Sockets: none by default.
- Animation list: none by default.
- Blueprint behavior: none.

Candidate future names for planning reference only:

- `DOC_GIA_BloodAxeCaveBrokenSlabLODAndCollision_A01`
- `SM_GIA_BloodAxeCaveBrokenSlabCluster_A01`
- `SM_GIA_BloodAxeCaveSplitSlabPair_A01`
- `SM_GIA_BloodAxeCaveAshGroundedSlab_A01`
- `SM_GIA_BloodAxeCavePaintedSlab_A01`
- `SM_GIA_BloodAxeCaveChockStones_A01`
- `DOC_GIA_BloodAxeCaveBrokenSlabReviewRows_A01`

These names are planning references only. This package does not select a first DCC, FBX, Unreal, source asset, runtime, gameplay, cave approval, final visual, or implementation target.

## Folder and Naming Recommendation

- Docs folder: `docs/assets/kits/DOC_GIA_BloodAxeCaveBrokenSlabLODAndCollision_A01/`
- Package file: `docs/assets/kits/DOC_GIA_BloodAxeCaveBrokenSlabLODAndCollision_A01/PRODUCTION_PACKAGE.md`
- Asset/document ID: `DOC_GIA_BloodAxeCaveBrokenSlabLODAndCollision_A01`
- Parent kit: `KIT_GIA_BloodAxeCaveBrokenSlabRemnants_A01`
- Parent intake row: `BloodAxeCaveBrokenSlabRemnants_A01#LODCollisionReference_A01`
- Parent approach policy: `DOC_GIA_BloodAxeCaveApproachLODAndCollision_A01`
- Material policy: `DOC_GIA_BloodAxeCaveApproachMaterialDiscipline_A01`

Future planning labels only:

- `BrokenSlab_PrimaryCluster_LODPolicy`
- `BrokenSlab_SplitSlabPair_LODPolicy`
- `BrokenSlab_AshGrounded_LODPolicy`
- `BrokenSlab_PaintedSlab_LODPolicy`
- `BrokenSlab_ChockStones_LODPolicy`
- `BrokenSlab_ReviewRows_CollisionDisabled`
- `BrokenSlab_MajorSlab_SimpleCollisionOnly`

Do not create source asset folders, DCC files, FBX exports, game content folders, material instances, texture assets, validators, global index edits, backlog edits, task-board edits, startup placement, external source concept copies, runtime files, VFX/audio assets, collision proxy files, UCX meshes, route blocker files, nav/pathing files, trigger volumes, gameplay volumes, or unrelated package files from this task.

## Quality Gate Checklist

- Package is docs-only and changes no DCC, FBX, Unreal Content, runtime source, startup scene, external concept, validator, material instance, texture asset, VFX/audio asset, global index, task board, backlog, bootstrap, or unrelated package file.
- Universal 15-section Aerathea format is present.
- Scope is focused on `DOC_GIA_BloodAxeCaveBrokenSlabLODAndCollision_A01`, not the full cave approach family.
- Primary broken slab cluster, split slab pair, ash-grounded slab, painted slab, small chock stones, and review rows are covered.
- LOD0, LOD1, LOD2, and LOD3 expectations are defined for future important static broken slab modules.
- Reduction order removes texture-only and small detail before reducing primary broken slab silhouettes.
- Collision policy is disabled by default and simple-major-slab-only when a later implementation lane explicitly needs basic contact.
- No collision proxies, UCX meshes, nav blockers, gameplay volumes, trigger volumes, route blocker setup, validators, DCC, FBX, Unreal Content, runtime implementation, startup placement, final approvals, or first implementation target selections are created or authorized.
- Blood Axe remains a hostile Giant sub-faction, separate from neutral/civilized Giant culture.
- Giant scale lock is explicit: female 442 cm / 14'6" and male 470 cm / 15'5".
- Approved Giant ranges are explicit: females 14-15 ft / 427-457 cm and males 14'10"-16'0" / 452-488 cm.
- Broken slab remnants remain broad static threshold memory dressing with chipped red paint and ash/mud cave-edge grounding.
- No cave compatibility proof, traversal proof, path widths as gameplay values, route validation, route blocker behavior, interaction behavior, cave gameplay, collision correctness, nav/pathfinding, quest/UI markers, encounter triggers, objective markers, readable signage, VFX/audio, source asset creation, startup placement, final cave approval, or final visual approval is defined.
- Review rows are clearly non-shipping and do not imply Unreal actors, validators, captures, startup placement, marker validation, camera approval, final cave approval, or final visual signoff.
- Default emissive, glow, animated material states, gameplay VFX, audio cues, UI-like markers, readable text, objective cues, neutral/civilized Giant language, graphic gore, and high-frequency micro-detail are absent and approval-gated.
