# DOC_GIA_BloodAxeCaveRemnantClusterReviewRows_A01 Production Package

## Art Direction Summary

- Asset name: `DOC_GIA_BloodAxeCaveRemnantClusterReviewRows_A01`
- Asset type: Documentation-only non-shipping cave remnant cluster review-row package
- Task: `AET-MA-20260629-343`
- Parent package: `KIT_GIA_BloodAxeCaveRemnantCluster_A01`
- Parent child row: `BloodAxeCaveRemnantCluster_A01#ReviewOnly_ClusterSilhouetteRows_A01`
- Related package: `KIT_GIA_BloodAxeCaveRemnantThreshold_A01`
- Related review package: `DOC_GIA_BloodAxeCaveBrokenSlabReviewRows_A01`
- Scale dependency: validated `SK_GIA_Base_A01` Giant scale lock
- Faction/theme: Blood Axe Tribe, hostile Giant sub-faction only
- Status: docs-only planning. No DCC, Unreal actor, validator, capture, startup placement, final visual approval, implementation target, source concept movement, or Hermes work belongs to this scope.

`DOC_GIA_BloodAxeCaveRemnantClusterReviewRows_A01` defines non-shipping comparison rows for abandoned Blood Axe cave remnant cluster silhouettes. The rows compare cairn height, low standing-stone height, old cloth density, ash/mud footprint, cluster silhouette rhythm, and Giant scale before any source or engine work is selected.

This document is a planning artifact, not a game asset. It supports art-direction review only and does not approve source creation, mesh creation, material creation, texture creation, placement, validator work, capture work, final visual signoff, cave signoff, or first implementation sequencing.

Blood Axe visual language remains a hostile Giant sub-faction identity. It must stay separate from neutral/civilized Giant culture, which remains tied to hidden highland settlements, skilled stonework, cave-town terraces, waterworks, hearth warmth, monumental civic masonry, and restrained blue-gray stone language.

## Gameplay Purpose

The purpose is visual comparison only. These rows help later reviewers judge whether cave remnant clusters feel Giant-scaled, abandoned, hostile, restrained, and readable without defining gameplay function.

Allowed planning uses:

- Compare cairn height options without turning the cairn into a waypoint, objective marker, or fortification.
- Compare low standing-stone height options without creating a doorway, cave gate, route lane, or tall standing-stone replacement.
- Compare old cloth density so Blood Axe identity remains visible but does not become a UI cue, banner field, quest pointer, or readable sign.
- Compare ash/mud footprint options so the cluster feels seated in cave grit without becoming a trigger area, aura, damage field, or terrain-integration proof.
- Compare total cluster silhouette options beside locked Giant baselines without selecting a first production target.
- Preserve Blood Axe hostile sub-faction language without replacing neutral/civilized Giant culture.

Out of scope:

- Cave gameplay, cave entrance gameplay marker, traversal proof, path-width rules, route validation, nav/pathfinding, quest/UI markers, encounter triggers, objective markers, interaction behavior, readable signage, spawn logic, patrol logic, combat cover, damage/aura behavior, VFX/audio, source asset creation, DCC, FBX, Unreal actor work, startup placement, validator creation, capture automation, final cave approval, final visual approval, implementation target selection, source concept movement, or Hermes work.

## Silhouette Notes

Review rows should isolate one comparison problem at a time. They should use simple row spacing, broad stone masses, fixed cloth shapes, and clear non-shipping labels rather than dense scene compositions.

Row silhouette families:

- Cairn height row: compare low, standard, heavy, and rejected tower-like cairn reads. The preferred read should use a few large stones rather than many small pebbles.
- Low standing-stone height row: compare short fractured marker, standard low stone, tall but acceptable low stone, and rejected tall-standing-stone drift.
- Old cloth density row: compare no cloth, one tied wrap, restrained wrap plus scrap, dense rag clutter, and rejected banner/UI read.
- Ash footprint row: compare dry contact, thin ash smear, standard irregular ash/mud seat, heavy burial, and rejected circular gameplay-zone read.
- Cluster silhouette row: compare cairn-led, low-stone-led, cloth-accented, ash-grounded, and rejected gate/ritual-marker compositions.
- Giant scale row: compare selected acceptable cluster silhouettes beside female 442 cm and male 470 cm Giant baselines.

