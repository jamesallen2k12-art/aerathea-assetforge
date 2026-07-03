# SM_GIA_BloodAxeLongbow_A02 Production Package

## Art Direction Summary

- Asset name: `SM_GIA_BloodAxeLongbow_A02`
- Asset type: Static Mesh weapon / Giant longbow
- Parent kit: `KIT_GIA_BloodAxeArmory_A01`
- Source intake child ID: `BloodAxeArmory.png#Bow_Longbow_02`
- Faction/theme: Blood Axe Tribe, hostile Giant sub-faction
- Variant role: cleaner wrapped-stave common archer variant
- Status: docs-only production package ready; DCC build not started

`SM_GIA_BloodAxeLongbow_A02` is the common Blood Axe Giant archer longbow: a clean, readable wrapped stave with a large central grip, restrained metal reinforcement, clear nocks, and enough hostile raider material language to identify the Blood Axe Tribe without turning the bow into a trophy-heavy hero weapon. It should feel field-made and brutal, but practical for many Giant archers.

Variant distinction is mandatory: `SM_GIA_BloodAxeLongbow_A01` is the larger first longbow with heavier trophy binding, `SM_GIA_BloodAxeLongbow_A02` is the cleaner wrapped-stave common archer bow, and `SM_GIA_BloodAxeLongbow_A03` is reserved for a heavier battle-scarred red-wrap variant with stronger silhouette breaks. Do not copy A01's trophy density, and do not pre-empt A03's heavier battle-damaged language.

Blood Axe is a hostile Giant sub-faction only. This bow must not overwrite neutral or civilized Giant culture, which remains associated with highland stonework, cave towns, masonry craft, warm hearth language, and restrained blue rune motifs in separate packages.

Docs-only guardrails: this package creates no DCC source, Blender file, FBX export, Unreal Content asset, runtime source, projectile behavior, animation timing, combat stats, source concept copy, startup-scene placement, validator, or final visual approval.

## Gameplay Purpose

This asset supports future Blood Axe Giant archer NPCs, camp sentries, hunters, patrol silhouettes, rack dressing, loot display, and armory scale reference. It is intended as the repeatable/common longbow that can appear on multiple hostile Giant archers without implying a named hero, chieftain, or boss variant.

Expected use cases:

- Equipped two-handed ranged weapon for common Blood Axe Giant archers.
- Rack, wall, ground, or bowyer-bench display prop in Blood Axe camps.
- Scale reference for `KIT_GIA_BloodAxeQuivers_A01` arrows and carry clearance.
- Support relationship for `KIT_GIA_BloodAxeBowParts_A01` nocks, replacement limbs, strings, and stave blanks.
- Socket planning reference for Giant hand, back carry, string pull, and arrow nock alignment.

Out of scope: final projectile gameplay, damage values, charge behavior, hit logic, arrow flight, ammunition rules, inventory behavior, pickup behavior, draw distance, release timing, animation montage timing, combat traces, and final visual approval.

## Silhouette Notes

Primary silhouette: a tall Giant-scale longbow with a smooth but hand-shaped stave arc, broad wrapped center grip, visible string line, readable upper and lower nocks, and a few practical binding bands. The first read should be the clean stave and grip, not trophies, spikes, skull clusters, or heavy battle damage.

Readable A02 features:

- Clear uninterrupted bow arc for MMO camera distance.
- Large central leather wrap sized for Giant hands.
- Slightly asymmetric hand-carved stave profile without jagged A03-style breaks.
- Restrained blackened iron or horn reinforcement at the tips and grip.
- Readable nock grooves at both ends, large enough to understand string attachment.
- One or two red cloth ties or dull red painted marks as faction identifiers.
- Minimal trophy language: optional single bone tag or tooth charm only, never a skull cluster.

Avoid:

- A01's larger trophy-bound hero read.
- A03's heavier red-wrap battle-scarred silhouette breaks.
- Elven elegance, civilized Giant blue-gray stoneworker motifs, shamanic glow, dense rivets, tiny lashings, repeated skulls, graphic gore, or micro-detail forests.

## Scale Notes

Use the validated Giant scale lock exactly:

- Female Giant baseline: 442 cm / 14'6".
- Male Giant baseline: 470 cm / 15'5".
- Approved Giant range lock: female Giants 14-15 ft / 427-457 cm; male Giants 14'10"-16'0" / 452-488 cm.
- Author in centimeters. 1 Unreal unit = 1 cm.
- Normal humanoid compatibility is not required.

Target proportions for A02:

- Resting bow height: 390-435 cm from lower nock to upper nock.
- Stave thickness: 10-18 cm through most limb sections, thicker at grip and reinforced tips.
- Grip height: 48-62 cm to read clearly in a Giant hand with wrapped leather layers.
- Grip diameter/depth: 16-24 cm depending on hand fit and wrap thickness.
- Tip/nock assembly: 26-40 cm long per end, with simple readable string grooves.
- Resting string line: clean and visible, offset enough to read from front and three-quarter views.
- Back carry envelope: must clear Giant shoulders, head, hair, trophy armor, and `back_quiver` placement.
- Quiver dependency: arrow length, arrow count, fletching mass, and draw-from-quiver clearance remain owned by `KIT_GIA_BloodAxeQuivers_A01`.

The A02 bow should be slightly less monumental and less trophy-heavy than A01, while still clearly too large for normal humanoids. It should also avoid the bulkier, more broken A03 profile reserved for a future heavy variant.

## Materials and Color Palette

Primary materials:

- Dark highland hardwood or laminated stave wood in gray-brown, dark umber, soot-stained ochre, and rubbed raw-wood edge tones.
- Scorched leather grip wrap with broad hand-painted folds.
- Sinew, rawhide, or heavy cord binding at the grip and nocks.
- Horn, bone, or blackened iron caps for the nock assemblies.
- Restrained blackened iron or dark steel reinforcement plates at high-stress points.
- Dull red cloth ties or red war-paint marks as Blood Axe identifiers.
- Soot, ash, grime, rubbed edges, minor chips, and broad use wear.

Palette control:

- Keep red accents limited to ties, small painted marks, and one or two wrap bands.
- Keep metal reinforcement secondary to the wooden stave silhouette.
- Use bone/horn as practical nock material or a single tag, not as a trophy covering.
- No baseline emissive map, magical glow, blue runes, warm neutral Giant hearth language, or civilized Giant stoneworker ornament.

## Concept Image Prompt

Create an original stylized fantasy MMORPG concept image of `SM_GIA_BloodAxeLongbow_A02` for the world of Aerathea. The design should emphasize a cleaner Giant-scale wrapped-stave longbow, a clear continuous stave silhouette, large scorched-leather center grip, restrained blackened iron and horn nock reinforcement, readable upper and lower nocks, heavy sinew string anchors, sparse red Blood Axe cloth markers, minimal trophy detail, hostile Giant common archer identity, practical raider bowyer construction, and future ranged weapon support role. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, sparing or no emissive accents, and MMO-friendly production design. Present it as a production asset sheet with front, side, three-quarter, grip detail, nock detail, string anchor detail, back-carry clearance sketch, quiver dependency note, and scale callouts against female baseline 442 cm / 14'6" and male baseline 470 cm / 15'5" Giants on a clean background. Avoid copying any existing franchise, avoid making Blood Axe language the default Giant culture, avoid graphic gore, avoid A01 trophy density, avoid A03 heavy battle-scar red-wrap language, avoid readable text, and avoid excessive micro-detail that would not translate to a mid-poly Unreal asset.

## Modeling Notes

This package is documentation only. Future DCC work should model the major functional forms and leave small wear to textures or normals.

Model real geometry for:

- Continuous curved longbow stave with a clean but hand-shaped silhouette.
- Large central grip with broad leather wrap bands and raised palm stops.
- Upper and lower nock caps with visible string grooves.
- Simple top and bottom string anchor shapes.
- Rest-position string as a clean thin mesh or separate future string subpiece.
- Restrained grip and tip reinforcement plates.
- A few large wrap bands, lash points, and red cloth tie forms.
- Optional single bone/tooth tag, placed away from the grip, nocks, and string readability.
- Back-carry attachment marker or simple loop fitting if needed for future review.

Use texture and normal maps for:

- Wood grain, small stave cracks, rubbed edges, scratches, pitting, soot streaks, leather pores, stitch lines, sinew fibers, small chips, tiny hammer marks, and minor red paint wear.

Do not model:

- Dense rivet rows, tiny knots, hundreds of lashings, individual string fibers, repeated skulls, fine cracks, dense stitch marks, per-thread wrap ridges, A01 trophy clusters, or A03 heavy broken limb chunks.

Fit notes:

- Pivot and grip center must align to a Giant bow hand; left-hand grip is the default review assumption.
- Arrow rest and nock reference must leave enough visual space for Giant arrows from `KIT_GIA_BloodAxeQuivers_A01`.
- String pull, arrow rest, and back-carry points are planning references only and do not define animation timing or projectile behavior.

## Texture and Material Notes

Texture set target: 2K baseline. Use 4K only if a later named hero or boss archer variant explicitly approves it; A02 is a common archer asset and should not require 4K by default.

