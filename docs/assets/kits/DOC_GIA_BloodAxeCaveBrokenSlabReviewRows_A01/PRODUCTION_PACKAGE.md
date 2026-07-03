# DOC_GIA_BloodAxeCaveBrokenSlabReviewRows_A01 Production Package

## Art Direction Summary

- Asset name: `DOC_GIA_BloodAxeCaveBrokenSlabReviewRows_A01`
- Asset type: Documentation-only non-shipping broken slab review-row package
- Task: `AET-MA-20260629-246`
- Parent package: `KIT_GIA_BloodAxeCaveBrokenSlabRemnants_A01`
- Related review packages: `DOC_GIA_BloodAxeCaveApproachScaleReviewRows_A01` and `DOC_GIA_BloodAxeCaveApproachThresholdRhythmRows_A01`
- Scale dependency: validated `SK_GIA_Base_A01` Giant scale lock
- Faction/theme: Blood Axe Tribe, hostile Giant sub-faction only
- Status: docs-only planning. No DCC, Unreal actor, validator, capture, startup placement, final cave approval, final visual approval, or implementation target belongs to this scope.

`DOC_GIA_BloodAxeCaveBrokenSlabReviewRows_A01` defines non-shipping comparison rows for broken Blood Axe cave slab remnants. The rows compare slab widths, split-pair stance, red paint density, ash/mud grounding, chock stone restraint, and Giant scale before any source or engine work is selected.

This document is a planning artifact, not a game asset. It supports art-direction review only and does not approve source creation, mesh creation, material creation, placement, validator work, final visual signoff, cave signoff, or first implementation sequencing.

Blood Axe visual language remains a hostile Giant sub-faction identity. It must stay separate from neutral/civilized Giant culture, which remains tied to hidden highland settlements, skilled stonework, cave-town terraces, waterworks, hearth warmth, monumental civic masonry, and restrained blue-gray stone language.

## Gameplay Purpose

The purpose is visual comparison only. These rows help later reviewers judge whether broken slab remnants feel Giant-scaled, hostile, restrained, and readable without defining gameplay function.

Allowed planning uses:

- Compare broad slab width variants against locked Giant baselines.
- Compare split-pair stance options without implying a doorway, route lane, or blocker.
- Compare chipped red paint density before it becomes a UI cue, objective cue, route marker, readable symbol, or dominant material.
- Compare ash/mud grounding so slabs feel seated in cave-edge grit without becoming trigger zones or terrain-integration proof.
- Compare small chock stone restraint so wedge stones support slab massing without becoming climb assists, cover pieces, or physics props.
- Preserve Blood Axe hostile sub-faction language without replacing neutral/civilized Giant culture.

Out of scope:

- Cave gameplay, traversal proof, path-width rules, route validation, nav/pathfinding, quest/UI markers, encounter triggers, objective markers, interaction behavior, readable signage, spawn logic, patrol logic, combat cover, damage/aura behavior, VFX/audio, source asset creation, DCC, FBX, Unreal actor work, startup placement, validator creation, capture automation, final cave approval, final visual approval, or implementation target selection.

## Silhouette Notes

Review rows should isolate one comparison problem at a time. They should use broad slab silhouettes and simple row spacing rather than dense scene compositions.

Row silhouette families:

- Slab width row: compare narrow, standard, broad, and oversized broken slab reads. The standard read should favor one or two dominant slabs rather than many small fragments.
- Split-pair stance row: compare close offset, staggered offset, wide offset, and rejected gate-like alignment. The row must never frame a functional doorway or path rule.
- Red paint density row: compare no paint, restrained paint, strong but acceptable paint, and overpainted reject. Paint is chipped visual history only.
- Ash/mud grounding row: compare dry contact, restrained ash lip, standard ash/mud seat, heavy burial, and rejected circular zone read.
- Chock stone restraint row: compare no chocks, two to four sparse chocks, heavy chock clutter, and rejected climb/cover read.
- Giant scale row: compare selected slab reads beside female 442 cm and male 470 cm Giant baselines.

Avoid polished civic stonework, symmetrical monument gateways, refined cave-town masonry, warm neutral settlement cues, blue rune identity, route arrows, readable text, objective icons, magic glyphs, dense trophy clutter, graphic gore, and micro-detail that would not survive mid-poly MMO production.

## Scale Notes

Use the validated Giant scale lock exactly:

