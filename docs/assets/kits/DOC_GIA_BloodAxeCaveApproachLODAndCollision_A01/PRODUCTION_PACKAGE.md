# DOC_GIA_BloodAxeCaveApproachLODAndCollision_A01 Production Package

## Art Direction Summary

- Asset name: `DOC_GIA_BloodAxeCaveApproachLODAndCollision_A01`
- Asset type: Docs-only LOD and collision policy package
- Task: `AET-MA-20260629-228`
- Parent kit: `KIT_GIA_BloodAxeCaveApproachMarkers_A01`
- Parent intake row: `BloodAxeCaveApproachMarkers_A01#LODCollisionPlanning_A01`
- Reference packages: `DOC_GIA_BloodAxeCaveApproachMaterialDiscipline_A01` and `DOC_GIA_BloodAxeRitualStoneLODAndCollision_A01`
- Scale dependency: validated `SK_GIA_Base_A01` Giant scale lock
- Faction/theme: Blood Axe Tribe, hostile Giant sub-faction only
- Scope: policy only; no asset implementation

`DOC_GIA_BloodAxeCaveApproachLODAndCollision_A01` defines shared LOD and collision policy for future Blood Axe cave approach marker planning: low cairns, paired standing stones, broken slab remnants, cloth or paint threshold markers, ash bases, and review rows. It exists to keep later static cave approach packages readable, cheap, and consistent before any separate production lane begins.

Blood Axe cave approach dressing must remain the language of a hostile Giant sub-faction. It may use rough highland stone, soot, cold ash, cave grit, trampled mud, oxide red cloth, rawhide, rope, blackened iron, sparse old horn, and dull bone. It must not become neutral/civilized Giant culture. Neutral/civilized Giant culture remains tied to skilled stonework, hidden highland cave towns, blue-gray civic masonry, terraces, waterworks, warm hearth identity, and restrained civic rune language.

This document defines policy only. It does not create collision proxies, UCX meshes, nav blockers, gameplay volumes, trigger volumes, objective volumes, validators, DCC files, FBX exports, Unreal Content, runtime source, source asset folders, startup placement, review actors, material instances, textures, sockets, animation assets, or engine settings.

## Gameplay Purpose

The gameplay purpose is production guardrail planning only. These policies help future docs keep static cave approach dressing readable and performant without implying cave mechanics, route behavior, encounter logic, or objective behavior.

Allowed planning uses:

- Define LOD0-LOD3 expectations for future static cave approach marker modules.
- Define disabled-by-default and simple-only collision rules for low cairns, standing pairs, slab remnants, cloth or paint markers, ash bases, and review rows.
- Preserve the role of cave approach markers as static threshold readability only.
- Keep repeated Giant-scale dressing cheap enough for cave mouths, cliff openings, abandoned shelter edges, and hostile Blood Axe territory thresholds.
- Provide a common policy reference for future package authors before any separate DCC or Unreal lane begins.
- Protect neutral/civilized Giant culture from Blood Axe raider visual drift.

Out of scope:

- Collision proxy work, UCX work, nav blocker work, gameplay volume work, trigger volume work, objective volume work, validator work, DCC work, FBX work, Unreal Content work, runtime implementation, cave gameplay, traversal proof, path widths as gameplay values, route validation, quest/UI markers, encounter triggers, spawn logic, patrol logic, damage/aura behavior, objective logic, interaction behavior, readable signage, VFX/audio, material graph behavior, startup placement, final visual approval, final cave approval, or implementation target selection.

## Silhouette Notes

LOD policy must protect the primary cave approach read before preserving decoration. Every future module should keep its Giant-scale silhouette at MMO camera distance:

