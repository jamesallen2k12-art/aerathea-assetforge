# SM_GIA_BloodAxePackedEarthPath_A01 Production Package

## Art Direction Summary

- Asset name: `SM_GIA_BloodAxePackedEarthPath_A01`
- Asset type: Static Mesh production package / visual ground dressing path strip
- Task: `AET-MA-20260629-131`
- Parent kit: `KIT_GIA_BloodAxeCamp_A01`
- Source child ID: `BloodAxeCamp.png#Path_MainPackedEarth`
- Faction/theme: Blood Axe Tribe, hostile Giant sub-faction
- Status: docs-only static visual production package ready for planning review
- Source-storage guardrail: source concepts remain external through existing intake records. Do not copy, move, crop, edit, embed, inspect for final approval, or commit source images for this task.

`SM_GIA_BloodAxePackedEarthPath_A01` defines a Giant-wide packed-earth path strip for Blood Axe camp layouts. It is a low-profile ground dressing asset with trampled mud, compacted dirt, ash, boot-worn ruts, scattered gravel, and rough log edging that helps mark the physical footprint of a hostile raider camp.

This asset is visual ground dressing and footprint planning only. It does not authorize DCC source creation, FBX export, Unreal Content creation, material graph authoring, modular snapping implementation, nav/pathfinding behavior, collision proxy creation, terrain blending, startup placement, final visual approval, first DCC target selection, runtime behavior, VFX, audio, or source concept movement.

Blood Axe path language must stay separate from neutral/civilized Giant culture. It should read as rough hostile camp infrastructure made by a brutal Giant sub-faction, not as the refined blue-gray masonry, hearth-lit terrace, waterwork, or restrained blue-rune language of civilized Giant cave towns.

## Gameplay Purpose

The path supports future Blood Axe camp readability by showing where enormous raiders, prisoners, carts, sledges, forge traffic, and sentries have worn the ground down through repeated use. It should guide composition and footprint planning without becoming gameplay navigation.

Allowed planning purpose:

- Static visual route marker for Blood Axe camp entrances, shelter rows, forge lanes, cooking pits, watch points, and stronghold approaches.
- Giant-scale footprint reference for future camp dressing around `SM_GIA_BloodAxeCampGate_A01`, `SM_GIA_BloodAxeWatchPlatform_A01`, shelter assets, forge props, barricades, and banner lines.
- Ground-surface identity for hostile Blood Axe camps using compacted dirt, churned mud, ash, log edging, and crude red warning accents.
- Visual scale contrast between smallfolk and the validated Giant baselines.

Out of scope:

- Navmesh, pathfinding, AI patrol routes, player guidance logic, quest markers, trigger volumes, spline systems, runtime decals, terrain blending, landscape materials, modular snapping implementation, collision proxy creation, DCC build, Unreal import, startup placement, damage volumes, loot/resource/crafting/economy behavior, or interactable path behavior.

## Silhouette Notes

Primary silhouette: a long, low, flattened path strip with broad Giant-scale width, uneven compressed edges, shallow worn ruts, log or stone edging, and visible directional flow through hostile camp space. It should read clearly from MMO camera distance as a traveled Blood Axe route without becoming a raised road, bridge, or full terrain system.

Key visual reads:

- Wide compacted center lane with two or three broad ruts sized for Giant foot traffic and dragged loads.
- Slightly raised or darker packed-earth center with churned mud at the edges.
- Crude log edging, half-buried stakes, stone weights, or broken plank edges used sparingly to keep the path readable.
- Boot depressions scaled for Giants, not normal humanoids; keep them broad and stylized rather than dense.
- Ash, charcoal dust, soot, trampled grass remnants, gravel, and clay color variation.
- Small red cloth scraps, paint smears, or warning-thread ties only as minimal Blood Axe identifiers.
- Optional sparse bone, horn, broken shield, or scrap markers at the edge only if they remain non-graphic and do not turn the path into a trophy marker asset.
- Low profile that does not compete with gates, shelters, towers, banners, or barricades.

