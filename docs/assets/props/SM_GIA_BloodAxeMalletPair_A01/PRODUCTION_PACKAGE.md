# SM_GIA_BloodAxeMalletPair_A01 Production Package

## Art Direction Summary

- Asset name: `SM_GIA_BloodAxeMalletPair_A01`
- Asset type: Static Mesh prop production package, docs-only
- Parent kit: `KIT_GIA_BloodAxeCampTools_A01`
- Child intake row: `BloodAxeShelter.png#CampTools_MalletPair_A01`
- Faction/theme: Blood Axe Tribe, hostile Giant sub-faction only
- Status: docs-only production package ready

`SM_GIA_BloodAxeMalletPair_A01` is a paired display arrangement of two oversized Blood Axe camp mallets, crossed or leaned for shelter-edge utility dressing. It should read as sparse, practical, and inert: two blunt tool silhouettes, thick heads, worn handles, hide wraps, blackened bands, soot, mud, and restrained dull red accents.

Blood Axe visual language must remain a hostile Giant sub-faction identity, separate from neutral/civilized Giant culture. Do not use refined highland workshop order, cave-town civic symbols, peaceful hearth storage, polished domestic tool racks, blue-gray carved stone, or restrained blue rune identity.

Guardrails: no-DCC, no-Unreal, no-harvest, no-crafting, no-salvage, no-resource, no-weapon-trace, no-pickup, no-NPC-work-loop, no-physics, no-gate/destructible, no-implementation-target. This package is planning documentation only and does not authorize source assets, FBX, Unreal Content, runtime source, validators, external concept movement, final visual approval, sockets, skeletal attachment, or first DCC target selection.

## Gameplay Purpose

Static shelter-edge dressing only:

- Visual clutter beside shelters, buckets, rope coils, wall edges, and low utility clusters.
- Scale support for female 442 cm / 14'6" and male 470 cm / 15'5" Giants.
- Non-interactive paired silhouette that suggests rough camp labor without defining pickup tools, weapons, crafting loops, or NPC work-loop targets.

The pair is not a weapon rack, not a pickup set, not a harvest tool set, not a crafting station, not a salvage source, not inventory gear, not a physics prop pair, and not an NPC work target.

## Silhouette Notes

Primary read: two distinct blunt mallets, crossed on the ground or leaned together with enough negative space to read as two tools.

Required silhouette features:

- Two thick mallet heads with different proportions.
- Long handles with readable Giant-scale grip wraps.
- Crossed, leaned, or offset arrangement that remains sparse and non-interactive.
- Broad iron bands, end caps, or hide wraps as secondary reads.
- Optional dull red tie or chipped paint accent on one mallet only.

Model the two heads, handles, bands, broad wraps, end caps, and major dents as geometry. Use textures for wood grain, soot, scratches, leather wear, small cracks, pitting, mud, and chipped paint.

Avoid weapon-rack presentation, socket-ready attachment positions, crossed-warhammer heraldry, pickup highlights, combat trail language, readable weapon stats, refined tool storage, and neutral/civilized Giant craft language.

## Scale Notes

Use the validated `SK_GIA_Base_A01` scale lock:

- Female Giant baseline: 442 cm / 14'6".
- Male Giant baseline: 470 cm / 15'5".
- Approved Giant ranges: females 14-15 ft / 427-457 cm; males 14'10"-16'0" / 452-488 cm.
- Author future source in centimeters. 1 Unreal unit equals 1 cm.

Recommended dimensions:

- Each mallet overall length: 140-260 cm.
- Each head width: 55-120 cm.
- Each head depth: 35-80 cm.
- Pair footprint when crossed or leaned: 220-420 cm wide, 160-320 cm deep, 80-240 cm tall depending on pose.
- Keep the pair low enough for shelter-edge dressing and not a default navigation blocker.

## Materials and Color Palette

Primary materials:

- Scorched hardwood, battered mallet heads, worn handles, and cracked tool surfaces.
- Blackened iron bands, dark steel caps, crude staples, and dull hammered plates.
- Hide wraps, dirty leather grips, soot, ash, mud, grease, and camp grime.
- Restrained dull Blood Axe red cloth tie or chipped paint on one accent area.

Palette targets:

- Wood: dark umber, scorched brown, dirty ochre, ash-stained tan.
- Metal: charcoal black, dark gunmetal, worn dull steel.
- Leather/hide: smoked tan, dark brown, soot black.
- Blood Axe accent: oxide red, faded maroon, chipped dark red.

No emissive material is approved for baseline `A01`.

## Concept Image Prompt

Create an original stylized fantasy MMORPG concept image of `SM_GIA_BloodAxeMalletPair_A01` for the world of Aerathea. The design should emphasize two oversized Giant-scale utility mallets, crossed or leaned shelter-edge arrangement, thick blunt heads, long worn handles, blackened iron bands, hide-wrapped grips, scorched hardwood, soot, ash, mud, one restrained chipped dull red accent, hostile Blood Axe Giant camp identity, clear separation from neutral/civilized Giant culture, female Giant scale 442 cm / 14'6", male Giant scale 470 cm / 15'5", and the gameplay role of static non-interactive shelter-edge utility dressing. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, no emissive glow, and MMO-friendly production design. Present it as a single prop production sheet with front, side, top, three-quarter, material swatches, LOD callouts, simple collision callouts, and scale markers. Avoid copying any existing franchise, avoid weapon-rack or combat presentation, avoid weapon-trace or pickup affordances, avoid harvest/crafting/resource/salvage language, avoid NPC work-loop diagrams, avoid physics or gate/destructible diagrams, avoid implementation-target claims, and avoid excessive micro-detail that would not translate to a mid-poly Unreal asset.

Concept source note: this package references `BloodAxeShelter.png#CampTools_MalletPair_A01` only through existing intake documentation. It does not copy, move, crop, edit, embed, inspect for final approval, or commit external source concept art.

## Modeling Notes

Future modeling guidance only:

- Build two mallets as one static display mesh only if the paired arrangement is needed for dressing.
- Keep enough negative space between handles and heads that the pair reads cleanly.
- Use different head widths or band layouts to avoid mirrored duplication.
- Keep the arrangement stable for ground or lean placement without physics simulation.
- Use broad bands and wraps as geometry only where they support silhouette.

Do not create DCC source, sculpt, retopo, UVs, bakes, collision proxies, proof renders, LOD source, FBX exports, Unreal assets, sockets, skeletal attachments, runtime files, validators, startup placement, NPC work-loop setup, physics constraints, or implementation targets from this task.

## Texture and Material Notes

Target material strategy:

- Material slots: 1 preferred, 2 maximum for wood/metal separation.
- Texture set: 1K target for the pair, 512 allowed for distant repeats.
- Required future maps: Base Color (`BC`), Normal (`N`), packed Occlusion/Roughness/Metallic (`ORM`).
- No emissive texture for baseline `A01`.

Suggested future names:

- `MI_GIA_BloodAxeMalletPair_A01`
- `T_GIA_BloodAxeMalletPair_A01_BC`
- `T_GIA_BloodAxeMalletPair_A01_N`
- `T_GIA_BloodAxeMalletPair_A01_ORM`

Use texture and normal detail for wood grain, soot, mud, ash, scratches, leather wear, small cracks, iron pitting, chipped red paint, and grime around ground contact.

## Triangle Budget

Target as a medium static paired prop:

- LOD0: 1,800-5,000 tris.
- Preferred A01 LOD0 range: 2,200-3,800 tris.
- LOD1: 900-2,300 tris.
- LOD2: 360-1,100 tris.
- LOD3: 140-420 tris.
- Material slots: 1 target, 2 maximum.

Spend geometry on the two head silhouettes, handles, broad bands, wraps, end caps, and the crossed/leaned footprint. Do not spend geometry on fine wood grain, small cracks, scratches, soot speckles, mud flecks, leather pores, or tiny rivets.

## LOD Plan