- Female Giant baseline: 442 cm / 14'6".
- Male Giant baseline: 470 cm / 15'5".
- Approved Giant ranges: females 14-15 ft / 427-457 cm and males 14'10"-16'0" / 452-488 cm.
- These rows must not alter race scale, skeleton policy, collision capsules, sockets, proportions, or character baselines.

Non-shipping broken slab review-row register:

| Row ID | Review focus | Variants | Scale beside Giant baselines | Planning notes |
| --- | --- | --- | --- | --- |
| `BrokenSlabRow_Width_A01` | Slab widths | 160 cm, 280 cm, 420 cm, and 560 cm dominant width reads; 35-110 cm slab thickness | Show each width beside female 442 cm and male 470 cm baselines | Width is visual massing only, not path width, blocker sizing, traversal clearance, or cave compatibility proof. |
| `BrokenSlabRow_SplitPairStance_A01` | Split-pair stance | Close offset pair, staggered pair, wide broken pair, and rejected gate-like pair | Show total pair span and inner negative space beside both Giant baselines | Negative space is composition only, not a route lane, doorway, nav gap, or player passage rule. |
| `BrokenSlabRow_RedPaintDensity_A01` | Red paint density | 0 percent, 5 percent, 10 percent, 18 percent, and overpainted reject | Show paint swipes at Giant-readable scale on broad slab faces | Preferred paint coverage is 5-10 percent of visible slab surface; overpainted rows are rejection references. |
| `BrokenSlabRow_AshMudGrounding_A01` | Ash/mud grounding | Dry contact, thin ash lip, standard ash/mud seat, heavy burial, and rejected circular zone | Show ground contact against slab thickness and Giant feet scale | Grounding is visual seating only, not terrain proof, trigger area, aura, damage field, or navigation surface. |
| `BrokenSlabRow_ChockStoneRestraint_A01` | Chock stone restraint | No chocks, two sparse chocks, four sparse chocks, cluttered chocks, and rejected climb/cover read | Show chock stones at 30-120 cm tall beside Giant baselines | Chocks are accent stones only and must not imply climb assists, cover rules, physics props, or interaction targets. |
| `BrokenSlabRow_GiantScale_A01` | Giant scale comparison | Primary slab, split pair, painted slab, ash-grounded slab, and chock restraint example | Show female 442 cm and male 470 cm baselines consistently at row start | Scale review is non-shipping and does not certify collision, camera, cave placement, or final visual approval. |

All dimensions are visual planning values only. They are not cave gameplay measurements, traversal proof, collision correctness claims, encounter spacing, trigger sizes, interaction ranges, camera approval metrics, terrain integration values, or final cave approval metrics.

## Materials and Color Palette

Primary materials:

- Rough highland stone, fractured cave-edge slabs, ash-stained field rock, dark granite, soot-blackened recesses, and chipped threshold stone.
- Packed mud, trampled earth, cold ash, charcoal dust, cave grit, dry stone dust, muted lichen, and eroded threshold dirt.
- Chipped oxide red paint, dirty maroon swipes, soot-darkened red residue, and old Blood Axe warning marks used sparingly.
- Rope residue, rawhide, scorched leather scraps, sparse blackened iron, old horn chips, and dull bone tokens only as secondary hostile cues.

Palette targets:

- Dominant: charcoal gray, dark stone gray, ash gray, cave black, weathered slate, mud brown, and cold dust.
- Blood Axe accent: oxide red, faded maroon, dirty red, and chipped dark red-brown in restrained beats.
- Secondary accent: rawhide tan, old horn tan, dull bone ivory, rubbed dark iron, and muted lichen green.
- Emissive: absent. No glow, ritual light, shamanic pulse, signal light, torch state, UI highlight, objective highlight, or animated material state belongs to this package.

Material ratio guidance:

- Stone, soot, ash, cave grit, and mud should carry 80-90 percent of the visual read.
- Chipped red paint should usually stay within 5-10 percent of visible slab surface.
- Rope, rawhide, iron, horn, and bone should remain sparse secondary accents.
- Neutral/civilized Giant material language must not become the default Blood Axe read.

## Concept Image Prompt

