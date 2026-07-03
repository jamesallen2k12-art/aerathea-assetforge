# SM_GIA_BloodAxeHangingHookRail_A01 Production Package

## Art Direction Summary

- Asset name: `SM_GIA_BloodAxeHangingHookRail_A01`
- Asset type: Static Mesh prop, docs-only production package
- Parent kit: `KIT_GIA_BloodAxeCampTools_A01`
- Intake row: `BloodAxeShelter.png#CampTools_HangingHookRail_A01`
- Faction/theme: Blood Axe Tribe, hostile Giant sub-faction
- Status: package-ready planning sheet

`SM_GIA_BloodAxeHangingHookRail_A01` defines a short shelter-edge rail with sparse oversized hooks for Blood Axe camp dressing. It is related to general camp tools, not bowyer tool racks, and must not become a usable rack, workstation, physics system, or neutral/civilized Giant fixture.

This is a docs-only package. Guardrails: no DCC, no Unreal, no pickup, no weapon, no trap, no hanging physics, no rope simulation, no objective, no interaction, no implementation target.

## Gameplay Purpose

Static shelter-edge and camp utility dressing only:

- Adds readable hanging-hardware silhouettes to shelters, rough walls, gate interiors, and utility clusters.
- Visually supports buckets, rope coils, mallets, hooks, and tie hardware without becoming an inventory rack.
- Provides a Giant-scale reference beside female 442 cm / 14'6" and male 470 cm / 15'5" Giants.

Do not define hanging physics, rope simulation, pickup behavior, usable rack behavior, workstation behavior, trap behavior, objective logic, interaction prompts, DCC, Unreal Content, runtime source, validators, or implementation targets.

## Silhouette Notes

Primary read: a horizontal heavy rail or timber beam with 3-5 sparse oversized hooks.

- Rail can be blackened iron, scorched timber with iron bands, or a crude metal strip bolted to wood.
- Hooks should hang or project downward in large, readable arcs.
- Keep spacing generous so the silhouette does not become visual noise.
- Include crude end brackets, large rivets, iron straps, and one restrained red cloth tie.
- Avoid dense tool-rack organization, refined workshop order, bowyer-specific clamp reads, weapon display, trap hooks, gore display, and dangling physics props.

Model rail mass, hook curves, brackets, large rivets, and broad straps as geometry. Texture small scratches, soot, wood grain, cloth weave, minor rivets, and pitting.

## Scale Notes

- Female Giant baseline: 442 cm / 14'6".
- Male Giant baseline: 470 cm / 15'5".
- Approved Giant ranges: females 14-15 ft / 427-457 cm; males 14'10"-16'0" / 452-488 cm.
- Author in centimeters. 1 Unreal unit = 1 cm.

Target sizes:

- Rail length: 250-520 cm.
- Rail height/thickness: 25-60 cm.
- Hook length: 70-150 cm.
- Hook spacing: 60-120 cm between major hook centers.
- Total mounted height in scene, if later placed: sized for Giant reach, not humanoid reach.

Future validation must compare to female 442 cm and male 470 cm Giant baselines before visual approval.

## Materials and Color Palette

- Blackened iron, dark steel, scorched timber, crude iron bands, and large hammered rivets.
- Soot, mud, ash, oil grime, chipped red paint, dull red cloth tie, and broad edge wear.
- Optional hide wrap around one rail section.

Avoid neutral/civilized Giant cave-town carpentry, blue-gray stone, warm hearth presentation, restrained blue runes, refined highland tool storage, default emissive, polished metal, or bright clean banners.

## Concept Image Prompt

Create an original stylized fantasy MMORPG concept image of `SM_GIA_BloodAxeHangingHookRail_A01` for the world of Aerathea. The design should emphasize a short Giant-scale shelter-edge hook rail, sparse oversized hooks, scorched timber or blackened iron rail, crude brackets, hammered rivets, soot, mud, chipped dull Blood Axe red ties, hostile Giant raider camp identity, female Giant scale 442 cm / 14'6", male Giant scale 470 cm / 15'5", and a gameplay role as static non-interactive camp dressing. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, no default emissive glow, and MMO-friendly production design. Present it as a clean prop sheet with front, side, and mounted-context views, scale callouts, material swatches, LOD notes, and simple display collision notes. Avoid copying any existing franchise, avoid neutral/civilized Giant culture, avoid usable rack behavior, pickup, weapon, trap, hanging physics, rope simulation, objective, or interaction reads, and avoid excessive micro-detail that would not translate to a mid-poly Unreal asset.

## Modeling Notes

