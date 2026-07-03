# SM_GIA_BloodAxeBoneHornPathMarker_A01 Production Package

## Art Direction Summary

- Asset name: `SM_GIA_BloodAxeBoneHornPathMarker_A01`
- Asset type: Static Mesh production package / docs-only path-marker prop planning
- Parent kit: `KIT_GIA_BloodAxePathMarkers_A01`
- Source planning row: `BloodAxeCamp.png#PathMarkers_BoneHornMarker_A01`
- Faction/theme: Blood Axe Tribe, hostile Giant sub-faction only
- Status: docs-only production package ready

`SM_GIA_BloodAxeBoneHornPathMarker_A01` is a sparse, non-graphic Blood Axe route warning made from one old horn or dull bone lashed to a short stake or cairn side. It should read as hostile Giant camp dressing from MMO camera distance without becoming gore, loot, ritual equipment, a resource node, or a gameplay marker.

Blood Axe identity must remain separate from neutral/civilized Giant culture. Do not use civic stoneworker motifs, blue-gray cave-town masonry, terrace/waterwork language, warm hearth settlement dressing, refined highland route markers, polished clan signs, or restrained blue-rune culture as the default read.

This package is planning only. It does not authorize DCC source creation, FBX export, Unreal Content creation, startup placement, runtime gameplay, validator creation, source concept movement, final visual approval, first implementation target selection, or Hermes work.

## Gameplay Purpose

The prop supports static visual hostility and path readability in Blood Axe camp spaces. It may visually reinforce rough path bends, approach turns, camp threshold edges, and stronghold-adjacent warning clusters.

Allowed planning uses:

- Mark a hostile Blood Axe route edge as visual dressing only.
- Add a low-to-mid-height horn or bone silhouette beside cairns, cloth stakes, shield scraps, and ash bases.
- Break up repeated stone/cloth markers with a single primitive warning shape.
- Show that the Blood Axe tribe leaves crude hostile signs without defining any mechanics.

Out of scope:

- Gore escalation, loot drop, pickup behavior, crafting resource, ritual mechanic, faction aura, morale system, AI marker, patrol marker, spawn marker, objective logic, trail-marker gameplay, waypoint behavior, nav/pathfinding behavior, UI marker, VFX pulse, audio cue, interaction behavior, destructible behavior, or startup placement.

## Silhouette Notes

Primary read:

- One blunt horn, old bone, or paired short bone forms lashed to a rough stake or the side of a small stone base.
- Height should sit below large banner poles and watch markers but remain readable against Giant-scale camp props.
- The silhouette should be asymmetrical and crude, with one dominant fork, curve, or protruding bone line.
- The base may include one or two chunky stones, a scorched stake, broad rope lashings, and a small ash/mud footprint.

Model as real geometry when promoted later:

- Main horn or bone form, stake shaft, major rope lashings, one or two base stones, and broad mud/ash base shape.

Keep in textures or normal maps:

- Fine pitting, bone pores, horn ridges, rope fibers, tiny scratches, soot speckles, ash flecks, small cracks, and dried mud streaks.

Avoid:

- Skull piles, graphic gore, trophy walls, readable text, glowing symbols, UI arrows, dense bones, delicate feathers, refined signs, or excessive micro-detail.

## Scale Notes

Use the validated `SK_GIA_Base_A01` scale lock:

- Female Giant baseline: 442 cm / 14 ft 6 in.
- Male Giant baseline: 470 cm / 15 ft 5 in.
- Approved Giant ranges: females 14-15 ft / 427-457 cm; males 14 ft 10 in-16 ft 0 in / 452-488 cm.
- Author future source in centimeters. 1 Unreal unit = 1 cm.

Planning dimensions:

- Overall height: 80-220 cm.
- Footprint: 80-250 cm.
- Stake diameter: 10-24 cm for a crude Giant-cut post.
- Dominant horn/bone length: 50-160 cm.
- Base stone or ash footprint: 80-220 cm wide.

The prop should feel placed by hostile Giants, not scaled up from human campsite dressing.

## Materials and Color Palette

Primary materials:

- Dull old bone and weathered horn.
- Scorched timber stake.
- Rawhide, rope, or sinew lashings.
- Rough field stone base.
- Soot, ash, mud, and trampled earth.
- Optional restrained oxide red cloth tie or paint smear.