Model only the main plane, raised edge lips, major log edging, large embedded stones, and broad rut geometry as future real geometry. Use texture, normals, AO, and material variation for small pebbles, mud cracks, footprint texture, bark grain, minor splinters, ash specks, grass remnants, and tiny scratches.

Avoid civilized Giant paving, cut stone roadwork, clean masonry borders, carved blue-gray terrace blocks, blue rune inlays, warm civic hearth identity, refined water-channel detailing, dense skull clutter, graphic gore, tiny modeled debris, or a terrain chunk that hides the primary path read.

## Scale Notes

Use the validated Giant scale lock exactly:

- Female Giant baseline: 442 cm / 14'6".
- Male Giant baseline: 470 cm / 15'5".
- Approved Giant range: females 14-15 ft / 427-457 cm; males 14'10"-16'0" / 452-488 cm.
- Author in centimeters. 1 Unreal unit = 1 cm.

Recommended visual footprint planning dimensions:

- Standard straight strip length: 900-1200 cm.
- Standard visible path width: 420-560 cm.
- Edge-to-edge width with log borders or mud shoulder: 520-700 cm.
- Thickness or height offset: 4-18 cm above the underlying ground plane for future static-mesh dressing, with edges feathered visually by texture rather than terrain blending in this task.
- Main Giant boot depressions: 90-140 cm long and 45-80 cm wide, used sparingly as broad shape language.
- Main rut width: 70-140 cm per rut, with 80-180 cm spacing depending on lane read.
- Log edging diameter: 25-55 cm for half-buried logs, with larger 70 cm anchor pieces only where the silhouette needs them.
- Embedded stones: 25-90 cm, chunky and sparse.

The path should feel comfortable for one Giant moving through camp gear or two Giants passing with tension, while making normal humanoids feel small. These dimensions are footprint planning only and do not define playable lane width, navmesh width, collision clearance, or modular snapping rules.

## Materials and Color Palette

Primary materials:

- Packed dark earth, compacted mud, clay, gravel, ash, and soot.
- Half-buried rough timber, split log edging, stake remnants, and bark.
- Scattered dark field stones, slag-like pebbles, charcoal pieces, and trampled dry grass.
- Optional blackened iron scraps, broken shield chips, or crude plate fragments at the edge in very low density.
- Optional faded red cloth ties or oxide-red paint smears as Blood Axe identifiers.

Palette targets:

- Dominant: dark umber earth, cool mud brown, charcoal gray, soot black, and muted clay.
- Secondary: weathered bark brown, dry grass olive, field-stone gray, and slag black.
- Faction accent: deep oxide red or faded maroon in tiny restrained marks.
- Emissive: none.

Blood Axe separation rule:

- Use hostile raider-camp grime, churned earth, rough timber, ash, and red warning accents.
- Do not use neutral/civilized Giant culture materials such as refined stonework, carved blue-gray masonry, clean terrace blocks, warm hearth-road treatment, elegant cave-town paving, waterwork channels, restrained blue runes, or civic clan markers.

## Concept Image Prompt

Create an original stylized fantasy MMORPG concept image of `SM_GIA_BloodAxePackedEarthPath_A01` for the world of Aerathea. The design should emphasize a Giant-wide hostile Blood Axe packed-earth camp path, low flattened ground dressing silhouette, compacted dark mud, broad Giant boot depressions, worn ruts, half-buried log edging, embedded field stones, ash and soot staining, trampled grass remnants, sparse oxide-red Blood Axe warning scraps, rough raider-camp construction, clear separation from neutral/civilized Giant cave-town road language, and the gameplay role of visual ground dressing and footprint planning only. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, no emissive glow, and MMO-friendly production design. Present it as a static mesh production sheet with top view, side thickness view, straight-strip footprint, material swatches, scale bars beside a 442 cm female Giant and a 470 cm male Giant, LOD planning notes, and a clear note that nav/pathfinding, terrain blending, modular snapping implementation, collision proxy creation, DCC, FBX, Unreal import, and startup placement are out of scope. Avoid copying any existing franchise, avoid graphic gore, avoid refined civilized Giant masonry, avoid making Blood Axe culture the default Giant culture, avoid AI path diagrams, avoid spline or terrain-system diagrams, and avoid excessive micro-detail that would not translate to a mid-poly Unreal asset.

