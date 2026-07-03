# SM_GIA_BloodAxeIronWedgeStack_A01 Production Package

## Art Direction Summary

- Asset name: `SM_GIA_BloodAxeIronWedgeStack_A01`
- Asset type: Static Mesh prop production package, docs-only
- Parent kit: `KIT_GIA_BloodAxeCampTools_A01`
- Child intake row: `BloodAxeForge.png#CampTools_IronWedgeStack_A01`
- Faction/theme: Blood Axe Tribe, hostile Giant sub-faction only
- Status: docs-only production package ready

`SM_GIA_BloodAxeIronWedgeStack_A01` is a forge-adjacent stack of dark iron wedges used as static Blood Axe camp utility dressing. It should feel brutally practical: heavy blackened metal, broad triangular chunks, soot, ash, chipped red marks, and a low compact stack sized for Giant hands.

Blood Axe visual language must stay separate from neutral/civilized Giant culture. Do not use refined stoneworker craft, peaceful highland tooling, cave-town civic marks, blue-gray carved stone, warm hearth presentation, or restrained blue rune motifs.

Guardrails: no-DCC, no-Unreal, no-harvest, no-crafting, no-salvage, no-resource, no-weapon-trace, no-pickup, no-NPC-work-loop, no-physics, no-gate/destructible, no-implementation-target. This package is planning documentation only and does not authorize source assets, FBX, Unreal Content, runtime source, validators, external concept movement, final visual approval, or first DCC target selection.

## Gameplay Purpose

Static display support for Blood Axe forge and camp work areas:

- Forge-adjacent clutter beside anvils, scrap sorting areas, tool buckets, mallets, and rough repair zones.
- Scale reinforcement for female 442 cm / 14'6" and male 470 cm / 15'5" Giants.
- Environmental storytelling for crude Blood Axe maintenance without creating a resource pile, salvage pile, loot stack, crafting ingredient, or usable forge station.

The stack is not a harvest node, crafting source, salvage source, pickup object, economy prop, weapon, physics object, gate support, destructible blocker, or NPC work-loop target.

## Silhouette Notes

Primary read: a low pile of three to six heavy iron wedges with strong triangular profiles and visible stacked offsets.

Required silhouette features:

- Thick wedge bodies with blunt points and battered backs.
- Alternating offsets so each wedge remains readable.
- One larger base wedge anchoring the stack.
- Broad chipped corners and hammered faces.
- Optional crude iron band, oxide-red paint slash, or soot-black tie mark as a secondary accent.

Model wedge masses, large bevels, silhouette chips, broad hammered planes, and stack contact. Use textures for pitting, soot, ash, scratches, small dents, heat discoloration, and chipped red paint.

Avoid ingot stacks, treasure bars, refined blacksmith display, sharp weapon blades, glowing hot metal, crafting UI readability, harvest-node presentation, and neutral/civilized Giant craft.

## Scale Notes

Use the validated `SK_GIA_Base_A01` scale lock:

- Female Giant baseline: 442 cm / 14'6".
- Male Giant baseline: 470 cm / 15'5".
- Approved Giant ranges: females 14-15 ft / 427-457 cm; males 14'10"-16'0" / 452-488 cm.
- Author future source in centimeters. 1 Unreal unit equals 1 cm.

Recommended dimensions:

- Individual iron wedge length: 70-150 cm.
- Individual wedge height: 30-80 cm.
- Stack footprint: 170-380 cm wide, 120-280 cm deep.
- Stack height: 60-160 cm.
- Major edge thickness should read clearly from MMO camera distance.

## Materials and Color Palette

Primary materials:

- Blackened iron, dark steel, dull hammered metal, soot-dark wedge faces.
- Ash, charcoal dust, forge grime, oil-dark stains, and mud.
- Chipped dull red paint or oxide markings used sparingly.
- Optional scorched wood spacer or hide strap only if it supports the stack read.

Palette targets:

- Metal: charcoal black, dark gunmetal, oxidized gray, worn dull steel.
- Forge grime: ash gray, soot black, oil brown, dark mud.
- Blood Axe accent: deep oxide red, dark maroon, chipped red paint.

No emissive, hot-metal glow, forge glow, ritual glow, or magic glow is approved for baseline `A01`.

## Concept Image Prompt

Create an original stylized fantasy MMORPG concept image of `SM_GIA_BloodAxeIronWedgeStack_A01` for the world of Aerathea. The design should emphasize a compact stack of oversized dark iron wedges, blunt triangular profiles, battered backs, hammered blackened metal, soot, ash, oil-dark grime, chipped dull red paint, hostile Blood Axe Giant forge-camp identity, clear separation from neutral/civilized Giant culture, female Giant scale 442 cm / 14'6", male Giant scale 470 cm / 15'5", and the gameplay role of static non-interactive forge-adjacent utility dressing. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, no emissive glow, and MMO-friendly production design. Present it as a single prop production sheet with top, side, three-quarter, material swatches, LOD callouts, collision callouts, and scale markers. Avoid copying any existing franchise, avoid hot glowing metal, avoid harvest/crafting/resource/salvage language, avoid pickup or weapon-trace presentation, avoid physics or gate/destructible diagrams, avoid implementation-target claims, and avoid excessive micro-detail that would not translate to a mid-poly Unreal asset.

Concept source note: this package references `BloodAxeForge.png#CampTools_IronWedgeStack_A01` only through existing intake documentation. It does not copy, move, crop, edit, embed, inspect for final approval, or commit external source concept art.

## Modeling Notes

Future modeling guidance only:

- Build the stack from three to six distinct wedge forms, reusing geometry where practical.
- Keep the pile stable, low, and readable rather than messy.
- Use broad bevels and a few silhouette chips; avoid dense micro damage.
- Offset wedges so the triangular profile remains visible from front and top views.
- Keep underside contact simple for easy placement on rough camp ground.

Do not create DCC source, sculpt, retopo, UVs, bakes, collision proxies, proof renders, LOD source, FBX exports, Unreal assets, sockets, runtime files, validators, startup placement, or implementation targets from this task.

## Texture and Material Notes

Target material strategy:

- Material slots: 1 preferred using a shared Blood Axe blackened metal material.
- Texture set: 512-1K.
- Required future maps: Base Color (`BC`), Normal (`N`), packed Occlusion/Roughness/Metallic (`ORM`).
- No emissive texture for baseline `A01`.

Suggested future names:

- `MI_GIA_BloodAxeIronWedgeStack_A01`
- `T_GIA_BloodAxeIronWedgeStack_A01_BC`
- `T_GIA_BloodAxeIronWedgeStack_A01_N`
- `T_GIA_BloodAxeIronWedgeStack_A01_ORM`

Packed `ORM` should carry strong occlusion between stacked wedges, high roughness for soot and ash, and metallic only on iron surfaces.

## Triangle Budget

Target as a small-to-medium static prop:

- LOD0: 1,200-3,500 tris.
- Preferred A01 LOD0 range: 1,600-2,800 tris.
- LOD1: 650-1,700 tris.
- LOD2: 250-850 tris.
- LOD3: 100-320 tris.
- Material slots: 1 target, 2 maximum.

Spend geometry on wedge silhouettes, stack offsets, large bevels, and readable battered backs. Do not spend geometry on fine pitting, soot, scratches, ash flecks, chipped paint specks, or tiny dents.

## LOD Plan

All future shipping-quality mesh work requires LOD0-LOD3.

- LOD0: full stack offsets, individual wedge profiles, major chips, bevels, and contact shadows.
- LOD1: 55-65 percent of LOD0; reduce bevel loops, backside cuts, small chips, and hidden contact faces.
- LOD2: 25-40 percent of LOD0; merge minor wedge separation while preserving stack silhouette and triangular reads.
- LOD3: 10-20 percent of LOD0; preserve low pile footprint and two or three dominant wedge angles.

Remove small pitting, scratches, soot flecks, ash marks, and minor chips before reducing the primary stacked form.

## Collision Notes

Collision is planning-only:

- Preferred default: collision disabled for decorative forge clutter.
- If blocking is later required: one simple box or low-count convex hull around the full stack.
- No per-wedge, per-gap, per-chip, or sharp-edge collision.

Do not create harvest volumes, crafting interaction volumes, salvage/resource triggers, pickup collision, weapon traces, NPC work-loop volumes, physics bodies, gate logic collision, destructible fracture collision, nav blockers, runtime gameplay collision, or Unreal collision proxies from this package.

## Animation Notes

Baseline asset is static. No animation, physics simulation, loose wedge settling, crafting use, harvesting state, salvage state, resource state, pickup behavior, weapon use, gate logic, destructible state, NPC work loop, VFX, audio, material-state timing, or Blueprint behavior is planned.

Any active, usable, salvageable, craftable, destructible, physics-enabled, or gameplay-linked iron wedge stack must become a separate approval-gated package.

## Unreal Import Notes

Future Unreal import guidance only:

- Asset type: Static Mesh.
- Suggested Unreal path: `/Game/Aerathea/Props/Giants/BloodAxeCamp/CampTools/SM_GIA_BloodAxeIronWedgeStack_A01`
- Import scale: 1.0; authored in centimeters.
- Pivot: ground center of the stack footprint.
- Orientation: stack rests on XY ground plane, Z up.
- Collision: disabled by default or one low hull only if later layout work requires it.
- LODs: import LOD0-LOD3 when authored by a future DCC lane.
- Material slots: 1 preferred, 2 maximum.
- Sockets: none.
- Blueprint behavior: none.

Do not import, place, create materials, create textures, define Blueprints, add sockets, run startup placement, create validators, or select an implementation target from this package.

## Folder and Naming Recommendation

Documentation path:

- `docs/assets/props/SM_GIA_BloodAxeIronWedgeStack_A01/PRODUCTION_PACKAGE.md`

Future naming, if separately approved:

- Static Mesh: `SM_GIA_BloodAxeIronWedgeStack_A01`
- Material Instance: `MI_GIA_BloodAxeIronWedgeStack_A01`
- Textures: `T_GIA_BloodAxeIronWedgeStack_A01_BC`, `T_GIA_BloodAxeIronWedgeStack_A01_N`, `T_GIA_BloodAxeIronWedgeStack_A01_ORM`

These are recommendations only and do not create source folders, exports, Unreal Content, runtime source, first DCC target selection, or implementation target selection.

## Quality Gate Checklist

- Uses the female 442 cm / 14'6" and male 470 cm / 15'5" Giant scale lock.
- Reads as Blood Axe hostile Giant sub-faction dressing, separate from neutral/civilized Giant culture.
- Keeps the stack blunt, heavy, and readable from MMO camera distance.
- Avoids hot-metal glow, refined forge display, treasure reads, and crafting affordances.
- Includes Base Color, Normal, and packed ORM texture planning.
- Includes LOD0-LOD3 and simple display collision guidance.
- Keeps emissive, harvest logic, crafting logic, salvage logic, resource logic, pickup behavior, weapon traces, NPC work loops, physics, gate/destructible behavior, DCC, Unreal, validators, source assets, and implementation targets out of scope.
