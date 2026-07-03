# SM_GIA_BloodAxeHideRoll_A01 Production Package

## 1. Art Direction Summary

- Asset name: `SM_GIA_BloodAxeHideRoll_A01`
- Asset type: Static Mesh prop production package, docs-only
- Parent kit: `KIT_GIA_BloodAxeBedrollHideBundles_A01`
- Child intake row: `BloodAxeCamp.png#BedrollBundles_HideRoll_Single_A01`
- Faction/theme: Blood Axe Tribe, hostile Giant sub-faction only
- Visual brief: one oversized flattened hide roll, 240-480 cm long, with broad end caps, two thick straps, and one oxide red cloth tag
- Status: docs-only production package ready

`SM_GIA_BloodAxeHideRoll_A01` is a single Giant-scale hide roll used as static camp dressing in hostile Blood Axe camps. It should read as a rough, heavy, travel-ready bundle: a flattened cylinder of smoked hide and patched leather, blunt broad end caps, two oversized straps cinching the roll, and one dirty oxide red cloth tag that identifies Blood Axe ownership without turning the prop into a quest marker or loot item.

Blood Axe visual language must stay separate from neutral/civilized Giant culture. This prop belongs to a hostile raider camp and should use rough hide, rawhide, soot, mud, blackened hardware, and restrained red cloth. It must not become refined highland bedding, warm hearth camp gear, civic stoneworker storage, cave-town domestic dressing, blue-rune Giant culture, or a general Giant prop.

This package is planning documentation only. It does not authorize DCC source work, first DCC target selection, implementation target selection, FBX export, Unreal Content creation, startup placement, validators, runtime source, pickup behavior, inventory behavior, loot behavior, resource behavior, search behavior, interaction behavior, cloth simulation, final visual approval, external concept edits, or Hermes work.

## 2. Gameplay Purpose

The prop supports static environmental storytelling and Giant-scale readability in Blood Axe camp layouts. It gives future level artists a single reusable hide roll for shelter edges, sleeping clutter, path-side piles, camp thresholds, and travel-bundle arrangements without defining gameplay systems.

Allowed purpose:

- Static hostile camp dressing for Blood Axe Giant shelters, lean-tos, hide tents, cooking edges, forge outskirts, and path bends.
- Scale reference that reinforces the size of Blood Axe camp gear beside Giant characters and structures.
- Low-profile clutter that breaks up ground planes without blocking the primary camp silhouette.
- Reusable child prop for later hide-roll stacks or shelter-adjacent pile compositions after separate approval.

Out of scope:

- No pickup, inventory, loot, resource, salvage, crafting, economy, search, interaction, storage, usable bed, rest behavior, objective marker, cover definition, nav/pathfinding rule, destructible state, cloth simulation, physics pile, startup placement, first DCC target selection, implementation target selection, final visual approval, or Hermes work.

## 3. Silhouette Notes

Primary read:

- One oversized horizontal flattened cylinder mass.
- Broad circular or slightly oval end caps that make the rolled-hide construction readable from side view.
- Two thick straps crossing the roll around its circumference, placed roughly one third in from each end.
- One oxide red cloth tag tied under or beside one strap, visible as a single accent, not a banner or UI marker.
- Lumpy compressed upper surface, flattened ground-contact underside, and a few broad hide flap overlaps.
- Asymmetric roll ends with large folded hide layers, not many tiny curled strips.

Shape hierarchy:

- First read: long low Giant-scale hide-roll mass.
- Second read: broad end caps and flattened cylinder profile.
- Third read: two heavy strap bands.
- Fourth read: one oxide red cloth tag and large hide overlaps.
- Fifth read: hide grain, stitch marks, soot, mud, fray, and scratches handled through textures and normals.

Model real geometry for the main roll, broad end caps, major hide flaps, two strap bands, strap buckles or knots if used, and the single cloth tag as fixed shaped geometry. Fake fine hide grain, tiny stitching, small fray, leather pores, soot speckles, mud spatters, rope fibers, and small scratches with texture and normal detail.

