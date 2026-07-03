# KIT_GIA_BloodAxeSleepingRow_A01 Production Package

## 1. Art Direction Summary

`KIT_GIA_BloodAxeSleepingRow_A01` is a docs-only production package for a Blood Axe hostile Giant sub-faction camp-dressing row of two to four rough bedding forms placed near hide shelters, lean-tos, or camp wall edges. The row should read as a Giant-scale sleeping footprint without becoming a usable bed, gameplay rest station, spawn marker, or AI behavior point.

The visual language is brutal, low, heavy, dirty, and temporary: broad hide mats, flattened fur layers, patched leather, rawhide lashings, rope coils, soot, ash, mud, oxide red cloth tags, and occasional blackened iron tie rings. This package is for Blood Axe war-camp clutter only and must stay separate from neutral or civilized Giant culture, including refined cave-town bedding, clean highland nomad craft, blue-gray civic masonry, warm hearth comfort, restrained blue runes, or polished stoneworker symbols.

This is a planning handoff only: no DCC, no Unreal, no startup placement, no final approval, no implementation target, no sleeping system, no spawn point, no AI rest behavior, and no interaction marker.

## 2. Gameplay Purpose

- Role: static environmental storytelling and scale dressing for Blood Axe camp shelters.
- Use case: show where hostile Giant raiders sleep or collapse between raids, giving the camp a lived-in footprint and reinforcing the size difference between Giants and smaller races.
- Player read: hostile encampment life, rough war-camp discipline, temporary shelter adjacency, and Giant-scale occupancy.
- Non-goals: no usable bed, no rest buff, no checkpoint, no respawn, no patrol or idle anchor, no inventory, no loot, no pickup, no salvage, no resource node, no UI prompt, no quest marker, no cover definition, and no nav/pathfinding rule.

## 3. Silhouette Notes

- Overall form: a staggered row of two to four low, broad, rough bedding shapes with varied lengths and angles so the row feels placed by massive bodies rather than aligned like barracks furniture.
- Primary silhouettes:
  - One broad hide mat with an uneven oval or rectangular footprint.
  - One thicker fur or hide layer with a raised shoulder mass and sagging edge.
  - Optional bundled end roll or folded hide lip at one side.
  - Optional stake-and-rope tie point near the row edge for camp anchoring.
- Layout rhythm: each bedding form should overlap or offset slightly, leaving clear gaps that reveal the ground plane and avoid a single merged blob.
- Readability rules: model only the large bedding masses, folded edges, major straps, anchor stakes, and large rope turns. Push hide grain, fur strands, stitching, soot speckles, scratches, mud splatter, and cloth weave into future texture or normal detail.
- Avoid: neat mattresses, civilian comfort, refined blankets, symbolic civic patterns, blue-rune decoration, readable text, gore display, trophy escalation, or UI-like markers.

## 4. Scale Notes

- Giant scale lock: female Giant baseline is 442 cm / 14 ft 6 in; male Giant baseline is 470 cm / 15 ft 5 in.
- Approved Giant range remains female 14-15 ft and male 14 ft 10 in-16 ft 0 in. This package must not change the validated scale lock.
- Row footprint target: approximately 700-1200 cm long across the row, depending on whether two, three, or four bedding forms are present.
- Individual bedding target: approximately 450-650 cm long, 180-280 cm wide, and 12-55 cm high depending on folded hide, fur, or support thickness.
- Shelter clearance: keep the row low and edge-aligned so it can sit near a Blood Axe shelter without implying a doorway blocker, nav blocker, or gameplay volume.
- Human-scale contrast: a normal humanoid should read as small beside the row, but no shipped comparison marker is included in this docs-only package.

## 5. Materials and Color Palette

- Primary materials: rough hide, patched leather, worn fur, rawhide straps, heavy rope, muddy ground contact, soot-darkened bedding, scorched timber stakes, and blackened iron rings.
- Accent materials: oxide red cloth tags, faded clan wraps, dull bone toggles, and ash-stained leather patches.
- Color palette: dark umber, smoke black, dirty tan, old hide brown, matted gray fur, dull rawhide beige, oxide red, muted rust, and dry mud gray.
- Surface treatment: hand-painted wear, baked-AO-style depth, broad dirt gradients, heavy underside shadow, and normal-map-style hide folds.
- Emissive policy: no default emissive. Do not add blue runes, magical glow, forge glow, shamanic glow, ritual glow, VFX pulses, or animated material states.
- Culture separation: Blood Axe bedding is hostile raider camp clutter. It must not borrow neutral or civilized Giant cave-town materials, refined highland bedding, civic stoneworker patterns, warm hearth presentation, blue-gray masonry motifs, or restrained blue rune language.

