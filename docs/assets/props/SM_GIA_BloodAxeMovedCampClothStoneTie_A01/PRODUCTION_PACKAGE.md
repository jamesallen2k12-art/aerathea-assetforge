# SM_GIA_BloodAxeMovedCampClothStoneTie_A01 Production Package

## Art Direction Summary

- Asset name: `SM_GIA_BloodAxeMovedCampClothStoneTie_A01`
- Asset type: Static Mesh prop production package, docs-only
- Task: `AET-MA-20260629-322`
- Parent kit: `KIT_GIA_BloodAxeMovedCampCairnLine_A01`
- Parent child row: `BloodAxeRitualStones_A01#MovedCamp_ClothRemnantStoneTie_A01`
- Source child note: fixed oxide red cloth tied around or trapped under a low cairn stone
- Faction/theme: Blood Axe Tribe, hostile Giant sub-faction only
- Scale dependency: validated `SK_GIA_Base_A01` Giant scale lock
- Status: package candidate, planning only

`SM_GIA_BloodAxeMovedCampClothStoneTie_A01` defines a small static moved-camp residue prop: a low rough cairn stone with one fixed oxide red cloth remnant tied around it or trapped beneath it. The asset should read as abandoned Blood Axe camp evidence, not an active banner, route marker, quest clue, color-coded UI element, faction buff source, readable message, or interaction object.

Blood Axe visual language must remain separate from neutral/civilized Giant culture. Use hostile raider residue: rough highland stone, soot, ash, trampled mud, oxide red cloth, rawhide, rope, and sparse blackened iron only if needed. Do not use refined blue-gray civic masonry, cave-town carving, terrace or waterwork motifs, warm hearth settlement language, peaceful highland markers, restrained blue runes, or neutral/civilized Giant cultural identity as the default read.

This package is docs-only. It explicitly blocks DCC work, FBX export, Unreal Content edits, startup placement, source concept movement, runtime source, validators, Hermes work, final visual approval, final camp-route approval, and first implementation target selection.

## Gameplay Purpose

The gameplay purpose is environmental storytelling only. The prop suggests that a Blood Axe camp once occupied or crossed the area, then moved on and left a small cloth-and-stone remnant behind.

Allowed planning uses:

- Add one restrained Blood Axe color beat to a moved-camp cairn-line composition.
- Support the sense of abandoned Giant raider passage without forming a functional trail.
- Provide future artists with scale, silhouette, material, LOD, collision, and naming guidance for a single static dressing prop.
- Preserve separation between hostile Blood Axe raider residue and neutral/civilized Giant culture.

Out of scope:

- Cloth simulation, wind response, vertex wind, swaying cloth, UI color coding, faction buff behavior, readable message content, interaction behavior, pickup behavior, loot behavior, salvage behavior, resource behavior, crafting behavior, waypoint behavior, breadcrumb behavior, tracking mechanics, UI path logic, objective logic, route validation, navigation/pathfinding, spawn logic, patrol logic, encounter scripting, AI behavior, damage or aura behavior, VFX, audio, active ritual state, collision correctness, DCC, FBX, Unreal work, startup placement, final approval, implementation target selection, source concept movement, Hermes work, runtime source, validators, global docs edits, source folders, material instances, or texture assets.

## Silhouette Notes

- Primary read: one low cairn stone or compact two-stone base pinning a fixed oxide red cloth remnant.
- Cloth read: the cloth is tied tight around the stone or trapped under its lower edge, with a short dirty tail or folded strip visible at ground level.
- Stone read: broad, rough, Giant-placed field stone, chunky and low rather than a maintained guidepost.
- Grounding read: cold ash, soot, trampled mud, or packed earth may ground the stone, but must not form a trail, arrow, ring, footprint line, or objective area.
- Faction read: the oxide red cloth provides a subdued Blood Axe identity beat only. It must not become a banner, signal flag, UI cue, faction buff icon, warning marker, or readable text panel.
- Camera read: from a normal MMO camera, the asset should read as a small abandoned cloth-stone remnant, not a player-facing marker.

