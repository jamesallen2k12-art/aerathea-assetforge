## Art Direction Summary

- Asset name: `SM_GIA_BloodAxeApproachCliffLedgeCap_A01`
- Asset type: Static Mesh production package / docs-only local cliff ledge cap planning
- Task: `AET-MA-20260629-147`
- Parent kit: `KIT_GIA_BloodAxeStrongholdApproach_A01`
- Parent route: `KIT_GIA_BloodAxeCamp_A01#Gate_StrongholdApproach`
- Source child ID: `BloodAxeStronghold.png#Cliffs_LedgeCaps`
- Related planning references: `KIT_GIA_BloodAxeStrongholdApproach_A01`, `KIT_GIA_BloodAxeApproachCliffWalls_A01`, `SM_GIA_BloodAxePackedEarthPath_A01`, and future switchback approach rows
- Faction/theme: Blood Axe Tribe, hostile Giant sub-faction only
- Status: docs-only production package ready for planning review

`SM_GIA_BloodAxeApproachCliffLedgeCap_A01` defines local ledge caps, rubble shelves, rock lips, and shelf-edge silhouettes for the hostile Blood Axe stronghold approach. The asset should help future switchback compositions feel physically massive and dangerous at Giant scale without becoming a terrain system, climb route, walkable path proof, or final environment implementation.

Blood Axe visual language must stay separate from neutral/civilized Giant culture. This package uses hostile raider approach materials such as fractured dark rock, mud, soot, ash, chipped oxide red marks, blackened debris, and rough field damage. It must not replace neutral/civilized Giant identity, which remains tied to highland cave towns, master stonework, blue-gray masonry, terraces, waterworks, warm hearth light, restrained blue runes, and civic stoneworker craft.

This package does not create or authorize DCC source, FBX, Unreal Content, runtime source, source concept movement, startup placement, final visual approval, first implementation target selection, traversal proof, climb route, nav/pathfinding, walkable collision implementation, or landscape fit validation.

## Gameplay Purpose

The purpose is visual production planning only. The ledge cap gives future Blood Axe stronghold approach compositions a readable cliff-shelf edge, rubble shelf, and rock-lip language around switchbacks and overlooks. It supports scale, silhouette, material, and LOD planning without defining gameplay traversal.

Allowed planning purpose:

- Frame switchback edges, cliff shelves, overlook bases, and approach pinch silhouettes with local rock-cap modules.
- Give the approach a hostile Blood Axe environmental read through soot-dark stone, mud-packed shelf edges, ash settling, rough rock lips, and sparse red warning marks.
- Show visual scale around Giant-built cliff routes using local ledge caps rather than final terrain or landscape claims.
- Provide future DCC agents with clear form, material, and budget expectations if a later task approves source creation.

Out of scope:

- DCC source, Blender work, terrain sculpt, mesh creation, retopo, UVs, bakes, proof renders, FBX export, Unreal import, material graph authoring, collision proxy creation, custom UCX, runtime source, validators, startup placement, final visual approval, source concept movement, first DCC target selection, first build target selection, traversal proof, climb route, nav/pathfinding, walkable collision implementation, route scripting, encounter scripting, AI patrols, spawn logic, cover rules, objective logic, loot, resource, crafting, economy, VFX, audio, or interaction behavior.

## Silhouette Notes

Primary silhouette: a broad, broken cliff ledge cap with an uneven horizontal shelf top, jagged rock lip, undercut shadow edge, rubble shelf buildup, mud and ash settling zones, and large readable fracture planes. It should read as a local shelf edge or cap module that can visually sit against larger cliff walls and switchback routes, not as a complete terrain tile.

Required silhouette elements:

- One main ledge cap mass with a thick upper shelf and heavy broken front lip.
- Chunky fractured rock planes large enough to read at MMO camera distance.
- A recessed shadow band or undercut below the lip to emphasize height and switchback danger.
- Rubble shelf buildup along one or both ends, using large stones rather than dense gravel.
- Mud-packed top edge, ash-dusted pockets, and compacted dirt settling where a future path might visually meet the ledge.
- Optional blackened scrap, broken shield chip, horn marker, or faded oxide-red cloth scrap only as sparse Blood Axe territory cues.
- Irregular end shapes that can visually overlap cliff wall segments, path strips, or switchback turns without defining snapping behavior.