- Low cave approach cairns: squat stacks made from a few large stones, broad ash-stained bases, optional heavy cloth ties, and irregular collapsed edges.
- Paired standing stones: asymmetric tall and short rough stones that frame a visual threshold without becoming a doorway, gate, objective frame, or route device.
- Broken slab remnants: low heavy slab pieces, snapped stone edges, old threshold fragments, and broad contact shadows near cave-edge ground.
- Cloth and paint threshold markers: broad oxide red cloth strips, static knots, draped bands, chipped red paint swaths, and faded warning beats.
- Ash bases: low cold ash, soot, cave grit, and trampled mud pads that ground marker clusters without becoming gameplay zones.
- Review rows: clean non-shipping rows for scale, LOD comparison, material restraint, and collision policy comparison.

Future asset packages should model real geometry only for the forms that carry silhouette: major stones, slab thickness, broad chipped planes, large cloth strips, oversized knots, heavy rope wraps, major ash or mud base shapes, and a few large horn, bone, or iron accents. Tiny cracks, soot speckles, ash flecks, cloth weave, rope fibers, fray, small paint chips, mud droplets, lichen specks, scratches, and minor pitting belong in future texture, normal, AO, roughness, or mask planning.

Never let LOD reduction turn cave approach markers into UI arrows, quest markers, readable text, polished monuments, refined civic Giant masonry, or neutral/civilized Giant culture.

## Scale Notes

Use the validated `SK_GIA_Base_A01` Giant scale lock in every future package:

- Female Giant baseline: 442 cm / 14'6".
- Male Giant baseline: 470 cm / 15'5".
- Approved Giant range remains females 14-15 ft / 427-457 cm and males 14'10"-16'0" / 452-488 cm.
- Future source, if separately approved, should be authored in centimeters with 1 Unreal unit = 1 cm.

Scale guidance for future policy consumers:

- Low cave approach cairns should remain readable as Giant-built threshold dressing: roughly 80-180 cm tall and 140-360 cm across when future packages need planning dimensions.
- Paired low cairns may sit roughly 250-700 cm apart as visual threshold beats only, not route gates.
- Paired standing stones should read as rough Giant-scale markers: roughly 220-520 cm tall, 120-260 cm wide, and 80-220 cm deep if later packages need planning dimensions.
- Broken slab remnants and mixed cave remnant clusters may cover roughly 300-1100 cm footprints, with one to three major stone reads.
- Cloth markers should use broad strips, roughly 80-240 cm long and 20-70 cm wide, sized for Giant hands and MMO camera readability.
- Review rows should place female 442 cm and male 470 cm Giant baselines beside representative cairns, standing pairs, slab remnants, cloth markers, and ash bases.

These are visual production planning values only. They are not collision proof, pathing data, traversal clearance, encounter spacing, objective ranges, interaction ranges, camera approval, or implementation guidance.

## Materials and Color Palette

LOD and collision policy must support the cave approach material discipline:

- Rough highland stone, dark granite, fractured slate, ash-stained field rock, soot-blackened cave-edge slabs, and chipped pale edges.
- Packed earth, trampled mud, cold ash, charcoal dust, cave grit, dry mineral residue, and old camp remains.
- Oxide red cloth, faded maroon strips, dirty red wraps, static knots, broad draped bands, and chipped dirty red paint.
- Rope, rawhide lashings, sinew ties, worn leather strips, blackened iron clamps, old horn, and dull bone used as sparse secondary warning accents.

Palette policy:

- Dominant values: charcoal gray, dark stone gray, cold ash gray, cave black, mud brown, and muted weathered stone.
- Blood Axe accents: oxide red, faded maroon, dirty red cloth, and chipped red pigment in controlled beats.
- Secondary accents: rawhide tan, rope brown, dull iron gray, old horn tan, dull bone ivory, and muted lichen green.
- Emissive: absent by default. Glow, signal light, rune glow, ritual light, shamanic pulse, torch state, UI highlight, or animated material state belongs in a separately scoped package.

Collision policy must ignore material micro-detail. Cloth weave, rope fibers, soot, ash, cave grit, pitting, red paint wear, lichen, mud streaks, small chips, cracks, horn rings, and bone pores should never drive collision detail.

