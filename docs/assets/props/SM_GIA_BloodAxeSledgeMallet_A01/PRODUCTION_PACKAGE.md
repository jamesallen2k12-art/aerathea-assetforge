# SM_GIA_BloodAxeSledgeMallet_A01 Production Package

## Art Direction Summary

- Asset name: `SM_GIA_BloodAxeSledgeMallet_A01`
- Asset type: Static Mesh prop production package, docs-only
- Parent kit: `KIT_GIA_BloodAxeCampTools_A01`
- Child intake row: `BloodAxeForge.png#CampTools_Mallet_Sledge_A01`
- Faction/theme: Blood Axe Tribe, hostile Giant sub-faction only
- Status: docs-only production package ready

`SM_GIA_BloodAxeSledgeMallet_A01` is a heavier forge-adjacent Giant-scale sledge mallet for Blood Axe camp utility dressing. It should read as an inert work prop with a massive rectangular head, reinforced bands, long worn handle, soot, ash, and crude red marks.

Blood Axe visual language must remain a hostile Giant sub-faction identity, separate from neutral/civilized Giant culture. Do not use refined highland toolcraft, cave-town civic symbols, peaceful hearth storage, polished smithy display, blue-gray carved stone, or restrained blue rune identity.

Guardrails: no-DCC, no-Unreal, no-harvest, no-crafting, no-salvage, no-resource, no-weapon-trace, no-pickup, no-NPC-work-loop, no-physics, no-gate/destructible, no-implementation-target. This package is planning documentation only and does not authorize source assets, FBX, Unreal Content, runtime source, validators, external concept movement, final visual approval, sockets, skeletal attachment, or first DCC target selection.

## Gameplay Purpose

Static forge-support dressing only:

- Visual clutter near forge support clusters, iron wedge stacks, repair areas, tool buckets, and rough camp work lanes.
- Scale support for female 442 cm / 14'6" and male 470 cm / 15'5" Giants.
- Non-interactive evidence of heavy Blood Axe maintenance without defining a usable forge station, crafting loop, pickup tool, weapon, or NPC work-loop target.

The sledge mallet is not a combat weapon, not a crafting station interaction, not a harvest tool, not a salvage tool, not inventory gear, not a resource object, and not a physics object.

## Silhouette Notes

Primary read: one massive rectangular-headed sledge mallet with an extra-heavy head and long handle.

Required silhouette features:

- Oversized rectangular or squared-off head with broad striking faces.
- Dark reinforcing bands, end plates, or crude staples.
- Long thick handle with practical grip wraps.
- Low lying display posture or lean-ready profile for forge-adjacent clutter.
- Optional dull red slash, cloth tie, or chipped paint mark as a restrained Blood Axe accent.

Model the large head, handle, bands, end plates, broad wraps, and major dents as geometry. Use textures for scratches, soot, ash, wood grain, leather wear, pitting, mud, and chipped paint.

Avoid warhammer silhouette language, spikes, blades, socket-ready weapon proportions, swing trail reads, pickup highlights, hot forge glow, refined smithy presentation, and neutral/civilized Giant craft language.

## Scale Notes

Use the validated `SK_GIA_Base_A01` scale lock:

- Female Giant baseline: 442 cm / 14'6".
- Male Giant baseline: 470 cm / 15'5".
- Approved Giant ranges: females 14-15 ft / 427-457 cm; males 14'10"-16'0" / 452-488 cm.
- Author future source in centimeters. 1 Unreal unit equals 1 cm.

Recommended dimensions:

- Overall length: 180-300 cm.
- Head width: 80-150 cm.
- Head depth: 50-95 cm.
- Head height: 45-95 cm.
- Handle diameter: 14-32 cm, with larger grip wraps.
- Display footprint when lying down: 220-340 cm long, 90-170 cm wide.

## Materials and Color Palette

Primary materials:

- Dense scorched hardwood, battered head blocks, dark iron caps, and blackened steel bands.
- Worn handle wood, hide grip wrap, scorched leather, soot, ash, oil, mud, and forge grime.
- Restrained dull Blood Axe red cloth tie, rubbed paint mark, or warning slash.

