# DOC_GIA_BloodAxeRitualStoneLODAndCollision_A01 Production Package

## Art Direction Summary

- Asset name: `DOC_GIA_BloodAxeRitualStoneLODAndCollision_A01`
- Asset type: Docs-only LOD and collision policy package
- Parent planning source: `KIT_GIA_BloodAxeRitualStones_A01`
- Related child packages: `SM_GIA_BloodAxeStandingStone_A01`, `SM_GIA_BloodAxeAltarStone_A01`, `KIT_GIA_BloodAxeCairnGuideposts_A01`, `SM_GIA_BloodAxeRitualChannelStone_A01`, and `KIT_GIA_BloodAxeRitualBannerPoles_A01`
- Scale dependency: validated `SK_GIA_Base_A01` Giant scale lock
- Faction/theme: Blood Axe Tribe as a hostile Giant sub-faction
- Scope: policy only; no asset implementation

`DOC_GIA_BloodAxeRitualStoneLODAndCollision_A01` defines shared LOD and collision policy for future Blood Axe ritual-stone planning rows: standing-stone rings, altar stones, cairn guideposts, channel stones, banner poles, cave approach markers, and review rows. It exists to keep future packages consistent, readable, and safe for MMO-scale production without creating any mesh, texture, material, collision, validator, Unreal, DCC, or runtime work.

Blood Axe ritual-stone dressing must remain the visual language of a hostile Giant sub-faction. It must not become neutral/civilized Giant culture. Use rough highland stone, soot, ash, trampled mud, scorched timber, rawhide, rope, oxide red cloth, blackened iron, sparse horn, and dull bone. Exclude refined cave-town masonry, blue-gray civic stonework, terrace or waterwork motifs, warm hearth settlement identity, peaceful highland guide language, and restrained blue rune culture as default reads.

This document defines policy only. It does not create collision proxies, nav blockers, gameplay volumes, validators, DCC files, FBX exports, Unreal Content, runtime source, implementation files, source asset folders, startup placement, review actors, material instances, textures, sockets, animation assets, or engine settings.

## Gameplay Purpose

The gameplay purpose is production guardrail planning only. These policies help later docs keep static ritual-stone dressing readable and performant without implying mechanics.

Allowed planning uses:

- Define LOD0-LOD3 expectations for future static ritual-stone modules.
- Define disabled-by-default/simple-only collision rules for standing-stone rings, altar stones, cairn guideposts, channel stones, banner poles, cave approach markers, and review rows.
- Preserve the Blood Axe ritual-stone role as non-graphic warning, memory, guidepost, and moved-camp remnant dressing.
- Keep repeated Giant-scale props cheap enough for camp edges, stronghold approaches, abandoned highland sites, and cave thresholds.
- Provide a common policy reference for future package authors before any separate DCC or Unreal lane begins.

Out of scope:

- Collision proxy creation, nav blockers, gameplay volumes, trigger volumes, objective volumes, damage volumes, aura volumes, interaction volumes, waypoint logic, quest markers, readable rune text, ritual gameplay, offering mechanics, liquid flow, VFX/audio, material graph behavior, encounter logic, AI behavior, pathfinding rules, traversal proof, pickup/loot/resource/crafting/economy behavior, destructible behavior, runtime source, validators, DCC, FBX, Unreal Content, startup placement, source concept movement, or implementation target selection.

## Silhouette Notes

LOD policy must protect the primary silhouette before preserving decoration. Every future module should keep its Giant-scale read at MMO camera distance:

- Standing-stone rings: uneven monolith arcs, taller anchor stones, secondary stones, broken gaps, fallen stones, and open centers.
- Altar stones: massive low slabs, uneven support stones, broad chipped edges, soot-dark tops, and grounded heavy footprints.
- Cairn guideposts: a few large stacked stones, paired route-edge rhythm, cloth-tied guidepost forms, ash-stained bases, and moved-camp collapse shapes.
- Channel stones: low heavy slabs, broad dry trough lines, broken module seams, ash-packed bases, and inactive eroded channel silhouettes.
- Banner poles: tall rough verticals, split tops, broad static red cloth shapes, heavy rope lashings, stone weights, and sparse horn punctuation.
- Cave approach markers: paired rough standing stones, threshold cairns, low stone rows, red cloth accents, and one or two dominant marker forms near cave approaches.
- Review rows: clean non-shipping rows for scale, LOD comparison, collision policy comparison, and camera-distance readability.