Palette targets:

- Bone and horn: `#9E8C6B` to `#CDB78A`
- Charcoal and soot: `#111214` to `#2A2C2E`
- Scorched timber: `#22170F` to `#4A2B17`
- Rough stone and ash: `#2E2C28` to `#6C6254`
- Rope and hide: `#6C5434` to `#A88958`
- Oxide red accent: `#5F1513` to `#8B211B`

No default emissive is approved. Ritual glow, signal glow, shamanic effects, VFX pulses, or animated material states require a separate approval gate.

## Concept Image Prompt

Create an original stylized fantasy MMORPG production concept image of `SM_GIA_BloodAxeBoneHornPathMarker_A01` for the world of Aerathea. The design should emphasize a sparse non-graphic Blood Axe Giant path warning, one dull horn or old bone lashed to a scorched stake or cairn side, rough field stone, rope and hide ties, soot, mud, restrained oxide red cloth or paint, hostile Giant sub-faction identity, clear separation from neutral/civilized Giant culture, and the gameplay role of static non-interactive route readability. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, no default emissive glow, and MMO-friendly mid-poly production design. Present it as a single prop concept sheet with front, side, scale notes beside a 442 cm female Giant and a 470 cm male Giant, material swatches, and LOD/collision callouts on a clean background. Avoid copying any existing franchise, avoid gore, avoid skull piles, avoid readable text, avoid waypoint behavior, avoid trail-marker gameplay, avoid pickup or loot behavior, avoid ritual mechanics, avoid DCC or Unreal implementation claims, and avoid excessive micro-detail that would not translate to a mid-poly Unreal asset.

## Modeling Notes

This is a docs-only modeling plan. No DCC source, sculpt, retopo, UV, bake, FBX export, Unreal asset, collision proxy, proof render, material graph, validator, startup actor, runtime source, final visual approval, or Hermes file is created or authorized by this package.

Future modeling should prioritize:

- A ground-centered pivot for terrain placement.
- One dominant horn or bone silhouette with a clear profile.
- Broad rope lashings that are readable from gameplay camera distance.
- Chunky stake and base forms with simple bevels.
- Static cloth or paint accents only if they improve Blood Axe readability.
- A base footprint that visually grounds the marker without implying collision or trail gameplay.

Do not introduce sockets, pickup affordances, inventory scale cues, resource-node shapes, destructible chunks, trigger volumes, aura radii, pathfinding helpers, waypoint arrows, or ritual gameplay elements.

## Texture and Material Notes

Target material strategy:

- 1 material slot preferred for the full prop.
- 2 material slots only if horn/bone and stone/timber/cloth need separation for reuse.
- Shared atlas should align with `KIT_GIA_BloodAxePathMarkers_A01` if later approved.

Suggested future material instances:

- `MI_GIA_BloodAxeBoneHorn_A01`
- `MI_GIA_BloodAxePathMarkerStone_A01`
- `MI_GIA_BloodAxePathMarkerClothHide_A01`

Required future texture set if a unique prop set is approved:

- `T_GIA_BloodAxeBoneHornPathMarker_A01_BC`
- `T_GIA_BloodAxeBoneHornPathMarker_A01_N`
- `T_GIA_BloodAxeBoneHornPathMarker_A01_ORM`

Optional emissive texture is not part of this package.

Packed `ORM` plan:

- R: Ambient occlusion around lashings, horn/bone contact, stake base, and stone/mud contact.
- G: High roughness for bone, horn, rope, timber, stone, soot, ash, and mud.
- B: Metallic black unless a small blackened iron tack or clamp is later approved.

## Triangle Budget

Target LOD0 budget:

- 800-3k tris.
- 1 material preferred, 2 maximum if justified.
- 512-1K texture set, or shared path-marker atlas.

Spend geometry on the dominant horn/bone silhouette, stake shaft, major rope lashings, base stones, and broad ash/mud footprint. Do not spend geometry on tiny chips, rope fibers, bone pores, soot flecks, scratches, or small fray.

## LOD Plan

All important future modules require LOD0-LOD3.

