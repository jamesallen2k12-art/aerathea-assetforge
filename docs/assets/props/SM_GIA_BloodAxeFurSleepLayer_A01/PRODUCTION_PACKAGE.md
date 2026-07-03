# SM_GIA_BloodAxeFurSleepLayer_A01 Production Package

Asset status: docs-only production package. No DCC, no Unreal work, no startup placement, no final approval, and no implementation target are created by this package.

## 1. Art Direction Summary

`SM_GIA_BloodAxeFurSleepLayer_A01` is a broad, worn fur or hide sleep layer for Blood Axe Giant camp bedding. It is old, practical, static ground dressing used to make hostile Giant shelters feel occupied without implying a usable bed, resource object, loot object, or inventory item.

The visual read should be rough and utilitarian: smoke-dark hide, matted fur edges, patched wear, mud staining, ash, soot, and a few oversized repair seams. Keep it non-graphic and finished as camp bedding, not fresh hide processing, not a display piece, and not a trophy escalation.

Blood Axe remains a hostile Giant sub-faction. This asset must stay separate from neutral or civilized Giant culture: do not use refined cave-town craft, blue-gray civic masonry language, clean highland bedding, warm hearth comfort cues, restrained blue rune language, or master stoneworker symbols.

## 2. Gameplay Purpose

This is static environmental dressing for Blood Axe camps, lean-to interiors, awning edges, and rough sleeping rows. It communicates Giant scale, hard living conditions, and hostile war-camp practicality.

This package defines no gameplay behavior. There is no harvesting, no trophy escalation, no gore read, no resource pickup, no loot, no inventory behavior, no usable bed behavior, no sleeping or resting behavior, no interaction prompt, no search behavior, no crafting behavior, no container UI, and no AI or player system hook.

## 3. Silhouette Notes

- Primary silhouette: very low, broad, irregular fur or hide layer with a flattened central sleeping surface and uneven curled edges.
- Shape language: asymmetric pelt-like blanket, heavy and sagging, with one or two lifted corners and a few broad folds visible from gameplay camera height.
- Edge treatment: matted fur rim, patchy torn outline, blunt old wear, and compressed corners. Keep all torn edges non-graphic.
- Surface breakup: use three to five large readable panels or fold zones, not dense strips or tiny modeled tufts.
- Repair details: a few oversized rawhide stitches, patch seams, or tied repair tabs may be included, but these should read as practical field repairs.
- Exclusions: no heads, limbs, bones, fresh cuts, blood marks, butchery presentation, trophy display composition, readable faction text, or ritual display framing.

## 4. Scale Notes

Giant scale lock is fixed for this package:

- Female Giant baseline: 442 cm / 14 ft 6 in.
- Male Giant baseline: 470 cm / 15 ft 5 in.

Target prop footprint:

- Length: 520-650 cm.
- Width: 260-380 cm.
- Base thickness: 6-14 cm.
- Raised curl or folded edge height: 20-45 cm maximum.

The layer should feel large enough for a Giant to sleep on or under as a rough camp layer, but it should remain low to the ground and non-blocking. Do not resize the asset to human bedding proportions. Keep the pivot at bottom center for simple placement on uneven camp floors, hide shelters, and packed earth.

## 5. Materials and Color Palette

Primary materials:

- Old rough hide.
- Matted fur edge.
- Patched leather underside.
- Rawhide stitch or repair tabs.
- Embedded mud, ash, soot, and camp grime.

Color palette:

- Smoke black brown.
- Dark umber.
- Desaturated tawny fur.
- Charcoal gray soot.
- Mud brown.
- Bone-tan worn frays.
- Muted oxide red only as a tiny cloth tag or repair accent if needed.

Do not use emissive materials. Do not use civilized Giant blue-gray stone, refined textile patterns, clean hearth blankets, decorative blue runes, polished metal, or neutral highland craft motifs.

## 6. Concept Image Prompt

Create an original stylized fantasy MMORPG concept image of a broad worn fur or hide sleep layer for the Blood Axe Giant camp culture of Aerathea. The design should emphasize a low irregular bedding silhouette, old smoke-dark hide, matted fur edges, patched leather repairs, rawhide stitch accents, hostile Giant war-camp practicality, non-graphic wear, and static environmental dressing. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, no emissive accents, and MMO-friendly production design. Present it as a single prop concept sheet with top view, three-quarter view, scale notes for a 442 cm female Giant and 470 cm male Giant, and material swatches on a clean neutral background. Avoid copying any existing franchise, avoid excessive micro-detail that would not translate to a mid-poly Unreal asset, and avoid harvesting, trophy escalation, gore read, resource pickup, loot, inventory, or usable-bed presentation.