Model real geometry in future packages only for large forms that carry the silhouette: major stones, slabs, dry trough lips, cairn stack masses, banner poles, broad cloth sheets, major lashings, stone weights, and large horn or iron accents. Keep tiny chips, soot speckles, ash flecks, cloth weave, rope fibers, scratches, small cracks, paint wear, lichen, mud streaks, small horn cuts, and minor metal nicks in texture, normal, AO, or mask detail.

Never let LOD reduction turn Blood Axe warning forms into UI arrows, quest markers, readable text, polished monuments, refined civic Giant masonry, or neutral/civilized Giant culture.

## Scale Notes

Use the validated `SK_GIA_Base_A01` Giant scale lock in every future package:

- Female Giant baseline: 442 cm / 14'6".
- Male Giant baseline: 470 cm / 15'5".
- Approved Giant range remains females 14-15 ft / 427-457 cm and males 14'10"-16'0" / 452-488 cm.
- Author future source in centimeters. 1 Unreal unit = 1 cm.

LOD and collision policy must not change Giant race scale, character capsule expectations, skeleton policy, prop scale, or review-row scale markers. Future review rows should show female 442 cm and male 470 cm baselines beside representative standing-stone rings, altar stones, cairn guideposts, channel stones, banner poles, and cave approach markers.

Scale guidance for future LOD/collision decisions:

- Keep standing-stone ring diameter, anchor height, altar footprint, cairn height, channel slab length, banner pole height, and cave approach rhythm readable before preserving small surface cuts.
- Do not use collision to define path widths, gate logic, arena boundaries, ritual boundaries, traversal proofs, encounter spaces, objective radii, damage radii, aura radii, interaction ranges, or waypoint ranges.
- Treat review rows as non-shipping planning aids with collision disabled.

## Materials and Color Palette

LOD and collision policy must support the shared Blood Axe material read:

- Rough highland stone, dark granite, fractured slate, ash-stained cairn stone, soot-blackened boulders, and chipped pale edges.
- Packed earth, trampled mud, cold ash, charcoal dust, burned grass, cave-mouth grit, and old camp residue.
- Scorched timber poles, rawhide lashings, rope, sinew ties, dirty leather wraps, fixed oxide red cloth, faded maroon strips, and chipped red paint.
- Blackened iron clamps, crude collars, rough scrap hooks, dull shield-rim fragments, sparse old horn, and aged bone used as low-density accents.

Palette policy:

- Dominant values: charcoal gray, dark stone gray, mud brown, cold ash gray, soot black, and muted weathered stone.
- Blood Axe accents: oxide red, faded maroon, chipped red pigment, and dirty red cloth in controlled beats.
- Secondary accents: rawhide tan, rope brown, dull iron gray, horn tan, aged bone ivory, and muted lichen green.
- Emissive: absent by default. Any glowing material, signal light, rune glow, aura read, animated material state, torch/VFX state, or gameplay-readable highlight belongs in a separately scoped material or VFX task.

Collision policy must ignore material micro-detail. Cloth weave, rope fibers, soot, ash, pitting, red paint wear, horn rings, lichen, mud streaks, small chips, and cracks should never create collision detail.

## Concept Image Prompt

Create an original stylized fantasy MMORPG production policy sheet of `DOC_GIA_BloodAxeRitualStoneLODAndCollision_A01` for the world of Aerathea. The design should emphasize LOD0-LOD3 reduction policy, disabled-by-default/simple-only collision policy, standing-stone rings, altar stones, cairn guideposts, channel stones, banner poles, cave approach markers, review rows, Giant-scale readability, rough highland stone, soot, ash, trampled mud, scorched timber, rope, rawhide, oxide red cloth, blackened iron, sparse horn and dull bone accents, hostile Giant sub-faction identity, strict separation from neutral/civilized Giant culture, and the role of static non-graphic warning, memory, guidepost, and moved-camp remnant dressing. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, no default emissive glow, and MMO-friendly mid-poly production design. Present it as a docs-only policy board with LOD comparison rows, collision policy callouts, material swatches, and scale markers beside female 442 cm and male 470 cm Giant baselines on a clean background. Avoid copying any existing franchise, avoid readable rune text, avoid ritual gameplay, avoid VFX/audio, avoid objective or quest marker language, avoid navigation/pathfinding diagrams, avoid collision proxy diagrams that imply implementation, avoid neutral Giant cave-town architecture, avoid graphic gore, and avoid excessive micro-detail that would not translate to mid-poly Unreal assets.