- Build one rail asset with 2-3 bracket variants if later expanded, but keep baseline `A01` simple.
- Model rail body, hooks, brackets, large rivets, iron bands, and hanging plates as geometry.
- Keep hooks thick and blunt; avoid weapon or trap silhouettes.
- Keep hook count sparse, usually 3-5, with strong negative space.
- Use texture and normal detail for wood grain, soot, scratches, pitting, chipped paint, cloth weave, and grime.

No DCC source, sculpt, UV, bake, collision proxy, FBX export, Unreal import, material instance, runtime file, validator, or implementation target is created by this package.

## Texture and Material Notes

Required future map set:

- `T_GIA_BloodAxeHangingHookRail_A01_BC`
- `T_GIA_BloodAxeHangingHookRail_A01_N`
- `T_GIA_BloodAxeHangingHookRail_A01_ORM`

Material slots:

- Slot 0: scorched timber, blackened metal, soot, mud, dull red marks.
- Optional slot 1: separate blackened metal only if the rail uses a timber/metal split that needs material control.

Use a 1K texture set for the baseline rail. No emissive map is planned.

## Triangle Budget

- Simple rail with three hooks LOD0: 2k-3.5k tris.
- Larger rail with five hooks LOD0: 3k-5k tris.
- Bracket-heavy variant LOD0: 4k-6k tris maximum.
- Target material slots: 1-2.

## LOD Plan

- LOD0: full rail, hook curves, brackets, rivets, bands, red tie, and primary bevels.
- LOD1: 60-70 percent of LOD0; reduce bevel loops, rivet sides, bracket backs, and hook subdivisions.
- LOD2: 35-45 percent of LOD0; simplify hook cross sections, rail backs, end brackets, and small straps.
- LOD3: 15-25 percent of LOD0; preserve rail length, hook count read, main negative spaces, and red/black material blocks.

Do not remove primary hooks or rail footprint before texture-only wear, small rivets, and backside detail.

## Collision Notes

Use simple mounted display collision only:

- One box or convex hull for the rail.
- Optional simplified hulls for major hook projections.
- No per-hook sharp collision, per-rivet collision, dangling item collision, or physics bodies.

No pickup collision, usable rack volumes, workstation volumes, weapon traces, trap volumes, hanging physics, rope simulation, objective volumes, interaction volumes, nav blockers, damage collision, or runtime gameplay collision.

## Animation Notes

Static mesh baseline. No animation, no physics simulation, no rope simulation, no hanging secondary motion, no swinging hooks, no dangling objects, no pickup state, no weapon use, no trap state, no objective state, no interaction prompt, no VFX, no audio, and no material-state timing.

## Unreal Import Notes

Planning notes only; do not create Unreal assets in this task.

- Planned asset type: Static Mesh.
- Planned folder: `/Game/Aerathea/Props/Giants/BloodAxeCamp/CampTools/Hooks/`
- Planned material: `MI_GIA_BloodAxeCampUtility_A01` or shared blackened metal/timber material.
- Pivot: wall contact center or rail centerline at mounting plane.
- Scale: centimeters, import scale 1.0.
- Collision: simple display collision only.
- LODs: LOD0-LOD3 required.
- Sockets: none.
- Blueprint behavior: none.

Do not create Blueprint Actors, pickup items, weapon data, trap logic, rope simulation, hanging physics, objective logic, interaction logic, DCC, Unreal Content, runtime source, validators, startup placement, or implementation targets.

## Folder and Naming Recommendation

- Docs folder: `docs/assets/props/SM_GIA_BloodAxeHangingHookRail_A01/`
- Package: `docs/assets/props/SM_GIA_BloodAxeHangingHookRail_A01/PRODUCTION_PACKAGE.md`
- Future mesh: `SM_GIA_BloodAxeHangingHookRail_A01`
- Future material instance: `MI_GIA_BloodAxeHangingHookRail_A01`
- Future textures: `T_GIA_BloodAxeHangingHookRail_A01_BC`, `T_GIA_BloodAxeHangingHookRail_A01_N`, `T_GIA_BloodAxeHangingHookRail_A01_ORM`

## Quality Gate Checklist

- Follows the universal 15-section Aerathea production package format.
- Blood Axe remains a hostile Giant sub-faction, separate from neutral/civilized Giant culture.
- Giant scale lock is explicit: female 442 cm / 14'6" and male 470 cm / 15'5".
- Reads as static shelter-edge hook rail dressing, not a usable rack, weapon, trap, pickup, objective, or interaction prop.
- Includes no-DCC/no-Unreal/no-pickup/no-weapon/no-trap/no-hanging-physics/no-rope-simulation/no-objective/no-interaction/no-implementation-target guardrails.
- Includes texture map list, triangle budget, LOD plan, collision notes, animation notes, and Unreal import planning.
- Does not create or request Content, SourceAssets, Tools/DCC, Tools/Unreal, runtime source, external concepts, validators, global indexes, task board edits, Hermes files, or implementation files.