Model real geometry for the main ledge slab, large rock lip, broad undercut, major fracture planes, shelf thickness, large rubble stones, and any silhouette-critical Blood Axe marker. Use texture, normals, AO, and masks for small cracks, grit, ash speckles, soot stains, tiny chips, mud drying lines, cloth fibers, and minor stone pitting.

Avoid refined masonry, terrace blocks, carved civic Giant symbols, blue rune inlays, warm hearth cues, polished stonework, dense skull clutter, graphic gore, glowing route marks, arrow-like path signs, climb-handhold patterns, nav arrows, UI readability, tiny modeled gravel fields, or a one-piece terrain chunk that obscures the local ledge-cap read.

## Scale Notes

Use the validated `SK_GIA_Base_A01` scale lock exactly:

- Female Giant baseline: 442 cm / 14'6".
- Male Giant baseline: 470 cm / 15'5".
- Approved Giant ranges: females 14-15 ft / 427-457 cm; males 14'10"-16'0" / 452-488 cm.
- Author future source in centimeters. 1 Unreal unit = 1 cm.
- This package does not change Giant race scale, skeleton policy, capsule expectations, body proportions, or character collision assumptions.

Recommended visual planning dimensions:

- Overall ledge cap width: 600-1200 cm.
- Overall ledge cap depth: 350-800 cm.
- Visible shelf thickness: 120-360 cm from top plane to lowest broken lip.
- Main front rock lip height variation: 80-240 cm.
- Undercut shadow band: 60-180 cm deep where visible from the approach.
- Top mud or ash settling strip: 120-320 cm wide, treated as visual material buildup only.
- Rubble shelf stones: 60-220 cm across for primary stones, with smaller rubble represented mostly in texture.
- Edge drop read: tall enough beside a 470 cm male Giant to feel like a dangerous cliff shelf, but not authored here as a traversal value.
- Visual switchback relationship: ledge caps should make wide Giant-scale shelf turns feel massive and constrained, but dimensions are composition guidance only.

All dimensions are planning values. They are not gameplay lane widths, navmesh values, climb metrics, slope rules, step-height rules, pathfinding constraints, collision guarantees, or terrain fit approvals.

## Materials and Color Palette

Primary Blood Axe approach materials:

- Fractured highland rock, dark cliff stone, split shale-like faces, and rough weathered ledge slabs.
- Packed mud, compacted dirt, ash settling, soot staining, charcoal dust, and gravel trapped along shelf edges.
- Sparse blackened iron scrap, broken shield chips, blade fragments, or dark chain scraps only where they support Blood Axe territorial read.
- Optional rough timber splinter, horn marker, or bone marker in very low density and non-graphic presentation.
- Faded oxide-red cloth strip, chipped red paint smear, or maroon warning tie used as a restrained faction accent.

Palette targets:

- Dominant: dark rock gray, cold charcoal, ash gray, mud brown, and soot black.
- Secondary: weathered stone beige-gray, clay brown, dry dust, and muted gravel.
- Faction accent: oxide red, faded maroon, or chipped dull red in small controlled beats.
- Metal accent: blackened iron or dull dark steel only for sparse embedded scrap.
- Emissive: none for the baseline asset.

Blood Axe separation rule:

- Use hostile raider approach grime, rough damage, ash, mud, and intimidation marks.
- Do not use neutral/civilized Giant materials such as refined blue-gray masonry, terrace stonework, water channels, warm orderly hearth treatment, restrained blue runes, civic clan symbols, or master stoneworker pride.

## Concept Image Prompt

Create an original stylized fantasy MMORPG concept image of `SM_GIA_BloodAxeApproachCliffLedgeCap_A01` for the world of Aerathea. The design should emphasize a hostile Blood Axe Giant stronghold approach ledge cap, thick local cliff shelf silhouette, broken rock lip, rubble shelves, undercut shadow band, mud and ash settling on the shelf top, fractured dark highland stone, soot staining, sparse blackened scrap, restrained oxide-red warning cloth or paint, validated Giant scale with female baseline 442 cm / 14'6" and male baseline 470 cm / 15'5", visual scale for switchbacks, and strict separation from neutral/civilized Giant stoneworker culture. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, no emissive glow, and MMO-friendly mid-poly production design. Present it as a static mesh production sheet with front lip view, side thickness view, top footprint view, rubble-shelf callouts, material swatches, LOD notes, scale bars beside the 442 cm female and 470 cm male Giant baselines, and labels stating docs-only visual ledge framing. Avoid copying any existing franchise, avoid graphic gore, avoid refined civilized Giant masonry, avoid making Blood Axe culture the default Giant culture, avoid climb-route diagrams, avoid nav/pathfinding arrows, avoid walkable-collision claims, avoid terrain implementation claims, avoid Unreal or startup placement claims, avoid source concept embedding or movement, and avoid excessive micro-detail that would not translate to a mid-poly Unreal asset.

