# SM_GIA_BloodAxeRingPegSet_A01 Production Package

## Art Direction Summary

- Asset name: `SM_GIA_BloodAxeRingPegSet_A01`
- Asset type: Static Mesh prop set, docs-only production package
- Parent kit: `KIT_GIA_BloodAxeTieHardware_A01`
- Intake row: `BloodAxeGate.png#CampTools_RingPegSet_A01`
- Faction/theme: Blood Axe Tribe, hostile Giant sub-faction
- Status: package-ready planning sheet

`SM_GIA_BloodAxeRingPegSet_A01` defines ground pegs and ring anchors for Blood Axe camp perimeter visual dressing. It is static tie hardware for hostile Giant camps, not a rope-simulation setup, physics constraint, trap, objective device, pickup, weapon, or neutral/civilized Giant fixture.

This is a docs-only package. Guardrails: no DCC, no Unreal, no pickup, no weapon, no trap, no hanging physics, no rope simulation, no objective, no interaction, no implementation target.

## Gameplay Purpose

Static camp perimeter dressing only:

- Supports visual tie-down language near gates, shelters, banners, rope coils, and utility clusters.
- Gives large readable hardware scale beside female 442 cm / 14'6" and male 470 cm / 15'5" Giants.
- Provides a focused child package for ring-and-peg silhouettes from the broader tie-hardware kit.

Do not define rope simulation, physics constraints, trap behavior, objective logic, nav blockers, pickup/resource behavior, interaction prompts, DCC, Unreal Content, runtime source, validators, or implementation targets.

## Silhouette Notes

Primary read: blunt ground peg plus oversized ring anchor.

- Pegs should be thick, hammered, and partially mud-seated.
- Rings should be oval or circular with exaggerated thickness and broad inner negative space.
- Include 2-4 variants: single peg with ring, double peg pair, low ground ring plate, and loose spare peg set.
- Keep all points blunt and worn.
- Use one restrained dull red tie or chipped red mark per set at most.

Avoid spear, spike trap, bear-trap, objective marker, pickup outline, weapon head, polished shackle, dense chain, or refined neutral/civilized Giant reads.

## Scale Notes

- Female Giant baseline: 442 cm / 14'6".
- Male Giant baseline: 470 cm / 15'5".
- Approved Giant ranges: females 14-15 ft / 427-457 cm; males 14'10"-16'0" / 452-488 cm.
- Author in centimeters. 1 Unreal unit = 1 cm.

Target sizes:

- Peg length: 90-180 cm.
- Peg thickness: 14-35 cm.
- Exposed peg height after placement: 45-120 cm.
- Ring diameter: 45-110 cm.
- Ring thickness: 7-20 cm.
- Set footprint: 120-320 cm wide, 80-260 cm deep.

Future validation must compare against female 442 cm and male 470 cm Giant baselines.

## Materials and Color Palette

- Blackened iron, dark steel, hammered metal, mud-caked lower surfaces.
- Soot, ash, rust staining, oil-dark grime, chipped dull red paint, and restrained red cloth ties.
- Optional hide wrap near ring contact.

Avoid neutral/civilized Giant blue-gray stone, refined cave-town fixtures, warm hearth color, restrained blue runes, default emissive, polished metal, clean chains, or bright quest-like colors.

## Concept Image Prompt

Create an original stylized fantasy MMORPG concept image of `SM_GIA_BloodAxeRingPegSet_A01` for the world of Aerathea. The design should emphasize Giant-scale ground pegs and ring anchors, blunt hammered silhouettes, oversized oval rings, mud-dark bases, blackened iron, dark steel, soot, chipped dull Blood Axe red marks, hostile Giant raider camp identity, female Giant scale 442 cm / 14'6", male Giant scale 470 cm / 15'5", and a gameplay role as static non-interactive perimeter dressing. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, no default emissive glow, and MMO-friendly production design. Present it as a clean prop sheet with variant labels, scale callouts, material swatches, LOD notes, and simple display collision notes. Avoid copying any existing franchise, avoid neutral/civilized Giant culture, avoid rope simulation, physics constraints, traps, objectives, pickups, weapons, nav blockers, or interaction reads, and avoid excessive micro-detail that would not translate to a mid-poly Unreal asset.

## Modeling Notes

- Model peg bodies, hammered heads, ring geometry, low ground plates, and mud-seat bases as real geometry.
- Use broad bevels and bent, uneven forms for Blood Axe field-made construction.
- Keep all exposed ends blunt; do not create sharp trap spikes.
- Limit each set to a few large shapes with readable spacing.
- Texture pitting, rust, scratches, soot, chipped red paint, mud, leather grain, and cloth weave.