Avoid readable trophies, gore, many dangling strips, dense strap fields, refined bedding, elegant travel gear, cozy neutral Giant camp language, blue runes, magic glow, pickup affordances, search clues, or UI-like tag shapes.

## 4. Scale Notes

Use the validated `SK_GIA_Base_A01` Giant scale lock:

- Female Giant baseline: 442 cm / 14 ft 6 in.
- Male Giant baseline: 470 cm / 15 ft 5 in.
- Approved Giant ranges: females 14-15 ft / 427-457 cm; males 14 ft 10 in-16 ft 0 in / 452-488 cm.
- Author all future source in centimeters. 1 Unreal unit equals 1 cm.

Asset dimensions:

- Required length range: 240-480 cm.
- Preferred A01 nominal length: 360-420 cm, long enough to read as Giant-owned but still reusable in camp clusters.
- End-cap width/depth: 85-150 cm across, with slight oval flattening.
- Flattened height: 55-115 cm depending on variant, lower than the end-cap width so it feels compressed by weight.
- Ground-contact footprint: 240-480 cm long by 90-160 cm deep.
- Strap width: 18-38 cm, oversized and readable from MMO camera distance.
- Strap thickness: 4-10 cm, enough to cast baked-AO style shadows.
- Red cloth tag: 35-70 cm wide by 45-100 cm long, one tag only.

Do not shrink the roll to normal humanoid bedding scale. A smallfolk character should read the prop as a heavy camp object owned by Blood Axe Giants, while a 470 cm male Giant should read it as portable or stackable camp gear.

## 5. Materials and Color Palette

Primary materials:

- Rough smoked hide and patched leather for the roll body.
- Stiff rawhide or scorched leather for the two thick straps.
- Heavy rope or sinew knot detail only where it supports the strap read.
- Optional blackened iron buckle, ring, or crude clamp used sparingly.
- One oxide red cloth tag with soot-dark edges and dirty wear.
- Soot, ash, trampled mud, grease, and weather staining around the underside and strap contact points.

Palette targets:

- Hide and leather: dark umber, desaturated tan, smoked brown, gray brown.
- Strap leather/rawhide: dry tan, dark fiber brown, scorched ochre, blackened edge wear.
- Metal accents if used: charcoal black, dull gunmetal, worn dark steel edge.
- Blood Axe cloth tag: deep oxide red, faded maroon, rubbed dark red.
- Grounding grime: ash gray, charcoal black, dried mud brown.

Avoid neutral/civilized Giant material language: no blue-gray carved stone, refined highland woven bedding, warm hearth blanket colors, civic stoneworker symbols, restrained blue runes, polished domestic trim, or clean nomad craft as the default read.

No emissive material is approved for this asset.

## 6. Concept Image Prompt

Create an original stylized fantasy MMORPG concept image of `SM_GIA_BloodAxeHideRoll_A01` for the world of Aerathea. The design should emphasize one oversized Giant-scale flattened hide roll, a long low cylinder mass, broad end caps, two thick leather or rawhide straps, one oxide red cloth tag, rough smoked hide, patched leather, soot, ash, mud, hostile Blood Axe Giant sub-faction identity, clear separation from neutral/civilized Giant culture, and the gameplay role of static non-interactive camp dressing. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, no emissive glow, and MMO-friendly production design. Present it as a single prop concept sheet with front, side, top, and three-quarter views, material swatches, LOD/collision callouts, and scale markers beside a 442 cm female Giant and a 470 cm male Giant on a clean background. Avoid copying any existing franchise, avoid refined Giant cave-town language, avoid warm hearth bedding, avoid blue runes, avoid gore, avoid pickup or loot presentation, avoid inventory tags, avoid search clues, avoid interaction prompts, avoid cloth simulation, avoid startup placement claims, and avoid excessive micro-detail that would not translate to a mid-poly Unreal asset.

Concept source note: this package references `BloodAxeCamp.png#BedrollBundles_HideRoll_Single_A01` only through existing intake documentation. It does not copy, move, crop, edit, embed, inspect for final approval, or commit external source concept art.

