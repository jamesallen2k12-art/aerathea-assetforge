# SM_GIA_BloodAxeGateLookout_A01 Production Package

## Art Direction Summary

- Asset name: `SM_GIA_BloodAxeGateLookout_A01`
- Asset type: Static Mesh production package / hostile Blood Axe Giant gate-mounted lookout prop
- Task: `AET-MA-20260629-118`
- Parent kit: `KIT_GIA_BloodAxeCamp_A01`
- Source child ID: `BloodAxeGate.png#Watch_GateLookout`
- Related visual packages: `SM_GIA_BloodAxeCampGate_A01`, `SM_GIA_BloodAxeTrophyGate_A01`, `SM_GIA_BloodAxeWatchPlatform_A01`, `SK_GIA_BloodAxeCampSentry_A01`, and `SM_GIA_BloodAxeWarBanner_A01`
- Faction/theme: Blood Axe Tribe, hostile Giant sub-faction only
- Status: docs-only static visual production package ready for planning review
- Source-storage guardrail: source concepts remain external through existing intake records. Do not copy, move, crop, edit, embed, inspect for final approval, or commit source images for this task.

`SM_GIA_BloodAxeGateLookout_A01` defines a gate-mounted lookout deck or flanking perch for Blood Axe Giant camp entrances. It should read as a hostile raider watch point bolted, lashed, or braced into a rough Giant-scale gate: heavy timber deck mass, crude side brackets, partial rails, red warning cloth, blackened iron clamps, hide lashings, sparse horn or bone markers, soot, ash, mud, and brutal temporary construction.

This is not neutral or civilized Giant architecture. Do not use blue-gray master stonework, orderly cave-town masonry, warm civic hearth language, refined terraces, restrained blue runes, waterwork craft, or peaceful highland clan motifs. Blood Axe identity remains a hostile sub-faction language and must not replace normal Giant culture.

This package is static visual planning only. It does not authorize DCC source creation, collision proxy creation, FBX export, Unreal Content creation, runtime source, Blueprint behavior, startup placement, climb behavior, ladder behavior, ramp behavior, nav links, walkable setup, AI sightline logic, gate interaction behavior, gate opening behavior, sentry behavior, source concept movement, first build target selection, final visual approval, or implementation work.

## Gameplay Purpose

The purpose is visual role planning only: make a Blood Axe camp gate read as watched, hostile, and Giant-built at MMO camera distance. The lookout should strengthen the gate silhouette by implying a sentry position without defining how any character reaches, uses, guards, patrols, shoots from, or interacts with it.

Allowed visual planning uses:

- Add a gate-mounted watch read to Blood Axe camp entrances and trophy-gate approaches.
- Provide a static visual perch context for later `SK_GIA_BloodAxeCampSentry_A01` compositions without defining AI or animation behavior.
- Establish Giant-scale platform, rail, bracket, and clearance rules for a lookout that can visually sit above or beside a gate.
- Coordinate Blood Axe timber, blackened iron, red cloth, hide lashing, soot, and sparse trophy language with existing camp gate and watch platform packages.

Out of scope:

- AI sight cones, perception ranges, aggro radii, line-of-sight tests, patrol posts, spawn points, encounter scripting, ranged attack advantage, cover behavior, climb logic, ladder use, ramp traversal, navmesh rules, smart links, player interaction, objective logic, gate opening, gate locking, gate damage, destructibility, loot, crafting, salvage, resource collection, or camp ownership mechanics.

## Silhouette Notes

Primary silhouette: a compact Giant-scale lookout deck visually mounted into a Blood Axe gate, with heavy under-bracing, partial rails, and a red warning signal that reads above the gate line. It should feel added by raiders using brute-force timber and stolen hardware, not designed as clean civic architecture.

Silhouette goals:

- Read as a gate lookout before the viewer resolves small detail: deck/perch mass, rail line, support braces, and red signal cloth must be visible from front and three-quarter views.
- Keep the perch smaller and more gate-bound than `SM_GIA_BloodAxeWatchPlatform_A01`; this is not a standalone tower.
- Use one broad deck or paired flanking mini-decks sized for a Giant sentry silhouette, with a clear front edge and rough side rail.
- Add two to four bold diagonal braces or bracket arms that visually bite into the gate posts or lintel without requiring edits to the gate asset.
- Use partial Giant-height rail segments: thick, uneven, lashed logs or broken boards, not fine fence pickets.
- Include one clear Blood Axe signal element: torn red gate cloth, short warning banner, horn marker, or signal pole stub. Reuse Blood Axe banner language without turning the lookout into a banner package.
- Keep the gate passage visually open. The lookout must not collapse the gate threshold into a clutter wall.
- Use sparse bone, horn, broken shield, or old weapon markers at large scale. Keep them non-graphic and restrained.
- Optional ladder-like, notch-log, or access-shape silhouettes are not part of baseline `A01`. If later concept art requires them, they remain static visual dressing only and must not imply climb or nav behavior.

Model real geometry for the deck beams, plank mass, underside brackets, main brace arms, rail logs, large clamps, signal pole or cloth support, broad red cloth, major lashings, large plates, and sparse trophy markers. Use texture, normal, and AO detail for wood grain, tiny cuts, rope fibers, nail heads, soot streaks, leather pores, small scratches, minor cracks, cloth weave, and mud flecks.

## Scale Notes

Use the validated `SK_GIA_Base_A01` scale lock without alteration:

- Female Giant baseline: 442 cm / 14'6".
- Male Giant baseline: 470 cm / 15'5".
- Approved Giant ranges: females 14-15 ft / 427-457 cm; males 14'10"-16'0" / 452-488 cm.
- Author future source in centimeters. 1 Unreal unit = 1 cm.
- Normal humanoid compatibility is not required. Smallfolk should read as trespassers beneath an oversized hostile gate watch.

Recommended static scale targets:

- Deck floor height above ground: 620-880 cm depending on gate variant. It should sit above the entry read or on a flanking post mass, not at normal humanoid tower height.
- Minimum gate passage preservation when mounted over a threshold: keep visual clear height at 700-820 cm and clear width at 600-740 cm, matching `SM_GIA_BloodAxeCampGate_A01` planning.
- Deck footprint for one Giant sentry read: 480-700 cm wide by 320-520 cm deep.
- Paired flanking perch option: each perch 360-520 cm wide by 300-460 cm deep, with the central gate passage unobstructed.
- Clear standing zone on deck: at least 480 cm vertical clearance above the deck if overhead cloth, horn, or marker elements are used.
- Rail height from deck: 185-240 cm, roughly waist to lower-chest height for a Giant.
- Deck plank width: 70-130 cm, with chunky uneven gaps and broad bevels.
- Main bracket or brace diameter/thickness: 35-75 cm logs or equivalent split-beam mass.
- Clamp bands and scrap plates: 25-80 cm broad shapes, readable at distance.
- Red cloth signal panel: 120-240 cm wide by 160-320 cm tall.
- Overall height including signal cloth, horn markers, or pole stub: 900-1180 cm from ground when mounted to a main gate.

Gate relationship rules:

- The lookout must visually integrate with `SM_GIA_BloodAxeCampGate_A01` and `SM_GIA_BloodAxeTrophyGate_A01` without requiring those assets to change.
- It may appear clamped to a gate post, seated over a crossbeam, or hung from side braces, but no socket transforms, snap implementation, gate split, or attachment authoring is approved here.
- It must preserve Giant clearance and not imply a working gate mechanism, guard post gameplay marker, or interaction station.

## Materials and Color Palette

Primary materials:

- Raw dark timber, split beams, charred deck planks, rough cross-braces, and crude rail logs.
- Hide lashings, sinew wraps, heavy rope, scorched leather pads, and rawhide repairs.
- Blackened iron, dark steel, rough reforged plates, large clamps, spike collars, stolen scrap brackets, and short heavy chain loops.
- Packed mud, ash, soot, slag dust, rubbed grime, and trampled earth at contact points.
- Torn Blood Axe red cloth, dirty red paint, warning strips, and faded maroon gate markers.
- Bone, horn, broken shield fragments, old teeth, or dry territory markers used sparsely and non-graphically.

Suggested palette:

- Charred timber: `#1A1510` to `#3A2618`
- Weathered raw wood: `#5B412D` to `#8A6A45`
- Blackened iron: `#141619` to `#2E3031`
- Dark reforged steel: `#54585A` to `#797A76`
- Blood Axe red cloth: `#5A1412` to `#8A211A`
- Scorched leather and hide: `#241611` to `#5B3A27`
- Bone and horn accents: `#A69578` to `#D0B98C`
- Soot, ash, and mud: `#0B0A09` to `#4A3A2B`

No default emissive is approved. Forge heat, shamanic glow, signal fire, warning lamp, faction aura, VFX pulse, magic marker states, or alert-state material changes require a separate package and approval gate.

## Concept Image Prompt

Create an original stylized fantasy MMORPG concept image of `SM_GIA_BloodAxeGateLookout_A01` for the world of Aerathea. The design should emphasize a hostile Blood Axe Giant gate-mounted lookout deck or flanking perch, validated Giant scale with female baseline 442 cm / 14'6" and male baseline 470 cm / 15'5", a compact heavy deck mounted into a rough Blood Axe gate, massive raw-log plank mass, crude diagonal support brackets, Giant-height partial rails, blackened iron clamp plates, stolen scrap braces, hide lashings, rough rope, soot, ash, mud, torn red warning cloth, sparse non-graphic bone or horn territory markers, preserved Giant gate clearance, Blood Axe raider sub-faction identity, and a gameplay role limited to static hostile gate environment planning. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, no default emissive glow, and MMO-friendly mid-poly production design. Present it as a static prop concept sheet with front, side, back, top-down footprint, gate relationship callout, deck/perch scale callouts, Giant clearance callout, material swatches, and scale markers beside a 442 cm female Giant and a 470 cm male Giant on a clean background or simple Blood Axe gate context. Avoid copying any existing franchise, avoid making Blood Axe language the default Giant culture, avoid graphic gore, avoid AI sight cones, avoid patrol diagrams, avoid climb/ramp/nav diagrams, avoid gate interaction diagrams, avoid final visual approval claims, and avoid excessive micro-detail that would not translate to a mid-poly Unreal asset.

Source reference note: use `BloodAxeGate.png#Watch_GateLookout` only as an intake route reference. This docs-only package does not copy, move, inspect for final approval, crop, embed, edit, or commit external source concept imagery.

## Modeling Notes

This is a docs-only modeling plan. No mesh, Blender source, sculpt, retopo, UV, bake, collision proxy, LOD source, FBX export, Unreal asset, material graph, validator, startup placement, or final visual approval is created or approved by this package.

Future modeling should build large readable forms first:

- Deck mass: one rough plank deck or paired flanking perch deck, with broad plank widths, uneven front edge, thick side beam, and strong shadow under the platform.
- Under-bracing: two to four oversized diagonal bracket logs or split beams that visually seat into gate posts or crossbeam areas.
- Gate clamp language: large blackened iron bands, stolen scrap plates, heavy peg blocks, or ring brackets that sell a gate-mounted retrofit without requiring actual gate-asset edits.
- Rails: partial Giant-scale rail segments, using thick horizontal logs, broken boards, and lashed posts. Preserve rail read without turning the deck into dense fence clutter.
- Signal element: short pole, torn red warning cloth, horn marker, or compact banner shape that supports the Blood Axe gate read.
- Side silhouette: keep the profile deep enough to read as a perch, but not so deep that it becomes a standalone platform or wall-walk.
- Sparse Blood Axe dressing: one to three large bone/horn markers, broken shield plates, warning strips, or blackened iron trophies. Keep non-graphic and readable.
- Base/gate contact: mud, soot, iron wear, rubbed timber, and crushed lashing zones should appear where the lookout presses against gate structure.
- Optional deck dressing: static horn, warning drum, rope coil, weapon rest, or crate must remain separate or easily removable in future DCC work. Do not bake gameplay props into the main mesh unless later approved.

