# SM_GIA_BloodAxeTiedCampBundle_A01 Production Package

Docs-only production package for a Blood Axe Giant camp dressing prop. This package creates no DCC source, no Unreal Content, no startup placement, no final approval, and no implementation target.

## 1. Art Direction Summary

`SM_GIA_BloodAxeTiedCampBundle_A01` is a lumpy Giant-scale travel bundle for Blood Axe war-camp dressing. It reads as a dark hide-covered load that has been cinched shut with two thick straps, wrapped with heavy rope, and tied off with one large, blunt knot. The silhouette should feel overstuffed, uneven, heavy, and practical, not refined luggage or neutral Giant highland craft.

Blood Axe remains a hostile Giant sub-faction. This asset must stay visually separate from neutral or civilized Giant culture: no blue-gray civic masonry language, no clean terrace-town bedding, no warm hearth comfort read, no restrained blue rune identity, and no refined stoneworker symbols.

## 2. Gameplay Purpose

This is visual camp packing only. It supports Blood Axe camp storytelling by showing that raiders move in rough, temporary, hostile encampments with oversized travel goods, shelter clutter, and war-path baggage.

This package defines no bag inventory, no container UI, no loot, no pickup, no salvage, no interaction behavior, no resource behavior, no rest behavior, no sleeping behavior, no objective behavior, and no usable gameplay state.

## 3. Silhouette Notes

- Primary read: low, lumpy, hide-wrapped mass sized for Giant hands and Giant camps.
- Overall shape: broad oval mound with uneven side bulges and a slightly flattened base.
- Strap read: two thick straps must be visible from the main camera angle, either crossing over the top or running in offset bands across the bundle.
- Knot read: one large knot is a hero detail and should be readable at LOD0 and LOD1.
- Rope wrap: heavy rope should wrap around the bundle with a few broad turns, not many thin cords.
- Cover: dark hide cover should fold over the upper mass with heavy seams and blunt hide edges.
- Avoid: tidy merchant baggage, small human-scale sacks, refined packs, readable text labels, trophy gore, ritual glow, or decorative over-detail.

## 4. Scale Notes

Use the locked Giant scale baseline for review planning:

- Female Giant scale lock: 442 cm / 14 ft 6 in.
- Male Giant scale lock: 470 cm / 15 ft 5 in.

Target prop footprint:

- Length: 260-360 cm.
- Width: 150-220 cm.
- Height: 90-140 cm.

The bundle should feel portable only for Giants. It should be too large for normal humanoid races to carry, but small enough to sit beside a Blood Axe shelter, path bend, rough bedding row, or temporary camp pile without becoming a building-scale object.

## 5. Materials and Color Palette

- Dark hide cover: charcoal brown, smoke-black, deep umber, dull gray-black hide.
- Strap material: thick rawhide or cracked leather in dark brown and scorched tan.
- Rope material: coarse hemp, rawhide cord, or darkened fiber with muddy tan highlights.
- Knot material: same rope family, enlarged and simplified for readability.
- Accent color: sparing oxide red cloth tag or wrap scrap only if needed for Blood Axe identity.
- Dirt layer: soot, ash, dried mud, dust, and worn pale edge scuffs.

No emissive material is needed. No magic glow, shamanic glow, forge glow, Aetherium glow, UI marker color, or animated material state belongs on this asset.

## 6. Concept Image Prompt

Create an original stylized fantasy MMORPG concept image of a Blood Axe Giant tied camp bundle for the world of Aerathea. The design should emphasize a lumpy oversized travel-bundle silhouette, dark hide cover, two thick straps, a heavy rope wrap, one large readable knot, soot-dark Blood Axe raider material language, hostile temporary war-camp identity, and static visual camp-packing role. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, no emissive accents, and MMO-friendly production design. Present it as a single prop concept sheet with front, side, and top readability on a clean neutral background. Avoid copying any existing franchise and avoid excessive micro-detail that would not translate to a mid-poly Unreal asset.

## 7. Modeling Notes

- Build the main bundle as a simple uneven mound with a flattened underside and several broad bulges.
- Model the dark hide cover as large folded planes or shaped surface forms that sit over the mound, with only a few major folds.
- Model two straps as thick raised bands with chunky thickness and simple bevels.
- Model the rope wrap as a small number of broad rope turns. Do not model many fine rope fibers.
- Model the large knot as a simplified readable shape with 3-5 major lobes and short rope tails.
- Add a few large hide flap edges or folded corners, but keep all tiny stitches, fibers, scuffs, and hide grain in textures or normals.
- Keep the underside simple. This is a ground dressing prop and should not spend geometry on hidden bottom detail.
- Maintain a rough Blood Axe camp read without gore, graphic trophy material, or civilized Giant craft language.

## 8. Texture and Material Notes

Recommended future texture set:

- `T_GIA_BloodAxeTiedCampBundle_A01_BC`: dark hide, strap, rope, soot, ash, mud, and optional oxide red accent color.
- `T_GIA_BloodAxeTiedCampBundle_A01_N`: hide folds, leather cracks, rope twist suggestion, knot compression, edge dents, and broad seam relief.
- `T_GIA_BloodAxeTiedCampBundle_A01_ORM`: packed occlusion, roughness, and metallic. Metallic should remain black unless a later approved variant adds a tiny iron ring.

Material plan:

- One material slot preferred: `MI_GIA_BloodAxeTiedCampBundle_A01`.
- Roughness should stay high with dull hide, dusty rope, and matte soot.
- Fine hide grain, rope fibers, fray, scratches, stitching, mud spatters, ash flecks, and edge wear must be texture or normal detail, not individual modeled micro-geometry.
- No emissive map is required.

## 9. Triangle Budget

Treat as a large prop because it is Giant-scale camp dressing.

- LOD0 target: 3,500-6,000 tris.
- LOD1 target: 1,800-3,000 tris.
- LOD2 target: 700-1,200 tris.
- LOD3 target: 200-500 tris.

Use one material slot and a 1K texture set for normal camp use. A 2K texture set is acceptable only if this prop becomes a close-up hero dressing item in a later approved implementation task.

## 10. LOD Plan

- LOD0: full lumpy mound, two straps, rope wrap, readable knot, major hide cover folds, broad edge wear via texture.
- LOD1: preserve primary bundle shape, two straps, and knot; reduce rope roundness and simplify secondary hide folds.
- LOD2: merge minor bulges, flatten rope turns into fewer forms, keep strap bands and knot silhouette readable.
- LOD3: simplified mound with strap silhouettes and a blocky knot impression; remove small flap thickness and secondary folds.

Reduce tiny detail first: fray, stitch hints, small scratches, minor fold cuts, rope grooves, underside shaping, and small accent scraps. Do not destroy the primary lumpy bundle silhouette before distant LODs.

## 11. Collision Notes

Future collision should be simple and non-interactive:

- Collision type: simple static blocking or simple query collision only, depending on later placement needs.
- Preferred proxy: one low convex hull or two overlapping box/convex hulls around the mound.
- Do not trace rope, straps, knot lobes, or hide flaps with collision.
- Do not create cloth collision, physics bodies, rope physics, pickup collision, loot search volumes, interaction volumes, nav blockers, cover tags, or gameplay trigger volumes.

## 12. Animation Notes

No animation is planned.

Do not define cloth simulation, rope simulation, jiggle motion, carry motion, open/close states, inventory states, salvage states, pickup states, container states, interaction prompt states, VFX pulses, audio cues, or Blueprint-driven behavior for this docs-only package.

## 13. Unreal Import Notes

This task performs no Unreal work. These notes are future-facing only if a later approved implementation task selects the asset.

- Asset name: `SM_GIA_BloodAxeTiedCampBundle_A01`.
- Asset type: Static Mesh, future planning only.
- Pivot: centered on the flattened underside at ground contact.
- Scale: authored in centimeters; validate against female Giant 442 cm / 14 ft 6 in and male Giant 470 cm / 15 ft 5 in.
- Orientation: long axis forward or side-facing consistently with the future kit layout; keep top knot readable from the expected gameplay camera.
- Material slots: 1 preferred.
- Texture list: `T_GIA_BloodAxeTiedCampBundle_A01_BC`, `T_GIA_BloodAxeTiedCampBundle_A01_N`, `T_GIA_BloodAxeTiedCampBundle_A01_ORM`.
- LODs: LOD0, LOD1, LOD2, and LOD3 required for an important camp prop.
- Collision: simple convex or simple box-based proxy only.
- Sockets: none.
- Blueprint behavior: none.
- Runtime behavior: none.
- Startup placement: none.
- Final approval: not claimed.
- Implementation target: not selected.

## 14. Folder and Naming Recommendation

Docs package path:

- `docs/assets/props/SM_GIA_BloodAxeTiedCampBundle_A01/PRODUCTION_PACKAGE.md`

Future naming recommendation if separately approved:

- Static Mesh: `SM_GIA_BloodAxeTiedCampBundle_A01`
- Material Instance: `MI_GIA_BloodAxeTiedCampBundle_A01`
- Base Color: `T_GIA_BloodAxeTiedCampBundle_A01_BC`
- Normal: `T_GIA_BloodAxeTiedCampBundle_A01_N`
- ORM: `T_GIA_BloodAxeTiedCampBundle_A01_ORM`

No DCC folder, source asset folder, FBX export, Unreal Content asset, validator, startup actor, index update, or implementation branch is created by this package.

## 15. Quality Gate Checklist

- [ ] Asset remains original to Aerathea and specific to Blood Axe hostile Giant camp dressing.
- [ ] Blood Axe identity stays separate from neutral and civilized Giant culture.
- [ ] Giant scale lock is explicit: female 442 cm / 14 ft 6 in and male 470 cm / 15 ft 5 in.
- [ ] Primary silhouette reads as a lumpy Giant-scale travel bundle.
- [ ] Required features are present: two thick straps, one large knot, rope wrap, and dark hide cover.
- [ ] Materials stay production-friendly: dark hide, rawhide or leather straps, coarse rope, soot, ash, mud, and optional oxide red cloth accent.
- [ ] No emissive, magic, Aetherium, ritual glow, UI marker, or animated material state is included.
- [ ] Geometry plan uses real forms for the mound, straps, rope turns, knot, and large hide folds.
- [ ] Micro-detail is assigned to textures or normals, not modeled geometry.
- [ ] Triangle budgets and LOD0-LOD3 targets are included.
- [ ] Collision remains simple and non-interactive.
- [ ] No bag inventory, container UI, loot, pickup, salvage, interaction behavior, resource behavior, rest behavior, or sleeping behavior is defined.
- [ ] No DCC source, Unreal Content, runtime source, external source concept, startup placement, final approval, or implementation target is created or claimed.
- [ ] Package is useful as a future DCC handoff without selecting the first DCC target.
- [ ] File content is ASCII-only.