- LOD0: full horn/bone shape, stake, major lashings, chunky base, broad cloth or paint accent, and ash/mud grounding.
- LOD1: 60-70 percent of LOD0; reduce bevels, simplify lashings, flatten small base chips, and reduce minor horn ridges.
- LOD2: 35-45 percent of LOD0; preserve the horn/bone warning silhouette, stake read, and base mass while removing secondary cuts and small ties.
- LOD3: 15-25 percent of LOD0; preserve the broad horn/bone and stake silhouette only, with simplified base volume.

Reduction order:

1. Tiny scratches, pores, soot flecks, ash speckles, and paint chips.
2. Minor rope fibers and secondary lashings.
3. Small base stones and undercuts.
4. Small horn chips and bone bevels.
5. Back-facing detail and underside detail.

Never reduce the hostile horn/bone silhouette before removing small detail.

## Collision Notes

Default collision should be disabled or simple.

- Use no collision for visual dressing in non-contact placement.
- If player contact is later expected, use one slim capsule or box for the stake and one simple primitive around the base.
- Do not create per-bone, per-horn, per-rope, or per-stone collision.
- Do not define nav blockers, gameplay volumes, aura volumes, trigger volumes, objective volumes, pickup collision, or destructible collision in this package.

## Animation Notes

No animation is planned.

- Horn, bone, stake, lashings, cloth accent, and base should remain static.
- No cloth simulation, wind animation, physics sway, breakage, pickup animation, signal pulse, ritual state, or audio-reactive motion is authorized.

## Unreal Import Notes

Future import path if approved:

- Static Mesh: `/Game/Aerathea/Props/Giants/BloodAxe/PathMarkers/SM_GIA_BloodAxeBoneHornPathMarker_A01`
- Material instances: `/Game/Aerathea/Materials/Instances/Giants/BloodAxe/PathMarkers/`
- Textures: `/Game/Aerathea/Textures/Giants/BloodAxe/PathMarkers/`

Suggested import settings:

- Import uniform scale: 1.0.
- Units: centimeters.
- Pivot: ground center below the main stake or base.
- Collision: disabled by default or simple collision only if later approved.
- Generate missing collision: off unless implementation task overrides it.
- LODs: LOD0-LOD3 required before game-ready use.

Do not create Unreal assets, material instances, Blueprints, sockets, validators, startup placement, or runtime hooks from this package.

## Folder and Naming Recommendation

Docs:

- `docs/assets/props/SM_GIA_BloodAxeBoneHornPathMarker_A01/PRODUCTION_PACKAGE.md`

Future source folders only after approval:

- `SourceAssets/Blender/Props/Giants/BloodAxe/PathMarkers/SM_GIA_BloodAxeBoneHornPathMarker_A01/`
- `SourceAssets/Exports/Props/Giants/BloodAxe/PathMarkers/SM_GIA_BloodAxeBoneHornPathMarker_A01/`

Future Unreal naming:

- `SM_GIA_BloodAxeBoneHornPathMarker_A01`
- `MI_GIA_BloodAxeBoneHornPathMarker_A01`
- `T_GIA_BloodAxeBoneHornPathMarker_A01_BC`
- `T_GIA_BloodAxeBoneHornPathMarker_A01_N`
- `T_GIA_BloodAxeBoneHornPathMarker_A01_ORM`

No source folder, export folder, Unreal asset, or material instance is created by this docs-only package.

## Quality Gate Checklist

- Asset is original to Aerathea and belongs to the Blood Axe hostile Giant sub-faction only.
- Neutral/civilized Giant culture remains separate and is not replaced by Blood Axe path-marker language.
- Validated Giant scale is explicit: female 442 cm / 14 ft 6 in and male 470 cm / 15 ft 5 in.
- Silhouette is readable as a sparse horn/bone path warning from MMO camera distance.
- Prop is buildable as a mid-poly static mesh.
- Materials use dull bone/horn, scorched timber, rope/hide, rough stone, soot, ash, mud, and restrained oxide red accent.
- No gore escalation, loot, pickup, crafting resource, ritual mechanic, waypoint behavior, trail-marker gameplay, objective logic, nav/pathfinding behavior, UI marker, VFX/audio, interaction, destructible behavior, or startup placement is defined.
- No DCC source, FBX export, Unreal Content, runtime source, validator file, final visual approval, first implementation target, source concept movement, or Hermes work is authorized.
- Triangle budget, texture plan, LOD plan, collision limits, Unreal import notes, and naming recommendations are included.