Model real geometry in future approved work only for the main stone mass, broad bevels affecting silhouette, fixed cloth strip silhouette, large knot or pinched fold if present, and low grounding base if needed. Reserve cloth weave, fray, soot speckles, ash flecks, stone cracks, chipped edges, mud streaks, rope fibers, lichen, and tiny paint wear for future texture, normal, AO, or mask detail.

Avoid clean symmetry, vertical signpost forms, route-facing arrows, readable glyphs, written message marks, flag shapes, banner silhouettes, glowing runes, fresh saturated cloth, UI-like color blocking, trophy clutter, graphic gore, neutral Giant civic carving, warm hearth motifs, and blue rune language.

## Scale Notes

Use the validated `SK_GIA_Base_A01` Giant scale lock:

- Female Giant baseline: 442 cm / 14 ft 6 in.
- Male Giant baseline: 470 cm / 15 ft 5 in.
- Approved Giant ranges: females 14-15 ft / 427-457 cm; males 14 ft 10 in-16 ft / 452-488 cm.
- These Giant baselines must not be changed by this package.

Visual planning dimensions:

- Overall asset height: 35-110 cm above ground.
- Preferred common height: 45-80 cm so the prop remains a low residue beat, not an active guidepost.
- Stone footprint: 70-190 cm wide by 50-150 cm deep.
- Dominant stone: 60-160 cm across the broad face, sized for Giant-built readability without becoming a wall block.
- Visible cloth length: 35-130 cm total visible length, including tied band and short tail.
- Visible cloth width: 10-35 cm, wide enough to read from gameplay camera but subordinate to the stone.
- Optional ash/mud grounding: 90-240 cm irregular footprint with very low relief.

At this scale, the prop sits far below the 442 cm female Giant and 470 cm male Giant baselines. It should read as a low, knee-near remnant for Giants and oversized ground dressing for smaller races.

These dimensions are visual planning values only. They are not collision correctness, traversal metrics, interaction reach, route metrics, objective radii, faction-buff radius, UI marker scale, navigation values, camera approval values, DCC approval, FBX approval, Unreal approval, startup placement, final approval, or implementation target selection.

## Materials and Color Palette

Primary materials:

- Rough highland stone, fractured field rock, soot-stained cairn stone, and mud-packed contact surfaces.
- Fixed oxide red cloth, dirty maroon fabric, sun-faded Blood Axe textile, and ash-stained cloth edges.
- Rawhide, rough rope, sinew cord, or scorched leather as small tie support only if needed.
- Cold ash, charcoal dust, trampled mud, packed earth, and sparse burned grass residue.
- Sparse blackened iron only as an optional old pin or scrap, never as a focal object.

Palette targets:

- Dark stone and soot: `#17191A`, `#252728`, `#3B3A37`, `#55534D`
- Ash and worn stone: `#646059`, `#817A70`, `#9E9587`
- Mud and packed earth: `#241A15`, `#392A20`, `#57402F`
- Fixed Blood Axe cloth: `#4B1110`, `#651714`, `#7A241B`, `#8B3D30`
- Rope, rawhide, and leather: `#503E26`, `#6C5334`, `#947349`
- Optional old iron: `#1E2223`, `#2F3333`

No default emissive is approved. Do not add ritual glow, magic glow, signal glow, torch light, animated material states, UI highlights, faction-buff color states, objective color states, readable message ink, or blue rune language. Any active, glowing, readable, buff-granting, interactive, or gameplay-readable variant requires a separate approved package.

## Concept Image Prompt

