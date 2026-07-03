# SM_GIA_BloodAxeLogWalkway_A01 Production Package

## Art Direction Summary

- Asset name: `SM_GIA_BloodAxeLogWalkway_A01`
- Asset type: Static Mesh production package / hostile Blood Axe Giant visual route dressing
- Task: `AET-MA-20260629-132`
- Parent kit: `KIT_GIA_BloodAxeCamp_A01`
- Source child ID: `BloodAxecamp.png#Path_LogWalkway`
- Related visual packages: `KIT_GIA_BloodAxeCamp_A01`, `SM_GIA_BloodAxePackedEarthPath_A01`, `SM_GIA_BloodAxeWatchPlatform_A01`, `SM_GIA_BloodAxeCampGate_A01`, and `KIT_GIA_BloodAxePathMarkers_A01`
- Faction/theme: Blood Axe Tribe, hostile Giant sub-faction only
- Status: docs-only static visual production package ready for planning review
- Source-storage guardrail: source concepts remain external through existing intake records. Do not copy, move, crop, edit, embed, inspect for final approval, or commit source images for this task.

`SM_GIA_BloodAxeLogWalkway_A01` defines a rough Giant-scale log walkway or raised crossing used as Blood Axe camp route dressing. It should read as a brutal temporary path element made from massive split logs, uneven crossbeams, mud-packed edges, crude blackened-iron spikes, rawhide lashings, soot, ash, deep red warning cloth, and sparse non-graphic horn or bone route markers.

Blood Axe must remain a hostile Giant sub-faction, not neutral/civilized Giant culture. This walkway uses raider-camp construction language only and must stay separate from neutral/civilized Giant cave-town masonry, blue-gray stoneworker craft, warm hearth halls, refined terraces, waterworks, highland nomad domestic identity, and restrained blue-rune motifs.

This package is planning-only and docs-only. It treats the log walkway as visual route dressing and scale planning only. It does not authorize DCC source creation, collision proxy creation, FBX export, Unreal Content creation, runtime source, Blueprint behavior, walkable collision implementation, navmesh or pathfinding behavior, modular snapping, destructible behavior, startup placement, source concept movement, first DCC target selection, final visual approval, or implementation work.

## Gameplay Purpose

The purpose is visual route dressing only: make Blood Axe camp lanes, ditch crossings, mud gaps, shelter approaches, and gate approaches read as Giant-built, hostile, and temporary at MMO camera distance.

Allowed visual planning uses:

- Suggest a rough route through a Blood Axe camp without defining player, NPC, or AI traversal.
- Establish the scale of Giant-wide log paths against the validated `SK_GIA_Base_A01` body baselines.
- Add visual contrast against packed-earth paths, forge yards, shelter rows, barricades, and camp gates.
- Support enemy-territory storytelling through crushed mud, split timber, ash, blackened iron, rawhide lashings, and red Blood Axe warning scraps.
- Provide a future static environment prop reference for route composition, not a gameplay movement system.

Out of scope:

- Walkable collision implementation, navigation mesh setup, pathfinding, AI patrol lanes, smart links, climb logic, ramp traversal, player step-up tuning, movement friction, spline paths, modular snap rules, grid placement, destructible states, physics reactions, bridge collapse, trap behavior, damage volumes, objective logic, resource collection, loot, crafting, salvage, interaction prompts, or camp ownership mechanics.

## Silhouette Notes

Primary silhouette: a low, heavy, uneven strip of Giant-scale logs laid over mud or a shallow crossing, with a clear broad route read, raised edges, crude lashings, and a few Blood Axe warning accents.

Silhouette goals:

- Read as a rough log walkway before the viewer resolves small detail: long timber direction, cross-log rhythm, mud-packed edges, and a hostile red marker must be visible from top-down and three-quarter views.
- Use five to nine oversized split logs or trunk halves as the main walking surface, with irregular lengths and a slightly staggered outline.
- Add two to four broad crossbeams or underside sleepers to show the walkway was dragged, lashed, or hammered into place by Giants.
- Include side edging with half-buried logs, crude stakes, or stone weights. Keep edges chunky, not delicate.
- Add one to three Blood Axe identifiers: torn red cloth strips, chipped red paint marks, horn route markers, broken shield scraps, or blackened iron warning spikes.
- Keep trophy detail sparse and non-graphic. The route should feel hostile through scale and material abuse, not gore.
- Avoid refined bridge architecture, clean decking, symmetrical civic craft, polished handrails, decorative stone piers, or normal humanoid boardwalk proportions.
- Optional raised crossing shapes may appear as visual mass only. Do not imply an approved ramp, bridge traversal, walkable surface, or nav path.

