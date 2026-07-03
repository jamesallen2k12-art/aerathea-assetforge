# SM_GIA_BloodAxeThresholdBundle_A01 Production Package

## 1. Art Direction Summary

`SM_GIA_BloodAxeThresholdBundle_A01` is a docs-only production package for a single Giant-scale strapped bundle or hide roll placed near a Blood Axe shelter threshold or camp path bend for scale and route clutter. It belongs only to the hostile Blood Axe Giant sub-faction and must not be used as neutral or civilized Giant culture.

The read should be immediate: one heavy, rough, travel-worn mass dropped at the edge of a shelter route, lashed with thick rawhide and marked by a small oxide red cloth tag. The prop should feel practical, brutal, temporary, and raider-camp specific, not refined highland bedding, civic cave-town craft, or clean nomad gear.

This package is docs-only: no DCC, no Unreal, no startup placement, no final approval, no implementation target, no objective marker, no cover definition, no lootable bag, no pickup, and no blocker rule.

## 2. Gameplay Purpose

- Visual dressing for Blood Axe camps, shelter thresholds, and path bends.
- Reinforces Giant scale by placing an oversized soft bundle near a route edge.
- Adds route clutter and lived-in camp composition without defining gameplay behavior.
- Supports hostile Blood Axe environmental storytelling through rough hide, ash, soot, rope, rawhide, and red cloth accents.

This is not an inventory bag, loot container, pickup item, objective marker, cover object, nav blocker, usable bedding, resource node, search target, salvage prop, or interaction prompt.

## 3. Silhouette Notes

- Primary silhouette: one low, bulky oblong roll or lumpy strapped bundle.
- Shape language: heavy flattened cylinder with one sagging side, uneven end caps, and two to three oversized strap bands.
- Read distance: the object should read as one single bundle, not a pile, crate, sack stack, or bedding row.
- Threshold placement: designed to sit near a shelter entrance edge or bend in a camp path while visually implying clutter without blocking the route.
- Distinctive details:
  - Large knot or strap crossing on top or one side.
  - One broad hide flap tucked under a strap.
  - Small oxide red cloth tag tied to a strap for Blood Axe identity.
  - Optional blackened iron ring or crude buckle as a minor accent.

Keep the silhouette simple and readable. Do not add many dangling cords, tiny trophies, ritual props, UI-like markers, readable text, or decorative micro-detail.

## 4. Scale Notes

- Giant scale lock: female baseline 442 cm / 14 ft 6 in; male baseline 470 cm / 15 ft 5 in.
- Approved Giant range remains female 14-15 ft and male 14 ft 10 in-16 ft 0 in.
- Suggested prop footprint:
  - Length: 260-380 cm.
  - Width: 80-135 cm.
  - Height: 55-105 cm.
- The bundle should feel portable by a Giant but oversized beside smaller races.
- The prop must be low enough to read as threshold clutter, not a barricade, wall, chest, or defensive cover object.
- Placement planning should preserve clear path readability. This package does not create a nav/pathfinding rule or blocker rule.

## 5. Materials and Color Palette

- Primary materials:
  - Rough dark hide.
  - Patched leather.
  - Fur edge strips used sparingly.
  - Thick rope.
  - Rawhide lashings.
  - Mud, ash, soot, and worn grime.
- Accent materials:
  - Small blackened iron ring or crude buckle.
  - One oxide red cloth tag or strip.
- Color palette:
  - Charcoal brown hide.
  - Soot black wear zones.
  - Mud brown lower contact areas.
  - Desaturated tan rawhide.
  - Dirty off-white rope fibers.
  - Oxide red Blood Axe tag accent.

Avoid blue-gray civic stone, warm hearth bedding language, clean highland craft, restrained blue runes, Aetherium glow, default emissive effects, refined Giant masonry motifs, and neutral/civilized Giant culture cues.

## 6. Concept Image Prompt

Create an original stylized fantasy MMORPG concept image of a single Giant-scale Blood Axe threshold bundle for the world of Aerathea. The design should emphasize a low heavy oblong hide roll or lumpy strapped bundle, rough dark hide, patched leather, thick rawhide lashings, soot, ash, mud, one oxide red cloth tag, hostile Blood Axe raider-camp identity, harsh temporary camp mood, and visual route clutter near a shelter threshold or camp path bend. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, sparing non-emissive accents, and MMO-friendly production design. Present it as a compact prop concept sheet with front, side, top, and small threshold-placement view on a clean background. Avoid copying any existing franchise and avoid excessive micro-detail that would not translate to a mid-poly Unreal asset.

