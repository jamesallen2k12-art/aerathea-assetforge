# KIT_GIA_BloodAxeLowThresholdCairnPair_AshBase_A01 Production Package

## Art Direction Summary

- Asset name: `KIT_GIA_BloodAxeLowThresholdCairnPair_AshBase_A01`
- Asset type: Kit production package / docs-only static environment dressing planning
- Task: `AET-MA-20260629-236`
- Parent kit: `KIT_GIA_BloodAxeLowThresholdCairns_A01`
- Source row: `BloodAxeLowThresholdCairns_A01#AshBasePair_A01`
- Grounding reference: `SM_GIA_BloodAxeCaveAshRemnantBase_A01`
- Material reference: `DOC_GIA_BloodAxeCaveApproachMaterialDiscipline_A01`
- Scale dependency: validated `SK_GIA_Base_A01` Giant scale lock
- Faction/theme: Blood Axe Tribe, hostile Giant sub-faction only
- Status: docs-only package; no decal gameplay, trigger area, damage field, aura field, objective zone, material graph work, VFX/audio, DCC, FBX, Unreal Content, startup placement, final approval, or first implementation target is created or authorized

`KIT_GIA_BloodAxeLowThresholdCairnPair_AshBase_A01` defines a paired low-threshold cairn kit grounded by broad cold ash, soot, trampled mud, cave grit, and support contact shadows. The cairns should read as squat, crude, Giant-built warning masses that have settled into an old cave approach, with the ash base acting as static visual grounding only.

The ash base material and material language are read-only references for this package. This package may plan how paired cairns sit on `SM_GIA_BloodAxeCaveAshRemnantBase_A01`, but it does not alter that ash-base package, create material instances, create textures, author material graphs, or define any gameplay decal behavior.

Blood Axe visual language must stay separate from neutral/civilized Giant culture. This kit may suggest hostile Giant raider occupation through rough stones, cold ash, soot, trampled mud, cave grit, sparse rope/rawhide, and restrained oxide red contamination. It must not become the default Giant cultural identity. Neutral/civilized Giant culture remains tied to hidden highland settlements, skilled stonework, cave-town terraces, waterworks, hearth warmth, monumental masonry, blue-gray civic stonework, and restrained blue-rune culture.

## Gameplay Purpose

The purpose is visual planning only. The kit provides a grounded paired low-cairn composition for Blood Axe cave approaches without becoming a gate, marker volume, hazard, quest target, route cue, or interaction object.

Allowed planning uses:

- Define a static paired low-threshold cairn composition grounded by cold ash, soot, trampled mud, cave grit, and broad contact shadows.
- Support Blood Axe territory readability near cave edges, camp thresholds, or old hostile occupation breaks.
- Keep the ash base as a matte, static support read beneath the stones rather than a decal gameplay system.
- Provide future DCC and Unreal owners with clear stop gates, scale planning, LOD planning, and material restraint language.
- Preserve Blood Axe as a hostile Giant sub-faction while protecting neutral/civilized Giant culture from visual drift.

Out of scope:

- No decal gameplay, trigger area, damage field, aura field, objective zone, quest/UI marker, encounter marker, gate behavior, route validation, path-width rule, nav/pathfinding, interaction behavior, readable signage, spawn logic, patrol logic, VFX/audio, material graph work, collision correctness, DCC, FBX, Unreal Content, startup placement, final visual approval, final Blood Axe approval, final cave approval, or first implementation target selection.

## Silhouette Notes

Primary silhouette read:

- Two squat low cairns placed as a paired threshold rhythm, with one side allowed to be slightly wider or lower so the pair avoids formal doorway symmetry.
- Each cairn uses a few large Giant-placed stones, not dense pebble piles.
- A shared or broken ash base spreads under and between the cairns, with feathered irregular edges and no clean circular radius.
- Broad contact shadows should ground every support stone into the ash, soot, mud, and cave grit.
- The ash base should remain lower than the cairns and should never become the primary read from MMO camera distance.
- Optional restrained edge contamination may include a dirty oxide-red cloth smear, old rope residue, a few embedded stone chips, or charred stick fragments.

Future geometry, if separately approved, should model the main stone masses, large chipped planes, broad ash/mud base silhouette, major embedded stone chips, and visible ground-contact lips. Fine cracks, ash flecks, soot speckles, mud streaks, cloth fibers, rope fibers, grit, lichen, pitting, small scratches, and chipped paint belong to future textures, normals, AO, or masks.

