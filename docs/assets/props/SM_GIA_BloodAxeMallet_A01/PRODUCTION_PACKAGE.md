# SM_GIA_BloodAxeMallet_A01 Production Package

## Art Direction Summary

- Asset name: `SM_GIA_BloodAxeMallet_A01`
- Asset type: Static Mesh prop production package, docs-only
- Parent kit: `KIT_GIA_BloodAxeCampTools_A01`
- Child intake row: `BloodAxeCamp.png#CampTools_Mallet_Heavy_A01`
- Faction/theme: Blood Axe Tribe, hostile Giant sub-faction only
- Status: docs-only production package ready

`SM_GIA_BloodAxeMallet_A01` is a single heavy Giant-scale camp mallet for Blood Axe utility dressing. It should read as a brutal practical tool, not a combat weapon: thick head, long worn handle, iron bands, hide wrap, soot grime, and restrained dull red marks.

Blood Axe visual language must remain a hostile Giant sub-faction identity, separate from neutral/civilized Giant culture. Do not use refined highland toolcraft, cave-town civic symbols, polished domestic workshop language, warm hearth presentation, blue-gray carved stone, or restrained blue rune identity.

Guardrails: no-DCC, no-Unreal, no-harvest, no-crafting, no-salvage, no-resource, no-weapon-trace, no-pickup, no-NPC-work-loop, no-physics, no-gate/destructible, no-implementation-target. This package is planning documentation only and does not authorize source assets, FBX, Unreal Content, runtime source, validators, external concept movement, final visual approval, sockets, skeletal attachment, or first DCC target selection.

## Gameplay Purpose

Static environmental storytelling only:

- Utility dressing beside buckets, rope coils, wedges, rough repairs, forge support clutter, and shelter edges.
- Scale reference for Blood Axe Giant camp tools beside female 442 cm / 14'6" and male 470 cm / 15'5" Giants.
- Non-interactive prop that suggests rough maintenance without becoming a usable tool, weapon, pickup, crafting loop, or NPC work-loop target.

The mallet is not a weapon, not a harvest tool, not a crafting station tool, not a pickup, not inventory gear, not a resource object, and not a physics prop.

## Silhouette Notes

Primary read: one oversized mallet with a thick head, long handle, blunt ends, and simple wrapped grip.

Required silhouette features:

- Heavy rectangular or barrel-like head with broad end faces.
- Long handle scaled for Giant hands.
- Wide iron bands or crude straps around the head.
- Hide-wrapped grip with large readable wraps.
- Slight bend, dent, or asymmetry to avoid a refined workshop read.
- Optional dull red cloth tie or chipped paint slash as a restrained Blood Axe accent.

Model the head, handle, bands, large wrap forms, end caps, and major dents as geometry. Use textures for wood grain, soot, scratches, leather wear, small cracks, pitting, mud, and chipped paint.

Avoid axe/hammer weapon silhouettes, sharp striking spikes, socket-ready handles, pickup highlights, combat trail language, readable weapon stats, refined tool-shop finish, and neutral/civilized Giant craft language.

## Scale Notes

Use the validated `SK_GIA_Base_A01` scale lock:

- Female Giant baseline: 442 cm / 14'6".
- Male Giant baseline: 470 cm / 15'5".
- Approved Giant ranges: females 14-15 ft / 427-457 cm; males 14'10"-16'0" / 452-488 cm.
- Author future source in centimeters. 1 Unreal unit equals 1 cm.

Recommended dimensions:

- Overall length: 140-260 cm.
- Head width: 55-120 cm.
- Head depth: 35-80 cm.
- Head height: 35-80 cm.
- Handle diameter: 12-28 cm, with larger grip wraps.
- Display footprint when lying down: 170-300 cm long, 70-140 cm wide.

## Materials and Color Palette

Primary materials:

- Scorched hardwood, cracked handle wood, battered mallet head timber, or dark metal-capped head faces.
- Blackened iron bands, dark steel plates, crude staples, and dull hammered caps.
- Hide wraps, scorched leather grip, soot, ash, mud, grease, and grime.
- Restrained dull Blood Axe red cloth tie or chipped paint.

Palette targets:

- Wood: dark umber, scorched brown, dirty ochre, ash-stained tan.
- Metal: charcoal black, dark gunmetal, worn dull steel.
- Leather/hide: dark brown, smoked tan, soot black.
- Blood Axe accent: oxide red, faded maroon, chipped dark red.

No emissive material is approved for baseline `A01`.

## Concept Image Prompt

Create an original stylized fantasy MMORPG concept image of `SM_GIA_BloodAxeMallet_A01` for the world of Aerathea. The design should emphasize one oversized Giant-scale utility mallet, thick blunt head, long worn handle, blackened iron bands, hide-wrapped grip, scorched hardwood, soot, ash, mud, chipped dull red paint, hostile Blood Axe Giant camp identity, clear separation from neutral/civilized Giant culture, female Giant scale 442 cm / 14'6", male Giant scale 470 cm / 15'5", and the gameplay role of static non-interactive camp utility dressing. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, no emissive glow, and MMO-friendly production design. Present it as a single prop production sheet with front, side, top, three-quarter, material swatches, LOD callouts, simple collision callouts, and scale markers. Avoid copying any existing franchise, avoid combat weapon presentation, avoid weapon-trace or pickup affordances, avoid harvest/crafting/resource/salvage language, avoid NPC work-loop diagrams, avoid physics or gate/destructible diagrams, avoid implementation-target claims, and avoid excessive micro-detail that would not translate to a mid-poly Unreal asset.

