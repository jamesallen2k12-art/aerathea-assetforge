# DOC_GIA_BloodAxeCaveRemnantClusterLODAndCollision_A01 Production Package

## Art Direction Summary

- Asset name: `DOC_GIA_BloodAxeCaveRemnantClusterLODAndCollision_A01`
- Asset type: Docs-only LOD and collision policy package
- Parent planning source: `KIT_GIA_BloodAxeCaveRemnantCluster_A01`
- Parent child row: `BloodAxeCaveRemnantCluster_A01#LODCollisionPlanning_A01`
- Related packages: `SM_GIA_BloodAxeCaveRemnantCairn_A01`, `SM_GIA_BloodAxeCollapsedCaveRemnantCairn_A01`, `SM_GIA_BloodAxeLowCaveStandingStone_A01`, `SM_GIA_BloodAxeBrokenLeaningCaveStone_A01`, `SM_GIA_BloodAxeCaveAshMudBase_A01`, `SM_GIA_BloodAxeColdCaveFireScar_A01`, and `KIT_GIA_BloodAxeCaveRemnantThreshold_A01`
- Faction/theme: Blood Axe Tribe, hostile Giant sub-faction only
- Scope: documentation policy only; no asset implementation

`DOC_GIA_BloodAxeCaveRemnantClusterLODAndCollision_A01` defines future LOD0-LOD3 reduction policy and disabled/simple collision limits for the Blood Axe cave-remnant cluster family. It covers low cairns, collapsed cairns, low standing stones, broken leaning stones, old cloth, ash/mud bases, cold fire scars, threshold kits, broken slab threshold variants, half-buried stone clusters, review rows, and material rows.

Blood Axe cave-remnant dressing must stay separate from neutral/civilized Giant culture. The family may use rough highland stone, soot, ash, trampled mud, cave grit, fixed oxide red cloth, rope, rawhide, sparse blackened iron, old horn, and dull bone. It must not become refined Giant cave-town masonry, warm hearth identity, blue-gray civic stonework, terrace/waterwork language, peaceful highland wayfinding, carved civic ornament, or restrained blue-rune culture.

This package creates no collision proxies, UCX meshes, nav blockers, gameplay volumes, trigger volumes, objective volumes, validators, DCC source, FBX export, Unreal Content, runtime implementation, startup placement, final approval, implementation target, source concept movement, or Hermes work.

## Gameplay Purpose

The gameplay purpose is production guardrail planning only. These rules preserve static environmental-history readability while preventing cave-remnant dressing from becoming gameplay geometry or navigation language.

Allowed planning uses:

- Define LOD0-LOD3 simplification priorities for future cave-remnant static modules.
- Define disabled-by-default and simple-major-stone-only collision policy.
- Keep cave-remnant modules cheap, readable, and reusable for future MMO environment dressing.
- Preserve Blood Axe hostile Giant sub-faction identity without drifting into neutral/civilized Giant culture.
- Provide a shared policy reference for QA when future package rows move toward DCC review.

Out of scope:

- Collision proxies, UCX meshes, nav blockers, gameplay volumes, trigger volumes, objective volumes, validators, DCC work, FBX work, Unreal Content work, runtime implementation, cave gameplay, cave compatibility proof, traversal proof, path widths as gameplay values, route validation, interaction behavior, cover rules, destructible behavior, quest/UI markers, encounter triggers, spawn logic, patrol logic, damage/aura behavior, VFX/audio, material graph behavior, startup placement, final visual approval, final cave approval, or implementation target selection.

## Silhouette Notes

LOD policy must protect the primary cave-remnant read before preserving decoration:

- Low cairn and collapsed cairn: preserve a few large rough stones, low abandoned mass, broad contact shadows, and cold ash/mud grounding.
- Low standing stone and broken leaning stone: preserve short fractured slab height, broad chipped faces, heavy base contact, and non-civic roughness.
- Old cloth and draped scrap: preserve one broad fixed oxide red shape only when it supports Blood Axe identity; cloth fray, weave, and small tears reduce first.
- Ash/mud base and cold fire scar: preserve non-circular low footprint, cold matte value, and broken edge rhythm while removing fine soot, grit, and char detail.
- Threshold and half-buried cluster kits: preserve compact asymmetrical stone/cloth/ash relationship, not a clean gate, doorway, route lane, or objective frame.
- Review rows, scale rows, material rows, and closure docs are non-shipping planning aids and must not become actors, captures, validators, startup placements, or final approvals.