## Concept Image Prompt

Create an original stylized fantasy MMORPG production policy sheet of `DOC_GIA_BloodAxeCaveApproachLODAndCollision_A01` for the world of Aerathea. The design should emphasize LOD0-LOD3 reduction policy, disabled-by-default and simple-only collision policy, low cave approach cairns, paired standing stones, broken slab remnants, cloth and paint threshold markers, ash bases, review rows, Giant-scale readability, rough highland stone, soot, cold ash, cave grit, trampled mud, oxide red cloth, rope, rawhide, blackened iron, sparse old horn and dull bone accents, hostile Giant sub-faction identity, strict separation from neutral/civilized Giant culture, and the role of static threshold readability only. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, no default emissive glow, and MMO-friendly mid-poly production design. Present it as a docs-only policy board with LOD comparison rows, collision policy callouts, material swatches, and scale markers beside female 442 cm and male 470 cm Giant baselines on a clean background. Avoid copying any existing franchise, avoid cave gameplay, avoid route signs, avoid objective or quest marker language, avoid navigation/pathfinding diagrams, avoid collision proxy diagrams that imply implementation, avoid neutral Giant cave-town architecture, avoid readable text, avoid magic glow, avoid graphic gore, and avoid excessive micro-detail that would not translate to mid-poly Unreal assets.

## Modeling Notes

This is not a modeling task. It creates no DCC source, mesh, sculpt, retopo, UVs, bakes, proof renders, LOD source files, collision proxies, UCX meshes, FBX exports, Unreal assets, material instances, textures, validators, runtime source, review actors, startup placement, or implementation files.

Future modeling packages should follow these policy rules:

- Build large silhouette carriers as geometry: main cairn stones, standing-stone bodies, slab thickness, broken slab planes, broad cloth strips, oversized knots, heavy rope wraps, major ash or mud base forms, and large horn, bone, or iron accents.
- Keep small surface language in texture or normal detail: tiny cracks, fine chips, soot speckles, ash flecks, cave grit particles, cloth weave, rope fibers, scratches, lichen, mud streaks, paint chips, horn rings, bone pores, and minor iron pitting.
- Use modular variants only when they reduce repetition: single low cairns, paired low cairns, collapsed cairns, tall and short standing-stone pairs, leaning pairs, broken pairs, slab remnant clusters, cloth-tied stones, paint-only stones, and ash bases.
- Keep review rows visibly non-shipping through simple row organization and utility presentation, not through in-world prop finish.
- Do not model dense pebble carpets, skull piles, graphic remains, readable text, UI-like symbols, fine glyph panels, many nails, complex rope nets, cloth simulation strips, or high-frequency damage.

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
- Emissive (`E`) only for a separately scoped glowing variant; baseline cave approach LOD/collision policy assumes no emissive

Texture detail should carry detail removed through LODs:

- LOD0 can use normal and AO detail for cracks, chips, soot, ash, lichen, cloth weave, rope fibers, pitting, and red paint wear.
- LOD1 should keep broad material value changes and reduce reliance on tiny normal detail.
- LOD2 should preserve stone, ash, mud, and red cloth or paint reads through large color blocks and baked AO.
- LOD3 should keep only broad dark stone mass, cold ash value, mud grounding, and one or two Blood Axe red or horn/bone/iron accent reads where needed.

Material slot policy:

- Low cairns, ash bases, paint-only stones, and simple slab remnants: 1 material target.
- Cloth-tied cairns, paired standing stones with wraps, and mixed slab remnant clusters: 1-2 material target.
- Large cave approach compositions: 2 material target, 3 maximum only when stone/soil, cloth/hide/rope, and iron/horn/bone truly need separation in a separately scoped child package.
- Review rows: 1 simple utility material if a later task defines non-shipping review geometry.
- Do not assign unique material slots for individual cracks, cloth strips, ash patches, rope wraps, stones, chips, stains, horn tips, bone tokens, or iron scraps.