## 6. Concept Image Prompt

Create an original stylized fantasy MMORPG concept image of `KIT_GIA_BloodAxeSleepingRow_A01`, a row of two to four rough Giant-scale bedding forms near Blood Axe camp shelters for the world of Aerathea. The design should emphasize a low staggered row silhouette, oversized hide mats, matted fur layers, patched leather, rawhide lashings, heavy rope, soot, ash, mud, oxide red cloth tags, hostile Blood Axe Giant sub-faction identity, grim war-camp mood, and static shelter-adjacent environmental storytelling. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, no emissive accents, and MMO-friendly production design. Present it as a concept sheet with a top-down footprint row, a low three-quarter hero view, and simple Giant scale callouts on a clean neutral background. Avoid copying any existing franchise, avoid neutral or civilized Giant culture, avoid readable text, avoid gore escalation, avoid UI markers, and avoid excessive micro-detail that would not translate to a mid-poly Unreal asset.

## 7. Modeling Notes

- Package type: kit planning row composed from future bedding forms and small anchor dressing pieces. This document does not select a first DCC target.
- Model as simple, readable mid-poly forms if later approved:
  - Two to four broad bedding bases with uneven flattened profiles.
  - Folded hide lips or raised fur edges on one or two forms.
  - One or two large strap bands per selected bedding form.
  - Optional rope coil or stake anchor only if it supports the row silhouette.
  - Ground-contact sag and asymmetric compression to show heavy Giant use.
- Use modular variation rather than unique sculpt complexity: rotate, offset, mirror, or scale future forms within approved bounds to avoid repetition.
- Keep underside and backside details minimal because this is shelter-edge dressing.
- Avoid cloth simulation, dynamic ropes, physics bodies, skeletal rigs, socket authoring, destructible parts, or gameplay markers.
- Do not create DCC source, sculpt, retopo, UVs, bakes, proof renders, FBX exports, Unreal Content, startup actors, validators, or runtime files from this package.

## 8. Texture and Material Notes

- Future texture set, if approved: Base Color, Normal, Ambient Occlusion, packed ORM, and no Emissive map by default.
- Recommended material count if later implemented: 2 material slots maximum for the full row.
  - `MI_GIA_BloodAxeHideBedding_A01`: hide, leather, fur, straps, rope, and oxide red tag accents.
  - `MI_GIA_BloodAxeGroundContact_A01`: optional shared dirt, ash, and mud underside blend if needed.
- Texture resolution target if later implemented: 2K for a row kit, with 1K acceptable for repeated variants or distant camp dressing.
- Texture detail assignment:
  - Normal map: hide wrinkles, leather stitching, rope fibers, shallow fur clumps, dents, and compressed bedding ridges.
  - AO: heavy contact shadow under folds, between overlapping forms, and around tied straps.
  - ORM: rough, non-metal bedding surfaces; blackened iron rings only as small low-metallic accents if included.
  - Base Color: broad hand-painted color blocks and dirt gradients, not noisy photo detail.
- No readable clan text, no painted UI symbols, no fresh blood focus, and no glowing material state.

## 9. Triangle Budget

Planning budget only; no mesh is created by this package.

- Full row LOD0 target: 8k-16k triangles total for two to four bedding forms plus small anchor dressing.
- Individual bedding form target: 2k-4k triangles at LOD0.
- Optional rope, stake, or ring accents: 300-1.5k triangles total, kept secondary to bedding silhouettes.
- Material slots: 1-2 maximum.
- Texture set: 1 shared 2K set preferred; no 4K hero texture unless a later lead-approved hero camp review requires it.
- Performance priority: preserve the Giant-scale low row silhouette first; reduce micro folds, straps, rope turns, and underside details before reducing the main bedding mass.

## 10. LOD Plan

- LOD0: full readable row with two to four varied bedding forms, large folds, main straps, optional rope or stake anchor, and broad ground-contact deformation.
- LOD1: reduce to roughly 50-60 percent of LOD0. Simplify folded edges, remove minor strap bevels, reduce rope segment count, and merge small underside ridges.
- LOD2: reduce to roughly 25-35 percent of LOD0. Keep only the primary bedding footprints, largest folded lips, and one or two major straps per visible form.
- LOD3: reduce to roughly 10-15 percent of LOD0. Preserve the low staggered row footprint and color breakup; remove small stakes, rings, knots, and most secondary folds.
- LOD reduction order: tiny stitches and fray, small straps, minor folds, rope details, underside details, small stakes and rings, then secondary silhouette cuts.
- Never destroy the broad Giant sleeping footprint before distant LODs.