Prompt guardrails: no objective marker, no cover icon, no loot sparkle, no pickup presentation, no resource node language, no readable text label, no ritual glow, no gore display, no neutral/civilized Giant craft language, and no final visual approval claim.

## 7. Modeling Notes

- Model real geometry for:
  - Main bundle body as one softened oblong mass.
  - Broad end caps or tucked hide folds.
  - Two or three thick strap bands.
  - One large knot or strap overlap.
  - Optional crude iron ring or buckle.
  - Small cloth tag as a simple low-poly folded strip.
- Fake with textures and normals:
  - Hide grain.
  - Fur strands.
  - Rope fibers.
  - Rawhide fray.
  - Stitching.
  - Scratches.
  - Soot speckles.
  - Ash flecks.
  - Mud spatters.
  - Leather cracks.
- Keep underside simple and stable for ground contact.
- Avoid loose cloth simulation, rope physics, dangling secondary motion, many tiny buckles, many strap tails, or detailed interior contents.
- This package does not select a first DCC target and does not authorize sculpt, retopo, UV, bake, collision proxy, proof render, LOD source, or FBX work.

## 8. Texture and Material Notes

- Planned material slot count: 1 material.
- Suggested texture set: 1K for normal use; 2K only if later approved as a close camera camp hero prop.
- Texture maps:
  - `T_GIA_BloodAxeThresholdBundle_A01_BC` for base color.
  - `T_GIA_BloodAxeThresholdBundle_A01_N` for normal detail.
  - `T_GIA_BloodAxeThresholdBundle_A01_ORM` for packed occlusion, roughness, and metallic.
- Emissive map: none.
- Metallic should be near zero except the optional blackened iron ring or buckle.
- Roughness should stay high across hide, rope, rawhide, mud, and cloth.
- AO should emphasize strap pressure, fold overlap, underside contact, and the seam between the bundle body and end caps.
- Paint detail should remain broad and hand-readable. Do not bake dense micro-stitching or tiny rope fibers into geometry.

## 9. Triangle Budget

- Asset class: small-to-medium Giant-scale camp prop.
- LOD0 target: 1,500-3,500 triangles.
- LOD1 target: 800-1,800 triangles.
- LOD2 target: 350-800 triangles.
- LOD3 target: 120-350 triangles.
- Material budget: 1 material slot.
- Texture budget: 1K texture set by default.

The prop should stay comfortably inside the small prop budget while allowing enough silhouette support for straps, knots, and softened hide mass.

## 10. LOD Plan

- LOD0:
  - Full softened bundle mass.
  - Two to three straps.
  - Large knot or strap overlap.
  - Cloth tag.
  - Optional crude buckle or ring.
- LOD1:
  - Merge minor strap bevels.
  - Simplify knot shape.
  - Keep cloth tag if readable.
  - Reduce underside folds.
- LOD2:
  - Reduce straps to simplified bands.
  - Bake knot and buckle read into texture where possible.
  - Remove tiny strap tails and minor fold geometry.
- LOD3:
  - Preserve the low oblong bundle silhouette.
  - Preserve only the strongest strap band reads.
  - Use texture-only detail for knots, stitching, fibers, mud, soot, and fray.

Do not destroy the primary low bulky silhouette before removing strap and surface-detail complexity.

## 11. Collision Notes

- Docs-only collision guidance only; no collision proxy is created in this task.
- If later implemented, use a very simple non-complex collision shape approximating the low oblong footprint.
- Suggested future collision: one low box or capsule-like convex hull, tuned to avoid snagging.
- Do not author cover definition, objective collision, pickup collision, loot interaction collision, resource collision, physics simulation, cloth collision, or gameplay volume.
- Do not define this asset as a nav blocker or route blocker. This package has no blocker rule.

## 12. Animation Notes

- Static mesh planning only.
- No skeletal mesh.
- No cloth simulation.
- No rope physics.
- No secondary motion.
- No pickup animation.
- No idle animation.
- No interaction animation.
- No VFX or audio cue.