## Triangle Budget

This package creates no mesh. Triangle values below are future policy targets for separately scoped packages.

Future LOD0 budget bands:

- Single low cave approach cairn: 800-3.5k tris, 1 material.
- Paired low cave approach cairns: 2k-7k tris total, 1 material target.
- Single cave approach standing stone: 1.5k-5k tris, 1 material target.
- Paired cave approach standing stones: 4k-12k tris total, 1-2 materials.
- Broken slab remnant cluster: 3k-12k tris total, 1 material target, 2 maximum.
- Cave ash base or low soot/mud pad: 300-2k tris, 1 material target.
- Cloth or paint threshold marker: 300-1.5k tris as static accent geometry, usually shared with a marker mesh.
- Mixed cave approach marker composition: 8k-28k tris total through reusable static modules.
- Review rows: 500-3k tris per non-shipping row set only if a later task defines row geometry.

LOD percentage policy:

- LOD1: 55-70 percent of LOD0, depending on asset family and silhouette complexity.
- LOD2: 30-45 percent of LOD0.
- LOD3: 10-25 percent of LOD0.

Spend triangles on primary silhouette and contact readability. Do not spend triangles on tiny cracks, ash flecks, cloth fibers, rope fibers, dense nails, repeated horn chips, fine scratches, soot dust, paint chips, grit specks, or hidden underside detail.

## LOD Plan

All important future static cave approach modules need LOD0, LOD1, LOD2, and LOD3 before any production import lane uses them.

Global LOD policy:

- LOD0: full primary forms, major silhouette cuts, broad contact bases, large stone planes, chunky chipped edges, broad cloth shapes, large knots, major lashings, slab thickness, ash and mud bases, sparse horn/iron silhouettes, and authored material detail.
- LOD1: reduce secondary bevels, small chips, cloth edge cuts, rope subdivisions, minor knots, small horn cuts, base undercuts, backside detail, and hidden underside forms.
- LOD2: merge smaller forms, simplify stones into large planes, flatten cloth folds, remove non-silhouette accents, simplify ash and mud bases, and preserve only the strongest red/stone/ash reads.
- LOD3: preserve primary asset identity only: low threshold cairn mass, paired-stone threshold rhythm, broken slab footprint, broad red cloth or paint beat, ash-base value, or review-row layout.

Reduction order for all cave approach families:

1. Remove texture-only detail from geometry assumptions first: tiny cracks, small chips, soot speckles, ash flecks, cloth weave, rope fibers, lichen specks, paint chips, minor scratches, cave grit particles, mud droplets, horn rings, bone pores, and iron pitting.
2. Remove small accent geometry: small lashings, minor knots, little stone wedges, small cloth holes, tiny horn chips, dull bone tokens, small metal nicks, and tiny rubble.
3. Remove hidden or low-value geometry: back-facing cairn stones, underside slab bevels, hidden standing-stone base cuts, rear-only cloth folds, interior cluster clutter, and non-visible ash/mud undercuts.
4. Remove secondary decorations: minor blackened iron clamps, small cloth knots, duplicate foot stones, extra horn chips, little bone pieces, and non-silhouette scraps.
5. Simplify secondary form detail: shallow groove subdivisions, stone bevel density, cloth fold geometry, slab broken-edge density, and non-primary broken cuts.
6. Only after small detail is gone, simplify primary silhouettes while preserving Giant-scale read, Blood Axe material identity, and static threshold readability.

Family-specific LOD requirements:

- Low cave approach cairns: preserve the few-large-stones stack, squat threshold read, broad ash base, and one optional red cloth or paint beat through LOD3. Merge small stones and remove minor ties before reducing the main cairn mass.
- Paired standing stones: preserve asymmetric tall/short rhythm, paired threshold framing, large stone lean, and broad red warning accent through LOD3. Remove tiny chips, backside cuts, minor lashings, and foot stones first.
- Broken slab remnants: preserve low heavy slab footprint, snapped-stone read, one or two broad broken planes, and cave-edge contact shadow through LOD3. Remove small shard pieces, underside bevels, paint chips, and secondary rubble first.
- Cloth and paint threshold markers: preserve one clear oxide red warning beat through LOD3. Remove tiny fray, cloth holes, rope subdivisions, edge cuts, and paint chips before reducing the broad cloth or paint shape.
- Ash bases: preserve the cold ash/mud grounding value through LOD3 as broad shape or material read. Remove grit particles, ash flecks, tiny pebbles, and edge noise first.
- Review rows: preserve row layout intent only if future non-shipping geometry exists. LODs may be simplified aggressively because review rows are planning aids, and collision remains disabled.

Never reduce the Giant-scale relationship, Blood Axe red/black warning identity, static cave threshold read, or primary cairn/standing-stone/slab silhouettes before removing small detail.

## Collision Notes

This package creates no collision. It defines disabled-by-default and simple-only collision policy for future static cave approach modules. Do not create collision proxies, UCX meshes, Unreal collision settings, physics bodies, nav blockers, pathfinding helpers, smart links, gameplay volumes, trigger volumes, damage volumes, aura volumes, objective volumes, interaction volumes, validator scripts, or runtime setup from this package.

Global collision policy:

- Default to collision disabled for visual dressing, review rows, cloth, rope, horn tokens, small bone accents, soot, ash, mud, cave grit, minor chips, small stones, paint, lichen, decals, and non-contact details.
- Use simple primitive collision only when a later implementation lane needs basic player or camera blocking on a large static body.
- Prefer simple boxes, capsules, or low-count convex hulls around major masses only.
- Do not use complex-as-simple collision for repeated cave approach dressing.
- Do not use collision to prove navigation/pathfinding, traversal widths, route gates, encounter lanes, objectives, cave entry logic, damage fields, aura fields, interaction affordances, cover, destructibility, loot pickup, resource gathering, or quest logic.

Family-specific collision policy:

- Low cave approach cairns: collision disabled by default. If basic contact is required later, use one simple primitive around the largest cairn mass only. Paired cairns must not become a path gate, route validator, nav blocker, waypoint pair, or quest frame.
- Paired standing stones: collision disabled by default for review rows and threshold planning. If later contact is needed, use one simple box or low-count convex hull per major standing stone. Do not add a gate volume, cave traversal proof, route validation, nav blocker, ritual boundary, trigger volume, or objective area.
- Broken slab remnants: collision disabled by default for low dressing. If later contact is needed, use one simple hull around the dominant slab footprint, with optional simple support hulls only for major contact masses. Do not define walkable surface behavior, cover rules, destructible states, interaction collision, damage fields, or objective zones.
- Cloth and paint threshold markers: collision disabled always for cloth, paint, rope, small stakes, knots, loose straps, and surface warning accents. Cloth must not receive cloth collision, physics behavior, interaction collision, or per-strip collision.
- Ash bases: collision disabled always for ash, soot, cave grit, trampled mud, decals, paint, lichen, small pebbles, and contact stains. Ash bases must not become damage zones, aura zones, objective zones, trigger areas, or gameplay fields.
- Review rows: collision disabled always. Review rows are non-shipping planning aids and must not receive collision proxies, UCX meshes, nav blockers, validators, startup placement, or gameplay volumes.

Small accents with collision always disabled:

- Cloth strips, rope lashings, small knots, horn chips, dull bone tokens, tiny iron scraps, ash piles, soot marks, mud streaks, cave grit, lichen, paint chips, small cracks, minor bevels, small stones, scratches, and texture-only detail.

## Animation Notes

Baseline policy is static.

Allowed planning language:

- Static low cave approach cairns, paired standing stones, broken slab remnants, cloth or paint markers, ash bases, and review rows.
- Static material variation for stone value, soot, ash, cloth age, red paint wear, lichen, mud, cave grit, and roughness if a later material task defines it.
- Fixed cloth and rope silhouettes modeled as static geometry only in future packages.

Not part of this package:

- Skeletal animation, cloth simulation, vertex wind, rope physics, dangling motion, destructible states, collapse states, material pulse, ritual activation, VFX/audio, gameplay state change, quest/objective state, waypoint behavior, aura behavior, damage behavior, interaction behavior, patrol/spawn behavior, or runtime animation.

Any future moving, glowing, interactive, damaging, aura-emitting, quest-readable, waypoint-readable, or gameplay-active variant must be split into its own scoped package.

## Unreal Import Notes

This section is planning policy only. No Unreal Content asset, import script, material instance, texture asset, socket, collision proxy, Blueprint, validator, runtime source, review actor, startup actor, placement file, DCC source, FBX export, or implementation file is created or authorized.

Potential future identity after a separately scoped production lane:

- Asset family: Blood Axe cave approach static marker modules and docs-only review rows.
- Candidate folder family: `/Game/Aerathea/Props/Giants/BloodAxeCamp/CaveApproach/`
- Candidate review folder family: `/Game/Aerathea/Review/Giants/BloodAxe/CaveApproach/`
- Pivot policy: base center for standalone cairns, standing stones, slab remnants, cloth markers, and ash bases; cluster center for paired stones, mixed remnants, and review rows.
- Orientation policy: primary readable side faces +X unless a later export convention sets another direction.
- Scale policy: centimeter-authored source, imported at scale 1.0, preserving female 442 cm and male 470 cm Giant baselines.
- Collision policy: disabled by default; simple primitive collision only for major static masses when a future lane needs basic contact; review rows always disabled.
- LOD policy: LOD0-LOD3 required for important shipping modules before production import.
- Material slot policy: 1 target for stone-only modules and ash bases, 2 target for cloth-accent variants, 3 maximum for larger mixed clusters.
- Texture policy: `BC`, `N`, and `ORM` by default; no baseline emissive.
- Sockets: none by default.
- Animation list: none by default.
- Blueprint behavior: none.

Candidate future names for planning reference only:

- `DOC_GIA_BloodAxeCaveApproachLODAndCollision_A01`
- `SM_GIA_BloodAxeLowThresholdCairn_A01`
- `KIT_GIA_BloodAxeLowThresholdCairns_A01`
- `KIT_GIA_BloodAxeCaveApproachStandingPair_A01`
- `KIT_GIA_BloodAxeLeaningCaveStandingPair_A01`
- `KIT_GIA_BloodAxeBrokenCaveStandingPair_A01`
- `KIT_GIA_BloodAxeCaveRemnantCluster_A01`
- `SM_GIA_BloodAxeCaveAshRemnantBase_A01`
- `KIT_GIA_BloodAxeCaveBrokenSlabRemnants_A01`
- `SM_GIA_BloodAxeRedClothThresholdMarker_A01`
- `SM_GIA_BloodAxeDrapedThresholdCloth_A01`
- `SM_GIA_BloodAxePaintedThresholdStone_A01`
- `DOC_GIA_BloodAxeCaveApproachScaleReviewRows_A01`
- `DOC_GIA_BloodAxeCaveApproachThresholdRhythmRows_A01`

Do not create or edit `Content/Aerathea`, `SourceAssets`, `Tools/DCC`, `Tools/Unreal`, runtime source, external concept folders, global indexes, task boards, backlog docs, bootstrap docs, unrelated package files, validators, startup placement files, or any file outside this package path from this task.

## Folder and Naming Recommendation

Docs path:

- `docs/assets/kits/DOC_GIA_BloodAxeCaveApproachLODAndCollision_A01/PRODUCTION_PACKAGE.md`