Create an original stylized fantasy MMORPG static prop concept sheet of `SM_GIA_BloodAxeMovedCampClothStoneTie_A01` for the world of Aerathea. The design should emphasize a low rough Giant cairn stone with one fixed oxide red cloth remnant tied around it or trapped under the stone edge, broad readable stone massing, dirty cloth folds, soot-dark contact marks, cold ash, trampled mud, rawhide or rope restraint only if needed, hostile Blood Axe Giant sub-faction identity, strict separation from neutral/civilized Giant culture, abandoned moved-camp mood, and the gameplay role of static environmental storytelling only. Use hand-painted texture detail, readable shapes, baked-AO-style depth, normal-map-style surface detail, no emissive glow, no cloth simulation, and MMO-friendly mid-poly production design. Present it as a static mesh prop production sheet with front, side, top-down footprint, material swatches, LOD and collision guardrail notes, and scale markers beside female 442 cm / 14 ft 6 in and male 470 cm / 15 ft 5 in Giant baselines on a clean background. Avoid copying any existing franchise, avoid wind or cloth motion, avoid readable message text, avoid UI color coding, avoid faction buff reads, avoid route arrows, avoid waypoint chains, avoid breadcrumb symbols, avoid tracking UI, avoid pickup or loot reads, avoid interaction prompts, avoid objective markers, avoid navigation diagrams, avoid spawn or patrol reads, avoid DCC claims, avoid FBX claims, avoid Unreal implementation claims, avoid startup placement, avoid final approval language, avoid source concept movement, avoid Hermes work, avoid neutral Giant civic materials as Blood Axe defaults, avoid graphic gore, and avoid excessive micro-detail that would not translate to a mid-poly game asset.

## Modeling Notes

This is a docs-only modeling plan. No DCC source, Blender file, sculpt, mesh, retopo, UV, bake, proof render, LOD source, collision proxy, FBX export, Unreal asset, material instance, texture asset, material graph, validator, runtime source, Blueprint, socket, animation asset, startup placement, implementation target, source concept movement, Hermes work, final visual approval, or final camp-route approval is created or authorized.

Future modeling guidance only if a later approved task promotes the asset:

- Build one compact static prop with a ground-centered footprint and a clear front/three-quarter read.
- Use one dominant low stone, or one dominant stone with a small support stone only if the silhouette remains simple.
- Place the cloth as a fixed band, trapped flap, or tight wrap that is visibly pinned by stone weight.
- Keep the cloth short, dirty, and slack against the stone. Do not pose it like a flag, streamer, route ribbon, UI marker, or readable sign.
- Use broad bevels and simple fractured planes where they affect the stone silhouette.
- Keep ash and mud as irregular grounding residue. Do not form footprints, trails, arrows, rings, lanes, route beats, or objective shapes.
- If rawhide or rope is included, keep it thick, low-count, and subordinate to the fixed cloth and stone.
- If future source is approved, place the pivot at ground center under the full footprint and orient the strongest readable cloth-stone face toward +X unless a later export convention says otherwise.

Suggested future mesh groups, planning only:

- `ClothStoneTie_StoneMass`
- `ClothStoneTie_FixedCloth`
- `ClothStoneTie_AshMudBase`
- `ClothStoneTie_RawhideRopeOptional`
- `ClothStoneTie_OldIronOptional`

Do not add sockets, marker locators, route helpers, navigation helpers, spawn helpers, patrol helpers, VFX locators, audio locators, pickup affordances, interaction prompts, objective volumes, trigger volumes, damage volumes, aura volumes, faction-buff volumes, gameplay collision, cloth physics setup, wind setup, destructible states, or implementation-specific files.

## Texture and Material Notes

Target material strategy for possible future source work:

- Default material count: 1 shared Blood Axe moved-camp stone/cloth material.
- Maximum material count: 2 only if a later approved art pass separates stone/base from cloth/rawhide accents.
- Default texture resolution: 1K BC/N/ORM for repeated static dressing.
- 512 can be acceptable for distant repeated dressing if atlas reuse is prioritized.
- 2K is acceptable only if a separate later task promotes the prop to close-view focal dressing.
- No default emissive map.

Future texture names if a unique texture set is separately approved:

- `T_GIA_BloodAxeMovedCampClothStoneTie_A01_BC`
- `T_GIA_BloodAxeMovedCampClothStoneTie_A01_N`
- `T_GIA_BloodAxeMovedCampClothStoneTie_A01_ORM`