## Modeling Notes

This is not a modeling task. It creates no DCC source, mesh, sculpt, retopo, UVs, bakes, proof renders, LOD source files, collision proxies, FBX exports, Unreal assets, material instances, textures, validators, runtime source, review actors, startup placement, or implementation files.

Future modeling packages should follow these policy rules:

- Build large silhouette carriers as geometry: standing stones, altar slabs, cairn masses, dry channel trough lips, banner poles, broad cloth strips, major lashings, stone weights, cave threshold stones, and large horn or iron accents.
- Keep all small surface language in texture or normal detail: tiny cracks, fine chips, soot speckles, ash flecks, cloth weave, rope fibers, scratches, lichen, mud streaks, paint chips, wood grain, horn rings, and minor iron pitting.
- Use modular variants only when they reduce repetition: anchor stones, secondary stones, broken stones, slab altars, support stones, cairn singles, paired cairns, channel ends, banner pole heights, stone weights, and cave threshold clusters.
- Keep review rows visibly non-shipping through simple row organization and utility presentation, not through in-world prop finish.
- Do not model dense pebble carpets, skull piles, graphic remains, readable text, UI-like symbols, fine glyph panels, many nails, complex rope nets, cloth simulation-ready strips, or high-frequency damage.

LOD modeling policy:

- Future LOD0 meshes carry all large forms and major silhouette cuts.
- Future LOD1 meshes reduce small geometry while keeping the asset identity readable.
- Future LOD2 meshes simplify to broad planes, masses, and color beats.
- Future LOD3 meshes preserve only the primary Giant-scale silhouette and strongest Blood Axe material accents.

## Texture and Material Notes

This package creates no texture, material instance, material graph, mask, atlas, or engine content. It defines texture and material policy only.

Future packages should use standard Aerathea texture outputs:

- Base Color / Albedo (`BC`)
- Normal (`N`)
- Packed Occlusion/Roughness/Metallic (`ORM`)
- Emissive (`E`) only for a separately scoped glowing variant; baseline ritual-stone LOD/collision policy assumes no emissive

Texture detail should carry detail removed through LODs:

- LOD0 can use normal and AO detail for cracks, chips, soot, ash, lichen, cloth weave, rope fibers, wood grain, and pitting.
- LOD1 should keep broad material value changes and reduce reliance on tiny normal detail.
- LOD2 should preserve stone/ash/red-cloth reads through large color blocks and baked AO.
- LOD3 should keep only broad dark stone mass, soot/ash value, and one or two Blood Axe red or horn/iron accent reads where needed.

Material slot policy:

- Single stones, altar slabs, cairns, and channel stones: 1 material target, 2 maximum only if accent separation is necessary.
- Banner poles and mixed cave approach markers: 1-2 material target, 3 maximum only for large clustered modules needing wood/rope/cloth, stone, and horn/iron separation.
- Review rows: 1 simple utility material if a later task creates non-shipping review geometry.
- Do not create unique material slots for individual cracks, cloth strips, ash patches, rope wraps, stones, chips, stains, horn tips, or iron scraps.

## Triangle Budget

This package creates no mesh. Triangle values below are future policy targets for separately scoped packages.

Future LOD0 budget bands:

- Single standing stone: 3k-7k tris, 1 material target.
- Standing-stone ring section: 8k-24k tris per reusable arc or partial set, 1-2 materials.
- Full standing-stone review ring: 20k-60k tris total through instanced modules; review-only until separately scoped.
- Altar stone: 3k-7k tris, 1 material target, 2 maximum.
- Single cairn guidepost: 1k-4k tris, 1 material.
- Paired or moved-camp cairn set: 2k-8k tris, 1-2 materials.
- Ritual channel stone: 3k-7k tris, 1 material target, 2 maximum.
- Dry channel stone set: 8k-24k tris total, 1-2 materials.
- Tall ritual banner pole: 1.5k-4k tris, 1-2 materials.
- Banner pole cluster: 6k-14k tris, 2 material target, 3 maximum.
- Cave approach marker cluster: 8k-28k tris, 1-3 materials.
- Review rows: 500-3k tris per non-shipping row set only if a later task creates review geometry.

LOD percentage policy:

- LOD1: 55-70 percent of LOD0, depending on asset family and silhouette complexity.
- LOD2: 30-45 percent of LOD0.
- LOD3: 10-25 percent of LOD0.

