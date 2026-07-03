# SM_GIA_BloodAxeWedgeSet_A01 Production Package

## Art Direction Summary

- Asset name: `SM_GIA_BloodAxeWedgeSet_A01`
- Asset type: Static Mesh prop production package, docs-only
- Parent kit: `KIT_GIA_BloodAxeCampTools_A01`
- Child intake row: `BloodAxeCamp.png#CampTools_WedgeSet_A01`
- Faction/theme: Blood Axe Tribe, hostile Giant sub-faction only
- Status: docs-only production package ready

`SM_GIA_BloodAxeWedgeSet_A01` is a small set of oversized blunt splitting wedges and chock-like utility wedges for Blood Axe camp dressing. The set should read as crude, heavy, soot-dark, and practical for hostile Giant raiders, with broad triangular forms visible from MMO camera distance.

Blood Axe visual language must remain a hostile Giant sub-faction identity, separate from neutral/civilized Giant culture. Do not use civilized Giant cave-town masonry, refined stoneworker craft, peaceful highland tools, warm hearth presentation, blue-gray civic stone, or restrained blue rune language.

Guardrails: no-DCC, no-Unreal, no-harvest, no-crafting, no-salvage, no-resource, no-weapon-trace, no-pickup, no-NPC-work-loop, no-physics, no-gate/destructible, no-implementation-target. This package does not authorize source assets, FBX exports, Unreal Content, runtime source, validators, external concept movement, final visual approval, or first DCC target selection.

## Gameplay Purpose

Static environmental storytelling only:

- Camp utility dressing near tool buckets, rope coils, forge support clutter, barricade repairs, path edges, and shelter work areas.
- Visual scale support beside female 442 cm / 14'6" and male 470 cm / 15'5" Giants.
- Non-interactive evidence of rough Blood Axe camp maintenance.
- Reusable ground clutter that breaks up mud and ash surfaces without becoming loot, a resource node, a crafting ingredient, or a harvest target.

No gameplay behavior is defined. The wedges are not weapons, pickups, crafting inputs, salvage items, gate blockers, destructible supports, physics props, NPC work-loop targets, or interaction objects.

## Silhouette Notes

Primary read: three to five broad blunt triangular wedges, with varied lengths, chipped corners, and heavy ground contact.

Required silhouette features:

- Oversized wedge bodies with thick backs and broad striking faces.
- One or two low stacked pairs for readable camp clutter.
- One loose wedge set at a slight angle to avoid a clean workshop read.
- Chipped and battered large edges as geometry only where silhouette-relevant.
- Optional dull red paint slash, cloth tie, or iron band as a restrained Blood Axe accent.

Model the main wedge masses, thick bevels, large chips, metal bands, and ground-contact shapes as geometry. Paint or normal-map small scratches, pitting, soot, ash, dents, minor red paint loss, and fine cracks.

Avoid thin carpenter wedges, refined tool-shop precision, treasure bars, sharpened weapon blades, magic markers, UI arrows, readable labels, excessive red decoration, and neutral/civilized Giant craft language.

## Scale Notes

Use the validated `SK_GIA_Base_A01` scale lock:

- Female Giant baseline: 442 cm / 14'6".
- Male Giant baseline: 470 cm / 15'5".
- Approved Giant ranges: females 14-15 ft / 427-457 cm; males 14'10"-16'0" / 452-488 cm.
- Author future source in centimeters. 1 Unreal unit equals 1 cm.

Recommended dimensions:

- Individual wedge length: 50-140 cm.
- Individual wedge height: 25-70 cm.
- Individual wedge width: 30-90 cm.
- Small set footprint: 160-360 cm wide, 100-260 cm deep, 25-95 cm tall.
- Striking faces should be large enough to read as Giant-scale tools, not ordinary humanoid props scaled up.

## Materials and Color Palette

Primary materials:

- Blackened iron, dark steel, dull hammered metal, or scorched hardwood.
- Soot, ash, mud, grease, charcoal dust, and chipped camp grime.
- Optional hide strap, crude iron band, or dull red cloth tie.
- Sparse non-graphic bone or horn spacer only if needed as a hostile accent.

Palette targets:

- Metal: charcoal black, dark gunmetal, soot gray, worn steel edge.
- Wood: scorched umber, dark brown, ash-stained tan.
- Blood Axe accent: deep oxide red, faded maroon, chipped dark red.
- Grounding dirt: dried mud brown, ash gray, black soot.

No emissive material is approved for baseline `A01`.

## Concept Image Prompt

Create an original stylized fantasy MMORPG concept image of `SM_GIA_BloodAxeWedgeSet_A01` for the world of Aerathea. The design should emphasize oversized blunt Blood Axe Giant splitting wedges, broad triangular silhouettes, heavy striking faces, low stacked and loose variants, blackened iron, dark steel, scorched hardwood, soot, ash, mud, chipped dull red paint, hostile Giant raider camp identity, clear separation from neutral/civilized Giant culture, female Giant scale 442 cm / 14'6", male Giant scale 470 cm / 15'5", and the gameplay role of static non-interactive camp utility dressing. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, no emissive glow, and MMO-friendly production design. Present it as a single prop production sheet with front, side, top, three-quarter, material swatches, LOD callouts, simple collision callouts, and scale markers. Avoid copying any existing franchise, avoid refined Giant craft, avoid harvest/crafting/resource/salvage language, avoid pickup or weapon-trace presentation, avoid physics or gate/destructible diagrams, avoid implementation-target claims, and avoid excessive micro-detail that would not translate to a mid-poly Unreal asset.

Concept source note: this package references `BloodAxeCamp.png#CampTools_WedgeSet_A01` only through existing intake documentation. It does not copy, move, crop, edit, embed, inspect for final approval, or commit external source concept art.