Concept source note: this package references `BloodAxeStronghold.png#Cliffs_LedgeCaps` only through existing intake documentation. It does not inspect, move, copy, crop, embed, rename, commit, or approve external source concept art.

## Modeling Notes

This is a docs-only modeling plan. No mesh, sculpt, retopo, UV, bake, collision proxy, proof render, FBX, Unreal import, material graph, Blueprint, validator, startup actor, runtime behavior, first implementation target, or final visual approval is created or approved here.

Future modeling, if separately approved, should prioritize:

- A single strong ledge cap silhouette with a thick readable shelf and broken front lip.
- Broad rock planes with stylized fractures that support hand-painted material detail.
- Large rubble shelves at the sides or base, using a few chunky stones instead of dense scatter.
- Mud-packed upper surface areas and ash settling pockets that visually tie into switchback path dressing.
- Undercut planes and shadow-catching geometry beneath the front lip to sell cliff depth.
- Slight asymmetry at the ends so repeated modules do not look tiled, while keeping forms reusable.
- Sparse Blood Axe accents such as one red cloth scrap, a blackened shield fragment, or a horn marker only if they do not dominate the rock form.

Use texture, normal maps, AO, or masks for:

- Fine stone cracks, small chips, gravel, ash dust, soot speckles, mud drying lines, minor scrape marks, tiny embedded grit, cloth weave, faint red paint wear, and subtle weathering gradients.

Do not model gameplay affordances such as climb holds, jump markers, route arrows, ladder notches, nav guides, collision planes, trigger shapes, objective symbols, loot markers, destructible fracture states, or player-readable path signage.

## Texture and Material Notes

Required future map set:

- Base Color / Albedo (`BC`)
- Normal (`N`)
- Packed Occlusion/Roughness/Metallic (`ORM`)

No material graph, shader, material instance, texture asset, emissive map, VFX graph, Unreal import, or source file is authored by this package.

Material slot target:

- Slot 0: planned `MI_GIA_BloodAxeCliffRock_A01` for fractured stone, ledge faces, undercut planes, rubble stones, baked AO, soot staining, and broad rock value variation.
- Optional Slot 1: planned `MI_GIA_BloodAxePackedEarth_A01` or shared dirt/ash mask material for mud-packed top edges, ash settling, compacted dirt, and small Blood Axe red marks if a later build needs separate control.
- Optional accent handling: sparse red cloth, blackened iron scrap, or horn markers should be atlas or mask driven where possible instead of adding unique slots.

Texture naming targets:

- `T_GIA_BloodAxeApproachCliffLedgeCap_A01_BC`
- `T_GIA_BloodAxeApproachCliffLedgeCap_A01_N`
- `T_GIA_BloodAxeApproachCliffLedgeCap_A01_ORM`
- Optional future `T_GIA_BloodAxeApproachCliffLedgeCap_A01_Mask` for mud, ash, soot, red accent, or rock-value variation if separately approved.

Texture resolution targets:

- Standard ledge cap: 1K texture set.
- Close-route ledge cap: 2K texture set only if later approved for near-camera switchback dressing.
- Far repeated ledge cap: 512 texture set or shared cliff atlas if repeated heavily.

Packed `ORM` guidance:

- R: ambient occlusion in undercuts, rubble shelf contacts, deep fractures, mud pockets, and rock-to-dirt transitions.
- G: high roughness for dry stone, ash, dirt, soot, and matte mud; medium-high variation only for damp mud pockets.
- B: metallic black except for sparse blackened iron scrap, shield chip, or blade fragment masks if included.

## Triangle Budget

`SM_GIA_BloodAxeApproachCliffLedgeCap_A01` is a large local environment prop. It should be lighter than a full cliff wall kit segment and heavier than a flat path strip.

