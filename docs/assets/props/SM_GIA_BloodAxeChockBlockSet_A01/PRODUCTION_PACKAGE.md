# SM_GIA_BloodAxeChockBlockSet_A01 Production Package

## Art Direction Summary

- Asset name: `SM_GIA_BloodAxeChockBlockSet_A01`
- Asset type: Static Mesh prop production package, docs-only
- Parent kit: `KIT_GIA_BloodAxeCampTools_A01`
- Child intake row: `BloodAxeStronghold.png#CampTools_ChockBlocks_A01`
- Faction/theme: Blood Axe Tribe, hostile Giant sub-faction only
- Status: docs-only production package ready

`SM_GIA_BloodAxeChockBlockSet_A01` is a set of heavy wood and metal chock blocks used as static Blood Axe stronghold and barricade dressing. The set should read as blunt support props: battered triangular blocks, scorched timber, blackened iron caps, mud-dark undersides, and crude red marks.

Blood Axe visual language must remain separate from neutral/civilized Giant culture. Do not use refined highland carpentry, cave-town civic marks, blue-gray carved stone, peaceful hearth storage, terrace craft, or restrained blue rune identity.

Guardrails: no-DCC, no-Unreal, no-harvest, no-crafting, no-salvage, no-resource, no-weapon-trace, no-pickup, no-NPC-work-loop, no-physics, no-gate/destructible, no-implementation-target. This package is planning documentation only and does not authorize source assets, FBX, Unreal Content, runtime source, validators, external concept movement, final visual approval, or first DCC target selection.

## Gameplay Purpose

Static visual support props only:

- Dressing near barricades, wagons, gates, palisade repairs, rough platforms, and stronghold clutter.
- Scale markers for hostile Giant camp hardware beside female 442 cm / 14'6" and male 470 cm / 15'5" Giants.
- Non-interactive environmental storytelling for crude Blood Axe support work.

The chocks do not define gate logic, destructible logic, physics constraints, wheel blocking, resource nodes, salvage, crafting, pickup behavior, weapon traces, NPC work loops, nav rules, or interaction prompts.

## Silhouette Notes

Primary read: two to four oversized chock blocks with blunt wedge profiles, flat ground contact, and heavy backs.

Required silhouette features:

- Broad triangular or trapezoid side profiles.
- Thick squared backs and flattened undersides.
- Wood chocks with metal cap variants, or metal chocks with scorched wood spacers.
- Simple leaning or paired arrangement that reads as camp support clutter.
- Optional dull red slash, hide wrap, or black iron staple as a restrained Blood Axe accent.

Model main block volumes, metal caps, large straps, broad bevels, and major silhouette gouges. Use textures for wood grain, soot, ash, small cracks, scratches, pitting, mud, chipped paint, and leather stitching.

Avoid engineered machinery, refined gate hardware, animated constraint parts, wheel physics components, puzzle props, quest markers, clean workshop blocks, and neutral/civilized Giant material language.

## Scale Notes

Use the validated `SK_GIA_Base_A01` scale lock:

- Female Giant baseline: 442 cm / 14'6".
- Male Giant baseline: 470 cm / 15'5".
- Approved Giant ranges: females 14-15 ft / 427-457 cm; males 14'10"-16'0" / 452-488 cm.
- Author future source in centimeters. 1 Unreal unit equals 1 cm.

Recommended dimensions:

- Individual chock length: 80-180 cm.
- Individual chock height: 35-90 cm.
- Individual chock width: 45-120 cm.
- Set footprint: 180-420 cm wide, 120-300 cm deep, 40-130 cm tall.
- Forms should feel usable by Giant hands while remaining low-profile camp dressing.

## Materials and Color Palette

Primary materials:

- Scorched timber, rough hardwood, cracked block faces, and mud-dark undersides.
- Blackened iron caps, dark steel straps, crude staples, and hammered plates.
- Hide lashings, dirty leather wraps, soot, ash, grease, and dried mud.
- Restrained dull Blood Axe red paint, cloth, or warning slash.

Palette targets:

- Wood: charred umber, dark brown, dirty ochre, ash tan.
- Metal: charcoal black, dark gunmetal, worn dull steel.
- Blood Axe accent: oxide red, faded maroon, chipped red paint.
- Grime: soot black, ash gray, dried mud brown.

No emissive material is approved for baseline `A01`.

## Concept Image Prompt

Create an original stylized fantasy MMORPG concept image of `SM_GIA_BloodAxeChockBlockSet_A01` for the world of Aerathea. The design should emphasize oversized Giant-scale chock blocks, blunt wedge and trapezoid silhouettes, scorched timber, blackened iron caps, dark steel straps, hide lashings, mud-dark undersides, soot, ash, chipped dull red paint, hostile Blood Axe Giant stronghold identity, clear separation from neutral/civilized Giant culture, female Giant scale 442 cm / 14'6", male Giant scale 470 cm / 15'5", and the gameplay role of static non-interactive support dressing. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, no emissive glow, and MMO-friendly production design. Present it as a single prop production sheet with front, side, top, three-quarter, material swatches, LOD callouts, simple collision callouts, and scale markers. Avoid copying any existing franchise, avoid refined Giant carpentry, avoid gate logic or destructible diagrams, avoid harvest/crafting/resource/salvage language, avoid pickup or weapon-trace presentation, avoid physics constraints, avoid implementation-target claims, and avoid excessive micro-detail that would not translate to a mid-poly Unreal asset.

Concept source note: this package references `BloodAxeStronghold.png#CampTools_ChockBlocks_A01` only through existing intake documentation. It does not copy, move, crop, edit, embed, inspect for final approval, or commit external source concept art.

## Modeling Notes

Future modeling guidance only:

- Build two to four chock variants with clear wedge or trapezoid profiles.
- Include wood-heavy and metal-capped variants if material separation remains low cost.
- Keep the block backs thick and the undersides flattened for stable set dressing.
- Add a few large gouges or chipped corners as silhouette detail.
- Keep straps, staples, and ties broad enough to read from gameplay distance.

Do not create DCC source, sculpt, retopo, UVs, bakes, collision proxies, proof renders, LOD source, FBX exports, Unreal assets, sockets, runtime files, validators, startup placement, physics constraints, or implementation targets from this task.

## Texture and Material Notes

Target material strategy:

- Material slots: 1 preferred, 2 maximum for wood/metal separation.
- Texture set: 512-1K.
- Required future maps: Base Color (`BC`), Normal (`N`), packed Occlusion/Roughness/Metallic (`ORM`).
- No emissive texture for baseline `A01`.

Suggested future names:

- `MI_GIA_BloodAxeChockBlockSet_A01`
- `T_GIA_BloodAxeChockBlockSet_A01_BC`
- `T_GIA_BloodAxeChockBlockSet_A01_N`
- `T_GIA_BloodAxeChockBlockSet_A01_ORM`

Use texture and normal detail for wood grain, soot, mud, ash, scratches, leather wear, small cracks, iron pitting, chipped red paint, and grime around ground contact.

## Triangle Budget

Target as a small-to-medium static prop set:

- LOD0: 900-3,200 tris.
- Preferred A01 LOD0 range: 1,300-2,600 tris.
- LOD1: 500-1,500 tris.
- LOD2: 220-760 tris.
- LOD3: 90-280 tris.
- Material slots: 1 target, 2 maximum.

Spend geometry on chock silhouettes, metal caps, thick straps, large gouges, and set footprint. Do not spend geometry on wood grain, fine cracks, scratches, pitting, soot speckles, mud flecks, or tiny stitch lines.

## LOD Plan

All future shipping-quality mesh work requires LOD0-LOD3.

- LOD0: full block profiles, metal caps, straps, broad bevels, major chips, and full set footprint.
- LOD1: 55-65 percent of LOD0; reduce bevel loops, hidden underside faces, small gouges, and strap subdivisions.
- LOD2: 25-40 percent of LOD0; preserve wedge/trapezoid silhouettes and large cap shapes while simplifying backside detail.
- LOD3: 10-20 percent of LOD0; preserve simple chock block mass and ground footprint.

Remove small cracks, scratches, soot flecks, paint chips, pitting, stitching, and mud flecks before reducing primary block silhouettes.

## Collision Notes

Collision is planning-only:

- Preferred default: collision disabled for decorative support clutter.
- If blocking is later required: one simple box or low-count convex hull around the set.
- No per-strap, per-chip, per-gap, wheel-contact, hinge, gate, or destructible collision.

Do not create physics constraints, gate logic collision, destructible fracture collision, pickup collision, harvest volumes, crafting interaction volumes, salvage/resource triggers, weapon traces, NPC work-loop volumes, nav blockers, runtime gameplay collision, or Unreal collision proxies from this package.

## Animation Notes

Baseline asset is static. No animation, physics simulation, wheel blocking, gate operation, destructible state, crafting use, harvesting state, salvage state, resource state, pickup behavior, weapon use, NPC work loop, VFX, audio, material-state timing, or Blueprint behavior is planned.

Any active support prop, destructible gate prop, physics chock, craftable resource, or gameplay-linked variant must become a separate approval-gated package.

## Unreal Import Notes

Future Unreal import guidance only:

- Asset type: Static Mesh.
- Suggested Unreal path: `/Game/Aerathea/Props/Giants/BloodAxeCamp/CampTools/SM_GIA_BloodAxeChockBlockSet_A01`
- Import scale: 1.0; authored in centimeters.
- Pivot: ground center of the full set footprint.
- Orientation: chocks rest on XY ground plane, Z up.
- Collision: disabled by default or one low hull only if later layout work requires it.
- LODs: import LOD0-LOD3 when authored by a future DCC lane.
- Material slots: 1 preferred, 2 maximum.
- Sockets: none.
- Blueprint behavior: none.

Do not import, place, create materials, create textures, define Blueprints, add sockets, run startup placement, create validators, or select an implementation target from this package.

## Folder and Naming Recommendation

Documentation path:

- `docs/assets/props/SM_GIA_BloodAxeChockBlockSet_A01/PRODUCTION_PACKAGE.md`

Future naming, if separately approved:

- Static Mesh: `SM_GIA_BloodAxeChockBlockSet_A01`
- Material Instance: `MI_GIA_BloodAxeChockBlockSet_A01`
- Textures: `T_GIA_BloodAxeChockBlockSet_A01_BC`, `T_GIA_BloodAxeChockBlockSet_A01_N`, `T_GIA_BloodAxeChockBlockSet_A01_ORM`

These are recommendations only and do not create source folders, exports, Unreal Content, runtime source, first DCC target selection, or implementation target selection.

## Quality Gate Checklist

- Uses the female 442 cm / 14'6" and male 470 cm / 15'5" Giant scale lock.
- Reads as Blood Axe hostile Giant sub-faction dressing, separate from neutral/civilized Giant culture.
- Keeps the chock silhouettes blunt, broad, low, and readable.
- Avoids physics constraints, gate logic, destructible behavior, refined carpentry, and puzzle-prop reads.
- Includes Base Color, Normal, and packed ORM texture planning.
- Includes LOD0-LOD3 and simple display collision guidance.
- Keeps emissive, harvest logic, crafting logic, salvage logic, resource logic, pickup behavior, weapon traces, NPC work loops, physics, gate/destructible behavior, DCC, Unreal, validators, source assets, and implementation targets out of scope.