Avoid polished civic stonework, refined cave-town masonry, terrace or waterwork forms, warm neutral settlement cues, peaceful wayfinding, blue rune identity, symmetrical monument gateways, route arrows, readable text, objective icons, magic glyphs, active ritual effects, dense trophy clutter, graphic gore, and micro-detail that would not survive mid-poly MMO production.

## Scale Notes

Use the validated Giant scale lock exactly:

- Female Giant baseline: 442 cm / 14 ft 6 in.
- Male Giant baseline: 470 cm / 15 ft 5 in.
- Approved Giant ranges: females 14-15 ft / 427-457 cm and males 14 ft 10 in-16 ft / 452-488 cm.
- These rows must not alter race scale, skeleton policy, collision capsules, sockets, proportions, or character baselines.

Non-shipping cave remnant cluster review-row register:

| Row ID | Review focus | Variants | Scale beside Giant baselines | Planning notes |
| --- | --- | --- | --- | --- |
| `ClusterRow_CairnHeight_A01` | Cairn height | 60 cm low remnant, 120 cm standard low cairn, 190 cm heavy cairn, and 260 cm rejected tower-like stack | Show each cairn beside female 442 cm and male 470 cm baselines | Height is visual massing only, not waypoint strength, cover sizing, blocker sizing, traversal clearance, or fortification proof. |
| `ClusterRow_LowStandingStoneHeight_A01` | Low standing-stone height | 90 cm short fractured marker, 160 cm standard low stone, 240 cm tall low stone, and 340 cm rejected tall-standing-stone drift | Show each stone beside both Giant baselines and below tall standing-stone identity | Height is cluster rhythm only, not a cave gate, route marker, objective frame, or standing-stone replacement. |
| `ClusterRow_OldClothDensity_A01` | Old cloth density | 0 percent, 3 percent tied wrap, 8 percent wrap plus scrap, 14 percent dense but still readable cloth, and over-clothed reject | Show cloth coverage at Giant-readable scale on stone and cairn surfaces | Preferred cloth coverage is 3-8 percent of visible cluster surface; higher density is a rejection reference unless separately approved. |
| `ClusterRow_AshFootprint_A01` | Ash/mud footprint | Dry contact, thin ash smear, standard irregular ash/mud seat, heavy burial, and rejected circular zone | Show footprint spread against Giant feet scale and total cluster width | Footprint is visual seating only, not terrain proof, trigger area, aura, damage field, objective zone, or navigation surface. |
| `ClusterRow_ClusterSilhouette_A01` | Total cluster silhouette | Cairn-led cluster, low-stone-led cluster, cloth-accented cluster, ash-grounded cluster, and rejected gate/ritual-marker cluster | Show total cluster mass beside female 442 cm and male 470 cm baselines | Silhouette is art-direction comparison only and does not select a kit layout, gameplay lane, entrance marker, or first implementation target. |
| `ClusterRow_GiantScale_A01` | Giant scale comparison | Preferred cairn height, preferred low stone height, restrained cloth example, standard ash footprint, and compact full-cluster example | Show female 442 cm and male 470 cm baselines consistently at row start | Scale review is non-shipping and does not certify collision, camera, cave placement, terrain integration, or final visual approval. |

All dimensions are visual planning values only. They are not cave gameplay measurements, traversal proof, collision correctness claims, encounter spacing, trigger sizes, interaction ranges, camera approval metrics, terrain integration values, marker validation, or final cave approval metrics.

## Materials and Color Palette

Primary materials:

- Rough highland stone, fractured cave-edge field rock, ash-stained cairn stones, dark granite, soot-blackened recesses, and chipped low standing-stone faces.
- Packed mud, trampled earth, cold ash, charcoal dust, cave grit, dry stone dust, muted lichen, and eroded cave-edge dirt.
- Faded oxide red cloth, dirty maroon cloth residue, soot-darkened red scraps, rope residue, rawhide ties, and scorched leather scraps used sparingly.
- Sparse blackened iron, old horn chips, and dull bone tokens only as secondary hostile cues.

Palette targets:

- Dominant: charcoal gray, dark stone gray, ash gray, cave black, weathered slate, mud brown, and cold dust.
- Blood Axe accent: oxide red, faded maroon, dirty red, and chipped dark red-brown in restrained cloth or paint beats.
- Secondary accent: rawhide tan, old horn tan, dull bone ivory, rubbed dark iron, and muted lichen green.
- Emissive: absent. No glow, ritual light, shamanic pulse, signal light, torch state, UI highlight, objective highlight, or animated material state belongs to this package.

Material ratio guidance:

- Stone, soot, ash, cave grit, and mud should carry 80-90 percent of the visual read.
- Old cloth should usually stay within 3-8 percent of visible cluster surface.
- Rope, rawhide, iron, horn, and bone should remain sparse secondary accents.
- Neutral/civilized Giant material language must not become the default Blood Axe read.

## Concept Image Prompt

Create an original stylized fantasy MMORPG documentation planning board of `DOC_GIA_BloodAxeCaveRemnantClusterReviewRows_A01` for the world of Aerathea. The design should emphasize non-shipping review rows for Blood Axe cave remnant cluster silhouettes, cairn height comparison, low standing-stone height comparison, old cloth density comparison, ash and mud footprint comparison, full cluster silhouette comparison, rough highland stone, soot-blackened cave-edge rock, cold ash, trampled mud, cave grit, restrained oxide red cloth, rope and rawhide accents, hostile Giant sub-faction identity, strict separation from neutral/civilized Giant culture, and validated Giant scale with a female 442 cm / 14 ft 6 in baseline and male 470 cm / 15 ft 5 in baseline. Use hand-painted texture detail only in planning swatches, readable chunky shapes, baked-AO-style depth, normal-map-style surface detail, no emissive glow, and MMO-friendly production design. Present it as a clean docs-only comparison sheet with row labels, scale callouts, material restraint notes, rejection examples, and stop gates on a neutral background. Avoid copying any existing franchise, avoid cave gameplay diagrams, avoid traversal proof, avoid collision correctness claims, avoid nav/pathfinding diagrams, avoid quest/UI markers, avoid encounter triggers, avoid objective markers, avoid route validation, avoid readable route text, avoid UI arrows, avoid magic glyphs, avoid VFX/audio, avoid DCC or FBX claims, avoid Unreal implementation claims, avoid startup placement, avoid final approval language, avoid selecting a first implementation target, avoid source concept movement, avoid Hermes work, avoid neutral Giant cave-town architecture as Blood Axe default language, avoid graphic gore, and avoid excessive micro-detail that would not translate to mid-poly assets.

## Modeling Notes

This is a docs-only review-row plan. No source folder, Blender file, mesh, sculpt, retopo, UV, bake, proof render, LOD source, collision proxy, FBX export, Unreal asset, material instance, texture asset, material graph, validator, runtime source, Blueprint, socket, animation, startup placement, implementation target, source concept movement, Hermes work, cave signoff, or visual signoff is created or authorized.

Review rows should remain document-level comparisons:

- Cairn height row: use the same few-large-stones cairn language at different heights so scale drift is easy to judge.
- Low standing-stone height row: use broad fractured slabs that remain shorter and older than tall standing-stone assets.
- Old cloth density row: use fixed wraps and scraps on the same stone/cairn silhouette so cloth restraint is easy to compare.
- Ash footprint row: use irregular non-circular ash/mud contact shapes and clearly reject any ring, aura, or objective-zone read.
- Cluster silhouette row: combine cairn, low stone, cloth, and ash/mud elements in compact silhouettes without forming a functional gateway.
- Giant scale row: repeat the strongest acceptable examples beside the female 442 cm and male 470 cm baselines.

