# SM_GIA_BloodAxeHeavySack_A01 Production Package

Docs-only production package for a single Blood Axe Giant heavy sack. This package creates no DCC source, no Unreal Content, no startup placement, no final approval, and no implementation target.

## 1. Art Direction Summary

`SM_GIA_BloodAxeHeavySack_A01` is a single sagging Giant-scale sack with a broad tied neck, patched cloth, a dirt-weighted base, and one thick rope tie. It should read as inert Blood Axe camp storage: heavy, dirty, oversized, and roughly maintained by raiders who value utility over care.

Blood Axe remains a hostile Giant sub-faction only. This asset must stay visually separate from neutral or civilized Giant culture: no blue-gray civic masonry language, no warm hearth market storage, no clean highland craft, no refined stoneworker motifs, and no restrained blue-rune identity.

## 2. Gameplay Purpose

This is visual storage dressing only for Blood Axe camps, shelter edges, gate interiors, and rough supply clusters. It supports Giant scale, hostile camp storytelling, and storage-kit rhythm without defining any gameplay system.

This package explicitly defines no pickup, loot, inventory, resource, crafting, economy, or interaction behavior. It is not a loot bag, resource sack, vendor good, crafting ingredient, harvest node, inventory container, searchable object, objective object, destructible prop, or usable gameplay actor.

## 3. Silhouette Notes

- Primary silhouette: one upright but slumped sack with a wide sagging belly and a compressed dirt-heavy base.
- Top read: broad tied neck pinched by one thick rope tie, with short folded cloth flaps above the tie.
- Base read: flattened, weighty, slightly spreading bottom that feels packed with heavy contents but never reveals them.
- Side read: asymmetrical cloth bulges, a few broad fold planes, and one or two large patch shapes.
- Patch read: patches must be large and readable, not many tiny stitches.
- Rope read: one oversized tie band with a large simple knot and short rope tails.
- Avoid: treasure-pouch silhouette, small humanoid scale, tidy merchant sack, cozy neutral Giant storage, readable labels, UI-like markings, glowing accents, gore, or dense micro-detail.

## 4. Scale Notes

Use the locked Giant scale baseline for all future review planning:

- Female Giant scale lock: 442 cm / 14 ft 6 in.
- Male Giant scale lock: 470 cm / 15 ft 5 in.

Target prop dimensions:

- Height to tied neck: 190-260 cm.
- Widest belly width: 105-165 cm.
- Depth: 85-140 cm.
- Ground contact footprint: broad oval, roughly 90-150 cm across.

The sack should feel movable only by Giants. It should be clearly too large for normal humanoid races to lift, but still small enough to sit beside crates, baskets, covered bundles, or shelter clutter without reading as a barricade or building-scale object.

## 5. Materials and Color Palette

- Primary cloth: dirty sackcloth, smoke-gray canvas, muddy tan burlap, and ash-stained coarse fabric.
- Patch material: darker patched cloth, rawhide repair strips, or stained hide scraps used sparingly.
- Rope material: thick coarse hemp or rawhide cord in dirty tan, dull umber, and soot-darkened brown.
- Base grime: dried mud, soot, ash, dust, and darker ground-contact staining.
- Accent color: a restrained oxide red patch, tie scrap, or painted smear only if needed to reinforce Blood Axe identity.

No emissive material is needed. No magic glow, shamanic glow, forge glow, Aetherium glow, loot sparkle, UI marker color, or animated material state belongs on this asset.

## 6. Concept Image Prompt

Create an original stylized fantasy MMORPG concept image of a single Blood Axe Giant heavy sack for the world of Aerathea. The design should emphasize one sagging Giant-scale sack silhouette, broad tied neck, patched dirty sackcloth, dirt-weighted base, thick rope tie with a large simple knot, soot and ash wear, restrained oxide red Blood Axe accent, hostile Giant raider-camp identity, harsh temporary storage mood, and static visual storage role. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, no emissive accents, and MMO-friendly production design. Present it as a single prop concept sheet with front, side, top, and scale-read views on a clean neutral background. Avoid copying any existing franchise and avoid excessive micro-detail that would not translate to a mid-poly Unreal asset.

Prompt guardrails: no pickup presentation, no loot sparkle, no inventory bag UI, no resource-node framing, no crafting iconography, no economy or vendor display, no interaction prompt, no readable text label, no ritual glow, no neutral/civilized Giant craft language, and no final visual approval claim.