## Modeling Notes

This package is a planning document only. Future DCC work requires a separate approved task before any source folders, Blender files, proof renders, collision proxies, LOD sources, FBX exports, material graphs, terrain blends, or Unreal assets are created.

Future modeling should prioritize these readable forms:

- One low, broad rectangular or gently irregular path strip with uneven boundaries.
- Slight raised lip or bevel around the mud shoulder to catch light without becoming a curb.
- Broad shallow rut depressions and flattened central lane forms.
- Sparse half-buried logs along one or both sides, broken where camp traffic has damaged them.
- A few embedded field stones and mud clumps large enough to read at game camera distance.
- Optional split-plank patches or crude stake edges where the path passes near gates or shelters.
- Optional edge debris in very low density: broken shield chunk, iron scrap, bone/horn marker, or red cloth tie.

Use textures, normals, and AO for:

- Fine mud cracks, grit, shallow footprint noise, pebble scatter, bark grain, soot dust, charcoal specks, grass remnants, small splinters, minor scratches, wet/dry mud variation, and small cloth fibers.

Simplification rules:

- Keep the asset flat and readable; it must not become a raised bridge, road kit, terrain tile system, or full camp-scene base.
- Keep edge dressing sparse enough that barricades, path markers, camp clutter, ritual stones, and stronghold approach modules remain separate packages.
- Do not model hundreds of pebbles, grass blades, footprints, splinters, stitch holes, rope strands, or mud chunks.
- Do not add nav arrows, gameplay markers, route icons, patrol indicators, collision volumes, spline handles, or modular snapping sockets.

## Texture and Material Notes

Target material slot count:

- Preferred: 1 material slot.
- Maximum: 2 material slots if future visual approval needs separate log-edge material control.

Suggested slots:

- Slot 0: `MI_GIA_BloodAxePackedEarth_A01` for packed earth, mud, ash, gravel, soot, grass remnants, and broad footprint/rut detail.
- Optional slot 1: `MI_GIA_BloodAxeRoughTimber_A01` for half-buried log edging and large broken timber pieces.

Required future texture maps:

- `T_GIA_BloodAxePackedEarthPath_A01_BC`
- `T_GIA_BloodAxePackedEarthPath_A01_N`
- `T_GIA_BloodAxePackedEarthPath_A01_ORM`

Optional future texture maps only after separate approval:

- `T_GIA_BloodAxePackedEarthPath_A01_Mask` for controlled mud, ash, rut, dry-edge, red-scrap, or wetness variation.

No emissive map is planned for the baseline asset.

Texture set targets:

- Standard path strip: 1K texture set.
- Repeated far-camp dressing variant: 512 texture set if repeated heavily.
- Hero close-up camp entrance variant: 2K only with explicit approval.

Packed ORM guidance:

- R: Ambient occlusion in ruts, under embedded stones, under half-buried logs, around mud shoulders, and in deep footprints.
- G: Roughness high for dry earth, ash, bark, dust, and trampled grass; medium-high with subtle variation for damp mud.
- B: Metallic should remain black except for optional tiny blackened iron scrap regions.

Material guardrails:

- Do not author terrain blend materials, runtime decal materials, landscape layers, virtual textures, spline materials, or material graph logic in this task.
- Future terrain or landscape blending, if needed, requires a separate approved implementation package.

## Triangle Budget

`SM_GIA_BloodAxePackedEarthPath_A01` is a low-profile ground dressing prop. It should stay far below large structure budgets.

Targets:

- LOD0 target: 1.2k-2.8k tris.
- LOD0 hard cap: 4k tris.
- Material slots: 1 target, 2 maximum.
- Texture set: 1K standard; 512 for repeated far dressing; 2K only with explicit hero approval.

Suggested LOD0 allocation:

- Main path plane, edge lip, broad ruts, and silhouette bevels: 45-55 percent.
- Half-buried log edging and large timber damage: 20-30 percent.
- Embedded stones, large mud clumps, and readable edge debris: 12-18 percent.
- Optional red scraps, shield chips, or sparse Blood Axe markers: 3-7 percent.
- Minor bevels and asymmetry: remaining budget only after the primary path read is stable.

Do not spend triangles on dense pebbles, tiny grass blades, per-footprint relief, small cracks, fine splinters, cloth fibers, individual ash specks, or many small debris pieces.

## LOD Plan

All future approved mesh work should include LOD0-LOD3.

- LOD0: 1.2k-2.8k tris target, 4k hard cap. Full path footprint, broad ruts, edge lips, half-buried log edging, embedded stones, major mud clumps, and sparse Blood Axe markers.
- LOD1: 60-70 percent of LOD0. Reduce edge bevel cuts, stone subdivisions, log-edge segments, red-scrap geometry, and minor rut contours.
- LOD2: 35-45 percent of LOD0. Preserve the wide path outline, main ruts, major log/stone edge masses, and broad value separation while flattening small edge debris.
- LOD3: 15-25 percent of LOD0. Preserve the dark path rectangle, rough edge silhouette, and Giant-wide footprint. Remove most stones, small logs, red scraps, and minor rut relief.

Reduction order:

1. Tiny cracks, pebble noise, grass blades, ash specks, bark chips, and cloth fibers.
2. Small red scraps, shield chips, tiny stones, and minor mud clumps.
3. Secondary log cuts, small edge bevels, and subtle rut subdivisions.
4. Embedded stone undercuts and optional edge debris.
5. Only then reduce the primary path outline, broad ruts, edge lip, and main Giant-scale width.

Never destroy the path's broad Giant-wide footprint, low ground-dressing profile, or Blood Axe camp material read before removing small detail.

## Collision Notes

Collision is planning only. Do not create collision proxies, UCX meshes, physics bodies, runtime collision channels, nav links, nav blockers, navmesh modifiers, damage volumes, interaction volumes, terrain blockers, or validation scripts from this task.

Future collision intent:

- Default recommendation: collision disabled. The path is visual ground dressing; player, NPC, and physics traversal should be handled by the underlying landscape, floor, or approved environment collision.
- If a future map needs contact response for raised log edging, use one or two very simple non-complex hulls around only the largest edge logs after separate approval.
- Do not add collision to pebbles, mud clumps, footprints, red scraps, cloth ties, grass remnants, shield chips, horn/bone markers, or small debris.
- Do not use this asset to define gameplay lane width, AI patrol width, navmesh carving, pathfinding preference, or movement cost.

## Animation Notes

No animation is planned.

The baseline asset is a static ground dressing path strip. Do not add animated mud, cloth flutter, shifting debris, footprint deformation, runtime decals, particle dust, water ripples, procedural track generation, or spline deformation from this package. Any future animated dust, weathering, footprint, or wet-mud state requires separate VFX/material/runtime approval.

## Unreal Import Notes

This section is future planning only. Do not create Unreal Content, import FBX, author materials, build collision, place in startup, or run Unreal validators from this task.

Future import target:

- Asset name: `SM_GIA_BloodAxePackedEarthPath_A01`
- Asset type: Static Mesh
- Suggested Unreal path: `/Game/Aerathea/Props/Giants/BloodAxe/Camp/SM_GIA_BloodAxePackedEarthPath_A01`
- Suggested material instance path: `/Game/Aerathea/Materials/Giants/BloodAxe/MI_GIA_BloodAxePackedEarth_A01`
- Naming convention:
  - Static mesh: `SM_GIA_BloodAxePackedEarthPath_A01`
  - Material instance: `MI_GIA_BloodAxePackedEarth_A01`
  - Optional timber material instance: `MI_GIA_BloodAxeRoughTimber_A01`
  - Textures: `T_GIA_BloodAxePackedEarthPath_A01_BC`, `T_GIA_BloodAxePackedEarthPath_A01_N`, `T_GIA_BloodAxePackedEarthPath_A01_ORM`