Package naming:

- `DOC_GIA_BloodAxeCaveApproachLODAndCollision_A01` for this docs-only policy package.
- `DOC_GIA_BloodAxeCaveApproach<Purpose>_A01` for future docs-only scale, review, material, or policy rows.
- `KIT_GIA_BloodAxeCaveApproach<ModuleFamily>_A01` for future kit-level static module packages.
- `SM_GIA_BloodAxe<ModuleName>_A01` for future static mesh module packages.
- `T_GIA_BloodAxe<AssetName>_BC`, `T_GIA_BloodAxe<AssetName>_N`, and `T_GIA_BloodAxe<AssetName>_ORM` for future texture naming if a separate task creates textures.
- `MI_GIA_BloodAxe<MaterialPurpose>_A01` for future material instances if a separate task creates materials.

No source, export, Unreal, runtime, DCC, validator, collision proxy, nav blocker, gameplay volume, startup placement, external concept, index, backlog, task-board, or unrelated package path is created by this package.

## Quality Gate Checklist

- Package uses the Aerathea universal production-package headings where appropriate for a docs-only policy package.
- Package is docs-only and defines policy only.
- File path is limited to `docs/assets/kits/DOC_GIA_BloodAxeCaveApproachLODAndCollision_A01/PRODUCTION_PACKAGE.md`.
- Giant scale lock is explicit from `SK_GIA_Base_A01`: female 442 cm / 14'6" baseline and male 470 cm / 15'5" baseline.
- Approved Giant ranges are explicit: females 14-15 ft / 427-457 cm and males 14'10"-16'0" / 452-488 cm.
- Blood Axe remains a hostile Giant sub-faction and stays separate from neutral/civilized Giant culture.
- Policy covers low cave approach cairns, paired standing stones, broken slab remnants, cloth markers, paint markers, ash bases, and review rows.
- LOD0, LOD1, LOD2, and LOD3 policy is present with a reduction order that removes micro-detail before primary silhouettes.
- Collision policy is disabled by default and simple-only when needed for future large static masses.
- Cloth, paint, ash, mud, cave grit, small accents, and review rows have collision disabled.
- Review rows are non-shipping planning aids and do not imply startup placement, validators, gameplay checks, or final visual approval.
- No collision proxy creation, UCX mesh creation, nav blocker creation, gameplay volume creation, trigger volume creation, objective volume creation, validator creation, DCC work, FBX export, Unreal Content work, runtime source, implementation file, source asset folder, material instance, texture, socket, animation asset, or startup placement is authorized.
- No cave gameplay, traversal proof, path widths as gameplay values, route validation, encounter behavior, AI behavior, objective logic, quest/UI marker, waypoint logic, navigation/pathfinding, damage/aura behavior, interaction behavior, pickup/loot behavior, resource/crafting/economy behavior, destructible behavior, readable text, or route signage is defined.
- Materials stay on rough highland stone, soot, cold ash, cave grit, trampled mud, oxide red cloth, rawhide, rope, blackened iron, sparse old horn, and dull bone.
- Default emissive, ritual glow, shamanic glow, signal glow, animated material states, UI-like markers, refined civic Giant stonework, blue-rune culture, warm hearth settlement language, and neutral/civilized Giant material defaults are absent.
- Triangle budgets, material slot policy, texture map policy, LOD plan, collision policy, animation limits, Unreal import policy, and folder naming are included without performing implementation work.
- Stop if policy work requires collision proxies, UCX meshes, nav blockers, gameplay volumes, trigger volumes, objective volumes, validators, DCC, FBX, Unreal Content, runtime implementation, source asset creation, startup placement, final visual approval, or edits outside the assigned package file.
- Stop if Blood Axe hostile raider language starts replacing neutral/civilized Giant culture.
- Stop if any wording changes the Giant scale lock or treats this document as an implementation directive.