Avoid perfect rings, radial decals, hazard borders, objective circles, route arrows, readable text, UI symbols, magic glyph panels, glow-based entrance cues, smoke columns, particle wisps, warm hearth settlement cues, refined civic masonry, blue-rune identity, dense skull piles, graphic gore, and micro-detail that would not survive mid-poly MMO production.

## Scale Notes

Use the Giant scale lock from `SK_GIA_Base_A01`:

- Female Giant baseline: 442 cm / 14'6".
- Male Giant baseline: 470 cm / 15'5".
- Approved Giant ranges: females 14-15 ft / 427-457 cm and males 14'10"-16'0" / 452-488 cm.
- Future source, if separately approved, should be authored in centimeters with 1 Unreal unit = 1 cm.

Visual planning dimensions:

- Left cairn: 70-145 cm tall, 150-320 cm footprint.
- Right cairn: 80-170 cm tall, 140-340 cm footprint.
- Pair spacing: 280-620 cm between primary stone centers as visual rhythm only.
- Shared ash support base: 420-900 cm wide by 260-640 cm deep.
- Broken ash support base option: two overlapping low ash pads with 40-160 cm of visual overlap or near-contact.
- Ash/mud height profile: 2-18 cm, with rare 25-45 cm raised mud lips or embedded stone chips.
- Contact shadow zone: broad, dark, non-emissive grounding beneath each stone mass, painted or baked into future material detail rather than defined as a gameplay volume.

These values are visual planning measurements only. They are not decal extents, trigger sizes, damage radii, aura radii, objective-marker ranges, route validation, path-width rules, nav/pathfinding values, traversal proof, encounter spacing, camera approval metrics, collision correctness, or final placement rules.

## Materials and Color Palette

Primary materials:

- Rough highland stone, weathered granite, fractured gray slabs, ash-stained field rock, soot-blackened cave-edge stone, and broad chipped planes.
- Matte dry ash, cold charcoal dust, cave grit, trampled mud, packed earth, and dark threshold dirt.
- Optional restrained oxide-red contamination as dirty cloth smear, worn pigment dust, faded cloth edge, or tiny stained grit at the base edge.
- Sparse rope, rawhide, sinew, charred wood, blackened iron, old horn, or dull bone only where they support the Blood Axe read without clutter.

Palette targets:

- Stone and soot: `#151718`, `#222527`, `#343635`, `#4E4D47`
- Cold ash and stone dust: `#5F5D56`, `#7A766C`, `#9A9487`, `#C0B5A3`
- Cave grit and trampled mud: `#241D17`, `#382C22`, `#554332`, `#6F5B45`
- Restrained Blood Axe contamination: `#531411`, `#6B1A16`, `#81251D`
- Rope, rawhide, old horn, and dull bone: `#4E3925`, `#8E7048`, `#AE986B`, `#C6B78A`
- Blackened iron: `#0F1011`, `#202326`, `#383D3E`

Material restraint:

- Stone, soot, ash, cave grit, and trampled mud carry roughly 85-95 percent of the visual read.
- Oxide red contamination stays below 5 percent unless a later red-cloth package owns a stronger accent.
- The ash base is static and read-only in this package; do not change its material policy, material slot count, texture names, or material graph.
- No emissive map, glow edge, heat pulse, magic stain, torch state, smoke material, particle material, aura material, damage field, objective highlight, or animated material state belongs to this baseline kit.
- Exclude neutral/civilized Giant culture as the default material read: no refined blue-gray civic masonry, terrace or waterwork motifs, warm hearth dirt language, peaceful highland guide marks, carved civic ornament, restrained blue rune identity, or polished stonework.

## Concept Image Prompt