## 7. Modeling Notes

- Model the main sack as one softened sagging volume with a broad belly, compressed lower contact shape, and mild asymmetry.
- Model the tied neck as a real pinched upper form with simplified cloth flaps above the tie.
- Model the thick rope tie as a raised band with a large simple knot and short rope tails.
- Model two to four large cloth patches as shallow raised or inset forms where they affect the silhouette.
- Keep the underside simple and stable for ground placement.
- Use broad fold geometry only where it changes the silhouette or catches light from common gameplay camera angles.
- Fake cloth weave, rope fibers, frayed edges, tiny stitches, small holes, fine stains, dirt speckles, ash flecks, and paint chips with textures or normal maps.
- Avoid many dangling cords, many small patches, individual stitch geometry, cloth simulation, rope physics, visible contents, readable labels, or treasure-pouch cues.

This package does not authorize DCC source work, sculpting, retopology, UV work, baking, collision proxy creation, proof renders, LOD source work, FBX export, Unreal import, startup placement, final approval, or implementation target selection.

## 8. Texture and Material Notes

Recommended future texture set:

- `T_GIA_BloodAxeHeavySack_A01_BC`: dirty sackcloth, cloth patches, rope, soot, ash, mud, and restrained oxide red accent color.
- `T_GIA_BloodAxeHeavySack_A01_N`: broad fabric folds, patch seams, rope twist suggestion, knot compression, burlap weave, and base compression.
- `T_GIA_BloodAxeHeavySack_A01_ORM`: packed occlusion, roughness, and metallic. Metallic should remain black.

Material plan:

- One material slot preferred: `MI_GIA_BloodAxeHeavySack_A01`.
- Texture size: 1K by default; 2K only if a later approved task promotes the prop to close-camera hero dressing.
- Roughness should stay high across cloth, rope, mud, ash, and soot.
- AO should emphasize the tied neck, patch overlaps, rope pressure, bottom dirt contact, and large fold intersections.
- No emissive map is required.

## 9. Triangle Budget

Treat as a Giant-scale small-to-medium camp prop.

- LOD0 target: 1,200-3,500 tris.
- LOD1 target: 600-1,600 tris.
- LOD2 target: 250-750 tris.
- LOD3 target: 80-300 tris.

Use one material slot and a 1K texture set for normal camp dressing. The triangle budget should support the sagging main mass, broad tied neck, thick rope tie, readable knot, and a small number of large patch forms without modeling micro-detail.

## 10. LOD Plan

- LOD0: full sagging sack volume, broad tied neck, thick rope tie, readable knot, short rope tails, large patch forms, and major cloth folds.
- LOD1: preserve the sack silhouette, tied neck, rope band, and knot; simplify patch bevels and secondary folds.
- LOD2: merge smaller bulges into the main volume, reduce rope roundness, keep one strong knot impression, and move patch detail toward texture.
- LOD3: simplified sagging sack with broad base and top-neck mass; rope and patch reads may become texture-only if the silhouette remains clear.

Reduce tiny detail first: fray, stitch hints, small holes, cloth weave, rope grooves, dirt speckles, ash flecks, minor fold cuts, underside shaping, and small accent scraps. Do not destroy the primary sagging Giant-scale sack silhouette before distant LODs.

## 11. Collision Notes

This package creates no collision proxy. Future collision, if separately approved, should be simple and non-interactive:

- Collision type: simple static collision only if needed for placement.
- Preferred proxy: one low convex hull or a simple capsule-like hull around the sack belly and base.
- Do not trace rope tails, knot lobes, cloth flaps, patch edges, or small folds with collision.
- Do not create pickup collision, loot search volumes, inventory interaction volumes, resource harvesting volumes, crafting stations, economy triggers, objective volumes, nav blockers, cover tags, physics bodies, cloth collision, or gameplay trigger volumes.

## 12. Animation Notes

No animation is planned.

Do not define cloth simulation, rope simulation, jiggle motion, carry motion, open or close states, pickup animation, loot states, inventory states, resource states, crafting states, economy states, interaction prompt states, destructible states, VFX pulses, audio cues, or Blueprint-driven behavior for this docs-only package.

## 13. Unreal Import Notes