No DCC source, sculpt, UV, bake, collision proxy, FBX export, Unreal import, material instance, runtime file, validator, or implementation target is created by this package.

## Texture and Material Notes

Required future map set:

- `T_GIA_BloodAxeRingPegSet_A01_BC`
- `T_GIA_BloodAxeRingPegSet_A01_N`
- `T_GIA_BloodAxeRingPegSet_A01_ORM`

Material slots:

- Slot 0: blackened iron, mud, soot, rust, chipped dull red marks.
- Optional slot 1: hide wrap or cloth tie only if needed.

Use 512-1K for the prop set. No emissive map is planned.

## Triangle Budget

- Single peg with ring LOD0: 700-1.4k tris.
- Double peg pair LOD0: 1.2k-2.4k tris.
- Ground ring plate LOD0: 900-1.8k tris.
- Full ring peg set LOD0: 2k-4k tris.
- Target material slots: 1, with 2 maximum.

## LOD Plan

- LOD0: full peg bodies, ring profiles, ground plates, mud-seat bases, red tie, and broad bevels.
- LOD1: 60-70 percent of LOD0; reduce ring subdivisions, peg bevels, plate backs, and tie loops.
- LOD2: 35-45 percent of LOD0; simplify ring cross sections, peg heads, mud bases, and small plate cuts.
- LOD3: 15-25 percent of LOD0; preserve peg height, ring silhouette, set footprint, and black/red material blocks.

Remove pitting, scratches, cloth weave, soot speckles, and mud flecks before reducing the main ring and peg silhouettes.

## Collision Notes

Use simple display collision only:

- One capsule or box for each peg.
- One simplified hull for each ring/plate set.
- One grouped hull for a bundled set if used as ground clutter.

No per-ring collision, per-link collision, rope simulation, physics constraints, pickup collision, weapon traces, trap volumes, objective volumes, interaction volumes, nav blockers, damage collision, destructible collision, or runtime gameplay collision.

## Animation Notes

Static mesh baseline. No animation, no physics simulation, no rope simulation, no hanging secondary motion, no chain swing, no peg pull state, no pickup state, no weapon use, no trap state, no objective state, no interaction prompt, no VFX, no audio, and no material-state timing.

## Unreal Import Notes

Planning notes only; do not create Unreal assets in this task.

- Planned asset type: Static Mesh.
- Planned folder: `/Game/Aerathea/Props/Giants/BloodAxeCamp/CampTools/TieHardware/`
- Planned material: `MI_GIA_BloodAxeTieHardware_A01` or shared blackened metal material.
- Pivot: ground contact center for placed variants; local center for loose spare peg sets.
- Scale: centimeters, import scale 1.0.
- Collision: simple display collision only.
- LODs: LOD0-LOD3 required.
- Sockets: none.
- Blueprint behavior: none.

Do not create Blueprint Actors, pickup items, weapon data, trap logic, rope simulation, physics constraints, objective logic, nav blocker behavior, interaction logic, DCC, Unreal Content, runtime source, validators, startup placement, or implementation targets.

## Folder and Naming Recommendation

- Docs folder: `docs/assets/props/SM_GIA_BloodAxeRingPegSet_A01/`
- Package: `docs/assets/props/SM_GIA_BloodAxeRingPegSet_A01/PRODUCTION_PACKAGE.md`
- Future mesh: `SM_GIA_BloodAxeRingPegSet_A01`
- Future material instance: `MI_GIA_BloodAxeRingPegSet_A01`
- Future textures: `T_GIA_BloodAxeRingPegSet_A01_BC`, `T_GIA_BloodAxeRingPegSet_A01_N`, `T_GIA_BloodAxeRingPegSet_A01_ORM`

## Quality Gate Checklist

- Follows the universal 15-section Aerathea production package format.
- Blood Axe remains a hostile Giant sub-faction, separate from neutral/civilized Giant culture.
- Giant scale lock is explicit: female 442 cm / 14'6" and male 470 cm / 15'5".
- Reads as static ring-and-peg perimeter dressing, not rope simulation, physics constraint, trap, objective, pickup, weapon, nav, or interaction content.
- Includes no-DCC/no-Unreal/no-pickup/no-weapon/no-trap/no-hanging-physics/no-rope-simulation/no-objective/no-interaction/no-implementation-target guardrails.
- Includes texture map list, triangle budget, LOD plan, collision notes, animation notes, and Unreal import planning.
- Does not create or request Content, SourceAssets, Tools/DCC, Tools/Unreal, runtime source, external concepts, validators, global indexes, task board edits, Hermes files, or implementation files.