Model real geometry for the main logs, split-log caps, broad crossbeams, large side edging, major stakes, oversized lashings, blackened iron plates, stone weights, and large red cloth scraps. Use texture, normal, and AO detail for tiny cuts, wood grain, rope fibers, nail heads, soot streaks, leather pores, small scratches, minor cracks, cloth weave, and mud flecks.

## Scale Notes

Use the validated `SK_GIA_Base_A01` scale lock without alteration:

- Female Giant baseline: 442 cm / 14'6".
- Male Giant baseline: 470 cm / 15'5".
- Approved Giant ranges: females 14-15 ft / 427-457 cm; males 14'10"-16'0" / 452-488 cm.
- Author future source in centimeters. 1 Unreal unit = 1 cm.
- Normal humanoid comfort is not required. Smallfolk should read as trespassers on an oversized enemy-camp route.

Recommended static scale targets:

- Overall visual length: 900-1500 cm for baseline `A01`, enough to read as a camp route segment without selecting a modular snap length.
- Overall visual width: 520-760 cm, wide enough for a 470 cm Giant route read and broad enough to feel hostile and oversized.
- Surface height above surrounding mud: 25-100 cm for low walkway variants; up to 160 cm for a raised visual crossing variant only.
- Main log diameter or split-log thickness: 45-95 cm, irregular.
- Main log visible length: 650-1400 cm, with some cut shorter to break the outline.
- Crossbeam diameter or thickness: 30-70 cm.
- Side edging or half-buried log height: 35-85 cm.
- Stake or warning spike height: 90-220 cm, used sparingly so the walkway does not become a barricade.
- Red cloth marker size: 60-160 cm wide by 80-220 cm long, dirty and tattered but not dense.
- Mud or ash shoulder width: 60-160 cm on either side if included in the mesh footprint.

Route readability is visual only:

- The asset can imply where Blood Axe Giants have moved through a camp.
- It must not define path width, passability, AI lane width, movement speed, step height, climbability, or player traversal behavior.
- It must not require modular snapping, socketed path connections, terrain blending implementation, or nav/pathfinding authoring.

## Materials and Color Palette

Primary materials:

- Raw dark timber, split logs, charred trunks, rough crossbeams, and mud-dark plank faces.
- Packed mud, wet earth, ash, soot, trampled dirt, and crushed charcoal along the contact edges.
- Hide lashings, sinew wraps, heavy rope, scorched leather ties, and rawhide repairs.
- Blackened iron, dark steel, stolen scrap plates, large pegs, crude spikes, and clamp bands.
- Torn Blood Axe red cloth, dirty red paint, and warning strips as hostile sub-faction identifiers.
- Sparse bone, horn, broken shield fragments, or dry route markers used non-graphically and at large scale.

Suggested palette:

- Charred timber: `#1A1510` to `#3A2618`
- Weathered raw wood: `#5B412D` to `#8A6A45`
- Wet mud and trampled earth: `#1C1510` to `#4A3829`
- Soot and ash: `#0B0A09` to `#3C3832`
- Blackened iron: `#141619` to `#2E3031`
- Dark reforged steel: `#54585A` to `#797A76`
- Blood Axe red cloth: `#5A1412` to `#8A211A`
- Scorched leather and hide: `#241611` to `#5B3A27`
- Bone and horn accents: `#A69578` to `#D0B98C`

Avoid neutral/civilized Giant material language: no blue-gray carved stoneworker masonry, no warm civic hearth treatment, no restrained blue runes, no refined highland clan banners, no clean cave-town bridge craft, no waterwork elegance, and no polished peaceful settlement identity.

No default emissive is approved. Forge heat, shamanic glow, torchlight, magic route markers, faction aura, warning VFX, or animated material states require a separate package and approval gate.

## Concept Image Prompt

