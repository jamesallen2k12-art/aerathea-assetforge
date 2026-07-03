# SM_GIA_BloodAxeStakeHook_A01 Production Package

## Art Direction Summary

- Asset name: `SM_GIA_BloodAxeStakeHook_A01`
- Asset type: Static Mesh prop, docs-only production package
- Parent kit: `KIT_GIA_BloodAxeCampTools_A01`
- Intake row: `BloodAxeGate.png#CampTools_StakeHook_A01`
- Faction/theme: Blood Axe Tribe, hostile Giant sub-faction
- Status: package-ready planning sheet

`SM_GIA_BloodAxeStakeHook_A01` defines a Giant-scale ground or wall stake hook with a crude mounting plate, hammered ring, and mud-dark base for Blood Axe gate, shelter, and perimeter utility dressing. It is hostile raider hardware and must not become neutral/civilized Giant craft language.

This is a docs-only package. Guardrails: no DCC, no Unreal, no pickup, no weapon, no trap, no hanging physics, no rope simulation, no objective, no interaction, no implementation target.

## Gameplay Purpose

Static display and visual tie-down language only:

- Provides perimeter and shelter-edge dressing that suggests heavy camp anchoring.
- Supports nearby rope coils, ring pegs, hook rails, and utility clusters visually.
- Reinforces Blood Axe Giant scale beside female 442 cm / 14'6" and male 470 cm / 15'5" Giants.

Do not define collision gameplay, nav blockers, gate behavior, rope simulation, physics constraints, traps, objectives, pickups, weapons, interaction prompts, DCC, Unreal Content, runtime source, validators, or implementation targets.

## Silhouette Notes

Primary read: a thick driven stake or wall spike with an oversized hook and ring.

- Ground variant: broad wedge-like stake base, forward hook, large ring eye, and mud-caked foot.
- Wall variant: crude rectangular plate or spike plate with projecting hook and hammered ring.
- Keep the hook blunt, thick, and utilitarian.
- Use a strong triangular support shape so the asset reads from a distance.
- Add one dull red tie or paint slash only if it does not look like an interaction marker.

Avoid thin spear reads, weapon heads, trap spikes, polished shackles, refined masonry fixtures, gore, hanging bodies, or dense chains.

## Scale Notes

- Female Giant baseline: 442 cm / 14'6".
- Male Giant baseline: 470 cm / 15'5".
- Approved Giant ranges: females 14-15 ft / 427-457 cm; males 14'10"-16'0" / 452-488 cm.
- Author in centimeters. 1 Unreal unit = 1 cm.

Target sizes:

- Ground stake total height: 120-220 cm.
- Hook projection: 45-110 cm.
- Stake or plate width: 35-100 cm.
- Ring diameter: 35-80 cm.
- Base footprint: 70-170 cm wide, 60-160 cm deep.

Future validation must compare against female 442 cm and male 470 cm Giant baselines. Do not scale down to humanoid camp hardware.

## Materials and Color Palette

- Blackened iron, dark steel, hammered metal, and mud-stained lower surfaces.
- Scorched wood core or crude iron stake variants are both acceptable.
- Soot, ash, oil-dark grime, chipped red paint, dull red cloth tie, and broad edge wear.
- Optional hide wrap under the ring.

Avoid neutral/civilized Giant blue-gray stoneworker craft, warm hearth treatment, restrained blue runes, refined ornamental carving, default emissive, polished metal, or bright red overuse.

## Concept Image Prompt

Create an original stylized fantasy MMORPG concept image of `SM_GIA_BloodAxeStakeHook_A01` for the world of Aerathea. The design should emphasize a Giant-scale ground or wall stake hook, thick blackened iron, crude mounting plate, hammered ring, mud-dark base, blunt practical hook, soot, grime, chipped dull Blood Axe red markings, hostile Giant raider camp identity, female Giant scale 442 cm / 14'6", male Giant scale 470 cm / 15'5", and a gameplay role as static non-interactive tie-down dressing. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, no default emissive glow, and MMO-friendly production design. Present it as a clean prop turnaround with scale callouts, material swatches, LOD notes, and simple display collision notes. Avoid copying any existing franchise, avoid neutral/civilized Giant culture, avoid trap, weapon, pickup, objective, rope simulation, or interaction reads, and avoid excessive micro-detail that would not translate to a mid-poly Unreal asset.

## Modeling Notes

