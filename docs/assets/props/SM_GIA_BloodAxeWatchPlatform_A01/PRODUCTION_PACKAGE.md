# SM_GIA_BloodAxeWatchPlatform_A01 Production Package

## Art Direction Summary

- Asset name: `SM_GIA_BloodAxeWatchPlatform_A01`
- Asset type: Static Mesh production package / hostile Giant raised watch platform prop
- Parent kit: `KIT_GIA_BloodAxeCamp_A01`
- Source child ID: `BloodAxeCamp.png#Watch_RaisedPlatform`
- Related visual dependencies: `KIT_GIA_BloodAxeArmory_A01`, `SM_GIA_BloodAxeWarBanner_A01`, and shared Blood Axe material families
- Faction/theme: Blood Axe Tribe, hostile Giant sub-faction only
- Status: docs-only production package ready for planning review
- Source-storage guardrail: source concepts remain external through existing intake records. Do not copy, move, edit, embed, inspect for final approval, or commit source images from this package.

`SM_GIA_BloodAxeWatchPlatform_A01` defines a Giant-scale raised camp lookout for hostile Blood Axe raider spaces. The platform should read as rough, temporary, territorial, and dangerous: massive raw-log uprights, crude lashed cross-bracing, uneven deck planks, blunt rail segments, a signal pole or red warning banner, blackened iron clamps, hide lashings, bone or horn warning accents, soot, ash, mud, and Blood Axe red cloth.

This is not neutral or civilized Giant architecture. Do not use blue-gray master stonework, orderly cave-town masonry, warm civic hearth language, refined terraces, restrained blue runes, or peaceful highland clan motifs. Blood Axe is a hostile sub-faction whose camp materials must remain visually separate from normal Giant culture.

This package is static visual planning only. It does not authorize DCC source creation, collision proxy creation, FBX export, Unreal Content creation, runtime source, Blueprint behavior, startup placement, climb or ramp behavior, nav links, AI sightline logic, interaction behavior, source concept movement, first build target selection, final visual approval, or implementation work.

## Gameplay Purpose

The purpose is visual role planning only: make Blood Axe camp perimeters and high points read as guarded, Giant-built, and hostile at MMO camera distance.

Allowed visual planning uses:

- Provide a raised watch silhouette for Blood Axe camp layouts, gates, barricades, shelter clusters, and perimeter compositions.
- Give `SK_GIA_BloodAxeCampSentry_A01` and related warband characters a visually plausible static placement context without defining guard behavior.
- Establish Giant-scale deck height, railing mass, pole/banner read, and construction language for later DCC planning.
- Support future environment storytelling through crude build quality, territorial red cloth, soot, blackened iron, and sparse non-graphic trophy markers.

Out of scope:

- AI sight cones, perception ranges, aggro radii, line-of-sight tests, patrol routes, spawn logic, encounter scripting, cover behavior, climb logic, ramp traversal, ladder use, navmesh rules, smart links, player interaction, objective logic, destructibility, trap behavior, loot, crafting, salvage, resource collection, or camp ownership mechanics.

## Silhouette Notes

Primary silhouette: a raised raw-log platform sized for Giants, with thick vertical supports, an uneven plank deck, heavy cross-bracing, crude rail sections, and one clear Blood Axe signal element visible from a distance.

Silhouette goals:

- Read as a Blood Axe watch point before the viewer resolves small details.
- Use four to six oversized upright trunks or split logs with irregular heights and blunt chopped tops.
- Keep the deck broad and heavy, with a slightly uneven plank edge and enough mass to feel built for a 470 cm Giant.
- Add diagonal cross-bracing in a few bold X or slash shapes, not dense scaffolding.
- Use partial railings: chest-high for Giants, uneven, lashed, and broken in silhouette, but still readable as a platform edge.
- Include one visual signal element: a tall red warning cloth, compact banner, horn marker, or signal pole. Reuse `SM_GIA_BloodAxeWarBanner_A01` language without turning this into a banner package.
- Optional ladder-like or ramp-like shapes may exist only as static construction silhouettes if required by concept art. They must not imply approved climb, ramp, or nav behavior.
- Use sparse bone, horn, broken shield, or tooth markers at large scale. Avoid dense skull curtains, graphic gore, or trophy clutter.
- Keep camp clutter minimal on the deck: a horn, warning drum, crate, coil, or weapon rest may be planned as separate dressing only if it does not blur the platform silhouette.