## 7. Modeling Notes

This is modeling guidance only for a later authorized build lane. No source asset, sculpt, retopo, UV, bake, proof render, export, engine import, validator, capture, placement, or target selection is part of this task.

Model as real geometry:

- Main flattened cylinder hide-roll body with a broad, weighty lower contact plane.
- Two broad end caps with visible large roll-layer steps.
- Major hide flap overlaps on the top or side, kept broad and sparse.
- Exactly two thick strap bands around the roll.
- One large buckle, knot, or tied strap mass per strap only if needed for readability.
- One fixed oxide red cloth tag attached to one strap.
- Slight asymmetry in end-cap compression, strap spacing, and hide lumpy forms.

Keep in texture or normal maps:

- Fine hide grain, leather pores, small stitches, cloth weave, tiny fray fibers, hair-like fur traces, rope fibers, soot speckles, mud flecks, shallow scratches, small wrinkles, pitting on metal, and subtle edge wear.

Construction notes:

- Spend geometry on the low roll mass, broad end caps, the two strap silhouettes, large flap overlaps, and the red tag thickness.
- Keep the underside flattened so the prop sits firmly on camp ground without looking like a perfect tube.
- Keep strap bands chunky and readable; do not add extra decorative straps.
- Keep the red tag as fixed geometry with a few broad tears or bends, not simulated cloth.
- Avoid hidden gameplay helpers, sockets, collision proxies, pickup handles, readable labels, or inventory-like compartments.

## 8. Texture and Material Notes

Target material strategy:

- Material slots: 1 target using an atlas or shared material instance; 2 maximum only if a later close-review version needs separate red cloth or metal tint control.
- Texture set: 512-1K for normal repeated camp dressing; 1K preferred for near-shelter placement.
- No emissive texture.
- Use shared Blood Axe material families where possible so this prop can combine cleanly with future hide-roll stacks and shelter piles.

Suggested future material and texture names:

- `MI_GIA_BloodAxeHideRoll_A01`
- `T_GIA_BloodAxeHideRoll_A01_BC`
- `T_GIA_BloodAxeHideRoll_A01_N`
- `T_GIA_BloodAxeHideRoll_A01_ORM`

Optional shared material references if a later implementation task splits slots:

- `MI_GIA_BloodAxeHideLeather_A01`
- `MI_GIA_BloodAxeRopeRawhide_A01`
- `MI_GIA_BloodAxeRedCloth_A01`
- `MI_GIA_BloodAxeReforgedMetal_A01`

Base color plan:

- Keep the roll body dark, smoky, and patchy with tan-brown hide variation.
- Separate straps with darker rawhide or scorched leather values.
- Use the oxide red cloth tag as the only strong color accent.
- Add soot and mud around the underside and strap pressure points without making the prop look magical or quest-readable.

Normal map plan:

- Broad hide compression, end-cap roll layers, strap pressure ridges, large flap folds, shallow cracks, cloth weave on the tag, and low mud contact ridges.

Packed `ORM` plan:

- R: ambient occlusion under straps, end-cap fold steps, flap overlaps, underside ground contact, and tag tie points.
- G: high roughness for hide, leather, rawhide, cloth, soot, ash, and mud; medium-high roughness for any blackened metal accent.
- B: metallic isolated to optional buckles, rings, or clamps only. Hide, leather, cloth, rope, soot, ash, and mud stay non-metallic.

## 9. Triangle Budget

Target as a large camp prop child:

- LOD0: 1,200-3,500 tris.
- Preferred A01 LOD0 range: 1,500-3,000 tris.
- Hard cap: 3,500 tris unless a later approved close-review version adds extra end-cap complexity.
- LOD1: 700-1,600 tris.
- LOD2: 300-800 tris.
- LOD3: 120-300 tris.
- Material slots: 1 target, 2 maximum.
- Texture target: 512-1K texture set.

Geometry priorities:

- Preserve the flattened cylinder mass, broad end caps, two thick straps, strap tie/buckle silhouettes, one red tag, and large hide flap overlaps.
- Use lower-cost geometry for minor lumps and broad dents.
- Do not spend triangles on tiny stitches, hide pores, rope fibers, many frayed cloth strips, dense scratches, soot flecks, mud grains, small cracks, or repeated little buckles.

## 10. LOD Plan

All shipping-quality versions require LOD0-LOD3.

- LOD0: full flattened roll profile, broad end caps, large roll-layer steps, two strap bands, strap tie or buckle masses, one fixed red cloth tag, broad hide flaps, and main contact-plane deformation.
- LOD1: 55-65 percent of LOD0; simplify end-cap layer cuts, reduce minor lumpy forms, merge small strap bevels, and reduce tag fold cuts.
- LOD2: 25-40 percent of LOD0; preserve long low roll mass, two straps, end-cap color blocks, and red tag while flattening secondary folds and removing small underside detail.
- LOD3: 10-20 percent of LOD0; preserve a simple flattened cylinder silhouette with two dark strap reads and one red accent block.

Reduction order:

1. Tiny stitches, cloth weave, hide pores, soot speckles, mud flecks, pitting, and fine scratches.
2. Small fray fibers, minor edge cuts, tiny strap notches, and secondary wrinkles.
3. Minor lumpy forms, underside folds, and hidden back-facing flap detail.
4. Small buckle bevels, knot undercuts, and non-structural strap thickness changes.
5. Secondary end-cap layer cuts and small asymmetry details.

Never reduce the primary flattened cylinder mass, broad end caps, two thick strap bands, one red cloth tag, or Blood Axe hide-and-soot read before removing small detail.

## 11. Collision Notes

Collision is planning-only in this package. Do not create collision proxies, UCX meshes, physics bodies, cloth collision, nav rules, destructible chunks, interaction volumes, pickup collision, search volumes, loot volumes, resource nodes, or gameplay traces from this task.

Future collision guidance:

- Preferred collision: one simple capsule, rounded box, or low-count convex hull around the main flattened roll mass if collision is required.
- Decorative-only placement may use collision disabled if future layout rules allow it.
- Strap bands should have no separate collision.
- Red cloth tag should have no separate collision.
- Buckles, knots, end-cap folds, small flaps, mud contact, and grime details should have no separate collision.
- Do not use per-poly collision.
- Do not make the prop a nav blocker, cover asset, pickup item, loot container, inventory object, resource node, search object, or interaction target.

Any walkability, blocking, path clearance, or navmesh policy must be decided in a separate approved layout or implementation task.

## 12. Animation Notes

Baseline asset is static.

- Animation list: none.
- The hide roll, straps, knots, and cloth tag are fixed shaped geometry.
- No cloth simulation, wind animation, dangling strap motion, rope physics, physics asset, destructible state, skeletal setup, vertex flutter, material pulse, VFX pulse, audio cue, Blueprint state, startup actor behavior, pickup behavior, inventory behavior, loot behavior, resource behavior, search behavior, or interaction behavior is approved.

Any moving, usable, searchable, pickup, inventory-linked, loot-linked, resource-linked, glowing, simulated-cloth, or player-facing variant must be split into a separately named package with separate approval.

## 13. Unreal Import Notes

These are future import planning notes only. This task performs no Unreal work and creates no engine content.