Create an original stylized fantasy MMORPG production kit board of `KIT_GIA_BloodAxeLowThresholdCairnPair_AshBase_A01` for the world of Aerathea. The design should emphasize paired low-threshold cairns, squat Giant-scale rough stone clusters, a broad static cold ash support base, soot, trampled mud, cave grit, heavy support contact shadows, irregular non-circular ash edges, sparse rope or rawhide residue, restrained oxide red contamination, hostile Blood Axe Giant sub-faction identity, strict separation from neutral/civilized Giant culture, abandoned cave-edge threshold mood, and the visual role of static environmental grounding only. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, no emissive glow, no particles, and MMO-friendly mid-poly production design. Present it as a docs-only kit production sheet with top view, three-quarter view, material swatches, LOD planning notes, collision stop gates, and scale markers beside a female 442 cm Giant and a male 470 cm Giant from `SK_GIA_Base_A01` on a clean background. Avoid copying any existing franchise, avoid perfect circles, avoid decal gameplay, avoid trigger areas, avoid damage fields, avoid aura rings, avoid objective zones, avoid quest/UI markers, avoid encounter markers, avoid nav/pathfinding diagrams, avoid route arrows, avoid interaction affordances, avoid readable text, avoid VFX/audio cues, avoid material graph language, avoid DCC, avoid FBX, avoid Unreal approval claims, avoid startup placement, avoid final visual approval language, avoid selecting a first implementation target, avoid neutral Giant cave-town architecture as Blood Axe default language, avoid warm hearth settlement cues, avoid magic glow, avoid graphic gore, and avoid excessive micro-detail that would not translate to a mid-poly static kit.

## Modeling Notes

This is a docs-only modeling plan. No DCC source, Blender file, mesh, sculpt, retopo, UV, bake, proof render, LOD source, collision proxy, FBX export, Unreal Content asset, material instance, texture asset, material graph, validator, runtime source, Blueprint, socket, animation, startup placement, final visual approval, or first implementation target is created or authorized.

Future source work, if separately approved, should treat the kit as a static paired composition:

- Build two low cairn clusters from a few large stones each, using broad planes, limited bevels, and chunky chipped silhouettes.
- Use the ash base as a shallow irregular support mesh or shared static ground form, not as a decal gameplay plane and not as a radial marker.
- Add broad ground-contact lips and dark contact-shadow areas where stones compress ash, soot, mud, and cave grit.
- Keep the ash base feathered and broken so it can rotate or scale with other Blood Axe cave approach dressing.
- Keep optional contamination sparse: one or two broad stone chips, a small cloth-edge smear, old rope residue, or a charred stick fragment.
- Use modular reuse where possible: left cairn, right cairn, and ash support base may be separate future static modules if a later implementation owner scopes them.

Do not model dense pebble fields, hundreds of cracks, ash grains, soot puffs, cloth fuzz, rope fibers, tiny stick scatter, readable symbols, UI-like rings, hazard borders, magic stains, gore-heavy residue, or per-detail collision shapes.

## Texture and Material Notes

Use standard Aerathea texture outputs only if a later task approves asset creation:

- Base Color / Albedo (`BC`)
- Normal (`N`)
- Packed Occlusion/Roughness/Metallic (`ORM`)
- Emissive (`E`) is not part of this baseline package and requires a separate approved package

Suggested future texture naming, planning only:

- `T_GIA_BloodAxeLowThresholdCairnPair_AshBase_A01_BC`
- `T_GIA_BloodAxeLowThresholdCairnPair_AshBase_A01_N`
- `T_GIA_BloodAxeLowThresholdCairnPair_AshBase_A01_ORM`
- Read-only reference only: `T_GIA_BloodAxeCaveAshRemnantBase_A01_BC`
- Read-only reference only: `T_GIA_BloodAxeCaveAshRemnantBase_A01_N`
- Read-only reference only: `T_GIA_BloodAxeCaveAshRemnantBase_A01_ORM`

Material slot target:

- 1 material target when stone, ash, soot, mud, and grit can share a Blood Axe cave-approach atlas.
- 2 material maximum only if a later approved task separates stone/cairn material from a shared ash-remnant base material.
- No baseline emissive texture, no particle material, no aura material, no decal gameplay material, no VFX material, and no material graph authoring in this package.

Texture detail guidance:

- Base Color should carry dark stone value groups, cold ash value shifts, soot darkening, muddy browns, cave grit, dull stone chips, and restrained dirty red contamination.
- Normal should carry chipped stone planes, shallow ash ridges, trampled mud ripples, broad scuffs, and embedded stone edges.
- ORM should keep roughness high and metallic at zero except rare dull scrap accents if a later approved art direction requires them.
- AO should ground stone contacts, perimeter buildup, ash/mud undercuts, and support contact shadows.

Fine ash flecks, soot speckles, grit, mud streaks, cloth fibers, stone scratches, lichen, chipped pigment, and small scuffs should remain texture-led. Do not create unique materials for small surface contamination.

## Triangle Budget

This package creates no mesh. Future LOD0 planning targets:

- Left low cairn: 900-2.4k tris, 1 material.
- Right low cairn: 900-2.6k tris, 1 material.
- Shared ash support base: 700-2.4k tris, 1 material.
- Optional embedded stone or cloth-edge contamination: included in the above targets, not added as dense separate scatter.
- Full paired ash-base composition: 2.5k-8.5k tris total, 1 material target, 2 material maximum with later approval.