Model real geometry for the main posts, deck planks, crossbeams, rails, major bindings, large clamps, signal pole, broad red cloth, base stones, and sparse trophy markers. Use texture, normal, and AO detail for tiny cuts, wood grain, rope fibers, nail heads, soot streaks, leather pores, small scratches, minor cracks, cloth weave, and mud flecks.

## Scale Notes

Use the validated `SK_GIA_Base_A01` scale lock without alteration:

- Female Giant baseline: 442 cm / 14'6".
- Male Giant baseline: 470 cm / 15'5".
- Approved Giant ranges: females 14-15 ft / 427-457 cm; males 14'10"-16'0" / 452-488 cm.
- Author future source in centimeters. 1 Unreal unit = 1 cm.
- Normal humanoid compatibility is not required. Smallfolk should read as trespassers around an oversized enemy structure.

Recommended static scale targets:

- Deck height above ground: 520-760 cm. This is high enough to read as a watch point while staying below full tower/stronghold scale.
- Deck footprint: 650-950 cm wide by 500-800 cm deep.
- Clear standing zone on deck: at least 480 cm vertical clearance above deck if any overhead element is included.
- Platform rail height: 185-240 cm from deck surface, roughly waist to lower-chest height for a Giant, not normal-human railing scale.
- Main support log diameter: 45-90 cm, irregular and rough-hewn.
- Secondary braces: 28-55 cm diameter or equivalent split-beam mass.
- Deck plank width: 70-140 cm, with visible Giant-scale spacing and uneven edges.
- Signal pole total height: 760-980 cm from ground if mounted to the platform, or 220-360 cm above deck if measured from deck surface.
- Red cloth signal panel: 140-260 cm wide by 180-340 cm tall, depending on variant and camera read.
- Optional visual-only ladder/ramp shape: oversized enough for Giant construction language, but no climb spacing, traversal angle, or nav approval is defined here.

Sightline readability is visual only:

- The deck height, rail gaps, and signal pole should communicate "lookout position" from camp approach angles.
- Do not encode AI perception, player visibility, ranged attack advantage, cover rules, or gameplay sightline volumes in the asset plan.
- The structure should frame a Giant sentry silhouette cleanly if a character is placed nearby in a later approval-gated composition.

## Materials and Color Palette

Primary materials:

- Raw dark timber, split logs, charred stakes, crude deck planks, and rough crossbeams.
- Hide lashings, sinew wraps, heavy rope, scorched leather pads, and rawhide repairs.
- Blackened iron, dark steel, rough reforged plates, large clamps, spike collars, and stolen scrap braces.
- Packed mud, ash, soot, slag dust, and trampled earth around the base.
- Rough field stone, base weights, or cairn-like stabilizers used sparingly and crudely.
- Torn Blood Axe red cloth, dirty red paint, and warning strips as hostile sub-faction identifiers.
- Bone, horn, broken shield fragments, teeth, or dry territory markers used sparsely and non-graphically.

Suggested palette:

- Charred timber: `#1A1510` to `#3A2618`
- Weathered raw wood: `#5B412D` to `#8A6A45`
- Blackened iron: `#141619` to `#2E3031`
- Dark reforged steel: `#54585A` to `#797A76`
- Blood Axe red cloth: `#5A1412` to `#8A211A`
- Scorched leather and hide: `#241611` to `#5B3A27`
- Bone and horn accents: `#A69578` to `#D0B98C`
- Soot, ash, and mud: `#0B0A09` to `#4A3A2B`

No default emissive is approved. Forge heat, shamanic glow, signal fire, warning lamp, faction aura, VFX pulse, or magic marker states require a separate package and approval gate.

## Concept Image Prompt