`T_GIA_BloodAxeMovedCampClothStoneTie_A01_E` must not be created for the baseline asset. Emissive, active ritual, signal, torch, magic, faction-buff, UI-readable, message-readable, VFX, or gameplay-state variants are outside this package.

Texture guidance:

- Base Color should carry broad stone value changes, soot staining, cold ash, mud buildup, faded oxide red cloth, rawhide/rope warmth, and optional old iron darkness.
- Normal should carry stone cracks, chipped edges, cloth weave, fray, compressed cloth folds, rope fibers, lichen specks, mud ridges, and shallow pitting.
- ORM should emphasize occlusion under the stone, buried cloth edges, tight wrap overlaps, ash pockets, mud recesses, and rope contact if present.
- Roughness should stay high across stone, ash, mud, cloth, hide, rope, and old iron.
- Metallic should remain near zero except for rare blackened iron scraps.

Avoid unique materials for each stone chip, crack, ash patch, mud smear, cloth fold, rope tie, lichen spot, paint mark, or iron fleck. Avoid readable text, UI-color masks, faction-buff masks, objective-highlight masks, active ritual masks, and animated material masks.

## Triangle Budget

- Target category: small static prop, Giant-scaled environmental dressing.
- LOD0 target: 600-2.5k tris total.
- LOD0 hard upper limit: 4k tris only if a later approved focal variant adds broader grounding and a more complex fixed wrap silhouette.
- LOD1 target: 300-1.2k tris.
- LOD2 target: 120-550 tris.
- LOD3 target: 50-180 tris.
- Material budget: 1 material target, 2 maximum.
- Texture budget: 1K BC/N/ORM by default; no baseline emissive texture.

Spend geometry on the dominant stone silhouette, broad chipped planes, contact bevels, fixed cloth outline, major cloth folds that affect silhouette, one simple knot or pinched area if needed, and the broad grounding base. Do not spend geometry on tiny cracks, soot speckles, ash flecks, cloth weave, thread fray, rope fibers, lichen, mud flecks, small scratches, chipped paint, hidden underside detail, or micro debris.

The triangle budget is a future planning range only. It does not authorize DCC work, FBX export, Unreal import, implementation target selection, runtime validation, collision correctness, final approval, source movement, or Hermes work.

## LOD Plan

All future important static meshes require LOD0, LOD1, LOD2, and LOD3 before any separately approved shipping use.

- LOD0: full low cloth-stone silhouette, dominant rough stone, fixed tied or trapped oxide red cloth, broad chipped planes, tight wrap or trapped flap shape, and optional low ash/mud grounding.
- LOD1: 55-70 percent of LOD0; reduce secondary bevels, small chips, cloth edge cuts, knot subdivisions, underside cuts, minor mud forms, and hidden backside detail while preserving the fixed cloth-stone read.
- LOD2: 30-45 percent of LOD0; simplify the stone into larger planes, flatten cloth folds, merge grounding forms, remove non-silhouette rope or iron accents, and retain one subdued oxide red cloth read.
- LOD3: 10-25 percent of LOD0; preserve the low stone mass and one controlled red cloth patch only if needed for Blood Axe identity.

Reduction order:

1. Tiny cracks, soot speckles, ash flecks, lichen specks, cloth weave, rope fibers, fray cuts, chipped paint, and minor scratches.
2. Small knot cuts, cloth edge tears, tiny wedges, old iron nicks, and non-silhouette rope/rawhide detail.
3. Back-facing contacts, hidden underside bevels, buried base cuts, and non-visible mud undercuts.
4. Optional accent pieces, duplicate cloth folds, secondary chip planes, and small grounding geometry.
5. Stone bevel density, cloth fold geometry, and minor base-plane subdivisions.
6. Only after small detail is removed, simplify the primary stone and fixed cloth silhouette.

Never reduce Giant-scale readability, the abandoned moved-camp residue, the fixed cloth pinned by stone, the low non-marker footprint, or the Blood Axe/neutral Giant culture separation before removing small detail.