Create an original stylized fantasy MMORPG concept image of `SM_GIA_BloodAxeLogWalkway_A01` for the world of Aerathea. The design should emphasize a hostile Blood Axe Giant log walkway used as visual route dressing only, validated Giant scale with female baseline 442 cm / 14'6" and male baseline 470 cm / 15'5", a broad low strip of massive split logs over mud, irregular trunk lengths, thick crossbeams, half-buried side logs, crude rawhide lashings, blackened iron clamp plates, soot, ash, wet earth, torn deep red warning cloth, sparse non-graphic horn or bone route markers, hostile Giant sub-faction identity, and a gameplay role limited to static enemy-camp route composition and scale planning. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, no default emissive glow, and MMO-friendly mid-poly production design. Present it as a static prop concept sheet with front, side, back, top-down footprint, three-quarter view, material swatches, LOD/collision planning notes, scale markers beside a 442 cm female Giant and a 470 cm male Giant, and clear labels that it is visual route dressing only on a clean background or simple Blood Axe camp context. Avoid copying any existing franchise, avoid making Blood Axe language the default Giant culture, avoid neutral/civilized Giant cave-town materials, avoid graphic gore, avoid navmesh/pathfinding diagrams, avoid walkable collision diagrams, avoid modular snapping grids, avoid destructible behavior, avoid interaction prompts, avoid final visual approval claims, and avoid excessive micro-detail that would not translate to a mid-poly Unreal asset.

Source reference note: use `BloodAxecamp.png#Path_LogWalkway` only as an intake route reference. This docs-only package does not copy, move, inspect for final approval, crop, embed, edit, or commit external source concept imagery.

## Modeling Notes

This is a docs-only modeling plan. No mesh, Blender source, sculpt, retopo, UV, bake, collision proxy, LOD source, FBX export, Unreal asset, material graph, validator, startup placement, or final visual approval is created or approved by this package.

Future modeling should build large readable forms first:

- Main route surface: five to nine massive split logs or trunk halves with uneven lengths, broad end cuts, worn top planes, and strong overlap shadows.
- Crossbeams: two to four heavy sleepers underneath or across the logs, visible from side and three-quarter views.
- Edge forms: half-buried side logs, mud shoulders, crude stakes, or stone weights that keep the route visually contained without becoming a wall.
- Lashing and hardware: oversized rawhide bindings, rope wraps, blackened iron straps, stolen scrap plates, and large peg blocks at key joins only.
- Blood Axe markers: restrained red cloth scraps, chipped red paint, horn stakes, broken shield shards, or small route warnings. Keep them sparse enough that the log rhythm remains primary.
- Mud contact: heavy trampled mud, soot-dark edges, ash streaks, and crushed footprints should be painted and shaped broadly.
- Optional raised crossing: a slight arch, ditch span, or mud-gap lift can be planned visually if needed, but no traversal angle, collision step, walkability, or path behavior is defined.

Use texture, normal maps, or material masks for:

- Wood grain and small cracks.
- Fine rope fibers.
- Tiny pegs, nails, chips, and axe marks.
- Soot speckles and ash streaks.
- Cloth weave and frayed fibers.
- Leather pores, stitch rows, and small cuts.
- Mud stains, damp lower edges, puddle tint, and grime gradients.
- Minor paint chips and scratched metal pitting.

Do not model:

- Dense per-log splinters, hundreds of nails, tiny rope fibers, small mud pebbles, complex puddle geometry, per-footprint meshes, gore piles, readable text, UI markers, path arrows, navigation helpers, snap sockets, spline handles, destructible fracture cuts, hidden gameplay objects, or interaction prompts.

Keep the mesh split-friendly where practical for future DCC judgment. Baseline `A01` can be one static mesh for package identity, but edge markers, red cloth, and optional route markers should be easy to remove or instance separately if a later approved composition needs fewer details. Do not choose that split, create source folders, or promote this package to a build target from this docs-only task.

## Texture and Material Notes

Required map families for future approved build:

- Base Color / Albedo (`BC`)
- Normal (`N`)
- Packed Occlusion/Roughness/Metallic (`ORM`)
- Optional Emissive (`E`) only for a separately approved torch, shamanic, magic route, or signal-state variant, not for baseline `A01`

Target material slot count:

- Slot 0: `MI_GIA_BloodAxeRoughTimber_A01` for split logs, crossbeams, side edging, stakes, and rough wood.
- Slot 1: `MI_GIA_BloodAxeMudAsh_A01` for packed mud, wet earth, soot, ash, and route shoulders.
- Slot 2: `MI_GIA_BloodAxeBlackenedIron_A01` or `MI_GIA_BloodAxeReforgedMetal_A01` for clamp plates, spikes, pegs, and stolen scrap, with red cloth and hide handled by atlas masks where practical.
- Optional shared accent within an existing atlas: `MI_GIA_BloodAxeScorchedHide_A01`, `MI_GIA_BloodAxeRedCloth_A01`, or `MI_GIA_BloodAxeBoneTrophy_A01` only if atlas packing cannot keep these accents readable.

Target 2 material slots, 3 maximum. Avoid one-off slots for each log, rope, clamp, cloth strip, mud patch, puddle, or marker.

Texture naming targets:

- `T_GIA_BloodAxeLogWalkway_A01_BC`
- `T_GIA_BloodAxeLogWalkway_A01_N`
- `T_GIA_BloodAxeLogWalkway_A01_ORM`
- Optional future `T_GIA_BloodAxeLogWalkway_A01_E` only after emissive approval

Texture resolution targets:

- Default walkway: 2K texture set.
- Far route dressing variant: 1K if the asset becomes repeated background camp dressing.
- Hero close-route variant: 2K, with 4K only if a later hero-environment approval justifies it.

Packed `ORM` guidance:

- R: strong baked AO between logs, under crossbeams, beneath lashings, under clamp plates, around mud shoulders, and under route markers.
- G: high roughness for charred wood, wet mud, soot, ash, hide, rope, and red cloth; varied medium-high roughness for blackened iron with brighter rubbed edges.
- B: metallic only for iron, steel, clamp plates, spikes, nails, peg caps, and stolen scrap.

Texture readability requirements:

- Maintain broad value separation between timber, mud, metal, hide, red cloth, and bone/horn accents.
- Paint soot, mud, and wear at Giant scale rather than as tiny speckles only.
- Keep red cloth broad but sparse so it signals Blood Axe without turning the route into a banner strip.
- Avoid readable text, faction UI symbols, loot-rarity color coding, nav color bands, interaction highlights, weak-point markings, or magical glow masks.

## Triangle Budget

`SM_GIA_BloodAxeLogWalkway_A01` is a large static route-dressing prop, not a building, tower, bridge system, or gameplay traversal object.

Target budget:

- LOD0 target: 5k-10k tris.
- LOD0 hard cap: 12k tris if the mud shoulders, side edging, cloth markers, and sparse horn or bone route markers stay in one mesh.
- Material slots: 2 target, 3 maximum.
- Texture resolution: 2K standard for baseline `A01`.

Budget distribution guidance:

- Main split logs and crossbeams: 50-60 percent.
- Mud shoulders, side edging, stakes, and stone weights: 18-25 percent.
- Lashings, clamp plates, red cloth, and large bindings: 12-18 percent.
- Sparse route markers, horn/bone accents, and optional broken shield details: 5-8 percent.

Do not spend geometry on tiny rope fibers, dense nails, small scratches, individual mud clumps, tiny puddle rims, fine splinters, dense trophy strings, many small chain links, cloth fray threads, or micro cracks.

## LOD Plan

All future implementations require LOD0-LOD3.

- LOD0: full log walkway silhouette, individual main logs, crossbeams, side edging, mud shoulders, large lashings, blackened iron plates, broad red cloth scraps, sparse horn/bone route markers, and broad contact grime.
- LOD1: 60-70 percent of LOD0; reduce log bevels, small end chips, secondary lashings, clamp bevels, minor cloth cuts, mud edge complexity, and small marker backs.
- LOD2: 35-45 percent of LOD0; merge log forms into larger groups, simplify side edging, flatten mud shoulders, reduce route markers, remove underside details, and simplify crossbeam cuts.
- LOD3: 15-25 percent of LOD0; preserve the long low route strip, broad log direction, Giant-scale width, raised side read, red marker read, and hostile camp silhouette.

LOD reduction order:

1. Tiny nails, stitches, scratches, edge nicks, wood grain cuts, rope fibers, and paint chips.
2. Small secondary lashings, leather knots, minor cloth holes, and small mud clumps.
3. Small horn chips, tooth fragments, broken shield chips, and non-silhouette tokens.
4. Back-side underside details, interior log spacing, and invisible crossbeam cuts.
5. Clamp bevels, log end chip complexity, and side-edge undercuts.
6. Optional raised-crossing underside detail.
7. Only after secondary detail is removed, simplify the primary log rhythm, Giant-scale width, route strip length, and red Blood Axe marker read.