Palette targets:

- Wood: dark umber, charred brown, dirty ochre, ash-stained tan.
- Metal: charcoal black, dark gunmetal, dull steel edge.
- Leather/hide: smoked tan, dark brown, soot black.
- Blood Axe accent: oxide red, faded maroon, chipped dark red.

No emissive, hot-metal glow, forge glow, ritual glow, or magic glow is approved for baseline `A01`.

## Concept Image Prompt

Create an original stylized fantasy MMORPG concept image of `SM_GIA_BloodAxeSledgeMallet_A01` for the world of Aerathea. The design should emphasize one oversized Giant-scale forge-adjacent sledge mallet, massive rectangular head, long thick handle, blackened iron bands, dark end plates, hide-wrapped grip, scorched hardwood, soot, ash, mud, chipped dull red paint, hostile Blood Axe Giant camp identity, clear separation from neutral/civilized Giant culture, female Giant scale 442 cm / 14'6", male Giant scale 470 cm / 15'5", and the gameplay role of static non-interactive forge support dressing. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, no emissive glow, and MMO-friendly production design. Present it as a single prop production sheet with front, side, top, three-quarter, material swatches, LOD callouts, simple collision callouts, and scale markers. Avoid copying any existing franchise, avoid combat weapon presentation, avoid weapon-trace or pickup affordances, avoid harvest/crafting/resource/salvage language, avoid NPC work-loop diagrams, avoid physics or gate/destructible diagrams, avoid implementation-target claims, and avoid excessive micro-detail that would not translate to a mid-poly Unreal asset.

Concept source note: this package references `BloodAxeForge.png#CampTools_Mallet_Sledge_A01` only through existing intake documentation. It does not copy, move, crop, edit, embed, inspect for final approval, or commit external source concept art.

## Modeling Notes

Future modeling guidance only:

- Build one static sledge mallet with a dominant rectangular head and strong handle silhouette.
- Keep the head utilitarian and blunt; avoid warhammer spikes, blades, or heroic weapon proportions.
- Use wide bands, end plates, and handle wraps as geometry where they affect silhouette.
- Add a few major dents, chipped corners, and asymmetries; keep fine wear in textures.
- Ground one side for stable display near forge support clusters.

Do not create DCC source, sculpt, retopo, UVs, bakes, collision proxies, proof renders, LOD source, FBX exports, Unreal assets, sockets, skeletal attachments, runtime files, validators, startup placement, or implementation targets from this task.

## Texture and Material Notes

Target material strategy:

- Material slots: 1 preferred, 2 maximum for wood/metal separation.
- Texture set: 1K target, 512 allowed for distant repeats.
- Required future maps: Base Color (`BC`), Normal (`N`), packed Occlusion/Roughness/Metallic (`ORM`).
- No emissive texture for baseline `A01`.

Suggested future names:

- `MI_GIA_BloodAxeSledgeMallet_A01`
- `T_GIA_BloodAxeSledgeMallet_A01_BC`
- `T_GIA_BloodAxeSledgeMallet_A01_N`
- `T_GIA_BloodAxeSledgeMallet_A01_ORM`

Use texture and normal detail for scorched wood grain, soot, ash, oil stains, mud, scratches, leather wear, small cracks, iron pitting, and chipped red paint.

## Triangle Budget

Target as a medium static prop:

- LOD0: 1,200-3,600 tris.
- Preferred A01 LOD0 range: 1,700-2,900 tris.
- LOD1: 650-1,700 tris.
- LOD2: 260-850 tris.
- LOD3: 100-320 tris.
- Material slots: 1 target, 2 maximum.

Spend geometry on the heavy head silhouette, handle, broad bands, end plates, large wraps, and major dents. Do not spend geometry on fine wood grain, soot speckles, small cracks, scratches, mud flecks, leather pores, or tiny rivets.

## LOD Plan