Create an original stylized fantasy MMORPG documentation planning board of `DOC_GIA_BloodAxeCaveBrokenSlabReviewRows_A01` for the world of Aerathea. The design should emphasize non-shipping review rows for Blood Axe cave broken slab remnants, slab width comparison, split-pair stance comparison, chipped red paint density comparison, ash and mud grounding comparison, sparse chock stone restraint, rough highland stone, soot-blackened cave-edge slabs, cold ash, trampled mud, cave grit, hostile Giant sub-faction identity, strict separation from neutral/civilized Giant culture, and validated Giant scale with a female 442 cm / 14'6" baseline and male 470 cm / 15'5" baseline. Use hand-painted texture detail only in planning swatches, readable shapes, baked-AO-style depth, normal-map-style surface detail, no emissive glow, and MMO-friendly production design. Present it as a clean docs-only comparison sheet with row labels, scale callouts, material restraint notes, rejection examples, and stop gates on a neutral background. Avoid copying any existing franchise, avoid cave gameplay diagrams, avoid traversal proof, avoid collision correctness claims, avoid nav/pathfinding diagrams, avoid quest/UI markers, avoid encounter triggers, avoid objective markers, avoid route validation, avoid readable route text, avoid UI arrows, avoid magic glyphs, avoid VFX/audio, avoid DCC or FBX claims, avoid Unreal implementation claims, avoid startup placement, avoid final approval language, avoid selecting a first implementation target, avoid neutral Giant cave-town architecture as Blood Axe default language, avoid graphic gore, and avoid excessive micro-detail that would not translate to mid-poly assets.

## Modeling Notes

This is a docs-only review-row plan. No source folder, Blender file, mesh, sculpt, retopo, UV, bake, proof render, LOD source, collision proxy, FBX export, Unreal asset, material instance, texture asset, material graph, validator, runtime source, Blueprint, socket, animation, startup placement, implementation target, cave signoff, or visual signoff is created or authorized.

Review rows should remain document-level comparisons:

- Slab width row: use simple dominant slab silhouettes with clear width labels.
- Split-pair stance row: show the same two slab pieces in close, staggered, wide, and rejected gate-like stances.
- Red paint density row: use the same slab silhouette with increasing chipped paint coverage so restraint is easy to judge.
- Ash/mud grounding row: show contact buildup from dry to heavy burial, with the rejected row clearly reading as too circular or gameplay-zone-like.
- Chock stone restraint row: show sparse wedge stones supporting the slab read, then a rejected cluttered or climb-like arrangement.
- Giant scale row: repeat the strongest acceptable examples beside the female 442 cm and male 470 cm baselines.

If later art-direction work creates a visual sheet, keep rows flat, clearly non-shipping, and limited to broad silhouettes. Do not model new assets, construct review geometry, author collision, create validators, place actors, or select a first production item from this package.

## Texture and Material Notes

This package creates no textures, materials, material instances, texture atlases, masks, or material graphs.

If a later separately scoped art sheet uses material swatches, keep them aligned with the existing Blood Axe cave approach family:

- Base Color / Albedo (`BC`) should carry dark stone, soot, ash, mud, cave grit, chipped oxide red paint, rawhide, rope, sparse blackened iron, old horn, and dull bone.
- Normal (`N`) should describe broad stone planes, large slab breaks, ash/mud grounding, coarse stone pitting, chipped paint edges, and large wedge-stone contact.
- Packed Occlusion/Roughness/Metallic (`ORM`) should emphasize contact shadows under slabs, chocks, mud buildup, soot pockets, and stone occlusion.
- Emissive (`E`) is not part of this package.

No unique material should be created for each row, slab face, paint mark, ash patch, mud smear, chock stone, rope tie, horn chip, bone token, lichen fleck, or crack. Fine cracks, soot speckles, ash flecks, chipped paint, stone pitting, lichen, mud streaks, grit, and small scratches remain texture or normal-map concerns for future child assets only.

## Triangle Budget

This package creates no mesh and has no shipping triangle budget.

Reference budgets for future child assets remain owned by their packages:

- Single major broken slab: 1.2k-4k tris at LOD0, 1 material target.
- Primary broken slab cluster: 4k-12k tris total at LOD0, 1-2 material target.
- Split slab pair: 3k-9k tris total at LOD0, 1 material target.
- Ash-grounded slab: 2.5k-8k tris total at LOD0, 1-2 material target.
- Painted slab: 1.5k-5k tris at LOD0, 1-2 material target.
- Small chock stone set: 500-2.5k tris total at LOD0, usually included in a slab module.
- Non-shipping review row visual sheet: no mesh by default; if a separate task creates simple row geometry, keep it to simple blockout silhouettes only and do not treat it as a shipping asset.

