# SM_GIA_BloodAxeHornForkMarker_A01 Production Package

## Art Direction Summary

- Asset name: `SM_GIA_BloodAxeHornForkMarker_A01`
- Asset type: Static Mesh production package / docs-only path-marker prop planning
- Parent kit: `KIT_GIA_BloodAxePathMarkers_A01`
- Source planning row: `BloodAxeStronghold.png#PathMarkers_HornFork_A01`
- Faction/theme: Blood Axe Tribe, hostile Giant sub-faction only
- Status: docs-only production package ready

`SM_GIA_BloodAxeHornForkMarker_A01` is a forked horn silhouette used near Blood Axe stronghold approaches, camp thresholds, or rough path turns. It should read as a crude hostile warning from gameplay camera distance through a strong forked profile, rope lashings, ash-dark base, and restrained red cloth or paint, without becoming a signal device, aura source, VFX object, or shamanic state marker.

Blood Axe identity must remain separate from neutral/civilized Giant culture. Do not use civic cave-town stonework, blue-gray carved masonry, terrace or waterwork motifs, warm hearth settlement language, refined highland wayfinding, polished clan signs, or restrained blue-rune culture as the default read.

This package is planning only. It does not authorize DCC source creation, FBX export, Unreal Content creation, startup placement, runtime gameplay, validator creation, source concept movement, final visual approval, first implementation target selection, or Hermes work.

## Gameplay Purpose

The prop supports static Blood Axe route readability and hostile threshold dressing. It may visually mark a camp turn, stronghold approach beat, or path compression point without defining mechanics.

Allowed planning uses:

- Add one forked horn silhouette to a path-marker cluster.
- Support stronghold-adjacent warning composition without becoming a functional signal.
- Provide a mid-height marker that pairs with cairns, cloth stakes, broken shield scraps, and ash bases.
- Reinforce Blood Axe camp identity from MMO camera distance.

Out of scope:

- Signal device behavior, faction aura, VFX pulse, shamanic state, ritual mechanic, morale system, AI behavior, patrol marker, spawn marker, objective logic, trail-marker gameplay, waypoint behavior, nav/pathfinding behavior, UI marker, audio cue, interaction behavior, destructible behavior, pickup behavior, loot behavior, or startup placement.

## Silhouette Notes

Primary read:

- Forked horn shape mounted on a short scorched stake, stone socket, or compact cairn-side base.
- The fork should have a strong V or asymmetric split that remains readable at distance.
- Rope lashings and hide ties should be broad enough to read without dense detail.
- A low ash/mud base should ground the marker and separate it from taller banner lines.
- Optional oxide red cloth strip or paint smear may support Blood Axe identity, but it must stay restrained.

Model as real geometry when promoted later:

- Forked horn form, stake or socket, major rope lashings, one or two base stones, broad cloth strip if used, and ash/mud grounding.

Keep in textures or normal maps:

- Horn ridges, small cracks, scratches, soot speckles, ash flecks, rope fibers, cloth weave, minor fray, and dried mud streaks.

Avoid:

- Glowing crystals, magic cores, UI arrows, readable text, dense skull trophies, graphic gore, elegant carved signs, refined highland markers, or excessive horn/bone clutter.

## Scale Notes

Use the validated `SK_GIA_Base_A01` scale lock:

- Female Giant baseline: 442 cm / 14 ft 6 in.
- Male Giant baseline: 470 cm / 15 ft 5 in.
- Approved Giant ranges: females 14-15 ft / 427-457 cm; males 14 ft 10 in-16 ft 0 in / 452-488 cm.
- Author future source in centimeters. 1 Unreal unit = 1 cm.

Planning dimensions:

- Overall height: 120-260 cm.
- Footprint: 100-280 cm.
- Forked horn width: 80-220 cm.
- Stake or socket height below fork: 60-160 cm.
- Base stone or ash footprint: 120-260 cm wide.

The prop should feel like a hostile Giant-made threshold warning, not a human-size sign scaled up after the fact.

## Materials and Color Palette

Primary materials:

- Weathered forked horn.
- Scorched timber or rough stone socket.
- Rope, rawhide, sinew, and dirty leather lashings.
- Rough field stone, ash, soot, mud, and trampled earth at the base.
- Optional restrained oxide red cloth or red paint smear.
- Optional tiny blackened iron tack or clamp only if silhouette clarity needs it.