- Model the stake body, hook projection, ring, plate, base wedge, and large rivets as real geometry.
- Keep all points blunt and worn; do not create spear, blade, or trap silhouettes.
- Use broad hammered facets and irregular bends for crude Blood Axe manufacture.
- Use mud buildup at the base to ground it as camp dressing.
- Texture small pits, rust, scratches, soot, chipped paint, wood grain, and cloth weave.

No DCC source, sculpt, UV, bake, collision proxy, FBX export, Unreal import, material instance, runtime file, validator, or implementation target is created by this package.

## Texture and Material Notes

Required future map set:

- `T_GIA_BloodAxeStakeHook_A01_BC`
- `T_GIA_BloodAxeStakeHook_A01_N`
- `T_GIA_BloodAxeStakeHook_A01_ORM`

Material slots:

- Slot 0: blackened iron, scorched wood if used, soot, mud, chipped dull red marks.
- Optional slot 1: hide or cloth tie only if needed.

Use a 512-1K texture set. No emissive map is planned.

## Triangle Budget

- Simple stake hook LOD0: 900-1.8k tris.
- Wall plate variant LOD0: 1.2k-2.4k tris.
- Ground base variant LOD0: 1.5k-3k tris.
- Target material slots: 1, with 2 maximum.

## LOD Plan

- LOD0: full stake, hook, ring, plate, base, large rivets, and broad hammered bevels.
- LOD1: 60-70 percent of LOD0; reduce bevel loops, rivet sides, ring subdivisions, and underside detail.
- LOD2: 35-45 percent of LOD0; simplify the ring, hook cross-section, mud base, and plate cuts.
- LOD3: 15-25 percent of LOD0; preserve stake height, hook projection, ring silhouette, and base footprint.

Preserve primary hook/stake silhouette before any decorative chips, pitting, or red marks.

## Collision Notes

Use simple display collision only:

- One hull or box for the stake/base.
- One simplified hull or box for the hook projection.
- No per-ring collision, per-rivet collision, sharp point collision, or chain collision.

No collision gameplay, nav blocker definition, pickup collision, weapon traces, trap volumes, rope simulation, physics constraints, objective volumes, interaction volumes, damage collision, destructible collision, or gate logic.

## Animation Notes

Static mesh baseline. No animation, no physics simulation, no rope simulation, no hanging secondary motion, no gate motion, no pickup state, no weapon use, no trap state, no objective state, no interaction prompt, no VFX, no audio, and no material-state timing.

## Unreal Import Notes

Planning notes only; do not create Unreal assets in this task.

- Planned asset type: Static Mesh.
- Planned folder: `/Game/Aerathea/Props/Giants/BloodAxeCamp/CampTools/Hooks/`
- Planned material: `MI_GIA_BloodAxeBlackenedIron_A01` or shared camp utility material.
- Pivot: ground variant at base center; wall variant at wall contact center.
- Scale: centimeters, import scale 1.0.
- Collision: simple display collision only.
- LODs: LOD0-LOD3 required.
- Sockets: none.
- Blueprint behavior: none.

Do not create Blueprint Actors, pickup items, weapon data, trap logic, rope simulation, objective logic, interaction logic, DCC, Unreal Content, runtime source, validators, startup placement, or implementation targets.

## Folder and Naming Recommendation

- Docs folder: `docs/assets/props/SM_GIA_BloodAxeStakeHook_A01/`
- Package: `docs/assets/props/SM_GIA_BloodAxeStakeHook_A01/PRODUCTION_PACKAGE.md`
- Future mesh: `SM_GIA_BloodAxeStakeHook_A01`
- Future material instance: `MI_GIA_BloodAxeStakeHook_A01`
- Future textures: `T_GIA_BloodAxeStakeHook_A01_BC`, `T_GIA_BloodAxeStakeHook_A01_N`, `T_GIA_BloodAxeStakeHook_A01_ORM`

## Quality Gate Checklist

- Follows the universal 15-section Aerathea production package format.
- Blood Axe remains a hostile Giant sub-faction, separate from neutral/civilized Giant culture.
- Giant scale lock is explicit: female 442 cm / 14'6" and male 470 cm / 15'5".
- Reads as static stake hook dressing, not a weapon, trap, pickup, objective, gate mechanic, or interaction prop.
- Includes no-DCC/no-Unreal/no-pickup/no-weapon/no-trap/no-hanging-physics/no-rope-simulation/no-objective/no-interaction/no-implementation-target guardrails.
- Includes texture map list, triangle budget, LOD plan, collision notes, animation notes, and Unreal import planning.
- Does not create or request Content, SourceAssets, Tools/DCC, Tools/Unreal, runtime source, external concepts, validators, global indexes, task board edits, Hermes files, or implementation files.