Target budget:

- LOD0 target: 3.5k-8k tris.
- LOD0 hard cap: 10k tris only if the future approved mesh includes substantial undercut geometry, side rubble shelves, and strong silhouette variation.
- Material slots: 1 target, 2 maximum.
- Texture target: 1K standard, 2K only for approved near-camera switchback use.

Suggested LOD0 allocation:

- Main shelf plane, thick ledge mass, and front rock lip: 45-55 percent.
- Undercut shadow planes and side fracture silhouettes: 18-25 percent.
- Large rubble shelf stones and broken side masses: 15-22 percent.
- Mud/ash top forms and broad settling ridges: 5-10 percent.
- Sparse Blood Axe accent geometry: 0-5 percent.

Do not spend triangles on dense gravel, tiny cracks, per-pebble rubble, ash flecks, small scratches, cloth fibers, little chips, subtle mud ripples, or non-silhouette grit.

## LOD Plan

All future approved mesh work should include LOD0-LOD3.

- LOD0: 3.5k-8k tris target, 10k hard cap. Full ledge shelf, thick front lip, undercut shadow band, large fracture planes, side rubble shelves, mud/ash top buildup, and sparse Blood Axe accent if approved.
- LOD1: 60-70 percent of LOD0. Reduce small fracture cuts, rubble stone subdivisions, minor ledge bevels, mud ridge geometry, and non-silhouette accent detail.
- LOD2: 35-45 percent of LOD0. Preserve the shelf footprint, thick lip, main undercut read, and largest rubble masses while flattening secondary fracture planes and small stones.
- LOD3: 15-25 percent of LOD0. Preserve the broad ledge-cap block, dark front lip value, and switchback shelf silhouette. Remove most rubble detail, small accents, bevels, and minor mud relief.

Reduction order:

1. Fine cracks, ash speckles, soot noise, grit, tiny chips, and cloth fibers.
2. Small stones, minor red scraps, little mud ridges, and non-silhouette chips.
3. Secondary fracture cuts, rubble undercuts, and side bevel subdivisions.
4. Optional accent fragments and hidden backside detail.
5. Only then simplify the main shelf plane, front lip, undercut shadow read, and Giant-scale ledge silhouette.

Never destroy the primary shelf-lip read, rubble shelf massing, switchback scale cue, or Blood Axe hostile material identity before removing small detail.

## Collision Notes

Collision is planning only. Do not create collision proxies, custom UCX meshes, physics bodies, runtime collision channels, nav links, nav blockers, smart links, traversal proofs, validation scripts, or runtime setup from this package.

Future collision intent, if a later implementation task approves it:

- Default recommendation: collision disabled for visual-only ledge caps placed against larger environment collision.
- If promoted to static blocking dressing, use one to three simple convex hulls around the largest rock mass and front lip only.
- Do not use per-crack, per-rubble, per-stone, per-mud, per-cloth, or per-scrap collision.
- Do not use this asset to define walkable surfaces, player route clearance, AI route clearance, climbing, jumping, navmesh carving, pathfinding preference, encounter lanes, cover rules, projectile blocking, damage volumes, trigger zones, or terrain fit.

The asset may visually suggest a cliff shelf or switchback edge, but this package does not validate route safety, playable traversal, landscape integration, or collision correctness.

## Animation Notes

Baseline asset is static.

Allowed at planning level:

- Static rock cap, rubble shelf, mud/ash top, and sparse non-animated Blood Axe accent.
- Static material variation for rock value, soot, mud, ash, and red paint wear if later approved by a material task.

Approval-gated future options:

- Wind movement for a small cloth scrap.
- Falling dust, loose pebble trickle, torch glow, signal fire, shamanic effect, or ritual marker variant.
- Breakable ledge, falling rock, climb response, destructible state, physics debris, audio cue, Blueprint behavior, or gameplay trigger.

None of those options are authorized by this package.

## Unreal Import Notes

This section is future planning only. No Unreal Content asset, material instance, texture, socket, collision proxy, Blueprint, validator, runtime source, review-scene actor, startup actor, import script, source asset, or implementation file is created or authorized.

Potential future Unreal placement, if a separate implementation task approves it:

- Mesh folder: `/Game/Aerathea/Environment/Giants/BloodAxeCamp/StrongholdApproach/Cliffs/`
- Material folder: `/Game/Aerathea/Materials/Giants/BloodAxe/`
- Texture folder: `/Game/Aerathea/Textures/Giants/BloodAxe/StrongholdApproach/Cliffs/`

Candidate future asset settings:

- Asset type: Static Mesh.
- Candidate mesh name: `SM_GIA_BloodAxeApproachCliffLedgeCap_A01`.
- Pivot recommendation: bottom-center of the main ledge footprint, aligned for manual placement against cliff-wall and switchback visual modules.
- Scale: authored in centimeters at 1 Unreal unit = 1 cm.
- Collision: disabled by default unless a later implementation task explicitly approves simple static hulls.
- LODs: LOD0-LOD3 required for any approved mesh.
- Material slots: 1 target, 2 maximum.
- Sockets: none planned.
- Blueprint behavior: none planned.
- Animation: none planned.
- Performance note: use instancing or repeated variants for multiple ledge caps; avoid unique high-poly ledge geometry per switchback beat.

No startup placement, final view capture, visual approval, traversal validation, climb validation, nav/pathfinding validation, terrain validation, or first implementation target is claimed here.

## Folder and Naming Recommendation

Allowed docs path for this package:

- `docs/assets/props/SM_GIA_BloodAxeApproachCliffLedgeCap_A01/PRODUCTION_PACKAGE.md`

Recommended future naming, approval-gated only:

- Static mesh: `SM_GIA_BloodAxeApproachCliffLedgeCap_A01`
- Material instance: `MI_GIA_BloodAxeApproachCliffLedgeCap_A01`
- Base color texture: `T_GIA_BloodAxeApproachCliffLedgeCap_A01_BC`
- Normal texture: `T_GIA_BloodAxeApproachCliffLedgeCap_A01_N`
- ORM texture: `T_GIA_BloodAxeApproachCliffLedgeCap_A01_ORM`
- Optional mask texture: `T_GIA_BloodAxeApproachCliffLedgeCap_A01_Mask`

Future variant naming, if later approved:

- `SM_GIA_BloodAxeApproachCliffLedgeCap_A02` for a narrower side shelf variant.
- `SM_GIA_BloodAxeApproachCliffLedgeCap_B01` for a larger overhang-heavy variant.
- `SM_GIA_BloodAxeApproachCliffRubbleShelf_A01` only if rubble shelves become a separate asset rather than part of this ledge cap.

No SourceAssets folder, DCC folder, Unreal folder, runtime source path, import script path, validator path, startup-scene path, external source concept path, or implementation target is created by this package.

## Quality Gate Checklist

- The package uses the 15 required Aerathea production headings and remains docs-only.
- The asset is scoped to local ledge caps, rubble shelves, rock lips, cliff shelf silhouettes, mud/ash settling, and visual scale for switchbacks.
- Giant scale lock is explicit: female baseline 442 cm / 14'6", male baseline 470 cm / 15'5", approved ranges females 14-15 ft / 427-457 cm and males 14'10"-16'0" / 452-488 cm.
- Blood Axe is clearly a hostile Giant sub-faction and is not presented as neutral/civilized Giant culture.
- Neutral/civilized Giant cave-town, master stonework, blue-gray masonry, terrace, waterwork, warm hearth, restrained blue-rune, and civic stoneworker language remain excluded from the Blood Axe default read.
- Silhouette reads as a thick local cliff ledge cap with broken rock lip, undercut shadow, rubble shelf, and switchback scale cue.
- Materials prioritize fractured dark rock, packed mud, ash, soot, charcoal, muted gravel, sparse blackened scrap, and restrained oxide-red accents.
- Emissive, VFX, animation, destructible behavior, and gameplay interaction are absent from the baseline asset.
- Triangle budget, LOD0-LOD3 plan, texture map set, material slot target, and collision planning notes are included.
- No DCC, FBX, Unreal Content, runtime source, source concept movement, startup placement, final visual approval, first implementation target selection, traversal proof, climb route, nav/pathfinding, walkable collision implementation, or terrain implementation claim is made.
- Collision remains future planning only and does not define route safety, playable traversal, navmesh, climb behavior, or terrain fit.
- The package is useful for future production handoff without requiring another agent to reinterpret the child intake row.