Palette targets:

- Horn: `#9E8C6B` to `#CDB78A`
- Charcoal and blackened iron: `#111214` to `#2A2C2E`
- Scorched timber: `#22170F` to `#4A2B17`
- Rough stone and ash: `#2E2C28` to `#6C6254`
- Rope and hide: `#6C5434` to `#A88958`
- Oxide red accent: `#5F1513` to `#8B211B`

No default emissive is approved. Signal glow, shamanic glow, faction aura, VFX pulse, animated material state, or magic marker behavior requires a separate approval gate.

## Concept Image Prompt

Create an original stylized fantasy MMORPG production concept image of `SM_GIA_BloodAxeHornForkMarker_A01` for the world of Aerathea. The design should emphasize a forked horn silhouette mounted on a short scorched stake or rough stone socket, rope lashings, ash-dark base, restrained oxide red cloth or paint, hostile Blood Axe Giant sub-faction identity, clear separation from neutral/civilized Giant culture, and the gameplay role of static non-interactive route readability near camp thresholds or stronghold approaches. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, no default emissive glow, and MMO-friendly mid-poly production design. Present it as a single prop concept sheet with front, side, scale notes beside a 442 cm female Giant and a 470 cm male Giant, material swatches, and LOD/collision callouts on a clean background. Avoid copying any existing franchise, avoid signal devices, avoid faction aura, avoid VFX pulses, avoid shamanic state markers, avoid readable text, avoid UI arrows, avoid waypoint behavior, avoid objective logic, avoid DCC or Unreal implementation claims, and avoid excessive micro-detail that would not translate to a mid-poly Unreal asset.

## Modeling Notes

This is a docs-only modeling plan. No DCC source, sculpt, retopo, UV, bake, FBX export, Unreal asset, collision proxy, proof render, material graph, validator, startup actor, runtime source, final visual approval, or Hermes file is created or authorized by this package.

Future modeling should prioritize:

- Strong forked horn silhouette with readable asymmetry.
- Ground-centered pivot for later terrain placement.
- Simple stake or stone socket that does not compete with the horn fork.
- Broad rope lashings and hide ties as large readable bands.
- Low ash/mud base that anchors the marker without implying a trigger or aura volume.
- Optional static cloth strip shaped as fixed geometry, not simulated cloth.

Do not introduce sockets, signal emitters, aura rings, VFX anchors, gameplay radii, objective markers, nav helpers, waypoint arrows, destructible breakpoints, pickup affordances, or ritual state components.

## Texture and Material Notes

Target material strategy:

- 1 material slot preferred for the full prop.
- 2 material slots only if horn and base/cloth need separation for reuse.
- Shared atlas should align with `KIT_GIA_BloodAxePathMarkers_A01` if later approved.

Suggested future material instances:

- `MI_GIA_BloodAxeHornForkMarker_A01`
- `MI_GIA_BloodAxeBoneHorn_A01`
- `MI_GIA_BloodAxePathMarkerClothHide_A01`
- `MI_GIA_BloodAxePathMarkerStone_A01`

Required future texture set if a unique prop set is approved:

- `T_GIA_BloodAxeHornForkMarker_A01_BC`
- `T_GIA_BloodAxeHornForkMarker_A01_N`
- `T_GIA_BloodAxeHornForkMarker_A01_ORM`

Optional emissive texture is not part of this package.

Packed `ORM` plan:

- R: Ambient occlusion around fork base, lashings, socket/stake contact, cloth folds, and ash/mud base.
- G: High roughness for horn, rope, hide, cloth, timber, stone, soot, ash, and mud.
- B: Metallic black except for any later-approved tiny iron tack or clamp.

## Triangle Budget

Target LOD0 budget:

- 800-3k tris.
- 1 material preferred, 2 maximum if justified.
- 512-1K texture set, or shared path-marker atlas.

Spend geometry on the forked horn profile, mounting stake or socket, major lashings, broad cloth accent if used, and simple base. Do not spend geometry on horn pores, small cracks, rope fibers, soot flecks, cloth weave, tiny chips, or paint scratches.

## LOD Plan

All important future modules require LOD0-LOD3.