Create an original stylized fantasy MMORPG concept image of `SM_GIA_BloodAxeWatchPlatform_A01` for the world of Aerathea. The design should emphasize a hostile Blood Axe Giant raised watch platform silhouette, validated Giant scale with female baseline 442 cm / 14'6" and male baseline 470 cm / 15'5", massive raw-log uprights, heavy uneven deck planks, crude diagonal cross-bracing, Giant-height partial rails, a tall signal pole or torn red warning banner, blackened iron clamps, hide lashings, rough rope, soot, ash, mud, sparse non-graphic bone or horn territory markers, Blood Axe raider sub-faction identity, visual sightline readability only, and a gameplay role limited to static hostile camp environment planning. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, no default emissive glow, and MMO-friendly mid-poly production design. Present it as a static prop concept sheet with front, side, back, top-down footprint, material swatches, rail/deck scale callouts, and scale markers beside a 442 cm female Giant and a 470 cm male Giant on a clean background or simple Blood Axe camp context. Avoid copying any existing franchise, avoid making Blood Axe language the default Giant culture, avoid graphic gore, avoid AI sight cones, avoid patrol diagrams, avoid climb/ramp/nav diagrams, avoid interaction callouts, avoid final visual approval claims, and avoid excessive micro-detail that would not translate to a mid-poly Unreal asset.

## Modeling Notes

This is a docs-only modeling plan. No mesh, Blender source, sculpt, retopo, UV, bake, collision proxy, LOD source, FBX export, Unreal asset, material graph, validator, startup placement, or final visual approval is created or approved by this package.

Future modeling should build large readable forms first:

- Main supports: four to six rough logs with uneven diameters, chopped tops, slight bends, broad splinters, and heavy contact at ground.
- Deck frame: large perimeter beams, uneven deck planks, oversized plank gaps, heavy nail or peg blocks, and crude load-bearing corners.
- Cross-bracing: a few bold diagonal beams or X braces on visible faces, with large lashings and clamp plates at intersections.
- Rails: partial rail segments at Giant scale, using thick horizontal logs, broken boards, and lashed vertical posts. Preserve rail read without creating dense fence clutter.
- Base stabilization: rough stone weights, mud-packed log feet, hammered metal collars, or crude stakes. Keep base elements broad enough to read from MMO camera distance.
- Signal element: signal pole, compact red warning cloth, horn marker, or small camp banner that references `SM_GIA_BloodAxeWarBanner_A01` without duplicating a full banner asset.
- Sparse Blood Axe dressing: one to three large bone/horn markers, broken shield plates, warning cloth strips, or blackened iron trophies. Keep non-graphic and readable.
- Deck dressing: optional static horn, crate, rope coil, weapon rest, or warning drum should remain separate or easily removable in future DCC work. Do not bake gameplay props into the main mesh unless later approved.
- Optional access silhouette: ladder-like slats, a heavy notched log, or a ramp-like plank mass may be blocked in visually only. Do not define rung spacing, traversal angle, climb volumes, navmesh use, or interaction logic.

Use texture, normal maps, or material masks for:

- Wood grain and small cracks.
- Fine rope fibers.
- Tiny rivets, pegs, nails, and chips.
- Soot speckles and ash streaks.
- Cloth weave and frayed fibers.
- Leather pores, stitch rows, and small cuts.
- Mud stains, damp lower edges, and grime gradients.
- Minor paint chips and scratched metal pitting.

Keep the mesh modular-friendly where practical. The main platform may be one static mesh for package identity, but posts, signal pole, banner cloth, and deck dressing should be planned so later DCC can split them if composition or LOD needs require it.

## Texture and Material Notes

Required map families for future approved build:

- Base Color / Albedo (`BC`)
- Normal (`N`)
- Packed Occlusion/Roughness/Metallic (`ORM`)
- Optional Emissive (`E`) only for a separately approved signal-fire, shamanic, lamp, or faction-state variant, not for baseline `A01`

Target material slot count:

- Slot 0: `MI_GIA_BloodAxeRoughTimber_A01` for posts, deck, braces, rails, and rough wood.
- Slot 1: `MI_GIA_BloodAxeBlackenedIron_A01` or `MI_GIA_BloodAxeReforgedMetal_A01` for clamps, collars, plates, nails, and stolen scrap.
- Slot 2: `MI_GIA_BloodAxeScorchedHide_A01` for hide lashings, rope, leather wraps, and rawhide repairs.
- Slot 3: `MI_GIA_BloodAxeRedCloth_A01` for warning cloth, signal strips, and banner panels.
- Optional shared accent within an existing atlas: `MI_GIA_BloodAxeBoneTrophy_A01` if bone/horn accents cannot be handled in the timber or hide atlas.

Target 3 material slots, 4 maximum. Avoid one-off slots for each rope, clamp, trophy, cloth strip, mud patch, or deck plank.

Texture naming targets:

- `T_GIA_BloodAxeWatchPlatform_A01_BC`
- `T_GIA_BloodAxeWatchPlatform_A01_N`
- `T_GIA_BloodAxeWatchPlatform_A01_ORM`
- Optional future `T_GIA_BloodAxeWatchPlatform_A01_E` only after emissive approval

Texture resolution targets:

- Default platform: 2K texture set.
- Hero close-route variant: 2K, with 4K only if a later hero/environment approval justifies it.
- Far camp silhouette variant: 1K with simplified material reads.

Packed `ORM` guidance:

- R: Strong baked AO under deck planks, rail overlaps, lashings, clamp plates, brace joints, base stones, and trophy attachments.
- G: High roughness for charred wood, hide, rope, soot, mud, and red cloth; varied medium-high roughness for blackened iron with slightly brighter worn edges.
- B: Metallic only for iron, steel, clamps, collars, plates, spikes, nails, and stolen scrap braces.

Texture readability requirements:

- Maintain broad value separation between wood, red cloth, metal, hide, bone, and mud.
- Paint soot and grime at Giant scale rather than as tiny speckles only.
- Keep red cloth broad but sparse so it signals Blood Axe without turning the whole prop red.
- Avoid readable text, faction UI symbols, loot-rarity color coding, alert-state colors, weak-point markings, or magical glow masks.

## Triangle Budget

`SM_GIA_BloodAxeWatchPlatform_A01` is a large static camp prop, not a full tower, building, or hero stronghold module.

Target budget:

- LOD0 target: 10k-18k tris.
- LOD0 hard cap: 22k tris if the signal pole, base weights, partial rail, and sparse trophy accents are kept in the same mesh.
- Material slots: 3 target, 4 maximum.
- Texture resolution: 2K standard for baseline `A01`.

Budget distribution guidance:

- Main posts, deck beams, deck planks, and underside frame: 45-55 percent.
- Cross-bracing, rail segments, and base stabilization: 22-30 percent.
- Signal pole, red cloth, clamps, lashings, and large bindings: 15-20 percent.
- Sparse trophies, deck dressing, mud/base details, and accent props: 5-10 percent.

Do not spend geometry on tiny rope fibers, dense nails, small scratches, individual mud clumps, fine splinters, dense trophy strings, many small chain links, cloth fray threads, or micro cracks.

## LOD Plan

All future implementations require LOD0-LOD3.

- LOD0: full platform silhouette, main posts, deck planks, underside frame, cross-bracing, partial rails, base weights, signal pole, broad red cloth, major clamps, large lashings, and sparse trophy markers.
- LOD1: 60-70 percent of LOD0; reduce plank bevels, minor post chips, secondary lashings, small clamp bevels, minor rail breaks, small cloth edge cuts, and deck dressing backs.
- LOD2: 35-45 percent of LOD0; simplify deck planks into larger groups, reduce rail interiors, flatten small brace cuts, merge base details, simplify trophy accents, and remove most underside detail that does not support silhouette.
- LOD3: 15-25 percent of LOD0; preserve raised platform mass, vertical post read, deck block, cross-brace diagonals, rail line, red signal cloth, and overall height.

LOD reduction order:

1. Tiny nails, stitches, scratches, edge nicks, wood grain cuts, rope fibers, and paint chips.
2. Small secondary lashings, leather knots, and minor cloth holes.
3. Small trophy chips, tooth fragments, and non-silhouette tokens.
4. Back-side deck dressing, underside clutter, and interior plank spacing.
5. Clamp bevels, post chip complexity, and rail undercuts.
6. Optional visual-only access silhouette detail.
7. Only after secondary detail is removed, simplify main post height, deck mass, rail line, cross-brace read, and red signal cloth.

Never reduce the raised watch-platform outline, Giant-scale deck height, primary post mass, red signal read, or camp-warning silhouette before removing small detail.

## Collision Notes

This package plans collision intent only. It does not create collision proxies, custom UCX meshes, nav links, walkable setup, physics assets, or Unreal collision channels.

Future collision planning:

- Main supports: simple boxes or low-count convex hulls around post clusters, not per-splinter or per-lashing collision.
- Deck: one simple blocking box or convex hull for the deck mass if the platform is later approved as walkable. If not walkable, collision can remain simplified around the overall prop bounds.
- Rails: simple rail boxes only if later placement requires blocking. Do not create per-board or per-gap rail collision.
- Base weights and stones: simple low-count hulls or merged base box if they block traversal.
- Signal pole: simple pole capsule or box. Cloth collision disabled by default.
- Trophy accents, rope, lashings, loose cloth, and deck dressing: collision disabled by default unless a later implementation task identifies a large blocking shape.
- Optional ladder-like or ramp-like silhouettes: collision disabled or simplified as static prop obstruction only. Do not define climb collision, ramp traversal, ladder volumes, navmesh links, smart links, or interaction triggers.

No AI sight volumes, perception blockers, cover volumes, projectile blockers, damage zones, destructible hit shapes, objective volumes, player interaction volumes, pickup collision, physics bodies, cloth collision, or combat traces are authorized here.

## Animation Notes

Baseline asset is static.

Approved for this docs-only package:

- Static mesh planning for platform, rail, posts, deck, base, signal pole, and fixed red cloth.
- Optional material-only dirt or paint variation in future material instances.
- Static visual placement context for a future sentry, with no character or AI behavior.

Approval-gated future options:

- Banner cloth simulation or vertex wind.
- Hanging marker sway.
- Signal fire, smoke, lamp, horn, or VFX state.
- Breakable rail, destructible platform, falling debris, or damage states.
- Character climb, ladder use, ramp traversal, sentry idle, patrol, lookout animation, or interaction sequences.

None of those options are authorized by this package. Any moving or interactive version should be split into a separately named asset or Blueprint package.

## Unreal Import Notes

This section is planning only. No Unreal Content asset, material instance, texture, Blueprint, collision proxy, validator, startup actor, import script, runtime source, source asset, or DCC export is created by this package.

Planned future Unreal asset:

- Asset name: `SM_GIA_BloodAxeWatchPlatform_A01`
- Asset type: Static Mesh
- Planned folder: `/Game/Aerathea/Environment/Giants/BloodAxeCamp/Structures/`
- Alternate prop folder if camp structure taxonomy changes: `/Game/Aerathea/Props/Giants/BloodAxeCamp/`
- Import scale: centimeter-authored source, import scale 1.0 after future DCC/export validation
- Pivot: ground-contact center beneath the deck footprint, with +Z up
- Forward orientation: primary platform face and signal cloth read toward +X unless a future environment import convention specifies otherwise
- Collision type: simple custom collision or generated primitive collision only after implementation approval
- LODs: LOD0, LOD1, LOD2, LOD3 required before production import approval
- Material slot count: 3 target, 4 maximum
- Texture set: 2K baseline `BC`, `N`, `ORM`; optional `E` only behind separate emissive approval
- Sockets: none required for baseline static mesh
- Blueprint behavior: none
- Animation list: none
- Performance notes: keep as a reusable large static prop, avoid per-board material splits, instance separate repeated dressing where practical, and reduce small lashings/trophies before primary post/deck silhouette.