Never reduce the broad log-walkway outline, Giant-scale route width, primary log direction, or hostile Blood Axe marker read before removing small detail.

## Collision Notes

This package plans collision intent only. It does not create collision proxies, custom UCX meshes, walkable collision implementation, nav links, physics assets, Unreal collision channels, or complex-as-simple collision.

Future collision planning, if separately approved:

- Baseline visual route dressing can use no collision or one simplified non-walkable bounds shape, depending on placement needs.
- If a later task approves physical blocking, use a few low-count boxes or convex hulls around the main log mass and side edging, not per-log collision.
- Mud shoulders should be non-blocking unless a future environment pass needs one broad terrain-overlap blocker.
- Stakes and large side markers can use simple merged blockers only when they are large enough to affect camera or traversal space.
- Cloth, lashings, ropes, small clamps, horn markers, bone markers, puddle details, small stones, and broken shield accents should have collision disabled by default.
- Any future walkable version must be treated as a separate approval-gated implementation task with explicit collision, traversal, and validation requirements.

No walkable collision implementation, navmesh, pathfinding behavior, AI lane, smart link, climb volume, ramp traversal, step-up tuning, cover volume, projectile blocker, damage zone, destructible hit shape, objective volume, player interaction volume, pickup collision, physics body, cloth collision, or combat trace is authorized here.

## Animation Notes

Baseline asset is static.

Approved for this docs-only package:

- Static mesh planning for logs, crossbeams, mud shoulders, side edging, fixed lashings, fixed red cloth scraps, and static route markers.
- Optional material-only dirt, wetness, soot, age, and red paint variation in future material instances.
- Static visual placement context for enemy-camp route composition, with no movement or interaction behavior.

Approval-gated future options:

- Cloth flutter, vertex wind, hanging marker sway, or rope movement.
- Signal fire, smoke, torchlight, shamanic route glow, or VFX state.
- Breakable logs, collapsing bridge behavior, loosened stakes, falling debris, or destructible states.
- Character traversal, AI patrol use, path following, player interaction, climb, ramp, or movement animation.

None of those options are authorized by this package. Any moving, walkable, interactive, destructible, AI-linked, or VFX-driven version should be split into a separately named asset or Blueprint package.

## Unreal Import Notes

This section is planning only. No Unreal Content asset, material instance, texture, Blueprint, collision proxy, validator, startup actor, import script, runtime source, source asset, or DCC export is created by this package.

Planned future Unreal asset:

- Asset name: `SM_GIA_BloodAxeLogWalkway_A01`
- Asset type: Static Mesh
- Planned folder: `/Game/Aerathea/Environment/Giants/BloodAxeCamp/Paths/`
- Alternate prop folder if camp route taxonomy changes: `/Game/Aerathea/Props/Giants/BloodAxeCamp/`
- Import scale: centimeter-authored source, import scale 1.0 after future DCC/export validation
- Pivot: ground-contact center of the visual footprint, with +Z up
- Forward orientation: primary route direction faces +X unless a future environment import convention specifies otherwise
- Collision type: none or simple generated primitive collision only after implementation approval; no walkable collision implementation is approved here
- LODs: LOD0, LOD1, LOD2, LOD3 required before production import approval
- Material slot count: 2 target, 3 maximum
- Texture set: 2K baseline `BC`, `N`, `ORM`; optional `E` only behind separate emissive approval
- Sockets: none required or approved for baseline static mesh
- Blueprint behavior: none
- Animation list: none
- Performance notes: keep as reusable static route dressing, avoid per-log material splits, keep repeated markers instance-friendly, and reduce small lashings, chips, and route markers before the primary log silhouette.

Potential future visual attachment markers, if separately approved:

- `route_marker_socket_l`
- `route_marker_socket_r`
- `cloth_warning_socket`
- `horn_marker_socket`
- `ash_clutter_socket`

These are visual attachment planning notes only. Do not author sockets, interaction hooks, VFX hooks, AI hooks, nav links, gameplay traces, snap connectors, walkable setup, terrain blending rules, or Blueprint behavior from this package.