- LOD0: full forked horn profile, stake/socket, major lashings, optional cloth strip, and ash/mud grounding.
- LOD1: 60-70 percent of LOD0; simplify horn bevels, reduce lashing turns, flatten small chips, and reduce base undercuts.
- LOD2: 35-45 percent of LOD0; preserve fork silhouette, mounting read, and red/black material read while removing secondary wraps and backside detail.
- LOD3: 15-25 percent of LOD0; preserve the broad fork shape and base silhouette only.

Reduction order:

1. Tiny horn scratches, soot flecks, ash speckles, cloth weave, and paint chips.
2. Minor rope fibers and secondary lashings.
3. Small base stones and small stake cuts.
4. Back-facing cloth and underside detail.
5. Horn bevels that do not affect the primary fork silhouette.

Never reduce the forked silhouette before removing small detail.

## Collision Notes

Default collision should be disabled or simple.

- Use no collision for non-contact visual dressing.
- If later player contact is expected, use one simple capsule or box for the mounting shaft and one low primitive for the base.
- Do not create per-horn, per-rope, per-cloth, per-stone, or per-chip collision.
- Do not define nav blockers, gameplay volumes, aura volumes, signal volumes, trigger volumes, objective volumes, pickup collision, or destructible collision in this package.

## Animation Notes

No animation is planned.

- Horn fork, mount, lashings, cloth accent, and base should remain static.
- No cloth simulation, wind animation, physics sway, signal pulse, aura pulse, shamanic state change, breakage, pickup animation, or audio-reactive motion is authorized.

## Unreal Import Notes

Future import path if approved:

- Static Mesh: `/Game/Aerathea/Props/Giants/BloodAxe/PathMarkers/SM_GIA_BloodAxeHornForkMarker_A01`
- Material instances: `/Game/Aerathea/Materials/Instances/Giants/BloodAxe/PathMarkers/`
- Textures: `/Game/Aerathea/Textures/Giants/BloodAxe/PathMarkers/`

Suggested import settings:

- Import uniform scale: 1.0.
- Units: centimeters.
- Pivot: ground center under the stake, socket, or base.
- Collision: disabled by default or simple collision only if later approved.
- Generate missing collision: off unless implementation task overrides it.
- LODs: LOD0-LOD3 required before game-ready use.

Do not create Unreal assets, material instances, Blueprints, sockets, validators, startup placement, VFX hooks, or runtime hooks from this package.

## Folder and Naming Recommendation

Docs:

- `docs/assets/props/SM_GIA_BloodAxeHornForkMarker_A01/PRODUCTION_PACKAGE.md`

Future source folders only after approval:

- `SourceAssets/Blender/Props/Giants/BloodAxe/PathMarkers/SM_GIA_BloodAxeHornForkMarker_A01/`
- `SourceAssets/Exports/Props/Giants/BloodAxe/PathMarkers/SM_GIA_BloodAxeHornForkMarker_A01/`

Future Unreal naming:

- `SM_GIA_BloodAxeHornForkMarker_A01`
- `MI_GIA_BloodAxeHornForkMarker_A01`
- `T_GIA_BloodAxeHornForkMarker_A01_BC`
- `T_GIA_BloodAxeHornForkMarker_A01_N`
- `T_GIA_BloodAxeHornForkMarker_A01_ORM`

No source folder, export folder, Unreal asset, material instance, VFX asset, or runtime file is created by this docs-only package.

## Quality Gate Checklist

- Asset is original to Aerathea and belongs to the Blood Axe hostile Giant sub-faction only.
- Neutral/civilized Giant culture remains separate and is not replaced by Blood Axe path-marker language.
- Validated Giant scale is explicit: female 442 cm / 14 ft 6 in and male 470 cm / 15 ft 5 in.
- Silhouette is readable as a forked horn path warning from MMO camera distance.
- Prop is buildable as a mid-poly static mesh.
- Materials use weathered horn, scorched timber or rough stone, rope/hide, ash, mud, soot, and restrained oxide red accent.
- No signal device, faction aura, VFX pulse, shamanic state, ritual mechanic, waypoint behavior, trail-marker gameplay, objective logic, nav/pathfinding behavior, UI marker, AI behavior, interaction, destructible behavior, pickup/loot behavior, or startup placement is defined.
- No DCC source, FBX export, Unreal Content, runtime source, validator file, final visual approval, first implementation target, source concept movement, or Hermes work is authorized.
- Triangle budget, texture plan, LOD plan, collision limits, Unreal import notes, and naming recommendations are included.