If later art-direction work creates a visual sheet, keep rows flat, clearly non-shipping, and limited to broad silhouettes. Do not model new assets, construct review geometry, author collision, create validators, place actors, move source concepts, or select a first production item from this package.

## Texture and Material Notes

This package creates no textures, materials, material instances, texture atlases, masks, or material graphs.

If a later separately scoped art sheet uses material swatches, keep them aligned with the existing Blood Axe cave remnant family:

- Base Color / Albedo (`BC`) should carry dark stone, soot, ash, mud, cave grit, faded oxide red cloth, rawhide, rope, sparse blackened iron, old horn, and dull bone.
- Normal (`N`) should describe broad stone planes, large breaks, ash/mud grounding, coarse stone pitting, fixed cloth folds, rope/rawhide pressure, and major contact shadows.
- Packed Occlusion/Roughness/Metallic (`ORM`) should emphasize contact shadows under stones, cloth wraps, mud buildup, soot pockets, and stone occlusion; roughness remains high and metallic remains near zero except sparse blackened iron.
- Emissive (`E`) is not part of this package.

No unique material should be created for each row, stone face, cloth scrap, ash patch, mud smear, rope tie, horn chip, bone token, lichen fleck, or crack. Fine cracks, soot speckles, ash flecks, chipped stone, stone pitting, cloth weave, fray, lichen, mud streaks, grit, rope fibers, and small scratches remain texture or normal-map concerns for future child assets only.

## Triangle Budget

This package creates no mesh and has no shipping triangle budget.

Reference budgets for future child assets remain owned by their packages:

- Low cave remnant cairn: 1.5k-5k tris at LOD0, 1 material target.
- Collapsed cave remnant cairn: 2k-7k tris at LOD0, 1 material target.
- Low standing stone or broken leaning cave stone: 1.2k-4.5k tris at LOD0, 1 material target.
- Fixed old cloth wrap or draped scrap: 500-2.5k tris at LOD0, usually included with the parent stone or cairn module.
- Ash/mud base or cold fire-scar dressing: 500-3k tris at LOD0, collision disabled by default.
- Compact remnant threshold cluster: 4k-10k tris total at LOD0, 1-2 material target.
- Non-shipping review row visual sheet: no mesh by default; if a separate task creates simple row geometry, keep it to simple blockout silhouettes only and do not treat it as a shipping asset.

Any future geometry budget should spend triangles on primary cairn masses, broad low standing-stone silhouettes, large chipped planes, fixed cloth folds, and ash/mud grounding forms. Do not spend triangles on tiny cracks, soot speckles, ash flecks, cloth weave, fray fibers, paint chips, lichen, mud flecks, grit, small scratches, or repeated small tokens.

## LOD Plan

This package creates no LOD source. LOD guidance here is a review-row reminder for future child assets only.

- LOD0: preserve full cluster massing, cairn height read, low standing-stone height read, fixed cloth density, ash/mud footprint, and compact Blood Axe cave-remnant silhouette.
- LOD1: preserve the main row composition while reducing small bevels, secondary chips, cloth-edge cuts, minor rope/rawhide detail, hidden back-facing detail, and minor ash/mud undercuts.
- LOD2: preserve big massing only: cairn height, low stone height, one restrained cloth color block, and broad cave-edge grounding.
- LOD3: preserve the abandoned cave-remnant read only: compact dark stone cluster, low asymmetrical silhouette, and minimal Blood Axe color cue where needed.

Reduction order for future child assets:

1. Remove tiny cracks, soot speckles, ash flecks, lichen specks, cloth weave, fray fibers, grit dots, and minor scratches.
2. Remove small stone chips, tiny rubble, horn chips, bone pores, minor iron nicks, rope fiber cuts, and shallow mud crumbs.
3. Reduce back-facing stones, hidden underside bevels, buried contact cuts, and non-visible ash/mud undercuts.
4. Reduce secondary cloth fray, duplicate foot stones, small paint islands, and optional review-row helper detail.
5. Reduce stone bevel density, cairn edge cuts, ash/mud ridge geometry, and secondary base-plane subdivisions.
6. Only after small detail is gone, simplify the primary cairn height, low standing-stone height, cloth density read, ash footprint, or cluster silhouette.

Never reduce Giant-scale readability, Blood Axe hostile sub-faction read, static cave-edge memory, compact cluster massing, or primary silhouette before removing small detail.

## Collision Notes

Collision is out of scope for this docs-only review-row package. Do not create collision proxies, UCX meshes, engine settings, physics bodies, nav blockers, smart links, gameplay volumes, trigger volumes, damage volumes, aura volumes, objective volumes, interaction volumes, validator scripts, or runtime setup from this package.

Review-row collision policy:

- Documentation rows: collision not applicable.
- Any future visual sheet rows: collision disabled.
- Cloth, ash, mud, soot, cave grit, lichen, rope residue, horn chips, bone tokens, and small accents: collision disabled in future child assets unless a separate package changes the scope.
- Large stone bodies: collision planning remains owned by the relevant future child asset package and must not be certified here.

This package makes no claim of collision correctness, cave compatibility, pathing validity, traversal clearance, player movement validity, combat cover, route blocking, camera clearance, objective-zone behavior, interaction behavior, terrain blending, runtime performance validation, marker validation, or nav/pathfinding validity.

## Animation Notes

The review rows are static documentation.

Allowed at planning level:

- Static cairn height comparisons.
- Static low standing-stone height comparisons.
- Static old cloth density comparisons.
- Static ash/mud footprint comparisons.
- Static cluster silhouette comparisons.
- Static Giant scale comparison rows.

Not part of this package:

- Physics collapse, destructible breakage, moving stones, falling stones, cloth simulation, wind sway, torch states, material pulse, glow, particles, VFX, audio, Blueprint state, interaction state, quest state, objective state, encounter state, damage state, aura state, cave gameplay state, nav/pathfinding behavior, startup placement, source concept movement, Hermes work, or runtime behavior.

Any moving, glowing, interactive, objective-readable, UI-readable, audio-linked, damaging, route-affecting, cave-trigger-readable, or gameplay-readable variant needs a separately named package and explicit scope.

## Unreal Import Notes

This section is future guardrail planning only because the universal package format requires import notes. No Unreal asset, game folder, import script, material instance, texture asset, socket, Blueprint, validator, runtime source, review actor, startup actor, source asset, DCC work, FBX export, cave placement, collision setup, nav/pathfinding setup, trigger setup, objective setup, quest/UI setup, interaction setup, VFX/audio setup, source concept movement, Hermes work, or first implementation target is created or authorized.

Potential future identity after separate lead authorization:

- Asset name: `DOC_GIA_BloodAxeCaveRemnantClusterReviewRows_A01`
- Asset type: Documentation-only non-shipping cave remnant cluster review-row package
- Game asset status: none selected and none created
- Pivot guidance: not applicable to the documentation package
- Orientation guidance: not applicable to the documentation package
- Scale reference: female Giant 442 cm / 14 ft 6 in and male Giant 470 cm / 15 ft 5 in; approved Giant ranges remain females 14-15 ft / 427-457 cm and males 14 ft 10 in-16 ft / 452-488 cm
- Collision type: not applicable; no collision is created or validated
- LOD plan: planning reference only; no LOD source is created
- Material slot count: not applicable; no material is created
- Texture list: not applicable; no texture is created
- Sockets: none
- Animation list: none
- Blueprint behavior: none
- Performance notes: use the document to prevent cairn-height overreach, low-stone tall-monument drift, cloth overuse, ash/mud trigger-zone reads, cluster gate reads, unnecessary material splits, collision overreach, and gameplay-readable marker drift in later packages.