Future packages should model real geometry only for silhouette carriers: large stones, broad broken planes, slab thickness, major ash or mud lips, simple cloth planes, large rope/rawhide wraps, and a few major chock or support stones. Tiny cracks, soot speckles, ash flecks, grit dots, paint chips, lichen, scratches, mud streaks, cloth weave, rope fibers, horn rings, and bone pores belong in textures, normals, AO, roughness, or masks.

## Scale Notes

Use the validated `SK_GIA_Base_A01` Giant scale lock:

- Female Giant baseline: 442 cm / 14 ft 6 in.
- Male Giant baseline: 470 cm / 15 ft 5 in.
- Approved Giant ranges: females 14-15 ft / 427-457 cm and males 14 ft 10 in-16 ft / 452-488 cm.
- Future source, if separately approved, should be authored in centimeters with 1 Unreal unit = 1 cm.

Policy scale bands for future packages:

- Single low cairn or collapsed cairn: 70-210 cm tall, 180-520 cm footprint.
- Low standing stone or broken leaning stone: 110-280 cm tall, below tall standing-stone packages.
- Cloth wrap or draped cloth scrap: 30-220 cm long, fixed and visually subordinate.
- Ash/mud base or cold fire scar: 220-1050 cm footprint, 1-45 cm high depending on ground lip.
- Compact threshold kit: 420-900 cm wide by 280-680 cm deep.
- Broken slab threshold and half-buried cluster variants: 380-1050 cm footprint with low, broken, non-doorway silhouettes.

These are visual production planning values only. They are not collision proof, pathing data, traversal clearance, route blocker sizing, encounter spacing, objective ranges, interaction ranges, camera approval, terrain integration proof, or implementation guidance.

## Materials and Color Palette

LOD and collision policy must support the cave-remnant material discipline:

- Rough highland stone, dark fractured slabs, soot-blackened cave-edge stones, weathered granite, ash-stained field rock, and cold cave grit.
- Packed earth, trampled mud, cold ash, charcoal dust, dry stone dust, and old threshold dirt.
- Fixed oxide red cloth, dirty maroon wraps, chipped red paint, rawhide, rope, old leather, sparse blackened iron, old horn, and dull bone.

Palette policy:

- Deep stone and soot: `#111313`, `#202223`, `#343635`, `#4D4B45`
- Weathered stone and ash: `#66635C`, `#817A70`, `#A19788`, `#B8AD9C`
- Cave grit and mud: `#211811`, `#382A20`, `#54402F`, `#6B533D`
- Blood Axe oxide red: `#50110F`, `#681816`, `#7C221B`, `#913127`
- Rope, rawhide, old horn, and bone: `#4F3A25`, `#6B5134`, `#91744B`, `#AA9468`
- Sparse blackened iron: `#101112`, `#232424`, `#373532`

Material ratio guidance:

- Stone, ash, mud, soot, and grit should carry most of the visual read.
- Oxide red cloth or paint should remain restrained and weathered.
- Rope, rawhide, horn, bone, and iron should stay sparse secondary reads.
- No baseline emissive. Glow, signal light, ritual pulse, torch state, UI highlight, smoke, particles, or animated material state requires a separately scoped package.

## Concept Image Prompt

Create an original stylized fantasy MMORPG docs-only LOD and collision policy sheet of `DOC_GIA_BloodAxeCaveRemnantClusterLODAndCollision_A01` for the world of Aerathea. The design should emphasize Blood Axe Giant cave-remnant LOD0-LOD3 reduction policy, disabled-by-default and simple-major-stone-only collision policy, low cairns, collapsed cairns, low standing stones, broken leaning stones, old fixed cloth, ash/mud bases, cold fire scars, compact threshold kits, half-buried stone clusters, non-shipping review rows, Giant-scale readability, rough highland stone, soot, cold ash, trampled mud, cave grit, restrained oxide red cloth, hostile Giant sub-faction identity, strict separation from neutral/civilized Giant culture, and static environmental history only. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, no default emissive glow, and MMO-friendly mid-poly production design. Present it as a policy board with LOD comparison rows, collision-disabled callouts, simple hull policy notes without implementation diagrams, material swatches, and scale markers beside female 442 cm and male 470 cm Giant baselines. Avoid copying any existing franchise, avoid cave gameplay, avoid route signs, avoid objective or quest marker language, avoid navigation/pathfinding diagrams, avoid collision proxy diagrams that imply implementation, avoid neutral Giant cave-town architecture, avoid readable text, avoid magic glow, avoid active fire or smoke, and avoid excessive micro-detail.