Required texture names:

- `T_GIA_BloodAxeLongbow_A02_BC`
- `T_GIA_BloodAxeLongbow_A02_N`
- `T_GIA_BloodAxeLongbow_A02_ORM`

Optional texture name:

- `T_GIA_BloodAxeLongbow_A02_E` only for a separately approved ritual or shamanic variant; no emissive is planned for this baseline.

Material instance:

- `MI_GIA_BloodAxeLongbow_A02`

Material slot target:

- 1 material slot preferred for the full bow.
- 2 material slots maximum if future DCC work separates string/leather from stave/metal.
- Do not create separate slots for every wrap, tag, nock, tie, or reinforcement plate.

Packed ORM guidance:

- Strong AO under grip wraps, nock caps, and binding bands.
- High roughness on wood, leather, sinew, bone, horn, and red cloth.
- Restrained metallic response on blackened iron reinforcement only.
- No glow for red faction marks.

## Triangle Budget

- LOD0 target: 4k-6.5k tris.
- LOD0 hard cap: 7.5k tris if the grip, nocks, string, and reinforcement require extra silhouette support.
- Material slots: 1 target, 2 maximum.
- Texture set: 2K baseline.

Budget priorities:

- Spend geometry on the stave arc, grip mass, nock shape, string line, major wrap bands, and restrained reinforcement.
- Keep A02 cheaper and cleaner than A01 by limiting trophies and secondary fittings.
- Do not spend geometry on tiny rivets, thread fibers, scratch patterns, dense binding wraps, small knots, or repeated trophy details.

## LOD Plan

All production variants need LOD0-LOD3.

- LOD0: full clean stave arc, large grip, wrap forms, readable nocks, string line, restrained reinforcement plates, simple red tie accents, and optional single tag.
- LOD1: 60-70 percent of LOD0; simplify wrap bevels, metal plate bevels, minor nock cuts, small cloth folds, and tag bevels.
- LOD2: 35-45 percent of LOD0; reduce tip cap geometry, merge small fittings, simplify string support, flatten secondary wrap bands, and remove optional tag detail if needed.
- LOD3: 15-25 percent of LOD0; preserve bow arc, grip block, nock endpoints, string line, and red faction color blocks.

Reduce details in this order: tiny scratches and rivets, stitch marks, small cloth tears, secondary wrap cuts, minor chips, optional tag bevels, back-side fittings, reinforcement plate bevels, then nock bevels. Never reduce the main bow arc, grip mass, nock endpoints, or string line before removing small detail.

## Collision Notes

Equipped baseline collision should be disabled. Combat traces, projectile collision, hit detection, and damage volumes are future gameplay-system work and are not defined in this package.

Display or pickup variants may use simple collision:

- One long capsule or narrow box following the bow height.
- One small box around the grip only if pickup focus requires it.
- No per-string collision.
- No per-wrap, per-tag, per-nock, or per-reinforcement collision.
- No arrow, projectile, damage, or combat collision in this package.

Back-carry review should rely on character attachment bounds or a simple non-blocking preview volume. The bow must not create blocking collision that catches on Giant armor, quivers, or camp props.

## Animation Notes

Static mesh baseline. This package does not author animations, string deformation, draw distance, release timing, reload timing, projectile spawn behavior, combat montage rules, or animation timing.

Future animation and socket planning notes:

- Bow grip should align to Giant hand sockets, defaulting to left-hand grip review.
- Arrow rest and nock reference should be visibly clear near the grip and string line.
- String pull reference may be documented as a locator in future DCC, but timing and deformation are not part of this task.
- Top and bottom string anchors must be clear enough for a future swapped or rigged string plan.
- Back carry should support `back_large_weapon` or a future bow-specific back socket without clipping Giant shoulders, hair, trophy armor, or `back_quiver`.
- Quiver clearance remains dependent on `KIT_GIA_BloodAxeQuivers_A01`.

## Unreal Import Notes

These are planned future import notes only. This task does not perform Unreal import, create Unreal Content assets, create DCC source, export FBX files, add runtime source, place startup-scene actors, or create validators.

- Planned Unreal path: `/Game/Aerathea/Weapons/Giants/BloodAxe/SM_GIA_BloodAxeLongbow_A02`
- Planned asset type: Static Mesh
- Import scale: 1.0 after future DCC/export approval; authored in centimeters
- Pivot: center of the main bow grip
- Forward/orientation: align to the project weapon convention during future DCC handoff; document any deviation before import
- Collision: disabled for equipped use; simple display collision only if a pickup/display variant is approved
- Material slots: 1 target, 2 maximum
- LODs: LOD0, LOD1, LOD2, LOD3 required
- Performance note: A02 should remain the cleaner common archer bow; preserve the stave arc and nocks at distance while keeping trophies and heavy damage off this variant

