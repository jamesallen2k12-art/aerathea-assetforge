# SM_GIA_BloodAxeStakeWatchTower_A01 Production Package

## Art Direction Summary

- Asset name: `SM_GIA_BloodAxeStakeWatchTower_A01`
- Asset type: Static Mesh production package / hostile Blood Axe Giant temporary stake watch tower prop
- Task: `AET-MA-20260629-119`
- Parent kit: `KIT_GIA_BloodAxeCamp_A01`
- Source child ID: `BloodAxecamp.png#Watch_StakeTower`
- Related visual dependencies: `SM_GIA_BloodAxeWatchPlatform_A01`, `SM_GIA_BloodAxeCampGate_A01`, `SM_GIA_BloodAxeTrophyGate_A01`, `SK_GIA_BloodAxeCampSentry_A01`, `SM_GIA_BloodAxeWarBanner_A01`, and shared Blood Axe material families
- Faction/theme: Blood Axe Tribe, hostile Giant sub-faction only
- Status: docs-only static visual production package ready for planning review
- Source-storage guardrail: source concepts remain external through existing intake records. Do not copy, move, crop, edit, embed, inspect for final approval, or commit source images from this package.

`SM_GIA_BloodAxeStakeWatchTower_A01` defines a taller perimeter stake-tower variant for hostile Blood Axe Giant camps. It should read as crude, temporary, territorial, and unsafe by civilized standards: towering sharpened trunks, lashed stake bundles, a heavy elevated lookout deck, rough cross-bracing, partial Giant-height rails, red warning cloth, blackened iron clamps, hide lashings, mud-packed feet, stone weights, and sparse non-graphic horn or bone markers.

This tower is not neutral or civilized Giant architecture. Do not use carved blue-gray master stonework, orderly hidden cave-town masonry, warm civic hearth language, refined terraces, waterworks, peaceful highland clan motifs, or restrained blue rune identity. Blood Axe is a hostile raider sub-faction and must stay visually separate from normal Giant culture.

This package is static visual planning only. It does not authorize DCC source creation, source asset creation, FBX export, Unreal Content creation, material graph authoring, collision proxy creation, startup placement, final visual approval, first build target selection, climb behavior, ladder behavior, ramp traversal, nav behavior, AI sightline behavior, destructible behavior, interaction behavior, encounter logic, VFX, audio, or source concept movement.

## Gameplay Purpose

The purpose is visual role planning only: give Blood Axe camp perimeters a taller, more threatening vertical silhouette than the lower raised watch platform while staying temporary and raider-built.

Allowed planning uses:

- Establish a high perimeter marker for Blood Axe camp borders, palisade corners, gate approaches, and ridge-side camp compositions.
- Support static visual context for `SK_GIA_BloodAxeCampSentry_A01` without defining patrol, lookout, or perception behavior.
- Reinforce hostile territory read through height, sharpened stakes, red cloth, blackened iron, soot, mud, and rough Giant-scale construction.
- Provide scale, material, LOD, collision, and future import planning for later approval-gated DCC or Unreal work.

Out of scope:

- Climb logic, ladder use, ramp traversal, navmesh links, smart links, walkable implementation, AI perception, sight cones, line-of-sight tests, patrol routes, spawn rules, sentry behavior, cover behavior, encounter scripting, objective behavior, interaction prompts, destructibility, damage states, fire spread, trap behavior, loot, crafting, salvage, resource collection, economy, audio, VFX, startup placement, source concept handling, final visual approval, or first DCC target selection.

## Silhouette Notes

Primary silhouette: a tall, narrow-to-broad Giant-scale stake watch tower made from oversized sharpened trunks, with a rough elevated deck or crow's-nest-like platform lashed into the upper third. It should read from a distance as a brutal temporary perimeter tower, not a polished fortress tower or neutral Giant stone lookout.

Silhouette goals:

- Use six to ten massive uneven stake trunks or split logs, leaning slightly inward or outward to create an unstable raider-built profile.
- Keep the top profile jagged with blunt-chopped and sharpened stake tips, but avoid a dense forest of tiny spikes.
- Place the main deck high enough to read as a perimeter watch tower, with a heavy plank floor and underside brace mass visible from below.
- Add bold diagonal braces and X-braces on the exterior faces; use a few large structural strokes rather than dense scaffolding.
- Use partial Giant-height rails around the deck, broken or uneven in silhouette, but clear enough to read as a lookout edge.
- Include one strong Blood Axe signal element: a torn red vertical banner, warning cloth strip, horn marker, or compact signal pole.
- Keep the base planted with mud-packed feet, rough stone weights, driven side stakes, or blackened iron collars.
- Allow ladder-like notched logs or steep ramp-like plank shapes only as static construction silhouettes if concept art requires them. They must not imply approved climb, traversal, or nav behavior.
- Use sparse bone, horn, broken shield, or old weapon markers as territory accents. Avoid graphic gore, fresh remains, trophy curtains, dense skull clutter, or many tiny dangling charms.
- Keep any deck dressing minimal and separable: a warning horn, coil, crate, weapon rest, or signal drum may be planned as visual dressing, but should not blur the tower silhouette.

Model real geometry for the primary stake trunks, deck frame, thick planks, major braces, rail logs, signal pole, broad red cloth, large clamps, major lashings, base stones, and sparse trophy markers. Use textures, normal maps, and AO for wood grain, fine cracks, rope fibers, small nail heads, soot streaks, mud flecks, cloth weave, leather pores, tiny scratches, and minor metal pitting.

## Scale Notes

Use the validated `SK_GIA_Base_A01` scale lock without alteration:

- Female Giant baseline: 442 cm / 14'6".
- Male Giant baseline: 470 cm / 15'5".
- Approved Giant ranges: females 14-15 ft / 427-457 cm; males 14'10"-16'0" / 452-488 cm.
- Author future source in centimeters. 1 Unreal unit = 1 cm.
- Normal humanoid compatibility is not required. Smallfolk should read as trespassers around an oversized hostile Giant structure.

Recommended static scale targets:

- Overall tower height: 1150-1550 cm from ground to top stake or banner tip.
- Main deck height above ground: 760-1050 cm, taller than `SM_GIA_BloodAxeWatchPlatform_A01` while staying camp-temporary rather than stronghold-scale.
- Deck footprint: 620-900 cm wide by 520-820 cm deep.
- Clear standing zone on deck: at least 500 cm vertical clearance above deck if any overhead signal beam, roof scrap, or trophy arch is included.
- Rail height: 185-250 cm from deck surface, roughly Giant waist to lower-chest height.
- Main stake or support diameter: 55-110 cm, irregular and rough-hewn.
- Secondary brace diameter: 30-65 cm or equivalent split-beam mass.
- Deck plank width: 75-150 cm, with visible Giant-scale plank spacing and uneven edges.
- Base footprint: 850-1300 cm wide by 750-1150 cm deep including angled supports, side stakes, stone weights, and mud-packed feet.
- Signal pole height: 250-450 cm above deck if mounted high, or up to 1650 cm total world height if it extends from ground.
- Red cloth signal panel: 150-300 cm wide by 220-420 cm tall, sized for perimeter read.
- Optional visual-only notched-log or ladder-like shape: oversized for Giant construction language, with no rung-spacing, traversal angle, climb volume, or nav approval.

Perimeter readability is visual only:

- The height, stake tips, red cloth, and upper deck should communicate "hostile watch tower" from camp approach angles.
- Do not encode AI perception, sight cones, player visibility rules, ranged attack advantage, cover tagging, or gameplay sightline volumes into this asset plan.
- The tower may frame a Giant sentry silhouette in a later approval-gated composition, but this package does not place, animate, or behavior-author any sentry.

## Materials and Color Palette

Primary materials:

- Raw dark timber, split trunks, sharpened stakes, charred logs, rough deck planks, and crude crossbeams.
- Hide lashings, sinew wraps, heavy rope, scorched leather pads, and rawhide repair strips.
- Blackened iron, dark steel, rough reforged plates, wide clamp bands, spike collars, short heavy chain loops, and stolen scrap braces.
- Packed mud, soot, ash, trampled earth, charcoal dust, and damp grime around the base.
- Rough field stone, crude base weights, and cairn-like stabilizers used as raider utility rather than civilized masonry.
- Torn Blood Axe red cloth, dirty red paint, and warning strips as hostile sub-faction identifiers.
- Bone, horn, broken shield fragments, teeth, or old weapon pieces used sparsely and non-graphically.

Suggested palette:

- Charred timber: `#1A1510` to `#3A2618`
- Weathered raw wood: `#5B412D` to `#8A6A45`
- Blackened iron: `#141619` to `#2E3031`
- Dark reforged steel: `#54585A` to `#797A76`
- Blood Axe red cloth: `#5A1412` to `#8A211A`
- Scorched leather and hide: `#241611` to `#5B3A27`
- Bone and horn accents: `#A69578` to `#D0B98C`
- Soot, ash, and mud: `#0B0A09` to `#4A3A2B`

No default emissive is approved. Signal fire, warning lamp, shamanic glow, faction aura, VFX pulse, magic marker states, and animated material states require a separate approval-gated package.

## Concept Image Prompt

Create an original stylized fantasy MMORPG concept image of `SM_GIA_BloodAxeStakeWatchTower_A01` for the world of Aerathea. The design should emphasize a hostile Blood Axe Giant temporary stake watch tower silhouette, validated Giant scale with female baseline 442 cm / 14'6" and male baseline 470 cm / 15'5", towering sharpened raw-log stakes, a high rough lookout deck, heavy uneven planks, crude diagonal cross-bracing, Giant-height partial rails, mud-packed base feet, rough stone weights, blackened iron clamp bands, hide lashings, heavy rope, soot, ash, mud, sparse non-graphic bone or horn territory markers, torn Blood Axe red warning cloth, hostile raider sub-faction identity, perimeter readability, and a gameplay role limited to static hostile camp environment planning. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, no default emissive glow, and MMO-friendly mid-poly production design. Present it as a static prop concept sheet with front, side, back, top-down footprint, deck-height callout, base footprint callout, material swatches, LOD planning notes, simple collision intent callouts, and scale markers beside a 442 cm female Giant and a 470 cm male Giant on a clean background or simple Blood Axe camp perimeter context. Avoid copying any existing franchise, avoid making Blood Axe language the default Giant culture, avoid graphic gore, avoid AI sight cones, avoid patrol diagrams, avoid climb or ladder diagrams, avoid navmesh diagrams, avoid interaction or destructible behavior callouts, avoid final visual approval claims, and avoid excessive micro-detail that would not translate to a mid-poly Unreal asset.

Source reference note: use `BloodAxecamp.png#Watch_StakeTower` only as an intake route reference. This docs-only package does not copy, move, inspect for final approval, crop, embed, edit, or commit external source concept imagery.

## Modeling Notes

This is a docs-only modeling plan. No mesh, Blender source, sculpt, retopo, UV, bake, proof render, collision proxy, LOD source, FBX export, Unreal asset, material graph, validator, startup placement, source asset, or final visual approval is created or approved by this package.

Future modeling should build large readable forms first:

- Main stake cluster: six to ten Giant-scale trunks with varied thickness, rough bark breaks, chopped or sharpened tops, and large silhouette chips. Keep the stakes readable as structural supports, not decorative toothpicks.
- Deck frame: broad upper frame beams, thick uneven planks, underside bearers, and overhanging rough edges sized for Giant feet and weight.
- Exterior bracing: a few large diagonal braces or X braces on key faces, with visible load path from deck to base.
- Rails: broken partial rail segments built from thick logs and lashed verticals. Preserve the lookout edge read without making a dense fence.
- Base stabilization: mud-packed feet, driven ground stakes, rough field stones, blackened iron collars, log chocks, or crude side anchors. Use broad base shapes that read at MMO camera distance.
- Signal element: torn red cloth, compact warning banner, horn marker, or tall signal pole that references Blood Axe banner language without turning this package into a banner asset.
- Sparse territory dressing: one to three major horn, bone, broken shield, old weapon, or warning-token accents. Keep them dry, aged, non-graphic, and readable.
- Deck dressing: optional static horn, rope coil, crate, weapon rest, or warning drum should remain separate or easily removable in future DCC work. Do not bake gameplay props into the main mesh unless later approved.
- Optional access silhouette: a notched support log, ladder-like slats, or steep ramp-like plank mass may be blocked in visually only. Do not define rung spacing, traversal angle, climb volumes, navmesh use, smart links, or interaction logic.

Use texture, normal maps, or material masks for:

- Wood grain and small cracks.
- Fine rope fibers.
- Tiny rivets, pegs, nails, and chips.
- Soot speckles and ash streaks.
- Cloth weave and frayed fibers.
- Leather pores, stitch rows, and small cuts.
- Mud stains, damp lower edges, and grime gradients.
- Minor paint chips and scratched metal pitting.

The default `A01` should be planned as one static mesh for package identity, but the future DCC worker may split posts, deck, signal cloth, and removable deck dressing only after a separate implementation task approves that breakdown. Do not collapse adjacent palisades, sentries, gates, paths, barricades, shelters, or camp clutter into this tower mesh.

## Texture and Material Notes

Required map families for a future approved build:

- Base Color / Albedo (`BC`)
- Normal (`N`)
- Packed Occlusion/Roughness/Metallic (`ORM`)
- Optional Emissive (`E`) only for a separately approved signal-fire, shamanic, lamp, or faction-state variant, not for baseline `A01`

Target material slot count:

- Slot 0: `MI_GIA_BloodAxeRoughTimber_A01` for stake trunks, deck, braces, rails, and rough wood.
- Slot 1: `MI_GIA_BloodAxeBlackenedIron_A01` or `MI_GIA_BloodAxeReforgedMetal_A01` for clamps, collars, plates, nails, short chain loops, and stolen scrap braces.
- Slot 2: `MI_GIA_BloodAxeScorchedHide_A01` for hide lashings, rope, leather wraps, sinew ties, and rawhide repairs.
- Slot 3: `MI_GIA_BloodAxeRedCloth_A01` for warning cloth, signal strips, and banner panels.
- Optional shared accent within an existing atlas: `MI_GIA_BloodAxeBoneTrophy_A01` if bone, horn, or trophy accents cannot be handled in the timber or hide atlas.

Target 3 material slots, 4 maximum. Avoid one-off slots for each post, rope, clamp, trophy, cloth strip, mud patch, deck plank, or base stone.

Texture naming targets:

- `T_GIA_BloodAxeStakeWatchTower_A01_BC`
- `T_GIA_BloodAxeStakeWatchTower_A01_N`
- `T_GIA_BloodAxeStakeWatchTower_A01_ORM`
- Optional future `T_GIA_BloodAxeStakeWatchTower_A01_E` only after emissive approval

Texture resolution targets:

- Baseline tower: 2K texture set.
- Hero close-route perimeter variant: 2K with shared trim support; 4K only if a later hero environment approval justifies it.
- Far camp silhouette or HLOD variant: 1K or shared atlas after simplification.

Packed `ORM` guidance:

- R: Strong baked AO under deck planks, brace intersections, rail overlaps, lashings, clamp plates, base stones, post collars, and ground-contact mud.
- G: High roughness for charred wood, hide, rope, soot, mud, ash, and red cloth; varied medium-high roughness for blackened iron with slightly brighter rubbed edges.
- B: Metallic only for iron, steel, clamp bands, collars, plates, nails, short chains, and stolen scrap braces.

Texture readability requirements:

- Maintain broad value separation between wood, red cloth, blackened metal, hide, bone, and mud.
- Paint soot, grime, edge wear, and mud at Giant scale rather than as tiny noise only.
- Keep red cloth broad but sparse so it signals Blood Axe territory without making the whole prop red.
- Avoid readable text, neutral Giant civic symbols, loot-rarity color coding, alert-state colors, weak-point markings, magical glow masks, or source-concept overlays.

## Triangle Budget

`SM_GIA_BloodAxeStakeWatchTower_A01` is a tall large static camp prop. It should be heavier than a low watch platform but lighter and more temporary than a fortified tower or stronghold module.

Target budget:

- LOD0 target: 18k-28k tris.
- LOD0 hard cap: 32k tris if the signal element, base weights, partial rails, and sparse territory accents remain in the same mesh.
- Material slots: 3 target, 4 maximum.
- Texture resolution: 2K standard for baseline `A01`.

Budget distribution guidance:

- Main stake trunks, deck frame, thick planks, and underside support: 45-55 percent.
- Exterior braces, partial rails, base stabilization, and mud/stone anchors: 22-30 percent.
- Signal pole, red cloth, clamp bands, lashings, and large bindings: 12-18 percent.
- Sparse trophies, deck dressing, base dressing, and accent props: 5-10 percent.

Do not spend geometry on tiny rope fibers, dense nails, fine splinters, individual mud clumps, cloth fray threads, tiny trophy strings, many small chain links, dense cracks, or micro scratches.

## LOD Plan

All future implementations require LOD0-LOD3.

- LOD0: full tower silhouette, tall stake cluster, deck planks, underside frame, exterior braces, partial rails, base stabilization, signal pole, broad red cloth, major clamps, large lashings, and sparse territory markers.
- LOD1: 60-70 percent of LOD0; reduce plank bevels, minor post chips, secondary lashings, small clamp bevels, rail undercuts, cloth edge cuts, and deck dressing backs.
- LOD2: 35-45 percent of LOD0; simplify deck planks into larger groups, reduce rail interiors, flatten small brace cuts, merge base details, simplify trophy accents, and remove most underside detail that does not support the silhouette.
- LOD3: 15-25 percent of LOD0; preserve the tall stake-tower mass, jagged top read, upper deck block, diagonal brace read, rail line, red signal cloth, and overall perimeter height.

LOD reduction order:

1. Tiny nails, stitches, scratches, edge nicks, wood grain cuts, rope fibers, and paint chips.
2. Small secondary lashings, leather knots, tiny chain segments, and minor cloth holes.
3. Small trophy chips, tooth fragments, and non-silhouette tokens.
4. Back-side deck dressing, underside clutter, interior plank spacing, and hidden base dressing.
5. Clamp bevels, post chip complexity, rail undercuts, and optional visual-only access silhouette detail.
6. Only after secondary detail is removed, simplify the main stake height, deck mass, rail line, cross-brace read, jagged top profile, and red signal cloth.

Never reduce the tower height read, Giant-scale deck height, primary stake mass, jagged perimeter silhouette, red signal read, or Blood Axe camp-warning identity before removing small detail.

## Collision Notes

This package plans collision intent only. It does not create collision proxies, custom UCX meshes, physics assets, Unreal collision channels, walkable setup, nav links, climb volumes, interaction volumes, AI sight volumes, cover volumes, damage volumes, or validation scripts.

Future collision planning:

- Main support cluster: simple boxes or low-count convex hulls around the post groups, not per-splinter or per-lashing collision.
- Deck: one simple blocking box or convex hull for the deck mass only if a future implementation task approves the tower as walkable. If not walkable, collision can remain simplified around the overall prop bounds.
- Rails: simple rail boxes only if later placement requires blocking. Do not create per-board, per-gap, or per-rail collision.
- Base weights, stones, and side stakes: simple low-count hulls or merged base blockers if they affect traversal.
- Signal pole: simple pole capsule or box if needed. Cloth collision disabled by default.
- Trophy accents, rope, lashings, loose cloth, small chains, and deck dressing: collision disabled by default unless a later implementation task identifies a large blocking shape.
- Optional ladder-like, notched-log, or ramp-like silhouettes: collision disabled or simplified as static prop obstruction only.