- Asset name: `SM_GIA_BloodAxeHideRoll_A01`
- Asset type: Static Mesh prop
- Planned folder if later authorized: `/Game/Aerathea/Props/Giants/BloodAxeCamp/Dressing/`
- Naming convention: `SM_` for mesh, `MI_` for material instance, `T_` for textures.
- Pivot location: ground-contact center under the roll, centered along length and depth.
- Orientation: long roll axis along +Y, primary presentation side facing +X unless a later approved export lane confirms a different convention.
- Scale: centimeter-authored source, import scale 1.0 after a separate approved asset build.
- Collision type: disabled by default or one simple capsule, rounded box, or low-count convex hull if later placement requires contact.
- LOD plan: LOD0, LOD1, LOD2, and LOD3 required.
- Material slot count: 1 target, 2 maximum.
- Texture list: `T_GIA_BloodAxeHideRoll_A01_BC`, `T_GIA_BloodAxeHideRoll_A01_N`, `T_GIA_BloodAxeHideRoll_A01_ORM`.
- Emissive texture: none.
- Sockets: none.
- Animation list: none.
- Blueprint behavior: none.
- Performance notes: keep one reusable mesh, low material count, fixed geometry, no runtime cloth, no gameplay volumes, no pickup/search affordances, and aggressive LOD reduction of small folds and surface detail.

Do not create Content files, Blueprints, material assets, texture assets, validator files, startup scene placement, source folders, FBX exports, runtime source, first implementation target selection, final visual approval, or Hermes work from this docs-only task.

## 14. Folder and Naming Recommendation

Allowed docs package path:

- `docs/assets/props/SM_GIA_BloodAxeHideRoll_A01/PRODUCTION_PACKAGE.md`

Recommended future names if a separate build lane is approved:

- Static mesh: `SM_GIA_BloodAxeHideRoll_A01`
- Material instance: `MI_GIA_BloodAxeHideRoll_A01`
- Base color: `T_GIA_BloodAxeHideRoll_A01_BC`
- Normal: `T_GIA_BloodAxeHideRoll_A01_N`
- Packed ORM: `T_GIA_BloodAxeHideRoll_A01_ORM`

Package relationship:

- Parent kit: `KIT_GIA_BloodAxeBedrollHideBundles_A01`
- Related future stack package: `KIT_GIA_BloodAxeHideRollStack_A01`
- Related future open-roll package: `SM_GIA_BloodAxeOpenHideRoll_A01`
- Related future shelter-pile package: `KIT_GIA_BloodAxeShelterPile_A01`

Do not add or edit global indexes, task boards, backlog files, bootstrap files, Content, SourceAssets, Tools, runtime source, external concept folders, Hermes files/config, or any companion docs from this task.

## 15. Quality Gate Checklist

- Package is docs-only and changes only `docs/assets/props/SM_GIA_BloodAxeHideRoll_A01/PRODUCTION_PACKAGE.md`.
- Asset is a single oversized hide roll, not a stack, kit, container, bed system, or review composition.
- Required form is explicit: 240-480 cm long, flattened cylinder mass, broad end caps, two thick straps, and one oxide red cloth tag.
- Blood Axe remains a hostile Giant sub-faction and is kept separate from neutral/civilized Giant culture.
- Giant scale lock is explicit: female baseline 442 cm / 14 ft 6 in and male baseline 470 cm / 15 ft 5 in.
- Silhouette is low, broad, readable, and buildable as a mid-poly MMO static prop.
- Materials use rough hide, patched leather, rawhide, soot, ash, mud, blackened hardware if needed, and one oxide red cloth accent.
- No default emissive, magic glow, ritual state, shamanic state, forge-heat state, UI marker, readable text, or quest-object presentation is included.
- Fine hide grain, stitch marks, fray, cloth weave, rope fibers, soot speckles, mud flecks, and scratches are assigned to texture or normal detail.
- Triangle budgets, LOD0-LOD3 planning, material slot targets, texture maps, collision guidance, animation limits, and Unreal import planning are included.
- Collision stays simple or disabled and does not define nav, cover, pickup, search, loot, resource, interaction, or gameplay volumes.
- Animation is none; cloth tag and straps are fixed shaped geometry with no cloth simulation or physics.
- Package stops before pickup, inventory, loot, resource, search, interaction, cloth simulation, startup placement, DCC, FBX, Unreal Content, final visual approval, first DCC target selection, implementation target selection, and Hermes work.
- No source concepts are copied, moved, cropped, embedded, edited, inspected for final approval, or committed.
- No global index, task board, Content, SourceAssets, Tools, runtime source, external concept folder, or Hermes file/config is edited.