## 7. Modeling Notes

This task does not create DCC work. The following notes are for a future approved DCC task only.

- Build as one static mesh with a low, broad, irregular footprint.
- Model the main sleeping surface as a shallow padded slab with uneven edge thickness.
- Use real geometry for the largest curled corners, folded edge lips, broad depressions, and major overlap panels.
- Keep fur texture mostly material-driven; only use simple silhouette geometry for the largest matted edge clumps.
- Use normal maps and baked detail for fine fur strands, scratches, stitch holes, wrinkles, mud spatters, ash flecks, and leather grain.
- Avoid alpha-heavy fur cards unless a later art review explicitly approves them; the default target should be opaque, MMO-safe geometry and texture work.
- Keep underside detail minimal: enough to read as patched leather if the edge lifts, but not a fully detailed reversible prop.
- Do not add bones, skulls, claws, fresh hide processing tools, gore elements, readable trophies, containers, pockets, or removable items.
- Freeze all folds and wrinkles into the mesh. No cloth simulation, rope simulation, physics bodies, dangling motion, or runtime deformation.

## 8. Texture and Material Notes

Recommended material count: 1 material slot.

Recommended texture set:

- `T_GIA_BloodAxeFurSleepLayer_A01_BC` - base color with hand-painted hide, fur, mud, soot, ash, and worn repair color.
- `T_GIA_BloodAxeFurSleepLayer_A01_N` - normal map for broad hide wrinkles, compressed fur, shallow stitch holes, leather grain, and edge wear.
- `T_GIA_BloodAxeFurSleepLayer_A01_ORM` - packed occlusion, roughness, metallic. Metallic should remain black.

No emissive texture is needed. Do not create `T_GIA_BloodAxeFurSleepLayer_A01_E` unless a later task changes the art direction, which is not expected for this prop.

Texture resolution target: 2K for LOD0 source texture, with 1K acceptable for repeated camp dressing variants. Use hand-painted value grouping and baked AO-style contact depth so the broad folds read from gameplay distance. Keep small fur strands, leather pores, stitch fibers, scratches, soot speckles, ash flecks, and mud stains in texture or normal detail rather than modeled geometry.

## 9. Triangle Budget

This is a large-footprint prop with low mesh complexity.

- LOD0 target: 2,000-4,000 triangles.
- LOD1 target: 1,000-1,800 triangles.
- LOD2 target: 400-800 triangles.
- LOD3 target: 120-300 triangles.

The budget should prioritize the irregular outline, broad fold silhouettes, and a few raised corners. Do not spend triangles on dense fur strands, tiny stitch geometry, tiny tears, or underside detail that will rarely be visible.

## 10. LOD Plan

- LOD0: Full irregular outline, primary curled edges, broad folds, major panel overlaps, and limited raised corner detail.
- LOD1: Reduce edge loops, simplify panel overlap ridges, merge smaller fold zones, and remove small underside thickness changes.
- LOD2: Preserve the main footprint and two or three large fold forms; flatten minor curls and simplify matted fur edge geometry.
- LOD3: Low flattened silhouette proxy with only the largest outline breaks and one broad central depression.

LOD reduction order:

1. Tiny stitch geometry or repair tabs.
2. Small edge clumps.
3. Secondary folds.
4. Underside hints.
5. Minor corner curls.
6. Panel seam bevels.

Never destroy the broad bedding footprint or Giant-scale read first.

## 11. Collision Notes

This task creates no collision assets.

For a future approved implementation, use simple collision only:

- Preferred collision: one low simple box or two to three simple convex hulls covering the broad footprint.
- Collision height should remain shallow so the layer does not behave like a wall, chest, or gameplay blocker.
- Do not author cloth collision, physics bodies, ragdoll collision, pickup collision, usable-bed volumes, interaction volumes, nav blockers, cover tags, or resource-node collision.
- If the asset is used in dense shelter dressing, collision may be disabled or reduced to decorative-only query settings by a later Unreal owner.

