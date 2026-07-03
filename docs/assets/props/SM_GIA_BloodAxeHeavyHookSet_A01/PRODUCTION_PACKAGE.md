# SM_GIA_BloodAxeHeavyHookSet_A01 Production Package

## Art Direction Summary

- Asset name: `SM_GIA_BloodAxeHeavyHookSet_A01`
- Asset type: Static Mesh prop set, docs-only production package
- Parent kit: `KIT_GIA_BloodAxeCampTools_A01`
- Intake row: `BloodAxeCamp.png#CampTools_HeavyHookSet_A01`
- Faction/theme: Blood Axe Tribe, hostile Giant sub-faction
- Status: package-ready planning sheet

`SM_GIA_BloodAxeHeavyHookSet_A01` defines oversized blackened-iron S-hooks, wall hooks, and loose tie-down hooks for Blood Axe camp utility dressing. The set must read as crude, brutal, practical camp hardware for hostile Giant raiders, not as refined neutral/civilized Giant stoneworker equipment.

This is a docs-only package. Guardrails: no DCC, no Unreal, no pickup, no weapon, no trap, no hanging physics, no rope simulation, no objective, no interaction, no implementation target.

## Gameplay Purpose

Static environmental storytelling and scale dressing only:

- Supports Blood Axe camp buckets, rope coils, gate dressing, shelter edges, utility clusters, and forge-adjacent clutter.
- Shows that Blood Axe raiders use oversized field-made hardware sized for female 442 cm / 14'6" and male 470 cm / 15'5" Giants.
- Provides reusable hook silhouettes for later composition packages without defining gameplay.

Do not define pickup behavior, weapon use, trap use, hanging physics, rope simulation, objective logic, interaction prompts, workstation behavior, crafting/resource/economy data, loot, NPC routines, nav behavior, DCC, Unreal Content, runtime source, validators, or a first implementation target.

## Silhouette Notes

Primary read: large curved hook silhouettes with thick forged bodies, blunt points, and readable negative spaces.

- Include 3-5 variants: heavy S-hook, wall hook with plate, loose tie-down hook, ring-ended hook, and short double hook.
- Keep each hook broad enough to read from MMO camera distance.
- Use asymmetry, hammered bends, flattened contact plates, and rough ring ends for Blood Axe crudeness.
- Use sparse dull red cloth tags or chipped red marks as faction accents.
- Avoid thin fishhook shapes, elegant smithing, polished civilized Giant craft, readable weapon blades, trap jaws, gore display, or UI-like markers.

Model the main hook curves, ring ends, wall plates, large rivet heads, and heavy hammered thickness as geometry. Put pitting, scratches, soot, edge chips, small rivets, and cloth fiber into texture and normal detail.

## Scale Notes

- Female Giant baseline: 442 cm / 14'6".
- Male Giant baseline: 470 cm / 15'5".
- Approved Giant ranges: females 14-15 ft / 427-457 cm; males 14'10"-16'0" / 452-488 cm.
- Author in centimeters. 1 Unreal unit = 1 cm.

Target sizes:

- Small heavy hook: 70-95 cm long, 12-20 cm thick at main body.
- Standard S-hook: 100-145 cm long, 16-28 cm thick.
- Large tie-down hook: 140-180 cm long, 20-36 cm thick.
- Wall plate variants: 80-160 cm wide, 60-130 cm tall, 8-18 cm deep before hook projection.

Normal humanoid scale compatibility is not required. Future validation must compare silhouettes against the female 442 cm and male 470 cm Giant baselines.

## Materials and Color Palette

- Blackened iron and dark steel as the dominant read.
- Hammered bright-edge wear only on broad contact zones.
- Soot, oil grime, mud staining, ash, and dark rust.
- Dull Blood Axe red cloth tags or chipped paint as restrained hostile sub-faction marks.
- Optional hide wrap on one ring or grip point.

Avoid neutral/civilized Giant blue-gray stone, warm hearth color, refined cave-town carving, peaceful highland clan markings, restrained blue runes, default emissive, polished brass, or jewel accents.

## Concept Image Prompt

Create an original stylized fantasy MMORPG concept image of `SM_GIA_BloodAxeHeavyHookSet_A01` for the world of Aerathea. The design should emphasize oversized curved blackened-iron S-hooks, wall hooks, loose tie-down hooks, hammered ring ends, blunt brutal silhouettes, soot, mud, chipped dull Blood Axe red tags, hostile Giant raider camp identity, female Giant scale 442 cm / 14'6", male Giant scale 470 cm / 15'5", and a gameplay role as static non-interactive camp dressing. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, no default emissive glow, and MMO-friendly production design. Present it as a clean prop sheet with front and side views, scale callouts, material swatches, LOD notes, and simple collision notes. Avoid copying any existing franchise, avoid neutral/civilized Giant culture, avoid making hooks into weapons or traps, avoid pickup or interaction markers, and avoid excessive micro-detail that would not translate to a mid-poly Unreal asset.

## Modeling Notes