Potential future visual attachment markers, if separately approved:

- `watch_signal_socket`
- `banner_socket`
- `hanging_trophy_socket`
- `horn_marker_socket`
- `torch_socket`
- `deck_dressing_socket`

These are visual attachment planning notes only. Do not author sockets, interaction hooks, VFX hooks, AI hooks, climb hooks, nav links, gameplay traces, or Blueprint behavior from this package.

Planned texture names:

- `T_GIA_BloodAxeWatchPlatform_A01_BC`
- `T_GIA_BloodAxeWatchPlatform_A01_N`
- `T_GIA_BloodAxeWatchPlatform_A01_ORM`
- Optional future `T_GIA_BloodAxeWatchPlatform_A01_E`

Planned material instances:

- `MI_GIA_BloodAxeWatchPlatform_A01`
- Shared references as appropriate: `MI_GIA_BloodAxeRoughTimber_A01`, `MI_GIA_BloodAxeBlackenedIron_A01`, `MI_GIA_BloodAxeReforgedMetal_A01`, `MI_GIA_BloodAxeScorchedHide_A01`, `MI_GIA_BloodAxeRedCloth_A01`, `MI_GIA_BloodAxeBoneTrophy_A01`, and `MI_GIA_BloodAxeSootAsh_A01`

## Folder and Naming Recommendation

Docs:

- `docs/assets/props/SM_GIA_BloodAxeWatchPlatform_A01/PRODUCTION_PACKAGE.md`

Planned future source/export paths, pending separate approval only:

- Source: `SourceAssets/Blender/Props/Giants/BloodAxeCamp/SM_GIA_BloodAxeWatchPlatform_A01/`
- Export: `SourceAssets/Exports/Props/Giants/BloodAxeCamp/SM_GIA_BloodAxeWatchPlatform_A01.fbx`
- Unreal: `/Game/Aerathea/Environment/Giants/BloodAxeCamp/Structures/`

Naming:

- Static mesh: `SM_GIA_BloodAxeWatchPlatform_A01`
- Material instance: `MI_GIA_BloodAxeWatchPlatform_A01`
- Textures: `T_GIA_BloodAxeWatchPlatform_A01_BC`, `T_GIA_BloodAxeWatchPlatform_A01_N`, `T_GIA_BloodAxeWatchPlatform_A01_ORM`
- Optional emissive texture, if separately approved: `T_GIA_BloodAxeWatchPlatform_A01_E`
- Optional later variants, if approved separately: `SM_GIA_BloodAxeGateLookout_A01`, `SM_GIA_BloodAxeStakeWatchTower_A01`, or `SM_GIA_BloodAxeWatchPlatform_Damaged_A01`

Related docs:

- `docs/assets/kits/KIT_GIA_BloodAxeCamp_A01/PRODUCTION_PACKAGE.md`
- `docs/assets/kits/KIT_GIA_BloodAxeCamp_A01/CHILD_ASSET_INTAKE.md`
- `docs/assets/kits/KIT_GIA_BloodAxeArmory_A01/PRODUCTION_PACKAGE.md`
- `docs/assets/props/SM_GIA_BloodAxeWarBanner_A01/PRODUCTION_PACKAGE.md`
- `docs/assets/characters/SK_GIA_BloodAxeCampSentry_A01/PRODUCTION_PACKAGE.md`

Do not add SourceAssets folders, Blender files, sculpt files, retopo files, UVs, bakes, collision proxies, FBX exports, Unreal Content assets, material graphs, Blueprints, runtime source, tools, validators, startup-scene actors, copied source concepts, global index entries, task-board edits, backlog edits, bootstrap edits, final approval captures, or external concept-folder edits from this task.

## Approval Gates and Stop Points