All future shipping-quality mesh work requires LOD0-LOD3.

- LOD0: full massive head, handle, bands, end plates, wraps, major dents, and display footprint.
- LOD1: 55-65 percent of LOD0; reduce bevel loops, end-plate subdivisions, wrap folds, and underside detail.
- LOD2: 25-40 percent of LOD0; preserve rectangular head, long handle, and dominant bands while simplifying wraps.
- LOD3: 10-20 percent of LOD0; preserve blunt sledge read, large head-to-handle ratio, and one strong material accent.

Remove fine scratches, soot flecks, paint chips, pitting, small cracks, mud flecks, and leather pores before reducing the primary sledge silhouette.

## Collision Notes

Collision is planning-only:

- Preferred default: collision disabled for decorative forge clutter.
- If blocking is later required: one simple box/capsule combination or low-count convex hull around the display footprint.
- No weapon trace, handle trace, per-band, per-wrap, per-end-plate, or sharp-edge collision.

Do not create pickup collision, weapon traces, harvest volumes, crafting interaction volumes, salvage/resource triggers, NPC work-loop volumes, physics bodies, gate logic collision, destructible fracture collision, nav blockers, runtime gameplay collision, or Unreal collision proxies from this package.

## Animation Notes

Baseline asset is static. No animation, physics simulation, mallet swing, tool use, weapon use, weapon trace, pickup behavior, crafting loop, harvesting state, salvage state, resource state, NPC work loop, socket attachment, gate operation, destructible state, VFX, audio, material-state timing, or Blueprint behavior is planned.

Any active, held, socketed, usable, craftable, harvest-linked, physics-enabled, or combat sledge mallet must become a separate approval-gated package.

## Unreal Import Notes

Future Unreal import guidance only:

- Asset type: Static Mesh.
- Suggested Unreal path: `/Game/Aerathea/Props/Giants/BloodAxeCamp/CampTools/SM_GIA_BloodAxeSledgeMallet_A01`
- Import scale: 1.0; authored in centimeters.
- Pivot: ground center of display footprint for lying-down placement.
- Orientation: display variant rests on XY ground plane, Z up.
- Collision: disabled by default or one simple low hull only if later layout work requires it.
- LODs: import LOD0-LOD3 when authored by a future DCC lane.
- Material slots: 1 preferred, 2 maximum.
- Sockets: none.
- Blueprint behavior: none.

Do not import, place, create materials, create textures, add sockets, define Blueprints, run startup placement, create validators, or select an implementation target from this package.

## Folder and Naming Recommendation

Documentation path:

- `docs/assets/props/SM_GIA_BloodAxeSledgeMallet_A01/PRODUCTION_PACKAGE.md`

Future naming, if separately approved:

- Static Mesh: `SM_GIA_BloodAxeSledgeMallet_A01`
- Material Instance: `MI_GIA_BloodAxeSledgeMallet_A01`
- Textures: `T_GIA_BloodAxeSledgeMallet_A01_BC`, `T_GIA_BloodAxeSledgeMallet_A01_N`, `T_GIA_BloodAxeSledgeMallet_A01_ORM`

These are recommendations only and do not create source folders, exports, Unreal Content, runtime source, first DCC target selection, or implementation target selection.

## Quality Gate Checklist

- Uses the female 442 cm / 14'6" and male 470 cm / 15'5" Giant scale lock.
- Reads as Blood Axe hostile Giant sub-faction dressing, separate from neutral/civilized Giant culture.
- Keeps the sledge mallet as forge-support utility clutter, not a combat weapon.
- Avoids pickup affordances, weapon traces, sockets, skeletal attachment, hot-metal glow, and NPC work-loop claims.
- Includes Base Color, Normal, and packed ORM texture planning.
- Includes LOD0-LOD3 and simple display collision guidance.
- Keeps emissive, harvest logic, crafting logic, salvage logic, resource logic, pickup behavior, weapon traces, NPC work loops, physics, gate/destructible behavior, DCC, Unreal, validators, source assets, and implementation targets out of scope.