No folder path in game content is selected by this docs-only package.

## Folder and Naming Recommendation

Documentation path:

- `docs/assets/kits/DOC_GIA_BloodAxeCaveRemnantClusterReviewRows_A01/PRODUCTION_PACKAGE.md`

Review-row identifiers:

- `ClusterRow_CairnHeight_A01`
- `ClusterRow_LowStandingStoneHeight_A01`
- `ClusterRow_OldClothDensity_A01`
- `ClusterRow_AshFootprint_A01`
- `ClusterRow_ClusterSilhouette_A01`
- `ClusterRow_GiantScale_A01`

Related source-of-truth packages:

- `KIT_GIA_BloodAxeCaveRemnantCluster_A01`
- `KIT_GIA_BloodAxeCaveRemnantThreshold_A01`
- `DOC_GIA_BloodAxeCaveBrokenSlabReviewRows_A01`
- `SK_GIA_Base_A01` for Giant scale lock

Do not create or edit source asset folders, DCC files, FBX exports, Unreal game content folders, material graphs, material instances, texture assets, validators, global indexes, backlog docs, task-board docs, bootstrap docs, child intake docs, startup placement, external source concept files, runtime source files, VFX assets, audio assets, Hermes files/config, or unrelated package files from this task.

## Quality Gate Checklist

- Required universal package headings are present in order for a docs-only review-row package.
- Package is limited to `docs/assets/kits/DOC_GIA_BloodAxeCaveRemnantClusterReviewRows_A01/PRODUCTION_PACKAGE.md`.
- Package is non-shipping and does not create a mesh, source asset, material instance, texture asset, validator, runtime source, Unreal asset, startup placement, approval artifact, source concept movement, Hermes work, or first implementation target.
- Review rows compare cairn height, low standing-stone height, old cloth density, ash/mud footprint, cluster silhouette, and Giant scale.
- Cairn height values are visual massing only and do not define waypoint strength, cover sizing, blocker sizing, traversal clearance, fortification proof, or placement approval.
- Low standing-stone height remains cluster rhythm only and does not define a cave gate, route marker, objective frame, or tall standing-stone replacement.
- Old cloth density remains restrained, with 3-8 percent as the preferred visible cluster-surface target and over-clothed rows treated as rejection references.
- Ash/mud footprint remains visual seating and does not become a trigger zone, aura, damage field, objective zone, terrain proof, or navigation surface.
- Cluster silhouette remains composition-only and does not define a doorway, route lane, nav gap, route blocker, ritual activation marker, or traversal rule.
- Giant scale lock is explicit: female 442 cm / 14 ft 6 in baseline and male 470 cm / 15 ft 5 in baseline.
- Approved Giant ranges are explicit: females 14-15 ft / 427-457 cm and males 14 ft 10 in-16 ft / 452-488 cm.
- Blood Axe remains a hostile Giant sub-faction and does not replace neutral/civilized Giant culture.
- Neutral/civilized Giant culture remains separate: hidden highland settlements, skilled stonework, cave-town terraces, waterworks, hearth warmth, monumental civic masonry, and restrained blue-gray stone language.
- Review rows use rough stone, soot, ash, trampled mud, cave grit, oxide red cloth, rope, rawhide, sparse blackened iron, old horn, and dull bone without default emissive.
- No cave gameplay, traversal proof, collision correctness, nav/pathfinding, quest/UI marker, encounter trigger, objective marker, readable signage, VFX/audio, DCC, FBX, Unreal, source asset creation, startup placement, validator work, capture work, final cave approval, final visual approval, source concept movement, Hermes work, or first implementation target is defined.
- Fine cracks, soot speckles, ash flecks, stone pitting, cloth weave, fray, lichen, mud streaks, grit, rope fibers, and small scratches are assigned to future textures or normals, not modeled review-row detail.
- LOD0-LOD3 guidance, no-collision guardrails, animation limits, import-planning guardrails, folder naming, and stop gates are included without claiming shipping readiness.