Use texture, normal maps, or material masks for:

- Wood grain and small cracks.
- Fine rope fibers.
- Tiny rivets, pegs, nails, and chips.
- Soot speckles and ash streaks.
- Cloth weave and frayed fibers.
- Leather pores, stitch rows, and small cuts.
- Mud stains, damp lower edges, and grime gradients.
- Minor paint chips and scratched metal pitting.

Do not model:

- Working gate hinges, latch mechanisms, pulleys, climb rungs, interactable levers, guard markers, AI sight cones, patrol markers, nav links, cover affordances, hidden gameplay objects, dense trophy strings, many tiny teeth, graphic gore, fresh remains, readable tally text, source-concept overlays, particle cards, or spell meshes.

Keep the mesh modular-friendly where practical. The default `A01` can be one static mesh for package identity, but the signal cloth, bracket arms, and optional deck dressing should be planned so later DCC can split them if composition, gate-fit, or LOD needs require it. Do not select that split or promote this package to a first build target from this docs-only task.

## Texture and Material Notes

Required map families for future approved build:

- Base Color / Albedo (`BC`)
- Normal (`N`)
- Packed Occlusion/Roughness/Metallic (`ORM`)
- Optional Emissive (`E`) only for a separately approved signal-fire, shamanic, lamp, or faction-state variant, not for baseline `A01`

Target material slot count:

- Slot 0: `MI_GIA_BloodAxeRoughTimber_A01` for deck planks, braces, rails, posts, and rough wood.
- Slot 1: `MI_GIA_BloodAxeBlackenedIron_A01` or `MI_GIA_BloodAxeReforgedMetal_A01` for clamps, collars, brackets, plates, nails, rings, and stolen scrap.
- Slot 2: `MI_GIA_BloodAxeScorchedHide_A01` for hide lashings, rope, leather wraps, and rawhide repairs.
- Slot 3: `MI_GIA_BloodAxeRedCloth_A01` for warning cloth, signal strips, and banner panels.
- Optional shared accent within an existing atlas: `MI_GIA_BloodAxeBoneTrophy_A01` if bone/horn accents cannot be handled in the timber or hide atlas.

Target 3 material slots, 4 maximum. Avoid one-off slots for each rope, clamp, trophy, cloth strip, mud patch, or deck plank.

Texture naming targets:

- `T_GIA_BloodAxeGateLookout_A01_BC`
- `T_GIA_BloodAxeGateLookout_A01_N`
- `T_GIA_BloodAxeGateLookout_A01_ORM`
- Optional future `T_GIA_BloodAxeGateLookout_A01_E` only after emissive approval

Texture resolution targets:

- Default gate lookout: 2K texture set.
- Hero gate close-route variant: 2K, with 4K only if a later hero/environment approval justifies it.
- Far camp silhouette variant: 1K with simplified material reads.

Packed `ORM` guidance:

- R: strong baked AO under deck planks, rail overlaps, brace seats, lashings, clamp plates, gate-contact brackets, cloth folds, trophy attachments, and underside shadow.
- G: high roughness for charred wood, hide, rope, soot, mud, and red cloth; varied medium-high roughness for blackened iron with slightly brighter rubbed edges.
- B: metallic only for iron, steel, clamps, collars, plates, spikes, nails, rings, and stolen scrap brackets.

Texture readability requirements:

- Maintain broad value separation between wood, red cloth, metal, hide, bone, and mud.
- Paint soot and grime at Giant scale rather than as tiny speckles only.
- Keep red cloth broad but sparse so it signals Blood Axe without turning the whole prop red.
- Avoid readable text, faction UI symbols, loot-rarity color coding, alert-state colors, weak-point markings, or magical glow masks.

## Triangle Budget

`SM_GIA_BloodAxeGateLookout_A01` is a large static gate accessory and watch prop, smaller than a standalone watch platform but more complex than simple gate dressing.

Target budget:

- LOD0 target: 10k-16k tris.
- LOD0 hard cap: 20k tris if the rail, signal cloth, bracket arms, and sparse trophy accents stay in one mesh.
- Material slots: 3 target, 4 maximum.
- Texture resolution: 2K standard for baseline `A01`.

Budget distribution guidance:

- Deck beams, deck planks, underside frame, and rail segments: 38-48 percent.
- Diagonal braces, gate brackets, clamp plates, collars, and structural hardware: 24-32 percent.
- Signal pole, red cloth, lashings, and large bindings: 14-20 percent.
- Sparse trophies, small deck dressing, mud/contact wear, and accent props: 5-10 percent.

Do not spend geometry on tiny rope fibers, dense nails, small scratches, individual mud clumps, fine splinters, dense trophy strings, many small chain links, cloth fray threads, or micro cracks.

## LOD Plan

All future implementations require LOD0-LOD3.

- LOD0: full gate-mounted lookout silhouette, deck planks, underside frame, bracket arms, partial rails, gate clamp forms, signal cloth, major lashings, large hardware, sparse trophy markers, and gate-contact dressing.
- LOD1: 60-70 percent of LOD0; reduce plank bevels, minor wood chips, secondary lashings, small clamp bevels, minor rail breaks, cloth edge cuts, and deck dressing backs.
- LOD2: 35-45 percent of LOD0; simplify deck planks into larger groups, reduce rail interiors, flatten small brace cuts, merge gate-contact details, simplify trophy accents, and remove most underside detail that does not support silhouette.
- LOD3: 15-25 percent of LOD0; preserve the mounted deck mass, bracket silhouette, rail line, red signal cloth, and overall gate-lookout read.

LOD reduction order:

1. Tiny nails, stitches, scratches, edge nicks, wood grain cuts, rope fibers, and paint chips.
2. Small secondary lashings, leather knots, and minor cloth holes.
3. Small trophy chips, tooth fragments, and non-silhouette tokens.
4. Back-side deck dressing, underside clutter, and interior plank spacing.
5. Clamp bevels, bracket chip complexity, and rail undercuts.
6. Optional visual-only access-shape detail, if any later variant adds it.
7. Only after secondary detail is removed, simplify main deck mass, bracket read, rail line, gate-mounted profile, and red signal cloth.

Never reduce the gate-mounted perch silhouette, Giant-scale deck read, primary bracket mass, red signal read, or preserved gate clearance before removing small detail.

## Collision Notes

This package plans collision intent only. It does not create collision proxies, custom UCX meshes, nav links, walkable setup, physics assets, or Unreal collision channels.

Future collision planning:

- Deck: one simple blocking box or low-count convex hull for the deck mass only if the lookout is later approved as a physical blocker or walkable visual surface. This package does not approve walkable setup.
- Brackets and braces: simple boxes or low-count convex hulls around major brace masses, not per-splinter or per-lashing collision.
- Rails: simple rail boxes only if later placement requires blocking. Do not create per-board or per-gap rail collision.
- Gate-contact clamps: simple merged blocker only where a large clamp intersects traversal or camera space.
- Signal pole: simple pole capsule or box if needed. Cloth collision disabled by default.
- Trophy accents, rope, lashings, loose cloth, small chains, and deck dressing: collision disabled by default unless a later implementation task identifies a large blocking shape.
- Optional ladder-like, notch-log, or ramp-like silhouettes: collision disabled or simplified as static prop obstruction only.

