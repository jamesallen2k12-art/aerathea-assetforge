# KIT_GIA_BloodAxeTieHardware_A01 Production Package

## Art Direction Summary

- Asset name: `KIT_GIA_BloodAxeTieHardware_A01`
- Asset type: Static Mesh prop kit, docs-only production package
- Parent kit: `KIT_GIA_BloodAxeCampTools_A01`
- Intake row: `BloodAxeCamp.png#CampTools_TieHardware_A01`
- Faction/theme: Blood Axe Tribe, hostile Giant sub-faction
- Status: package-ready planning sheet

`KIT_GIA_BloodAxeTieHardware_A01` defines secondary camp utility hardware: oversized rings, pegs, short chain lengths, latch plates, hide ties, and crude anchor pieces that support buckets, rope coils, hooks, and static camp clusters. It is a supporting dressing kit, not a standalone interaction system, weapon system, trap system, or neutral/civilized Giant hardware language.

This is a docs-only package. Guardrails: no DCC, no Unreal, no pickup, no weapon, no trap, no hanging physics, no rope simulation, no objective, no interaction, no implementation target.

## Gameplay Purpose

Static support dressing only:

- Adds reusable secondary detail around Blood Axe gates, shelters, ropes, hook sets, tool buckets, and utility clusters.
- Reinforces hostile Giant camp scale beside female 442 cm / 14'6" and male 470 cm / 15'5" Giants.
- Provides simple ring, peg, latch, and short-chain language for composition packages.

Do not define pickup behavior, resource behavior, per-link collision, rope simulation, physics constraints, traps, objective logic, interaction prompts, workstation behavior, crafting/economy data, DCC, Unreal Content, runtime source, validators, or implementation targets.

## Silhouette Notes

Primary read: oversized crude tie hardware with large simple shapes.

- Rings: thick circular or oval rings, 35-100 cm diameter.
- Pegs: blunt hammered pegs, 80-180 cm long, with broad heads and muddy bases.
- Short chains: 2-5 oversized links only, used as static visual bundles.
- Latch plates: crude blackened plates, hooks, and loops for gates or shelter supports.
- Hide ties: broad straps and knots, not dense rope rigs.

Keep hardware secondary and sparse. Avoid tiny link fields, polished shackles, refined hinges, mechanical puzzles, trap mechanisms, objective markers, glowing affordances, or neutral/civilized Giant craft language.

## Scale Notes

- Female Giant baseline: 442 cm / 14'6".
- Male Giant baseline: 470 cm / 15'5".
- Approved Giant ranges: females 14-15 ft / 427-457 cm; males 14'10"-16'0" / 452-488 cm.
- Author in centimeters. 1 Unreal unit = 1 cm.

Target sizes:

- Rings: 35-100 cm diameter, 6-18 cm thick.
- Pegs: 80-180 cm long, 14-35 cm thick.
- Chain links: 30-70 cm long per link, limited to short static bundles.
- Latch plates: 50-140 cm wide, 35-110 cm tall.
- Small hardware cluster: 150-350 cm wide.

Future validation must compare against female 442 cm and male 470 cm Giant baselines.

## Materials and Color Palette

- Blackened iron, dark steel, rough hammered metal, crude iron bands.
- Hide ties, scorched leather, mud-dark rope ends, and dirty sinew wraps.
- Soot, ash, oil grime, rust staining, chipped dull red paint, and restrained red cloth markers.
- Sparse bone or horn spacers only as non-graphic hostile accents.

Avoid neutral/civilized Giant blue-gray stone, refined cave-town fixtures, warm hearth treatment, restrained blue runes, default emissive, polished metal, shiny treasure reads, or bright UI-like colors.

## Concept Image Prompt

Create an original stylized fantasy MMORPG concept image of `KIT_GIA_BloodAxeTieHardware_A01` for the world of Aerathea. The design should emphasize oversized Giant-scale tie hardware, crude rings, blunt pegs, short static chain bundles, latch plates, hide ties, blackened iron, dark steel, scorched leather, mud, soot, chipped dull Blood Axe red marks, hostile Giant raider camp identity, female Giant scale 442 cm / 14'6", male Giant scale 470 cm / 15'5", and a gameplay role as static non-interactive secondary camp dressing. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, no default emissive glow, and MMO-friendly production design. Present it as a clean kit sheet with labeled variants, scale callouts, material swatches, LOD notes, and simple collision notes. Avoid copying any existing franchise, avoid neutral/civilized Giant culture, avoid traps, pickups, weapons, per-link collision, rope simulation, physics constraints, objective logic, or interaction markers, and avoid excessive micro-detail that would not translate to mid-poly Unreal assets.

## Modeling Notes

- Build reusable static child meshes for rings, pegs, short chain bundles, latch plates, and hide ties.
- Use real geometry for ring masses, peg heads, plate thickness, large chain links, and broad strap knots.
- Keep chain lengths very short and static; no dense or physics-ready chain rigs.
- Keep points blunt and practical; do not create trap teeth, weapon spikes, or interactive devices.
- Texture small pitting, rust, soot, scratches, chipped paint, leather grain, hide stitching, and mud splatter.