Planned texture names:

- `T_GIA_BloodAxeLogWalkway_A01_BC`
- `T_GIA_BloodAxeLogWalkway_A01_N`
- `T_GIA_BloodAxeLogWalkway_A01_ORM`
- Optional future `T_GIA_BloodAxeLogWalkway_A01_E`

Planned material instances:

- `MI_GIA_BloodAxeLogWalkway_A01`
- Shared references as appropriate: `MI_GIA_BloodAxeRoughTimber_A01`, `MI_GIA_BloodAxeMudAsh_A01`, `MI_GIA_BloodAxeBlackenedIron_A01`, `MI_GIA_BloodAxeReforgedMetal_A01`, `MI_GIA_BloodAxeScorchedHide_A01`, `MI_GIA_BloodAxeRedCloth_A01`, and `MI_GIA_BloodAxeBoneTrophy_A01`

## Folder and Naming Recommendation

Docs:

- Package folder: `docs/assets/props/SM_GIA_BloodAxeLogWalkway_A01/`
- Package file: `docs/assets/props/SM_GIA_BloodAxeLogWalkway_A01/PRODUCTION_PACKAGE.md`

Planned future source/export paths, pending separate approval only:

- Source: `SourceAssets/Blender/Props/Giants/BloodAxeCamp/SM_GIA_BloodAxeLogWalkway_A01/`
- Export: `SourceAssets/Exports/Props/Giants/BloodAxeCamp/SM_GIA_BloodAxeLogWalkway_A01.fbx`
- Unreal: `/Game/Aerathea/Environment/Giants/BloodAxeCamp/Paths/`

Naming:

- Static mesh: `SM_GIA_BloodAxeLogWalkway_A01`
- Material instance: `MI_GIA_BloodAxeLogWalkway_A01`
- Textures: `T_GIA_BloodAxeLogWalkway_A01_BC`, `T_GIA_BloodAxeLogWalkway_A01_N`, `T_GIA_BloodAxeLogWalkway_A01_ORM`
- Optional emissive texture, if separately approved: `T_GIA_BloodAxeLogWalkway_A01_E`
- Related but separate path assets: `SM_GIA_BloodAxePackedEarthPath_A01` and `KIT_GIA_BloodAxePathMarkers_A01`
- Related but separate barricade candidates: `SM_GIA_BloodAxeStakeBarricade_A01`, `SM_GIA_BloodAxeScrapShieldBarricade_A01`, and `SM_GIA_BloodAxeChainedPlateBarricade_A01`

Related docs:

- `docs/assets/kits/KIT_GIA_BloodAxeCamp_A01/PRODUCTION_PACKAGE.md`
- `docs/assets/kits/KIT_GIA_BloodAxeCamp_A01/CHILD_ASSET_INTAKE.md`
- `docs/assets/props/SM_GIA_BloodAxeWatchPlatform_A01/PRODUCTION_PACKAGE.md`
- `docs/assets/props/SM_GIA_BloodAxeCampGate_A01/PRODUCTION_PACKAGE.md`
- `docs/assets/kits/KIT_GIA_BloodAxeStrongholdApproach_A01/PRODUCTION_PACKAGE.md`

Do not add SourceAssets folders, Blender files, sculpt files, retopo files, UVs, bakes, collision proxies, FBX exports, Unreal Content assets, material graphs, Blueprints, runtime source, tools, validators, startup-scene actors, copied source concepts, global index entries, task-board edits, backlog edits, bootstrap edits, final approval captures, or external concept-folder edits from this task.

## Stop Gates