No AI sight volumes, perception blockers, cover volumes, projectile blockers, damage zones, destructible hit shapes, objective volumes, player interaction volumes, pickup collision, physics bodies, cloth collision, combat traces, gate triggers, gate blockers, gate links, climb collision, ladder volumes, ramp traversal, navmesh links, or smart links are authorized here.

## Animation Notes

Baseline asset is static.

Approved for this docs-only package:

- Static mesh planning for deck, rail, braces, gate brackets, signal pole, and fixed red cloth.
- Optional material-only dirt, soot, red paint, or timber-age variation in future material instances.
- Static visual placement context for a future sentry, with no character, AI, climb, or interaction behavior.

Approval-gated future options:

- Banner cloth simulation or vertex wind.
- Hanging marker sway.
- Signal fire, smoke, lamp, horn, or VFX state.
- Breakable rail, damaged bracket, destructible lookout, falling debris, or damage states.
- Character climb, ladder use, ramp traversal, sentry idle, patrol, lookout animation, gate operation, or interaction sequences.

None of those options are authorized by this package. Any moving, interactive, walkable, destructible, AI-linked, or gate-linked version should be split into a separately named asset or Blueprint package.

## Unreal Import Notes

This section is planning only. No Unreal Content asset, material instance, texture, Blueprint, collision proxy, validator, startup actor, import script, runtime source, source asset, or DCC export is created by this package.

Planned future Unreal asset:

- Asset name: `SM_GIA_BloodAxeGateLookout_A01`
- Asset type: Static Mesh
- Planned folder: `/Game/Aerathea/Environment/Giants/BloodAxeCamp/Structures/Gates/`
- Alternate prop folder if camp structure taxonomy changes: `/Game/Aerathea/Props/Giants/BloodAxeCamp/`
- Import scale: centimeter-authored source, import scale 1.0 after future DCC/export validation
- Pivot: ground-projected center beneath the lookout footprint, with +Z up; if a later gate-fit task requires a gate-post pivot, document it before DCC work
- Forward orientation: primary gate approach/read faces +X unless a future environment import convention specifies otherwise
- Collision type: simple custom collision or generated primitive collision only after implementation approval
- LODs: LOD0, LOD1, LOD2, LOD3 required before production import approval
- Material slot count: 3 target, 4 maximum
- Texture set: 2K baseline `BC`, `N`, `ORM`; optional `E` only behind separate emissive approval
- Sockets: none required or approved for baseline static mesh
- Blueprint behavior: none
- Animation list: none
- Performance notes: keep as a reusable large static gate accessory, avoid per-plank material splits, instance separate repeated dressing where practical, and reduce small lashings/trophies before primary deck/bracket/rail silhouette.

Potential future visual attachment markers, if separately approved:

- `gate_mount_socket_l`
- `gate_mount_socket_r`
- `watch_signal_socket`
- `banner_socket`
- `hanging_trophy_socket`
- `horn_marker_socket`
- `torch_socket`
- `deck_dressing_socket`

These are visual attachment planning notes only. Do not author sockets, interaction hooks, VFX hooks, AI hooks, climb hooks, nav links, gameplay traces, gate-operation hooks, or Blueprint behavior from this package.

Planned texture names:

- `T_GIA_BloodAxeGateLookout_A01_BC`
- `T_GIA_BloodAxeGateLookout_A01_N`
- `T_GIA_BloodAxeGateLookout_A01_ORM`
- Optional future `T_GIA_BloodAxeGateLookout_A01_E`

Planned material instances:

- `MI_GIA_BloodAxeGateLookout_A01`
- Shared references as appropriate: `MI_GIA_BloodAxeRoughTimber_A01`, `MI_GIA_BloodAxeBlackenedIron_A01`, `MI_GIA_BloodAxeReforgedMetal_A01`, `MI_GIA_BloodAxeScorchedHide_A01`, `MI_GIA_BloodAxeRedCloth_A01`, `MI_GIA_BloodAxeBoneTrophy_A01`, and `MI_GIA_BloodAxeSootAsh_A01`

