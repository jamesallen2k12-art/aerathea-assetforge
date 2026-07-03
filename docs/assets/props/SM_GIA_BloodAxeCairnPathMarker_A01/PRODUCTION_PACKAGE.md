# SM_GIA_BloodAxeCairnPathMarker_A01 Production Package

## 1. Art Direction Summary

- Task ID: `AET-MA-20260629-351`
- Asset name: `SM_GIA_BloodAxeCairnPathMarker_A01`
- Asset type: Static Mesh production package, docs-only
- Parent kit: `KIT_GIA_BloodAxePathMarkers_A01`
- Child intake row: `Blood Axe Village.png#PathMarkers_CairnSingle_A01`
- Faction/theme: Blood Axe Tribe, hostile Giant sub-faction only
- Package status: docs-only production specification for one single crude cairn path marker

`SM_GIA_BloodAxeCairnPathMarker_A01` is a low, hostile Blood Axe Giant route-dressing prop made from a few large field stones stacked into a crude cairn, with soot staining and mud packed around the base. It should read as rough raider-made camp language at MMO camera distance: squat, heavy, practical, and unpleasant, not elegant or civic.

This asset is not neutral or civilized Giant culture. Blood Axe visual language must remain separate from civilized Giant cave towns, blue-gray masonry, terraces, waterworks, warm hearth settlement dressing, refined highland route markers, civic stoneworker symbols, and restrained blue-rune language.

This package is planning only. It does not authorize DCC source creation, source-folder creation, sculpting, retopology, UVs, baking, collision proxy authoring, proof renders, LOD source, FBX export, Unreal Content creation, material instance creation, texture asset creation, runtime source, Blueprint work, startup placement, final visual approval, first DCC target selection, first implementation target selection, Hermes files, or Hermes configuration work.

## 2. Gameplay Purpose

The cairn supports static environmental readability inside Blood Axe Giant camp spaces. It can visually suggest the edge of a hostile footpath, a rough bend in a camp approach, or a repeated ground-level route rhythm, but it must remain non-interactive dressing.

Allowed purpose:

- Provide low, readable Blood Axe camp dressing near rough paths and trampled-earth approaches.
- Reinforce hostile Giant scale through oversized stones and crude stacked massing.
- Break up mud, ash, and packed-earth ground planes without becoming a mechanical marker.
- Complement sibling path-marker assets without borrowing their cloth, horn, shield, or banner features.

Out of scope:

- No waypoint behavior, trail-marker gameplay, objective logic, nav/pathfinding behavior, pickup/loot behavior, startup placement, UI marker, quest marker, minimap marker, interaction prompt, resource node, harvesting, salvage, crafting/economy behavior, combat cover definition, damage volume, faction buff, morale behavior, AI behavior, patrol marker, spawn marker, encounter scripting, VFX pulse, audio cue, material-state gameplay, or runtime logic.

## 3. Silhouette Notes

Primary silhouette:

- Crude stacked cairn, 80-180 cm tall, built from a few large field stones.
- Uneven tapered profile with a wide base, one or two heavy middle stones, and a blunt top stone.
- Slight off-axis lean is acceptable if the stack still feels stable and physically plausible.
- Stones should be chunky and readable from top-down MMO camera distance, not a pile of small pebbles.
- Mud should visibly ground the cairn with a low, irregular footprint instead of looking like a clean museum display.
- Soot should collect on lower stones, stone contact seams, and the muddy base, implying nearby fires and Blood Axe camp filth.

Model as major forms in any future approved DCC task:

- Base stones, middle stones, cap stone, broad bevels, large chipped corners, and the low mud/soot base.

Keep as texture, normal, or baked detail in any future approved material task:

- Fine stone cracks, tiny chips, pitting, soot speckles, ash flecks, dried mud streaks, subtle scrape marks, and small contact darkening.

Avoid:

- Cloth strips, horn tokens, bone markers, shield scraps, banners, readable runes, arrows, sign text, skull piles, graphic gore, refined carving, polished masonry, blue rune marks, glowing accents, or UI-like shapes. Those belong to other packages or require separate approval.

## 4. Scale Notes

Use the validated `SK_GIA_Base_A01` scale lock:

- Female Giant baseline: 442 cm / 14 ft 6 in.
- Male Giant baseline: 470 cm / 15 ft 5 in.
- Approved Giant range: females 14-15 ft / 427-457 cm; males 14 ft 10 in-16 ft / 452-488 cm.
- Author all future source in centimeters. 1 Unreal unit = 1 cm.