## Collision Notes

This package creates no collision asset, collision proxy, UCX mesh, Unreal collision setting, physics body, nav blocker, smart link, gameplay volume, trigger volume, damage volume, aura volume, objective volume, interaction volume, faction-buff volume, validator script, runtime setup, or collision correctness claim.

Collision guardrails:

- Static dressing only; no collision correctness is approved or claimed.
- Collision disabled should be the baseline assumption for planning discussion only.
- If a later implementation task requires simple contact, it must separately approve one primitive hull around the largest stone mass.
- Cloth, rope, rawhide, ash, soot, mud, lichen, paint, old iron scraps, tiny chips, thread fray, and texture-only detail should never drive collision.
- Do not use per-cloth, per-rope, per-chip, per-ash, per-mud, per-paint, complex-as-simple, physics, destructible, cover, combat, pickup, route, waypoint, objective, trigger, interaction, damage, aura, faction-buff, spawn, patrol, or ritual-boundary collision.

This package makes no claim of terrain integration, route clearance, player movement validity, camera clearance, pickup reach, interaction reach, collision correctness, runtime performance validation, or implementation readiness.

## Animation Notes

The baseline asset is static.

Allowed planning language:

- Static mesh prop only.
- Fixed stone, fixed cloth, ash, mud, rope, rawhide, and optional old iron silhouettes if a later source task is approved.
- Static material wear variation may be considered by a later material task, but no material animation is included here.

Not authorized:

- Skeletal animation, cloth simulation, vertex wind, wind response, rope physics, swaying cloth, fluttering cloth, collapse states, destruction, physics settling, material pulses, ritual activation, VFX, audio, UI feedback, readable message behavior, faction buff behavior, objective state, waypoint behavior, breadcrumb behavior, trail gameplay, tracking behavior, navigation behavior, pickup behavior, loot behavior, salvage behavior, interaction behavior, damage/aura behavior, encounter behavior, AI behavior, spawn behavior, patrol behavior, startup placement, runtime behavior, Hermes work, or gameplay behavior.

Any moving, glowing, interactive, pickup-readable, objective-readable, waypoint-readable, UI-readable, message-readable, buff-granting, damaging, aura-emitting, audio-linked, wind-reactive, cloth-simulated, or VFX version must be split into a separately named and approved package.

## Unreal Import Notes

This section is a guardrail only. No Unreal asset, Content folder, import script, material instance, texture asset, socket, Blueprint, validator, runtime source, review actor, startup actor, placement file, DCC source, FBX export, collision setup, navigation setup, trigger setup, objective setup, quest/UI setup, interaction setup, faction-buff setup, material graph, VFX, audio, final approval, or implementation target is created, selected, or authorized.

No first implementation target is selected by this package. No candidate Unreal folder is created or approved by this package.

If a later separate task authorizes implementation, it must re-confirm:

- Asset name: `SM_GIA_BloodAxeMovedCampClothStoneTie_A01`
- Asset type: Static Mesh
- Naming convention: `SM_GIA_BloodAxeMovedCampClothStoneTie_A01`, `MI_GIA_BloodAxeMovedCampClothStoneTie_A01`, `T_GIA_BloodAxeMovedCampClothStoneTie_A01_BC`, `T_GIA_BloodAxeMovedCampClothStoneTie_A01_N`, `T_GIA_BloodAxeMovedCampClothStoneTie_A01_ORM`
- Pivot: ground center under the stone and cloth footprint, if source is later approved.
- Orientation: strongest readable cloth-stone side faces +X unless a later DCC/export task confirms a different convention.
- Scale: centimeter-authored source, imported at scale 1.0, preserving female 442 cm / 14 ft 6 in and male 470 cm / 15 ft 5 in Giant baselines.
- Collision type: not approved here; no collision correctness claim.
- LOD plan: LOD0-LOD3 required before any shipping use.
- Material slot count: 1 target, 2 maximum.
- Texture list: BC, N, and ORM only by default; no baseline emissive.
- Sockets: none.
- Animation list: none.
- Blueprint behavior: none.
- Performance notes: low material count, shared Blood Axe stone/cloth material language, aggressive LOD reduction, disabled collision on cloth/detail, no cloth simulation, no wind, and instancing for repeated static use.