## 12. Animation Notes

This is a static mesh prop.

- No skeletal rig.
- No animation clips.
- No cloth simulation.
- No physics simulation.
- No wind animation.
- No material animation.
- No Blueprint-driven state changes.
- No sockets are required.

All wrinkles, folded corners, and bedding compression should be baked into the static mesh for any future implementation.

## 13. Unreal Import Notes

This package performs no Unreal work. It creates no Content assets, no Blueprint, no material instance, no texture import, no map placement, no validator, no startup scene actor, no final approval, and no implementation target.

Future import recommendation only if a later task explicitly approves implementation:

- Asset name: `SM_GIA_BloodAxeFurSleepLayer_A01`.
- Asset type: Static Mesh.
- Suggested Unreal folder: `/Game/Aerathea/Props/Giants/BloodAxe/Bedrolls/`.
- Unit scale: centimeters, 1 Unreal unit = 1 cm.
- Pivot: bottom center of the bedding footprint.
- Forward orientation: align longest axis along local X unless a later kit layout requires otherwise.
- Material slots: 1.
- Material instance: `MI_GIA_BloodAxeFurSleepLayer_A01`.
- Texture names: `T_GIA_BloodAxeFurSleepLayer_A01_BC`, `T_GIA_BloodAxeFurSleepLayer_A01_N`, `T_GIA_BloodAxeFurSleepLayer_A01_ORM`.
- Collision: simple shallow collision only if needed by placement context.
- Sockets: none.
- Blueprint behavior: none.
- Performance note: treat as repeated camp dressing; avoid expensive shader features, opacity-heavy fur, or unique 4K textures.

## 14. Folder and Naming Recommendation

Documentation path for this task:

- `docs/assets/props/SM_GIA_BloodAxeFurSleepLayer_A01/PRODUCTION_PACKAGE.md`

Recommended future asset names if implementation is later approved:

- Static Mesh: `SM_GIA_BloodAxeFurSleepLayer_A01`
- Material Instance: `MI_GIA_BloodAxeFurSleepLayer_A01`
- Base Color: `T_GIA_BloodAxeFurSleepLayer_A01_BC`
- Normal: `T_GIA_BloodAxeFurSleepLayer_A01_N`
- Packed ORM: `T_GIA_BloodAxeFurSleepLayer_A01_ORM`

No DCC source folder, Unreal Content folder, runtime source file, Hermes file, global index update, external source concept copy, or startup placement is created by this package.

## 15. Quality Gate Checklist

- [ ] The package uses all 15 universal Aerathea package sections.
- [ ] The asset is original to Aerathea and supports the Blood Axe hostile Giant sub-faction only.
- [ ] Blood Axe visual language remains separate from neutral and civilized Giant culture.
- [ ] Giant scale lock is explicit: female 442 cm / 14 ft 6 in and male 470 cm / 15 ft 5 in.
- [ ] The prop reads as a broad worn fur or hide bedding layer: old, practical, non-graphic, and static.
- [ ] The primary silhouette is readable from gameplay camera height.
- [ ] Materials are limited to old hide, matted fur, patched leather, rawhide repairs, mud, ash, and soot.
- [ ] No emissive material, blue rune language, refined Giant civic craft, warm hearth blanket language, or polished neutral Giant read is introduced.
- [ ] Fine fur, stitch fibers, scratches, soot speckles, ash flecks, mud stains, and leather grain are assigned to textures or normals.
- [ ] Triangle budgets include LOD0, LOD1, LOD2, and LOD3.
- [ ] Collision guidance stays simple, shallow, and non-gameplay.
- [ ] Animation guidance confirms static mesh only.
- [ ] Unreal notes are future recommendations only and create no Unreal assets.
- [ ] There is no DCC, no Unreal work, no startup placement, no final approval, and no implementation target.
- [ ] There is no harvesting, no trophy escalation, no gore read, no resource pickup, no loot, no inventory behavior, no usable-bed behavior, no sleeping or resting behavior, and no interaction behavior.
- [ ] No external source concepts are copied, moved, edited, embedded, inspected for visual approval, or committed.
- [ ] The package changes only `docs/assets/props/SM_GIA_BloodAxeFurSleepLayer_A01/PRODUCTION_PACKAGE.md`.