- Lead approval is required before `SM_GIA_BloodAxeWatchPlatform_A01` is selected as a first DCC target.
- Visual approval is required before final platform silhouette, deck height, rail density, signal pole, red cloth placement, trophy density, access-shape read, or camp composition role is locked.
- Culture approval is required if Blood Axe raider language starts bleeding into neutral/civilized Giant packages.
- DCC approval is required before creating source folders, Blender sources, sculpt files, retopo files, UVs, bakes, proof renders, collision proxies, LOD sources, or exports.
- Unreal approval is required before importing static meshes, material instances, textures, LODs, collision, sockets, validators, Blueprints, or startup-scene actors.
- Collision approval is required before authoring custom collision, walkable deck setup, rail blocking, or base hulls.
- Cloth and physics approval is required before adding cloth simulation, vertex wind, hanging-marker sway, destructible parts, physics bodies, or moving cloth.
- Gameplay approval is required before any climb/ramp behavior, ladder use, navmesh rules, smart links, AI sightline behavior, patrol posts, cover rules, combat behavior, projectile blocking, encounter scripting, spawn rules, guard-post interactions, loot rules, trap behavior, objective logic, destructibility, camp capture, resource/crafting/salvage behavior, or interactable behavior.
- Source-storage approval is required before copying, embedding, editing, moving, cropping, inspecting for final visual approval, or committing any external source concept.

Stop immediately before:

- Any DCC, FBX, Unreal, source asset, runtime source, validator, material graph, Blueprint, startup placement, or source concept work.
- Final visual approval, first playable visual approval, or first build target selection.
- Any collision proxy creation, UCX mesh work, walkable platform implementation, climb/ramp/nav setup, or AI sightline implementation.
- Any socket authoring, VFX hook, interaction hook, gameplay trace, cover volume, objective volume, or encounter logic.
- Any patrol, AI, aggro, spawn, combat, projectile, loot, economy, crafting, interaction, resource, salvage, destructible, or objective definition.
- Any change to the validated `SK_GIA_Base_A01` scale lock or Giant race range.
- Any shift that makes Blood Axe red-black raider language the default Giant culture.
- Any increase in trophies, skulls, red cloth, chains, straps, rivets, cracks, scratches, gore, or deck clutter that hurts mid-poly MMO readability.

## Quality Gate Checklist

- Package is docs-only and changes no DCC, FBX, Unreal Content, runtime source, startup scene, source asset, external concept, validator, global index, task board, backlog, bootstrap, or other package file.
- `SM_GIA_BloodAxeWatchPlatform_A01` is a hostile Blood Axe Giant camp prop, not a neutral/civilized Giant structure.
- Giant scale lock is explicit and unchanged: female baseline 442 cm / 14'6" and male baseline 470 cm / 15'5", with approved ranges females 14-15 ft / 427-457 cm and males 14'10"-16'0" / 452-488 cm.
- Gameplay purpose is limited to static visual environment planning.
- Sightline readability is described as visual only; no AI sight cones, perception ranges, patrol logic, cover behavior, or encounter scripting are defined.
- Climb/ramp/ladder/nav behavior is explicitly out of scope.
- Primary silhouette reads at MMO distance: raised deck, massive raw-log supports, cross-bracing, partial rails, signal pole or red cloth, and rough Giant-scale construction.
- Materials align with raw timber, charred wood, blackened iron, reforged metal, hide lashings, rough rope, dull red cloth, soot, ash, mud, grime, and sparse aged bone/horn trophies.
- Neutral/civilized Giant stoneworker materials, blue-gray cave-town identity, warm hearth language, refined masonry, and restrained rune accents are excluded from the baseline.
- Default emissive, magical glow, signal fire, VFX, faction aura, animated material states, cloth simulation, physics, destructibility, and final socket transforms are not claimed.
- Texture maps include `BC`, `N`, `ORM`, and optional future `E` only behind approval.
- Triangle budget, material slot target, LOD0-LOD3 plan, collision planning, animation scope, Unreal import planning, folder naming, approval gates, and stop points are included.
- Tiny lashings, scratches, rope fibers, wood grain, stitch detail, ash flecks, small nails, and grime are assigned to textures or normals instead of geometry.
- Package does not claim walkable implementation, custom collision completion, AI sightline behavior, source concept handling, final visual approval, first DCC target selection, or implementation completion.