No climb collision, ladder volumes, ramp traversal, smart links, navmesh rules, AI sight volumes, perception blockers, cover tags, projectile blockers, damage zones, destructible hit shapes, objective volumes, player interaction volumes, pickup collision, physics bodies, cloth collision, or combat traces are authorized here.

## Animation Notes

Baseline asset is static.

Approved for this docs-only package:

- Static mesh planning for stake trunks, deck, rails, braces, base anchors, signal pole, and fixed red cloth.
- Optional future material-only dirt, mud, soot, or paint variation in material instances.
- Static visual placement context for a future sentry, with no character, patrol, AI, or gameplay behavior.

Approval-gated future options:

- Banner cloth simulation or vertex wind.
- Hanging marker sway.
- Signal fire, smoke, lamp, horn, or VFX state.
- Breakable stakes, destructible tower, falling debris, damaged-state variants, or collapse states.
- Character climb, ladder use, ramp traversal, sentry idle, patrol, lookout animation, interaction sequence, or AI behavior.

None of those options are authorized by this package. Any moving, interactive, destructible, climbable, walkable, or AI-linked version must be split into a separately approved asset or Blueprint package.

## Unreal Import Notes

This section is future import planning only. No Unreal Content asset, material instance, texture, collision proxy, socket, Blueprint, validator, runtime source, startup actor, source asset, DCC export, or import script is created by this package.

Planned future Unreal asset:

- Asset name: `SM_GIA_BloodAxeStakeWatchTower_A01`
- Asset type: Static Mesh
- Planned folder: `/Game/Aerathea/Environment/Giants/BloodAxeCamp/Structures/`
- Alternate prop folder if camp structure taxonomy changes: `/Game/Aerathea/Props/Giants/BloodAxeCamp/`
- Materials folder: `/Game/Aerathea/Materials/Giants/BloodAxe/`
- Textures folder: `/Game/Aerathea/Textures/Giants/BloodAxe/Camp/`
- Import scale: centimeter-authored source, Unreal import scale 1.0 after future DCC/export validation
- Pivot: ground-contact center beneath the tower base footprint, with +Z up
- Forward orientation: primary approach/read face and red signal cloth toward +X unless a later project import convention overrides it
- Bounds: include top stakes, signal cloth, upper deck, and base anchors in visual bounds
- Collision type: simple custom collision or generated primitive collision only after implementation approval
- LODs: LOD0, LOD1, LOD2, LOD3 required before any production import approval
- Material slot count: 3 target, 4 maximum
- Texture list: `T_GIA_BloodAxeStakeWatchTower_A01_BC`, `T_GIA_BloodAxeStakeWatchTower_A01_N`, `T_GIA_BloodAxeStakeWatchTower_A01_ORM`
- Optional texture: `T_GIA_BloodAxeStakeWatchTower_A01_E` only for a separately approved emissive variant
- Sockets: none required or authored for baseline static mesh
- Animation list: none
- Blueprint behavior: none
- Performance notes: preserve height, stake silhouette, deck block, brace read, and red signal cloth; reduce small lashings, trophies, chain detail, cloth cuts, and underside detail before reducing primary tower mass.

Candidate future visual-only markers, if a later task approves modular attachments:

- `watch_signal_socket`
- `banner_socket`
- `hanging_trophy_socket`
- `horn_marker_socket`
- `torch_socket`
- `deck_dressing_socket`

These are planning notes only. Do not author sockets, attachment transforms, VFX hooks, torch behavior, gameplay links, climb hooks, nav links, AI hooks, interaction hooks, trace points, Blueprint behavior, or startup placement from this package.

## Folder and Naming Recommendation

Docs:

- Package folder: `docs/assets/props/SM_GIA_BloodAxeStakeWatchTower_A01/`
- Package file: `docs/assets/props/SM_GIA_BloodAxeStakeWatchTower_A01/PRODUCTION_PACKAGE.md`