These notes are not Unreal work authorization. They do not permit source asset creation, DCC, FBX, import, Content edits, startup placement, validator work, final visual approval, source concept movement, Hermes work, or implementation target selection.

## Folder and Naming Recommendation

Documentation path created by this task:

- `docs/assets/props/SM_GIA_BloodAxeMovedCampClothStoneTie_A01/PRODUCTION_PACKAGE.md`

Future asset naming references, for planning only:

- Static mesh: `SM_GIA_BloodAxeMovedCampClothStoneTie_A01`
- Material instance: `MI_GIA_BloodAxeMovedCampClothStoneTie_A01`
- Base color: `T_GIA_BloodAxeMovedCampClothStoneTie_A01_BC`
- Normal: `T_GIA_BloodAxeMovedCampClothStoneTie_A01_N`
- ORM: `T_GIA_BloodAxeMovedCampClothStoneTie_A01_ORM`

Related planning references:

- Parent moved-camp cairn-line kit: `docs/assets/kits/KIT_GIA_BloodAxeMovedCampCairnLine_A01/`
- Parent child row: `BloodAxeRitualStones_A01#MovedCamp_ClothRemnantStoneTie_A01`

Do not create DCC, FBX, Unreal, material, texture, validator, runtime, startup, source folder, source concept, final approval, implementation target, global docs, task-board, backlog, bootstrap, approval queue, or Hermes files from this package without a separate approved task.

## Quality Gate Checklist

- Required universal package headings are present in the requested order.
- Package remains docs-only and changes no DCC source, FBX export, Unreal asset, runtime source, startup scene, external concept, source concept movement, validator, material instance, texture asset, VFX/audio asset, Hermes work, global index, task board, backlog, bootstrap, approval queue, or unrelated package file.
- Asset reads as fixed oxide red cloth tied around or trapped under a low cairn stone.
- Cloth remains static and fixed, with no cloth simulation, wind response, vertex wind, rope physics, flutter, or material animation.
- Cloth color remains a subdued Blood Axe residue beat, not UI color coding, objective color coding, faction buff language, route highlighting, or a readable message.
- Asset remains environmental history only and does not imply a functional trail, waypoint, breadcrumb, tracking mechanic, UI path, objective logic, navigation aid, patrol marker, spawn marker, encounter lane, pickup, loot, salvage, interaction behavior, or active ritual state.
- Blood Axe remains a hostile Giant sub-faction only and is separate from neutral/civilized Giant culture.
- Giant scale lock is explicit: female 442 cm / 14 ft 6 in and male 470 cm / 15 ft 5 in; approved Giant ranges are females 14-15 ft and males 14 ft 10 in-16 ft.
- Materials stay on rough highland stone, soot, ash, mud, fixed oxide red cloth, rawhide, rope, and sparse blackened iron only if needed.
- No blue-gray civic masonry, refined cave-town carving, terrace/waterwork motifs, warm hearth settlement language, peaceful highland markers, restrained blue runes, or neutral/civilized Giant craft identity is used as Blood Axe default language.
- No default emissive, active glow, VFX, audio, UI feedback, message behavior, or gameplay-readable state is defined.
- Tiny cracks, cloth weave, fray, soot speckles, ash flecks, mud streaks, lichen, rope fibers, and small scratches are reserved for future texture, normal, AO, or mask detail.
- LOD0-LOD3, material count, texture list, collision guardrails, animation guardrails, and Unreal import guardrails are included as planning notes only.
- No source folders, DCC files, Unreal files, validators, images, material instances, texture assets, external source concept movement, global docs, task board, backlog, bootstrap, approval queue, or other workers' package files are edited by this task.
- The package does not select a first implementation target, does not claim final visual approval, and does not authorize startup placement.