No Unreal work is authorized or performed by this package. These notes are future-facing only if a later approved implementation task exists, and they do not select an implementation target.

- Asset name: `SM_GIA_BloodAxeHeavySack_A01`.
- Asset type: Static Mesh, future planning only.
- Proposed future folder path: `/Game/Aerathea/Props/Giants/BloodAxe/Storage/HeavySack/`.
- Mesh scale: authored in centimeters, matching Unreal scale.
- Scale validation: compare against female Giant 442 cm / 14 ft 6 in and male Giant 470 cm / 15 ft 5 in.
- Pivot: bottom center of the flattened dirt-weighted base for ground placement.
- Orientation: front faces the most readable patch and rope-knot side; keep the tied neck readable from the expected gameplay camera.
- Collision: simple non-interactive static collision only if later approved.
- LODs: LOD0, LOD1, LOD2, and LOD3 as planned above.
- Material slots: 1.
- Material instance: `MI_GIA_BloodAxeHeavySack_A01`, future only.
- Texture list: `T_GIA_BloodAxeHeavySack_A01_BC`, `T_GIA_BloodAxeHeavySack_A01_N`, `T_GIA_BloodAxeHeavySack_A01_ORM`.
- Sockets: none.
- Animations: none.
- Blueprint behavior: none.
- Runtime behavior: none.
- Startup placement: none.
- Final approval: not claimed.
- Implementation target: not selected.

This task creates no Unreal Content, no material instance, no texture asset, no Blueprint, no validator, no runtime source, no startup actor, and no final visual approval.

## 14. Folder and Naming Recommendation

Docs package path:

- `docs/assets/props/SM_GIA_BloodAxeHeavySack_A01/PRODUCTION_PACKAGE.md`

Future naming recommendation if separately approved:

- Static Mesh: `SM_GIA_BloodAxeHeavySack_A01`
- Material Instance: `MI_GIA_BloodAxeHeavySack_A01`
- Base Color: `T_GIA_BloodAxeHeavySack_A01_BC`
- Normal: `T_GIA_BloodAxeHeavySack_A01_N`
- ORM: `T_GIA_BloodAxeHeavySack_A01_ORM`

Do not create source folders, Content folders, DCC files, Unreal files, Hermes files or configuration, runtime files, external concept copies, global index edits, task board edits, startup placement, final approval records, or implementation targets as part of this package.

## 15. Quality Gate Checklist

- [ ] The package is docs-only and changes only this production package file.
- [ ] The asset remains `SM_GIA_BloodAxeHeavySack_A01`.
- [ ] The concept is original to Aerathea and fits stylized fantasy MMORPG production.
- [ ] The prop is a single sagging Giant-scale sack with broad tied neck, patched cloth, dirt-weighted base, and thick rope tie.
- [ ] Giant scale lock is explicit: female 442 cm / 14 ft 6 in and male 470 cm / 15 ft 5 in.
- [ ] Blood Axe remains a hostile Giant sub-faction and is separate from neutral/civilized Giant culture.
- [ ] Neutral/civilized Giant cave-town, blue-gray masonry, warm hearth, clean highland craft, refined stoneworker motifs, and restrained blue-rune language are excluded.
- [ ] Materials use dirty sackcloth, patched cloth, rawhide or coarse rope, soot, ash, mud, and optional restrained oxide red accent.
- [ ] Glow, emissive, ritual VFX, loot sparkle, UI markers, readable labels, vendor-display language, and treasure-pouch cues are absent.
- [ ] Texture maps include base color, normal, and packed ORM; emissive is not used.
- [ ] Geometry uses real forms for the sagging sack, tied neck, rope tie, knot, major folds, and large patches.
- [ ] Micro-detail is assigned to textures or normals, not modeled geometry.
- [ ] Triangle budgets and LOD0-LOD3 targets are included.
- [ ] Collision remains future guidance only, simple, static, and non-interactive.
- [ ] No pickup, loot, inventory, resource, crafting, economy, interaction, destructible, objective, vendor, search, harvest, physics, cloth simulation, nav/pathfinding, VFX, audio, or Blueprint behavior is defined.
- [ ] No DCC work, Unreal work, startup placement, final approval, or implementation target is created or claimed.
- [ ] Package is useful as a future DCC handoff without selecting the first DCC target.
- [ ] File content is ASCII-only.