Related docs:

- Parent camp package: `docs/assets/kits/KIT_GIA_BloodAxeCamp_A01/PRODUCTION_PACKAGE.md`
- Parent camp child intake: `docs/assets/kits/KIT_GIA_BloodAxeCamp_A01/CHILD_ASSET_INTAKE.md`
- Related watch platform package: `docs/assets/props/SM_GIA_BloodAxeWatchPlatform_A01/PRODUCTION_PACKAGE.md`
- Related camp gate package: `docs/assets/props/SM_GIA_BloodAxeCampGate_A01/PRODUCTION_PACKAGE.md`
- Related trophy gate package: `docs/assets/props/SM_GIA_BloodAxeTrophyGate_A01/PRODUCTION_PACKAGE.md`
- Related sentry package: `docs/assets/characters/SK_GIA_BloodAxeCampSentry_A01/PRODUCTION_PACKAGE.md`

Future source/export paths, pending separate approval only:

- Source: `SourceAssets/Blender/Props/Giants/BloodAxeCamp/SM_GIA_BloodAxeStakeWatchTower_A01/`
- Export: `SourceAssets/Exports/Props/Giants/BloodAxeCamp/SM_GIA_BloodAxeStakeWatchTower_A01.fbx`
- Unreal: `/Game/Aerathea/Environment/Giants/BloodAxeCamp/Structures/`

Naming:

- Static mesh: `SM_GIA_BloodAxeStakeWatchTower_A01`
- Material instance: `MI_GIA_BloodAxeStakeWatchTower_A01`
- Shared material references: `MI_GIA_BloodAxeRoughTimber_A01`, `MI_GIA_BloodAxeBlackenedIron_A01`, `MI_GIA_BloodAxeReforgedMetal_A01`, `MI_GIA_BloodAxeScorchedHide_A01`, `MI_GIA_BloodAxeRedCloth_A01`, `MI_GIA_BloodAxeBoneTrophy_A01`, and `MI_GIA_BloodAxeSootAsh_A01`
- Textures: `T_GIA_BloodAxeStakeWatchTower_A01_BC`, `T_GIA_BloodAxeStakeWatchTower_A01_N`, `T_GIA_BloodAxeStakeWatchTower_A01_ORM`
- Optional future emissive texture, if separately approved: `T_GIA_BloodAxeStakeWatchTower_A01_E`
- Related but separate watch assets: `SM_GIA_BloodAxeWatchPlatform_A01` and future `SM_GIA_BloodAxeGateLookout_A01`

Do not add SourceAssets folders, Blender files, sculpt files, retopo files, UV files, bake outputs, proof renders, collision proxy files, FBX exports, Unreal Content assets, material graphs, Blueprints, runtime source, tools, validators, startup-scene actors, copied source concepts, embedded concept images, global index entries, task-board edits, backlog edits, bootstrap edits, final approval captures, or external concept-folder edits from this task.

## Approval Gates and Stop Points

- Lead approval is required before `SM_GIA_BloodAxeStakeWatchTower_A01` is selected as a first DCC target.
- Visual approval is required before final tower height, deck height, base footprint, rail density, stake angle, signal cloth placement, trophy density, access-shape read, or camp perimeter composition role is locked.
- Culture approval is required if Blood Axe raider language starts bleeding into neutral/civilized Giant packages.
- DCC approval is required before creating source folders, Blender sources, sculpt files, retopo files, UVs, bakes, proof renders, collision proxies, LOD sources, or exports.
- Unreal approval is required before importing static meshes, material instances, textures, LODs, collision, sockets, validators, Blueprints, or startup-scene actors.
- Collision approval is required before authoring custom collision, walkable deck setup, rail blocking, base hulls, or tower blockers.
- Cloth and physics approval is required before adding cloth simulation, vertex wind, hanging-marker sway, destructible parts, physics bodies, moving cloth, or collapse states.
- Gameplay approval is required before any climb behavior, ladder use, ramp traversal, navmesh rules, smart links, AI sightline behavior, perception ranges, patrol posts, cover rules, combat behavior, projectile blocking, encounter scripting, spawn rules, guard-post interactions, loot rules, trap behavior, objective logic, destructibility, camp capture, resource behavior, crafting behavior, salvage behavior, or interactable behavior.
- Source-storage approval is required before copying, embedding, editing, moving, cropping, inspecting for final visual approval, or committing any external source concept.