Asset dimensions:

- Height target: 80-180 cm.
- Footprint target: approximately 120-240 cm wide, depending on stone spread and mud base.
- Stone count: 3-6 major stones, plus optional very small supporting wedges only if they do not clutter the silhouette.
- Giant scale read: low shin-to-lower-thigh route dressing against the 442 cm female and 470 cm male baselines.
- Human scale read: large and intimidating, but not a monument or barricade.

The cairn should feel deliberately placed by Blood Axe Giants using stones that are heavy for smaller races. It must not feel like a human-scale wilderness cairn simply enlarged without design intent.

## 5. Materials and Color Palette

Primary materials:

- Rough field stone with soot-darkened lower faces.
- Mud packed around the base and pressed between lower stones.
- Ash and charcoal staining near the ground contact.
- Sparse dried grass or grit may appear as painted surface breakup only, not as separate foliage dressing.

Palette targets:

- Field stone gray-brown: `#3A3732` to `#6A6256`
- Soot and charcoal: `#0E0D0C` to `#242322`
- Wet mud: `#21170F` to `#3E2B1B`
- Dry mud and earth: `#5D4B35` to `#806847`
- Ash dust: `#6F6A61` to `#9A9285`
- Very restrained Blood Axe red smear, optional texture-only accent: `#5F1513` to `#7A1E18`

Material separation:

- One material slot target.
- No default emissive.
- No metallic requirement.
- No refined carved trim.
- No civilized Giant blue-gray masonry, warm hearth light, civic stone marks, terrace/waterwork motifs, highland guide symbols, or restrained blue runes.

Blood Axe identity should come from crude construction, soot, mud, harsh stone placement, and optional faint oxide-red staining, not from glowing magic or readable signage.

## 6. Concept Image Prompt

Create an original stylized fantasy MMORPG concept image of `SM_GIA_BloodAxeCairnPathMarker_A01` for the world of Aerathea. The design should emphasize a single crude stacked cairn, 80-180 cm tall, built from a few large field stones with a wide muddy base, soot-darkened lower stones, ash staining, chunky readable silhouette, hostile Blood Axe Giant sub-faction identity, clear separation from neutral/civilized Giant culture, and the gameplay role of static non-interactive route readability. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style stone surface detail, no default emissive glow, and MMO-friendly mid-poly production design. Present it as a single prop concept sheet on a clean background with front, side, top, material swatches, and scale callouts beside a 442 cm female Giant and a 470 cm male Giant. Avoid copying any existing franchise, avoid making Blood Axe culture the default Giant culture, avoid neutral Giant cave-town architecture, avoid cloth banners, horn trophies, shield scrap, readable text, waypoint behavior, trail-marker gameplay, objective logic, nav/pathfinding diagrams, pickup or loot behavior, startup placement claims, final approval language, and excessive micro-detail that would not translate to a mid-poly Unreal asset.

## 7. Modeling Notes

This is a docs-only modeling handoff. No DCC source, sculpt, retopo, UV, bake, FBX export, Unreal asset, collision proxy, proof render, material graph, validator file, startup actor, runtime source, Hermes file, or final visual approval is created or authorized by this package.

Future approved modeling should prioritize:

- Build the cairn from 3-6 large stones with distinct silhouettes and broad bevels.
- Use an uneven vertical stack with a wide lower stone, one or two heavy middle stones, and a blunt cap stone.
- Keep the base integrated with a low mud pad so the prop feels pressed into camp ground.
- Shape the stone contact areas to imply weight without requiring per-stone physics.
- Use asymmetry in stone rotation, edge chips, and mass distribution while preserving a readable upright stack.
- Keep the stone count low and the form bold enough to read from distant MMO camera angles.
- Make the asset self-contained as one static prop if later approved for implementation.

Recommended geometry treatment:

- Real geometry for major stone bodies, broad chips, large bevel breaks, main contact overlaps, and the low mud footprint.
- Texture or normal detail for fine cracks, small chips, soot freckles, ash dust, dried mud streaks, pitting, and subtle scrape marks.

Do not add:

- Cloth strips, poles, horn/bone parts, broken shield parts, sign boards, arrow shapes, skull piles, gore, sockets, attachment points, pickup affordances, destructible states, physics parts, gameplay volumes, nav helpers, objective helpers, or startup-scene review placement.

## 8. Texture and Material Notes

Material target:

- 1 material slot.
- 512-1K texture set for normal use.
- 1K preferred if the cairn will be viewed close to the player in a later approved art task.
- 2K is not required for this single small prop unless a later lead-approved close-review use case changes scope.

Required map plan for a future approved texture task:

- `T_GIA_BloodAxeCairnPathMarker_A01_BC`
- `T_GIA_BloodAxeCairnPathMarker_A01_N`
- `T_GIA_BloodAxeCairnPathMarker_A01_ORM`

No emissive texture is planned:

- Do not create `T_GIA_BloodAxeCairnPathMarker_A01_E` for the default asset.
- Any ritual, signal, shamanic, magic, or glow variant must be split into a separately approved package.

Base Color plan:

- Hand-painted stone color variation with warm gray, dirty brown, soot black, and ash gray.
- Mud should be darker and slightly warmer than stone.
- Optional oxide-red smear must be subtle, broad, and paint-like, not a UI arrow or readable symbol.

Normal plan:

- Broad stone plane changes, large chipped corners, stone contact compression, mud ridges, and shallow cracks.
- Keep tiny surface noise controlled so it does not glitter or clutter at distance.

Packed ORM plan:

- R: Ambient occlusion in stacked stone contacts, under the cap stone, around lower stones, and where mud meets rock.
- G: High roughness for stone, soot, ash, and mud, with subtle wetness variation only in the mud.
- B: Metallic should remain black unless a later approved variant adds hardware, which this A01 asset does not include.

## 9. Triangle Budget

Target as a small prop:

- LOD0: 800-2,500 tris, 1 material.
- LOD1: 450-1,400 tris.
- LOD2: 200-650 tris.
- LOD3: 80-250 tris.

Budget priorities:

- Spend triangles on the main stacked stone silhouette, broad chipped corners, cap-stone profile, lower contact shapes, and mud base outline.
- Do not spend triangles on tiny pebbles, dense cracks, small ash clumps, many chips, repeated soot flecks, or underside detail.
- If a later approved implementation combines this cairn into a repeated route set, favor instancing and shared material use over unique high-density variations.

## 10. LOD Plan

All important future implementations require LOD0-LOD3 before import approval in a separate task.

- LOD0: Full 3-6 stone stack, broad bevels, readable chipped edges, low mud base, soot-darkened lower shape, and clear top-down silhouette.
- LOD1: Preserve stone count and overall lean; simplify bevels, reduce mud edge cuts, merge minor stone cuts, and bake small chip detail.
- LOD2: Preserve stacked cairn mass, cap stone, base footprint, and soot/mud color read; remove small stone profile variations and most underside detail.
- LOD3: Preserve only the broad tapered cairn silhouette and base mass; collapse small stones into simpler volumes and rely on baked color/normal detail.

Reduction order:

1. Tiny soot flecks, ash speckles, small pitting, and tiny surface chips.
2. Minor mud ridges and underside cuts.
3. Small supporting wedges or non-silhouette chips.
4. Secondary bevels on hidden stone faces.
5. Back-side contact detail that is not visible from normal camera angles.

Never reduce the primary stack silhouette, the Giant-scale mass read, or the soot/mud base identity before removing small detail.

## 11. Collision Notes

Default collision guidance:

- Collision disabled is acceptable for purely visual dressing if later placement does not require player contact.
- If collision is needed in a later approved implementation task, use one simple box, capsule, or low-count convex hull around the main cairn mass.
- Do not create per-stone collision.
- Do not create mud-base collision unless terrain contact requires a simple broad blocker.
- Do not mark it as a nav blocker by default.

Explicitly out of scope:

- No waypoint collision, trail-marker collision, objective volume, nav/pathfinding helper, pickup collision, loot collision, interaction collision, destructible collision, physics collision, combat cover collision, AI marker collision, spawn logic volume, aura volume, damage volume, or startup placement collision.

## 12. Animation Notes

The asset is static.

Approved animation scope:

- None.

Not approved here:

- No skeletal setup, vertex animation, physics wobble, destructible collapse, material animation, VFX pulse, ember effect, smoke effect, glow state, audio cue, interaction response, waypoint behavior, trail-marker gameplay, objective logic, nav/pathfinding behavior, pickup/loot behavior, AI behavior, patrol behavior, spawn timing, startup placement, or runtime state change.

Any animated, glowing, interactive, destructible, objective, pickup, waypoint, or gameplay-readable variant must be split into a separately named and separately approved package.

## 13. Unreal Import Notes