Spend triangles on primary silhouette and contact readability. Do not spend triangles on tiny cracks, ash flecks, cloth fibers, rope fibers, dense nails, repeated horn chips, fine scratches, soot dust, paint chips, or hidden underside detail.

## LOD Plan

All important future static modules need LOD0, LOD1, LOD2, and LOD3 before any production import lane uses them.

Global LOD policy:

- LOD0: full primary forms, major silhouette cuts, large contact bases, broad cloth shapes, dry channel lips, stone stack rhythms, major lashings, stone weights, sparse horn/iron silhouettes, and authored material detail.
- LOD1: reduce secondary bevels, small chips, cloth edge cuts, rope subdivisions, minor knots, small horn cuts, base undercuts, backside detail, and hidden underside forms.
- LOD2: merge smaller forms, simplify stones into large planes, flatten shallow groove detail, simplify cloth to broad strips, remove non-silhouette accents, and preserve only the strongest red/stone/ash reads.
- LOD3: preserve primary asset identity only: ring rhythm, tall stone anchors, altar slab mass, cairn guidepost height, channel slab footprint and one trough line, banner pole height and red cloth block, cave threshold rhythm, or review-row layout.

Reduction order for all ritual-stone families:

1. Remove texture-only detail from geometry assumptions first: tiny cracks, small chips, soot speckles, ash flecks, cloth weave, rope fibers, lichen specks, paint chips, minor scratches, wood grain, and iron pitting.
2. Remove small accent geometry: small lashings, minor knots, small cloth holes, tiny horn chips, little stone wedges, small metal nicks, and tiny rubble.
3. Remove hidden or low-value geometry: back-facing cairn stones, underside slab bevels, hidden pole base cuts, interior ring clutter, and non-visible ash/mud undercuts.
4. Remove secondary decorations: minor blackened iron clamps, small cloth knots, blade fragments, small horn tokens, duplicate foot stones, and non-silhouette scraps.
5. Simplify secondary form detail: shallow groove subdivisions, stone bevel density, cloth fold geometry, pole split-top interior cuts, and non-primary broken edges.
6. Only after small detail is gone, simplify primary silhouettes while preserving Giant-scale read and Blood Axe material identity.

Family-specific LOD requirements:

- Standing-stone rings: preserve ring rhythm, tall anchor stones, broken gaps, and one or two red/ash beats through LOD3. Remove tiny chips, secondary stones, backside clutter, and ring interior debris first.
- Altar stones: preserve low slab mass, support-stone read, broad footprint, and soot-dark top value through LOD3. Remove underside detail, small clamps, minor chips, and optional accents first.
- Cairn guideposts: preserve a few large stacked stones, paired rhythm, cloth guidepost read, and moved-camp collapse shape through LOD3. Merge small stones and remove minor ties before reducing the main cairn mass.
- Channel stones: preserve low slab footprint, one dominant dry trough read, and broken end mass through LOD3. Remove secondary trough cuts, iron wedges, small notches, and hidden underside detail first.
- Banner poles: preserve tall pole rhythm, broad fixed red cloth block, stone-weight mass, and sparse horn punctuation through LOD3. Remove tiny fray, rope wrap segments, minor knots, and small hardware first.
- Cave approach markers: preserve threshold rhythm, dominant paired stones or cairns, and red cloth warning beats through LOD3. Remove small side stones, minor ash bases, and secondary decorations first.
- Review rows: preserve row label intent through layout only if future non-shipping geometry exists. Collision remains disabled, and LODs may be simplified aggressively because review rows are planning aids.

Never reduce the Giant-scale relationship, Blood Axe red/black warning identity, static remnant read, or primary stone/pole silhouettes before removing small detail.

## Collision Notes

This package creates no collision. It defines disabled-by-default/simple-only collision policy for future static modules. Do not create collision proxies, UCX meshes, Unreal collision settings, physics bodies, nav blockers, pathfinding helpers, smart links, gameplay volumes, trigger volumes, damage volumes, aura volumes, objective volumes, interaction volumes, validator scripts, or runtime setup from this package.

Global collision policy:

- Default to collision disabled for visual dressing, review rows, cloth, rope, horn tokens, small bone accents, soot, ash, mud, minor chips, small stones, paint, lichen, decals, and non-contact details.
- Use simple primitive collision only when a later implementation lane needs basic player or camera blocking on a large static body.
- Prefer simple boxes, capsules, or low-count convex hulls around major masses only.
- Do not use complex-as-simple collision for repeated ritual-stone dressing.
- Do not use collision to prove navigation/pathfinding, traversal widths, route gates, encounter lanes, objectives, ritual boundaries, damage fields, aura fields, interaction affordances, cover, destructibility, loot pickup, resource gathering, or quest logic.

Family-specific collision policy:

- Standing-stone rings: collision disabled by default for review rows and composed ring planning. If a future static mesh needs contact, use simple hulls per major standing stone only. Do not add a ring boundary, arena wall, nav blocker, ritual volume, trigger volume, or objective area.
- Altar stones: collision disabled by default for distant dressing. If contact is needed, use one simple box or low-count convex hull around the main slab, with optional simple support-stone hulls only for major contact masses. Do not define walkable surface behavior, offering slots, interaction collision, damage fields, aura fields, or cover behavior.
- Cairn guideposts: collision disabled by default. If required, use one simple primitive around the largest cairn mass or guidepost shaft. Paired cairns must not become a path gate, route validator, nav blocker, waypoint pair, or quest frame.
- Channel stones: collision disabled by default. If promoted to contact dressing, use one simple hull for the slab footprint and optionally a second hull for a high broken end. Do not collide trough interiors, liquid paths, damage paths, VFX paths, channel lines, ash deposits, or iron wedges.
- Banner poles: collision disabled by default for review rows, cloth, rope, horn markers, and small hardware. If contact is needed, use one slim capsule or box for the pole and one simple hull for a stone weight. Do not add cloth collision, rope physics, per-strip collision, aura volumes, trigger volumes, faction buff volumes, or interaction volumes.
- Cave approach markers: collision disabled by default for low dressing. If needed, use simple hulls only around major paired stones, dominant cairns, or heavy marker bases. Do not define cave traversal, path widths, pathfinding, nav blockers, smart links, encounter triggers, quest markers, or route validation.
- Review rows: collision disabled always. Review rows are non-shipping planning aids and must not receive collision proxies, nav blockers, validators, startup placement, or gameplay volumes.

Small accents with collision always disabled:

- Cloth strips, rope lashings, small knots, horn chips, dull bone tokens, tiny iron scraps, ash piles, soot marks, mud streaks, lichen, paint chips, small cracks, minor bevels, small stones, scratches, and texture-only detail.

## Animation Notes

Baseline policy is static.

Allowed planning language:

- Static standing-stone rings, altar stones, cairn guideposts, channel stones, banner poles, cave approach markers, and review rows.
- Static material variation for stone value, soot, ash, cloth age, red paint wear, lichen, mud, and roughness if a later material task defines it.
- Fixed cloth and rope silhouettes modeled as static geometry only in future packages.

Not part of this package:

- Skeletal animation, cloth simulation, vertex wind, rope physics, banner waving, dangling motion, destructible states, collapse states, material pulse, ritual activation, liquid movement, VFX/audio, gameplay state change, quest/objective state, waypoint behavior, aura behavior, damage behavior, interaction behavior, patrol/spawn behavior, or runtime animation.

Any future moving, glowing, interactive, damaging, aura-emitting, quest-readable, waypoint-readable, or gameplay-active variant must be split into its own scoped package.

## Unreal Import Notes

This section is planning policy only. No Unreal Content asset, import script, material instance, texture asset, socket, collision proxy, Blueprint, validator, runtime source, review actor, startup actor, placement file, DCC source, FBX export, or implementation file is created or authorized.

Potential future identity after a separately scoped implementation lane:

- Asset family: Blood Axe ritual-stone static mesh modules and docs-only review rows.
- Candidate folder family: `/Game/Aerathea/Props/Giants/BloodAxeCamp/RitualStones/`
- Candidate review folder family: `/Game/Aerathea/Review/Giants/BloodAxe/RitualStones/`
- Pivot policy: base center for standalone stones, altars, cairns, poles, and cave markers; ring center for ring compositions; row center for review rows.
- Orientation policy: primary readable side faces +X unless a later export convention sets another direction.
- Scale policy: centimeter-authored source, imported at scale 1.0, preserving female 442 cm and male 470 cm Giant baselines.
- Collision policy: disabled by default; simple primitive collision only for major static masses when a future lane needs basic contact; review rows always disabled.
- LOD policy: LOD0-LOD3 required for important shipping modules before production import.
- Material slot policy: 1 target for stone-only modules, 2 target for mixed cloth/stone assets, 3 maximum for large pole or cave approach clusters.
- Texture policy: BC, N, ORM by default; no baseline emissive.
- Sockets: none by default.
- Animation list: none by default.
- Blueprint behavior: none.