## Folder and Naming Recommendation

Docs:

- Package folder: `docs/assets/props/SM_GIA_BloodAxeGateLookout_A01/`
- Package file: `docs/assets/props/SM_GIA_BloodAxeGateLookout_A01/PRODUCTION_PACKAGE.md`

Planned future source/export paths, pending separate approval only:

- Source: `SourceAssets/Blender/Props/Giants/BloodAxeCamp/SM_GIA_BloodAxeGateLookout_A01/`
- Export: `SourceAssets/Exports/Props/Giants/BloodAxeCamp/SM_GIA_BloodAxeGateLookout_A01.fbx`
- Unreal: `/Game/Aerathea/Environment/Giants/BloodAxeCamp/Structures/Gates/`

Naming:

- Static mesh: `SM_GIA_BloodAxeGateLookout_A01`
- Material instance: `MI_GIA_BloodAxeGateLookout_A01`
- Textures: `T_GIA_BloodAxeGateLookout_A01_BC`, `T_GIA_BloodAxeGateLookout_A01_N`, `T_GIA_BloodAxeGateLookout_A01_ORM`
- Optional emissive texture, if separately approved: `T_GIA_BloodAxeGateLookout_A01_E`
- Related but separate gate assets: `SM_GIA_BloodAxeCampGate_A01` and `SM_GIA_BloodAxeTrophyGate_A01`
- Related standalone watch variants, if approved separately: `SM_GIA_BloodAxeWatchPlatform_A01` and `SM_GIA_BloodAxeStakeWatchTower_A01`

Related docs:

- `docs/assets/kits/KIT_GIA_BloodAxeCamp_A01/PRODUCTION_PACKAGE.md`
- `docs/assets/kits/KIT_GIA_BloodAxeCamp_A01/CHILD_ASSET_INTAKE.md`
- `docs/assets/props/SM_GIA_BloodAxeCampGate_A01/PRODUCTION_PACKAGE.md`
- `docs/assets/props/SM_GIA_BloodAxeTrophyGate_A01/PRODUCTION_PACKAGE.md`
- `docs/assets/props/SM_GIA_BloodAxeWatchPlatform_A01/PRODUCTION_PACKAGE.md`
- `docs/assets/characters/SK_GIA_BloodAxeCampSentry_A01/PRODUCTION_PACKAGE.md`

Do not add SourceAssets folders, Blender files, sculpt files, retopo files, UVs, bakes, collision proxies, FBX exports, Unreal Content assets, material graphs, Blueprints, runtime source, tools, validators, startup-scene actors, copied source concepts, global index entries, task-board edits, backlog edits, bootstrap edits, final approval captures, or external concept-folder edits from this task.

## Stop Gates

- Stop before creating DCC source, Blender files, proof renders, sculpt files, retopo files, UVs, bakes, LOD source meshes, collision proxy meshes, FBX exports, Unreal imports, material graphs, Blueprints, runtime source, tools, validators, startup placements, or global documentation updates.
- Stop before copying, moving, cropping, editing, embedding, inspecting for final approval, or committing external source concept images.
- Stop before selecting this asset as a first DCC build target, first playable visual target, or final visual approval target.
- Stop before selecting final gate attachment method, authoring snap points, authoring socket transforms, splitting the gate mesh, editing gate assets, or changing `SM_GIA_BloodAxeCampGate_A01` or `SM_GIA_BloodAxeTrophyGate_A01`.
- Stop before defining climb behavior, ladder behavior, ramp behavior, walkable platform setup, navmesh rules, smart links, traversal volumes, or player access logic.
- Stop before defining AI sightline behavior, AI perception cones, patrol posts, aggro ranges, spawn rules, cover tags, projectile blockers, encounter layout, combat timing, trigger volumes, or gameplay collision channels.
- Stop before defining gate opening behavior, hinge behavior, portcullis behavior, lock/key logic, interaction prompts, usable doors, gate damage behavior, destructible states, repair states, fire spread, VFX, audio, objective logic, loot, resource, crafting, salvage, economy, pickup, or camp capture behavior.
- Stop before adding default emissive, ritual glow, shamanic glow, signal-fire VFX, torch VFX, smoke VFX, faction aura, cloth simulation, wind animation, physics bodies, hanging-marker sway, or animated material states.
- Stop if the design starts using neutral/civilized Giant culture as the primary identity: blue-gray carved masonry, cave-town civic pride, warm hearth halls, restrained blue runes, refined stonework, waterworks, terraces, or peaceful highland clan banners.
- Stop if any future scale review requires changing the validated Giant scale lock: female baseline 442 cm / 14'6", male baseline 470 cm / 15'5", approved range females 14-15 ft / 427-457 cm and males 14'10"-16'0" / 452-488 cm.
- Stop if material count exceeds 4 slots or LOD0 exceeds 20k tris without explicit hero gate-lookout approval.