This section records future constraints only. It does not create or select an Unreal implementation target, and it does not authorize Unreal Content creation, material instance creation, texture import, Blueprint work, socket work, validator work, runtime source work, startup placement, or final visual approval.

Future import constraints if a separate implementation task is approved:

- Asset name: `SM_GIA_BloodAxeCairnPathMarker_A01`
- Asset type: Static Mesh
- Authorized Unreal folder for this task: none; no `/Game` path is selected or created by this package.
- Pivot: ground center under the cairn footprint.
- Orientation: primary cairn lean and strongest read should face +X only if later project convention confirms that orientation.
- Scale: centimeter-authored source, Unreal import scale 1.0.
- Collision type: disabled or one simple primitive/convex hull only if later placement requires it.
- LODs: LOD0-LOD3 required before any later import approval.
- Material slot count: 1.
- Texture list: `T_GIA_BloodAxeCairnPathMarker_A01_BC`, `T_GIA_BloodAxeCairnPathMarker_A01_N`, `T_GIA_BloodAxeCairnPathMarker_A01_ORM`.
- Emissive texture: none.
- Sockets: none.
- Animation list: none.
- Blueprint behavior: none.
- Performance notes: keep collision minimal, share material language with Blood Axe path-marker stone assets, preserve silhouette at distance, and avoid unique high-cost material variants for repeated cairns.

Do not add waypoint behavior, trail-marker gameplay, objective logic, nav/pathfinding behavior, pickup/loot behavior, startup placement, source folders, FBX exports, Unreal assets, implementation target choices, Hermes files, or Hermes configuration from this package.

## 14. Folder and Naming Recommendation

Allowed docs path for this task:

- `docs/assets/props/SM_GIA_BloodAxeCairnPathMarker_A01/PRODUCTION_PACKAGE.md`

Reserved asset naming:

- Static mesh name: `SM_GIA_BloodAxeCairnPathMarker_A01`
- Material instance name, if separately approved later: `MI_GIA_BloodAxeCairnPathMarker_A01`
- Base Color texture name, if separately approved later: `T_GIA_BloodAxeCairnPathMarker_A01_BC`
- Normal texture name, if separately approved later: `T_GIA_BloodAxeCairnPathMarker_A01_N`
- ORM texture name, if separately approved later: `T_GIA_BloodAxeCairnPathMarker_A01_ORM`

Not authorized by this task:

- No `Content/Aerathea/` edits.
- No `SourceAssets/` edits.
- No `Tools/DCC/` edits.
- No `Tools/Unreal/` edits.
- No runtime source edits.
- No external source concept copying, movement, editing, embedding, inspection for visual approval, or commits.
- No global index edits.
- No Hermes file or configuration edits.
- No DCC, FBX, Unreal, final approval, or implementation target work.

## 15. Quality Gate Checklist

- Package is docs-only and changes only the allowed production package file.
- Asset remains a single crude stacked cairn, not a cluster, cloth stake, horn marker, shield marker, banner marker, ritual stone, or review row.
- Height range is explicit: 80-180 cm tall.
- Construction is limited to a few large field stones with soot and mud at the base.
- Female Giant scale is explicit: 442 cm / 14 ft 6 in.
- Male Giant scale is explicit: 470 cm / 15 ft 5 in.
- Blood Axe identity is treated as a hostile Giant sub-faction only.
- Blood Axe visual language remains separate from neutral/civilized Giant culture.
- No civilized Giant cave-town, blue-gray masonry, warm hearth, terrace, waterwork, civic stoneworker, refined highland marker, or restrained blue-rune language is used.
- Gameplay purpose is static visual route readability only.
- No waypoint behavior, trail-marker gameplay, objective logic, nav/pathfinding behavior, pickup/loot behavior, startup placement, UI marker, VFX pulse, audio cue, interaction, resource, combat, AI, patrol, spawn, or encounter behavior is defined.
- No DCC source, source folder, sculpt, retopo, UV, bake, collision proxy, proof render, LOD source, FBX export, Unreal Content, material instance, texture asset, Blueprint, runtime source, final visual approval, implementation target, Hermes file, or Hermes configuration is created or authorized.
- Triangle budget, LOD0-LOD3 plan, collision limits, animation limits, texture map plan, material slot target, and Unreal import constraints are included.
- Tiny chips, cracks, soot speckles, ash flecks, pitting, and dried mud streaks are assigned to textures or normals rather than unnecessary geometry.
- The package is useful for a later approved production handoff without selecting or starting that future implementation work.