Candidate future names for planning reference only:

- `DOC_GIA_BloodAxeRitualStoneLODAndCollision_A01`
- `KIT_GIA_BloodAxeStandingStoneRing_A01`
- `SM_GIA_BloodAxeStandingStone_A01`
- `SM_GIA_BloodAxeAltarStone_A01`
- `KIT_GIA_BloodAxeCairnGuideposts_A01`
- `SM_GIA_BloodAxeRitualChannelStone_A01`
- `KIT_GIA_BloodAxeRitualBannerPoles_A01`
- `KIT_GIA_BloodAxeCaveApproachMarkers_A01`
- `DOC_GIA_BloodAxeRitualStoneReviewRows_A01`

Do not create or edit `Content/Aerathea`, `SourceAssets`, `Tools/DCC`, `Tools/Unreal`, runtime source, external concept folders, global indexes, task boards, backlog docs, bootstrap docs, unrelated package files, validators, startup placement files, or any file outside this package path from this task.

## Folder and Naming Recommendation

Docs path:

- `docs/assets/kits/DOC_GIA_BloodAxeRitualStoneLODAndCollision_A01/PRODUCTION_PACKAGE.md`

Package naming:

- `DOC_GIA_BloodAxeRitualStoneLODAndCollision_A01` for this docs-only policy package.
- `DOC_GIA_BloodAxeRitualStone<Purpose>_A01` for future docs-only scale, review, material, or policy rows.
- `KIT_GIA_BloodAxe<ModuleFamily>_A01` for future kit-level static module packages.
- `SM_GIA_BloodAxe<ModuleName>_A01` for future static mesh module packages.
- `T_GIA_BloodAxe<AssetName>_BC`, `T_GIA_BloodAxe<AssetName>_N`, and `T_GIA_BloodAxe<AssetName>_ORM` for future texture naming if a separate task creates textures.
- `MI_GIA_BloodAxe<MaterialPurpose>_A01` for future material instances if a separate task creates materials.

No source, export, Unreal, runtime, DCC, validator, collision proxy, nav blocker, gameplay volume, startup placement, external concept, index, backlog, task-board, or unrelated package path is created by this package.

## Quality Gate Checklist

- Package uses exactly the requested top-level headings in order.
- Package is docs-only and defines policy only.
- File path is limited to `docs/assets/kits/DOC_GIA_BloodAxeRitualStoneLODAndCollision_A01/PRODUCTION_PACKAGE.md`.
- Giant scale lock is explicit from `SK_GIA_Base_A01`: female 442 cm / 14'6" baseline and male 470 cm / 15'5" baseline.
- Blood Axe remains a hostile Giant sub-faction and stays separate from neutral/civilized Giant culture.
- Policy covers standing-stone rings, altar stones, cairn guideposts, channel stones, banner poles, cave approach markers, and review rows.
- LOD0, LOD1, LOD2, and LOD3 policy is present with a reduction order that removes micro-detail before primary silhouettes.
- Collision policy is disabled by default and simple-only when needed for future large static masses.
- Review rows have collision disabled and remain non-shipping planning aids.
- No collision proxy creation, nav blockers, gameplay volumes, validators, DCC, FBX, Unreal Content, runtime source, implementation files, source asset folders, material instances, textures, sockets, animation assets, or startup placement are created or authorized.
- No ritual gameplay, offering mechanics, activation states, liquid flow, VFX/audio, damage/aura behavior, objective logic, quest/UI markers, waypoint logic, navigation/pathfinding, traversal proof, encounter behavior, AI behavior, interaction behavior, pickup/loot behavior, resource/crafting/economy behavior, destructible behavior, or readable rune text is defined.
- Materials stay on rough highland stone, soot, ash, trampled mud, scorched timber, rawhide, rope, oxide red cloth, blackened iron, sparse old horn, and dull bone.
- Default emissive, ritual glow, shamanic glow, signal glow, animated material states, UI-like markers, refined civic Giant stonework, blue-rune culture, warm hearth settlement language, and neutral/civilized Giant material defaults are absent.
- Triangle budgets, material slot policy, texture map policy, LOD plan, collision policy, animation limits, Unreal import policy, and folder naming are included without performing implementation work.