Concept source note: this package references `BloodAxeCamp.png#CampTools_Mallet_Heavy_A01` only through existing intake documentation. It does not copy, move, crop, edit, embed, inspect for final approval, or commit external source concept art.

## Modeling Notes

Future modeling guidance only:

- Build one static mallet with a clear head/handle hierarchy.
- Keep the head blunt and utilitarian; avoid spikes, blades, or combat weapon silhouette language.
- Use broad bands and large wraps as geometry where they affect silhouette.
- Add a few major dents, chips, and asymmetries; keep fine wear in textures.
- Support lying-down display orientation by keeping one side visually grounded.

Do not create DCC source, sculpt, retopo, UVs, bakes, collision proxies, proof renders, LOD source, FBX exports, Unreal assets, sockets, skeletal attachments, runtime files, validators, startup placement, or implementation targets from this task.

## Texture and Material Notes

Target material strategy:

- Material slots: 1 preferred, 2 maximum for wood/metal separation.
- Texture set: 512-1K.
- Required future maps: Base Color (`BC`), Normal (`N`), packed Occlusion/Roughness/Metallic (`ORM`).
- No emissive texture for baseline `A01`.

Suggested future names:

- `MI_GIA_BloodAxeMallet_A01`
- `T_GIA_BloodAxeMallet_A01_BC`
- `T_GIA_BloodAxeMallet_A01_N`
- `T_GIA_BloodAxeMallet_A01_ORM`

Use texture and normal detail for wood grain, soot, mud, ash, scratches, leather wear, small cracks, iron pitting, chipped red paint, and grime around ground contact.

## Triangle Budget

Target as a small static prop:

- LOD0: 900-3,000 tris.
- Preferred A01 LOD0 range: 1,200-2,400 tris.
- LOD1: 450-1,300 tris.
- LOD2: 180-650 tris.
- LOD3: 80-240 tris.
- Material slots: 1 target, 2 maximum.

Spend geometry on the head silhouette, handle cylinder, broad bands, large wraps, end caps, and major dents. Do not spend geometry on wood grain, small cracks, scratches, soot speckles, mud flecks, leather pores, or tiny rivets.

## LOD Plan

All future shipping-quality mesh work requires LOD0-LOD3.

- LOD0: full head, handle, bands, wraps, end caps, major dents, and display footprint.
- LOD1: 55-65 percent of LOD0; reduce bevel loops, wrap folds, hidden underside faces, and minor dents.
- LOD2: 25-40 percent of LOD0; preserve head/handle silhouette and major bands while simplifying wraps.
- LOD3: 10-20 percent of LOD0; preserve blunt mallet read, long handle, and one strong material accent.

Remove fine scratches, small cracks, soot flecks, paint chips, leather pores, and pitting before reducing the primary mallet silhouette.

## Collision Notes

Collision is planning-only:

- Preferred default: collision disabled for decorative ground clutter.
- If blocking is later required: one simple box/capsule combination or low-count convex hull around the display footprint.
- No weapon trace, handle trace, per-band, per-wrap, or sharp-edge collision.

Do not create pickup collision, weapon traces, harvest volumes, crafting interaction volumes, salvage/resource triggers, NPC work-loop volumes, physics bodies, gate logic collision, destructible fracture collision, nav blockers, runtime gameplay collision, or Unreal collision proxies from this package.

## Animation Notes

Baseline asset is static. No animation, physics simulation, mallet swing, tool use, weapon use, weapon trace, pickup behavior, crafting loop, harvesting state, salvage state, resource state, NPC work loop, socket attachment, gate operation, destructible state, VFX, audio, material-state timing, or Blueprint behavior is planned.

Any active, held, socketed, usable, craftable, harvest-linked, physics-enabled, or combat mallet must become a separate approval-gated package.

## Unreal Import Notes

Future Unreal import guidance only:

- Asset type: Static Mesh.
- Suggested Unreal path: `/Game/Aerathea/Props/Giants/BloodAxeCamp/CampTools/SM_GIA_BloodAxeMallet_A01`
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

- `docs/assets/props/SM_GIA_BloodAxeMallet_A01/PRODUCTION_PACKAGE.md`

Future naming, if separately approved:

- Static Mesh: `SM_GIA_BloodAxeMallet_A01`
- Material Instance: `MI_GIA_BloodAxeMallet_A01`
- Textures: `T_GIA_BloodAxeMallet_A01_BC`, `T_GIA_BloodAxeMallet_A01_N`, `T_GIA_BloodAxeMallet_A01_ORM`

These are recommendations only and do not create source folders, exports, Unreal Content, runtime source, first DCC target selection, or implementation target selection.

## Quality Gate Checklist

- Uses the female 442 cm / 14'6" and male 470 cm / 15'5" Giant scale lock.
- Reads as Blood Axe hostile Giant sub-faction dressing, separate from neutral/civilized Giant culture.
- Keeps the mallet as a utility prop, not a combat weapon.
- Avoids pickup affordances, weapon traces, sockets, skeletal attachment, and NPC work-loop claims.
- Includes Base Color, Normal, and packed ORM texture planning.
- Includes LOD0-LOD3 and simple display collision guidance.
- Keeps emissive, harvest logic, crafting logic, salvage logic, resource logic, pickup behavior, weapon traces, NPC work loops, physics, gate/destructible behavior, DCC, Unreal, validators, source assets, and implementation targets out of scope.