- Pivot location: center of footprint at ground plane, with Z at the bottom of the dressing mesh.
- Scale: centimeters, 1 Unreal unit = 1 cm.
- Collision type: no collision by default; any simple edge collision requires separate approval.
- LODs: LOD0, LOD1, LOD2, LOD3.
- Material slot count: 1 target, 2 maximum.
- Sockets: none.
- Animation list: none.
- Blueprint behavior: none.
- Performance notes: keep low-poly, low material count, no emissive, no runtime deformation, no terrain blend logic, no nav/pathfinding behavior, and no modular snapping implementation in this package.

## Folder and Naming Recommendation

Documentation path created by this task:

- `docs/assets/props/SM_GIA_BloodAxePackedEarthPath_A01/PRODUCTION_PACKAGE.md`

Future content recommendations only, not created by this task:

- Static mesh: `/Game/Aerathea/Props/Giants/BloodAxe/Camp/SM_GIA_BloodAxePackedEarthPath_A01`
- Material instance: `/Game/Aerathea/Materials/Giants/BloodAxe/MI_GIA_BloodAxePackedEarth_A01`
- Optional timber material instance: `/Game/Aerathea/Materials/Giants/BloodAxe/MI_GIA_BloodAxeRoughTimber_A01`
- Source asset folder, if later approved: `SourceAssets/Props/Giants/BloodAxe/SM_GIA_BloodAxePackedEarthPath_A01/`

Related planning dependencies:

- Parent kit: `docs/assets/kits/KIT_GIA_BloodAxeCamp_A01/PRODUCTION_PACKAGE.md`
- Child intake: `docs/assets/kits/KIT_GIA_BloodAxeCamp_A01/CHILD_ASSET_INTAKE.md`
- Scale dependency: `docs/assets/characters/SK_GIA_Base_A01/PRODUCTION_PACKAGE.md`
- Adjacent Blood Axe packages: `SM_GIA_BloodAxeCampGate_A01`, `SM_GIA_BloodAxeTrophyGate_A01`, `SM_GIA_BloodAxeWatchPlatform_A01`, `SM_GIA_BloodAxeForgeHearth_A01`, `SM_GIA_BloodAxeCookingPit_A01`, `KIT_GIA_BloodAxeBannerLine_A01`, and future path, marker, barricade, clutter, ritual-stone, and stronghold modules.

Do not update global indexes, backlog files, bootstrap docs, source concept folders, DCC tools, Unreal tools, runtime source, or `Content/Aerathea/` from this task.

## Quality Gate Checklist

- [x] Uses the universal Aerathea production package format.
- [x] Defines `SM_GIA_BloodAxePackedEarthPath_A01` as docs-only planning.
- [x] Treats the packed earth path as visual ground dressing and footprint planning only.
- [x] Keeps Blood Axe as a hostile Giant sub-faction, not neutral/civilized Giant culture.
- [x] Includes neutral/civilized Giant culture separation wording.
- [x] Includes validated Giant scale anchors: female baseline 442 cm / 14'6" and male baseline 470 cm / 15'5".
- [x] Uses Blood Axe camp material language: packed mud, ash, soot, rough timber, field stones, and restrained red warning accents.
- [x] Avoids civilized Giant cave-town road language, refined masonry, warm hearth identity, blue-gray terraces, and restrained blue runes.
- [x] Includes concept prompt, modeling notes, texture/material plan, triangle budget, LOD0-LOD3 plan, collision notes, animation notes, Unreal import notes, and folder/naming recommendations.
- [x] Stops before DCC, FBX, Unreal Content, source folder creation, material graph authoring, modular snapping implementation, nav/pathfinding behavior, collision proxy creation, terrain blending, startup placement, first DCC target selection, source concept movement, and final visual approval.
- [x] Keeps material slots low and no emissive baseline.
- [x] Keeps geometry low-profile, MMO-safe, and mid-poly friendly.
- [x] Avoids graphic gore, excessive debris, dense trophy clutter, tiny modeled pebbles, spline diagrams, nav diagrams, terrain-system diagrams, and runtime behavior claims.