## Quality Gate Checklist

- Package is docs-only and touches only `docs/assets/props/SM_GIA_BloodAxeGateLookout_A01/PRODUCTION_PACKAGE.md`.
- `SM_GIA_BloodAxeGateLookout_A01` is a hostile Blood Axe Giant gate-mounted lookout, not a neutral/civilized Giant structure.
- Blood Axe red-black raider language stays separate from neutral/civilized Giant stoneworker, cave-town, hearth, terrace, waterwork, highland nomad, and restrained rune culture.
- Giant scale lock is explicit and unchanged: female baseline 442 cm / 14'6" and male baseline 470 cm / 15'5", with approved ranges females 14-15 ft / 427-457 cm and males 14'10"-16'0" / 452-488 cm.
- Gameplay purpose is limited to static visual environment planning.
- Gate relationship is visual only; no gate mesh edit, gate split, gate opening behavior, lock behavior, interaction behavior, or gate runtime logic is defined.
- Sightline readability is described as visual only; no AI sight cones, perception ranges, patrol logic, cover behavior, projectile blocker logic, or encounter scripting is defined.
- Climb/ramp/ladder/walkable/nav behavior is explicitly out of scope.
- Primary silhouette reads at MMO distance: gate-mounted deck/perch, heavy bracket arms, partial rails, red signal cloth, blackened clamps, rough Giant-scale construction, and preserved gate clearance.
- Materials align with raw timber, charred wood, blackened iron, reforged metal, hide lashings, rough rope, dull red cloth, soot, ash, mud, grime, and sparse aged bone/horn trophies.
- Neutral/civilized Giant blue-gray stonecraft, warm hearth identity, terrace/waterwork language, clean masonry, and restrained blue rune motifs are excluded from the baseline.
- Default emissive, magical glow, signal fire, VFX, faction aura, animated material states, cloth simulation, physics, destructibility, and final socket transforms are not claimed.
- Texture maps include `BC`, `N`, `ORM`, and optional future `E` only behind approval.
- Triangle budget, material slot target, LOD0-LOD3 plan, collision planning, animation scope, Unreal import planning, folder naming, stop gates, and quality checklist are included.
- Tiny lashings, scratches, rope fibers, wood grain, stitch detail, ash flecks, small nails, small chips, cloth weave, metal pitting, and grime are assigned to textures or normals instead of geometry.
- Collision remains simple future planning only, with no collision proxy creation, walkable setup, per-splinter collision, per-chain collision, per-cloth collision, per-trophy collision, navmesh rules, or gameplay collision claims.
- Source concepts remain external and are not copied, moved, edited, embedded, cropped, inspected for final approval, or committed.
- Package makes no DCC, FBX, Unreal Content, runtime source, validator, startup-scene, source asset, material graph, final visual approval, first build target selection, global index edit, task-board edit, backlog edit, bootstrap edit, or external concept-folder edit claim.