## 11. Collision Notes

- Docs-only collision planning; no collision proxies are created by this package.
- If later approved as static dressing, use simple non-blocking or low-profile simple collision only.
- Recommended future collision: one simplified low box or convex hull per bedding form, or no collision if the row is strictly background dressing.
- Avoid complex per-poly collision, cloth collision, physics bodies, nav blockers, cover volumes, trigger volumes, interaction traces, sleep markers, spawn volumes, or AI rest points.
- Collision should not imply the shelter entrance is blocked unless a separate level-design task explicitly owns that rule.

## 12. Animation Notes

- No animation is authorized or needed for this docs-only package.
- No cloth simulation, rope physics, secondary motion, idle motion, particle effects, material pulsing, or interactive state changes.
- The row must remain static environmental dressing unless a future approved task explicitly expands scope.
- Do not define sleeping behavior, rest behavior, AI rest behavior, spawn behavior, morale behavior, faction buffs, audio cues, or interaction marker states.

## 13. Unreal Import Notes

- Asset name: `KIT_GIA_BloodAxeSleepingRow_A01`.
- Asset type: docs-only kit production package; possible future Static Mesh kit only if separately approved.
- Current state: no Unreal import, no Content asset, no Blueprint Actor, no material instance, no texture import, no sockets, no validators, no startup scene placement, no capture, and no final visual approval.
- Future folder path if approved: `/Game/Aerathea/Environment/Giants/BloodAxe/Kits/SleepingRow/`.
- Future pivot recommendation: row center at ground level, Z = 0, with forward axis aligned along the row length for predictable shelter-edge placement.
- Future scale: 1 Unreal unit = 1 cm; preserve the Giant scale lock of female 442 cm / 14 ft 6 in and male 470 cm / 15 ft 5 in.
- Future collision: simple low-profile static collision or no collision, depending on level-design ownership.
- Future sockets: none.
- Future Blueprint behavior: none.
- Performance note: keep this as static camp dressing with no runtime logic.

## 14. Folder and Naming Recommendation

Docs-only path written by this task:

- `docs/assets/kits/KIT_GIA_BloodAxeSleepingRow_A01/PRODUCTION_PACKAGE.md`

Future naming recommendations if a later approved implementation task is opened:

- Static mesh kit: `SM_GIA_BloodAxeSleepingRow_A01`
- Optional kit label: `KIT_GIA_BloodAxeSleepingRow_A01`
- Material instance: `MI_GIA_BloodAxeHideBedding_A01`
- Base Color texture: `T_GIA_BloodAxeSleepingRow_A01_BC`
- Normal texture: `T_GIA_BloodAxeSleepingRow_A01_N`
- Packed ORM texture: `T_GIA_BloodAxeSleepingRow_A01_ORM`
- Emissive texture: none by default

Do not create source folders, DCC files, FBX exports, Unreal folders, Content assets, global index edits, task-board edits, Hermes files, or runtime source as part of this package.

## 15. Quality Gate Checklist

- [x] Uses the 15 universal Aerathea package sections.
- [x] Defines `KIT_GIA_BloodAxeSleepingRow_A01` as a row of two to four rough bedding forms showing Giant-scale sleeping footprint near camp shelters.
- [x] Keeps the package docs-only with no DCC, no Unreal, no startup placement, no final approval, and no implementation target.
- [x] Includes the Giant scale lock: female 442 cm / 14 ft 6 in and male 470 cm / 15 ft 5 in.
- [x] Keeps Blood Axe as a hostile Giant sub-faction separate from neutral and civilized Giant culture.
- [x] Uses Blood Axe material language: rough hide, patched leather, fur edges, rawhide, rope, scorched timber, blackened iron, soot, ash, mud, and oxide red cloth tags.
- [x] Excludes refined cave-town bedding, clean highland nomad craft, civic stoneworker symbols, warm hearth presentation, blue-gray masonry motifs, and restrained blue runes.
- [x] Assigns tiny hide grain, fur strands, rope fibers, cloth weave, fray, stitches, scratches, soot speckles, ash flecks, mud spatters, and wood grain to future textures or normals.
- [x] Includes triangle budget, LOD0-LOD3 plan, collision notes, animation notes, Unreal import guardrails, and naming recommendations.
- [x] States no sleeping system, no spawn point, no AI rest behavior, and no interaction marker.
- [x] Avoids loot, pickup, inventory, resource, crafting, salvage, cover, nav/pathfinding, destructible, VFX, audio, quest, and runtime behavior claims.
- [x] Does not claim final visual approval or select a first DCC or implementation target.