## Modeling Notes

Future modeling guidance only:

- Build three to five reusable wedge variants and one small stacked arrangement.
- Use chunky proportions with blunt tips, thick backs, and readable ground contact.
- Add large bevels and a few silhouette chips; keep fine damage in textures.
- Use asymmetry so the set reads field-made rather than refined.
- Include optional large iron bands or hide ties only when they support scale and silhouette.

Do not create mesh files, Blender files, collision proxies, LOD source, proof renders, FBX exports, Unreal assets, sockets, runtime files, validators, or startup placement from this task.

## Texture and Material Notes

Target material strategy:

- Material slots: 1 preferred, 2 maximum if metal and wood variants need separation.
- Texture set: 512-1K for repeated camp dressing.
- Required future maps: Base Color (`BC`), Normal (`N`), packed Occlusion/Roughness/Metallic (`ORM`).
- No emissive texture for baseline `A01`.

Suggested future names:

- `MI_GIA_BloodAxeWedgeSet_A01`
- `T_GIA_BloodAxeWedgeSet_A01_BC`
- `T_GIA_BloodAxeWedgeSet_A01_N`
- `T_GIA_BloodAxeWedgeSet_A01_ORM`

Use textures and normals for soot speckles, iron pitting, fine scratches, small chips, ash flecks, mud, wood grain, rubbed red paint, and leather wear.

## Triangle Budget

Target as a small static prop set:

- LOD0: 800-3,000 tris.
- Preferred A01 LOD0 range: 1,200-2,400 tris.
- LOD1: 450-1,400 tris.
- LOD2: 180-700 tris.
- LOD3: 80-260 tris.
- Material slots: 1 target, 2 maximum.

Spend geometry on wedge bodies, blunt triangular profiles, thick backs, silhouette chips, major bands, and stacked contact. Do not spend geometry on tiny scratches, pitting, mud grains, soot flecks, small dents, or micro cracks.

## LOD Plan

All future shipping-quality mesh work requires LOD0-LOD3.

- LOD0: full wedge bodies, stacked offsets, large bevels, major chips, broad bands or ties, and full ground footprint.
- LOD1: 55-65 percent of LOD0; reduce bevel loops, hidden contact faces, minor chips, and underside detail.
- LOD2: 25-40 percent of LOD0; preserve the wedge silhouettes and stacked read while simplifying backs and contact faces.
- LOD3: 10-20 percent of LOD0; preserve broad triangular shapes and the set footprint.

Remove tiny damage, fine paint loss, soot speckles, mud flecks, pitting, and non-silhouette chips before reducing the primary wedge profiles.

## Collision Notes

Collision is planning-only:

- Preferred default: collision disabled for decorative ground clutter.
- If blocking is later required: one simple box or low-count convex hull per wedge group.
- No per-chip, per-band, per-stack-gap, or sharp-edge collision.

Do not create pickup collision, harvest volumes, crafting interaction volumes, resource triggers, salvage triggers, weapon traces, NPC work-loop volumes, physics bodies, gate logic collision, destructible fracture collision, nav blockers, runtime gameplay collision, or Unreal collision proxies from this package.

## Animation Notes

Baseline asset is static. No animation, physics simulation, moving parts, destructible state, wedge sliding, gate blocking, crafting loop, harvesting state, salvage state, pickup behavior, weapon use, NPC work loop, VFX, audio, material-state timing, or Blueprint behavior is planned.

Any moving, usable, craftable, salvageable, destructible, physics-enabled, or gameplay-linked wedge must become a separate approval-gated package.

## Unreal Import Notes

Future Unreal import guidance only:

- Asset type: Static Mesh.
- Suggested Unreal path: `/Game/Aerathea/Props/Giants/BloodAxeCamp/CampTools/SM_GIA_BloodAxeWedgeSet_A01`
- Import scale: 1.0; authored in centimeters.
- Pivot: ground center of the full set footprint.
- Orientation: wedges rest on XY ground plane, Z up.
- Collision: disabled by default or simple low hull only if later layout work requires it.
- LODs: import LOD0-LOD3 when authored by a future DCC lane.
- Material slots: 1 preferred, 2 maximum.
- Sockets: none.
- Blueprint behavior: none.

Do not import, place, create materials, create textures, add sockets, define Blueprints, run startup placement, create validators, or select an implementation target from this package.

## Folder and Naming Recommendation

Documentation path:

- `docs/assets/props/SM_GIA_BloodAxeWedgeSet_A01/PRODUCTION_PACKAGE.md`

Future naming, if separately approved:

- Static Mesh: `SM_GIA_BloodAxeWedgeSet_A01`
- Material Instance: `MI_GIA_BloodAxeWedgeSet_A01`
- Textures: `T_GIA_BloodAxeWedgeSet_A01_BC`, `T_GIA_BloodAxeWedgeSet_A01_N`, `T_GIA_BloodAxeWedgeSet_A01_ORM`

These are recommendations only and do not create source folders, exports, Unreal Content, runtime source, first DCC target selection, or implementation target selection.

## Quality Gate Checklist

- Uses the female 442 cm / 14'6" and male 470 cm / 15'5" Giant scale lock.
- Reads as Blood Axe hostile Giant sub-faction dressing, separate from neutral/civilized Giant culture.
- Keeps the wedge silhouettes blunt, broad, and readable.
- Assigns micro damage, soot, pitting, mud, and fine scratches to textures or normals.
- Includes Base Color, Normal, and packed ORM texture planning.
- Includes LOD0-LOD3 and simple display collision guidance.
- Keeps emissive, magic, UI markers, pickup language, harvest logic, crafting logic, salvage logic, resource logic, weapon traces, NPC work loops, physics, gate/destructible behavior, DCC, Unreal, validators, source assets, and implementation targets out of scope.