Stop immediately before:

- Any DCC, FBX, Unreal, source asset, runtime source, validator, material graph, Blueprint, startup placement, or source concept work.
- Final visual approval, first playable visual approval, or first build target selection.
- Any collision proxy creation, UCX mesh work, walkable tower implementation, climb/ramp/ladder/nav setup, or AI sightline implementation.
- Any socket authoring, VFX hook, interaction hook, gameplay trace, cover volume, objective volume, guard-post marker, or encounter logic.
- Any patrol, AI, aggro, spawn, combat, projectile, loot, economy, crafting, interaction, resource, salvage, destructible, collapse, or objective definition.
- Any change to the validated `SK_GIA_Base_A01` scale lock or Giant race range.
- Any shift that makes Blood Axe red-black raider language the default Giant culture.
- Any increase in stakes, trophies, skulls, red cloth, chains, straps, rivets, cracks, scratches, gore, deck clutter, or scaffold density that hurts mid-poly MMO readability.

## Quality Gate Checklist

- Package is docs-only and changes no DCC, FBX, Unreal Content, runtime source, startup scene, source asset, external concept, validator, global index, task board, backlog, bootstrap, or other package file.
- `SM_GIA_BloodAxeStakeWatchTower_A01` is a hostile Blood Axe Giant camp prop, not a neutral/civilized Giant structure.
- Blood Axe remains a hostile Giant sub-faction and does not replace neutral/civilized Giant culture.
- Giant scale lock is explicit and unchanged: female baseline 442 cm / 14'6" and male baseline 470 cm / 15'5", with approved ranges females 14-15 ft / 427-457 cm and males 14'10"-16'0" / 452-488 cm.
- Gameplay purpose is limited to static visual environment planning.
- Perimeter and sightline readability are described as visual only; no AI sight cones, perception ranges, patrol logic, cover behavior, or encounter scripting are defined.
- Climb, ladder, ramp, traversal, nav, interaction, and destructible behavior are explicitly out of scope.
- Primary silhouette reads at MMO distance: tall stake cluster, jagged top profile, high deck, exterior braces, partial rails, base anchors, and red signal cloth.
- Giant clearance and scale notes include tower height, deck height, deck footprint, rail height, support diameter, base footprint, and signal cloth dimensions.
- Materials align with raw timber, charred wood, blackened iron, reforged metal, hide lashings, rough rope, dull red cloth, soot, ash, mud, grime, and sparse aged bone/horn trophies.
- Neutral/civilized Giant stoneworker materials, blue-gray cave-town identity, warm hearth language, refined masonry, terrace/waterwork motifs, and restrained rune accents are excluded from the baseline.
- Default emissive, magical glow, signal fire, VFX, faction aura, animated material states, cloth simulation, physics, destructibility, collapse states, and final socket transforms are not claimed.
- Texture maps include `BC`, `N`, `ORM`, and optional future `E` only behind approval.
- Triangle budget, material slot target, LOD0-LOD3 plan, collision planning, animation scope, Unreal import planning, folder naming, approval gates, and stop points are included.
- Tiny lashings, scratches, rope fibers, wood grain, stitch detail, ash flecks, small nails, fine cracks, and grime are assigned to textures or normals instead of geometry.
- Source concepts remain external and are not copied, moved, edited, embedded, cropped, inspected for final approval, or committed.
- Package does not claim walkable implementation, custom collision completion, AI sightline behavior, source concept handling, final visual approval, first DCC target selection, or implementation completion.