Any future geometry budget should spend triangles on primary slab mass, broad slab thickness, major split faces, large chipped corners, ash/mud grounding forms, and sparse chock stones. Do not spend triangles on tiny cracks, soot speckles, ash flecks, paint chips, lichen, mud flecks, grit, small scratches, or repeated small tokens.

## LOD Plan

This package creates no LOD source. LOD guidance here is a review-row reminder for future child assets only.

- LOD0: preserve full broken slab massing, slab width read, split-pair stance, broad chipped faces, ash/mud grounding, sparse chock stones, and restrained red paint beat.
- LOD1: preserve the main row composition while reducing small bevels, secondary chips, minor paint-edge cuts, small chock bevels, hidden back-facing detail, and minor ash/mud undercuts.
- LOD2: preserve big massing only: dominant slab width, split-pair offset, low cave-edge grounding, and one restrained red accent where needed.
- LOD3: preserve the broken threshold read only: broad slab silhouette, low dark grounding, and minimal Blood Axe color cue where needed.

Reduction order for future child assets:

1. Remove tiny cracks, soot speckles, ash flecks, lichen specks, paint chips, grit dots, and minor scratches.
2. Remove small chock chips, tiny stone wedges, horn chips, bone pores, minor iron nicks, and shallow mud crumbs.
3. Reduce back-facing stones, hidden underside bevels, buried contact cuts, and non-visible ash/mud undercuts.
4. Reduce secondary slab scars, duplicate foot stones, small paint islands, and optional review-row helper detail.
5. Reduce stone bevel density, slab edge cuts, ash/mud ridge geometry, and secondary base-plane subdivisions.
6. Only after small detail is gone, simplify the primary slab width, split-pair stance, painted slab read, or ash-grounded silhouette.

Never reduce Giant-scale readability, Blood Axe hostile sub-faction read, static cave-edge memory, slab massing, or primary silhouette before removing small detail.

## Collision Notes

Collision is out of scope for this docs-only review-row package. Do not create collision proxies, UCX meshes, engine settings, physics bodies, nav blockers, smart links, gameplay volumes, trigger volumes, damage volumes, aura volumes, objective volumes, interaction volumes, validator scripts, or runtime setup from this package.

Review-row collision policy:

- Documentation rows: collision not applicable.
- Any future visual sheet rows: collision disabled.
- Paint, ash, mud, cave grit, lichen, rope residue, horn chips, bone tokens, and small accents: collision disabled in future child assets unless a separate package changes the scope.
- Large stone bodies: collision planning remains owned by the relevant future child asset package and must not be certified here.

This package makes no claim of collision correctness, cave compatibility, pathing validity, traversal clearance, player movement validity, combat cover, route blocking, camera clearance, objective-zone behavior, interaction behavior, terrain blending, runtime performance validation, or nav/pathfinding validity.

## Animation Notes

The review rows are static documentation.

Allowed at planning level:

- Static slab width comparisons.
- Static split-pair stance comparisons.
- Static red paint density comparisons.
- Static ash/mud grounding comparisons.
- Static chock stone restraint comparisons.
- Static Giant scale comparison rows.

Not part of this package:

- Physics collapse, destructible breakage, moving slabs, falling stones, cloth simulation, wind sway, torch states, material pulse, glow, particles, VFX, audio, Blueprint state, interaction state, quest state, objective state, encounter state, damage state, aura state, cave gameplay state, nav/pathfinding behavior, startup placement, or runtime behavior.

Any moving, glowing, interactive, objective-readable, UI-readable, audio-linked, damaging, route-affecting, or gameplay-readable variant needs a separately named package and explicit scope.

## Unreal Import Notes

This section is future guardrail planning only. No Unreal asset, game folder, import script, material instance, texture asset, socket, Blueprint, validator, runtime source, review actor, startup actor, source asset, DCC work, FBX export, cave placement, collision setup, nav/pathfinding setup, trigger setup, objective setup, quest/UI setup, interaction setup, VFX/audio setup, or first implementation target is created or authorized.

Potential future identity after separate lead authorization:

- Asset name: `DOC_GIA_BloodAxeCaveBrokenSlabReviewRows_A01`
- Asset type: Documentation-only non-shipping broken slab review-row package
- Game asset status: none selected and none created
- Pivot guidance: not applicable to the documentation package
- Orientation guidance: not applicable to the documentation package
- Scale reference: female Giant 442 cm / 14'6" and male Giant 470 cm / 15'5"; approved Giant ranges remain females 14-15 ft / 427-457 cm and males 14'10"-16'0" / 452-488 cm
- Collision type: not applicable; no collision is created or validated
- LOD plan: planning reference only; no LOD source is created
- Material slot count: not applicable; no material is created
- Texture list: not applicable; no texture is created
- Sockets: none
- Animation list: none
- Blueprint behavior: none
- Performance notes: use the document to prevent slab-width overreach, split-pair doorway drift, red paint overuse, ash/mud trigger-zone reads, chock clutter, unnecessary material splits, collision overreach, and gameplay-readable marker drift in later packages.

No folder path in game content is selected by this docs-only package.

## Folder and Naming Recommendation

Documentation path:

- `docs/assets/kits/DOC_GIA_BloodAxeCaveBrokenSlabReviewRows_A01/PRODUCTION_PACKAGE.md`

Review-row identifiers:

- `BrokenSlabRow_Width_A01`
- `BrokenSlabRow_SplitPairStance_A01`
- `BrokenSlabRow_RedPaintDensity_A01`
- `BrokenSlabRow_AshMudGrounding_A01`
- `BrokenSlabRow_ChockStoneRestraint_A01`
- `BrokenSlabRow_GiantScale_A01`

Related source-of-truth packages:

- `KIT_GIA_BloodAxeCaveBrokenSlabRemnants_A01`
- `DOC_GIA_BloodAxeCaveApproachScaleReviewRows_A01`
- `DOC_GIA_BloodAxeCaveApproachThresholdRhythmRows_A01`
- `SK_GIA_Base_A01` for Giant scale lock

Do not create or edit source asset folders, DCC files, FBX exports, Unreal game content folders, material graphs, material instances, texture assets, validators, global indexes, backlog docs, task-board docs, bootstrap docs, startup placement, external source concept files, runtime source files, VFX assets, audio assets, or unrelated package files from this task.

## Quality Gate Checklist

- Required universal package headings are present in order for a docs-only review-row package.
- Package is limited to `docs/assets/kits/DOC_GIA_BloodAxeCaveBrokenSlabReviewRows_A01/PRODUCTION_PACKAGE.md`.
- Package is non-shipping and does not create a mesh, source asset, material instance, texture asset, validator, runtime source, Unreal asset, startup placement, approval artifact, or first implementation target.
- Review rows compare slab widths, split-pair stance, red paint density, ash/mud grounding, chock stone restraint, and Giant scale.
- Slab width values are visual massing only and do not define path width, blocker sizing, traversal clearance, cave compatibility proof, or placement approval.
- Split-pair stance remains composition-only and does not define a doorway, route lane, nav gap, route blocker, or traversal rule.
- Red paint density remains restrained, with 5-10 percent as the preferred visible surface target and overpainted rows treated as rejection references.
- Ash/mud grounding remains visual seating and does not become a trigger zone, aura, damage field, terrain proof, or navigation surface.
- Chock stones remain sparse accent stones and never become climb assists, cover rules, physics props, or interaction targets.
- Giant scale lock is explicit: female 442 cm / 14'6" baseline and male 470 cm / 15'5" baseline.
- Approved Giant ranges are explicit: females 14-15 ft / 427-457 cm and males 14'10"-16'0" / 452-488 cm.
- Blood Axe remains a hostile Giant sub-faction and does not replace neutral/civilized Giant culture.
- Neutral/civilized Giant culture remains separate: hidden highland settlements, skilled stonework, cave-town terraces, waterworks, hearth warmth, monumental civic masonry, and restrained blue-gray stone language.
- Review rows use rough stone, soot, ash, trampled mud, cave grit, chipped red paint, rope, rawhide, sparse blackened iron, old horn, and dull bone without default emissive.
- No cave gameplay, traversal proof, collision correctness, nav/pathfinding, quest/UI marker, encounter trigger, objective marker, readable signage, VFX/audio, DCC, FBX, Unreal, source asset creation, startup placement, validator work, capture work, final cave approval, final visual approval, or first implementation target is defined.
- Fine cracks, soot speckles, ash flecks, stone pitting, chipped paint, lichen, mud streaks, grit, and small scratches are assigned to future textures or normals, not modeled review-row detail.
- LOD0-LOD3 guidance, no-collision guardrails, animation limits, import-planning guardrails, folder naming, and stop gates are included without claiming shipping readiness.