Spend geometry on the main stone masses, broad chipped planes, irregular ash footprint, raised mud lips, major ash ridges, embedded stone silhouettes, and readable stone-to-ground contact. Do not spend geometry on ash grains, soot speckles, grit flecks, small pebbles, cloth fibers, rope strands, fine cracks, lichen, paint chips, foot dust, or hidden underside detail.

## LOD Plan

All future important static meshes need LOD0, LOD1, LOD2, and LOD3 before any separate implementation signoff.

- LOD0: full paired low-cairn forms, major stone planes, broad ash support base, contact-shadow zones, shallow mud lips, cave grit buildup, embedded stone reads, and restrained contamination.
- LOD1: 60-70 percent of LOD0; reduce small bevels, minor perimeter cuts, secondary stone chips, small ash ridges, cloth-edge subdivisions, and hidden underside detail.
- LOD2: 35-45 percent of LOD0; simplify each cairn into larger stone masses, flatten small base ridges, merge embedded stones into the base, remove non-silhouette accents, and keep the broad paired rhythm.
- LOD3: 15-25 percent of LOD0; preserve only the paired low-threshold cairn rhythm, broad dark stone masses, and non-circular cold ash support footprint.

Reduction order:

1. Fine ash flecks, soot speckles, grit dots, cloth fibers, mud streak texture accents, pitting, lichen, paint chips, and tiny scratches.
2. Minor perimeter notches, small stone chips, small cloth-edge tears, tiny raised mud crumbs, and non-silhouette contamination.
3. Secondary ash ridges, small scuff geometry, hidden underside cuts, and back-facing bevels.
4. Embedded stones that do not affect the main silhouette.
5. Broad mud lip density, stone bevel density, and low mound subdivisions.
6. Only after small detail is gone, simplify the main paired low-cairn rhythm and shared ash support footprint.

Never simplify the kit into a perfect circle, clean ring, objective zone, aura radius, trigger shape, route marker, or UI-readable sign.

## Collision Notes

Collision is planning only. Do not create collision proxies, UCX meshes, Unreal collision settings, physics bodies, nav/pathfinding helpers, blockers, smart links, gameplay volumes, trigger volumes, damage volumes, aura volumes, objective volumes, interaction volumes, validator scripts, or runtime setup from this package.

Future static collision intent:

- Ash base, soot, mud, cave grit, cloth-edge contamination, small stones, scuffs, and surface detail: collision disabled.
- Low cairn stones: collision disabled by default; simple primitive blocking only if a later owner separately requests basic static blocking for large stone masses.
- Shared composition: no path gate, no route validation, no passage promise, no encounter lane, no cover guarantee, and no traversal proof.
- Review-only rows, if later created elsewhere: collision disabled.

This package makes no claim of collision correctness, cave compatibility, pathing validity, traversal clearance, route behavior, encounter spacing, spawn safety, cover behavior, camera clearance, terrain blending, or runtime performance validation.

## Animation Notes

Baseline kit is static.

Allowed at planning level:

- Static paired low cairns.
- Static cold ash, soot, trampled mud, cave grit, embedded stone, and optional cloth-edge contamination.
- Static material variation for ash value, soot density, dry mud value, cave grit, stone darkening, and restrained Blood Axe contamination if a later material task approves it.

Not approved here:

- No particle effects, smoke wisps, dust plumes, ember drift, glow, heat haze, torch states, material pulses, aura behavior, damage states, decal gameplay, cloth simulation, wind motion, audio cues, destructible behavior, pickup behavior, quest/UI behavior, objective behavior, trigger behavior, interaction behavior, nav/pathfinding behavior, startup placement, or runtime behavior.

Any moving, glowing, interactive, objective-readable, damaging, aura-based, particle-based, audio-driven, or gameplay-readable version must be split into a separately named and approved package.

## Unreal Import Notes

This section is future guardrail planning only. No Unreal Content asset, game folder, import script, material instance, texture asset, socket, Blueprint, validator, runtime source, review actor, startup actor, source asset, DCC source, FBX export, cave placement, collision setup, nav/pathfinding setup, trigger setup, objective setup, quest/UI setup, interaction setup, material graph authoring, VFX/audio setup, or first implementation target is created or authorized.

Potential future identity after separate approval:

- Asset name: `KIT_GIA_BloodAxeLowThresholdCairnPair_AshBase_A01`
- Asset type: Static Mesh kit planning package
- Game asset status: none selected and none created
- Folder path if later promoted: no game content folder selected by this docs-only package
- Pivot guidance if later promoted: composition center at ground contact, centered between the two cairns and the ash support footprint
- Orientation if later promoted: primary readable side faces +X unless a later export task establishes a different project convention
- Scale if later promoted: centimeter-authored source using `SK_GIA_Base_A01` female 442 cm and male 470 cm baselines for review comparison
- Collision if later promoted: disabled by default for ash base and detail; optional simple static hulls only for separately requested large stone bodies
- LODs if later promoted: LOD0-LOD3 required for any shipping mesh
- Material slots if later promoted: 1 target, 2 maximum only with later approval for a shared ash-remnant base split
- Texture list if later promoted: `T_GIA_BloodAxeLowThresholdCairnPair_AshBase_A01_BC`, `T_GIA_BloodAxeLowThresholdCairnPair_AshBase_A01_N`, and `T_GIA_BloodAxeLowThresholdCairnPair_AshBase_A01_ORM`; no baseline emissive texture
- Sockets: none
- Animation list: none
- Blueprint behavior: none
- Performance notes: keep the composition low-poly, matte, non-emissive, non-interactive, low material count, collision-disabled by default for detail, and free of VFX/audio or runtime behavior

## Folder and Naming Recommendation

Docs:

- `docs/assets/kits/KIT_GIA_BloodAxeLowThresholdCairnPair_AshBase_A01/PRODUCTION_PACKAGE.md`

Future planning names only:

- `KIT_GIA_BloodAxeLowThresholdCairnPair_AshBase_A01`
- `SM_GIA_BloodAxeLowThresholdCairnPair_AshBase_A01`
- `T_GIA_BloodAxeLowThresholdCairnPair_AshBase_A01_BC`
- `T_GIA_BloodAxeLowThresholdCairnPair_AshBase_A01_N`
- `T_GIA_BloodAxeLowThresholdCairnPair_AshBase_A01_ORM`
- Read-only grounding reference: `SM_GIA_BloodAxeCaveAshRemnantBase_A01`

Do not create source asset folders, DCC files, FBX exports, game content folders, material instances, texture assets, validators, global index edits, backlog edits, task-board edits, startup placement, external source concept copies, runtime files, material graph files, VFX/audio assets, collision proxies, or unrelated package files from this task.

## Quality Gate Checklist

- Required package headings are present in the requested 15-section order.
- Package is docs-only and limited to `docs/assets/kits/KIT_GIA_BloodAxeLowThresholdCairnPair_AshBase_A01/PRODUCTION_PACKAGE.md` for task `AET-MA-20260629-236`.
- Asset remains a paired low-threshold cairn kit grounded by broad cold ash, soot, trampled mud, cave grit, and support contact shadows.
- The ash base material is static and read-only; no material graph, material instance, texture asset, decal gameplay, VFX material, aura material, or animated material state is created or authorized.
- Giant scale lock is explicit from `SK_GIA_Base_A01`: female 442 cm / 14'6" baseline and male 470 cm / 15'5" baseline.
- Approved Giant ranges are explicit: females 14-15 ft / 427-457 cm and males 14'10"-16'0" / 452-488 cm.
- Blood Axe remains a hostile Giant sub-faction and does not replace neutral/civilized Giant culture.
- Materials remain matte and restrained: rough highland stone, dry ash, soot, cave grit, trampled mud, optional embedded stone, sparse rope/rawhide, and restrained oxide-red contamination.
- No particles, aura, emissive glow, decal gameplay, trigger area, damage field, objective zone, quest/UI marker, nav/pathfinding, interaction behavior, VFX/audio, material graph authoring, DCC, FBX, Unreal, startup placement, final approval, first implementation target, source asset creation, material instance, texture asset, validator, runtime source, Blueprint, socket, animation, collision proxy, or collision correctness claim is defined.
- Silhouette remains irregular and non-circular, never a clean ring, route marker, objective radius, trigger shape, aura radius, or UI-readable sign.
- Fine ash flecks, soot speckles, grit, mud streaks, cloth fibers, stone scratches, lichen, chipped pigment, and small scuffs are assigned to textures or normals in future packages.
- LOD0-LOD3 planning, triangle budgets, collision limits, animation limits, folder naming, import-planning guardrails, material restraint, and stop gates are included.