## Modeling Notes

This is not a modeling task. It creates no DCC source, mesh, sculpt, retopo, UVs, bakes, proof renders, LOD source files, collision proxies, UCX meshes, FBX exports, Unreal assets, material instances, textures, validators, runtime source, review actors, startup placement, source concept movement, Hermes work, or implementation files.

Future modeling packages should follow these policy rules:

- Build primary mass from a few large forms instead of dense rubble or pebble carpets.
- Keep low cairns and collapsed cairns broad, grounded, and abandoned.
- Keep standing stones short, fractured, and cluster-bound, not monumental or civic.
- Keep cloth as fixed broad shapes or texture-led resting folds, never simulation-ready.
- Keep ash/mud and fire-scar bases low and non-circular so they do not read as gameplay zones.
- Keep threshold variants asymmetrical and broken; they must not become gates, doorway frames, route markers, encounter lanes, or objective frames.
- Keep review rows and scale rows non-shipping and documentation-oriented.

Do not model dense cracks, ash grains, soot puffs, grit flecks, readable text, UI-like signs, magic glyphs, cave trigger markers, route helper arrows, gore-heavy residue, high-frequency damage, or collision-helper geometry in visible assets.

## Texture and Material Notes

This package creates no texture, material instance, material graph, mask, atlas, trim sheet, or engine content. It defines texture and material policy only.

Future packages should use standard Aerathea texture outputs:

- Base Color / Albedo (`BC`)
- Normal (`N`)
- Packed Occlusion/Roughness/Metallic (`ORM`)
- Emissive (`E`) only for a separately scoped glowing variant; baseline cave-remnant policy assumes no emissive

Texture detail should carry detail removed through LODs:

- Fine stone cracks, soot speckles, ash flecks, grit dots, cloth weave, fray, rope fibers, chipped paint, lichen, mud streaks, and small scratches are texture-led.
- AO should ground stone contacts, cloth trapped under stones, ash/mud lips, and collapsed cairn pockets.
- ORM should keep roughness high, metallic near zero, and metallic only for rare blackened iron accents if separately approved.

Material slot policy:

- Single stone or ground props: 1 material target.
- Mixed stone/cloth props: 1-2 material target.
- Larger threshold or half-buried kits: 1-2 material target, 3 maximum only under separate approval.
- Review rows: 1 simple utility material if a later task defines non-shipping review geometry.

## Triangle Budget

This package creates no mesh. Triangle values below are future policy targets for separately scoped packages.

Future LOD0 budget bands:

- Low cairn or collapsed cairn: 800-5k tris.
- Low standing stone or broken leaning stone: 1.2k-5k tris.
- Old cloth wrap or draped scrap: 250-1.8k tris, usually part of a stone module.
- Ash/mud base or cold fire scar: 350-3k tris.
- Compact threshold kit: 4k-10k tris.
- Broken slab threshold or half-buried cluster: 4k-12k tris.
- Non-shipping review row: 300-2k tris per row only if a later planning task creates row geometry.

LOD percentage policy:

- LOD1: 60-70 percent of LOD0.
- LOD2: 35-45 percent of LOD0.
- LOD3: 15-25 percent of LOD0.

Spend triangles on primary silhouette and contact readability: main stone bodies, visible thickness, broad broken planes, large chipped corners, simple cloth shape, major ash/mud grounding, and broad threshold footprint. Do not spend triangles on tiny cracks, ash flecks, soot speckles, paint chips, grit specks, lichen, mud droplets, rope fibers, hidden underside detail, or small scratches.

## LOD Plan

All important future cave-remnant static modules need LOD0, LOD1, LOD2, and LOD3 before any production import lane uses them.