- Build as a small reusable static mesh set, not one fused clutter slab.
- Use real geometry for each primary hook curve, ring eye, wall plate, large hammered bevel, broad rivet, and plate lip.
- Keep hook ends blunt and practical; do not sharpen into weapon blades or trap teeth.
- Plate variants may include 2-4 large rivets or crude spike heads, but not dense rivet fields.
- Add one or two red cloth tag variants as broad strips only.
- Use texture and normal detail for iron pitting, soot, scratches, small chips, grime, stamped marks, and cloth weave.

No DCC source, sculpt, UV, bake, collision proxy, FBX export, Unreal import, material instance, runtime file, validator, or implementation target is created by this package.

## Texture and Material Notes

Required future map set:

- `T_GIA_BloodAxeHeavyHookSet_A01_BC`
- `T_GIA_BloodAxeHeavyHookSet_A01_N`
- `T_GIA_BloodAxeHeavyHookSet_A01_ORM`

Material slots:

- Slot 0: blackened metal, soot, dark rust, broad edge wear, and chipped dull red marks.
- Optional slot 1: hide or cloth tag material only if atlasing with slot 0 loses readability.

Use 512-1K for repeated hook variants. Use 1K only for a larger set sheet. No emissive map is planned.

## Triangle Budget

- Individual small hook LOD0: 500-900 tris.
- Standard S-hook LOD0: 800-1.4k tris.
- Wall hook with plate LOD0: 1.2k-2.2k tris.
- Full hook set display LOD0: 2.5k-5k tris.
- Target material slots: 1, with 2 maximum only for cloth or hide variants.

## LOD Plan

- LOD0: full hook curves, ring eyes, plate thickness, broad bevels, large rivets, red tags, and hammered silhouette.
- LOD1: 60-70 percent of LOD0; reduce bevel loops, rivet sides, ring subdivisions, and backside plate detail.
- LOD2: 35-45 percent of LOD0; simplify hook cross sections, flatten minor dents, and reduce plate lips.
- LOD3: 15-25 percent of LOD0; preserve curved hook read, ring read, plate footprint, and red/black material blocks.

Remove texture-only detail before reducing primary hook curves or main negative spaces.

## Collision Notes

Use simple display collision only:

- One convex hull or simple box per loose hook.
- Wall plate variants can use one box for the plate and one simplified hull for the hook projection.
- No per-point, per-rivet, per-ring, per-chain, or sharp hook collision.

No pickup collision, weapon traces, trap volumes, hanging physics, rope simulation, physics constraints, objective volumes, interaction volumes, nav blockers, damage collision, or runtime gameplay collision.

## Animation Notes

Static mesh baseline. No animation, no physics simulation, no rope simulation, no hanging secondary motion, no hook swing, no pickup state, no weapon use, no trap state, no objective state, no interaction prompt, no VFX, no audio, and no material-state timing.

## Unreal Import Notes

Planning notes only; do not create Unreal assets in this task.

- Planned asset type: Static Mesh.
- Planned folder: `/Game/Aerathea/Props/Giants/BloodAxeCamp/CampTools/Hooks/`
- Planned material: `MI_GIA_BloodAxeBlackenedIron_A01` or shared camp utility metal.
- Pivot: loose hooks at ground/contact center; wall hooks at wall contact center.
- Scale: centimeters, import scale 1.0.
- Collision: simple display collision only.
- LODs: LOD0-LOD3 required.
- Sockets: none.
- Blueprint behavior: none.

Do not create Blueprint Actors, pickup items, weapon data, trap logic, rope simulation, objective logic, interaction logic, DCC, Unreal Content, runtime source, validators, startup placement, or implementation targets.

## Folder and Naming Recommendation

- Docs folder: `docs/assets/props/SM_GIA_BloodAxeHeavyHookSet_A01/`
- Package: `docs/assets/props/SM_GIA_BloodAxeHeavyHookSet_A01/PRODUCTION_PACKAGE.md`
- Future mesh: `SM_GIA_BloodAxeHeavyHookSet_A01`
- Future material instance: `MI_GIA_BloodAxeHeavyHookSet_A01`
- Future textures: `T_GIA_BloodAxeHeavyHookSet_A01_BC`, `T_GIA_BloodAxeHeavyHookSet_A01_N`, `T_GIA_BloodAxeHeavyHookSet_A01_ORM`

## Quality Gate Checklist

- Follows the universal 15-section Aerathea production package format.
- Blood Axe remains a hostile Giant sub-faction, separate from neutral/civilized Giant culture.
- Giant scale lock is explicit: female 442 cm / 14'6" and male 470 cm / 15'5".
- Reads as static heavy camp hooks, not weapons, traps, pickups, or interaction props.
- Includes no-DCC/no-Unreal/no-pickup/no-weapon/no-trap/no-hanging-physics/no-rope-simulation/no-objective/no-interaction/no-implementation-target guardrails.
- Uses blackened iron, dark steel, soot, mud, grime, and restrained dull red marks.
- Keeps micro-detail in textures and normals.
- Includes texture map list, triangle budget, LOD plan, collision notes, animation notes, and Unreal import planning.
- Does not create or request Content, SourceAssets, Tools/DCC, Tools/Unreal, runtime source, external concepts, validators, global indexes, task board edits, Hermes files, or implementation files.