All future shipping-quality mesh work requires LOD0-LOD3.

- LOD0: full paired arrangement, both heads, handles, bands, wraps, end caps, major dents, and display footprint.
- LOD1: 55-65 percent of LOD0; reduce bevel loops, wrap folds, minor dents, and hidden contact faces.
- LOD2: 25-40 percent of LOD0; preserve two-mallet read, crossed/leaned silhouette, and major bands while simplifying wraps.
- LOD3: 10-20 percent of LOD0; preserve two blunt head shapes, long handle diagonals, and one strong material accent.

Remove fine scratches, soot flecks, paint chips, pitting, small cracks, mud flecks, and leather pores before reducing the paired silhouette.

## Collision Notes

Collision is planning-only:

- Preferred default: collision disabled for decorative shelter clutter.
- If blocking is later required: one simple low-count convex hull around the display footprint.
- No per-mallet, per-handle, per-band, per-wrap, weapon trace, or lean-physics collision.

Do not create pickup collision, weapon traces, harvest volumes, crafting interaction volumes, salvage/resource triggers, NPC work-loop volumes, physics bodies, gate logic collision, destructible fracture collision, nav blockers, runtime gameplay collision, or Unreal collision proxies from this package.

## Animation Notes

Baseline asset is static. No animation, physics simulation, mallet swing, tool use, weapon use, weapon trace, pickup behavior, crafting loop, harvesting state, salvage state, resource state, NPC work loop, socket attachment, skeletal attachment, gate operation, destructible state, VFX, audio, material-state timing, or Blueprint behavior is planned.

Any active, held, socketed, usable, craftable, harvest-linked, physics-enabled, NPC-operated, or combat mallet pair must become a separate approval-gated package.

## Unreal Import Notes

Future Unreal import guidance only:

- Asset type: Static Mesh.
- Suggested Unreal path: `/Game/Aerathea/Props/Giants/BloodAxeCamp/CampTools/SM_GIA_BloodAxeMalletPair_A01`
- Import scale: 1.0; authored in centimeters.
- Pivot: ground center of display footprint for crossed or leaned placement.
- Orientation: display variant rests or leans in authored pose, Z up.
- Collision: disabled by default or one simple low hull only if later layout work requires it.
- LODs: import LOD0-LOD3 when authored by a future DCC lane.
- Material slots: 1 preferred, 2 maximum.
- Sockets: none.
- Blueprint behavior: none.

Do not import, place, create materials, create textures, add sockets, define Blueprints, run startup placement, create validators, or select an implementation target from this package.

## Folder and Naming Recommendation

Documentation path:

- `docs/assets/props/SM_GIA_BloodAxeMalletPair_A01/PRODUCTION_PACKAGE.md`

Future naming, if separately approved:

- Static Mesh: `SM_GIA_BloodAxeMalletPair_A01`
- Material Instance: `MI_GIA_BloodAxeMalletPair_A01`
- Textures: `T_GIA_BloodAxeMalletPair_A01_BC`, `T_GIA_BloodAxeMalletPair_A01_N`, `T_GIA_BloodAxeMalletPair_A01_ORM`

These are recommendations only and do not create source folders, exports, Unreal Content, runtime source, first DCC target selection, or implementation target selection.

## Quality Gate Checklist

- Uses the female 442 cm / 14'6" and male 470 cm / 15'5" Giant scale lock.
- Reads as Blood Axe hostile Giant sub-faction dressing, separate from neutral/civilized Giant culture.
- Keeps the mallet pair as static shelter-edge utility dressing, not a weapon rack or pickup set.
- Avoids pickup affordances, weapon traces, sockets, skeletal attachment, physics claims, and NPC work-loop claims.
- Includes Base Color, Normal, and packed ORM texture planning.
- Includes LOD0-LOD3 and simple display collision guidance.
- Keeps emissive, harvest logic, crafting logic, salvage logic, resource logic, pickup behavior, weapon traces, NPC work loops, physics, gate/destructible behavior, DCC, Unreal, validators, source assets, and implementation targets out of scope.