Global cave-remnant LOD policy:

- LOD0: full stone massing, major fractured planes, broad cloth shapes, ash/mud contact, cold fire-scar footprint, and authored material detail.
- LOD1: reduce secondary bevels, small chipped edges, cloth edge cuts, underside cuts, small ash ridges, char fragments, and rear-facing detail.
- LOD2: simplify stones into larger planes, merge small support stones, flatten ash/mud lips, reduce cloth fold geometry, and preserve only broad stone/ash/mud/red reads.
- LOD3: preserve primary asset identity only: low abandoned remnant footprint, one or two broad stone masses, cave-edge grounding value, and one restrained Blood Axe red beat if needed.

Reduction order:

1. Tiny cracks, soot speckles, ash flecks, grit dots, lichen specks, paint chips, stone pitting, mud droplets, rope fibers, cloth weave, horn rings, bone pores, and minor scratches.
2. Tiny stones, minor chock chips, small cloth tears, little paint-edge cuts, tiny knots, and shallow mud crumbs.
3. Back-facing stones, underside bevels, hidden contact cuts, rear-only damage, interior cluster clutter, and non-visible ash/mud undercuts.
4. Duplicate foot stones, small paint islands, minor blackened iron flecks, small horn or bone pieces, and non-silhouette scraps.
5. Slab bevel density, ash/mud ridge geometry, cloth fold subdivisions, broken-edge density, and optional review-row helper detail.
6. Only after small detail is gone, simplify primary silhouettes while preserving Giant-scale read, Blood Axe identity, and static cave-remnant readability.

Never reduce a cluster into a clean gate, path marker, objective ring, waypoint chain, or neutral/civilized Giant civic marker.

## Collision Notes

This package creates no collision. It defines disabled-by-default and simple-only collision policy for future static cave-remnant modules. Do not create collision proxies, UCX meshes, Unreal collision settings, physics bodies, nav blockers, pathfinding helpers, smart links, gameplay volumes, trigger volumes, route blocker setup, damage volumes, aura volumes, objective volumes, interaction volumes, validator scripts, runtime setup, source assets, or Hermes files from this package.

Global collision policy:

- Default to collision disabled for visual dressing, review rows, scale rows, material rows, ash, mud, soot, cave grit, chipped paint, lichen, cloth, rope, rawhide, horn, bone, small stones, and non-contact details.
- Use simple primitive collision only when a later implementation lane explicitly needs basic player or camera blocking on a large static stone body.
- Prefer simple boxes or low-count convex hulls around major stone masses only.
- Do not use complex-as-simple collision for repeated cave-remnant dressing.
- Do not use collision to prove navigation/pathfinding, traversal widths, route gates, encounter lanes, objectives, cave entry logic, damage fields, aura fields, interaction affordances, cover, destructibility, loot pickup, resource gathering, or quest logic.

Family-specific collision policy:

- Low cairn and collapsed cairn: collision disabled by default; optional simple hull only around dominant stones if separately approved.
- Low standing stone and broken leaning stone: collision disabled by default; optional simple slab hull only under later approval.
- Old cloth and draped cloth: collision disabled always unless a future task defines a major stone carrier separately; cloth itself receives no collision.
- Ash/mud base and cold fire scar: collision disabled always; no trigger, damage, aura, objective, route, decal gameplay, or hazard collision.
- Threshold and half-buried cluster kits: collision disabled by default; optional simple hulls only around large stone masses if separately approved; no gate volume, route validator, nav blocker, trigger volume, or objective frame.
- Review rows, scale rows, material rows, and closure docs: collision disabled always and no Unreal actor, validator, capture, startup placement, or marker validation is approved.

## Animation Notes

Baseline policy is static.

Allowed planning language:

- Static low cairns, standing stones, old cloth, ash/mud bases, fire scars, threshold variants, half-buried clusters, review rows, scale rows, and material rows.
- Static material variation for stone value, soot, ash, red cloth wear, lichen, mud, cave grit, and roughness if a later material task defines it.

Not part of this package:

- Skeletal animation, physics collapse, destructible states, movable stones, puzzle movement, cloth simulation, vertex wind, rope physics, material pulse, ritual activation, active fire, smoke, particles, VFX/audio, gameplay state change, quest/objective state, waypoint behavior, route blocker behavior, aura behavior, damage behavior, interaction behavior, patrol/spawn behavior, runtime animation, startup placement, final approval, source concept movement, or Hermes work.