- Stop before creating DCC source, Blender files, proof renders, sculpt files, retopo files, UVs, bakes, LOD source meshes, collision proxy meshes, FBX exports, Unreal imports, material graphs, Blueprints, runtime source, tools, validators, startup placements, or global documentation updates.
- Stop before copying, moving, cropping, editing, embedding, inspecting for final approval, or committing external source concept images.
- Stop before selecting this asset as a first DCC target, first playable visual target, or final visual approval target.
- Stop before defining walkable collision implementation, character traversal, AI traversal, player step height, movement friction, ramp rules, bridge rules, path width, route scoring, navmesh use, pathfinding behavior, smart links, spline paths, or patrol lanes.
- Stop before defining modular snapping, snap sockets, connector transforms, path-grid rules, terrain blending implementation, spline placement tools, auto-layout tools, or runtime path assembly.
- Stop before defining destructible behavior, collapsing logs, breakable bridge states, physics simulation, falling debris, damage volumes, trap behavior, fire spread, repair states, or objective logic.
- Stop before adding interaction prompts, pickup rules, loot/resource/crafting/salvage behavior, camp capture behavior, economy rules, or usable workstation behavior.
- Stop before adding default emissive, ritual glow, shamanic glow, torch VFX, smoke VFX, faction aura, cloth simulation, wind animation, physics bodies, hanging-marker sway, or animated material states.
- Stop if the design starts using neutral/civilized Giant culture as the primary identity: blue-gray carved masonry, cave-town civic pride, warm hearth halls, restrained blue runes, refined stonework, waterworks, terraces, or peaceful highland clan banners.
- Stop if any future scale review requires changing the validated Giant scale lock: female baseline 442 cm / 14'6", male baseline 470 cm / 15'5", approved range females 14-15 ft / 427-457 cm and males 14'10"-16'0" / 452-488 cm.
- Stop if material count exceeds 3 slots or LOD0 exceeds 12k tris without explicit hero route-dressing approval.

## Quality Gate Checklist

- Package is docs-only and touches only `docs/assets/props/SM_GIA_BloodAxeLogWalkway_A01/PRODUCTION_PACKAGE.md`.
- `SM_GIA_BloodAxeLogWalkway_A01` is a hostile Blood Axe Giant route-dressing prop, not a neutral/civilized Giant structure.
- Blood Axe remains a hostile Giant sub-faction, separate from neutral/civilized Giant culture.
- Blood Axe red-black raider language stays separate from neutral/civilized Giant stoneworker, cave-town, hearth, terrace, waterwork, highland nomad, and restrained rune culture.
- Giant scale lock is explicit and unchanged: female baseline 442 cm / 14'6" and male baseline 470 cm / 15'5", with approved ranges females 14-15 ft / 427-457 cm and males 14'10"-16'0" / 452-488 cm.
- Gameplay purpose is limited to static visual route dressing and scale planning.
- Route readability is visual only; no navmesh, pathfinding, AI lane, patrol route, movement logic, step-up tuning, spline path, or traversal rule is defined.
- Walkable collision implementation is explicitly out of scope.
- Modular snapping, snap connectors, terrain blending implementation, and path-grid behavior are explicitly out of scope.
- Destructible behavior, physics simulation, collapse states, damage volumes, and trap behavior are explicitly out of scope.
- Primary silhouette reads at MMO distance: broad split-log route strip, Giant-scale width, crossbeams, mud shoulders, side edging, crude lashings, red Blood Axe warning scraps, and rough camp construction.
- Materials align with raw timber, charred wood, packed mud, soot, ash, blackened iron, reforged metal, hide lashings, rough rope, dull red cloth, grime, and sparse aged bone/horn markers.
- Neutral/civilized Giant blue-gray stonecraft, warm hearth identity, terrace/waterwork language, clean masonry, and restrained blue rune motifs are excluded from the baseline.
- Default emissive, magical glow, signal fire, VFX, faction aura, animated material states, cloth simulation, physics, destructibility, walkability, and final socket transforms are not claimed.
- Texture maps include `BC`, `N`, `ORM`, and optional future `E` only behind approval.
- Triangle budget, material slot target, LOD0-LOD3 plan, collision planning, animation scope, Unreal import planning, folder naming, stop gates, and quality checklist are included.
- Tiny lashings, scratches, rope fibers, wood grain, stitch detail, ash flecks, small nails, small chips, cloth weave, metal pitting, mud flecks, and grime are assigned to textures or normals instead of geometry.
- Collision remains simple future planning only, with no collision proxy creation, walkable setup, per-log collision, per-rope collision, per-cloth collision, per-marker collision, navmesh rules, or gameplay collision claims.
- Source concepts remain external and are not copied, moved, edited, embedded, cropped, inspected for final approval, or committed.
- Package makes no DCC, FBX, Unreal Content, runtime source, validator, startup-scene, source asset, material graph, final visual approval, first DCC target selection, global index edit, task-board edit, backlog edit, bootstrap edit, or external concept-folder edit claim.