No DCC source, sculpt, UV, bake, collision proxy, FBX export, Unreal import, material instance, runtime file, validator, or implementation target is created by this package.

## Texture and Material Notes

Required future map set:

- `T_GIA_BloodAxeTieHardware_A01_BC`
- `T_GIA_BloodAxeTieHardware_A01_N`
- `T_GIA_BloodAxeTieHardware_A01_ORM`

Optional child texture names:

- `T_GIA_BloodAxeRingPegSet_A01_BC`
- `T_GIA_BloodAxeLatchPlate_A01_BC`
- `T_GIA_BloodAxeShortChain_A01_BC`

Material slots:

- Slot 0: blackened iron, dark steel, soot, rust, chipped dull red marks.
- Optional slot 1: hide, scorched leather, rope, and sinew ties.

Use 512-1K texture sets for child hardware and 1K for a composed kit sheet. No emissive map is planned.

## Triangle Budget

- Ring variant LOD0: 300-800 tris.
- Peg variant LOD0: 400-900 tris.
- Short chain bundle LOD0: 800-2k tris, limited to 2-5 large links.
- Latch plate variant LOD0: 700-1.6k tris.
- Small hardware cluster LOD0: 1.5k-4k tris.
- Full kit display LOD0: 4k-8k tris if later approved as a composed preview.
- Target material slots: 1-2.

## LOD Plan

- LOD0: full ring profiles, peg heads, short chain links, latch plates, hide ties, and broad bevels.
- LOD1: 60-70 percent of LOD0; reduce ring subdivisions, peg bevels, chain link sides, plate backs, and strap loops.
- LOD2: 35-45 percent of LOD0; simplify chain bundles, plate lips, ring cross sections, and hide tie knots.
- LOD3: 15-25 percent of LOD0; preserve ring/peg/latch silhouettes and black/red material blocks.

Remove pitting, scratches, stitch lines, soot speckles, and small chips before reducing the primary hardware silhouettes.

## Collision Notes

Use simple display collision only:

- Rings and pegs: one simple hull or box/capsule per piece.
- Short chain bundles: one simplified hull around the bundle, never per-link collision.
- Latch plates: one box or convex hull around the plate and projection.
- Hardware clusters: grouped display collision around broad shapes only.

No per-link collision, rope simulation, physics constraints, pickup collision, trap volumes, objective volumes, interaction volumes, weapon traces, damage collision, nav blockers, destructible collision, or runtime gameplay collision.

## Animation Notes

Static mesh baseline. No animation, no physics simulation, no rope simulation, no hanging secondary motion, no chain swing, no latch operation, no pickup state, no weapon use, no trap state, no objective state, no interaction prompt, no VFX, no audio, and no material-state timing.

## Unreal Import Notes

Planning notes only; do not create Unreal assets in this task.

- Planned asset type: Static Mesh kit children.
- Planned folder: `/Game/Aerathea/Props/Giants/BloodAxeCamp/CampTools/TieHardware/`
- Planned material: `MI_GIA_BloodAxeBlackenedIron_A01` and optional shared hide/leather material.
- Pivot: base/contact center for pegs and clusters; local center for loose rings and latch plates.
- Scale: centimeters, import scale 1.0.
- Collision: simple display collision only.
- LODs: LOD0-LOD3 required.
- Sockets: none.
- Blueprint behavior: none.

Do not create Blueprint Actors, pickup items, weapon data, trap logic, rope simulation, physics constraints, objective logic, interaction logic, DCC, Unreal Content, runtime source, validators, startup placement, or implementation targets.

## Folder and Naming Recommendation

- Docs folder: `docs/assets/kits/KIT_GIA_BloodAxeTieHardware_A01/`
- Package: `docs/assets/kits/KIT_GIA_BloodAxeTieHardware_A01/PRODUCTION_PACKAGE.md`
- Future kit: `KIT_GIA_BloodAxeTieHardware_A01`
- Future child mesh examples: `SM_GIA_BloodAxeRingPegSet_A01`, `SM_GIA_BloodAxeLatchPlate_A01`, `SM_GIA_BloodAxeShortChain_A01`
- Future material instance: `MI_GIA_BloodAxeTieHardware_A01`
- Future textures: `T_GIA_BloodAxeTieHardware_A01_BC`, `T_GIA_BloodAxeTieHardware_A01_N`, `T_GIA_BloodAxeTieHardware_A01_ORM`

## Quality Gate Checklist

- Follows the universal 15-section Aerathea production package format.
- Blood Axe remains a hostile Giant sub-faction, separate from neutral/civilized Giant culture.
- Giant scale lock is explicit: female 442 cm / 14'6" and male 470 cm / 15'5".
- Reads as secondary static tie hardware, not a standalone interaction, weapon, trap, objective, rope, or physics system.
- Includes no-DCC/no-Unreal/no-pickup/no-weapon/no-trap/no-hanging-physics/no-rope-simulation/no-objective/no-interaction/no-implementation-target guardrails.
- Includes texture map list, triangle budget, LOD plan, collision notes, animation notes, and Unreal import planning.
- Does not create or request Content, SourceAssets, Tools/DCC, Tools/Unreal, runtime source, external concepts, validators, global indexes, task board edits, Hermes files, or implementation files.