Any future moving, glowing, interactive, damaging, aura-emitting, quest-readable, waypoint-readable, route-affecting, or gameplay-active variant must be split into its own scoped package.

## Unreal Import Notes

This section is planning policy only. No Unreal Content asset, import script, material instance, texture asset, socket, collision proxy, Blueprint, validator, runtime source, review actor, startup actor, placement file, DCC source, FBX export, route blocker setup, trigger setup, gameplay volume setup, nav/pathing setup, or implementation file is created or authorized.

Potential future identity after a separately scoped production lane:

- Asset family: Blood Axe cave remnant static modules and docs-only review rows.
- Candidate folder family: `/Game/Aerathea/Props/Giants/BloodAxeCamp/RitualStones/CaveRemnants/`
- Candidate review folder family: `/Game/Aerathea/Review/Giants/BloodAxe/CaveRemnants/`
- Pivot policy: base center for standalone props; cluster center for kit compositions.
- Orientation policy: primary readable side faces +X unless a later export convention sets another direction.
- Scale policy: centimeter-authored source, imported at scale 1.0, preserving female 442 cm and male 470 cm Giant baselines.
- Collision policy: disabled by default; simple primitive collision only for major static stone masses when a future lane explicitly needs basic contact; review rows always disabled.
- LOD policy: LOD0-LOD3 required for important shipping modules before production import.
- Material slot policy: 1 target for single stone or ground props, 1-2 target for mixed stone/cloth props, 3 maximum for larger mixed kits only under separate approval.

No game-content folder path is selected by this docs-only package.

## Folder and Naming Recommendation

Documentation path:

- `docs/assets/kits/DOC_GIA_BloodAxeCaveRemnantClusterLODAndCollision_A01/PRODUCTION_PACKAGE.md`

Potential future package references after separate approval:

- `SM_GIA_BloodAxeCaveRemnantCairn_A01`
- `SM_GIA_BloodAxeCollapsedCaveRemnantCairn_A01`
- `SM_GIA_BloodAxeLowCaveStandingStone_A01`
- `SM_GIA_BloodAxeBrokenLeaningCaveStone_A01`
- `SM_GIA_BloodAxeOldCaveClothWrap_A01`
- `SM_GIA_BloodAxeDrapedCaveClothScrap_A01`
- `SM_GIA_BloodAxeCaveAshMudBase_A01`
- `SM_GIA_BloodAxeColdCaveFireScar_A01`
- `KIT_GIA_BloodAxeCaveRemnantThreshold_A01`
- `KIT_GIA_BloodAxeCaveBrokenSlabThreshold_A01`
- `KIT_GIA_BloodAxeHalfBuriedCaveStoneCluster_A01`

Do not create source asset folders, DCC files, FBX exports, game content folders, material instances, texture assets, validators, global index edits, backlog edits, task-board edits, startup placement, external source concept copies, runtime files, Hermes files, or unrelated package files from this task.

## Quality Gate Checklist

- Required universal package headings are present in the requested order.
- Package is docs-only and limited to `docs/assets/kits/DOC_GIA_BloodAxeCaveRemnantClusterLODAndCollision_A01/PRODUCTION_PACKAGE.md`.
- Giant scale lock is explicit: female 442 cm / 14 ft 6 in and male 470 cm / 15 ft 5 in.
- Approved Giant ranges are explicit: females 14-15 ft and males 14 ft 10 in-16 ft.
- Blood Axe remains a hostile Giant sub-faction and does not replace neutral/civilized Giant culture.
- LOD0-LOD3 policy protects primary cave-remnant silhouettes before preserving micro-detail.
- Collision policy blocks collision proxies, UCX meshes, nav blockers, gameplay volumes, trigger volumes, objective volumes, validators, collision correctness claims, and runtime implementation.
- Review rows, scale rows, material rows, and closure docs remain non-shipping planning aids.
- No DCC, FBX, Unreal Content, startup placement, runtime source, material instance, texture asset, material graph, VFX/audio, source concept movement, final approval, implementation target, or Hermes work is authorized.