Recommended mesh sockets/locators for future import planning:

- `socket_bow_grip`
- `socket_arrow_rest`
- `socket_arrow_nock`
- `socket_string_top`
- `socket_string_bottom`
- `socket_string_pull_ref`
- `socket_back_carry_attach`
- `socket_quiver_alignment_ref`

Expected character-side socket dependencies:

- `hand_l_offhand` or future `bow_grip_l`
- `bow_string_pull_r`
- `arrow_nock`
- `back_large_weapon`
- `back_quiver`

These names are planning references only. Final socket naming, projectile spawn rules, combat traces, animation timing, and visual approval require separate future tasks.

## Folder and Naming Recommendation

- Docs folder: `docs/assets/props/SM_GIA_BloodAxeLongbow_A02/`
- Production package: `docs/assets/props/SM_GIA_BloodAxeLongbow_A02/PRODUCTION_PACKAGE.md`
- Planned Unreal folder after approval: `/Game/Aerathea/Weapons/Giants/BloodAxe/`
- Planned mesh name: `SM_GIA_BloodAxeLongbow_A02`
- Planned material instance: `MI_GIA_BloodAxeLongbow_A02`
- Planned textures: `T_GIA_BloodAxeLongbow_A02_BC`, `T_GIA_BloodAxeLongbow_A02_N`, `T_GIA_BloodAxeLongbow_A02_ORM`

DCC source folders, FBX export folders, Unreal Content assets, runtime source, startup-scene placement, external concept storage, source concept copying, final visual approval, validators, task-board updates, backlog edits, bootstrap edits, and global index edits are intentionally out of scope for this docs-only task.

## Approval Gates

- Stop before DCC mesh creation, Blender source creation, FBX export, Unreal Content import, material authoring, runtime source changes, startup-scene placement, validator creation, or final visual approval.
- Stop before copying, moving, editing, embedding, or committing the external source concept.
- Stop if the bow appears sized for normal humanoids instead of the Giant scale lock.
- Stop if Blood Axe raider language begins to overwrite neutral/civilized Giant culture.
- Stop if A02 starts duplicating A01's trophy-heavy first longbow read.
- Stop if A02 starts duplicating A03's future heavy battle-scarred red-wrap read.
- Stop if trophies, skulls, gore, rivets, lashings, strings, or scratches become dense enough to hurt mid-poly readability.
- Stop before defining projectile gameplay, combat stats, combat traces, hit behavior, arrow inventory rules, draw distance, draw timing, release timing, reload timing, or animation montage timing.
- Stop before final bow approval if quiver clearance, arrow scale, and draw-from-quiver dependency have not been resolved by future work.

## Quality Gate Checklist

- Blood Axe remains a hostile Giant sub-faction separate from neutral/civilized Giant culture.
- Giant scale lock is explicit: female baseline 442 cm / 14'6", male baseline 470 cm / 15'5", approved range female Giants 14-15 ft / 427-457 cm and male Giants 14'10"-16'0" / 452-488 cm.
- A02 variant reads as the cleaner wrapped-stave common archer bow.
- A02 does not duplicate A01's heavier trophy-bound first longbow identity.
- A02 does not duplicate A03's future heavier battle-scarred red-wrap identity.
- Clear stave silhouette, large wrapped grip, restrained metal reinforcement, readable nocks, and MMO-safe mid-poly planning are included.
- Bow height, grip, nock, string anchor, draw reference, back carry, and quiver dependency notes are included.
- Final projectile behavior, combat stats, combat traces, and animation timing are explicitly out of scope.
- Primary silhouette reads as a massive Giant longbow at MMO camera distance.
- Materials use dark hardwood, scorched leather, sinew/rawhide, blackened iron, horn/bone, soot, grime, and restrained dark red Blood Axe cloth/paint consistently.
- Emissive is absent by default and approval-gated for any future ritual or shamanic variant.
- Tiny rivets, scratches, string fibers, dense lashings, pitting, wood grain, leather pores, stitch marks, and minor chips are assigned to textures or normals instead of geometry.
- Texture maps, material slot limits, triangle budgets, LOD0-LOD3, collision, pivot, socket planning, Unreal import planning, folder naming, approval gates, and docs-only guardrails are included.
- The package makes no DCC, FBX, Unreal Content, runtime source, global index, task board, external concept copy, startup-scene placement, projectile behavior, animation timing, combat stats, or final visual approval claim.