Any later scene dressing should treat the bundle as inert environmental dressing.

## 13. Unreal Import Notes

No Unreal work is authorized by this package. These notes are future-facing only if a later approved implementation task exists.

- Asset name: `SM_GIA_BloodAxeThresholdBundle_A01`.
- Asset type: Static Mesh, future only.
- Proposed folder path: `/Game/Aerathea/Props/Giants/BloodAxe/BedrollHideBundles/ThresholdBundle/`.
- Mesh scale: authored in centimeters, matching Unreal scale.
- Pivot: bottom center of the bundle footprint for ground placement; align local X along the long axis.
- Collision: future simple low non-complex collision only if approved; no blocker rule and no cover definition.
- LODs: LOD0, LOD1, LOD2, LOD3 as planned above.
- Material slots: 1.
- Material instance: `MI_GIA_BloodAxeThresholdBundle_A01`, future only.
- Texture list:
  - `T_GIA_BloodAxeThresholdBundle_A01_BC`.
  - `T_GIA_BloodAxeThresholdBundle_A01_N`.
  - `T_GIA_BloodAxeThresholdBundle_A01_ORM`.
- Sockets: none.
- Animations: none.
- Blueprint behavior: none.
- Gameplay tags: none.
- Performance notes: keep as static visual dressing; avoid dynamic lights, emissive pulses, runtime material changes, physics, overlap logic, or interaction traces.

This task creates no Unreal Content, no startup actor, no validator, no Blueprint, no runtime source, no material instance, no texture asset, and no final approval.

## 14. Folder and Naming Recommendation

- Package document path: `docs/assets/props/SM_GIA_BloodAxeThresholdBundle_A01/PRODUCTION_PACKAGE.md`.
- Future source folder, if separately approved later: `SourceAssets/Props/Giants/BloodAxe/BedrollHideBundles/SM_GIA_BloodAxeThresholdBundle_A01/`.
- Future Unreal folder, if separately approved later: `/Game/Aerathea/Props/Giants/BloodAxe/BedrollHideBundles/ThresholdBundle/`.
- Future mesh name: `SM_GIA_BloodAxeThresholdBundle_A01`.
- Future material instance: `MI_GIA_BloodAxeThresholdBundle_A01`.
- Future textures:
  - `T_GIA_BloodAxeThresholdBundle_A01_BC`.
  - `T_GIA_BloodAxeThresholdBundle_A01_N`.
  - `T_GIA_BloodAxeThresholdBundle_A01_ORM`.

Do not create source folders, Content folders, DCC files, Unreal files, Hermes files/config, runtime files, external concept copies, global index edits, or task board edits as part of this package.

## 15. Quality Gate Checklist

- [ ] The package is docs-only and changes only this production package file.
- [ ] The asset remains `SM_GIA_BloodAxeThresholdBundle_A01`.
- [ ] The concept is original to Aerathea and fits stylized fantasy MMORPG production.
- [ ] The prop is a single strapped bundle or roll near a shelter threshold or camp path bend for scale and route clutter.
- [ ] Giant scale lock is explicit: female 442 cm / 14 ft 6 in and male 470 cm / 15 ft 5 in.
- [ ] Blood Axe remains a hostile Giant sub-faction and is separate from neutral/civilized Giant culture.
- [ ] Neutral/civilized Giant cave-town, blue-gray masonry, warm hearth, clean nomad craft, and restrained blue-rune language are excluded.
- [ ] The silhouette is low, bulky, oblong, readable, and not a pile, crate, barricade, or bedding row.
- [ ] Materials use rough hide, patched leather, fur edge strips, rope, rawhide, soot, ash, mud, blackened iron accents, and oxide red cloth.
- [ ] Glow, emissive, ritual VFX, loot sparkle, UI markers, and readable text are absent.
- [ ] Texture maps include base color, normal, and packed ORM; emissive is not used.
- [ ] LOD0 through LOD3 are defined and protect the primary silhouette first.
- [ ] Collision is guidance only, with no authored proxy in this task.
- [ ] The package defines no objective marker, cover definition, lootable bag, pickup, blocker rule, nav/pathfinding rule, interaction, physics, cloth setup, usable bed, resource behavior, search behavior, or inventory behavior.
- [ ] No DCC, Unreal, startup placement, final visual approval, or implementation target is claimed.
